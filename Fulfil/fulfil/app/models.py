from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = (
    ("COMPLETED", "Completed"),
    ("INPROGRESS", "In Progress"),
)

class Document(models.Model):
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    elements = models.IntegerField(blank=False, default=0)
    status = models.CharField(choices=STATUS, max_length=20, blank=False, default="INPROGRESS")

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

"""
@receiver(post_save, sender=Product)
def schedule_task_post_save(sender, instance, created, **kwargs):
    from django_eventstream import send_event
    send_event('test', 'message', {'sku': 'Hello'})
    #send_event('test', 'message', {'sku': str(instance.sku), 'total': str(instance.document.elements)})
"""