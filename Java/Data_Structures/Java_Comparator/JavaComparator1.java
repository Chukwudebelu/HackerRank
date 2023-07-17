// Write your Checker class here
class Checker implements java.util.Comparator<Player> {
  @Override
  public int compare(Player a, Player b) {    
    // DESCENDING order sort!
    return (a.score == b.score) ? a.name.compareTo(b.name) : b.score - a.score;
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
    java.util.Scanner sc = new java.util.Scanner(System.in);
    int n = sc.nextInt();

    Player[] player = new Player[n];
    Checker checker = new Checker();
        
    for(int i = 0; i < n; i++){
      player[i] = new Player(sc.next(), sc.nextInt());
    }
    sc.close(); // Close Scanner object
     
    java.util.Arrays.sort(player, checker);
    for (int i = 0; i < player.length; i++) {
      System.out.printf("%s %s\n", player[i].name, player[i].score);
    }
  }
}
