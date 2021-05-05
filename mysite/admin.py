from django.contrib import admin
from . models import *

class PostAdmin(admin.ModelAdmin):
	search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Slider)	
admin.site.register(Studlife)
admin.site.register(Ads)
admin.site.register(Idiom)
admin.site.register(Competition)
admin.site.register(Abiturient)
admin.site.register(PhotoGallery)
admin.site.register(Structure)
admin.site.register(StructureCategory)