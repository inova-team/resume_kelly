from django.contrib import admin
from django.urls import path

from landing import views

urlpatterns = [
    path('', views.renderHome, name="home"),
    path('about/', views.renderAbout, name="about"),
    path('short_bio/', views.renderShortBio, name="short_bio"),
    path('resume/', views.renderResume, name="resume"),
    path('research/', views.renderResearch, name="research"),
    path('projects/', views.renderProjects, name="projects"),
    path('contact/', views.renderContact, name="contact"),
    path('article_list/', views.renderArticle, name="article_list"),
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    path('contactanos/', views.renderContactUs_email, name="contact_us"),
]
