import json

from prettyprinter import pprint

with open("./train.json") as f:
    data = json.load(f)

# Assingning the different cuisines as keys
classes = {}
for x in data:
    if x["cuisine"] not in classes:
        classes[x["cuisine"]] = {}

# Get the frequency of all the ingredients for each cuisine
for x in data:
    ingredients = x["ingredients"]
    for i in ingredients:
        if classes.get(x["cuisine"]).get(i) == None:
            classes.get(x["cuisine"])[i] = 1
        else:
            classes.get(x["cuisine"])[i] += 1 
#pprint(classes)

# Get the top ten ingredients for each cuisine
first, second, third, fourth, fifth, sixth, seventh, eigth, ninth, tenth = (0,)*10
eleventh, twelfth, thirteenth, fourteenth = (0,)*4
first_name, second_name, third_name, fourth_name, fifth_name, sixth_name, seventh_name, eigth_name, ninth_name, tenth_name = ("",)*10
eleventh_name, twelfth_name, thirteenth_name, fourteenth_name = ("",)*4

rank_name = [first_name, second_name, third_name, fourth_name, fifth_name,
        sixth_name, seventh_name, eigth_name, ninth_name, tenth_name]
rank_freq = [first, second, third, fourth, fifth, sixth, seventh, eigth,
             ninth, tenth]
secondary_rank_freq = [eleventh, twelfth, thirteenth]
secondary_rank_name = [eleventh_name, twelfth_name, thirteenth_name]

def shuffleList(list_name, list_freq, index):
    i = len(list_freq) - 1
    while i > index:
        list_name[i] = list_name[i - 1]
        list_freq[i] = list_freq[i - 1]
        i -= 1

def top10(dictionary, classes, rank_name, rank_freq, repeats,
            secondary_dictionary, repeat_2, repeat_3, repeat_4_5):
    ''' Gets top 10 ingredients based on frequency '''
    ignore = repeats + repeat_2 + repeat_3 + repeat_4_5
    for x in classes:
        for i in classes[x]:
            # Top 10 ingredients for each cuisine
            if i not in ignore:
                for o in range(len(rank_name)):
                    if (classes[x][i] > rank_freq[o]):
                        shuffleList(rank_name, rank_freq, o)
                        rank_name[o] = i
                        rank_freq[o] = classes[x][i]
                        break 
            # Ingredients that repeat in more than 2 cuisines
            elif i in repeat_2:
                for y in range(len(secondary_rank_name)):
                    if classes[x][i] > secondary_rank_freq[y]:
                        shuffleList(secondary_rank_name, secondary_rank_freq, y)
                        secondary_rank_name[y] = i
                        secondary_rank_freq[y] = classes[x][i]
                        break
        # Top 10
        # Uncomment for [name, frequency]
        tmp_list = []
        for item in range(len(rank_name)):
            tmp_list.append([rank_name[item], rank_freq[item]])
            rank_name[item] = ""
            rank_freq[item] = 0
        # Lower 3
        secondary_tmp_list = []
        for j in range(len(secondary_rank_name)):
            secondary_tmp_list.append([secondary_rank_name[j], 
                                        secondary_rank_freq[j]])
            secondary_rank_name[j] = ""
            secondary_rank_freq[j] = 0
        dictionary[x] = tmp_list
        secondary_dictionary[x] = secondary_tmp_list
    return dictionary, secondary_dictionary

def findRepeats(repeats, main_list):
    ''' Finds the frequency of each ingredient among
        the other cuisines ''' 
    for x in main_list:
        for i in main_list[x]:
            if repeats.get(i[0]) == None:
                repeats[i[0]] = 1
            else:
                repeats[i[0]] += 1
    return repeats

def plus_n_repeats(main_list, repeats, thresh_lower, thresh_upper):
    ''' Adds ingredients that repeats more than thresh '''
    for x in repeats:
        if repeats[x] >= thresh_lower and repeats[x] <= thresh_upper:
            main_list.append(x)
    return main_list

def convertResult(main_list):
    converted = {}
    for x in main_list:
        tmp = []
        for i in main_list[x]:
            tmp.append(i[0])
        converted[x] = tmp
    return converted

# =========================================================================
# Main:
# =========================================================================
def main():
    result = {}
    secondary_result = {}
    repeats_list = ["salt", "water", "pepper"] # Repeats in more than 6 cuisines
    repeat_2 = []
    repeat_3 = []
    repeat_4_5 = []
    for times in range(7): # so far 4 is the optimal
        # Calculating new repeats
        repeats = {}
        repeats = findRepeats(repeats, result)
        # Adding the > 5 frequency to new repeats
        repeat_2 = plus_n_repeats(repeat_2, repeats, 2, 2)
        repeat_3 = plus_n_repeats(repeat_2, repeats, 3, 3)
        repeat_4_5 = plus_n_repeats(repeat_2, repeats, 4, 5)
        repeats_list = plus_n_repeats(repeats_list, repeats, 6, 20)
        # Getting top 10
        result, secondary_result = top10(result, classes, rank_name, rank_freq, 
                                          repeats_list, secondary_result, repeat_2,
                                            repeat_3, repeat_4_5)
    result = convertResult(result)
    secondary_result = convertResult(secondary_result)
    #pprint(result)
    #pprint(secondary_result)
    return result, secondary_result
