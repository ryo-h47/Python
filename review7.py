for i in range(0,9):
    print(3**i)
l=[]
for i in range(0,11):
    l.append(3*i)
print(l)
t="python"
for i in t:
    print(i)
j=1
for i in t:
    print("文字: {} - 繰り返し変数: {}".format(i,j))
    j+=1
for i in range(5,26):
    if i%2==0:
        print("{}: 偶数".format(i))
    else:
        print("{}: 奇数".format(i))
l=[52,91,67,88,74,60,83,70]
s=0
for i in l:
    if i>=70:
      s+=1
print("{}人".format(s))
sum=0
for i in l:
    sum+=i
    ave=sum/len(l)
print("{}点".format(ave))
a="abracadabradabra"
num=0
for i in a:
    if i=="a":
        num+=1
print("{}個".format(num))
for i in range(1,1000):
    if i%135==0:
        print(i)
sum=0
for i in range(1,16):
    sum+=i
print(sum)
m=1
for i in range(1,7):
    m*=i
print(m)
sum=0
m=1
n=10
for i in range(1,n+1):
    sum+=i
    m*=i
print("総和: {}".format(sum))
print("総積: {}".format(m))
n=12
S=0
for i in range(1,n+1):
    S+=2*i-1
print(S)
for number in range(1,31):
    if number%3==0 and number%5!=0:
        print("Fizz")
    elif number%3!=0 and number%5==0:
        print("Buzz")
    elif number%3==0 and number%5==0:
        print("FizzBuzz")
    else:
        print(number)
