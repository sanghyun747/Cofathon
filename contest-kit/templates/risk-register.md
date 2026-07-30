# Risk register

| Risk | Trigger | Impact | Prevention | Fallback | Evidence |
|---|---|---|---|---|---|
| Temporal leakage | Future data enters train features | Invalid offline score | Chronological split and feature cutoff | Rebuild baseline | |
| Cold start | New user/item or missing attributes | Empty/poor recommendations | Popularity/metadata fallback | Return eligible fallback list | |
| Invalid model output | Malformed schema or hallucinated ID | Crash or bad action | Schema and ID validation | Deterministic baseline | |
| API timeout | Remote call exceeds budget | Incomplete result | Timeout, cache, bounded retry | Last champion | |
| Secret leakage | Key appears in file/log | Security failure | Environment variables and secret scan | Remove file and rotate if exposed | |
| Submission failure | Wrong entrypoint or ZIP | No valid result | Fresh preflight and early bundle | Upload last verified bundle | |
