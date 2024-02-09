import pywinctl as pwc
import time


def activeCB(active):
    print("NEW ACTIVE STATUS", active)
    if active == True:
        print("Новое окно")
        print()


def movedCB(pos):
    print("NEW POS", pos)


npw = pwc.getActiveWindow()
npw.watchdog.start(isActiveCB=activeCB)
npw.watchdog.setTryToFind(True)
print("Toggle focus and move active window")
print("Press Ctl-C to Quit")
i = 0
while True:
    try:
        if i == 50:
            npw.watchdog.updateCallbacks(isActiveCB=activeCB, movedCB=movedCB)
        if i == 100:
            npw.watchdog.updateInterval(0.1)
            npw.watchdog.setTryToFind(False)
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
    i += 1
npw.watchdog.stop()