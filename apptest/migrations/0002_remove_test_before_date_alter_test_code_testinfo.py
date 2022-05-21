# Generated by Django 4.0.4 on 2022-05-22 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='before_date',
        ),
        migrations.AlterField(
            model_name='test',
            name='code',
            field=models.CharField(help_text='ex)일련번호', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='TestInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptest.test')),
            ],
        ),
    ]
