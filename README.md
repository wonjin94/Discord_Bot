# Discord_Bot

Bot commands are called by using !command.<br/>
Some commands are no longer in use (outdated but still functional) or has been updated with more functionality.


up to date commands :<br/>

1. !havenss<br/>
    input - screenshot of the quest<br/>
    output - quest difficulties + quest location marked on a map<br/>
    
    example screenshot from discord<br/>
    ![alt text](https://github.com/wonjin94/Discord_Bot/blob/main/example_screenshots/havenss_example.PNG)<br/>
    
    In order to use python tesseract, download all files in https://github.com/tesseract-ocr/tesseract to the same folder as the rest of the code.
    
    
2. !havenmap -<br/>
    input - abbreviation of quests<br/>
    output - quest difficulties + quest location marked on a map<br/>
        format : !havenmap quest1 quest2... (the number of quest names does not matter)
            
            quest abbreviation has 2 parts
              part 1 index:
                Haven - hav
                Scarpyard - scr
                skyline - sky
                Black Haven Deck - bhd
                Black Haven Inside - bhi
              
              part 2 :
                first letter of the each word after ":" (this includes the word "the")
                !!!! for the word steel and scrap, you must include the first two letters (st for steel and sc for scrap)

        example quest name : Black Haven Inside: Collect Scrap ID Plate
        !haven bhicscip  quest2 ....
   
   example screenshot from discord<br/>
   ![alt text](https://github.com/wonjin94/Discord_Bot/blob/main/example_screenshots/haven_map_example.PNG)<br/>
  


3. !hyperstat - <br/>
    I made this function for a personal use, but it is still available for anyone.<br/>
    It computes the best combination for hyper stat (max dmg)
    
    format - !hyperstat main_stat sub_stat crit_dmg ied dmg boss_dmg att% stat_window_value weap_value stat_point_avail
    
    ![alt text](https://github.com/wonjin94/Discord_Bot/blob/main/example_screenshots/hyperstat_example.PNG)<br/>
    


out dated commands :

1. !haven - updated to havenmap
2. !tree - rarely used by users since quest difficulties can be determined easily
