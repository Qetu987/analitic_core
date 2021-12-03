from django.db import models
from django.db.models import query
from django.db.models.query_utils import select_related_descend
from main.models import (
    Heading,
    Category,
    Type,
    Brand,
    Item_model,
)

from bot_office.bot import Olx_Parser


class Olx_items(models.Model):
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    item_model = models.ForeignKey(Item_model, on_delete=models.CASCADE, null=True)
    total = models.CharField(max_length=200, default=0)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return "%s_%s" % (self.id, self.item_model)


    def save(self, *args, **kwargs):
        bot_result = Olx_Parser(
            heading=self.heading,
            category=self.category,
            type=self.type,
            brand=self.brand,
            item_model=self.item_model,
            id=self.id
            )
        self.total = bot_result.average()
        examples = bot_result.first_three()
        for example in examples:
            obj = Olx_examples()
            obj.parent = self
            obj.title = example['title']
            obj.url = example['url']
            obj.cost = example['cost']
            obj.save()

        super(Olx_items, self).save(*args, **kwargs)


class Olx_examples(models.Model):
    parent = models.ForeignKey(Olx_items, on_delete=models.CASCADE)
    url = models.TextField()
    title = models.CharField(max_length=300)
    cost = models.CharField(max_length=100)


    def __str__(self):
        return "%s_%s" % (self.id, self.title)