def add_item(item:str, curr_list:list) -> None:
    curr_list.append(item)
    
def insert_item(item:str, index:int, curr_list:list) -> None:
    curr_list.insert(index, item)

def clear_list() -> list:
    return []

def view_list(curr_list:list) -> None:
    for i in range(len(curr_list)):
        print(f"{i+1}. {curr_list[i]}")
        
def remove_item(item:str, curr_list:list) -> None:
    try:
        curr_list.remove(item)
    except:
        print("Item not found in the list")

def remove_pos(index:int, curr_list:list) -> None:
    try:
        curr_list.remove(curr_list[index])
    except:
        print("Index out of range")

def sort_list(curr_list:list, which_way:bool) -> None:
    if which_way:
        curr_list.sort()
    else:
        curr_list.sort(reverse=True)
        
kroger_list: list = []
heb_list: list = []
walmart_list: list = []

end = False

while not end:
    print("Which list would you like to modify?")
    l = input()
    if l != "kroger" and l != "heb" and l != "walmart":
        print("Invalid list name")
        continue
    else:
        print("What would you like to do?")
        print("1. Add item")
        print("2. Insert item")
        print("3. Clear list")
        print("4. View list")
        print("5. Remove item")
        print("6. Remove item at position")
        print("7. Sort list")
        x = int(input())
        
        match x:
            case 1:
                print("What item would you like to add?")
                item = input()
                match l:
                    case "kroger":
                        add_item(item, kroger_list)
                    case "heb":
                        add_item(item, heb_list)
                    case "walmart":
                        add_item(item, walmart_list)
            case 2:
                print("What item would you like to insert?")
                item = input()
                print("What index would you like to insert at?")
                index = int(input())
                match l:
                    case "kroger":
                        insert_item(item, index, kroger_list)
                    case "heb":
                        insert_item(item, index, heb_list)
                    case "walmart":
                        insert_item(item, index, walmart_list)
            case 3:
                match l:
                    case "kroger":
                        kroger_list = clear_list()
                    case "heb":
                        heb_list = clear_list()
                    case "walmart":
                        walmart_list = clear_list()
            case 4:
                print("Here is your list:")
                match l:
                    case "kroger":
                        view_list(kroger_list)
                    case "heb":
                        view_list(heb_list)
                    case "walmart":
                        view_list(walmart_list)     
            case 5:
                print("What item would you like to remove?")
                item = input()
                match l:
                    case "kroger":
                        remove_item(item, kroger_list)
                    case "heb":
                        remove_item(item, heb_list)
                    case "walmart":
                        remove_item(item, walmart_list)
            case 6:
                print("At what index would you like to remove?")
                index = int(input())
                match l:
                    case "kroger":
                        remove_pos(index, kroger_list)
                    case "heb":
                        remove_pos(index, heb_list)
                    case "walmart":
                        remove_pos(index, walmart_list)
                        
            case 7:
                print("How would you like to sort the list?")
                print("1. Ascending")
                print("2. Descending")
                way = int(input())
                b = False if way == 1 else True
                match l:
                    case "kroger":
                        sort_list(kroger_list, b)
                    case "heb":
                        sort_list(heb_list, b)
                    case "walmart":
                        sort_list(walmart_list, b)
                
    print("Would you like to continue?")
    a = input()
    end = True if a == "no" else False