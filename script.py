def add(x, y):
    return float(x) +float(y)


val1=input('Enter the first number')
val2=input('Enter the second number')
sum=add(val1,val2)
print('The sum of {0} and {1} is {2}'.format(val1, val2, sum))