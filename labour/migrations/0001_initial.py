# Generated by Django 2.0 on 2019-10-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('aadhar_num', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('rfid_num', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maindata',
            fields=[
                ('aadhar_num', models.BigIntegerField(primary_key=True, serialize=False)),
                ('rfid_num', models.BigIntegerField(default=0)),
                ('fullname', models.CharField(max_length=50)),
                ('f_name', models.CharField(max_length=50)),
                ('dist', models.CharField(default='Jabalpur', max_length=100)),
                ('tehseel', models.CharField(max_length=50)),
                ('janpad', models.CharField(max_length=50)),
                ('pincode', models.BigIntegerField()),
                ('village', models.CharField(max_length=50)),
                ('gram_panchayt', models.CharField(max_length=100)),
                ('f_contact', models.BigIntegerField()),
                ('s_contact', models.BigIntegerField()),
                ('experience', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
