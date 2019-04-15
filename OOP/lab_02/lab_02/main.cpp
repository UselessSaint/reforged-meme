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

		Matrix<int> m0(3,3);
		
		Matrix<int> m2(3,3);
						  
		//m1.printRows();
		
		
		m1 = m1 + m0;
		
		m1.clear();
		
		m1.printRows();
	}
	catch (exception& exc)
	{
		cout << exc.what() << endl;
	}


    return 0;
}
