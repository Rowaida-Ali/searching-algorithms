#tak 1
l1=list(input("enter a list "))
l1.sort()
print(l1[-2])


#task 2
l5=list(eval(input("enter a list")))
l5.sort()
missing=0
for i in range(l5[0],l5[-1]+1):
    if i not in l5:
        missing=i
    else:
        missing="nothing is missed"    
print(missing) 

   
#task 3
s=eval(input("enter numbers "))
dict={

}    
for i in s:  
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)     
l4=list(dict.values())  
print(max(l4))
       

#task 4
r=list(eval(input("enter a list")))
if r[-1]<r[0]:
    print("not sorted")
     