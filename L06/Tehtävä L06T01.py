# Tehtävä L06T01


def showtime(seconds):
    hours = seconds // (60*60)
    seconds = seconds % (60*60)
    minutes = seconds // 60
    seconds = seconds % 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)

print(showtime(500))
print(showtime(10000))
print(showtime(121000))