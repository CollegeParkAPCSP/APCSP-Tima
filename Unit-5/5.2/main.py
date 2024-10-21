def morning_message(date, fname, percent, temp):
    print(f"Good morning {fname}, today is {date}")
    print(f"The current temperature is {temp}F")
    print(f"There is a {100*percent}% chance of rain today")
    
    x = "chilly" if temp < 70 else "beautiful" if temp <= 85 else "scorching"
    print(f"Have a {x} day!")
    
morning_message( "10/21/2024", "Christy", 0.6, 67)
morning_message( "10/21/2024", "Misty", 0.2, 81)
morning_message( "10/21/2024", "Bob", 0.8, 99)