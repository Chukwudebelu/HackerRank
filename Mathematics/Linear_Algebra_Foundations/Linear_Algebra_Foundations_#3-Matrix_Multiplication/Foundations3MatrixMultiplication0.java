public class Solution {
  public static void main(String[] args) {
    // [1 2]
    // [2 3]
    int[][] matrix1 = {{1, 2}, {2, 3}};
    // [4 5]
    // [7 8]
    int[][] matrix2 = {{4, 5}, {7, 8}};
    
    System.out.println(matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0]); // A
    System.out.println(matrix1[0][0]*matrix2[0][1] + matrix1[0][1]*matrix2[1][1]); // B
    System.out.println(matrix1[1][0]*matrix2[0][0] + matrix1[1][1]*matrix2[1][0]); // C
    System.out.println(matrix1[1][0]*matrix2[0][1] + matrix1[1][1]*matrix2[1][1]); // D
  }
}
