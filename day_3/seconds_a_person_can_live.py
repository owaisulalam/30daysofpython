# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

years = int(input("Enter number of years you have lived: "))
seconds = years * 60 * 60 * 24 * 365
print("You have lives for ", seconds, "seconds.")