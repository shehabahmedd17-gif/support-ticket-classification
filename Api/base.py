from abc import ABC, abstractmethod
from .model import GenerationRequest


class LMM (ABC):

    @abstractmethod
    def generate(self,request: GenerationRequest):
       raise NotImplementedError

    