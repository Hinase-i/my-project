print("--- レッドウィング診断へようこそ！ ---")

# 形を選択
print("【形を選択してください】")
print("1: モックトゥ / 2: プレーントゥ")
shape_num = input("番号を入力: ")

# 色を選択
print("\n【色を選択してください】")
print("1: 黒 / 2: 赤茶 / 3: ブラウン / 4: チェリーブラック")
color_num = input("番号を入力: ")

# 数字を言葉に変換する辞書
shape_map = {"1": "モックトゥ", "2": "プレーントゥ"}
color_map = {"1": "黒", "2": "赤茶", "3": "ブラウン", "4": "チェリーブラック"}

# 選択肢を変換
shape = shape_map.get(shape_num)
color = color_map.get(color_num)

def suggest_boots(shape, color):
    if not shape or not color:
        return "正しい番号を選択してください。"
    
    # 診断ロジック
    if shape == "モックトゥ":
        if color == "ブラウン": return "875 (これぞレッドウィング！王道のアイリッシュセッター)"
        if color == "赤茶": return "8875 (深みのある赤茶色で、履くほどに育つ相棒)"
        if color == "黒": return "8849 (履くほどに茶芯が顔を出す、育てがいのあるブラック)"
　　　　if color == "チェリーブラック"：return "8149 (履くほどに深みが増し、大人の風格が漂う一足)"
    elif shape == "プレーントゥ":
        if color == "黒": return "9060(フラットボックスならではのやれ感と茶芯がたまらない)"
        if color == "赤茶": return "9422(履き込むほどに深い味わいが出て、愛着が湧く一足)"
        if color == "チェリーブラック": return "9419 (ベックマン・スタイルで、気品とタフさを両立)"
　　　　if color == "ブラウン": return "8083(ウエスタンな雰囲気も漂う、ラフに履きこなしたいアイアンレンジャー)"
    return "その組み合わせも渋い！お店で探してみる価値ありです。"

print("\n--- 診断結果 ---")
print(f"あなたにおすすめのレッドウィングは... {suggest_boots(shape, color)}")
