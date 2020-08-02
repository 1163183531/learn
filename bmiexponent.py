# TODO（shane） 用公式体重/身高^2 来计算bmi
height = 1.78  # 保存身高的变量，单位米
print("您的身高：", height)
# print("您的身高："+ str(height))  # 可以用str方法来转换成字符串
weight = 80.5  # 保存体重的变量，单位千克
print("您的体重：", weight)

bmi = weight / (height * height)  # 计算BMI指数
print("您的BMI指数：", bmi)
if bmi < 18.5:
    print("您的体重过轻~@_@~")
if 18.5 <= bmi < 24.9:
    print("正常范围，注意保持（-_-）")
if 24.9 <= bmi < 29.9:
    print("您的体重过重~@_@~")
if bmi > 29.9:
    print("肥胖")
