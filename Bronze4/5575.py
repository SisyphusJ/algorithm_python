for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    ft = 3600 * h1 + 60 * m1 + s1
    lt = 3600 * h2 + 60 * m2 + s2
    tc = lt - ft
    h = tc // 3600
    m = (tc % 3600) // 60
    s = (tc % 3600) % 60
    print(h, m, s)
