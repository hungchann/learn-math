# 📚 Ôn tập Giải tích 1 (MI1111) - Giữa kỳ

| Thông tin | Chi tiết |
| :--- | :--- |
| **Môn học** | Giải tích 1 (MI1111) |
| **Nội dung** | Tổng hợp kiến thức & Dạng bài tập giữa kỳ |
| **Mục tiêu** | Nắm vững lý thuyết, mẹo giải nhanh và trình bày chuẩn |

---

## 📖 Mục lục
1. [Nội dung chuyên sâu](#i-nội-dung-chuyên-sâu)
    - [Quy tắc hàm hợp & Hàm ẩn](#1-quy-tắc-hàm-hợp--hàm-ẩn)
    - [Đạo hàm các hàm đặc biệt](#2-đạo-hàm-các-hàm-đặc-biệt-mũ-logarit)
    - [Hàm sơ cấp (Euler & Hyperbolic)](#3-hàm-số-sơ-cấp)
2. [Tổng hợp Mẹo nhớ (Cheat Sheet)](#ii-tổng-hợp-mẹo-nhớ-cheat-sheet)
3. [Các dạng bài tập thi giữa kỳ](#iii-các-dạng-bài-tập-thi-giữa-kỳ)

---

## I. Nội dung chuyên sâu

### 1. Quy tắc hàm hợp & Hàm ẩn

#### a. Quy tắc hàm hợp (Chain Rule)
> **Định lý:** Đạo hàm của hàm hợp là tích của các đạo hàm thành phần.

$$f(x) = (g \circ h)(x) = g(h(x)) \quad \Rightarrow \quad f'(x) = g'(h(x)) \cdot h'(x)$$

**Ví dụ minh họa:**  
Tính đạo hàm của $f(x) = \sin(x^2 + 1)$.
*   Đặt $u = x^2 + 1 \Rightarrow u' = 2x$.
*   Hàm trở thành $\sin(u) \Rightarrow (\sin u)' = \cos u \cdot u'$.
*   **Kết quả:** $f'(x) = 2x \cos(x^2 + 1)$.

#### b. Đạo hàm hàm ẩn (Implicit Differentiation)
Sử dụng khi không thể (hoặc khó) biểu diễn $y$ theo $x$ một cách tường minh.

**Bài toán:** Tính $y'$ biết $y = \arcsin(x)$.
1.  Biến đổi về dạng ẩn: $\sin(y) = x$.
2.  Đạo hàm hai vế theo $x$:
    $$\frac{d}{dx}(\sin y) = \frac{d}{dx}(x) \iff \cos(y) \cdot y' = 1$$
3.  Suy ra: $y' = \frac{1}{\cos y} = \frac{1}{\sqrt{1 - \sin^2 y}} = \frac{1}{\sqrt{1 - x^2}}$.

---

### 2. Đạo hàm các hàm đặc biệt (Mũ & Logarit)

#### a. Hàm số mũ tổng quát $y = b^{f(x)}$
Công thức:
$$\frac{d}{dx} b^{f(x)} = f'(x) \cdot b^{f(x)} \cdot \ln b$$

**Ví dụ:** Với $y = e^{2x}$ ($b=e, \ln e = 1$):
$$y' = (2x)' \cdot e^{2x} = 2e^{2x}$$

#### b. Hàm Logarit $y = \log_a(x)$
Chứng minh từ công thức đổi cơ số $\log_a x = \frac{\ln x}{\ln a}$:
$$\frac{d}{dx} \log_a(x) = \frac{d}{dx} \left( \frac{\ln x}{\ln a} \right) = \frac{1}{\ln a} \cdot (\ln x)' = \frac{1}{x \ln a}$$

---

### 3. Hàm số sơ cấp

#### a. Công thức Euler
"Cây cầu" nối liền lượng giác và số phức:
$$e^{ix} = \cos x + i\sin x$$

**Hệ quả (Biểu diễn $\cos, \sin$ qua $e$):**
$$\cos x = \frac{e^{ix} + e^{-ix}}{2}; \quad \sin x = \frac{e^{ix} - e^{-ix}}{2i}$$

#### b. Hàm Hyperbolic
Tương tự lượng giác nhưng trên Hyperbol:
*   $\cosh x = \frac{e^x + e^{-x}}{2}$
*   $\sinh x = \frac{e^x - e^{-x}}{2}$
*   $\tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$

> **Bản chất:**
> *   $e^{ix}$: Biểu diễn phép quay (Rotation) $\rightarrow$ Lượng giác.
> *   $e^x$: Biểu diễn sự tăng trưởng/phóng (Scaling) $\rightarrow$ Hyperbolic.

---

## II. Tổng hợp Mẹo nhớ (Cheat Sheet)

### 1. Đạo hàm cấp cao $y^{(n)}$
Hãy nhớ **"Quy luật biến đổi"** thay vì học vẹt:

| Hàm số ($y$) | Đạo hàm cấp $n$ ($y^{(n)}$) | Mẹo nhớ logic |
| :--- | :--- | :--- |
| **Lượng giác**<br>$\sin(ax), \cos(ax)$ | $a^n \sin(ax + n\frac{\pi}{2})$<br>$a^n \cos(ax + n\frac{\pi}{2})$ | Mỗi lần đạo hàm là một lần cộng thêm góc $90^\circ$ ($\pi/2$). |
| **Phân thức**<br>$\frac{1}{x+a}$ | $\frac{(-1)^n n!}{(x+a)^{n+1}}$ | Số mũ rơi xuống tạo giai thừa ($n!$) và dấu xen kẽ $(-1)^n$. Mẫu tăng bậc. |
| **Logarit**<br>$\ln(x+a)$ | $\frac{(-1)^{n-1}(n-1)!}{(x+a)^n}$ | Là "lùi 1 cấp" của hàm phân thức (vì đạo hàm cấp 1 của $\ln$ là phân thức). |
| **Mũ**<br>$e^{ax}$ | $a^n e^{ax}$ | Đơn giản nhất: chỉ nhân thêm hệ số $a$ mỗi lần đạo hàm. |

**Quy tắc Leibniz (Đạo hàm tích $u \cdot v$):**  
Structurally giống hệt **Nhị thức Newton**:
$$(u \cdot v)^{(n)} = \sum_{k=0}^{n} C_n^k \cdot u^{(n-k)} \cdot v^{(k)}$$
*Tip:* Chọn $v$ là đa thức để nó triệt tiêu về 0 sau vài lần đạo hàm.

### 2. Các Vô cùng bé (VCB) tương đương khi $x \to 0$

| Lượng giác | Mũ & Logarit | Nhị thức |
| :--- | :--- | :--- |
| $\sin x \sim x$ | $e^x - 1 \sim x$ | $(1+x)^\alpha - 1 \sim \alpha x$ |
| $\tan x \sim x$ | $\ln(1+x) \sim x$ | $\sqrt{1+x} - 1 \sim \frac{x}{2}$ |
| $\arcsin x \sim x$ | $a^x - 1 \sim x \ln a$ | $1 - \cos x \sim \frac{x^2}{2}$ |
| $\arctan x \sim x$ | | |

---

## III. Các dạng bài tập thi giữa kỳ

### Dạng 1: Tìm Tập xác định
**Ví dụ:** $y = \arcsin(3x-5)$
*   ĐK: $-1 \le 3x-5 \le 1 \iff 4 \le 3x \le 6 \iff \frac{4}{3} \le x \le 2$.
*   **Đáp án:** $D = [\frac{4}{3}, 2]$.

### Dạng 2: Tính giới hạn & So sánh VCB
**Ví dụ:** $L = \lim_{x \to 0} \frac{(e^{2x^2} - 1) \ln(1+ 3x)}{4x^3 + x^5}$
*   Thay thế VCB: $e^{2x^2}-1 \sim 2x^2$ và $\ln(1+3x) \sim 3x$.
*   Mẫu số: $4x^3 + x^5 = x^3(4+x^2) \sim 4x^3$.
*   Tính toán:
    $$L = \lim_{x \to 0} \frac{(2x^2) \cdot (3x)}{4x^3} = \frac{6}{4} = \frac{3}{2}$$

### Dạng 3: Cực trị hàm số
**Ví dụ:** $y = 3x(\ln x - 7)$ với $x > 0$.
1.  **Đạo hàm:**
    $$y' = 3(\ln x - 7) + 3x \cdot \frac{1}{x} = 3\ln x - 21 + 3 = 3\ln x - 18$$
2.  **Điểm tới hạn:** $y' = 0 \iff \ln x = 6 \iff x = e^6$.
3.  **Xét dấu $y''$:**
    $$y'' = \frac{3}{x} \Rightarrow y''(e^6) = \frac{3}{e^6} > 0$$
    $\Rightarrow$ Hàm số đạt **Cực tiểu** tại $x = e^6$, $y_{CT} = -3e^6$.

### Dạng 4: Quy tắc L'Hospital & Đạo hàm một phía
**L'Hospital:** Dùng cho dạng $\frac{0}{0}$ hoặc $\frac{\infty}{\infty}$.
$$\lim_{x \to 0} \frac{\sin x - x}{x^3} \xrightarrow{L'H} \lim \frac{\cos x - 1}{3x^2} \xrightarrow{L'H} \lim \frac{-\sin x}{6x} = -\frac{1}{6}$$

**Đạo hàm một phía:** Với hàm chứa trị tuyệt đối $|A|$.
*   Xét $A > 0$ và $A < 0$ để phá dấu trị tuyệt đối, sau đó đạo hàm bình thường.

### Dạng 5: Khai triển Maclaurin & Đạo hàm cấp cao tại 0
**Công thức liên hệ:** Hệ số của $x^n$ trong khai triển Maclaurin của $f(x)$ chính là $\frac{f^{(n)}(0)}{n!}$.

**Ví dụ:** Khai triển Maclaurin của $f(x) = e^{-x^3+2}$ đến cấp 21 và tính $f^{(21)}(0)$.

**Bước 1: Khai triển chuỗi**
Ta có $f(x) = e^2 \cdot e^{-x^3}$.
Sử dụng khai triển cơ bản: $e^u = 1 + \frac{u}{1!} + \frac{u^2}{2!} + \dots + \frac{u^n}{n!} + o(u^n)$.
Thay $u = -x^3$:
$$e^{-x^3} = 1 + \frac{(-x^3)}{1!} + \frac{(-x^3)^2}{2!} + \dots + \frac{(-x^3)^7}{7!} + o(x^{21})$$
$$e^{-x^3} = 1 - x^3 + \frac{x^6}{2!} - \frac{x^9}{3!} + \dots - \frac{x^{21}}{7!} + o(x^{21})$$
Vậy khai triển của $f(x)$ đến cấp 21 là:
$$f(x) = e^2 \left( 1 - x^3 + \frac{x^6}{2!} - \dots - \frac{x^{21}}{7!} \right) + o(x^{21})$$

**Bước 2: Tìm đạo hàm cấp cao**
Hệ số của $x^{21}$ trong khai triển trên là:
$$a_{21} = e^2 \cdot \frac{-1}{7!} = -\frac{e^2}{5040}$$
Theo công thức Taylor: $a_{21} = \frac{f^{(21)}(0)}{21!}$.
Suy ra:
$$f^{(21)}(0) = a_{21} \cdot 21! = -\frac{e^2}{7!} \cdot 21!$$

### Dạng 6: Tiệm cận
*   **Đứng:** $\lim_{x \to x_0} f(x) = \infty \Rightarrow x = x_0$.
*   **Ngang:** $\lim_{x \to \infty} f(x) = y_0 \Rightarrow y = y_0$.
*   **Xiên:** $y = ax+b$ với $a = \lim \frac{f(x)}{x}, b = \lim (f(x) - ax)$.