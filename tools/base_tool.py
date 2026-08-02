from abc import ABC, abstractmethod


class BaseTool(ABC):

    name: str

    @abstractmethod
    def run(self, question: str):
        """
        Execute the tool.
        """
        pass