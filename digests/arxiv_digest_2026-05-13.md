# arXiv Daily Digest - 2026-05-13

Total papers: 300

---

## cs.AI

**50 papers**

### 1. AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward

**Authors:** Runhui Huang, Jie Wu, Rui Yang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12495v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12495v1)

**Summary:** In this paper, we propose AlphaGRPO, a novel framework that applies Group Relative Policy Optimization (GRPO) to AR-Diffusion Unified Multimodal Models (UMMs) to enhance multimodal generation capabilities without an additional cold-start stage. Our approach unlocks the model's intrinsic potential to perform advanced reasoning tasks: Reasoning Text-to-Image Generation, where the model actively infers implicit user intents, and Self-Reflective Refinement, where it autonomously diagnoses and correc...

---

### 2. Learning, Fast and Slow: Towards LLMs That Adapt Continually

**Authors:** Rishabh Tiwari, Kusha Sareen, Lakshya A Agrawal, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12484v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12484v1)

**Summary:** Large language models (LLMs) are trained for downstream tasks by updating their parameters (e.g., via RL). However, updating parameters forces them to absorb task-specific information, which can result in catastrophic forgetting and loss of plasticity. In contrast, in-context learning with fixed LLM parameters can cheaply and rapidly adapt to task-specific requirements (e.g., prompt optimization), but cannot by itself typically match the performance gains available through updating LLM parameter...

---

### 3. Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training

**Authors:** Yuanda Xu, Hejian Sang, Zhengze Zhou, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12483v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12483v1)

**Summary:** In settings where labeled verifiable training data is the binding constraint, each checked example should be allocated carefully. The standard practice is to use this data directly on the model that will be deployed, for example by running GRPO on the deployment student. We argue that this is often an inefficient allocation because it overlooks a reward-density principle: sparse sequence-level reward should train models where exploration is productive, while dense token-level teacher reward shou...

---

### 4. ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents

**Authors:** Xuhao Hu, Xi Zhang, Haiyang Xu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12481v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12481v1)

**Summary:** Computer Use Agents (CUAs) can act through both atomic GUI actions, such as click and type, and high-level tool calls, such as API-based file operations, but this hybrid action space often leaves them uncertain about when to continue with GUI actions or switch to tools, leading to suboptimal execution paths. This difficulty stems from the scarcity of high-quality interleaved GUI-Tool trajectories, the cost and brittleness of collecting real tool trajectories, and the lack of trajectory-level sup...

---

### 5. OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation

**Authors:** Guohui Zhang, XiaoXiao Ma, Jie Huang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12480v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12480v1)

**Summary:** Recent advances in joint audio-video generation have been remarkable, yet real-world applications demand strong per-modality fidelity, cross-modal alignment, and fine-grained synchronization. Reinforcement Learning (RL) offers a promising paradigm, but its extension to multi-objective and multi-modal joint audio-video generation remains unexplored. Notably, our in-depth analysis first reveals that the primary obstacles to applying RL in this stem from: (i) multi-objective advantages inconsistenc...

---

### 6. Reward Hacking in Rubric-Based Reinforcement Learning

**Authors:** Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12474v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12474v1)

**Summary:** Reinforcement learning with verifiable rewards has enabled strong post-training gains in domains such as math and coding, though many open-ended settings rely on rubric-based rewards. We study reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator. Our framework separates two sources of divergence: verifier failure, where the training verifier credi...

---

### 7. KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference

**Authors:** Alireza Nadali, Patrick Cooper, Ashutosh Trivedi, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12471v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12471v1)

**Summary:** We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks. At each step, the model processes the next chunk conditioned on the accumulated cache, appends the newly produced keys and values, and passes the enlarged cache forward; the same one-step update is applied repeatedly, analogous to foldl in functional programming. Building on the KV cache concatenation primitive introduced for l...

---

### 8. Solve the Loop: Attractor Models for Language and Reasoning

**Authors:** Jacob Fein-Ashley, Paria Rashidinejad

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12466v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12466v1)

**Summary:** Looped Transformers offer a promising alternative to purely feed-forward computation by iteratively refining latent representations, improving language modeling and reasoning. Yet recurrent architectures remain unstable to train, costly to optimize and deploy, and constrained to small, fixed recurrence depths. We introduce Attractor Models, in which a backbone module first proposes output embeddings, then an attractor module refines them by solving for the fixed point, with gradients obtained th...

---

### 9. Towards Affordable Energy: A Gymnasium Environment for Electric Utility Demand-Response Programs

**Authors:** Jose E. Aguilar Escamilla, Lingdong Zhou, Xiangqi Zhu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12462v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12462v1)

**Summary:** Extreme weather and volatile wholesale electricity markets expose residential consumers to catastrophic financial risks, yet demand response at the distribution level remains an underutilized tool for grid flexibility and energy affordability. While a demand-response program can shield consumers by issuing financial credits during high-price periods, optimizing this sequential decision-making process presents a unique challenge for reinforcement learning despite the plentiful offline historical ...

---

### 10. Enabling AI-Native Mobility in 6G: A Real-World Dataset for Handover, Beam Management, and Timing Advance

**Authors:** Mannam Veera Narayana, Rohit Singh, Deepa M. R, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12453v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12453v1)

**Summary:** To address the issues of high interruption time and measurement report overhead under user equipment (UE) mobility especially in high speed 5G use cases the use of AI/ML techniques (AI/ML beam management and mobility procedures) have been proposed. These techniques rely heavily on data that are most often simulated for various scenarios and do not accurately reflect real deployment behavior or user traffic patterns. Therefore, there is an utmost need for realistic datasets under various conditio...

---

### 11. The Algorithmic Caricature: Auditing LLM-Generated Political Discourse Across Crisis Events

**Authors:**  Gunjan, Sidahmed Benabderrahmane, Talal Rahwan

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12452v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12452v1)

**Summary:** Large Language Models (LLMs) can generate fluent political text at scale, raising concerns about synthetic discourse during crises and social conflict. Existing AI-text detection often focuses on sentence-level cues such as perplexity, burstiness, or token irregularities, but these signals may weaken as generative systems improve. We instead adopt a Computational Social Science perspective and ask whether synthetic political discourse behaves like an observed online population. We construct a pa...

---

### 12. A Causal Language Modeling Detour Improves Encoder Continued Pretraining

**Authors:** Rian Touchent, Eric de la Clergerie

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12438v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12438v1)

**Summary:** When adapting an encoder to a new domain, the standard approach is to continue training with Masked Language Modeling (MLM). We show that temporarily switching to Causal Language Modeling (CLM) followed by a short MLM decay improves downstream performance. On biomedical texts with ModernBERT, this CLM detour outperforms MLM baselines trained on identical data and compute across 8 French and 11 English biomedical tasks, by +1.2-2.8pp and +0.3-0.8pp respectively, depending on model size. We invest...

---

### 13. CAAFC: Chronological Actionable Automated Fact-Checker for misinformation / non-factual hallucination detection and correction

**Authors:** Islam Eldifrawi, Shengrui Wang, Amine Trabelsi

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12436v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12436v1)

**Summary:** With the vast amount of content uploaded every hour, along with the AI generated content that can include hallucinations, Automated Fact-Checking (AFC) has become increasingly vital, as it is infeasible for human fact-checkers to manually verify the sheer volume of information generated online. Professional fact-checkers have identified several gaps in existing AFC systems, noting a misalignment between how these systems operate and how fact-checking is performed in practice. In this paper, we i...

---

### 14. Formalize, Don't Optimize: The Heuristic Trap in LLM-Generated Combinatorial Solvers

**Authors:** Haoyu Wang, Yuliang Song, Tao Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12421v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12421v1)

**Summary:** Large Language Models (LLMs) struggle to solve complex combinatorial problems through direct reasoning, so recent neuro-symbolic systems increasingly use them to synthesize executable solvers. A central design question is how the LLM should represent the solver, and whether it should also attempt to optimize search. We introduce CP-SynC-XL, a benchmark of 100 combinatorial problems (4,577 instances), and evaluate three solver-construction paradigms: native algorithmic search (Python), constraint...

---

### 15. Stories in Space: In-Context Learning Trajectories in Conceptual Belief Space

**Authors:** Eric Bigelow, Raphaël Sarfati, Daniel Wurgaft, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12412v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12412v1)

**Summary:** Large Language Models (LLMs) update their behavior in context, which can be viewed as a form of Bayesian inference. However, the structure of the latent hypothesis space over which this inference operates remains unclear. In this work, we propose that LLMs assign beliefs over a low-dimensional geometric space - a conceptual belief space - and that in-context learning corresponds to a trajectory through this space as beliefs are updated over time. Using story understanding as a natural setting fo...

---

### 16. Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling

**Authors:** Eilam Shapira, Moshe Tennenholtz, Roi Reichart

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12411v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12411v1)

**Summary:** AI agents negotiate and transact in natural language with unfamiliar counterparts: a buyer bot facing an unknown seller, or a procurement assistant negotiating with a supplier. In such interactions, the counterpart's LLM, prompts, control logic, and rule-based fallbacks are hidden, while each decision can have monetary consequences. We ask whether an agent can predict an unfamiliar counterpart's next decision from a few interactions. To avoid real-world logging confounds, we study this problem i...

---

### 17. Semantic Reward Collapse and the Preservation of Epistemic Integrity in Adaptive AI Systems

**Authors:** William Parris

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12406v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12406v1)

**Summary:** Recent advances in reinforcement learning from human feedback (RLHF) and preference optimization have substantially improved the usability, coherence, and safety of large language models. However, recurring behaviors such as performative certainty, hallucinated continuity, calibration drift, sycophancy, and suppression of visible uncertainty suggest unresolved structural issues within scalarized preference optimization systems.   We propose Semantic Reward Collapse (SRC): the compression of sema...

---

### 18. OGLS-SD: On-Policy Self-Distillation with Outcome-Guided Logit Steering for LLM Reasoning

**Authors:** Yuxiao Yang, Xiaoyun Wang, Weitong Zhang

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12400v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12400v1)

**Summary:** We study {on-policy self-distillation} (OPSD), where a language model improves its reasoning ability by distilling privileged teacher distributions along its own on-policy trajectories. Despite the performance gains of OPSD, we identify a common but often overlooked mismatch between teacher and student responses: self-reflected teacher responses can be shifted by reflection-induced bias and response templates, leading to miscalibrated token-level supervision. To mitigate this issue, we propose \...

---

### 19. Detecting overfitting in Neural Networks during long-horizon grokking using Random Matrix Theory

**Authors:** Hari K. Prakash, Charles H Martin

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12394v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12394v1)

**Summary:** Training Neural Networks (NNs) without overfitting is difficult; detecting that overfitting is difficult as well. We present a novel Random Matrix Theory method that detects the onset of overfitting in deep learning models without access to train or test data. For each model layer, we randomize each weight matrix element-wise, $\mathbf{W} \to \mathbf{W}_{\mathrm{rand}}$, fit the randomized empirical spectral distribution with a Marchenko-Pastur distribution, and identify large outliers that viol...

---

### 20. SEMIR: Semantic Minor-Induced Representation Learning on Graphs for Visual Segmentation

**Authors:** Luke James Miller, Yugyung Lee

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12389v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12389v1)

**Summary:** Segmenting small and sparse structures in large-scale images is fundamentally constrained by voxel-level, lattice-bound computation and extreme class imbalance -- dense, full-resolution inference scales poorly and forces most pipelines to rely on fixed regionization or downsampling, coupling computational cost to image resolution and attenuating boundary evidence precisely where minority structures are most informative. We introduce SEMIR (Semantic Minor-Induced Representation Learning), a repre...

---

### 21. Scalable Token-Level Hallucination Detection in Large Language Models

**Authors:** Rui Min, Tianyu Pang, Chao Du, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12384v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12384v1)

**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities, but they still frequently produce hallucinations. These hallucinations are difficult to detect in reasoning-intensive tasks, where the content appears coherent but contains errors like logical flaws and unreliable intermediate results. While step-level analysis is commonly used to detect internal hallucinations, it suffers from limited granularity and poor scalability due to its reliance on step segmentation. To address thes...

---

### 22. Trust the Batch, On- or Off-Policy: Adaptive Policy Optimization for RL Post-Training

**Authors:** Rasool Fakoor, Murdock Aubry, Nicholas Stranges, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12380v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12380v1)

**Summary:** Reinforcement learning is structurally harder than supervised learning because the policy changes the data distribution it learns from. The resulting fragility is especially visible in large-model training, where the training and rollout systems differ in numerical precision, sampling, and other implementation details. Existing methods manage this fragility by adding hyper-parameters to the training objective, which makes the algorithm more sensitive to its configuration and requires retuning wh...

---

### 23. Discrete Flow Matching for Offline-to-Online Reinforcement Learning

**Authors:** Fairoz Nower Khan, Nabuat Zaman Nahim, Peizhong Ju

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12379v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12379v1)

**Summary:** Many reinforcement learning (RL) tasks have discrete action spaces, but most generative policy methods based on diffusion and flow matching are designed for continuous control. Meanwhile, generative policies usually rely heavily on offline datasets and offline-to-online RL is itself challenging, as the policy must improve from new interaction without losing useful behavior learned from static data. To address those challenges, we introduce DRIFT, an online fine-tuning method that updates an offl...

---

### 24. ProfiliTable: Profiling-Driven Tabular Data Processing via Agentic Workflows

**Authors:** Wei Liu, Yang Gu, Xi Yan, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12376v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12376v1)

**Summary:** Table processing-including cleaning, transformation, augmentation, and matching-is a foundational yet error-prone stage in real-world data pipelines. While recent LLM-based approaches show promise for automating such tasks, they often struggle in practice due to ambiguous instructions, complex task structures, and the lack of structured feedback, resulting in syntactically correct but semantically flawed code. To address these challenges, we propose ProfiliTable, an autonomous multi-agent framew...

---

### 25. Agent-Based Post-Hoc Correction of Agricultural Yield Forecasts

**Authors:** Matthew Beddows, Aiden Durrant, Georgios Leontidis

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12375v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12375v1)

**Summary:** Accurate crop yield forecasting in commercial soft fruit production is constrained by the data available in typical commercial farm records, which lack the sensor networks, satellite imagery, and high-resolution meteorological inputs that most state-of-the-art approaches assume. We propose a structured LLM agent framework that performs post-hoc correction of existing model predictions, encoding agricultural domain knowledge across tools for phase detection, bias learning, and range validation. E...

---

### 26. Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models

**Authors:** Yanting Miao, Yutao Sun, Dexin Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12374v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12374v1)

**Summary:** Visual latent reasoning lets a multimodal large language model (MLLM) create intermediate visual evidence as continuous tokens, avoiding external tools or image generators. However, existing methods usually follow an output-as-input latent paradigm and yield unstable gains. We identify evidence for a feature-space mismatch that can contribute to this instability: dominant visual-latent models build on pre-norm MLLMs and reuse decoder hidden states as predicted latent inputs, even though these st...

---

### 27. Classifier Context Rot: Monitor Performance Degrades with Context Length

**Authors:** Sam Martin, Fabien Roger

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12366v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12366v1)

**Summary:** Monitoring coding agents for dangerous behavior using language models requires classifying transcripts that often exceed 500K tokens, but prior agent monitoring benchmarks rarely contain transcripts longer than 100K tokens. We show that when used as classifiers, current frontier models fail to notice dangerous actions more often in longer transcripts. In particular, on a dataset that requires identifying when a coding agent takes a subtly dangerous action, Opus 4.6, GPT 5.4, and Gemini 3.1 miss ...

---

### 28. QAP-Router: Tackling Qubit Routing as Dynamic Quadratic Assignment with Reinforcement Learning

**Authors:** Kien X. Nguyen, Ankit Kulshrestha, Ilya Safro, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12365v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12365v1)

**Summary:** Qubit routing is a fundamental problem in quantum compilation, known to be NP-hard. Its dynamic nature makes local routing decisions propagate and compound over time, making global efficient solutions challenging. Existing heuristic methods rely on local rules with limited lookahead, while recent learning-based approaches often treat routing as a generic sequential decision problem without fully exploiting its underlying structure. In this paper, we introduce QAP-Router, framing qubit routing ba...

---

### 29. A Family of Quaternion-Valued Differential Evolution Algorithms for Numerical Function Optimization

**Authors:** Gerardo Altamirano-Gomez, Álvaro Gallardo, Carlos Ignacio Hernández Castellanos

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12362v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12362v1)

**Summary:** The numerical optimization of continuous functions is a fundamental task in many scientific and engineering domains, ranging from mechanical design to training of artificial intelligence models. Among the most effective and widely used algorithms for this purpose is Differential Evolution (DE), known for its simplicity and strong performance. Recent research has shown that adapting AI models to operate over alternative number systems-such as complex numbers, quaternions, and geometric algebras-c...

---

### 30. MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering

**Authors:** Rezarta Islamaj, Robert Leaman, Joey Chan, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12361v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12361v1)

**Summary:** Evaluating large language models (LLMs) in the biomedical domain requires benchmarks that can distinguish reasoning from pattern matching and remain discriminative as model capabilities improve. Existing biomedical question answering (QA) benchmarks are limited in this respect. Multiple-choice formats can allow models to succeed through answer elimination rather than inference, while widely circulated exam-style datasets are increasingly vulnerable to performance saturation and training data con...

---

### 31. $δ$-mem: Efficient Online Memory for Large Language Models

**Authors:** Jingdi Lei, Di Zhang, Junxian Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12357v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12357v1)

**Summary:** Large language models increasingly need to accumulate and reuse historical information in long-term assistants and agent systems. Simply expanding the context window is costly and often fails to ensure effective context utilization. We propose $δ$-mem, a lightweight memory mechanism that augments a frozen full-attention backbone with a compact online state of associative memory. $δ$-mem compresses past information into a fixed-size state matrix updated by delta-rule learning, and uses its readou...

---

### 32. A New Technique for AI Explainability using Feature Association Map

**Authors:** Sayantani Ghosh, Amit Kumar Das, Amlan Chakrabarti

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12350v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12350v1)

**Summary:** Lack of transparency in AI systems poses challenges in critical real-life applications. It is important to be able to explain the decisions of an AI system to ensure trust on the system. Explainable AI (XAI) algorithms play a vital role in achieving this objective. In this paper, we are proposing a new algorithm for Explaining AI systems, FAMeX (Feature Association Map based eXplainability). The proposed algorithm is based on a graph-theoretic formulation of the feature set termed as Feature Ass...

---

### 33. BSO: Safety Alignment Is Density Ratio Matching

**Authors:** Tien-Phat Nguyen, Truong Nguyen, Thin Nguyen, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12339v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12339v1)

**Summary:** Aligning language models for both helpfulness and safety typically requires complex pipelines-separate reward and cost models, online reinforcement learning, and primal-dual updates. Recent direct preference optimization approaches simplify training but incorporate safety through ad-hoc modifications such as multi-stage procedures or heuristic margin terms, lacking a principled derivation. We show that the likelihood ratio of the optimal safe policy admits a closed-form decomposition that reduce...

---

### 34. Manifold Sampling via Entropy Maximization

**Authors:** Cornelius V. Braun, Tilman Burghoff, Marc Toussaint

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12338v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12338v1)

**Summary:** Sampling from constrained distributions has a wide range of applications, including in Bayesian optimization and robotics. Prior work establishes convergence and feasibility guarantees for constrained sampling, but assumes that the feasible set is connected. However, in practice, the feasible set often decomposes into multiple disconnected components, which makes efficient sampling under constraints challenging. In this paper, we propose MAnifold Sampling via Entropy Maximization (MASEM) for sam...

---

### 35. EHR-RAGp: Retrieval-Augmented Prototype-Guided Foundation Model for Electronic Health Records

**Authors:** Saeed Shurrab, Mariam Al-Omari, Dana El Samad, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12335v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12335v1)

**Summary:** Electronic Health Records (EHR) contain rich longitudinal patient information and are widely used in predictive modeling applications. However, effectively leveraging historical data remains challenging due to long trajectories, heterogeneous events, temporal irregularity, and the varying relevance of past clinical context. Existing approaches often rely on fixed windows or uniform aggregation, which can obscure clinically important signals. In this work, we introduce EHR-RAGp, a retrieval-augme...

---

### 36. Reinforcing VLAs in Task-Agnostic World Models

**Authors:** Yucen Wang, Rui Yu, Fengming Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12334v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12334v1)

**Summary:** Post-training Vision-Language-Action (VLA) models via reinforcement learning (RL) in learned world models has emerged as an effective strategy to adapt to new tasks without costly real-world interactions. However, while using imagined trajectories reduces the sample complexity of policy training, existing methods still heavily rely on task-specific data to fine-tune both the world and reward models, fundamentally limiting their scalability to unseen tasks. To overcome this, we argue that world a...

---

### 37. Towards Automated Air Traffic Safety Assessment Around Non-Towered Airports Using Large Language Models

**Authors:** Torsten Darrell, Mahyar Ghazanfari, Jordan Kam, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12332v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12332v1)

**Summary:** We investigate frameworks for post-flight safety analysis at non-towered airports using large language models (LLMs). Non-towered airports rely on the Common Traffic Advisory Frequency (CTAF) for air traffic coordination and experience frequent near mid-air collisions due to the pilot self-announcement communication protocol. We propose a general vision-language model (VLM) approach to analyze the transcribed CTAF radio communications in natural language, METeorological Aerodrome Report (METAR) ...

---

### 38. LISA: Cognitive Arbitration for Signal-Free Autonomous Intersection Management

**Authors:** Abderrahmane Lakas, Mohamed Amine Ferrag, Merouane Debbah

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12321v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12321v1)

**Summary:** Large language models (LLMs) show strong potential for Intelligent Transportation Systems (ITS), particularly in tasks requiring situational reasoning and multi-agent coordination. These capabilities make them well suited for cooperative driving, where rule-based approaches struggle in complex and dynamic traffic environments. Intersection management remains especially challenging due to conflicting right-of-way demands, heterogeneous vehicle priorities, and vehicle-specific kinematic constraint...

---

### 39. Transferable Delay-Aware Reinforcement Learning via Implicit Causal Graph Modeling

**Authors:** Chenran Zhao, Dianxi Shi, Yaowen Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12312v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12312v1)

**Summary:** Random delays weaken the temporal correspondence between actions and subsequent state feedback, making it difficult for agents to identify the true propagation process of action effects. In cross-task scenarios, changes in task objectives and reward formulations further reduce the reusability of previously acquired task knowledge. To address this problem, this paper proposes a transferable delay-aware reinforcement learning method based on implicit causal graph modeling. The proposed method uses...

---

### 40. KAN-CL: Per-Knot Importance Regularization for Continual Learning with Kolmogorov-Arnold Networks

**Authors:** Minjong Cheon

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12306v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12306v1)

**Summary:** Catastrophic forgetting remains the central obstacle in continual learning (CL): parameters shared across tasks interfere with one another, and existing regularization methods such as EWC and SI apply uniform penalties without awareness of which input region a parameter serves. We propose KAN-CL, a continual learning framework that exploits the compact-support spline parameterization of Kolmogorov-Arnold Networks (KANs) to perform importance-weighted anchoring at per-knot granularity. Deployed a...

---

### 41. Executable Agentic Memory for GUI Agent

**Authors:** Zerui Qin, Sheng Yue, Xingyuan Hua, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12294v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12294v1)

**Summary:** Modern GUI agents typically rely on a model-centric and step-wise interaction paradigm, where LLMs must re-interpret the UI and re-decide actions at every screen, which is fragile in long-horizon tasks. In this paper, we propose Executable Agentic Memory (EAM), a structured Knowledge Graph (KG) that shifts GUI planning from free-form generation to a robust retrieval-and-execution process. Our approach includes a sample-efficient memory construction pipeline using state-aware DFS and action-group...

---

### 42. PriorZero: Bridging Language Priors and World Models for Decision Making

**Authors:** Junyu Xiong, Yuan Pu, Jia Tang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12289v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12289v1)

**Summary:** Leveraging the rich world knowledge of Large Language Models (LLMs) to enhance Reinforcement Learning (RL) agents offers a promising path toward general intelligence. However, a fundamental prior-dynamics mismatch hinders existing approaches: static LLM knowledge cannot directly adapt to the complex transition dynamics of long-horizon tasks. Using LLM priors as fixed policies limits exploration diversity, as the prior is blind to environment-specific dynamics; while end-to-end fine-tuning suffer...

---

### 43. TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching

**Authors:** Truong Nguyen, Tien-Phat Nguyen, Linh Ngo Van, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12288v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12288v1)

**Summary:** Direct Preference Optimization (DPO) is a widely used RL-free method for aligning language models from pairwise preferences, but it models preferences over full sequences even though generation is driven by per-token decisions. Existing token-level extensions typically decompose a sequence-level Bradley-Terry objective across timesteps, leaving per-prefix (state-wise) optimality implicit. We study how to recover token-level preference optimality using only standard sequence-level pairwise compar...

---

### 44. Set-Aggregated Genome Embeddings for Microbiome Abundance Prediction

**Authors:** Younhun Kim, Georg K. Gerber, Travis E. Gibson

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12286v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12286v1)

**Summary:** Microbiome functions are encoded within the genes of the community-wide metagenome. A natural question is whether properties of a microbial community can be predicted just from knowing the raw DNA sequences of its members. In this work, we employ set-aggregated genome embeddings (SAGE) to predict community-level abundance profiles, exploiting the few-shot learning capabilities of genomic language models (GLMs). We benchmark this approach to show improved generalization on novel genomes compared ...

---

### 45. Iterative Audit Convergence in LLM-Managed Multi-Agent Systems: A Case Study in Prompt Engineering Quality Assurance

**Authors:** Elias Calboreanu

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12280v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12280v1)

**Summary:** Prompt specifications for multi-agent large language model (LLM) systems carry data contracts and integration logic across many interdependent files but are rarely subjected to structured-inspection rigor. This paper reports a single-system empirical case study of iterative, agent-driven auditing applied to AEGIS (Autonomous Engineering Governance and Intelligence System), a production seven-lane orchestration pipeline whose prompt-specification surface comprises approximately 7150 lines: 6907 a...

---

### 46. NARA: Anchor-Conditioned Relation-Aware Contextualization of Heterogeneous Geoentities

**Authors:** Jina Kim, Gengchen Mai, Lingyi Zhao, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12276v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12276v1)

**Summary:** Geospatial foundation models have primarily focused on raster data such as satellite imagery, where self-supervised learning has been widely studied. Vector geospatial data instead represent the world as discrete geoentities with explicit geometry, semantics, and structured spatial relations, including metric proximity and topological relationships. These relations jointly determine how entities interact within space, yet existing representation learning methods remain fragmented, often restrict...

---

### 47. How Useful Is Cross-Domain Generalization for Training LLM Monitors?

**Authors:** Sam Martin, Fabien Roger

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12265v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12265v1)

**Summary:** Using prompted language models as classifiers enables classification in domains with limited training data, but misses some of the robustness and performance benefits that fine-tuning can bring. We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts. We show that such training partially generalizes to adjacent domains, improving classification performance on tasks that are unseen during training. H...

---

### 48. Reconnecting Fragmented Citation Networks with Semantic Augmentation

**Authors:** Vu Thi Huong, Annika Buchholz, Imene Khebouri, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12263v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12263v1)

**Summary:** Citation graphs are fundamental tools for modeling scientific structure, but are often fragmented due to missing citations of scientifically connected articles. To address this issue, we propose a computationally efficient hybrid framework integrating citation topology with large language model (LLM)-based text similarity. Using 662,369 Web of Science publications in Mathematics and Operations Research & Management Science, we augment the original graph by adding semantic edges from small, disco...

---

### 49. Missingness-MDPs: Bridging the Theory of Missing Data and POMDPs

**Authors:** Joshua Wendland, Markel Zubia, Roman Andriushchenko, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12262v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12262v1)

**Summary:** We introduce missingness-MDPs (miss-MDPs), a novel subclass of partially observable Markov decision processes (POMDPs) that incorporates the theory of missing data. A miss-MDP is a POMDP whose observation function is a missingness function, specifying the probability that individual state features are missing (i.e., unobserved) at a time step. The literature distinguishes three canonical missingness types: missing (1) completely at random (MCAR), (2) at random (MAR), and (3) not at random (MNAR)...

---

### 50. Why Conclusions Diverge from the Same Observations: Formalizing World-Model Non-Identifiability via an Inference

**Authors:** Toru Takahashi

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12255v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12255v1)

**Summary:** When people share the same documents and observations yet reach different conclusions, the disagreement often shifts into a judgment that the other party is cognitively defective, irrational, or acting in bad faith. This paper argues that such divergence is better described as a form of non-identifiability inherent in inference and learning, rather than as a defect of the other party. We organize the phenomenon into two levels: (i) $θ$-level non-identifiability, where conclusions diverge under t...

---

## cs.CL

**50 papers**

### 1. LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues

**Authors:** Di Wu, Zixiang Ji, Asmi Kawatkar, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12493v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12493v1)

**Summary:** Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, state dynamics, workflows, and recurring failure modes. However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience. To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for ...

---

### 2. Task-Adaptive Embedding Refinement via Test-time LLM Guidance

**Authors:** Ariel Gera, Shir Ashury-Tahan, Gal Bloch, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12487v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12487v1)

**Summary:** We explore the effectiveness of an LLM-guided query refinement paradigm for extending the usability of embedding models to challenging zero-shot search and classification tasks. Our approach refines the embedding representation of a user query using feedback from a generative LLM on a small set of documents, enabling embeddings to adapt in real time to the target task. We conduct extensive experiments with state-of-the-art text embedding models across a diverse set of challenging search and clas...

---

### 3. MEME: Multi-entity & Evolving Memory Evaluation

**Authors:** Seokwon Jung, Alexander Rubinstein, Arnas Uselis, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12477v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12477v1)

**Summary:** LLM-based agents increasingly operate in persistent environments where they must store, update, and reason over information across many sessions. While prior benchmarks evaluate only single-entity updates, MEME defines six tasks spanning the full space defined by the multi-entity and evolving axes, including three not scored by prior work: Cascade and Absence (dependency reasoning) and Deletion (post-removal state). Evaluating six memory systems spanning three memory paradigms on 100 controlled ...

---

### 4. Routers Learn the Geometry of Their Experts: Geometric Coupling in Sparse Mixture-of-Experts

**Authors:** Sagi Ahrac, Noya Hochwald, Mor Geva

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12476v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12476v1)

**Summary:** Sparse Mixture-of-Experts (SMoE) models enable scaling language models efficiently, but training them remains challenging, as routing can collapse onto few experts and auxiliary load-balancing losses can reduce specialization. Motivated by these hurdles, we study how routing decisions in SMoEs are formed mechanistically. First, we reveal a geometric coupling between routers and their corresponding experts. For a given token, the router weights for the selected expert and the expert weights proce...

---

### 5. KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference

**Authors:** Alireza Nadali, Patrick Cooper, Ashutosh Trivedi, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12471v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12471v1)

**Summary:** We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks. At each step, the model processes the next chunk conditioned on the accumulated cache, appends the newly produced keys and values, and passes the enlarged cache forward; the same one-step update is applied repeatedly, analogous to foldl in functional programming. Building on the KV cache concatenation primitive introduced for l...

---

### 6. Solve the Loop: Attractor Models for Language and Reasoning

**Authors:** Jacob Fein-Ashley, Paria Rashidinejad

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12466v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12466v1)

**Summary:** Looped Transformers offer a promising alternative to purely feed-forward computation by iteratively refining latent representations, improving language modeling and reasoning. Yet recurrent architectures remain unstable to train, costly to optimize and deploy, and constrained to small, fixed recurrence depths. We introduce Attractor Models, in which a backbone module first proposes output embeddings, then an attractor module refines them by solving for the fixed point, with gradients obtained th...

---

### 7. Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs

**Authors:** Guinan Su, Yanwu Yang, Xueyan Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12460v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12460v1)

**Summary:** The continued improvements in language model capability have unlocked their widespread use as drivers of autonomous agents, for example in coding or computer use applications. However, the core of these systems has not changed much since early instruction-tuned models like ChatGPT. Even advanced AI agents function on message exchange formats, successively exchanging messages with users, systems, with itself (i.e. chain-of-thought) and tools in a single stream of computation. This bottleneck to a...

---

### 8. TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection

**Authors:** Tom Sander, Hongyan Chang, Tomáš Souček, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12456v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12456v1)

**Summary:** We introduce TextSeal, a state-of-the-art watermark for large language models. Building on Gumbel-max sampling, TextSeal introduces dual-key generation to restore output diversity, along with entropy-weighted scoring and multi-region localization for improved detection. It supports serving optimizations such as speculative decoding and multi-token prediction, and does not add any inference overhead. TextSeal strictly dominates baselines like SynthID-text in detection strength and is robust to di...

---

### 9. The Algorithmic Caricature: Auditing LLM-Generated Political Discourse Across Crisis Events

**Authors:**  Gunjan, Sidahmed Benabderrahmane, Talal Rahwan

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12452v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12452v1)

**Summary:** Large Language Models (LLMs) can generate fluent political text at scale, raising concerns about synthetic discourse during crises and social conflict. Existing AI-text detection often focuses on sentence-level cues such as perplexity, burstiness, or token irregularities, but these signals may weaken as generative systems improve. We instead adopt a Computational Social Science perspective and ask whether synthetic political discourse behaves like an observed online population. We construct a pa...

---

### 10. ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models

**Authors:** Chen Li, Xiaoling Hu, Songzhu Zheng, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12446v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12446v1)

**Summary:** Large language models (LLMs) often produce answers with high certainty even when they are incorrect, making reliable confidence estimation essential for deployment in real-world scenarios. Verbalized confidence, where models explicitly state their confidence in natural language, provides a flexible and user-facing uncertainty signal that can be applied even when token logits are unavailable. However, existing verbalized-confidence methods often optimize answer generation and confidence generatio...

---

### 11. A Causal Language Modeling Detour Improves Encoder Continued Pretraining

**Authors:** Rian Touchent, Eric de la Clergerie

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12438v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12438v1)

**Summary:** When adapting an encoder to a new domain, the standard approach is to continue training with Masked Language Modeling (MLM). We show that temporarily switching to Causal Language Modeling (CLM) followed by a short MLM decay improves downstream performance. On biomedical texts with ModernBERT, this CLM detour outperforms MLM baselines trained on identical data and compute across 8 French and 11 English biomedical tasks, by +1.2-2.8pp and +0.3-0.8pp respectively, depending on model size. We invest...

---

### 12. Geometric Factual Recall in Transformers

**Authors:** Shauli Ravfogel, Gilad Yehudai, Joan Bruna, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12426v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12426v1)

**Summary:** How do transformer language models memorize factual associations? A common view casts internal weight matrices as associative memories over pairs of embeddings, requiring parameter counts that scale linearly with the number of facts. We develop a theoretical and empirical account of an alternative, \emph{geometric} form of memorization in which learned embeddings encode relational structure directly, and the MLP plays a qualitatively different role. In a controlled setting where a single-layer t...

---

### 13. Predicting Disagreement with Human Raters in LLM-as-a-Judge Difficulty Assessment without Using Generation-Time Probability Signals

**Authors:** Yo Ehara

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12422v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12422v1)

**Summary:** Automatic generation of educational materials using large language models (LLMs) is becoming increasingly common, but assigning difficulty levels to such materials still requires substantial human effort. LLM-as-a-Judge has therefore attracted attention, yet disagreement with human raters remains a major challenge. We propose a method for predicting which LLM-generated difficulty ratings are likely to disagree with human raters, so that such cases can be sent for re-rating. Unlike prior approach...

---

### 14. ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging

**Authors:** Neha Verma, Nikhil Mehta, Shao-Chuan Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12419v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12419v1)

**Summary:** Despite the rapid advancements in large language model (LLM) development, fine-tuning them for specific tasks often results in the catastrophic forgetting of their general, language-based reasoning abilities. This work investigates and addresses this challenge in the context of the Generative Retrieval (GenRetrieval) task. During GenRetrieval fine-tuning, we find this forgetting occurs rapidly and correlates with the distance between the fine-tuned and original model parameters. Given these obse...

---

### 15. Stories in Space: In-Context Learning Trajectories in Conceptual Belief Space

**Authors:** Eric Bigelow, Raphaël Sarfati, Daniel Wurgaft, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12412v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12412v1)

**Summary:** Large Language Models (LLMs) update their behavior in context, which can be viewed as a form of Bayesian inference. However, the structure of the latent hypothesis space over which this inference operates remains unclear. In this work, we propose that LLMs assign beliefs over a low-dimensional geometric space - a conceptual belief space - and that in-context learning corresponds to a trajectory through this space as beliefs are updated over time. Using story understanding as a natural setting fo...

---

### 16. Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling

**Authors:** Eilam Shapira, Moshe Tennenholtz, Roi Reichart

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12411v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12411v1)

**Summary:** AI agents negotiate and transact in natural language with unfamiliar counterparts: a buyer bot facing an unknown seller, or a procurement assistant negotiating with a supplier. In such interactions, the counterpart's LLM, prompts, control logic, and rule-based fallbacks are hidden, while each decision can have monetary consequences. We ask whether an agent can predict an unfamiliar counterpart's next decision from a few interactions. To avoid real-world logging confounds, we study this problem i...

---

### 17. Question Difficulty Estimation for Large Language Models via Answer Plausibility Scoring

**Authors:** Jamshid Mozafari, Bhawna Piryani, Adam Jatowt

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12398v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12398v1)

**Summary:** Estimating question difficulty is a critical component in evaluating and improving large language models (LLMs) for question answering (QA). Existing approaches often rely on readability formulas, retrieval-based signals, or popularity statistics, which may not fully capture the reasoning challenges posed to modern LLMs. In this paper, we introduce Q-DAPS (Question Difficulty based on Answer Plausibility Scores) method, a novel approach that estimates question difficulty by computing the entropy...

---

### 18. A Comparative Study of Controlled Text Generation Systems Using Level-Playing-Field Evaluation Principles

**Authors:** Michela Lorandi, Anya Belz

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12395v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12395v1)

**Summary:** Background: Many different approaches to controlled text generation (CTG) have been proposed over recent years, but it is difficult to get a clear picture of which approach performs best, because different datasets and evaluation methods are used in each case to assess the control achieved.   Objectives: Our aim in the work reported in this paper is to develop an approach to evaluation that enables us to comparatively evaluate different CTG systems in a manner that is both informative and fair t...

---

### 19. Scalable Token-Level Hallucination Detection in Large Language Models

**Authors:** Rui Min, Tianyu Pang, Chao Du, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12384v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12384v1)

**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities, but they still frequently produce hallucinations. These hallucinations are difficult to detect in reasoning-intensive tasks, where the content appears coherent but contains errors like logical flaws and unreliable intermediate results. While step-level analysis is commonly used to detect internal hallucinations, it suffers from limited granularity and poor scalability due to its reliance on step segmentation. To address thes...

---

### 20. Pretraining Exposure Explains Popularity Judgments in Large Language Models

**Authors:** Jamshid Mozafari, Bhawna Piryani, Adam Jatowt

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12382v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12382v1)

**Summary:** Large language models (LLMs) exhibit systematic preferences for well-known entities, a phenomenon often attributed to popularity bias. However, the extent to which these preferences reflect real-world popularity versus statistical exposure during pretraining remains unclear, largely due to the inaccessibility of most training corpora. We provide the first direct, large-scale analysis of popularity bias grounded in fully observable pretraining data. Leveraging the open OLMo models and their compl...

---

### 21. Context Convergence Improves Answering Inferential Questions

**Authors:** Jamshid Mozafari, Bhawna Piryani, Adam Jatowt

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12370v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12370v1)

**Summary:** While Large Language Models (LLMs) are widely used in open-domain Question Answering (QA), their ability to handle inferential questions-where answers must be derived rather than directly retrieved-remains still underexplored. This study investigates how the structure and quality of passages influence LLM performance on such questions. We focus on convergence, a measure of how effectively sentences (hints) eliminate incorrect answers, as a criterion for constructing passages. Using subsets of th...

---

### 22. MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering

**Authors:** Rezarta Islamaj, Robert Leaman, Joey Chan, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12361v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12361v1)

**Summary:** Evaluating large language models (LLMs) in the biomedical domain requires benchmarks that can distinguish reasoning from pattern matching and remain discriminative as model capabilities improve. Existing biomedical question answering (QA) benchmarks are limited in this respect. Multiple-choice formats can allow models to succeed through answer elimination rather than inference, while widely circulated exam-style datasets are increasingly vulnerable to performance saturation and training data con...

---

### 23. Output Composability of QLoRA PEFT Modules for Plug-and-Play Attribute-Controlled Text Generation

**Authors:** Michela Lorandi, Anya Belz

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12345v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12345v1)

**Summary:** Parameter-efficient fine-tuning (PEFT) techniques offer task-specific fine-tuning at a fraction of the cost of full fine-tuning, but require separate fine-tuning for every new task (combination). In this paper, we explore three ways of generalising beyond single-task training/inference: (i) training on combinations of multiple, related datasets; (ii) at inference, composing the weight matrices of separately trained PEFT modules; and (iii) at inference, composing the outputs of separately trained...

---

### 24. A categorical error sensitivity index (ISEC): A preventive ordinal decision-support measure for irrecoverable errors in manual data entry systems

**Authors:** Ricardo Raúl Palma, Mauro Anibal Benetti, Fabricio Orlando Sanchez Varretti

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12328v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12328v1)

**Summary:** Data entry systems remain structurally vulnerable to categorical misclassifications, particularly in small and medium sized enterprises (SMEs). When nominal categories exhibit semantic or morphological proximity, human machine interaction may produce errors that are irrecoverable ex post. In the absence of automated input controls, manual data entry frequently generates irrecoverable categorical distortions that propagate into Key Performance Indicators (KPIs), thereby misleading managerial deci...

---

### 25. Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering

**Authors:** Rezarta Islamaj, Joey Chan, Robert Leaman, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12313v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12313v1)

**Summary:** Multi-hop question answering (QA) remains a significant challenge in the biomedical domain, requiring systems to integrate information across multiple sources to answer complex questions. To address this problem, the BioCreative IX MedHopQA shared task was designed to benchmark in multi-hop reasoning for large language models (LLMs). We developed a novel dataset of 1,000 challenging QA pairs spanning diseases, genes, and chemicals, with particular emphasis on rare diseases. Each question was con...

---

### 26. GKnow: Measuring the Entanglement of Gender Bias and Factual Gender

**Authors:** Leonor Veloso, Hinrich Schütze

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12299v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12299v1)

**Summary:** Recent works have analyzed the impact of individual components of neural networks on gendered predictions, often with a focus on mitigating gender bias. However, mechanistic interpretations of gender tend to (i) focus on a very specific gender-related task, such as gendered pronoun prediction, or (ii) fail to distinguish between the production of factually gendered outputs (the correct assumption of gender given a word that carries gender as a semantic property) and gender biased outputs (based ...

---

### 27. TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching

**Authors:** Truong Nguyen, Tien-Phat Nguyen, Linh Ngo Van, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12288v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12288v1)

**Summary:** Direct Preference Optimization (DPO) is a widely used RL-free method for aligning language models from pairwise preferences, but it models preferences over full sequences even though generation is driven by per-token decisions. Existing token-level extensions typically decompose a sequence-level Bradley-Terry objective across timesteps, leaving per-prefix (state-wise) optimality implicit. We study how to recover token-level preference optimality using only standard sequence-level pairwise compar...

---

### 28. What makes a word hard to learn? Modeling L1 influence on English vocabulary difficulty

**Authors:** Jonas Mayer Martins, Zhuojing Huang, Aaricia Herygers, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12281v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12281v1)

**Summary:** What makes a word difficult to learn, and how does the difficulty depend on the learner's native language? We computationally model vocabulary difficulty for English learners whose first language is Spanish, German, or Chinese with gradient-boosted models trained on features related to a word's familiarity (e.g., frequency), meaning, surface form, and cross-linguistic transfer. Using Shapley values, we determine the importance of each feature group. Word familiarity is the dominant feature group...

---

### 29. Reconstruction of Personally Identifiable Information from Supervised Finetuned Models

**Authors:** Sae Furukawa, Alina Oprea

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12264v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12264v1)

**Summary:** Supervised Finetuning (SFT) has become one of the primary methods for adapting a large language model (LLM) with extensive pre-trained knowledge to domain-specific, instruction-following tasks. SFT datasets, composed of instruction-response pairs, often include user-provided information that may contain sensitive data such as personally identifiable information (PII), raising privacy concerns. This paper studies the problem of PII reconstruction from SFT models for the first time. We construct m...

---

### 30. PRISM: Pareto-Efficient Retrieval over Intent-Aware Structured Memory for Long-Horizon Agents

**Authors:** Jingyi Peng, Zhongwei Wan, Weiting Liu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12260v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12260v1)

**Summary:** Long-horizon language agents accumulate conversation history far faster than any fixed context window can hold, making memory management critical to both answer accuracy and serving cost. Existing approaches either expand the context window without addressing what is retrieved, perform heavy ingestion-time fact extraction at substantial token cost, or rely on heuristic graph traversal that leaves both accuracy and efficiency on the table. We present PRISM, a training-free retrieval-side framewor...

---

### 31. PreScam: A Benchmark for Predicting Scam Progression from Early Conversations

**Authors:** Weixiang Sun, Shang Ma, Yiyang Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12243v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12243v1)

**Summary:** Conversational scams, such as romance and investment scams, are emerging as a major form of online fraud. Unlike one-shot scam lures such as fake lottery or unpaid toll messages, they unfold through multi-turn conversations in which scammers gradually manipulate victims using evolving psychological techniques. However, existing research mainly focuses on static scam detection or synthetic scams, leaving open whether language models can understand how real-world scams progress over time. We intro...

---

### 32. Mind the Pause: Disfluency-Aware Objective Tuning for Multilingual Speech Correction with LLMs

**Authors:** Deepak Kumar, Baban Gain, Asif Ekbal

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12242v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12242v1)

**Summary:** Automatic Speech Recognition (ASR) transcripts often contain disfluencies, such as fillers, repetitions, and false starts, which reduce readability and hinder downstream applications like chatbots and voice assistants. If left unaddressed, such disfluencies can significantly degrade the reliability of downstream systems. Most existing approaches rely on classical models that focus on identifying disfluent tokens for removal. While this strategy is effective to some extent, it often disrupts gram...

---

### 33. Combining On-Policy Optimization and Distillation for Long-Context Reasoning in Large Language Models

**Authors:** Miguel Moura Ramos, Duarte M. Alves, André F. T. Martins

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12227v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12227v1)

**Summary:** Adapting large language models (LLMs) to long-context tasks requires post-training methods that remain accurate and coherent over thousands of tokens. Existing approaches are limited in several ways: 1) off-policy methods such as supervised fine-tuning (SFT) and knowledge distillation (KD) suffer from exposure bias and limited recovery from model-generated errors over long horizons; 2) on-policy reinforcement learning methods such as Group Relative Policy Optimization (GRPO) better align trainin...

---

### 34. Mechanistic Interpretability of ASR models using Sparse Autoencoders

**Authors:** Dan Pluth, Zachary Nicholas Houghton, Yu Zhou, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12225v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12225v1)

**Summary:** Understanding the internal machinations of deep Transformer-based NLP models is more crucial than ever as these models see widespread use in various domains that affect the public at large, such as industry, academia, finance, health. While these models have advanced rapidly, their internal mechanisms remain largely a mystery. Techniques such as Sparse Autoencoders (SAE) have emerged to understand these mechanisms by projecting dense representations into a sparse vector. While existing research ...

---

### 35. Not How Many, But Which: Parameter Placement in Low-Rank Adaptation

**Authors:** Arijit Sehanobish, Charles Lovering

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12207v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12207v1)

**Summary:** We study the \textit{parameter placement problem}: given a fixed budget of $k$ trainable entries within the B matrix of a LoRA adapter (A frozen), does the choice of which $k$ matter? Under supervised fine-tuning, random and informed subsets achieve comparable performance. Under GRPO on base models, random placement fails to improve over the base model, while gradient-informed placement recovers standard LoRA accuracy. This regime dependence traces to gradient structure: SFT gradients are low-ra...

---

### 36. Mitigating Context-Memory Conflicts in LLMs through Dynamic Cognitive Reconciliation Decoding

**Authors:** Yigeng Zhou, Wu Li, Yifan Lu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12185v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12185v1)

**Summary:** Large language models accumulate extensive parametric knowledge through pre-training. However, knowledge conflicts occur when outdated or incorrect parametric knowledge conflicts with external knowledge in the context. Existing methods address knowledge conflicts through contrastive decoding, but in conflict-free scenarios, static approaches disrupt output distribution. Other dynamic decoding methods attempt to measure the degree of conflict but still struggle with complex real-world situations....

---

### 37. Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics

**Authors:** Jishnu Sethumadhavan Nair, Patrice Bechard, Rishabh Maheshwary, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12178v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12178v1)

**Summary:** World models enable agents to anticipate the effects of their actions by internalizing environment dynamics. In enterprise systems, however, these dynamics are often defined by tenant-specific business logic that varies across deployments and evolves over time, making models trained on historical transitions brittle under deployment shift. We ask a question the world-models literature has not addressed: when the rules can be read at inference time, does an agent still need to learn them? We argu...

---

### 38. Correcting Selection Bias in Sparse User Feedback for Large Language Model Quality Estimation: A Multi-Agent Hierarchical Bayesian Approach

**Authors:** Andrea Morandi, Mahesh Viswanathan

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12177v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12177v1)

**Summary:** [Abridged] Production LLM deployments receive feedback from a non-random fraction of users: thumbs sit mostly in the tails of the satisfaction distribution, and a naive average over them can land 40-50 percentage points away from true system quality. We treat this as a topic- and sentiment- stratified selection-bias problem and propose a three-agent hierarchical Bayesian pipeline that does not require ground-truth labels on individual interactions. A Topic Clustering Agent partitions the stream ...

---

### 39. Latent Causal Void: Explicit Missing-Context Reconstruction for Misinformation Detection

**Authors:** Hui Li, Zhongquan Jian, Jinsong Su, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12156v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12156v1)

**Summary:** Automatic misinformation detection performs well when deception is visible in what an article explicitly states. However, some misinformation articles remain locally coherent and only become misleading once compared with contemporaneous reports that supply background facts the article omits. We study this omission-relevant setting and observe that current omission-aware approaches typically either attach retrieved context as auxiliary evidence or infer a categorical omission signal, leaving the ...

---

### 40. Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models

**Authors:** Yexing Xu, Wei Feng, Shen Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12138v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12138v1)

**Summary:** Generating realistic and user-preferred advertisements is a key challenge in e-commerce. Existing approaches utilize multiple independent models driven by click-through-rate (CTR) to controllably create attractive image or text advertisements. However, their pipelines lack cross-modal perception and rely on CTR that only reflects average preferences. Therefore, we explore jointly generating personalized image-text advertisements from historical click behaviors. We first design a Unified Advertis...

---

### 41. Metaphor Is Not All Attention Needs

**Authors:** Olga Sorokoletova, Francesco Giarrusso, Giacomo De Luca, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12128v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12128v1)

**Summary:** Large language models are increasingly deployed in safety-critical applications, where their ability to resist harmful instructions is essential. Although post-training aims to make models robust against many jailbreak strategies, recent evidence shows that stylistic reformulations, such as poetic transformation, can still bypass safety mechanisms with alarming effectiveness. This raises a central question: why do literary jailbreaks succeed? In this work, we investigate whether their effectiven...

---

### 42. Sign Language Recognition and Translation for Low-Resource Languages: Challenges and Pathways Forward

**Authors:** Nigar Alishzade, Gulchin Abdullayeva

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12096v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12096v1)

**Summary:** Sign languages are natural, visual-gestural languages used by Deaf communities worldwide. Over 300 distinct sign languages remain severely low-resource due to limited documentation, sparse datasets, and insufficient computational tools. This systematic review synthesizes literature on sign language recognition and translation for under-resourced languages, using Azerbaijan Sign Language (AzSL) as a case study. Analysis of global initiatives extracts eight actionable lessons, including community ...

---

### 43. World Action Models: The Next Frontier in Embodied AI

**Authors:** Siyin Wang, Junhao Shi, Zhaoyang Fu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12090v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12090v1)

**Summary:** Vision-Language-Action (VLA) models have achieved strong semantic generalization for embodied policy learning, yet they learn reactive observation-to-action mappings without explicitly modeling how the physical world evolves under intervention. A growing body of work addresses this limitation by integrating world models, predictive models of environment dynamics, into the action generation pipeline. We term this emerging paradigm World Action Models (WAMs): embodied foundation models that unify ...

---

### 44. Do Language Models Encode Knowledge of Linguistic Constraint Violations?

**Authors:**  Hardy, Sebastian Padó

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12055v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12055v1)

**Summary:** Large Language Models (LLMs) achieve strong linguistic performance, yet their internal mechanisms for producing these predictions remain unclear. We investigate the hypothesis that LLMs encode representations of linguistic constraint violations within their parameters, which are selectively activated when processing ungrammatical sentences. To test this, we use sparse autoencoders to decompose polysemantic activations into sparse, monosemantic features and recover candidates for violation-relate...

---

### 45. Is Child-Directed Language Optimized for Word Learning? A Computational Study of Verb Meaning Acquisition

**Authors:** Francesca Padovani, Jaap Jumelet, Yevgen Matusevych, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12047v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12047v1)

**Summary:** Is child-directed language (CDL) optimized to support language learning, and which aspects of linguistic development does it facilitate? We investigate this question using neural language models trained on CDL versus adult-directed language (ADL). We selectively remove syntactic or lexical co-occurrence information from the model training data, and evaluate the impact of these manipulations on verb meaning acquisition. While disrupting syntax impairs learning across all datasets, models trained ...

---

### 46. SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs

**Authors:** Xiaoyuan Li, Moxin Li, Keqin Bao, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12039v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12039v1)

**Summary:** Skill libraries enable large language model agents to reuse experience from past interactions, but most existing libraries store skills as isolated entries and retrieve them only by semantic similarity. This leads to two key challenges for compositional tasks. Firstly, an agent must identify not only relevant skills but also how they depend on and build upon each other. Secondly, it also makes library maintenance difficult, since the system lacks structural cues for deciding when skills should b...

---

### 47. Caraman at SemEval-2026 Task 8: Three-Stage Multi-Turn Retrieval with Query Rewriting, Hybrid Search, and Cross-Encoder Reranking

**Authors:** David-Maximilian Caraman, Gheorghe Cosmin Silaghi

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12028v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12028v1)

**Summary:** We describe our system for SemEval-2026 Task 8 (MTRAGEval), participating in Task A (Retrieval) across four English-language domains. Our approach employs a three-stage pipeline: (1) query rewriting via a LoRA-fine-tuned Qwen 2.5 7B model that transforms context-dependent follow-up questions into standalone queries, (2) hybrid BM25 and dense retrieval combined through Reciprocal Rank Fusion, and (3) cross-encoder reranking with BGE-reranker-v2-m3. On the official test set, the system achieves nD...

---

### 48. SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation

**Authors:** Xiaoyuan Li, Yuzhe Wang, Moxin Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12022v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12022v1)

**Summary:** Large Language Models (LLMs) achieve strong performance on standard knowledge evaluation benchmarks, yet recent work shows that their knowledge capabilities remain brittle under question variants that test the same knowledge in different forms. Robustness augmentation of existing knowledge evaluation benchmarks is therefore necessary, but current LLM-assisted generate-then-verify pipelines are costly and difficult to scale due to low-yield variant generation and unreliable variant verification. ...

---

### 49. SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces

**Authors:** Chang Jin, An Wang, Zeming Wei, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12015v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12015v1)

**Summary:** Reusable skills are becoming a common interface for extending large language model agents, packaging procedural guidance with access to files, tools, memory, and execution environments. However, this modularity introduces attack surfaces that are largely missed by existing safety evaluations: even when the user request is benign, task-relevant skill materials or local artifacts can steer an agent toward unsafe actions. We present SkillSafetyBench, a runnable benchmark for evaluating such skill-m...

---

### 50. Learning Agentic Policy from Action Guidance

**Authors:** Yuxiang Ji, Zengbin Wang, Yong Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12004v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12004v1)

**Summary:** Agentic reinforcement learning (RL) for Large Language Models (LLMs) critically depends on the exploration capability of the base policy, as training signals emerge only within its in-capability region. For tasks where the base policy cannot reach reward states, additional training or external guidance is needed to recover effective learning signals. Rather than relying on costly iterative supervised fine tuning (SFT), we exploit the abundant action data generated in everyday human interactions....

---

## cs.CV

**50 papers**

### 1. Covering Human Action Space for Computer Use: Data Synthesis and Benchmark

**Authors:** Miaosen Zhang, Xiaohan Zhao, Zhihong Tan, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12501v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12501v1)

**Summary:** Computer-use agents (CUAs) automate on-screen work, as illustrated by GPT-5.4 and Claude. Yet their reliability on complex, low-frequency interactions is still poor, limiting user trust. Our analysis of failure cases from advanced models suggests a long-tail pattern in GUI operations, where a relatively small fraction of complex and diverse interactions accounts for a disproportionate share of task failures. We hypothesize that this issue largely stems from the scarcity of data for complex inter...

---

### 2. SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture

**Authors:** Haiwen Diao, Penghao Wu, Hanming Deng, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12500v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12500v1)

**Summary:** Recent large vision-language models (VLMs) remain fundamentally constrained by a persistent dichotomy: understanding and generation are treated as distinct problems, leading to fragmented architectures, cascaded pipelines, and misaligned representation spaces. We argue that this divide is not merely an engineering artifact, but a structural limitation that hinders the emergence of native multimodal intelligence. Hence, we introduce SenseNova-U1, a native unified multimodal paradigm built upon NE...

---

### 3. EgoForce: Forearm-Guided Camera-Space 3D Hand Pose from a Monocular Egocentric Camera

**Authors:** Christen Millerdurai, Shaoxiang Wang, Yaxu Xie, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12498v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12498v1)

**Summary:** Reconstructing the absolute 3D pose and shape of the hands from the user's viewpoint using a single head-mounted camera is crucial for practical egocentric interaction in AR/VR, telepresence, and hand-centric manipulation tasks, where sensing must remain compact and unobtrusive. While monocular RGB methods have made progress, they remain constrained by depth-scale ambiguity and struggle to generalize across the diverse optical configurations of head-mounted devices. As a result, models typically...

---

### 4. From Web to Pixels: Bringing Agentic Search into Visual Perception

**Authors:** Bokang Yang, Xinyi Sun, Kaituo Feng, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12497v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12497v1)

**Summary:** Visual perception connects high-level semantic understanding to pixel-level perception, but most existing settings assume that the decisive evidence for identifying a target is already in the image or frozen model knowledge. We study a more practical yet harder open-world case where a visible object must first be resolved from external facts, recent events, long-tail entities, or multi-hop relations before it can be localized. We formalize this challenge as Perception Deep Research and introduce...

---

### 5. CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives

**Authors:** Yihao Meng, Zichen Liu, Hao Ouyang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12496v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12496v1)

**Summary:** Autoregressive video generation aims at real-time, open-ended synthesis. Yet, cinematic storytelling is not merely the endless extension of a single scene; it requires progressing through evolving events, viewpoint shifts, and discrete shot boundaries. Existing autoregressive models often struggle in this setting. Trained primarily for short-horizon continuation, they treat long sequences as extended single shots, inevitably suffering from motion stagnation and semantic drift during long rollout...

---

### 6. AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward

**Authors:** Runhui Huang, Jie Wu, Rui Yang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12495v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12495v1)

**Summary:** In this paper, we propose AlphaGRPO, a novel framework that applies Group Relative Policy Optimization (GRPO) to AR-Diffusion Unified Multimodal Models (UMMs) to enhance multimodal generation capabilities without an additional cold-start stage. Our approach unlocks the model's intrinsic potential to perform advanced reasoning tasks: Reasoning Text-to-Image Generation, where the model actively infers implicit user intents, and Self-Reflective Refinement, where it autonomously diagnoses and correc...

---

### 7. Revisiting Photometric Ambiguity for Accurate Gaussian-Splatting Surface Reconstruction

**Authors:** Jiahe Li, Jiawei Zhang, Xiao Bai, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12494v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12494v1)

**Summary:** Surface reconstruction with differentiable rendering has achieved impressive performance in recent years, yet the pervasive photometric ambiguities have strictly bottlenecked existing approaches. This paper presents AmbiSuR, a framework that explores an intrinsic solution upon Gaussian Splatting for the photometric ambiguity-robust surface 3D reconstruction with high performance. Starting by revisiting the foundation, our investigation uncovers two built-in primitive-wise ambiguities in represen...

---

### 8. Elastic Attention Cores for Scalable Vision Transformers

**Authors:** Alan Z. Song, Yinjie Chen, Mu Nan, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12491v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12491v1)

**Summary:** Vision Transformers (ViTs) achieve strong data-driven scaling by leveraging all-to-all self-attention. However, this flexibility incurs a computational cost that scales quadratically with image resolution, limiting ViTs in high-resolution domains. Underlying this approach is the assumption that pairwise token interactions are necessary for learning rich visual-semantic representations. In this work, we challenge this assumption, demonstrating that effective visual representations can be learned ...

---

### 9. OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation

**Authors:** Guohui Zhang, XiaoXiao Ma, Jie Huang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12480v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12480v1)

**Summary:** Recent advances in joint audio-video generation have been remarkable, yet real-world applications demand strong per-modality fidelity, cross-modal alignment, and fine-grained synchronization. Reinforcement Learning (RL) offers a promising paradigm, but its extension to multi-objective and multi-modal joint audio-video generation remains unexplored. Notably, our in-depth analysis first reveals that the primary obstacles to applying RL in this stem from: (i) multi-objective advantages inconsistenc...

---

### 10. FuTCR: Future-Targeted Contrast and Repulsion for Continual Panoptic Segmentation

**Authors:** Nicholas Ikechukwu, Keanu Nichols, Deepti Ghadiyaram, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12451v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12451v1)

**Summary:** Continual Panoptic Segmentation (CPS) requires methods that can quickly adapt to new categories over time. The nature of this dense prediction task means that training images may contain a mix of labeled and unlabeled objects. As nothing is known about these unlabeled objects a priori, existing methods often simply group any unlabeled pixel into a single "background" class during training. In effect, during training, they repeatedly tell the model that all the different background categories are...

---

### 11. LychSim: A Controllable and Interactive Simulation Framework for Vision Research

**Authors:** Wufei Ma, Chloe Wang, Siyi Chen, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12449v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12449v1)

**Summary:** While self-supervised pretraining has reduced vision systems' reliance on synthetic data, simulation remains an indispensable tool for closed-loop optimization and rigorous out-of-distribution (OOD) evaluation. However, modern simulation platforms often present steep technical barriers, requiring extensive expertise in computer graphics and game development. In this work, we present LychSim, a highly controllable and interactive simulation framework built upon Unreal Engine 5 to bridge this gap....

---

### 12. 3D Gaussian Splatting for Efficient Retrospective Dynamic Scene Novel View Synthesis with a Standardized Benchmark

**Authors:** Yunxiao Zhang, Suryansh Kumar

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12437v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12437v1)

**Summary:** Retrospective novel view synthesis (NVS) of dynamic scenes is fundamental to applications such as sports. Recent dynamic 3D Gaussian Splatting (3DGS) approaches introduce temporally coupled formulations to enforce motion coherence across time. In this paper, we argue that, in a synchronized multi-view (MV) setting typical of sports, the dynamic scene at each time step is already strongly geometrically constrained. We posit that the availability of calibrated, synchronized viewpoints provides suf...

---

### 13. GaitProtector: Impersonation-Driven Gait De-Identification via Training-Free Diffusion Latent Optimization

**Authors:** Huiran Duan, Qian Zhou, Zhongliang Guo, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12431v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12431v1)

**Summary:** Conventional gait de-identification methods often encounter an inherent trade-off: they either provide insufficient identity suppression or introduce spatiotemporal distortions that impede structure-sensitive downstream applications. We propose GaitProtector, an impersonation-driven gait de-identification framework that formulates privacy protection as a unified objective with two tightly coupled components: (i) obfuscation, which repels the protected gait from the source identity, and (ii) impe...

---

### 14. AOI-SSL: Self-Supervised Framework for Efficient Segmentation of Wire-bonded Semiconductors In Optical Inspection

**Authors:** Joaquín Figueira, Rob Van Gastel, Giacomo D'Amicantonio, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12430v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12430v1)

**Summary:** Segmentation models in automated optical inspection of wire-bonded semiconductors are typically device-specific and must be re-trained when new devices or distribution shifts appear. We introduce AOI-SSL, a training-efficient framework for semantic segmentation of wire-bonded semiconductors by combining small-domain self-supervised pre-training of vision transformers with in-context inference that minimizes the need of labeled examples. We pre-train SOTA self-supervised algorithms in a small ind...

---

### 15. Beyond Localization: A Comprehensive Diagnosis of Perspective-Conditioned Spatial Reasoning in MLLMs from Omnidirectional Images

**Authors:** Yuangong Chen, Wai Keung Wong, Jiaxing Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12413v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12413v1)

**Summary:** Multimodal Large Language Models (MLLMs) show strong visual perception, yet remain limited in reasoning about space under changing viewpoints. We study this challenge as Perspective-Conditioned Spatial Reasoning (PCSR) in 360-degree omnidirectional images, where broad scene coverage reduces ambiguity from partial observations without eliminating the need for viewpoint-dependent inference. To assess this capability, we introduce PCSR-Bench, a diagnostic benchmark of 84,373 question-answer pairs f...

---

### 16. GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction

**Authors:** Xiao Cao, Yuze Li, Youmin Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12399v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12399v1)

**Summary:** 3D Gaussian Splatting (3DGS) has emerged as a prominent paradigm for 3D reconstruction and novel view synthesis. However, it remains vulnerable to severe artifacts when trained under sparse-view constraints. While recent methods attempt to rectify artifacts in rendered views using image diffusion models, they typically rely on multi-view self-attention to retrieve information from reference images. We observe that this mechanism often fails when the rendered novel views output by 3DGS are heavil...

---

### 17. SEMIR: Semantic Minor-Induced Representation Learning on Graphs for Visual Segmentation

**Authors:** Luke James Miller, Yugyung Lee

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12389v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12389v1)

**Summary:** Segmenting small and sparse structures in large-scale images is fundamentally constrained by voxel-level, lattice-bound computation and extreme class imbalance -- dense, full-resolution inference scales poorly and forces most pipelines to rely on fixed regionization or downsampling, coupling computational cost to image resolution and attenuating boundary evidence precisely where minority structures are most informative. We introduce SEMIR (Semantic Minor-Induced Representation Learning), a repre...

---

### 18. Fast Image Super-Resolution via Consistency Rectified Flow

**Authors:** Jiaqi Xu, Wenbo Li, Haoze Sun, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12377v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12377v1)

**Summary:** Diffusion models (DMs) have demonstrated remarkable success in real-world image super-resolution (SR), yet their reliance on time-consuming multi-step sampling largely hinders their practical applications. While recent efforts have introduced few- or single-step solutions, existing methods either inefficiently model the process from noisy input or fail to fully exploit iterative generative priors, compromising the fidelity and quality of the reconstructed images. To address this issue, we propos...

---

### 19. Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models

**Authors:** Yanting Miao, Yutao Sun, Dexin Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12374v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12374v1)

**Summary:** Visual latent reasoning lets a multimodal large language model (MLLM) create intermediate visual evidence as continuous tokens, avoiding external tools or image generators. However, existing methods usually follow an output-as-input latent paradigm and yield unstable gains. We identify evidence for a feature-space mismatch that can contribute to this instability: dominant visual-latent models build on pre-norm MLLMs and reuse decoder hidden states as predicted latent inputs, even though these st...

---

### 20. VIP: Visual-guided Prompt Evolution for Efficient Dense Vision-Language Inference

**Authors:** Hao Zhu, Shuo Jin, Wenbin Liao, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12325v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12325v1)

**Summary:** Pursuing training-free open-vocabulary semantic segmentation in an efficient and generalizable manner remains challenging due to the deep-seated spatial bias in CLIP. To overcome the limitations of existing solutions, this work moves beyond the CLIP-based paradigm and harnesses the recent spatially-aware dino.txt framework to facilitate more efficient and high-quality dense prediction. While dino.txt exhibits robust spatial awareness, we find that the semantic ambiguity of text queries gives ris...

---

### 21. Contrastive Learning under Noisy Temporal Self-Supervision for Colonoscopy Videos

**Authors:** Luca Parolari, Pietro Gori, Lamberto Ballan, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12320v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12320v1)

**Summary:** Learning robust representations of polyp tracklets is key to enabling multiple AI-assisted colonoscopy applications, from polyp characterization to automated reporting and retrieval. Supervised contrastive learning is an effective approach for learning such representations, but it typically relies on correct positive and negative definitions. Collecting these labels requires linking tracklets that depict the same underlying polyp entity throughout the video, which is costly and demands specializ...

---

### 22. G$^2$TR: Generation-Guided Visual Token Reduction for Separate-Encoder Unified Multimodal Models

**Authors:** Junxian Li, Kai Liu, Zizhong Ding, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12309v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12309v1)

**Summary:** The development of separate-encoder Unified multimodal models (UMMs) comes with a rapidly growing inference cost due to dense visual token processing. In this paper, we focus on understanding-side visual token reduction for improving the efficiency of separate-encoder UMMs. While this topic has been widely studied for MLLMs, existing methods typically rely on attention scores, text-image similarity and so on, implicitly assuming that the final objective is discriminative reasoning. This assumpti...

---

### 23. KAN-CL: Per-Knot Importance Regularization for Continual Learning with Kolmogorov-Arnold Networks

**Authors:** Minjong Cheon

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12306v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12306v1)

**Summary:** Catastrophic forgetting remains the central obstacle in continual learning (CL): parameters shared across tasks interfere with one another, and existing regularization methods such as EWC and SI apply uniform penalties without awareness of which input region a parameter serves. We propose KAN-CL, a continual learning framework that exploits the compact-support spline parameterization of Kolmogorov-Arnold Networks (KANs) to perform importance-weighted anchoring at per-knot granularity. Deployed a...

---

### 24. Images in Sentences: Scaling Interleaved Instructions for Unified Visual Generation

**Authors:** Yabo Zhang, Kunchang Li, Dewei Zhou, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12305v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12305v1)

**Summary:** While recent advancements in multimodal language models have enabled image generation from expressive multi-image instructions, existing methods struggle to maintain performance under complex interleaved instructions. This limitation stems from the structural separation of images and text in current paradigms, which forces models to bridge difficult long-range dependencies to match descriptions with visual targets. To address these challenges, we propose \texttt{I}mages i\texttt{N} \texttt{SE}n\...

---

### 25. From Model Uncertainty to Human Attention: Localization-Aware Visual Cues for Scalable Annotation Review

**Authors:** Moussa Kassem Sbeyti, Joshua Holstein, Philipp Spitzer, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12303v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12303v1)

**Summary:** High-quality labeled data is essential for training robust machine learning models, yet obtaining annotations at scale remains expensive. AI-assisted annotation has therefore become standard in large-scale labeling workflows. However, in tasks where model predictions carry two independent components, a class label and spatial boundaries, a model may classify an object with high confidence while mislocalizing it. Existing AI-assisted workflows offer annotators no signal about where spatial errors...

---

### 26. EgoEV-HandPose: Egocentric 3D Hand Pose Estimation and Gesture Recognition with Stereo Event Cameras

**Authors:** Luming Wang, Hao Shi, Jiajun Zhai, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12297v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12297v1)

**Summary:** Egocentric 3D hand pose estimation and gesture recognition are essential for immersive augmented/virtual reality, human-computer interaction, and robotics. However, conventional frame-based cameras suffer from motion blur and limited dynamic range, while existing event-based methods are hindered by ego-motion interference, monocular depth ambiguity, and the lack of large-scale real-world stereo datasets. To overcome these limitations, we propose EgoEV-HandPose, an end-to-end framework for joint ...

---

### 27. Large-Small Model Collaboration for Farmland Semantic Change Detection

**Authors:** Xinjia Li, Rui Wang, Qiurong Peng, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12282v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12282v1)

**Summary:** Farmland Semantic Change Detection (SCD) is essential for cultivated land protection, yet existing benchmarks and models remain insufficient for fine-grained farmland conversion monitoring. Current datasets often lack dedicated "from-to" annotations, while visual change detection models are easily disturbed by phenology-induced pseudo-changes caused by crop rotation, seasonal variation, and illumination differences. To address these challenges, we construct HZNU-FCD, a large-scale fine-grained f...

---

### 28. Beyond Text Prompts: Visual-to-Visual Generation as A Unified Paradigm

**Authors:** Yaofang Liu, Kangning Cui, Meng Chu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12271v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12271v1)

**Summary:** Humans often specify and create through visual artifacts: typography sheets, sketches, reference images, and annotated scenes. Yet modern visual generators still ask users to serialize this intent into text, a bottleneck that compresses signals like spatial structure, exact appearance, and glyph shape. We propose \textbf{\emph{visual-to-visual} (V2V)} generation, in which the user conditions a generative model with a visual specification page rather than a text prompt. The page is not an edit ta...

---

### 29. CAD-feature enhanced machine learning for manufacturing effort estimation on sheet metal bending parts

**Authors:** Matteo Ballegeer, Toon Van Camp, Willem Jaspers, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12266v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12266v1)

**Summary:** Graph-based machine learning has emerged as a promising approach for manufacturability analysis by learning directly from CAD models represented as Boundary Representations (B-reps), exploiting both surface geometry and topological connectivity. However, purely geometric representations often lack the process-specific semantics required for accurate manufacturability prediction: many manufacturing factors, such as surface roles or bend intent, are not explicitly encoded in shape alone and are di...

---

### 30. From Image Hashing to Scene Change Detection

**Authors:** Anh-Kiet Duong, Marie-Claire Iatrides, Petra Gomez-Krämer, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12259v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12259v1)

**Summary:** Image hashing provides compact representations for efficient storage and retrieval but is inherently limited to global comparison and cannot reason about where changes occur. This limitation prevents hashing from being directly applicable to scene change detection, where spatial localization is essential. In this work, we revisit hashing from a scene change detection perspective and propose HashSCD, a patch-wise hashing framework that enables both efficient global change detection and localized ...

---

### 31. H3D-MarNet: Wavelet-Guided Dual-Path Learning for Metal Artifact Suppression and CT Modality Transformation for Radiotherapy Workflows

**Authors:** Mubashara Rehman, Niki Martinel, Michele Avanzo, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12252v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12252v1)

**Summary:** Metal artifacts in computed tomography (CT) severely degrade image quality, compromising diagnostic accuracy and radiotherapy planning, especially in cancer patients with high-density implants. We propose H3D-MarNet, a two-stage framework for artifact-aware CT domain transformation from kilo-voltage CT (kVCT) to mega-voltage CT (MVCT). In the first stage, a wavelet-based preprocessing module suppresses metal-induced artifacts through frequency-aware denoising while preserving anatomical structur...

---

### 32. UHR-Micro: Diagnosing and Mitigating the Resolution Illusion in Earth Observation VLMs

**Authors:** Shuo Ni, Tong Wang, Jing Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12237v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12237v1)

**Summary:** Vision-Language Models (VLMs) increasingly operate on ultra-high-resolution (UHR) Earth observation imagery, yet they remain vulnerable to a severe scale mismatch between large-scale scene context and micro-scale targets. We refer to this empirical gap as a "resolution illusion": higher input resolution provides the appearance of richer visual detail, but does not necessarily yield reliable perception of spatially small, task-relevant evidence. To benchmark this challenge, we introduce UHR-Micro...

---

### 33. TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion

**Authors:** Mohammad Khoshkdahan, Alexey Vinel

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12220v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12220v1)

**Summary:** Safe autonomous agents and mobile robots need fast real time 3D perception, especially for vulnerable road users (VRUs) such as pedestrians. We introduce a new bird's eye view (BEV) encoding, which maps the full 3D LiDAR point cloud into a light-weight 2D BEV tensor with three height bands. We explicitly reformulate 3D detection as a 2D detection problem and then reconstruct 3D boxes from the BEV outputs. A single network detects cars, pedestrians, and cyclists in one pass. The backbone uses are...

---

### 34. Learning Ego-Centric BEV Representations from a Perspective-Privileged View: Cross-View Supervision for Online HD Map Construction

**Authors:** Daniel Lengerer, Mathias Pechinger, Klaus Bogenberger, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12218v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12218v1)

**Summary:** Bird's-eye-view (BEV) representations derived from multi-camera input have become a central interface for online high-definition (HD) map construction. However, most approaches rely solely on ego-centric supervision, requiring large-scale scene structure to be inferred from incomplete observations, occlusions, and diminishing information density at long range, where perspective effects and spatial sparsity hinder consistent structural reasoning. We introduce Cross-View Supervision (CVS), a repre...

---

### 35. Enhancing Domain Generalization in 3D Human Pose Estimation through Controllable Generative Augmentation

**Authors:** Xinhao Hu, Yiyi Zhang, Liqing Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12198v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12198v1)

**Summary:** Pedestrian motion, due to its causal nature, is strongly influenced by domain gaps arising from discrepancies between training and testing data distributions. Focusing on 3D human pose estimation, this work presents a controllable human pose generation framework that synthesizes diverse video data by systematically varying poses, backgrounds, and camera viewpoints. This generative augmentation enriches training datasets, enhances model generalization, and alleviates the limitations of existing m...

---

### 36. SyncDPO: Enhancing Temporal Synchronization in Video-Audio Joint Generation via Preference Learning

**Authors:** Xin Cheng, Xihua Wang, Ying Ba, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12179v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12179v1)

**Summary:** Recent advancements in video-audio joint generation have achieved remarkable success in semantic correspondence. However, achieving precise temporal synchronization, which requires fine-grained alignment between audio events and their visual triggers, remains a challenging problem. The post-training method for joint generation is largely dominated by Supervised Fine-Tuning, but the commonly used Mean Squared Error loss provides insufficient penalties for subtle temporal misalignments. Direct Pre...

---

### 37. UniFixer: A Universal Reference-Guided Fixer for Diffusion-Based View Synthesis

**Authors:** Sihan Chen, Xiang Zhang, Yang Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12169v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12169v1)

**Summary:** With the recent surge of generative models, diffusion-based approaches have become mainstream for view synthesis tasks, either in an explicit depth-warp-inpaint or in an implicit end-to-end manner. Despite their success, both paradigms often suffer from noticeable quality degradation, e.g., blurred details and distorted structures, caused by pixel-to-latent compression and diffusion hallucination. In this paper, we investigate diffusion degradation from three key dimensions (i.e., spatial, tempo...

---

### 38. From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation

**Authors:** Yajie Li, Bozhou Zhang, Chun Gu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12167v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12167v1)

**Summary:** Video generation models offer a promising imagination mechanism for robot manipulation by predicting long-horizon future observations, but effectively exploiting these imagined futures for action execution remains challenging. Existing approaches either condition policies on predicted frames or directly decode generated videos into actions, both suffering from a mismatch between visual realism and control relevance. As a result, predicted observations emphasize perceptual fidelity rather than ac...

---

### 39. Self-Consistent Latent Reasoning: Long Latent Sequence Reasoning for Vision-Language Model

**Authors:** Chenfeng Wang, Wei He, Xuhan Zhu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12163v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12163v1)

**Summary:** In language reasoning, longer chains of thought consistently yield better performance, which naturally suggests that visual latent reasoning may likewise benefit from longer latent sequences. However, we discover a counterintuitive phenomenon: the performance of existing latent visual reasoning methods systematically degrades as the latent sequence grows longer. We reveal the root cause: Information Gain Collapse -- autoregressive generation makes each step highly dependent on prior outputs, so ...

---

### 40. Cross-Modal-Domain Generalization Through Semantically Aligned Discrete Representations

**Authors:** Souptik Sen, Raneen Younis, Zahra Ahmadi

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12145v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12145v1)

**Summary:** Multimodal learning seeks to integrate information across diverse sensory sources, yet current approaches struggle to balance cross-modal generalizability with modality-specific structure. Continuous (implicit) methods preserve fine-grained priors but render generalization challenging, while discrete (explicit) approaches enforce shared prototypes at the expense of modality specificity. We introduce CoDAAR (Cross-modal Discrete Alignment And Reconstruction), a novel framework that resolves this ...

---

### 41. PoseCompass: Intelligent Synthetic Pose Selection for Visual Localization

**Authors:** Yanan Zhou, Zhaoyan Qian, Yanli Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12144v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12144v1)

**Summary:** In visual localization, Absolute Pose Regression (APR) enables real-time 6-DoF camera pose inference from single images, yet critically depends on fine-tuning data quality and coverage. While recent methods leverage 3D Gaussian Splatting (3DGS) for novel view synthesis-based data augmentation, random sampling generates redundant views and noisy samples from poorly reconstructed regions. To mitigate this research gap, we propose PoseCompass, an intelligent pose selection pipeline for 3DGS-based A...

---

### 42. EchoTracker2: Enhancing Myocardial Point Tracking by Modeling Local Motion

**Authors:** Md Abulkalam Azad, Vegard Holmstrøm, John Nyberg, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12140v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12140v1)

**Summary:** Myocardial point tracking (MPT) has recently emerged as a promising direction for motion estimation in echocardiography, driven by advances in general-purpose point tracking methods. However, myocardial motion fundamentally differs from motion encountered in natural videos, as it arises from physiologically constrained deformation that is spatially and temporally continuous throughout the cardiac cycle. Consequently, motion trajectories typically remain locally confined despite substantial tissu...

---

### 43. Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models

**Authors:** Yexing Xu, Wei Feng, Shen Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12138v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12138v1)

**Summary:** Generating realistic and user-preferred advertisements is a key challenge in e-commerce. Existing approaches utilize multiple independent models driven by click-through-rate (CTR) to controllably create attractive image or text advertisements. However, their pipelines lack cross-modal perception and rely on CTR that only reflects average preferences. Therefore, we explore jointly generating personalized image-text advertisements from historical click behaviors. We first design a Unified Advertis...

---

### 44. MULTI: Disentangling Camera Lens, Sensor, View, and Domain for Novel Image Generation

**Authors:** Sonali Godavarthy, Matthias Neuwirth-Trapp, Tim-Felix Faasch, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12134v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12134v1)

**Summary:** Recent text-to-image models produce high-quality images, yet text ambiguity hinders precise control when specific styles or objects are required. There have been a number of recent works dealing with learning and composing multiple objects and patterns. However, current work focuses almost entirely on image content, overlooking imaging factors such as camera lens, sensor types, imaging viewpoints, and scenes' domain characteristics. We introduce this new challenge as Imaging Factor Disentangleme...

---

### 45. Disentangled Sparse Representations for Concept-Separated Diffusion Unlearning

**Authors:** Hyeonjin Kim, Hangyeol Jung, Heechan Yun, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12122v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12122v1)

**Summary:** Unlearning specific concepts in text-to-image diffusion models has become increasingly important for preventing undesirable content generation. Among prior approaches, sparse autoencoder (SAE)-based methods have attracted attention due to their ability to suppress target concepts through lightweight manipulation of latent features, without modifying model parameters. However, SAEs trained with sparse reconstruction objectives do not explicitly enforce concept-wise separation, resulting in shared...

---

### 46. MoCam: Unified Novel View Synthesis via Structured Denoising Dynamics

**Authors:** Haofeng Liu, Yang Zhou, Ziheng Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12119v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12119v1)

**Summary:** Generative novel view synthesis faces a fundamental dilemma: geometric priors provide spatial alignment but become sparse and inaccurate under view changes, while appearance priors offer visual fidelity but lack geometric correspondence. Existing methods either propagate geometric errors throughout generation or suffer from signal conflicts when fusing both statically. We introduce MoCam, which employs structured denoising dynamics to orchestrate a coordinated progression from geometry to appear...

---

### 47. When Policy Entropy Constraint Fails: Preserving Diversity in Flow-based RLHF via Perceptual Entropy

**Authors:** Xiaofeng Tan, Jun Liu, Bin-Bin Gao, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12112v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12112v1)

**Summary:** RLHF is widely used to align flow-matching text-to-image models with human preferences, but often leads to severe diversity collapse after fine-tuning. In RL, diversity is often assumed to correlate with policy entropy, motivating entropy regularization. However, we show this intuition breaks in flow models: policy entropy remains constant, even while perceptual diversity collapses. We explain this mismatch both theoretically and empirically: the constant entropy arises from the fixed, pre-defin...

---

### 48. World Action Models: The Next Frontier in Embodied AI

**Authors:** Siyin Wang, Junhao Shi, Zhaoyang Fu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12090v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12090v1)

**Summary:** Vision-Language-Action (VLA) models have achieved strong semantic generalization for embodied policy learning, yet they learn reactive observation-to-action mappings without explicitly modeling how the physical world evolves under intervention. A growing body of work addresses this limitation by integrating world models, predictive models of environment dynamics, into the action generation pipeline. We term this emerging paradigm World Action Models (WAMs): embodied foundation models that unify ...

---

### 49. UniCustom: Unified Visual Conditioning for Multi-Reference Image Generation

**Authors:** Yiyan Xu, Qiulin Wang, Wenjie Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12088v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12088v1)

**Summary:** Multi-reference image generation aims to synthesize images from textual instructions while faithfully preserving subject identities from multiple reference images. Existing VLM-enhanced diffusion models commonly rely on decoupled visual conditioning: semantic ViT features are processed by the VLM for instruction understanding, whereas appearance-rich VAE features are injected later into the diffusion backbone. Despite its intuitive design, this separation makes it difficult for the model to asso...

---

### 50. The Missing GAP: From Solving Square Jigsaw Puzzles to Handling Real World Archaeological Fragments

**Authors:** Ofir Itzhak Shahar, Gur Elkin, Ohad Ben-Shahar

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12077v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12077v1)

**Summary:** Jigsaw puzzle solving has been an increasingly popular task in the computer vision research community. Recent works have utilized cutting-edge architectures and computational approaches to reassemble groups of pieces into a coherent image, while achieving increasingly good results on well established datasets. However, most of these approaches share a common, restricting setting: operating solely on strictly square puzzle pieces. In this work, we introduce GAP, a set of novel jigsaw puzzles data...

---

## cs.LG

**50 papers**

### 1. AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward

**Authors:** Runhui Huang, Jie Wu, Rui Yang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12495v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12495v1)

**Summary:** In this paper, we propose AlphaGRPO, a novel framework that applies Group Relative Policy Optimization (GRPO) to AR-Diffusion Unified Multimodal Models (UMMs) to enhance multimodal generation capabilities without an additional cold-start stage. Our approach unlocks the model's intrinsic potential to perform advanced reasoning tasks: Reasoning Text-to-Image Generation, where the model actively infers implicit user intents, and Self-Reflective Refinement, where it autonomously diagnoses and correc...

---

### 2. Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation

**Authors:** Kexuan Shi, Hanxuan Li, Zeju Qiu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12492v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12492v1)

**Summary:** We introduce Pion, a spectrum-preserving optimizer for large language model (LLM) training based on orthogonal equivalence transformation. Unlike additive optimizers such as Adam and Muon, Pion updates each weight matrix through left and right orthogonal transformations, preserving its singular values throughout training. This yields an optimization mechanism that modulates the geometry of weight matrices while keeping their spectral norm fixed. We derive the Pion update rule, systematically exa...

---

### 3. Elastic Attention Cores for Scalable Vision Transformers

**Authors:** Alan Z. Song, Yinjie Chen, Mu Nan, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12491v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12491v1)

**Summary:** Vision Transformers (ViTs) achieve strong data-driven scaling by leveraging all-to-all self-attention. However, this flexibility incurs a computational cost that scales quadratically with image resolution, limiting ViTs in high-resolution domains. Underlying this approach is the assumption that pairwise token interactions are necessary for learning rich visual-semantic representations. In this work, we challenge this assumption, demonstrating that effective visual representations can be learned ...

---

### 4. Task-Adaptive Embedding Refinement via Test-time LLM Guidance

**Authors:** Ariel Gera, Shir Ashury-Tahan, Gal Bloch, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12487v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12487v1)

**Summary:** We explore the effectiveness of an LLM-guided query refinement paradigm for extending the usability of embedding models to challenging zero-shot search and classification tasks. Our approach refines the embedding representation of a user query using feedback from a generative LLM on a small set of documents, enabling embeddings to adapt in real time to the target task. We conduct extensive experiments with state-of-the-art text embedding models across a diverse set of challenging search and clas...

---

### 5. Learning, Fast and Slow: Towards LLMs That Adapt Continually

**Authors:** Rishabh Tiwari, Kusha Sareen, Lakshya A Agrawal, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12484v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12484v1)

**Summary:** Large language models (LLMs) are trained for downstream tasks by updating their parameters (e.g., via RL). However, updating parameters forces them to absorb task-specific information, which can result in catastrophic forgetting and loss of plasticity. In contrast, in-context learning with fixed LLM parameters can cheaply and rapidly adapt to task-specific requirements (e.g., prompt optimization), but cannot by itself typically match the performance gains available through updating LLM parameter...

---

### 6. Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training

**Authors:** Yuanda Xu, Hejian Sang, Zhengze Zhou, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12483v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12483v1)

**Summary:** In settings where labeled verifiable training data is the binding constraint, each checked example should be allocated carefully. The standard practice is to use this data directly on the model that will be deployed, for example by running GRPO on the deployment student. We argue that this is often an inefficient allocation because it overlooks a reward-density principle: sparse sequence-level reward should train models where exploration is productive, while dense token-level teacher reward shou...

---

### 7. MEME: Multi-entity & Evolving Memory Evaluation

**Authors:** Seokwon Jung, Alexander Rubinstein, Arnas Uselis, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12477v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12477v1)

**Summary:** LLM-based agents increasingly operate in persistent environments where they must store, update, and reason over information across many sessions. While prior benchmarks evaluate only single-entity updates, MEME defines six tasks spanning the full space defined by the multi-entity and evolving axes, including three not scored by prior work: Cascade and Absence (dependency reasoning) and Deletion (post-removal state). Evaluating six memory systems spanning three memory paradigms on 100 controlled ...

---

### 8. Routers Learn the Geometry of Their Experts: Geometric Coupling in Sparse Mixture-of-Experts

**Authors:** Sagi Ahrac, Noya Hochwald, Mor Geva

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12476v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12476v1)

**Summary:** Sparse Mixture-of-Experts (SMoE) models enable scaling language models efficiently, but training them remains challenging, as routing can collapse onto few experts and auxiliary load-balancing losses can reduce specialization. Motivated by these hurdles, we study how routing decisions in SMoEs are formed mechanistically. First, we reveal a geometric coupling between routers and their corresponding experts. For a given token, the router weights for the selected expert and the expert weights proce...

---

### 9. KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference

**Authors:** Alireza Nadali, Patrick Cooper, Ashutosh Trivedi, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12471v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12471v1)

**Summary:** We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks. At each step, the model processes the next chunk conditioned on the accumulated cache, appends the newly produced keys and values, and passes the enlarged cache forward; the same one-step update is applied repeatedly, analogous to foldl in functional programming. Building on the KV cache concatenation primitive introduced for l...

---

### 10. Solve the Loop: Attractor Models for Language and Reasoning

**Authors:** Jacob Fein-Ashley, Paria Rashidinejad

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12466v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12466v1)

**Summary:** Looped Transformers offer a promising alternative to purely feed-forward computation by iteratively refining latent representations, improving language modeling and reasoning. Yet recurrent architectures remain unstable to train, costly to optimize and deploy, and constrained to small, fixed recurrence depths. We introduce Attractor Models, in which a backbone module first proposes output embeddings, then an attractor module refines them by solving for the fixed point, with gradients obtained th...

---

### 11. High-arity Sample Compression

**Authors:** Leonardo N. Coregliano, William Opich

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12465v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12465v1)

**Summary:** Recently, a series of works have started studying variations of concepts from learning theory for product spaces, which can be collected under the name high-arity learning theory. In this work, we consider a high-arity variant of sample compression schemes and we prove that the existence of a high-arity sample compression scheme of non-trivial quality implies high-arity PAC learnability.

---

### 12. Search Your Block Floating Point Scales!

**Authors:** Tanmaey Gupta, Hayden Prairie, Xiaoxia Wu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12464v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12464v1)

**Summary:** Quantization has emerged as a standard technique for accelerating inference for generative models by enabling faster low-precision computations and reduced memory transfers. Recently, GPU accelerators have added first-class support for microscaling Block Floating Point (BFP) formats. Standard BFP algorithms use a fixed scale based on the maximum magnitude of the block. We observe that this scale choice can be suboptimal with respect to quantization errors. In this work, we propose ScaleSearch, a...

---

### 13. Towards Affordable Energy: A Gymnasium Environment for Electric Utility Demand-Response Programs

**Authors:** Jose E. Aguilar Escamilla, Lingdong Zhou, Xiangqi Zhu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12462v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12462v1)

**Summary:** Extreme weather and volatile wholesale electricity markets expose residential consumers to catastrophic financial risks, yet demand response at the distribution level remains an underutilized tool for grid flexibility and energy affordability. While a demand-response program can shield consumers by issuing financial credits during high-price periods, optimizing this sequential decision-making process presents a unique challenge for reinforcement learning despite the plentiful offline historical ...

---

### 14. A proximal gradient algorithm for composite log-concave sampling

**Authors:** Linghai Liu, Sinho Chewi

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12461v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12461v1)

**Summary:** We propose an algorithm to sample from composite log-concave distributions over $\mathbb{R}^d$, i.e., densities of the form $π\propto e^{-f-g}$, assuming access to gradient evaluations of $f$ and a restricted Gaussian oracle (RGO) for $g$. The latter requirement means that we can easily sample from the density $\text{RGO}_{g,h,y}(x) \propto \exp(-g(x) -\frac{1}{2h}||y-x||^2)$, which is the sampling analogue of the proximal operator for $g$. If $f + g$ is $α$-strongly convex and $f$ is $β$-smooth...

---

### 15. Multi-Stream LLMs: Unblocking Language Models with Parallel Streams of Thoughts, Inputs and Outputs

**Authors:** Guinan Su, Yanwu Yang, Xueyan Li, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12460v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12460v1)

**Summary:** The continued improvements in language model capability have unlocked their widespread use as drivers of autonomous agents, for example in coding or computer use applications. However, the core of these systems has not changed much since early instruction-tuned models like ChatGPT. Even advanced AI agents function on message exchange formats, successively exchanging messages with users, systems, with itself (i.e. chain-of-thought) and tools in a single stream of computation. This bottleneck to a...

---

### 16. TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection

**Authors:** Tom Sander, Hongyan Chang, Tomáš Souček, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12456v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12456v1)

**Summary:** We introduce TextSeal, a state-of-the-art watermark for large language models. Building on Gumbel-max sampling, TextSeal introduces dual-key generation to restore output diversity, along with entropy-weighted scoring and multi-region localization for improved detection. It supports serving optimizations such as speculative decoding and multi-token prediction, and does not add any inference overhead. TextSeal strictly dominates baselines like SynthID-text in detection strength and is robust to di...

---

### 17. Enabling AI-Native Mobility in 6G: A Real-World Dataset for Handover, Beam Management, and Timing Advance

**Authors:** Mannam Veera Narayana, Rohit Singh, Deepa M. R, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12453v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12453v1)

**Summary:** To address the issues of high interruption time and measurement report overhead under user equipment (UE) mobility especially in high speed 5G use cases the use of AI/ML techniques (AI/ML beam management and mobility procedures) have been proposed. These techniques rely heavily on data that are most often simulated for various scenarios and do not accurately reflect real deployment behavior or user traffic patterns. Therefore, there is an utmost need for realistic datasets under various conditio...

---

### 18. ORCE: Order-Aware Alignment of Verbalized Confidence in Large Language Models

**Authors:** Chen Li, Xiaoling Hu, Songzhu Zheng, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12446v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12446v1)

**Summary:** Large language models (LLMs) often produce answers with high certainty even when they are incorrect, making reliable confidence estimation essential for deployment in real-world scenarios. Verbalized confidence, where models explicitly state their confidence in natural language, provides a flexible and user-facing uncertainty signal that can be applied even when token logits are unavailable. However, existing verbalized-confidence methods often optimize answer generation and confidence generatio...

---

### 19. Environment-Adaptive Preference Optimization for Wildfire Prediction

**Authors:** Enyi Jiang, Wu Sun

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12435v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12435v1)

**Summary:** Predicting rare extreme events such as wildfires from meteorological data requires models that remain reliable under evolving environmental conditions. This problem is inherently long-tailed: wildfire events are rare but high-impact, while most observations correspond to non-fire conditions, causing standard learning objectives to underemphasize the minority class (fire) that matters most. In addition, models trained on historical distributions often fail under distribution shifts, exhibiting de...

---

### 20. Learning Minimally Rigid Graphs with High Realization Counts

**Authors:** Oleksandr Slyvka, Jan Rubeš, Rodrigo Alves, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12427v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12427v1)

**Summary:** For minimally rigid graphs, the same edge-length data can admit multiple realizations (up to translations and rotations). Finding graphs with exceptionally many realizations is an extremal problem in rigidity theory, but exhaustive search quickly becomes infeasible due to the super-exponential growth of the number of candidate graphs and the high cost of realization-count evaluation. We propose a reinforcement-learning approach that constructs minimally rigid graphs via 0- and 1-extensions, also...

---

### 21. ORBIT: Preserving Foundational Language Capabilities in GenRetrieval via Origin-Regulated Merging

**Authors:** Neha Verma, Nikhil Mehta, Shao-Chuan Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12419v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12419v1)

**Summary:** Despite the rapid advancements in large language model (LLM) development, fine-tuning them for specific tasks often results in the catastrophic forgetting of their general, language-based reasoning abilities. This work investigates and addresses this challenge in the context of the Generative Retrieval (GenRetrieval) task. During GenRetrieval fine-tuning, we find this forgetting occurs rapidly and correlates with the distance between the fine-tuned and original model parameters. Given these obse...

---

### 22. Aligning Flow Map Policies with Optimal Q-Guidance

**Authors:** Christos Ziakas, Alessandra Russo, Avishek Joey Bose

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12416v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12416v1)

**Summary:** Generative policies based on expressive model classes, such as diffusion and flow matching, are well-suited to complex control problems with highly multimodal action distributions. Their expressivity, however, comes at a significant inference cost: generating each action typically requires simulating many steps of the generative process, compounding latency across sequential decision-making rollouts. We introduce flow map policies, a novel class of generative policies designed for fast action ge...

---

### 23. Stories in Space: In-Context Learning Trajectories in Conceptual Belief Space

**Authors:** Eric Bigelow, Raphaël Sarfati, Daniel Wurgaft, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12412v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12412v1)

**Summary:** Large Language Models (LLMs) update their behavior in context, which can be viewed as a form of Bayesian inference. However, the structure of the latent hypothesis space over which this inference operates remains unclear. In this work, we propose that LLMs assign beliefs over a low-dimensional geometric space - a conceptual belief space - and that in-context learning corresponds to a trajectory through this space as beliefs are updated over time. Using story understanding as a natural setting fo...

---

### 24. Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling

**Authors:** Eilam Shapira, Moshe Tennenholtz, Roi Reichart

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12411v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12411v1)

**Summary:** AI agents negotiate and transact in natural language with unfamiliar counterparts: a buyer bot facing an unknown seller, or a procurement assistant negotiating with a supplier. In such interactions, the counterpart's LLM, prompts, control logic, and rule-based fallbacks are hidden, while each decision can have monetary consequences. We ask whether an agent can predict an unfamiliar counterpart's next decision from a few interactions. To avoid real-world logging confounds, we study this problem i...

---

### 25. Model-based Bootstrap of Controlled Markov Chains

**Authors:** Ziwei Su, Imon Banerjee, Diego Klabjan

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12410v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12410v1)

**Summary:** We propose and analyze a model-based bootstrap for transition kernels in finite controlled Markov chains (CMCs) with possibly nonstationary or history-dependent control policies, a setting that arises naturally in offline reinforcement learning (RL) when the behavior policy generating the data is unknown. We establish distributional consistency of the bootstrap transition estimator in both a single long-chain regime and the episodic offline RL regime. The key technical tools are a novel bootstra...

---

### 26. OGLS-SD: On-Policy Self-Distillation with Outcome-Guided Logit Steering for LLM Reasoning

**Authors:** Yuxiao Yang, Xiaoyun Wang, Weitong Zhang

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12400v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12400v1)

**Summary:** We study {on-policy self-distillation} (OPSD), where a language model improves its reasoning ability by distilling privileged teacher distributions along its own on-policy trajectories. Despite the performance gains of OPSD, we identify a common but often overlooked mismatch between teacher and student responses: self-reflected teacher responses can be shifted by reflection-induced bias and response templates, leading to miscalibrated token-level supervision. To mitigate this issue, we propose \...

---

### 27. Detecting overfitting in Neural Networks during long-horizon grokking using Random Matrix Theory

**Authors:** Hari K. Prakash, Charles H Martin

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12394v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12394v1)

**Summary:** Training Neural Networks (NNs) without overfitting is difficult; detecting that overfitting is difficult as well. We present a novel Random Matrix Theory method that detects the onset of overfitting in deep learning models without access to train or test data. For each model layer, we randomize each weight matrix element-wise, $\mathbf{W} \to \mathbf{W}_{\mathrm{rand}}$, fit the randomized empirical spectral distribution with a Marchenko-Pastur distribution, and identify large outliers that viol...

---

### 28. Trajectory-Agnostic Asteroid Detection in TESS with Deep Learning

**Authors:** Brian P. Powell, Jorge Martinez-Palomera, Amy Tuson, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12391v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12391v1)

**Summary:** We present a novel method for extracting moving objects from TESS data using machine learning. Our approach uses two stacked 3D U-Nets with skip connections, which we call a W-Net, to filter background and identify pixels containing moving objects in TESS image time-series data. By augmenting the training data through rotation of the image cubes, our method is robust to differences in speed and direction of asteroids, requiring no assumptions for either parameter range which are typically requir...

---

### 29. SEMIR: Semantic Minor-Induced Representation Learning on Graphs for Visual Segmentation

**Authors:** Luke James Miller, Yugyung Lee

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12389v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12389v1)

**Summary:** Segmenting small and sparse structures in large-scale images is fundamentally constrained by voxel-level, lattice-bound computation and extreme class imbalance -- dense, full-resolution inference scales poorly and forces most pipelines to rely on fixed regionization or downsampling, coupling computational cost to image resolution and attenuating boundary evidence precisely where minority structures are most informative. We introduce SEMIR (Semantic Minor-Induced Representation Learning), a repre...

---

### 30. Events as Triggers for Behavioral Diversity in Multi-Agent Reinforcement Learning

**Authors:** Hannes Büchi, Manon Flageat, Eduardo Sebastián, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12388v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12388v1)

**Summary:** Effective multi-agent cooperation requires agents to adopt diverse behaviors as task conditions evolve-and to do so at the right moment. Yet, current Multi-Agent Reinforcement Learning (MARL) frameworks that facilitate this diversity are still limited by the fact that they bind fixed behaviors to fixed agent identities. Consequently, they are ill-equipped for tasks where agents need to take on different roles at very specific moments in time. We argue that, to define these behavioral transitions...

---

### 31. A Semi-Supervised Framework for Speech Confidence Detection using Whisper

**Authors:** Adam Wynn, Jingyun Wang

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12387v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12387v1)

**Summary:** Automatic detection of speaker confidence is critical for adaptive computing but remains constrained by limited labelled data and the subjectivity of paralinguistic annotations. This paper proposes a semi-supervised hybrid framework that fuses deep semantic embeddings from the Whisper encoder with an interpretable acoustic feature vector composed of eGeMAPS descriptors and auxiliary probability estimates of vocal stress and disfluency. To mitigate reliance on scarce ground truth data, we introdu...

---

### 32. Scalable Token-Level Hallucination Detection in Large Language Models

**Authors:** Rui Min, Tianyu Pang, Chao Du, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12384v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12384v1)

**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities, but they still frequently produce hallucinations. These hallucinations are difficult to detect in reasoning-intensive tasks, where the content appears coherent but contains errors like logical flaws and unreliable intermediate results. While step-level analysis is commonly used to detect internal hallucinations, it suffers from limited granularity and poor scalability due to its reliance on step segmentation. To address thes...

---

### 33. Trust the Batch, On- or Off-Policy: Adaptive Policy Optimization for RL Post-Training

**Authors:** Rasool Fakoor, Murdock Aubry, Nicholas Stranges, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12380v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12380v1)

**Summary:** Reinforcement learning is structurally harder than supervised learning because the policy changes the data distribution it learns from. The resulting fragility is especially visible in large-model training, where the training and rollout systems differ in numerical precision, sampling, and other implementation details. Existing methods manage this fragility by adding hyper-parameters to the training objective, which makes the algorithm more sensitive to its configuration and requires retuning wh...

---

### 34. Discrete Flow Matching for Offline-to-Online Reinforcement Learning

**Authors:** Fairoz Nower Khan, Nabuat Zaman Nahim, Peizhong Ju

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12379v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12379v1)

**Summary:** Many reinforcement learning (RL) tasks have discrete action spaces, but most generative policy methods based on diffusion and flow matching are designed for continuous control. Meanwhile, generative policies usually rely heavily on offline datasets and offline-to-online RL is itself challenging, as the policy must improve from new interaction without losing useful behavior learned from static data. To address those challenges, we introduce DRIFT, an online fine-tuning method that updates an offl...

---

### 35. Agent-Based Post-Hoc Correction of Agricultural Yield Forecasts

**Authors:** Matthew Beddows, Aiden Durrant, Georgios Leontidis

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12375v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12375v1)

**Summary:** Accurate crop yield forecasting in commercial soft fruit production is constrained by the data available in typical commercial farm records, which lack the sensor networks, satellite imagery, and high-resolution meteorological inputs that most state-of-the-art approaches assume. We propose a structured LLM agent framework that performs post-hoc correction of existing model predictions, encoding agricultural domain knowledge across tools for phase detection, bias learning, and range validation. E...

---

### 36. Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models

**Authors:** Yanting Miao, Yutao Sun, Dexin Wang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12374v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12374v1)

**Summary:** Visual latent reasoning lets a multimodal large language model (MLLM) create intermediate visual evidence as continuous tokens, avoiding external tools or image generators. However, existing methods usually follow an output-as-input latent paradigm and yield unstable gains. We identify evidence for a feature-space mismatch that can contribute to this instability: dominant visual-latent models build on pre-norm MLLMs and reuse decoder hidden states as predicted latent inputs, even though these st...

---

### 37. MetaColloc: Optimization-Free PDE Solving via Meta-Learned Basis Functions

**Authors:** Zichuan Yang

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12368v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12368v1)

**Summary:** Solving partial differential equations (PDEs) with machine learning typically requires training a new neural network for every new equation. This optimization is slow. We introduce MetaColloc. It is an optimization-free and data-free framework that removes this bottleneck completely. We decouple basis discovery from the solving process. We meta-train a dual-branch neural network on diverse Gaussian Random Fields. This offline process creates a universal dictionary of neural basis functions. At t...

---

### 38. Attacks and Mitigations for Distributed Governance of Agentic AI under Byzantine Adversaries

**Authors:** Matthew D. Laws, Alina Oprea, Cristina Nita-Rotaru

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12364v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12364v1)

**Summary:** Agentic AI governance is a critical component of agentic AI infrastructure ensuring that agents follow their owner's communication and interaction policies, and providing protection against attacks from malicious agents. The state-of-the-art solution, SAGA, assumes a logically centralized point of trust, the Provider, which serves as a repository for user and agent information and actively enforces policies. While SAGA provides protection against malicious agents, it remains vulnerable to a mali...

---

### 39. From Message-Passing to Linearized Graph Sequence Models

**Authors:** Joël Mathys, Basil Rohner, Saku Peltonen, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12358v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12358v1)

**Summary:** Message-passing based approaches form the default backbone of most learning architectures on graph-structured data. However, the rapid progress of modern deep learning architectures in other domains, particularly sequence modeling, raises the question of how graph learning can benefit from these advances. We introduce Linearized Graph Sequence Models, a framework that recasts message-passing graph computation from the perspective of sequence modeling to simplify architectural choices. Our approa...

---

### 40. A New Technique for AI Explainability using Feature Association Map

**Authors:** Sayantani Ghosh, Amit Kumar Das, Amlan Chakrabarti

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12350v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12350v1)

**Summary:** Lack of transparency in AI systems poses challenges in critical real-life applications. It is important to be able to explain the decisions of an AI system to ensure trust on the system. Explainable AI (XAI) algorithms play a vital role in achieving this objective. In this paper, we are proposing a new algorithm for Explaining AI systems, FAMeX (Feature Association Map based eXplainability). The proposed algorithm is based on a graph-theoretic formulation of the feature set termed as Feature Ass...

---

### 41. Neural-Schwarz Tiling for Geometry-Universal PDE Solving at Scale

**Authors:** Paolo Secchi, Daniel S. Balint, Marco Maurizi

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12343v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12343v1)

**Summary:** Most learned PDE solvers follow a global-surrogate paradigm: a neural operator is trained to map full problem descriptions to full solution fields for a prescribed distribution of geometries, boundary conditions, and coefficients. This has enabled fast inference within fixed problem families, but limits reuse across new domains and makes large-scale deployment dependent on expensive problem-specific data generation. We introduce $\textbf{NEST}$ ($\textbf{Ne}$ural-$\textbf{S}$chwarz $\textbf{T}$i...

---

### 42. Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting

**Authors:** Laura Lützow, Simone Garatti, Marco C. Campi, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12341v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12341v1)

**Summary:** Conformal prediction constructs prediction sets with finite-sample coverage guarantees, but its calibration stage is structurally constrained to a scalar score function and a single threshold variable - forcing shapes of prediction sets to be fixed before calibration, typically through data splitting. We introduce multi-variable conformal prediction (MCP), a framework that extends conformal prediction to vector-valued score functions with multiple simultaneous calibration variables. Building on ...

---

### 43. Online Learning-to-Defer with Varying Experts

**Authors:** Dang Hoang Duy, Yannis Montreuil, Maxime Meyer, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12340v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12340v1)

**Summary:** Learning-to-Defer (L2D) methods route each query either to a predictive model or to external experts. While existing work studies this problem in batch settings, real-world deployments require handling streaming data, changing expert availability, and shifting expert distribution. We introduce the first online L2D algorithm for multiclass classification with bandit feedback and a dynamically varying pool of experts. Our method achieves regret guarantees of $O((n+n_e)T^{2/3})$ in general and $O((...

---

### 44. BSO: Safety Alignment Is Density Ratio Matching

**Authors:** Tien-Phat Nguyen, Truong Nguyen, Thin Nguyen, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12339v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12339v1)

**Summary:** Aligning language models for both helpfulness and safety typically requires complex pipelines-separate reward and cost models, online reinforcement learning, and primal-dual updates. Recent direct preference optimization approaches simplify training but incorporate safety through ad-hoc modifications such as multi-stage procedures or heuristic margin terms, lacking a principled derivation. We show that the likelihood ratio of the optimal safe policy admits a closed-form decomposition that reduce...

---

### 45. Manifold Sampling via Entropy Maximization

**Authors:** Cornelius V. Braun, Tilman Burghoff, Marc Toussaint

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12338v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12338v1)

**Summary:** Sampling from constrained distributions has a wide range of applications, including in Bayesian optimization and robotics. Prior work establishes convergence and feasibility guarantees for constrained sampling, but assumes that the feasible set is connected. However, in practice, the feasible set often decomposes into multiple disconnected components, which makes efficient sampling under constraints challenging. In this paper, we propose MAnifold Sampling via Entropy Maximization (MASEM) for sam...

---

### 46. EHR-RAGp: Retrieval-Augmented Prototype-Guided Foundation Model for Electronic Health Records

**Authors:** Saeed Shurrab, Mariam Al-Omari, Dana El Samad, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12335v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12335v1)

**Summary:** Electronic Health Records (EHR) contain rich longitudinal patient information and are widely used in predictive modeling applications. However, effectively leveraging historical data remains challenging due to long trajectories, heterogeneous events, temporal irregularity, and the varying relevance of past clinical context. Existing approaches often rely on fixed windows or uniform aggregation, which can obscure clinically important signals. In this work, we introduce EHR-RAGp, a retrieval-augme...

---

### 47. Grid Games: The Power of Multiple Grids for Quantizing Large Language Models

**Authors:** Vage Egiazarian, Erik Schultheis, Andrei Panferov, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12327v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12327v1)

**Summary:** A major recent advance in quantization is given by microscaled 4-bit formats such as NVFP4 and MXFP4, quantizing values into small groups sharing a scale, assuming a fixed floating-point grid. In this paper, we study the following natural extension: assume that, for each group of values, we are free to select the "better" among two or more 4-bit grids marked by one or more bits in the scale value. We formalize the power-of-two-grids (PO2) problem, and provide theoretical results showing that pra...

---

### 48. Autoregressive Learning in Joint KL: Sharp Oracle Bounds and Lower Bounds

**Authors:** Yunbei Xu, Yuzhe Yuan, Ruohan Zhan

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12316v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12316v1)

**Summary:** We study the fundamental and timely problem of learning long sequences in autoregressive modeling and next-token prediction under model misspecification, measured by the joint Kullback--Leibler (KL) divergence. Our goal is to characterize how the sequence horizon \(H\) affects both approximation and estimation errors in this joint-distribution, sequence-level regime. By establishing matching upper and lower bounds, we provide, to our knowledge, the first complete characterization of long-horizon...

---

### 49. Transferable Delay-Aware Reinforcement Learning via Implicit Causal Graph Modeling

**Authors:** Chenran Zhao, Dianxi Shi, Yaowen Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12312v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12312v1)

**Summary:** Random delays weaken the temporal correspondence between actions and subsequent state feedback, making it difficult for agents to identify the true propagation process of action effects. In cross-task scenarios, changes in task objectives and reward formulations further reduce the reusability of previously acquired task knowledge. To address this problem, this paper proposes a transferable delay-aware reinforcement learning method based on implicit causal graph modeling. The proposed method uses...

---

### 50. In-context learning to predict critical transitions in dynamical systems

**Authors:** Yunus Sevinchan, Juan Nathaniel, Kai Ueltzhöffer, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12308v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12308v1)

**Summary:** Critical transitions - abrupt, often irreversible changes in system dynamics - arise across human and natural systems, often with catastrophic consequences. Real-world observations of such shifts remain scarce, preventing the development of reliable early warning systems. Conventional statistical and spectral indicators, such as increasing variance, tend to fail under realistic conditions of limited data and correlated noise, whereas existing deep learning classifiers do not extrapolate beyond t...

---

## cs.NE

**50 papers**

### 1. Solve the Loop: Attractor Models for Language and Reasoning

**Authors:** Jacob Fein-Ashley, Paria Rashidinejad

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12466v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12466v1)

**Summary:** Looped Transformers offer a promising alternative to purely feed-forward computation by iteratively refining latent representations, improving language modeling and reasoning. Yet recurrent architectures remain unstable to train, costly to optimize and deploy, and constrained to small, fixed recurrence depths. We introduce Attractor Models, in which a backbone module first proposes output embeddings, then an attractor module refines them by solving for the fixed point, with gradients obtained th...

---

### 2. A Family of Quaternion-Valued Differential Evolution Algorithms for Numerical Function Optimization

**Authors:** Gerardo Altamirano-Gomez, Álvaro Gallardo, Carlos Ignacio Hernández Castellanos

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12362v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12362v1)

**Summary:** The numerical optimization of continuous functions is a fundamental task in many scientific and engineering domains, ranging from mechanical design to training of artificial intelligence models. Among the most effective and widely used algorithms for this purpose is Differential Evolution (DE), known for its simplicity and strong performance. Recent research has shown that adapting AI models to operate over alternative number systems-such as complex numbers, quaternions, and geometric algebras-c...

---

### 3. Black-Box Optimization of Mixed Binary-Continuous Variables: Challenges and Opportunities in Evolutionary Model Merging

**Authors:** Md. Robiul Islam Niloy

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12326v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12326v1)

**Summary:** Model merging has emerged as a cost-effective alternative to training large language models (LLMs) from scratch, enabling researchers to combine pre-trained models into more capable systems without full retraining. Evolutionary approaches to model merging have shown particular promise, automatically searching for optimal merging configurations across both parameter space (PS) and data flow space (DFS). However, the optimization challenges underlying these approaches -- particularly in DFS mergin...

---

### 4. Graph-Grounded Optimization: Rao-Family Metaheuristics, Classical OR, and SLM-Driven Formulation over Knowledge Graphs

**Authors:** Madhulatha Mandarapu, Sandeep Kunkunuru

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12204v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12204v1)

**Summary:** We propose graph-grounded optimization: a paradigm in which the decision variables, constraints, and objective coefficients of a real-world optimization problem are sourced from a property knowledge graph (KG) via Cypher queries, rather than supplied as free-form natural-language text or static tabular input. We motivate the paradigm by surveying recent LLM/SLM-driven optimization systems -- OptiMUS, Chain-of-Experts, LLMOPT, OPRO, FunSearch, Eureka -- none of which consume property graphs as th...

---

### 5. Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons

**Authors:** Aaron Spieler, Georg Martius, Anna Levina

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12049v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12049v1)

**Summary:** Cortical neurons are complex, multi-timescale processors wired into recurrent circuits, shaped by long evolutionary pressure under stringent biological constraints. Mainstream machine learning, by contrast, predominantly builds models from extremely simple units, a default inherited from early neural-network theory. We treat this as a normative architectural question. How should one split a fixed parameter budget $P$ between the number of units $N$, per-unit effective complexity $k_e$, and per-u...

---

### 6. Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing

**Authors:** Alex Fulleda-Garcia, Saray Soldado-Magraner, Josep Maria Margarit-Taulé

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11835v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11835v1)

**Summary:** Spiking neural networks (SNNs) promise low-power event-driven computation for temporally rich tasks, but commonly used neuron models often trade off gradient-based trainability, dynamical richness, and high activity sparsity. These limitations are acute in regression, where approximation error, noise and spike discretization can severely degrade continuous-valued outputs. Indeed, many state-of-the-art (SOTA) SNNs rely on simple phenomenological dynamics trained with surrogate gradients and offer...

---

### 7. Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization

**Authors:** Zhaotian Gu, Molan Li, Jie Su, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11718v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11718v1)

**Summary:** The spatial and functional organization of the primate visual cortex is a fundamental problem in neuroscience. While recent computational frameworks like the Topographic Deep Artificial Neural Network (TDANN) have successfully modeled spatial organization in the ventral stream, the computational origins of the dorsal stream's distinct topographies, such as direction-selective maps in the middle temporal (MT) area, remain largely unresolved. In this work, we present a spatiotemporal TDANN to inve...

---

### 8. Leveraging Non-Equilibrium ECRAM Dynamics for Short-Term Plasticity in Neuromorphic Circuits

**Authors:** Alex Currie, Sean Borkholder, Nithil Harris Manimaran, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11243v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11243v1)

**Summary:** Short-term plasticity (STP) is fundamental to temporal information processing in biological neural systems but remains difficult to realize efficiently in neuromorphic hardware. Memristive electrochemical random-access memory (ECRAM) devices naturally exhibit non-equilibrium ionic dynamics that produce transient conductance modulation; however, these behaviors are typically treated as undesirable variability or tolerated as side effects in memory-centric computing paradigms. In this work, we ins...

---

### 9. On the Impact of Crossover in Many-Objective Optimization: A Runtime Analysis of NSGA-III

**Authors:** Andre Opris

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11201v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11201v1)

**Summary:** In recent years, a theoretical understanding has rapidly advanced regarding how popular multi-objective evolutionary algorithms (MOEAs) can optimize many-objective problems. However, the benefits of using crossover in many-objective optimization are theoretically not understood, except for specifically designed benchmark functions tuned to particular crossover operators, and still lag significantly behind its practical use. In this paper, we build upon this line of research and present a theoret...

---

### 10. Decomposing Evolutionary Mixture-of-LoRA Architectures: The Routing Lever, the Lifecycle Penalty, and a Substrate-Conditional Boundary

**Authors:** Ramchand Kumaresan

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11153v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11153v1)

**Summary:** We decompose an evolutionary mixture-of-LoRA system on a from-scratch ~150M-parameter widened-D substrate (D=1536, V=32000; D/V approx 0.048; the "widened-1536" substrate) into three factors -- a router rewrite (parallel sigmoid gate with learnable per-adapter floor and bounded temperature anneal, fed post-stack hidden states rather than token-embedding means), a per-domain leave-one-out evaluation scope, and a lifecycle of death plus alpha-blend inheritance plus SVD mutation plus slot reallocat...

---

### 11. Energy-Efficient Implementation of Spiking Recurrent Cells on FPGA

**Authors:** Pascal Harmeling, Florent De Geeter, Guillaume Drion

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10679v2) | 📄 [PDF](https://arxiv.org/pdf/2605.10679v2)

**Summary:** Spiking Neural Networks (SNNs) can reduce energy consumption compared to conventional Artificial Neural Networks (ANNs) when spiking activity is sparse and the neuron model is hardware-friendly. However, biologically faithful models are often too costly to implement on FPGAs, whereas very simple models (e.g., IR/LIF) sacrifice part of the neuronal dynamics. In this work, we present an FPGA accelerator for an SNN using Spiking Recurrent Cell (SRC) neurons, providing a trade-off between biological...

---

### 12. A Theory of Multilevel Interactive Equilibrium in NeuroAI

**Authors:** Zhe Sage Chen, Quanyan Zhu

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10505v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10505v1)

**Summary:** We propose a game-theoretic framework for adaptive multi-agent intelligent systems. Unlike classical game theory, which often treats strategies as primitive objects chosen by perfectly rational agents, the proposed framework provides a mathematical foundation for studying equilibrium in NeuroAI and can be viewed as an extension of game theory under relaxed assumptions, including partial observability, bounded computation, and uncertainty. At its core, Multilevel Interactive Equilibrium (MIE) gen...

---

### 13. Causal Explanations from the Geometric Properties of ReLU Neural Networks

**Authors:** Hector Woods, Philippa Ryan, Rob Alexander

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10396v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10396v1)

**Summary:** Neural networks have proved an effective means of learning control policies for autonomous systems, but these learned policies are difficult to understand due to the black-box nature of neural networks. This lack of interpretability makes safety assurance for such autonomous systems challenging. The fields of eXplainable Artificial Intelligence (XAI) and eXplainable Reinforcement Learning (XRL) aim to interpret the decision making processes of neural networks and autonomous agents, respectively....

---

### 14. Meta-Black-Box Optimization Can Do Search Guidance for Expensive Constrained Multi-Objective Optimization

**Authors:** Yukun Du, Haiyue Yu, Jiang Jiang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10260v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10260v1)

**Summary:** Existing Meta-Black-Box Optimization (MetaBBO) methods focus on how to search when controlling optimizers, but largely overlook where to search. We propose MetaSG-SAEA, a bi-level MetaBBO framework for expensive constrained multi-objective optimization problems (ECMOPs), in which a meta-policy provides search guidance to the low-level Surrogate-Assisted Evolutionary Algorithm (SAEA). To achieve this, we introduce Max-Min Constraint-Calibrated Inequality (MM-CCI), a compact, problem-agnostic regi...

---

### 15. Joint sparse coding and temporal dynamics support context reconfiguration

**Authors:** Qianqian Shi, Yue Che, Faqiang Liu, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10178v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10178v1)

**Summary:** Adaptive behavior requires the brain to transition between distinct contexts while maintaining representations of prior experience. The ability to reconfigure neural representations without erasing previously acquired knowledge is central to learning in dynamic environments, yet the neural mechanisms that support this balance remain unclear. Understanding these mechanisms is also critical for addressing catastrophic forgetting in artificial systems designed for lifelong learning. Here, we identi...

---

### 16. Prospective Compression in Human Abstraction Learning

**Authors:** Leonardo Hernandez Cano, Ivan Zareski, Luisa El Amouri, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09985v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09985v1)

**Summary:** A core challenge in program synthesis is online library learning: the incremental acquisition of reusable abstractions under uncertainty about future task demands. Existing algorithms treat library learning as retrospective compression over a static task distribution, where the learned library is determined by the corpus of past tasks. However, real-world learning domains are often non-stationary, with tasks arising from a generative process that evolves over time. We propose and test the hypoth...

---

### 17. Frequency Matching in Spiking Neural Networks for mmWave Sensing

**Authors:** Di Yu, Zhenyu Liao, Changze Lv, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09983v1)

**Summary:** Millimeter-wave (mmWave) sensing enables privacy-preserving, always-on edge perception, but its measurements are often sparse, temporally irregular, and corrupted by high-frequency noise. Existing mmWave pipelines predominantly rely on artificial neural networks (ANNs), which achieve robustness through extensive preprocessing or deep architectures, thereby limiting their efficiency on edge devices. In this work, we study spiking neural networks (SNNs) for mmWave sensing from a mechanism-data ali...

---

### 18. Parameter-Efficient Neuroevolution for Diverse LLM Generation: Quality-Diversity Optimization via Prompt Embedding Evolution

**Authors:** Dongxin Guo, Jikun Wu, Siu Ming Yiu

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09781v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09781v1)

**Summary:** Large Language Models exhibit mode collapse, producing homogeneous outputs that fail to explore valid solution spaces. We present QD-LLM, a framework for parameter-efficient neuroevolution that evolves prompt embeddings, compact neural interfaces (~32K parameters) that steer generation in frozen LLMs (70B+ parameters), within a Quality-Diversity (QD) optimization framework. Our contributions: (1) evolved prompt embeddings via gradient-free optimization enabling behavioral steering without model ...

---

### 19. EvoPref: Multi-Objective Evolutionary Optimization Discovers Diverse LLM Alignments Beyond Gradient Descent

**Authors:** Dongxin Guo, Jikun Wu, Siu Ming Yiu

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09777v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09777v1)

**Summary:** Gradient-based preference optimization methods for large language model (LLM) alignment suffer from preference collapse, converging to narrow behavioral modes while neglecting preference diversity. We introduce EvoPref, a multi-objective evolutionary algorithm that maintains populations of Low-Rank Adaptation (LoRA) adapters optimized across helpfulness, harmlessness, and honesty objectives using Non-dominated Sorting Genetic Algorithm II (NSGA-II) selection with archive-based diversity preserva...

---

### 20. Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets

**Authors:** Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09770v1)

**Summary:** Spike-based encodings are sparse and energy-efficient, but have largely been formulated probabilistically, disconnected from most signal processing literature. We recast spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds. The proposed wavelets preserve the sparsity and locality of spiking representations, with reconstruction up to spike quantization and time discretization. We demonstrate reconstruction on ECG and audio datasets, achieving a...

---

### 21. LEVI: Stronger Search Architectures Can Substitute for Larger LLMs in Evolutionary Search

**Authors:** Temoor Tanveer

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09764v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09764v1)

**Summary:** LLM-guided evolutionary methods such as AlphaEvolve have proven effective in domains like math, systems research, and algorithmic discovery, but their reliance on frontier models makes each run expensive. We argue this is largely an artifact of how existing frameworks allocate search: archives that fail to preserve solution diversity force compensation through stronger mutation models; blind model use spends frontier dollars on local edits a smaller model could handle; and full-set evaluation wa...

---

### 22. Discovery of Nonlinear Dynamics with Automated Basis Function Generation

**Authors:** Mohammad Amin Basiri, Charles Nicholson

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09696v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09696v1)

**Summary:** Discovering governing equations from observational data remains a fundamental challenge in scientific modeling, particularly when the underlying mathematical structure is unknown. Traditional sparse identification methods like SINDy excel at discovering parsimonious models but require researchers to specify candidate basis functions a priori, a limitation that often leads to model failure when critical terms are omitted or when systems exhibit unconventional dynamics. Purely symbolic regression ...

---

### 23. RDEx-CASK: Cauchy Mutation, Archive, and Stagnation Kick for RDEx-CSOP

**Authors:**  Dikshant, Dikshit Chauhan, Chen Hao, et al.

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09652v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09652v1)

**Summary:** We extend RDEx-CSOP with 3 changes that target stagnation & late-stage variance, plus minor parameter tuning. The second scale factor in the standard branch is sampled independently from a truncated Cauchy. A small feasible-only JADE-style archive (|A|_max = 50) is added & sampled with probability |A|/(|A|+|P|). Per-individual stagnation counter triggers, after 180 no-improvement generations, three local overrides on standard branch: pull toward the global best, lift the archive sampling floor t...

---

### 24. Neuromorphic Reinforcement Learning for Quadruped Locomotion Control on Uneven Terrain

**Authors:** Zhuangyu Han, Abhronil Sengupta

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09595v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09595v1)

**Summary:** Reinforcement learning (RL) has enabled robust quadruped locomotion over complex terrain, but most learned controllers are trained offline with backpropagation in massively parallel simulation and deployed as fixed policies, limiting adaptation to terrain variation, payload changes, actuator wear, and other real-world conditions under onboard power constraints. Local learning provides a potential path toward energy-aware on-robot adaptation by replacing global backpropagation graphs with updates...

---

### 25. Sparsity Moves Computation: How FFN Architecture Reshapes Attention in Small Transformers

**Authors:** Gabriel Smithline, Chris Mascioli

**Published:** 2026-05-10

🔗 [Paper](http://arxiv.org/abs/2605.09403v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09403v1)

**Summary:** Architectural choices inside the Transformer feedforward network (FFN) block do not merely affect the block itself; they reshape the computations learned by the rest of the model. We study this effect in one-layer Transformers trained on digit addition with carry, modular arithmetic, and histogram counting. Comparing dense FFNs, gated linear units (GLUs), mixture-of-experts (MoE), and MoE-GLUs, we find that sparse MoE routing can shift computation from FFN to attention, with the strongest ablati...

---

### 26. Evolutionary Ensemble of Agents

**Authors:** Zongmin Yu, Liu Yang

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.09018v1) | 📄 [PDF](https://arxiv.org/pdf/2605.09018v1)

**Summary:** We introduce Evolutionary Ensemble (EvE), a decentralized framework that organizes existing, highly capable coding agents into a live, co-evolving system for algorithmic discovery. Rather than reinventing the wheel within the "LLMs as optimizers" paradigm, EvE fixes the base agent substrate and focuses entirely on evolving the cumulative guidance and skills that dictate agent behaviors. By maintaining two co-evolving populations, namely functional code solvers and agent guidance states, the syst...

---

### 27. Drain-Vortex Optimization: A Population-Based Metaheuristic Inspired by Multi-Drain Free-Vortex Flow

**Authors:** Mohsen Omidi, Brian Vaughan

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.08883v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08883v1)

**Summary:** This paper proposes Drain-Vortex Optimization (DVO), a population-based metaheuristic for continuous optimization. DVO models each candidate solution as a particle moving in a multi-drain vortex field. Its update rule decomposes motion into radial attraction toward selected drain centres and tangential rotation governed by a regularized free-vortex law. A three-phase mechanism switches between far-field exploration, spiral inward motion, and localized core exploitation according to the normalize...

---

### 28. AHD Agent: Agentic Reinforcement Learning for Automatic Heuristic Design

**Authors:** Haoze Lv, Ning Lu, Ziang Zhou, et al.

**Published:** 2026-05-09

🔗 [Paper](http://arxiv.org/abs/2605.08756v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08756v1)

**Summary:** Automatic heuristic design (AHD) has emerged as a promising paradigm for solving NP-hard combinatorial optimization problems (COPs). Recent works show that large language models (LLMs), when integrated into well-designed frameworks (i.e., LLM-AHD), can autonomously discover high-performing heuristics. However, existing LLM-AHD frameworks typically treat LLMs as passive generators within fixed workflows, where the model generates heuristics from manually designed, limited context. Such context ma...

---

### 29. Structure-Preserving Reconstruction of Convex Lipschitz Functionals on Hilbert Spaces from Finite Samples

**Authors:** Anastasis Kratsios

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08559v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08559v1)

**Summary:** Convex functionals are ubiquitous in applied analysis, appearing as value functions, risk measures, super-hedging prices, and loss functionals in machine learning. In many applications, however, the functional is only observed through finitely many exact pointwise evaluations. We ask whether a convex functional on a separable Hilbert space $H$ can be reconstructed, up to arbitrary uniform accuracy, by an explicit formula which preserves convexity and Lipschitz regularity and is finitely computab...

---

### 30. Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction

**Authors:** Himanshu Udupi, Xiaocong Yang, ChengXiang Zhai

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08022v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08022v1)

**Summary:** Spiking Neural Networks (SNNs) have been proposed as biologically plausible and energy-efficient alternatives to conventional Artificial Neural Networks (ANNs). However, the training of SNN usually relies on surrogate gradients due to the non-differentiability of the spike function, introducing approximation errors that accumulate across layers. To address this challenge, we extend the work on convexification of parallel feedforward threshold networks to parallel recurrent threshold networks, wh...

---

### 31. Broken-symmetry shape discrimination on a driven Duffing ring

**Authors:** Kaspar Anton Schindler

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07475v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07475v1)

**Summary:** Distributed computational substrates rely on two elementary operations: bundling, the act of populating a shared physical medium with independently retrievable components, and binding, the act of composing components into outputs whose identity depends on their relations. We study these two primitives on the simplest closed substrate carrying a continuous symmetry, a cycle graph of N nodes, in two parameter regimes of a single master equation of motion. The linear regime sorts a temporal input a...

---

### 32. Discovering Ordinary Differential Equations with LLM-Based Qualitative and Quantitative Evaluation

**Authors:** Sum Kyun Song, Bong Gyun Shin, Jae Yong Lee

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07323v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07323v1)

**Summary:** Discovering governing differential equations from observational data is a fundamental challenge in scientific machine learning. Existing symbolic regression approaches rely primarily on quantitative metrics; however, real-world differential equation modeling also requires incorporating domain knowledge to ensure physical plausibility. To address this gap, we propose DoLQ, a method for discovering ordinary differential equations with LLM-based qualitative and quantitative evaluation. DoLQ employs...

---

### 33. Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability

**Authors:** Dengzhe Hou, Zihao Wu, Lingyu Jiang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07212v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07212v1)

**Summary:** Electroencephalography (EEG) is a cornerstone of brain-computer interfaces and clinical neuroscience, yet deep learning models are typically trained and evaluated under a single, unreported preprocessing pipeline. We formalize preprocessing choices as a counterfactual intervention space and show that EEG predictions are surprisingly unstable under this space: across six datasets spanning four paradigms, up to 42% of trial-level predictions flip when only the preprocessing changes, a variability ...

---

### 34. Direct-to-Event Spiking Neural Network Transfer

**Authors:** Nhan Trong Luu, Duong Trung Luu, Pham Ngoc Nam, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07207v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07207v1)

**Summary:** Spiking Neural Networks (SNNs) have gained increasing attention due to their potential for low-power computation on neuromorphic hardware. A widely adopted training strategy for SNNs is direct coding, which enable backpropagation on neuron implementations using continuous-valued surrogate activations. However, recent studies have shown that direct-coded SNNs remain substantially less energy-efficient than their event-based counterparts, limiting their practical deployment in energy sensitive sce...

---

### 35. Every Feedforward Neural Network Definable in an o-Minimal Structure Has Finite Sample Complexity

**Authors:** Anastasis Kratsios, Gregory Cousins, Haitz Sáez de Ocáriz Borde, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07097v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07097v1)

**Summary:** We show that, in a precise sense, a broad class of feedforward neural networks learn (have finite sample complexity) in the PAC model: every fixed finite feedforward architecture whose layers are definable in an o-minimal structure has finite sample complexity in the agnostic PAC setting, even with unbounded parameters. This covers standard fixed-size MLPs, CNNs, GNNs, and transformers with fixed sequence length, together with the operations and layers typically used in such architectures, inclu...

---

### 36. A Unified Measure-Theoretic View of Diffusion, Score-Based, and Flow Matching Generative Models

**Authors:** Aditya Ranganath, Mukesh Singhal

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06829v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06829v1)

**Summary:** We survey continuous-time generative modeling methods based on transporting a simple reference distribution to a data distribution via stochastic or deterministic dynamics. We present a unified framework in which diffusion models, score-based generative models, and flow matching are instances of learning a time-dependent vector field that induces a family of marginals $(ρ_t)_{t \in [0,1]}$ governed by continuity and Fokker-Planck equations. Such a unified theory is timely because these methods a...

---

### 37. The Causally Emergent Alignment Hypothesis: Causal Emergence Aligns with and Predicts Final Reward in Reinforcement Learning Agents

**Authors:** Federico Pigozzi, Michael Levin

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06746v1)

**Summary:** A hallmark of life on Earth is the ability of agents to exert causal power and be drivers of subsequent events. This is key to cognition at all scales. Causal emergence, measuring the degree to which an agent exerts unique predictive power on its future, is one consequence of causal power. Indeed, recent discoveries have shown that biological agents, even minimal ones, increase their causal emergence after learning new memories. However, there is a major knowledge gap regarding how causally emer...

---

### 38. CoupleEvo: Evolving Heuristics for Coupled Optimization Problems Using Large Language Models

**Authors:** Thomas Bömer, Bastian Amberg, Max Disselnmeyer, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06341v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06341v1)

**Summary:** Many real-world optimization problems consist of multiple tightly coupled subproblems whose solutions must be coordinated to achieve high overall performance. However, existing large language model driven automated heuristic design approaches are limited to single-problem settings. In this paper, we propose CoupleEvo. CoupleEvo proposes three evolutionary coordination strategies to evolve heuristics for coupled optimization problems: the sequential strategy evolves heuristics for one subproblem ...

---

### 39. Efficient event-driven retrieval in high-capacity kernel Hopfield networks

**Authors:** Akira Tamamori

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05978v2) | 📄 [PDF](https://arxiv.org/pdf/2605.05978v2)

**Summary:** High-capacity associative memory models, such as Kernel Logistic Regression (KLR) Hopfield networks, have demonstrated strong storage capabilities but typically rely on computationally expensive synchronous updates. This reliance poses a bottleneck for deployment on energy-efficient, event-driven neuromorphic hardware. In this paper, we investigate the asynchronous retrieval dynamics of KLR Hopfield networks. We show empirically that, under appropriately tuned kernel parameters, asynchronous seq...

---

### 40. MDN: Parallelizing Stepwise Momentum for Delta Linear Attention

**Authors:** Yulong Huang, Xiang Liu, Hongxiang Huang, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05838v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05838v1)

**Summary:** Linear Attention (LA) offers a promising paradigm for scaling large language models (LLMs) to long sequences by avoiding the quadratic complexity of self-attention. Recent LA models such as Mamba2 and GDN interpret linear recurrences as closed-form online stochastic gradient descent (SGD), but naive SGD updates suffer from rapid information decay and suboptimal convergence in optimization. While momentum-based optimizers provide a natural remedy, they pose challenges in simultaneously achieving ...

---

### 41. Graph Normalization: Fast Binarizing Dynamics for Differentiable MWIS

**Authors:** Laurent Guigues

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05330v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05330v1)

**Summary:** We introduce Graph Normalization (GN), a principled dynamical system on graphs that serves as a differentiable approximation engine for the NP-hard Maximum Weight Independent Set (MWIS) problem. MWIS encompasses many combinatorial challenges, including optimal assignment, scheduling, set packing, and MAP inference in discrete Markov Random Fields. Unlike Belief Propagation, we prove GN always converges to a binary indicator of a Maximum Independent Set. GN realizes a fast quasi-Newton descent th...

---

### 42. S-LCG: Structured Linear Congruential Generator-Based Deterministic Algorithm for Search and Optimization

**Authors:** Ahmed Qasim Mohammed, Haider Banka, Anamika Singh

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05198v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05198v1)

**Summary:** This study presents a novel deterministic optimization algorithm based on a special variant of the Linear Congruential Generator (LCG). While conventional algorithms generally operate within the search space, the introduced technique follows a two-level architecture. In particular, an external loop that adaptively balances between exploration and exploitation, while the internal loop evaluates solutions. It is motivated by the intrinsic structure of the generator, the reason behind naming it the...

---

### 43. Direct From Darwin: Deriving Advanced Optimizers From Evolutionary First Principles

**Authors:** Daniel Grimmer

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05284v2) | 📄 [PDF](https://arxiv.org/pdf/2605.05284v2)

**Summary:** Evolutionary computation has long promised to deliver both high-performance optimization tools as well as rigorous scientific simulations of Darwinian evolution. However, modern algorithms frequently abandon evolutionary fidelity for physics-inspired heuristics or superficial biological metaphors. This paper derives a suite of advanced gradient-based optimization algorithms directly from evolutionary first principles. We introduce Darwinian Lineage Simulations (DLS) to prove that, in an asexual ...

---

### 44. On the Influence of the Feature Computation Budget on Per-Instance Algorithm Selection for Black-Box Optimization

**Authors:** Koen van der Blom, Diederick Vermetten

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04954v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04954v1)

**Summary:** Per-instance algorithm selection (PIAS) takes advantage of complementarity between a set of algorithms by deciding which algorithm to run on a given instance. This decision is based on features of the instances, which, in the context of black-box optimization (BBO), require a part of the optimization budget to be computed. This raises two questions: (a) from which fraction of the budget spent on feature computation does PIAS become worth it for BBO, and (b) which fraction of the budget optimizes...

---

### 45. DALight-3D: A Lightweight 3D U-Net for Brain Tumor Segmentation from Multi-Modal MRI

**Authors:** Nand Kumar Mishra, Dhruv Mishra, Dr Manu Pratap Singh

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04518v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04518v1)

**Summary:** Automatic brain tumor segmentation from multi-modal MRI remains challenging because volumetric models often incur substantial computational cost. This paper presents DALight-3D, a compact 3D U-Net variant that combines depthwise separable 3D convolutions, identifier-conditioned normalization, cross-slice attention, and adaptive skip fusion. The method is evaluated on the Medical Segmentation Decathlon Task01 BrainTumour benchmark under matched optimization settings against standard 3D U-Net, Att...

---

### 46. Interpreting V1 Population Activity via Image-Neural Latent Representation Alignment

**Authors:** Xin Wang, Zhuangzhi Gao, Hongyi Qin, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04309v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04309v1)

**Summary:** Understanding the neural mechanisms underlying visual computation has long been a central challenge in neuroscience. Recent alignment based approaches have improved the accuracy of decoding visual stimuli from brain activity, yet they provide limited insight into the neural computations that give rise to these improvements. To address this gap, we propose Dual-Tower Image-Neural Alignment (DINA), an interpretable contrastive framework for analyzing population level visual computations in primary...

---

### 47. QUIVER: Cost-Aware Adaptive Preference Querying in Surrogate-Assisted Evolutionary Multi-Objective Optimization

**Authors:** Florian A. D. Burnat

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04267v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04267v1)

**Summary:** Interactive multi-objective optimization systems face a budget allocation dilemma: one can spend resources on expensive objective evaluations or on eliciting decision-maker preferences that identify the relevant region of the Pareto set. Moreover, preference elicitation itself spans modalities with different information content and cognitive burden, ranging from cheap, noisy pairwise preference statements (PS) to richer but costlier indifference adjustments (IA).   We study cost-aware optimizati...

---

### 48. phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks

**Authors:** Stefan Fischer, Maliheh Hariri, Sebastian Otte

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04256v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04256v1)

**Summary:** Physical neural networks (PNNs) embed computation directly in material dynamics, including molecular, chemical, biological, photonic, memristive, and mechanical substrates. They are attractive for edge computing, especially at the extreme edge, where computation can be placed at the interface to sensing, actuation, or the physical process itself. However, PNNs are difficult to integrate into edge-cloud software stacks because each substrate exposes distinct interfaces, timing behavior, observabi...

---

### 49. Exact and Evolutionary Algorithms for Sequential Multi-Objective Transmission Topology Planning

**Authors:** Job Groeneveld, Miguel Muñoz, Jan Viebahn, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03753v1) | 📄 [PDF](https://arxiv.org/pdf/2605.03753v1)

**Summary:** We address day-ahead transmission topology planning and congestion management as a sequential, multi-objective optimization problem and develop two complementary algorithms for it: an exact enumeration method and a tailored evolutionary heuristic. The problem is formulated with four operational objectives reflecting real TSO decision criteria: worst-case line loading under $N-1$ security, topological depth, number of switching actions, and time spent in non-reference topologies, over a 24-hour h...

---

### 50. Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Computation in Neural Networks

**Authors:** Jatin Sharma, Dan F. M Goodman, Danyal Akarca

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03598v2) | 📄 [PDF](https://arxiv.org/pdf/2605.03598v2)

**Summary:** Understanding how biological and artificial neural networks implement computation from connectivity is a central problem in neuroscience and machine learning. In neural systems, structural and functional connectivity are known to diverge, motivating approaches that move beyond direct connections alone. Here, we show that the spatial and temporal function of recurrent neural networks (RNNs) trained on hierarchically modular tasks can be recovered by modelling the network as a graph and analysing ...

---

## stat.ML

**50 papers**

### 1. Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation

**Authors:** Kexuan Shi, Hanxuan Li, Zeju Qiu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12492v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12492v1)

**Summary:** We introduce Pion, a spectrum-preserving optimizer for large language model (LLM) training based on orthogonal equivalence transformation. Unlike additive optimizers such as Adam and Muon, Pion updates each weight matrix through left and right orthogonal transformations, preserving its singular values throughout training. This yields an optimization mechanism that modulates the geometry of weight matrices while keeping their spectral norm fixed. We derive the Pion update rule, systematically exa...

---

### 2. A proximal gradient algorithm for composite log-concave sampling

**Authors:** Linghai Liu, Sinho Chewi

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12461v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12461v1)

**Summary:** We propose an algorithm to sample from composite log-concave distributions over $\mathbb{R}^d$, i.e., densities of the form $π\propto e^{-f-g}$, assuming access to gradient evaluations of $f$ and a restricted Gaussian oracle (RGO) for $g$. The latter requirement means that we can easily sample from the density $\text{RGO}_{g,h,y}(x) \propto \exp(-g(x) -\frac{1}{2h}||y-x||^2)$, which is the sampling analogue of the proximal operator for $g$. If $f + g$ is $α$-strongly convex and $f$ is $β$-smooth...

---

### 3. Model-based Bootstrap of Controlled Markov Chains

**Authors:** Ziwei Su, Imon Banerjee, Diego Klabjan

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12410v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12410v1)

**Summary:** We propose and analyze a model-based bootstrap for transition kernels in finite controlled Markov chains (CMCs) with possibly nonstationary or history-dependent control policies, a setting that arises naturally in offline reinforcement learning (RL) when the behavior policy generating the data is unknown. We establish distributional consistency of the bootstrap transition estimator in both a single long-chain regime and the episodic offline RL regime. The key technical tools are a novel bootstra...

---

### 4. Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting

**Authors:** Laura Lützow, Simone Garatti, Marco C. Campi, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12341v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12341v1)

**Summary:** Conformal prediction constructs prediction sets with finite-sample coverage guarantees, but its calibration stage is structurally constrained to a scalar score function and a single threshold variable - forcing shapes of prediction sets to be fixed before calibration, typically through data splitting. We introduce multi-variable conformal prediction (MCP), a framework that extends conformal prediction to vector-valued score functions with multiple simultaneous calibration variables. Building on ...

---

### 5. Online Learning-to-Defer with Varying Experts

**Authors:** Dang Hoang Duy, Yannis Montreuil, Maxime Meyer, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12340v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12340v1)

**Summary:** Learning-to-Defer (L2D) methods route each query either to a predictive model or to external experts. While existing work studies this problem in batch settings, real-world deployments require handling streaming data, changing expert availability, and shifting expert distribution. We introduce the first online L2D algorithm for multiclass classification with bandit feedback and a dynamically varying pool of experts. Our method achieves regret guarantees of $O((n+n_e)T^{2/3})$ in general and $O((...

---

### 6. Optimal Policy Learning under Budget and Coverage Constraints

**Authors:** Giovanni Cerulli

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12235v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12235v1)

**Summary:** We study optimal policy learning under combined budget and minimum coverage constraints. We show that the problem admits a knapsack-type structure and that the optimal policy can be characterized by an affine threshold rule involving both budget and coverage shadow prices. We establish that the linear programming relaxation of the combinatorial solution has an O(1) integrality gap, implying asymptotic equivalence with the optimal discrete allocation. Building on this result, we analyze two imple...

---

### 7. Self-Supervised Laplace Approximation for Bayesian Uncertainty Quantification

**Authors:** Julian Rodemann, Alexander Marquard, Thomas Augustin, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12208v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12208v1)

**Summary:** Approximate Bayesian inference typically revolves around computing the posterior parameter distribution. In practice, however, the main object of interest is often a model's predictions rather than its parameters. In this work, we propose to bypass the parameter posterior and focus directly on approximating the posterior predictive distribution. We achieve this by drawing inspiration from self-training within self-supervised and semi-supervised learning. Essentially, we quantify a Bayesian model...

---

### 8. Information-Theoretic Generalization Bounds for Sequential Decision Making

**Authors:** Futoshi Futami, Masahiro Fujisawa

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12190v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12190v1)

**Summary:** Information-theoretic generalization bounds based on the supersample construction are a central tool for algorithm-dependent generalization analysis in the batch i.i.d.~setting. However, existing supersample conditional mutual information (CMI) bounds do not directly apply to sequential decision-making problems such as online learning, streaming active learning, and bandits, where data are revealed adaptively and the learner evolves along a causal trajectory. To address this limitation, we devel...

---

### 9. Keeping Score: Efficiency Improvements in Neural Likelihood Surrogate Training via Score-Augmented Loss Functions

**Authors:** Alexander Shen, Mikael Kuusela

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12118v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12118v1)

**Summary:** For stochastic process models, parameter inference is often severely bottlenecked by computationally expensive likelihood functions. Simulation-based inference (SBI) bypasses this restriction by constructing amortized surrogate likelihoods, but most SBI methods assume a black-box data generating process. While these surrogates are exact in the limit of infinite training data, practical scenarios force a strict tradeoff between model quality and simulation cost. In this work, we loosen the black-...

---

### 10. Approximation Theory of Laplacian-Based Neural Operators for Reaction-Diffusion System

**Authors:** Takashi Furuya, Ryo Ozawa, Jenn-Nan Wang

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.12025v1) | 📄 [PDF](https://arxiv.org/pdf/2605.12025v1)

**Summary:** Neural operators provide a framework for learning solution operators of partial differential equations (PDEs), enabling efficient surrogate modeling for complex systems. While universal approximation results are now well understood, approximation analysis specific to nonlinear reaction-diffusion systems remains limited. In this paper, we study neural operators applied to the solution mapping from initial conditions to time-dependent solutions of a generalized Gierer-Meinhardt reaction-diffusion ...

---

### 11. Random-Set Graph Neural Networks

**Authors:** Tommy Woodley, Shireen Kudukkil Manchingal, Matteo Tolloso, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11987v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11987v1)

**Summary:** Uncertainty quantification has become an important factor in understanding the data representations produced by Graph Neural Networks (GNNs). Despite their predictive capabilities being ever useful across industrial workspaces, the inherent uncertainty induced by the nature of the data is a huge mitigating factor to GNN performance. While aleatoric uncertainty is the result of noisy and incomplete stochastic data such as missing edges or over-smoothing, epistemic uncertainty arises from lack of ...

---

### 12. QDSB: Quantized Diffusion Schrödinger Bridges

**Authors:** Tobias Fuchs, Florian Kalinke, Nadja Klein

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11983v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11983v1)

**Summary:** Learning generative models in settings where the source and target distributions are only specified through unpaired samples is gaining in importance. Here, one frequently-used model are Schrödinger bridges (SB), which represent the most likely evolution between both endpoint distributions. To accelerate training, simulation-free SBs avoid the path simulation of the original SB models. However, learning simulation-free SBs requires paired data; a coupling of the source and target samples is obta...

---

### 13. LOFT: Low-Rank Orthogonal Fine-Tuning via Task-Aware Support Selection

**Authors:** Lanxin Zhao, Bamdev Mishra, Pratik Jawanpuria, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11872v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11872v1)

**Summary:** Orthogonal parameter-efficient fine-tuning (PEFT) adapts pretrained weights through structure-preserving multiplicative transformations, but existing methods often conflate two distinct design choices: the subspace in which adaptation occurs and the transformation applied within that subspace. This paper introduces LOFT, a low-rank orthogonal fine-tuning framework that explicitly separates these two components. By viewing orthogonal adaptation as a multiplicative subspace rotation, LOFT provides...

---

### 14. Variance-aware Reward Modeling with Anchor Guidance

**Authors:** Shuxing Fang, Ruijian Han, Liangyu Zhang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11865v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11865v1)

**Summary:** Standard Bradley--Terry (BT) reward models are limited when human preferences are pluralistic. Although soft preference labels preserve disagreement information, BT can only express it by shrinking reward margins. Gaussian reward models provide an alternative by jointly predicting a reward mean and a reward variance, but suffer from a fundamental non-identifiability from pairwise preferences alone. We propose Anchor-guided Variance-aware Reward Modeling, a framework that resolves this non-identi...

---

### 15. Minimax Rates and Spectral Distillation for Tree Ensembles

**Authors:** Binh Duc Vu, David S. Watson

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11841v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11841v1)

**Summary:** Tree ensembles such as random forests (RFs) and gradient boosting machines (GBMs) are among the most widely used supervised learners, yet their theoretical properties remain incompletely understood. We adopt a spectral perspective on these algorithms, with two main contributions. First, we derive minimax-optimal convergence for RF regression, showing that, under mild regularity conditions on tree growth, the eigenvalue decay of the induced kernel operator governs the statistical rate. Second, we...

---

### 16. One-Step Generative Modeling via Wasserstein Gradient Flows

**Authors:** Jiaqi Han, Puheng Li, Qiushan Guo, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11755v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11755v1)

**Summary:** Diffusion models and flow-based methods have shown impressive generative capability, especially for images, but their sampling is expensive because it requires many iterative updates. We introduce W-Flow, a framework for training a generator that transforms samples from a simple reference distribution into samples from a target data distribution in a single step. This is achieved in two steps: we first define an evolution from the reference distribution to the target distribution through a Wasse...

---

### 17. Posterior Contraction Rates for Sparse Kolmogorov-Arnold Networks in Anisotropic Besov Spaces

**Authors:** Jeunghun Oh, Kyeongwon Lee, Jaeyong Lee, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11652v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11652v1)

**Summary:** We study posterior contraction rates for sparse Bayesian Kolmogorov-Arnold networks (KANs) over anisotropic Besov spaces, providing a statistical foundation of KANs from a Bayesian point of view. We show that sparse Bayesian KANs equipped with spike-and-slab-type sparsity priors attain the near-minimax posterior contraction. In particular, the contraction rate depends on the intrinsic anisotropic smoothness of the underlying function. Moreover, by placing a hyperprior on a single model-size para...

---

### 18. Learning U-Statistics with Active Inference

**Authors:** Xiaoning Wang, Yuyang Huo, Liuhua Peng, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11638v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11638v1)

**Summary:** $U$-statistics play a central role in statistical inference. In many modern applications, however, acquiring the labels required for $U$-statistics is costly. Motivated by recent advances in active inference, we develop an active inference framework for $U$-statistics that selectively queries informative labels to improve estimation efficiency under a fixed labeling budget, while preserving valid statistical inference. Our approach is built on the augmented inverse probability weighting $U$-stat...

---

### 19. Exact Stiefel Optimization for Probabilistic PLS: Closed-Form Updates, Error Bounds, and Calibrated Uncertainty

**Authors:** Haoran Hu, Xingce Wang

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11607v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11607v1)

**Summary:** Probabilistic partial least squares (PPLS) is a central likelihood-based model for two-view learning when one needs both interpretable latent factors and calibrated uncertainty. Building on the identifiable parameterization of Bouhaddani et al.\ (2018), existing fitting pipelines still face two practical bottlenecks: noise--signal coupling under joint EM/ECM updates and nontrivial handling of orthogonality constraints. Following the fixed-noise scalar-likelihood line of Hu et al.\ (2025), we dev...

---

### 20. A Composite Activation Function for Learning Stable Binary Representations

**Authors:** Seokhun Park, Choeun Kim, Kwanho Lee, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11558v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11558v1)

**Summary:** Activation functions play a central role in neural networks by shaping internal representations. Recently, learning binary activation representations has attracted significant attention due to their advantages in computational and memory efficiency, as well as interpretability. However, training neural networks with Heaviside activations remains challenging, as their non-differentiability obstructs standard gradient-based optimization. In this paper, we propose Heavy Tailed Activation Function (...

---

### 21. Post-ADC Inference: Valid Inference After Active Data Collection

**Authors:** Shuichi Nishino, Tomohiro Shiraishi, Teruyuki Katsuoka, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11511v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11511v1)

**Summary:** The validity of statistical inference depends critically on how data are collected. When data gathered through active data collection (ADC) are reused for a post-hoc inferential task, conventional inference can fail because the sampling is adaptively biased toward regions favored by the collection strategy. This issue is especially pronounced in black-box optimization, where sequential model-based optimization (SMBO) methods such as the tree-structured Parzen estimator (TPE) and Gaussian process...

---

### 22. Adaptive Calibration in Non-Stationary Environments

**Authors:** Junyan Liu, Haipeng Luo, Lillian J. Ratliff

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11490v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11490v1)

**Summary:** Making calibrated online predictions is a central challenge in modern AI systems. Much of the existing literature focuses on fully adversarial environments where outcomes may be arbitrary, leading to conservative algorithms that can perform suboptimally in more benign settings, such as when outcomes are nearly stationary. This gap raises a natural question: can we design online prediction algorithms whose calibration error automatically adapts to the degree of non-stationarity in the environment...

---

### 23. FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression

**Authors:** Namyoon Lee, Yongjune Kim

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11478v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11478v1)

**Summary:** Long-context inference is increasingly a memory-traffic problem. The culprit is the key--value (KV) cache: it grows with context length, batch size, layers, and heads, and it is read at every decoding step. Rotation-based scalar codecs meet this systems constraint by storing a norm, applying a shared random rotation, and quantizing one coordinate at a time. They are universal and random-access, but they discard the geometry created by the normalization step. After a Haar rotation, a block of $k$...

---

### 24. A Barrier-Metric First-Order Method for Linearly Constrained Bilevel Optimization

**Authors:** Tenglong Hong, Paul Grigas

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11476v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11476v1)

**Summary:** We study bilevel optimization with a fixed polyhedral lower feasible set. Such problems are challenging for two reasons: active-set changes can make the upper objective nonsmooth, and existing hypergradient methods typically require lower-Hessian inversions or equivalent linear solves, which are computationally expensive. To address these issues, we adopt a logarithmic barrier smoothing of the lower problem to obtain a differentiable approximation of the constrained bilevel objective, and develo...

---

### 25. TOPPO: Rethinking PPO for Multi-Task Reinforcement Learning with Critic Balancing

**Authors:** Yuanpeng Li, Gefei Lin, Annie Qu, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11473v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11473v1)

**Summary:** Soft Actor-Critic (SAC) and its variants dominate Multi-Task Reinforcement Learning (MTRL) due to their off-policy sample efficiency, while on-policy methods such as Proximal Policy Optimization (PPO) remain underexplored. We diagnose that PPO in MTRL suffers from a previously overlooked issue: critic-side gradient ill-conditioning, which may cause tail tasks to stall while easy tasks dominate the value function's updates. To address this, we propose TOPPO (Tail-Optimized PPO), a reformulation o...

---

### 26. Spatial Adapter: Structured Spatial Decomposition and Closed-Form Covariance for Frozen Predictors

**Authors:** Wen-Ting Wang, Wei-Ying Wu, Hao-Yun Huang, et al.

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11394v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11394v1)

**Summary:** We present the Spatial Adapter, a parameter-efficient post-hoc layer that equips any frozen first-stage predictor with a structured spatial representation of its residual field and an induced closed-form spatial covariance. The adapter operates as a cascade second stage on residuals, jointly learning a spatially regularized orthonormal basis and per-sample scores via a tractable mini-batch ADMM procedure, without modifying any first-stage parameter. Because the first-stage parameters are frozen,...

---

### 27. Causal Algorithmic Recourse: Foundations and Methods

**Authors:** Drago Plecko, Collin Wang, Elias Bareinboim

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11373v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11373v1)

**Summary:** The trustworthiness of AI decision-making systems is increasingly important. A key feature of such systems is the ability to provide recommendations for how an individual may reverse a negative decision, a problem known as algorithmic recourse. Existing approaches treat recourse outcomes as counterfactuals of a fixed unit, ignoring that real-world recourse involves repeated decisions on the same individual under possibly different latent conditions. We develop a causal framework that models reco...

---

### 28. Causal Bias Detection in Generative Artifical Intelligence

**Authors:** Drago Plecko

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11365v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11365v1)

**Summary:** Automated systems built on artificial intelligence (AI) are increasingly deployed across high-stakes domains, raising critical concerns about fairness and the perpetuation of demographic disparities that exist in the world. In this context, causal inference provides a principled framework for reasoning about fairness, as it links observed disparities to underlying mechanisms and aligns naturally with human intuition and legal notions of discrimination. Prior work on causal fairness primarily foc...

---

### 29. Causal Fairness for Survival Analysis

**Authors:** Drago Plecko

**Published:** 2026-05-12

🔗 [Paper](http://arxiv.org/abs/2605.11362v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11362v1)

**Summary:** In the data-driven era, large-scale datasets are routinely collected and analyzed using machine learning (ML) and artificial intelligence (AI) to inform decisions in high-stakes domains such as healthcare, employment, and criminal justice, raising concerns about the fairness behavior of these systems. Existing works in fair ML cover tasks such as bias detection, fair prediction, and fair decision-making, but largely focus on static settings. At the same time, fairness in temporal contexts, parti...

---

### 30. $\varepsilon$-Good Action Identification in Fixed-Budget Monte Carlo Tree Search

**Authors:** Yinan Li, Tuan Nguyen, Kwang-Sung Jun

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11324v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11324v1)

**Summary:** We study the fixed-budget max-min action identification problem in depth-2 max-min trees, an important special case of Monte Carlo Tree Search. A learner sequentially allocates $T$ samples to leaves and then recommends a subtree whose minimum leaf value is largest. Motivated by approximate planning, we focus on $\varepsilon$-good subtree identification, where any subtree whose min value is within $\varepsilon$ of the optimal maximin value is acceptable.   Our main contribution is an $\varepsilon...

---

### 31. Couple to Control: Joint Initial Noise Design in Diffusion Models

**Authors:** Jing Jia, Liyue Shen, Guanyang Wang

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11311v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11311v1)

**Summary:** Diffusion models typically generate image batches from independent Gaussian initial noises. We argue that this independence assumption is only one choice within a broader class of valid joint noise designs. Instead, one can specify a coupling of the initial noises: each noise remains marginally standard Gaussian, so the pretrained diffusion model receives the same single-sample input distribution, while the dependence across samples is chosen by design. This reframes initial-noise control from s...

---

### 32. Extending Kernel Trick to Influence Functions

**Authors:** Zhenhuan Sun, Shahrokh Valaee

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11239v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11239v1)

**Summary:** In this paper, we present a dual representation of the influence functions, whose computational complexity scales with dataset size rather than model size. Both analytically and experimentally, we show that this representation can be an efficient alternative to the original influence functions for estimating changes in parameters, model outputs and loss due to data point removal, when model size is large relative to dataset size, or when evaluating the original influence functions in parameter s...

---

### 33. A Stable Distance Persistence Homology for Dynamic Bayesian Network Clustering

**Authors:** Will Bales, Carmen Rovi

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11226v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11226v1)

**Summary:** Dynamic Bayesian networks (DBNs) are a widely used framework for modeling systems whose probabilistic structure evolves over time. Standard inference methods focus on local conditional distributions and can miss larger-scale patterns in how dependencies between variables organize and change over time. We introduce a topological approach to this problem. To each DBN we associate a time-varying graph, called a Dynamic Bayesian Graph (DBG), by assigning to each edge a strength that measures variati...

---

### 34. Adaptive Policy Learning Under Unknown Network Interference

**Authors:** Aidan Gleich, Eric Laber, Alexander Volfovsky

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11191v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11191v1)

**Summary:** Adaptive experimentation under unknown network interference requires solving two coupled problems: (i) learning the underlying dynamics of interference among units and (ii) using these dynamics to inform treatment allocation in order to maximize a cumulative outcome of interest (e.g. revenue). Existing adaptive experimentation methods either assume the interference network is fully known or bypass the network by operating on coarse cluster-level randomizations. We develop a Thompson sampling alg...

---

### 35. Muon is Not That Special: Random or Inverted Spectra Work Just as Well

**Authors:** Zakhar Shumaylov, Nathaël Da Costa, Peter Zaika, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11181v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11181v1)

**Summary:** The recent empirical success of the Muon optimizer has renewed interest in non-Euclidean optimization, typically justified by similarities with second-order methods, and linear minimization oracle (LMO) theory. In this paper, we challenge this geometric narrative through three contributions, demonstrating that precise geometric structure is not the key factor affecting optimization performance. First, we introduce Freon, a family of optimizers based on Schatten (quasi-)norms, powered by a novel,...

---

### 36. Interpretable Machine Learning for Spatial Science: A Lie-Algebraic Kernel for Rotationally Anisotropic Gaussian Processes

**Authors:** Kane Warrior, Dalia Chakrabarty

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11179v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11179v1)

**Summary:** Many three-dimensional spatial fields are anisotropic, with directions of rapid and slow variation that need not align with the coordinate axes. Standard Gaussian process kernels with Automatic Relevance Determination (ARD) capture only axis-aligned anisotropy, while generic full symmetric positive definite (SPD) metrics can represent rotated anisotropy but do not parameterise principal length-scales and directions directly. We introduce an interpretable rotationally anisotropic GP kernel that p...

---

### 37. Variational predictive resampling

**Authors:** Laura Battaglia, Stefano Cortinovis, Chris Holmes, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11168v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11168v1)

**Summary:** Bayesian inference provides principled uncertainty quantification, but accurate posterior sampling with MCMC can be computationally prohibitive for modern applications. Variational inference (VI) offers a scalable alternative and often yields accurate predictive distributions, but cheap variational families such as mean-field (MF) can produce over-concentrated approximations that miss posterior dependence. We propose variational predictive resampling (VPR), a scalable posterior sampling method t...

---

### 38. Sensor Design for Accuracy-Bounded Estimation via Maximum-Entropy Likelihood Synthesis

**Authors:** Raktim Bhattacharya

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11120v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11120v1)

**Summary:** Designing the sensing architecture for large-scale spatio-temporal systems is hard when accuracy requirements are specified but sensor models are uncertain or unavailable. Classical design treats sensor placement and estimation sequentially, requiring valid forward models for each sensing modality. This paper inverts the design flow: given an error budget, synthesize the measurement likelihood that enforces it while injecting minimal information beyond the dynamical prior. The likelihood is cons...

---

### 39. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting

**Authors:** Yaman Kindap, Manfred Opper, Benjamin Dupuis, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10934v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10934v1)

**Summary:** Modelling extreme events and heavy-tailed phenomena is central to building reliable predictive systems in domains such as finance, climate science, and safety-critical AI. While Lévy processes provide a natural mathematical framework for capturing jumps and heavy tails, Bayesian inference for Lévy-driven stochastic differential equations (SDEs) remains intractable with existing methods: Monte Carlo approaches are rigorous but lack scalability, whereas neural variational inference methods are eff...

---

### 40. Revisiting Policy Gradients for Restricted Policy Classes: Escaping Myopic Local Optima with $k$-step Policy Gradients

**Authors:** Alex DeWeese, Guannan Qu

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10909v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10909v1)

**Summary:** This work revisits standard policy gradient methods used on restricted policy classes, which are known to get stuck in suboptimal critical points. We identify an important cause for this phenomenon to be that the policy gradient is itself fundamentally myopic, i.e. it only improves the policy based on the one-step $Q$-function. In this work, we propose a generalized $k$-step policy gradient method that couples the randomness within a $k$-step time window and can escape the myopic local optima in...

---

### 41. Uniform Scaling Limits in AdamW-Trained Transformers

**Authors:** William Gibson, Christoph Reisinger

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.11059v1) | 📄 [PDF](https://arxiv.org/pdf/2605.11059v1)

**Summary:** We study the large-depth limit of transformers trained with AdamW, by modelling the hidden-state dynamics as an interacting particle system (IPS) coupled through the attention mechanism. Under appropriate scaling of the attention heads, we prove that the joint dynamics of the hidden states and backpropagated variables converge in $L^2$, uniformly over the initial condition, to the solution of a forward--backward system of ODEs at rate $\mathcal O(L^{-1}+L^{-1/3}H^{-1/2})$. Here, $L$ and $H$ deno...

---

### 42. Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge

**Authors:** Wenbo Zhang, Lijinghua Zhang, Liner Xiang, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10805v1)

**Summary:** Reasoning-capable large language models (LLMs) have recently been adopted as automated judges, but their benefits and costs in LLM-as-a-Judge settings remain unclear. Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational...

---

### 43. Factual recall in linear associative memories: sharp asymptotics and mechanistic insights

**Authors:** Alessio Giorlandino, Sebastian Goldt, Antoine Maillard

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10795v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10795v1)

**Summary:** Large language models demonstrate remarkable ability in factual recall, yet the fundamental limits of storing and retrieving input--output associations with neural networks remain unclear. We study these limits in a minimal setting: a linear associative memory that maps $p$ input embeddings in $\mathbb{R}^d$ to their corresponding~$d$-dimensional targets via a single layer, requiring each mapped input to be well separated from all other targets. Unlike in supervised classification, this strict s...

---

### 44. When Are Trade-Off Functions Testable from Finite Samples?

**Authors:** Kaining Shi, Qiaosen Wang, Cong Ma

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10774v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10774v1)

**Summary:** We study finite-sample inference for the trade-off function of two unknown probability distributions, the function that traces the optimal type I/type II error frontier in binary testing. Given samples from distributions $P$ and $Q$, we consider the problem of testing whether their trade-off function lies above a benchmark curve $f_0$ or falls below a weaker benchmark $f_1$. Without structural restrictions, this problem is impossible uniformly over nonparametric classes. We identify a sharp cond...

---

### 45. What should post-training optimize? A test-time scaling law perspective

**Authors:** Muheng Li, Jian Qian, Wenlong Mou

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10716v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10716v1)

**Summary:** Large language models are increasingly deployed with test-time strategies: sample $N$ responses, score them with a reward model or verifier, and return the best. This deployment rule exposes a mismatch in post-training: standard objectives optimize the mean reward of a single response, whereas best-of-$N$ performance is governed by the upper tail of the reward distribution. Recent test-time-aware objectives partly address this mismatch, but typically assume that training can use the same per-pro...

---

### 46. Price of Quality: Sufficient Conditions for Sparse Recovery using Mixed-Quality Data

**Authors:** Youssef Chaabouni, David Gamarnik

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10713v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10713v1)

**Summary:** We study sparse recovery when observations come from mixed-quality sources: a small collection of high-quality measurements with small noise variance and a larger collection of lower-quality measurements with higher variance. For this heterogeneous-noise setting, we establish sample-size conditions for information-theoretic and algorithmic recovery. On the information-theoretic side, we show that it is sufficient for $(n_1, n_2)$ to satisfy a linear trade-off defining the Price of Quality: the n...

---

### 47. Natural Policy Gradient as Doubly Smoothed Policy Iteration: A Bellman-Operator Framework

**Authors:** Phalguni Nanda, Zaiwei Chen

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10671v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10671v1)

**Summary:** In this work, we show that natural policy gradient, a core algorithm in reinforcement learning, admits an exact formulation as a smoothed and averaged form of policy iteration. Specifically, we introduce doubly smoothed policy iteration (DSPI), a Bellman-operator framework in which each policy is obtained by applying a regularized greedy step to a weighted average of past $Q$-functions. DSPI includes policy iteration, dual-averaged policy iteration, natural policy gradient, and more general poli...

---

### 48. When Can Digital Personas Reliably Approximate Human Survey Findings?

**Authors:** Mumin Jia, Yilin Chen, Divya Sharma, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10659v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10659v1)

**Summary:** Digital personas powered by Large Language Models (LLMs) are increasingly proposed as substitutes for human survey respondents, yet it remains unclear when they can reliably approximate human survey findings. We answer this question using the LISS panel, constructing personas from respondents' background variables and pre-2023 survey histories, then testing them against the same respondents' held-out post-cutoff answers. Across four persona architectures, three LLMs, and two prediction tasks, we...

---

### 49. A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables

**Authors:** Zheng Li, Feng Xie, Shenglan Nie, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10651v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10651v1)

**Summary:** Constraint-based causal discovery is widely used for learning causal structures, but heavy reliance on conditional independence (CI) testing makes it computationally expensive in high-dimensional settings. To mitigate this limitation, many divide-and-conquer frameworks have been proposed, but most assume causal sufficiency, i.e., no latent variables. In this paper, we show that divide-and-conquer strategies can be theoretically generalized beyond causal sufficiency to settings with latent variab...

---

### 50. Amortizing Causal Sensitivity Analysis via Prior Data-Fitted Networks

**Authors:** Emil Javurek, Dennis Frauen, Marie Brockschmidt, et al.

**Published:** 2026-05-11

🔗 [Paper](http://arxiv.org/abs/2605.10590v1) | 📄 [PDF](https://arxiv.org/pdf/2605.10590v1)

**Summary:** Causal sensitivity analysis aims to provide bounds for causal effect estimates in the presence of unobserved confounding. However, existing methods for causal sensitivity analysis are per-instance procedures, meaning that changes to the dataset, causal query, sensitivity level, or treatment require new computation. Here, we instead present an in-context learning approach. Specifically, we propose an amortized approach to causal sensitivity analysis based on prior-data fitted networks. A key chal...

---

