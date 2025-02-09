from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rango.models import Category, Page

class RangoTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', 
                                           password='testpass123')
        
        # Create a test category
        self.category = Category.objects.create(
            name='Test Category',
            views=10,
            likes=5
        )
        
        # Create a test page
        self.page = Page.objects.create(
            category=self.category,
            title='Test Page',
            url='http://www.test.com',
            views=5
        )

    def test_index_view(self):
        """Test the index view"""
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Crunchy, creamy, cookie, candy, cupcake!')
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_about_view(self):
        """Test the about view"""
        response = self.client.get(reverse('rango:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rango/about.html')

    def test_category_view(self):
        """Test the category detail view"""
        response = self.client.get(
            reverse('rango:show_category',
                   kwargs={'category_name_slug': self.category.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Category')
        self.assertContains(response, 'Test Page')

    def test_add_category_view_protected(self):
        """Test that add_category view requires login"""
        response = self.client.get(reverse('rango:add_category'))
        self.assertRedirects(response, 
            f'/accounts/login/?next={reverse("rango:add_category")}')

    def test_user_login(self):
        """Test user login functionality"""
        response = self.client.post(reverse('rango:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertRedirects(response, reverse('rango:index'))
