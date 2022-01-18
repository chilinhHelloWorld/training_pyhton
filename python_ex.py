# from user import User

# userList = []
# userUpdateList = []


# # file_object = open('Users.txt')
# # data = file_object.readlines()
# # file_object.close()


# def splitStr(dataFromFile):
#     usertmp = dataFromFile.split("-")
#     name = usertmp[0]
#     age = usertmp[1]
#     address = usertmp[2]
#     user = User(name, age, address.rstrip("\n"))
#     return user

# # for user in data:
# #     userList.append(splitStr(user))

# def addUser(number):
#     count = 1
#     for i in range(int(number)):
         
#          print ("Enter information of user " + str(count) + ":")
#          name = input("enter full name: ")
#          age = input("enter age: ")
#          address = input("enter address: ")
#          user = User(name, age, address)
#          userUpdateList.append(user)
#          count += 1
    
#     writeFile(userUpdateList)
#     menu()

# def writeFile(userList):
#     file_object = open('Users.txt', mode='w')
#     for u in userList:
#         file_object.writelines(u.name + "-" + u.age + "-" + u.address)
#         file_object.write('\n')
        
#     file_object.close()

# def getUSerFromFileToList ():
#     file_object = open('Users.txt')
#     data = file_object.readlines()
#     file_object.close()
#     for u in data :
#         userUpdateList.append(splitStr(u))
    
# def displayAllUsers ():
#     print ( "Index " + "---"+ "Name" + "-----" +"Age" + "------" +"Address")
#     count = 1    
#     for user in userUpdateList:
#         print ( str(count) + "      "+ user.name + "     " + user.age + "     " + user.address)
#         count += 1
# def option(num):
#     while ( 0 < int(num) < 4):
#         if (int(num) == 1):
#             print("------------Add new User----------------")
#             numberOfUser = input("Please enter number of user you want add (limit 5): ")
#             addUser(numberOfUser)
#             break
#         elif (int(num) == 2):
#             exit()
#             break
#         elif (int(num) == 3):
#             print("------------List User----------------")
#             displayAllUsers()
#             print("-----------Action--------------")
#             print("1. Update")
#             print("2. Delete")
#             print("3. Exit")
#             op = input("Enter number option: ")
#             if(int(op) == 1):
#                 displayAllUsers()
#                 print("------Update user------")
#                 index = input("Please enter index of user you want update: ")

#                 name = input("enter full name: ")
#                 age = input("enter age: ")
#                 address = input("enter address: ")
#                 user = User(name, age, address)
#                 userUpdateList[int(index) - 1] = user
#                 displayAllUsers()
#                 writeFile(userUpdateList)
#                 menu()
#             elif(int(op) == 2):
#                 print("------Delete user------")
#                 index = input("Please enter index of user you want delete: ")
#                 userUpdateList.remove(userUpdateList[int(index) - 1])
#                 displayAllUsers()
#                 writeFile(userUpdateList)
#                 menu()
#             elif(int(op) == 3):
#                 menu()

#             break
#     else :
#         print("Option number only from 1 to 4")
#         num = input("Enter number: ")    
#         option(num)


# def menu():
#     print("--------------Manage User-----------------")
#     print("Please choose option: ")
#     print("1. Add user")
#     print("2. Exit")
#     print("3. Display all user")

#     num = input("Enter number: ")
#     option(num)

# getUSerFromFileToList()
# menu()

def add(x, y = 2):
    return x + y
def product(x, y=2):
    return x * y
def add_product(x,y):
    return x + y

    




