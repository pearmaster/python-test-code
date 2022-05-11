
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/select.h>

int main(int argc, char** argv) {

    const char* write_pipe_path = "/tmp/to_python";
    const char* read_pipe_path = "/tmp/from_python";

    mkfifo(write_pipe_path, 0666);
    mkfifo(read_pipe_path, 0666);

    printf("C opening write fifo\n");
    int write_fd = open(write_pipe_path, O_WRONLY);
    printf("C opening read fifo\n");
    int read_fd = open(read_pipe_path, O_RDONLY);
    char out_buf[10];
    char in_buf[10];

    for(int a = 0; a < 10; a++) {
        printf("C writing %d\n", a);
        int len = snprintf(out_buf, sizeof(out_buf), "%d\n", a);
        write(write_fd, out_buf, len);
        sleep(1);
        int bytes_read = read(read_fd, in_buf, sizeof(in_buf));
        in_buf[bytes_read] = '\0';
        printf("C received: %s\n", in_buf);
    }

    close(write_fd);

    remove(write_pipe_path);
    remove(read_pipe_path);
}