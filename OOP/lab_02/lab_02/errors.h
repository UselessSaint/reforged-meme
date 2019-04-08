#ifndef ERRORS_H
#define ERRORS_H

#include "includes.h"

class Matrix_size_error: public exception
{
public:
	const char* what() const noexcept
	{
		return "Matrix sizes have to be natural number";
	}
};

class Matrix_initializer_error: public exception
{
public:
	const char* what() const noexcept
	{
		return "You are trying to initialize more values than the matrix can hold";
	}
};

#endif // ERRORS_H
