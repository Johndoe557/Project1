## 함수 선언부
def add_func(n1, n2):
    retVal=n1+n2
    return retVal
def sub_func(n1, n2):
    retVal=n1-n2;
    return retVal
def mul_func(n1, n2):
    retVal=n1*n2;
    return retVal
def dev_func(n1, n2):
    retVal=n1/n2;
    return retVal
def pow_func(n1, n2):
    retVal=pow(n1,n2);
    return retVal
##전역 변수부
num1, num2, res = 100, 200, 0

##메인 코드부
res=add_func(num1,num2)
print(num1,'+',num2,'=',res)
res=sub_func(num1,num2)
print(num1,'-',num2,'=',res)
res=mul_func(num1,num2)
print(num1,'x',num2,'=',res)
res=dev_func(num1,num2)
print(num1,'/',num2,'=',res)
res=pow_func(num1,num2)
print(num1,'^',num2,'=',res)
