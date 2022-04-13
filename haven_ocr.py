import pytesseract
import os
from PIL import Image
from dict_haven import dict_Haven_screenshot

# returns full path of tesseract exe file
# func only works on local pc machine with tesseract files
def get_tess_exe_path():
    curr_folder_path = os.path.abspath(os.getcwd())
    full_tesseract_path = os.path.join(curr_folder_path,r'Tesseract-OCR\tesseract')
    return full_tesseract_path



# check if input image is correct size and return its size
def image_size_checker(img):
    if img.size == (1920,1200):
        return (1920,1200)
    elif img.size == (1920,1080):
        return (1920,1080)
    elif img.size == (1366,768):
        return (1366,768)
    else:
        return (0,0)

# crop image according to given size
def crop_image(img,size):
    img_02 = crop_image_02(img,size)
    img_34 = crop_image_34(img,size)
    
    return img_02,img_34

# crop image according to given size
# use this function if there are 0~2 quests that takes up 2 lines each
def crop_image_02(img,size):
    
    xmin_1920 = 858
    xmax_1920 = 1190
    xmin_1366 = 580
    xmax_1366 = 910

    ymin_1200 = 515
    ymin_1080 = 454
    ymin_1366 = 299

    ymax_1200 = 620
    ymax_1080 = 558
    ymax_1366 = 402

    if size == (1920,1200):
        cropped_img = img.crop((xmin_1920,ymin_1200,xmax_1920,ymax_1200))
    elif size == (1920,1080):
        cropped_img = img.crop((xmin_1920,ymin_1080,xmax_1920,ymax_1080))
    else:
        cropped_img = img.crop((xmin_1366,ymin_1366,xmax_1366,ymax_1366))
    
    # enlarge the image
    return cropped_img.resize((1000,400), Image.LANCZOS)

# crop image according to given size
# use this function if there are 3~4 quests that takes up 2 lines each
def crop_image_34(img,size):
    xmin_1920 = 858
    xmax_1920 = 1190
    xmin_1366 = 580
    xmax_1366 = 910

    ymin_1200 = 490
    ymin_1080 = 430
    ymin_1366 = 274

    ymax_1200 = 640
    ymax_1080 = 585
    ymax_1366 = 428

    if size == (1920,1200):
        cropped_img = img.crop((xmin_1920,ymin_1200,xmax_1920,ymax_1200))
    elif size == (1920,1080):
        cropped_img = img.crop((xmin_1920,ymin_1080,xmax_1920,ymax_1080))
    else:
        cropped_img = img.crop((xmin_1366,ymin_1366,xmax_1366,ymax_1366))
    
    return cropped_img.resize((1000,400), Image.LANCZOS)


# remove unnessary characters from the string ("\n"))
# this func might be needed to be fixed for effiency, but it works fine
def clean_text(input):
    count = 0
    output = []
    for text in input:
        if text.find("\n\n") != -1:
            count += 1
        output_temp = ""
        temp = text.split("\n\n")
        for i in temp:
            if i != "":
                output_temp = i
        temp = output_temp.split("\n")
        if len(temp) != 1:
            if temp[0] != "":
                output_temp = temp[0]
                if temp[1] != "":
                    output_temp = output_temp + " " + temp[1]
                output.append(output_temp)
        else:
            output.append(temp[0])
    final_output = []
    for i in output:
        if i != "":
            final_output.append(i)
    return final_output

# separate the quest name into two parts  (quest location / quest name)
# input - string 
# format - quest_location: quest_name
def classify_quest(input):
    part1 = []
    part2 = []
    for text in input:
        temp = text.split(": ")
        part1.append(temp[0])
        part2.append(temp[1])
    return part1,part2

def perform_ocr (image) :
    img_size = image_size_checker(image)
    crop_image1,crop_image2 = crop_image(image,img_size)
    
    #imgplot = plt.imshow(crop_image1)
    #plt.show()
    #imgplot = plt.imshow(crop_image2)
    #plt.show()
    

    con = r'--oem 2'

    # get tesseract folder path
    pytesseract.pytesseract.tesseract_cmd = get_tess_exe_path()

    # perform ocr
    text = pytesseract.image_to_string(crop_image1,lang ="eng" ,config=con)

    if text.find("[Weekly Quest]") != 0:
        text = pytesseract.image_to_string(crop_image2,lang ="eng" ,config=con)
    
    # remove unwanted text
    parsed_text = text.split("[Weekly Quest] ")

    # clean next - remove, extra new line
    clean_parsed_text = clean_text(parsed_text)
 
    # separate quest location and quest name from text
    p1,p2 = classify_quest(clean_parsed_text)

    return p1,p2

