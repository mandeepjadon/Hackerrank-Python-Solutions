# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(raw_input())
b=set(raw_input().split(" "))
c=int(raw_input())
d=set(raw_input().split(" "))
e=sorted(map(int,list(d.difference(b).union(b.difference(d)))))
for i in e:
    print i
