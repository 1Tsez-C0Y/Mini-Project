import random
k = []
for i in range(1, 31):
    k.append([i, "Kosong", "-", "-", 0])

for r in random.sample(k, 15):
    r[1], r[2] = "Terisi", random.choice(["Budi", "Siti", "Dewi", "Asep"])
    r[3], r[4] = random.choice(["Wedding", "Rapat", "Diklat", "Seminar"]), random.choice([500000, 1000000, 2500000])

while True:
    print("\n === SISTEM RESERVASI GEDUNG SERBAGUNA ===") 
    p = input("\n1. Masuk\n2. Keluar\nPilih (1-2): ")
    if p == "2": 
        break
    if p != "1": 
        continue

    while True:
        print("\n === KALENDER BULAN ===")
        for r in k:
            t = str(r[0])
            if r[0] < 10: 
                t = t + " " 
            
            if r[1] == "Terisi":
                if r[4] >= 2500000:
                    bayar = "Lunas"
                else:
                    nom_fmt = "{:,}".format(r[4]).replace(",", ".")
                    bayar = "DP: Rp" + nom_fmt
                print("Tgl " + t + " | Terisi | " + r[3] + " (" + bayar + ")")
            else:
                print("Tgl " + t + " | Kosong")
        
        
        m = input("\n1.Booking 2.Batal Reservasi 3.Ganti Tgl 4.Keluar\nPilih: ")
        if m == "4": 
            break
        
        # validasi tanggal
        while True:
            tgl = input("Masukkan Tanggal (1-30): ")
            if tgl.isdigit() and 1 <= int(tgl) <= 30:
                rp = k[int(tgl) - 1]
                break
            print("Error: Tanggal tidak valid!")
        
        # 1. booking
        if m == "1":
            if rp[1] == "Terisi":
                print("Maaf, sudah terisi!")
                continue
            
            n = input("Nama (Untuk Verifikasi): ")
            a = input("Acara: ")
            
            while True:
                d_in = input("Nominal (Min Rp500.000): ").replace(".", "")
                if d_in.isdigit() and int(d_in) >= 500000:
                    d = int(d_in)
                    break
                print("Nominal tidak valid!")
            
            rp[1], rp[2], rp[3], rp[4] = "Terisi", n, a, d
            
            if d >= 2500000:
                kembali = d - 2500000
                if kembali > 0:
                    kmb = "{:,}".format(kembali).replace(",", ".")
                    print("Booking LUNAS! Kembalian: Rp" + kmb)
                else:
                    print("Booking LUNAS!")
            else:
                print("Booking Berhasil (DP)!")
                
        # 2. batlkan reservasi & 3. ganti tanggal
        elif (m == "2" or m == "3") and rp[1] == "Terisi":
            verif = input("Verifikasi Nama: ")
            if verif != rp[2]:
                print("Nama salah! Akses ditolak.")
                continue
            
            if m == "2":
                rp[1], rp[2], rp[3], rp[4] = "Kosong", "-", "-", 0
                print("Reservasi Dibatalkan.")
                
            elif m == "3":
                while True:
                    t2 = input("Tanggal Tujuan Baru: ")
                    if t2.isdigit() and 1 <= int(t2) <= 30:
                        r2 = k[int(t2) - 1]
                        break
                    print("Tidak valid!")
                        
                if r2[1] == "Kosong":
                    r2[1], r2[2], r2[3], r2[4] = rp[1], rp[2], rp[3], rp[4]
                    rp[1], rp[2], rp[3], rp[4] = "Kosong", "-", "-", 0
                    print("Berhasil pindah tanggal!")
                else:
                    print("Gagal: Tanggal tujuan terisi!")
                    
        elif rp[1] == "Kosong" and m != "1":
            print("Tanggal kosong. Tidak ada data untuk diubah.")