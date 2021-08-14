---
layout: single
permalink: /content/msa/classification/classification
title: "[MSA] Phân lớp - Phần 1"
author_profile: true
toc: true
comments: True
---

## 1) Động lực nghiên cứu khoa học

Trong quá trình hoạt động, con người tạo ra rất nhiều tập dữ liệu nghiệp vụ. Các tập dữ liệu được tích lũy có kích thước ngày càng lớn, và có thể chứa nhiều thông tin ẩn cùng những quy luật chưa được khám phá. Chính vì vậy, một nhu cầu đặt ra là cần tìm cách phân lớp dữ liệu để tìm được sự khác biệt dữ liệu từ đó đưa ra dự đoán chính xác về sự đặc trưng của dữ liệu.

Từ đó các thuật toán phân lớp dữ liệu được ra đời để đáp ứng mong muốn đó. Trong những năm qua, phân lớp dữ liệu đã thu hút sự quan tâm các nhà nghiên cứu trong nhiều lĩnh vực khác nhau như học máy (machine learning), thống kê (statistics)... Công nghệ này cũng ứng dụng trong nhiều lĩnh vực thực tế như: thương mại, nhà băng, maketing, nghiên cứu thị trường, bảo hiểm, y tế, giáo dục...

**Phân tách (Discriminant)** tìm những cách tối ưu để tách các quần thể khác nhau.

**Phân lớp (Classification)** là quá trình phân lớp một đối tượng dữ liệu vào một hay nhiều lớp đã cho trước nhờ một mô hình phân lớp (model). Mô hình này được xây dựng dựa trên một tập dữ liệu được xây dựng trước đó có gán nhãn (hay còn gọi là tập huấn luyện). Quá trình phân lớp là quá trình gán nhãn cho đối tượng dữ liệu.

Để sắp xếp các đối tượng (observation) vào 2 hay nhiều lớp đã được dán nhãn. Trọng tâm của vấn đề này là tạo ra một phương pháp tối ưu để dán nhãn đối tượng cho các lớp đã được dán nhãn

Ví dụ:

- Loan classification
- Hệ thống cảnh báo (Warning systems/ Alert systems)
- Chuẩn đoán y khoa
- Phân lớp những ngôi sao

![](/contents/msa/classification/star_classification.png)

## 2) Phát biểu bài toán

**Đầu vào bài toán (Input)**: Tập dữ liệu huấn luyện đã được đánh nhãn (label), một quan sát mới chưa có nhãn.

**Đầu vào bài toán (Output)**: Mô hình (models), bộ phân lớp (classifiers) mà phân tách dữ liệu thành các nhóm/ lớp đã biết, phản hồi lại những quan sát mới vào (đánh nhãn cho những quan sát mới này)
