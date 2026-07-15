# arXiv Daily Digest - 2026-07-15

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution

**Authors:** Junjie Yin, Xinyu Feng

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13034v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13034v1)

**Summary:** Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. We argue the missing capability is task-aware execution-scope estimation: judging a task's difficulty, the information it truly needs, and the shortest reliable path be...

---

### 2. TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

**Authors:** Zhouchonghao Wu, Akshay Rangesh, Weixin Li, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13028v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13028v1)

**Summary:** Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per se...

---

### 3. PalmClaw: A Native On-Device Agent Framework for Mobile Phones

**Authors:** Hongru Cai, Yongqi Li, Ran Wei, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13027v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13027v1)

**Summary:** Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, and daily-use applications. Existing mobile agents mainly operate smartphones through graphical user ...

---

### 4. Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model

**Authors:** Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13013v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13013v1)

**Summary:** Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time. We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps. We train an audio-native interface for DiffusionGemma, a 26B mixture-of-experts model that generates text by uniform, random-token discrete diffusion rather than the absorbing-mask scheme common to recent diffusion language models. A froz...

---

### 5. Dynamic Resource Allocation for Ensemble Determinization MCTS

**Authors:** Jakub Kowalski, Adam Ciężkowski, Artur Krzyżyński, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13007v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13007v1)

**Summary:** Simulation-based algorithms are especially suited for high-uncertainty environments such as adversarial board games with significant elements of randomness and hidden information. In particular, several Monte Carlo Tree Search (MCTS) variants are commonly used in such domains. In this paper, we propose a series of enhancements for Ensemble Determinization MCTS, introducing two axes for dynamic resource allocation. First, Dynamic Number of Determinizations, increases or decreases the number of cu...

---

### 6. Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation

**Authors:** Aleh Manchuliantsau

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12986v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12986v1)

**Summary:** Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. Proposition 1 gives the score change from deleting an interior transition while retargeting its predecessor and retaining downstream value: Delta_k = (prod_{i<k} p_i)[c_k + (1 - p_k)R_{k+1}]. On a frozen 26-route cohort, all 57 admissible deletions matched the analytic identity and threshold sign, and every route had at least ...

---

### 7. Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible LLMs

**Authors:** Sen Yang, Yuen-Hei Yeung

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12985v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12985v1)

**Summary:** Aligned language models routinely misreport under non-evidential incentive pressure: they agree with a confident user or overstate certainty even when their internal belief is unchanged. We cast this as a failure of internal incentive-compatibility (IC) and present a method for learning and certifying counterfactual report mediators that hold a model's reports to a causal contract: invariant to forbidden influences (pressure, prestige, restyling) and responsive to licensed ones (genuine evidence...

---

### 8. FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation

**Authors:** Ruoran Xu, Wending Gao, Qiufeng Wang

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12982v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12982v1)

**Summary:** Math reasoning has achieved significant progress with the rapid advancement of Multimodal Large Language Models (MLLMs), however analytic geometry remains largely underexplored, primarily due to the scarcity of annotated samples. Existing diagram generation approaches struggle with analytic geometry: template methods cannot handle constraint-driven layouts, and generative models lack the geometric precision to render annotated conic curves correctly. We present FormalAnalyticGeo, a scalable fram...

---

### 9. Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models

**Authors:** Mehmet Iscan

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12962v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12962v1)

**Summary:** Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature. We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generated code can be used operationally by that same model. In PoPE, error content is p...

---

### 10. ViHoRec: A Quality-Controlled Vietnamese Hotel Recommendation Dataset and Cold-Start Benchmark

**Authors:** Minh Hoang Nguyen

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12946v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12946v1)

**Summary:** Recommender-system research for Vietnamese remains limited by the absence of a public, well-documented hotel interaction resource. Building such a resource is challenging for three reasons: cross-platform hotel names must be reconciled before interactions are comparable; quality must be audited with reproducible metrics rather than ad hoc cleaning; and public release must preserve privacy while remaining benchmarkable under realistic cold-start conditions. We introduce ViHoRec, a quality-control...

---

### 11. Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes

**Authors:** Jonas Ehrhardt, René Heesch, Oliver Niggemann

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12924v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12924v1)

**Summary:** In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Reinforcement Learning algorithms typically determine parameters with one-shot estimators, which makes their training sample inefficient. Though in most PAMDP environments explicit but incomplete knowledge (e.g., rules, safety constraints, or expert heuristics) is available, it is rarely directly used...

---

### 12. Real-time fall detection based on vision for low-power edge platforms

**Authors:** Wenjun Xia, Zhicheng Peng, Haopeng Li, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12909v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12909v1)

**Summary:** Falling detection is vital for elderly care and intelligent surveillance; however, prevailing vision-based approaches predominantly frame it as static pose classification or discrete temporal pattern matching, fundamentally overlooking the instability dynamics of the human support system. This paper proposes a physics-informed falling detection framework that recasts falling as a stability-loss event in a coupled dynamical system. We introduce a novel dual-LTC architecture comprising a Center-of...

---

### 13. MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations

**Authors:** Xixuan Hao, Zeyu Zhang, Zehao Lin, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12893v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12893v1)

**Summary:** Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values...

---

### 14. UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies

**Authors:** Lirui Zhao, Modi Shi, Li Chen, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12892v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12892v1)

**Summary:** Modern robot learning systems increasingly rely on dense progress or value signals to evaluate intermediate states, guide policy learning, and detect task completion, making the quality of these signals critical. Since such dense labels are rarely available at scale, normalized time within a demonstration is often used as a scalable substitute: later frames are treated as higher progress. However, this time-derived label is only a noisy proxy for physical task progress. In contact-rich manipulat...

---

### 15. A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study

**Authors:** Cameron Cagan, Pedram Fard, Jiazi Tian, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12886v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12886v1)

**Summary:** Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concepts without manual prompt engineering or fine-tuning. Running on a locally hosted ...

---

### 16. Unveiling Complex Collective Behaviors from Simple Rewards

**Authors:** Yize Mi, Jianan Li, Liang Li, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12861v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12861v1)

**Summary:** Multi-agent Reinforcement Learning (MARL) holds great potential for robot swarms, but the black-box nature of neural policies complicates strategic analysis, limiting multi-robot applications. Furthermore, complex swarm behaviors can surprisingly emerge from simple rewards without explicit aggregation incentives. Unveiling the mechanisms behind this emergence is critical, but the disconnection between simple rewards and collective behaviors exacerbates interpretability challenges. This paper aim...

---

### 17. ChartGenEval: Corruption-Tested Multi-Dimensional Feedback for Rhythm-Game Chart Generation

**Authors:** Jhen-Ke Lin

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12857v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12857v1)

**Summary:** A generated rhythm-game chart need not reproduce one official note sequence: many note choices can fit the same song and difficulty. Reference-note agreement therefore measures reconstruction, not the full design problem. We introduce ChartGenEval, a six-question evaluation framework with an automatic, corruption-tested core. It leaves note choice open while anchoring timing to the song: the matched official chart supplies only its authored timing map, never target notes.   We test each core out...

---

### 18. Reproducible Reservoir Computing with Thermally Driven Superparamagnets: Controlling Temperature Sensitivity

**Authors:** Zhengfei Chen, Alex Welbourne, Matthew O. A. Ellis, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12840v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12840v1)

**Summary:** Unconventional computing systems must demonstrate robust performance under real-world environmental conditions to enable practical deployments. We have recently proposed superparamagnetic nanodot ensembles driven by strain-induced magnetoelectric coupling as exciting candidates for use as ultra-low energy consumption reservoir computing substrates. However, because their dynamics are governed by thermal activation effects, these systems are intrinsically sensitive to ambient temperature fluctuat...

---

### 19. Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques

**Authors:** Daehoon Gwak, Minhyung Lee, Junwoo Park, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12829v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12829v1)

**Summary:** Diffusion large language models (dLLMs) offer a theoretical advantage in parallel generation over standard autoregressive models. However, parallel generation alone does not guarantee practical speedups. Realizing this efficiency requires specialized inference mechanisms, such as diffusion-aware caching and reuse. Consequently, as inference efficiency becomes a prerequisite for practical deployment, recent research has actively explored acceleration techniques across algorithms, architectures, a...

---

### 20. Solution of the Hempel's statistical ambiguity problem and Causal AI

**Authors:** Evgenii Vityaev

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12826v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12826v1)

**Summary:** This paper addresses Carl Hempel's longstanding problem of statistical ambiguity in inductive-statistical inference, in which contradictory predictions are derived from statistical laws. To avoid such predictions, Carl Hempel proposed the Requirement of Maximal Specificity (RMS) for the statistical laws used in the inference. An analysis of the RMS refinements made by Wesley Salmon, Alberto Coffa, and James Fetzer led to the following definition of maximally specific statistical laws: "the lawli...

---

### 21. Human-AI Agent Interaction as a Neuroplastic Training Environment

**Authors:** Eranga Bandara, Ross Gore, Asanga Gunaratna, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12823v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12823v1)

**Summary:** Interaction with AI agents has become one of the most frequent activities of everyday digital life. Whether conversing with an assistant, working with a coding copilot, or generating images, the interaction follows a common iterative loop: a request is issued, a result returned, appraised, and the request revised. We observe that this loop is a high-frequency stream of contact events -- moments at which a result meets a person and a conditioned response may fire before deliberate appraisal -- ma...

---

### 22. Visual Access Boundaries in Vision-Language Model Reasoning

**Authors:** Hiroto Osaka, Shohei Taniguchi, Gouki Minegishi, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12815v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12815v1)

**Summary:** Chain-of-Thought (CoT) prompting is widely used as a test-time scaling strategy for Vision-Language Models (VLMs), but it remains unclear what is extended when VLMs generate longer reasoning traces. We ask whether CoT requires continued access to image tokens, or whether it mainly operates over visual information already made available earlier in the forward pass. We introduce Visual Access Sweep, a causal intervention that masks attention from generated-token queries to image-token keys along l...

---

### 23. PixelLoop: Shortcut Topological Navigation with Pixel-Level Loops

**Authors:** Sarthak Chittawar, Vansh Garg, Aditya Vadali, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12811v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12811v1)

**Summary:** Although topological mapping and navigation have been studied extensively, the specific role and downstream effect of loop closures in purely topological representations has received relatively little attention. Importantly, loop closure over topological maps is distinct from loop closure over globally referenced trajectories and metric maps. Building on recent denser topologies grounded in pixel-level, relative 3D geometry, we propose PixelLoop which introduces loop closures directly in pixel s...

---

### 24. Autonomous Tracking and Terminal Guidance of Moving Targets for Fixed-Wing UAVs

**Authors:** Wei-Hao Liou, Teng-Hu Cheng

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12801v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12801v1)

**Summary:** This study introduces a unified control framework for fixed-wing unmanned aerial vehicles (UAVs) fitted with a pan-tilt (PT) camera, intended to perform an end-to-end mission spanning from initial target detection to accurate terminal engagement. The proposed system employs a three-phase strategy: a vision-based target acquisition phase, an NMPC-based tracking phase, and a terminal guidance phase. During tracking, the framework uses an Unscented Kalman Filter (UKF) to fuse YOLO-based visual dete...

---

### 25. The One-Word Census: Answer-Choice Conformity Across 44 Language Models

**Authors:** Tapan Parikh

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12796v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12796v1)

**Summary:** When a language model must pick one answer from a large space of equally valid options, which does it pick -- and how often is it the same answer every other model picks? Asked to "pick a word -- any word," 44 models chose "serendipity" 41% of the time. We characterize this convergence with a deliberately minimal instrument: 31 single-turn prompts, each naming a category with many valid one-word answers ("Name a tree."), asked four times per model with no system prompt. Analysis is exact-match o...

---

### 26. Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models and Quantization Levels

**Authors:** Roman Prosvirnin, Victor Minchenkov, Alexey Soldatov, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12792v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12792v1)

**Summary:** Jailbreak-robustness research typically evaluates safety through generated responses using an LLM-as-judge approach. Such evaluations, however, are sensitive to the benchmark's grading procedure and capture only observed behavior on a given set of attacks, without directly revealing the hidden fragility of the underlying safety mechanisms. This work proposes JADR (Jacobian Assessment of Danger Recognition), a protocol that measures a model's internal representation through Jacobian space (J-spac...

---

### 27. Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents

**Authors:** Xing Zhang, Guanghui Wang, Yanwei Cui, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12790v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12790v1)

**Summary:** Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and aud...

---

### 28. Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?

**Authors:** Kaiwen Zheng, Junchen Fu, Wenhao Deng, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12787v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12787v1)

**Summary:** Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on reso...

---

### 29. When Close Enough Is Not Enough: Autoregressive Drift in Quantum Circuit Synthesis

**Authors:** Mehdi Saeedi, Eddie Richter, Paul Hartke

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12780v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12780v1)

**Summary:** Quantum circuit optimization for fault-tolerant computing requires exact functional equivalence while minimizing expensive non-Clifford resources such as T gates. We study this problem using a compact 44.8M-parameter encoder-decoder transformer with structured circuit tokenization, evaluating on parameterized circuits (2-6 qubits) and Clifford+T circuits (3-6 qubits). On parameterized circuits, a hybrid approach -- structure from the transformer, angles from classical optimization -- achieves me...

---

### 30. HSEmotion Team at the 11th ABAW Challenge: Multi-Task Learning and Ambivalence/Hesitancy Video Recognition

**Authors:** Aleksei Bakin, Andrey V. Savchenko

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12774v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12774v1)

**Summary:** This article presents our results for the 11th Affective Behavior Analysis in-the-Wild (ABAW) competition. For multi-task learning with simultaneous prediction of valence, arousal, facial expressions, and action units on s-Aff-Wild2 dataset, we use frozen lightweight facial extractors, MT-EmotiDDAMFN and MT-EmotiEffNet-B0, with separate heads and systematic post-processing: temporal Gaussian smoothing, per-class expression bias, AffectNet blending, per-AU threshold tuning, and weighted backbone ...

---

### 31. Accuracy and Normalized Accuracy under Length Bias: Analysis, Guidelines, and a Bayesian Alternative

**Authors:** Koen Oostermeijer

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12767v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12767v1)

**Summary:** Multiple-choice benchmarks that rank candidate completions by conditional log-probability suffer from a length bias: because log-probabilities sum over tokens, longer answers tend to be penalized relative to shorter ones in practice. A common mitigation is to normalize scores by completion length, but we show empirically that this heuristic frequently over-corrects, introducing a bias toward longer answers instead. We first analyze these scoring rules, characterizing when standard and length-nor...

---

### 32. Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination

**Authors:** Usman Haider, Karl Mason

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12763v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12763v1)

**Summary:** Federated Reinforcement Learning (FedRL) enables coordination of distributed energy resources without sharing raw local data, but standard aggregation methods such as FedAvg do not account for system-level constraints, often leading to unsafe global behavior. In this work, we study constraint-aware aggregation for federated reinforcement learning in distributed energy coordination. We propose aggregation rules that incorporate both local performance and estimated constraint violation into the se...

---

### 33. Practical Judgment, Virtue, and Intuition in the Use of Opaque AI-Enabled Systems

**Authors:** Nathan G. Wood, Andrew P. Rebera

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12755v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12755v1)

**Summary:** AI-enabled systems are seeing increasing deployment across numerous domains, with many being "black boxes" with respect to core functions and capabilities. I.e., many systems take inputs and give outputs, but without users having any ability to see how the former lead to the latter. AI-enabled systems are also being used to augment autonomy in systems, and autonomy coupled with opacity raises numerous concerns surrounding, e.g., the reliability of systems, their regularity in functioning, human ...

---

### 34. Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal Generation

**Authors:** Hongbo Wang, Huaibo Huang, Jie Cao, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12752v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12752v1)

**Summary:** While recent advances in 3D generation have enabled impressive visual synthesis, existing methods often rely on 2D diffusion supervision without explicit mechanisms for geometric consistency, leading to spatial hallucinations such as duplicated structures and misaligned geometry. These issues become more severe in 4D generation, where maintaining consistency across viewpoints and temporal evolution introduces additional challenges, including jitter, identity flicker, and structural drift. We pre...

---

### 35. Weakly Supervised Spatio-Temporal Candidate Discovery of Dairy Farm Sites from Seasonal Satellite Imagery

**Authors:** Usman Haider, Fatima Khalid, Karl Mason

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12748v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12748v1)

**Summary:** Farm site discovery from satellite imagery is a spatiotemporal candidate ranking problem because farm evidence is distributed across pasture, field boundaries, roads, buildings, and seasonal vegetation patterns. Direct farm labels are often incomplete, which makes fully supervised detection difficult. This paper proposes a weakly supervised pipeline for ranking dairy farm candidate clusters from seasonal Sentinel imagery and open map priors. The method uses aligned spring, summer, and autumn ima...

---

### 36. Tracing Agentic Failure from the Flow of Success

**Authors:** Samuel Yeh, Yiwen Zhu, Shaleen Deep, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12747v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12747v1)

**Summary:** Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. Existing approaches either rely on prompting-based pipelines, which are computationally expensive, or require post-training on failure trajectories with step-level error annotations, which are costly to collect and difficult to scale. We argue that a practical failure attribution model should be lightweight and tr...

---

### 37. LLMs Can See the Smoke but not the Fire: Evaluating Abductive Reasoning with Elenchos

**Authors:** Julius Steiglechner, Lucas Mahler, Gabriele Lohmann

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12733v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12733v1)

**Summary:** Large language models (LLMs) excel at pattern recognition and text generation, but their capacity for abductive inference - inferring latent hypotheses that explain observed behavior - remains poorly understood. Here, we introduce Elenchos (named after the Socratic method of cross-examination), a generative evaluation framework that measures abductive reasoning as a structural inverse problem. Given a reference formal system, such as the lambda-calculus, and a potentially mutated counterpart, ag...

---

### 38. Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty

**Authors:** Sarah Al-Shareeda, Gulcihan Ozdemir, Heung Seok Jeon

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12730v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12730v1)

**Summary:** Smart-building load forecasters are often trained offline on dense, multivariate, high-frequency data, but deployment may provide only hourly, feature-limited inputs. Missing features must then be reconstructed, and their errors can propagate through the model. If this input uncertainty is not reflected, prediction intervals may become miscalibrated, affecting demand-response scheduling. Our work examines where uncertainty should be placed once inference inputs are reconstructed. We develop a un...

---

### 39. Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities

**Authors:** Qiyuan Fan, Zhi Li, Junjie Li, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12723v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12723v1)

**Summary:** Filesystem isolation in container ecosystems is often weakened by cross-boundary path misresolution, causing path traversal (PaTra) vulnerabilities. These vulnerabilities stem from insecure host-container interactions and have become increasingly pervasive as cloud systems mount shared resources, such as GPUs and agent workspaces, into containers to support AI workloads. Existing defenses remain inadequate. Kernel-level protections are intrusive, can destabilize system calls, and have therefore ...

---

### 40. Line-Anchored Feedback Cuts Token Costs and Improves Correctness in AI Code Editing

**Authors:** William Franz Lamberti

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12713v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12713v1)

**Summary:** Generated tokens are a direct driver of the cost, latency, and energy of generative AI (GAI) code editing. We show the format of feedback is a lever on all three. We compare two deliveries of the same requested changes: a holistic prompt (control) versus the structured, line-anchored export of FileMark (treatment). FileMark is a VSCodium extension for inline comments on any file. In a paired experiment line anchoring cut generated tokens by 22% (Claude Opus) and 58% (Claude Sonnet), reaching 24%...

---

### 41. MaxSAT-Based Feedback for Guiding Vision-Language Models in Sudoku

**Authors:** Pedro Orvalho, Guillem Alenyà, Felip Manyà

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12711v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12711v1)

**Summary:** Vision--Language Models (VLMs) have recently demonstrated promising performance on structured visual reasoning tasks, including grid-based puzzles. However, despite strong perceptual capabilities, these models lack explicit mechanisms for enforcing logical consistency and frequently generate assignments that violate underlying constraints. In this paper, we propose a neuro-symbolic approach that integrates formal constraint reasoning into the VLM solving process via a Maximum Satisfiability (Max...

---

### 42. Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts

**Authors:** Jincheng Xie, Runheng Liu, Heyan Huang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12696v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12696v1)

**Summary:** Sparse Mixture-of-Experts (MoE) models have become an important approach for scaling Large Language Models (LLMs), but their inference efficiency depends strongly on expert activation patterns. Speculative decoding (SD) accelerates autoregressive generation by verifying multiple draft tokens in parallel, yet existing draft selection strategies primarily optimize acceptance likelihood. In large-scale MoE models, however, selecting draft tokens also determines the union of experts activated during...

---

### 43. From Critic to Confidence: PPO for Language-Based Quantitative Prediction with Confidence Estimation

**Authors:** Mehak Dhaliwal, Rasta Tadayon, Andong Hua, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12687v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12687v1)

**Summary:** LLMs can perform language-based quantitative prediction from unstructured inputs, but remain susceptible to hallucinations and overconfident errors, making it critical to know not only what a model predicts, but when its predictions can be trusted. We introduce CARE-PPO, a reinforcement learning framework that establishes a connection between loss prediction for uncertainty estimation and actor-critic PPO fine-tuning, enabling joint learning of accurate numerical estimates and reliable confidenc...

---

### 44. Text-Aided Multi-Modal Panoptic Symbol Spotting for CAD Floor Plan Drawings

**Authors:** Yan Gong, Bohao Li, Bowen Du, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12678v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12678v1)

**Summary:** Computer-Aided Design (CAD) floor plan drawings contain both graphical primitives and textual annotations, which provide complementary geometric and semantic cues for intelligent design understanding. Among CAD analysis tasks, panoptic symbol spotting has become increasingly important with the growing demand for industrial digitalization and deep learning-based automation. However, most existing methods remain primarily primitive-centric and underexploit textual annotations, despite their critic...

---

### 45. Internet of Agentic Things: Networked AI Agents for Closed-Loop IoT Orchestration

**Authors:** Quanyan Zhu

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12662v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12662v1)

**Summary:** The paper introduces the Internet of Agentic Things (IoAT), an architectural framework that integrates agentic AI, IoT, cyber-physical systems, Physical AI, edge computing, and digital twins into a unified closed-loop orchestration framework. The proposed architecture consists of cloud, edge/fog, and physical IoT layers connected through autonomous AI agents that perceive, reason, coordinate, and actuate across distributed cyber-physical environments. The paper formalizes IoAT as a coupled workf...

---

### 46. Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference

**Authors:** Zebin Yang, Qi Wang, Yunhe Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12659v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12659v1)

**Summary:** Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially mask this latency by parallelizing action execution and subsequent inference, but it introduces two critical issues: perception-execution misa...

---

### 47. Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

**Authors:** Junyu Ren

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12650v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12650v1)

**Summary:** Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny. We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts. Every verified output structurally descends from an attested tool call (Thm. 3.1) and...

---

### 48. A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism

**Authors:** Chengguang Gan, Zhixi Cai, Yunhao Liang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12640v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12640v1)

**Summary:** Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised checkpoint in the hope of producing a stronger agent. We ask whether it adds skill to a small language and vision-language model web agent at the 4B to 8B scale, or whether it mostly reshapes behavior the supervised model already has. Across a control grid of 18 runs that varies learning rate, KL weight, seed, initialization, and clipping, no configura...

---

### 49. Atomic Units of X: The Compression Layer of Intelligence

**Authors:** Sachin Dev Duggal, Pradyumna Swarnalatha Ramanna, Alexandros Vassiliades

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12634v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12634v1)

**Summary:** This paper proposes a theoretical framework for understanding intelligence as a process of atomic compression and compositional reuse. We argue that cognitive, biological, computational, and organizational systems achieve scalable intelligence by decomposing complex phenomena into reusable atomic units that can be recombined into higher-order structures. Drawing on evidence from cognitive science, information theory, evolutionary biology, software engineering, medicine, legal reasoning, educatio...

---

### 50. Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?

**Authors:** Minh Khoi Ho, Zihao Zhu, Runchuan Zhu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12631v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12631v1)

**Summary:** As Large Language Models (LLMs) are increasingly deployed as autonomous agents in high-stakes domains, understanding contextual factors that may modulate their decision-making becomes critical. While LLMs are trained to perceive and resonate with users' emotions, it remains unclear whether induced emotion can influence their sequential decision-making. We investigate this question using the Iowa Gambling Task (IGT), a classic psychological paradigm for studying decision-making under uncertainty,...

---

## cs.CL

**50 papers**

### 1. Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution

**Authors:** Junjie Yin, Xinyu Feng

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13034v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13034v1)

**Summary:** Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. We argue the missing capability is task-aware execution-scope estimation: judging a task's difficulty, the information it truly needs, and the shortest reliable path be...

---

### 2. PalmClaw: A Native On-Device Agent Framework for Mobile Phones

**Authors:** Hongru Cai, Yongqi Li, Ran Wei, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13027v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13027v1)

**Summary:** Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, and daily-use applications. Existing mobile agents mainly operate smartphones through graphical user ...

---

### 3. The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context

**Authors:** Yanzhe Zhang, Sanmi Koyejo, Diyi Yang

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12963v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12963v1)

**Summary:** As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy. This aggregate stability, however, masks significant per-example instability. Even semantically meanin...

---

### 4. MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations

**Authors:** Xixuan Hao, Zeyu Zhang, Zehao Lin, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12893v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12893v1)

**Summary:** Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values...

---

### 5. LLM Judges Can Be Too Generous When There Is No Reference Answer

**Authors:** Chalamalasetti Kranti, Sowmya Vajjala

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12885v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12885v1)

**Summary:** LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such evaluation setups? We explore this question in this paper through a two stage pipeline with a) calibration experiments that assess the judge model's knowledge of the task it is evaluating, and b) sensitivity experiments that assess how the judge model's performance is impacted by the presence and positi...

---

### 6. Evaluating Large Language Models on Misconceptions in Multi-Turn Medical Conversations

**Authors:** Monica Munnangi, Saiph Savage

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12884v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12884v1)

**Summary:** Patients seeking medical information often ask questions that embed incorrect assumptions or misconceptions. In such cases, safe medical communication requires not only answering the question, but identifying and correcting the underlying false belief. These interactions naturally unfold over multiple turns, a pattern now mirrored in interactions with LLMs. Yet current evaluation frameworks do not capture model behavior in these settings, where misconceptions can emerge, persist, or evolve over ...

---

### 7. Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction

**Authors:** Hanhua Hong, Yizhi Li, Jiaoyan Chen, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12835v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12835v1)

**Summary:** Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is prone to hallucination. However, constructing paper-specific rubrics requires substantial expert effort, limiting the scalability of benchmarks such as PaperBench. In this work, we present, to our knowledge, the first systematic meta-evaluation of LLM-generated rubrics for paper reproduction. We reformu...

---

### 8. Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling

**Authors:** Roi Cohen, Yvan Carré, Nick Lechtenbörger, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12831v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12831v1)

**Summary:** Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning. We introduce Knowledge--''Less'' Language Models (KLLMs), a fundamentally different epistemic training paradigm for LLMs, which are pretra...

---

### 9. Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques

**Authors:** Daehoon Gwak, Minhyung Lee, Junwoo Park, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12829v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12829v1)

**Summary:** Diffusion large language models (dLLMs) offer a theoretical advantage in parallel generation over standard autoregressive models. However, parallel generation alone does not guarantee practical speedups. Realizing this efficiency requires specialized inference mechanisms, such as diffusion-aware caching and reuse. Consequently, as inference efficiency becomes a prerequisite for practical deployment, recent research has actively explored acceleration techniques across algorithms, architectures, a...

---

### 10. The One-Word Census: Answer-Choice Conformity Across 44 Language Models

**Authors:** Tapan Parikh

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12796v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12796v1)

**Summary:** When a language model must pick one answer from a large space of equally valid options, which does it pick -- and how often is it the same answer every other model picks? Asked to "pick a word -- any word," 44 models chose "serendipity" 41% of the time. We characterize this convergence with a deliberately minimal instrument: 31 single-turn prompts, each naming a category with many valid one-word answers ("Name a tree."), asked four times per model with no system prompt. Analysis is exact-match o...

---

### 11. Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents

**Authors:** Xing Zhang, Guanghui Wang, Yanwei Cui, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12790v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12790v1)

**Summary:** Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and aud...

---

### 12. Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?

**Authors:** Kaiwen Zheng, Junchen Fu, Wenhao Deng, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12787v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12787v1)

**Summary:** Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on reso...

---

### 13. Learning Mechanistic Reasoning for Chemical Reactions with Large Language Models

**Authors:** Xingyu Dang, Haocheng Tang, Junmei Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12771v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12771v1)

**Summary:** Reaction mechanisms consist of the step-by-step sequences of elementary reactions that explain chemical transformations. Learning the mechanism logic is therefore essential for enhancing the fundamental chemical intelligence of large language models (LLMs). The stepwise deduction of reaction mechanism aligns naturally with the reasoning paradigms of reasoning LLMs. However, current chemical LLMs primarily emphasize coarse-grained name reactions for product prediction and retrosynthesis, often le...

---

### 14. Tracing Agentic Failure from the Flow of Success

**Authors:** Samuel Yeh, Yiwen Zhu, Shaleen Deep, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12747v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12747v1)

**Summary:** Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. Existing approaches either rely on prompting-based pipelines, which are computationally expensive, or require post-training on failure trajectories with step-level error annotations, which are costly to collect and difficult to scale. We argue that a practical failure attribution model should be lightweight and tr...

---

### 15. Epistemic Stance Flexibility Probing: Measuring Prompt-Conditioned Register Shift in Large Language Models

**Authors:** Binwen Liu, Yilin Ren

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12739v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12739v1)

**Summary:** A language model may be asked either what experts believe about a contested claim or what it believes about the claim itself. A trustworthy conversational agent should distinguish these two requests and respond in different epistemic registers: neutral attribution in the first case and stance expression in the second. Whether such a shift occurs-and whether it occurs coherently-is not directly assessed by existing benchmarks for accuracy, instruction following, or safety. We introduce ESFP, a be...

---

### 16. Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts

**Authors:** Jincheng Xie, Runheng Liu, Heyan Huang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12696v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12696v1)

**Summary:** Sparse Mixture-of-Experts (MoE) models have become an important approach for scaling Large Language Models (LLMs), but their inference efficiency depends strongly on expert activation patterns. Speculative decoding (SD) accelerates autoregressive generation by verifying multiple draft tokens in parallel, yet existing draft selection strategies primarily optimize acceptance likelihood. In large-scale MoE models, however, selecting draft tokens also determines the union of experts activated during...

---

### 17. From Critic to Confidence: PPO for Language-Based Quantitative Prediction with Confidence Estimation

**Authors:** Mehak Dhaliwal, Rasta Tadayon, Andong Hua, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12687v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12687v1)

**Summary:** LLMs can perform language-based quantitative prediction from unstructured inputs, but remain susceptible to hallucinations and overconfident errors, making it critical to know not only what a model predicts, but when its predictions can be trusted. We introduce CARE-PPO, a reinforcement learning framework that establishes a connection between loss prediction for uncertainty estimation and actor-critic PPO fine-tuning, enabling joint learning of accurate numerical estimates and reliable confidenc...

---

### 18. Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis

**Authors:** Alexios Filippakopoulos, Elias Kallioras, Nikolaos Xiros, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12686v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12686v1)

**Summary:** Multimodal fusion must simultaneously refine modality-specific signals and model cross-modal interactions; two competing objectives typically entangled within the same operation. We propose \textbf{SeRIn} (\textbf{Se}gregate, \textbf{R}efine, \textbf{In}tegrate), a multimodal LM fusion scheme that enforces this separation as an architectural prior. Modality-specific representations evolve along isolated pathways, each refined against its respective encoder context, while a dedicated cross-modal ...

---

### 19. Extractable Memorization From First Principles

**Authors:** A. Feder Cooper, Marika Swanberg, Jamie Hayes, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12649v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12649v1)

**Summary:** Recent work on extractable memorization in LLMs suffers from two contrasting validity problems. Some studies overstate extraction, e.g., relying on sequences too short to distinguish memorization from predictability. Others imply that extraction is unreliable evidence of memorization, since models can also reproduce real-world text they weren't explicitly trained on. In different ways, both overlook what makes a valid extraction claim: the model must generate a training sequence with high enough...

---

### 20. A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism

**Authors:** Chengguang Gan, Zhixi Cai, Yunhao Liang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12640v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12640v1)

**Summary:** Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised checkpoint in the hope of producing a stronger agent. We ask whether it adds skill to a small language and vision-language model web agent at the 4B to 8B scale, or whether it mostly reshapes behavior the supervised model already has. Across a control grid of 18 runs that varies learning rate, KL weight, seed, initialization, and clipping, no configura...

---

### 21. Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?

**Authors:** Minh Khoi Ho, Zihao Zhu, Runchuan Zhu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12631v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12631v1)

**Summary:** As Large Language Models (LLMs) are increasingly deployed as autonomous agents in high-stakes domains, understanding contextual factors that may modulate their decision-making becomes critical. While LLMs are trained to perceive and resonate with users' emotions, it remains unclear whether induced emotion can influence their sequential decision-making. We investigate this question using the Iowa Gambling Task (IGT), a classic psychological paradigm for studying decision-making under uncertainty,...

---

### 22. KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill

**Authors:** Yunxin Li, Jinchao Li, Shibo Su, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12625v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12625v1)

**Summary:** OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism. These flaws limit its adaptation to diverse device ecosystems and prevent performance improvements through continuous learning from execution experience. To resolve these issues, we propose the Know Deeply, Act Perfectly paradigm for personal assistants, which holds that accumulated user interaction and task-run...

---

### 23. Translation as a Computationally Efficient Bridge: Feasibility of English BERT for Low-Resource Languages

**Authors:** Hielke Muizelaar, Giulia Rivetti, Marco Spruit, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12612v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12612v1)

**Summary:** BERT models have revolutionised Natural Language Processing (NLP) through their ability to process unstructured text across diverse domains. However, developing high-quality BERT models for non-English languages remains challenging due to limited annotated data and high computational demands. Translating non-English data into English and fine-tuning existing English BERT models offers a resource-efficient alternative, yet few studies have structurally compared translation-based fine-tuning with ...

---

### 24. A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs

**Authors:** Rahul Krishnan, Volker Schulz

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12550v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12550v1)

**Summary:** The key-value (KV) cache has become the dominant memory cost of transformer inference. It grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the ceiling on throughput. Two families of methods reduce it. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither family exploits the fact that the cache at a layer i...

---

### 25. Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models

**Authors:** Yubo Wang, Jiarong Liang, Yuxuan Zhang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12463v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12463v1)

**Summary:** Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction. We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value. This conditioning structure exists at internet scale in ordinary code. We explo...

---

### 26. Language Identification with Succinct Machine-Independent Traces

**Authors:** Moses Charikar, Jon Kleinberg, Chirag Pabbaraju

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12443v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12443v1)

**Summary:** Motivated by the power of large language models, there has been renewed interest in the Gold-Angluin model of language identification in the limit, with an eye toward variants of the model that might overcome the negative results for its original formulation. Recent papers on this question have proposed looking at computational traces and annotations of training strings as a source of additional power for a learner, reflecting empirical regularities such as the way that commented source code is ...

---

### 27. WikiSTAR: A System for Shedding Light on the Hidden History of Scientific Wikipedia Articles

**Authors:** Omer Ehrlich, Nitzan Barzilay, Rona Aviram, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12441v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12441v1)

**Summary:** Wikipedia plays a key role in shaping public understanding of science, and its openly accessible revision history is a unique record of how scientific knowledge evolves over time. Yet scientifically meaningful revisions are obscured by the sheer volume of routine edits, leaving each article's scientific history hidden. We present WikiSTAR (Scientific Tracking of Article Revisions), an interactive system for exploring scientifically meaningful changes across an article's revision history. Using a...

---

### 28. Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

**Authors:** Xinyu Tang, Gangqiang Cao, Yurou Liu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12395v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12395v1)

**Summary:** Reinforcement learning with verifiable rewards without human-annotated data, often referred to as zero RL, has emerged as a powerful paradigm for eliciting chain-of-thought reasoning. However, due to computational constraints, existing studies are largely restricted to small models, leaving the training dynamics and emergent capabilities at a large scale unexplored. To meaningfully explore this frontier, we aim to elicit high-quality reasoning behaviors from the model. However, we find that naiv...

---

### 29. Beyond Binary Detection: A Multi-Dimensional Taxonomy of Cancer Misinformation on Reddit

**Authors:** Aria Pessianzadeh, Pooriya Jamie, Naima Sultana, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12383v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12383v1)

**Summary:** Cancer-related discussions on social media provide an important space for information exchange and peer support, but also facilitate the spread of misinformation that may influence prevention, screening, and treatment decisions. Existing research on cancer misinformation often relies on narrow definitions, small-scale datasets, or binary labeling frameworks. We introduce a multi-dimensional taxonomy for characterizing cancer misinformation in Reddit discussions of breast, lung, colon, and prosta...

---

### 30. Policy-Conditioned Constrained Decoding for Column-Level Access Control in Text-to-SQL

**Authors:** Ryoto Miyamoto, Xin Fan, Hayato Yamana

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12341v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12341v1)

**Summary:** Text-to-SQL is increasingly deployed across trust boundaries between data providers and users. Such deployment must balance three competing requirements: policy compliance, answer coverage, and bounded cost. Existing approaches typically decide refusal based on which columns a query mentions and enforce it stochastically. Whether a query is compliant, however, depends not only on which columns appear but on how they are used, and stochastic enforcement cannot deterministically rule out violation...

---

### 31. Evaluating Health Misinformation in Low-Resource Languages: Integrating Small Language Models with a Culturally-Sensitive Responsible NLP Framework (Bangla as a Case Study)

**Authors:** Farnaz Farid, Raihan Alam, Al Al-Areqi, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12336v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12336v1)

**Summary:** Artificial Intelligence (AI) technologies, while serving as a foundational enabler for modern social media and digital health services, exert a bivalent effect by simultaneously acting as a combatant against and a spread vector for misinformation. A prevalent challenge in mitigating this issue arises in non-English contexts and low socioeconomic classes, where limited data hinders the training of AI models for effective detection. Consequently, culturally and linguistically diverse (CALD) commun...

---

### 32. QUBO-Optimized Evidence Selection for Retrieval-Augmented Question Answering with Unconventional Solvers

**Authors:** Rahul Singh, Madhav Vadlamani

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12334v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12334v1)

**Summary:** Retrieval-augmented question answering depends on selecting evidence passages that jointly support answer generation. However, many RAG pipelines rely on top-\(k\) ranking, where passages are selected mainly by individual relevance scores, even though multi-hop questions often require complementary evidence satisfying multiple information requirements. Recent LLM-based selectors address this by treating retrieval as set selection, but using an LLM for this intermediate stage can be costly and di...

---

### 33. LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes

**Authors:** Michael Solodko, Steven Gong, Guangwei Yu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12310v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12310v1)

**Summary:** While modern question answering (QA) systems excel on clean, schema-aligned corpora, real-world knowledge is rarely so neatly packaged. Answering questions over enterprise and scientific data lakes requires systems to navigate heterogeneous, weakly structured collections of tables, passages, and linked metadata. Current benchmarks abstract away this noisy discovery process, failing to evaluate end-to-end performance. To bridge this gap, we introduce LakeQuest, a human-validated benchmark of 9,84...

---

### 34. The Sound of Absence: Audio-Language Embedding Models Struggle with Negation

**Authors:** Chun-Yi Kuan, Hung-yi Lee

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12290v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12290v1)

**Summary:** Audio-language embedding models such as CLAP are widely evaluated on matching present sound events, but rarely on negation. We show this affirmation-only evaluation hides a key limitation: these models fail to encode negated sound concepts, mapping affirmative and negated captions to nearly identical representations. To expose this blind spot, we introduce NegEval-Audio, a framework that converts existing datasets into two negation-aware tasks, Retrieval-Neg and Multiple-Choice Negation (MCQ-Neg...

---

### 35. A Shared Subcircuit Lets LLMs Count Down Across Tasks

**Authors:** Jacob Dunefsky, Wes Gurnee, Emmanuel Ameisen

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12279v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12279v1)

**Summary:** Writing a sentence of exactly twelve words; ending a DNA sequence at the right codon; formatting an ASCII table. These are all tasks that language models can do that requires tracking how many tokens remain before a target. In this work, we identify in Llama-3.1-70B-Instruct a general mechanism for performing these tasks: a "countdown subcircuit" that compares the current position to a goal length and estimates the time remaining until then. We first isolate a countdown subcircuit in a controlle...

---

### 36. Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs

**Authors:** Xiaoning Ren, Yinxing Xue, Lei Ma, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12273v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12273v1)

**Summary:** As Code Large Language Models (LLMs) become central to modern software engineering, their inherent stochasticity poses significant real-world risks, where even minor errors can lead to severe functional, security, or safety consequences. Reliable automation, therefore, demands the ability to distinguish between confident, well-supported predictions and stochastic guessing. However, existing uncertainty estimation methods face a critical gap: white and grey-box techniques are often inapplicable t...

---

### 37. On-Device Deep Research at 4B: Exposure Bounds Faithfulness, Retrieval Bounds Coverage

**Authors:** Vinay Kumar Chaganti

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12257v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12257v1)

**Summary:** On-device research agents search a corpus, read sources, and write a cited brief on a personal laptop. Whether their citations are faithful, and at what cost, is unmeasured for a deployable small model. This study fixes one 4B generator on a 24 GB laptop and asks what makes its citations faithful. It separates two quantities usually reported as one number. Cited claim faithfulness asks whether the cited source supports the claim. Trustworthy coverage asks whether the agent also cites the right s...

---

### 38. FinResearchBench II: A Deep Research Benchmark with Consensus-Derived Gold Rubrics for Distinguishing Financial Report Quality

**Authors:** Beidi Luan, Rui Sun, Sinuo Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12252v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12252v1)

**Summary:** Deep research agents are increasingly used to produce long-form financial reports, yet large-scale evaluation remains bottlenecked by the need for human experts to define and execute high-quality rubrics. We address this problem by proposing a scalable pipeline for generating high-quality rubrics without human experts in the final loop. We build a financial deep research benchmark from 104 real-world user queries and automatically synthesize 14,450 query-specific candidate rubrics from model-gen...

---

### 39. Speculate with Memory: Lossless Acceleration for LLM Agents

**Authors:** Yu Li, Qinyuan Ye, Prafulla Kumar Choubey, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12236v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12236v1)

**Summary:** Speculative execution accelerates LLM agents by using a smaller, cheaper model to predict and pre-launch the next step while the environment is idle. However, existing speculators are stateless and discard all information between tasks, preventing prediction quality from improving with experience. We equip the speculator with three online memory systems that learn from past agent trajectories: a contrastive transition table tracking action-sequence statistics, an episodic memory retrieving conte...

---

### 40. Fin-Analyst at FinMMEval 2026 Task 3: A Live Hybrid Trading Agent with LLM Specialists and Rule-Based Signals

**Authors:** Mohotarema Rashid, Lingzi Hong, Junhua Ding, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12233v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12233v1)

**Summary:** Large language model (LLM) trading agents show promising performance in equity markets, yet remain narrowly focused on US equities with little evidence from live deployment. We present Fin-Analyst, a hybrid agent for FinMMEval 2026 Task 3: an eight-specialist LLM pipeline over news, SEC filings, fundamentals, analyst forecasts, technical indicators, and social sentiment, aggregated by a Meta-Agent for Tesla (TSLA), and a lightweight rule based three-signal vote for Bitcoin (BTC). On the final of...

---

### 41. RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls

**Authors:** Brenda Lelis, Rodrigo Cabral-Carvalho

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12216v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12216v1)

**Summary:** Multi-agent and memory-augmented LLM systems often place coordination content, shared state, prior discussion, tool outputs, summaries, and role instructions, inside the same finite prompt used for the current task. This creates a practical allocation problem: every token spent on coordination is unavailable to task instructions or evidence when a call is assembled under a fixed context budget. We introduce the Roundtable Context Window Test (RCWT), a controlled protocol for measuring this task-...

---

### 42. Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives

**Authors:** Rasiq Hussain, Darshil Italiya, Joshua Oltmanns, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12215v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12215v1)

**Summary:** Accurately assessing personality from text is challenging because traits are latent, context-dependent, and often subtly expressed across long narratives. Large language models (LLMs) offer new opportunities by processing extensive textual contexts, but pretraining of these models can induce latent "personality-like" biases, making single-model inferences inconsistent. We propose a fine-tuned multi-agent framework for detecting OCEAN personality traits, in which sub-agents are conditioned to ado...

---

### 43. Comparing Semantic Navigation in Humans and Large Language Models using Natural Language Processing

**Authors:** Gabriel Paris-Colombo, Rodrigo M. Cabral-Carvalho, Felipe D. Toro-Hernández

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12195v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12195v1)

**Summary:** Semantic memory retrieval can be conceptualized as navigation through conceptual space. We compared semantic search dynamics between humans and three large language models (GPT-4o, Gemini-2.5-Pro, Claude-Sonnet-4.5) using verbal fluency data. By applying trajectory-based NLP metrics to the items generated by 82 human participants and LLM output across eight temperature settings, we quantified three complementary dimensions: entropy (step size predictability), distance to next (successive semanti...

---

### 44. Entropy in Semantic Memory Navigation in Blind and Sighted Individuals: The Effect of Visual Experience

**Authors:** Felipe D. Toro-Hernández, Rodrigo Lagos, Sergio E. Chaigneau

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12185v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12185v1)

**Summary:** Embodied accounts of semantic memory highlight the role of sensorimotor systems in acquiring and storing knowledge. Congenitally blind populations offer a critical test bed for these assumptions, providing an opportunity to assess whether conceptual grounding requires visual experience. In this study, we assessed semantic memory navigation differences between blind and sighted individuals using a property listing task with concrete and abstract concepts. We computed semantic entropy, an embeddin...

---

### 45. We Hebben Een Serieus Translatie: Modeling Intercomprehension as Probabilistic Inference

**Authors:** Thomas Hikaru Clark, Edward Gibson, Roger Levy

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12169v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12169v1)

**Summary:** Intercomprehension refers to partial intelligibility of an unfamiliar language (L2) by a speaker of a related language (L1). How is this zero-shot cross-language comprehension possible? In this work, we extend past work on algorithmic models of noisy-channel inference to model intercomprehension in a Bayesian framework. The model uses an LM in L1 only for scoring latent hypotheses about the translations of observed L2 utterances, and a general-purpose noise model to infer a mapping between L2 an...

---

### 46. Token Reduction Is Not Cost Reduction

**Authors:** Sarel Weinberger, Amir Hozez

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12161v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12161v1)

**Summary:** Context-reduction layers for API-based coding agents, including command-output compressors, retrieval rankers, and payload-optimizing proxies, are usually evaluated by how much text they remove. We ask instead: when does reducing retrieved context or tool output lower the actual billed cost of a coding agent without reducing task success or lengthening its trajectory?   Our primary evidence is a pre-specified, hash-frozen, paired campaign of 2,908 provider-billed Claude Code runs, of which 2,848...

---

### 47. CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform

**Authors:** Gustavo H. Santos, Aline Viana, Thiago H Silva

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12086v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12086v1)

**Summary:** Recent LLM-based multi-agent urban simulators can generate semantically rich city routines, but they remain costly to scale and are often weakly validated against empirical mobility patterns. We present CityBehavEx, an interactive LLM-assisted urban simulation platform that scales to city-size populations, exposes agent behavior for inspection, supports empirical validation, and generates mobility patterns that better match real-world spatial, temporal, and semantic distributions. Instead of inv...

---

### 48. The Capacity of Thought: Benchmarking Llama 3.2 in Semantic fMRI Neural Language Decoding and Improving the Huth Encoding-Model Baseline

**Authors:** Milos Suvakovic, Dom Marhoefer, Glenn Grant-Richards, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12079v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12079v1)

**Summary:** Decoding continuous language from fMRI signals remains a core challenge in non-invasive brain-computer interface research. We present two complementary investigations. First, we improve the Huth et al. ridge regression encoding pipeline through expanded voxel selection (10K->15K), substitution of GPT-2 medium for GPT-1 as the beam-search proposal model, and GPU-accelerated bootstrap training, achieving mean METEOR = 0.149 and BLEU-1 = 0.200 across three held-out narratives for subject UTS03 -- a...

---

### 49. Beyond Parallel Tracking: Interactive Multi-Feature Fusion Drives Semantic Reconstruction from Non-invasive Brain Recordings

**Authors:** Boda Xiao, Xiran Xu, Songyi Li, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12071v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12071v1)

**Summary:** Continuous semantic reconstruction from non-invasive neural recordings remains limited by the representational mismatch between semantic feature spaces and neural coding patterns, which severely impedes cross-modal alignment between high-noise neural signals and target semantic features. Prior semantic decoders have predominantly relied on static lexical representations or dynamic contextualized representations in isolation. This single-dimension approach inevitably leads to severe information l...

---

### 50. Agentic systems for breast cancer treatment recommendations

**Authors:** Vinicius Anjos de Almeida, Nícolas Henrique Borges, Leonardo Vicenzi, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12051v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12051v1)

**Summary:** Large language models (LLMs) are increasingly being explored for clinical decision support, but their reliability in complex oncology treatment planning remains unclear. We evaluated agentic LLM systems for breast cancer treatment recommendation generation using 72 real clinical cases across stages I to IV and 1,147 case-specific rubrics generated through Asymmetric Information Rubric Generation (AIRG), in which the rubric generator had access to real clinical decisions unavailable to the evalua...

---

## cs.CV

**50 papers**

### 1. The Seriality Gap in Video Diffusion Models

**Authors:** Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13031v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13031v1)

**Summary:** When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation largely disappears, isolating dependent-event structure rather than video length a...

---

### 2. FlowWAM: Optical Flow as a Unified Action Representation for World Action Models

**Authors:** Yixiang Chen, Peiyan Li, Yuan Xu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13017v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13017v1)

**Summary:** World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction. However, directly leveraging such video generators for control raises a new challenge: how to represent actions in a suitable form that aligns with pretrained video generators while carrying enough motion cues for accurate control. Existing numerical actions fail to satisfy the former, and prior visual action representations overlook the temporal motion structure across fram...

---

### 3. DermDepth: Toward Monocular Metric Scale 3D Reconstruction Models for Dermatology

**Authors:** Héctor Carrión, Narges Norouzi

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13010v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13010v1)

**Summary:** Dermatological practice routinely involves measuring and tracking lesion size, morphology and texture, as critical components of wound or skin cancer screening, monitoring and diagnosis. To accomplish this task, practitioners often image the skin surface with commonly available off-the-shelf camera sensors. This has led to an overwhelming research focus on 2D methods while these objectives naturally benefit from 3D information. In this paper, we demonstrate that dense monocular 3D reconstruction...

---

### 4. X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras

**Authors:** Heng Zhou, Shuhong Liu, Yonghao He, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12993v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12993v1)

**Summary:** We present X-lens, a compact feed-forward model for metric depth estimation from a variable number of calibrated fisheye and pinhole views. To support real-time downstream perception, X-lens is built around a geometry-aware heterogeneous camera formulation with two key components. Learnable calibration tokens provide a coarse alignment between fisheye and pinhole projective spaces, while a Jacobian-parameterized distortion bias injected into cross-attention models local projection changes and pr...

---

### 5. Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification

**Authors:** Héctor Carrión, Narges Norouzi

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12987v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12987v1)

**Summary:** Accurate dermatological diagnosis naturally necessitates equitable performance across diverse populations, yet a systematic lack of expertly annotated images, especially for underrepresented skin tones and rare diseases, impedes progress toward measurably fair methods. We introduce cgDDI (Controllable Generation of Diverse Dermatological Imagery), a hybrid framework that (1) synthesizes realistic healthy skin samples without disturbing other input properties, (2) maps single-sample rare lesions ...

---

### 6. ViCo3D: Empowering LiDAR-based Collaborative 3D Object Detection with Vision Foundation Models

**Authors:** Haojie Ren, Songrui Luo, Lingfeng Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12959v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12959v1)

**Summary:** LiDAR-based collaborative 3D perception in Vehicle-to-Everything (V2X) systems typically relies on fusing bird's-eye-view (BEV) features across agents. However, current BEV representations, typically extracted by LiDAR backbones trained from scratch, are geometry-dominated and lack general semantic priors, inherently limiting the efficacy of feature-level collaboration. Meanwhile, vision foundation models (VFMs) pretrained on large-scale image data have demonstrated strong capability in learning...

---

### 7. Point Tracking in Surgery--The 2025 Surgical Tattoos in Infrared Challenge (STIRC2025)

**Authors:** Adam Schmidt, Mert Asim Karaoglu, Zijian Wu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12939v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12939v1)

**Summary:** Point tracking in surgery is crucial to enable applications in downstream tasks such as segmentation, 3D reconstruction, virtual tissue landmarking, autonomous probe-based scanning, and subtask autonomy. This paper introduces the 2025 iteration of a point tracking challenge to address this, wherein participants submit their algorithms for quantification. Their algorithms are evaluated using a dataset named surgical tattoos in infrared (STIR), with the challenge named the STIR Challenge 2025 (STI...

---

### 8. Exact and Calibrated Diffusion Reconstruction for Digital Breast Tomosynthesis

**Authors:** Imade Bouftini

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12937v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12937v1)

**Summary:** Limited-angle digital breast tomosynthesis (DBT) reconstructs a volume from a few low-dose projections over a narrow arc. At a representative nine-view, $25^{\circ}$ protocol more than 98% of image space is unmeasured, so a learned prior must supply structure in the missing wedge. Conditional diffusion priors achieve strong perceptual quality here but leave three clinical obstacles: inexact data consistency, unlocalized hallucination, and uncalibrated uncertainty. We enforce measurements exactly...

---

### 9. Domain-Incremental Remote Sensing Change Detection via Difference-Guided Adaptation and Frequency-Decoupled Distillation

**Authors:** Daifeng Peng, Yaning Li, Haiyan Guan

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12934v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12934v1)

**Summary:** Remote sensing change detection (RSCD) models are prone to catastrophic forgetting when incrementally adapted to new domains. Existing domain-incremental learning (DIL) methods mainly preserve image-level representations but often overlook bitemporal discrepancy cues, which are critical for robust change detection under domain shifts. To address this limitation, we propose DG-FDD, a domain-incremental change detection framework that integrates Difference-Guided Adaptation and Frequency-Decoupled...

---

### 10. Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition

**Authors:** Bruce Coburn, Jingbo Yue, Jinge Ma, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12911v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12911v1)

**Summary:** Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find this premise no longer holds for current MLLMs. A modern MLLM's direct estimate now matches or surpasses the full retrieval pipeline. This raises a question: if retrieval no longer improves the overall estimate, can it still deliver the two things clinicians value, accurate portions and a traceable, ...

---

### 11. Real-time fall detection based on vision for low-power edge platforms

**Authors:** Wenjun Xia, Zhicheng Peng, Haopeng Li, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12909v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12909v1)

**Summary:** Falling detection is vital for elderly care and intelligent surveillance; however, prevailing vision-based approaches predominantly frame it as static pose classification or discrete temporal pattern matching, fundamentally overlooking the instability dynamics of the human support system. This paper proposes a physics-informed falling detection framework that recasts falling as a stability-loss event in a coupled dynamical system. We introduce a novel dual-LTC architecture comprising a Center-of...

---

### 12. Rank-1 Identity Consensus Predicts Gallery Enrollment in 1:N Face Matching More Accurately than Score Thresholding

**Authors:** Gabriella Pangelinan, Aman Bhatta, Michael C. King, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12903v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12903v1)

**Summary:** In operational 1:N face identification, a crucial question arises for each probe: is this person enrolled in the gallery or not? The stakes are high and asymmetric. Rejecting a mate-present (MP) probe loses a valid lead; accepting a mate-absent (MA) probe makes every returned candidate a false identification, at worst a wrongful arrest. Most approaches threshold match scores, but scores shift substantially with image quality and gallery size and composition, making thresholds fixed before deploy...

---

### 13. UniMedSeg: Unified In-Context Learning for Multi-Paradigm 2D/3D Medical Image Segmentation

**Authors:** Yunzhou Li, Jiesi Hu, Yanwu Yang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12896v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12896v1)

**Summary:** Medical image segmentation foundation models are expected to generalize across diverse clinical scenarios, yet existing universal methods remain fragmented by prompt paradigms and spatial dimensions. Visual in-context learning, interactive segmentation, and language-guided segmentation are typically handled by paradigm-specific models, while 2D and 3D images are also modeled separately. Such isolation prevents heterogeneous annotations and data from being jointly absorbed by a single scalable mo...

---

### 14. Hy-Embodied-VLM-1.0: Efficient Physical-World Agents

**Authors:** Ziyi Wang, Xumin Yu, Yongming Rao, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12894v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12894v1)

**Summary:** Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting with the physical world. In this report, we introduce Hy-Embodied-VLM-1.0, an efficient and powerful embodied foundation model specifically designed for embodied agents operating in the physical world. To cultivate such capabilities from the pre-training stage onward, we define an action-centric cap...

---

### 15. Inhibited Self-Attention: Sharpening Focus in Vision Transformers

**Authors:** Peter R. D. van der Wal, Nicola Strisciuglio, George Azzopardi

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12881v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12881v1)

**Summary:** Vision Transformers (ViTs) have demonstrated remarkable performance in computer vision tasks. However, their self-attention mechanism often diffuses focus across background regions, relying on spurious correlations rather than object-relevant cues. Inspired by inhibitory mechanisms observed in biological vision systems, we propose the Inhibited Self-Attention (ISA), a novel self-attention that integrates inhibitory signals to enhance feature selectivity and suppress spurious responses. In contra...

---

### 16. Metric-Guided Synthetic Image Data Rendering for Deep Learning compatible with Agentic AI

**Authors:** Martina Radoynova, Samuel Pantze, Trina De, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12874v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12874v1)

**Summary:** Deep learning computer vision for scientific applications requires collecting and annotating large datasets in a laborious, expensive and error-prone process. Synthetic data generation through 3D modelling and rendering may simplify this process and increase the accuracy of annotations by generating them programmatically. However, minimising the domain gap between real and synthetic images visually is subjective and lacks systematic quantitative guidance. We present GraNatPy, a Python package wi...

---

### 17. Statistical Non-linear Reconstruction Loss for Image Anomaly Detection

**Authors:** Nguyen Minh Tri, Hoang Khuong Duy, Huynh Cong Viet Ngu

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12866v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12866v1)

**Summary:** Reconstruction-based methods are a cornerstone of unsupervised image anomaly detection, but they remain vulnerable to \emph{outlier leakage}, where standard mean squared error (MSE) loss drives the model to faithfully reconstruct anomalous patterns. We propose a Non-linear Reconstruction Loss that applies a sigmoid-based squashing function to suppress high-magnitude features, preventing outliers from dominating optimization while preserving sensitivity to normal patterns. In addition, we introdu...

---

### 18. LARAD: Layout-Aware Road Anomaly Detection via Spatial-Logic Reasoning

**Authors:** Shiyi Mu, Xujie Chen, Shugong Xu

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12858v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12858v1)

**Summary:** Accurate open-world obstacle detection is critical for autonomous driving. Current anomaly segmentation methods suffer from a fundamental blind spot: they over-rely on texture novelty to identify out-of-distribution (OoD) objects while ignoring contextual spatial logic. Furthermore, mitigating the resulting false positives often requires cascading massive vision models, introducing unacceptable inference latency. To address these issues, we propose Layout-Aware Road Anomaly Detection (LARAD), sh...

---

### 19. AVSCap: Orchestrating Audio-Visual Synergy for Omni-modal Video Captioning

**Authors:** Yanghai Wang, Jiahao Wang, Jiafu Tang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12820v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12820v1)

**Summary:** Omni-modal video captioning is not merely combining visual captioning with audio transcription: a useful caption must describe how visual actions, speech, music, and sound effects co-evolve. Existing large multimodal models often fail at this relational step, treating audio and visual streams as loosely coupled observations, relying on automatic speech recognition, and under-specifying non-speech sounds and their links to visual events. We present AVSCap, a framework for audio-visual captioning ...

---

### 20. Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning

**Authors:** Sania Waheed, Michael Milford, Sarvapali D. Ramchurn, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12818v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12818v1)

**Summary:** Visual place recognition (VPR) is a key enabler of accurate localization and long-term autonomous navigation in robotics applications, such as loop closure detection for simultaneous localisation and mapping (SLAM). However, real-world VPR deployment relies on selecting an image matching threshold that balances precision and recall. These thresholds are typically tuned using labeled validation data and fixed during deployment, making them unreliable under environmental changes where ground truth...

---

### 21. UniVR: Thinking in Visual Space for Unified Visual Reasoning

**Authors:** Zhongwei Ren, Yunchao Wei, Yao Zhao, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12800v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12800v1)

**Summary:** Learning broad world knowledge directly from raw visual data is a fundamental capability of intelligence. We introduce UniVR, the first investigation into simultaneously learning complex reasoning, fine-grained physical dynamics, and long-term planning from pure visual demonstrations. At its core, UniVR features VR-GRPO, a reinforcement learning paradigm with complementary global and step-level rewards. This approach enforces logical coherence and physical consistency throughout the reasoning pr...

---

### 22. AVQ-Attention: Adaptive Vector-Quantized Attention

**Authors:** Winfried van den dool, Patrick Forré, Amir Habibian, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12789v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12789v1)

**Summary:** The $\mathcal{O}(N^2)$ complexity of attention over $N$ tokens remains a computational bottleneck in transformer models. Vector-Quantized (VQ) attention reduces this to $\mathcal{O}(MN)$ by representing keys with $M$ codewords, but applies uniform codebook capacity regardless of where attention mass concentrates: high-attention regions of key space may be coarsely approximated while low-attention regions waste representational capacity. We propose Adaptive Vector-Quantized (AVQ) Attention, which...

---

### 23. Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?

**Authors:** Kaiwen Zheng, Junchen Fu, Wenhao Deng, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12787v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12787v1)

**Summary:** Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on reso...

---

### 24. CoRe: A Comprehensive Framework for Cross-Image Comparative Reasoning in Vision-Language Models

**Authors:** Lin Peng, Cong Wan, Zeyu Guo, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12786v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12786v1)

**Summary:** Cross-image comparative reasoning remains challenging for vision-language models (VLMs), especially when correct prediction requires fine-grained attribute grounding and globally consistent reasoning. We present CoRe, a unified framework for this problem. CoRe includes: (i) CoRe-20K, a large-scale triplet-based training set automatically constructed from structured visual metadata through a multi-expert collaborative pipeline, covering counting, depth, distance, and spatial relations; (ii) TriSR...

---

### 25. ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting

**Authors:** Cheng-Tai Hsieh, Jiwei Shan, Han Fang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12785v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12785v1)

**Summary:** Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating beyo...

---

### 26. MBTI: A Multi-Branch Efficient Fine-Tuning Framework for Hyperspectral Image Classification with Foundation Models

**Authors:** Mingzhen Xu, Haonan Guo, Di Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12782v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12782v1)

**Summary:** Hyperspectral foundation models learn transferable spectral-spatial representations from large-scale unlabeled data. They provide an effective paradigm for adapting to downstream hyperspectral image (HSI) classification tasks with limited labeled samples. However, spectral band configurations vary substantially across sensors, which makes direct model transfer difficult. Existing adaptation strategies often compress, select, or reshape the original spectra to match model-specific input requireme...

---

### 27. HSEmotion Team at the 11th ABAW Challenge: Multi-Task Learning and Ambivalence/Hesitancy Video Recognition

**Authors:** Aleksei Bakin, Andrey V. Savchenko

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12774v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12774v1)

**Summary:** This article presents our results for the 11th Affective Behavior Analysis in-the-Wild (ABAW) competition. For multi-task learning with simultaneous prediction of valence, arousal, facial expressions, and action units on s-Aff-Wild2 dataset, we use frozen lightweight facial extractors, MT-EmotiDDAMFN and MT-EmotiEffNet-B0, with separate heads and systematic post-processing: temporal Gaussian smoothing, per-class expression bias, AffectNet blending, per-AU threshold tuning, and weighted backbone ...

---

### 28. EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval

**Authors:** Jiashi Lin, Changhong Jiang, Xiangru Lin, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12764v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12764v1)

**Summary:** Retrieval-augmented generation (RAG) has emerged as a critical paradigm for grounding Multimodal Large Language Models (MLLMs) in external knowledge. Recent GraphRAG methods introduce structured entity-relation graphs to improve retrieval and reasoning. However, they remain limited by treating knowledge graphs as static data structures built offline and queried in a single pass. This static paradigm misaligns with the interactive, iterative nature of knowledge-intensive reasoning, creating three...

---

### 29. VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression

**Authors:** Yupeng Zheng, Kai Zou, Bin Liu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12756v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12756v1)

**Summary:** Vision-language models (VLMs) process large numbers of visual tokens, resulting in substantial inference latency and memory overhead. This has motivated extensive research on visual token compression. While training-free strategies rely on heuristic metrics and suffer significant performance degradation under high compression ratios, many training-based methods introduce external compression modules that force the VLM backbone to adapt, incurring substantial retraining cost and compromising VLMs...

---

### 30. RFMSR: Residual Flow Matching for Image Super-Resolution

**Authors:** Shuwei Huang, Tianyao Luo, Jicheng Liu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12753v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12753v1)

**Summary:** Image super-resolution (ISR) has witnessed remarkable progress with diffusion models and flow matching. The dominant text-to-image (T2I) based approaches leverage large-scale foundation models as generative priors, achieving impressive perceptual quality but at the cost of massive model sizes and prohibitive training expenses. Recent flow-matching-based vision-only approaches have made significant strides; however, they adopt standard flow formulations that transport from a pure Gaussian prior t...

---

### 31. Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal Generation

**Authors:** Hongbo Wang, Huaibo Huang, Jie Cao, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12752v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12752v1)

**Summary:** While recent advances in 3D generation have enabled impressive visual synthesis, existing methods often rely on 2D diffusion supervision without explicit mechanisms for geometric consistency, leading to spatial hallucinations such as duplicated structures and misaligned geometry. These issues become more severe in 4D generation, where maintaining consistency across viewpoints and temporal evolution introduces additional challenges, including jitter, identity flicker, and structural drift. We pre...

---

### 32. CRC-HGD: A Histopathological Image Dataset for Grading Colorectal Cancer

**Authors:** Elham Amjadi, Amin Bahreini, Sayed Mohammad Hasan Emami, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12750v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12750v1)

**Summary:** Colorectal cancer (CRC) is the third most common cancer worldwide and the second leading cause of cancer-related deaths globally, with approximately 1,926,425 new cases and 904,019 deaths reported in 2022. Accurate histologic grading plays a critical role in prognosis and treatment planning for colorectal adenocarcinoma. In recent years, artificial intelligence and its subcategories, including machine learning and deep learning, have been increasingly employed for automated cancer detection and ...

---

### 33. Weakly Supervised Spatio-Temporal Candidate Discovery of Dairy Farm Sites from Seasonal Satellite Imagery

**Authors:** Usman Haider, Fatima Khalid, Karl Mason

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12748v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12748v1)

**Summary:** Farm site discovery from satellite imagery is a spatiotemporal candidate ranking problem because farm evidence is distributed across pasture, field boundaries, roads, buildings, and seasonal vegetation patterns. Direct farm labels are often incomplete, which makes fully supervised detection difficult. This paper proposes a weakly supervised pipeline for ranking dairy farm candidate clusters from seasonal Sentinel imagery and open map priors. The method uses aligned spring, summer, and autumn ima...

---

### 34. Color Pass-Through via Camera-Display Coupling

**Authors:** Ruikang Li, Molin Li, Jiarui Wu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12746v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12746v1)

**Summary:** When a real-world scene is captured by a smartphone camera and viewed on its screen, the displayed image often differs noticeably from the original scene in color, brightness, and contrast. This gap persists despite substantial advances in both modern cameras and displays. A key reason is that most pipelines factor the high-dimensional capture-to-display process into two separately calibrated camera and display stages, and then connect them through low-dimensional color transforms, leading to in...

---

### 35. Label-Decoupled Style Augmentation for Domain Generalization in Multi-Label Remote Sensing Scene Classification

**Authors:** Alaa Almouradi, Erchan Aptoula

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12704v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12704v1)

**Summary:** Multi-label classification assigns several co-occurring labels to each aerial scene, yet deployed models often encounter data distributions different from their training. Feature-statistics augmentation such as MixStyle, EFDMix, and correlated style uncertainty improves generalization at low cost but perturbs channel statistics globally, treating each image as a single style; one class can then contaminate the augmentation of another. Domain generalization is understudied for multi-label remote ...

---

### 36. Lesion Segmentation in Moderate to Severe Traumatic Brain Injury: An nnU-Net Based Approach with Adaptive Normalization in the AIMS-TBI 2025 Challenge

**Authors:** Inhwa Son, Gaeun Lee, Sohyeon Sim, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12684v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12684v1)

**Summary:** The segmentation of lesions in Moderate to Severe Traumatic Brain Injury (msTBI) from T1-weighted MRI presents a significant clinical challenge due to the profound heterogeneity of lesion characteristics in terms of size, shape, and location. To address this, the AIMS-TBI 2025 Challenge was organized to promote the development of robust and accurate segmentation algorithms. In this paper, we present our deep learning-based solution. Our methodology employs the nnU-Net framework with an adaptive ...

---

### 37. MambaPSA: A Mamba-based Replacement for C2PSA in YOLO26

**Authors:** Sheng-Wei Chan, Chia-Min Lin, Hsin-Jui Pan, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12681v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12681v1)

**Summary:** State space models (SSMs), notably Mamba, have recently emerged as efficient alternatives to self-attention with linear computational complexity. We investigate the integration of Mamba into YOLO26, the latest non-maximum suppression (NMS)-free object detection framework, by proposing MambaPSA, a lightweight Mamba-based replacement for the C2PSA block at the end of the backbone. To complement this study, we additionally insert a bidirectional Vision Mamba (BiViM) module at the P3, P4, and P5 lev...

---

### 38. ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning

**Authors:** Jiahang Wang, Yirong Yang, Yanqing Zhu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12680v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12680v1)

**Summary:** Existing vision-language navigation methods often couple a VLM with waypoint decoders to produce multi-step action plans, but they typically lack an explicit closed-loop mechanism for tracking semantic progress, diagnosing execution failures, and recovering from error accumulation in long-horizon navigation. To address this gap, we propose ReflectVLN, an agentic VLN framework that organizes decision-making through bidirectionally interactive intention and execution agents. The intention agent pe...

---

### 39. Text-Aided Multi-Modal Panoptic Symbol Spotting for CAD Floor Plan Drawings

**Authors:** Yan Gong, Bohao Li, Bowen Du, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12678v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12678v1)

**Summary:** Computer-Aided Design (CAD) floor plan drawings contain both graphical primitives and textual annotations, which provide complementary geometric and semantic cues for intelligent design understanding. Among CAD analysis tasks, panoptic symbol spotting has become increasingly important with the growing demand for industrial digitalization and deep learning-based automation. However, most existing methods remain primarily primitive-centric and underexploit textual annotations, despite their critic...

---

### 40. MAGE: Color-Invariant and Spatial Knowledge Distillation for Gastric Neoplasm Classification

**Authors:** Jiho Jun, Jeongwon Woo, Jaemin Song, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12663v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12663v1)

**Summary:** Accurate differentiation between gastric adenoma and carcinoma during endoscopy is critical for clinical decision-making. Yet, this task is highly challenging due to high inter-class similarity and ambiguous boundaries between the two classes. Existing ROI-based classification methods often suffer from detection/segmentation error propagation and loss of surrounding global context. In contrast, full-image classification lacks the necessary spatial focus. Furthermore, we observe that deep neural ...

---

### 41. Instance-Enriched Semantic Maps for Visual Language Navigation

**Authors:** Jiho Hong, Eunae Kang, Sanghyun Kim, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12630v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12630v1)

**Summary:** Visual Language Navigation (VLN) aims to enable an embodied agent to navigate complex environments by following natural language instructions. Recent approaches build semantic spatial maps and leverage Large Language Models (LLMs) for reasoning and decision making. Despite these advances, existing systems lack instance-level object detail and robustness to diverse user queries, limiting reliable navigation in complex indoor environments. To address these limitations, we propose Instance-Enriched...

---

### 42. KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill

**Authors:** Yunxin Li, Jinchao Li, Shibo Su, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12625v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12625v1)

**Summary:** OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism. These flaws limit its adaptation to diverse device ecosystems and prevent performance improvements through continuous learning from execution experience. To resolve these issues, we propose the Know Deeply, Act Perfectly paradigm for personal assistants, which holds that accumulated user interaction and task-run...

---

### 43. Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval

**Authors:** Ryotaro Shimada, Yu-Chieh Lin, Yuji Nozawa, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12621v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12621v1)

**Summary:** Recent work has shown that "Vision-Free'' approaches (representing images as text) can be effective for standard image retrieval tasks. However, it remains unclear whether this paradigm can effectively handle a more complex, multimodal task, Composed Image Retrieval (CIR), due to the inherent information loss in textual descriptions. In this paper, we introduce a Vision-Free CIR framework that addresses this challenge through two key techniques: (1) Attribute-Augmented Hybrid Scoring, which comp...

---

### 44. Decouple and Reason: Anatomically Guided Two-Stage Voxel-Level Grounding of Free-Text Findings in 3D Chest CT

**Authors:** Kwang-Hyun Uhm, Inhwa Son, Sung-Jea Ko

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12602v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12602v1)

**Summary:** Automatic voxel-level grounding of free-text findings in 3D chest Computed Tomography (CT) is critical for clinical interpretability. However, this task remains highly challenging due to the intricate spatial complexity of large 3D volumes and the heterogeneity of free-text findings. Existing end-to-end approaches often struggle to simultaneously learn the localized feature representations required for accurate 3D segmentation and the complex semantic understanding needed for text alignment, lea...

---

### 45. WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction

**Authors:** Li Hu, Guangyuan Wang, Peng Zhang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12592v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12592v1)

**Summary:** We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input. Prior generative game engines target either single-player first-person settings or non-real-time cooperative scenarios; multi-player control, real-time inference, complex physical interaction, and adversarial gameplay have not been jointly addressed. WanToFight closes this gap with three components built on the Wan-1.3B video diffusion transformer:...

---

### 46. Medical Image Segmentation based on Deep Active Contour and Mean Curvature Loss Function

**Authors:** Xiao-qiang Zhai, Zhi-feng Pang, Peng Zheng, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12586v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12586v1)

**Summary:** Medical image segmentation is a crucial task in the field of clinical analysis and applications. Though deep learning techniques recently play a crucial role in several scenarios, the training at the individual pixel level leads to a lack of geometric prior information. Scholars proposed to integrate the Chan-Vese model into the loss function for training which can take into account the region and length of the region inside and outside the segmentation process and then improve the performance i...

---

### 47. Traceback Translators Against Forgetting in Continual Fake Speech Detection

**Authors:** Enrico Gottardis, Mattia Tamiazzo, Simone Milani

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12569v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12569v1)

**Summary:** Fake speech detectors are increasingly challenged by the development of new and more accurate generative models. To cope with this problem, continual learning techniques are nowadays widely considered feasible strategies for updating models to new datasets, but they also lead to decreased performance on previously seen samples (catastrophic forgetting). In this work, we propose a forgetting-resilient solution based on the adoption of domain translators within a frozen detector, which remaps the ...

---

### 48. Gaussian Mixture Modeling for Event-Aware Visual Allocation in Long Video Understanding

**Authors:** Yifan Lu, Ziqi Zhang, Chunfeng Yuan, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12557v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12557v1)

**Summary:** Large Vision-Language Models (LVLMs) face significant challenges in long video understanding due to the excessive computational cost and information loss associated with uniform sampling. Existing keyframe selection methods often treat video frames as atomic entities and allocate visual budgets equally, thereby overlooking high-level semantic structures and introducing substantial redundancy. To address these limitations, we propose GMM-EVA (Gaussian Mixture Modeling for Event-Aware Visual Alloc...

---

### 49. CGRL: Concept-Guided Pruning and Representation Learning for Whole-Slide Image Classification

**Authors:** Thuc Huynh, Tuan Le, Doanh C. Bui

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12556v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12556v1)

**Summary:** Weakly supervised whole-slide image (WSI) classification is widely used in computational pathology because slide-level labels are easier to obtain than dense region annotations. Existing multiple instance learning (MIL) methods often aggregate large bags of patch embeddings using mainly visual cues, which can retain many non-informative patches and provide weak alignment between instance features and class-level disease semantics. We propose Concept-Guided Pruning and Representation Learning (CG...

---

### 50. VanillaBench: The Hidden Accuracy Cost of Adversarial Robustness

**Authors:** Niklas Bunzel

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12545v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12545v1)

**Summary:** Adversarial robustness research has produced hundreds of defended models over the past decade, yet the literature almost universally reports robustness results in isolation: standard (clean) accuracy and adversarial accuracy of the robust model are shown, but the gap to the corresponding vanilla model is rarely quantified. We introduce VanillaBench, a systematic benchmark that makes this gap explicit. For every adversarially-trained model catalogued by RobustBench across four threat models, we c...

---

## cs.LG

**50 papers**

### 1. The Seriality Gap in Video Diffusion Models

**Authors:** Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13031v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13031v1)

**Summary:** When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation largely disappears, isolating dependent-event structure rather than video length a...

---

### 2. TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

**Authors:** Zhouchonghao Wu, Akshay Rangesh, Weixin Li, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13028v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13028v1)

**Summary:** Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per se...

---

### 3. A Shortcut to Statistically Steady-State Turbulence with Flow Matching

**Authors:** Gianluca Galletti, Gerald Gutenbrunner, William Hornsby, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13022v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13022v1)

**Summary:** Many nonlinear physical systems exhibit an initial transient phase in which perturbations grow before nonlinear interactions lead to a statistically steady state. While this saturated regime is of primary interest, direct numerical simulations must resolve the full transient dynamics before reaching it, incurring significant computational cost. In Computational Fluid Dynamics, reduced-order approaches such as Large Eddy Simulation mitigate computational cost by modeling small-scale dynamics, ena...

---

### 4. The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting

**Authors:** Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13006v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13006v1)

**Summary:** A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longer lookback, a retrieval plug-in, or a pretrained model, will help. These are not the same question. The value of context is a property of the operating point, not of the series. Any index built from the power spectrum is invariant under phase randomization, whereas the beyond-second-order value that...

---

### 5. Watermark Forensics for Generative Models: An Information-Theoretic Perspective

**Authors:** Xiaoyu Li, Zheng Gao, Xiaoyan Feng, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.13003v1) | 📄 [PDF](https://arxiv.org/pdf/2607.13003v1)

**Summary:** A watermark in a generative model's output is usually asked only whether a text is machine-made. The same mark can do more: attribute it to the user who produced it, extract a hidden payload, or localize the part that survives editing. These form a forensic ladder, and we ask what each rung costs in the sample length $n$.   One object organizes the answers. Let $S$ be the secret the mark carries (a user's identity or payload), and let the information profile $ν(t)=I(S;X_t\mid X_{<t})$ record how...

---

### 6. Ensemble Controlled-Flow Filtering for Implicit Data Assimilation

**Authors:** Zhuoyuan Li, Yue Zhao, Ming Li

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12975v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12975v1)

**Summary:** Data assimilation estimates the state of a dynamical system from model forecasts and incoming observations. Many observation mechanisms, however, are many-to-one, implicit, non-smooth, or accessible only through simulation, and need not provide the residual structures or likelihood guidance required by existing ensemble filters. We introduce implicit data assimilation, in which the analysis law is defined as an energy tilt of the forecast distribution. We then propose the Ensemble Controlled-flo...

---

### 7. Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models

**Authors:** Mehmet Iscan

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12962v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12962v1)

**Summary:** Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature. We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generated code can be used operationally by that same model. In PoPE, error content is p...

---

### 8. Robustness of Deep Learning Models for PV Power Forecasting under NWP Forecast Errors: A Spatiotemporal and Physically Interpretable Analysis

**Authors:** Dandan Chen, Yan Zhao, Xuepeng Chen

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12954v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12954v1)

**Summary:** Engineering use of AI forecasting models requires not only high nominal accuracy but also predictable behavior under uncertain inputs. In photovoltaic (PV) forecasting, this requirement is especially challenging because numerical weather prediction (NWP) errors are temporally correlated, state dependent, and physically coupled across variables. Existing evaluations, however, often rely on perfect forecast assumptions or simplistic perturbations that do not reflect these characteristics. This stu...

---

### 9. Efficient Sequential Calibration with $O(T^{2/3-ε})$ Error Bound

**Authors:** Zihan Zhang

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12928v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12928v1)

**Summary:** We study the online binary sequential calibration problem. A recent breakthrough by \citet{dagan2024breaking} overcomes the classical \(T^{2/3}\) barrier for calibration error. Building on this result, we present an efficient randomized forecaster that achieves an expected calibration error \(O(T^{2/3-\varepsilon})\) for some constant \(\varepsilon>0\).   Our forecaster combines the \textsc{SPR-Calibration} procedure \citep{dagan2024breaking} with an outer Blackwell-style correction layer. The \...

---

### 10. LatentFlow: A General Framework for Conditioning Stochastic Processes

**Authors:** Louis Sharrock, Lachlan Astfalck, Henry Moss

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12922v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12922v1)

**Summary:** Stochastic-process models are, as a rule, far easier to simulate than to condition. Non-linear observations, non-Gaussian likelihoods, black-box information, and global constraints all induce intractable conditional laws, requiring bespoke, model-specific constructions. We introduce LatentFlow, a single framework for conditioning stochastic processes, with no learned neural approximations and no training. Our starting point is to write the stochastic process as the deterministic image of a tract...

---

### 11. Contrastive-Collapsed Loss for Flexible and Geometrically Optimal Embeddings and Faster Convergence

**Authors:** Blanca Cano-Camarero, Ángela Fernández-Pascual, José R. Dorronsoro

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12916v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12916v1)

**Summary:** In this work, we introduce CoCo, a loss function aimed at learning normalized and well-structured representations. The proposed loss encourages intra-class collapse and inter-class contrast while preserving sufficient flexibility for neural networks to approximate geometrically optimal embeddings with large angular separation between classes. We provide a theoretical analysis positioning CoCo with respect to related objectives such as dot regression and cross-entropy, showing that the new propos...

---

### 12. Accelerated Mixing Time of Randomized Hamiltonian Monte Carlo

**Authors:** Siddharth Mitra, Vishwak Srinivasan, Xiuyuan Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12902v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12902v1)

**Summary:** We show the Randomized Hamiltonian Monte Carlo (RHMC) algorithm has accelerated mixing time guarantees for sampling from log-concave probability distributions. RHMC proceeds by repeatedly simulating the continuous-time Hamiltonian dynamics for some random integration times, and resetting the velocity to be an independent Gaussian random variable between each simulation. We show that when the target distribution is log-concave and satisfies an $α$-Talagrand inequality (for example, if the target ...

---

### 13. Energy-Based Physics-Informed Form Finding for Clustered Tensegrity Structures

**Authors:** Jing Qin, Muhao Chen

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12888v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12888v1)

**Summary:** Tensegrity form-finding and physical property prediction are fundamental inverse problems in structural mechanics, which aim to determine equilibrium configurations and internal force distributions. These problems are challenging due to strong nonlinearity arising from the coupling between geometry and forces, the need to ensure structural stability, and the enforcement of constraints such as boundary conditions and symmetry. Moreover, traditional methods often lack robustness to noise and outli...

---

### 14. Deep4ge: DNN Training Trajectories for Fault Detection and Diagnosis

**Authors:** Sigma Jahan

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12868v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12868v1)

**Summary:** Deep learning systems often fail due to subtle implementation faults that alter training behavior. Recent work has studied how to detect and diagnose such failures from changes observed across training epochs. However, the software engineering community still lacks a public dataset of per-epoch training runs with documented fault history, feature extraction details, and clear reuse support for fault detection and diagnosis tasks. We present Deep4ge, a controlled benchmark of 14,227 training runs...

---

### 15. Toward Localizing and Repairing Bias in Transformer Attention Heads

**Authors:** Sigma Jahan

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12863v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12863v1)

**Summary:** Transformer language models are increasingly used as software components, yet biased outputs remain difficult to localize and repair inside the model. Existing fairness testing and repair methods largely operate at the input-output or retraining level, while recent work suggests that bias-related behavior can concentrate in a small set of attention heads. This paper studies whether attention heads can be localized and repaired through a targeted inference-time intervention. We introduce ROBIN, a...

---

### 16. Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control

**Authors:** Takumi Shioda, Kohei Terashima, Tatsuo Nagai

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12856v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12856v1)

**Summary:** Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constraints. Model predictive control (MPC) and reinforcement learning are difficult to scale across buildings. This study instead adapts an open-weight reasoning model through reinforcement learning with verifiable rewards (RLVR). We convert exact offline dynamic-programming (DP) action values into dense...

---

### 17. Reproducible Reservoir Computing with Thermally Driven Superparamagnets: Controlling Temperature Sensitivity

**Authors:** Zhengfei Chen, Alex Welbourne, Matthew O. A. Ellis, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12840v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12840v1)

**Summary:** Unconventional computing systems must demonstrate robust performance under real-world environmental conditions to enable practical deployments. We have recently proposed superparamagnetic nanodot ensembles driven by strain-induced magnetoelectric coupling as exciting candidates for use as ultra-low energy consumption reservoir computing substrates. However, because their dynamics are governed by thermal activation effects, these systems are intrinsically sensitive to ambient temperature fluctuat...

---

### 18. ANGLE: Angular Neural Generative Learning via Engression

**Authors:** Rajdeep Pathak, Archi Roy, Tanujit Chakraborty

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12833v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12833v1)

**Summary:** Circular data, representing angles or directions, are frequently encountered in computer vision, biology, geology, and meteorology. Traditional regression targets the conditional mean, which is often geometrically misleading for circular responses under multimodal, skewed, or asymmetric data structures. To address these limitations, a lightweight deep generative framework, namely ANGLE, is introduced for non-parametric distributional regression on the circle. The full conditional distribution of...

---

### 19. Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques

**Authors:** Daehoon Gwak, Minhyung Lee, Junwoo Park, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12829v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12829v1)

**Summary:** Diffusion large language models (dLLMs) offer a theoretical advantage in parallel generation over standard autoregressive models. However, parallel generation alone does not guarantee practical speedups. Realizing this efficiency requires specialized inference mechanisms, such as diffusion-aware caching and reuse. Consequently, as inference efficiency becomes a prerequisite for practical deployment, recent research has actively explored acceleration techniques across algorithms, architectures, a...

---

### 20. AVQ-Attention: Adaptive Vector-Quantized Attention

**Authors:** Winfried van den dool, Patrick Forré, Amir Habibian, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12789v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12789v1)

**Summary:** The $\mathcal{O}(N^2)$ complexity of attention over $N$ tokens remains a computational bottleneck in transformer models. Vector-Quantized (VQ) attention reduces this to $\mathcal{O}(MN)$ by representing keys with $M$ codewords, but applies uniform codebook capacity regardless of where attention mass concentrates: high-attention regions of key space may be coarsely approximated while low-attention regions waste representational capacity. We propose Adaptive Vector-Quantized (AVQ) Attention, which...

---

### 21. Directional Constraints for Efficient Exploration in Safe Reinforcement Learning

**Authors:** Paolo Magliano, Puze Liu, Jan Peters, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12784v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12784v1)

**Summary:** Reinforcement Learning has revolutionized the landscape of robotic research, allowing robust learning of complex robotic skills in simulation. However, real-world deployment in open-ended environments requires strong safety guarantees to prevent dangerous or harmful behaviors. Safe Reinforcement Learning methods address this requirement by enforcing safety constraints. Nevertheless, learning under constraints often reduces learning speed and could lead to suboptimal task performance, as the agen...

---

### 22. Learning-enabled Acceleration of Scenario-based Model Predictive Control

**Authors:** Trinh Tran, Binh Nguyen, Truong X. Nghiem

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12775v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12775v1)

**Summary:** Scenario-based model predictive control (SBMPC) is a variant of model predictive control (MPC) that explicitly accounts for uncertainty by optimizing control actions over multiple predicted scenarios. However, its computational complexity increases rapidly with the number of scenarios and prediction horizon, limiting is applicability to real-time planning and control. This paper presents a learning-accelerated Alternating Direction Method of Multipliers (ADMM) algorithm for efficiently solving S...

---

### 23. Learning Mechanistic Reasoning for Chemical Reactions with Large Language Models

**Authors:** Xingyu Dang, Haocheng Tang, Junmei Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12771v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12771v1)

**Summary:** Reaction mechanisms consist of the step-by-step sequences of elementary reactions that explain chemical transformations. Learning the mechanism logic is therefore essential for enhancing the fundamental chemical intelligence of large language models (LLMs). The stepwise deduction of reaction mechanism aligns naturally with the reasoning paradigms of reasoning LLMs. However, current chemical LLMs primarily emphasize coarse-grained name reactions for product prediction and retrosynthesis, often le...

---

### 24. Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination

**Authors:** Usman Haider, Karl Mason

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12763v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12763v1)

**Summary:** Federated Reinforcement Learning (FedRL) enables coordination of distributed energy resources without sharing raw local data, but standard aggregation methods such as FedAvg do not account for system-level constraints, often leading to unsafe global behavior. In this work, we study constraint-aware aggregation for federated reinforcement learning in distributed energy coordination. We propose aggregation rules that incorporate both local performance and estimated constraint violation into the se...

---

### 25. What Makes a Representational Prior Work? Feature Families, Label-Free Invariances, and Critical Windows in Grokking

**Authors:** Gunner Levi Howe

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12735v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12735v1)

**Summary:** Companion work showed the grokking delay is causally the time to form task-structured representations, injectable via a contrastive prior. Here we characterize what makes such a prior work, across four axes, in 188 new runs. Content: a coherent, learnable prior built from the wrong feature family (magnitude bands) blocks generalization like a random partition (1/15 vs 0/20 grok; $p=0.43$ between them), confirming the companion's prediction that priors act at the level of the circuit's features. ...

---

### 26. LLMs Can See the Smoke but not the Fire: Evaluating Abductive Reasoning with Elenchos

**Authors:** Julius Steiglechner, Lucas Mahler, Gabriele Lohmann

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12733v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12733v1)

**Summary:** Large language models (LLMs) excel at pattern recognition and text generation, but their capacity for abductive inference - inferring latent hypotheses that explain observed behavior - remains poorly understood. Here, we introduce Elenchos (named after the Socratic method of cross-examination), a generative evaluation framework that measures abductive reasoning as a structural inverse problem. Given a reference formal system, such as the lambda-calculus, and a potentially mutated counterpart, ag...

---

### 27. Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty

**Authors:** Sarah Al-Shareeda, Gulcihan Ozdemir, Heung Seok Jeon

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12730v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12730v1)

**Summary:** Smart-building load forecasters are often trained offline on dense, multivariate, high-frequency data, but deployment may provide only hourly, feature-limited inputs. Missing features must then be reconstructed, and their errors can propagate through the model. If this input uncertainty is not reflected, prediction intervals may become miscalibrated, affecting demand-response scheduling. Our work examines where uncertainty should be placed once inference inputs are reconstructed. We develop a un...

---

### 28. Physically Consistent Parameter Inference: Transparent Machine Learning Emulation in High Energy Physics and Cosmology

**Authors:** Jorge Alda, Jacobo Asorey, Alejandro Mir, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12726v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12726v1)

**Summary:** Global fits in high energy physics and cosmology often face the challenge of exploring high-dimensional parameter spaces with computationally expensive or topologically complex likelihood functions. In this work, we present a Machine Learning framework designed to emulate complex, often non-Gaussian likelihood landscapes using gradient-boosted regression trees (XGBoost). We discuss the advantages of the Machine Learning approach in terms of computational efficiency and the resolution of confiden...

---

### 29. Label-Decoupled Style Augmentation for Domain Generalization in Multi-Label Remote Sensing Scene Classification

**Authors:** Alaa Almouradi, Erchan Aptoula

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12704v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12704v1)

**Summary:** Multi-label classification assigns several co-occurring labels to each aerial scene, yet deployed models often encounter data distributions different from their training. Feature-statistics augmentation such as MixStyle, EFDMix, and correlated style uncertainty improves generalization at low cost but perturbs channel statistics globally, treating each image as a single style; one class can then contaminate the augmentation of another. Domain generalization is understudied for multi-label remote ...

---

### 30. Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

**Authors:** Junyu Ren

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12650v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12650v1)

**Summary:** Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny. We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts. Every verified output structurally descends from an attested tool call (Thm. 3.1) and...

---

### 31. Extractable Memorization From First Principles

**Authors:** A. Feder Cooper, Marika Swanberg, Jamie Hayes, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12649v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12649v1)

**Summary:** Recent work on extractable memorization in LLMs suffers from two contrasting validity problems. Some studies overstate extraction, e.g., relying on sequences too short to distinguish memorization from predictability. Others imply that extraction is unreliable evidence of memorization, since models can also reproduce real-world text they weren't explicitly trained on. In different ways, both overlook what makes a valid extraction claim: the model must generate a training sequence with high enough...

---

### 32. AdaPCLA: Adaptive Prior-Calibrated Logit Adjustment for Long-Tailed Longitudinal EHR Generation

**Authors:** Shuai Cui, Chen Wenxuan, Wenjie Du, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12645v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12645v1)

**Summary:** Generative modeling of longitudinal Electronic Health Records is increasingly important for privacy-preserving research, yet standard autoregressive models tend to underrepresent the co-occurrence structure of tail events (i.e., diseases, symptoms), reducing the fidelity and faithfulness of generated data for rare subpopulations. To this end, we propose AdaPCLA framework, which enables generative models to adaptively fit and generate EHR data through a data distribution-aware training strategy; ...

---

### 33. Learning Forced Multibody Dynamics on Lie Groups

**Authors:** Martine Dyring Hansen, Marta Ghirardelli, Elena Celledoni, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12627v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12627v1)

**Summary:** We propose an architecture for learning the dynamics of mechanical systems based on discrete forced Euler-Lagrange equations on Lie groups using only position data. By formulating the dynamics directly on manifold-valued configuration spaces, the method naturally respects the geometric structure of the systems and preserves geometric invariants and conservation laws. The reliance on position measurements alone makes the framework applicable in settings where velocity data are unavailable or nois...

---

### 34. Gradient-free learning of a closed-loop wall controller for turbulent drag reduction

**Authors:** Giorgio Maria Cavallazzi, Miguel Pérez Cuadrado, Alfredo Pinelli

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12626v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12626v1)

**Summary:** Closed-loop wall control learnt by multi-agent reinforcement learning can lower skin-friction drag in turbulent channels, but these gradient-based policies are trained on small periodic boxes and exhibit reduced performance when carried over to a larger domain. We recently showed that such policies are also prone to saturated bang-bang actuations that collapse into standing streamwise waves whose scale is set by the computational box rather than by the near-wall cycle, and proposed architectural...

---

### 35. The Geometry of Memorization: Finite-Time Spectral Sensitivity as a Diagnostic for Flow Matching Models

**Authors:** Shuchan Wang

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12616v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12616v1)

**Summary:** Continuous-time generative frameworks construct probability paths between base and target domains by optimizing time-dependent velocity fields. While theoretical targets favor straight trajectories, empirical networks develop complex path deformations. This paper presents the Finite-Time Spectral Sensitivity (FTSS) g(t), a gradient-free, forward-pass metric that exposes flow geometry by tracking the root-mean-square singular value of the state-transition matrix. Serving as a continuous proxy for...

---

### 36. Lightweight Multi-Scale Anomaly Detection for Resource-Constrained Edge Devices

**Authors:** Raheen Junaid Wani, Smruti R. Sarangi

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12599v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12599v1)

**Summary:** Time-series anomaly detection is increasingly important in IoT systems, sensor networks, and edge monitoring applications, where models must operate under strict constraints on memory, latency, and power consumption. While recent deep-learning approaches have improved detection accuracy, many remain computationally expensive and often fail to capture subtle anomalies due to limited multi-scale sensitivity. Autoencoders are widely used for anomaly detection because they reconstruct normal pattern...

---

### 37. Environment Parameter Gradient Theorem for Policy-Environment Co-Design in Reinforcement Learning

**Authors:** Amber Srivastava

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12590v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12590v1)

**Summary:** Reinforcement learning (RL) is traditionally concerned with learning a control policy for a fixed environment. In many engineering systems, however, the environment itself is alterable: physical or operational parameters can be tuned to shape the transition dynamics and costs experienced by the agent. This motivates jointly optimizing both the policy and the environment design parameters. To this end, we establish an Environment Parameter Gradient Theorem -- a formal expression for the gradient ...

---

### 38. Deep Learning-based Surrogate Modelling of the LOD Method for Multiscale Problems

**Authors:** Marc Haltmayer, Jaemin Seo, Yuseung Lee, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12570v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12570v1)

**Summary:** Multiscale problems are notoriously difficult to tackle using traditional numerical methods, as accurately resolving fine-scale features often requires prohibitively fine discretizations. This challenge is particularly pronounced in applications such as materials science, fluid dynamics, climate systems, chemical processes, and complex networks. Recent neural operator models provide a promising data-driven alternative, but frequently struggle to achieve sufficient accuracy in the presence of str...

---

### 39. A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs

**Authors:** Rahul Krishnan, Volker Schulz

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12550v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12550v1)

**Summary:** The key-value (KV) cache has become the dominant memory cost of transformer inference. It grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the ceiling on throughput. Two families of methods reduce it. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither family exploits the fact that the cache at a layer i...

---

### 40. Mind the Gap: Promises and Pitfalls of Hierarchical Planning in LeWorldModel

**Authors:** Niccolò Caselli, Salvatore Lo Sardo, Francesco Massafra, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12547v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12547v1)

**Summary:** We investigate whether temporal hierarchy can improve LeWorldModel on long-horizon goal-conditioned control. We introduce Hi-LeWM, an extension that freezes the pretrained low-level LeWM and adds high-level planning over latent subgoals. We evaluate Hi-LeWM on PushT and Cube across increasing goal offsets. Hierarchy does not automatically improve performance: at short horizons, the best configuration uses a one-step high-level horizon, while longer horizons reveal a mismatch between the learned ...

---

### 41. From Preimage Search To Source-Grounded Feature Inversion

**Authors:** Kaixiang Shu

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12526v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12526v1)

**Summary:** Interpreting a neural network requires understanding what its internal features extract from a particular input. Feature inversion seeks to express a selected feature in the input domain, but canonical iterative methods search for an input whose re-encoded representation matches the target. Because many inputs can satisfy this constraint, target matching alone does not specify the inverse associated with the sample that generated the feature. We formulate source-grounded feature inversion by con...

---

### 42. OOD-RL-Bench: A Benchmark Framework for Out-of-Distribution Detection in Reinforcement Learning

**Authors:** Emil Mittag, Richard Dazeley, Peter Vamplew

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12523v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12523v1)

**Summary:** Reliable reinforcement learning (RL) agents must maintain operational integrity amidst sensor malfunctions, dynamic disturbances, and slow environmental shifts. The detection of out-of-distribution conditions is pivotal to determining when an agent's observations, transitions, or trajectory dynamics deviate from the assumptions underpinning its policy training. Current out-of-distribution (OOD) detection benchmarks typically evaluate image classifiers or static low-dimensional datasets, failing ...

---

### 43. What Does Goodness Measure? A Likelihood-Ratio Account of Forward-Forward Learning

**Authors:** Paolo Giannitrapani

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12501v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12501v1)

**Summary:** The Forward-Forward (FF) algorithm trains each layer locally, so that a scalar goodness - the sum of squared activations - is high on real inputs and low on contrastive ones, with activations normalized between layers. Both choices are usually treated as heuristics. Under an explicit generative model they are not: the squared goodness is the sufficient statistic of a likelihood-ratio test between two zero-mean populations differing in scale, and the FF threshold is its boundary. It generalizes: ...

---

### 44. Adversarial Attacks on Online Handwriting using Salience-based Temporal Editing

**Authors:** Yataro Tamura, Brian Kenji Iwana, Jiseok Lee

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12500v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12500v1)

**Summary:** Deep learning models for online handwriting recognition have been shown effective and are increasingly deployed in practical applications. However, their vulnerability to adversarial attacks is still a challenge. Existing adversarial methods are predominantly designed for image-based inputs and typically rely on additive spatial perturbations. When applied to online handwriting, which is inherently represented as a time series of pen trajectories, such perturbations often introduce high-frequenc...

---

### 45. Sample Efficient Generative Optimization for Molecular Design

**Authors:** Sarina Kopf, Cristina Nevado, Philippe Schwaller

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12488v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12488v1)

**Summary:** Molecular optimization in drug discovery, materials design, and catalysis requires searching vast chemical spaces under tight evaluation budgets, since high-fidelity oracles and experimental measurements are costly. The practical impact of an optimization method therefore hinges on its sample efficiency: how few evaluations it needs to find strong candidates. We introduce Sample Efficient Generative Optimization (SEGO), a framework for Bayesian optimization on adaptively generated molecules. In ...

---

### 46. Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Medical Classification

**Authors:** Jeeyung Kim, Erfan Esmaeili, Qiang Qiu

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12464v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12464v1)

**Summary:** When labeled data are scarce, off-the-shelf diffusion models can augment training sets for few-shot medical image classification, but not all generated samples are equally useful for the downstream task. Existing approaches largely improve synthetic data by increasing realism, diversity, or domain adaptation, while overlooking a more fundamental question: how should sample usefulness for classification be measured and optimized? We address this with Class-Contrastive Influence (C2I), a criterion...

---

### 47. Exploring Zero-Shot Foundation Models for Multivariate Time Series Anomaly Detection

**Authors:** Martin Uray, Saverio Messineo, Roland Kwitt, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12454v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12454v1)

**Summary:** Multivariate Time Series Anomaly Detection (MTSAD) is essential for reliability and safety in domains such as industrial process monitoring and financial risk management, yet conventional approaches rely on application-specific models that are costly to train and hard to scale. Foundation Models (FMs), pre-trained on broad data with strong zero-shot generalization, have recently become available for univariate time series forecasting, raising the question of whether they can address MTSAD withou...

---

### 48. The Computational Basis of Confidence in Large Language Models

**Authors:** Dharshan Kumaran, Viorica Patraucean, Maks Ovsanikov, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12447v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12447v1)

**Summary:** Reliable confidence -- the probability that a model's own answer is correct -- is essential for the trustworthy deployment of language models. Existing work has largely evaluated confidence by how well it predicts correctness and whether it is calibrated, leaving open a more fundamental question: what does the confidence signal itself represent? Answer logits may reflect a latent decision variable sufficient to compute normative confidence, or instead a heuristic preference signal that combines ...

---

### 49. Language Identification with Succinct Machine-Independent Traces

**Authors:** Moses Charikar, Jon Kleinberg, Chirag Pabbaraju

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12443v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12443v1)

**Summary:** Motivated by the power of large language models, there has been renewed interest in the Gold-Angluin model of language identification in the limit, with an eye toward variants of the model that might overcome the negative results for its original formulation. Recent papers on this question have proposed looking at computational traces and annotations of training strings as a source of additional power for a learner, reflecting empirical regularities such as the way that commented source code is ...

---

### 50. Fisher Rank Inflation: A Spectral Signature of Memorization under Label Noise

**Authors:** Satwik Bathula, Anand A. Joshi

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12438v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12438v1)

**Summary:** Deep networks trained with label noise often learn clean structure before memorizing corrupted labels. We show that this transition leaves a spectral signature in the centered scatter of per-example last-layer gradients. Its effective rank transiently expands during memorization and contracts after corrupted labels are fit. We call this phenomenon Fisher Rank Inflation. Corrupted labels increase effective rank by injecting spectral mass into low-energy or previously unused eigendirections, incre...

---

## cs.NE

**50 papers**

### 1. A 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding

**Authors:** Narayanan Shyam, Saptarshi Ghosh, Giacomo Indiveri

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12901v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12901v1)

**Summary:** Low-power event-based Analog Front-Ends (AFEs) are essential for building efficient, end-to-end neuromorphic signal processing systems. In this paper, we present an event-based AFE Application-Specific Integrated Circuit (ASIC) optimized for biomedical signal acquisition and encoding. The chip features 32 independently programmable input channels with dual-mode encoding mechanism outputs, comprising Pulse Frequency Modulation (PFM) and adaptive Asynchronous Delta Modulator (aADM) circuits. The a...

---

### 2. Structured Fluctuations and the Information Dynamics of Self-Maintenance in Growing Neural Cellular Automata

**Authors:** Atsushi Masumori, Hiroki Sato, Takashi Ikegami

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12403v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12403v1)

**Summary:** Growing Neural Cellular Automata (GNCA) are capable of robust self-maintenance and self-repair, yet the internal dynamical mechanisms that support these capabilities remain poorly understood. Here, we investigate the role of internal fluctuations--temporal micro-variability of hidden channel states--in a trained GNCA model, challenging the assumption that such variability is merely residual stochastic noise. Through systematic analysis spanning update-rate sweeps, spatial correlation measurement...

---

### 3. A new dual-population constrained multi-objective evolutionary optimization algorithm with repair constraint handling for structural optimization

**Authors:** Fardad Homafar, Jasmin Jelovica

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12240v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12240v1)

**Summary:** Structural optimization problems often involve a large number of decision variables and highly non-convex feasible regions, making convergence to the true Pareto front extremely challenging. Even when convergence is achievable, it typically requires thousands of function evaluations, resulting in significant computational cost. This highlights the need for efficient and robust optimization algorithms for real-world engineering applications. In this study, we introduce a novel constrained multi-o...

---

### 4. Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search

**Authors:** Romain Amigon

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11826v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11826v1)

**Summary:** Neural Architecture Search (NAS) has automated the design of deep learning models but traditionally requires massive computational resources, often measured in thousands of GPU-days. In this paper, we propose a frugal and memetic NAS framework designed to democratize architecture design on consumer-grade hardware. Our approach combines the global macro-search capabilities of an autoregressive Transformer controller, trained via Reinforcement Learning (RL), with the local micro-exploitation of an...

---

### 5. Representing the Non-dominated Set of Multi-objective Network Problems by Supported Non-dominated Points

**Authors:** David Könen, Lara Löhken, Michael Stiglmayr

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11821v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11821v1)

**Summary:** In multi-objective combinatorial optimization, unsupported non-dominated points typically outnumber supported points and are often significantly more challenging to compute. Recent studies show that extreme supported non-dominated points provide high-quality representations of the non-dominated set for certain binary problems. We demonstrate that this observation does not generalize to capacitated network optimization problems: representation quality decreases with increasing arc capacities, whe...

---

### 6. Event-based Neural Decoding for Neuroprosthetic Motor Control

**Authors:** Khaleelulla Khan Nazeer, Sirine Arfa, Matthias Jobst, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11445v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11445v1)

**Summary:** A substantial number of patients experience diminished mobility due to disabilities, diseases, or accidents. Although modern prostheses, powered by deep neural networks, hold the promise of significantly enhancing the quality of life for these individuals, their widespread adoption is hindered by significant latency, energy consumption, and spatial requirements. Wired connections to external high-performance processors restrict patient mobility, while wireless connections limit the volume of inf...

---

### 7. Backpropagation as a Nilpotent Linear System

**Authors:** Ahmed Boughammoura

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11289v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11289v1)

**Summary:** Backpropagation is the computational engine of deep learning, yet its mathematical structure is typically treated as a procedural traversal of computational graphs. We present a global operator theory of the \emph{F-adjoint} framework, which reformulates the layerwise backward recursion of an $L$-depth feedforward network into a single linear system $(I-\cB)\Xs=\bG$, where $\bG$ is a source vector. We prove that the global backward operator $\cB$ is strictly block upper-triangular and nilpotent ...

---

### 8. Efficient and Robust Spiking Neural Networks for sEMG-Based Muscle Fatigue Detection

**Authors:** Kaiwen Tang, Jiaqi Dong, Zhanglu Yan, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11065v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11065v1)

**Summary:** Detecting muscle fatigue via surface electromyography (sEMG) is essential for applications in sports, rehabilitation, and wearable health monitoring. Accurate and timely detection of fatigue is crucial for preventing injuries, optimizing physical performance, and ensuring user safety during prolonged activity. However, existing deep learning models are often unsuitable for this task due to their high computational cost and dependence on large-scale data. In this work, we propose an energy-effici...

---

### 9. LayerNorm as Implicit Gain Control in Looped Transformers

**Authors:** Matthias M. M. Buehlmaier

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10681v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10681v1)

**Summary:** In pre-LayerNorm looped transformers, LayerNorm inside the recurrent block acts as an implicit gain controller: by coupling the block's local Lipschitz constant inversely to the activation scale, it renders the recurrence Jacobian non-normal -- asymptotically contractive at every verified fixed point even where its operator norm exceeds 1 -- so the true stability budget is the spectral margin, not an operator-norm bound. That margin depletes as the carry $ρ\to 1$, and a minority of initializatio...

---

### 10. Emergent Generalization by Representation Learning in Artificial Neural Networks

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-07-11

🔗 [Paper](http://arxiv.org/abs/2607.10430v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10430v1)

**Summary:** Dimensionality reduction has proven powerful for identifying neural manifolds, which are low-dimensional structures underlying high-dimensional neural activity. These low-dimensional representations have improved the interpretability of population-level coding. Yet whether such low-dimensional representations are biologically relevant and confer functional advantages in learning systems, or merely reflect neuron-level activity, remains contested in neuroscience. We show that an explicit informat...

---

### 11. Adaptive Search in Collatz Exponent-Code Space via 2-adic and 3-adic Constraints

**Authors:** Oliver Kramer

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.10041v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10041v1)

**Summary:** We study a symbolic search space for the Collatz conjecture based on finite exponent codes of the accelerated map. Each code records the number of divisions by two after every 3n + 1 step and determines three quantities: real drift, a 2-adic start representative, and a 3-adic endpoint representative. Their combination defines the 2-3-infinity diagnostic. Counterexample-like codes should exhibit near-critical drift, small 2-adic start representatives, and endpoints compatible with growth on the s...

---

### 12. A Symbolic Neural CPU for Quantization-Simulated Writeback and Interpretable Program Execution

**Authors:** Jose Luis Lima de Jesus Silva

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.10021v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10021v1)

**Summary:** Neural networks can learn algorithmic input-output mappings, but trusting a learned executor requires more than a correct final answer because the state transitions that produce it are usually hidden. To make those transitions visible, we introduce a trace-supervised symbolic neural CPU, a factorized learned execution architecture that combines recurrent control, an explicit operation router over a fixed differentiable arithmetic-logic unit bank, destination-masked register writeback, complete t...

---

### 13. Remembering Distinct Items, Not Tokens: A Learnable Dirichlet-Process Cache Between State-Space Models and Attention

**Authors:** Siddharth Pal, Viktoria Rojkova

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09889v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09889v1)

**Summary:** Fixed-state sequence models compress an unbounded past into a bounded state, which caps their associative recall at roughly the state dimension; attention escapes the cap by keeping a key-value entry for every token, at quadratic compute and a cache that grows with the sequence. We study the middle ground: a sparse cache that allocates a slot only when an input is novel, so its size tracks the number of distinct items rather than the number of tokens. The allocation rule is the DP-means clusteri...

---

### 14. Foveation-Guided Dynamic Token Selection for Robust and Efficient Vision Transformers

**Authors:** Ibrahim Batuhan Akkaya, Kishaan Jeeveswaran, Bahram Zonooz, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09480v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09480v1)

**Summary:** The human visual system (HVS) employs foveated sampling and eye movements to achieve efficient perception, conserving both metabolic energy and computational resources. Drawing inspiration from this robustness and adaptability, we introduce the Foveated Dynamic Transformer (FDT), a foveation-guided dynamic token-selection architecture that integrates these mechanisms into a vision transformer framework. The FDT exhibits strong resilience to various types of noise and adversarial attacks, despite...

---

### 15. Co-evolution of self-replication and function in a digital primordial soup

**Authors:** Francesco Cicala, Eyvind Niklasson, Ettore Randazzo, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09211v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09211v1)

**Summary:** While traditional evolutionary algorithms hard-code reproduction, self-replication can emerge spontaneously within digital ``primordial soups''. This paper investigates the co-evolution of this emergent self-replication alongside problem-solving capabilities. We initialize a population of random 32-byte Z80 assembly programs, requiring self-replication to arise purely through random assembly-level mutations and pairwise program interactions. To link these behaviors, we introduce a task-based val...

---

### 16. Interference and Retention in Continual Learning

**Authors:** Julius Störk

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09202v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09202v1)

**Summary:** Continual learning commonly relies on post-hoc mechanisms such as replay, elastic regularization, or distillation. This work argues that forgetting should instead be modeled directly as interference between tasks. In the frozen-feature regime, forgetting from learning a new task is exactly the interference energy induced on the old task. In deep networks, the same quantity is recovered through path-averaged curvature with minimal additional forward passes.   When task supports are disjoint, forg...

---

### 17. Evolutionary Intelligence for Scientific Discovery: From Evolutionary Computation to Cumulative Discovery Systems

**Authors:** Chao Wang, Lingling Li, Fang Liu, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09025v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09025v1)

**Summary:** Artificial intelligence (AI) is shifting scientific discovery from task-specific workflows towards autonomous systems that organize exploration with experimental and human feedback in open-ended candidate spaces. Evolutionary computation (EC) provides a computational basis for feedback-driven discovery because population-based search can maintain diverse scientific candidates while steering exploration through accumulated evidence. However, EC predominantly focuses on candidate refinement for pr...

---

### 18. Sampling on Random Subspaces under Limited Data in the Context of Exploratory Landscape Analysis

**Authors:** Iván Olarte Rodríguez, Anja Jankovic, Thomas Bäck, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07854v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07854v1)

**Summary:** Classical space-filling designs often fail to provide reliable statistical results for Exploratory Landscape Analysis (ELA) when only limited evaluation budgets are available, as commonly occurs in high-dimensional problems or other resource-constrained settings, resulting in noisy and unstable landscape descriptors.   To address this challenge, we propose an alternative sampling strategy for ELA based on random linear embeddings. Rather than sampling uniformly in the full decision space, we all...

---

### 19. Social-spatial dependencies for learning visual navigation

**Authors:** Patrick Govoni, Pawel Romanczuk

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07460v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07460v1)

**Summary:** Navigation for social organisms rarely is a fully independent activity. Group structure and dynamics, as well as embodied interactions, critically influence useful behavior. Individual neural network controlled agents are trained to navigate in different social contexts, where social dependence and behavioral strategy learned is determined by relative task performance and spatial effect. Increasing high quality social information drives phase transitions from individual to following navigational...

---

### 20. Single-Entity Spiking Neuron Models: Survey

**Authors:** Leon Parepko, Danila Shulepin, Albert Nasybullin

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07429v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07429v1)

**Summary:** In this work, we reviewed different approaches in mathematical modeling of biologically plausible neural systems. Models are characterized and classified based on their common features and special use cases. In addition to spiking models, different types of discrete and continuous analogs are considered to accurately simulate biological processes, including membrane potential dynamics. The models under investigation include neurons and various components encountered in neural systems and affecte...

---

### 21. Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware

**Authors:** Oskar von Seeler, Christian Tetzlaff, Andrew Lehr

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07373v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07373v1)

**Summary:** In biological circuits, sequential neural activity evolves along dynamic, low-dimensional manifolds to enable flexible behavior. Spiking network models link aspects of this sequential activity to features of manifold geometry through specific circuit mechanisms, making dynamic neural manifolds parameterizable, and thereby offering an explainable framework for neural computation. Extending this framework to neuromorphic engineering, we present an implementation on the SpiNNaker 2 chip for real-ti...

---

### 22. Intrinsic-Noise Consolidation: A Doob-Barrier-Conditioned Diffusion Turns Analog Device Noise into a Continual-Learning Resource

**Authors:** Gunner Levi Howe

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06924v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06924v1)

**Summary:** On analog neuromorphic hardware, intrinsic device noise is normally an accuracy tax. We ask whether it can instead consolidate memories. We cast per-synapse consolidation as a Doob h-transform: condition each weight's stochastic dynamics on never crossing a memory-critical barrier around its consolidated value. The conditioned diffusion gains an extra drift sigma^2 d/dw log h, a restoring force amplified by the noise variance itself that diverges at the barrier. We are explicit about novelty: th...

---

### 23. Do You Remember? Toward Memory-Centric Multimodal AI

**Authors:** Xuguang Yu, Weigang Zheng, Minyue Yu

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.11919v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11919v1)

**Summary:** Human memory is reconstructive, not a faithful recording. Current multimodal LLMs (MLLMs) lack this capability: they process images through a frozen visual encoder, produce a one-shot text output, and discard internal representations. We present DoYouRemember, a three-stage architecture introducing reconstructive memory into MLLMs: (1) a VQ-VAE compresses images into discrete visual tokens, (2) a LoRA-fine-tuned LLM jointly attends to visual and text tokens, and (3) a Diffusion Decoder reconstru...

---

### 24. An Introduction and Tutorial for the Beagle Framework

**Authors:** Ilya Basin, Nathan Haut

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06731v2) | 📄 [PDF](https://arxiv.org/pdf/2607.06731v2)

**Summary:** The Beagle framework is a GPU-based genetic programming framework that enables highly efficient genetic programming search using large population sizes by leveraging NVIDIA GPUs. This technical guide provides an introduction to the Beagle framework and provides detailed instructions for using the framework for symbolic regression problems.

---

### 25. A Hardware-Aware Open-Source Framework for Design Space Exploration of Mixed-Signal Spiking Neural Networks

**Authors:** Sayma Nowshin Chowdhury, Vineeta Nair, Taseen Forhad, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06456v2) | 📄 [PDF](https://arxiv.org/pdf/2607.06456v2)

**Summary:** Energy-efficient neuromorphic computing at the edge requires simulation tools that can capture the non-ideal behavior of mixed-signal spiking neural network (SNN) hardware while supporting system-level design exploration. This work presents an open-source hardware-aware simulation framework for mixed-signal SNNs that enables comparative analysis across neuron, synapse and architecture choices. The framework supports multiple neuron models, including Leaky Integrate-and-Fire (LIF), Hodgkin-Huxley...

---

### 26. Scalable Perturbation Learning for Online Self-Supervised Echo State Networks

**Authors:** Taiki Yamada, Kantaro Fujiwara

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06079v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06079v1)

**Summary:** Intelligent systems should not only solve tasks but also adapt under real-world constraints. Autonomous adaptation via self-supervised learning, sequential adaptation via online learning, and memory-efficient implementation via perturbation-based learning are important requirements for such systems. However, these requirements are generally in tension for high-dimensional systems, because perturbation-based learning suffers from variance that grows with the dimension of the perturbed variables. ...

---

### 27. An event-driven framework for fly-inspired visual motion detection

**Authors:** Qinbing Fu, Jingyu Huang, Yan Xie, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05205v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05205v1)

**Summary:** Fast and reliable motion detection is essential for machine vision and autonomous systems operating in dynamic environments. This work integrates emerging event-based sensing with biologically structured neural computation to establish an efficient computational paradigm for visual motion detection. The proposed framework is built upon a recently developed fly-inspired neural network that emulates motion-processing circuits in the optic lobe. Owing to its feed-forward and training-free architect...

---

### 28. LLM for the development of FCM

**Authors:** Alexis Kafantaris

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04983v2) | 📄 [PDF](https://arxiv.org/pdf/2607.04983v2)

**Summary:** This article is about the development of a fuzzy cognitive map using a local large language model. In the light of recent advances it is evident that large language models, and even local large language models are capable of extracting quantities from textual data. In other words, a local LLM like Qwen2.5-32B, or probably larger, can accept entities as prompt input and determine relevant quantitative data as the model output. In turn, this output can be utilized for the construction of a data dr...

---

### 29. LLM-Driven Evolutionary Generation of Multi-Objective Bayesian Optimization Algorithms

**Authors:** Georgios Laskaris, Reuben Brasher, Niki van Stein, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.08791v1) | 📄 [PDF](https://arxiv.org/pdf/2607.08791v1)

**Summary:** Designing effective multi-objective Bayesian optimization (MOBO) algorithms requires balancing many interdependent design choices whose optimal configuration is problem-dependent and typically demands deep expertise. We extend the LLaMEA framework to MOBO, using large language models as mutation and crossover operators within evolutionary strategies to generate complete algorithm implementations, with SMAC hyperparameter optimization integrated into the evolutionary loop. Across nine evolutionar...

---

### 30. A Large-Scale Sparse Multiobjective Optimization Algorithm Based on Optimal Performance Scores

**Authors:** Jia-Lin Mai, Min-Rong Chen, Guo-Qiang Zeng, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04765v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04765v1)

**Summary:** Large-scale sparse multiobjective optimization problems (LSSMOPs) involve a large number of decision variables and Pareto optimal solutions with only a few nonzero variables. However, as the number of decision variables grows, it becomes increasingly challenging to accurately identify the nonzero variables, and optimization performance is adversely affected. To address these issues, this paper proposes an evolutionary algorithm for LSSMOPs. Specifically, we propose a new initialization method ca...

---

### 31. QDEvo: A Multi-Objective Quality-Diversity Framework for Automated Heuristic Design

**Authors:** Nam Do Khanh, Nhat Nguyen Tran Minh, Dat Pham Vu Tuan, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.11916v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11916v1)

**Summary:** The integration of Large Language Models (LLMs) with evolutionary computation has emerged as a powerful paradigm for automated heuristic design in combinatorial optimization. However, existing approaches suffer from mode collapse, converging to homogeneous populations that lack semantic diversity and fail to explore the full algorithmic space. We propose Quality-Diversity Evolution (QDEvo), a multi-objective framework that integrates Quality-Diversity optimization with LLM-driven heuristic searc...

---

### 32. Heaviside Continuity of Rolling Coefficients for Eliminating Epistemic Entropy in Large Language Models

**Authors:** MY Pitsane, Hope Mogale

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04562v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04562v1)

**Summary:** Large language models (LLMs) generate fluent outputs that can be wrong. Unlike humans, who often exhibit cues when providing false information, LLMs produce errors that are difficult to detect because autoregressive decoding provides no mechanism for verifying intermediate reasoning before state progression. We introduce Heaviside Continuity of Rolling Coefficients (HCRC), a verification-first execution framework that reformulates inference as predicate-gated state transitions governed by a Heav...

---

### 33. Neuromorphic Silicon Neuron Controller for Adaptive Deep Brain Stimulation in Parkinson's Disease

**Authors:** Md Abu Bakr Siddique, Jakub Orłowski, Yan Zhang, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.05453v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05453v1)

**Summary:** Parkinson's disease (PD) affects millions worldwide and causes severe motor symptoms. Adaptive deep brain stimulation (aDBS) delivers physiologically informed stimulation that can track fluctuations in PD motor symptoms, enabling more intelligent DBS control. However, most existing aDBS approaches are primarily algorithm- and software-driven, with limited efforts toward circuit realization, particularly low-power and implantable integrated circuits. This paper presents the Silicon Leaky Integrat...

---

### 34. Burst Spiking Neural Networks

**Authors:** Jiahong Zhang, Sijun Shen, Man Yao, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.11914v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11914v1)

**Summary:** A central goal of current Spiking Neural Network (SNN) research is to improve their accuracy toward becoming low-power alternatives to Artificial Neural Networks (ANNs). This work further argues that realizing this ambition requires improving not only accuracy but also robustness, defined as the ability to maintain correct predictions under input perturbations. We identify two key issues in existing SNN methods that undermine robustness. First, binary spiking activations can produce large activa...

---

### 35. Towards Self-Evolving Agents: A Human-Inspired Adaptive Exploration-Exploitation Framework for Genetic Network Programming

**Authors:** Ali Kohan, Mohamad Roshanzamir, Roohallah Alizadehsani, et al.

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.11913v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11913v1)

**Summary:** Recent advancements in agentic AI have increasingly moved toward graph-based methods, driven by the demand for explainable, human-centered, and non-linear reasoning workflows. A prominent example is Genetic Network Programming (GNP), a self-evolving algorithm that utilizes directed graphs to evolve interpretable decision structures for agents. As in most evolutionary algorithms, effectively balancing exploration and exploitation is a key aspect of GNP. However, this trade-off has received limite...

---

### 36. Life as Plasmas: Autonomy and Interactivism in-materio

**Authors:** Nicolás Hinrichs, Mahault Albarracin, Felipe Engelberger, et al.

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.09747v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09747v1)

**Summary:** When is a material system a candidate for life at all? We argue that this question is prior to behavior, functional architecture, or computational capacity, and that at root it is one of physical admissibility. We develop a framework in which minimal autonomy, taken in the interactivist sense of normativity grounded in self-maintaining far-from-equilibrium organization, corresponds to a distinct non-equilibrium phase of matter, and we take complex plasmas, a physical and non-biological system, a...

---

### 37. SeqGPT: A Constrained Transformer Agent for the Inverse Designof Multi-Panel Composite Structures

**Authors:** Driss Chraibi, Alejandro García Pis, Stéphane Grihon, et al.

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.11910v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11910v1)

**Summary:** Optimizing composite stacking sequences to match continuous targets (e.g., Lamination or Buckling Parameters) with discrete manufacturing constraints represents a challenging combinatorial inverse problem that regularly occurs in composite design especially when numerical optimization approaches are used (bi-step, bi-level configurations). In multipanel configurations, this complexity is further intensified by blending, a global compatibility/continuity requirement between the different panel st...

---

### 38. Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures

**Authors:** Joy Bose

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02967v2) | 📄 [PDF](https://arxiv.org/pdf/2607.02967v2)

**Summary:** Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory. CALM (Nechesov and Ruponen, 2025) identifies its threshold-binary encoder as an open design question. This paper evaluates rank-order N-of-M encoding (Furber et al., 2007) as an alternative. We make three contributions. First, a faithful reimplementation validates the published architecture by confirming exact equivalence betwee...

---

### 39. Microcosmos: Reimagining Artificial Life for the GPU Era

**Authors:** Mark Tensen, Ciaran Regan, Bert Wang-Chak Chan, et al.

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02954v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02954v1)

**Summary:** Most artificial life simulators either operate on abstract substrates disconnected from physical reality, or simulate physically grounded worlds that do not scale to the population sizes required for open-ended evolution. We present Microcosmos, a simulation engine in which artificial lifeforms are modeled as elastic filament chains inhabiting a two-dimensional viscous fluid world, designed from the ground up for modern GPU hardware and end-to-end differentiable simulation. We validate the engin...

---

### 40. A Spiking Sequence Generator for Polar Trajectories on Neuromorphic Hardware

**Authors:** William R. P. Nourse, Roger D. Quinn

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02753v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02753v1)

**Summary:** Neuromorphic controllers for size, weight, and power-constrained systems require neural architectures that are both energy-efficient and interpretable at the level of system dynamics. However, existing approaches either rely on end-to-end trained spiking networks with limited interpretability, or on converted classical controllers that fail to fully exploit neuromorphic dynamics. We present a spiking neural network (SNN) architecture for generating polar trajectories, using a winner-take-all (WT...

---

### 41. Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

**Authors:** Kuo-Chung Peng, Jiun-Cheng Jiang, Chun-Hua Lin, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02363v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02363v1)

**Summary:** Quantum Fast-Weight Programmers (QFWPs) store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states, offering a practical route to quantum sequence modeling. Self-Modulating QFWP improves this framework by using input-dependent gates for both new fast-weight updates and the accumulated fast-weight state, but its unbounded old-state multiplier can diverge in long-sequence regimes. We propose a bounded old-state modulation ru...

---

### 42. Hybridizing a Grouping Metaheuristic with Reinforcement Learning for the One-Dimensional Bin Packing Problem

**Authors:** Zitouni Rania, Mostefai Mounir Sofiane, Tati Youcef, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02315v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02315v1)

**Summary:** The one-dimensional bin packing problem (1D-BPP) is a canonical NP-hard combinatorial optimization problem with broad industrial applications. We propose RL-HGGA, a hybrid algorithm that integrates Falkenauer's Hybrid Grouping Genetic Algorithm (HGGA) with a tabular Q-learning controller. Rather than applying genetic operators at fixed probabilities, a Q-learning agent dynamically selects among eight macro-actions -- including BPCX crossover, light and heavy mutation, Martello-Toth local search,...

---

### 43. Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

**Authors:** Juwei Shen, Yujie Wu, Changwen Chen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02283v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02283v1)

**Summary:** In-context learning (ICL) operates via implicit gradient descent embedded in the forward pass of modern AI architectures -- Transformers, Mamba, state-space models, and MLPs. Capturing this capability in biologically plausible Spiking Neural Networks (SNNs) has remained an open challenge: existing SNNs fail the Garg-2022 benchmark at non-trivial task dimensions. We trace this failure to a structural assumption: prior SNN designs route adaptation through inference-time synaptic plasticity, viewin...

---

### 44. Predicting Early Stages Of Alzheimer's Disease And Identifying Key Biomarkers Using Deep Artificial Neural Network And Ensemble Of Machine Learning Methodologies

**Authors:** Debopriya Ghosh

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02142v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02142v1)

**Summary:** Alzheimers disease (AD) is a brain disorder that develops slowly and mainly affects memory, thinking, language, and daily activities. It is one of the most common causes of dementia and creates many difficulties for patients as well as their families. In the early stage, the symptoms are often mild and may look like normal ageing. For this reason, many people are diagnosed late, when the disease has already progressed. At present, there is no complete cure for AD. Still, early detection can help...

---

### 45. Electronic Bursting Neuron: design, equations and hardware implementation

**Authors:** Lev V. Takaishvili, Vladimir I. Ponomarenko, Maksim V. Kornilov, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02122v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02122v1)

**Summary:** Electronic neurons are a keystone for construction of the spiking neural networks which have numerous applications in neuroprosthetics, artificial memory, intensive calculations etc. A number of concepts of electronic neurons has been already proposedm with some of them implemented in hardware. However, new schemes are of significant interest since the existing ones do not fit all requirements: either they are too complex and expensive in realization, or they are not able to demonstrate all dema...

---

### 46. Evolutionary Wave Function Collapse

**Authors:** Dipika Rajesh, Ahmed Khalifa, Julian Togelius

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02082v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02082v1)

**Summary:** Wave Function Collapse (WFC) is a widely used procedural content generation method that learns local adjacency constraints from example inputs to generate larger outputs. In this paper, we explore combining WFC with evolutionary search by evolving the small input examples used by WFC rather than directly evolving complete levels. In this approach, WFC acts as a genotype-to-phenotype mapping. The generated levels are then evaluated through domain-specific fitness functions. We evaluate the method...

---

### 47. Mechanism and Stability Analysis of Metabolic Closed-Loop Metaheuristics

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01551v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01551v2)

**Summary:** This paper studies the Metabolic Multi-Agent Optimizer (MMAO) at the framework level rather than at the implementation or benchmark level. The central question is whether the metabolic resource loop of private energy, communal budget, role drift, and lifecycle turnover has a framework-level interpretation beyond narrative metaphor. We introduce a generic MMAO state model that abstracts away domain-specific move operators while retaining the resource bookkeeping that defines the framework. Under ...

---

### 48. MMAO-Cls: Metabolic Multi-Agent Optimization for Joint Feature Selection and Classifier Tuning

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01539v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01539v2)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can act as a credible outer-loop optimizer for classification model selection. We propose MMAO-Cls, a mixed-space realization in which each agent jointly encodes a binary feature mask and classifier hyperparameters, while private energy, communal budget, role drift, and lifecycle turnover are mapped to the accuracy-complexity tradeoff of wrapper learning. The implementation is strengthened by deriving feature-budget adaptation...

---

### 49. BFF: Simple explanations for complex phenomena

**Authors:** Charlotte Knierim, Luca Versari, Robert Obryk, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01483v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01483v1)

**Summary:** The ''Computational Life'' paper (Agüera y Arcas et al., 2024) argues that paired interactions in a computational soup are an effective way to find self-replicators. In this work, aided by recent developments in self-replicator detection, we explore the alternate hypothesis that self-replicators can be found at least as easily using simple mutation random walks in program space. We also explore the claim that capping the maximum ''depth'' and ''width'' of the ancestry tree stops self-replicators...

---

### 50. Towards transferable lightweight neuromorphic computing through a model-free temporal-switch framework

**Authors:** Zefeng Zhang, Chao Li, Siyao Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.02608v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02608v1)

**Summary:** Lightweight neuromorphic computing offers a promising route to efficient AI, with particular benefits for resource-constrained edge deployments. However, its scalable deployment that can reliably transfer the expected performance has long been hindered by device-to-device variations, which necessitate costly and repeated re-training on new copies and undermine the practical advantages. To address this issue, we introduce a model-free temporal-switch (TS) framework to improve the direct transfer ...

---

## q-bio.NC

**50 papers**

### 1. Optimal photostimulation selection for iterative activity maps

**Authors:** Jacob J. Morra, Kaitlyn E. Fouke, Owen Traubert, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12930v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12930v1)

**Summary:** All-optical two-photon holographic optogenetics enables causal circuit mapping by stimulating defined neurons or ensembles while imaging population activity. Yet exhaustive connectivity mapping remains experimentally prohibitive because of combinatorial complexity, tissue heating, photodamage, and experimental time. We present OPhELIA (Optimal Photostimulation sElection for Iterative Activity maps), a Bayesian framework for selecting informative perturbations under limited trial budgets. OPhELIA...

---

### 2. Real-time fall detection based on vision for low-power edge platforms

**Authors:** Wenjun Xia, Zhicheng Peng, Haopeng Li, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12909v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12909v1)

**Summary:** Falling detection is vital for elderly care and intelligent surveillance; however, prevailing vision-based approaches predominantly frame it as static pose classification or discrete temporal pattern matching, fundamentally overlooking the instability dynamics of the human support system. This paper proposes a physics-informed falling detection framework that recasts falling as a stability-loss event in a coupled dynamical system. We introduce a novel dual-LTC architecture comprising a Center-of...

---

### 3. Differentiable Clone-Structured Causal Graphs for End-to-End Cognitive Map Learning from Image Sequences

**Authors:** Arash Nikzad, Sasan Sarbishegi, Ali Dasmeh, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12382v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12382v1)

**Summary:** How can an agent build a structured map of its world from nothing but an ongoing sequence of raw sensory input and its own movements, especially when natural variation means exact sensory patterns rarely repeat? The Clone-Structured Causal Graph algorithm (CSCG), a normative hippocampus model, shows how an interpretable map can be learned from aliased observations. However, CSCG requires a predefined discrete alphabet, and its expectation-maximization formulation is not easily combined with exis...

---

### 4. Imputation-free transformer learning enables robust Alzheimer's disease prediction and calibrated uncertainty quantification across heterogeneous clinical cohorts

**Authors:** Christelle Schneuwly Diaz, Narmina Baghirova, Duy-Thanh Vu, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11656v2) | 📄 [PDF](https://arxiv.org/pdf/2607.11656v2)

**Summary:** Accurate diagnostic classification and disease-severity prediction for Alzheimer's disease are hampered by the incompleteness and heterogeneity of real-world clinical data. Left unaddressed, these barriers prevent reliable disease modelling and hinder effective clinical evaluation. Conventional imputation strategies introduce systematic bias, distort inter-feature relationships, and yield overconfident predictions, limitations especially consequential in diagnostic settings. Here, we propose NIT...

---

### 5. Fast Whole-Brain, Geometry-Aware Functional Alignment for Cross-Subject Decoding

**Authors:** Pierre-Louis Barbarant, Florent Meyniel, Bertrand Thirion

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10931v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10931v1)

**Summary:** Decoding brain activity is useful for characterizing brain processes and understanding the functional architecture underlying cognition. However, the inter-individual variability in brain response patterns limits the development of decoders that generalize across individuals. A solution to this challenge is functional alignment: aligning functional data across individuals before training population-level decoders. The core issue is to strike the balance between aligning functional features and p...

---

### 6. Constructed Reality, Contested Priors: Decoupling and the Architecture of Cognitive Relapse Under the Free Energy Principle

**Authors:** MD Ibrahim Hossain Ridoy

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.11958v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11958v1)

**Summary:** Under the free energy principle, a predictive system does not observe reality directly; it maintains a generative model of the world and experiences that model's best current hypothesis. Can a synthetic environment be made consistent enough that a predictive system's own inference machinery adopts it as this default hypothesis, permanently displacing the environment that first shaped it? We call this state ontological inversion. Because inducing and monitoring such a transition in a nervous syst...

---

### 7. Threat Vectors and the State of the Art in Defense Methods for Security in Neurotechnology

**Authors:** Bryce-Allen Bagley, Nathaniel Rose, Quintus Kilbourn, et al.

**Published:** 2026-07-11

🔗 [Paper](http://arxiv.org/abs/2607.10451v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10451v1)

**Summary:** Brain-computer interfaces (BCIs) are a class of diverse hardware modalities, associated software, and connected devices which are widely used in a variety of fields, including neurosurgery, biomedical data analysis, and neuroimaging. Recent years have seen rapid advancements in BCI technology, and neurotechnology more broadly, with the first devices now passing clinical trials, early examples of consumer hardware entering the market, and many variants of consumer and medical hardware with increa...

---

### 8. Learning the Brain's Dynamics as a Port-Hamiltonian System

**Authors:** Dibakar Sigdel

**Published:** 2026-07-11

🔗 [Paper](http://arxiv.org/abs/2607.10439v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10439v1)

**Summary:** We model human motor cortex during a wrist-extension BCI task as a port-Hamiltonian system (pHS): a conservative interconnection (gyroscopic coupling between neural phasors) plus a dissipative port (power-law energy decay driven by a GNN surrogate). A metriplectic integrator evolves the phasor state; a Fluctuation--Dissipation-consistent noise channel produces stochastic trajectories at body temperature. Training on \FitTrainN\ real EEG cycles (PhysioNet EEGMMIDB, 3 held-out subjects) reaches a ...

---

### 9. Emergent Generalization by Representation Learning in Artificial Neural Networks

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-07-11

🔗 [Paper](http://arxiv.org/abs/2607.10430v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10430v1)

**Summary:** Dimensionality reduction has proven powerful for identifying neural manifolds, which are low-dimensional structures underlying high-dimensional neural activity. These low-dimensional representations have improved the interpretability of population-level coding. Yet whether such low-dimensional representations are biologically relevant and confer functional advantages in learning systems, or merely reflect neuron-level activity, remains contested in neuroscience. We show that an explicit informat...

---

### 10. Prompting-MammAlps: Fine-Grained Text-to-Video Retrieval for Camera-Trap Data

**Authors:** Valentin Gabeff, Baptiste Maquignaz, Jennifer Shan, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09876v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09876v1)

**Summary:** Automatically retrieving videos from large camera-trap datasets remains challenging. Text-to-Video retrieval (TVR) methods based on large video-language models (VLMs) have potential to retrieve events of interest by describing them with simple text queries. However, current methods often lack spatiotemporal understanding and do not generalize well to ecological data. In this work, we introduce Prompting-MammAlps, the first camera-trap TVR benchmark, and propose a fine-grained and interpretable T...

---

### 11. PHINN-EEG: Topological Time-Series Analysis of Dream-State EEG -- Dynamic Betti Curves for Dream Content Classification and Topology-Conditioned Neural Signal Synthesis

**Authors:** Ren Takahashi, Emre Yusuf, Jayabrata Bhaduri

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09662v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09662v1)

**Summary:** Current electroencephalography (EEG)-based dream detection relies on power spectral density (PSD) and statistical moment features, achieving a state-of-the-art area under the receiver operating characteristic curve (AUC) of approximately 0.70 on the DREAM database (Wong et al., 2025, Nature Communications). We introduce PHINN-EEG (Persistent Homology Inspired Neural Network for EEG), the first topological time-series framework for dream mentation analysis. Using sliding-window Takens delay embed...

---

### 12. CoCoT-EEG: Contrastive-Pretrained Multiscale Convolutional Transformer for EEG Decoding

**Authors:** Gabriel Mahuas, Victoria Shevchenko, Ugo Tanielian, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09543v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09543v1)

**Summary:** Self-supervised pretrained foundation models (FM) have shown early promise for non-invasive electroencephalogram (EEG) decoding applications. Many recent large-scale models converged on the approach of tokenizing raw EEG followed by masked reconstruction pretraining. However, this recipe has been shown to be suboptimal for data, like EEG, with high noise amplitude and information confined to limited dimensions such as narrow frequency bands. Building on this insight, we develop a novel contrasti...

---

### 13. A multi-ensemble mean-field reduction method for networks of globally coupled phase oscillators with arbitrary parameter distributions

**Authors:** Richard Gast, Shotaro Takasu, Helmut Schmidt, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09516v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09516v1)

**Summary:** Understanding the dynamical properties of coupled phase oscillator systems with heterogeneous oscillator frequencies has been a long-standing challenge of complex systems theory. While the seminal work of Ott and Antonsen dramatically improved our theoretical understanding of coupled phase oscillators for a small family of oscillator frequency distributions, we here present a mean-field reduction method for arbitrary frequency distributions. Our method leverages the drastic dimensionality reduct...

---

### 14. Structural Brain Predictors of Visual Attention Gradient Modulated by Trait Anxiety

**Authors:** Suhail Rafiq Mir, Dolcy Dhar, Ishita Singh, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09278v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09278v1)

**Summary:** Dynamic allocation of attention across the visual field, quantified as a visuospatial attention gradient, is essential for maintaining perceptual breadth. Disruptions to this flexibility may contribute to altered spatial attentional bias and may be influenced by trait anxiety. We investigated whether individual differences in structural brain morphology predict spatial attentional deployment as a function of trait anxiety. Sixty participants, recruited based on an a priori sample size calculatio...

---

### 15. Quantum Logic as the Logic of Contexts

**Authors:** Haruki Emori, Atsushi Iriki, Andrei Khrennikov, et al.

**Published:** 2026-07-10

🔗 [Paper](http://arxiv.org/abs/2607.09032v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09032v1)

**Summary:** Quantum logic is usually presented as a non-classical departure from ordinary reasoning forced on us by quantum mechanics, with classical logic kept as the secure starting point. We argue for the opposite order of explanation in a finite and fully computable setting. The free orthomodular lattice on two generators has ninety-six elements, the direct product of a six-element non-distributive factor and a sixteen-element Boolean factor. Reading the first factor as a register of contexts and the se...

---

### 16. Spatial Neighboring Scattering Transform: A Cross-Channel Amplitude Coupling Measure for EEG Connectivity

**Authors:** Md. Taksimul Ahsan Tawhid, Nasif Ahmed Rafe, Alif Tahmid Priyom, et al.

**Published:** 2026-07-09

🔗 [Paper](http://arxiv.org/abs/2607.08855v1) | 📄 [PDF](https://arxiv.org/pdf/2607.08855v1)

**Summary:** The functional organization of the brain relies on coordinated activity across spatially distributed regions, making the analysis of inter-regional dependencies fundamental. Existing connectivity measures address this predominantly through phase synchronization, which is vulnerable to volume conduction artifacts and discards amplitude-domain coupling. This study introduces the Spatial Neighboring Scattering Transform, which extends the wavelet scattering transform to the multichannel setting, yi...

---

### 17. Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks

**Authors:** Dan Yamins, Aran Nayebi

**Published:** 2026-07-09

🔗 [Paper](http://arxiv.org/abs/2607.08561v1) | 📄 [PDF](https://arxiv.org/pdf/2607.08561v1)

**Summary:** A series of results from the NeuroAI over the past fifteen years have raised core questions both about how to compare Deep Neural Network (DNN) models to the brain, and about how much convergent evolution to expect between artificial networks and real brain networks. Here, we show that for any two minimal DNN solutions to a sufficiently hard task: (i) "weak" alignment of network representations based on affine mappings guarantees "strong" alignment of privileged axes, and (ii) alignment "zippers...

---

### 18. A Non-Hermitian Potential Well Formalism for Conscious--Preconscious--Subliminal Processing

**Authors:** Vasily Lubashevskiy, Ihor Lubashevsky

**Published:** 2026-07-09

🔗 [Paper](http://arxiv.org/abs/2607.08302v1) | 📄 [PDF](https://arxiv.org/pdf/2607.08302v1)

**Summary:** We propose a phenomenological model of the Global Neuronal Workspace (GNW) in which early sensory processing generates an effective complex-valued landscape governing the dynamics of high-level stimulus representations. This landscape provides a dynamical bridge between sensory encoding and conscious access, enabling both processes to be described within a unified framework. High-level representations are encoded in a cloud function defined on a Hilbert space over a perceptual state space, there...

---

### 19. Single-Entity Spiking Neuron Models: Survey

**Authors:** Leon Parepko, Danila Shulepin, Albert Nasybullin

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07429v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07429v1)

**Summary:** In this work, we reviewed different approaches in mathematical modeling of biologically plausible neural systems. Models are characterized and classified based on their common features and special use cases. In addition to spiking models, different types of discrete and continuous analogs are considered to accurately simulate biological processes, including membrane potential dynamics. The models under investigation include neurons and various components encountered in neural systems and affecte...

---

### 20. Quantifying Entrainment Evidence: A Comparison of Frequentist and Bayesian Approaches for Information Processing Pathway Maps

**Authors:** Kaibo Zhang, Ji Wu, Chao Zhang, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06284v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06284v1)

**Summary:** Information Processing Pathway Maps (IPPMs) offer a scalable framework for formalizing the complex sequence of mathematical transformations applied to sensory stimuli. These maps chart the latency and cortical expression of computational steps, relying on statistical inference to link model outputs with observed neural activity. Traditionally, this mapping has relied on frequentist hypothesis testing. However, determining which of several competing computational models best explains neural data ...

---

### 21. STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning

**Authors:** Roy Segal, Yoni Svechinsky, Tomer Fekete

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06629v2) | 📄 [PDF](https://arxiv.org/pdf/2607.06629v2)

**Summary:** Brain age - the age inferred from a physiological recording - is an emerging biomarker whose deviation from chronological age tracks neurological and psychiatric burden, and EEG is an attractive substrate for it because it is cheap, portable, and temporally rich. Yet EEG brain-age models must contend with cross-site montage heterogeneity, small labelled cohorts, and dominant subject-level non-stationarity, and few EEG foundation models have been shown to deliver competitive age regression across...

---

### 22. Reward Valuation in Vision Language Models: Causal Mechanisms Underlying Anhedonia

**Authors:** Melika Honarmand, Samin Mahdipour Aghabagher, Martin Schrimpf

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06626v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06626v1)

**Summary:** Recent Vision-Language Models capture increasingly complex aspects of human cognition. Here we ask whether this alignment extends to reward valuation, which we assess in a mechanistic framework built on clinical tests that were developed to evaluate anhedonia and motivational deficits in major depressive disorder. In the brain, anhedonia is frequently linked to dysregulation in the Nucleus Accumbens (NAc) and the broader dopaminergic reward system. While neuroimaging has localized these deficits...

---

### 23. Using hierarchical statistical learning models to model individual statistical learning

**Authors:** Hanna Ringer, Tatsuya Daikoku

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.05822v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05822v1)

**Summary:** Statistical learning is essential for individuals to discover structure in the sensory environment, especially during communication via speech or music. Individual differences in statistical learning abilities have been proposed to account for differences in various cognitive functions and development, including developmental disorders such as dyslexia. In this study, we used a Hierarchical Bayesian Statistical Learning (HBSL) model to model individual learning trajectories as recorded using ele...

---

### 24. On the Increased and Decreased Connectivity of the Demented Human Brain

**Authors:** Daniel Hegedus, Marton Barnabas Mora, Balint Varga, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05654v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05654v1)

**Summary:** With the enormous advances in cerebral imaging techniques, a large amount of data is available for studying the aging and demented brain. In this contribution, we apply the OASIS-3 dataset for identifying small areas of the human gray matter, which have higher- or lower structural connectivity in dementia and aging. As anticipated, we found that finer structures of the hippocampus and the temporal lobe show decreased connectivity in dementia. More surprisingly, the precuneus, the cuneus, and fin...

---

### 25. Governable Individuals: An Identity Layer for Embodied Agents That Keep Learning

**Authors:** Xue Qin, Simin Luan, Cong Yang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05463v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05463v1)

**Summary:** Embodied artificial intelligence is moving from deployable models to persistent agents that learn in the field, acquire skills and migrate across bodies. Governing such a system means governing an individual, not a model, and existing proposals (agent identifiers, activity logs, guardrails) do not survive an agent that keeps rewriting itself. We propose the governable individual: an agent whose competence may change without bound, but whose authority, memory schema, embodiment rights and capabil...

---

### 26. Beyond DSA: Conjugacy-based Comparison of Dynamical Systems

**Authors:** Prakhar Godara, Pang Shiang Tay, Marcelo G. Mattar

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04493v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04493v1)

**Summary:** Comparing whether two dynamical systems implement the same computation despite differences in coordinates or measurements is a central problem in neuroscience and machine learning. Dynamical Similarity Analysis [DSA; Ostrow et al., 2023] addresses this problem by aligning finite-dimensional Koopman approximations through an orthogonal similarity transformation. Here we show that orthogonal alignment is neither necessary nor sufficient for topological conjugacy: conjugate systems may require a no...

---

### 27. Cross-Subject Modeling for Widefield Calcium Imaging via Atlas-Aligned Spatiotemporal Tokenization

**Authors:** Mohammad Hosseini, Eray Erturk, Saba Hashemi, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.09754v1) | 📄 [PDF](https://arxiv.org/pdf/2607.09754v1)

**Summary:** Large-scale, multi-subject widefield calcium imaging provides unprecedented access to brain-wide cortical dynamics. However, the high dimensionality, complex spatiotemporal structure, and substantial task-irrelevant activity in widefield recordings have largely restricted modeling efforts to single-session analyses, limiting scalability and generalization. While multi-subject pretrained models have been explored for some neural modalities, multi-subject models for widefield calcium imaging have ...

---

### 28. Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation

**Authors:** Amrith Lotlikar, Ian Christopher Tanoh, Praful Vasireddy, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04063v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04063v1)

**Summary:** Multi-compartment Hodgkin-Huxley (HH) models provide a principled framework for predicting neural dynamics and responses to electrical stimulation. However, fitting HH biophysical parameters typically requires intracellular recordings, which are invasive and low-throughput, limiting the ability to capture the geometry and cell-specific properties of many neurons in a given neural circuit. Multi-electrode arrays (MEAs) offer a scalable alternative - high-density extracellular measurements from fu...

---

### 29. Microsecond-precision sound localization emerges from slow equilibrium dynamics

**Authors:** Toshio Irino

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03890v2) | 📄 [PDF](https://arxiv.org/pdf/2607.03890v2)

**Summary:** Precise sound localization relies on microsecond sensitivity to interaural time differences (ITDs), yet binaural perception exhibits sluggish tracking of dynamic acoustic cues. How microsecond-level ITD sensitivity arises despite such slow responses remains unresolved. This study proposes that ITD is represented as a stable equilibrium of neural population dynamics rather than through the classical place-coding framework based on delay-line coincidence detection. In this framework, excitatory an...

---

### 30. Diffusion learning reveals viable parameter manifolds and compensation geometry in biological dynamical systems

**Authors:** Ruilin Zhang, Louis Tao, Zhuo-Cheng Xiao

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03671v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03671v1)

**Summary:** Models of complex systems often have many parameters, yet are constrained by far fewer experimentally accessible observables: similar activity can emerge from coordinated parameter changes. We formalize these compatible parameter sets as \emph{viable parameter manifolds}: the inverse images of a system's target dynamical behaviors under a parameter-to-feature map. The relevant codimension is not the number of reported features, but the effective rank of that map at the target scale. Co-varying f...

---

### 31. Shunting Inhibition and Dendritic Branching Shape Local Credit Assignment

**Authors:** Houman Safaai, Maceo Richards, Bernardo L. Sabatini

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03556v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03556v1)

**Summary:** Biological neurons assign credit across branching dendrites, where synaptic drive, dendritic conductance, local voltage, and somatic teaching signals interact to shape synaptic plasticity. We study conductance-based dendritic networks with E/I synapse banks, shunting inhibition, and tree-structured branch-to-soma coupling, and examine when restricted somatic feedback can approximate compartment-specific backpropagated errors. Exact gradients factor into local eligibility x compartment error term...

---

### 32. Modeling the Impact of Visual Brand Language on Attention, Object Recognition, and Memory Retrieval

**Authors:** Rachel F. Heaton, John E. Hummel

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02929v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02929v1)

**Summary:** Visual brand language is the set of visual properties that convey brand identity for a product. What is the impact of visual brand language on a person's ability to recognize and understand the functional identity of an object? Using an empirically supported modeling framework based on the JIM model of object recognition and the LISA model of analogical inference, we simulated the impact of visual brand language on object recognition, the allocation of attention, and retrieval of functional info...

---

### 33. A global predicted-fMRI drive signal from TRIBE does not predict YouTube replay heatmaps

**Authors:** Barada Sahu, Shivesh Pandey

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01400v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01400v2)

**Summary:** Deep multimodal brain-encoding models now predict fMRI responses to naturalistic video with high accuracy; whether their predicted neural signals also forecast behavioral engagement is unknown. We run TRIBE, the winning model of the 2025 Algonauts challenge (Llama-3.2 + V-JEPA 2 + Wav2Vec-BERT), on 48 YouTube videos and reduce its predicted cortical response to a per-second engagement curve, the global field power. Correlated against each video's "most replayed" heatmap, a proxy for re-watch, it...

---

### 34. DRIADA: A Python Toolkit for Cross-Scale Analysis of Single-Neuron Selectivity and Population Dynamics

**Authors:** Nikita Pospelov, Viktor Plusnin, Olga Rogozhnikova, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00851v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00851v1)

**Summary:** Brain activity spans single-neuron, population, and network levels, and core questions in neural coding require moving between them. Yet current tools target a single paradigm and incompatible data formats, leaving cross-level questions hard to address. We present DRIADA, an open-source Python framework that unifies neural signals and time-aligned behavior in a shared data model, so selectivity testing, dimensionality reduction, and network analysis operate within a unified workflow. We evaluate...

---

### 35. NeuroCogMap Reveals Cognitive Organization of Large Language Models

**Authors:** Zhongxiang Sun, Haolang Lu, Qiang Ma, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00397v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00397v1)

**Summary:** Understanding how complex cognitive functions are organized within artificial systems is central to interpreting large language models (LLMs) and relating them to biological cognition. Yet although LLMs exhibit broad cognitive-like behaviours, it remains unclear whether their internal representations form reproducible functional systems that explain behaviour, failure and links to human cognition. Here we present NeuroCogMap, a cognitive neuroscience-inspired framework that organizes internal fe...

---

### 36. Stationary covariance spectra of discrete-time non-normal random recurrent dynamics

**Authors:** Jacob A. Zavatone-Veth

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31944v1)

**Summary:** Principal component analysis is widely used to characterize structure in the dynamics of recurrent neural networks. For stationary noise-driven dynamics, the distribution of variance among the principal components is determined by the spectrum of the stationary covariance matrix. While the spectral properties of this matrix are well-understood for linear networks with normal synaptic weight matrices, our understanding of the stationary covariance spectrum for random non-normal dynamics remains i...

---

### 37. Mean-field theory of rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation

**Authors:** Bowen W. Zheng, Earl K. Miller, Ila R. Fiete

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30366v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30366v1)

**Summary:** We develop a dynamical mean-field theory for random recurrent networks with low-rank structure and firing-rate-driven adaptation. When the random connectivity is strong enough to generate chaos, increasing adaptation strength drives the network through four regimes: a static coherent state, noise-sustained oscillations that progress from regular to irregular, stochastic switching between symmetric wells, and a global limit cycle. The theory identifies two instability mechanisms, chaos onset from...

---

### 38. Cohort-amortized personalization: navigating the privacy-utility frontier for virtual brain twins

**Authors:** Amirhossein Esmaeili, Marmaduke Woodman, Nina Baldy, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30329v2) | 📄 [PDF](https://arxiv.org/pdf/2606.30329v2)

**Summary:** Personalized generative brain models require individual neuroimaging data that privacy constraints and re-identification risk make difficult to share, while per-subject fitting procedures cost hours of compute -- limiting clinical translation and multi-site collaboration. We introduce cohort-amortized personalization (CAP), which replaces data sharing with model sharing: a neural density estimator is trained on simulations from a mechanistic whole-brain model under a low-rank cohort prior, and o...

---

### 39. Clear Mind: Meditation and the Brain's Signal-to-Noise Ratio

**Authors:** Ruben Laukkonen

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29698v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29698v1)

**Summary:** Meditation is quintessentially associated with a clear mind. This paper proposes that diverse findings in the science of meditation can be mapped onto a single, empirically tractable construct: functional signal-to-noise ratio in the brain, or f-SNR. Signal denotes neural variance that tracks the goal-relevant causes of sensory input, while noise denotes residual activity, including irrelevant endogenous fluctuations. Mechanistically, meditation increases f-SNR through two primary operations: se...

---

### 40. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 41. Connectivity Estimation using Stochastic Graph Heat Modelling

**Authors:** Stephan Goerttler, Min Wu, Fei He

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29098v1)

**Summary:** A growing number of techniques leverage the spatial structures that underlie many real-world datasets. Despite these advances, the complementary task of estimating spatial structures and understanding their role within these techniques has often been overlooked. In neurophysiological data analysis specifically, numerous methods exist to estimate brain connectivity, but most are not explicitly model-based, dynamic, multivariate, or directed. To address these limitations, we previously introduced ...

---

### 42. Interpretable machine learning predicts Parkinson's disease severity using motion-corrected QSM MRI and multiband multiecho fMRI features

**Authors:** Aixa X. Andrade

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2607.02553v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02553v1)

**Summary:** Introduction: Objective neuroimaging biomarkers may improve Parkinson's disease motor assessment by capturing brain variation not directly observable from clinical examination. We used interpretable machine learning to predict current motor severity, measured by MDS-UPDRS Part III, from QSM and multiband multi-echo resting-state fMRI-derived ReHo features.   Methods: Regional QSM and ReHo features were extracted from 28 participants, including 24 individuals with Parkinson's disease and 4 contro...

---

### 43. Modelling Emotional Memory in Children with Tensor Networks

**Authors:** Henry Groves, Lucia F. Jackson, Barbara-Anne Robertson, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28470v1)

**Summary:** We demonstrate how emotional valence influences the order-dependent structure of children's recognition memory: correct recall of a sequence of emotionally-valenced toys depended not just on the valence of a given toy itself, but also on the valence of the toys shown before and after it. Whilst standard psychological models confirm that order-dependence differs across an event (a set of toys shown in sequence), accuracy is low and the model does not reflect how memory for an emotional object inf...

---

### 44. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 45. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 46. Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks

**Authors:** Mauricio A Diaz, Manuela A. Beyer, Janina Hesse

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27529v1)

**Summary:** Stress is an adaptive response coordinated by neural and physiological systems. While acute stress can enhance survival, chronic stress drives structural brain changes, cognitive dysfunction, and increased psychiatric risk. At the cellular level, chronic stress shifts the excitatory-inhibitory (E/I) balance of prefrontal pyramidal neurons toward inhibitory dominance, yet the mechanisms underlying these alterations are still unknown. We here investigate possible mechanisms causing inhibitory domi...

---

### 47. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 48. Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist

**Authors:** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26448v1)

**Summary:** Across the sciences, autonomous systems are increasingly being used in closed-loop discovery, proposing new theories and designing and running experiments to test them. This approach is yet to be applied in the field of cognitive science, where the central bottleneck is theory-building: the creative step of turning the accumulated failures of existing models into better ones. Theory generation has remained manual even as data collection, modeling, and experiment design have been automated. We pr...

---

### 49. Beyond Single-Source Cognitive Taskonomy:Multi-Source Task Relations through fMRI Transfer Learning

**Authors:** Junfeng Xia, Wendu Li, Mengjiao Zhang, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26279v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26279v1)

**Summary:** Cognitive tasks are organized by shared and specialized neural processes. Masked fMRI reconstruction provides a common self-supervised objective for quantifying transfer relations among task states, but existing reconstruction-based taskonomies mainly study one-to-one transfer from a single source task to a target. Here, we extend an fMRI cognitive taskonomy from single-source to multi-source transfer across 23 Human Connectome Project task states and use Boolean Integer Programming (BIP) to ana...

---

### 50. Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization

**Authors:** Lucas A. T. X. Carneiro, Armand D. Jiofack, Fernando F. Ferreira

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25874v1)

**Summary:** Polychronous Neuronal Groups (PNGs) reproducible, time-locked spatiotemporal firing cascades stabilised by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays provide a combinatorially rich substrate for neural computation whose structural determinants remain poorly understood. We simulate a recurrent network of N=1000 Izhikevich neurons over ten hours of biological time and identify 1545 unique PNGs via an offline event-driven detection algorithm. A parametric Watts-Strogat...

---

## stat.ML

**50 papers**

### 1. Ensemble Controlled-Flow Filtering for Implicit Data Assimilation

**Authors:** Zhuoyuan Li, Yue Zhao, Ming Li

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12975v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12975v1)

**Summary:** Data assimilation estimates the state of a dynamical system from model forecasts and incoming observations. Many observation mechanisms, however, are many-to-one, implicit, non-smooth, or accessible only through simulation, and need not provide the residual structures or likelihood guidance required by existing ensemble filters. We introduce implicit data assimilation, in which the analysis law is defined as an energy tilt of the forecast distribution. We then propose the Ensemble Controlled-flo...

---

### 2. Sharp Optimal Algorithm for Derivative-Free Stochastic Convex Optimization in One Dimension

**Authors:** Alexandra Carpentier, Chloé Rouyer, Alexandre Tsybakov, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12938v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12938v1)

**Summary:** Stochastic convex optimization is a classical problem with well-understood guarantees under first-order feedback. In contrast, for zero-order optimization with noisy function evaluations, a logarithmic gap has persisted between known upper bounds and the $Ω(1/\sqrt{T})$ lower bound, even in the one-dimensional case. In this work, we study the problem of minimizing a convex function $f : [0,1] \to [0,1]$ using a zero-order oracle with subGaussian noise. We propose a computationally efficient algo...

---

### 3. LatentFlow: A General Framework for Conditioning Stochastic Processes

**Authors:** Louis Sharrock, Lachlan Astfalck, Henry Moss

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12922v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12922v1)

**Summary:** Stochastic-process models are, as a rule, far easier to simulate than to condition. Non-linear observations, non-Gaussian likelihoods, black-box information, and global constraints all induce intractable conditional laws, requiring bespoke, model-specific constructions. We introduce LatentFlow, a single framework for conditioning stochastic processes, with no learned neural approximations and no training. Our starting point is to write the stochastic process as the deterministic image of a tract...

---

### 4. Accelerated Mixing Time of Randomized Hamiltonian Monte Carlo

**Authors:** Siddharth Mitra, Vishwak Srinivasan, Xiuyuan Wang, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12902v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12902v1)

**Summary:** We show the Randomized Hamiltonian Monte Carlo (RHMC) algorithm has accelerated mixing time guarantees for sampling from log-concave probability distributions. RHMC proceeds by repeatedly simulating the continuous-time Hamiltonian dynamics for some random integration times, and resetting the velocity to be an independent Gaussian random variable between each simulation. We show that when the target distribution is log-concave and satisfies an $α$-Talagrand inequality (for example, if the target ...

---

### 5. ANGLE: Angular Neural Generative Learning via Engression

**Authors:** Rajdeep Pathak, Archi Roy, Tanujit Chakraborty

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12833v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12833v1)

**Summary:** Circular data, representing angles or directions, are frequently encountered in computer vision, biology, geology, and meteorology. Traditional regression targets the conditional mean, which is often geometrically misleading for circular responses under multimodal, skewed, or asymmetric data structures. To address these limitations, a lightweight deep generative framework, namely ANGLE, is introduced for non-parametric distributional regression on the circle. The full conditional distribution of...

---

### 6. Contrast-Free ICA and Causal Inference via Wasserstein Distances to the Gaussian

**Authors:** Félix Laplante, Christophe Ambroise, Pierre Humbert

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12832v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12832v1)

**Summary:** We study the squared $2$-Wasserstein distance to the standard Gaussian as a non-Gaussianity criterion and use it for linear Independent Component Analysis (ICA) and causal inference in Linear Non-Gaussian Acyclic Models (LiNGAM). The analysis relies on a strict inequality between the Wasserstein non-Gaussianity of independent standardized sources and that of their linear combinations. When at most one source is Gaussian, any unit-norm linear combination involving at least two sources has strictl...

---

### 7. MixCIT: A Kernel Based Local-Polynomial Debiased Test for Conditional Independence on Mixed-Type Data

**Authors:** Mengxiao Gao, Kyra Gan, Promit Ghosal

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12830v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12830v1)

**Summary:** Conditional independence testing (CIT) is fundamental to modern statistical inference in areas related to causal discovery and variable selection. While marginal independence is relatively well-understood, despite multiple advances, no existing non-parametric CIT provides a unified, efficient, and statistically guaranteed solution across heterogeneous data. We introduce a graph-based test statistic comparing kernel similarities of the response within composite neighborhoods that use exact matchi...

---

### 8. What Does Goodness Measure? A Likelihood-Ratio Account of Forward-Forward Learning

**Authors:** Paolo Giannitrapani

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12501v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12501v1)

**Summary:** The Forward-Forward (FF) algorithm trains each layer locally, so that a scalar goodness - the sum of squared activations - is high on real inputs and low on contrastive ones, with activations normalized between layers. Both choices are usually treated as heuristics. Under an explicit generative model they are not: the squared goodness is the sufficient statistic of a likelihood-ratio test between two zero-mean populations differing in scale, and the FF threshold is its boundary. It generalizes: ...

---

### 9. Fisher Rank Inflation: A Spectral Signature of Memorization under Label Noise

**Authors:** Satwik Bathula, Anand A. Joshi

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12438v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12438v1)

**Summary:** Deep networks trained with label noise often learn clean structure before memorizing corrupted labels. We show that this transition leaves a spectral signature in the centered scatter of per-example last-layer gradients. Its effective rank transiently expands during memorization and contracts after corrupted labels are fit. We call this phenomenon Fisher Rank Inflation. Corrupted labels increase effective rank by injecting spectral mass into low-energy or previously unused eigendirections, incre...

---

### 10. PolarBM: Complex-valued Boltzmann Machine for Modeling Audio Signals in Polar and Log-polar Coordinates

**Authors:** Toru Nakashika, Kohei Yatabe

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12417v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12417v1)

**Summary:** Although vast amounts of data, such as audio signal spectra, are naturally represented using complex numbers, conventional machine learning methods often simplify complex-domain problems by employing frameworks designed for real-valued variables. While this simplification offers computational benefits, it discards structural information regarding the inherent relationship between amplitude and phase. In this paper, we propose a novel Boltzmann machine (BM), named PolarBM, capable of naturally ha...

---

### 11. Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring

**Authors:** Abdullah Karasan, Alper Hekimoğlu

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12407v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12407v1)

**Summary:** Divergence measures are essential tools for detecting distributional shifts in model monitoring, particularly crucial given the volatility of financial data. While the Population Stability Index is the most widely used measure, Jensen-Shannon Divergence and Kullback-Leibler Divergence offer distinct advantages. Jensen-Shannon Divergence handles mixture models, addresses zero-binning problems, and is symmetric, while Kullback-Leibler Divergence excels in Bayesian model comparison.   This study ex...

---

### 12. Thompson Sampling Is 2-Competitive for Mistakes

**Authors:** Mark Sellke, Gregory Valiant

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12389v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12389v1)

**Summary:** We consider Bayesian bandit models and prove that Thompson sampling makes at most twice the expected number of mistakes (selections of a suboptimal arm) as any other policy. Our analysis applies as long as the latent arm processes are independent and each arm evolves only when played. For stochastic bandits with best arm defined via mean reward, this confirms a conjecture of Guha and Munagala from 2014, where the factor $2$ is already best possible. The result holds under any nonincreasing seque...

---

### 13. Forecasting Inflation with Microdata: An Adaptive Machine Learning Approach

**Authors:** Catherine Chen, Chen Gao, Jonathon Hazell, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12345v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12345v1)

**Summary:** Does microeconomic heterogeneity help to forecast aggregate inflation in a non-stationary environment? We develop a scan test for whether one forecast outperforms another, over an interval with unknown starting point and duration. To exploit any occasional forecasting power that the scan test detects, we design an adaptive machine learning pipeline. We encode the distribution of price changes into a high-dimensional vector, which we combine with a gradient boosted trees algorithm. We then combin...

---

### 14. Cluster-Weighted EDMD

**Authors:** Lorenzo Tomaz, Judd Rosenblatt, Flavio Kicis, et al.

**Published:** 2026-07-14

🔗 [Paper](http://arxiv.org/abs/2607.12243v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12243v1)

**Summary:** Extended Dynamic Mode Decomposition (EDMD) approximates Koopman operators from data, but a single global operator is inefficient when different state-space regions exhibit distinct local dynamics. We introduce Cluster-Weighted EDMD (CW-EDMD), which jointly learns a soft phase-space partition and a per-cluster EDMD operator. Its Expectation-Maximization (EM) objective assigns each transition based on both geometric proximity and prediction residuals, so clusters specialize where local Koopman mod...

---

### 15. Falsifying Causal Graphs With Outlier Events

**Authors:** William Roy Orchard, Philipp M. Faller, Dominik Janzing

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12145v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12145v1)

**Summary:** True causal relationships are rarely known, and inferring causal graphs from data is hard. A fundamental challenge is how to assess whether a given causal graph is good in the absence of a ground truth. We propose falsifying candidate causal graphs based on whether they can explain the propagation of an outlier event. Our approach leverages a key principle: weak outliers rarely cause strong ones. While this principle has previously been used in root cause analysis to identify root causes without...

---

### 16. Causal Graphs, Markov Properties and Do-calculus for Stochastic Differential Equations

**Authors:** Philip Boeken, Joris M. Mooij

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12140v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12140v1)

**Summary:** Stochastic differential equations (SDEs) are widely used to model continuous-time dynamical systems, but graphical causal models for them are not yet well-understood. We consider systems of causal SDEs that are equipped with an explicit causal semantics. We pose solvability conditions for systems of causal SDEs such that they have well-defined observational and interventional distributions - even after marginalisation - and provide a general class of Lipschitz semimartingale SDEs that satisfies ...

---

### 17. Dynamic Online Processor-Native Inference for State Estimation

**Authors:** Orestis Kaparounakis

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12095v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12095v1)

**Summary:** Sensor-rich data-driven applications increasingly use Bayesian approaches to infer latent states of dynamic systems from noisy sensor measurements and physical models. Yet the computation of the likelihood remains an essential bottleneck for accurate posteriors and performant inference. This paper presents a Bayesian filtering technique that uses processor-native uncertainty tracking for both uncertainty propagation and inference. The technique implements deterministic hierarchical importance re...

---

### 18. Learning the Graphical Nature of Symmetries

**Authors:** Rashid Barket, Enrico Grimaldi, Yacoub Hendi, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.12026v1) | 📄 [PDF](https://arxiv.org/pdf/2607.12026v1)

**Summary:** Finite groups are rigid algebraic objects, whose Cayley graphs expose a rich network geometry through which group-theoretic structure can be measured, compared, and learned. In this paper, a dataset of $131{,}406$ Cayley graphs is constructed, covering all groups of order at most $767$ except order $512$, recording exact algebraic labels for group properties together with a broad collection of graph, cycle, distance, and spectral statistics. This census aims to provide novel benchmarks for study...

---

### 19. Relaxing Faithfulness with Intervention-Only Causal Discovery

**Authors:** Bijan Mazaheri, Jiaqi Zhang, Caroline Uhler

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11816v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11816v1)

**Summary:** Causal discovery algorithms learn a network that describes the causal dependencies among random variables. A common workflow involves first utilizing conditional independence properties on observational data to determine partially directed causal relationships, then applying interventions to orient the unknown causal directions. A critical assumption for the first step is faithfulness: a requirement that causally linked variables exhibit statistical dependence. Many natural systems include buffe...

---

### 20. Are we Merging the Right Models? Impact of Expert Training Duration on Model Merging for LLMs

**Authors:** Nikita Kozodoi, Zainab Afolabi, Jack Butler

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11997v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11997v1)

**Summary:** Multi-task model merging combines separately trained expert models into a single model that handles all tasks without co-training. Standard practice merges experts at their optimal validation loss. We challenge this convention by systematically studying how training duration of domain experts affects the quality of the merged model. We fine-tune experts on five domains (Math, Code, Instruction Following, Multilingual, and Safety) across three model sizes (Qwen 3.5 0.8B, 2B, and 4B), saving check...

---

### 21. Diversified Multinomial Logit Contextual Bandits

**Authors:** Heesang Ann, Taehyun Hwang, Min-hwan Oh

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11684v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11684v1)

**Summary:** Existing contextual multinomial logit (MNL) bandits model relevance-driven choice but ignore the potential benefits of within-assortment diversity, while submodular/combinatorial bandits encode diversity in rewards but lack structured choice probabilities. We bridge this gap with the $\textit{diversified multinomial logit}$ (DMNL) contextual bandit, which augments MNL choice probabilities with a generally submodular diversity function, thereby formalizing the relevance--diversity trade-off withi...

---

### 22. Bet on Features: Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters

**Authors:** Ivane Antonov, Sohom Mukherjee, Richard Pibernik, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11653v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11653v1)

**Summary:** Black-box conditional quantile forecasts are widely used for sequential decisions under asymmetric costs, such as inventory planning in supply chain management. Once deployed, such forecasters must be monitored continuously as data streams drift and regimes change; this invalidates standard, fixed-horizon backtests for calibration. Further, existing backtests do not take into account that the notion of calibration is, in fact, information-dependent: forecasts can look calibrated to an auditor wi...

---

### 23. Fundamental Limitations of Fixed-Budget Best-Arm Identification

**Authors:** Motti Goldberger

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11635v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11635v1)

**Summary:** In fixed-budget best-arm identification, also known as ranking and selection, an algorithm has a sampling budget to distribute across $K$ arms. Each sample provides noisy feedback about that arm's mean, and the goal is to identify the arm with the largest mean. A common performance benchmark is the static oracle: a non-adaptive strategy that knows the means in advance and chooses fixed sampling proportions to maximize the exponential decay rate of the probability of incorrect identification. Sev...

---

### 24. Markov Chain Monte Carlo with Diffusion Paths

**Authors:** Han Chen, Sifan Liu, Jun Yang

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11631v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11631v1)

**Summary:** Sampling from multimodal distributions is a longstanding challenge for classical local Markov chain Monte Carlo (MCMC) methods. A popular remedy is to introduce a sequence of intermediate distributions that interpolate between the target and a simpler reference. The classical choice, tempering, raises the density to a power, but distorts the relative weights of asymmetric modes and can lead to poor mixing. We instead propose interpolating along the diffusion path, the marginals of a noising diff...

---

### 25. Auditing the Risk Claims of Distributional Reinforcement Learning

**Authors:** Hari Prasad

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11607v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11607v1)

**Summary:** Distributional reinforcement learning agents learn full return distributions that are increasingly read at face value: for interpretability, risk-sensitive control, and safety monitoring. We ask a question theory anticipates but that has not been measured directly: are the risk claims of a trained distributional agent true? Our audit combines a decision-relevant screening metric (the excess Wasserstein gap between the top two actions, which equals the mass by which first-order stochastic dominan...

---

### 26. Removable Defects: The Economics and Limits of Deliberate Deficiency

**Authors:** Cheng Qian

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11983v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11983v1)

**Summary:** A specialist tolerates blind spots that a generalist does not. Usually this is treated as a cost to be minimized. We treat it as a design variable: a deficiency can be kept because it pays and removed on demand in the rare situation where it would be fatal, by routing to a compensation channel. We give three results. First, an advantage condition under which keeping the deficiency is a computable economic position; structurally it is the Ehrlich-Becker market-vs-self-insurance margin applied to ...

---

### 27. DAG-FM: A Foundation Model for Causal Discovery under Heterogeneous Causal Mechanisms

**Authors:** Yikang Chen, Zhengkang Guan, Haoyuan Qian, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11510v1)

**Summary:** Causal discovery from observational tabular data remains fundamentally challenging, primarily due to the heterogeneity of underlying causal mechanisms and the high-dimensional combinatorial search space of Directed Acyclic Graphs (DAGs). In this paper, we propose \textbf{DAG-FM}, a novel foundation model architecture that amortizes causal discovery. Unlike direct matrix prediction, DAG-FM decomposes the causal discovery process into two auto-regressive stages using two specialized Transformer-ba...

---

### 28. CDFM: Towards a General-Purpose Causal Discovery Foundation Model

**Authors:** Jie Qiao, Ruichu Cai, Zijian Li, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11508v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11508v1)

**Summary:** Causal discovery, the process of recovering underlying causal structures from observational data, is a fundamental pursuit across scientific disciplines. Over the past decades, numerous algorithms have been developed to tackle this challenge through workflows tailored to the specific causal mechanisms underlying each type of dataset, demonstrating effectiveness across a wide range of applications. However, as the volume and heterogeneity of real-world data continue to grow, this dataset-specific...

---

### 29. Robust Subgroup Analysis for Heterogeneous Censored Data

**Authors:** Zhaohui Xu, Daoji Li, Zemin Zheng

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11389v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11389v1)

**Summary:** Subgroup analysis is important in practice because real-world data typically come from heterogeneous populations, where meaningful patterns can differ substantially across subpopulations. Correctly identifying these subgroups can improve prediction accuracy, prevent biased or misleading conclusions, and support more effective, targeted decision-making. While most existing subgroup analysis methods are developed for complete data, in this paper we propose a novel and robust approach for censored ...

---

### 30. Learning to control switching nonlinear systems with Koopman operator regression

**Authors:** Edoardo Caldarelli, Oleksii Kachaiev, Cesare Molinari, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11344v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11344v1)

**Summary:** In this work, we consider the identification and control of nonlinear systems with finite action spaces. The unknown dynamics are estimated from finite samples with Koopman operator regression in a reproducing kernel Hilbert space, yielding a linear switching predictive model, the switches governed by the value of the control variable. In order to perform control in closed-loop, the learned dynamics are employed in an infinite-horizon optimal control problem with time-varying stage cost, which i...

---

### 31. Long-Memory Reservoir Computing for Data-Scarce Dengue Forecasting

**Authors:** Rahul Goswami, Shinjini Paul, Palash Ghosh, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11272v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11272v1)

**Summary:** Accurate dengue forecasting is crucial for public health planning, but remains challenging because incidence series are often short, noisy, non-stationary, nonlinear, and often affected by long-range temporal dependence. Fractional differencing in Autoregressive Fractionally Integrated Moving Average (ARFIMA) helps balance non-stationarity and persistence, but its linear structure limits its ability to capture nonlinear dynamics. Deep neural networks can model nonlinear patterns, but usually req...

---

### 32. Trustworthy synthetic data for campaign decision support: strategy simulation fidelity and the PolicySynth framework

**Authors:** Tung Dang, The Hung Phung, Son Lam Nguyen, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11269v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11269v1)

**Summary:** Decision support systems (DSS) increasingly run retention what-if analysis on synthetic customer populations, because privacy constraints preclude unrestricted use of real data. Such a system is trustworthy only if the synthetic data lead managers to the same decisions as the real data would; yet prevailing criteria certify distributional similarity, not decision alignment, so a synthetic population can match every marginal distribution while still steering a marketing team toward the wrong camp...

---

### 33. NeuroMem-FHP: A Likelihood-Free Deep Learning Framework for Parameter Estimation of Fractional Hawkes Process

**Authors:** Neha Gupta, Aditya Maheshwari

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11177v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11177v1)

**Summary:** In this paper, we propose deep learning based NeuroMem-FHP framework for estimating the parameters of the fractional Hawkes process (FHP), a self-exciting point process that captures long-range dependence through a fractional Mittag-Leffler excitation kernel. Two neural architectures, namely a Long Short-Term Memory (LSTM) network and a Transformer, are developed to estimate the model parameters $(μ,γ,α,β)$ directly from sequences of inter-arrival times without requiring computationally intensiv...

---

### 34. Rank-Conditioned Sample Reuse for the Plackett--Luce Best-of-$K$ Objective

**Authors:** Melveena Jolly, Midhun Xavier

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11146v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11146v1)

**Summary:** We study the coupled objective J_K^WOR = E_{S ~ PL-WOR_K}[max_{i in S} R_i]: the expected maximum reward of a size-K Plackett-Luce draw without replacement, the law of Gumbel-Top-K / Stochastic Beam Search decoding. This estimand differs from the conventional i.i.d. objective J_K^iid = E[max_{i<=K} R_i] targeted by existing sample-reuse Max@K estimators, and reusing their i.i.d. weights under the coupled sampler is provably biased (a closed-form three-item instance gives E[g_iid] = (4/5) grad J_...

---

### 35. Difference-Driven Gating: Adaptive Feature Fusion for U-Net Decoder

**Authors:** Kai Li, Xuechao Zou, Jiashen Fu, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11096v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11096v1)

**Summary:** The U-Net style models have been widely used in many applications. A critical step in these models is to reconstruct the lower-level features using a top-down decoder. This reconstruction requires precise fusion of high-level semantics and low-level details. Existing attention-based fusion methods typically derive attention weights from the top-down decoder features (global) alone or the correlation between the top-down decoder features and the bottom-up encoder features (local), then modulate t...

---

### 36. Adapting Evidential Neural Networks to Test-Time Neighbor Fusion Improves Molecular Property Prediction

**Authors:** Cameron Gruich, Weichi Yao, Yixin Wang, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11091v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11091v1)

**Summary:** A trained molecular property model can be refined at test time by correcting each prediction with the measured labels of the most similar training molecules, a retraining-free procedure we call neighbor fusion; evidential neural networks make it principled by using their aleatoric and epistemic uncertainty to parameterize a Bayesian update. Our main contribution, PG-EVIKAL, learns a property-distance metric to re-rank structurally similar neighbors by their property relevance before fusion, buil...

---

### 37. Actor-Critic Learning for Extended Mean Field Control with Deterministic Policies

**Authors:** Ziheng Cheng, Xin Guo, Huyên Pham, et al.

**Published:** 2026-07-13

🔗 [Paper](http://arxiv.org/abs/2607.11005v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11005v1)

**Summary:** This paper develops a model-free reinforcement learning framework for continuous--time extended mean field control problems, where both the dynamics and reward may depend on the joint distribution of states and controls. We adopt deterministic feedback policies, under which the state--action distribution is induced directly as a push--forward of the state law. This avoids optimization over stochastic kernels and bypasses key limitations of existing approaches in extended mean field settings.   W...

---

### 38. Reinforcement Learning for Execution under Dynamic Fees in a Closed-Loop DEX Simulator

**Authors:** Wen-Ting Wang

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10960v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10960v1)

**Summary:** Trader-facing dynamic fees are increasingly proposed for automated market makers (AMMs), but historical data do not identify how order flow would respond: trader-facing fees do not vary, trader types are latent, and a replayed tape is not a sequential decision environment. We therefore construct a minimal closed-loop simulator in which the missing signal exists by construction: two constant-product pools repriced by an equilibrium-inspired dynamic-fee rule, fee-sensitive noise flow, and closed-f...

---

### 39. WSqD: A Horizon-Free Learning Rate Schedule for Large Model Training

**Authors:** Jianhao Ma, Yuxin Chen

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10959v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10959v1)

**Summary:** Standard learning rate schedules such as cosine annealing are tied to a fixed training horizon, limiting their ability to accommodate post hoc horizon extension. Warmup-stable-decay (WSD) partially addresses this issue by maintaining a long constant-rate phase before a short linear cooldown, allowing training to resume from a pre-decay checkpoint. However, its peak learning rate is still tuned based on the original training horizon and can become suboptimal when training is extended. Motivated b...

---

### 40. Sticky Jump Diffusions: A Unifying View of Masked, Continuous, and Hybrid Diffusion

**Authors:** Pascal Jutras-Dubé, Patrick Pynadath, Jeremy Lu, et al.

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10951v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10951v1)

**Summary:** We introduce Sticky Jump Diffusions (SJDs), continuous-time Markov processes on $\mathbb R^d$ whose discrete anchors are token embeddings. In forward time, anchors release their mass at a hazard rate and the released mass diffuses in the continuous ambient space; time reversal couples a score-driven SDE with a sticky jump kernel whose rate and destination are fixed by flux balance with the forward law. We estimate the score and the per-anchor reverse hazards from a single denoising classifier vi...

---

### 41. Did We Actually Fix It? An Independent Adversarial Stress-Test of Post-Point-Adjustment Evaluation Metrics for Time-Series Anomaly Detection

**Authors:** Zongye Lyu

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.11969v1) | 📄 [PDF](https://arxiv.org/pdf/2607.11969v1)

**Summary:** Point-adjustment (PA), long the default scoring protocol in time-series anomaly detection (TSAD), was shown by Kim et al. (2022) to award near-perfect F1 to random scores. The field migrated to replacement metrics: PA%K, range-based precision/recall, affiliation precision/recall, and Volume-Under-the-Surface (VUS) ROC/PR. But did the fix work? Every robustness check to date is proposer-run or theoretical; no independent, adversarial, SOTA-relative audit on real benchmarks exists. We provide one....

---

### 42. Bandit PCA with Minimax Optimal Regret

**Authors:** Moïse Blanchard, Dmitrii Ostrovskii, Aadirupa Saha

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10936v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10936v1)

**Summary:** We study the bandit-feedback version of online principal component analysis (Bandit PCA): in each round $t = 1,\dots,T$, the adversary selects a $d \times d$ symmetric gain matrix $G_t$ with spectrum in $[0,1]$ and rank at most $r$; the learner simultaneously selects a unit vector $w_t \in S^{d-1}$ and receives the reward $w_t^\top G_t w_t$. The learner receives no other feedback, and aims to minimize the regret against the best unit vector in hindsight. This problem was introduced by Kotlowski ...

---

### 43. Fast Whole-Brain, Geometry-Aware Functional Alignment for Cross-Subject Decoding

**Authors:** Pierre-Louis Barbarant, Florent Meyniel, Bertrand Thirion

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10931v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10931v1)

**Summary:** Decoding brain activity is useful for characterizing brain processes and understanding the functional architecture underlying cognition. However, the inter-individual variability in brain response patterns limits the development of decoders that generalize across individuals. A solution to this challenge is functional alignment: aligning functional data across individuals before training population-level decoders. The core issue is to strike the balance between aligning functional features and p...

---

### 44. The Spectral Structure of Latent Treatment Effects

**Authors:** Hamza Virk, Bijan Mazaheri, Yihren Wu

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10926v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10926v1)

**Summary:** Identifying heterogeneous treatment effects under unobserved confounding is central in observational causal inference. In proxy models with a discrete latent confounder, prior Synthetic Potential Outcomes (SPO) [Mazaheri-Squires-Uhler '25] recover the mixture of treatment effects through recursively constructed scalar moments. We show that this sequence is one projection of a more fundamental object. Under the same population factorization assumptions, there is an exact compressed observable ope...

---

### 45. Incremental Transformer for Surrogate-Based Inverse Design of Geopolymer Mixtures

**Authors:** Giansalvo Cirrincione, Filippo Grassia

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10896v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10896v1)

**Summary:** Small-data inverse design is challenging in engineering informatics when observations are heterogeneous, mixed-type, and constrained by physical relations among design variables. This work proposes a topology-aware surrogate framework guided by an Incremental Transformer (INCRT) for physics-constrained inverse design, applied to geopolymer mixture design. The method integrates intrinsic-dimensionality analysis, mixed-variable design-space representation, tabular surrogate prediction, INCRT-based...

---

### 46. GNet: A scalable and flexible Gaussian process network with nonparametric neurons

**Authors:** Mengyang Gu

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10735v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10735v1)

**Summary:** We develop GNet, a scalable and flexible Gaussian process network with nonparametric activation functions modeled by Gaussian processes. To reduce computational and storage costs, we introduce the jointly inverse Kalman filter, a fast algorithm together with closed-form expressions of gradients for accelerating model training and predictions without the need to form covariance matrices. Using a unified optimization setting, GNet shows competitive performance across a diverse range of test proble...

---

### 47. An Extreme Value Perspective on Learning Stress Laws

**Authors:** Mantu Gupta, Anand Deo

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10700v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10700v1)

**Summary:** We introduce Self-Similar Generative Estimation (SS-GEN), a method for simulating multivariate tail events and estimating rare-event probabilities in both heavy and light-tailed settings. SS-GEN exploits asymptotic tail structure to decompose the tail distribution into an explicit radial component and a nonparametric angular component, reducing tail learning to a compact-domain problem that can be handled by off-the-shelf deep generative models. The resulting sampler generates representative ext...

---

### 48. Edge Cluster Expansion with Radial Rotary Attention for Interatomic Potentials

**Authors:** Zemin Xu, Wenbo Xie, P. Hu

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10664v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10664v1)

**Summary:** In this paper, we provide a systematic investigation of SO(2) theory to machine learning interatomic potentials (MLIPs) and identify the limitations of conventional SO(2) Linear architectures relative to SO(3) Clebsch-Gordan Tensor Products (CGTP). Building on these insights, we propose direct Cartesian construction and recursive Clebsch-Gordan construction of Wigner D-matrices and introduce two novel interaction building blocks. First, we propose the Edge Complex Product Basis based on Generali...

---

### 49. Demixing Sparse Signals from Nonlinear Observations using Generalized Non-convex Regularization

**Authors:** Raziyeh Takbiri

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10618v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10618v1)

**Summary:** We consider the recovery of a pair of sparse vectors from a limited number of nonlinear observations of their superposition: $y_i=g(\inner{\ba_i}{\bPhi\bw^\ast+\bPsi\bz^\ast})+e_i$, $i=1,\dots,m$, with $m\ll n$, incoherent orthonormal bases $\bPhi,\bPsi$, a scalar link $g$, and noise $e_i$ that may be heavy-tailed or contaminated. We propose a regularization-based framework combining a Huberized data fidelity with generalized folded-concave penalties (SCAD, MCP), and a two-block proximal alterna...

---

### 50. Approximation of Analytic Functions by ReLU Neural Networks with Adjustable Depth and Width

**Authors:** Yanming Lai, Defeng Sun, Yang Wang

**Published:** 2026-07-12

🔗 [Paper](http://arxiv.org/abs/2607.10589v1) | 📄 [PDF](https://arxiv.org/pdf/2607.10589v1)

**Summary:** In contrast to most studies on neural network approximation theory that characterize results through a single parameter, such as the total number of network parameters, \cite{shen2020deep} pioneered the characterization of approximation rates as a joint function of the width parameter $N$ and the depth parameter $L$, thereby granting greater architectural flexibility. Existing works using the $(N,L)$-characterization focus on function classes with finite smoothness $s$, establishing a typical ap...

---

