import datetime
import os
import pygame
import pygame.camera
import pygame.image
import time

INTERVAL = 10.0  # 撮影間隔
IMAGE_WIDTH = 1280  # 写真の幅
IMAGE_HEIGHT = 720  # 写真の高さ
base_dir = '/home/pi/Documents/Projects/timelapse'  # プログラム用ディレクトリー名
data_dir = base_dir + '/data'  # データ用ディレクトリー名
if not os.path.exists(data_dir):  # データ用ディレクトリーがない場合は作成
    os.mkdir(data_dir)

# カメラ用意
pygame.init()
pygame.camera.init()
camera_list = pygame.camera.list_cameras()
camera = pygame.camera.Camera(camera_list[0], (IMAGE_WIDTH, IMAGE_HEIGHT))

# 撮影
for cnt in range(150):  # 150回撮影したら終了
    now = datetime.datetime.now()  # 現在時刻の取得
    now_str = now.strftime('%Y%m%d%H%M%S')  # 年月日時分秒の文字列の取得
    file_name = data_dir + '/' + now_str + '.jpg'  # 写真ファイル名の生成
    print(str(cnt) + ':' + file_name)
    camera.start()
    img = camera.get_image()  # カメラ撮影
    pygame.image.save(img, file_name)  # ファイル保存
    camera.stop()
    td = datetime.datetime.now() - now  # コマンド実行後の時刻取得
    micro_td = (td / datetime.timedelta(microseconds=1)) / 1000000.0  # コマンド実行にかかった秒数算出
    time.sleep(INTERVAL - micro_td)  # コマンド実行分も考慮してINTERVAL秒休止

