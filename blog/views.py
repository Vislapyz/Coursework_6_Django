from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from pytils.translit import slugify

from blog.models import Blog
from blog.services import get_blogs_from_cache


class BlogCreateView(CreateView):
    """Для создания новой публикации"""

    model = Blog
    fields = ("title", "content", "preview", "view_counter")
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    """Просмотр всех публикаций."""

    model = Blog

    def get_queryset(self):
        queryset = get_blogs_from_cache()
        return queryset


class BlogDetailView(DetailView):
    """Просмотра детальной информации публикации."""

    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """Редактирования публикации"""

    model = Blog
    fields = ("title", "content", "preview", "view_counter")

    def get_success_url(self):
        return reverse("blog:view", args=[self.kwargs.get("slug")])


class BlogDeleteView(DeleteView):
    """Удаления публикации"""

    model = Blog
    success_url = reverse_lazy("blog:list")
