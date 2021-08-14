---
layout: single
permalink: /content/msa/classification/classification_part_3
title: "[MSA] Phân lớp - Phần 3"
author_profile: true
toc: true
comments: True
---

## Bài toán phân tách và tách lớp cho hai quần thể phân phối chuẩn đa biến cùng ma trận hiệp phương sai

### 1. Phát biểu bài toán

Cho $X = \left(X_1, X_2, ..., X_p\right)'$ là vector ngẫu nhiên

- $f_1(x) \sim N(\mu_1, \Sigma)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_1$
- $f_2(x) \sim N(\mu_2, \Sigma)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_2$

Bài toán: Cho một quan sát mới $X = x$, gán nhãn cho $x$ là $\pi_1$ hoặc $\pi_2$

Nhiệm vụ: Cần tìm luật phân lớp (Classification rule) để quyết định gán nhãn cho $X = x$ là  $\pi_1$ hay $\pi_2$, tức là tìm đường (mặt) phân tách hai quần thể.

Luật phân lớp (Classification rule): dựa trên hàm phân biệt (Discriminant Function)

### 2. Giải bài toán

Giả sử các tham số cho quần thể $\mu_1$, $\mu_2$, $\Sigma$ đã biết

Với $i=1,2$, hàm mật độ xác suất đa biến có dạng:

$$
\begin{equation}
\begin{split}
f_{i}(x) = \frac{1}{(2\pi)^{p/2}|\Sigma|^{1/2}}exp\left[-\frac{1}{2}(x - \mu_i)'\Sigma^{-1}(x - \mu_i)\right]
\end{split}
\end{equation}
$$

Gọi $f^{*} = \frac{f_1(x)}{f_2(x)}$, ta có:

$$
\begin{equation}
\begin{split}
f^{*} =exp\left[-\frac{1}{2}(x - \mu_1)'\Sigma^{-1}(x - \mu_1) + \frac{1}{2}(x - \mu_2)'\Sigma^{-1}(x - \mu_2)\right] \\
=exp\left[(\mu_1-\mu_2)'\Sigma^{-1}x-\frac{1}{2}(\mu_1-\mu_2)'\Sigma^{-1}(\mu_1+\mu_2)\right]
\end{split}
\end{equation}
$$

Do $f(x)$ và $log(f(x))$ đồng biến nên ta có hai miền $R_1$, $R_2$ tối tiểu ECM

**Biến đổi**

Ta có:

$$
\begin{equation}
\begin{split}
f_1(x) = (2\pi)^{-\frac{p}{2}}|\Sigma|^{-\frac{p}{2}}exp\left[-\frac{1}{2}(x - \mu_{1})^{T}|\Sigma|^{-1}|(x - \mu_{1})\right]\\
f_2(x) = (2\pi)^{-\frac{p}{2}}|\Sigma|^{-\frac{p}{2}}exp\left[-\frac{1}{2}(x - \mu_{2})^{T}|\Sigma|^{-1}|(x - \mu_{2})\right]
\end{split}
\end{equation}
$$

Lấy $f_1(x)$ chia $f_2(x)$, ta được:

$$
\begin{equation}
\begin{split}
\frac{f_1(x)}{f_2(x)} = exp\left[-\frac{1}{2}(x - \mu_{1})^{T}|\Sigma|^{-1}|(x - \mu_{1}) + \frac{1}{2}(x - \mu_{2})^{T}|\Sigma|^{-1}|(x - \mu_{2})\right]
\end{split}
\end{equation}
$$

Lấy logarithm tự nhiên hai vế, ta thu được đẳng thức:

$$
\begin{equation}
log\left(\frac{f_1(x)}{f_2(x)}\right) = \left[-\frac{1}{2}(x - \mu_{1})^{T}|\Sigma|^{-1}|(x - \mu_{1}) + \frac{1}{2}(x - \mu_{2})^{T}|\Sigma|^{-1}|(x - \mu_{2})\right] \\
\Leftrightarrow log\left(\frac{f_1(x)}{f_2(x)}\right) =  -\frac{1}{2}(x - \mu_{1})^{T}|\Sigma|^{-1}|x + \frac{1}{2}(x - \mu_{1})^{T}|\Sigma|^{-1}|\mu_{1} + \frac{1}{2}(x - \mu_{2})^{T}|\Sigma|^{-1}|x -\\ \frac{1}{2}(x - \mu_{2})^{T}|\Sigma|^{-1}|\mu_{2} \\
\Leftrightarrow log\left(\frac{f_1(x)}{f_2(x)}\right) = -\frac{1}{2}x^T|\Sigma|^{-1}|x - \frac{1}{2}\mu_{1}^T|\Sigma|^{-1}|x + \frac{1}{2}x^T|\Sigma|^{-1}|\mu_1 -  \frac{1}{2}\mu_{1}^T|\Sigma|^{-1}|\mu_{1} + \frac{1}{2}x^T|\Sigma|^{-1}|x \\ -\frac{1}{2}\mu_{2}^T|\Sigma|^{-1}|x - \frac{1}{2}x^T|\Sigma|^{-1}|\mu_2 + \frac{1}{2}\mu_{2}^T|\Sigma|^{-1}|\mu_{2}\\
\Leftrightarrow log\left(\frac{f_1(x)}{f_2(x)}\right) = \frac{1}{2}(\mu_{1}^T - \mu_{2}^T)|\Sigma|^{-1}|x + \frac{1}{2}x^T|\Sigma|^{-1}|(\mu_1 - \mu_2) - \frac{1}{2}\mu_{1}^T|\Sigma|^{-1}|\mu_{1} + \frac{1}{2}\mu_{2}^T|\Sigma|^{-1}|\mu_{2}\\
\Leftrightarrow log\left(\frac{f_1(x)}{f_2(x)}\right) = (\mu_1-\mu_2)'\Sigma^{-1}x-\frac{1}{2}(\mu_1-\mu_2)'\Sigma^{-1}(\mu_1+\mu_2)
\end{equation}
$$

Cuối cùng, ta có luật phân lớp như sau:

$$
\begin{equation}
\begin{split}
R_1: log(f^{*}) \geq log\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p2}{p_1}\right)\right] \\
R_2: log(f^{*}) < log\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p2}{p_1}\right)\right]
\end{split}
\end{equation}
$$

Do trong thực tế các giá trị $\mu_1$ $\mu_2$ và $\Sigma$ của quần thể ta không biết, nên người ta sẽ ước lượng nó.


Giả sử các tham số cho quần thể $\mu_1$, $\mu_2$, $\Sigma$ chưa biết\newline
Lấy $n_1$ mẫu độc lập từ quần thể $\pi_1$ và $n_2$ mẫu độc lập từ quần thể $\pi_2$, điều kiện $n_1 + n_2 - 2 \geq p$, ước lượng các tham số cần thiết như sau:

$$
\begin{equation}
\begin{split}
\widehat{\mu_1} = \bar{x_1} = \frac{1}{n_1}\sum_{i=1}^{n_1}x_{1j}; S_1 = \frac{1}{n_1 - 1}\sum_{j=1}^{n_1}(x_{1j} - \bar{x}_{1})(x_{1j} - \bar{x}_{1})\\
\widehat{\mu_2} = \bar{x_2} = \frac{1}{n_2}\sum_{i=1}^{n_2}x_{2j}; S_2 = \frac{1}{n_2 - 1}\sum_{j=1}^{n_2}(x_{2j} - \bar{x}_{2})(x_{2j} - \bar{x}_{2})\\
S_{\text{pooled}} = \left[\frac{n_1 - 1}{(n_1 - 1) + (n_2 - 1)}\right]S_1 + \left[\frac{n_2 - 1}{(n_1 - 1) + (n_2 - 1)}\right]S_2
\end{split}
\end{equation}
$$

Ước lượng tối tiểu ECM cho hai quần thể phân phối chuẩn:\

Gán nhãn $x_0$ là $\pi_1$ nếu:

$$
\begin{equation}
\begin{split}
(\bar{x}_1 - \bar{x}_2)'S_{\text{pooled}}^{-1}x_0 - \frac{1}{2}(\bar{x}_1 - \bar{x}_2)'S_{\text{pooled}}^{-1}(\bar{x}_1 + \bar{x}_2) \geq ln\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p_2}{p_1}\right)\right]
\end{split}
\end{equation}
$$

Gán nhãn $x_0$ là $\pi_2$ nếu:

$$
\begin{equation}
\begin{split}
(\bar{x}_1 - \bar{x}_2)'S_{\text{pooled}}^{-1}x_0 - \frac{1}{2}(\bar{x}_1 - \bar{x}_2)'S_{\text{pooled}}^{-1}(\bar{x}_1 + \bar{x}_2) < ln\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p_2}{p_1}\right)\right]
\end{split}
\end{equation}
$$

Trường hợp: $\left(\frac{c(1\|2)}{c(2\|1)}\right)\left(\frac{p_2}{p_1}\right) = 1$ mà $ln(1) = 0$.

Luật trở thành

$$
\begin{equation}
\begin{split}
	R_1: \hat{y} \geq \hat{m}
	R_2: \hat{y} < \hat{m}
\end{split}
\end{equation}
$$

Trong đó:

$$
\begin{equation}
\begin{split}
\hat{y} = (\bar{x}_1 - \bar{x}_2)'S_{\text{pooled}}^{-1}x = \hat{a}'x
\hat{m} = \frac{1}{2}(\bar{y}_1 + \bar{y}_1)
\end{split}
\end{equation}
$$

Chuẩn hóa $\hat{a}$ bằng cách:
- $\hat{a}^{*} = \frac{\hat{a}}{\|\|\hat{a}\|\|}$
- $\hat{a}^{*} =  \frac{\hat{a}}{\hat{a}_{1}}$
