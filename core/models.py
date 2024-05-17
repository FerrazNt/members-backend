from django.db import models

# Create your models here.
class Member(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    addres = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='members_profile', blank=True, null=True )

    def __str__(self):
        return self.nome + " " + self.sobrenome
    
