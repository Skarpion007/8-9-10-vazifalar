#               #1- amaliyot
# juft_son = int(input("juft son kirit:"))
# if juft_son % 2 == 0:
#     print("Raxmat")
# else:
#     print("bu toq son")
    
    
                #2- amaliyot
# yosh = int(input("Yoshingiz nechada:"))
# if yosh < 4 or yosh > 60:
#     print("sizga kirish bepul")
# elif yosh < 18:
#     print("kirish 10000 som")
# elif yosh > 18:
#     print("kirish 20000 som")


#             #3-amaliyot
# a = int(input("1-sonni kirit:"))            
# b = int(input("2-sonni kirit:")) 
           
# if a > b:
#     print(f"{a} > {b}")
# if a < b:
#     print(f"{b} > {a}")
# else:
#     print("ular teng")
    
    
#     ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")
    
# #     #4-amaliyot
# mahsulotlar = ["olma", "anor", "nok", "kivi", "limon", "banan", "uzum",
#                 "bexi", "shaftoli", "gilos"]
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni qoshing:"))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
    

    #5-amaliyot
mahsulotlar = ["olma", "anor", "nok", "kivi", "limon", "banan", "uzum",
               "bexi", "shaftoli", "gilos"]

bor_mahsulotlar = []
yoq_mahsulotlar = []

for n in range(5):
    mahsulot = input(f"{n+1}-mahsulotni kiriting: ")
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
          
    else:
       yoq_mahsulotlar.append(mahsulot)
if not yoq_mahsulotlar:
    print(f"siz soragan mahsulotlar dokonimizda {bor_mahsulotlar} bor")
else:
    print(f"siz soragan mahsulotlar {yoq_mahsulotlar} bizda yo'q")
     
#   #6-amaliyot
# foydalanuvchilar = ["real", "barca", "apple", "samsung"]
# yangi_login = []
# yangi_login.append(input("Loginni kiriting:"))
# for foydalanuvchi in yangi_login:
#    if foydalanuvchi in foydalanuvchilar:
#         print("xush kelibsiz")
#    else:
#         print("login band")
        
    #7-amaliyot    