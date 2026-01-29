from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post:/<int:pk>/", views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name='post_new'),
    path('signup/', SignUpView.as_view(), name='signup'),
]