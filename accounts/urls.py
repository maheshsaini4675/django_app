from django.contrib import admin
from accounts.models import Post
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("create_post/", views.create_post, name="create_post"),
    path("delete/<int:id>", views.delete_post, name="delete_post"),
    path("update/<int:id>/", views.update_post, name="update_post"),
    # path("contact/", views.contact_form, name="contact_form"),
    path('contact/',views.contact_view, name="contact_view"),
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)