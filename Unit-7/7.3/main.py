def remove_item(item:str, curr_list:list):
    try:
        curr_list.remove(item)
    except:
        print("Item not found in the list")

def remove_pos(index:int, curr_list:list):
    try:
        curr_list.remove(curr_list[index])
    except:
        print("Index out of range")

def sort_list(curr_list:list, which_way:bool):
    if which_way:
        curr_list.sort()
    else:
        curr_list.sort(reverse=True)