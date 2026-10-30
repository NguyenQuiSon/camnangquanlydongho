# -*- coding: utf-8 -*-
# Chạy: python build.py  -> tạo docs/index.html (trang đơn). Sửa nội dung ở danh sách C bên dưới.
import os, shutil, html
e = html.escape
BASE = "https://nguyenquison.github.io/camnangquanlydongho/"
TODO = '<p class="todo">✦ Bổ sung nội dung chi tiết của bài này tại đây (đoạn văn, danh sách, bảng...).</p>'

# ---------- Hàm hỗ trợ viết bài ----------
def find(n):
    for x in ("jpg","jpeg","png","webp"):
        if os.path.exists(f"anh/{n}.{x}"): return f"anh/{n}.{x}"
    return None
def pf(name, title, note="", price="", alt=""):
    """Thẻ ảnh sản phẩm. Chưa có ảnh anh/<name>.jpg|png|webp thì hiện ô giữ chỗ để bổ sung sau."""
    p = find(name)
    im = f'<img src="{p}" alt="{e(alt or title)}" loading="lazy">' if p else f'<span class="phx">Thêm ảnh: anh/{name}.jpg</span>'
    pr = f'<span class="pr">{e(price)}</span>' if price else ""
    return f'<figure class="pf"><div class="pi">{im}</div><figcaption><b>{e(title)}</b>{e(note)}{pr}</figcaption></figure>'
def gal(*a): return '<div class="gal">' + "".join(a) + '</div>'
def tbl(head, rows):
    h = "".join(f"<th>{e(x)}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in row) + "</tr>" for row in rows)
    return f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'
def src(items):
    li = "".join(f'<li><a href="{u}" target="_blank" rel="noopener nofollow">{e(t)}</a></li>' for t, u in items)
    return f'<div class="src"><h5>Nguồn tham khảo</h5><ul>{li}</ul></div>'

# ---------- Nội dung 3 bài chọn đồng hồ nam ----------
B1 = "".join([
'<p>Chọn đồng hồ nam không nên bắt đầu từ kiểu dáng. Hãy trả lời ba câu hỏi trước: bạn đeo nó khi nào, cổ tay bạn cỡ nào và bạn sẵn sàng chi bao nhiêu. Sau ba câu trả lời đó, danh sách mẫu phù hợp sẽ thu hẹp rất nhanh.</p>',
'<h4>Bước 1: Xác định nhu cầu và phong cách</h4>',
'<p>Mỗi chiếc đồng hồ phục vụ một nhu cầu khác nhau: có chiếc sinh ra để đi làm, có chiếc dành cho vận động, có chiếc chủ yếu để thể hiện gu. Hãy xác định bạn sẽ đeo nó nhiều nhất ở đâu:</p>',
'<ul><li><b>Công sở, gặp khách:</b> mặt tròn gọn, màu trung tính. Dây da cho cảm giác lịch sự, dây kim loại cho cảm giác mạnh mẽ, nam tính.</li>',
'<li><b>Thể thao, hoạt động ngoài trời:</b> ưu tiên độ bền, chịu va đập và chống nước.</li>',
'<li><b>Hằng ngày, thể hiện cá tính:</b> chọn theo gu, nhưng vẫn phải vừa cổ tay (xem bước 2).</li></ul>',
'<p>Nếu bạn thích vẻ ngoài bụi bặm, cá tính mạnh mẽ, dòng G-Shock của Casio là lựa chọn quen thuộc. Ba mẫu thường được nhắc đến là GA-2100-1A1, GA-B2100CD-1A4 và GM-2100MG-1A:</p>',
gal(
 pf("g-shock-mau","Mẫu G-Shock","Hình minh họa phong cách G-Shock",alt="Đồng hồ Casio G-Shock mặt vàng, dây nhựa đen"),
 pf("ga-2100-1a1","GA-2100-1A1","Vỏ bát giác, toàn thân màu đen",alt="Đồng hồ Casio G-Shock GA-2100-1A1 màu đen"),
 pf("ga-b2100cd-1a4","GA-B2100CD-1A4","Phối đen đỏ, mặt số có Tough Solar và Bluetooth",alt="Đồng hồ Casio G-Shock GA-B2100CD-1A4 phối đen đỏ"),
 pf("gm-2100mg-1a","GM-2100MG-1A","Viền kim loại màu vàng, dây nhựa đen",alt="Đồng hồ Casio G-Shock GM-2100MG-1A viền kim loại vàng")),
'<h4>Bước 2: Chọn size mặt theo cổ tay</h4>',
'<p>Nam giới thường có cổ tay lớn hơn nữ, nên mặt đồng hồ nam phổ biến ở khoảng 38–42 mm. Một số mốc để bạn hình dung:</p>',
'<ul><li><b>Cổ tay nhỏ</b> (chu vi dưới 16 cm): mặt khoảng 36–38 mm.</li><li><b>Cổ tay trung bình:</b> mặt khoảng 38–42 mm.</li><li><b>Cổ tay lớn:</b> mặt 42–44 mm, có thể lên tới 45 mm.</li></ul>',
'<p>Cách đo: dùng thước dây mềm quấn một vòng quanh cổ tay, ngay dưới xương cổ tay, không siết quá chặt cũng không để quá lỏng, rồi đọc số đo theo cm. Nếu mua trực tiếp, hãy đeo thử xem mặt có quá to hay quá nhỏ. Nếu mua làm quà, hãy hỏi trước hoặc ước chừng cổ tay người nhận. Bảng quy đổi chi tiết nằm ở bài <a href="#size-dong-ho-nam-theo-co-tay">Size mặt đồng hồ nam bao nhiêu mm là vừa cổ tay</a>.</p>',
'<h4>Bước 3: Chất liệu, dây đeo và màu sắc</h4>',
'<ul><li><b>Vỏ:</b> thép không gỉ (Stainless Steel) là chất liệu phổ biến nhất vì bền và chi phí sản xuất thấp. Vỏ carbon, gốm, nhôm hay titanium thường chỉ xuất hiện ở dòng cao cấp.</li>',
'<li><b>Dây:</b> dây inox bền, không bị oxy hóa hay gỉ. Dây kim loại còn có thể tháo bớt mắt xích để vừa cổ tay. Dây da mềm và lịch sự hơn nhưng cần giữ khô.</li>',
'<li><b>Màu sắc:</b> nam giới thường thích các tông tối, trầm. Một số người chọn màu theo phong thủy, ngũ hành.</li></ul>',
'<h4>Bước 4: Chọn theo ngân sách</h4>',
'<p>Đặt ngân sách trước giúp bạn lọc nhanh những mẫu đáng xem. Chiếc đồng hồ đẹp nhất là chiếc vừa với phong cách sống và điều kiện kinh tế của người đeo. Các mốc dưới đây chỉ mang tính tham khảo.</p>',
'<h5>Khoảng 1 triệu đồng: phổ thông, dễ sử dụng</h5>',
'<p>Nhóm này dành cho người cần một chiếc đồng hồ đúng nghĩa để xem giờ hằng ngày mà không muốn tốn nhiều chi phí. Một ví dụ dáng thể thao là CASIO MWC-100H-1AV. Mặt số ghi WR 100M, tức chống nước 100 m (tương đương 10 ATM). Cách hiểu chỉ số này nằm ở bài <a href="#chi-so-chong-nuoc-atm">Chỉ số chống nước 3 ATM, 5 ATM, 10 ATM nghĩa là gì</a>.</p>',
gal(pf("casio-mwc-100h-1av","CASIO MWC-100H-1AV","Dáng thể thao, chống nước 100 m",price="Từ khoảng 1 triệu đồng",alt="Đồng hồ Casio MWC-100H-1AV dáng thể thao, dây nhựa đen")),
'<h5>Tầm giá kế tiếp: chất liệu và tính năng tốt hơn</h5>',
'<p>Khi nâng ngân sách, sản phẩm được đầu tư nhiều hơn về chất liệu (thép không gỉ 16L, dây da thật) và tính năng (bấm giờ thể thao Chronograph, chống nước 5–10 ATM). Chiếc đồng hồ không chỉ đẹp mà còn chịu được tác động bên ngoài tốt hơn khi dùng lâu dài.</p>',
'<h5>Từ 3 đến 5 triệu đồng: bước đệm sang đồng hồ cơ và kính Sapphire</h5>',
'<p>Ở mức giá này bạn bắt đầu chạm tới hai thứ tạo nên khác biệt: bộ máy cơ (Automatic) cơ bản và mặt kính Sapphire, loại kính cứng, khó trầy hơn kính thông thường. Hai loại đồng hồ cơ và đồng hồ pin khác nhau thế nào được so sánh ở bài <a href="#dong-ho-co-hay-dong-ho-pin">Đồng hồ cơ hay đồng hồ pin: nên chọn loại nào</a>.</p>',
gal(
 pf("dong-ho-co","Đồng hồ cơ","Có ô lộ một phần bộ máy ở mặt số",alt="Đồng hồ cơ Orient Automatic mặt trắng lộ bộ máy, dây da nâu"),
 pf("kinh-sapphire","Kính Sapphire","Mặt kính cứng, khó trầy",alt="Đồng hồ dây lưới kim loại dùng mặt kính Sapphire trên cổ tay")),
'<h5>Từ 5 đến 10 triệu đồng: Automatic của Orient và Citizen</h5>',
'<p>Phân khúc này là nơi đồng hồ Automatic của Orient và Citizen lên ngôi, thường đi kèm kính Sapphire và bộ máy cơ tinh giản. Giá bên dưới là mức tham khảo, có thể thay đổi theo đại lý và thời điểm.</p>',
'<p><b>Một số ví dụ của Orient</b></p>',
gal(
 pf("orient-ra-ag0017y10b","Orient RA-AG0017Y10B","Automatic",price="Từ khoảng 6,9 triệu đồng",alt="Đồng hồ Orient RA-AG0017Y10B Automatic"),
 pf("orient-ra-ar0003l","Đồng hồ nam Orient Automatic Small Second Blue RA-AR0003L","Mặt xanh, kim giây nhỏ",price="Từ khoảng 7,3 triệu đồng",alt="Đồng hồ nam Orient Automatic Small Second Blue RA-AR0003L mặt xanh")),
'<p><b>Một số ví dụ của Citizen</b></p>',
gal(
 pf("citizen-nh9138-82a","Đồng hồ nam Citizen Automatic Mechanical NH9138-82A","Automatic",price="Từ khoảng 7 triệu đồng",alt="Đồng hồ nam Citizen Automatic Mechanical NH9138-82A"),
 pf("citizen-nh9130-84l","Đồng hồ nam Citizen Automatic Open Heart NH9130-84L","Mặt xanh, lộ bộ máy (Open Heart)",price="Từ khoảng 7,2 triệu đồng",alt="Đồng hồ nam Citizen Automatic Open Heart NH9130-84L mặt xanh dây thép")),
'<h5>Cao cấp: từ hàng chục triệu đồng</h5>',
'<p>Trên mức này là các mẫu chế tác cao cấp, giá từ hàng chục triệu đồng trở lên. Chỉ nên cân nhắc khi bạn đã rõ mình cần gì ở chiếc đồng hồ.</p>',
'<div class="note">Đồng hồ đắt tiền chưa chắc phù hợp nếu không đáp ứng đúng nhu cầu sử dụng. Đặt ngân sách hợp lý giúp bạn tránh lãng phí mà vẫn có sản phẩm ưng ý.</div>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>Xác định nơi đeo nhiều nhất: công sở, thể thao hay hằng ngày.</li><li>Đo cổ tay rồi chọn mặt khoảng 38–42 mm (cổ tay nhỏ 36–38 mm, cổ tay lớn đến 44–45 mm).</li><li>Chọn vỏ, dây và màu hợp gu; dây kim loại có thể chỉnh mắt xích.</li><li>Đặt ngân sách trước, rồi đeo thử trước khi mua nếu có thể.</li></ul>',
src([
 ("Thế Giới Di Động: Nên chọn đồng hồ như thế nào","https://www.thegioididong.com/tin-tuc/nen-chon-dong-ho-nhu-the-nao-1561356"),
 ("Thế Giới Di Động: Thông tin ngành hàng đồng hồ, chọn theo giới tính và cổ tay","https://www.thegioididong.com/dong-ho-deo-tay-skagen"),
 ("Thế Giới Di Động: Thông tin ngành hàng đồng hồ, chọn theo ngân sách","https://www.thegioididong.com/dong-ho-deo-tay-michael-kors"),
 ("Thế Giới Di Động: Đồng hồ thời trang từ 3 đến 5 triệu","https://www.thegioididong.com/lac-bang-vang"),
 ("CellphoneS: Cách chọn đồng hồ cho cổ tay nhỏ","https://cellphones.com.vn/sforum/dong-ho-cho-co-tay-nho"),
 ("Quantrimang: Bí quyết chọn mua đồng hồ cơ","https://quantrimang.com/bi-quyet-vang-de-chon-mua-dong-ho-co-136367")])])

B2 = "".join([
'<p>Trên thị trường hiện có hai loại đồng hồ chính: đồng hồ pin (Quartz) và đồng hồ cơ. Mỗi loại có bộ máy và cách hoạt động riêng, nên trải nghiệm đeo hằng ngày cũng khác nhau. Câu trả lời đúng không phải là loại nào “tốt hơn”, mà là loại nào hợp với cách bạn sống.</p>',
'<h4>So sánh nhanh</h4>',
tbl(["Tiêu chí","Đồng hồ pin (Quartz)","Đồng hồ cơ"],[
 ["Nguồn năng lượng","Pin. Pin cấp điện để tinh thể thạch anh dao động.","Dây cót, không cần pin."],
 ["Độ chính xác","Cao hơn.","Thấp hơn. Cần lên cót lại nếu không đeo khoảng 40–80 giờ."],
 ["Chăm sóc","Thay pin định kỳ, thường sau vài năm.","Bảo dưỡng định kỳ để giữ độ chính xác và tuổi thọ."],
 ["Chịu va đập","Chịu lực tốt hơn theo một số nguồn.","Bộ máy cơ khí tinh vi nên cần nhẹ tay hơn."],
 ["Sửa chữa","Khi hỏng thường phải thay pin hoặc IC, có thể tốn kém.","Thường dễ sửa hơn khi hỏng hoặc va đập mạnh."],
 ["Thẩm mỹ","Kiểu dáng đa dạng.","Có kiểu lộ cơ, hở tim, siêu mỏng, Tourbillon. Vận hành êm, tiếng tích tắc rất nhỏ."],
 ["Hợp với","Người cần chính xác, ít chăm sóc, vận động nhiều.","Người thích cơ khí, thẩm mỹ và chấp nhận bảo dưỡng."]]),
'<p class="small">Đây là xu hướng chung. Từng mẫu cụ thể có thể khác, nên hãy xem thông số của nhà sản xuất.</p>',
'<h4>Đồng hồ pin (Quartz, thạch anh)</h4>',
'<p>Đồng hồ pin dùng bộ dao động điện tử. Pin tạo điện trường làm tinh thể thạch anh dao động, nhờ đó đồng hồ đo thời gian ổn định. Pin thường dùng được vài năm mới phải thay.</p>',
'<h5>Ưu điểm</h5>',
'<ul><li>Chạy chính xác hơn đồng hồ cơ.</li><li>Ít phải chăm sóc, không cần lên cót.</li><li>Theo một số nguồn, chịu va đập tốt hơn đồng hồ cơ.</li></ul>',
'<h5>Nhược điểm</h5>',
'<ul><li>Phải thay pin định kỳ, nếu không đồng hồ sẽ ngừng chạy.</li><li>Khi hỏng, thường phải thay pin hoặc IC, chi phí có thể cao.</li></ul>',
'<h5>Lưu ý về pin</h5>',
'<ul><li>Tuổi thọ pin tính từ lúc nhà sản xuất lắp pin, không phải lúc bạn mua. Vì vậy có đồng hồ mới đeo 6–7 tháng đã hết pin. Nếu còn bảo hành, bạn được thay pin miễn phí.</li><li>Khi tự mua pin, hãy chọn đúng hình dạng và kích thước (có pin dẹt lớn như đồng xu, có pin nhỏ như nút áo).</li><li>Nên dùng pin oxit bạc hoặc lithium của hãng uy tín như Renata hoặc Varta để đảm bảo tuổi thọ cho máy.</li></ul>',
'<h4>Đồng hồ cơ</h4>',
'<p>Đồng hồ cơ không dùng pin hay linh kiện điện tử. Năng lượng đến từ dây cót, truyền qua hàng trăm chi tiết kim loại nhỏ lắp ráp tỉ mỉ. Loại lên cót bằng tay cần bạn vặn núm. Loại Automatic (tự động) tự lên cót nhờ chuyển động của cổ tay khi đeo.</p>',
'<h5>Ưu điểm</h5>',
'<ul><li>Không phải thay pin, thân thiện với môi trường.</li><li>Kiểu dáng đa dạng: lộ cơ, hở tim, siêu mỏng, Tourbillon.</li><li>Thẩm mỹ cao, 5–10 năm sau vẫn không lỗi thời.</li><li>Vận hành êm, tiếng tích tắc rất nhỏ.</li><li>Thường dễ sửa hơn khi hỏng hoặc va đập mạnh.</li></ul>',
'<h5>Nhược điểm</h5>',
'<ul><li>Kém chính xác hơn đồng hồ pin.</li><li>Cần lên cót lại nếu để khoảng 40–80 giờ không đeo.</li><li>Cần bảo dưỡng định kỳ để giữ độ chính xác và tuổi thọ.</li></ul>',
'<h4>Còn đồng hồ năng lượng ánh sáng?</h4>',
'<p>Ngoài hai loại trên còn có đồng hồ chạy bằng ánh sáng (solar) hoặc bằng chuyển động (kinetic). Ví dụ Citizen có công nghệ Eco-Drive tiết kiệm năng lượng, thường giảm nhu cầu thay pin. Nếu bạn ngại thay pin nhưng vẫn muốn độ chính xác của máy điện tử, đây là hướng đáng xem.</p>',
'<h4>Nên chọn loại nào?</h4>',
'<ul><li><b>Chọn đồng hồ pin</b> nếu bạn cần độ chính xác, muốn ít chăm sóc và hay vận động mạnh.</li><li><b>Chọn đồng hồ cơ</b> nếu bạn thích cơ khí, đề cao thẩm mỹ và chấp nhận bảo dưỡng định kỳ.</li><li><b>Chọn cả hai</b> nếu có điều kiện: một chiếc pin đeo hằng ngày, một chiếc cơ cho dịp quan trọng.</li></ul>',
'<p>Về ngân sách, đồng hồ cơ Automatic của Orient và Citizen thường nằm ở khoảng 5–10 triệu đồng. Xem ví dụ cụ thể ở bài <a href="#cach-chon-dong-ho-nam">Cách chọn đồng hồ nam theo cổ tay và ngân sách</a>.</p>',
src([
 ("Điện máy XANH: Nên chọn đồng hồ cơ hay pin, ưu nhược điểm của mỗi loại","https://www.dienmayxanh.com/kinh-nghiem-hay/nen-chon-dong-ho-co-hay-pin-uu-nhuoc-diem-cua-moi-1178715"),
 ("FPT Shop: Phân biệt đồng hồ pin và đồng hồ cơ","https://fptshop.com.vn/tin-tuc/thu-thuat/phan-biet-dong-ho-pin-va-dong-ho-co-dau-la-su-khac-biet-co-ban-103404"),
 ("Thế Giới Di Động: Đồng hồ cơ tự động (Automatic) là gì","https://www.thegioididong.com/hoi-dap/dong-ho-co-tu-dong-automatic-la-gi-1167202"),
 ("Thế Giới Di Động: Nên chọn đồng hồ cơ hay đồng hồ điện tử","https://www.thegioididong.com/tin-tuc/theo-ban-chung-ta-nen-chon-dong-ho-co-hay-dong-ho-dien-tu-1244955"),
 ("Hoàng Hà Mobile: Đồng hồ cơ là gì","https://hoanghamobile.com/tin-tuc/dong-ho-co-la-gi/"),
 ("Meta.vn: Tiêu chí khi chọn mua đồng hồ đeo tay","https://meta.vn/hotro/nhung-tieu-chi-anh-em-can-luu-y-khi-chon-mua-dong-ho-deo-tay-3600"),
 ("FPT Shop: Nên chọn loại pin nào để thay cho đồng hồ đeo tay","https://fptshop.com.vn/tin-tuc/dong-ho/nen-chon-loai-pin-nao-de-thay-cho-dong-ho-deo-tay-133538")])])

B3 = "".join([
'<p>Size đồng hồ nam là đường kính mặt đồng hồ, tính bằng mm. Chọn đúng size quyết định chiếc đồng hồ trông cân đối hay cồng kềnh. Chỉ cần ba bước: đo cổ tay, tra bảng, rồi kiểm thêm vài yếu tố phụ như kiểu mặt và độ dày.</p>',
'<h4>Bước 1: Đo cổ tay</h4>',
'<ul><li>Dùng thước dây mềm, quấn một vòng quanh cổ tay ở vị trí bạn hay đeo đồng hồ, ngay dưới xương cổ tay.</li><li>Thước vừa khít, không siết quá chặt và không để lỏng.</li><li>Đọc và ghi lại số đo theo cm.</li></ul>',
'<h4>Bước 2: Tra bảng size đồng hồ nam</h4>',
tbl(["Chu vi cổ tay nam","Size mặt gợi ý","Khoảng an toàn","Nhận xét nhanh"],[
 ["Dưới 15 cm","36–38 mm","35–39 mm","Hợp mặt gọn, thanh lịch"],
 ["15–16 cm","38–40 mm","37–41 mm","Dễ đeo nhất với đồng hồ công sở, đồng hồ thường ngày"],
 ["16–17 cm","40–42 mm","39–42 mm","Nhóm phổ biến nhất của nam giới Việt Nam"],
 ["17–18 cm","41–43 mm","40–44 mm","Hợp nhiều kiểu, từ công sở đến thể thao"],
 ["Trên 18 cm","42–44 mm trở lên","41–46 mm","Nên kiểm thêm độ dày và lug-to-lug"]]),
'<p class="small">Bảng là mốc tham khảo phổ biến, không phải công thức cứng cho mọi mẫu.</p>',
'<h5>Công thức nhanh</h5>',
'<p>Lấy chu vi cổ tay (mm) chia cho 4,5. Ví dụ cổ tay 18 cm = 180 mm, chia 4,5 được khoảng 40 mm. Công thức này cho kết quả thiên về mặt gọn. Nếu lệch với bảng, hãy chọn khoảng ở giữa rồi đeo thử.</p>',
'<h4>Các nhóm size theo tiêu chuẩn quốc tế</h4>',
'<ul><li><b>Midsize (nam và nữ đều đeo được):</b> 34–36 mm.</li><li><b>Men’s Regular (size phổ thông của nam):</b> 37–39 mm.</li><li><b>Men’s Sport (size thể thao):</b> 40–42 mm.</li><li><b>Men’s XL (size rất lớn):</b> khoảng 45 mm.</li></ul>',
'<p>Đồng hồ nam trên thị trường thường có size từ 34 đến 50 mm. Nam giới châu Á thường có cổ tay nhỏ hơn, nên nhiều người hợp với size 36–40 mm hơn là các mẫu quá lớn.</p>',
'<h4>Một số số đo cổ tay hay gặp</h4>',
'<ul><li><b>Cổ tay 16 cm:</b> khoảng 38–40 mm là vùng an toàn. Một số nguồn cho phép tới 42 mm.</li><li><b>Cổ tay 17 cm:</b> khoảng 40–42 mm theo bảng trên, có thể lên 43 mm nếu thích mặt lớn.</li><li><b>Cổ tay 18 cm:</b> khoảng 41–43 mm. Nhiều bài tư vấn gợi ý các mẫu mặt 42–43 mm cho số đo này.</li></ul>',
'<h4>Cổ tay nhỏ nên chú ý gì</h4>',
'<p>Nam có chu vi cổ tay dưới 16 cm được xếp vào nhóm cổ tay nhỏ. Mặt quá lớn sẽ phủ kín cổ tay và làm tổng thể mất cân đối.</p>',
'<ul><li>Chọn mặt 36–38 mm; với cổ tay 15–17 cm có thể chọn 36–40 mm và độ dày từ 12 mm trở xuống.</li><li>Ưu tiên đồng hồ nhẹ, ôm tay, không quá dày.</li><li>Dây da hoặc dây NATO bản mỏng 16–18 mm hợp hơn dây kim loại nhiều mắt xích cứng. Nên chọn dây có nhiều nấc chỉnh để không bị xoay vòng.</li><li>Tránh mẫu mạ vàng nhiều, vì màu vàng đậm có thể làm tay trông nhỏ hơn.</li></ul>',
'<h4>Những yếu tố làm đồng hồ trông to hoặc nhỏ hơn size thực</h4>',
'<ul><li><b>Độ dày vỏ:</b> nên dưới 12 mm để đeo thoải mái và dễ luồn tay áo.</li><li><b>Kiểu mặt:</b> mặt tròn là lựa chọn dễ hợp nhất.</li><li><b>Lug-to-lug:</b> khoảng cách từ đầu chấu dây này đến đầu chấu dây kia. Nếu dài hơn bề ngang cổ tay, đồng hồ sẽ chìa ra ngoài dù đường kính mặt hợp lý.</li><li><b>Màu vỏ và dây:</b> màu tối thường trông gọn hơn, màu sáng hoặc mạ vàng trông nổi hơn.</li></ul>',
'<div class="note">Con số trong bảng chỉ giúp thu hẹp lựa chọn. Cảm nhận thực tế khi đeo mới là tiêu chí cuối cùng.</div>',
src([
 ("Thế Giới Di Động: Bảng size đồng hồ nam chuẩn, cách chọn size","https://www.thegioididong.com/hoi-dap/bang-size-dong-ho-nam-chuan-cach-chon-size-1595677"),
 ("Thế Giới Di Động: Đồng hồ nam tay nhỏ","https://www.thegioididong.com/hoi-dap/top-20-mau-dong-ho-nam-tay-nho-sang-trong-lich-lam-1453362"),
 ("Thế Giới Di Động: Cổ tay 16 cm đeo đồng hồ size bao nhiêu","https://www.thegioididong.com/hoi-dap/co-tay-16cm-deo-dong-ho-size-bao-nhieu-top-10-1468312"),
 ("Thế Giới Di Động: Cổ tay 18 cm đeo đồng hồ size bao nhiêu","https://www.thegioididong.com/hoi-dap/co-tay-18cm-deo-dong-ho-size-bao-nhieu-top-mau-1535676"),
 ("Điện máy XANH: Cách đo size đồng hồ để chọn mua chuẩn nhất","https://www.dienmayxanh.com/kinh-nghiem-hay/cach-do-size-dong-ho-de-chon-mua-chuan-nhat-1179133"),
 ("CellphoneS: Cách chọn đồng hồ cho cổ tay nhỏ","https://cellphones.com.vn/sforum/dong-ho-cho-co-tay-nho"),
 ("Chiaki: Đồng hồ cho nam cổ tay nhỏ","https://chiaki.vn/tin-tuc/dong-ho-cho-nam-co-tay-nho"),
 ("Mytour: Top 22 mẫu đồng hồ nam cho cổ tay nhỏ","https://mytour.vn/vi/blog/bai-viet/top-22-mau-dong-ho-nam-cho-co-tay-nho-dang-so-huu-nhat-2024.html")])])

# ---------- Nội dung 3 bài chọn đồng hồ nữ ----------
B4 = "".join([
'<p>Chọn đồng hồ nữ không nên bắt đầu từ màu sắc hay thương hiệu. Hãy trả lời ba câu hỏi trước: cổ tay bạn cỡ nào, kiểu mặt nào cân đối với cổ tay đó và màu dây nào hợp với màu da. Sau ba câu trả lời đó, danh sách mẫu phù hợp sẽ thu hẹp rất nhanh.</p>',
'<h4>Bước 1: Đo cổ tay và chọn size mặt</h4>',
'<p>Dùng thước dây mềm quấn một vòng quanh cổ tay ở vị trí bạn hay đeo đồng hồ, không siết quá chặt cũng không để lỏng, rồi ghi số đo theo cm. Cổ tay nữ thường nằm trong khoảng 12–17 cm. Các nguồn tư vấn đưa ra mốc hơi khác nhau, nên bảng dưới đây chỉ giúp thu hẹp lựa chọn:</p>',
tbl(["Trường hợp","Size mặt gợi ý","Nhận xét nhanh"],[
 ["Cổ tay nhỏ, khoảng 12–14 cm","22–28 mm","Mặt gọn, dây mảnh để đồng hồ không át cổ tay"],
 ["Chưa biết số đo (ví dụ mua làm quà)","29–34 mm","Vùng an toàn cho phần lớn cổ tay nữ"],
 ["Cổ tay to, khoảng 15–16 cm trở lên","36–40 mm với mặt tròn; một số nguồn cho phép đến 42 mm","Mặt oval hoặc tonneau giúp cổ tay trông thon hơn"]]),
'<p class="small">Bảng là mốc tham khảo tổng hợp từ nhiều nguồn, không phải công thức cứng cho mọi mẫu.</p>',
'<h5>Công thức tham khảo</h5>',
'<p>Một nguồn tư vấn gợi ý lấy chu vi cổ tay (mm) chia 4 để ra cỡ mặt lý tưởng và chia 5 để ra cỡ tối thiểu. Ví dụ cổ tay 15 cm = 150 mm cho khoảng 30 đến 37,5 mm. Khoảng này khá rộng, nên hãy đối chiếu với bảng trên rồi đeo thử.</p>',
'<h4>Bước 2: Chọn kiểu mặt và dây theo hình dáng cổ tay</h4>',
'<ul><li><b>Mặt tròn:</b> kiểu phổ biến nhất. Một nguồn ước tính kiểu này chiếm khoảng 80% đồng hồ nữ. Góc bo mềm mại nên dễ đeo và hợp người thích vẻ nhẹ nhàng.</li>',
'<li><b>Mặt vuông, chữ nhật:</b> xuất hiện từ năm 1917 khi Cartier ra mẫu Tank. Cùng đường kính, mặt vuông trông nhỏ gọn và thanh mảnh hơn mặt tròn. Các đường thẳng còn tôn cổ tay nhỏ, thon dài.</li>',
'<li><b>Mặt oval:</b> thường được làm như một món trang sức đeo tay, hay kết hợp với đá quý, vàng hoặc bạc.</li>',
'<li><b>Mặt tonneau (dáng thùng):</b> hình chữ nhật bo tròn góc, nổi bật và mang hơi hướng nghệ thuật. Franck Muller nổi tiếng với dòng này.</li></ul>',
'<p>Về dây và dáng cổ tay:</p>',
'<ul><li><b>Cổ tay nhỏ, tròn:</b> chọn dây da bản mảnh hoặc dây kim loại mắt nhỏ.</li><li><b>Cổ tay xương to, lộ xương:</b> mặt vuông kết hợp dây da mềm cho cảm giác thanh thoát.</li><li><b>Cổ tay ngang to:</b> chọn mặt lớn hơn với dây da hoặc dây kim loại bản to.</li></ul>',
'<p>Dù chọn kiểu nào, điều quan trọng nhất vẫn là tỷ lệ giữa đồng hồ và cổ tay, chứ không hẳn là hình dáng mặt. Ví dụ cho cổ tay nhỏ là Fossil Scarlette Mini ES4897, bản thu nhỏ của dòng Scarlette cổ điển:</p>',
gal(pf("fossil-scarlette-mini-es4897","Đồng hồ Fossil Scarlette Mini ES4897","Bản thu nhỏ của dòng Scarlette, dành cho cổ tay nhỏ",alt="Đồng hồ Fossil Scarlette Mini ES4897 cùng các mẫu Scarlette khác")),
'<h4>Bước 3: Chọn màu dây và mặt theo màu da</h4>',
tbl(["Màu da","Nên ưu tiên","Lưu ý"],[
 ["Da trắng","Màu nhạt hoặc trung tính như nâu, đen, vàng","Một nguồn khuyên tránh màu quá nổi như hồng, đỏ, xanh lá. Nguồn khác lại cho rằng da trắng chọn được nhiều màu, kể cả dây hồng hay tím. Vì vậy màu nổi là tùy chọn, không phải điều cấm."],
 ["Da bánh mật, da ngăm","Đen, nâu đậm, xanh dương đậm, tức màu gần với màu da","Có nguồn gợi ý thêm xanh lá và đỏ đô."],
 ["Da ngâm","Tông vừa phải","Tránh màu quá đậm và quá sáng."],
 ["Da sậm, khỏe mạnh","Mặt đồng hồ sáng kết hợp dây tối màu","Cách phối này làm nổi vùng da quanh cổ tay."],
 ["Theo tông da ấm hoặc lạnh","Tông da ấm hợp màu ấm như đỏ, vàng, cam, hồng","Nên phối thêm với màu trang phục thường mặc."]]),
'<p class="small">Quy tắc màu da là kinh nghiệm thẩm mỹ, các nguồn không hoàn toàn thống nhất. Đeo thử trước gương vẫn là cách chắc nhất.</p>',
'<p>Hai ví dụ minh họa: Daniel Wellington Petite Rosewater với dây vải hồng, mặt trắng, hợp phong cách nữ tính, và Daniel Wellington Classic Sheffield DW00100145 với dây da đen, hợp tông da ngăm:</p>',
gal(
 pf("dw-petite-rosewater","Đồng hồ DW Petite Rosewater","Dây vải hồng, vỏ vàng hồng, mặt trắng",alt="Đồng hồ Daniel Wellington Petite Rosewater dây vải hồng, mặt trắng"),
 pf("dw-classic-sheffield-dw00100145","Đồng hồ Daniel Wellington Classic Sheffield DW00100145","Dây da đen, mặt đen, vỏ bạc",alt="Đồng hồ Daniel Wellington Classic Sheffield DW00100145 dây da đen mặt đen")),
'<h4>Bước 4: Phối theo hoàn cảnh sử dụng</h4>',
'<ul><li><b>Công sở:</b> kiểu tối giản mặt khoảng 30–34 mm, dây da nâu hoặc đen, hoặc dây kim loại mảnh. Một nguồn còn gợi ý mẫu vỏ thép không gỉ và kính sapphire hợp áo sơ mi, chân váy bút chì.</li>',
'<li><b>Thể thao, vận động:</b> chọn dây cao su, mặt lớn hơn, khỏe khoắn và chịu va chạm.</li>',
'<li><b>Dự tiệc, hẹn hò:</b> dây ngọc trai, vòng cứng hoặc dây lưới ánh kim tạo điểm nhấn.</li></ul>',
'<p>Các phong cách này kèm ví dụ cụ thể và ảnh nằm ở bài <a href="#dong-ho-nu-day-da-hay-day-kim-loai">Đồng hồ nữ dây da hay dây kim loại</a>.</p>',
'<div class="note">Màu da chỉ là một yếu tố. Màu trang phục, công việc và sở thích cá nhân cũng quan trọng không kém.</div>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>Đo cổ tay rồi chọn mặt khoảng 22–28 mm (cổ tay nhỏ), 29–34 mm (phổ biến) hoặc 36–40 mm (cổ tay to).</li><li>Cổ tay nhỏ hợp dây mảnh, mặt vuông hoặc chữ nhật; cổ tay to hợp mặt lớn, dây bản to.</li><li>Da trắng chọn màu nhạt hoặc trung tính; da ngăm chọn đen, nâu đậm, xanh dương đậm; da sậm hợp mặt sáng với dây tối.</li><li>Đeo thử trước khi mua nếu có thể.</li></ul>',
src([
 ("VOH: Mách bạn cách chọn đồng hồ đeo tay nữ vừa duyên dáng vừa sang chảnh","https://voh.com.vn/dep/mach-ban-cach-chon-dong-ho-deo-tay-nu-vua-duyen-dang-vua-sang-chanh-342943.html"),
 ("Meta.vn: Cách chọn đồng hồ đeo tay nữ chuẩn nhất","https://meta.vn/hotro/mach-ban-cach-chon-dong-ho-deo-tay-cho-nu-chuan-nhat-3389"),
 ("Meta.vn: Đồng hồ nữ","https://meta.vn/dong-ho-nu-c3323"),
 ("Điện máy XANH: Cách chọn đồng hồ đeo tay phù hợp cho nữ giới","https://www.dienmayxanh.com/kinh-nghiem-hay/cach-chon-dong-ho-deo-tay-phu-hop-cho-nu-gioi-1178227"),
 ("Báo Quốc tế: 6 cách đeo đồng hồ nữ đẹp, đúng cách","https://baoquocte.vn/he-lo-6-cach-deo-dong-ho-nu-dep-dung-cach-danh-cho-nang-167551.html"),
 ("FPT Shop: Những yếu tố cần lưu ý khi chọn đồng hồ cho phái nữ","https://fptshop.com.vn/tin-tuc/thu-thuat/nhung-yeu-to-can-luu-y-khi-chon-dong-ho-cho-phai-nu-103211"),
 ("Thế Giới Di Động: Tư vấn chọn mua đồng hồ cho người có cổ tay nhỏ","https://www.thegioididong.com/hoi-dap/tu-van-chon-mua-dong-ho-cho-nguoi-co-co-tay-nho-1179315"),
 ("Thế Giới Di Động: Top đồng hồ thời trang dành tặng bạn gái","https://www.thegioididong.com/hoi-dap/top-10-dong-ho-thoi-trang-danh-tang-ban-gai-dip-valentine-1414750"),
 ("Đồng hồ Hải Triều: Phụ nữ nên đeo đồng hồ mặt vuông hay tròn","https://donghohaitrieu.com/thu-vien-kien-thuc/thu-vien-dong-ho-nu/nu-nen-deo-dong-ho-mat-vuong-hay-tron.html"),
 ("Tiktakus: Tay nhỏ nên đeo đồng hồ mặt vuông hay tròn","https://www.tiktakus.com/blogs/news/tay-nho-nen-deo-dong-ho-mat-vuong-hay-tron"),
 ("Tiktakus: Cổ tay to nên đeo đồng hồ gì","https://www.tiktakus.com/blogs/news/co-tay-to-nen-deo-dong-ho-gi"),
 ("Elly: Những kiểu dáng mặt đồng hồ phổ biến","https://elly.vn/nhung-kieu-dang-mat-dong-ho-pho-bien-hien-nay/"),
 ("LuxShopping: Khám phá những kiểu dáng đồng hồ phổ biến","https://luxshopping.vn/kien-thuc-dong-ho/kham-pha-nhung-kieu-dang-dong-ho-pho-bien-hien-nay-112926.aspx"),
 ("Fossil Việt Nam: Các phong cách thời trang","https://fossil.com.vn/blogs/news/cac-phong-cach-thoi-trang"),
 ("Shopee Blog: Mẫu đồng hồ nữ đẹp","https://shopee.vn/blog/mau-dong-ho-nu-dep/")])])

B5 = "".join([
'<p>Dây da và dây kim loại không có loại nào “tốt hơn” cho mọi người. Câu trả lời đúng phụ thuộc vào cách bạn sống: bạn ra nhiều mồ hôi không, da có nhạy cảm không, thường đeo đi đâu và thích phong cách nào. Bài này so sánh hai loại dây, sau đó gợi ý từng phong cách đồng hồ nữ kèm mẫu ví dụ.</p>',
'<h4>So sánh nhanh</h4>',
tbl(["Tiêu chí","Dây da","Dây kim loại"],[
 ["Cảm giác và phong cách","Mềm, ôm tay, thanh lịch, tạo cảm giác ấm vào mùa lạnh.","Bề mặt sáng, nhìn chỉn chu, thường tạo cảm giác sang và gọn gàng."],
 ["Độ bền","Một nguồn cho rằng dùng được khoảng 6 tháng đến 2 năm. Dây da tổng hợp ngắn hơn, khoảng 3–6 tháng.","Làm từ chất liệu không gỉ, chống xước và chống ăn mòn tốt, chịu va đập."],
 ["Nhược điểm","Sợ nước, ẩm và mồ hôi. Không hợp người chơi thể thao.","Có thể nặng tay. Dây rẻ tiền có lớp mạ dễ xỉn, gỉ, gây dị ứng."],
 ["Bảo quản","Giữ khô, tránh ngâm nước.","Lau sạch dễ dàng."],
 ["Hợp với","Người ít ra mồ hôi, thích vẻ mềm mại, dùng văn phòng.","Người ra nhiều mồ hôi, hay vận động, hoặc cổ tay to muốn trông gọn."]]),
'<p class="small">Đây là xu hướng chung. Từng mẫu cụ thể có thể khác, nên hãy xem thông số của nhà sản xuất.</p>',
'<h4>Dây da</h4>',
'<h5>Ưu điểm</h5>',
'<ul><li>Mềm, ôm tay và thanh lịch.</li><li>Tạo cảm giác ấm khi đeo vào mùa lạnh.</li><li>Dây bản mảnh tạo cảm giác nhẹ nhàng, hợp cổ tay nhỏ.</li></ul>',
'<h5>Nhược điểm</h5>',
'<ul><li>Không hợp môi trường nước, độ ẩm cao hoặc người ra nhiều mồ hôi.</li><li>Cần tránh để dính nước hoặc ngâm nước.</li><li>Dây da tổng hợp rẻ tiền dễ bong tróc nếu bảo quản sai cách.</li></ul>',
'<h4>Dây kim loại</h4>',
'<h5>Ưu điểm</h5>',
'<ul><li>Bền, chống xước và chống ăn mòn tốt khi làm từ thép không gỉ.</li><li>Dễ lau chùi, hợp người hay vận động hoặc ra nhiều mồ hôi.</li><li>Kết hợp mặt lớn với dây kim loại giúp cổ tay to trông gọn hơn.</li></ul>',
'<h5>Nhược điểm</h5>',
'<ul><li>Có thể nặng tay hơn dây da.</li><li>Dây rẻ tiền có lớp mạ dễ xỉn màu, gỉ và gây dị ứng. Người dị ứng kim loại nên cân nhắc.</li></ul>',
'<h4>Chọn theo phong cách và mẫu ví dụ</h4>',
'<p>Mỗi phong cách thường đi kèm một kiểu dây quen thuộc. Bảng dưới đây gom các nhóm chính, phần sau là ảnh từng mẫu để bạn hình dung:</p>',
tbl(["Phong cách","Đặc điểm","Dây thường gặp","Ví dụ"],[
 ["Tối giản (minimalist)","Mặt tròn, kim mỏng, nền trung tính; hợp văn phòng và sự kiện trang trọng","Dây da hoặc dây lưới kim loại mảnh","Daniel Wellington Classic Petite, Skagen SKW2722"],
 ["Cổ điển","Mặt đồng hồ rõ ràng, dễ phối đồ công sở","Dây da, dây kim loại","Orient Bambino Open Heart RA-AG0003S30B, Fossil Scarlette ES4318"],
 ["Thanh lịch, công nghệ","Hướng đến vẻ thanh lịch, hiện đại; công nghệ Eco-Drive chạy bằng ánh sáng","Dây kim loại, dây da","Citizen EW5593-64D"],
 ["Thời trang, nổi bật","Nằm giữa cổ điển và fashion, nhận diện cao hơn nhóm tối giản","Dây kim loại ánh kim, vòng cứng, dây ngọc trai","Calvin Klein Confidence Bangle 25200023, Julius"],
 ["Năng động, thể thao","Nhỏ gọn, chịu va chạm; hợp đi học, đi làm thoải mái, du lịch","Dây cao su, resin; có kiểu dây da","G-Shock GMA-S2100, Baby-G BA-130-7A1DR, Timex"],
 ["Retro, vuông nhỏ","Dáng vuông hoặc chữ nhật nhỏ gọn, giá dễ tiếp cận","Dây da, dây nhựa, dây lưới","Casio LQ-142E-2ADF, Daniel Wellington Quadro DW00100748, Casio LTP-V007L-9BUDF"]]),
'<h5>Phong cách tối giản</h5>',
'<p>Mặt tròn, kim mỏng, ít chi tiết. Daniel Wellington và Skagen là hai thương hiệu hay được nhắc đến cho phong cách này.</p>',
gal(
 pf("dw-classic-petite","Đồng hồ Daniel Wellington Classic Petite","Mặt đen, vỏ bạc, dây lưới kim loại đen",alt="Đồng hồ Daniel Wellington Classic Petite mặt đen dây lưới kim loại đen"),
 pf("skagen-skw2722","Đồng hồ Skagen SKW2722","Mặt trắng, vỏ và dây lưới màu vàng",alt="Đồng hồ Skagen SKW2722 mặt trắng, vỏ và dây lưới vàng")),
'<h5>Phong cách cổ điển</h5>',
'<p>Mặt số dễ đọc, dễ phối với trang phục công sở. Một mẫu có thể xem thêm là Orient Bambino Open Heart, lộ một phần bộ máy cơ ở mặt số.</p>',
gal(
 pf("orient-bambino-ra-ag0003s30b","Đồng hồ Orient Bambino Open Heart RA-AG0003S30B","Mặt trắng, vỏ vàng, dây da, lộ một phần bộ máy",alt="Đồng hồ Orient Bambino Open Heart RA-AG0003S30B mặt trắng vỏ vàng dây da"),
 pf("fossil-scarlette-es4318","Đồng hồ Fossil Scarlette ES4318","Cọc số La Mã và kim thanh mảnh; mặt hồng, vỏ và dây vàng hồng",alt="Đồng hồ Fossil Scarlette ES4318 mặt hồng, vỏ vàng hồng, cọc số La Mã")),
'<h5>Thanh lịch, công nghệ Eco-Drive</h5>',
'<p>Citizen hướng đến vẻ thanh lịch, hiện đại và công nghệ Eco-Drive chạy bằng ánh sáng, nên giảm nhu cầu thay pin. Mẫu EW5593-64D có mặt chữ nhật nhỏ gọn.</p>',
gal(pf("citizen-ew5593-64d","Đồng hồ Citizen EW5593-64D","Mặt chữ nhật nhỏ gọn, dây lưới vàng hồng, Eco-Drive",alt="Đồng hồ Citizen EW5593-64D mặt chữ nhật nhỏ dây lưới vàng hồng")),
'<h5>Thời trang, nổi bật</h5>',
'<p>Nhóm này có dáng đồng hồ khác lạ hơn: vòng cứng (bangle) hoặc dây ngọc trai xâu chuỗi, hợp dự tiệc hay buổi họp quan trọng.</p>',
gal(
 pf("calvin-klein-confidence-bangle-25200023","Đồng hồ Calvin Klein Confidence Bangle 25200023","Dạng vòng cứng vàng hồng (ảnh chụp mặt sau)",alt="Đồng hồ Calvin Klein Confidence Bangle 25200023 dạng vòng cứng vàng hồng"),
 pf("julius-day-ngoc-trai","Đồng hồ Julius","Dây ngọc trai xâu chuỗi, mặt xanh lục",alt="Đồng hồ Julius dây ngọc trai xâu chuỗi mặt xanh lục")),
'<h5>Năng động, thể thao</h5>',
'<p>Casio nhỏ gọn hoặc Baby-G hợp đi học, đi làm thoải mái, du lịch và những nơi dễ va chạm. Timex đi theo hướng thể thao, khỏe khoắn.</p>',
gal(
 pf("g-shock-gma-s2100","Đồng hồ G-Shock GMA-S2100","Màu hồng nude, chống nước 20 BAR",alt="Đồng hồ G-Shock GMA-S2100 màu hồng nude"),
 pf("baby-g-ba-130-7a1dr","Đồng hồ Baby-G BA-130-7A1DR","Vỏ trắng, mặt hồng",alt="Đồng hồ Baby-G BA-130-7A1DR vỏ trắng mặt hồng"),
 pf("timex-expedition","Đồng hồ Timex","Dáng thể thao, dây da nâu; mặt khá lớn nên nên đeo thử",alt="Đồng hồ Timex Expedition dây da nâu")),
'<h5>Retro, vuông nhỏ</h5>',
'<p>Dáng vuông hoặc chữ nhật nhỏ gọn, giá dễ tiếp cận. Các mẫu Casio và Daniel Wellington Quadro dưới đây là ví dụ quen thuộc.</p>',
gal(
 pf("casio-lq-142e-2adf","Đồng hồ Casio LQ-142E-2ADF","Mặt vuông nhỏ, mặt xanh, dây nhựa đen",alt="Đồng hồ Casio LQ-142E-2ADF mặt vuông xanh dây nhựa đen"),
 pf("dw-quadro-dw00100748","Đồng hồ Daniel Wellington Quadro DW00100748","Mặt chữ nhật, dây lưới vàng hồng",alt="Đồng hồ Daniel Wellington Quadro DW00100748 mặt chữ nhật dây lưới vàng hồng"),
 pf("casio-ltp-v007l-9budf","Đồng hồ Casio LTP-V007L-9BUDF","Mặt chữ nhật, cọc số La Mã, dây da nâu",alt="Đồng hồ Casio LTP-V007L-9BUDF mặt chữ nhật cọc số La Mã dây da nâu")),
'<h4>Chọn theo hoàn cảnh</h4>',
'<ul><li><b>Người ra nhiều mồ hôi, đặc biệt mồ hôi dầu hoặc mồ hôi muối:</b> tránh dây da, chọn dây kim loại hoặc silicone.</li>',
'<li><b>Da nhạy cảm hoặc dị ứng kim loại:</b> dây kim loại không phải lựa chọn tốt; ưu tiên dây da hoặc dây silicone.</li>',
'<li><b>Cổ tay nhỏ:</b> ưu tiên dây da bản mảnh hoặc dây kim loại mắt nhỏ. Xem thêm bài <a href="#cach-chon-dong-ho-nu">Cách chọn đồng hồ nữ theo hình dáng cổ tay và màu da</a>.</li>',
'<li><b>Cổ tay to:</b> mặt lớn với dây kim loại giúp tay trông gọn hơn.</li>',
'<li><b>Công sở:</b> kiểu tối giản mặt 30–34 mm với dây da nâu hoặc đen, hoặc dây kim loại mảnh.</li>',
'<li><b>Độ tuổi:</b> học sinh, sinh viên hợp dây da hoặc dây cao su trẻ trung; người đi làm có thể chọn dây kim loại sang trọng. Tuy vậy độ tuổi không quá quan trọng, mỗi loại dây có phong cách riêng.</li></ul>',
'<div class="note">Muốn đổi phong cách thường xuyên, hãy chọn dòng có dây thay dễ dàng, ví dụ Daniel Wellington có dây da và dây kim loại thay đổi nhanh.</div>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>Dây da mềm và thanh lịch nhưng sợ nước, mồ hôi; dây kim loại bền, dễ lau nhưng có thể nặng hơn.</li><li>Ra nhiều mồ hôi hoặc hay vận động: ưu tiên dây kim loại hoặc silicone.</li><li>Da nhạy cảm với kim loại: ưu tiên dây da hoặc silicone.</li><li>Chọn phong cách trước (tối giản, cổ điển, thời trang, thể thao, retro), rồi chọn kiểu dây đi kèm.</li></ul>',
src([
 ("Meta.vn: Nên đeo đồng hồ dây da hay kim loại","https://meta.vn/hotro/nen-chon-dong-ho-day-da-hay-day-kim-loai-3468"),
 ("Thế Giới Di Động: Nên chọn mua đồng hồ dây da hay dây kim loại","https://www.thegioididong.com/hoi-dap/nen-chon-mua-dong-ho-day-da-hay-dong-ho-day-kim-loai-de-su-1324685"),
 ("Điện máy XANH: Nên mua đồng hồ dây da hay dây kim loại","https://www.dienmayxanh.com/kinh-nghiem-hay/nen-mua-dong-ho-day-da-hay-day-kim-loai-1223744"),
 ("Điện máy XANH: Khám phá các chất liệu dây đeo của đồng hồ thời trang","https://www.dienmayxanh.com/kinh-nghiem-hay/kham-pha-cac-chat-lieu-day-deo-cua-dong-ho-thoi-tr-1193739"),
 ("FPT Shop: Strap là gì, các loại strap đồng hồ","https://fptshop.com.vn/tin-tuc/thu-thuat/strap-cua-dong-ho-la-gi-va-cac-loai-day-dong-ho-pho-bien-hien-nay-132869"),
 ("Thế Giới Di Động: Các loại đồng hồ đeo tay nữ phổ biến","https://www.thegioididong.com/hoi-dap/cac-loai-dong-ho-deo-tay-nu-pho-bien-1595419"),
 ("La Force: Dây da và dây kim loại","https://laforce.vn/?p=61226"),
 ("Shopee Blog: Dây đồng hồ","https://shopee.vn/blog/?p=56360"),
 ("Maison Online: Top hãng đồng hồ nữ được lựa chọn nhiều nhất","https://www.maisononline.vn/blogs/news/cac-hang-dong-ho-nu"),
 ("Shopee Blog: Mẫu đồng hồ nữ đẹp","https://shopee.vn/blog/mau-dong-ho-nu-dep/"),
 ("Tiktakus: Hãng đồng hồ nữ nổi tiếng","https://www.tiktakus.com/blogs/news/cac-hang-dong-ho-nu"),
 ("Tiktakus: Hãng đồng hồ nữ bình dân","https://www.tiktakus.com/blogs/news/cac-hang-dong-ho-nu-binh-dan"),
 ("Tiktakus: Đồng hồ nữ đẹp nhất thế giới","https://www.tiktakus.com/blogs/news/dong-ho-nu-dep-nhat-the-gioi"),
 ("Klein Watches: Đồng hồ nữ thời trang","https://kleinwatches.vn/dong-ho-nu-thoi-trang-dep/"),
 ("Fossil Việt Nam: Các phong cách thời trang","https://fossil.com.vn/blogs/news/cac-phong-cach-thoi-trang"),
 ("DWatches: Đồng hồ nữ công sở","https://dwatches.vn/dong-ho-nu-cong-so/"),
 ("The Julius: Bí quyết chọn đồng hồ nữ cá tính theo từng phong cách","https://thejulius.com.vn/bi-quyet-chon-dong-ho-nu-ca-tinh/"),
 ("The Julius: Đồng hồ nữ mặt vuông nhỏ","https://thejulius.com.vn/dong-ho-nu-mat-vuong-nho/"),
 ("Đồng hồ Duy Anh: Thương hiệu đồng hồ nữ được ưa chuộng tại Việt Nam","https://donghoduyanh.com/tu-van-giai-dap/10-thuong-hieu-dong-ho-nu-duoc-ua-chuong-nhat-tai-viet-nam-n3241.html")])])

B6 = "".join([
'<p>Đồng hồ là món quà có giá trị sử dụng lâu dài, nhưng cũng dễ chọn sai nếu không hợp gu hoặc không vừa cổ tay người nhận. Hãy bắt đầu từ ba câu hỏi: người nhận là ai, bạn có bao nhiêu ngân sách và họ sẽ đeo đồng hồ trong hoàn cảnh nào.</p>',
'<h4>Bước 1: Xác định người nhận và ngân sách</h4>',
'<p>Mối quan hệ (bạn bè, đồng nghiệp, người yêu, người thân, cấp trên) và mức ngân sách quyết định kiểu quà, thương hiệu và chất liệu. Một nguồn gợi ý mốc tham khảo:</p>',
tbl(["Dịp tặng","Mốc ngân sách tham khảo","Ghi chú"],[
 ["Quà thông thường","Khoảng 2–5 triệu đồng","Phù hợp quà sinh nhật, quà cảm ơn"],
 ["Dịp kỷ niệm quan trọng","Khoảng 5–10 triệu đồng","Có thể chọn mẫu có chất liệu tốt hơn"]]),
'<p class="small">Mốc này lấy từ một nguồn viết cho quà tặng bạn trai, dùng để tham khảo cho quà nữ. Giá thay đổi theo thương hiệu, đại lý và thời điểm, nên hãy kiểm tra giá hiện tại.</p>',
'<h4>Bước 2: Chọn kiểu dáng và size an toàn</h4>',
'<ul><li><b>Ưu tiên kiểu cổ điển, dễ phối:</b> vì chưa chắc đã hợp gu người nhận, nên tránh kiểu quá cầu kỳ. Các kiểu như Open Heart hay Moon Phase nên xem là điểm nhấn hơn là lựa chọn nền tảng.</li>',
'<li><b>Size mặt:</b> nếu không biết số đo cổ tay, chọn khoảng 29–34 mm, vùng an toàn cho phần lớn cổ tay nữ. Một số nguồn dùng khoảng 28–34 mm.</li>',
'<li><b>Theo sở thích người nhận:</b> người thích sự lấp lánh, quý phái có thể cân nhắc đồng hồ đính kim cương hoặc đá quý. Với người lớn tuổi, các mẫu bạch kim viền vàng hoặc mạ vàng là gợi ý quen thuộc.</li>',
'<li><b>Theo phong cách sống:</b> người hay vận động ngoài trời nên chọn loại có khả năng chống nước riêng biệt.</li></ul>',
'<p>Một vài mẫu dễ tặng, đã nêu ở bài <a href="#dong-ho-nu-day-da-hay-day-kim-loai">Đồng hồ nữ dây da hay dây kim loại</a>:</p>',
gal(
 pf("dw-classic-petite","Đồng hồ Daniel Wellington Classic Petite","Tối giản, dễ phối đồ",alt="Đồng hồ Daniel Wellington Classic Petite mặt đen dây lưới đen"),
 pf("citizen-ew5593-64d","Đồng hồ Citizen EW5593-64D","Mặt chữ nhật nhỏ gọn, Eco-Drive",alt="Đồng hồ Citizen EW5593-64D mặt chữ nhật nhỏ dây lưới vàng hồng"),
 pf("fossil-scarlette-mini-es4897","Đồng hồ Fossil Scarlette Mini ES4897","Bản thu nhỏ cho cổ tay nhỏ",alt="Đồng hồ Fossil Scarlette Mini ES4897")),
'<h4>Bước 3: Kiểm tra chất liệu và chất lượng</h4>',
'<ul><li><b>Kính:</b> ưu tiên kính sapphire chống xước.</li><li><b>Vỏ:</b> thép không gỉ.</li><li><b>Dây:</b> dây da cao cấp hoặc dây kim loại mạ PVD.</li><li><b>Chống nước:</b> kiểm tra chỉ số trên mặt số hoặc mặt sau, xem bài <a href="#chi-so-chong-nuoc-atm">Chỉ số chống nước 3 ATM, 5 ATM, 10 ATM nghĩa là gì</a>.</li></ul>',
'<h4>Bước 4: Chính hãng, bảo hành và chi tiết tặng quà</h4>',
'<ul><li><b>Hàng chính hãng:</b> không nên tặng hàng giả, vì người nhận sẽ mất quyền lợi bảo hành. Nên chọn đồng hồ hợp gu thời trang và công việc của người đeo.</li>',
'<li><b>Hóa đơn, phiếu bảo hành:</b> giữ lại để có thể đổi mẫu nếu người nhận không vừa ý.</li>',
'<li><b>Dịch vụ gói quà:</b> hỏi trước đại lý về hộp quà và thiệp.</li>',
'<li><b>Khắc chữ:</b> có thể khắc tên, lời chúc hoặc dấu kỷ niệm ở mặt sau đồng hồ để món quà thêm đặc biệt.</li>',
'<li><b>Giá trị tinh thần:</b> một chiếc chính hãng, thanh lịch và hợp phong cách người nhận thường ý nghĩa hơn một mẫu quá xa xỉ.</li></ul>',
'<h4>Gợi ý theo phân khúc</h4>',
tbl(["Phân khúc","Một số thương hiệu hay được nhắc đến","Ghi chú"],[
 ["Phổ thông, có bảo hành chính hãng","Elio, Nakzen, Obaku, Mathey-Tissot, Elle, Korlex","Bảo hành thường từ 1 đến 2 năm tùy hãng, nên hỏi lại đại lý"],
 ["Thời trang tầm trung","Daniel Wellington, Skagen, Fossil, Casio, Citizen","Dễ chọn, nhiều kiểu dáng và màu dây"],
 ["Cao cấp hơn","Longines, Mido, Maurice Lacroix, Frederique Constant; Gucci theo hướng thời trang Ý","Cần ngân sách lớn hơn đáng kể"]]),
'<p class="small">Đây chỉ là ví dụ để bạn tìm hiểu thêm, không phải bảng xếp hạng thương hiệu.</p>',
'<h4>Lưu ý về quan niệm tặng đồng hồ</h4>',
'<p>Đồng hồ là biểu tượng của thời gian, nên ở một số nơi, đặc biệt trong văn hóa phương Đông như Trung Quốc, món quà này không phải lúc nào cũng được đón nhận nhiệt tình. Cách hóa giải được nhiều người nhắc đến là để người nhận “mua lại” món quà bằng một đồng xu nhỏ, tượng trưng cho sự may mắn.</p>',
'<p>Ở góc nhìn tích cực, đồng hồ gợi nhớ quá khứ, hiện tại và tương lai bên người tặng, thể hiện mong muốn gắn kết bền lâu.</p>',
'<div class="note">Nếu chưa chắc người nhận có để ý đến quan niệm này, bạn có thể hỏi nhẹ trước hoặc chuẩn bị sẵn cách tặng phù hợp.</div>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>Xác định người nhận và ngân sách trước, rồi mới chọn kiểu.</li><li>Ưu tiên kiểu cổ điển, dễ phối; chọn mặt 29–34 mm nếu chưa biết số đo cổ tay.</li><li>Chọn hàng chính hãng, có bảo hành; giữ hóa đơn và phiếu bảo hành.</li><li>Cân nhắc khắc chữ, hộp quà và lưu ý quan niệm văn hóa của người nhận.</li></ul>',
src([
 ("FPT Shop: Những yếu tố cần lưu ý khi chọn đồng hồ cho phái nữ","https://fptshop.com.vn/tin-tuc/thu-thuat/nhung-yeu-to-can-luu-y-khi-chon-dong-ho-cho-phai-nu-103211"),
 ("Thế Giới Di Động: 12 cách chọn đồng hồ tặng 20/10 cho từng đối tượng","https://www.thegioididong.com/hoi-dap/12-cach-chon-dong-ho-tang-20-10-cho-tung-doi-1479624"),
 ("Điện máy XANH: Tặng đồng hồ có ý nghĩa gì","https://www.dienmayxanh.com/kinh-nghiem-hay/tang-dong-ho-co-y-nghi-gi-tu-van-tang-dong-ho-cho-1179335"),
 ("Điện máy XANH: Có nên tặng đồng hồ cho bạn gái","https://www.dienmayxanh.com/kinh-nghiem-hay/co-nen-tang-dong-ho-cho-ban-gai-co-y-nghia-gi-1180232"),
 ("Hoàng Hà Mobile: Ý nghĩa tặng đồng hồ","https://hoanghamobile.com/tin-tuc/y-nghia-tang-dong-ho/"),
 ("FPT Shop: Ý nghĩa tặng đồng hồ","https://fptshop.com.vn/tin-tuc/danh-gia/y-nghia-tang-dong-ho-171479"),
 ("Hoa Thuận Watch: Chọn đồng hồ làm quà tặng","https://hoathuanwatch.com/blog/chon-dong-ho-lam-qua-tang"),
 ("LM Timepiece: 5 điều cần lưu ý khi mua đồng hồ làm quà tặng","https://lmtimepiece.com/blogs/news/5-dieu-can-luu-y-khi-mua-dong-ho-lam-qua-tang"),
 ("Đồng hồ chính hãng: Tặng đồng hồ có ý nghĩa gì","https://donghochinhhang.com/blogs/tin-tuc/tang-dong-ho-co-y-nghia-gi"),
 ("Danawatch: Cách chọn đồng hồ làm quà tặng","https://danawatch.vn/chon-dong-ho-lam-qua-tang"),
 ("DWatches: Đồng hồ tặng bạn trai dưới 10 triệu","https://dwatches.vn/dong-ho-tang-ban-trai/"),
 ("Meta.vn: Cách chọn đồng hồ đeo tay nữ chuẩn nhất","https://meta.vn/hotro/mach-ban-cach-chon-dong-ho-deo-tay-cho-nu-chuan-nhat-3389"),
 ("Tuổi Trẻ: Gợi ý quà tặng đồng hồ cho Ngày Quốc tế Phụ nữ 8-3","https://tuoitre.vn/goi-y-qua-tang-dong-ho-cho-ngay-quoc-te-phu-nu-8-3-2024022915421048.htm"),
 ("Mytour: Top đồng hồ mệnh Kim làm quà tặng cho phụ nữ","https://mytour.vn/vi/blog/bai-viet/top-10-dong-ho-menh-kim-pho-bien-lam-qua-tang-cho-phu-nu-tai-mytour.html"),
 ("Luxshopping: Đồng hồ quà tặng doanh nghiệp","https://luxshopping.vn/tin-tuc/dong-ho-qua-tang-doanh-nghiep-119550.aspx")])])

# ---------- Nội dung 4 bài bảo quản và quản lý đồng hồ ----------
B7 = "".join([
'<p>Đồng hồ bền hay không phần lớn phụ thuộc vào cách cất giữ và thói quen hằng ngày. Có sáu yếu tố cần để ý: nước và hơi ẩm, nhiệt độ, từ trường, ánh nắng, va đập và hóa chất. Bài này chỉ cách xử lý từng yếu tố, kèm lý do để bạn hiểu mình đang tránh điều gì.</p>',
'<h4>Bước 1: Tránh nước nóng, hơi nước và xà phòng</h4>',
'<p>Gioăng chống nước làm bằng vật liệu mềm. Dùng lâu, mồ hôi và hơi ẩm làm gioăng mất đàn hồi hoặc giòn, nên khả năng chống nước giảm dần. Vì vậy Citizen khuyên không ngâm đồng hồ trong nước nóng, suối nước nóng hay phòng xông hơi. Casio dặn tránh đeo khi tắm bồn hoặc ở nơi dùng xà phòng, dầu gội vì những điều kiện này làm giảm khả năng chống nước. Không kéo hoặc bấm núm khi đồng hồ đang ướt. Cách đọc chỉ số chống nước nằm ở bài <a href="#chi-so-chong-nuoc-atm">Chỉ số chống nước 3 ATM, 5 ATM, 10 ATM nghĩa là gì</a>.</p>',
'<h4>Bước 2: Kiểm soát nhiệt độ, từ trường, độ ẩm, ánh nắng, va đập và hóa chất</h4>',
tbl(["Yếu tố","Nên làm","Lý do theo hãng và tiêu chuẩn"],[
 ["Nhiệt độ","Tránh để đồng hồ lâu ở nơi dưới 5°C hoặc trên 35°C","Với đồng hồ cơ, Seiko cho biết các chi tiết quyết định độ chính xác đều bằng kim loại nên sai số đổi theo nhiệt độ. Hãng chỉ cam kết sai số khi đeo trên tay ở khoảng 5–35°C. Casio cũng dặn tránh nhiệt độ cực đoan."],
 ["Từ trường","Để cách loa, TV, tủ lạnh, nam châm, điện thoại. Seiko khuyên trên 5 cm (chuẩn JIS cấp 1) hoặc trên 1 cm (cấp 2)","Từ trường mạnh làm lò xo tóc bên trong bị ảnh hưởng, đồng hồ có thể chạy nhanh, chậm hoặc dừng. Khi đã nhiễm từ, đồng hồ cần mang đi khử từ và chỉnh lại độ chính xác. Chuẩn ISO 764 yêu cầu đồng hồ chống từ chịu được 4800 A/m với sai số trong ±30 giây/ngày, nên không phải đồng hồ nào cũng có mức bảo vệ này."],
 ["Độ ẩm","Cất nơi khô ráo, thông thoáng","Seiko xếp nơi ẩm cao, nhiều bụi và rung động mạnh vào nhóm nơi không nên để đồng hồ."],
 ["Ánh nắng","Không để lâu dưới nắng, ví dụ trên taplo ô tô","Dây da dễ phai màu và xuống cấp do ẩm, mồ hôi và ánh nắng. Seiko cảnh báo dây da có thể đổi màu, biến dạng hoặc gãy."],
 ["Va đập","Tránh làm rơi, tránh va đập mạnh","Kính xước, nứt và chi tiết cong vênh đều làm giảm khả năng chống nước (theo Citizen)."],
 ["Hóa chất","Không để tiếp xúc với xăng, dung môi, bình xịt, keo dán, cồn. Nên xịt nước hoa trước khi đeo đồng hồ","Casio khuyên tránh xăng, dung môi, bình xịt và keo dán. Citizen cho biết chất dễ bay hơi, chất tẩy và cồn làm dây da đổi màu và hỏng."]]),
'<p class="small">Các blog tiếng Việt nêu ngưỡng nhiệt độ khác nhau (có nơi ghi 50–60°C). Bài này ưu tiên sách hướng dẫn của hãng. Gói hút ẩm là mẹo phổ biến ở các cửa hàng, nhưng chưa thấy hãng nào viết về nó.</p>',
'<h4>Bước 3: Cất đồng hồ khi không đeo</h4>',
'<ul><li>Trước khi cất lâu, lau sạch bụi, mồ hôi, hơi ẩm rồi cất nơi mát, khô (theo Casio).</li>',
'<li>Nếu đồng hồ còn dính mồ hôi hoặc bụi, lau kỹ và để chỗ thoáng gió, không cho vào hộp kín khi còn ẩm (theo Citizen).</li>',
'<li>Dùng hộp có lớp lót mềm và đặt mặt đồng hồ hướng lên để hạn chế trầy xước. Đây là khuyến nghị của một số cửa hàng.</li></ul>',
'<h4>Bước 4: Chăm sóc theo loại máy</h4>',
'<ul><li><b>Đồng hồ cơ tự động:</b> nên đeo thường xuyên. Seiko cho biết đeo đều giúp độ chính xác của đồng hồ tự động ổn định hơn.</li>',
'<li><b>Đồng hồ pin:</b> thay pin ngay khi có dấu hiệu yếu như chạy chậm hoặc đèn tối (theo hướng dẫn của Casio). Nhiều tiệm sửa cảnh báo pin hết để lâu trong máy có thể rò hóa chất gây ăn mòn, và một cửa hàng khuyên tháo pin nếu không đeo trong thời gian dài. Đây là lời khuyên của tiệm, không phải của hãng.</li></ul>',
'<div class="note">Bảo quản tốt vẫn cần kiểm tra định kỳ. Xem bài <a href="#bao-lau-nen-bao-duong-dong-ho">Bao lâu nên bảo dưỡng đồng hồ một lần</a>. Cách lau dây nằm ở bài <a href="#cach-ve-sinh-day-dong-ho">Cách vệ sinh dây da và dây kim loại của đồng hồ</a>.</div>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>Tránh nước nóng, hơi nước, xà phòng và việc bấm núm khi đồng hồ ướt.</li><li>Giữ đồng hồ ở nhiệt độ ổn định, nơi khô ráo, xa nguồn từ trường.</li><li>Không để dưới nắng gắt, tránh va đập và hóa chất.</li><li>Cất lâu thì lau sạch, để nơi mát, khô, thông thoáng; đồng hồ pin nên thay pin kịp thời.</li></ul>',
src([
 ("Citizen: Water Resistance, hướng dẫn chống nước chính thức","https://www.citizenwatch-global.com/support/maintenance/wr.html"),
 ("Casio: Degree of Water Resistance","https://www.casio-intl.com/asia/en/wat/water_resistance/"),
 ("Casio: Precautions Module No. 3515","https://support.casio.com/global/en/wat/manual/3515_en/PJONSYlaqcpkiu.html"),
 ("Seiko: hướng dẫn sử dụng máy 6R31/6R35/6R38","https://www.seikowatches.com/-/media/HtmlUploader/Common/Seiko/Home/instructions/html/SEIKO_6R31_6R35_6R38_EN/assets/pdf/JSY6R3CA1_EN.pdf"),
 ("Seiko: hướng dẫn sử dụng máy 6R35 (đồng hồ lặn)","https://www.seikowatches.com/-/media/HtmlUploader/Common/Seiko/Home/instructions/html/SEIKO_6R35_D_EN/assets/pdf/JSY6R35D1_EN.pdf"),
 ("Seiko: How should I care for my watch band?","https://www.seikowatches.com/us-en/customerservice/faq/care-maintenance-3"),
 ("Citizen: Metal band (chăm sóc dây kim loại)","https://www.citizenwatch-global.com/support/html/en/w510/maintenance_03_w510.html"),
 ("Wikipedia: Antimagnetic watch","https://en.wikipedia.org/wiki/Antimagnetic_watch"),
 ("Alexander Ferros: Bảo quản đồng hồ đeo tay","https://alexanderferros.com/tin-tuc/bao-quan-dong-ho-deo-tay"),
 ("Tiktakus: Cách bảo quản đồng hồ","https://www.tiktakus.com/blogs/news/cach-bao-quan-dong-ho"),
 ("Emerald Jewelers: Watch Battery Dying? What to Know Before Replacing","https://emeraldjewelers.com/blog/watch-battery-dying-what-to-know-before-you-replace-it/")])])

B8 = "".join([
'<p>Dây tiếp xúc trực tiếp với da nên luôn dính mồ hôi và bụi. Để lâu, dây kim loại có thể gỉ, kể cả inox, gây phát ban và làm ố cổ tay áo. Casio nêu thêm rằng mồ hôi và gỉ trong kẽ dây còn có thể kích ứng da và ảnh hưởng hoạt động của đồng hồ. Citizen nhắc inox không hoàn toàn chống gỉ, vì mồ hôi hoặc vết bẩn có thể làm hỏng lớp phủ. Mỗi loại dây có cách làm sạch riêng, nên bài này chia theo từng chất liệu.</p>',
'<h4>Bước 1: Chuẩn bị</h4>',
'<ul><li>Bàn chải đánh răng lông mềm.</li><li>Nước xà phòng hoặc dung dịch chất tẩy trung tính loãng.</li><li>Khăn mềm thấm hút.</li><li>Màng bọc thực phẩm để bọc mặt và thân đồng hồ khi rửa dây.</li></ul>',
'<h4>Bước 2: Chọn cách làm theo loại dây</h4>',
tbl(["Loại dây","Cách làm sạch","Cần tránh"],[
 ["Kim loại (inox, mạ)","Khi ướt mồ hôi, lau bằng khăn mềm thấm hút. Định kỳ chải nhẹ bằng bàn chải mềm với nước xà phòng, tráng sạch rồi lau khô.","Chất mài mòn, vì làm mòn lớp mạ và lộ phần thép bên dưới. Để dây còn ẩm trong hộp kín."],
 ["Da","Mỗi ngày lau mặt trong và mặt ngoài bằng khăn mềm khô. Khi mồ hôi thấm vào, thấm nhẹ cho khô. Khi bẩn, dùng khăn hơi ẩm rồi lau khô ngay.","Ngâm nước, chà mạnh, cồn, chất tẩy, chất dễ bay hơi. Đeo khi tắm, bơi hoặc làm việc với nước."],
 ["Cao su, resin, silicone (như G-Shock)","Chải nhẹ bằng bàn chải mềm với nước rửa chén dịu, tráng kỹ rồi lau khô. Sau khi tiếp xúc nước biển, tráng ngay bằng nước ngọt.","Để mồ hôi hoặc nước đọng lâu trên dây, cất nơi ẩm cao."]]),
'<h4>Bước 3: Dây kim loại, làm từng bước</h4>',
'<ul><li><b>Bọc mặt đồng hồ bằng màng bọc thực phẩm.</b> Casio và Citizen đều khuyên làm vậy để thân đồng hồ không dính nước và xà phòng. Xà phòng làm giảm khả năng chống nước, xem bài <a href="#cach-bao-quan-dong-ho">Cách bảo quản đồng hồ đeo tay đúng cách tại nhà</a>.</li>',
'<li><b>Nếu tháo được dây, hãy tháo.</b> Citizen khuyên dùng bàn chải mềm và nước xà phòng ấm, tránh chạm vào thân đồng hồ.</li>',
'<li><b>Tráng sạch và lau khô hoàn toàn.</b> Để chỗ thoáng, không cho vào hộp kín khi còn ẩm.</li></ul>',
'<p class="small">Casio chỉ nói nên lau thường xuyên. Mốc 2–4 tuần rửa kỹ một lần là gợi ý của một số trang kỹ thuật, không phải khuyến nghị của hãng.</p>',
'<h4>Bước 4: Dây da, những điều cần nhớ</h4>',
'<ul><li>Dây da dễ hỏng và mòn sớm hơn dây kim loại vì ẩm và mồ hôi. Casio khuyên tránh bơi, rửa hoặc để dây da tiếp xúc trực tiếp với nước, kể cả khi đồng hồ chống nước. Seiko cũng dặn không đeo đồng hồ dây da khi tắm, bơi hoặc làm việc với nước, dù đồng hồ chống nước 10–20 bar.</li>',
'<li>Thấm thay vì chà. Citizen khuyên lau nhẹ, và một hướng dẫn của Seiko cho biết chà mạnh có thể làm đổi màu hoặc mất độ bóng.</li>',
'<li>Seiko khuyên chừa khoảng một ngón tay giữa dây và cổ tay để thoáng và đỡ đọng mồ hôi.</li>',
'<li>Dây da làm từ vật liệu tự nhiên nên sẽ mòn, biến dạng và phai màu theo thời gian. Citizen khuyên thay định kỳ. Dây màu sáng dễ lộ vết bẩn.</li></ul>',
'<h4>Bước 5: Dây cao su, resin và silicone</h4>',
'<ul><li>Dây cao su hút mồ hôi, nước biển và dầu nên dễ nứt rồi gãy (theo Citizen). Casio cho biết để mồ hôi hoặc nước đọng lâu trên dây resin có thể làm dây mòn sớm, rách và gãy.</li>',
'<li>Vệt như bụi trắng trên dây resin là vô hại và lau đi được (theo Casio).</li>',
'<li>Với dây polyurethane, khi dây mất độ mềm dẻo thì nên thay mới.</li></ul>',
'<h4>Sau khi tiếp xúc nước biển hoặc bùn</h4>',
'<p>Casio khuyên tráng bằng nước ngọt sạch. Hãy xem mức chống nước của đồng hồ trước khi rửa. Một hướng dẫn của Seiko ghi đồng hồ chống nước 5, 10 hoặc 20 bar nên rửa trong chậu nước ngọt. Citizen cảnh báo không để nước máy chảy trực tiếp vào đồng hồ.</p>',
'<h4>Da nhạy cảm và thay dây</h4>',
'<ul><li>Người da nhạy cảm nên giữ dây da, dây resin thật sạch. Nếu nổi mẩn thì bỏ đồng hồ ra và hỏi chuyên gia da liễu (theo Casio).</li><li>Khi thay dây, Citizen khuyên thay luôn chốt dây.</li></ul>',
'<div class="note">Dây là phần mòn nhanh nhất của đồng hồ. Nếu dây nứt, giòn, đổi màu hoặc không còn vừa tay thì nên thay thay vì cố làm sạch.</div>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>Dây kim loại: lau mồ hôi, chải nhẹ bằng nước xà phòng loãng, bọc mặt đồng hồ trước khi rửa, lau khô kỹ.</li><li>Dây da: lau khô hằng ngày, thấm chứ không chà, tránh nước và cồn.</li><li>Dây cao su, resin: rửa bằng nước xà phòng dịu, tráng nước ngọt sau khi đi biển.</li><li>Dây hỏng, giòn hoặc phai màu thì thay mới.</li></ul>',
src([
 ("Seiko: hướng dẫn sử dụng máy 8R46/8R48, phần dây đeo","https://www.seikowatches.com/instructions/html/SEIKO_8R46_8R48_EN/BONDSYpbrsfmrq"),
 ("Citizen: Metal band (chăm sóc dây kim loại)","https://www.citizenwatch-global.com/support/html/en/w510/maintenance_03_w510.html"),
 ("Casio: User Maintenance Module No. 3495 G-SHOCK","https://support.casio.com/global/en/wat/manual/3495_en/UQIDSYlzjqphzk.html"),
 ("Casio: Precautions Module No. 3515","https://support.casio.com/global/en/wat/manual/3515_en/PJONSYlaqcpkiu.html"),
 ("Casio: Caring for Watch","https://casiosupport.zendesk.com/hc/en-us/articles/4408758850969-Caring-for-Watch"),
 ("Citizen: What is the best way to care for my watch?","https://support.citizenwatch.com/hc/en-us/articles/360004018013-What-is-the-best-way-to-care-for-my-watch"),
 ("Citizen UK: How should I clean my watch?","https://faq.citizenwatch.co.uk/hc/en-gb/articles/6600433050519-How-should-I-clean-my-watch"),
 ("Citizen: How do I take care of a leather band?","https://www.citizenwatch-global.com/faq/detail/44"),
 ("Seiko: hướng dẫn sử dụng (phần chống nước và dây da)","https://www.seikowatches.com/my-en/-/media/Files/Common/Seiko/instructions/Japanese/4/4205/4205.pdf"),
 ("Seiko Boutique Philippines: How To Care For Your Watch Band","https://shop.seikoboutique.com.ph/blogs/news/how-to-care-for-your-watch-band"),
 ("Seiko: hướng dẫn sử dụng máy 4R35 và các máy cùng dòng","https://www.seikowatches.com/instructions/html/SEIKO_4R35_4R36_4R37_4R38_4R39_4R71_4R72_EN/assets/pdf/JSY4RCC2_EN.pdf"),
 ("Citizen: hướng dẫn sử dụng máy C520","https://www.citizenwatch-global.com/support/pdf/c520/e.pdf"),
 ("Watch Police: How to Clean a Watch","https://watchpolice.com/articles/how-to-clean-a-watch"),
 ("Montres Outlet: How to Clean a Watch and Strap Without Damaging It","https://montres-outlet.com/en/blog/how-to-clean-a-watch-and-strap-without-damaging-it")])])

B9 = "".join([
'<p>Chỉ số chống nước là thông số dễ bị hiểu nhầm nhất trên đồng hồ. Con số 3 ATM, 5 ATM hay 10 ATM là áp suất thử trong phòng thí nghiệm, không phải độ sâu bạn được phép xuống nước. Bài này giải thích cách đọc chỉ số, mỗi mức dùng được cho việc gì theo hãng và những việc làm mất khả năng chống nước.</p>',
'<h4>Bước 1: Hiểu con số ATM</h4>',
'<p>Theo Citizen, một bar xấp xỉ một atm và tương ứng độ sâu nước khoảng 10 m. Vì vậy 3 ATM ≈ 30 m, 5 ATM ≈ 50 m, 10 ATM ≈ 100 m, 20 ATM ≈ 200 m.</p>',
tbl(["Ghi trên đồng hồ","Áp suất thử","Độ sâu quy đổi"],[
 ["3 ATM, 3 BAR, 30M","3 bar","khoảng 30 m"],
 ["5 ATM, 5 BAR, 50M","5 bar","khoảng 50 m"],
 ["10 ATM, 10 BAR, 100M","10 bar","khoảng 100 m"],
 ["20 ATM, 20 BAR, 200M","20 bar","khoảng 200 m"]]),
'<p>Đây không phải độ sâu cho phép. Phép thử chỉ làm một lần, bằng áp suất tĩnh, trên mẫu đồng hồ mới sản xuất, nên đồng hồ ghi 30 m không có nghĩa dùng lâu dài ở độ sâu đó. Trong nước thật, chuyển động tạo ra các đợt tăng áp ngắn mà bài thử tĩnh không mô phỏng.</p>',
'<h4>Bước 2: Xem mỗi mức dùng được cho việc gì</h4>',
tbl(["Mức","Rửa tay, đi mưa","Bơi","Lặn nông, thể thao nước","Lặn bình khí"],[
 ["Chỉ ghi Water Resist (khoảng 3 bar)","Được","Không","Không","Không"],
 ["5 ATM (50 m)","Được","Được, bơi thông thường (theo Casio và Citizen)","Không","Không"],
 ["10 ATM (100 m)","Được","Được","Được, như lướt ván buồm và lặn nông","Không"],
 ["20 ATM (200 m)","Được","Được","Được","Không, trừ khi ghi DIVER’S theo ISO 6425"]]),
'<p class="small">Bảng tổng hợp từ tài liệu của Casio và Citizen. Casio dặn không dùng đồng hồ thường để lặn bình khí. Với dòng 100M của Casio, đồng hồ dùng được khi bơi và lặn ống thở nhưng không dùng khi lướt ván nước hay lặn bình khí. Ví dụ CASIO MWC-100H-1AV ở bài <a href="#cach-chon-dong-ho-nam">Cách chọn đồng hồ nam theo cổ tay và ngân sách</a> ghi WR 100M. Đây là bảng chung của Casio, nên vẫn cần xem sách hướng dẫn của đúng mẫu.</p>',
'<div class="note">Ảnh bìa bài này dùng cách phân loại thận trọng của nhiều cửa hàng, trong đó 5 ATM chưa dùng để bơi và 10 ATM mới bơi được. Citizen, Casio và Seiko lại xếp mức 5 bar vào nhóm dùng được khi bơi thông thường. Nếu bạn bơi thường xuyên, hãy chọn 10 ATM để có thêm biên an toàn và luôn theo sách hướng dẫn của đúng mẫu.</div>',
'<h4>Bước 3: Hiểu tiêu chuẩn ISO</h4>',
'<ul><li><b>ISO 22810:</b> áp dụng cho đồng hồ đeo hằng ngày và bơi. Đồng hồ phải qua các bài thử ngâm, gồm quá áp ít nhất 2 bar trong 10 phút, và mặt kính bên trong không được đọng hơi nước.</li>',
'<li><b>ISO 6425:</b> áp dụng cho đồng hồ lặn, yêu cầu độ sâu từ 100 m trở lên, thử ở 125% áp suất định mức và thử từng chiếc khi sản xuất. Chỉ loại ghi DIVER’S WATCH mới đeo lặn bình khí.</li>',
'<li><b>Thuật ngữ:</b> ISO không cho dùng từ “waterproof” cho đồng hồ, vì vậy nên dùng từ “chống nước”.</li></ul>',
'<h4>Bước 4: Tránh những việc làm mất khả năng chống nước</h4>',
'<ul><li>Dùng núm hoặc nút khi ở dưới nước hoặc đang ướt, và đeo khi núm vặn chưa khóa (theo Citizen).</li>',
'<li>Quên lau sạch nước biển, mồ hôi, bụi sau khi dùng, hoặc để vòi nước chảy trực tiếp vào đồng hồ (theo Citizen).</li>',
'<li>Ngâm nước nóng, tắm nước nóng, xông hơi. Casio còn nói tắm bồn hoặc nơi có xà phòng, dầu gội cũng làm giảm khả năng chống nước.</li></ul>',
'<h4>Bước 5: Nhớ rằng chống nước giảm theo thời gian</h4>',
'<p>Gioăng lão hóa nên Citizen khuyên bảo dưỡng và thay gioăng ít nhất 2–3 năm một lần. Casio cũng khuyên thay gioăng khoảng 2–3 năm và kiểm tra chống nước mỗi khi thay pin. Nếu mặt kính mờ hơi nước không tan, hãy ngừng dùng và mang đến trung tâm bảo hành. Xem thêm bài <a href="#bao-lau-nen-bao-duong-dong-ho">Bao lâu nên bảo dưỡng đồng hồ một lần</a>.</p>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>ATM là áp suất thử, không phải độ sâu cho phép.</li><li>3 ATM chịu mưa, rửa tay; 5 ATM theo hãng dùng được khi bơi thông thường; 10 ATM dùng được cho lặn nông; chỉ đồng hồ ghi DIVER’S mới dùng lặn bình khí.</li><li>Không bấm núm khi ướt, không ngâm nước nóng, xông hơi.</li><li>Gioăng cần thay khoảng 2–3 năm một lần.</li></ul>',
src([
 ("Citizen: Water Resistance, hướng dẫn chống nước chính thức","https://www.citizenwatch-global.com/support/maintenance/wr.html"),
 ("Casio: Degree of Water Resistance","https://www.casio-intl.com/asia/en/wat/water_resistance/"),
 ("Casio: Are there any precautions when handling a water resistant watch?","https://www.casio.com/intl/support/watches/faq/article/00/05/15/61/"),
 ("Casio: Operating Precautions Module No. 5674 G-SHOCK","https://support.casio.com/global/en/wat/manual/5674_en/VPCVSYjxbgcryw.html"),
 ("CLD: Water resistance và tiêu chuẩn ISO 22810","https://www.cld-design.com/en/journal/watch-water-resistance-iso-22810.html"),
 ("ISO 22810:2010, bản trích","https://cdn.standards.iteh.ai/samples/45334/df1ac964c8404f60aa035d5eddaa1829/ISO-22810-2010.pdf"),
 ("Wikipedia: Water Resistant mark","https://en.wikipedia.org/wiki/Water_Resistant_mark"),
 ("WatchScanning: Watch Water Resistance Chart","https://www.watchscanning.com/guides/watch-water-resistance-chart/"),
 ("Shop Watch Direct: Water Resistance Watch Guide","https://shopwatchdirect.com/blogs/news/water-resistance-watch-guide"),
 ("Montres Outlet: 5 ATM on a watch","https://montres-outlet.com/en/blog/5-atm-on-a-watch-everything-you-need-to-know-shower-swimming-pool-swimming"),
 ("Hoerner & Co: How water resistant is a watch","https://www.hoernerco.com/guides/how-water-resistant-is-a-watch")])])

B10 = "".join([
'<p>Đồng hồ cũng cần được bảo dưỡng như xe hay máy móc, nhưng chu kỳ phụ thuộc vào loại bộ máy, hãng và cách bạn dùng. Các nguồn đưa ra mốc khác nhau, nên bài này nêu từng mốc kèm nguồn và gợi ý cách chọn mốc phù hợp.</p>',
'<h4>Bước 1: Biết bảo dưỡng gồm những gì</h4>',
'<p>Theo Seiko UK, đồng hồ cơ có khoảng 200–300 chi tiết và dầu bôi trơn xuống cấp sau nhiều năm. Một lần bảo dưỡng gồm tháo máy, vệ sinh, tra dầu, thay toàn bộ gioăng rồi thử độ chính xác, dự trữ cót và chống nước. Dầu già và linh kiện mòn có thể khiến đồng hồ chạy sai hoặc dừng.</p>',
'<h4>Bước 2: Xem mốc thời gian theo hãng và loại máy</h4>',
tbl(["Loại hoặc hãng","Khuyến nghị","Nguồn"],[
 ["Seiko (cơ)","Khoảng 3 năm một lần, tùy khí hậu và cách giữ gìn","Hãng"],
 ["Grand Seiko","3–4 năm","Trang kỹ thuật dẫn lại hãng"],
 ["Citizen, Casio","Thay gioăng và kiểm tra chống nước khoảng 2–3 năm","Hãng"],
 ["Rolex","Khoảng 10 năm, tùy mẫu và cách dùng","Hãng, qua trang dẫn lại"],
 ["Omega","5–8 năm","Bài thứ cấp"],
 ["Tiệm sửa VN: đồng hồ cơ Nhật","2–3 năm","Tiệm sửa"],
 ["Tiệm sửa VN: đồng hồ cơ khác","3–5 năm","Tiệm sửa"],
 ["Đồng hồ pin","2–3 năm hoặc mỗi lần thay pin; có tiệm nói khoảng 6–7 năm","Tiệm sửa, không thống nhất"]]),
'<p class="small">Citizen và Casio không nêu mốc đại tu bộ máy trong tài liệu được tham khảo. Chưa tìm được khuyến nghị chính thức của Orient, nên con số 2–3 năm cho Orient chỉ là lời các tiệm sửa. Mốc của Rolex và Omega đến từ trang thứ cấp trích lại. Với đồng hồ pin, các tiệm đưa hai con số chênh nhau nhiều, nên hãy theo khuyến nghị của hãng.</p>',
'<h4>Bước 3: Điều chỉnh mốc theo cách dùng</h4>',
'<ul><li><b>Rút ngắn mốc</b> nếu đeo hằng ngày, bơi, đi nhiều hoặc làm việc ở nơi bụi, ẩm.</li><li><b>Kéo dài mốc</b> nếu luân phiên nhiều chiếc, ít đeo và cất giữ tốt.</li><li>Hoạt động mạnh, cách cất giữ và tuổi đồng hồ cũng ảnh hưởng.</li><li>Gioăng lão hóa dù bộ máy còn tốt. Nhiều hãng khuyên kiểm tra chống nước mỗi năm và thay gioăng sau 2–4 năm, tách riêng khỏi việc đại tu.</li></ul>',
'<h4>Bước 4: Nhận biết dấu hiệu cần mang đi sớm</h4>',
'<ul><li>Chạy sai vài phút mỗi ngày, hay dừng, hoặc rôto kêu lạ thì nên bảo dưỡng ngay.</li><li>Mặt kính mờ hơi nước không tan thì ngừng dùng và mang đi kiểm tra (theo Casio).</li></ul>',
'<h4>Bước 5: Cân nhắc quan điểm khác</h4>',
'<ul><li>Một tiệm VN cho rằng không nên lau dầu quá nhiều, chỉ làm khi có vấn đề hoặc theo khuyến cáo của hãng.</li><li>Một bài khác cho rằng đồng hồ hiện đại có thể đi khoảng 10 năm giữa hai lần bảo dưỡng.</li><li>Với đồng hồ rẻ, đổi nguyên bộ máy đôi khi rẻ hơn đại tu.</li></ul>',
'<p>Các ý này không mâu thuẫn với hãng. Gioăng và chống nước vẫn nên kiểm tra theo mốc 2–3 năm nếu bạn hay tiếp xúc nước. Xem thêm bài <a href="#chi-so-chong-nuoc-atm">Chỉ số chống nước 3 ATM, 5 ATM, 10 ATM nghĩa là gì</a> và bài <a href="#dong-ho-co-hay-dong-ho-pin">Đồng hồ cơ hay đồng hồ pin: nên chọn loại nào</a>.</p>',
'<h4>Bước 6: Lên lịch chăm sóc</h4>',
tbl(["Thời điểm","Việc nên làm"],[
 ["Hằng ngày hoặc hằng tuần","Lau mồ hôi, bụi trên dây và thân đồng hồ"],
 ["Hằng năm","Nếu hay bơi, kiểm tra chống nước"],
 ["Mỗi 2–3 năm","Kiểm tra, thay gioăng; đồng hồ pin thì thay pin"],
 ["Đồng hồ cơ","Bảo dưỡng theo hãng, thường khoảng 3–5 năm, sớm hơn nếu có dấu hiệu bất thường"]]),
'<p class="small">Lịch này là tổng hợp từ các nguồn trên, không phải khuyến cáo của một hãng cụ thể.</p>',
'<div class="note">Nên bảo dưỡng ở trung tâm bảo hành hoặc thợ uy tín. Theo Seiko UK, đồng hồ sau bảo dưỡng chính hãng được bảo hành dịch vụ một năm.</div>',
'<h4>Tóm tắt nhanh</h4>',
'<ul><li>Seiko khoảng 3 năm; Citizen và Casio thay gioăng 2–3 năm; Rolex khoảng 10 năm.</li><li>Dùng nhiều, bơi lội thì rút ngắn; ít đeo, luân phiên thì kéo dài.</li><li>Đồng hồ sai giờ nhiều, hay dừng hoặc mờ hơi nước thì mang đi sớm.</li><li>Ưu tiên khuyến nghị của hãng, và chọn nơi bảo dưỡng uy tín.</li></ul>',
src([
 ("Seiko: Why does Seiko recommend servicing your watch about every three years?","https://www.seikowatches.com/us-en/customerservice/faq/care-maintenance-1"),
 ("Seiko: How often should I have the watch serviced?","https://www.seikowatches.com/us-en/customerservice/faq/mechanical-4"),
 ("Seiko UK: Servicing Steps","https://www.seikoservice.co.uk/servicing-steps"),
 ("Citizen: Water Resistance, hướng dẫn chống nước chính thức","https://www.citizenwatch-global.com/support/maintenance/wr.html"),
 ("Casio: Operating Precautions Module No. 5674 G-SHOCK","https://support.casio.com/global/en/wat/manual/5674_en/VPCVSYjxbgcryw.html"),
 ("Hispotion: How to Service a Mechanical Watch","https://www.hispotion.com/how-to-service-a-mechanical-watch-108785"),
 ("We Know Watches: Watch Service Interval Guide","https://weknowwatches.com/watch-service-interval-guide/"),
 ("Horology Library: How Often Should You Service Your Mechanical Watch?","https://horologylibrary.com/maintenance/how-often-should-you-service-your-mechanical-watch/"),
 ("Toke Index: Servicing a Used Seiko","https://tokeindex.com/servicing-a-used-seiko/"),
 ("WatchLab: How Often to Service a Rolex","https://watchlab.sg/blog/how-often-to-service-rolex/"),
 ("The Hour Markers: The Costs Of Luxury Watch Servicing","https://www.thehourmarkers.com/articles/luxury-watch-servicing-costs"),
 ("Thợ đồng hồ: Đồng hồ cơ bao lâu phải bảo dưỡng","https://thodongho.vn/dong-ho-co-bao-lau-phai-bao-duong/"),
 ("BI Watch: Khi nào nên đem đồng hồ đi bảo dưỡng","https://biwatch.vn/khi-nao-nen-dem-dong-ho-di-bao-duong/"),
 ("Đồng hồ Hải Triều: Dịch vụ lau dầu đồng hồ","https://donghohaitrieu.com/dich-vu-lau-dau-dong-ho"),
 ("QVWATCH: Khi nào cần bảo dưỡng đồng hồ","https://donghoquocviet.vn/khi-nao-can-bao-duong-dong-ho/")])])


# (id bài, tiêu đề, tóm tắt, nội dung HTML thêm - để "" nếu chưa có)
C = [
("chon-dong-ho-nam","Chọn đồng hồ nam","Chọn đồng hồ nam theo cổ tay, bộ máy và ngân sách.",[
 ("cach-chon-dong-ho-nam","Cách chọn đồng hồ nam theo cổ tay và ngân sách","Bắt đầu từ ngân sách, hoàn cảnh sử dụng và kích cỡ cổ tay, sau đó mới đến kiểu dáng.",B1),
 ("dong-ho-co-hay-dong-ho-pin","Đồng hồ cơ hay đồng hồ pin: nên chọn loại nào","Đồng hồ pin tiện và ít chăm sóc; đồng hồ cơ cần bảo dưỡng định kỳ nhưng có nét riêng về cơ khí.",B2),
 ("size-dong-ho-nam-theo-co-tay","Size mặt đồng hồ nam bao nhiêu mm là vừa cổ tay","Mặt vừa vặn thường chiếm khoảng hai phần ba bề ngang cổ tay; hãy đo cổ tay trước khi chọn.",B3)]),
("chon-dong-ho-nu","Chọn đồng hồ nữ","Chọn đồng hồ nữ theo cổ tay, màu da, dây đeo và dịp tặng quà.",[
 ("cach-chon-dong-ho-nu","Cách chọn đồng hồ nữ theo hình dáng cổ tay và màu da","Chọn theo hình dáng cổ tay, màu da, kích thước mặt và màu dây để hài hòa.",B4),
 ("dong-ho-nu-day-da-hay-day-kim-loai","Đồng hồ nữ dây da hay dây kim loại","Dây da êm và mềm mại nhưng cần giữ khô; dây kim loại bền, dễ lau nhưng nặng hơn.",B5),
 ("chon-dong-ho-lam-qua-tang","Chọn đồng hồ làm quà tặng: những điều cần lưu ý","Ưu tiên kiểu cổ điển, dễ phối đồ và vừa cổ tay người nhận.",B6)]),
("bao-quan-bao-duong","Bảo quản và bảo dưỡng","Cách bảo quản, vệ sinh đồng hồ đeo tay đúng cách tại nhà.",[
 ("cach-bao-quan-dong-ho","Cách bảo quản đồng hồ đeo tay đúng cách tại nhà","Độ ẩm, nhiệt độ thay đổi và ánh nắng là ba rủi ro chính; cất nơi khô ráo, ổn định.",B7),
 ("cach-ve-sinh-day-dong-ho","Cách vệ sinh dây da và dây kim loại của đồng hồ","Lau bằng vải mềm là bước cơ bản; sau khi tiếp xúc nước biển hoặc bùn thì rửa bằng nước ngọt.",B8)]),
("quan-ly-dong-ho","Quản lý đồng hồ","Theo dõi chống nước, lịch bảo dưỡng và thay pin cho đồng hồ của bạn.",[
 ("chi-so-chong-nuoc-atm","Chỉ số chống nước 3 ATM, 5 ATM, 10 ATM nghĩa là gì","Chỉ số ATM là mức thử nghiệm, không có nghĩa dùng thoải mái ở mọi độ sâu.",B9),
 ("bao-lau-nen-bao-duong-dong-ho","Bao lâu nên bảo dưỡng đồng hồ một lần","Chu kỳ phụ thuộc loại bộ máy; hãy theo khuyến nghị của nhà sản xuất.",B10)]),
]
import sys, math
T = sys.argv[1] if len(sys.argv) > 1 else "1"
OUT = sys.argv[2] if len(sys.argv) > 2 else "docs"
GSC = ""   # dán mã xác minh Google Search Console (cách "Thẻ HTML": chỉ phần content="...") nếu dùng
GS = f'<meta name="google-site-verification" content="{GSC}">' if GSC else ""
ROMAN = ["I","II","III","IV"]
def gear(n=12, r1=40, r2=48, h=13):
    d = ""
    for i in range(n):
        a = 2*math.pi*i/n; w = math.pi/n
        for ang, r in ((a-.5*w,r1),(a-.3*w,r2),(a+.3*w,r2),(a+.5*w,r1)):
            d += ("M" if not d else "L") + f"{50+r*math.cos(ang):.1f} {50+r*math.sin(ang):.1f}"
    return f'<svg viewBox="0 0 100 100" aria-hidden="true"><path fill-rule="evenodd" fill="currentColor" d="{d}ZM{50-h} 50a{h} {h} 0 1 0 {2*h} 0a{h} {h} 0 1 0 {-2*h} 0Z"/></svg>'
GEAR = gear()
IC = {"w":'<circle cx="24" cy="24" r="11"/><path d="M24 18v6l4 3M20 4h8l1 9H19zM19 35h10l-1 9h-8z"/>',
"s":'<rect x="13" y="13" width="22" height="22" rx="5"/><path d="M24 18v6l4 3M19 4h10l-1 9H20zM20 35h8l1 9H19z"/>',
"d":'<path d="M24 5C17 15 12 21 12 28a12 12 0 0024 0c0-7-5-13-12-23z"/><path d="M18 29a6 6 0 006 6"/>',
"c":'<rect x="8" y="10" width="32" height="30" rx="4"/><path d="M8 19h32M16 6v8M32 6v8M17 28l5 5 9-10"/>'}
def icon(k): return f'<svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[k]}</svg>'
def exists(n): return next((f"anh/{n}.{x}" for x in ("jpg","jpeg","png","webp") if os.path.exists(f"anh/{n}.{x}")), None)
hi, bi = exists("hero"), exists("banner")
HERO = f' style="background-image:linear-gradient(rgba(10,15,28,.62),rgba(10,15,28,.62)),url({hi})"' if hi else ""
BAND = '<div class="band reveal"' + (f' style="background-image:linear-gradient(rgba(10,15,28,.55),rgba(10,15,28,.55)),url({bi})"' if bi else "") + '><div class="wrap narrow"><p>✦ Thời gian là thứ đáng chăm sóc nhất, và chiếc đồng hồ là người giữ nó cho bạn. ✦</p></div></div>'
W = "Đồng hồ cơ ✦ Đồng hồ pin ✦ Chống nước ✦ Dây da ✦ Dây kim loại ✦ Bảo dưỡng ✦ Thay pin ✦ Size cổ tay ✦ Quà tặng ✦ "
MQ = f'<div class="mq" aria-hidden="true"><div>{W*4}</div></div>'
FT = [("s","Chọn đúng","Hiểu cổ tay, bộ máy và ngân sách trước khi xuống tiền."),("d","Dùng bền","Biết chống nước, vệ sinh và cất giữ để đồng hồ luôn đẹp."),("c","Chăm sóc đều","Theo dõi lịch bảo dưỡng và thay pin cho từng chiếc.")]
FEAT = '<section class="light fw"><div class="feat">' + "".join(f'<div class="reveal">{icon(k)}<h3>{a}</h3><p>{b}</p></div>' for k,a,b in FT) + '</div></section>'
def fig(slug, alt=""):
    for x in ("jpg","jpeg","png","webp"):
        if os.path.exists(f"anh/{slug}.{x}"):
            return f'<figure class="fig"><img src="anh/{slug}.{x}" alt="{e(alt)}" loading="lazy" width="1280" height="720"></figure>'
    return f'<figure class="fig ph"><span>Thêm ảnh: anh/{slug}.jpg</span></figure>'
def art(a):
    if a[3]:  # bài đã có nội dung: bố cục đầy đủ, ảnh bìa + tiêu đề ở đầu, nội dung bên dưới
        return f'<article id="{a[0]}" class="art full"><div class="head reveal"><div class="txt"><h3>{e(a[1])}</h3><p class="sum">{e(a[2])}</p></div>{fig(a[0], a[1])}</div><div class="body">{a[3]}</div></article>'
    return f'<article id="{a[0]}" class="art reveal"><div class="txt"><h3>{e(a[1])}</h3><p>{e(a[2])}</p>{TODO}</div>{fig(a[0], a[1])}</article>'
menu = '<a class="m-cat" href="#top">Trang chủ</a>'
for c in C:
    menu += f'<a class="m-cat" href="#{c[0]}">{e(c[1])}</a>' + "".join(f'<a class="m-art" href="#{a[0]}">{e(a[1])}</a>' for a in c[3])
menu += '<a class="m-cat" href="#ve-du-an">Về dự án</a><a class="m-cat" href="#lien-he">Liên hệ</a>'
secs = ""
for i, c in enumerate(C):
    arts = "".join(art(a) for a in c[3])
    secs += f'<section id="{c[0]}" class="sec {"light" if i%2==0 else "dark"}"><span class="gear g1">{GEAR}</span><span class="gear g2 r">{GEAR}</span><div class="wrap"><div class="sh reveal"><span class="num">{ROMAN[i]}</span><span class="ico">{icon("swdc"[i])}</span><h2>{e(c[1])}</h2><p class="lead">{e(c[2])}</p></div><div class="arts">{arts}</div></div></section>' + (BAND if i==1 else "")
ticks = "".join(f'<line x1="100" y1="{20 if i%5==0 else 22}" x2="100" y2="{32 if i%5==0 else 27}" transform="rotate({i*6} 100 100)" class="{"t5" if i%5==0 else "t1"}"/>' for i in range(60))
watch = f'<svg class="watch" viewBox="0 0 200 200" role="img" aria-label="Đồng hồ đang chạy"><circle cx="100" cy="100" r="96" class="case"/><circle cx="100" cy="100" r="86" class="dial"/>{ticks}<line id="hh" x1="100" y1="100" x2="100" y2="58" class="hh"/><line id="mh" x1="100" y1="100" x2="100" y2="38" class="mh"/><line id="sh" x1="100" y1="112" x2="100" y2="30" class="sh2"/><circle cx="100" cy="100" r="5" class="pin"/></svg>'
STARS = '<span class="tw t1">✦</span><span class="tw t2">✦</span><span class="tw t3">✦</span><span class="tw t4">✦</span>'
page = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cẩm Nang Đồng Hồ - Chọn và quản lý đồng hồ đeo tay</title>
<meta name="description" content="Cẩm nang chọn và quản lý đồng hồ đeo tay: cách chọn đồng hồ nam, nữ, bảo quản, bảo dưỡng, chống nước và lịch chăm sóc.">
{GS}<link rel="canonical" href="{BASE}"><meta property="og:title" content="Cẩm Nang Đồng Hồ"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}"><meta property="og:locale" content="vi_VN">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%E2%8F%B1%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"><script>document.documentElement.className="js"</script></head>
<body id="top" class="t{T}"><div id="pg"></div>
<header><button id="mb" aria-label="Mở menu" aria-expanded="false" aria-controls="nav"><i></i><i></i><i></i></button><a class="logo" href="#top"><span class="tk">⏱</span> Cẩm Nang Đồng Hồ</a></header>
<nav id="nav" aria-label="Danh sách nội dung">{menu}</nav><div id="veil"></div>
<section class="hero"{HERO}><span class="orbit"></span>{STARS}<div class="wrap hg"><div class="ht"><p class="eyebrow">Chọn ✦ Dùng ✦ Chăm sóc</p><h1>Cẩm nang chọn và quản lý đồng hồ đeo tay</h1><p class="lead">Hướng dẫn chọn đồng hồ nam, nữ, cách bảo quản, bảo dưỡng và quản lý đồng hồ của bạn một cách khoa học.</p><a class="btn" href="#chon-dong-ho-nam">Bắt đầu đọc</a></div><div class="hw">{watch}</div></div></section>{MQ}{FEAT}
{secs}
<section id="ve-du-an" class="sec light"><span class="gear g1">{GEAR}</span><div class="wrap narrow"><div class="sh reveal"><h2>Về dự án</h2></div><p class="reveal">Đây là website học tập theo đề tài: Tối ưu hóa công cụ tìm kiếm cho website cẩm nang chọn và quản lý đồng hồ đeo tay.</p><h3 class="reveal">Sinh viên thực hiện</h3><ul class="reveal"><li>Nguyễn Quí Sơn</li><li>Nguyễn Đức Tiến</li><li>Võ Văn Vĩnh</li></ul></div></section>
<section id="lien-he" class="sec dark"><span class="gear g2 r">{GEAR}</span><div class="wrap narrow"><div class="sh reveal"><h2>Liên hệ</h2></div><p class="reveal">Email: <a href="mailto:thichgacha14@gmail.com">thichgacha14@gmail.com</a></p></div></section>
<footer><span class="tw-s">✦</span> Cẩm Nang Đồng Hồ · Website học tập, không bán hàng <span class="tw-s">✦</span></footer>
<button id="topb" aria-label="Lên đầu trang" hidden>↑</button><script src="script.js" defer></script></body></html>'''
os.makedirs(OUT + "/anh", exist_ok=True)
open(OUT + "/index.html", "w", encoding="utf-8").write(page)
today = __import__("datetime").date.today().isoformat()
open(OUT + "/sitemap.xml", "w", encoding="utf-8").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>{BASE}</loc><lastmod>{today}</lastmod></url>\n</urlset>\n')
open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open(OUT + "/.nojekyll", "w").close()
import glob
for g in glob.glob("google*.html"): shutil.copy(g, OUT)  # tệp xác minh Google Search Console (nếu có)
open(OUT + "/style.css", "w", encoding="utf-8").write(open("style-base.css", encoding="utf-8").read() + open(f"theme-{T}.css", encoding="utf-8").read())
shutil.copy("script.js", OUT)
if os.path.isdir("anh"): shutil.copytree("anh", OUT + "/anh", dirs_exist_ok=True)
print("Xong mau", T, "->", OUT)
