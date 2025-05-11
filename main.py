def sumTheList(arr):
    if not arr:
        return 0
    head, *tail = arr
    return (head**4 if head<0 else 0 ) + sumTheList(tail)
    
def recurseTestCase(theTestCase,**kwargs):
    if(theTestCase==0):
        return list(kwargs.values())
    else:
        x = int(input()) 
        y = list(map(int, input().split(" ")))
        if len(y) != x:
            kwargs[str(len(kwargs.keys())+1)] = -1
        else:
           kwargs[str(len(kwargs.keys())+1)] = sumTheList(y)+0

        return recurseTestCase(theTestCase-1,**kwargs)
def print_ans(sums):
    if not sums:
        return
    head, *tail = sums
    print(head)
    return print_ans(tail)
def main(): 
    N = int(input())
    sums = recurseTestCase(N)
    print_ans(sums)
    return 1
if __name__ == "__main__":
    main()
