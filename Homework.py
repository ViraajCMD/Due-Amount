def calculate_due_amount(total_bill, amount_paid):
    change_due = amount_paid - total_bill
    return change_due

bill_amount = 2.50
paid_amount = 4.00

change_to_return = calculate_due_amount(bill_amount, paid_amount)

print(f"The shopkeeper should return: ${change_to_return:.2f}")
