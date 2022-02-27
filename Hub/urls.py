from django.urls import path
from .views import homePage, list_Students, details_Student

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStudents', list_Students, name='Student_list'),
    path('Student/<int:id>', details_Student, name='Student_details'),
]
