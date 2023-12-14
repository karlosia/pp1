def f(player1,player2):
    def card_value(card):
        values={"A":10,"K":10,"Q":10,"J":10,"T":10}
        if card.isdigit():
            return int(card)
        else:
            return values[card[0]]

    play1_values=(card_value(card)for card in player1)
    play2_values=(card_value(card)for card in player2)

    if sum(play1_values)>=sum(play2_values):
        return True
    else:
        return False


print(f("AJ972","AQT72"))
