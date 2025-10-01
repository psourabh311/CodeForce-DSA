n = int(input())
s = 0
for i in range(n):
    petya, vasya, tonya = map(int, input().split())
 
    if (petya + vasya + tonya >= 2):
        s += 1
print(s)
