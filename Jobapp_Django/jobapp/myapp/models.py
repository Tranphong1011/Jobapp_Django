from django.db import models
from django.utils.text import slugify
# Create your models here.

class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length= 50)
    country = models.CharField(max_length= 20)
    zip = models.CharField(max_length=20)
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    company= models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    
class Skills(models.Model):
    name = models.CharField(max_length=200)
class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length= 40 , unique=True) #enable indexing
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) #foreignkey : many to one relationship
    skills = models.ManyToManyField(Skills)


    def save(self, *args, **kwargs):
        if not self.id:
            # nếu ko có id thì set slug, có rồi thì ko set
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.title
    def __str__(self):
        return f"{self.title} with salary {self.salary}"