import random

secret = random.randint(1, 100)
javab = 0
hads = 0

print("به بازی حدس عدد خوش آمدید")
print("ما یه عدد در نظر گرفتیم، اون عدد از 1 تا 100 هست، و شما باید توی هشت حدس اون رو پیدا کنید")
print("~" * 30)

while javab != secret and hads < 8:
    javab = int(input("جواب رو حدس بزن:"))
    hads += 1
    
    if hads == 8 and javab != secret:
        print("به تعداد هشت حدس رسیدی و باختی")
    else:
        if javab < secret:
            print("برو بالاتر")
        elif javab > secret:
            print("برو پایین‌تر")
        else:
            print(f"افرین تو حدس {hads} موفق شدی")