from django.db import models

class List(models.Model):
    task = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['-created_date']