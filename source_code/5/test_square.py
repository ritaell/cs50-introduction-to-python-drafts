from square import squared
'''
def main():
    test_square()
pytest
def test_square():
    assert squared(3)==8
'''
def test_positive():
    assert squared(2)==4
    assert squared(3)==9
def test_zero():
    assert squared(0)==0
def test_negative():
    assert squared(-2)==4
    assert squared(-3)==4
def test_str():
    with pytest.raises(TypeError):
        squared("cat")

if __name__ == "__main__":
    main()