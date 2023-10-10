import random

# グーチョキパーの定数
GU = 1
CHOKI = 2
PA = 3

# 選択肢のリスト
CHOICES = ["グー", "チョキ", "パー"]

while True:
# プレイヤーの選択を取得
    while True:
        print("1: グー")
        print("2: チョキ")
        print("3: パー")
        choice_str = input("1から3の数字を入力してください: ")
        try:
            choice = int(choice_str)
            if choice < 1 or choice > 3:
                raise ValueError()
            break
        except ValueError:
            print("1から3の数字を入力してください。")

    # コンピューターの選択をランダムに生成
    computer_choice = random.randint(0, 100) % 3

    # 選択を表示
    print("あなたは" + CHOICES[choice - 1] + "を出しました。")
    print("コンピューターは" + CHOICES[computer_choice] + "を出しました。")

    # 勝敗を判定
    if choice == computer_choice + 1:
         print("引き分けです。")
    elif choice == GU and computer_choice + 1 == CHOKI or \
          choice == CHOKI and computer_choice + 1 == PA or \
          choice == PA and computer_choice + 1 == GU:
         print("あなたの勝ちです！")
    else:
         print("あなたの負けです。")
