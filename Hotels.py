import json
import os
import resource
import time
from typing import List, TypeVar


class ExtractCityHotelsData:
    filename: str
    city: str
    
    def __init__(self, filename: str, city: str):
        self.filename = filename
        self.city = city
        self._hotels: List[str] = []
    
    @property
    def hotels(self):
        with open(self.filename) as f:
            ds = json.load(f)
            for doc in ds:
                name_unprocessed: str = doc.get("name")
                name_unprocessed = name_unprocessed.split("-")[0]
                name = name_unprocessed.removeprefix("Hotel ").strip()
                self._hotels.append(name)
        
        return self._hotels


if __name__ == "__main__":
    city_hotels = ExtractCityHotelsData('barcelona.json', 'Barcelona')
    before_time = time.time()
    before_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("[Before] Memory usage: ", before_mem/1024, "Mi")
    for h in city_hotels.hotels:
        print(h)
    after_time = time.time()
    after_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("[After] Memory usage: ", after_mem/1024, "Mi")

    print(f"Memory increase: {((after_mem-before_mem)/before_mem) * 100}%\ttime: {after_time-before_time}s")
