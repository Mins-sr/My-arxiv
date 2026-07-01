# arXiv Daily Digest - 2026-07-01

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision

**Authors:** Zifan Carl Guo, Laura Ruis, Jacob Andreas, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32038v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32038v1)

**Summary:** When does training language models (LMs) to generate explanations of their predictions yield faithful introspection, rather than superficial imitation? We study LMs trained to explain which features of their inputs influenced their behavior, using models' counterfactual behavior on modified inputs as supervision. Surprisingly, we find that LMs trained on fixed counterfactual explanations derived from earlier checkpoints of themselves, or even from behaviorally similar models in different familie...

---

### 2. QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents

**Authors:** Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32034v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32034v1)

**Summary:** LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream perfo...

---

### 3. Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs

**Authors:** Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32032v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32032v1)

**Summary:** Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal uncertainty--undermining trustworthiness and reliability. Since monitoring task performance and adapting behavior accordingly are central to metacognition, we posit that models capab...

---

### 4. When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors

**Authors:** Yuqing Yang, Qi Zhu, Zhen Han, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32029v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32029v1)

**Summary:** While large language models (LLMs) perform well on table tasks, they still make data referencing errors (DREs), i.e., incorrectly citing or omitting table values, despite understanding the table structure. Beyond final-answer accuracy, DREs directly compromise the correctness and reliability of intermediate reasoning steps. Yet prior studies have only offered limited, small-scale analyses. In this work, we present the first systematic evaluation of tabular data referencing errors across differen...

---

### 5. Freeform Preference Learning for Robotic Manipulation

**Authors:** Marcel Torne, Anubha Mahajan, Abhijnya Bhat, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32027v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32027v1)

**Summary:** Reward design remains a central bottleneck for autonomous robot policy improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two trajectories is better overall, FPL lets them define natural-...

---

### 6. AdaJEPA: An Adaptive Latent World Model

**Authors:** Ying Wang, Oumayma Bounou, Yann LeCun, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32026v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32026v1)

**Summary:** Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes ...

---

### 7. FLORA: A deep learning approach to predict forest attributes from heterogeneous LiDAR data

**Authors:** Emilie Vautier, Clément Mallet, Cédric Vega

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32023v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32023v1)

**Summary:** Forest attributes are essential for national-scale resource monitoring. Airborne LiDAR metrics are among the auxiliary variables most strongly correlated with forest attributes used in National Forest Inventory (NFI) estimates. However, producing wall-to-wall predictions remains challenging when LiDAR data are acquired under heterogeneous conditions. As national LiDAR programs expand across Europe, variability in sensors, flight parameters, seasons, and scan angles limits the robustness of exist...

---

### 8. TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

**Authors:** Yuanda Xu, Zhengze Zhou, Hejian Sang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32017v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32017v1)

**Summary:** Agentic reinforcement learning requires assigning credit to environment-facing actions such as searches, clicks, edits, navigation commands, and object interactions. Standard GRPO uses the final verifier outcome as a uniform advantage over all action tokens. This outcome signal is useful but structurally incomplete: it punishes useful exploration in failed rollouts and reinforces redundant or regressive actions in successful rollouts. We propose TRIAGE, a role-typed credit assignment framework t...

---

### 9. AxDafny: Agentic Verified Code Generation in Dafny

**Authors:** Benjamin Breen, Austin Letson, Borja Requena Pozo, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32007v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32007v1)

**Summary:** We study agentic code generation in Dafny, where a model must generate both executable code and the proof artifacts for verification. We present AxDafny, a verifier-guided repair framework that iteratively generates implementations, invariants, assertions, and termination arguments. We also introduce LiveCodeBench-Pro-Dafny (LCB-Pro-Dafny), a benchmark of 250 competition-style programming problems translated into Dafny with formal specifications and a verifier-based evaluation harness. On LCB-Pr...

---

### 10. PolicyGuard: From Organizational Policies to Neuro-SymbolicCompliance Review Engines

**Authors:** Sameer Malik, Ayush Singh, Amar Prakash Azad

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32004v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32004v1)

**Summary:** Policy-grounded document review requires determining whether a target document complies with organization-specific policies, guidelines, or playbooks. While large language models can assist with policy interpretation and document analysis, end-to-end prompting leaves the applied policy logic implicit, making compliance decisions difficult to inspect, update, and test. We present PolicyGuard, a neuro-symbolic framework for policy-grounded document compliance review. PolicyGuard converts organizat...

---

### 11. Self-Study Reconsidered: The Hidden Fragility of Learning from Self-Generated QA

**Authors:** Ekaterina Alimaskina, Denis Shveykin, Gleb Molodtsov, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32002v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32002v1)

**Summary:** Language models are increasingly taught from synthetic question--answer (QA) supervision: a model generates questions about a document, answers them from the same text, and the resulting pairs are used to fine-tune, distill, or compress knowledge into another model. We show that this generation step is not neutral preprocessing. It is an implicit policy that both selects which evidence becomes training signal and decides how that evidence is answered, and it is fragile at both stages. When choos...

---

### 12. Radial Suppression Accelerates Algorithmic Generalization: A Geometric Analysis of Delayed Generalization

**Authors:** Srijan Tiwari, Aditya Chauhan, Manjot Singh

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32000v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32000v1)

**Summary:** Why do neural networks memorize algorithmic training data long before they generalize? We present a geometric case study demonstrating that, on tasks where generalization requires discovering structured low-dimensional circuits, the memorization-generalization delay is driven by radial inflation of hidden representations under cross-entropy optimization. We formalize a radial-angular decomposition of activation-space dynamics and derive three testable propositions: (i) that penalizing radial inf...

---

### 13. Amplifying Membership Signal Through Chained Regeneration

**Authors:** Wojciech Łapacz, Stanisław Pawlak

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31991v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31991v1)

**Summary:** The tendency of large generative models to memorize training data makes sample verification critical for privacy auditing and copyright enforcement. Current membership (MIA) and dataset inference (DI) attacks often rely on one-shot generations, which yield weak signals and limited sensitivity across modalities. Inspired by Model Autophagy Disorder (MAD), we introduce MADreMIA, a model-agnostic framework that enhances white-, gray-, and black-box MIA and DI. Rather than relying on shadow model tr...

---

### 14. GR2 Technical Report

**Authors:** Yufei Li, Zaiwei Zhang, Mingfu Liang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31984v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31984v1)

**Summary:** Industrial recommendation systems serve billions of users through a multi-stage funnel -- retrieval, early-stage ranking, and re-ranking -- where the final re-ranking step disproportionately shapes user engagement and downstream performance, particularly for carousel and grid display formats. Despite growing enthusiasm for Large Language Models (LLMs) in recommendation, three gaps hinder industrial adoption: (1) most efforts target retrieval and ranking, leaving re-ranking -- the stage closest t...

---

### 15. LUNA: Learning Universal 3D Human Animation Beyond Skinning

**Authors:** Peng Li, Rawal Khirodkar, Junxuan Li, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31981v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31981v1)

**Summary:** Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often introduce artifacts due to imperfect fitting. We propose LUNA, an LBS-free universal neural animation model that directly maps multiple 2D controls like images, keypoints, sketches, and unseen characters into 3D Gaussian deformations, bypassing explicit body fitting. At its core, a transformer-based moti...

---

### 16. TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling in Forestry via Compiled Expert Rules and Vision-Language Models

**Authors:** Shiyi Chen, Nicholas Saban, Collin Hargreaves, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31976v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31976v1)

**Summary:** Human-labeled data are widely used as reference annotations in ML, despite known variability across annotators in many expert-driven domains. In addition, expert annotation is slow, inconsistent, and remains a major bottleneck for scaling tasks like tree height bias classification in forestry remote sensing. We propose a multi-agent system (MAS) that orchestrates expert decision trees with Vision-Language Models (VLMs), treating the decision tree as a structural prior while VLMs perform localize...

---

### 17. MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments

**Authors:** Qingyun Liu, Jiwen Zhang, Jingyi Hu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31966v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31966v1)

**Summary:** Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration genera...

---

### 18. LeCropFollow: Latent Space Planning for Navigation in Unstructured Crop Fields

**Authors:** Felipe Tommaselli, Francisco Affonso, Arthur Pompeu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31941v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31941v1)

**Summary:** Unstructured navigational features, such as irregular planting or discontinuities, remain the primary failure mode for under-canopy agricultural robots. Existing geometric approaches often fail in these scenarios because they compress high-dimensional visual data into deterministic spatial references, effectively discarding the uncertainty and semantic context required to navigate ambiguous terrain. To address this, we present LeCropFollow, a visual navigation framework that bypasses explicit ge...

---

### 19. MVP-Nav: Multi-layer Value Map Planner Navigator

**Authors:** Wenyuan Xie, Shaokai Wu, Yijin Zhou, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31919v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31919v1)

**Summary:** Zero-shot Object Goal Navigation (ZSON) with RGB-only perception poses a fundamental challenge for embodied agents, as the absence of explicit depth information introduces severe physical uncertainty and semantic-physical misalignment. Existing approaches either rely on high-level semantic reasoning without geometric grounding or learn end-to-end policies that lack explicit physical constraints, often resulting in semantically plausible but physically unsafe behaviors. In this paper, we propose ...

---

### 20. Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference

**Authors:** Zhaoyang Luo, Runmin Dong, Miao Yang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31903v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31903v1)

**Summary:** Multimodal large language models (MLLMs) increasingly process long visual-token sequences, increasing the overall inference computation. Existing acceleration methods usually remove visual tokens or skip visual-token updates in entire layers, but these coarse strategies may discard fine-grained evidence or suppress useful operators together with redundant ones. In this paper, we study visual-token computation from an answer-observable perspective and find that late visual-token updates can remai...

---

### 21. Better Understanding, Understanding Better

**Authors:** Yu Wei

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31892v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31892v1)

**Summary:** "Any fool can know; the point is to understand." A well-known remark often attributed to Einstein captures a widely shared intuition: understanding is more than merely knowing. Yet epistemic logic has paid relatively little attention to understanding, despite its central role in contemporary epistemology, philosophy of science, and recent debates about AI. A recurring theme in the philosophical literature is that, unlike knowledge, understanding comes in degrees: one may understand something mor...

---

### 22. Modal CEGAR-tableaux with RECAR and resolution-based SAT-shortcuts

**Authors:** Rajeev Goré, Cormac Kikkert

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31878v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31878v1)

**Summary:** We investigate two approaches for extending CEGAR-tableaux with SAT-shortcuts using a previously known approach called RECAR but also a totally new approach using the modal resolution theorem prover KSP  as an oracle. Our experiments using our C++ implementation CEGARBox++ of CEGAR-tableaux show that:   (1) CEGARBox++ with RECAR SAT-shortcuts is not competitive   (2) CEGARBox++ using KSP to provide SAT-shortcuts is superior to both CEGARBox++ and KSP,   particularly on large satisfiable problems...

---

### 23. Harnessing Textual Refusal Directions for Multimodal Safety

**Authors:** Moreno D'Incà, Massimiliano Mancini, Nicu Sebe

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31876v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31876v1)

**Summary:** To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary f...

---

### 24. Belief Contraction in Dynamic Epistemic Logic

**Authors:** Gaia Belardinelli, Snow Zhang

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31861v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31861v1)

**Summary:** Dynamic epistemic logic represents belief change via model transformations induced by epistemic events. Its standard formulation (Baltag, Moss, Solecki, 1998) provides a natural account of belief expansion through the elimination of possibilities, but it cannot model belief contraction about factual propositions. A classic response enriches Kripke models with plausibility orderings, representing contraction as an update that promotes certain possibilities over others. We show that this approach ...

---

### 25. Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models

**Authors:** Lang Cao, Renhong Chen, Luyi Li, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31846v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31846v1)

**Summary:** Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top ...

---

### 26. Bridging Local Observation and Global Simulation in Closed-Loop Traffic Modeling

**Authors:** Ziyan Wang, Tan Xiang, Peng Chen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31844v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31844v1)

**Summary:** A local-to-global context mismatch arises when autoregressive traffic simulators trained on ego-centric driving logs are deployed in globally observable closed-loop environments. In such logs, the ego vehicle has rich local observations, while surrounding agents are only partially observed due to perception limits and occlusions. As a result, simulators may learn incomplete context--action mappings that remain hidden in log-based training but emerge during closed-loop rollouts, leading to unreal...

---

### 27. Real-Time Source-Free Object Detection

**Authors:** Sairam VCR, Varun Gopal, Poornima Jain, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31834v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31834v1)

**Summary:** Real-world detectors for autonomous driving, surveillance, and robotics must handle domain-shifts under strict latency and memory constraints, yet existing source-free object detection (SFOD) methods rely on heavyweight architectures that prioritize accuracy alone. We show this trade-off is unnecessary: building on YOLOv10, an NMS-free dual-head detector, we achieve state-of-the-art adaptation accuracy while being faster and more compact. We observe that directly applying vanilla mean-teacher se...

---

### 28. An Agentic AI Framework to Accelerate Scientific Discovery in Plant Phenotyping

**Authors:** Renan Souza, Daniel Rosendo, Kelsey Carter, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31831v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31831v1)

**Summary:** High-throughput plant phenotyping now generates image derived datasets far faster than scientists can analyze them. At Oak Ridge National Laboratory's Advanced Plant Phenotyping Laboratory (APPL), automated stations image hundreds of plants daily across multiple remote sensing modalities; yet, trait extraction and interpretation remain manual, expert-bound, and strictly post-hoc, making analysis, not acquisition, the binding constraint on discovery. We present an end-to-end agentic AI framework ...

---

### 29. Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning

**Authors:** Junha Jung, Minbyul Jeong, Suhyeon Lim, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31825v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31825v1)

**Summary:** Recent multimodal large language models have shown great promise in clinical image reasoning, but existing post-training pipelines remain predominantly outcome-centric, relying on final answer correctness or sequence-level preferences. This suffers from sparse credit assignment, making it difficult to optimize the reasoning process essential for clinical applications. Our analysis reveals that cascading errors from early-stage reasoning failures are a leading cause of incorrect predictions in me...

---

### 30. Adaptive Cluster-First Route-Second Decomposition for Industrial-Scale Vehicle Routing

**Authors:** Oguzhan Karaahmetoglu, Hyong Kim

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31820v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31820v1)

**Summary:** Large-scale capacitated vehicle routing problems (CVRPs) are commonly addressed using cluster-first route-second (CFRS) approaches that split a routing instance into smaller, computationally tractable subproblems. Existing splitting methods typically rely on fixed partitioning rules, predefined optimization objectives, or learned policies, which may perform inconsistently across instances exhibiting different spatial, demand, and operational characteristics. In this work, we propose an adaptive ...

---

### 31. Creating Intelligence: A Computational Foundation for AGI

**Authors:** Peter Overmann

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31819v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31819v1)

**Summary:** This work introduces a new computational theory of mind grounded in set theory and hyperdimensional computing. Whereas traditional neural networks rely on continuous weights and matrix multiplication, this framework works with sparse binary data. It represents information as discrete sets, directly modeling biological neural population codes. I demonstrate that associative memory emerges naturally from network topologies featuring a combinatorially expanded hidden layer. Learning is driven by to...

---

### 32. Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR

**Authors:** Ruijia Zhang, Jiacheng Zhu, Hanqing Zhu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31813v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31813v1)

**Summary:** Low-rank adaptation (LoRA) and its variants enable parameter-efficient fine-tuning of large language models under the supervised fine-tuning (SFT) paradigm. However, their efficacy and behavior under Reinforcement learning with verifiable rewards (RLVR) are less well understood. In particular, two structurally initialized LoRA variants, PiSSA and MiLoRA, which outperform standard LoRA under SFT, can underperform standard LoRA under RLVR and may even exhibit training instability. These observatio...

---

### 33. Large Databases Need Small, Open-Weight Language Models

**Authors:** Parker Glenn, Alfy Samuel

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31808v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31808v1)

**Summary:** Language model systems built around proprietary APIs often operate on a token-based cost model. This becomes prohibitively expensive in the context of large databases, where LM-enhanced relational operators can incur costs exceeding $10,000 for a single set of experiments, hindering thorough research and practical deployment. In this paper, we demonstrate that quantized, open-weight models running locally on just 16GB of VRAM can match or exceed the accuracy of closed-source counterparts at lowe...

---

### 34. RAISE: LLM-based Automated Heuristic Design with Robust Adversary Instance Search

**Authors:** Fei Liu, Alessio Figalli, Patrick Owen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31801v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31801v1)

**Summary:** Automated Heuristic Design (AHD) with Large Language Models (LLMs) has shown remarkable progress in discovering high-quality heuristics. However, existing LLM-based AHD methods optimize heuristics for a fixed training instance set and may fail catastrophically when deployed under real-world distributional shifts. We propose Robust Adversary Instance Search (RAISE), a framework that integrates constrained worst-case instance search within a principled neighborhood of the training distribution int...

---

### 35. Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision

**Authors:** Xianda Zheng, Huan Gao, Meng-Fen Chiang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31800v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31800v1)

**Summary:** Despite recent progress, the reasoning capabilities of large multimodal language models (MLLMs) remain fundamentally constrained by static supervision, where fixed prompts, rules, or reward models provide non-adaptive guidance throughout training. Such static signals are often sufficient to enforce output formats, but fail to shape the underlying reasoning process, leading to brittle generalization and performance saturation in complex decision-making tasks. We propose Evo-PI, a principle-centri...

---

### 36. CHERRY: Compressed Hierarchical Experts with Recurrent Representational Yield

**Authors:** Dohyeon Kwon, Youngjin Park

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31796v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31796v1)

**Summary:** We study three complementary techniques for training compute-efficient language models.   (1) Selective supervision and per-token efficiency. Selective Ground Truth Token Training (SGT) concentrates supervision on the ~15% of output tokens that carry semantic payload. Through positive gradient coupling in position-shared transformer weights -- a token-level instance of auxiliary-task transfer -- the remaining 85% of unsupervised tokens still improve substantially, giving a 4.5x per-supervised-to...

---

### 37. A Self-Evolving Agentic System for Automated Generation and Execution of Biological Protocols

**Authors:** Yankai Jiang, Weiting Tang, Haoran Sun, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31763v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31763v1)

**Summary:** Autonomous wet-lab experimentation requires more than plausible protocol text: biological intent, quantitative procedures, device constraints and experimental feedback must remain aligned from protocol and SOP design to code and physical execution. We developed ProtoPilot, a self-evolving multi-agent system, together with an expert-grounded benchmark and evaluation framework for testing this conversion as an experimental automation problem. The framework spans 294 synthetic-biology and molecular...

---

### 38. A Technical Typology of AI Systems in Public Administration

**Authors:** Jonathan Rystrøm, Chris Schmitz, Nathan Davies, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31755v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31755v1)

**Summary:** Research on artificial intelligence (AI) in the public sector often treats "AI" as a single category, neglecting technical distinctions between different AI systems. But these distinctions affect how different systems impact core public values like accountability, procedural justice, and non-discrimination. This paper argues that public administration research would benefit from more technical precision on "AI" and makes three contributions to this end. First, we introduce a typology of five cat...

---

### 39. JL1-CC&QA: Extending the JL1-CD Benchmark with Change Captioning and Question Answering

**Authors:** Ziyuan Liu, Ruifei Zhu, Ouqiao Ma, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31745v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31745v1)

**Summary:** Remote sensing change detection (CD) traditionally focuses on pixel-level binary segmentation, which identifies where changes occur but neither what nor why. To bridge this semantic gap, we introduce JL1-CC&QA, a multi-task benchmark that extends the JL1-CD dataset with two complementary annotation layers: change captioning (CC) and change question answering (QA). Built upon 5,000 bi-temporal image pairs acquired by the Jilin-1 satellite at 0.5-0.75m ground sample distance, the benchmark compris...

---

### 40. FedXDS: Leveraging Model Attribution Methods to counteract Data Heterogeneity in Federated Learning

**Authors:** Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31742v1)

**Summary:** Explainable AI (XAI) methods have demonstrated significant success in recent years at identifying relevant features in input data that drive deep learning model decisions, enhancing interpretability for users. However, the potential of XAI beyond providing model transparency has remained largely unexplored in adjacent machine learning domains. In this paper, we show for the first time how XAI can be utilized in the context of federated learning. Specifically, while federated learning enables col...

---

### 41. STEB: Style Text Embedding Benchmark

**Authors:** Rafael Rivera Soto, Anna Wegmann, Cristina Aggazzotti

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31741v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31741v1)

**Summary:** While semantic embeddings are rigorously evaluated on the Massive Text Embedding Benchmark, the evaluation of style embeddings remains fragmented, with each work relying on their own set of tasks and datasets. To bridge this gap, we introduce the Style Text Embedding Benchmark, a comprehensive open-source benchmark intended to standardize the evaluation of style embeddings. STEB encompasses 96 datasets across 7 languages, spanning applications such as authorship verification, authorship retrieva...

---

### 42. Seeing Is Not Sharing: Some Vision-Language Models Overestimate Common Ground in Asymmetric Dialogue

**Authors:** Nan Li, Albert Gatt, Massimo Poesio

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31719v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31719v1)

**Summary:** In collaborative dialogue, shared perception does not guarantee shared interpretation. Mutual understanding must be established through interaction. We investigate whether vision-language models (VLMs) can distinguish what could be shared from what has been shared between dialogue participants through grounding. We formulate this as an interpretation-matching task on 13,077 annotated reference expressions from HCRC MapTask dialogues, and evaluate VLMs under systematically controlled manipulation...

---

### 43. Cross-lingual Relation Extraction with Large Language Models: Zero-Shot, Few-Shot, and Fine-Tuned Evaluation on Romanian

**Authors:** Dragos-Mitrut Vasile, Elena-Simona Apostol, Stefan-Adrian Toma, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31718v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31718v1)

**Summary:** Relation extraction (RE) for low-resource languages is typically constrained by the lack of annotated corpora. We investigate the feasibility of cross-lingual RE for Romanian by combining automatic dataset translation with large language model (LLM) inference. We translate the SemEval-2010 Task 8 benchmark from English to Romanian using an LLM-based translation pipeline and evaluate Gemma 4 31B under zero-shot, few-shot, and QLoRA fine-tuned configurations, against four encoder baselines spannin...

---

### 44. Arena-T2I Hard: Benchmarking and Improving Faithfulness with Dependency-Aware Checklist

**Authors:** Yuanhao Ban, Tong Xie, Sohyun An, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31711v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31711v1)

**Summary:** Faithfulness -- how precisely a generated image aligns with its prompt -- is increasingly central to the real-world utility of text-to-image (T2I) models. Existing faithfulness benchmarks, however, rely on simple atomic instructions, on which top-tier systems already achieve near-perfect scores. As T2I models enter creative workflows, users issue multi-faceted requests combining intricate spatial relationships, stylistic constraints, and complex text rendering. In this setting, a single binary V...

---

### 45. Look But Don't Touch with Sparse Autoencoders for Unlearning in Diffusion Models

**Authors:** Enrico Cassano, Riccardo Renzulli, Rayyan Ahmed, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31699v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31699v1)

**Summary:** Sparse autoencoders (SAEs) have recently been proposed as interpretable tools for concept-level manipulation, under the assumption that isolated features can serve as controllable intervention points. In this work, we systematically evaluate this assumption in the context of object erasure and steering in diffusion models. We show that while SAEs reliably detect and localize semantic concepts within diffusion model activations, direct intervention in their latent space frequently induces out-of-...

---

### 46. RCT: A Robot-Collected Touch-Vision-Language Dataset for Tactile Generalization

**Authors:** Jingbo He, Michael Färber, Roberto Calandra

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31694v1)

**Summary:** For robots manipulating open-world objects, tactile representations must generalize to unseen materials. We introduce RCT (Robotic Contact Tactile), a robot-collected touch-vision-language dataset with 29,279 tactile frames from full robot presses on 122 industrial reference materials in 7 categories, recorded with three DIGIT sensors at multiple contact positions. RCT preserves each press as a contact sequence, enabling held-out evaluation across materials, categories, sensors, contact position...

---

### 47. ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping

**Authors:** Jiacheng Chen, Tao Zhang, Manxi Lin, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31693v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31693v1)

**Summary:** The wave of AI-native applications is moving shopping beyond page- and feed-based browsing toward intent-driven experiences orchestrated by LLM agents. A common design wraps an LLM around existing search and recommendation pipelines, forcing complex intents through low-bandwidth retrieval or ranking interfaces and leaving a gap between language understanding and item-space fulfillment. Generative recommendation gives LLMs a direct item-space interface through semantic IDs (SIDs), but existing mo...

---

### 48. When to Truncate a Feature Ranking: A Residual-Overlap Stopping Rule for Subset Selection

**Authors:** Jesus S. Aguilar-Ruiz

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31686v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31686v1)

**Summary:** Feature rankings are widely used in supervised feature selection because they are simple, scalable and easy to interpret. Variables are first ranked by a relevance score, and a subset is then obtained by retaining the top-ranked variables. Although the first stage has been extensively studied, the second is often governed by an arbitrary cardinality, an empirical threshold or cross-validation, without a direct interpretation. This raises a basic question: given a feature ranking, when is there e...

---

### 49. Histogram-constrained Image Generation

**Authors:** Haoming Liu, Yuanhe Guo, Yijia Cao, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31683v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31683v1)

**Summary:** Diffusion models have emerged as a dominant paradigm in generative modeling, enabling high-fidelity sampling from complex data distributions. Despite impressive capabilities, controlling diffusion models to produce outputs aligned with user intent remains an open challenge, especially when balancing global coherence with local precision. Existing control mechanisms vary in the granularity of their conditioning signals. For example, textual prompts guide generation globally through high-level sem...

---

### 50. WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models

**Authors:** Ting-Bing Xu, Jiacheng Sui, Zhe Gao, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31672v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31672v1)

**Summary:** Despite rapid progress in interactive world models (IWMs), existing benchmarks evaluate action following only at trajectory level and ignore memory and interaction physics. We introduce WorldRoamBench, an open-world benchmark for long-horizon stability across four dimensions, each with tailored innovations: (i) Action: per-frame action metric bypassing cross-model semantic scale disparity and exposing failures hidden by trajectory; (ii) Vision: segment-based drift metric capturing non-monotonic ...

---

## cs.CL

**50 papers**

### 1. Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision

**Authors:** Zifan Carl Guo, Laura Ruis, Jacob Andreas, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32038v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32038v1)

**Summary:** When does training language models (LMs) to generate explanations of their predictions yield faithful introspection, rather than superficial imitation? We study LMs trained to explain which features of their inputs influenced their behavior, using models' counterfactual behavior on modified inputs as supervision. Surprisingly, we find that LMs trained on fixed counterfactual explanations derived from earlier checkpoints of themselves, or even from behaviorally similar models in different familie...

---

### 2. QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents

**Authors:** Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32034v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32034v1)

**Summary:** LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream perfo...

---

### 3. Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs

**Authors:** Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32032v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32032v1)

**Summary:** Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal uncertainty--undermining trustworthiness and reliability. Since monitoring task performance and adapting behavior accordingly are central to metacognition, we posit that models capab...

---

### 4. When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors

**Authors:** Yuqing Yang, Qi Zhu, Zhen Han, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32029v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32029v1)

**Summary:** While large language models (LLMs) perform well on table tasks, they still make data referencing errors (DREs), i.e., incorrectly citing or omitting table values, despite understanding the table structure. Beyond final-answer accuracy, DREs directly compromise the correctness and reliability of intermediate reasoning steps. Yet prior studies have only offered limited, small-scale analyses. In this work, we present the first systematic evaluation of tabular data referencing errors across differen...

---

### 5. Generative Skill Composition for LLM Agents

**Authors:** Xinyu Zhao, Zhen Tan, Vaishnav Tadiparthi, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32025v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32025v1)

**Summary:** Recent LLM agents benefit from skills for solving complex tasks. Skills encapsulate modular packages of procedural knowledge and instructions for performing specialized tasks, such as setting up a sandboxed environment, running a test suite, or refactoring a function across multiple files. As skill libraries grow and become reusable across tasks and domains, selecting an appropriate skill composition has emerged as a central bottleneck. Existing approaches fall into two categories. One exposes t...

---

### 6. SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language Models

**Authors:** Jian Gu, Aldeida Aleti, Chunyang Chen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32022v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32022v1)

**Summary:** Residual-stream analysis asks how language-model computation evolves across depth, but intermediate decoding requires comparable readout coordinates across layers. If embedding anchors and unembedding readout disagree on the chosen span, apparent motion may reflect measurement drift rather than computation. We introduce \emph{Semantic Reference Frames} (SemRF), an anchor-based formalism separating semantic measurement from residual dynamics. A SemRF fixes anchors and measures states against them...

---

### 7. Scalable Behaviour Cloning on Browser Using via Skill Distillation

**Authors:** Kaisen Yang, Zheng Jiang, Yuzhao Peng, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32014v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32014v1)

**Summary:** Internet users collectively perform an enormous range of skilled work through web browsers, from software development and document editing to search, forms, and enterprise workflows, making human browsing a highly scalable but under-exploited source of reusable browser skills. We argue that the bottleneck for browser agents is decision-making under incomplete information rather than low-level operation, and that the priors agents lack are already implicit in human interaction traces. We therefor...

---

### 8. DigitalCoach: Communication and Grounding Gaps in Human and Agentic Computer Use Coaching

**Authors:** Meng Chen, Anya Ji, Tsung-Han Wu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31980v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31980v1)

**Summary:** Agents are increasingly capable of automating software tasks, but can they teach humans how to use software themselves? We introduce DigitalCoach, a multimodal dataset of 72 human expert-novice computer use coaching sessions consisting of 22,752 dialogue turns grounded in 28.1 hours of screen and input event recordings across five software applications. We use DigitalCoach to evaluate whether state-of-the-art models can teach humans how to use computers. Automated evaluation shows that models di...

---

### 9. MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments

**Authors:** Qingyun Liu, Jiwen Zhang, Jingyi Hu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31966v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31966v1)

**Summary:** Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration genera...

---

### 10. Signed-Permutation Coordinate Transport for RMSNorm Transformers

**Authors:** John Sweeney

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31963v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31963v1)

**Summary:** Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only...

---

### 11. LuxEmo: Expressive Text-to-Speech Corpus for Luxembourgish

**Authors:** Nina Hosseini-Kivanani, Sandipana Dowerah

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31947v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31947v1)

**Summary:** State-of-the-art speech datasets predominantly focus on widely spoken languages, often overlooking low-resource languages such as Luxembourgish, which remain underrepresented in speech technology research. In this work, we introduce LuxEmo, a 21-hour conversational expressive speech corpus for Luxembourgish with 4 emotion categories. LuxEmo is derived from Radio Télévision Luxembourg (RTL) youth broadcasts, using automated detection followed by human validation. We propose a semi-automatic curat...

---

### 12. Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity of LLMs to Induce Belief States via Planning and Action

**Authors:** Ben Slater, Matteo G. Mecattaf, Lucy G. Cheke, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31916v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31916v1)

**Summary:** Theory of Mind (ToM) benchmarks for Large Language Models (LLMs) typically rely on passive question-answering formats, but the deployment of LLMs in increasingly agentic and autonomous forms demands new evaluations. In this paper we evaluate an agent's ability to induce specific belief states in other agents by taking actions rather than using conversational persuasion, a capability we call Non-Conversational Planning ToM (NCP-ToM). NCP-ToM is likely to be essential for many agent use-cases, inc...

---

### 13. Review Residuals: Update-Conditioned Residual Gating for Transformers

**Authors:** Kyle Kramer

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31859v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31859v1)

**Summary:** Residual connections add every sublayer's proposed update with a fixed coefficient of one; the network never evaluates whether an update is reliable before committing it. Drawing on the human-factors principle of independent verification, we introduce Review Residuals, which scale each update by a learned, input-dependent gate conditioned on both the current state and the proposed update: h_l = h_{l-1} + r_l * u_l with r_l = sigmoid(W[RMSNorm(h_{l-1}), RMSNorm(u_l)]). Conditioning the gate on th...

---

### 14. Explicit Fuzzy Logic in the Feed-Forward Layer: Self-Forgetting Quantifiers Discover Legible Grammatical-Licensing Detectors

**Authors:** Mark Oskin

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31845v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31845v1)

**Summary:** A transformer's feed-forward (FFN) sublayer materializes the distinctions attention gathers, yet gives no account of what it computes. In a parameter-neutral replacement, each hidden unit is an explicit fuzzy set operation on sigmoid-bounded [0,1] memberships: intersection A*B and set-difference A*(1-B), the latter a bounded positive negation ("A but not B") that gated/bilinear units lack -- a negation-capable FFN (NC-FFN). On N-bit parity they are the most parameter-efficient reasoning basis at...

---

### 15. CHERRY: Compressed Hierarchical Experts with Recurrent Representational Yield

**Authors:** Dohyeon Kwon, Youngjin Park

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31796v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31796v1)

**Summary:** We study three complementary techniques for training compute-efficient language models.   (1) Selective supervision and per-token efficiency. Selective Ground Truth Token Training (SGT) concentrates supervision on the ~15% of output tokens that carry semantic payload. Through positive gradient coupling in position-shared transformer weights -- a token-level instance of auxiliary-task transfer -- the remaining 85% of unsupervised tokens still improve substantially, giving a 4.5x per-supervised-to...

---

### 16. SpikeLogBERT: Energy-Efficient Log Parsing Using Spiking Transformer Networks

**Authors:** Thuan Bui, Duong Do, Tung Vu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31781v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31781v1)

**Summary:** Log parsing is a fundamental step in automated log analysis, transforming raw system logs into structured event templates for downstream tasks such as anomaly detection and system monitoring. Existing log parsing methods range from rule-based and clustering-based approaches to neural models that learn semantic representations from log messages. However, neural approaches typically rely on dense matrix multiplications, which can result in high computational cost and energy consumption. This paper...

---

### 17. Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers

**Authors:** Ying Fan, Anej Svete, Kangwook Lee

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31779v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31779v1)

**Summary:** Language models typically reason via explicit chain-of-thought (CoT), generating intermediate steps token-by-token. Latent CoT offers an alternative: it performs multi-step reasoning in the model's hidden states, replacing decoded tokens with continuous representations for greater efficiency. However, existing latent CoT methods underperform explicit CoT beyond 1B parameters, and the gap widens with scale. Looped, or recurrent-depth, Transformers, which reuse their weights to increase computatio...

---

### 18. STEB: Style Text Embedding Benchmark

**Authors:** Rafael Rivera Soto, Anna Wegmann, Cristina Aggazzotti

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31741v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31741v1)

**Summary:** While semantic embeddings are rigorously evaluated on the Massive Text Embedding Benchmark, the evaluation of style embeddings remains fragmented, with each work relying on their own set of tasks and datasets. To bridge this gap, we introduce the Style Text Embedding Benchmark, a comprehensive open-source benchmark intended to standardize the evaluation of style embeddings. STEB encompasses 96 datasets across 7 languages, spanning applications such as authorship verification, authorship retrieva...

---

### 19. Adapting Foundation ASR Models to Dysarthric Speech: A Case Study

**Authors:** Christian Huber, Laura Kernahan, Alexander Waibel

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31722v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31722v1)

**Summary:** Automatic speech recognition (ASR) systems often perform poorly in dysarthric speech, limiting their usefulness to affected speakers in everyday communication. This paper presents a personalized ASR system for a dysarthric speaker, built by adapting a foundation ASR model to speaker-specific data. Using the TEQST tool, we collected 92 hours of read speech and later added 8.8 hours of user corrections gathered through a deployed mobile application. Starting from Whisper, fine-tuning reduced word ...

---

### 20. Seeing Is Not Sharing: Some Vision-Language Models Overestimate Common Ground in Asymmetric Dialogue

**Authors:** Nan Li, Albert Gatt, Massimo Poesio

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31719v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31719v1)

**Summary:** In collaborative dialogue, shared perception does not guarantee shared interpretation. Mutual understanding must be established through interaction. We investigate whether vision-language models (VLMs) can distinguish what could be shared from what has been shared between dialogue participants through grounding. We formulate this as an interpretation-matching task on 13,077 annotated reference expressions from HCRC MapTask dialogues, and evaluate VLMs under systematically controlled manipulation...

---

### 21. Cross-lingual Relation Extraction with Large Language Models: Zero-Shot, Few-Shot, and Fine-Tuned Evaluation on Romanian

**Authors:** Dragos-Mitrut Vasile, Elena-Simona Apostol, Stefan-Adrian Toma, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31718v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31718v1)

**Summary:** Relation extraction (RE) for low-resource languages is typically constrained by the lack of annotated corpora. We investigate the feasibility of cross-lingual RE for Romanian by combining automatic dataset translation with large language model (LLM) inference. We translate the SemEval-2010 Task 8 benchmark from English to Romanian using an LLM-based translation pipeline and evaluate Gemma 4 31B under zero-shot, few-shot, and QLoRA fine-tuned configurations, against four encoder baselines spannin...

---

### 22. RCT: A Robot-Collected Touch-Vision-Language Dataset for Tactile Generalization

**Authors:** Jingbo He, Michael Färber, Roberto Calandra

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31694v1)

**Summary:** For robots manipulating open-world objects, tactile representations must generalize to unseen materials. We introduce RCT (Robotic Contact Tactile), a robot-collected touch-vision-language dataset with 29,279 tactile frames from full robot presses on 122 industrial reference materials in 7 categories, recorded with three DIGIT sensors at multiple contact positions. RCT preserves each press as a contact sequence, enabling held-out evaluation across materials, categories, sensors, contact position...

---

### 23. ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping

**Authors:** Jiacheng Chen, Tao Zhang, Manxi Lin, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31693v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31693v1)

**Summary:** The wave of AI-native applications is moving shopping beyond page- and feed-based browsing toward intent-driven experiences orchestrated by LLM agents. A common design wraps an LLM around existing search and recommendation pipelines, forcing complex intents through low-bandwidth retrieval or ranking interfaces and leaving a gap between language understanding and item-space fulfillment. Generative recommendation gives LLMs a direct item-space interface through semantic IDs (SIDs), but existing mo...

---

### 24. Overview of the TalentCLEF 2026: Skill and Job Title Intelligence for Human Capital Management

**Authors:** Luis Gasco, Hermenegildo Fabregat, Laura García-Sardiña, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31692v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31692v1)

**Summary:** This paper presents an overview of the second edition of the TalentCLEF challenge, organized as a Lab at the Conference and Labs of the Evaluation Forum (CLEF) 2026. TalentCLEF is an initiative aimed at advancing Natural Language Processing research in Human Capital Management. The second edition of the challenge consisted of two tasks: Task A, contextualized job-person matching, focuses on identifying and ranking the most suitable candidates represented by their resumes for a given job vacancy ...

---

### 25. Moral Safety in LLMs: Exposing Performative Compliance with Puzzled Cues

**Authors:** Mohammadamin Shafiei, Shuyue Stella Li, Yulia Tsvetkov

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31644v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31644v1)

**Summary:** As large language models take on morally consequential roles in healthcare, legal, and hiring contexts, we need to examine whether their ethical behaviors are genuine or superficial. We show that current fairness evaluations substantially overestimate moral safety. Models appear fair when demographic identity is stated as an explicit label, yet become measurably less fair when the same identity must be inferred. We term this failure \emph{performative compliance}, where a model is fair when the ...

---

### 26. Tone-Conditioned Curriculum Learning for Low-Resource Bantu Speech Recognition

**Authors:** Kesego Mokgosi, Vukosi Marivate, Sitwala Mundia, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31642v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31642v1)

**Summary:** Southern Bantu languages are spoken by over 80 million people, yet current foundation ASR models still produce zero-shot WER above 100%, which limits practical use in education and public services. We addressed this gap with a tone conditioned curriculum framework for 6 Southern Bantu languages that combined hybrid difficulty scoring, gated adapters driven by tonal statistics and staged curriculum training. We trained on a community corpus and tested transfer to NCHLT to measure robustness beyon...

---

### 27. CLExEval: A Human-in-the-Loop Framework for Qualitative Evaluation of LLM Clinical Reasoning

**Authors:** Ajmal M., Abin Roy, Afthab Salam Kanniyan, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31608v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31608v1)

**Summary:** Large Language Models (LLMs) achieve strong results on many medical benchmarks, but their clinical reasoning remains difficult to evaluate reliably. A central risk is an evaluation illusion: fluent and well-structured explanations can appear clinically convincing even when the final diagnosis is incorrect. We introduce CLExEval, a human-in-the-loop framework for evaluating LLM clinical reasoning under progressive information masking. CLExEval combines 5,600 expert-physician annotations with 200 ...

---

### 28. Robust Text Watermarking for Large Language Models via Dual Semantic Embeddings

**Authors:** Jonas Schäfer, Cezary Pilaszewicz, Gerhard Wunder

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31602v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31602v1)

**Summary:** This work presents Dual-Embedding Watermarking (DEW), a semantic watermarking scheme for large language models (LLMs) that leverages contextual and token-level embeddings to enhance robustness against paraphrasing and translation. DEW utilizes a signal-processing methodology, applying algebraic vector-space operations to \mbox{token and context embeddings to derive a watermark signal that degrades gracefully under semantic shifts. The method obfuscates the watermark by projecting embedding vecto...

---

### 29. AutoTrainess: Teaching Language Models to Improve Language Models Autonomously

**Authors:** Zhaojian Yu, Penghao Yin, Shuzheng Gao, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31551v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31551v1)

**Summary:** Training language models (LMs) remains a highly human-intensive process, even as frontier language model agents become increasingly capable at software engineering and other long-horizon tasks. A central challenge is that autonomous post-training is not just a coding problem: it requires the agent to repeatedly plan iterations, construct benchmark-aligned data, run stable training jobs, evaluate checkpoints, and preserve experiment state across many hours of interaction. We present AutoTrainess,...

---

### 30. Modality-Driven Search with Holistic Trace Judging for ARC-AGI-2

**Authors:** Johan Land

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31543v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31543v1)

**Summary:** Large language models can produce fluent, internally coherent reasoning traces for abstract reasoning tasks while still being confidently wrong - making selection among candidates, not just generation, the central challenge. I present a solver for ARC-AGI-2, a few-shot visual reasoning benchmark, built around two principles: (i) treating reasoning modalities as search operators, generating diverse candidates independently across text, image, and code channels, and (ii) context-preserving holisti...

---

### 31. FinPersona-Bench: A Benchmark for Longitudinal Psychometric Stability of Autonomous Financial Agents

**Authors:** Muhammad Usman Safder, Ayesha Gull, Rania Elbadry, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31522v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31522v1)

**Summary:** Large Language Models (LLMs) are increasingly deployed as autonomous financial agents initialized with explicit behavioral mandates such as "preserve capital" or "avoid speculative bets" that are meant to govern every decision throughout deployment. In practice, however, as market context accumulates over long horizons, these mandates gradually lose their behavioral influence, a phenomenon we formalize as Mandate Salience Decay (MSD). To measure MSD objectively, we introduce FinPersona-Bench, a ...

---

### 32. RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference

**Authors:** Wenhao Li, Jinhao Dong, Hailin Zhang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31519v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31519v1)

**Summary:** Long-context Large Language Model inference is severely bottlenecked by the massive Key-Value (KV) cache, yet existing sparse attention methods often suffer from static fixed-budget (Top-k) retrieval or rely on proxy scores that are computationally expensive and biased. To address these limitations, we propose RaBitQCache, a novel sparse attention framework that utilizes randomized rotated binary quantization and high-throughput binary-INT4 arithmetic to efficiently estimate attention weights. O...

---

### 33. Falsification, Not Exposure: An Internally Preregistered Placebo-Controlled Decomposition of Self-Repair Feedback in Frozen Small Code Models

**Authors:** Mehmet Iscan

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31511v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31511v1)

**Summary:** In deployment settings where retraining is infeasible, small frozen code models are routinely asked to repair a failed program after seeing their own failing output, usually treated as a retry mechanism. From a Popperian view, a generated program is a conjecture and a test-execution violation is an oracle-relative, executable counterexample, so feedback's value should be attributed not to re-exposure to failing code but to whether the conjecture is opened to external, executable criticism. As th...

---

### 34. Building an ASR Solution for Training and Assessing Children's Reading

**Authors:** Yacouba Diarra, Nouhoum Souleymane Coulibaly, Mamadou Dembele, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31508v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31508v1)

**Summary:** Automatic speech recognition for children's reading remains underdeveloped for most African languages, including Bambara, despite its potential value for reproducible literacy assessment. We present an open-source system for assessing children's reading in Bambara, developed through an end-to-end process linking field data collection, benchmark construction, model adaptation, a reading application, and classroom validation. A mobile collection and assessment app was used to collect 55 hours of r...

---

### 35. Fork-Think with Confidence

**Authors:** Zena Al-Khalili, Rafi Hakim, Dietrich Klakow, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31484v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31484v1)

**Summary:** Parallel thinking has enjoyed great success for boosting LLM performance on reasoning tasks without the need for any re-training. However, existing methods follow a think-first-then-decide paradigm, i.e., they first sample multiple reasoning paths, which inevitably leads to overgeneration, then prune or stop unnecessary paths to compensate. In contrast, decide-first-then-think, i.e., first identifying points that are likely to lead to desirable generations, has been underexplored so far. Followi...

---

### 36. Team MKC at CLPsych 2026: Capturing and Characterizing Mental Health Changes through Social Media Timeline Dynamics

**Authors:** Kyomin Hwang, Hyeonjin Kim, Hyunho Lee, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31464v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31464v1)

**Summary:** Recent advances in Large Language Models (LLMs) have motivated their adoption across a wide range of domains, including Artificial Intelligence (AI) for mental health. Given the growing prevalence of mental health disorders worldwide and the limited accessibility of professional care, there is an increasing demand for scalable computational approaches that can assist in early detection and continuous monitoring of psychological well-being. In this area, ongoing efforts have focused on curating d...

---

### 37. Revising RVL-CDIP: Quantifying Errors and Test-Train Overlap

**Authors:** Stefan Larson, Attila Nagy, Sam Desai, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31446v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31446v1)

**Summary:** RVL-CDIP is a popular dataset for benchmarking document classifiers. However, the dataset contains ample amounts of label errors as well as non-trivial amounts of test-train overlap, both of which may impact model performance metrics. In this paper, we address these two problems by (1) finding and fixing label errors, and (2) detecting and addressing test-train overlap. We produce several variations of RVL-CDIP with label error and test-train overlap fixes, and benchmark document classification ...

---

### 38. CDR-Bench: Evaluating Faithful Execution of Compositional, Order-Sensitive Data Refinement Recipes

**Authors:** Yuchen Huang, Xiang Li, Zhenqing Ling, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31435v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31435v1)

**Summary:** Data refinement involves executing multi-step recipes over evolving text states, where both composition and execution order of processing operators determine the outcome. While existing benchmarks either isolate text editing or entangle it with code and tool execution, it remains unclear whether LLMs can directly and faithfully execute these compositional, order-sensitive data refinement recipes. To fill this gap, we introduce CDR-Bench, a comprehensive benchmark featuring 3,462 high-quality tas...

---

### 39. Clinically Structured Rank-Gated LoRA for Cross-Benchmark Medical Question Answering

**Authors:** Yining Huang

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31432v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31432v1)

**Summary:** Medical multiple-choice question answering requires parameter-efficient adaptation across heterogeneous knowledge domains and reasoning operations. A medication question, a diagnostic decision, a public-health item, and a nursing-action item may require different low-rank updates, while some recall items should preserve the base model's representation with only mild adapter intervention. We propose BiRG-LoRA, a single-adapter rank-gated LoRA method for medical question answering. BiRG-LoRA keeps...

---

### 40. Linguistic Bias Mitigation for Spoofing Detection via Gradient Reversal and A Variational Information Bottleneck

**Authors:** Anh-Tuan Dao, Driss Matrouf, Mickael Rouvier, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31411v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31411v1)

**Summary:** Rapid advancements in generative speech technology have compromised the reliability of voice biometrics. While current spoofing detectors excel when assessed under in-domain conditions, generalisation to out-of-domain settings is often poor. We show that this can be due to linguistic bias. A reliance on linguistic cues observed in training data can then compromise robustness to cross-data. We propose a linguistic-invariant spoofing detection framework utilizing teacher-student adversarial learni...

---

### 41. Visual Semantic Entropy: Do Vision Language Models Recognize Visual Ambiguity?

**Authors:** Ta Duc Huy, Trang Nguyen, Townim Chowdhury, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31407v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31407v1)

**Summary:** Vision-language models can produce confident answers on visually ambiguous inputs, resulting in biased predictions. Common entropy-based methods, such as Semantic Entropy (SE), rely on output diversity. Yet our analysis shows that overconfident visual embeddings suppress output diversity under stochastic decoding, causing SE to underestimate uncertainty in such cases. Recent methods instead probe output diversity through input perturbations, including textual paraphrasing or joint text-image per...

---

### 42. Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?

**Authors:** Zewen Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31371v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31371v1)

**Summary:** When large language model (LLM) agents adapt their behavior through evaluator feedback, systematic evaluator biases propagate into the agent's learned strategy distribution - a phenomenon termed evaluator preference coupling. Prior work has documented this coupling and established a diagnostic framework (EPC) to measure it, but has not investigated whether calibration techniques can mitigate the effect. We present the first study of evaluator calibration as mitigation: applying probability calib...

---

### 43. BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding

**Authors:** Hao Zhang, Yiming Hu, Yong Wang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31315v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31315v1)

**Summary:** Speculative decoding accelerates inference by using a lightweight draft model to generate candidate tokens in parallel, and are then verified by the target model, enabling lossless acceleration. Recently, diffusion-based speculative decoding further improves parallelism by generating multiple tokens per forward pass via block-level diffusion, achieving state-of-the-art (SOTA) performance. However, existing methods adopt a fixed inference block size and assume a uniform optimal decoding strategy ...

---

### 44. LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment

**Authors:** Hong-Yun Lin, Fu-An Chao, Bi-Cheng Yan, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31310v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31310v1)

**Summary:** Fueled by increasing model scale and multimodal inputs, Multimodal Large Language Models (MLLMs) have emerged as a promising paradigm for Spoken Language Assessment (SLA). While effective, this paradigm often overlooks the intrinsic ordinal structure of language acquisition. This paper works around the necessity of large-scale MLLMs by introducing Latent Ordinal Prototype Alignment (LOPA) for SLA, a prototype-based regularizer that enforces an ordinal geometric prior directly on the latent space...

---

### 45. When the Database Fails: Prompting LLM Dialogue Agents for Safe Recovery in Task-Oriented Dialogue

**Authors:** Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Jiann Shiun Yuan

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31307v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31307v1)

**Summary:** Large language models used in task-oriented dialogue often produce fluent but unsafe responses when backend database calls fail, return empty results, or surface mismatched information, inventing venues, confirmations, or booking details not grounded in the database. We study a lightweight prompting-based recovery approach that improves robustness without retraining or additional model calls. We compare three response strategies, including a guided recovery prompt conditioned on structured datab...

---

### 46. The Decomposition Is the Fingerprint: Per-Component Identity for Agent Skills

**Authors:** Hongliang Liu, Yuhao Wu, Tung-Ling Li

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31272v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31272v1)

**Summary:** AI agents increasingly acquire and execute skills at runtime: bundles of prompt instructions, executable code, and tool declarations fetched from marketplaces and other agents. Governing them needs a stable notion of skill identity, yet cryptographic hashing is engineered to destroy the very similarity we need, as a one-character edit scrambles the digest. We present a compact, locality-sensitive fingerprint that embeds each component of a skill and projects it to bits with a multi-bank SimHash,...

---

### 47. Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents

**Authors:** Xueqiao Sun, Xiaohan Wang, Ludwig Schmidt, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31270v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31270v1)

**Summary:** Computer-use agents, which leverage multimodal large language models (MLLMs) to operate computers and complete tasks, have attracted significant attention for their utility and versatility. A major challenge in developing these agents is collecting large-scale, high-quality trajectories. The standard approach generates synthetic data through a self-improving loop: an agent is placed in a verifiable environment and iteratively fine-tuned on its successful trajectories. Despite its effectiveness, ...

---

### 48. Probing Stylistic Appropriation using Large Language Models: An Evaluation Framework for Copyright Infringement under EU Law

**Authors:** Noah Scharrenberg, Chang Sun

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31250v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31250v1)

**Summary:** Large language models (LLM) trained on web-scale corpora generate output that may infringe copyright, yet existing technical safeguards focus narrowly on verbatim memorisation. EU copyright doctrine applies a broader standards: substantial similarity, which extends to stylistic choices, narrative structure, and creative elaboration. This mismatch between what current methods detect and what the law protects leaves a significant compliance gap. We introduce PSALM, an LLM-as-a-judge framework that...

---

### 49. Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?

**Authors:** Jongchan Choi, Nari Yang, Sung Soo Park, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31213v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31213v1)

**Summary:** As large language models (LLMs) are increasingly deployed as moral advisors and agents, they need to address dilemmas between two competing values. However, existing research on LLMs with moral dilemmas overlooks a central aspect of human moral cognition: the ability to imagine alternatives that move beyond the given options. We introduce MoralAltDataset, a dataset of 307 moral dilemmas spanning narrative Advisor dilemmas and AI-facing Agent dilemmas, each augmented with compromise and reframed ...

---

### 50. Gated Multi-Graph Fusion via Graph Attention Networks for Alzheimer's Disease Detection

**Authors:** Jinyu Li, Xiao Wei, Bin Wen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31186v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31186v1)

**Summary:** Spontaneous speech is a vital non-invasive biomarker for Alzheimer's Disease (AD), yet many systems overlook non-linear structural disruptions and clinical heterogeneity in pathological language. We propose a Multi-View Gated Graph Attention Network that transcribes audio via Automatic Speech Recognition (ASR) to construct semantic, dependency, and co-occurrence graphs, characterizing speech through a "content-structure-flow" framework. Notably, the co-occurrence graph leverages Pointwise Mutual...

---

## cs.CV

**50 papers**

### 1. FaceMoE: Mixture of Experts for Low-Resolution Face Recognition

**Authors:** Kartik Narayan, Vishal M. Patel

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32040v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32040v1)

**Summary:** Low-resolution face recognition (LR-FR) remains a challenging task due to poor feature extraction and aggregation, as probe images often contain limited identity information resulting from extreme degradations such as blur, occlusion, and low contrast. Additionally, the domain gap between high-resolution (HR) gallery images and low-resolution (LR) probe images poses a significant challenge. A single feature encoder struggles to generalize effectively across both domains when fine-tuned on an LR ...

---

### 2. GEAR: Guided End-to-End AutoRegression for Image Synthesis

**Authors:** Bin Lin, Zheyuan Liu, Chenguo Lin, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32039v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32039v1)

**Summary:** Visual generative models are typically trained in two stages. A tokenizer is first trained for reconstruction and then frozen, after which a generator is trained on its discrete indices or continuous latents. This decoupling leaves the tokenizer unaware of what the generator finds easy to model. We present GEAR (Guided End-to-end AutoRegression), which trains a vector-quantized (VQ) tokenizer and an autoregressive (AR) generator jointly and end-to-end, guided by representation alignment. The key...

---

### 3. PointSplat: Compact Gaussian Splatting via Human-Centric Prediction

**Authors:** Yujie Guo, Yudong Jin, Lingteng Qiu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32036v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32036v1)

**Summary:** Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our ...

---

### 4. SpheRoPE: Zero-Shot Optimization-Free 360 Panorama Generation with Spherical RoPE

**Authors:** Or Hirschorn, Aaron Olender, Eli Alshan, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32033v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32033v1)

**Summary:** We present a zero-shot, training-free and optimization-free framework for generating 360 panoramic images and videos by directly injecting spherical priors into pre-trained diffusion transformers. Existing methods either rely on costly fine-tuning on scarce panoramic data that limits generalization, or leverage multi-step optimization that incurs prohibitive inference latency. We observe that contemporary generative models natively exhibit some panoramic priors from large-scale training. However...

---

### 5. FLORA: A deep learning approach to predict forest attributes from heterogeneous LiDAR data

**Authors:** Emilie Vautier, Clément Mallet, Cédric Vega

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32023v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32023v1)

**Summary:** Forest attributes are essential for national-scale resource monitoring. Airborne LiDAR metrics are among the auxiliary variables most strongly correlated with forest attributes used in National Forest Inventory (NFI) estimates. However, producing wall-to-wall predictions remains challenging when LiDAR data are acquired under heterogeneous conditions. As national LiDAR programs expand across Europe, variability in sensors, flight parameters, seasons, and scan angles limits the robustness of exist...

---

### 6. Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion Teachers

**Authors:** Anh Nguyen, Ngan Nguyen, Duc Vu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32020v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32020v1)

**Summary:** Modern one-step diffusion models achieve impressive quality through distribution-based timestep distillation. Yet, they rely on a critical assumption: Teacher and Student must inhabit the same latent space. This Shared-Space constraint prevents knowledge transfer from modern high-capacity Teachers (e.g., SD 3.5 and Flux) into compact, deployment-friendly Students such as SD 1.5, whose latent resolution and VAE parameterization differ from the Teacher. We formalize this overlooked regime as Cross...

---

### 7. Automated Background Swapping for Robustness against Spurious Backgrounds

**Authors:** Cesar Roder, Kajetan Schweighofer

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32018v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32018v1)

**Summary:** Classifiers based on Deep Neural Networks exhibit strong performance across domains, yet can fail catastrophically if they rely on spurious correlations, i.e., features that are predictive of the target label in the training data but are not causally linked and thus fail to generalize. For the vision domain, many such spurious correlations manifest themselves within the background of the image, where only the foreground is predictive of the class label. In this paper, we introduce Automated Back...

---

### 8. CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation

**Authors:** Sanghyuk Chun, William Yang, Amaya Dharmasiri, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32012v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32012v1)

**Summary:** Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is notoriously difficult even for humans (cf. the Dunning-Kruger effect). Although it is still far from solved even in simpler classification systems, tackling it in multimodal large language models (MLLMs) is becoming increasingly important. Within MLLMs, uncertainty can stem from any of the diverse sources as well as from their relationships, and further can st...

---

### 9. CoLT: Teaching Multi-Modal Models to Think with Chain of Latent Thoughts

**Authors:** Lianyu Hu, Shengqian Qin, Zeqin Liao, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31986v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31986v1)

**Summary:** Chain-of-thought (CoT) reasoning has enabled multi-modal large language models (MLLMs) to tackle complex visual reasoning tasks by generating explicit intermediate reasoning steps in natural language. However, this text-based reasoning paradigm is inherently slow at inference time with even thousands of tokens and fundamentally constrained by the expressiveness of natural language. In this paper, we propose CoLT, (Chain of Latent Thoughts), a novel framework that teaches multi-modal models to re...

---

### 10. ERA: Entropy-Guided Visual Token Pruning with Rectified Attention for Efficient MLLMs

**Authors:** Yuhao Wang, Mu Qiao, Haiwen Diao, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31982v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31982v1)

**Summary:** Multimodal Large Language Models (MLLMs) incur prohibitive inference costs due to long visual token sequences. Training-free visual token reduction provides an efficient solution. However, existing methods distort attention distributions, giving rise to a phenomenon we term Attention Logit Collapse. To address this issue, we propose ERA, an Entropy-guided visual token pruning framework with Rectified Attention for efficient MLLMs. Specifically, ERA comprises three crucial components: Dual-view E...

---

### 11. LUNA: Learning Universal 3D Human Animation Beyond Skinning

**Authors:** Peng Li, Rawal Khirodkar, Junxuan Li, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31981v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31981v1)

**Summary:** Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often introduce artifacts due to imperfect fitting. We propose LUNA, an LBS-free universal neural animation model that directly maps multiple 2D controls like images, keypoints, sketches, and unseen characters into 3D Gaussian deformations, bypassing explicit body fitting. At its core, a transformer-based moti...

---

### 12. Planar-SfM: Camera Pose Estimation via Homography Graph Embeddings

**Authors:** Gabi Pragier, Matan Karklinsky, David Ungarish, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31979v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31979v1)

**Summary:** Structure from Motion (SfM) systems traditionally struggle with planar scenes, where standard epipolar geometry-based methods become degenerate. Rather than viewing planar surfaces as a limitation, we propose a unified framework that leverages them as a source of geometric constraints. Our key insight is that each planar surface visible across multiple views provides an independent estimate of relative camera poses through homography decomposition. By aggregating estimates from multiple planes o...

---

### 13. MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments

**Authors:** Qingyun Liu, Jiwen Zhang, Jingyi Hu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31966v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31966v1)

**Summary:** Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration genera...

---

### 14. AnyBokeh: Physics-Guided Any-to-Any Bokeh Editing with Optical Fingerprint Transfer

**Authors:** Xinyu Hou, Xiaoming Li, Zongsheng Yue, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31959v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31959v1)

**Summary:** Depth-of-field control is a fundamental tool in photography, yet post-capture bokeh editing from a single image remains challenging. A practical editor should handle images captured under arbitrary focus and aperture settings. Existing methods typically assume an all-in-focus input, or first recover an all-in-focus image before rendering new bokeh. Such pipelines can discard useful blur cues from the source image and propagate reconstruction artifacts into the final edit. We introduce AnyBokeh, ...

---

### 15. DEMUN: Fast and accurate discovery of music notation in very large collections

**Authors:** Vojtěch Dvořák, Filip Bím, Jiří Mayer, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31956v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31956v1)

**Summary:** Much of written musical heritage is preserved and digitised at memory institutions: libraries, museums, and archives. Owing to their collection structures, sheet music tends to be concentrated in large subsets that are defined as collections of music, with corresponding metadata that makes the music findable. However, when studying musical life as opposed to individual works, relevant documents often lie outside of these specialised collections: in textbooks, newspapers, other periodicals, pamph...

---

### 16. World Narrative Model for Highly Controllable Video Generation: A Paradigm Shift from Pixel Sampling to Physical World Orchestration

**Authors:** Ye Chen, Xuanhong Chen, Yupeng Zhu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31946v1)

**Summary:** The fundamental obstacle to industrial grade video generation is the lack of controllability: existing models treat video as a pixel distribution sampling problem, bypassing the explicit, instance level $4D$ $(3D + T)$ physical world. Consequently, content creators cannot specify geometry, motion, camera parameters, or lighting in a deterministic, quantitative way, leading to the infamous ''gacha'' loop that makes professional content creation prohibitively inefficient and expensive. To address ...

---

### 17. FlexViT: A Flexible FPGA-based Accelerator for Edge Vision Transformers

**Authors:** Hubert Dymarkowski, Xingjian Fu, Rappy Saha, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31938v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31938v1)

**Summary:** Deploying Vision Transformer (ViT) models on edge platforms remains challenging due to their high computational demands and the architectural heterogeneity of modern hybrid ViT models, which incorporate both fully connected and convolutional layers. This heterogeneity leads to significant variation in tensor shapes, requiring flexible and efficient FPGA-based acceleration. In this paper, we present FlexViT, a reconfigurable FPGA accelerator for efficient ViT inference on resource-constrained edg...

---

### 18. No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs

**Authors:** Haojian Huang, Harold Haodong Chen, Meng Luo, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31933v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31933v1)

**Summary:** We introduce VidPair-Halluc, a new benchmark for evaluating video hallucination in large video models (LVMs) under rigorous and controlled conditions. Unlike previous benchmarks that primarily rely on text-based perturbations or adversarial questions while neglecting the consistency of visual backgrounds, VidPair-Halluc features video pairs with highly similar backgrounds but distinctly different foreground semantics, enabling precise attribution of model errors to genuine hallucination rather t...

---

### 19. InstanceControl: Controllable Complex Image Generation without Instance Labeling

**Authors:** Xiaoyu Liu, Huan Wang, Fan Li, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31924v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31924v1)

**Summary:** Controllable image generation methods, such as ControlNet, have demonstrated a remarkable capacity to introduce visual conditions(e.g., depth maps) to guide image generation. However, these methods often struggle with complex multi-instance scenes, frequently leading to attribute confusion among instances. While recent approaches attempt to mitigate this via manual instance labeling, such requirements are labor-intensive. In this paper, we propose InstanceControl, a novel multi-instance controll...

---

### 20. MVP-Nav: Multi-layer Value Map Planner Navigator

**Authors:** Wenyuan Xie, Shaokai Wu, Yijin Zhou, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31919v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31919v1)

**Summary:** Zero-shot Object Goal Navigation (ZSON) with RGB-only perception poses a fundamental challenge for embodied agents, as the absence of explicit depth information introduces severe physical uncertainty and semantic-physical misalignment. Existing approaches either rely on high-level semantic reasoning without geometric grounding or learn end-to-end policies that lack explicit physical constraints, often resulting in semantically plausible but physically unsafe behaviors. In this paper, we propose ...

---

### 21. DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation

**Authors:** Junzhe Jiang, Zipei Ma, Zijie Pan, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31918v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31918v1)

**Summary:** A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes. This process enhances scene diversity and facilitates the creation of various corner cases for testing and improving autonomous driving models. However, existing methods often rely on pre-reconstructed 3D assets, which frequently lead to lighting inconsistencies between the inserted foreground and the background. Moreover, the reliance on limited, manually-cu...

---

### 22. Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference

**Authors:** Zhaoyang Luo, Runmin Dong, Miao Yang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31903v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31903v1)

**Summary:** Multimodal large language models (MLLMs) increasingly process long visual-token sequences, increasing the overall inference computation. Existing acceleration methods usually remove visual tokens or skip visual-token updates in entire layers, but these coarse strategies may discard fine-grained evidence or suppress useful operators together with redundant ones. In this paper, we study visual-token computation from an answer-observable perspective and find that late visual-token updates can remai...

---

### 23. RESOLVE: A Multi-Resolution and Multi-Modal Dataset for Roadside Cooperative Perception

**Authors:** Shaozu Ding, Linan Song, Marco De Vincenzi, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31895v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31895v1)

**Summary:** LiDAR has increasingly been integrated into traffic cameras to expand coverage and mitigate occlusion in roadside cooperative perception. However, how unimodal and camera-LiDAR fusion architectures behave under variations in LiDAR point sparsity induced by sensor configurations and scene-dependent sensing conditions remains underexplored. We introduce RESOLVE, a large-scale real-world benchmark dataset featuring multi-resolution roadside LiDAR and synchronized camera-LiDAR sensing for systematic...

---

### 24. Harnessing Textual Refusal Directions for Multimodal Safety

**Authors:** Moreno D'Incà, Massimiliano Mancini, Nicu Sebe

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31876v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31876v1)

**Summary:** To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary f...

---

### 25. SENSE-VAD: Sentient and Semantic Video Anomaly Detection for Autonomous Driving

**Authors:** Nghia T. Nguyen, Lokman Bekit, Yasin Yilmaz

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31875v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31875v1)

**Summary:** Autonomous vehicles (AVs) must navigate not only motion-based hazards but also socially complex situations whose danger is constituted by inter-agent relationships rather than movement statistics alone. A child running away from a guardian, a person being carried by another, or a pursuer chasing a pedestrian across a sidewalk are all anomalous in social context, yet none produces an obvious motion signal that current anomaly detectors are equipped to flag. We introduce SENSE-VAD, the first synth...

---

### 26. Towards Voxel Spacing Consistency for Medical Image Segmentation

**Authors:** Xin You, Runze Yang, Minghui Zhang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31839v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31839v1)

**Summary:** Volumetric medical image segmentation is essential for both preoperative diagnosis and intraoperative guidance. While recent years have witnessed rapid progress in segmentation architectures, comparatively little attention is paid to the physical voxel spacing of anatomical data. Indeed, volumetric image resampling is a ubiquitous preprocessing step before segmentation, yet its interaction with downstream segmentation has not been systematically exploited. In this work, we study the correlation ...

---

### 27. Real-Time Source-Free Object Detection

**Authors:** Sairam VCR, Varun Gopal, Poornima Jain, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31834v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31834v1)

**Summary:** Real-world detectors for autonomous driving, surveillance, and robotics must handle domain-shifts under strict latency and memory constraints, yet existing source-free object detection (SFOD) methods rely on heavyweight architectures that prioritize accuracy alone. We show this trade-off is unnecessary: building on YOLOv10, an NMS-free dual-head detector, we achieve state-of-the-art adaptation accuracy while being faster and more compact. We observe that directly applying vanilla mean-teacher se...

---

### 28. PriorEye: Geospatial Visual Priors for End-to-End Autonomous Driving

**Authors:** Kyuhwan Yeon, Benjamin Ramtoula, Daniele De Martini

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31830v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31830v1)

**Summary:** Most end-to-end autonomous driving methods rely solely on instantaneous sensor observations, limiting them to reactive behavior without the anticipatory foresight human drivers employ through prior experience. We introduce geospatial visual priors, street-level visual context anchored to the intended driving route, providing visual-spatial foresight independent of real-time sensors. We propose a memory augmentation module featuring a dual-memory architecture and an adaptive memory gate, which ca...

---

### 29. Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning

**Authors:** Junha Jung, Minbyul Jeong, Suhyeon Lim, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31825v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31825v1)

**Summary:** Recent multimodal large language models have shown great promise in clinical image reasoning, but existing post-training pipelines remain predominantly outcome-centric, relying on final answer correctness or sequence-level preferences. This suffers from sparse credit assignment, making it difficult to optimize the reasoning process essential for clinical applications. Our analysis reveals that cascading errors from early-stage reasoning failures are a leading cause of incorrect predictions in me...

---

### 30. Absorption-Feature-Guided Distance-Decoupled Estimation and Band Selection for LWIR Hyperspectral Passive Ranging

**Authors:** Shuo Liu, Chen Fan, Zhihe Chen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31824v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31824v1)

**Summary:** Long-wave infrared (LWIR) hyperspectral observations contain distance-dependent atmospheric absorption signatures, providing a physical basis for long-range passive ranging. However, in natural scenes, these signatures are nonlinearly coupled with target temperature, material emissivity, and path radiance, making distance inversion from observed radiance ill posed. Existing methods typically rely on full-band measurements and pixel-wise joint optimization, which is computationally expensive and ...

---

### 31. Generative Lane Topology Reasoning via Autoregressive Model with Geometry Prior

**Authors:** Jiahui Fu, Zehao Huang, Han Li, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31814v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31814v1)

**Summary:** Lane topology reasoning aims to construct a lane graph from onboard sensor observations. Existing methods follow a detection and association paradigm that treats each lane instance independently, leading to geometric inconsistency at connected endpoints and incomplete graphs due to visual occlusions. To address these issues, we propose TopoGPT, a generative framework that learns the geometry prior from typical lane graph structures through autoregressive sequence modeling. Specifically, we const...

---

### 32. MuSViT: A Foundation Vision Model for Sheet Music Representation

**Authors:** Carlos Penarrubia, Antonio Rios-Vila, Eliseo Fuentes-Martinez, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31811v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31811v1)

**Summary:** Foundation models have transformed vision and language processing by providing rich, reusable representations that transfer across diverse tasks. Sheet music, as a visual encoding of musical language, lacks such a strong domain-specific backbone. We introduce MuSViT (Music Score Vision Transformer): the first foundation vision model for sheet music representation -- a ViT encoder pre-trained via Masked Autoencoders on 9.7 million pages from the IMSLP. To handle the complexity of real-world score...

---

### 33. Self-Supervised Temporal Regularization for Landmark-Based Cardiac Segmentation with Automatic AHA Regional Mapping

**Authors:** David Montalvo-García, Nicolás Gaggion, María J. Ledesma-Carbayo, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31785v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31785v1)

**Summary:** Graph-based cardiac segmentation with implicit anatomical correspondences provides topological guarantees and population-level analysis capabilities, but models trained on independent frames of image sequences exhibit temporal discontinuities that affect reliable clinical measurements, particularly in cardiac ultrasound. In this work, we introduce self-supervised temporal regularization as a post-training refinement stage that exploits the temporal coherence in image sequences to enforce consist...

---

### 34. SpikeLogBERT: Energy-Efficient Log Parsing Using Spiking Transformer Networks

**Authors:** Thuan Bui, Duong Do, Tung Vu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31781v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31781v1)

**Summary:** Log parsing is a fundamental step in automated log analysis, transforming raw system logs into structured event templates for downstream tasks such as anomaly detection and system monitoring. Existing log parsing methods range from rule-based and clustering-based approaches to neural models that learn semantic representations from log messages. However, neural approaches typically rely on dense matrix multiplications, which can result in high computational cost and energy consumption. This paper...

---

### 35. Mesh BDF: Barycentric Dominance Field for 3D Native Mesh Generation

**Authors:** Gaochao Song, Haohan Weng, Luo Zhang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31777v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31777v1)

**Summary:** Autoregressive (AR) modeling has recently achieved remarkable progress in native 3D mesh generation, largely due to its natural ability to handle variable-length, discrete data structures. However, the inherent constraints of the AR paradigm severely restrict the generated meshes, leading to limited face counts, bounded vertex resolutions, and difficulties in supporting textures. To overcome these bottlenecks, we propose the Barycentric Dominance Field (BDF), a continuous representation defined ...

---

### 36. NURBS Splatting: A Unified Differentiable Rendering Framework for Vector Graphics

**Authors:** Jingye Qiu, Shizhe Zhou

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31764v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31764v1)

**Summary:** Differentiable rendering of planar rational splines remains largely underexplored, despite their widespread use in vector graphics and design. Existing differentiable vector renderers primarily focus on Bézier curves and rely on analytic rasterization, which can suffer from gradient instability and limited flexibility. We propose NURBS Splatting, a unified framework that represents planar rational curves as continuous Gaussian fields. By sampling Gaussians along the curve parameter domain and in...

---

### 37. Estimating Velocity of Spheres from Rolling-Shutter Image(s)

**Authors:** Wenjie Xue, Jun Yang, Jingmin Wang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31760v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31760v1)

**Summary:** Rolling-shutter cameras introduce characteristic distortions when imaging fast moving objects, and these effects are typically treated as artifacts to be corrected. In this work, we instead leverage rolling-shutter distortions as a valuable source of temporal information to estimate the 3D translational and angular velocities of rapidly moving spherical objects from a single rolling-shutter frame. We design a robust and easily detectable spherical pattern and propose a correspondence-free formul...

---

### 38. JL1-CC&QA: Extending the JL1-CD Benchmark with Change Captioning and Question Answering

**Authors:** Ziyuan Liu, Ruifei Zhu, Ouqiao Ma, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31745v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31745v1)

**Summary:** Remote sensing change detection (CD) traditionally focuses on pixel-level binary segmentation, which identifies where changes occur but neither what nor why. To bridge this semantic gap, we introduce JL1-CC&QA, a multi-task benchmark that extends the JL1-CD dataset with two complementary annotation layers: change captioning (CC) and change question answering (QA). Built upon 5,000 bi-temporal image pairs acquired by the Jilin-1 satellite at 0.5-0.75m ground sample distance, the benchmark compris...

---

### 39. Rhythm-Structured Predictive Learning for Remote Photoplethysmography

**Authors:** Ba-Thinh Nguyen, Huu-Dung Nguyen, Thi-Duyen Ngo, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31736v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31736v1)

**Summary:** Remote photoplethysmography (rPPG) estimates physiological signals from facial videos by analyzing subtle pulse induced skin color variations. Despite recent progress, existing self-supervised rPPG methods mainly reconstruct masked pixels or low-level visual representations, which can bias the model toward facial appearance rather than latent physiological dy namics. Moreover, most recent Mamba-based approaches scan facial video tokens only in chronological order, limiting their ability to explo...

---

### 40. MemLearner: Learning to Query Context memory for Video World Models

**Authors:** Jiwen Yu, Jianxiong Gao, Jianhong Bai, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31734v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31734v1)

**Summary:** Video World Models are interactive video generation models that predict future world states based on user actions and history video frames. A critical challenge in video world models is the lack of memory, causing inconsistent generated scenes over extended durations. Previous methods explored rule-based context frame retrieval as memory, but they fail to generalize in scenarios with scene occlusions and dynamic objects. We propose MemLearner, a learning-based adaptive context query method using...

---

### 41. UniCoder: Unified Visual-to-Code Generation via Symbolic Rewards and Reference-Guided Code Optimization

**Authors:** Yaozhi Zheng, Yilei Jiang, Manyuan Zhang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31732v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31732v1)

**Summary:** Visual-to-Code generation, which transforms scientific plots, vector graphics, and webpages into executable scripts, demands a level of pixel-precise alignment that standard Multimodal Large Language Models (MLLMs) fail to achieve through Supervised Fine-Tuning (SFT) alone. While Reinforcement Learning (RL) offers a theoretical pathway to bridge this gap, its application is hindered by two fundamental obstacles: (1) \textit{Reward Coarseness}, where semantic metrics like CLIP scores fail to pena...

---

### 42. Semantic-Aware Multiple Access via Spatial Redundancy Exploitation for Uplink-Dominant 6G Use Cases

**Authors:** Hamidreza Mazandarani, Masoud Shokrnezhad, Tarik Taleb, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31715v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31715v1)

**Summary:** Emerging uplink-dominant 6G use cases, such as cooperative vehicular streaming, require efficient transmission of high-volume visual data over limited wireless resources. While semantic communications can reduce traffic by prioritizing task-relevant content, most existing approaches treat users independently and therefore overlook spatial redundancy among nearby devices' observations. This paper proposes a semantic-aware multiple access scheme that exploits overlapping fields of view among vehic...

---

### 43. WIDER-FAIR: An Annotated Version of the WIDER-FACE Dataset for Fairness Evaluation

**Authors:** Maxime Moussi, Benoît Ronval, Siegfried Nijssen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31704v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31704v1)

**Summary:** The deployment of face detection models in real-world applications raises important fairness concerns, as these systems may showcase performance disparities across demographic groups. A key obstacle to studying and mitigating such biases is the lack of face detection datasets with sensitive feature annotations. To address this gap, we introduce WIDER-FAIR, a new dataset built on the widely used WIDER-FACE benchmark, manually annotated with the perceived ethnicity and sex of each face. The datase...

---

### 44. Phantom: A Unified Face-Swap Deepfake Protection Framework with Latent and Spatial Constraints

**Authors:** Jungkon Kim, Cheolseung Jung, Jong-Min Choi, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31703v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31703v1)

**Summary:** Face-swapping deepfakes pose an escalating threat to personal privacy by enabling unauthorized identity manipulation. While adversarial approaches have demonstrated success against black-box face recognition (FR) models, their applicability to face-swapping scenarios remains underexplored. In particular, reliance on fixed or random targets yields ambiguous latent guidance, and the lack of explicit spatial constraints causes perturbations to spill into identity-irrelevant regions. These issues ar...

---

### 45. Look But Don't Touch with Sparse Autoencoders for Unlearning in Diffusion Models

**Authors:** Enrico Cassano, Riccardo Renzulli, Rayyan Ahmed, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31699v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31699v1)

**Summary:** Sparse autoencoders (SAEs) have recently been proposed as interpretable tools for concept-level manipulation, under the assumption that isolated features can serve as controllable intervention points. In this work, we systematically evaluate this assumption in the context of object erasure and steering in diffusion models. We show that while SAEs reliably detect and localize semantic concepts within diffusion model activations, direct intervention in their latent space frequently induces out-of-...

---

### 46. Intrinsically Stable Spiking Neural Networks: Overcoming the Performance Barrier in the Absence of Batch Normalization

**Authors:** Ruichen Ma, Xiaoyang Zhang, Jian Bai, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31695v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31695v1)

**Summary:** The performance of deep spiking neural networks (SNNs) often relies on batch normalization (BN). However, the advanced dynamic BN variants used in state-of-the-art models introduce runtime multiplications, which weaken the hardware-efficiency motivation of SNNs. To address this tension, we identify catastrophic firing-rate decay as a primary cause of severe performance degradation in normalization-free SNNs. Guided by this insight, this work proposes the Intrinsically Stable SNN (IS-SNN) archite...

---

### 47. RCT: A Robot-Collected Touch-Vision-Language Dataset for Tactile Generalization

**Authors:** Jingbo He, Michael Färber, Roberto Calandra

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31694v1)

**Summary:** For robots manipulating open-world objects, tactile representations must generalize to unseen materials. We introduce RCT (Robotic Contact Tactile), a robot-collected touch-vision-language dataset with 29,279 tactile frames from full robot presses on 122 industrial reference materials in 7 categories, recorded with three DIGIT sensors at multiple contact positions. RCT preserves each press as a contact sequence, enabling held-out evaluation across materials, categories, sensors, contact position...

---

### 48. Semantic Occupancy Prediction with Dual Range-Voxel Representation

**Authors:** Sitao Chen, Zhuangwei Zhuang, Hui Luo, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31688v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31688v1)

**Summary:** LiDAR-based 3D semantic occupancy prediction, which aims to provide accurate and comprehensive scene representation, is crucial for autonomous driving systems. As point clouds suffer from sparsity and incompleteness, leading to insufficient semantic learning and difficult occupancy perception, existing methods often stack multi-sweep point clouds to obtain dense spatial information. However, such a naive strategy also results in efficiency (e.g., additional computational burden) and robustness (...

---

### 49. Histogram-constrained Image Generation

**Authors:** Haoming Liu, Yuanhe Guo, Yijia Cao, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31683v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31683v1)

**Summary:** Diffusion models have emerged as a dominant paradigm in generative modeling, enabling high-fidelity sampling from complex data distributions. Despite impressive capabilities, controlling diffusion models to produce outputs aligned with user intent remains an open challenge, especially when balancing global coherence with local precision. Existing control mechanisms vary in the granularity of their conditioning signals. For example, textual prompts guide generation globally through high-level sem...

---

### 50. ShellMaker: Language-Guided Exterior Completion under Structural Constraints

**Authors:** Ruiqi Xu, Daniel Aliaga

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31680v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31680v1)

**Summary:** Despite advances in indoor scene generation, synthesizing coherent building exteriors consistent with generated interiors remains largely unexplored. Existing methods can generate floor plans and wall layouts but typically stop at a structural shell, lacking stylistically consistent facades and roofs. Completing these exteriors is challenging because the footprint, wall geometry, and opening semantics must remain fixed-constraints that unconstrained generative models often violate. We introduce ...

---

## cs.LG

**50 papers**

### 1. Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision

**Authors:** Zifan Carl Guo, Laura Ruis, Jacob Andreas, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32038v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32038v1)

**Summary:** When does training language models (LMs) to generate explanations of their predictions yield faithful introspection, rather than superficial imitation? We study LMs trained to explain which features of their inputs influenced their behavior, using models' counterfactual behavior on modified inputs as supervision. Surprisingly, we find that LMs trained on fixed counterfactual explanations derived from earlier checkpoints of themselves, or even from behaviorally similar models in different familie...

---

### 2. QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents

**Authors:** Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32034v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32034v1)

**Summary:** LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream perfo...

---

### 3. Freeform Preference Learning for Robotic Manipulation

**Authors:** Marcel Torne, Anubha Mahajan, Abhijnya Bhat, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32027v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32027v1)

**Summary:** Reward design remains a central bottleneck for autonomous robot policy improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two trajectories is better overall, FPL lets them define natural-...

---

### 4. AdaJEPA: An Adaptive Latent World Model

**Authors:** Ying Wang, Oumayma Bounou, Yann LeCun, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32026v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32026v1)

**Summary:** Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes ...

---

### 5. SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language Models

**Authors:** Jian Gu, Aldeida Aleti, Chunyang Chen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32022v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32022v1)

**Summary:** Residual-stream analysis asks how language-model computation evolves across depth, but intermediate decoding requires comparable readout coordinates across layers. If embedding anchors and unembedding readout disagree on the chosen span, apparent motion may reflect measurement drift rather than computation. We introduce \emph{Semantic Reference Frames} (SemRF), an anchor-based formalism separating semantic measurement from residual dynamics. A SemRF fixes anchors and measures states against them...

---

### 6. Automated Background Swapping for Robustness against Spurious Backgrounds

**Authors:** Cesar Roder, Kajetan Schweighofer

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32018v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32018v1)

**Summary:** Classifiers based on Deep Neural Networks exhibit strong performance across domains, yet can fail catastrophically if they rely on spurious correlations, i.e., features that are predictive of the target label in the training data but are not causally linked and thus fail to generalize. For the vision domain, many such spurious correlations manifest themselves within the background of the image, where only the foreground is predictive of the class label. In this paper, we introduce Automated Back...

---

### 7. TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

**Authors:** Yuanda Xu, Zhengze Zhou, Hejian Sang, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32017v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32017v1)

**Summary:** Agentic reinforcement learning requires assigning credit to environment-facing actions such as searches, clicks, edits, navigation commands, and object interactions. Standard GRPO uses the final verifier outcome as a uniform advantage over all action tokens. This outcome signal is useful but structurally incomplete: it punishes useful exploration in failed rollouts and reinforces redundant or regressive actions in successful rollouts. We propose TRIAGE, a role-typed credit assignment framework t...

---

### 8. FedLAB: Traceable Semantic Codebooks for Federated Multimodal Graph Foundation Learning

**Authors:** Zekai Chen, Kairui Yang, Xuaner Chen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32016v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32016v1)

**Summary:** Multimodal graph foundation models aim to learn reusable knowledge from graphs enriched with text, images, attributes, and relational topology, thereby supporting diverse graph-centric and modality-centric tasks. In practice, however, such multimodal graphs are often distributed across decentralized clients, where raw contents and local structures cannot be centrally shared due to privacy constraints. This motivates federated multimodal graph foundation learning, which requires not only transfer...

---

### 9. CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation

**Authors:** Sanghyuk Chun, William Yang, Amaya Dharmasiri, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32012v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32012v1)

**Summary:** Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is notoriously difficult even for humans (cf. the Dunning-Kruger effect). Although it is still far from solved even in simpler classification systems, tackling it in multimodal large language models (MLLMs) is becoming increasingly important. Within MLLMs, uncertainty can stem from any of the diverse sources as well as from their relationships, and further can st...

---

### 10. Surrogate Fidelity: When Can Open LLMs Explain Closed Ones?

**Authors:** Philippe Chlenski, Zachariah Carmichael, Ayush Warikoo, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32008v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32008v1)

**Summary:** Mechanistic interpretability (MI) requires full access to model internals, yet the APIs for most widely deployed language models at best expose log-probabilities over output tokens. This creates a surrogate problem: when do measurements made on open models allow us to make claims about a closed model? We evaluate surrogate fidelity at the prediction, attribution, and representation levels. For binary classification tasks, log-odds provide an API-compatible scalar readout of the model's represent...

---

### 11. Random Reshuffling Dominates Stochastic Gradient Descent

**Authors:** Zijian Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32005v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32005v1)

**Summary:** Stochastic Gradient Descent ($\textsf{SGD}$) is one of the most classical optimization algorithms with favorable theoretical guarantees, yet the practical implementation of $\textsf{SGD}$ differs subtly from its well-known form and is often referred to as Shuffling Stochastic Gradient Descent ($\textsf{Shuffling SGD}$). A particularly popular strategy in $\textsf{Shuffling SGD}$ is Random Reshuffling ($\textsf{RR}$), which has achieved great empirical success across numerous experiments. Despite...

---

### 12. PolicyGuard: From Organizational Policies to Neuro-SymbolicCompliance Review Engines

**Authors:** Sameer Malik, Ayush Singh, Amar Prakash Azad

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32004v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32004v1)

**Summary:** Policy-grounded document review requires determining whether a target document complies with organization-specific policies, guidelines, or playbooks. While large language models can assist with policy interpretation and document analysis, end-to-end prompting leaves the applied policy logic implicit, making compliance decisions difficult to inspect, update, and test. We present PolicyGuard, a neuro-symbolic framework for policy-grounded document compliance review. PolicyGuard converts organizat...

---

### 13. Self-Study Reconsidered: The Hidden Fragility of Learning from Self-Generated QA

**Authors:** Ekaterina Alimaskina, Denis Shveykin, Gleb Molodtsov, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32002v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32002v1)

**Summary:** Language models are increasingly taught from synthetic question--answer (QA) supervision: a model generates questions about a document, answers them from the same text, and the resulting pairs are used to fine-tune, distill, or compress knowledge into another model. We show that this generation step is not neutral preprocessing. It is an implicit policy that both selects which evidence becomes training signal and decides how that evidence is answered, and it is fragile at both stages. When choos...

---

### 14. Radial Suppression Accelerates Algorithmic Generalization: A Geometric Analysis of Delayed Generalization

**Authors:** Srijan Tiwari, Aditya Chauhan, Manjot Singh

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32000v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32000v1)

**Summary:** Why do neural networks memorize algorithmic training data long before they generalize? We present a geometric case study demonstrating that, on tasks where generalization requires discovering structured low-dimensional circuits, the memorization-generalization delay is driven by radial inflation of hidden representations under cross-entropy optimization. We formalize a radial-angular decomposition of activation-space dynamics and derive three testable propositions: (i) that penalizing radial inf...

---

### 15. Amplifying Membership Signal Through Chained Regeneration

**Authors:** Wojciech Łapacz, Stanisław Pawlak

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31991v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31991v1)

**Summary:** The tendency of large generative models to memorize training data makes sample verification critical for privacy auditing and copyright enforcement. Current membership (MIA) and dataset inference (DI) attacks often rely on one-shot generations, which yield weak signals and limited sensitivity across modalities. Inspired by Model Autophagy Disorder (MAD), we introduce MADreMIA, a model-agnostic framework that enhances white-, gray-, and black-box MIA and DI. Rather than relying on shadow model tr...

---

### 16. Evaluation of Population Initialization Methods for Genetic Programming-based Symbolic Regression

**Authors:** Lukas Kammerer, Gabriel Kronberger, Deaglan J. Bartlett, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31990v1)

**Summary:** We analyze the effect of optimizing the initial population of genetic programming (GP) for symbolic regression (SR) on the accuracy and complexity of solutions. We compare three well-established random initialization methods as well as initialization with small optimized solutions from exhaustive symbolic regression (ESR) using a GP/SR implementation which is based on the multi-objective evolutionary algorithm NSGA-II. We compare the final Pareto fronts found with each initialization method on t...

---

### 17. Semantic Leakage and Privacy Preservation in Relay-Assisted Semantic Communications

**Authors:** Yalin E. Sagduyu, Tugba Erpek, Aylin Yener, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31973v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31973v1)

**Summary:** Semantic communication (SemCom) has emerged as a promising paradigm in which the transmission of task-relevant information is prioritized over raw data, enabling efficient and robust communication under resource and channel constraints. In this paper, the privacy implications of relay-assisted SemCom systems are studied, where the intermediate relay node operates directly on learned latent representations. It is shown that the relay, even without access to source data, can reliably infer semanti...

---

### 18. Signed-Permutation Coordinate Transport for RMSNorm Transformers

**Authors:** John Sweeney

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31963v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31963v1)

**Summary:** Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only...

---

### 19. Making Sense of Touch from the Child's View for Contrastive Learning

**Authors:** Max Whitton, Zecheng Wang, Puchen Liu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31943v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31943v1)

**Summary:** Is the sense of touch a mechanism for human babies' learning of visual concepts? If so, can we quantify its importance, and to what extent do babies rely on their sense of touch for visual learning? To approach these questions in a principled way, we propose a structured coding system for baby-centric touch events, yielding a dataset of 264k two-second clips of touch events coded according to this system. Using this dataset, we pretrain developmentally grounded models that reveal promising insig...

---

### 20. FlexViT: A Flexible FPGA-based Accelerator for Edge Vision Transformers

**Authors:** Hubert Dymarkowski, Xingjian Fu, Rappy Saha, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31938v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31938v1)

**Summary:** Deploying Vision Transformer (ViT) models on edge platforms remains challenging due to their high computational demands and the architectural heterogeneity of modern hybrid ViT models, which incorporate both fully connected and convolutional layers. This heterogeneity leads to significant variation in tensor shapes, requiring flexible and efficient FPGA-based acceleration. In this paper, we present FlexViT, a reconfigurable FPGA accelerator for efficient ViT inference on resource-constrained edg...

---

### 21. Interface-Aware Neural Newton Preconditioning for Robust Cohesive Zone Model Simulations

**Authors:** Zhangyong Liang, Huanhuan Gao

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31921v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31921v1)

**Summary:** Cohesive Zone Models (CZMs) are widely used to simulate interface fracture, delamination, adhesive failure, and fiber--matrix debonding in aerospace composite structures. In implicit quasi-static finite element analyses, cohesive softening may introduce negative interface tangents, solution jumps, and Newton-basin mismatch, so the previous converged state can become a poor initial guess for the next increment. This may lead to stagnation, wrong-branch convergence, or repeated step cuts. Existing...

---

### 22. Accelerating Conformal Prediction via Approximate Leave-One-Out

**Authors:** Jiachen Cong, Jingbo Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31915v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31915v1)

**Summary:** While conformal prediction provides a general framework for uncertainty quantification in predictive inference, its application is often limited by computational cost. Recent methods, including Jackknife+ and Jackknife-minmax, achieve faster computation by trading a slight loss of efficiency relative to full conformal prediction, but still requires computing leave-one-out refits for all observations. In this paper, we further accelerate conformal prediction by incorporating approximate leave-one...

---

### 23. Sequential RC-TGAN: Generating Relational Time Series with Spectral Envelope Loss

**Authors:** Mohamed Gueye, Yazid Attabi, Manuel Morales, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31904v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31904v1)

**Summary:** The generation of synthetic relational databases often involves modeling complex temporal dynamics, such as transaction logs or event sequences. A significant challenge in this domain is the handling of categorical time series (e.g., status codes), where standard encoding methods like one-hot encoding fail to capture intrinsic frequency-domain features such as seasonality and cyclicity. In this paper, we introduce Sequential RC-TGAN (Seq. RC-TGAN), a temporal extension of the RC-TGAN framework, ...

---

### 24. Harnessing Textual Refusal Directions for Multimodal Safety

**Authors:** Moreno D'Incà, Massimiliano Mancini, Nicu Sebe

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31876v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31876v1)

**Summary:** To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary f...

---

### 25. Review Residuals: Update-Conditioned Residual Gating for Transformers

**Authors:** Kyle Kramer

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31859v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31859v1)

**Summary:** Residual connections add every sublayer's proposed update with a fixed coefficient of one; the network never evaluates whether an update is reliable before committing it. Drawing on the human-factors principle of independent verification, we introduce Review Residuals, which scale each update by a learned, input-dependent gate conditioned on both the current state and the proposed update: h_l = h_{l-1} + r_l * u_l with r_l = sigmoid(W[RMSNorm(h_{l-1}), RMSNorm(u_l)]). Conditioning the gate on th...

---

### 26. Low-dimensional topology of deep neural networks

**Authors:** Junyu Ren, Lek-Heng Lim

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31856v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31856v1)

**Summary:** We study layered models, including feedforward networks, ResNets, and transformers, by limiting each layer to a width of $d = 3$, i.e., $\mathbb{R}^3$ as representation space. This allows us to track how a neural network changes low-dimensional topological invariants through its layers. Just about any topological structure may be simplified or even trivialized by simply increasing dimension; e.g., any knot is equivalent to an unknot in $\mathbb{R}^4$. By restricting to $\mathbb{R}^3$, we not onl...

---

### 27. Explicit Fuzzy Logic in the Feed-Forward Layer: Self-Forgetting Quantifiers Discover Legible Grammatical-Licensing Detectors

**Authors:** Mark Oskin

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31845v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31845v1)

**Summary:** A transformer's feed-forward (FFN) sublayer materializes the distinctions attention gathers, yet gives no account of what it computes. In a parameter-neutral replacement, each hidden unit is an explicit fuzzy set operation on sigmoid-bounded [0,1] memberships: intersection A*B and set-difference A*(1-B), the latter a bounded positive negation ("A but not B") that gated/bilinear units lack -- a negation-capable FFN (NC-FFN). On N-bit parity they are the most parameter-efficient reasoning basis at...

---

### 28. Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR

**Authors:** Ruijia Zhang, Jiacheng Zhu, Hanqing Zhu, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31813v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31813v1)

**Summary:** Low-rank adaptation (LoRA) and its variants enable parameter-efficient fine-tuning of large language models under the supervised fine-tuning (SFT) paradigm. However, their efficacy and behavior under Reinforcement learning with verifiable rewards (RLVR) are less well understood. In particular, two structurally initialized LoRA variants, PiSSA and MiLoRA, which outperform standard LoRA under SFT, can underperform standard LoRA under RLVR and may even exhibit training instability. These observatio...

---

### 29. Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models

**Authors:** Keivan Faghih Niresi, Alice Cicirello, Olga Fink

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31804v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31804v1)

**Summary:** Accurate energy demand forecasting is essential for the reliable operation and planning of modern sustainable energy systems. Spatial-temporal graph neural networks (STGNNs) have recently achieved strong performance in point forecasting by jointly modeling temporal dynamics and relational dependencies across interconnected energy nodes. However, in real-world energy systems, accurate point forecasts alone are insufficient, as operators also require reliable uncertainty estimates to support risk-...

---

### 30. Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers

**Authors:** Ying Fan, Anej Svete, Kangwook Lee

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31779v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31779v1)

**Summary:** Language models typically reason via explicit chain-of-thought (CoT), generating intermediate steps token-by-token. Latent CoT offers an alternative: it performs multi-step reasoning in the model's hidden states, replacing decoded tokens with continuous representations for greater efficiency. However, existing latent CoT methods underperform explicit CoT beyond 1B parameters, and the gap widens with scale. Looped, or recurrent-depth, Transformers, which reuse their weights to increase computatio...

---

### 31. Policy Optimization Achieves Data-Dependent Regret Bounds in MDPs with Unknown Transitions

**Authors:** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31769v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31769v1)

**Summary:** We study policy optimization for online episodic tabular Markov decision processes with unknown transition kernels, aiming for best-of-both-worlds guarantees together with data-dependent regret bounds. Recent work (Dann et al., 2023; Li et al., 2026) has shown that policy optimization can adapt to both adversarial and stochastic losses with first-order, second-order, and path-length bounds, but only under known transitions, leaving open whether such data-dependent guarantees are achievable by po...

---

### 32. Addressing Over-Refusal in LLMs with Competing Rewards

**Authors:** Taeyoun Kim, Aviral Kumar

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31748v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31748v1)

**Summary:** Safety training on language models often induces over-refusal: improved safety on harmful prompts at the cost of increased refusal on harmless ones. Though this trade-off can be mitigated by training models with reinforcement learning (RL) to reason before answering, it does not remove the underlying problem that reasoning can often be a "rubber stamp" for a predetermined response. In this paper, we address the safety-refusal trade-off by rethinking how models are trained to reason about safety....

---

### 33. FedXDS: Leveraging Model Attribution Methods to counteract Data Heterogeneity in Federated Learning

**Authors:** Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31742v1)

**Summary:** Explainable AI (XAI) methods have demonstrated significant success in recent years at identifying relevant features in input data that drive deep learning model decisions, enhancing interpretability for users. However, the potential of XAI beyond providing model transparency has remained largely unexplored in adjacent machine learning domains. In this paper, we show for the first time how XAI can be utilized in the context of federated learning. Specifically, while federated learning enables col...

---

### 34. STEB: Style Text Embedding Benchmark

**Authors:** Rafael Rivera Soto, Anna Wegmann, Cristina Aggazzotti

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31741v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31741v1)

**Summary:** While semantic embeddings are rigorously evaluated on the Massive Text Embedding Benchmark, the evaluation of style embeddings remains fragmented, with each work relying on their own set of tasks and datasets. To bridge this gap, we introduce the Style Text Embedding Benchmark, a comprehensive open-source benchmark intended to standardize the evaluation of style embeddings. STEB encompasses 96 datasets across 7 languages, spanning applications such as authorship verification, authorship retrieva...

---

### 35. Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation

**Authors:** Dominika Woszczyk, Andreas Triantafyllopoulos, Jura Miniota, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31729v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31729v1)

**Summary:** Text-to-speech (TTS) evaluation is an open challenge. While the primary target was "naturalness," recent fidelity gains shifted focus toward "appropriateness" and whether speech is correct for its context. In this work, we examine how perception changes when the expected downstream use varies. We measure the appropriateness and human-likeness of five SOTA TTS systems across five domains: AI assistant, reader, actor, animated character, and spontaneous speaker. Results show appropriateness varies...

---

### 36. Nonlinearity-Aware LoRA: Structured Gate Adaptation under Low-Rank Constraints

**Authors:** Shuai Yuan, Sudong Cai, Bingzhi Chen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31717v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31717v1)

**Summary:** Low-rank adaptation (LoRA) is commonly viewed as an update-space approximation to full fine-tuning, yet this view is incomplete for self-gated Transformer feed-forward networks. In gated FFNs, a low-rank residual can change not only projected features but also the nonlinear selection weights that determine which channels contribute to the output. We formalize this effect as selection misalignment and connect it to the local effective homogeneity of self-gated activations. This motivates a nonlin...

---

### 37. WIDER-FAIR: An Annotated Version of the WIDER-FACE Dataset for Fairness Evaluation

**Authors:** Maxime Moussi, Benoît Ronval, Siegfried Nijssen, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31704v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31704v1)

**Summary:** The deployment of face detection models in real-world applications raises important fairness concerns, as these systems may showcase performance disparities across demographic groups. A key obstacle to studying and mitigating such biases is the lack of face detection datasets with sensitive feature annotations. To address this gap, we introduce WIDER-FAIR, a new dataset built on the widely used WIDER-FACE benchmark, manually annotated with the perceived ethnicity and sex of each face. The datase...

---

### 38. Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

**Authors:** Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31700v1)

**Summary:** Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically plausible learning rules avoid backpropagation's weight transport requirement, but it has been difficult to achieve strong performance under Dale's principle beyond MNIST. Error Diffusion (E...

---

### 39. When to Truncate a Feature Ranking: A Residual-Overlap Stopping Rule for Subset Selection

**Authors:** Jesus S. Aguilar-Ruiz

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31686v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31686v1)

**Summary:** Feature rankings are widely used in supervised feature selection because they are simple, scalable and easy to interpret. Variables are first ranked by a relevance score, and a subset is then obtained by retaining the top-ranked variables. Although the first stage has been extensively studied, the second is often governed by an arbitrary cardinality, an empirical threshold or cross-validation, without a direct interpretation. This raises a basic question: given a feature ranking, when is there e...

---

### 40. Histogram-constrained Image Generation

**Authors:** Haoming Liu, Yuanhe Guo, Yijia Cao, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31683v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31683v1)

**Summary:** Diffusion models have emerged as a dominant paradigm in generative modeling, enabling high-fidelity sampling from complex data distributions. Despite impressive capabilities, controlling diffusion models to produce outputs aligned with user intent remains an open challenge, especially when balancing global coherence with local precision. Existing control mechanisms vary in the granularity of their conditioning signals. For example, textual prompts guide generation globally through high-level sem...

---

### 41. Improving Certified Robustness via Adversarial Distillation

**Authors:** Matteo Melis, Jesus Martinez Del Rincon, Vishal Sharma

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31653v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31653v1)

**Summary:** Certified training aims to produce models whose predictions can be formally verified against adversarial perturbations, typically by optimising upper bounds on the worst-case loss over an allowed perturbation set. For neural networks, certified training methods based purely on tight relaxation bounds produce networks that are amenable to certification, but sacrifice standard accuracy. Conversely, adversarial training often yields stronger empirical robustness and standard accuracy, but the resul...

---

### 42. ECHO: Prune to act, trace to learn with selective turn memory in agentic RL

**Authors:** Zijun Xie, Binbin Zheng, Enlei Gong, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31650v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31650v1)

**Summary:** Long-horizon language agents must repeatedly interact with tools, accumulate evidence, and make decisions under bounded context windows. Existing context-management methods make such rollouts feasible by truncating distant history, folding past turns into summaries, or selecting compact memory states. However, these breakthroughs introduce two coupled limitations. First, as the number of turns grows, historical observations are progressively removed or collapsed into compressed states, making it...

---

### 43. Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents

**Authors:** Utsav Garg, Sungjin Hong, Jason Jung, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31648v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31648v1)

**Summary:** We present LuckyStar 111B, a 111B-parameter hybrid reasoning model developed through a collaboration between Cohere and LG CNS for Korean-English enterprise agents under practical memory and serving constraints. The model trains from Cohere's fully post-trained Command A model rather than a new pretraining run, and uses preamble conditioning to switch between concise non-reasoning behavior and longer tool-oriented reasoning. We study four choices for scaling tool-using agents efficiently: multil...

---

### 44. Calibration, Not Compilation: Detecting and Repairing Misspecified Probabilistic Programs Written by Language Models

**Authors:** Jian Xu, Delu Zeng, John Paisley, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31630v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31630v1)

**Summary:** Language models increasingly write probabilistic programs (in NumPyro, Stan, or Pyro), but a program that compiles, runs, and passes every unit test can still be \emph{statistically} wrong -- a Gaussian likelihood for heavy-tailed data, a Poisson for over-dispersed counts, an invalid prior support, or a pathological parameterization. The right verifier is therefore not a test suite but the Bayesian workflow itself: posterior predictive checks, simulation-based calibration, sampler diagnostics ($...

---

### 45. Preserve the Hard, Regenerate the Rest: Uncertainty-Guided Synthetic Training Data Augmentation with Diffusion Models

**Authors:** Nikolai Röhrich, Julian Gleißner, Ahmed H. A. Ibrahim, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31603v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31603v1)

**Summary:** Semantic segmentation models struggle with data sparsity and rare or visually diverse regions, e.g., dense regions or small objects in aerial or autonomous mobility data. While synthetic augmentation is an appealing solution, directly generating new labeled data risks misalignment of labels and generated pixels. Existing solutions to this problem often rely on external models, or employ coarse heuristics such as indiscriminately augmenting all foreground objects or entire backgrounds, which wast...

---

### 46. On Optimal Data Splitting for Split Conformal Prediction

**Authors:** Sayan Das, Bahram Yaghooti, Todd A. Kuffner, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31600v1)

**Summary:** Conformal prediction and its variants, including the split conformal prediction, provide a distribution-free framework for uncertainty quantification by constructing prediction intervals or sets with finite-sample coverage guarantees. The statistical efficiency of these intervals depends critically on how the data are split into training and calibration samples. Despite its practical importance, a principled characterization of the training-calibration split that minimizes prediction interval le...

---

### 47. Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment

**Authors:** Jason R. Brown, Patrick Leask, Lev McKinney

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31591v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31591v1)

**Summary:** Emergent misalignment (EM) is a recently discovered phenomenon in LLMs where fine-tuning on a narrow misaligned task, such as writing insecure code, leads to broadly misaligned behaviour on unrelated prompts. Previous work has noted that the severity of EM is highly sensitive to training choices; however, we still lack a systematic characterisation of this sensitivity. We perform a sweep over several Qwen3 models, optimisers, datasets, and batch sizes, and find that the choice of optimiser has t...

---

### 48. From Failure to Alignment: A Requirements Engineering Framework for Machine Learning Systems

**Authors:** Amel Bennaceur, Gopi Krishnan Rajbahadur, Prince Mercy, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31589v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31589v1)

**Summary:** Organisations designing, developing, and deploying machine learning systems (MLS) need to be able to check that these systems are trustworthy, and communicate this clearly to their stakeholders, be they different categories of users, engineers, or wider society. By focusing on stakeholders, Requirements Engineering is well positioned to drive the design and engineering of MLS that align with the needs of their stakeholders. Yet, we still need a systematic process for modelling and reasoning abou...

---

### 49. Robustness of neural networks to random noise perturbations of their inputs

**Authors:** Mark Levene, Martyn Harris

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31581v1)

**Summary:** We investigate the problem of the robustness of a trained neural network to the perturbation of its input values. More specifically, we examine the interplay between the accuracy of the network, as measured by the mean squared error, and robustness. Accordingly, we present a robustness measure, which, with high probability, suggests an upper bound on the mean squared error of the network, with respect to an input data set, for a given perturbation of the input values of the network. The measure ...

---

### 50. Localized Conformal Prediction for Image Classification with Vision-Language Models

**Authors:** Clément Fuchs, Tim Bary, Benoît Macq

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31577v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31577v1)

**Summary:** Conformal predictions have attracted significant attention in the field of uncertainty quantification, mainly because of their strong marginal coverage guarantees. Full conditional guarantee is not an attainable goal, a well known fact in conformal predictions literature. As a result, several approaches have tried to approximate this behavior by adapting the conformal sets of test-time samples according to their similarity to calibration examples. Although the latter has gained traction and show...

---

## cs.NE

**50 papers**

### 1. Evaluation of Population Initialization Methods for Genetic Programming-based Symbolic Regression

**Authors:** Lukas Kammerer, Gabriel Kronberger, Deaglan J. Bartlett, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31990v1)

**Summary:** We analyze the effect of optimizing the initial population of genetic programming (GP) for symbolic regression (SR) on the accuracy and complexity of solutions. We compare three well-established random initialization methods as well as initialization with small optimized solutions from exhaustive symbolic regression (ESR) using a GP/SR implementation which is based on the multi-objective evolutionary algorithm NSGA-II. We compare the final Pareto fronts found with each initialization method on t...

---

### 2. Distributed Hierarchical Temporal Memory with Shared Associative Memory for Cross-Entity Preemptive Warning

**Authors:** Pavia Bera, Jennifer Adorno, Sanjukta Bhanja

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31789v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31789v1)

**Summary:** Anomaly detection in multivariate time series remains a critical challenge in large-scale distributed systems, where related entities may exhibit transferable precursor behavior prior to anomaly onset. Existing methods typically operate independently on each data stream and therefore remain fundamentally reactive. To address this limitation, we introduce Distributed Hierarchical Temporal Memory (D-HTM), a neuromorphic framework that enables cross-entity preemptive warning through a Shared Associ...

---

### 3. Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

**Authors:** Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31700v1)

**Summary:** Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically plausible learning rules avoid backpropagation's weight transport requirement, but it has been difficult to achieve strong performance under Dale's principle beyond MNIST. Error Diffusion (E...

---

### 4. A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31584v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31584v1)

**Summary:** This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronge...

---

### 5. Robustness of neural networks to random noise perturbations of their inputs

**Authors:** Mark Levene, Martyn Harris

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31581v1)

**Summary:** We investigate the problem of the robustness of a trained neural network to the perturbation of its input values. More specifically, we examine the interplay between the accuracy of the network, as measured by the mean squared error, and robustness. Accordingly, we present a robustness measure, which, with high probability, suggests an upper bound on the mean squared error of the network, with respect to an input data set, for a given perturbation of the input values of the network. The measure ...

---

### 6. Partition-Guided Distance Saliency: Bridging Decision and Objective Spaces in Many-Objective Optimization

**Authors:** Cláudio Lúcio do Val Lopes, Flávio Vinícius Cruzeiro Martins, Elizabeth Fialho Wanner

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30836v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30836v1)

**Summary:** Explainability in Many-Objective Optimization (MaO) is currently hindered by the escalating complexity of the Pareto front, which renders the relationship between high-dimensional decision variables and objective outcomes increasingly opaque. As the number of objectives exceeds the limits of traditional visualization, decision-makers encounter a ``cognitive drought'' in identifying relevant trade-offs or specifying target regions without a priori knowledge. To bridge this interpretability gap, w...

---

### 7. Why can genetic algorithms work in high-dimensional search spaces?

**Authors:** Stephen Whitelam

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30619v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30619v1)

**Summary:** We show that the effective dynamics of the elitist $(1+M)$ genetic algorithm is, in the limit of small mutations, clipped gradient descent on the loss in the presence of anisotropic Gaussian white noise. In expectation, therefore, a simple mutation-selection genetic algorithm follows the gradient of the loss, without explicit calculation of gradients and without averaging over loss evaluations. The genetic algorithm is slower than gradient descent because of the noise that acts in directions tra...

---

### 8. Computing the Integral R2 Indicator by Perspective Mapping and Box Decomposition

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30530v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30530v1)

**Summary:** The continuous integral R2 indicator is a Pareto-compliant refinement of the classical finite-weight-vector R2 indicator, used in performance assessment, bounded archiving for a-posteriori multi-objective optimization, and skyline selection in databases. This work introduces a bidirectional perspective mapping between continuous integral R2 computation and integration over unions of anchored axis-aligned boxes. After translating the ideal point of a minimization problem to the origin, approximat...

---

### 9. Minimal MMAO: A Resource-Closed-Loop Framework for Adaptive Metaheuristic Search

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30450v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30450v1)

**Summary:** This paper presents the Metabolic Multi-Agent Optimizer (MMAO) as an adaptive metaheuristic built around endogenous resource circulation. The central premise is that search intensity, exploration--exploitation balance, and lifecycle turnover should be induced by a shared metabolic controller rather than by separately attached schedules. We formulate MMAO through bounded private energy, a communal budget, normalized reward, continuous role adaptation, and resource-financed branching and pruning. ...

---

### 10. From Detecting Agency to Doing Work: Self-Caused Credit Builds a Durable Behavioral Self in a Minimal Spiking Agent

**Authors:** Haoliang Han

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30191v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30191v1)

**Summary:** How does an agent that can tell self from world come to be durably shaped by that distinction? Recent work shows that a predictive system can detect its own agency (Ye, 2026), but detecting agency does not explain durable, self-shaped behavior. We show that agency-gated slow credit -- a conjunctive term Own*Agency*Salience driving a slow parameter update -- produces post-unload behavioral residue: on a spiking substrate (Nengo LIF/PES), a learned self-preserving choice survives episodic buffer r...

---

### 11. Semantics-Aware Bilevel Co-Evolution: Towards Automated Multicomponent Algorithm Design

**Authors:** Zhiyao Zhang, Shenghao Wu, Xingyu Wu, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29953v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29953v1)

**Summary:** LLM-assisted evolutionary search (LES) has emerged as a promising paradigm for automated algorithm design. However, existing methods usually suffer from two inherent limitations when facing the automated design of real-world complex algorithms that usually consist of multiple components. The first limitation is that they either focus on modifying entire algorithms, making it difficult to reuse high-quality components, or concentrate on component refinement within a limited set of predefined mult...

---

### 12. Evolutionary Hyperparameter Optimization to Find Lightweight CNN Models for Autonomous Steering

**Authors:** Devson Butani, Ryan Kaddis, Chan-Jin Chung

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29684v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29684v1)

**Summary:** This research investigates the optimization of Convolutional and Dense Neural Networks (CNNs and DNNs) for autonomous steering using the (N+M) Evolution Strategy (ES) with the 1/5th success rule. The primary objective is to develop a lightweight CNN based model capable of real-time steering angle prediction, mimicking human driving behavior on predefined paths. The ES algorithm automates hyperparameter tuning, dynamically adjusting parameters such as filter sizes and layer configurations. Data c...

---

### 13. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 14. Supervised Hebbian learning in Deep Counterstream Associative Networks

**Authors:** Andreas Knoblauch

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29528v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29528v1)

**Summary:** Modern machine learning applications employ deep neural networks training with the error backpropagation algorithm. Although this algorithm is very effective, it lacks biological realism. For example, backpropagation requires symmetric connectivity, and a separate neural processing channel for error signals. Prior works have therefore proposed a number of more realistic alternatives for error backpropagation. However, most of them still suffer from demanding preassumptions that may be not fulfil...

---

### 15. When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning

**Authors:** Zhengqi Pei, Qingming Huang, Shuhui Wang

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29354v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29354v1)

**Summary:** Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. We propose Communicative Language Symbolism Routing (CLSR), a test-time framework in which multiple LLM agents autonomously invent, evolve, and share compact Language Symbolism Frameworks (LSFs), while a latent-free router adaptively selects and composes these languages per query to optimize the a...

---

### 16. Travel-Oriented Reasoning Large Language Model via Domain-Specific Knowledge Graphs

**Authors:** Vignesh Ram Nithin Kappagantula, Shayan Hassantabar, Samuel Simpson, et al.

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29254v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29254v1)

**Summary:** Large language models (LLMs) demonstrate broad reasoning abilities but struggle with accuracy and reliability in specialized domains such as travel, where reasoning depends on precise definitions, rules, and expert-defined conceptual frameworks, and where confident but unfounded outputs arise from a reasoning failure in which the model has not internalized the underlying domain graph rather than from missing domain knowledge alone. We propose a modular pipeline for building a travel-domain reaso...

---

### 17. Unified Complex-valued Neural Network: A Magnitude-Phase Computational Model for Event-Driven Neuromorphic Learning

**Authors:** Reza Ahmadvand, Sarah Safura Sharif, Yaser Mike Banad

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29099v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29099v1)

**Summary:** Artificial neural networks (ANN) provide accurate continuous-valued representation, whereas spiking neural networks (SNN) offer event-driven temporal processing, yet both paradigms face limitations when value encoding and timing dynamics must be learned within a single computational structure. This paper introduces a network based on Unified Complex-valued Neuron (UCN), a new neural computational model that integrates continuous activation and phase-driven event generation through an asymmetric ...

---

### 18. Road to scalability for efficient graph search on massively parallel neuromorphic hardware

**Authors:** Oskar von Seeler, Elena C. Offenberg, Carlo Michaelis, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28907v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28907v1)

**Summary:** Efficient computation of shortest paths in weighted graphs is a fundamental problem with many applications. Neuromorphic hardware platforms promise massively parallel, efficient computation, changing parallelism tradeoffs. In this work, we introduce NEURO-MAPP (Neuromorphic-based Min-Add Parallel Propagation), a distributed shortest path algorithm designed to use the local computation and network communication available in neuromorphic systems. We provide an optimized implementation of the algor...

---

### 19. Closed-Form Steepest Descent Direction toward Flat Minima: Reducing Upper Bounds on the Loss Hessian Eigenspectrum in Neural Networks

**Authors:** Yuto Omae, Kazuki Sakai, Yohei Kakimoto, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28662v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28662v1)

**Summary:** The flatness hypothesis suggests that flatness of the loss landscape, as measured by the eigenvalues of the loss Hessian, correlates with better neural network generalization. While various algorithms reduce these eigenvalues, most focus on procedural design, leaving it unclear how data distributions and NN parameters structurally determine directions toward flat minima. Characterizing these directions analytically is generally intractable. To overcome this mathematical difficulty, recent studie...

---

### 20. Analysis of Parameter Settings for the Bat Algorithm Using Variance Evolution

**Authors:** Xin-She Yang, Mehmet Karamanoglu

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28644v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28644v1)

**Summary:** Parameter settings in evolutionary algorithms and metaheuristics are important because such parameter values can influence the performance of algorithms under evaluation. For a given algorithm, there are many different numerical experiments to show that the algorithm can work well in practice; however, in most cases there is no theoretical analysis of parameter settings. In this work, we show that theoretical analysis using the theory of dynamical systems and evolution of population variance can...

---

### 21. Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation

**Authors:** Binh Nguyen, Colleen Josephson, Mircea Teodorescu, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28600v1)

**Summary:** Neuromorphic and edge computing research has focused on reducing the inference cost of neural network controllers, yet in physical closed-loop systems the actuator can rival or exceed an efficient controller in energy. An efficient controller is therefore necessary but not sufficient, because the actuator becomes the cost worth reducing once inference no longer dominates it. Here, we introduce energy-aware learning, an approach that incorporates actuator energy directly into the reinforcement le...

---

### 22. Comparing Scalar Objective Functions for Multi-Criteria Engineering Optimization

**Authors:** Olaf Frommann

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28541v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28541v1)

**Summary:** Scalar objective functions are required when a multi-criteria optimization problem must yield a single preferred design rather than only a Pareto set. The choice of scalarization influences which compromise is selected, how preference parameters are interpreted, and whether non-supported Pareto regions can be reached. This paper compares four formulations for normalized bi-criteria minimization: weighted sums, achievement scalarizing functions, desirability functions, and a fuzzy-logic-based for...

---

### 23. MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28109v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28109v1)

**Summary:** Traditional meta-heuristics often rely on fixed population sizes, manually chosen search scales, and externally attached parameter-control modules. This paper presents the \textit{Metabolic Multi-Agent Optimizer} (MMAO), a cross-domain optimization framework in which adaptation is derived endogenously from a private-public metabolic resource loop. Each agent carries internal energy, a continuous role state, motion or structural memory, and local search history, while the population shares a comm...

---

### 24. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 25. Co-Optimization of Analog Kolmogorov-Arnold Networks for Low-Power Function Approximation in Flexible Electronics

**Authors:** Paula Carolina Lozano Duarte, Georgios Zervakis, Mehdi Tahoori, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27892v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27892v1)

**Summary:** Wearable devices and Internet of Things (IoT) sensors require on-sensor processing of biosignals and environmental data, including computationally demanding operations such as nonlinear activation functions for neural network inference, sensor calibration curves to map raw readings to physical units, and signal preprocessing functions like logarithmic compression and power operations for feature extraction. These functions exhibit significant complexity, often involving transcendental operations...

---

### 26. Criticality-Constrained Iterative Pruning for Energy-Efficient Spiking Neural Networks via Combined Importance Scoring

**Authors:** Muhammad Hamza

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.30676v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30676v1)

**Summary:** Deploying spiking neural networks (SNNs) on neuromorphic hardware demands aggressive synaptic pruning while preserving temporal computation integrity. Existing strategies either neglect neuronal criticality or rely on convex relaxations of the inherently combinatorial pruning problem whose fractional masks, upon binarisation, destroy accuracy at moderate-to-high sparsity. We present Criticality-Constrained Quadratic Pruning (CQP), a native PyTorch pipeline that fuses weight magnitude with surrog...

---

### 27. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 28. DE-2LS: Differential Evolution with Lightweight Late Local Search for Constrained Numerical Optimization

**Authors:** Dikshit Chauhan, Anupam Trivedi

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27764v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27764v1)

**Summary:** Constrained single-objective numerical optimization requires a careful balance among feasibility, objective convergence, and computational efficiency under a fixed function-evaluation budget. This paper proposes DE-2LS, a late-stage, locally search-enhanced variant of differential evolution built on the RDEx framework. The proposed method preserves the original RDEx components, including mutation and crossover operators, success-history adaptation, archive mechanism, population-size reduction, a...

---

### 29. DE-2LS: Differential Evolution with Late-Stage local-search for Unconstrained Single-Objective Numerical Optimization

**Authors:** Dikshit Chauhan

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27762v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27762v1)

**Summary:** Unconstrained single-objective numerical optimization requires a careful balance among global exploration, late-stage exploitation, and function-evaluation efficiency. This paper presents DE-2LS, a late-stage, local-search-enhanced differential evolution framework built on RDEx for unconstrained single-objective optimization with variable bounds. The proposed method preserves the original RDEx evolutionary search engine and introduces two conservative refinements: a smoothed exploitation-biased ...

---

### 30. Multi-Objective Molecular Generation with Frequency-Controlled Evolutionary Dynamics

**Authors:** Elia Colleoni, Paolo Guida, Didier Barradas-Bautista, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27467v1)

**Summary:** Molecule generation methods that leverage generative models have been successfully applied to drug discovery. However, they often require extensive pre-training, suffer statistical biases in the training data, and might suffer from limited interpretability of generated chemical structures. In this work, we introduce SpectralMol, an algorithm based on evolutionary computation that processes chemical structures as a compact matrix of Fourier coefficients, projected onto a fixed basis to generate p...

---

### 31. CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear Attention

**Authors:** Sayak Dutta

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27229v2) | 📄 [PDF](https://arxiv.org/pdf/2606.27229v2)

**Summary:** Recurrent models must forget in order to remember, yet the state of the art decides what to erase without consulting what is stored -- the gate sees only the arriving token, not the memory it is about to modify. This memory-blind gating is one of three coupled defects in the leading delta-rule architecture (GDN-2): the value-axis erase mask wastes parameters at the scale of the value projection, and -- as we prove -- mathematically prevents the WY-form triangular chunk solver that makes recurren...

---

### 32. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 33. Random Walk on Bézier Curves for Global Optimization

**Authors:** Jinpeng Wang, Xingguo Xu, Yujing Sun, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26714v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26714v1)

**Summary:** Balancing exploration and exploitation remains a central challenge in metaheuristic optimization. To address this issue, this paper proposes Bézier Walk Evolution (BWE), a geometry-driven optimization framework that reformulates evolutionary search as adaptive trajectory construction in the decision space. BWE integrates Bézier curve modeling with a distance-aware random walk mechanism to generate topology-guided search trajectories. By adaptively varying the curve order during evolution, the pr...

---

### 34. Three-Objective Integral R2 Subset Selection: NP-Hardness and Submodular Approximation

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26591v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26591v1)

**Summary:** Selecting a fixed number of representative points from a finite Pareto-front approximation is a fundamental post-processing task in multiobjective optimization. This paper studies this problem for the integral R2 indicator in three objectives, where the indicator is defined as the integral of the lower envelope of weighted Tchebycheff scalarizations over the two-dimensional weight simplex. We provide two complementary algorithmic results. On the positive side, we show that the integral R2 improv...

---

### 35. The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators

**Authors:** Alex Iacob, Andrej Jovanović, William F. Shen, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26294v2) | 📄 [PDF](https://arxiv.org/pdf/2606.26294v2)

**Summary:** Self-improving agents are state-of-the-art (SOTA) on agentic coding benchmarks and have recently been extended to general domains. However, their search methods generally assume a stationary evaluation criterion: a fixed verifier, benchmark, or labeled dataset that remains valid as the agent improves. This ignores a central feature of evolution: species adapt as their environments change with them. We aim to bring the same principle to recursive self-improvement, making evaluation part of the im...

---

### 36. EvoFlock: evolved inverse design of multi-agent motion

**Authors:** Craig Reynolds

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25280v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25280v1)

**Summary:** This paper describes an automatic method for adjusting or tuning models of multi-agent motion. Simulating the motion of bird flocks, human crowds, vehicle traffic, and other multi-agent systems is a widely used technique. These simulations model the behavior of a single group member (bird, human, or vehicle). The group behaviors (flock, crowd, traffic) emerge from interactions between group members. These models typically have many numerical control parameters. Even if each parameter is intuitiv...

---

### 37. Spatial Partial Functionalization of Neural Networks based on Noise Fields

**Authors:** Shuhei Ikemoto, Fabio DallaLibera

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24588v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24588v1)

**Summary:** Noise in neural computation is typically regarded as a disturbance, but its spatial distribution may also actively regulate which parts of a network participate in computation. This paper investigates the spatial partial functionalization of Noise-modulated Neural Networks using noise fields. We first present an activation function suitable for this goal, the crossing activation function, using the sample-level, statistical-level, and analytical-level implementations, and examine parameter reuse...

---

### 38. What Does a Pathological Speech Assessment Model Know about Acoustic Features? A Case Study on Oral and Oropharyngeal Cancer Patients

**Authors:** Tuan Nguyen, Corinne Fredouille, Alain Ghio, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24949v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24949v1)

**Summary:** This work investigates the interpretability of a Wav2Vec 2.0based speech intelligibility assessment model for oral and oropharyngeal cancer patients through canonical correlation analysis. By measuring the correlation between the model embeddings and eGeMAPS low-level descriptors (LLDs) as an interpretable reference, we analyze how acoustic information is encoded across the model layers. The analysis is conducted at two levels: individual LLDs layer-wise, and group-level: prosodic, spectral, and...

---

### 39. Distributed Quality-Diversity Search for Toxicity in Large Language Models

**Authors:** Onkar Shelar, Travis Desell

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24166v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24166v1)

**Summary:** Large Language Models remain vulnerable to adversarial prompts that elicit harmful responses, and scaling red-teaming to cover a broad range of failure modes is constrained by the cost of text generation and evaluation. We present \emph{ToxSearch-S}, a speciated extension of toxicity-focused evolutionary prompt search with incremental, embedding-driven niche maintenance, together with an MPI master-worker realization that centralizes population and species bookkeeping on rank~0 while offloading ...

---

### 40. Identifying structural design principles shaping the computational abilities of recurrent neural networks

**Authors:** Tom Talpir, Elad Schneidman

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23874v1)

**Summary:** Understanding how the architecture of neural networks shapes the computations they carry is a central challenge in neuroscience and machine learning. While specific circuit architectures have been linked to particular network computations and theoretical bounds on expressivity of broad classes of networks have been found, we are still missing general principles connecting the structure of finite networks to their computational capabilities. Here, we characterize the computational abilities of re...

---

### 41. It's Much Easier for Neural Networks to learn Game of Life Dynamics with the Right Activation Function: Polynomial Kolmogorov-Arnold Networks

**Authors:** Tashin Ahmed, Q. Tyrell Davis

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23587v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23587v1)

**Summary:** Previous work has found a gap between the scale of neural networks that reliably learn Conway's Game of Life, and minimal networks capable of representing the classic cellular automaton with hard-coded parameter values. Viewing neural network learning as a search process suggests a dependence on networks large enough to contain sub-networks with lucky initializations (sometimes known as 'winning tickets') that actually learn the task. In this work, we reorient our perspective from discovering Li...

---

### 42. An Open-Source LFSR-Based Stochastic Leaky Integrate-and-Fire Neuron in SkyWater 130 nm: Design, Stochastic Characterisation, and Rate Coding

**Authors:** Poornima Kumaresan, Santhosh Sivasubramani

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23532v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23532v1)

**Summary:** Stochastic spiking neurons trade exact arithmetic for controlled randomness, lowering area and tolerating input noise, which suits event-driven edge hardware. We present a compact, configurable stochastic leaky integrate-and-fire neuron in standard-cell CMOS on the SkyWater 130 nm process, released openly. A 16-bit configurable-polynomial linear-feedback shift register drives an eight-entry programmable activation table that sets a Bernoulli firing probability, and a saturating 16-bit leaky inte...

---

### 43. Local Pheromone Network: Sparse Local Learning with Multi-Scale Synaptic Trails, Consolidation, and Replay

**Authors:** Xingcheng Fu, Xianjun Chen, Zhihao Li

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.30669v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30669v1)

**Summary:** Backpropagation-trained dense neural networks are powerful function approximators, but they couple learning across many parameters and can overwrite previous associations when tasks conflict. This paper describes Local Pheromone Network, a small research prototype for sparse, local, manually updated neural networks. In Local Pheromone Network, each output unit reads only a fixed local neighborhood of input units subject to geometric distance and molecular-tag compatibility. Each synapse stores a...

---

### 44. EML Trees Are Universal Approximators

**Authors:** Joe Germany, Elie Abdo, Joseph Bakarji

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23179v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23179v1)

**Summary:** The recently introduced EML (Exp-Minus-Log) function acts as continuous analogue of NAND gates, providing a compositional building block capable of representing elementary functions. In this work, we study the expressive power of tree-structured compositions of EML functions. We show that such trees enjoy a universal approximation property for functions in $W^{k, \infty}$ for $k \in \mathbb N$, drawing on classical neural network approximation arguments while exploiting the ability to explicitly...

---

### 45. Decomposing Financial Market Dynamics via Mechanism Analysis in an Evolutionary Multi-Agent Simulation

**Authors:** Zhibao Chen

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23158v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23158v1)

**Summary:** Evolutionary agent-based markets (ABMs) couple several mechanisms -- who reproduces, how price forms, how biased the agents are, how consensus propagates -- yet these are usually fixed by convention, so it is unclear which mechanism controls which emergent property. In a coevolving, endogenous-price simulator with 120 heterogeneous behavioral agents, we make four mechanisms pluggable and run matched 3x20-seed interventions. We find the levers are largely separable. (1) Selection -> diversity: a ...

---

### 46. Self-Modulating Quantum Fast-Weight Programmers for Efficient Adaptive Sequential Learning

**Authors:** Samuel Yen-Chi Chen, Yifeng Peng, Kuo-Chung Peng, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.24933v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24933v1)

**Summary:** Recent advances in quantum machine learning have motivated efficient models for sequential data processing. In this paper, we propose Self-Modulating Quantum Fast Weight Programmers, or Self-Modulating QFWP, which extends Quantum Fast Weight Programmers by introducing adaptive modulation over both newly generated fast-weight updates and historical fast-weight memory. Numerical results show that the proposed mechanism improves convergence stability and prediction performance across varying model ...

---

### 47. Recursive QLSTM with Dynamic Variational Quantum Circuit Adaptation

**Authors:** Samuel Yen-Chi Chen, Yifeng Peng, Jiun-Cheng Jiang, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.24932v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24932v1)

**Summary:** Recent advances in quantum computing and machine learning have motivated the development of quantum models for sequential data processing. In this paper, we propose a Recursive Quantum Long Short-Term Memory model, or Recursive QLSTM, which extends QLSTM through metacore-based recursive constructions. We numerically test the model under different input sequence lengths, metacore designs, and recursive rules, and identify the best-performing architecture among these variants. For this selected mo...

---

### 48. Mass Conservation as an Inductive Bias for Self-Organized Criticality in NCA Reservoirs

**Authors:** Tong Zhang, Etienne Guichard, Sidney Pontes-Filho, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23115v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23115v1)

**Summary:** Self-organized criticality (SOC), a dynamical regime associated with maximal information processing, offers a promising foundation for reservoir computing. Recent work has shown that neural cellular automata (NCA) can be evolved toward critical avalanche dynamics and employed as effective reservoirs for memory and classification tasks. Here, we investigate whether mass conservation -- a local redistribution rule that preserves total lattice mass -- serves as an inductive bias toward SOC in evolv...

---

### 49. EEG Benchmarking Needs a Task Specification Layer: NeuroDoc for Rulebook-Guided, Executable Benchmark Construction

**Authors:** Chengxuan Qin, Zhige Chen, Shu Peng, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.22925v1) | 📄 [PDF](https://arxiv.org/pdf/2606.22925v1)

**Summary:** Electroencephalography (EEG) foundation models increasingly rely on multi-dataset training and evaluation, yet public EEG datasets still lack a shared task specification layer that can turn heterogeneous recordings into reusable benchmark units. Existing standards organize files, metadata, and provenance, but they do not specify EEG tasks under a common language and rulebook, leaving critical task semantics scattered across papers, code, and manual interpretation. We investigate whether heteroge...

---

### 50. Evolutionary Optimization Reveals Structural Constraints on Reservoir Architecture for Spatiotemporal Chaos

**Authors:** Nima Dehghani

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.22765v1) | 📄 [PDF](https://arxiv.org/pdf/2606.22765v1)

**Summary:** Biological systems maintain function in fluctuating environments by transforming past stimulation into internal dynamical states that support future-oriented responses. Reservoir computing provides a computational analogue, but standard formulations often treat the recurrent substrate as a fixed random network and train only the readout. Here we ask how the substrate itself changes when reservoir architecture is placed under evolutionary selection for prediction. Using the Kuramoto--Sivashinsky ...

---

## q-bio.NC

**50 papers**

### 1. Stationary covariance spectra of discrete-time non-normal random recurrent dynamics

**Authors:** Jacob A. Zavatone-Veth

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31944v1)

**Summary:** Principal component analysis is widely used to characterize structure in the dynamics of recurrent neural networks. For stationary noise-driven dynamics, the distribution of variance among the principal components is determined by the spectrum of the stationary covariance matrix. While the spectral properties of this matrix are well-understood for linear networks with normal synaptic weight matrices, our understanding of the stationary covariance spectrum for random non-normal dynamics remains i...

---

### 2. Mean-field theory of rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation

**Authors:** Bowen W. Zheng, Earl K. Miller, Ila R. Fiete

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30366v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30366v1)

**Summary:** We develop a dynamical mean-field theory for random recurrent networks with low-rank structure and firing-rate-driven adaptation. When the random connectivity is strong enough to generate chaos, increasing adaptation strength drives the network through four regimes: a static coherent state, noise-sustained oscillations that progress from regular to irregular, stochastic switching between symmetric wells, and a global limit cycle. The theory identifies two instability mechanisms, chaos onset from...

---

### 3. Cohort-amortized personalization: navigating the privacy-utility frontier for virtual brain twins

**Authors:** Amirhossein Esmaeili, Marmaduke Woodman, Nina Baldy, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30329v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30329v1)

**Summary:** Personalized generative brain models require individual neuroimaging data that privacy constraints and re-identification risk make difficult to share, while per-subject fitting procedures cost hours of compute -- limiting clinical translation and multi-site collaboration. We introduce cohort-amortized personalization (CAP), which replaces data sharing with model sharing: a neural density estimator is trained on simulations from a mechanistic whole-brain model under a low-rank cohort prior, and o...

---

### 4. Clear Mind: Meditation and the Brain's Signal-to-Noise Ratio

**Authors:** Ruben Laukkonen

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29698v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29698v1)

**Summary:** Meditation is quintessentially associated with a clear mind. This paper proposes that diverse findings in the science of meditation can be mapped onto a single, empirically tractable construct: functional signal-to-noise ratio in the brain, or f-SNR. Signal denotes neural variance that tracks the goal-relevant causes of sensory input, while noise denotes residual activity, including irrelevant endogenous fluctuations. Mechanistically, meditation increases f-SNR through two primary operations: se...

---

### 5. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 6. Connectivity Estimation using Stochastic Graph Heat Modelling

**Authors:** Stephan Goerttler, Min Wu, Fei He

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29098v1)

**Summary:** A growing number of techniques leverage the spatial structures that underlie many real-world datasets. Despite these advances, the complementary task of estimating spatial structures and understanding their role within these techniques has often been overlooked. In neurophysiological data analysis specifically, numerous methods exist to estimate brain connectivity, but most are not explicitly model-based, dynamic, multivariate, or directed. To address these limitations, we previously introduced ...

---

### 7. Modelling Emotional Memory in Children with Tensor Networks

**Authors:** Henry Groves, Lucia F. Jackson, Barbara-Anne Robertson, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28470v1)

**Summary:** We demonstrate how emotional valence influences the order-dependent structure of children's recognition memory: correct recall of a sequence of emotionally-valenced toys depended not just on the valence of a given toy itself, but also on the valence of the toys shown before and after it. Whilst standard psychological models confirm that order-dependence differs across an event (a set of toys shown in sequence), accuracy is low and the model does not reflect how memory for an emotional object inf...

---

### 8. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 9. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 10. Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks

**Authors:** Mauricio A Diaz, Manuela A. Beyer, Janina Hesse

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27529v1)

**Summary:** Stress is an adaptive response coordinated by neural and physiological systems. While acute stress can enhance survival, chronic stress drives structural brain changes, cognitive dysfunction, and increased psychiatric risk. At the cellular level, chronic stress shifts the excitatory-inhibitory (E/I) balance of prefrontal pyramidal neurons toward inhibitory dominance, yet the mechanisms underlying these alterations are still unknown. We here investigate possible mechanisms causing inhibitory domi...

---

### 11. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 12. Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist

**Authors:** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26448v1)

**Summary:** Across the sciences, autonomous systems are increasingly being used in closed-loop discovery, proposing new theories and designing and running experiments to test them. This approach is yet to be applied in the field of cognitive science, where the central bottleneck is theory-building: the creative step of turning the accumulated failures of existing models into better ones. Theory generation has remained manual even as data collection, modeling, and experiment design have been automated. We pr...

---

### 13. Beyond Single-Source Cognitive Taskonomy:Multi-Source Task Relations through fMRI Transfer Learning

**Authors:** Junfeng Xia, Wendu Li, Mengjiao Zhang, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26279v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26279v1)

**Summary:** Cognitive tasks are organized by shared and specialized neural processes. Masked fMRI reconstruction provides a common self-supervised objective for quantifying transfer relations among task states, but existing reconstruction-based taskonomies mainly study one-to-one transfer from a single source task to a target. Here, we extend an fMRI cognitive taskonomy from single-source to multi-source transfer across 23 Human Connectome Project task states and use Boolean Integer Programming (BIP) to ana...

---

### 14. Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization

**Authors:** Lucas A. T. X. Carneiro, Armand D. Jiofack, Fernando F. Ferreira

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25874v1)

**Summary:** Polychronous Neuronal Groups (PNGs) reproducible, time-locked spatiotemporal firing cascades stabilised by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays provide a combinatorially rich substrate for neural computation whose structural determinants remain poorly understood. We simulate a recurrent network of N=1000 Izhikevich neurons over ten hours of biological time and identify 1545 unique PNGs via an offline event-driven detection algorithm. A parametric Watts-Strogat...

---

### 15. Weight geometry governs functional memory in complex systems

**Authors:** Elkaïoum M. Moutuou, Habib Benali

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25826v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25826v1)

**Summary:** Complex systems, from gene regulatory networks to neural circuits and transportation infrastructures, exhibit rich functional behaviour that topology alone does not capture. Here we show that functional memory exhibits a universal organisational regularity: in every biological, ecological, social, and technological domain studied, real interaction strengths organise memory at greater hierarchical depth than random weight assignment on the same topology, across thirty-four networks spanning sever...

---

### 16. Meta-learning as a principle for human-like visual representations

**Authors:** Can Demircan, Marcel Binz, Alireza Modirshanechi, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.28399v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28399v1)

**Summary:** The structure of human visual representations underpins our capacity for adaptive behaviour. While pretrained neural networks model human visual representations with unprecedented success, a large discrepancy remains. We propose one reason: these networks optimise a single fixed objective, whereas human representations must support open-ended tasks. We hypothesise this flexibility arises from meta-learning (learning to learn), a pressure shaping representations to acquire new tasks from few obse...

---

### 17. A pilot study examining transcranial photobiomodulation therapy intervention in college students with insomnia

**Authors:** Jiangshan He, Lianghua Zhang, Dan Liang, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24668v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24668v1)

**Summary:** College students commonly report insufficient sleep and poor sleep quality, with ~30% meeting insomnia criteria, posing significant threats to their physical growth, cognitive development, and overall well-being, as well as imposing a substantial economic burden on society [1]. The hyperarousal model of insomnia [2] emphasizes that hyperarousal across cognitive, emotional, and physiological domains mutually reinforces one another. Neuroimaging studies have further identified prefrontal hypoactiv...

---

### 18. EEG Interpretation Across Chant Listening: A Single-Subject Pilot Investigation Using Spectral and Functional Connectivity Analysis

**Authors:** Prerna Singh, Aishwarya Ghosh, Neelam Sinha, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24406v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24406v1)

**Summary:** This technical report presents an EEG-based investigation of neural activity across five auditory conditions: Resting State (RS), Shiv Tandav Stotra (STS), Mahasudarshan Mantra (MM), Aum Chant, and Tanpura Listening. EEG recordings acquired from a healthy 5-year-old participant were analyzed using spectral power estimation and functional connectivity measures based on the weighted Phase Lag Index (wPLI). Spectral analysis revealed condition-specific modulation of neural oscillatory activity, wit...

---

### 19. Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders

**Authors:** Xavier Vasques, Paul Barbaste, Olivier Oullier

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24394v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24394v1)

**Summary:** Electroencephalography (EEG) is the dominant non-invasive modality for brain-computer interfaces (BCIs), yet reliable decoding of motor imagery is hampered by inter- and intra-individual variability. A recurring claim is that one decoding pipeline, most often a spatial or Riemannian method, is broadly preferable. We test the weakest version of that claim under the most favourable conditions. Using the Mother of All BCI Benchmarks (MOABB) framework, we evaluated 1,056 decoding configurations (fea...

---

### 20. Graph-based analysis of inflammatory profiles in New Onset Refractory Status Epilepticus (NORSE)

**Authors:** Linon Denis, Martin Guillemaud, Vincent Navarro, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24351v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24351v1)

**Summary:** Background and Objectives: Cryptogenic new-onset refractory status epilepticus (cNORSE) represents one of the most severe forms of status epilepticus, occurring in patients without prior neurological disease, and remaining of unknown aetiology despite extensive diagnostic evaluation. Emerging evidence supports a role for immune dysregulation in cNORSE; however, marked heterogeneity in inflammatory signatures has been reported, complicating the selection of targeted immunotherapies. Therefore, a ...

---

### 21. The Morality Game: An online multiplayer platform to standardize, expedite, and expand research on cooperation

**Authors:** Gregory N. Stanley, Alan Yang, Liam Tsimhoni, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24037v1)

**Summary:** This paper presents the Morality Game, a platform designed to standardize and accelerate research on cooperation and morality through game theory-based experiments. The Morality Game functions as a video game for science, a hub for economic game research, an open-access data repository, and a tool for expediting the research process. It allows researchers to launch customized online multiplayer experiments with zero coding, using game trees to simulate moral dilemmas. The platform automates part...

---

### 22. Identifying structural design principles shaping the computational abilities of recurrent neural networks

**Authors:** Tom Talpir, Elad Schneidman

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23874v1)

**Summary:** Understanding how the architecture of neural networks shapes the computations they carry is a central challenge in neuroscience and machine learning. While specific circuit architectures have been linked to particular network computations and theoretical bounds on expressivity of broad classes of networks have been found, we are still missing general principles connecting the structure of finite networks to their computational capabilities. Here, we characterize the computational abilities of re...

---

### 23. The adaptive nature of confirmation bias

**Authors:** Dorje C. Brody, Karl J. Friston, Bernhard K. Meister, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23325v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23325v1)

**Summary:** In this paper, the phenomenon generally classified as confirmation bias is formulated on the space of square-root probabilities (or equivalently, using the structures of quantum probability). In this framework, observations are modelled by matrices, rather than random variables on a probability space. In the problem of binary hypothesis testing, an optimal evidence choice minimises the expected error probability. We show that the resulting optimal choice of evidence leads to a confirmation bias,...

---

### 24. Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg

**Authors:** Helio V. Cabral, Giacomo Valli, Roberto Zanotti, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23066v1)

**Summary:** Common synaptic input is considered a fundamental principle of motor neuron control and represents the dominant component of the neural drive transmitted from the motor neurons to muscle. Recent advances in High-Density surface Electromyography (HDsEMG) and motor unit (MU) decomposition algorithms have enabled the concurrent identification of increasingly large populations of MUs and substantially expanded the possibility of estimating common synaptic input from MU spike trains, making this appr...

---

### 25. SPIDER -- Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings

**Authors:** Yisi S. Zhang, Daniel Y. Takahashi

**Published:** 2026-06-21

🔗 [Paper](http://arxiv.org/abs/2606.22695v1) | 📄 [PDF](https://arxiv.org/pdf/2606.22695v1)

**Summary:** Mapping the directed flow of information between brain regions -- their effective connectivity -- is central to understanding brain function, yet large-scale recordings sample only a fraction of the brain at a time: sessions, animals, and laboratories cover different, partially overlapping regions, usually without a shared temporal reference. Established directed-connectivity methods (Granger causality, dynamic causal modeling, partial directed coherence, PDC) require all regions to be recorded ...

---

### 26. DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics

**Authors:** Jayadratha Gayen, Bradly Alicea

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21940v1)

**Summary:** Understanding how a nervous system wires itself from birth to adulthood is a fundamental challenge in developmental neuroscience. We present DevoTG, a temporal graph framework that applies Temporal Graph Neural Networks (TGNs) to two complementary representations of C. elegans neural development: a Continuous-Time Dynamic Graph (CTDG) of cell division events derived from cell lineage data, and a Discrete-Time Dynamic Graph (DTDG) of the developing synaptic connectome spanning eight reconstructed...

---

### 27. Dynamic Computerized Tumbling-E Testing for Temporal Reliability of Human Sequential Perceptual Decisions

**Authors:** Avneek Sandhu, Bin Hu

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21818v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21818v1)

**Summary:** OBJECTIVES: Visual acuity and tumbling-E tasks are often treated as static threshold measures, yet sequential perceptual decisions unfold over time. A computerized tumbling-E task preserves response latency, timeouts, and stimulus-size adaptation, creating a temporal reliability dataset rather than only a chart-line score. This matters for human-AI comparison because the Temporal Hallucination Index (THI) shows how static accuracy can obscure delays, drift, persistence, and unstable convergence....

---

### 28. Mostly-monocular responses and other visual functions in a multiscale network model of Macaque V1

**Authors:** Zhuo-Cheng Xiao, Kevin K. Lin, Lai-Sang Young

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21785v2) | 📄 [PDF](https://arxiv.org/pdf/2606.21785v2)

**Summary:** Visual signals from the two eyes merge gradually as they pass through the primary visual cortex (V1). Here we use a computational model of Macaque V1 to study the first stage of this integration along the magnocellular pathway, in layer 4C$α$, aiming to infer neuroanatomical origins of binocular response. It is known that neurons in layer 4C$α$ are predominantly monocular, though some do exhibit varying degrees of binocularity. We find (1) the emergence of narrow binocular strips along borders o...

---

### 29. Delay coordinates synchronization and induces abrupt transition in excitable networks

**Authors:** Bruno R. R. Boaretto, Kalel L. Rossi, Lyle E. Muller, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21703v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21703v1)

**Summary:** Neuronal communication is inherently time-delayed, due to the finite speed of signal propagation. Although often considered challenging or disruptive, such time delays can also endow neural circuits with useful capabilities. Here, we show that delays in excitatory connections between excitable neurons coordinate their synchronization patterns by creating self-sustained oscillations that may be out-of-phase or in-phase. The emergence of these oscillations leads to an abrupt, explosive, transition...

---

### 30. Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks

**Authors:** Stephen Coombes, Rüdiger Thul, Stefan Ruschel, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21508v1)

**Summary:** We develop a theory of phase-locked activity in delayed spiking networks using the Haken Lighthouse model as an analytically tractable event-based description of neural dynamics. For networks with fixed delays, we derive self-consistency conditions for phase-locked states and an associated linear stability theory formulated directly in terms of spike-time perturbations. The framework is illustrated for a delayed autapse, a reciprocally coupled two-cell network, and spatially structured rings wit...

---

### 31. Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity

**Authors:** Ch. Meessen

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21432v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21432v1)

**Summary:** We construct a minimal but biologically plausible spiking neuron model operating in discrete time, combining multiplicative spike-timing-dependent plasticity (WSTDP), divisive normalization of synaptic integration, homeostatic threshold adaptation, and a one-step refractory period. We show that this normalization admits a biologically plausible dendritic implementation in which each binary junction operates using only locally available information.   Assembling excitatory-inhibitory pairs of suc...

---

### 32. Relational Gaze Transitions During Encoding Predict Episodic Recall of Naturalistic Scenes

**Authors:** Hugo Rydel, Alex Kafkas

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20844v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20844v1)

**Summary:** Remembering a visual scene requires organizing distinct details into a cohesive event. This study investigates whether relation-guided gaze transitions provide a behavioural marker of this cognitive organization during episodic encoding and retrieval. By applying scene graph annotations to eye-tracking data, we measured whether gaze moved between objects that were meaningfully related within complex scenes. This approach allowed us to quantify relational scanning within naturalistic environments...

---

### 33. Synchronization modes in bipartite oscillator networks

**Authors:** Pau Pomés, Bastian Pietras, Ernest Montbrió

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20345v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20345v1)

**Summary:** Collective oscillations in neuronal systems often arise from interactions between excitatory and inhibitory populations rather than from recurrent coupling within a single ensemble. Motivated by the coexistence of strongly and partially synchronized regimes in such systems, we study the Kuramoto Sakaguchi model on a bipartite network. Despite its minimal structure, the model exhibits rich collective dynamics, including both continuous and discontinuous transitions from full synchrony to partial ...

---

### 34. Quadratic Forms for Measuring Geometric Trees in 3-dimensional Space

**Authors:** Yossi Bokor Bleile, Emanuele Cortinovis, Herbert Edelsbrunner, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20096v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20096v1)

**Summary:** Tree-like structures appear in many areas of science, and their shapes can help understand the underlying processes they drive or that give rise to them.   By thinking of these structures as geometric graphs in $\mathbb{R}^3$, we gain access to tools from computational geometry and topology to study them.   In this paper, we adopt the theory of quadratic forms to measure the directional spread of geometric graphs, and we introduce the hexplot model -- equipped with a metric derived from the Fish...

---

### 35. Robust probabilistic measurement of structural-functional module consistency in infant brain development

**Authors:** Lingbin Bian, Feihong Liu, Qian Wang, et al.

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.19739v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19739v1)

**Summary:** Brain network is commonly divided into modules for analyzing their functionally segregated roles for group-level analysis in neuroimaging studies. Here, we introduce stochastic modules within brain networks for a robust probabilistic measurement of structural-functional module consistency (SFMC) in a group of subjects. Specifically, a stochastic module can be regarded as the chance of a brain region across subjects potentially being assigned to a group-level sub-network, characterized as an assi...

---

### 36. Retrieval-Based Brain Decoding by Alignment, not Complexity

**Authors:** Matteo Ciferri, Matteo Ferrante, Nicola Toschi

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.19081v1) | 📄 [PDF](https://arxiv.org/pdf/2606.19081v1)

**Summary:** A prominent theory in cognitive science suggests that concepts in the brain are organized as high-dimensional vectors, with semantic meaning captured by directions and relative angles in this space. Brain decoding is the effort of reconstructing or retrieving stimuli (or their representations) from neural activity and involves finding a function that approximates how the brain represents concepts. This motivates the investigation of contrastive objectives as biologically plausible candidates to ...

---

### 37. Dissecting emerging slow rhythms in delay-coupled neural oscillators

**Authors:** Xinxin Qie, Matteo Martin, Shenquan Liu, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.20733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20733v1)

**Summary:** Synaptic transmission delays are ubiquitous in neural circuits and can alter the dynamical repertoire of coupled oscillators quantitatively and qualitatively. Here, we demonstrate that delayed coupling in inhibitory networks introduces an effective slow-fast structure in the phase-difference dynamics, generating low-frequency components that are not due to intrinsic cellular properties, and we show that this behavior is not specific to a particular model structure. The origin of this generic phe...

---

### 38. Can neurons speak? Semantic narration of vision at single-cell resolution

**Authors:** Arnau Marin-Llobet, Richard Hakim, Sara Matias, et al.

**Published:** 2026-06-17

🔗 [Paper](http://arxiv.org/abs/2606.18667v1) | 📄 [PDF](https://arxiv.org/pdf/2606.18667v1)

**Summary:** Identifying what individual neurons encode in higher-order visual cortex is an open problem. Responses resist intuitive parameterization, and the deep-network embeddings used in their place are black boxes. Here, we introduce NEURRATOR, a framework that decodes spiking activity into free-form natural-language narration of the viewed scene at single-neuron resolution. A learned encoder maps spike trains from arbitrary subsets of simultaneously-recorded neurons into the patch-embedding space of a ...

---

### 39. Separating wiring-specific from statistical control of dynamics in a complete connectome

**Authors:** Stavros Therianos

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17745v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17745v1)

**Summary:** Electron-microscopy reconstruction now yields complete synaptic wiring diagrams, or connectomes, of entire small brains, including the larval Drosophila, the first insect brain reconstructed in full. How far a wiring diagram alone fixes a circuit's activity, as opposed to the finer physiological detail it does not record, is debated. We run a complete connectome as a fixed, rate-based dynamical operator in which no single-neuron parameter is fitted, so that, at one fixed dynamical regime, the mo...

---

### 40. BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17742v1)

**Summary:** Whole-brain 4D fMRI generation is valuable for modeling functional brain dynamics, yet existing fMRI foundation models mainly target representation learning and downstream prediction rather than conditional predictive generation. We introduce BrainWorld, a structural-prior-conditioned generative model for whole-brain 4D fMRI dynamics. BrainWorld uses sMRI as subject-level anatomical context to guide future fMRI generation, integrating structural information into the denoising process rather than...

---

### 41. Ten Years of the Stochastic Resonance Model of Tinnitus: From Phantom Perception to Adaptive Sensory Optimization

**Authors:** Patrick Krauss, Achim Schilling

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17736v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17736v1)

**Summary:** Subjective tinnitus - the perception of sound in the absence of an external acoustic stimulus - remains one of the most debated phenomena in auditory neuroscience. In 2016, the stochastic resonance (SR) model was introduced as an alternative account of tinnitus-related neuronal hyperactivity, proposing that internally generated neural noise is adaptively upregulated to restore information transmission after hearing loss. Rather than interpreting increased spontaneous activity as maladaptive, the...

---

### 42. Embodiment Shapes Rolling Behavior in a Multimodal Infant Model

**Authors:** Leon Philipp, Francisco M. López, Jochen Triesch

**Published:** 2026-06-16

🔗 [Paper](http://arxiv.org/abs/2606.17456v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17456v1)

**Summary:** Rolling over is one of the earliest milestones in infant motor development, reflecting the emergence of coordinated, whole-body sensorimotor control. Here, we conduct a computational study of infant rolling using MIMo, a virtual infant embodiment equipped with proprioception and vestibular sensation. MIMo learns supine-to-prone rolls with reinforcement learning. Interestingly, the learned behaviors capture developmental trends and coordination patterns consistent with those reported in real infa...

---

### 43. Adaptive inference and function vectors in deep transformers

**Authors:** Ravin Raj, Gautam Reddy

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16694v1)

**Summary:** Transformers are widely used as a general-purpose substrate for learning complex correlations between a large collection of coupled variables, but their internal mechanisms have remained mysterious. We introduce a theory of a deep transformer as a mean-field interacting system that implements distributed inference, subject to constraints on communication, locality and depth. We show that such a system can exploit internal state representations ('function vectors') to infer a latent context varia...

---

### 44. Learning Hybrid Biophysical Neuron Models with Neural ODEs

**Authors:** Jonas Beck, Michael Deistler, Dóra Viktória Molnár, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16693v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16693v1)

**Summary:** Biophysical neuron models link measurements of neural activity to underlying cellular mechanisms. Yet, a central challenge is that the kinetics of many ion channels are poorly characterized, and practical simplifications -- omitting channels or reducing morphological detail -- introduce systematic gaps between model and biology. Bridging these gaps requires approaches that can flexibly discover unmodeled dynamics while preserving mechanistic interpretability. Here, we introduce a hybrid modeling...

---

### 45. Infant Spontaneous Movement Noise Improves Exploration in Deep RL

**Authors:** Francisco M. López, Markus R. Ernst, Francisco Cruz, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16590v2) | 📄 [PDF](https://arxiv.org/pdf/2606.16590v2)

**Summary:** Exploration in deep reinforcement learning (RL) is commonly implemented as temporally uncorrelated white noise. However, recent works show that temporally correlated colored noise can improve exploration efficiency by producing smooth trajectories with better coverage of the state space. We inquire whether action noise inspired by infant spontaneous movements can also improve exploration in deep RL. We find that the power spectral densities of babies' end-effector velocities follow a colored noi...

---

### 46. Sex-based Network-Specific Differences in Connectomes: A Krakencoder-Based Analysis

**Authors:** Vibhashree S H, Debanjali Bhattacharya, Vamshi Krishna Kancharla, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16294v1)

**Summary:** This study examines how deficiencies in one brain connectome modality propagate to the other, using the Krakencoder as a simulation framework. Structural and functional connectomes from 702 healthy participants in the Human Connectome Project were analyzed, with the impact of each of the Yeo-7 functional networks assessed separately. Seven scenarios were considered, each involving the removal of a single network while the remaining networks were preserved. The resulting perturbations in cross-mo...

---

### 47. EEGDash: An open-source platform for machine learning on public neurophysiological data

**Authors:** Bruno Aristimunha, Aviv Dotan, Pierre Guetschel, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.16041v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16041v1)

**Summary:** Public neurophysiological datasets are increasingly accessible but remain hard to reuse: turning one into a trained model still takes thousands of lines of code for download, loading, format repair, windowing, and evaluation, and a dataset that meets metadata standards can still fail to load. EEG-Dash is a software resource that catalogues 791 publicly archived recordings (39,778 participants, over 86,051 hours) spanning electroencephalography (EEG), magnetoencephalography (MEG), intracranial EE...

---

### 48. Task-guided cross-subject latent alignment: a multi-encoder-decoder VAE

**Authors:** Angeliki Papathanasiou, Jascha Achterberg, Thomas E. Nichols, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15989v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15989v1)

**Summary:** Aligning neural activity across subjects offers the promise of discovering shared computational principles and generalizable decoders. However, traditional alignment methods require shared stimuli across subjects, a constraint that limits applicability to naturalistic paradigms with limited or non-overlapping data. We introduce a Multi-Encoder-Decoder Variational Autoencoder (MED-VAE) that achieves cross-subject alignment without shared stimuli by anchoring representations to a common scaffold p...

---

### 49. Intrinsic Computational Functionalism and Simulated Consciousness

**Authors:** Ryota Kanai, Shuqin Ma

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15348v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15348v1)

**Summary:** A common objection to artificial or simulated consciousness is that a simulated brain is no more conscious than simulated water is wet. We address this from the perspective of Intrinsic Computational Functionalism (ICF): if consciousness is computationally constituted, it depends not on externally imposed descriptions but on the computational structures a system physically realizes in virtue of its own causal-dynamical organization. In previous work we developed Canonical Functionalism as a math...

---

### 50. OpTI-Mouse: Optimization for Targeted Temporal Interference Stimulation in the Mouse Brain

**Authors:** Jingsheng Tang, Zhengkang Zhou, Yingyue Xin, et al.

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15192v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15192v1)

**Summary:** Temporal Interference (TI) stimulation enables deep brain targeting, yet precise optimization tools for mouse models remain limited. We developed a computational optimization tool integrating mouse head modeling with the optimization algorithm to optimize stimulation strategies for predefined target regions. By balancing target intensity and spatial focality, the optimized strategy significantly outperformed empirical baselines. For the CA3-CA1 target, it achieved a 7-fold intensity increase (10...

---

## stat.ML

**50 papers**

### 1. Random Reshuffling Dominates Stochastic Gradient Descent

**Authors:** Zijian Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.32005v1) | 📄 [PDF](https://arxiv.org/pdf/2606.32005v1)

**Summary:** Stochastic Gradient Descent ($\textsf{SGD}$) is one of the most classical optimization algorithms with favorable theoretical guarantees, yet the practical implementation of $\textsf{SGD}$ differs subtly from its well-known form and is often referred to as Shuffling Stochastic Gradient Descent ($\textsf{Shuffling SGD}$). A particularly popular strategy in $\textsf{Shuffling SGD}$ is Random Reshuffling ($\textsf{RR}$), which has achieved great empirical success across numerous experiments. Despite...

---

### 2. Signed-Permutation Coordinate Transport for RMSNorm Transformers

**Authors:** John Sweeney

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31963v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31963v1)

**Summary:** Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only...

---

### 3. Accelerating Conformal Prediction via Approximate Leave-One-Out

**Authors:** Jiachen Cong, Jingbo Liu

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31915v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31915v1)

**Summary:** While conformal prediction provides a general framework for uncertainty quantification in predictive inference, its application is often limited by computational cost. Recent methods, including Jackknife+ and Jackknife-minmax, achieve faster computation by trading a slight loss of efficiency relative to full conformal prediction, but still requires computing leave-one-out refits for all observations. In this paper, we further accelerate conformal prediction by incorporating approximate leave-one...

---

### 4. Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models

**Authors:** Keivan Faghih Niresi, Alice Cicirello, Olga Fink

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31804v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31804v1)

**Summary:** Accurate energy demand forecasting is essential for the reliable operation and planning of modern sustainable energy systems. Spatial-temporal graph neural networks (STGNNs) have recently achieved strong performance in point forecasting by jointly modeling temporal dynamics and relational dependencies across interconnected energy nodes. However, in real-world energy systems, accurate point forecasts alone are insufficient, as operators also require reliable uncertainty estimates to support risk-...

---

### 5. Policy Optimization Achieves Data-Dependent Regret Bounds in MDPs with Unknown Transitions

**Authors:** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31769v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31769v1)

**Summary:** We study policy optimization for online episodic tabular Markov decision processes with unknown transition kernels, aiming for best-of-both-worlds guarantees together with data-dependent regret bounds. Recent work (Dann et al., 2023; Li et al., 2026) has shown that policy optimization can adapt to both adversarial and stochastic losses with first-order, second-order, and path-length bounds, but only under known transitions, leaving open whether such data-dependent guarantees are achievable by po...

---

### 6. On Optimal Data Splitting for Split Conformal Prediction

**Authors:** Sayan Das, Bahram Yaghooti, Todd A. Kuffner, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31600v1)

**Summary:** Conformal prediction and its variants, including the split conformal prediction, provide a distribution-free framework for uncertainty quantification by constructing prediction intervals or sets with finite-sample coverage guarantees. The statistical efficiency of these intervals depends critically on how the data are split into training and calibration samples. Despite its practical importance, a principled characterization of the training-calibration split that minimizes prediction interval le...

---

### 7. On the Convergence of Self-Improving Online LLM Alignment

**Authors:** Xudong Wu, Pangpang Liu, Vaneet Aggarwal, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31524v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31524v1)

**Summary:** The Self-Improving Alignment (SAIL) algorithm addresses distribution shift by reducing a bilevel formulation of the problem to an efficient, single-level method. Empirically, SAIL has demonstrated strong performance on this task. However, a formal analysis of its convergence properties has been lacking. We identify a key theoretical challenge: the standard SAIL objective function is not guaranteed to be strongly concave due to unfavorable properties of its Hessian. To address this limitation, we...

---

### 8. Contextual Slate GLM Bandits with Limited Adaptivity

**Authors:** Tanmay Goyal, Sukruta Prakash Midigeshi, Gaurav Sinha

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31449v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31449v1)

**Summary:** We investigate the contextual slate bandit problem with generalized linear rewards under limited adaptivity. At each round, the learner is presented with $N$ sets of items, where each item is represented by a $d$-dimensional feature vector. The learner then constructs a slate by selecting one item per set; the resulting slate yields a scalar reward sampled from a Generalized Linear Model (GLM). We propose algorithms under two limited-adaptivity settings: (a) Batched and (b) Rarely-Switching. For...

---

### 9. Sequential sparse Gaussian process quantile regression

**Authors:** Hugo Nicolas, Olivier Le Maître

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31284v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31284v1)

**Summary:** Quantile regression aims to estimate the conditional quantiles of a response variable from observed data. In a Bayesian setting, Gaussian process quantile regression provides uncertainty quantification but faces significant computational challenges due to the nonconjugacy of the asymmetric Laplace likelihood and the cost of posterior inference. We develop a sparse Gaussian process framework in which the quantile function is represented through a reduced set of inducing variables and posterior in...

---

### 10. MNAR-$k$-means: A $k$-means Clustering for Data Missing Not at Random with Magnitude-Decaying Probability

**Authors:** Xin Guan

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31253v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31253v1)

**Summary:** The classical $k$-means clustering, based on distances computed from all data features, cannot be directly applied to incomplete data with missing values. A natural extension of $k$-means to missing data is to involve only the observed positions in clustering, which is equivalent to imputing missing values by corresponding cluster means. However, for data missing not at random (MNAR), since missingness is related to data values, such a mean-imputation-based method may lead to the distortion of e...

---

### 11. Learning Gaussian Graphical Models from a Glauber Trajectory Without Mixing

**Authors:** Eric Shen, Tony Wu, Mahbod Majid, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31230v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31230v1)

**Summary:** We study the task of learning the structure of a $d$-sparse Gaussian graphical model on $n$ variables from a single trajectory of Glauber dynamics. Beyond algorithmic considerations, many applications present temporally correlated observations rather than i.i.d.\ samples. In the classical i.i.d.\ setting, under comparably general sparsity and minimum edge-strength assumptions, sublinear-in-$n$ sample guarantees are known, but achieving them in polynomial-time remains open. Motivated in part by t...

---

### 12. Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction?

**Authors:** Davy Guan, Lu Zhang, Asiri Wijesinghe, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31126v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31126v1)

**Summary:** Predicting biomolecular properties from limited labeled data is a central bottleneck in protein engineering and small-molecule design. As strong pretrained encoders now supply rich fixed-length representations, the difficulty has shifted from representation learning to building a data-efficient predictor for the few-shot regime. Tabular foundation models such as TabPFN3 and TabICL are unlikely candidates for this role: they are in-context learners pretrained on synthetic tables drawn from random...

---

### 13. Dynamic Gaussian Processes and the Vanilla-SPDE Exchange

**Authors:** Rui-Yang Zhang, Lachlan Astfalck, Edward Cripps, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31063v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31063v1)

**Summary:** Gaussian process inference is often limited by cubic computational costs, a challenge that becomes more pronounced in spatio-temporal settings where posterior inference is required over dense grids. While state-space SPDE formulations enable linear complexity in time, exact inference remains cubic in space and deteriorates further when observation locations are disjoint from the prediction locations, which inflates the number of considered spatial points. To address this, we propose the Vanilla-...

---

### 14. Multistage Defer Trees for Hybrid Interpretability: If at First You Can't Succeed, Tree Again

**Authors:** Zakk Heile, Hayden McTavish, Margo Seltzer, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.30995v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30995v1)

**Summary:** Recent work has shown that well-optimized individual decision trees can match complex black box models in some settings, primarily in noisy domains. For the remaining settings, however, complex ensembled compositions of trees often achieve higher accuracy at the cost of interpretability, leaving practitioners with difficult modeling decisions along an accuracy-interpretability tradeoff. Ideally, we would like to classify as much of the data as possible with one or a small number of trees, achiev...

---

### 15. Exponential-Family Tensor Completion via Nonconvex Dual Total-Variation Regularization

**Authors:** Wenfei Cao, Yang Chen, Qibin Zhao, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30958v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30958v1)

**Summary:** With the emergence of various tensor data, tensor completion from partial measurements has attracted widespread attention in data science and signal processing. Total Variation (TV) has been widely used as an effective regularization technique for tensor completion; however, theoretical studies on TV regularization in this context remain limited. In this work, we present a rigorous theoretical analysis of TV regularization for tensor completion. Specifically, we consider tensor completion under ...

---

### 16. SGD at the Edge of Stability: Stochastic Stabilization with Large Learning Rates

**Authors:** Konstantinos Emmanouilidis, Lachlan MacDonald, Salma Tarmoun, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30930v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30930v1)

**Summary:** Modern deep learning has been shown to operate at the edge of stability, routinely using learning rates far larger than those justified by classical optimization theory. Most prior analyses of the edge of stability phenomenon focus on deterministic gradient descent, leaving the stochastic setting largely unexplored. In this work, we provide sharp convergence guarantees for Stochastic Gradient Descent (SGD) applied to the multiclass cross-entropy loss, for both linear classifiers and two-layer ne...

---

### 17. Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback

**Authors:** Ved Sriraman, Peihan Liu, Daniel Hsu, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30923v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30923v1)

**Summary:** Imitation Learning is a natural framework for learning in sequential decision-making systems and has emerged as the dominant paradigm through which we understand language model training. A central puzzle is that, while in theory offline IL can be horizon-free and optimal, in practice online methods such as on-policy distillation often outperform offline methods such as supervised fine-tuning. We propose a noisy expert model to explain this gap, in which the learner only has access to a noisy ver...

---

### 18. Dynamic Prediction of Alternating Recurrent Events via Neural Network

**Authors:** Abigail Loe, Susan Murry, Zhenke Wu

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30889v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30889v1)

**Summary:** Alternating recurrent events -- event-times of a specific nature that trigger a secondary refractory period -- occur in a wide-range of fields, including behavioral science, criminal justice, and biostatistics. Analysis of these events requires careful attention to the statistical nuance, including correlated observations and repeated outcomes subject to potential censoring. We develop an online dynamic prediction framework appropriate for predicting subsequent alternating recurrent events, by d...

---

### 19. A Stationary-Distribution Theory for Triplet-Based Plateau Search in Random Forest Ensemble-Size Selection

**Authors:** Andrey A. Dukhovny, Andrey M. Lange

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30837v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30837v1)

**Summary:** The number of trees is a central computational parameter in Random Forests: increasing it reduces finite-ensemble variability but increases training and prediction cost. Plateau-based tuning adapts this parameter through local comparisons of out-of-bag scores at a geometric triplet of tree counts. After the remaining hyperparameters have stabilized, however, the central triplet point need not converge to a deterministic value; instead, it fluctuates around a stationary regime.   This paper devel...

---

### 20. Geometric Dyson Brownian Motions and the Free Log-Normal Limit for a Non-Square Product of Random Matrices

**Authors:** Mufan Li, Jaume de Dios Pont, Mihai Nica, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30831v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30831v1)

**Summary:** We study the squared singular value spectrum of a product of non-square random matrices, a setting that also corresponds to the feature covariance eigenvalues of a deep linear neural network at initialization. We first take a proportional depth-width $d,n$ limit with the number of data points $m$ held fixed, and show that the resulting covariance eigenvalue process satisfies a geometric version of Dyson Brownian motion. We then take a second, sequential mean-field limit corresponding to the scal...

---

### 21. Separation Capacity of Scattering Networks

**Authors:** Konstantin Häberle, Helmut Bölcskei

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30822v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30822v1)

**Summary:** In this paper, we attempt to enhance the theoretical understanding of convolutional neural networks (CNNs) as feature extractors in classification tasks by analyzing them through the lens of Cover's function-counting theory. Specifically, our focus lies on the notion of separation capacity, a combinatorial quantity derived from counting the number of realizable dichotomies (i.e., binary label assignments). Our contributions are threefold. First, we extend Cover's framework by establishing a conc...

---

### 22. Predictable GRPO: A Closed-Form Model of Training Dynamics

**Authors:** Rajat Ghosh, Datta Nimmaturi, Aryan Singhal, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30789v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30789v1)

**Summary:** Group Relative Policy Optimization (GRPO) has become a standard tool for improving the reasoning ability of large language models, yet its training dynamics are still described empirically: reward trajectories are fit with low-parameter functional forms whose constants carry no mechanistic meaning, and hyperparameter choices remain a matter of trial and error.  We develop a first-principles reduced-order model of these dynamics. The reduction has three consequences. First, it subsumes the empiri...

---

### 23. Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models

**Authors:** Subramanyam Sahoo, Aman Chadha, Vinija Jain, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30627v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30627v1)

**Summary:** Conservative offline training is widely advocated as a safe foundation for subsequent online adaptation: if a policy stays close to well-supported behaviour, the argument goes, it is less likely to exploit imperfections in a learned reward model. We challenge this intuition empirically and mechanistically. We train a Qwen3-14B policy under Direct Preference Optimisation (DPO) with three levels of conservatism ($β\in \{β_{\mathrm{lo}}, β_{\mathrm{mid}}, β_{\mathrm{hi}}\}$ derived from empirical l...

---

### 24. Optimization Dynamics Imprint Semantic Specificity in Contrastive Embedding Norms

**Authors:** Ziwei Su, Junyu Ren, Victor Veitch

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30625v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30625v1)

**Summary:** Contrastive embedding models trained with scale-invariant losses are typically paired with distance metrics like cosine similarity, effectively ignoring embedding magnitudes. However, surprisingly, empirical studies reveal that despite this, these "discarded" norms seem to correlate with semantic properties such as concept specificity, token frequency, and human uncertainty. In this work, we provide a formal theoretical framework explaining this phenomenon. By analyzing the optimization dynamics...

---

### 25. The Fundamental Limits of Valid Transport Map Estimation

**Authors:** Sivaraman Balakrishnan

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30574v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30574v1)

**Summary:** Many modern generative modeling methods, including diffusion models, normalizing flows, and flow matching, estimate transport maps or plans between distributions without explicitly targeting an optimal transport (OT) map. In applications like generative modeling, the transport cost itself is irrelevant, and this makes it natural to target maps which are more tractable from either a statistical or computational standpoint. In this short note, we formalize the task of estimating any valid transpor...

---

### 26. Convergence of Continual Learning in Homogeneous Deep Networks

**Authors:** Matan Schliserman, Gon Buzaglo, Itay Evron, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30559v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30559v1)

**Summary:** We characterize weakly regularized continual classification in homogeneous models as sequential projections onto task margin sets. This result generalizes prior analyses restricted to either stationary (single-task) deep models or continual linear models. We show that global convergence generally fails, even for simple models linear in data but nonlinear in parameters. Nevertheless, by leveraging results from nonconvex projection theory, we identify regularity properties of homogeneous deep netw...

---

### 27. ITSPACE: Monotone Gaussian Optimal Transport Updates

**Authors:** Woojoo Na, Jennifer Dy

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30523v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30523v1)

**Summary:** Covariance matrices serve as compact descriptors of feature distributions in many machine-learning pipelines, including domain adaptation and Gaussian embeddings. Under a centered Gaussian approximation, the unregularized Wasserstein-2 optimal-transport (OT) discrepancy admits a closed form on covariances given by the Bures-Wasserstein (BW) objective on the symmetric positive definite (SPD) cone. We propose ITSPACE (Iterative Transport for Stable Proximal Alignment of Covariance Embeddings), a p...

---

### 28. Doubly Robust Adaptive Conformal Inference for Causal Effects Under Temporal Dependence

**Authors:** Andreas Koukorinis, Ricardo Silva

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30500v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30500v1)

**Summary:** We propose doubly robust adaptive conformal inference (DR-ACI), which constructs prediction intervals for doubly robust pseudo-outcomes under temporal dependence.

---

### 29. Factorizable Normalizing Flows for parameter-dependent density morphing

**Authors:** Davide Valsecchi, Mauro Donegà, Rainer Wallny

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30489v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30489v1)

**Summary:** Normalizing Flows excel at modeling a single fixed density, yet many problems across the sciences, such as high energy physics, instead require modeling how that density deforms as a function of continuous parameters: the strength of a physical effect, a calibration constant, or a source of systematic uncertainty. Learning a separate flow for every parameter configuration quickly becomes intractable, since the number of joint settings grows exponentially with the number of parameters. We introdu...

---

### 30. Non-parametric recovery of causal diffusion mechanisms from steady-state observations

**Authors:** Richard Schwank, Mathias Drton

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30467v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30467v1)

**Summary:** We consider sparse multivariate stochastic systems that evolve in continuous time according to a causal mechanism and present methodology to recover the system's time-infinitesimal transition mechanism from mere cross-sectional data. This observational paradigm is motivated by applications such as gene expression analysis, where destructive experimental techniques may only allow recording data once over a cell's lifetime. Precisely, we assume the system follows a time-homogeneous diffusion proce...

---

### 31. Curvature-Weighted Gradient Diversity: A Noise Measure for Geometry-Adaptive SGD Schedules

**Authors:** Muhammad Hamza, Ayush Goel

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30455v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30455v1)

**Summary:** The standard convergence analysis of mini-batch stochastic gradient descent (SGD) models gradient noise using a single variance term that treats all parameter directions equally, ignoring the fact that noise in high-curvature directions has less impact because learning rates are already constrained there. We introduce Curvature-Weighted Gradient Diversity (CWGD), a geometry-aware measure that weights per-sample gradient diversity by the inverse square root of the Hessian, providing a tighter pro...

---

### 32. SGD Provably Prioritizes a Shortcut Spurious Feature in the XOR Model

**Authors:** Tyler LaBonte, Vidya Muthukumar

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30444v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30444v1)

**Summary:** Neural networks are known to be susceptible to over-reliance on spurious correlations. However, the precise mechanism by which models exploit shortcut features is not fully understood, and algorithms to mitigate this behavior rely on as yet unjustified assumptions about the learned representations. In this work, we provide the first end-to-end theoretical characterization of spurious feature learning for two-layer ReLU neural networks trained by online minibatch SGD on the logistic loss. We cons...

---

### 33. A Stochastic--Geometric Theory of Scaling Laws in Grokking

**Authors:** Róisín Luo, Christian Gagné, Jonas Ngnawé, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30388v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30388v1)

**Summary:** Delayed generalization (\ie~grokking) refers to the phenomenon in which a neural network fits its training data early in training but only begins to generalize after a prolonged delay, often through an abrupt transition. Despite extensive empirical study, its underlying mechanism remains poorly understood. In this work, we first theoretically characterize a shell--core topological configuration of the reachable solution space induced by Adam's optimization dynamics with weight-shrinkage regulari...

---

### 34. Extrapolating from Regularised Solutions for Solving Ill-Conditioned Linear Systems in Machine Learning

**Authors:** Disha Hegde, Jon Cockayne, Chris. J. Oates

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30328v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30328v1)

**Summary:** Rapid prototyping of algorithms is a critical step in modern machine learning. Most algorithms exploit linear algebra, creating a need for lightweight numerical routines which -- while potentially sub-optimal for the task at hand -- can be rapidly implemented. For the numerical solution of ill-conditioned linear systems of equations, the standard solution for prototyping is Tikhonov-regularised inversion using a nugget. However, selection of the size of nugget is often difficult, and the use of ...

---

### 35. Highly Data Parallelizable Estimation of the Sliced-Wasserstein Distance Using Cumulative Distribution Functions

**Authors:** Christophe Vauthier, Quentin Mérigot, Anna Korba

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30310v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30310v1)

**Summary:** The Sliced Wasserstein (SW) distance has emerged as a computationally attractive alternative to the Wasserstein distance by leveraging one-dimensional optimal transport along random projections. Standard estimators of the SW distance rely on Monte Carlo averages of one-dimensional Wasserstein distances computed via quantile functions, which require sorting projected samples and access to full datasets. In this work, we introduce a new class of estimators for the Sliced Wasserstein distance based...

---

### 36. When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding

**Authors:** Aaryam Sharma

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30265v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30265v1)

**Summary:** Speculative decoding accelerates language model inference by using a fast drafter to propose candidate tokens that are then verified by a larger target model. Existing theory largely studies the stochastic, distribution-preserving setting, where the goal is to exactly sample from the target distribution. In contrast, many practical systems use greedy decoding, relaxed acceptance rules, or tree-based candidate sets, where success is governed by local ranking and threshold events rather than exact...

---

### 37. Accelerometry-Derived Digital Biomarkers for Cardiometabolic Risk: A Population-Representative Tabular Benchmark with Uncertainty Quantification

**Authors:** Federico Felizzi

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30702v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30702v1)

**Summary:** Structured tabular data dominates clinical medicine, yet existing benchmarks fail to reflect real-world properties like complex survey sampling, demographic oversampling, and subgroup fairness. We introduce the NHANES Accelerometry Cardiometabolic Benchmark, derived from NHANES 2003-2006, comprising 1,381 adults with hip-worn accelerometry, fasting laboratory biomarkers, dietary intake, and anthropometrics. We evaluate three tabular learning methods -- ridge regression, XGBoost, and the foundati...

---

### 38. Notes on generative modeling: flow matching, diffusion, optimal transport and Schr{ö}dinger bridge

**Authors:** Titouan Vayer

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30053v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30053v1)

**Summary:** These notes recapitulate the high level mathematical principles behind different techniques for generative modeling. I show the connections between optimal transport and standard techniques such as Schr{ö}dinger bridge and flow matching.

---

### 39. AdaGrad does not adapt to Hölder-smoothness for composite objectives

**Authors:** Matia Bojovic, Saverio Salzo, Massimiliano Pontil

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29893v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29893v1)

**Summary:** We exhibit a simple deterministic one-dimensional convex composite optimization problem for which AdaGrad scheme does not achieve the classical convergence rate $\mathcal{O}(n^{-(1+ν)/2})$ associated with Hölder-smooth objectives. The example highlights a basic mismatch between classical AdaGrad accumulation and composite optimality. A main insight is that the gradient of the smooth term may not vanish at the optimum, causing AdaGrad to keep reducing its stepsize excessively and converge more sl...

---

### 40. Decision-Value Attribution in Predict-then-Optimize Systems

**Authors:** Konstantinos Ziliaskopoulos, Alexander Vinel, Alice E. Smith

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29878v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29878v1)

**Summary:** Predictive models are increasingly embedded in operational decision-making, yet standard explanation methods typically explain forecasts rather than the decisions those forecasts induce. This distinction is important in predict-then-optimize systems: large forecast changes may leave the optimizer's action unchanged, while small changes can alter the selected decision and its realized value. We propose Decision Value Attribution (DVA), a Shapley-based framework for attributing the value of a fixe...

---

### 41. A Sieve-Accelerated Quadrature Method for Exact Privacy Accounting in the 2020 U.S. Decennial Census

**Authors:** Buxin Su, Weijie Su, Chendi Wang

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29835v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29835v1)

**Summary:** In 2020, the U.S. Census Bureau adopted differential privacy for the Decennial Census by injecting integer-valued Gaussian noise into published census tabulations. Exactly evaluating the privacy guarantees of these data releases would enable the Bureau to determine the absolute minimum noise required to satisfy a given privacy budget, preventing the injection of unnecessary excess noise and thereby substantially enhancing the statistical utility of the data for downstream applications such as fe...

---

### 42. What Drives the Inlier-Memorization Effect? A Theory of Outlier Detection via Early Training Dynamics

**Authors:** Kunwoong Kim, Dongha Kim

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29791v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29791v1)

**Summary:** Outlier detection (OD) aims to identify anomalous instances by learning the underlying structure of normal data (inliers), and is particularly challenging in fully unsupervised settings where no information about anomalies is available during training. Recent advances have leveraged the inlier-memorization (IM) effect, a phenomenon in which deep models memorize inlier patterns earlier than those of outliers, as a powerful signal for distinguishing outliers. However, despite its empirical success...

---

### 43. Testing hypotheses via orthogonalization

**Authors:** Ameer Dharamshi, Runjia Zou, Daniela Witten

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29732v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29732v1)

**Summary:** Classical hypothesis testing frameworks break down in contemporary settings in which null hypotheses are increasingly abstract, the same data are used to both generate and test hypotheses, and minimal assumptions about the underlying data are made. In this work, we propose a new framework for conducting valid hypothesis tests in broad contexts. We propose to add and subtract external noise generated from a symmetric shift-family to our data, $X$, to partition it into two pieces, $X^{(1)}$ and $X...

---

### 44. I-BBS: Coordinate-Free Inference of Latent Sub-Manifolds Using Random Distance Matrix Theory

**Authors:** Igor Halperin

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29675v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29675v1)

**Summary:** Bogomolny, Bohigas and Schmit (BBS) found that the spectrum of the pairwise distance matrix on N points sampled from a smooth d-dimensional manifold encodes a signature of the underlying geometry. We develop I-BBS (Inference-BBS), a coordinate-free method that identifies a low-dimensional latent sub-manifold embedded in a high-dimensional ambient distance matrix alone, without accessing an ambient high-dimensional vector space. It therefore applies even when that space is only partly observable ...

---

### 45. Adjusted Wasserstein distances for bridging empirical and true distributions with applications to MDS

**Authors:** Flor Martinez-Sermeno, Arturo Jaramillo, Johan Van Horebeek

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29665v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29665v1)

**Summary:** This paper examines how metric adjustments to Multidimensional Scaling (MDS) can enhance its effectiveness as a visual tool for pattern recognition. The distance under consideration, referred to as Max-D-SW, is an adjustment of the Max-Sliced Wasserstein distance. In contrast to the original formulation, which optimizes over single unit directions, Max-D-SW aggregates contributions over orthonormal bases. This modification provides a clear numerical advantage in MDS outcomes, particularly when a...

---

### 46. Multi-Source Transfer Learning of Sparse Single-Index Models

**Authors:** Ye Tian

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29658v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29658v1)

**Summary:** Transfer learning leverages knowledge from related source domains to improve learning in a target domain. Recent theoretical advances cover a broad range of regression settings within (generalized) linear models. Despite their diversity, these methods share two common constraints: they assume a known link function or linear structure and require direct access to raw source data. To move beyond these constraints, we propose a source-data-free transfer learning framework based on the single-index ...

---

### 47. Bidirectional Autoregressive Latent Diffusion for Forward and Inverse Magnetohydrodynamics

**Authors:** Alexander Scheinker

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29620v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29620v1)

**Summary:** This work presents a new bidirectional autoregressive latent diffusion approach for predicting the evolution of multiple fields (mass density, pressure, velocity, and magnetic field components) for magnetohydrodynamics. We show that this bidirectional flow can be used as a self-supervised consistency metric for uncertainty and error estimation, which enables the model to estimate test-time uncertainty and error without access to ground truth, by comparing how closely flowing forwards and backwar...

---

### 48. How AI settled the complexity of the oldest SGD algorithm

**Authors:** Michał Dereziński, Xiaoyu Dong

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29593v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29593v1)

**Summary:** In 1937, Stefan Kaczmarz proposed a simple algorithm for solving systems of linear equations. This algorithm turned out to be the earliest known example of stochastic gradient descent, a ubiquitous computing paradigm that drives the training of modern AI models such as ChatGPT and Gemini. Now, those AI models have joined forces to discover the worst-case complexity of the Kaczmarz algorithm. This paper tells the story of how it happened.

---

### 49. Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise

**Authors:** John Sweeney

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29554v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29554v1)

**Summary:** Shuffle order can be a larger source of fine-tuning noise than a memoryless analysis predicts: fixed-clock optimizer memory makes local equal-multiset contrasts first order in the learning rate rather than second order, and the resulting order channel can be large enough for a single seed to flip a close A/B comparison. We isolate this mechanism and derive a fit-free way to size the noise it produces. For a memoryless optimizer, reordering an equal multiset has no first-order endpoint term; the ...

---

### 50. Not All Objectives Are Born Equal: Priority-Constrained Descent for Hierarchical Multi-Objective Optimization

**Authors:** Dara Varam, Mohamed I. Alhajri

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29521v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29521v1)

**Summary:** Deep learning problems rarely involve objectives that are equal in importance. A primary objective defines the goal, whilst secondary objectives, such as sparsity, compression, or robustness constrain the solution. While existing multi-objective methods have proven effective in practice, they have a clear symmetry problem and neglect the inherent objective hierarchy built into these objective spaces. We introduce Priority-Constrained Descent (PCD), a gradient-based optimization framework designe...

---

