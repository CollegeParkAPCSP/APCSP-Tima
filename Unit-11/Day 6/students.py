f = []
s = []
j = []
se = []

# Read the file
with open("students.dat", "r") as file:
    for line in file:
        temp = line.strip().split(",")  # Split the data by comma
        name, grade = temp[0], temp[1]  # Extract name and grade

        # Categorize by grade level
        if grade == "9":
            f.append(name)
        elif grade == "10":
            s.append(name)
        elif grade == "11":
            j.append(name)
        elif grade == "12":
            se.append(name)

# Insert the count at the beginning of each list
f.insert(0, len(f))
s.insert(0, len(s))
j.insert(0, len(j))
se.insert(0, len(se))

# Display results
print(f"{len(f)} Freshmen: {f[1:]}")
print(f"{len(s)} Sophomores: {s[1:]}")
print(f"{len(j)} Juniors: {j[1:]}")
print(f"{len(se)} Seniors: {se[1:]}")