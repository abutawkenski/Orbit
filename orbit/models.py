from django.db import models


# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='about/')
    c_plus = models.IntegerField()
    python = models.IntegerField()
    html = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to="portfolio/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Server(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=200)
    office = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_time = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Cleant(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to="clent/")
    massenge = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    massage = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


from django.db import models

# Create your models here.
