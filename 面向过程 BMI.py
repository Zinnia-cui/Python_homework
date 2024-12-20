def bmi(weight, height):
    weight = weight * 0.45359237
    height = height * 0.0254
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    name1 = "John Doe"
    age1 = 18
    weight1 = 145
    height1 = 70
    bmi1 = bmi(weight1, height1)
    print(f"{name1} is {age1} years old. His BMI is {bmi1:.2f}, and he is {interpret_bmi(bmi1)}.")
    name2 = "Mary King"
    age2 = 20
    weight2 = 215
    height2 = 70
    bmi2 = bmi(weight2, height2)
    print(f"{name2} is {age2} years old. Her BMI is {bmi2:.2f}, and she is {interpret_bmi(bmi2)}.")

main()