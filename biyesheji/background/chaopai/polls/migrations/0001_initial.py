# Generated by Django 2.2.7 on 2019-12-03 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaid', models.CharField(max_length=6, verbose_name='区县编码')),
                ('area', models.CharField(max_length=40, verbose_name='区县名称')),
            ],
            options={
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类名')),
            ],
            options={
                'verbose_name_plural': '类目表',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Categoryproperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='类目属性名')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category', verbose_name='类名')),
            ],
            options={
                'verbose_name_plural': '类目属性表',
                'db_table': 'categoryproperties',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityid', models.CharField(max_length=6, unique=True, verbose_name='城市编码')),
                ('city', models.CharField(max_length=40, verbose_name='城市名称')),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='商品名')),
                ('describe', models.CharField(max_length=200, verbose_name='描述')),
                ('img', models.CharField(max_length=200, verbose_name='图片')),
                ('style', models.CharField(max_length=20, verbose_name='样式')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('color', models.CharField(max_length=20, verbose_name='颜色')),
                ('size', models.CharField(max_length=20, verbose_name='尺码')),
                ('price', models.CharField(max_length=20, verbose_name='价格')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category', verbose_name='类目id')),
            ],
            options={
                'verbose_name_plural': '商品表',
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.CharField(max_length=20, verbose_name='支付方式')),
            ],
            options={
                'verbose_name': '支付方式表',
                'verbose_name_plural': '支付方式表',
                'db_table': 'pay',
            },
        ),
        migrations.CreateModel(
            name='Provincial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceid', models.IntegerField(unique=True, verbose_name='省编码')),
                ('province', models.CharField(max_length=100, verbose_name='省')),
            ],
            options={
                'db_table': 'provinces',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, verbose_name='状态')),
            ],
            options={
                'verbose_name': '状态表',
                'verbose_name_plural': '状态表',
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='admin', max_length=20, verbose_name='用户名')),
                ('password', models.CharField(default='admin', max_length=20, verbose_name='密码')),
                ('name', models.CharField(default='abc', max_length=20, verbose_name='昵称')),
                ('reg_time', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('real', models.CharField(default='abc', max_length=20, verbose_name='真实姓名')),
                ('birth', models.CharField(default='1996-08-10', max_length=20, verbose_name='生日')),
                ('sex', models.CharField(default='男', max_length=20, verbose_name='性别')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('Provincial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Provincial', verbose_name='省')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Area', verbose_name='区/县')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.City', verbose_name='市')),
            ],
            options={
                'verbose_name_plural': '用户',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=20, verbose_name='库存')),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Goods', verbose_name='商品id')),
            ],
            options={
                'verbose_name_plural': '库存表',
                'db_table': 'stock',
            },
        ),
        migrations.CreateModel(
            name='Shopcar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='数量')),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Goods', verbose_name='商品id')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Users', verbose_name='用户id')),
            ],
            options={
                'verbose_name_plural': '购物车',
                'db_table': 'shopcar',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.CharField(max_length=20, verbose_name='订单号')),
                ('status', models.CharField(max_length=20, verbose_name='状态')),
                ('pay', models.CharField(max_length=20, verbose_name='支付方式')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='下单时间')),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Goods', verbose_name='商品id')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Users', verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '订单表',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Goodsvalue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='颜色')),
                ('size', models.CharField(max_length=20, verbose_name='尺码')),
                ('price', models.CharField(max_length=20, verbose_name='价格')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Goods', verbose_name='商品id')),
            ],
            options={
                'verbose_name_plural': '商品属性表',
                'db_table': 'goodsvalue',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='provinceid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Provincial', to_field='provinceid'),
        ),
        migrations.CreateModel(
            name='Categoryvalue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类目属性值名')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category', verbose_name='类目id')),
                ('cpid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Categoryproperties', verbose_name='类目属性名')),
            ],
            options={
                'verbose_name_plural': '类目属性值表',
                'db_table': 'categoryvalue',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='cityid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.City', to_field='cityid'),
        ),
    ]