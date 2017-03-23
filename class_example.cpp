#include<iostream> 

class Complex{
  //private: can only be accessed by members of the class, referencing outside will give an error
  //public: can be accessed from outside of the class functions

private:
  //private stuff, doesn't need to be declared because it is default, but nice to declare it. You don't really have to do this, but it's good for protection so that you don't mess something up in the future
  double real,imag;


public:
  //can be accessed from outside of the class
  Complex();
  Complex(double);
  Complex(double,double); //Don't have to define with re or im here, we can include them in the constructors, sometimes being explicit is better
  ~Complex(){}; //useful for dynamically allocated memory, just makes sure you don't mess up your computer
    void print();
    //adding in some print functionality
    
}; //We could define some complex things to put here for later, but we can also just have them defined later, they are 'complex' type

//We can define it in the class, but then it gets messy so we don't have to do that, usually define it outside of the class

//Define constructors, they're just functions so we can do anything
Complex::Complex(){
  real=0.0;
  imag=0.0;
}
Complex::Complex(double re){
  real = re;
  imag = 0.0;
}
Complex::Complex(double re, double im){
  real = re;
  imag =im;
}

//If we define constructors as private, then we can't even define it later
//Constructors intialize the class

//Destructors, when the class is no longer being used, like a local variable in the local loop, then it will get rid of it

void Complex::print(){
  std::cout<<"("<<real<<","<<imag<<")"<<std::endl;
std::cout<<real<<"+"<<imag<<"i"<<std::endl;
}

int main(int arc, char*argv[]){
  //declare variables
  double real, imag;

  //ask for input
  std::cout<<"Real: ";
  std::cin>>real;
  std::cout<<"Imaginary: ";
  std::cin>> imag;

  Complex number1;
  Complex number2(real);
  Complex number3(real, imag);
  //Defines the number types based on how many arguments we gave it

  /*
  std::cout <<number3.real<<std::endl;
  std::cout<<number3.imag<<std::endl;
  */
  //These won't work because of the fact that we defined them in private

  number1.print();
  number2.print();
  number3.print();
  //These should print them out

  return 0;
}
//Just did some stuff with classes, example for how to define some classes in C++
