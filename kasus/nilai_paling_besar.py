# find the greatest value of 3 number

a, b, c = (
    int(input('Enter the value of A : ')),
    int(input('Enter the value of B : ')),
    int(input('Enter the value of C : '))
)

if a > b and a > c:
    print('The largest value is A ')
elif b > a and b > c:
    print('The largest value is B ')
else:
    print('The largest value is C ')