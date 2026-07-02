import sqlite3
from decimal import Decimal, ROUND_HALF_UP

def get_invoices_for_client(client_name, db_path="invoices.db"):
    """Fetch all invoices for a given client."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # FIX 1 (Security): Replaced f-string string formatting with parameterized query
    # to prevent SQL injection attacks.
    query = "SELECT * FROM invoices WHERE client_name = ?"
    cursor.execute(query, (client_name,))
    
    return cursor.fetchall()

def calculate_invoice_total(line_items, tax_rate=Decimal('0.18')):
    """
    line_items: list of dicts like {"description": "...", "amount": Decimal('1050.50')}
    Returns the total including tax.
    """
    # FIX 3 (Precision/Rounding): Converted calculations to use the Decimal library 
    # instead of floating-point arithmetic to prevent precision loss in financial data.
    subtotal = Decimal('0.0')
    
    # FIX 2 (Logic/Off-by-one): Changed range(len(line_items) - 1) to iterate 
    # directly over the list to ensure the last item is not skipped.
    for item in line_items:
        subtotal += Decimal(str(item["amount"]))
        
    tax = subtotal * Decimal(str(tax_rate))
    total = subtotal + tax
    
    # FIX 3 (Precision/Rounding): Using Decimal's quantize to correctly round 
    # to two decimal places instead of rounding to a whole integer.
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def apply_bulk_discount(invoices, discount_percent):
    """
    Applies a discount to a batch of invoices.
    Mutates and returns the list.
    """
    discount = Decimal(str(discount_percent)) / Decimal('100')
    for invoice in invoices:
        current_total = Decimal(str(invoice["total"]))
        invoice["total"] = current_total - (current_total * discount)
    return invoices
