#   63011212098
#   พีรธัช บุตรโท
a = 9
n = ''
while a > 0 :
    mod = a % 2     # ทำการ mod 
    #print(mod)
    a = a//2        # และทำการ mod ไม่เอาเศษ เพื่ออัพ a ให้ mod ต่อ จนกว่า เศษ จะ เท่ากับ 0
    #print(a)
    n += str(mod)   # รวมคำเหมือน
   
print(n[::-1])
if n == n[::-1]:
    print("Palindrome ")
else :
    print("Not Palindrome ")