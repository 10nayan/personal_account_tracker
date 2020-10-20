from django.urls import path,include
from .views import ReportDetailView,ReportCreateView,ReportUpdateView,ReportDeleteView,index,signin,signout,register,weather
urlpatterns = [
    path("",index,name='list'),
    path("<int:pk>",ReportDetailView.as_view(),name='detail'),
    path("create",ReportCreateView.as_view(),name='create'),
    path('<int:pk>/update',ReportUpdateView.as_view(),name='update'),
    path('<int:pk>/delete',ReportDeleteView.as_view(),name='delete'),
    path('register',register,name='register'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),
    path('weather',weather,name='weather')

]