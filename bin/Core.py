def LD(s, t):
    n = len(s)
    m = len(t)
    if n == 0:
        return m
    if m == 0:
        return n
        D = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(0, n + 1):
            D[i][0] = i
        for j in range(0, m + 1):
            D[0][j] = j

        for i in range(1, n + 1):
            s_i = s[i - 1]
            for j in range(1, m + 1):
                t_j = t[j - 1]
                if s_i == t_j:
                    cost = 0
                else:
                    cost = 1
                D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + cost)

        return D[n][m]