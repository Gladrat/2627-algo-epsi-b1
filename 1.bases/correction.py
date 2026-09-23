# base_points = int(input("Quel est le score ? "))
base_points = 120
multiplier = 1.5
bonus = 40

final_score = base_points * multiplier
final_score = final_score + bonus

print(final_score)

f_s = 120 * 1.5 + 40
print(f_s)

print(120 * 1.5 + 40)

print("=" * 20)

# ======================

red = 140
green = 254
blue = 12

color = red * 65536 + green * 256 + blue

print(color)

red = color // 65536
rest = color % 65536
green = rest // 256
blue = rest % 256

print(red, green, blue)