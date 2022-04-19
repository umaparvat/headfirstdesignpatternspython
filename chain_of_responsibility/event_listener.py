
class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = f"handle_{event}"

        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):

    def handle_close(self, event):
        print(f"Mainwindow: {event}")

    def handle_default(self, event):
        print(f"Mainwindow default: {event}")

class SendDialog(Widget):

    def handle_paint(self, event):
        print(f"send dialog: {event}")

class MsgText(Widget):

    def handle_down(self, event):
        print(f"msg text: {event}")


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    mt = MsgText(sd)

    for e in ['down', 'paint', 'unhandled', 'close']:
        evt = Event(e)
        print(f"\n sending event -{evt}- to Mainwindow")
        mw.handle(evt)
        print(f"\n sending event -{evt}- to send dialog")
        sd.handle(evt)
        print(f"\n sending event -{evt}- to msg text")
        mt.handle(evt)


if __name__ == "__main__":
    main()


