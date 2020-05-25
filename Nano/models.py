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

class Images(models.Model):
    photo = ProcessedImageField(
       upload_to =  user_path,
        processors = [ResizeToFill(80,80)],
        format = 'JPEG',
        options={'qulity':60},
        null=True
    )

class WordDict(models.Model):
    word = models.CharField(max_length=30,blank=False,primary_key=True)
    summary = models.TextField(blank=False)

    def __str__(self):
        return '%s' %(self.word)

class WordImg(models.Model):
    word = models.CharField(max_length=30,blank=False)
    image = models.ImageField(upload_to='wordimg',blank=False)

    def __str__(self):
        return '%s' %(self.word)

class Summary(models.Model):
    title = models.CharField(max_length=30,blank = False,primary_key=True)
    content = models.TextField()

    def __str__(self):
        return '%s' %(self.title)

class SummaryImg(models.Model):
    title = models.CharField(max_length=30,blank = False)
    image = models.ImageField(upload_to="summaryimg",blank=False)
    figure = models.TextField()
    descript = models.TextField()

    def __str__(self):
        return '%s' %(self.title)

class Solution(models.Model):
    RECOMMEND_CHOICES = (
        (1,'★☆☆☆☆'),
        (2,'★★☆☆☆'),
        (3,'★★★☆☆'),
        (4,'★★★★☆'),
        (5,'★★★★★'),
    )

    sol_id = models.CharField(max_length=30)
    problem = models.ImageField(upload_to="solutionimg",blank=False)
    solution = models.TextField()
    rating = models.IntegerField(choices=RECOMMEND_CHOICES )

    def __str__(self):
        return '%s' %(self.sol_id)