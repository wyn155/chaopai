# Generated by Django 2.2.7 on 2019-12-05 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20191204_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attrchoice',
            name='name',
        ),
        migrations.AddField(
            model_name='attrchoice',
            name='color',
            field=models.CharField(default='', max_length=20, verbose_name='规格选项颜色'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attrchoice',
            name='size',
            field=models.CharField(default='', max_length=20, verbose_name='规格选项尺寸'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attrchoice',
            name='attr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attr', to='polls.Attr', verbose_name='类目规格'),
        ),
    ]