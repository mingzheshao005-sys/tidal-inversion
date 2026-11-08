# Result-table guide

- model_error_metrics.csv: all nine models; prediction error, likelihood diagnostics and reference-normalized posterior displacement.
- model_posteriors_4097.csv: 4097-point approximate-posterior statistics for all nine models.
- direction_cases_25.csv: zero baseline and all signed direction/amplitude controls.
- response_approximation_cases_25.csv: cached, affine-in-n and affine-in-n-squared response comparisons; original prior retained.
- likelihood_scale_cases_27.csv: fixed observations and 1 mm perturbations at three likelihood scales; not repeated-noise coverage experiments.
- direct_diagnostics.json and delayed_acceptance_diagnostics.json: saved sampling summaries; raw chains are not part of this public subset.

Manning coefficient and its dimensional summary statistics are in s m^(-1/3); water level in metres unless a field explicitly states otherwise; discharge per unit width in m^2/s. Reference-normalized shifts are dimensionless. `refSD` uses the original reference SD 0.0016200408022456227 unless a field identifies the same-scale reference. Preserve signed shifts and do not confuse posterior displacement with error relative to the generating parameter. Original field names and numeric precision are preserved.
