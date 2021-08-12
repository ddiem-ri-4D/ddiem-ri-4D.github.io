---
layout: single
permalink: /content/msa/classification/lda_calculus
title: "[MSA] Trình bày LDA bằng tiếp cận Giải tích"
author_profile: true
toc: true
comments: True
---

## 1. Mục đích
- Tìm một phép biến đổi tuyến tính W tối ưu (bộ phân lớp ít lỗi nhất)
- Khoảng cách giữa các lớp với nhau là xa nhất có thể
- Khoảng cách giữa các phần tử trong cùng một lớp sau khi thực hiện phép chiếu là gần nhau nhất (tức là, dữ liệu sau khi biến đổi gom cụm lại)

## 2. Phát biểu bài toán:

*Xét bài toán phân loại 2 lớp

Đầu vào: Hai tập đã được đánh nhãn

Lớp 1:

$$X_1 = \{x_1, x_2, ..., x_{n_{1}}\}$$

Lớp 2:

$$X_2 = \{x_1, x_2, ..., x_{n_{2}}\}$$

Đầu ra:  một phép biến đổi tuyến tính 1-d $\mathbf{w}$ mà cực đại tính phân tách giữa hai lớp này

## 3. Giải bài toán:

Dựa vào đó, cần tối ưu biểu thức sau

$$
\begin{gather*}
\frac{(\mu_1 - \mu_2)^2}{s_1 + s_2} \rightarrow \text{max}
\end{gather*}
$$

Trong đó:

- $\mu_1, \mu_2$ là trung bình của dữ liệu đã biến đổi

$$
\begin{gather*}
\mu_1 = \frac{1}{n_1}\sum_{i=1}^{n_{1}}w^{T}x_i = w^{T}\bar{X_1}\\
\mu_2 = \frac{1}{n_2}\sum_{i=1}^{n_{2}}w^{T}x_i = w^{T}\bar{X_2}
\end{gather*}
$$

- $s_1, s_2$ là phương sai của dữ liệu đã biến đổi

$$
\begin{gather*}
s_1 = \sum_{i=1}^{n_{1}}(w^{T}x_i - w^{T}\bar{X_1})^2\\
s_2 = \sum_{i=1}^{n_{2}}(w^{T}x_i - w^{T}\bar{X_2})^2
\end{gather*}
$$

Ta có:

$$
\begin{gather*}
(\mu_1 - \mu_2)^2 = [w^T(\bar{X_1} - \bar{X_2})]^2\\
\Leftrightarrow (\mu_1 - \mu_2)^2  = w^T(\bar{X_1} - \bar{X_2})w^T(\bar{X_1} - \bar{X_2})\\
\Leftrightarrow (\mu_1 - \mu_2)^2  = w^T(\bar{X_1} - \bar{X_2})(\bar{X_1} - \bar{X_2})^Tw
\end{gather*}
$$

Đặt $S_b = (\bar{X_1} - \bar{X_2})(\bar{X_1} - \bar{X_2})^T$

Với phương sai:

$$
\begin{gather*}
s_1 = \sum_{i=1}^{n_{1}}(w^{T}x_i - w^{T}\bar{X_1})^2\\
= \sum_{i=1}^{n_{1}}(w^{T}x_i - w^{T}\bar{X_1})(w^{T}x_i - w^{T}\bar{X_1})\\
= \sum_{i=1}^{n_{1}}w^T(x_i  - \bar{X_1})(x_i  - \bar{X_1})^Tw\\
= w^T\left(\sum_{i=1}^{n_{1}}(x_i  - \bar{X_1})(x_i  - \bar{X_1})^T\right)w \\
s_2 = \sum_{i=1}^{n_{2}}(w^{T}x_i - w^{T}\bar{X_2})^2\\
= \sum_{i=1}^{n_{2}}(w^{T}x_i - w^{T}\bar{X_2})(w^{T}x_i - w^{T}\bar{X_1})\\
= \sum_{i=1}^{n_{2}}w^T(x_i  - \bar{X_2})(x_i  - \bar{X_2})^Tw\\
= w^T\left(\sum_{i=1}^{n_{2}}(x_i  - \bar{X_2})(x_i  - \bar{X_2})^T\right)w
\end{gather*}
$$

Ta đặt:

$$
\begin{gather*}
S_1 = \sum_{i=1}^{n_{1}}(x_i  - \bar{X_1})(x_i  - \bar{X_1})^T\\
S_2 = \sum_{i=1}^{n_{2}}(x_i  - \bar{X_2})(x_i  - \bar{X_2})^T
\end{gather*}
$$

Viết lại biểu thức cần tối ưu:

$$
\begin{gather*}
J(w) = \frac{(\mu_1 - \mu_2)^2}{s_1 + s_2} = \frac{w^TS_{b}w}{w^T(S_1 + S_2)w} = \frac{w^TS_{b}w}{w^TS_ww}
\end{gather*}
$$

Trong đó:

- $S_b$ được gọi là between-class scatter matrix

 $$S_b = (\bar{X_1} - \bar{X_2})(\bar{X_1} - \bar{X_2})^T$$

- $S_w$ được gọi là within-class scatter matrix, $S_w = S_1 + S_2$

$$S_1 = \sum_{i=1}^{n_{1}}(x_i  - \bar{X_1})(x_i  - \bar{X_1})^T$$

$$S_2 = \sum_{i=1}^{n_{2}}(x_i  - \bar{X_2})(x_i  - \bar{X_2})^T$$

Để tìm cực đại của hàm $J(w)$, ta đạo hàm $J(w)$ theo $w$ và cho đạo hàm bằng 0, như sau:

$$
\begin{gather*}
\frac{\partial}{\partial w}J(w) = \frac{\partial}{\partial w}\left(\frac{w^TS_{b}w}{w^TS_ww}\right) = 0\\
\Rightarrow (w^TS_ww)\frac{\partial}{\partial w}(w^TS_{b}w) - (w^TS_{b}w)\frac{\partial}{\partial w}(w^TS_{w}w) = 0\\
\Rightarrow (w^TS_ww)2S_{b}w- (w^TS_{b}w)2S_{w}w= 0\\
\Rightarrow S_{b}w - \frac{w^TS_{b}w}{w^TS_ww}S_{w}w = 0\\
\Rightarrow S_{b} - J(w)S_{w}w = 0\\
\Rightarrow S_{w}^{-1}S_{b} - J(w)w = 0\\
\end{gather*}
$$

Ta nhận thấy dạng biểu thức

$$
\begin{gather*}
S_{w}^{-1}S_{b} = \lambda w \\
\text{Trong đó } \lambda = J(w) = \text{Scalar}
\end{gather*}
$$

$$
\begin{gather*}
w^{*} = \underset{w}{\text{argmax}}J(w) = \underset{w}{\text{argmax}}\left(\frac{w^TS_{b}w}{w^TS_ww}\right) = \frac{S_{w}^{-1}(\bar{X_1} - \bar{X_2}}{||S_{w}^{-1}(\bar{X_1} - \bar{X_2}||}
\end{gather*}
$$
