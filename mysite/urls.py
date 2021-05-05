from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('slider_detail/<int:key>', views.slider_detail, name ='slider_detail'),
    path('post_detail/<int:key>', views.post_detail, name='post_detail'),
    path('studlife_detail/<int:key>', views.studlife_detail, name='studlife_detail'),
    path('ads_detail/<int:key>', views.ads_detail, name='ads_detail'),
    path('competition/<int:key>', views.competition_detail, name='competition_detail'),
    path('abiturient_detail/', views.abiturient_detail, name='abiturient_detail'),
    path('structures/', views.structure_detail, name='structure_detail'),
    path('all_posts/', views.post_list, name = 'all_posts'),
    path('studlife_list/', views.studlife_list, name='studlife_list'),
    path('gallery/', views.photo_gallery, name='photo_gallery'),

    # Структура университета
    path('structure_education/', views.structure_education, name='structure_education'),
    path('education_plan/', views.structure_edc_plan, name='structure_edc_plan'),
    path('education_development/', views.structure_development, name='structure_development'),
    path('structure_reception/', views.structure_reception, name='structure_reception'),
    path('okutuuchuluk_komokchu_kuram/', views.structure_komokchu_kuram, name='structure_komokchu_kuram'),
    path('technikalyk_baza/', views.structure_tech_base, name='structure_tech_base'),
    path('maalymatty_bashkaruu/', views.structure_info_leading, name='structure_info_leading'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
   	# path('login/', views.user_login, name='login'),
   	# path('register/', views.register, name = 'register')
]