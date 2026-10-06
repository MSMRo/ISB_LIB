import unittest
import sympy as sp
from isb_lib import ISB, plot_pz, pzmap


class TestISBLibrary(unittest.TestCase):
    def test_imports(self):
        self.assertIsNotNone(ISB)
        self.assertIsNotNone(plot_pz)
        self.assertIsNotNone(pzmap)

    def test_symbolic_transforms(self):
        t, s = sp.symbols("t s")
        X_s = 1 / (s + 2)
        t_sym = sp.symbols("t", real=True, positive=True)
        s_sym = sp.symbols("s")

        x_t_calc = sp.inverse_laplace_transform(X_s, s_sym, t_sym)
        self.assertIsNotNone(x_t_calc)


if __name__ == "__main__":
    unittest.main()
