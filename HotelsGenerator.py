import json 

def read_hotels(filename: str):
    with open(filename, "r") as f:
        pos = 0
        while True:
            # read line by line until end of line or eof
            line = ""
            while True:
                f.seek(pos)
                c = f.read(1)
                if c == '\n':
                    pos += 1
                    break
                if c == '':
                    return
                line += c
                pos += 1

            doc = json.loads(line)
            name_unprocessed: str = doc.get("name")
            name_unprocessed = name_unprocessed.split("-")[0]
            name = name_unprocessed.removeprefix("Hotel ").strip()
            yield name



if __name__ == "__main__":
    before_time = time.time()
    before_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("[Before] Memory usage: ", before_mem/1024, "Mi")
    for h in read_hotels('barcelona_inline.json'):
        print(h)
    after_time = time.time()
    after_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("[After] Memory usage: ", after_mem/1024, "Mi")

    print(f"Memory increase: {((after_mem-before_mem)/before_mem) * 100}%\ttime: {after_time-before_time}s")
