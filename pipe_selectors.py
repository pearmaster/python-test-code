import threading
import selectors
import os
from time import sleep

def listener(read_fd):
    print("Starting listener thread")
    sel = selectors.DefaultSelector()
    print(sel.register(read_fd, selectors.EVENT_READ, "hello world"))

    pipe_r_fd = os.open("/tmp/jacobpipe", os.O_RDONLY)
    sel.register(pipe_r_fd, selectors.EVENT_READ, "hello pipe")

    # Don't use this, but we can solve problems by keeping it open
    # per https://forums.freebsd.org/threads/python-3-selectors-select-fails-for-named-pipes.62377/
    pipe_w_fd = os.open("/tmp/jacobpipe", os.O_WRONLY)

    running = True
    print("Waiting")
    while running:
        events = sel.select()
        print(f"Got {len(events)} events")
        for key, mask in events:
            if mask & selectors.EVENT_READ:
                print(os.read(key.fd, 64))
                print(key.data)
                if key.fd == read_fd:
                    running = False

    sel.unregister(read_fd)
    sel.unregister(pipe_r_fd)
    os.close(read_fd)
    os.close(pipe_r_fd)
    os.close(pipe_w_fd)
    sel.close()

def speaker(write_fd):
    print("Speaking")
    os.write(write_fd, b"This could be anything")
    sleep(1)
    os.close(write_fd)


if __name__ == '__main__':
    if os.path.exists("/tmp/jacobpipe"):
        os.remove("/tmp/jacobpipe")
    os.mkfifo("/tmp/jacobpipe", mode=0o777)

    read_fd, write_fd = os.pipe()

    listener_thread = threading.Thread(target=listener, kwargs={"read_fd":read_fd})
    listener_thread.start()

    sleep(60)

    speaker(write_fd)

