# 在这个文件下编写代码
# WeightConvert.py
weight_str=input("请输入带有单位的重量值:")
  unit=weight_str[-2].lower()
if unit=='kg':
  kg=float(weight_str[:-2])
  pd=kg*2.2046
  print(f"转换后的重量是{pd:.3f}pd")
elif unit=='pd':
  pd=float(weight_str[:-2])
  kg=pd/2.2046
  print(f"转换后的重量是{kg:.3f}kg")
else:
  print("输入格式错误，请输入正确单位，例如 10kg 或 10pd") 
