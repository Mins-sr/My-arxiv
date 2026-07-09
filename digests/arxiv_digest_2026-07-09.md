# arXiv Daily Digest - 2026-07-09

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning

**Authors:** Chen Tang, Yizhou Wang, Jianyu Wu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07708v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07708v1)

**Summary:** Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint ch...

---

### 2. Co-LMLM: Continuous-Query Limited Memory Language Models

**Authors:** Yair Feldman, Linxi Zhao, Nathan Godey, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07707v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07707v1)

**Summary:** Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant ...

---

### 3. Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass

**Authors:** Victor Giannakouris, Immanuel Trummer

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07696v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07696v1)

**Summary:** Analytical workloads operating on data stored in external database systems face a fundamental bottleneck: data access is guarded entirely by the database driver, like JDBC or ODBC, forcing all reads through query execution and other driver layers that are not designed for bulk columnar analytics. We present Jailbreak, an approach that bypasses the database engine entirely by reading storage files directly and materializing data as in-memory columnar buffers. Jailbreak's key insight is that datab...

---

### 4. Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety

**Authors:** Yujiao Chen

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07695v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07695v1)

**Summary:** We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces...

---

### 5. Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF

**Authors:** Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07693v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07693v1)

**Summary:** Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that subs...

---

### 6. Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

**Authors:** Vladislav Beliaev

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07690v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07690v1)

**Summary:** Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is r...

---

### 7. SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents

**Authors:** Tianming Sha, Yue Zhao, Lichao Sun, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07676v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07676v1)

**Summary:** Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and maintainable. We introduce SkillCenter, to our knowledge the largest open skill library for agents by total count: 216,938 structured skills across 24 domain bundles. A SkillGate-filtered pipeline contributes 114,565 source-grounded skills from peer-reviewed journals, ArXiv, and over 24,000 technical so...

---

### 8. DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation

**Authors:** Jordan Painter, Dipankar Srirag, Adarsh Kappiyath, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07669v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07669v1)

**Summary:** Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled compar...

---

### 9. Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops

**Authors:** Mingguang Chen, Licheng Wang, Bo Qu

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07663v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07663v1)

**Summary:** AI systems increasingly participate in their own improvement: revising their outputs, adapting their own harnesses during deployment, training on data they generate, and, increasingly, conducting AI research itself. This literature is described under a vocabulary ("self-refine," "self-reward," "self-play," "self-evolve") that conflates fundamentally different ambitions. We survey 1,250 arXiv papers (2024-2026) along two axes: what the system improves -- its behavior in deployment, its policy thr...

---

### 10. RL Post-Training Builds Compositional Reasoning Strategies

**Authors:** Azwar Abdulsalam, Nishil Patel, Andrew Saxe

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07646v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07646v1)

**Summary:** Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that...

---

### 11. ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation

**Authors:** Xuan-Thong Truong, Trung-Kien Le, Tung Kieu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07640v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07640v1)

**Summary:** Deep learning has significantly advanced time series imputation, yet most existing architectures primarily rely on localized temporal context within the corrupted input sequence. This reliance can be limiting in real-world scenarios, where time series often exhibit non-stationary dynamics, weak temporal correlations, and infrequent patterns that are difficult to reconstruct from nearby observations alone. In this paper, we propose ALER-TI, Aligned Latent Embedding Retrieval for Time Series Imput...

---

### 12. QCNN with Rough Path Signature Kernels

**Authors:** Leonardo Nogueira Falabella, Vasily Sazonov

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07634v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07634v1)

**Summary:** Time series analysis plays a vital role across a wide range of scientific and engineering domains but poses substantial computational challenges. A major difficulty arises from the time reparameterization invariance of time series data, which complicates the extraction of meaningful temporal features. In this work, we address the problem of time series classification by exploring the application of quantum computation techniques. We propose a hybrid quantum-classical architecture that integrates...

---

### 13. Future Confidence Distillation in Large Language Models

**Authors:** Sahil Kale

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07626v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07626v1)

**Summary:** Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation depend on accurately estimating answer reliability. Existing approaches, however, largely treat confidence as a property of completed responses, overlooking how confidence-related information evolves throughout the answering process. In this work, we investigate confidence from a temporal perspective b...

---

### 14. Towards Agentic AI Governance: A Preliminary Assessment

**Authors:** Mubarak Raji, Masooda Bashir

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07612v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07612v1)

**Summary:** Artificial intelligence is rapidly evolving from generative systems to agentic AI capable of autonomously planning and executing tasks. Widely characterized as the Year of Agentic AI, 2025 marked accelerated development and deployment, introducing new ethical and governance challenges. This paper presents a systematic review of the emerging literature on agentic AI governance. Our analysis identifies features that distinguish agentic AI from traditional systems and why it warrants targeted gover...

---

### 15. CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis

**Authors:** Kaicong Huang, Meng Ma, Ruimin Ke

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07601v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07601v1)

**Summary:** Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations. Corner-case generation is inherently a multi-source problem spanning visual representation, scene reasoning, and vehicle trajectory generation and control. Prior knowledge- and model-based approaches typically focus on scene or trajectory components in isolation, while diffusion-based methods attempt end...

---

### 16. Collaborative Synthetic Data Generation for Knowledge Transfer in Federated Learning

**Authors:** Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07565v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07565v1)

**Summary:** One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, particularly when client data distributions diverge. Recent work has addressed this challenge by aggregating client knowledge on the server through the construction of transferable synthetic datasets or distillates. However, most of these methods lack formal privacy guarantees, leaving a gap in jointly...

---

### 17. Creativity from Friction: Human-AI Interaction for Exploratory Structural Design

**Authors:** Ricardo Maia Avelino, Rita Sevastjanova, Tom Van Mele, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07521v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07521v1)

**Summary:** AI agents that generate final answers based on user input often do not meet the needs of creative fields. Fields such as structural design and architecture need interactive systems that help users externalise and develop ideas, explore alternatives, and refine partial solutions. The final product of such designs needs to comply with many constraints concerning, e.g., spatial configuration, mechanical behaviour, material quantities, and costs. These constraints create friction in the design proce...

---

### 18. Stability of Flow Models for Graph Signals

**Authors:** Martin Schmidt, Gonzalo Mateos

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07510v1)

**Summary:** Generating signals on graphs requires permutation-equivariant models that exhibit stability with respect to relative structural perturbations. While favorable stability properties of Graph Neural Networks (GNNs) have been well documented, it is unclear how structural errors propagate through the dynamics of continuous generative flow models that are gaining traction for graph signal generation. In this paper, we analyze continuous normalized flow models parameterized by GNNs and show that permut...

---

### 19. Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

**Authors:** Zhenyu Hou, Yujiang Li, Jie Tang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07508v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07508v1)

**Summary:** Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks. Recently, asynchronous RL has emerged as a more efficient alternative by updating the model as rollouts arrive. However, existing asynchronous RL systems often emphasize throughput, while leaving training stability and task effectiveness largely underexplore...

---

### 20. HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models

**Authors:** Feng He, Zhenting Wang, Qifan Wang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07507v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07507v1)

**Summary:** Hallucinations in vision language models (VLMs) are commonly treated as semantic errors, yet they often arise from partial or ambiguous visual evidence. Prior work mainly focuses on detecting or suppressing hallucinations at generation time, leaving the subsequent reasoning stage largely unexplored. In this work, we study Post Hallucination Reasoning (PHR), the stage in which hallucinated semantics enter the model's inference context and influence downstream predictions. To systematically invest...

---

### 21. Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows

**Authors:** Wei-Jung Huang

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07504v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07504v1)

**Summary:** Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results. Reusable skill files are meant to avoid prompting from scratch by packaging guidance for a task family. Expert-written skills can encode high-quality guidance, but writing and maintaining them across many data-science task families creates a manual bottleneck. We ask whether LLM-generated skills offer a useful low-curati...

---

### 22. TimEE: End-to-end Time Series Classification via In-Context Learning

**Authors:** Jaris Küken, Shi Bin Hoo, Martin Mráz, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07500v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07500v1)

**Summary:** Time series classification (TSC) is dominated by a two-stage paradigm: train a feature encoder -- either from scratch on the target dataset or via pretraining on large corpora -- and then fit a task-specific classifier on top. While effective, this decoupling optimizes representation learning independently of the classification objective, requires per-dataset training, and prevents the model from exploiting label information during inference. We introduce TimEE, a 4.5M-parameter foundation model...

---

### 23. Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26

**Authors:** Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07498v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07498v1)

**Summary:** Testing is a major effort for the gaming industry, requiring a significant part of development budget and people power. We present a case study on a development version of the ice hockey game EA SPORTS NHL 26, for which human playtesters test the goalie AI for behavioral exploits. To reduce the effort of re-testing the goalie AI after every game or behavior modification in the development phase, we propose Reward-Adaptive Iterative Discovery (RAID), a novel approach to automatically find exploit...

---

### 24. Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning

**Authors:** Dmitry Beresnev, Vladimir Makharev, Roman Khalikov, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07492v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07492v1)

**Summary:** Many reasoning tasks are not well described by a single left-to-right chain: a solver may need to pursue a plausible branch, observe delayed failure, and return to the latest prefix that can still be completed. We introduce Pyligent, a training and inference framework inspired by the Diligent Learner formulation that represents reasoning as validated search over partial solution chains. A task validator labels generated continuations and failures, and the resulting search trees are converted int...

---

### 25. Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents

**Authors:** Harry Owiredu-Ashley

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07474v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07474v1)

**Summary:** Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another ...

---

### 26. Where to Intervene? Benchmarking Fairness-Aware Learning on Differentially Private Synthetic Tabular Data

**Authors:** Vinícius Gabriel Angelozzi, Héber H. Arcolezi

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07471v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07471v1)

**Summary:** Machine learning models are increasingly deployed in high-stakes domains, raising concerns about both privacy and fairness. Differential Privacy (DP) has become a gold standard for privacy-preserving data analysis, while fairness-aware mechanisms aim to mitigate discrimination against underrepresented groups. However, these objectives can conflict: DP often amplifies disparities across demographic groups, and little is known about whether established fairness interventions remain effective under...

---

### 27. SynthAVE: Scalable Synthetic Labeling for E-Commerce with LLM-Arena Validation

**Authors:** Andrea Scarinci, Virginia Negri, Brayan Impata, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07469v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07469v1)

**Summary:** Fine-tuning large language models (LLMs) for e-commerce attribute extraction requires labeled data representative across thousands of product types, attributes, and multiple languages. This combinatorial scale translates to millions of annotations, rendering human labeling prohibitively costly. While recent work has demonstrated synthetic label generation using LLMs, deploying such approaches at industrial scale requires integrated quality control mechanisms. We present SynthAVE, a large-scale h...

---

### 28. SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis

**Authors:** Songhan Wang, Haoang Chi, He Li, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07467v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07467v1)

**Summary:** Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end sp...

---

### 29. The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents

**Authors:** Xing Zhang, Yanwei Cui, Guanghui Wang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07436v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07436v1)

**Summary:** A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted...

---

### 30. RLVP: Penalize the Path, Reward the Outcome

**Authors:** Bojie Li, Noah Shi

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07435v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07435v1)

**Summary:** Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them fr...

---

### 31. InductWave: Inductive Multi-Hop Logical Query Answering on Knowledge Graphs

**Authors:** Mayank Kharbanda, Michael Cochez, Rajiv Ratn Shah, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07422v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07422v1)

**Summary:** Logical Multi-Hop Query Answering over Knowledge Graphs (KGs) can be formulated as querying, with an implicit completeness assumption. Current works mainly focus on Existential First Order Logic (EFO) queries. These EFO queries contain conjunction, disjunction, and negation operators. Most existing works employ transductive reasoning, meaning they are not capable of reasoning over entities unseen during training. In the real world, there is a resource scarcity, and we cannot train a model with a...

---

### 32. Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents

**Authors:** Vikas Reddy, Sumanth Reddy Challaram, Abhishek Basu

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07405v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07405v1)

**Summary:** Tool-using LLM agents can violate the very policies they are deployed to enforce while appearing to complete the task successfully. In policy-permissive environments, a tool may execute any well-formed call even when the corresponding state transition is forbidden by domain policy. The result is a silent wrong state (a booking cancelled, a passenger count changed, a claim acted on without verification) that neither the tool nor the agent's self-report exposes.   We study this failure mode in the...

---

### 33. Heterogeneity-Adaptive Diffusion Schrodinger Bridge for PET-Guided Whole-Body MRI Translation

**Authors:** Chengbo Wang, Jiacheng Yu, Linjie Bian, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07401v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07401v1)

**Summary:** While whole-body multimodal medical imaging scanners have been increasingly recognized for more effective medical applications, the excessive long acquisition time in PET-MR scanning is a major obstacle in more efficient clinical practice. Deep learning-based MRI translation provides a potential solution to reduce scan duration. However, current models often focus on specific anatomical regions and face challenges for whole-body scans that consists of highly heterogeneous feature distributions m...

---

### 34. Agentic Data Environments

**Authors:** Elaine Ang, Chenxi Huang, Georgios Liargkovas, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07397v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07397v1)

**Summary:** Autonomous agents promise substantial gains in speed, scale, and labor efficiency, but their failures can impose abrupt and often irreversible costs. The central challenge for agentic automation is therefore to increase the benefits of automation while bounding the consequences of failure.   While databases remain central to modern computing, agents operate over a broader data environment spanning files, APIs, applications, and system state. In this talk, I will outline early work on Agentic Dat...

---

### 35. When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated VLMs

**Authors:** Tanay Sodha, Aditya Sharma, Ramya Hebbalaguppe, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07395v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07395v1)

**Summary:** Reliable confidence estimation remains a key limitation of test-time adaptation in vision-language models (VLMs), where prompt tuning improves zero-shot accuracy but often degrades calibration due to entropy-driven overconfidence. Prior approaches mitigate this using LLM-derived class attributes and contrastive regularization, yet treat attributes independently, ignoring their relational structure. We propose ARGTCA, which represents (class, attribute) pairs as nodes in a Symbolic Attribute Grap...

---

### 36. MIRA-Math: A Benchmark for Minimal Information Requesting and Mathematical Reasoning

**Authors:** Charbel Al Bateh, Samer Saab

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07391v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07391v1)

**Summary:** Mathematical reasoning benchmarks typically provide all facts needed to solve each problem, while interactive benchmarks often mix reasoning with tools, retrieval, and long-horizon dialogue. We introduce MIRA-Math, a benchmark for a narrower diagnostic capability: solving mathematical problems whose full latent state has a unique answer, but whose solver-facing view is missing exactly one necessary atomic fact. The solver must request the missing information in natural language under a strict bu...

---

### 37. Physics-Audited Agentic Discovery in Scientific Machine Learning

**Authors:** Diab W. Abueidda, Bilal Ahmed, Panos Pantidis, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07379v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07379v1)

**Summary:** In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not establish that the predicted fields satisfy the physics that matter for mechanics, such as boundary conditions, superposition, stiffness scaling, or causality. We introduce Physics-Audited Agentic SciML (PA-SciML), a verification-first workflow for agentic SciML discovery. The workflow fixes...

---

### 38. On Adversarial Vulnerability of Vision-Language Models through the Lens of Intermediate Spectral Subspaces

**Authors:** Chethan Krishnamurthy Ramanaik, Tobias Callies, Michael Hecht, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07375v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07375v1)

**Summary:** Adversarial vulnerability in deep neural networks (DNNs) has been studied from the perspectives of decision-boundary geometry, feature robustness, input-output Jacobians, and the instability of inverse problems. Here, we focus on the spectral structure of intermediate linear transformations that propagate information through modern DNNs, an unexplored mechanism of adversarial vulnerability. Specifically, we investigate transformer-based vision-language models, whose linear layers admit interpret...

---

### 39. Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report

**Authors:** Xufeng Zhao, Fuzhi Yang, Jianhui Chen, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07370v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07370v1)

**Summary:** In embodied intelligence systems, the motion controller serves as the critical bridge between semantic reasoning and physical execution. Humanoid control has progressed rapidly through large-scale human motion-capture data and motion-tracking paradigm. However, producing quadruped robots motion corpora with scalability and physical feasibility faces more fundamental obstacles: animal motion data is scarce, and cross-embodiment retargeting remains fragile. We present ABot-C0, a generalist motion-...

---

### 40. Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors

**Authors:** Oliver Makins, Orazio Angelini, Zohreh Shams, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07368v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07368v1)

**Summary:** AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a ...

---

### 41. HumAIN: Human-Aware Implicit Social Robot Navigation

**Authors:** Daeun Song, Nhat Le, Jeffrey Chen, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07357v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07357v1)

**Summary:** Effective social robot navigation requires sensitivity to human behavior, often revealed through subtle skeletal cues like gait and orientation. We present Human-Aware Implicit Social Robot Navigation (HumAIN), a novel framework that fuses implicit social cues directly into the planning loop via knowledge distillation. We first employ a transformer-based teacher model that fuses rich multi-modal inputs, including historic images, skeletal keypoints, robot state, and a robot's target goal, to lea...

---

### 42. Latency-Aware Bid Acceptance under Operational Feasibility: A Public Benchmark with Hindsight Ceilings

**Authors:** Aswin Chandrasekaran

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07343v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07343v1)

**Summary:** Online truckload bid acceptance is a closed-loop stochastic decision problem in which a carrier or broker must, in real time, accept or reject a tendered load subject to operational feasibility, fleet repositioning costs, and opportunity cost against future demand. Public, reproducible benchmarks for this problem are scarce: existing routing benchmarks are static, while dynamic-fleet studies typically rely on private operator data. We introduce FreightBidBench, a public-calibrated, dependency-fr...

---

### 43. Quantum simulation of real-world nonlinear dynamics via Koopman method

**Authors:** Baoyang Zhang, Dong An, Zhaoyuan Meng, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07338v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07338v1)

**Summary:** Nonlinear dynamics is ubiquitous in nature, ranging from chemical pattern formation to ocean circulation, yet its simulation on quantum computers is fundamentally limited by the unitary nature of quantum evolution. We propose the quantum Koopman method, a data-driven framework that embeds nonlinear dynamics into a learned linear representation and implements the resulting evolution using shallow quantum circuits. This method learns Koopman observables from trajectory data, projects the lifted dy...

---

### 44. Hypergraph Neural Stochastic Diffusion: An SDE Framework for Uncertainty Estimation

**Authors:** Zhiheng Zhou, Mengyao Zhou, Dengyi Zhao, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07330v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07330v1)

**Summary:** Hypergraph neural networks have shown powerful capability in modeling higher-order relations, yet their predictive uncertainty remains underexplored. Unlike pairwise graphs, uncertainty in hypergraphs arises not only from noisy attributes and ambiguous labels, but also from variations in node-hyperedge incidence structures and complex higher-order dependencies. Existing approaches mainly estimate uncertainty from final predictions or rely on computationally expensive ensembles and Bayesian infer...

---

### 45. HAJJv2-CrowdCount: Zero-Shot Benchmark for Dense Crowd Counting

**Authors:** Reem AlYabis, Fares AlTuwaim, AlJawharh AlOtaibi, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07322v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07322v1)

**Summary:** Automated crowd counting in Hajj video is difficult not because current models lack capacity, but because the footage violates the assumptions those models were built on: cameras observe the crowd from steep, near-vertical angles, individuals occlude one another extensively, and a single frame can contain well over a thousand people. Benchmarks that test crowd counting in such an environment are either private or not detailed per second. We revisit the HAJJv2 dataset and contribute HAJJv2-CrowdC...

---

### 46. From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents

**Authors:** Haipeng Ding, Yuexiang Xie, Zhewei Wei, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07321v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07321v1)

**Summary:** Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed of granular atomic actions (e.g., basic file I/O or single-turn search), which forces agents to reinvent low-level logic for every recurring workflow, leading to increased reasoning overhead and failure rates. In this study, we propose that agents can achieve self-evolution by synthesizing these ato...

---

### 47. FedCVESA: Taking Away Training Data in Federated Learning via Correlation Value Encoding and Segmented Aggregation

**Authors:** Chongkai Li, Bang Zhang, Wenjian Luo

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07314v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07314v1)

**Summary:** Federated learning (FL) avoids explicit data exposure by keeping raw data on local clients, yet privacy risks remain in the training process and the learned model itself. Recently, centralized Taking Away Training Data (TATD) attacks have shown that malicious training could abuse the memorization capacity of deep models to store and later recover training data. However, this memorization-based threat has not been systematically studied under FL environments, where multi-client averaging could ov...

---

### 48. POO-LPSP: Parallel Osprey Optimized Least Penalty-Squared Prioritization Methods for Priority Derivation in the Analytic Hierarchy Process

**Authors:** Kevin Kam Fung Yuen

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07313v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07313v1)

**Summary:** Pairwise comparison (PC) via pairwise reciprocal matrices (PRMs) is central to the Analytic Hierarchy Process (AHP). Although the traditional eigenvector method is widely applied to derive priorities, its theoretical robustness in reflecting true priority vectors remains debated. Building upon a previous iteration of this study, this research develops the revised Least Penalty-Squared Prioritization (LPSP) optimization models, including the revised Least Product of Penalty and Direct Squares (LP...

---

### 49. Multimodal Voice Activity Projection for Turn-Taking in Social Robots with Voice-Activity-Related Pretrained Encoders

**Authors:** Antonio Cano, Guillermo Pérez, Luis Merino, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07294v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07294v1)

**Summary:** Turn-taking prediction is a key requirement for social robots involved in human-human interaction, particularly in mediator settings, where the robot must anticipate conversational dynamics rather than merely react to pauses. This work presents a Multimodal Voice Activity Projection (MM-VAP) framework that extends the original audio-only VAP formulation to synchronized audio-visual inputs while preserving its self-supervised future-projection objective. The proposed approach builds on pretrained...

---

### 50. CarbonCLIP: Enhance Carbon Prediction from Satellite Imagery via Integrated Street-View Semantics and Temporal Context Training

**Authors:** Zeru Yang, Fang-Ying Gong, Steve H. L. Yim, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07292v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07292v1)

**Summary:** Accurately estimating urban carbon emissions is critical for sustainable urban planning, yet many existing approaches remain difficult to apply consistently across cities due to data-source heterogeneity and the lack of fine-grained semantic-temporal context in remote sensing data. We propose CarbonCLIP, a task-oriented multimodal distillation framework that improves satellite-based carbon emission prediction by transferring contextual knowledge into a unified satellite representation through du...

---

## cs.CL

**50 papers**

### 1. Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning

**Authors:** Chen Tang, Yizhou Wang, Jianyu Wu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07708v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07708v1)

**Summary:** Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint ch...

---

### 2. Co-LMLM: Continuous-Query Limited Memory Language Models

**Authors:** Yair Feldman, Linxi Zhao, Nathan Godey, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07707v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07707v1)

**Summary:** Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant ...

---

### 3. From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization

**Authors:** Ying Chang, Jiahang Xu, Xuan Feng, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07702v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07702v1)

**Summary:** The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, ...

---

### 4. Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

**Authors:** Vladislav Beliaev

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07690v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07690v1)

**Summary:** Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is r...

---

### 5. Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems

**Authors:** Vladislav Beliaev

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07674v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07674v1)

**Summary:** Group Relative Policy Optimization (GRPO) stalls on a model's hardest problems: when no rollout in a group succeeds, the group-relative advantages vanish and the problem contributes no gradient, wasting the frontier examples we most want to learn from. Prepending a correct prefix of a reference solution raises the success rate, making prefix length a continuous knob on difficulty. Concurrent methods set the knob once; AdaPrefix-GRPO turns it into a feedback controller: throughout training it adj...

---

### 6. Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity Familiarity from Factual Reliability Across Model Scale

**Authors:** Grzegorz Brzezinka

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07670v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07670v1)

**Summary:** Large language models hallucinate most about entities they have never seen. We ask whether a model's activations betray entity familiarity before a single answer token is generated, and whether that signal predicts the factual reliability of the answers. On four Polish Bielik models (1.5B-11B parameters), we probe four entity domains (athletes, cities, writers, musicians), each with 42 well-known, 42 obscure-but-real, and 42 fabricated entities addressed by a one-sentence question (504 prompts p...

---

### 7. DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation

**Authors:** Jordan Painter, Dipankar Srirag, Adarsh Kappiyath, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07669v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07669v1)

**Summary:** Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled compar...

---

### 8. RL Post-Training Builds Compositional Reasoning Strategies

**Authors:** Azwar Abdulsalam, Nishil Patel, Andrew Saxe

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07646v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07646v1)

**Summary:** Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that...

---

### 9. Future Confidence Distillation in Large Language Models

**Authors:** Sahil Kale

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07626v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07626v1)

**Summary:** Reliable confidence estimation is essential for deploying large language models (LLMs) in confidence-aware systems, where downstream decisions such as retrieval, tool use, and adaptive computation depend on accurately estimating answer reliability. Existing approaches, however, largely treat confidence as a property of completed responses, overlooking how confidence-related information evolves throughout the answering process. In this work, we investigate confidence from a temporal perspective b...

---

### 10. PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning

**Authors:** Yazdan Jamshidi, Alexey Shvets

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07557v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07557v1)

**Summary:** One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwise Sparsity), which adjusts per-layer sparsity based on the 99th percentile of activation magnitudes, bounded to $\pm 5\%$ around the target ratio. On LLaMA-2-7B at 50\% sparsity, PALS achieves 10.96 WikiText-2 perplexity versus 12.92 for uniform Wanda (mean over 9 runs, $p < 0.001$). The benefit is...

---

### 11. Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?

**Authors:** Qinnan Cai, Yibo Zhao, Xiang Li

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07548v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07548v1)

**Summary:** Large language model based search agents increasingly adopt multi-agent architectures in which a main agent decomposes a complex question into sub-queries and dispatches them to parallel sub-agents. However, existing systems instantiate all roles from a single model of identical scale, leaving open how model capacity should be distributed across roles. We factorize hierarchical search into three roles: a delegation role responsible for task decomposition, an execution role responsible for retrie...

---

### 12. FourierQK: Spectral Preprocessing of Query-Key Projections Improves Transformer Attention

**Authors:** Athanasios Zeris

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07478v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07478v1)

**Summary:** FFT-based spectral preprocessing of learned query-key (Q/K) projections substantially improves transformer attention on character-level language modelling. On TinyShakespeare: a fixed random spectral filter achieves val=1.031 (Delta=+0.443); a single learned frequency at paragraph scale achieves val=0.608 (Delta=+0.867); and four learned frequencies spanning paragraph to word scale achieve val=0.309 (Delta=+1.166), a 79% reduction over standard dot-product attention. The single-frequency result ...

---

### 13. Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents

**Authors:** Harry Owiredu-Ashley

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07474v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07474v1)

**Summary:** Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another ...

---

### 14. SynthAVE: Scalable Synthetic Labeling for E-Commerce with LLM-Arena Validation

**Authors:** Andrea Scarinci, Virginia Negri, Brayan Impata, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07469v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07469v1)

**Summary:** Fine-tuning large language models (LLMs) for e-commerce attribute extraction requires labeled data representative across thousands of product types, attributes, and multiple languages. This combinatorial scale translates to millions of annotations, rendering human labeling prohibitively costly. While recent work has demonstrated synthetic label generation using LLMs, deploying such approaches at industrial scale requires integrated quality control mechanisms. We present SynthAVE, a large-scale h...

---

### 15. The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents

**Authors:** Xing Zhang, Yanwei Cui, Guanghui Wang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07436v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07436v1)

**Summary:** A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted...

---

### 16. DeLS-Spec: Decoupled Long-Short Contexts for Parallel Speculative Drafting

**Authors:** Hong-Kai Zheng, Piji Li

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07409v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07409v1)

**Summary:** Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them in parallel. Block-parallel drafters such as DFlash further improve drafting efficiency by predicting an entire block in one pass, but their position-wise predictions lack explicit intra-block causal conditioning. Recent methods such as Domino and DSpark attempt to introduce such causality into block-parallel drafting, but they require training the draft model from scratch, which limits their flexibilit...

---

### 17. Transformer-based segmentation of prosodic boundaries in Brazilian Portuguese

**Authors:** Rodrigo de Freitas Lima, Julio Cesar Galdino, Marcos Vinicius Treviso

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07408v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07408v1)

**Summary:** Automatic prosodic segmentation identifies boundaries between speech units from acoustic and linguistic evidence. Although recent deep learning approaches have produced strong results for English, automatic segmentation for Brazilian Portuguese (BP) still relies mostly on rule-based or traditional machine-learning methods. This paper presents SAMPA, a Whisper-based segmenter that transcribes BP speech while inserting explicit markers for terminal prosodic boundaries. We fine-tune Whisper large-v...

---

### 18. TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models

**Authors:** Yutang Ma, Kecheng Huang, Xikun Jiang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07388v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07388v1)

**Summary:** Large Language Models (LLMs) store factual knowledge and domain-specific patterns implicitly in dense Transformer parameters, making knowledge expansion costly through pretraining, fine-tuning, retrieval augmentation, or longer contexts. Engram-style memory offers a compact hidden-state injection pathway, but existing GPU-resident designs often rely on hash-based compression, causing unrelated phrases to collide in shared slots and weakening phrase-level semantic fidelity. We present TF-Engram, ...

---

### 19. From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents

**Authors:** Haipeng Ding, Yuexiang Xie, Zhewei Wei, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07321v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07321v1)

**Summary:** Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed of granular atomic actions (e.g., basic file I/O or single-turn search), which forces agents to reinvent low-level logic for every recurring workflow, leading to increased reasoning overhead and failure rates. In this study, we propose that agents can achieve self-evolution by synthesizing these ato...

---

### 20. R^3: Advertisement Compliance Rectification via Group-Relative Experience Extractor and Curriculum Reinforcement

**Authors:** Yuan Chen, Zhenyu Hu, Mengge Xue, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07318v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07318v1)

**Summary:** Rigorous content moderation is crucial for online advertising but leads to millions of daily rejections. This scale renders manual rectification infeasible, particularly for video advertisements. However, existing safety-driven methods often suffer from aggressive over-editing, which compromises the advertiser's original semantic intent merely to satisfy compliance. In this work, we target the rectification of textual violations in video ads, covering both speech transcripts and on-screen text. ...

---

### 21. Evaluating RAG Metrics in Applied Contexts: An Experiment, Its Findings and Its Limitations

**Authors:** Quentin Brabant

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07302v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07302v1)

**Summary:** This paper reports an empirical study evaluating the relevance of several RAG metrics. The experiment is based on a question-answering dataset created by human annotators from business data. The generated responses and retrieved spans of a RAG system are scored using evaluation metrics from four libraries (Ragas, DeepEval, RAGChecker, Opik). These metrics are compared to scores given by two evaluators, as well as to standard metrics such as recall. An analysis of correlations is conducted. Final...

---

### 22. Multimodal Voice Activity Projection for Turn-Taking in Social Robots with Voice-Activity-Related Pretrained Encoders

**Authors:** Antonio Cano, Guillermo Pérez, Luis Merino, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07294v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07294v1)

**Summary:** Turn-taking prediction is a key requirement for social robots involved in human-human interaction, particularly in mediator settings, where the robot must anticipate conversational dynamics rather than merely react to pauses. This work presents a Multimodal Voice Activity Projection (MM-VAP) framework that extends the original audio-only VAP formulation to synchronized audio-visual inputs while preserving its self-supervised future-projection objective. The proposed approach builds on pretrained...

---

### 23. A Word-Level Digital Reader of the Prasthanatrayi with Sankara's Bhasya: Corpus, Method, and an Open, Offline Reading Aid for the Advaita Vedanta Canon

**Authors:** Tamal Maharaj

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07282v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07282v1)

**Summary:** The Prasthanatrayi -- the ten principal Upanisads, the Brahmasutra, and the Bhagavadgita, with Sankara's commentaries (bhasya) -- is the foundational corpus of Advaita Vedanta. Continuous euphonic combination (sandhi), long compounds (samasa), and dense scholastic prose make it hard to read at the word level: where one word ends, and what each word means grammatically, are both obscured. We present an open, fully offline, word-level digital reader of the entire Prasthanatrayi with Sankara's bhas...

---

### 24. Understanding Interpretation Difficulty in Harmful Online Communication: Insights from Cybercrime Communities

**Authors:** Tomohiro Okatsu, Naoki Takada, Yin Min Pa Pa, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07277v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07277v1)

**Summary:** Harmful online communication often contains slang, coded terms, abbreviations, and community-specific expressions, which make messages difficult to interpret. This paper presents an exploratory study of interpretation difficulty in Discord chats related to cybercrime. We construct reference interpretations of purposefully selected difficult messages, which were reviewed by an expert. We then use them to evaluate human and large language model (LLM) interpretations under different context conditi...

---

### 25. Billions of Sketches Reveal Hidden Cultural Variation in Human Concepts

**Authors:** Arianna Pera, Mauro Martino, Nima Dehmamy, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07267v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07267v1)

**Summary:** Claims about the universality of human concepts have been predominantly assessed through linguistic similarity across languages and cultures. However, words are effective as communication devices because they compress rich experiential variation into shared conventions, potentially obscuring hidden individual and cultural differences in how concepts are mentally represented. Here, we analyse 2.6 billion human-made sketches of common concepts from 236 countries and territories to examine conceptu...

---

### 26. Evaluation of Multilingual Ability to Use Spatial Deictic Expressions in Vision-Language Models

**Authors:** Kaito Watanabe, Taisei Yamamoto, Tomoki Doi, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07251v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07251v1)

**Summary:** One of the expected abilities of vision-language models (VLMs) is spatial reasoning ability based on a given text and image. To evaluate the spatial reasoning abilities of VLMs, we focus on the use of spatial deictic expressions, which are defined as spatial expressions whose referent is determined by their situational context, such as ``this'' and ``that''. To handle spatial deictic expressions, VLMs must jointly reason over language and visual space, grounding context-dependent references in t...

---

### 27. Recovering Latent Structures after Variational Bayesian Variable Selection: Fit Assessment and Factor-Number Selection in Partially Exploratory Factor Analysis

**Authors:** Jinsong Chen, Yi Jin

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07159v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07159v1)

**Summary:** In partially exploratory factor analysis (PEFA), the loading structure and factor numbers are weakly specified. The regularized variational approximation for partially confirmatory factor analysis (PCFA VA) recovers this structure via Bayesian variable selection, using spike and slab priors to assign inclusion probabilities to unspecified loadings. This research introduces a post selection assessment framework for this approach. We convert converged solutions into covariance models using either ...

---

### 28. From Text to Parameters: Predicting Item Parameters from Embedding Regularization with Reliability and Design Ceilings

**Authors:** Shi-Ting Chen, Jinsong Chen

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07141v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07141v1)

**Summary:** Newly developed items must ordinarily be field tested before their psychometric properties are known, creating a cold start problem for item calibration. Predicting item parameters from features is a long standing measurement problem dating back to the Linear Logistic Test Model; modern text embeddings now automate the design matrices traditionally specified by hand. We propose an evaluation framework combining regularized regression on item text embeddings, repeated cross validated R squared re...

---

### 29. Behavior Leverage Imbalance in Multi-Teacher On-Policy Distillation

**Authors:** Jiabin Shen, Guang Chen, Chengjun Mao

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07050v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07050v1)

**Summary:** Agentic language models must learn when to call tools, when to consume tool responses, and when to answer directly. This makes multi-teacher on-policy distillation a natural training strategy: one teacher can specialize in tool calls, another in direct responses, and the student can learn from both on   its own generated distribution. We show that this strategy can induce a behavior shift that is invisible from aggregate losses alone. In a two-teacher tool-use setting, vanilla generalized knowle...

---

### 30. Riemannian Geometry for Pre-trained Language Model Embeddings

**Authors:** Szczepan Konior, Alexandre Quemy, Przemysław Klocek, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07047v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07047v1)

**Summary:** Understanding the geometric structure of pre-trained language model embeddings matters for interpretability and safety. We ask whether sentence-level classification signal lives in the Riemannian geometry of contextual token embeddings, and probe it by extracting per-token pullback metrics from a learned encoder's analytical Jacobian and aggregating them with the Fréchet mean on the symmetric positive definite (SPD) manifold; we call this procedure Riemannian Mean Pooling (RMP). Across three dat...

---

### 31. Dissociating the Internal Representations of Sycophancy in LLMs

**Authors:** Anthony Baez, Sheer Karny, Pat Pataranutaporn

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07003v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07003v1)

**Summary:** Large Language Models (LLMs) frequently exhibit sycophancy, where they agree with a user's statement even when incorrect. While sycophancy is often treated as a single defined behavior, it can manifest in substantially distinct ways and circumstances, raising the question of whether this multi-faceted nature is reflected in its internal mechanisms. To address this gap, we dissociate the representations of sycophancy into factual and opinion subtypes -- motivated by the distinction between verifi...

---

### 32. MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

**Authors:** Ruilin Tong, Dong Gong

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06974v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06974v1)

**Summary:** Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection polic...

---

### 33. Large Language Models (LLMs) and Generative AI in Cybersecurity and Privacy: A Survey of Dual-Use Risks, AI-Generated Malware, Explainability, and Defensive Strategies

**Authors:** Kiarash Ahi, Saeed Valizadeh

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06963v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06963v1)

**Summary:** Large Language Models (LLMs) and generative AI (GenAI) systems, such as ChatGPT, Claude, Gemini, LLaMA, Copilot, Stable Diffusion by OpenAI, Anthropic, Google, Meta, Microsoft, Stability AI, respectively, are revolutionizing cybersecurity, enabling both automated defense and sophisticated attacks. These technologies power real-time threat detection, phishing defense, secure code generation, and vulnerability exploitation at unprecedented scales. Following a rapid surge where LLM-generated malwar...

---

### 34. Comprehensive Evaluation of Large Language Model Responses: A Multi-Factor Scoring System

**Authors:** Yiming Gai, Junde Lu, Xuefei Huang

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06940v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06940v1)

**Summary:** The remarkable performance of large language models (LLMs) in linguistic tasks underscores an urgent need for comprehensive evaluation of their response quality. Prevailing methods, often confined to singular dimensions, fall short of capturing the full spectrum of model capabilities. This study introduces a multifactor scoring paradigm, integrating accuracy, conciseness, factual consistency, readability, and coherence, complemented by a graphical user interface (GUI) for visualizing outcomes. E...

---

### 35. Geometric Self-Distillation for Reasoning Generalization

**Authors:** Josip Jukić, Ivan Titov

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06855v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06855v1)

**Summary:** On-policy distillation is a practical post-training recipe for large language models, supplying dense teacher supervision on the student's own trajectories. In privileged-context self-distillation, teacher and student are the same model conditioned on the same prefix, but the teacher also sees a hint or the full solution trace. This makes supervision abundant but harder to trust: the teacher can be confident about continuations its privileged view makes obvious but the student cannot yet justify...

---

### 36. LLMs Silently Correct African American English: Auditing and Mitigating Dialect Bias via Activation Steering

**Authors:** Huan Wu, Ali Emami, Muhammad Furquan Hassan, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06845v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06845v1)

**Summary:** African American English (AAE), a rule-governed dialect spoken by over 30 million people, is routinely misinterpreted and "corrected" by large language models (LLMs). Across six instruction-tuned LLMs (14B to 70B), we show that state-of-the-art models systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, effectively rewriting AAE into SAE. We present an end-to-end framework to audit and mitigate this bias. For auditing, we introduce condit...

---

### 37. Gradient-Based Speech-to-Text Alignment for Any ASR Model: From CTC to Speech LLMs

**Authors:** Albert Zeyer, Ralf Schlüter, Hermann Ney

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06831v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06831v1)

**Summary:** Speech-to-text alignment means finding the temporal boundaries of each word in the audio. Some models provide such an alignment directly and others do not. Connectionist temporal classification (CTC) and transducer models have an alignment by construction, whereas attention-based encoder-decoders (AED) and speech large language models (LLMs) do not, and their word timings are usually read off the attention weights instead. All of these signals live on the encoder frame grid, which bounds their t...

---

### 38. Ad Headline Generation using Self-Critical Masked Language Model

**Authors:** Yashal Shakti Kanungo, Sumit Negi, Aruna Rajan

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06818v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06818v1)

**Summary:** For any E-commerce website it is a nontrivial problem to build enduring advertisements that attract shoppers. It is hard to pass the creative quality bar of the website, especially at a large scale. We thus propose a programmatic solution to generate product advertising headlines using retail content. We propose a state of the art application of Reinforcement Learning (RL) Policy gradient methods on Transformer based Masked Language Models. Our method creates the advertising headline by jointly ...

---

### 39. Trees from Marginals: Autoregressive drafting with factorized priors

**Authors:** Yuma Oda, Ryan Mathieu, Roman Knyazhitskiy, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06763v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06763v1)

**Summary:** Speculative decoding greatly increases the interactivity of autoregressive language models by trading off computation for extra tokens generated in a single forward pass. Factorized draft models are especially efficient because they predict future-token marginals in parallel, but their independence assumption causes acceptance rates to degrade sharply as the speculative budget grows. We analyze this limitation and introduce Weaver, a lightweight autoregressive adapter that constructs proposal tr...

---

### 40. When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning

**Authors:** Yotam Wolf, Noam Wies, Amnon Shashua

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06720v1)

**Summary:** Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines a prior and self-reflection provides feedback for posterior updates, and study the resulting inference-time sampling complexity - the number of sequential attempts needed to achieve ...

---

### 41. Rethinking Indic AI from a Lens of Cultural Heritage Preservation

**Authors:** Aparna Madva, Sharath Srivatsa, Srinath Srinivasa, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06544v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06544v1)

**Summary:** As Artificial Intelligence (AI) makes inroads into different parts of the Indian subcontinent, there is significant interest in studying how AI impacts the linguistic and cultural foundations of this civilization. AI is seen as a ''double-edged sword'' where on the one hand, it can enable access and inclusion for a large population, on the other, it can homogenize worldviews and exclude underrepresented languages and worldviews. In this paper, we try to characterize this problem by addressing th...

---

### 42. On the feasibility of dependency parsing of non-human sequences without a gold standard. Is evaluation possible in other species?

**Authors:** Ramon Ferrer-i-Cancho, Catherine Hobaiter, Thore Bergman, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06542v2) | 📄 [PDF](https://arxiv.org/pdf/2607.06542v2)

**Summary:** Dependency parsing consists of finding a tree representation for a sequence. Unsupervised dependency parsing aims to develop parsing methods without a gold standard during model training. In human languages, an unsupervised parser can be evaluated because some gold standard is usually available or can be created. For other species, a gold standard is unknown. Thus one may conclude that it is impossible to determine the accuracy of an unsupervised parser and, consequently, dependency parsing is u...

---

### 43. Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs

**Authors:** Zhenyu Liu, Yunxin Li, Xuanyu Zhang, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06540v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06540v1)

**Summary:** Developing seamless, high-performance, native intelligent full-duplex Spoken Language Models (SLMs) remains a critical challenge and long-standing goal for the speech and NLP community. Despite notable progress, recent endeavors are fundamentally constrained by severe modality interference, which causes substantial knowledge degradation and compromises semantic integrity -- ultimately making full-duplex SLMs feel unnatural and unintelligent. In this paper, through an exhaustive fine-grained anal...

---

### 44. Life Style Levels: Neighborhood Delineation using Geospatial Data

**Authors:** Srivatsa Kulkarni, Debarag Banerjee

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06529v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06529v1)

**Summary:** Fine-scale socioeconomic information is often unavailable across rapidly ur-banizing regions of the developing world, like India, limiting the ability to delineate intra-urban variations in affluence and deprivation. This study pro-poses a scalable, grid-based urban delineation framework using building morphology derived from open-source satellite imagery. Urban areas across 59 Indian cities and towns are partitioned into high-resolution spatial grids and characterized using interpretable morpho...

---

### 45. RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation

**Authors:** Sambaran Bandyopadhyay, Ananth Muppidi

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06527v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06527v1)

**Summary:** Multi-hop Question Answering over Knowledge Graphs faces a critical challenge: traditional retrieve-then-read pipelines break differentiability, preventing the retriever from learning to bridge the semantic gap where intermediate nodes lack lexical overlap with the query. To address this, we propose RSF-GLLM, a framework decoupling differentiable graph reasoning from answer generation. Our Recurrent Soft-Flow (RSF) module employs a GRU-guided query updater to propagate continuous relevance score...

---

### 46. DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop Retrieval-Augmented Generation

**Authors:** Yaqi Wu, Xiaolei Guo, Chenyu Zhou, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06507v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06507v1)

**Summary:** Multi-hop retrieval-augmented generation (RAG) acquires evidence sequentially, with each new document potentially revealing missing facts, bridge entities, query defects, or sufficient support for answering. Existing methods provide useful operations such as iterative retrieval, query reformulation, evidence critique, and sufficiency judging, but typically organize them within method-specific pipelines or predefined control topologies. This leaves underexplored how to learn a shared state-condit...

---

### 47. Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated Real-Time Monte Carlo Engine

**Authors:** Juan S. Santillana

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06495v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06495v1)

**Summary:** Live sports commentary is grounded generation under a deadline: statements concern real, named athletes, the grounding state changes every few seconds, and no reference text exists at generation time. We present Pitwall, a production system that generates natural-language Formula 1 strategy briefings in English, Spanish, and Portuguese, treating faithfulness as an architectural property rather than an aspiration: every published sentence is decomposed into typed factual claims (positions, gaps, ...

---

### 48. Data Analysis in the Wild: Benchmarking Large Language Models Against Real-World Data Complexities

**Authors:** So Hasegawa, Shailaja Keyur Sampat, Lei Liu, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06482v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06482v1)

**Summary:** Current benchmarks for evaluating Large Language Models (LLMs) in data analysis often fail to reflect real-world settings. They typically focus on fact retrieval from small tables and overlook the challenges of large multi-tabular datasets, external knowledge integration, and exploratory insight discovery. We introduce DataGovBench, a benchmark derived from governmental open data designed to evaluate LLMs in practical scenarios. The benchmark includes two tasks: Table QA that requires solving co...

---

### 49. WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS

**Authors:** Sihang Nie, Jinxin Ji, Xiaofen Xing, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06461v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06461v1)

**Summary:** While recent Large Language Model (LLM)-based Text-to-Speech (TTS) systems have achieved remarkable naturalness, they predominantly rely on implicit end-to-end generation paradigms, resulting in coarse-grained control. In scenarios demanding precise stylistic interventions and strict temporal alignment, such as audiobook narration and video dubbing, the inability to explicitly manipulate word-level acoustic attributes remains a critical bottleneck. This limitation is primarily amplified by the s...

---

### 50. From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ 14b

**Authors:** Taeyun Roh, Eunha Lee, Wonjune Jang, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06452v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06452v1)

**Summary:** Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a question-type-specific large language model (LLM) framework for BioASQ 14b Task B, designed to improve answer robustness and evidence grounding in biomedical question answering. Rather than applying a single prompting strategy to all questions, the framework selects different inference procedures f...

---

## cs.CV

**50 papers**

### 1. Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF

**Authors:** Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07693v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07693v1)

**Summary:** Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that subs...

---

### 2. Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence

**Authors:** Shuailei Ma, Jiaqi Liao, Xinyang Wang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07675v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07675v1)

**Summary:** Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visual fidelity and creativity over computational efficiency and physical realism. In this work, we present LingBot-Video, a DiT-based video pretraining paradigm specifically tailored for embodied intelligence. From the architecture perspective, we adopt the Mixture-of-Experts (MoE), instead of dense, f...

---

### 3. MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models

**Authors:** Hyunjae Kim, Dain Kim, Pan Xiao, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07673v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07673v1)

**Summary:** Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable frame...

---

### 4. Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation

**Authors:** Hongyu Qu, Jianzhe Gao, Xiaobin Hu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07608v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07608v1)

**Summary:** Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multim...

---

### 5. Cardiac MRI Through-Plane Super-Resolution Guided by Reference and Memory

**Authors:** Shaoming Pan, Chenchuhui Hu, Leon Axel, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07581v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07581v1)

**Summary:** Clinical cardiac MRI is commonly acquired with high in-plane resolution but coarse through-plane resolution to reduce scan time and accommodate breath-hold and cardiac-motion constraints, which limits 3D analysis and diagnostic accuracy. We propose STRMSR, a reference- and memory-guided through-plane super-resolution (SR) framework that reconstructs high-resolution (HR) cardiac volumes by leveraging HR reference views acquired from the same subject and intermediate SR results as the memory. Our ...

---

### 6. Automatic Echocardiography Segmentation via Transition Probability Correlation for Stable Semantic Extraction

**Authors:** Xinran Chen, Xiyuan Wang, Guangquan Zhou, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07580v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07580v1)

**Summary:** While echocardiography is essential for cardiovascular diagnosis, inherent speckle noise and low signal-to-noise ratio often lead to ambiguous semantic features and fragmented boundaries. These limitations significantly hinder the segmentation accuracy of deep learning models in complex clinical cases. Moreover, temporal motion of the heart plays a critical role in recognizing anatomical structures. To address these challenges, we designed a STLSF module which comprises a window-matching-based s...

---

### 7. AA-ViT: Anatomically Aware Vision Transformer with Structural and Frequency Guidance for Contrast Enhanced Brain MRI Synthesis

**Authors:** Talha Meraj, Tom Flannery, Charlie Cummins, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07553v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07553v1)

**Summary:** Accurate tumour localization and diagnosis is a critical component of clinical care for brain cancers. Magnetic Resonance Imaging (MRI) is the most commonly used imaging modality due to its superior soft-tissue contrast. However, standard MRI often exhibits limited contrast and imaging artifacts, which necessitates the use of contrast agents to enhance lesion visibility. The administration of chemical contrast agents is not always feasible and may be contraindicated in patients with renal impair...

---

### 8. Face-trace: Open-Set Attribution and Progressive Discovery of Synthetic Face Generators

**Authors:** Alessia Infantino, Claudio Schiavella, Irene Amerini

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07545v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07545v1)

**Summary:** Recent advances in generative Artificial Intelligence have made synthetic face images increasingly realistic, creating new challenges for multimedia forensics. Source attribution methods should not only identify the generator of an image when the source is known, but also handle samples produced by previously unseen models. However, most existing approaches address synthetic face attribution in a closed-set setting, where all possible generators are available during training. This assumption doe...

---

### 9. SonoRank: Towards Calibration-Free Real-Time Finger Flexion Detection from Forearm Ultrasound Sequences

**Authors:** Dean Zadok, Alon Wolf, Alex M. Bronstein, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07542v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07542v1)

**Summary:** Powered prosthetic hands are frequently abandoned, largely due to the limited functionality of current devices that rely on surface electromyography (sEMG). Sonomyography (ultrasound) has emerged as a promising alternative, owing to its ability to observe muscle activity in real time and control a greater number of degrees of freedom. Yet, existing ultrasound-based methods require per-user fine-tuning, limiting their commercialization. We propose SonoRank, an important step towards calibration-f...

---

### 10. Infinite Worlds with Versatile Interactions

**Authors:** Zelin Gao, Qiuyu Wang, Jiapeng Zhu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07534v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07534v1)

**Summary:** We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon while maintaining consistent output quality, benefiting from a carefully crafted causal pretraining paradigm. (2) Through distilling a real-time variant from the base model, our system guarantees rapid response time, sufficient to drive 720p video streams at 60 fps. (3) Compared to the previous versio...

---

### 11. Context-Aware Slum Mapping in Sub-Saharan Africa Using Sentinel-1 Texture and Local Climate Zones

**Authors:** Peterson Chepkilot, Babak Memar, Paolo Gamba

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07532v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07532v1)

**Summary:** Accurate mapping of informal settlements remains a major challenge in Sub-Saharan African (SSA) cities because optical imagery often fails to distinguish Informal Settlements (defined here as LCZ 7) from spectrally similar formal Compact Low-Rise areas (LCZ 3). This study presents a context-aware, reproducible Optical-SAR framework that improves informal settlement delineation using Sentinel-2 spectral features and Sentinel-1 structural information within an adapted Local Climate Zone (LCZ) taxo...

---

### 12. Learning to Unify Deformable Shape and Texture Representations for Cardiac Video Classification

**Authors:** Tonmoy Hossain, Miaomiao Zhang

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07518v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07518v1)

**Summary:** Deformable shape representations have proven to be robust complements to texture features in cardiac image classification, offering geometric priors that are invariant to imaging artifacts and intensity variations. However, existing deep networks perform simple concatenation to combine these distinct feature representations, which neither fully exploits their complementary nature nor learns cross-modal feature dependencies. Furthermore, this results in uniform attention across all timepoints; he...

---

### 13. HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models

**Authors:** Feng He, Zhenting Wang, Qifan Wang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07507v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07507v1)

**Summary:** Hallucinations in vision language models (VLMs) are commonly treated as semantic errors, yet they often arise from partial or ambiguous visual evidence. Prior work mainly focuses on detecting or suppressing hallucinations at generation time, leaving the subsequent reasoning stage largely unexplored. In this work, we study Post Hallucination Reasoning (PHR), the stage in which hallucinated semantics enter the model's inference context and influence downstream predictions. To systematically invest...

---

### 14. Discovering Geometric Biases in 3D Face Reconstruction: A Curvature-Aware Spectral Framework for Fairness Evaluation

**Authors:** Veronika Shilova, Emmanuel Malherbe, Giovanni Palma, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07486v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07486v1)

**Summary:** 3D Morphable Models (3DMMs) remain the standard parametric shape priors for many state-of-the-art 3D face reconstruction algorithms. However, as these models are derived from a finite number of 3D face samples, they inherit the morphological biases of their training data, potentially limiting their generalizability across diverse global populations. In this paper, we propose a novel framework to analyze 3DMM reconstructions through the lens of surface curvature, with the objective to discover, q...

---

### 15. A Theory of Contrastive Learning with Natural Images

**Authors:** Antonio Torralba, Yair Weiss

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07470v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07470v1)

**Summary:** Why does contrastive learning with simple images and augmentations yield useful representations for downstream tasks? We address this question by analytically computing the optimal representation in terms of a contrastive loss for a range of basic augmentations and any image dataset with stationary statistics. We show that for certain augmentations the optimum can be attained by a CNN whose first layer filters are sinusoids, followed by a pointwise nonlinearity, global average pooling, and a fin...

---

### 16. EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI

**Authors:** Xinjie Wang, Liu Liu, Taojun Ding, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07459v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07459v1)

**Summary:** We present EmbodiedGen V2, a generative 3D world engine for building executable sim-ready environments for embodied intelligence. Sim-ready 3D asset generation has advanced rapidly, yet assembling such assets into policy-ready task environments remains largely manual, limiting scalable closed-loop learning. EmbodiedGen V2 addresses this gap through a unified sim-ready representation that connects cross-simulator assets, interaction affordances, task-driven worlds, large-scale multi-room scenes, ...

---

### 17. Two-Stage Multi-Modal Fusion with Adaptive Alignment for Action Quality Assessment

**Authors:** Kanglei Zhou, Ruizhi Cai, Xinning Wang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07438v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07438v1)

**Summary:** Action Quality Assessment (AQA) aims to evaluate how well a person performs a movement, which is essential in applications such as sports scoring, skill assessment, and healthcare. However, unimodal approaches often struggle to capture subtle cues of movement quality in real-world settings. Although multi-modal inputs provide complementary information, existing methods still face two major challenges: heterogeneous modalities often lead to cross-modal misalignment and unstable fusion, and reliab...

---

### 18. VCDP: Variation-Conditioned Distributional Proxy Learning for Semi-Supervised Medical Image Segmentation

**Authors:** Zimu Zhang, Yiheng Zhong, Zhuoru Zhang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07416v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07416v1)

**Summary:** Semi-supervised 3D medical image segmentation reduces the need for dense voxel-level annotations by exploiting unlabeled volumes. Although existing methods such as consistency regularization, pseudo-labeling, and co-training improve prediction-level robustness, they often provide insufficient feature-space organization for anatomically complex structures, especially small organs and ambiguous boundary regions with large intra-class variations. To address this issue, we propose Variation-Conditio...

---

### 19. Heterogeneity-Adaptive Diffusion Schrodinger Bridge for PET-Guided Whole-Body MRI Translation

**Authors:** Chengbo Wang, Jiacheng Yu, Linjie Bian, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07401v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07401v1)

**Summary:** While whole-body multimodal medical imaging scanners have been increasingly recognized for more effective medical applications, the excessive long acquisition time in PET-MR scanning is a major obstacle in more efficient clinical practice. Deep learning-based MRI translation provides a potential solution to reduce scan duration. However, current models often focus on specific anatomical regions and face challenges for whole-body scans that consists of highly heterogeneous feature distributions m...

---

### 20. When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated VLMs

**Authors:** Tanay Sodha, Aditya Sharma, Ramya Hebbalaguppe, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07395v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07395v1)

**Summary:** Reliable confidence estimation remains a key limitation of test-time adaptation in vision-language models (VLMs), where prompt tuning improves zero-shot accuracy but often degrades calibration due to entropy-driven overconfidence. Prior approaches mitigate this using LLM-derived class attributes and contrastive regularization, yet treat attributes independently, ignoring their relational structure. We propose ARGTCA, which represents (class, attribute) pairs as nodes in a Symbolic Attribute Grap...

---

### 21. MMAgent-R$^2$: Learning to Rerank and Reject for Agentic mRAG

**Authors:** Tao Zhang, Ziqi Zhang, Zongyang Ma, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07383v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07383v1)

**Summary:** Knowledge-based Visual Question Answering (KB-VQA) requires models to retrieve visual entities matching the query image from large-scale encyclopedic knowledge bases and answer related questions. Existing multimodal Retrieval Augmented Generation (mRAG) methods rely on global visual features to match candidate entities, yet when the knowledge base contains numerous visually similar entities, the retriever struggles to distinguish them, populating the candidate set with visually similar but factu...

---

### 22. BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning

**Authors:** Jiacheng Yang, Tongying Xiao, Yunkai Dang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07361v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07361v1)

**Summary:** Current Vision-Language Models (VLMs) often struggle to handle complex visual tasks that require consistent and fine-grained reasoning. Recent methods aim to train models to facilitate self-reflective reasoning, i.e., reviewing and improving the generated reasoning. However, they require large volumes of annotated data and lack explicit reflective behavior during test time. This work aims to bridge this gap through inspiration from neuroscience. The human brain exhibits efficient backward predic...

---

### 23. HAJJv2-CrowdCount: Zero-Shot Benchmark for Dense Crowd Counting

**Authors:** Reem AlYabis, Fares AlTuwaim, AlJawharh AlOtaibi, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07322v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07322v1)

**Summary:** Automated crowd counting in Hajj video is difficult not because current models lack capacity, but because the footage violates the assumptions those models were built on: cameras observe the crowd from steep, near-vertical angles, individuals occlude one another extensively, and a single frame can contain well over a thousand people. Benchmarks that test crowd counting in such an environment are either private or not detailed per second. We revisit the HAJJv2 dataset and contribute HAJJv2-CrowdC...

---

### 24. SoccerNet 2026 Challenges Results

**Authors:** Anthony Cioppa, Silvio Giancola, Håkan Ardö, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07320v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07320v1)

**Summary:** The SoccerNet 2026 Challenges constitute the sixth annual edition of the SoccerNet open benchmarking effort, dedicated to advancing computer vision research in sports video understanding. This year's challenges span five vision-based tasks: (1) Ball Action Anticipation, predicting the timing and class of ball-related actions within a short future window from a preceding observation window; (2) Player-Centric Ball Action Spotting, temporally localizing and classifying ball-related actions while a...

---

### 25. CarbonCLIP: Enhance Carbon Prediction from Satellite Imagery via Integrated Street-View Semantics and Temporal Context Training

**Authors:** Zeru Yang, Fang-Ying Gong, Steve H. L. Yim, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07292v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07292v1)

**Summary:** Accurately estimating urban carbon emissions is critical for sustainable urban planning, yet many existing approaches remain difficult to apply consistently across cities due to data-source heterogeneity and the lack of fine-grained semantic-temporal context in remote sensing data. We propose CarbonCLIP, a task-oriented multimodal distillation framework that improves satellite-based carbon emission prediction by transferring contextual knowledge into a unified satellite representation through du...

---

### 26. InfraQR: Edge-Placed QR-Inspired Structured Patch Attacks on Infrared Vision-Language Models

**Authors:** Xin Li, Jiaju Han, Ma Yaqi, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07288v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07288v1)

**Summary:** Infrared vision-language models are increasingly used for perception under low-light and adverse visual conditions, yet their robustness to localized structured perturbations remains underexplored. Existing infrared adversarial studies mainly focus on object detectors, leaving the security of infrared vision-language models less systematically examined. We present InfraQR, a QR-inspired structured patch attack for infrared vision-language models. Unlike localized attacks that attach perturbation...

---

### 27. Naming the Concepts Classifiers Rely On: Language-Anchored Decomposition for Faithful Explanation

**Authors:** Ahsan Habib Akash, Dipkamal Bhusal, Stacey Jones, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07264v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07264v1)

**Summary:** Deep neural networks are widely deployed in high-stakes visual applications where interpretability is critical, yet existing explanations face a trade-off: post-hoc concept methods recover factors that are faithful to a model's behavior but unnamed, while naming and by-design methods attach human-readable concepts only by retraining or altering the classifier. We propose Language-Anchored Decomposition (LAD), a post-hoc framework that delivers concepts which are simultaneously named, faithful, a...

---

### 28. An Edge-aware Prompt-enhanced SAM for Ultrasound Image Segmentation

**Authors:** Wenhao Li, Fangyi Liu, Bo Du

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07240v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07240v1)

**Summary:** Ultrasound image segmentation is essential for delineating anatomical structures and lesions, providing the foundation for accurate diagnosis. While the Segment Anything Model (SAM) has demonstrated remarkable success on natural images, its performance on ultrasound data is often hindered by poor boundary delineation. To address this limitation, we propose EP-SAM, an edge-aware and prompt-enhanced adaptation of SAM. Specifically, we leverage multi-block feature extraction from the image encoder ...

---

### 29. Unraveling Machine Behavior by Multi-Level Bias Analysis and Detection: Methodology and Application to Computer Vision

**Authors:** Ignacio Serna, Aythami Morales, Julian Fierrez

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07236v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07236v1)

**Summary:** This study investigates the presence and propagation of bias within Neural Networks through a comprehensive multi-level analysis spanning the learned latent space, layer activations, and the network's parameters. Based on this taxonomy, we propose three bias detection approaches: 1) SpaceBias (new method), which characterizes the latent space prior to the final classification layer using neighbor-probability distributions and quantifies bias with the two-sample Kolmogorov-Smirnov test on the per...

---

### 30. `Attention-Guided Cross-Temporal Clustering for Self-Supervised Video Object Segmentation

**Authors:** Waqas Arshid, Mohammad Awrangjeb, Alan Wee-Chung Liew, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07230v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07230v1)

**Summary:** Video object segmentation (VOS) is a fundamental task in video understanding, requiring accurate delineation and consistent tracking of objects across frames. While supervised methods achieve strong performance, they rely on densely annotated datasets that are costly to obtain and have limited domain coverage. Self-supervised learning offers a promising alternative by removing the need for manual labels; however, existing approaches often struggle to jointly maintain spatial accuracy and tempora...

---

### 31. Vision Foundation Models in Radiology: A Scoping Review of Data, Methodology, Evaluation and Clinical Translation

**Authors:** Alejandro Vergara-Richart, Xavier Rafael-Palou, Almudena Fuster-Matanzo, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07219v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07219v1)

**Summary:** Vision foundation models (VFMs) are increasingly being developed for radiological imaging, yet their definition, development and evaluation remain heterogeneous. We conducted a PRISMAScR scoping review of peer-reviewed studies published between January 2017 and March 2026 describing foundation models trained exclusively on radiological imaging data. Sixty-seven studies were included and mapped across three pillars: data scale and heterogeneity, architectural and pretraining scalability, and down...

---

### 32. Why Fake ? Unveiling the Semantic Vocabulary of Deepfake Detectors

**Authors:** Vazgken Vanian, Alexandros Doumanoglou, Dimitris Zarpalas

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07216v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07216v1)

**Summary:** Deepfake (DF) technology poses a significant threat to information integrity, driving the need for robust detection methods. Most DF detectors only consider predicting a binary label for whether the input is real or fake, lacking the justification required for real-world applications like legal proceedings. Explainable DF Detection has emerged to address this limitation, but existing techniques frequently fall short by either relying on human annotations for precise artifact localization or gene...

---

### 33. DiffCVE: Diffusion-based Compressed Video Enhancement

**Authors:** Wenqiang Xiao, Wenzhuo Ma, Junxi Zhang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07195v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07195v1)

**Summary:** Perceptual quality enhancement of severely compressed videos remains challenging due to complex artifact patterns and substantial information loss. Recent diffusion models have demonstrated strong generative capability for visual restoration, but directly applying them to compressed video often ignores compression degradation characteristics and may introduce structure-inconsistent hallucinations. To address this issue, this paper presents a diffusion-based compressed video enhancement method, n...

---

### 34. Prototype-Anchored Generalized Manifold Regression for Unknown-Domain Object Detection

**Authors:** Zihao Zhang, Aming Wu, Yang Li, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07192v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07192v1)

**Summary:** In this paper, we study Single-Domain Generalized Object Detection (Single-DGOD), which aims to transfer a detector trained on a single source domain to multiple unseen domains. Existing methods mainly rely on simulation-driven strategies, such as data augmentation or textual prompts, to enlarge the training distribution. However, finite simulations can hardly cover the dynamic variations of real-world scenarios, often causing overfitting to synthetic styles and limited robustness to complex str...

---

### 35. EditVerse3D: High-Quality 3D Object Editing with Region-Aware Learning

**Authors:** Youtan Yin, Yanning Zhou, Jiacheng Wei, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07187v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07187v1)

**Summary:** Local editing of 3D objects remains a long-standing challenge. When interacting with 3D content, humans naturally tend to specify a coarse region of interest for modification rather than defining precise editing boundaries. However, previous methods rely on fully edited 2D images, precise 3D masks, or redundant pipelines, which present a gap. To bridge this gap, we propose EditVerse3D, a novel 3D editing framework that enables high-quality object editing under such coarse guidance. Our approach ...

---

### 36. Comparative Study of Domain-adapted VLMs for General Document Visual Question Answering

**Authors:** Miguel Lopez-Duran, Elena Marrero, Julian Fierrez, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07179v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07179v1)

**Summary:** Document Visual Question Answering (DocVQA) presents a complex multimodal challenge, requiring models to exploit visual, textual, and layout information from documents. Although Vision-Language Models (VLMs) have shown remarkable performance in text-vision tasks, their robustness and transferability to different document domains remains underexplored. In this study, we present a comprehensive evaluation of 8 open-source pretrained VLMs on DocVQA in three different document domains: industrial do...

---

### 37. Towards Accurate and Fast Clinical Body Composition: A Resource-Efficient Hierarchical Segmentation Framework for Multi-Source CT

**Authors:** Xiaodi Shen, Qingzhu Zheng, Yaoyang Qiu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07177v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07177v1)

**Summary:** Background: Automated 3D segmentation of muscles and adipose tissue from CT is vital for body composition analysis, but multi-source data heterogeneity and high CPU memory demands hinder clinical deployment.   Methods: We propose a coarse-to-fine hierarchical framework to segment ten tissue structures. Efficiency is optimized using Dynamic Spacing and Anisotropic Patching, a Group Inference mechanism for low-memory sliding-window processing, and Topology-Aware Asymmetric Resampling for fast post...

---

### 38. Stage-Aware Adaptation and Distribution Calibration for Subject-Driven Personalized Text-to-Image Generation

**Authors:** Wenyan Xu, Alizer Wong

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07173v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07173v1)

**Summary:** Subject-driven personalized text-to-image generation requires a pretrained diffusion model to acquire a specific subject from a few reference images while preserving subject identity, following novel text prompts, and maintaining sample diversity. Existing optimization-based methods instantiate subject adaptation through full fine-tuning, textual embedding optimization, or low-rank parameter updates; PaRa further constrains personalization from the perspective of parameter rank reduction. Howeve...

---

### 39. PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation

**Authors:** Yi Yang, Myrna Castillo, Bodo Rosenhahn, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07170v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07170v1)

**Summary:** Online 3D scene graph generation builds a persistent, structured representation of a scene by incrementally fusing 2D observations into a global 3D graph. Existing online methods treat this fusion as a fully deterministic pipeline, where we identify three sources of uncertainty that are overlooked: observation, 2D model, and 3D representation. We propose PUF: a Plug-and-play, Uncertainty-aware, and training-free Fusion framework. Scene graph node association is reformulated as a probabilistic li...

---

### 40. TACoS: Weakly Supervised Learning of Two-Dimensional Materials from Scribble Annotations to Precise Segmentation

**Authors:** Jiabei Chen, Liping Zhang, Jiang-Bin Wu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07169v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07169v1)

**Summary:** The precise pixel-level localization of 2D material flakes is crucial for high-throughput screening. However, traditional fully supervised methods rely on dense annotations, which are costly and time-consuming, severely limiting the practical deployment of segmentation models. This paper proposes TACoS, a specialized scribble segmentation framework tailored for 2D materials. First, we design a unified framework that integrates semi-supervised consistency learning with structured tree energy cons...

---

### 41. NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction

**Authors:** Xiangyu Sun, Liu Liu, Seungkwon Yang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07168v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07168v1)

**Summary:** Pose-Free Feed-forward 3D Gaussian Splatting (3DGS) has recently emerged as a powerful paradigm for fast scene reconstruction. However, its performance degrades significantly in long image sequences due to cumulative camera pose estimation drift, which propagates errors into geometric modeling and severely limits rendering fidelity. In this work, we revisit the long-sequence bottleneck and identify pose drift as the primary factor restricting reconstruction quality. Furthermore, while SfM-based ...

---

### 42. ASFR-Net: Adversarial Alignment and Spatio-Frequency Refinement Network for Heterogeneous Remote Sensing Image Change Detection

**Authors:** Xin-Jie Wu, Zhi-Hui You, Si-Bao Chen, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07161v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07161v1)

**Summary:** The core challenge of heterogeneous change detection in remote sensing imagery lies in effectively decoupling genuine land-cover changes from significant modal disparities caused by distinct imaging mechanisms. These intrinsic inconsistencies are prone to introducing pseudo-changes, thereby constraining detection accuracy. To address this, we propose a novel, end-to-end adversarial spatio-frequency refinement network (ASFR-Net). Initially, a modality-invariant representation learner (MIR-Learner...

---

### 43. Prior-matched evaluation of operational Earth-observation classifiers: a three-number reporting method demonstrated on Sentinel-1 internal-wave detection

**Authors:** Joao Pinelo, Joao Goncalves, Arun Shukla, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07146v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07146v1)

**Summary:** The Internal Waves Service screens the Sentinel-1 Wave-mode archive for internal solitary waves, routing detections to experts whose adjudication time is the resource the effort exists to conserve. Because attention is the cost of error, precision leads. Its classifier was trained and reported at a one-to-one class balance, fixed before the operational rate could be known. That rate has since emerged at roughly one scene in twenty, and a balanced-test score badly overstates the precision a valid...

---

### 44. Sparse Attention for Dense Open-Vocabulary Prediction in CLIP

**Authors:** Fatimah Zohra, Chen Zhao, Shuming Liu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07135v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07135v1)

**Summary:** Contrastive Language-Image Pre-training (CLIP) relies on softmax-based self-attention, a strictly positive distribution that assigns probability mass to every pair of tokens-even semantically irrelevant ones. While these dense softmax weights are effective for gathering broad context during pre-training, they spread attention across many low-salience tokens, producing noise that obscures the fine-grained, spatially localized cues required for dense, open-vocabulary prediction. We study an infere...

---

### 45. Widest-Path Reachability Fields for Connectivity-Preserving Slender Structure Segmentation

**Authors:** Youcheng Zong, Runda Jia, Minxuan Hu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07123v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07123v1)

**Summary:** Segmenting slender curvilinear structures such as retinal vessels, cracks, and roads demands topological correctness, as even a single-pixel discontinuity can fragment a continuous network and invalidate downstream analysis. Under standard binary-mask supervision, models optimized for pixel-level overlap frequently produce topologically broken predictions. We trace this to a fundamental mismatch: pixel-wise losses distribute gradients uniformly, yet connectivity hinges on a sparse set of bottlen...

---

### 46. ColorFM: An Optimization-to-Learning Framework for Color Transfer via Flow Matching

**Authors:** Yuhang He, Kai Zhang, Xiaoming Li, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07119v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07119v1)

**Summary:** Color transfer aims to align the color distribution of a source image with that of a reference image while preserving structural and semantic consistency. However, existing methods often suffer from inaccurate global mapping, semantic misalignment, and visual artifacts. To address these issues, we propose ColorFM, an optimization-to-learning framework. ColorFM connects online optimization to offline inference by reformulating color transfer as the transport of pixel distributions along velocity ...

---

### 47. Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning

**Authors:** Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07117v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07117v1)

**Summary:** In text-to-image in-context learning (T2I-ICL), a model has to infer a latent compositional pattern from fewshot demonstrations for generating a query image. Recent studies show that state-of-the-art multimodal large language models struggle with this setting, particularly due to limited compositional reasoning and sensitivity to prompt construction. In this work, we propose a Tree-of-Thoughts (ToT) reasoning framework for T2I-ICL that introduces a multi-stage reasoning and selection layer that ...

---

### 48. Video-Based Detection of squint and cataract for accessibility-aware adaptive web interface rendering

**Authors:** Amar Ranjan Dash, Manas Ranjan Patra

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07099v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07099v1)

**Summary:** Squint and cataract are major ocular disorders that majorly affect visual perception and interaction capability. This paper proposes a real-time video-based automated detection system for squint and cataract detection based on computer vision and image processing methods. The proposed system uses a media-pipe face-mesh (a 478-point facial landmark detection model) to extract geometric ocular features for multi-class squint classification. Simultaneously, The presence and severity cataract is est...

---

### 49. AT-Attn: Temporal-Aware Cross-Attention for Longitudinal Multimodal Alzheimer's Disease Diagnosis

**Authors:** Xinyue Du, Yibo Liu, Zhenglei Zhou, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07091v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07091v1)

**Summary:** In longitudinal Alzheimer's disease (AD) diagnosis support, clinical and imaging information is often collected at irregular visits. Integrating these multimodal observations may improve diagnostic assessment, but naive fusion can degrade performance when MRI is noisy or intermittently unavailable. We propose AT-Attn, a temporal-aware multimodal framework that combines Change-and-Time encoding, time-biased asymmetric cross-attention, and gated fusion to integrate MRI with longitudinal clinical i...

---

### 50. Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis

**Authors:** Yapeng Li, Bo Jiang, Ziyan Zhang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07077v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07077v1)

**Summary:** Functional brain networks exhibit a hierarchical organization across ROI, community, and whole-brain levels, supporting local processing, inter-community coordination, and global integration. Recent studies have demonstrated that brain community-aware modeling is beneficial for both diagnosis and biomarker identification of brain networks. However, existing brain graph modeling methods often struggle to model ROI-community interactions, thereby failing to fully exploit the hierarchy across ROI, ...

---

## cs.LG

**50 papers**

### 1. Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning

**Authors:** Chen Tang, Yizhou Wang, Jianyu Wu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07708v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07708v1)

**Summary:** Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint ch...

---

### 2. Co-LMLM: Continuous-Query Limited Memory Language Models

**Authors:** Yair Feldman, Linxi Zhao, Nathan Godey, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07707v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07707v1)

**Summary:** Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant ...

---

### 3. The Key to Going Linear: Analysis-Driven Transformer Linearization

**Authors:** Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07706v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07706v1)

**Summary:** The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of ...

---

### 4. Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF

**Authors:** Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07693v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07693v1)

**Summary:** Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that subs...

---

### 5. Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

**Authors:** Vladislav Beliaev

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07690v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07690v1)

**Summary:** Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is r...

---

### 6. ECGLight: Compute-Light Framework For Paper ECG Digitization and Myocardial Infarction Screening

**Authors:** Shreyasvi Natraj, Cyrus Achtari, Felice Gragnano, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07683v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07683v1)

**Summary:** Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited connectivity and computational capacity. As a result, vast numbers of physical ECGs obtained in remote areas still remain incapable of being accessed by contemporary artificial-intelligence (AI)-based decision support as they require high computational resources or strong high-speed internet connectivi...

---

### 7. Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization

**Authors:** Xiangming Huang, Guannan Zhang, Lu Lu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07682v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07682v1)

**Summary:** The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces. This paper introduces a Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES) that integrates dimensionality reduction, representation learn...

---

### 8. Any-Dimensional Learning by Sampling

**Authors:** Eitan Levin, Venkat Chandrasekaran

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07680v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07680v1)

**Summary:** Many machine learning models are defined for inputs of different sizes, such as point clouds containing different numbers of points, sequences of tokens of different lengths, and graphs on different numbers of nodes. Such models are trained on finitely-many examples of necessarily limited sizes. How well do these models generalize from inputs of small size to larger inputs of size not seen during training? Furthermore, evaluating such models on large inputs is often expensive. How can we sketch ...

---

### 9. How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization

**Authors:** Xinyi Wu, Siyuan Liu, Ali Jadbabaie

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07678v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07678v1)

**Summary:** Rotary Position Embeddings (RoPE) provide transformers with a fixed grid of positional frequencies, yet trained models use these frequencies highly non-uniformly. We study what determines this frequency usage and propose a data-centered explanation: RoPE frequencies are selected to match the relative-distance structure of the training data. Viewing each frequency as a positional lens, we formalize a field-resolution tradeoff and show that, for a data-induced dependency profile of width $W$, the ...

---

### 10. Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems

**Authors:** Vladislav Beliaev

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07674v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07674v1)

**Summary:** Group Relative Policy Optimization (GRPO) stalls on a model's hardest problems: when no rollout in a group succeeds, the group-relative advantages vanish and the problem contributes no gradient, wasting the frontier examples we most want to learn from. Prepending a correct prefix of a reference solution raises the success rate, making prefix length a continuous knob on difficulty. Concurrent methods set the knob once; AdaPrefix-GRPO turns it into a feedback controller: throughout training it adj...

---

### 11. MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models

**Authors:** Hyunjae Kim, Dain Kim, Pan Xiao, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07673v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07673v1)

**Summary:** Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable frame...

---

### 12. PeTeR: Post-Training Robustification of Probabilistic Circuits

**Authors:** Adrian Ciotinga, Yeming Dai, YooJung Choi

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07671v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07671v1)

**Summary:** Probabilistic circuits (PCs) can model complex joint distributions while supporting exact and efficient computation of many inference queries. However, standard likelihood-based PC learning is vulnerable to overfitting and fragile generalization when confronted with data noise, small sample sizes, or distribution shifts. This can be mitigated using distributionally-robust optimization which consider worst-case distributions within a Wasserstein ball of the empirical distribution, but current met...

---

### 13. Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity Familiarity from Factual Reliability Across Model Scale

**Authors:** Grzegorz Brzezinka

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07670v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07670v1)

**Summary:** Large language models hallucinate most about entities they have never seen. We ask whether a model's activations betray entity familiarity before a single answer token is generated, and whether that signal predicts the factual reliability of the answers. On four Polish Bielik models (1.5B-11B parameters), we probe four entity domains (athletes, cities, writers, musicians), each with 42 well-known, 42 obscure-but-real, and 42 fabricated entities addressed by a one-sentence question (504 prompts p...

---

### 14. Guidance Breaks the Fitted Operator: A Terminal-Fitted Repair for Classifier-Free Guidance

**Authors:** Shiheng Zhang

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07665v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07665v1)

**Summary:** Classifier-free guidance (CFG) is the standard way to strengthen class-conditioning in diffusion and flow-matching samplers, yet at large guidance it oversaturates and destabilizes, symptoms practitioners suppress with more steps or limited-interval schedules. We analyze CFG through an asymptotic-preserving, numerical-analysis lens. Building on a recent result that the deterministic DDIM step is the unique fitted operator for the unguided terminal layer, exact on the final small-sigma stretch of...

---

### 15. ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation

**Authors:** Xuan-Thong Truong, Trung-Kien Le, Tung Kieu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07640v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07640v1)

**Summary:** Deep learning has significantly advanced time series imputation, yet most existing architectures primarily rely on localized temporal context within the corrupted input sequence. This reliance can be limiting in real-world scenarios, where time series often exhibit non-stationary dynamics, weak temporal correlations, and infrequent patterns that are difficult to reconstruct from nearby observations alone. In this paper, we propose ALER-TI, Aligned Latent Embedding Retrieval for Time Series Imput...

---

### 16. An optimal control approach for neural network architecture adaptation with a posteriori error estimation

**Authors:** C G Krishnanunni, Thomas Scott, Tan Bui-Thanh

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07637v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07637v1)

**Summary:** This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation. By formulating neural network training as a continuous-time optimal control problem, we derive rigorous error estimates that quantify how approximation error distributes across network layers. This error decomposition enables a principled depth adaptation strategy: new layers are inserted at locations of maximum estimated error, allowing the network to efficiently ...

---

### 17. Higher-Order Geometric Updates for Levenberg-Marquardt Method via Riemann Normal Coordinates

**Authors:** Jianing Liu, Dong H. Zhang

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07623v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07623v1)

**Summary:** Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks. Such problems have a natural geometric interpretation, model predictions form a manifold in data space, while the chosen parameterization can introduce parameter-effects curvature that becomes a dominant source of nonlinearity. This exposes a limitation of the Levenberg-Marquardt (LM) method, its tangent-space step is applied as a straight update in parameter coordin...

---

### 18. Asymmetric Focal Loss Improves Graph Neural Network Prediction of Drug-Drug Interactions

**Authors:** Faranak Hatami, Mousa Moradi

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07611v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07611v1)

**Summary:** Background: Graph neural networks improve computational prediction of polypharmacy side effects, but standard binary cross-entropy training allocates equal capacity to well-classified and difficult examples, potentially missing clinically significant interactions. We evaluated whether an asymmetric focal objective could improve multi-relational drug-drug interaction (DDI) prediction by emphasizing difficult positive interactions. Methods: ClinicalFocal loss was integrated into a relation-aware g...

---

### 19. Multi-Class vs. Multi-Label BERT for CVE-to-CWE Mapping: How Taxonomy Structure Shapes the Errors

**Authors:** Ana Schwengber Kelm, Christian Bockermann, Jörg Frochte

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07573v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07573v1)

**Summary:** Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task as a text classification problem and compare two modelling choices: a \emph{multi-class} formulation that predicts a single CWE per CVE and a \emph{multi-label} formulation that allows multiple assignments. Three transformer encoders (BERT Base, SecureBERT, and CySecBERT) are evaluated on three nest...

---

### 20. Collaborative Synthetic Data Generation for Knowledge Transfer in Federated Learning

**Authors:** Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07565v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07565v1)

**Summary:** One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, particularly when client data distributions diverge. Recent work has addressed this challenge by aggregating client knowledge on the server through the construction of transferable synthetic datasets or distillates. However, most of these methods lack formal privacy guarantees, leaving a gap in jointly...

---

### 21. PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning

**Authors:** Yazdan Jamshidi, Alexey Shvets

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07557v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07557v1)

**Summary:** One-shot pruning methods like Wanda and SparseGPT apply the same sparsity ratio to every layer of a transformer, ignoring known variation in layer importance. We propose PALS (Percentile-Aware Layerwise Sparsity), which adjusts per-layer sparsity based on the 99th percentile of activation magnitudes, bounded to $\pm 5\%$ around the target ratio. On LLaMA-2-7B at 50\% sparsity, PALS achieves 10.96 WikiText-2 perplexity versus 12.92 for uniform Wanda (mean over 9 runs, $p < 0.001$). The benefit is...

---

### 22. Avoiding unsafe sets when training with Langevin Dynamics

**Authors:** Adam M. Oberman

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07538v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07538v1)

**Summary:** Training a model with noisy gradient descent can be idealized as overdamped Langevin dynamics on the loss landscape, and a natural safety question is to bound the probability $ν_t(\mathcal{A}_H) = \mathbb{P}(Q_t \in \mathcal{A}_H)$ that the trajectory lies in a designated failure region $\mathcal{A}_H$. We study this for a smooth, strongly convex loss in $d$ dimensions and a failure region separated from the minimizer by an energy gap. Three bounds emerge. At the end of training, the equilibrium...

---

### 23. A Unified Detection Framework for AI-Related Content and Artifacts

**Authors:** Xifeng Zhang, Tao Hu, Yijie Peng, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07527v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07527v1)

**Summary:** Artificial intelligence (AI) is a double-edged sword: while it has achieved remarkable success across a wide range of domains, its deployment also calls for effective oversight and regulation, for which the detection of AI-related content and artifacts is perhaps the most direct and cost-effective approach. To this end, we propose a unified detection framework based on Mahalanobis distance scores (MDS), applicable to several important settings, including the detection of large language model (LL...

---

### 24. Gradient-free Riemannian Langevin Sampler

**Authors:** Ricardo Baptista, Olivier Zahm

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07519v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07519v1)

**Summary:** We address the problem of efficiently sampling multimodal probability distributions, where standard Markov Chain Monte Carlo methods often suffer from poor mixing and mode trapping. To mitigate these issues, we propose Gradient-free Riemannian Langevin Sampler (GRiLS), a novel proposal that improves exploration without requiring gradient evaluations of the target density. Our approach introduces a Riemannian metric which reshapes the local geometry in order to facilitate transitions across modes...

---

### 25. Fast Rates for Semi-Supervised Learning via Data-Augmentation Graph Regularization

**Authors:** Adam M. Oberman

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07513v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07513v1)

**Summary:** Self-supervised learning matches supervised accuracy from a fraction of the labels, but the labeled-sample efficiency behind this has lacked a theoretical explanation. We provide one. Data augmentation induces a similarity graph on the unlabeled data, so downstream learning on that graph is graph-Laplacian-regularized learning. We prove a fast transductive rate, $O(1/n_L)$ in the number of labels, in place of the supervised $O(1/\sqrt{n_L})$, by carrying the leave-one-out stability apparatus of ...

---

### 26. Stability of Flow Models for Graph Signals

**Authors:** Martin Schmidt, Gonzalo Mateos

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07510v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07510v1)

**Summary:** Generating signals on graphs requires permutation-equivariant models that exhibit stability with respect to relative structural perturbations. While favorable stability properties of Graph Neural Networks (GNNs) have been well documented, it is unclear how structural errors propagate through the dynamics of continuous generative flow models that are gaining traction for graph signal generation. In this paper, we analyze continuous normalized flow models parameterized by GNNs and show that permut...

---

### 27. Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

**Authors:** Zhenyu Hou, Yujiang Li, Jie Tang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07508v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07508v1)

**Summary:** Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks. Recently, asynchronous RL has emerged as a more efficient alternative by updating the model as rollouts arrive. However, existing asynchronous RL systems often emphasize throughput, while leaving training stability and task effectiveness largely underexplore...

---

### 28. TimEE: End-to-end Time Series Classification via In-Context Learning

**Authors:** Jaris Küken, Shi Bin Hoo, Martin Mráz, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07500v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07500v1)

**Summary:** Time series classification (TSC) is dominated by a two-stage paradigm: train a feature encoder -- either from scratch on the target dataset or via pretraining on large corpora -- and then fit a task-specific classifier on top. While effective, this decoupling optimizes representation learning independently of the classification objective, requires per-dataset training, and prevents the model from exploiting label information during inference. We introduce TimEE, a 4.5M-parameter foundation model...

---

### 29. Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26

**Authors:** Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07498v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07498v1)

**Summary:** Testing is a major effort for the gaming industry, requiring a significant part of development budget and people power. We present a case study on a development version of the ice hockey game EA SPORTS NHL 26, for which human playtesters test the goalie AI for behavioral exploits. To reduce the effort of re-testing the goalie AI after every game or behavior modification in the development phase, we propose Reward-Adaptive Iterative Discovery (RAID), a novel approach to automatically find exploit...

---

### 30. GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining

**Authors:** Jieying Wang, Shuyuan Fan, Mingkai Zheng, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07494v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07494v1)

**Summary:** Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining. Communicating gradients in low-precision formats, such as FP8 and NVFP4, can significantly reduce the communication volume. Existing methods quantize gradients via linear or nonlinear mappings in Euclidean space, often degrading model performance because highly anisotropic gradients incur direction-dependent distortion. We present GIFT, a geometry-informed gradient scaling method that performs low-p...

---

### 31. FourierQK: Spectral Preprocessing of Query-Key Projections Improves Transformer Attention

**Authors:** Athanasios Zeris

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07478v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07478v1)

**Summary:** FFT-based spectral preprocessing of learned query-key (Q/K) projections substantially improves transformer attention on character-level language modelling. On TinyShakespeare: a fixed random spectral filter achieves val=1.031 (Delta=+0.443); a single learned frequency at paragraph scale achieves val=0.608 (Delta=+0.867); and four learned frequencies spanning paragraph to word scale achieve val=0.309 (Delta=+1.166), a 79% reduction over standard dot-product attention. The single-frequency result ...

---

### 32. Where to Intervene? Benchmarking Fairness-Aware Learning on Differentially Private Synthetic Tabular Data

**Authors:** Vinícius Gabriel Angelozzi, Héber H. Arcolezi

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07471v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07471v1)

**Summary:** Machine learning models are increasingly deployed in high-stakes domains, raising concerns about both privacy and fairness. Differential Privacy (DP) has become a gold standard for privacy-preserving data analysis, while fairness-aware mechanisms aim to mitigate discrimination against underrepresented groups. However, these objectives can conflict: DP often amplifies disparities across demographic groups, and little is known about whether established fairness interventions remain effective under...

---

### 33. Statistical inverse learning and $\ell^1$-regularization

**Authors:** Abhishake Rastogi, Tatiana A. Bubba, Tapio Helin, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07468v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07468v1)

**Summary:** We study the recovery of sparse functions from finite, noisy, and indirect observations in the framework of statistical inverse learning. The unknown is modeled as an element of $\ell^1$, and observations are generated through a possibly nonlinear forward operator $A:\ell^1\to H$, where $H$ is a vector-valued reproducing kernel Hilbert space. We propose an $\ell^1$-regularized empirical risk minimizer and develop a theoretical analysis of its statistical properties.   Under mild assumptions, we ...

---

### 34. RLVP: Penalize the Path, Reward the Outcome

**Authors:** Bojie Li, Noah Shi

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07435v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07435v1)

**Summary:** Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them fr...

---

### 35. Reliable mechanistic operator recovery with biologically-informed neural networks: principles for architecture and optimisation design

**Authors:** Rebecca M. Crossley, Yuan Yin, Sarah L. Waters, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07425v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07425v1)

**Summary:** Many biological processes are governed by complex dynamical mechanisms that remain incompletely understood despite increasing volumes of experimental data. Biologically-informed neural networks (BINNs) seek to address this challenge by embedding mechanistic differential equations into neural network training, enabling interpretable constitutive operators to be recovered directly from sparse and noisy observations. However, reliable operator recovery depends sensitively on network architecture, o...

---

### 36. The Optimal Sample Complexity of Learning Autoregressive Chain-of-Thought

**Authors:** Zhiyuan Li

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07423v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07423v1)

**Summary:** We prove that, in the realizable PAC setting, the sample complexity of exact-trace learning for full autoregressive Chain-of-Thought traces is upper bounded by the standard multiclass rate of the local next-token class, where this rate is governed by the Daniely--Shalev-Shwartz dimension. Under exact-trace loss, one wrong action makes the whole trace incorrect; nevertheless, for every stopping rule $\mathtt{halt}$ and every pointwise $\mathtt{halt}$-halting local class $\mathrm{H}$, $n_{\mathrm{...

---

### 37. Heterogeneity-Adaptive Diffusion Schrodinger Bridge for PET-Guided Whole-Body MRI Translation

**Authors:** Chengbo Wang, Jiacheng Yu, Linjie Bian, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07401v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07401v1)

**Summary:** While whole-body multimodal medical imaging scanners have been increasingly recognized for more effective medical applications, the excessive long acquisition time in PET-MR scanning is a major obstacle in more efficient clinical practice. Deep learning-based MRI translation provides a potential solution to reduce scan duration. However, current models often focus on specific anatomical regions and face challenges for whole-body scans that consists of highly heterogeneous feature distributions m...

---

### 38. When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated VLMs

**Authors:** Tanay Sodha, Aditya Sharma, Ramya Hebbalaguppe, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07395v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07395v1)

**Summary:** Reliable confidence estimation remains a key limitation of test-time adaptation in vision-language models (VLMs), where prompt tuning improves zero-shot accuracy but often degrades calibration due to entropy-driven overconfidence. Prior approaches mitigate this using LLM-derived class attributes and contrastive regularization, yet treat attributes independently, ignoring their relational structure. We propose ARGTCA, which represents (class, attribute) pairs as nodes in a Symbolic Attribute Grap...

---

### 39. TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models

**Authors:** Yutang Ma, Kecheng Huang, Xikun Jiang, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07388v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07388v1)

**Summary:** Large Language Models (LLMs) store factual knowledge and domain-specific patterns implicitly in dense Transformer parameters, making knowledge expansion costly through pretraining, fine-tuning, retrieval augmentation, or longer contexts. Engram-style memory offers a compact hidden-state injection pathway, but existing GPU-resident designs often rely on hash-based compression, causing unrelated phrases to collide in shared slots and weakening phrase-level semantic fidelity. We present TF-Engram, ...

---

### 40. Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity

**Authors:** Loïc Cabannes, Pierre-Emmanuel Mazaré, Gergely Szilvasy, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07386v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07386v1)

**Summary:** Linear attention models allow a fixed state size and a fixed amount of compute per token. However, due to their limited state size, linear attention models fall behind in long-context recall compared to softmax-attention-based transformer architectures. Increasing the state size of linear attention improves recall performance but at the cost of higher FLOPs. In this work, we introduce Sparse Delta Memory (SDM), an architecture that scales the hidden state of gated linear RNNs to orders of magnit...

---

### 41. Generalist Vision-Language Models for Fast Radio Burst detection: a zero-shot benchmark against a specialized detector

**Authors:** Raiff H. Santos, Amilcar R. Queiroz, Tharcisyo S. S. Duarte, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07382v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07382v1)

**Summary:** Fast Radio Bursts (FRBs) are millisecond-duration radio transients whose automated detection increasingly relies on highly specialized deep learning models. These detectors achieve exceptional performance, but they require large task-specific training datasets and cannot be redefined without retraining. In this work, we evaluate whether small, open-weight, locally run generalist Vision-Language Models (VLMs) can detect FRBs in dynamic spectra under a zero-shot, prompt-only regime, with no fine-t...

---

### 42. Physics-Audited Agentic Discovery in Scientific Machine Learning

**Authors:** Diab W. Abueidda, Bilal Ahmed, Panos Pantidis, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07379v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07379v1)

**Summary:** In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not establish that the predicted fields satisfy the physics that matter for mechanics, such as boundary conditions, superposition, stiffness scaling, or causality. We introduce Physics-Audited Agentic SciML (PA-SciML), a verification-first workflow for agentic SciML discovery. The workflow fixes...

---

### 43. On Adversarial Vulnerability of Vision-Language Models through the Lens of Intermediate Spectral Subspaces

**Authors:** Chethan Krishnamurthy Ramanaik, Tobias Callies, Michael Hecht, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07375v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07375v1)

**Summary:** Adversarial vulnerability in deep neural networks (DNNs) has been studied from the perspectives of decision-boundary geometry, feature robustness, input-output Jacobians, and the instability of inverse problems. Here, we focus on the spectral structure of intermediate linear transformations that propagate information through modern DNNs, an unexplored mechanism of adversarial vulnerability. Specifically, we investigate transformer-based vision-language models, whose linear layers admit interpret...

---

### 44. Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report

**Authors:** Xufeng Zhao, Fuzhi Yang, Jianhui Chen, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07370v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07370v1)

**Summary:** In embodied intelligence systems, the motion controller serves as the critical bridge between semantic reasoning and physical execution. Humanoid control has progressed rapidly through large-scale human motion-capture data and motion-tracking paradigm. However, producing quadruped robots motion corpora with scalability and physical feasibility faces more fundamental obstacles: animal motion data is scarce, and cross-embodiment retargeting remains fragile. We present ABot-C0, a generalist motion-...

---

### 45. Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors

**Authors:** Oliver Makins, Orazio Angelini, Zohreh Shams, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07368v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07368v1)

**Summary:** AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a ...

---

### 46. Latency-Aware Bid Acceptance under Operational Feasibility: A Public Benchmark with Hindsight Ceilings

**Authors:** Aswin Chandrasekaran

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07343v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07343v1)

**Summary:** Online truckload bid acceptance is a closed-loop stochastic decision problem in which a carrier or broker must, in real time, accept or reject a tendered load subject to operational feasibility, fleet repositioning costs, and opportunity cost against future demand. Public, reproducible benchmarks for this problem are scarce: existing routing benchmarks are static, while dynamic-fleet studies typically rely on private operator data. We introduce FreightBidBench, a public-calibrated, dependency-fr...

---

### 47. Hypergraph Neural Stochastic Diffusion: An SDE Framework for Uncertainty Estimation

**Authors:** Zhiheng Zhou, Mengyao Zhou, Dengyi Zhao, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07330v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07330v1)

**Summary:** Hypergraph neural networks have shown powerful capability in modeling higher-order relations, yet their predictive uncertainty remains underexplored. Unlike pairwise graphs, uncertainty in hypergraphs arises not only from noisy attributes and ambiguous labels, but also from variations in node-hyperedge incidence structures and complex higher-order dependencies. Existing approaches mainly estimate uncertainty from final predictions or rely on computationally expensive ensembles and Bayesian infer...

---

### 48. R^3: Advertisement Compliance Rectification via Group-Relative Experience Extractor and Curriculum Reinforcement

**Authors:** Yuan Chen, Zhenyu Hu, Mengge Xue, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07318v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07318v1)

**Summary:** Rigorous content moderation is crucial for online advertising but leads to millions of daily rejections. This scale renders manual rectification infeasible, particularly for video advertisements. However, existing safety-driven methods often suffer from aggressive over-editing, which compromises the advertiser's original semantic intent merely to satisfy compliance. In this work, we target the rectification of textual violations in video ads, covering both speech transcripts and on-screen text. ...

---

### 49. Mechanistic Interpretability for Neural Networks: Circuits, Sparse Features and Symbolic Reasoning

**Authors:** Pranav Sawant, Jakub Krejčí

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07316v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07316v1)

**Summary:** This article offers a comprehensive overview of mechanistic interpretability, an emerging field that seeks to reverse-engineer the internal algorithms of modern neural networks. While traditional explainable AI methods often stop at surface-level input-output correlations, this approach directly addresses the opaque "black box" nature of machine learning models, which is essential for ensuring safety and auditability in high-stakes deployments. The paper provides a detailed examination of Transf...

---

### 50. FedCVESA: Taking Away Training Data in Federated Learning via Correlation Value Encoding and Segmented Aggregation

**Authors:** Chongkai Li, Bang Zhang, Wenjian Luo

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07314v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07314v1)

**Summary:** Federated learning (FL) avoids explicit data exposure by keeping raw data on local clients, yet privacy risks remain in the training process and the learned model itself. Recently, centralized Taking Away Training Data (TATD) attacks have shown that malicious training could abuse the memorization capacity of deep models to store and later recover training data. However, this memorization-based threat has not been systematically studied under FL environments, where multi-client averaging could ov...

---

## cs.NE

**50 papers**

### 1. Social-spatial dependencies for learning visual navigation

**Authors:** Patrick Govoni, Pawel Romanczuk

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07460v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07460v1)

**Summary:** Navigation for social organisms rarely is a fully independent activity. Group structure and dynamics, as well as embodied interactions, critically influence useful behavior. Individual neural network controlled agents are trained to navigate in different social contexts, where social dependence and behavioral strategy learned is determined by relative task performance and spatial effect. Increasing high quality social information drives phase transitions from individual to following navigational...

---

### 2. Single-Entity Spiking Neuron Models: Survey

**Authors:** Leon Parepko, Danila Shulepin, Albert Nasybullin

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07429v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07429v1)

**Summary:** In this work, we reviewed different approaches in mathematical modeling of biologically plausible neural systems. Models are characterized and classified based on their common features and special use cases. In addition to spiking models, different types of discrete and continuous analogs are considered to accurately simulate biological processes, including membrane potential dynamics. The models under investigation include neurons and various components encountered in neural systems and affecte...

---

### 3. Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware

**Authors:** Oskar von Seeler, Christian Tetzlaff, Andrew Lehr

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07373v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07373v1)

**Summary:** In biological circuits, sequential neural activity evolves along dynamic, low-dimensional manifolds to enable flexible behavior. Spiking network models link aspects of this sequential activity to features of manifold geometry through specific circuit mechanisms, making dynamic neural manifolds parameterizable, and thereby offering an explainable framework for neural computation. Extending this framework to neuromorphic engineering, we present an implementation on the SpiNNaker 2 chip for real-ti...

---

### 4. Intrinsic-Noise Consolidation: A Doob-Barrier-Conditioned Diffusion Turns Analog Device Noise into a Continual-Learning Resource

**Authors:** Gunner Levi Howe

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06924v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06924v1)

**Summary:** On analog neuromorphic hardware, intrinsic device noise is normally an accuracy tax. We ask whether it can instead consolidate memories. We cast per-synapse consolidation as a Doob h-transform: condition each weight's stochastic dynamics on never crossing a memory-critical barrier around its consolidated value. The conditioned diffusion gains an extra drift sigma^2 d/dw log h, a restoring force amplified by the noise variance itself that diverges at the barrier. We are explicit about novelty: th...

---

### 5. An Introduction and Tutorial of the Beagle Framework

**Authors:** Ilya Basin, Nathan Haut, Wolfgang Banzhaf

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06731v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06731v1)

**Summary:** The Beagle framework is a GPU-based genetic programming framework that enables highly efficient genetic programming search using large population sizes by leveraging NVIDIA GPUs. This technical guide provides an introduction to the Beagle framework and provides detailed instructions for using the framework for symbolic regression problems.

---

### 6. A Hardware-Aware Open-Source Framework for Design Space Exploration of Mixed-Signal Spiking Neural Networks

**Authors:** Sayma Nowshin Chowdhury, Vineeta Nair, Taseen Forhad, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06456v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06456v1)

**Summary:** Energy-efficient neuromorphic computing at the edge requires simulation tools that can capture the non-ideal behavior of mixed-signal spiking neural network (SNN) hardware while supporting system-level design exploration. This work presents an open-source hardware-aware simulation framework for mixed-signal SNNs that enables comparative analysis across neuron, synapse and architecture choices. The framework supports multiple neuron models, including Leaky Integrate-and-Fire (LIF), Hodgkin-Huxley...

---

### 7. Scalable Perturbation Learning for Online Self-Supervised Echo State Networks

**Authors:** Taiki Yamada, Kantaro Fujiwara

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06079v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06079v1)

**Summary:** Intelligent systems should not only solve tasks but also adapt under real-world constraints. Autonomous adaptation via self-supervised learning, sequential adaptation via online learning, and memory-efficient implementation via perturbation-based learning are important requirements for such systems. However, these requirements are generally in tension for high-dimensional systems, because perturbation-based learning suffers from variance that grows with the dimension of the perturbed variables. ...

---

### 8. An event-driven framework for fly-inspired visual motion detection

**Authors:** Qinbing Fu, Jingyu Huang, Yan Xie, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05205v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05205v1)

**Summary:** Fast and reliable motion detection is essential for machine vision and autonomous systems operating in dynamic environments. This work integrates emerging event-based sensing with biologically structured neural computation to establish an efficient computational paradigm for visual motion detection. The proposed framework is built upon a recently developed fly-inspired neural network that emulates motion-processing circuits in the optic lobe. Owing to its feed-forward and training-free architect...

---

### 9. LLM for the development of FCM

**Authors:** Alexis Kafantaris

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04983v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04983v1)

**Summary:** This article is about the development of a fuzzy cognitive map using a local large language model. In the light of recent advances it is evident that large language models, and even local large language models are capable of extracting quantities from textual data. In other words, a local LLM like Qwen2.5-32B, or probably larger, can accept entities as prompt input and determine relevant quantitative data as the model output. In turn, this output can be utilized for the construction of a data dr...

---

### 10. A Large-Scale Sparse Multiobjective Optimization Algorithm Based on Optimal Performance Scores

**Authors:** Jia-Lin Mai, Min-Rong Chen, Guo-Qiang Zeng, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04765v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04765v1)

**Summary:** Large-scale sparse multiobjective optimization problems (LSSMOPs) involve a large number of decision variables and Pareto optimal solutions with only a few nonzero variables. However, as the number of decision variables grows, it becomes increasingly challenging to accurately identify the nonzero variables, and optimization performance is adversely affected. To address these issues, this paper proposes an evolutionary algorithm for LSSMOPs. Specifically, we propose a new initialization method ca...

---

### 11. Heaviside Continuity of Rolling Coefficients for Eliminating Epistemic Entropy in Large Language Models

**Authors:** MY Pitsane, Hope Mogale

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04562v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04562v1)

**Summary:** Large language models (LLMs) generate fluent outputs that can be wrong. Unlike humans, who often exhibit cues when providing false information, LLMs produce errors that are difficult to detect because autoregressive decoding provides no mechanism for verifying intermediate reasoning before state progression. We introduce Heaviside Continuity of Rolling Coefficients (HCRC), a verification-first execution framework that reformulates inference as predicate-gated state transitions governed by a Heav...

---

### 12. Neuromorphic Silicon Neuron Controller for Adaptive Deep Brain Stimulation in Parkinson's Disease

**Authors:** Md Abu Bakr Siddique, Jakub Orłowski, Yan Zhang, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.05453v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05453v1)

**Summary:** Parkinson's disease (PD) affects millions worldwide and causes severe motor symptoms. Adaptive deep brain stimulation (aDBS) delivers physiologically informed stimulation that can track fluctuations in PD motor symptoms, enabling more intelligent DBS control. However, most existing aDBS approaches are primarily algorithm- and software-driven, with limited efforts toward circuit realization, particularly low-power and implantable integrated circuits. This paper presents the Silicon Leaky Integrat...

---

### 13. Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures

**Authors:** Joy Bose

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02967v2) | 📄 [PDF](https://arxiv.org/pdf/2607.02967v2)

**Summary:** Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory. CALM (Nechesov and Ruponen, 2025) identifies its threshold-binary encoder as an open design question. This paper evaluates rank-order N-of-M encoding (Furber et al., 2007) as an alternative. We make three contributions. First, a faithful reimplementation validates the published architecture by confirming exact equivalence betwee...

---

### 14. Microcosmos: Reimagining Artificial Life for the GPU Era

**Authors:** Mark Tensen, Ciaran Regan, Bert Wang-Chak Chan, et al.

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02954v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02954v1)

**Summary:** Most artificial life simulators either operate on abstract substrates disconnected from physical reality, or simulate physically grounded worlds that do not scale to the population sizes required for open-ended evolution. We present Microcosmos, a simulation engine in which artificial lifeforms are modeled as elastic filament chains inhabiting a two-dimensional viscous fluid world, designed from the ground up for modern GPU hardware and end-to-end differentiable simulation. We validate the engin...

---

### 15. A Spiking Sequence Generator for Polar Trajectories on Neuromorphic Hardware

**Authors:** William R. P. Nourse, Roger D. Quinn

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02753v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02753v1)

**Summary:** Neuromorphic controllers for size, weight, and power-constrained systems require neural architectures that are both energy-efficient and interpretable at the level of system dynamics. However, existing approaches either rely on end-to-end trained spiking networks with limited interpretability, or on converted classical controllers that fail to fully exploit neuromorphic dynamics. We present a spiking neural network (SNN) architecture for generating polar trajectories, using a winner-take-all (WT...

---

### 16. Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

**Authors:** Kuo-Chung Peng, Jiun-Cheng Jiang, Chun-Hua Lin, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02363v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02363v1)

**Summary:** Quantum Fast-Weight Programmers (QFWPs) store temporal information in dynamically programmed variational-circuit parameters rather than in nonlinear recurrent hidden states, offering a practical route to quantum sequence modeling. Self-Modulating QFWP improves this framework by using input-dependent gates for both new fast-weight updates and the accumulated fast-weight state, but its unbounded old-state multiplier can diverge in long-sequence regimes. We propose a bounded old-state modulation ru...

---

### 17. Hybridizing a Grouping Metaheuristic with Reinforcement Learning for the One-Dimensional Bin Packing Problem

**Authors:** Zitouni Rania, Mostefai Mounir Sofiane, Tati Youcef, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02315v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02315v1)

**Summary:** The one-dimensional bin packing problem (1D-BPP) is a canonical NP-hard combinatorial optimization problem with broad industrial applications. We propose RL-HGGA, a hybrid algorithm that integrates Falkenauer's Hybrid Grouping Genetic Algorithm (HGGA) with a tabular Q-learning controller. Rather than applying genetic operators at fixed probabilities, a Q-learning agent dynamically selects among eight macro-actions -- including BPCX crossover, light and heavy mutation, Martello-Toth local search,...

---

### 18. Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

**Authors:** Juwei Shen, Yujie Wu, Changwen Chen

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02283v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02283v1)

**Summary:** In-context learning (ICL) operates via implicit gradient descent embedded in the forward pass of modern AI architectures -- Transformers, Mamba, state-space models, and MLPs. Capturing this capability in biologically plausible Spiking Neural Networks (SNNs) has remained an open challenge: existing SNNs fail the Garg-2022 benchmark at non-trivial task dimensions. We trace this failure to a structural assumption: prior SNN designs route adaptation through inference-time synaptic plasticity, viewin...

---

### 19. Predicting Early Stages Of Alzheimer's Disease And Identifying Key Biomarkers Using Deep Artificial Neural Network And Ensemble Of Machine Learning Methodologies

**Authors:** Debopriya Ghosh

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02142v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02142v1)

**Summary:** Alzheimers disease (AD) is a brain disorder that develops slowly and mainly affects memory, thinking, language, and daily activities. It is one of the most common causes of dementia and creates many difficulties for patients as well as their families. In the early stage, the symptoms are often mild and may look like normal ageing. For this reason, many people are diagnosed late, when the disease has already progressed. At present, there is no complete cure for AD. Still, early detection can help...

---

### 20. Electronic Bursting Neuron: design, equations and hardware implementation

**Authors:** Lev V. Takaishvili, Vladimir I. Ponomarenko, Maksim V. Kornilov, et al.

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02122v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02122v1)

**Summary:** Electronic neurons are a keystone for construction of the spiking neural networks which have numerous applications in neuroprosthetics, artificial memory, intensive calculations etc. A number of concepts of electronic neurons has been already proposedm with some of them implemented in hardware. However, new schemes are of significant interest since the existing ones do not fit all requirements: either they are too complex and expensive in realization, or they are not able to demonstrate all dema...

---

### 21. Evolutionary Wave Function Collapse

**Authors:** Dipika Rajesh, Ahmed Khalifa, Julian Togelius

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.02082v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02082v1)

**Summary:** Wave Function Collapse (WFC) is a widely used procedural content generation method that learns local adjacency constraints from example inputs to generate larger outputs. In this paper, we explore combining WFC with evolutionary search by evolving the small input examples used by WFC rather than directly evolving complete levels. In this approach, WFC acts as a genotype-to-phenotype mapping. The generated levels are then evaluated through domain-specific fitness functions. We evaluate the method...

---

### 22. Mechanism and Stability Analysis of Metabolic Closed-Loop Metaheuristics

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-02

🔗 [Paper](http://arxiv.org/abs/2607.01551v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01551v2)

**Summary:** This paper studies the Metabolic Multi-Agent Optimizer (MMAO) at the framework level rather than at the implementation or benchmark level. The central question is whether the metabolic resource loop of private energy, communal budget, role drift, and lifecycle turnover has a framework-level interpretation beyond narrative metaphor. We introduce a generic MMAO state model that abstracts away domain-specific move operators while retaining the resource bookkeeping that defines the framework. Under ...

---

### 23. MMAO-Cls: Metabolic Multi-Agent Optimization for Joint Feature Selection and Classifier Tuning

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01539v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01539v2)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can act as a credible outer-loop optimizer for classification model selection. We propose MMAO-Cls, a mixed-space realization in which each agent jointly encodes a binary feature mask and classifier hyperparameters, while private energy, communal budget, role drift, and lifecycle turnover are mapped to the accuracy-complexity tradeoff of wrapper learning. The implementation is strengthened by deriving feature-budget adaptation...

---

### 24. BFF: Simple explanations for complex phenomena

**Authors:** Charlotte Knierim, Luca Versari, Robert Obryk, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01483v1) | 📄 [PDF](https://arxiv.org/pdf/2607.01483v1)

**Summary:** The ''Computational Life'' paper (Agüera y Arcas et al., 2024) argues that paired interactions in a computational soup are an effective way to find self-replicators. In this work, aided by recent developments in self-replicator detection, we explore the alternate hypothesis that self-replicators can be found at least as easily using simple mutation random walks in program space. We also explore the claim that capping the maximum ''depth'' and ''width'' of the ancestry tree stops self-replicators...

---

### 25. Towards transferable lightweight neuromorphic computing through a model-free temporal-switch framework

**Authors:** Zefeng Zhang, Chao Li, Siyao Chen, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.02608v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02608v1)

**Summary:** Lightweight neuromorphic computing offers a promising route to efficient AI, with particular benefits for resource-constrained edge deployments. However, its scalable deployment that can reliably transfer the expected performance has long been hindered by device-to-device variations, which necessitate costly and repeated re-training on new copies and undermine the practical advantages. To address this issue, we introduce a model-free temporal-switch (TS) framework to improve the direct transfer ...

---

### 26. MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00846v2) | 📄 [PDF](https://arxiv.org/pdf/2607.00846v2)

**Summary:** This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can be credibly derived into a dynamic-optimization method without replacing its core metabolic control loop by external adaptation modules. The proposed MMAO-Dyn maps private energy, communal budget, role drift, success feedback, and lifecycle turnover to a nonstationary setting in which environmental changes repeatedly invalidate previously useful local structure. We evaluate MMAO-Dyn on an 18-scenario synthetic dynamic cont...

---

### 27. From Consistency to Collaborative Discovery: MFEA-CoD for Multitask Novelty Search

**Authors:** Jiao Liu, Yanchi Li, Hua Yu, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00761v2) | 📄 [PDF](https://arxiv.org/pdf/2607.00761v2)

**Summary:** Evolutionary multitasking (EMT) has shown strong capability in solving multiple optimization problems simultaneously by exploiting latent inter-task consistency, such as similarities in promising solutions or search directions. However, most existing EMT studies remain focused on objective-driven optimization, where such consistency is mainly used to accelerate convergence toward predefined optima. In this paper, we move EMT from consistency to collaborative discovery and propose a multifactoria...

---

### 28. Self-Organized Learning in Oscillatory Neural Networks with Memristive Signed Couplings

**Authors:** Riley Acker, Aman Desai, Garrett Kenyon, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00286v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00286v1)

**Summary:** Oscillatory neural networks (ONNs) have emerged as a promising neuromorphic architecture, leveraging coupled dynamical systems to perform computation and represent information through phase relationships. Their interactions can be designed to support intrinsic energy-minimizing dynamics, enabling tasks such as associative memory and optimization, and positioning them as a candidate architecture for continuous learning and inference. We present a neuromorphic primitive implemented using memristiv...

---

### 29. EVOTS: Evolutionary Transformer Search for Time Series Forecasting

**Authors:** AbdElRahman ElSaid, Damir Pulatov

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2607.00154v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00154v1)

**Summary:** Evolutionary neural architecture design for multivariate time-series forecasting remains underexplored, with most approaches relying on fixed Transformer architectures despite substantial variation across tasks and forecasting settings. This paper introduces an evolutionary neural architecture search framework for discovering task-adaptive Transformer-like models for time-series forecasting (EVOTS). Architectures are encoded using a modular genome representation that enables flexible composition...

---

### 30. Evaluation of Population Initialization Methods for Genetic Programming-based Symbolic Regression

**Authors:** Lukas Kammerer, Gabriel Kronberger, Deaglan J. Bartlett, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31990v1)

**Summary:** We analyze the effect of optimizing the initial population of genetic programming (GP) for symbolic regression (SR) on the accuracy and complexity of solutions. We compare three well-established random initialization methods as well as initialization with small optimized solutions from exhaustive symbolic regression (ESR) using a GP/SR implementation which is based on the multi-objective evolutionary algorithm NSGA-II. We compare the final Pareto fronts found with each initialization method on t...

---

### 31. Distributed Hierarchical Temporal Memory with Shared Associative Memory for Cross-Entity Preemptive Warning

**Authors:** Pavia Bera, Jennifer Adorno, Sanjukta Bhanja

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31789v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31789v1)

**Summary:** Anomaly detection in multivariate time series remains a critical challenge in large-scale distributed systems, where related entities may exhibit transferable precursor behavior prior to anomaly onset. Existing methods typically operate independently on each data stream and therefore remain fundamentally reactive. To address this limitation, we introduce Distributed Hierarchical Temporal Memory (D-HTM), a neuromorphic framework that enables cross-entity preemptive warning through a Shared Associ...

---

### 32. Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

**Authors:** Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn, et al.

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31700v1)

**Summary:** Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically plausible learning rules avoid backpropagation's weight transport requirement, but it has been difficult to achieve strong performance under Dale's principle beyond MNIST. Error Diffusion (E...

---

### 33. A Large-Scale Empirical Evaluation of MMAO Under Fair-Budget Continuous and Discrete Benchmarks

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31584v2) | 📄 [PDF](https://arxiv.org/pdf/2606.31584v2)

**Summary:** This paper evaluates the Metabolic Multi-Agent Optimizer (MMAO) under a stricter empirical protocol rather than reintroducing the framework itself. The study asks whether MMAO's closed-loop resource-allocation principle remains credible under broader, more standard, and more explicitly budget-controlled continuous and discrete benchmarks. The main completed matrix covers eight CEC2017 functions at 10D and 30D with 20 seeds each, and five TSPLIB instances with 20 seeds each, together with stronge...

---

### 34. Robustness of neural networks to random noise perturbations of their inputs

**Authors:** Mark Levene, Martyn Harris

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31581v1)

**Summary:** We investigate the problem of the robustness of a trained neural network to the perturbation of its input values. More specifically, we examine the interplay between the accuracy of the network, as measured by the mean squared error, and robustness. Accordingly, we present a robustness measure, which, with high probability, suggests an upper bound on the mean squared error of the network, with respect to an input data set, for a given perturbation of the input values of the network. The measure ...

---

### 35. Partition-Guided Distance Saliency: Bridging Decision and Objective Spaces in Many-Objective Optimization

**Authors:** Cláudio Lúcio do Val Lopes, Flávio Vinícius Cruzeiro Martins, Elizabeth Fialho Wanner

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30836v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30836v1)

**Summary:** Explainability in Many-Objective Optimization (MaO) is currently hindered by the escalating complexity of the Pareto front, which renders the relationship between high-dimensional decision variables and objective outcomes increasingly opaque. As the number of objectives exceeds the limits of traditional visualization, decision-makers encounter a ``cognitive drought'' in identifying relevant trade-offs or specifying target regions without a priori knowledge. To bridge this interpretability gap, w...

---

### 36. Why can genetic algorithms work in high-dimensional search spaces?

**Authors:** Stephen Whitelam

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30619v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30619v1)

**Summary:** We show that the effective dynamics of the elitist $(1+M)$ genetic algorithm is, in the limit of small mutations, clipped gradient descent on the loss in the presence of anisotropic Gaussian white noise. In expectation, therefore, a simple mutation-selection genetic algorithm follows the gradient of the loss, without explicit calculation of gradients and without averaging over loss evaluations. The genetic algorithm is slower than gradient descent because of the noise that acts in directions tra...

---

### 37. Computing the Integral R2 Indicator by Perspective Mapping and Box Decomposition

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30530v5) | 📄 [PDF](https://arxiv.org/pdf/2606.30530v5)

**Summary:** The continuous integral R2 indicator is a Pareto-compliant refinement of the classical finite-weight-vector R2 indicator, used in performance assessment, bounded archiving for a-posteriori multi-objective optimization, and skyline selection in databases. This work introduces a bidirectional perspective mapping between continuous integral R2 computation and integration over unions of anchored axis-aligned boxes. After translating the ideal point of a minimization problem to the origin, approximat...

---

### 38. Minimal MMAO: A Resource-Closed-Loop Framework for Adaptive Metaheuristic Search

**Authors:** Jinliang Xu, Liping Ma

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30450v2) | 📄 [PDF](https://arxiv.org/pdf/2606.30450v2)

**Summary:** This paper presents the Metabolic Multi-Agent Optimizer (MMAO) as an adaptive metaheuristic built around endogenous resource circulation. The central premise is that search intensity, exploration--exploitation balance, and lifecycle turnover should be induced by a shared metabolic controller rather than by separately attached schedules. We formulate MMAO through bounded private energy, a communal budget, normalized reward, continuous role adaptation, and resource-financed branching and pruning. ...

---

### 39. From Detecting Agency to Doing Work: Self-Caused Credit Builds a Durable Behavioral Self in a Minimal Spiking Agent

**Authors:** Haoliang Han

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30191v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30191v1)

**Summary:** How does an agent that can tell self from world come to be durably shaped by that distinction? Recent work shows that a predictive system can detect its own agency (Ye, 2026), but detecting agency does not explain durable, self-shaped behavior. We show that agency-gated slow credit -- a conjunctive term Own*Agency*Salience driving a slow parameter update -- produces post-unload behavioral residue: on a spiking substrate (Nengo LIF/PES), a learned self-preserving choice survives episodic buffer r...

---

### 40. Semantics-Aware Bilevel Co-Evolution: Towards Automated Multicomponent Algorithm Design

**Authors:** Zhiyao Zhang, Shenghao Wu, Xingyu Wu, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29953v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29953v1)

**Summary:** LLM-assisted evolutionary search (LES) has emerged as a promising paradigm for automated algorithm design. However, existing methods usually suffer from two inherent limitations when facing the automated design of real-world complex algorithms that usually consist of multiple components. The first limitation is that they either focus on modifying entire algorithms, making it difficult to reuse high-quality components, or concentrate on component refinement within a limited set of predefined mult...

---

### 41. Evolutionary Hyperparameter Optimization to Find Lightweight CNN Models for Autonomous Steering

**Authors:** Devson Butani, Ryan Kaddis, Chan-Jin Chung

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29684v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29684v1)

**Summary:** This research investigates the optimization of Convolutional and Dense Neural Networks (CNNs and DNNs) for autonomous steering using the (N+M) Evolution Strategy (ES) with the 1/5th success rule. The primary objective is to develop a lightweight CNN based model capable of real-time steering angle prediction, mimicking human driving behavior on predefined paths. The ES algorithm automates hyperparameter tuning, dynamically adjusting parameters such as filter sizes and layer configurations. Data c...

---

### 42. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 43. Supervised Hebbian learning in Deep Counterstream Associative Networks

**Authors:** Andreas Knoblauch

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29528v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29528v1)

**Summary:** Modern machine learning applications employ deep neural networks training with the error backpropagation algorithm. Although this algorithm is very effective, it lacks biological realism. For example, backpropagation requires symmetric connectivity, and a separate neural processing channel for error signals. Prior works have therefore proposed a number of more realistic alternatives for error backpropagation. However, most of them still suffer from demanding preassumptions that may be not fulfil...

---

### 44. When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning

**Authors:** Zhengqi Pei, Qingming Huang, Shuhui Wang

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29354v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29354v1)

**Summary:** Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. We propose Communicative Language Symbolism Routing (CLSR), a test-time framework in which multiple LLM agents autonomously invent, evolve, and share compact Language Symbolism Frameworks (LSFs), while a latent-free router adaptively selects and composes these languages per query to optimize the a...

---

### 45. Travel-Oriented Reasoning Large Language Model via Domain-Specific Knowledge Graphs

**Authors:** Vignesh Ram Nithin Kappagantula, Shayan Hassantabar, Samuel Simpson, et al.

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29254v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29254v1)

**Summary:** Large language models (LLMs) demonstrate broad reasoning abilities but struggle with accuracy and reliability in specialized domains such as travel, where reasoning depends on precise definitions, rules, and expert-defined conceptual frameworks, and where confident but unfounded outputs arise from a reasoning failure in which the model has not internalized the underlying domain graph rather than from missing domain knowledge alone. We propose a modular pipeline for building a travel-domain reaso...

---

### 46. Unified Complex-valued Neural Network: A Magnitude-Phase Computational Model for Event-Driven Neuromorphic Learning

**Authors:** Reza Ahmadvand, Sarah Safura Sharif, Yaser Mike Banad

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29099v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29099v1)

**Summary:** Artificial neural networks (ANN) provide accurate continuous-valued representation, whereas spiking neural networks (SNN) offer event-driven temporal processing, yet both paradigms face limitations when value encoding and timing dynamics must be learned within a single computational structure. This paper introduces a network based on Unified Complex-valued Neuron (UCN), a new neural computational model that integrates continuous activation and phase-driven event generation through an asymmetric ...

---

### 47. Road to scalability for efficient graph search on massively parallel neuromorphic hardware

**Authors:** Oskar von Seeler, Elena C. Offenberg, Carlo Michaelis, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28907v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28907v1)

**Summary:** Efficient computation of shortest paths in weighted graphs is a fundamental problem with many applications. Neuromorphic hardware platforms promise massively parallel, efficient computation, changing parallelism tradeoffs. In this work, we introduce NEURO-MAPP (Neuromorphic-based Min-Add Parallel Propagation), a distributed shortest path algorithm designed to use the local computation and network communication available in neuromorphic systems. We provide an optimized implementation of the algor...

---

### 48. Closed-Form Steepest Descent Direction toward Flat Minima: Reducing Upper Bounds on the Loss Hessian Eigenspectrum in Neural Networks

**Authors:** Yuto Omae, Kazuki Sakai, Yohei Kakimoto, et al.

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.28662v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28662v1)

**Summary:** The flatness hypothesis suggests that flatness of the loss landscape, as measured by the eigenvalues of the loss Hessian, correlates with better neural network generalization. While various algorithms reduce these eigenvalues, most focus on procedural design, leaving it unclear how data distributions and NN parameters structurally determine directions toward flat minima. Characterizing these directions analytically is generally intractable. To overcome this mathematical difficulty, recent studie...

---

### 49. Analysis of Parameter Settings for the Bat Algorithm Using Variance Evolution

**Authors:** Xin-She Yang, Mehmet Karamanoglu

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28644v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28644v1)

**Summary:** Parameter settings in evolutionary algorithms and metaheuristics are important because such parameter values can influence the performance of algorithms under evaluation. For a given algorithm, there are many different numerical experiments to show that the algorithm can work well in practice; however, in most cases there is no theoretical analysis of parameter settings. In this work, we show that theoretical analysis using the theory of dynamical systems and evolution of population variance can...

---

### 50. Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation

**Authors:** Binh Nguyen, Colleen Josephson, Mircea Teodorescu, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28600v1)

**Summary:** Neuromorphic and edge computing research has focused on reducing the inference cost of neural network controllers, yet in physical closed-loop systems the actuator can rival or exceed an efficient controller in energy. An efficient controller is therefore necessary but not sufficient, because the actuator becomes the cost worth reducing once inference no longer dominates it. Here, we introduce energy-aware learning, an approach that incorporates actuator energy directly into the reinforcement le...

---

## q-bio.NC

**50 papers**

### 1. Single-Entity Spiking Neuron Models: Survey

**Authors:** Leon Parepko, Danila Shulepin, Albert Nasybullin

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07429v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07429v1)

**Summary:** In this work, we reviewed different approaches in mathematical modeling of biologically plausible neural systems. Models are characterized and classified based on their common features and special use cases. In addition to spiking models, different types of discrete and continuous analogs are considered to accurately simulate biological processes, including membrane potential dynamics. The models under investigation include neurons and various components encountered in neural systems and affecte...

---

### 2. Quantifying Entrainment Evidence: A Comparison of Frequentist and Bayesian Approaches for Information Processing Pathway Maps

**Authors:** Kaibo Zhang, Ji Wu, Chao Zhang, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06284v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06284v1)

**Summary:** Information Processing Pathway Maps (IPPMs) offer a scalable framework for formalizing the complex sequence of mathematical transformations applied to sensory stimuli. These maps chart the latency and cortical expression of computational steps, relying on statistical inference to link model outputs with observed neural activity. Traditionally, this mapping has relied on frequentist hypothesis testing. However, determining which of several competing computational models best explains neural data ...

---

### 3. STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning

**Authors:** Roy Segal, Yoni Svechinsky, Tomer Fekete

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06629v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06629v1)

**Summary:** Brain age -- the age inferred from a physiological recording -- is an emerging biomarker whose deviation from chronological age tracks neurological and psychiatric burden, and EEG is an attractive substrate for it because it is cheap, portable, and temporally rich. Yet EEG brain-age models must contend with cross-site montage heterogeneity, small labelled cohorts, and dominant subject-level non-stationarity, and few EEG foundation models have been shown to deliver competitive age regression acro...

---

### 4. Reward Valuation in Vision Language Models: Causal Mechanisms Underlying Anhedonia

**Authors:** Melika Honarmand, Samin Mahdipour Aghabagher, Martin Schrimpf

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06626v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06626v1)

**Summary:** Recent Vision-Language Models capture increasingly complex aspects of human cognition. Here we ask whether this alignment extends to reward valuation, which we assess in a mechanistic framework built on clinical tests that were developed to evaluate anhedonia and motivational deficits in major depressive disorder. In the brain, anhedonia is frequently linked to dysregulation in the Nucleus Accumbens (NAc) and the broader dopaminergic reward system. While neuroimaging has localized these deficits...

---

### 5. Using hierarchical statistical learning models to model individual statistical learning

**Authors:** Hanna Ringer, Tatsuya Daikoku

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.05822v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05822v1)

**Summary:** Statistical learning is essential for individuals to discover structure in the sensory environment, especially during communication via speech or music. Individual differences in statistical learning abilities have been proposed to account for differences in various cognitive functions and development, including developmental disorders such as dyslexia. In this study, we used a Hierarchical Bayesian Statistical Learning (HBSL) model to model individual learning trajectories as recorded using ele...

---

### 6. On the Increased and Decreased Connectivity of the Demented Human Brain

**Authors:** Daniel Hegedus, Marton Barnabas Mora, Balint Varga, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05654v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05654v1)

**Summary:** With the enormous advances in cerebral imaging techniques, a large amount of data is available for studying the aging and demented brain. In this contribution, we apply the OASIS-3 dataset for identifying small areas of the human gray matter, which have higher- or lower structural connectivity in dementia and aging. As anticipated, we found that finer structures of the hippocampus and the temporal lobe show decreased connectivity in dementia. More surprisingly, the precuneus, the cuneus, and fin...

---

### 7. Governable Individuals: An Identity Layer for Embodied Agents That Keep Learning

**Authors:** Xue Qin, Simin Luan, Cong Yang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05463v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05463v1)

**Summary:** Embodied artificial intelligence is moving from deployable models to persistent agents that learn in the field, acquire skills and migrate across bodies. Governing such a system means governing an individual, not a model, and existing proposals (agent identifiers, activity logs, guardrails) do not survive an agent that keeps rewriting itself. We propose the governable individual: an agent whose competence may change without bound, but whose authority, memory schema, embodiment rights and capabil...

---

### 8. Beyond DSA: Conjugacy-based Comparison of Dynamical Systems

**Authors:** Prakhar Godara, Pang Shiang Tay, Marcelo G. Mattar

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04493v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04493v1)

**Summary:** Comparing whether two dynamical systems implement the same computation despite differences in coordinates or measurements is a central problem in neuroscience and machine learning. Dynamical Similarity Analysis [DSA; Ostrow et al., 2023] addresses this problem by aligning finite-dimensional Koopman approximations through an orthogonal similarity transformation. Here we show that orthogonal alignment is neither necessary nor sufficient for topological conjugacy: conjugate systems may require a no...

---

### 9. Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation

**Authors:** Amrith Lotlikar, Ian Christopher Tanoh, Praful Vasireddy, et al.

**Published:** 2026-07-05

🔗 [Paper](http://arxiv.org/abs/2607.04063v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04063v1)

**Summary:** Multi-compartment Hodgkin-Huxley (HH) models provide a principled framework for predicting neural dynamics and responses to electrical stimulation. However, fitting HH biophysical parameters typically requires intracellular recordings, which are invasive and low-throughput, limiting the ability to capture the geometry and cell-specific properties of many neurons in a given neural circuit. Multi-electrode arrays (MEAs) offer a scalable alternative - high-density extracellular measurements from fu...

---

### 10. Microsecond-precision sound localization emerges from slow equilibrium dynamics

**Authors:** Toshio Irino

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03890v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03890v1)

**Summary:** Precise sound localization relies on microsecond sensitivity to interaural time differences (ITDs), yet binaural perception exhibits sluggish tracking of dynamic acoustic cues. How these properties coexist remains unresolved. Here, ITD is represented as a stable equilibrium of neural population dynamics rather than by the classical place-coding framework originally proposed by Jeffress in 1948. In this framework, excitatory and inhibitory interactions across frequency channels generate a populat...

---

### 11. Diffusion learning reveals viable parameter manifolds and compensation geometry in biological dynamical systems

**Authors:** Ruilin Zhang, Louis Tao, Zhuo-Cheng Xiao

**Published:** 2026-07-04

🔗 [Paper](http://arxiv.org/abs/2607.03671v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03671v1)

**Summary:** Models of complex systems often have many parameters, yet are constrained by far fewer experimentally accessible observables: similar activity can emerge from coordinated parameter changes. We formalize these compatible parameter sets as \emph{viable parameter manifolds}: the inverse images of a system's target dynamical behaviors under a parameter-to-feature map. The relevant codimension is not the number of reported features, but the effective rank of that map at the target scale. Co-varying f...

---

### 12. Shunting Inhibition and Dendritic Branching Shape Local Credit Assignment

**Authors:** Houman Safaai, Maceo Richards, Bernardo L. Sabatini

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.03556v1) | 📄 [PDF](https://arxiv.org/pdf/2607.03556v1)

**Summary:** Biological neurons assign credit across branching dendrites, where synaptic drive, dendritic conductance, local voltage, and somatic teaching signals interact to shape synaptic plasticity. We study conductance-based dendritic networks with E/I synapse banks, shunting inhibition, and tree-structured branch-to-soma coupling, and examine when restricted somatic feedback can approximate compartment-specific backpropagated errors. Exact gradients factor into local eligibility x compartment error term...

---

### 13. Modeling the Impact of Visual Brand Language on Attention, Object Recognition, and Memory Retrieval

**Authors:** Rachel F. Heaton, John E. Hummel

**Published:** 2026-07-03

🔗 [Paper](http://arxiv.org/abs/2607.02929v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02929v1)

**Summary:** Visual brand language is the set of visual properties that convey brand identity for a product. What is the impact of visual brand language on a person's ability to recognize and understand the functional identity of an object? Using an empirically supported modeling framework based on the JIM model of object recognition and the LISA model of analogical inference, we simulated the impact of visual brand language on object recognition, the allocation of attention, and retrieval of functional info...

---

### 14. A global predicted-fMRI drive signal from TRIBE does not predict YouTube replay heatmaps

**Authors:** Barada Sahu, Shivesh Pandey

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.01400v2) | 📄 [PDF](https://arxiv.org/pdf/2607.01400v2)

**Summary:** Deep multimodal brain-encoding models now predict fMRI responses to naturalistic video with high accuracy; whether their predicted neural signals also forecast behavioral engagement is unknown. We run TRIBE, the winning model of the 2025 Algonauts challenge (Llama-3.2 + V-JEPA 2 + Wav2Vec-BERT), on 48 YouTube videos and reduce its predicted cortical response to a per-second engagement curve, the global field power. Correlated against each video's "most replayed" heatmap, a proxy for re-watch, it...

---

### 15. DRIADA: A Python Toolkit for Cross-Scale Analysis of Single-Neuron Selectivity and Population Dynamics

**Authors:** Nikita Pospelov, Viktor Plusnin, Olga Rogozhnikova, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00851v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00851v1)

**Summary:** Brain activity spans single-neuron, population, and network levels, and core questions in neural coding require moving between them. Yet current tools target a single paradigm and incompatible data formats, leaving cross-level questions hard to address. We present DRIADA, an open-source Python framework that unifies neural signals and time-aligned behavior in a shared data model, so selectivity testing, dimensionality reduction, and network analysis operate within a unified workflow. We evaluate...

---

### 16. NeuroCogMap Reveals Cognitive Organization of Large Language Models

**Authors:** Zhongxiang Sun, Haolang Lu, Qiang Ma, et al.

**Published:** 2026-07-01

🔗 [Paper](http://arxiv.org/abs/2607.00397v1) | 📄 [PDF](https://arxiv.org/pdf/2607.00397v1)

**Summary:** Understanding how complex cognitive functions are organized within artificial systems is central to interpreting large language models (LLMs) and relating them to biological cognition. Yet although LLMs exhibit broad cognitive-like behaviours, it remains unclear whether their internal representations form reproducible functional systems that explain behaviour, failure and links to human cognition. Here we present NeuroCogMap, a cognitive neuroscience-inspired framework that organizes internal fe...

---

### 17. Stationary covariance spectra of discrete-time non-normal random recurrent dynamics

**Authors:** Jacob A. Zavatone-Veth

**Published:** 2026-06-30

🔗 [Paper](http://arxiv.org/abs/2606.31944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.31944v1)

**Summary:** Principal component analysis is widely used to characterize structure in the dynamics of recurrent neural networks. For stationary noise-driven dynamics, the distribution of variance among the principal components is determined by the spectrum of the stationary covariance matrix. While the spectral properties of this matrix are well-understood for linear networks with normal synaptic weight matrices, our understanding of the stationary covariance spectrum for random non-normal dynamics remains i...

---

### 18. Mean-field theory of rich oscillatory dynamics in low-rank recurrent networks with activity-dependent adaptation

**Authors:** Bowen W. Zheng, Earl K. Miller, Ila R. Fiete

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30366v1) | 📄 [PDF](https://arxiv.org/pdf/2606.30366v1)

**Summary:** We develop a dynamical mean-field theory for random recurrent networks with low-rank structure and firing-rate-driven adaptation. When the random connectivity is strong enough to generate chaos, increasing adaptation strength drives the network through four regimes: a static coherent state, noise-sustained oscillations that progress from regular to irregular, stochastic switching between symmetric wells, and a global limit cycle. The theory identifies two instability mechanisms, chaos onset from...

---

### 19. Cohort-amortized personalization: navigating the privacy-utility frontier for virtual brain twins

**Authors:** Amirhossein Esmaeili, Marmaduke Woodman, Nina Baldy, et al.

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.30329v2) | 📄 [PDF](https://arxiv.org/pdf/2606.30329v2)

**Summary:** Personalized generative brain models require individual neuroimaging data that privacy constraints and re-identification risk make difficult to share, while per-subject fitting procedures cost hours of compute -- limiting clinical translation and multi-site collaboration. We introduce cohort-amortized personalization (CAP), which replaces data sharing with model sharing: a neural density estimator is trained on simulations from a mechanistic whole-brain model under a low-rank cohort prior, and o...

---

### 20. Clear Mind: Meditation and the Brain's Signal-to-Noise Ratio

**Authors:** Ruben Laukkonen

**Published:** 2026-06-29

🔗 [Paper](http://arxiv.org/abs/2606.29698v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29698v1)

**Summary:** Meditation is quintessentially associated with a clear mind. This paper proposes that diverse findings in the science of meditation can be mapped onto a single, empirically tractable construct: functional signal-to-noise ratio in the brain, or f-SNR. Signal denotes neural variance that tracks the goal-relevant causes of sensory input, while noise denotes residual activity, including irrelevant endogenous fluctuations. Mechanistically, meditation increases f-SNR through two primary operations: se...

---

### 21. Geometric Stability of Neural Population Codes: Regional Variation, Behavioral Relevance, and Circuit Dependence

**Authors:** Prashant C. Raju

**Published:** 2026-06-28

🔗 [Paper](http://arxiv.org/abs/2606.29655v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29655v1)

**Summary:** Current models of representational reliability in neural populations focus on temporal stability: whether population centroids are preserved across sessions and days. This framing leaves a fundamental question unanswered: how reliably does the pairwise distance structure among stimuli reproduce across independent observations within a session? We argue that this property, geometric stability, constitutes an independent axis of representational analysis that existing frameworks do not capture. We...

---

### 22. Connectivity Estimation using Stochastic Graph Heat Modelling

**Authors:** Stephan Goerttler, Min Wu, Fei He

**Published:** 2026-06-27

🔗 [Paper](http://arxiv.org/abs/2606.29098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.29098v1)

**Summary:** A growing number of techniques leverage the spatial structures that underlie many real-world datasets. Despite these advances, the complementary task of estimating spatial structures and understanding their role within these techniques has often been overlooked. In neurophysiological data analysis specifically, numerous methods exist to estimate brain connectivity, but most are not explicitly model-based, dynamic, multivariate, or directed. To address these limitations, we previously introduced ...

---

### 23. Interpretable machine learning predicts Parkinson's disease severity using motion-corrected QSM MRI and multiband multiecho fMRI features

**Authors:** Aixa X. Andrade

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2607.02553v1) | 📄 [PDF](https://arxiv.org/pdf/2607.02553v1)

**Summary:** Introduction: Objective neuroimaging biomarkers may improve Parkinson's disease motor assessment by capturing brain variation not directly observable from clinical examination. We used interpretable machine learning to predict current motor severity, measured by MDS-UPDRS Part III, from QSM and multiband multi-echo resting-state fMRI-derived ReHo features.   Methods: Regional QSM and ReHo features were extracted from 28 participants, including 24 individuals with Parkinson's disease and 4 contro...

---

### 24. Modelling Emotional Memory in Children with Tensor Networks

**Authors:** Henry Groves, Lucia F. Jackson, Barbara-Anne Robertson, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.28470v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28470v1)

**Summary:** We demonstrate how emotional valence influences the order-dependent structure of children's recognition memory: correct recall of a sequence of emotionally-valenced toys depended not just on the valence of a given toy itself, but also on the valence of the toys shown before and after it. Whilst standard psychological models confirm that order-dependence differs across an event (a set of toys shown in sequence), accuracy is low and the model does not reflect how memory for an emotional object inf...

---

### 25. Heterogeneous synaptic motifs bridge microscale structure and macroscale nonlinear dynamics

**Authors:** Meiyi Zhang, Jinjian Yu, Louis Tao, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27946v1)

**Summary:** Recent breakthroughs in synaptic-resolution network connectomics have revealed that brain circuits feature fine-scale structural connectivity, such as pairs of correlated synaptic couplings known as second-order motifs. Large-scale recordings of neuronal activity in networks containing nonlinear neurons reveal macroscopic heterogeneous population dynamics throughout the brain. These findings rekindle the inquiry into this intriguing question: Can microscale synaptic structures contribute to macr...

---

### 26. CANNs: A Toolkit for Research on Continuous Attractor Neural Networks

**Authors:** Sichao He, Aiersi Tuerhong, Shangjun She, et al.

**Published:** 2026-06-26

🔗 [Paper](http://arxiv.org/abs/2606.27783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27783v1)

**Summary:** Continuous attractor neural networks (CANNs) are the canonical computational framework for how the brain encodes continuous variables such as spatial position, head direction, and movement direction, and explain the activity of hippocampal place cells, entorhinal grid cells, and head-direction cells. CANN research, however, is fragmented: most results rest on lab-specific implementations, general-purpose simulators lack CANN-specific abstractions, and the path from spike trains to attractor geom...

---

### 27. Modelling chronic stress as an excitatory-inhibitory perturbation in recurrent working-memory networks

**Authors:** Mauricio A Diaz, Manuela A. Beyer, Janina Hesse

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.27529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.27529v1)

**Summary:** Stress is an adaptive response coordinated by neural and physiological systems. While acute stress can enhance survival, chronic stress drives structural brain changes, cognitive dysfunction, and increased psychiatric risk. At the cellular level, chronic stress shifts the excitatory-inhibitory (E/I) balance of prefrontal pyramidal neurons toward inhibitory dominance, yet the mechanisms underlying these alterations are still unknown. We here investigate possible mechanisms causing inhibitory domi...

---

### 28. Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems

**Authors:** Claus Metzner, Ali Ghebleh, Achim Schilling, et al.

**Published:** 2026-06-25

🔗 [Paper](http://arxiv.org/abs/2606.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26733v1)

**Summary:** Complex adaptive systems often develop organized structures without centralized control. Yet the local mechanisms by which functional organization emerges and persists remain incompletely understood. Here we propose Surviving by Serving (SBS) as a general principle of self-organization: components persist as long as their outputs are utilized by other components, whereas prolonged non-utilization promotes adaptation and exploration. To investigate this idea, we introduce a minimal multi-agent mo...

---

### 29. Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist

**Authors:** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26448v1)

**Summary:** Across the sciences, autonomous systems are increasingly being used in closed-loop discovery, proposing new theories and designing and running experiments to test them. This approach is yet to be applied in the field of cognitive science, where the central bottleneck is theory-building: the creative step of turning the accumulated failures of existing models into better ones. Theory generation has remained manual even as data collection, modeling, and experiment design have been automated. We pr...

---

### 30. Beyond Single-Source Cognitive Taskonomy:Multi-Source Task Relations through fMRI Transfer Learning

**Authors:** Junfeng Xia, Wendu Li, Mengjiao Zhang, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.26279v1) | 📄 [PDF](https://arxiv.org/pdf/2606.26279v1)

**Summary:** Cognitive tasks are organized by shared and specialized neural processes. Masked fMRI reconstruction provides a common self-supervised objective for quantifying transfer relations among task states, but existing reconstruction-based taskonomies mainly study one-to-one transfer from a single source task to a target. Here, we extend an fMRI cognitive taskonomy from single-source to multi-source transfer across 23 Human Connectome Project task states and use Boolean Integer Programming (BIP) to ana...

---

### 31. Topology-Dependent Emergence of Polychronous Neuronal Groups: A Recurrence-Plot Characterization

**Authors:** Lucas A. T. X. Carneiro, Armand D. Jiofack, Fernando F. Ferreira

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25874v1)

**Summary:** Polychronous Neuronal Groups (PNGs) reproducible, time-locked spatiotemporal firing cascades stabilised by Spike-Timing-Dependent Plasticity (STDP) and heterogeneous axonal delays provide a combinatorially rich substrate for neural computation whose structural determinants remain poorly understood. We simulate a recurrent network of N=1000 Izhikevich neurons over ten hours of biological time and identify 1545 unique PNGs via an offline event-driven detection algorithm. A parametric Watts-Strogat...

---

### 32. Weight geometry governs functional memory in complex systems

**Authors:** Elkaïoum M. Moutuou, Habib Benali

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.25826v1) | 📄 [PDF](https://arxiv.org/pdf/2606.25826v1)

**Summary:** Complex systems, from gene regulatory networks to neural circuits and transportation infrastructures, exhibit rich functional behaviour that topology alone does not capture. Here we show that functional memory exhibits a universal organisational regularity: in every biological, ecological, social, and technological domain studied, real interaction strengths organise memory at greater hierarchical depth than random weight assignment on the same topology, across thirty-four networks spanning sever...

---

### 33. Meta-learning as a principle for human-like visual representations

**Authors:** Can Demircan, Marcel Binz, Alireza Modirshanechi, et al.

**Published:** 2026-06-24

🔗 [Paper](http://arxiv.org/abs/2606.28399v1) | 📄 [PDF](https://arxiv.org/pdf/2606.28399v1)

**Summary:** The structure of human visual representations underpins our capacity for adaptive behaviour. While pretrained neural networks model human visual representations with unprecedented success, a large discrepancy remains. We propose one reason: these networks optimise a single fixed objective, whereas human representations must support open-ended tasks. We hypothesise this flexibility arises from meta-learning (learning to learn), a pressure shaping representations to acquire new tasks from few obse...

---

### 34. A pilot study examining transcranial photobiomodulation therapy intervention in college students with insomnia

**Authors:** Jiangshan He, Lianghua Zhang, Dan Liang, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24668v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24668v1)

**Summary:** College students commonly report insufficient sleep and poor sleep quality, with ~30% meeting insomnia criteria, posing significant threats to their physical growth, cognitive development, and overall well-being, as well as imposing a substantial economic burden on society [1]. The hyperarousal model of insomnia [2] emphasizes that hyperarousal across cognitive, emotional, and physiological domains mutually reinforces one another. Neuroimaging studies have further identified prefrontal hypoactiv...

---

### 35. EEG Interpretation Across Chant Listening: A Single-Subject Pilot Investigation Using Spectral and Functional Connectivity Analysis

**Authors:** Prerna Singh, Aishwarya Ghosh, Neelam Sinha, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24406v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24406v1)

**Summary:** This technical report presents an EEG-based investigation of neural activity across five auditory conditions: Resting State (RS), Shiv Tandav Stotra (STS), Mahasudarshan Mantra (MM), Aum Chant, and Tanpura Listening. EEG recordings acquired from a healthy 5-year-old participant were analyzed using spectral power estimation and functional connectivity measures based on the weighted Phase Lag Index (wPLI). Spectral analysis revealed condition-specific modulation of neural oscillatory activity, wit...

---

### 36. Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders

**Authors:** Xavier Vasques, Paul Barbaste, Olivier Oullier

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24394v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24394v1)

**Summary:** Electroencephalography (EEG) is the dominant non-invasive modality for brain-computer interfaces (BCIs), yet reliable decoding of motor imagery is hampered by inter- and intra-individual variability. A recurring claim is that one decoding pipeline, most often a spatial or Riemannian method, is broadly preferable. We test the weakest version of that claim under the most favourable conditions. Using the Mother of All BCI Benchmarks (MOABB) framework, we evaluated 1,056 decoding configurations (fea...

---

### 37. Graph-based analysis of inflammatory profiles in New Onset Refractory Status Epilepticus (NORSE)

**Authors:** Linon Denis, Martin Guillemaud, Vincent Navarro, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24351v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24351v1)

**Summary:** Background and Objectives: Cryptogenic new-onset refractory status epilepticus (cNORSE) represents one of the most severe forms of status epilepticus, occurring in patients without prior neurological disease, and remaining of unknown aetiology despite extensive diagnostic evaluation. Emerging evidence supports a role for immune dysregulation in cNORSE; however, marked heterogeneity in inflammatory signatures has been reported, complicating the selection of targeted immunotherapies. Therefore, a ...

---

### 38. The Morality Game: An online multiplayer platform to standardize, expedite, and expand research on cooperation

**Authors:** Gregory N. Stanley, Alan Yang, Liam Tsimhoni, et al.

**Published:** 2026-06-23

🔗 [Paper](http://arxiv.org/abs/2606.24037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.24037v1)

**Summary:** This paper presents the Morality Game, a platform designed to standardize and accelerate research on cooperation and morality through game theory-based experiments. The Morality Game functions as a video game for science, a hub for economic game research, an open-access data repository, and a tool for expediting the research process. It allows researchers to launch customized online multiplayer experiments with zero coding, using game trees to simulate moral dilemmas. The platform automates part...

---

### 39. Identifying structural design principles shaping the computational abilities of recurrent neural networks

**Authors:** Tom Talpir, Elad Schneidman

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23874v1)

**Summary:** Understanding how the architecture of neural networks shapes the computations they carry is a central challenge in neuroscience and machine learning. While specific circuit architectures have been linked to particular network computations and theoretical bounds on expressivity of broad classes of networks have been found, we are still missing general principles connecting the structure of finite networks to their computational capabilities. Here, we characterize the computational abilities of re...

---

### 40. The adaptive nature of confirmation bias

**Authors:** Dorje C. Brody, Karl J. Friston, Bernhard K. Meister, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23325v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23325v1)

**Summary:** In this paper, the phenomenon generally classified as confirmation bias is formulated on the space of square-root probabilities (or equivalently, using the structures of quantum probability). In this framework, observations are modelled by matrices, rather than random variables on a probability space. In the problem of binary hypothesis testing, an optimal evidence choice minimises the expected error probability. We show that the resulting optimal choice of evidence leads to a confirmation bias,...

---

### 41. Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg

**Authors:** Helio V. Cabral, Giacomo Valli, Roberto Zanotti, et al.

**Published:** 2026-06-22

🔗 [Paper](http://arxiv.org/abs/2606.23066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.23066v1)

**Summary:** Common synaptic input is considered a fundamental principle of motor neuron control and represents the dominant component of the neural drive transmitted from the motor neurons to muscle. Recent advances in High-Density surface Electromyography (HDsEMG) and motor unit (MU) decomposition algorithms have enabled the concurrent identification of increasingly large populations of MUs and substantially expanded the possibility of estimating common synaptic input from MU spike trains, making this appr...

---

### 42. SPIDER -- Stitched Power-spectra for Inferring Directed information flow from incomplete and asynchronous Experimental Recordings

**Authors:** Yisi S. Zhang, Daniel Y. Takahashi

**Published:** 2026-06-21

🔗 [Paper](http://arxiv.org/abs/2606.22695v2) | 📄 [PDF](https://arxiv.org/pdf/2606.22695v2)

**Summary:** Mapping the directed flow of information between brain regions -- their effective connectivity -- is central to understanding brain function, yet large-scale recordings sample only a fraction of the brain at a time: sessions, animals, and laboratories cover different, partially overlapping regions, usually without a shared temporal reference. Established directed-connectivity methods (Granger causality, dynamic causal modeling, partial directed coherence, PDC) require all regions to be recorded ...

---

### 43. DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics

**Authors:** Jayadratha Gayen, Bradly Alicea

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21940v1)

**Summary:** Understanding how a nervous system wires itself from birth to adulthood is a fundamental challenge in developmental neuroscience. We present DevoTG, a temporal graph framework that applies Temporal Graph Neural Networks (TGNs) to two complementary representations of C. elegans neural development: a Continuous-Time Dynamic Graph (CTDG) of cell division events derived from cell lineage data, and a Discrete-Time Dynamic Graph (DTDG) of the developing synaptic connectome spanning eight reconstructed...

---

### 44. Dynamic Computerized Tumbling-E Testing for Temporal Reliability of Human Sequential Perceptual Decisions

**Authors:** Avneek Sandhu, Bin Hu

**Published:** 2026-06-20

🔗 [Paper](http://arxiv.org/abs/2606.21818v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21818v1)

**Summary:** OBJECTIVES: Visual acuity and tumbling-E tasks are often treated as static threshold measures, yet sequential perceptual decisions unfold over time. A computerized tumbling-E task preserves response latency, timeouts, and stimulus-size adaptation, creating a temporal reliability dataset rather than only a chart-line score. This matters for human-AI comparison because the Temporal Hallucination Index (THI) shows how static accuracy can obscure delays, drift, persistence, and unstable convergence....

---

### 45. Mostly-monocular responses and other visual functions in a multiscale network model of Macaque V1

**Authors:** Zhuo-Cheng Xiao, Kevin K. Lin, Lai-Sang Young

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21785v2) | 📄 [PDF](https://arxiv.org/pdf/2606.21785v2)

**Summary:** Visual signals from the two eyes merge gradually as they pass through the primary visual cortex (V1). Here we use a computational model of Macaque V1 to study the first stage of this integration along the magnocellular pathway, in layer 4C$α$, aiming to infer neuroanatomical origins of binocular response. It is known that neurons in layer 4C$α$ are predominantly monocular, though some do exhibit varying degrees of binocularity. We find (1) the emergence of narrow binocular strips along borders o...

---

### 46. Delay coordinates synchronization and induces abrupt transition in excitable networks

**Authors:** Bruno R. R. Boaretto, Kalel L. Rossi, Lyle E. Muller, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21703v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21703v1)

**Summary:** Neuronal communication is inherently time-delayed, due to the finite speed of signal propagation. Although often considered challenging or disruptive, such time delays can also endow neural circuits with useful capabilities. Here, we show that delays in excitatory connections between excitable neurons coordinate their synchronization patterns by creating self-sustained oscillations that may be out-of-phase or in-phase. The emergence of these oscillations leads to an abrupt, explosive, transition...

---

### 47. Adaptive conduction delays and phase locking in spiking Haken Lighthouse networks

**Authors:** Stephen Coombes, Rüdiger Thul, Stefan Ruschel, et al.

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21508v1)

**Summary:** We develop a theory of phase-locked activity in delayed spiking networks using the Haken Lighthouse model as an analytically tractable event-based description of neural dynamics. For networks with fixed delays, we derive self-consistency conditions for phase-locked states and an associated linear stability theory formulated directly in terms of spike-time perturbations. The framework is illustrated for a delayed autapse, a reciprocally coupled two-cell network, and spatially structured rings wit...

---

### 48. Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity

**Authors:** Ch. Meessen

**Published:** 2026-06-19

🔗 [Paper](http://arxiv.org/abs/2606.21432v1) | 📄 [PDF](https://arxiv.org/pdf/2606.21432v1)

**Summary:** We construct a minimal but biologically plausible spiking neuron model operating in discrete time, combining multiplicative spike-timing-dependent plasticity (WSTDP), divisive normalization of synaptic integration, homeostatic threshold adaptation, and a one-step refractory period. We show that this normalization admits a biologically plausible dendritic implementation in which each binary junction operates using only locally available information.   Assembling excitatory-inhibitory pairs of suc...

---

### 49. Relational Gaze Transitions During Encoding Predict Episodic Recall of Naturalistic Scenes

**Authors:** Hugo Rydel, Alex Kafkas

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20844v1) | 📄 [PDF](https://arxiv.org/pdf/2606.20844v1)

**Summary:** Remembering a visual scene requires organizing distinct details into a cohesive event. This study investigates whether relation-guided gaze transitions provide a behavioural marker of this cognitive organization during episodic encoding and retrieval. By applying scene graph annotations to eye-tracking data, we measured whether gaze moved between objects that were meaningfully related within complex scenes. This approach allowed us to quantify relational scanning within naturalistic environments...

---

### 50. Synchronization modes in bipartite oscillator networks

**Authors:** Pau Pomés, Bastian Pietras, Ernest Montbrió

**Published:** 2026-06-18

🔗 [Paper](http://arxiv.org/abs/2606.20345v2) | 📄 [PDF](https://arxiv.org/pdf/2606.20345v2)

**Summary:** Collective oscillations in neuronal systems often arise from interactions between excitatory and inhibitory populations rather than from recurrent coupling within a single ensemble. Motivated by the coexistence of strongly and partially synchronized regimes in such systems, we study the Kuramoto Sakaguchi model on a bipartite network. Despite its minimal structure, the model exhibits rich collective dynamics, including both continuous and discontinuous transitions from full synchrony to partial ...

---

## stat.ML

**50 papers**

### 1. Avoiding unsafe sets when training with Langevin Dynamics

**Authors:** Adam M. Oberman

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07538v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07538v1)

**Summary:** Training a model with noisy gradient descent can be idealized as overdamped Langevin dynamics on the loss landscape, and a natural safety question is to bound the probability $ν_t(\mathcal{A}_H) = \mathbb{P}(Q_t \in \mathcal{A}_H)$ that the trajectory lies in a designated failure region $\mathcal{A}_H$. We study this for a smooth, strongly convex loss in $d$ dimensions and a failure region separated from the minimizer by an energy gap. Three bounds emerge. At the end of training, the equilibrium...

---

### 2. A Unified Detection Framework for AI-Related Content and Artifacts

**Authors:** Xifeng Zhang, Tao Hu, Yijie Peng, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07527v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07527v1)

**Summary:** Artificial intelligence (AI) is a double-edged sword: while it has achieved remarkable success across a wide range of domains, its deployment also calls for effective oversight and regulation, for which the detection of AI-related content and artifacts is perhaps the most direct and cost-effective approach. To this end, we propose a unified detection framework based on Mahalanobis distance scores (MDS), applicable to several important settings, including the detection of large language model (LL...

---

### 3. Fast Rates for Semi-Supervised Learning via Data-Augmentation Graph Regularization

**Authors:** Adam M. Oberman

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07513v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07513v1)

**Summary:** Self-supervised learning matches supervised accuracy from a fraction of the labels, but the labeled-sample efficiency behind this has lacked a theoretical explanation. We provide one. Data augmentation induces a similarity graph on the unlabeled data, so downstream learning on that graph is graph-Laplacian-regularized learning. We prove a fast transductive rate, $O(1/n_L)$ in the number of labels, in place of the supervised $O(1/\sqrt{n_L})$, by carrying the leave-one-out stability apparatus of ...

---

### 4. Statistical inverse learning and $\ell^1$-regularization

**Authors:** Abhishake Rastogi, Tatiana A. Bubba, Tapio Helin, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07468v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07468v1)

**Summary:** We study the recovery of sparse functions from finite, noisy, and indirect observations in the framework of statistical inverse learning. The unknown is modeled as an element of $\ell^1$, and observations are generated through a possibly nonlinear forward operator $A:\ell^1\to H$, where $H$ is a vector-valued reproducing kernel Hilbert space. We propose an $\ell^1$-regularized empirical risk minimizer and develop a theoretical analysis of its statistical properties.   Under mild assumptions, we ...

---

### 5. The Optimal Sample Complexity of Learning Autoregressive Chain-of-Thought

**Authors:** Zhiyuan Li

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07423v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07423v1)

**Summary:** We prove that, in the realizable PAC setting, the sample complexity of exact-trace learning for full autoregressive Chain-of-Thought traces is upper bounded by the standard multiclass rate of the local next-token class, where this rate is governed by the Daniely--Shalev-Shwartz dimension. Under exact-trace loss, one wrong action makes the whole trace incorrect; nevertheless, for every stopping rule $\mathtt{halt}$ and every pointwise $\mathtt{halt}$-halting local class $\mathrm{H}$, $n_{\mathrm{...

---

### 6. DiPhon: Diffusion on Graphons for Scalable Graph Generation

**Authors:** Sergio Rozada, Yiming Qin, Manuel Madeira, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07232v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07232v1)

**Summary:** Diffusion models represent a leading paradigm for graph generation, with notable impact in domains such as molecular design. Yet, scaling these models to large graphs remains an open problem. We approach this question in the dense-graph setting through the lens of graphons, the size-agnostic limit objects of dense graph sequences, to study how structural graph statistics behave across node-size scales. This perspective leads to DiPhon, a diffusion framework for size-scalable graph generation. Sp...

---

### 7. Gauge-Invariant Learnable Spectral Positional Encodings for Directed Graphs via Hermitian Block Krylov Subspaces

**Authors:** Jiaqing Xie, Yuxin Wang

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07032v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07032v1)

**Summary:** Spectral positional encodings (PEs) for \emph{directed} graphs face two obstacles: magnetic Laplacians require an $O(n^3)$ Hermitian eigendecomposition per potential, and their complex eigenvectors are defined only up to unitary gauge, which prior work handles with basis-invariant architectures. We propose learnable spectral PEs of the form $h_θ(A_q)\,R$, where $A_q$ is a normalized magnetic operator, $h_θ$ a learnable scalar spectral response, and $R$ a block of random probes. Because the PE is...

---

### 8. Local large deviations for linear-region growth in random piecewise-linear networks

**Authors:** Recep Özkan, Christian Hirsch

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07014v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07014v1)

**Summary:** We study a random compositional model for the growth of affine regions in deep piecewise-linear networks. The model is generated by i.i.d.\ perturbations of the symmetric height-one tent map, and the main observable is the number \(N_n\) of affine pieces after \(n\) layers. We prove the existence of a submultiplicative pressure for \(N_n\), yielding exponential upper bounds for both tails of \(n^{-1}\log N_n\). The same argument applies to abstract submultiplicative complexity observables and gi...

---

### 9. Tensorized algorithms and scalable filtering methods for hidden Markov and factorial hidden Markov models

**Authors:** Roxana Barrios, Ioannis Sgouralis

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.07008v1) | 📄 [PDF](https://arxiv.org/pdf/2607.07008v1)

**Summary:** A common method for the representation and analysis of time-series data is the hidden Markov model (HMM), where each observation is associated with a hidden state that evolves over time. However, many real-world systems are influenced by multiple independent factors, which are more naturally represented by factorial hidden Markov models (fHMM), where several hidden Markov chains jointly generate the observed data. Although an fHMM provides a richer and more realistic representation of many real-...

---

### 10. Transfer Learning for Linear Discriminant Analysis with a Shared Classification Signal

**Authors:** Yonghan Zhang, Yimeng Fan, Wenya Luo, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06936v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06936v1)

**Summary:** This paper studies transfer learning for linear discriminant analysis in high-dimensional two-class classification. We consider one target domain and several source domains, where the mean difference in each domain is decomposed into a deterministic common component and a domain-specific random deviation. The common component represents a shared classification signal across domains, while the random deviation captures domain-specific heterogeneity. Under spiked covariance models, we derive deter...

---

### 11. Finding a stationary point of a stochastic convex problem

**Authors:** Felipe Areces, John Duchi, Malo Sommers

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06883v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06883v1)

**Summary:** We consider the problem of finding stationary points for stochastic convex optimization problems. Rather than surrogates to stationarity, such as a proximity-to-stationarity guarantee or small gradient of the Moreau envelope, we ask for a stronger notion: that the subdifferential of the objective actually contains a small element. This criterion is non-trivial, because subdifferentials of convex functions fail to converge uniformly, even in arbitrarily small neighborhoods of the optimum. Our con...

---

### 12. Best-Arm Identification with Generative Proxy

**Authors:** Tianyi Ma, Hanzhang Qin, Ruihao Zhu, et al.

**Published:** 2026-07-08

🔗 [Paper](http://arxiv.org/abs/2607.06879v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06879v1)

**Summary:** Best-arm identification is a canonical model for data-driven decision-making, but in many applications each reward observation is costly. Motivated by the growing availability of cheap predictions from machine learning and large language models, we study fixed-confidence best-arm identification in which each costly reward pull is paired with a cheap but correlated proxy score. The marginal mean of the proxy can be estimated offline and is treated as known, whereas its correlation $ρ$ with the re...

---

### 13. Tensor Train Diffusion: Leveraging Low-Rank Structures for High-Dimensional Score-Based Sampling

**Authors:** Robert Gruhlke, Julius Berner, David Sommer, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06841v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06841v1)

**Summary:** Diffusion models offer a powerful framework for sampling from complex probability densities by learning to reverse a noising process. A common approach involves solving for the time-reversed stochastic differential equation (SDE), which requires the score function of the evolving sample distribution. The logarithm of this distribution's density is governed by a Hamilton-Jacobi-Bellman (HJB) type partial differential equation (PDE). However, current methods for solving this PDE, such as PINNs or ...

---

### 14. Heat-Kernel Entropy Profiles and Geometric Effective Sample Size for Weighted Measures on Manifolds

**Authors:** Kisung You

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06696v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06696v1)

**Summary:** Weighted empirical measures on compact manifolds arise in importance sampling, particle approximations, posterior summaries, quadrature, and representation learning. Standard weight-only summaries, such as ordinary effective sample size, ignore the geometry of the support. We introduce heat-kernel entropy profiles, a multiscale summary that diffuses weighted atoms by intrinsic heat flow and tracks nonuniformity across scales. For order-two Rényi entropy, the profile is computable from pairwise h...

---

### 15. From Jumps to Signatures: a Generative Method for Temporal Point Processes

**Authors:** Niels Cariou-Kotlarek, Vasileios Lampos

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06652v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06652v1)

**Summary:** Rough path signatures are a universal feature map for continuous paths and, via the expected signature, characterise path distributions. These guarantees do not directly extend to cadlag paths of Temporal Point Processes (TPPs), limiting the use of signature methods for event sequences. Furthermore, neural TPP models, including recent generative approaches, optimise per-event objectives with no global sequence-level loss, while evaluation of variable-length event sequences lacks distributional d...

---

### 16. EntroPath: Maximum Entropy Path Ensemble Embedding for Manifold Learning

**Authors:** Przemysław Rola

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06497v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06497v1)

**Summary:** We introduce EntroPath, a manifold learning method that recovers geodesic geometry from data graphs through ensembles of diffusion paths. Many existing graph-based embeddings rely either on locally normalised random walks or on shortest-path distances. The former can concentrate diffusion in densely sampled regions, while the latter are sensitive to spurious shortcut edges in the graph. EntroPath instead builds its dissimilarities from the maximum entropy random walk (MERW), which aggregates the...

---

### 17. Fast determinantal sampling on general spaces and diffusion geometry

**Authors:** Hoang-Son Tran, Pranav Gupta, Subhroshekhar Ghosh

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06644v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06644v1)

**Summary:** Determinantal point processes have recently emerged as a kernel-based alternative to standard independent sampling for constructing efficient minibatches, coresets, and other compact representations of large-scale datasets. In particular, sampling mechanisms based on DPPs are believed to demonstrate better approximation properties compared to classical i.i.d. samplers, even at the scale of the exponent. One of the key strengths of DPP based samplers is that they can be deployed over very general...

---

### 18. A Function-Space Dichotomy for Compositional Learning: Exponential Sub-Optimality of the Neural Tangent Kernel

**Authors:** Arkaprabha Ganguli, Emil Constantinescu

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06382v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06382v1)

**Summary:** A persistent empirical observation is that trained neural networks outperform their neural tangent kernel (NTK) limit on tasks with compositional structure, yet a quantitative account of $\textbf{when}$ and $\textbf{by how much}$ has been lacking. Working on the unit circle, we give such an account through a dichotomy between two complexity measures of the target: its $\textbf{Fourier complexity}$, which controls NTK kernel regression, and its $\textbf{architectural complexity}$, which controls ...

---

### 19. Feature Learning for the High Dimensional Stationary Schödinger Equation with Deep Ritz Method

**Authors:** Yao Yao, Yulong Lu, Gilad Lerman

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06369v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06369v1)

**Summary:** This paper investigates feature learning within the framework of the deep Ritz method for solving the stationary Schrödinger equation with Neumann boundary conditions. We first analyze the convergence of Riemannian gradient descent in an agnostic setting, where the hypothesis function is restricted to a single-index model while the PDE solution is arbitrary. We prove that gradient descent reaches an approximate global minimum: after T = O(log(1/ε)) iterations, the loss is within εof a constant m...

---

### 20. Factor-Augmented Machine Learning Panel Regressions

**Authors:** Andrii Babii, Luca Barbaglia, Eric Ghysels, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06368v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06368v1)

**Summary:** This paper develops the asymptotic theory for high-dimensional panel data regressions in settings with cross-sectionally dependent errors driven by common shocks. We consider a factor-augmented sparse-group LASSO estimator that combines MIDAS aggregation with latent factors. The estimator can take advantage of the mixed-frequency group structure in the time-series dimension. Theory shows that it can outperform the standard LASSO estimator both for prediction and estimation while allowing for cro...

---

### 21. Approximate Risk Minimization Over Shrinking-Thresholding Rules in Normal Mean Estimation

**Authors:** Wei Jiang

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06367v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06367v1)

**Summary:** We develop an approximate risk minimization framework for shrinkage-thresholding estimation in normal mean problems. In the canonical multivariate normal mean model, we introduce a general functional class of estimators that contains classical shrinkage and thresholding behavior, including James-Stein-type and lasso-type rules. We express quadratic risk as a functional over this class, derive optimality conditions for both oracle risk and data-driven approximate risk minimization, and construct ...

---

### 22. A unified perspective of Gaussian process approximation for differential equations

**Authors:** Mengwu Guo

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06292v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06292v1)

**Summary:** The use of Gaussian processes for approximating differential equations has expanded rapidly, leading to a growing, diverse, and fragmented body of numerical methods. We present a unified Bayesian perspective that places these techniques within a common probabilistic framework, based on a derivative matching interpretation for incorporating differential equation constraints into likelihood. This unified perspective supports both parameter estimation and solution approximation, and shows how a ran...

---

### 23. Quantitative Gaussian-Process limits of Tensor Programs

**Authors:** Andrea Agazzi, Eloy Mosig García, Dario Trevisan

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06290v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06290v1)

**Summary:** We study the infinite-width Gaussian-process limit of random neural networks   through the lens of tensor programs, and we provide a quantitative convergence   theory in Wasserstein distance.   Our main result gives explicit finite-width error bounds, of order inverse square-root of the widths   between finite-network executions and their   Gaussian-process limits. The framework is architecture-agnostic and covers feed-forward models together   with weight-sharing schemes relevant for recurrent ...

---

### 24. A Convex Approximation Framework for Neural Likelihood-Based Bayesian Inverse Problems

**Authors:** Fabian Schneider, Tapio Helin, Leila Taghizadeh

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06252v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06252v1)

**Summary:** Many problems in science and engineering are difficult to model accurately, either due to unknown physical mechanisms, poorly quantified measurement uncertainty, or prohibitive computational costs of high-fidelity simulations. These challenges limit the applicability of classical probabilistic inference methods such as Markov chain Monte Carlo, especially in high-dimensional Bayesian inverse problems. As data from scientific experiments become increasingly available, machine learning methods off...

---

### 25. Closed-form fractional radial links for elliptical Mahalanobis discriminant analysis

**Authors:** Serhii Zabolotnii

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06089v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06089v1)

**Summary:** We study binary classification under shared-generator elliptical class-conditional distributions. The log-likelihood ratio is an additive function of the two squared Mahalanobis radii, with radial link $\varphi=\log g$; QDA is recovered only when this link is affine. We derive the Bayes radial-link family from the within-class radius law and estimate it by a finite fractional-power stochastic-polynomial projection instead of tuning a generic spline. The link is identifiable from the radius law, ...

---

### 26. Separation Capacity of Scattering Networks on Low-Dimensional Datasets

**Authors:** Konstantin Häberle, Helmut Bölcskei

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06048v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06048v1)

**Summary:** We aim to identify scattering network architectures that maximize the separation capacity on data with low intrinsic dimension. The networks we consider employ a fixed monomial nonlinearity and no pooling, so that the only design variable is the frame generated by the network filters. For data modeled as rectifiable sets, we first characterize and bound the separation capacity of general feature extractors in terms of the geometry of the dataset. We then particularize to scattering networks and ...

---

### 27. Stochastic generator of trajectories from record data: application to the fluctuations of a glacier's frontal position from a sample of moraines

**Authors:** Megret Maud, Mike Pereira, Nicolas Eckert, et al.

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06020v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06020v1)

**Summary:** The record values theory study elements of a time series that exceed all previous observations, which are of particular interest in fields such as sports or climate science. In this paper, we propose a statistical method based on the construction of a Brownian stochastic simulator to reconstruct entire time series solely from such record values, even in a non-stationary case. We then implement a procedure, which can be compared to a Neural-Based Inference (NBI) procedure, to choose the optimal g...

---

### 28. On the convergence of graph Laplacians with a symmetric divergence

**Authors:** Liane Xu

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.05892v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05892v1)

**Summary:** When analyzing a manifold learning algorithm for data lying on a smooth, compact, connected Riemannian submanifold $(\mathcal{M}, g)$ of $\mathbb{R}^d$, a key estimate for the geodesic distance $d_g$ is that there exists $K > 0$ such that $0 \leq d_g(p, q)^2 - \|p-q\|^2 \leq K d_g(p, q)^4$ for all $p, q \in \mathcal{M}$. We observe that more generally, when $\mathcal{M}$ is equipped with a smooth symmetric divergence $D$ satisfying a non-degeneracy condition and $g$ is given by $g_p := \frac{1}{...

---

### 29. No Subspace to Track: Non-Identifiability and Optimizer State in Low-Rank Training

**Authors:** Noel Thomas

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.05872v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05872v1)

**Summary:** Memory-efficient optimizers such as GaLore train large language models by projecting gradients onto a rank-r subspace recomputed every T steps, assuming this subspace is a slowly drifting object that can be tracked. We show that beyond a small reproducible core, there is no such object. Two estimates of the top-r subspace computed at the same step from disjoint minibatches disagree as much as estimates computed T steps apart (0.73 vs 0.74 of the maximal chordal distance sqrt(2r), at Pythia-160M ...

---

### 30. A Quiet Failure in Calibrated Virtual Screening: Marginal Conformal Prediction Under-Covers the Minority Class, and a Class-Conditional Fix Recovers It

**Authors:** Muhammadjon Tursunbadalov, Mustafojon Tursunbadalov

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.06605v1) | 📄 [PDF](https://arxiv.org/pdf/2607.06605v1)

**Summary:** Conformal prediction is being adopted in drug discovery to put an honest number on model reliability: pick an error rate alpha, and the method returns prediction sets containing the true label with probability at least 1 - alpha. We show this guarantee can be dangerous on imbalanced datasets. Across four datasets, standard (marginal) conformal prediction hits its global 90% coverage target while leaving the minority class badly exposed: realized minority coverage falls to 64.8% on blood-brain-ba...

---

### 31. Boosting with List-Decodable Codes

**Authors:** Addison Prairie, Li-Yang Tan

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.05791v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05791v1)

**Summary:** Boosting is a fundamental technique for generically improving the accuracy of learning algorithms (Schapire 1989). Existing boosting algorithms construct a strong learner using $O(\log(\frac{1}ε)/γ^2)$ calls to a $γ$-advantage weak learner, and this round complexity is known to be optimal for generic boosters that succeed on all concept classes (Freund 1995). We show that this lower bound can be circumvented for concept classes that satisfy a mild closure property.   Specifically, we present a n...

---

### 32. Width-Robust Learnability in Mean-Field Bayesian Neural Networks

**Authors:** Dmitry Vaintrob, Kaarel Hänni

**Published:** 2026-07-07

🔗 [Paper](http://arxiv.org/abs/2607.05735v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05735v1)

**Summary:** Infinite-width limits are a standard way to reason about neural networks, but it is not automatic that the limiting learner has the same complexity-theoretic inductive bias as large finite networks. We study this question for Bayesian neural networks at the mean-field, or critical feature-learning, scaling. The central quantity is the \emph{reduced entropy} \[   s_\infty(y,\varepsilon)=\limsup_N -\frac{1}{N}\log π_N^0(L\le \varepsilon), \] the intensive prior cost of representing a target functi...

---

### 33. Beyond Heuristic Tuning: Power-Calibrated LLM Watermarking

**Authors:** Xiaopu Wang, Zelin He, Chengyuan Liu, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05694v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05694v1)

**Summary:** Logit-based watermarking is a widely used mechanism for identifying LLM generated content, yet its effectiveness is governed by a fundamental trade-off between detectability and semantic distortion. Existing analyses provide limited guidance for principled hyperparameter selection, leaving practical deployments reliant on heuristic tuning. In this work, we develop a power-calibrated statistical framework that establishes explicit quantitative relationships between watermark hyperparameters, dete...

---

### 34. Exact computation of posterior distribution of mixture weights in hierarchical Bayesian models

**Authors:** Georgy Meshcheryakov

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05692v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05692v1)

**Summary:** Hierarchical mixture models are a powerful tool for modeling data generated from heterogeneous sources, particularly when the mixing proportion $\boldsymbol{w}$ itself is treated as a random variable with a Dirichlet or Beta-Liouville prior. Such models are widely employed in scenarios where uncertainty in class membership or data-generating processes must be probabilistically quantified. This paper studies the exact marginalization of the mixture weight. For the two-component case we give an $O...

---

### 35. To Retain or to Adapt? Generalizing Continual Learning

**Authors:** Giulia Lanzillotta, Mandana Samiei, Doina Precup, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05609v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05609v1)

**Summary:** The Continual Learning (CL) literature has long been driven by the goal of mitigating catastrophic forgetting. This objective rests on a pervasive, often unstated assumption: that a lifelong learner should approximate the Joint-Task Learning (JTL) solution and retain all previously acquired knowledge. We challenge this retention-centered premise, arguing that in non-stationary environments prioritizing retention can impede real-time adaptation. Shifting the focus to the Average Lifelong Error (A...

---

### 36. Deep Neural Variation Spaces: A Unifying Perspective on Depth and Complexity

**Authors:** Julia Nakhleh, Robert D. Nowak

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05546v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05546v1)

**Summary:** We develop a unified function space theory of deep fully connected neural networks. Functions in our spaces are defined recursively as $\ell^1$-bounded linear combinations of activated functions from preceding layers, with a dictionary of affine functions at the first layer. Unlike existing theories that are largely specialized to homogeneous activations such as the ReLU, our framework provides a meaningful notion of functional complexity for deep networks with a broad range of homogeneous and n...

---

### 37. Higher-Order Certified Robustness for Regression

**Authors:** Jie Zhang, Natalie Frank

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05536v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05536v1)

**Summary:** Randomized smoothing has emerged as a scalable technique for certifying the adversarial robustness of classifiers. However, its application to regression remains under-explored and faces unique challenges. Existing regression certificates rely on probabilistic acceptance regions and fail to exploit the local geometry of the function. In this work, we present a novel framework for certified robust regression that addresses these limitations. We derive a prediction-centered certificate that guaran...

---

### 38. What Does a Discrete Diffusion Model Learn?

**Authors:** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05381v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05381v1)

**Summary:** What does a discrete diffusion model learn: a denoiser, a score ratio, or a bridge plug-in predictor? At the level of jump rates, these are one object in different coordinates, and reading a neural network in the wrong coordinate changes the process being trained and sampled. Starting with a rigorous derivation of the continuous-time Markov chain (CTMC) ELBO for any noising process, boundary terms included, we prove the \emph{Oracle Distance} theorem: the negative ELBO is exactly equal to the da...

---

### 39. Fitted Occupancy-Ratio Evaluation without Bellman Completeness

**Authors:** Lars van der Laan, Nathan Kallus

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05375v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05375v1)

**Summary:** Occupancy ratios correct distribution shift in offline reinforcement learning and are central to off-policy evaluation. Existing primal-dual and minimax methods typically estimate these ratios by enforcing occupancy-balance moments over a critic class. We propose fitted occupancy-ratio evaluation (FORE), a fitted fixed-point method that characterizes the discounted occupancy ratio through an adjoint Bellman recursion. At each iteration, FORE solves a single-level density-ratio objective on one-s...

---

### 40. TREK: Distill to Explore, Reinforce to Refine

**Authors:** Yuanda Xu, Zhengze Zhou, Kayhan Behdin, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05339v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05339v1)

**Summary:** Group Relative Policy Optimization (GRPO) is effective when the current policy already samples useful reasoning trajectories, but it stalls on hard prompts whose correct solution modes lie outside the student's on-policy support. We propose TREK (Teacher-Routed Exploration via Forward KL), a simple staged procedure that uses distillation not for imitation but for exploration support expansion. A key advantage of TREK is its generality: because it only consumes verified output trajectories, it ca...

---

### 41. Locally Private Online Quantile Regression: Estimation and Inference

**Authors:** Yi Liu, Qirui Hu

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05312v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05312v1)

**Summary:** We study estimation and inference for online quantile regression under a one-report user-level $\eps$-locally differentially private ($\eps$-LDP) protocol. The main difficulty is that the standard quantile-regression estimating-equation contribution couples covariates with a residual comparison, so a server that receives only privatized reports cannot form the usual online update. We address this by developing a finite-alphabet channel in which each user computes the contribution locally, applie...

---

### 42. Emputation: Identification-Guided Neural Imputation Framework

**Authors:** Yanjiao Yang, Yikun Zhang, Xinwei Shen, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05279v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05279v1)

**Summary:** We propose Emputation, a deep generative framework for learning imputation models. Emputation targets the extrapolation distribution of missing variables given observed variables, and training is guided by specific missingness assumptions that guarantee identification of the target distribution. The training objective, called the emputation risk, is an energy-score-based risk in which the identification assumption determines how observed entries are masked and which observations contribute to tr...

---

### 43. msPCA: An R Package for Sparse PCA with Multiple Components

**Authors:** Ryan Cory-Wright, Jean Pauphilet

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05229v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05229v1)

**Summary:** We present msPCA: an open-source R package for sparse principal component analysis with multiple components. It implements an alternating maximization algorithm to generate a set of sparse loading vectors that collectively explain a large fraction of the variance in a dataset, while remaining non-redundant. The algorithm supports two definitions of non-redundancy: either orthogonality of the loading vectors or zero pairwise correlation between principal components (PCs). In the reported benchmar...

---

### 44. The Exact Worst-Case Tail Probability under Bounded Kurtosis

**Authors:** Xiaoyu Li, Andi Han, Jiaojiao Jiang, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05226v2) | 📄 [PDF](https://arxiv.org/pdf/2607.05226v2)

**Summary:** We determine exactly what a kurtosis bound buys for one-sided tail control. For the class $\mathcal{C}(κ)$ of real random variables with mean $0$, variance $1$, and fourth moment at most $κ$, the skewness left free, we compute the worst-case tail probability $V_1(t,κ)=\sup_{X\in\mathcal{C}(κ)}\mathbb{P}(X\geq t)$ for every threshold $t>0$ and every $κ\geq 1$. The answer is a four-regime map: a Cantelli tongue $b(κ)\le t\le c(κ)$ on which the two-moment bound $1/(1+t^2)$ remains tight and the kur...

---

### 45. Geometric Causal Models

**Authors:** Eli N. Weinstein, David M. Blei

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05153v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05153v1)

**Summary:** Scientists often seek to draw causal inferences from structured data that is not independently and identically distributed, such as spatial data, network data, or molecular data. We develop geometric causal models (GCMs), a framework for causal inference from dependent data that exploits underlying symmetries of the data generating process. For example, in spatial data, we consider processes that are symmetric under translations, or in graph data, symmetric under permutations of the nodes. We sh...

---

### 46. Functional Bilevel Optimization for Predictive Fairness

**Authors:** Ieva Petrulionyte, Julien Mairal, Michael Arbel

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.05098v1) | 📄 [PDF](https://arxiv.org/pdf/2607.05098v1)

**Summary:** When sensitive attributes are continuous and high-dimensional $-$ demographic score vectors, posteriors over attributes, age or income profiles $-$ enforcing full statistical independence is often too restrictive, and existing relaxations rely on indirect dependence penalties or adversarial schemes that do not directly target the fairness-accuracy trade-off. We instead consider mean demographic parity through DPVar, the variance of the conditional-mean prediction given the sensitive attribute, a...

---

### 47. Geometry-Aware Bayesian Quantification via Compositional Data Analysis

**Authors:** Alejandro Moreo, Pablo González, Juan José del Coz

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04977v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04977v1)

**Summary:** Accurately estimating the unknown target label distribution is the critical first step for adapting to label shift. This task, widely known as quantification or class prevalence estimation, has recently seen significant advances through continuous KDE-based methods which model the density of multiclass classifier posteriors. Posterior vectors might be regarded as compositional data, since they lie on the probability simplex. However, existing KDE-based quantifiers typically rely on Euclidean Gau...

---

### 48. Identification and Bounding of Central Moments of Causal Effects Using Marginal Moments Information

**Authors:** Naoya Hashimoto, Yuta Kawakami, Jin Tian

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04957v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04957v1)

**Summary:** Evaluating the causal effect of a treatment on an outcome is a central objective in causal inference. While the average causal effect summarizes the mean impact of treatment, the central moments of the individual causal effect (ICE) characterize the shape of the ICE distribution, thereby revealing the extent and structure of treatment effect heterogeneity across individuals. This paper investigates the identification and bounding of the central moments of the ICE using only the marginal central ...

---

### 49. On the Complexity of Entrywise Power Matrix Factorization

**Authors:** Nicolas Gillis, Subhayan Saha, Stefano Sicilia, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04875v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04875v1)

**Summary:** Given a nonnegative matrix $X$, a factorization rank $r$ and a real parameter $p$, entrywise power matrix factorization (EPMF) looks for a low-rank matrix $X_r$ such that $X = |X_r|^{\circ p}$ (exact case) or $X \approx |X_r|^{\circ p}$ (approximate case), where $(\cdot)^{\circ p}$ denotes the component-wise exponent. EPMF includes the modulus model ($p=1$) and component-wise square factorization ($p=2$) as special cases, the latter being closely related to the square root rank. We analyze the c...

---

### 50. Active Learning on Adversarially Corrupted Graphs

**Authors:** Marco Bressan, Nicolò Cesa-Bianchi, Tommaso d`Orsi, et al.

**Published:** 2026-07-06

🔗 [Paper](http://arxiv.org/abs/2607.04869v1) | 📄 [PDF](https://arxiv.org/pdf/2607.04869v1)

**Summary:** Motivated by real-world scenarios where malicious entities tamper with existing networks, we define a model where an adversary seeks to hide a set of \emph{corrupted vertices} inside a graph $G^*$. To this end, the adversary can add edges between the corrupted vertices, as well as edges between the corrupted vertices and $G^*$, and its power is then measured by the size of the \emph{neighborhood} of the corrupted vertices in $G^*$. Our goal is to design an active learning algorithm that efficien...

---

