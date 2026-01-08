from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Import untuk login/logout

urlpatterns = [
    # Halaman Utama
    path('', views.home_view, name='home'),
    
    # API Peta (Soulthan)
    path('api/schools/', views.school_data_api, name='school-data-api'),
    
    # Berita & Kegiatan
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    
    # Autentikasi (Register/Login/Logout)
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='locator/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # PPDB Online
    path('ppdb/dashboard/', views.ppdb_dashboard, name='ppdb_dashboard'),
    path('ppdb/apply/', views.ppdb_apply, name='ppdb_apply'),
    path('ppdb/success/', views.ppdb_success, name='ppdb_success'),
]