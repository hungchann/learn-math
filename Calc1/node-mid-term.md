# Ôn tập Giải tích 1 (MI1111) - Giữa kỳ

Đây là tài liệu tổng hợp các kiến thức quan trọng và các ví dụ thực tế để chuẩn bị cho bài thi giữa kỳ môn Giải tích 1.

---

## I. Nội dung chuyên sâu

### 1. Quy tắc hàm hợp (Chain Rule)
Công thức: 
$$f(x) = (g \circ h)(x) = g(h(x)) \Rightarrow f'(x) = g'(h(x)) \cdot h'(x)$$

**Ví dụ:** Tính đạo hàm của $f(x) = \sin(x^2 + 1)$
- Đặt $h(x) = x^2 + 1 \Rightarrow h'(x) = 2x$
- $g(u) = \sin(u) \Rightarrow g'(u) = \cos(u)$
- **Kết quả:** $f'(x) = \cos(x^2 + 1) \cdot 2x$

### 2. Đạo hàm hàm ẩn (Implicit Differentiation)
Áp dụng khi hàm số không được cho dưới dạng tường minh $y = f(x)$.

**Ví dụ:** Tính đạo hàm của $y = \arcsin(x)$
1. Chuyển về hàm ẩn: $\sin(y) = x$
2. Đạo hàm hai vế theo $x$:
   $$\frac{d}{dx}(\sin y) = \frac{d}{dx}(x)$$
   $$\cos(y) \cdot y' = 1$$
3. Rút $y'$:
   $$y' = \frac{1}{\cos y}$$
4. Vì $\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$
   $$\Rightarrow y' = \frac{1}{\sqrt{1 - x^2}}$$


### 3. Chứng minh

$$\frac{d}{dx} b^{fx} = f'(x) \cdot \ln b \cdot b^{fx}$$

**Ví dụ:** Tính đạo hàm của $f(x) = e^{2x}$
- $f'(x) = 2$
- $f(x) = e^{2x} \Rightarrow b = e$
- **Kết quả:** $f'(x) = 2e^{2x}$

### 4. Đạo hàm hàm Logarit
**Chứng minh:** $\frac{d}{dx} \log_a(x) = \frac{1}{x \ln a}$

1. Sử dụng công thức đổi cơ số:
   $$\log_a(x) = \frac{\ln x}{\ln a}$$
2. Đạo hàm hai vế theo $x$:
   $$\frac{d}{dx} \log_a(x) = \frac{d}{dx} \left( \frac{\ln x}{\ln a} \right) = \frac{1}{\ln a} \cdot \frac{d}{dx}(\ln x) = \frac{1}{\ln a} \cdot \frac{1}{x} = \frac{1}{x \ln a}$$

---

## II. Các dạng bài tập thi giữa kỳ

### 1. Tìm tập xác định
**Ví dụ:** Tìm tập xác định của hàm số $y = \arcsin(3x-5)$
- Điều kiện: $-1 \le 3x-5 \le 1$
- Giải bất phương trình:
  $$4 \le 3x \le 6 \Leftrightarrow \frac{4}{3} \le x \le 2$$
- **Kết luận:** $D = [\frac{4}{3}, 2]$

> **Lưu ý:** Các vô cùng bé tương đương khi $x \to 0$:
> - $\sin x \sim x$
> - $\tan x \sim x$
> - $\arcsin x \sim x$
> - $\arctan x \sim x$
> - $e^x - 1 \sim x$
> - $\ln(1 + x) \sim x$
> - $(1+x)^n - 1 \sim nx$
> - $1 - \cos x \sim \frac{x^2}{2}$

### 2. So sánh các cặp vô cùng bé
**Ví dụ:** So sánh $a(x) = \sin(2x^2 - x^4)$ và $b(x) = 1 - \cos(2x)$ khi $x \to 0$.
- $a(x) \sim 2x^2 - x^4 \sim 2x^2$ (lấy bậc thấp nhất)
- $b(x) \sim \frac{(2x)^2}{2} = \frac{4x^2}{2} = 2x^2$
- **Kết luận:** $a(x) \sim b(x)$ (hai vô cùng bé tương đương).

### 3. Cực trị hàm số
**Ví dụ:** Tìm cực trị của $y = 3x(\ln x - 7)$ trên $D = (0, +\infty)$.
- Đạo hàm: $y' = 3(\ln x - 7) + 3x \cdot \frac{1}{x} = 3\ln x - 21 + 3 = 3\ln x - 18$
- Cực trị: $y' = 0 \Leftrightarrow \ln x = 6 \Leftrightarrow x = e^6$

**Kiểm tra tính chất:**
- **Cách 1 (Bảng biến thiên):**
  - $0 < x < e^6 \Rightarrow y' < 0$ (nghịch biến)
  - $x > e^6 \Rightarrow y' > 0$ (đồng biến)
  $\Rightarrow$ Cực tiểu tại $x = e^6$, giá trị cực tiểu $y(e^6) = -3e^6$.
- **Cách 2 (Đạo hàm cấp 2):**
  $y'' = \frac{3}{x} \Rightarrow y''(e^6) = \frac{3}{e^6} > 0 \Rightarrow$ Hàm số đạt cực tiểu.

### 4. Quy tắc L'Hospital (Dạng $0/0$ hoặc $\infty/\infty$)
**Ví dụ:** $L = \lim_{x \to 0} \frac{\sin x - x}{x^3}$
- Áp dụng L'Hospital: $L = \lim_{x \to 0} \frac{\cos x - 1}{3x^2}$
- Tiếp tục: $L = \lim_{x \to 0} \frac{-\sin x}{6x}$
- Tiếp tục: $L = \lim_{x \to 0} \frac{-\cos x}{6} = -\frac{1}{6}$

### 5. Tính giới hạn bằng vô cùng bé tương đương
**Ví dụ:** $L = \lim_{x \to 0} \frac{(e^{2x^2} - 1) \ln(1+ 3x)}{4x^3 + x^5}$
- Thay vô cùng bé tương đương:
  $L = \lim_{x \to 0} \frac{(2x^2) \cdot (3x)}{4x^3} = \lim_{x \to 0} \frac{6x^3}{4x^3} = \frac{6}{4} = \frac{3}{2}$

### 6. Đạo hàm một phía
**Ví dụ:** $f(x) = |16 - x^2|$. Tính đạo hàm tại $x = 4$ và $x = -4$.
- **Tại $x = 4$:**
  - $x \to 4^-: f(x) = 16 - x^2 \Rightarrow f'_{-}(4) = -2(4) = -8$
  - $x \to 4^+: f(x) = x^2 - 16 \Rightarrow f'_{+}(4) = 2(4) = 8$
- **Tại $x = -4$:**
  - $x \to -4^-: f(x) = x^2 - 16 \Rightarrow f'_{-}(-4) = 2(-4) = -8$
  - $x \to -4^+: f(x) = 16 - x^2 \Rightarrow f'_{+}(-4) = -2(-4) = 8$

### 7. Khai triển Maclaurin
**Ví dụ:** Cho $f(x) = e^{-x^3+2}$. Tính $f^{(21)}(0)$.
- Ta có $f(x) = e^2 \cdot e^{-x^3}$
- Khai triển $e^u = \sum_{n=0}^{\infty} \frac{u^n}{n!}$. Với $u = -x^3$:

  $e^{-x^3} = \sum_{n=0}^{\infty} \frac{(-x^3)^n}{n!} = \sum_{n=0}^{\infty} \frac{(-1)^n x^{3n}}{n!}$
- Số hạng chứa $x^{21}$ ứng với $3n = 21 \Rightarrow n = 7$:

  Hệ số của $x^{21}$ là: $\frac{f^{(21)}(0)}{21!} = e^2 \cdot \frac{(-1)^7}{7!}$
  $\Rightarrow f^{(21)}(0) = -\frac{21!}{7!} e^2$

### 8. Tiệm cận của đồ thị hàm số
*   **Tiệm cận đứng:** $x = x_0$ nếu $\lim_{x \to x_0} f(x) = \pm\infty$
*   **Tiệm cận ngang:** $y = y_0$ nếu $\lim_{x \to \pm\infty} f(x) = y_0$
*   **Tiệm cận xiên:** $y = ax + b$ ($a \neq 0$) với:
    $$a = \lim_{x \to \pm\infty} \frac{f(x)}{x}; \quad b = \lim_{x \to \pm\infty} [f(x) - ax]$$

**Ví dụ:** Tìm tiệm cận xiên của $f(x) = \frac{x^2+2x-1}{x+1}$
1. $a = \lim_{x \to \infty} \frac{x^2+2x-1}{x(x+1)} = 1$
2. $b = \lim_{x \to \infty} \left(\frac{x^2+2x-1}{x+1} - x\right) = \lim_{x \to \infty} \frac{x-1}{x+1} = 1$
- **Kết luận:** Tiệm cận xiên $y = x + 1$.