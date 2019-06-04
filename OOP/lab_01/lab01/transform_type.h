#ifndef TRANSFORM_TYPE_H
#define TRANSFORM_TYPE_H

typedef enum {
    TRANSLATION,
    ROTATION,
    SCALING
} transform_type_t;

typedef struct {
    int dx, dy, dz;
} translation_t;

typedef enum {
    X,
    Y,
    Z
} axis_t;

typedef struct {
    axis_t axis;
    double angel;
} rotation_t;

typedef struct {
    double scale;
} scaling_t;

#endif // TRANSFORM_TYPE_H
