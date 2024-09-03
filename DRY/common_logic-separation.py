# utils.py
def apply_percentage(base, percentage):
    return base + (base * percentage / 100)

# main.py
from utils import apply_percentage

def calculate_discounted_price(price, discount):
    return apply_percentage(price, -discount)

def calculate_taxed_price(price, tax_rate):
    return apply_percentage(price, tax_rate)
