from django.db import models

# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_number = models.IntegerField()
    comments = models.CharField(max_length = 200, blank =True)

    def __str__(self):
        return self.first_name + " " + self.last_name 


class Menu(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    description = models.CharField(max_length = 1000, default='None')
    image = models.ImageField(upload_to= 'menu_images/', default='littleLemon2.jpg')
#upload_to parameter specifies the subdirectory within your media directory where uploaded menu images will be stored. You can customize this to your liking, but it's common to use a folder structure like 'menu_images/'.
    def __str__(self):
        return self.name

