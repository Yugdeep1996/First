from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Django_app.views import *

router = DefaultRouter()

router.register(r'ifsc_search', Ifsc_viewset, basename='Ifsc_viewset')
router.register(r'bank_leader_board', Bank_leader_board_Viewset, basename='Bank_leader_board_Viewset')
router.register(r'statistics', Statistics_viewset, basename='Statistics_viewset')
router.register(r'api_count', Api_count_viewset, basename='Api_count_viewset')
router.register(r'ifsc_count', Ifsc_count_viewset, basename='Ifsc_count_viewset')

urlpatterns = [
    path('', include(router.urls)),
]
