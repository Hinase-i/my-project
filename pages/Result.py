import streamlit as st

boots_info = {
    "875": {"name": "875 (王道のアイリッシュセッター)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/RW00875_N3.png"},
    "8875": {"name": "8875 (履くほどに育つ相棒)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08875/RW08875_N3.png"},
    "8849": {"name": "8849 (育てがいのあるブラック)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08849/RW08849_N3.png"},
    "8146": {"name": "8146 (大人の風格が漂う一足)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08146/RW08146_N3.png"},
    "9060": {"name": "9060 (フラットボックスの茶芯が最高)", "url":"https://redwingheritage.jp/client_info/RWJ/itemimage/09060/RW09060_N3re.png"},
    "9422": {"name": "9422 (愛着が湧く一足)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/RW09422_N3.png"},
    "9419": {"name": "9419 (気品とタフさを両立)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/RW09419_N3.png"},
    "8083": {"name": "8083 (ラフに履きたいアイアンレンジャー)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08083/RW08083_N3.png"}
}

st.title("診断結果")

if 'boots_id' in st.session_state:
    boots_id = st.session_state.boots_id
    # 万が一、辞書にないIDが来た時のための安全策
    if boots_id in boots_info:
        info = boots_info[boots_id]
        st.success(f"あなたにおすすめのレッドウィング: **{info['name']}**")
        st.image(info['url'], use_column_width=True)
        st.balloons()
    else:
        st.write("結果が見つかりませんでした。")
else:
    st.warning("診断がまだ行われていません。ホームに戻ってください。")

if st.button("もう一度診断してみる 🥾"):
    st.switch_page("Home.py")
