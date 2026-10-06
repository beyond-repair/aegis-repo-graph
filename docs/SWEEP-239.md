# Sweep-239 — 2026-10-06

Selection: random.SystemRandom().choice over 81 names (search total 83, excluding sunder and ADL-Governance as the immediately prior subject and the governance host).

Subject: aegis-repo-graph.

Classification: RESEARCH. Claim <=1. Reconfirmed. Catalog row still stores integer claim 3 as snapshot data.

Pre-head: 98bac63122d060a51a21f023bcf3328a82eb6cc2. CI run 37402540834 success on that head. Local pytest before this change: 10 passed. Engine: artifacts=73 relationships=21 OK.

Finding: CLAIM_STATUS cited run 37069800025 as current evidence after a later green run. Locked catalog is 72 repository names versus search 83. Drift is documented, not absorbed.

Action: add frozen observation and name_drift. Do not edit catalog rows. Version 0.1.2.

Not claimed: live completeness, FLS compiler, Nehemiah host, census built.
