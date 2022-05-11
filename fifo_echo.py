
import sys
import os
from time import sleep

if __name__ == '__main__':
    fifo_in_path = sys.argv[1]
    fifo_out_path = sys.argv[2]

    fifo_in_fd = None
    fifo_out_fd = None

    try:
        while not os.path.exists(fifo_in_path) and not os.path.exists(fifo_out_path):
            print("Python Waiting for fifo creation")
            sleep(2)
        
        fifo_in_fd = os.open(fifo_in_path, os.O_RDONLY)
        fifo_out_fd = os.open(fifo_out_path, os.O_WRONLY)

        while True:
            data = os.read(fifo_in_fd, 256)
            print(f"Python data from fifo: {data}")
            if len(data) == 0:
                break
            print("Python Writing the same")
            os.write(fifo_out_fd, data)

    except Exception as e:
        raise
    finally:
        if fifo_out_fd is not None:
            os.close(fifo_out_fd)
        if fifo_in_fd is not None:
            os.close(fifo_in_fd)