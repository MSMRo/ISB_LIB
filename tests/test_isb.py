import unittest
import sympy as sp
from isb_lib import ISB, plot_pz, pzmap


class MockTransferFunction:
    def __init__(self, expr):
        self._expr = expr

    def to_expr(self):
        return self._expr


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

    def test_transfer_function_object(self):
        s = sp.symbols("s")
        tf = MockTransferFunction(1 / (s**2 + 3 * s + 2))
        expr = tf.to_expr()
        self.assertEqual(expr, 1 / (s**2 + 3 * s + 2))

    def test_sympify_string_input(self):
        expr_str = "1/(s+4)"
        sym_expr = sp.sympify(expr_str)
        self.assertTrue(isinstance(sym_expr, sp.Basic))


if __name__ == "__main__":
    unittest.main()
