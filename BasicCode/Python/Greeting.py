import datetime
import random
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good night"

print("{}!".format(greeting))


hour1 = datetime.datetime.now().hour
greeting3 = "Have a nice day" if hour1<20 else "Good night"
print(random.choice(["I look forward to our next meeting!",greeting3+"!"]))