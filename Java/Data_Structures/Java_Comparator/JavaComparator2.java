import java.util.Comparator;
import java.util.Scanner;
import java.util.Arrays;

// Write your Checker class here
class Checker implements Comparator<Player> {
  @Override
  public int compare(Player a, Player b) {    
    // Sort in DESCENDING order!
    int a_score = Integer.valueOf(a.score);
    int b_score = Integer.valueOf(b.score);
  
    if (a_score != b_score)
      return Integer.compare(b_score, a_score);
    else
      return a.name.compareTo(b.name);
  }
}

class Player {
  String name;
  int score;

  Player(String name, int score) {
    this.name = name;
    this.score = score;
  }
}

class Solution {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    Player[] player = new Player[n];
    Checker checker = new Checker();
        
    for (int i = 0; i < n; i++) {
      player[i] = new Player(sc.next(), sc.nextInt());
    }
    sc.close(); // Close Scanner object
     
    Arrays.sort(player, checker);
    for (int i = 0; i < player.length; i++) {
      System.out.printf("%s %s\n", player[i].name, player[i].score);
    }
  }
}
