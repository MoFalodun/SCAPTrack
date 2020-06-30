# This prints the lyrics of 99 bottles using the string formatting method. Thank you.

bottle = 100
bottles = 99
bottle_left = bottle-1
#loop == 1

for i in range(0,100):
    bottle-= 1 #To loop in decreasing order
    bottle_left = bottle - 1
    if bottle > 2:
         print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer. Take one down and pass it around.")
         print(f"{bottle_left} bottles of beer on the wall.")
    elif bottle ==2:
        print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer. Take one down and pass it around.")
        print(f"{bottle_left} bottle of beer on the wall.")
    elif bottle == 1:
        print(f"{bottle} bottle of beer on the wall, {bottle} bottle of beer. Take one down and pass it around.")
        #print("No more bottles of beer on the wall.")
    else:
        print("No more bottles of beer on the wall, no more bottles of beer")
        print("Go to the store and buy some more", "," f"{bottles} bottles of beer on the wall")
