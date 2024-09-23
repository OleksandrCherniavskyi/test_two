from django.urls import path

from .views import index, articles_list, article_create, article_delete, article_update, article_detail, logout_view, login_view, register

urlpatterns = [
    path('login/', login_view, name='login'),  # Login view
    path('register/', register, name='register'),  # Registration view
    path('logout/', logout_view, name='logout'),  # Logout view
    path('', articles_list, name='articles_list'),  # List all articles
    path('article_create/', article_create, name='article_create'),  # Create a new article
    path('<slug:slug>/', article_detail, name='article_detail'),  # Detail view for specific article (using slug)

    path('<slug:slug>/update/', article_update, name='article_update'),  # Update an existing article
    path('<slug:slug>/delete/', article_delete, name='article_delete'),  # Delete an article
]