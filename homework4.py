#This is my python file for homework 4 assignment. 

#part 2.1
def part1lst (r1, r2):
    return [item for item in range (r1, r2+1)]
r1, r2 = 0, 50
print (part1lst(r1, r2))

#part 2.2
def square (part2lst):
    return [i ** 2 for i in part2lst]
part2lst = (2,3,4)
print (square (part2lst))
# i made a typo on the list name

#part 2.3
part3lsta = (1,2,3,4,5,6,7,8,9,10)
part3lstb = (20,21,22,23,24,25,26,27,28,29,30)
def oddlsta (part3lsta):
    return [ item for item in part3lsta if item % 2 == 1]

def oddlstb (partslstb):
    return [ item for item in partslstb if item % 2 == 1]

print ((oddlsta (part3lsta))+(oddlstb (part3lstb)) )

#this one gave me so many errors all saying something i wrote didn't exist, and it was because I made typos. 


# part 3.1
part31list = []
count = 1

for i in range (5):
    row = []
    for j in range (5):
        row.append(count)
        count +=1
    part31list.append(row)

for row in part31list:
    print (row)


# part 4




# part 3.2

for i in range (5):
    for j in range (5):
        if part31list [i][j] % 3 == 0:
            part31list[i][j] = "?"

for row in part31list:
    print (row)



def removeDuplicates(part4listin):
    part4listout = []
    seen = set()

    for item in part4listin:
        if item not in seen:
            part4listout.append(item)
            seen.add(item)

    return part4listout
    
part4listin = [1,1,2,3,4,4]
print(removeDuplicates(part4listin))

#here i didnt get an error, but the result was just a list with [1], so I had to fix the syntax to get the right product.
 



    