
# Print the pattern
# n=0
# while n<=5:
#     ast
#     print()

# n=5
# string=''
# for i in range(n):
#     string+='*'
#     print(string)
#     string+=' '
# for i in range(1,n):
#     times=n-i
#     string=('*'+' ')*(times-1)+'*'
#     print(string)

n=5
stars=[]
for i in range(n):
    stars.append('*')
    print(' '.join(stars))
while len(stars)>1:
    stars.pop()
    print(' '.join(stars))


#make a list of 4 '*' and remove last index every iteration