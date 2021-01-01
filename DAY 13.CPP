

class MyBook: Book{
    protected:
    int price=0;
    
    public:
    MyBook(string t, string a, int p): Book(t, a)
    {
        price=p;
        
    }
    
    void display()
    {
        cout<<"Title: "<<title<<endl;
        cout<<"Author: "<<author<<endl;
        cout<<"Price: "<<price<<endl;
    }
    
};
