from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os

STATUS = ((0, "Draft" ) , (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200 , unique= True)
    slug = models.SlugField(max_length=200 , unique= True)
    author = models.ForeignKey(User , on_delete= models.CASCADE, related_name = 'blog_posts')
    created_on = models.DateTimeField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    status = models.IntegerField(choices= STATUS , default=0)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Nouveau champ pour l'image

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    # Supprimer le fichier image associé lors de la suppression de l'article
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)