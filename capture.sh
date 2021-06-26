#!/bin/sh
# fswebcamコマンドのオプション「-q」を追加して実行時に
# 必要ないメッセージ表示を抑制してあります。

# プログラムを置くディレクトリー
BASE_DIR=/home/pi/Documents/Projects/timelapse

# 写真の幅
WIDTH=640

# 写真の高さ
HEIGHT=360

# ファイル名は年月日時分秒の文字列.jpgとします。
file_name=$(date +%Y%m%d%H%M%S).jpg

#fswebcam -q --no-banner -r ${WIDTH}x${HEIGHT} --rotate 270 \
#   ${BASE_DIR}/data/${file_name} 
raspistill -e jpg -q 20 -w ${WIDTH} -h ${HEIGHT} -rot 90 -o ${BASE_DIR}/data/${file_name} 

