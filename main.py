from PIL import Image
import pyperclip
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y)) #returns the rgb values of the pixel coordinate
    a = (r, g, b)
    return a

print("type the full path to the image you would like to use (Ex: C:\picture\example.jpg, __NO PNGS__):")
path = input()
img = Image.open(path, 'r')
print("please specify the size of the image you want to scale it to")
print("type width: ")
w = input()
print("type height: ")
h = input()
print("select the billboard type: ")
print("fixed,vertical,horizontal,center :")
billboard = input()
print("Do you want to be able to see it through blocks?")
print("type 1b for true and 0b for false: ")
seethrough = input()
image = img.resize((int(w), int(h)), Image.Resampling.LANCZOS)
pix = image.load()
image.show();
command = "{EntityTag:{id:\"minecraft:text_display\",line_width:32767,background:-16777216,billboard:" + billboard + ",see_through:" + seethrough + ",text:'["
i = 0
j = 0
ran = 0
isPng = 0 #checks if the image ends in png
if "png" in path:
    isPng = 1
while i < image.height:
    while j < image.width:
        if isPng == 1:
            r,g,b,a = pix[j,i]
            rgb = r,g,b
            hexval = rgb_to_hex(rgb)
        else:
            r,g,b = pix[j,i]
            rgb = r,g,b
            hexval = rgb_to_hex(rgb)

        squares = "█"
        while(1) :
            if(j==image.width-1) : #stops index out of range exceptions
                break;
            if isPng == 1:
                r,g,b,a = pix[j,i]
                r1,g1,b1,a1 = pix[j+1,i]
                rgb = r,g,b
                rgb2 = r1,g1,b1
            else:
                r,g,b = pix[j,i]
                r1,g1,b1 = pix[j+1,i]
                rgb = r,g,b
                rgb2 = r1,g1,b1
            if(rgb_to_hex(rgb) == rgb_to_hex(rgb2)):
                j+=1
                squares += "█" #if the pixel next to it is the same color it doesnt create a new text parameter and instead adds another square
            else:
                break
        if(j==image.width-1):
            squares+= r"\\n"
        command += ("{\"text\":\"" + squares + "\",\"color\":\"#" + hexval + "\"") #adds the text with the hex value
        if ran == 0:
            command += ",\"italic\":false" # sets the first text on the line to not italic
        ran = 1
        command += "}"
        if j != image.width-1:
            command += ","

        j+=1

    if i != image.height-1: 
        command += ","

    i+=1
    j=0
    ran = 0
command += "]\'}}"
pyperclip.copy(command)
print("/give @p ghast_spawn_egg" + command)
print("nbt data copied to clipboard")
