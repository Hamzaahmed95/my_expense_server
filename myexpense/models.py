from django.db import models

class HomeExpense(models.Model):
    month=models.CharField(max_length=50)
    amount_send=models.DecimalField(max_digits=19, decimal_places=2)
    amount_received=models.DecimalField(max_digits=19, decimal_places=2)
    sent_date=models.DateField()
    channel = models.CharField(max_length=50)
    rates = models.DecimalField(max_digits=19, decimal_places=2)
    
    # def __str__(self):
    #     return '%s %d %d %s %s %d' % (self.month, self.amount_send, self.amount_received, self.sent_date,self.channel, self.rates)
               