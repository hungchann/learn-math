# 🧠 Sơ đồ tư duy: Xác suất & Thống kê
> **Từ Căn Bản đến Công Thức**

---

## 💡 Triết lý chung

Toàn bộ môn học này thực chất chỉ xoay quanh **một câu chuyện duy nhất**:

> **Thực tế ngẫu nhiên** $\rightarrow$ **Mô tả bằng xác suất** $\rightarrow$ **Dùng mẫu để suy ngược lại tổng thể**

Bạn chỉ cần nắm vững 3 tầng tư duy dưới đây là có thể suy ra gần như toàn bộ công thức.

---

## 🔴 Tầng 1: XÁC SUẤT – "Đếm khả năng xảy ra"

### 1.1. Ý tưởng gốc
Xác suất là **tỉ lệ số lần biến cố xảy ra trên tổng số lần thử khi lặp vô hạn**:

$$P(A) = \frac{\text{Số trường hợp thuận lợi cho A}}{\text{Tổng số trường hợp có thể}}$$

### 1.2. Các quy tắc cơ bản
*   **Cộng xác suất:** 
    *   Nếu A, B xung khắc: $P(A \cup B) = P(A) + P(B)$
    *   Nếu không xung khắc: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ (tránh đếm trùng).
*   **Nhân xác suất:** $P(A \cap B) = P(A) \cdot P(B|A)$
    *   *Giải thích:* Xác suất A và B cùng xảy ra = xác suất A xảy ra $\times$ xác suất B xảy ra khi đã biết A đã xảy ra.
*   **Xác suất có điều kiện:** $P(A|B) = \frac{P(A \cap B)}{P(B)}$ (thu hẹp không gian mẫu lại chỉ còn B).
*   **Công thức Bayes:** Đảo ngược điều kiện dựa trên $P(A \cap B)$:
    $$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

### 1.3. Các phân phối rời rạc – "Mô hình đếm"
*   **Bernoulli:** 1 lần thử (Thành công $p$ / Thất bại $q=1-p$).
*   **Nhị thức (Binomial):** Lặp $n$ lần Bernoulli độc lập, đếm số lần thành công:
    $$P(X=k) = C_n^k \cdot p^k \cdot q^{n-k}$$
*   **Poisson:** Đếm số sự kiện trong một khoảng (thời gian/không gian) với tốc độ trung bình $\lambda$:
    $$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
*   **Siêu bội (Hypergeometric):** Chọn $n$ phần tử từ tập $N$ (có $M$ phần tử loại 1), không hoàn lại:
    $$P(X=k) = \frac{C_M^k \cdot C_{N-M}^{n-k}}{C_N^n}$$

### 1.4. Phân phối liên tục – "Đếm" bằng tích phân
*   **Hàm mật độ $f(x)$:** Xác suất trong khoảng $[a, b]$ là diện tích dưới đường cong:
    $$P(a < X < b) = \int_a^b f(x)\,dx$$
*   **Hàm phân phối tích lũy:** $F(x) = P(X \le x) = \int_{-\infty}^x f(t)\,dt$
*   **Phân phối chuẩn $N(\mu, \sigma^2)$:** Hình chuông đối xứng quanh $\mu$.
    *   **Quy tắc 68-95-99.7:**
        *   68% dữ liệu trong $[\mu \pm \sigma]$
        *   95% dữ liệu trong $[\mu \pm 2\sigma]$
        *   99.7% dữ liệu trong $[\mu \pm 3\sigma]$

### 1.5. Kỳ vọng & Phương sai – "Tâm và Độ rộng"
*   **Kỳ vọng $E(X)$:** Giá trị trung bình lý thuyết.
    *   Rời rạc: $E(X) = \sum x_i P(X=x_i)$
    *   Liên tục: $E(X) = \int_{-\infty}^\infty x f(x)\,dx$
*   **Phương sai $\text{Var}(X)$:** Độ dao động quanh trung bình.
    $$\text{Var}(X) = E(X^2) - [E(X)]^2$$
*   **Độ lệch chuẩn $\sigma = \sqrt{\text{Var}(X)}$:** Đưa về cùng đơn vị với $X$.

> **Tóm lại tầng 1:** Mọi bài xác suất đều là "đếm". Nắm vững cách đếm + nhận dạng đúng mô hình (Nhị thức/Poisson/Chuẩn) là coi như xong bài.

---

## 🟡 Tầng 2: BIẾN NGẪU NHIÊN – "Gắn số cho kết quả"

### 2.1. Bản chất
Biến ngẫu nhiên $X$ là cầu nối: **Kết quả thí nghiệm $\rightarrow$ Con số thực**.
*Ví dụ: Gieo 2 con xúc xắc, $X$ = Tổng số chấm.*

### 2.2. Đặc trưng mô tả
| Đặc trưng | Ý nghĩa | Công thức cơ bản |
| :--- | :--- | :--- |
| **Kỳ vọng $E(X)$** | Trung bình lý thuyết | $\sum x_i p_i$ hoặc $\int x f(x)dx$ |
| **Phương sai $\text{Var}(X)$** | Độ phân tán | $E(X^2) - [E(X)]^2$ |
| **Độ lệch chuẩn $\sigma$** | Độ lệch thực tế | $\sqrt{\text{Var}(X)}$ |

### 2.3. Định lý giới hạn trung tâm (CLT) – "Trái tim của Thống kê"
Khi cỡ mẫu $n$ đủ lớn ($n \ge 30$), trung bình mẫu $\bar{X}$ sẽ có phân phối gần đúng là **Phân phối Chuẩn**:

$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \Rightarrow \quad Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$$

> **Tóm lại tầng 2:** Biến ngẫu nhiên biến mọi thứ ngẫu nhiên thành các con số có thể tính toán. CLT cho phép chúng ta dùng phân phối Chuẩn/t để suy luận cho dù tổng thể gốc có phân phối gì đi nữa.

---

## 🔵 Tầng 3: THỐNG KÊ – "Từ mẫu suy ngược tổng thể"

Trong thực tế, ta không biết tham số tổng thể ($\mu, p, \sigma^2$). Ta dùng mẫu $(x_1, \dots, x_n)$ để:
1.  **Ước lượng:** Đoán giá trị tham số.
2.  **Kiểm định:** Thử nghiệm một giả thuyết về tham số.

### 3.1. Ước lượng điểm (Best Guess)
| Tham số tổng thể | Ước lượng từ mẫu | Công thức |
| :--- | :--- | :--- |
| **Trung bình $\mu$** | Trung bình mẫu $\bar{x}$ | $\frac{1}{n}\sum x_i$ |
| **Tỉ lệ $p$** | Tỉ lệ mẫu $\hat{p}$ | $m/n$ |
| **Phương sai $\sigma^2$** | Phương sai mẫu hiệu chỉnh $s^2$ | $\frac{1}{n-1}\sum (x_i - \bar{x})^2$ |

### 3.2. Ước lượng khoảng (Best Guess $\pm$ Sai số)
Công thức chung:
$$\text{Khoảng tin cậy} = \text{Ước lượng điểm} \pm \text{Hệ số phân phối} \times \text{Sai số chuẩn}$$

**Bảng chọn phân phối cho $\mu$:**
| Điều kiện | Phân phối | Công thức biên sai số ($\epsilon$) |
| :--- | :--- | :--- |
| Biết $\sigma$ (hoặc $n \ge 30$) | Chuẩn ($z_{\alpha/2}$) | $z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$ |
| Chưa biết $\sigma$ và $n < 30$ | t-Student ($t_{\alpha/2}$) | $t_{\alpha/2}(n-1) \cdot \frac{s}{\sqrt{n}}$ |

### 3.3. Kiểm định giả thuyết (Bằng chứng & Bác bỏ)
Khung tư duy 5 bước:
1.  **Giả thuyết:** $H_0$ (không đổi) và $H_1$ (đối lập).
2.  **Chọn Thống kê kiểm định:** $Z, t, \chi^2$ hoặc $F$.
3.  **Tính giá trị quan sát:** Từ dữ liệu mẫu.
4.  **So sánh:** Với giá trị tới hạn (tra bảng) hoặc dùng **p-value**.
5.  **Kết luận:** Bác bỏ $H_0$ hay chưa đủ cơ sở bác bỏ.

**Công thức chung cho Thống kê kiểm định:**
$$\text{Giá trị kiểm định} = \frac{\text{Ước lượng mẫu} - \text{Giá trị giả thuyết}}{\text{Sai số chuẩn}}$$

### 3.4. So sánh 2 mẫu & Hồi quy
*   **So sánh 2 trung bình:** $\frac{(\bar{x}_1 - \bar{x}_2) - 0}{SE_{diff}}$
*   **Hệ số tương quan $r$:** Đo độ mạnh mối quan hệ tuyến tính ($-1 \le r \le 1$).
*   **Hồi quy tuyến tính:** $\hat{y} = a + bx$ (Dùng phương pháp bình phương tối thiểu).

> **Tóm lại tầng 3:** Mọi bài toán thống kê đều là **Chuẩn hóa và So sánh**. Bạn lấy kết quả từ mẫu, đưa về một phân phối chuẩn mực ($z, t$), rồi xem nó "bất thường" đến mức nào so với giả thuyết.

---

## 🗺️ Sơ đồ tổng hợp: Từ gốc đến ngọn

1.  **THỰC TẾ NGẪU NHIÊN**
    *   $\downarrow$ *Tầng 1:* **Xác suất** (Đếm khả năng: Nhị thức, Poisson, Chuẩn...)
2.  **DỮ LIỆU ĐO ĐẠC**
    *   $\downarrow$ *Tầng 2:* **Biến ngẫu nhiên** (Đặc trưng: $E(X), \text{Var}(X)$. Cầu nối: CLT)
3.  **KẾT LUẬN & DỰ BÁO**
    *   $\downarrow$ *Tầng 3:* **Thống kê** (Ước lượng khoảng, Kiểm định giả thuyết, Hồi quy)
4.  **🎯 RA QUYẾT ĐỊNH**

---

## 🛠️ Bí kíp giải bài nhanh

Khi đọc đề, hãy đi qua 3 bước:
1.  **Phân loại:** Là bài toán **Xác suất** (tính $P$), **Biến ngẫu nhiên** (tính $E, \text{Var}$), hay **Thống kê** (Ước lượng/Kiểm định)?
2.  **Xác định mô hình:** 
    *   Xác suất: Có mấy lần thử? Có độc lập không? (Nhị thức hay Poisson?)
    *   Thống kê: Đang xét tham số nào ($\mu, p$ hay $\sigma^2$)? Mẫu lớn hay nhỏ? Đã biết $\sigma$ chưa?
3.  **Áp dụng khung:**
    *   Khoảng tin cậy: $\text{điểm} \pm \text{hệ số} \times \text{sai số}$
    *   Kiểm định: $T = \frac{\text{mẫu} - \text{giả thuyết}}{\text{sai số}}$

**Ví dụ:** Mẫu $n=25$, $\bar{x}=7.2, s=1.5$. Ước lượng $\mu$ ở độ tin cậy 95%.
- **Bước 1:** Thống kê - Ước lượng khoảng cho $\mu$.
- **Bước 2:** $n < 30$, chưa biết $\sigma \rightarrow$ Dùng phân phối **t**.
- **Bước 3:** $7.2 \pm t_{0.025}(24) \cdot \frac{1.5}{\sqrt{25}} \approx 7.2 \pm 2.064 \cdot 0.3 = 7.2 \pm 0.62$.

---
*Chúc bạn chinh phục môn Xác suất Thống kê dễ dàng!* 🚀
