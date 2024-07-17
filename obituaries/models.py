from django.db import models
from django.utils.text import slugify


class Obituary(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'obituaries'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if Obituary.objects.filter(slug=self.slug).exists():
                unique_slug = f"{self.slug}-{self.date_of_death.strftime('%Y-%m-%d')}"
                self.slug = unique_slug
        super(Obituary, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
