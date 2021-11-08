from django.db import models


class Heading(models.Model):
    title = models.CharField(max_length=100)
    name_pattern = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "%s_%s" % (self.id, self.title)


class Category(models.Model):
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name_pattern = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "%s_%s" % (self.id, self.title)


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name_pattern = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "%s_%s" % (self.id, self.title)


class Item_model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name_pattern = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "%s_%s" % (self.id, self.title)
