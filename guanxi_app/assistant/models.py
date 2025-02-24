import uuid
from django.db import models

class VirtualAssistent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100, null=True, blank=True)
    personality = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Directive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField()
    answer = models.TextField()
    directive = models.ForeignKey('Directive', on_delete=models.CASCADE, related_name='directive_ref', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    virtual_assistant = models.ForeignKey('VirtualAssistent', on_delete=models.CASCADE, null=True, blank=True)
