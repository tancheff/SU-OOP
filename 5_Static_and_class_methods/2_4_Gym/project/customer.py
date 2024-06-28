from project.class_id_mixin import ClassIdMixin


class Customer(ClassIdMixin):
    id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id: int = Customer.get_next_id()

    def __repr__(self):
        return (f"Customer <{self.id}> {self.name}; "
                f"Address: {self.address}; Email: {self.email}")


c1 = Customer("n1", "a1", "e1")
c2 = Customer("n1", "a1", "e1")

print(c1.id)
print(c2.id)