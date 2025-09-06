from datetime import datetime

# Store and invoice details
store_name = "D-Mart"
store_address = "Avenue Supermarts Ltd.\nDMART PANVEL\nPlot No. 42 & 45, Sector 5, Opp. Pragnapati Garden,\nNear Railway Phatak, New Panvel (E)\nPhone: 022-27491104"
gstin = "27AACCD4834H1ZE"
fssai = "1151101900678"
cashier = "NBE011461"
bill_no = "420210102-003109"
bill_date = datetime(2019, 12, 14, 9, 45)

# Items purchased
items = [
    {"desc": "TMT R MCPQPL", "qty": 2, "rate": 199.00, "amount": 398.00},
    {"desc": "STOLE LVS VIS DM", "qty": 1, "rate": 149.00, "amount": 149.00},
    {"desc": "ZERI PLAIN COTN CLOTH", "qty": 1, "rate": 39.00, "amount": 39.00},
    {"desc": "SUPERMAX 3 DIS TR-RS", "qty": 2, "rate": 33.50, "amount": 67.00}
]

# GST breakdown (Example values)
gst_details = [
    {"taxable": 520.98, "cgst": 13.02, "sgst": 13.02, "total": 547.00},
    {"taxable": 14.28, "cgst": 0.86, "sgst": 0.86, "total": 16.00},
    {"taxable": 76.28, "cgst": 0.86, "sgst": 0.86, "total": 653.00}
]

# Total amount
total_amount = 653.00

# Generate bill
def print_line(char='-', length=60):
    print(char * length)

def print_bill():
    print(f"{store_name.center(60)}")
    print(store_address)
    print(f"GSTIN: {gstin}   FSSAI No: {fssai}")
    print_line()
    print(f"Bill No: {bill_no}   Date: {bill_date.strftime('%d/%m/%Y %I:%M%p')}")
    print(f"Cashier: {cashier}")
    print_line()
    print(f"{'Item Description':30} {'Qty':>3} {'Rate':>8} {'Amount':>8}")
    print_line()
    for item in items:
        print(f"{item['desc']:30} {item['qty']:>3} {item['rate']:>8.2f} {item['amount']:>8.2f}")
    print_line()
    print(f"{'Total':>50} {total_amount:>8.2f}")
    print_line()
    print("GST Breakup Details")
    print(f"{'Taxable':>10} {'CGST':>10} {'SGST':>10} {'Total':>10}")
    for gst in gst_details:
        print(f"{gst['taxable']:>10.2f} {gst['cgst']:>10.2f} {gst['sgst']:>10.2f} {gst['total']:>10.2f}")
    print_line()
    print(f"Card Payment: Rs. {total_amount:.2f}")
    print("* Saved Rs. 206.00 On MRP *")
    print_line('=')

# Run the bill
print_bill()
