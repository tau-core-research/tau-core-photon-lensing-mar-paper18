# Tau Core Photon-Lensing MAR Paper 18

Private Paper 18 scaffold:

**Photon-Lensing Morphological Alignment Residual: a synthetic Tau Core bridge protocol**

This repository turns `tau_core_photon_lensing_mar_v2_package.zip` into a
reproducible paper package. It preserves the source package as provenance,
extracts compact derived CSV summaries, builds paper figures, compiles a PDF,
and prepares an arXiv source archive.

## Main Claim

The paper defines a synthetic photon-lensing search protocol for a
Morphological Alignment Residual (MAR):

```text
T_tau = B_env * A_f * M_bf
C_tau = Corr(delta_kappa, T_tau)
```

where `T_tau` is built from source-side morphology handles: environment
boundary, filament strength, and baryon-filament angular mismatch. It is not
built from the lensing residual itself.

The package result is claim-safe:

```text
v2 MAR score:                    Q_MAR = 13/24
toy recovery:                    C_tau = 0.8745
random-orientation control mean: 0.3938
spatial-shuffle control mean:    0.0123
sensitivity threshold:           epsilon_tau <= 0.01 in the tested noise ladder
stress-test MAR Q scores:        mild 5/10, medium 4/10, hard 4/10, no-tau 2/10
systematics-separated Delta R2:  positive for mild/medium/hard, near zero for no-tau
B1c OOS scale validation:        positive Tau-injected split signal, but scale/split scatter remains
B1d-2 physical shear mock:       positive gamma1/gamma2 and kappa support in synthetic flat-sky mock
B1e Null-Matter Link toy:        positive lensing-after-transfer signal; matter-dynamics control remains negative
```

The v2 extension is still a controlled synthetic/mock protocol. It is not
observational evidence and not validation-grade photon-lensing physics. In
short, it is not observational evidence.

## Does Not Claim

- It does not prove Tau Core.
- It does not analyze real survey data.
- It does not detect a photon-lensing residual in nature.
- It does not falsify dark matter, LCDM, GR, or standard lensing.
- It does not derive the photon or lensing operator from bare Tau principles.
- It does not claim that the MAR template is unique or physically validated.
- It is not physical validation of Tau Core or of the MAR template.
- It does not claim that the Null-Matter Link toy is a real dark-sector
  measurement.

## Source-Transport Boundary

`T_tau` and the Null-Matter Link transfer term are terminal descriptors and
controls, not parent optical connections. Physical non-scalar optical
transport would additionally require independently sourced full
body-connection holonomy or Kato transport of a varying, constant-rank access
projector. A scalar phase/clock branch cannot fix normalized multimode optical
orientation. The synthetic scores remain method tests and are not inverted
into source-arrow claims.

## Included Data

Only compact synthetic derived artifacts are included:

```text
data/derived/*.csv
figures/*.png
paper18_submission_source/figures/*
source_package_docs/
source_package_figures/
```

## Full-4D Score Boundary

`Q_MAR` is a package-local audit score. A physical photon/lensing/matter score
must instead derive every terminal from the same nonzero source-frozen
`E_K = (K_HH - K_std) - C K_VV^-1 C^dagger`, remove exact duplicates, and
retain full cross-terminal covariance. Existing MAR values are unchanged.

## Reproduce

```bash
python scripts/reproduce.py
```

The command:

1. rebuilds the compact Paper18 summary CSV/JSON;
2. regenerates Paper18 PDF figures from the derived CSV files;
3. compiles `paper18_submission_source/main.tex`;
4. builds `arxiv_submission_source.zip`;
5. runs public package tests;
6. prints `PAPER18_PHOTON_LENSING_MAR_REPRODUCTION_COMPLETE`.

## arXiv Source Package

`arxiv_submission_source.zip` is generated from
`paper18_submission_source/` and excludes the compiled PDF plus temporary TeX
build products.

## Scope

Paper 18 is a synthetic methodology and bridge-protocol paper. It strengthens
the Tau Core lensing/readout program by giving a concrete non-circular
Morphological Alignment Residual statistic and by showing where it survives
and where it weakens under controls.

The correct current status is:

```text
CONTROLLED_SYNTHETIC_MOCK_PHOTON_LENSING_MAR_V2_PROTOCOL
```

## Relation to Other Tau Core Papers

- Paper 7 gives the observer-gated lensing feasibility and falsification
  framework.
- Paper 14 gives the cosmic-web multi-readout witness ladder.
- Paper 17 gives the shared-parent covariance versus orientation-only
  classifier.
- Paper 18 supplies a photon-lensing MAR bridge protocol that should later be
  tested under the Paper 17 shared-parent/orientation discipline.  The v2
  package extends the protocol from convergence-only MAR checks to
  out-of-sample scale validation, physical shear mocks, and a toy Null-Matter
  Link residual.
