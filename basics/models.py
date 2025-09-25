from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "basics"
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["name"]