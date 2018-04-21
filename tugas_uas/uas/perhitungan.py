def kalkulator():
    print "--"*10
    a = input("masukan nilai a:")
    b = input("\nmasukan nilai b:")
    print  "----------------------"
    print "\t1.perkalian  3.pertambahan "
    print "\n\t2.pembagian  4.pengurangan "
    pilih = input("pilih operasi = ")
    if pilih == 1:
        a=a*b
        print "\n\tsama dengan :" + str(a)
    elif pilih == 2:
        b=a/b
        print "\n\tsama dengan :" + str(b)
    elif pilih == 3:
        c=a+b
        print "\n\tsama dengan :" + str(c)
    elif pilih == 4:
        d=a-b
        print "\n\tsama dengan :" + str(d)
    else:
        print "salah input"
        tanya()
