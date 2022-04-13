from PIL import Image
import numpy as np

# rgb code for each color
RGB_dict = {
    "red" : [255,0,0,255],
    "green" : [0,255,0,255] ,
    "blue" : [0,0,255,255],
    "pink" : [255,192,203,255],
}

# x y coordinates for points on and inside a circle
circle_coord = [(0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7),(8, 8),(8, 9) ,(9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7)]

# prepare clean png map to be marked
def prep_map():
    # read png file and save it as np array
    haven_map = Image.open('scrapyard cap.PNG')
    map_RGB_arr = np.asarray(haven_map)
    temp_map = map_RGB_arr.copy()

    return temp_map



def mark_map(map_png,map_name,map_dict,rgb):
    
    # if location has ben marked do nothing
    if map_dict[map_name][2]:
        return map_png

    # x y location of the map
    map_location = map_dict[map_name]

    # x y point to start the marking process
    x_start = map_location[1]-5
    y_start = map_location[0]-5

    new_map = map_png

    # mark each pixel location by chaning its color into rgb value
    for i in circle_coord:
        x = i[0] + x_start
        y = i[1] + y_start
        map_png[x][y] = rgb

    # update map location as marked
    map_dict[map_name][2] = 1

    # return marked map
    return new_map