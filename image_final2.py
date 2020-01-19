import cv2          # for handling color related functions
import numpy as np  # for handling array
import webcolors    # functions to extract color from rgb value

print("\nProgram to find a particular pixel RGB value/colour name in a given image file..\n")

print("Keep the image file in the current working directory..")
file1 = input ("\nEnter image file name (ex. sky.jpg)...")
image = cv2.imread(file1)

print("\nPlease Enter the X & Y co-ornidate of the image where you need the colour value..")
x = int (input("\nEnter X coordinate..:"))
y = int (input("\nEnter Y coordinate..:"))

pixel = image[x,y]  # to get RGB value
print ("\n\nThe given image file ",file1,"co-ordinates from X =",x," Y=",y,"\nRGB value is..",pixel)

# to find the color name using RGB value thru library webcolors

try:
    closest_name = actual_name = webcolors.rgb_to_name(pixel)
except ValueError:
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - pixel[0]) ** 2
        gd = (g_c - pixel[1]) ** 2
        bd = (b_c - pixel[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    print("Colour Name ...:", min_colours[min(min_colours.keys())])

center = (x,y)
color1 = (255,255,255)
image1 = cv2.circle(image, center, 5, color1, 2) 
# Displaying the image
window_name = 'image'
cv2.imshow(window_name, image1) 
