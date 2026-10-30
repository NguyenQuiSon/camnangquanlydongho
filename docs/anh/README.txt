Đặt ảnh thật vào thư mục này, rồi chạy: python build.py
Chạy cho từng bản: python build.py 1 docs | python build.py 1 xem-thu/mau-1 | python build.py 2 xem-thu/mau-2 | python build.py 3 xem-thu/mau-3

Quy ước tên file (đuôi .jpg, .png hoặc .webp):
  <slug-bai>.jpg   -> ảnh bìa 16:9 (nên ~1280x720, dưới 200 KB): hiện đầu mỗi bài. Slug xem trong build.py, cột đầu của mỗi bài.
  Ảnh sản phẩm trong bài (hàm pf() trong build.py): tên file đặt theo tham số đầu của pf().
  Chưa có ảnh thì trang tự hiện ô giữ chỗ "Thêm ảnh: anh/<tên>.jpg"; thêm ảnh rồi chạy lại build là xong.

Ảnh sản phẩm bài đồng hồ nam: ga-2100-1a1, ga-b2100cd-1a4, gm-2100mg-1a, g-shock-mau, casio-mwc-100h-1av,
  orient-ra-ag0017y10b, orient-ra-ar0003l, citizen-nh9130-84l, citizen-nh9138-82a, dong-ho-co, kinh-sapphire.
Ảnh sản phẩm bài đồng hồ nữ (đã có): fossil-scarlette-mini-es4897, dw-petite-rosewater, dw-classic-sheffield-dw00100145,
  dw-classic-petite, skagen-skw2722, orient-bambino-ra-ag0003s30b, citizen-ew5593-64d,
  calvin-klein-confidence-bangle-25200023, julius-day-ngoc-trai, g-shock-gma-s2100, baby-g-ba-130-7a1dr,
  timex-expedition, casio-lq-142e-2adf, dw-quadro-dw00100748, casio-ltp-v007l-9budf.
Ảnh sản phẩm bài đồng hồ nữ: đã đủ, gồm cả fossil-scarlette-es4318.
citizen-eco-drive-fe6170-88d.webp: có sẵn, chưa dùng trong bài nào.
Bài mục III, IV (bảo quản, vệ sinh dây, chống nước, bảo dưỡng) chỉ dùng ảnh bìa, không có ảnh sản phẩm.
Ảnh bìa (10 bài, đã đủ): cach-chon-dong-ho-nam, dong-ho-co-hay-dong-ho-pin, size-dong-ho-nam-theo-co-tay, cach-chon-dong-ho-nu,
  dong-ho-nu-day-da-hay-day-kim-loai, chon-dong-ho-lam-qua-tang, cach-bao-quan-dong-ho, cach-ve-sinh-day-dong-ho,
  chi-so-chong-nuoc-atm, bao-lau-nen-bao-duong-dong-ho (.jpg 1280x720).
Alt ảnh bìa lấy từ tiêu đề bài; alt ảnh sản phẩm viết trong lời gọi pf() ở build.py.
