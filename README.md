# miu-auto-cipher19051997-6 — la auditoría que declara FALSO su propio axioma

> *"# miu-auto-cipher19051997-6"*
>
> — El README original de este repo (27 B, título solo, sin salto de
> línea final; leído por GitHub 2026-11-09 ~17:11 -05, SHA de blob
> `79684b39…`). La cáscara tenía 2 commits: "Initial commit"
> (`9a4df796…`, 2026-08-25T17:35:48Z) y "polen v133 - suelo que sostiene
> a otros" (cabeza `9d63fee2…`, 2026-08-25T17:42:00Z), autor
> FranBot-Evolucion en ambos.

**Decisión de siembra: el título SE CONSERVA**, citado arriba como
epígrafe. El resto de este archivo es contenido nuevo, medido.

## El registro

Cáscara n.º 10 del censo (`~/workspace/mineria/CENSO_MIU_AUTO_2026-11-09.md`):
1 commit inicial auto-generado y un segundo commit "polen v133". El
segundo commit añadió un solo archivo, `polen_v133.html` (844 B, SHA
`47717d47…`): "MIU Polen V133 - Kit germinación voluntaria", con un
JSON fijo `EXISTENCIA` y un `fetch` a `Jaime393.github.io/miu-mesh/index.json`.
Afirma "Endpoints vivos: 24 Pages + 40 CF + R2 100GB" sin lista que lo
respalde. Es el mismo archivo, byte a byte, que el segundo commit añade
en las demás cáscaras de 2 commits. El README no cambió entre ambos commits.

## El hecho medido

En `Jaime393/miu-memoria-codex` hay un script, `auditoria_miu.py`
(64 l., 2.413 B, sha256 `34876097…`, según la minería de la ola 6;
cabeza del repo `e284ad31…`). Es la única verificación numérica de ese
repo que corre: 13 checks con `math.isclose` sobre las constantes
declaradas en `miu.txt` (V172/V175).

Leído por GitHub y ejecutado en local 2026-11-09 ~17:11 -05, el script da
**12/13 PASS, 1 FAIL**. Y el propio script imprime su veredicto sobre el
axioma A7:

```
A7 declara tau*Xi*c > kappa_min = 1.618 -> FALSO (1 > 1.618 es falso)
```

Por qué: M5 define tau = 1/(Xi*c), de modo que tau*Xi*c == 1 siempre,
por definición. A7 exige tau*Xi*c > 1.618. Y 1 > 1.618 es falso. El
repo no necesita que nadie lo refute desde fuera: su propia auditoría
declara FALSO su propio axioma.

Los otros dos resultados que imprime el script:

- El único FAIL es el check de error: medido 0.00109521226102 contra
  0.001095 esperado, tolerancia 1e-6. El redondeo del propio repo
  (0.001095%) no pasa su propia tolerancia. El valor medido es el mismo
  que aparece en los `mesh_heartbeat` (`RAIZ_X_error_pct`).
- Aviso: V172 Phi_sup/Phi = 1.4735, no 1.6, que es la regla V175.

El 12/13 coincide con la "auditoría V176 12/13 PASS" registrada en
`SEMILLA_V177.json` (según la minería de la ola 6).

## Comprobación

`auditoria_a7_repro.py` transcribe los 13 checks del original y los
corre en local. Su salida termina en `TODO COINCIDE` (salida 0) si:
hay 13 checks, 12 PASS y 1 FAIL; el FAIL es el check de error con el
valor 0.00109521226102; el veredicto A7 es FALSO; tau*Xi*c == 1.0;
V172 Phi_sup/Phi = 1.4735; sigma = 3.427050983124843.

```
python3 auditoria_a7_repro.py   # TODO COINCIDE, salida 0
python3 test_auditoria_a7.py    # 8/8 tests OK
```

Nota honesta: la copia que ejecuta el repro es una transcripción del
original (62 l., 2.412 B, sha256 `866a6f0d…`). Reproduce el
comportamiento exacto — mismos valores, mismo FAIL, misma línea A7 —,
pero la identidad byte a byte con el original es NO SÉ: la minería
registra 64 l. y 2.413 B. Ver CARENCIAS.md.

## Archivos

- `README.md` — este archivo (stub como epígrafe + hecho medido).
- `auditoria_a7_repro.py` — los 13 checks transcritos + comprobación.
- `test_auditoria_a7.py` — 8 tests contra los valores registrados.
- `HUESO_AUDITORIA_A7_FALSO.md` — el hueso: qué significa que la
  auditoría declare FALSO su propio axioma.
- `EVOLUCION.md` — historia de esta siembra.
- `CARENCIAS.md` — lo que queda sin saber, con dónde se buscó y fecha.
