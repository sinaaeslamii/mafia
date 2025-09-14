def bresenham_cells(a, b):
    x0, y0 = a; x1, y1 = b
    dx, dy = abs(x1-x0), abs(y1-y0)
    sx = 1 if x1 > x0 else -1 if x1 < x0 else 0
    sy = 1 if y1 > y0 else -1 if y1 < y0 else 0
    x, y = x0, y0
    cells = [(x, y)]
    if dx >= dy:                     # در تساوی، گام افقی (غیرمورب) را ترجیح می‌دهیم
        err = dx // 2
        for _ in range(dx):
            x += sx
            err -= dy
            if err < 0:
                y += sy
                err += dx
            cells.append((x, y))
    else:                             # در تساوی، گام عمودی (غیرمورب) را ترجیح می‌دهیم
        err = dy // 2
        for _ in range(dy):
            y += sy
            err -= dx
            if err < 0:
                x += sx
                err += dy
            cells.append((x, y))
    return cells

def count_unique_cells(points):
    seen = set()
    for i in range(len(points)-1):
        seg = bresenham_cells(points[i], points[i+1])
        if i: seg = seg[1:]           # نقطه مشترک ابتدای سگمنت بعدی را دوباره نشماریم
        seen.update(seg)
    return len(seen)

pts = [
[5, 27], [50, 35], [27, 16], [64, 60], [47, 41], [49, 74], [79, 5], [12, 52], [78, 64], [16, 69], [36, 50], [62, 40], [7, 24], [70, 26], [26, 60], [46, 68], [13, 37], [75, 26], [58, 58], [59, 57]]
print(count_unique_cells(pts))  # 22