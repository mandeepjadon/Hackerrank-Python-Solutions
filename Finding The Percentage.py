#Did it via list . Fuck DICT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
li=[]
for i in range(n):
    li.append(raw_input().split())
name=raw_input()
for i in range(n):
    if li[i][0]==name:
        print "%.2f"%((float(li[i][1])+float(li[i][2])+float(li[i][3]))/3)
