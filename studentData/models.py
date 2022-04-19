from pyexpat import model
import random
import string
from django.db import models
import uuid

def generate_unique_code():
    length = 7
    code = ''.join(random.choices(string.digits, k=length))
    return code

class Certificate(models.Model):
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    studentId = models.CharField(max_length=100)
    date = models.DateField()
    event = models.CharField(max_length=100, blank=True)
    certificateId = models.CharField(max_length=100, blank=True) 
    certificateURL = models.URLField(max_length=256, blank=True)
1