from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'signals'
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        unique_together = ['name', 'email']