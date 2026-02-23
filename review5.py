x=2
x<10
x=-6
abs(x)<5
word="Python"
word=="Python"
35 not in [10,20,30,40,50]
"world" in "Hello world!"
text="analysis"
len(text)>5 and len(text)<=10
score=95
if score>80:
  print("優秀です")
number=6
if number%2==0:
  print("偶数です")
hour=15
if hour<12:
  print("午前")
else:
  print("午後")
number=-4
if number>0:
  print("正の数です")
else:
  print("正の数ではありません")
grade=75
if grade>=80:
  print("優")
elif grade>=60 and grade<80:
  print("良")
elif grade>=40 and grade<60:
  print("可")
else:
  print("不可")
temperature=27
if temperature>=30:
  print("猛暑です")
elif temperature>=25 and temperature<30:
  print("暑いです")
elif temperature>=15 and temperature<25:
  print("過ごしやすいです")
else:
  print("寒いです")
x=25
if x>=10 and x<=20:
  print("範囲内です")
else:
  print("範囲外です")
fruit="apple"
if fruit in ["apple","orange","banana"]:
  print("取り扱いがあります")
else:
  print("取り扱いがありません")
number=10
if number%3==0 and number%5!=0:
  print("Fizz")
elif number%5==0 and number%3!=0:
  print("Buzz")
elif number%3==0 and number%5==0:
  print("FizzBuzz")
else:
  print(number)
number=13
if number%3==0 or '3' in str(number):
  print("3に関する数です")
a=3
b=4
c=5
if a+b>c and b+c>a and c+a>b:
  if a==b and b==c:
    print("正三角形")
  elif a==b or b==c or c==a:
    print("二等辺三角形")
  else:
    print("不等辺三角形")