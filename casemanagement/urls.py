"""
URL configuration for casemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from legalcases import views 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("cases/", views.cases, name="cases"),
    path("cases/create/", views.createcase, name="createcase"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path('logout/', views.signout, name='logout'),
    path('cases/<int:case_id>', views.case_detail, name='case_detail'),
    path('cases/<int:case_id>/edit/', views.edit_case, name='edit_case'),
    path('cases/<int:case_id>/comment/', views.createcomment, name='create_comment'),
    path('cases/<int:case_id>/presentation/', views.createpresentation, name='create_presentation'),
    path('cases/<int:case_id>/upload_doc/', views.upload_doc, name='upload_doc'),
    path('delete/<int:pk>/', views.delete_doc, name="delete_doc"),
    path('cases/<int:case_id>/delete', views.delete_case, name='delete_case') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)