
# DevOps Lifecycle

Assignment II — Presentation on the continuous software delivery process.

---

## Topic

DevOps Lifecycle covers the eight-stage loop (Plan, Code, Build, Test, Release, Deploy, Operate, Monitor) that describes how modern engineering teams develop, ship, and maintain software in a continuous, feedback-driven manner.

---

## Slide Structure

| Slide | Title | Key Content |
|-------|-------|-------------|
| 1 | Title | Topic, course context |
| 2 | The Problem with Traditional Development | Silos, slow delivery, blame culture |
| 3 | What is DevOps? | Definition, four pillars |
| 4 | The DevOps Lifecycle | Infinity loop diagram |
| 5 | Developer to User — The Flow | Process flow diagram with feedback arrow |
| 6 | Lifecycle Stages — Development Side | Plan, Code, Build, Test |
| 7 | Lifecycle Stages — Operations Side | Release, Deploy, Operate, Monitor |
| 8 | Real-World Scenario: Swiggy | End-to-end feature delivery walkthrough |
| 9 | Why DevOps Delivers Business Value | DORA metrics, four key benefits |
| 10 | The Engine of DevOps: CI/CD | CI vs CD vs Continuous Deployment |
| 11 | Monitoring — The Heartbeat of DevOps | Four golden signals, feedback loop |
| 12 | Traditional Development vs DevOps | Side-by-side comparison table |
| 13 | Team Contributions | Member roles and responsibilities |
| 14 | References | Annotated source list |

---

## Diagrams

Two original diagrams are included in this repository and embedded in the presentation.

`DevOps_process_flow_diagram.png` — A linear flow from Developer through Code, Build, Test, Deploy, to User, with a feedback arrow looping back. Used on Slide 5.

`DevOps_lifecycle_infinity_loop_diagram.png` — The standard infinity loop representation of the DevOps lifecycle showing all eight stages. Used on Slide 4.

---

## Real-World Scenario

Slide 8 walks through how Swiggy's engineering team would ship a redesigned live order tracking feature using the DevOps lifecycle. The scenario covers a concrete problem (users abandoning orders due to lack of tracking visibility), moves through each lifecycle stage with specific tooling and decisions, and includes a canary deployment and a real-time rollback triggered by Datadog alerts.

---

## Key Concepts Covered

The presentation explains what DevOps is and why it emerged from the failures of traditional software development. It describes each lifecycle stage in detail, shows how CI/CD pipelines power the automation layer, explains why monitoring closes the loop between operations and planning, and compares DevOps practices against traditional approaches across six dimensions.

---

## References

Forsgren, N., Humble, J., & Kim, G. — Accelerate: The Science of Lean Software and DevOps. Presents DORA metrics framework with causal links between technical practices and organizational outcomes.

AWS DevOps Documentation — aws.amazon.com/devops/what-is-devops. Practitioner-level reference linking lifecycle theory to cloud architecture patterns.

Microsoft Learn DevOps Resource Center — learn.microsoft.com/devops. Covers DevOps maturity models and enterprise adoption paths from beginner to advanced pipeline design.

Google Cloud — DORA State of DevOps Report 2023. Quantitative annual survey tracking deployment frequency, lead time, MTTR, and change failure rate across thousands of organizations globally.

---

## Files

```
DevOps_Lifecycle_Presentation.pptx
DevOps_process_flow_diagram.png
DevOps_lifecycle_infinity_loop_diagram.png
README.md
```
