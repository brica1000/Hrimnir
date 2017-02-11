from django.db import models
import datetime


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
    certificatons = models.ManyToManyField(Cert, blank=True)

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    last_updated = models.DateField()
    num_stars = models.IntegerField() # out of five
    approved_edit = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    pass


class Verification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #conglomerate = models.ForeignKey(Conglomerate, on_delete=models.CASCADE)

    individual = models.CharField(max_length=100, default="")
    date = models.DateField(default=datetime.date.today())
    who = models.CharField(max_length=1000, default="")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.individual
