from django.db import models

class URLRecord(models.Model):
    url = models.URLField(max_length=1000)
    prediction = models.CharField(max_length=10)
    confidence = models.FloatField()
    feedback = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.url} - {self.prediction}"