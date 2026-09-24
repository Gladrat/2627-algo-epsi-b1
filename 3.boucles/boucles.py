# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

print("="*20)
 
# borne de fin : n-1
# range(debut, fin) → créer un intervalle entre début et fin-1



# total = 0

for i in range(1051):
    # total = total + i
    print(i)

# print(total)

i = 50
while i < 1050: # evaluation de condition
    i = i + 3
    print(i)

for row in range(3):
    for column in range(5):
        print(row, column)