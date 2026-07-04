# Tau Core Photon–Lensing MAR v2 Package

## Verzió

**Csomag:** Tau Core Photon–Lensing Bridge — Morphological Alignment Residual v2  
**Score:** \(Q_{MAR} = 13/24\)  
**Státusz:** controlled synthetic/mock research protocol, **not real-data evidence**.

---

## 0. Executive summary

A v2 csomag frissíti a korábbi Photon–Lensing/MAR modult az újabb futásokkal:

```text
B1c  — out-of-sample + scale stability validation
B1d  — multi-observable mock shear test
B1d-2 — stricter physical shear mock
B1e  — Null–Matter Link toy model
```

A jelenlegi állapot:

\[
\boxed{Q_{MAR} = 13/24}
\]

Ez azt jelenti:

```text
A MAR már működő, kontrollált synthetic/mock protokoll.
Még nem real-data claim.
Még nem sötétanyag-cáfolat.
Még nem Tau Core-bizonyíték.
```

A legfontosabb új eredmény: a MAR már nemcsak convergence residualon működő template-játék, hanem kiterjed:

\[
\kappa
\]

\[
\gamma_1, \gamma_2
\]

és:

\[
\delta a_\tau
\]

matter-dynamics residual irányába is.

---

## 1. Core Tau Core állítás

A Photon–Lensing Bridge lényege:

\[
\gamma_\tau = \operatorname{NullProbe}[g^{eff}_{\mu\nu}]
\]

A foton nem az anomália forrása, hanem null-readout probe. A lencsézési residual elsődlegesen:

\[
\Delta O_{lens}
=
\mathcal{L}_O[\delta g^\tau_{\mu\nu}]
\]

ahol:

\[
O \in \{\alpha,\kappa,\gamma,\mu,\Delta t\}
\]

A MAR hipotézis:

\[
\Delta\kappa_\tau(x)
\sim
T_\tau(x)
\]

ahol:

\[
T_\tau(x)
=
B_{env}(x) A_f(x) M_{bf}(x)
\]

és:

\[
M_{bf}(x)
=
1-(\hat b(x)\cdot \hat f(x))^2
\]

---

## 2. Modulok és státusz

| Module | Status | Rövid jelentés |
|---|---|---|
| B1a synthetic recovery | PASSED | Beültetett \(T_\tau\) residual visszanyerhető. |
| B1a-2 sensitivity ladder | PASSED but optimistic | \(C_\tau\) nő \(\epsilon_\tau\)-val, de túl tiszta mock. |
| B1a-3 realistic stress test | PARTIAL / WARNING | Systematics és filament-only kontrollok veszélyesek. |
| B1a-4 systematics separation | PASSED as method improvement | \(\Delta R^2_\tau\) és partial corr jobb, mint sima korreláció. |
| B1c OOS + scale stability | PARTIAL PASS | Validation \(\Delta R^2_\tau>0\), legjobb skála kb. \(\sigma=2.2\). |
| B1d multi-observable shear | PIPELINE PASS | Spin-2 pipeline működik, de túl barátságos mock. |
| B1d-2 physical shear mock | PARTIAL PASS | Fourier \(\kappa\to\gamma\) relációval is részben működik, nagy split szórással. |
| B1e Null–Matter Link | SYNTHETIC STRUCTURAL PASS | \(\Delta_{NM}\sim T_\tau\) toy protokoll működött. |

---

## 3. Synthetic recovery és baseline képek

### Fig. 1 — Baryonic surface density

![Fig. 1](figures/fig01_baryonic_surface_density.png)

### Fig. 2 — Filament strength

![Fig. 2](figures/fig02_filament_strength.png)

### Fig. 3 — Initial Tau template

![Fig. 3](figures/fig03_tau_template_initial.png)

### Fig. 4 — Initial lensing residual

![Fig. 4](figures/fig04_lensing_residual_initial.png)

### Fig. 5 — Control distributions

![Fig. 5](figures/fig05_control_distributions_initial.png)

Initial synthetic recovery:

\[
C_\tau \approx 0.875
\]

Ez method sanity check, nem fizikai evidencia.

---

## 4. Sensitivity ladder

### Fig. 6 — \(C_\tau\) vs \(\epsilon_\tau\)

![Fig. 6](figures/fig06_c_tau_vs_epsilon.png)

A \(C_\tau\) monoton nő a beültetett residual amplitúdóval.

### Fig. 7 — SNR vs \(\epsilon_\tau\)

![Fig. 7](figures/fig07_snr_vs_epsilon.png)

Tanulság: az egyszerű SNR túl optimista, mert a random orientation kontroll nem tiszta null.

---

## 5. Realistic stress és systematics separation

### Fig. 8 — Stress-test controls

![Fig. 8](figures/fig08_stress_test_control_bars.png)

Fő tanulság:

```text
Corr(Δκ,Tτ)>0 nem elég.
Systematics, baryon, filament-only, boundary és halo kontrollok után kell jel.
```

### Fig. 9 — \(\Delta R^2_\tau\) after controls

![Fig. 9](figures/fig09_delta_r2_tau_after_controls.png)

A jobb statisztika:

\[
\Delta R^2_\tau
=
R^2(T_\tau+Controls)
-
R^2(Controls)
\]

### Fig. 10 — residualized partial correlation

![Fig. 10](figures/fig10_partial_corr_tau_after_controls.png)

A residualizált kapcsolat:

\[
\rho_{\tau|controls}
=
Corr(\Delta\kappa_{\perp controls},T_{\tau,\perp controls})
\]

---

## 6. B1c — Out-of-sample + scale stability

### Fig. 11 — validation \(\Delta R^2\) by scale

![Fig. 11](figures/fig11_b1c_validation_delta_r2_by_scale.png)

Több smoothing skála közül a legstabilabb synthetic mockban:

\[
\sigma_\tau^* \approx 2.2
\]

### Fig. 12 — validation partial correlation by scale

![Fig. 12](figures/fig12_b1c_validation_partial_corr_by_scale.png)

A Tau-injected condition pozitív maradt, a no-Tau kontroll közelebb nullához.

### Fig. 13 — split details at best scale

![Fig. 13](figures/fig13_b1c_best_scale_split_delta_r2.png)

A split szerinti eredmény pozitív, de checkerboard gyengébb.

**Score update:** S8 0→1, S11 0→1.

---

## 7. B1d és B1d-2 — Multi-observable lensing

### 7.1 Friendly shear mock

![Fig. 14](figures/fig14_b1d_friendly_shear_delta_r2.png)

Ez pipeline check volt, de túl kedvező.

### 7.2 Physical shear mock

A szigorúbb B1d-2 a flat-sky weak-lensing relációt használta:

\[
\tilde\gamma_1(\ell)
=
\frac{\ell_x^2-\ell_y^2}{\ell^2}
\tilde\kappa(\ell)
\]

\[
\tilde\gamma_2(\ell)
=
\frac{2\ell_x\ell_y}{\ell^2}
\tilde\kappa(\ell)
\]

### Fig. 15 — physical shear validation \(\Delta R^2_\tau\)

![Fig. 15](figures/fig15_b1d2_physical_shear_delta_r2.png)

A shear-csatornák pozitívak, de nagy szórással.

### Fig. 16 — physical shear partial correlations

![Fig. 16](figures/fig16_b1d2_physical_shear_partial_corr.png)

### Fig. 17–22 — physical maps and templates

![Fig. 17](figures/fig17_b1d2_delta_kappa.png)

![Fig. 18](figures/fig18_b1d2_delta_gamma1_physical.png)

![Fig. 19](figures/fig19_b1d2_delta_gamma2_physical.png)

![Fig. 20](figures/fig20_b1d2_tau_template_kappa.png)

![Fig. 21](figures/fig21_b1d2_tau_template_gamma1_physical.png)

![Fig. 22](figures/fig22_b1d2_tau_template_gamma2_physical.png)

**Interpretáció:** a multi-observable pipeline részben működik, de S9 marad 1/2, nem 2/2.

---

## 8. B1e — Null–Matter Link

### 8.1 Definíció

A photon-lensing residual:

\[
\Delta\kappa_\tau
=
\mathcal D_{null}[\delta g^\tau_{\mu\nu}]
\]

A matter-dynamics residual:

\[
\delta a_\tau
=
\mathcal D_{matter}[\delta g^\tau_{\mu\nu}]
\]

A mismatch:

\[
\Delta_{NM}
=
\Delta\kappa_\tau
-
\mathcal T[\delta a_\tau]
\]

Tau Core-kompatibilis elvárás:

\[
\Delta_{NM}
\sim
T_\tau
\]

### Fig. 23 — B1e Tau template

![Fig. 23](figures/fig23_b1e_tau_template.png)

### Fig. 24 — photon-lensing residual

![Fig. 24](figures/fig24_b1e_delta_kappa_obs.png)

### Fig. 25 — matter-dynamics residual

![Fig. 25](figures/fig25_b1e_delta_a_obs.png)

### Fig. 26 — matter-to-lensing transfer proxy

![Fig. 26](figures/fig26_b1e_transfer_proxy.png)

### Fig. 27 — Null–Matter mismatch after controls

![Fig. 27](figures/fig27_b1e_null_matter_mismatch.png)

### Fig. 28 — permutation partial corr

![Fig. 28](figures/fig28_b1e_permutation_partial_corr.png)

### Fig. 29 — permutation \(\Delta R^2\)

![Fig. 29](figures/fig29_b1e_permutation_delta_r2.png)

B1e eredmény:

\[
\Delta R^2_\tau \approx 0.10
\]

és:

\[
\rho_{\Delta NM,T_\tau|controls} \approx 0.26
\]

Permutation kontrollhoz képest a real Tau-template kiugrott.

**Score update:** S10 0→1.

---

## 9. Frissített scoring

| Axis | Score | Max | Indok |
|---|---:|---:|---|
| S1 Spatial Null Survival | 2 | 2 | Spatial shuffle kontrollokkal szemben a synthetic recovery és későbbi validációkban a Tau-template túlél. |
| S2 Orientation Specificity | 1 | 2 | A real orientation jobb, de random orientation/filament-strength kontrollok továbbra is részben versenyképesek. |
| S3 Baryon Independence | 1 | 2 | Baryon kontroll után marad jel, de stress mild/medium esetben baryon-keveredés még lehetséges. |
| S4 Filament-Only Control | 1 | 2 | Full template többlete van, de filament-only kontroll több stress esetben erős. |
| S5 Systematics Resistance | 1 | 2 | Systematics-separated regresszió javított, de hard stress esetben systematics még dominálhat. |
| S6 Incremental Explanatory Power | 1 | 2 | ΔR²_tau pozitív synthetic és no-Tau kontrollban eltűnik, de még nem real-data és nem teljesen robusztus. |
| S7 Residualized Partial Correlation | 1 | 2 | Partial correlation pozitív Tau-injection és null no-Tau kontrollban; még synthetic. |
| S8 Scale Stability | 1 | 2 | B1c-ben több smoothing skálán pozitív validation jel, legjobb skála σ≈2.2, de split szórás marad. |
| S9 Multi-Observable Consistency | 1 | 2 | B1d/B1d-2 megmutatta κ+γ pipeline-t, fizikai shear mockban részleges pass, de nagy split-szórás. |
| S10 Null–Matter Link | 1 | 2 | B1e synthetic null–matter mismatch test működött, de transfer proxy egyszerű és nem valódi rotáció. |
| S11 Out-of-Sample Replication | 1 | 2 | B1c train/validation split partial pass, független survey nincs. |
| S12 Theoretical Parsimony | 1 | 2 | A T_tau template egyszerű és nem körkörös, de a teljes kontrollhierarchia és smoothing választás még fejlesztendő. |


Összesen:

\[
\boxed{Q_{MAR}=13/24}
\]

Értelmezés:

| Score tartomány | Jelentés |
|---:|---|
| 0–4 | nincs használható MAR protokoll |
| 5–8 | korai synthetic jelölt |
| 9–12 | működő synthetic protokoll, de gyenge |
| 13–16 | kontrollált mock program alsó-közép szint |
| 17–20 | real-data candidate több kontrollal |
| 21–24 | replikált, multi-observable kihívás baseline modelleknek |

A jelenlegi:

\[
13/24
\]

tehát:

```text
controlled synthetic/mock program lower-mid tier
```

---

## 10. Mit mondhatunk most?

### Mondható

```text
A MAR immár pontozható, falszifikálható residual-protokoll.
A synthetic recovery működik.
A systematics-separated ΔR² jobb, mint a sima korreláció.
Az OOS/scale stability részben túléli.
A physical shear mock részben működik.
A Null–Matter Link toy modell működött synthetic struktúrában.
```

### Nem mondható

```text
Tau Core bizonyított.
Dark matter cáfolva.
Valódi lensing adaton MAR detektálva.
Bullet Cluster megoldva.
A physical shear eredmény robusztus.
A matter-dynamics link valódi rotációs adatokon igazolt.
```

---

## 11. Következő real-data roadmap

### R1 — Real-data feasibility

Kell:

```text
lensing κ/shear map
baryon mass proxy
cosmic web / filament catalogue
survey systematics maps
mask and PSF templates
redshift slicing
```

### R2 — Pre-registration

Fagyasztani kell:

```text
T_tau formula
smoothing scale vagy scale ladder
control templates
masks
validation split
success/failure thresholds
```

### R3 — First observational target

Legjobb kezdés:

```text
weak lensing survey patch + public cosmic web catalogue
```

Második:

```text
cluster lensing sample with baryon gas/stellar maps
```

Harmadik:

```text
CMB lensing + large-scale structure filament map
```

### R4 — Hard failure conditions

A MAR bukik, ha:

```text
ΔR²_tau validation ≈ 0
no-Tau/random templates hasonlóak
systematics template dominál
filament-only kontroll elmagyarázza
nincs OOS replikáció
κ és γ csatornák ellentmondanak
null–matter mismatch nem strukturált
```

---

## 12. Végső v2 verdikt

\[
\boxed{
\text{MAR v2 is a controlled synthetic/mock protocol, not an observational detection.}
}
\]

Magyarul:

\[
\boxed{
\text{A MAR v2 már kontrollált synthetic/mock protokoll, de még nem megfigyelési bizonyíték.}
}
\]

A következő valódi ugrás:

\[
\boxed{
\text{pre-registered real-data feasibility test}
}
\]

vagy még előtte:

\[
\boxed{
\text{stricter mock with survey masks + E/B separation + real rotation-curve proxy}
}
\]

---

## 13. Data inventory

CSV fájlok a `data/` mappában:

- `mar_toy_model_results.csv`
- `mar_sensitivity_ladder_results.csv`
- `mar_sensitivity_thresholds.csv`
- `mar_realistic_stress_test_results.csv`
- `mar_systematics_separation_results.csv`
- `mar_systematics_separation_coefficients.csv`
- `mar_b1c_oos_scale_validation_results.csv`
- `mar_b1c_oos_scale_validation_aggregate.csv`
- `mar_b1d_multi_observable_shear_results.csv`
- `mar_b1d2_physical_shear_results.csv`
- `mar_b1d2_physical_shear_aggregate.csv`
- `mar_b1e_null_matter_link_results.csv`

Ábrák a `figures/` mappában.
