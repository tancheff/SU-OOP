from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        self.loans.append(self.VALID_LOANS[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(self.VALID_CLIENTS[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client: BaseClient = next(filter(lambda client: client.client_id == client_id, self.clients), None)
        loan: BaseLoan = next(filter(lambda loan: loan.__class__.__name__ == loan_type, self.loans), None)

        if client.allowed_loan != loan_type:
            "Inappropriate loan type!"

        client.loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str):
        client: BaseClient = next(filter(lambda client: client.client_id == client_id, self.clients), None)

        if not client:
            raise Exception("No such client!")

        if len(client.loans) != 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = sum([len(client.loans) for client in self.clients])
        granted_sum = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) \
            if self.clients else sum([client.interest for client in self.clients])

        return (f"Active Clients: {total_clients_count}\n"
                f"Total Income: {total_clients_income:.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
