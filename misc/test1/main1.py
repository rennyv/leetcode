def gcf(a,b):
    if(b==0):
        return a
    else:
        return gcf(b,a%b)

def test_gcf():
    assert 12 == gcf(48,60)

