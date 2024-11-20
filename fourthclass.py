# list in python
# list store multiple data
mylist=["pawan","ivan","deepanshu"]
# tuple store multiple data
mytuple=("pawan","ivan","deepanshu")
# set store multiple data
myset={"pawan","ivan","deepanshu"}
# dictionary store multiple data in key value pair
mydict={"name":"joshi","email":"sakshamjoshi@gmail.com"}

# # to check the data type of all above data set
# print("list:",type(mylist),"tuple:",type(mytuple))
# print("set:",type(myset),"dict:",type(mydict))

# # how to identify list,set,tuple,dictionary
# # list ->[]==list can have duuplicate item
# # tuple->()==tuple can store duplicate item
# # set->{}==no duplicate item
# # dict->{:}==no dulpicate item

# # access complete data from data set
# print ("list:",mylist[0])
# print("tuple:",mytuple[0],"dict:",mydict["name"])

# # access complete data from data set
# for data in mylist:
#     print("list",data)
# for item in myset:
#     print("set",item)
# for value in mytuple:
#     print("tuple",value)
# for x in mydict.values():
#     print("dict",x)


# # to check with data set support duplicate data
# print("list",mylist,"tuple",tuple,"dict",mydict,"set",my)\

# to update the data in all data set
# mylist[0]="joshi"
# print(mylist)
# chngeable

# mytuple[0]="joshi"
# print(mytuple)
# # tuple is not chnageble

# myset[0]="joshi"
# print(myset)
# # set is not chngeble

# mydict["name"]="saksham"
# print(mydict)
# # my dict has no index it has only base and base is name so we put r value in name
# # my dict is chngeable

# # add new  value in data set
# mylist.append("ivan")
# myset.add("dushyant")
# mydict.update({"name":"joshi"})
# print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)

# to remove data set
mydict.pop("name")
mylist.pop(0)
myset.remove("pawan")
print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)


# you cannot uupdate or chnge anything in tuple
# tuple only comes with 2 functions

# convert tuple to list
convertlist=list(mytuple)
print(type(convertlist))
convertlist.append("rohan")
convertlist.pop(2)
print(convertlist)
mytuple=tuple(convertlist)  #convert to tuple
print(mytuple)

