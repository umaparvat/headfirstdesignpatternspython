"""
Scenario: The Remote functionality is same for all the Smart TV.
But There can be different TV brands Sony, LG, Samsung.
How to combine Remote with Tv.
So that whenever user presses a button the TV respond.

Solution: Create Remote and bridge with TV.
Below is the bridge pattern used to provide the solution.

The Remote can work irrespective of TV.
Whatever varies in the remote class you can override in concreteRemote class.


"""
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
        return self.tvmodel.tunechannel()


class SonyRemote(Remote):
    def setchannel(self):
        for each in self.tvmodel.tunechannel():
            print(each)

class RCARemote(Remote):
    def __init__(self, tvmodel):
        super().__init__(tvmodel)


if __name__ == "__main__":
    print("\nSony\n")
    sony_tv = SonyTv()
    myremote = SonyRemote(sony_tv)
    myremote.on()
    myremote.off()
    myremote.setchannel()
    print(f"\nRCA\n")
    rca_tv = RCATv()
    rca_remote = RCARemote(rca_tv)
    rca_remote.on()
    rca_remote.off()
    for each in rca_remote.setchannel():
        print(each)