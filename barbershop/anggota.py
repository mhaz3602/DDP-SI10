import streamlit as st
import pandas as pd

# Kelas untuk Anggota
class Anggota:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_info(self):
        return f"Anggota: {self.nama} | Email: {self.email} 📧"

# Riwayat anggota
riwayat_anggota = []

# Fungsi untuk sistem pendaftaran anggota
def sistem_anggota():
    st.title("Manajemen Keanggotaan 👥")

    # Formulir pendaftaran anggota
    nama = st.text_input("Nama Lengkap ✍️")
    email = st.text_input("Email 📧")

    if st.button("Daftar Member 📝"):
        if nama and email and email.endswith("@gmail.com"):  # Tambahan validasi email
            anggota_baru = Anggota(nama, email)
            riwayat_anggota.append({"Nama": nama, "Email": email})
            st.success(f"Selamat datang, {nama}! Anda telah terdaftar sebagai member. 🎉")
            st.write(anggota_baru.tampilkan_info())
            st.balloons()  # Efek visual saat berhasil mendaftar 🎈

            # Menampilkan reward untuk pendaftaran
            st.write("### Selamat! Anda Mendapatkan Reward 🏆:")
            st.write("- Diskon 25% untuk layanan pertama. ✂️")
            st.write("- Gratis layanan tambahan pijat kepala untuk kunjungan pertama. 💆‍♂️")

            # Menampilkan tabel riwayat anggota dengan nomor urut
            st.write("### Riwayat Anggota 📋")
            if riwayat_anggota:
                df = pd.DataFrame(riwayat_anggota)
                df.index = df.index + 1  # Menambahkan nomor urut mulai dari 1 🔢
                st.table(df)
        else:
            if not nama:
                st.error("Silakan isi nama dengan benar ❗️")
            elif not email:
                st.error("Silakan isi email dengan benar ❗️")
            elif not email.endswith("@gmail.com"):
                st.error("Format email harus diakhiri dengan '@gmail.com' ❗️")

# Menjalankan aplikasi
if __name__ == "__main__":
    sistem_anggota()