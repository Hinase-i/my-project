import streamlit as st

st.set_page_config(page_title="レッドウィング診断", layout="centered")

st.title("🥾 レッドウィング診断アプリ")
st.write("あなたにぴったりの一足を見つけましょう！")

shape = st.radio("形を選んでください", ["モックトゥ", "プレーントゥ"])
color = st.radio("色を選んでください", ["黒", "赤茶", "チェリーブラック", "ブラウン"])

def get_boots_id(shape, color):
    if shape == "モックトゥ":
        if color == "ブラウン": return "875"
        if color == "赤茶": return "8875"
        if color == "黒": return "8849"
        if color == "チェリーブラック": return "8149"
    elif shape == "プレーントゥ":
        if color == "黒": return "9060"
        if color == "赤茶": return "9422"
        if color == "チェリーブラック": return "9419"
        if color == "ブラウン": return "8083"
    return None

if st.button("診断する"):
    boots_id = get_boots_id(shape, color)
    if boots_id:
        st.session_state.boots_id = boots_id
        st.switch_page("pages/Result.py")
    else:
        st.error("その組み合わせは該当なしです。別の組み合わせを試してください！")
