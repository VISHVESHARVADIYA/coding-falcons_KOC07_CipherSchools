a = int(input("Enter Your Date Of Birth(_,__): "))
b = int(input("Enter Your Month Of Birth(_,__): "))
c = int(input("Enter Your Year Of Birth(____): "))
d = int(input("Enter Present Date(_,__): "))
e = int(input("Enter Present Month(_,__): "))
f = int(input("Enter Present Year(____): "))

if b == e and c == f:
    days = d-a
elif b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
    days = (31 - a)
elif b == 2 and c%4 == 0:
    days = (29 - a)
elif b == 2 and c%4 != 0:
    days = (28 - a)
elif b == 4 or b == 6 or b == 9 or b == 11:
    days = (30 - a)

g = b + 1
if b == e and c == f:
    month = 0
elif g == 13 or g >13:
    month = 0
elif g == 2 and c%4 == 0:
    month = (335)
elif g == 2 and c%4 != 0:
    month = (334)
elif g == 3 and c%4 == 0:
    month = (306)
elif g == 3 and c%4 != 0:
    month = (306)
elif g == 4 and c%4 == 0:
    month = (275)
elif g == 4 and c%4 != 0:
    month = (275)
elif g == 5 and c%4 == 0:
    month = (245)
elif g == 5 and c%4 != 0:
    month = (245)
elif g == 6 and c%4 == 0:
    month = (214)
elif g == 6 and c%4 != 0:
    month = (214)
elif g == 7 and c%4 == 0:
    month = (184)
elif g == 7 and c%4 != 0:
    month = (184)
elif g == 8 and c%4 == 0:
    month = (153)
elif g == 8 and c%4 != 0:
    month = (153)
elif g == 9 and c%4 == 0:
    month = (122)
elif g == 9 and c%4 != 0:
    month = (122)
elif g == 10 and c%4 == 0:
    month = (92)
elif g == 10 and c%4 != 0:
    month = (92)
elif g == 11 and c%4 == 0:
    month = (61)
elif g == 11 and c%4 != 0:
    month = (61)
elif g == 12 and c%4 == 0:
    month = (31)
elif g == 12 and c%4 != 0:
    month = (31)




h = c + 1
lyear = 0
nyear = 0
for i in range(h, f):
    if i % 4 == 0:
        lyear += 1
    else:
        nyear += 1

year = (lyear * 366) + (nyear * 365)

if f == c:
    remain = 0
elif e == 1:
    remain = d
elif e == 2:
    remain = 31 + d
elif e == 3 and f%4 == 0:
    remain = 60 + d
elif e == 3 and f%4 != 0:
    remain = 59 + d
elif e == 4 and f%4 == 0:
    remain = 91 + d
elif e == 4 and f%4 != 0:
    remain = 90 + d
elif e == 5 and f%4 == 0:
    remain = 121 + d
elif e == 5 and f%4 != 0:
    remain = 120 + d
elif e == 6 and f%4 == 0:
    remain = 152 + d
elif e == 6 and f%4 != 0:
    remain = 151 + d
elif e == 7 and f%4 == 0:
    remain = 182 + d
elif e == 7 and f%4 != 0:
    remain = 181 + d
elif e == 8 and f%4 == 0:
    remain = 213 + d
elif e == 8 and f%4 != 0:
    remain = 212 + d
elif e == 9 and f%4 == 0:
    remain = 244 + d
elif e == 9 and f%4 != 0:
    remain = 243 + d
elif e == 10 and f%4 == 0:
    remain = 274 + d
elif e == 10 and f%4 != 0:
    remain = 273 + d
elif e == 11 and f%4 == 0:
    remain = 305 + d
elif e == 11 and f%4 != 0:
    remain = 304 + d
elif e == 12 and f%4 == 0:
    remain = 335 + d
elif e == 12 and f%4 != 0:
    remain = 334 + d



zz = days + month + year + remain
zzz = zz + 1


print("As per Vishvesh,Kunal,Ayyappa No of Days You Lived on Earth")
print("Excluding Today:",zz,"Days")
print("Including Today:",zzz,"Days")
