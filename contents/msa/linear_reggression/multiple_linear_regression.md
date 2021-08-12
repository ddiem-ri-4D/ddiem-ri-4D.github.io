---
layout: single
permalink: /content/msa/linear_regression/multiple_linear_regression
title: "[MSA] Multiple Linear Regression"
author_profile: true
toc: true
comments: True
---
Phần trình bày về mô hình hồi quy tuyến tính bội - multiple linear regression model

## 1) Động lực nghiên cứu khoa học

Trong lĩnh vực nghiên cứu Máy học (Machine Learning), người ta mong muốn đưa ra các giá trị dự đoán với những thông tin mới được đưa vào mô hình nào đó, thông qua những dữ kiện đã biết trước đó sao cho các giá trị dự đoán càng gần với giá trị thực, và đó là bài toán Regression hay được gọi là hồi quy.

Với trường hợp đơn biết, ta có thể mô phỏng mô hình bằng một đường thẳng có dạng $y = ax + b$, rất quen thuộc khi chúng ta học cấp 3. Với trường hợp hai biến, ta có thể mô phỏng mô hình bằng một mặt phẳng có dạng $y = ax + by + c$, và khi số lượng biến của chúng ta lớn hơn hai, mô hình có thể được mô phỏng bằng một siêu phẳng (hyperplane)

## 2) Phát biểu bài toán

Đầu vào bài toán: ta nhận các biến $(X_1, X_2, ..., X_p)$ và các giá trị thực tương ứng với quan sát thứ $i$ đó $y_i \in \mathbb{R}$

Đầu ra của bài toán: $b_0 \in \mathbb{R}$ hệ số chặn hồi quy (regression intercept) và $b_j \in \mathbb{R}$ là các hệ số hồi quy (regression slope) của giá trị dự đoán thứ $j$

Mô hình hồi quy tuyến tính bội như sau:

$$y_i = b_0 + \sum_{j=1}^pb_jx_{ij} + e_i, \forall i \in \{1,...,n\}$$

Trong đó:
- $y_i \in \mathbb{R}$ là giá trị thực tương ứng với quan sát thứ $i$
- $b_0 \in R$ là hệ số chặn hồi quy (regression intercept)
- $b_j \in \mathbb{R}$ là các hệ số hồi quy (regression slope) của giá trị dự đoán thứ $j$
- $x_{ij} \in \mathbb{R}$ là giá trị dự đoán thứ $j$ cho quan sát thứ $i$
- $e_i \overset{\underset{\mathrm{iid}}{}}{\sim} \mathcal{N}(0, \sigma^2)$ một Gaussian Error

Hay viết gọn hơn bằng dạng ma trận như sau

$$\mathbf{y = Xb + e}$$

Trong đó:
- $\mathbf{y} = (y_1, y_2, ..., y_n)' \in \mathbb{R}^n$ có kích thước $n \times 1$ là vector các giá trị tương ứng với biến quan sát
- $\mathbf{X = [1_n, x_1, x_2, ..., x_p]} \in \mathbb{R}^{n\times (p+1)}$ có kích thước  $n \times (p + 1)$ là ma trận biến quan sát
- $\mathbf{b} = (b_0, b_1, b_2, ..., b_p)' \in \mathbb{R}^{p+1}$ có kích thước $(p + 1) \times n$ là vector các hệ số hồi quy (coefficient vector)
- $\mathbf{e} = (e_1, e_2, ..., e_n)' \in \mathbb{R}^n$ là vector độ lỗi (error vector)

Mô hình là một mô hình hồi quy và tuyến tính (linear) với những tham số $b_0, b_1, ..., b_p$ vì chúng ta mô hình hóa một biến (Y) tương ứng như một hàm dự đoán các giá trị $(X_1, X_2, ..., X_p)$. Hơn nữa, mô hình là bội (multiple) vì chúng ta có nhiều hơn một bộ dự đoán, nếu chỉ có một bộ dự đoán, mô hình trở thành một mô hình Simple Linear Regression

Các giả định cơ sở của mô hình hồi quy tuyến tính bội
- Mối quan hệ giữa $X_j$ và $Y$ là tuyến tính
- $x_{ij}$ và $y_i$ là những biến ngẫu nhiên đã biết
- $e_i \overset{\underset{\mathrm{iid}}{}}{\sim} \mathcal{N}(0, \sigma^2)$ là biến ngẫu nhiên chưa biết
- $b_0, b_1, ..., b_p$ là các hằng số chưa biết
- $(y_i \|\ x_{i1}, x_{i2}, ..., x_{ip}) \overset{\underset{\mathrm{iid}}{}}{\sim} \mathcal{N}(b_0 + \sum_{j=1}^pb_jx_{ij} , \sigma^2)$

## 3) Phương pháp

### 3.1 Ước lượng tham số mô hình bằng phương pháp bình phương tối tiểu (Ordinary Least Squares)

Bài toán bình phương tối tiểu (OLS)

$$\underset{\mathbf{b} \in \mathbb{R}^{p+1}}{min} ||\mathbf{y -Xb}||^2 = \underset{\mathbf{b} \in \mathbb{R}^{p+1}}{min} \sum_{i=1}^{n}\left(y_i - b_0 - \sum_{j=1}^pb_jx_{ij}\right)^2$$

Với ma trận $\mathbf{X} \in \mathbb{R}^{p+1}$, $p+1 \leq n$, $rank(\mathbf{X}) = n$. Xét hàm số:

$$f: \mathbb{R}^n \rightarrow \mathbb{R}$$

$$f(x) =  ||\mathbf{y -Xb}||^2$$

Ta có:

$$
\begin{gather*}
f(x) = \left< \mathbf{y -Xb}, \mathbf{y -Xb}\right>\\
= (\mathbf{y -Xb})^\text{T}(\mathbf{y -Xb})\\
= (\mathbf{y}^{\text{T}} - \mathbf{b}^{\text{T}}\mathbf{X}^{\text{T}})(\mathbf{y - Xb})\\
= \mathbf{b}^{\text{T}}\mathbf{X}^{\text{T}}\mathbf{Xb} - \mathbf{y}^{\text{T}}\mathbf{Xb} - \mathbf{b}^{\text{T}}\mathbf{X}^{\text{T}}\mathbf{y} + \mathbf{y}^{\text{T}}\mathbf{y}\\
= \mathbf{b}^{\text{T}}(\mathbf{X}^{\text{T}}\mathbf{X})\mathbf{b} - (2 \mathbf{y}^{\text{T}}\mathbf{X})\mathbf{b} + \mathbf{y}^{\text{T}}\mathbf{y}
\end{gather*}
$$

Vì $\mathbf{y}^{\text{T}}\mathbf{X}\mathbf{b} = \mathbf{b}^{\text{T}}\mathbf{A}^{\text{T}}\mathbf{y}$ nên ta có:

$$
\begin{gather*}
\nabla f(x) = 2(\mathbf{X}^{\text{T}}\mathbf{X})\mathbf{b} - 2\mathbf{X}^{\text{T}}\mathbf{y}\\
\nabla^2 f(x) = 2(\mathbf{X}^{\text{T}}\mathbf{X})
\end{gather*}
$$

Mà do $\mathbf{b}  \in \mathbb{R}^{p+1}$

$$
\begin{gather*}
\mathbf{b}\nabla^2 f(x) \mathbf{b} = 2[\mathbf{b}^{\text{T}}(\mathbf{X}^{\text{T}}\mathbf{X})\mathbf{b}]\\
= 2[\mathbf{b}^{\text{T}}(\mathbf{X}\mathbf{b})]\\
= 2||\mathbf{X}\mathbf{b}||^2 \geq 0
\end{gather*}
$$

Vì thế mà $\nabla^2 f(x)$ là ma trận xác định dương mặc khác $rank(\mathbf{X}^{\text{T}}\mathbf{X}) = n$
nên $\mathbf{X}^{\text{T}}\mathbf{X}$ khả nghịch

Ta thu được nghiệm của bài toán $\hat{\mathbf{b}} = (\mathbf{X}^{\text{T}}\mathbf{X})^{-1}\mathbf{X}^{\text{T}}\mathbf{y}$

### 3.2 Ước lượng tham số mô hình bằng phương pháp triển vọng cực đại (maximum likelihood)

Nhớ lại rằng $(y\|\\mathbf{X}) \sim \mathcal{N}(\mathbf{Xb}, \sigma^2\mathbf{I}_n)$ trong đó $\mathbf{y}$ có hàm mật độ xác suất (probability density function):

$$
\begin{gather*}
f(\mathbf{y} \|\ \mathbf{X}, \mathbf{b}, \sigma^2) = (2\pi)^{-n/2}(\sigma^2)^{-n/2}exp\{-\frac{1}{2\sigma^2}(\mathbf{y} - \mathbf{Xb})^{\text{T}}(\mathbf{y} - \mathbf{Xb})\}
\end{gather*}
$$

log-likelihood của $\mathbf{b}$ bởi $(\mathbf{y}, \mathbf{X}, \sigma^2)$

$$
\begin{gather*}
ln\{L(\mathbf{b} | \mathbf{y}, \mathbf{X}, \sigma^2)\} = \frac{1}{2\sigma^2}(\mathbf{y} - \mathbf{Xb})^{\text{T}}(\mathbf{y} - \mathbf{Xb}) + c
\end{gather*}
$$

Ước lượng triển vọng cực đại (maximum likelihood estimate - MLE) của $\mathbf{b}$

$$
\begin{gather*}
\underset{\mathbf{b} \in \mathbb{R}^{p+1}}{max} \frac{1}{2\sigma^2}(\mathbf{y} - \mathbf{Xb})^{\text{T}}(\mathbf{y} - \mathbf{Xb})\\
= \underset{\mathbf{b} \in \mathbb{R}^{p+1}}{max} -(\mathbf{y} - \mathbf{Xb})^{\text{T}}(\mathbf{y} - \mathbf{Xb})\\
= \underset{\mathbf{b} \in \mathbb{R}^{p+1}}{min} (\mathbf{y} - \mathbf{Xb})^{\text{T}}(\mathbf{y} - \mathbf{Xb})\\
\end{gather*}
$$

Để cực đại likelihood function, chúng ta cần phải cực tiểu $||\mathbf{y-Xb}||^2$. Ta có:
$$
\begin{gather*}
||\mathbf{y-Xb}||^2 = \left<\left(y - \sum_{i=1}^pb_ix_{i}\right), \left(y - \sum_{i=1}^pb_ix_{i}\right)\right>\\
= \left<y, y\right> - 2\sum_{i=1}^pb_i\left<y,x_i\right> + \sum_{i=1, j=1}^pb_ib_j\left<x_i, x_j\right>
\end{gather*}
$$

Đạo hàm theo $b_i$ và cho đạo hàm bằng 0
$$
\begin{gather*}
-2\left<y, x_i\right> + 2\sum_{j=1}^pb_j\left<x_i, x_j\right> = 0
\end{gather*}
$$

Ta được
$$
\begin{gather*}
\left<y, x_i\right> = \sum_{j=1}^pb_j\left<x_i, x_j\right>
\end{gather*}
$$

Viết lại ở dạng ma trận

$$
\begin{gather*}
\mathbf{X}^{\text{T}}\mathbf{y} = \mathbf{X}^{\text{T}}\mathbf{X}\mathbf{b}
\end{gather*}
$$

Trong đó $\mathbf{X}^{\text{T}}\mathbf{X}$ có kích thước $n \times n$, giả định X khả nghịch, hạng bằng p

$$\hat{b} = (\mathbf{X}^{\text{T}}\mathbf{X})^{-1} \mathbf{X}^{\text{T}}\mathbf{y}$$

### 3.3 Đánh giá mô hình

Gọi $\mathbf{\hat{e} = y -\hat{y}}$ phần dư (residual) giữa giá trị thực và giá trị dự đoán của mô hình và đặt những giá trị khớp (fitted values) cho bởi công thức $\mathbf{\hat{y} = X\hat{b}}$

Ta có thể viết những giá trị được khớp như sau:

$$
\begin{gather*}
\mathbf{\hat{y} = X\hat{b}}\\
= \mathbf{X(X^{\text{T}}X)^{-1}X^{\text{T}}y}
= \mathbf{Hy}
\end{gather*}
$$

Trong đó $\mathbf{H = X(X^{\text{T}}X)^{-1}X^{\text{T}}}$ được gọi là ma trận hat (hat matrix)

Note: Một số tính chất của hat matrix

1) Hat matrix là ma trận đối xứng (symmetric matrix)

Dễ dàng biến đổi được

$$
\begin{gather*}
\mathbf{H}^{\text{T}} = (\mathbf{X(X^{\text{T}}X)^{-1}X^{\text{T}}})^{\text{T}}\\
= \mathbf{(X^{\text{T}})^{\text{T}}((X^{\text{T}})^{\text{T}}(X)^{\text{T}})^{-1}(X')^{\text{T}}}\\
= \mathbf{X(X^{\text{T}}X)^{-1}X^{\text{T}}}\\
= H
\end{gather*}
$$

2) Hat matrix là ma trận lũy đẳng (idempotent matrix)

Dễ dàng biến đổi được

$$
\begin{gather*}
\mathbf{H}\mathbf{H} = (\mathbf{X(X^{\text{T}}X)^{-1}X^{\text{T}}})(\mathbf{X(X^{\text{T}}X)^{-1}X^{\text{T}}}) = \mathbf{H}
\end{gather*}
$$

Trong mô hình Multiple Linear Regression, ta có một số tổng bình phương như sau:

1) Tổng bình phương tổng thể (Sum-of-Squares Total)

$$
SST = \sum_{i=1}^n(y_i - \bar{y})^2 = \mathbf{y}^{\text{T}}\left[\mathbf{I}_n - \frac{1}{n}\mathbf{J}\right]\mathbf{y}
$$

bậc tự do tương ứng $df_T = n - 1$

2) Tổng bình phương hồi quy (Sum-of-Squares Regression)

$$
SSR = \sum_{i=1}^n(\hat{y}_i - \bar{y})^2 = \mathbf{y}^{\text{T}}\left[\mathbf{H} - \frac{1}{n}\mathbf{J}\right]\mathbf{y}
$$

bậc tự do tương ứng $df_R = p$

3) Tỗng bình phương độ lỗi (Sum-of-Squares Error)

$$
SSE = \sum_{i=1}^n(y_i - \hat{y})^2 = \mathbf{y}^{\text{T}}\left[\mathbf{I}_n - \mathbf{H}\right]\mathbf{y}
$$

bậc tự do tương ứng $df_E = n - p - 1$

Với $\mathbf{J}$ là một ma trận toàn một có kích thước $n \times n$

Mối liên hệ giữa SST với SSR và SSE như sau

$$
\begin{gather*}
SST =  \sum_{i=1}^n(y_i - \bar{y})^2\\
=  \sum_{i=1}^n(y_i - \hat{y}_i + \hat{y}_i \bar{y})^2\\
= \sum_{i=1}^n(\hat{y}_i - \bar{y})^2 +  \sum_{i=1}^n(y_i - \hat{y})^2 + 2\sum_{i=1}^n(\hat{y}_i - \bar{y})(y_i - \hat{y})\\
= SSR + SSE + 2\sum_{i=1}^n(\hat{y}_i - \bar{y})\hat{e}_i\\
\approx SSR + SSE
\end{gather*}
$$

Trong thống kê sử dụng một đại lượng đánh giá các mô hình hồi quy là R-squared (Coefficient of Multiple Determination) được định nghĩa như sau:

$$
R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}
$$

cho biết số lượng biến thiên trong $y_i$ mà được giải thích bằng quan hệ tuyến tính với $x_{i1}, x_{i2}, ..., x_{ip}$

Khi xem xét R-Squared:
- R-Squared có giá trị nằm trong khoảng $0 \leq R^2 \leq 1$
- Những giá trị R-Squared lớn không có nghĩa là mô hình sẽ tốt! Khi R-Squared = 1, ta sẽ đạt được mô hình lý tưởng (Nhưng thực tế, điều này cực kỳ khó để xảy ra!)
- Khi R-Squared = 0, mô hình không phù hợp!

Khi trong mô hình MLR có nhiều bộ dự đoán, nó có thể ảnh hưởng đến R-Squared:
- Ảnh hưởng của nhiễu trong dữ liệu
- Hiện tượng "over-fitting"

Ta cần sử dụng R-Square hiệu chỉnh (Adjusted R-Square)

$$
R_a^2 = 1 - \frac{SSE/df_E}{SST/df_T} = 1 - \frac{\hat{\sigma}^2}{s_Y^2}
$$

Trong đó:

$s_Y^2 = \frac{\sum_{i=1}^n(y_i - \bar{y})^2}{n-1}$ là ước lượng phương sai mẫu của $Y$

**Ước lượng độ lỗi phương sai - Estimated Error Variance (Mean Squared Error)**

Ước lượng độ lỗi phương sai:

$$
\begin{gather*}
\hat{\sigma}^2 = \frac{SSE}{n - p - 1}\\
= \frac{\sum_{i=1}^n(y_i - \hat{y}_i)^2}{n-p-1}\\
= \frac{||(\mathbf{I}_n - \mathbf{H})\mathbf{y}||^2}{n-p-1}
\end{gather*}
$$

là một ước lượng độ lỗi phương sai $\sigma^2$ không thiên vị (unbiased estimate of error variance) và ước lượng $\hat{\sigma}^2$ được gọi là mean squared error (MSE) 

**Ước lượng triển vọng cực đại độ lỗi phương sai - Maximum Likelihood Estimate of Error Variance**

Ước lượng triển vọng cực đại của $\sigma^2$ là:

$$
\widetilde{\sigma}^2 = \frac{\sum_{i=1}^n(y_i - \hat{y}_i)^2}{n}
$$

Ta có kỳ vọng của $\widetilde{\sigma}^2$ liên hệ với $\sigma^2$:

$$
E(\widetilde{\sigma}^2) = \frac{n-p-1}{n}\sigma^2
$$

Hệ quả là, thiên vị (bias) của ước lượng $\widetilde{\sigma}^2$ được tính:

$$
\frac{n-p-1}{n}\sigma^2 - \sigma^2 = - \frac{p+1}{n}\sigma^2
$$

Khi $n \rightarrow \infty$ thì $- \frac{p+1}{n}\sigma^2 \rightarrow 0$

Với MSE và MLE của phương sai $\sigma^2$ lần lượt như sau

$$
\begin{gather*}
\hat{\sigma}^2  = \frac{||(\mathbf{I}_n - \mathbf{H})\mathbf{y}||^2}{n-p-1}\\
\widetilde{\sigma}^2 = \frac{||(\mathbf{I}_n - \mathbf{H})\mathbf{y}||^2}{n}
\end{gather*}
$$

Suy ra $\widetilde{\sigma}^2  < \hat{\sigma}^2$

### 3.4 Suy luận (inference) và dự đoán (prediction)

#### ANOVA Table và Regression F Test

#### Suy luận $\hat{b}_j$ với phương sai $\sigma^2$ đã biết

Nếu phương sai $\sigma^2$ đã biết, sử dụng khoảng tin cậy (Confidence Interval) $100(1-\alpha)%$

$$
\hat{b}_0 \pm t_{n-p-1}^{\alpha/2}\sigma_{b_0}\\
\hat{b}_j \pm Z_{\alpha/2}\sigma_{b_j}
$$

Trong đó:
- $Z_{\alpha/2}$ là normal quantile mà $P(X > Z_{\alpha/2}) = \alpha/2$
- $\sigma_{b_0}, \sigma_{b_j}$ là căn bậc hai của ma trận đường chéo $V(\hat{b}) = \sigma^2(\mathbf{X^{\text{T}X}})^{-1}$

Để kiểm định $H_0$: $b_i = b_j^{\*}$ và $H_1$ : $b_j \ne  b_j^{\*}$ sử dụng

$$Z = \frac{b_i -  b_j^{*}}{\sigma_{b_j}}$$

theo một phân phối chuẩn (standard normal distribution) dưới $H_0$

#### Suy luận $\hat{b}_j$ với phương sai $\sigma^2$ chưa biết

Nếu phương sai $\sigma^2$ chưa biết, sử dụng khoảng tin cậy (Confidence Interval) $100(1-\alpha)%$

$$
\hat{b}_0 \pm t_{n-p-1}^{\alpha/2}\hat{\sigma}_{b_0}\\
\hat{b}_j \pm t_{n-p-1}^{\alpha/2}\hat{\sigma}_{b_j}
$$

Trong đó:
- $t_{n-p-1}^{\alpha/2}$ là $t_{n-p-1}$ quantile với $P(X > t_{n-p-1}^{\alpha/2}) = \alpha/2$
- $\hat{\sigma_{b_0}}$, $\hat{\sigma_{b_j}}$ là căn bậc hai của đường chéo của $\hat{V}(\mathbf{\hat{b}}) = \hat{\sigma}^2(\mathbf{X^{\text{T}}X})^{-1}$

Để kiểm định $H_0: b_i = b_j^{\*}$ và $H_1: b_j \ne  b_j^{\*}$ sử dụng:

$$T = \frac{b_i -  b_j^{*}}{\hat{\sigma}_{b_j}}$$

theo một phân phối $t_{n-p-1}$ dưới $H_0$

#### Suy luận đa $\hat{b}_j$ (Multiple $\hat{b}_j$)

Giả định rằng $q < p$ và chúng ta muốn kiểm tra nếu một mô hình tinh giảm (reduced model) là đủ tốt

$$
\begin{gather*}
H_0 : b_{q+1} = b_{q+2} = ... = b_p = b^{*}\\
H_1 : \text{ có ít nhất một } b_k \ne b^{*}
\end{gather*}
$$

So sánh SSE với full và reduced (constrained) model

a) Full model:

$$
y_i = b_0 + \sum_{j=1}^pb_jx_{ij} + e_i
$$

b) Reduce (Constrained) model

$$
y_i =  b_0 + \sum_{j=1}^qb_jx_{ij} + b^{*}\sum_{k=q+1}^px_{ik} + e_i
$$

Kiểm định thống kê:

$$
\begin{gather*}
F^{*} = \frac{SSE_R - SSE_F}{df_R - df_F} \times \frac{df_F}{SSE_F}\\
=  \frac{SSE_R - SSE_F}{(n − q − 1) − (n − p − 1)} \times \frac{(n − p − 1)}{SSE_F} \sim F(p-q, n-p-1)\\
\end{gather*}
$$

Trong đó:

$SSE_R$ là tổng bình phương sai số cho mô hình được tối giản (reduce model)

$SSE_R$ là tổng bình phương sai số cho mô hình đầy đủ (full model)

$df_R$ là bậc tự do độ lỗi cho mô hình được tối giản (reduce model)

$df_F$ là bậc tự do độ lỗi cho mô hình đầy đủ (full model)


#### Suy luận tổ hợp tuyến tính (Linear Combinations) của $\hat{b}_j$

Giả định rằng cho biết $\mathbf{c} = (c_0, c_1, ..., c_p)'$ và chúng ta muốn kiểm tra

$$
H_0: \mathbf{c'b} = b^{*}\\
H_1: \mathbf{c'b} \ne b^{*}\\
$$

Kiểm định thống kê:

$$
t^{*} = \frac{\mathbf{c'\hat{b}} - b^{*}}{\hat{\sigma}\sqrt{\mathbf{c'(X'X)^{-1}c}}} \sim t_{n-p-1}
$$

#### Khoảng tin cậy (Confidence Interval) cho phương sai $\sigma^2$

Ta chứng minh được

$$
\frac{(n-p-1)\hat{\sigma}^2}{\sigma^2} = \frac{SSE}{\sigma^2} = \frac{\sum_{i=1}^n\hat{e}_i}{\sigma^2} \sim \mathcal{X}_{n-p-1}^2
$$

Do đó

$$
\mathcal{X}_{(n-p-1; 1 - \alpha/2)}^2 < \frac{(n-p-1)\hat{\sigma}^2}{\sigma^2} < \mathcal{X}_{(n-p-1; \alpha/2)}^2
$$

Trong đó

$$
P(Q > \mathcal{X}_{(n-p-1; \alpha/2)}^2 = \alpha2/2
$$

nên khoảng tin cậy $100(1-\alpha)\%$ được cho bởi

$$
\frac{(n-p-1)\hat{\sigma}^2}{\mathcal{X}_{(n-p-1; \alpha/2)}^2} < \sigma^2 < \frac{(n-p-1)\hat{\sigma}^2}{\mathcal{X}_{(n-p-1; 1 - \alpha/2)}^2}
$$

#### Khoảng ước lượng (Interval Estimation) 

Ý tưởng: Ước lượng giá trị với một bộ dự đoán điểm cho trước

Cho $\mathbf{x_h} = (1, x_{h1}, x_{h2}, ..., x_{hp})$, hàm khớp giá trị $\hat{y}_h = \mathbf{x_h\hat{b}}$

Phương sai của $\hat{y}_h$:

$$
\sigma_{y_h}^2 = V(\mathbf{x_h\hat{b}}) = \mathbf{x_h}V(\hat{b})\mathbf{x_h}' = \sigma^2\mathbf{x_h}(\mathbf{(X'X)^{-1}})\mathbf{x_h}'
$$

Nếu phương sai $\sigma^2$ chưa biết:

$$
\hat{\sigma}_{y_h}^2 = \hat{sigma}^2\mathbf{x_h}(\mathbf{(X'X)^{-1}})\mathbf{x_h}'
$$

Ta kiểm định:
$$
\begin{gather*}
H_0: E(y_h) = y_h^{*}\\
H_0: E(y_h) \ne y_h^{*}\\
\end{gather*}
$$

Kiểm định thống kê

$$
T = \frac{\hat{y}_h - y_h^{*}}{\hat{\sigma}_{\bar{y}_h}}
$$ 

theo phần phối $t_{n-p-1}$

Khoảng tin cậy $100(1-\alpha)%$ cho $E(y_h)$

$$
\hat{y}_h \pm t_{n-p-1}^{\alpha/2}\hat{\sigma}_{\bar{y}_h}
$$

#### Dự đoán quan sát mới (Predicting New Observations)

Ý tưởng: Ước lượng giá trị với một bộ dự đoán điểm cho trước. Ta tập trung vào giá trị $\hat{y}_h$ thay vì kỳ vọng $E(\hat{y}_h)$

Cho $\mathbf{x_h} = (1, x_{h1}, x_{h2}, ..., x_{hp})$, hàm khớp giá trị $\hat{y}_h = \mathbf{x_h\hat{b}}$

Hai vấn đề không chắc chắn trong việc dự đoán một quan sát mới
- vị trị của phân phối của $Y$ cho $X_1, X_2, ..., X_p$
- sự thay đổi trong phân phối của $Y$

Ta sử dụng hai phương sai nguồn độc lập với nhau

$$
\sigma_{y_h}^2 = \sigma_{\bar{y}_h}^2  + \sigma^2
$$

Trong trường hợp phương sai $\sigma^2$ chưa biết, sử dụng

$$
\hat{\sigma}_{y_h}^2 = \hat{\sigma}_{\bar{y}_h}^2  + \hat{\sigma}^2
$$

Bài toán kiểm định

$$
\begin{gather*}
H_0: y_h = y^{*}_h\\
H_1: y_h \ne y^{*}_h\\
\end{gather*}
$$

Kiểm định thống kê:

$$
T = \frac{\hat{y}_h - y^{*}_h}{\hat{\sigma}_{y_h}}
$$

theo phân phối $t_{n-p-1}$

Khoảng dự đoán (Prediction Interval) $100(1-\alpha)%$ cho $y_h$

$$
\hat{y}_h \pm t_{n-p-1}^{\alpha/2}\hat{\sigma}_{y_h}
$$

**Tài liệu tham khảo**

[0] Multivariate Linear Regression, Nathaniel E. Helwig, Assistant Professor of Psychology and Statistics, University of Minnesota (Twin Cities)

[1] Wikipedia, "Ordinary Least Squares," [Online]. Available:
https://en.wikipedia.org/wiki/Ordinary_least_squares.

[2] K. Academy, "r squared or coefficient of determination," [Online]. Available:
https://www.khanacademy.org/math/statistics-probability/describing-relationships-
quantitative-data/more-on-regression/v/r-squared-or-coefficient-of-determination.

[3] Wikipedia, "Variance," [Online]. Available: https://en.wikipedia.org/wiki/Variance.

[4] Wikipedia, "Maximum Likelihood Estimation," [Online]. Available:
https://en.wikipedia.org/wiki/Maximum_likelihood_estimation.

[5] Wikipedia, "Degrees Of Freedom (statistics)," [Online]. Available:
https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics).

[6] Wikipedia, "Student t distribution," [Online]. Available:
https://en.wikipedia.org/wiki/Student%27s_t-distribution.

[7] Wikipedia, "Bessel Correction," [Online]. Available:
https://en.wikipedia.org/wiki/Bessel%27s_correction.

[8] D. W. W. Richard A. Johnson, Applied Multivariate Statistical Analysis, US: Pearson Education,
2007.
