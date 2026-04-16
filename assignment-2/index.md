# DevOps Overview and Evolution

Assignment II — Topic 1. A presentation on how software development evolved from traditional Waterfall to Agile to DevOps, covering the historical context, core principles, and business case for the DevOps model.

---

## Context

This presentation was originally prepared for Topic 5 (DevOps Lifecycle). Upon clarifying the assignment allocation, it was rebuilt for the assigned topic — DevOps Overview and Evolution — with fully original content, a scenario-based example, and all required diagrams. That clarification is noted on the title slide.

---

## Slide Structure

| Slide | Title | Key Content |
|-------|-------|-------------|
| 1 | Title | Topic, assignment context, clarification note |
| 2 | The World Before DevOps | Waterfall phases, why each one failed |
| 3 | Core Problems — Why Traditional Development Failed | Six systemic failures |
| 4 | Agile — The First Step Toward Speed | What Agile solved and what it left unsolved |
| 5 | The Evolution of Software Development | Evolution diagram: Waterfall → Agile → DevOps |
| 6 | Traditional, Agile, and DevOps Side by Side | Team structure illustration |
| 7 | What is DevOps? | Definition, four pillars |
| 8 | DevOps Core Principles | Five practices with explanations |
| 9 | Traditional vs DevOps — Key Contrasts | Comparison image with written analysis |
| 10 | Comparison at a Glance | Six-dimension comparison table |
| 11 | Real-World Scenario: Zomato | Traditional vs DevOps side-by-side on the same problem |
| 12 | Business Value of DevOps | DORA metrics, four benefit categories |
| 13 | DevOps Across the Industry | Amazon, Netflix, Flipkart adoption patterns |
| 14 | Team Contributions | Member roles |
| 15 | References | Annotated source list |

---

## Diagrams

Three diagrams are included in this repository and embedded in the presentation.

`evolution_diagram.png` — Waterfall (linear stack of Requirements → Design → Development → Testing → Deployment), Agile (iterative cycle), and DevOps (infinity loop), shown side by side with arrows indicating progression. Used on Slide 5.

`trad_agile_devops_illustration.png` — Illustration contrasting isolated Dev and Ops buildings under a time bottleneck (Traditional/Agile) with a unified collaborative team working on shared pipelines and dashboards (DevOps). Used on Slide 6.

`trad_vs_devops_comparison.png` — Side-by-side icon comparison: siloed/collaborative teams, slow/fast delivery, late/continuous testing, manual/automated processes. Used on Slide 9.

---

## Real-World Scenario

Slide 11 presents Zomato's restaurant rating system overhaul as a direct comparison between how a traditional team and a DevOps team would approach the same problem. The traditional path takes six months and results in a four-hour outage. The DevOps path takes eleven days, with zero downtime, using feature flags, a canary deployment to 1% of users, and automated rollback thresholds configured in the pipeline before launch.

---

## Key Concepts Covered

The presentation traces the evolution of software development from the rigid Waterfall model through Agile's iterative improvements and into DevOps as the current standard for high-performing engineering organizations. It explains why each transition was driven by the failures of the previous model, not by theory. It covers the four pillars of DevOps (culture, automation, measurement, sharing), the five core practices (CI, CD, Infrastructure as Code, monitoring, feedback loops), and supports each with DORA research data and real industry examples.

---

## References

Forsgren, N., Humble, J., & Kim, G. — Accelerate: The Science of Lean Software and DevOps (2018). Primary source for DORA metrics. Establishes causal links between DevOps practices and organizational outcomes using four-year longitudinal survey data.

AWS DevOps Documentation — aws.amazon.com/devops/what-is-devops. Practitioner-level reference covering principles, CI/CD pipeline design, and toolchain patterns for cloud environments.

Microsoft Learn DevOps Resource Center — learn.microsoft.com/devops. Covers DevOps maturity models and enterprise adoption paths from beginner to advanced pipeline design.

Google Cloud — DORA State of DevOps Report 2023. Annual survey of 32,000+ engineering professionals tracking deployment frequency, lead time, mean time to restore, and change failure rate across industries.

---

## Files

```
DevOps_Overview_Evolution.pptx
evolution_diagram.png
trad_agile_devops_illustration.png
trad_vs_devops_comparison.png
README.md
```
