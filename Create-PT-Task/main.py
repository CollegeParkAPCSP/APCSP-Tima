print("\033c")
def calculate(dailies: list=[], majors:list=[], finalw:float = None, dailyWeight:float=None, majorWeight:float=None, finalWeight:float=None, classAvg:float=None):
    avgDailies = 0
    avgMajors = 0
    if classAvg:
        classAvg = float(classAvg)
        return round(classAvg*(1-finalWeight) + (finalw * finalWeight),2) if finalw else round(classAvg,2)
    else:
        for i in dailies:
            avgDailies += float(i)
        avgDailies /= len(dailies)

        for i in majors:
            avgMajors += float(i)
        avgMajors /= len(majors)

        return round(((avgDailies * dailyWeight) + (avgMajors * majorWeight))*(1-finalWeight) + (finalw * finalWeight),2) if finalw else round((avgDailies * dailyWeight) + (avgMajors * majorWeight),2)
classAvg=(input("Enter your class average or hit enter to enter dailies and majors individually: "))
if(classAvg):
    pass
else:
    k = (input("Enter your dailies separated by commas: "))
    dailies = k.split(",")
    dailyWeight = float(input("Enter your daily weight: "))

    kk = (input("Enter your majors separated by commas: "))
    majors = kk.split(",")
    majorWeight = float(input("Enter your major weight: "))

final = float(input("Enter your final grade(if none, just enter): "))

if classAvg:
    if final:
        final = float(final)
        finalWeight = float(input("Enter your final weight: "))
        print("Your final grade is: " + str(calculate(finalw=final, finalWeight=finalWeight, classAvg=classAvg)))
    else:
        print("Your final grade is: " + str(classAvg))
elif final:
    final = float(final)
    finalWeight = float(input("Enter your final weight: "))

    print("Your final grade is: " + str(calculate(dailies=dailies, majors=majors, finalw=final, dailyWeight=dailyWeight, majorWeight=majorWeight, finalWeight=finalWeight)))
else:
    print("Your final grade is: " + str(calculate(dailies=dailies, majors=majors, dailyWeight=dailyWeight, majorWeight=majorWeight)))