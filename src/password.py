import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

req1=False
req2=False
req3=False
req4=False

length=False

for i in password:
    if i.islower():
        req1=True
    if i.isupper():
        req2=True
    if i.isnumeric():
        req3=True
    if i in "$#@":
        req4=True

if len(password)>5 and len(password)<17:
    length=True

if req1 and req2 and req3 and req4 and length:
    is_valid=True

# print(len(password))

# print(length)
# print(req1)
# print(req2)
# print(req3)
# print(req4)

print(is_valid)
