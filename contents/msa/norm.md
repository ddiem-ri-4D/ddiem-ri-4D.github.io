---
layout: single
permalink: /content/msa/norm
title: "[MSA] Phân phối chuẩn đa biến"
author_profile: true
toc: true
comments: True
---

## Chuẩn một biến (Univariate normal)

### Hàm mật độ chuẩn (Đơn biến - Univariate)

Cho một biến $x \in \mathbb{R}$, hàm mật độ xác suất (probability density function - pdf) chuẩn là

$$
\begin{gather}
f(x) = \frac{1}{\sigma\sqrt{2\pi}}exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
\end{gather}
$$

Trong đó:
- $\mu \in \mathbb{R}$ là trung bình (mean)
- $\sigma > 0$ là độ lệch chuẩn (standard deviation), $]\sigma^2$ là phương sai (variance)
- $e \approx 2.71828$ là cơ số của logarit tự nhiên

### Phân phối chuẩn (Standard Normal Distribution)

Nếu $X \sim N(0, 1)$ thì $X$ theo một phân phối chuẩn

$$
f(x) = \frac{1}{2\pi}e^{-x^2/2}
$$

![](https://cdn.scribbr.com/wp-content/uploads/2020/10/standard-normal-distribution-768x475.png)

### Tính toán xác suất

Những xác suất liên hệ với diện tích bên dưới hàm mật độ xác suất

$$
P(a \leq X \leq b) = \int_a^bf(x)dx = F(b) - F(a)
$$

Trong đó

$$
F(x) = \int_{-\infty}^xf(u)du
$$

là hàm phân phối tích lũy - cumulative distribution function (cdf)


Xuất suất chuẩn

![](https://upload.wikimedia.org/wikipedia/commons/8/8c/Standard_deviation_diagram.svg)

### Các phép biến đổi Affine

### Ước lượng tham số

Giả sử rằng $\mathbf{x} = (x_1, ..., x_n)$ là một mẫu dữ liệu của các biến ngẫu nhiên độc lập và phân phối giống hệt nhau từ một phân phối chuẩn với trung bình $\mu$ và phương sai $\sigma^2$, tức là $x_i \sim N(\mu, \sigma^2)$

Hàm likelihood cho những tham số (dữ liệu cho trước) có dạng như sau

$$
L(\mu, \sigma^2 | \mathbf{x}) = \prod_{i=1}^{n}f(x_i) = \prod_{i=1}^{n}\frac{1}{\sqrt{2\pi\sigma^2}}exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
$$

và hàm log-likelihood được cho bởi

$$
LL(\mu, \sigma^2 | \mathbf{x}) = \sum_{i=1}^n\text{log}(f(x_i)) = -\frac{n}{2}\text{log}(2\pi) - \frac{n}{2}\text{log}(\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^n(x_i - \mu)^2
$$

Ước lượng triển vọng cực đại (Maximum likelihood estimate) của trung bình (mean) là giá trị của $\mu$ sao cho cực tiểu

$$
\sum_{i=1}^n(x_i - \mu)^2 = \sum_{i=1}^nx_i^2 - 2n\bar{x}\mu+n\mu^2
$$

Trong đó:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^nx_i
$$

là trung bình mẫu (sample)

Lấy đạo hàm theo $\mu$

$$
\frac{\partial \sum_{i=1}^n(x_i - \mu)^2}{\partial \mu} = -2n\bar{x} + 2n\mu \leftrightarrow \bar{x} = \mu
$$

Ước lượng triển vọng cực đại (Maximum likelihood estimate) của phương sai $\sigma^2$ mà cực tiểu

$$
\frac{n}{2}\text{log}(\sigma^2) + \frac{1}{2\sigma^2}\sum_{i=1}^n(x_i - \mu)^2 = \frac{n}{2}\text{log}(\sigma^2) + \frac{1}{2\sigma^2}\sum_{i=1}^nx_i^2 - \frac{n\bar{x}^2}{2\sigma^2}
$$

Lấy đạo hàm theo $\sigma^2$

$$
\frac{\partial \frac{n}{2}\text{log}(\sigma^2) + \frac{1}{2\sigma^2}\sum_{i=1}^n(x_i - \hat{\mu})^2}{\partial \sigma^2} = \frac{n}{2\sigma^2} - \frac{1}{2\sigma^4} \sum_{i=1}^n(x_i - \hat{\mu})^2
$$

Suy ra

$$
\hat{\sigma}^2 \frac{1}{n}\sum_{i=1}^n(x_i - \bar{x})^2
$$

là ước lượng triển vọng cực đại (Maximum likelihood estimate) của phương sai $\sigma^2$

## Chuẩn hai biến (Bivariate normal)

## Chuẩn đa biến (Multivariate normal)

## Phân phối mẫu (Sampling distributions)
