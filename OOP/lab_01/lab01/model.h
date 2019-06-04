#ifndef MODEL_H
#define MODEL_H

#include <cstdio>
#include <cstdlib>

#include "err.h"
#include "command_type.h"
#include "points.h"
#include "edges.h"
#include "file.h"
#include "io.h"
#include "draw.h"

typedef struct {
    points_t points;
    edges_t edges;
} model_t;

model_t init_model();

err_t alloc_model(model_t *model, int points_count, int edges_count);
void free_model(model_t *model);

bool is_alloc_model(model_t *model);

err_t load_model(model_t *model, const load_data_t *load_data);
err_t get_model(model_t *model, FILE *fd);
err_t get_model_header(int *point_count, int *edge_count, FILE *fd);
err_t copy_model(model_t *model, model_t *copied_model);
err_t replace_model(model_t *model, model_t *tmp_model);

err_t render_model(model_t *model, const render_data_t *render_data);

err_t transform_model(model_t *model, const transform_data_t *transform_data);

err_t save_model(model_t *model, const save_data_t *save_data);
int put_model(model_t *model, FILE *fd);
int put_model_header(points_t *points, edges_t *edges, FILE *fd);

#endif // MODEL_H
