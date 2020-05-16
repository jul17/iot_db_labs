from abc import ABC, abstractmethod

class ViewDataInterface(ABC):

    @abstractmethod
    def view_data(self):
        pass
