"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>/', blog.views.detail, name="detail"),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create', blog.views.create, name='create'),
    path('blog/edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name="delete"),
    # project/urls.py
    path('blog/comment_add/<int:blog_id>', blog.views.comment_add, name="comment_add"),
    path('blog/comment_edit/<int:comment_id>', blog.views.comment_edit, name="comment_edit"),
    path('blog/comment_delete/<int:comment_id>', blog.views.comment_delete, name="comment_delete"),
    
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),

    path('accounts/signup/', accounts.views.signup, name='signup'),
    path('accounts/login/', accounts.views.login, name='login'),
    path('accounts/logout/', accounts.views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)