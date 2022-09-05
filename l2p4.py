# List-Program No : L2-P4
# Developed By : Vaibhav Bakshi
# Date : 12/01/21

L=[1,2,3,4,5]

def AddValues(L):
    
    while True:
        Value = int(input('Enter the value to add in the List L'))
        L.append(Value)
        Cont = input('Continue Adding Values (Y/N?)')
        if Cont in ['N','n']:
            break
    print('List is:\n', L)

def DispValues(L):
    print("Final Values of List L:\n", L)

def SwapPair(L):
    
    T = L
    Length = len(T)
    S = Length - 1 if Length % 2 else Length
    for i in range(0, S - 1, 2):
        T[i], T[i+1] = T[i+1], T[i]
    print('List with re-arranged content with adjacent neighbouring values swapped:\n', T)

def SwapHalf(L):

    T = len(L) // 2
    Add = L[T:] + L[:T]
    print('List with re-arranged content with first and second half swapped:\n', Add)

AddValues(L)
DispValues(L)
SwapPair(L)
SwapHalf(L)


    
