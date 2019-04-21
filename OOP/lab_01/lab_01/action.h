#ifndef ACTION_H
#define ACTION_H

#include "model.h"

enum command
{
	LOAD = 0
};

union input_data
{
	model input_model;
};

void do_action(command, const union input_data);
void load(model &curr_model, model &inp_model);
void read_file(char *file_name);

#endif // ACTION_H
