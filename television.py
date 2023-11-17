class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the Television remote."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__prev_volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Press the power button for the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the television."""
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = self.MIN_VOLUME
            else:
                if self.__prev_volume is not None:
                    self.__volume = self.__prev_volume
            self.__muted = not self.__muted
            
    def channel_up(self) -> None:
        """Channel up on the television."""
        if self.__status:
            self.__channel = (self.__channel + 1) % 4

    def channel_down(self) -> None:
        """Channel down on the television."""
        if self.__status:
            self.__channel = (self.__channel - 1) % 4

    def volume_up(self) -> None:
        """Increase the volume of the television."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = min(self.__prev_volume + 1, self.MAX_VOLUME)
            else:
                self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decrease the volume of the television."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = max(self.__prev_volume - 1, self.MIN_VOLUME)
            else:
                self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """
        Return a string of the Television status.
        :return: returns tv status.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
