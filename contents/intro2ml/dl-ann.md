---
layout: single
permalink: /intro2ml/modern-ml-artificial-neural-networks
title: "[Modern Machine Learning - Deep Learning] Artificial Neural Networks"
author_profile: true
toc: true
comments: True
---


Mạng neural thần kinh nhân tạo (Artificial Neural Networks hay gọi cho gọn là Neural Networks) là một hệ thống tính toán dựa trên mạng neural thần kinh sinh học, mà có ở người và động vật. Nó mô phỏng lại cách hoạt động của mạng thần kinh sinh học thông qua việc tính toán trên máy tính. Một mô hình ANN là một tập các tầng (layers) nút đơn vị tính toán, bao gồm tầng đầu vào (input layer), các tầng ẩn (hidden layers) - thường là nhiều hơn một, và tầng đầu ra (output layer). 

Mỗi một nút mô phỏng lại cách hoạt động của neurons trong não sinh học. Một neuron trong ANN nhận một tính hiệu đầu vào, sau đó xử lý chúng, và lan truyền đến những neuron khác để cập nhật trọng số. Các neuron được liên kết với nhau bởi các cạnh có trọng số. Trọng số neuron và cạnh được hiệu chỉnh trong quá trình huấn luyện mô hình. Để sau quá trình huấn luyện, ta có được một tín hiệu đầu ra, mang số liệu giá trị thực chỉ kết quả dự đoán được.


## Giới thiệu

ANN là một bước quan trọng trong việc cải tiến các mô hình học máy cổ điển. Hình minh họa bên dưới cho thấy điểm khác biệt giữa phương pháp học máy cổ điển và phương pháp học máy hiện đại (ở đây, mình xin phép được nói gọn là học sâu - deep learning).

![](https://blog.dataiku.com/hs-fs/hubfs/machine%20learning%20vs%20deep%20learning.png?width=602&name=machine%20learning%20vs%20deep%20learning.png)

Về cơ bản, đối với học máy cổ điển, chúng ta cần phải xử lý dữ liệu đầu vào để rút trích ra những đặc trưng. Những đặc trưng này gọi là handcrafted features - đặc trưng thủ công (tự tạo), rồi sau đó mới đưa vào mô hình học, tức là giai đoạn huấn luyện, kiểm tra mô hình. Các thuật toán thường được dùng để giải quyết các dạng bài toán hồi quy (regression) và phân lớp (classification) như: linear regression, logistic regression, decision tree hay SVM, v.v. 

Còn đối với phương pháp học sâu, chủ yếu dựa trên mạng neural, chúng ta không cần phải tự tạo ra những đặc trưng thủ công. Mọi chuyện từ rút trích đặc trưng, đưa vào mạng phân lớp (hồi quy) đều được tích hợp vào một cái hộp đen (a black box). Cái chúng ta cần là đổ vào thật nhiều dữ liệu (data) và nó sẽ tự động cho ra kết quả. 

Rõ ràng, học sâu có nhiều lợi thể hơn các mô hình học máy cổ điển.
- Hiệu suất cao vượt trội: Các mạng học sâu đạt được hiệu suất, độ chính xác vượt xa các phương pháp học máy cổ điển trong hầu hết các lĩnh vực từ xử lý giọng nói (speech processing), thị giác máy tính (computer vision), xử lý ảnh số (digital image processing), ngôn ngữ tự nhiên (natural language processing) hay trong trò chơi (game).
- Mở rộng quy mô hiệu quả với lượng dữ liệu lớn: Các mạng học sâu mở rộng tốt hơn với lượng dữ liệu nhiều như hiện nay, so với các mô hình học máy cổ điển.

![](https://i.stack.imgur.com/TuHv1.png)

- Không cần kỹ thuật đặc trưng (feature engineering): Như đã nói ở trên, các phương pháp máy học cổ điển cần kỹ thuật đặc trưng rất phức tạp và tốn nhiều chi phí, công sức. Những mô hình học sâu chỉ cần truyền dữ liệu qua các tầng mạng học và có thể tự động rút trích ra những đặc trưng "sâu" từ đó đạt được hiệu suất cải thiện vượt trội.
- Khả năng thích ứng và chuyển tiếp: Các kỹ thuật học sâu có thể thích nghi với các miền khác nhau, nhờ tính toán tổng quát hóa cao vượt trội so với các thuật toán máy học cổ điển. Phương pháp học chuyển tiếp (transfer learning) đã chứng minh điều này. Nó sử dụng những mạng học sâu đã được huấn luyện trước trên các tập dữ liệu lớn, sau đó áp dụng cho những bài toán nhỏ hơn, với hy vọng sẽ có được một điểm bắt đầu tốt hơn, tiết kiệm chi phí và thời gian huấn luyện. 

Tuy nhiên, ta cũng không nên coi nhẹ các phương pháp học máy cổ điển, bởi vì chúng vẫn đứng một vai trò trụ cột trong lĩnh vực nghiên cứu và ứng dụng máy học. So với học sâu, ta vẫn có thể tận dụng ưu thế của những phương pháp này:
- Xử lý những dữ liệu có kích thước nhỏ: Để đạt được hiệu suất tốt nhất có thể, chúng ta cần một lượng dữ liệu lớn cho các mạng học sâu. Với những bộ dữ liệu nhỏ, việc áp dụng các mô hình Deep thường sẽ dễ dẫn đến tình trạng overfitting. Do đó, các phương pháp học máy cổ điển trở thành hướng giải quyết chủ đạo trong tình huống này.
- Tính toán với chi phí thấp và hoạt động hiệu quả trong điều kiện thiếu thốn tài nguyên vật lý: Các phương pháp học sâu tiêu tốn tài nguyên rất lớn. Để huấn luyện một mô hình như thế, việc có tài nguyên mạnh là một lợi thế lớn (GPU, SSD, RAM, CPU, ...). Những thuật toán máy học cổ điển thì không cần như thế. Do đó, việc áp dụng các thuật toán này cho môi trường thiếu thốn tài nguyên là rất hợp lý, nhất là nhúng lên các thiết bị nhỏ (IoT).
- Dễ dàng kết hợp vào các mô hình học sâu để tăng cường hiệu suất tính toán, thời gian thực hiện và độ chính xác.


## Artificial Neural Networks

Mô hình Artificial Neural Networks hay gọi cho gọn là Neural Networks, mạng thần kinh nhân tạo là một mô hình suy luận, được lấy ý tưởng từ não bộ con người và động vật, bao gồm hàng triệu neurons và hàng tỉ liên kết giữa chúng. 

![](https://www.lifewire.com/thmb/GTZkjZopmmb3fXL3L3lSve3bv1w=/650x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/what-is-neural-network-bd8fc6a5fb6f40bba291b64e609ee0b7.jpeg)

Não bộ sinh học được xem là một hệ thống xử lý thông tin cực kỳ phức tạp, phi tuyến và có khả năng xử lý song song một cách tuyệt vời. Theo thống kê, trong não bộ con người có khoảng $10^{10}$ neurons với gần $10^{4} - 10^{5}$ liên kết. Điều đặt ra động lực thúc đẩy con người nghiên cứu ra những phương pháp tính toán để có thể mô phỏng lại cách hoạt động của não bộ sinh học, đạt dược trí tuệ nhân tạo tổng quát (General Artificial Intelligence).

Hình (a) mô tả cách hoạt động của một tế bào neuron thần kinh sinh học, trong đó:
- Dendrite: sợi nhánh
- Nucleus: Nhân
- Cell body: Thanh neuron
- Axon: sợi trục
- Synapse: cơ quan thụ cảm

Khi nhận được tín hiệu đầu vào từ những tế bào thần kinh khác, các tín hiệu này được tổng hợp cho đến kinh chúng vượt một ngưỡng cụ thể nào đó. Khi vượt quá ngưỡng, tế bào thần kinh kích hoạt, gửi xung điện dọc theo sợi trục để đi đến những tế bào kế tiếp. 

![](https://www.researchgate.net/publication/317679065/figure/fig6/AS:654765507751936@1533119670109/1-A-comparison-between-a-human-neuron-and-an-ANN-neuron-a-Shows-an-illustration-of-a.png)

ANN cũng cố gắng hoạt động một cách tương tự như thế. Mỗi neuron trong ANN là một phần tử xử lý thông tin đơn vị. Chúng được liên kết với nhau thông qua các cạnh. Mỗi neuron khi nhận vào một số tín hiệu đầu vào thông qua các liên kết của nó, nó tiến hành xử lý để cho ra kết quả đầu ra. Mỗi liên kết với một trọng số nhất định thể hiện mức độ/ trọng lượng cho đầu vào neuron. Quá trình học của ANN học thông qua việc hiệu chỉnh những trọng số này.

Dưới đây là minh họa một số kiến trúc mạng ANN thường gặp:

![](https://www.asimovinstitute.org/wp-content/uploads/2019/04/NeuralNetworkZoo20042019.png)


## Mô hình ANN đơn giản nhất - Perceptron

Trong máy học, perceptron là một thuật toán cho học giám sát, tức là phương pháp học mà ta có dữ liệu đã được gán nhãn, của bài toán phân lớp nhị phân. Thuật toán perceptron được phát minh vào năm 1958, trong phòng thí nghiệm Cornell Aeronautical, bởi Frank Rosenblatt và từ đó có nhiều cải tiến liên quan đến nó.  Marvin Minsky và Seymour Papert cho thấy rằng multi-layer perceptron có khả năng xử lý một XOR function trong cuốn sách nổi tiếng Perceptron (ở phiên bản sửa lỗi lần thứ 2). 

Đầu vào của thuật toán: $n$ đầu vào $x_1, x_2, ..., x_n$

Đầu ra của thuật toán: chỉ có một đầu ra $o$

Đầu tiên, mô hình tính toán một tổng có trọng số của những đầu vào

$$
in = w_0 + w_1x_1 + x_2w_w + ... + w_nx_n
$$

Sau đó, nó đưa tổng trên qua một hàm kích hoạt (activation function) $g(in)$ (hàm này là một hàm phi tuyến, ví dụ như sign, sigmoid, tanh, ...)

$$
o(x_1, x_2, ..., x_n) = g(in) = \begin{cases}1 \text{ if } in > 0 \\ -1 \text{ otherwise }\end{cases}
$$

![](https://i.stack.imgur.com/KUvpQ.png)

Perceptron có thể đại diện cho một số hàm, ví dụ như một số hàm logic như NOT, OR, AND hoặc XOR

Với NOT, NOT(x) là một hàm một biến, với một đầu vào và đầu ra có 2 giá trị 0 và 1. Cho trước hai tham số $w$ và $b$, trong đó $w$ là vector trọng số, $b$ là bias (thiên vị), thuật toán thực hiện tính toán $\hat{y} = f(xw + b)$

Ta có thể chọn giá trị trọng số $w=-1$ và $b=0.25$ (Còn nhiều giá trị khác nữa :v)

```python
import numpy as np

def sign(s):
    return (0, 1)[s >= 0]

def perceptron(x, w, b):
    return sign(np.dot(x, w) + b)

def not_perceptron(x):
    return perceptron(x, w=-1, b=0.25)

print("not(1) = {}".format(not_perceptron(1))) # 0
print("not(0) = {}".format(not_perceptron(0))) # 1
```
Với AND, AND$(x_1, x_2)$ là một hàm nhiều biến, cụ thể là hai biến. Nó nhận vào đầu vào là vector chứa $x$ và $y$ với giá trị nhị phân, 1 đầu ra cũng với giá trị nhị phân. Cho trước hai tham số $w$ và $b$, trong đó $w$ là vector trọng số, $b$ là bias (thiên vị), thuật toán thực hiện tính toán $\hat{y} = f(xw + b) = f(w_1x_1 + w_2x_2 + b)$ 

Chọn $w=[1, 1]$ và $b=-2$ (Còn rất nhiều trường hợp khác, các bạn có thể mò)

```python
import numpy as np

def sign(s):
    return (0, 1)[s >= 0]

def perceptron(x, w, b):
    return sign(np.dot(x, w) + b)

def and_perceptron(x):
    return perceptron(x, w=[1, 1], b=-2)

print("and(1, 1) = {}".format(and_perceptron([1, 1]))) # 1
print("and(1, 0) = {}".format(and_perceptron([1, 0]))) # 0
print("and(0, 1) = {}".format(and_perceptron([0, 1]))) # 0
print("and(0, 0) = {}".format(and_perceptron([0, 0]))) # 0
```
Với OR, OR$(x_1, x_2)$ cũng là một hàm nhiều biến, cụ thể là hàm hai biết. Nó cũng nhận  là vector chứa $x$ và $y$ với giá trị nhị phân, 1 đầu ra cũng với giá trị nhị phân. Chúng ta có thể sử dụng kiến trúc cũ.

Ta có thể chọn $w=[1.1]$ và $b=-1$

```python
import numpy as np

def sign(s):
    return (0, 1)[s >= 0]

def perceptron(x, w, b):
    return sign(np.dot(x, w) + b)

def or_perceptron(x):
    return perceptron(x, w=[1, 1], b=-1)

print("or(1, 1) = {}".format(or_perceptron([1, 1]))) # 1
print("or(1, 0) = {}".format(or_perceptron([1, 0]))) # 1
print("or(0, 1) = {}".format(or_perceptron([0, 1]))) # 1
print("or(0, 0) = {}".format(or_perceptron([0, 0]))) # 0
```

Đối XOR thì khó hơn một chút. Perceptron thông thường như cũ thì không thể đại diện được. Chúng ta cần 1 số biến đổi nhất định

$$
\text{XOR}(x, y) = \text{AND}(OR(x, y), \text{NOT}(\text{AND}(x, y)))
$$

Và áp dụng biến đổi này, ta có thể kết hợp kiến trúc cũ để code như sau

```python
import numpy as np

def sign(s):
    return (0, 1)[s >= 0]

def perceptron(x, w, b):
    return sign(np.dot(x, w) + b)

def not_perceptron(x):
    return perceptron(x, w=-1, b=0.25)

def and_perceptron(x):
    return perceptron(x, w=[1, 1], b=-2)

def or_perceptron(x):
    return perceptron(x, w=[1, 1], b=-1)

def xor_perceptron(x):
    x = and_perceptron(x)
    x = and_perceptron([not_perceptron(x), or_perceptron(x)])
    return x

print("xor(1, 1) = {}".format(xor_perceptron([1, 1]))) # 0
print("xor(1, 0) = {}".format(xor_perceptron([1, 0]))) # 1
print("xor(0, 1) = {}".format(xor_perceptron([0, 1]))) # 1
print("xor(0, 0) = {}".format(xor_perceptron([0, 0]))) # 0
```

Qua ví dụ trên, ta cần kết hợp nhiều tầng perceptron lại với nhau để có thể giải quyết bài toán đại diện hàm XOR. Và đây cũng là ý tưởng của multi-layer perceptrons.

## Go deeper - Multilayer Perceptron (MLP)

Multi-layer perceptron là một cấu trúc dữ liệu đồ thị vòng hữu hướng (Directed acyclic graph), gồm nhiều tầng bên trong nó:
- Tầng đầu tiên được gọi tầng nhập/ tầng đầu vào (input layer)
- Tầng cuối cùng được gọi tầng xuất/ tầng đầu ra (output layer)
- Các tầng khác nằm giữa hai tầng đầu tiên và cuối cùng được gọi là các tầng ẩn (hidden layers)


Mỗi tầng gồm nhiều nút, mỗi nút là một neuron. Các nút được liên kết trực tiếp để lan truyền kích hoạt. Ta gọi $w_{jk}^{l}$ là trọng số của cạnh liên kết từ neuron thứ $k$ trong tầng thứ $l-1$ đến neuron thứ $j$ trong tầng thứ $l$. Như vậy mỗi tầng có ma trận trọng số $w^{l}$ và một vector bias (vector thiên vị) $b^{l}$. Tại neuron thứ $j$ trong tầng thứ $l$ có một kích hoạt $a_{j}^{l}$. 

$$
\text{input} = \sum_{k}w_{jk}^{l}a_k^{l-1}+b_j^{l}
$$

Sau đó, dùng một hàm kích hoạt $g$ áp dụng lên tổng này, hàm kích hoạt là một hàm phi tuyến, có thể là hàm sigmoid, hàm step, hàm sign, hàm linear, v.v. Tại tầng thứ $l$, neuron thứ $j$ tính toán một tổng có trọng số từ những đầu vào của nó:

$$
a_j^{l} = g(\text{input}) = g\left(\sum_{k}w_{jk}^{l}a_k^{l-1}+b_j^{l}\right)
$$

Ví dụ như mô hình multi-layer perceptron dưới đây. Với tầng đầu tiên nhận 4 đầu vào và tầng cuối cùng có 1 đầu ra. Các tầng ẩn 1, 2, ..., 6 được liên kết đầy đủ.

![](https://i.stack.imgur.com/epElm.png)

Một số hàm kích hoạt thường dùng

![](https://i.pinimg.com/originals/e8/b0/fd/e8b0fdeb7e13353fdf115c161d02b191.png)

Định lý về khả năng biểu diễn (expressive capabilities) của MLP:
- Các hàm luận lý (Boolean functions): Mọi hàm luận lý có thể được biểu diễn bởi mạng với một tầng ẩn nhưng có thể cần đơn vị ẩn (hidden units) theo cấp số nhân (về số lượng đầu vào).
- Các hàm liên tục (Continuous functions):
  - Mọi hàm liên tục bị chặn (bounded continuous function) có thể được xấp xỉ với độ lỗi nhỏ tùy ý bằng mạng với một tầng ẩn.
  - Bất kỳ hàm nào cũng có thể được xấp xỉ với độ chính xác tùy ý bởi một mạng với hai tầng ẩn.

Một mô hình học bao gồm
- Tập giả thuyết (Hypothesis set) hay không gian hàm số (function space) hay không gian tìm kiếm $$\mathcal{F} = \{ f \| y = f(x, W) \}$$
- Thuật toán học (learning algorithm): Gradient-based algorithm, Delta learning rule, Newton method, Conjugate gradient, Quasi-Newton method, Levenberg-Marquadt algorithm, ...

Trong giai đoạn huấn luyện mô hình, ta khớp mô hình với dữ liệu dựa trên một hàm mất mát (cost function). Hàm mất mát có thể được đưa ra từ nhiều phương pháp khác nhau tùy thuộc vào bài toán, ví dụ như Mean Square Error, Cross Entropy, .v.v. Việc lựa chọn tầng đầu ra cho mô hình mạng neural cũng tùy thuộc vào bài toán đang giải quyết là bài toán phân lớp (classification) hay hồi quy (regression).


## Gradient-Based Learning

Mục tiêu của việc học là tìm trọng số mà cực tiểu hàm mất mát C. Các thuật toán/ kỹ thuật dựa trên đạo hàm (gradient) thường được sử dụng để thực hiện việc này.

Bài toán học được xây dựng như bài toán cực tiểu một hàm mất mát/ hàm mục tiêu, $J$. Hàm này là một hàm có thể đo hiệu suất của một mạng neural trên một bộ dữ liệu. 

Một cách tổng quát mà nói, hàm mất mát bao gồm hai khái niệm là lỗi và chính quy hóa (regularization). Khái niệm về lỗi đánh giá một mạng neural khớp dữ liệu như thế nào. Khái niệm chính quy hóa (regularization) được dùng để tránh tình trạng overfitting bằng cách kiểm soát độ phức tạp của mô hình.

“Regularization is any modification we make to a learning model that is
intended to reduce its generalization error but not its training error.”

![](https://imaddabbura.github.io/post/coding-nn-regularization/featured.png)

Bằng cách thêm một số ràng buộc chính quy cho thuật toán học, ta có thể giúp nó ít nhạy cảm với dữ liệu hơn và ổn định quá trình huấn luyện mô hình. Chúng ta không thể tìm được một hàm lý tưởng cho dữ liệu, do đó chiến lược tốt nhất là phải xây dựng một mô hình phức tạp để có thể cực tiểu độ lỗi thấp nhất. Điều này lại gây là một điều là mô hình rất tốt trên dữ liệu huấn luyện nhưng với dữ liệu mới thì nó lại không tốt (vấn đề overfitting). Khi dùng chính quy hóa, chúng ta cần giảm độ lỗi tổng quá và có thể làm tăng độ lỗi trong quá trình huấn luyện, ta cố gắng đưa mô hình từ phức tạp trở về tình trang ổn định hơn bằng tăng thiên vị (bias) và giảm phương sai (variance).

Thông thường thì ta sẽ có một số phương pháp để thực hiện việc này như:
- L2 Parameter Regularization hay weight decay: Phương pháp thêm vào một chuẩn L2 để phạt hàm mục tiêu nhằm đưa những trọng số hướng trở lại như ban đầu.
- L1 Parameter Regularization hay Lasso: Thay vì dùng chuẩn L2 (L2 norm), một số trọng số có thể thực sự bằng 0. Nó thu nhỏ tất cả các trọng số bằng cùng một lượng bằng cách thêm một lượng chuẩn L1 vào hàm mục tiêu.
- Dropout: Trong một lần duyệt, ta ngẫu nhiên bỏ bớt một số neuron trên mỗi tầng và không dùng những neuron này ở pha lan truyền tiến và lan truyền ngược. Điều này giúp cho mạng neural trở nên thưa hơn, dễ dàng huấn luyện. Ngoài ra, mô hình sẽ không biết neurons nào bị bỏ đi trong mỗi lần duyết huấn luyện, điều này giống như huấn luyện những mô hình khác nhau qua mỗi lần duyệt. Về trực giác, ta cảm thấy nó sẽ giúp mô hình thích nghi hơn với sự thay đổi dữ liệu.
- Augmentation: Bằng cách thêm dữ liệu giả thông qua việc phát sinh mẫu từ dữ liệu huấn luyện và thêm những tính chất như biến dạng như thu phóng kích thước, xoay chiều. Nhờ đó, dữ liệu được tăng cường hơn và càng nhiều dữ liệu, ta hy vọng mô hình có thể đạt được hiệu suất tốt hơn.
- Early Stopping: Phương pháp này nhằm tối ưu hàm mất mát và chính quy quy hóa. Trong quá trình huấn luyện, mỗi lần lặp, ta ghi lại độ lỗi xác nhận (validation error). Nếu độ lỗi xác nhận cải thiện, ta tiếp tục ghi nhận cho đến khi thuật toán dừng. Nếu không cải thiện, theo một ngưỡng nào đó, việc huấn luyện mô hình dừng lại.

Hàm mất mát phụ thuộc vào những tham số thích ứng (bias và trọng số) trong mạng neural. Ta có thể gom nhóm tất cả tham số này thành:

$$
J(\theta) = J(\theta_1, \theta_2, \theta_3, ..., \theta_D)
$$

Và bài toán của chúng ta là

$$
\hat{\theta} = \text{arg}\underset{\theta}{\text{ min }}J(\theta)
$$

Phương pháp Gradient Descent: Bắt đầu tại điểm $\theta^{(0)}$ và di chuyển từ $\theta^{(t)}$ đến $\theta^{(t+1)}$ cho đến khi thỏa mãn được một tiêu chí dừng.

$$
\theta^{(t+1)} \leftarrow \theta^{(t)} - \eta\nabla_{\theta}J
$$

Trong đó: $\eta$ là tốc độ học (learning rate), $0 < \eta < 1$ và

$$
\nabla_{\theta}J = \left[\frac{\partial J}{\partial \theta_1}, \frac{\partial J}{\partial \theta_2}, ..., \frac{\partial J}{\partial \theta_D}\right]^{\top}
$$

![](https://www.researchgate.net/profile/Alexander-Amini/publication/325142728/figure/fig1/AS:766109435326465@1559666131320/Non-convex-optimization-We-utilize-stochastic-gradient-descent-to-find-a-local-optimum.jpg)

Ta có ba biến thể của phương pháp gradient descent. Phụ thuộc vào lượng dữ liệu, mà chúng ta đánh đổi giữa độ chính xác của việc cập nhật tham số và thời gian thực thi.
- Batch gradient descent
- Stochastic gradient descent
- Mini-batch gradient descent

Với Batch gradient descent, ta tính toán đạo hàm của hàm mất mát liên quan đến tham số $\theta$ cho toàn bộ dữ liệu huấn luyện $\mathcal{D}$

$$
\theta^{(t+1)} \leftarrow \theta^{(t)} - \eta\nabla_{\theta}J(\theta^{(t)}, \mathcal{D})
$$

Phương pháp này có thể rất chậm và có thể khó xử lý cho những bộ dữ liệu mà không khớp với bộ nhớ. Bên cạnh dó, nó cũng không cho phép cập nhật mô hình trực tuyến.


Với Stochastic gradient descent, nó thực hiện cập nhật tham số cho mỗi mẫu huấn luyện $x^{(i)}$ và nhãn $y^{(i)}$ của dữ liệu huấn luyện $\mathcal{D}$

$$
\theta^{(t+1)} \leftarrow \theta^{(t)} - \eta\nabla_{\theta}J(\theta^{(t)}; x^{(i)}; y^{(i)})
$$

Để sử dụng SGD một cách tốt nhất có thể, chúng ta nên trộn dữ liệu huấn luyện tại mỗi epoch. Việc thực hiện cập nhật của SGD thường với một phương sai lớn, điều này gây ra biến động lớn cho hàm mục tiêu.

Với Mini-batch gradient descent, phương pháp này thực hiện một cập nhật cho mỗi mini-batch của $n$ mẫu huấn luyện của bộ dữ liệu huấn luyện $\mathcal{D}$

$$
\theta^{(t+1)} \leftarrow \theta^{(t)} - \eta\nabla_{\theta}J(\theta^{(t)}; x^{(i+n)}; y^{(i+n)})
$$

Bằng việc thực thi trên những mini-batch, gồm một số lượng mẫu từ dữ liệu huấn luyện, nó giảm phương sai của những cập nhật tham số, dẫn đến việc hội tụ một cách ổn định hơn. 

Bên cạnh những kỹ thuật này, chúng ta cũng có những phương pháp giải quyết vấn đề gradient tại các điểm yên ngựa (saddle point) và tại các vùng phẳng của đạo hàm. Một số kỹ thuật Momentum, Nesterov accelerated gradient, Adagrad, Adadelta, RMSprop, Adam, AdaMAx, ... sẽ giúp giải quyết một số vấn đề của Gradient descent.

## Back-Propagation Learning

Kiến trúc mạng neural với các biểu diễn với dạng đồ thị cổ điển rất khó tính toán và phức tạp. Ta cần sử dụng một đại diện khác để có thể tính toán dễ dàng hơn, đó là đồ thị tính toán (giản lược) (reduced graph/ computational graph)

![](https://media5.datahacker.rs/2021/01/54-1-1024x490.jpg)

Đồ thị tính toán thường có ba loại nút:
- Các nút đầu vào (input nodes): mang dữ liệu đầu vào (tín hiệu đầu vào). Ví dụ như trên hình vẽ là các nút màu xanh
- Các nút tham số (parameter nodes): mang tham số của mô hình, các giá trị tham số được cập nhật để tính toán mất mát. Ví dụ như trên hình vẽ là các màu cam.
- Các nút tính toán (computation nodes): các nút được dùng cho tính toán giá trị đầu ra. Ví dụ như trên hình vẽ là các màu vàng.

Hình bên trên là mô hình hồi quy tuyến tính. Để tính toán được mất mát, ta thực hiện như sau:
- Bước 1: Với những giá trị đầu vào $x$ tham số $w$, khởi tạo biến $u$ gán bằng tích vô hướng $x$ và $w$
- Bước 2: Thêm giá trị thiên vị (bias) $b$ vào biến $u$. Nhờ đó, ta tính toán được giá trị $\hat{y}$ dự đoán của mô hình
- Bước 3: Tính toán độ lỗi $\hat{y} - y$, trong đó $y$ là giá trị xác thực từ dữ liệu đầu vào. Ta có được một biến mới là $e$
- Bước 4: Tính toán bình phương của biến này và gán kế quả cho biến $\mathcal{L}$ đại diện cho mất mát.

Thuật toán lan truyền ngược được đề xuất bởi Bryson và Ho vào năm 1969 và được sử dụng rộng rãi trong nhiều công trình, mô hình mạng neural hiện nay. Thuật toán cho chúng ta một cách tính toán gradient của hàm mất mát 

Đầu vào (Input): Một đồ thị tính toán $G = \left<n, l, E, u^1 ... u^n, d^1 ... d^n, f^{l+1} ... f^n \right>$. Giá trị của các nút lá là $u^1 ... u^l$

Thuật toán:

Ở pha lan truyền tiến (forward pass):

Với $i = (l + 1) ... n$, tính toán

$$
u^i = f^i(\alpha^i)
$$

Trong đó:

$$
\alpha^i = \left< u^j | (j, i) \in E\right>
$$

Ở pha lan truyền ngược (backward pass):

Khởi tạo tập $P^n = I(d^n)$ trong đó $I(d^n)$ là ma trận đơn vị có kích thước $d^n \times d^n$

Với $j = (n - 1) ... 1$, tính toán

$$
\underbrace{P^j}_{d^n \times d^j} = \sum_{i:(j, i)\in E}\underbrace{P^i}_{d^n \times d^i} \times \underbrace{J^{j \rightarrow i}(\alpha^i)}_{d^i \times d^j}
$$

Trong đó: $\alpha^i$ được tính toán bởi pha lan truyền tiến phía trên.

Đầu ra (ouput): Với $j = 1 ... l$, trả ra Jacobian

$$
P^j = \left.\begin{matrix}\frac{\partial u^n}{\partial u^j}\end{matrix}\right|_{h^n}^{u^1 ... u^l}
$$

Ví dụ: Áp dụng thuật toán lan truyền ngược (back-propagation) cho mô hình hồi quy tuyến tính tại một điểm đơn $(x, y)$, với $x=1$, $y=2$. 

Ta có thể ký hiệu: $u^1 = x$, $u^2 = w$, $u^3 = u$, $u^4 = b$, $u^5 = \hat{y}$, $u^6 = y$, $u^7 = e$, $u^8=\mathcal{L}$

Các hàm cục bộ được định nghĩa như sau:

$$
f^3(x, w) = x \cdot w = u
$$

$$
f^5(u, b) = u + b = x \cdot w + b = \hat{y}
$$

$$
f^7(\hat{y}, y) = \hat{y} - y = x \cdot w + b - y = e
$$

$$
f^8(e) = e^2 = (x \cdot w + b - y)^2
$$

Từ đó, ta có được các hàm Jacobian cục bộ như sau:

$$
J^{(1) \rightarrow (3)}(u^1, u^2) = \left.\begin{matrix}\frac{\partial u^3}{\partial u^1}\end{matrix}\right|_{u^1, u^2}^{f^3} = u^2 = w
$$

$$
J^{(2) \rightarrow (3)}(u^1, u^2) = \left.\begin{matrix}\frac{\partial u^3}{\partial u^2}\end{matrix}\right|_{u^1, u^2}^{f^3} = u^1 = x
$$


$$
J^{(3) \rightarrow (5)}(u^3, u^4) = \left.\begin{matrix}\frac{\partial u^5}{\partial u^3}\end{matrix}\right|_{u^3, u^4}^{f^5} = u^4 = b
$$

$$
J^{(4) \rightarrow (5)}(u^3, u^4) = \left.\begin{matrix}\frac{\partial u^5}{\partial u^4}\end{matrix}\right|_{u^3, u^4}^{f^5} = 1
$$

$$
J^{(5) \rightarrow (7)}(u^5, u^6) = \left.\begin{matrix}\frac{\partial u^7}{\partial u^5}\end{matrix}\right|_{u^5, u^6}^{f^7} = 1
$$

$$
J^{(6) \rightarrow (7)}(u^5, u^6) = \left.\begin{matrix}\frac{\partial u^7}{\partial u^6}\end{matrix}\right|_{u^5, u^6}^{f^8} = -1
$$

$$
J^{(7) \rightarrow (8)}(u^7) = \left.\begin{matrix}\frac{\partial u^8}{\partial u^7}\end{matrix}\right|_{u^7}^{f^8} = 2u^7 = 2 \cdot e
$$

Pha lan truyền tiến

$$
f^1(x, w) = x \cdot w = 1 \times 5 = 5
$$

$$
f^2(u, b) = u + b = x \cdot w + b = \hat{y} = 5 + 1 = 6
$$

$$
f^3(\hat{y}, y) = \hat{y} - y = x \cdot w + b - y = 6 - 2 = 4 
$$

$$
f^4(e) = e^2 = (x \cdot w + b - y)^2 = 16
$$

$$
J^{(1) \rightarrow (3)}(u^1, u^2) = w = 5
$$

$$
J^{(2) \rightarrow (3)}(u^1, u^2) = x = 2
$$

$$
J^{(3) \rightarrow (5)}(u^3, u^4) = b = 1
$$

$$
J^{(4) \rightarrow (5)}(u^3, u^4) =  1
$$

$$
J^{(5) \rightarrow (7)}(u^5, u^6) = 1
$$

$$
J^{(6) \rightarrow (7)}(u^5, u^6) = -1
$$

$$
J^{(7) \rightarrow (8)}(u^7) = 2 \cdot e
$$

![](https://media5.datahacker.rs/2021/01/55-1-1024x519.jpg)

Khởi tạo: $P^8 = 1$

$$
P^7 = P^8 \times J^{(7) \rightarrow (8)}(u^7) = 1 \cdot 2 \cdot e = 8
$$

$$
P^5 = P^7 \times J^{(5) \rightarrow (7)}(u^5, u^6) = 8 \times 1 = 8
$$

$$
P^3 = P^5 \times J^{(3) \rightarrow (5)}(u^3, u^4) = 8 \times 1 = 8
$$



![](https://media5.datahacker.rs/2021/01/57-1024x821.jpg)



## Tài liệu tham khảo

[1] [004 PyTorch – Computational graph and Autograd with Pytorch](https://datahacker.rs/004-computational-graph-and-autograd-with-pytorch)

[2] Goodfellow, I., Bengio, Y., and Courville, A. (2016). Deep learning. MIT press.

[3] Russell, S. and Norvig, P. (2016). Artificial intelligence: a modern approach. Pearson Education Limited.
   