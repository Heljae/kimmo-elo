from math import erf

"""
class for calculating kimmo elo (kilo)
opponent = person on your right
opponent elo = the average of the people that have been 
on your right during the game
"""

class Elo:
    def __init__(self, prev_elo, opponent_elo, cups, new_palyer):
        self._prev = prev_elo
        self._opelo = opponent_elo
        self._cups = cups
        self._new = new_palyer

    def count(self):
        if self._new:
            return self.new_player_elo()
        return self.new_elo()

    def new_elo(self):
        kerroin = self.get_kerroin()
        result = self.get_result()
        expected = float(self.get_expected_per()/100)
        elo = self._prev + kerroin*(result-expected)+(1/10)

        return elo
    
    def new_player_elo(self):
        elo = float(self._opelo+800*(self.get_result()-0.5))

        return elo

    def get_kerroin(self):
        if self._prev < 1650:
            return 45
        if 1650 <= self._prev < 1750:
            return 40
        if 1750 <= self._prev < 1850:
            return 35
        if 1850 <= self._prev < 1950:
            return 30
        if 1950 <= self._prev < 2050:
            return 25
        if self._prev >= 2050:
            return 20

    def get_result(self):
        if self._cups < 3:
            return 1
        if 2 < self._cups < 5:
            return 0.5
        else:
            return 0

    def get_expected_per(self):
        pd = 50*(1+erf((self._prev-self._opelo)/400))

        if abs(pd) > 92:
            if pd<0:
                return -92
            else:
                return 92
        return pd
