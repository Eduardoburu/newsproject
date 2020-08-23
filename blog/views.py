from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.


def about(request): 
    return render(request, 'blog/about.html', {'title': 'About'})


def contact(request): 
    return render(request, 'blog/contact.html', {'title': 'Contact Us'})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 



class ScienceListView(ListView):
    model = Post
    template_name = 'blog/science.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 


class BusinessListView(ListView):
    model = Post
    template_name = 'blog/business.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class PoliticsListView(ListView):
    model = Post
    template_name = 'blog/politics.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class RestateListView(ListView):
    model = Post
    template_name = 'blog/restate.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class SstoryListView(ListView):
    model = Post
    template_name = 'blog/sstory.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class TravelListView(ListView):
    model = Post
    template_name = 'blog/travel.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class SportsListView(ListView):
    model = Post
    template_name = 'blog/sports.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class TechnologyListView(ListView):
    model = Post
    template_name = 'blog/technology.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class EducationListView(ListView):
    model = Post
    template_name = 'blog/education.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class HealthListView(ListView):
    model = Post
    template_name = 'blog/health.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class EntertainmentListView(ListView):
    model = Post
    template_name = 'blog/entertainment.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 

class ArtListView(ListView):
    model = Post
    template_name = 'blog/art.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 20 


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title', 
        'section', 
        'summary', 
        'caption', 
        'writer', 
        'section', 
        'content', 
        'image', 
        'paragraph1', 
        'paragraph2', 
        'paragraph3',
        'subheading1', 
        'paragraph4', 
        'image2', 
        'paragraph5', 
        'paragraph6',
        'subheading2', 
        'paragraph7', 
        'image3', 
        'paragraph8', 
        'paragraph9', 
        'subheading3',
        'paragraph10',  
        'paragraph11',
        'paragraph12', 
        'paragraph13',
        'image4',  
        'subheading4',
        'paragraph14', 
        'paragraph15',
        'paragraph16', 
        'paragraph17',
        'subheading5',  
        'paragraph18', 
        'paragraph19',
        'paragraph20', 
        ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title', 
        'section', 
        'summary', 
        'caption', 
        'writer', 
        'section', 
        'content', 
        'image', 
        'paragraph1', 
        'paragraph2', 
        'paragraph3',
        'subheading1', 
        'paragraph4', 
        'image2', 
        'paragraph5', 
        'paragraph6',
        'subheading2', 
        'paragraph7', 
        'image3', 
        'paragraph8', 
        'paragraph9', 
        'subheading3',
        'paragraph10',  
        'paragraph11',
        'paragraph12', 
        'paragraph13',
        'image4',  
        'subheading4',
        'paragraph14', 
        'paragraph15',
        'paragraph16', 
        'paragraph17',
        'subheading5',  
        'paragraph18', 
        'paragraph19',
        'paragraph20', 
        ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
