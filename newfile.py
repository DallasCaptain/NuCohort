students = {
    'a':['apple','ardvark'],
    'b':['banana','boy']
}

for key,value in students.items():
    print(key,value)
    newstr = ''
    for eachvalue in value:
        newstr += 'this is value '
        newstr += eachvalue
        newstr += " "
    print (newstr)