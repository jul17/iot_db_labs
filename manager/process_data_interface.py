from abc import ABC, abstractmethod

class ProcessData(ABC):

    @abstractmethod
    def process_data(self, show_data_method):
        pass