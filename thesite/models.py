from django.db import models


class Conglomerate(models.Model):  # But each Conglomerate can make many products
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    last_updated = models.DateField()
    num_stars = models.IntegerField() # out of five
    approved_edit = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    pass


class Cert(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

    pass


class Product(models.Model):  # Each product has one Conglomerate
    conglomerate = models.ForeignKey(Conglomerate, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    last_updated = models.DateField()
    num_stars = models.IntegerField() # out of five
    approved_edit = models.BooleanField(default=False)

    certificatons = models.ManyToManyField(Cert, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
