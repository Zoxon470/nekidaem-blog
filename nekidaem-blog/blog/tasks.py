from django.conf import settings
from django.core.mail import send_mail
from django_rq import job


@job
def email_notification_subscriber(email, blog_title, post_url):
    subject = 'Новый пост от %s' % blog_title
    message = f'''
        Блог от <{blog_title}> опубликовал новый пост. 
        Пост доступен по прямой ссылке - {post_url} .
    '''
    email_from = settings.EMAIL_HOST_USER
    email_to = [email]
    send_mail(subject, message, email_from, email_to)
