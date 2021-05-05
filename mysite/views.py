from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import *

# Башкы бет
def index(request):
	post = Post.objects.order_by('-id')[:4]
	main_post = Post.objects.all()[Post.objects.count()-1]
	slider = Slider.objects.order_by('-id')[:4]
	idiom = Idiom.objects.order_by('-id')[:5]
	studlife = Studlife.objects.order_by('-id')[:5]	
	gallery = PhotoGallery.objects.order_by('-id')[:5]
	abiturient = Abiturient.objects.all()[Abiturient.objects.count()-1]
	structure = Structure.objects.only('str_category')

	studlife_main = Studlife.objects.all()[Studlife.objects.count()-1]
	ads_main = Ads.objects.all()[Ads.objects.count()-1]
	main_competition = Competition.objects.all()[Post.objects.count()-1]

	parms =  {
		"posts" : post,
		"slider" : slider,
		"main_post" : main_post,
		"idiom" : idiom,
		"studlife" : studlife,
		"studlife_main" : studlife_main,
		"ads_main" : ads_main,
		"main_competition": main_competition,
		"gallery" : gallery,
		"abiturient" : abiturient,
		"structure" : structure,
	}
	return render(request, 'index.html', parms)

def error_404(request):
	redirect('/')


	

def structure_detail(request):
	structure = Structure.objects.all()
	str_education = Structure.objects.filter(str_category = 1)
	parms = {
		"structure" : structure,
		"str_detail" : str_detail,
 	}
	return render(request, 'faqs.html', parms) 

# Структура 1
def structure_education(request):
	str_education = Structure.objects.filter(str_category = 1)
	parms = {
		"str_education" : str_education,
 	}
	return render(request, 'structure_education.html', parms)

# Структура 2
def structure_edc_plan(request):
	str_edc_plan = Structure.objects.filter(str_category = 2)
	parms = {
		"str_edc_plan" : str_edc_plan,
 	}
	return render(request, 'structure_education_plan.html', parms)	

# Сруктура 3. Инсанга багытталган окутуу
def structure_development(request):
	str_development = Structure.objects.filter(str_category = 3)
	parms = {
		"str_development" : str_development,
 	}
	return render(request, 'structure_development.html', parms)	

# Структура 4. Кабыл алуу жана Билим берүү
def structure_reception(request):
	str_reception = Structure.objects.filter(str_category = 4)
	parms = {
		"str_reception" : str_reception,
 	}
	return render(request, 'structure_reception.html', parms)	

# Структура 5.	Окутуучулук жана окутуучу-көмөкчү курам 
def structure_komokchu_kuram(request):
	str_komokchu_kuram = Structure.objects.filter(str_category = 5)
	parms = {
		"str_komokchu_kuram" : str_komokchu_kuram,
 	}
	return render(request, 'structure_komokchu_kuram.html', parms)	

# Структура 6. Материалдык-техникалык база жана маалымат ресурстары 
def structure_tech_base(request):
	str_tech_base = Structure.objects.filter(str_category = 6)
	parms = {
		"str_tech_base" : str_tech_base,
 	}
	return render(request, 'structure_tech_baza.html', parms)	

# Структура 7. Маалыматты башкаруу жана аны коомчулукка жеткирүү  
def structure_info_leading(request):
	str_info_leading = Structure.objects.filter(str_category = 7)
	parms = {
		"str_info_leading" : str_info_leading,
 	}
	return render(request, 'structure_leading.html', parms)	


# Slider детально
def slider_detail(request, key):
	slider = get_object_or_404(Slider, pk=key)
	parms = {
		"slider" : slider,
	}

	return render(request, 'slider_detail.html', parms)

# Жаңылыктар детально
def post_detail(request, key):
	post = get_object_or_404(Post, pk=key)
	parms = {
		"post" : post 
	}
	return render(request, 'post-item-details.html', parms)

# Студ кеңещ жаңылыктары детально
def studlife_detail(request, key):
	studlife_detail = get_object_or_404(Studlife, pk = key)

	parms = {
		"studlife_detail" : studlife_detail,
	}
	return render(request, 'studlife_detail.html', parms)

# Жарыя жана Кулактандыруу детально
def ads_detail(request, key):
	ads_detail = get_object_or_404(Ads, pk = key)

	parms = {
		"ads_detail" : ads_detail,
	}

	return render(request, 'ads_detail.html', parms)

# Конкурс детально 
def competition_detail(request, key):
	comp_detail = get_object_or_404(Competition, pk = key)

	parms = {
		"comp_detail" : comp_detail,
	}
	return render(request, 'competition.html', parms)

# Абитуриент детально
def abiturient_detail(request):
	abiturient_detail = get_object_or_404(Abiturient)

	parms = {
		"abiturient_detail" : abiturient_detail,
	}

	return render(request, 'abiturient.html', {})
# View all posts
def post_list(request):
	all_post = Post.objects.all().order_by('-id')
	paginator = Paginator(all_post, 6)
	page_number = request.GET.get('page', 1)
	try:
		posts = paginator.page(page_number)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	parms = {
		"posts" : posts,
	}   
	return render(request, 'all_posts.html', parms)

# Studlife list
def studlife_list(request):
	all_post = Studlife.objects.all().order_by('-id')
	paginator = Paginator(all_post, 6)
	page_number = request.GET.get('page', 1)
	try:
		studlife_posts = paginator.page(page_number)
	except PageNotAnInteger:
		studlife_posts = paginator.page(1)
	except EmptyPage:
		studlife_posts = paginator.page(paginator.num_pages)
	
	parms = {
		"posts" : studlife_posts,
	}
	return render(request, 'studlife_list.html', parms)

# Фотогалерея все посты
def photo_gallery(request):
	all_photo = PhotoGallery.objects.all().order_by('-id')
	paginator = Paginator(all_photo, 10)
	page_number = request.GET.get('page', 1)
	try:
		photos = paginator.page(page_number)
	except PageNotAnInteger:
		# if page is not integer then put page 1
		photos = paginator.page(1)
	except EmptyPage:
		# if page is out of range, deliver last page
		photos = paginator.page(paginator.num_pages)
	
	parms = {
		"pag_photo" : photos,
	}
	return render(request, 'gallery.html', parms)	

def structure(request, key):

	all_structure = Structure.objects.all()

# Студ кеңеш жаңылыктары
# def stud_life(request):
# 	studlife = Post.objects.order_by('-id')[:5]	

# 	parms = {
# 		"studlife" : studlife,
# 	}
# 	pa