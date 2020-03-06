#converting decimal to binary;
res=int(input("Enter the value : "));
val=[];
while res>0:
        if res%2==0:
                val.append(0);
                res=int(res/2);
        elif res%2==1:
                val.append(1);
                res=int(res/2);
        if res==2 and res%2==0:
                val.append(0);
                val.append(1);
                break;
        elif res/2==1 and res%2==1:
                val.append(1);
                val.append(1);
                break;
x='';
for y in range(len(val)-1,-1,-1):
        x+=str(val[y]);

print(x);
