class IndianMetric(object):
    def temperature(self):pass
    def distance(self):pass
    def date(self):pass


class IndianMouth(IndianMetric):
    def __init__(self,celsius=30,kilometer=10,date=100):
        self._celsius=celsius
        self._kilometer=kilometer
        self._date=date

    def temperature(self):
        print(f'''temperature is {self._celsius}, degrees''')

    def distance(self):
        print(f'''Distance is {self._kilometer}, far''')

    def date(self):
        print(f'''weight is {self._date}, heavy''')

class NRIMetric(object):
    def temperature(self): pass
    def distance(self): pass
    def date(self): pass

class NRIMouth(NRIMetric):
    _indianmouth=IndianMouth()
    def __init__(self,_indianmouth):
        self._indianmouth=_indianmouth
        self._farenheit=1.8*self._indianmouth._celsius+32
        self._miles=0.6213*self._indianmouth._kilometer
        self._date=2.2*self._indianmouth._date

    def temperature(self):
        print(f'''temperature is {self._farenheit}, degrees''')

    def distance(self):
        print(f'''Distance is {self._miles}, far''')

    def weight(self):
        print(f'''weight is {self._date}, heavy''')

def main():
    hardik=IndianMouth()
    nri_hardik=NRIMouth(hardik)
    nri_hardik.temperature()
    nri_hardik.distance()
    nri_hardik.weight()

if __name__ == '__main__':
    main()









