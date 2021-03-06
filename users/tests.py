from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'jon',
            email = 'jon@mail.ru',
            password = 'test'
        )
        self.assertEqual(user.username, 'jon')
        self.assertEqual(user.email, 'jon@mail.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
            
        admin_user = User.objects.create_superuser(
            username = 'superadmin',
            email = 'superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

