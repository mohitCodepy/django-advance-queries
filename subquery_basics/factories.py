import factory
import random

from .models import Category, Hero

'''
Factory to create models objects instantly.
'''


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'Category %02d' % n)


class HeroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hero

    name = factory.Sequence(lambda n: 'Hero %02d' % n)
    category = factory.SubFactory(CategoryFactory)
    benevolence_factor = factory.LazyAttribute(random.randrange(25, 100))