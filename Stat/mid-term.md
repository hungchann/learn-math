# Đề Cương Ôn Tập Giữa Kỳ MI2020 - Xác Suất Thống Kê

Tài liệu này tổng hợp nội dung lý thuyết trọng tâm và lời giải chi tiết cho các bài tập trong đề cương thi giữa kỳ của bạn.

---

## Chương 1: Sự Kiện Ngẫu Nhiên và Phép Tính Xác Suất

### I. Tóm Tắt Lý Thuyết

#### 1. Sự kiện và Quan hệ
- **Phép thử ($E$):** Thực hiện một thí nghiệm ngẫu nhiên.
- **Không gian mẫu ($\Omega$):** Tập hợp tất cả các kết quả có thể xảy ra.
- **Sự kiện ($A, B, C...$):** Tập con của $\Omega$.
- **Các quan hệ cơ bản:**
    - **Kéo theo:** $A \subset B$ (Nếu $A$ xảy ra thì $B$ cũng xảy ra).
    - **Tổng:** $A \cup B$ ($A$ hoặc $B$ xảy ra).
    - **Tích:** $AB$ hoặc $A \cap B$ ($A$ và $B$ cùng xảy ra).
    - **Đối ngẫu:** $\overline{A}$ ($A$ không xảy ra). $P(\overline{A}) = 1 - P(A)$.
    - **Xung khắc:** $AB = \emptyset$ (Không thể cùng xảy ra).
    - **Đối lập:** Xung khắc và $A \cup B = \Omega$.

#### 2. Định nghĩa xác suất
- **Cổ điển:** $P(A) = \frac{n(A)}{n(\Omega)}$ (áp dụng khi không gian mẫu hữu hạn và đồng khả năng).
- **Hình học:** $P(A) = \frac{\text{Độ đo của } A}{\text{Độ đo của } \Omega}$ (độ dài, diện tích, thể tích).
- **Thống kê:** Tần suất xuất hiện của sự kiện khi số phép thử $n \to \infty$.

#### 3. Các công thức tính xác suất
- **Công thức cộng:**
  $$P(A \cup B) = P(A) + P(B) - P(AB)$$
  *Nếu A, B xung khắc:* $P(A \cup B) = P(A) + P(B)$.
- **Công thức nhân:**
  $$P(AB) = P(A)P(B|A)$$
  *Nếu A, B độc lập:* $P(AB) = P(A)P(B)$.
- **Xác suất có điều kiện:**
  $$P(A|B) = \frac{P(AB)}{P(B)}$$
- **Công thức Bernoulli:**
  Thực hiện $n$ phép thử độc lập, xác suất thành công mỗi lần là $p$. Xác suất có đúng $k$ lần thành công là:
  $$P_n(k) = C_n^k p^k (1-p)^{n-k}$$
- **Công thức Xác suất đầy đủ:**
  Cho hệ đầy đủ $\{H_1, H_2, ..., H_n\}$ ($H_i$ xung khắc từng đôi và $\cup H_i = \Omega$).
  $$P(A) = \sum_{i=1}^n P(H_i)P(A|H_i)$$
- **Công thức Bayes:**
  Dùng để tính xác suất hậu nghiệm của giả thiết $H_i$ khi biết sự kiện $A$ đã xảy ra:
  $$P(H_i|A) = \frac{P(H_i)P(A|H_i)}{P(A)}$$

---

### II. Giải Bài Tập Mẫu Chương 1

#### 1. Bài tập 1.3: Quan hệ sự kiện
**Đề bài:** Có 3 sinh viên thi môn XSTK. Gọi $A_i$ là sự kiện "sinh viên thứ $i$ đạt điểm tổng kết loại A" ($i=1,2,3$). Hãy biểu diễn các sự kiện:

**(a)** $A$: "Sinh viên thứ nhất có điểm tổng kết **không** phải loại A".
- **Giải:** $A$ là sự kiện đối của $A_1$.
  $$A = \overline{A_1}$$

**(b)** $B$: "Cả ba sinh viên có điểm tổng kết loại A".
- **Giải:** Cả 3 sự kiện $A_1, A_2, A_3$ cùng xảy ra.
  $$B = A_1 A_2 A_3$$

**(c)** $C$: "Có **ít nhất một** trong ba sinh viên có điểm tổng kết loại A".
- **Giải:** Đây là sự kiện tổng. (Lưu ý: Đối lập với "Không có ai được A").
  $$C = A_1 \cup A_2 \cup A_3 \quad \text{hoặc} \quad C = \overline{\overline{A_1} \overline{A_2} \overline{A_3}}$$

**(d)** $D$: "Có **duy nhất một** trong ba sinh viên có điểm tổng kết loại A".
- **Giải:** Xảy ra 1 trong 3 trường hợp xung khắc (chỉ $A_1$ hoặc chỉ $A_2$ hoặc chỉ $A_3$).
  $$D = A_1 \overline{A_2} \overline{A_3} \cup \overline{A_1} A_2 \overline{A_3} \cup \overline{A_1} \overline{A_2} A_3$$

#### 2. VD1: Định nghĩa xác suất / Bernoulli
**Đề bài:** Một thiết bị có 10 chi tiết làm việc độc lập. Xác suất làm việc tốt của mỗi chi tiết là $0.95$. Tìm xác suất để có **ít nhất 1** chi tiết không hoạt động (hỏng).

**Giải:**
- Gọi $X$ là số chi tiết hỏng trong 10 chi tiết.
- Xác suất hỏng của một chi tiết là: $p = 1 - 0.95 = 0.05$.
- Yêu cầu bài toán: Tính $P(X \ge 1)$.
- Sử dụng biến cố đối: "Không có chi tiết nào hỏng" (tất cả 10 chi tiết đều tốt).
  $$P(X \ge 1) = 1 - P(X = 0) = 1 - (0.95)^{10}$$
  $$\approx 1 - 0.5987 = 0.4013$$

#### 3. VD2: Công thức cộng, nhân
**Đề bài:** Hai người A và B chơi bóng rổ. Xác suất ném trúng của A là $0.6$, của B là $0.7$. Mỗi người ném 1 quả.

**Giải:**
- **(a)** Tính xác suất số lần ném trúng của 2 người bằng nhau.
  - Các trường hợp "bằng nhau":
    1. Cả hai cùng trượt: $\overline{A}\overline{B} \Rightarrow P_1 = (1-0.6)(1-0.7) = 0.12$
    2. Cả hai cùng trúng: $AB \Rightarrow P_2 = 0.6 \times 0.7 = 0.42$
  - Tổng xác suất:
    $$P = 0.12 + 0.42 = 0.54$$

- **(b)** Tính xác suất số lần ném trúng của A > số lần ném trúng của B.
  - Xảy ra khi A trúng và B trượt: $A\overline{B}$.
  - Xác suất:
    $$P = P(A\overline{B}) = 0.6 \times (1-0.7) = 0.18$$

#### 4. Bài tập 1.54: Công thức Bayes
**Đề bài:** Kho rượu có số lượng loại A và loại B bằng nhau $\Rightarrow P(A) = P(B) = 0.5$. Chọn ngẫu nhiên 1 chai, đưa 5 người nếm. Xác suất đoán đúng mỗi người là $0.8$.
- Kết quả thực nghiệm ($E$): 3 người đoán A, 2 người đoán B.
- Hỏi: Xác suất chai rượu đó thực sự là loại A ($P(A|E)$)?

**Giải:**
- Đặt $H_1$: Rượu là loại A; $H_2$: Rượu là loại B. $P(H_1)=P(H_2)=0.5$.
- Tính xác suất có kết quả $E$ (3 người bảo A, 2 người bảo B) trong từng trường hợp:
    - Nếu là rượu A ($H_1$): 3 người đoán đúng (bảo A), 2 người đoán sai (bảo B).
      $$P(E|H_1) = C_5^3 (0.8)^3 (0.2)^2 = 10 \times 0.512 \times 0.04 = 0.2048$$
    - Nếu là rượu B ($H_2$): 3 người đoán sai (bảo A), 2 người đoán đúng (bảo B).
      $$P(E|H_2) = C_5^3 (0.2)^3 (0.8)^2 = 10 \times 0.008 \times 0.64 = 0.0512$$
- Áp dụng công thức Bayes:
  $$P(H_1|E) = \frac{P(E|H_1)P(H_1)}{P(E|H_1)P(H_1) + P(E|H_2)P(H_2)}$$
  $$= \frac{0.2048 \times 0.5}{0.2048 \times 0.5 + 0.0512 \times 0.5} = \frac{0.2048}{0.256} = 0.8$$
**Đáp số:** $0.8$ (hay $80\%$).

---

## Chương 2: Biến Ngẫu Nhiên và Phân Phối Xác Suất

### I. Tóm Tắt Lý Thuyết

#### 1. Biến ngẫu nhiên (BNN)
- **Rời rạc:** Nhận giá trị đếm được $x_1, x_2, ...$. Phân phối xác suất cho bởi bảng $P(X=x_k)=p_k$.
- **Liên tục:** Nhận giá trị lấp đầy một khoảng. Phân phối xác suất cho bởi hàm mật độ $f(x)$.

#### 2. Các hàm đặc trưng
- **Hàm phân phối (CDF):** $F(x) = P(X < x)$ (hoặc $P(X \le x)$).
- **Hàm mật độ (PDF - BNN liên tục):** $f(x) = F'(x)$.
  - Tính chất: $\int_{-\infty}^{+\infty} f(x)dx = 1$.
  - Tính xác suất: $P(a < X < b) = \int_a^b f(x)dx$.

#### 3. Số đặc trưng
- **Kỳ vọng $E(X)$ (Gía trị trung bình):**
    - Rời rạc: $E(X) = \sum x_i p_i$
    - Liên tục: $E(X) = \int_{-\infty}^{+\infty} x f(x) dx$
- **Phương sai $V(X)$ (Độ phân tán):**
  $$V(X) = E(X^2) - [E(X)]^2$$
  *(Trong đó $E(X^2) = \sum x_i^2 p_i$ hoặc $\int x^2 f(x)dx$)*

#### 4. Phân phối thông dụng
- **Nhị thức $B(n, p)$:** $n$ thử nghiệm Bernoulli. $E(X)=np$.
- **Poisson $P(\lambda)$:** Sự kiện hiếm. $E(X)=V(X)=\lambda$.
- **Chuẩn $N(\mu, \sigma^2)$:** Quan trọng nhất. Hàm mật độ hình chuông đối xứng qua $\mu$.
- **Đều $U(a, b)$**, **Mũ $E(\lambda)$**.

---

### II. Giải Bài Tập Mẫu Chương 2

#### 1. Bài tập 2.6 (và VD3): BNN Rời rạc
**Đề bài:** Một xạ thủ có 5 viên đạn. Bắn đến khi trúng 2 viên **hoặc** hết đạn thì dừng. Xác suất trúng mỗi lần là $0.4$. Gọi $X$ là số đạn cần bắn.
**(a) Tìm phân phối xác suất của X.**
$X$ nhận giá trị $\{2, 3, 4, 5\}$.
- $P(X=2)$: Trúng cả 2 viên đầu ($TT$). $0.4^2 = 0.16$.
- $P(X=3)$: 2 viên đầu có 1 trúng, viên 3 trúng. $C_2^1 (0.4)(0.6) \times 0.4 = 0.192$.
- $P(X=4)$: 3 viên đầu có 1 trúng, viên 4 trúng. $C_3^1 (0.4)(0.6)^2 \times 0.4 = 0.1728$.
- $P(X=5)$: Dừng ở viên 5 (có 2 khả năng):
    1. Viên 5 là viên trúng thứ 2 (Trước đó 1 trúng 3 trượt).
       $P_1 = C_4^1 (0.4)(0.6)^3 \times 0.4 = 0.13824$.
    2. Hết đạn mà chưa đủ 2 viên trúng (0 trúng hoặc 1 trúng cả 5 viên).
       $P_2 = (0.6)^5 + C_5^1 (0.4)(0.6)^4 = 0.07776 + 0.2592 = 0.33696$.
    $\Rightarrow P(X=5) = 0.13824 + 0.33696 = 0.4752$.

**Bảng phân phối:**
| X | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|:-:|
| P | 0.16 | 0.192 | 0.1728 | 0.4752 |

**(b) Tính kỳ vọng:**
$$E(X) = 2(0.16) + 3(0.192) + 4(0.1728) + 5(0.4752) = 3.9632$$

#### 2. Bài 2.24 (VD4): BNN Liên tục
**Đề bài:** Cho hàm mật độ $f(x) = c \cdot e^{-(x + e^{-x})}$.
**Giải:**
- **Tìm c:** Điều kiện chuẩn hóa $\int_{-\infty}^{+\infty} f(x)dx = 1$.
  Đặt $u = e^{-x} \Rightarrow du = -e^{-x}dx$. Khi đó $e^{-x}dx = -du$.
  Biểu thức trong tích phân: $e^{-x} \cdot e^{-e^{-x}} dx \Rightarrow -e^{-u} du$.
  $\int_{+\infty}^0 -e^{-u} du = \int_0^{+\infty} e^{-u} du = 1$.
  Vậy $c=1$.
- **Tính kỳ vọng:** Đây là phân phối Gumbel Chuẩn. $E(X) \approx 0.5772$ (Hằng số Euler).

#### 3. Bài tập 2.39: Nhị thức & Hình học
**Đề bài:** 10 máy, tỷ lệ phế phẩm $p=0.02$.
**(a) Xác suất lấy 10 sp có nhiều nhất 2 phế phẩm:**
- Gọi $Y$ là số phế phẩm. $Y \sim B(10, 0.02)$.
- $P(Y \le 2) = P(0) + P(1) + P(2)$
  $= C_{10}^0 (0.98)^{10} + C_{10}^1 (0.02)(0.98)^9 + C_{10}^2 (0.02)^2 (0.98)^8$
  $\approx 0.817 + 0.167 + 0.015 \approx 0.999$.

**(b) Trung bình số sp máy 1 sx trước khi hỏng đầu tiên:**
- Phân phối Hình học. Kỳ vọng $E = \frac{1}{p} = \frac{1}{0.02} = 50$ sản phẩm.

#### 4. Bài tập 2.50: Phân phối Chuẩn
**Đề bài:** Lựa chọn phương án kinh doanh. Yêu cầu lợi nhuận $\ge 80$ triệu.
- **PA1:** $X_1 \sim N(140; 50^2)$.
  $$P(X_1 \ge 80) = P(Z \ge \frac{80-140}{50}) = P(Z \ge -1.2) \approx 0.8849$$
- **PA2:** $X_2 \sim N(200; 60^2)$.
  $$P(X_2 \ge 80) = P(Z \ge \frac{80-200}{60}) = P(Z \ge -2.0) \approx 0.9772$$

**Kết luận:** Chọn **Phương án 2** vì xác suất đạt mục tiêu cao hơn ($97.7\% > 88.5\%$).
