from isb_lib import ISB, plot_pz, pzmap

__all__ = ["ISB", "plot_pz", "pzmap"]

if __name__ == "__main__":
    import sympy as sp

    t, s = sp.symbols("t s")
    x_t = sp.E ** (-2 * t) * sp.cos(2 * t)
    X_s = sp.laplace_transform(x_t, t, s, noconds=True)

    print("Probando ISB library...")
    print("X(s) =", X_s)
    X_s, x_t, polos, ceros = ISB.plot_pz(X_s)
    print("Polos:", polos)
    print("Ceros:", ceros)