from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
POST_CHOICES = (
    ('business','Business'),
    ('politics', 'Politics'),
    ('real estate', 'Real Estate'),
    ('travel', 'Travel'),
    ('sports', 'Sports'),
    ('technology', 'Technology'),
    ('education', 'Education'),
    ('health', 'Health'),
    ('entertainment', 'Entertainment'),
    ('art', 'Art'),
    ('short story', 'Short Story'),
    ('science', 'Science'),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    summary = models.TextField(null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    writer = models.TextField(null=True, blank=True)
    paragraph1 = models.TextField(null=True, blank=True)
    paragraph2 = models.TextField(null=True, blank=True)
    paragraph3 = models.TextField(null=True, blank=True)
    paragraph4 = models.TextField(null=True, blank=True)
    paragraph5 = models.TextField(null=True, blank=True)
    paragraph6 = models.TextField(null=True, blank=True)
    paragraph7 = models.TextField(null=True, blank=True)
    paragraph8 = models.TextField(null=True, blank=True)
    paragraph9 = models.TextField(null=True, blank=True)
    paragraph10 = models.TextField(null=True, blank=True)
    paragraph11 = models.TextField(null=True, blank=True)
    paragraph12 = models.TextField(null=True, blank=True)
    paragraph13 = models.TextField(null=True, blank=True)
    paragraph14 = models.TextField(null=True, blank=True)
    paragraph15 = models.TextField(null=True, blank=True)
    paragraph16 = models.TextField(null=True, blank=True)
    paragraph17 = models.TextField(null=True, blank=True)
    paragraph18 = models.TextField(null=True, blank=True)
    paragraph19 = models.TextField(null=True, blank=True)
    paragraph20 = models.TextField(null=True, blank=True)
    subheading1 = models.TextField(null=True, blank=True)
    subheading2 = models.TextField(null=True, blank=True)
    subheading3 = models.TextField(null=True, blank=True)
    subheading4 = models.TextField(null=True, blank=True)
    subheading5 = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.FileField(upload_to='story_pics', null=True, blank=True)
    image2 = models.FileField(upload_to='story_pics', null=True, blank=True)
    image3 = models.FileField(upload_to='story_pics', null=True, blank=True)
    image4 = models.FileField(upload_to='story_pics', null=True, blank=True)
    section = models.CharField(max_length=10, choices=POST_CHOICES, default='main')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

