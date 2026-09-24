entered_pin = "3812"
expected_pin = "3812"
is_blocked = True

can_open = entered_pin == expected_pin and not is_blocked

if can_open:
    print("ouverture")
else:
    print("accès refusé")

# =========================================

age = 21
is_student = True
is_weekend = True

if age < 6:
    price = 0
elif age < 18:
    price = 12
elif is_student:
    price = 16
else:
    price = 20

if price > 0 and is_weekend:
    price += 2

print(price)