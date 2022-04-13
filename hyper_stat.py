
# each number corresponds to a stat, some stats have min value for faster calculation
# 0,1 ab_stat = 30
# 2 c_crit_d = 1
# 3 d_ied = 3
# 4 e_dmg = 3
# 5 boss dmg
# 6 att pow

# formulas for calculating values for maplestory
# https://strategywiki.org/wiki/MapleStory/Formulas


# main function for calculating best hyper stat
def hyper_stat_mainfunc(user_input):

     # inputs
     # 0 main stat
     # 1 sub stat
     # 2 crit dmg
     # 3 ied
     # 4 dmg
     # 5 boss dmg
     # 6 attack percent
     # 7 range
     # 8 weapon type
     # 9 final dmg
     # 10 available points

     # convert user input into float
     curr_stat_int = []
     names = user_input.split(" ")
     for name in names:
        curr_stat_int.append(float(name))
     
     # calculate attack_power
     attack_power = cal_attack_power(curr_stat_int)
     
     # replace attack % with attack_power, attack % is no longer needed
     curr_stat_int[6] = attack_power
     
     # calculate best option
     best_hyp = cal_dmg(curr_stat_int[10],curr_stat_int)

     return best_hyp

# input - curr_stats (array of stats)
# output - calculated attack power
def cal_attack_power(curr_stats):

     # dmg https://www.inven.co.kr/board/maple/2299/2052468
    dmg_multiplier=(curr_stats[4]+100)/100
    percent_att_multiplier = (100 + curr_stats[6])/100
    stats_multiplier = (curr_stats[0] * 4 + curr_stats[1])/100
    final_dmg_multiplier = (curr_stats[9]+100)/100
    attack_power= curr_stats[7] / (dmg_multiplier * percent_att_multiplier * stats_multiplier * curr_stats[8] *final_dmg_multiplier)

    return attack_power

# input - possible hyper stat combination, user input stats
# output - total multiplier (result)
def cal_dmg_multiplier(hyp_stat_list,curr_stats):
     # stats multiplier
     new_main_stat = hyp_stat_list[0]+curr_stats[0]
     new_sub_stat = hyp_stat_list[1]+curr_stats[1]
     stat_multiplier = (new_main_stat*4 + new_sub_stat)

     # crit dmg multiplier
     new_crit_dmg = hyp_stat_list[2] + curr_stats[2]
     crit_dmg_multiplier = (1+(135+new_crit_dmg)/100)

     # ied multiplier
     new_ied = (1-(100-curr_stats[3])/100*(100-hyp_stat_list[3])/100)
     ied_multiplier = 100-(300-300*new_ied)

     # dmg + boss dmg multiplier
     new_boss_dmg = curr_stats[4] + hyp_stat_list[4]
     new_dmg = curr_stats[5] + hyp_stat_list[5]
     dmg_multiplier = (100 + new_boss_dmg + new_dmg)/100

     # attack power multiplier
     att_multiplier = curr_stats[6] + hyp_stat_list[6]

     return stat_multiplier * crit_dmg_multiplier * ied_multiplier * dmg_multiplier * att_multiplier


def cal_dmg (av_pt,current_stat) :

     # required points for each level
     req_pt = [1,3,7,15,25,40,60,85,115,150,200,265,345,440,550]

     # boss damage have different value per level than other stats
     bd = [3,6,9,12,15,19,23,27,31,35,39,43,47,51,55]


     # following calculation is a brute forced method
     # i have no future plans to optimize this because the function will be rarely used
     total_point_used = 0
     total_point_temp = [0,0,0,0,0,0,0]
     stat_temp = [0,0,0,0,0,0,0]
     best_multiplier = 0
     best_hyp = [-1,-1,-1,-1,-1,-1,-1]
     for a in range(8):
          # Cal main stat
          stat_temp[0] = 30+a*30
          total_point_temp[0] = req_pt[a]
          for b in range(8):
               # Cal sub stat
               stat_temp[1] = 30+b*30
               total_point_temp[1] = req_pt[b]
               for c in range(15):
                    # Cal crit damage
                    stat_temp[2] = 1+c
                    total_point_temp[2] = req_pt[c]
                    for d in range(12):
                         # Cal ied
                         stat_temp[3] = 3+d*3
                         total_point_temp[3] = req_pt[d]
                         for e in range(15):
                              # Cal dmg
                              stat_temp[4] = 3+e*3
                              total_point_temp[4] = req_pt[e]
                              for f in range(15):
                                   # Cal boss dmg
                                   stat_temp[5] = bd[f]
                                   total_point_temp[5] = req_pt[f]
                                   for g in range(8):
                                        # Cal att power
                                        stat_temp[6] = 3+g*3
                                        total_point_temp[6] = req_pt[g]
                                        total_point_used = sum(total_point_temp)
                                        
                                        
                                        if total_point_used <= av_pt:
                                             multiplier = cal_dmg_multiplier(stat_temp,current_stat)
                                             if multiplier > best_multiplier:
                                                  best_multiplier = multiplier
                                                  best_hyp[0] = a + 1
                                                  best_hyp[1] = b + 1
                                                  best_hyp[2] = c+ 1
                                                  best_hyp[3] = d+ 1
                                                  best_hyp[4] = e+ 1
                                                  best_hyp[5] = f+ 1
                                                  best_hyp[6] = g+ 1

     return best_hyp                               