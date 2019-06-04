#include "file.h"

err_t open_file(FILE **fd, const char *path, const char *mode)
{
    err_t err = NONE_ERR;
    *fd = fopen(path, mode);
    if (*fd == NULL)
        err = FILE_OPEN_ERR;
    return err;
}

void close_file(FILE *fd)
{
    fclose(fd);
}
