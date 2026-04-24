from django.db import models
import uuid
from datetime import timedelta

# Create your models here.
#class ExampleModel(models.Model):
   # id = models.AutoField(primary_key=True) #Auto-incrementing ID
   # big_id = models.BigAutoField()
   # big_integer = models.BigIntegerField(default=123456789)
   # is_active = models.BooleanField(default=True)
   # title = models.CharField(max_length=200)
   # publish_date = models.DateField()
   # created_at = models.DateTimeField(auto_now_add=True)
   # price = models.DecimalField(max_digits=10, decimal_places=2)
   # duration = models.DurationField(default=timedelta(days=1))
   # email = models.EmailField()
   # file = models.FileField(upload_to='documents/')
   # image = models.ImageField(upload_to='images/')
   # rating = models.FloatField(default=4.5)
   # age = models.IntegerField()
   # stock = models.PositiveIntegerField(default=10)
   # rank = models.PositiveSmallIntegerField(default=1)
   # slug = models.SlugField(unique=True)
   # count = models.SmallIntegerField(default=5)
   # description = models.TextField()
   # opening_time = models.TimeField()
   # website = models.URLField()
   # uuid = models.UUIDField(default=uuid.uuid4, unique=True)
   # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   # tags = models.ManyToManyField('Tag')
   # profile = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    
#class Tag(models.Model):
    #name = models.CharField(max_length=50)
    