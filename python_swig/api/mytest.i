%module mytest
%{
extern int add(int a, int b, int count);
extern int sub(int a, int b);
extern long fib(int n);
%}
 
extern int add(int a, int b, int count);
extern int sub(int a, int b);
extern long fib(int n);