from __future__ import unicode_literals

import datetime

from django.contrib.auth.admin import User
from django.db import migrations


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@example.com'
    superuser.set_password('password1')
    superuser.last_login = datetime.datetime.now()
    superuser.save()


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
