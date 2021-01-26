# t=1,2,'isaac',4.5
# print(type(t))

# blank_tuple= tuple()
# print(blank_tuple)

num_tuple=(1,2,3,4,5)
# print(num[2])
# print(num[-6])

# add = (3+5,)
# print(add*2)
# print(num[2:])
num_list = [1,2,3,4,5]
num_list[1]=9
print(num_list)

fruits = ("apple","banana","mango")
print('orange' in fruits)

x=5
y=7
x,y=y,x

print("x is = ",x)
print("y is = ",y)

#assignment
# email is mugishaisaac@gmail.com
# extract username and domain from gmail
# username dshould be mugishaisaac
# domain should be gmail.com

# email = 'mugishaisaac@gmail.com'
# username = email[0:12]
# domain = email[13:]
# print("username is: ",username)
# print("domain is: ",domain)

email = "mugishaisaac@gmail.com"
username,domain = email.split('@')
print('username: ', username)
print('domain: ', domain)
