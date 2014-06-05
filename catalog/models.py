from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50,unique = True,help_text = 'Unique value for product page URL,created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default = True)
    meta_keywords = models.CharField(max_length = 255,help_text = 'Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length = 255,help_text = 'Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse()
