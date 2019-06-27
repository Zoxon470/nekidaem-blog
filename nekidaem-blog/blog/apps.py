from django.apps import AppConfig
from django.db.models.signals import post_save

from .models import Post
from .signals import create_user_profile


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        post_save.connect(create_user_profile, sender=Post)
