# List-Program No : L2-P6
# Developed By : Vaibhav Bakshi
# Date : 12/01/21

T = (10, 40, 20, 30, 50, 70)

print('The Tuple is T:\n', T)
print('The Tuple in reverse order:\n', T[::-1])
print('Minimum Value in Tuple T:\n', min(T))
print('Maximum Value in Tuple T:\n', max(T))
print()

#To display sum of each adjacent pair of values

O = len(T) -1 if len(T) % 2 else len(T)
print("Adjacent Pair : Sum of Values")
for i in range (0, O-1, 2):
    print(f'{T[i]},{T[i+1]}           {T[i]+T[i+1]}')
print()

#To find pairs whose sum an element in T

P = []
for i in range (len(T)):
    for j in range(i+1, len(T)):
        if (T[i] + T[j]) in T:
            P.append((T[i], T[j]))
            
print("Pairs :     Sum/Element")
for p in P:
      print(p,'     ' ,p[0] + p[1])

