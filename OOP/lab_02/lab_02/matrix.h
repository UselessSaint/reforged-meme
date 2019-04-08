#ifndef MATRIX_H
#define MATRIX_H

#include "includes.h"
#include "errors.h"
#include "iterator.h"

template <typename T>
class Matrix
{
private:
	T** mtr = nullptr;
	int rows = 0, cols = 0;

public:
	Matrix(int n, int m)
	{
		if (n < 0 || m < 0)
		{
			throw Matrix_size_error();
		}

		rows = n;
		cols = m;

		mtr = new T* [rows];

		for (int i = 0; i < cols; i++)
		{
			mtr[i] = new T [cols];
			fill_n(mtr[i], cols, 0);
		}
	}

	Matrix(int n, int m, initializer_list<T> list)
	{
		rows = n;
		cols = m;

		if (int(list.size()) > n*m)
		{
			throw Matrix_initializer_error();
		}

		rows = n;
		cols = m;

		mtr = new T* [rows];

		for (int i = 0; i < cols; i++)
		{
			mtr[i] = new T [cols];
			fill_n(mtr[i], cols, 0);
		}

		auto it = list.begin();

		for (int i = 0; i < rows; i++)
		{
			for (int j = 0; j < cols; j++)
			{
				if (it != list.end())
				{
					mtr[i][j] = *it;
					it++;
				}
				else
				{
					mtr[i][j] = 0;
				}
			}
		}
	}

	~Matrix()
	{
		cout << "Here i'm boys and girls.";

		for (int i = 0; i < rows; i++)
		{
			delete [] mtr[i];
		}
		delete [] mtr;
	}

	void print()
	{
		auto it = this->beginRow();
		auto end = this->end();

		while (it != end)
		{
			cout << *it << " ";
			++it;
		}
		cout << *end;
	}

	MatrixIteratorRow<T> beginRow()
	{
		return MatrixIteratorRow<T>(rows, cols, mtr);
	}

	MatrixIteratorColumn<T> beginColumn()
	{
		return MatrixIteratorColumn<T>(rows, cols, mtr);
	}

	MatrixIterator<T> end()
	{
		return MatrixIteratorEnd<T>(rows, cols, mtr);
	}
};

#endif // MATRIX_H
