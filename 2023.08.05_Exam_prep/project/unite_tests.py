# App increase_loan_interest method - clients with loans

from unittest import TestCase, main
from project.bank_app import BankApp


class TestBankAppClass(TestCase):
    def test_increase_loan_interest(self):
        self.ba = BankApp(5)

        # increases interest of not granted loans only
        self.ba.add_loan('StudentLoan')
        self.ba.add_loan('MortgageLoan')
        self.ba.add_loan('StudentLoan')
        self.ba.add_client('Student', 'Test Name', '0123456789', 500.0)
        self.ba.add_client('Adult', 'Test Name2', '1234567899', 1500.0)

        self.assertEqual(len(self.ba.loans), 3)
        self.assertEqual(self.ba.loans[0].interest_rate, 1.5)
        self.assertEqual(self.ba.loans[1].interest_rate, 3.5)
        self.assertEqual(self.ba.loans[2].interest_rate, 1.5)

        self.ba.grant_loan('StudentLoan', '0123456789')
        self.assertEqual(len(self.ba.loans), 2)
        self.assertEqual(self.ba.loans[0].interest_rate, 3.5)
        self.assertEqual(self.ba.loans[1].interest_rate, 1.5)
        self.assertEqual(self.ba.clients[0].loans[0].interest_rate, 1.5)

        res = self.ba.increase_loan_interest('StudentLoan')
        self.assertEqual(len(self.ba.loans), 2)
        self.assertEqual(self.ba.loans[0].interest_rate, 3.5)
        self.assertEqual(self.ba.loans[1].interest_rate, 1.7)
        self.assertEqual(self.ba.clients[0].loans[0].interest_rate, 1.5)    # INCORRECT!
        self.assertEqual(res, "Successfully changed 1 loans.")
        #
        # res = self.ba.increase_loan_interest('MortgageLoan')
        # self.assertEqual(len(self.ba.loans), 2)
        # self.assertEqual(self.ba.loans[0].interest_rate, 4.0)
        # self.assertEqual(self.ba.loans[1].interest_rate, 1.7)
        # self.assertEqual(self.ba.clients[0].loans[0].interest_rate, 1.5)
        # self.assertEqual(res, "Successfully changed 1 loans.")
        #
        # 0 loans interests increased
        # self.ba.grant_loan('StudentLoan', '0123456789')
        # self.assertEqual(len(self.ba.loans), 1)
        # self.assertEqual(self.ba.loans[0].interest_rate, 4.0)
        # res = self.ba.increase_loan_interest('StudentLoan')
        # self.assertEqual(self.ba.loans[0].interest_rate, 4.0)
        # self.assertEqual(res, "Successfully changed 0 loans.")
        # self.assertEqual(self.ba.clients[0].loans[0].interest_rate, 1.5)
        # self.assertEqual(self.ba.clients[0].loans[1].interest_rate, 1.7)
        #
        # self.ba.grant_loan('MortgageLoan', '1234567899')
        # self.assertEqual(len(self.ba.loans), 0)
        # res = self.ba.increase_loan_interest('MortgageLoan')
        # self.assertEqual(res, "Successfully changed 0 loans.")
        # self.assertEqual(self.ba.clients[0].loans[0].interest_rate, 1.5)
        # self.assertEqual(self.ba.clients[1].loans[0].interest_rate, 4.0)
        # self.assertEqual(self.ba.clients[0].loans[1].interest_rate, 1.7)


if __name__ == '__main__':
    main()
