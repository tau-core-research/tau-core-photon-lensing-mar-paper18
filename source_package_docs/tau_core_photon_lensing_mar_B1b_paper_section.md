# Photon–Lensing Bridge és Morphological Alignment Residual  
## Tau Core B1b paper-section draft — maximálisan részletes munkacsomag

**Státusz:** belső kutatási jegyzet / paper-section draft  
**Modul:** Tau Core Photon–Lensing Bridge → B1 Morphological Alignment Residual  
**Futtatott részek:** synthetic recovery, sensitivity ladder, realistic stress test, systematics-separated regression  
**Fontos korlát:** ez a csomag **nem bizonyítja** a Tau Core-t és **nem cáfolja** a sötétanyag-modellt. A csomag egy mérhető, falszifikálható keresési protokollt épít fel.

---

## 0. Rövid vezető összefoglaló

A Tau Core fotonmodul szerint a foton nem fundamentális „kis golyó”, amely egy előre adott térben végigmegy egy kész pályán, hanem **koherens null-csatornás readout** egy mélyebb parent-level elektromágneses átmenetből.

A lencsézés esetén ez azt jelenti:

\[
\text{foton} = \text{null-readout probe}
\]

és:

\[
\text{lencsézés} = \text{az effektív metrikus readout tomográfiája}
\]

A standard megfigyelési tény: a fény elhajlása sok rendszerben több gravitációs hatást mutat, mint amit a látható/baryonikus anyag alapján várnánk. A standard modell ezt sötétanyaggal írja le. A Tau Core óvatosabb elsődleges megfogalmazása:

\[
\text{amit közvetlenül mérünk, az metrikus/lencsézési residual}
\]

nem pedig közvetlenül maga az ontológiai anyagkomponens.

Ezért a Tau Core Photon–Lensing Bridge fő állítása:

\[
\Delta O_{lens}
=
\mathcal{L}_{O}
\left[
\delta g_{\mu\nu}^{\tau}
\right]
\]

ahol:

- \(\Delta O_{lens}\) lencsézési residual valamely observable-ben,
- \(O \in \{\alpha,\kappa,\gamma,\mu,\Delta t\}\),
- \(\delta g_{\mu\nu}^{\tau}\) egy lehetséges Tau Core metrikus/readout residual,
- \(\mathcal{L}_{O}\) a lencsézési projekciós operátor.

A B1 modul erre épít egy konkrét keresési javaslatot:

\[
\boxed{
\text{Morphological Alignment Residual} \quad \text{MAR}
}
\]

A MAR hipotézis szerint, ha a lencsézési residual egy mélyebb parent-morfológiai/metrikus readout-feszültségből ered, akkor nemcsak lokális tömegsűrűséggel, hanem **kozmikus web-orientációval, filamentáris szerkezettel, boundary-régiókkal és baryon–filament mismatch-csel** is korrelálhat.

---

## 1. Tau Core ontológiai háttér

### 1.1 Parent morphology

A Tau Core alapszintje:

\[
\mathcal{P}
\]

Ez a parent morphology: nem közvetlenül azonos a 3+1D téridővel, hanem annál mélyebb, morfológiai szerkezet.

A megfigyelhető effektív világ:

\[
R_{3+1}: \mathcal{P} \rightarrow \mathcal{M}_{3+1}
\]

ahol:

\[
\mathcal{M}_{3+1}
\]

az effektív 3+1D readout.

### 1.2 Metric sector

A gravitációs/metrikus readout:

\[
g_{\mu\nu}^{eff}
=
R_{3+1}^{G}(\mathcal{P})
\]

A standard GR-kompatibilis bontás:

\[
g_{\mu\nu}^{eff}
=
g_{\mu\nu}^{GR}
+
\delta g_{\mu\nu}^{\tau}
\]

ahol:

- \(g_{\mu\nu}^{GR}\): standard GR metrika a modellezett források alapján,
- \(\delta g_{\mu\nu}^{\tau}\): Tau Core metrikus/readout residual.

### 1.3 Electromagnetic sector

Az elektromágneses parent-transition:

\[
\Delta \mathcal{P}_{EM}
\]

A foton Tau Core-definíciója:

\[
\gamma_{\tau}
=
\operatorname{NullCoh}
\left[
R_{3+1}(\Delta \mathcal{P}_{EM})
\right]
\]

Vagyis a foton:

\[
\text{minimális koherens null-csatornás elektromágneses readout}
\]

A null-feltétel:

\[
ds^2 = 0
\]

Tau Core-nyelven:

\[
ds^2=0
\quad \Longleftrightarrow \quad
\text{belső sajátidő nélküli null-readout csatorna}
\]

---

## 2. Photon–Lensing Bridge

### 2.1 Standard lensing kép

Standard GR-ben a foton null geodetikát követ:

\[
ds^2 = g_{\mu\nu}dx^\mu dx^\nu = 0
\]

és:

\[
k^\mu\nabla_\mu k^\nu = 0
\]

A lencsézés standard lánca:

```text
mass-energy → metric → null geodesics → observed lensing
```

### 2.2 Tau Core fordítás

Tau Core-ban:

\[
\ell_{\gamma}^{lens}
=
\operatorname{NullRecon}
\left[
g_{\mu\nu}^{eff},
\Delta \mathcal{P}_{EM}
\right]
\]

Vagyis a lencsézett fotonpálya nem parent-szintű primitív út, hanem:

\[
\text{effektív metrikus readout + elektromágneses parent-transition közös null-rekonstrukciója}
\]

### 2.3 Lensing residual

A lencsézési residual:

\[
\Delta \kappa(x)
=
\kappa_{obs}(x)
-
\kappa_{base}(x)
\]

ahol \(\kappa_{base}\) lehet:

1. baryon-only,
2. baryon + halo,
3. flexible halo + nuisance model.

Tau Core-olvasat:

\[
\Delta \kappa_{\tau}(x)
=
\operatorname{Proj}_{lens}
\left[
\delta g_{\mu\nu}^{\tau}
\right]
\]

Ez nem jelenti, hogy nincs sötétanyag. Csak azt jelenti, hogy **a közvetlenül mért objektum metrikus residual**, amelyet utána különféle ontológiai modellekkel lehet magyarázni.

---

## 3. Morphological Alignment Residual hipotézis

### 3.1 Intuíció

Ha:

\[
\delta g_{\mu\nu}^{\tau}
\]

nem pusztán lokális tömegsűrűségből ered, hanem parent-morfológiai readout-többlet, akkor a residual szerkezete nem feltétlenül lesz gömbszimmetrikus vagy lokális halo-profil.

Lehetséges extra függések:

```text
filament direction
void–filament–cluster boundary
baryonic gradient mismatch
cosmic web anisotropy
environmental transition
scale-dependent morphology
```

### 3.2 Fő hipotézis

\[
\boxed{
\Delta \kappa_{\tau}(x)
\sim
T_{\tau}(x)
}
\]

ahol \(T_{\tau}\) egy nem körkörös, a residualtól függetlenül épített morfológiai template.

### 3.3 Nem körkörös template

A template:

\[
T_{\tau}(x)
=
B_{env}(x)
A_f(x)
M_{bf}(x)
\]

ahol:

- \(B_{env}(x)\): environmental boundary strength,
- \(A_f(x)\): filament anisotropy / filament strength,
- \(M_{bf}(x)\): baryon–filament angular mismatch.

A mismatch:

\[
M_{bf}(x)
=
1-
(\hat b(x)\cdot \hat f(x))^2
\]

ahol:

- \(\hat b(x)\): baryonikus gradiens iránya,
- \(\hat f(x)\): lokális filament irány.

A négyzet azért kell, mert a filament iránya tengely, nem nyíl:

\[
\hat f \sim -\hat f
\]

### 3.4 Miért nem körkörös?

A template nem használja \(\Delta \kappa\)-t. Ez kritikus. Ha a residual gradiensét használnánk a template-ben, majd a residuallal korreláltatnánk, részben önmagunkra illesztenénk.

A korrekt irány:

\[
T_{\tau}
=
F(\text{baryon map},\text{filament map},\text{environment map})
\]

és utána:

\[
C_{\tau}
=
Corr(\Delta\kappa,T_{\tau})
\]

---

## 4. Ábrák: synthetic recovery alapmezők

### 4.1 Baryonikus felszíni sűrűség

![Fig. 1 — Baryonic surface density](figures/fig01_baryonic_surface_density.png)

**Értelmezés:** a mock rendszer baryonikus térképe. Ez több komponensből áll: központi tömeg, mellékkomponens és kisebb alstruktúra.

### 4.2 Filament strength

![Fig. 2 — Cosmic-web filament strength](figures/fig02_filament_strength.png)

**Értelmezés:** a mock kozmikus web filamentáris struktúrája. Ez a mező adja a nagy skálájú morfológiai orientációt.

### 4.3 Tau morphology template

![Fig. 3 — Tau morphology template](figures/fig03_tau_template.png)

**Értelmezés:** a nem körkörös \(T_\tau\) template:

\[
T_{\tau}
=
B_{env}A_fM_{bf}
\]

Ez a template boundary + filament + baryon–filament mismatch kombináció.

### 4.4 Observed residual

![Fig. 4 — Observed residual](figures/fig04_lensing_residual.png)

**Értelmezés:** a beültetett Tau-szerű residual + zaj után kapott mock lencsézési residual.

---

## 5. Synthetic MAR recovery test

### 5.1 Generatív modell

A mock megfigyelt konvergencia:

\[
\kappa_{obs}
=
\kappa_{base}
+
\epsilon_{\tau}T_{\tau}
+
\eta
\]

A residual:

\[
\Delta\kappa
=
\kappa_{obs}
-
\kappa_{base}
\]

A recovery statistic:

\[
C_{\tau}
=
Corr(\Delta\kappa,T_{\tau})
\]

### 5.2 Kontrollok

Használt kontrollok:

```text
random filament orientation
spatial shuffle
baryon template
filament-only template
```

### 5.3 Eredmények

A synthetic recovery eredménye:

\[
C_{\tau}
\approx
0.875
\]

Random orientation kontroll:

\[
C_{rand}
\approx
0.394
\]

Spatial shuffle:

\[
C_{shuffle}
\approx
0.012
\]

Baryon template:

\[
C_{baryon}
\approx
0.074
\]

### 5.4 Kontroll-disztribúció

![Fig. 5 — Control distributions](figures/fig05_control_distributions.png)

**Értelmezés:** a valódi \(T_\tau\) messze jobban korrelál a residual mezővel, mint a spatial shuffle. A random orientation kontroll magasabb, mert megtartja a filament-strength és boundary mezőket; ez nem teljesen null kontroll, hanem orientációs specifikussági kontroll.

### 5.5 Következtetés

A synthetic recovery test:

```text
PASSED as method sanity check
```

De:

```text
nem bizonyít Tau Core-t,
csak megmutatja, hogy a statisztika visszanyer egy beültetett morfológiai residualt.
```

---

## 6. Sensitivity ladder

### 6.1 Cél

Megnéztük, milyen \(\epsilon_\tau\) residual-erősségnél kezd működni a MAR recovery.

Létra:

\[
\epsilon_\tau =
0.00,\ 0.005,\ 0.01,\ 0.015,\ 0.02,\ 0.03,\ 0.04,\ 0.06,\ 0.08,\ 0.10,\ 0.12
\]

Zajszintek:

\[
noise = 0.04,\ 0.06,\ 0.08
\]

### 6.2 \(C_\tau\) vs \(\epsilon_\tau\)

![Fig. 6 — C_tau vs epsilon](figures/fig06_c_tau_vs_epsilon.png)

**Értelmezés:** \(C_\tau\) monoton nő a beültetett Tau-residual erősségével. Ez a statisztika alapvető sanity check-je.

### 6.3 Konzervatív SNR

![Fig. 7 — SNR vs epsilon](figures/fig07_snr_vs_epsilon.png)

**Értelmezés:** az SNR túl hamar telítődik. Ennek oka, hogy a random orientation kontroll megtartja a filament-strength és boundary komponenseket, ezért nem igazi null.

### 6.4 Kontrollok közepes zajnál

![Fig. 8 — Controls at noise 0.06](figures/fig08_controls_noise_006.png)

**Értelmezés:** a teljes \(T_\tau\) erősebb, mint a baryon template vagy spatial shuffle, de a filament strength és random orientation kontroll részben követi. Ezért a végleges protokollnak nem elég egy sima korreláció.

### 6.5 Tanulság

A sensitivity ladder:

```text
PASSED, but overly optimistic
```

A fő javítás:

\[
Corr(\Delta\kappa,T_\tau)>0
\]

nem elég. Kell:

\[
T_\tau
>
T_{baryon}, T_{filament}, T_{boundary}, T_{sys}, T_{shuffle}
\]

vagy még jobb:

\[
\Delta R^2_\tau > 0
\quad \text{kontrollok után}
\]

---

## 7. Realistic noise stress test

### 7.1 Cél

A realisztikusabb stress testben hozzáadtuk:

```text
correlated shape-noise-like field
PSF/systematics-like contaminant
noisy baryonic map
filament orientation errors
imperfect baseline halo modeling
no-Tau control
```

### 7.2 Generatív modell

\[
\kappa_{obs}
=
\kappa_{base,true}
+
\epsilon_\tau T_{\tau,true}
+
\eta_{white}
+
\eta_{corr}
+
S_{sys}
\]

A mért residual:

\[
\Delta\kappa
=
\kappa_{obs}
-
\kappa_{base,model}
\]

A mért template már nem egyezik meg a valódi template-tel:

\[
T_{\tau,meas}
\neq
T_{\tau,true}
\]

mert hibás:

```text
filament orientation
baryon gradient
environment boundary field
```

### 7.3 Kontrollsávok

![Fig. 9 — Stress-test control bars](figures/fig09_stress_test_control_bars.png)

**Értelmezés:** a mild és medium esetben van pozitív \(T_\tau\) jel, de a systematics és filament-only template sokszor versenyképes vagy erősebb. Hard esetben a systematics dominál.

### 7.4 Hierarchikus stress score

![Fig. 10 — Stress-test Q scores](figures/fig10_stress_test_q_scores.png)

Pontszámok:

```text
mild:    Q_MAR = 5 / 10
medium:  Q_MAR = 4 / 10
hard:    Q_MAR = 4 / 10
no Tau:  Q_MAR = 2 / 10
```

Ez fontos, mert a no-Tau kontroll alacsonyabb, de a MAR még nem robusztus.

### 7.5 Medium residual és measured template

![Fig. 11 — Medium residual](figures/fig11_medium_delta_kappa.png)

![Fig. 12 — Medium measured Tau template](figures/fig12_medium_tau_template_measured.png)

**Értelmezés:** medium esetben a residualban még látszik morfológiai komponens, de a zaj és a systematics már erősen keveredik vele.

### 7.6 Hard residual és measured template

![Fig. 13 — Hard residual](figures/fig13_hard_delta_kappa.png)

![Fig. 14 — Hard measured Tau template](figures/fig14_hard_tau_template_measured.png)

**Értelmezés:** hard esetben a beültetett jel gyenge a zaj/systematics mellett. Itt a sima korrelációs MAR-claim nem lenne elfogadható.

### 7.7 Stress-test következtetés

A stress test státusza:

```text
PARTIAL / WARNING
```

A fő tanulság:

\[
Corr(\Delta\kappa,T_\tau)>0
\]

nem elég. A Tau-template-et versenyeztetni kell:

```text
systematics
baryon
filament-only
boundary
halo nuisance
spatial shuffle
random orientation
```

---

## 8. Systematics-separated regression

### 8.1 Motiváció

A stress test megmutatta, hogy a systematics és filament-only kontrollok néha dominálhatnak. Ezért a következő modell:

\[
\Delta\kappa
=
aT_\tau
+
bT_{sys}
+
cT_{baryon}
+
dT_{filament}
+
eT_{boundary}
+
fT_{halo}
+
\eta
\]

A kérdés:

\[
a \neq 0?
\]

marad-e, ha a kontrollok már bent vannak.

### 8.2 Inkrementális magyarázóerő

Definíció:

\[
\Delta R^2_\tau
=
R^2(T_\tau + Controls)
-
R^2(Controls)
\]

### 8.3 Residualizált partial correlation

Definíció:

\[
\rho_{\tau|controls}
=
Corr
\left(
\Delta\kappa_{\perp controls},
T_{\tau,\perp controls}
\right)
\]

ahol:

- \(\Delta\kappa_{\perp controls}\): residual, miután a kontroll-template-ek által magyarázott részt kivettük,
- \(T_{\tau,\perp controls}\): Tau-template, miután a kontroll-template-ekkel közös részt kivettük.

### 8.4 Eredmény: \(\Delta R^2_\tau\)

![Fig. 15 — Delta R2 Tau after controls](figures/fig15_delta_r2_tau_after_controls.png)

Eredmények:

```text
mild:    ΔR² ≈ 0.054
medium:  ΔR² ≈ 0.022
hard:    ΔR² ≈ 0.010
no Tau:  ΔR² ≈ 0.000
```

Ez nagyon egészséges viselkedés:

```text
van Tau-jel → pozitív inkrementális hozzájárulás
nincs Tau-jel → eltűnik
nagyobb zaj → gyengül
```

### 8.5 Ridge-koefficiensek

![Fig. 16 — Ridge coefficients](figures/fig16_ridge_coefficients_by_scenario.png)

**Értelmezés:** a Tau-koefficiens mild/medium/hard esetben pozitív marad, de a systematics és más kontrollok is jelentősek. Ez indokolja, hogy a MAR csak kontrollhierarchiával legyen értelmezve.

### 8.6 Residualizált Tau-jel

![Fig. 17 — Partial correlation Tau after controls](figures/fig17_partial_corr_tau_after_controls.png)

Eredmények:

```text
mild:    partial corr ≈ 0.28
medium:  partial corr ≈ 0.18
hard:    partial corr ≈ 0.11
no Tau:  partial corr ≈ 0.00
```

Ez a legfontosabb sanity check: no-Tau esetben eltűnik a residualizált Tau-jel.

### 8.7 Következtetés

A systematics-separated regression:

```text
PASSED as methodological improvement
```

A végleges MAR statisztika:

\[
\boxed{
\Delta R^2_\tau
=
R^2(T_\tau + Controls)
-
R^2(Controls)
}
\]

és:

\[
\boxed{
\rho_{\tau|controls}
>
0
}
\]

---

## 9. Véglegesített MAR-protokoll

### 9.1 Inputok

Szükséges adatok:

```text
observed lensing map: κ_obs vagy shear map
baseline lensing model: κ_base
baryonic mass map: Σ_b
cosmic web filament orientation: f_hat
filament strength / anisotropy: A_f
environment boundary map: B_env
systematics templates: PSF, masks, selection, survey artifacts
halo nuisance templates
redshift / tomography information, ha van
```

### 9.2 Lépések

#### Step 1 — residual

\[
\Delta \kappa(x)
=
\kappa_{obs}(x)
-
\kappa_{base}(x)
\]

#### Step 2 — Tau morphology template

\[
T_{\tau}(x)
=
B_{env}(x)
A_f(x)
M_{bf}(x)
\]

\[
M_{bf}(x)
=
1-
(\hat b(x)\cdot \hat f(x))^2
\]

#### Step 3 — control templates

\[
Controls =
\{
T_{sys},
T_{baryon},
T_{filament},
T_{boundary},
T_{halo},
T_{mask},
T_{PSF}
\}
\]

#### Step 4 — controls-only model

\[
\Delta\kappa
=
Controls
+
\eta
\]

#### Step 5 — controls + Tau model

\[
\Delta\kappa
=
aT_\tau
+
Controls
+
\eta
\]

#### Step 6 — incremental test

\[
\Delta R^2_\tau
=
R^2(T_\tau+Controls)
-
R^2(Controls)
\]

#### Step 7 — partial correlation

\[
\rho_{\tau|controls}
=
Corr
\left(
\Delta\kappa_{\perp controls},
T_{\tau,\perp controls}
\right)
\]

#### Step 8 — permutation

Randomizálandó:

```text
Tau template spatial location
filament orientation
boundary labels
object assignments
redshift slices
```

#### Step 9 — out-of-sample validation

A template-definíciót fagyasztani kell, majd új mintán futtatni.

---

## 10. Failure criteria

A MAR hipotézis gyengül vagy bukik, ha:

```text
1. ΔR²_tau ≈ 0 kontrollok után.
2. ρ_tau|controls ≈ 0.
3. A Tau-template nem jobb, mint systematics template.
4. A Tau-template nem jobb, mint filament-only template.
5. A Tau-template nem jobb, mint baryon template.
6. Az eredmény eltűnik spatial shuffle vagy random orientation kontroll után.
7. Csak utólag választott smoothing scale mellett működik.
8. Nem reprodukálható független mintán.
9. Shear, convergence, magnification és time-delay residualok inkompatibilisek.
10. A null–matter mismatch nem strukturált, hanem véletlenszerű.
```

---

## 11. Success criteria

A MAR hipotézis erősödik, ha:

```text
1. ΔR²_tau > 0 out-of-sample.
2. ρ_tau|controls > 0 out-of-sample.
3. Permutation p-value kicsi.
4. Systematics, baryon, filament-only és halo kontrollok után is marad Tau-hozzájárulás.
5. Van reprodukálható skálafüggő optimum R_tau*.
6. A jel boundary-régiókban erősebb.
7. A jel több survey-ben megjelenik.
8. A jel több observable-ben konzisztens:
   convergence, shear, magnification, time delay.
9. A matter-dynamics residual és photon-lensing residual strukturáltan kapcsolódik.
10. A null–matter mismatch korrelál ugyanazzal a T_tau template-tel.
```

---

## 12. Null–Matter Mismatch

### 12.1 Motiváció

A lencsézés foton/null-probe:

\[
\Delta \kappa_{\tau}
=
\mathcal{D}_{null}
[
\delta g_{\mu\nu}^{\tau}
]
\]

A galaxisrotáció masszív matter-probe:

\[
\delta a_{\tau}
=
\mathcal{D}_{matter}
[
\delta g_{\mu\nu}^{\tau}
]
\]

A kettő nem feltétlenül azonos projekció.

### 12.2 Mismatch definíció

\[
\Delta_{NM}
=
\Delta\kappa_{\tau}
-
\mathcal{T}
[
\delta a_{\tau}
]
\]

Tau Core-kompatibilis esetben nem véletlen mismatch kell, hanem strukturált:

\[
\Delta_{NM}
\sim
T_{\tau}
\]

Ez lenne erős későbbi teszt.

---

## 13. Observational roadmap

### 13.1 Első cél: weak lensing survey

Lehetséges adatirány:

```text
DES / KiDS / HSC / Euclid / LSST jellegű weak lensing térképek
```

Szükséges:

```text
κ vagy shear residual map
baryonic mass proxy
galaxy density / cosmic web reconstruction
filament orientation catalogue
systematics maps
masks
redshift slicing
```

### 13.2 Második cél: cluster lensing

Előny:

```text
erősebb jel
konkrét objektumok
multi-observable lehetőség
strong + weak lensing kombinálható
```

Hátrány:

```text
bonyolult baryon physics
merger history
gas offset
selection effects
```

### 13.3 Harmadik cél: CMB lensing

Előny:

```text
nagy skála
cosmic web-level probe
független photon population
```

Hátrány:

```text
foregrounds
beam systematics
projection complexity
```

---

## 14. Interpretációs státusz

A jelenlegi eredmény nem azt mondja:

```text
Tau Core bizonyított.
Dark matter cáfolva.
MAR megtalálva valódi adaton.
```

Hanem azt:

```text
A Photon–Lensing Bridge ad egy mérhető residual-keresési programot.
A MAR-template működik synthetic injection esetén.
A sima korreláció túl gyenge kritérium.
A systematics-separated ΔR² és partial correlation sokkal jobb.
Valódi adat előtt kontrollhierarchia és out-of-sample validation kell.
```

---

## 15. Végső paper-style summary

The Photon–Lensing Bridge treats photons as coherent null-channel readout probes of the effective metric structure. In this framework, gravitational lensing does not directly measure an ontologically primary dark component; it measures an effective metric residual, which may then be modeled as dark matter or, more generally, as a metric/readout tension.

The Morphological Alignment Residual module proposes that if part of this residual originates from parent-level morphology, then it may correlate with cosmic-web morphology beyond what is captured by baryonic density, filament strength alone, halo profiles, or survey systematics.

The core template is:

\[
T_{\tau}(x)
=
B_{env}(x)A_f(x)M_{bf}(x)
\]

with:

\[
M_{bf}(x)
=
1-
(\hat b(x)\cdot\hat f(x))^2
\]

The final statistic is not raw correlation but incremental explanatory power after controls:

\[
\Delta R^2_\tau
=
R^2(T_\tau+Controls)
-
R^2(Controls)
\]

and residualized partial correlation:

\[
\rho_{\tau|controls}
=
Corr
\left(
\Delta\kappa_{\perp controls},
T_{\tau,\perp controls}
\right)
\]

The synthetic tests show that the method can recover an injected morphology-aligned residual, but the stress tests also show that systematics can mimic or dominate simple MAR correlations. Therefore, a real-data claim requires strict control templates, permutation tests, multi-observable consistency, and out-of-sample replication.

---

## 16. Appendix A — current module status table

| Module | Status | Meaning |
|---|---:|---|
| Photon as null-readout | Conceptual bridge ready | Interpretive Tau Core EM sector |
| Photon–Lensing Bridge | Formal skeleton ready | Lensing as metric readout tomography |
| MAR hypothesis | Defined | Morphological residual template proposed |
| Synthetic recovery | Passed | Injected \(T_\tau\) recovered |
| Sensitivity ladder | Passed but optimistic | Correlation grows with \(\epsilon_\tau\) |
| Realistic stress test | Partial / warning | Systematics can dominate |
| Systematics separation | Passed as method improvement | \(\Delta R^2_\tau\) and partial corr behave correctly |
| Real-data validation | Not done | Required before any physical claim |

---

## 17. Appendix B — recommended next work

### B1c — Out-of-sample mock validation

Split the mock field into train and validation regions:

```text
train: fit/control template weights
validation: evaluate ΔR²_tau
```

Goal:

\[
\Delta R^2_{\tau,validation}>0
\]

### B1d — Multi-observable synthetic test

Add mock shear:

\[
\gamma_1,\gamma_2
\]

and require consistency with \(\kappa\).

### B1e — Real survey feasibility map

Identify exact public datasets:

```text
lensing map
baryon map
cosmic web catalogue
systematics maps
mask files
```

### B1f — Null–Matter Mismatch toy model

Add rotation residual:

\[
\delta a_\tau
\]

and test:

\[
\Delta_{NM}
\sim
T_\tau
\]

---

## 18. Appendix C — data files in this package

CSV files copied into `data/`:

```text
mar_toy_model_results.csv
mar_sensitivity_ladder_results.csv
mar_sensitivity_thresholds.csv
mar_realistic_stress_test_results.csv
mar_systematics_separation_results.csv
mar_systematics_separation_coefficients.csv
```

Figures copied into `figures/`.

---

## 19. One-line final result

\[
\boxed{
\text{MAR is not a claim of detection; it is a falsifiable Tau Core lensing residual protocol.}
}
\]

Magyarul:

\[
\boxed{
\text{A MAR nem detektálási állítás, hanem egy falszifikálható Tau Core lencsézési residual-protokoll.}
}
\]
