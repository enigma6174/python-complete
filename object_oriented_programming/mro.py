class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(A):
    num = 7


class E(B, C):
    pass


class F(C, B):
    pass


class G(D, C):
    pass


class H(C, D):
    pass


print(f"E.num {E.num}")
print(f"F.num {F.num}")
print(f"G.num {G.num}")
print(f"H.num {H.num}")
