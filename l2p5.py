# List-Program No : L2-P5
# Developed By : Vaibhav Bakshi
# Date : 12/01/21

C=['Delhi','Mumbai','Hyderabad']

def AddCity(C):
    
    while True:
        city = input('Enter The Name of The City')
        C.append(city)
        cont = input('Continue Adding Cities? (Y/N?)')
        if cont in ['n','N']:
            break
    print('List is:\n', C)

def AllUCase(C):
    
    T = []
    for S in C:
        T.append(S.upper())
    print('Cities in List in UpperCase:\n',T)

def ShowDisp(C):

    print('Cities in the list C are:\n', C)

def ShortNameCities(C):

    T = []
    for S in C:
        if len(S) <= 4:
            T.append(S)
    print('Cities in list C with less than 4 Characters:\n', T)

def BigNameCities(C):

    T = []
    for S in C:
        if len(S) > 4:
            T.append(S)
    print('Cities in list C with more than 4 characters:\n', T)

def CityNameLength(C):
    print('Number of alphabets in each name of the city in list C:\n')
    for S in C:
        print('City:', S, 'Characters:', len(S))

AddCity(C)
AllUCase(C)
ShowDisp(C)
ShortNameCities(C)
BigNameCities(C)
CityNameLength(C)
        
