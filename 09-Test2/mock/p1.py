def f(player1,player2):
    def card_value(card):
        values={"A":10,"K":10,"Q":10,"J":10,"T":10}
        for card in card:
            if card.isdigit():
                return int(card)
            else:
                return values[card[0]]
            
    play1_value=(card_value(card) for card in player1)
    play2_value=(card_value(card) for card in player2)  

    if sum(play1_value)>=sum(play2_value):
        return True
    else:
        return False

print(f("AJ972","AQT72"))      
        



        

    