import random

class Filter(object):
    def turnOff(self):
        print( "Filter is disabled")


    def turnOn(self):
        print("Filter is enabled")


class Top():
    def attach(self):
        print("top is attavched")

    def remove(self):
        print(("top is removed"))

class Container():
    def fillwater(self):
        print( "water is filled up to max quantity")
    def removewater(self):
        print( "water is entirely removed")


class FancyBrita(object):
    def __init__(self):
        self._filter=Filter()
        self._container=Container()
        self._top=Top()

    def first_job(self):
        self._top.remove()
        self._container.fillwater()
        self._filter.turnOn()


def main():
    fb=FancyBrita()
    fb.first_job()

if __name__ == '__main__':
    main()




