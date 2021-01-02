
    Difference(vector<int> x)
    {
        elements=x;
    }
    void computeDifference()
    {
        int min=100;
        int max=0;
        for (int i=0;i<elements.size();i++)
        {
            if (elements[i]>max)
            {
                max=elements[i];
            }
            if(elements[i]<min)
            {
                min=elements[i];
            }
        }
        maximumDifference=max-min;
    }

