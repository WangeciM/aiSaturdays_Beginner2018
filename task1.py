import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList

#elemets of ourList that are below 5

belowFive = [num for num in ourList if num<5]

print(belowFive)
