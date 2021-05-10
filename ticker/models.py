from django.db import models

# Create your models here.


class Ticker(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class History(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return str(self.id)
