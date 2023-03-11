# print("#")
# print("##")
# print("###")
# print("####")
# print("#####")

# print('''
# #
# ##
# ###
# ####
# #####
# ''')

# print(10 * 1)
# print(10 * 2)
# print(10 * 3)
# print(10 * 4)
# print(10 * 5)
# print(10 * 6)
# print(10 * 7)
# print(10 * 8)
# print(10 * 9)
# print(10 * 10)

# a = "10"
# b = 10
# int(a)
# a = 10

######## -=============================================================

### Assignment VVVVIP

a = 10
b = 20

# #Output
# a = 20
# b = 10

# # 1.using temp variable swipe two numbers

#     # # temp = a
#     # # a = b
#     # # b = temp

# # 2. without using temp variable swipe two numbers

# 	# # a = a + b	#a = 10 + 20, 	#a = 30
# 	# # b = a - b	#b = 30 - 20,	#b = 10
# 	# # a = a - b	#a = 30 - 10,	#a = 20


#     ### a, b = b, a


# a="Nil"
# b="Priya"
# print("a:",a)
# print("b:",b)

# a=a+b
# b=a[0:len(a)-len(b)]
# a=a[len(b):]

# print("a:",a)
# print("b:",b)



### sort a list without using inbuilt function

## "Mahendra Sigh Dhoni"  => MS Dhoni

a = "Mahendra Sigh Dhoni" 
temp = a.split(" ")
temp[0][0] + temp[1][0] + ' '+ temp[2]
print(temp)

atemp = [10,4,20,59]
temp = atemp
atemp.sort()

print(atemp, temp)


### ===============================================
## c5r8de1n9  ## do addtion of all numbers present in string 
## output 23

##userWord='c5r8de1n9'
userWord = input("Input word for addtion of digit")

sum=0
for char in userWord:
    if char.isdigit():
        sum+=(int(char))    # sum = sum + int(char)
print(f"The sum of digits in String '{userWord}' is equle to: {sum}")

### -------------------------------------------------------------
## if you want to get input till user enter correct input

isWrongInput = True

while isWrongInput: 
    # input
    # validate
    # if wrong input then isWrongInput = True
    # else which correct input then isWrongInput = False
        # actual operaion
    pass


#### ---------------------------------------------------
a = "sada34dfsfsddjhio"
## count number of character present in string 
## count of each char  # s = 3, 0 = 1
## delete duplicate from string and keep only unique character
count=0
for char in a:
    if char.isnumeric():
        count+=1
print(count)