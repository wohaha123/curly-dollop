
a = 10
b = "你好"

def get_bmi(height, weight):
    height /= 100
    bmi = weight / height ** 2
    bmi = round(bmi, 1)
    return bmi

def get_bmr(sex, height, weight, age):
    if sex == "男":
        bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age
    else:
        bmr = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
    bmr = round(bmr, 2)
    return bmr

def get_tdee(sex, height, weight, age, times):
    bmr = get_bmr(sex, height, weight, age)
    tdee = bmr * times
    tdee = round(tdee, 2)
    return tdee