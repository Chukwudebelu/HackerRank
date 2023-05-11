import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  public static void main(String[] args) {
    // [1 2 3]
    // [2 3 4]
    // [1 1 1]
    int[][] matrix1 = {{1, 2, 3}, {2, 3, 4}, {1, 1, 1}};
    // [4 5 6]
    // [7 8 9]
    // [4 5 7]
    int[][] matrix2 = {{4, 5, 6}, {7, 8, 9}, {4, 5, 7}};
    
    System.out.println(matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0] + matrix1[0][2]*matrix2[2][0]); // A
    System.out.println(matrix1[0][0]*matrix2[0][1] + matrix1[0][1]*matrix2[1][1] + matrix1[0][2]*matrix2[2][1]); // B
    System.out.println(matrix1[0][0]*matrix2[0][2] + matrix1[0][1]*matrix2[1][2] + matrix1[0][2]*matrix2[2][2]); // C
    System.out.println(matrix1[1][0]*matrix2[0][0] + matrix1[1][1]*matrix2[1][0] + matrix1[1][2]*matrix2[2][0]); // D
    System.out.println(matrix1[1][0]*matrix2[0][1] + matrix1[1][1]*matrix2[1][1] + matrix1[1][2]*matrix2[2][1]); // E
    System.out.println(matrix1[1][0]*matrix2[0][2] + matrix1[1][1]*matrix2[1][2] + matrix1[1][2]*matrix2[2][2]); // F
    System.out.println(matrix1[2][0]*matrix2[0][0] + matrix1[2][1]*matrix2[1][0] + matrix1[2][2]*matrix2[2][0]); // G
    System.out.println(matrix1[2][0]*matrix2[0][1] + matrix1[2][1]*matrix2[1][1] + matrix1[2][2]*matrix2[2][1]); // H
    System.out.println(matrix1[2][0]*matrix2[0][2] + matrix1[2][1]*matrix2[1][2] + matrix1[2][2]*matrix2[2][2]); // I
  }
}
