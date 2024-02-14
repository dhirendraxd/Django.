from django.db import models

class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    recipe_image = models.ImageField(upload_to="receipe")

