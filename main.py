# WeightConvert.py
weight_str=input()
  unit=weight_str[-2:].lower()
if unit == 'kg':
  kg=float(weight_str[:-2])
  pd=kg*2.2046
  print(f"转换后的重量是{pd:.3f} pd")
elif unit == 'pd':
  pd=float(weight_str[:-2])
  kg=pd/2.2046
  print(f"转换后的重量是{kg:.3f} kg")
else:
  print("输入格式错误") 
