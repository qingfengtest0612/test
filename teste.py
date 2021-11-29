import pytest

def test():
    print('这个自动化测试用例111')

if __name__ == '__main__':
    pytest.main(['teste.py','-s','--alluredir=./reportjson111'])
