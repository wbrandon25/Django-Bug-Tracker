from pydoc import describe
from tokenize import blank_re
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class extendedUser(models.Model):
    ogUser = models.OneToOneField(User, on_delete=models.CASCADE)
    # nickname = models.CharField(max_length=200, null = True, blank = True)
    fullName = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    bDev = models.BooleanField(default=False)

    def __str__(self):
        return self.ogUser.username


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(User, max_length=200, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class bug_ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', blank=True)
    developers = models.ManyToManyField(
        User, related_name='developers', limit_choices_to={'extendeduser__bDev': True})
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    resolved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_ticket = models.ForeignKey(bug_ticket, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
