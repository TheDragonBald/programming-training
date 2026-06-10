from django.db import models


class Request(models.Model):
    
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнена'),
    ]
    
    name = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    text = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')  
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} — {self.subject}"