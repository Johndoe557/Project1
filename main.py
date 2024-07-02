## 함수 선언부
def add_func(n1, n2):
    retVal=n1+n2
    return retVal


##전역 변수부
num1, num2, res = 100, 200, 0

##메인 코드부
res=add_func(num1,num2)
print(num1,'+',num2,'=',res)
