def pembayaran () :
    print("\n\tPROGRAM PEMBAYARAN MAHASISWA ")
    print("\n\tKAMPUS PELITA BANGSA ")

   
    print("\nPilihan Pembayaran Mahasiswa : ")
    print("\n1. Pembayaran UTS per Mata Kuliah ")
    print("\n2. Pembayaran UAS per Mata Kuliah ")

    pilihan =input("\nSilahkan pilih pembayaran Anda : ")
    
    if   pilihan == '1' :
        uts() 
    elif pilihan == '2' :
        uas()
    else :
        akhir()

def uts():
    from texttable import Texttable
    table = Texttable()
    jawab = "y"
    no = 0
    nama =[]
    nim = []
    kelas = []
    jum_matkul_uts_bayar = []
    bulan_bayar = []
    seminar_bayar = []
    kas_bayar = []
    
    while(jawab == "y") :
        nama.append(input(" \nNama   : "))
        nim.append(input(" \nNIM     : "))
        kelas.append(input("\nKelas : "))
        jum_matkul_uts_bayar.append(input(" \nJumlah Mata Kuliah yang di bayar : "))
        bulan_bayar.append(input(" \nJumlah Bulanan yang di bayar : "))
        pilih = input(" \nBayar Uang Kas atau tidak ( y / t ) ? : ")
        if pilih == "y" :
            kas_bayar = 20000
        else :
            kas_bayar = 0
        pil = input(" \nBayar Uang Seminar atau tidak ( y / t ) ? : ")
        if pil == "y" :
            seminar_bayar = 100000
        else :
            seminar_bayar = 0
        jawab = input("\n\tIngin Bayar Lagi (y/t) ? ")
        no += 1
    for i in range (no):
        bayar_uts = int(jum_matkul_uts_bayar[i])*50000
        bayar_spp = int(bulan_bayar[i])*500000
        admin = int(5000)
        akhir = bayar_uts + bayar_spp + seminar_bayar + kas_bayar + admin
        table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
        table.set_cols_align(['i','c','c','c','c','c','c','c','c','c'])
        table.set_cols_width([10,10,10,10,10,10,10,10,10,10])
        table.add_rows([['No','NAMA',' NIM ','KELAS','BIAYA UTS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uts,bayar_spp,seminar_bayar,kas_bayar,admin,akhir]])
    print (table.draw())
    tanya()
      
            
 
def uas():
    from texttable import Texttable
    table = Texttable()
    jawab = "y"
    no = 0
    nama =[]
    nim = []
    kelas = []
    jum_matkul_uas_bayar = []
    bulan_bayar = []
    bayar_seminar = []
    kas_bayar = []
        
    while(jawab == "y") :
        nama.append(input(" \nNama   : "))
        nim.append(input(" \nNIM     : "))
        kelas.append(input("\nKelas : "))
        jum_matkul_uas_bayar.append(input(" \nJumlah Mata Kuliah yang di bayar : "))
        bulan_bayar.append(input(" \nJumlah Bulanan yang di bayar : "))
        pilih = input(" \nBayar Uang Kas atau tidak ( y / t ) ? : ")
        if pilih == "y" :
            kas_bayar = 20000
            
        else :
            kas_bayar = 0
        pil = input(" \nBayar Uang Seminar atau tidak ( y / t ) ? : ")
        if pil == "y" :
            bayar_seminar = 100000
            
        else :
            bayar_seminar = 0

        jawab = input("\n\tIngin Bayar Lagi (y/t) ? ")
        no += 1
    for i in range (no):
        bayar_uas = int(jum_matkul_uas_bayar[i])*50000
        bayar_spp = int(bulan_bayar[i])*500000
        admin = int("5000")
        akhir = bayar_uas + bayar_spp + bayar_seminar + kas_bayar + admin
        table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
        table.set_cols_align(['i','c','c','c','c','c','c','c','c','c'])
        table.set_cols_width([10,10,10,10,10,10,10,10,10,10])
        table.add_rows([['No','NAMA','NIM','KELAS','BIAYA UAS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uas,bayar_spp,bayar_seminar,kas_bayar,admin,akhir]])
    print(table.draw())
    tanya()


def tanya():
     pil = input("\nApakah Anda ingin mengulang ( y / t ) ? ")
     if pil == 'y' :
        pembayaran ()
     else :
        print(" TERIMA KASIH TELAH MELAKUKAN TRANSAKSI PEMBAYARAN")
       


    
