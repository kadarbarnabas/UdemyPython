import random as r

def gensquares(n):
    for x in range(n):
        yield x ** 2
        
for i in gensquares(10):
    print(i)
 
print("\n")   
def rand_num(low, high, n):
    for x in range(n):
        yield r.randint(low, high)
        
for x in rand_num(1, 10, 12):
    print(x)
    
print("\n")   

s = 'hello'
s_iter = iter(s)
print(type(s_iter))

print("\n") 

my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 2)

for item in gencomp:
    print(item)