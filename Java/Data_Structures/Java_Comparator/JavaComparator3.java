import java.util.*;

// Write your Checker class here
abstract class Checker implements Comparator<Player> {
  public static Comparator<Player> studentComparator = new Comparator<Player>() {
    @Override
    public int compare(Player a, Player b) {
      return (int) ((a.score != b.score) ? b.score - a.score : a.name.compareTo(b.name));
    }
  };
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
        
    for (int i = 0; i < n; i++) {
      player[i] = new Player(sc.next(), sc.nextInt());
    }
    sc.close(); // Close Scanner object
     
    Arrays.sort(player, Checker.studentComparator);
    for (int i = 0; i < player.length; i++) {
      System.out.printf("%s %s\n", player[i].name, player[i].score);
    }
  }
}
