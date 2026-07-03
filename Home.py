import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="レッドウィング診断", layout="centered")

st.title("🥾 レッドウィング診断アプリ")
st.write("あなたにぴったりの一足を見つけましょう！")

# 2. 型番とデータの辞書
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

# 3. 診断ロジック
def get_boots_id(shape, color):
    if shape == "モックトゥ":
        if color == "オレンジ": return "875"
        if color == "赤茶": return "8875"
        if color == "黒": return "8849"
        if color == "チェリーブラック": return "8146"
    elif shape == "プレーントゥ":
        if color == "黒": return "9060"
        if color == "赤茶": return "9422"
        if color == "チェリーブラック": return "9419"
        if color == "ブラウン": return "8083"
    return None

# 4. 入力フォーム
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

if not st.session_state.show_result:
    shape = st.radio("形を選んでください", ["モックトゥ", "プレーントゥ"])
    color = st.radio("色を選んでください", ["黒", "赤茶", "オレンジ", "チェリーブラック", "ブラウン"])

    if st.button("診断する"):
        boots_id = get_boots_id(shape, color)
        if boots_id:
            st.session_state.boots_id = boots_id
            st.session_state.show_result = True
            st.rerun()
        else:
            st.error("その組み合わせは該当なしです。")

# 5. 結果表示エリア
else:
    boots_id = st.session_state.boots_id
    info = boots_info[boots_id]
    
    st.success(f"おすすめ: **{info['name']}**")
    st.image(info['url'], use_column_width=True)
    st.balloons()
    
    if st.button("もう一度診断してみる 🥾"):
        st.session_state.show_result = False
        st.rerun()
