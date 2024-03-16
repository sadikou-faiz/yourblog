from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]

# Configuration des URL de médias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
