import sys

#Jason Schriner
#10/24/24
#Assignemnt 1.3

#Create countdown function
def countdown(bottles):
    while bottles > 1:
      #Prints song than subtracts 1 exits at 1
      print(f"{bottles} bottles of beer on the wall,")
      print(f"{bottles} bottles of beer on the wall,")
      print("Take one down and pass it around,")
      print(f"There are {bottles -1} bottles of beer on the wall.")
      print()
      bottles -= 1
      #Prints last verse of song
    if bottles == 1:
      print(f"{bottles} bottle of beer on the wall,")
      print(f"{bottles} bottle of beer on the wall,")
      print("Take one down and pass it around,")
      print("There are no bottles of beer on the wall.")
      print()
      bottles -= 1
      #Prints there is no more beer and calls main function
    if bottles == 0:
      print("No bottles of beer on the wall ")
      print("Buy more beer ")
      print(" ")
      main()
      
#Create main function
def main():
  #Ask user for input and validates data
  try:
    bottles = int(input("How many bottles are on the wall? "))
  except ValueError:
    print("Please enter a number")
    bottles = int(input("How many bottles are on the wall? "))
  
  #Calls countdown function if greater than 0
  #If 0 exits program
  #If less than 0 prints error message and calls main function
  if bottles > 0:
    countdown(bottles)
  elif bottles == 0:
    print(" ")
    print("Terminated with exit code 0")
    sys.exit()
  else:
    print(" ")
    print("Please enter a positive number")
    main()

if __name__ == "__main__":
  main()

# I tried to code the program with a for loop and if statements the if == 1 worked but
# the if == 0 did not work. So I used a while loop instead.