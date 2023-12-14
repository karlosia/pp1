def f(player1,player2):
    def value(card):
        values={"A":10,"K":10,"Q":10,"J":10,"T":10}
        for card in card:
            if card.isdigit():
                return int(card)
            else:
                return values[card[0]]
            
    play1=(value(card) for card in player1)
    play2=(value(card) for card in player2)

    if sum(play1)>=sum(play2):
        return True
    else:
        return False

print(f("AJKKKKKK","AQT72") )    


