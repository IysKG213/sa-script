# テストの平均点を出力する処理

# for loopで変数に渡す値を設定
point_list = [50, 75, 91]
# 合計点の変数totalの初期化
total = 0
# for文で合計点を計算
for point in point_list:
    total = total + point
#    print('Your Point is', total , '.')
#print('End of For Loop')

# 変数point_listのデータの個数(リストの長さ)をlen関数で取得
num_subject = len(point_list)
# 合計点をデータの個数で割って平均点を割り出す
avg = total / num_subject
print ('SUM={}. AVERAGE={}.'.format(total, avg))
