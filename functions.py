#Creating a function helps you get something created to prevent writing the same thing over and over like this:
print("Words and Things")

#some statements
x = 1 + 3
y = 7 + 2

#print something
print("This again")
x = 3 + 2
y = 4 + 5


#So we use a dictionary to add a definition such as:
def function1():
  print("Words and Things")
  print("This again")

#to call it you just ask for the definition and that will execute the function
function1()

x = 3
#insert breakpoint
function1()
#when you call a function it transfers control to that function (or detours traffic to that definition) and then comes back to the loc in the file
#functions only run when called

#adding a tuple to go into the function as a value
def my_function(*kids)
  print("There are bunches of " +kids[3])
my_function("Sammy","Tommy","Linus")
