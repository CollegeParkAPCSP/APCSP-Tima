def calculate(dailies: list, majors:list, finalw:float = None, dailyWeight = .2, majorWeight = .6, finalWeight = .2):
    avgDailies = 0
    avgMajors = 0
    
    for i in dailies:
        avgDailies += int(i)
    avgDailies /= len(dailies)

    for i in majors:
        avgMajors += int(i)
    avgMajors /= len(majors)

    return round((avgDailies * dailyWeight) + (avgMajors * majorWeight) + (finalw * finalWeight),2) if finalw else round((avgDailies * dailyWeight) + (avgMajors * majorWeight),2)

dailies = input("Enter your dailies sepparated by commas: ")
dailies = dailies.split(",")
dailyWeight = float(input("Enter your daily weight: "))

majors = input("Enter your majors sepparated by commas: ")
majors = majors.split(",")
majorWeight = float(input("Enter your major weight: "))

final = input("Enter your final grade sepparated by commas (if none, just enter): ")

if final:
    final = float(final)
    finalWeight = float(input("Enter your final weight: "))

    print("Your final grade is: " + str(calculate(dailies, majors, final, dailyWeight, majorWeight, finalWeight)))
else:
    print("Your final grade is: " + str(calculate(dailies, majors, dailyWeight=dailyWeight, majorWeight=majorWeight)))