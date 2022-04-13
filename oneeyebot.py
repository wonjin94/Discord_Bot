# One Eye Bot v2.0


from dict_tree import dict_Dark_world_Tree
from dict_haven import dict_Haven
from dict_haven import dict_Haven_find  
from dict_haven_map_coord import dict_center_coord
import haven_ocr as demo
import hyper_stat as hp
import discord
import PIL
from PIL import Image
import numpy as np
from discord.ext import commands
from dict_haven import dict_Haven_screenshot
import io
import os
import map
from discord_components import Button, Select,SelectOption,ComponentsBot
#from discord import File

client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('Bot is ready')


# input : abbreviation of quest name
# returns true if such quest exists
def dict_hav_find(input):
    quest_pt1 = input[:3]
    quest_pt2 = input[3:]

    if quest_pt1 in dict_Haven_find:
        if quest_pt2 in dict_Haven_find[quest_pt1]:
            return True

    return False    

# function for testing tesseract paths
@client.command(pass_context=True)
async def tespath(ctx):
    curr_folder_path = os.path.abspath(os.getcwd())
    full_tesseract_path = os.path.join(curr_folder_path,'Tesseract-OCR/tesseract')
    await ctx.send(full_tesseract_path)
    await ctx.send(r'/app/Tesseract-OCR/tesseract.exe')



# command for heaven quests
# user inputs screen shot
# prints out quest difficulty + img with location for each quests
@client.command(pass_context=True)
async def havenss(ctx):
        

        output_string = ""

        # prepare png
        temp_map = map.prep_map()

        # read user's screenshot
        attachment = ctx.message.attachments[0]
        await attachment.save("dd.png")
       
        
        # open image
        screenshot_png = Image.open("dd.png")
        
        # perform ocr
        p1,p2 = demo.perform_ocr(screenshot_png)
        
        for i in range(4):
            # find quest's map location
            map = dict_Haven_screenshot[p1[i]][p2[i]]["map"]
            # find quest's difficulty
            difficulty = dict_Haven_screenshot[p1[i]][p2[i]]["difficulty"]
            # mark map location
            temp_map = map.mark_map(temp_map,map,dict_center_coord,[255,0,0,255])
            # update output string
            output_string = output_string +p1[i] + ": " + p2[i] + " : " +difficulty+ "\n"
            output_string = output_string + "--- Map : " + map + "\n"

        # print output string
        await ctx.send(output_string)
        

        # print marked map
        output_map = Image.fromarray(temp_map)
        output_map.save("output.png",format='PNG')
        await ctx.send(file = discord.File("output.png"))

# command for Heaven quests
# prints out quest difficulty
# !!!!! function is no longer in use, updated to havenmap !!!!
@client.command()
async def haven(ctx,*,args):

        # set up output string
        names = args.split(" ")
        output_string = ""

        # look up quest info for each quests
        for name in names:
            #if quest exists
            if dict_hav_find(name):
                # update output string
                output_string = output_string + dict_Haven[name]["new_name"] + " : " + dict_Haven[name]["difficulty"]+ "\n"
            # if quest doesn't exists
            else:
                # if quest is non-empty print error statement
                if name != '':
                    await ctx.send("{} is invalid name".format(name))

        # print out result
        await ctx.send(output_string)            


def haven_map_update_output_string(quest_name):
   
    #  output string is in following format:
    #
    #  quest_name : difficulty
    #   --- Map: map location
    
    
    output_string = dict_Haven[quest_name]["new_name"] + " : " + dict_Haven[quest_name]["difficulty"]+ "\n" + "--- Map : " + dict_Haven[quest_name]["map"] + "\n"

    return output_string

# command for Heaven quests with map info
# prints out quest difficulty + img with location for each quests
@client.command()
async def havenmap(ctx,*,args):

        # prepare png
        temp_map = map.prep_map
        

        output_string = ""
        names = args.split(" ")

        # look up quest info for each quests
        for name in names:
            # if user input exist 
            if dict_hav_find(name):
                # mark map on image
                temp_map = map.mark_map(temp_map,dict_Haven[name]["map"],dict_center_coord,[255,0,0,255])

                # update output_string
                output_string += haven_map_update_output_string(name)
                
            # if user input doesn't exist
            else:
                # if quest is non-empty print error statement
                if name != '':
                    await ctx.send("{} is invalid name".format(name))
        
        # print output string
        await ctx.send(output_string)

        # make PNG file of output map and print it
        output_map = Image.fromarray(temp_map)
        output_map.save("output.png",format='PNG')
        await ctx.send(file = discord.File("output.png"))

# command for Dark World Tree quests
@client.command()
async def tree(ctx,*,args):

        output = ""
        names = args.split(" ")

        for name in names:
            if name in dict_Dark_world_Tree:
                output = output + dict_Dark_world_Tree[name]["name"] + " : " + dict_Dark_world_Tree[name]["difficulty"]+ "\n"
            else:
                if name != '':
                    await ctx.send("{} is invalid name".format(name))
        await ctx.send(output)

# Command for hyperstat optimizer
@client.command()
async def hyperstat(ctx,*,args):
    
    best_hyp = hp.hyper_stat_mainfunc(args)
    
    output = """Best combination is:
    Main stat: {main_stat}
    Sub stat: {sub_stat}
    Crit dmg: {crit_dmg}
    Ied: {ied}
    Dmg: {dmg}
    Boss dmg: {boss_dmg}
    Attack power: {att}
    """.format(main_stat =best_hyp[0],sub_stat = best_hyp[1],crit_dmg = best_hyp[2],ied = best_hyp[3],dmg = best_hyp[4],boss_dmg = best_hyp[5],att = best_hyp[6] )

    
    await ctx.send(output)


def update_output_sttring(quest_name):
    
    output_string = ""



client.run('insert bot id here')