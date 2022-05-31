from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path(r'^$', views.post_list, name='post_list'),  # post_views 라는 view가 ^$(^로 시작해 $로 끝나는 것) 에 할당
]
