from django.db import models

# Create your models here.
# Create a class for a club with a Unique ID, name, cardNum, ExpDate, DiscountRate
class Club(models.Model):
    clubID = models.AutoField(primary_key=True)
    clubName = models.CharField(max_length=50)
    cardNum = models.CharField(max_length=16)
    expDate = models.DateField()
    discountRate = models.FloatField()

    def __str__(self):
        return self.clubName


class MonthlyStatement(models.Model):
    statementID = models.AutoField(primary_key=True)
    clubID = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return self.clubID.clubName

class UserAccount(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.userName