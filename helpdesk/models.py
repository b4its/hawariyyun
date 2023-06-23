from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
status = (
	(1,'Diajukan'),
	(2,'Diproses'),
    (3,'Selesai'),
)
jenis = (
	(1,'Kritik'),
	(2,'Saran')
)


class kritik_saran(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='kritik_saran' , blank = True , null = True )
    jenis = models.IntegerField(choices = jenis)
    pembahasan = models.CharField(max_length=5000)
    status = models.IntegerField(choices = status ,default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    