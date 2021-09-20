# These are the variables we will be using for the program.
# The X variable represents the X axis.
# The Y variable represents the Y axis.
# The blockName variable is the name of the block entered by the user.
# The blockID variable will be assigned to every block created.
# The blockLocation variable will use an array that will contain two variables (x and y).
# limitX is the limit for how far X can be from the origin.
# limitY is the limit for how long Y can be.
# blockLimit is the variable that contains the limitX and limitY variable and
# creates the boundaries in coordinates.
x = 0
y = 0
blockName = ""
blockID = 0
blockLocation = [x, y]
limitX = 32
limitY = 32
blockLimit = [limitX, limitY]


# This is the main menu function, its a function as it will be used to be called back to later
# when the user wants to go back to the main menu
def Menu():
    print("Welcome to the block creator")
    print("This python script explores coordinates in python and "
        "how it can be used for my future programs")
    print("This is a command line demonstration")
    print("1. Create a block on a 2D canvas")
    print("2. Create a block on a 3D canvas (not available yet)")
    userInput = input("Enter a number listed from the menu: ")


def createCanvas():
    global sizeOfCanvas, distanceX, distanceY
    sizeOfCanvas = blockLimit
    distanceX = blockLimit[0]
    distanceY = blockLimit[1]



def blockCreator():
    print("The size of this canvas: ", sizeOfCanvas)
    print("The length of the X axis: ", distanceX)
    print("The width of the Y axis: ", distanceY)
    userX = input("Enter the location the block is gonna be on the X axis: ")
    userY = input("Enter the location the block is gonna be on the Y axis: ")
    x = userX
    y = userY
    blockLocation = [x, y]
    if int(userX) > distanceX or int(userY) > distanceY:
        print("The block can't be outside the canvas.")
    else:
        print("The location of this block on this canvas: ", blockLocation[0],",", blockLocation[1])

createCanvas()
blockCreator()



