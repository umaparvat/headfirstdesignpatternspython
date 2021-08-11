from abc import ABCMeta, abstractmethod
from tvs import Tv, RCATv, SonyTv

class Remote(metaclass=ABCMeta):
    def __init__(self, tvmodel:Tv):
        self.tvmodel = tvmodel

    def on(self):
        self.tvmodel.on()

    def off(self):
        self.tvmodel.off()

    def setchannel(self):
        self.tvmodel.tunechannel()


class SonyRemote(Remote):
    def setchannel(self):
        for each in self.tvmodel.tunechannel():
            print(each)


if __name__ == "__main__":
    sony_tv = SonyTv()
    myremote = SonyRemote(sony_tv)
    myremote.on()
    myremote.off()
    myremote.setchannel()