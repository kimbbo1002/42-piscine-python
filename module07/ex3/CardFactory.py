from abc import ABC, abstractmethod

class CardFactory(ABC):
    @abstractmethod
    def create_cerature(self, name_or_power: str | int | None = None):
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None):
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None):
        pass

    @abstractmethod
    def create_themed_deck(self, size: int):
        pass

    @abstractmethod
    def get_supported_types(self):
        pass
