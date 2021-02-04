from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pursose = models.TextField()
    terget = models.TextField()
    course = models.TextField()
    textbook = models.TextField()
    evaluation = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    time = models.CharField(max_length=20)
    t_mail = models.CharField(max_length=200)
    subjecturl =  models.TextField()
    sllabus = models.TextField()
    homework = models.TextField()
    lesson = models.TextField()
    regi = models.CharField(max_length=5)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def isregi(self):
        self.regi="1"
        self.save()
        return self.regi
        
    def notregi(self):
        self.regi='0'
        self.save()

class Post2(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pursose = models.TextField()
    terget = models.TextField()
    course = models.TextField()
    textbook = models.TextField()
    evaluation = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    time = models.CharField(max_length=20)
    t_mail = models.CharField(max_length=200)
    subjecturl =  models.TextField()
    sllabus = models.TextField()
    homework = models.TextField()
    lesson = models.TextField()
    regi = models.CharField(max_length=5)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title

    def isregi(self):
        self.regi="1"
        self.save()

    def notregi(self):
        self.regi='0'
        self.save()

    
class Post3(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pursose = models.TextField()
    terget = models.TextField()
    course = models.TextField()
    textbook = models.TextField()
    evaluation = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    time = models.CharField(max_length=20)
    t_mail = models.CharField(max_length=200)
    subjecturl =  models.TextField()
    sllabus = models.TextField()
    homework = models.TextField()
    lesson = models.TextField()
    regi = models.CharField(max_length=5)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title

    def isregi(self):
        self.regi="1"
        self.save()

    def notregi(self):
        self.regi='0'
        self.save()

        
class Post4(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pursose = models.TextField()
    terget = models.TextField()
    course = models.TextField()
    textbook = models.TextField()
    evaluation = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    time = models.CharField(max_length=20)
    t_mail = models.CharField(max_length=200)
    subjecturl =  models.TextField()
    sllabus = models.TextField()
    homework = models.TextField()
    lesson = models.TextField()
    regi = models.CharField(max_length=5)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title

    def isregi(self):
        self.regi="1"
        self.save()

    def notregi(self):
        self.regi='0'
        self.save()


class Post5(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pursose = models.TextField()
    terget = models.TextField()
    course = models.TextField()
    textbook = models.TextField()
    evaluation = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    time = models.CharField(max_length=20)
    t_mail = models.CharField(max_length=200)
    subjecturl =  models.TextField()
    sllabus = models.TextField()
    homework = models.TextField()
    lesson = models.TextField()
    regi = models.CharField(max_length=5)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
   
    def __str__(self):
        return self.title

    def isregi(self):
        self.regi="1"
        self.save()

    def notregi(self):
        self.regi='0'
        self.save()

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Chatpost(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment1(models.Model):
    chatpost = models.ForeignKey('blog.Chatpost', on_delete=models.CASCADE, related_name='comment1s')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
