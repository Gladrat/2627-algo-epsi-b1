# Exercice — Limiter un volume

def limit_volume(volume):
    if volume < 0:
        return 0
    
    if volume > 100:
        return 100

    return volume

assert limit_volume(275) == 100
assert limit_volume(12) == 12
assert limit_volume(-50) == 0

# ##################################
# Exercice bonus - refactorisation #
# ##################################

duration = 99999999

hours = duration // 3600
remaining = duration % 3600
minutes = remaining // 60
secondes = remaining % 60

print(hours, minutes, secondes)

# ####################################
# Exercice bonus - refactorisation 2 #
# ####################################

quantity = 4
unit_price = 25
is_member = True
express = True

subtotal = quantity * unit_price

if is_member:
    subtotal = subtotal * 0.90

shipping = 5
if express:
    shipping = shipping + 8

total = subtotal + shipping

print(total)