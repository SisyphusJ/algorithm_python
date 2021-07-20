ls = int(input())
cs = int(input())
os = cs - ls
if os <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 < os <= 20:
    print("You are speeding and your fine is $100.")
elif 20 < os <= 30:
    print("You are speeding and your fine is $270.")
elif 30 < os:
    print("You are speeding and your fine is $500.")
