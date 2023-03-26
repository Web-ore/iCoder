from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
Type_choice = (
    ('Card', 'Card ads'),
    ('sheet','Tips ads'),
    ('Image','Images ads'),
    ('Search', 'Url/flat cards')
)

class Ads(models.Model):
    Ads_Name = models.CharField(max_length=1000)
    Ads_HTML = models.TextField()
    Visibility = models.BooleanField(default=False)
    Created = models.DateTimeField(auto_now_add=True)
    Type = models.CharField(max_length=100, choices=Type_choice, default='Card')
    Shifted = models.CharField(max_length=1000)
    Position_Number = models.IntegerField()
    tags = TaggableManager()

    Status = models.CharField(max_length=100, choices=(("Edit", "Edit"), ("Create", "Create")), default='Create')

    # def save(self, *args, **kwargs):
    #     if self.Status == "Create":
    #         if Ads.objects.count()>0:
    #             p1 = Ads.objects.all().last().Position_Number
    #             self.Position_Number = int(p1)+1
    #         else:
    #             self.Position_Number = 1
    #     elif self.Status == "Edit":
    #         if not Ads.objects.count()>0:
    #             self.Position_Number = 1
    #     else:
    #         pass

    #     super(Ads, self).save(*args, **kwargs)
    

    def __str__(self):
        return f'Ads: {self.Shifted} | Position: {self.Position_Number} | Type: {self.Type}'
    def get_absolute_url(self):
        return reverse("Tip", args=[self.id])
    

    