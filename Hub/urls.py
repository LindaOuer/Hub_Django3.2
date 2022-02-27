from django.urls import path
from .views import homePage, list_Students

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStudents', list_Students, name='Student_list'),
]
