# Generated by Django 2.2.7 on 2019-12-04 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='规格名称')),
            ],
            options={
                'verbose_name': '类目规格',
                'verbose_name_plural': '类目规格',
                'db_table': 'attr',
            },
        ),
        migrations.CreateModel(
            name='AttrChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='规格选项名称')),
                ('attr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Attr', verbose_name='类目规格')),
            ],
            options={
                'verbose_name': '类目规格选项',
                'verbose_name_plural': '类目规格选项',
                'db_table': 'attrchoice',
            },
        ),
        migrations.CreateModel(
            name='Exhausted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
            ],
            options={
                'verbose_name': '库存管理',
                'verbose_name_plural': '库存管理',
                'db_table': 'exhausted',
            },
        ),
        migrations.CreateModel(
            name='ExhaustedAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Attr')),
                ('attrchoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.AttrChoice', verbose_name='规格选项')),
                ('exhausted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Exhausted')),
            ],
        ),
        migrations.CreateModel(
            name='OrderAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhausted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Exhausted')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AttrChoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.AttrChoice')),
                ('attr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Attr')),
                ('exhausted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Exhausted')),
            ],
            options={
                'verbose_name': '详情表',
                'verbose_name_plural': '详情表',
                'db_table': 'page',
            },
        ),
        migrations.RemoveField(
            model_name='categoryvalue',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='categoryvalue',
            name='cpid',
        ),
        migrations.RemoveField(
            model_name='goodsvalue',
            name='gid',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='gid',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '类目', 'verbose_name_plural': '类目'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品管理', 'verbose_name_plural': '商品管理'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单表', 'verbose_name_plural': '订单表'},
        ),
        migrations.AlterModelOptions(
            name='shopcar',
            options={'verbose_name': '购物车', 'verbose_name_plural': '购物车'},
        ),
        migrations.RemoveField(
            model_name='goods',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='color',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='num',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='size',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='style',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='time',
        ),
        migrations.RemoveField(
            model_name='shopcar',
            name='total',
        ),
        migrations.AddField(
            model_name='category',
            name='father',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Category', verbose_name='父id'),
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Category', verbose_name='类目'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_id',
            field=models.CharField(default='', max_length=10, verbose_name='商品编码'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='info',
            field=models.CharField(default='', max_length=200, verbose_name='商品简介'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcar',
            name='num',
            field=models.IntegerField(default=0, verbose_name='购买数量'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='类目名称'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='img',
            field=models.ImageField(upload_to='goods', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=20, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='order',
            name='gid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Goods'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Pay', verbose_name='支付方式'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Status', verbose_name='状态'),
        ),
        migrations.DeleteModel(
            name='Categoryproperties',
        ),
        migrations.DeleteModel(
            name='Categoryvalue',
        ),
        migrations.DeleteModel(
            name='Goodsvalue',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='page',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='orderattr',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Order'),
        ),
        migrations.AddField(
            model_name='exhausted',
            name='attr',
            field=models.ManyToManyField(through='polls.ExhaustedAttr', to='polls.Attr'),
        ),
        migrations.AddField(
            model_name='exhausted',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='attr',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate', to='polls.Category', verbose_name='类目'),
        ),
        migrations.AddField(
            model_name='order',
            name='exhausted',
            field=models.ManyToManyField(through='polls.OrderAttr', to='polls.Exhausted'),
        ),
    ]
