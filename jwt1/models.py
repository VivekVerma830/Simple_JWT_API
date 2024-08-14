from django.db import models

# Create your models here.
class BankModel(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name
    

class UserModel(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_contact = models.IntegerField(max_length=10)

    def __str__(self):
        return self.user_name