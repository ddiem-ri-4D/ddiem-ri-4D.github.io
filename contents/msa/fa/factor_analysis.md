---
layout: single
permalink: /content/msa/fa/factor_analysis
title: "[MSA] Factor Analysis"
author_profile: true
toc: true
comments: True
---
Phần trình bày về phương pháp phân tích dữ kiện - Factor Analysis Methods

## 1) Động lực nghiên cứu khoa học
Phân tích dữ kiện (Factor Analysis) là một **phương pháp thống kê** dùng để mô tả sự biến
thiên của những biến có tương quan được quan sát bằng một số nhỏ hơn các biến không quan
sát được (unobservable/latent variables) gọi là nhân tố (factors)

Nó giả định rằng cấu trúc hiệp phương sai (covariation structure) giữa một tập các biến có thể được biểu diễn thông qua một tổ hợp tuyến tính (linear combination) của những biến chưa quan sát được (tiềm ẩn)

Phân tích dữ kiện (Factor Analysis) có ba mục đích chính:
- Tinh giảm dữ liệu - Data reduction: tức là biểu diễn phương sai giữa $p$ biến bằng cách sử dụng $r < p$ tổ hợp tuyến tính
- Diễn dịch dữ liệu - Data interpretation: tức là tìm những đặc trưng (features) (ví dụ những nhân tố - factors) mà là quan trong cho việc biểu diễn hiệp phương sai (covariation)
- Kiểm tra giả thuyết - Theory testing: xác định xem cấu trúc nhân tố giả thuyết (hypothesized factor structure) có phù hợp với dữ liệu quan sát được không (confirmatory FA)

So sánh điểm khác biệt giữa Factor Analysis (FA) và Principal Components Analysis (PCA)

Về điểm giống nhau, cả hai đều cố gắp biểu diễn hiệp phương sai (covariation) giữa các biến thông qua những tổ hợp tuyến tính của những biến khác

Về điểm khác nhau, hai phương pháp tiếp cận này có những điểm khác biệt rõ ràng
- FA giả định một mô hình thống kê (statistical model) mà mô tả được hiệp phương saio trong những biến quan sát được thông qua những tổ hợp tuyến tính của những biến tiềm ẩn (latent variables) => nó đề cập đến một mô hình thống kê
- PCA tìm kiếm những tổ hợp tuyến tính không tương quan (uncorrelated linear combinations) của những biến quan sát được mà biểu diễn phương sai lớn nhất có thể (không có những biến tiềm ẩn trong phương pháp của PCA) => nó đề cập đến phân rã trị riêng (eigenvalue decomposition) của một ma trận hiệp phương sai (covariance matrix) hay một ma trận tương quan (correlation matrix)

## 2) Phát biểu bài toán

### Mô hình nhân tố với m nhân tố chung (common factors)

Cho $\mathbf{X} = (X_1, ..., X_p)'$ là một vector ngẫu nhiên có vector trung bình $\mu$ và ma trận hiệp phương sai $\mathbf{\Sigma}$

Mô hình Factor Analsysis giả định rằng

$$
\mathbf{X} = \mu + \mathbf{L}\mathbf{F} + \mathbf{\epsilon}
$$

$$
\begin{gather}
\mathbf{X}_1 = \mu_1 + \mathbf{L}_{11}\mathbf{F}_1 \mathbf{L}_{12}\mathbf{F}_2 + ... + \mathbf{L}_{1m}\mathbf{F}_m + \mathbf{\epsilon}_1\\
\mathbf{X}_2 = \mu_2 + \mathbf{L}_{21}\mathbf{F}_1 \mathbf{L}_{22}\mathbf{F}_2 + ... + \mathbf{L}_{2m}\mathbf{F}_m + \mathbf{\epsilon}_2\\
...\\
\mathbf{X}_p = \mu_p + \mathbf{L}_{p1}\mathbf{F} \mathbf{L}_{p2}\mathbf{F}_2 + ... + \mathbf{L}_{pm}\mathbf{F}_m + \mathbf{\epsilon}_p\\
\end{gather}
$$

Trong đó
- $$\mathbf{L} = \{l_{jk}\}_{p \times m}$$ đại diện cho ma trận tải nhân tố (factor loading matrix), $l_{jk}$ là hệ số tải của biến thứ $j$ trên nhân tố chung (common factor) thứ $k$
- $\mathbf{F} = (F_1, ..., F_m)'$ đại diện cho vector điểm nhân tố tiềm ẩn (latent factor score vector), $F_k$ là điểm (score) trên nhân tố chung (common factor) thứ $k$
- $\mathbf{\epsilon} = (\epsilon_1, ..., \epsilon_p)'$ đại diện cho vector lỗi tiềm ẩn (latent error term vector), $\epsilon_j$ là nhân tố cụ thể thứ $j$

Với quá nhiều biến cần xác định trong mô hình trên, việc xác định mô hình nhân tố là không khả thi. Tuy nhiên ta sẽ giả định về vector ngẫu nhiên $\mathbf{F}$ và $\mathbf{\epsilon}$ thì có khả năng mô hình trên có thể suy ra một số quan hệ về hiệp phương sai mà ta có thể kiểm tra

### Mô hình nhân tố trực giao giả định (Orthogonal Factor Model Assumptions)

Mô hình nhân tố trực giao giả định có dạng

$$
\mathbf{X} = \mu + \mathbf{L}\mathbf{F} + \mathbf{\epsilon}
$$

Về hình dạng, nó khá là giống với mô hình nhân tố với m nhân tố chung (common factors), nhưng có thêm những giả định sau:
- $\mathbf{F} \sim (\mathbf{0}, \mathbf{I}_m)$, tức là những nhân tố tiềm ẩn có trung bình bằng không, phương sai đơn vị (unit variance) và không có tương quan
- $\mathbf{\epsilon} \sim (\mathbf{0}, \Psi)$, $\Psi = \text{diag}(\psi_1, ..., \psi_p)$ với $\psi_i$ đại diện cho phương sai cụ thể thứ $j$
- $\epsilon_j$ và $F_k$ độc lập với nhau cho mọi cặp $j, k$

### Mô hình nhân tố trực giao có thể suy ra cấu trúc ma trận hiệp phương sai của $\mathbf{X}$

Cấu trúc hiệp phương sai được suy ra cho $\mathbf{X}$

$$
\begin{gather}
\text{Var}(\mathbf{X}) = E[(\mathbf{X} - \mu)(\mathbf{X} - \mu)']\\
= E[(\mathbf{L}\mathbf{F} + \mathbf{\epsilon})(\mathbf{L}\mathbf{F} + \mathbf{\epsilon})']\\
= E[\mathbf{L}\mathbf{F}\mathbf{F}'\mathbf{L}'] + E[\mathbf{L}\mathbf{F}\mathbf{\epsilon}'] + E[\mathbf{\epsilon}\mathbf{F}'\mathbf{L}'] + E[\mathbf{\epsilon}\mathbf{\epsilon}']\\
= \mathbf{L}E[\mathbf{F}\mathbf{F}']\mathbf{L}' + \mathbf{L}E[\mathbf{F}\mathbf{\epsilon}'] + E[\mathbf{\epsilon}\mathbf{F}']\mathbf{L}' + E[\mathbf{\epsilon}\mathbf{\epsilon}']\\
= \mathbf{L}\mathbf{L}' + \Psi
\end{gather}
$$

Trong đó

$$
E[\mathbf{F}\mathbf{F}'] = \mathbf{I}_m, E[\mathbf{F}\mathbf{\epsilon}'] = \mathbf{0}_{m \times p}, E[\mathbf{\epsilon}\mathbf{F}'] = \mathbf{0}_{p \times m}, E[\mathbf{\epsilon}\mathbf{\epsilon}'] = \Psi
$$

Suy ra hiệp phương sai giữa $\mathbf{X}$ và $\mathbf{F}$ có dạng

$$
\text{Cov}(\mathbf{X}, \mathbf{F}) = E[(\mathbf{X} - \mu)\mathbf{F}'] = E[(\mathbf{L}\mathbf{F} + \mathbf{\epsilon})\mathbf{F}'] = \mathbf{L}
$$

### Phương sai được biểu diễn bởi những nhân tố chung

Một phần của phương sai của biến thứ $j$ được biểu diễn m nhân tố chung được gọi là **communality** của biến thứ $j$

$$
\begin{gather}
\underbrace{\sigma_{jj}}_{\text{Var}(X_j)} = \underbrace{l_{j1}^2 + l_{j2}^2 + ... + l_{jm}^2}_\text{communality} + \underbrace{\psi_{j}}_\text{uniqueness} \\
= \underbrace{(\mathbf{L}\mathbf{L}')_{jj}}_\text{communality} + \underbrace{\psi_{j}}_\text{uniqueness}
\end{gather}
$$

Trong đó
- $\sigma_{jj}$ là phương sai của $X_j$, tức là phần tử đường chéo thứ $j$ của $\mathbf{\Sigma}$
- $(\mathbf{L}\mathbf{L}')\_{jj} = l_{j1}^2 + l_{j2}^2 + ... + l_{jm}^2$ là communality của $X_j$
communality của $X_j$, là tổng bình phương tải cho $X_j$
- $\psi_j$ là phương sai cụ thể (hay uniqueness) của $X_j$

Một phần phương sai của $X_j$ được cống hiến từ tổng bình phương của từng hệ số tải nhân tố,
một phần được cống hiến từ phương sai của biến ngẫu nhiên độ lỗi.S

Hay nói cách khác phương sai và hiệp phương sai đến từ các biến ngẫu nhiên của vector ngẫu nhiên $\mathbf{X}$ có thể tái tạo lại từ mô hình nhân tố trực giao.

Mô hình nhân tố giả định rằng có $p$ giá trị phương sai và $p(p-1)/2$ giá trị hiệp phương sai của ma trận hiệp phương sai của $\mathbf{X}$ mà ta có thể tái tạo được từ $pm$ biến của hệ số tải $\mathbf{L}$ và $p$ phương sai của độ lỗi $\epsilon$. Khi $m = p$, mỗi ma trận hiệp phương sai $\mathbf{\Sigma}$ có thể biểu diễn chính xác là $\mathbf{L}\mathbf{L}'$. Khi $m < p$, mô hình cung giải thích một cách đơn giản hơn ma trận hiệp phương sai của $\mathbf{X}$ bằng ít biến hơn

Tuy nhiên, khi số lượng nhân tố $m$ nhỏ hơn $p$ rất nhiều lần thì mô hình không thể phân tích dữ kiện ra được dạng $\mathbf{L}\mathbf{L}' + \mathbf{\Psi}$

Nếu $\mathbf{R}$ là một ma trận trực giao $p \times p$, vì vậy $\mathbf{R}\mathbf{R}' = \mathbf{R}'\mathbf{R} = \mathbf{I}_p$

Ta có

$$
\mathbf{X} - \mu = \mathbf{LF} + \epsilon = \mathbf{L}\mathbf{R}\mathbf{R}'\mathbf{F} + \epsilon = \mathbf{L}^{*}\mathbf{F}^{*} + \epsilon
$$

Với $$\mathbf{L}^{*} = \mathbf{L}\mathbf{R}$$ và $$\mathbf{F}^{*}=\mathbf{R}'\mathbf{F}$$

Khi đó $$E(\mathbf{F}^{*}) = \mathbf{R}'E(\mathbf{F}) = 0$$ và $$\text{Cov}(\mathbf{F}^{*}) = \mathbf{R}'\text{Cov}(\mathbf{F})\mathbf{R} = \mathbf{R}\mathbf{R}' = \mathbf{I}_p$$

Hay nói cách khác nhân tố $\mathbf{F}$ và $\mathbf{F}^{\*} = \mathbf{R}'\mathbf{F}$ giống nhau về các đặc tính thống kê mà ban đầu chúng ta giả sử, và mặc dù ma trận hệ số tải $\mathbf{L}^{*}$ khác với $\mathbf{L}$
nhưng cả hai đều sinh ra ma trận hiệp phương sai như nhau bởi vì:

$$
\mathbf{\Sigma} = \mathbf{L}\mathbf{L}' + \mathbf{\Psi} = \mathbf{L}\mathbf{R}\mathbf{R}'\mathbf{L}' + \mathbf{\Psi} = (\mathbf{L}^{*})(\mathbf{L}^{*}) + \mathbf{\Psi}
$$

Điều này sẽ dân tới khái niệm "xoay nhân tố" (factor rotation).

## 3) Phương pháp

### Phương pháp phân tích thành phần chính (Principal Components) cho phân tích dữ kiện

Những tham số cần quan tâm là tải nhân tố (factor loadings) $\mathbf{L}$ và phương sai cụ thể trên đường chéo của $\mathbf{\Psi}$

Với $m < p$ nhân tố chung, lời giải PCA ước lượng $\mathbf{L}$ và $\mathbf{\Psi}$:

$$
\hat{\mathbf{L}} = [\lambda_1^{1/2}\mathbf{v}_1, \lambda_2^{1/2}\mathbf{v}_2, ..., \lambda_m^{1/2}\mathbf{v}_m]
$$

$$
\hat{\psi} = \sigma_{jj} - \sum_{k=1}^ml_{jk}^2
$$

Trong đó $\mathbf{\Sigma = V\Lambda V'}$ là phân rã trị riêng của $\mathbf{\Sigma}$ và $\sum_{k=1}^ml_{jk}^2$ là estimated communality của biến thứ $j$

Tỷ lệ của tổng phương sai được biểu diễn bởi nhân tố thứ $k$

$$
R_k^2 = \frac{\sum_{j=1}^p\hat{l}_{jk}^2}{\sum_{j=1}^p\sigma_{jj}} = \frac{(\lambda_k^{1/2}\mathbf{v}_k)'(\lambda_k^{1/2}\mathbf{v}_k)}{\sum_{j=1}^p\sigma_{jj}} = \frac{\lambda_k}{\sum_{j=1}^p\sigma_{jj}}
$$

### Iterated Principal Axis Factoring Method

Giả sử ta áp dụng FA vào một sample correlation matrix $\mathbf{R}$

$$
\mathbf{R - \Psi = LL'}
$$

và ta có một số ước lượng ban đầu của một phương sai cụ thể $\hat{\psi}_j$

Thuật toán iterated principal axis factoring

Bước 01: Tính toán $\widetilde{\mathbf{R}} = \mathbf{R} - \hat{\mathbf{\Psi}}$ với những ước lượng $\hat{\psi}_j$ hiện tại cho trước

Bước 02: Cập nhật

$$\widetilde{\mathbf{L}} = [\widetilde{\lambda}_1^{1/2}\widetilde{\mathbf{v}}_1, \widetilde{\lambda}_2^{1/2}\widetilde{\mathbf{v}}_2, ..., \widetilde{\lambda}_m^{1/2}\widetilde{\mathbf{v}}_m]$$

 trong đó $\widetilde{\mathbf{R}} = \widetilde{\mathbf{V}}\widetilde{\mathbf{\Lambda}}\widetilde{\mathbf{V}}'$ là phân rã trị riêng của $\widetilde{\mathbf{R}}$

Bước 03: Cập nhật

$$\hat{\psi}_j = 1 - \sum_{k=1}^{m}\widetilde{l}_{jk}^2$$

### Ước lượng triển vọng cực đại (Maximum Likelihood Estimation) cho cho phân tích dữ kiện

Giả sử $\mathbf{x}_i \sim \mathcal{N}(\mu, \mathbf{LL}' + \mathbf{\Psi})$ là một vector chuẩn đa biến

Log-likelihood function cho một mẫu gồm $n$ quan sát có dạng

$$
LL(\mu,  \mathbf{L},  \mathbf{\Psi}) = -\frac{np\text{log}(2\pi)}{2} + \frac{np\text{log}(|\Sigma^{-1}|)}{2} - \frac{\sum_{i=1}^n(\mathbf{x}_i - \mu)'\Sigma^{-1}(\mathbf{x}_i - \mu)}{2}
$$

Trong đó

$$
\mathbf{\Sigma} = \mathbf{LL}' +  \mathbf{\Psi}
$$

Sử dụng iterative algorithm để cực đại $LL$

Lợi ích của ML: có một quan hệ đơn giản giữa FA cho $\mathbf{S}$ (co-variance matrix) và $\mathbf{R}$ (correlation matrix)
- Nếu $\hat{\theta}$ là MLE của $\theta$, thì $g(\hat{\theta})$ là MLE của $g(\theta)$

### Xoay nhân tố (Factor rotation)

#### Xoay điểm trong hai chiều

Giả sử ta có $\mathbf{z} = (x, y)' \in \mathbb{R}^2$, tức là những điểm trong không gian Euclidean 2 chiều

Một phép quay trực giao (orthogonal rotation) $2 \times 2$ của $(x, y)$ có dạng

$$
\begin{bmatrix} x^{*} \\ y^{*} \end{bmatrix}
=
\begin{bmatrix}
\text{cos}(\theta) & -\text{sin}(\theta)\\
\text{sin}(\theta) & \text{cos}(\theta)
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

quay $(x, y)$ ngược chiều kim đồng hồ xung quanh điểm gốc một góc $\theta$

$$
\begin{bmatrix} x^{*} \\ y^{*} \end{bmatrix}
=
\begin{bmatrix}
\text{cos}(\theta) & \text{sin}(\theta)\\
-\text{sin}(\theta) & \text{cos}(\theta)
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

quay $(x, y)$ theo chiều kim đồng hồ xung quanh điểm gốc một góc $\theta$

Một ma trận xoay $2 \times 2$

$$
\mathbf{R}
= \begin{bmatrix}
\text{cos}(\theta) & -\text{sin}(\theta)\\
\text{sin}(\theta) & \text{cos}(\theta)
\end{bmatrix}
$$

là một ma trận trực giao (orthogonal matrix) với mọi $\theta$

*Proof*

$$
\begin{gather}
\mathbf{R}'\mathbf{R} =
\begin{bmatrix}
\text{cos}(\theta) & \text{sin}(\theta)\\
-\text{sin}(\theta) & \text{cos}(\theta)
\end{bmatrix}
\begin{bmatrix}
\text{cos}(\theta) & -\text{sin}(\theta)\\
\text{sin}(\theta) & \text{cos}(\theta)
\end{bmatrix}
\end{gather}\\
=
\begin{bmatrix}
\text{cos}^2(\theta) + \text{sin}^2(\theta) & \text{cos}(\theta)\text{sin}(\theta)-\text{cos}(\theta)\text{sin}(\theta)\\
\text{cos}(\theta)\text{sin}(\theta) -  \text{cos}(\theta)\text{sin}(\theta)& \text{cos}^2(\theta) + \text{sin}^2(\theta)
\end{bmatrix}
= \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}
$$

Ở số chiều cao hơn, ta có một data matrix $\mathbf{X}$ với $p$ cột
- Những dòng của $\mathbf{X}$ tương ứng với những điểm trong không gian $p$ chiều

Một ma trận xoay trực giao $p \times p$ là một phép biến đổi tuyến tính trực giao
- $\mathbf{R}'\mathbf{R} = \mathbf{R}\mathbf{R}' = \mathbf{I}_p$
- Nếu $\widetilde{\mathbf{X}} = \mathbf{X}\mathbf{R}$ là ma trận dữ liệu đã được xoay, thì $\widetilde{\mathbf{X}}\widetilde{\mathbf{X}}' = \mathbf{X}\mathbf{X}'$
- Xoay trực giao bảo tồn quan hệ giữa các điểm

#### Factor rotation

Giả sử $\mathbf{R}$ là một ma trận xoay trực giao

$$
\mathbf{X} = \mu + \mathbf{LF} + \epsilon = \mu + \widetilde{\mathbf{L}}\widetilde{\mathbf{F}} + \epsilon
$$

Trong đó:
- Nhân tố tải đã được xoay $\widetilde{\mathbf{L}} = \mathbf{L}\mathbf{R}$
- Điểm nhân tố đã được xoay  $\widetilde{\mathbf{F}} = \mathbf{R}'\mathbf{F}$

Những phương pháp xoay nhân tố cố gắng tìm một số phép quay của kết quả FA mà có thể đưa ra một diễn giải hợp lý hơn

Cấu trúc đơn giản của Thurstone, mô tả một lời giải nhân tố lý tưởng ("ideal" factor solution)
- Mỗi dòng của $\mathbf{L}$ chứa ít nhất một số 0
- Mỗi cột của $\mathbf{L}$ chứa ít nhất một số 0
- Mỗi cặp cột của $\mathbf{L}$, nên có một biến với tải nhỏ trên chỉ một trong hai nhân tố
- Mỗi cặp cột của $\mathbf{L}$, nên có một biến với tải nhỏ trên cả hai nhân tố nếu $m \geq 4$
-  Mỗi cặp cột của $\mathbf{L}$, nên có một biến với tải lớn trên cả hai nhân tố

Nhiều phương pháp xoay nhân tố trực giao cố gắng cực đại

$$
V(\mathbf{L}, \mathbf{R} | \gamma) = \frac{1/p}\sum_{k=1}^m\left[\sum_{j=1}^p(\widetilde{l}_{jk}/\widetilde{h}_{jk})^4 - \frac{\gamma}{p}\left(\sum_{j=1}^p(\widetilde{l}_{jk}/\widetilde{h}_{jk})^2\right)^2\right]
$$

Trong đó
- $\widetilde{l}_{jk}$ là hệ số tải được xoay của biến thứ $j$ trên nhân tố $k$
- $$\widetilde{h}_{jk} = \sqrt{\sum_{k=1}^m\widetilde{l}_{jk}^2}$$ là căn bậc hai của communality cho $X_j$

Với các giá trị $\gamma$, tương ứng với tiêu chí khác nhau
- Với $\gamma = 1$ => varimax criterion
- Với $\gamma = 0$ => quartimax criterion
- Với $\gamma = m/2$ => equamax criterion
- Với $\gamma = p(m-1)/(p+m-2)$ => parsimax criterion

### Điểm nhân tố (Factor Scores)

Mô hình phân tích dữ kiện

$$
X = \mu + \mathbf{LF} + \epsilon = \mu + \begin{bmatrix}\mathbf{L} & \mathbf{I}_p\end{bmatrix}\begin{bmatrix}\mathbf{F}\\ \mathbf{\epsilon}\end{bmatrix} = \mu + \mathbf{L}^*\mathbf{F}^*
$$

Trong đó: $\mathbf{L}^\*$ là ma trận $p \times m + p$ của những nhân tố tải xác định và chung,  $\mathbf{F}^*$ là ma trận $m + p \times 1$ của những điểm nhân tố xác định và chung

Cho trước $\mu$ và $\mathbf{L}$, ta có $m + p$ thành phần chưa biết (thành phần của  $\mathbf{F}^*$) nhưng chỉ có $p$ biểu thức có sẵn để giải cho những thành phần chưa biết
- Giới hạn $m$ và cho $p \rightarrow \infty$, sự không xác định biến mất
- Với hữu hạn $p$, có vô số tổ hợp của $(\mathbf{F}, \mathbf{\epsilon})$

#### Least Squares Method

Đặt $\hat{\mathbf{L}}$ và  $\hat{\mathbf{\Psi}}$ đại diện cho ước lượng của $\mathbf{L}$ và $\mathbf{\Psi}$

Ước lượng bình phối tối tiểu có trọng số của điểm nhân tố là

$$
\hat{\mathbf{f}}_i = (\hat{\mathbf{L}}'\hat{\mathbf{\Psi}}^{-1}\hat{\mathbf{L}})\hat{\mathbf{L}}'\hat{\mathbf{\Psi}}^{-1}(\mathbf{x}_i - \bar{\mathbf{x}})
$$

Trong đó:
- $\mathbf{x}_i$ là vector của đối tượng thứ $i$ của dữ liệu
- $\bar{\mathbf{x}} = \frac{1}{n}\sum_{i=1}^n\mathbf{x}_i$ là trung bình mẫu

#### Regression Method

Sử dụng phương pháp Maximum Likelihood, phân phối kết của $(\mathbf{X} - \mu, \mathbf{F})$ là chuẩn đa biến với vector trung bình $\mathbf{0}_{p+m}$ và ma trận hiệp phương sai

$$
\mathbf{\Sigma}^{*} = \begin{bmatrix} \mathbf{LL}' + \mathbf{\Psi} & \mathbf{L} \\  \mathbf{L}' &  \mathbf{I}_m \end{bmatrix}
$$

mà chỉ ra phân phối có điều kiện của $\mathbf{F}$ được cho bởi $\mathbf{X}$
- $E(\mathbf{F}\|\ \mathbf{X})=  \mathbf{L}'(\mathbf{LL}' + \mathbf{\Psi})^{-1}(\mathbf{X} - \mu)$
- $V(\mathbf{F}\|\ \mathbf{X}) =  \mathbf{I}_m -  \mathbf{L}'(\mathbf{LL}' + \mathbf{\Psi})^{-1}\mathbf{L}$

Ước lượng hồi quy của điểm nhân tố

$$
\hat{\mathbf{f}}_i = \hat{\mathbf{L}'}(\hat{\mathbf{L}}\hat{\mathbf{L}'} + \hat{\mathbf{\Psi}})^{-1}(\mathbf{x}_i - \bar{\mathbf{x}}) = (\mathbf{I}_m + \hat{\mathbf{L'}}\hat{\mathbf{\Psi}}^{-1}\hat{\mathbf{L}})^{-1}\hat{\mathbf{L'}}\hat{\mathbf{\Psi}}^{-1}(\mathbf{x}_i - \bar{\mathbf{x}})
$$

## 4) Một vài mở rộng

### Oblique Factor Model Assumptions

Oblique FA model giả định dạng

$$
\mathbf{X} = \mu + \mathbf{LF} + \epsilon
$$

Có thêm những giả định sau:
- $\mathbf{F} \sim (\mathbf{0}, \mathbf{\Psi})$, tức là những nhân tố tiềm ẩn có trung bình bằng không, phương sai đơn vị (unit variance) và có tương quan
- $\mathbf{\epsilon} \sim (\mathbf{0}, \mathbf{\Psi})$, $\mathbf{\Psi} = \text{diag}(\psi_1, ..., \psi_p)$ với $\psi_i$ đại diện cho phương sai cụ thể thứ $j$
- $\epsilon_j$ và $F_k$ độc lập với nhau cho mọi cặp $j, k$

Cấu trúc hiệp phương sai tiềm ẩn cho $\mathbf{X}$

$$
\begin{gather}
\text{Var}(\mathbf{X}) = E[(\mathbf{X} - \mu)(\mathbf{X} - \mu)'] = E[(\mathbf{LF} + \epsilon - \mu)(\mathbf{LF} + \epsilon- \mu)']\\
= E[\mathbf{LFF'L'}] + E[\mathbf{LF\epsilon'}] + E[\mathbf{\epsilon F'L'}] + E[\mathbf{\epsilon'\epsilon}]\\
= \mathbf{L}E[\mathbf{FF}]\mathbf{L}' + \mathbf{L}E[\mathbf{F\epsilon'}] +  E[\mathbf{\epsilon F'}] \mathbf{L}' + E[\mathbf{\epsilon'\epsilon}]\\
= \mathbf{L\Phi L'} + \mathbf{\Psi}
\end{gather}
$$

Trong đó

$$
E[\mathbf{FF}] = \mathbf{\Phi}
$$

$$
E[\mathbf{F\epsilon'}] = \mathbf{0}_{m \times p}
$$

$$
E[\mathbf{\epsilon'\epsilon}] =  \mathbf{\Psi}
$$

Ám chỉ hiệp phương sai giữa $\mathbf{X}$ và $\mathbf{F}$ có dạng

$$
\text{Cov}(\mathbf{X}, \mathbf{F}) = E[(\mathbf{X} - \mu)\mathbf{F}'] =  E[(\mathbf{LF} + \epsilon)\mathbf{F}'] = \mathbf{L\Phi}
$$

Với
- $\mathbf{L}$ được gọi là factor pattern matrix
- $\mathbf{L\Phi}$ được gọi là factor structure matrix, cho biết hiệp phương sai giữa những biến quan sát được trong $\mathbf{X}$ và nhân tố tiềm ẩn trong $\mathbf{F}$

Nếu những nhân tố là trực giao, thì $\mathbf{\Phi} = \mathbf{I}_m$ và factor pattern, structure matrix là những ma trận đơn vị

Đặt $$\mathbf{\Phi} = \mathbf{V}_{\phi}\mathbf{\Lambda}_{\phi}\mathbf{V}'_{\phi}$$ đại diện cho phân rã tri riêng của $$\mathbf{\Phi}$$
- Bước 01: Định nghĩa $$\widetilde{\mathbf{L}} = \mathbf{L}\mathbf{V}_{\phi}\mathbf{\Lambda}_{\phi}^{1/2}$$ và
$$\widetilde{F} = \mathbf{\Lambda}_{\phi}^{-1/2}\mathbf{V}'_{\phi}$$ mà $$\mathbf{\Sigma} = \widetilde{\mathbf{L}}\widetilde{\mathbf{L}}' + \mathbf{\Psi}$$
- Bước 02: Khớp mô hình nhân tố trực giao để ước lượng $$\widetilde{\mathbf{L}}$$ và $\mathbf{\Psi}$
- Bước 03: Sử dụng phương pháp oblique rotation như promax, quartimin để xoay kết quả thu được

## Tài liệu tham khảo

[1] Richard Johnson Dean Wichern - Applied Multivariate Statistical Analysis -
2006-Pearson

[2] Andy Field, Jeremymiles, Zoëfield - Discovering Statistics Using R –
2012 – SAGE Publications Ltd

[3] PennSate Eberly College of Science - STAT 505 Applied Multivariate Statistical
Analysis (Online Course) -https://onlinecourses.science.psu.edu/stat505/node/74

[4] Multivariate Statistics Note - Nathaniel E. Helwig, Associate Professor of Psychology and Statistics - http://users.stat.umn.edu/~helwig/teaching.html
