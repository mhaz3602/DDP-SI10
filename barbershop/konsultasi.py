import streamlit as st

# Kelas untuk Saran Gaya Rambut
class SaranGayaRambut:
    def __init__(self, bentuk_wajah, jenis_kelamin, saran):
        self.bentuk_wajah = bentuk_wajah
        self.jenis_kelamin = jenis_kelamin
        self.saran = saran

    def tampilkan_saran(self):
        return self.saran[self.bentuk_wajah][self.jenis_kelamin]

# Gambar model rambut
model_gambar = {
    "Undercut": "https://th.bing.com/th/id/OIP.PfDvXEyXL_gtxKx5GXHKFgHaIP?rs=1&pid=ImgDetMain",
    "Quiff": "https://th.bing.com/th/id/OIP.5InHc661l1acSMzhBGWZ5AAAAA?rs=1&pid=ImgDetMain",
    "Pompadour": "https://haircuts4men.b-cdn.net/wp-content/uploads/2023/11/High-Fade-Pompadour-and-Hard-Part-Pompadour-Haircut.jpg",
    "High Fade": "https://i.pinimg.com/originals/42/9a/e6/429ae6081e8cf7e344581d709232d956.jpg",
    "Faux Hawk": "https://cdn.idntimes.com/content-images/community/2021/11/skin-sharp-fade-faux-hawk-3-2df74cab14a794816f8530862347a9af-003316c719b5426ab453659928477408.jpg",
    "Crew Cut": "https://awsimages.detik.net.id/community/media/visual/2023/01/09/potongan-rambut-crew-cut-6_34.webp?w=375",
    "Side Part": "https://obs.line-scdn.net/0h2g-QfggMbUgQKEBdUV0SHyp-bicjRH5LdB48S0xGM3xuHikbfk0hJjMgY3k0SCoWfhknKDwgdnk0SH4YLk4h/w644",
    "Textured Crop": "https://lookosm.com/wp-content/uploads/2023/10/French-Crop-With-Blunt-Bangs.jpg",
    "Fringe": "https://st4allthings4p4ci.blob.core.windows.net/allthingshair/allthingshair/wp-content/uploads/sites/10/2022/08/31100539/textured-fringe-pinterest.jpg",
    "Slick Back": "https://haircutinspiration.com/wp-content/uploads/Neat-Side-Swept-with-Faded-Temple-300x407.jpg",
    "Angular Fringe": "https://th.bing.com/th/id/OIP.w6FYkxYi4joN-YNbitN2RAHaG4?w=700&h=650&rs=1&pid=ImgDetMain",
    "Layered": "https://hairstylesfeed.com/wp-content/uploads/2022/03/Curtain-Bangs.jpg",
    "Bob": "https://cdn.popmama.com/content-images/community/20220203/community-7d95ad996a2c3341d0a5a81d5c845dcb.jpg?1643888359",
    "Pixie": "https://pagaralampos.disway.id/upload/af3b3386fc1ce2c08a1abefd26d07e3a.jpg",
    "Long Layers": "https://cdn.popmama.com/content-images/community/20220428/community-d230f8e807138cfa2079d3120a9c1165.jpg?1651137523",
    "Shaggy Bob": "https://o-cdn-cas.sirclocdn.com/parenting/images/bob-layer.width-800.format-webp.webp",
    "Bangs": "https://img.okezone.com/okz/500/library/images/2022/10/10/gu8dm1tdklnqc8y6t0gd_20632.jpg",
    "Soft Layers": "https://th.bing.com/th/id/OIP.oxPDKxkfUVhb3xiUvUcQrAAAAA?rs=1&pid=ImgDetMain",
    "Wavy Bob": "https://img.okezone.com/okz/500/library/images/2022/12/10/puucfr0d6qj3jc7vecfq_11973.jpg",
    "Chin-Length Bob": "https://cdn.popmama.com/content-images/community/20220428/community-85d05ab54afa5144296bacca7f8c208a.jpg?1651136471",
    "Wispy Bangs": "https://i.pinimg.com/236x/6a/2a/30/6a2a30ce416eebf1a96b0d342ec49a81.jpg"
}

# Fungsi untuk konsultasi gaya rambut
def konsultasi_gaya_rambut():
    st.title("Konsultasi Gaya Rambut 💇‍♂️💇‍♀️")

    bentuk_wajah = st.selectbox("Pilih Bentuk Wajah 👱‍♂️👱", ["Oval", "Bulat", "Kotak", "Hati"])
    jenis_kelamin = st.selectbox("Pilih Jenis Kelamin 👦👧", ["Laki-laki", "Perempuan"])

    # Saran gaya rambut berdasarkan bentuk wajah dan jenis kelamin
    saran = {
        "Oval": {"Laki-laki": ["Undercut", "Quiff", "Pompadour"], "Perempuan": ["Layered", "Bob", "Pixie"]},
        "Bulat": {"Laki-laki": ["Pompadour", "High Fade", "Faux Hawk"], "Perempuan": ["Long Layers", "Shaggy Bob", "Bangs"]},
        "Kotak": {"Laki-laki": ["Crew Cut", "Side Part", "Textured Crop"], "Perempuan": ["Soft Layers", "Side Part", "Wavy Bob"]},
        "Hati": {"Laki-laki": ["Fringe", "Slick Back", "Angular Fringe"], "Perempuan": ["Chin-Length Bob", "Wispy Bangs", "Long Layers"]},
    }

    saran_gaya = SaranGayaRambut(bentuk_wajah, jenis_kelamin, saran)
    gaya_rambut = saran_gaya.tampilkan_saran()

    st.write("Saran Gaya Rambut ✂️:", ", ".join(gaya_rambut))

    # Tampilkan gambar untuk setiap gaya rambut yang disarankan
    for gaya in gaya_rambut:
        if gaya in model_gambar:
            st.image(model_gambar[gaya], caption=gaya, width=150)  


    # FAQ
    st.write("### FAQ (Pertanyaan yang Sering Diajukan) 🤔")
    faq = {
        "Berapa lama waktu untuk potong rambut?": "Waktu rata-rata sekitar 30-45 menit, tergantung gaya yang dipilih.",
        "Apakah ada biaya tambahan untuk konsultasi?": "Tidak, konsultasi gaya rambut adalah gratis.",
        "Apakah bisa request model rambut?": "Tentu, Anda bisa membawa contoh gambar atau deskripsi yang jelas."
    }
    for tanya, jawab in faq.items():
        with st.expander(tanya):
            st.write(jawab)

    # Formulir pertanyaan untuk ahli
    st.write("### Ajukan Pertanyaan ke Ahli 📝")
    pertanyaan = st.text_area("Tulis pertanyaan Anda:")
    if st.button("Kirim Pertanyaan 📤"):
        if pertanyaan:
            st.success("Pertanyaan Anda telah terkirim ke ahli. Harap tunggu balasan dalam waktu 24 jam. ⏳")
        else:
            st.error("Harap tuliskan pertanyaan sebelum mengirim. ❗️")

# Jalankan aplikasi
if __name__ == "__main__":
    konsultasi_gaya_rambut()
