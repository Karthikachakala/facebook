from django.db import models

class create(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date=models.DateTimeField('auto_now_add=TRUE')
    caption=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.caption



# Create your models here.
