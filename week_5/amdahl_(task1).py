def amdahls_law(F, p):
    return 1 / ((1 - F) + F / p)
def amdahls_law_inf(F):
    return 1/(1-F)


def parallel_fraction(parelelpart,nonparallelpart):
    return parelelpart/(parelelpart+nonparallelpart)

f=parallel_fraction(100,20)


print(f)
print(amdahls_law(f,8))
print(amdahls_law_inf(f))
print(100/4+5)
print(100/8+20)

