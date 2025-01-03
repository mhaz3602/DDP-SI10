import streamlit as st
import pandas as pd
import re  # Untuk validasi email

if "anggota_terdaftar" not in st.session_state:
    st.session_state["anggota_terdaftar"] = []  

# Kelas untuk Anggota
class Anggota:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_info(self):
        return f"Anggota: {self.nama} | Email: {self.email} 📧"

# Fungsi untuk sistem pendaftaran anggota
def sistem_anggota():
    st.title("Manajemen Keanggotaan 👥")

    # Formulir pendaftaran anggota
    nama = st.text_input("Nama Lengkap ✍️")
    email = st.text_input("Email 📧")

    # Validasi email menggunakan regex
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if st.button("Daftar Member 📝"):
        if nama.strip() and email and re.match(email_regex, email):
            anggota_baru = Anggota(nama.strip(), email.strip())
            st.session_state.anggota_terdaftar.append({"Nama": nama.strip(), "Email": email.strip()})
            st.success(f"Selamat datang, {nama}! Anda telah terdaftar sebagai member. 🎉")
            st.write(anggota_baru.tampilkan_info())
            st.balloons()

            # Menampilkan reward untuk pendaftaran
            st.write("### Selamat! Anda Mendapatkan Reward 🏆:")
            st.write("- Diskon 25% untuk layanan pertama. ✂️")
            st.write("- Gratis layanan tambahan pijat kepala untuk kunjungan pertama. 💆‍♂️")

            # Menampilkan tabel riwayat anggota dengan nomor urut
            st.write("### Riwayat Anggota 📋")
            if st.session_state.anggota_terdaftar:
                df = pd.DataFrame(st.session_state.anggota_terdaftar)
                df.index = df.index + 1  # Menambahkan nomor urut mulai dari 1 🔢
                st.table(df)
        else:
            if not nama.strip():
                st.error("Silakan isi nama dengan benar ❗️")
            elif not email:
                st.error("Silakan isi email dengan benar ❗️")
            elif not re.match(email_regex, email):
                st.error("Format email tidak valid ❗️")

# Menjalankan aplikasi
if __name__ == "__main__":
    sistem_anggota()
