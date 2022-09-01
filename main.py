#Lab 2 part 1
first_name = input("Please enter your first name.\t")
last_name = input("Please enter your last name.\t")
age = float(input("How Old Are You?\t")) #age of user
age_years = int(age)
dog_age = age * 7 #age of user in dog years
dog_age_years = int(dog_age / 1) #isolates dog years
dog_age_decimal = dog_age % 1 #isolates the decimal in the dog age 
dog_age_total_days = dog_age_decimal * 360 #puts that decimal into days
dog_age_months = int((dog_age_total_days / 30) / 1) #calculates months from the decimal
dog_age_days = int(((dog_age_total_days / 30) % 1) * 30) #calculates days from the decimal
print("Hi",first_name,"",last_name,",you are",age_years,"years old. You are also",dog_age_years,"year(s),",dog_age_months,"month(s), and ",dog_age_days,"days old in dog years.")
horse_age = ((((age**2)-47)/7)+12)*3
horse_age_years = int(horse_age / 1) #isolates horse years
horse_age_decimal = horse_age % 1 #isolates the decimal in the horse age 
horse_age_total_days = horse_age_decimal * 360 #puts that decimal into days
horse_age_months = int((horse_age_total_days / 30) / 1) #calculates months from the decimal
horse_age_days = int(((horse_age_total_days / 30) % 1) * 30) #calculates days from the decimal
print("Hi",first_name,"",last_name,",you are",age_years,"years old. You are also",horse_age_years,"year(s),",horse_age_months,"month(s), and ",horse_age_days,"days old in horse years.")
mother_height = float(input("What is your Mother's height?"))
father_height = float(input("What is your Father's height?"))
sex = input("What is your biological sex?")
if sex == male or Male:
  ((mother_height + father_height)+5)/2
else:
  ((mother_height + father_height)-5)/2
                            