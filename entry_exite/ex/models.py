from django.db import models

class Person(models.Model):
    person_id = models.CharField(max_length=100, unique=True)
    is_inside = models.BooleanField(default=False)
    last_entry_time = models.DateTimeField(null=True, blank=True)
    last_exit_time = models.DateTimeField(null=True, blank=True)
