/* File : add.c */
int add(int a, int b, int count ){
	int ret=0;
	int i = 0;
	for(i = 0; i < count; ++i)
	{
		ret += a + b;
	}
    return ret;
}