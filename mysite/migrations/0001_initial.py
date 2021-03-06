# Generated by Django 3.2 on 2021-05-04 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Idiom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idiom_text', models.CharField(max_length=70, verbose_name='(Максимум 70 символ) Хадис же Накыл сөздөр')),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str_title', models.CharField(max_length=200, verbose_name='Названия')),
                ('str_file', models.FileField(upload_to='static/documents/stucture/', verbose_name='Документтер(pdf)')),
            ],
        ),
        migrations.CreateModel(
            name='StructureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Studlife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studlife_photo', models.ImageField(null=True, upload_to='static/images/studlife/', verbose_name='Сүрөт жарыяга')),
                ('studlife_title', models.CharField(max_length=70, verbose_name='(Максимум 70 символ) Темасы кыскача')),
                ('studlife_text', models.TextField(verbose_name='Студенттик кеңеш жаңылыктары')),
                ('studlife_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='Studlife', to='mysite.category', verbose_name='Категория')),
                ('tag_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.tag', verbose_name='Категория Тегов')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(null=True, upload_to='static/images/banner-slider/', verbose_name='Сүрөттү сөзсүз танда!!!')),
                ('slider_title', models.CharField(max_length=90)),
                ('slider_text', models.TextField()),
                ('slider_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, related_name='slider', to='mysite.category')),
                ('tag_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(null=True, upload_to='static/images/posts/', verbose_name='Сүрөттү сөзсүз танда!!!')),
                ('post_slug', models.CharField(default='', max_length=40, verbose_name='Темасы кыска(30 символ Максимум)')),
                ('title', models.CharField(max_length=100, verbose_name='Толук Темасы')),
                ('text', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Убакытты белгиле!!')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='mysite.category')),
                ('tag_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.tag')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_slug', models.CharField(max_length=40, verbose_name='(Максимум 40 символ) Темасы кыскача')),
                ('gallery_title', models.CharField(max_length=100, verbose_name='Темасы толук (макс 100символ)')),
                ('gallery_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gallery_photo', models.ImageField(null=True, upload_to='static/images/gallery/', verbose_name='Фото')),
                ('tag_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.tag', verbose_name='Категория Тегов')),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_slug', models.CharField(max_length=40, verbose_name='(Максимум 40 символ) Темасы кыскача')),
                ('comp_title', models.CharField(max_length=80, verbose_name='(Максимум 80 символ) Темасы толук')),
                ('comp_text', models.TextField(verbose_name='Текст')),
                ('comp_warning', models.CharField(max_length=100, verbose_name='Эскертүү')),
                ('comp_prize', models.TextField(max_length=255, verbose_name='Байгелер')),
                ('comp_condition', models.TextField(max_length=255, verbose_name='Шарттары')),
                ('comp_phone', models.TextField(max_length=255, verbose_name='Телефон номерлери')),
                ('comp_photo', models.ImageField(null=True, upload_to='static/images/competition/', verbose_name='Сүрөт башкы бетке(236х434px)')),
                ('comp_img', models.ImageField(null=True, upload_to='static/images/competition/', verbose_name='Сүрөт жарыяга')),
                ('comp_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='Competition', to='mysite.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads_photo', models.ImageField(null=True, upload_to='static/images/banner-slider/', verbose_name='Сүрөт жарыяга')),
                ('ads_title', models.CharField(max_length=30, verbose_name='(Максимум 30 символ) Жарыя кыска текст')),
                ('ads_text', models.TextField(verbose_name='Жарыя толук текст')),
                ('ads_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='Ads', to='mysite.category', verbose_name='Категория')),
                ('tag_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.tag', verbose_name='Категория Тегов')),
            ],
        ),
        migrations.CreateModel(
            name='Abiturient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abt_slug', models.CharField(max_length=40, verbose_name='(Максимум 40 символ) Темасы кыскача')),
                ('abt_title', models.CharField(max_length=100, verbose_name='Темасы толук (макс 100символ)')),
                ('abt_text', models.TextField(verbose_name='Текст')),
                ('abt_condition', models.TextField(max_length=255, verbose_name='Кабыл алуу шарттары')),
                ('abt_docs', models.TextField(max_length=255, verbose_name='Керектелүүчү документтер')),
                ('abt_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('abt_photo', models.ImageField(null=True, upload_to='static/images/abiturient/', verbose_name='Фото')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Абитуриент', to='mysite.category', verbose_name='Категория')),
                ('tag_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.tag', verbose_name='Категория Тегов')),
            ],
        ),
    ]
