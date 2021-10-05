---
layout: single
permalink: /content/msa/clutering/clustering
title: "[MSA] Clustering"
author_profile: true
toc: true
comments: True
---
Phần trình bày về phương pháp gom nhóm - Clustering Methods

## 1) Động lực nghiên cứu khoa học

Những phương pháp gom cụm (clustering methods) cố gắng nhóm - group (hay gom cụm - cluster) những đối tượng (objects) dựa trên những luật định nghĩa tương đồng - similarity (hay khác biệt - dissimilarity) giữa những đối tượng

Phân biệt giữa gom cụm (clutering) và phân lớp (classification/discrimination)
- Clustering: nhãn của nhóm không được biết trước
- Classification: nhãn của nhóm được biết trước (thường là cho tập huấn luyện)

Mục đích thông thường trong việc gom cụm là để khám phá "nhóm tự nhiên (natural groupings)" ở hiện tại trong dữ liệu, tạo ra cấu trúc phân cấp trong dữ liệu, phát hiện những mối quan hệ giữa những đặc trưng với nhau

Trong ứng dụng, các nhóm được hình thành từ phương pháp gom nhóm có thể
được sử dụng để làm bước đầu cho các mục đích khác như:
- Tóm tắt dữ liệu
- Nén dữ liệu
- Phân đoạn ảnh
- Tìm láng giềng gần nhất

## 2) Phát biểu bài toán

Đầu vào: cho $\mathbf{X} = (X_1, ..., X_n)'$

Đầu ra: Luật gom nhóm mà thỏa tính chất
- Các phần tử trong cùng một nhóm có tính chất giống nhau (gần nhau)
- Các phần tử trong các nhóm khác nhau có tính chất khác nhau (xa nhau)

Làm sao định nghĩa "giống nhau"?, "khác nhau"?

### Xác định độ giống nhau (tương đồng) - Similarity

Cho hai vector bất kỳ $\mathbf{x} = (x_1, x_2, ..., x_p)'$ và $\mathbf{y} = (y_1, y_2, ..., y_p)'$

Bài toán: Đưa ra một số luật mà có thể đo được độ gần (closeness) hay độ gần (similarity) giữa $\mathbf{x}$ và $\mathbf{y}$

Kết quả của bài toán này sẽ dẫn tới cách mà chúng ta gom nhóm những đối tượng vào những cụm (clusters)
- Rule 1: tương quan Pearson (Pearson correlation) giữa $\mathbf{x}$ và $\mathbf{y}$
- Rule 2: Khoảng cách Euclidean giữa $\mathbf{x}$ và $\mathbf{y}$
- Rule 3: Số lượng trùng khớp, tức $\sum_{i=1}^{p}1_{x_i == y_i}$

Định nghĩa một khoảng cách thích hợp (proper distance)

Lý thuyết: Một metric (hay distance) trên một tập $\mathcal{X}$ là một hàm $d : \mathcal{X} \times \mathcal{X} \rightarrow [0, \infty)$

Gọi $d(\cdot, \cdot)$ là một khoảng cách giữa đối tượng $P$ và $Q$ và $R$ đại diện cho một đối tượng trung Lagrangian

Một độ đo khoảng cách phải thỏa mãn những tính chất
- Tính đối xứng (symmetry)

$$
d(Q, P) = d(P, Q)
$$

- Không âm (non-negativity)

$$
d(P, Q) \geq 0 \forall P, Q
$$

- (Identity of indiscernibles)

$$
d(P, Q) = 0 \text{ khi và chỉ khi } P = Q
$$

- Bất đẳng thức tam giác (triangle inequality)

$$
d(P, Q) \leq d(P, R) + d(R, Q)
$$

**Minkowski Metric và các trường hợp đặc biệt**

Minkowski Metric được định nghĩa như sau

$$
d_m(\mathbf{x}, \mathbf{y}) = \left(\sum_{i=1}^p|x_i - y_i|^m\right)^{\frac{1}{m}}
$$

trong đó $m \geq 1$ định nghĩa một khoảng cách metric đúng

Khi $m = 1$, cho ta khoảng cách Manhattan (Manhattan distance)

$$
d_1(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^{p}|x_i - y_j|
$$

Khi $m = 2$, cho ta khoảng cách Euclidean (Euclidean distance)

$$
d_2(\mathbf{x}, \mathbf{y}) = \left(\sum_{i=1}^{p}[x_i - y_j]^2\right)^{\frac{1}{2}}
$$

Khi $m = \infty$, cho ta khoảng cách Chebyshev (Chebyshev distance)

$$
d_{\infty} = max_i|x_i - y_i|
$$


## 3) Phương pháp

Các phương pháp gom nhóm dữ liệu được chia thành: gom nhóm không có cấu
trúc (Non-Hierarchical Clustering Methods), gom nhóm có cấu trúc (Hierarchical
Clustering Methods) và gom nhóm theo mô hình thống kê (Clustering Based on
Statistical Models)

### Hierarchical Clustering

Phương pháp gom nhóm có cấu trúc (Hierarchical Clustering Methods) có hai hướng tiếp cận chính

- Gom nhóm cấu trúc kết tụ (Agglomerative Hierarchical Clustering): Bắt đầu với N cluster (mỗi đối tượng là một cluster riêng biệt), sau đó gọp những đối tượng tương đồng với nhau lại, cứ lặp lại như thế cho toàn bộ đối tượng cho tất cả đều cùng thuộc cluster

- Gom nhóm cấu trúc phân chia (Divisive Hierarchical Clustering): Bắt đầu với một cluster, tất cả các đối tượng đều thuộc cluster này, sau đó phân chia những đối tượng tách biệt nhau nhất, cứ lặp lại như thế cho toàn bộ đối tượng cho tất cả đều cùng thuộc cluster của chúng

Đầu vào cho hierarchical clustering là một dissimilarity matrix có kích thước $N \times N$

$$
\mathbf{D} =
\begin{pmatrix}
d_{11} & d_{12} & ... & d_{1N}\\
d_{21} & d_{22} & ... & d_{2N}\\
... & ... & ... & ...\\
d_{N1} & d_{N2} & ... & d_{NN}\\
\end{pmatrix}
$$

Trong đó $d_{ij} = d(X_i, X_j)$ là khoảng cách giữa hai đối tượng $X_i$ và $X_j$

Gọi hai cluster như sau, $$C_X = \{X_1, ..., X_m\}$$, $$C_Y = \{Y_1, ..., Y_n\}$$

- $X_i$ là đối tượng thứ $i$ trong cluster $C_X$, với $i = 1, ...m$
- $Y_j$ là đối tượng thứ $j$ trong cluster $C_Y$, với $i = j, ...n$

Để định lượng khoảng cách giữa hai cluster, ta có thể dùng

- Liên kết đơn (Single Linkage): khoảng cách nhỏ nhất (lân cận gần nhất)

$$
d(C_X, C_Y) = \text{min}_{i, j}d(X_i, Y_j)
$$

- Liên kết đầy đủ (Complete Linkage): khoảng cách lớn nhất (lân cận xa nhất)

$$
d(C_X, C_Y) = \text{max}_{i, j}d(X_i, Y_j)
$$

- Liên kết trung bình (Average Linkage)

$$
d(C_X, C_Y) = \frac{1}{mn}\sum_{i=1}^m\sum_{j=1}^nd(X_i, Y_j)
$$


### Non-Hierarchical Clustering

Gom nhóm không có cấu trúc (Non-Hierarchical Clustering Methods) chia một tập gồm $N$ đối tượng thành $K$ nhóm tách biệt dựa trên một vài khoảng cách (hoặc dissimilarity)

Số lượng cluster $K$ có thể được biết trước hoặc có thể được ước lượng

Phương pháp K-Means

- Mục đích của phương pháp K-means là để phân dữ liệu đầu vào thành $k$ nhóm làm
sao cho tổng bình phương trong mỗi nhóm được tối thiểu hóa sử dụng hàm mục
tiêu

$$
J = \sum_{j=1}^k\sum_{x_i \in C_i}||x_i - c_i||^2
$$

Các bước của thuật toán

Bước 1: Chọn k điểm một cách ngẫu nhiên trong các điểm dữ liệu đầu vào làm tâm
của k nhóm

Bước 2: Gán các giá trị đầu vào vào các nhóm có tâm gần với mỗi điểm nhất sử
dụng hàm mục tiêu

Bước 3: Cập nhật lại các tâm bằng cách tính tổng trung bình các điểm đã được gán

Bước 4: Lặp lại 2, 3 cho đến khi không có điểm nào thay đổi
