from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.management import call_command
import traceback

def setup_admin(request):
    try:
        call_command('migrate')
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='info@createstudiosleicester.co.uk',
                password='CreateSecureAdmin2025!'
            )
            return HttpResponse('✅ Superuser created! Go to /admin/ to log in.')
        return HttpResponse('⚠️ Admin already exists.')
    except Exception as e:
        return HttpResponse(f'<pre>{traceback.format_exc()}</pre>')
