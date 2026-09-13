print('Suraj')

### Type Function

name='suraj'
print(type(name))

age=27
print(type(age))

print('my age is:-', str(age))
print('my age is:-', str(age)) # in the both condition i am able to run my code

#math
#len Function

password="12348533533"
print(len(password))


if len(password) < 8:
        print( "your password is to short there should be total 8 Number")

##count

text="""
Python is easy to learn.
Many people love python.
"""

print  (text.count('$'))

#replace
price='12345,44444'

print(price.replace(',','.'))

phone='98-788-262-845'
print(phone.replace('-','/'))

phone='98-788-262-845'
print(phone.replace('-',''))

cost= ('$34,98.545')

print(cost.replace(',','.').replace('.',''))

#Python Challenge

#convert the messy phone Number into a clean number format with only digits

moblie_No=('+49(176) 123-4567')

print(moblie_No.replace('+','').replace('(','').replace(')','').replace('-','').replace(' ',''))

 #Join Strings
Firstname='Sri'
LastName='Lanka'
Full_Name=Firstname +' ' + LastName
print(Full_Name)


Folder='Users/suraj/Downloads/sql-ultimate-course-main/datasets/postgres/'
file = "init-postgres-mydatabase.sql"
full_file_path=Folder+file
print(full_file_path)



first_name='Suraj'
last_name= 'yadav'
old=27
is_student=False

print('my self is '+ first_name +' '+ last_name +' i am '+ str(old) + ' year old and student status is '+ str(is_student) + '.')

print(f'my name is {first_name} {last_name}, i am {old} year old, and student status is {is_student}')

print(f'3+3={3+3}' )

print('{{Belive }}')

#Split
a='12-44-66-434-332-55'

print(a.split('-'))

#String repateations

print('*'* 45) 
print('Ha'* 45) 

 #indexing & Slicing

text='python'

print(text[1:4])

#extract the first character
print(text[4])

#extract the last character
print(text[-1])
date='11-9-2026'

#Extract years
print(date[5:])

#Extract the months
print (date[3:4])

#extract the day
print (date[0:2])

#Whitespace cleanup
text="    Engineering".lstrip()
print(text)

text="Engineering    ".rstrip()
print(text)

text=" Engin eering   ".strip()
print(text) 


abc='#####ASSD####'.strip('#')
print(abc)

Course='      Deployment  '
Course1='Deployment'

print()
print(len(Course.strip()))

Intial=len(Course)
after=len(Course.strip())
print('Intial count of text',Intial)

print('After removing spaces and',after)

no_of_spaces= len(Course1)-len(Course1.strip())
is_clean=len(Course1)==len(Course1.strip())
print('No of spaces:',no_of_spaces)
print('is my data clean?',is_clean)

#case Conversion

Search= 'Email'.lower().strip()
data= 'emAil'.lower().strip()
print(Search)
print(data)
print(Search==data)

# Turn the messy string into a single clean summary
#with name, role, and age

Python="968-Maria, (D@t@ Engineer);; 27y.."

name='Maria'
Role='Data Engineer'
age=27

Summary=f"name:{name} Role : {Role} Age:{age}"
print(Summary)

#Search-String Function

phone="+91-8788261856"
print(phone.startswith('+91'))

email='yadavsijsj@gmail.com'
print(email.endswith('@outlook'))

file='data_backup.csv'
print(file.endswith('csv'))

print('@' in email)

print('8788' in phone)

url=("https://www.hackerrank.com/domains/sql")
print('hackerrank' in url)

#search
phone1= '+91-8788261856'
phone2='8459237343'

print(phone1[4:13])
print(phone1[4:])
print(phone2[3:])

print(phone1.find("-"))

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])

#validation


#isalpha

country='INDIA'
country1='USA1'

print(country.isalpha())
print(country1.isalpha())

#isnumeric
phone='8788261856'

print(phone.isnumeric())

