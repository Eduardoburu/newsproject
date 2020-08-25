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

    #Table One
    row1cell1 = models.CharField(max_length=150, null=True, blank=True)
    row1cell2 = models.CharField(max_length=150, null=True, blank=True)
    row1cell3 = models.CharField(max_length=150, null=True, blank=True)
    row2cell1 = models.CharField(max_length=150, null=True, blank=True)
    row2cell2 = models.CharField(max_length=150, null=True, blank=True)
    row2cell3 = models.CharField(max_length=150, null=True, blank=True)
    row3cell1 = models.CharField(max_length=150, null=True, blank=True)
    row3cell2 = models.CharField(max_length=150, null=True, blank=True)
    row3cell3 = models.CharField(max_length=150, null=True, blank=True)
    row4cell1 = models.CharField(max_length=150, null=True, blank=True)
    row4cell2 = models.CharField(max_length=150, null=True, blank=True)
    row4cell3 = models.CharField(max_length=150, null=True, blank=True)
    row5cell1 = models.CharField(max_length=150, null=True, blank=True)
    row5cell2 = models.CharField(max_length=150, null=True, blank=True)
    row5cell3 = models.CharField(max_length=150, null=True, blank=True)
    row6cell1 = models.CharField(max_length=150, null=True, blank=True)
    row6cell2 = models.CharField(max_length=150, null=True, blank=True)
    row6cell3 = models.CharField(max_length=150, null=True, blank=True)
    row7cell1 = models.CharField(max_length=150, null=True, blank=True)
    row7cell2 = models.CharField(max_length=150, null=True, blank=True)
    row7cell3 = models.CharField(max_length=150, null=True, blank=True)
    row8cell1 = models.CharField(max_length=150, null=True, blank=True)
    row8cell2 = models.CharField(max_length=150, null=True, blank=True)
    row8cell3 = models.CharField(max_length=150, null=True, blank=True)
    row9cell1 = models.CharField(max_length=150, null=True, blank=True)
    row9cell2 = models.CharField(max_length=150, null=True, blank=True)
    row9cell3 = models.CharField(max_length=150, null=True, blank=True)
    row10cell1 = models.CharField(max_length=150, null=True, blank=True)
    row10cell2 = models.CharField(max_length=150, null=True, blank=True)
    row10cell3 = models.CharField(max_length=150, null=True, blank=True)
    row11cell1 = models.CharField(max_length=150, null=True, blank=True)
    row11cell2 = models.CharField(max_length=150, null=True, blank=True)
    row11cell3 = models.CharField(max_length=150, null=True, blank=True)
    row12cell1 = models.CharField(max_length=150, null=True, blank=True)
    row12cell2 = models.CharField(max_length=150, null=True, blank=True)
    row12cell3 = models.CharField(max_length=150, null=True, blank=True)
    row13cell1 = models.CharField(max_length=150, null=True, blank=True)
    row13cell2 = models.CharField(max_length=150, null=True, blank=True)
    row13cell3 = models.CharField(max_length=150, null=True, blank=True)
    row14cell1 = models.CharField(max_length=150, null=True, blank=True)
    row14cell2 = models.CharField(max_length=150, null=True, blank=True)
    row14cell3 = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

