import pandas as pd

# Data jadwal dosen + SKS + Semester
jadwal_dosen =  [
    {"Hari": "Senin", "Mata Kuliah": "Statistika dan Probalitas", "Kelas": "TI24A", "Ruang": "B4A", "Mulai": "10.30", "Selesai": "13.00", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Kalkulus", "Kelas": "TI24E", "Ruang": "B4B", "Mulai": "10.30", "Selesai": "13.00", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24I", "Ruang": "B4C", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT":"1", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Algoritma Dan Struktur Data", "Kelas": "TI24F", "Ruang": "B4D", "Mulai": "13.00", "Selesai": "16.20", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Interaksi Manusia Dan Komputer", "Kelas": "TI23A", "Ruang": "B4E", "Mulai": "16.00", "Selesai": "17.40", "SKS": "5", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Kalkulus", "Kelas": "TI24I", "Ruang": "B4F", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23I", "Ruang": "B4G", "Mulai": "16.00", "Selesai": "18.00", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Metodelogi Penelitian", "Kelas": "TI22E", "Ruang": "B4H", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Senin", "Mata Kuliah": "Statistika Dan Probalitas", "Kelas": "TI24M", "Ruang": "B4A", "Mulai": "18.30", "Selesai": "20.00", "SKS": "2", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Metode Numerik", "Kelas": "TI23H", "Ruang": "B4B", "Mulai": "18.00", "Selesai": "10.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23J", "Ruang": "B4C", "Mulai": "08.00", "Selesai": "11.20", "SKS": "3", "SMT": "2", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Data Science", "Kelas": "TI22I", "Ruang": "B4D", "Mulai": "10.30", "Selesai": "12.10", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Sistem Paralel dan Terdistribusi", "Kelas": "TI23I", "Ruang": "B4E", "Mulai": "13.00", "Selesai": "14.40", "SKS": "3", "SMT": "2", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23A", "Ruang": "B4F", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Deep Learning", "Kelas": "TI22I", "Ruang": "B4G", "Mulai": "13.00", "Selesai": "14.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23E", "Ruang": "B4H", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23J", "Ruang": "B4A", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Interaksi Manusia dan Komputer", "Kelas": "TI23E", "Ruang": "B4B", "Mulai": "16.00", "Selesai": "17.40", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Pengolahan Citra Digital", "Kelas": "TI22I", "Ruang": "B4C", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Pengolahan Perangkat Lunak", "Kelas": "TI22F", "Ruang": "B4D", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Basis Data", "Kelas": "TI22E", "Ruang": "B4E", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Metodelogi Penelitian", "Kelas": "TI22A", "Ruang": "B4F", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Organisasi dan arsitektur Komputer", "Kelas": "TI24M", "Ruang": "B4G", "Mulai": "18.30", "Selesai": "19.30", "SKS": "1", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Selasa", "Mata Kuliah": "Projek Perangkat Lunak", "Kelas": "TI22M", "Ruang": "B4H", "Mulai": "20.00", "Selesai": "21.30", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Basis Data", "Kelas": "TI22J", "Ruang": "B4A", "Mulai": "08.00", "Selesai": "10.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23T", "Ruang": "B4B", "Mulai": "08.00", "Selesai": "11.20", "SKS": "4", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Deep Learning", "Kelas": "TI22A", "Ruang": "B4C", "Mulai": "08.00", "Selesai": "09.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23A", "Ruang": "B4D", "Mulai": "08.00", "Selesai": "10.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Kompleksitas Algoritma", "Kelas": "TI23G", "Ruang": "B4E", "Mulai": "10.30", "Selesai": "12.10", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Metode Numerik", "Kelas": "TI23E", "Ruang": "B4F", "Mulai": "10.30", "Selesai": "13.00", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Organisasi dan arsitektur Komputer", "Kelas": "TI24A", "Ruang": "B4G", "Mulai": "13.00", "Selesai": "14.40", "SKS": "2", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Kalkulus", "Kelas": "TI24H", "Ruang": "B4H", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Sistem Paralel dan Terdistribusi", "Kelas": "TI23A", "Ruang": "B4A", "Mulai": "13.00", "Selesai": "14.40", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Pemrograman Berbasis Mobile", "Kelas": "TI22F", "Ruang": "B4B", "Mulai": "13.00", "Selesai": "14.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Kompleksitas Algoritma", "Kelas": "TI23E", "Ruang": "B4C", "Mulai": "13.00", "Selesai": "14.40", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23G", "Ruang": "B4D", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Etika Profesi", "Kelas": "TI22E", "Ruang": "B4E", "Mulai": "13.00", "Selesai": "14.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Basis Data", "Kelas": "TI22A", "Ruang": "B4F", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Pemrograman Berbasis Web", "Kelas": "TI22F", "Ruang": "B4G", "Mulai": "16.00", "Selesai": "17.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24A", "Ruang": "B4H", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Rabu", "Mata Kuliah": "Sistem Informasi Geografis", "Kelas": "TI22M", "Ruang": "B4A", "Mulai": "18.30", "Selesai": "19.30", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23H", "Ruang": "B4B", "Mulai": "08.00", "Selesai": "10.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Data Science", "Kelas": "TI22A", "Ruang": "B4C", "Mulai": "08.00", "Selesai": "09.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Statistika dan Probabilitas", "Kelas": "TI24H", "Ruang": "B4D", "Mulai": "10.30", "Selesai": "13.00", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Computer Vision", "Kelas": "TI22A", "Ruang": "B4E", "Mulai": "10.30", "Selesai": "12.10", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Kompleksitas Algoritma", "Kelas": "TI23A", "Ruang": "B4F", "Mulai": "10.30", "Selesai": "12.10", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Projek Perangkat Lunak", "Kelas": "TI22A", "Ruang": "B4G", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24H", "Ruang": "B4H", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Pengolahan Citra Digital", "Kelas": "TI22F", "Ruang": "B4A", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Projek Perangkat Lunak", "Kelas": "TI22J", "Ruang": "B4B", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Pengolahan Citra Digital", "Kelas": "TI22A", "Ruang": "B4C", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23F", "Ruang": "B4D", "Mulai": "16.00", "Selesai": "18.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23M", "Ruang": "B4E", "Mulai": "18.30", "Selesai": "20.30", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Kamis", "Mata Kuliah": "Pemrograman Berbasis Web", "Kelas": "TI22M", "Ruang": "B4F", "Mulai": "19.00", "Selesai": "20.00", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24A", "Ruang": "B4G", "Mulai": "08.00", "Selesai": "11.20", "SKS": "4", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24E", "Ruang": "B4H", "Mulai": "08.00", "Selesai": "11.20", "SKS": "4", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23A", "Ruang": "B4A", "Mulai": "08.00", "Selesai": "11.20", "SKS": "4", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23E", "Ruang": "B4B", "Mulai": "13.00", "Selesai": "16.20", "SKS": "4", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23J", "Ruang": "B4C", "Mulai": "13.00", "Selesai": "15.30", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24I", "Ruang": "B4D", "Mulai": "13.00", "Selesai": "16.20", "SKS": "4", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Big Data Architecture and Infrastructure", "Kelas": "TI22T", "Ruang": "B4E", "Mulai": "13.00", "Selesai": "14.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Etika Profesi", "Kelas": "TI22I", "Ruang": "B4F", "Mulai": "16.00", "Selesai": "17.40", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Jumat", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24M", "Ruang": "B4G", "Mulai": "18.30", "Selesai": "20.00", "SKS": "2", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23B", "Ruang": "B4H", "Mulai": "13.00", "Selesai": "14.30", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Basis Data", "Kelas": "TI22B", "Ruang": "B4A", "Mulai": "13.00", "Selesai": "14.30", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23B", "Ruang": "B4B", "Mulai": "14.30", "Selesai": "16.30", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Teknologi Blockchain", "Kelas": "TI22B", "Ruang": "B4C", "Mulai": "14.30", "Selesai": "15.30", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Cyber Security", "Kelas": "TI22B", "Ruang": "B4D", "Mulai": "16.00", "Selesai": "17.00", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Big Data Arsitektur dan Infrastruktur", "Kelas": "TI22B", "Ruang": "B4E", "Mulai": "17.00", "Selesai": "18.00", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Metode Numerik", "Kelas": "TI23B", "Ruang": "B4F", "Mulai": "17.00", "Selesai": "18.30", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Organisasi dan Arsitektur Komputer", "Kelas": "TI24B", "Ruang": "B4G", "Mulai": "17.00", "Selesai": "18.00", "SKS": "1", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Pengolahan Citra Digital", "Kelas": "TI22B", "Ruang": "B4H", "Mulai": "18.30", "Selesai": "20.00", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Kalkulus", "Kelas": "TI24B", "Ruang": "B4A", "Mulai": "19.00", "Selesai": "20.30", "SKS": "2", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23B", "Ruang": "B4B", "Mulai": "19.00", "Selesai": "20.30", "SKS": "2", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Metodologi Penelitian", "Kelas": "TI22B", "Ruang": "B4C", "Mulai": "online", "Selesai": "", "SKS": "3", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Interaksi manusia dan Komputer", "Kelas": "TI23B", "Ruang": "B4D", "Mulai": "online", "Selesai": "", "SKS": "3", "SMT": "3", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Kompleksitas Algoritma", "Kelas": "TI23B", "Ruang": "B4E", "Mulai": "online", "Selesai": "", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Sabtu", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24B", "Ruang": "B4F", "Mulai": "online", "Selesai": "", "SKS": "3", "SMT": "1", "Prodi": "TI"},
    {"Hari": "Minggu", "Mata Kuliah": "Deep Learning", "Kelas": "TI22C", "Ruang": "B4G", "Mulai": "13.00", "Selesai": "14.00", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Minggu", "Mata Kuliah": "Metodologi Penelitian", "Kelas": "TI22C", "Ruang": "B4H", "Mulai": "14.00", "Selesai": "15.30", "SKS": "2", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Minggu", "Mata Kuliah": "Computer Vision", "Kelas": "TI22C", "Ruang": "B4A", "Mulai": "16.00", "Selesai": "17.00", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Minggu", "Mata Kuliah": "Etika Profesi", "Kelas": "TI22C", "Ruang": "B4B", "Mulai": "17.00", "Selesai": "18.00", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Minggu", "Mata Kuliah": "Project Perangkat Lunak", "Kelas": "TI22C", "Ruang": "B4C", "Mulai": "17.00", "Selesai": "18.00", "SKS": "1", "SMT": "5", "Prodi": "TI"},
    {"Hari": "Minggu", "Mata Kuliah": "Etika Profesi", "Kelas": "TI22B", "Ruang": "B4D", "Mulai": "online", "Selesai": "", "SKS": "3", "SMT": "5", "Prodi": "TI"}

    
]

# Buat DataFrame
df = pd.DataFrame(jadwal_dosen)

# Urutkan berdasarkan Semester
df = df.sort_values(by="SMT").reset_index(drop=True)

# Tampilkan ke terminal
print("📘 JADWAL DOSEN TERURUT BERDASARKAN SEMESTER:\n")
for _, row in df.iterrows():
    print(f"Hari       : {row['Hari']}")
    print(f"Mata Kuliah: {row['Mata Kuliah']}")
    print(f"Kelas      : {row['Kelas']}")
    print(f"Ruang      : {row['Ruang']}")
    print(f"Mulai      : {row['Mulai']}")
    print(f"Selesai    : {row['Selesai']}")
    print(f"SKS        : {row['SKS']}")
    print(f"SMT        : {row['SMT']}")
    print(f"Prodi      : {row['Prodi']}")
    print(f"SKS        : {row['SKS']}")
    print("-" * 50)

# Simpan ke Excel
df.to_excel("jadwal_dosen_by_semester.xlsx", index=False)
print("\n✅ File Excel berhasil disimpan: jadwal_dosen_by_semester.xlsx")
