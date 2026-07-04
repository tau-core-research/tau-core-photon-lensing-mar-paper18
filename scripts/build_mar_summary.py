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
    v2_scores = pd.read_csv(DERIVED / "mar_v2_current_scores.csv")
    b1c = pd.read_csv(DERIVED / "mar_b1c_oos_scale_validation_aggregate.csv")
    b1d2 = pd.read_csv(DERIVED / "mar_b1d2_physical_shear_aggregate.csv")
    b1e = pd.read_csv(DERIVED / "mar_b1e_null_matter_link_results.csv")

    score_total = float(v2_scores["Score"].sum())
    score_max = float(v2_scores["Max"].sum())
    tau_b1c = b1c[b1c["condition"] == "tau_injected"].copy()
    best_b1c = tau_b1c.sort_values("Delta_R2_mean", ascending=False).iloc[0]

    def b1c_at(condition: str, scale: float, column: str) -> float:
        row = b1c[
            (b1c["condition"] == condition)
            & (abs(b1c["scale_sigma"] - scale) < 1e-12)
        ]
        if row.empty:
            raise KeyError(f"{condition} scale={scale} {column}")
        return float(row[column].iloc[0])

    def b1d2_value(observable: str, column: str) -> float:
        row = b1d2[b1d2["observable"] == observable]
        if row.empty:
            raise KeyError(f"{observable} {column}")
        return float(row[column].iloc[0])

    def b1e_value(test: str, column: str) -> float:
        row = b1e[b1e["test"] == test]
        if row.empty:
            raise KeyError(f"{test} {column}")
        return float(row[column].iloc[0])

    rows: list[tuple[str, float | str]] = [
        ("claim_boundary", "controlled_synthetic_mock_protocol_not_observational_evidence"),
        ("toy_c_tau", stat_value(toy, "C_tau: Corr(Δκ, T_tau)")),
        ("toy_random_orientation_mean", stat_value(toy, "Random-orientation mean")),
        ("toy_spatial_shuffle_mean", stat_value(toy, "Spatial-shuffle mean")),
        ("toy_baryon_template_corr", stat_value(toy, "Baryon template Corr")),
        ("toy_filament_only_corr", stat_value(toy, "Filament-only Corr")),
        ("sensitivity_min_epsilon_overall", float(thresholds["epsilon_tau_min_detected"].min())),
        ("sensitivity_max_min_detected", float(thresholds["epsilon_tau_min_detected"].max())),
        ("mar_v2_score_total", score_total),
        ("mar_v2_score_max", score_max),
        ("mar_v2_score_fraction", score_total / score_max),
        ("b1c_best_tau_injected_scale_sigma", float(best_b1c["scale_sigma"])),
        ("b1c_best_tau_injected_delta_r2_mean", float(best_b1c["Delta_R2_mean"])),
        ("b1c_best_tau_injected_partial_corr_mean", float(best_b1c["PartialCorr_mean"])),
        ("b1c_tau_injected_scale_2_2_delta_r2_mean", b1c_at("tau_injected", 2.2, "Delta_R2_mean")),
        ("b1c_no_tau_scale_2_2_delta_r2_mean", b1c_at("no_tau_control", 2.2, "Delta_R2_mean")),
        ("b1d2_kappa_delta_r2_mean", b1d2_value("kappa", "Delta_R2_mean")),
        ("b1d2_gamma1_physical_delta_r2_mean", b1d2_value("gamma1_physical", "Delta_R2_mean")),
        ("b1d2_gamma2_physical_delta_r2_mean", b1d2_value("gamma2_physical", "Delta_R2_mean")),
        ("b1d2_joint_physical_kappa_gamma_delta_r2_mean", b1d2_value("joint_physical_kappa_gamma", "Delta_R2_mean")),
        (
            "b1e_lensing_residual_after_matter_transfer_delta_r2",
            b1e_value("lensing_residual_after_matter_transfer_controls", "Delta_R2_tau_validation"),
        ),
        (
            "b1e_lensing_residual_after_matter_transfer_partial_corr",
            b1e_value(
                "lensing_residual_after_matter_transfer_controls",
                "PartialCorr_NullMatterMismatch_Tau",
            ),
        ),
        (
            "b1e_lensing_residual_after_matter_transfer_permutation_p",
            b1e_value("lensing_residual_after_matter_transfer_controls", "Permutation_p_partial_corr"),
        ),
        (
            "b1e_matter_dynamics_residual_controls_delta_r2",
            b1e_value("matter_dynamics_residual_controls", "Delta_R2_tau_validation"),
        ),
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
