from django.contrib import admin
from .models.posts import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'created']
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
# Register your models here.
