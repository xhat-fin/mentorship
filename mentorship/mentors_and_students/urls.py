from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('mentors/', views.get_mentors, name = 'mentors'),
    path('mentors/<int:id>', views.get_mentors_by_id, name = 'get_mentors_by_id'),
    path('students/', views.get_students, name = 'students'),
    path('students/<int:id>', views.get_student_by_id, name = 'get_student_by_id'),
    path('meetings/', views.get_meetings, name = 'meetings'),
    path('bids/', views.get_bids, name = 'bids'),
]
