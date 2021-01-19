from django.db import models

# Create your models here.
class Alliance(models.Model):
    name = models.CharField('Фракция', max_length = 50)
    info = models.TextField('Краткая информация', default = "-")
    back_c = models.CharField('Цвет фона', default = "antiquewhite", max_length = 50)
    font_c = models.CharField('Цвет текста', default = "black", max_length = 50)

    def __str__(self):
        return self.name

class Country(models.Model):
    ally_id = models.ForeignKey(Alliance, on_delete=models.CASCADE)
    name = models.CharField('Страна', max_length = 50)
    flag = models.ImageField(upload_to = 'flags')
    info = models.TextField('Краткая информация')
    population = models.FloatField('Население')
    area = models.FloatField('Площадь')

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField('Техника', max_length = 50)
    info = models.TextField('Краткая информация', default = "-")
    users = models.ManyToManyField(Country)

    def __str__(self):
        return self.name