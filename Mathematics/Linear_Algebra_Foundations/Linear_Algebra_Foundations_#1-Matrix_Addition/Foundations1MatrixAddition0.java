public class Solution {
    public static void main(String[] args) {
        int[][] M = {{1, 2, 3}, {2, 3, 4}, {1, 1, 1}};
        int[][] N = {{4, 5, 6}, {7, 8, 9}, {4, 5, 7}};
                
        for (int i = 0; i < M.length; i++) {
          for (int j = 0; j < M[i].length; j++) {
            System.out.println(M[i][j] + N[i][j]);
          }
        }
    }
}
