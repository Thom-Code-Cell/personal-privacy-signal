# Confirmatory analysis preregistration — required fields

Status: TEMPLATE / NOT_APPROVED / NO_DATA. Does not authorize a study or invent
measurements. Complete, version and timestamp before confirmatory collection;
obtain independent method/privacy review. Exploratory results stay exploratory.

| Field | Required decision before collection |
|---|---|
| Scope | hypothesis ID, implementation/spec/firmware SHA, settings, population and conditions |
| Estimand | precise numerator/denominator, unit and target population for each primary outcome |
| Trial/cluster unit | distinguish event, participant, device and session; repeated packets are not trials |
| Primary endpoints | choose before data; separate detection, false binding, coverage/ambiguity, latency and enforcement |
| Decision rule | declare point estimate versus one-sided confidence bound, level and inequality explicitly |
| Sample size | calculate for each critical condition and clustering assumption; justify precision/power |
| Analysis | fixed interval/cluster method, verified implementation/version and synthetic worked example |
| Multiple conditions | preselect primary cells; simultaneous uncertainty or multiplicity approach; no favorable pooling |
| Missingness/aborts | count all scheduled trials, distinguish technical loss, withdrawal and safety stop; no silent exclusion |
| Ground truth | independent observer method, blinding, random seed and measurement-clock uncertainty |
| Deviations | record timing/reason; amendments after seeing outcomes become exploratory/new protocol |
| Ethics/privacy | consenting responsible roles, stop/deletion/access plan and operator authority |
| Outputs | reviewed aggregates, exact reproduction, negative results and residual limits |

For ≥95% detection targets, explicitly choose whether a lower one-sided bound
must be ≥0.95; a point estimate of 0.95 does not establish that bound. For a <1%
error target, explicitly select the upper-bound rule and denominator, and report
coverage/ambiguity too. No default statistical procedure is approved here.

For illustration under independent Bernoulli trials only, zero errors at n=300
gives the exact one-sided 95% upper bound `1 - 0.05**(1/300)`, about 0.009936.
For three independent Poisson observation-hours with zero events, the analogous
rate bound is `-log(0.05)/3`, about 0.9986/hour. Dependence or changing rates invalidate
those simple assumptions; real clustered data require a justified method/sample plan.

Have a statistician/method reviewer check the completed plan and synthetic
calculation before people/device research. Templates and green parser tests are
not a measurement of safe field performance.
