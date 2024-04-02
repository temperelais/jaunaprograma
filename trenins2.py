number1 = 20
number2 = 30
number3 = 40
number4 = 30

print(number1*number2)
print(number3+number4)

for i in range(10):
    i1=i-1
    i2=i+i1
    print("current number",i,"previous number",i1,"sum",i2)


str = "abecedefghijklmnopr"

for i in str:
    print(i)

def remove_chars(x,y):
    res=x
    for i in range(y):
        res=rstrip(res)


remove_chars("abcdfghijklmo",4)

    