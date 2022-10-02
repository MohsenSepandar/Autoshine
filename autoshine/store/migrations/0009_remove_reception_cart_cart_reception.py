# Generated by Django 4.1.1 on 2022-09-29 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reception',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='reception',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.reception'),
        ),
    ]