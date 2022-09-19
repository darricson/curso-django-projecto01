from django.urls import path
from recipies.views import home


urlpatterns = [
    path('home/', home),
]
