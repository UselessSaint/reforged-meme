#ifndef ERR_H
#define ERR_H

typedef enum {
    NONE_ERR,
    FILE_OPEN_ERR,
    INCORRECT_INPUT_ERR,
    MEMORY_ALLOC_ERR,
    NOT_LOAD_YET_ERR,
    UNKNOWN_CMD_ERR,
    COPY_ERR,
    NOT_ALLOC_YET_ERR
} err_t;

#endif // ERROR_H
