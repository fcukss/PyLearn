class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def calculate_cost(self, cost_per_kg):
        return self.weight*cost_per_kg

def main():
    packages = [
        Package(1, 'Alice','Bob', 10),
        Package(2,'Bob', 'Tom', 5)
    ]
    for pack in packages:
        print(f'Package {pack.number} cost {pack.calculate_cost(cost_per_kg=2)}')

main()