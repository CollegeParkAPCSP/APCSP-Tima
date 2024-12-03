def names(names:list):
    print(f"{names[0]} {names[2]} {names[4]}")

def num_names(names:list, nums:list):
    for i in range(len(names)):
        for j in range(len(nums)):
            print(f"{nums[j]}, {names[i]}")
            
def even_nums(nums:list):
    for i in range(len(nums)):
        print(f"{nums[i]}") if nums[i] % 2 == 0 else None
        
names(["John", "Doe", "Jane", "Smith", "Tom"])
num_names(["John", "Doe", "Jane"], [1,2,3])
even_nums([0,1,2,3,4,5,6,7,8,9])