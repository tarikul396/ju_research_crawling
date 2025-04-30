from django.db import models

class Teacher(models.Model):
  name = models.CharField(max_length=200)
  department = models.CharField(max_length=100)
  api_author_name = models.CharField(
    max_length=200,
    help_text="Exact author name format for API search"
  )

  def __str__(self):
    return self.name