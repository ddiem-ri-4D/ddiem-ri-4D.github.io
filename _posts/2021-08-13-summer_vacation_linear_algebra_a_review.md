---
title: "Giải trí mùa hè - Review Linear Algebra"
categories:
  - Mathematics
tags:
  - Mathematics
toc: true
comments: true
header:
  teaser: "/assets/images/header/lambda_01.jpg"
---

Ghi và dịch ra Tiếng Việt từ Mathematics for Machine Learning của Garrett Thomas, Department of Electrical Engineering and Computer Sciences, University of California, Berkeley nhằm ôn tập và tổng hợp lại kiến thức Toán cho Học Máy.

## Không gian Vector - Vector spaces

Không gian Vector là cơ sở trong việc hình thành Đại số tuyến tính. Một không gian Vector - vector space $V$ là một tập hợp (trong đó những phần tử được gọi là những **vector**) được định nghĩa hai toán tử trên nó: những vector có thể được cộng với nhau, và những vector có thể được nhân với số thực được gọi là **scalars**

1) Tồn tại một đơn vị cộng (an additive identity), được viết là $0$ trong $V$ mà $x + 0 = x$ với mọi $x \in V$

2) Với mọi $x \in V$, tồn tại một đơn vị nghịch đảo (an additive inverse), được viết là $-x$ sao cho $x + (-x) = 0$

3) Tồn tại một đơn vị nhân (a multiplicative identity), được viết là 1 trong $\mathbb{R}$ mà $1x = x$ với mọi $x \in V$

4) Tính giao hoán (Commutativity): $x + y = y + x$ với mọi $x, y \in V$

5) Tính kết hợp (Associativity): $(x+y)+z = x + (y + z)$ và $\alpha(\beta x) = (\alpha\beta)x$ với mọi $x, y,z \in V$ và $\alpha, \beta \in \mathbb{R}$

6) Tính phân phối (Distributivity): $\alpha(x + y) = \alpha x + \alpha y$ và $(\alpha + \beta)x = \alpha x + \beta x$ với  $x, y \in V$ và $\alpha, \beta \in \mathbb{R}$

Một tập hợp các vector $v_1, v_2, ..., v_n \in V$ được gọi là độc lập tuyến tính (**linearly independent**) nếu

$$
\alpha_1v_1 + \alpha_2v_2 + ... + \alpha_nv_n = 0 \text{  kéo theo } $\alpha_1 = \alpha_2 = ... = \alpha_n$
$$

Bao (span) của $v_1, v_2, ..., v_n \in V$ là tập hợp tất cả những vector mà có thể được thể hiện bằng sự tổ hợp tuyến tính của chúng

$$
span\{v_1, v_2, ..., v_n\} = \{v\in V: \exists \alpha_1, \alpha_2, ..., \alpha_n \text{ mà } \alpha_1v_1 + \alpha_2v_2 + ... + \alpha_nv_n = v\}
$$

Nếu một tập hợp những vector là độc lập tuyến tính (linearly independent) và bao (span) của nó là toàn bộ V, những vector này được gọi là một **cơ sở** (**basis**) của V. Một cách tổng quát, mọi tập vector độc lập tuyến tính đều tạo thành cơ sở cho bao của nó

Nếu một không gian vector được bao bởi một số lượng hữu hạn vector, nó được gọi là **finite-dimensional** - có chiều hữu hạn. Trường hợp còn lại, nó gọi là **infinite-dimensional** - vô hạn chiều. Số lượng vector trong một cơ sở cho một không gian Vector hữu hạn chiều V được gọi là **dimension** - chiều của **V** và được ký hiệu là $dimV$

### Không gian Euclidean (Euclidean spaces)

Không gian Vector thông thường là **Không gian Euclidean** (**Euclidean spaces**), chúng ta ký hiệu là $\mathbb{R}$. Những vector trong không gian này bao gồm n-tuples số thực

$$
\mathbf{x} = (x_1, x_2, ..., x_n)
$$

Để dễ dàng, nó thường được nhìn bằng dạng một ma trật $n \times 1$ hoặc có thể gọi là vector cột (**column vector**)

$$
\mathbf{x} = \begin{bmatrix}x_1\\x_2\\...\\x_n\end{bmatrix}
$$

Phép cộng (addition) và nhân với một số (scalar multiplication) được định nghĩa trên những vector trong  $\mathbb{R}^n$

$$
\mathbf{x} + \mathbf{y} =  \begin{bmatrix}x_1 + y_1\\x_2 + y_2\\...\\x_n + y_n\end{bmatrix}
$$

$$
\alpha\mathbf{x} = \begin{bmatrix}\alpha x_1\\ \alpha x_2\\...\\ \alpha x_n\end{bmatrix}
$$

Không gian Euclidean được sử dụng để đại diện không gian vật lý một cách Toán học, với những khái niệm như khoảng cách (distance), độ dài (length) và góc (angles). Mặc dù nó trở nên khó hơn khi trực quan với số chiều $n > 3$, những khái niệm này về mặt toán học theo cách tổng quát hóa rõ ràng. Mặc dù bạn đang làm việc trong một trường hợp tổng quát hơn $\mathbb{R}^n$, nó thường hữu ích để trực quan phép cộng và nhân với một số trong thuật ngữ vector 2 chiều (2D vectors) trong một mặt phẳng (plane) hay vector 3 chiều (3D vectors) trong không gian.

### Không gian con (Subspaces)

Không gian vector có thể chứa những không gian vector khác. Nếu $V$ là một không gian vector, $S \subseteq V$ được gọi là một không gian con của $V$ nếu

1) $0 \in S$

2) $S$ là tập đóng với phép cộng: $\mathbf{x}, \mathbf{y} \in S$ kéo theo $\mathbf{x} + \mathbf{y} \in S$

3) $S$ là tập đóng với phép nhân với một số (scalar): $\mathbf{x} \in S, \alpha \in \mathbb{R}$ kéo theo $\alpha\mathbf{x} \in S$

Để ý rằng $V$ luôn là một không gian con của $V$, vì là một không gian vector tầm thường chỉ chứa 0

Ví dụ cụ thể, một đường thẳng đi qua gốc tọa độ (orgin) là một không gian con của không gian Euclidean

Nếu $U$ và $W$ là những không gian con của $V$, thì tổng của chúng được định nghĩa

$$
U + W = \{\mathbf{u} + \mathbf{w} |\mathbf{u} \in U, \mathbf{w} \in W\}
$$

Thật đơn giản để xác minh rằng tập hợp này cũng là một không gian con của $V$. Nếu $U \cap W = \{0\}$, tổng được gọi là tổng trực tiếp (**direct sum**) và được viết là $U \bigoplus W$. Với mọi vector trong $U \bigoplus W$ có thể được viết như sau $\mathbf{u} + \mathbf{w}$ với $\mathbf{u} \in U$ và $\mathbf{w} \in W$ (Đây vừa là điều kiện cần và điều kiện đủ để có tổng trực tiếp)

Số chiều của tổng của không gian con liên hệ với nhau như sau:

$$
dim(U+W) = dimU + dimW - dim(U \cap W)
$$

Và

$$
dim(U \bigoplus W) = dimU + dimW
$$

Vì $dim(U \cap W) = dim(\{0\}) = 0$ nếu tổng là tổng trực tiếp.

## Ánh xạ tuyến tính - Linear maps

Một **ánh xạ tuyến tính (linear maps)** là một hàm $T: V \rightarrow W$ trong đó $V$ và $W$ là những không gian vector, thỏa

1) $T(\mathbf{x} + \mathbf{y}) = T\mathbf{x} + T\mathbf{y}$ với mọi $\mathbf{x}, \mathbf{y} \in V$

2) $T(\alpha\mathbf{x}) = \alpha T\mathbf{x}$ với mọi $\mathbf{x} \in V, \alpha \in \mathbb{R}$

Một ánh xạ tuyến tính từ $V$ đến chính nó được gọi là một toán tử tuyến tính (**linear operator**)

Quan sát rằng định nghĩa của một ánh xạ tuyến tính phù hợp để phản ánh cấu trúc của không gian vector, vì nó bảo tồn hai toán hạng của không gian vector là phép cộng (addition) và phép nhân scalar (scalar multiplication). Trong thuật ngữ Đại số, một ánh xạ tuyến tính gọi là **homomorphism** - đồng cấu của không gian vector. Phép đồng cấu không thể đảo ngược (trong đó phép nghịch đảo cũng là phép đồng cấu) được gọi là **isomorphism** - đẳng cấu. Nếu tồn tại một đẳng cấu từ $V$ đến $W$, thì $V$ và $W$ được gọi là đẳng tích (isomorphic) và chúng ta viết $V \cong W$. Không gian vector đẳng cấu (Isomorphic vector space) về cơ bản là “giống nhau” về cấu trúc đại số của chúng.Có một thực tế thú vị là không gian vectơ hữu hạn chiều có cùng thứ nguyên (dimensional) luôn là đẳng cấu; Nếu $V, W$ là những không gian vector thực với $dimV = dimW = n$, thì chúng ta có đẳng cấu tự nhiên (natural isomorphism)

$$
\begin{gather*}
\varphi : V \rightarrow W\\
\alpha_1v_1 + \alpha_2v_2 + ... + \alpha_nv_n \rightarrow \alpha_1w_1 + \alpha_1w_2 + ... + \alpha_nw_n    
\end{gather*}
$$

Trong đó: $v_1, v_2, ..., v_n$ và $w_1, w_2, ..., w_n$ là bất kỳ cơ sở nào của $V$ và $W$. Ánh xạ này được xác định rõ ràng vì mọi vector trong $V$ có thể được biểu diễn đơn nhất như một tổ hợp tuyến tính (linear combination) của $v_1, v_2, ..., v_n$. Thật đơn giản để xác minh rằng $\varphi$ là một đẳng cấu, vì vậy trên thực tế $V \cong W$. Đặc biệt, với mọi không gian vector n chiều thực là đẳng cấu với $\mathbb{R}^n$

### Dạng ma trận của một ánh xạ tuyến tính

Không gian vector khá là trừu tượng. Để đại diện (represent) và thao tác (manipulate) những vector và ánh xạ tuyến tính trên máy tính, chúng ta sử dụng những mảng hình chữ nhật của những số được gọi là những ma trận (matrices)

Giả sử $V$ và $W$ là những không gian vector hữu hạn chiều với những cơ sở
$\mathbf{v}\_1, \mathbf{v}\_2, ..., \mathbf{v}\_n$ và $\mathbf{w}\_1, \mathbf{w}\_2, ..., \mathbf{w}\_m$ tương ứng và $T: V \rightarrow W$ là một ánh xạ tuyến tính. Dạng ma trận của $T$, với $A_{ij}$ trong đó $i = 1...m, j = 1...n$ được định nghĩa bởi

$$
T\mathbf{v}_j = A_{1j}\mathbf{w}_1 + ... + A_{mj}\mathbf{w}_m
$$

Cột thứ $j$ của $\mathbf{A}$ gồm các tọa độ của $T_\mathbf{v_j}$ trong cơ sở được chọn của $W$

Ngược lại, với mọi ma trận $\mathbf{A} \in \mathbb{R}^{m \times n}$ tạo ra một ánh xạ tuyến tính $T: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$ được cho bởi:

$$
T\mathbf{x} = \mathbf{A}\mathbf{x}
$$

và ma trận của ánh xạ này với đối với những cơ sở chuẩn của $\mathbb{R}^{n}$ và $\mathbb{R}^{m}$ là $\mathbf{A}$

Nếu $\mathbf{A} \in \mathbb{R}^{m \times n}$, chuyển vị (transpose) của nó $A^T \in \mathbb{R}^{n \times m}$ được cho bởi $(\mathbf{A}^T)\_{ij} = A_{ji}$ với mỗi $(i, j)$. Nói một cách khác, những cột của $\mathbf{A}$ trở thành những dòng của $\mathbf{A}^T$ và những cột của $\mathbf{A}$ trở thành dòng của  $\mathbf{A}^T$

Phép chuyển vị có một số tính chất thú vị vị như sau:

i) $(\mathbf{A}^T)^T = \mathbf{A}$

ii) $(\mathbf{A} + \mathbf{B})^T = \mathbf{A}^T + \mathbf{B}^T$

iii) $(\alpha\mathbf{A})^T = \alpha\mathbf{A}^T$

iv) $(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T\mathbf{A}^T$

### Không gian rỗng (Nullspace), khoảng (range)

Một vài không gian con quan trọng được tạo ra bởi ánh xạ tuyến tính. Nếu $T: V \rightarrow W$ là một ánh xạ tuyến tính, chúng ta định nghĩa không gian rỗng (nullspace) của $T$

$$
null(T) = \{\mathbf{v} \in V | T\mathbf{v} = 0\}
$$

và khoảng (range) của $T$

$$
range(T) = \{ \mathbf{w} \in W | \exists \mathbf{v} \in V \text{ such that } T\mathbf{v} =  \mathbf{w}\}
$$

Không gian cột (**columnspace**) của một ma trận $\mathbf{A} \in \mathbb{R}^{m \times n}$ là bao của những cột của nó (xem như những vector trong không gian $\mathbb{R}^m$) và tương tự không gian dòng (**rowspace**) của $\mathbf{A}$ là bao của các dòng của nó (xem như những vector trong không gian $\mathbb{R}^m$). Nó không khó để thấy được rằng không cột của $\mathbf{A}$ chính xác là khoảng của ánh xạ tuyến tính từ $\mathbb{R}^n$ vào $\mathbb{R}^m$ mà được tạo ra bởi $\mathbf{A}$, thế nên chúng ta biểu diễn nó bởi range($\mathbf{A}$) trong một sự lạm dụng nhẹ ký hiệu. Tương tự, không gian dòng được biểu diễn range($\mathbf{A}^T$)

Một điều đáng chú ý là chiều của không gian cột của $\mathbf{A}$ là cùng số chiều với không gian dòng của $\mathbf{A}$. Định lượng này gọi là hạng (rank) của $\mathbf{A}$

$$
rank(\mathbf{A}) = dim(range(\mathbf{A}))
$$

## Không gian metric

Metrics tổng quát hóa khái niệm khoảng cách từ không gian Euclidean (mặc dù không gian metric không nhất thiết là không gian vector)

Một metric trên một tập $S$ là một hàm $d: S \times S \rightarrow \mathbb{R}$ mà thỏa:

1) $d(x, y) \geq 0$ với dấu đẳng thức xảy ra khi và chỉ khi $x = y$

2) $d(x, y) = d(y, x)$

3) $d(x, z) \leq d(x, y) + d(y, z)$ (được gọi là bất đẳng thức tam giác - triangle inequality)

với mọi $x, y, z \in S$

Động lực chính cho metric là chúng cho phép giới hạn để định nghĩa đối tượng toán học hơn là số thực. Chúng ta nói rằng một chuỗi $\{x_n\} \subseteq S$ hội tụ về giới hạn $x$ nếu với mọi $\epsilon > 0$, tồn tại $N \in \mathbb{N}$ mà $d(x_n,x) < \epsilon$ với mọi $n \geq N$. Để ý rằng định nghĩa cho giới hạn của chuỗi của số thực, mà bạn được học trong mấy cái lớp Giải tích, là một trường hợp đặc biệt của cái định nghĩa này khi sử dụng metric $d(x, y) = \|x - y\|$

## Không gian định chuẩn - Normed spaces

Chuẩn tổng quát hóa khái niệm độ dài - length từ không gian Euclidean

Một chuẩn (**norm**) trên một không gian vector thực $V$ là một hàm $\|\|.\|\|:V \rightarrow \mathbb{R}$ thỏa:

1) $\|\|\mathbf{x}\|\| \geq 0$ với dấu dẳng thức xảy ra khi và chỉ khi $x = 0$

2) $\|\|\alpha \mathbf{x}\|\| = \|\alpha\|\|\|\mathbf{x}\|\|$

3) $\|\|\mathbf{x} + \mathbf{y}\|\| \leq \|\|\mathbf{x}\|\| + \|\|\mathbf{y}\|\|$ (bất đẳng thức tam giác giác)

với mọi $x, y \in V$ và tất cả $\alpha \in \mathbb{R}$. Một không gian vector với một chuẩn được gọi là không gian vector định chuẩn (normed vector space) hoặc một cách đơn giản hơn là một không gian chuẩn (nromed space)

Lưu ý rằng, bất kỳ chuẩn nào trên $V$ tạo ra một khoảng cách metric trên $V$

$$
d(\mathbf{x}, \mathbf{y}) = ||\mathbf{x}-\mathbf{y}||
$$

Người ta có thể xác minh rằng các tiên đề cho các metric được thỏa mãn theo định nghĩa này và theo dõi trực tiếp từ các tiên đề cho các chuẩn. Do đó bất kỳ không gian định chuẩn nào cũng được gọi là không gian metric. Nếu một không gian định chuẩn là đầy đủ với khoảng cách metric tương ựng được tạo ra bởi chuẩn của nó, chúng ta nói rằng nó là một không gian Banach (Banach space)

Chúng ta sẽ thường chỉ quan tâm đến một vài chuẩn cụ thể trên không gian $\mathbb{R}^n$

$$
||x||_1 = \sum_{i=1}^n|x_i|
$$

$$
||x||_2 = \sqrt{\sum_{i=1}^nx_i^2}
$$

$$
||x||_p = \left(\sum_{i=1}^n|x_i|^p\right)^{\frac{1}{p}}, (p \geq 1)
$$

$$
||x||_{\infty} = \underset{1 \leq i \leq n}{\text{ max }}|x_i|
$$

Để ý rằng 1- và 2-norms là những trường hợp đặc biệt của $p$-norm, và $\infty$-norm là giới hạn của $p$-norm khi $p$ tiến ra vô cùng. Chúng ta cần $p \geq 1$ cho định nghĩa tổng quát của $p$-norm bởi vì bất đẳng thức tam giác không đạt được nếu mà $p < 1$

Và ở đây có một điều thú vị là: với bất kỳ không gian vector hữu hạn chiều $V$ nào, tất cả chuẩn trên $V$ tương đương với nghĩa là với hai chuẩn $\|\| \cdot \|\|_A$ và $\|\| \cdot \|\|_B$, tồn tại những hằng số $\alpha$, $\beta$ dương sao cho

$$
\alpha||\mathbf{x}||_A \leq ||\mathbf{x}||_B \leq \beta||\mathbf{x}||_A
$$

với mọi $x \in V$. Do đó hội tụ trong một chuẩn kéo theo hội tụ trong bất kỳ chuẩn nào khác. Luật này có thể không được áp dụng cho không gian vector vô hạn chiều như không gian hàm số (function spaces)

## Không gian tích trong - Inner product spaces

Một tích trong (inner product) trên một không gian vector thực $V$ là một hàm $\left<\cdot, \cdot \right>: V \times V \rightarrow \mathbb{R}$ thỏa

i) $\left<\mathbf{x}, \mathbf{x}\right> \geq 0$ với dấu đẳng thức xảy xa nếu và chỉ nếu $x = 0$

ii) $\left<\mathbf{x} + \mathbf{y}, \mathbf{z}\right> = \left<\mathbf{x}, \mathbf{z}\right> + \left<\mathbf{y}, \mathbf{z}\right>$ và $\left<\alpha \mathbf{x}, \mathbf{y}\right> = \alpha\left<\mathbf{x}, \mathbf{y}\right>$

iii) $\left<\mathbf{x}, \mathbf{y}\right> = \left<\mathbf{y}, \mathbf{x}\right>$

với mọi $\mathbf{x}, \mathbf{y}, \mathbf{z} \in V$ và mọi $\alpha \in \mathbb{R}$. Một không gian vector có một tích trong được gọi là một không gian tích trong (**inner product space**)

Lưu ý rằng bất kỳ tích trong nào trên $V$ cũng tạo ra một chuẩn trên $V$:

$$
||\mathbf{x}|| = \sqrt{\left<\mathbf{x}, \mathbf{x}\right>}
$$

Người ta có thể xác minh rằng các tiên đề cho các metric được thỏa mãn theo định nghĩa này và theo dõi trực tiếp từ các tiên đề cho các tích trong. Do đó bất kỳ không gian tích trong nào cũng được gọi là không gian định chuẩn (và do đó cũng là một không gian metric). Nếu một không gian tích trong là đầy đủ với khoảng cách metric tương ứng được tạo ra bởi tích trong của nó, chúng ta gọi đó là **không gian Hilbert** (**Hilbert space**)

Hai vector $x$ và $y$ được gọi là trực giao (**orthogonal**) nếu $\left<x, y\right> = 0$, ta viết là $x \perp y$ cho nó gọn. Trực giao tổng quát hóa khai niệm vuông góc (perpendicularity) từ không gian Euclidean. Nếu hai vector trực giao $x$ và $y$ có độ dài đơn vị, tức là $\|\|\mathbf{x}\|\| = \|\|\mathbf{y}\|\| = 1$, chúng ta gọi nó là trực chuẩn (**orthonormal**)

Tích trong chuẩn trên không gian $\mathbb{R}^n$ được cho bởi:

$$
\left<x, y\right> = \sum_{i=1}^nx_iy_i = \mathbf{x}^T\mathbf{y}
$$


### Định lý Pythagorean (Pythagorean Theorem)

Định lý Pythagorean nổi tiếng khái quát một cách tự nhiên đến các không gian tích trong (inner product spaces)

**Theorem 1**. Nếu $\mathbf{x} \perp \mathbf{y}$ thì

$$
||\mathbf{x} + \mathbf{y}||^2 = ||\mathbf{x}||^2 + ||\mathbf{y}||^2
$$

*Chứng minh*: Giả sử rằng $\mathbf{x} \perp \mathbf{y}$ tức là $\left<\mathbf{x}, \mathbf{y}\right> = 0$ thì

$$
||\mathbf{x} + \mathbf{y}||^2 = \left<\mathbf{x} + \mathbf{y}, \mathbf{x} + \mathbf{y}\right> = \left<\mathbf{x}, \mathbf{x}\right> + \left<y, \mathbf{x}\right> + \left<\mathbf{x}, \mathbf{y}\right> + \left<\mathbf{y}, \mathbf{y}\right> = ||\mathbf{x}||^2 + ||\mathbf{y}||^2
$$

Kết luận điều phải chứng minh.

### Bất đẳng thức Cauchy-Schwarz (Cauchy-Schwarz inequality)

$$
|\left<\mathbf{x}, \mathbf{y}\right>| \leq ||\mathbf{x}||\text{ }||\mathbf{y}||
$$

với mọi $\mathbf{x}, \mathbf{y} \in V$. Dấu đẳng thức xảy ra khi $\mathbf{x}$ và $\mathbf{y}$ là những scalars nhân với nhau (hay nói cách khác, là khi chúng độc lập tuyến tính)

### Phần bù trực giao (Orthogonal complements) và Phép chiếu (projections)

Nếu $S \subseteq V$ trong đó $V$ là không gian tích trong, thì phần bù trực giao (orthogonal complement) của $S$, đặt là $S^{\perp}$, là tập tất cả những vector trong $V$ mà trực giao với mọi thành phần của $S$

$$
S^{\perp} = \{\mathbf{v} \in V | \mathbf{v} \perp \mathbf{s} \text{ for all } \mathbf{s} \in S\}
$$

Rất dễ dàng để xác nhận rằng $S^{\perp}$ là một không gian con của $V$ với bất kỳ $S \subseteq V$. Để ý rằng không có yêu cầu rằng bản thân $S$ là một không gian con của $V$. Tuy nhiên nếu $S$ là một (hữu hạn chiều) không gian con của $V$, chúng ta có vài thứ quan trọng sau đây:

**Mệnh đề 1** Gọi $V$ là một không gian tích trong (inner product space) và $S$ là một không gian gian con hữu hạn chiều của $V$. Thì với mọi $\mathbf{v} \in V$ có thể được viết dưới dạng đơn nhất sau đây:

$$
\mathbf{v} = \mathbf{v}_S + \mathbf{v}_{\perp}
$$

Trong đó $\mathbf{v_S} \in S$ và $\mathbf{v}\_{\perp} \in S^{\perp}$

*Chứng minh*. Gọi $\mathbf{u}_1, \mathbf{u}_2, ..., \mathbf{u}_m$ là cơ sở trực chuẩn của $S$ và giả định $\mathbf{v} \in V$. Định nghĩa:

$$
\mathbf{v}_S = \left<\mathbf{v}, \mathbf{u_1}\right>\mathbf{u_1} + ... + \left<\mathbf{v}, \mathbf{u_m}\right>\mathbf{u_m}
$$

và

$$
\mathbf{v}_{\perp} = \mathbf{v} - \mathbf{v}_S
$$

Dễ dàng thấy rằng $\mathbf{v}_S \in S$ bởi vì nó là trong bao của cơ sở được chọn. Ta có, với mọi $i = 1...m$

$$
\begin{gather}
\left<\mathbf{v}_{\perp}, \mathbf{u}_i\right> = \left<\mathbf{v} - (\left<\mathbf{v}, \mathbf{u}_1\right>\mathbf{u}_1 + ... + \left<\mathbf{v}, \mathbf{u}_m\right>\mathbf{u}_m), \mathbf{u}_i\right>\\
= \left<\mathbf{v}, \mathbf{u}_i\right> - \left<\mathbf{v}, \mathbf{u}_1\right>\left<\mathbf{u}_1, \mathbf{u}_i\right> - ... - \left<\mathbf{v}, \mathbf{u}_m\right>\left<\mathbf{u}_m, \mathbf{u}_i\right> \\
= \left<\mathbf{v}, \mathbf{u}_i\right> - \left<\mathbf{v}, \mathbf{u}_i\right>  = 0
\end{gather}
$$

mà kéo theo $\mathbf{v}_{\perp} \in S^{\perp}$



## Trị riêng - Eigenthings

Với một ma trận $\mathbf{A} \in \mathbb{R}^{n \times n}$, có thể là những vector, khi $\mathbf{A}$ tác động lên chúng, thì đơn giản là bị co dãn bởi một vài hằng số nào đó (constant). Chúng ta gọi đó là những vector khác 0 (nonzero vector) $\mathbf{x} \in \mathbb{R}^n$ là một vector riêng (**eigenvector**) của $\mathbf{A}$ tương ứng với trị riêng (**eigenvalue**) $\lambda$ nếu

$$
\mathbf{A}\mathbf{x} = \lambda\mathbf{x}
$$

Những vector không bị loại trừ bởi định nghĩa trên là do $\mathbf{A}0 = 0 = \lambda 0$ với mọi $\lambda$

**Mệnh đề 3**. Gọi $\mathbf{x}$ là một vector riêng của $\mathbf{A}$ với giá trị riêng tương ứng là $\lambda$. thì

i) Với mọi $\gamma \in \mathbb{R}$, $\mathbf{x}$ là một vector riêng của $\mathbf{A} + \gamma \mathbf{I}$ với giá trị riêng $\lambda + \gamma$

ii) Nếu $\mathbf{A}$ khả nghịch, thì $\mathbf{x}$ là một vector riêng của $\mathbf{A}^{-1}$ với giá trị riêng $\lambda^{-1}$

iii) $\mathbf{A}^k\mathbf{x} = \lambda^k\mathbf{x}$ với bất kỳ $k \in \mathbb{Z}$ nào (trong đó $\mathbf{A}^0 = \mathbf{I}$)

## Vết - Trace

Vết (trace) của một ma trận vuông là tổng của những phần tử trên đường chéo chính của nó

$$
tr(\mathbf{A}) = \sum_{i=1}^nA_{ii}
$$

Tính chất đại số:

i) $tr(\mathbf{A} + \mathbf{B}) = tr(\mathbf{A}) + tr(\mathbf{B}) $

ii) $tr(\mathbf{\alpha A}) = \alpha tr(\mathbf{A})$

iii) $tr(\mathbf{A}^T) = tr(\mathbf{A})$

iv) $tr(\mathbf{ABCD}) = tr(\mathbf{BCDA}) = tr(\mathbf{CDAB}) = tr(\mathbf{DABC})$ (bất biến với phép quay - invariance under cyclic permutations)

Một điều thú vị, vết của một ma trận bằng với tổng của những giá trị riêng của nó

$$
tr(\mathbf{A}) = \sum_{i}\lambda_i(\mathbf{A})
$$

## Định thức - Determinant

Định nghĩa của định thức có thể được định nghĩa theo nhiều cách khác nhau, các bạn có thể tham khảo [Wikipedia của nó](https://en.wikipedia.org/wiki/Determinant) để biết thêm chi tiết. Chúng ta nên nhớ những tính chất thú vị của nó

i) $det(\mathbf{I}) = 1$

ii) $det(\mathbf{A}^T) = det(\mathbf{A})$

iii) $det(\mathbf{AB}) = det(\mathbf{A})det(\mathbf{B})$

iv) $det(\mathbf{A}^{-1}) = det(\mathbf{A})^{-1}$

v) $det(\alpha\mathbf{A}) = \alpha^ndet(\mathbf{A})$

Thú vị hơn nữa là, định thức của một ma trận bằng với tích của những vector riêng của nó

$$
det(\mathbf{A}) = \prod_{i}\lambda_i(\mathbf{A})
$$

## Ma trận trực giao - Orthogonal matrices

Một ma trận $\mathbf{Q} \in \mathbb{R}^{n \times n}$ được gọi là trực giao nếu các cột của nó trực chuẩn đôi một.

$$
\mathbf{Q}^T\mathbf{Q} = \mathbf{Q}\mathbf{Q}^T = \mathbf{I}
$$

hay tương đương với

$$
\mathbf{Q}^T = \mathbf{Q}^{-1}
$$

Một điều hay ho về những ma trận trực giao là chúng bảo tồn tích trong

$$
(\mathbf{Q}\mathbf{x})^T(\mathbf{Q}\mathbf{y}) = \mathbf{x}^T\mathbf{Q}^T\mathbf{Q}\mathbf{y} = \mathbf{x}^T\mathbf{I}\mathbf{y} = \mathbf{x}^T\mathbf{y}
$$

Một kết quả trực tiếp từ dữ kiện này là chúng cũng bảo tồn 2-norms:

$$
||\mathbf{Q}\mathbf{x}||_2 = \sqrt{(\mathbf{Q}\mathbf{x})^T(\mathbf{Q}\mathbf{x}} = \sqrt{\mathbf{x}^T\mathbf{x}} = ||x||_2
$$

## Ma trận đối xứng - Symmetric matrices

Một ma trận $\mathbf{A} \in \mathbb{R}^{n \times n}$ được gọi là đối xứng (**Symmetric**) nếu nó bằng với chuyển vị của nó ($\mathbf{A} = \mathbf{A}^T$), có nghĩa là $A_{ij} = A_{ji}$ với mọi $(i, j)$. Định nghĩa này nhìn có vẻ vô hại nhưng thực ra nó mang trong mình một vài hàm ý rất mạnh mẽ.

**Theorem 2**. (Spectral Theorem - Định lý phổ) Nếu $\mathbf{A} \in \mathbb{R}^{n \times n}$ là đối xứng, thì tồn tại một cơ sở trực chuẩn cho không gian $\mathbb{R}^n$ gồm những vector riêng của $\mathbf{A}$

Ứng dụng thực tế của định lý này cụ thể là phân rã của ma trận đối xứng, như là phân rã trị riêng (eigen decomposition) hay phân rã phổ (spectral decomposition). Đặt cơ sở trực chuẩn của những vector riêng (eigen vectors) $\mathbf{q}_1, ..., \mathbf{q}_n$ và những giá trị riêng (eigenvalue) của chúng là $\lambda_1, ..., \lambda_n$. Gọi $\mathbf{Q}$ là ma trận trực giao với $\mathbf{q}_1, ..., \mathbf{q}_n$ là các cột của nó và $\Lambda  = \text{diag}(\lambda_1, ..., \lambda_n)$. Vì với định nghĩa $\mathbf{Aq}_i = \lambda_i\mathbf{q}_i$, mối quan hệ:

$$
\mathbf{AQ} = \mathbf{Q}\Lambda
$$

Nhân bên phải với $\mathbf{Q}^T$, ta có phân rã

$$
\mathbf{A} = \mathbf{Q}\Lambda\mathbf{Q}^T
$$

### Thương số Rayleigh (Rayleigh quotients)

Đặt $\mathbf{A} \in \mathbb{R}^{n \times n}$ là một ma trận đối xứng. Biểu thức $\mathbf{x}^T\mathbf{A}\mathbf{x}$ được gọi là dạng toàn phương (quadratic form)

Nó xuất hiện một liên kết thú vị giữa dạng toàn phương của một ma trận đối xứng và những giá trị riêng của nó. Liên kết này được cho bởi Thương số Rayleigh (Rayleigh quotient)

$$
R_{\mathbf{A}}(\mathbf{x}) = \frac{\mathbf{x}^T\mathbf{A}\mathbf{x}}{\mathbf{x}^T\mathbf{x}}
$$

Thương số Rayleigh có hai tính chất quan trọng mà chúng ta có thể chứng minh dễ dàng (mà thôi không chứng minh đâu :v lười)

i) Bất biến với phép co (Scale invariance): Với bất kỳ vector $\mathbf{x} \ne \mathbf{0}$ và bất kỳ số (scalar) $\alpha \ne 0$, $R_{\mathbf{A}}(\mathbf{x}) = R_{\mathbf{A}}(\mathbf{\alpha x})$

ii) Nếu $\mathbf{x}$ là một vector riêng của $\mathbf{A}$ với giá trị riêng $\lambda$ thì $R_{\mathbf{A}}(\mathbf{x}) = \lambda$

**Mệnh đề 4**. Với bất kỳ $\mathbf{x}$ mà $\|\|x\|\|_2 = 1$

$$
\lambda_{min}(\mathbf{A}) \leq \mathbf{x}^T\mathbf{A}\mathbf{x} \leq \lambda_{max}(\mathbf{A})
$$

với dấu đẳng thức xảy ra nếu và chỉ nếu $\mathbf{x}$ là một vector riêng tương ứng

*Chứng minh*. Chứng minh trường hợp max bởi vì với trường hợp min thì nó khá là tương tự

Bởi vì $\mathbf{A}$ là đối xứng, chúng ta có thể phân rã $\mathbf{A} = \mathbf{Q}\Lambda\mathbf{Q}^T$. Sau đó sử dụng phép đổi biến $\mathbf{y} = \mathbf{Q}^T\mathbf{x}$, ta thấy rằng mối quan hệ giữa $\mathbf{x}$ và $\mathbf{y}$ là mối quan hệ 1-1 và $\|\|\mathbf{y}\|\|_2 = 1$ vì $\mathbf{Q}$ là trực giao. Do đó

$$
 \underset{||\mathbf{x}||_2 = 1}{\text{max }}\mathbf{x}^T\mathbf{A}\mathbf{x} =  \underset{||\mathbf{y}||_2 = 1}{\text{max }}\mathbf{y}^T\Lambda\mathbf{y} =  \underset{y_1^2 + ... + y_n^2}{\text{max }}\sum_{i=1}^n\lambda_iy_i^2
$$

Viết theo cách này, dễ thấy rằng biểu thức $\mathbf{y}$ cực đại nếu và chỉ nếu nó thỏa $\sum_{i \in I}y_i^2 = 1$ trong đó $$I = \{i : \lambda_i = max_{j=1...n}\lambda_j = \lambda_{max}(\mathbf{A})\}$$ và $y_j = 0$ với $j \notin I$. Đó là $I$ chứa những chỉ số của giá trị riêng lớn nhất. Trong trường hợp này, giá trị lớn nhất của biểu thức

$$
\sum_{i=1}^n\lambda_iy_i^2 = \sum_{i \in I}^n\lambda_iy_i^2 = \lambda_{max}(\mathbf{A}) \sum_{i \in I}^ny_i^2 = \lambda_{max}(\mathbf{A})
$$

Sau đó viết $\mathbf{q}_1, ..., \mathbf{q}_n$ là những cột của $\mathbf{Q}$, ta có:

$$
\mathbf{x} = \mathbf{Q}\mathbf{Q}^T\mathbf{x} = \mathbf{Q}\mathbf{y} = \sum_{i = 1}^ny_i\mathbf{q}_i = \sum_{i \in I}y_i\mathbf{q}_i
$$

Nhớ lại $\mathbf{q}_1, ..., \mathbf{q}_n$ là các vector riêng của $\mathbf{A}$ và hình thành một cơ sở trực chuẩn trong $\mathbb{R}^n$. Do đó, tập $$\{\mathbf{q}_i: i \in I\}$$ hình thành một cơ sở trực chuẩn cho không gian trị riêng của $\lambda\_{max}(\mathbf{A})$. Vì $\mathbf{x}$m là một tổ hợp tuyến tính của chúng, nằm trong không gian trị riêng và do đó một vector riêng của $\mathbf{A}$ tương ứng $\lambda\_{max}(\mathbf{A})$

Chúng ta đã chứng minh $$max_{\|\mathbf{x}\|_2 = 1} = \mathbf{x}^T\mathbf{A}\mathbf{x} = \lambda_{max}(\mathbf{A})$$, từ đây là có bất đẳng thức tổng quát $\mathbf{x}^T\mathbf{A}\mathbf{x} \leq \lambda_{max}(\mathbf{A})$ cho tất cả các vector độ đài đơn vị $\mathbf{x}$

**Theorem 3** (Min-max theorem) Với mọi $\mathbf{x} \ne 0$

$$
\lambda_{min}(\mathbf{A}) \leq R_{\mathbf{A}}(\mathbf{x}) \leq \lambda_{max}(\mathbf{A})
$$

## Ma trận xác định dương - Positive (semi-)definite matrices

## Singular Value Decomposition (SVD)

## Định lý cơ sở của Đại số tuyến tính

## Toán tử và ma trận chuẩn

## Xấp xỉ hạng thấp (low-rank)

## Giả nghịch đảo (Pseudoinverses)

## Matrix-Vector - Tổ hợp tuyến tính của ma trận cột

## Matrix-Matrix Products

## Dạng toàn phương - Quadratic forms
