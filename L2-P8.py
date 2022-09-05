# List-Program No : L2-P8
# Developed By : Vaibhav Bakshi
# Date : 12/01/21

#To initialize a tuple TL=('RED','YELLOW','GREEN')

TL = ('RED', 'YELLOW', 'GREEN')

#To accepts names of 10 colors from user and store them in a list CL

CL = []
C = 0
while C <= 9:
    color = input('Enter a color:')
    CL.append(color)
    C += 1
print('List CL:', CL)

#To display the color names from CL along with corresponding message "TRAFFIC LIGHT" and "NOT TRAFFIC LIGHT" after checking from the content of TL

for color in CL:
    if color.upper() in TL:
        print('TRAFFIC LIGHT')
    else:
        print('NOT TRAFFIC LIGHT')

#To initialize another tuple TM=('STOP','BE READY TO START/STOP','GO')

TM = ('STOP', 'BE READY TO START/STOP', 'GO')

#To create a dictionary TLM by combining corresponding key-value pairs from TL and TM.

TLM = {}
for i in range (len(TL)):
    TLM[TL[i]] = TM[i]

print('TLM Dictionary:', TLM)

