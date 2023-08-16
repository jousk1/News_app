from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_main, name='news_main'),
    path('add/', views.add_news, name='add_news'),
    path('edit_news/<int:news_id>', views.edit_news, name='edit_news'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('author/<int:author_id>', views.author_news, name='author_news'),
    path('delete/<int:news_id>/', views.delete_news, name='delete_news'),
    path('download/<int:news_id>', views.download_file, name='download_file')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)