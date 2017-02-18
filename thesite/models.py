from django.db import models
from django.utils import timezone

class Conglomerate(models.Model):  # But each Conglomerate can make many products
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    sustainability = models.CharField(max_length=1000, blank=True)
    employees = models.CharField(max_length=1000, blank=True)
    last_updated = models.DateTimeField(default=timezone.now)
    num_stars = models.IntegerField() # out of five
    approved_edit = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    """ Maybe this is useful one day?
    def update(self):
        self.last_updated = timezone.now()
        self.save()
    """
    class Meta:
        ordering = ('name', '-last_updated')

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
    sustainability = models.CharField(max_length=1000, blank=True)
    employees = models.CharField(max_length=1000, blank=True)
    last_updated = models.DateTimeField(default=timezone.now)
    num_stars = models.IntegerField() # out of five
    approved_edit = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', '-last_updated')

    pass


class Verification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    conglomerate = models.ForeignKey(Conglomerate, on_delete=models.CASCADE, null=True)

    individual = models.CharField(max_length=100, default="", null=True)
    date = models.DateTimeField(default=timezone.now)
    who = models.CharField(max_length=1000, default="", null=True)
    comment = models.CharField(max_length=1000, default="", null=True)
    comment_sustain = models.CharField(max_length=1000, default="", null=True)
    comment_employ = models.CharField(max_length=1000, default="", null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.individual
