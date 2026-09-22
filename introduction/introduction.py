duration = 99999999

hours = duration // 3600
remaining = duration % 3600
minutes = remaining // 60
secondes = remaining % 60

print(hours, minutes, secondes)