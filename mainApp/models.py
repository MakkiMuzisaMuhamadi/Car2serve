from django.db import models

# Create your models here.
class Slides(models.Model):
    image = models.ImageField(upload_to='slide_images/')  
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.caption
    
class Staff(models.Model):
    image = models.ImageField(upload_to='slide_images/')  
    title = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Testimonials(models.Model):
    image = models.ImageField(upload_to='slide_images/')  
    proffesion = models.CharField(max_length=100, default='')
    clientname = models.CharField(max_length=100, default='')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.clientname
    
class Services(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100,)
    icon = models.CharField(max_length=50)  
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Cars(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars')
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=65, decimal_places=0)
    ENGINE_CHOICES = [
            ('Manual', 'Manual'),
            ('Automatic', 'Automatic'),
        ]
    enginetype = models.CharField(max_length=20,choices=ENGINE_CHOICES,default='Automatic')
    description = models.TextField(default='')
    fuelConsumption = models.CharField(max_length=100,default='')
    date = models.DateTimeField(auto_now_add=True)

class CarImages(models.Model):
    car = models.ForeignKey(Cars, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_other_images/')  

    def __str__(self):
        return self.car.name
class Booking(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    pickup_date = models.CharField(max_length=20)
    return_date = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer_name}"
    
class Cargo(models.Model):
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    cargo = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

