# Number 1: Basic Boolean Evaluation

def evaluate_conditions(a: bool, b: bool) -> bool: # just good practice to give parameter and return types
    return (a and b) or (a or b)

# evaluate_conditions(True, True)
# evaluate_conditions(True, False)
# evaluate_conditions(False, True)
# evaluate_conditions(False, False)

# Number 2: Teenager Check

def is_teenager(age: int) -> bool:
    return 13 <= age <= 19

# is_teenager(23)
# is_teenager(13)
# is_teenager(18)
# is_teenager(9)

# Number 3: Valid Login

def is_valid_login(username: str, password: str) -> bool:
    return username == 'admin' and password == 'secret'
    
# is_valid_login("admin", "secret")
# is_valid_login("adin", "scret")
# is_valid_login("admin", "password")
# is_valid_login("user", "secret")

# Number 4: Exclusive Condition

def exclusive_or(a: bool, b: bool) -> bool:
    return a != b

# exclusive_or(True, True)
# exclusive_or(True, False)
# exclusive_or(False, True)
# exclusive_or(False, False)

# Number 5: Light Switch

def lights_on(switch1: bool, switch2: bool) -> bool:
    return switch1 or switch2

# lights_on(True, True)
# lights_on(True, False)
# lights_on(False, True)
# lights_on(False, False)

# Number 6: Eligibility Check

def is_eligible(age: int, citizenship: bool) -> bool:
    return 18 <= age and citizenship

# is_eligible(12, True)
# is_eligible(18, True)
# is_eligible(18, False)
# is_eligible(21, False)

# Number 7: Combination of Conditions

def can_drive(age: int, has_license: bool) -> bool:
    return 16 <= age and has_license

# can_drive(12, True)
# can_drive(16, True)
# can_drive(16, False)
# can_drive(21, False)

# Number 8: Complex Condition

def is_safe_to_cross(traffic_light: str, pedestrian_signal: str) -> bool:
    return traffic_light == "green" and pedestrian_signal == "walk"

# is_safe_to_cross("green", "walk")
# is_safe_to_cross("red", "run")
# is_safe_to_cross("yellow", "wlk")
# is_safe_to_cross("green", "Walk")

# Number 9: Leap Year

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 400 == 0 or year % 100 != 0

# is_leap_year(1900)
# is_leap_year(2000)
# is_leap_year(4)
# is_leap_year(3200)
