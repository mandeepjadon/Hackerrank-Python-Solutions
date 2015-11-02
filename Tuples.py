# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
m=map(int,raw_input().split(" "))
print hash(tuple(m))
