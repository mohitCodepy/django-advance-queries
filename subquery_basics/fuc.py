from django.db.models import F
from subquery_basics.models import Category, Hero
from subquery_basics.factories import CategoryFactory, HeroFactory
cat1=Category.objects.first()
cat2=Category.objects.last()