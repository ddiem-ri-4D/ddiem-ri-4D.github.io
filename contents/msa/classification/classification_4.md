---
layout: single
permalink: /content/msa/classification/classification_part_4
title: "[MSA] Phân lớp - Phần 4"
author_profile: true
toc: true
comments: True
---

## Bài toán phân tách và tách lớp cho hai quần thể phân phối chuẩn đa biến không cùng ma trận hiệp phương sai

### 1. Phát biểu bài toán

Cho $X = \left(X_1, X_2, ..., X_p\right)'$ là vector ngẫu nhiên
- $f_1(x) \sim N(\mu_1, \Sigma_{1})$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_1$
- $f_2(x) \sim N(\mu_2, \Sigma_{2})$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_2$

Bài toán: Cho một quan sát mới $X = x$, gán nhãn cho $x$ là $\pi_1$ hoặc $\pi_2$

Nhiệm vụ: Cần tìm luật phân lớp (Classification rule) để quyết định gán nhãn cho $X = x$ là  $\pi_1$ hay $\pi_2$, tức là tìm đường (mặt) phân tách hai quần thể

Luật phân lớp (Classification rule): dựa trên hàm phân biệt (Discriminant Function)

### 2. Giải bài toán

Ta có, với $i=\{1, 2\}$ hàm mật độ phân phối chuẩn đa biến có dạng:

$$
\begin{equation}
\begin{split}
	f_{i}(k)=(2\pi)^{-p/2}|\Sigma|^{-1/2}exp\left[-\frac{1}{2}(x-\mu_i)'\Sigma^{-1}_{i}(x-\mu_i)\right]
\end{split}
\end{equation}
$$

Gọi $f^{*} = \frac{f_1(x)}{f_2(x)}$, ta có:

$$
\begin{equation}
\begin{split}
	f^{*} =\left(\frac{|\Sigma_1|}{|\Sigma_2|}\right)^{-1/2}exp\left[-\frac{1}{2}(x - \mu_1)'\Sigma^{-1}_{1}(x - \mu_1) + \frac{1}{2}(x - \mu_2)'\Sigma^{-1}_{2}(x - \mu_2)\right]\\
\end{split}
\end{equation}
$$

$f(x)$ và $log(f(x))$ đồng biến nên ta có hai miền $R_1$, $R_2$ tối tiểu ECM

**Biến đổi** $log(f^{*})$

$$
\begin{equation}
log(f^{*}) = -\frac{1}{2}log\left(\frac{|\Sigma_1|}{|\Sigma_2|}\right) + \left[-\frac{1}{2}(x - \mu_1)'\Sigma^{-1}_{1}(x - \mu_1) + \frac{1}{2}(x - \mu_2)'\Sigma^{-1}_{2}(x - \mu_2)\right]\\
log(f^{*}) =-\frac{1}{2}log\left(\frac{|\Sigma_1|}{|\Sigma_2|}\right) - \frac{1}{2}(x - \mu_1)'\Sigma^{-1}_{1}x + \frac{1}{2}(x - \mu_1)'\Sigma^{-1}_{1}\mu_1 + \frac{1}{2}(x - \mu_2)'\Sigma^{-1}_{2}x\\ - \frac{1}{2}(x - \mu_2)'\Sigma^{-1}_{2}\mu_2\\
log(f^{*}) =-\frac{1}{2}log\left(\frac{|\Sigma_1|}{|\Sigma_2|}\right) - \frac{1}{2}x'\Sigma^{-1}_{1}x + \frac{1}{2}\mu_1'\Sigma^{-1}_{1}x + \frac{1}{2}x'\Sigma^{-1}_{1}\mu_1 - \frac{1}{2}\mu_1'\Sigma^{-1}_{1}\mu_1\\ +\frac{1}{2}x'\Sigma^{-1}_{2}x - \frac{1}{2}\mu_2'\Sigma^{-1}_{2}x + \frac{1}{2}x'\Sigma^{-1}_{2}\mu_2 + \frac{1}{2}\mu_2'\Sigma^{-1}_{2}\mu_2\\
log(f^{*}) =-\frac{1}{2}log\left(\frac{|\Sigma_1|}{|\Sigma_2|}\right) -  \frac{1}{2}x'(\Sigma^{-1}_{1} - \Sigma^{-1}_{2})x + \frac{1}{2}(\mu_1'\Sigma^{-1}_{1} - \mu_2'\Sigma^{-1}_{2})x + \frac{1}{2}x'(\Sigma^{-1}_{1}\mu_1 -\Sigma^{-1}_{2}\mu_2) - \\
\frac{1}{2}(\mu_1'\Sigma^{-1}_{1}\mu_1 + \mu_2'\Sigma^{-1}_{2}\mu_2)\\
log(f^{*}) =-\frac{1}{2}log\left(\frac{|\Sigma_1|}{|\Sigma_2|}\right) - \frac{1}{2}x'(\Sigma^{-1}_{1} - \Sigma^{-1}_{2})x + (\mu_1'\Sigma^{-1}_{1} - \mu_2'\Sigma^{-1}_{2})x - \frac{1}{2}(\mu_1'\Sigma^{-1}_{1}\mu_1 - \mu_2'\Sigma^{-1}_{2}\mu_2)
\end{equation}
$$

Cuối cùng, ta có luật phân lớp như sau:

$$
\begin{equation}
\begin{split}
R_1: log(f^{*}) \geq log\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p2}{p_1}\right)\right]\\
R_2: log(f^{*}) < log\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p2}{p_1}\right)\right]
\end{split}
\end{equation}
$$

Giả sử các tham số cho quần thể $\mu_1$, $\mu_2$, $\Sigma_1$, $\Sigma_2$ chưa biết

Lấy $n_1$ mẫu độc lập từ quần thể $\pi_1$ và $n_2$ mẫu độc lập từ quần thể $\pi_2$, điều kiện $n_1 + n_2 - 2 \geq p$, ước lượng các tham số cần thiết như sau:

$$
\begin{equation}
\begin{split}
	\widehat{\mu_1} = \bar{x_1} = \frac{1}{n_1}\sum_{i=1}^{n_1}x_{1j}; \widehat{\Sigma_1} = S_1 = \frac{1}{n_1 - 1}\sum_{j=1}^{n_1}(x_{1j} - \bar{x}_{1})(x_{1j} - \bar{x}_{1})\\
	\widehat{\mu_2} = \bar{x_2} = \frac{1}{n_2}\sum_{i=1}^{n_2}x_{2j}; \widehat{\Sigma_2} = S_2 = \frac{1}{n_2 - 1}\sum_{j=1}^{n_2}(x_{2j} - \bar{x}_{2})(x_{2j} - \bar{x}_{2})\\
	S_{\text{pooled}} = \left[\frac{n_1 - 1}{(n_1 - 1) + (n_2 - 1)}\right]S_1 + \left[\frac{n_2 - 1}{(n_1 - 1) + (n_2 - 1)}\right]S_2
\end{split}
\end{equation}
$$

Ta thay thế hàm $f^{\*}$ bằng ước lượng $\hat{f}^{*}$:

$$
\begin{equation}
\begin{split}
	\hat{f}^{*}=\left(\frac{|S_1|}{|S_2|}\right)^{-1/2}exp\left[-\frac{1}{2}(x-\bar{x_1})'S_1^{-1}(x-\bar{x_1}) + \frac{1}{2}(x-\bar{x_2})'S_2^{-1}(x-\bar{x_2})\right]
\end{split}
\end{equation}
$$

Lấy logarithm tự nhiên $\hat{f}^{*}$:

$$
\begin{equation}
\begin{split}
	log(\hat{f}^{*})
	=log\left[\left(\frac{|S_1|}{|S_2|}\right)^{-1/2}exp\left[-\frac{1}{2}(x-\bar{x_1})'S_1^{-1}(x-\bar{x_1}) + \frac{1}{2}(x-\bar{x_2})'S_2^{-1}(x-\bar{x_2})\right]\right]
	=\hat{y}-\hat{m}
\end{split}
\end{equation}
$$

**Biến đổi** $log(\hat{f}^{*})$

$$
\begin{equation}
\begin{aligned}
log(\hat{f}^{*}) = -\frac{1}{2}log\left(\frac{|S_1|}{|S_2|}\right) + \left[-\frac{1}{2}(x - \bar{x_1})'S^{-1}_{1}(x - \bar{x_1}) + \frac{1}{2}(x - \bar{x_2})'S^{-1}_{2}(x - \bar{x_2})\right]\\
log(\hat{f}^{*}) =-\frac{1}{2}log\left(\frac{|S_1|}{|S_2|}\right) - \frac{1}{2}(x - \bar{x_1})'\S^{-1}_{1}x + \frac{1}{2}(x - \bar{x_1})'S^{-1}_{1}\bar{x_1} + \frac{1}{2}(x - \bar{x_2})'\S^{-1}_{2}x\\ - \frac{1}{2}(x - \bar{x_2})'S^{-1}_{2}\bar{x_2}\\
log(\hat{f}^{*}) =-\frac{1}{2}log\left(\frac{|S_1|}{|S_2|}\right) - \frac{1}{2}x'S^{-1}_{1}x + \frac{1}{2}\bar{x_1}'S^{-1}_{1}x + \frac{1}{2}x'S^{-1}_{1}\bar{x_1} - \frac{1}{2}\bar{x_1}'S^{-1}_{1}\bar{x_1}\\ +\frac{1}{2}x'S^{-1}_{2}x - \frac{1}{2}\bar{x_2}'S^{-1}_{2}x + \frac{1}{2}x'S^{-1}_{2}\bar{x_2} + \frac{1}{2}\bar{x_2}'S^{-1}_{2}\bar{x_2}\\
log(\hat{f}^{*}) =-\frac{1}{2}log\left(\frac{|S_1|}{|S_2|}\right) -  \frac{1}{2}x'(S^{-1}_{1} - S^{-1}_{2})x + \frac{1}{2}(\bar{x_1}'S^{-1}_{1} - \bar{x_2}'S^{-1}_{2})x + \frac{1}{2}x'(S^{-1}_{1}\bar{x_1} -S^{-1}_{2}\bar{x_2}) - \\
\frac{1}{2}(\bar{x_1}'S^{-1}_{1}\bar{x_1} + \bar{x_2}'S^{-1}_{2}\bar{x_2})\\
log(\hat{f}^{*}) =-\frac{1}{2}log\left(\frac{|S_1|}{|S_2|}\right) - \frac{1}{2}x'(S^{-1}_{1} - S^{-1}_{2})x + (\bar{x_1}'S^{-1}_{1} - \bar{x_2}'S^{-1}_{2})x - \frac{1}{2}(\bar{x_1}'S^{-1}_{1}\bar{x_1} - \bar{x_2}'S^{-1}_{2}\bar{x_2})
\end{aligned}
\end{equation}
$$

Trong đó

$$
\begin{equation}
\begin{split}
	\hat{y} = -\frac{1}{2}x'(S_1^{-1} - S_1^{-2})x + (\bar{x}_1'S_1^{-1} - \bar{x}_2'S_2^{-1})x\\
	\hat{m} = \frac{1}{2}log\left(\frac{|S_1|}{|S_2|}\right) + \frac{1}{2}(\bar{x}_1'S_1^{-1}\bar{x}_1-\bar{x}_2'S_2^{-1}\bar{x}_2)\\
\end{split}
\end{equation}
$$

Gán nhãn một quan sát mới $x_0$ vào $\pi_1$ nếu:

$$
\begin{equation}
\begin{split}
	\hat{y}-\hat{m} \geq ln\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p_2}{p_1}\right)\right]
\end{split}
\end{equation}
$$

Gán nhãn một quan sát mới $x_0$ vào $\pi_2$ nếu:

$$
\begin{equation}
\begin{split}
	\hat{y}-\hat{m} < ln\left[\left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p_2}{p_1}\right)\right]
\end{split}
\end{equation}
$$

|![](/contents/msa/classification/figure_11_6.png)|
|:--:|
| Figure 11.6 from Applied Multivariate Statistical Analysis, 6th Ed (Johnson & Wichern) |
