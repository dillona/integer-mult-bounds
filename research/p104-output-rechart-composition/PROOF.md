# Compose the unit-pivot split with the credited output rechart

The exact baseline is #7130 at `161e482bc2d8c78ecef96135430c60d49b8fc345`,
word SHA256 `a32696e806c5cde0510cdf2f494e1f14ebb01e73d4ec577413fd7e7c0d9d68b2`.
`INPUTS.json` retains its complete 25-file export, including the complete
nested #7123 closure and every earlier source notice.

The peer is Rohan Arun's #7124 at
`97dc14132da53562b7939776d7a83d72af72eeb1`. Eight exact files are pinned in
`PEER-SOURCES.json`: its constructor, changes, input manifest, word,
native/application receipts, proof and README. They are the inputs needed
for this transfer and comparison, not a full peer-package export or a claim
that we independently replayed its complete registered package. The peer's
common #7123 archive is byte-identical to the complete one already retained
inside #7130. The source wrapper authenticates that equality and independently
reconstructs every peer word byte from the common source. Its SHA256 is
`95c4cc4afa5ddfdc699ce6741ebacf5a9d454b46404fce0197a8a28c46943686`.

## Exact instruction and boundary transfer

The #7130 split adds a 426-instruction inverse input basis, two 17-instruction
cut bases after source event 37583, and a 426-instruction final basis. Its
neutral placement leaves the common source program unchanged before those
insertions. The continuing pivot 639 is relabelled to the new public role
1491; owned labels shift by one. Every other retained source instruction is
unchanged, with this operand relabelling where necessary.

All 129 peer scalar-chart edits occur after event 37583 and before the new
final basis: original indices 39877 through 73719. Their current indices
are therefore i+426+2·17=i+460. `transfer.py` checks the actual original
opcode, old chart, operands and coefficient, applies the exact pivot/owned
relabel, and requires complete equality with the instruction at i+460 in
#7130. It checks uniqueness, the expected inventories, and every transferred
helper output contract. `TRANSFER.json` records all original/current event
pairs; `verify_transfer.py` rejects five index/chart/coefficient/duplicate/
output corruptions. No edit is accepted merely because its index has the
right offset.

The 21 affected output roles are

```
226,234,236,297,299,393,449,484,485,707,990,998,1060,1155,
1208,1445,1460,1461,1477,1489,1490.
```

Each still ends at chart 246 in #7130 and is changed to 127. None is the
retired pivot 639 or its fresh successor 1491. The new split's boundary
vectors only mix helpers already ending at full chart 127, so those common
output promises are retained. The transferred scalar charts likewise change
246→127. The complete causal reconstruction, rather than this observation
alone, proves that the new contacts can be reached legally.

## Normalized operator and physical interpretation

The package's `construct.py` is byte-identical to Rohan Arun's pinned peer
constructor. For a field in chart F, write its value as C_F z. A legal MOVE
F→G applies C_G C_F⁻¹, preserving z. Cocharted scalar operations have their
usual rational action on z, independent of the chart. The constructor
retains every scalar opcode, operand, coefficient and chronological order,
changes only the specified public contact/output charts, and rebuilds public
transport immediately before each scalar contact and at the final boundary.
Every public MOVE must be strictly nested and increasing.

Consequently the entire normalized operator of #7130 is retained. Each
changed helper now promises C_new-final C_initial⁻¹ on its independent input,
so its productive rank is recounted at the actual new boundary. Main charts
remain fixed. The full rational adjoint and separate integer forward replay
check every public input, main/helper output and cleared owned row. All owned
INIT/CLEAR operations, contacts and MOVEs retain their order and charts;
all 54 lifetimes, peak 43, and 23 rises of mass 56 are unchanged. The inherited
nonzero-content owned-erasure assumption remains explicit.

The scalar chronology is identical, so the exact prefix/pre-product grid
remains 1125/F25. This is independently derived and replayed; F24 is rejected.
The full physical catalogue, absolute phases, independent helper allocation,
caller substitution, precision and all costs are checked in APPLICATION.md.
No free transport, zero-initialized public helper or reuse of an obsolete
helper target is assumed.

## Recounted invoice

Relative to #7130, the actual native changes are

```
ΔT = {1:−2, 2:+2, 5:−1, 6:+1, 8:−18, 9:+18},
ΔP = {1:−35, 2:+12, 3:+8, 4:−8, 5:+8}.
```

Both rank masses rise by 21. Helper count stays 1092, while paid positions
fall by 15 per invocation. The exact 17-stage caller gives 110400 paid
positions, 22308 productive fields, surplus 1424 and zero empty credit.
The word has 74591 events and 1492 public fields, canonical SHA256
`9557c4682056ab7cc7cda89aa73865bef0e3948cc10b3c3061b0a944af05b96a`.

For H_r=r^(1−κ), the per-native signed difference is

```
33 H1 − 10 H2 − 8 H3 + 8 H4 − 9 H5 + H6 − 18 H8 + 18 H9.
```

The complete new crossing is bracketed by two directed engines. The narrower
interval is `(0.00364240849686931699339641963661833,
0.00364240849686931699339641963661834)`. The certified decimal claim
.003642408496869 improves #7130 by .000000189212232. This gain is recomputed
from the complete invoices, not obtained by adding the sibling claims.
Both engines reject #7130's invoice at the new claim. This is a bound for
this emitted invoice, not a global optimum or removal of the five assumptions.

## Credit

Rohan Arun supplied #7124's nominated output changes, causal rechart
constructor and normalized-coordinate proof, using 1337isnot1337/OpenAI
Codex's fresh-helper-boundary alpha-expansion method. The #7130 split and its
source chain retain credit to Ali Romman, Jerry Chen/CubeJerry, Matarener,
ToikY, Rohan Arun's #7113 caller and #7122 input rechart, DreamingOfClouds,
Douglas Colkitt/#7000 reviewers and every nested source notice. This exact
composition and transfer check were prepared for dillona with substantial
OpenAI Codex assistance; no subagents. Apache-2.0.
