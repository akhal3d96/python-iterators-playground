import json
import os
import time
import resource
from typing import List, TypeVar


class ExtractCityHotelsData:
    filename: str
    city: str
    
    def __init__(self, filename: str, city: str):
        self.filename = filename
        self.city = city
        self._pos = 0
    
    def __iter__(self):
        self._pos = 0
        return self
    
    def __next__(self):
        with open(self.filename, "r") as f:
            
            # read line by line until end of line or eof
            line = ""
            while True:
                f.seek(self._pos)
                c = f.read(1)
                if c == '\n':
                    self._pos += 1
                    break
                if c == '':
                    raise StopIteration
                line += c
                self._pos += 1

            doc = json.loads(line)
            name_unprocessed: str = doc.get("name")
            name_unprocessed = name_unprocessed.split("-")[0]
            name = name_unprocessed.removeprefix("Hotel ").strip()
            return name



if __name__ == "__main__":
    
    barcelona = ExtractCityHotelsData("barcelona_inline.json", "Barcelona")

    before_time = time.time()
    before_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("[Before] Memory usage: ", before_mem/1024, "Mi")
    for h in barcelona:
        print(h)
    after_time = time.time()
    after_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("[After] Memory usage: ", after_mem/1024, "Mi")

    print(f"Memory increase: {((after_mem-before_mem)/before_mem) * 100}%\ttime: {after_time-before_time}s")
