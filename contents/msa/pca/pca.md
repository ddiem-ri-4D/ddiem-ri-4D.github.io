---
layout: single
permalink: /content/msa/pca/principal_components_analysis
title: "[MSA] Principal Components Analysis"
author_profile: true
toc: true
comments: True
---
Phần trình bày về phương pháp phân tích thành phần chính - Principal Components Analysis Methods

## 1) Động lực nghiên cứu khoa học

- Tinh giảm dữ liệu là một trong những tác vụ của bài toán khai thác dữ liệu
- Một vấn đề thường gặp là dữ liệu thường rất nhiều chiều (lớn = phức tạp), điều đó gây khó khăn cho việc lưu trữ, phân tích, biểu diễn và giải thích dữ liệu
- Phương pháp phân tích thành phần chính (Principal Components Analysis) là một kỹ thuật tinh giảm dữ liệu được sử dụng phổ biến

## 2) Phát biểu bài toán

Phân tích thành phần chính (Principal Components Analysis - PCA) tìm những tổ hợp tuyến tính (linear combinations) của các biến mà có thể biểu diễn tốt nhất cấu trúc hiệp phương sai (covariation structure) của các biến này

PCA có 2 mục đích
- Mục đích thứ nhất: Data reduction - Giảm chiều dữ liệu, tức là biểu diễn phương sai giữa $p$ biến bằng cách sử dụng $r < p$ tổ hợp tuyến tính
- Mục đích thứ hai: Data interpretation - Diễn dịch dữ liệu, tức là tìm những đặc trưng (features) (ví dụ những thành phần chính) mà là quan trong cho việc biểu diễn hiệp phương sai (covariation)

Ma trận dữ liệu (data matrix)

$$
\mathbf{X} =
\begin{bmatrix}
x_{11} & x_{12} & ... & x_{1p} \\
x_{21} & x_{22} & ... & x_{2p} \\
x_{31} & x_{32} & ... & x_{3p} \\
.. & ... & ... & ... \\
x_{n1} & x_{n2} & ... & x_{np} \\
\end{bmatrix}
$$

Trong đó $x_{ij}$ là biến thứ j được thu nhặc từ đối tượng thứ i
- đối tượng là các dòng
- biến là các cột

Ma trận hiệp phương sai (Covariance matrix)

$$
\mathbf{\Sigma} =
\begin{bmatrix}
\sigma_{11} & \sigma_{12} & ... & \sigma_{1p} \\
\sigma_{21} & \sigma_{22} & ... & \sigma_{2p} \\
\sigma_{31} & \sigma_{32} & ... & \sigma_{3p} \\
.. & ... & ... & ... \\
\sigma_{n1} & \sigma_{n2} & ... & \sigma_{np} \\
\end{bmatrix}
$$

Trong đó
- $\sigma_{ij} = E()[X_j - \mu_j]^2)$ là phương sai quần thể (population variance) của biến thứ $j$
- $\sigma_{jk} = E([X_j - \mu_j][X_k - \mu_k])$ là hiệp phương sai quần thể (population covariance) giữa biến thứ $j$ và $k$
- $\mu_j = E(X_j)$ là trung bình quần thể (population mean) của biến thứ $j$

Hiệp phương sai mẫu (Sample covariance)

$$
\mathbf{S} =
\begin{bmatrix}
s_{1}^2 & s_{12} & ... & s_{1p} \\
s_{21} & s_{2}^2 & ... & s_{2p} \\
s_{31} & s_{32} & ... & s_{3p} \\
.. & ... & ... & ... \\
s_{n1} & s_{n2} & ... & s_{p}^2 \\
\end{bmatrix}
$$

Trong đó:
- $s_j^2 = \frac{1}{n-1}\sum_{i=1}^n(x_{ij} - \bar{x_j})^2$ là phương sai mẫu (sample variance) của biến thứ $j$
- $s_{jk} = \frac{1}{n-1}\sum_{i=1}^n(x_{ij} - \bar{x_j})(x_{ik} - \bar{x_k})$ là hiệp phương sai mẫu (sample covariance) giữa biến thứ $i$ và $k$
- $\bar{x_j} = \frac{1}{n}\sum_{i=1}^nx_{ij}$ là trung bình mẫu (sample mean) của biến thứ $j$

Bên cạnh đó, có thể tính toán (sample) ma trận hiệp phương sai (covariance matrix) như sau

$$
\mathbf{S} = \frac{1}{n - 1}\mathbf{X}'_c\mathbf{X}_c
$$

Trong đó: $\mathbf{X}_c = \mathbf{X} - \mathbf{1}_n\bar{\mathbf{x}'} = \mathbf{C}\mathbf{X}$
- $\mathbf{x}' = (\bar{x}_1, \bar{x}_2, ..., \bar{x}_p)$
- $\mathbf{C} = \mathbf{I}_n - n^{-1}\mathbf{1}_n\mathbf{1'}_n$

$$
\mathbf{X}_c =
\begin{bmatrix}
x_{11} - \bar{x}_1 & x_{12} - \bar{x}_2 & ... & x_{1p} - \bar{x}_p \\
x_{21} - \bar{x}_1 & x_{22} - \bar{x}_2 & ... & x_{2p} - \bar{x}_p \\
x_{31} - \bar{x}_1 & x_{32} - \bar{x}_2 & ... & x_{3p} - \bar{x}_p \\
.. & ... & ... & ... \\
x_{n1} - \bar{x}_1 & x_{n2} -\bar{x}_2 & ... & x_{np} - \bar{x}_p \\
\end{bmatrix}
$$

Ma trận tương quan quần thể (Population correlation matrix)

$$
\mathbf{R} =
\begin{bmatrix}
1 & \rho_{12} & ... & \rho_{1p} \\
\rho_{21} & 1 & ... & \rho_{2p} \\
\rho_{31} & \rho_{32} & ... & \rho_{3p} \\
.. & ... & ... & ... \\
\rho_{n1} & \rho_{n2} & ... & 1 \\
\end{bmatrix}
$$

Trong đó

$$
\rho_{jk} = \frac{\sigma_{jk}}{\sqrt{\sigma_{jj}\sigma}_{kk}}
$$

là hệ số tương quan Person (Pearson correlation coefficient) giữa biến $X_j$ và $X_k$

Và ma trận tương quan mẫu (Sample correlation matrix) có dạng như sau

$$
\mathbf{R} =
\begin{bmatrix}
1 & r_{12} & ... & r_{1p} \\
r_{21} & 1 & ... & r_{2p} \\
r_{31} & r_{32} & ... & r_{3p} \\
.. & ... & ... & ... \\
r_{n1} & r_{n2} & ... & 1 \\
\end{bmatrix}
$$

Trong đó

$$
r_{jk} = \frac{s_{jk}}{s_js_k}= \frac{\sum_{i=1}^n(x_{ij}-\bar{x}_j)(x_{ik}-\bar{x}_k)}{\sqrt{\sum_{i=1}^n(x_{ij}-\bar{x}_j)^2}\sqrt{\sum_{i=1}^n(x_{ik}-\bar{x}_k)^2}}
$$

là hệ số tương quan Person (Pearson correlation coefficient) giữa biến $\mathbf{x}_j$ và $\mathbf{x}_k$

Ta có thể tính toán ma trận tương quan quần thể (mẫu) như sau

$$
\mathbf{R} = \frac{1}{n-1}\mathbf{X}'_s\mathbf{R}_s
$$

Trong đó: $\mathbf{X}_s = \mathbf{C}\mathbf{X}\mathbf{D}^{-1}$
- $\mathbf{C} = \mathbf{I}_n - n^{-1}\mathbf{1}_n\mathbf{1}'_n$ đại diện cho trung tâm ma trận (centering matrix)
- $\mathbf{D} = diag(s_1, ..., s_p)$ là diện ma trận co dãn đường chéo (diagonal scaling matrix)

$$
\mathbf{X}_s =
\begin{bmatrix}
(x_{11} - \bar{x}_1)/s_1 & (x_{12} - \bar{x}_2)/s_2 & ... & (x_{1p} - \bar{x}_p)/s_p \\
(x_{21} - \bar{x}_1)/s_1 & (x_{22} - \bar{x}_2)/s_2 & ... & (x_{2p} - \bar{x}_p)/s_p \\
x_{31} - \bar{x}_1 & x_{32} - \bar{x}_2 & ... & x_{3p} - \bar{x}_p \\
.. & ... & ... & ... \\
(x_{n1} - \bar{x}_1)/s_1 & (x_{n2} -\bar{x}_2)/s_2 & ... & (x_{np} - \bar{x}_p)/s_p \\
\end{bmatrix}
$$

## 3) Phương pháp

**Tổ hợp tuyến tính của các biến ngẫu nhiên**

$\mathbf{X} = (X_1, ..., X_p)'$ là một vector ngẫu nhiên với ma trận hiệp phương sai $\mathbf{\Sigma}$, trong đó $\lambda_1 \geq ... \geq \lambda_p$ là những giá trị riêng (eigenvalues) của  $\mathbf{\Sigma}$

Xem xét dạng các biến mới $Y_1, ..., Y_p$ bằng cách sử dụng $p$ tổ hợp tuyến tính của biến $X_j$

$$
\begin{gather}
Y_1 = \mathbf{b'_1X} = b_{11}X_1 + b_{21}X_2 + ... + b_{p1}X_p \\
Y_2 = \mathbf{b'_2X} = b_{12}X_1 + b_{22}X_2 + ... + b_{p2}X_p \\
...
Y_p = \mathbf{b'_1X} = b_{1p}X_1 + b_{2p}X_2 + ... + b_{pp}X_p \\
\end{gather}
$$

Trong đó $\mathbf{b'}\_k = (b_{1k}, ..., b_{pk})$ là vector tổ hợp tuyến tính thứ $k$

Những thành phần chính là những tổ hợp tuyến tính không tương quan $Y_1, ..., Y_p$ mà có phương sai lớn nhất có thể

$$
\begin{gather}
\mathbf{b}_1 = \underset{||\mathbf{b}_1|| = 1}{\text{ argmax }}\{Var(\mathbf{b'}_1\mathbf{X})\}\\
\end{gather}
$$

$$
\begin{gather}
\mathbf{b}_2 = \underset{||\mathbf{b}_2|| = 1}{\text{ argmax }}\{Var(\mathbf{b'}_2\mathbf{X})\} \text{ subject to } \text{ Cov}(\mathbf{b'}_1\mathbf{X}, \mathbf{b'}_2\mathbf{X}) = 0
\end{gather}
$$


$$
\begin{gather}
\mathbf{b}_l = \underset{||\mathbf{b}_l|| = 1}{\text{ argmax }}\{Var(\mathbf{b'}_l\mathbf{X})\} \text{ subject to } \text{ Cov}(\mathbf{b'}_k\mathbf{X}, \mathbf{b'}_l\mathbf{X}) = 0 \forall k < l
\end{gather}
$$

**Giải PCA thông qua Eigenvalue Decomposition**

$$
\mathbf{\Sigma} = \mathbf{V\Lambda V'} = \sum_{k=1}^p\lambda_k\mathbf{v}_k\mathbf{v}'_k
$$

Trong đó:
- $\mathbf{V} = [\mathbf{v}_1, ..., \mathbf{v}_p]$ chứa những vector riêng
- $\Lambda = \text{diag}(\lambda_1, ..., \lambda_p)$ chứa những giá trị riêng không âm

Thu được lời giải PCA bằng cách cho $\mathbf{b}_k = \mathbf{v}_k$ với $k = 1, ..., p$

Các bước thực hiện như sau: Học những thành phần chính từ $$\{x_1, ..., x_N\}$$
- Bước 1: Tính toán vector trung bình

$$\mathbf{m} = \frac{1}{N}\sum_{k=1}^Nx_k$$

- Bước 2: Tính toán trung tâm (centering)

$$
\mathbf{A} = [x_1 - \mathbf{m}, ..., x_N - \mathbf{m}]
$$

- Bước 3: Tính toán

$$
\mathbf{S} = \sum_{k=1}^N(x_k - \mathbf{m})(x_k - \mathbf{m})^T = \mathbf{A}\mathbf{A}^T
$$

- Bước 4: Eigenvalue decomposition

$$
\mathbf{S} = \mathbf{U}^T\Sigma\mathbf{U}
$$

- Bước 5: sắp xếp các giá trị riêng và vector riêng

- Bước 6: Tìm ra cơ sở

$$
\mathbf{W} = [\mathbf{e}_1, ..., \mathbf{e}_m]
$$

- $\text{Var}(Y_k) = \text{Var}(\mathbf{v}'_k\mathbf{X}) = \mathbf{v}'_k\mathbf{\Sigma}\mathbf{v}_k = \mathbf{v}'_k\mathbf{V\Lambda V'}\mathbf{v}_k = \lambda_k$
- $\text{Cov}(Y_k, Y_l) = \text{Cov}(\mathbf{v}'_k\mathbf{X}, \mathbf{v}'_l\mathbf{X}) = \mathbf{v}'_k\mathbf{\Sigma}\mathbf{v}_l = \mathbf{v}'_k\mathbf{V\Lambda V'}\mathbf{v}_l = 0$ nếu $k \ne l$

**Tính chất của PCA**

$Y_1, ..., Y_p$ có cùng tổng phương sai như $X_1, ..., X_p$

$$
\sum_{j=1}^{p}\text{Var}(X_j) = \text{tr}(\mathbf{\Sigma}) = \text{tr}(\mathbf{V\Lambda V'}) = \text{tr}(\mathbf{\Lambda}) = \sum_{j=1}^\text{Var}(Y_j)
$$

Tỷ lệ của tổng phương sai chiếm bởi thành phần chính thứ $k$ là

$$
R_k^2 = \frac{\lambda_k}{\sum_{l-1}^p\lambda_l}
$$

nếu $\sum_{k=1}^1 R_k^2 \approx 1$ với một số $r < p$ thì ta sẽ không mất quá nhiều khi biến đổi từ các biến ban đầu sang một số (thành phần chính) biến mới

Hiệp phương sai giữa $X_j$ và $Y_k$ có dạng

$$
\text{Cov}(X_j, Y_k) = \text{Cov}(\mathbf{e'_jX}, \mathbf{v'_kX}) = \mathbf{e'_j\Sigma v_k} = \mathbf{e'_j(V\Lambda V')v_k)} = \mathbf{e'_jv_k}\lambda_k = v_{jk}\lambda_k
$$

Trong đó:
- $\mathbf{e_k}$ là vector 0 với giá trị 1 ở vị trí thứ $j$
- $\mathbf{v_k} = (v_{1k}, ..., v_{pk})'$ là vector riêng thứ $k$ của $\mathbf{\Sigma}$

$$
\text{Cor}(X_j, Y_k) = \frac{\text{Cov}(X_j, Y_k)}{\sqrt{\text{Var}(X_j)}\sqrt{\text{Var}(Y_k)}} =
\frac{v_{jk}\lambda_k}{\sqrt{\sigma_{jj}}\sqrt{\lambda_k}} = \frac{v_{ik}\sqrt{\lambda_k}}{\sqrt{\sigma_{jj}}}
$$

**Sample principal components**

Gọi $\mathbf{x_i} = (x_{í}, ..., x_{ip})'$ là vector ngẫu nhiên quan sát được, có thể ấp xỉ phân phối $(\mu, \mathbf{\Sigma})$

Xem xét dạng các biến mới $y_{i1}, ..., y_{ip}$ bằng cách sử dụng $p$ tổ hợp tuyến tính của biến $x_{ij}$

$$
\begin{gather}
y_{i1} = \mathbf{b'_1x_i} = b_{11}X_{i1} + b_{21}X_{i2} + ... + b_{p1}X_{ip} \\
y_{i2} = \mathbf{b'_2x_i} = b_{12}X_{i1} + b_{22}X_{i2} + ... + b_{p2}X_{ip} \\
...
y_{ip} = \mathbf{b'_1x_i} = b_{1p}X_{i1} + b_{2p}X_{i2} + ... + b_{pp}X_{ip} \\
\end{gather}
$$

Trong đó $\mathbf{b'}\_k = (b_{1k}, ..., b_{pk})$ là vector tổ hợp tuyến tính thứ $k$

Trung bình và phương sai mẫu của biến $y_{ik}$ là

$$
\bar{y}_k = \frac{1}{n}\sum_{i=1}^ny_{ik}=\mathbf{b'_k\bar{x}}
$$

$$
s_{y_k}^2 = \frac{1}{n-1}\sum_{i=1}^n(y_{ik} - \bar{y}_k)2 = \frac{1}{n-1}\sum_{i=1}^n(\mathbf{(b'_kx_i - b'_k\bar{x})(b'_kx_i - b'_k\bar{x})'} =  \frac{1}{n-1}\sum_{i=1}^n\mathbf{b'_k(x_i - \bar{x})(x_i - \bar{x})'b_k} = \mathbf{b'_kSb_k}
$$

Hiệp phương sai giữa $y_{ik}$ và $y_{il}$

$$
s_{y_ky_l} = \frac{1}{n-1}\sum_{i=1}^n(y_{ik} - \bar{y}_k)(y_{il} - \bar{y}_l) = \mathbf{b'_kSb_l}
$$

Những thành phần chính là những tổ hợp tuyến tính không tương quan $y_{i1}, ..., Y_{ip}$ mà có phương sai lớn nhất có thể

$$
\begin{gather}
\mathbf{b}_1 = \underset{||\mathbf{b}_1|| = 1}{\text{ argmax }}\{Var(\mathbf{b'}_1\mathbf{X})\}\\
\end{gather}
$$

$$
\begin{gather}
\mathbf{b}_2 = \underset{||\mathbf{b}_2|| = 1}{\text{ argmax }}\{Var(\mathbf{b'}_2\mathbf{X})\} \text{ subject to } \text{ Cov}(\mathbf{b'}_1\mathbf{X}, \mathbf{b'}_2\mathbf{X}) = 0
\end{gather}
$$


$$
\begin{gather}
\mathbf{b}_l = \underset{||\mathbf{b}_l|| = 1}{\text{ argmax }}\{Var(\mathbf{b'}_l\mathbf{X})\} \text{ subject to } \text{ Cov}(\mathbf{b'}_k\mathbf{X}, \mathbf{b'}_l\mathbf{X}) = 0 \forall k < l
\end{gather}
$$

Sử dụng Eigenvalue decomposition

$$
\mathbf{\Sigma} = \mathbf{\hat{V}\hat{\Lambda} \hat{V}'} = \sum_{k=1}^p\hat{\lambda}_k\mathbf{\hat{v}}_k\mathbf{\hat{v}}'_k
$$

Trong đó:
- $\mathbf{\hat{V}} = [\mathbf{\hat{v}}_1, ..., \mathbf{\hat{v}}_p]$ chứa những vector riêng
- $\hat{\Lambda} = \text{diag}(\hat{\lambda}_1, ..., \hat{\lambda}_p)$ chứa những giá trị riêng không âm

Thu được lời giải PCA bằng cách cho $\mathbf{b}_k = \mathbf{\hat{v}}_k$ với $k = 1, ..., p$
- $s_{y_k}^2 = \mathbf{\hat{v}}'_k\mathbf{\hat{\Sigma}}\mathbf{\hat{v}}_k = \mathbf{\hat{v}}'_k\mathbf{\hat{V}\hat{\Lambda}\hat{V}'}\mathbf{\hat{v}}_k = \hat{\lambda}_k$
- $s_{y_ky_l} = \mathbf{\hat{v}}'_k\mathbf{hat{\Sigma}}\mathbf{\hat{v}}_l = \mathbf{\hat{v}}'_k\mathbf{\hat{V}\hat{\Lambda} \hat{V}'}\mathbf{\hat{v}}_l = 0$ nếu $k \ne l$

## 4) Giải thuật PCA

Thuật toán PCA:

Input: $$D = \{x_1, x_2, ..., x_n\}, x_i \in R^{D}$$

Output: $W$

Bước 1. Xây dựng vector trung bình $\mu$

$$\mu = \frac{1}{n}\sum_{i=1}^{n}x_i$$

Bước 2. Xây dựng ma trận hiệp phương sai $S$

$$S = \frac{1}{n}\sum_{i=1}^{n}(x_i - \mu_i)(x_i - \mu_i)^T$$

Bước 3. Phân rã ma trận hiệp phương sai thành những cặp vector riêng và giá trị riêng

$$\{w_1, w_2, ..., w_D\}$$

và

$$\lambda_1, \lambda_2, ..., \lambda_D$$

Bước 4. Sắp xếp các giá trị riêng theo thứ tự giảm dần tương ứng với các vectors riêng

$$\{w_1, w_2, ..., w_D\}$$

và

$$\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_D$$

Bước 5. Chọn $k$ vector riêng mà tương ứng với $k$ giá trị riêng lớn nhất, với $k$ là số chiều đặc trưng mới  ($k \leq D$). Ở đây mình sẽ có một cách chọn k sao cho hợp lý với cách dựa vào threshold

$$\{w_1, w_2, ..., w_k\}$$

và

$$\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_k$$

Bước 6. Xây dưng ma trận hình chiếu $W$ từ $k$ vector riêng

$$W = [w_1, w_2, ..., w_k]^T$$

Bước 7: Ta có một phép biến đổi tuyến tính (linear transformation) $R^N \rightarrow R^k$ thực hiện giảm chiều (dimensionality reduction)

$$
\begin{bmatrix}
b_1 \\
b_2 \\
... \\
b_k \\
\end{bmatrix} =
\begin{bmatrix}
w_1^T \\
w_2^T \\
... \\
w_k^T \\
\end{bmatrix}(x- \bar{x}) = W^T(x- \bar{x})
$$

Để chọn được giá trị $k$, chúng ta có thể sử dụng tiêu chí sau:

$$\frac{\sum_{i=1}^k\lambda_i}{\sum_{i=1}^N\lambda_i} > \text{threshold}$$

Trong đó: threshold là một người mà chúng ta muốn, có thể là 0.9, 0.95

## 5) Ví dụ minh họa


Ví dụ: Cho dữ liệu

$$
X = \begin{bmatrix}
7 & 4& 6& 8& 8 &7& 5& 9 &7& 8 \\
4 &1 &3& 6& 5& 2& 3& 5& 4 &2\\
3 &8 &5 &1&7& 9& 3& 8& 5& 2
\end{bmatrix}
$$

Bước 01: Tính toán vector trung bình

$$\text{mean_vector} = [6.9, 3.5, 5.1]$$

Bước 02: Xây dựng ma trận hiệp phương sai

$$
C = \begin{bmatrix}
2.32 & 1.61 & -0.43\\
1.61 & 2.5 & -1.278\\
-0.43 & -1.278 & 7.878\\
\end{bmatrix}
$$

Bước 03: Phân rã ma trận hiệp phương sai thành những cặp vector riêng và giá trị riêng

$$w_1 = [-0.7012, 0.7075, 0.0841], \lambda_1 = 0.7499$$
$$w_2 = [0.699, 0.6609, 0.2731], \lambda_2 = 3.6761$$
$$w_3 = [-0.1376, -0.2505, 0.9583], \lambda_3 = 8.2739$$

Bước 04: Sắp xếp các giá trị riêng theo thứ tự giảm dần tương ứng với các vectors riêng

$$w_3 = [-0.1376, -0.2505, 0.9583], \lambda_3 = 8.2739$$
$$w_2 = [0.699, 0.6609, 0.2731], \lambda_2 = 3.6761$$
$$w_1 = [-0.7012, 0.7075, 0.0841], \lambda_1 = 0.7499$$

Bước 05: Chọn $k=2$ vector riêng mà tương ứng với $k$ giá trị riêng lớn nhất, với $k$ là số chiều đặc trưng mới  ($k \leq D$). Ở đây mình sẽ có một cách chọn k sao cho hợp lý với cách dựa vào threshold

$$w_3 = [-0.1376, -0.2505, 0.9583], \lambda_3 = 8.2739$$
$$w_2 = [0.699, 0.6609, 0.2731], \lambda_2 = 3.6761$$

Bước 06: Xây dưng ma trận hình chiếu $W$ từ $k=2$ vector riêng

$$W =
\begin{bmatrix}
-0.1376 & 0.699\\
-0.2505 & 0.6609\\
0.9583 & 0.2731\\
\end{bmatrix}
$$

Bước 7: Giảm chiều dữ liệu

$$
\begin{bmatrix}
b_1 \\
b_2 \\
... \\
b_k \\
\end{bmatrix} =
\begin{bmatrix}
w_1^T \\
w_2^T \\
... \\
w_k^T \\
\end{bmatrix}(x- \bar{x}) = W^T(X- \bar{X})
$$

$$
\begin{bmatrix}
-0.1376 & -0.2505 & 0.9583\\
0.699 & 0.6609 & 0.2731
\end{bmatrix}
\begin{bmatrix}
0.1 & -2.9 & -0.9 & 1.1 & 1.1 & 0.1 & -1.9 & 2.1 & 0.1 & 1.1\\
0.5 & -2.5 & -0.5 & 2.5 & 1.5 & -1.5 & -0.5 & 1.5 & 0.5 & -1.5\\
-2.1 & 2.9 & -0.1 & -4.1 & -1.9 & -3.9 & -2.1 & 2.9 & -0.1 & -3.1\\
\end{bmatrix}
$$
$$
 =
\begin{bmatrix}
-2.15 & 3.80 & 0.15 & -4.7 & 1.29 & 4.09 & -1.63 & 2.11 & -0.23 & -2.75\\
-0.17 & -2.89 & -0.999 & 1.30 & 2.28 & 0.14 & -2.23 & 3.25 & 0.37 & -1.07\\
\end{bmatrix}
$$

Tính $\hat{X}$

$$\hat{X} = W^T.Y + \bar{X}
$$
$$
=\begin{bmatrix}
7.075 & 4.3582 & 6.1891 & 8.4573 & 8.3152 & 6.4364 & 5.5633 & 8.8818 & 7.1931 & 6.5306\\
3.9244 & 0.6388 & 2.8094 & 5.5389 & 4.6822 & 2.5682 & 2.4320 & 5.1129 & 3.8054 & 3.4814 \\
2.9910 & 7.9570 & 4.9773& 0.9451& 6.9622& 9.6076& 2.9324& 8.0142 &4.9768 &7.1762\\
\end{bmatrix}
$$

$$MSE = \frac{1}{10}\sum_{i=1}^{10}(X_i - \hat{X}_i)^2 = 0.67493$$

## Tài liệu tham khảo
