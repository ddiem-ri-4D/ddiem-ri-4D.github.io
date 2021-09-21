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

### Hierarchical Clustering

### Non-Hierarchical Clustering
