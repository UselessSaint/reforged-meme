#ifndef ITERATOR_H
#define ITERATOR_H

#include "includes.h"

template <typename T>
class MatrixIterator
{
protected:
	//int rows = 0, cols = 0;
	T* cur_elem = nullptr;
	//T **mtr = nullptr;
public:
	virtual bool operator ==(const MatrixIterator& second)
	{
		return cur_elem == second.cur_elem;
	}

	virtual bool operator !=(const MatrixIterator& second)
	{
		return cur_elem != second.cur_elem;
	}

	virtual T& operator *()
	{
		return *cur_elem;
	}
};

template <typename T>
class MatrixIteratorRow: virtual public MatrixIterator<T>
{
private:
	//int& rows = MatrixIterator<T>::rows, cols = MatrixIterator<T>::cols;
	int rows = 0, cols = 0;
	T** mtr = nullptr; //MatrixIterator<T>::mtr;
	int cur_row = 0, cur_col = 0;
public:
	MatrixIteratorRow(int n, int m, T** matrix)
	{
		rows = n;
		cols = m;
		mtr = matrix;

		MatrixIterator<T>::cur_elem = &(mtr[cur_row][cur_col]);
	}

	MatrixIteratorRow& operator ++()
	{
		if (cur_col == cols-1)
		{
			cur_col = 0;
			cur_row++;
		}
		else
		{
			cur_col++;
		}
		MatrixIterator<T>::cur_elem = &(mtr[cur_row][cur_col]);
		return *this;
	}
};

template <typename T>
class MatrixIteratorColumn: virtual public MatrixIterator<T>
{
private:
	//int& rows = MatrixIterator<T>::rows, cols = MatrixIterator<T>::cols;
	int rows = 0, cols = 0;
	T** mtr = nullptr; //MatrixIterator<T>::mtr;
	int cur_row = 0, cur_col = 0;
public:
	MatrixIteratorColumn(int n, int m, T** matrix)
	{
		rows = n;
		cols = m;
		mtr = matrix;

		MatrixIterator<T>::cur_elem = &(mtr[cur_row][cur_col]);
	}

	MatrixIteratorColumn& operator ++()
	{
		if (cur_row == rows-1)
		{
			cur_row = 0;
			cur_col++;
		}
		else
		{
			cur_row++;
		}
		MatrixIterator<T>::cur_elem = &(mtr[cur_row][cur_col]);
		return *this;
	}
};

template  <typename T>
class MatrixIteratorEnd: virtual public MatrixIterator<T>
{
private:
	T** mtr = nullptr;// MatrixIterator<T>::mtr;
public:
	MatrixIteratorEnd(int n, int m, T** matrix)
	{
		mtr = matrix;

		MatrixIterator<T>::cur_elem = &(mtr[n-1][m-1]);
	}
};

#endif // ITERATOR_H
