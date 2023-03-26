from attr import attrs
from django.db import models
from tinymce import models as tm


Contact_CHOICES = (
     ('choose', 'choose what you want to send us'),
    ('message','Message'),
    ('questions', 'Questions'),
    ('issues','Issues'),
    ('suggestions for creating tips','Suggestions for creating tips'),
    ('suggestions for improving our tips','Suggestions for improving tips'),
)


# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= tm.HTMLField()
     image = models.ImageField(default='static/Default.jpg', upload_to='static/users/', null=True, blank=True)
     
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     contact_type = models.CharField(max_length=100, choices=Contact_CHOICES, default='choose')
     