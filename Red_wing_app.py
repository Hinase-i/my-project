import streamlit as st

st.title("🥾 レッドウィング診断アプリ")

# 型番と画像の辞書データ
boots_info = {
    "875": {"name": "875 (王道のアイリッシュセッター)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/RW00875_N3.png"},
    "8875": {"name": "8875 (履くほどに育つ相棒)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08875/RW08875_N3.png"},
    "8849": {"name": "8849 (育てがいのあるブラック)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08849/RW08849_N3.png"},
    "8149": {"name": "8146 (大人の風格が漂う一足)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08146/RW08146_N3.png"},
    "9060": {"name": "9060 (フラットボックスの茶芯が最高)", "url":"https://redwingheritage.jp/client_info/RWJ/itemimage/09060/RW09060_N3re.png"},
    "9422": {"name": "9422 (愛着が湧く一足)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/RW09422_N3.png"},
    "9419": {"name": "9419 (気品とタフさを両立)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/RW09419_N3.png"},
    "8083": {"name": "8083 (ラフに履きたいアイアンレンジャー)", "url": "https://redwingheritage.jp/client_info/RWJ/itemimage/08083/RW08083_N3.png"}
}

shape = st.radio("形を選んでください", ["モックトゥ", "プレーントゥ"])
color = st.radio("色を選んでください", ["黒", "赤茶", "チェリーブラック", "ブラウン"])

def get_boots_id(shape, color):
    # ロジックで型番を返す（簡易化のため）
    if shape == "モックトゥ":
        if color == "ブラウン": return "875"
        if color == "赤茶": return "8875"
        if color == "黒": return "8849"
        if color == "チェリーブラック": return "8146"
    elif shape == "プレーントゥ":
        if color == "黒": return "9060"
        if color == "赤茶": return "9422"
        if color == "チェリーブラック": return "9419"
        if color == "ブラウン": return "8083"
    return None

if st.button("診断する"):
    boots_id = get_boots_id(shape, color)
    if boots_id and boots_id in boots_info:
        info = boots_info[boots_id]
        st.success(f"おすすめ: {info['name']}")
        st.image(info['url'], use_column_width=True)
    else:
        st.write("その組み合わせも渋い！お店で探してみる価値ありです。")
