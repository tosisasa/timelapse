#!/bin/sh

BASE_DIR=/home/pi/Documents/Projects/timelapse
WORK_DIR=${BASE_DIR}/work

# タイムラプス動画ファイルの名前は日時から決める
file_name=$(date +%Y%m%d%H%M%S).mp4

# ファイルをdataからworkへコピー。ファイル名は000001.jpgから始まる連番のものへ変更。
cd ${BASE_DIR}
/usr/bin/python3 file_copy.py

# タイムラプス動画ファイルの生成
cd ${WORK_DIR}
if [ -e ${WORK_DIR}/000001.jpg ]; then
  # ${WORK_DIR}/000001.jpg が存在する時だけ下記を実行
  /usr/bin/ffmpeg -y -f image2 -r 12 -i %06d.jpg -aspect 16:9 -s '640x360' ${file_name}
  /usr/bin/python3 ${BASE_DIR}/tweet.py ${file_name}
  rm ${BASE_DIR}/data/*.jpg
  rm ${WORK_DIR}/*.jpg
fi

