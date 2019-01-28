from PIL import Image
import math

# The filename of the picture being used
FILENAME = "balloon.jpg"

# The number of people in the space
# the program is being displayed
PEOPLE = 100

# The percentage of people that are likely
# to actively participate in the program
ACTIVITY = .5

image = Image.open(FILENAME)

IMG_WIDTH = image.size[0]
IMG_HEIGHT = image.size[1]

# ratio of width/height. If rows/columns equals
# this ratio then the snippets with be square
ratio = IMG_WIDTH/IMG_HEIGHT
print(ratio)

# Sets rows and columns so that the number of
# snippets generated equals people * activity
# and so that rows/columns equals ratio
ROWS = math.ceil(math.sqrt(ratio * PEOPLE * ACTIVITY))
COLUMNS = math.ceil(math.sqrt(PEOPLE * ACTIVITY/ratio))

# Rounds off the image so that the pictures are even
IMG_WIDTH = IMG_WIDTH - (IMG_WIDTH % ROWS)
IMG_HEIGHT = IMG_HEIGHT - (IMG_HEIGHT % COLUMNS)

# divides the picture
def dividePicture():
    for x in range(ROWS):
        for y in range(COLUMNS):
            write(crop(image, x, y),
                  "snippet_(" + str(x) + "," + str(y) + ")")

# crops a snippet based on the coordinates
def crop(image, x, y):
    x1 = IMG_WIDTH * x/ROWS
    y1 = IMG_HEIGHT * y/COLUMNS
    x2 = IMG_WIDTH * (x + 1)/ROWS
    y2 = IMG_HEIGHT * (y + 1)/COLUMNS

    return image.crop((x1, y1, x2, y2))

# writes the picture to file
def write(file, name):
    file.save(name + ".jpg")