# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30, default='unknown')

    def save(self, *args,**kwargs):
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' %self.name


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null = True)
    #image = models.ImageField(upload_to = "post_images")
    body = models.TextField(blank = True, null = True)
    #order = models.IntegerField(blank = True, null = True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(default = '', blank = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.title 



