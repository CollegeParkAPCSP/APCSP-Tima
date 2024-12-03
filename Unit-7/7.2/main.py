def add_item(item, curr_list):
    curr_list.append(item)
    
def insert_item(item, index, curr_list):
    curr_list.insert(index, item)

def clear_list():
    return []

def view_list(curr_list):
    for i in range(len(curr_list)):
        print(f"{i+1}. {curr_list[i]}")
        
kroger_list: list = []
heb_list: list = []
walmart_list: list = []

end = False

while not end:
    print("Which list would you like to modify?")
    s = input()
    if s != "kroger" and s != "heb" and s != "walmart":
        print("Invalid list name")
        continue
    else:
        print("What would you like to do?")
        print("1. Add item")
        print("2. Insert item")
        print("3. Clear list")
        print("4. View list")
        x = int(input())
        
        match x:
            case 1:
                print("What item would you like to add?")
                item = input()
                match s:
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
                match s:
                    case "kroger":
                        insert_item(item, index, kroger_list)
                    case "heb":
                        insert_item(item, index, heb_list)
                    case "walmart":
                        insert_item(item, index, walmart_list)
            case 3:
                match s:
                    case "kroger":
                        kroger_list = clear_list()
                    case "heb":
                        heb_list = clear_list()
                    case "walmart":
                        walmart_list = clear_list()
            case 4:
                print("Here is your list:")
                match s:
                    case "kroger":
                        view_list(kroger_list)
                    case "heb":
                        view_list(heb_list)
                    case "walmart":
                        view_list(walmart_list)
    print("Would you like to continue?")
    a = input()
    end = True if a == "no" else False