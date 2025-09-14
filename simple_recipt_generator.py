Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def item_total(price, qty):
...     return price * qty
... 
... grand_total = 0
... 
... print("----- Receipt -----")
... 
... while True:
...     item = input("Enter item name (or type 'done' to finish): ")
...     if item.lower() == "done":
...         break
...     qty = int(input("Enter quantity: "))
...     cost = float(input("Enter price per item: "))
...     total = item_total(cost, qty)
...     print(f"{item} x{qty} @ ${cost:.2f} each: ${total:.2f}")
...     grand_total += total
... 
... print("-------------------")
