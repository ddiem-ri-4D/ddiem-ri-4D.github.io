---
title: "Introduction to Convolutional Neural Networks"
categories:
  - Machine Learning
tags:
  - Machine Learning
toc: true
comments: true
header:
  teaser: "/assets/images/header/lambda_01.jpg"
---

Bài viết trích từ một câu hỏi trong Đồ án cuối kỳ của mình, nói chung là note vài thứ về Convolutional Neural Networks.

##  Mô tả tổng quan về mạng nơron tích chập (CNN)

Những công trình đầu tiên vào năm 1959 của David Hubel và Torsten Wiesel đưa ra mô tả về "simple cell" và "complex cell" trong vỏ não thị giác của con người (human visual cortex) và được đề xuất sử dụng trong lĩnh vực Nhận dạng mẫu (Pattern Recognition)

Một "Simple cell" tương ứng với cạnh và đường trục trong một không gian cụ thể:

![](/assets/media_blog_posts/2021-08-09-intro-cnns/simple_cell.png)

Một "Complex cell" cũng tương ứng với cạnh và đường trục trong một không gian cụ thể nhưng nó khá khác so với "Simple cell"

![](/assets/media_blog_posts/2021-08-09-intro-cnns/complex_cell_simple_cell.jpg)

Với "simple cell" có thể chỉ ứng với một trục ngang ở cạnh dưới của một bức ảnh, còn với "complex cell" có thể ứng các trục ngang ở dưới (bottom), giữa (middle) hoặc trên cùng (top) của một bức ảnh.

Cho đến năm 1962, Hubel và Wiesel đề xuất một công trình cho thấy rằng Complex Cell đạt được bất biến không gian bằng cách "**summing**" - tổng hợp đầu ra của nhiều simple cell tham chiếu cùng hướng (cùng đường trục) nhưng khác nhau về vị trí tiếp nhận (có thể bottom, middle hoặc top). Khái niệm về một bộ nhận diện phức tạp có thể được tổng hợp từ nhiều bộ nhận diện đơn giản được phát hiện trong **hệ thống thị giác con người (human visual system)** và trở thành khái niệm cơ sở cho những **mô hình Convolution Neural Networks**.

Trong những năm 1980, Dr. Kunihiko Fukushima dựa trên ý tưởng công trình Simple cell và Complex cell của Hubel và Wiesel, đề xuất mô hình tên là "**neocognition**" trong bài báo "**Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position**”. Mô hình bao gồm hai thuật ngữ quan trọng "S-cells" và "C-cells" định nghĩa toán tử toán tử. S-cells được đặt ở tầng đầu tiên của mô hình và được liên kết với C-cell nằm ở tầng hai của mô hình. Nhờ vào đây, người ta có thể biến nó thành mô hình tính toán cho Nhận dạng mẫu thị giác (Visual Pattern Recognition) với ý tưởng "**simple-to-complex**".

Công trình đầu tiên đặt nền móng cho Convolution Neural Network hiện đai xuất hiện vào những năm 1990, bởi Giáo sư Yann LeCun và đồng nghiệp công bố trong bài báo của họ "**Gradient-Based Learning Applied to Document Recognition**”, và đến nay đã có hơn 38019 lượt citation cho bài báo này. Xuất phát từ ý tưởng của mô hình neocognition, công trình của giáo sư trình bày một mô hình CNN tổng hợp những đặc trưng đơn vào những đặc trưng phức tạp hơn có thể được sử dụng cho nhận dạng chữ viết tay (handwritten character recognition)

Một cách tổng quát, hầu hết các phương pháp dựa trên Neural Networks thường là những phương pháp có giám sát (supervised methods). Không chỉ các bài toán dự đoán hồi quy (regression) hay bài toán phân lớp (classification), nhưng có thể là không giám sát, do đó, tùy vào yêu cầu bài toán, với bài toán phân loại, chúng ta cần dữ liệu huấn luyện được gán nhãn trước, quá trình huấn luyện là giám sát, nhưng với bài toán gom cụ, ví dụ như gom cụm hình ảnh dựa trên độ tương đồng, thì các Neural Network đóng vai trò như bộ rút trích và được kết hợp với một số phương pháp không giám sát như K-means, ...

Với Convolution Neural Networks được sử dụng khá rộng rãi trong hầu hết các bài toán như phân lớp hình ảnh (Image Classification), nhận dạng vật thể (Object Recognition), các bài toán nhận dạng sinh trắc học (Biometric Recognition) như Nhận dạng khôn mặt, Nhận dạng vân tay, Nhận dạng dáng đi, Nhận dạng mẫu mắt, ... ngay cả Nhận dạng giọng nói/ người nói, nó chỉ dùng trong giai đoạn rút trích đặc trưng từ bức ảnh, tổng hợp và chồng chéo các khu vực nhỏ trên bức ảnh.

## Một số bài toán có thể áp dụng CNNs

### Nhận dạng vân tay bằng mạng CNNs
Phát biểu bài toán:

- Đầu vào: Hình ảnh vân tay
- Đầu ra: Lớp của vân tay

Phương pháp:

![](/assets/media_blog_posts/2021-08-09-intro-cnns/finger_recognition.png)

CNNs đóng vai trò như bộ phân lớp, dựa trên mạng học đã được huấn luyện từ trước với rất nhiều tham số như AlexNet, GoogleNet, ResNet.

### Nhận dạng khuôn mặt bằng FaceNet và MTCNN
Phát biểu bài toán:

- Đầu vào: Dữ liệu hình ảnh khuôn mặt
- Đầu ra: Lớp của hình ảnh khuôn mặt

![](/assets/media_blog_posts/2021-08-09-intro-cnns/face-recognition-pipeline.png)

- Face detection: Nhận diện một hay nhiều khuôn mặt trong một bức ảnh
- Feature extraction: Rút trích đặc trưng quan trọng từ một bức ảnh khuôn mặt
- Face classification: Phân lớp khuôn mặt dựa trên những đặc trưng được rút trích

Tham khảo từ: https://arsfutura.com/magazine/face-recognition-with-facenet-and-mtcnn/

Face Recognition Framework bao gồm những thành phần như MTCNN cho face detection, FaceNet cho việc phát sinh face embedding và dùng Softmax như một bộ phân lớp.

Dùng FaceNet để học:

- Chọn ngẫu nhiễn một anchor image
- Chọm ngẫu nhiên một ảnh cùng một người với ảnh anchor
- Chọn ngẫu nhiên một ảnh khác người với ảnh anchor
- Hiệu chỉnh tham số FaceNet để ảnh với ảnh anchor hơn là ảnh khác với anchor

### Nhận dạng giọng nói

Bài toán nhận dạng người nói thường được chia thành hai tác vụ con, gồm: xác minh người nói (speaker verification) và định danh người nói (speaker identification). Xét bài toán con xác minh người nói (speaker verification)

- Đầu vào: dữ liệu âm thanh giọng nói
- Đầu ra: Đồng ý (Accept)/ Từ chối (Deny)

Phương pháp thực hiện:

Trong giai đoạn phát triển (development stage), lời nói của các người nói được sử dụng để tạo ra một mô hình nền cho việc đại diện người nói. Sử dụng kiến trúc DNN như một bộ rút trích đặc trưng người nói mạnh mẽ.

Trong giai đoạn đăng ký (Enrollment stage), một mô hình phân biệt sẽ được tạo cho mỗi định danh người nói. Những lời nói của người nói sẽ được sử dụng để phát sinh mô hình người nói. Trong DNN, lời nói của người nói sẽ là đầu vào của mô hình được tạo ra ở giai đoạn trước đó, và đầu ra được tích hợp với một số phương pháp để cho ra một mô hình người nói.

Trong giai đoạn đánh giá (Evaluation stage), những lời nói kiểm gia sẽ được đưa vào bộ rút trích đại diện người nói, truy vấn kiểm tra mẫu sẽ được so sánh với tất cả mô hình người nói bằng cách sử dụng một hàm tính điểm (score function) nào đó và điểm cao nhất được chọn là người nói được dự đó của mô hình.

CNN đóng vai trò như một bộ rút trích đặc trưng từ dữ liệu đầu vào, là những sóng âm thanh thô, được tinh chỉnh và dùng kỹ thuật cửa sổ (ví dụ hamming windows) trong miền tần số, làm CNN có thể hoạt động tương tự như xử lý với ảnh số.

## Tư tưởng chủ đạo và những thành phần chính của CNNs

Mạng neural Tích Chập (hay được biết là Convolutional Neural Networks - CNNs) được hình thành từ ba ý tưởng chính:

- Tiếp nhận khu vực cục bộ (local receptive fields)
- Chia sẻ trọng số (Shared weights)
- Tổng hợp (Pooling)

Hai tính chất đặc trưng của CNNs:

- Những mẫu (patterns) mà CNNs học là bất biến với phép tịnh tiến
- CNNs có thể học những chiều phân cấp của mẫu

![](/assets/media_blog_posts/2021-08-09-intro-cnns/An-example-of-a-simple-CNN-architecture.png)


**Lớp Convolutional - Convolutional Layer**

Trong Xử lý ảnh số và Video số (Digital Image and Video Processing), một bức ảnh đầu vào được tích chập với một nhân (kernel) để tạo ra một ảnh đầu ra (output image)

- Input Image (Input feature map)
- Output Image (Output feature map)
- Filter (Bộ lọc) gồm ba tham số:
  - Kích thước nhân (kernel) F cho biết phạm vi không gian của kernel
  - Stride S cho biết khoảng cách giữa hai vị trí liên tiếp nhau của nhân (kernel)
  -  Số lượng bộ đệm không (zero padding) P cho biết dố lượng các số không được thêm vào từ vị trí bắt đầu đến vị trí kết thúc của một trục

Ta có thể sử dụng hai toán tử cho việc tính tích chập gồm Convolution Operator và Cross-correlation operator

- Toán tử Convolution được sử dụng nhiều trong Xử lý ảnh số

$$
\begin{equation}
			\text{Output}(x, y) = (K * \text{Input})(x, y) = \sum_m\sum_n\text{Input}(x-m, y-m)K(m,n)
\end{equation}
$$

- Toán tử Cross-correlation được sử dụng trong mạng CNN

$$
\begin{equation}
			\text{Output}(x, y) = (K * \text{Input})(x, y) = \sum_m\sum_n\text{Input}(x+m, y+m)K(m,n)
\end{equation}
$$


Ví dụ:

Ảnh đầu vào (Input image) có kích thước $7 \times 7$

Ảnh đầu ra (Output image) có kích thước $5 \times 5$

Nhân (Kernel) có kích thước $F = 3$, $S = 1$, $P = 0$

![](/assets/media_blog_posts/2021-08-09-intro-cnns/convo.png)

**Lớp tổng hợp - Pooling layer** nhiệm vụ chính của lớp này là sub-sampling các feature map, tác nó thành những feature map nhỏ hơn

![](/assets/media_blog_posts/2021-08-09-intro-cnns/max_pool.png)


**Activation Function (non-linearity)** ánh xạ đầu vào thành đầu ra, được coi là hàm cốt lõi (core function) của tất cả các hàm kích hoạt của tất cả các loại mạng Neural. Một hàm kích hoạt thường gặp như: Sigmoid, Tanh, ReLU, Leaky ReLU, Noisy ReLU, Parametric Linear Units

**Lớp Fully-Connected Layers**

Fully connected layers còn được gọi là affine layers, tạo ra suy luận mức cao (high-level reasoning) trong DNN. Những neuron trong một fully connected layer kết nối đầy đủ với tất cả các kích hoạt trong layer trước đó.

![](/assets/media_blog_posts/2021-08-09-intro-cnns/FullyConnectedLayer.png)

**Loss Function - Hàm mất mát** là những hàm dùng để tính toán độ lỗi trong quá trình huấn luyện, nó tính toán độ lỗi giữa giá trị đúng (actual values) với giá trị dự đoán (predicted values) để tối ưu việc học trong mạng CNN. Một số hàm mất mát thường gặp như: Cross-Entropy hay Softmax Loss Function, Euclidean Loss Function, Hinge Loss Function

## Đánh giá ưu nhược điểm của CNNs

Ưu điểm của mạng nơron tích chập (CNN)

- CNN chia sẻ trọng số đặc trưng, mà làm giảm số lượng tham số huấn luyến có thể có và nó giúp mạng học tăng cường phát sinh và tránh overfitting
- Những tầng rút trích đặc trưng (feature extraction layers) và tầng phân lớp (classifcation layer) học một cách đồng thời vì đầu ra của mô hình vừa được tổ chức cao vừa có độ tin cậy cao vào các tính năng được trích xuất.
- Cài đặt mạng ở mức độ quy mô một cách dễ dàng với CNN hơn những mạng Neural khác.


Nhược điểm:

- Cần nhiều sức mạnh tính toán, ví dụ như sử dụng GPU, TPU hay các máy chủ có cấu hình mạnh
- Hiệu năng phụ thuộc vào dữ liệu đầu vào, liệu nó có sạch hay không, có đủ nhiều hay không, có cân bằng hay không
- Quá nặng, việc nhúng vào các phần cứng bị hạn chế tài nguyên là một thách thức lớn.
