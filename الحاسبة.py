print("أهلًا بك في حاسبة أسهم أرامكو المجانية")
start = 'y'
while start == 'y':
        orginal_share = int(input("الرجاء إدخال اسهم الاكتتاب: "))
        if orginal_share < 10 :
            print("يجب أن تمتلك أكثر من 10 أسهم ")
        else:
            year = int(input("الرجاء إدخال عدد السنوات: "))
            additional_share = 2* year
            additional_share2 = int (orginal_share/10)
            total_share= additional_share * additional_share2
            if total_share <= 100:
                your_share = orginal_share + total_share
                print( " عدد أسهمك سيكون "+ str(your_share) + " سهم ")
            elif total_share > 100:
                your_share = orginal_share + 100
                print( " لا يمكن أن يتجاوز عدد الأسهم الإضافية أكثر من 100 سهم . عدد أسهمك سيكون "  +  str(your_share)  +  " سهم " )
            else :
                print("ERORR")
        start = input(("هل تريد أن تحسب الأسهم المجانية مرة أخرى؟  y/n:"))
        print('شكرًا لاستخدام حاسبة أسهم الأسهم المجانية لأرامكو')