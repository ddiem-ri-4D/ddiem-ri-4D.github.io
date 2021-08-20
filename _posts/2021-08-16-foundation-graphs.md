---
title: "Cơ bản về Lý Thuyết Đồ Thị"
categories:
  - Mathematics
tags:
  - Mathematics
  - Graphs
  - Theory
toc: true
comments: true
header:
  teaser: "/assets/images/header/graph-theory.png"
---
Một số kiến thức, định nghĩa, định lý cơ bản về Lý Thuyết Đồ Thị rất cần thiết trong việc tìm hiểu và nghiên cứu về Lý thuyết đồ thị và Máy học với Đồ thị.

## Đại diện đồ thị (Graph Representations)

**Định nghĩa về đồ thị** (Graph): Một đồ thị được ký hiệu là $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$
, trong đó $$\mathcal{V} = \{v_1, ..., v_N\}$$ là một tập của $N = \|\mathcal{V}\|$ nút (nodes) và $$\mathcal{E} = \{e_1, ..., e_N\}$$ là một tập của $M = \|\mathcal{E}\|$ cạnh (edges)

**Định nghĩa về ma trận kề** (Adjacency Matrix): Cho một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, ma trận kề tương ứng được ký hiệu là $$\mathbf{A} \in \{0, 1\}^{N \times N}$$. Phần tử hàng $i$ cột $j$, gọi là $\mathbf{A}_{ij}$ đại diện cho liên kết giữa hai nút $v_i$ và $v_j$. Cụ thể hơn, nếu $$\mathbf{A}_{ij} = 1$$ thì $v_i$ kề với $v_j$, ngược lại thì $$\mathbf{A}_{ij} = 0$$

## Các tính chất và độ đo (Properties and Measures)

### Bậc (Degree)

**Định nghĩa về bậc** (Degree): Trong một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, bậc của một nút $v_i \in \mathcal{V}$ là số lượng nút kề với $v_i$

$$
d(v_i) = \sum_{v_j \in \mathcal{V}}\mathbb{1}_{\mathcal{E}}(\{v_i,v_j\})
$$

trong đó

$$
\mathbb{1}_{\mathcal{E}}(\{v_i,v_j\}) = \begin{cases}1, \text{    if}(v_i, v_j) \in\mathcal{E}\\1, \text{    if}(v_i, v_j) \notin\mathcal{E}\end{cases}
$$


**Định nghĩa về lân cận** (Neighbors): Với một nút $v_i$ trong một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, tập những lân cận của nó $\mathcal{N}(v_i)$ bao gồm tất cả các nút kề với $v_i$

**Định lý 1** về sự liên hệ giữa bậc và số cạnh của đồ thị: Với một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, tổng bậc của nó bằng hai lần số cạnh trong đồ thị

$$
\sum_{v_i \in \mathcal{V}}d(v_i) = 2 \cdot |\mathcal{E}|
$$

**Hệ quả 1** Số lượng phần tử khác không trong ma trận kề cũng bằng hai lần số cạnh

### Tính liên thông (Connectivity)

**Định nghĩa về bước đi** (Walk): Một bước đi (Walk) trên một đồ thị là một cách nói thay thế chuỗi các nút và cạnh, bắt đầu với một nút và kết nút bằng một nút, mà trong đó mỗi cạnh liên kết với nút trước và sau nó.

**Định nghĩa về đường mòn** (Trail): Một Trail là một bước đi của các cạnh phân biệt

**Định nghĩa về đường đi** (Path): Một path là một bước đi của các đỉnh phân biệt

**Định lý 2**: Với một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$ có ma trận kề $\mathbf{A}$, ta sử dụng $\mathbf{A}^n$ biểu diễn của lũy thừa cấp $n$ của ma trận kề. Phần tử vị trí $ij$ của ma trận $\mathbf{A}^n$ bằng với độ dài $n$ của bước đi $v_i-v_j$

**Định nghĩa về đồ thị con** (Subgraph): Một đồ thị con $$\mathcal{G'} = \{\mathcal{V'}, \mathcal{E'}\}$$ của một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$ cho trước là một dạng đồ thị với một tập con nút $\mathcal{V}' \subset \mathcal{V}$ và một tập cạnh con $\mathcal{E'} \subset \mathcal{E}$. Hơn nữa, tập con $\mathcal{V}'$ phải chứa toàn bộ nút trong tập $\mathcal{E'}$

**Định nghĩa về thành phân liên thông** (Connected Component): Cho một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, một đồ thị con $$\mathcal{G'} = \{\mathcal{V'}, \mathcal{E'}\}$$ được gọi là một thành phần liên thông nếu tồn tại ít nhất một đường đi giữa hai nút bất kỳ trong đồ thị và các nút trong $\mathcal{V'}$ không kề với bất kỳ đỉnh nào trong $\mathcal{V} \setminus \mathcal{V'}$

**Định nghĩa về đồ thị liên thông** (Connected Graph). Một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$ được gọi là liên thông nếu nó có chính xác một thành phần liên thông.

**Định nghĩa về đường đi ngắn nhất** (Shortest Path) Cho một cặp nút $v_s, v_t \in \mathcal{V}$ trong đồ thị $\mathcal{G}$, ta đặt tập đường đi từ nút $v_s$ đến nút $v_t$ là $\mathcal{P}_{st}$. Đường đi ngắn nhất giữa $v_s$ và nút $v_t$'

$$
p_{st}^{sp} = \underset{p \in \mathcal{P}_{st}}{\text{arg min}}|p|
$$

**Định nghĩa về bán kính** (Diameter)

$$
diameter(\mathcal{G}) = \underset{v_s, v_t \in \mathcal{V}}{\text{max} }\underset{p \in \mathcal{P}_{st}}{\text{min}}|p|
$$

### Centrality

1) Degree Centrality

$$
c_d(v_i) = d(v_i) = \sum_{j=1}^N\mathbf{A}_{i,j}
$$

2) Eigenvector Centrality

$$
c_e(v_i) = \frac{1}{\lambda}\sum_{j=1}^N\mathbf{A}_{i,j}\cdot c_e(v_j)
$$

$$
\mathbf{c}_e =  \frac{1}{\lambda}\mathbf{A} \cdot \mathbf{c}_e
$$

$$
\lambda \cdot \mathbf{c}_e = \mathbf{A} \cdot \mathbf{c}_e
$$

3) Katz Centrality

$$
c_k(v_i) = \alpha\sum_{j=1}^N\mathbf{A}_{i,j}c_k(v_j) + \beta
$$

$$
\begin{gather}
\mathbf{c}_k = \alpha\mathbf{A}\mathbf{c}_k + \mathbf{\beta}\\

(\mathbf{I} - \alpha \cdot \mathbf{A})\mathbf{c}_k = \mathbf{\beta}
\end{gather}
$$

4) Betweenness Centrality

$$
c_b(v_i) = \sum_{v_s \ne v_i \ne v_t}\frac{\sigma_{st}(v_i)}{\sigma_{st}}
$$

## Lý thuyết phổ đồ thị (Spectral Graph Theory)

### Ma trận Laplacian (Laplacian Matrix)

**Định nghĩa về ma trận Laplacian** Cho một đồ thị  $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$ với $\mathbf{A}$ là ma trận kề của nó. Thì Laplacian matrix của nó được định nghĩa

$$
\mathbf{L = D - A}
$$

Trong đó $\mathbf{D}$ là một ma trận đường chéo bậc $\mathbf{D} = diag(d(v_1), ..., d(v_N))$

**Định nghĩa về ma trận Laplacian chuẩn** Cho một đồ thị  $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$ với $\mathbf{A}$ là ma trận kề của nó. Thì Laplacian matrix chuẩn của nó được định nghĩa

$$
\mathbf{L} = \mathbf{D}^{-\frac{1}{2}}(\mathbf{D} - \mathbf{A})\mathbf{D}^{-\frac{1}{2}} = \mathbf{I} - \mathbf{D}^{-\frac{1}{2}}\mathbf{A}\mathbf{D}^{-\frac{1}{2}}
$$

### Giá trị riêng và vector riêng của ma trận Laplacian

**Định lý 3** Với độ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, giá trị riêng (eigenvalues) của ma trận Laplacian $\mathbf{L}$ của nó là không âm (non-negative)

**Định lý 4** Cho trước một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, số lượng giá trị riêng 0 của ma trận Laplacian $\mathbf{L}$ của nó bằng với số lượng thành phần liên thông trong đồ thị.

## Xử lý tín hiệu đồ thị (Graph Signal Processing)

Một đồ thị tín hiệu (graph signal) gồm một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$ và một hàm ánh xạ (mapping function) $f$ được định nghĩa trong miền đồ thị, mà ánh xạ các nút thành các giá trị thực

$$
f: \mathcal{V} \rightarrow \mathbb{R}^{N \times d}
$$

### Graph Fourier Transform

Classical Fourier Transform (Bracewell, n.d.)

$$
\hat{f}=< f(t), exp(-2\pi it\xi) >= \int_{-\infty}^{\infty}f(t)exp(-2\pi it\xi)dt
$$

phân rã một tính hiệu $f(t)$ thành một chuỗi của những mũ phức (complex exponentials) $exp(-2\pi it\xi)$ cho bất kỳ một số thực $\xi$ nào, trong đó $\xi$ có thể được xem là tần số với hàm mũ tương ứng. Những hàm mũ này là những hàm trị riêng (eigenfunctions) của toán tử Laplace một chiếu (one-dimensional Laplace operator)

$$
\nabla(exp(-2\pi it\xi)) = \frac{\partial^2}{\partial t^2}exp(-2\pi it\xi) = \frac{\partial}{\partial t}(-2\pi i\xi)exp(-2\pi it\xi)) = (-2\pi i\xi)^2exp(-2\pi it\xi)
$$

Graph Fourier Transform cho một đồ thị tính hiệu $\mathbf{f}$ trên đồ thị $\mathcal{G}$

$$
\hat{\mathbf{f}}[l] =\left<\mathbf{f}, \mathbf{u}_l\right>= \sum_{i=1}^{N}\mathbf{f}[i]\mathbf{u}_l[i]
$$

## Đồ thị phức (Complex Graphs)

Trong phần này, liệt kê một số dạng đồ thị phức (tạp) (Complex Graphs) và giới thiệu định nghĩa sơ lược về chúng

### Heterogeneous Graphs (Đồ thị bất đồng nhất)

**Định nghĩa về đồ thị bất đồng nhất** Một đồ thị bất đồng nhất (Heterogeneous Graphs) $\mathcal{G}$ bao gồm một tập các nút $$\mathcal{V} = \{v_1, ..., v_N\}$$ và một tập cách cạnh $$\mathcal{E} = \{e_1, ..., e_N\}$$ trong đó mỗi nút và mỗi cạnh được liên hệ với một kiểu (type). Gọi $\mathcal{T}_n$ đại diện cho tập kiểu (type) và $\mathcal{T}_e$ là tập kiểu cạnh. Ta có hai hàm ánh xạ (mapping function) $\phi_n: \mathcal{V} \rightarrow \mathcal{T}_n$ và $\phi_e: \mathcal{E} \rightarrow \mathcal{T}_e$, mà ánh xạ mỗi nút và mỗi cạnh thành kiểu tương ứng của chúng.

### Bipartite Graphs (Đồ thị lưỡng phân)

**Định nghĩa về đồ thị lưỡng phân** Cho một đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$, nó là lưỡng phân (bipartite) nếu và chỉ nếu $\mathcal{V} = \mathcal{V_1} \cup \mathcal{V_2}, \mathcal{V_1} \cap \mathcal{V_2} = \emptyset$ và $v_e^1 \in \mathcal{V_1}$ thì $v_e^2 \in \mathcal{V_2}$ với mọi $e=(v_e^1, v_e^2) \in \mathcal{E}$

### Multi-dimensional Graphs (Đồ thị đa chiều)

**Định nghĩa về đồ thị đa chiều** Một đồ thị đa chiều (multi-dimensional graph) bao gồm một tập các nút $$\mathcal{V} = \{v_1, ..., v_N\}$$ và một tập cách cạnh $$\{\mathcal{E}_1, ..., \mathcal{E}_D\}$$. Mỗi cạnh trong tập $\mathcal{E}_d$ mô tả kiểu quan hệ thứ $d$ giữa các nút tương ứng với chiều thứ $d$. Những quan hệ $D$ này cũng có thể khai triển bởi ma trận kề $\mathbf{A}^{(1)}, ..., \mathbf{A}^{(D)}$. Trong chiều d, ma trận kề tương ứng của nó $\mathbf{A}^{(D)} \in \mathbb{R}^{N \times N}$ mô tả cạnh $\mathcal{E}_d$ giữa các nút trong $\mathcal{V}$. Cụ thể hơn, phần tử i, j của ma trận $\mathbf{A}^{(D)}$, đại diện là $$\mathbf{A}^{(D)}_{ij}$$, bằng 1 khi đó là một cạnh giữa nút $v_i$ và $v_j$ trong chiều $d$, ngược lại thì nó bằng 0

### Signed Graphs (Đồ thị có dấu)

**Định nghĩa đồ thị có dấu** Gọi $$\mathcal{G} = \{\mathcal{V}, \mathcal{E^{+}},  \mathcal{E^{-}}\}$$ là một đồ thị có dấu, trong đó $$\mathcal{V} = \{v_1, ..., v_N\}$$ là tập $N$ nút, $ \mathcal{E^{+}} \subset \mathcal{V} \times \mathcal{V}$ và $\mathcal{E^{-}} \subset \mathcal{V} \times \mathcal{V}$ đại diện cho tập cạnh dương (positive edges) và tập cạnh âm (negative edges), tương ứng. Lưu ý rằng một cạnh chỉ có thể âm hoặc dương, tức là $\mathcal{E^{-}} \cap \mathcal{E^{-}} = \emptyset$. Những cạnh dương và âm giữa các nút có thể được mô tả bởi một ma trận kề có dấu $\mathbf{A}$, trong đó $\mathbf{A}\_{ij} = 1$ khi đây là cạnh dương giữa hai nút $v_i$ và $v_j$, $\mathbf{A}\_{ij} = -1$ là cạnh âm, còn lại thì $\mathbf{A}_{ij} = 0$

### Hypergraphs (Siêu đồ thị)

**Định nghĩa về siêu đồ thị** Đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E},  \mathbf{W}\}$$ được gọi là siêu đồ thị, trong đó $$\mathcal{V} $$ là tập $N$ nút,  $$\mathcal{E}$$ là một tập các siêu cạnh (hyperedges) và $\mathbf{W} \in \mathbb{R}^{\|\mathcal{E}\| \times \|\mathcal{E}\|}$ là ma trận dường chéo với $\mathbf{W}_{jj}$ đại diện cho trọng số của siêu cạnh $e_j$. Siêu đồ thị $\mathcal{G}$ có thể mô tả bởi một ma trận liên thuộc (incidence matrix) $\mathbf{H} \in \mathbb{R}^{\|\mathcal{V}\| \times \|\mathcal{E}\|}$, trong đó $\mathbf{H}\_{ij} = 1$ chỉ khi nút $v_i$ liên thuộc với cạnh $e_j$. Với một nút $v_i$, bậc của nó được định nghĩa

$$
d(v_i) = \sum_{j=1}^{|\mathcal{E}|}\mathbf{H}_{i, j}
$$

thì bậc cho một siêu cạnh được định nghĩa

$$
d(v_i) = \sum_{j=1}^{|\mathcal{V}|}\mathbf{H}_{i, j}
$$

Hơn nữa, ta sử dụng $\mathbf{D}_e$ và $\mathbf{D}_v$ để chỉ những ma trận thư của bậc nút và cạnh tương ứng.

### Dynamic Graphs (Đồ thị động)

**Định nghĩa về đồ thị động** (Dynamic Graphs) Một đồ thị động $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}$$ gồm một tập các nút $$\mathcal{V} = \{v_1, ..., v_N\}$$ và một tập cách cạnh $$\mathcal{E} = \{e_1, ..., e_M\}$$ trong đó mỗi nút và/hoặc mỗi cạnh được liên hệ với một bằng một khoảng thời gian chỉ ra thời điểm mà chúng gắn kết với nhau. Một cách cụ thể, ta có hai hàm ánh xạ $\phi_v$ và $\phi_e$ ánh xạ mỗi nút và mỗi cạnh thành khoảng thời gian kết hợp của chúng.

**Định nghĩa về đồ thị động rời rạc** (Discrete Dynamic Graphs) Một đồ thị động rời rạc bao gồm $T$ đồ thị snapshots, mà mỗi quan sát cùng với sự phát triển của một đồ thị động. Một cách cụ thể hơn,  $T$ đồ thị snapshots có thể đại diện như $$\{\mathcal{G_0}, ..., \mathcal{G_T}\}$$

## Tính toán trên đồ thị (Computational Tasks on Graphs)

### Node-focused Tasks (Những tác vụ tập trung ở mức nút)

Rất nhiều nghiên cứu về những tác vụ ở mức nút của đồ thị như phân loại nút (node classification), xếp hạng nút (node ranking), dự đoán liên kết (link prediction) và nhận diện cộng đồng (community detection)

#### Node classification (Phân loại nút)

Bài toán phân loại nút: Gọi đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}$$ với tập nút là $\mathcal{V}$ và tập cạnh $\mathcal{E}$. Một số nút trong $\mathcal{V}$ được liên kết với nhãn và tập những nút được gán nhãn được đại diện là $\mathcal{V}_l \subset \mathcal{V}$. Những nút còn lại không có nhãn và tập hợp những nút chưa có nhãn này được gọi là $\mathcal{V}_u$. Cụ thể, ta có $\mathcal{V}_l \cap \mathcal{V}_u = \mathcal{V}$. Mục tiêu của phân loại nút là học một hàm ánh xạ $\phi$ bằng cách sử dụng $\mathcal{G}$ và những nhãn trong $\mathcal{V}_l$, mà có thể dự đoán dược nhãn của những nút chưa được đánh nhãn ($v \in \mathcal{V}_u$)

#### Link Prediction (Dự đoán liên kết)

Bài toán dự đoán liên kết:  Gọi đồ thị $$\mathcal{G} = \{\mathcal{V}, \mathcal{E}$$ với tập nút là $\mathcal{V}$ và tập cạnh $\mathcal{E}$. Gọi $\mathcal{M}$ là tất cả những cạnh có thể có giữa các nút trong $\mathcal{V}$. Thì, ta gọi tập bù của $\mathcal{E}$ ứng với $\mathcal{M}$ là $\mathcal{E}' = \mathcal{M} \setminus\mathcal{E}$. Tập $\mathcal{E}$ chứa những cạnh chưa quan sát thấy giữa các nút. Mục tiêu của tác vụ dự đoán liên kết là dự đoán những cạnh mà có khả năng tồn tại. Cụ thể, một điểm số có thể được gán cho mỗi cạnh trong $\mathcal{E}'$. Nó chỉ ra rằng một cạnh có thể tồn tại hay sẽ có thể xuất hiện trong tương lai.

### Graph-focused Tasks (Những tác vụ tập trung ở mức đồ thị)

#### Graph Classification (Phân loại đồ thị)

Bài toán phân loại đồ thị (Graph Classification): Cho một tập các đồ thị được gán nhãn $\mathcal{D} = {\mathcal{G}_i, y_i}$, với $y_i$ là nhãn của đồ thị $\mathcal{G}_i$, mục tiêu của phân loại đồ thị là học một hàm ánh xạ $\phi$ với $\mathcal{D}$ mà có thể dự đoán nhãn của những đồ thị chưa được gán nhãn.

## Tài liệu tham khảo

Các bạn có thể đọc thêm tài liệu dưới đây để có thể nghiên cứu chi tiết hơn chứng minh và Deep Learning trên đồ thị (Graphs)

\[1\] Yiqi Wang, Wei Jin, Yao Ma and Jiliang Tang. "[Deep Learning on Graphs](https://cse.msu.edu/~mayao4/dlg_book/)"
