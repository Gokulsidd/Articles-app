from django.views.generic import ListView, DetailView  
from django.views.generic.edit import UpdateView, DeleteView ,CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin 
from django.urls import reverse_lazy  
from .models import Article , Comment


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article_list'
    

class CreateArticleView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields= ['title','body']
    
    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)


class DetailArticleView(LoginRequiredMixin,DetailView):  
    model = Article
    template_name = 'article_detail.html'


class UpdateArticleView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    
    
    def test_func(self):
        obj =self.get_object()
        return obj.author == self.request.user


class DeleteArticleView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):  
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    


class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['article','comment' ]
    template_name = 'article_comment.html'
    context_object_name = 'comment_list'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

