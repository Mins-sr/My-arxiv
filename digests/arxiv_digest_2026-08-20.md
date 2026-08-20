# arXiv Daily Digest - 2026-08-20

Total papers: 350

---

## cs.AI

**50 papers**

### 1. SPADE: Self-Play in Adaptive Synthetic Executable Environments

**Authors:** Bo Liu, Simon Yu, Yiding Jiang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19197v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19197v1)

**Summary:** Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environment pools (hand-curated, statically synthesized, or frozen-verifier) keep the goal distribution fixed as the learner scales. We introduce SPADE (Self-Play in Adaptive Synthetic Executable Environments), a self-play RL framework in which a single LLM plays two roles: an Environment Designer that writes complete, long-horizon training environments a...

---

### 2. ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning

**Authors:** Jayjun Lee, Jessica Yin, Asif Rana, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19182v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19182v1)

**Summary:** We introduce Accelerating Dexterity via Pre-Training (ADEPT), a large-scale reinforcement learning (RL) framework for learning sim-to-real transferable dexterity across high degree-of-freedom (DoF) robot embodiments that can solve long-horizon tasks directly from raw visuo-tactile perception. ADEPT pretrains a dexterous policy on a generic object reposing task, then post-trains downstream policies with this pretrained behavior as a prior. ADEPT enables learning new behaviors that are otherwise d...

---

### 3. Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning

**Authors:** Zhu Zhang, Jixun Wang, Xiaoang Xu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19181v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19181v1)

**Summary:** On-policy distillation (OPD) trains a student on its own responses using dense token-level guidance from a stronger teacher. In long-context tasks, however, token-level teacher support can favor locally plausible responses that omit evidence distributed across the input or violate global task constraints. Task-specific verifiers, in contrast, evaluate task completion at the response level and may return graded rewards that reflect partial success. We diagnose this mismatch on fixed responses fro...

---

### 4. Finetuning Strategies for Querying Sounds by Vocal Imitation

**Authors:** Aditya Bhattacharjee, Christos Plachouras, Sungkyun Chang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19174v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19174v1)

**Summary:** This technical report describes our winning submission to the AES AIMLA 2025 Challenge on querying sound effects by vocal imitation. We investigate two complementary fine-tuning strategies: contrastive learning with a frozen, pretrained CED encoder, and joint contrastive-triplet learning with semi-hard negatives using a MobileNetV3 encoder. This report has been updated for posterity to include details released after the challenge.

---

### 5. Interpretable AI predicts a 2026 summer dry anomaly in central China

**Authors:** Anran Wang, Wen Shi, Yong Luo, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19163v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19163v1)

**Summary:** Seasonal precipitation anomalies are largely regulated by atmospheric circulation, which dynamical models predict with greater reliability than precipitation itself. Here, we employ a deep learning model that translates dynamical circulation predictions into precipitation estimates. Predictions initialized from March to May consistently indicate a dry anomaly over central China in summer 2026. Retrospective evaluations revealed higher predictive skill in the analogue years, which also tended to ...

---

### 6. Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication

**Authors:** Ramneet Kaur, Pradyumna Chari, Ramesh Raskar, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19161v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19161v1)

**Summary:** Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent Alignments (VLA), an activation-aware framework for monitoring and steering these private communication channels. For every monitored decision, VLA links the private latent-state record and channel status to the resulting public action using a shared event identifier, enabling matched causal analysi...

---

### 7. Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets

**Authors:** Tate Berenbaum, Muthaiah Venkatachalam

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19147v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19147v1)

**Summary:** Modern Intel AI PCs ship capable integrated GPUs and NPUs with 16+ GB of unified memory, and they spend considerable time idle. That is not enough memory to fit a large model such as a 70B-parameter LLM. We show that a handful of AIPCs, working together over an ordinary network, can serve models beyond the capability of any single one. We use pipeline parallelism: a model is split by layer into per-stage shards, each pre-compiled into an OpenVINO graph, so that every machine runs one shard and p...

---

### 8. Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems

**Authors:** George Andrikopoulos

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19140v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19140v1)

**Summary:** Frontier language models are compared, marketed, and benchmarked on capability -- what their best or average output can achieve. I argue this measures the wrong axis. The models have saturated accuracy: their mean output lands on the target. What now separates one system from another in practice is precision: how tightly concentrated their outputs are around that target across repeated, identical requests. Borrowing the marksman's distinction, capability is where the average shot lands; reliabil...

---

### 9. Leaf Values as Coordinates: Exact Contrastive Explanation for Gradient-Boosted Ensembles

**Authors:** Emanuele Luzio

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19127v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19127v1)

**Summary:** A gradient-boosted ensemble predicts by summing one leaf value per tree. Read   those values as coordinates rather than as intermediate results, and every   instance becomes a point in R^M on which the model acts linearly: the score is   the sum of the coordinates.   This small change of view makes contrastive explanation exact. The difference   between two instances is a vector that is identically zero wherever they share   a leaf, so the gap between a rejected applicant and an accepted one is ...

---

### 10. Tuning the Stochastic Machine: A Systems Engineer's Operating Model for Human-AI Engineering

**Authors:** George Andrikopoulos

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19125v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19125v1)

**Summary:** When an expert corrects an LLM assistant's error, the correction usually dies with the session, and the error class returns. I argue this is an operations problem, not a tooling problem: mechanisms for persisting corrections exist and are shipping, but the discipline for governing them -- versioning with provenance, recurrence monitoring, counter-metrics, retirement of stale rules -- does not. Writing as a systems engineer of thirty years, I map the LLM stack onto the machines my profession alre...

---

### 11. PGFS++: Molecular Property Improvement under Synthesis and Diversity Constraints

**Authors:** Boqiao Zhang, Godbless James, Sai Krishna Gottipati, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19121v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19121v1)

**Summary:** Improving molecular properties, such as drug-likeness or binding affinity, is a recurring task in early-stage drug discovery. However, molecules optimized in an unconstrained chemical space have limited practical value if they cannot be synthesized. Policy Gradient for Forward Synthesis (PGFS) is a synthesis-aware reinforcement learning method for molecular improvement, but its use of reactant embedding prediction makes reactant selection indirect, which, as we show, limits learning effectivenes...

---

### 12. Discretizing Continuous Time Series for Imputation with Masked Diffusion Training

**Authors:** Dongbin Kim, Seungyun Lee, Geonwoo Shin, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19119v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19119v1)

**Summary:** Time series imputation is a crucial area for reliable time series analysis, yet it remains challenging due to the complex temporal dynamics and noise of real-world data. Existing approaches, however, exhibit two limitations: missing and observed values are embedded within the same representation space without explicit structural separation, and continuous diffusion-based methods are trained to predict added noise rather than the original signal. To address these, we propose the Masked Diffusion ...

---

### 13. Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation

**Authors:** Huan-ang Gao, Haohan Chi, Yong Yan, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19098v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19098v1)

**Summary:** Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) experts into a single generalist student via dense, token-level reward supervision. Despite its practical success, the optimization dynamics governing multi-teacher capability integration remain poorly understood, and open, rigorously reproducible recipes are conspicuously lacking. In this work, we establish a controlled M-OPD benchmark on SmolLM3-3B-B...

---

### 14. Detecting Backdoors in Object Detection via Pre-NMS Prediction Distribution Shift

**Authors:** Longtian Wang, Zhengyu Zhao, Chenhao Lin, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19088v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19088v1)

**Summary:** Object detection models deployed in safety-critical applications remain vulnerable to backdoor attacks that cause targeted misbehaviors when a hidden trigger is present. Existing detection methods either rely on trigger inversion or exploit architecture-specific assumptions, and critically, representative existing methods fail to generalize reliably to scene-level attacks, where a single trigger induces anomalous behavior across all objects in the scene simultaneously. We present DistScan, a bac...

---

### 15. DA-WAM: Decision-Aligned Future Latents for Driving World Models

**Authors:** Ruiguo Zhong, Benshan Ma, Xiaolong Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19085v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19085v1)

**Summary:** Anticipating how scenes evolve under ego actions is fundamental to safe autonomous driving, yet the full potential of world models for decision-making remains unrealized. The critical challenge lies in ensuring that future modeling is not merely predictive, but decision-informative: the predicted future must directly shape which trajectory is selected. Existing approaches decouple future representation learning from planning optimization, or share predicted states across trajectory candidates, t...

---

### 16. ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate Hallucinations in Large Vision-Language Models

**Authors:** Jihae Jeong, Junha Choi, Hwanjo Yu

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19075v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19075v1)

**Summary:** Large vision-language models (LVLMs) often hallucinate, generating content that the input image does not support. Preventing such content during decoding calls for a candidate-specific measure of how strongly the image supports the token under consideration. The model's visual-token states offer a natural source of this evidence because projecting each state through the output head reveals which vocabulary items that position favors. These position-wise readouts cannot be pooled directly because...

---

### 17. Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk

**Authors:** Deep Kumar Ganguly, Jan Křetínský

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19073v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19073v1)

**Summary:** An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a robust-optimization identity---a confidence level fixes the radius of a relative-entropy ball of alternative models---but that ball cannot reach catastrophes the nominal deems impossible, precisely what a safe agent must hedge. We instead use an optimal-transport ball and study the coherent risk measure it induces, the Wasserstein entropic value-at...

---

### 18. What is Missing from AI Post-Training AI: An Empirical Analysis

**Authors:** Joy Jia Yin Lim, Xin Huang, Hao Peng, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19072v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19072v1)

**Summary:** Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-AI. We argue that this picture conflates two distinct capabilities: execution-level capability, iterating within a selected training strategy; and strategy-level capability, revising the high-level judgment as experimental evidence accumulates. Analyzing a large corpus of publicly released post-train...

---

### 19. GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting

**Authors:** Yechan Park, HyunJin Kim

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19066v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19066v1)

**Summary:** This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displaceme...

---

### 20. Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery

**Authors:** Alizer Wong, Heng Cui, Yi Tan, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19047v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19047v1)

**Summary:** We present Eureka, a task-conditioned Meta-Agent architecture that compiles long-horizon tasks into dynamic obligation graphs with explicit acceptance semantics. During execution, Eureka forms Macro-Agents with specialized state, memory, operators, tools, verifiers, and local topology via receding-horizon planning, architecture promotion, and minimal-sufficient compilation. When bottlenecks recur, cost-benefit-gated evolution updates the local architecture under constraints. Theoretically, we es...

---

### 21. Bernstein-Vazirani Networks: Quantum Machine Learning by Interference

**Authors:** Natacha Kuete Meli, Tolga Birdal, Prayag Tiwari, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19043v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19043v1)

**Summary:** We introduce Bernstein-Vazirani Networks (BVNs), a non-variational quantum machine learning framework that leverages quantum interference for supervised learning, demonstrated on vision and representation learning tasks. In their standard form, BVNs follow the principle of quantum Fourier sampling: labelled data are placed in superposition and interfered in the Fourier basis to extract globally informative features. We then define generalised BVNs that enable interference in problem-adapted base...

---

### 22. Counterfactual Contrastive Analysis

**Authors:** Yunlong He, Pietro Gori

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19032v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19032v1)

**Summary:** Visual Counterfactual Explanations (VCEs) aim to explain image classifiers by generating minimally edited and realistic versions of an input image that change the classifier's prediction. Existing VCE methods are inherently classifier-dependent and therefore susceptible to classifier biases and failure modes, such as sensitivity to shortcut features and calibration errors. In this paper, we propose a classifier-free approach for visual counterfactual generation based on Contrastive Analysis (CA)...

---

### 23. Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering

**Authors:** Pradeep Murugesan, Luoxiao Yang, Xueli Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19029v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19029v1)

**Summary:** Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making. This work introduces an adaptive memory and reflection (AMR) agentic system, a multi-agent framework in which specialized agents use dedicated memory and reflection-based fe...

---

### 24. Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models

**Authors:** Valentin Romanov, Monique Bax, Steven Niederer

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19025v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19025v1)

**Summary:** Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) to extract highly contextualized information. We demonstrate four escalating workflows, 1) given an expert curated prompt and research articles, most frontier LLMs perform well at data extraction, however can struggle with interpreting scientific context and nuance, 2) given simple instructions, LLM...

---

### 25. One-Stage Object Detectors in Autonomous Driving

**Authors:** Jonel Roman, Ryan Sirjue, Peter Nguyen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19014v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19014v1)

**Summary:** Autonomous vehicles depend on fast and reliable perception systems to detect surrounding vehicles, pedestrians, cyclists, traffic signs, and other road objects in real time. This paper presents a comprehensive survey and analysis of one-stage object detectors for autonomous driving rather than an implementation of a new detection system. The survey reviews the evolution of major one-stage detectors, including YOLOv1, SSD, RetinaNet, EfficientDet, anchor-free detectors such as FCOS and CenterNet,...

---

### 26. Harness Continual Learning: Continual Adaptation Beyond Model Parameters

**Authors:** Borui Kang, Jinrui Gu, Junhan Lv, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19013v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19013v1)

**Summary:** Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience. Modern agents can also adapt through a harness of prompts, memories, tools, skills, and routing rules. Because these contents jointly shape later execution, a harness update can disrupt previously reliable behavior even when the model is frozen. This raises a new question: how can an agent continually improve its state outside the model while retaining behavior acqui...

---

### 27. From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation

**Authors:** Sepehr Ghaffarzadegan, Boubakr Nour, Makan Pourzandi, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19011v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19011v1)

**Summary:** Mechanisms for dynamically converting cyber threat intelligence (CTI) into actionable detection capabilities are necessary due to the rapid evolution of Advanced Persistent Threats (APTs). Sigma rules are an essential part of contemporary threat detection workflows because they offer a platform-independent framework for expressing detection logic that can be converted into particular queries across SIEM systems. Conventional techniques for manually crafting Sigma rules are prone to mistakes, and...

---

### 28. A Theory of Post-hoc Debate Judgement

**Authors:** Xiang Yin, Adam Dejl, Antonio Rago, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19002v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19002v1)

**Summary:** Debates have recently emerged as a useful methodology for agentic AI to improve performance as well as to aid explainability and user engagement. For example, LLM-empowered agents may debate internally (with themselves) and/or externally (with other agents). In many settings where debates are used, debates' outcomes and resulting outputs are determined post-hoc by external judges, often LLMs. In this paper we develop and test a novel theory of debate judgement applicable to all settings where ag...

---

### 29. GrabVG: Graph-Attentive Binding for Visual Grounding in UAV Imagery

**Authors:** Chaowei Wang, Yan Di, Jingjun Sun, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18996v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18996v1)

**Summary:** Visual grounding in Unmanned Aerial Vehicle (UAV) imagery aims to localize a target object in complex bird's-eye-view scenes according to a natural language description. However, the abundance of small, densely distributed, and visually similar objects creates high visual redundancy, while repetitive local configurations give rise to strong topological ambiguity. Existing approaches mainly focus on visual--language feature alignment or dense contextual interaction, yet they struggle to distingui...

---

### 30. DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering

**Authors:** Xujia Wang, Yizhe Zhang, Bin Xu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18988v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18988v1)

**Summary:** Retrieve-then-generate pipelines are commonly used to produce deep-research answers for open-ended questions, but retrieval alone is insufficient: LLMs must organize noisy and fragmented evidence into comprehensive, well-cited answers. We refer to this process as evidence synthesis. However, direct generation often underuses evidence, misaligns citations, and collapses diverse information into shallow summaries, exposing an evidence synthesis gap between retrieval and generation. Thus, we propos...

---

### 31. rEDMRec: Distilling Large Language Model Reasoning into an Editable Experience Memory for Recommendation

**Authors:** Minh Hoang Nguyen, Tung Le, Huy Tien Nguyen

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18952v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18952v1)

**Summary:** Large language models can improve recommendation quality by reasoning explicitly over user history and candidate items - for example, extracting a user's preferences or explaining why one item fits better than another - rather than mapping history directly to a ranked list. This reasoning, however, is expensive to repeat on every ranking request and, once produced, is typically consumed once and discarded, leaving it neither reusable across future requests nor easy to inspect or correct as user ...

---

### 32. AlphaClifford: Efficient Clifford Synthesis and Transpilation with Model-based RL

**Authors:** Daniele Lizzio Bosco, Jacopo Cossio, Carla Piazza, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18946v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18946v1)

**Summary:** Clifford circuits play a foundational role in quantum computing, particularly due to their importance in quantum error correction and fault-tolerant logical synthesis. While these circuits can be efficiently simulated and represented as symplectic matrices, standard synthesis methods-such as the Aaronson-Gottesman algorithm-often yield sub-optimal circuits with excessively high gate counts. In this work, we introduce AlphaClifford, a model-based Reinforcement Learning framework powered by Monte ...

---

### 33. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis

**Authors:** Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18940v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18940v1)

**Summary:** Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions. We compile CREED-CCV-2+USPTO-XL, an ultra-large-scale dataset of ~45.6 million verified reactions to train the C3LM (Chemistry Constraint-Consisten...

---

### 34. Breaking the weakest link to evade vision language models

**Authors:** Ilan Zini, Boussad Addad, Katarzyna Kapusta

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18938v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18938v1)

**Summary:** Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment. In this work, we investigate the vulnerability of VLMs to adversarial perturbations applied to vi...

---

### 35. MedUAG: Unified Understanding and Generation for Medical Multimodal Models

**Authors:** Zijie Meng, Yuncheng Zhang, Hualiang Wang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18937v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18937v1)

**Summary:** Recent Multimodal Large Language Models (MLLMs) are rapidly evolving into unified understanding and generation (UAG) frameworks. However, extending these unified paradigms to the medical domain is hindered by: the absence of comprehensive training and evaluation benchmarks, and the lack of broadly validated unified medical model. To address these gaps, we present a comprehensive foundation for medical UAG. First, we construct MedUAGCorpus, the largest unified medical understanding and generation...

---

### 36. Graphical Design of Interpretable Architectures

**Authors:** Pietro Barbiero

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18936v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18936v1)

**Summary:** Designing, implementing, and comparing interpretable architectures requires a formal language to represent them. The most common representations fall short in one of two ways. Symbolic equations give no global view of an architecture at a glance. Probabilistic graphical models and flowcharts do not describe actual tensor manipulations, thus hiding key insights and limiting reproducibility. To close this gap, we introduce a graphical notation for designing interpretable AI architectures, adapted ...

---

### 37. SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution

**Authors:** Silin Chen, Han Li, Xiaodong Gu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18933v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18933v1)

**Summary:** Large language model (LLM) based agents have demonstrated remarkable proficiency in automated software issue resolution, yet they often struggle to resolve issues in a specific repository because they lack project-specific knowledge. Existing self-evolving approaches acquire such knowledge from repository history or online repair trajectories, but they either depend on available historical issue-resolution signals or incur substantial per-issue test-time exploration cost. In this paper, we propo...

---

### 38. Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

**Authors:** Davide Romano, Kanak Raj, Jerrod Parker, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18931v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18931v1)

**Summary:** Test-time scaling (TTS) improves language model outputs by spending additional inference compute - generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine...

---

### 39. SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance

**Authors:** Jian Yang, Zhenqi Feng, Zhaoyang Yu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18921v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18921v1)

**Summary:** Existing LRM-DoS methods rely heavily on model feedback to synthesize attack queries, requiring either repeated queries to the target model or training a dedicated attack model. These expensive operations severely weaken attack leverage. In this paper, we propose \emph{search amplification}, a novel, model-feedback-free LRM-DoS paradigm. It employs the conflict count derived from an Satisfiability Modulo Theories (SMT) solver as a low-cost external signal to guide the synthesis of inference-heav...

---

### 40. Learning-State-Aware Dynamic Generative Data Augmentation on Small-Scale Datasets

**Authors:** Ting Xiang, Chenxi Deng, Jinhui Zhao, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18907v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18907v1)

**Summary:** Small-scale image classification is often limited by the scarcity of training data. Generative data augmentation (GDA) based on pretrained generative models has emerged as an effective solution. However, existing methods rely on task-agnostic augmentation strategies that overlook downstream model needs. Although recent dynamic GDA methods incorporate model feedback to guide augmentation, they still struggle to reliably determine sample-specific augmentation strengths and adapt augmentation strat...

---

### 41. \textsc{TestifAI}: Tomography-Based Testing for Deep Learning Systems

**Authors:** Arooj Arif, Tobias Hartung, Elena Botoeva, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18900v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18900v1)

**Summary:** As AI systems are increasingly deployed in safety-critical application domains (e.g., autonomous driving), associated risks increase too. Deep learning models underlying modern AI systems, therefore, must undergo thorough testing to ensure their correct behaviour. A single robustness test involves thousands of inferences to empirically verify if a model's outputs remain stable under a bounded perturbation of its inputs. However, existing testing frameworks lack the means to systematically explor...

---

### 42. Syntactic Simplification of OWL Class Expressions

**Authors:** Alkid Baci, N'Dah Jean Kouagou, Caglar Demir, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18899v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18899v1)

**Summary:** Class expression learning often produces complex OWL class expressions that are difficult to interpret and reason over. However, by following theoretically grounded simplification principles, this complexity can be reduced. In this paper, we propose Class Expression Simplifier (CES), a novel algorithm for the syntactic simplification of class expressions in Description Logics (DL). CES aims to preserve formal semantics while reducing representational complexity. It systematically applies rewriti...

---

### 43. Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models

**Authors:** Wei Yu, Suxing Liu, Minjie Yu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18884v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18884v1)

**Summary:** Reinforcement-learning training of reasoning LLMs (e.g., GRPO) is expensive and requires a controllable environment, committing every contribution to a full training pipeline. We present EvoResearcher, a training-free, inference-time protocol that adds cost-bounded self-reflection to a single frozen LLM backbone. The protocol iterates generate -> self-critique -> revise until a maximum depth D is reached or the critique returns the CONFIRMED sentinel, an implicit early stop that lets the backbon...

---

### 44. DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning

**Authors:** Zijie Meng, Xiwei Dai, Yixuan Tang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18878v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18878v1)

**Summary:** Oral diseases affect billions of people worldwide, underscoring a pressing need for accurate and reliable dental assessment that integrates heterogeneous evidence from domain knowledge, radiographs, intraoral photographs, and 3D dental data. Most existing dental AI systems remain modality- or task-specific. Although recent vision-language models support flexible dental question answering, directly generated response leaves evidence implicit and untraceable. To address these limitations, we intro...

---

### 45. SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents

**Authors:** Qingyao Li, Wenxiang Jiao, Shuai Shao, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18852v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18852v1)

**Summary:** Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-leve...

---

### 46. ORBITER: Conflict-Aware Decision-Making for Agentic Last-Mile Delivery

**Authors:** Mingzhao Li, Chenxi Liu, Yan Zhao, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18846v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18846v1)

**Summary:** Last-mile delivery aims to handle dynamically arriving orders with couriers while modeling complex spatial and temporal correlations. Recent learning-based methods model spatiotemporal dependencies among orders to predict courier service sequences, but leave next-order decision making unexplained. Describing the current delivery state in language allows LLMs to reason explicitly about the spatial, temporal, and behavioral cues behind an individual decision. As direct predictors, however, LLMs re...

---

### 47. Verifiable abstention makes AI leak diagnosis accountable in water distribution networks

**Authors:** Tianwei Mu, Yue Wang, Mingzhe Yuan, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18836v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18836v1)

**Summary:** Utilities lose a substantial share of treated water to leakage, yet rarely trust artificial-intelligence localizers to dispatch crews: guessing everywhere cannot justify excavation. The gap is accountability, not accuracy: no method proves when it should not act. Here we recast leak localization as decision-making under verifiable abstention. A physics-grounded executor agent falsifies hypotheses (leak, demand, sensor, valve) against a digital twin; an independent supervisor agent, with a large-...

---

### 48. MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models

**Authors:** Chenglin Liu, Xun Wang, Ruishuo Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18827v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18827v1)

**Summary:** Reward function design remains a bottleneck in reinforcement learning. While large language models (LLMs) have enabled automated reward generation, existing methods generate and revise reward functions as monolithic programs, making it difficult to reliably preserve and reuse effective components discovered in earlier iterations, leading to unstable performance across iterations. To address this, we propose Module Level Reward Evolution Framework (MLREF). At the core of MLREF is a module pool, a...

---

### 49. Understanding Multilingual Medical ASR Adaptation Through Layer-Wise Analysis

**Authors:** Souranil Kahali, Rituparna Bose, Abner Hernandez, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18825v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18825v1)

**Summary:** Medical automatic speech recognition (MedASR) requires adaptation to specialised terminology, limited annotated clinical data, and multilingual use cases. Although large-scale pretrained ASR models such as Whisper achieve strong generalisation, their behaviour after medical and multilingual adaptation remains insufficiently understood beyond word error rate (WER). This paper investigates how multilingual medical adaptation reshapes the internal representations of Whisper models through layer-wis...

---

### 50. Identifying Implicit Premises for Logical Reconstruction of Argument Graphs

**Authors:** Xuyao Feng, Anthony Hunter

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18821v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18821v1)

**Summary:** The logical reconstruction of argument graphs from natural language text is challenging because of the prevalence of enthymemes (i.e., arguments with implicit premises). There are natural language processing methods for identifying enthymemes in text, and there are symbolic methods based on abduction for identifying missing premises in a logical representation of enthymemes. However, there is a need for methods to generate implicit premises to logically show a known entailment or contradiction r...

---

## cs.CL

**50 papers**

### 1. SPADE: Self-Play in Adaptive Synthetic Executable Environments

**Authors:** Bo Liu, Simon Yu, Yiding Jiang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19197v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19197v1)

**Summary:** Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environment pools (hand-curated, statically synthesized, or frozen-verifier) keep the goal distribution fixed as the learner scales. We introduce SPADE (Self-Play in Adaptive Synthetic Executable Environments), a self-play RL framework in which a single LLM plays two roles: an Environment Designer that writes complete, long-horizon training environments a...

---

### 2. Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning

**Authors:** Zhu Zhang, Jixun Wang, Xiaoang Xu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19181v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19181v1)

**Summary:** On-policy distillation (OPD) trains a student on its own responses using dense token-level guidance from a stronger teacher. In long-context tasks, however, token-level teacher support can favor locally plausible responses that omit evidence distributed across the input or violate global task constraints. Task-specific verifiers, in contrast, evaluate task completion at the response level and may return graded rewards that reflect partial success. We diagnose this mismatch on fixed responses fro...

---

### 3. ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos

**Authors:** Thales Bertaglia, Catalina Goanta, Gerasimos Spanakis, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19165v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19165v1)

**Summary:** ChildSafeAds is a shared task on commercial content in YouTube videos likely to reach children and teenagers. It contains 3,360 videos from 939 channels. Each instance begins with a segment submitted to SponsorBlock, an open-source crowdsourced browser extension whose users mark sponsor segments so that others can skip them. We pair the segment with its available transcript, video and channel information, and a sales or service page linked from the video description. Systems determine what kind ...

---

### 4. Comment-level Topic Drift Analysis in the Reddit Corpus

**Authors:** Steven Morse, Daniel Runfola, Trenton W. Ford

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19133v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19133v1)

**Summary:** We present a novel application of embedding-based dynamic topic modeling techniques to detect and quantify topic drift at the comment level in a massive corpus. By leveraging pretrained language models to generate contextualized semantic embeddings for short text, we analyzed 12.7 billion Reddit comments spanning 2006 to 2022. Using unsupervised methods on these embeddings, we identify dynamically evolving topic clusters over time. Our primary contribution is a methodology for analysis of semant...

---

### 5. Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation

**Authors:** Huan-ang Gao, Haohan Chi, Yong Yan, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19098v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19098v1)

**Summary:** Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) experts into a single generalist student via dense, token-level reward supervision. Despite its practical success, the optimization dynamics governing multi-teacher capability integration remain poorly understood, and open, rigorously reproducible recipes are conspicuously lacking. In this work, we establish a controlled M-OPD benchmark on SmolLM3-3B-B...

---

### 6. When Readability and Source Retention Diverge: An Evaluability Gap in AI Translation

**Authors:** Chenchen Mao, Hanjing Shi, Haiyan Jia, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19083v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19083v1)

**Summary:** Readable AI output can leave an evaluability gap: even when the source is shown, an overall-quality judgment may not reflect what an output preserves. We investigated how source-text condition and output rendering relate to perceived translation quality, and how output and system appraisals relate to trust and stated disclosure willingness in a plain-text interface. A focal 2 * 2 comparison (N=306) using TransLingo examined simple generated narratives and complex literary-philosophical prose alo...

---

### 7. ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate Hallucinations in Large Vision-Language Models

**Authors:** Jihae Jeong, Junha Choi, Hwanjo Yu

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19075v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19075v1)

**Summary:** Large vision-language models (LVLMs) often hallucinate, generating content that the input image does not support. Preventing such content during decoding calls for a candidate-specific measure of how strongly the image supports the token under consideration. The model's visual-token states offer a natural source of this evidence because projecting each state through the output head reveals which vocabulary items that position favors. These position-wise readouts cannot be pooled directly because...

---

### 8. What is Missing from AI Post-Training AI: An Empirical Analysis

**Authors:** Joy Jia Yin Lim, Xin Huang, Hao Peng, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19072v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19072v1)

**Summary:** Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-AI. We argue that this picture conflates two distinct capabilities: execution-level capability, iterating within a selected training strategy; and strategy-level capability, revising the high-level judgment as experimental evidence accumulates. Analyzing a large corpus of publicly released post-train...

---

### 9. Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering

**Authors:** Pradeep Murugesan, Luoxiao Yang, Xueli Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19029v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19029v1)

**Summary:** Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making. This work introduces an adaptive memory and reflection (AMR) agentic system, a multi-agent framework in which specialized agents use dedicated memory and reflection-based fe...

---

### 10. Institutional Books - Enriched Text: A customizable multilingual open-source pipeline for denoising, deduplicating, and annotating OCR text at scale

**Authors:** David Lowry-Duda, Matteo Cargnelutti, Catherine Brobston, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19026v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19026v1)

**Summary:** Released in 2025, Institutional Books: Harvard Library (IB-HL) is a collection of 983,004 volumes (242B o200k_base tokens), originally digitized through Harvard Library's participation in the Google Books Library project. As researchers and developers have begun to use IB-HL, a tension has emerged between standard large-scale preprocessing practices and the goals of careful information stewardship. Many existing pipelines optimize for web text: as a result, they tend to aggressively filter, dedu...

---

### 11. Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning

**Authors:** Yajie Yin

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19009v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19009v1)

**Summary:** Large language models (LLMs) are increasingly paired with verifiers (step checkers, self-consistency filters, tool-based fact checkers, formal proof assistants) that claim to detect the model's errors. Yet the verification literature uses the word "level" to mean at least five different things: verification granularity, concept abstraction, risk tier, system-stack layer, and the epistemic source of the ground truth. We propose Verification Autonomy Levels (VAL), a meta-standard classifying verif...

---

### 12. Introducing the Privacy-HSD Trade-off: Hate Speech Detection, but not at the Cost of Privacy

**Authors:** Stephen Meisenbacher, Vlad Garbuz, Chirill Donos, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19006v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19006v1)

**Summary:** Hate speech is a real and timely threat that affects a large portion of online users, especially youth and minority groups. While building reliable and robust automatic hate speech detection (HSD) systems is paramount, we argue that this must also be balanced with the individual right to privacy. Exploring the intersection of HSD and privacy, we demonstrate that HSD systems might unintentionally achieve performance at the cost of encoding authorship, posing a threat to privacy. Building on these...

---

### 13. Structure, Association, and Decision Value: Representation-Based Difficulty Estimation for Adaptive Inference in African-Language NLI

**Authors:** Toheeb Ogunade

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19003v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19003v1)

**Summary:** We ask whether internal representation statistics can provide useful example-level difficulty signals for adaptive inference in multilingual African NLP, and find that they cannot in this setting. Studying natural language inference across 15 African languages with frozen off-the-shelf checkpoints, we report four results. First, AfriXNLI's English configuration shares 1,047 of its 1,050 examples verbatim with XNLI evaluation data, and one widely used NLI checkpoint scores 1.000 on that test spli...

---

### 14. DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering

**Authors:** Xujia Wang, Yizhe Zhang, Bin Xu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18988v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18988v1)

**Summary:** Retrieve-then-generate pipelines are commonly used to produce deep-research answers for open-ended questions, but retrieval alone is insufficient: LLMs must organize noisy and fragmented evidence into comprehensive, well-cited answers. We refer to this process as evidence synthesis. However, direct generation often underuses evidence, misaligns citations, and collapses diverse information into shallow summaries, exposing an evidence synthesis gap between retrieval and generation. Thus, we propos...

---

### 15. Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers

**Authors:** Matteo Cargnelutti, Catherine Brobston, Eben English, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18972v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18972v1)

**Summary:** Historical newspapers are an abundant record of public life, but their dense, irregular and sometimes noisy layouts make computational access to these materials both challenging and limited. We present the Institutional Newspapers Pipeline, a modular system we jointly designed with Boston Public Library to extract high-quality, structured datasets from historical newspaper scans. It was architected so that each step remains interpretable and customizable, and so that the pipeline as a whole rema...

---

### 16. rEDMRec: Distilling Large Language Model Reasoning into an Editable Experience Memory for Recommendation

**Authors:** Minh Hoang Nguyen, Tung Le, Huy Tien Nguyen

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18952v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18952v1)

**Summary:** Large language models can improve recommendation quality by reasoning explicitly over user history and candidate items - for example, extracting a user's preferences or explaining why one item fits better than another - rather than mapping history directly to a ranked list. This reasoning, however, is expensive to repeat on every ranking request and, once produced, is typically consumed once and discarded, leaving it neither reusable across future requests nor easy to inspect or correct as user ...

---

### 17. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis

**Authors:** Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18940v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18940v1)

**Summary:** Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions. We compile CREED-CCV-2+USPTO-XL, an ultra-large-scale dataset of ~45.6 million verified reactions to train the C3LM (Chemistry Constraint-Consisten...

---

### 18. MedUAG: Unified Understanding and Generation for Medical Multimodal Models

**Authors:** Zijie Meng, Yuncheng Zhang, Hualiang Wang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18937v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18937v1)

**Summary:** Recent Multimodal Large Language Models (MLLMs) are rapidly evolving into unified understanding and generation (UAG) frameworks. However, extending these unified paradigms to the medical domain is hindered by: the absence of comprehensive training and evaluation benchmarks, and the lack of broadly validated unified medical model. To address these gaps, we present a comprehensive foundation for medical UAG. First, we construct MedUAGCorpus, the largest unified medical understanding and generation...

---

### 19. Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

**Authors:** Davide Romano, Kanak Raj, Jerrod Parker, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18931v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18931v1)

**Summary:** Test-time scaling (TTS) improves language model outputs by spending additional inference compute - generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine...

---

### 20. SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance

**Authors:** Jian Yang, Zhenqi Feng, Zhaoyang Yu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18921v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18921v1)

**Summary:** Existing LRM-DoS methods rely heavily on model feedback to synthesize attack queries, requiring either repeated queries to the target model or training a dedicated attack model. These expensive operations severely weaken attack leverage. In this paper, we propose \emph{search amplification}, a novel, model-feedback-free LRM-DoS paradigm. It employs the conflict count derived from an Satisfiability Modulo Theories (SMT) solver as a low-cost external signal to guide the synthesis of inference-heav...

---

### 21. Assessing Quality of Experience in Natural Language Generation of German Text

**Authors:** Dinh Nam Pham, Shushen Manakhimova, Vivien Macketanz, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18888v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18888v1)

**Summary:** The rapid advancement of Natural Language Generation (NLG) has made the reliable evaluation of generated text increasingly critical, as these systems, such as large language models (LLMs), are now widely deployed in real-world applications. However, traditional automatic metrics fail to capture the multifaceted nature of perceived quality. In this paper, we introduce TextQ-German, a novel dataset suite for human-centered evaluation of German NLG from a Quality of Experience (QoE) perspective, co...

---

### 22. MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models

**Authors:** Chenglin Liu, Xun Wang, Ruishuo Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18827v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18827v1)

**Summary:** Reward function design remains a bottleneck in reinforcement learning. While large language models (LLMs) have enabled automated reward generation, existing methods generate and revise reward functions as monolithic programs, making it difficult to reliably preserve and reuse effective components discovered in earlier iterations, leading to unstable performance across iterations. To address this, we propose Module Level Reward Evolution Framework (MLREF). At the core of MLREF is a module pool, a...

---

### 23. Understanding Multilingual Medical ASR Adaptation Through Layer-Wise Analysis

**Authors:** Souranil Kahali, Rituparna Bose, Abner Hernandez, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18825v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18825v1)

**Summary:** Medical automatic speech recognition (MedASR) requires adaptation to specialised terminology, limited annotated clinical data, and multilingual use cases. Although large-scale pretrained ASR models such as Whisper achieve strong generalisation, their behaviour after medical and multilingual adaptation remains insufficiently understood beyond word error rate (WER). This paper investigates how multilingual medical adaptation reshapes the internal representations of Whisper models through layer-wis...

---

### 24. Identifying Implicit Premises for Logical Reconstruction of Argument Graphs

**Authors:** Xuyao Feng, Anthony Hunter

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18821v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18821v1)

**Summary:** The logical reconstruction of argument graphs from natural language text is challenging because of the prevalence of enthymemes (i.e., arguments with implicit premises). There are natural language processing methods for identifying enthymemes in text, and there are symbolic methods based on abduction for identifying missing premises in a logical representation of enthymemes. However, there is a need for methods to generate implicit premises to logically show a known entailment or contradiction r...

---

### 25. Do Large Language Models Hallucinate Electric Fata Morganas?

**Authors:** Kristina Šekrst

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18816v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18816v1)

**Summary:** AI hallucinations - that is, outputs which are made up, cannot be verified, or contradict the source material - are generally regarded as an engineering flaw to be dealt with. This paper contends that they also have philosophical significance when it comes to the question of machine consciousness. We examine the known causes of hallucinations in large language models - such as source-target divergence, discrepancies between training and inference, and overfitting - and we present two empirical i...

---

### 26. Decomposing Wrong-Consensus Agreement in LLM Self-Consistency: A GPT-4.1 Case Study

**Authors:** Lizhuo Zhang, Mengmeng Tang, Chenfeng Long, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18795v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18795v1)

**Summary:** Majority voting over multiple LLM samples is widely used to raise answer accuracy, yet its gain varies erratically: on hard questions it can even backfire. This paper gives a quantitative account of this failure. A pluralistic agreement index Gamma is defined as the expected fraction of the samples of a wrong run that agree with the consensus, normalized by a reference scale d=(1-p)/(C-1), and is decomposed into a mechanical component (what a vote delivers given only a per-case answer preference...

---

### 27. Readable, Faithful, Used: Three Dissociable Properties of Demographic Identity in a Language Model

**Authors:** Fathin Difa Robbani

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18768v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18768v1)

**Summary:** Large language models are widely used to simulate survey respondents, yet their answers are homogeneous and unfaithful to real inter-group differences. We ask where demographic group identity lives inside an LLM, how faithfully its geometry mirrors real inter-group opinion structure, and whether it uses what it encodes. Using representational similarity analysis against Pew ground truth over 169 demographic cells, we score 1,089 read-out locations in Mistral-7B and intervene causally across six ...

---

### 28. Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning

**Authors:** Shiyu Miao, Yunlong Mao, Zirui Huang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18767v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18767v1)

**Summary:** Gradient matching attacks (GMAs) in LLM split learning (SL) rely on a critical yet underexplored assumption: the gradient exposed at the split interface is a faithful derivative of the client's full-label training objective. This gradient-objective consistency allows a curious server to recover private labels by searching for a sequence whose induced gradient explains the observation. We propose Gradient Mirage, a defense that breaks this consistency without discarding the optimization utility o...

---

### 29. Learning Canonical Register Automata over Ordered Data Domains

**Authors:** Yong Li, Qiyi Tang, Di-De Yen

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18765v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18765v1)

**Summary:** Register automata are finite automata equipped with memory that recognize data languages over infinite alphabets. In this work, we investigate active learning algorithms for deterministic register automata (DRAs) over ordered data domains--covering both dense domains, such as the rationals, and non-dense domains such as the integers. We show that the active learning problem for DRAs over both dense and non-dense ordered domains can be treated within a single unified framework. More specifically,...

---

### 30. GreekBarRetrieval: A Benchmark for Greek Statutory Retrieval

**Authors:** Ernest Beta, Odysseas S. Chlapanis, Dimitrios Galanis, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18752v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18752v1)

**Summary:** Statutory retrieval is necessary for citation-grounded legal question answering, but remains underexplored for Greek. We introduce GreekBarRetrieval, a public retrieval benchmark derived from, and complementing GreekBarBench, which did not include retrieval. The new benchmark comprises 283 bar-exam questions, each accompanied by the facts of the case it refers to, and 6,308 candidate statutory articles to retrieve from. Questions and facts are stated in everyday language, but need to be mapped t...

---

### 31. Metrics That Write Themselves: Evolving an Evaluator from Its Own Blind Spots

**Authors:** Xing Zhang, Yanwei Cui, Guanghui Wang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18744v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18744v1)

**Summary:** Agents improve quickly against a reliable automatic metric and stall without one, and the applications that need them most, report generation among them, are the ones nobody knows how to score. Can the metric write itself? Saying what makes an answer good is hard; pointing at something wrong with one is easier, so the metric we evolve is a pool of small Python operators that each flag a candidate for one named defect, or abstain, and vote. Asking a model for operators directly does not work: 183...

---

### 32. Execution-grounded evaluation reveals hidden failures in language-model calculations for environmental science

**Authors:** Maohao Ran, Chendong Ma, Yanting Zhang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18726v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18726v1)

**Summary:** Large language models are increasingly used for quantitative work in the environmental sciences, yet existing evaluations score only final answers, leaving calculation process unobserved. Here we introduce AtmosCoder-Bench, an execution-grounded benchmark that makes the calculation process visible. Built through a transferable semi-automated pipeline (436 problems, 3,910 variants, 7,029 graded quantities), every problem is validated to be unambiguous and human-solvable, with uniquely verifiable ...

---

### 33. Budget-First Tariff Recommendation (BFTR): A Complete Algorithmic Framework for Telecom Plan Recommendation without Overcharging

**Authors:** Ghislain Dorian Tchuente Mondjo

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18723v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18723v1)

**Summary:** Telecom operators traditionally offer predefined tariff grids, forcing users to choose from a limited set of plans. This paper proposes BFTR (Budget-First Tariff Recommendation), a complete algorithmic framework integrating eight Budget-First strategies, including two original hybrid approaches: Recursive Hybrid (conditional interpolation) and Knapsack-First Hybrid (priority knapsack). Unlike existing approaches that adjust prices upward to guarantee a minimum margin, BFTR guarantees the absence...

---

### 34. MemFuse: Multi-Source Memory Fusion from Fragmented Observations

**Authors:** Chao Li, Yuanfa Li, Wenhao Wu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18704v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18704v1)

**Summary:** Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on single-source textual histories. In realistic settings, however, relevant information is often fragmented across applications and devices, as well as across users and time, requiring agents to integrate dispersed observations into coherent episodic memories while preserving their source provenance. To address these gaps, we introduce **MemFuseBench...

---

### 35. Aslema at NADI 2026: Augmentation through Fewshot for SLU

**Authors:** Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18689v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18689v1)

**Summary:** We present Aslema, our system for NADI 2026 Shared Task 5, which consists of two subtasks: intent recognition and slot filling. We evaluate four omni LLMs in a zero-shot setting and compare them with fine-tuned models. Our results show that fine-tuning consistently outperforms zero-shot inference. We further explore synthetic data augmentation by using an LLM to generate culturally grounded Tunisian Derja utterances, followed by voice cloning to generate synthetic speech. Incorporating this synt...

---

### 36. Learning What to Fail On: Failure-Mode Contextual Bandits for Adversarial Data Curation

**Authors:** Roie Kazoom, Ofir Cohen, Rami Puzis, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18681v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18681v1)

**Summary:** We introduce a failure-aware adversarial retrieval-augmented framework for improving robustness in natural language understanding. Rather than selecting synthetic examples with a fixed reward threshold, our method formulates adversarial data curation as a failure-mode contextual bandit problem. Candidate examples are generated with retrieval-augmented prompting, filtered by the current target model, automatically validated by an LLM judge ensemble, and clustered into recurring failure modes. A s...

---

### 37. X2Streaming-TTS: Causal Token-Level Text-to-Speech from Streaming Text with Speech-State Inheritance

**Authors:** Rime Wen, Zehan Liu, Shawn Qin, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18661v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18661v1)

**Summary:** Streaming text-to-speech is essential for low-latency spoken dialogue systems, yet many systems wait for sentence-level text and are therefore only pseudo-streaming. True token-level synthesis must generate speech from uncertain prefixes while maintaining perceptual continuity over an unbounded stream with bounded context. We present X2Streaming-TTS, a causal TTS framework that consumes asynchronously arriving text tokens and emits speech without accessing future input. To handle uncertain prefi...

---

### 38. TranslatePsy-AfriSLM: High-Quality Data Scaling For Low-Resource Machine Translation

**Authors:** Milan Gritta, Patrik Lambert, Jihye Back, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18655v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18655v1)

**Summary:** The rapid progress in Artificial Intelligence has largely bypassed African languages, creating a digital divide that limits AI adoption on the continent. Recent open-source LLMs systematically underperform on African machine translation, while the lack of large-scale, high-quality, open-source parallel data has constrained the development of competitive small language models (SLMs). We introduce *TranslatePsy-AfriSLM*, a collection of open-source MT resources for 19 Sub-Saharan African languages...

---

### 39. When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models

**Authors:** Mehak Gupta, Tanmoy Chakraborty

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18628v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18628v1)

**Summary:** Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking phenomenon: under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. This raises a fundamental question: does safety alignment suppress perceptual grounding itself, or does visual evidence remain internally a...

---

### 40. Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference

**Authors:** Zishan Ahmad, Vishal Vaddina

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18591v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18591v1)

**Summary:** Uniformly allocating inference reasoning budgets to LLMs is expensive and prone to over-thinking penalties; especially in document tasks where visual layouts drive complexity. To address this, we introduce BudgetDoc, the first multimodal benchmark providing explicit supervision for model-budget-performance trade-offs across three document tasks. Using BudgetDoc, we train DRB (Document-Reasoning Balancer), an approx. 1B-parameter pre-flight estimator (SigLIP-2 + Qwen3-0.6B) that predicts ordinal ...

---

### 41. From Storage to Access: Verifiable Activation of Parametric Knowledge in LLMs via Explicit Priming and Implicit Reasoning

**Authors:** Zuocheng Ying, Yang Yang, Yumou Wu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18581v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18581v1)

**Summary:** Although Large Language Models (LLMs) encode rich factual knowledge in their parameters, reliably recalling and verifying such knowledge remains a key bottleneck in factual question answering. Existing end-to-end methods entangle knowledge elicitation with reasoning, making it difficult to determine whether correct answers arise from parametric knowledge or the input context. To address this challenge, we propose VAKE (Verifiable Activation of Parametric KnowledgE), a two-stage reinforcement-lea...

---

### 42. Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs

**Authors:** Shayan Shahrabi-Farahani, Dara Rahmati

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18578v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18578v1)

**Summary:** Proactive interference (PI) is a documented failure mode in large language models in which retrieval of a repeatedly overwritten value degrades as prior overwrites accumulate, mirroring a classical phenomenon in human working memory. Post-training quantization (PTQ) is now the default deployment path for open-weight models, yet its effect on this failure mode has not been tested. We evaluate three precision levels (FP16, INT8, INT4/NF4, via bitsandbytes) across three architecturally distinct ins...

---

### 43. Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution

**Authors:** Ting-Wei Li, Yuanchen Bei, Xiao Lin, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18575v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18575v1)

**Summary:** Large language model (LLM)-based multi-agent systems (MAS) often exhibit complex failure modes, which frequently cause agents to produce incorrect outcomes. This motivates the task of Agent Failure Attribution: given a failed multi-agent trajectory, identify the faulty agents and their corresponding error types. Existing approaches predominantly rely on LLMs to perform failure attribution, either through direct prompting, fine-tuning on synthetic data or complex agentic pipelines. While effectiv...

---

### 44. Shared Circuits for Shared Grammar: Tracing Subject-Verb Agreement Across Languages

**Authors:** Isabella Gidi, Antonio Almudévar, Core Francisco Park, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18545v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18545v1)

**Summary:** Multilingual large language models often generalize across languages, and prior work suggests that their internal mechanisms can overlap cross-lingually. It remains unclear, however, when such sharing emerges and whether it varies with the overt realization of the same grammatical operation. We investigate this question for present-tense subject-verb agreement, a morphosyntactic process that varies substantially across languages and is only weakly expressed in English. Using activation patching ...

---

### 45. Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions

**Authors:** Ruiyang Qin, Qingzhuo Wang, Tian Wang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18539v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18539v1)

**Summary:** The remarkable capabilities of large language models (LLMs) are often undermined by their instability. Even subtle and semantically irrelevant changes in prompts can cause dramatic fluctuations in performance, a phenomenon known as prompt sensitivity. Previous studies typically evaluate prompt sensitivity by comparing the LLM's final outputs when prompts change. However, such coarse-grained metrics fail to explain the internal reasons for prompt sensitivity. In this paper, we introduce interacti...

---

### 46. DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents

**Authors:** Hangrui Xu, Jiarui Wang, Yang Yang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18524v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18524v1)

**Summary:** Equipping Large Language Models (LLMs) with multi-turn tool-calling capabilities is essential for building autonomous agents. However, progress is fundamentally limited by the reliance on full-length trajectory imitation. For tasks involving multiple order-independent sub-goals, the optimal solution space forms a vast combinatorial diamond lattice. Forcing this rich topology into monolithic trajectories causes a severe topological collapse, indiscriminately penalizing valid alternative explorati...

---

### 47. MissDiag: Diagnostic Evaluation of Incomplete-Knowledge Robustness in KGQA and KG-RAG

**Authors:** Hang Wang, Hang Dong, Lu Liu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18489v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18489v1)

**Summary:** Knowledge graph question answering (KGQA) and knowledge-graph-based retrieval-augmented generation (KG-RAG) aim to ground answers in explicit graph evidence, but real-world knowledge graphs are often sparse, outdated, and incomplete. Existing robustness evaluations usually report aggregate changes in answer quality after evidence is removed or perturbed, which measures sensitivity to incomplete support but leaves the source of degradation under-specified: the same score change can conflate the t...

---

### 48. WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing

**Authors:** Wenbo Zhang, Xiang Ren

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18486v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18486v1)

**Summary:** In a Transformer, each layer attends to past tokens only through KV produced at its own depth, despite the presence of deeper representations during autoregressive decoding. Feedback architectures allow shallow consumer layers to attend to KV produced by deeper past-token representations, but give all consumer layers the same fixed connection patterns to source layers. We propose WhiteMatter, which connects every attention layer to the representations from all layers of each past token, with con...

---

### 49. Building real-time digital twin instances with Function+Data Flow: user evaluation and extension for iterative pipelines

**Authors:** Eduardo de Conto, Blaise Genest, Arvind Easwaran, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18480v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18480v1)

**Summary:** Digital twins (DTs) increasingly leverage artificial intelligence (AI) and machine learning (ML) pipelines, both to build real-time DTs from high-fidelity simulations and to instantiate them with historical data. However, engineering these pipelines remains largely ad-hoc: pipelines are hard to specify, validate, and reuse, with scarce dedicated tooling. Function+Data Flow (FDF) addresses this by defining a visual domain-specific language (DSL) that represents functions (ML models) explicitly, e...

---

### 50. OmniAlign: A Unified Multilingual Aligner for Word and Sentence Alignment

**Authors:** Mengpeng Yang, Jingxu Yang, Chao Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18474v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18474v1)

**Summary:** Cross-lingual sequence alignment is fundamental for building and exploiting parallel corpora, spanning mappings from documents and sentences down to words and subwords. Existing tools, however, typically specialize in a single granularity, so practitioners often need separate systems for word- and sentence-level alignment---especially in multilingual and long-text settings. We present OmniAlign, a unified multilingual aligner that supports both word-level and sentence-level alignment with a sing...

---

## cs.CV

**50 papers**

### 1. Image-Guided Pavement Defect Recognition in GPR Data with novel 3D Deep Learning Architecture

**Authors:** Yuandong Pan, Linjun Lu, Mudan Wang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19177v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19177v1)

**Summary:** Ground Penetrating Radar (GPR) is a widely adopted non-destructive sensing technology for subsurface inspection in civil and transportation engineering. Despite its potential for pavement condition assessment, the large-scale application of GPR in automated inspection has two key challenges: the scarcity of annotated real-world datasets and the lack of deep learning models designed for the unique characteristics of 3-Dimensional (3D) GPR data. This study addresses these limitations by firstly in...

---

### 2. Detecting Backdoors in Object Detection via Pre-NMS Prediction Distribution Shift

**Authors:** Longtian Wang, Zhengyu Zhao, Chenhao Lin, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19088v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19088v1)

**Summary:** Object detection models deployed in safety-critical applications remain vulnerable to backdoor attacks that cause targeted misbehaviors when a hidden trigger is present. Existing detection methods either rely on trigger inversion or exploit architecture-specific assumptions, and critically, representative existing methods fail to generalize reliably to scene-level attacks, where a single trigger induces anomalous behavior across all objects in the scene simultaneously. We present DistScan, a bac...

---

### 3. SPK: Eliciting Structured Prior Knowledge for Interpretable Out-of-Distribution Detection in Real-Time Object Detection

**Authors:** Changshun Wu, Weicheng He, Xiaowei Huang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19080v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19080v1)

**Summary:** Object detectors often produce over-confident predictions for objects outside their training categories, leading to so-called out-of-distribution (OoD) hallucinations. Existing approaches for detecting or mitigating such hallucinations typically either construct scoring functions directly over learned object detector representations or modify the object detector itself to suppress hallucination emergence. However, the latent priors implicitly encoded in these representations remain largely unexp...

---

### 4. Subgroup performance analysis of adaptation strategies for chest X-ray foundation models

**Authors:** Dhruv Gupta, Emma A. M. Stanley, Fabio De Sousa Ribeiro, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19078v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19078v1)

**Summary:** Foundation models are increasingly adapted for downstream medical imaging tasks, yet the influence of the chosen adaptation strategy on subgroup fairness remains poorly understood. We investigate how three parameter-efficient adaptation techniques, including linear heads on the raw CLS token, an MLP, and an attention-pooling module over multi-layer patch features, affect both pathology classification performance and subgroup disparities when applied to the frozen Rad-DINO chest X-ray encoder. Us...

---

### 5. ReWEIGH the Evidence: Calibrating Token-Level Ordinal Visual Evidence to Mitigate Hallucinations in Large Vision-Language Models

**Authors:** Jihae Jeong, Junha Choi, Hwanjo Yu

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19075v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19075v1)

**Summary:** Large vision-language models (LVLMs) often hallucinate, generating content that the input image does not support. Preventing such content during decoding calls for a candidate-specific measure of how strongly the image supports the token under consideration. The model's visual-token states offer a natural source of this evidence because projecting each state through the output head reveals which vocabulary items that position favors. These position-wise readouts cannot be pooled directly because...

---

### 6. GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting

**Authors:** Yechan Park, HyunJin Kim

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19066v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19066v1)

**Summary:** This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displaceme...

---

### 7. When Two Tracers Disagree: An Investigation of Multimodal Fusion for Clinical PET/CT Segmentation

**Authors:** Jack A. Johnson, Bartłomiej W. Papież

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19063v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19063v1)

**Summary:** PSMA and FDG PET/CT visualise complementary biological information in prostate cancer. Combining both tracers could capture heterogeneous tumour phenotypes that may be missed by either alone, yet there is no consensus on effective deep learning architectures for fusing these modalities. We evaluated multimodal image-fusion strategies for automatic whole-body PET/CT lesion segmentation to estimate total tumour burden. Using the public DEEP-PSMA Challenge dataset, we trained tracer-specific 3D nnU...

---

### 8. LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding

**Authors:** Yumin Lee, Hyoseok Ju, Giseop Kim

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19059v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19059v1)

**Summary:** Long-term robot operation in evolving environments requires object-level understanding that persists across repeated revisits. Existing systems either overwrite history to maintain an up-to-date map or store semantic snapshots without consistent cross-session object identity, resulting in temporal amnesia: the systematic loss of object history that prevents answering queries such as "Where has the green chair been across all sessions?" We propose LT-Mem, a volatility-aware memory evolution frame...

---

### 9. Generalized Audio-Driven Synthesis of Precise Drummer Motion

**Authors:** Álvaro G. Iñesta, Mattia Ryffel, Amit H. Bermano, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19055v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19055v1)

**Summary:** Music-driven character animation enables and enhances transformative applications in entertainment and interactive education. However, synthesizing realistic drumming motion from audio remains challenging due to the inherent tension between high-acceleration dynamics and the need for extreme spatial-temporal precision. Existing approaches, often reliant on motion matching or MIDI input, struggle with generalizing to diverse real-world audio. Moreover, the field lacks standardized evaluation metr...

---

### 10. Bernstein-Vazirani Networks: Quantum Machine Learning by Interference

**Authors:** Natacha Kuete Meli, Tolga Birdal, Prayag Tiwari, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19043v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19043v1)

**Summary:** We introduce Bernstein-Vazirani Networks (BVNs), a non-variational quantum machine learning framework that leverages quantum interference for supervised learning, demonstrated on vision and representation learning tasks. In their standard form, BVNs follow the principle of quantum Fourier sampling: labelled data are placed in superposition and interfered in the Fourier basis to extract globally informative features. We then define generalised BVNs that enable interference in problem-adapted base...

---

### 11. USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes

**Authors:** Li-Heng Chen, Haokai Pang, Chengye Su, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19036v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19036v1)

**Summary:** Spatial representation learning for autonomous driving aims to map raw visual signals into structured 3D scene representations, where object-centric bounding boxes and rendering-oriented 3D primitives (\eg, 3D Gaussians) serve as two distinct yet highly complementary levels for scene understanding. Existing methods typically treat dynamic reconstruction and instance-level perception as separate tasks, despite their shared goal of estimating the underlying 3D world state. As a result, dynamic rec...

---

### 12. Counterfactual Contrastive Analysis

**Authors:** Yunlong He, Pietro Gori

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19032v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19032v1)

**Summary:** Visual Counterfactual Explanations (VCEs) aim to explain image classifiers by generating minimally edited and realistic versions of an input image that change the classifier's prediction. Existing VCE methods are inherently classifier-dependent and therefore susceptible to classifier biases and failure modes, such as sensitivity to shortcut features and calibration errors. In this paper, we propose a classifier-free approach for visual counterfactual generation based on Contrastive Analysis (CA)...

---

### 13. Orthogonal Polynomial Approximation for Matrix Log Normalization in Global Covariance Pooling

**Authors:** Md Rifat Ur Rahman, Md Raihan Khan, Md Sakib Hossain Shovon, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19021v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19021v1)

**Summary:** Global Covariance Pooling (GCP) improves deep networks by capturing second-order feature statistics, and is especially effective for fine-grained recognition. Because covariance matrices live on the Symmetric Positive Definite (SPD) manifold, a normalization step is required before the Euclidean classifier. The faithful choice is the matrix logarithm (MLN-COV), which maps the SPD manifold to its tangent space; in practice it was abandoned in favour of the matrix square root because its eigendeco...

---

### 14. One-Stage Object Detectors in Autonomous Driving

**Authors:** Jonel Roman, Ryan Sirjue, Peter Nguyen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19014v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19014v1)

**Summary:** Autonomous vehicles depend on fast and reliable perception systems to detect surrounding vehicles, pedestrians, cyclists, traffic signs, and other road objects in real time. This paper presents a comprehensive survey and analysis of one-stage object detectors for autonomous driving rather than an implementation of a new detection system. The survey reviews the evolution of major one-stage detectors, including YOLOv1, SSD, RetinaNet, EfficientDet, anchor-free detectors such as FCOS and CenterNet,...

---

### 15. Autonomous Agricultural Tractor: Integrated Weed Detection and LiDAR Navigation for Precision Paddy Farming

**Authors:** Benjamin Merryman-Smith, Tony Nguyen, Bilal Dogutas, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19004v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19004v1)

**Summary:** Site-specific weed management in paddy farming offers substantial reductions in herbicide use over conventional broadcast spraying, but field deployment has been limited by three persistent challenges: robust crop-row navigation under canopy where GNSS degrades, real-time visual discrimination between rice and morphologically diverse weeds, and the asymmetric cost of misclassifying rice as weed, which is irreversible.   This paper presents AgriNav, an integrated autonomous tractor system built a...

---

### 16. Mise-en-Scène: Implicit Layout Emergence in Diffusion Transformers for Human-AI Design Co-Creation

**Authors:** Zipeng Xu, Ryan Murdock, Umberto Michieli

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19000v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19000v1)

**Summary:** Automating graphic design synthesis from user-provided elements requires both a coherent overall composition and the exact preservation of each asset. Existing methods predict a layout as explicit bounding-box coordinates with a language model and then paste the assets into it, which separates spatial planning from visual synthesis and tends to produce rigid, mis-scaled compositions. We instead ask whether the layout can emerge implicitly inside a pretrained image-editing diffusion transformer. ...

---

### 17. GrabVG: Graph-Attentive Binding for Visual Grounding in UAV Imagery

**Authors:** Chaowei Wang, Yan Di, Jingjun Sun, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18996v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18996v1)

**Summary:** Visual grounding in Unmanned Aerial Vehicle (UAV) imagery aims to localize a target object in complex bird's-eye-view scenes according to a natural language description. However, the abundance of small, densely distributed, and visually similar objects creates high visual redundancy, while repetitive local configurations give rise to strong topological ambiguity. Existing approaches mainly focus on visual--language feature alignment or dense contextual interaction, yet they struggle to distingui...

---

### 18. ForeSightGuide: An Anticipatory Framework toward Accurate and Low-Redundancy Guidance for the Visually Impaired

**Authors:** Zhiyuan Wang, Xu Li, Shikang Guo, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18993v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18993v1)

**Summary:** Electronic travel aids are pivotal for the independent mobility of the visually impaired. While Vision-Language Models (VLMs) offer rich environmental understanding, they often suffer from excessive false positives in dynamic scenarios, leading to cognitive overload. To address this, we present ForeSightGuide, an anticipatory assistive guidance framework that couples semantic scene understanding with predictive hazard assessment. Unlike reactive systems, ForeSightGuide leverages the reasoning ca...

---

### 19. X-LMC: Cross-View Spatiotemporal Collateral Circulation Scoring from DSA

**Authors:** Maedeh Hafezi Moghadas, Hakim Baazaoui, Lukas Bastian Otto, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18986v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18986v1)

**Summary:** Digital subtraction angiography (DSA) is the reference standard for leptomeningeal collateral (LMC) assessment, providing critical prognostic insights to guide secondary treatment strategies, neurorehabilitation planning, and retrospective stroke research. However, clinical LMC grading via the ASITN/SIR scale relies on manual, highly variable visual inspection. We introduce X-LMC, a spatiotemporal framework for automated collateral scoring from time-resolved biplane DSA. The proposed architectur...

---

### 20. Uncertainty-Aware Art-Historical Dating with Vision-Language Models

**Authors:** Stefanie Schneider, Peter Bell

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18984v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18984v1)

**Summary:** Museum and archival datasets do not mirror historical artistic production, but materialize the contingent histories of collecting, preservation, cataloging, and digitization. This has direct consequences for interpreting pretrained image representations: they may appear to encode historical time while actually encoding the institutional conditions under which objects become visible as data. We describe this phenomenon as temporal entanglement and investigate it by formulating artwork dating as a...

---

### 21. When Simplicity Wins: Bottleneck-Aware Context Modeling for Lightweight Semantic Segmentation

**Authors:** Mian Muhammad Naeem Abid, Nancy Mehta, Zongwei Wu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18979v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18979v1)

**Summary:** Semantic segmentation demands a careful balance between accuracy, efficiency, and scalability, which remains difficult to achieve for high-resolution imagery. Convolutional networks effectively model local patterns but struggle with long-range dependencies, whereas Vision Transformers capture global context at a high computational cost. While recent work largely focuses on encoder design, the bottleneck stage, central to contextual aggregation and information flow, has been relatively overlooked...

---

### 22. Frozen DINO Localizes Image Edits Without a Localizer

**Authors:** Zane Kumar, Vishal Jain, Bernhard Kainz

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18968v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18968v1)

**Summary:** Localized image edits can change a photograph's meaning while leaving most of it authentic, so forensic analysis must identify where an edit occurred. We show that patch-level perturbation responses from frozen DINO encoders are themselves localization maps. Training-free Localization of AI-image Edits from patch-token Drift (TRAIL) applies one global Haar perturbation and maps cosine drift between corresponding patch tokens. On 80 source-disjoint CocoGlide test images, TRAIL reaches .903 patch ...

---

### 23. Institutional Books - Visual Elements: An open-source pipeline for extracting, classifying, deduplicating, and captioning visual elements from digital book collections

**Authors:** Jimmy Mendez, Matteo Cargnelutti, David Lowry-Duda, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18957v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18957v1)

**Summary:** Historical book collections contain rich visual elements - such as illustrations, photographs, engravings, and decorative art - that are frequently under-explored in large-scale digitization projects. While Optical Character Recognition (OCR) has standardized the extraction of textual content, these visual components offer a layer of nuance and context that remains largely untapped by automated text extraction workflows. This technical report introduces Institutional Books - Visual Elements, an ...

---

### 24. Simple, Safe, and Overlooked: Reclaiming Sustainable Domain Generalization with Statistical Color Matching

**Authors:** Sebastian Doerrich, Francesco Di Salvo, Shyam Nandan Rai, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18915v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18915v1)

**Summary:** Hardware shifts, color variations, and changing patient characteristics between development and deployment routinely break trained medical image classifiers. Existing remedies fall short: standard color jittering provides insufficient diversity, while deep generative style transfer algorithms hallucinate features, destroy clinically relevant structures, and waste massive compute resources. To address this, we revisit classical statistical color matching and repurpose it as Colorist, a highly eff...

---

### 25. Learning-State-Aware Dynamic Generative Data Augmentation on Small-Scale Datasets

**Authors:** Ting Xiang, Chenxi Deng, Jinhui Zhao, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18907v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18907v1)

**Summary:** Small-scale image classification is often limited by the scarcity of training data. Generative data augmentation (GDA) based on pretrained generative models has emerged as an effective solution. However, existing methods rely on task-agnostic augmentation strategies that overlook downstream model needs. Although recent dynamic GDA methods incorporate model feedback to guide augmentation, they still struggle to reliably determine sample-specific augmentation strengths and adapt augmentation strat...

---

### 26. Falcon Perception-HD: High Density Perception via Reinforcement Learning

**Authors:** Sofian Chaybouti, Yasser Dahou, Ngoc Dung Huynh, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18881v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18881v1)

**Summary:** Autoregressive perception models trained to localize visual entities under the open-vocabulary setting are mostly trained using Supervised fine-tuning (SFT) with maximum likelihood, yet it optimizes a proxy objective (per-token cross-entropy) that is fundamentally misaligned with perception metrics such as precision and recall. In this paper, we explore post-training reinforcement learning (RL), specifically GRPO, to directly align these models with their evaluation metrics. Building up on the r...

---

### 27. RVLoss: Runoff Vote Loss for Self-Supervised LiDAR Scene Flow Estimation

**Authors:** Shiming Wang, Liangliang Nan, Julian Kooij, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18864v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18864v1)

**Summary:** LiDAR scene flow estimates point-wise motion between two consecutive scans, referred to as the source and target. Leading self-supervised methods typically minimize the Chamfer loss, the nearest neighbor distance between the flow-compensated source and the target. However, nearest-neighbor search does not enforce motion rigidity, often leading to inconsistent flows within object instances. Existing approaches address this issue with additional regularization terms, but flow consistency among poi...

---

### 28. Beyond Placement and Articulation: Usage-Driven Code Scenes for Embodied Interaction

**Authors:** Zijian Xiao, Zipeng Ye, Jinkun Hao, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18840v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18840v1)

**Summary:** Indoor scene synthesis provides essential environments for embodied AI, robotic manipulation, and simulation-based policy learning. Recent code-based scene generation methods produce editable and extensible environments, yet they remain focused on visual construction and object-level articulation, leaving the functional usage of scenes largely unmodeled. To address this problem, we present RoomWright, an agentic usage-driven framework for generating 3D scenes represented entirely as code for emb...

---

### 29. EVADE: Evidence-Verified Agentic Diagnosis with Escape

**Authors:** Mohaimenul Azam Khan Raiaan, Nur Mohammad Fahad

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18833v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18833v1)

**Summary:** Medical vision-language models (VLMs) can achieve high accuracy but remain unreliable: they are systematically overconfident, benefit little from test-time reasoning, and lack the ability to reliably calibrate trust in their own responses. We introduce EVADE (Evidence-Verified Agentic Diagnosis with Escape), an inferential, non-training method that enhances the safety of deploying a single frozen VLM. EVADE responds and, when uncertain, localises the region most diagnostically relevant, re-answe...

---

### 30. EfficientSync: Real-Time Lip Synchronization via Deformation-Based Reference Texture Mixing

**Authors:** Fa-Ting Hong, Runzhen Liu, Luchuan Song, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18832v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18832v1)

**Summary:** Audio-driven lip synchronization manipulates the mouth region of a talking-face video to match the driving audio while preserving head pose, identity, and background. Although the task is inherently local editing, prevailing approaches reconstruct the entire lower face with heavy GAN- or diffusion-based decoders, incurring substantial latency and, more critically, hallucinating intra-oral details such as teeth and lip wrinkles instead of preserving authentic textures. We contend that the bottlen...

---

### 31. MIFR: A Modality-Invariant and Fair Representation Framework for Skin Disease Classification

**Authors:** Asonyu Senge Njih, Yvan Guifo Fodjo, Vianney Kengne Tchendji, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18774v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18774v1)

**Summary:** Skin diseases represent a major global public health burden, yet machine learning tools developed to assist in their diagnosis suffer from two critical limitations: reliance on only one modality for diagnosis and systematic performance disparities across skin tones. While existing approaches address each challenge separately, this work proposes a modality-invariant framework with fair representation (MIFR) for skin disease classification. The architecture pairs clinical photographs with dermosco...

---

### 32. SED-FOD: Scattering-Aware Expert Decomposition for Few-Shot Cross-Sensor SAR Object Detection

**Authors:** Shu Yang, Zhen Chen, Zhiyu Jiang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18755v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18755v1)

**Summary:** Synthetic aperture radar (SAR) object detection is an important part of remote sensing interpretation. However, because of variations in frequency band, resolution, background clutter, and target scattering responses, the performance of existing detectors often degrades when training and testing data are acquired from different SAR domains. Although domain adaptation methods offer a promising paradigm for solving this problem, most of them mainly pursue domain-invariant feature alignment and sup...

---

### 33. Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning

**Authors:** Jiawei Wang, Ke Rui, Yushen Zuo, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18746v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18746v1)

**Summary:** JEPA-style latent world models can use Euclidean distance to a goal latent as the cost for model-predictive control (MPC). Strong decoding of task variables, however, does not guarantee that this particular cost ranks candidate action sequences by real task progress. We call the latter property \emph{decision-metric alignment}. We introduce Plan-Real Spearman, which measures latent--real rank agreement on random plans, and CEM-stage Spearman, which measures the same agreement as cross-entropy-me...

---

### 34. CL4D: Contrastive Language-4D Pretraining for Vision-Language Reasoning in Dynamic Scenes

**Authors:** Kumal Hewagamage, Isuranga Senavirathne, Sasika Amarasinghe, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18734v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18734v1)

**Summary:** 4D understanding and reasoning is a fundamental capability for embodied AI agents operating in dynamic physical environments. However, existing vision encoders are largely limited to static 2D images or 3D point clouds without temporal modeling, or to 2D videos that lack accurate geometric depth reasoning. Consequently, current approaches fail to jointly capture spatial structure and motion evolution in dynamic scenes. We present CL4D, the first foundational 4D vision encoder that directly opera...

---

### 35. A Few Cases Are All You Need: An Empirical Study of Annotation-Efficient LoRA Fine-Tuning of MedSAM3

**Authors:** Sachin Dudda Nagaraju, Bendik Skarre Abrahamsen, Ashkan Moradi, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18731v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18731v1)

**Summary:** Medical image segmentation is essential for clinical workflows such as treatment planning and disease assessment. While specialist tools like TotalSegmentator and MRSegmentator achieve strong performance, they require large annotated datasets for training. Medical foundation models offer a promising alternative through large-scale pretraining that reduces the annotation burden for new tasks, but zero-shot performance remains limited. Parameter-efficient adaptation via Low-Rank Adaptation (LoRA) ...

---

### 36. The Impact of CutMix on Reliability and Robustness in Semantic Segmentation

**Authors:** Steven Landgraf, Markus Ulrich

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18715v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18715v1)

**Summary:** Ensuring not only high accuracy but also reliable and robust predictions is critical for the deployment of semantic segmentation models in safety-critical applications such as autonomous driving. Despite the widespread use of CutMix - a simple yet powerful data augmentation strategy - its effect on the reliability and robustness in dense predictions tasks remains unexplored. Motivated by recent findings that semi-supervised segmentation methods, where CutMix is a core component, can severely deg...

---

### 37. EgoHRV: Continuous Heart Rate Variability Estimation from Egocentric Systems for Autonomic Response and Skill Assessment

**Authors:** Berken Utku Demirel, Christian Holz

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18711v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18711v1)

**Summary:** Egocentric vision systems capture human behavior from visible cues, but overlook physiological indicators of autonomic states such as stress, engagement, and attention. Heart rate variability (HRV) is a widely used noninvasive marker of autonomic regulation under stress. HRV reflects small timing differences between successive heartbeats and has so far been out of reach for egocentric platforms, where motion and noise in gaze video mask exactly this fine-grained timing. We propose EgoHRV, a meth...

---

### 38. CamWorldQA: Perceptual Quality Assessment of Camera-Controlled World Video Generation

**Authors:** Yunhe Li, Likun Wu, Sijing Wu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18710v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18710v1)

**Summary:** Recent advances in generative video models have enabled camera-controlled world video generation, allowing models to synthesize videos under user-defined camera trajectories. However, existing video quality assessment (VQA) methods are mainly developed for natural videos and fail to capture the unique perceptual characteristics of camera-controlled generation, such as viewpoint consistency, motion coherence, and content preservation. In this work, we introduce CamWorldQA, the first benchmark for...

---

### 39. A Critical Synthesis of Uncertainty Quantification and Foundation Models for Semantic Segmentation

**Authors:** Steven Landgraf, Joceline Hinz, Markus Ulrich

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18709v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18709v1)

**Summary:** Foundation models are increasingly breaking what seemed to be impossible not long ago by enabling unprecedented accuracy and cross-domain generalization. Yet their lack of interpretability, tendency to be overconfident, and sensitivity to real-world domain shifts pose critical challenges for safety- and mission-critical applications. Uncertainty quantification (UQ) offers a principled way to address these issues, but its integration into segmentation foundation models has yet to be explored. In ...

---

### 40. Impact of Iterative Fine-Tuning on Transcription Accuracy in Complex Historical Sanskrit Manuscripts

**Authors:** Kartik Chincholikar, Kaushik Gopalan, Mihir Hasabnis

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18696v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18696v1)

**Summary:** Digitizing the text from handwritten historical manuscripts is required to make them easily accessible, preservable, and to enable historical scholars to study them in new ways. Historical manuscripts, however, often exhibit complex heterogeneous layouts and non-standard appearance due to period-specific writing styles, page textures, camera noise, and other nuisance factors, making them difficult to perform OCR on. To tackle this challenge, we introduce a local traditional OCR pipeline, which c...

---

### 41. Composed Historical Image Retrieval by Modeling Temporal Representations

**Authors:** Adrià Molina Rodríguez, Oriol Ramos Terrades, Josep Lladós Canet

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18694v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18694v1)

**Summary:** While time evolves linearly, the geometry of neural embedding spaces is inherently multi-dimensional, often chaotic, and difficult to interpret. In principle, one could constrain an embedding space to a single temporal dimension; however, such a reduction would sacrifice performance on downstream tasks, as one-dimensional embeddings cannot retain sufficient expressive capacity. This paper asks whether it is possible to learn representations that preserve temporal structure while remaining effect...

---

### 42. DocClaw: A Unified Agentic System for Intelligent Document Processing

**Authors:** Siqi Xiang, Zhipeng Xu, Yufei Liu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18685v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18685v1)

**Summary:** Intelligent document processing (IDP) encompasses a broad range of tasks, including optical character recognition (OCR), document question answering (DocQA), and key information extraction (KIE). Despite their distinct objectives, these tasks share a common need to perceive document content, acquire task-relevant information, and progressively refine intermediate results. However, they are typically formulated as separate prediction problems and addressed by task-specific models or processing pi...

---

### 43. FRAGMENT: Factorized Graph Representations for Document Generation and Editing via Entity-Aware Transformations

**Authors:** Ayoub El Bouchtili, Guilhaume Leroy-Meline

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18679v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18679v1)

**Summary:** Structured documents such as invoices, forms, reports, and scientific articles derive meaning from the interplay between spatial layout, textual content, and logical structure. Generative models operating at the pixel or token level often struggle to capture these dependencies effectively. We explore FRAGMENT, a generative framework that represents a document as a typed relational graph and factorizes its distribution as p(structure, content) = p(structure) * p(content | structure). The framewor...

---

### 44. DynCur-Geo: Dynamic Curiosity Reward Shaping for Multimodal Active Geo-Localization

**Authors:** Yiming Sun, Yang Zhang, Pengfei Zhu

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18673v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18673v1)

**Summary:** Active geo-localization enables low-altitude UAVs to search for specified targets from limited local aerial observations, supporting time-sensitive applications such as search and rescue and emergency inspection. However, multimodal target cues, restricted views, and sparse feedback make it difficult to balance exploration with target convergence. Existing curiosity-driven methods assign a fixed intrinsic-reward weight throughout search, which can continue rewarding novelty after the agent nears...

---

### 45. Vision-Language Models for Egocentric Video: From Hand-Object Interaction to Embodied AI

**Authors:** Mohammad Zamani, Fatemeh Ziaeetabar

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18671v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18671v1)

**Summary:** Egocentric video captures activities from the wearer's perspective, providing a direct view of human attention, hand--object interaction, and goal-directed behavior. This perspective is increasingly important for wearable intelligence, assistive systems, human--robot interaction, and embodied AI, yet it introduces challenges including ego-motion, occlusion, small active objects, viewpoint-dependent appearance, and long-range temporal dependencies. Vision--language models (VLMs) offer a promising...

---

### 46. Teeth2Point: A Two-Stage Dental CBCT ROI-to-Point Segmentation Framework

**Authors:** Qi Ma, Shipra Jain, Niko Benjamin Huber, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18667v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18667v1)

**Summary:** Modern deep learning architectures have demonstrated strong performance in dental CBCT segmentation. One remaining crucial challenge is accurate tooth labeling in cases with missing or malpositioned teeth, which are highly relevant for dental practice. Transformer-based architectures should in theory be able to resolve such ambiguities using global anatomical context. However, due to the high resolution of CBCT volumes and the wide spatial distribution of teeth within volumes, dense patch-based ...

---

### 47. Dynamic SpectraFormer for Ultra-High-Definition Underwater Image Enhancement

**Authors:** Zhiqiang Hu, Tao Yu, Shouren Huang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18662v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18662v1)

**Summary:** Underwater images suffer from color distortion, haze, and poor visibility due to light refraction and absorption in water. These challenges significantly impact the utilization of Autonomous Underwater Vehicles (AUVs) or marine robots. Typically, color and brightness distortions manifest at lower frequencies, while edge and texture distortions are prevalent at higher frequencies. Traditional methods struggle to concurrently rectify these mixed distortions as they primarily concentrate on the spa...

---

### 48. Clinically Structured Surrogate Rewards for Post-SFT Medical Image Captioning

**Authors:** Hyun Jun Kim, Heeseung Shin, Changwon Lim

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18654v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18654v1)

**Summary:** Medical image captioning requires translating heterogeneous visual evidence into concise clinical descriptions, where errors in findings, assertion states, or anatomical relations can alter clinical meaning despite surface-level fluency. Sequence-level policy optimization can directly optimize complete captions, but common rewards rely on global text similarity, direct image-caption compatibility, or unordered concept overlap, leaving visual neighborhoods and clinical-claim structure implicit. W...

---

### 49. SAM2Dual: Training-Free, Dual Memory for Long-Term Video Object Segmentation

**Authors:** JeongRae Kim, Changwon Lim

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18640v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18640v1)

**Summary:** Long-term video object segmentation (VOS) remains challenging due to error accumulation under extended occlusions, re-appearance, and scene changes. Although SAM2 provides strong zero-shot performance, its streaming memory can amplify drift over long horizons when recent, unreliable predictions dominate the memory state. We propose SAM2Dual, a training-free, plug-and-play inference-time enhancement that improves long-video robustness without updating model weights. SAM2Dual introduces a Dual Mem...

---

### 50. When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models

**Authors:** Mehak Gupta, Tanmoy Chakraborty

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18628v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18628v1)

**Summary:** Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking phenomenon: under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. This raises a fundamental question: does safety alignment suppress perceptual grounding itself, or does visual evidence remain internally a...

---

## cs.LG

**50 papers**

### 1. Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning

**Authors:** Zhu Zhang, Jixun Wang, Xiaoang Xu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19181v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19181v1)

**Summary:** On-policy distillation (OPD) trains a student on its own responses using dense token-level guidance from a stronger teacher. In long-context tasks, however, token-level teacher support can favor locally plausible responses that omit evidence distributed across the input or violate global task constraints. Task-specific verifiers, in contrast, evaluate task completion at the response level and may return graded rewards that reflect partial success. We diagnose this mismatch on fixed responses fro...

---

### 2. Lévy Attention: Single-Pass Predictive Uncertainty for Continuous-Time Attention

**Authors:** Sotirios P. Chatzis, Loukas Papadoulas

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19171v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19171v1)

**Summary:** Deep models for irregularly-sampled time series answer queries at arbitrary continuous timestamps, yet report nothing about how far each answer should be trusted. We show the attention layer itself can close that gap: with the right stochastic formulation, the pass that makes each prediction also reports, in closed form and at no extra cost, how far it should be trusted. We introduce Lévy Attention, a cross-attention operator whose output is a stochastic integral against an inhomogeneous Poisson...

---

### 3. Learned, Then Lost: A Measured Single-Example Counterfactual in Pre-training

**Authors:** Zachary Speck, Asa Shepard

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19168v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19168v1)

**Summary:** A single training example's contribution to a finished model is normally estimated rather than measured, because measuring it takes two expensive full pre-training runs that differ in one row of one batch. We ran that counterfactual 24 times at a small scale. We trained 32 GPT-2 models at 124M parameters from scratch on OpenWebText, over four conditions and eight seeds. At step 200 of 9,536, at peak learning rate, we replaced one row of a 256-row batch with a fixed context injection carrying a 1...

---

### 4. Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions

**Authors:** Tomasz R. Bielecki, Thibaut Mastrolia, Haoze Yan

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19151v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19151v1)

**Summary:** We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting. Due to the path dependence of the memory of the Hawkes intensity, this problem does not fall within classical stochastic control theory outside particular Markovian kernels. We first develop a finite-dimensional Markovianization procedure and algorithm to approximate multivariate Hawkes processes with mixtures of exponential kernels. We prove th...

---

### 5. Geometric Iterative Retrieval for Neural Audio Codec Resynthesis

**Authors:** Leo Schmidt-Traub, Frédéric Berdoz, Luca A. Lanzendörfer, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19141v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19141v1)

**Summary:** Neural audio codecs based on Residual Vector Quantization (RVQ) have become the dominant discrete representation for token-based general audio generation, yet resynthesizing high-quality audio from coarse codec tokens remains an open problem and bounds the fidelity of every system that generates them. Prior work has framed resynthesis as a choice between discrete token prediction and continuous regression. We argue that this dichotomy is incomplete and introduce geometric iterative retrieval, a ...

---

### 6. Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems

**Authors:** George Andrikopoulos

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19140v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19140v1)

**Summary:** Frontier language models are compared, marketed, and benchmarked on capability -- what their best or average output can achieve. I argue this measures the wrong axis. The models have saturated accuracy: their mean output lands on the target. What now separates one system from another in practice is precision: how tightly concentrated their outputs are around that target across repeated, identical requests. Borrowing the marksman's distinction, capability is where the average shot lands; reliabil...

---

### 7. SCORE: Subject Coordinate Recovery for Label-Free Cross-Subject EEG-to-Image Retrieval

**Authors:** Zhenyao Cui, Siyuan Kan, Siyang Li, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19134v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19134v1)

**Summary:** Accurate visual decoding can reveal how the brain represents visual information and recover perceived content from neural signals such as electroencephalography (EEG), with potential for neural communication. However, current EEG-to-image retrieval methods perform far below their within-subject counterparts for new users without labeled calibration, limiting real-world deployment. To understand this gap, we analyze EEG features across subjects and find that different subjects preserve similar re...

---

### 8. Beyond Trial Averaging: Anchoring Neural and Visual Representations for Few-Repetition Brain-to-Image Retrieval

**Authors:** Zhenyao Cui, Siyuan Kan, Dingkun Liu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19128v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19128v1)

**Summary:** Decoding visual information from brain signals probes neural representations and enables neuro-rehabilitation and dream decoding. Recent brain-to-image retrieval approaches have achieved promising performance, typically by averaging many (up to 80) neural trials per image, requiring repeated stimulus presentation that increases latency, cost, and user burden. When only one or a few repetitions are available, the retrieval accuracy drops sharply. This drop is commonly attributed to query noise be...

---

### 9. Leaf Values as Coordinates: Exact Contrastive Explanation for Gradient-Boosted Ensembles

**Authors:** Emanuele Luzio

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19127v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19127v1)

**Summary:** A gradient-boosted ensemble predicts by summing one leaf value per tree. Read   those values as coordinates rather than as intermediate results, and every   instance becomes a point in R^M on which the model acts linearly: the score is   the sum of the coordinates.   This small change of view makes contrastive explanation exact. The difference   between two instances is a vector that is identically zero wherever they share   a leaf, so the gap between a rejected applicant and an accepted one is ...

---

### 10. PGFS++: Molecular Property Improvement under Synthesis and Diversity Constraints

**Authors:** Boqiao Zhang, Godbless James, Sai Krishna Gottipati, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19121v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19121v1)

**Summary:** Improving molecular properties, such as drug-likeness or binding affinity, is a recurring task in early-stage drug discovery. However, molecules optimized in an unconstrained chemical space have limited practical value if they cannot be synthesized. Policy Gradient for Forward Synthesis (PGFS) is a synthesis-aware reinforcement learning method for molecular improvement, but its use of reactant embedding prediction makes reactant selection indirect, which, as we show, limits learning effectivenes...

---

### 11. Discretizing Continuous Time Series for Imputation with Masked Diffusion Training

**Authors:** Dongbin Kim, Seungyun Lee, Geonwoo Shin, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19119v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19119v1)

**Summary:** Time series imputation is a crucial area for reliable time series analysis, yet it remains challenging due to the complex temporal dynamics and noise of real-world data. Existing approaches, however, exhibit two limitations: missing and observed values are embedded within the same representation space without explicit structural separation, and continuous diffusion-based methods are trained to predict added noise rather than the original signal. To address these, we propose the Masked Diffusion ...

---

### 12. Enhancing EBSD throughput of battery electrode materials using super-resolution generative adversarial networks

**Authors:** John Mangum, Andrew Glaws, Francois Usseglio-Viretta, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19117v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19117v1)

**Summary:** Quantitative microstructural characterization of Li-ion battery electrode materials using electron backscatter diffraction (EBSD) has been proven as a critical method for optimizing cell performance. However, the inherently slow nature of EBSD can hinder the throughput of analyses needed for statistical representation of a material microstructure being developed. This work demonstrates a machine learning super-resolution framework using a generative adversarial network (SRGAN) to significantly i...

---

### 13. Pretraining Reusable Inference Across Views with Synthetic Task Priors

**Authors:** Jielong Lu, Zhihao Wu, Jiajun Yu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19115v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19115v1)

**Summary:** Modern pretrained encoders make representations from heterogeneous views increasingly reusable, but the procedure that determines view utility and combines evidence is still relearned for each downstream task. Consequently, knowledge about view relevance, complementarity, reliability, and missingness is repeatedly discarded rather than transferred across tasks. We therefore reformulate multi-view learning as learning a reusable, task-conditioned inference procedure rather than a fixed fusion fun...

---

### 14. Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation

**Authors:** Huan-ang Gao, Haohan Chi, Yong Yan, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19098v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19098v1)

**Summary:** Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) experts into a single generalist student via dense, token-level reward supervision. Despite its practical success, the optimization dynamics governing multi-teacher capability integration remain poorly understood, and open, rigorously reproducible recipes are conspicuously lacking. In this work, we establish a controlled M-OPD benchmark on SmolLM3-3B-B...

---

### 15. Does Mapping Non-Maximal Probabilities to GMM Components Matter for S-JEPA Encoder Representations?

**Authors:** Wenxuan He, Yunpeng Li, Shan Liang

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19084v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19084v1)

**Summary:** S-JEPA uses soft Gaussian mixture model (GMM) posteriors instead of hard cluster labels to preserve uncertainty. It remains unclear whether the probability values alone are sufficient, or whether it also matters which GMM components receive the non-maximal probabilities. We test this with two matched controls. FIXED-RANDPERM keeps the top-1 component and probability together with the multiset of non-maximal probability values, but reassigns those non-maximal values using a mapping fixed for each...

---

### 16. Learning Random Geometric Graphs Drawn in Probabilistic Metric Spaces

**Authors:** Dalia Chakrabarty, Kangrui Wang, Chuqiao Zhang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19082v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19082v1)

**Summary:** We present a new data-driven learning of a Random Geometric Graph (RGG) of a multivariate dataset, where the graph is drawn in a probabilistic metric space. This graph learning works for generic datasets, irrespective of the type of the observables; their probability distributions; or size of the data. We identify a metric of the space that the graph is drawn in, as a probability distribution of a random variable that we introduce, namely, a variable that represents the disparity between the con...

---

### 17. SPK: Eliciting Structured Prior Knowledge for Interpretable Out-of-Distribution Detection in Real-Time Object Detection

**Authors:** Changshun Wu, Weicheng He, Xiaowei Huang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19080v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19080v1)

**Summary:** Object detectors often produce over-confident predictions for objects outside their training categories, leading to so-called out-of-distribution (OoD) hallucinations. Existing approaches for detecting or mitigating such hallucinations typically either construct scoring functions directly over learned object detector representations or modify the object detector itself to suppress hallucination emergence. However, the latent priors implicitly encoded in these representations remain largely unexp...

---

### 18. Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk

**Authors:** Deep Kumar Ganguly, Jan Křetínský

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19073v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19073v1)

**Summary:** An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a robust-optimization identity---a confidence level fixes the radius of a relative-entropy ball of alternative models---but that ball cannot reach catastrophes the nominal deems impossible, precisely what a safe agent must hedge. We instead use an optimal-transport ball and study the coherent risk measure it induces, the Wasserstein entropic value-at...

---

### 19. What is Missing from AI Post-Training AI: An Empirical Analysis

**Authors:** Joy Jia Yin Lim, Xin Huang, Hao Peng, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19072v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19072v1)

**Summary:** Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-AI. We argue that this picture conflates two distinct capabilities: execution-level capability, iterating within a selected training strategy; and strategy-level capability, revising the high-level judgment as experimental evidence accumulates. Analyzing a large corpus of publicly released post-train...

---

### 20. Diffusion Models for High-Dimensional Clustered Data: Intrinsic-Dimension Adaptivity via Bayesian Classification

**Authors:** Yuga Iguchi, Paul Fearnhead

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19067v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19067v1)

**Summary:** The empirical success of diffusion models in generative modelling has motivated theoretical work, including quantitative error bounds and qualitative analyses that characterise the different phases of denoising. We bring these two areas together by studying the adaptivity of diffusion models to the structured geometry of multimodal high-dimensional data that consists of multiple clusters in $\mathbb{R}^D$, each with its own low-dimensional structure, and inter-cluster separation depending on $D$...

---

### 21. Multi-Agent Off-Policy Deep Reinforcement Learning for Smart Campus Coverage

**Authors:** Omar Rady, Mohamed Ayman, Ali Arafa, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19049v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19049v1)

**Summary:** Deep reinforcement learning (DRL) has recently gained a great attention due to its real-time adaptation and effectiveness in complex optimization problems. This paper investigates the optimal deployment of millimeter-wave (mmWave) base stations (BSs) in a realistic, non-convex campus topology. The optimization problem is NP-hard, due to the non-convex, non-smooth nature of the max-min fairness objective. To overcome these constraints, we formulate the BS placement as a Markov Decision Process (M...

---

### 22. Bernstein-Vazirani Networks: Quantum Machine Learning by Interference

**Authors:** Natacha Kuete Meli, Tolga Birdal, Prayag Tiwari, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19043v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19043v1)

**Summary:** We introduce Bernstein-Vazirani Networks (BVNs), a non-variational quantum machine learning framework that leverages quantum interference for supervised learning, demonstrated on vision and representation learning tasks. In their standard form, BVNs follow the principle of quantum Fourier sampling: labelled data are placed in superposition and interfered in the Fourier basis to extract globally informative features. We then define generalised BVNs that enable interference in problem-adapted base...

---

### 23. Harness Continual Learning: Continual Adaptation Beyond Model Parameters

**Authors:** Borui Kang, Jinrui Gu, Junhan Lv, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19013v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19013v1)

**Summary:** Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience. Modern agents can also adapt through a harness of prompts, memories, tools, skills, and routing rules. Because these contents jointly shape later execution, a harness update can disrupt previously reliable behavior even when the model is frozen. This raises a new question: how can an agent continually improve its state outside the model while retaining behavior acqui...

---

### 24. Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference

**Authors:** Blazej Banaszewski, Andrew W. Fitzgibbon

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18982v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18982v1)

**Summary:** Bioassay activity prediction is often data-limited because drug-discovery datasets rely on time-consuming and expensive wet-lab experiments for data generation and evaluation. This challenge has inspired recent research into molecular foundation models (MFMs), which aim to encode general-purpose chemical knowledge into molecular representations that generalize well in data-constrained scenarios. This paper presents Monroe, a new MFM with several innovations over the existing state of the art: in...

---

### 25. Fuzzy Accuracy Compensates for Label Subjectivity in Classification of Skin Tone Using Wearable Photoplethysmography Signals

**Authors:** Padmini Krishnadas, Urs Hackstein, Alen Bosnjakovic, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18969v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18969v1)

**Summary:** We consider the problem of classification of skin tone using photoplethysmography (PPG) signals with labels of the ordinal six-class Fitzpatrick skin tones. A typical accuracy for this task is a poor 40-55 %. However, the labels are subjectively determined by comparing the skin with a colour chart, and hence contain widespread small-scale inaccuracies. By working with a "fuzzy accuracy", which deems a prediction of skin tone class to be correct if its difference from the labelled class is not gr...

---

### 26. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis

**Authors:** Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18940v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18940v1)

**Summary:** Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions. We compile CREED-CCV-2+USPTO-XL, an ultra-large-scale dataset of ~45.6 million verified reactions to train the C3LM (Chemistry Constraint-Consisten...

---

### 27. Breaking the weakest link to evade vision language models

**Authors:** Ilan Zini, Boussad Addad, Katarzyna Kapusta

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18938v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18938v1)

**Summary:** Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment. In this work, we investigate the vulnerability of VLMs to adversarial perturbations applied to vi...

---

### 28. Graphical Design of Interpretable Architectures

**Authors:** Pietro Barbiero

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18936v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18936v1)

**Summary:** Designing, implementing, and comparing interpretable architectures requires a formal language to represent them. The most common representations fall short in one of two ways. Symbolic equations give no global view of an architecture at a glance. Probabilistic graphical models and flowcharts do not describe actual tensor manipulations, thus hiding key insights and limiting reproducibility. To close this gap, we introduce a graphical notation for designing interpretable AI architectures, adapted ...

---

### 29. Transportable Causal Effect Estimation across Networks under Interference

**Authors:** Xiaojing Du, Jiuyong Li, Lin Liu, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18932v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18932v1)

**Summary:** Estimating causal effects under network interference typically assumes that the network used for training and the network used for deployment coincide. In practice, an intervention is run on one population while the question of interest concerns a different population, and the two generally differ in topology, node-covariate composition, and spillover pathways. Transporting a causal effect across networks is therefore a data-fusion problem that no existing algorithm solves. We employ a selection...

---

### 30. Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths

**Authors:** Andrej Tschalzev, Stefan Lüdtke, Heiner Stuckenschmidt, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18919v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18919v1)

**Summary:** Tabular machine learning benchmarks typically summarize performance by averaging scores, ranks, or pairwise wins across datasets. Such aggregates are useful for selecting robust default models, but they can obscure a different question: which models are necessary to attain peak performance on particular datasets? We argue that benchmark evaluation should also consider the data-centric peak performance frontier, defined by the best statistically supported performance achieved on each dataset. Fro...

---

### 31. Score the Algebra, Not the Span: Dimension Reduction for Transfer Operator Models of Dynamical Systems

**Authors:** Mark Kozdoba, Shie Mannor

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18918v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18918v1)

**Summary:** Dimension reduction for dynamical systems is standard practice, and the standard route is spectral: model the transfer (Koopman) operator by its leading modes. We show that on systems assembled from several weakly interacting components --- a structure common in physical and biological settings --- this may either require an exponential number of modes, or drop an entire component: the component is absent from the model rather than modeled coarsely, and no function of it can be predicted at any ...

---

### 32. Simple, Safe, and Overlooked: Reclaiming Sustainable Domain Generalization with Statistical Color Matching

**Authors:** Sebastian Doerrich, Francesco Di Salvo, Shyam Nandan Rai, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18915v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18915v1)

**Summary:** Hardware shifts, color variations, and changing patient characteristics between development and deployment routinely break trained medical image classifiers. Existing remedies fall short: standard color jittering provides insufficient diversity, while deep generative style transfer algorithms hallucinate features, destroy clinically relevant structures, and waste massive compute resources. To address this, we revisit classical statistical color matching and repurpose it as Colorist, a highly eff...

---

### 33. Converting Expert Deliberation into Financial Signals Through A Context-Aware NLP Pipeline

**Authors:** Vivek Batra, Kristin Chen, Sanjiv Das, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18911v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18911v1)

**Summary:** We introduce the CDSP (context-conditional deliberation signal pipeline), converting an investment committee's meeting transcripts into structured predictive features. CDSP segments the meeting transcripts into topical chunks, assigns asset-class context labels using a large language model (LLM), maps financial keywords to a pre-determined taxonomy of labels, and constructs complementary features: sentiment polarity and mention frequency. This feature engineering framework is applied to a datase...

---

### 34. On the Slow Convergence to Trivial Solutions of Algorithms for Hard Optimization Problems

**Authors:** Ali Hussaini Umar, Jean Barbier, Matthieu Jonckheere, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18910v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18910v1)

**Summary:** Hard combinatorial optimization problems, many of which are NP-hard, present fundamental algorithmic challenges. Average-case analysis on random instances has emerged as a powerful framework for understanding typical algorithmic performance beyond worst-case guarantees. A substantial body of work has established negative results: for sufficiently hard instances (often controlled by the underlying graph connectivity/constraints density), no known polynomial-time algorithm can significantly outper...

---

### 35. A FEM-Based Surrogate Modelling and Optimization Framework for Physics-Constrained Electromagnetic Coil Design

**Authors:** Yucheng Liu

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18903v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18903v1)

**Summary:** This work evaluates surrogate-assisted optimization of a seven-parameter current-excited coil--core benchmark subject to geometric, manufacturing, and separate core and copper mass constraints. A Python--MPh--COMSOL workflow couples a two-dimensional axisymmetric finite-element method (FEM) model to a Matern 5/2 Gaussian-process (GP) probabilistic surrogate. Here, physics-constrained denotes a design problem evaluated by a governing-equation FEM model and restricted by explicit physical, geometr...

---

### 36. Quantum Tensor Network Learning with DMRG

**Authors:** Gustav J L Jäger, Martin B Plenio, Hans-Martin Rieser

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18901v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18901v1)

**Summary:** Tensor Networks are a relatively new machine learning approach. The architectures proposed initially are inspired by approaches from quantum many-body physics simulations. One common layout is the matrix product state (MPS) also known as a tensor train optimized with gradient descent techniques. We introduce a global normalization condition, so that the MPS represents a quantum state. We investigate two optimization methods that find the locally optimal tensors and compare them regarding their e...

---

### 37. Graph-Based Approaches to Learning Epileptogenic Zone Localization Using Stereo-EEG Recordings

**Authors:** Daniel Wendelken, Brian Ervin, Ravindra Arya, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18887v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18887v1)

**Summary:** The epileptogenic zone (EZ) is the brain region that generates seizures in an individual, and is the target of epilepsy surgery. Localizing the EZ from stereo-EEG (sEEG) recordings supports surgical planning, but manual interpretation is time-consuming and focuses on seizure recordings. Graphical learning models of resting-state functional connectivity among the recorded brain regions are an attractive alternative, but depend crucially on the network topology chosen for the model.   We present a...

---

### 38. Sharper Regret Bounds for Time-Varying Gaussian Process Bandits with Constant Exploration

**Authors:** Matthias Mandl, Hanne Kekkonen

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18863v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18863v1)

**Summary:** We study Bayesian optimization in a time-varying environment where the unknown reward function evolves according to a Gaussian process drift model. Existing GP-UCB analyses in this setting typically require the exploration parameter to grow with the horizon to maintain uniform confidence bounds. Using per-round local confidence events, we show that GP-UCB can instead be run with a constant exploration parameter and obtain an expected-regret bound whose coefficient depends on the drift rate. We a...

---

### 39. Multi-stage neural operator learning with application for convolutions

**Authors:** Zhiping Mao, Zhenye Wen, Yong Zhang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18851v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18851v1)

**Summary:** Convolution integrals widely exist in applications, and to enable fast and accurate computations, this paper introduces two general multi-stage neural operator learning frameworks. The first, Deep Collocation Neural Operator (DCNO), is a supervised approach that iteratively refines the operator approximation by learning residuals from input-output data pairs. The second, Deep Galerkin Neural Operator (DGNO), is an unsupervised framework applicable when the target operator can be represented by a...

---

### 40. GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models

**Authors:** Qi Qin, Jiajie Zhu, Dali Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18849v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18849v1)

**Summary:** Tabular foundation models (TFMs) achieve strong performance through in-context learning, but context-dependent inference imposes substantial latency and memory costs, hindering large-scale deployment. We propose GEAR (\emph{Generative Expansion and Real Anchoring}), a modular two-stage framework that distills TFMs into lightweight MLP or tree-based predictors that can be deployed on commodity CPUs. Stage 1 uses synthetic covariates solely as teacher-query locations and trains the student on soft...

---

### 41. MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models

**Authors:** Chenglin Liu, Xun Wang, Ruishuo Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18827v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18827v1)

**Summary:** Reward function design remains a bottleneck in reinforcement learning. While large language models (LLMs) have enabled automated reward generation, existing methods generate and revise reward functions as monolithic programs, making it difficult to reliably preserve and reuse effective components discovered in earlier iterations, leading to unstable performance across iterations. To address this, we propose Module Level Reward Evolution Framework (MLREF). At the core of MLREF is a module pool, a...

---

### 42. Understanding Multilingual Medical ASR Adaptation Through Layer-Wise Analysis

**Authors:** Souranil Kahali, Rituparna Bose, Abner Hernandez, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18825v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18825v1)

**Summary:** Medical automatic speech recognition (MedASR) requires adaptation to specialised terminology, limited annotated clinical data, and multilingual use cases. Although large-scale pretrained ASR models such as Whisper achieve strong generalisation, their behaviour after medical and multilingual adaptation remains insufficiently understood beyond word error rate (WER). This paper investigates how multilingual medical adaptation reshapes the internal representations of Whisper models through layer-wis...

---

### 43. A Unifying Relational Perspective on Expressive Lottery Tickets

**Authors:** Lorenz Kummer, Samir Moustafa, Anatol Ehrlich, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18819v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18819v1)

**Summary:** Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is poorly understood. The Strong Expressive Lottery Ticket Hypothesis (SELTH) posits the existence of sparse GNNs that preserve Weisfeiler-Leman (WL) expressivity on static graphs. We generalize this existence result to a probabilistic statement for multi-relational and temporal domains via the relational WL (RWL). We prove that sufficiently parame...

---

### 44. Many Optimizers But Only One Training Path: Repeated Resampling for Adaptive Optimizer Selection

**Authors:** Ronald Richman, Mario V. Wüthrich

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18810v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18810v1)

**Summary:** An optimizer is usually chosen before training a deep neural network and then kept fixed. Treating optimizer choice as a hyperparameter could boost performance, but it requires several complete training runs and discards all but the winner. Repeated Optimizer Resampling (ROR) instead searches during one evolving run. Every $b$ epochs, each candidate optimizer scouts from the current model weights for $s$ epochs. The best scout continues for the remaining $b-s$ epochs, and that completed segment ...

---

### 45. Tensor Field Models

**Authors:** Alexander Strunk, Roland Assam

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18808v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18808v1)

**Summary:** This paper introduces Tensor Field Models (TFMs), realization-level Mathematical Structures in which a learned Operator maps a product of admissible component-section families to a prescribed family of time-dependent tangent sections on a Generative State Manifold. Analytic and dynamical restrictions are encoded through the choice of admissible families rather than imposed by the root definition. Constructed, component-separable, and Tensor Bundle TFMs provide structured refinements of this comm...

---

### 46. Forgetting, plasticity, and co-observation: a third facet of continual learning

**Authors:** Timm Hess, Abhishek Jha, Gido M. van de Ven, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18803v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18803v1)

**Summary:** Efficient continual learning remains a fundamental challenge for deep neural networks. While catastrophic forgetting and loss of plasticity are widely considered the primary obstacles to overcome, we show that these two issues cannot fully explain the performance gap between naive sequential training and offline joint training. In this paper, we highlight data co-observation as a distinct factor influencing continual learning performance. By decoupling the constraints of separate data access fro...

---

### 47. A Real-Time Tsetlin Machine-based Non-intrusive Load Monitoring System on MCUs

**Authors:** Tianhang Tan, Han Wu, Tousif Rahman, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18780v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18780v1)

**Summary:** Non-Intrusive Load Monitoring (NILM) systems estimate individual appliance energy consumption from a single aggregate meter, without requiring separate sensors for each device. By installing a single meter that measures a building's total electricity consumption, NILM algorithms can determine the active status of each appliance. However, traditional NILM systems use computationally intensive optimization algorithms to process offline data, limiting their capability for on-device deployment, wher...

---

### 48. GraphK: Variable-Size Graph Generation with Efficient Edge Construction

**Authors:** Resul Tugay, Eren Oluğ, Elif Ak, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18777v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18777v1)

**Summary:** Graph generation models have advanced significantly with deep learning, yet they remain limited in scalability, flexibility, and ability to model underlying structures. We present GraphK, a novel encoder-sampler-decoder framework for graph generation that overcomes these challenges through structural flexibility and computational efficiency. Unlike autoregressive approaches constrained by vocabulary size (i.e. number of nodes in graph generation), GraphK allows for both upscaling (generating gra...

---

### 49. MIFR: A Modality-Invariant and Fair Representation Framework for Skin Disease Classification

**Authors:** Asonyu Senge Njih, Yvan Guifo Fodjo, Vianney Kengne Tchendji, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18774v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18774v1)

**Summary:** Skin diseases represent a major global public health burden, yet machine learning tools developed to assist in their diagnosis suffer from two critical limitations: reliance on only one modality for diagnosis and systematic performance disparities across skin tones. While existing approaches address each challenge separately, this work proposes a modality-invariant framework with fair representation (MIFR) for skin disease classification. The architecture pairs clinical photographs with dermosco...

---

### 50. To Go Far, Go Together: Diverse Preferences Induce a Curriculum for Reward Optimization

**Authors:** Taehyung Kim, Jongeun Choi

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18770v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18770v1)

**Summary:** Learning a reward model from human feedback and optimizing a policy against it is one approach to aligning AI systems with individual users. From a fairness perspective, existing work improves such alignment by developing data-efficient and accurate reward models that capture minority preferences despite scarce data. We push this line of inquiry one step further and argue that data-efficient and accurate per-user reward models are not sufficient: users whose reward models are difficult to \texti...

---

## cs.NE

**50 papers**

### 1. Graphical Design of Interpretable Architectures

**Authors:** Pietro Barbiero

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18936v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18936v1)

**Summary:** Designing, implementing, and comparing interpretable architectures requires a formal language to represent them. The most common representations fall short in one of two ways. Symbolic equations give no global view of an architecture at a glance. Probabilistic graphical models and flowcharts do not describe actual tensor manipulations, thus hiding key insights and limiting reproducibility. To close this gap, we introduce a graphical notation for designing interpretable AI architectures, adapted ...

---

### 2. Biological-Hybrid Intelligence: A Conceptual Framework for Distributed Biological--Artificial Computation

**Authors:** Michael Taynnan Barros, Sergio Lopez Bernal, Reinhold Scherer

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18748v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18748v1)

**Summary:** Biological and artificial systems offer complementary forms of adaptation, learning, and computation, with advances in in-vitro neurotechnology increasingly enabling bidirectional coupling between them. As these systems become more tightly integrated, a key architectural question is how task-relevant computation should be distributed across both substrates. Yet existing biohybrid solutions optimise the biological substrate, the AI model, or their interface without explicitly addressing how such ...

---

### 3. Beyond receptive fields: sequence-pooled normalization can supply most of a sequence labeler's context

**Authors:** Qing Tian

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18576v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18576v1)

**Summary:** A convolutional sequence labeler's receptive field is routinely treated as the extent of the model's usable context: it sets dilation schedules, bounds streaming horizons, and underwrites locality claims. However, we show that this can be false: when a normalization layer computes statistics from the current input along the sequence at inference, those statistics open a sequence-spanning path that bypasses the convolutional receptive field to provide global context. We derive this from the layer...

---

### 4. The Role of Grid Cells in Reducing Spatial Aliasing in Hippocampal Place Representations

**Authors:** Alexander Johnson, Obadah Ghizawi, Ali A. Minai

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18569v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18569v1)

**Summary:** Spatial aliasing occurs when two or more distinct locations produce highly similar place-cell representations, primarily due to environmental symmetry or repetitive structures. This issue is most pronounced when place representations are constructed solely from boundary vector cell (BVC) inputs, because symmetric or repetitive structures can yield indistinguishable sensory patterns across multiple locations in an environment. This work introduces grid cell signals to mitigate spatial aliasing in...

---

### 5. Low-Power, Neuromorphic, Acoustic Anomaly Detection for Persistent Machine Monitoring

**Authors:** Steven C. Nesbit, Victor M. Vergara, Michael A. Felix, et al.

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18341v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18341v1)

**Summary:** Persistent acoustic monitoring can detect machine faults without physical contact, but always-on inference is constrained by power, latency, and deployment complexity. We demonstrate autoencoder-based acoustic anomaly detection on an Intel Loihi 2 neuromorphic processor under clean and noisy conditions. Log-mel features are computed off chip; normalization, autoencoder inference, L1 reconstruction scoring, and thresholding run on chip. In a clean, microphone-position-invariant ToyADMOS ToyCar be...

---

### 6. SeisEvo: Evolution of Seismic Data Reconstruction Algorithms by Agents

**Authors:** Yingjie Xu, Siwei Yu, Jianwei Ma

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18272v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18272v1)

**Summary:** Classical seismic data reconstruction relies on manually designed structural priors and iterative operators, whose coupled design space is far larger than manual trial and error can explore systematically. Deep-learning methods encode the reconstruction rules in learned weights rather than in an explicit operator that can be inspected and modified. We propose SeisEvo (Seismic Algorithm Evolution), which does not optimize a single reconstruction result but searches for the algorithm that produces...

---

### 7. Procedural Content Metageneration via Program Search and Continual Abstraction Discovery

**Authors:** Matthew Siper, Ahmed Khalifa, Julian Togelius

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17947v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17947v1)

**Summary:** Large language models can generate executable programs, which makes it possible to search directly over procedural content generators rather than individual levels. We study this approach in Sokoban, Zelda, Dangerous Dave, and Lode Runner. Each run evolves complete Python generators through language-model mutation and crossover. We introduce Continual Abstraction Discovery, or CAD, which extracts reusable primitives from high-fitness programs into a run-specific helper module. A 2x2 experiment c...

---

### 8. Computational Prosopography across a Millennium: Mathematically Oriented Lineages Traced from the Fields Medalists

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17915v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17915v1)

**Summary:** We reconstruct the mentor--student network through which documented scholarly training passed across roughly nine centuries, and subject both the network and the means of reconstructing it to source criticism. From Wikidata, which aggregates the Mathematics Genealogy Project and the MacTutor Archive, we extract approximately 470,000 mentor--student assertions, yielding a directed acyclic graph of 372,853 persons. Using all 64 historical Fields Medalists as a fixed, ex ante tracer set, backward t...

---

### 9. Optically Writable Atomic Vapor Memory as a Substrate for Optical Reservoir Computing

**Authors:** Elizabeth Robertson, Mingwei Yang, Lina Jaurigue, et al.

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17807v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17807v1)

**Summary:** We present an optical random access memory (ORAM) based on warm cesium (Cs) atomic vapor and demonstrate its operation as the physical substrate of a reservoir computer. Information is stored in the hyperfine population distribution of a Cs ensemble via optical pumping and retrieved through differential probe absorption. Spatial multiplexing via acousto-optic deflection provides eight addressable memory rails able to store up to 3.8 bits of information per rail. Employing this platform as a temp...

---

### 10. Automating Parent Selection Configuration in Genetic Programming with Agentic AI

**Authors:** Jose Guadalupe Hernandez, Jui-Hsuan Chang, Anil Kumar Saini, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.17172v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17172v1)

**Summary:** We investigate whether agentic artificial intelligence can automate parts of the process of designing genetic programming systems by introducing an agentic framework that identifies and implements parent selection algorithms using large language model (LLM) reasoning and retrieval-augmented generation. Using symbolic regression as a test bed, we first conduct an ablation study across four LLM types to evaluate the effects of agentic reasoning and retrieval on generated algorithm categories, vali...

---

### 11. Drive, Pack, Fly: The Travelling Thief Problem with Drone

**Authors:** Kabir Murjani, Abhay Sobhanan

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16435v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16435v1)

**Summary:** In collection operations, accumulating payload progressively slows the vehicle, imposing a cumulative penalty on routing efficiency. An onboard drone can offset this penalty by retrieving outlying items, thereby shortening the makespan and increasing operational profit. However, travel time remains load-dependent, and each item collected by the ground vehicle shifts the arrival times that govern the drone's launch and rendezvous points. This paper introduces the Travelling Thief Problem with Dro...

---

### 12. Evolving Executable Pipeline Programs for AutoML with Language Models

**Authors:** Sofoklis Kitharidis, Cor J. Veenman, Jan N. van Rijn, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16416v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16416v1)

**Summary:** Automated machine learning (AutoML) systems search for pipelines within a space of preprocessing operators, learners, and hyper-parameters specified in advance: they can select and tune known components, but cannot produce structure outside that space. We present LACE, an AutoML framework that instead searches over complete executable pipeline programs: an evolutionary loop maintains a population of scikit-learn-compatible Python classes, and a large language model acts as the variation operator...

---

### 13. A Control-Theoretic Formulation of Global Workspace Theory

**Authors:** Ryota Kanai

**Published:** 2026-08-16

🔗 [Paper](http://arxiv.org/abs/2608.15926v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15926v1)

**Summary:** Global workspace theory explains conscious access as the broadcasting of selected information to the rest of the network, but it lacks a formal criterion for identifying the mechanism that enables this access. We propose that a global workspace is a mediator, namely, a subnetwork that receives activity from distributed systems, transforms it through internal modes, and returns differentiated effects to the broader network. We formalize this claim as the Global Mediation Workspace (GMW), a contro...

---

### 14. ATLAS: Scaffold-Free Algorithm Synthesis by LLMs via Embedding-Guided Quality-Diversity Search

**Authors:** Danial Yazdani, Mohammad Nabi Omidvar, Yuan Sun, et al.

**Published:** 2026-08-16

🔗 [Paper](http://arxiv.org/abs/2608.15546v2) | 📄 [PDF](https://arxiv.org/pdf/2608.15546v2)

**Summary:** Most LLM-based automated algorithm design methods optimize a designated component within a human-specified scaffold, fixing overall organization and component interactions. We present ATLAS, an embedding-guided quality-diversity framework for scaffold-free full-algorithm synthesis in combinatorial optimization. The problem specification supplies objectives and constraints; a minimal I/O interface fixes only instance and solution formats; the LLM chooses and restructures components, interactions,...

---

### 15. Mental Model Management: An Operator-Based Framework for LLM Memory

**Authors:** Oliver Kramer

**Published:** 2026-08-16

🔗 [Paper](http://arxiv.org/abs/2608.15451v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15451v1)

**Summary:** Large language models process large amounts of information but usually lack an explicit mechanism for maintaining compact and evolving conceptual representations. We introduce Mental Model Management (3M), a framework in which knowledge is represented as mental models consisting of compact chunks. Rather than accumulating text passages, 3M continuously integrates new information into an existing conceptual representation. A set of operators extracts knowledge, retrieves relevant models, adds and...

---

### 16. Language models suffer from a curse of ambiguity

**Authors:** Nicolas Zucchet, Hyun Dong Lee, Scott Linderman

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15448v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15448v1)

**Summary:** Large language models increasingly rely on sampling as a driver of their own improvement, making the fidelity of their learned distributions more critical than ever. Yet, not all distributions are equally easy to learn. In this work, we identify a curse of ambiguity: in large language models, and more broadly in all neural networks that produce discrete probability distributions, the more ambiguous a next-token distribution is, the harder it is to learn accurately. Through an extensive theoretic...

---

### 17. Chameleon: An Adaptive AI-Driven Honeypot Architecture Using Threat-Calibrated Particle Swarm Optimization and Semantic Deception Rapidly-Exploring Random Trees

**Authors:** Rohit Swami, Tushar Singh, Akash Warde, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15407v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15407v1)

**Summary:** An invariant behavioral profile is the defining vulnerability of traditional honeypot installations: a skilled adversary can confirm the presence of a deception environment within only a few diagnostic commands, limiting its intelligence value. High-cost commercial deception products (USD 100,000--150,000 per year) share a related weakness in that their response engines are not coupled to real-time model-driven feedback. Chameleon is an openly distributed adaptive honeypot platform introduced he...

---

### 18. External Sinkhole Attack Detection in Large-Scale WSNs Using Metaheuristic Feature Selection

**Authors:** Seungwoo Han, Sawako Kitagata, Ingon Chanpornpakdi, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15274v2) | 📄 [PDF](https://arxiv.org/pdf/2608.15274v2)

**Summary:** Sinkhole attacks in large-scale wireless sensor networks (WSNs) pose a serious threat to network functionality. This paper presents a metaheuristic feature selection for sinkhole attack detection using the bee swarm optimization (BSO) algorithm. In an external sinkhole attack simulation with 2000 nodes deployed over a 3000 $\times$ 3000 m$^2$ field, the proposed method achieves a detection accuracy of 0.997 while reducing the 16-feature set to eight features.

---

### 19. Adaptive Protection for Evolutionary Feature Construction in Symbolic Regression with Application to Credit Classification

**Authors:** Hengzhe Zhang, Qi Chen, Bing Xue, et al.

**Published:** 2026-08-14

🔗 [Paper](http://arxiv.org/abs/2608.14209v1) | 📄 [PDF](https://arxiv.org/pdf/2608.14209v1)

**Summary:** Evolutionary feature construction has shown strong promise in symbolic regression by automatically discovering informative transformations of input features that enhance a simple base learner. However, existing approaches often lack explicit mechanisms to preserve important constructed features discovered during evolution, and valuable genetic material can be lost when genetic operators disrupt effective features. This paper introduces an adaptive protection mechanism that leverages feature impo...

---

### 20. Emergent Models: Intelligence from Tiny Substrates

**Authors:** Giacomo Bocchese, Nicola Giacobbo, Etienne Guichard, et al.

**Published:** 2026-08-14

🔗 [Paper](http://arxiv.org/abs/2608.14019v1) | 📄 [PDF](https://arxiv.org/pdf/2608.14019v1)

**Summary:** Emergent Models (EMs) are a machine learning paradigm based on simple yet open-ended substrates, such as cellular automata, in which modeling is treated not as the learning of a closed-form input-output map but as the emergence, within simple dynamical systems, of computational behaviors that solve external tasks. Such substrates typically iterate a fixed local rule over a latent space for an adaptive number of steps, with an interface linking the latent state to external input/output signals. T...

---

### 21. Reducing ANN-SNN Conversion Error via Residual Membrane Potential Alignment

**Authors:** Zirui Chen, Zihan Huang, Tong Bu, et al.

**Published:** 2026-08-14

🔗 [Paper](http://arxiv.org/abs/2608.13952v1) | 📄 [PDF](https://arxiv.org/pdf/2608.13952v1)

**Summary:** Spiking Neural Networks (SNNs) serve as core architectures for neuromorphic computing thanks to event-driven operation and ultra-low power consumption. Direct SNN training is hindered by non-differentiable spikes that induce vanishing gradients and unstable optimization. ANN-SNN conversion circumvents such issues by reusing well-trained ANN weights for low-latency, energy-efficient inference. Nevertheless, existing conversion schemes suffer from severe accuracy drops at small timesteps, large in...

---

### 22. SAGE: Surrogate-gradient Adaptation via Attention-Guided Entropy for Spiking Transformers

**Authors:** Kiran Nair, Rodrigue Rizk, KC Santosh

**Published:** 2026-08-13

🔗 [Paper](http://arxiv.org/abs/2608.13702v1) | 📄 [PDF](https://arxiv.org/pdf/2608.13702v1)

**Summary:** Spiking neural networks (SNNs) offer an energy-efficient alternative to conventional deep neural networks by exploiting sparse event-driven computation, but their training remains challenging because the non-differentiable spike function requires surrogate gradients whose fixed shape may be suboptimal across layers and training stages. In this work, we introduce SAGE, an uncertainty-modulated surrogate-gradient mechanism for Transformer-based SNNs. SAGE estimates block-level uncertainty from nor...

---

### 23. Insights from Multi-tasking the EAX Algorithm for the Travelling Salesperson Problem

**Authors:** Liam Wigney, Aneta Neumann, Yew-Soon Ong, et al.

**Published:** 2026-08-13

🔗 [Paper](http://arxiv.org/abs/2608.12772v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12772v1)

**Summary:** Evolutionary multitasking allows several related problems to be solved in a single run of an algorithm. In this paper, we investigate integrating evolutionary multitasking with Edge Assembly Crossover (MT-EAX) to solve the classical Travelling Salesperson Problem (TSP). To fairly compare MT-EAX against standard EAX under strict compute budgets, we evaluate three scaling methods: generation scaling, population scaling, and balanced scaling. Our results show that generationally scaled MT-EAX is hi...

---

### 24. Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies

**Authors:** Conor F. Hayes, Elliot Meyerson, Kajetan Schweighofer, et al.

**Published:** 2026-08-13

🔗 [Paper](http://arxiv.org/abs/2608.12679v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12679v1)

**Summary:** Large Language Models (LLMs) are increasingly deployed in discovery domains such as math and science. The usual approach is to present the problem to the model and use its answer as the proposed solution. However, beyond this best guess, discovery can be enhanced by increasing test-time compute. In a process called pass@k, the model is allowed to explore the solution space and generate diverse candidate solutions. Unfortunately, the standard approach to post-training LLMs through Reinforcement L...

---

### 25. Lapis: Laplacian Spiking Attention via First-Spike Timing and Membrane Leakage

**Authors:** Kaiwen Tang, Jiaqi Zheng, Zixuan Zhu, et al.

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.11865v2) | 📄 [PDF](https://arxiv.org/pdf/2608.11865v2)

**Summary:** Self-attention has become central to spiking vision transformers, yet its query-key scoring is still largely inherited from dense networks. Existing spiking variants either simplify dot product scoring or replace it with discrete operators, but spike timing, the native variable of a spiking network, does not directly define how tokens are related. We propose Lapis, a spiking attention mechanism that scores each token pair by the L1 distance between its query and key first-spike latency vectors u...

---

### 26. Predictive Allostatic Organization in Recurrent and Spiking Agents Under Partial Observability

**Authors:** Frederick Hayes

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.11506v1) | 📄 [PDF](https://arxiv.org/pdf/2608.11506v1)

**Summary:** Adaptive behavior under partial observability depends on internal organization that carries information beyond the current observation. Drawing on Barrett and Miller's account of categorization as predictive, compressive, functionally organized, and allostatically constrained, we test whether recurrent and spiking agents develop internal states with corresponding computational properties. Agents operate in an energy-constrained foraging task requiring resource acquisition, threat avoidance, cont...

---

### 27. Contextual Quality-Diversity Evolutionary Reinforcement Learning for HVAC Control in Tropical Commercial Buildings

**Authors:** Tran Le Vu

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.11324v1) | 📄 [PDF](https://arxiv.org/pdf/2608.11324v1)

**Summary:** This paper proposes a contextual quality-diversity evolutionary reinforcement-learning controller, CQD-ERL, for the supervisory control of a tropical, water-cooled chiller plant and its associated air side. Rather than converging to a single scalarised policy, the controller maintains a product archive of specialised policies indexed jointly by a data- driven operating context, a cluster of daily weather and load regime, and a context-invariant behaviour descriptor, filled by a gradient-free evo...

---

### 28. EvoMem: Memory-Augmented Evolution for Code Optimization

**Authors:** Viktor Volkov, Valentin Khrulkov, Andrey V. Galichin, et al.

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.10795v1) | 📄 [PDF](https://arxiv.org/pdf/2608.10795v1)

**Summary:** Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks and domains. However, existing LLM-driven evolutionary frameworks largely discard such knowledge, repeatedly rediscovering similar ideas and limiting opportunities for cross-run and cross-task learning. We introduce EvoMem, a persistent memory architecture for LLM-based evolutionary program search that captures and reuse...

---

### 29. Optimize Cheap, Deploy Strong: Cost-Aware Cross-Tier Transfer for Evolutionary Optimization

**Authors:** Tal Oved, Roi Pony, Oshri Naparstek, et al.

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.10694v2) | 📄 [PDF](https://arxiv.org/pdf/2608.10694v2)

**Summary:** Evolutionary optimization of LLM prompts and agentic programs (e.g., GEPA) is dominated by fitness evaluation: scoring each candidate runs an answering LLM over a validation set, so the evaluator's price tier dictates total search cost. We restructure that search by decoupling the three roles an LLM plays, running the high-volume answering role on the cheapest tier, reserving a strong model for the rare reflection/variation operator, then exploiting upward cross-tier transfer to deploy the cheap...

---

### 30. Persistent Recursive Worlds Enable Autonomous Software Evolution

**Authors:** Beichen Huang, Zhenyu Liang, Bowen Zheng, et al.

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.10450v3) | 📄 [PDF](https://arxiv.org/pdf/2608.10450v3)

**Summary:** Complex software systems develop over timescales that exceed the lifespan of any individual coding agent. Most agentic software systems preserve continuity through persistent sessions, memories, managers or shared context. We introduce EvoX Genesis (hereafter, Genesis), which instead makes the software project persistent while allowing local agents to remain finite-lived. Genesis represents software as a persistent recursive world: each local world is situated by an accepted version and a reposi...

---

### 31. Multitask Pareto Optimization for Monotone Submodular Problems with Dynamic Constraints

**Authors:** Liam Wigney, Frank Neumann

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.10425v2) | 📄 [PDF](https://arxiv.org/pdf/2608.10425v2)

**Summary:** Evolutionary multitasking is a recent approach that solves multiple related optimization problems within a single evolutionary run, rather than addressing each problem separately. We consider monotone submodular optimization problems with dynamic knapsack constraints and study a multitasking formulation in which all tasks share a common monotone submodular function $f$, but differ in their constraints. We focus on the case where elements within each constraint have uniform cost and show that thi...

---

### 32. Neuroevolution Arena: Nested Ecological Evaluation of Update-and-Inheritance Regimes across Neural Architectures

**Authors:** Yuxu Ge, Yifei Cheng

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.10323v1) | 📄 [PDF](https://arxiv.org/pdf/2608.10323v1)

**Summary:** Competitive artificial-life systems can rank trained controllers differently under training and ecological evaluation. We present Neuroevolution Arena, a GPU-accelerated spatial ecology of independently parameterized neural-network cells, and an audit-tracked nested evaluation protocol. Three implementation-specific update-and-inheritance regimes (EvoEvo, EvoRL, and RLRL) are crossed with two neural architectures for 50,000 generations in three independent training runs per condition. One saved ...

---

### 33. A Graph Neural Network--Guided Genetic Algorithm for Physical Internet Supply Chain Optimization under Cost Uncertainty

**Authors:** Faezeh Ardali, Gerald M. Knapp

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.10245v1) | 📄 [PDF](https://arxiv.org/pdf/2608.10245v1)

**Summary:** Inventory and distribution planning in Physical Internet networks requires coordinating factory-hub assignments, factory supply, lateral transshipment among collaborative hubs, retailer deliveries, and shortages. The problem combines discrete assignment decisions with interdependent continuous flows, while uncertain operating costs make robust planning more difficult. This study formulates deterministic and min-max regret models for a three-echelon network of factories, hubs, and retailers and d...

---

### 34. DSLE: A Learning Environment for Dark Souls Boss Encounters

**Authors:** Derin Gezgin, Jim O'Connor, Tanner Goodwin, et al.

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.09902v1) | 📄 [PDF](https://arxiv.org/pdf/2608.09902v1)

**Summary:** We introduce the Dark Souls Learning Environment (DSLE), a containerized platform that presents all 22 boss encounters of Dark Souls: Remastered as game-playing agent benchmarks through a Gymnasium-style interface. DSLE combines real-time combat, high-dimensional visual input, and sparse terminal rewards, with each environment step being a real action executed against the running game. To support controlled comparison, we define DSLE-5, a representative five-boss subset, spanning a melee fight, ...

---

### 35. BDH-CQ: In-Context Learning with Recurrent Latent Reasoning

**Authors:** Björn Engdahl, Adrian Kosowski, Jan Chorowski, et al.

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.09888v1) | 📄 [PDF](https://arxiv.org/pdf/2608.09888v1)

**Summary:** We introduce BDH-CQ, a reasoning model that combines in-context learning with recurrent latent reasoning. Inputs presented at inference time continuously update the model's recurrent memory; the model then solves a query through iterative computation in a high-dimensional latent space, without verbalizing its intermediate reasoning. We evaluate the model on the public ARC-AGI-1 evaluation set and use controlled ARC-like interventions to study what it learns from demonstrations, how consistently ...

---

### 36. Identifying potentiating events in evolutionary search using replay experiments

**Authors:** Austin J. Ferguson, Alexander Lalejini

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.09833v1) | 📄 [PDF](https://arxiv.org/pdf/2608.09833v1)

**Summary:** In this work, we introduce analytical replay experiments to the evolutionary computing community. Replay experiments originated in the context of laboratory experimental evolution as an empirical approach to identifying potentiating events that increased the likelihood of an observed evolutionary outcome. By restarting a population's evolution from different historical time points, replay experiments sample the distribution of what could have evolved from different points in time, which allows u...

---

### 37. A New Approach to Characterising Optimisation Problems Using Programmatic Representation and Complexity Measures

**Authors:** Marcus Gallagher, Katherine M. Malan

**Published:** 2026-08-09

🔗 [Paper](http://arxiv.org/abs/2608.08898v1) | 📄 [PDF](https://arxiv.org/pdf/2608.08898v1)

**Summary:** Characterising optimisation problem instances is a fundamental part of understanding the behaviour and performance of different algorithms as well as providing information for algorithm selection and configuration. In this paper we propose a novel approach to problem characterisation based on the representation of instances when implemented as a program. The intuition is that the complexity of the code required to express an objective function should relate to the complexity of the search landsc...

---

### 38. Rethinking Attention Locality in Spiking Transformers

**Authors:** Zeqi Zheng, Zizheng Zhu, Yuping Yan, et al.

**Published:** 2026-08-09

🔗 [Paper](http://arxiv.org/abs/2608.08541v1) | 📄 [PDF](https://arxiv.org/pdf/2608.08541v1)

**Summary:** Spiking Transformers provide a promising paradigm for efficient visual processing with spike-driven computation, yet their Softmax-free Spiking Self-Attention (SSA) struggles to establish spatially localized token interactions. Although existing locality-enhanced SSA methods improve accuracy, it remains unclear whether they consistently induce spatial locality across layers and different Spiking Transformer architectures. Through Mean Attention Distance (MAD) analysis, we reveal that computation...

---

### 39. SuperNeuroMAT: An Efficient Matrix-based Simulator for Spiking Neural Networks

**Authors:** Prasanna Date, Kevin Zhu, Shruti Kulkarni, et al.

**Published:** 2026-08-09

🔗 [Paper](http://arxiv.org/abs/2608.08479v1) | 📄 [PDF](https://arxiv.org/pdf/2608.08479v1)

**Summary:** Spiking neural networks (SNNs) offer a promising pathway to energy-efficient AI and brain-inspired computing. However, their widespread adoption is hindered by a lack of fast, accessible, and versatile simulation frameworks. In this paper, we introduce SuperNeuroMAT, an open-source, scalable, and highly efficient Python-based SNN simulator. We devise a novel matrix-based approach to model the leaky integrate-and-fire (LIF) neuron dynamics and natively support dense and sparse execution modes. Th...

---

### 40. High-Capacity Generalized Hopfield Networks

**Authors:** Victor Galitski

**Published:** 2026-08-08

🔗 [Paper](http://arxiv.org/abs/2608.08226v1) | 📄 [PDF](https://arxiv.org/pdf/2608.08226v1)

**Summary:** Generalized Hopfield networks are introduced where memories and neurons are continuous variables that lie on a Riemannian manifold. We explicitly focus on symmetric spaces associated with the special unitary groups SU(d), and use both numerical and analytical (replica) techniques to demonstrate an almost order of magnitude enhancement in critical capacity over the vector networks starting with d=3 and further rapidly growing with d. To circumvent the non-linear geometric constraints, we use a Li...

---

### 41. A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven Optimization

**Authors:** Víctor Gallego

**Published:** 2026-08-08

🔗 [Paper](http://arxiv.org/abs/2608.08156v1) | 📄 [PDF](https://arxiv.org/pdf/2608.08156v1)

**Summary:** In evolutionary algorithms powered by language models, the LLM acts as a single operator that simultaneously updates structural components (like control flow) and continuous parameters. While LLMs can be good at the first, they are not efficient at the second, wasting tokens taking discrete jumps inside a trial and error loop. We resolve this by formalizing a hybrid nested search, in which an outer loop has the LLM propose a structural sketch, with numeric gaps, and an inner numerical optimizer ...

---

### 42. RotaryQuant: Fitting 120B MoE Models on Consumer Hardware via Fused Compressed-Space Attention

**Authors:** Anthony. Lui, Mohamed. Elsaied, N. P. Savani

**Published:** 2026-08-08

🔗 [Paper](http://arxiv.org/abs/2608.08081v1) | 📄 [PDF](https://arxiv.org/pdf/2608.08081v1)

**Summary:** Large mixture-of-experts (MoE) language models with 26--120 billion parameters exceed the memory capacity of consumer devices through three simultaneous pressures: resident weight matrices, key-value (KV) cache state that grows linearly with context, and dozens of expert sublayers that must be paged on demand. We present RotaryQuant, a three-axis compression system that addresses all three. Mixed-precision weight quantization assigns bit-widths by architectural role: 4-bit for dense layers, 2-bi...

---

### 43. Phase State Space Models: Parallel, Surrogate-Free Training of Spiking Networks

**Authors:** Wilkie Olin-Ammentorp

**Published:** 2026-08-07

🔗 [Paper](http://arxiv.org/abs/2608.07754v1) | 📄 [PDF](https://arxiv.org/pdf/2608.07754v1)

**Summary:** State-space models (SSMs) provide a powerful theoretical framework to enable parallel training of recurrent networks. We expand on previous work adapting SSMs to spiking models to provide a novel interpretation of resonate-and-fire (R\&F) neural networks which is compatible both with real and spiking inputs, parallel and recurrent execution, has clear connections to hyperdimensional (HD) computing, and maintains biologically-realistic features. We demonstrate an implementation of this approach w...

---

### 44. Adaptive Hybrid Particle Swarm Optimization with Gradient Descent

**Authors:** Aryan Gurudeo

**Published:** 2026-08-07

🔗 [Paper](http://arxiv.org/abs/2608.11258v1) | 📄 [PDF](https://arxiv.org/pdf/2608.11258v1)

**Summary:** Gradient injection helps Particle Swarm Optimization (PSO) only when the swarm has identified a basin with smooth local structure, not universally. We propose Adaptive Hybrid PSO (AHPSO), which uses a sigmoid function on swarm diversity to automatically modulate gradient influence: near-zero during exploration, near-maximum during exploitation, with no manual phase-switching. Under budget-normalized comparison (PSO given equivalent total function evaluations), PSO wins 52.5% of 40 configurations...

---

### 45. Recipes for Creativity: Iterative Generation and Evaluation in Large Language Models

**Authors:** Rens Anderson, Tessa Verhoef, Amirhossein Zohrehvand

**Published:** 2026-08-07

🔗 [Paper](http://arxiv.org/abs/2608.07243v1) | 📄 [PDF](https://arxiv.org/pdf/2608.07243v1)

**Summary:** Generative models are often evaluated through singular artifacts, whereas human creativity typically emerges through iterative generation, appraisal, and refinement. This pilot study examines whether iterative search improves LLM creativity by adapting FunSearch to recipe generation for the 2024 Pillsbury Bake-Off and evaluating outputs against human benchmarks using TTCT-based LLM evaluation. Across two experiments, we test iteration count, generator temperature, and in-loop selection-scorer mo...

---

### 46. LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning

**Authors:** Riccardo Curcio, Hongpeng Cao, Marco Caccamo

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06481v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06481v1)

**Summary:** Training controllers that are safe and robust in simulation, and systematically assessing their readiness for real-world deployment, remain key challenges in sim-to-real transfer. To address this, we propose LyEvO, a physics-grounded framework that combines constrained Evolutionary Optimization and Statistical Model Checking (SMC)-based verification with Lyapunov-based stability analysis. Leveraging prior knowledge of the system dynamics, LyEvO uses Lyapunov analysis to compute an initial candid...

---

### 47. Threshold-Based Early Stopping of Accumulations in Neural Networks with Binary Activation

**Authors:** Quentin Luquet de Saint-Germain, Massil Ait Abdeslam, Jean Pierre David

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06177v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06177v1)

**Summary:** Binary neural networks are very attractive for constrained deployment, enabling small footprint and low-power inference. For binary activations, the dot products become sign-controlled additions or subtractions, but the number of operations is unchanged. Indeed, every neuron or output channel still accumulates all of its input, even though only the sign will be retained, which is often wasteful. As the accumulation progresses, the running partial sum frequently drifts so far from zero that its f...

---

### 48. A Special Point Skeleton Reconstruction Algorithm for Dynamic Multiobjective Optimization

**Authors:** GuangXian Gan, MinRong Chen

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06096v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06096v1)

**Summary:** To address the issue that existing dynamic multi-objective optimization algorithms mainly rely on individual migration or independent special point sampling after environmental changes, while failing to fully exploit the structural relationships among representative solutions, a Special Point Skeleton Reconstruction based Dynamic Multi-Objective Evolutionary Algorithm (SPSR-DMOEA) is proposed. First, the centroid, knee points, and extreme points are extracted from the Pareto optimal solution set...

---

### 49. Convergent Evolution in Neural Representation Space: Emergent Order in Deep Belief Networks

**Authors:** Patrick Krauss, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05996v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05996v1)

**Summary:** Deep Belief Networks (DBNs) learn hierarchical generative models without class supervision. Here, we ask whether this purely unsupervised process nevertheless organizes internal representations according to the unknown data classes. We analyze successive layers of DBNs trained on MNIST, Fashion-MNIST, and KMNIST using the Generalized Discrimination Value (GDV), supervised probes applied only after training, a reconstruction-based measure of abstraction distance, effective dimensionality, and fre...

---

### 50. Relay, Don't Route: Adaptive Population Handoff for Cost-Efficient LLM-Driven Evolution

**Authors:** Sichun Luo, Yi Huang, Guanzhi Deng, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05651v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05651v1)

**Summary:** Large language model (LLM)-driven evolution has shown promise for program search and algorithm discovery, but relying on strong models throughout long evolutionary runs is costly. A natural alternative is to combine cheap and strong models under a fixed inference budget. However, existing approaches typically allocate models at the level of individual queries or mutation steps, overlooking that evolutionary search is \textit{stateful}: each generated candidate changes the population from which s...

---

## q-bio.NC

**50 papers**

### 1. Transcranial magnetic stimulation of visual-motion area V5/MT modulates sensory thalamus responses during visual speech recognition

**Authors:** Lisa Jeschke, Christa Mueller-Axt, Alejandro Tabas, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19034v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19034v1)

**Summary:** Responses in the sensory thalamic nuclei are modulated by perceptual tasks. Whether such response modulations rely on feedback from cerebral cortex in humans is unknown. Here, we addressed this question in the context of visual speech recognition: the visual sensory thalamus, i.e. the lateral geniculate nucleus (LGN), has differential BOLD-responses to visual speech than non-speech control tasks. We tested whether such response modulation relies on the function of the visual association cortex, ...

---

### 2. The Role of Grid Cells in Reducing Spatial Aliasing in Hippocampal Place Representations

**Authors:** Alexander Johnson, Obadah Ghizawi, Ali A. Minai

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18569v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18569v1)

**Summary:** Spatial aliasing occurs when two or more distinct locations produce highly similar place-cell representations, primarily due to environmental symmetry or repetitive structures. This issue is most pronounced when place representations are constructed solely from boundary vector cell (BVC) inputs, because symmetric or repetitive structures can yield indistinguishable sensory patterns across multiple locations in an environment. This work introduces grid cell signals to mitigate spatial aliasing in...

---

### 3. Phase-based spatial ordinal patterns for characterizing oscillatory dynamics

**Authors:** Robison J. Santos-Silva, Bruno R. R. Boaretto, Thiago L. Prado, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.17196v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17196v1)

**Summary:** The emergence of organized spatiotemporal patterns is ubiquitous in oscillatory systems, from neural populations to engineered networks. Identifying these patterns and tracking how they evolve over time remains challenging, particularly when systems exhibit transient dynamics. Here, we introduce a framework based on spatial ordinal patterns to characterize the spatiotemporal dynamics of oscillatory systems. Our approach acts directly on the phase rather than the amplitude, with additional patter...

---

### 4. Order-Sensitive Fast-Synapse Limits in Sparse Excitatory-Inhibitory Threshold-Reset Networks

**Authors:** Tonic Song

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16701v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16701v1)

**Summary:** Componentwise weak convergence of signed synaptic kernels does not, by itself, determine the fast-synapse limit of a sparse threshold-reset network. Within a causal event protocol with clamped refractoriness and smooth positive-delay kernels, we construct two families whose excitatory and inhibitory measures converge weakly to $δ_0$ while their microscopic arrival orders are reversed. A target fires in the excitatory-first family and not in the inhibitory-first family precisely when $x+a-b<θ\le ...

---

### 5. Continual-learning rules shape representational drift

**Authors:** Yikai Si, Shanshan Qin

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16141v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16141v1)

**Summary:** Lifelong learning requires acquiring new knowledge without erasing the old. Yet neural population codes for familiar stimuli and behaviors change over days and weeks. This coexistence of stable memory and changing internal codes may depend on how a learning system prevents forgetting. We therefore tested whether different continual-learning mechanisms produce distinct patterns of representational drift. We trained convolutional networks on sequential image classification tasks and recurrent netw...

---

### 6. Multi-Feature Riemannian Hypergraph for Online Test-Time Adaptation of Motor Imagery Brain-Computer Interface

**Authors:** Siqi Li, Zhi Li, Tong Liu, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16134v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16134v1)

**Summary:** In clinical motor imagery brain-computer interface (MI-BCI) decoding, cross-day transferability and online operation remain two critical challenges. Hypergraphs can improve transferability by capturing higher-order sample relationships, yet existing hypergraph-based methods for online emotion recognition neglect the cross-day benefits of Riemannian geometry widely adopted in EEG transfer learning. To bridge this gap, we propose the Multi-feature Riemannian Hypergraph (MRieHy), a framework tailor...

---

### 7. A Control-Theoretic Formulation of Global Workspace Theory

**Authors:** Ryota Kanai

**Published:** 2026-08-16

🔗 [Paper](http://arxiv.org/abs/2608.15926v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15926v1)

**Summary:** Global workspace theory explains conscious access as the broadcasting of selected information to the rest of the network, but it lacks a formal criterion for identifying the mechanism that enables this access. We propose that a global workspace is a mediator, namely, a subnetwork that receives activity from distributed systems, transforms it through internal modes, and returns differentiated effects to the broader network. We formalize this claim as the Global Mediation Workspace (GMW), a contro...

---

### 8. The effect of the excitatory feedback in anticipated synchronization and phase bistability regimes in neuronal populations

**Authors:** Julio N. Machado, Joana M. G. L. Silva, Katiele V. Brito, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15449v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15449v1)

**Summary:** Anticipated synchronization (AS), in which the receiver leads the sender and the phase lag is negative, can emerge in unidirectionally coupled dynamical systems when the receiver has faster internal dynamics than the sender. In cortical-like population models, AS and bistability between AS and delayed synchronization (DS) have been reported mainly in unidirectional motifs and have been proposed as possible explanations for phase relations observed in electrophysiological recordings. Because cort...

---

### 9. Head Impact Characterization and Cellular Response of a Live-neuron cell-integrated Biomechanical Full-body Surrogate Model

**Authors:** Raisa Akhtaruzzaman, Mohammad Ibrahim Hossain, Rahid Zaman, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15418v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15418v1)

**Summary:** In this study, we develop a novel integrated framework that links the impact response with cellular dynamics using a live-neuron cell-integrated biomechanical full-body surrogate model. The impact event is simulated by allowing the surrogate model to fall from controlled seated release angles of 30-degree, 60-degree, and 90-degree. Three vertically stacked cell-culture Petri dishes, each containing live SH-SY5Y neuroblastoma cells, were placed inside the head of a commercially available surrogat...

---

### 10. Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work

**Authors:** Yuyang Zheng, Nan Li, Wenxia Deng, et al.

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15193v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15193v1)

**Summary:** As large language model (LLM) agents are increasingly adopted in scientific research, external knowledge bases, knowledge graphs, and long-term memory have improved information retrieval and task continuity. However, most structured knowledge systems remain node-centric, representing files, concepts, results, and judgments as nodes and relations in a graph. While suitable for personal knowledge management, such structures often depend on individual organizational practices, limiting knowledge sh...

---

### 11. Phase- and amplitude-dependent control of synchronization in excitatory-inhibitory networks via pulsed stimulation

**Authors:** Ehsan Ahmadi, Mojtaba Madadi Asl, Alireza Valizadeh

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15081v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15081v1)

**Summary:** Oscillatory neuronal networks exhibit complex collective responses to external perturbations that depend on both the intrinsic network dynamics and the timing of stimulation. Although phase response curves (PRCs) have become a standard tool for characterizing these responses, phase resetting alone provides an incomplete description of how transient perturbations reshape collective activity. Here, we investigate the dynamics of a balanced excitatory-inhibitory network of exponential integrate-and...

---

### 12. Synaptic delays modulate population phase and amplitude responses in oscillatory excitatory-inhibitory networks

**Authors:** Parsa Shahab Rad, Mojtaba Madadi Asl, Alireza Valizadeh

**Published:** 2026-08-15

🔗 [Paper](http://arxiv.org/abs/2608.15077v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15077v1)

**Summary:** Synaptic delays are fundamental determinants of neuronal communication and can profoundly influence the emergence and stability of cortical oscillations. Although their role in shaping network synchronization is well established, how synaptic delays regulate the collective response of neuronal populations to transient perturbations remains poorly understood. Here, we investigate the effects of synaptic delays on the phase and amplitude responses of oscillatory activity in a conductance-based exc...

---

### 13. Data-driven techniques for translational neuroscience and personalized neuro-health

**Authors:** Vishal Subedi, Shashipraba N. K. Rajakaruna, Pratyusha Sarkar, et al.

**Published:** 2026-08-13

🔗 [Paper](http://arxiv.org/abs/2608.13749v1) | 📄 [PDF](https://arxiv.org/pdf/2608.13749v1)

**Summary:** Neurodegenexrative diseases such as Alzheimer's disease and Parkinson's disease are diagnosed most reliably only after substantial, often irreversible, neuronal loss has already occurred, creating an urgent need for quantitative tools that can detect subtle, early, and individual-specific brain changes from neuroimaging data. This review surveys a broad and rapidly evolving toolkit of data-driven techniques for translational neuroscience and personalized neuro-health, organized around four compl...

---

### 14. Activity-dependent epidemic spreading on multiscale brain networks predicts Alzheimer's disease progression

**Authors:** Christoffer G. Alexandersen, Suman S. Kulkarni, Jessica T. Davis, et al.

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.12647v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12647v1)

**Summary:** Neurodegenerative diseases can be viewed as spreading processes on brain networks, in which pathological proteins propagate between anatomically connected brain regions. Mathematical models have been used to study this process, but they generally ignore the influence of neuronal activity, even though experimental studies show that neuronal firing promotes protein transmission. Here, we couple a general node-activity process to susceptible--infected--susceptible dynamics. In this framework, an ep...

---

### 15. Testing the limits of past-adapted explanations by post-endpoint randomisation: anticipatory EEG as a worked case

**Authors:** George Sopasakis, Alexandros Sopasakis

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.12072v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12072v1)

**Summary:** A predictive model can fit its data even when its information set is insufficient; fit alone cannot establish sufficiency. This Perspective introduces Level II-A, a new design-based inference framework to test this distinction, illustrated in anticipatory EEG using contingent negative variation. A pre-event endpoint is committed before the delay to the imperative event is randomised. That later-assigned delay thereby becomes a negative-control probe of whether past-adapted information was suffic...

---

### 16. The Rosetta Stone and Levels of Principled Inference to the Experience of Another Mind

**Authors:** Kallum Robinson, Giulio Tononi, Naotsugu Tsuchiya, et al.

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.12030v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12030v1)

**Summary:** The classical problem of Other Minds has dogged philosophers for millennia; asking if we have any way to truly understand the experience of another mind. We know our own intrinsic experience by acquaintance, but can only ever hope to possess an extrinsic description of another's, with the two separated by an acquaintance gap. Structural approaches aim to characterise experience in terms of a mathematical structure, and promise a 'Rosetta Stone'; that is, a principled method to translate the cont...

---

### 17. Beyond Local Power: Functional Connectivity Analysis for Subject-Independent Learning Style Recognition

**Authors:** Wiga Maulana Baihaqi, Indriana Hidayah, Sri Kusrohmaniah, et al.

**Published:** 2026-08-12

🔗 [Paper](http://arxiv.org/abs/2608.12000v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12000v1)

**Summary:** Identifying individual learning styles optimizes pedagogical efficacy. While traditional questionnaires are structured, behavioral tracking methods require prolonged interaction log accumulation. To overcome these temporal constraints, this paper proposes an objective Electroencephalography (EEG) approach evaluating Phase Locking Value (PLV) connectivity against localized features across the Active-Reflective (AR) and Verbal-Visual (VV) Felder-Silverman dimensions. EEG signals were recorded from...

---

### 18. Conflict and Congruency Effects in Large Language Models: In-Weight and In-Context Competition in a Verbal Conflict Task

**Authors:** Xiaoyang Hu, Mike Angstadt, Shane Storks, et al.

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.11510v1) | 📄 [PDF](https://arxiv.org/pdf/2608.11510v1)

**Summary:** Congruency effects, observed in conflict tasks such as Stroop and flanker tasks, have been investigated for nearly a century in psychology and neuroscience, but their mechanistic basis is not fully understood. We introduce a verbal-only LLM conflict task in which a prompt stem elicits a default same-color completion and an explicit rule either agrees with (congruent condition) or conflicts with (incongruent condition) the completion. Gemma-2-2B and six Pythia models ranging from 410M to 12B para...

---

### 19. Consciousness as Intrinsic Structure: Towards a Chemistry of Experience

**Authors:** Matteo Grasso, Jeremiah Hendren, Giulio Tononi

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.11398v1) | 📄 [PDF](https://arxiv.org/pdf/2608.11398v1)

**Summary:** To be conscious is to have an experience - not a collection of phenomenal atoms, but a structured whole composed of distinctions and the relations that bind them. Integrated Information Theory (IIT) identifies the essential properties of every experience (axioms), formulates them operationally as postulates that a substrate must satisfy, and unfolds the cause-effect power of the resulting complex into a $Φ$-structure. Accounting for a content of experience is then a matter of identifying the phe...

---

### 20. A class of mean-field models to bridge molecular to brain scales

**Authors:** Alain Destexhe

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.11185v1) | 📄 [PDF](https://arxiv.org/pdf/2608.11185v1)

**Summary:** Predicting how molecular changes affect large-scale brain activity is a difficult task because of the lack of appropriate methods to link scales. In this perspective, we review a class of mean-field models that can integrate biophysical details such as synaptic receptors or membrane ion channels. This leads to a multi-scale modeling approach that can be used to evaluate how microscopic changes can impact macroscopic brain activity. This approach is illustrated here for the case of anesthesia, wh...

---

### 21. Evaluation Resolution Confounds Learning-Rule Comparisons in Model-Brain RSA of Early Visual Cortex

**Authors:** Nils Leutenegger

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.12408v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12408v1)

**Summary:** Representational similarity analysis (RSA) is increasingly used to ask which learning rules give convolutional networks brain-like representations. Because biologically plausible rules such as feedback alignment, predictive coding and STDP do not scale, studies that include them train small networks on small images (typically 32x32 CIFAR) and then compare them to brain responses modeled at much higher resolution. We find that a common result in this setting, that untrained or locally trained net...

---

### 22. Modeling and Interpreting Correlations, Null Distributions and Significance Levels in Neural Tracking of Natural Stimuli

**Authors:** Simon Geirnaert, Alexander Bertrand, Tom Francart, et al.

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.10887v1) | 📄 [PDF](https://arxiv.org/pdf/2608.10887v1)

**Summary:** Neural tracking - the time-locking of neural responses to continuous stimuli such as speech, music, and video - is widely used to study how the brain processes natural input. Tracking strength is typically quantified as the correlation between the recorded neural response and the stimulus, decoded and/or encoded through data-driven models, and this correlation is routinely used to compare stimulus features, models, or settings. However, its magnitude depends not only on how strongly the brain tr...

---

### 23. How many labels can a biological oscillator carry? A quality-factor screen for proposed information carriers

**Authors:** Eran Kopel

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.10560v2) | 📄 [PDF](https://arxiv.org/pdf/2608.10560v2)

**Summary:** How many distinguishable labels can a biological oscillator carry? Proposals invoking collective vibrational modes, endogenous electromagnetic fields, microtubule excitations and oscillatory phase codes are each debated on grounds particular to themselves, with no shared standard for comparison. We show that spectral distinguishability alone bounds the number of labels by the quality factor, M <= Q = 2 pi nu tau. This follows from the relation between linewidth and coherence time, so it is indep...

---

### 24. Improved cross-validated distances for multivariate pattern analysis

**Authors:** Laurent Caplette, Sarah Lippé

**Published:** 2026-08-11

🔗 [Paper](http://arxiv.org/abs/2608.10394v1) | 📄 [PDF](https://arxiv.org/pdf/2608.10394v1)

**Summary:** Characterizing the dissimilarity of neural representations between experimental conditions, and tracking it across time, is a central goal of multivariate pattern analysis. Guggenmos et al. (2018) assessed the reliability of many of the measures that can be used for that purpose on MEG data and recommended the use of either the cross-validated Euclidean distance or the within-class-corrected Pearson distance. In this commentary, we show that we can improve upon these distances. First, we show th...

---

### 25. Reduced Gibbs free energy supply hinders brain information processing during mental fatigue

**Authors:** Danko D. Georgiev, Oskan B. Tasinov, Danail V. Pavlov, et al.

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.10211v1) | 📄 [PDF](https://arxiv.org/pdf/2608.10211v1)

**Summary:** Background: Brain information processing deteriorates as cortical neurons gradually transition from a rested state into fatigue. Subjectively, fatigue is experienced as a state of weariness, tiredness, or lack of energy that reduces the ability to work safely and effectively. Objective: In this theoretical paper, we pinpoint the physical origin of brain fatigue in the gradual deterioration of biochemical reaction quotients and transmembrane ion concentration gradients, which increase neuronal ex...

---

### 26. Graph Analysis of Neuronal-Culture Connectivity Derived from a Reservoir-Computing Model

**Authors:** Ilya Auslender, Giorgio Letti, Yasaman Heydari, et al.

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.09773v1) | 📄 [PDF](https://arxiv.org/pdf/2608.09773v1)

**Summary:** Graph-theoretical analysis offers a principled framework for quantifying emergent dynamics in neuronal cultures. Here, we present an analytical pipeline for inferring network-level properties of in vitro cortical cultures from multichannel electrophysiological recordings. The approach builds on a recently proposed Reservoir Computing (RC) framework (Auslender et al., 2025), which enables direct extraction of an Intrinsic Connectivity Map (ICM) from neural activity. We interpret the ICM as an eff...

---

### 27. Reading Cognition as Decisions Unfold in Words: A Factorized Inverse Decision Model

**Authors:** Jiawen Kang, Dongrui Han, Xixin Wu, et al.

**Published:** 2026-08-10

🔗 [Paper](http://arxiv.org/abs/2608.09222v1) | 📄 [PDF](https://arxiv.org/pdf/2608.09222v1)

**Summary:** Inverse decision modeling infers latent properties of decision processes from observed behavior, but existing formulations rely primarily on action trajectories. In verbalized cognitive tasks, task execution also produces response dynamics that action-only formulations leave unmodeled, such as verbal production, interaction, and hesitation. We propose a factorized inverse decision model (FIDM) that decomposes each individual's task-execution likelihood into an action factor and an effort factor,...

---

### 28. Sensorimotor features of a reversal learning task bias decision behavior without disrupting individual difference structure

**Authors:** Elliot Huang, William Xu, Robert C. Wilson

**Published:** 2026-08-08

🔗 [Paper](http://arxiv.org/abs/2608.08206v1) | 📄 [PDF](https://arxiv.org/pdf/2608.08206v1)

**Summary:** In computational psychiatry, task-irrelevant factors such as a task's perceptual and motor features are typically assumed not to bias decision behavior, but at most to add noise. Yet growing evidence links sensorimotor processing to decision-making through multiple pathways, challenging this assumption. We tested this directly using a two-choice probabilistic reversal learning task completed by 90 participants under two sensorimotor conditions: a stationary condition requiring only arm movements...

---

### 29. A Hierarchical Energy-Based Model for Multimodal Cognition

**Authors:** Subir Varma

**Published:** 2026-08-08

🔗 [Paper](http://arxiv.org/abs/2608.12398v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12398v1)

**Summary:** We propose IM-LEPP (Integrated Multimodal Latent Energy-based Predictive Processing), a hierarchical, energy-based model of multimodal cognition that extends a previously proposed single-modality model (LEPP) to integrate vision and language. Following the view that generative neural networks are effective theories of cognitive dynamics, analogous to how statistical mechanics relates to thermodynamics, IM-LEPP models cognition as latent states flowing through learned energy landscapes rather tha...

---

### 30. FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity

**Authors:** Deepank Girish, Yi Hao Chan, Yubin Zheng, et al.

**Published:** 2026-08-07

🔗 [Paper](http://arxiv.org/abs/2608.07393v1) | 📄 [PDF](https://arxiv.org/pdf/2608.07393v1)

**Summary:** Functional Magnetic Resonance Imaging ( fMRI ) data are often pooled into collaborative multi-site consortia, as deep learning models for analyses require large datasets to generalize well. While Federated Learning (FL) offers a privacy-preserving paradigm for collaborative training, standard approaches continue to struggle with statistical heterogeneity. In particular, site differences pose a key challenge in multi-site data settings. Additionally, existing FL approaches for fMRI rely on static...

---

### 31. International Transfer of Stochastic Cortical Self-Reconstruction

**Authors:** Fabian Bongratz, Zhizheng Zhuo, Chao Zhang, et al.

**Published:** 2026-08-07

🔗 [Paper](http://arxiv.org/abs/2608.07092v1) | 📄 [PDF](https://arxiv.org/pdf/2608.07092v1)

**Summary:** Stochastic cortical self-reconstruction (SCSR) enables personalized mapping of gray matter atrophy, a hallmark of neurodegenerative disorders such as Alzheimer's disease (AD), onto high-resolution cortical surfaces. Unlike conventional normative modeling approaches, which typically operate at a coarse regional level and remain inherently constrained by the covariates included during training, SCSR estimates an individualized healthy reference directly from the observed cortical thickness at the ...

---

### 32. Zenons Demon and the Denial of Domain-Generality for Transformer-Based Computational Models of Human Behavior

**Authors:** Mark Orr, Edward A. Cranford, Ken Ford, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.12396v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12396v1)

**Summary:** Transformer-based models of human behavior (e.g., the Centaur model by Binz, et al., 2025) posit to be domain general computational models of human behavior. The claim of domain-generality is by virtue of the supposed capability to predict and simulate human behavior across a vast range of cognitive and perceptual domains. Further, it is argued that this degree of performance places such models on a path toward general, unified theories of cognition (Newell, 1990). We contest this characterizati...

---

### 33. Errorless Irrationality: A unified computational account of the inverse base-rate effect across predictive, observational, and unsupervised procedures

**Authors:** Lenard Dome, Andy J. Wills

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.06149v1) | 📄 [PDF](https://arxiv.org/pdf/2608.06149v1)

**Summary:** The inverse base-rate effect is a robust bias in how people resolve ambiguity between competing categories, and the most prominent theories explain it through prediction error. Across two experiments we progressively removed the elements of the predictive-learning design that supply such error signals: first by moving to observational learning, then to an unsupervised procedure in which category labels were not presented. The effect persisted--the irrational bias is independent of supervised lea...

---

### 34. Convergent Evolution in Neural Representation Space: Emergent Order in Deep Belief Networks

**Authors:** Patrick Krauss, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05996v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05996v1)

**Summary:** Deep Belief Networks (DBNs) learn hierarchical generative models without class supervision. Here, we ask whether this purely unsupervised process nevertheless organizes internal representations according to the unknown data classes. We analyze successive layers of DBNs trained on MNIST, Fashion-MNIST, and KMNIST using the Generalized Discrimination Value (GDV), supervised probes applied only after training, a reconstruction-based measure of abstraction distance, effective dimensionality, and fre...

---

### 35. Convergent Evolution in Algorithmic Space

**Authors:** Patrick Krauss, Achim Schilling, Andreas Maier, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05985v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05985v1)

**Summary:** In evolutionary biology, unrelated organisms can independently evolve similar structures when exposed to similar functional demands. Here we ask whether an analogous form of convergent evolution occurs during neural network training: do networks with different random initializations develop similar internal weight structures when trained on the same task? This question is technically nontrivial because hidden neurons can be arbitrarily permuted without changing the represented function, making d...

---

### 36. Complexity and Stability of Neural Activity Across Aging and Neurodegenerative Disease

**Authors:** Junjie Yu, Jianyu Zhang, Zian Pei, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05882v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05882v1)

**Summary:** Objective: EEG signals fluctuate continuously even within a fixed cognitive state, but an important question is whether the brain still reuses similar activity patterns to represent information over time. Methods: To address this, we model EEG as distributions of windowed activity patterns and quantify their temporal stability using Wasserstein distance, while intrinsic dimensionality captures representational complexity. Results: Across multi-task, lifespan, and clinical EEG datasets, we find t...

---

### 37. Two base rates, two weights: base-rate neglect has a second axis

**Authors:** Adam Y. Shavit

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05658v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05658v1)

**Summary:** Base-rate neglect is usually treated as one mistake: giving the prior too little weight. Turning the co-occurrences you see into a useful judgment, though, means correcting for two base rates, not one. The first is the familiar prior, how common the outcome is. The second is how common the cue itself is. Those are two separate mistakes, and a learner can make either one alone. Under-correcting the prior is classical base-rate neglect; under-correcting the cue is the cue-density effect of conting...

---

### 38. Transcutaneous Spinal Cord Stimulation Disrupts Conscious Ankle Proprioception and Produces a More Constrained Locomotor Pattern in Unimpaired Adults

**Authors:** Christopher A. Johnson, Andria J. Farrens, Parastoo Ali Pour, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05635v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05635v1)

**Summary:** Transcutaneous spinal cord stimulation (tSCS) modulates spinal sensorimotor circuits primarily through activation of afferent networks. While prior work has emphasized locomotor performance and spinal excitability, how tSCS affects conscious proprioceptive perception and the extent to which such effects parallel changes in locomotor control remain unclear. We investigated the acute and training-related effects of tSCS on ankle proprioception and gait in unimpaired adults (n = 14), with an indepe...

---

### 39. From Local Learning to Global Prediction Through Layered Surprise Cascades

**Authors:** Andrew L. Smith, Linxing Preston Jiang, Jason K. Eshraghian, et al.

**Published:** 2026-08-06

🔗 [Paper](http://arxiv.org/abs/2608.05481v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05481v1)

**Summary:** Hierarchical predictive coding proposes a compelling hypothesis of brain computation, suggesting that the cortex builds layered predictions to minimize surprise. Yet most models rely on error-coding neurons or generative modeling of unclear biological plausibility. Here, we examine a biologically plausible framework in which the functional goals of predictive coding emerge from local contrastive learning and simple activity cancellation. Building on recent machine learning advances, we present a...

---

### 40. Effective pruning of task-trained recurrent neural networks using noisy fluctuations and connection rescaling

**Authors:** Sanjith Senthil, Rishidev Chaudhuri

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05464v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05464v1)

**Summary:** The pruning of network connections is key to brain function but, despite its importance, there exist few biologically-plausible pruning rules with demonstrated good performance. In this work we evaluate noise-prune, a recently introduced unsupervised local pruning rule for recurrent networks that uses noisy fluctuations to determine the importance of connections. Noise-prune has previously only been empirically tested on random networks without a specific computational function. We show that noi...

---

### 41. Toward a Dynamical Taxonomy of Insomnia: A Multiaxial Framework for Sleep-State Transitions and Architectural Failure

**Authors:** Alexander Poltorak

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05462v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05462v1)

**Summary:** Insomnia disorder is defined at the syndrome level, yet similar complaints can arise from different abnormalities in sleep regulation, state transition, state stabilization, spatial recruitment, architectural sequencing, and state perception. We propose a multiaxial dynamical framework whose principal contribution is organizational: a candidate profile is specified by the dynamical operation that fails, the sleep stage or boundary at which it fails, and its causal status. Objective sleep duratio...

---

### 42. The ethics of artificial intelligence in the life sciences: Universality, cultural diversity and an architecture of care

**Authors:** Jean-Pierre Changeux, Gustavo Deco, Morten L. Kringelbach

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.05436v1) | 📄 [PDF](https://arxiv.org/pdf/2608.05436v1)

**Summary:** The life sciences and health research have started to benefit from artificial intelligence, which raises ethical concerns that are real but, we argue, not special. Any science should be governed by values that rest on how the human brain is built and socialised rather than anything distinct to artificial intelligence. Importantly, the human brain has a different, much less costly computational architecture than these machines. This is achieved through the orchestration of a global neuronal works...

---

### 43. VR-IPS: Virtual Reality Tool for Photic Stimulation in Photosensitive Diagnosis

**Authors:** Fernando Moncada Martins, Daniel Pérez Prádanos, Angel Rio-Alvarez, et al.

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.12394v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12394v1)

**Summary:** Photosensitivity is a neurological condition in which the brain generates epileptiform activity in response to visual stimuli. The standardized clinical diagnosis procedure, named Intermitent Photic Stimulation (IPS), involves exposing patients to a white flashing light at different frequencies to provoke this reaction. However, clinical neurophysiologists report that this protocol is insufficient, leading to underdiagnosis. VR-IPS is a flexible visual stimulation tool that extends conventional ...

---

### 44. An entropic explanation of insistence on sameness in autism

**Authors:** Przemysław Śliwiński

**Published:** 2026-08-05

🔗 [Paper](http://arxiv.org/abs/2608.04616v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04616v1)

**Summary:** An information theory-based framework is proposed in attempt to explain insistence on sameness in autism as an instance of a general behavior pattern in which an individual tries to reduce surprise and uncertainty. It offers a new definition of autism as an impairment in which cognitive functions are restricted to discrimination, memorization and prediction of tangible properties of the environment. An analogy between insistence on sameness and constrained minimization of the entropy metric is o...

---

### 45. Metacognitive Skill Learning: A Computational Account

**Authors:** Brendan Conway-Smith

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.12393v1) | 📄 [PDF](https://arxiv.org/pdf/2608.12393v1)

**Summary:** This dissertation presents the first formal theory of metacognitive skill learning. Metacognition, the capacity to monitor and control one's own cognitive processes, has been widely studied, yet the field still lacks a theoretical framework explaining how metacognitive abilities are learned. This gap limits progress in both theory and application across fields such as cognitive science, education, therapeutic practice, and artificial intelligence. The account developed here builds on classic mod...

---

### 46. Time^2: A framework for the neural dynamics of visual perception

**Authors:** Laurent Caplette, Frédéric Gosselin

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.04218v1) | 📄 [PDF](https://arxiv.org/pdf/2608.04218v1)

**Summary:** Whenever we look at an object, we seem to perceive it immediately. However, this is not the case for two reasons. First, it takes hundreds of milliseconds for the brain to process visual information reaching the retina. Second, we have to look at an object for a certain amount of time to perceive it (and we typically look at it for hundreds of milliseconds) -- during that time, visual information is continuously received on our retinas. These facts together imply that visual information is both ...

---

### 47. Persistent homology broadens the controllable subspace in human structural connectomes

**Authors:** Carter Sale, Marco Coraggio, Mengsen Zhang, et al.

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03181v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03181v1)

**Summary:** Network control theory applied to structural connectomes typically ranks brain regions as candidate driver nodes by their structural connectivity strength, and evaluates performance through scalar control energy. We test whether this framing captures the most relevant information about how driver-node selection shapes brain network control. We introduce an alternative criterion based on the persistent topological cycles in which each node participates---a measure of mesoscale integration that ca...

---

### 48. A Landau-Ginzburg Phenomenology of Sleep-Stage Transitions

**Authors:** Alexander Poltorak

**Published:** 2026-08-04

🔗 [Paper](http://arxiv.org/abs/2608.03000v1) | 📄 [PDF](https://arxiv.org/pdf/2608.03000v1)

**Summary:** Sleep staging provides a reproducible clinical description, but it does not by itself explain why some boundaries are abrupt while others are graded, or why transition windows contain instability, synchrony, and apparent state coexistence. We develop a local Landau-Ginzburg phenomenology in which each boundary is represented by motion in an effective potential of a spatially extended, noisy, dissipative neural field. A latent cortical-ordering coordinate phi is inferred from prespecified EEG/PSG...

---

### 49. Modelling temporal dynamics of suicidal ideation and behaviour across pre- to early adolescence using a Markov framework

**Authors:** Sieun Lee, Ben Cardoen, Marianne Etherson, et al.

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02896v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02896v1)

**Summary:** Understanding the dynamics of suicidal ideation and behaviour in youth and the factors associated with transitions from thoughts to behaviours is critical for early identification, monitoring, and prevention. Using longitudinal self-report data from the Adolescent Brain Cognitive Development (ABCD) Study (n = 11,864) spanning ages 9 to 13 years, we developed a time-inhomogeneous discrete-time Markov chain framework to model transitions across eight states defined by suicidal ideation and behavio...

---

### 50. Detecting high-frequency brain disorder signals using dynamic mode decomposition from EEG

**Authors:** Jacob Kang, Jong-Hyeon Seo

**Published:** 2026-08-03

🔗 [Paper](http://arxiv.org/abs/2608.02804v1) | 📄 [PDF](https://arxiv.org/pdf/2608.02804v1)

**Summary:** Recent studies have reported clearly identifiable dynamical changes in the high-frequency range of EEG signals recorded during specific stimuli, such as visual or auditory inputs, or in cases of brain disorders like epileptic seizures. In this study, we utilized Dynamic Mode Decomposition (DMD) to extract consistent and persistent dynamical changes in the high-frequency band from the signals of neurologically relevant EEG channels. High-frequency DMD modes were employed as features, composing a ...

---

## stat.ML

**50 papers**

### 1. Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions

**Authors:** Tomasz R. Bielecki, Thibaut Mastrolia, Haoze Yan

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19151v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19151v1)

**Summary:** We study stochastic control of multivariate Hawkes-driven stochastic differential equations with machine learning algorithms in a non-Markovian setting. Due to the path dependence of the memory of the Hawkes intensity, this problem does not fall within classical stochastic control theory outside particular Markovian kernels. We first develop a finite-dimensional Markovianization procedure and algorithm to approximate multivariate Hawkes processes with mixtures of exponential kernels. We prove th...

---

### 2. Learning Random Geometric Graphs Drawn in Probabilistic Metric Spaces

**Authors:** Dalia Chakrabarty, Kangrui Wang, Chuqiao Zhang, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19082v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19082v1)

**Summary:** We present a new data-driven learning of a Random Geometric Graph (RGG) of a multivariate dataset, where the graph is drawn in a probabilistic metric space. This graph learning works for generic datasets, irrespective of the type of the observables; their probability distributions; or size of the data. We identify a metric of the space that the graph is drawn in, as a probability distribution of a random variable that we introduce, namely, a variable that represents the disparity between the con...

---

### 3. Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk

**Authors:** Deep Kumar Ganguly, Jan Křetínský

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19073v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19073v1)

**Summary:** An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a robust-optimization identity---a confidence level fixes the radius of a relative-entropy ball of alternative models---but that ball cannot reach catastrophes the nominal deems impossible, precisely what a safe agent must hedge. We instead use an optimal-transport ball and study the coherent risk measure it induces, the Wasserstein entropic value-at...

---

### 4. Function-On-Function Regression Through Separable Neural Operators

**Authors:** Tailen Hsing, Su-Yun Huang, Toshinari Morimoto

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19070v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19070v1)

**Summary:** This paper investigates the estimation of the regression operator in function-on-function regression models. While traditional research has predominantly focused on linear models or their immediate nonlinear extensions, we propose a neural operator approach to accommodate general regression operators under mild smoothness assumptions. Operator learning has emerged as an active area of machine learning, particularly for solving physical models governed by partial differential equations. Using thi...

---

### 5. Diffusion Models for High-Dimensional Clustered Data: Intrinsic-Dimension Adaptivity via Bayesian Classification

**Authors:** Yuga Iguchi, Paul Fearnhead

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19067v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19067v1)

**Summary:** The empirical success of diffusion models in generative modelling has motivated theoretical work, including quantitative error bounds and qualitative analyses that characterise the different phases of denoising. We bring these two areas together by studying the adaptivity of diffusion models to the structured geometry of multimodal high-dimensional data that consists of multiple clusters in $\mathbb{R}^D$, each with its own low-dimensional structure, and inter-cluster separation depending on $D$...

---

### 6. Scalable Amortized Variational Inference for Non-Poisson Buy-'Til-You-Die Models

**Authors:** Sulagna Ghosh, Aaron Schein

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.19022v1) | 📄 [PDF](https://arxiv.org/pdf/2608.19022v1)

**Summary:** Despite the wide variety of existing Buy-`Til-You-Die (BTYD) models, nearly all rely upon the convenient assumption of transactions following a Poisson process. As modern customer bases grow larger and more diverse, a major gap in the marketing literature is BTYD models that can account for heterogeneity in timing patterns across millions of customers. This paper addresses that gap, introducing a family of models that assume transactions follow a Weibull renewal process and developing a highly s...

---

### 7. Sharper Regret Bounds for Time-Varying Gaussian Process Bandits with Constant Exploration

**Authors:** Matthias Mandl, Hanne Kekkonen

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18863v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18863v1)

**Summary:** We study Bayesian optimization in a time-varying environment where the unknown reward function evolves according to a Gaussian process drift model. Existing GP-UCB analyses in this setting typically require the exploration parameter to grow with the horizon to maintain uniform confidence bounds. Using per-round local confidence events, we show that GP-UCB can instead be run with a constant exploration parameter and obtain an expected-regret bound whose coefficient depends on the drift rate. We a...

---

### 8. GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models

**Authors:** Qi Qin, Jiajie Zhu, Dali Chen, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18849v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18849v1)

**Summary:** Tabular foundation models (TFMs) achieve strong performance through in-context learning, but context-dependent inference imposes substantial latency and memory costs, hindering large-scale deployment. We propose GEAR (\emph{Generative Expansion and Real Anchoring}), a modular two-stage framework that distills TFMs into lightweight MLP or tree-based predictors that can be deployed on commodity CPUs. Stage 1 uses synthetic covariates solely as teacher-query locations and trains the student on soft...

---

### 9. A Unifying Relational Perspective on Expressive Lottery Tickets

**Authors:** Lorenz Kummer, Samir Moustafa, Anatol Ehrlich, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18819v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18819v1)

**Summary:** Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is poorly understood. The Strong Expressive Lottery Ticket Hypothesis (SELTH) posits the existence of sparse GNNs that preserve Weisfeiler-Leman (WL) expressivity on static graphs. We generalize this existence result to a probabilistic statement for multi-relational and temporal domains via the relational WL (RWL). We prove that sufficiently parame...

---

### 10. ProxyGuard: Direct Reliability Inference for Randomized Data Release Mechanisms with Shared Targets

**Authors:** Dipesh Tharu Mahato, Pramod Dhungana

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18643v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18643v1)

**Summary:** Researchers often choose a proxy dataset from many releases, transformations, or seeds. Search can make an invalid release appear adequate, while one adequate release does not establish that its generator is reliable. ProxyGuard controls both errors using prespecified bounded risks and a sealed target set. Named-release mode corrects for multiplicity and certifies specific releases. Direct shared-target mode evaluates independent mechanism draws on a common target, lower-bounds their favorable-s...

---

### 11. Multi-Level Bayesian Calibration of a Multi-Component Dynamic System Model

**Authors:** Berkcan Kapusuzoglu, Sankaran Mahadevan, Shunsaku Matsumoto, et al.

**Published:** 2026-08-19

🔗 [Paper](http://arxiv.org/abs/2608.18430v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18430v1)

**Summary:** This paper proposes a multi-level Bayesian calibration approach that fuses information from heterogeneous sources and accounts for uncertainties in modeling and measurements for time-dependent multi-component systems. The developed methodology has two elements: quantifying the uncertainty at component and system levels, by fusing all available information, and corrected model prediction. A multi-level Bayesian calibration approach is developed to estimate component-level and system-level paramet...

---

### 12. Inference and Uncertainty Quantification for Streaming $r$-PCA

**Authors:** Haoshu Xu, Hongzhe Li

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18374v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18374v1)

**Summary:** We address two open questions in streaming PCA via Oja's algorithm: sharp operator-norm convergence for general rank under sub-Gaussian data, and distributional inference for the resulting subspace estimator. Existing convergence analyses, even in the rank-one case, either assume bounded data or leave non-vanishing remainder terms that prevent adaptation to a polynomially vanishing tail spectrum, while existing distributional results are confined to the rank-one case. Our convergence theory remo...

---

### 13. Debiased Inference for AI-Generated Data without Gold-Standard Labels: Identification via Multiple Imperfect Measurements

**Authors:** Naoki Egami, Sooahn Shin

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18294v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18294v1)

**Summary:** An increasing number of scholars use AI to measure variables they subsequently include in downstream analyses. Although AI-measured variables are often analyzed as if observed without error, ignoring prediction errors in automated measurement leads to substantial bias and invalid confidence intervals in downstream analyses, even if AI measurement accuracy is high, e.g., above 90%. Existing solutions, such as design-based supervised learning and prediction-powered inference, combine error-prone A...

---

### 14. SIGMA: Symmetry-aware, Intelligent, Geometric, Multi-objective Adaptive Control for Robust, Dependable Traffic Management

**Authors:** Pratham Payra, Jagadish B, Tanmay Sen, et al.

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18263v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18263v1)

**Summary:** Traffic signal control is a complex sequential decision-making problem requiring real-time adaptation and trade-offs among throughput, delay fairness, signal stability, and emergency vehicle priority. Existing RL methods often fix objectives, ignore dynamic priority changes, and fail to generalize across geometrically similar intersections.We propose SIGMA (Symmetry-aware, Intelligent, Geometric, Multi-objective Adaptive traffic control), an RL framework enhanced with a large language model (LLM...

---

### 15. Sobolev Regularized Score Difference Estimation in Diffusion Models

**Authors:** Chenghan Xie, Jose Blanchet, Renyuan Xu

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18237v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18237v1)

**Summary:** Estimating the difference of two Stein's score functions is a fundamental problem in generative modeling. In particular, score differences arise naturally in transfer learning, where the score difference provides the mechanism for adapting a pre-trained model to a new target distribution, and in diffusion model-based post-training methods such as discriminator guidance. Existing estimators for score differences in these settings either lack of statistical consistency or are difficult to scale up...

---

### 16. Where A Small Language Model Helps in Invoice Categorisation, Understood Through Embedding Geometry

**Authors:** Emma Ceccherini, Daniel Lawson, Anjulika Salhan

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18033v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18033v1)

**Summary:** Categorising invoices into the correct General Ledger (GL) code underpins financial reporting and tax compliance. This is a skilled accounting judgement rather than a routine task: the correct category depends subtly on the nature of the purchasing business, the vendor and the invoice text. Whilst AI is increasingly being adopted across industries to automate tasks, including invoice categorisation, implementations built on in-house small language models (SLMs) can simultaneously reduce cost and...

---

### 17. An RKHS Framework for Fixed Effects in Permanental Process Models

**Authors:** Matthew LeDuc

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17908v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17908v1)

**Summary:** This short work describes an extension of the permanental process model which includes fixed effects. By starting with a prior on the fixed effects coefficients we show that, in the diffuse prior limit, the intensity function of the permanental process can be found using the representer theorem and naturally decomposed into a fixed effects term and a function which is an element of a Reproducing Kernel Hilbert Space (RKHS). We show that the limiting equivalent kernel defines an RKHS whose square...

---

### 18. Toward the Optimal Regret-Instability Trade-off in Multi-Armed Bandits

**Authors:** Kaifei Wang, Yinyu Ye, Han Zhong

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17841v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17841v1)

**Summary:** Multi-armed bandit algorithms are evaluated by regret, yet comparable regret can coexist with different allocations across independent runs. We study the trade-off between worst-case regret $\mathcal{R}_{K,T}$ and instability $\mathcal S_{K,T}$, defined as the largest standard deviation of a terminal pull count, for $K$ arms and $T$ rounds. We prove the finite-time lower bound $\mathcal R_{K,T}\mathcal S_{K,T}\ge C T^{3/2}$, where $C$ is independent of $K$ and $T$, under a finite-time regret con...

---

### 19. Spatially explicit feature importance for building height estimation using research-access high-resolution SAR and optical sensors

**Authors:** Guilherme Iablonovski, Pierre-Louis Frison, Tatiana Silva da Silva

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17822v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17822v1)

**Summary:** Accurate building height information at the individual footprint scale is essential for material stock accounting and post-disaster damage assessments yet remains difficult to obtain at city scale in the Global South where airborne LiDAR coverage is rare and commercial very high-resolution imagery is cost-prohibitive or unavailable. While recent works have demonstrated building height estimation using freely available Sentinel imagery, the resolution ceiling of resulting products is still coarse...

---

### 20. Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See

**Authors:** Ayoub Kirouane, Christos Petrocheilos

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17744v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17744v1)

**Summary:** Take three frontier mixture-of-experts models (Alibaba, OpenAI, NVIDIA; 3.6-4.0B active parameters each) and fine-tune them to reason in a low-resource language. On accuracy benchmarks almost nothing happens, and the benchmark itself is noise at this scale: changing only the random seed moves the score by 7.7 points, more than every data and recipe effect we measured. That null is our first result. The real changes live where accuracy cannot see. Base models never think in Greek: 0 of 1,000 reas...

---

### 21. VERaiPHY -- Validation & Evaluation for Robust AI in PHYsics

**Authors:** Gaia Grosso, Ramon Winterhalder, Lydia Brenner, et al.

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17724v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17724v1)

**Summary:** Modern machine learning is leading to substantial gains in precision, flexibility, and computational efficiency in fundamental physics. Statistical validation, uncertainty quantification, and robustness assessment are less systematically addressed. The VERaiPHY initiative (Validation & Evaluation for Robust AI in PHYsics) is a series of articles developed within the PHYSTAT programme, aimed at establishing statistical standards for the development, evaluation, and deployment of ML techniques. Ea...

---

### 22. Modified Bryson-Frazier Smoothing and Hyperparameter Learning for Temporal Gaussian Process Regression

**Authors:** Tom Colemont, Brecht Evens, Tjonnie G. F. Li, et al.

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17595v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17595v1)

**Summary:** One-dimensional Gaussian processes with stationary, integrable kernel functions admit exact or arbitrarily accurate state-space representations, enabling linear-time inference through Kalman filtering and Rauch-Tung-Striebel (RTS) smoothing. However, the RTS smoother requires inversion of predicted state covariance matrices, which can become ill-conditioned and may therefore lead to numerical instabilities. In this work, we revisit the modified Bryson-Frazier (MBF) smoother as an alternative to ...

---

### 23. Feature Priming in Online Linear Regression: Sparse-Regret Lower Bounds and a Tight Univariate Rate

**Authors:** Huibo Xu, Shi Fu, Qixin Zhang, et al.

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17573v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17573v1)

**Summary:** In high-dimensional online prediction, the best predictor may depend on only a few features, so regret should scale with sparsity rather than the ambient dimension. Feature priming pursues this goal by estimating feature weights from past data and refitting a minimum-norm predictor on the rescaled design. Warmuth and Amid asked at COLT 2023 whether any of three such rules admits a competitive online regret guarantee. Using the natural Moore--Penrose protocol based only on past data, we give a ne...

---

### 24. Regularization of Statistical Inverse Problems on Non-Reflexive Banach Spaces

**Authors:** Darrel K Joseph, M P Rajan

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17533v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17533v1)

**Summary:** Inverse learning within a statistical framework has a wide range of applications. It has garnered significant attention in machine learning, artificial intelligence, and related fields, where the goal is to infer unknown parameters from indirect and noisy observations. This work investigates the stable approximation of $u^{\dagger}$ which solves the equation $Au=g$, with $A$ being a linear operator between appropriate vector spaces. We will consider the domain to be a non-reflexive Banach Space ...

---

### 25. Online Generalized Sparse Regression: How Does Overparametrization Help?

**Authors:** Shuoguang Yang, Qiang Sun

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17466v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17466v1)

**Summary:** Regularized sparse regression has been extensively studied in the offline setting, but online formulation remains relatively under-explored. This gap stems from four key challenges: (i) the infeasibility of dynamically updating the regularization parameter in every online round, (ii) managing storage and memory complexity, (iii) enabling real-time computation via closed-form updates rather than solving full optimization problems at each round, and (iv) achieving optimal statistical guarantees un...

---

### 26. Nonlocal Transition Kernel for Efficient Learning of Restricted Boltzmann Machines

**Authors:** Kaiji Sekimoto, Muneki Yasuda

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17450v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17450v1)

**Summary:** Learning restricted Boltzmann machines (RBMs) is computationally challenging because it requires expectations whose exact evaluation is generally intractable. The expectations are typically evaluated using a sampling approximation based on blocked Gibbs sampling (BGS), which is a local Markov chain Monte Carlo transition kernel. However, the locality of BGS can lead to poor sampling quality when the RBM has high energy barriers, thereby degrading learning performance. Deep tempering (DT), which ...

---

### 27. Tight Bounds for Data-driven Multiple Hyper-parameter Tuning with Structured Loss Function

**Authors:** Anh Tuan Nguyen, Viet Anh Nguyen

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17343v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17343v1)

**Summary:** Data-driven algorithm design frames hyperparameter tuning as a statistical learning problem, but establishing generalization guarantees remains challenging due to the implicit, non-smooth dependence of model performance on hyperparameters. Existing multi-dimensional bounds under piecewise-polynomial assumptions remain theoretically loose and lack comprehensive lower bounds. We resolve this by establishing tight pseudo-dimension bounds for multi-dimensional data-driven tuning. First, we refine th...

---

### 28. SPACE: Sample-cloud Predictive Adaptive Conformal Ellipsoids for Multivariate Time-Series Forecasting

**Authors:** Baishi Li, Kelvin J. L. Koa, Ke-Wei Huang

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17333v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17333v1)

**Summary:** Modern probabilistic time-series forecasters often express uncertainty through forecast samples. While typically converted into nominal prediction regions using empirical quantiles, these model-implied sets lack formal coverage guarantees and frequently deviate from nominal targets under distribution shift. Existing multivariate conformal methods can calibrate these regions online, but they typically estimate geometry from historical residuals using fixed or accumulating look-back windows. This ...

---

### 29. Fair Multi-View Determinantal Coresets via Adaptive NEPv

**Authors:** Richard Yi Da Xu

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.18181v1) | 📄 [PDF](https://arxiv.org/pdf/2608.18181v1)

**Summary:** Selecting a small, diverse subset from a large candidate pool often means balancing several incompatible notions of diversity. In trademark curation, for instance, a subset should cover both the language used to describe marks and the visual space of their logos. A single determinantal point process (\DPP) kernel can hide failure in one view, and averaging kernels replaces the multi-view relaxation by an ordinary single-kernel spectral problem. We formulate \emph{fair multi-view determinant sele...

---

### 30. Minimax Optimal Estimator and Improved Error Rate for the MLE in Logistic Regression with Gaussian Design

**Authors:** Junren Chen, Arya Mazumdar

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17260v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17260v1)

**Summary:** We study finite-sample parameter estimation in logistic regression with Gaussian design, where the goal is to estimate $\mathbfθ^*\in \mathbb{R}^d$ with $R=\|\mathbfθ^*\|_2\ge 1$ from i.i.d. samples $\{(\mathbf{x}_i,y_i)\}_{i=1}^n,$ $\mathbf{x}_i \sim N(0,\mathbf{I}_d)$, $y_i\mid \mathbf{x}_i \sim \mathrm{Bernoulli}((1+\exp(-\mathbf{x}_i^\top \mathbfθ^*))^{-1})$. In this paper, we provide the first minimax optimal estimator, and improve on the best known finite-sample error rate for the maximum ...

---

### 31. Adaptive surrogate modeling for high-dimensional spatio-temporal output

**Authors:** Berkcan Kapusuzoglu, Shunsaku Matsumoto, Yoshitomo Miyagi, et al.

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17250v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17250v1)

**Summary:** This paper develops an adaptive surrogate modeling method for problems with very high-dimensional spatio-temporal outputs. The analysis of spatio-temporal multi-physics systems is computationally expensive and consists of a large number of inputs and outputs. Surrogate models are often constructed to replace the physics-based model to achieve computational efficiency in analyses such as uncertainty quantification and optimization that require many function calls. In order to address the challeng...

---

### 32. Information fusion and machine learning for sensitivity analysis using physics knowledge and experimental data

**Authors:** Berkcan Kapusuzoglu, Sankaran Mahadevan

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17248v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17248v1)

**Summary:** When computational models (either physics-based or data-driven) are used for the sensitivity analysis of engineering systems, the sensitivity estimate is affected by the accuracy and uncertainty of the model. This paper considers global sensitivity analysis (GSA) for situations where both a physics-based model and experimental observations are available, and investigates physics-informed machine learning strategies to effectively combine the two sources of information in order to maximize the ac...

---

### 33. Maximum Tsallis Entropy Distributions for Robust and Efficient Sparse Learning from Correlated Data

**Authors:** Kai Yang, Masoud Asgharian, Celia M. T. Greenwood

**Published:** 2026-08-18

🔗 [Paper](http://arxiv.org/abs/2608.17244v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17244v1)

**Summary:** This paper addresses the limitations of Gaussian distribution assumptions in statistical sparse learning, particularly in modeling correlated and heterogeneous data. Conventional Gaussian models often lack robustness towards outliers and underlying distribution assumptions. To overcome these limitations, we propose the use of the $q$Gaussian distribution, derived from Tsallis entropy maximization, as a robust alternative. This is notably relevant in biostatistics, where the presence of correlate...

---

### 34. Expressivity In Multimodal Contrastive Learning

**Authors:** Andrew Stuart, Florian Wolf

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.17203v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17203v1)

**Summary:** Contrastive learning has become a cornerstone of modern representation learning, powering CLIP-style models that underpin text-to-image generation, vision-language models, and retrieval across a rapidly growing range of modalities. Despite this empirical success, the expressive power of these architectures remains poorly understood. To gain insight, we study expressivity by adopting a population-level, density-estimation viewpoint: each architecture comprises a parameterized set of densities who...

---

### 35. Policy Optimization and Statistical Inference for Online Contextual Matrix Games

**Authors:** Liner Xiang, Yixin Wang, Hengrui Cai

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.17173v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17173v1)

**Summary:** Online decision making often requires navigating a landscape shaped by both dynamic contexts and strategic interactions. In competitive pricing, for example, hotels must account for both dynamic contextual factors and rivals' strategic responses. Existing approaches address only part of this challenge: contextual bandits optimize single-agent decisions using observable features but ignore multi-player interactions, while online matrix games capture strategic behavior through Nash equilibrium but...

---

### 36. Expected free energy as an information constraint on the Bethe Lagrangian

**Authors:** Wouter M. Kouw

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.17167v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17167v1)

**Summary:** Active inference selects actions by minimising an expected free energy functional over predicted futures. However, adding an expectation over yet-unobserved outcomes means the free energy functional no longer has a Kullback-Leibler structure, which hinders message passing treatments of inference procedures. We propose an alternative formulation based on a Bethe free energy functional, fully supporting inference by message passing. The epistemic drive is maintained by imposing an information cons...

---

### 37. Causal Discovery in Equal Variance Linear Gaussian DAGs via SURE-Tuned Ridge Regression

**Authors:** Sambit Mishra, Urbashi Mitra

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.17132v1) | 📄 [PDF](https://arxiv.org/pdf/2608.17132v1)

**Summary:** Recovering the directed acyclic graph (DAG) of a structural equation model (SEM) from observational data is a central problem in causal discovery. The iterative gradient descent and per-problem hyperparameter tuning of continuous-optimization methods are poorly suited to two practically important regimes: the sample-limited regime, where the number of samples is comparable to or smaller than the number of nodes in the DAG, and the compute-limited regime. This work proposes SURE-Ridge, a non-iter...

---

### 38. Non-Crossing Deep Quantile Regression for Distributional Survival Prediction

**Authors:** Shuai Huang, Zhe Qu, Zhaowei Hua, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16864v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16864v1)

**Summary:** In survival analysis the way covariates act on the risk of an event often differs between early and late failure times, yet hazard- and mean-based summaries collapse this variation into a single number. Quantile-based modeling instead describes the full conditional distribution on the original time scale, but existing censored-data methods are either inflexible or produce logically inconsistent crossing quantile curves. We propose a Censored Non-crossing Quantile (CNQ) framework for right-censor...

---

### 39. Hide&Seek: Learning to Explain in an End-to-End Differentiable Network

**Authors:** Tal Ellinson, Hadi Mohasel Afshar, Sally Cripps

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16689v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16689v1)

**Summary:** Instance-wise feature selection is a valuable tool for interpreting labeled data and the predictions of black-box models. In contrast to global feature selection techniques, instance-wise methods dynamically identify important features for each instance. A growing number of methods learn a selector, which identifies important features, and a predictor, which uses these to make predictions. However, these pioneering methods face challenges including information leakage and lack of differentiabili...

---

### 40. Density-Reweighted Entropic Optimal Transport: Decoupling Geometry from Sampling Density

**Authors:** Keyi Li, Yuval Kluger, Boris Landa

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16506v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16506v1)

**Summary:** Dataset alignment is a central step in data analysis across science and engineering, where the goal is to match observations between datasets. Entropic Optimal Transport (EOT) offers a computationally tractable framework for this task by encoding cross-dataset affinities in a transport plan. However, when two datasets are sampled from geometrically similar low-dimensional structures with substantially different sampling densities, the EOT plan may match points by relative sampling density rather...

---

### 41. Improved Regret Analysis for Parallel Gaussian Process Bandit Optimization

**Authors:** Shion Takeno, Shogo Iwazaki

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16492v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16492v1)

**Summary:** This paper studies the regret analysis for parallel Gaussian process (GP) bandit optimization. The known regret upper bounds for the widely used GP batched upper confidence bound and GP batched Thompson sampling (GP-BTS) suffer from a multiplicative factor with respect to the batch size $Q$. To avoid this degradation, existing analyses require a polynomial number of uncertainty sampling (US) for $Q$ at the beginning of optimization. However, this initial US phase is often ineffective in practice...

---

### 42. Deep adaptive design with an evidential bias criterion

**Authors:** David Chen, Michael Evans, Xinwei Li, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16466v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16466v1)

**Summary:** Bayesian optimal experimental design (BOED) aims to collect informative data by optimizing an expected utility reflecting the goals of an experiment. However, this optimization is computationally challenging for common utilities and complex models. This is especially so for sequential or adaptive designs, where design and data collection alternate, so that feedback from already observed data must be taken into account. Most existing BOED research employs information gain as the utility, leading ...

---

### 43. Convergence Analysis of Statistical Inverse Problems on Reproducing Kernel Banach Spaces

**Authors:** Darrel K Joseph, M P Rajan

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16404v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16404v1)

**Summary:** Statistical inverse problems have garnered significant attention in recent years due to the growing importance of statistical learning theory and functional analytic approaches in the fields of machine learning and artificial intelligence. In this paper, we investigate the stable approximation of the element $u^{\dagger}$ that satisfies the equation $Au = g$, where $A$ is a linear operator that maps a Banach space into an appropriate function space. The function $g$ is observed only through inde...

---

### 44. LiD-GLM: Lipschitz-constrained Deep Generalized Linear Models

**Authors:** Tom Splittgerber, Niklas Koenen, Marvin N. Wright, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16340v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16340v1)

**Summary:** The combination of traditional statistical models and neural network (NN) components into semi-structured hybrid models is an intriguing approach to construct models that, ideally, combine traditional interpretability with the unprecedented flexibility of NNs. In order to preserve interpretability, it is usually necessary to restrict the NN components to prevent them from dominating the model. However, existing methods that enforce structural constraints on their NN components severely limit the...

---

### 45. Diagonal Multi-omics Integration of Heterogenous Datasets

**Authors:** Maksim V. Kukushkin, Mikhail S. Arbatskiy, Dmitriy E. Balandin, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16968v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16968v1)

**Summary:** In this paper, we consider methods for the diagonal multi-omics integration of heterogeneous datasets. Several approaches to the nature of biological heterogeneity are analyzed and developed to comprehend more clearly the generated differences. Specifically, the extremal trace problems for the coupled Laplacian on sets homeomorphic to the Stiefel manifold embedded in the complex Euclidean space are investigated. The gradient ascent method for the maximization problem is elaborated in the classic...

---

### 46. Conditional Evaluation of Language Models with Cheap Auxiliary Signals

**Authors:** Zhi Zhang, Lingfeng Lyu, Yue Kang, et al.

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16210v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16210v1)

**Summary:** Aggregate accuracy hides where models succeed and fail. Estimating conditional performance profiles from gold labels alone is expensive, while cheap auxiliary signals such as LLM-judge scores, pairwise comparisons, confidence scores, and judge-disagreement features can be collected for every benchmark item but are often biased or miscalibrated. We propose LACE (Local Augmented Control-Variate Evaluation), a semi-supervised estimator for conditional LLM evaluation. The key step is local centering...

---

### 47. Coded Hankel Polynomial Chaos: Spectral Identification of Dominant Polynomial-Chaos Modes

**Authors:** Zhiliang Deng, Xiaomei Yang

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16126v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16126v1)

**Summary:** Identification of dominant polynomial-chaos modes is usually formulated as a sparse-regression problem on a sampled multivariate polynomial dictionary. We develop coded Hankel polynomial chaos (CH-PC), a complementary spectral formulation for dominant-mode identification. A finite generating transform converts PCE coefficients into a coefficient-generating polynomial, and evaluation along a geometric phase orbit produces a finite exponential sum. Its model order and spectral nodes are encoded by...

---

### 48. EMS Coreset: An Efficient Expectation-Maximization Algorithm for Sinkhorn Coreset

**Authors:** Haoyun Yin, Chuanhui Liu, Xiao Wang

**Published:** 2026-08-17

🔗 [Paper](http://arxiv.org/abs/2608.16101v1) | 📄 [PDF](https://arxiv.org/pdf/2608.16101v1)

**Summary:** Coresets distill large datasets into small, representative subsets for efficient downstream learning. Yet Optimal Transport (OT)-based selection typically requires intensive computation of transport plans, limiting scalability. We introduce a scalable Sinkhorn coreset method that permits closed-form updates of the entropically regularized OT coupling by allowing non-uniform coreset weights. This produces centroids that generalize k-means via soft assignments. We establish asymptotic consistency ...

---

### 49. Generalized Linear Bandits with Memory

**Authors:** Heesang Ann, Hyunjun Choi, Taehyun Hwang, et al.

**Published:** 2026-08-16

🔗 [Paper](http://arxiv.org/abs/2608.15848v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15848v1)

**Summary:** We study generalized linear bandits with memory, an endogenous non-stationary setting in which rewards depend on past actions through a finite memory matrix. Building on prior work for linear models (Clerici et al., 2024), we show that the previously known $\tilde{O}(T^{3/4})$ regret bound stems from a loose analysis, and we provide a sharpened analysis that recovers a $\tilde{O}(\sqrt{T})$ regret rate in the linear case. We then extend this improvement to generalized linear models and propose a...

---

### 50. Self-Supervised Auxiliary Task Discovery for Stable Reinforcement Learning in Stock Trading

**Authors:** Arishi Orra, Himanshu Choudhary, Manoj Thakur

**Published:** 2026-08-16

🔗 [Paper](http://arxiv.org/abs/2608.15841v1) | 📄 [PDF](https://arxiv.org/pdf/2608.15841v1)

**Summary:** Reinforcement learning has gained increasing attention as a data-driven approach for stock trading. However, learning a policy that is both profitable and stable remains challenging due to non-stationary market behaviour and noisy reward signals. Auxiliary tasks are often used to improve representation learning and stabilize training, yet they are usually designed manually and depend heavily on prior assumptions about targets and prediction horizons. Such fixed designs may not remain suitable ac...

---

