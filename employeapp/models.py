from django.db import models


class Company(models.Model):
    company_name=models.CharField(max_length=500)
    established_year=models.CharField(max_length=500)
    
    def __str__(self):
        return self.company_name
    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    experiance=models.CharField(max_length=100)
    description=models.TextField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} of employee{self.company.company_name}"