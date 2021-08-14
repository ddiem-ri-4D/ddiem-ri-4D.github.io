---
layout: single
permalink: /content/msa/classification/classification_part_5
title: "[MSA] Phân lớp - Phần 5"
author_profile: true
toc: true
comments: True
output:
  pdf_document:
    keep_tex: yes
header-includes:
  \usepackage{dcolumn}
---

## Đánh giá hàm phân lớp

### Độ đo phân lớp sai

#### Tổng xác suất phân lớp sai - Total Probability of Misclassification

Cho công thức tổng xác suất phân lớp sai (Total Probability of Misclassification - TPM) như sau:

$$
\begin{equation}
    TPM(R_1, R_2) = p_1\int_{R_1}f_1(x)dx + p_2\int_{R_2}f_2(x)dx
\end{equation}
$$

Với bất kỳ luật phân lớp mà phân tách $\Omega = R_1 \cup R_2$

Ta gọi độ lỗi tối ưu (Optimum Error Rate - OER) là giá trị nhỏ nhất có thể có của TPM

$$
\begin{equation}
OER = \mathop{minimize}_{(R_{1}, R_{2})} TPM(R_{1}, R_{2}), \Omega = R_1 \cup R_2
\end{equation}
$$

Có được khi $R_1: \frac{f_1(x)}{f_2(x)} \geq \frac{p_2}{p_1}$ và $R_2: \frac{f_1(x)}{f_2(x)} < \frac{p_2}{p_1}$

#### Tỷ lệ lỗi thực tế - Actual Error Rate

Actual Error Rate (AER) được định nghĩa bằng cách dùng ước lượng mẫu

$$
\begin{equation}
    AER(\hat{R_1}, \hat{R_2}) = p_1\int_{\hat{R_1}}f_1(x)dx + p_2\int_{\hat{R_2}}f_2(x)dx
\end{equation}
$$

#### Apparent Error Rate

#### Cross-Validation

Lachenbruch đề xuất một cách tiếp cận tốt hơn để ước tính AER

Bước 01: Đối với quần thể thứ nhất, với i nằm trong khoảng từ 1 đến $n_1$
- Lấy ra quan sát thứ i từ quần thể $\pi_1$ và xây dưng luật phân lớp
- Sử dụng luật phân lớp ở trên đển phân lớp quan sát thứ i

Bước 02: Đối với quần thể thứ hai, với i nằm trong khoảng từ 1 đến $n_2$
- Lấy ra quan sát thứ i từ quần thể $\pi_1$ và xây dưng luật phân lớp
- Sử dụng luật phân lớp ở trên đển phân lớp quan sát thứ i

Kỳ vọng không thiên vị AER được cho bởi công thức:

$$\hat{E}(AER) = \frac{n_{M1}^{*} + n_{M2}^{*}}{n_1 + n_2}$$

Trong đó: $n_{M1}^{\*}, n_{M2}^{\*}$ là số phân lớp sai khi sử dụng thủ tục ở trên.

### Đánh giá phân lớp Linear Discriminant Analysis

Giả sử ta có $X = \left(X_1, X_2, ..., X_p\right)'$ là vector ngẫu nhiên
- $f_1(x)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_1$
- $f_2(x)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_2$

Giả định rằng $\left(\frac{c(1\|2)}{c(2\|1)}\right)\left(\frac{p_2}{p_1}\right) = 1$ ta có luật phân lớp

$$
\begin{equation*}
\begin{split}
    R_1: Y \geq m\\
    R_2: Y < m
\end{split}
\end{equation*}
$$

Trong đó
$$Y = a'X$$

$$m = \frac{1}{2}(\mu_{Y_1} + \mu_{Y_2})$$

$$a'=(\mu_1 - \mu_2)'\Sigma^{-1}$$

$$\mu_{Y_1} = a'\mu_1$$

$$\mu_{Y_2} = a'\mu_2$$

Do $Y = a'X = (\mu_1 - \mu_2)'\Sigma^{-1}X$ là một hàm tuyến tính

- $\mu_{Y_1} = a'\mu_1 = (\mu_1 - \mu_2)'\Sigma^{-1}\mu_1$
- $\mu_{Y_2} = a'\mu_2 = (\mu_1 - \mu_2)'\Sigma^{-1}\mu_2$
- $\sigma^2_Y = a'\Sigma a = (\mu_1 - \mu_2)'\Sigma^{-1}(\mu_1 - \mu_2)$

Và bởi vì X là phân phối chuẩn đa biến nên ta có thể xấp xỉ

$$
\begin{equation}
    Y \sim  \begin{cases}
    N(\mu_{Y_1}, \Delta^2) \text{    Nếu thuộc quần thể } \pi_1 \\
    N(\mu_{Y_2}, \Delta^2) \text{    Nếu thuộc quần thể } \pi_2\\
  \end{cases}
\end{equation}
$$
