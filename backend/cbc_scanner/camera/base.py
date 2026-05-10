from abc import ABC, abstractmethod

class BaseCamera(ABC):
    @abstractmethod
    def start(self):
        pass
        
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def test(self) -> bool:
        pass

    @abstractmethod
    def capture_array(self):
        pass

    @abstractmethod
    def capture_to_file(self, filepath: str):
        pass

    @abstractmethod
    def get_status(self) -> dict:
        pass

    @abstractmethod
    def set_controls(self, controls: dict):
        pass
