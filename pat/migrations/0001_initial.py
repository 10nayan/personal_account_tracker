# Generated by Django 3.1.2 on 2020-10-19 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
                ('date', models.DateField()),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('food', 'food'), ('health', 'health'), ('transport', 'transport'), ('utilities', 'utilities'), ('other', 'other')], max_length=37)),
                ('profileLinked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
