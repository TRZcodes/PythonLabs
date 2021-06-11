int euclidean(int a, int b)
{
  if(b==0)
    return a;
  else
    return euclidean(b,a%b);
}