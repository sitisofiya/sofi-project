def gaji() :
    
    from texttable import Texttable
    
    table = Texttable ()
    jawab = "ya"
    no = 0
    nama = []
    jabatan = []
    gaji = []
    

    while (jawab == 'ya'):
        nama.append(input("\n masukkan nama : "))
        jab = input("\n jabatan : ")
        jabatan.append(jab)

        if (jab == 'Programmer'):
            (jabatan == 'Programmer')
            gaji.append(7000000)
            jawab = input("\n tambah lagi? ")
            no+=1
            
        elif (jab == 'Direktur'):
            (jabatan == 'Direktur')
            gaji.append(10000000)
            jawab = input("\n tambah lagi? ")
            no+=1

        elif (jab == 'Operator'):
            (jabatan == 'Operator')
            gaji.append(4000000)
            jawab = input("\n tambah lagi? ")
            no+=1

        else:
            break

    for i in range (no):
            
        table.add_rows([['No','Nama','Jabatan','Gaji'],[i+1,nama[i],jabatan[i],gaji[i]]])


    print (table.draw())

