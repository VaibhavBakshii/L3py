# List-Program No : L2-P7
# Developed By : Vaibhav Bakshi
# Date : 12/01/21

WD = (1, 2, 3, 4, 5, 6, 7)
WDN = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
W = {}

# To create a dictionary W with key-value pairs with corresponding values from WD and WDN

for i in range(len(WD)):
    W[WD[i]] = WDN[i]
print('W:', W)

#To re-arrange the content of dictionary

for j in W.keys():
    W[j] = W[j+1] if j < len(W) else WDN [ len(WDN) - j]
print('The Re-arranged W:', W)

'''
To copy the partial content of W in dictionaries MyDays and OfficeDays, MyDays should have content from keys 2,4 and 7 and rest from W to be the content of OfficeDays.
'''

MyDaysLis = [2, 4, 7]
MyDays = {}
OfficeDays = {}

for j in W.keys():
    if j in MyDaysLis:
        MyDays[j] = W[j]
    else:
        OfficeDays[j] = W[j]

print('MyDays:', MyDays)
print('OfficeDays:', OfficeDays)
    
