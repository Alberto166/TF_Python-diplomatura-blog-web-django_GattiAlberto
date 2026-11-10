from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# 1. Listar todas las publicaciones (Público)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-fecha_creacion']  # Los más nuevos primero

# 2. Ver el detalle de una publicación (Público)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# 3. Crear una nueva publicación (Protegido)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asigna automáticamente al usuario logueado como autor
        return super().form_valid(form)

# 4. Editar una publicación existente (Protegido)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('post_list')

# 5. Eliminar una publicación (Protegido)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
