# ĐỀ CƯƠNG ÔN TẬP ĐẠI SỐ MI1141 VÀ LỜI GIẢI CHI TIẾT

## MỤC LỤC
1. [Chương 1: Logic, Tập Hợp, Ánh Xạ, Số Phức](#chương-1)
2. [Chương 2: Ma Trận, Định Thức, Hệ Phương Trình](#chương-2)
3. [Chương 3: Không Gian Vectơ](#chương-3)

---

## <a name="chương-1"></a>CHƯƠNG 1: LOGIC, TẬP HỢP, ÁNH XẠ, SỐ PHỨC

### A. TÓM TẮT LÝ THUYẾT

#### 1. Logic Mệnh Đề
- **Các phép toán logic**:
  - Phủ định ($\neg A$, $!A$): Đúng khi A sai.
  - Hội ($A \wedge B$): Đúng khi cả A và B cùng đúng.
  - Tuyển ($A \vee B$): Sai khi cả A và B cùng sai.
  - Kéo theo ($A \to B$): Chỉ sai khi A đúng, B sai. $\Leftrightarrow \neg A \vee B$.
  - Tương đương ($A \leftrightarrow B$): Đúng khi A, B cùng giá trị chân lý.

#### 2. Ánh Xạ
Cho ánh xạ $f: X \to Y$.
- **Đơn ánh**: $\forall x_1, x_2 \in X, f(x_1) = f(x_2) \Rightarrow x_1 = x_2$.
- **Toàn ánh**: $\forall y \in Y, \exists x \in X$ sao cho $f(x) = y$.
- **Song ánh**: Vừa đơn ánh vừa toàn ánh.
- **Ánh xạ tích**: $(f \circ g)(x) = f(g(x))$.

#### 3. Số Phức
- **Căn bậc $n$ của đơn vị**: Là nghiệm của $z^n = 1$. Có $n$ nghiệm:
  $$ \epsilon_k = \cos \frac{2k\pi}{n} + i \sin \frac{2k\pi}{n}, \quad k = 0, 1, \dots, n-1 $$
- **Tính chất**: Tổng bình phương các căn bậc $n$ của đơn vị bằng 0 (với $n > 2$).

---

### B. GIẢI BÀI TẬP CHƯƠNG 1

#### Bài 3. Chứng minh tương đương logic
**(a) $A \leftrightarrow B \equiv (A \wedge B) \vee (\neg A \wedge \neg B)$**
*Giải:*
- $A \leftrightarrow B$ đúng khi A, B cùng đúng hoặc cùng sai.
- Vế phải là hợp của hai trường hợp: "Cả hai cùng đúng" và "Cả hai cùng sai".
$\Rightarrow$ Tương đương.

**(b) $(A \to B) \to C$ và $A \to (B \to C)$ (Không tương đương)**
*Phản ví dụ:*
- $A=Sai, B=Đúng, C=Sai$.
- VT: $(S \to Đ) \to S \equiv Đ \to S \equiv Sai$.
- VP: $S \to (...) \equiv Đúng$.
$\Rightarrow$ Không tương đương.

**(c) $\neg(A \leftrightarrow B) \equiv \neg A \leftrightarrow B$**
*Giải:*
Cả hai đều biểu thị A và B có chân lý đối lập nhau.

#### Bài 16. Ánh xạ trên $R^2$
$f(x, y) = (x^2 - y, x + y)$; $g(x, y) = (x + y, x - y)$

**(a) Tính đơn ánh, toàn ánh của f**
- **Không đơn ánh**: $f(0,0) = f(-1,1) = (0,0)$.
- **Không toàn ánh**: Để hệ $x^2+x = u+v$ có nghiệm thì $u+v \ge -1/4$.

**(b) Tích ánh xạ**
- $f \circ g (x, y) = (x^2 + 2xy + y^2 - x + y, 2x)$.
- $g \circ f (x, y) = (x^2 + x, x^2 - x - 2y)$.

#### Bài 32. Số phức
Tính $S = \sum_{i=1}^{2014} \epsilon_i^2$.
Với $n=2014$, các căn đơn vị có dạng $\omega^k$.
Tổng bình phương là tổng cấp số nhân công bội $q = \omega^2 \neq 1$.
$S = \frac{1 - (q)^n}{1 - q} = 0$ do $q^n = (\omega^n)^2 = 1^2 = 1$.

---

## <a name="chương-2"></a>CHƯƠNG 2 & 3: MA TRẬN - HỆ PHƯƠNG TRÌNH - KHÔNG GIAN VECTƠ

### A. GIẢI BÀI TẬP

#### Bài 17. Tìm m để vectơ thuộc không gian sinh
Cho $u_1 = (1; 3; -2; 1), u_2 = (-2; 3; 1; 1), u_3 = (2; 1; 0; 1), u = (1; -1; -3; m)$.
Tìm $m$ để $u \in \text{span}\{u_1, u_2, u_3\}$.

*Giải:*
Điều này xảy ra khi hệ vectơ $\{u_1, u_2, u_3, u\}$ phụ thuộc tuyến tính, tức là hạng của ma trận tạo bởi 3 vectơ đầu bằng hạng ma trận bổ sung thêm $u$.
Xét ma trận các dòng:
$$ A = \begin{pmatrix} 1 & 3 & -2 & 1 \\ -2 & 3 & 1 & 1 \\ 2 & 1 & 0 & 1 \\ 1 & -1 & -3 & m \end{pmatrix} $$
Biến đổi sơ cấp về dạng bậc thang:
1. $d_2 \leftarrow d_2 + 2d_1$; $d_3 \leftarrow d_3 - 2d_1$; $d_4 \leftarrow d_4 - d_1$
   $\Rightarrow \begin{pmatrix} 1 & 3 & -2 & 1 \\ 0 & 9 & -3 & 3 \\ 0 & -5 & 4 & -1 \\ 0 & -4 & -1 & m-1 \end{pmatrix} \rightarrow \text{Rút gọn } d_2: (0, 3, -1, 1)$
2. Khử cột 2 bằng $d_2 (0, 3, -1, 1)$:
   - $3d_3 + 5d_2 \Rightarrow (0, 0, 7, 2)$
   - $3d_4 + 4d_2 \Rightarrow (0, 0, -7, 3m - 3 + 4) = (0, 0, -7, 3m+1)$
3. $d_4 \leftarrow d_4 + d_3$:
   $\Rightarrow (0, 0, 0, 3m+3)$.
Để $u$ phụ thuộc vào các vectơ còn lại, dòng cuối phải bằng 0:
$$ 3m + 3 = 0 \Leftrightarrow m = -1 $$
**Đáp số: $m = -1$.**

#### Bài 13. Tìm cơ sở và số chiều của KGVT sinh bởi hệ vectơ

**(a) Trong $R^4$:** $v_1 = (2; 1; 3; 4), v_2 = (1; 2; 0; 1), v_3 = (-1; 1; -3; 0)$.
Lập ma trận và biến đổi:
$$ \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 1 & 3 & 4 \\ -1 & 1 & -3 & 0 \end{pmatrix} \xrightarrow{d_1 \leftrightarrow d_2} \dots $$
Sau khi khử Gauss, ta thấy 3 vectơ này độc lập tuyến tính.
- **Số chiều (dim)** = 3.
- **Cơ sở**: $\{v_1, v_2, v_3\}$.

**(b) Trong $R^5$:** $v_1, v_2, v_3, v_4$ như đề bài.
Ta có mối quan hệ:
- $v_3 = v_1 - 2v_2$
- $v_4 = 2v_1 - 3v_2$
Vậy $v_3$ và $v_4$ phụ thuộc vào $v_1, v_2$.
$v_1, v_2$ không tỷ lệ $\Rightarrow$ độc lập tuyến tính.
- **Số chiều (dim)** = 2.
- **Cơ sở**: $\{v_1, v_2\}$.

#### Bài 12. Hạng của ma trận
$$ A = \begin{pmatrix} 1 & -1 & 1 & 2 \\ -1 & 2 & 2 & 1 \\ 1 & 0 & 4 & m \end{pmatrix} $$
Biến đổi:
1. $d_2 + d_1 \to (0, 1, 3, 3)$
2. $d_3 - d_1 \to (0, 1, 3, m-2)$
3. $d_3 - d_2 \to (0, 0, 0, m-5)$
Để hạng bằng 2, dòng cuối phải là dòng 0:
$$ m - 5 = 0 \Leftrightarrow m = 5 $$

#### Bài 21. Hệ có nghiệm duy nhất
Hệ phương trình có ma trận hệ số:
$$ A = \begin{pmatrix} m & 2 & -1 \\ 1 & m & 2 \\ 2 & 3 & 1 \end{pmatrix} $$
Để hệ có nghiệm duy nhất $\Leftrightarrow \det(A) \neq 0$.
$$ \det(A) = m(m-6) - 2(1-4) - 1(3-2m) = m^2 - 6m + 6 - 3 + 2m = m^2 - 4m + 3 $$
$$ \det(A) \neq 0 \Leftrightarrow m^2 - 4m + 3 \neq 0 \Leftrightarrow \begin{cases} m \neq 1 \\ m \neq 3 \end{cases} $$

#### Bài 18. Giải hệ phương trình

**(a)**
$$ \begin{cases} 3x_1 - 5x_2 + 2x_3 + 4x_4 = 2 \\ 7x_1 - 4x_2 + x_3 + 3x_4 = 5 \\ 5x_1 + 7x_2 - 4x_3 - 6x_4 = 3 \end{cases} $$
Biến đổi cho thấy $3 \times (1) - 2 \times (2) + 1 \times (3)$ dẫn đến mâu thuẫn ($0 = 1$ hoặc tương tự).
Kiểm tra: $-3(Pt1) + 2(Pt2) = 1(Pt3)$ về vế trái, nhưng vế phải ra $4 \neq 3$.
$\Rightarrow$ **Hệ vô nghiệm.**

**(b)**
$$ \begin{cases} 3x_1 - x_2 + 3x_3 = 1 \\ -4x_1 + 2x_2 + x_3 = 3 \\ -2x_1 + x_2 + 4x_3 = 4 \\ 10x_1 - 5x_2 - 6x_3 = -10 \end{cases} $$
Giải hệ ta được nghiệm duy nhất:
$$ x_1 = 0, \quad x_2 = 8/7, \quad x_3 = 5/7 $$

**(c)**
$$ \begin{cases} 2x_1 + 3x_2 + 4x_3 = 1 \\ 3x_1 - x_2 + x_3 = 2 \\ 5x_1 + 2x_2 + 5x_3 = 3 \\ x_1 - 4x_2 - 3x_3 = 1 \end{cases} $$
Hạng của A và A ngang đều bằng 2. Hệ có vô số nghiệm phụ thuộc 1 tham số ($x_3$ là ẩn tự do).
Nghiệm tổng quát:
$$ \begin{cases} x_1 = \frac{7 - 7x_3}{11} \\ x_2 = \frac{-1 - 10x_3}{11} \\ x_3 \in \mathbb{R} \end{cases} $$
