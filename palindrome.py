def is_palindrome(s: str) -> bool:

    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return True

    is_palindrome(s[1:-1])

    return False

    # if len(s) < 2: return True
    # if s[0] != s[-1]: return False
    # return is_palindrome(s[1:-1])

if __name__ == '__main__':
    assert is_palindrome("kaak") == True, "check your code!"
    assert is_palindrome("qwwqqwr") == False, "check your code!"
    assert is_palindrome("1234567890987654321") == True, "check your code!"
    assert is_palindrome("5452") == False, "check your code!"
    assert is_palindrome("1") == True, "check your code!"
    assert is_palindrome("12") == False, "check your code!"    