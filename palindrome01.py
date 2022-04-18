def is_palindrome(input, i=0, j=0):
    if len(input) == 0:
        return False

    if input[i] != input[j]:
        return False

    if j - i <=2:
        return True

    return is_palindrome(input, i+1, j-1)

if __name__ == '__main__':
    input = ''

    print(is_palindrome(input, 0, len(input)-1))