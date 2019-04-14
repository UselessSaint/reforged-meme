#ifndef ITERATOR_H
#define ITERATOR_H

#include "includes.h"

template <typename T>
class MatrixIteratorBase
{
protected:
	T* cur_item = nullptr;
public:
	bool operator ==(const MatrixIteratorBase& second)
	{
		return cur_item == second.cur_item;
	}

	bool operator !=(const MatrixIteratorBase& second)
	{
		return !(cur_item == second.cur_item);
	}

	T& operator *()
	{
		return *cur_item;
	}
};

template <typename T>
class MatrixIteratorRow: public MatrixIteratorBase<T>
{
public:
	MatrixIteratorRow(T* item)
	{
		setCurItem(item);
	}

	~MatrixIteratorRow() {}

	MatrixIteratorRow& operator++()
	{
		T* item = getCurItem();
		item++;
		setCurItem(item);

		return *this;
	}

	MatrixIteratorRow operator++(int)
	{
		auto old_it = MatrixIteratorRow(getCurItem());

		T* item = getCurItem();
		item++;
		setCurItem(item);

		return old_it;
	}

	void setCurItem(T* item)
	{
		MatrixIteratorBase<T>::cur_item = item;
	}

	T* getCurItem()
	{
		return MatrixIteratorBase<T>::cur_item;
	}
};

template <typename T>
class MatrixIteratorColumn: public MatrixIteratorBase<T>
{
private:
	int cur_row = 0, cur_col = 0;
	int rows = 0, cols = 0;
	T* mtr_p = nullptr;
public:
	MatrixIteratorColumn(T* item, int row, int col, int rows_total, int cols_total)
	{
		mtr_p = item;
		setCurItem(mtr_p+(cur_row*cols + cur_col));

		cur_row = row;
		cur_col = col;

		rows = rows_total;
		cols = cols_total;
	}

	~MatrixIteratorColumn() {}

	MatrixIteratorColumn& operator++()
	{
		if (cur_col == cols - 1 && cur_row == rows - 1)
		{
			setCurItem(mtr_p + (rows-1)*cols + cols);
		}
		else if (cur_row == rows - 1)
		{
			cur_row = 0;
			cur_col++;

			setCurItem(mtr_p + (cur_row*cols + cur_col));
		}
		else
		{
			cur_row++;
			setCurItem(mtr_p + (cur_row*cols + cur_col));
		}

		return *this;
	}

	MatrixIteratorColumn operator++(int)
	{
		auto old_it = MatrixIteratorColumn(mtr_p, cur_row, cur_col, rows, cols);

		++(*this);

		return old_it;
	}

	void setCurItem(T* item)
	{
		MatrixIteratorBase<T>::cur_item = item;
	}

	T* getCurItem()
	{
		return MatrixIteratorBase<T>::cur_item;
	}
};

template <typename T>
class MatrixIteratorEnd: public MatrixIteratorBase<T>
{
private:
	int rows = 0, cols = 0;
public:
	MatrixIteratorEnd(T* mtr, int rows_total, int cols_total)
	{
		rows = rows_total;
		cols = cols_total;

		setCurItem(mtr + (rows-1)*cols + cols);
	}

	void setCurItem(T* item)
	{
		MatrixIteratorBase<T>::cur_item = item;
	}
};

#endif // ITERATOR_H
