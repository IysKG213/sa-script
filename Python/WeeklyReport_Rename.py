import shutil, os, datetime

## 指定のディレクトリに移動
os.chdir('C:\\\DIR')
files = []

## カレントディレクトリのマークダウンファイル一覧を作成
for rep_name in os.listdir('.'):
    if os.path.isfile(rep_name):
        base, ext = os.path.splitext(rep_name)
        if ext == '.md':
            files.append(rep_name) 

## リスト内最新のファイルを変数に代入
rep_name = files[-1]

## 今日の日付を変数tDayに代入
tDay = datetime.date.today()

## 次の木曜の日付を計算する(月曜=0～日曜=6)
dayNum = 3 - tDay.weekday() 
dayNum = dayNum+7 if dayNum < 0 else dayNum
delta = datetime.timedelta(days=dayNum)
nextDate = tDay + delta

## 取得した最新のファイルコピー元にして新しい定例資料を作成
shutil.copy(rep_name,'定例資料_'+ nd +'.md')
