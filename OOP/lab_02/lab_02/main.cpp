#include <iostream>
#include "includes.h"
#include "matrix.h"

using namespace std;

int main()
{
	try
	{
		Matrix<int> m(2,3, {2, 3,
							4, 5});

		m.printRows();
		cout << "---------" << endl;
		m.printColumns();

		Matrix<double> q(5,5,  {1.2,2.2,3.2,4.2,5.2,
								1,2,3,4,5,
								1,2,3,4,5});
		cout << "---------" << endl;
		q.printRows();
		cout << "---------" << endl;
		q.printColumns();
	}
	catch (exception& exc)
	{
		cout << exc.what();
	}


    return 0;
}
