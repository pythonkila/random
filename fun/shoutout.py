# 10 May 2020
# The code takes in an input ( a greeting ) and shout out greeting n number of time.

hail = input('Enter your shoutout!...').upper()                                  
while hail.isalpha() == False:
    hail = input('Enter a valid shoutout!...').upper()    
reps = input('How many Gbosa !...')
while reps.isdigit()  == False:
    reps = input('How many time will you want this repeated...')
for x in hail:
    if x in 'AEIOU':
        print('Can i get an',x,'!')
    elif x not in 'AEIOU':
        print('Can i get a',x,'!')
reps = int(reps)
print('Can I get',reps,'Gbosa for my fellow!')
while reps > 0:
    print(reps,'Gbosa for',hail.upper()+'!')
    reps -= 1    
