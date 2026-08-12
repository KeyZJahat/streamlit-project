import streamlit as st

# Tajuk aplikasi
st.title("🧪 Ujian Streamlit")

# Teks pengenalan
st.write("Jika anda melihat halaman ini, Streamlit anda telah berjaya dipasang!")

# Interaksi ringkas menggunakan input nama
name = st.text_input("Masukkan nama anda:", "Pengguna")

# Butang tindakan
if st.button("Sapa Saya"):
    st.success(f"Helo, {name}! Selamat datang ke Streamlit.")

# Widget slider ringkas
number = st.slider("Pilih satu nombor:", 1, 100, 50)
st.write(f"Nombor yang anda pilih ialah: **{number}**")
