from django.db.models import F, OuterRef, Subquery, Max
from .models import Category, Hero

'''
 How to find the most benevolent Hero?
'''

hero_qs = Subquery(Hero.objects.filter(category=OuterRef("id"))
                   .order_by("-benevolence_factor")             # applying descending ordering .
                   .values('name')[:1])                         # applying limit to get only first data.

'''
 Created a Subquery from a child 'Hero' to parent 'Category' class using 'OuterRef'.
 OuterRef references to a column in the database 
'''

Category.objects.all().annotate(most_benevolent_hero=hero_qs).values()

'''
Got expected output.
<QuerySet [{'id': 1, 'name': 'testing', 'most_benevolent_hero': 'dj Mohit'}
''' 
