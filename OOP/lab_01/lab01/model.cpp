#include "model.h"

model_t init_model()
{
    return {init_points(), init_edges()};
}

err_t alloc_model(model_t *model, int points_count, int edges_count)
{
    err_t err = NONE_ERR;
    err = alloc_points(&model->points, points_count);
    if (err == NONE_ERR)
        err = alloc_edges(&model->edges, edges_count);
    return err;
}

void free_model(model_t *model)
{
    free_points(&model->points);
    free_edges(&model->edges);
}

bool is_alloc_model(model_t *model)
{
    return is_alloc_points(&model->points) && is_alloc_edges(&model->edges);
}

err_t load_model(model_t *model, const load_data_t *load_data)
{
    err_t err = NONE_ERR;

    FILE *fd;
    err = open_file(&fd, load_data->load_path, "r");
    if (err != NONE_ERR)
        return err;

    model_t tmp_model;
    err = get_model(&tmp_model, fd);

    if (err == NONE_ERR)
    {
        free_model(model);
        replace_model(model, &tmp_model);
    }

    free_model(&tmp_model);
    close_file(fd);
    return err;
}

err_t replace_model(model_t *model, model_t *tmp_model)
{
    err_t err = NONE_ERR;
    int points_count, edges_count;
    err = get_points_count(&points_count, &tmp_model->points);
    if (err == NONE_ERR)
        err = get_edges_count(&edges_count, &tmp_model->edges);
    if (err == NONE_ERR)
        err = alloc_model(model, points_count, edges_count);
    if (err == NONE_ERR)
        err = copy_model(model, tmp_model);
    if (err != NONE_ERR)
        free_model(model);
    return err;
}

err_t get_model(model_t *model, FILE *fd)
{
    err_t err;

    int point_count, edge_count;
    err = get_model_header(&point_count, &edge_count, fd);

    if (err == NONE_ERR)
        err = alloc_model(model, point_count, edge_count);
    if (err == NONE_ERR)
        err = get_points(&model->points, fd);
    if (err == NONE_ERR)
        err = get_edges(&model->edges, fd);

    if (err != NONE_ERR)
        free_model(model);

    return err;
}

err_t copy_model(model_t *model, model_t *copied_model)
{
    if (!is_alloc_model(model) || !is_alloc_model(copied_model))
        return COPY_ERR;

    err_t err = copy_points(&model->points, &copied_model->points);
    if (err == NONE_ERR)
        err = copy_edges(&model->edges, &copied_model->edges);
    return err;
}

err_t get_model_header(int *point_count, int *edge_count, FILE *fd)
{
    err_t err = fget_int(point_count, fd);
    if (err == NONE_ERR)
        err = fget_int(edge_count, fd);
    if (err == NONE_ERR)
        if (*point_count <= 0 || *edge_count <=0)
            err = INCORRECT_INPUT_ERR;
    return err;
}

err_t render_model(model_t *model, const render_data_t *render_data)
{
    if (!is_alloc_model(model))
        return NOT_LOAD_YET_ERR;

    draw_edges(&model->points, &model->edges, render_data);
    return NONE_ERR;
}

err_t transform_model(model_t *model, const transform_data_t *transform_data)
{
    if (!is_alloc_model(model))
        return NOT_LOAD_YET_ERR;

    err_t err = NONE_ERR;

    switch (transform_data->transform_type)
    {
        case TRANSLATION:
            err = translate_points(&model->points, transform_data->translation);
            break;
        case ROTATION:
            err = rotate_points(&model->points, transform_data->rotation);
            break;
        case SCALING:
            err = scale_points(&model->points, transform_data->scaling);
            break;
        default:
            err = UNKNOWN_CMD_ERR;
            break;
    }

    return err;
}

err_t save_model(model_t *model, const save_data_t *save_data)
{
    if (!is_alloc_model(model))
        return NOT_LOAD_YET_ERR;

    FILE *fd;
    err_t err = open_file(&fd, save_data->save_path, "w");
    if (err == NONE_ERR)
    {
        put_model(model, fd);
        close_file(fd);
    }

    return err;
}

int put_model(model_t *model, FILE *fd)
{
    int count = 0;

    count += put_model_header(&model->points, &model->edges, fd);
    count += fprintf(fd, "\n");
    count += put_points(&model->points, fd);
    count += fprintf(fd, "\n");
    count += put_edges(&model->edges, fd);

    return count;
}

int put_model_header(points_t *points, edges_t *edges, FILE *fd)
{
    int points_count, edges_count;
    get_points_count(&points_count, points);
    get_edges_count(&edges_count, edges);
    return fprintf(fd, "%d %d\n", points_count, edges_count);
}
