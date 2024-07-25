import sys
import threading

sum = 0
semaphore = threading.Semaphore(1)

def do_sum(path):
    _sum = 0
    global sum
    with open(path, 'rb') as f:
        byte = f.read(1)
        while byte:
            _sum += int.from_bytes(byte, byteorder='big', signed=False)
            byte = f.read(1)
    # controle de admissão
    semaphore.acquire()
    sum += _sum
    semaphore.release()

def controlled_sum(path):
   semaphore_2.acquire()
   do_sum(path)
   semaphore_2.release()


#many error could be raised error. we don't care       
if __name__ == "__main__":
    paths = sys.argv[1:]
    threads = []

    semaphore_2 = threading.Semaphore(max(1, len(paths)) // 2)

    for path in paths:
        try:
            thread = threading.Thread(target=controlled_sum, args=(path,))
            threads.append(thread)
            thread.start()
        except Exception as e:
            print(f"Erro ao processar {path}: {e}")
    
    for thread in threads:
          thread.join()
    print(sum)
