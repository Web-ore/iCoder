from django.urls import path, include
from ads.views import HA_Dashboard, TTA_Dashboard, SA_Dashboard,Ads_Create, Ads_Edit, Group


urlpatterns = [
    path('Homelist/', HA_Dashboard.as_view(), name='AdsList'),
    path('TTAlist/', TTA_Dashboard.as_view(), name='TopTipAdsList'),
    path('SAlist/', SA_Dashboard.as_view(), name='SearchAdsList'),
    # path('PAlist/', Ads_Dashboard.as_view(), name='PostAdsList'),
    path('Glist/', Group.as_view(), name='Group'),
    path('<str:grp>/create/', Ads_Create.as_view(), name='AdsCreate'),
    path('Edit/Ads/No.<int:pk>/', Ads_Edit.as_view(), name='AdsEdit'),

]