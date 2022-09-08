
# Print the pattern
# n=0
# while n<=5:
#     ast
#     print()

n=5
string=''
for i in range(n):
    string+='*'
    print(string)
    string+=' '
for i in range(1,n):
    times=n-i
    string=('*'+' ')*(times-1)+'*'
    print(string)


#make a list of 4 '*' and remove last index every iteration