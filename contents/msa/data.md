---
layout: single
permalink: /content/msa/data_cov_cor
title: "[MSA] Dữ liệu, ma trận hiệp phương sai, ma trận tương quan"
author_profile: true
toc: true
comments: True
---

## Tổ chức dữ liệu

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

## Ma trận hiệp phương sai (covariance matrix)

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

## Ma trận tương quan (Correlation matrix)

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

Giả sử $s^2_j > 0$ với mọi $j \in \{1, ..., p\}$, ta có

$$
\text{Cor}(\mathbf{x}_j, \mathbf{x}_k) = \frac{\sum_{i=1}^n(x_{ij} - \bar{x}_j)(x_{ik} - \bar{x}_k)}{\sqrt{\sum_{i=1}^n(x_{ij} - \bar{x}_j)^2}\sqrt{\sum_{i=1}^n(x_{ik} - \bar{x}_k})^2} = \begin{cases} 1 \text{ nếu } j = k \\ r_{jk} \text{ nếu } j \ne k \end{cases}
$$
