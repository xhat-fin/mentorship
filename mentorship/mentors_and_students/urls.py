from django.urls import path
from . import views
from .views import MentorAPIview, StudentAPIview, StudentAPIviewID, MentorAPIviewID


urlpatterns = [
    path('', views.index, name = 'index'),
    path('mentors/', views.get_mentors, name = 'mentors'),
    path('mentors/<int:id>', views.get_mentors_by_id, name = 'get_mentors_by_id'),
    path('students/', views.get_students, name = 'students'),
    path('students/<int:id>', views.get_student_by_id, name = 'get_student_by_id'),

    #REST
    path('api/v1/mentorlist', MentorAPIview.as_view()),
    path('api/v1/studentslist', StudentAPIview.as_view()),
    path('api/v1/student/<int:id>', StudentAPIviewID.as_view()),
    path('api/v1/mentor/<int:id>', MentorAPIviewID.as_view()),
]
