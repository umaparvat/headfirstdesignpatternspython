from abc import ABCMeta, abstractmethod
class Tv(metaclass=ABCMeta):
    @abstractmethod
    def on(self):
        raise NotImplementedError
    @abstractmethod
    def off(self):
        raise NotImplementedError

    @abstractmethod
    def tunechannel(self, *args, **kwargs):
        raise NotImplementedError


class SonyTv(Tv):
    def __init__(self):
        self.name = "SONY 4k"
        self.channels = ["CARTOON", "STAR MOVIES", "ESPN"]

    def on(self):
        print(f"{self.name} turned on")

    def off(self):
        print(f"{self.name} powered off")

    def tunechannel(self, *args, **kwargs):
        return channeliterator(self.channels)

class RCATv(Tv):
    def __init__(self):
        self.name = "RCA"
        self.channels = {1: "SUN", 2: "VIJAY"}

    def on(self):
        print("logo:$$$")
        print(f"{self.name} No1. tv")
        print("powering on")

    def off(self):
        print("see you soon")

    def tunechannel(self, *args, **kwargs):
        return self.channels




class channeliterator:
    def __init__(self, channels):
        self.current = 0
        self.channels = channels

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.channels):
            item = self.channels[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration



