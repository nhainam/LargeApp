#!venv/bin/python

fin=open('toys.txt', 'r')
toys = {}
for word in fin:
    x = word.replace("\n",",").split(",")
    a = x[0]
    b = x[1]
    toys[a]=str(b)
    print word.__str__()
    i = input("Please enter the code:")
    if i in toys:
        print(i," is the code for a= ", toys[i],)
    else:
        print('Try again')
    if i == 'quit':
        break