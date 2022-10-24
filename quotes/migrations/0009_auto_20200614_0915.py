# Generated by Django 2.2.7 on 2020-06-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0008_auto_20200528_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='quality',
            field=models.CharField(choices=[('TE', 'Terrible'), ('BA', 'Bad'), ('OK', 'Neutral'), ('GO', 'Good'), ('EX', 'Excellent'), ('TB', 'Tba')], default='OK', max_length=2),
        ),
    ]