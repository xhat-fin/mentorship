from django.urls import path
from .views import BidsAPIviewID, get_bids_by_id, get_bids, BidsAPIview

urlpatterns = [
    path('api/v1/bidslist/', BidsAPIview.as_view()),
    path('api/v1/bidslist/<int:id>', BidsAPIviewID.as_view()),
    path('view-bids/', get_bids, name='get_bids'),
    path('view-bids/<int:id>', get_bids_by_id, name='get_bids_by_id'),
]