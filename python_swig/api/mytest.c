int add(int a, int b, int count ){
    int ret=0;
    int i = 0;
    for(i = 0; i < count; ++i)
    {
        printf("%d\n", i);
    }
    return ret;
}
int sub(int a, int b){
    return a-b;
}

long fib(int n){
    if (n < 2)
        return n;
    return fib(n - 1) + fib(n - 2);
}