#ifndef COMMAND_TYPE_H
#define COMMAND_TYPE_H

#include <QPainter>

#include "transform_type.h"

typedef enum {
    LOAD,
    RENDER,
    TRANSFORM,
    SAVE,
    QUIT,
} command_t;

typedef struct {
    const char *load_path;
} load_data_t;

typedef struct {
    QPainter *paint;
} render_data_t;

typedef struct {
    transform_type_t transform_type;
    union {
        translation_t translation;
        rotation_t rotation;
        scaling_t scaling;
    };
} transform_data_t;

typedef struct {
    const char *save_path;
} save_data_t;

typedef union {
    load_data_t load_data;
    render_data_t render_data;
    transform_data_t transform_data;
    save_data_t save_data;
} command_data_t;

#endif // COMMAND_TYPE_H
