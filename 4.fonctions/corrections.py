def limit_volume(volume):
    if volume < 0:
        return 0
    
    if volume > 100:
        return 100

    return volume

assert limit_volume(275) == 100
assert limit_volume(12) == 12