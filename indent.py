# python 根据冒号和缩进来识别代码块的，
# 冒号代表了代码的开始

height = 1.70  # 保存身高的变量，单位：米
print("您的身高：" + str(height))
weight = 48.5  # 保存体重的变量，单位：千克
print("您的体重：" + str(weight))
bmi = weight / (height * height)  # 用于计算BMI指数，公式为“体重/身高的平方”
print("您的BMI指数为：" + str(bmi))  # 输出BMI指数