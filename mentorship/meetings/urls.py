from django.urls import path
from .views import MeetAPIview, MeetAPIviewID, get_meets, get_meets_by_id

urlpatterns = [
    path('api/v1/meetlist/', MeetAPIview.as_view()),
    path('api/v1/meetlist/<int:id>', MeetAPIviewID.as_view()),
    path('view-meets/', get_meets),
    path('view-meets/<int:id>', get_meets_by_id, name='get_meets_by_id'),
]
