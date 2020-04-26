from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def user_path(instance,filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]

    return '%s/%s.%s' % (instance.Descript, pid, extension)

class Descript(models.Model):
    Classname = models.CharField(max_length=50, default = "전자기학")
    Text = models.TextField(max_length = 500000)
    Thumname_image = models.ImageField(blank = True) 
    Comment = models.CharField(max_length = 255)

class Images(models.Model):
    Descript = models.ForeignKey(Descript, blank = False, null =False, on_delete=models.CASCADE)
    photo = ProcessedImageField(
        upload_to =  user_path,
        processors = [ResizeToFill(80,80)],
        format = 'JPEG',
        options={'qulity':60},
        null=True
    )