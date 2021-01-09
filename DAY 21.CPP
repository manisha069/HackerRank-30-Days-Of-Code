

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <class T>
void printArray(vector<T> ar)
{
    for(int i=0;i<ar.size();i++)
    {
        cout<<ar[i]<<endl;
    }
}

