import os
import sys
import threading


_sum = 0

def do_sum(path):
    global _sum
    sum = 0
    try:
        with open(path, 'rb',buffering=0) as f:
            byte = f.read(1)
            while byte:
                sum += int.from_bytes(byte, byteorder='big', signed=False)
                byte = f.read(1)
    except Exception as e:
        print(f"Error: {e}")
    
    _sum += sum


if __name__ == "__main__":
    paths = sys.argv[1:]
    for path in paths:
    #many error could be raised error. we don't care
        t = threading.Thread(target=do_sum, args=(path,))
        t.start()
        t.join()
# recuperar valor
        print(path + " : " + str(_sum))
