---
layout: single
permalink: /content/msa/classification/classification_part_2
title: "[MSA] Phân lớp - Phần 2"
author_profile: true
toc: true
comments: True
---

## Bài toán phân tách và tách lớp cho hai quần thể

### 1) Phát biểu bài toán

Cho $X = \left(X_1, X_2, ..., X_p\right)'$ là vector ngẫu nhiên

- $f_1(x)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_1$
- $f_2(x)$  là hàm mật độ xác suất (p.d.f) cho quần thể $\pi_2$

Bài toán: Cho một quan sát mới $X = x$, gán nhãn cho $x$ là $\pi_1$ hoặc $\pi_2$

Nhiệm vụ: Cần tìm luật phân lớp (Classification rule) để quyết định gán nhãn cho $X = x$ là  $\pi_1$ hay $\pi_2$, tức là tìm đường (mặt) phân tách hai quần thể

Luật phân lớp (Classification rule): dựa trên hàm phân biệt (Discriminant Function)

**Input**: Cho trước vector $X = \left(X_1, X_2, ..., X_p\right)^{T}$ có nhãn (đã được đánh label $\pi_1$ hoặc $\pi_2$) và một quan sát mới $X = x$

**Output**: gán nhãn cho $x$ là $\pi_1$ hoặc $\pi_2$

### 2) Trực quan hóa bài toán

Cho không gian mẫu $\Omega$, chứa tất cả giá trị có thể có của $\mathbf{x}$

- $R_1$ là tập hợp con của $\Omega$ mà $\mathbf{x}$ được gán nhãn là $\pi_1$
- $R_2 = \Omega - R_1$ là tập hợp con của $\Omega$ mà $\mathbf{x}$ được gán nhãn là $\pi_2$

|![](/contents/msa/classification/figure_11_2.png)|
|:--:|
| Figure 11.2 from Applied Multivariate Statistical Analysis, 6th Ed (Johnson & Wichern). Visualization is for p = 2 variables, page 580 |

### 3) Giải bài toán

Gọi $P(j \|\ i)$ = xác suất của phân lớp sai một quan sát mới có nhãn là $\pi_i$ vào $\pi_j$

Xác suất có điều kiện, $P(2 \|\ 1)$, của việc gán nhãn $\pi_2$ cho một đối tượng, trong khi nó thuộc $\pi_1$

$$
\begin{equation}
\begin{aligned}
P(2|1) = P(X \in R_2 | \pi_1) = \int_{R_2 = \Omega - R_1} f_1(x)dx
\end{aligned}
\end{equation}
$$

Xác suất có điều kiện, $P(1 \|\ 2)$, của việc gán nhãn $\pi_1$ cho một đối tượng, trong khi nó thuộc $\pi_2$

$$
\begin{equation}
\begin{aligned}
P(1|2) = P(X \in R_1 | \pi_2) = \int_{R_1} f_2(x)dx
\end{aligned}
\end{equation}
$$

Khi đó ta có được các xác suất có điều kiện sau khi kết hợp với xác suất tiên nghiệm

Cho $p_1$ và $p_2$ lần lượt là xác suất tiên nghiệm (Prior probabilities) mà một đối tượng tuơng ứng có nhãn $\pi_1$ và $\pi_2$, với điều kiện ràng buộc $p_1 + p_2 = 1$

|![](/contents/msa/classification/figure_11_3.png)|
|:--:|
| Figure 11.3 from Applied Multivariate Statistical Analysis, 6th Ed (Johnson & Wichern). Visualization is for p = 1 variables, page 580 |

Việc phân lớp ở đây là điều chỉnh đường phân lớp sao cho diện tích miền $P(2 \|\ 1)$ và $P(1 \|\ 2)$ đạt giá trị nhỏ nhất, ta có thể suy đoán được vị trí nhỏ nhất đó chính là điểm giao nhau của hai hàm mật độ xác suất


|![](/contents/msa/classification/figure_11_3_splited.png)|
|:--:|
| Figure 11.3 from Applied Multivariate Statistical Analysis, 6th Ed (Johnson & Wichern). Visualization is for p = 1 variables, page 580 |

Ta có công thức xác suất có điều kiện:

$$
\begin{equation}
\begin{aligned}
P(A.B) = P(A).P(B|A) = P(B).P(A|B)
\end{aligned}
\end{equation}
$$

Xét trường hợp bài toán, ta có thể coi xác suất để một đối tượng được gán nhãn là $\pi_{1}$ là một xác suất tiên nghiệm vì nó không phụ thuộc vào các đối tượng khác. Có thể diễn tả xác suất tiên nghiệm theo cách tung đồng xu, mỗi lần tung đồng xu khả năng xuất hiện mặt sấp và mặt ngửa là bằng nhau bất kể kết quả ném trước đó như thế nào. Xác suất tiên nghiệm còn có thể gọi là xác suất đề cho hoặc xác suất do quan sát logic.

- $P$(quan sát được gán đúng nhãn $\pi_1$) = $P$(quan sát đến từ quần thể $\pi_1$ và được gán đúng nhãn) = $P(X \in R_1 \|\ \pi_1)P(\pi_1) = P(1 \|\ 1)p_1$
- $P$(quan sát được gán đúng nhãn $\pi_2$) = $P$(quan sát đến từ quần thể $\pi_2$ và được gán đúng nhãn) = $P(X \in R_2 \|\ \pi_2)P(\pi_2) = P(2 \|\ 2)p_2$
- $P$(quan sát bị gán sai nhãn $\pi_1$) = $P$(quan sát đến từ quần thể $\pi_2$ mà được gán nhãn $\pi_1$) = $P(X \in R_1 \|\ \pi_2)P(\pi_2) = P(1 \|\ 2)p_2$
- $P$(quan sát bị gán sai nhãn $\pi_2$) = $P$(quan sát đến từ quần thể $\pi_1$ mà được gán nhãn $\pi_2$) = $P(X \in R_2 \|\ \pi_1)P(\pi_1) = P(2 \|\ 1)p_1$

Gọi $c(i \|\ j)$ là chi phí phân lớp sai đối tượng từ $i$ vào $j$ với $i, j=1,2$

Ta có thể biểu diễn chi phi phân lớp sai bằng vào cost matrix dưới đây:

|![](/contents/msa/classification/classification_table.png)|
|:--:|
|Classification Table |

Ta sẽ ước lượng một hàm tính chi phí tốn kém và mong muốn rằng chi phí ấy là nhỏ nhất. Cách đơn giản nhất để ước lượng được hàm này chính là tổng chi phí phân lớp sai ở mỗi quần thể:

Total probability of misclassification (Tổng xác suất phân lớp sai)

$$
\begin{equation}
\begin{aligned}
TPM = p_1P(2|1) + p2_P(1|2)
\end{aligned}
\end{equation}
$$

Expected cost of misclassification (Kỳ vọng giá trị phân lớp sai)

$$
\begin{equation}
\begin{aligned}
(ECM) =  c(2|1)(p_1P(2|1)) + c(1|2)(p_2P(1|2))
\end{aligned}
\end{equation}
$$

Nhiệm vụ: Tìm cách tối ưu phân hoạch $\{R_1, R_2\}$ của $X$ để mà TPM là nhỏ nhất hoặc ECM là nhỏ nhất.

Như đã biết:

$$
\begin{equation}
\begin{aligned}
ECM =  c(2|1)(p_1P(2|1)) + c(1|2)(p_2P(1|2))\\
ECM= c(2|1)p_1\int_{R_2 = \Omega - R_1} f_1(x)dx + c(1|2)p_2 \int_{R_1} f_2(x)dx
\end{aligned}
\end{equation}
$$

Do, $\Omega = R_1 \cup R_2$:

$$
\begin{equation}
\begin{aligned}
1=\int_{R_2 = \Omega - R_1} f_1(x)dx + \int_{R_1} f_1(x)dx
\end{aligned}
\end{equation}
$$

Viết lại ECM:

$$
\begin{equation}
\begin{aligned}
ECM = c(2|1)p_1\left[1-\int_{R_1} f_1(x)dx\right] + c(1|2)p_2 \int_{R_1} f_2(x)dx
\\
ECM = \int_{R_1} [c(1|2)p_2f_2(x) - c(2|1)p_1f_1(x)]dx + c(2|1)p_1
\end{aligned}
\end{equation}
$$

Giá trị nhỏ nhất xảy ra khi $R_1$ là miền làm cho biểu thức trong ngoặc dấu tích phân nhỏ hơn hoặc 0, nghĩa là:

$$
\begin{equation}
\begin{aligned}
c(1|2)p_2f_2(x) - c(2|1)p_1f_1(x) \leq 0 \\
\Leftrightarrow c(2|1)p_1f_1(x) \geq c(1|2)p_2f_2(x) \\
\Leftrightarrow \frac{f_1(x)}{f_2(x)} \geq \left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p_2}{p_1}\right)
\end{aligned}
\end{equation}
$$

Còn trong $R_2$ khi

$$
\begin{equation}
\begin{aligned}
\frac{f_1(x)}{f_2(x)} < \left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p_2}{p_1}\right)
\end{aligned}
\end{equation}
$$

Vậy, ta có thể kết luận để rút ra một luật phân lớp cho một quan sát mới vào $X=x$ như sau:

Giá trị $x$ thuộc vào $R_{1}$ khi thõa:

$$
\begin{equation}
\begin{split}
R_1: \frac{f_1(x)}{f_2(x)} \geq \left(\frac{c(1|2)}{c(2|1)}\right) \left(\frac{p_2}{p_1}\right)
\end{split}
\end{equation}
$$

Giá trị $x$ thuộc vào $R_{2}$ khi thõa

$$
\begin{equation}
\begin{split}
R_2: \frac{f_1(x)}{f_2(x)} < \left(\frac{c(1|2)}{c(2|1)}\right)\left(\frac{p_2}{p_1}\right)
\end{split}
\end{equation}
$$

Trong đó:

- Tỉ lệ mật độ - Density ratio: $\frac{f_1(x)}{f_2(x)}$
- Tỉ lệ chi phí - Cost ratio: $\frac{c(1 \|2)}{c(2 \|1)}$
- Tỉ lệ xác suất tiên nghiệm - Prior probability ratio: $\frac{p_2}{p_1}$

**Các trường hợp đặc biệt**

Trường hợp $\frac{p_2}{p_1} = 1$:

$$
\begin{equation}
        \begin{split}
		R_1: \frac{f_1(x)}{f_2(x)} \geq \frac{c(1|2)}{c(2|1)} \\ R_2: \frac{f_1(x)}{f_2(x)} < \frac{c(1|2)}{c(2|1)}
		\end{split}
        \end{equation}
        $$

Trường hợp $\frac{c(1 \|2)}{c(2\|1)} = 1$

$$
\begin{equation}
        \begin{split}
		R_1: \frac{f_1(x)}{f_2(x)} \geq \frac{p_2}{p_1}; R_2: \frac{f_1(x)}{f_2(x)} < \frac{p_2}{p_1}
		\end{split}
        \end{equation}$$

Trường hợp $\frac{p_2}{p_1} = \frac{c(1\|2)}{c(2\|1)} = 1$ hoặc $\frac{p_2}{p_1} = \frac{1}{\frac{c(1\|2)}{c(2\|1)}}$

$$
\begin{equation}
        \begin{split}
	    R_1: \frac{f_1(x)}{f_2(x)} \geq 1; R_2: \frac{f_1(x)}{f_2(x)} < 1
	    \end{split}
        \end{equation}

$$
