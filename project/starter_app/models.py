# -*- coding: utf-8 -*-

from django.db import models


class Message(models.Model):
    order = models.IntegerField()
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ['order']
