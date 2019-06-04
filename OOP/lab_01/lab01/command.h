#ifndef COMMAND_H
#define COMMAND_H

#include "command_type.h"
#include "err.h"

err_t command(command_t cmd, const command_data_t *cmd_data);

#endif // COMMAND_H
