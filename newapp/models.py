from django.db import models as m

# Create your models here.
#from django.db import models as m
                                                                                          
                                                                                          
class Post(m.Model):                                                                      
    content = m.CharField(max_length=256)                                                 
    created_at = m.DateTimeField('Datetime created')                                      
                                                                                          
                                                                                          
class Comment(m.Model):                                                                   
    post = m.ForeignKey(Post)                                                             
    message = m.TextField()                                                               
    created_at = m.DateTimeField('Datetime created')
