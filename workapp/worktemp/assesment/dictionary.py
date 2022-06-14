d1={"kerala":"tvm","bihar":"patna","tamilnadu":"chennai"}
state=input("enter a state")
for i in d1:
    if state==i:
        b=d1[i]
        print(b)
        break
    else:
        print('not found')
        break

