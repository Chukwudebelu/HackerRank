class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int q = in.nextInt();
        for(int i = 0; i < q; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            for (int j = 1; j <= n; j++){
              a += b;
              System.out.printf("%d ", a);
              b *= 2;
            }
            System.out.println();
        }
        in.close();
    }
}
