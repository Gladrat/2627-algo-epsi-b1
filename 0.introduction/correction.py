quantity = int(input("Combien de place fréro ? "))
unit_price = 32
fixed_fees = 2.5
service_rate = 0.05

ticket_price = quantity * unit_price
service_fee = ticket_price * service_rate
total = ticket_price + service_fee + fixed_fees

print(total, "€")