class TV():
    def __init__(self):
        self.is_on=False
        self.chanel_no= 1
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            print(f'TV is on, chanel {self.chanel_no}')
        else:
            print("TV is off")
            
tv=TV()
tv.show_status()
tv.turn_on()
tv.show_status()
               





