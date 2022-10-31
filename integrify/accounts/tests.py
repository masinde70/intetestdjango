
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class CustomTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username = "masinde", email = "masinde@your-email.com",password = 
            "test123",
        )
        self.assertEqual(user.username, "masinde")
        self.assertEqual(user.email, " masinde@your-email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    