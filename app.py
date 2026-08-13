import streamlit as st
import time

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎂",
    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #ffdde1 0%,
        #ee9ca7 50%,
        #ffd6e7 100%
    );
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #ffffff;
    text-shadow: 3px 3px 10px #c2185b;
}

.subtitle {
    text-align: center;
    font-size: 24px;
    color: white;
}

.card {
    background: rgba(255,255,255,0.90);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    text-align: center;
}

.message {
    font-size: 22px;
    color: #c2185b;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown(
    '<div class="title">🎂 HAPPY BIRTHDAY 🎂</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✨ A Special Birthday Surprise ✨</div>',
    unsafe_allow_html=True
)

st.write("")

# =========================
# SIDEBAR SETTINGS
# =========================

st.sidebar.title("🎨 Birthday Settings")

name = st.sidebar.text_input(
    "Nama birthday person",
    "My Friend"
)

message = st.sidebar.text_area(
    "Birthday Message",
    "Semoga panjang umur, dimurahkan rezeki, "
    "dipermudahkan segala urusan dan sentiasa bahagia! 💖"
)

emoji = st.sidebar.selectbox(
    "Pilih emoji",
    ["🎂", "🎉", "🥳", "🎁", "💖", "✨"]
)

# =========================
# PHOTO UPLOAD
# =========================

st.sidebar.write("### 📸 Upload Gambar")

uploaded_file = st.sidebar.file_uploader(
    "Upload gambar birthday",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(
        uploaded_file,
        caption=f"✨ {name} ✨",
        use_container_width=True
    )

# =========================
# MAIN CARD
# =========================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
    f"""
    <h1 style="color:#c2185b;">
        {emoji} Happy Birthday, {name}! {emoji}
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("")

if "surprise" not in st.session_state:
    st.session_state.surprise = False

# =========================
# BUTTON
# =========================

if not st.session_state.surprise:

    if st.button(
        "🎁 OPEN BIRTHDAY SURPRISE",
        use_container_width=True
    ):
        st.session_state.surprise = True
        st.rerun()

else:

    # Confetti
    st.balloons()

    st.markdown(
        f"""
        <div class="message">
            <h2>🎉 SURPRISE! 🎉</h2>

            <p>
            {message}
            </p>

            <h1>
            🎂 🎈 🎁 ✨ 🥳 ✨ 🎁 🎈 🎂
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Extra animation
    progress = st.progress(0)

    for i in range(101):
        time.sleep(0.01)
        progress.progress(i)

    st.success(
        f"🎉 Once again, HAPPY BIRTHDAY {name}! 🎉"
    )

    if st.button(
        "🔄 Reset Surprise",
        use_container_width=True
    ):
        st.session_state.surprise = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
