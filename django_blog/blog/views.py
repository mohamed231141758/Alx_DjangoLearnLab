from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm, UserUpdateForm, PostForm, CommentForm
from .models import Post, Comment

# ==================== AUTH VIEWS ====================

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

# ==================== POST VIEWS ====================

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    # Add comment form and comments to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# ==================== COMMENT VIEWS ====================

# Add a comment to a post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added!')
    return redirect('post-detail', pk=post_id)

# Edit a comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # Only the author can edit their comment
    if request.user != comment.author:
        messages.error(request, 'You cannot edit this comment!')
        return redirect('post-detail', pk=comment.post.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated!')
            return redirect('post-detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

# Delete a comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # Only the author can delete their comment
    if request.user != comment.author:
        messages.error(request, 'You cannot delete this comment!')
        return redirect('post-detail', pk=comment.post.pk)
    post_id = comment.post.pk
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect('post-detail', pk=post_id)
