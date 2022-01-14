from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Century(models.Model):
    century = models.CharField(max_length=100)
    sum_madrasa = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.century


class Madrasa(models.Model):
    name = models.CharField(max_length=100)
    relevant_century = models.ForeignKey(Century, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.name) + ' ' + str(self.relevant_century.century)


class AllomaMenu(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title

# def nameImage(instance, imagename):
#     return '/'.join(['images', str(instance.name), imagename])

class Alloma(models.Model):
    name = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=30, null=True)
    birth_area = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images')
    madrasa_alloma = models.ForeignKey(Madrasa, on_delete=models.PROTECT)
    about = models.TextField(null=True)
    allomamenu = models.ManyToManyField(AllomaMenu, null=True)

    def __str__(self) -> str:
        return self.name
