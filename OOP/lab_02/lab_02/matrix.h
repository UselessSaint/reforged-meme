#ifndef MATRIX_H
#define MATRIX_H

#include "includes.h"
#include "errors.h"
#include "iterator.h"


class MatrixBase
{
protected:
	int rows = 0, cols = 0;
public:
	virtual void setColumn(int n) = 0;
	virtual void setRow(int n) = 0;
	virtual int getColumn() const = 0;
	virtual int getRow() const = 0;

	virtual ~MatrixBase() = default;
};


template <typename T>
class MatrixRow
{
private:
	T* curr_row;
	int cols = 0;
public:
	MatrixRow(int in_col, T* in_curr_row)
	{
		cols = in_col;
		curr_row = in_curr_row;
	}

	~MatrixRow() {}

	T& operator[](int n)
	{
		if (n < 0 || n > cols)
		{
			throw MatrixIndexError();
		}
		return curr_row[n];
	}
};


template <typename T>
class Matrix: public MatrixBase
{
private:
	T* copy = nullptr;
public:
	Matrix() {}

	Matrix(int n, int m)
	{
		if (n <= 0 || m <= 0)
		{
			throw MatrixSizeError();
		}

		setRow(n);
		setColumn(m);

		copy = new T [n*m];
		fill_n(copy, n*m, 0);
	}

	Matrix(vector<initializer_list<T>> init_mtr)
	{
		int rows = init_mtr.size();
		int cols = 0;

		for (auto curr_list : init_mtr)
		{
			if (curr_list.size() > size_t(cols))
			{
				cols = curr_list.size();
			}
		}

		copy = new T [rows*cols];
		fill_n(copy, rows*cols, 0);

		setRow(rows);
		setColumn(cols);

		int curr_row = 0;
		int curr_col = 0;

		for (auto curr_list : init_mtr)
		{
			for (auto elem : curr_list)
			{
				copy[cols * curr_row + curr_col] = elem;
				curr_col++;
			}
			curr_row++;
			curr_col = 0;
		}
	}

	Matrix(const Matrix<T>& other)
	{
		setRow(other.getRow());
		setColumn(other.getColumn());

		copy = new T [getRow()*getColumn()];

		for (int i = 0; i < getRow()*getColumn(); i++)
		{
			copy[i] = other.copy[i];
		}
	}

	~Matrix() { delete [] copy; }

	MatrixRow<T> operator [](int row)
	{
		if (row < 0 || row > getRow())
		{
			throw MatrixIndexError();
		}
		return MatrixRow<T>(getColumn(), &(copy[row*getColumn()]));
	}

	Matrix<T> operator +(Matrix<T> &second)
	{
		if (second.getRow() != getRow() || second.getColumn() != getColumn())
		{
			throw MatrixAdditionError();
		}

		Matrix<T> result(getRow(), getColumn());

		auto res_it = result.beginColumn();
		auto frs_it = beginColumn();
		auto snd_it = second.beginColumn();

		while (snd_it != second.end())
		{
			*res_it = *frs_it + *snd_it;

			++res_it;
			++frs_it;
			++snd_it;
		}

		return result;
	}

	Matrix<T>& operator =(const Matrix<T>& other)
	{
		setRow(other.getRow());
		setColumn(other.getColumn());

		copy = new T [getRow()*getColumn()];

		for (int i = 0; i < getRow()*getColumn(); i++)
		{
			copy[i] = other.copy[i];
		}

		return *this;
	}

	Matrix<T>& operator +=(Matrix<T>& other)
	{
		if (other.getRow() != getRow() || other.getColumn() != getColumn())
		{
			throw MatrixAdditionError();
		}

		auto frs_it = beginColumn();
		auto snd_it = other.beginColumn();


		while (snd_it != other.end())
		{
			*frs_it = *frs_it + *snd_it;

			++frs_it;
			++snd_it;
		}

		return *this;
	}

	Matrix<T> operator *(Matrix<T> &other)
	{
		if (getColumn() != other.getRow())
		{
			throw MatrixMultiplicationError();
		}

		Matrix<T> result(getRow(), other.getColumn());

		for (int i = 0; i < getRow(); i++)
		{
			for (int j = 0; j < other.getColumn(); j++)
			{
				for (int k = 0; k < getColumn(); k++)
				{
					result[j][i] = result[j][i] + (*this)[k][i] * (other[j][k]);
				}
			}
		}

		return result;
	}

	Matrix<T>& operator *=(Matrix<T>& other)
	{
		(*this) = (*this) * other;

		return *this;
	}

	Matrix<T> operator *(const T& scalar)
	{
		Matrix<T> result(getRow(), getColumn());

		for (int i = 0; i < getRow(); i++)
		{
			for (int j = 0; j < getColumn(); j++)
			{
				result[i][j] = (*this)[i][j]*scalar;
			}
		}

		return result;
	}

	Matrix<T>& operator *=(const T& scalar)
	{
		(*this) = (*this) * scalar;

		return *this;
	}

	Matrix<T> transpose()
	{
		Matrix<T> result(getRow(), getColumn());

		auto res_it = result.beginRow();
		auto it = beginColumn();

		for(;res_it != result.end() || it != end(); res_it++, it++)
		{
			*res_it = *it;
		}

		return result;
	}

	T det()
	{
		if (getRow() != getColumn())
		{
			throw MatrixDetError();
		}

		Matrix<T> copy(*this);

		for (int i = 0; i < getColumn(); i++)
		{
			if (copy[i][i] == 0)
			{
				continue;
			}

			for (int j = i + 1; j < getColumn(); j++)
			{
				T sep = copy[j][i] / copy[i][i];

				for (int k = 0; k < getColumn(); k++)
				{
					copy[j][k] -= copy[i][k] * sep;
				}
			}
		}

		T det = 1.0;

		for (int i = 0; i < getColumn(); i++)
		{
			det *= copy[i][i];
		}

		return det;
	}

	Matrix<T> inverse()
	{
		if (getRow() != getColumn())
		{
			throw MatrixDetError();
		}

		Matrix<T> copy(*this);
		Matrix<T> unit_m({ {1},
						   {0,1},
						   {0,0,1} });

		for (int i = 0; i < getColumn(); i++)
		{
			if (copy[i][i] == 0)
			{
				continue;
			}

			for (int j = i + 1; j < getColumn(); j++)
			{
				T sep = copy[j][i] / copy[i][i];

				for (int k = 0; k < getColumn(); k++)
				{
					copy[j][k] -= copy[i][k] * sep;
					unit_m[j][k] -= unit_m[i][k] * sep;
				}
			}
		}

		T det = 1.0;

		for (int i = 0; i < getColumn(); i++)
		{
			det *= copy[i][i];
		}

		if (det == 0.0)
		{
			throw MatrixInverseError();
		}

		for (int i = 0; i <= getColumn() - 1; i++)
		{
			unit_m[getColumn() - 1][i] = (unit_m[getColumn() - 1][i]) / (copy[getColumn() - 1][getColumn() - 1]);
		}

		for (int i = 0; i <= getColumn() - 1; i++)
		{
			for (int j = getColumn() - 2; j >= 0; j--)
			{
				for (int k = j + 1; k < getColumn(); k++)
				{
					unit_m[j][i] -= copy[j][k] * unit_m[k][i];
				}
				unit_m[j][i] /= copy[j][j];
			}
		}

		return unit_m;
	}

	void printRow()
	{
		int i = 0;
		for (auto it = this->beginRow(); it != this->end(); it++)
		{
			cout << *it << " ";
			if (i == cols - 1)
			{
				cout << endl;
				i = 0;
			}
			else
			{
				i++;
			}
		}
	}

	void printColumn()
	{
		int i = 0;
		for (auto it = this->beginColumn(); it != this->end(); ++it)
		{
			cout << *it << " ";
			if (i == rows - 1)
			{
				cout << endl;
				i = 0;
			}
			else
			{
				i++;
			}
		}
	}

	MatrixIteratorRow<T> beginRow()
	{
		return MatrixIteratorRow<T>(copy);
	}

	MatrixIteratorColumn<T> beginColumn()
	{
		return MatrixIteratorColumn<T>(copy, 0, 0, getRow(), getColumn());
	}

	MatrixIteratorEnd<T> end()
	{
		return MatrixIteratorEnd<T>(copy, getRow(), getColumn());
	}

	void setColumn(int in_col) override
	{
		cols = in_col;
	}

	void setRow(int in_row) override
	{
		rows = in_row;
	}

	int getColumn() const override
	{
		return cols;
	}

	int getRow() const override
	{
		return rows;
	}
};


#endif // MATRIX_H
