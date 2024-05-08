young_driver_age = 25
older_driver_age = 70
elderly_driver_age = 80

young_driver_premium_multiplier = 2
older_driver_premium_multiplier = 1.5
elderly_driver_premium_multiplier = 2
young_driver_experience_multiplier = 2
no_multiplier = 1

young_driver_experience = 2
older_driver_experience = 5

# Assigns a premium multiplier depending on the age and experience of the driver
def agecheck (age, exp):
    
	if age <= young_driver_age and exp <= young_driver_experience: 
		return young_driver_premium_multiplier * young_driver_experience_multiplier

	if age <= young_driver_age:
		return young_driver_premium_multiplier

	if (age > older_driver_age and age <= elderly_driver_age) and exp <= older_driver_experience:
		return older_driver_premium_multiplier

	if age > elderly_driver_age:
		return elderly_driver_premium_multiplier

	return no_multiplier

