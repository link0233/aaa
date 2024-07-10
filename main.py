import json

def main () -> None:
    try:
        with open("save.json","r") as f:
            Data = json.load(f)
    except:
        with open("save.json","w") as f:
            pass
        Data = {}

    while True:
        songName : str = input("請輸入歌曲名稱，如果輸入 _exit_ 即可退出，洛直接按關掉就不存檔搂 ")
        if songName == "_exit_":
            break

        print("請輸入成績，如輸入錯誤將會有成績不準的問題")
        perfect : int = askNumber("perfect")
        great   : int = askNumber("great")
        good    : int = askNumber("good")
        bad     : int = askNumber("bad")
        miss    : int = askNumber("miss")
        score   : int = perfect * 3 + great * 2 + good
        maxscore: int =  (perfect + great + good + bad + miss) * 3
        print(f"您分數是:{score} = 理論值 - {abs(maxscore - score)}\n ，理論值是: {maxscore}")

        if songName not in Data:
            Data[songName] = [perfect,great,good,bad,miss,score,1]
        else:
            a = [perfect,great,good,bad,miss,score]
            b = Data[songName]
            b[-1] += 1 
            c = ["平均perfect","平均great","平均good","平均bad","平均miss","平均總分"]
            for i in range(len(a)):
                b[i] += a[i]
                print( c[i] + str(b[i] / b[-1]))
            
            Data[songName] = b
    
    with open("save.json","w") as f:
        json.dump(Data,f)

def askNumber(question : str) -> int:
    ok = False
    while not ok:
        ok = True
        try:
            k : int = int(input(f"請輸入您的{question}數量 : "))
        except: 
            ok = False
            print("請輸入數字")
    return k

if __name__ == "__main__":
    main()