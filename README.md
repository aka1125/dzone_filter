# dzone-filter 
ROS 2 ノード間の通信において、微小な入力値を無視するための不感帯処理を提供するパッケージです。

## 概要
ジョイスティックのスティックの遊びや、センサーの微細なノイズを除去するために使用します。指定したしきい値（`zone`）以下の絶対値を持つ入力を `0.0` として出力します。

#ノード構成
- filter_node
メインの処理を行うノードです。
 - パラメータ
zone(float, デフォルト: 0.1): フィルタリングする範囲。

- test_publisher
動作確認用にダミーのスキャンデータを送信するノードです。

## 必要なソフトウェア
- ROS 2（Humble/Iron/Jazzy 等）
- Python3.10以上（テスト済: 3.13.5, 3.7〜3.10）

# インストール手順・クイックスタート
※ ここではワークスペース名を `ros2_ws` と仮定します。ご自身の環境に合わせて読み替えてください。
```bash
$ git clone https://github.com/aka1125/dzone_filter
$ cd ~/ros2_ws
$ colcon build --packages-select dzone_filter
$ source install/setup.bash
$ ros2 launch dzone_filter filter_launch.py
[INFO] [launch]: All log files can be found below /home/...
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [filter_node-1]: process started with pid [85682]
[INFO] [test_publisher-2]: process started with pid [85684]
[filter_node-1] [INFO] [1766062337.642705270] [filter]: 0.0
[filter_node-1] [INFO] [1766062337.733747821] [filter]: 0.0
[filter_node-1] [INFO] [1766062337.835406267] [filter]: 0.0
[filter_node-1] [INFO] [1766062337.934763708] [filter]: 0.15000000000000002
[filter_node-1] [INFO] [1766062338.035405361] [filter]: 0.15000000000000002
[filter_node-1] [INFO] [1766062338.134136615] [filter]: 0.15000000000000002
[filter_node-1] [INFO] [1766062338.234472888] [filter]: 0.3
[filter_node-1] [INFO] [1766062338.335488275] [filter]: 0.3
[filter_node-1] [INFO] [1766062338.434305758] [filter]: 0.3
```

## テスト環境
- Ubuntu 22.04.4 LTS
- Python 3.13.5（64bit）

# 権利について
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

- © 2025 Yusaku Aka
