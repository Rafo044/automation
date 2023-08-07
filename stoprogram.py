#Program bəzən başlatdıqda döngüyə düşməməsi üçün alacağımız tədbirlərdən biridə onu vaxtla limitləməkdi.
#Aşaöıdakı funksiya programın işləmə vaxtını manual olaraq daxil etməyimiz üçündür.

def stop(func):
    def wrapper():
        import time
        basla = time.time() # baslama vaxti

        func()#Programın özü

        bitir = time.time() # baslama vaxti
        aradaki_vaxt = bitir-basla # aradaki vaxt


        if aradaki_vaxt > 60:
            print("Program 1 dəqiqədən artıq işlədi, dayandırılır ")
            exit()
        else :
            print("Program tamamlandı")
