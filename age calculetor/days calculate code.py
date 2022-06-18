print('answer the question to know how long youhave lived in life...')
name=input('Name')
print('what is your age?',(name),'?')
age=int(input('age'))
days=age*365
print(days)
minutes=age*525948
print(minutes)
seconds=age*31556926
print(seconds)

print(f"{name} has been alive for {days} days {minutes} minutes {seconds} seconds")