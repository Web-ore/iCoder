from email.policy import default
from django.db import models
from tinymce import models as tm
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
# from django_summernote import settings
from django_summernote.fields import SummernoteTextField
from ckeditor import configs
from django.utils.text import slugify

class another(models.Model):
    another = RichTextField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    class test(models.Model):
        title = models.CharField(max_length=140)



class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True)
    content = HTMLField()
    Is_search = models.BooleanField(default=False)

    #tags
    tags = TaggableManager()

        # hitcount work
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        

    def __str__(self):
        return self.title + " by " + self.author

    



class User(models.Model):
    user = models.TextField(default=None)
    def __str__(self):
        return self.user