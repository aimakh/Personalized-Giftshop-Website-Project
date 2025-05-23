from django.db import models
from django.contrib.auth.models import User


# CREATE TABLE Customer (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(100),
#     last_name VARCHAR(100),
#     email VARCHAR(254), -- Django EmailField default
#     phone_number VARCHAR(15)
# );



class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# CREATE TABLE Product (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     price DECIMAL(10, 2),
#     description TEXT,
#     image VARCHAR(100), -- Path to image file
#     quantity_in_stock INTEGER DEFAULT 0
# );



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    quantity_in_stock = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name



# CREATE TABLE "Order" (
#     id SERIAL PRIMARY KEY,
#     user_id INTEGER REFERENCES auth_user(id) ON DELETE SET NULL, -- Django's built-in User model
#     guest_name VARCHAR(100),
#     guest_email VARCHAR(254),
#     customer_address TEXT,
#     ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     status VARCHAR(50) DEFAULT 'Pending'
# );

class Order(models.Model):
    # For logged-in users
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # For guest users
    guest_name = models.CharField(max_length=100, null=True, blank=True)
    guest_email = models.EmailField(null=True, blank=True)

    # Common fields
    customer_address = models.TextField(null=True, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user or self.guest_email or self.guest_name}"



# CREATE TABLE OrderItem (
#     id INT PRIMARY KEY,
#     order_id INTEGER REFERENCES "Order"(id) ON DELETE CASCADE,
#     product_id INTEGER REFERENCES Product(id) ON DELETE CASCADE,
#     quantity INTEGER DEFAULT 1 CHECK (quantity >= 1),
#     customization TEXT
# );


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customization = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} for Order #{self.order.id}"



# CREATE TABLE GuestCart (
#     id SERIAL PRIMARY KEY,
#     email VARCHAR(254),
#     name VARCHAR(100),
#     cart_data JSON, 
#     saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

class GuestCart(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    cart_data = models.JSONField()
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.email} saved at {self.saved_at}"
