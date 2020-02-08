public class Core {

    public static int stringCompare(String s, String t) {
        int n = s.length();
        int m = t.length();
        if (n == 0) { return m; }
        if (m == 0) { return n; }
        int[][] D = new int[m + 1][n + 1];

        for (int i = 0; i <= n; i++) {
            D[0][i] = i;
        }
        for (int j = 0; j <= m; j++) {
            D[j][0] = j;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int minimum = D[i - 1][j] + 1;
                if (D[i][j - 1] + 1 < minimum) {
                    minimum = D[i][j - 1] + 1;
                }
                if (D[i - 1][j - 1] + cost(j - 1, i - 1, s, t) < minimum) {
                    minimum = D[i - 1][j - 1] + cost(j - 1, i - 1, s, t);
                }
                D[i][j] = minimum;
            }
        }

        return D[m][n];
    }

    private static int cost(int i, int j, String s, String t) {
        if (s.charAt(i) == t.charAt(j)) {
            return 0;
        }
        return 1;
    }

}