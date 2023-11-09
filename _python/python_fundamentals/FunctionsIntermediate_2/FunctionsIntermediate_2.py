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
