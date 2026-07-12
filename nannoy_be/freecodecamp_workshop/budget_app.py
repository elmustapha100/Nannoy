class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"[:7]
            lines.append(f"{desc:<23}{amt:>7}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    spent_per_category = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_per_category.append(spent)

    total_spent = sum(spent_per_category)
    percentages = [
        int((spent / total_spent) * 100 // 10 * 10) if total_spent else 0
        for spent in spent_per_category
    ]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    chart += "    " + "-" * ((len(categories) * 3) + 1) + "\n"

    max_name_len = max(len(category.name) for category in categories)
    for i in range(max_name_len):
        chart += "     "
        for category in categories:
            chart += category.name[i] + "  " if i < len(category.name) else "   "
        chart += "\n" if i != max_name_len - 1 else ""

    return chart