weight=eval(input('Enter weight in kg:'))
height=eval(input('Enter height in meter:'))
BMI=weight/(height*height)
print('BMI is %.2f'%BMI)
if BMI < 18.5:
    print("BMI\'s international interpretations is Underweight")
    print("BMI\'s domestic interpretations is Underweight")
elif 18.5 <= BMI < 24.0:
    print("BMI\'s international interpretations is Normal")
    print("BMI\'s domestic interpretations is Normal")
elif 24.0 <= BMI < 25.0:
    print("BMI\'s international interpretations is Normal")
    print("BMI\'s domestic interpretations is Overweight")
elif 25.0 <= BMI < 28.0:
    print("BMI\'s international interpretations is Overweight")
    print("BMI\'s domestic interpretations is Overweight")
elif 28.0 <= BMI < 30.0:
    print("BMI\'s international interpretations is Overweight")
    print("BMI\'s domestic interpretations is obese")
elif BMI >= 30.0:
    print("BMI\'s international interpretations is obese")
    print("BMI\'s domestic interpretations is obese")