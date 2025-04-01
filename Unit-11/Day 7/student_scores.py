student_scores = open("school_scores.txt")

# Creates the tables from the txt data
table = []
for line in student_scores:
    table.append(line.split(","))

max_row_count = int(table[0][0])
max_col_count = int(table[0][1].strip("\n"))

row_max_2005 = 53
scores_by_state = []
temp = ""

for row in range(2, row_max_2005):
    state = table[row][2] # state is at the current row and always column 2
    math_score = table[row][3] # math score is at the current row and always column 3
    verbal_score = table[row][5] # verbal score is at the current row and always column 5
    temp = f"State: {state}\nMath: {math_score} || Verbal: {verbal_score}"
    scores_by_state.append(temp)
    temp = ""

def getGPA():
    for row in range(2, row_max_2005):
        print(f"{table[row][2]}: {table[row][17]} GPA")

getGPA()

# the getGPA() function gets the average GPA for each
# state in the year 2005 and prints it out.