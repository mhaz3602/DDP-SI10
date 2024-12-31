import streamlit as st
from pemesanan import pemesanan_online
from anggota import sistem_anggota
from konsultasi import konsultasi_gaya_rambut
from promosi import promosi_dan_pemasaran
import streamlit.components.v1 as components

# CSS untuk mempercantik dengan tema warna baru
def add_custom_css():
    st.markdown("""
        <style>
        /* Global Style */
        body {
            background: linear-gradient(135deg, #fdf6e3, #f7d794); /* Gradasi warna emas lembut */
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3 {
            color: #333;
        }
        .main-header {
            background-color: #fff8e1; /* Warna emas pucat */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .sidebar .sidebar-content {
            background-color: #1a1a1a; /* Hitam */
            color: white;
        }
        .sidebar .sidebar-content .sidebar-title {
            font-size: 20px;
            font-weight: bold;
        }
        .menu-item:hover {
            background-color: #ffe0b2; /* Warna hover emas */
            border-radius: 8px;
        }
        /* Tombol Utama */
        .stButton>button {
            background-color: #ffb74d; /* Warna oranye emas */
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        /* Efek Hover */
        .stButton>button:hover {
            background-color: #ffa726; /* Oranye lebih gelap */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            transform: scale(1.02);
        }
        /* Efek Klik */
        .stButton>button:active {
            transform: scale(0.98);
        }
        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: #1a1a1a; /* Hitam */
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# Fungsi Utama
def main():
    add_custom_css()

    st.sidebar.title("👋 Welcome to Website 🙌🏼")
    st.sidebar.title("👑 Crown Cuts ✂️")
    st.sidebar.markdown("___")
    
    menu = st.sidebar.radio(
        "Pilih Menu",
        ["📅 Pemesanan Online", "👥 Manajemen Keanggotaan", "💇 Konsultasi Gaya Rambut", "📣 Promosi dan Pemasaran"]
    )

    st.markdown("<div class='main-header'><h1>👑 Welcome to Crown Cuts ✂️</h1><p>Experience the luxury of professional grooming</p></div>", unsafe_allow_html=True)

    if menu == "📅 Pemesanan Online":
        pemesanan_online()
        
    elif menu == "👥 Manajemen Keanggotaan":
        sistem_anggota()
    
    elif menu == "💇 Konsultasi Gaya Rambut":
        konsultasi_gaya_rambut()
     
    elif menu == "📣 Promosi dan Pemasaran":
        promosi_dan_pemasaran()
       


if __name__ == "__main__":
    main()
