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

# Create a class for monthlyStatments with a Unique ID, clubID, date, amount
class MonthlyStatement(models.Model):
    statementID = models.AutoField(primary_key=True)
    clubID = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return self.clubID.clubName