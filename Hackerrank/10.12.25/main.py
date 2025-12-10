def getMoneySpent(keyboards, drives, b):
      # Write your code here.
    #start
    new = []
    new1 = []
    for i in keyboards:
        for j in drives:
            sum_kd = i + j
            new.append(sum_kd)
    for k in new:
        if k <= b:
            new1.append(k)
    if new1 == []:
        print(-1)
    else:
        max_spend = max(new1)
        print(max_spend)
    #end

getMoneySpent([40,50,60],[5,8,12],60)

def catAndMouse(x, y, z):
    #write your code here
    #start
    distancec1 = abs(x-z)
    distancec2 = abs(y-z)
    if distancec1 == distancec2:
        print("Mouse C")
    elif distancec1 > distancec2:
        print("Cat B")
    elif distancec2 > distancec1:
        print("Cat A")
    #end
catAndMouse(1,2,3)
catAndMouse(1,3,2)