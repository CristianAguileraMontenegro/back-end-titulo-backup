# Generated by Django 4.1.2 on 2023-06-05 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_customessay_remove_essay_is_custom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essayanswer',
            name='essays',
        ),
        migrations.AddField(
            model_name='essayanswer',
            name='essay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='essay_answer', to='api.essay'),
        ),
        migrations.AlterField(
            model_name='essayanswer',
            name='custom_essay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='essay_custom', to='api.customessay'),
        ),
    ]
