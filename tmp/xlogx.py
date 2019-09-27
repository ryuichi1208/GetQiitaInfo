# y = xlogx のグラフ

# 必要なモジュールをインポート
import numpy as np
import matplotlib.pyplot as plt

# Figureを設定
fig = plt.figure()

# グラフ描画領域を追加
ax = fig.add_subplot(111)

# Axesのタイトルを設定
ax.set_title("y = xlogx", fontsize = 16)

# 0.1～4.0まで0.01刻みのデータを作成
x = np.arange(0.1, 4.0, 0.01)

# y = xlogx
y = x * np.log(x)

# 軸範囲の設定
ax.set_xlim(0, 2)
ax.set_ylim(-1, 2)

# データをプロット
ax.plot(x, y, color = "r")
