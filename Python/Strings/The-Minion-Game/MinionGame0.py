def minion_game(string):
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if string[i] in "AEIOU": # vowel
            player1 += (str_len)-i
        else: # consonant
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    else: # player1 == player2
        print("Draw")
  
if __name__ == '__main__':
    s = input()
    minion_game(s)
