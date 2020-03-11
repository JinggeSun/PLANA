

# 净胜球
def win_goal_alg(goal,lose):
    return goal - lose	
# 场均进球
def avg_goal_agl(goal,scene):
    return round(goal/scene,2)	
# 场均失球
def avg_fumble_agl(fumble,scene):
    return round(fumble/scene,2)	
# 场均净胜	
def avg_total_alg(avg_goal,avg_fumble):
    return round(avg_goal - avg_fumble,2)
# 场均积分	
def avg_integral_alg(integral,scene):
    return round(integral/scene,2)
# 积分
def integral_alg(win,flat,lose):
    return win * 3 + flat * 1 + lose * 0
# 排名
# 1. 按照积分从高到底
# 2. 积分相同的，净胜球
# 3. 净胜球相同 进球数
def rank_alg(list):
    result_list = sorted(list, key=lambda x: x['integral'],reverse=True)
    for index,result in enumerate(result_list):
        result['rank'] = index + 1
    return result_list

if __name__ == "__main__":
   list = [{'integral':1},{'integral':3}]
   print(rank_alg(list))