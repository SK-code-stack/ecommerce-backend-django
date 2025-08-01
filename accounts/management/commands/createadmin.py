from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a default admin user'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='adminpass123'
            )
            self.stdout.write(self.style.SUCCESS('✅ Superuser created: admin/adminpass123'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Superuser already exists'))
