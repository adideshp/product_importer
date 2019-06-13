from django.db import models

class Document(models.Model):
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)

STATUS = (
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
)

class Product(models.Model):
    sku = models.CharField(primary_key= True, max_length=20, blank=False)
    name = models.CharField(max_length=30, blank=False, default="no name")
    description = models.TextField(blank=False, default="no description")
    status = models.CharField(choices=STATUS, max_length=10, blank=False, default="ACTIVE")
    document = models.ForeignKey(to='Document', on_delete=models.CASCADE, related_name="products", null=True)