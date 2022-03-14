from django.db import models

class feedback(models.Model):
    GENDER = (('M', 'Male'),
        ('F', 'Female'),)
    Name=models.CharField(max_length=30)
    Address=models.CharField(max_length=50)
    Mobile_Number=models.IntegerField()
    Gender=models.CharField(max_length=1,choices=GENDER)
    Customer_id=models.IntegerField()
    feedback=models.TextField(max_length=500)
    
    class Meta:  
        db_table = "Customer_FeedBack"
