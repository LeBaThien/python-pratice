class Amplifier:
    def on(self):
        print("Amplifier on")

    def off(self):
        print("Amplifier off")

    def set_volume(self, volume):
        print(f"Setting volume to {volume}")


class Tuner:
    def on(self):
        print("Tuner on")

    def off(self):
        print("Tuner off")

    def set_frequency(self, frequency):
        print(f"Setting frequency to {frequency}")


class CDPlayer:
    def on(self):
        print("CD Player on")

    def off(self):
        print("CD Player off")

    def play(self, cd):
        print(f"Playing {cd}")

class HomeTheaterFacade:
    def __init__(self, amplifier, tuner, cd_player):
        self._amplifier = amplifier
        self._tuner = tuner
        self._cd_player = cd_player

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self._amplifier.on()
        self._amplifier.set_volume(5)
        self._cd_player.on()
        self._cd_player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self._cd_player.off()
        self._amplifier.off()

    def listen_to_radio(self, frequency):
        print("Tuning in the airwaves...")
        self._tuner.on()
        self._tuner.set_frequency(frequency)
        self._amplifier.on()
        self._amplifier.set_volume(5)

    def end_radio(self):
        print("Shutting down the tuner...")
        self._tuner.off()
        self._amplifier.off()
def main():
    amplifier = Amplifier()
    tuner = Tuner()
    cd_player = CDPlayer()

    home_theater = HomeTheaterFacade(amplifier, tuner, cd_player)

    home_theater.watch_movie("Inception")
    home_theater.end_movie()
    home_theater.listen_to_radio(89.1)
    home_theater.end_radio()

if __name__ == "__main__":
    main()
