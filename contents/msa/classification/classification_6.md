---
layout: single
permalink: /content/msa/classification/classification_part_6
title: "[MSA] Phân lớp - Phần 6"
author_profile: true
toc: true
comments: True
---

## Phát biểu bài toán

Cho $X = \left(X_1, X_2, ..., X_p\right)'$ là vector ngẫu nhiên

- $f_1(x)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_1$
- $f_2(x)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_2$
- ...
- $f_n(x)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_n$

Bài toán: Cho một quan sát mới $X = x$, gán nhãn cho $x$ là $\pi_1$ hoặc $\pi_2$ ... hoặc $\pi_g$

Nhiệm vụ: Cần tìm luật phân lớp (Classification rule) để quyết định gán nhãn cho $X = x$ là  $\pi_1$ hay $\pi_2$ ...  hay $\pi_g$, tức là tìm đường (mặt) phân tách các quần thể

Luật phân lớp (Classification rule): dựa trên hàm phân biệt (Discriminant Function)

Giả sử, ta gọi $\Omega$ là không gian mẫu chứa tất cả các giá trị có thể có của $x$

- $R_{1} \in \Omega$ là một tập con trong không gian mẫu $\Omega$, đại diện cho quần thể có nhãn là $\pi_{1}$
- $R_{2} \in \Omega$ là một tập con trong không gian mẫu $\Omega$, đại diện cho quần thể có nhãn là $\pi_{2}$
- $R_{3} \in \Omega$ là một tập con trong không gian mẫu $\Omega$, đại diện cho quần thể có nhãn là $\pi_{3}$
- ...
- $R_{g} \in \Omega$ là một tập con trong không gian mẫu $\Omega$, đại diện cho quần thể có nhãn là $\pi_{g}$

Ta có tính chất:
$$\Omega = R_{1} \cap R_{2} \cap R_{3} \cap ... \cap R_{n}$$

$$R_{i} \neq R_{j}, \forall i \neq j$$

|![](/contents/msa/classification/figure_11_10.png)|
|:--:|
| Figure 11.10 from Applied Multivariate Statistical Analysis, 6th Ed (Johnson & Wichern) |

## Giải quyết bài toán

Xác suất có điều kiện $P(l \|\ k)$ của việc phân lớp một quan sát vào $\pi_l$ trong khi quan sát này thật sự thuộc về $\pi_k$

$$(l|k) = P(X \in R_{l} | \pi_k) = \int_{R_l}f_{k}(x)dx$$

Với mọi $k \ne l$ với $$k, l \in \{1, ..., g\}$$

Gọi $c(l \|\ k)$ là chi phí cho việc phân bổ một quan sát vào $\pi_l$ trong khi nó thật sự thuộc về $\pi_k$, và gọi $p_k$ là xác suất tiên nghiệm của $\pi_k$

Ta có giá trị chi phí kỳ vọng của việc phân lớp sai một quan sát từ $\pi_k$:

$$ECM(k) = \sum_{l \ne k}P(l|k)c(l|k)$$

Khi kết hợp với xác suất tiên nghiệm, ta có ECM tổng thể như sau

$$ECM = \sum_{k=1}^gp_kECM(k) = \sum_{k=1}^gp_k\left[\sum_{l \ne k}P(l|k)c(l|k)\right]$$

Các vùng phần lớp $\{R_1, R_2, ..., R_g\}$ cực tiểu ECM được định nghĩa bằng cách phân bổ $X = x$ vào quần thể $\pi_k$ mà cực tiểu được

$$\sum_{l \ne k}p_lf_l(x)c(k|l)$$
