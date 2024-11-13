from django.test import TestCase

# Create your tests here.

class InvestmentFund(TestCase):
    def setUp(self):
        InvestmentFund.objects.create(
            fund_name='Dana MB',
            fund_manager_name='MB Selangor',
            fund_desc='Dana ini adalah Dana MB',
            fund_net_asset_value=1.0,
            fund_created_date='2020-01-01',
            fund_performance=1.0
        )

    def test_investment_fund(self):
        investment_fund = InvestmentFund.objects.get(fund_name='Dana MB')
        self.assertEqual(investment_fund.fund_name, 'Dana MB')
        self.assertEqual(investment_fund.fund_manager_name, 'MB Selangor')
        self.assertEqual(investment_fund.fund_desc, 'Dana ini adalah Dana MB')
        self.assertEqual(investment_fund.fund_net_asset_value, 1.0)
        self.assertEqual(investment_fund.fund_created_date, '2020-01-01')
        self.assertEqual(investment_fund.fund_performance, 1.0)