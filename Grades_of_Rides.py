a,b,c=map(int,input().split())
i=0
if a>50 and b>60 and c>100 :
    i=10
elif a>50 and b>60:
    i=9
elif b>60 and c>100:
    i=8
elif a>50 and c>100:
    i=7
elif a>50 or b>60 or c>100:
    i=6
else:
    i=5
print(i)
    