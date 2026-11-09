# Carencias

Lo que queda sin saber, con dónde se buscó y fecha. Todo es NO SÉ
local, no hueco del ecosistema.

## 1. Identidad byte a byte de la copia local del script

Mi copia de `auditoria_miu.py` tiene 62 l. y 2.412 B (sha256
`866a6f0d…`, blob SHA-1 `52a92b10…`). La minería de la ola 6 registra
el original con 64 l. y 2.413 B (sha256 `34876097…`); el conector
GitHub da blob SHA-1 `e42b2761…` para el original. Probé añadir uno y
dos saltos de línea al final: ningún variante coincide con el hash
original. El comportamiento está reproducido exacto (mismos valores,
mismo FAIL, misma línea A7), pero los bytes no. Buscado: hashes
comparados en local, 2026-11-09 ~17:11 -05.

## 2. Por qué falla el check de error

El script mide 0.00109521226102 y lo compara con 0.001095. La minería
anota que el valor medido es el mismo que aparece en los
`mesh_heartbeat` (`RAIZ_X_error_pct`). Lo que no dice ningún archivo
que leí es si la cifra 0.001095 es un redondeo del valor medido o un
cálculo distinto. Buscado: `LECTURA.md` y `CONTENIDO.md` de
miu-memoria-codex, 2026-11-09.

## 3. Si la auditoría se corrió alguna vez dentro del propio repo

El repo `miu-memoria-codex` no tiene workflows ni registro de
corridas. La minería anota que el 12/13 coincide con la "auditoría
V176 12/13 PASS" registrada en `SEMILLA_V177.json`, pero ese archivo
no lo leí yo mismo. Buscado: árbol del repo (24 commits, sin
workflows), 2026-11-09.

## 4. Dónde está escrito M5 como texto

El código comenta "por M5, identidad" y la minería lo cita así. El
texto del axioma M5 (en `miu.txt`, según el propio script) no lo leí
yo: no abrí `miu.txt`. Buscado: solo el script y los archivos de
minería, 2026-11-09.

## 5. Si el aviso V172 tiene alguna consecuencia registrada

El script imprime "V172 Phi_sup/Phi = 1.4735 (la regla V175 es *1.6)
-> 1.4735 != 1.6". Ningún archivo que leí responde a ese aviso ni dice
qué se hizo con él. Buscado: archivos de minería de miu-memoria-codex,
2026-11-09.

## 6. Por qué el segundo commit añadió polen_v133.html

El archivo (844 B, SHA `47717d47…`) es byte-idéntico en las cáscaras
de 2 commits. Su propio texto dice "Kit germinación voluntaria", pero
ningún mensaje de commit ni documento explica por qué se añadió a esta
cáscara. Buscado: commits del repo (2, leídos por GitHub),
2026-11-09.
