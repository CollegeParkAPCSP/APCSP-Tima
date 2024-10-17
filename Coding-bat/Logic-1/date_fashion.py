def date_fashion(you, date):
	return 0 if you <= 2 or date <= 2 else 2 if you >= 8 or date >= 8 else 1
	# don't you dare insult this majestic code
 
date_fashion(5, 10)
date_fashion(5, 2)
date_fashion(5, 5)