
from PIL import Image  
import json


with open('./src.json' , 'rb') as f : 
    data = json.load(f)



def filter (file_name ,saved_file) : 


    im = Image.open(file_name)
    impixel = im.load()
    new = Image.new('RGB' , (im.size[0],im.size[1]) ,0)
    pixels = new.load()
    for i in range(im.size[0]) : 
        for j in range(im.size[1]) : 
            pixels[i,j] = impixel[i,j]
    new.save(saved_file)


def resizing(size) : 
    im = Image.open('./test.jpg')
    impixel = im.load()
    new = Image.new('RGB' , (im.size[0],im.size[1]) ,0)
    pixels = new.load()
    print(im.size)
    for i in range(im.size[0]) : 
        for j in range(im.size[1]) : 
            pixels[i,j] = impixel[i,j]
    new = new.resize((size[0] , size[1]))
    new.save('dog.png')



if __name__ == "__main__":
    for image in data :
       filter(image['original_file'] , image['new_file'])
    #resizing([400,400])