from django.urls import path
from . import views



urlpatterns = [
    path('api/news', views.NewsList.as_view(),name=views.NewsList.name),# www.domainname.com/api/news
    path('api/news/<int:pk>', views.NewsDetail.as_view(),name=views.NewsDetail.name), # www.domanname.com/api/news/1

    path('api/entity', views.EntityList.as_view(), name=views.EntityList.name),  # www.domainname.com/api/entity
    path('api/entity/<int:pk>', views.EntityDetail.as_view(), name=views.EntityDetail.name),  # www.domanname.com/api/entity/1
]


