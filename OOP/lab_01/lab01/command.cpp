#include "command.h"
#include "model.h"

err_t command(command_t cmd, const command_data_t *cmd_data)
{
    static model_t model = init_model();
    err_t err = NONE_ERR;

    switch (cmd)
    {
        case LOAD:
            err = load_model(&model, &cmd_data->load_data);
            break;
        case RENDER:
            err = render_model(&model, &cmd_data->render_data);
            break;
        case TRANSFORM:
            err = transform_model(&model, &cmd_data->transform_data);
            break;
        case SAVE:
            err = save_model(&model, &cmd_data->save_data);
            break;
        case QUIT:
            free_model(&model);
            break;
        default:
            err = UNKNOWN_CMD_ERR;
            break;
    }

    return err;
}
