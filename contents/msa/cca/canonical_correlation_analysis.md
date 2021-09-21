---
layout: single
permalink: /content/msa/cca/canonical_correlation_analysis
title: "[MSA] Canonical Correlation Analysis"
author_profile: true
toc: true
comments: True
---
Phần trình bày về phân tích tương quan chính tắc - Canonical Correlation Analysis Methods

## 1) Động lực nghiên cứu khoa học

Phân tích tương quan chính tắc (Canonical Correlation Analysis – CCA) là một phương pháp phân tích mối quan hệ giữa hai tập dữ liệu, từ đó tìm ra được các mối tương quan, các sự liên hệ tồn tại trong dữ liệu để có thể hiểu sâu về dữ liệu cần phân tích hay tìm ra những tri thức tiềm ẩn bên trong của nó.

Mục tiêu chính của CCA là liên kết hai tập biến bằng cách tìm những tổ hợp tuyến tính của những biến đó mà cực đại tương quan nhất có thể
- Data reduction - Giảm chiều dữ liệu: giải thích hiệp phương sai giữa hai tập biến bằng cách sử dụng một số lượng nhỏ các tổ hợp tuyến tính
- Data interpretation - Diễn dịch dữ liệu: tìm những đặc trưng (tức là biến tương quan - canonical variates) quan trọng trong việc giải thích hiệp phương

## 2) Phát biểu bài toán

Định nghĩa bài toán trên quần thể (population)

Đầu vào (Input): Cho trước hai tập vector ngẫu nhiên

$$
\mathbf{X}= (X_1, X_2, ..., X_p)'
$$

Và

$$
\mathbf{Y}= (Y_1, Y_2, ..., Y_q)'
$$

với vector trung bình lần lượt là $\mu_{X}$ và $\mu_y$, các ma trận hiệp phương sai lần lượt là $\mathbf{\Sigma}_X$ và $\mathbf{\Sigma}_Y$

Đầu ra (Output):
- Mối tương quan chính tắc giữa 2 tập vector ngẫu nhiên $\mathbf{X}$ và $\mathbf{Y}$
- Hai biến chính tắc

$$
\begin{gather}
x = [x_1, x_2, x_3, ..., x_n]\\
y = [y_1, y_2, y_3, ..., y_n]
\end{gather}
$$

Đặt $\mathbf{Z}' = (\mathbf{X}', \mathbf{Y}')$ và $\mathbf{Z} \sim (\mu, \mathbf{\Sigma})$ trong đó $\mu' = (\mu'_x, \mu'_y)$ và

$$
 \mathbf{\Sigma} = \begin{bmatrix}  \mathbf{\Sigma}_X &  \mathbf{\Sigma}_{XY} \\  \mathbf{\Sigma}_{YX} &  \mathbf{\Sigma}_Y \end{bmatrix}
$$

Trong đó

$$
 \mathbf{\Sigma}_{XY} = \mathbf{\Sigma}_{YX} = E[(\mathbf{X} - \mu_x)(\mathbf{Y} - \mu_y)']
$$

là hiệp phương sai giữa $\mathbf{X}$ và $\mathbf{Y}$

Định nghĩa các biến mới $U$ và $V$ (canonical variate pair) thông qua tổ hợp tuyến tính của $\mathbf{X}$ và $\mathbf{Y}$

$$
U = \mathbf{a}'\mathbf{X}
$$

$$
V = \mathbf{b}'\mathbf{Y}
$$

Trong đó: $\mathbf{a}$ và $\mathbf{b}$ lần lượt là các vector hệ số tương ứng

Ta có:
$$
\text{Var}(U) = \mathbf{a}'\text{Cov}(\mathbf{X})\mathbf{a} = \mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}
$$

$$
\text{Var}(V) = \mathbf{b}'\text{Cov}(\mathbf{Y})\mathbf{b} = \mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b}
$$

$$
\text{Var}(U, V) = \mathbf{a}'\text{Cov}(\mathbf{X}, \mathbf{Y})\mathbf{b} = \mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b}
$$

Ta đã có các tổ hợp tuyến tính của $\mathbf{X}$ và $\mathbf{Y}$ lần lượt là $U$ và $V$. Cần tìm hệ số tương quan bằng cách tính tương quan giữa $U$ và $V$ => Ẩn số là $\mathbf{a}$, $\mathbf{b}$ sao cho

$$
\text{Corr}(U, V) = \frac{\mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b}}{\sqrt{\mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}}\sqrt{\mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b}}}
$$

đạt cực đại thì ta có thể tìm được tương quan giữa hai tập $\mathbf{X}$ và $\mathbf{Y}$

**Định nghĩa về first canonical variate pair**

Cặp biến chính tắc thứ nhất (first canonical variate pair) ($U_1$, $V_1$) là một cặp tổ hợp tuyến tính của những vector $\{\mathbf{a}_1, \mathbf{b}_1\}$ mà cực đại

$$
\text{Corr}(U, V) = \frac{\mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b}}{\sqrt{\mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}}\sqrt{\mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b}}}
$$

kéo theo $U_1$ và $V_1$ có các phương sai đơn vị

**Định nghĩa về second canonical variate pair**

Cặp biến chính tắc thứ nhất (first canonical variate pair) ($U_2$, $V_2$) là một cặp tổ hợp tuyến tính của những vector $\{\mathbf{a}_2, \mathbf{b}_2\}$ mà cực đại

$$
\text{Corr}(U, V) = \frac{\mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b}}{\sqrt{\mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}}\sqrt{\mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b}}}
$$

mà giữa tất cả các tổ hợp tuyến tính nào mà không có mối liên quan nào với cặp biến chính tắc đầu tiên.

Cặp biến chính tắc thứ ($l$-th canonical variate pair) là một cặp tổ hợp tuyến tính ($U_l$, $V_l$) có các phương sai đơn vị sao cho cực đại được biểu thức phía trên và giữa tất cả các tổ hợp tuyến tính nào mà không có mối liên quan nào với cặp biến chính tắc ($U_k$, $V_k$) với mọi $k < l$

## 3) Phương pháp

### Phương pháp giải toán cho quần thể

Cho trước hai tập biến

$$
\mathbf{X}= (X_1, X_2, ..., X_p)'
$$

Và

$$
\mathbf{Y}= (Y_1, Y_2, ..., Y_q)'
$$

với vector trung bình lần lượt là $\mu_{X}$ và $\mu_y$, các ma trận hiệp phương sai lần lượt là $\mathbf{\Sigma}_X$ và $\mathbf{\Sigma}_Y$

Ta cần

$$
\underset{\mathbf{a}, \mathbf{b}}{\text{ max }} \text{Corr}(U, V) = \frac{\mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b}}{\sqrt{\mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}}\sqrt{\mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b}}}
$$

Việc chọn phép biến đổi tuyến tính là tùy ý, cực đại hóa correlation tương đương với cực đại hóa phân số, tức cực đại hóa tử số với ràng buộc

$$
\begin{cases}
\mathbf{a}'\mathbf{\Sigma}_X\mathbf{a} = 1\\
\mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b} = 1
\end{cases}
$$

Ta có hàm Lagrangian như sau

$$
L(\lambda, \mathbf{a}, \mathbf{b}) = \mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b} + \frac{\lambda_a}{2}(1 - \mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}) + \frac{\lambda_b}{2}(1 - \mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b})
$$

Đạo hàm theo $\mathbf{a}$ và $\mathbf{b}$ và cho đạo hàm bằng 0

$$
\frac{\partial L}{\partial a} = \mathbf{\Sigma}_{XY}\mathbf{b} - \lambda_a\mathbf{\Sigma}_X\mathbf{a} = 0
$$

$$
\frac{\partial L}{\partial a} = \mathbf{\Sigma}_{XY}\mathbf{a} - \lambda_b\mathbf{\Sigma}_Y\mathbf{b} = 0
$$

Ta có:

$$
\begin{gather}
0 = \mathbf{a}'(\mathbf{\Sigma}_{XY}\mathbf{b} - \lambda_a\mathbf{\Sigma}_X\mathbf{a}) - \mathbf{b}'(\mathbf{\Sigma}_{XY}\mathbf{a} +  - \lambda_b\mathbf{\Sigma}_Y\mathbf{b})\\
= \mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b} - \mathbf{a}'\lambda_a\mathbf{\Sigma}_X\mathbf{a} -  \mathbf{b}'\mathbf{\Sigma}_{XY}\mathbf{a} + \mathbf{b}'\lambda_b\mathbf{\Sigma}_Y\mathbf{b}\\
= \lambda_b\mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b} - \lambda_a \mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}
\end{gather}
$$

Giả sử $\mathbf{\Sigma}_Y$ khả nghịch, $\lambda_a = \lambda_b = \lambda$

$$
 \mathbf{b} = \frac{\mathbf{\Sigma}_Y^{-1}\mathbf{\Sigma}_{XY} \mathbf{a}}{\lambda}
$$

Mà, từ chứng minh trên

$$
\mathbf{\Sigma}_{XY}\mathbf{b} - \lambda_a\mathbf{\Sigma}_X\mathbf{a} = 0
$$

Suy ra

$$
\begin{gather}
\frac{\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_Y^{-1}\mathbf{\Sigma}_{XY} \mathbf{a}}{\lambda}  - \lambda_a\mathbf{\Sigma}_X\mathbf{a} = 0\\
\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_Y^{-1}\mathbf{\Sigma}_{XY} = \lambda^2\mathbf{\Sigma}_X\mathbf{a}
\end{gather}
$$

Và tương tự, ta cũng sẽ thu được

$$
\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_X^{-1}\mathbf{\Sigma}_{XY} \mathbf{b} = \lambda^2\mathbf{\Sigma}_Y\mathbf{b}
$$

Biểu thức trên có dạng của bài toán eigen tổng quát (generalized eigen problem)

$$
\mathbf{A}x = \theta\mathbf{B}x
$$

Từ kết quả thu được

$$
\underset{\mathbf{a}, \mathbf{b}}{\text{ max }} \text{Corr}(U, V) = \frac{\mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b}}{\sqrt{\mathbf{a}'\mathbf{\Sigma}_X\mathbf{a}}\sqrt{\mathbf{b}'\mathbf{\Sigma}_Y\mathbf{b}}}
$$

thu được bởi các tổ hợp tuyến tính (first canonical variate pair)

$$
U_1 = \mathbf{e}_1'\mathbf{\Sigma}_X^{-1/2}\mathbf{X}
$$

và

$$
V_1 = \mathbf{f}_1'\mathbf{\Sigma}_Y^{-1/2}\mathbf{Y}
$$

Cặp biến chính tắc thứ ($l$-th canonical variate pair), $l = 2, 3, ..., \text{min}(p, q)$

$$
U_l = \mathbf{e}_l'\mathbf{\Sigma}_X^{-1/2}\mathbf{X}
$$

và

$$
V_l = \mathbf{f}_l'\mathbf{\Sigma}_Y^{-1/2}\mathbf{Y}
$$

cực đại $\underset{\mathbf{a}, \mathbf{b}}{\text{ max }} \text{Corr}(U_k, V_k) = \rho_k^*$ mà giữa tất cả tổ hợp tuyến tính mà không có mối liên hệ với các cặp biến thứ $1, 2, ..., l - 1$

Trong đó
- $ \rho_1^2 \geq  \rho_2^2 \geq ... \geq  \rho_p^2$ là các giá trị riêng của $$\mathbf{\Sigma}_X^{-1/2}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_Y^{-1}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_X^{-1/2}$$
và $\mathbf{e}_1, \mathbf{e}_2, ..., \mathbf{e}_p$ là các vector riêng tương ứng
- $ \rho_1^2 \geq  \rho_2^2 \geq ... \geq  \rho_p^2$ cũng là $p$ giá trị riêng lớn nhất của ma trận $$\mathbf{\Sigma}_Y^{-1/2}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_X^{-1}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_Y^{-1/2}$$ với các vector riêng $\mathbf{f}_1, \mathbf{f}_2, ..., \mathbf{f}_p$
- Mỗi $\mathbf{f}_i$ tỉ lệ với $$\mathbf{\Sigma}_Y^{-1/2}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_{X}^{-1}\mathbf{e}_i$$

### Phương pháp giải toán cho mẫu

Một mẫu ngẫu nhiên của $n$ quan sát trên mỗi $

### Suy diễn mẫu lớn

Nếu $$\mathbf{\Sigma}_{XY} = \mathbf{0}_{ p \times q}$$ thì $\text{Cov}(U, V) = \mathbf{a}'\mathbf{\Sigma}_{XY}\mathbf{b} = 0$ với mọi $\mathbf{a}$ và $\mathbf{b}$
- Ám chỉ rằng tất cả những tương quan chính tắc phải bằng không
- Không có lợi ích gì để áp dụng giải thuật CCA cả

Với $n$ lớn, ta loại bỏ $H_0$ : $$\mathbf{\Sigma}_{XY} = \mathbf{0}_{ p \times q}$$ và giữ lại $H_1$ : $$\mathbf{\Sigma}_{XY} \ne \mathbf{0}_{ p \times q}$$ nếu

$$
-2\text{ln}(\Lambda) = n\text{ln}\left(\frac{|\mathbf{S_X}||\mathbf{S_Y}|}{|\mathbf{S}|}\right) = -n\sum_{j=1}^p\text{ln}(1-\hat{\rho}_j^2)
$$

lớn hơn $\mathcal{X}_{pq}^2(\alpha)$

Với một cải tiến để xấp xỉ $\mathcal{X}^2$, Bartlett gợi ý thay thế hệ số co dãn của $n$ bằng $n - 1 - (1/2(p + q + 1))$

$$
-2\text{ln}(\Lambda) = -[n - 1 - (1/ 2)(p + q + 1)]\sum_{j=1}^p\text{ln}(1-\hat{\rho}_j^2)
$$

### Giải thuật CCA

Cho trước tập dữ liệu của 2 tập biến ngẫu nhiên

$$
\mathbf{X}= (X_1, X_2, ..., X_p)'
$$

Và

$$
\mathbf{Y}= (Y_1, Y_2, ..., Y_q)'
$$

Bước 1: Chuẩn hóa các biến mà được phân tích.

Bước 2: Tính ma trận $$\mathbf{\Sigma}_X^{-1/2}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_Y^{-1}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_X^{-1/2}$$ hoặc $$\mathbf{\Sigma}_Y^{-1/2}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_X^{-1}\mathbf{\Sigma}_{XY}\mathbf{\Sigma}_Y^{-1/2}$$

Bước 3: Tìm $ \rho_1^2 \geq  \rho_2^2 \geq ... \geq  \rho_p^2$

Bước 4: Tìm $\mathbf{e}_1, \mathbf{e}_2, ..., \mathbf{e}_p$ và $\mathbf{f}_1, \mathbf{f}_2, ..., \mathbf{f}_p$

Bước 5: Tính $$\mathbf{a}_k = \mathbf{\Sigma}_X^{-1/2}\mathbf{e}_k$$ và $$\mathbf{b}_k = \mathbf{\Sigma}_Y^{-1/2}\mathbf{f}_k$$

Cuối cùng, tổ hợp tuyến tính

$$
U_k = \mathbf{a}_k\mathbf{X}
$$

và

$$
V_k = \mathbf{b}_k\mathbf{Y}
$$

## 4) Ý nghĩa hình học

![]({{site.baseurl}}/contents/msa/cca/cca.jpg)

Các vector $V_x$ và $V_y$ lần lượt là các hình chiếu của các tổ hợp tuyến tính của $x_1, x_2$ và $y_1, y_2$ trên các mặt phẳng $X$, $Y$. Mối tương quan giữa chúng là góc giữa hai vector $V_x$ và $V_y$
