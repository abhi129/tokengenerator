# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models









class Tokenpool(models.Model):
    token = models.CharField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    alive = models.IntegerField(max_length=1,default=1)
    flag = models.IntegerField(max_length=1,default=0)


    def __str__(self):
        return u'%s %s %s %s ' % (self.id,self.token,self.alive,self.flag)
# Create your models here.
