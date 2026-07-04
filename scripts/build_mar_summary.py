from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"


def stat_value(df: pd.DataFrame, name: str) -> float:
    row = df[df["Statistic"] == name]
    if row.empty:
        raise KeyError(name)
    return float(row["Value"].iloc[0])


def main() -> None:
    toy = pd.read_csv(DERIVED / "mar_toy_model_results.csv")
    thresholds = pd.read_csv(DERIVED / "mar_sensitivity_thresholds.csv")
    stress = pd.read_csv(DERIVED / "mar_realistic_stress_test_results.csv")
    sep = pd.read_csv(DERIVED / "mar_systematics_separation_results.csv")

    rows: list[tuple[str, float | str]] = [
        ("claim_boundary", "synthetic_methodology_not_empirical_validation"),
        ("toy_c_tau", stat_value(toy, "C_tau: Corr(Δκ, T_tau)")),
        ("toy_random_orientation_mean", stat_value(toy, "Random-orientation mean")),
        ("toy_spatial_shuffle_mean", stat_value(toy, "Spatial-shuffle mean")),
        ("toy_baryon_template_corr", stat_value(toy, "Baryon template Corr")),
        ("toy_filament_only_corr", stat_value(toy, "Filament-only Corr")),
        ("sensitivity_min_epsilon_overall", float(thresholds["epsilon_tau_min_detected"].min())),
        ("sensitivity_max_min_detected", float(thresholds["epsilon_tau_min_detected"].max())),
    ]

    for _, row in stress.iterrows():
        prefix = f"stress_{row['name']}"
        rows.extend(
            [
                (f"{prefix}_c_real", float(row["C_real"])),
                (f"{prefix}_q_mar_0_to_10", float(row["Q_MAR_0_to_10"])),
                (f"{prefix}_p_shuffle", float(row["p_shuffle"])),
                (f"{prefix}_p_random_orientation", float(row["p_random_orientation"])),
                (f"{prefix}_c_systematic_template", float(row["C_systematic_template"])),
            ]
        )

    for _, row in sep.iterrows():
        prefix = f"systematics_{row['scenario']}"
        rows.extend(
            [
                (f"{prefix}_delta_r2_tau_after_controls", float(row["Delta_R2_tau_after_controls"])),
                (f"{prefix}_partial_corr_residualized_tau", float(row["PartialCorr_residualized_Tau"])),
                (f"{prefix}_permutation_p_tau_increment", float(row["Permutation_p_tau_increment"])),
                (f"{prefix}_tau_coef", float(row["Tau_coef"])),
                (f"{prefix}_systematic_coef", float(row["Systematic_coef"])),
            ]
        )

    summary = pd.DataFrame(rows, columns=["metric", "value"])
    summary.to_csv(DERIVED / "paper18_mar_summary.csv", index=False)

    payload = {metric: value for metric, value in rows}
    (DERIVED / "paper18_mar_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
