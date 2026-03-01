# ライブラリのインポート
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.datasets import load_iris
import numpy as np

# --------------------------------------------------
# 1. データの読み込み
# --------------------------------------------------
iris = load_iris()
X = iris.data        # 特徴量（sepal length/width, petal length/width）
y = iris.target      # ラベル（0:setosa, 1:versicolor, 2:virginica）
target_names = iris.target_names  # クラス名

# --------------------------------------------------
# 2. 散布図の描画
# --------------------------------------------------
# 色の設定（クラスごとに異なる色を使用）
colors = ['#E74C3C', '#2ECC71', '#3498DB']

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Iris Dataset - Scatter Plots', fontsize=16, fontweight='bold', y=1.02)

# ---- グラフ1: がく片（Sepal）の長さ vs 幅 ----
ax1 = axes[0]
for i, (name, color) in enumerate(zip(target_names, colors)):
    mask = y == i  # クラスiのデータのみ抽出
    ax1.scatter(
        X[mask, 0],  # Sepal Length（がく片の長さ）
        X[mask, 1],  # Sepal Width（がく片の幅）
        c=color, label=name, alpha=0.8, edgecolors='white', s=70
    )
ax1.set_xlabel('Sepal Length (cm)', fontsize=12)
ax1.set_ylabel('Sepal Width (cm)', fontsize=12)
ax1.set_title('Sepal: Length vs Width', fontsize=13)
ax1.legend(title='Species', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.4)

# ---- グラフ2: 花びら（Petal）の長さ vs 幅 ----
ax2 = axes[1]
for i, (name, color) in enumerate(zip(target_names, colors)):
    mask = y == i  # クラスiのデータのみ抽出
    ax2.scatter(
        X[mask, 2],  # Petal Length（花びらの長さ）
        X[mask, 3],  # Petal Width（花びらの幅）
        c=color, label=name, alpha=0.8, edgecolors='white', s=70
    )
ax2.set_xlabel('Petal Length (cm)', fontsize=12)
ax2.set_ylabel('Petal Width (cm)', fontsize=12)
ax2.set_title('Petal: Length vs Width', fontsize=13)
ax2.legend(title='Species', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.4)

# --------------------------------------------------
# 3. レイアウト調整して保存・表示
# --------------------------------------------------
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/iris_scatter.png', dpi=150, bbox_inches='tight')
print("散布図を保存しました: iris_scatter.png")
plt.show()
