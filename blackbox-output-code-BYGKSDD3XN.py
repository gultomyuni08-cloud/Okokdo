import time

# --- DATABASE PENYAKIT ---
# Anda bisa menambahkan penyakit lain ke dalam daftar ini
data_penyakit = [
    {
        "id": 1,
        "nama": "Flu (Common Cold)",
        "gejala": ["batuk", "pilek", "hidung tersumbat", "bersin", "demam ringan", "sakit tenggorokan"],
        "penyebab": "Virus Rhinovirus",
        "obat": "Paracetamol (untuk demam), Istirahat yang cukup, Minum air putih hangat, Vitamin C",
        "sumber": "WHO - Common Cold"
    },
    {
        "id": 2,
        "nama": "Demam Berdarah Dengue (DBD)",
        "gejala": ["demam tinggi", "sakit kepala", "nyeri otot", "mual", "muntah", "bintik merah"],
        "penyebab": "Virus Dengue (Ditularkan oleh nyamuk Aedes Aegypti)",
        "obat": "Paracetamol (JANGAN IBUPROFEN/ASPIRIN), Minum air putih banyak, Istirahat total",
        "sumber": "CDC / Kemenkes RI"
    },
    {
        "id": 3,
        "nama": "Mag (Gastritis)",
        "gejala": ["mual", "muntah", "sakit perut", "perut kembung", "panas dada"],
        "penyebab": "Bakteri H. Pylori, Stress, Makanan pedas/asam",
        "obat": "Antasida, Proton Pump Inhibitor (Omeprazole), Hindari makanan pedas",
        "sumber": "Alodokter / Halodoc"
    },
    {
        "id": 4,
        "nama": "Malaria",
        "gejala": ["demam tinggi", "menggigil", "keringat dingin", "sakit kepala", "mual"],
        "penyebab": "Parasit Plasmodium (Ditularkan oleh nyamuk Anopheles)",
        "obat": "Obat Antimalaria (Kloroquin, Artemisinin) - HARUS RESEP DOKTER",
        "sumber": "WHO - Malaria"
    },
    {
        "id": 5,
        "nama": "Migraine (Sakit Kepala Sebelah)",
        "gejala": ["sakit kepala", "mual", "peka terhadap cahaya", "pusing berputar"],
        "penyebab": "Genetik, Stress, Perubahan hormon, Kurang tidur",
        "obat": "Ibuprofen, Paracetamol, obat khusus migraine (Simptom)",
        "sumber": "Mayo Clinic"
    },
    {
        "id": 6,
        "nama": "Diare",
        "gejala": ["feses encer", "sakit perut", "mual", "muntah", "dehidrasi"],
        "penyebab": "Bakteri, Virus, Keracunan makanan",
        "obat": "Oralit (untuk mengganti cairan tubuh), Loperamide (untuk menghentikan diare sementara)",
        "sumber": "Kemkes RI"
    }
]

# --- FUNGSI UTAMA ---

def normalisasi_teks(teks):
    """Mengubah teks menjadi lowercase dan menghapus spasi berlebih"""
    return [kata.strip().lower() for kata in teks.split(',')]

def cek_kecocokan(gejala_user, penyakit):
    """Menghitung berapa banyak gejala user yang cocok dengan database"""
    list_gejala_penyakit = [g.lower() for g in penyakit['gejala']]
    cocok = 0
    for g in gejala_user:
        if g in list_gejala_penyakit:
            cocok += 1
    return cocok

def main():
    print("=" * 60)
    print("   SISTEM PENDETEKSI PENYAKIT SEDERHANA")
    print("=" * 60)
    print("CATATAN: Ini BUKAN diagnosis medis resmi. Konsultasi dengan dokter.")
    print("-" * 60)
    
    # Input dari user
    print("\nMasukkan gejala Anda dipisahkan dengan koma (,).")
    print("Contoh: sakit kepala, pusing berputar, mual")
    input_user = input("Gejala Anda: ")
    
    if not input_user.strip():
        print("Anda tidak memasukkan gejala.")
        return

    # Proses data
    gejala_list = normalisasi_teks(input_user)
    print("\nMemproses", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

    # Analisis
    hasil_analisa = []
    for penyakit in data_penyakit:
        skor_kecocokan = cek_kecocokan(gejala_list, penyakit)
        if skor_kecocokan > 0:
            # Simpan hasil dan hitung persentase kecocokan
            total_gejala_penyakit = len(penyakit['gejala'])
            persentase = (skor_kecocokan / total_gejala_penyakit) * 100
            hasil_analisa.append({
                "nama": penyakit['nama'],
                "skor": skor_kecocokan,
                "persentase": persentase,
                "data": penyakit
            })

    # Urutkan berdasarkan kecocokan tertinggi
    hasil_analisa.sort(key=lambda x: x['skor'], reverse=True)

    # Tampilkan Hasil
    if not hasil_analisa:
        print("❌ Maaf, gejala yang Anda masukkan tidak cocok dengan database kami.")
        print("Saran: Segera pergi ke dokter jika kondisi darurat.")
    else:
        print(f"Berikut adalah kemungkinan penyakit berdasarkan gejala ({input_user}):\n")
        for i, item in enumerate(hasil_analisa[:3]): # Tampilkan top 3
            data = item['data']
            print(f"--- Kemungkinan #{i+1}: {data['nama']} ---")
            print(f"   Tingkat Kecocokan: {item['persentase']:.1f}%")
            print(f"   Gejala yang Cocok: {item['skor']} dari {len(data['gejala'])} gejala umum ({data['gejala']})")
            print(f"   Penyebab: {data['penyebab']}")
            print(f"   Saran Obat/Action: {data['obat']}")
            print(f"   Sumber Info: {data['sumber']}")
            print("-" * 40)

if __name__ == "__main__":
    main()