# conditional statemnet will check the conditiom
# to check the condition we use if else
#wap to check user eligible for voting
# userage=int(input("enter your age"))
#note the default input function return type is string
# for vote userage must be greater thean 18
# if userage>=18:
#     print("you r eligible for voting")
# else:
#     print("you r not eligible for voting")


# userGender=input("enter your gender")

# if userGender=="male":
#     print("you cannot sit in 1st compartment of metro")

# elif userGender=="female":
#     print("you cann sit in 1st compartment of metro")
# else:
#     print("you can sit in any compartment of metro")



# wap if gender and age greater than 18->govt job apply
# else male age greater thean 18> private job apply

# userGender=input("enter your gender")
# userage=int(input("enter your age"))

# if userGender=="female" and userage>=18:
#     print("your are eligible for govt job")

# elif userGender=="male" and userage>=18:
#     print("your are eligible for prvt job")

# else:
#     print("you are not eligible")


# it prints the all litertions 
# userName="saksham joshi"
# for i in userName:
#     print(i)

# #print 1 to 20 using loop
# for i in range(1,11):
#     print(i)


# wap in create table of any no

# number=int(input("enter your number"))
# for a in range(1,11):
#     print(number*a)

# # wap print the pattern  1 4 7 10 13
# for x in range(1,14,3): #3 is step size
#     print(x)

# wap to print pattern 1 3 7 11 13 15
for b in range(1,16,2):
    if b==9 or b==5:
        continue #skip the current iteration
    else:
        print(b)