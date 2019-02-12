from __future__ import unicode_literals

from django.conf import settings
# from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.utils import timezone


from markdown_deux import markdown

RESULT = (
  ('Scalene','Scalene'),
  ('Equilateral','Equilateral'),
  ('Isosceles','Isosceles'),
  ('Incorrect','Incorrect'),
)

class Trangle(models.Model):
  a = models.IntegerField(default=0)
  b = models.IntegerField(default=0)
  c = models.IntegerField(default=0)
  output = models.CharField(max_length=100,choices=RESULT, default='Scalene')

  def save(self,*args, **kwargs):
      if self.a == self.b == self.c:
            return "Equilateral "
      elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "Isosceles "
      elif self.a != self.b or self.b != self.c or self.c != self.a:
            return "Scalene"
      else:
            return "Incorrect"

  def __unicode__(self):
      return self.output

  def __str__(self):
      return self.output

  def get_api_url(self):
      return reverse("comment:thread",  kwargs={"id": self.id})

  def get_absolute_url(self):
      return reverse("comment:thread", kwargs={"id": self.id})