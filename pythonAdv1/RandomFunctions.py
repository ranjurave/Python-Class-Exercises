import random
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print(days[random.randrange(0,6)])
print("From choice",random.choice(days))
random.shuffle(days)
print(days)
print(random.random())