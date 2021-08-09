---
title: "Introduction to Improved Local Binary Patterns"
categories:
  - Machine Learning
tags:
  - Machine Learning
toc: true
comments: true
header:
  teaser: "/assets/images/header/lambda_01.jpg"
---

Trong bài này, mình sẽ giới thiệu một biến thể khá kinh điển của LBP, ILBP hay Improved Local Binary Pattern được trình bày trong bài báo Face Detection Using Improved LBP Under Bayesian Framework bởi Hongliang Jin, Qingshan Liu, Hanqing Lu, Xiaofeng Tong đến từ National Lab of Pattern Recognition, Institute of Automation, Chinese Academy of Sciences, China được công bố tại hội nghị Third International Conference on Image and Graphics (ICIG'04) năm 2004
	
Đặc trưng ILBP là một cải tiến của đặc trưng LBP, xem xét cả dáng cục bộ (local shape) và thông tin kết cấu (texture information) thay vì thông tin xám thô (raw grayscale information) và nó cực kỳ tốt với sự thay đổi ánh sáng (illumination variation)

## (1) Phương pháp xác định giá trị

Với một tập $P$ lân cận và một đường tròn bán kính $R$, ta dễ dàng tính được hiệu số giữa pixel trung tâm (central pixel) $g_c$ và lân cận của nó $\{g_0, ..., g_{p-1}\}$

$$
    \begin{gather*}
        LBP_{P,R} = \sum_{i=0}^{P-1}s(g_i - g_c)^2\\
        s(x) = \begin{cases}
            1, x > 0\\
            0, x \leq 0
        \end{cases}
    \end{gather*}
$$

![](/assets/media_blog_posts/2021-08-09-intro-ilbp/cau_d.png)

Đặc trưng Improved Local Binary Pattern từ ý tưởng ánh xạ giá trị điểm ảnh sang một khoảng giá trị mới, có thể được khai triển như sau:

$$
	\begin{gather*}
		LBP_{P,R} = \sum_{i=0}^{P-1}s(g_i-m)2^i+s(g_c - m)2^P\\
		s(x) = \begin{cases}
			1, x > 0\\
			0, x \leq 0
		\end{cases}\\
		m = \frac{1}{P+1}\left(\sum_{i=0}^{P-1}g_i + g_c\right)
	\end{gather*}
$$

![](/assets/media_blog_posts/2021-08-09-intro-ilbp/cau_d_1.png)

![](/assets/media_blog_posts/2021-08-09-intro-ilbp/cau_d_2.png)

## (2) Ưu điểm và nhược điểm, trên cơ sở so sánh LBP

Về ưu điểm của ILBP:

- Giữa được cấu trúc cục bộ trong một số hoàn cảnh nhất định. Khi sử dụng LBP truyền thống, ta chỉ có thể sử dụng $2^8 = 256$ trong tổng số 511 patterns từ một patch $3 \times 3$
- ILBP xem xét nhiều hơn pixel trung tâm, trong đa số trường hợp, pixel trung tâm có nhiều thông tin hơn những lân cận của nó. Vì thế, trong ILBP, pixel trung tâm được mang trọng số lớn nhất

Về nhược điểm ILBP

- Những hình ảnh có chứa nguồn sáng cực mạnh khi sử dụng phương pháp này sẽ có kết quả không cao vì những thông tin cấu trúc đã bị mất mát
