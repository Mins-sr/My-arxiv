# arXiv Daily Digest - 2026-11-09

Total papers: 350

---

## cs.AI

**50 papers**

### 1. On Agentic Manipulation Policies

**Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09892v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09892v1)

**Summary:** Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged ...

---

### 2. CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse

**Authors:** Peter Belcak, Greg Heinrich, Saurav Muralidharan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09891v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09891v1)

**Summary:** Large language models reinvent the wheel all the time. They conflate task-solving with the execution of the solutions, which forces them to solve every problem from scratch. We show that once a task has been reasoned through, the application of its solution to a new problem instance can be done very efficiently and with little involvement from language models. We introduce agentic reasoning caching, a method for constructing robust CPU-executable agentic reasoning caches (ARCs) from LLM reasonin...

---

### 3. On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning

**Authors:** Haoyu Wang, Ru Wang, Yuanyuan Wang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09872v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09872v1)

**Summary:** Test-time reinforcement learning (TTRL) adapts pretrained language models to unlabeled target-domain data using self-generated pseudo-labels, whose reliability remains poorly understood. We analyze majority-vote supervision for TTRL with online Direct Preference Optimization (DPO) and decompose its error into population-majority bias and prompt-dependent finite-rollout variation. Because population-majority bias is generally unidentifiable without external supervision, we focus on mitigating the...

---

### 4. GRAC: Graph-Based Retrieval-Augmented Captioning for Surgical Scene Description

**Authors:** Rochak Dhakal, Chen Zhao, Soup Cobb, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09866v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09866v1)

**Summary:** Purpose: Surgical operative reports support procedural documentation, surgical training, performance assessment, and workflow review. However, extracting meaningful information often requires extensive manual review and clinical expertise. Automated surgical scene descriptions could reduce this burden by leveraging recurring surgical activities and prior knowledge.   Methods: We propose GRAC (Graph-Based Retrieval-Augmented Captioning), a framework that represents surgical scenes as graphs captu...

---

### 5. Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation

**Authors:** Xun Tu, Minghao Zou, Karthik Desingh

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09864v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09864v1)

**Summary:** Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons, is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation. Despite recent progress, reliably executing these tasks remains challenging because performance depends on complex robot-object and object-environment interaction dynamics. Existing approaches address this challenge either through model-based methods, which often re...

---

### 6. Flow-Guided Target-Space Alignment via Path Consistency

**Authors:** Ruizhi Yuan, Zeqiu Yu, Wei Gao, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09863v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09863v1)

**Summary:** Many multimodal alignment problems require mapping a source modality into a fixed space defined by a target modality, where the target space is not merely an intermediate embedding but is used directly for downstream analysis. In this setting, successful alignment should preserve both the global structure of the target distribution and the instance-level correspondence observed in paired source--target training data. Existing objectives typically address only part of this goal: contrastive losse...

---

### 7. Ensemble Methodology for Reference-Free Confidence Estimation in LLM-based Code Summarization

**Authors:** Marco Colombo, Balaji A Jayaram, Sowmyakumari Selvaraj, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09846v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09846v1)

**Summary:** This paper describes an approach and use case to estimate the correctness of LLM-generated COBOL summaries without access to human-authored references. The core intuition is that inter-model agreement on semantics is informative about truth, and that an LLM-as-judge can provide higher-fidelity pairwise assessments than traditional string- or embedding-based metrics. We operationalise this intuition with (i) controlled summary generation from diverse models; (ii) a LLM evaluator that compares pai...

---

### 8. Can Agentic Systems Close the Gap in Radiology with Production AI Tools?

**Authors:** Aubin Charley, Julien Khlaut, Charles Corbière, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09836v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09836v1)

**Summary:** Radiology AI has developed along two paths: specialized models that perform well on narrow tasks but cover few clinical findings, and generalist models that address a broader range of tasks but remain prone to hallucination and inaccurate measurements. Combining the two through agentic systems offers a route towards comprehensive radiology reporting, but published systems are tied to one modality or body part. We describe a radiology agentic framework that standardizes how an orchestrator calls ...

---

### 9. BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design

**Authors:** Dayou Du, Woon Yee Ng, Guangming Sheng, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09825v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09825v1)

**Summary:** The key-value (KV) cache dominates memory capacity and bandwidth in long-context LLM serving. While 4-bit microscaling formats (NVFP4, MXFP4) shrink the cache and run attention on FP4 Tensor Cores, a fundamental gap remains between algorithmic quantization and system-aware acceleration: existing FP4 KV systems use vanilla quantization that causes severe accuracy drops, whereas accuracy-oriented 4-bit algorithms rely on vector codebooks whose lookup overhead degrades decoding throughput. We prese...

---

### 10. Discovering formally verified quantum programs with AI

**Authors:** Sergey Shirobokov, Ben Jaderberg, Katerina Hristova, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09822v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09822v1)

**Summary:** The timeline by which quantum computers can solve breakthrough problems in science depends on improved quantum algorithms as much as on better hardware. Such algorithmic advances are typically achieved through many years of expert human collaboration. In mathematics and computer science, large language models have accelerated progress through automated discovery loops. However, quantum algorithms can only be evaluated by classical computers on restricted or small instances. Here we demonstrate a...

---

### 11. Generative Latent Priors for Interpreting and Steering Protein Language Models

**Authors:** Daniel Hinjos, Lucía Urcelay

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09818v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09818v1)

**Summary:** Dominant methods for interpreting large models impose strong structural assumptions. Generative Latent Priors (GLP) are a complementary approach: a diffusion model that learns the distribution of a frozen model's activations directly, imposing no assumptions. We port GLP to ESM-2 activations (UniRef50) and evaluate it at two host scales (ESM-2-8M and -650M), both as a lens for protein representations and as a prior for editing them. Generation quality scales smoothly with depth and compute. As a...

---

### 12. Scaling Graph Similarity Learning with Graph Neural Networks

**Authors:** Ahmet Tüzen, Helge Langseth, Kjetil Nørvåg

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09805v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09805v1)

**Summary:** Graph similarity computation is an important task in graph mining with many real-world applications, such as chemical compound analysis, program dependence comparison, and social network analysis. The problem is computationally challenging: Graph Edit Distance (GED) and Maximum Common Subgraph (MCS), which quantify the distance between graphs and identify their largest shared subgraph, respectively, are NP-hard to compute exactly. To address these computational challenges, Graph Neural Networks ...

---

### 13. When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents

**Authors:** Tural Mehtiyev, Biruk Tadesse, Lawrence Arkoh, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09802v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09802v1)

**Summary:** LLM-based coding agents such as Claude Code are guided by repository instruction files (also called context files or agent configuration files) like AGENTS.md and CLAUDE.md, which are read in every agent session. As any documentation artifact, these files can fall behind the code and become stale (e.g., a test folder moves, but the file still points to the old one). In technical debt terms, such a stale instruction is documentation debt, and its interest is the cost it adds to every later agent ...

---

### 14. Maya a1: Do the Options Read the Model, or Does Their Position? Order Sensitivity in a Non-Autoregressive Decision Model

**Authors:** Mohammed Nayeem Khan, Logesh L

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09803v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09803v1)

**Summary:** Laya answers typed multiple-choice questions in one forward pass by scoring a hidden state at one [MASK] marker per option. We re-engineer the checkpoint (421M parameters; a 2-layer option head with no positional tensor; a documented but unused parallel layout) and test whether the answer depends on where an option is listed. Presenting 951 Qwen-verified questions under every cyclic rotation of their options (or six random permutations for 12 options), the released checkpoint changes its answer ...

---

### 15. Test-Time Compute Scales Better with Parallel Agent Teams

**Authors:** Junlin Wang, Haozhe Chen, Ang Li, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09798v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09798v1)

**Summary:** Test-time scaling improves the performance of a fixed model by spending more computation at inference. There are two common ways to spend it on agents when a verifier can score every attempt. Best-of-N sampling runs many independent agents and keeps the best result but saturates quickly. One large team of collaborating agents can score higher but stops improving as it grows. Can we get the best of both? Our method, parallel agent teams, does so by sampling many small teams in parallel and keepin...

---

### 16. Knowing When to Intervene: Causal Evaluation of AI Agents

**Authors:** Ayush Sawarni, Wenqian Xing, Tijana Zrnic, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09792v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09792v1)

**Summary:** Current evaluations of agentic AI systems primarily rely on benchmarks. However, the static nature of benchmarks makes them uninformative about the value of auditing interventions at deployment time. For reliable deployment, we often need to determine within an agent's trajectory whether or not to intervene, e.g., by verifying the agent's current output or steering it toward different behavior, using either human review or more costly models or time-consuming agentic supervision. The value of su...

---

### 17. Assessing the Impact of Retrieval-Augmented Generation on Algorithmic Problem-Solving

**Authors:** Gabriel Souza Baggio, Gabriel Machado Lunardi, Guilherme Medeiros Machado, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09791v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09791v1)

**Summary:** Competitive programming problems pose distinctive challenges for Large Language Models, as they demand not only proficient code generation but also advanced algorithmic reasoning. This study presents a Retrieval-Augmented Generation approach specifically designed to enhance the capacity of Large Language Models to address such problems. Our approach integrates an embedding-based retrieval mechanism and a similarity search algorithm to identify analogous problems within a knowledge database, empl...

---

### 18. ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models

**Authors:** Lingyun Song, Ziyao Chen, Kang Pan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09770v1)

**Summary:** Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{S}ubspace navigation framework for lifelong knowledge \textbf{E}diting. ROSE addr...

---

### 19. Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents

**Authors:** Yuchen Li, Lisa Liu, Runqi Zou, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09768v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09768v1)

**Summary:** Large language model (LLM) agents coordinate through conversation, and the same message can be phrased in simpler or more complex language, bluntly or politely. We test whether such differences change how other agents judge and act, using the LURK Werewolf framework, which separates each utterance's speech-act predicate from its natural-language realization. We rewrite only the realization, check that the game content is preserved, and replay each game day from saved checkpoints against a re-sam...

---

### 20. Continuous wavelet-based feature extraction for laser-induced breakdown spectroscopy classification of human plasma samples

**Authors:** Md Mahmudur Rahman, Atqiya Munawara Mahi, Nazim Ahmed Belabbaci, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09746v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09746v1)

**Summary:** Extracting discriminative features from laser-induced breakdown spectroscopy (LIBS) spectra is important for the classification of complex biological samples. This study evaluates continuous wavelet transform (CWT)-based spectral peak extraction for distinguishing human plasma samples labeled as SARS-CoV-2-positive or negative. Plasma specimens from 181 individuals, comprising 53 positive samples and 128 negative controls, were deposited as 5 μL droplets on silicon substrates and dried before an...

---

### 21. Safety Is $Π_1$, Provability Is $Σ_1$: One Framework for the Hugging Face Breach and OpenAI's Mathematical Proofs

**Authors:** Jinho Kang, Jinsook Kim

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09736v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09736v1)

**Summary:** OpenAI's agents breached Hugging Face in July 2026, and the same company released more than seven hundred AI-generated manuscripts of mathematical proofs in October 2026. The first event is read as a failure in security, while the second is read as a success in mathematics. We read both through the hybrid framework of our paper (Kim and Kang, 2026, arXiv:2611.01914), in which coding, proving, and learning from data are derivations by one and the same deductive mechanism, distinguished by the kin...

---

### 22. What to Delegate, What to Preserve: Human Preferences for Agentic AI Across Everyday Life and Work

**Authors:** Sarah Wheeler, Veronica Rammouz, Yaoyao Qian, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09730v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09730v1)

**Summary:** AI agents can execute multi-step tasks on users' behalf, yet the boundaries of acceptable delegation remain unclear. We report a scenario-based survey of 289 U.S. adults with prior AI experience covering 45 use cases across nine life domains. Each respondent evaluated one scenario per domain, producing repeated measures of automation preference, trust, collaboration, AI leadership, privacy concern, and willingness to pay. Automation preferences varied substantially across domains. Generalized es...

---

### 23. FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding

**Authors:** Donglin Zhuang, Pragaash Ponnusamy, Xiaoxia Wu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09722v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09722v1)

**Summary:** Large-language-model decode attention streams the key-value (KV) cache for every generated token. Packing that cache into 2-bit or 4-bit quantized integers reduces memory traffic but does not automatically translate into latency saving. Existing 2-bit fused kernels reach under 31%/15% of peak HBM throughput on H100/B200. Converting each value and applying its scale and offset before feeding Tensor Cores is a major bottleneck because instruction-issue throughput is scarce on modern GPUs. Instead ...

---

### 24. MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory

**Authors:** David H. Yang, Blake Bullwinkel, Amanda Minnich, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09721v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09721v1)

**Summary:** LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning a...

---

### 25. Intent-Aware Caching for Efficient LLM Serving

**Authors:** Kazi Hasan Ibn Arif, JinYi Yoon, Dimitrios S. Nikolopoulos, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09715v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09715v1)

**Summary:** Modern LLM serving systems use prefix caching to accelerate multi-turn conversational workloads. They cache the key-value states of previous conversation prefixes and reuse them when subsequent requests share the same prefix, to avoid redundant prefill computation and reduce serving latency. However, achieving a high cache hit rate remains challenging because cache reuse depends on whether a conversation continues and how soon the next turn arrives. Our analysis of real workloads shows that user...

---

### 26. ICare-DT: a digital twin for continuous forecasting of intensive care patients

**Authors:** Yanke Li, Yahang Qi, Yumi Kim, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09712v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09712v1)

**Summary:** Digital twins of intensive care patients should update forecasts from new data and predict treatment responses, but few studies test whether routine records support either. We propose ICare-DT, a Transformer-based twin that updates a latent patient state hourly from new measurements without retraining. We trained it on 140,473 eICU-CRD stays to forecast vital signs crossing their training-set means. On test data, later forecasts beat the twin's own hour-6 forecasts of the same windows in all 12 ...

---

### 27. Empirical Assessment of Post-Quantum Cryptography Adoption Status in TLS

**Authors:** Md Ariful Haque, Sander Vinberg, Ben Edwards, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09707v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09707v1)

**Summary:** Anticipating Q-day security concerns, major CDNs and cloud providers are migrating to post-quantum cryptography (PQC). While existing literature benchmarks PQC performance, empirical research evaluating real-world adoption data remains scarce. We present an empirical assessment of PQC deployment across seven critical protocols (HTTPS, LDAPS, SMTPS, IMAP-SSL, POP3-SSL, TELNETS, and RDP) using 10,000 target IP addresses per protocol. At the origin-server level, PQC algorithm support reaches 9.1% f...

---

### 28. Empirical Study of Post-Quantum Cryptography Adoption Status in SSH Infrastructure

**Authors:** Md Ariful Haque, Sander Vinberg, Ben Edwards, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09703v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09703v1)

**Summary:** With the anticipated arrival of Q-day, quantum computers threaten current cryptographic schemes for encryption and digital signatures. In response, major content delivery networks and cloud service providers are already adopting Post-Quantum Cryptography (PQC). The current state-of-the-art focuses on benchmarking the operational performance of implementing PQC, but the real-world adoption status remains under-researched. This work utilizes large-scale SSH fingerprint data from a proprietary scan...

---

### 29. Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure

**Authors:** Wajih Hassan Raza, Ahsan Bilal, Yidan Shen, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09700v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09700v1)

**Summary:** Attention is a major scalability bottleneck in large language models (LLMs), with its computational cost and key-value (KV) memory traffic becoming increasingly prohibitive as context length grows. Sparse attention addresses this bottleneck by restricting each query to a subset of the context, but its effectiveness hinges on identifying relevant regions both cheaply and reliably. Existing training-free methods primarily rely on runtime relevance estimates, with selection dimensionality and granu...

---

### 30. Verifier Noise Is a Temperature: Testing Tilt Predictions in Finite-Budget LLM-Guided Search

**Authors:** Xiaomeng Li

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09699v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09699v1)

**Summary:** LLM-guided search loops propose a modified candidate, score it, and keep it if it scores better. When both candidates are re-scored at every comparison, as in the minibatch acceptance gates of prompt optimizers, keep-if-better is a reversible Markov chain if the score difference is logistic and the mutation operator is reversible, and its stationary law is the mutation equilibrium tilted by exp(beta f). For any continuous symmetric noise difference the same tilt is the stationary law of a small-...

---

### 31. SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning

**Authors:** Jingye Zhang, Choo Sin Wai, Dake Zhong, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09684v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09684v1)

**Summary:** Vision-language-action (VLA) policies have become a promising paradigm for end-to-end robot control, but their effectiveness still depends heavily on large volumes of demonstration data. In manipulation tasks, this dependence is compounded by structured spatiotemporal uncertainty in the action space: multiple nearby actions or trajectories may successfully solve the same task, while semantically equivalent demonstrations often unfold at different speeds. Standard pointwise supervision treats eac...

---

### 32. Goodhart in the Planner: Sampling-Based Control Exploits Rewards Learned from Human Preferences

**Authors:** Soovadeep Bakshi, Apurba Bose

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09670v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09670v1)

**Summary:** Robots increasingly choose actions by searching against a reward model learned from human preferences, in model-predictive control or best-of-$N$ selection; we measure what this does to the true objective. On HalfCheetah and Hopper with crowd-sourced labels, and on Meta-World drawer-open and plate-slide with synthetic labels and blind labels from the two authors, harder MPPI search cuts true return by up to 76%: with human labels the drawer opens in 0 of 20 runs against 10 of 10 for the cloned p...

---

### 33. How Much Conversation History Does an AI Agent Need?

**Authors:** Danny Kim, Fernando Koch

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09662v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09662v1)

**Summary:** How does using less conversational history change reader-token use and benchmark scores? We examine this question on 1,100 BEAM questions. We held the retrieval ranking and reader constant across five fixed passage budgets, and mean assigned scores rose as the passage budget grew. The score gain per additional token became smaller at the upper tested budgets. Answerable questions generally received higher scores with more context. Pooled abstention scores sometimes rose as the passage budget shr...

---

### 34. Differentially Private GraphRAG: Protecting Relation Connectivity and Semantics

**Authors:** Jie Fu, Yuan Hong, Yue Ning, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09658v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09658v1)

**Summary:** Graph Retrieval-Augmented Generation (GraphRAG) connects information across documents through entity relationships to support relational reasoning. However, black-box access to GraphRAG systems can enable adversaries to reconstruct knowledge graphs and recover both structural connectivity between entities and the semantics of their relationships. Existing defenses lack formal privacy guarantees and provide limited protection against such reconstruction attacks. We propose RelGuard, the first dif...

---

### 35. Breaking the Privacy Promise: Gradient Inversion Attacks on Federated Low-Rank Adapted Vision Transformers

**Authors:** Ritik K. Badiya, Siladittya Manna, Ashmit Sinha, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09652v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09652v1)

**Summary:** Parameter-efficient fine-tuning (PEFT) has been increasingly adopted to fine-tune pretrained models with low computational cost and is therefore also preferred in the federated learning paradigm to reduce computational and communication overhead. In this work, we investigate the sparsely explored problem of the risk of private data leakage in LoRA-adapted Vision Transformers (ViTs), where low-rank updates weaken the gradient signal available to a server with access to individual client updates. ...

---

### 36. Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters

**Authors:** Constantinos Karouzos, Nikolaos Aletras

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09634v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09634v1)

**Summary:** Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector select...

---

### 37. Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning

**Authors:** Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09625v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09625v1)

**Summary:** Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term memory and planning. In this work, we address the problem of long-term memory in MBRL by moving beyond the commonly studied paradigm of architecture design. We introduce Test-Time Model-B...

---

### 38. Not Your Diary, Just Your Topic: Grading the Wrong-User Control

**Authors:** Karina Romanova, Igor Kiselev, Vladimir Platonov, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09609v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09609v1)

**Summary:** A common test of personalization replaces a user's history with someone else's and measures the drop in accuracy. But this swap also changes the topics in the history, so the drop may reflect topic mismatch. We examine this problem with a frozen language model on LaMP-2 news categorization, using histories from similar users and synthetic histories assembled from other users' articles. The user's own history improves accuracy by 2.3 percentage points over a model trained without history. Removin...

---

### 39. Alignment by Confident Debate: Preference Learning from Multi-Agent Debate

**Authors:** Nikhil Verma, Dingxian Wang, Mohammad Reza Rezaei, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09568v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09568v1)

**Summary:** Post-training language models for reasoning typically rely on gold answers, task-specific verifiers, or learned reward models, limiting scalability when such signals are scarce. Multi-agent debate offers a self-supervised alternative, but converting debate into reliable training supervision remains challenging: majority voting weights agreeing responses equally, lacks a principled tie-breaking rule, and is ill-defined for open-ended tasks without a canonical answer; likelihood-based scoring can ...

---

### 40. Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs

**Authors:** Peiyu Zhang, Heng Ping, Shinibali Bhattacharyya, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09554v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09554v1)

**Summary:** Long-context language models often neglect information in the middle of the input, a phenomenon known as "lost-in-the-middle". Part of this gap may stem from the long-range decay of rotary position embedding (RoPE), which weakens the positional signal between distant tokens. Existing input compression deletes low-importance tokens, and attention reweighting acts only after RoPE has weakened this signal. RoPE-level methods modify positions directly but apply the same remapping to every query. To ...

---

### 41. CoMoFlow: Controllable Protein Conformational Ensemble Generation via Explicit Collective-Mode Modeling

**Authors:** Yusong Wang, Zheyuan Gu, Ailiang Lin, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09548v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09548v1)

**Summary:** Protein conformational ensemble generation aims to efficiently characterize the structural variations accessible to a protein beyond a single static structure. Recent flow-based methods efficiently generate conformational ensembles, but they model coordinated structural variation implicitly, which can limit ensemble fidelity and hinder direct control. To address this limitation, we propose CoMoFlow, a controllable framework for generating protein backbone conformational ensembles by explicitly m...

---

### 42. CID: Measuring Cognitive Work Through Semantic State Change

**Authors:** Ron Fulbright

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09542v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09542v1)

**Summary:** Traditional information theory provides powerful tools for analyzing statistical properties of information but offers limited insight into meaning and semantic transformation. It has never been possible to quantify the meaning of an arbitrary piece of information. Large language models represent information as vectors embedded within high-dimensional semantic spaces, enabling meaning to be analyzed geometrically. This paper defines semantic state as the vector representation of information withi...

---

### 43. Multimodal Training with Knowledge Traction for Video Anomaly Detection

**Authors:** Xiao Tan

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09536v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09536v1)

**Summary:** The task of weakly supervised video anomaly detection is challenging. Existing approaches mainly model video frame features and determine whether anomalies are present based on their magnitudes. In this work, we propose a novel method that incorporates external knowledge into training to improve model performance, robustness, and generalization. We leverage textual prompts and a large language model (LLM) to establish prior information for the specific task, and employ dictionary learning to nor...

---

### 44. PreForceVision: Physics-Guided Optical Estimation of Bolt Preload from Bolt-Head Deformation

**Authors:** Nehal Afifi, Klaus Rappenecker, Florian Peinhardt, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09529v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09529v1)

**Summary:** Bolt preload is a decisive functional quantity in bolted joints because it determines whether external loads are transmitted primarily through frictional clamping or directly through the bolt. Existing preload measurement techniques, including strain-gauge bolts, force washers, ultrasonic methods, and bolt-length measurements, are effective in certain applications but require additional hardware, coupling, calibration, or joint modifications. This limits their scalability for large numbers of st...

---

### 45. StockASkill: A Local-First AgentSkill for Intelligent Stock Selection

**Authors:** Xiangjing An, Zhibin Jiao, Aiting Chen

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09528v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09528v1)

**Summary:** Quantitative equity selection and portfolio construction in emerging and cross-border markets frequently suffer from computational bottlenecks, remote API fragility, survivorship bias, and rigid execution constraints such as discrete board lots and investor-mandated drawdown limits. In this paper, we present StockASkill, a local-first, full-data-driven AgentSkill engineered as a specialized Quant Co-Processor for autonomous AI agents and quantitative researchers. Tailored for agile portfolios (1...

---

### 46. Atik: A Shared-Mesh Transformer Accelerator for RISC-V

**Authors:** Ahmed Zeer, Erkan Uslu

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09522v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09522v1)

**Summary:** Transformer inference repeatedly invokes dense matrix multiplication and attention, including its data-dependent softmax normalization. We present Atik, an open-source RoCC accelerator for RocketChip that executes matrix multiplication and dense attention through one shared fixed-point MAC mesh. Atik accepts and returns BF16 tensors, uses a streaming online-softmax schedule that never materializes the full score matrix, and is invoked through a small descriptor-based ABI. We evaluate three meshe...

---

### 47. Active Learning of Robust Models

**Authors:** Mizu Nishikawa-Toomey, Andreas Kirsch, Laurent Charlin, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09520v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09520v1)

**Summary:** In many domains from species identification to cancer diagnosis, labelling data to train predictive models remains costly. In these settings, it is advantageous to intelligently select data points to label to achieve the maximum information gain, this is the motivation behind the study of active learning. In addition to the high costs of acquiring data in such domains, there is the added complexity of data distribution shifts that can occur between training and deployment. For example, the featu...

---

### 48. A Physics-Informed Learning Framework for Linking Microscopic Surface Degradation to Bolted Joint Functional Behavior

**Authors:** Nehal Afifi, Gerhard Kachel, Sven Matthiesen

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09514v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09514v1)

**Summary:** Returned products in circular engineering often have heterogeneous degradation histories, making remaining function difficult to assess. For bolted joints, corrosion alters surface morphology, contact, friction, preload retention, and mechanical response. This paper presents a physics-informed multimodal framework for linking microscopic and camera-based degradation observations to functional indicators of corroded bolted joints. The workflow defines the corrosion failure mode, generates synchro...

---

### 49. V-STORM: A Structure-Aware Grounded Chain of Thought Dataset for Faithful and Fine-Grained Spatio-Temporal Video Reasoning

**Authors:** Dian Jiao, Yuqian Yuan, Jiaqi Zhu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09511v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09511v1)

**Summary:** While MLLMs can often identify what happens in a video, they still struggle with fine-grained spatio-temporal reasoning, which requires precise grounding when and where the supporting evidence appears and composing such evidence into a coherent reasoning chain. This challenge is exacerbated by the lack of scalable data construction and evaluation pipelines that provide granular, verifiable supervision linking reasoning steps to explicit spatio-temporal evidence.To address this gap, we present V-...

---

### 50. BEiTScore++: Reference-free Image Captioning Evaluation with BEiT-3 and Conformalized Quantile Regression

**Authors:** Gonçalo Gomes, Bruno Martins, Chrysoula Zerva

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09505v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09505v1)

**Summary:** Reliable uncertainty estimation is important for deploying evaluation metrics in real-world settings, where both input ambiguity and domain shifts are common. In this work, we propose an uncertainty-aware extension of the BEiTScore image captioning metric, producing conformally calibrated confidence intervals alongside alignment scores. Our approach models predictive distributions over human judgments, enabling both accurate scoring and principled uncertainty quantification in a single forward p...

---

## cs.CL

**50 papers**

### 1. CodeQuant2: Enhanced Outlier Mitigation and Adaptive Clustering for Low-Precision LRMs

**Authors:** Xingyu Liu, Xiangyang Yin, Tianhua Xia, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09868v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09868v1)

**Summary:** Large reasoning models (LRMs) improve task performance by generating longer intermediate reasoning traces, but this substantially increases inference costs and makes low-precision quantization increasingly important. However, aggressively quantized models often perform poorly on reasoning tasks. We observe larger activation fluctuations during the first decoding steps of reasoning. Calibration that omits these early states may miss their activation fluctuations. To address these reasoning-specif...

---

### 2. How far does a hash-only sender go? A pre-registered map of sender memory versus bits for short text messages

**Authors:** Marcelo Samoilenko

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09848v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09848v1)

**Summary:** Can a sender that only computes hashes, with a language model only at the receiver, transmit short human text more cheaply than a classical sender trained on the same domain? We answer with one pre-registered run on 1,000 English user utterances from Taskmaster-1. The primary endpoint is the cost per message to deliver 100% of the messages (hash bits, plus a 2-byte negative acknowledgement and the raw text when the first attempt fails), paired against an in-domain PPM order-1 sender. The hash-on...

---

### 3. BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design

**Authors:** Dayou Du, Woon Yee Ng, Guangming Sheng, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09825v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09825v1)

**Summary:** The key-value (KV) cache dominates memory capacity and bandwidth in long-context LLM serving. While 4-bit microscaling formats (NVFP4, MXFP4) shrink the cache and run attention on FP4 Tensor Cores, a fundamental gap remains between algorithmic quantization and system-aware acceleration: existing FP4 KV systems use vanilla quantization that causes severe accuracy drops, whereas accuracy-oriented 4-bit algorithms rely on vector codebooks whose lookup overhead degrades decoding throughput. We prese...

---

### 4. Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation

**Authors:** Osamudiamen Edogun, Joshua Obigwe, Irfan Mehmood

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09807v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09807v1)

**Summary:** A conversational agent that remembers has to decide what to keep. Retrieval-augmented generation keeps the transcript and searches it; the alternative is to compact each turn into atomic facts and search those. We compare the two on LoCoMo, with both arms answering all 1,985 questions in one window, against the same stores, with the same generator and judge, and both predictions on one row, which licenses McNemar's exact test on the 512 questions where they disagree.   On the four categories com...

---

### 5. Maya a1: Do the Options Read the Model, or Does Their Position? Order Sensitivity in a Non-Autoregressive Decision Model

**Authors:** Mohammed Nayeem Khan, Logesh L

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09803v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09803v1)

**Summary:** Laya answers typed multiple-choice questions in one forward pass by scoring a hidden state at one [MASK] marker per option. We re-engineer the checkpoint (421M parameters; a 2-layer option head with no positional tensor; a documented but unused parallel layout) and test whether the answer depends on where an option is listed. Presenting 951 Qwen-verified questions under every cyclic rotation of their options (or six random permutations for 12 options), the released checkpoint changes its answer ...

---

### 6. Are These Programmers Ripe Enough to Eat? Evaluating How LLMs Handle Lexical Knowledge Conflicts in Translation

**Authors:** Dongxu Wu, Sara Court, Micha Elsner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09785v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09785v1)

**Summary:** External lexical resources can help large language models (LLMs) translate texts in low-resource languages and specialized domains, but these resources may conflict with models' prior lexical knowledge. To isolate this conflict, we construct a controlled Mandarin-to-English translation task in which familiar source words are assigned new meanings within and across semantic categories. We treat these prompt-supplied meanings as contextual knowledge (CK) and systematically evaluate the effects of ...

---

### 7. ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models

**Authors:** Lingyun Song, Ziyao Chen, Kang Pan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09770v1)

**Summary:** Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{S}ubspace navigation framework for lifelong knowledge \textbf{E}diting. ROSE addr...

---

### 8. Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents

**Authors:** Yuchen Li, Lisa Liu, Runqi Zou, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09768v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09768v1)

**Summary:** Large language model (LLM) agents coordinate through conversation, and the same message can be phrased in simpler or more complex language, bluntly or politely. We test whether such differences change how other agents judge and act, using the LURK Werewolf framework, which separates each utterance's speech-act predicate from its natural-language realization. We rewrite only the realization, check that the game content is preserved, and replay each game day from saved checkpoints against a re-sam...

---

### 9. MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory

**Authors:** David H. Yang, Blake Bullwinkel, Amanda Minnich, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09721v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09721v1)

**Summary:** LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning a...

---

### 10. RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill

**Authors:** Dylan Johnston, Robert P. Smith

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09709v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09709v1)

**Summary:** RidgeFill shortens prefill by not computing most of a model's upper layers for the prompt. The lower layers run exactly up to a split; from the split layer's state a per-layer map predicts every later layer's input, and each late layer writes its cache from that prediction. The design follows YOCO and DeepSeek-V4.1-Flash, where the projection is trained into the model. RidgeFill retrofits it onto models that were never trained for it: the map is a ridge regression fitted once in closed form from...

---

### 11. How Much Conversation History Does an AI Agent Need?

**Authors:** Danny Kim, Fernando Koch

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09662v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09662v1)

**Summary:** How does using less conversational history change reader-token use and benchmark scores? We examine this question on 1,100 BEAM questions. We held the retrieval ranking and reader constant across five fixed passage budgets, and mean assigned scores rose as the passage budget grew. The score gain per additional token became smaller at the upper tested budgets. Answerable questions generally received higher scores with more context. Pooled abstention scores sometimes rose as the passage budget shr...

---

### 12. Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters

**Authors:** Constantinos Karouzos, Nikolaos Aletras

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09634v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09634v1)

**Summary:** Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector select...

---

### 13. RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers

**Authors:** Yijun Li, Zhengxi Lu, Zhipiao Liu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09597v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09597v1)

**Summary:** Rubric-based reinforcement learning (RL) extends RL with verifiable rewards to open-ended tasks by scoring each response against query-specific rubrics. Under group-relative optimization, however, a rubric that every sampled response fails (unreachable) or passes (saturated) gives all responses the same outcome and no learning signal; in Qwen3-4B medical training, 60.88% of query-rubric observations are inactive. We find that the two states lack different supervision: stating an unreachable rubr...

---

### 14. Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs

**Authors:** Peiyu Zhang, Heng Ping, Shinibali Bhattacharyya, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09554v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09554v1)

**Summary:** Long-context language models often neglect information in the middle of the input, a phenomenon known as "lost-in-the-middle". Part of this gap may stem from the long-range decay of rotary position embedding (RoPE), which weakens the positional signal between distant tokens. Existing input compression deletes low-importance tokens, and attention reweighting acts only after RoPE has weakened this signal. RoPE-level methods modify positions directly but apply the same remapping to every query. To ...

---

### 15. Benchmarking Speaker Embedders in the Sub-Second Regime for Real-Time Voice AI Agents

**Authors:** Abhishek Gautam

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09516v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09516v1)

**Summary:** Real-time Voice AI agents must separate the active user from intelligible background speech that survives conventional noise suppression. Background sources include television audio, family members, and colleagues. Production denoisers remove non-stationary environmental noise effectively. Background speech shares the spectral characteristics of the target and passes through, causing false acceptances in downstream speaker verification (SV) and automatic speech recognition (ASR). We benchmark op...

---

### 16. On the Effectiveness and Limitations of Open-Weight LLMs for Low-Resource Offensive Language Detection in Danish

**Authors:** Elnur Adl Zarabi, Amit Kumar, Adi Singh, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09506v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09506v1)

**Summary:** We study the effectiveness and robustness of open-weight large language models (LLMs) for Danish offensive language detection, an underexplored low-resource task. We evaluate four model families (Llama, Mistral, Gemma, and Qwen) across eleven prompting strategies spanning five design categories, cross-prompt generalization, Danish orthographic variation, and robustness under balanced and naturally imbalanced class distributions. We compare against three BERT-family baselines with distinct pre-tr...

---

### 17. BEiTScore++: Reference-free Image Captioning Evaluation with BEiT-3 and Conformalized Quantile Regression

**Authors:** Gonçalo Gomes, Bruno Martins, Chrysoula Zerva

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09505v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09505v1)

**Summary:** Reliable uncertainty estimation is important for deploying evaluation metrics in real-world settings, where both input ambiguity and domain shifts are common. In this work, we propose an uncertainty-aware extension of the BEiTScore image captioning metric, producing conformally calibrated confidence intervals alongside alignment scores. Our approach models predictive distributions over human judgments, enabling both accurate scoring and principled uncertainty quantification in a single forward p...

---

### 18. An Effective Spoken Language Understanding Approach Leveraging Query-Adaptive Intent Detection

**Authors:** Bing-Long Kuo, Yu-Hsuan Fang, Tien-Hong Lo, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09491v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09491v1)

**Summary:** Large language models enable fine-tuning-free spoken language understanding (SLU) through in-context learning, but direct query-based retrieval may select semantically similar yet intent irrelevant demonstrations. This paper presents Query-Adaptive Intent Detection via Prototype Extraction (APEX), a two-stage retrieval framework that first selects candidate intents using intent-level prototypes and then retrieves contextual exemplars within the selected intent space. Experiments on the SLURP dat...

---

### 19. From LoRA to Language: Recovering Skill Documents from Adapters

**Authors:** Saranya Dintakurthy Swadha, Pavan C Shekar, Arpit Jain, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09454v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09454v1)

**Summary:** Agent skills are short documents that teach a language model how to handle a class of tasks. To save context, these documents are increasingly compiled into low-rank adapters (LoRA), which keep the behaviour but lose the text: an adapter is hard to read, edit, audit or move to another model. We ask whether the skill document can be written back from the adapter and its frozen base model, and we score each recovered document by the share of the original's key instructions it states and by the tas...

---

### 20. A Spiking Neural Model of the Mental Lexicon: Representations, Similarity Structure, and Associative Retrieval in Perception and Production

**Authors:** Bernd J. Kröger

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09402v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09402v1)

**Summary:** A neural account of lexical access requires an explicit distinction between the structure of lexical representations, the associations linking representational levels, and the activity generated during retrieval. This paper specifies a spiking neural implementation of the mental lexicon within the Neural Engineering Framework and Semantic Pointer Architecture. Conceptual and phonological form representations are constructed recursively from relational graphs, whereas lemma representations provid...

---

### 21. Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data

**Authors:** Carlos Martín-Abellán, Mark Kröll

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09372v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09372v1)

**Summary:** Energy management officers and grid operators increasingly rely on smart meter data for anomaly detection, performance monitoring, and strategic decision-making. However, extracting actionable insights from large-scale, heterogeneous telemetry databases requires advanced SQL and data engineering expertise, creating a critical bottleneck for non-technical personnel. Furthermore, the strict data privacy regulations and security constraints inherent to critical energy infrastructure often prohibit ...

---

### 22. Syn2DRE: Synergistic Dual Teacher-Student Framework for Document-level Relation Extraction

**Authors:** Khai Phan Tran, Xue Li

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09342v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09342v1)

**Summary:** Document-level Relation Extraction (DocRE) aims to identify relations between entities across a document but typically relies on costly large-scale annotations. While pseudo-labelling enables the use of low-quality data, existing methods often suffer from inefficiency and confirmation bias. To address these challenges, we propose Syn2DRE, a semi-supervised framework that combines self-supervised learning with cross-supervision in a lightweight teacher-student architecture to produce more reliabl...

---

### 23. ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective

**Authors:** Chaoran Li, Yukun Li, Zeyuan Zhao, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09326v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09326v1)

**Summary:** Foundation models are increasingly deployed as agentic systems that perceive context and act autonomously, raising the need to evaluate their moral behavior as active decision-makers. Existing benchmarks, however, largely ask models to judge human actions from third-person textual vignettes, leaving untested how models behave when they themselves become the acting agent. We introduce ABHBench, a multimodal benchmark built from Detroit: Become Human, an interactive narrative game, to evaluate how...

---

### 24. Asymmetric Correspondence Learning for Lexical and Style Embeddings: Interpreting Latent Space via Acoustic Features

**Authors:** Michael Whealing, Robert Gaizauskas, Thomas Hain

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09313v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09313v1)

**Summary:** Self-supervised speech embeddings jointly encode lexical, speaker, and prosodic information, complicating feature isolation. We introduce Asymmetric Correspondence Learning (ACL), distilling HuBERT features into separate Acoustic Word Embeddings (AWEs) and Acoustic Style Embeddings (ASEs) via a split-latent correspondence bottleneck. Through probing and clustering evaluations on single-word utterances, we demonstrate that substantial variance from extrinsic sources remains encoded within each la...

---

### 25. Multilingual Artificial Datasets for AI-Driven Cardiology: the CliTe and ParaCliTe corpora

**Authors:** Lorenzo Pratesi, Eulalia Farre-Maduell, Machteld Boonstra, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09296v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09296v1)

**Summary:** Background and Aims. Comparable, multilingual, validated cardiology corpora are critical to advance trustworthy natural language processing (NLP) models for cardiology but such resources are scarce due to privacy concerns. This study aimed to cover this gap by presenting suitable artificial corpus creation guidelines and by releasing 3 multilanguage corpora. Methods. Following purpose-specific publicly-available corpus construction guidelines, cardiologists from 7 European hospitals generated ar...

---

### 26. DUET: Dual-Sparse Inference for Block Diffusion Language Models

**Authors:** Siyuan Yan, Shen Gu, Xiaoxing Ma, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09239v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09239v1)

**Summary:** Diffusion language models (DLMs) enable parallel token generation through iterative denoising, yet their inference remains costly due to repeated attention over a growing historical prefix and repeated processing of the entire current generation block. Historical attention becomes increasingly expensive as generation progresses, while all current-block positions are propagated through the Transformer at every denoising step even though only a small fraction are typically resolved at that step. I...

---

### 27. KLEAR: Knowledge-Matched LLM Evaluation in Korean across Application Requirements via Controlled Benchmark Transformation

**Authors:** Seoyeon Kim, Jeonghyun Kang, Hamin Koo, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09223v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09223v1)

**Summary:** Existing Korean benchmarks for Large Language Models (LLMs) evaluate performance across diverse knowledge domains, but their accuracy scores cannot distinguish whether incorrect responses arise from a lack of required knowledge or a failure to apply that knowledge correctly. Our analysis of existing Korean benchmarks reveals that most questions can be answered through factual recall alone, while those demanding greater application also differ in required knowledge, making it difficult to isolate...

---

### 28. Khmer PFGen-Bench: Building a Judge-Free Benchmark for Open-Ended Generation in a Low-Resource Language

**Authors:** Mengsay Loem, Kentaro Imajo, Ryota Ozaki, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09222v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09222v1)

**Summary:** Benchmarks for open-ended generation often rely on large language model (LLM) judges, whose reliability in low-resource languages is uncertain. We introduce Khmer PFGen-Bench, to our knowledge the first judge-free benchmark for multi-sentence answers to questions composed directly in Khmer, a low-resource language. Khmer PFGen-Bench adapts the scorer of PFGen-Bench, a benchmark for Japanese that scores responses with keyword rules and n-gram statistics from LLM-generated references. This scoring...

---

### 29. RPEG: Training Reasoning Language Models Scalably and Cost-Effectively

**Authors:** Maciej Besta, Leonard Schmidt, Pierre Pang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09207v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09207v1)

**Summary:** Reinforcement learning (RL) is now central to training Reasoning Language Models (RLMs), but RLM pipelines are difficult to scale and costly to run because each RL step couples multiple large models, heterogeneous stages, cross-step state, and complex asynchronous dependencies. Existing systems typically optimize only parts of this design space. We address this complexity by jointly optimizing the pipeline structure as well as its execution using a novel data-centric graph intermediate represent...

---

### 30. Representational drift in a code model: behaviour settles, which neurons carry it does not

**Authors:** Piotr Wilam

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09204v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09204v1)

**Summary:** In neuroscience, representational drift is a change in which neurons carry a representation while behaviour stays the same; we measure its analogue in OpenCoder-1.5B during pretraining, for 169 Python constructs over two trillion tokens at a constant learning rate, with a noise unit on every change, at checkpoints as close as 1,000 training steps. For 16 of the 169, those whose grammar fixes a next token, the loss at those positions reaches its floor within the first 4% of training, while the mo...

---

### 31. Copies Are Not Confirmations: How News Duplication Fools LLM Judges and Continual Learners

**Authors:** Abdelkader Metales, Miriam Grabenheinrich, Aicha Metales

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09203v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09203v1)

**Summary:** Many news reports of a claim are copies of one source: wire stories, content shared within a media group, syndicated features and press releases. We ask whether LLM judges and continual learners treat such copies as independent confirmations. In 200,000 English CC-News articles, a MinHash detector links 18.9% to a near-copy from another outlet (precision 0.97 once boilerplate is removed); it links 92% of edited reprints to their originals but none of the LLM rewrites by phi4, Llama 3.2 or Gemini...

---

### 32. Structure and Lineage Evidence for Vietnamese Statutory Article Retrieval on DRiLL

**Authors:** Duc-Vu Nguyen, Ngan Luu-Thuy Nguyen

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09200v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09200v1)

**Summary:** We study Vietnamese statutory Article retrieval on DRiLL using features for provision identity and local form, same-law support, and citation and lineage evidence. Across five random seeds, selectors sharing candidates, listwise Qwen evidence, and learner settings improve official $F_2$ from 71.77% to 72.91%, with the largest descriptive gain on two-Article questions. Added features account for 18.20% of the proposed selector's total decision-tree split gain, measured as training-objective reduc...

---

### 33. Calibrated concept profiles: making the reading of a model's neurons a measurement

**Authors:** Piotr Wilam

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09196v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09196v1)

**Summary:** Interpretability has largely moved from reading a model's neurons directly to reading a second model trained on the first: a probe, a sparse autoencoder, a crosscoder. The move answered real faults -- mixed meanings, thresholds without a unit, readings that did not transfer from one study to the next -- but gave up what a direct reading alone provides: nothing trained in between, the neurons themselves named, and a reading that can be repeated and compared. Here the direct reading is made a meas...

---

### 34. A Taxonomy-Driven Synthetic Dataset for Retrieval Effectiveness and Fairness Evaluation in Hiring

**Authors:** Warren Jouanneau, Morgane Hoffmann, Emma Jouffroy, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09178v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09178v1)

**Summary:** While machine learning hiring tools are ubiquitous, the need for privacy regulations and commercial sensitivity makes public benchmarking legally complex. We address this challenge by introducing a taxonomy-driven, fully synthetic HR dataset and benchmark to simultaneously evaluate retrieval effectiveness and algorithmic fairness. Grounded in 660K real freelancer profiles, our multilingual corpus features candidate profiles, project briefs, and counterfactual demographic twins. Auditing state-of...

---

### 35. BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models

**Authors:** Anthony Rhodes, Gadi Singer

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09147v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09147v1)

**Summary:** Behavioral evaluation of language models fixes its dimensions in advance: hallucination, sycophancy, toxicity, over-refusal. An operator in a regulated industry needs a different question answered: does a system do what a particular rulebook requires? We introduce the Behavioral Misalignment Metric Suite (BMMS), which measures policy-conditioned misalignment by taking a policy corpus as an argument and returning a compliance profile over it, for any published policy and any system that answers i...

---

### 36. PathXAI: Evidence-guided structured pathology reporting by transferable tissue segmentation

**Authors:** Zhaorui Tan, Jun Aun Tan, Weixiang Zhong, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09117v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09117v1)

**Summary:** Pathology reporting requires translating tissue observations across regions and slides into specific diagnoses and supporting morphological descriptions. However, the use of explicit tissue-composition measurements to guide H&E-based report generation remains underexplored. Thus, we developed PathXAI, which combines segmentation-derived tissue information with H&E images and optional domain knowledge to guide diagnostic reasoning, targeted reinspection and structured report writing. Its segmenta...

---

### 37. PhoPunct: A Large-Scale Benchmark of Transformer Architectures for Vietnamese Punctuation Restoration

**Authors:** Khoa D. Nguyen, Thai Bao Huynh, Binh T. Nguyen

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09107v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09107v1)

**Summary:** Vietnamese punctuation restoration is often evaluated on relatively small benchmarks, limiting conclusions about how architectural choices scale with data volume. We present a controlled benchmark on News and Novels corpora containing 22.1 million labeled tokens (19.9M News and 2.2M Novels). We evaluate 17 architectures formed from four pretrained Transformer backbones and optional bidirectional long short-term memory (Bi-LSTM) and conditional random field (CRF) layers, together with a PhoBERT-l...

---

### 38. AlienBench: A Benchmark of Structural Novelty in Language Model Outputs

**Authors:** Jonas Oppenlaender, Johanna M. Silvennoinen

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09094v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09094v1)

**Summary:** Large language models (LLMs) are increasingly used for creative tasks such as writing, design, and idea generation. For these uses, it matters whether a model's ideas depart from familiar examples or stay close to them. Novelty is one standard measure of creativity, and current creativity evaluations ask human experts or LLM judges to rate how novel an output is. However, these ratings have no fixed reference for what counts as novel (or, in other terms, departure from the familiar). Measuring t...

---

### 39. MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition

**Authors:** Rui Qi, Yunlong Liang, Yufeng Chen, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09090v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09090v1)

**Summary:** Existing multilingual retrieval-augmented generation relies heavily on learned retrievers and similarity-based ranking from multilingual collections, which are vulnerable to cross-lingual retrieval errors and indexing overhead. In this paper, we explore retriever-free multilingual search, where the model directly interacts with raw corpora through executable shell commands. This paradigm shifts the bottleneck to multilingual search action generation, where exact search is sensitive to entity sur...

---

### 40. The Invisible Gap: Romanized Indic Generation Fails Where Automatic Metrics Succeed

**Authors:** Madhu Sudhan Rao Beesetty, Surbhi Sharma, Devesh Maheshwari, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09085v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09085v1)

**Summary:** Hundreds of millions of Indians communicate with digital systems in romanized Latin characters -- typing "aap kaise hain" rather than native script -- yet romanized Indic generation is absent from NLP benchmarks and evaluation frameworks. We demonstrate that automatic metrics (BGE-M3, BERTScore) systematically misrepresent the quality of romanized Hindi, Telugu, and Kannada generation. We evaluate four LLMs (Claude Opus 4.8, GPT-5.5, Gemini 2.5-flash, Qwen3.5-35B) on 142 OpenAssistant query-resp...

---

### 41. Large Language Model Deployment on Resource-Constrained Edge Devices: A Practitioners Survey

**Authors:** Rahul Maliakkal, Yashasvi Makin, Plawan Rath, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09075v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09075v1)

**Summary:** Large Language Models (LLMs) have transformed many areas of artificial intelligence (AI), but their substantial resource requirements limit their deployment on mobile and edge devices. Although LLMs have demonstrated impressive capabilities in various applications, the next challenge is deploying these models on resource-limited edge devices. Recent innovations in software optimizations and specialized hardware have made it feasible to deploy LLMs on edge devices. Edge deployment offers benefits...

---

### 42. Does Reasoning Improve Psychological Depth in Large Language Models?

**Authors:** Ruichen Zheng, Yihe Wang, Fabrice Harel-Canada, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09061v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09061v1)

**Summary:** Benchmark gains from reasoning-enhanced large language models encourage the assumption that these models should broadly perform better on complex generative tasks, but this remains underexplored in open-ended, creative domains shaped by nuances of reader experience. We tested this assumption through the lens of psychological depth in short stories. We compared DeepSeek-R1 vs. DeepSeek-V3, our closest available contrast for reasoning-oriented post-training, and GPT-5 vs. GPT-4o, through 60 blinde...

---

### 43. Real-Time Short-Response Selection for Spoken Dialogue Systems

**Authors:** Hien Ohnaka, Kazuyo Onishi, Koichiro Yoshino

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09057v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09057v1)

**Summary:** To realize spoken dialogue systems that can interact naturally with users, it is important for the system to respond to user utterances at appropriate timings. To achieve such natural turn-taking, the system needs not only to predict appropriate response timings but also to mask delays caused by language generation and speech synthesis so that they are not perceived by the user. We propose a real-time short-response selection task that can be integrated with existing turn-taking models to mask g...

---

### 44. Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation

**Authors:** Yijun Zhu, Jianxin Wang, Chengchao Shen

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09042v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09042v1)

**Summary:** Training smaller language models on reasoning solutions generated by a larger teacher model is the prevailing approach for transferring mathematical reasoning capabilities. However, the student tends to overfit the output distribution of the teacher and generalizes poorly when its own behavior at inference time deviates from the training data. Recent methods attempt to bridge this gap by incorporating error data, yet the corrective trajectories still reflect the reasoning patterns of the teacher...

---

### 45. Language, Not Code Abstraction: Natural-language Training Shapes Brain-aligned Geometry

**Authors:** Iñigo Parra

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09027v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09027v1)

**Summary:** Code-trained language models produce positive brain scores, which raises the question of whether abstract structure learned from programming languages can substitute for natural-language training. We trained 25 GPT-2-small models on TinyStories, Python, C functions, x86-64 assembly, and the corresponding machine code, and scored them using a shared tokenizer and encoding procedure against matched random-weight models. On Pereira-243 and Tuckute2024, TinyStories exceeds the mean of the four code ...

---

### 46. Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams

**Authors:** Yin Liu

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08998v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08998v1)

**Summary:** When a multimodal LLM miscounts in a diagram, does it fail at seeing or at counting? Existing visual graph and puzzle benchmarks vary visual density and algorithmic hardness together, confounding the two. We pair counting questions about the same drawing that sit in different counting-complexity classes, such as its spanning trees (a determinant) and its simple paths (#P-complete), and use a transcription probe and a text-only control to separate reading from computing. We test Gemini, Gemma and...

---

### 47. Same Facts, Different Remedy: Linguistic Profiling and Arbitrariness in LLM and System One Decisions

**Authors:** Colin Priest

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08995v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08995v1)

**Summary:** Large language models are increasingly used to resolve consumer complaints, and the way complainants write varies with age, education and socioeconomic status (SES). We audit three remedy-decision systems using sociolinguistic rewrites of US consumer financial complaints that are instructed to preserve every fact: two generative LLMs that return a single label (GPT-4o-mini and GPT-5-mini) and a probabilistic "System One" model that returns a distribution over remedies (Jev). Using pre-registered...

---

### 48. Beyond Truncation? Entailment-Licensed Elision and the Limits of Semantic Preservation in LLM Decoding

**Authors:** Mahmoud Alyosify, Mirna Imbabi, Eman Elkhamisi

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08975v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08975v1)

**Summary:** Instruction-tuned large language models (LLMs) answer at greater length than a request needs. We ask whether a training-free controller inside the decoding loop can remove that surplus while preserving content, judged against the simplest possible baseline: truncating the model's own answer to the same length. An entropy-gated logits processor removes 25.5-34.9% of tokens on MT-Bench development questions and 19.9-34.2% on a sealed test split within pre-registered BERTScore non-inferiority margi...

---

### 49. Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making

**Authors:** Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08971v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08971v1)

**Summary:** Multi-agent LLM systems increasingly aggregate judgments across model instances, but reasoning about other agents can itself introduce failure. We study a setting in which LLMs shift their public decisions after observing ambiguous social signals while reporting inaccurate estimates of what other agents privately judged, even when the group's recorded private judgments do not support the apparent consensus. We call this failure phantom consensus and study it as a pluralistic-ignorance-style patt...

---

### 50. Using an LLM to Tackle Difficult Cases in NER for Nepali Tweets

**Authors:** Claire Wang

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08967v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08967v1)

**Summary:** Named entity recognition (NER) is challenging for social media data in a low-resource language. LLMs often lag behind pretrained language models (PLMs) in NER performance, but they show promise in handling cases that PLMs struggle with. Using a dataset of Nepali tweets, we split the test set into "easy" and "hard" cases using token probabilities from a fine-tuned pretrained language model (PLM). We then evaluate an LLM on the hard test cases using 16 different prompt configurations. We find that...

---

## cs.CV

**50 papers**

### 1. Video-Coder: Reinforcing Agentic Coding for Video Generation

**Authors:** Chaoyang Wang, Sicheng Gao, Junan Hu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09894v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09894v1)

**Summary:** Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remains challenging. In this paper, we introduce Video-Coder, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to construct a dynamic 3D scene (Draft Video) that provides structure and motion signals...

---

### 2. On Agentic Manipulation Policies

**Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09892v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09892v1)

**Summary:** Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged ...

---

### 3. FlowMoP: Stochastic Multi-Person Motion Prediction

**Authors:** Aadya Agrawal, Ho Kei Cheng, Alexander Schwing

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09882v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09882v1)

**Summary:** Predicting the future motion of multiple people is inherently stochastic: the same observed history admits many plausible continuations depending on intent, coordination, and social context. Yet the dominant paradigm in multi-person 3D motion prediction remains deterministic, with existing methods producing a fixed number of outputs per agent. In contrast, we present a conditional flow matching framework that jointly generates diverse future motions for multiple agents, modeling both global traj...

---

### 4. ZeoBench: A Benchmark for Self-Supervised Learning on 3D Zeolite Representations

**Authors:** Aaron Sun, Yachan Liu, Ping Yang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09880v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09880v1)

**Summary:** Zeolites are an important class of porous crystalline materials with broad applications in gas storage, separations, and catalysis. Although hundreds of thousands of experimentally realized and hypothetical zeolite structures are known, identifying materials optimized for a target application remains challenging because property labels are expensive to obtain and available only for limited structure-molecule pairs. While prior work has demonstrated that 3D neural representations can predict zeol...

---

### 5. Graded convolutional networks: scale invariance without the scale and robustness to unknown blur

**Authors:** Tanush Shaska

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09878v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09878v1)

**Summary:** The Gaussian jet of an image is a graded vector space: a dilation by $λ$ multiplies derivatives of order $k$ by $λ^{-k}$. Local graded convolutions are exactly homogeneous differential operators, and a local feature is dilation-invariant if and only if it factors through the scale-normalized jet or, without the scale, through the retraction onto the weighted sphere of the grading. Under unknown Gaussian blur the retraction changes only by a change of scale, whereas the scale-normalized jet acqui...

---

### 6. GRAC: Graph-Based Retrieval-Augmented Captioning for Surgical Scene Description

**Authors:** Rochak Dhakal, Chen Zhao, Soup Cobb, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09866v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09866v1)

**Summary:** Purpose: Surgical operative reports support procedural documentation, surgical training, performance assessment, and workflow review. However, extracting meaningful information often requires extensive manual review and clinical expertise. Automated surgical scene descriptions could reduce this burden by leveraging recurring surgical activities and prior knowledge.   Methods: We propose GRAC (Graph-Based Retrieval-Augmented Captioning), a framework that represents surgical scenes as graphs captu...

---

### 7. Flow-Guided Target-Space Alignment via Path Consistency

**Authors:** Ruizhi Yuan, Zeqiu Yu, Wei Gao, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09863v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09863v1)

**Summary:** Many multimodal alignment problems require mapping a source modality into a fixed space defined by a target modality, where the target space is not merely an intermediate embedding but is used directly for downstream analysis. In this setting, successful alignment should preserve both the global structure of the target distribution and the instance-level correspondence observed in paired source--target training data. Existing objectives typically address only part of this goal: contrastive losse...

---

### 8. Super-resolved digital terrain models for GEDI geolocation correction: agreement with airborne LiDAR DTM-based corrections at the beam level, not the footprint level

**Authors:** Natsuki Yuda, Shinichiro Shirota

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09854v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09854v1)

**Summary:** The Global Ecosystem Dynamics Investigation (GEDI) mission measures three-dimensional forest structure with a LiDAR aboard the International Space Station. GEDI observations have geolocation errors of about 10 m, which cause misalignment with other remote sensing data and reduce the accuracy of downstream tasks. Matching GEDI ground elevations against high-resolution digital terrain models (DTMs) from airborne LiDAR is one way to correct these errors, but such DTMs exist in few regions. To widen...

---

### 9. Health-System-Wide Mapping of Demographic Information in Routine Clinical Histopathology

**Authors:** Shengjia Chen, Ruchika Verma, Kevin Clare, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09851v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09851v1)

**Summary:** The extent to which demographic-associated information is detectable across organs and disease states in routine clinical histopathology remains unclear. Here, we analyzed 1.3 million hematoxylin and eosin whole-slide images from 257,322 patients across 25 organs, using pathology foundation-model representations and multiple-instance learning to systematically map information associated with sex, age group, and self-reported race. Across 69 organ-demographic combinations, demographic attributes ...

---

### 10. AdaptivePnP: Fast Auto-Tuned Plug-and-Play for Deconvolution

**Authors:** Haley Duba-Sullivan, Emma J. Reid, Charles A. Bouman, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09845v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09845v1)

**Summary:** Plug-and-play (PnP) methods reconstruct images by alternating a data-fitting step with an image denoiser. Their performance depends on two parameters: the step size $γ$ and the measurement noise level $σ$. In practice, $γ$ is often tuned by grid search over validation images and must be retuned whenever the problem setting changes, and $σ$ is assumed known or estimated separately. We propose AdaptivePnP, a PnP framework that jointly estimates $σ$ and $γ$ at every iteration from the data-fitting ...

---

### 11. BEV3SR: Evidence-Aware 3D Spatial Reasoning from Video

**Authors:** Fan Zhu, Rui Yu

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09816v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09816v1)

**Summary:** 3D spatial reasoning from video remains challenging for VLMs because videos provide sequential, view-local observations rather than persistent metric scene records. Many questions must be answered in a query-specified perspective rather than the observed camera viewpoint, and prompting with a fixed set of RGB views may miss sparse or occluded visual cues. To address these gaps, we introduce BEV3SR, a training-free and backbone-agnostic framework for RGB-D videos with camera parameters. BEV3SR tu...

---

### 12. AR-Edit: Training-Free Autoregressive Video Editing without Inversion

**Authors:** Hovhannes Margaryan, Quentin Bammey, Christian Sandor, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09795v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09795v1)

**Summary:** Editing a video stream in real time, without access to future frames, is essential for interactive applications. Existing training-free video editing methods, however, assume full offline access to the entire sequence, while streaming approaches either rely on additional training or are limited to specific editing techniques. We show that this limitation can be removed by analyzing the self-attention dynamics of DMD-distilled autoregressive (AR) video diffusion models. We uncover a key asymmetry...

---

### 13. Seeing What Matters: Benchmarking Task-Conditioned Actionable Spatial Belief for Manipulation

**Authors:** Yina Jian, Mingkun Xu

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09794v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09794v1)

**Summary:** When should a robot look at the cup, and when at the portafilter? Spatial-reasoning benchmarks evaluate whether a model can describe a scene, but manipulation needs something more specific: the ability to acquire the particular evidence that makes the current command executable. A view that is informative for one task can be useless for another, even at the same workstation. We introduce Seeing What Matters, a benchmark for task-conditioned actionable spatial belief in simulated tabletop manipul...

---

### 14. ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models

**Authors:** Lingyun Song, Ziyao Chen, Kang Pan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09770v1)

**Summary:** Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{S}ubspace navigation framework for lifelong knowledge \textbf{E}diting. ROSE addr...

---

### 15. AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos

**Authors:** Zhongyi Zhang, Jingyu Xiao, Shuqing Li, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09769v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09769v1)

**Summary:** Animation is pervasive on the Web, the CSS animation property alone appears on over three-quarters of webpages. Yet existing webpage code generation benchmarks target static screenshots, user-triggered interactions, or isolated motion graphics, leaving the ability of multimodal large language models (MLLMs) and coding agents to reconstruct complete animated webpages largely unexplored. To fill this gap, we introduce AnimWeb-Bench, the first benchmark for animated webpage code generation from vid...

---

### 16. A lightweight convolutional neural network for target detection in an edge environment

**Authors:** Hughes Perreault, Ola Ahmad, Daniel Czuboka

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09756v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09756v1)

**Summary:** This paper proposes a novel, lightweight convolutional neural network (CNN) designed for edge device deployment. The CNN is developed to recognize and classify threats or targets of interest. The model is equipped with a real-time hotspot detection algorithm, which enables it to process information quickly and accurately, resulting in improved inference time of up to 20 fps and a detection range of more than 400 meters with typical thermal situational awareness sensors. The proposed CNN has been...

---

### 17. Multiscale Closing Index (MCI) for measuring structural similarity between 2D point sets

**Authors:** Nicolò Zava, Angel Franco-Alvarez, Samy Blusseau, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09745v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09745v1)

**Summary:** We introduce Multi-scale Closing Index (MCI), a new dissimilarity measure for evaluating the alignment of two 2D point sets. MCI is bounded between 0 and 1 and is based on multiscale mathematical morphology operations, with smaller values indicating greater structural agreement. The measure was motivated by the need to assess the quality of registration between point sets representing cell populations in biological images. To evaluate its behaviour under controlled conditions, we generated synth...

---

### 18. Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration

**Authors:** Dario Scilla, Omar A. Lopez, Mattia Rosso, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09740v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09740v1)

**Summary:** Shallow-water UAV imagery provides centimeter-scale observations of benthic environments, but water-induced distortions complicate interpretation. To our knowledge, we present the first systematic zero-shot benchmark of unified multimodal large language models (MLLMs) for both assessing water-induced distortions and restoring shallow-water imagery within the same model framework. We evaluate five open-weight unified MLLMs with frozen pretrained weights and without access to paired reference imag...

---

### 19. TriNetra: Thermal-Reliability-Guided RGB-Thermal Fusion and Tracking for Surveillance

**Authors:** Sadique Khatib, Aditya Ahirrao, Vedant Sonawane, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09725v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09725v1)

**Summary:** Visible cameras fail at night and thermal sensors fail under saturation, blur or loss of contrast, yet most RGB-thermal (RGB-T) detectors mix the two streams with fixed weights and cannot tell when one modality has become unreliable. TriNetra is a reliability-aware surveillance framework built around this problem. The proposed solution computes a frame-level Thermal Reliability Coefficient (TRC) from five label-free image cues, uses it to gate the thermal features of a dual-branch YOLOv8m detect...

---

### 20. Evaluating Anterior Cruciate Ligament Risk of Injury Using a Graph Convolutional Autoencoder

**Authors:** Athanasios Babouras, Paul A. Martineau, Thomas Fevens

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09724v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09724v1)

**Summary:** Current solutions for assessing the risk of anterior cruciate ligament (ACL) injury typically rely on expensive motion-capture labs that require substantial resource investment or subjective evaluations of specific athletic stress tests by experts. The Drop Vertical Jump (DVJ) and the Single Leg Hop (SLH) are two examples of such tests typically used to track progress in ACL rehabilitation. In this paper, we develop an unsupervised learning model that runs entirely on a smartphone for two tasks,...

---

### 21. Direct Regression and Geometric Recovery for Event-based Spacecraft Pose Estimation

**Authors:** Pruthvi Nandan Janga, Kashyap Hegde Kota, Bharatesh Chakravarthi

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09717v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09717v1)

**Summary:** Event cameras offer high temporal resolution and dynamic range for uncooperative spacecraft pose estimation, but models trained on synthetic event streams must generalize to the noise, background activity, and contrast variation of physical sensors. We present a comparative systems study of two independently developed approaches to synthetic-to-real, event-based 6-DoF spacecraft pose estimation. The first is a modular pipeline that combines learned keypoint detection and unlabeled target-domain ...

---

### 22. Beyond Segmentation: Enriching ImageCAS with Coronary Ostia Landmarks, Rooted Centerline Graphs, and Open-Weight Localization Models

**Authors:** Matteo Leccardi, Andrea Moglia, Marco Morandini, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09714v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09714v1)

**Summary:** Coronary ostia and centerlines are key reference points for automated analysis of coronary computed tomography angiography (CCTA), from surgical planning to intraoperative vessel tracking. However, the only public ostium annotations cover 77 non-gated aortic scans, not CCTA, while CAT08 and ASOCA (32 and 40 CCTA scans) mark the ostia only implicitly, as centerline start points. This work enriches ImageCAS, the largest public dataset for coronary artery segmentation, with ostium annotations for i...

---

### 23. PoseRieFlow: Riemannian Flow Matching for Whole-Body Text-to-Pose Generation

**Authors:** Jan Spindler, Bardia Ardakanian, Patrick Stotko, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09692v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09692v1)

**Summary:** We present PoseRieFlow, a compact flow-matching framework for text-conditioned generation of whole-body 3D human poses. Prior text-to-pose methods either neglect articulated hands or model rotations in Euclidean space despite their non-Euclidean geometry. PoseRieFlow instead formulates generation directly on the product manifold of SMPL-H joint rotations, learning a text-conditioned vector field that transports samples from an isotropic $\mathrm{SO}(3)$ Gaussian prior to the data distribution al...

---

### 24. Dual Architecture Fusion Vehicle Lidar 3D Target Detection

**Authors:** Muyun Li, Weizheng Jin, Yuan Sun

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09664v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09664v1)

**Summary:** In this paper, a 3D backbone network (SpconvTransformer) based on the fusion of convolutional architecture branch and Transformer architecture branch is proposed. The convolution branch uses 3D sparse convolution and submanifold convolution to learn local voxel features and semantic information, and the Transformer branch uses the self-attention mechanism to model the remote relationship between voxels, uses the broad receptive field to capture rich context information, and complementing the adv...

---

### 25. Video2Asset: Online Construction of Persistent 3D Street-Scene Assets

**Authors:** Zihan Zheng, Chunlei Cai, Zhenlong Wu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09661v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09661v1)

**Summary:** Online 3D street-scene asset construction turns multi-view video into a continually updated scene of independently editable objects. The central challenge is to accumulate partial, intermittent observations under motion and occlusion without fragmenting identities or mixing evidence across objects. To address this challenge, we propose Video2Asset, an online framework for constructing persistent 3D assets from multi-view video. Using occupancy as an intermediate representation, we construct iden...

---

### 26. Decoupled Mode Connectivity for Base-to-Novel Generalization in Vision-Language Models

**Authors:** Imad Eddine Marouf, Khalid Oublal, Enzo Tartaglione, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09655v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09655v1)

**Summary:** Prompt learning adapts vision-language models such as CLIP by optimizing a short learnable prompt. The cross-entropy objective pulls this prompt toward   base-class specialization, whereas generalization to unseen classes benefits from staying close to CLIP's zero-shot feature space. Because both objectives   act on the same prompt, their gradients conflict at convergence, and in our experiments no single-prompt loss design clearly improves on the cosine   baseline. We propose Decoupled Mode Con...

---

### 27. Breaking the Privacy Promise: Gradient Inversion Attacks on Federated Low-Rank Adapted Vision Transformers

**Authors:** Ritik K. Badiya, Siladittya Manna, Ashmit Sinha, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09652v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09652v1)

**Summary:** Parameter-efficient fine-tuning (PEFT) has been increasingly adopted to fine-tune pretrained models with low computational cost and is therefore also preferred in the federated learning paradigm to reduce computational and communication overhead. In this work, we investigate the sparsely explored problem of the risk of private data leakage in LoRA-adapted Vision Transformers (ViTs), where low-rank updates weaken the gradient signal available to a server with access to individual client updates. ...

---

### 28. Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning

**Authors:** Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09625v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09625v1)

**Summary:** Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term memory and planning. In this work, we address the problem of long-term memory in MBRL by moving beyond the commonly studied paradigm of architecture design. We introduce Test-Time Model-B...

---

### 29. CRTrack-Cap: A New Benchmark for Cross-View Dense Video Object Captioning

**Authors:** Xiangqun Zhang, Likai Wang, Zekun Qian, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09617v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09617v1)

**Summary:** Dense video object captioning (DVOC) localizes, tracks, and describes object trajectories within a video. Existing methods process each camera view independently, producing separate camera-local tracklets and captions for the same person across cameras. These outputs lack a unified description and leave complementary appearance evidence across views unused. We therefore formulate cross-view DVOC (CVDVOC), which associates these tracklets into scene-level global trajectories and generates one cap...

---

### 30. Dual-Region Slice Aggregation for CT-Based Renal Tumor Classification

**Authors:** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09599v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09599v1)

**Summary:** Clear cell renal cell carcinoma (ccRCC) is the most common kidney cancer in adults. We present a region-aware architecture for CT-based ccRCC classification. Tumor and 0--10 mm peritumoral context are pooled separately from shared frozen DINOv3 feature maps. A shared position-aware slice aggregator precedes fixed training-only principal component analysis (PCA). The resulting representations are fused with radiomics using two scalar feature gates. Evaluation on KiTS23 and 111 external cases yiel...

---

### 31. MSR-ABC: Complementary Feature Fusion for Clear Cell Renal Cell Carcinoma Classification

**Authors:** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09583v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09583v1)

**Summary:** Clear cell renal cell carcinoma (ccRCC) classification from computed tomography (CT) may benefit from representations that capture different aspects of tumour phenotype. However, simply concatenating reconstruction-derived features, image--text embeddings, and radiomic descriptors may not fully exploit their complementary information. We propose MSR-ABC, a global--local framework integrating MedVAE, MedSigLIP, and radiomics. Spatially matched local image descriptors interact through cross-repres...

---

### 32. Video Stitching from Multiple Moving Cameras

**Authors:** Shira Ifergane, Roy Amoyal, Shahar Benishay, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09570v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09570v1)

**Summary:** We address geometric video alignment for the same scene captured by multiple freely moving cameras. Existing methods, which are based on image stitching or video stabilization, are typically limited to two cameras or must assume the restrictive setting of a fixed linear ordering of the cameras. We propose MViS, a lightweight test-time optimization framework for joint multi-view alignment with temporal consistency. MViS uses a spatial-transformer-inspired net to jointly process frames from all vi...

---

### 33. Multimodal Training with Knowledge Traction for Video Anomaly Detection

**Authors:** Xiao Tan

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09536v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09536v1)

**Summary:** The task of weakly supervised video anomaly detection is challenging. Existing approaches mainly model video frame features and determine whether anomalies are present based on their magnitudes. In this work, we propose a novel method that incorporates external knowledge into training to improve model performance, robustness, and generalization. We leverage textual prompts and a large language model (LLM) to establish prior information for the specific task, and employ dictionary learning to nor...

---

### 34. ExQuery: Explicit Structured Query Priors for Temporal 3D Object Detection

**Authors:** Honglin Sun, Yifei Zhang, Junyang Zhang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09527v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09527v1)

**Summary:** Sparse query-based 3D detectors commonly encode heterogeneous semantic, geometric, and motion information into unified latent queries, including when explicit 3D anchors are used. We introduce ExQuery, an explicit structured query framework for temporal 3D object detection. Each decoded query is organized into a shared semantic context slice and physical-state-specific slices for center, dimensions, orientation, and velocity. This structure is preserved from prior encoding to branch-specific reg...

---

### 35. RadarDINO: Distilling a Visual Foundation Model into mmWave Radar for Human Mesh Reconstruction

**Authors:** Furkan Mert Algan, Zhifan Ni, Eckehard Steinbach

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09524v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09524v1)

**Summary:** Millimeter-wave (mmWave) radar offers a privacy-preserving and illumination-robust alternative for human mesh reconstruction (HMR). However, high-fidelity radar HMR remains challenging. Sparse point cloud-based methods suffer from information loss and missed detections, while raw radar tensor methods like RT-Mesh lack fine-grained semantics and explicit local body modeling. In this paper, we propose RadarDINO, a radar HMR framework that distills visual semantics from a DINOv3 teacher into 3D rad...

---

### 36. Embedding Predictive Adaptation and Refinement for Multi-Modal Industrial Anomaly Detection

**Authors:** Jaeho Cho, Jinsik Bang, Taehwan Kim

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09521v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09521v1)

**Summary:** Industrial Anomaly Detection (IAD) has evolved from 2D image-based approaches to multi-modal methods that leverage the complementary nature of RGB images and 3D point clouds. Among these, memory bank-based methods, which identify anomalies by the discrepancy between each query patch feature and its nearest normal prototype, have proven particularly effective. However, two limitations remain: (i) employing frozen pretrained encoders yields insufficient discrimination between normal and anomalous ...

---

### 37. V-STORM: A Structure-Aware Grounded Chain of Thought Dataset for Faithful and Fine-Grained Spatio-Temporal Video Reasoning

**Authors:** Dian Jiao, Yuqian Yuan, Jiaqi Zhu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09511v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09511v1)

**Summary:** While MLLMs can often identify what happens in a video, they still struggle with fine-grained spatio-temporal reasoning, which requires precise grounding when and where the supporting evidence appears and composing such evidence into a coherent reasoning chain. This challenge is exacerbated by the lack of scalable data construction and evaluation pipelines that provide granular, verifiable supervision linking reasoning steps to explicit spatio-temporal evidence.To address this gap, we present V-...

---

### 38. BEiTScore++: Reference-free Image Captioning Evaluation with BEiT-3 and Conformalized Quantile Regression

**Authors:** Gonçalo Gomes, Bruno Martins, Chrysoula Zerva

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09505v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09505v1)

**Summary:** Reliable uncertainty estimation is important for deploying evaluation metrics in real-world settings, where both input ambiguity and domain shifts are common. In this work, we propose an uncertainty-aware extension of the BEiTScore image captioning metric, producing conformally calibrated confidence intervals alongside alignment scores. Our approach models predictive distributions over human judgments, enabling both accurate scoring and principled uncertainty quantification in a single forward p...

---

### 39. FusionCLIP: Multimodal Contrastive Pretraining for Fusion Plasma Diagnostics

**Authors:** Qiang Chen, Xiao Wang, Qingquan Yang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09493v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09493v1)

**Summary:** Visible-light videos and multivariate diagnostic signals provide complementary observations of tokamak discharges. However, existing fusion pretraining methods, primarily learn representations by reconstructing or predicting observations, leaving the correspondence between these modalities underexplored. Representation learning is further challenged by the fact that plasma-related regions occupy only part of each video frame and diagnostic variables have substantially different sampling rates. W...

---

### 40. Left-Right-Consistent Iterative Stereo Matching via Cross-Injection

**Authors:** Manuel Knott, Diogo Luvizon, Daniel Scharstein, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09458v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09458v1)

**Summary:** State-of-the-art stereo matching models predominantly predict the disparity of only the left (reference) view. However, applications such as per-eye AR/VR rendering, novel view synthesis, or two-view depth fusion require disparity for both views, and need those two maps to agree. The usual workaround of running the network a second time on the horizontally flipped and swapped pair gives two independent predictions that can be inconsistent, especially on transparent surfaces, in textureless regio...

---

### 41. Overview of the ImageCLEFmedical 2026 GANs task: Exploring fingerprint detection, privacy leakage, and synthetic medical image generation

**Authors:** Alexandra-Georgiana Andrei, Mihai Gabriel Constantin, Mihai Dogariu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09455v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09455v1)

**Summary:** The 2026 ImageCLEFmedical GANs Task Exploring Fingerprint Detection, Privacy Leakage, and Synthetic Medical Image Generation continues to investigate privacy and security concerns around using patient data to generate synthetic medical images, now in its fourth edition. This edition introduces three complementary subtasks: the first extends prior editions by asking participants to detect which real images were used in training a Generative Adversarial Network to produce given synthetic outputs; ...

---

### 42. The Role Of Recurrent Refinement In Medical Image Segmentation

**Authors:** Joao D. S. Marques, David Calhas, Arlindo L. Oliveira

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09436v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09436v1)

**Summary:** While feed-forward segmentation networks perform well on large cohorts, they degrade in constrained clinical settings with few training samples and imaging artifacts. Human vision, by contrast, remains robust under these conditions, a property partly attributed to the recurrent and feedback connectivity of the visual cortex, which refines visual information over time. Inspired by this, we append lightweight recurrent refinement blocks to segmentation backbones, namely Conditional Random Fields (...

---

### 43. A Bridge from Paste to Place: Physics-Guided One-Step Image Composition via Object-Scene Interaction

**Authors:** Hongzhen Li, Youwei Pan, Yingfang Zhu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09387v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09387v1)

**Summary:** Realistic image composition must make a pasted object appear naturally present in a scene while preserving the fine details of both foreground and background. Reference-based insertion methods can change object pose and appearance, while foreground harmonization methods and shadow-specific synthesis methods each address only part of this task. An efficient, unified solution to this task remains an open challenge. We introduce Paste2Place, an end-to-end, physics-guided flow-based model that learn...

---

### 44. SPSC: Zero-Shot Cross-Subject EEG-to-Image Reconstruction via Semantic Preservation and Subspace Calibration

**Authors:** Yutang Lu, Shuai Jiang, Fei Su, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09380v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09380v1)

**Summary:** Pretrained vision-language models and diffusion generators have driven rapid progress in brain-to-image generation, while EEG-based reconstruction is still constrained by low signal-to-noise ratio and cross-subject semantic shifts. Zero-shot cross-subject reconstruction poses even greater challenges: EEG semantic embeddings learned from source subjects deviate from the manifold of image embeddings of the unseen target subject, particularly when neither target labels nor target image embeddings a...

---

### 45. HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes

**Authors:** Boran Zhao, Yanbin Hu, Jun Ye, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09355v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09355v1)

**Summary:** Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes. However, existing VLA memory mechanisms suffer from memory noise, particularly in complex 3D scenes, as stored episodic memories contain extensive redundant details about scene layouts, object configurations, and robot-specific states, which obscure generalizable manipulation principles and hinder cross-task transfer. To address this cha...

---

### 46. RegNC-Mamba3: Shared Structural Feature Learning Using Non-Causal State Space Principles for Multi-Modal Image Registration

**Authors:** Zhikang Li, Yan Wu, Xin Hu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09336v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09336v1)

**Summary:** The main challenge of multi-modal image registration is shared structural feature extraction with higher accuracy and lower computational complexity. Compared with a State Space Model (SSM), the State Space Principles (SSP) formulation of Mamba-3 uses a more accurate discretization with lower truncation error while maintaining linear complexity. However, vanilla SSP is designed for natural language processing (NLP) and is not directly suitable for images. To address this issue, we propose a nove...

---

### 47. Keyline Detection with YOLO: Runway Perception for Vision-Based Aircraft Landing

**Authors:** Leander Fritsch, David Rügamer, Alexej Klushyn

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09316v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09316v1)

**Summary:** Modern object detectors can predict keypoints as per-object geometric features, but keypoints are inherently vulnerable to occlusion and truncation. Object edges can provide complementary information, often remaining observable even when partially occluded or when their defining endpoints leave the field of view. We therefore introduce object keyline detection, the task of predicting a fixed, semantically ordered set of infinite lines per object instance. Unlike the outputs of general line-segme...

---

### 48. Interpretable Context-Aware Multi-Label Retinal Classification with Dual-Hub Heterogeneous Graph Neural Network

**Authors:** Proshanto Chanda, Munib Mesinovic, Tingting Zhu, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09309v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09309v1)

**Summary:** Multi-label retinal screening requires capturing co-occurring pathologies and clinical context, yet standard multimodal fusion remains opaque. We propose a dual-hub heterogeneous graph neural network (GNN) that couples spatial fundus features and structured clinical covariates through cross-modal message passing while providing inherent interpretability. Rather than relying on post-hoc saliency approximations, our architecture exposes multi-level decision pathways during forward aggregation: spa...

---

### 49. T2I Models Rarely Invert Negation but Often Fail to Suppress Negated Concepts: Benchmarking Negation Suppression in Text-to-Image Generation

**Authors:** Akansha Gautam, Aparna Bharati, Mayank Vatsa, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09304v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09304v1)

**Summary:** Text-to-image diffusion models often fail to suppress explicitly negated concepts, such as a lamp for "a desk without a lamp." We introduce T2I-NSI, a benchmark and metric for measuring negation sensitivity in text-to-image generation. It pairs each negated prompt with a canonical positive counterpart and factorizes negation by linguistic form (lexical/semantic, morphological, syntactic) and target type (objects, attributes, relations, compositions, and nested cases). The benchmark contains 759,...

---

### 50. A Stochastic Latent Variable Generalization of Joint-Embedding Predictive Architectures

**Authors:** Nikos Giakoumoglou, Paschalis Giakoumoglou, Tania Stathaki

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09302v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09302v1)

**Summary:** Joint-Embedding Predictive Architectures (JEPAs) predict the latent embedding of a target signal from a context signal, with an auxiliary variable z conditioning the predictor. Despite its prominent role in the original JEPA blueprint, the content of z has been carried by a fixed deterministic token in every prior instantiation, collapsing the genuinely multi-modal distribution over plausible completions to a point estimate. We present S-JEPA, which realises z as a proper stochastic latent varia...

---

## cs.LG

**50 papers**

### 1. On Agentic Manipulation Policies

**Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09892v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09892v1)

**Summary:** Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged ...

---

### 2. On the (non-)closedness of the set of ReLU networks

**Authors:** Eloi Martinet, Leon Bungert

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09887v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09887v1)

**Summary:** We prove that the set $\mathcal{N}_N$ of ReLU networks with one hidden layer and at most $N\in\mathbb N$ neurons is weakly closed in $W^{1,p}(Ω)$, for a bounded connected open set $Ω\subset\mathbb R^d$. Consequently, every coercive, weakly lower semicontinuous energy on this space attains its minimum over $\mathcal{N}_N$. This covers the Deep Ritz method with convex integrands, Sobolev training and Lipschitz learning. Moreover, as the weight decay parameter tends to zero, minimizers of the regul...

---

### 3. FlowMoP: Stochastic Multi-Person Motion Prediction

**Authors:** Aadya Agrawal, Ho Kei Cheng, Alexander Schwing

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09882v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09882v1)

**Summary:** Predicting the future motion of multiple people is inherently stochastic: the same observed history admits many plausible continuations depending on intent, coordination, and social context. Yet the dominant paradigm in multi-person 3D motion prediction remains deterministic, with existing methods producing a fixed number of outputs per agent. In contrast, we present a conditional flow matching framework that jointly generates diverse future motions for multiple agents, modeling both global traj...

---

### 4. Graded convolutional networks: scale invariance without the scale and robustness to unknown blur

**Authors:** Tanush Shaska

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09878v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09878v1)

**Summary:** The Gaussian jet of an image is a graded vector space: a dilation by $λ$ multiplies derivatives of order $k$ by $λ^{-k}$. Local graded convolutions are exactly homogeneous differential operators, and a local feature is dilation-invariant if and only if it factors through the scale-normalized jet or, without the scale, through the retraction onto the weighted sphere of the grading. Under unknown Gaussian blur the retraction changes only by a change of scale, whereas the scale-normalized jet acqui...

---

### 5. Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation

**Authors:** Xun Tu, Minghao Zou, Karthik Desingh

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09864v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09864v1)

**Summary:** Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons, is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation. Despite recent progress, reliably executing these tasks remains challenging because performance depends on complex robot-object and object-environment interaction dynamics. Existing approaches address this challenge either through model-based methods, which often re...

---

### 6. Flow-Guided Target-Space Alignment via Path Consistency

**Authors:** Ruizhi Yuan, Zeqiu Yu, Wei Gao, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09863v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09863v1)

**Summary:** Many multimodal alignment problems require mapping a source modality into a fixed space defined by a target modality, where the target space is not merely an intermediate embedding but is used directly for downstream analysis. In this setting, successful alignment should preserve both the global structure of the target distribution and the instance-level correspondence observed in paired source--target training data. Existing objectives typically address only part of this goal: contrastive losse...

---

### 7. Computer-Use Agents Are Embodied Generalists

**Authors:** Pranjal Aggarwal, Sean Welleck

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09847v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09847v1)

**Summary:** In many areas of AI, general-purpose models have increasingly replaced handcrafted methods and specialized architectures. We argue that embodied AI is poised for a similar shift. Our key claim is that embodied tasks can be formulated as interaction with digital software. Specifically, we build software that renders an agent's view of a physical environment on a screen and provides controls for acting in it. A computer-use agent (CUA) can then perform embodied tasks through the same screenshots a...

---

### 8. Fifty-Two Shades of Pig: What the UCR Archive Really Asks Classifiers to Do

**Authors:** Omar Swelam, Jaris Küken, Shi Bin Hoo, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09843v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09843v1)

**Summary:** The pigs were bleeding. That was the point of the experiment: could airway pressure reveal hemorrhage before it became critical? In the UCR Time Series Classification Archive, the de facto benchmark for Time Series Classification (TSC), the same recordings ask a different question: "which of 52 pigs produced this trace?". The dataset PigAirwayPressure is not an outlier. Although the archive is the standard benchmark, whether its tasks resemble the problems TSC is meant to solve has rarely been e...

---

### 9. Can Agentic Systems Close the Gap in Radiology with Production AI Tools?

**Authors:** Aubin Charley, Julien Khlaut, Charles Corbière, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09836v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09836v1)

**Summary:** Radiology AI has developed along two paths: specialized models that perform well on narrow tasks but cover few clinical findings, and generalist models that address a broader range of tasks but remain prone to hallucination and inaccurate measurements. Combining the two through agentic systems offers a route towards comprehensive radiology reporting, but published systems are tied to one modality or body part. We describe a radiology agentic framework that standardizes how an orchestrator calls ...

---

### 10. Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL

**Authors:** Aria Wong, Joshua Engels, Neel Nanda

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09828v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09828v1)

**Summary:** Reinforcement learning (RL) rewards are notoriously difficult to design and control, often leading to the model learning unintended behaviors such as reward hacking. One potential solution is to monitor for reward hacking and penalize it when detected; however, training against a monitor could lead to evasive behavior, and our general understanding of how to apply monitors effectively during training is limited. To study how best to use monitors to mitigate reward hacking, we introduce and open ...

---

### 11. Generative Latent Priors for Interpreting and Steering Protein Language Models

**Authors:** Daniel Hinjos, Lucía Urcelay

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09818v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09818v1)

**Summary:** Dominant methods for interpreting large models impose strong structural assumptions. Generative Latent Priors (GLP) are a complementary approach: a diffusion model that learns the distribution of a frozen model's activations directly, imposing no assumptions. We port GLP to ESM-2 activations (UniRef50) and evaluate it at two host scales (ESM-2-8M and -650M), both as a lens for protein representations and as a prior for editing them. Generation quality scales smoothly with depth and compute. As a...

---

### 12. Machine learning for lattice QCD

**Authors:** Gurtej Kanwar, Scott Lawrence, Alessandro Nada, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09817v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09817v1)

**Summary:** Machine learning (ML) methods have been explored as a means of optimizing lattice field theory calculations, with increasing interest in recent years. This chapter gives an introduction and summary to the use of ML methods to optimize lattice field theory without introducing any uncontrolled approximations. We focus on those directions which are clearly established as of late 2025, marking the 50th anniversary of the beginning of the study of lattice gauge theory. This chapter is a contribution ...

---

### 13. The Cost of Coverage: Conformalising Native Forecast Uncertainty for GB Wind Power

**Authors:** Carl Somers

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09815v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09815v1)

**Summary:** Uncertainty bands on wind forecasts help inform reserve sizing and commitments, but often fail to deliver their stated coverage. We apply conformal prediction to native bands to see what it adds and what it costs, comparing six forecasters, from ARIMA to a tabular foundation model, at two wind farms in Great Britain (GB) under operational conditions. We show that calibration repairs empirical marginal coverage with little or no Winkler Score penalty, but this apparent success conceals under-cove...

---

### 14. Scaling Graph Similarity Learning with Graph Neural Networks

**Authors:** Ahmet Tüzen, Helge Langseth, Kjetil Nørvåg

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09805v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09805v1)

**Summary:** Graph similarity computation is an important task in graph mining with many real-world applications, such as chemical compound analysis, program dependence comparison, and social network analysis. The problem is computationally challenging: Graph Edit Distance (GED) and Maximum Common Subgraph (MCS), which quantify the distance between graphs and identify their largest shared subgraph, respectively, are NP-hard to compute exactly. To address these computational challenges, Graph Neural Networks ...

---

### 15. Knowing When to Intervene: Causal Evaluation of AI Agents

**Authors:** Ayush Sawarni, Wenqian Xing, Tijana Zrnic, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09792v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09792v1)

**Summary:** Current evaluations of agentic AI systems primarily rely on benchmarks. However, the static nature of benchmarks makes them uninformative about the value of auditing interventions at deployment time. For reliable deployment, we often need to determine within an agent's trajectory whether or not to intervene, e.g., by verifying the agent's current output or steering it toward different behavior, using either human review or more costly models or time-consuming agentic supervision. The value of su...

---

### 16. Are These Programmers Ripe Enough to Eat? Evaluating How LLMs Handle Lexical Knowledge Conflicts in Translation

**Authors:** Dongxu Wu, Sara Court, Micha Elsner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09785v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09785v1)

**Summary:** External lexical resources can help large language models (LLMs) translate texts in low-resource languages and specialized domains, but these resources may conflict with models' prior lexical knowledge. To isolate this conflict, we construct a controlled Mandarin-to-English translation task in which familiar source words are assigned new meanings within and across semantic categories. We treat these prompt-supplied meanings as contextual knowledge (CK) and systematically evaluate the effects of ...

---

### 17. Quasipolynomial-Time Planning for Decodable POMDPs

**Authors:** Oliver Dobson, Varun Jog, Chun Hei Michael Shiu

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09778v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09778v1)

**Summary:** We study planning for finite-horizon partially observable Markov decision processes (POMDPs) with finite state, action, and observation spaces. Both exact and approximate planning are known to be computationally hard in this setting, so prior work has explored natural assumptions that make planning easier. Recent work [Golowich et al., 2022] gave quasipolynomial-time approximate planning algorithms for observable POMDPs. These are POMDPs whose observation channels satisfy an $\ell_1$-observabili...

---

### 18. From PAC bounds on the generalization error to PAC bounds on the parameter estimation error

**Authors:** Mihaly Petreczky, John Leth, Emma Lukacs, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09767v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09767v1)

**Summary:** Probably Approximately Correct (PAC) bounds on the generalization error (the difference between the empirical prediction error computed on the training data and its expectation) are an established tool in statistical machine learning, and there have been several extensions of these bounds to dynamical systems. In parallel, in recent years, there has been growing interest in finite-sample bounds for parameter estimation error in system identification. The latter bounds tend to be algorithm-specif...

---

### 19. A Tight Hierarchy for Chain of Thought

**Authors:** Thanh Le, A. Pavan, N. V. Vinodchandran

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09759v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09759v1)

**Summary:** Chain-of-thought (CoT) reasoning has emerged as a powerful paradigm for extending the computational capabilities of transformer-based models. A growing body of recent work has begun to uncover the fine-grained computational power of transformers augmented with CoT, as well as their connections to classical complexity theory.   In this work, we advance this line of research by establishing the first hierarchy theorem for CoT-based computation. Our main result shows that for any reasonable resourc...

---

### 20. Diffusion-free Score Matching for Exact Conditional Sampling

**Authors:** Thomas Wedenig, Robert Peharz

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09758v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09758v1)

**Summary:** The success of modern score-based generative models is largely driven by diffusion-based training, which learns a collection of time-indexed score fields corresponding to progressively noisier versions of the data distribution. While such models achieve impressive sample quality, leveraging them for sound probabilistic inference---particularly sampling from arbitrary conditionals of the model---remains challenging. This difficulty arises because conditioning information is only available for cle...

---

### 21. Safety Is $Π_1$, Provability Is $Σ_1$: One Framework for the Hugging Face Breach and OpenAI's Mathematical Proofs

**Authors:** Jinho Kang, Jinsook Kim

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09736v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09736v1)

**Summary:** OpenAI's agents breached Hugging Face in July 2026, and the same company released more than seven hundred AI-generated manuscripts of mathematical proofs in October 2026. The first event is read as a failure in security, while the second is read as a success in mathematics. We read both through the hybrid framework of our paper (Kim and Kang, 2026, arXiv:2611.01914), in which coding, proving, and learning from data are derivations by one and the same deductive mechanism, distinguished by the kin...

---

### 22. One Run Is Not Enough: A Monte Carlo Protocol for Evaluating LLM Reliability on Data Science Tasks

**Authors:** Wenqi Ni, Ozan Evkaya, Miguel de Carvalho

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09729v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09729v1)

**Summary:** Large language models (LLMs) have shown promise for automating data science workflows. Benchmarks such as DataSciBench (2026) and StatQA (2024) have advanced the evaluation of their capabilities across data science and statistical tasks. Assessing their reliability requires examining both the quality of their responses and their consistency across repeated runs, task types, and difficulty levels. With this aim, we introduce DS-QA, a benchmark comprising 100 data science and statistics questions ...

---

### 23. Fixed-point acceleration on Neural Wasserstein manifolds

**Authors:** Vitalii Aksenov, Sebastian Gutierrez Hernandez

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09723v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09723v1)

**Summary:** We propose a fixed-point acceleration method for optimization over probability measures, applicable to a variety of machine learning problems. We represent probability measures as pushforwards of a reference distribution through a neural network map and equip the parameter space with the induced pullback Wasserstein metric. This geometric structure allows natural gradient descent to be interpreted as a fixed-point iteration on a Riemannian manifold. We accelerate this iteration using Riemannian ...

---

### 24. Intent-Aware Caching for Efficient LLM Serving

**Authors:** Kazi Hasan Ibn Arif, JinYi Yoon, Dimitrios S. Nikolopoulos, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09715v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09715v1)

**Summary:** Modern LLM serving systems use prefix caching to accelerate multi-turn conversational workloads. They cache the key-value states of previous conversation prefixes and reuse them when subsequent requests share the same prefix, to avoid redundant prefill computation and reduce serving latency. However, achieving a high cache hit rate remains challenging because cache reuse depends on whether a conversation continues and how soon the next turn arrives. Our analysis of real workloads shows that user...

---

### 25. ICare-DT: a digital twin for continuous forecasting of intensive care patients

**Authors:** Yanke Li, Yahang Qi, Yumi Kim, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09712v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09712v1)

**Summary:** Digital twins of intensive care patients should update forecasts from new data and predict treatment responses, but few studies test whether routine records support either. We propose ICare-DT, a Transformer-based twin that updates a latent patient state hourly from new measurements without retraining. We trained it on 140,473 eICU-CRD stays to forecast vital signs crossing their training-set means. On test data, later forecasts beat the twin's own hour-6 forecasts of the same windows in all 12 ...

---

### 26. RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill

**Authors:** Dylan Johnston, Robert P. Smith

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09709v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09709v1)

**Summary:** RidgeFill shortens prefill by not computing most of a model's upper layers for the prompt. The lower layers run exactly up to a split; from the split layer's state a per-layer map predicts every later layer's input, and each late layer writes its cache from that prediction. The design follows YOCO and DeepSeek-V4.1-Flash, where the projection is trained into the model. RidgeFill retrofits it onto models that were never trained for it: the map is a ridge regression fitted once in closed form from...

---

### 27. Where Should Learning Live? Regret Analysis for Text, Parameter, and Joint Adaptation

**Authors:** Jungtaek Kim, Jaden Park, Jongwon Jeong, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09701v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09701v1)

**Summary:** Language-model systems can select prompts and parameter adapters repeatedly during deployment, using feedback to guide later choices. Earlier choices may change the context or environment inherited by later configurations. We study selection among preconstructed candidates and compare cumulative loss with the best fixed prompt--parameter pair used from the beginning. This excess loss separates into three terms: selection regret within the available family, the gap from restricting that family, a...

---

### 28. Verifier Noise Is a Temperature: Testing Tilt Predictions in Finite-Budget LLM-Guided Search

**Authors:** Xiaomeng Li

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09699v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09699v1)

**Summary:** LLM-guided search loops propose a modified candidate, score it, and keep it if it scores better. When both candidates are re-scored at every comparison, as in the minibatch acceptance gates of prompt optimizers, keep-if-better is a reversible Markov chain if the score difference is logistic and the mutation operator is reversible, and its stationary law is the mutation equilibrium tilted by exp(beta f). For any continuous symmetric noise difference the same tilt is the stationary law of a small-...

---

### 29. The Multiscale Single-Index Model: An MSE Analysis of Online SGD Dynamics

**Authors:** Gordon Dai, Joan Bruna

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09682v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09682v1)

**Summary:** We consider the Multiscale Single-Index Model (MSIM), first introduced by Oymak and Soltanolkotabi (2021), as a stylized model for hierarchical feature learning with scale separation. Each layer extracts a shared single-index feature at one physical scale and passes it to the next, giving a tractable setting in which to study how deep architectures learn local multiscale representations. Under non-degeneracy and delocalization assumptions on the link function and planted features respectively, f...

---

### 30. Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning

**Authors:** Chang Rajani, Luke Sebastien Marsden, Stephan Kunz, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09679v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09679v1)

**Summary:** Particle image velocimetry (PIV) reconstructs a flow field from the motion of tracer particles but the reconstruction quality is bounded by how well the flow structure of interest is resolved in the images. The acquisition position is typically fixed by the operator before the measurement. We cast camera placement as a sequential decision-making problem and train a reinforcement learning agent to control a 6-DoF manipulator equipped with a camera, enabling it to locate, frame and resolve a hydro...

---

### 31. Goodhart in the Planner: Sampling-Based Control Exploits Rewards Learned from Human Preferences

**Authors:** Soovadeep Bakshi, Apurba Bose

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09670v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09670v1)

**Summary:** Robots increasingly choose actions by searching against a reward model learned from human preferences, in model-predictive control or best-of-$N$ selection; we measure what this does to the true objective. On HalfCheetah and Hopper with crowd-sourced labels, and on Meta-World drawer-open and plate-slide with synthetic labels and blind labels from the two authors, harder MPPI search cuts true return by up to 76%: with human labels the drawer opens in 0 of 20 runs against 10 of 10 for the cloned p...

---

### 32. Online Causal Configuration for Networked Systems via Doubly Robust Steady-State Learning

**Authors:** Yuli Liu, Zhiheng Zhang

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09665v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09665v1)

**Summary:** Measurement exploration reveals how interacting local controllers behave but can alter the steady-state regime a network operator seeks to optimize. Exploratory rewards may therefore fail to identify a configuration's no-exploration value: under full exploration, identical logged distributions can conceal different target values. Identification requires accounting for both action-law mismatch and shifts in the steady-state context distribution. We introduce CAUSAL-UCB, which selects configuratio...

---

### 33. Breaking the Privacy Promise: Gradient Inversion Attacks on Federated Low-Rank Adapted Vision Transformers

**Authors:** Ritik K. Badiya, Siladittya Manna, Ashmit Sinha, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09652v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09652v1)

**Summary:** Parameter-efficient fine-tuning (PEFT) has been increasingly adopted to fine-tune pretrained models with low computational cost and is therefore also preferred in the federated learning paradigm to reduce computational and communication overhead. In this work, we investigate the sparsely explored problem of the risk of private data leakage in LoRA-adapted Vision Transformers (ViTs), where low-rank updates weaken the gradient signal available to a server with access to individual client updates. ...

---

### 34. TensorMutation: Learning Weight-Space Mutations of Deep Learning Models on Neural Graphs

**Authors:** Zaheed Ahmed, Philip Makedonski, Jens Grabowski

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09650v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09650v1)

**Summary:** Mutation testing for deep learning (DL) faces a cost-realism trade-off. The pre-training approach produces realistic but computationally expensive mutants, whereas existing post-training operators modify trained models efficiently but produce mutants that less closely resemble real faults. This study asks whether the trade-off is necessary: can the weight-space effect of a fault-informed pre-training mutation operator be predicted from a trained model, without retraining it? We answer this quest...

---

### 35. NAVE: A Normalized, Adaptive Conformer for Antarctic Whale Vocalization Detection

**Authors:** Matthias Nagl, Paul Primus, Gerhard Widmer

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09642v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09642v1)

**Summary:** Antarctic whale vocalization detection requires temporally localizing call boundaries in long underwater recordings and classifying them into predefined call types. Training reliable machine learning models for this task is difficult due to the variability and sparsity of whale calls in passive acoustic monitoring datasets. These difficulties are further amplified by time-varying noise that can mask whale calls and by site-specific ambient sound characteristics to which a trained model may not g...

---

### 36. Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters

**Authors:** Constantinos Karouzos, Nikolaos Aletras

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09634v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09634v1)

**Summary:** Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector select...

---

### 37. Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning

**Authors:** Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09625v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09625v1)

**Summary:** Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term memory and planning. In this work, we address the problem of long-term memory in MBRL by moving beyond the commonly studied paradigm of architecture design. We introduce Test-Time Model-B...

---

### 38. BiLoGo: Reducing the smoothing of localised responses in Transformer-based neural operators for sheet forming

**Authors:** Yingxue Zhao, Haoran Li, Haosu Zhou, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09621v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09621v1)

**Summary:** Trial-and-error FE simulation of sheet forming could be computationally expensive, neural-network-based learned simulators are used to accelerate design. These simulators should accurately capture localised responses, such as thinning around sharp radii or near ribs, which determine formability. Transformer-based neural operators propagate information efficiently across the mesh but tend to smooth such localised responses. This study develops BiLoGo, a Bipartite Local-Global learned simulator wi...

---

### 39. Contextual Search and Bilateral Trade with a Trace-Square-Root Potential

**Authors:** Romain Cosson, Federico Fusco, Anupam Gupta, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09615v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09615v1)

**Summary:** We present a unified potential method for contextual search and bilateral trade with one-bit feedback and obtain order-tight algorithms for both problems. Our framework starts from a Bayesian perspective in which the unknown target (for contextual search) and the unknown pair of valuations (for bilateral trade) are sampled from a known prior distribution. In that model, the decision maker bases its prediction on the posterior distribution, obtained by conditioning on feedback received in previou...

---

### 40. Know What You Need: Efficient Activation Checkpointing

**Authors:** Danyal Ahmed, Edouard Oyallon

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09614v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09614v1)

**Summary:** Large Language Model training is increasingly constrained by memory capacity. Activation Checkpointing reduces activation memory by avoiding storing selected activations during the forward pass and rematerializing them during backpropagation, thereby trading memory savings for additional computation. Although this technique is essential for scaling model training, rematerialization can be prohibitively expensive, particularly for Transformer linear layers. Approximate computation could reduce th...

---

### 41. Kernel-Based Learning of Analytic Operators and Parametric PDEs

**Authors:** Giovanni S. Alberti, Markus Holzleitner, Lorenzo Rosasco, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09612v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09612v1)

**Summary:** We study kernel-based learning of analytic operators from finite samples, with a focus on how the regularity of the target should determine the choice of the kernel. We establish embeddings of analytic operators into vector-valued reproducing kernel Hilbert spaces and derive finite-sample, high-probability guarantees that quantify the uncertainty due to random sampling: in the noiseless setting, suitable analytic kernels yield rates exponential in a fractional power of the sample size, while Sob...

---

### 42. ReplayAudit: Auditing Outsourced LLM Fine-Tuning via Sealed Records and Selective Replay

**Authors:** Yihan Xia, Wenxin Xu, Taotao Wang

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09607v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09607v1)

**Summary:** Auditing outsourced LLM fine-tuning requires checking an untrusted provider's training while controlling verification cost. Uniform sampling ignores training-time signals, while checking a suspicious record can require replaying several preceding steps. We present ReplayAudit, a telemetry-guided auditing system that seals training records before challenges and independently replays sampled intervals from sealed checkpoints. Loss changes and parameter-update norms guide stratified random sampling...

---

### 43. Coresets for Capacitated Clustering via Dual Concentration

**Authors:** Milind Prabhu, Chris Schwiegelshohn, Sudarshan Shyam, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09600v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09600v1)

**Summary:** We study coresets for clustering problems, focusing on the classical $k$-median and $k$-means objectives. A coreset is a small weighted summary of the input data that approximately preserves the clustering cost for every choice of centers. Such summaries are a central tool for scaling clustering algorithms to large datasets.   In this work, we consider the capacitated setting, where the clustering is subject not only to choosing centers but also to respecting prescribed cluster-size constraints....

---

### 44. Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression

**Authors:** Andras Szecsenyi, Thomas L. Lee, Vaisakh Shaj, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09598v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09598v1)

**Summary:** Private, personalised language models must run on local consumer devices, where large, frontier models cannot fit, and retaining long contexts is non-trivial. Sequential memory---the key-value (KV) cache---grows linearly with context length, quickly dwarfing the model itself: for Qwen3-1.7B-Base, 200,000 retained entries require 21 GiB, 6.6 times more than the model weights. Yet the KV-cache compression methods we measured fail beyond moderate compression ratios. We introduce Transformer-FSQ, ad...

---

### 45. Coordinatewise Epsilon for Adam under Heavy-Tailed Noise

**Authors:** Jeonseong Kim, Chenglin Fan

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09596v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09596v1)

**Summary:** Adam estimates second moments coordinatewise, but typically adds the same scalar $\varepsilon$ to every denominator. We study how this shared $\varepsilon$ affects convergence when noise and curvature vary across coordinates. Under coordinatewise finite-$p$ noise moments, $p\in(1,2]$, choosing $\varepsilon_i$ from the noise and curvature bounds for each coordinate attains the heavy-tailed $\ell_1$-stationarity benchmark $O(T^{-\frac{p-1}{3p-2}})$, matching the known optimal time exponent for smo...

---

### 46. Half-precision inference of AI weather prediction models: negligible loss of skill at a fraction of the cost

**Authors:** Stefan Siegert

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09573v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09573v1)

**Summary:** AI weather prediction models are released with 32-bit (fp32) weights and run in fp32 by default, although current GPUs compute much faster in 16-bit formats. We run five publicly available models -- Aurora, Pangu-Weather, FourCastNet, SFNO and FastNet -- on a single 16 GB GPU from 52 initial dates in 2024, in fp32 and with their networks in half precision (fp16), and verify the forecasts against ERA5. The physical state must stay in fp32: converting the whole model rounds it in physical units, w...

---

### 47. TurtLES: A Large-Scale Benchmark for Turbulent 3D Neural PDE Surrogates

**Authors:** Jarno Platenburg, Armand Kassaï Koupaï, Paola Cinnella, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09567v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09567v1)

**Summary:** Machine-learning surrogates are increasingly used to accelerate computational fluid dynamics, yet progress is limited by the lack of benchmarks capturing realistic, time-dependent turbulent flows. We introduce TurtLES, a 14 TB dataset of 3D turbulent cylinder wakes in the shear-layer transition regime, computed via high-fidelity implicit large-eddy simulations. The dataset contains 400 trajectories of 400 time steps each, with 3-11 million points per frame, spanning variations in geometry, Reyno...

---

### 48. Solver-Free Decision-Focused Learning via Neural Optimization Layers for Edge Selection

**Authors:** Xinda Zheng, Frits de Nijs, Edward Lam

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09560v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09560v1)

**Summary:** Decision-focused learning trains prediction models to improve downstream decisions, but many methods require costly solver calls or optimal-solution labels. We propose a solver-free decision-focused learning framework for NP-hard edge-selection problems with uncertain parameters in the objective, the constraints, or both. A neural optimization layer is first trained without solution labels, using problem objectives and constraint penalties. Graph-informed edge scoring and iterative refinement en...

---

### 49. Optimal Regret for Profit Maximization in Bilateral Trade

**Authors:** Matteo Castiglioni, Anna Lunghi, Alberto Marchesi

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09558v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09558v1)

**Summary:** Learning to profit from trade requires learning both sides of a market: what a seller is willing to accept and what a buyer is willing to pay. We study repeated bilateral trade, where an intermediary posts a purchase price to a seller and a sale price to a buyer whose valuations are drawn from an unknown joint distribution. Trade occurs only if both parties accept their respective prices, in which case the intermediary earns the difference between the two prices. The intermediary observes only w...

---

### 50. Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs

**Authors:** Peiyu Zhang, Heng Ping, Shinibali Bhattacharyya, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09554v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09554v1)

**Summary:** Long-context language models often neglect information in the middle of the input, a phenomenon known as "lost-in-the-middle". Part of this gap may stem from the long-range decay of rotary position embedding (RoPE), which weakens the positional signal between distant tokens. Existing input compression deletes low-importance tokens, and attention reweighting acts only after RoPE has weakened this signal. RoPE-level methods modify positions directly but apply the same remapping to every query. To ...

---

## cs.NE

**50 papers**

### 1. Bridging Spiking and Continuous Dynamics in Spiking Neural Networks: A Muscle-Inspired Model

**Authors:** Maryam Soltani, Philip N. Garner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09295v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09295v1)

**Summary:** Transforming the spike trains produced by spiking neural networks (SNNs) into continuous signals through biologically inspired mechanisms remains an open challenge in generative and regression tasks. In biological systems, a similar transformation occurs when muscles integrate neural spikes to produce smooth, coordinated movements. Inspired by this mechanism, we introduce a muscle-response model, a biologically motivated dynamical layer that converts spike trains into continuous representations....

---

### 2. OMCDE: Opposition-based Multi-Stage Matrix-Based Competitive Differential Evolution

**Authors:** Mohammad Sarhangzadeh, Shahryar Rahnamayan, Doruk Oner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09167v1)

**Summary:** Differential Evolution has proven to be an effective algorithm for continuous global optimization, but it's modern high-performing variants often introduce additional complexity and computational cost. We propose OMCDE, a matrix-based competitive Differential Evolution algorithm that aims to improve optimization performance while maintaining computational efficiency. The proposed approach integrates competition-driven search dynamics, adaptive behavior between optimization stages, and opposition...

---

### 3. Circuit Theory-Informed AI for Condition Monitoring in Power Electronics

**Authors:** Yubo Song, Pascal A. Schirmer, Subham Sahoo

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09141v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09141v1)

**Summary:** Artificial intelligence for power electronics is evolving toward a deeper comprehension of system intrinsic behaviors and dynamics. As a novel integration of neural computation and electric circuits, spike-based neuromorphic computing offers promising potential in high energy efficiency and adaptability for data-driven applications. Building on the latency-coding principles, this article proposes a framework for data-light condition monitoring that relies solely on three-phase AC current measure...

---

### 4. Two-Layer Evolutionary Scheduling for Machine Learning Jobs in Multi-Cluster Environments

**Authors:** Jingyuan Xu, Changwu Huang, Lemeng Pan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09093v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09093v1)

**Summary:** The rapid growth of large-scale machine learning (ML) workloads has led to unprecedented demands on GPU cluster scheduling systems. However, existing heuristic schedulers struggle to handle the complexity and dynamics of multi-cluster GPU environments, often leading to load imbalance, long queuing delays, and poor alignment to business objectives. This paper formulates the ML scheduling problem in multi-cluster GPU environments as online multi-objective optimization that minimizes the average an...

---

### 5. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

**Authors:** Qile Jiang, George Em Karniadakis

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08483v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08483v1)

**Summary:** LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decod...

---

### 6. Invariance before structure: two modes of emergent compression in representation learning

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07952v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07952v1)

**Summary:** Learned representations show striking invariance across biological and artificial neural networks, with different substrates and variations driven by drift, heterogeneity and initialisation. To understand this invariance, we propose Emergent Adaptive Representation Learning (EARL), a framework that distinguishes two modes of emergence in learned representations: state-space compression, where a learned representation gains predictive power over its own future beyond what the network's units can ...

---

### 7. Projection-Free Gradient Tracking Neurodynamic for Distributed Nonnegative Sparse Optimization

**Authors:** Juntao Li, Qihang Guo, Deyuan Meng

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07643v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07643v1)

**Summary:** This paper proposes a continuous-time, projection-free neurodynamic system based on gradient tracking for distributed nonnegative sparse optimization. Unlike traditional methods, our approach avoids projecting states onto the feasible set. Instead, it employs gradient tracking to estimate average gradients under heterogeneous costs, coupling primal and dual dynamics such that feasibility and sparsity emerge naturally from the equilibrium conditions. The system ensures unique solutions through a ...

---

### 8. When Does Blockwise Additivity Break? Diagnosing and Repairing the Additive Assumption in Distillation-Based Architecture Search

**Authors:** Yuefeng Xu, Jun Yu

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07487v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07487v1)

**Summary:** Blockwise distillation methods for architecture search, such as DNA, DONNA, LANA and Puzzle, score each candidate replacement block in isolation and assemble a child network by minimizing the sum of per-block scores. We test this additive assumption on DeiT-S and DeiT-B with seven replacement blocks per layer, seven block-latency budgets from 70% to 40%, three fine-tuning seeds and paired bootstrap confidence intervals. (i) At mild compression the additive integer linear program (ILP) is close t...

---

### 9. Learning Time-Varying Connectomes for Stable Behavior Across Development

**Authors:** Christof Fehrman, Jacob J. Morra, Eva A. Naumann

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06895v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06895v1)

**Summary:** Neural circuits must maintain functionality to drive effective behavior while their size, topology, geometry, and intrinsic dynamics change across development. To model developing visuomotor circuits and behavior, we investigated whether a single compact generative encoding could produce functional recurrent controllers across such changes. Building on the HyperNEAT algorithm, we represented this program as a compositional pattern-producing network that received developmental time as an input to...

---

### 10. Adaptive Multi Mode: Budget-Aware Routing of Optimizers By Online Landscape Probes

**Authors:** Benjamin Jacob Bodner

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06879v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06879v1)

**Summary:** The best classical optimizer for a continuous black-box problem depends on its budget and landscape. Existing routers decide from the dimension and budget, past improvement or features fitted to one benchmark, and few test an optimizer's implicit assumptions online. AMM (Adaptive Multi Mode) routes a known budget among quasi-Newton, trust-region, coordinate, multistart and evolution-strategy optimization engines with online probes of curvature, plateaus, separability, kinks, basins and fractal s...

---

### 11. SpikePose: Lightweight Video Human Pose Estimation

**Authors:** Yunhao Huang, Kaushik Bhargav Sivangi, Tianyi Yu, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06594v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06594v1)

**Summary:** Efficient video human pose estimation must balance localisation accuracy, motion quality, and energy cost. We present SpikePose, a lightweight video pose estimator that pairs a frame-reset, single-step spiking encoder with motion-aligned heatmap memory (MAM). The encoder supplies per-frame spatial evidence, while MAM estimates joint displacement, aligns historical heatmaps, and adaptively fuses them with current predictions. By confining temporal reasoning to a compact, lightweight module outsid...

---

### 12. From Admission to Retention: Predicting Durable Offspring in Quality-Diversity Search

**Authors:** Corrado Calamita, Matteo Mendicini, Luca Ferrari, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06522v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06522v1)

**Summary:** Automated failure discovery can be framed as a diversity problem: the objective is to expose distinct ways a system fails rather than a single critical adversarial case. Yet uniform parent sampling provides no way to allocate search effort toward individuals likely to produce durable archive contributions. We study this credit assignment problem in an unstructured Quality-Diversity (QD) archive, testing whether signals available before an individual has reproduced distinguish offspring that mere...

---

### 13. Multi-Resident Data Association in Smart Homes via MDP Modeling and Behavior Cloning

**Authors:** Xi Chen, Julien Cumin, Fano Ramparany, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06296v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06296v1)

**Summary:** Ambient sensors offer a privacy-preserving solution for activity recognition in smart homes, yet they face a critical challenge in multi-resident environments known as Data Association, which aims to identify the resident triggering a specific anonymous sensor event. Existing approaches fundamentally fail to maintain global consistency by often yielding conflicting associations for silent residents. Additionally, these methods frequently suffer from severe trajectory fragmentation caused by the ...

---

### 14. Explainable Anomaly Detection in 5G Networks through Continuous Time Graphs

**Authors:** Thomas Hoger, Philippe Owezarski

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06225v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06225v1)

**Summary:** 5G networks increasingly resemble distributed systems in their design. It then becomes crucial to move beyond traditional network-based detection methods and to explore alternative approaches. In this work, we propose a formalization of 5G network exchanges as a dynamic graph, on which we apply techniques from the field of graph-based learning to detect anomalies effectively. This representation allows for fine-grained analysis of packet-level semantic content, while simultaneously capturing seq...

---

### 15. Mobility-Aware Mobile Edge Computing for Energy-Balanced Data Collection in IoT-Enabled Underwater Sensor Networks

**Authors:** Nguyen Thi My Binh, Do Dinh Hoan, Tong Tien Manh, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06186v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06186v1)

**Summary:** Underwater wireless sensor networks (UWSNs) face critical challenges in energy imbalance, connectivity, and data collection due to harsh environments. To address these issues, this paper focuses on the problem is how to achieve energy-balanced data collection in IoT-enabled UWSNs with a mobility-aware mobile edge computing (MEC), named MECEBDC. Unlike existing approaches, the proposed scheme jointly optimizes energy-aware clustering, cluster head selection, and AUV-assisted data collection. Furt...

---

### 16. Neural networks and games

**Authors:** Philip R. Neary

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05706v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05706v1)

**Summary:** Hopfield neural networks and noncooperative games provide seemingly different approaches to understanding how collective outcomes emerge from local interactions. In a neural network, individual units adjust their states according to local signals; in a game, players choose actions to maximise individual payoffs. I establish an exact equivalence between symmetric binary Hopfield networks and binary-action games that admit a quadratic potential. The equivalence identifies stable network configurat...

---

### 17. Learning Behaviorally Relevant Dynamics in Multimodal Neural Recordings

**Authors:** Parastoo Azizeddin, Eray Erturk, Maryam M. Shanechi

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05167v1)

**Summary:** Multimodal neural data can enable a more complete understanding of brain dynamics underlying behavior. Modalities such as spiking activity, local field potentials (LFPs), and behavior capture diverse spatiotemporal aspects of brain processes, yet prior neural-behavioral models that separate sources of variability rely on a single neural modality. By leveraging these complementary strengths, multimodal neural fusion can provide a unified, rich representation of brain-behavior processes and addres...

---

### 18. Solving the Nonlinear Westervelt Equation in Ultrasound Propagation Using Physics-Informed Neural Networks

**Authors:** Luke Oluwaseye Joel

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05130v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05130v1)

**Summary:** Modeling the nonlinear acoustic wave propagation in biological tissues needs accuracy, especially in ultrasound imaging and therapeutic applications. The 1D Westervelt equation, \( p_{xx} - p_{tt} + γ\, p_{ttt} + η\,(p^{2})_{tt}=0, \) could be used to describe a finite-amplitude ultrasound propagation in these tissues. This equation accounts for nonlinearity, \(η\), and attenuation, \(γ\). To solve this equation, we observe that traditional solvers may struggle to do so correctly. This is due to...

---

### 19. Refined CMA-ES for CEC 2026 Bound-Constrained Single-Objective Optimization

**Authors:** Adam Stelmaszczyk, Rafał Biedrzycki, Jarosław Arabas

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.04620v1) | 📄 [PDF](https://arxiv.org/pdf/2611.04620v1)

**Summary:** We present a simplified and parameter-adjusted variant of CMA-ES designed for the CEC 2026 Bound-Constrained Single-Objective Optimization competition. Unlike typical algorithmic developments that increase complexity by adding mechanisms, Refined CMA-ES systematically removes components that do not improve performance, such as the flat-land escape, while retaining standard features that provide measurable benefits. Adjusting key parameters (population size and initial step-size) yields substanti...

---

### 20. Structured Visual Landscape: Generating Preferred Representations in Biological and Artificial Neural Networks

**Authors:** Yusong Zhao, Edgar Y. Walker, Hao Wang, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03597v2) | 📄 [PDF](https://arxiv.org/pdf/2611.03597v2)

**Summary:** Understanding how neurons respond to visual stimulus is an important question in both deep learning and neuroscience. It has significant implications for enhancing the interpretability of black-box artificial neural networks and for understanding the visual representation in the human brain. We propose a structured visual representations landscape and design an activation-based prior that allows us to effectively regularize the landscape with activations from brain regions or neural network unit...

---

### 21. Exact Fusion of Softmax Attention Heads Can Require Exponentially Many Atoms

**Authors:** Hiroyasu Usami, Keisuke Hara, Ayato Tsuboi, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02943v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02943v1)

**Summary:** Fusing independently normalized attention heads can increase the number of explicit key-value entries, or atoms, needed to preserve their output. We prove a sharp separation for $W_d(q)=\sum_{j=1}^dσ(q_j)$: its $d$ two-atom heads use $2d$ head-atom terms, whereas its minimum single-head representation has exactly $2^d$ atoms, even with arbitrary fixed replacement keys, scalar values, and positive masses. The same lower bound holds for every fixed uniform error below $1/2$ on $\mathbb R^d$, and t...

---

### 22. Iterated Narrow Networks: Turing Completeness at Width 4 on Convex Input Spaces and the Complexity of Verification

**Authors:** Olivier Bournez, Johanne Cohen, Adrian Wurm

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02840v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02840v1)

**Summary:** We study the iterates of a fixed ReLU network $N$ of width 4, that is, the discrete-time system $x_{k+1} = N(x_k)$ on $[0,1]^4$. Equivalently, $x_k$ is the output of a weight-tied network made of $k$ copies of $N$, or of a recurrent network with no external input, started at $x_0$. We prove that every deterministic Turing machine $M$ admits such a network $N_M$. The network can be constructed in polynomial time from $M$. Each iteration has depth $\mathrm{poly}(|M|)$. The iterates of $N_M$ simula...

---

### 23. HyVox: Rethinking Low-Power Voice Intelligence towards Neuromorphic-von Neumann Edge Computing

**Authors:** Snehasis Addy, Eduardo Calle Ortiz, Prashant Shenoy, et al.

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.03735v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03735v1)

**Summary:** We present HyVox, a hybrid neuromorphic--von Neumann system for low-energy open-set speaker identification under tight energy budgets. HyVox splits the workload at the speaker embedding. A neuromorphic processor embeds the speech with sparse, event-driven computation, and a von Neumann microcontroller holds the speaker gallery and makes every decision: it scores queries by cosine similarity, rejects unknown speakers, and enrolls new users by writing a prototype, with no weight update. On the neu...

---

### 24. Exposure-Length Trade-off Optimization for Obstacle-Aware Intrusion Paths in Heterogeneous Wireless Sensor Networks

**Authors:** Nguyen Thi My Binh, Ho Viet Duc Luong, Nguyen Tuan Nghia, et al.

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.01606v1) | 📄 [PDF](https://arxiv.org/pdf/2611.01606v1)

**Summary:** Barrier coverage is a key paradigm for intrusion detection and surveillance in IoT-enabled heterogeneous wireless sensor networks, where monitoring quality depends not only on the existence of sensing barriers but also on the detectability of feasible crossing paths. In this paper, we study the obstacle-aware maximal exposure path planning problem in heterogeneous sensor fields under truncated omni-directional sensing and line-of-sight occlusion. Unlike conventional maximal exposure formulations...

---

### 25. Is Newborn Wiring Special? Separating Wiring from Weight Placement in Connectome Reservoirs

**Authors:** Riccardo Bertamini, Corrado Calamita, Ramiro Pascual, et al.

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.01213v1) | 📄 [PDF](https://arxiv.org/pdf/2611.01213v1)

**Summary:** Reservoir computing offers a way to study the brain's wiring before it is even trained. The recurrent network remains fixed, while only a linear readout is trained. The human connectome is found to perform better than randomly rewired versions of itself, suggesting that biological wiring is special. To understand the source of this advantage, a mathematical graph-theoretic decomposition is introduced. Rewiring a weighted network changes both the regions that are connected and the weights assigne...

---

### 26. A Tool in the Forward Pass: Frozen Tape Modules as Layers of a Small Language Model

**Authors:** Michael Granitzer, Saber Zerhoudi, Mohammad Al-Maamari, et al.

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.00783v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00783v1)

**Summary:** Calling a tool through generated text adds decoding steps, even when the computation itself is short. We study an alternative: a small neural module that runs inside a language model's forward pass. A learned writer turns hidden states into a symbolic tape, a short sequence of discrete symbols that encodes the computation. The module, trained separately and then frozen, reduces the tape to a result, and a learned reader returns that result to the model. We evaluate arithmetic and object tracking...

---

### 27. Boosted Physics-Informed Neural Networks for Solving Homogeneous and Non-Homogeneous Lane-Emden Type Equations

**Authors:** Luke Oluwaseye Joel

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.00701v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00701v1)

**Summary:** The Lane-Emden Equation is a class of nonlinear differential equations commonly used to model phenomena in astrophysics and mathematical physics, such as stellar structure and thermal behavior in polytropic gas spheres. This study presents a novel hybrid framework that integrates Physics-Informed Neural Networks (PINNs) with boosting methods to enhance the accuracy and robustness of solutions for Lane-Emden type differential equations. Standard PINNs leverage physical laws encoded within the los...

---

### 28. From Connection Loss to Collision: Closed-Loop Fault Assessment of a Fly-Connectome SNN

**Authors:** Shuchao Gao

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.06940v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06940v1)

**Summary:** The public release of the complete adult fruit-fly brain connectome enables brain-scale spiking-network studies, motivating closed-loop assessment of connection loss. We test a connectome-derived controller in synthetic pursuit-escape and check record consistency. Across 576 test episodes in paired campaigns, the baseline mapping at 50% connection-row deletion yields 11/48 proportional and 0/48 relay collisions by 1 s, despite paired P/R trigger/burst schedules. The prespecified secondary relay-...

---

### 29. Proof-Carrying Evolution: Black-Box Search, White-Box Flight

**Authors:** Amit Jain, Sergio Sanchez-Hurtado, Victor Rodriguez-Fernandez, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42043v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42043v1)

**Summary:** We study whether a language model can help design controllers whose behavior can be formally checked. In proof-carrying evolution (PCE), a search proposes controllers together with their certificates. Their mathematical forms are fixed; a proposer chooses their numerical parameters together. Certificate checks guide selection, and only a certified candidate can be returned. The deployed artifact is a control law and its certificate; the language model is used only during design. We compare four ...

---

### 30. In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents

**Authors:** Xuning He, Kai Fan, Runyu Zhang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41291v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41291v1)

**Summary:** Long-horizon LLM agents play an important role in solving complex and sustained tasks, with ever-growing interaction contexts. However, these accumulated contexts will raise substantial computational cost and obscure key decision-relevant evidence. Existing methods typically train external compressors or context-management agents to rewrite context as shorter hard-token sequences, but such external selection may not align with the LLM's evolving representation and is necessarily lossy. In this p...

---

### 31. Input-dependent Neuromodulation Enhances Mixed-Signal Neuromorphic Hardware

**Authors:** Aashman Mehta, AbdelQader AlKilany, Dan F. M. Goodman, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41265v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41265v1)

**Summary:** Gating mechanisms allow a fixed neural network to adapt its computation to the current input by dynamically modulating its effective parameters. In the brain, neuromodulation uses this principle to move neural circuits between dynamical regimes, and deep learning exploits input-dependent gating, e.g., in gated recurrent networks and self-attention. Input-dependent modulation has also recently been shown to improve spiking neural networks, with particularly strong benefits in small, parameter-lim...

---

### 32. Memory and Recall of Color Images Using Neural Networks-1 - The Cue-Ball Model based on the Associative Memory Mechanism -

**Authors:** Hiroshi Inazawa

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41108v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41108v1)

**Summary:** This paper presents a neural network model for storing and recalling color images of different sizes using the Cue BallRecall Net systems [1,2,3,4,5]. The Cue Ball system consists of a Recall Net composed of multiple memory neurons each responsible for memorizing a single, distinct memory and a large number of neurons that represent image patterns. The images used in this study [6] consist of ten images(see Appendix). The pixel values of these images were converted into digital values and used f...

---

### 33. Local Budget Benefits, Population Commitment, and Solver Performance: A DGO Case Study with Controlled DE Transfer

**Authors:** Shiqi Li

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41099v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41099v1)

**Summary:** An evaluated candidate can improve a local search step, alter the population used by later steps, and affect a solver's final result. We distinguish these three questions using Da Gou Gun Optimization (DGO), a population optimizer designed for this study. Its JQ100 configuration evaluates an interpolation candidate during a two-sided probe. We define local budget value, population commitment effects and complete-policy performance, and give an exact example in which a locally better commitment l...

---

### 34. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

**Authors:** Jiongfan Yang, Weichen Fan, Haiwen Diao, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40647v1)

**Summary:** Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introduce SpecSlot, a pixel-space rectified-flow Transformer that decouples output detail from the length o...

---

### 35. Dynamic Powergrid Optimization with FPGA-based Neuromorphic Higher-order Ising Machines

**Authors:** Saptarshi Maiti, Shantanu Chakrabartty, Chetan Singh Thakur

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40522v1)

**Summary:** The advent of large, high-density FPGAs such as the AMD Versal enables efficient hardware implementation of neuromorphic Ising machines, unlocking unprecedented performance for complex combinatorial optimizations. A critical application for this computing paradigm is dynamic powergrid optimization, specifically Distribution Network Reconfiguration (DNR), which seeks to mitigate severe resistive losses and reduce electricity costs by optimizing network switch configurations in real time. This pap...

---

### 36. AutoHebb: Self-Modifying Neural Networks that Zero-Shot Infer and Continually Learn

**Authors:** Daniel Levine, David van Dijk, Kenneth Kay

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40757v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40757v1)

**Summary:** Humans and animals have a unique capacity to generalize and learn in novel circumstances, including "0-shot" inference (ZI) and continual learning (CL) -- two powerful cognitive abilities. Despite this importance, efforts to model ZI and CL are seriously limited in several ways. First, existing models typically lack components critical to ZI and CL in the brain, namely, strong inductive biases (for ZI) and autonomous control of learning (for CL). Second, models can be less tractable to analysis ...

---

### 37. HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization

**Authors:** Jianghan Zhu, Cong Zhang, Ni Zhang, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40023v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40023v1)

**Summary:** Automatic operator design (AOD) has increasingly adopted large language models (LLMs) to generate problem-specific search and variation operators for multi-objective combinatorial optimization (MOCO). Yet most methods evolve the operators while leaving the process that discovers them fixed. This limits adaptation as new Pareto trade-offs and operator interactions change where and how the search should proceed. We introduce HEMO, which makes the AOD harness itself a self-evolving optimization tar...

---

### 38. AI at a Turning Point: From ChatGPT through Neural Networks to Neuromorphic AI

**Authors:** Volker Kempe

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39796v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39796v1)

**Summary:** The tension between the established technologies of connectionist AI and their neuromorphic challengers is attracting growing attention, above all because of the enormous energy demand of the former and the low power consumption of the latter. Developing and running large AI models consumes gigawatt- to terawatt-hours of energy, while the human brain operates on a continuous 20 watts. Spiking neural networks (SNNs) counter this energy demand with a frugal approach and bring elements of self-orga...

---

### 39. Diagnosing Optimizer-Landscape Interaction via Representation in Subset Selection Multitasking: Evidence from Piano Fingering

**Authors:** Ananda Phan Iman, Tingyang Wei, Chang Wook Ahn

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39779v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39779v1)

**Summary:** Continuous relaxations are commonly used as an encoding scheme for evolutionary multitasking optimization (EMTO), allowing heterogeneous tasks to be optimized within a unified search space. However, these continuous representations fundamentally reshape the induced fitness landscape, and their impact on optimization behavior and knowledge transfer remains underexplored. In this work, we bridge the gap by analyzing the interaction between the representation-induced fitness landscape and optimizer...

---

### 40. Hardware-Aware Model Inversion in Memristive Spiking Neural Networks

**Authors:** Pablo Sorrentino, Fernando M. Quintana, Erika Covi, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39688v2) | 📄 [PDF](https://arxiv.org/pdf/2610.39688v2)

**Summary:** Hardware-accelerated spiking neural networks (SNNs) implemented on memristive crossbar arrays offer significant gains in energy efficiency, while device variability and analog noise are sometimes assumed to hinder information extraction. However, whether these hardware effects improve, preserve, or degrade privacy after deployment remains largely unexplored. Therefore, we ask whether model-inversion leakage characterized on an SNN remains representative after the same model is mapped to a non-id...

---

### 41. GC-LIF: Spiking Group-Equivariant Neural Network With Group-Coupled Membrane Dynamics

**Authors:** Nhan Trong Luu, Duong Trung Luu, Thang Cong Truong

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39601v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39601v1)

**Summary:** Spiking neural networks (SNNs) promise event-driven, low-power inference, but on vision tasks they still acquire rotation invariance only through data augmentation. Group-equivariant CNNs build such symmetries into the architecture, yet a faithful spiking analogue is missing: a leaky integrate-and-fire (LIF) neuron placed after a $G$-equivariant convolution can break equivariance through its membrane recurrence. We give a necessary and sufficient condition for this not to happen. The layer is eq...

---

### 42. FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss

**Authors:** Hina Otake, Shinei Arakawa, Keitaro Tanaka, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39423v1)

**Summary:** Formula-Driven Supervised Learning (FDSL) enables vision pre-training without real images, but existing methods cast pre-training as classification on discretized labels, discarding continuity in the generative process. We propose Formula-Driven Supervised Metric Learning (FDSML), which derives relational supervision from image-generation parameters beyond discrete class labels. FDSML combines FineFractalDB, our refined fractal dataset with higher intra-class variation and more stable structures...

---

### 43. MulClip: A table-free activation function with monotonic and folding regimes for reservoir computing on microcontrollers

**Authors:** Guren Matsumura, Masato Takemoto, Shinzo Koyama

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.39343v1) | 📄 [PDF](https://arxiv.org/pdf/2610.39343v1)

**Summary:** This letter proposes MulClip, a lightweight activation function for reservoir computing (RC) on microcontrollers (MCUs). In a ring reservoir, a representative sparse RC topology, multiply-accumulate operations are few, and evaluating tanh accounted for 75% of the state-update time on a Cortex-M4. MulClip introduces curvature into the response using only comparison, absolute value, multiplication, and subtraction, and places its clipping threshold not at the extremum but at the point where the re...

---

### 44. State-Dependent Memristor Dynamics for Device-Informed Spike-Timing-Dependent Plasticity in Spiking Neural Networks

**Authors:** Samiur Rahman Khan, Saifur Rahman Sabuj

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2611.00119v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00119v1)

**Summary:** This work investigates device-informed spike-timing-dependent plasticity (STDP) in spiking neural networks using a literature-derived threshold-memristor model. Local STDP commands determine programming polarity and a programming coordinate for state-dependent conductance updates in the first fully connected layer, while a backpropagation-trained readout performs classification. HSPICE simulations characterize thresholded, polarity- and state-dependent device dynamics and differential crossbar m...

---

### 45. The Power Watershed as a Differentiable Segmentation Layer

**Authors:** Galia Akl, Laurent Najman, Hugues Talbot

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38516v1)

**Summary:** Can a Watershed transform, the classical tool of morphological segmentation, be placed at the end of a deep network and trained through? The Power Watershed (PW) is the limit of the seeded Random Walker (RW) as p grows to infinity with edge weights raised to the power p. At every finite p the RW solves a sparse positive-definite linear system and is exactly differentiable with respect to the edge weights and the unaries through one adjoint solve; its multi-label form costs one right-hand side pe...

---

### 46. SpikeAD: Toward Multiplication-Free Spike-Controlled Neuromorphic Architecture for Energy-Efficient Small Object Detection

**Authors:** Zhifan Song, Haralampos-G. Stratigopoulos

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2611.00112v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00112v1)

**Summary:** Energy-constrained aerial platforms require accurate object detection under strict power and latency budgets, yet conventional inference remains bottlenecked by multiply-accumulate (MAC) operations. While spiking neural networks (SNNs) offer bio-inspired efficiency, many SNN detectors retain hybrid MACs in intermediate layers, or use spike-driven inference where multi-level spikes are interpreted as repeated binary events. We propose SpikeAD, a direct-trained spike-controlled neuromorphic aerial...

---

### 47. FPGAFly: A 166.7k-Neuron Fruit-Fly Connectome on One FPGA via Deferred Spike Expansion and Shared-Codeword States

**Authors:** YE Ziyang

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38118v1)

**Summary:** Synapse-resolution fruit-fly (Drosophila) connectomes enable neuron-by-neuron simulation of entire insect nervous systems, yet whole-brain models still require computationally demanding software or multiple neuromorphic chips, and single FPGAs support only small or statistical networks. Scaling to the full connectome, per-synapse spike expansion scales queue traffic with fan-out up to 11.2k, while 41-bit neuron states require 6.83 Mbit, exceeding the 6.27 Mbit on-chip block static RAM (BSRAM) of...

---

### 48. SLICE-CiM: Selective Layer-wise Inference Control Engine with Confidence-Based Early Exit for SRAM based Digital Compute-in-Memory

**Authors:** Pratham Sharma, Mohd Faisal Khan, Santosh Kumar Vishvakarma

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37601v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37601v1)

**Summary:** Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3). To address these, we present four synthesizable peripheral blocks: a Flush-Merge Enable (FME) controller, a Confidence-Based Early-Exit (EE) module, a Precision Register wit...

---

### 49. GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting

**Authors:** Joseph Natter, Long Vu, Yifan Zhang, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37598v1)

**Summary:** Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. E...

---

### 50. GNBG-C: A Unified and Configurable Benchmark Generator for Constrained Continuous Optimization

**Authors:** Ali Ghasemzadeh, Erfan Babakhani, Armin Khosravi, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37590v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37590v1)

**Summary:** Many real-world optimization tasks are governed not only by what should be optimized, but also by what is allowed: a solution must first satisfy physical, operational, safety, budgetary, or structural requirements before its objective value becomes meaningful. Yet benchmark design for constrained continuous optimization often treats these restrictions as fixed properties of predefined test instances. Existing generators and benchmark suites provide essential foundations for reproducible comparis...

---

## q-bio.NC

**50 papers**

### 1. Path-dependent triage: Early judgments lead conversational AI chatbots to miss mental-health emergencies

**Authors:** Veith Weilnhammer, Raymond Dolan, Lennart Luettgau, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09647v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09647v1)

**Summary:** People increasingly bring mental-health concerns to consumer AI chatbots. In these conversations, clinically relevant information rarely arrives all at once. Instead, it unfolds over multiple turns, often in response to the questions the chatbot asks. Recognizing risk therefore depends on how a chatbot integrates newly disclosed information (inference) and on the questions it asks on each turn to elicit this information (context-seeking). Here we evaluated the conversational triage performance o...

---

### 2. A hair-thin implant opens the entire depth of the mouse brain to revisiting the same structures at subcellular resolution

**Authors:** Miroslav Stibůrek, Tomáš Pikálek, Petra Ondráčková, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09481v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09481v1)

**Summary:** Ultrathin multimode-fibre endoscopes provide minimally invasive access to subcellular structures throughout the depth of the mouse brain. Here we introduce a chronically implantable interface with a diameter of 144 μm, about the thickness of a human hair, that extends this capability to longitudinal imaging, enabling repeated access to the same fine structures over extended periods. The system supports weeks-long tracking of individual dendritic spines, allowing quantitative comparison of their ...

---

### 3. Decoding spatial and semantic information from large-scale visual cortical activity for natural-movie reconstruction

**Authors:** Yukai Huang, Haoyu Albert Wang, Jiawei Zhang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08887v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08887v1)

**Summary:** Reconstructing natural visual experience from cortical population activity is a central challenge in neural decoding, particularly for calcium imaging, where signals are noisy, temporally filtered, and paired neural-video data are limited. Here we present Ca2REAL (Calcium Activity to Reconstruct Events, Appearance, and Layout), a neural-to-video framework that conditions a pretrained video diffusion model through separate layout and semantic controls derived from calcium activity. Using measured...

---

### 4. Same Behavior, Different Mechanism: What Finite Experiments Can Certify About Integrated Information

**Authors:** Linqian Wu, Diaoxuan He

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08469v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08469v1)

**Summary:** Interpretability, AI auditing and assessments of machine consciousness increasingly rest on mechanism-level quantities: functionals of a system's causal transition law that describe how it computes, not what it outputs. Experiments see that law only through finite, partial and noisy interventions. We ask when such a quantity is identifiable from an experiment's access, continuous in the mechanism and certifiable from finite data, and answer exactly for a deliberately demanding case - the integra...

---

### 5. Spiking neuromodulation: a linear control perspective

**Authors:** Fulvio Forni, Rodolphe Sepulchre

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08571v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08571v1)

**Summary:** Neuronal excitability is a nonlinear phenomenon, and the complexity of spiking experimental traces sometimes looks defeating. The present paper takes the view point that excitability is a neuromodulated property, and aims to demonstrate that the neuromodulation of spiking is amenable to the classical linear analysis tools of control theory. We illustrate the value of linear feedback analysis as an alternative to bifurcation analysis in the simple yet classical example of spiking modulation by th...

---

### 6. Do sEMG Foundation Models Improve Cross-Subject Generalisation?

**Authors:** William Raftery, Dario Farina

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08199v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08199v1)

**Summary:** sEMG Foundation Models aim to learn general purpose representations over diverse subjects and recording conditions that boost performance on a variety of downstream tasks. However, existing evaluations make it difficult to discern whether pretraining alone is sufficient to combat the cross-subject overfitting which makes machine learning on sEMG so challenging. We conduct a systematic evaluation of three sEMG foundation models across three gesture classification datasets under both intra-session...

---

### 7. Reversible Dynamics, Asymmetric Actions: Parking as a Trajectory-Level Affordance

**Authors:** Adam Y. Shavit

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07965v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07965v1)

**Summary:** Drivers are often told to back into a tight parking space, not drive in nose first. The advice looks paradoxical, because a slow car is dynamically reversible: reverse its speed and replay the steering backward, and it retraces a feasible path. Played backward, though, reverse-in shows a car driving forward out of the space. Reverse-in and forward-in are different tasks: they share a start position but end facing opposite ways. We separate three clearances between car and obstacles. Static fit $...

---

### 8. Invariance before structure: two modes of emergent compression in representation learning

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07952v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07952v1)

**Summary:** Learned representations show striking invariance across biological and artificial neural networks, with different substrates and variations driven by drift, heterogeneity and initialisation. To understand this invariance, we propose Emergent Adaptive Representation Learning (EARL), a framework that distinguishes two modes of emergence in learned representations: state-space compression, where a learned representation gains predictive power over its own future beyond what the network's units can ...

---

### 9. Self-Supervised Learning of Local Predictive Directions as a Neural Computation

**Authors:** Marco Zenari, Xuehao Ding, Daniel Burnham, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07809v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07809v1)

**Summary:** Natural sensory dynamics are globally nonlinear but often exhibit simple local geometry, with nearby trajectories evolving preferentially along a small number of predictive directions. We ask how neural circuits could discover this geometry directly from temporal experience. We introduce Local Predictive Directions (LPD), a self-supervised framework that learns local directions whose projections maximally predict near-future trajectory evolution. LPD applies past-future canonical correlation ana...

---

### 10. Bearing, heading and the perceptual geometry of collective motion

**Authors:** Mohammad Salahshour

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.07214v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07214v1)

**Summary:** Traditional models of collective motion commonly assume that animals turn to match their neighbours' directions of travel. In the harmonic theory, decisions follow from a neural representation of direction, and a neighbour enters only as a stimulus at a bearing, the direction in which it lies. Here we show that a neighbour's spatial extent allows its orientation to enter through projection geometry alone, and the theory generates a matrix of coupling coefficients indexed by the neighbour's beari...

---

### 11. Learning Time-Varying Connectomes for Stable Behavior Across Development

**Authors:** Christof Fehrman, Jacob J. Morra, Eva A. Naumann

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06895v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06895v1)

**Summary:** Neural circuits must maintain functionality to drive effective behavior while their size, topology, geometry, and intrinsic dynamics change across development. To model developing visuomotor circuits and behavior, we investigated whether a single compact generative encoding could produce functional recurrent controllers across such changes. Building on the HyperNEAT algorithm, we represented this program as a compositional pattern-producing network that received developmental time as an input to...

---

### 12. Cell-type-specific modularity in E/I networks shapes dynamical regimes and computational capabilities

**Authors:** Emmanouil Giannakakis, Victor Buendía, Oleg Vinogradov, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06720v1)

**Summary:** Structural modularity is a ubiquitous feature of brain networks that shapes neural dynamics and information processing. Yet excitatory and inhibitory populations can differ in their modular organization, and it remains unclear how this asymmetry affects network dynamics and computation. Here, using dynamical mean-field theory and simulations of networks performing complex temporal tasks, we show that independently tuning excitatory and inhibitory modularity controls the dynamical regimes of bala...

---

### 13. PINR-ESI: Physics-Informed Self-Supervised Implicit Neural Representation Framework for EEG Extended-Source Imaging

**Authors:** Zhiyong Zhou, Sheng Liao, Youshen Xiao, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06700v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06700v1)

**Summary:** EEG extended-source imaging aims to localize active cortical regions and characterize their spatial extent, yet supervised inverse networks typically depend on synthetic EEG-source pairs and may be sensitive to synthetic-to-real mismatch. We propose a physics-informed self-supervised implicit neural representation (INR) framework for spatial source reconstruction without paired source labels or simulation-based supervised pretraining. The lead field matrix encodes the source-to-sensor volume-con...

---

### 14. Synchronized Hearts, Desynchronized Brains: A Nonlinear Dynamics Perspective for Function and Failure

**Authors:** Irene Pellini, Simon Bauer, Seba Contreras, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06618v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06618v1)

**Summary:** Both the heart and the brain are built from electrically excitable cells, yet the emergent dynamics of these organs could not differ more. In the myocardium, a coherent traveling wave of action potentials ensures coordinated contraction; in the cerebral cortex, distributed, irregular spiking underlies efficient information processing and the generation of behavior. Here, we illuminate the principles that underlie the emergence of such distinct nonlinear dynamics using concepts from complex syste...

---

### 15. Time-Division Multiplexing: The Operational Rhythm and Temporal Organization Layer of Digital Life

**Authors:** Haibin Tong, Luming Guo, Nana Cui, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06603v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06603v1)

**Summary:** Continual agents must handle urgent interaction while retaining alternatives, replaying errors, and committing safe long-term changes. A previous digital-life framework distinguishes online (busy) and offline (idle) channels, but leaves open whether these are separate programs or phases of a common process and how their operations should be ordered. Motivated by recent observations of rapidly alternating perceptual representations in primate cortex, we develop a temporal organization layer with ...

---

### 16. Mind Control of LLMs via Closed-Loop Stimulation: Out-of-Distribution Robustness

**Authors:** Kasra Fallah, Rudramani Singha, Hannah Ghanei, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06418v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06418v1)

**Summary:** Brains and large language models need not be considered equivalent systems to reveal an interpretable commonality: both exhibit high-dimensional, nonlinear dynamics whose behavior can only be modeled imperfectly. This creates a shared challenge whenever we seek to intervene in their dynamics. A controller may either rely on a model identified around a particular operating regime and risk failure as the system moves away from that regime, or explicitly account for uncertainty and a changing inter...

---

### 17. A minimal E/I circuit model explains differential recovery from amblyopia under TTX and reverse occlusion

**Authors:** Lawrence Udeigwe

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06189v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06189v1)

**Summary:** Recovery from amblyopia beyond the critical period remains a major challenge in visual neuroscience. Experimental studies show that transient inactivation of the fellow eye with tetrodotoxin (TTX) produces stronger and more persistent recovery than reverse occlusion (RO), despite both interventions reducing competition from the fellow eye. The circuit mechanisms underlying this difference remain unclear.   We develop a minimal cortical circuit model combining excitatory-inhibitory population dyn...

---

### 18. A Bayesian Optimized Biquad Filter-Burg Model for Real-Time EEG Phase Estimation

**Authors:** Ivan Martinez-Kay, Tatiana Kardashina, ShiNung Ching, et al.

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05374v2) | 📄 [PDF](https://arxiv.org/pdf/2611.05374v2)

**Summary:** Real-time phase estimation on stimulus-aligned transient EEG is critical for closed-loop neuromodulation systems targeting the theta-band, yet most real-time phase estimation methods have been developed and validated on resting-state, high-fidelity signals in the alpha band. Recent work has pursued deep learning architectures, while individualized classical bandpass filter tuning remains underexplored. This study characterizes the spectral and temporal properties of non-anticipative bandpass fil...

---

### 19. Curriculum unlearning in humans and neural networks

**Authors:** Jirko Rubruck, Alice Zhang, Andrew Saxe, et al.

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.04565v1) | 📄 [PDF](https://arxiv.org/pdf/2611.04565v1)

**Summary:** During learning, humans often benefit from curricula that teach simple rules before exceptions. However, we lack a computational explanation for this phenomenon. Here, using a canonical behavioural task and modelling with neural networks, we develop and test a theory for why simple-to-complex curricula succeed. We show that during learning, both humans and neural networks show simplicity biases, a tendency to learn simple rules that are underfit to the data. In neural networks this bias is accom...

---

### 20. When Model Complexity Matters in Cross-Subject Naturalistic fMRI Prediction

**Authors:** Junhao Zhao, Jacob Kang, Colin Kurniawan, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.04041v1) | 📄 [PDF](https://arxiv.org/pdf/2611.04041v1)

**Summary:** Increasingly complex neural models predict blood-oxygen-level-dependent (BOLD) responses to naturalistic stimuli, but the predictive value of this added complexity remains unclear. We ask when pretrained stimulus representations help and how much downstream complexity is needed, with and without recent measured BOLD history. We compare linear diagnostic references and nonlinear predictors across HCP movie fMRI (154 subjects), BOLD Moments (10 subjects), and Algonauts 2025 (4 subjects). Under a s...

---

### 21. Fly Whiskers Meet LiDAR: Robust Navigation under Sensor Failure

**Authors:** Ali Mahzarnia, Homayoun Jamshidi

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03897v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03897v1)

**Summary:** We extend FLYNN, a leaky integrator recurrent network wired on the Drosophila melanogaster connectome, with a 32-ray 2D LiDAR interface that requires no learned fusion layer beyond a scalar input gain. A 270 degree frontal scan at 8 m range is injected as inverted proximity into the 37 BM Vib head-bristle neurons. Across 24 paired comparisons in a four- state vision matrix with LiDAR on or off, FLYNN-LiDAR has 17 significant wins, 5 nonsignificant comparisons, and 2 significant losses against th...

---

### 22. Evolved Spiking Neural Networks for EEG Seizure Detection: Calcium Dynamics and Delay Mechanics

**Authors:** Tuba Aksoy

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03841v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03841v1)

**Summary:** Neuroevolution can discover compact network designs that are hard to specify by hand. The EONS framework evolves the topology, weights, thresholds and delays of neuromorphic spiking networks without gradients. We tested whether giving integrate-and-fire (IF) neurons an activity-dependent calcium current (Ca-IF neurons) improves evolved networks for EEG seizure detection, with calcium parameters fixed, shared across a network, or evolved for each neuron. On 10 held-out CHB-MIT patients never seen...

---

### 23. Intrinsic network dynamics catalyze switching in functional connectivity states of the brain

**Authors:** Steven S. Kang, Dae-Jin Kim

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03071v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03071v1)

**Summary:** Dynamic functional connectivity (dFC) reflects ongoing reconfiguration of large-scale brain networks, but the temporal organization and network processes underlying spontaneous state transitions remain poorly understood. We developed functional connectivity state switching (FCSS), a phase-coherence-based framework that tracks multiscale changes in dominant whole-brain connectivity configurations. In Human Connectome Project fMRI, FCSS was strongly evoked by cognitive state and condition switches...

---

### 24. AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding

**Authors:** Shiqi Shen, Shurui Li, Xilin Zhang, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02593v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02593v1)

**Summary:** Visual mental imagery (VMI) decoding uses brain activity to reconstruct internally generated visual scenes, providing a potential pathway for externalizing internal experiences and developing neuroprosthetic communication interfaces. However, progress is limited by the lack of dedicated, training-scale VMI datasets. Current VMI paradigms often rely on visual prompts or short-term memory images, introducing visual and mnemonic confounds that make it difficult to disentangle neural activity associ...

---

### 25. Prior Action Control Causally Alters Language-Model Plasticity

**Authors:** Marc-Andre Schulz

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02362v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02362v1)

**Summary:** Two copies of one language model start from identical weights and receive the same rewards during training. For one copy the rewards depend on its own answers. The other copy is yoked: it receives the first copy's rewards no matter what it answers, a design taken from the learned-helplessness experiments of animal learning. We ask whether the copy whose rewards depended on its answers, the copy with control, later learns a new task faster, that is, whether control changes the model's plasticity....

---

### 26. Modeling Visual Cortex with Layerwise Multiscale Manifold Capacity Maximization

**Authors:** Thomas Yerxa, SueYeon Chung, Eero P. Simoncelli

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.02245v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02245v1)

**Summary:** Task-optimized deep neural networks have risen to prominence as the most predictive phenomenological models of responses in primate visual cortex, but leave much to be desired from the perspective of biological plausibility. One such limitation is the reliance on precise credit assignment through global backpropagation of error signals. Recent work has shown that this weakness can be circumvented by requiring each subsequent stage to solve a distinct and increasingly complex task, allowing for l...

---

### 27. Statistical mechanics of spontaneous behavior

**Authors:** Daniel Y. Takahashi, Ahmed El Hady

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.02220v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02220v1)

**Summary:** Why do a few behaviors fill most of an animal's time? The usual answer is that these behaviors are started more often, because learning and reinforcement favor them. Here we show that how long a behavior lasts can, by itself, explain much of what is observed. We consider a system that runs until it meets a constraint, such as a wall, and then resets. The fraction of time it spends in each behavior then follows the Boltzmann law, and the partition function is the mean time between resets. The fou...

---

### 28. Do agents need to sleep?

**Authors:** Ido Haber, Giulio Tononi

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.02216v2) | 📄 [PDF](https://arxiv.org/pdf/2611.02216v2)

**Summary:** LLM-based agents, which increasingly operate persistently across sessions and accumulate memory through interaction, already exhibit the familiar symptoms of unchecked plasticity: semantic drift, degraded retrieval precision, propagation of stored errors, and saturation of memory capacity. Drawing on the selectionist "ringing, resonance and renormalization" (RRR) account of sleep, we propose that each of its three phases maps onto an operation feasible in digital memory architectures. Engineers ...

---

### 29. The (Butter)fly Dream: Linear Separability of World-Model Rollouts in a Connectome-Constrained Visual Model

**Authors:** Junichiro Niimi

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.01866v1) | 📄 [PDF](https://arxiv.org/pdf/2611.01866v1)

**Summary:** Zhuangzi dreamt he was a butterfly and, on waking, could not tell which was the dream. We ask a version of his question of a model of the fly brain: placed inside a world generated by a world model, can a fixed brain tell that the world is a dream? We treat it as a question about what a connectome-constrained model trained on one task makes available beyond that task: do its responses make the defects of a dream linearly decodable? The observer is a published model of the fly visual system train...

---

### 30. A Planar Switching Neuron Shares Logarithmic First-Spike Latency with Its Three-Dimensional Parent But Not Its Onset Mechanism

**Authors:** Giorgio Sonnino, Vadim Shlyonskiy, Thomas Erneux, et al.

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.01632v1) | 📄 [PDF](https://arxiv.org/pdf/2611.01632v1)

**Summary:** Can a reduced neuron model reproduce first-spike latency scaling while changing how a stimulus initiates sustained firing? We compare a piecewise-linear planar Neurosimilator with its three-dimensional parent. Both exhibit logarithmic latency dependence over the investigated input intervals, with different fitted coefficients. The mechanisms differ. In the parent, sustained spiking and a stable resting focus coexist in a spiking--rest bistability regime. An abrupt step accesses spiking, while sl...

---

### 31. S1CogBench: What System One Decision Models Can and Cannot Do on Cognitive Experiments

**Authors:** Dengzhe Hou, Kazunori D Yamada

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.00911v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00911v1)

**Summary:** Language models are no longer used only to generate text. Software also asks them for decisions, in routing, guardrails, and automated gates. System One decision models, also called typed decision models, such as Jev and Laya, return one fast decision over the legal options, leaving no text to inspect. However, a fast, well-formed decision does not show that the model used the evidence. Cognitive experiments can test this, because they vary task demands and measure how behavior changes, yet exis...

---

### 32. Adversarial robustness does not entail human-aligned categorization

**Authors:** Itay Reznik, Raz Lapid, Moshe Sipper, et al.

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.00715v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00715v1)

**Summary:** Adversarial training can improve some forms of correspondence between artificial and biological vision, but whether robust classifiers acquire human-aligned classification behavior remains unclear. We generated 1,008 controversial stimuli by optimizing latent inputs to a pretrained GAN to elicit high-confidence disagreements between pairs of robust ImageNet classifiers. We compared four adversarially robust ImageNet classifiers - ResNet-101, ViT-B, ConvNeXt-L, and Swin-L - with two-alternative c...

---

### 33. From Connection Loss to Collision: Closed-Loop Fault Assessment of a Fly-Connectome SNN

**Authors:** Shuchao Gao

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.06940v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06940v1)

**Summary:** The public release of the complete adult fruit-fly brain connectome enables brain-scale spiking-network studies, motivating closed-loop assessment of connection loss. We test a connectome-derived controller in synthetic pursuit-escape and check record consistency. Across 576 test episodes in paired campaigns, the baseline mapping at 50% connection-row deletion yields 11/48 proportional and 0/48 relay collisions by 1 s, despite paired P/R trigger/burst schedules. The prespecified secondary relay-...

---

### 34. Geometric and algebraic inference in humans and neural networks

**Authors:** Jacob Russin, Joonhwa Kim, Ellie Pavlick, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2611.00387v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00387v1)

**Summary:** Humans possess a remarkable ability to draw inferences from limited data. While some inferences are made intuitively from past experience, others require online reasoning based on novel information given in context. Here, we formalize these strategies, which we term geometric and algebraic inference, and study their computational tradeoffs in humans and neural networks. The geometric strategy gradually shapes representational geometry to reflect underlying relational structure, making subsequent...

---

### 35. Hyperbolic embedding of higher-order simplicial networks

**Authors:** Martin Guillemaud, Vito Latora, Mario Chavez

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41684v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41684v1)

**Summary:** Many biological interactions involve groups rather than pairs, as when several proteins assemble into a multi-protein complex. Simplicial complexes naturally capture these collective interactions. Existing hyperbolic embeddings represent network hierarchy and similarity through a few interpretable coordinates, but rely only on pairwise links: they cannot distinguish three units engaged in a common interaction from three units connected only in pairs. We introduce here the hyperbolic higher-order...

---

### 36. Expression of White and Gray Matter Autism Functional Network Connectivity Signatures in Infancy

**Authors:** Qiang Li, Jingyu Liu, Zening Fu, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40839v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40839v1)

**Summary:** Functional connectivity studies have provided valuable insights into altered brain organization in autism spectrum disorder (ASD). However, most functional connectivity studies focus exclusively on either gray matter (GM) regions or white matter (WM) tracts and examine specific age groups, rather than investigating their functional interactions across brain development. This limits our understanding of how GM-WM functional interactions evolve developmentally and may obscure important aspects of ...

---

### 37. A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening

**Authors:** Zach Paris, Emily Finn

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40511v1)

**Summary:** Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three naturalistic language-listening datasets spanning intracranial electrophysiology and f...

---

### 38. Latent Prediction Yields Cross-Subject Alignable Representations in Sensory-Evoked fMRI

**Authors:** Serwan Jassim, Victoria Bosch, Daniel Anthes, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40280v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40280v1)

**Summary:** Decoding sensory-evoked functional magnetic resonance imaging (fMRI) data is a central analytical tool in cognitive neuroscience. Here we ask whether self-supervised learning (SSL), which has been scarcely explored in this domain, can yield representations that support strong downstream performance. To do so, we adapt a joint embedding predictive architecture (JEPA) to train participant-specific encoders on brain data alone. The encoders never see the stimulus images or any representation derive...

---

### 39. Recognition of auditory objects from continuous and ultra-sparse spike streams in neuromorphic devices

**Authors:** Leonardo E. S. Tavares, Kevin D. Sargent, Jon T. Sakata, et al.

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38564v1)

**Summary:** Energy consumption is a major concern for modern artificial intelligence (AI) applications. The brain is thought to achieve energy-efficient computation through sparse coding schemes. By emulating the spiking dynamics of the brain, neuromorphic chips hold the potential to realize energy-efficient AI. In this work, we use birdsong to demonstrate that auditory object recognition can be achieved using ultra-sparse coding. Feature-detecting neurons tuned to short temporal features ($\sim$37 ms), sam...

---

### 40. REVBRAIN: Real-time Probabilistic EEG Forecasting Using Residual Vector Quantization

**Authors:** Hanna Pankka, Jaakko Lehtinen, Timo Roine

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38558v1)

**Summary:** Real-time forecasting of resting-state EEG signals is required by applications like brain-state-dependent stimulation, where computer generated actions are coupled with ongoing neural oscillations. Recently, the deep learning model WaveNet was proposed for the forecasting task. It shows superior accuracy compared to the prevailing method, the linear autoregressive (AR) model, and provides a built-in uncertainty measure due to its probabilistic modeling framework. However, inference using WaveNet...

---

### 41. Data Amount Heterogeneity Improves Performance in Federated Learning for Neuroimaging

**Authors:** Paul Kurian, Tamoghna Chattopadhyay, Abhijith Shaji, et al.

**Published:** 2026-10-28

🔗 [Paper](http://arxiv.org/abs/2610.38172v1) | 📄 [PDF](https://arxiv.org/pdf/2610.38172v1)

**Summary:** Federated Learning (FL) allows for secure analysis of distributed data without data sharing. We and others have successfully applied FL to neuroimaging tasks, such as Alzheimer's disease classification from structural magnetic resonance imaging (MRI). FL trains a deep learning model locally at each site, encrypts the local model parameters and sends them to a federation controller that aggregates the local models under homomorphic encryption, the resulting community model is sent back to the sit...

---

### 42. Solitary movement style predicts collective foraging while whom to follow emerges only in company

**Authors:** Hiroshi Higashi

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37978v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37978v1)

**Summary:** How far can behaviour inside a group, and the group's performance, be predicted from members measured while alone? We tested this on three public datasets of human collective foraging (621, 128 and 1,133 participants). A low-dimensional individual representation estimated from private-phase movement was mapped onto behaviour inside the group through a mapping learned on other participants. Private information processing was stable between the two halves of a session (split-half reliability, the ...

---

### 43. Every route counts, but some count more: a max-plus view of the C. elegans brain

**Authors:** Emma Reyner-Fuentes, Sebastian Rudolph, Carmen Peláez-Moreno, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37587v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37587v1)

**Summary:** Brains do not simply add up every signal they receive: they select which routes dominate. Yet connectomes are usually analyzed with tools that sum over all paths and place neural states in Euclidean spaces, blurring the feedback circuits that may sustain internal states. Here we treat neural signaling as routing instead of diffusion and describe it with max-plus algebra, in which signals accumulate along a path and the strongest route prevails. We propose a model in which the functional connecto...

---

### 44. Sufficiency Theorem and Closed-Form Posterior for a Windowed Change Point Detection Task

**Authors:** Payton Hanks, Rishidev Chaudhuri, Timothy D. Hanks

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37486v1)

**Summary:** To function effectively in a changing world, agents must detect changes and act on them in a timely fashion. We study this in the context of a change point detection task in which clicks arrive from a Poisson process whose rate changes at an unknown time. An agent must declare the change within a detection window of fixed width or the trial ends in a miss. Here we prove a window sufficiency theorem, which states that the posterior probability of a change depends only on the clicks within the mos...

---

### 45. Local learning is all you need: brain-aligned predictive coding networks

**Authors:** Dirk Gütlin, Ryszard Auksztulewicz, Adrien Doerig

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.37327v1) | 📄 [PDF](https://arxiv.org/pdf/2610.37327v1)

**Summary:** Predictive Coding (PC) is an influential account of how brain representations emerge through hierarchical, local, self-supervised prediction-based learning, without requiring globally propagated error signals. Despite extensive evidence supporting PC, a striking paradox persists: computational models built on these biologically grounded principles have consistently failed to match state-of-the-art Deep Neural Networks in performance and brain-alignment. Here, we show that this paradox can be ove...

---

### 46. Exploring Neural Dynamics with Time Delays: A Numerical and Bifurcation Analysis Approach

**Authors:** Martin R Nelson, Jonathan J Crofts

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36920v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36920v1)

**Summary:** The Wilson-Cowan model is a classic example of a ``neural mass model'' - a simplified yet powerful way to describe the activity of large networks of neurons. It is particularly interesting because, even in its relatively simple form, it can produce a surprising variety of behaviours, from steady rhythms to complex oscillations. A key factor influencing these dynamics is the presence of time delays, reflecting the time it takes for signals to travel between neurons. This article offers an accessi...

---

### 47. Neuronal Identity as an Organizational Basis for Analyzing Neural Population Dynamics

**Authors:** Seungjae Han, Joshua Yedam You, Soi Kim, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36745v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36745v1)

**Summary:** Individual neurons exhibit diverse molecular, morphological, and electrophysiological properties that shape their distinct roles in neural circuits. While these multimodal features are largely shared across individuals, they remain an underutilized source of information in analyzing neural population dynamics. We posit that these shared biological profiles provide a common reference for relating neural dynamics across subjects and recording sessions. Our framework leverages this structure by rou...

---

### 48. The geometry of cognition: from neural populations to neurotechnology

**Authors:** Lucas Bayones, Devika Narain, Roman Rossi-Pool

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36541v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36541v1)

**Summary:** Cognition is implemented by distributed neural populations whose collective activity evolves through structured, low-dimensional state spaces. In this review, we survey the analytical and conceptual tools used to study latent population dynamics in biological neural networks. We begin with single-unit coding, which remains essential for interpreting neuronal selectivity, and then review population-level approaches, including population vectors, cosine similarity, principal component analysis and...

---

### 49. CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments

**Authors:** Kianté Fernandez, Caitlin Chen, Jialu Zhou, et al.

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36484v1)

**Summary:** Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI agents can now complete online behavioral tasks and produce human-like data, which raises concerns that online datasets in the social and behavioral sciences are increasingly open to contamination. We introduce CogArena, ...

---

### 50. Stationary Action Principles for Neuronal Growth

**Authors:** Nathan Brodeur, Cristian Staii

**Published:** 2026-10-27

🔗 [Paper](http://arxiv.org/abs/2610.36463v1) | 📄 [PDF](https://arxiv.org/pdf/2610.36463v1)

**Summary:** Neuronal growth is guided by biochemical, mechanical, and geometrical cues while being influenced by stochastic fluctuations in cytoskeletal dynamics, adhesion, and growth cone sensing. Here, we develop two complementary variational descriptions of mechanically guided axonal growth. First, for neurons growing on periodic parallel micropatterns, we use Langevin and Fokker--Planck models to derive a stochastic path action incorporating deterministic substrate guidance and random fluctuations. The ...

---

## stat.ML

**50 papers**

### 1. Quasipolynomial-Time Planning for Decodable POMDPs

**Authors:** Oliver Dobson, Varun Jog, Chun Hei Michael Shiu

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09778v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09778v1)

**Summary:** We study planning for finite-horizon partially observable Markov decision processes (POMDPs) with finite state, action, and observation spaces. Both exact and approximate planning are known to be computationally hard in this setting, so prior work has explored natural assumptions that make planning easier. Recent work [Golowich et al., 2022] gave quasipolynomial-time approximate planning algorithms for observable POMDPs. These are POMDPs whose observation channels satisfy an $\ell_1$-observabili...

---

### 2. Where Should Learning Live? Regret Analysis for Text, Parameter, and Joint Adaptation

**Authors:** Jungtaek Kim, Jaden Park, Jongwon Jeong, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09701v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09701v1)

**Summary:** Language-model systems can select prompts and parameter adapters repeatedly during deployment, using feedback to guide later choices. Earlier choices may change the context or environment inherited by later configurations. We study selection among preconstructed candidates and compare cumulative loss with the best fixed prompt--parameter pair used from the beginning. This excess loss separates into three terms: selection regret within the available family, the gap from restricting that family, a...

---

### 3. A Generalized Bayesian Approach to Clustering with Dimension Reduction

**Authors:** Shen Jia, Weipeng Huang, Geng Yang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09698v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09698v1)

**Summary:** Generalized Bayes product partition models provide a probabilistic counterpart to loss-based clustering. They update a prior over partitions through an exponentiated clustering loss rather than a likelihood, so allocation uncertainty can be quantified without a full generative model for the data. However, their performance depends on the space in which the loss is evaluated. For high-dimensional observations, a squared Euclidean loss on the raw features can be dominated by irrelevant coordinates...

---

### 4. Online Causal Configuration for Networked Systems via Doubly Robust Steady-State Learning

**Authors:** Yuli Liu, Zhiheng Zhang

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09665v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09665v1)

**Summary:** Measurement exploration reveals how interacting local controllers behave but can alter the steady-state regime a network operator seeks to optimize. Exploratory rewards may therefore fail to identify a configuration's no-exploration value: under full exploration, identical logged distributions can conceal different target values. Identification requires accounting for both action-law mismatch and shifts in the steady-state context distribution. We introduce CAUSAL-UCB, which selects configuratio...

---

### 5. Kernel-Based Learning of Analytic Operators and Parametric PDEs

**Authors:** Giovanni S. Alberti, Markus Holzleitner, Lorenzo Rosasco, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09612v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09612v1)

**Summary:** We study kernel-based learning of analytic operators from finite samples, with a focus on how the regularity of the target should determine the choice of the kernel. We establish embeddings of analytic operators into vector-valued reproducing kernel Hilbert spaces and derive finite-sample, high-probability guarantees that quantify the uncertainty due to random sampling: in the noiseless setting, suitable analytic kernels yield rates exponential in a fractional power of the sample size, while Sob...

---

### 6. Locally Adaptive Conformal Prediction for Polynomial Chaos Expansions

**Authors:** Dimitrios Loukrezis, Arthur Hatstatt, Bruno Sudret, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09579v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09579v1)

**Summary:** This work develops a locally adaptive jackknife+ conformal prediction framework for polynomial chaos expansions. Therein, the non-conformity scores are normalized with an auxiliary polynomial chaos expansion trained on the log-transformed leave-one-out residuals of the base model. We show that the coverage guarantee of jackknife+ conformal prediction carries over to the adaptive intervals if the leave-one-out auxiliary models are trained on nested leave-one-out residuals. For fixed-basis polynom...

---

### 7. Marginal-Nonuniform Multiclass Learning

**Authors:** Nataly Brukhim, Steve Hanneke, Amirreza Shaeiri, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09543v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09543v1)

**Summary:** We study the problem of multiclass classification within the framework of marginal-nonuniform learning, where the constants in the learning rate may depend on the unknown marginal distribution generating the unlabeled data, but not on the target concept. This notion naturally lies between classical PAC learning, where the constants are independent of both the marginal distribution and the target concept, and more recent universal learning, where the constants may depend on both. We give a comple...

---

### 8. k-Volume: a Unified Active Learning Strategy

**Authors:** Eliot Tron, Alain Celisse, Christophe Denis, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09388v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09388v1)

**Summary:** In the classification context where revealing the label of a sample is costly, we propose a new Active Learning (AL) strategy named k-Volume (kVol). It randomly selects a sample to be labeled according to the volume of the smallest ball containing its k nearest neighbors. kVol is highly versatile: it can be applied either in the input space or in the output space, and it enjoys the desirable properties of the three main families of AL strategies: density, diversity, and (when performed in the ou...

---

### 9. Calibrating your confidence requires thinking of all the ways you could be wrong

**Authors:** Marco Miani

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08997v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08997v1)

**Summary:** A primary limitation of modern deep learning is the miscalibration of model confidence; traditional architectures fundamentally lack a mechanism to quantify their own uncertainty. Larger models and larger datasets mitigate this issue, but they do not resolve the underlying structural deficiency. Bayesian methods offer a principled uncertainty-aware learning framework through stochastic parameters. Yet, despite the established benefits, the inherent computational overhead often compromises either...

---

### 10. Enforcing Symmetries on Pre-trained ML Models for Physics

**Authors:** Wenjie Zhou, Valentino F. Foit, David W. Hogg, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08992v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08992v1)

**Summary:** Post-hoc group averaging (or test-time augmentation) is a simple way to impose symmetry on a trained predictor without changing its architecture or retraining it. For finite and compact groups, averaging over a normalized Haar measure on the group gives the Reynolds operator: a canonical projection onto invariant or equivariant predictors with known non-increasing risk guarantees under certain assumptions. This paper provides numerical experiments on physics emulation models that demonstrate the...

---

### 11. Ordered Policy Optimization

**Authors:** Dongkyu Derek Cho, Pan Xu

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08936v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08936v1)

**Summary:** Proximal Policy Optimization (PPO) stabilizes policy updates by clipping the importance ratio between the new policy and the data-collecting policy. The standard rule uses one fixed clipping range for all samples. While this choice offers simplicity and effectiveness, it fails to distinguish statistically harmful extreme ratio values from large, yet tolerable changes. We study how to adapt the clipping radius to the reliability of the induced importance ratio distribution. Our case study demonst...

---

### 12. Geometry-Aware Score-Repellent Monte Carlo

**Authors:** Jie Hu, Lingyun Chen, Do Young Eun

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08909v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08909v1)

**Summary:** The recently proposed Score-Repellent Monte Carlo (SRMC) method improves MCMC sampling by tilting the target density $π$ in $\mathbb{R}^d$ with the factor $\exp(-α\,θ_n^\top s(x))$, where the score function $s(x) = \nabla_x \log π(x)$, and $θ_n$ is the score average from past samples. However, a single scalar repellence strength $α\ge0$ cannot handle both the steep and the flat directions in anisotropic energy landscapes at once. We introduce \emph{Geometry-Aware SRMC} (GA-SRMC), which generaliz...

---

### 13. Reweighting for Transfer Classification: Exact Risk Conversion and Minimax Adaptation

**Authors:** Aoran Chen, Yang Feng

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08876v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08876v1)

**Summary:** A source can make a training mixture easier to learn while making its accuracy less valuable for the target. We study how the training problem a source creates and the finite-sample error of learning it jointly determine target-risk guarantees under reweighting. For binary classification, for each pair of laws and each positive target weight, we derive the sharpest target excess hinge-risk bound implied by mixture excess alone, uniformly over clipped predictors. This exact conversion curve is de...

---

### 14. Beyond the Lower-Star Filtration: Alternative Filtration Methods for Persistent Homology

**Authors:** Innocent Abaa, Umar Islambekov

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08833v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08833v1)

**Summary:** In the lower-star filtration (LSF), simplices are assigned filtration values according to the maximum-vertex rule, with each simplex entering the filtration when its highest-valued vertex appears. A limitation of this construction is that some higher-dimensional simplices may enter simultaneously with their boundary faces, causing certain topological features to be filled immediately upon formation and thus not appear in the resulting persistence diagram. To address this limitation, we propose t...

---

### 15. High-Dimensional Off-Policy Evaluation without Sample Splitting using an Onsager Correction

**Authors:** Saksham Jain, Guillaume Braun, Masaaki Imaizumi

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08794v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08794v1)

**Summary:** Reward models used for off-policy evaluation (OPE) are commonly selected using held-out data. When sample size and context dimension grow proportionally, the difference in test risk between models fitted on the full sample and on a fixed fraction of it need not vanish. Held-out evaluation can therefore consistently estimate the test risk of the model trained on the smaller sample, but because the relative ranking of candidate reward models can change after full-data refitting, held-out selection...

---

### 16. Blind Noise Equalization for Large Data Matrices under General Variance Profiles

**Authors:** Boris Landa, Francesco Strino, Fabio Parisi, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08784v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08784v1)

**Summary:** Low-rank approximation is a basic tool for inference from large and noisy data matrices. However, when noise variances differ across entries, a setting known as heteroskedasticity, the noise can distort the observed spectrum, producing spurious components and obscuring weak signals. To address these challenges, we develop BRINE (Blind Resolvent-based Iterative Noise Equalizer), a data-driven procedure that iteratively rescales rows and columns to equalize the average noise variance across both d...

---

### 17. On Lipschitz Explosion in Deep Neural Networks with Normalization: Consequences for Optimization and Adversarial Robustness

**Authors:** Ashkan Soleymani, Reyhaneh Hosseinpourkhoshkbari, Hadi Daneshmand, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08775v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08775v1)

**Summary:** Can a network look stable at every layer and still be exponentially unstable as a whole? The Lipschitz constant of a neural network is a basic stability quantity appearing in optimization guarantees, generalization bounds, and robustness certificates. Deep networks naturally admit two such notions, input Lipschitzness, measuring sensitivity to data perturbations, and parameter Lipschitzness, measuring sensitivity to weight perturbations. We prove that, for deep networks with normalization layers...

---

### 18. MEDALLION: Manifold Embedding Distillation and Attributions for Low-dimensional Latent InterpretatiON

**Authors:** Vicky Jung, Claire M. He, Irene Chang, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08767v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08767v1)

**Summary:** Dimensionality reduction is widely used to visualize high-dimensional data and guide scientific discovery, yet interpreting which original features contribute to low-dimensional representations remains challenging, particularly for black-box methods such as t-SNE and UMAP. We introduce \textbf{MEDALLION} (Manifold Embedding Distillation and Attributions for Low-dimensional Latent InterpretatiON), a novel framework for interpreting low-dimensional embeddings through knowledge distillation and neu...

---

### 19. Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning

**Authors:** Chenruo Liu, Zihan Wang, Yijun Dong, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08414v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08414v1)

**Summary:** Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two stages manifest in the low-rank increment that LoRA optimizes remains unclear. Tracking the singular spectrum and subspaces of LoRA updates on mathematical reasoning tasks, we find that RL concentrates the spectrum at every learning rate, while SFT expands it at moderate learning rates; moreover, RL ro...

---

### 20. Conformal Prediction for Time-Dependent PDEs

**Authors:** Joshua Stiller, Annika Schneider, Eyke Hüllermeier

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08409v2) | 📄 [PDF](https://arxiv.org/pdf/2611.08409v2)

**Summary:** Uncertainty quantification is crucial in scientific machine learning, where models inform safety-critical tasks such as flood forecasting, financial risk management, and thermal control in machines. Conformal prediction provides distribution-free coverage guarantees, but in time-dependent settings common to physics and engineering, these guarantees can break down, leading to systematic undercoverage. We study this problem in the context of surrogate models for time-dependent physical systems des...

---

### 21. Unifying Central Flow, Rod Flow, and the Edge Coupling

**Authors:** Eric Regis, Sinho Chewi

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08358v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08358v1)

**Summary:** At the edge of stability, the iterates of gradient descent oscillate along the sharp directions of the Hessian. This poses a significant challenge for continuous-time models as the usual continuous-time approximation -- the gradient flow -- admits no oscillations. Several continuous-time models have been proposed to capture the behavior at the edge of stability, among them central flow and rod flow. Although both models can be interpreted as performing a coarse-graining in time, the connection b...

---

### 22. Series-wise Cross-validation for Global Time Series Forecasting

**Authors:** Vitor Cerqueira, Mariana Oliveira, Luis Roque

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08252v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08252v1)

**Summary:** We consider the problem of cross-validation (CV) in time series forecasting, with a focus on global forecasting models based on deep learning. The prevailing CV strategy in forecasting is to partition data across time with the last part of each series used for testing. With global models trained on collections of time series, however, a fundamentally different approach becomes possible: partitioning across series and time. We formalize series-wise CV for global forecasting models and benchmark s...

---

### 23. BUMP: Brief Unexpected Mid-Interpolation Peak

**Authors:** Melinda Flóra Kiss, Márton Muntag, Adrián Csiszárik, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08182v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08182v1)

**Summary:** We identify an intriguing phenomenon when linearly interpolating between permutation-aligned neural networks: test accuracy briefly improves near the interpolation endpoints before dropping toward the midpoint, which we term BUMP (Brief Unexpected Mid-interpolation Peak). We observe that BUMP appears consistently across datasets, architectures, training regimes, and remains robust under substantial perturbations such as early checkpoints and extreme pruning. Moreover, controlled ablations sugges...

---

### 24. Patch Attention Wisely: Understanding Patch Length in Attention-Based Forecasting

**Authors:** Junyu Chen, Likai Chen, Weining Wang

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08160v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08160v1)

**Summary:** Attention-based time series forecasters commonly group consecutive observations into patches. Patch length is known to have a substantial impact on forecasting performance, yet its selection remains largely empirical. We develop a theoretical framework that explains why patch length matters for forecasting accuracy and provides a principled basis for its selection. For linear state-space models, we derive an exact factorization of the forecasting coefficient matrix that separates forecast dynami...

---

### 25. Identifying Neural Dynamics Using Nonlinear Interventional State Space Models

**Authors:** Hanna M. Tolle, Carles Balsells-Rodas, Yixin Wang, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08113v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08113v1)

**Summary:** State-space models (SSMs) recover low-dimensional latent dynamics from high-dimensional observations, but latents are generally not identifiable from observational data alone. Interventional state-space models (iSSMs) use perturbations to break observational symmetries and identify parameters up to permutation, scaling, and shift. However, prior work restricts identifiability to linear latent dynamics and piecewise-linear emissions, excluding many behaviors characteristic of neural circuits. We ...

---

### 26. Doubly-robust causal inference for multi-valued treatment regimes with recurrent neural networks

**Authors:** Jason Poulos

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08077v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08077v1)

**Summary:** We propose a doubly-robust method to estimate the causal effects of multi-valued treatment regimes on patient outcomes. A multi-valued treatment regime assigns personalized treatments from a set of competing options based on a patient's history. Existing methods for optimal treatment regimes are largely limited to binary or continuous treatments. We extend the longitudinal targeted minimum loss-based estimator (LTMLE) to accommodate multi-valued treatments by modeling treatment assignments with ...

---

### 27. Joint Modeling of Conditional Mean and Variability in Multilevel Functional Data: Application to Postprandial Glucose Trajectories in the AEGIS Study

**Authors:** Yang Xiao, Francisco Gude, Marcos Matabuena

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07937v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07937v1)

**Summary:** Functional data analysis provides a framework for studying time-varying associations between covariates and high-frequency biological signals. In digital health, participants often contribute repeated functional trajectories, yet existing multilevel regression methods largely focus on the conditional mean, overlooking variability and its role in biological heterogeneity. We propose a heteroskedastic functional mixed-effects regression framework that jointly models the conditional mean and varian...

---

### 28. pESTO: Iterative p-greedy kernel regression with risk-driven Early STOpping

**Authors:** L. Bruni Bruno, P. Massa, E. Perracchione, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08555v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08555v1)

**Summary:** Kernel-based greedy algorithms select suitable approximation nodes by minimizing point-wise error indicators, such as the power function; in this context, they are usually referred to as p-greedy approaches. In the presence of noisy data, deterministic criteria may fail, as the discrepancy between the true solution and its estimate is influenced by both approximation error and noise amplification, and the balance between the two is unknown. This study explicitly separates these two contributions...

---

### 29. Network Effect Decomposition for Causal Effect Estimation under Network Interference

**Authors:** Zhirong Huang, Wenzhen Zhang, Guangquan Lu, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07879v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07879v1)

**Summary:** Estimating causal effects from observational network data requires accounting for both individual treatment and neighborhood exposure. Existing outcome models commonly incorporate these intervention variables into a joint predictor and estimate causal effects through prediction contrasts, leaving the corresponding response components implicit. We propose the $\underline{N}$etwork $\underline{E}$ffect $\underline{D}$ecomposition $\underline{Net}$work (NEDNet), which parameterizes the conditional ...

---

### 30. Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents

**Authors:** Emmanuel Esposito, Andrew Jacobsen, Hao Qiu, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07773v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07773v1)

**Summary:** We study learning in zero-sum games with delayed feedback. We introduce Multi-Anchor Optimistic Online Mirror Descent (MAO-OMD), a single algorithm which obtains optimal fast rates in self-play on smooth games, while simultaneously maintaining minimax optimal guarantees against arbitrary opponents. In particular, in smooth zero-sum games with arbitrary and unknown feedback delays, MAO-OMD obtains $O(σ_{\max}+1)$ social and individual regrets when used by both players, where $σ_{\max}$ denotes th...

---

### 31. Identification and Bounding of Joint Expectation over Potential Outcomes

**Authors:** Yuta Kawakami, Jin Tian

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07536v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07536v1)

**Summary:** The joint expectation of functions of potential outcomes $(Y_1,Y_0)$ is a fundamental quantity in causal inference, particularly when investigating the variation or heterogeneity of causal effects. This paper provides novel assumptions for their identification: comonotonicity and countercomonotonicity. These assumptions offer a unified framework for their identification across discrete, continuous, and mixed outcome variables. In the absence of these assumptions, we derive sharp bounds for two b...

---

### 32. Changepoint localization via nested exchangeability tests: from point estimates to confidence intervals

**Authors:** Rohan Hore, Aaditya Ramdas

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07399v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07399v1)

**Summary:** We study distribution-free uncertainty quantification for a changepoint estimate in an offline setting. We observe a sequence with a single changepoint and are given an estimate of its location. The pre- and post-change segments are independent and each consists of i.i.d. (or, more generally, exchangeable) observations from arbitrary and unknown distributions. We introduce Changepoint LOcalization via Nested Exchangeability testing (CLONE), a novel method for constructing distribution-free confi...

---

### 33. Last-Iterate Convergence of Stochastic Gradient Methods for Unbounded Problems

**Authors:** Kevin Kurian Thomas Vaidyan, Ahmet Alacaoglu, Michael P. Friedlander

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07334v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07334v1)

**Summary:** Last-iterate convergence guarantees for stochastic gradient methods have attracted significant attention as practical implementations typically return the last iterate instead of an average of the iterates. In this paper, we study two approaches for analyzing the last-iterate convergence of proximal and projected stochastic gradient methods without bounded domain or bounded variance assumptions, where black-box variational inference serves as a running example. Under two related assumptions rela...

---

### 34. ELPAC: Endpoint-Anchored Latent Progression with Stage-Varying Multimodal Coordination

**Authors:** Shengxian Ding, Yifei Zhang, Xinyuan Tian, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08541v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08541v1)

**Summary:** Aging cohorts increasingly combine imaging, plasma, and cognitive measurements, but most subjects provide only a partially observed cross-sectional snapshot, leaving latent stage, progression subtype, and stage-varying multimodal coordination to be inferred jointly. Existing methods estimate the cohort-level aging process, model covariance under observed covariates, or fuse modalities for prediction. However, they rarely target the joint problem of endpoint-anchored staging and progression-resol...

---

### 35. Neural Realized Measures: Forecast-Supervised Intraday Aggregation for Volatility Forecasting

**Authors:** Brian Sing Fan Chan, Jennifer So Kuen Chan

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07287v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07287v1)

**Summary:** High-frequency volatility forecasting typically separates measurement from prediction: intraday observations are first compressed into a daily realized measure using a fixed aggregation rule, and the resulting statistic is then passed to a forecasting model. This conventional pipeline therefore treats measure construction as forecast-agnostic preprocessing. We ask whether the aggregation stage itself can instead be learned from the downstream forecasting objective while preserving the statistica...

---

### 36. Satisficing as competitive Bayesian weighting: a minimal model of goal-directed choice under an unattained target

**Authors:** Moto Shinriki, Yu Kono, Tatsuji Takahashi

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07270v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07270v1)

**Summary:** Animals and humans often do not maximize; they act relative to goals (aspiration levels) that are frequently not yet met. How can a goal that is not (yet) realized organize choice? Deacon (2012) calls such absence-referenced organization \emph{ententional}, and García-Valdecasas and Deacon (2024) argue that ends are best understood as constraints rather than as particular states. We examine this idea in a minimal formal setting: Risk-sensitive Satisficing (RS), a bandit learning rule that values...

---

### 37. Double Machine Learning for Panel Data: Identification, Specification, and a Bank Regulation Effect

**Authors:** Ali Habibnia, Esfandiar Maasoumi, Gaurav Shah

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.07249v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07249v1)

**Summary:** This paper examines robustness and causal interpretation of panel estimates using double/debiased machine learning. The prototype treatment setup is the 2018 US banking regulation. Under common treatment timing, we characterize identification and nuisance restrictions and derive exact bank-level representations of specified "within" and "first-difference" scores. Simulations assess panel model transformation-induced specification bias and inference under weaker overlap. Empirically, estimates va...

---

### 38. Task-Calibrated Random Features via Influence-Based Error Cancellation

**Authors:** Shinto Eguchi

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.07209v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07209v1)

**Summary:** Random features approximate kernel integrals by Monte Carlo, yet only selected frequency-sampling errors affect a downstream task. We propose Task-Calibrated Random Features (TCRF), which balance frequency moments constructed from task-specific influence using weights shared across kernel entries. Closed-form weights coincide with classical minimum-distance calibration; the contribution is a reusable, task-derived calibration space. We show that first-order variance equals the residual variance ...

---

### 39. ShapleyOG: Fast Adaptive Shapley Value Estimation with Odd Gaussian Processes

**Authors:** David Rundel, R. Teal Witter, Santo M. A. R. Thies, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.07173v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07173v1)

**Summary:** Shapley values are a central tool for attribution in machine learning. Since their exact computation requires evaluating the cooperative game to be explained on exponentially many player coalitions, they are typically estimated from a limited number of evaluations. Recently, ShaplEIG has shown that adaptively selecting the coalitions to evaluate substantially improves sample efficiency over classical estimators. This, however, comes at the cost of a sequential procedure that, in every iteration,...

---

### 40. Bayesian Tensor Train Kernel Machines with Automatic Model Complexity Inference

**Authors:** Afra Kilic, Kim Batselier

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.07129v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07129v1)

**Summary:** Tensor Network (TN) kernel machines accelerate supervised learning by using low-rank TNs to reduce computation and memory. However, most TN-based methods are deterministic with manually tuned ranks and feature dimensions, while the existing Bayesian TN kernel machine is restricted to the CANDECOMP/PARAFAC decomposition (CPD), whose single rank is shared by all modes. We extend this framework to the tensor train (TT) and propose Bayesian Tensor Train Kernel Machines (BTT-KM), whose hierarchical A...

---

### 41. Regression with Many Generated Controls

**Authors:** Timothy Christensen, Daniel Vebman

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06855v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06855v1)

**Summary:** We consider linear regression when some covariates are endogenous, a variable sufficient to control for endogeneity exists but is latent, and the practitioner can generate many proxies for the latent control. For instance, one could cheaply but imperfectly impute the latent control using different AI/ML methods, each generating a different proxy. There are several options the practitioner might consider in this scenario: including all proxies or factors computed from the proxies as controls, ins...

---

### 42. Alignment Myopia in Generative AI

**Authors:** Remi Denton, Aida Davani, Cynthia L Bennett, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06830v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06830v1)

**Summary:** Current generative AI alignment relies on a myopic paradigm that prioritizes immediate conversational satisfaction. By relying on short-horizon feedback, this approach ignores the profound, longitudinal externalities of persistent human-AI interaction, which can lead to adverse outcomes such as cognitive atrophy, social erosion, and diminished human agency. To address this, we propose a paradigm shift toward long-horizon alignment that accounts for how AI reshapes human experience over time. To ...

---

### 43. ToroFit: Fitting Wedge Sums of Tori to High-Dimensional Data

**Authors:** Tanishq Bhatia, Jose A. Perea, Tarek M. Zikry

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06990v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06990v1)

**Summary:** Data arising in scientific applications often exhibits complex nonlinear structure. Identifying and parameterizing said nonlinearities can enable better modeling, enhance predictive analysis, data interpolation, denoising, and anomaly detection. In this paper, we develop theoretical and computational methods to detect and parametrize Euclidean point cloud data lying near a wedge sum of tori. Specifically, we use persistent cohomology and cup products to identify the distinct toroidal components,...

---

### 44. Message-passing graph persistence

**Authors:** Jorge Luiz Franco, Arthur Queiroz Moura, Moacir Ponti, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06801v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06801v1)

**Summary:** Message-passing graph neural networks (GNNs) are limited in expressive power by the one-dimensional Weisfeiler-Leman test. Persistent homology (PH) provides topological descriptors that can complement GNN representations, but existing approaches typically compute persistence separately from the representation learning process. In this paper, we introduce Message-Passing Graph Persistence (MGP), a family of topological descriptors that incorporates message passing into graph filtrations. At each ...

---

### 45. Fundamental Limits of Coherent Imaging in The Presence of Atmospheric Turbulence

**Authors:** Songbin Liu, Hanyu Yang, Junren Chen, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06784v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06784v1)

**Summary:** We study the fundamental limits of jointly estimating the signal amplitude and the atmospheric phase distortion in complex-valued multi-look coherent imaging, where the measurements are corrupted by multiplicative speckle and additive Gaussian noise, all looks share a known Gaussian sensing matrix, and both parameters belong to structured classes. By analyzing a constrained maximum likelihood estimator, we establish an upper bound on the joint minimax risk that holds uniformly over the admissibl...

---

### 46. Regularization vs. Convolution in Kernel-Based Hypothesis Testing

**Authors:** Omar Hagrass, Bharath K. Sriperumbudur

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06778v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06778v1)

**Summary:** The maximum mean discrepancy (MMD) test is a popular nonparametric test on general domains. Two lines of work have studied its optimality through structurally different approaches. The first, a convolution approach on $\mathbb{R}^d$, uses translation-invariant kernels with a shrinking bandwidth and is minimax optimal over Sobolev balls under $L^2$-separation; the second, a regularization approach on general measurable spaces, uses spectral regularization of the kernel covariance operator and is ...

---

### 47. TestBED: An Open-Source Toolkit for Bayesian Experimental Design

**Authors:** Gavin Kerrigan, Marcel Hedman, Sahel Iqbal, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06633v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06633v1)

**Summary:** Bayesian experimental design (BED) is a principled framework for intelligent data acquisition with applications across a wide range of scientific and industrial domains. However, the development and adoption of BED remains hindered by a lack of standardised software and benchmarks. Existing methods are typically implemented in bespoke codebases and evaluated on a small subset of tasks, making methods difficult to apply, compare, or extend. To address this, we present TestBED, a general-purpose, ...

---

### 48. Finite-width shift of the edge of chaos in deep neural networks

**Authors:** Arn Caesar

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06582v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06582v1)

**Summary:** Deep neural networks train best when they are initialised at the edge of chaos, the critical line in the plane of weight and bias variances on which the distance between two inputs neither grows nor shrinks with depth. The line is known for infinitely wide networks; at finite width it moves, and how it moves has been disputed. We treat the logarithm of the distance between two inputs through a network of width $N$ as a random walk and compute its drift and variance to order $1/N$. The edge of ch...

---

### 49. Risk-Sensitive Non-Parametric and Kernel Bandits

**Authors:** Devdan Dey, Sujoy Bhore, Avishek Ghosh

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06489v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06489v1)

**Summary:** We study non-parametric bandits in which arms are evaluated using Cumulative Prospect Theory (CPT) rather than expected reward. We consider continuous action spaces with arm-dependent noise and propose Non-Parametric CPT Bandits ($\mathtt{NPCB}$), an optimistic algorithm that decouples mean estimation from CPT-based decision-making. We prove CPT regret of order $\widetilde{\mathcal O}\bigl(\sqrt{T\,\dim_E(\mathcal F,T^{-2})\,\log N(\mathcal F,T^{-2},\|\cdot\|_\infty)}\bigr)$, where $\dim_E$ is t...

---

### 50. Understanding the Out-of-Distribution Generalization of Chain-of-Thought Reasoning in LLMs

**Authors:** Nuo-Jing Liang, Xiao-Tong Yuan, Pan Zhou

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06438v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06438v1)

**Summary:** Chain-of-Thought (CoT) reasoning substantially improves Large Language Models (LLMs), yet its out-of-distribution (OOD) generalization mechanism remains theoretically underexplored. We study CoT as compositional OOD generalization: the target task lacks complete reasoning trajectories or direct input-output pairs, while training provides only in-distribution (ID) atomic step data. We show that CoT generalizes by repeatedly applying a shared single-step predictor to compose reusable ID transition...

---

