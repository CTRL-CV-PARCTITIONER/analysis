from multiprocessing.pool import Pool
from multiprocessing import Process, Manager
from typing import Any
import os
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))


class Multiprocess(Process):
    """
        TODO:The generic multiprocess execution framework takes each item from a list and executes it in a specified function,
        TODO:Note that calls executing this class must be executed under if __name__ == "__main__"
        lines: Contains all the data that needs to be executed
        processes_number: Number of processes
        function: Executive function, At least one parameter is used to receive Element in lines
        params: Execute the parameters corresponding to the function, Pass in a tuple, and use the tuple parsing in the execution function
    """

    def __init__(self, lines: list, processes_number: int, function: callable, params: tuple = ()) -> None:
        self.lines = lines
        self.processes_number = processes_number
        self.function = function
        self.params = params
        self.Manager_queue = Manager().Queue()
        self.accumulator = []

    def __call__(self, *args: Any, **kwds: Any) -> list:
        self.get_queue()
        self.run()
        return self.accumulator
    
    def get_queue(self):
        for line in self.lines:
            self.Manager_queue.put(line)

    @staticmethod
    def get_result(Manager_queue, params, func, size, processes_number) -> Any:
        while not Manager_queue.empty():
            q = Manager_queue.get()
            cn = size - Manager_queue.qsize()
            if cn % 288 == 0:
                logger.info (f"child process id:{os.getpid()}  processes_number: {processes_number}  all: {size}  current execute id: {cn}")
            if params == ():
                result = func(q)
            else:
                result = func(q, params)
            return result

    def run(self):
        size = self.Manager_queue.qsize()
        p = Pool(self.processes_number)
        logger.info (f"host process id: {os.getppid()}  all: {size}")
        for _ in range(size):
            async_result = p.apply_async(self.get_result, args=(self.Manager_queue, self.params, self.function, size, self.processes_number))
            self.accumulator.append(async_result.get())
        p.close()
        p.join()
        logger.info("host process end !!!")