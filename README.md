# Tidal inversion: public supporting materials

Supporting materials for the manuscript **Diagnosing surrogate-induced posterior shifts in tidal friction inversion: An idealized 1D channel benchmark**.

Authors: Bo-Ran Ren, Ming-Zhe Shao, Cai-Ren Jian. The first two authors contributed equally. This repository does not imply journal acceptance or publication.

## Public scope

This repository provides saved numerical summary tables, direct and delayed-acceptance diagnostic summaries, and a peripheral plotting script. It documents a synthetic, fully wet, one-dimensional, single-parameter friction inversion. It contains no real-estuary calibration data.

Run `python -m pip install -r requirements.txt`, then `python reproduce_summary_figures.py`. This recreates Figures 2, 4 and 5 from the saved summaries and writes PNG, PDF and SVG files to `Figures/`. It does not execute a hydrodynamic solver, train a network, run MCMC, or independently regenerate the published statistics. Figures 1 and 3 require chain or pointwise inputs not included in this public subset.

## Core code and requests

The core hydrodynamic solver, neural-network training code, inference implementation, trained weights and full computational archive are not publicly distributed, at the authors' request to retain control over redistribution of their implementation. They are available from the authors upon reasonable request, subject to agreement on use and redistribution. No legal or third-party restriction is asserted.

To request access, open an issue in this repository describing the material needed and intended research or verification use. The repository maintainer will coordinate the request with the authors, including the corresponding author, Cai-Ren Jian. Do not post confidential information in a public issue. No response time or approval is guaranteed. The corresponding-author email will be added when supplied.

This is a **partial public reproducibility package**, not a fully open-source implementation. Its availability does not by itself establish compliance with any journal's data/code policy. Editors may require further materials or reviewer access.

## Scientific boundaries

Prediction RMSE and posterior displacement need not rank the nine fixed surrogates identically. Equal-magnitude error controls test local sensitivity alignment; they do not establish a universal error theorem. The delayed-acceptance run did not pass its preset ESS/MCSE gates. No end-to-end speedup or real-estuary validation is claimed.

## Files and provenance

`Numerical_data/` contains five CSV result tables and two diagnostic JSON summaries copied from the manuscript package. `SHA256_manifest.json` records file checksums. The figures and statistics originate from previously completed computations; preparing this repository involved no new scientific experiments. AI assistance was used in drafting and computational preparation; scientific responsibility remains with the human authors.

## Citation and reuse

Cite the authors, manuscript title, repository URL and the exact Git commit used. No DOI or journal publication identifier has been assigned. See `RIGHTS.md` for reuse status. Public visibility is not a technical guarantee against copying.
