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

- Không cần kỹ thuật đặc trưng (feature engineering)
- Khả năng thích ứng và chuyển tiếp

Tuy nhiên, ta cũng không nên coi nhẹ các phương pháp học máy cổ điển, bởi vì chúng vẫn đứng một vai trò trụ cột trong lĩnh vực nghiên cứu và ứng dụng máy học. So với học sâu, ta vẫn có thể tận dụng ưu thế của những phương pháp này:
- Xử lý những dữ liệu có kích thước nhỏ
- Tính toán với chi phí thấp và hoạt động hiệu quả trong điều kiện thiếu thốn tài nguyên vật lý
- Dễ dàng kết hợp vào các mô hình học sâu để tăng cường hiệu suất tính toán, thời gian thực hiện và độ chính xác.


## Artificial Neural Networks


## Mô hình ANN đơn giản nhất - Perceptron


## Go deeper - Multilayer Perceptron (MLP)


## Gradient-Based Learning


## Back-Propagation Learning


## Kết luận
  