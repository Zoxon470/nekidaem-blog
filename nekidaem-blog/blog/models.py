from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .tasks import email_notification_subscriber


class Blog(models.Model):
    title = models.CharField(_('title'), max_length=125)
    slug = models.SlugField(_('blog url'), unique=True)
    description = models.TextField(_('description'))
    subscriptions = models.ManyToManyField(User,
                                           related_name='subscription',
                                           blank=True,
                                           verbose_name=_('subscriptions'))
    user = models.ForeignKey(User, related_name='blog',
                             verbose_name=_('user'),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')

    def __str__(self):
        return self.title


class UsersReaderThrough(models.Model):
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', related_name='post',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Post(models.Model):
    title = models.CharField(_('title'), max_length=125)
    description = models.TextField(_('description'))
    users_read = models.ManyToManyField(User,
                                        related_name='user_read',
                                        through=UsersReaderThrough,
                                        through_fields=('post', 'user'),
                                        blank=True,
                                        verbose_name=_('Users have read'))
    publication = models.DateTimeField(_('date published'), auto_now_add=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    blog = models.ForeignKey(Blog, related_name='post',
                             verbose_name=_('blog'),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title


@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):
    if created:
        blog_title = instance.title
        post_url = 'http://0.0.0.0:8000/posts/%s' % instance.pk
        user_emails = instance.blog.subscriptions.values_list(
            'email', flat=True)
        for email in user_emails:
            email_notification_subscriber.delay(email, blog_title, post_url)
