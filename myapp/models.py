from django.db import models
from django.utils import timezone

class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  # Assuming icon is a class name for an icon font
    image = models.ImageField(upload_to='services/')
    brief_description = models.TextField()
    main_body = models.TextField()

    def __str__(self):
        return self.title

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title
