# Problem 
"""
You are developing a big data batch job that takes some sort of data as input, and there is a pipeline of operations that need to occur on this data.



The data needs to pass the whole pipeline successfully in order to proceed with handling the data.



The pipeline consists of validation checks on data, formatting checks, data size checks, and finally personal information checks.



The batch job needs to fulfill the whole pipeline of checks and pass them successfully before proceeding with processing the data.


"""


from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    def __init__(self):
        self.next_handler : Optional['Handler'] = None


    def set_next(self, handler: 'Handler') -> 'Handler':
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass


class ValidationHandler(Handler):
    def handle(self, request: Any) -> bool:
        if request.get('data') is None:
            print ("Data is missing")
            return False
        print('Validation passed')
        if self.next_handler:
            return self.next_handler.handle(request)
        return True
    

class FormattingHandler(Handler):
    def handle(self, request: Any) -> bool:
        if request.get('format') is None:
            print ("Data is missing")
            return False
        print('Formatting passed')
        if self.next_handler:
            return self.next_handler.handle(request)
        return True


class DataSizeHandler(Handler):
    def handle(self, request: Any) -> bool:
        if request.get('data') is None:
            print ("Data is missing")
            return False
        print('Data size passed')
        if self.next_handler:
            return self.next_handler.handle(request)
        return True


class PersonalInfoHandler(Handler):
    def handle(self, request: Any) -> bool:
        if request.get('data') is None:
            print ("Data is missing")
            return False
        print('Personal info passed')
        if self.next_handler:
            return self.next_handler.handle(request)
        return True


class DataPipeline:
    def __init__(self):
        self.handler = ValidationHandler()
        self.handler.set_next(FormattingHandler()).set_next(DataSizeHandler()).set_next(PersonalInfoHandler())

    def process(self, request: Any):
        self.handler.handle(request)
    

if __name__ == '__main__':
    data = {
        'data': 'data',
        'format': 'json',
        'size': 100,
        'personal_info': 'name'
    }

    pipeline = DataPipeline()
    pipeline.process(data)
