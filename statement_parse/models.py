from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.TextField('Human readable name of account')
    slug = models.SlugField()

    number = models.IntegerField("Bank account number")
    bank = models.TextField(default="")

    def __unicode__(self):
        return self.name

class Transaction(models.Model):
    date = models.DateTimeField('Date the transcation occured')
    type = models.CharField('The type of trasaction', max_length=20)
    amount = models.DecimalField('Amount moved', max_digits=20, decimal_places=2)

    account = models.ForeignKey('Account')

