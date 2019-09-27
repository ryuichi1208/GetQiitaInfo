import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,6]
plt.plot(x, y)

x = [1,2,3]
y = [2,4,6]
plt.scatter(x, y)

left = [1, 2, 3]
height = [100, 200, 300]
plt.bar(left, height)

plt.title('グラフタイトル')

plt.xlabel('X軸ラベル')
plt.ylabel('Y軸ラベル')

plt.xlim(Xの最小値, Xの最大値)
plt.ylim(Yの最小値, Yの最大値)

plt.grid()

plt.legend()

plt.figure(figsize=(6,4))

# 左上
plt.subplot(2,2,1)
plt.plot(x1, y1)

# 右上
plt.subplot(2,2,2)
plt.plot(x2, y2)

# 左下
plt.subplot(2,2,3)
plt.plot(x3, y3)

# 右下
plt.subplot(2,2,4)
plt.plot(x4, y4)

plt.show()

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # 下軸と左軸をそれぞれ中央へもってくる
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    # 上軸と右軸を表示しない
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

ax.spines['bottom'].set_position(('outward', 20))
ax.spines['left'].set_position(('outward', -20))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.spines['bottom'].set_position(('data', 2))
ax.spines['left'].set_position(('data', -3))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.spines['bottom'].set_position('center')
ax.spines['left'].set_position('center')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

def main():
    font = {"family": "IPAexGothic"}
    mpl.rc('font', **font)

    point_list = [
        {'p': [2, 1], 'name': 'A', 'c': 'red'},
        {'p': [-1, 2], 'name': 'B', 'c': 'blue'},
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for p in point_list:
        ax.annotate(s=p['name'], xy=[0, 0], xytext=p['p'], fontsize=13,
                    arrowprops=dict(arrowstyle='<-',
                                    connectionstyle='arc3',
                                    facecolor=p['c'], edgecolor=p['c'])
                    )

    lim = [-4, 4]

    ax.set_xlim(lim)
    ax.set_ylim(lim)

    ax.grid()

    ax.spines['bottom'].set_position('center')
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.6))

    plt.savefig(re.sub(".py", "", os.path.basename(__file__))+".png")


if __name__ == '__main__':
    main()
    
"""
right
center left
upper right
lower right
best
center
lower left
center right
upper left
upper center
lower center
"""
