s = input()
def test_str(s):
    if len(s) < 2:
        return ""
    else:
        return s[0:2]+s[-2:]
print(test_str(s))
