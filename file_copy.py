import os
import pathlib
import shutil


base_dir = '/home/pi/Documents/Projects/timelapse'  # プログラム用のディレクトリー名
pattern = '*.jpg'  # 対象はファイル名が .jpg で終わるファイル
cnt = 0  # 連番ファイル名の作成に使用
work_dir = base_dir + '/work' # work用のディレクトリー名
if not os.path.exists(work_dir):
    os.mkdir(work_dir)  # work_dirが存在しなかったら作成
path = pathlib.Path( base_dir + '/data')  # 写真データのあるディレクトリーへのパスを取得
sorted_list = sorted(list(path.iterdir()))  # ファイル一覧をソートしてリスト変数へ代入
for f in sorted_list:  # ファイル一覧の各ファイルについて繰り返し処理
    if f.match(pattern):  # patternに一致するファイルならコピー処理
        src = f
        cnt += 1  # 連番ファイル用の変数をカウントアップ
        dest = '{0}/{1:06d}.jpg'.format(work_dir, cnt)  # コピー先のファイル名は連番にする
        shutil.copyfile(src, dest)  # ファイルコピー

