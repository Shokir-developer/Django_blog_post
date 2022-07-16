from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):

	STATUS = (
		('draft', 'Draft'),
		('published', 'Publish'),
	)

	title = models.CharField(max_length=200, null=True)
	slug = models.SlugField(max_length=100, null=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
	body = RichTextUploadingField()
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS, default='draft')

	tags = TaggableManager()
	
	like_count = models.IntegerField(null=True, blank=True, default=0)
	dislike_count = models.IntegerField(null=True, blank=True, default=0)

	def total_likes(self):
		return self.likes.count()

	class Meta:
		ordering = ('-created',)

	def get_absolute_url(self):
		return f'posts/{self.slug}'
		
	def __str__(self):
		return self.title