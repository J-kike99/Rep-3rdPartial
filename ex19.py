def cheese_and_crackers(cheese_count , boxes_of_cracker):
    print(f"You have {cheese_count} Cheeses!")
    print(f"You have {boxes_of_cracker} boxes of cracker")
    print("Man that's enough for a party")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20 , 30)


print("OR , we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese , amount_of_crackers)

print("And we can combine the two , variables and math:")
cheese_and_crackers(amount_of_cheese * 100 , amount_of_crackers + 1000)