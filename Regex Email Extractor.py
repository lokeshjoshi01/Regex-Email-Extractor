#Bhai baad me update kr skta hu..
import re
str1='''

Hello bro, my name is lokesh joshi and my email id is lokeshjoshi053@gmail.com,
And I am learning programming on code with harry youtube channel and I have one more
email:"lokeshjoshi053@dprotonmail.com"
and some more
email id:<lj@reddit.com>

email:"lj@lj.com.in" and I have one more codewithlj@protonmail.com.

'''
list1=re.findall(r'\w+@\S+\w',str1)

op=open("email_store.txt","a")

j=1
for i in list1:
    op.write(f"Email{j}:{i}\n")
    j=j+1
op.close()

print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")