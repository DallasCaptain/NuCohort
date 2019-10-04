# # # Change the value 10 in x to 15. Once you're done,
# # #  x should now be [ [5,2,3], [15,8,9] ].
# # # Change the last_name of the first student from 'Jordan' to 'Bryant'
# # # In the sports_directory, change 'Messi' to 'Andres'
# # # Change the value 20 in z to 30

# # x = [ 
# #     [5,2,3], 
# #     [10,8,9] 
# #     ] 
# # students = [
# #     {'first_name':  'Michael', 'last_name' : 'Jordan'},
# #     {'first_name' : 'John', 'last_name' : 'Jor'}
# # ]
# # sports_directory = {
# #     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
# #     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# # }
# # z = [ {'x': 10, 'y': 20} ]
# # print(x,'before')
# # x [1] [0] = 15
# # print (x)
# # students[0]['last_name'] = 'Bryant'
# # sports_directory['soccer'][0] = 'Andresi'
# # z[0]['y']=30

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(keyname, dict):
#     for student in students:
#         print(student[keyname])


# iterateDictionary2('first_name', students)
# print('*'*20)
# iterateDictionary2('last_name', students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    
    for key,value in dict.items():

        print( len(value) , key.upper() )
        for val in value:

            print(val)

printInfo(dojo)