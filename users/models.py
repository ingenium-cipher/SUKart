from django.db import models
from django.contrib.auth.models import User
import uuid
import PIL
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

STATUS_OPTIONS = (('P', 'Order Placed'), ('S', 'Shipped'), ('O', 'Out for Delivery'), ('D', 'Delivered'))

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ShoppingUser(models.Model):
    user_detail = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    DOB = models.DateField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.name} residing in {self.city}, {self.state}"

class DeliveryAgent(models.Model):
    agent_detail = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    DOB = models.DateField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.name} delivering in {self.city}, {self.state}"

class Company(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, related_name='company_product', on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return f"{self.title} of company {self.company} in category {self.category}"

    def save(self):
        im = Image.open(self.image)
        output = BytesIO()
        print("hoi")

		#Resize/modify the image
        im = im.resize((353, 353))

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Product,self).save()

class ProductStatus(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    shopping_user = models.OneToOneField(ShoppingUser, on_delete=models.CASCADE)
    agent = models.OneToOneField(DeliveryAgent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)

    def __str__(self):
        return f"{self.product} has status {self.status}"
