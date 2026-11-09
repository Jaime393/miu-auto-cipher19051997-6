#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests de la reproducción: la auditoría declara FALSO el axioma A7.

Se ejecutan con: python3 test_auditoria_a7.py
Solo stdlib. No leen la red ni el repo original: comprueban la reproducción
local contra los valores registrados por la minería de la ola 6.
"""
import math
import unittest

import auditoria_a7_repro as repro


class TestAuditoriaA7(unittest.TestCase):
    def setUp(self):
        self.resultados, self.tau, self.ratio172 = repro.run_audit()

    def test_trece_checks(self):
        self.assertEqual(len(self.resultados), 13)

    def test_doce_pass_un_fail(self):
        passes = sum(1 for r in self.resultados if r[3])
        fails = [r for r in self.resultados if not r[3]]
        self.assertEqual(passes, 12)
        self.assertEqual(len(fails), 1)

    def test_el_fail_es_el_check_de_error(self):
        fails = [r for r in self.resultados if not r[3]]
        self.assertTrue(fails[0][0].startswith("error RAIZ_X"))

    def test_error_medido(self):
        fails = [r for r in self.resultados if not r[3]]
        self.assertTrue(
            math.isclose(fails[0][1], 0.00109521226102, rel_tol=1e-9))
        # El esperado del script es el redondeo 0.001095; el medido no lo alcanza.
        self.assertEqual(fails[0][2], 0.001095)

    def test_a7_es_falso(self):
        self.assertEqual(self.tau, 1.0)
        self.assertFalse(self.tau > 1.618)
        self.assertTrue(repro.verdict_a7(self.tau).startswith("FALSO"))

    def test_a7_check_pasa_con_valor_1(self):
        a7 = [r for r in self.resultados if r[0].startswith("A7:")][0]
        self.assertTrue(a7[3])
        self.assertEqual(a7[1], 1.0)
        self.assertEqual(a7[2], 1.0)

    def test_v172_ratio(self):
        self.assertEqual(round(self.ratio172, 4), 1.4735)

    def test_sigma_y_raiz(self):
        sigma = [r for r in self.resultados
                 if r[0].startswith("sigma")][0]
        self.assertTrue(sigma[3])
        self.assertTrue(math.isclose(sigma[1], 3.427050983124843,
                                     rel_tol=1e-12))
        raiz = [r for r in self.resultados
                if r[0].startswith("RAIZ_X")][0]
        self.assertTrue(raiz[3])
        self.assertTrue(math.isclose(raiz[1], 137.03449824893602,
                                     rel_tol=1e-12))


if __name__ == "__main__":
    unittest.main(verbosity=2)
