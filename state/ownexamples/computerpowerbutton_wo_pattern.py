import enum

class Power(enum.Enum):
    ON = 1
    OFF = 2
    HIBERNATE = 3
    SLEEP = 4
    RESTART = 5

class ComputerPowerButton:
    def __init__(self):
        self.current = Power.OFF

    def turn_on(self):
        print("powered on")

    def restart(self):
        print("restarting")

    def turn_off(self):
        print("turning off")

    def hibernate(self):
        print("going to hibernate mode")

    def sleep(self):
        print("going to sleep")

    def buttonpressed(self, option):
        """
        Here it's like a switch case which changes the instance variable value
        as well as perform some behavioural changes.
        the states are definite states and well known.
        :param option:
        :return:
        """
        if option == Power.OFF and self.current == Power.ON:
            self.turn_off()
            self.current = Power.OFF
        elif option == Power.ON and self.current not in [Power.ON, Power.RESTART]:
            self.turn_on()
            self.current = Power.ON
        elif option == Power.SLEEP and self.current == Power.ON:
            self.sleep()
            self.current = Power.SLEEP
        elif option == Power.HIBERNATE and self.current == Power.ON:
            self.hibernate()
            self.current = Power.HIBERNATE
        elif option == Power.RESTART and self.current == Power.ON:
            self.restart()
            self.current = Power.RESTART
        else:
            print(f"current state is :{self.current} and you pressed: {option} is not possible to do")


if __name__ == "__main__":
    mycomputer_power = ComputerPowerButton()
    mycomputer_power.buttonpressed(option=Power.ON)
    #mycomputer_power.buttonpressed(option=Power.ON)
    #mycomputer_power.buttonpressed(option=Power.RESTART)
    mycomputer_power.buttonpressed(Power.SLEEP)
    mycomputer_power.buttonpressed(Power.ON)
    mycomputer_power.buttonpressed(Power.HIBERNATE)
    mycomputer_power.buttonpressed(Power.ON)
    mycomputer_power.buttonpressed(Power.OFF)

