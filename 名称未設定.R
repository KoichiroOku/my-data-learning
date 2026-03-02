# ============================================================
# irisデータセットを使った散布図の描画
# 花びらの長さ（Petal.Length）と幅（Petal.Width）の相関を可視化
# ============================================================

# --- 1. データの確認 ---
# irisはRに最初から入っているサンプルデータです
head(iris)        # 最初の6行を表示
str(iris)         # データの構造を確認（列名・型など）

# --- 2. 基本的な散布図を描く ---
# plot() は最もシンプルなグラフ描画関数です
plot(
  x    = iris$Petal.Length,      # X軸：花びらの長さ
  y    = iris$Petal.Width,       # Y軸：花びらの幅
  col  = as.integer(iris$Species), # 種ごとに色分け（1〜3の整数に変換）
  pch  = 16,                     # 点の形（16 = 塗りつぶし円）
  xlab = "花びらの長さ (Petal Length)",  # X軸ラベル
  ylab = "花びらの幅 (Petal Width)",     # Y軸ラベル
  main = "irisデータ：花びらの長さと幅の相関"  # グラフのタイトル
)

# --- 3. 凡例（legend）を追加 ---
legend(
  "topleft",                          # 凡例の位置
  legend = levels(iris$Species),      # 種名（setosa, versicolor, virginica）
  col    = 1:3,                       # 色（種の番号に対応）
  pch    = 16,                        # 点の形
  title  = "品種"
)

# --- 4. 相関係数を計算して表示 ---
# cor() で2つの数値の相関係数（-1〜1）を計算します
r <- cor(iris$Petal.Length, iris$Petal.Width)
cat(sprintf("花びらの長さと幅の相関係数: r = %.3f\n", r))
# 1に近いほど強い正の相関（一方が大きいともう一方も大きい）

# --- 5. 回帰直線を追加 ---
# abline() + lm() で「最もよく当てはまる直線」を引きます
abline(
  lm(Petal.Width ~ Petal.Length, data = iris),  # 線形回帰モデル
  col = "gray40",   # 直線の色
  lwd = 2,          # 直線の太さ
  lty = 2           # 線の種類（2 = 破線）
)


