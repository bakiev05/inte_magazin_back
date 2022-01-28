from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True, blank=True
    )
    slug = models.SlugField(
        blank=True, unique=True
    )

    def __str__(self):
        return f"{self.title} -- {self.slug}"
