from django.urls import path,include
from .views import ReportDetailView,ReportCreateView,ReportUpdateView,ReportDeleteView,index,signin,signout,register
urlpatterns = [
    path("",index,name='list'),
    path("<int:id>",ReportDetailView.as_view(),name='detail'),
    path("create",ReportCreateView.as_view(),name='create'),
    path('<int:pk>/update',ReportUpdateView.as_view(),name='update'),
    path('<int:id>/delete',ReportDeleteView.as_view(),name='delete'),
    path('register',register,name='register'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout')
]