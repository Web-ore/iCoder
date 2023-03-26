from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHomeListView.as_view(), name="bloghome"),
    path('<str:slug>', views.blogPostDetailView, name="blogPost"),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),

]
