class Appliance:
    def __init__(self, cost: float):
        self.cost = cost  # per day

    def get_monthly_expense(self):
        return 30 * self.cost
