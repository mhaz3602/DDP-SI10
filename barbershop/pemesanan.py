import streamlit as st
import pandas as pd  


# Kelas untuk Barber
class Barber:
    def __init__(self, nama, bio, gambar):
        self.nama = nama
        self.bio = bio
        self.gambar = gambar

    def tampilkan_bio(self):
        return f"👤 Biodata Barber {self.nama}:  {self.bio} "


# Kelas untuk Layanan
class Layanan:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


# Data Barber
barbers = [
    Barber(
        "Ali",
        """
        **Nama Lengkap**: Muhammad Hudzaifah Ali Al-Mubarok  
        **Spesialisasi**: Profesional dalam berbagai ✔️ model rambut, termasuk gaya klasik dan modern.  
        **Pengalaman**: Lebih dari 10 tahun dalam industri tata rambut. ✂️  
        **Kelebihan**: Ahli dalam teknik fade, quiff, dan pompadour dengan hasil presisi tinggi. 👌  
        """,
        "https://png.pngtree.com/element_origin_min_pic/16/09/01/1357c7bcd874384.jpg",
    ),
    Barber(
        "Denovri",
        """
        **Nama Lengkap**: Denovri Syachriaziiz Pribadi 🌟  
        **Spesialisasi**: Gaya rambut pria modern seperti undercut, crew cut, dan high fade. ✔️✂️  
        **Pengalaman**: 8 tahun menjadi barber profesional. 👨‍🎤  
        **Kelebihan**: Kreatif dalam menciptakan tampilan baru dan memiliki kemampuan personalisasi gaya rambut sesuai tren terkini. 💡  
        """,
        "https://png.pngtree.com/png-clipart/20230920/original/pngtree-vintage-hair-salon-vector-art-featuring-a-barbers-profile-vector-png-image_12452065.png",
    ),
    Barber(
        "Ghina",
        """
        **Nama Lengkap**: Fairuz Ghina Mufidah 🎨  
        **Spesialisasi**: Styling rambut wanita untuk acara formal, kasual, dan pernikahan. 💇‍♀️  
        **Pengalaman**: 6 tahun dalam styling dan pewarnaan rambut wanita. 🌺  
        **Kelebihan**: Mahir dalam menciptakan gaya rambut elegan, termasuk updos, soft curls, dan pewarnaan ombre. 😍  
        """,
        "https://t3.ftcdn.net/jpg/02/73/71/72/360_F_273717249_jfDMOyyfmE9I7syV8gOrk8gCgnqldptC.jpg",
    ),
    Barber(
        "Rara",
        """
        **Nama Lengkap**: Yumna Dzakirah 🌼  
        **Spesialisasi**: Potongan rambut unisex dan perawatan rambut anak-anak. ✂️👶  
        **Pengalaman**: 7 tahun sebagai barber handal di berbagai salon ternama. ✨  
        **Kelebihan**: Berpengalaman dalam memberikan potongan rambut yang nyaman dan stylish untuk segala usia. 💇‍♂️💇‍♀️  
        """,
        "https://t4.ftcdn.net/jpg/00/87/47/03/360_F_87470394_WgPDDqza9QiHdEYAjuYTEI6938iljTo5.jpg",
    ),
]

# Fungsi untuk menampilkan sistem pemesanan
def pemesanan_online():
    st.title("Pemesanan Online 📅")

    # Input data pelanggan
    nama = st.text_input("Nama ✍️")
    umur = st.number_input("Umur 🎂", min_value=0)
    jenis_kelamin = st.selectbox("Jenis Kelamin 👨‍👩‍👧‍👦", ["Laki-laki", "Perempuan"])

    # Pilihan barber
    barber = st.selectbox("Pilih Barber ✂️", [barber.nama for barber in barbers])
    selected_barber = next(b for b in barbers if b.nama == barber)

    # Menampilkan biodata barber yang dipilih
    st.image(selected_barber.gambar, width=200)
    st.write(selected_barber.tampilkan_bio())

    # Pilihan Model Rambut
    model_rambut = st.selectbox(
        "Pilih Model Rambut 💇‍♂️",
        [
            "Undercut",
            "Quiff",
            "Pompadour",
            "High Fade",
            "Faux Hawk",
            "Crew Cut",
            "Side Part",
            "Textured Crop",
            "Fringe",
            "Slick Back",
            "Angular Fringe",
            "Layered",
            "Bob",
            "Pixie",
            "Long Layers",
            "Shaggy Bob",
            "Bangs",
            "Soft Layers",
            "Wavy Bob",
            "Chin-Length Bob",
            "Wispy Bangs",
        ],
    )

    # Warna rambut (opsional) dan gradasi warna rambut
    warna_rambut = st.selectbox(
        "Pilih Warna Rambut 🎨",
        [" ", "Hitam", "Coklat", "Blonde", "Merah", "Abu-abu", "Putih", "Lainnya"],
    )
    gradasi_warna = st.selectbox(
        "Pilih Gradasi Warna (Opsional) 🌈",
        ["Tanpa Gradasi", "Gradasi Gelap ke Terang", "Gradasi Terang ke Gelap", "Gradasi Warna Lain"],
    )

    # Harga berdasarkan umur
    harga_potong = 25000 if umur < 17 else 35000

    # Pilihan layanan tambahan
    layanan_items = [
        Layanan("Cukur Rambut", 10000),
        Layanan("Cukur Jenggot", 10000),
        Layanan("Keramas", 25000),
        Layanan("Styling Rambut", 70000),
        Layanan("Pewarnaan Rambut", 100000),
        Layanan("Perawatan Rambut", 50000),
        Layanan("Manikur", 30000),
        Layanan("Pedikur", 35000),
        Layanan("Facial", 75000),
        Layanan("Pijat Kepala", 10000),
        Layanan("Waxing", 50000),
    ]

    layanan = st.multiselect("Pilih Layanan Tambahan 🛠️", [layanan.nama for layanan in layanan_items])
    total_harga = harga_potong

    layanan_rincian = []
    for layanan_item in layanan_items:
        if layanan_item.nama in layanan:
            total_harga += layanan_item.harga
            layanan_rincian.append(f"{layanan_item.nama}: Rp {layanan_item.harga}")

    # Pilihan tempat pemotongan
    tempat_potong = st.selectbox("Pilih Tempat Potong Rambut 🏠", ["Barbershop", "Di Rumah"])

    # Request lagu (opsional) 
    lagu_request = st.text_input("Request Lagu (Opsional) 🎵 untuk di putar saat proses pelayanan")

    # Pilihan pembayaran
    metode_pembayaran = st.selectbox(
        "Pilih Metode Pembayaran 💰", ["GoPay", "Transfer Bank BNI", "BCA", "Mandiri", "Bayar di Tempat"]
    )

    # Tanggal dan waktu pemesanan
    tanggal = st.date_input("Pilih Tanggal Pemesanan 📅")
    waktu = st.time_input("Pilih Waktu Pemesanan ⏰")
    
        # Proses pembayaran
    if metode_pembayaran == "GoPay":
        st.info("Silakan scan QR Code berikut untuk melakukan pembayaran menggunakan GoPay.")
        st.image("https://member.hostingceria.com/gambar/gopay-qrcode.jpg")  # Ganti dengan QR Code asli
    elif metode_pembayaran == "Transfer Bank BNI":
        st.info("Silakan transfer ke rekening BNI: 123456789 atas nama BarberShop.")
    elif metode_pembayaran == "BCA":
        st.info("Silakan transfer ke rekening BCA: 987654321 atas nama BarberShop.")
    elif metode_pembayaran == "Mandiri":
        st.info("Silakan transfer ke rekening Mandiri: 123123123 atas nama BarberShop.")
    elif metode_pembayaran == "Bayar di Tempat":
        st.info("Pembayaran akan dilakukan di tempat sesuai total yang telah dihitung.")

    # Menampilkan total harga
    st.write("Rincian Harga 💵:")
    st.write(f"Potong Rambut: Rp {harga_potong}")
    for rincian in layanan_rincian:
        st.write(rincian)
    st.write(f"Total Harga: Rp {total_harga}")

    # Menyimpan riwayat pemesanan
    if "riwayat_pemesanan" not in st.session_state:
        st.session_state.riwayat_pemesanan = []

    if st.button("Pesan Sekarang ✔️"):
        pemesanan_baru = {
            "Nama": nama,
            "Barber": barber,
            "Tanggal": str(tanggal),
            "Waktu": str(waktu),
            "Total Harga": total_harga,
            "Metode Pembayaran": metode_pembayaran,
            "Tempat Potong": tempat_potong,
            "Warna Rambut": warna_rambut,
            "Gradasi Warna": gradasi_warna,
            "Request Lagu": lagu_request,
        }
        st.session_state.riwayat_pemesanan.append(pemesanan_baru)
        st.success(f"Pemesanan berhasil! Detail:\nNama: {nama}\nTanggal: {tanggal}\nWaktu: {waktu}\nTotal Harga: Rp {total_harga}")

        # Menampilkan tabel riwayat pemesanan
        riwayat = st.session_state.riwayat_pemesanan
        st.write("### Riwayat Pemesanan 📊")
        if riwayat:
            df = pd.DataFrame(riwayat)
            df.index = df.index + 1
            st.table(df)


# Menjalankan aplikasi
if __name__ == "__main__":
    pemesanan_online()
