# Generated by Django 3.0.5 on 2020-05-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=50)),
                ('amount_send', models.DecimalField(decimal_places=2, max_digits=19)),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=19)),
                ('sent_date', models.DateField()),
                ('channel', models.CharField(max_length=50)),
                ('rates', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
    ]