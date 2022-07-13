
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugTrackerApp', '0011_extendeduser_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='nickname',
        ),
    ]
