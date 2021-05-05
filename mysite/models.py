from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
	# Соңку кабарлар
	category_title = models.CharField(max_length=20)

	def __str__(self):
		return self.category_title

class Tag(models.Model):
	tags_title = models.CharField(max_length=100)

	def __str__(self):
		return self.tags_title

# Жаңылыктар
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_image = models.ImageField(null = True,upload_to='static/images/posts/', verbose_name='Сүрөттү сөзсүз танда!!!')
    post_slug = models.CharField(default = '', max_length=40, verbose_name='Темасы кыска(30 символ Максимум)')
    title = models.CharField(max_length=100, verbose_name='Толук Темасы')
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name= 'Убакытты белгиле!!')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', default=1)
    tag_category = models.ForeignKey(Tag,on_delete=models.CASCADE, default = 1)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Слайд үчүн
class Slider(models.Model):
	slider_img = models.ImageField(null = True, upload_to='static/images/banner-slider/', verbose_name='Сүрөттү сөзсүз танда!!!')
	slider_title = models.CharField(max_length=90)
	slider_text = models.TextField()
	slider_created_date = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='slider', default=9)
	tag_category = models.ForeignKey(Tag,on_delete=models.CASCADE, default = 1)
	def __str__(self):
		return self.slider_title
	
# Кыскача сөздөр 
class Idiom(models.Model):
	idiom_text = models.CharField(max_length=70, verbose_name='(Максимум 70 символ) Хадис же Накыл сөздөр')

	def __str__(self):
		return self.idiom_text
# Жарыялар ж.а Конкурстар
class Ads(models.Model):
	ads_photo = models.ImageField(null = True, upload_to='static/images/banner-slider/', verbose_name='Сүрөт жарыяга')
	ads_title = models.CharField(max_length=30, verbose_name='(Максимум 30 символ) Жарыя кыска текст')
	ads_text  = models.TextField(verbose_name='Жарыя толук текст')
	ads_created_date = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Ads', default=8, verbose_name='Категория')
	tag_category = models.ForeignKey(Tag,on_delete=models.CASCADE, default = 1, verbose_name='Категория Тегов')

	def __str__(self):
		return self.ads_title
# Студ кеңеш ж.а Студенттик жашоо 
class Studlife(models.Model):
	studlife_photo = models.ImageField(null = True, upload_to='static/images/studlife/', verbose_name='Сүрөт жарыяга')
	studlife_title = models.CharField(max_length=70, verbose_name='(Максимум 70 символ) Темасы кыскача')
	studlife_text = models.TextField(verbose_name='Студенттик кеңеш жаңылыктары')
	studlife_created_date = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Studlife', default=10, verbose_name='Категория')
	tag_category = models.ForeignKey(Tag,on_delete=models.CASCADE, default = 1, verbose_name='Категория Тегов')

	def __str__(self):
		return self.studlife_title

# Конкурс база
class Competition(models.Model):
	comp_slug = models.CharField(max_length = 40, verbose_name='(Максимум 40 символ) Темасы кыскача')
	comp_title = models.CharField(max_length = 80, verbose_name='(Максимум 80 символ) Темасы толук')
	comp_text = models.TextField(verbose_name='Текст')
	comp_warning = models.CharField(max_length=100, verbose_name='Эскертүү')
	comp_prize = models.TextField(max_length=255, verbose_name='Байгелер')
	comp_condition = models.TextField(max_length=255, verbose_name='Шарттары')
	comp_phone = models.TextField(max_length=255, verbose_name='Телефон номерлери')
	comp_photo = models.ImageField(null = True, upload_to='static/images/competition/', verbose_name='Сүрөт башкы бетке(236х434px)')
	comp_img = models.ImageField(null=True, upload_to='static/images/competition/', verbose_name='Сүрөт жарыяга')
	comp_created_date = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Competition', default=10, verbose_name='Категория')

	def __str__(self):
		return self.comp_title

# Абитуриент 
class Abiturient(models.Model):
	abt_slug = models.CharField(max_length = 40, verbose_name='(Максимум 40 символ) Темасы кыскача')
	abt_title = models.CharField(max_length = 100, verbose_name='Темасы толук (макс 100символ)')
	abt_text = models.TextField(verbose_name='Текст')
	abt_condition = models.TextField(max_length=255, verbose_name='Кабыл алуу шарттары')
	abt_docs = models.TextField(max_length=255, verbose_name='Керектелүүчү документтер')
	abt_created_date = models.DateTimeField(default=timezone.now)
	abt_photo = models.ImageField(null=True, upload_to='static/images/abiturient/', verbose_name = 'Фото')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Абитуриент', default=1, verbose_name='Категория')
	tag_category = models.ForeignKey(Tag,on_delete=models.CASCADE, default = 1, verbose_name='Категория Тегов')

	def __str__(self):
		return self.abt_slug
# Photo Gallery
class PhotoGallery(models.Model):
	gallery_slug = models.CharField(max_length=40, verbose_name='(Максимум 40 символ) Темасы кыскача')	
	gallery_title = models.CharField(max_length = 100, verbose_name='Темасы толук (макс 100символ)')
	gallery_created_date = models.DateTimeField(default = timezone.now)
	gallery_photo = models.ImageField(null=True, upload_to='static/images/gallery/', verbose_name = 'Фото')
	tag_category = models.ForeignKey(Tag,on_delete=models.CASCADE, default = 1, verbose_name='Категория Тегов')

	def __str__(self):
		return self.gallery_slug

class StructureCategory(models.Model):
	title = models.CharField(max_length=150, verbose_name='Категория')

	def __str__(self):
		return self.title
# Структура университета
class Structure(models.Model):
	str_title = models.CharField(max_length=200, verbose_name='Названия')
	str_file = models.FileField(upload_to='static/documents/stucture/', verbose_name='Документтер(pdf)')

	str_category = models.ForeignKey(StructureCategory,on_delete=models.CASCADE, default = 1, verbose_name='Категория')
	def __str__(self):
		return self.str_title
