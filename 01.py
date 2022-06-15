import termcolor
import time

'''
入力
'''
path = "01_prob.txt"#ファイルのパス
prob_txt = []#問題文用の空リスト
prob_choice = []#選択肢用の空リスト
prob_correct = []#正解用の空リスト
with open(path) as file:#ファイル読み込み
    for f in file.readlines():
        f = f.strip()
        if f[0] == "t":
            prob_txt.append(f[2:])
        elif f[0] == "c":
            prob_choice.append(f[2:].split())
        elif f[0] == "a":
            prob_correct.append(f[2:].split())
        else:
            continue

'''
問題作成用の関数
'''
def probCreate(tx, ch, co):#第一引数に問題文、第二引数に選択肢、第三引数に正解
    print(tx)
    import random
    random.shuffle(ch)#選択肢の並びをランダム化
    item = ["a", "b", "c", "d"]
    inp = []
    for k, v in zip(item, ch):
        print("{}.{}".format(k, v))
        if v in co:
            inp.append(k)
    ans = input().split()#解答受付(複数解答が行えるようlist)
    ans.sort()
    result = termcolor.colored("不正解...", "red")
    if ans == inp:
        result = termcolor.colored("正解!!", "green")
    return result

'''
解答
'''
start = time.time()
N = len(prob_txt)#問題数
cnt = [0]*2#正答率表示用のカウントリスト
pickup = []#間違えた問題用リスト
for n in range(N):
    txt = prob_txt[n]
    choice = prob_choice[n]
    correct = prob_correct[n]
    out = probCreate(txt, choice, correct)
    print(out+"\n")
    if out == termcolor.colored("正解!!", "green"):
        if txt[0] == "数":
            cnt[0] += 1
        else:
            cnt[1] += 1
    else:
        pickup.append(txt[0:2])
end = time.time()

'''
出力
'''
print("全体正答率：{}％".format(int((sum(cnt)/N)*100)))
#ジャンル別で正答率表示
print("数学正答率：{}％".format(int((cnt[0]/(N/2))*100)))
print("英語正答率：{}％".format(int((cnt[1]/(N/2))*100)))
print("\n")
#解答時間計測
print("あなたが解答にかけた時間")
print("{}秒です！".format(round((end-start), 2)))
print("\n")
#間違えた問題ピックアップ
print("あなたが間違えた問題")
print("  ".join(pickup))
