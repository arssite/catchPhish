from django.urls import path, re_path, include
from . import views


urlpatterns = [
    re_path('auth/', include('drf_social_oauth2.urls')),
    # path('delay/', views.delay),
    path('detect/', views.DetectView.as_view()),
    path('signup/', views.SignUPView.as_view()),
    path('report/', views.ReportView.as_view()),
    path('stats/', views.StatsUserView.as_view()),
]