from django.db import models

# Create your models here.
class Customer(models.Model):
    main_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}"

