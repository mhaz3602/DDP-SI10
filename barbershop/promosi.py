import streamlit as st
import random
from PIL import Image
import datetime

# Fitur Promosi dan Pemasaran
def promosi_dan_pemasaran():
    st.title("Promosi & Pemasaran 📣")

    # Add a video section
    st.markdown("<h2 style='color:#f76c6c;'>Video of Barbershop Tour</h2>", unsafe_allow_html=True)
    st.video("https://youtu.be/sL3iCtFga3Q?si=PTobCbvplS7QnrLC")

    # Formulir Feedback
    komentar = st.text_area("Pesan, Kesan, Kritik, dan Masukan 💬")

    # Fitur Rating Bintang
    st.write("Berikan Rating Anda: ⭐️")
    rating = st.slider("Rating (1-5) ⭐️", min_value=1, max_value=5, step=1)

    if st.button("Kirim Komentar 📝"):
        if "komentar_riwayat" not in st.session_state:
            st.session_state.komentar_riwayat = []
        st.session_state.komentar_riwayat.append({"komentar": komentar, "rating": rating})
        st.success("Komentar dan rating Anda berhasil dikirim! 🎉")

    # Tampilkan Riwayat Komentar dan Rating
    if "komentar_riwayat" in st.session_state:
        st.write("Riwayat Komentar dan Rating 💬:")
        for idx, entry in enumerate(st.session_state.komentar_riwayat, 1):
            st.write(f"{idx}. Komentar: {entry['komentar']}")
            st.write(f"   Rating: {'★' * entry['rating']} 🌟")

    # Tampilkan Rata-rata Rating
    if "komentar_riwayat" in st.session_state:
        ratings = [entry['rating'] for entry in st.session_state.komentar_riwayat]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        st.write(f"Rata-rata Rating: {'★' * int(avg_rating)} ({avg_rating:.2f})")

    # Promo Diskon dan Kode Promo
    st.image("img/infografis babershop.jpeg", caption="Promo Potong Rambut ✂️")
    st.write("Dapatkan diskon 25% untuk member baru! 🎁")

    if st.button("Dapatkan Kode Promo 🎟️"):
        kode_promo = f"PROMO{random.randint(1000, 9999)}"
        st.write(f"Kode Promo Anda: {kode_promo} 🎉")

    # Galeri Gambar Promo
    st.write("Galeri Promo 📸:")
    st.image(["img/poster barbershop.png"], caption=["Promo A"], use_column_width=True)

    # Tautan Media Sosial
    st.write("Jangan Lupa Kunjungi SOSMED Kami Dibawah ini, Terimakasih! 😊")
    st.markdown("[Instagram Kami](https://www.instagram.com/mhaz326/<username>)")
    st.markdown("[LinkedIn Kami](https://www.linkedin.com/in/m-hudzaifah-ali-al-mubarok-a1a83132b/<username>)")

# Jalankan aplikasi
if __name__ == "__main__":
    promosi_dan_pemasaran()
