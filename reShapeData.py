import PIL
import os, sys
from PIL import Image
def imagepad():
    size = 28, 28
    root='.'
    filename= os.path.join( root, 'BanglaLekha-Isolated') 
    data_folders = [os.path.join(filename, d)for d in sorted(os.listdir(filename))
                    if os.path.isdir(os.path.join(filename, d))]
    print(filename)
    for folder in data_folders:
        print(folder)
        image_files=os.listdir(folder)
        for image in image_files:
            infile=os.path.join(folder,image)
            print (infile)
            #infile="shoro1.png"
            #for infile in sys.argv[1:]:
            outfile = os.path.splitext(infile)[0]
            try:
                im = Image.open(infile)
                im.thumbnail(size, Image.ANTIALIAS)
                #im.save("beforePaddign1.png")
                background= Image.new('1',size) #convert the image into 1 (1-bit pixels, black and white, stored with one pixel per byte)
                background.paste(im, (int((size[0]-im.size[0])/2), int((size[1]-im.size[1])/2)))
                background.save(infile)



            except IOError:
                print (infile)
                #return background
imagepad()
