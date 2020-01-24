a = input('input the sting').split()
k=''
for i in a:
    if i not in k:
        k+=i
        b = a.count(i)
        print(i,':',b)
	
