from django.db import models


class Seeds(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(blank = True, null=True)
    image = models.ImageField(upload_to="seeds", null=True, blank=True)


    def __str__(self):
        return f'{self.name} --'