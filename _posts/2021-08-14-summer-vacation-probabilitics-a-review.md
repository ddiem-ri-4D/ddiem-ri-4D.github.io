---
title: "Giải trí mùa hè - Review Probability"
categories:
  - Mathematics
  - Probability
tags:
  - Mathematics
toc: true
comments: true
header:
  teaser: "/assets/images/header/lambda_01.jpg"
---

Ghi và dịch ra Tiếng Việt từ Mathematics for Machine Learning của Garrett Thomas, Department of Electrical Engineering and Computer Sciences, University of California, Berkeley nhằm ôn tập và tổng hợp lại kiến thức Toán cho Học Máy.

Lý thuyết Xác suất (Probability theory) cung cấp những công cụ mạnh mẽ cho việc mô hình hóa và giải quyết với vấn đề không chắc chắc (uncertainty)

## Cơ bản về Xác suất

Giả sử rằng chúng ta có một vài thí nghiệm ngẫu nhiên (ví dụ như tung đồng xu, tung xí ngầu) mà có một tập cố định khả năng có thể xảy ra. Tập này gọi là không gian mẫu (**sample space**) và được ký hiệu là $\Omega$

Chúng ta muốn định nghĩa xác suất cho một số sự kiện (**event**), mà là tập con của $\Omega$. Tập những sự kiện được ký hiệu là $\mathcal{F}$. Phần bù (**complement**) của tập sự kiện $A$ là sự kiện còn lại, $A^c = \Omega \setminus A$

Thì chúng ta có thể định nghĩa một độ đo xác suất (**probability measure**) $\mathbb{P}: \mathcal{F} \rightarrow [0, 1]$ mà phải thỏa mãn

i) $\mathbb{P}(\Omega) = 1$

ii) Bổ sung đếm được (Countable additivity): Với bất kỳ bộ đếm được nào của các tập rời rạc (disjoint sets) $$\{A_i\} \subseteq \mathcal{F}$$

$$
\mathbb{P}\left(\bigcup_iA_i\right) = \sum_i\mathbb{P}(A_i)
$$

Bộ ba $(\Omega, \mathcal{F}, \mathbb{P})$ được gọi là không gian xác suất (**probability space**)

Nếu $\mathbb{P}(A) = 1$, ta nói rằng $A$ xuất hiện hầu hết một cách chắc chắn (almost surely) và ngược lại $A$ luôn không bao giờ (almost never) $\mathbb{P}(A) = 0$

**Mệnh đề 26** Gọi $A$ là một sự kiện. Thì

i) $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$

ii) Nếu $B$ là một sự kiện và $B \subseteq A$ thì $\mathbb{P}(B) \leq \mathbb{P}(A)$

iii) $0 = \mathbb{P}(\emptyset) \leq \mathbb{P}(A) \leq \mathbb{P}(\Omega) = 1$

**Mệnh đề 27** Nếu $A$ và $B$ là các sự kiện, thì $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$

**Mệnh đề 28** Nếu $$\{A_i\} \subseteq \mathcal{F}$$ là một tập sự kiện đếm được, rời rạc hoặc không, thì

$$
\mathbb{P}\left(\bigcup_iA_i\right) \leq \sum_i\mathbb{P}(A_i)
$$

Bất đẳng thức này đôi khi được biết đến như là bất đẳng thức Boole (**Boole’s inequality**) hay union bound


### Xác suất có điều kiện (Conditional Probability)

Xác suất có điều kiện (**conditional probability**) của một sự kiện $A$ nào đó biết rằng sự kiện $B$ đã xảy ra, được viết là $\mathbb{P}(A \| B)$, được định nghĩa

$$
\mathbb{P}(A \| B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}
$$

## Chain Rule

$$
\mathbb{P}(A \cap B) = \mathbb{P}(A \| B)\mathbb{P}(B) = \mathbb{P}(B \| A)\mathbb{P}(A)
$$

## Bayes's Rule

Định lý Bayes

$$
\mathbb{P}(A \| B) = \frac{\mathbb{P}(B \| A)}{\mathbb{P}(B)}
$$

Đôi khi sẽ có lợi nếu bỏ qua hằng số chuẩn hóa và viết lại là

$$
\mathbb{P}(A \| B) \propto \mathbb{P}(A)\mathbb{P}(B \| A)
$$

Với biểu thức này, $\mathbb{P}(A)$ thường được gọi là xác suất tiên nghiệm (**prior**), $\mathbb{P}(A \| B)$ là xác suất hậu nghiệm (**posterior**), và $\mathbb{P}(B \| A)$ gọi là triển vọng (**likelihood**)

Trong ngữ cảnh của Machine Learning, chúng ta có thể sử dụng luật Bayes để cập nhật "niềm tin - beliefs" của chúng ta (ví dụ như giá trị của những tham số của mô hình) được cho bởi dữ liệu mà chúng ta quan sát được.

## Biến ngẫu nhiên (Random Variables)

Một biến ngẫu nhiên là một số số lượng không chắc chắn với một phân phối xác suất có thể giả định được liên hệ trên những giá trị.

Một cách toán học, một biến ngẫu nhiên trên một không gian xác suất $(\Omega, \mathcal{F}, \mathbb{P})$ là một hàm $X: \Omega \rightarrow \mathbb{R}$

Ta đặt khoảng của $X$ bởi $$X(\Omega) = \{X(\omega) : \omega \in \Omega\}$$

### Hàm phân phối tích lũy (The cumulative distribution function)

$$
F(x) = \mathbb{P}(X \leq x)
$$

$$
\mathbb{P}(a \leq X \leq b) = F(b) - F(a)
$$

### Biến ngẫu nhiên rời rạc (Discrete random variables)

$$
\sum_{x \in X(\Omega)}p(x) = 1
$$

$$
\mathbb{P}(X = x) = p(x)
$$

### Biến ngẫu nhiên liên tục (Continuous random variables)

$$
F(x) = \int_{-\infty}^xp(z)dz
$$

$$
\int_{-\infty}^{\infty}p(x)dx = 1
$$

$$
\mathbb{P}(x - \epsilon \leq X \leq x + \epsilon) = \int_{x - \epsilon}^{x + \epsilon}p(z)dz \approx 2\epsilon p(x)
$$

$$
\mathbb{P}(a \leq X \leq b) = \int_a^bp(x)dx
$$

$$
p(x) = F'(x)
$$

## Phân phối kết hợp (Joint Distribution)

### Biến ngẫu nhiên độc lập

$$
p(X, Y) = p(X)p(Y)
$$

$$
p(X_{i_1}, ..., X_{i_k}) = \prod_{j=1}^{k}p(X_{i_j})
$$

$$
p(X_{1}, ..., X_{n}) = \prod_{j=1}^{n}p(X_{i})
$$

### Phân phối lề (Marginal distributions)

$$
p(X) = \sum_yp(X, y)
$$

## Kỳ vọng (Expectations)

$$
\mathbb{E}[X] = \sum_{x \in X(\Omega)}xp(x)
$$

$$
\mathbb{E}[X] = \int_{-\infty}^{\infty}xp(x)dx
$$

### Tính chất của giá trị kỳ vọng

$$
\mathbb{E}\left[\sum_{i=1}^n\alpha_iX_i + \beta\right] = \sum_{i=1}^n\alpha_i\mathbb{E}[X_i]+\beta
$$

$$
\mathbb{E}\left[\prod_{i=1}^nX_i\right] = \prod_{i=1}^n\mathbb{E}[X_i]
$$

## Phương sai (Variance)

$$
Var(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]
$$

$$
Var(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2
$$

### Tính chất của phương sai

$$
Var(\alpha X + \beta) = \alpha^2Var(X)
$$

$$
Var(X_1 + ... + X_n) = Var(X_1) + ... + Var(X_n)
$$

### Độ lệch chuẩn (Standard deviation)

$$
std = \sqrt{Var(X)}
$$

## Hiệp phương sai (Covariance)

$$
Cov(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])]
$$

$$
Cov(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]
$$

$$
Cov(\alpha X + \beta Y, Z) = \alpha Cov(X, Z) + \beta Cov(Y, Z)
$$

$$
Cov(X, \alpha Y + \beta Z) = \alpha Cov(X, Y) + \beta Cov(X, Z)
$$

### Tương quan (Correlation)

$$
\rho (X, y) = \frac{Cov(X, Y)}{\sqrt{Var(X)Var(Y)}}
$$

## Vector ngẫu nhiên (Random Vector)

Cho đến hiện tại, chúng ta đang nói về những phân phối đơn biến (**univariate distributions**), đó là những phân bối một biến. Nhưng chúng ta cũng có thể nói về phân phối đa biến **multivariate distributions** được cho bởi những vector ngẫu nhiên **random vector**

$$
\mathbf{X} = \begin{bmatrix}X_1\\...\\X_n\end{bmatrix}
$$

$$
\mathbb{E}[\mathbf{X}] = \begin{bmatrix}\mathbb{E}[X_1]\\...\\\mathbb{E}[X_n]\end{bmatrix}
$$

$$
\mathbf{\Sigma} = \mathbb{E}[(\mathbf{X} - \mathbb{E}[\mathbf{X}])(\mathbf{X} - \mathbb{E}[\mathbf{X}])^T] = \begin{bmatrix}
Var(X_1) & Cov(X_1, X_2) & ... & Cov(X_1, X_n)\\
Cov(X_2, X_1) & Var(X_2) & ... & Cov(X_2, x_n)\\
... & ... & ... & ... \\
Cov(X_n, X_1) & Cov(X_n, X_2) & ... & Var(X_n)
\end{bmatrix}
$$

## Ước lượng tham số (Estimation of Parameters)

### Ước lượng triển vọng cực đại (Maximum likelihood estimation)

Một cách phổ thông để khớp tham số (fit parameters) là ước lượng triển vọng cực đại (maximum likelihood estimation - MLE). Nguyên lý cơ bản của MLE là chọn những giá trị mà "giải thích" dữ liệu tốt tất bằng cách cực đại xác suất/ mật độ của dữ liệu mà ta thấy như một hàm của những tham số. Giả định ta có các biến ngẫu nhiên $X_1, ..., X_n$ và những quan sát tương ứng $x_1, ..., x_n$. Thì

$$
\hat{\theta}_{MLE} = \underset{\theta}{\text{arg max }}\mathcal{L}(\theta)
$$

trong đó $\mathcal{L}$ là **likelihood function**

$$
\mathcal{L}(\theta) = p(x_1, ..., x_n; \theta)
$$

Thông thường, ta giả sử rằng $X_1, ..., X_n$ là những biến độc lập và có phân phối giống hệt nhau (independent and identically distributed random variables)

$$
p(x_1, ..., x_n; \theta) = \prod_{i=1}^np(x_i;\theta)
$$

$$
log\mathcal{L}(\theta)  = \sum_{i=1}^nlog(p(x_i;\theta))
$$

### Ước lượng một cực đại hậu nghiệm (Maximum a posteriori estimation)

Một cách Bayesian để khớp tham số là ước lượng một cực đại hậu nghiệm (maximum a posteriori estimation - MAP). Trong kỹ thuật này, ta giả định rằng những tham số là một biến ngẫu nhiên và ta xác định một tiền phân phối $p(\theta)$. Sau đó, ta có thể dùng Bayes's rule để tính toán phân phối hậu nghiệm của những tham số của dữ liệu quan sát được

$$
p(\theta \| x_1, ..., x_n) \propto p(\theta)p(x_1, ..., x_n | \theta)
$$

$$
\hat{\theta}_{MAP} = \underset{\theta}{\text{arg max }}p(\theta)p(x_1, ..., x_n | \theta)
$$

$$
\hat{\theta}_{MAP}  = \underset{\theta}{\text{arg max }}\left(log(p(\theta)) + \sum_{i=1}^nlog(p(x_i | \theta))\right)
$$

## Phân phối Gauss (Gaussian Distribution)

$$
p(\mathbf{x}; \mathbf{\mu}, \mathbf{\Sigma}) = \frac{1}{\sqrt{(2\pi)^d\text{det}(\Sigma)}}\text{exp}\left(-\frac{1}{2}(\mathbf{x} - \mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\mathbf{x} - \mathbf{\mu})\right)
$$

$$
p(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}\text{exp}\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

## Tài liệu gốc

\[1\] [Garrett Thomas. Department of Electrical Engineering and Computer Sciences. University of California, Berkeley. "Mathematics for Machine Learning", January 11, 2018](https://gwthomas.github.io/docs/math4ml.pdf)
