# Generated by Django 4.2.1 on 2023-05-15 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_rename_title_image_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('CANCELED', 'canceled'), ('DELIVERED', 'delivered')], default='PENDING', max_length=50)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders.orderitem')),
            ],
        ),
    ]
