from django.shortcuts import render
from .models import News
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def home(request):
#     data = {
#         "news": News.objects.all(),
#         "title": "Главная страница"
#     }
#     return render(request, "blog/home.html", data)


class ShowNewsView(ListView):
    model = News
    template_name = "blog/home.html"
    context_object_name = "news"
    ordering = ["-date"]

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx["title"] = "Главная страница сайта"
        return ctx

class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = "blog/create-news.html"
    fields = ['title', 'text']
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwards):
        ctx = super(CreateView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = "blog/create-news.html"
    fields = ['title', 'text']


    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)





class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False


def contacti(request):
    return render(request, "blog/contacti.html", {"title": "Контакты!"})
