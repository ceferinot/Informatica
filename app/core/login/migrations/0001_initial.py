# Generated by Django 4.0.4 on 2022-05-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idname', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('procesador', models.CharField(choices=[('1', 'CELERON'), ('2', 'PENTIUM DUAL CORE'), ('3', 'CORE I3'), ('4', 'CORE I5'), ('5', 'CORE I5'), ('6', 'RAYZEN 3'), ('7', 'RAYZEN 5'), ('8', 'RAYZEN 7'), ('9', 'SEMPROM'), ('10', 'ATHOL X2'), ('11', 'RAYZEN 7')], max_length=20)),
                ('mem1_ram_type', models.CharField(choices=[('1', 'DDR1'), ('2', 'DDR2'), ('3', 'DDR3'), ('4', 'DDR4'), ('5', 'DDR5')], max_length=20)),
                ('mem1_ram_capacidad', models.CharField(choices=[('1', '512 MB'), ('2', '1 GB'), ('3', '2 GB'), ('4', '4 GB'), ('5', '8 GB')], max_length=20)),
                ('mem2_ram_type', models.CharField(choices=[('1', 'DDR1'), ('2', 'DDR2'), ('3', 'DDR3'), ('4', 'DDR4'), ('5', 'DDR5')], max_length=20)),
                ('mem2_ram_capacidad', models.CharField(choices=[('1', '512 MB'), ('2', '1 GB'), ('3', '2 GB'), ('4', '4 GB'), ('5', '8 GB')], max_length=20)),
                ('mem3_ram_type', models.CharField(choices=[('1', 'DDR1'), ('2', 'DDR2'), ('3', 'DDR3'), ('4', 'DDR4'), ('5', 'DDR5')], max_length=20)),
                ('mem3_ram_capacidad', models.CharField(choices=[('1', '512 MB'), ('2', '1 GB'), ('3', '2 GB'), ('4', '4 GB'), ('5', '8 GB')], max_length=20)),
                ('mem4_ram_type', models.CharField(choices=[('1', 'DDR1'), ('2', 'DDR2'), ('3', 'DDR3'), ('4', 'DDR4'), ('5', 'DDR5')], max_length=20)),
                ('mem4_ram_capacidad', models.CharField(choices=[('1', '512 MB'), ('2', '1 GB'), ('3', '2 GB'), ('4', '4 GB'), ('5', '8 GB')], max_length=20)),
                ('hdd1_type', models.CharField(choices=[('1', 'SSD'), ('2', 'HHD')], max_length=20)),
                ('hdd1_capacidad', models.CharField(choices=[('1', '160 GB'), ('2', '320 GB'), ('3', '500 GB'), ('4', '1TB GB'), ('5', '2TB GB')], max_length=20)),
                ('hdd2_type', models.CharField(choices=[('1', 'SSD'), ('2', 'HHD')], max_length=20)),
                ('hdd2_capacidad', models.CharField(choices=[('1', '160 GB'), ('2', '320 GB'), ('3', '500 GB'), ('4', '1TB GB'), ('5', '2TB GB')], max_length=20)),
                ('hdd3_type', models.CharField(choices=[('1', 'SSD'), ('2', 'HHD')], max_length=20)),
                ('hdd3_capacidad', models.CharField(choices=[('1', '160 GB'), ('2', '320 GB'), ('3', '500 GB'), ('4', '1TB GB'), ('5', '2TB GB')], max_length=20)),
                ('hdd4_type', models.CharField(choices=[('1', 'SSD'), ('2', 'HHD')], max_length=20)),
                ('hdd4_capacidad', models.CharField(choices=[('1', '160 GB'), ('2', '320 GB'), ('3', '500 GB'), ('4', '1TB GB'), ('5', '2TB GB')], max_length=20)),
                ('sistema_operativo', models.CharField(choices=[('1', 'WINDOWS 7 32 BIT '), ('2', 'WINDOWS 7 64 BIT'), ('3', 'WINDOWS 10 32 BTI'), ('4', 'WINDOWS 10 64 BIT'), ('5', 'LINUX')], max_length=20)),
                ('observacion', models.CharField(max_length=255)),
            ],
        ),
    ]
