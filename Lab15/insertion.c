void InsertionSortCLang(int* a, int size)
{
  int i,j,temp;
  for(i=1;i<size;i++)
  {
    temp=a[i];
    j=i-1;
    while(j>=0 &&a[j]>temp)
    {
      a[j+1]=a[j];
      j-=1;
    }
    a[j+1]=temp;
  }
}