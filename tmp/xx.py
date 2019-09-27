# xのx乗のグラフ

# 必要なモジュールをインポート
import numpy as np
import matplotlib.pyplot as plt

# Figureを設定
fig = plt.figure()

# Axesを追加
ax = fig.add_subplot(111)

# Axesのタイトルを設定
ax.set_title("y = x**x", fontsize = 16)

# 0～4.0まで0.01刻みのデータを作成
x = np.arange(0, 4.0, 0.1)

# y = x ** x
y = x ** x

# x軸を対数軸に設定
ax.set_yscale("log")

# データをプロット
ax.plot(x, y, color = "r")
