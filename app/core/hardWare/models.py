from django.db import models

PROCESADOR_CHOICES = (
    ("1", "CELERON"),
    ("2", "PENTIUM DUAL CORE"),
    ("3", "CORE I3"),
    ("4", "CORE I5"),
    ("5", "CORE I5"),
    ("6", "RAYZEN 3"),
    ("7", "RAYZEN 5"),
    ("8", "RAYZEN 7"),
    ("9", "SEMPROM"),
    ("10", "ATHOL X2"),
    ("11", "RAYZEN 7"),
)
FRECUENCIA_PROCESADOR_CHOICES = (
    ("1", "1 GHZ"),
    ("2", "2 GHZ"),
    ("3", "3 GHZ"),
)
RAM_TYPE_CHOICES = (
    ("1", "DDR1"),
    ("2", "DDR2"),
    ("3", "DDR3"),
    ("4", "DDR4"),
    ("5", "DDR5"),
)
RAM_CAPACIDAD_CHOICES = (
    ("1", "512 MB"),
    ("2", "1 GB"),
    ("3", "2 GB"),
    ("4", "4 GB"),
    ("5", "8 GB"),
)
HDD_TYPE_CHOICES = (
    ("1", "SSD"),
    ("2", "HHD"),
    )
HDD_CAPACIDAD_CHOICES = (
    ("1", "160 GB"),
    ("2", "320 GB"),
    ("3", "500 GB"),
    ("4", "1TB GB"),
    ("5", "2TB GB"),
)
SO_TYPE_CHOICES = (
    ("1", "WINDOWS 7 32 BIT "),
    ("2", "WINDOWS 7 64 BIT"),
    ("3", "WINDOWS 10 32 BTI"),
    ("4", "WINDOWS 10 64 BIT"),
    ("5", "LINUX"),
)
class WorkStation(models.Model):

    idname=models.CharField(max_length=50) 
    serial_number= models.CharField(max_length=50)
    procesador= models.CharField(max_length=20,choices=PROCESADOR_CHOICES)
    mem1_ram_type=models.CharField(max_length=20,choices=RAM_TYPE_CHOICES)
    mem1_ram_capacidad=models.CharField(max_length=20,choices=RAM_CAPACIDAD_CHOICES)
    mem2_ram_type=models.CharField(max_length=20,choices=RAM_TYPE_CHOICES)
    mem2_ram_capacidad=models.CharField(max_length=20,choices=RAM_CAPACIDAD_CHOICES)
    mem3_ram_type=models.CharField(max_length=20,choices=RAM_TYPE_CHOICES)
    mem3_ram_capacidad=models.CharField(max_length=20,choices=RAM_CAPACIDAD_CHOICES)
    mem4_ram_type=models.CharField(max_length=20,choices=RAM_TYPE_CHOICES)
    mem4_ram_capacidad=models.CharField(max_length=20,choices=RAM_CAPACIDAD_CHOICES)
    hdd1_type=models.CharField(max_length=20,choices=HDD_TYPE_CHOICES)
    hdd1_capacidad =models.CharField(max_length=20,choices=HDD_CAPACIDAD_CHOICES)
    hdd2_type=models.CharField(max_length=20,choices=HDD_TYPE_CHOICES)
    hdd2_capacidad =models.CharField(max_length=20,choices=HDD_CAPACIDAD_CHOICES)
    hdd3_type=models.CharField(max_length=20,choices=HDD_TYPE_CHOICES)
    hdd3_capacidad =models.CharField(max_length=20,choices=HDD_CAPACIDAD_CHOICES)
    hdd4_type=models.CharField(max_length=20,choices=HDD_TYPE_CHOICES)
    hdd4_capacidad =models.CharField(max_length=20,choices=HDD_CAPACIDAD_CHOICES)
    sistema_operativo= models.CharField(max_length=20,choices=SO_TYPE_CHOICES)
    observacion=models.CharField(max_length=255)
    #user_responsable
    #user
    #date_creation=models.DateField(auto_now_add=True)
    #date_update=models.DateField(auto)
    #user_creation
    #user_update
