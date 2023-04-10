from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Cases(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    case_type=models.CharField(max_length=20)
    start_date=models.DateField(null=True)
    demandante=models.CharField(max_length=30)
    demandado=models.CharField(max_length=30)
    juzgado=models.CharField(max_length=100)
    partido_judicial=models.CharField(max_length=30)
    phase=models.CharField(max_length=30)
    lawyers=models.ManyToManyField(User)
    cont_lawyer_one=models.CharField(max_length=30)
    cont_lawyer_two=models.CharField(max_length=30, blank=True)
    cont_lawyer_three=models.CharField(max_length=30, blank=True)
    procurador_one=models.CharField(max_length=30)
    procurador_two=models.CharField(max_length=30, blank=True)
    procurador_three=models.CharField(max_length=30, blank=True)
    pc_one=models.CharField(max_length=30)
    pc_two=models.CharField(max_length=30, blank=True)
    pc_three=models.CharField(max_length=30, blank=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Case"
        verbose_name_plural="Cases"
        
class CaseComments(models.Model):
    id=models.AutoField(primary_key=True)
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    case_id=models.ForeignKey(Cases, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.case_id.name + " - " + self.created.strftime('%m/%d/%Y')
    
    class Meta:
        verbose_name="CaseComment"
        verbose_name_plural="CaseComments"

class CasePresentations(models.Model):
    id=models.AutoField(primary_key=True)
    description=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    presentation_date=models.DateField(null=True, blank=True)
    case_id=models.ForeignKey(Cases, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.case_id.name + " - " + self.presentation_date.strftime('%m/%d/%Y')
    
    class Meta:
        verbose_name="Presentación"
        verbose_name_plural="Presentaciones"
    
class Documents(models.Model):
    title=models.CharField(max_length=100)
    doc=models.ImageField(upload_to='docs/')
    created=models.DateTimeField(auto_now_add=True)
    case_id=models.ForeignKey(Cases, on_delete=models.CASCADE)
    
    
    
    
def get_full_name(self):
    return self.first_name + " " + self.last_name
    

User.add_to_class("__str__", get_full_name)