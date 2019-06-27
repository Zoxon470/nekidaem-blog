from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from .forms import PostCreateForm
from .models import Blog, Post, UsersReaderThrough


class PostCreateView(generic.CreateView):
    form_class = PostCreateForm
    template_name = 'blog/post-create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if self.request.user.is_anonymous:
                user_not_exists = _('You must create user for creating post')
                return render(request, self.template_name, {
                    'form': form, 'user_not_exists': user_not_exists})
            blog = Blog.objects.filter(user=self.request.user)
            if blog:
                post = form.save(commit=False)
                post.blog = blog
                post.save()
                return HttpResponseRedirect(
                    reverse_lazy('blog:post_detail', args=[post.pk]))
            blog_not_exists = _('You must create blog for creating post')
            return render(request, self.template_name, {
                'form': form, 'blog_not_exists': blog_not_exists})
        return render(request, self.template_name, {'form': form})


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post-list.html'
    paginate_by = 5

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Post.objects.filter(
                blog__subscriptions__in=[self.request.user]).order_by('-id')
        return []


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    pk_url_kwarg = 'pk'
    template_name = 'blog/post-detail.html'


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blogs'
    queryset = Blog.objects.all()
    template_name = 'blog/blog-list.html'
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'posts'
    slug_url_kwarg = 'slug'
    template_name = 'blog/blog-detail.html'
    paginate_by = 5

    def get_object(self, queryset=None):
        super(BlogDetailView, self).get_object(queryset)
        return Post.objects.filter(blog__slug=self.kwargs['slug'])


class BlogSubscribeView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs.get('pk'))
        user = request.user
        if not blog.subscriptions.filter(pk=user.pk).exists():
            blog.subscriptions.add(user)
            return JsonResponse({'message': f'User {user} subscribed.'})
        return JsonResponse({'message': f'User {user} already subscribed.'})


class BlogUnsubscribeView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs.get('pk'))
        user = request.user
        if blog.subscriptions.filter(pk=user.pk).exists():
            blog.subscriptions.remove(user)
            readers = blog.post.values_list('users_read', flat=True)
            UsersReaderThrough.objects.filter(user__in=readers).delete()
            return JsonResponse({'message': f'User {user} unsubscribed.'})
        return JsonResponse({'message': f'User {user} already unsubscribed.'})


class PostMarkAsReadView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        user = request.user
        if not post.users_read.filter(pk=user.pk).exists():
            post.users_read.add(user)
            return JsonResponse(
                {'message': f'Post has marked as read for user {user}'})
        return JsonResponse(
            {'message': f'User {user} has already canceled this post as read'})
