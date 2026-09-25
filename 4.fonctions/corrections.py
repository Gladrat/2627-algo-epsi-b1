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

# Refactorisation

def convert_duration(duration):
    hours = duration // 3600
    remaining = duration % 3600
    minutes = remaining // 60
    secondes = remaining % 60

    # print(hours, minutes, secondes)
    return (hours, minutes, secondes)

# Refactorisation 2

# ! Todo : Correction