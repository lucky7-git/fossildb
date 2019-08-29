# Generated by Django 2.1.2 on 2019-08-27 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20190825_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='作成時間'),
        ),
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CreatedBy', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='更新時間'),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UpdatedBy', to=settings.AUTH_USER_MODEL, verbose_name='更新者'),
        ),
    ]