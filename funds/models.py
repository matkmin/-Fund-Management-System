from django.db import models

# Create your models here.
class InvestmentFund(models.Model):
    fund_id = models.AutoField(primary_key=True)
    fund_name = models.CharField(max_length=100)
    fund_manager_name = models.CharField(max_length=100)
    fund_desc = models.TextField()
    fund_net_asset_value = models.DecimalField(max_digits=10, decimal_places=2)
    fund_created_date = models.DateField(auto_now_add=True)
    fund_performance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.fund_name