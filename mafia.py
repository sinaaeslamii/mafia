def solve_mafia(A):
    n = len(A)
    # تشخیص خاکستری: فقط به خودش 1 و برای بقیه 0
    grey = [A[i][i] == 1 and all(A[i][j] == 0 for j in range(n) if j != i) for i in range(n)]

    # نقش‌ها: +1 شهروند، -1 مافیا (خاکستری‌ها را جدا کردیم)
    role = [0]*n
    for i in range(n):
        if grey[i]:
            role[i] = 0  # خاکستری
    # مؤلفه‌ها را با قید A[i][j] = role[i] * role[j] برای ورودی‌های غیرصفر حل می‌کنیم
    for s in range(n):
        if role[s] != 0:  # 0 اینجا یعنی هنوز تعیین‌نشده (نه خاکستری واقعی)
            continue
        role[s] = 1  # فرض شروع
        stack = [s]
        while stack:
            v = stack.pop()
            for u in range(n):
                if A[v][u] == 0: 
                    continue
                want = A[v][u] * role[v]
                if role[u] == 0:
                    role[u] = want
                    stack.append(u)
                elif role[u] != want:
                    raise ValueError("تناقض در داده‌ها")

    # خروجی باینری: 1=شهروند، 0=مافیا (خاکستری اگر بود اینجا 1 نمی‌شود)
    return ''.join('1' if role[i] == 1 else '0' for i in range(n))

A = [
        [0, -1, -1, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, -1, -1, 1, 1, 1, -1],
        [1, 1, 1, 0, 0, 1, 1, 0, 0],
        [0, 1, 1, -1, -1, 1, 0, 0, -1],
        [0, -1, -1, 0, 1, -1, 0, 0, 0],
        [-1, 0, -1, 1, 1, 0, 0, -1, 0],
        [0, 1, 1, -1, 0, 1, 0, 1, 0],
        [0, 1, 1, -1, 0, 1, 1, 0, -1],
        [1, 1, 0, 0, 0, 1, 0, 1, -1],
    ]
print(solve_mafia(A))