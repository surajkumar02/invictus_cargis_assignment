from django.urls import path
from .views import Item,ItemList,ItemRadius,ItemSort
urlpatterns = [
    path('getitem/',Item.as_view()),
    path('getsorteddata/',ItemSort.as_view()),
    path('getitemlist/',ItemList.as_view()),
    path('getiteminradius/',ItemRadius.as_view()),
]