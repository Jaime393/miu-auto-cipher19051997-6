# Hueso: la auditoría que declara FALSO su propio axioma

## El hecho

`auditoria_miu.py`, en `Jaime393/miu-memoria-codex`, es la única
verificación numérica de ese repo que corre (según la minería de la
ola 6). Tiene 13 checks. Da 12/13 PASS. Y en su propia salida imprime:

```
A7 declara tau*Xi*c > kappa_min = 1.618 -> FALSO (1 > 1.618 es falso)
```

## Por qué es un hueso y no una anécdota

La falsedad no viene de fuera. Viene de dos piezas del mismo repo que
no encajan entre sí:

- **M5** define tau = 1/(Xi*c). Por definición, tau*Xi*c == 1 siempre.
  No es una medición: es una identidad. El script lo escribe así en su
  propio código (`tau_Xi_c = 1.0  # por M5, identidad`).
- **A7** exige tau*Xi*c > 1.618.

1 > 1.618 es falso. No hay medición que lo salve, porque no hay nada
que medir: la identidad ya fijó el valor en 1. El script lo sabe y lo
imprime. El repo se refuta a sí mismo con su propia herramienta.

## Los otros dos resultados de la misma corrida

- **El FAIL del error.** El script mide 0.00109521226102 y lo compara
  con 0.001095, tolerancia 1e-6. El redondeo del propio repo no pasa su
  propia tolerancia. El valor medido es el mismo que aparece en los
  `mesh_heartbeat` (`RAIZ_X_error_pct`). No es un error de cálculo de
  nadie: es la cifra redondeada del repo, rechazada por el listón del
  repo.
- **El aviso V172.** Phi_sup/Phi = 1.4735, y la regla V175 dice *1.6.
  El script lo imprime como aviso. Ningún archivo que leí responde a
  ese aviso.

## Lo que esto no dice

No dice que todo el sistema caiga. Dice una cosa precisa: un axioma
(A7) es inconsistente con una definición (M5) dentro del mismo repo,
y la inconsistencia la mide el código del propio repo, no un crítico
externo. Los otros 12 checks pasan: sigma, RAIZ_X, los delta_k, los
gradientes y las reglas V175 coinciden con sus valores declarados.

## El patrón

Un axioma que exige más que lo que su propia definición permite es un
axioma que su propio código declara falso. La auditoría no lo esconde:
lo imprime en la primera línea de su salida.

## Fuentes

- `Jaime393/miu-memoria-codex`, `auditoria_miu.py` (64 l., 2.413 B,
  sha256 `34876097…`), leído por GitHub 2026-11-09 ~17:11 -05,
  ejecutado en local el mismo día: 12/13 PASS, 1 FAIL.
- `~/workspace/mineria/miu-memoria-codex/LECTURA.md`, sección
  `auditoria_miu.py`; `CONTENIDO.md` §2.
- Reproducción local: `auditoria_a7_repro.py` (TODO COINCIDE, salida 0).
