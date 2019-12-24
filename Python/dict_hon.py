# 生徒の評価を表示するプログラムの作成
## 生徒と点数の入った辞書データを用意する。

## 学籍番号と点数群を辞書に登録
point_dict = {
    '001': (100,88,81),
    '002': (77,94,85),
    '003': (80,52,99),
}

## 辞書の変数をfor文にかける
for student_id in point_dict:
    ## keyを指定してvalueを取得
    points  = point_dict[student_id]
    ## 教科数を取得
    subject_num = len(points)
    ## タプルに入った点数群を多重代入と合計の取得
    japanese,english,math = points
    total = japanese + english + math

    ## 評価基準を変数に代入
    excellent = subject_num * 100 * 0.8
    good = subject_num * 100 * 0.65
    
    ## 生徒の点数を評価
    if total > excellent:
        evaluation = 'Excellent!'
    elif total > good:
        evaluation = 'Good.'
    else:
        evaluation = 'Bad!'
    print ('学籍番号{}: 合計点は{}、評価は{}です。'.format(student_id, total, evaluation))

