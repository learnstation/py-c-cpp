%module mytest
%{
extern int add(int a, int b, int count);
extern int sub(int a, int b);
%}
 
extern int add(int a, int b, int count);
extern int sub(int a, int b);