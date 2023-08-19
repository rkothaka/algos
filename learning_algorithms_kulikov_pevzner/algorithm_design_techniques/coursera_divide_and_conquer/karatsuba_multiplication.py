def multiply(A, B):
    if A < 10 or B < 10:
        return A * B

    def split(num: int):
        temp = num
        l = 0
        while temp:
            temp //= 10
            l += 1

        n_2 = 10 ** (l//2)
        a, b = num // n_2, num % n_2

        return a, b, l//2

    a, b, n1 = split(A)
    c, d, n2 = split(B)

    # AB = (a * 10^n1 + b) * (c * 10^n2 + d)
    # = ac * 10^ (n1+n2) + ad*10^n1 + bc*10^n2 + bd
    # (a+b)(c+d) = ac + ad + bc + bd, makes sense if n1 == n2
    assert n1 == n2

    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_bc = multiply(a+b, c+d) - ac - bd

    return (ac * (10 ** (n1 + n2))) + (ad_bc * (10 ** n1)) + bd


if __name__ == "__main__":
    print(multiply(251, 25))
