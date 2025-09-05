import pandas as pd

# Data jadwal dosen + SKS + Semester
jadwal_dosen = [

    {"Hari": "Senin", "Dosen": "Nugraha, M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24F", "Mulai": "13.00", "Selesai": "16.30", "SKS": 4, "Semester": 1},
    {"Hari": "Senin", "Dosen": "Nugraha, M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24G", "Mulai": "08.00", "Selesai": "11.20", "SKS": 4, "Semester": 1},
    {"Hari": "Senin", "Dosen": "Ivana Lucia Kharisma, M.Kom", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24I", "Mulai": "13.00", "Selesai": "15.30", "SKS": 3, "Semester": 1},
    {"Hari": "Senin", "Dosen": "Lusiana Sani Parwati, M.Mat", "Mata Kuliah": "Kalkulus", "Kelas": "TI24I", "Mulai": "16.00", "Selesai": "18.30", "SKS": 3, "Semester": 1},
    {"Hari": "Senin", "Dosen": "Drs. Nuzwan Sudariana, MM", "Mata Kuliah": "Statistika dan Probabilitas", "Kelas": "TI24M", "Mulai": "13.00", "Selesai": "15.30", "SKS": 3, "Semester": 1},
    {"Hari": "Selasa", "Dosen": "M.Ikhsan Thohir, M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24I", "Mulai": "13.00", "Selesai": "16.20", "SKS": 4, "Semester": 1},
    {"Hari": "Selasa", "Dosen": "Hermanto, M.Kom", "Mata Kuliah": "Organisasi dan Arsitektur Komputer", "Kelas": "TI24M", "Mulai": "18.30", "Selesai": "19.30", "SKS": 2, "Semester": 1},
    {"Hari": "Rabu", "Dosen": "Hermanto, M.Kom", "Mata Kuliah": "Organisasi dan Arsitektur Komputer", "Kelas": "TI24M", "Mulai": "10.30", "Selesai": "12.10", "SKS": 2, "Semester": 1},
    {"Hari": "Rabu", "Dosen": "Ir. Kamdan, M.Kom", "Mata Kuliah": "Organisasi dan Arsitektur Komputer", "Kelas": "TI24A", "Mulai": "18.30", "Selesai": "20.00", "SKS": 2, "Semester": 1},
    {"Hari": "Rabu", "Dosen": "Gina Purnama Insany, S.Si.T, M.Kom", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24A", "Mulai": "16.00", "Selesai": "18.30", "SKS": 3, "Semester": 1},
    {"Hari": "Kamis", "Dosen": "Gina Purnama Insany, S.Si.T, M.Kom", "Mata Kuliah": "Statistika dan Probabilitas", "Kelas": "TI24H", "Mulai": "10.30", "Selesai": "13.00.30", "SKS": 3, "Semester": 1},
    {"Hari": "Kamis", "Dosen": "Zaenal Alamsyah, M.Kom", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24H", "Mulai": "13.00", "Selesai": "15.30", "SKS": 3, "Semester": 1},
    {"Hari": "Jumat", "Dosen": "Zaenal Alamsyah, M.Kom", "Mata Kuliah": "Logika Informatika", "Kelas": "TI24M", "Mulai": "18.30", "Selesai": "20.00", "SKS": 3, "Semester": 1},
    {"Hari": "Jumat", "Dosen": "Alun Sujjada, ST., M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24A", "Mulai": "08.00", "Selesai": "11.20", "SKS": 4, "Semester": 1},
    {"Hari": "Jumat", "Dosen": "Nugraha, M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24H", "Mulai": "08.00", "Selesai": "11.20", "SKS": 4, "Semester": 1},
    {"Hari": "Jumat", "Dosen": "M.Ikhsan Thohir, M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24I", "Mulai": "13.00", "Selesai": "16.20", "SKS": 4, "Semester": 1},
    {"Hari": "Jumat", "Dosen": "Shinta Ayuningtyas, M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24E", "Mulai": "08.00", "Selesai": "11.20", "SKS": 4, "Semester": 1},
    {"Hari": "Senin", "Dosen": "Dr. Nurkhan", "Mata Kuliah": "Metodologi Penelitian", "Kelas": "TI22E", "Mulai": "13.00", "Selesai": "14.30", "SKS": 3, "Semester": 6},
    {"Hari": "Senin", "Dosen": "Ivana Lucia Kharisma, M.Kom", "Mata Kuliah": "Interaksi Manusia dan Komputer", "Kelas": "TI23A", "Mulai": "16.00", "Selesai": "17.40", "SKS": 2, "Semester": 3},
    {"Hari": "Senin", "Dosen": "Ivana Lucia Kharisma, M.Kom", "Mata Kuliah": "Interaksi Manusia dan Komputer", "Kelas": "TI23I", "Mulai": "10.30", "Selesai": "12.0", "SKS": 2, "Semester": 3},
    {"Hari": "Selasa", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Sistem Paralel dan Terdistribusi", "Kelas": "TI23I", "Mulai": "13.00", "Selesai": "14.40", "SKS": 2, "Semester": 3},
    {"Hari": "Selasa", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23J", "Mulai": "16.00", "Selesai": "18.10", "SKS": 3, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Ivana Lucia Kharisma, M.Kom", "Mata Kuliah": "Interaksi Manusia dan Komputer", "Kelas": "TI23F", "Mulai": "13.00", "Selesai": "14.40", "SKS": 2, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Ivana Lucia Kharisma, M.Kom", "Mata Kuliah": "Interaksi Manusia dan Komputer", "Kelas": "TI23H", "Mulai": "16.00", "Selesai": "17.40", "SKS": 2, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Ir. Soemantri, ST.,M.Kom", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23T", "Mulai": "08.00", "Selesai": "11.20", "SKS": 4, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Ir. Soemantri, ST.,M.Kom", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23I", "Mulai": "13.00", "Selesai": "16.20", "SKS": 4, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Rekayasa Perangkat Lunak", "Kelas": "TI23M", "Mulai": "18.30", "Selesai": "20.00", "SKS": 3, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Basis Data", "Kelas": "TI22J", "Mulai": "08.30", "Selesai": "10.30", "SKS": 3, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Basis Data", "Kelas": "TI22T", "Mulai": "08.30", "Selesai": "15.30", "SKS": 3, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Alun Sujjada, ST., M.Kom", "Mata Kuliah": "Kompleksitas Algoritma", "Kelas": "TI23G", "Mulai": "10.30", "Selesai": "12.10", "SKS": 2, "Semester": 3},
    {"Hari": "Rabu", "Dosen": "Alun Sujjada, ST., M.Kom", "Mata Kuliah": "Kompleksitas Algoritma", "Kelas": "TI23J", "Mulai": "13.30", "Selesai": "14.40", "SKS": 2, "Semester": 3},
    {"Hari": "Kamis", "Dosen": "Alun Sujjada, ST., M.Kom", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23H", "Mulai": "08.00", "Selesai": "10.30", "SKS": 3, "Semester": 3},
    {"Hari": "Kamis", "Dosen": "Alun Sujjada, ST., M.Kom", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23T", "Mulai": "10.30", "Selesai": "13..00", "SKS": 3, "Semester": 3},
    {"Hari": "Jumat", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Sistem Paralel dan Terdistribusi", "Kelas": "TI23T", "Mulai": "16.30", "Selesai": "18.10", "SKS": 2, "Semester": 3},
    {"Hari": "Jumat", "Dosen": "Alun Sujjada, ST., M.Kom", "Mata Kuliah": "Pemrograman Berbasis Platform", "Kelas": "TI23I", "Mulai": "13.00", "Selesai": "15.30", "SKS": 3, "Semester": 3},
    {"Hari": "Jumat", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23F", "Mulai": "08.00", "Selesai": "11.20", "SKS": 4, "Semester": 3},
    {"Hari": "Jumat", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23E", "Mulai": "13.00", "Selesai": "16.20", "SKS": 4, "Semester": 3},
    {"Hari": "Selasa", "Dosen": "Adrian Reza, M.Kom", "Mata Kuliah": "Interaksi Manusia dan Komputer", "Kelas": "TI23E", "Mulai": "16.00", "Selesai": "17.40", "SKS": 2, "Semester": 5},
    {"Hari": "Selasa", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23J", "Mulai": "08.00", "Selesai": "11.20", "SKS": 3, "Semester": 5},
    {"Hari": "Jumat", "Dosen": "Alun Sujjada, ST., M.Kom", "Mata Kuliah": "Algoritma dan Struktur Data", "Kelas": "TI24A", "Mulai": "08.00", "Selesai": "11.20", "SKS": 3, "Semester": 2},
    {"Hari": "Jumat", "Dosen": "Anggun Fergina, M.Kom", "Mata Kuliah": "Jaringan Komputer dan Keamanan Informasi", "Kelas": "TI23E", "Mulai": "13.00", "Selesai": "16.20", "SKS": 3, "Semester": 5},
    {"Hari": "Rabu", "Dosen": "Dede Sukmawan, M.Kom", "Mata Kuliah": "Basis Data", "Kelas": "TI22A", "Mulai": "13.00", "Selesai": "15.30", "SKS": 3, "Semester": 4},
    {"Hari": "Sabtu", "Dosen": "Dr. Deni Hasman", "Mata Kuliah": "Etika Profesi", "Kelas": "TI22B", "Mulai": "Online", "Selesai": "Online", "SKS": 2, "Semester": 6},
    {"Hari": "Selasa", "Dosen": "Dr. Huang Gan", "Mata Kuliah": "Data Science", "Kelas": "TI22I", "Mulai": "10.30", "Selesai": "12.10", "SKS": 2, "Semester": 6},
    {"Hari": "Selasa", "Dosen": "Dr. Iwan Setiawan, S.T., M.T", "Mata Kuliah": "Metodologi Penelitian", "Kelas": "TI22H", "Mulai": "13.00", "Selesai": "15.30", "SKS": 3, "Semester": 6},
]

# Buat DataFrame
df = pd.DataFrame(jadwal_dosen)

# Urutkan berdasarkan Semester
df = df.sort_values(by="Semester").reset_index(drop=True)

# Tampilkan ke terminal
print("📘 JADWAL DOSEN TERURUT BERDASARKAN SEMESTER:\n")
for _, row in df.iterrows():
    print(f"Semester   : {row['Semester']}")
    print(f"Hari       : {row['Hari']}")
    print(f"Dosen      : {row['Dosen']}")
    print(f"Mata Kuliah: {row['Mata Kuliah']}")
    print(f"Kelas      : {row['Kelas']}")
    print(f"Mulai      : {row['Mulai']}")
    print(f"Selesai    : {row['Selesai']}")
    print(f"SKS        : {row['SKS']}")
    print("-" * 50)

# Simpan ke Excel
df.to_excel("jadwal_dosen_by_semester.xlsx", index=False)
print("\n✅ File Excel berhasil disimpan: jadwal_dosen_by_semester.xlsx")
