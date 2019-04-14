#include <iostream>
#include "includes.h"
#include "matrix.h"

using namespace std;

int main()
{
	try
	{
		Matrix<int> m1( { {1,2,3},
							  {5,5,6},
							  {7,8,9} } );

		m1 *= 2;

		m1.printRow();
	}
	catch (exception& exc)
	{
		cout << exc.what() << endl;
	}


    return 0;
}
