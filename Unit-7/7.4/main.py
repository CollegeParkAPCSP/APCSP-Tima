def add_item(item:str, curr_list:list, amount:int) -> None:
    for i in range(amount):
        curr_list.append(item)

def remove_item(item:str, curr_list:list, amount:int) -> None:
    try:
        for i in range(amount):
            curr_list.remove(item)
    except:
        print("Item not found in the list")