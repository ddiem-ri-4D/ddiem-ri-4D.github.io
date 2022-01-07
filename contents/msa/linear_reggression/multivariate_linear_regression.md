---
layout: single
permalink: /content/msa/linear_regression/multivariate_linear_regression
title: "[MSA] Multivariate Linear Regression"
author_profile: true
toc: true
comments: True
---

Phần trình bày về mô hình hồi quy tuyến tính đa biến - multivariate linear regression model

## 1) Động lực nghiên cứu khoa học

Trong lĩnh vực nghiên cứu Máy học (Machine Learning), người ta mong muốn đưa ra các giá trị dự đoán với những thông tin mới được đưa vào mô hình nào đó, thông qua những dữ kiện đã biết trước đó sao cho các giá trị dự đoán càng gần với giá trị thực, và đó là bài toán Regression hay được gọi là hồi quy.

Với trường hợp đơn biết, ta có thể mô phỏng mô hình bằng một đường thẳng có dạng $y = ax + b$, rất quen thuộc khi chúng ta học cấp 3. Với trường hợp hai biến, ta có thể mô phỏng mô hình bằng một mặt phẳng có dạng $y = ax + by + c$, và khi số lượng biến của chúng ta lớn hơn hai, mô hình có thể được mô phỏng bằng một siêu phẳng (hyperplane)

## 2) Phát biểu bài toán

Mô hình hồi quy tuyến tính đa biến như sau:

$$y_{ik} = b_{0k} + \sum_{j=1}^pb_{jk}x_{ij} + e_{ik}, \forall i \in \{1,...,n\}, k \in \{1,...,m\}$$

Trong đó:
- $y_{ik} \in \mathbb{R}$ là giá trị thực tương ứng với quan sát thứ $i$
- $b_{0k} \in R$ là hệ số chặn hồi quy (regression intercept)
- $b_{jk} \in \mathbb{R}$ là các hệ số hồi quy (regression slope) của giá trị dự đoán thứ $j$
- $x_{ij} \in \mathbb{R}$ là giá trị dự đoán thứ $j$ cho quan sát thứ $i$
- $(e_{i1}, e_{i2}, ..., e_{im}) \overset{\underset{\mathrm{iid}}{}}{\sim} \mathcal{N}(0, \sigma^2)$ là multivariate Gaussian error vector

Hay viết gọn hơn bằng dạng ma trận như sau:

$$
\mathbf{Y = XB + E}
$$

Trong đó:
- $\mathbf{Y = [y_1, y_2, ..., y_m]} \in \mathbb{R}^{n \times m}$ có kích thước $n \times m$
    - $\mathbf{y_k} = (y_{1k}, y_{2k}, ..., y_{nk})' \in \mathbb{R}^{n}$ là vector giá trị dự đoán thứ k
- $\mathbf{X = [1_n, x_1, x_2, ..., x_p]} \in \mathbb{R}^{n \times (p+1)}$
    - $1_n$ là vector một có kích thước $n \times 1$
    - $x_j = (x_{1j}, x_{2j}, ..., x_{nj})' \in \mathbb{R}^{n}$ vector bộ dự đoán thứ j có kích thước $n \times 1$
- $\mathbf{B = [b_1, b_2, ..., b_m]}  \in \mathbb{R}^{(p+1) \times m}$
    - $b_k = (b_{0k}, b_{1k}, ..., b_{pk})' \in \mathbb{R}^{p+1}$ là vector hệ số thứ k có kích thước $((p + 1) \times 1)$
- $\mathbf{E = [e_1, e_2, ..., e_m]} \in \mathbb{R}^{n \times m}$
    - $e_k = (e_{1k}, e_{2k}, ..., e_{nk})'  \in \mathbb{R}^{n}$ là vector độ lỗi có kích thước $n \times 1$

## 3) Phương pháp

### 3.1 Ước lượng tham số mô hình bằng phương pháp bình phương tối tiểu (Ordinary Least Squares)

$$\underset{\mathbf{B} \in \mathbb{R}^{(p+1) \times m}}{\text{min}} ||\mathbf{Y -XB}||^2 = \underset{\mathbf{B} \in \mathbb{R}^{(p+1) \times m}}{\text{min}} \sum_{i=1}^{n}\sum_{k=1}^m\left(y_{ik} - b_{0k} - \sum_{j=1}^pb_{jk}x_{ij}\right)^2$$

Trong đó: $$\|\cdot\|$$ là Frobenius norm

$$
\text{OLS}(\mathbf{B}) = ||\mathbf{Y -XB}||^2 = \text{tr}(\mathbf{Y'Y}) - 2\text{tr}(\mathbf{Y'XB}) + \text{tr}(\mathbf{B'X'XB})
$$

$$
\frac{\partial \text{OLS}(\mathbf{B})}{\partial \mathbf{B}} = -2\mathbf{X'Y} + 2\mathbf{X'XB}
$$

OLS Solution:

$$
\hat{\mathbf{B}} = \mathbf{(X'X)^{-1}X'Y} \leftrightarrow \hat{\mathbf{b}}_k = \mathbf{(X'X)^{-1}X'}\mathbf{y}_k
$$

### 3.2 Ước lượng tham số mô hình bằng phương pháp triển vọng cực đại (maximum likelihood)

## 4) Ý nghĩa hình học

## 5) Ví dụ minh họa
