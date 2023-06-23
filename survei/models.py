from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

jenis = (
	(1,'Minat dan Bakat'),
	(2,'Tujuan dan Harapan'),
	(3,'Informasi Tambahan')
) 



class jawaban_pilgan(models.Model):
    jawab = models.CharField(blank=True,null=True,max_length = 500)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__ (self):
        return f'{self.jawab}'
        

class survei(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,related_name='jawabku' , blank = True , null = True )
    nomor1 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor2 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor3 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor4 = models.ForeignKey(jawaban_pilgan, on_delete= models.CASCADE,verbose_name="jawab",related_name='jawaban_pilgan' , blank = True , null = True )
    nomor5 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor6 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor7 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor8 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor9 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor10 = models.TextField(blank=True,null=True,max_length = 1000)
    nomor11 = models.TextField(blank=True,null=True,max_length = 1000)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return f' {self.user}'
