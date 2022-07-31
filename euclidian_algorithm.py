# Euclidian algorithm for fiding the inverse mod p of a given integer x
def find_inverse_mod_prime(x: int, p: int):
    r_prev = x
    r_curr = p
    s_prev = 1
    s_curr = 0
    t_prev = 0
    t_curr = 1

    while r_curr > 0:
        r_next = r_prev % r_curr
        q = int((r_prev-r_next)/r_curr)
        s_next = s_prev - q*s_curr
        t_next = t_prev - q*t_curr

        r_prev = r_curr
        s_prev = s_curr
        t_prev = t_curr
        r_curr = r_next
        s_curr = s_next
        t_curr = t_next

    return int(s_prev % p)