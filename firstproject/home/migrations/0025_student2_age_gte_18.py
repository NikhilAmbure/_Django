# Generated by Django 5.1.1 on 2025-04-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_mymodel'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='student2',
            constraint=models.CheckConstraint(condition=models.Q(('age__gte', 18)), name='age_gte_18'),
        ),
    ]
