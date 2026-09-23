age = 19
limit = 18

# évaluation booléenne (condition)
print(age >= limit)     # True
print(age < limit)      # False
print(age == limit)     # True
print(age != limit)     # True

is_adult = age >= limit

# structures conditionnelles

temperature = 25

if temperature >= 30:
    print("jé cho")
    print("jé cho")
    print("jé cho")
    print("jé cho")
else:
    print("glagla")
    print("glagla")
    print("glagla")
    print("glagla")


score = 40

if score > 90:
    print("Excellent")
elif score >= 60:
    print("Validé")
else:
    print("A revoir !")

# >=
# >
# <=
# <
# ==
# !=

age = 20
has_ticket = True

can_enter = age >= 20 and has_ticket

# and
# or
# not

score = 95

if score >= 60:
    print("validé")
elif score >= 90:
    print("excellent")

if age >= 20:

    # ...

    if has_ticket:
        print("bouge ton boule")

if age >= 20 and has_ticket:
    print("bouge ton boule")
