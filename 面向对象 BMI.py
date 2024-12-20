class Person():
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def bmi(self):
        self.kg = self.weight * 0.45359237
        self.m = self.height * 0.0254
        BMI = self.kg / (self.m ** 2)
        return BMI

    def interpret_bmi(self):
        bmi_value = self.bmi()
        if bmi_value < 18.5:
            return "Underweight"
        elif bmi_value <= 24.9:
            return "Normal"
        elif bmi_value <= 29.9:
            return "Overweight"
        else:
            return "Obese"

name1 = "John Doe"
age1 = 18
weight1 = 145
height1 = 70
person1 = Person(name1, age1, weight1, height1)
print(f"{person1.name} is {person1.age} years old. His BMI is {person1.bmi():.2f}, and he is {person1.interpret_bmi()}.")

name2 = "Marry King"
age2 = 20
weight2 = 215
height2 = 70
person2 = Person(name2, age2, weight2, height2)
print(f"{person2.name} is {person2.age} years old. Her BMI is {person2.bmi():.2f}, and she is {person2.interpret_bmi()}.")
