from abc import ABC, abstractmethod


class GamingConfigration:
    def __init__(self):
        self.quality = None
        self.sound_options = None
        self.control_preference = None

    def __str__(self):
        return f"Quality: {self.quality}, Sound: {self.sound_options}, Controls: {self.control_preference}"


class ConfigBuilder(ABC):
    @abstractmethod
    def set_quality(self):
        pass

    @abstractmethod
    def set_sound(self):
        pass

    @abstractmethod
    def set_controls(self):
        pass

    @abstractmethod
    def get_configuration(self):
        pass


class HighEndConfigBuilder(ConfigBuilder):
    def __init__(self):
        self.configuration = GamingConfigration()

    def set_quality(self):
        self.configuration.quality = "High"
        return self

    def set_sound(self):
        self.configuration.sound_options = "Dolby Atmos"
        return self

    def set_controls(self):
        self.configuration.control_preference = "Keyboard and Mouse"
        return self

    def get_configuration(self):
        return self.configuration
    

class LowEndConfigBuilder(ConfigBuilder):
    def __init__(self):
        self.configuration = GamingConfigration()

    def set_quality(self):
        self.configuration.quality = "Low"
        return self

    def set_sound(self):
        self.configuration.sound_options = "Stereo"
        return self

    def set_controls(self):
        self.configuration.control_preference = "Gamepad"
        return self

    def get_configuration(self):
        return self.configuration
    

class Director:
    def __init__(self, builder: ConfigBuilder):
        self.builder = builder

    def build(self):
        return self.builder.set_quality().set_sound().set_controls().get_configuration()


if __name__ == "__main__":
    high_end_builder = HighEndConfigBuilder()
    low_end_builder = LowEndConfigBuilder()

    director = Director(high_end_builder)
    high_end_config = director.build()

    director = Director(low_end_builder)
    low_end_config = director.build()

    print(high_end_config)
    print(low_end_config)