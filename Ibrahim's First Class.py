Name = input("Enter Your Name")
print(f"This is {Name}'s First Class.")
print(f"Hello {Name}. How are you feeling?")
Answer = input()
print("It's good to know that you are feeling", Answer)
age = input("What is your age?\n")
Friend = input("What is your Friend's Name?\n")
FriendAge = input(f"What is your {Friend}'s Age?\n")
Difference = abs(int(age) - int(FriendAge))
print(f"It's Good to know {Name} that Your Age is {age} and Your Friend {Friend}'s age is {FriendAge} and the age difference is {Difference}")
if age > FriendAge:
    print(f"Congrats! {Name} is elder than {Friend} and is {Difference} years older.")
elif FriendAge > age:
    print(f"Congrats! {Name} is younger than {Friend} and {Friend} is {Difference} years older.")
else:
    print(f"Bingo! {Name} and {Friend}'s age are same.")