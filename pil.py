from PIL import Image, ImageDraw, ImageFont
import csv
from csv import reader
import os 

i = 0

image_folder = 'image'

final_folder = 'id_cards'
with open("data.csv", "r") as f:
    
    csv_reader = reader(f)
    reader = csv.reader(f, delimiter="\t")
    
    for row in csv_reader:
        
        name = row[0]
        # source template 
        img1 = Image.open(r'Template.png')

        ssn = row[1]

        Occupation = row[2]

        Birthday = row[3]
        # The angle at which the cropped Image must be rotated
        angle = 0
        img_name = row[4]
        try:
            img = Image.open(f'{image_folder}\{img_name}')
        except:
            continue
        # resizing the image 
        img = img.resize((659,659),resample = 0)

        # pasting the resized image over the original image, guided by the transparency mask of resized image
        img1.paste(img, (30,550))
        
        # writing text 
        d1 = ImageDraw.Draw(img1)
        myFont = ImageFont.truetype(r'fonts\OpenSans-ExtraBold.ttf', 120)
        #  NAME 
        d1.text((725, 575), f'{name}','black', font=myFont)
        font2 = ImageFont.truetype(r'fonts\OpenSans-Regular.ttf', 70)
        # SOCIAL SECURITY NUMBER 
        d1.text((725,725),f'{ssn}','black',font = font2)
        # OCCUPATION
        d1.text((725,800),f'{Occupation}','black',font = font2)

        d1.text((725,1100),f'BIRTHDAY {Birthday}','black',font = font2)
        # converting the final image into its original color mode, and then saving it
        img_name = img_name.split('.')[0]
        img1.save(fr"{final_folder}\{img_name}.png")
        i = i+1
        
    #print(i)
    