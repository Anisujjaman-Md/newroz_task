from django.db import models

class Quote(models.Model):
    quote = models.TextField(unique=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.quote} - {self.author}'
    
    class Meta:
        # Add indexes to the quote and author fields
        indexes = [
            models.Index(fields=['quote']),
            models.Index(fields=['author']),
        ]