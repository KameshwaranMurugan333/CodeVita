def findValency(an):
    return (an - 1) % 9 + 1 if an > 0 else 0

# Getting the input
nonBalancedComponent=input()
equivalentPoint=int(input())

first=[]
sec=[]

# Spliting the component
firstComponent=nonBalancedComponent[0]
secondComponent=nonBalancedComponent[1]

# Finding the ASCII number of the components
ASCIIOfFirstComponent=ord(firstComponent)
ASCIIOfSecondComponent=ord(secondComponent)

valencyOfFirstComponent=findValency(ASCIIOfFirstComponent)
valencyOfSecondComponent=findValency(ASCIIOfSecondComponent)

i=equivalentPoint
flag=0

while(i>0):
   x=i*valencyOfFirstComponent
   y=equivalentPoint-x
   if y>0 and y%valencyOfSecondComponent==0:
      first.append(i)
      sec.append(y//valencyOfSecondComponent)
      flag=1
   i=i-1
if flag==0:
    print("Not Possible") 
for i in range(len(first)) :
   if (i+1 )!=(len(first)):
       print(firstComponent + str(first[i])+" "+secondComponent+str(sec[i]))      
   else:
       print(firstComponent + str(first[i])+ " "+secondComponent+str(sec[i]),end="")