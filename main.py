#Lab 2 part 1
first_name = input("Please enter your first name.\t") #gets user name
last_name = input("Please enter your last name.\t") #gets user last name
age = float(input("How Old Are You?\t")) #age of user
age_years = int(age)
dog_age = age * 7 #age of user in dog years
dog_age_years = int(dog_age / 1) #isolates dog years
dog_age_decimal = dog_age % 1 #isolates the decimal in the dog age 
dog_age_total_days = dog_age_decimal * 360 #puts that decimal into days
dog_age_months = int((dog_age_total_days / 30) / 1) #calculates months from the decimal
dog_age_days = int(((dog_age_total_days / 30) % 1) * 30) #calculates days from the decimal
print("Hi",first_name,"",last_name,",you are",age_years,"years old. You are also",dog_age_years,"year(s),",dog_age_months,"month(s), and ",dog_age_days,"day(s) old in dog years.")
horse_age = ((((age**2)-47)/7)+12)*3 #calculates your horse age
horse_age_years = int(horse_age / 1) #isolates horse years
horse_age_decimal = horse_age % 1 #isolates the decimal in the horse age 
horse_age_total_days = horse_age_decimal * 360 #puts that decimal into days
horse_age_months = int((horse_age_total_days / 30) / 1) #calculates months from the decimal
horse_age_days = int(((horse_age_total_days / 30) % 1) * 30) #calculates days from the decimal
print(first_name,",you are",horse_age_years,"year(s),",horse_age_months,"month(s), and ",horse_age_days,"day(s) old in horse years.")
cat_age = age/9 #calculates your cat age
cat_age_years = int(cat_age / 1) #isolates cat years
cat_age_decimal = cat_age % 1 #isolates the decimal in the cat age 
cat_age_total_days = cat_age_decimal * 360 #puts that decimal into days
cat_age_months = int((cat_age_total_days / 30) / 1) #calculates months from the decimal
cat_age_days = int(((cat_age_total_days / 30) % 1) * 30) #calculates days from the decimal
print(first_name,",you are",cat_age_years,"year(s),",cat_age_months,"month(s), and ",cat_age_days,"day(s) old in cat years.")
mother_height = float(input("What is your mother's height in inches?\t")) #getting mothers height
father_height = float(input("What is your father's height in inches?\t")) #getting fathers height
estimated_height = 0 #initializing a variable
while estimated_height == 0: #While loop to unsure a gender then calculates estimated final height
 sex = input("What is your biological sex?\t")
 if sex == "Male":
  estimated_height = ((mother_height + father_height)+5)/2
 elif sex == "Female":
  estimated_height = ((mother_height + father_height)-5)/2
 else:
  print("Please use inputs Male or Female")
print(first_name,"you are",age_years,"years old and your estimated final height is",estimated_height,"inches.")