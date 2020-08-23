from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ScienceListView, BusinessListView, PoliticsListView, RestateListView, SstoryListView, TravelListView, SportsListView, TechnologyListView, EducationListView, HealthListView, EntertainmentListView, ArtListView
from . import views



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('blog/science', ScienceListView.as_view(), name='blog-science'),
    path('blog/business', BusinessListView.as_view(), name='blog-business'),
    path('blog/politics', PoliticsListView.as_view(), name='blog-politics'),
    path('blog/restate', RestateListView.as_view(), name='blog-restate'),
    path('blog/sstory', SstoryListView.as_view(), name='blog-sstory'),
    path('blog/travel', TravelListView.as_view(), name='blog-travel'),
    path('blog/sports', SportsListView.as_view(), name='blog-sports'),
    path('blog/technology', TechnologyListView.as_view(), name='blog-technology'),
    path('blog/education', EducationListView.as_view(), name='blog-education'),
    path('blog/health', HealthListView.as_view(), name='blog-health'),
    path('blog/entertainment', EntertainmentListView.as_view(), name='blog-entertainment'),
    path('blog/art', ArtListView.as_view(), name='blog-art'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
]