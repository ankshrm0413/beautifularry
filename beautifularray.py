#beautiful array

#iterating till the range and taking the no of elements as input.
for i in range(int(input())):
#takes interger input from the user
    n=int(input())
    #another variable with value zero
    c=0
    d={0:0,1:0,-1:0}
    #gets user input and returns a string splits that input on whitespaces, applies the function fn to each element in the sequence, applies int to each string element in the input. 
    for x in map(int,input().split()):
        if x not in d:
            #executing the statement if it's satisfy then it will increment the value of input and store it.
            c+=1
            #executing when the above statement if it's dis-satisfy then it will increment the value of input and store it on variable d.
        else:
            d[x]+=1
        if c>1:
            print('no')
            break
         #else part is executed if the above condition is notvalid then it will print NO.
    else:
        if c and d[-1]:
            print('no')
            #this varifies again when if above condition in not valid and if this satisfy then print no or else part will be executed directly.
        elif d[-1]>1 and d[1]==0:
            print('no')
        else: 
            print('yes')