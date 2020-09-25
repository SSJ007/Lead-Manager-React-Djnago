

from django.db import migrations

def create_data(apps, schema_editor):
    Lead = apps.get_model('leads', 'Lead')
    Lead(name="Joe Silver", email="joe@email.com", document="22342342", phone="00000000").save()


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20200925_1521'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
