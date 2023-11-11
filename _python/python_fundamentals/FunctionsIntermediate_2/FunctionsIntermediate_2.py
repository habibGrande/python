x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1-1

x[1][0] = 15
print(x)

#1-2

michael = students[0] 
michael['first_name'] = 'Bryant'
print(michael)

#1-3
Messi = sports_directory['soccer'][0] 
Messi = 'Andres'
print(Messi)

#1-4
z[0]['y']= 30
print(z)
# --------------------------------------------------------------

def iterateDictionary(students):
    for dictionary in students:
        for key, value in dictionary.items():
            print(key, value)


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]

print(iterateDictionary(students))

# --------------------------------------------------------------


def iterateDictionary2 (users):
    for dictionary in users:
        first_key = list(dictionary.keys())[0]
        first_value = dictionary[first_key]
        print(first_value)


users = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]


print(iterateDictionary2(users))

#3_2

def iterateDictionary2_1 (users):
    for dictionary in users:
        seccond_key = list(dictionary.keys())[1]
        seccond_value = dictionary[seccond_key]
        print(seccond_value)

print(iterateDictionary2_1(users))



# 4

def printInfo(Users_locations):
    for key, value in Users_locations.items():
      print(f"{key}, Size: {len(value)}")
      for item in value:
            print(item)
        

Users_locations ={
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print(printInfo(Users_locations))

