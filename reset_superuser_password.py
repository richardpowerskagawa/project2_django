import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project2.settings')  # Replace with your project name
django.setup()

from django.contrib.auth.models import User

# Replace 'your_superuser_username' with the actual username
user = User.objects.get(username='moto')  

# Set a new password
user.set_password('8837stst')  # Replace 'new_password' with your desired new password
user.save()

print(f"Password reset successful for superuser: {user.username}")
