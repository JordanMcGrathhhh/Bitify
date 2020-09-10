from PIL import Image, ImageDraw
import argparse
import sys

def checkRes(x, y):
    if ((im_y % 10 != 0) and (im_x % 10 != 0)):

        res_y = list(str(im_y))
        new_res_y = im_y - int(res_y[(len(res_y) - 1)])
        res_x = list(str(im_x))
        new_res_x = im_x - int(res_x[(len(res_x) - 1)])

        crop = image.crop((0, 0, new_res_x, new_res_y))
        crop.save("Cropped_" + args.path)
        print("[*] Saved New Image [*]")
        print("[*] Please Proceed On the New Image! [*]")
        return False

    elif (im_y % 10 != 0):
        res_y = list(str(im_y))
        new_res = im_y - int(res_y[(len(res_y) - 1)])
        print("[*] Image y-value cropped to " + str(new_res))

        crop = image.crop((0, 0, im_x, new_res))
        crop.save("Cropped_" + args.path)
        print("[*] Saved New Image [*]")
        print("[*] Please Proceed On the New Image! [*]")
        return False

    elif (im_x % 10 != 0):
        res_x = list(str(im_x))
        new_res = im_x - int(res_x[(len(res_x) - 1)])
        print("[*] Image y-value cropped to " + str(new_res))

        crop = image.crop((0, 0, new_res, im_y))
        crop.save("Cropped_" + args.path)
        print("[*] Saved New Image [*]")
        print("[*] Please Proceed On the New Image! [*]")
        return False

    else:

        return True

parser = argparse.ArgumentParser()

#Arguments
parser.add_argument("--path",
                    "-p",
                    help = "Path to the desired image")
parser.add_argument("--export",
                    "-e",
                    help = "File name to save the image to")
parser.add_argument("--grid_size",
                     "-gS",
                     help = "Desired size of grid 'put' on image\nDefault size is 10x10")

#Parse Arguments
args = parser.parse_args()

if( Image.open(args.path) ):
    print("[*] Image Successfully Found and Opened [*]")
else:
    sys.exit()

with Image.open(args.path) as image:

    im_x, im_y = image.size
    print("Image Length: " + str(im_x) + "\nImage Height: " + str(im_y))

    #Prep the Image, ensure both y and x value of image res are multiples of 10
    if((im_x % 10 == 0) and (im_y % 10 == 0)):
        print("[*] Origin Resolution - OKAY [*]")
    else:
        print("[*] Origin Resolution - BAD [*]")

    if( checkRes(im_x, im_y)):
        pass
    else:
        sys.exit()


    #Default Grid Size is 10x10, incrementing by "grid_size" will create your grid :)
    grid_size = int(args.grid_size)
    x1, y1 = grid_size, grid_size
    x2, y2 = 0, 0

    while True:

        color = image.load()

        color_box = ((x1 - (grid_size / 10)), (y1 - (grid_size / 10)))
        section = (x1, y1, x2, y2)

        draw = ImageDraw.Draw(image)
        try:
            draw.rectangle(section, fill=(color[color_box]), outline=(color[color_box]))
        except:
            pass

        x1 = x1 + grid_size
        x2 = x2 + grid_size

        if(x1 > im_x):
            x1 = grid_size
            x2 = 0
            y1 = y1 + grid_size
            y2 = y2 + grid_size
        elif(y1 > im_y):
            break

    image.save(args.export)



