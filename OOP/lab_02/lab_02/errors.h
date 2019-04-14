#ifndef ERRORS_H
#define ERRORS_H

#include "includes.h"

class MatrixErrorBase: public exception
{
public:
	virtual const char* what() const noexcept
	{
		return "Matrix error was catched";
	}
};

class MatrixSizeError: public MatrixErrorBase
{
public:
	const char* what() const noexcept
	{
		return "Matrix sizes have to be natural number";
	}
};

class MatrixIndexError: public MatrixErrorBase
{
public:
	const char* what() const noexcept
	{
		return "Incorrect indices";
	}
};

class MatrixAdditionError: public MatrixErrorBase
{
public:
	const char* what() const noexcept
	{
		return "Incorrect addition sizes";
	}
};

class MatrixDetError: public MatrixErrorBase
{
public:
	const char* what() const noexcept
	{
		return "Cols != Rows";
	}
};

class MatrixInverseError: public MatrixErrorBase
{
public:
	const char* what() const noexcept
	{
		return "Degenerate matrix";
	}
};

class MatrixMultiplicationError: public MatrixErrorBase
{
public:
	const char* what() const noexcept
	{
		return "Incorrect multiplication sizes";
	}
};

#endif // ERRORS_H
