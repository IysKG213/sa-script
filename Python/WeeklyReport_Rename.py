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

## リスト内最後尾(最新)のファイルを変数に代入
rep_name = files[-1]

## 変数tdに今日の日付を代入
td = datetime.date.today()

## 変数tdに来週の7日分加算して変数ndとする
nd = td + datetime.timedelta(days = 7)
## 変数ndを整形しyyyymmdd形式にする
nd = nd.strftime("%Y%m%d")

## 取得した最新のファイルコピー元にして新しい定例資料を作成
shutil.copy(rep_name,'定例資料_'+ nd +'.md')