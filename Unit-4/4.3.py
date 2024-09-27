def grade(score: float):
        
    if score < 0.0 or score > 5.0:    
        # error handling :O
        # makes it a lot easier, no need to write < x < every time
        return 'Invalid input!'
    elif score == 5.0:
        return 'Perfect score!'
    elif score >= 4.0:
        return 'That\'s an A!'
    elif score >= 3.0:
        return 'That\'s a B!'
    elif score >= 2.0:
        return 'That\'s a C!'
    elif score >= 1.0:
        return 'That\'s an D!'
    elif score >= 0.0: 
        return 'That\'s an F :('
    
print(grade(float(input('Enter your score: '))))

print(grade(5.0))
print(grade(4.4))
print(grade(3.8))
print(grade(2.3))
print(grade(1.9))
print(grade(0.0))
print(grade(4.0))
print(grade(3.01))
print(grade(1.9999))
print(grade(5.1))