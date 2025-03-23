from django.db import models
from django.urls import reverse
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)

    class Meta:
        ordering = ['-date_publication']  # Trier par date de publication descendante

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})