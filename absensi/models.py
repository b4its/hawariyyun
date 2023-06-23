from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
status = (
	(1,'Hadir'),
	(2,'Izin'),
    (3,'Tidak Hadir'),
)



class kegiatan(models.Model):
    nama_kegiatan = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.nama_kegiatan}'

class absensi_kehadiran(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='problem' , blank = True , null = True )
    kegiatan = models.ForeignKey(kegiatan, on_delete = models.CASCADE,related_name = 'items')
    status = models.IntegerField(choices = status ,default=1)
    keterangan = models.CharField(max_length=5000,blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name},  {self.kegiatan}, {self.date_posted} '
    