# Discord_Bot

Bot commands are called by using !command.<br/>
Some commands are no longer in use (outdated but still functional) or has been updated with more functionality.


up to date commands :<br/>

1. !havenss<br/>
    input - screenshot of the quest<br/>
    output - quest difficulties + quest location marked on a map<br/>
    
2. !havenmap -<br/>
    input - abbreviation of quests<br/>
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
   
   example screenshot from discord
   ![alt text](https://github.com/wonjin94/Discord_Bot/blob/main/haven_map_example.PNG)
   output - quest difficulties + quest location marked on a map


3. !hyperstat - 


out dated commands :

1. !haven - updated to havenmap
2. !tree - rarely used by users since quest difficulties can be determined easily
3. 