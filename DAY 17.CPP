

//Write your code here
class Calculator{
  public:
  int power(double n, int p)
  {
      
    if(n>=0 && p>=0)
    {
        return pow(n, p);
    }
    else
    {
        throw runtime_error("n and p should be non-negative");
    }
  }
};

