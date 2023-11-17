import pytest
from television import Television

class Test:

    def setup_method(self):
        """Start each test with the power on"""
        self.tv = Television()
        self.tv.power()

    def test_init(self):
        """initial status and values for tests"""
        assert self.tv._Television__status is True
        assert self.tv._Television__muted is False
        assert self.tv._Television__volume == 0
        assert self.tv._Television__channel == 0
        self.tv.power()
        assert self.tv._Television__status is False
        assert self.tv._Television__muted is False
        assert self.tv._Television__volume == 0
        assert self.tv._Television__channel == 0
        

    def test_power(self):
        """Power test"""
        self.tv.power()
        assert self.tv._Television__status is False
        self.tv.power()
        assert self.tv._Television__status is True

    def test_mute(self):
        """Test the mute function"""
        assert self.tv._Television__muted is False
        self.tv.volume_up()
        assert self.tv._Television__volume == 1
        self.tv.mute()
        assert self.tv._Television__muted is True
        assert self.tv._Television__volume == 0
        self.tv.mute()
        assert self.tv._Television__muted is False
        assert self.tv._Television__volume == 1
        self.tv.power()
        assert self.tv._Television__muted is False
        self.tv.mute()
        assert self.tv._Television__muted is False
        self.tv.power()
        assert self.tv._Television__volume == 1
        self.tv.mute()
        assert self.tv._Television__muted is True
        assert self.tv._Television__volume == 0
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv._Television__volume == 2
        self.tv.mute()
        self.tv.power()
        self.tv.power()
        assert self.tv._Television__volume == 0
        self.tv.mute()
        self.tv.mute()
        assert self.tv._Television__muted is True

    def test_channel_up(self):
        """Test channel up"""
        assert self.tv._Television__channel == 0
        self.tv.channel_up()
        assert self.tv._Television__channel == 1
        self.tv.channel_up()
        assert self.tv._Television__channel == 2
        self.tv.channel_up()
        assert self.tv._Television__channel == 3
        self.tv.channel_up()
        assert self.tv._Television__channel == 0

    def test_channel_down(self):
        """Test channel down"""
        assert self.tv._Television__channel == 0
        self.tv.channel_down()
        assert self.tv._Television__channel == 3
        self.tv.channel_down()
        assert self.tv._Television__channel == 2
        self.tv.channel_down()
        assert self.tv._Television__channel == 1
        self.tv.channel_down()
        assert self.tv._Television__channel == 0

    def test_volume_up(self):
        """Test volume up"""
        assert self.tv._Television__volume == 0
        self.tv.volume_up()
        assert self.tv._Television__volume == 1
        self.tv.volume_up()
        assert self.tv._Television__volume == 2
        self.tv.volume_up()
        assert self.tv._Television__volume == 2

    def test_volume_down(self):
        """Test volume down"""
        assert self.tv._Television__volume == 0
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv._Television__volume == 1
        self.tv.volume_down()
        assert self.tv._Television__volume == 0

    def test_combined(self):
        """Combined scenario test"""
        self.tv.volume_up()
        self.tv.channel_down()
        assert self.tv._Television__status is True
        assert self.tv._Television__volume == 1
        assert self.tv._Television__channel == 3
        self.tv.channel_up()
        self.tv.mute()
        self.tv.volume_up()
        self.tv.channel_up()
        self.tv.mute()
        assert self.tv._Television__volume == 0
        assert self.tv._Television__channel == 1
        self.tv.mute()
        assert self.tv._Television__volume == 2
        self.tv.channel_down()
        self.tv.mute()
        assert self.tv._Television__muted is True
        self.tv.channel_down()
        self.tv.volume_up()
        self.tv.channel_down()
        self.tv.volume_up()
        assert self.tv._Television__volume == 2
        assert self.tv._Television__channel == 2
        self.tv.power()
        assert self.tv._Television__volume == 2
        assert self.tv._Television__channel == 2
        assert self.tv._Television__status is False
        assert self.tv._Television__muted is False
        self.tv.power()
        assert self.tv._Television__volume == 2
        assert self.tv._Television__channel == 2
        
        