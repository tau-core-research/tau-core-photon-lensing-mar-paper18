from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "data" / "derived"
FIG = ROOT / "figures"
PAPER_FIG = ROOT / "paper18_submission_source" / "figures"


def save(fig: plt.Figure, name: str) -> None:
    for out_dir in (FIG, PAPER_FIG):
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_dir / name, bbox_inches="tight")
    plt.close(fig)


def build_protocol_figure() -> None:
    fig, ax = plt.subplots(figsize=(10.8, 5.8))
    ax.set_axis_off()
    boxes = [
        (0.05, 0.62, 0.22, 0.18, "Source-side\nmorphology"),
        (0.35, 0.76, 0.20, 0.13, "$B_{env}$\nboundary"),
        (0.35, 0.58, 0.20, 0.13, "$A_f$\nfilament strength"),
        (0.35, 0.40, 0.20, 0.13, "$M_{bf}$\nbaryon-filament\nmismatch"),
        (0.66, 0.58, 0.24, 0.16, "$T_\\tau=B_{env}A_fM_{bf}$\nMAR template"),
        (0.66, 0.28, 0.24, 0.14, "$C_\\tau=Corr(\\Delta\\kappa,T_\\tau)$\nwith controls"),
    ]
    for x, y, w, h, text in boxes:
        ax.add_patch(plt.Rectangle((x, y), w, h, fc="#eef3fb", ec="#345995", lw=1.4))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=10)
    arrows = [
        ((0.27, 0.71), (0.35, 0.825)),
        ((0.27, 0.71), (0.35, 0.645)),
        ((0.27, 0.71), (0.35, 0.465)),
        ((0.55, 0.825), (0.66, 0.66)),
        ((0.55, 0.645), (0.66, 0.66)),
        ((0.55, 0.465), (0.66, 0.66)),
        ((0.78, 0.58), (0.78, 0.42)),
    ]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.text(
        0.50,
        0.08,
        "Non-circular rule: T_tau is built before looking at the lensing residual.",
        ha="center",
        fontsize=10,
    )
    save(fig, "fig_mar_protocol.pdf")


def build_sensitivity_figure() -> None:
    df = pd.read_csv(DERIVED / "mar_sensitivity_ladder_results.csv")
    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    for noise, group in df.groupby("noise_level"):
        group = group.sort_values("epsilon_tau")
        ax.plot(group["epsilon_tau"], group["C_tau"], marker="o", lw=2, label=f"noise={noise:.2f}")
    ax.set_xlabel(r"injected $\epsilon_\tau$")
    ax.set_ylabel(r"$C_\tau=Corr(\Delta\kappa,T_\tau)$")
    ax.set_title("MAR sensitivity ladder")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    save(fig, "fig_mar_sensitivity_ladder.pdf")


def build_stress_figure() -> None:
    df = pd.read_csv(DERIVED / "mar_realistic_stress_test_results.csv")
    x = np.arange(len(df))
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.8))
    axes[0].bar(x - 0.2, df["C_real"], width=0.4, label="MAR measured", color="#2374ab")
    axes[0].bar(x + 0.2, df["C_systematic_template"], width=0.4, label="systematic template", color="#b45f5f")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(df["name"], rotation=20, ha="right")
    axes[0].set_ylabel("correlation")
    axes[0].set_title("Stress test: MAR versus systematics")
    axes[0].legend(frameon=False, fontsize=8)
    axes[0].grid(axis="y", alpha=0.25)

    axes[1].bar(x, df["Q_MAR_0_to_10"], color="#3b78b4")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(df["name"], rotation=20, ha="right")
    axes[1].set_ylim(0, 10)
    axes[1].set_ylabel("Q_MAR score")
    axes[1].set_title("Hierarchical stress score")
    axes[1].grid(axis="y", alpha=0.25)
    save(fig, "fig_mar_stress_summary.pdf")


def build_systematics_figure() -> None:
    df = pd.read_csv(DERIVED / "mar_systematics_separation_results.csv")
    x = np.arange(len(df))
    fig, ax = plt.subplots(figsize=(8.8, 5.0))
    ax.bar(x, df["Delta_R2_tau_after_controls"], color="#59a14f")
    ax.axhline(0, color="black", lw=1)
    ax.set_xticks(x)
    ax.set_xticklabels(df["scenario"], rotation=20, ha="right")
    ax.set_ylabel(r"$\Delta R^2_\tau$ after controls")
    ax.set_title("Systematics-separated Tau-template increment")
    ax.grid(axis="y", alpha=0.25)
    save(fig, "fig_mar_delta_r2_after_controls.pdf")


def main() -> None:
    build_protocol_figure()
    build_sensitivity_figure()
    build_stress_figure()
    build_systematics_figure()
    print("PAPER18_FIGURES_BUILT")


if __name__ == "__main__":
    main()
