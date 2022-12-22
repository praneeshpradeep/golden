from django.urls import path
from.import views
urlpatterns = [
    path('',views.home),
    path('chain/',views.chain),
path('anklet/',views.anklet),
path('earrings/',views.earrings),
]