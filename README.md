
## Hệ thống hỏi đáp - QA System
### Đồ án Khoa học dữ liệu - DS445
#### I. Thành viên
1. Trần Quang Thìn (nhóm trưởng)
2. Trương Văn Thành
3. Lê Văn Hiếu
4. Trần Huy Hoàng
5. Huỳnh Ngọc Vinh

#### II. Hướng dẫn cài đặt


# answerbiosa
Sau khi tải về và giải nén file qa-server.zip thì mình sẽ dùng vscode mở thư mục qablog.
Sau đó gõ:
- python manage.py makemigrations
- python manage.py migrate
Sau khi hoàn tất mình có thể dùng:
- python manage.py runserver để chạy.

Đối với server api, thì cần phải cài các gói sau: 
- pip install transformers
- pip install googletrans==4.0.0rc1
- torch
- !pip install google-search-results
- bottle
- pip install bottle-cors-plugin

