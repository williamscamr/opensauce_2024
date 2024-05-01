from mindstorms import Hub
hub = Hub()
print(hub.battery.current())
while True:
    while hub.motion.gesture() != hub.motion.TAPPED:
        pass
    hub.sound.play('/extra_files/Hello')

