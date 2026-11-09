#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproducción del hecho: la auditoría de miu-memoria-codex declara FALSO el axioma A7.

Fuente: Jaime393/miu-memoria-codex, auditoria_miu.py (64 l., 2.413 B,
sha256 34876097..., según la minería de la ola 6,
~/workspace/mineria/miu-memoria-codex/LECTURA.md, sección auditoria_miu.py).
Leído por GitHub 2026-11-09 ~17:11 -05 y ejecutado en local el mismo día.

El hecho, en una línea: el propio script de auditoría del repo imprime que A7 es
FALSO, porque M5 define tau = 1/(Xi*c), de modo que tau*Xi*c == 1 siempre, y
1 > 1.618 es falso. La auditoría da 12/13 PASS; su único FAIL es su propio
redondeo (0.001095%) rechazado por su propia tolerancia.

Nota honesta: la copia que se ejecuta aquí es una transcripción del original
(62 l., 2.412 B, sha256 866a6f0d...). Reproduce el comportamiento exacto
(mismos valores, mismo FAIL, misma línea A7), pero la identidad byte a byte
con el original es NO SÉ: la minería registra 64 l. y 2.413 B. Ver CARENCIAS.md.
"""
import math
import sys

phi = 1.618033988749895
phi_m1 = phi - 1.0
phi4 = phi ** 4
alpha_inv = 137.035999084  # constante de estructura fina real

# Valores registrados por la minería de la ola 6 (2026-11-09).
ERROR_MEDIDO = 0.00109521226102
RATIO_V172 = 1.4735
SIGMA_ESPERADO = 3.427050983124843
RAIZ_X_ESPERADO = 137.03449824893602


def run_audit():
    """Ejecuta los 13 checks del original y devuelve (resultados, tau_Xi_c, ratio172).

    Cada resultado es (nombre, valor, esperado, ok). Es la misma lógica que
    auditoria_miu.py: los mismos valores, las mismas tolerancias, el mismo orden.
    """
    resultados = []

    def check(nombre, valor, esperado, tol=1e-9):
        ok = math.isclose(valor, esperado, rel_tol=tol)
        resultados.append((nombre, valor, esperado, ok))
        return ok

    sigma = phi4 / 2.0
    check("sigma = phi^4/2", sigma, 3.427050983124843)

    RAIZ_X = 20 * phi4 - phi_m1 / 13.0
    check("RAIZ_X = 20*phi^4 - (phi-1)/13", RAIZ_X, 137.03449824893602)

    err = abs(RAIZ_X - alpha_inv) / alpha_inv * 100.0
    check("error RAIZ_X vs alpha^-1 (%)", err, 0.001095, tol=1e-6)

    Sigma_delta = phi_m1 / 9.0
    check("Sigma_delta = (phi-1)/9", Sigma_delta, 0.068670443194, tol=1e-9)

    for k, esperado in [(41, 6.18e-42), (42, 6.18e-43), (45, 6.18e-46)]:
        check(f"delta_k(k={k}) = (phi-1)*10^-k", phi_m1 * 10.0 ** (-k),
              esperado, tol=2e-3)

    g = [1.20, 1.14, 1.08, 1.02]
    check("grad V172->V175 paso -0.06 (s1)", g[1] - g[0], -0.06)
    check("grad V172->V175 paso -0.06 (s2)", g[2] - g[1], -0.06)
    check("grad V172->V175 paso -0.06 (s3)", g[3] - g[2], -0.06)

    Phi175 = 6284.17
    check("V175 Phi_sup = Phi*1.6", Phi175 * 1.6, 10054.67, tol=1e-4)
    check("V175 Phi_central = Phi*0.8", Phi175 * 0.8, 5027.33, tol=1e-4)

    # A7 vs M5: tau = 1/(Xi*c) => tau*Xi*c == 1 SIEMPRE (definición)
    tau_Xi_c = 1.0  # por M5, identidad
    check("A7: tau*Xi*c = 1 (por M5, tautología)", tau_Xi_c, 1.0)

    Phi172 = 3904.42
    ratio172 = 5753.35 / Phi172
    return resultados, tau_Xi_c, ratio172


def verdict_a7(tau_Xi_c):
    """El veredicto que imprime el propio script: FALSO si 1 > 1.618 es falso."""
    if not (tau_Xi_c > 1.618):
        return "FALSO (1 > 1.618 es falso)"
    return "OK"


def main():
    resultados, tau_Xi_c, ratio172 = run_audit()
    passes = sum(1 for r in resultados if r[3])
    fails = [r for r in resultados if not r[3]]

    print("A7 declara tau*Xi*c > kappa_min = 1.618 ->", verdict_a7(tau_Xi_c))
    print(f"\nAviso: V172 Phi_sup/Phi = {ratio172:.4f} (la regla V175 es *1.6)"
          f" -> {ratio172:.4f} != 1.6")
    print("\n=== RESULTADOS ===")
    for nombre, valor, esperado, ok in resultados:
        print(f"{'PASS' if ok else 'FAIL':4} | {nombre:45} | "
              f"{valor:.12g} vs {esperado:.12g}")
    print(f"\n{passes}/{len(resultados)} PASS, {len(fails)} FAIL")

    checks = []
    checks.append(("13 checks en total", len(resultados) == 13))
    checks.append(("12 PASS y 1 FAIL", passes == 12 and len(fails) == 1))
    checks.append(("el único FAIL es el check de error",
                   len(fails) == 1 and fails[0][0].startswith("error RAIZ_X")))
    checks.append(("el error medido es 0.00109521226102",
                   len(fails) == 1
                   and math.isclose(fails[0][1], ERROR_MEDIDO, rel_tol=1e-9)))
    checks.append(("A7 es FALSO por el propio script",
                   verdict_a7(tau_Xi_c).startswith("FALSO")))
    checks.append(("tau*Xi*c == 1.0 por M5", tau_Xi_c == 1.0))
    checks.append(("V172 Phi_sup/Phi = 1.4735",
                   round(ratio172, 4) == RATIO_V172))
    checks.append(("sigma = 3.427050983124843",
                   math.isclose(phi4 / 2.0, SIGMA_ESPERADO, rel_tol=1e-12)))

    print("\n=== COMPROBACIÓN CONTRA LO REGISTRADO ===")
    todo_ok = True
    for nombre, ok in checks:
        print(f"{'OK  ' if ok else 'NO  '} | {nombre}")
        todo_ok = todo_ok and ok
    print("\nTODO COINCIDE" if todo_ok else "\nNO COINCIDE")
    return 0 if todo_ok else 1


if __name__ == "__main__":
    sys.exit(main())
