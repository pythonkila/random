# 09 May 2020
# The code takes in an input ( a greeting ) and shout out greeting n number of time.

hail = input('Enter your shoutout!...').upper()
reps = int(input('how many time will you want this repeated...'))
for x in hail.lower():
    if x in 'aeiou':
        print('Can i get an',x,'!')
    elif x not in 'aeiou':
        print('Can i get a',x,'!')
while reps > 0:
    print(hail.upper()+'!')
    reps -= 1
