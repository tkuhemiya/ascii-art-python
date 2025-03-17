from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import os, sys
importedImage = ""
CHARS = [" ","`", "^", "\\", "\"", ",", ":", ";", "I", "l", "!", "i", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "\\", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"]

def asciiConvert(image):        

    global CHARS
    # Folder = input("Enter file directory: ")
    
    img = Image.open(image)

    width, height = img.size
    
    pixArray = list(img.getdata())

    pixel_matrix = []
    addarr = 0

    for i in range(height):
        temparr = []
        for j in range(width):
            temparr.append(pixArray[i+j+addarr])
        if(i == width-1):
            pass
        else:
            addarr +=width-1
            
        pixel_matrix.append(temparr)
    
    f = open("art.txt", "w")
         
    for x in range(height):
        #print()
        f.write("\n")
        for y in range(width):
            pixel = pixel_matrix[x][y]
            brightness = (((pixel[0]+pixel[1]+pixel[2])/3)*(len(CHARS)-1)/255)
            lightness = (max(pixel[0], pixel[1], pixel[2]) + min(pixel[0], pixel[1], pixel[2])) / 2
            luminosity = (21*pixel[0]+72*pixel[1]+7*pixel[2])/100
            index = int(((brightness + lightness + luminosity)/3)*(len(CHARS)/255))
            #print(CHARS[index]*2,end="")
            f.write(CHARS[index])

def openFile():
    global importedImage
    filepath = filedialog.askopenfilename(initialdir="C:\\")
    importedImage = filepath

def createWindow():
    
    window = Tk()
    window.title('ASCII Converter')
    window.geometry("215x100")
    frame = ttk.Frame(window, padding=10)
    frame.grid()
    ttk.Label(frame, text="ASCII Converter").grid(column=0, row=0)

    ttk.Button(frame, width=30, text="Open image", command=openFile).grid(column=0, row=1)
    ttk.Button(frame, width=30,text="Convert", command=lambda: asciiConvert(importedImage)).grid(column=0, row=2)
    window.mainloop()
    
createWindow()
    


