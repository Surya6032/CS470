value=int(input("Enter max number:"))
numbers=[True for i in range(value)]
for i in range(len(numbers)): 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        numbers[i]=False
for i in range(len(numbers)):
  if numbers[i]==False:
    print(i, end=" ") 
