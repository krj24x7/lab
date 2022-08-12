class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of variables: channel, volume, and status
        """
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method to turn tv on and off.
        """
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method to turn tv channel up while tv is on.
        """
        if self.__status:
            if self.__channel + 1 > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to turn channel down while tv is on.
        """
        if self.__status:
            if self.__channel - 1 < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to turn tv volume up while tv is on.
        """
        if self.__status:
            if self.__volume + 1 > self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to turn tv volume down while tv is on.
        """
        if self.__status:
            if self.__volume - 1 < self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        pass

    def __str__(self) -> str:
        """
        Method to access tv status.
        :return: Tv's status, channel, and volume.
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
