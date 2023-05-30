import random
print("Hello\n")
while True:
    print("choose a Option :\n1) Start Game \n2)Exit")
    choice = input("Enter a choose :")
    if choice == "1":
        print("Dice : " + str(random.randint(1,7)))
    elif choice == "2":
        print("good luck")
        break
    else:
        print("please choose correct number!")      