#include <iostream>
#include "includes.h"
#include "matrix.h"
#include "iterator.h"

using namespace std;

int main()
{
	try
	{
		Matrix<int> m(2,2, {2, 3,
							4, 2});

		m.print();
	}
	catch (exception& e)
	{
		cout << e.what();
	}


    return 0;
}
