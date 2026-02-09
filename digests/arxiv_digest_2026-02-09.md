# arXiv Daily Digest - 2026-02-09

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Learning a Generative Meta-Model of LLM Activations

**Authors:** Grace Luo, Jiahai Feng, Trevor Darrell, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06964v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06964v1)

**Summary:** Existing approaches for analyzing neural network activations, such as PCA and sparse autoencoders, rely on strong structural assumptions. Generative models offer an alternative: they can uncover structure without such assumptions and act as priors that improve intervention fidelity. We explore this direction by training diffusion models on one billion residual stream activations, creating "meta-models" that learn the distribution of a network's internal states. We find that diffusion loss decrea...

---

### 2. InftyThink+: Effective and Efficient Infinite-Horizon Reasoning via Reinforcement Learning

**Authors:** Yuchen Yan, Liang Jiang, Jin Jiang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06960v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06960v1)

**Summary:** Large reasoning models achieve strong performance by scaling inference-time chain-of-thought, but this paradigm suffers from quadratic cost, context length limits, and degraded reasoning due to lost-in-the-middle effects. Iterative reasoning mitigates these issues by periodically summarizing intermediate thoughts, yet existing methods rely on supervised learning or fixed heuristics and fail to optimize when to summarize, what to preserve, and how to resume reasoning. We propose InftyThink+, an e...

---

### 3. DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

**Authors:** Shenyuan Gao, William Liang, Kaiyuan Zheng, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06949v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06949v1)

**Summary:** Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture r...

---

### 4. Agentic Uncertainty Reveals Agentic Overconfidence

**Authors:** Jean Kaddour, Srijan Patel, Gbètondji Dovonon, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06948v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06948v1)

**Summary:** Can AI agents predict whether they will succeed at a task? We study agentic uncertainty by eliciting success probability estimates before, during, and after task execution. All results exhibit agentic overconfidence: some agents that succeed only 22% of the time predict 77% success. Counterintuitively, pre-execution assessment with strictly less information tends to yield better discrimination than standard post-execution review, though differences are not always significant. Adversarial prompti...

---

### 5. Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay

**Authors:** Duygu Altinok

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06942v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06942v1)

**Summary:** Tokenization is a pivotal design choice for neural language modeling in morphologically rich languages (MRLs) such as Turkish, where productive agglutination challenges both vocabulary efficiency and morphological fidelity. Prior studies have explored tokenizer families and vocabulary sizes but typically (i) vary vocabulary without systematically controlling the tokenizer's training corpus, (ii) provide limited intrinsic diagnostics, and (iii) evaluate a narrow slice of downstream tasks. We pres...

---

### 6. Endogenous Resistance to Activation Steering in Language Models

**Authors:** Alex McKenzie, Keenan Pepper, Stijn Servaes, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06941v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06941v1)

**Summary:** Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 SAE latents that activate diff...

---

### 7. Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics

**Authors:** Zuyuan Zhang, Sizhe Tang, Tian Lan

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06939v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06939v1)

**Summary:** Non-Markovian dynamics are commonly found in real-world environments due to long-range dependencies, partial observability, and memory effects. The Bellman equation that is the central pillar of Reinforcement learning (RL) becomes only approximately valid under Non-Markovian. Existing work often focus on practical algorithm designs and offer limited theoretical treatment to address key questions, such as what dynamics are indeed capturable by the Bellman framework and how to inspire new algorith...

---

### 8. Implementing Grassroots Logic Programs with Multiagent Transition Systems and AI

**Authors:** Ehud Shapiro

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06934v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06934v1)

**Summary:** Grassroots Logic Programs (GLP) is a concurrent logic programming language with variables partitioned into paired \emph{readers} and \emph{writers}, conjuring both linear logic and futures/promises: an assignment is produced at most once via the sole occurrence of a writer (promise) and consumed at most once via the sole occurrence of its paired reader (future), and may contain additional readers and/or writers, enabling the concise expression of rich multidirectional communication modalities.  ...

---

### 9. From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers

**Authors:** Ziming Liu, Sophia Sanborn, Surya Ganguli, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06923v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06923v1)

**Summary:** Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, they typically rely on strong, domain-specific priors that effectively "bake in" the physics. Conversely, Vafa et al. recently showed that...

---

### 10. Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs

**Authors:** Samir Abdaljalil, Parichit Sharma, Erchin Serpedin, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06920v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06920v1)

**Summary:** Hallucinations in large language models remain a persistent challenge, particularly in multilingual and generative settings where factual consistency is difficult to maintain. While recent models show strong performance on English-centric benchmarks, their behavior across languages, tasks, and hallucination types is not yet well understood. In this work, we introduce Halluverse-M^3, a dataset designed to enable systematic analysis of hallucinations across multiple languages, multiple generation ...

---

### 11. PANC: Prior-Aware Normalized Cut for Object Segmentation

**Authors:** Juan Gutiérrez, Victor Gutiérrez-Garcia, José Luis Blanco-Murillo

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06912v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06912v1)

**Summary:** Fully unsupervised segmentation pipelines naively seek the most salient object, should this be present. As a result, most of the methods reported in the literature deliver non-deterministic partitions that are sensitive to initialization, seed order, and threshold heuristics.   We propose PANC, a weakly supervised spectral segmentation framework that uses a minimal set of annotated visual tokens to produce stable, controllable, and reproducible object masks. From the TokenCut approach, we augmen...

---

### 12. TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering

**Authors:** Saad Hossain, Tom Tseng, Punya Syon Pandey, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06911v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06911v1)

**Summary:** As increasingly capable open-weight large language models (LLMs) are deployed, improving their tamper resistance against unsafe modifications, whether accidental or intentional, becomes critical to minimize risks. However, there is no standard approach to evaluate tamper resistance. Varied data sets, metrics, and tampering configurations make it difficult to compare safety, utility, and robustness across different models and defenses. To this end, we introduce TamperBench, the first unified fram...

---

### 13. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design

**Authors:** Samuel Klein, Willie Neiswanger, Daniel Ratner, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06900v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06900v1)

**Summary:** Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural ...

---

### 14. NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices

**Authors:** Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Couto Pimentel Ramos, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06879v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06879v1)

**Summary:** While large-scale text-to-image diffusion models continue to improve in visual quality, their increasing scale has widened the gap between state-of-the-art models and on-device solutions. To address this gap, we introduce NanoFLUX, a 2.4B text-to-image flow-matching model distilled from 17B FLUX.1-Schnell using a progressive compression pipeline designed to preserve generation quality. Our contributions include: (1) A model compression strategy driven by pruning redundant components in the diffu...

---

### 15. TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code

**Authors:** Jiangping Huang, Wenguang Ye, Weisong Sun, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06875v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06875v1)

**Summary:** Large Language Models (LLMs) often generate code with subtle but critical bugs, especially for complex tasks. Existing automated repair methods typically rely on superficial pass/fail signals, offering limited visibility into program behavior and hindering precise error localization. In addition, without a way to learn from prior failures, repair processes often fall into repetitive and inefficient cycles. To overcome these challenges, we present TraceCoder, a collaborative multi-agent framework...

---

### 16. Git for Sketches: An Intelligent Tracking System for Capturing Design Evolution

**Authors:** Sankar B, Amogh A S, Sandhya Baranwal, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06047v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06047v1)

**Summary:** During product conceptualization, capturing the non-linear history and cognitive intent is crucial. Traditional sketching tools often lose this context. We introduce DIMES (Design Idea Management and Evolution capture System), a web-based environment featuring sGIT (SketchGit), a custom visual version control architecture, and Generative AI. sGIT includes AEGIS, a module using hybrid Deep Learning and Machine Learning models to classify six stroke types. The system maps Git primitives to design ...

---

### 17. Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts

**Authors:** Xinyu Zhao, Qingyun Sun, Jiayi Luo, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06859v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06859v1)

**Summary:** Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, existing zero-shot GAD methods largely ignore intrinsic geometric differences across diverse anomaly patterns, substantially limiting their cross-domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graph...

---

### 18. AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

**Authors:** Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06855v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06855v1)

**Summary:** LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. These tasks span diverse domains, including language modeling, mathematics, bioinformatics, and time series forecasting. AIRS-Bench tasks assess agentic capabilities over the full research lifecycle -- including idea generation, experiment analysis and iterative r...

---

### 19. The Quantum Sieve Tracer: A Hybrid Framework for Layer-Wise Activation Tracing in Large Language Models

**Authors:** Jonathan Pan

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06852v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06852v1)

**Summary:** Mechanistic interpretability aims to reverse-engineer the internal computations of Large Language Models (LLMs), yet separating sparse semantic signals from high-dimensional polysemantic noise remains a significant challenge. This paper introduces the Quantum Sieve Tracer, a hybrid quantum-classical framework designed to characterize factual recall circuits. We implement a modular pipeline that first localizes critical layers using classical causal tracing, then maps specific attention head acti...

---

### 20. Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping

**Authors:** Chao Zhou, Tianyi Wei, Yiling Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06850v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06850v1)

**Summary:** While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi-condition control addresses this, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate-and-attend'' strategy, which suffers from quadratic computational and memory overhead as the number of conditions scales. Our analysis reveals that much of this...

---

### 21. The Representational Geometry of Number

**Authors:** Zhimin Hu, Lanhao Niu, Sashank Varma

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06843v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06843v1)

**Summary:** A central question in cognitive science is whether conceptual representations converge onto a shared manifold to support generalization, or diverge into orthogonal subspaces to minimize task interference. While prior work has discovered evidence for both, a mechanistic account of how these properties coexist and transform across tasks remains elusive. We propose that representational sharing lies not in the concepts themselves, but in the geometric relations between them. Using number concepts a...

---

### 22. From Features to Actions: Explainability in Traditional and Agentic AI Systems

**Authors:** Sindhuja Chaduvula, Jessee Ho, Kina Kim, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06841v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06841v1)

**Summary:** Over the last decade, explainable AI has primarily focused on interpreting individual model predictions, producing post-hoc explanations that relate inputs to outputs under a fixed decision structure. Recent advances in large language models (LLMs) have enabled agentic AI systems whose behaviour unfolds over multi-step trajectories. In these settings, success and failure are determined by sequences of decisions rather than a single output. While useful, it remains unclear how explanation approac...

---

### 23. An Adaptive Differentially Private Federated Learning Framework with Bi-level Optimization

**Authors:** Jin Wang, Hui Ma, Fei Xing, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06838v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06838v1)

**Summary:** Federated learning enables collaborative model training across distributed clients while preserving data privacy. However, in practical deployments, device heterogeneity, non-independent, and identically distributed (Non-IID) data often lead to highly unstable and biased gradient updates. When differential privacy is enforced, conventional fixed gradient clipping and Gaussian noise injection may further amplify gradient perturbations, resulting in training oscillation and performance degradation...

---

### 24. LLM Active Alignment: A Nash Equilibrium Perspective

**Authors:** Tonghan Wang, Yuqi Pan, Xinyi Yang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06836v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06836v1)

**Summary:** We develop a game-theoretic framework for predicting and steering the behavior of populations of large language models (LLMs) through Nash equilibrium (NE) analysis. To avoid the intractability of equilibrium computation in open-ended text spaces, we model each agent's action as a mixture over human subpopulations. Agents choose actively and strategically which groups to align with, yielding an interpretable and behaviorally substantive policy class. We derive closed-form NE characterizations, a...

---

### 25. AEGPO: Adaptive Entropy-Guided Policy Optimization for Diffusion Models

**Authors:** Yuming Li, Qingyu Li, Chengyu Bai, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06825v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06825v1)

**Summary:** Reinforcement learning from human feedback (RLHF) shows promise for aligning diffusion and flow models, yet policy optimization methods such as GRPO suffer from inefficient and static sampling strategies. These methods treat all prompts and denoising steps uniformly, ignoring substantial variations in sample learning value as well as the dynamic nature of critical exploration moments.   To address this issue, we conduct a detailed analysis of the internal attention dynamics during GRPO training ...

---

### 26. AI-Generated Music Detection in Broadcast Monitoring

**Authors:** David Lopez-Ayala, Asier Cabello, Pablo Zinemanas, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06823v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06823v1)

**Summary:** AI music generators have advanced to the point where their outputs are often indistinguishable from human compositions. While detection methods have emerged, they are typically designed and validated in music streaming contexts with clean, full-length tracks. Broadcast audio, however, poses a different challenge: music appears as short excerpts, often masked by dominant speech, conditions under which existing detectors fail. In this work, we introduce AI-OpenBMAT, the first dataset tailored to b...

---

### 27. POP: Online Structural Pruning Enables Efficient Inference of Large Foundation Models

**Authors:** Yi Chen, Wonjin Shin, Shuhong Liu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06822v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06822v1)

**Summary:** Large foundation models (LFMs) achieve strong performance through scaling, yet current structural pruning methods derive fixed pruning decisions during inference, overlooking sparsity patterns that emerge in the autoregressive token generation. In this paper, we propose POP (Partition-guided Online Pruning), an efficient online structural pruning framework that enables context-conditioned dynamic pruning with minimal computational overhead. POP partitions model channels into retained, candidate,...

---

### 28. ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training

**Authors:** Dunwei Tu, Hongyan Hao, Hansi Yang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06820v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06820v1)

**Summary:** Training generalist agents capable of adapting to diverse scenarios requires interactive environments for self-exploration. However, interactive environments remain critically scarce, and existing synthesis methods suffer from significant limitations regarding environmental diversity and scalability. To address these challenges, we introduce ScaleEnv, a framework that constructs fully interactive environments and verifiable tasks entirely from scratch. Specifically, ScaleEnv ensures environment ...

---

### 29. Bridging 6G IoT and AI: LLM-Based Efficient Approach for Physical Layer's Optimization Tasks

**Authors:** Ahsan Mehmood, Naveed Ul Hassan, Ghassan M. Kraidy

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06819v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06819v1)

**Summary:** This paper investigates the role of large language models (LLMs) in sixth-generation (6G) Internet of Things (IoT) networks and proposes a prompt-engineering-based real-time feedback and verification (PE-RTFV) framework that perform physical-layer's optimization tasks through an iteratively process. By leveraging the naturally available closed-loop feedback inherent in wireless communication systems, PE-RTFV enables real-time physical-layer optimization without requiring model retraining. The pr...

---

### 30. Wild Guesses and Mild Guesses in Active Concept Learning

**Authors:** Anirudh Chari, Neil Pattanaik

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06818v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06818v1)

**Summary:** Human concept learning is typically active: learners choose which instances to query or test in order to reduce uncertainty about an underlying rule or category. Active concept learning must balance informativeness of queries against the stability of the learner that generates and scores hypotheses. We study this trade-off in a neuro-symbolic Bayesian learner whose hypotheses are executable programs proposed by a large language model (LLM) and reweighted by Bayesian updating. We compare a Ration...

---

### 31. SuReNav: Superpixel Graph-based Constraint Relaxation for Navigation in Over-constrained Environments

**Authors:** Keonyoung Koh, Moonkyeong Jung, Samuel Seungsup Lee, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06807v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06807v1)

**Summary:** We address the over-constrained planning problem in semi-static environments. The planning objective is to find a best-effort solution that avoids all hard constraint regions while minimally traversing the least risky areas. Conventional methods often rely on pre-defined area costs, limiting generalizations. Further, the spatial continuity of navigation spaces makes it difficult to identify regions that are passable without overestimation. To overcome these challenges, we propose SuReNav, a supe...

---

### 32. On the Identifiability of Steering Vectors in Large Language Models

**Authors:** Sohan Venkatesh, Ashish Mahendran Kurapath

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06801v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06801v1)

**Summary:** Activation steering methods, such as persona vectors, are widely used to control large language model behavior and increasingly interpreted as revealing meaningful internal representations. This interpretation implicitly assumes steering directions are identifiable and uniquely recoverable from input-output behavior. We formalize steering as an intervention on internal representations and prove that, under realistic modeling and data conditions, steering vectors are fundamentally non-identifiabl...

---

### 33. Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling

**Authors:** Kate Sanders, Nathaniel Weir, Sapana Chaudhary, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06795v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06795v1)

**Summary:** An impediment to using Large Language Models (LLMs) for reasoning output verification is that LLMs struggle to reliably identify errors in thinking traces, particularly in long outputs, domains requiring expert knowledge, and problems without verifiable rewards. We propose a data-driven approach to automatically construct highly granular reasoning error taxonomies to enhance LLM-driven error detection on unseen reasoning traces. Our findings indicate that classification approaches that leverage ...

---

### 34. Next-generation cyberattack detection with large language models: anomaly analysis across heterogeneous logs

**Authors:** Yassine Chagna, Antal Goldschmidt

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06777v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06777v1)

**Summary:** This project explores large language models (LLMs) for anomaly detection across heterogeneous log sources. Traditional intrusion detection systems suffer from high false positive rates, semantic blindness, and data scarcity, as logs are inherently sensitive, making clean datasets rare. We address these challenges through three contributions: (1) LogAtlas-Foundation-Sessions and LogAtlas-Defense-Set, balanced and heterogeneous log datasets with explicit attack annotations and privacy preservation...

---

### 35. Towards Understanding What State Space Models Learn About Code

**Authors:** Jiali Wu, Abhinav Anand, Shweta Verma, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06774v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06774v1)

**Summary:** State Space Models (SSMs) have emerged as an efficient alternative to the transformer architecture. Recent studies show that SSMs can match or surpass Transformers on code understanding tasks, such as code retrieval, when trained under similar conditions. However, their internal mechanisms remain a black box. We present the first systematic analysis of what SSM-based code models actually learn and perform the first comparative analysis of SSM and Transformer-based code models. Our analysis revea...

---

### 36. AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models

**Authors:** Fengpeng Li, Kemou Li, Qizhou Wang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06771v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06771v1)

**Summary:** Concept erasure helps stop diffusion models (DMs) from generating harmful content; but current methods face robustness retention trade off. Robustness means the model fine-tuned by concept erasure methods resists reactivation of erased concepts, even under semantically related prompts. Retention means unrelated concepts are preserved so the model's overall utility stays intact. Both are critical for concept erasure in practice, yet addressing them simultaneously is challenging, as existing works...

---

### 37. A Unified Framework for LLM Watermarks

**Authors:** Thibaud Gloaguen, Robin Staab, Nikola Jovanović, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06754v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06754v1)

**Summary:** LLM watermarks allow tracing AI-generated texts by inserting a detectable signal into their generated content. Recent works have proposed a wide range of watermarking algorithms, each with distinct designs, usually built using a bottom-up approach. Crucially, there is no general and principled formulation for LLM watermarking.   In this work, we show that most existing and widely used watermarking schemes can in fact be derived from a principled constrained optimization problem. Our formulation ...

---

### 38. Gold Exploration using Representations from a Multispectral Autoencoder

**Authors:** Argyro Tsandalidou, Konstantinos Dogeas, Eleftheria Tetoula Tsonga, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06748v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06748v1)

**Summary:** Satellite imagery is employed for large-scale prospectivity mapping due to the high cost and typically limited availability of on-site mineral exploration data. In this work, we present a proof-of-concept framework that leverages generative representations learned from multispectral Sentinel-2 imagery to identify gold-bearing regions from space. An autoencoder foundation model, called Isometric, which is pretrained on the large-scale FalconSpace-S2 v1.0 dataset, produces information-dense spectr...

---

### 39. Semantically Labelled Automata for Multi-Task Reinforcement Learning with LTL Instructions

**Authors:** Alessandro Abate, Giuseppe De Giacomo, Mathias Jackermeier, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06746v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06746v1)

**Summary:** We study multi-task reinforcement learning (RL), a setting in which an agent learns a single, universal policy capable of generalising to arbitrary, possibly unseen tasks. We consider tasks specified as linear temporal logic (LTL) formulae, which are commonly used in formal methods to specify properties of systems, and have recently been successfully adopted in RL. In this setting, we present a novel task embedding technique leveraging a new generation of semantic LTL-to-automata translations, o...

---

### 40. Optimal Abstractions for Verifying Properties of Kolmogorov-Arnold Networks (KANs)

**Authors:** Noah Schwartz, Chandra Kanth Nagesh, Sriram Sankaranarayanan, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06737v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06737v1)

**Summary:** We present a novel approach for verifying properties of Kolmogorov-Arnold Networks (KANs), a class of neural networks characterized by nonlinear, univariate activation functions typically implemented as piecewise polynomial splines or Gaussian processes. Our method creates mathematical ``abstractions'' by replacing each KAN unit with a piecewise affine (PWA) function, providing both local and global error estimates between the original network and its approximation. These abstractions enable pro...

---

### 41. Pairwise is Not Enough: Hypergraph Neural Networks for Multi-Agent Pathfinding

**Authors:** Rishabh Jain, Keisuke Okumura, Michael Amir, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06733v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06733v1)

**Summary:** Multi-Agent Path Finding (MAPF) is a representative multi-agent coordination problem, where multiple agents are required to navigate to their respective goals without collisions. Solving MAPF optimally is known to be NP-hard, leading to the adoption of learning-based approaches to alleviate the online computational burden. Prevailing approaches, such as Graph Neural Networks (GNNs), are typically constrained to pairwise message passing between agents. However, this limitation leads to suboptimal...

---

### 42. GhostCite: A Large-Scale Analysis of Citation Validity in the Age of Large Language Models

**Authors:** Zuyao Xu, Yuqi Qiu, Lu Sun, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06718v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06718v1)

**Summary:** Citations provide the basis for trusting scientific claims; when they are invalid or fabricated, this trust collapses. With the advent of Large Language Models (LLMs), this risk has intensified: LLMs are increasingly used for academic writing, yet their tendency to fabricate citations (``ghost citations'') poses a systemic threat to citation validity.   To quantify this threat and inform mitigation, we develop CiteVerifier, an open-source framework for large-scale citation verification, and cond...

---

### 43. F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare

**Authors:** Daniil Plyusov, Alexey Gorbatovski, Boris Shaposhnikov, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06717v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06717v1)

**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) is commonly based on group sampling to estimate advantages and stabilize policy updates. In practice, large group sizes are not feasible due to computational limits, which biases learning toward trajectories that are already likely. Smaller groups often miss rare-correct trajectories while still containing mixed rewards, concentrating probability on common solutions. We derive the probability that updates miss rare-correct modes as a function...

---

### 44. Autoregressive Models for Knowledge Graph Generation

**Authors:** Thiviyan Thanapalasingam, Antonis Vozikis, Peter Bloem, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06707v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06707v1)

**Summary:** Knowledge Graph (KG) generation requires models to learn complex semantic dependencies between triples while maintaining domain validity constraints. Unlike link prediction, which scores triples independently, generative models must capture interdependencies across entire subgraphs to produce semantically coherent structures. We present ARK (Auto-Regressive Knowledge Graph Generation), a family of autoregressive models that generate KGs by treating graphs as sequences of (head, relation, tail) t...

---

### 45. SaDiT: Efficient Protein Backbone Design via Latent Structural Tokenization and Diffusion Transformers

**Authors:** Shentong Mo, Lanqing Li

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06706v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06706v1)

**Summary:** Generative models for de novo protein backbone design have achieved remarkable success in creating novel protein structures. However, these diffusion-based approaches remain computationally intensive and slower than desired for large-scale structural exploration. While recent efforts like Proteina have introduced flow-matching to improve sampling efficiency, the potential of tokenization for structural compression and acceleration remains largely unexplored in the protein domain. In this work, w...

---

### 46. compar:IA: The French Government's LLM arena to collect French-language human prompts and preference data

**Authors:** Lucie Termignon, Simonas Zilinskas, Hadrien Pélissier, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06669v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06669v1)

**Summary:** Large Language Models (LLMs) often show reduced performance, cultural alignment, and safety robustness in non-English languages, partly because English dominates both pre-training data and human preference alignment datasets. Training methods like Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) require human preference data, which remains scarce and largely non-public for many languages beyond English. To address this gap, we introduce compar:IA, an ope...

---

### 47. Not All Layers Need Tuning: Selective Layer Restoration Recovers Diversity

**Authors:** Bowen Zhang, Meiyi Wang, Harold Soh

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06665v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06665v1)

**Summary:** Post-training improves instruction-following and helpfulness of large language models (LLMs) but often reduces generation diversity, which leads to repetitive outputs in open-ended settings, a phenomenon known as mode collapse. Motivated by evidence that LLM layers play distinct functional roles, we hypothesize that mode collapse can be localized to specific layers and that restoring a carefully chosen range of layers to their pre-trained weights can recover diversity while maintaining high outp...

---

### 48. Multimodal Generative Retrieval Model with Staged Pretraining for Food Delivery on Meituan

**Authors:** Boyu Chen, Tai Guo, Weiyu Cui, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06654v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06654v1)

**Summary:** Multimodal retrieval models are becoming increasingly important in scenarios such as food delivery, where rich multimodal features can meet diverse user needs and enable precise retrieval. Mainstream approaches typically employ a dual-tower architecture between queries and items, and perform joint optimization of intra-tower and inter-tower tasks. However, we observe that joint optimization often leads to certain modalities dominating the training process, while other modalities are neglected. I...

---

### 49. RAPID: Reconfigurable, Adaptive Platform for Iterative Design

**Authors:** Zi Yin, Fanhong Li, Shurui Zheng, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06653v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06653v1)

**Summary:** Developing robotic manipulation policies is iterative and hypothesis-driven: researchers test tactile sensing, gripper geometries, and sensor placements through real-world data collection and training. Yet even minor end-effector changes often require mechanical refitting and system re-integration, slowing iteration. We present RAPID, a full-stack reconfigurable platform designed to reduce this friction. RAPID is built around a tool-free, modular hardware architecture that unifies handheld data ...

---

### 50. Same Answer, Different Representations: Hidden instability in VLMs

**Authors:** Farooq Ahmad Wani, Alessandro Suglia, Rohit Saxena, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06652v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06652v1)

**Summary:** The robustness of Vision Language Models (VLMs) is commonly assessed through output-level invariance, implicitly assuming that stable predictions reflect stable multimodal processing. In this work, we argue that this assumption is insufficient. We introduce a representation-aware and frequency-aware evaluation framework that measures internal embedding drift, spectral sensitivity, and structural smoothness (spatial consistency of vision tokens), alongside standard label-based metrics. Applying t...

---

## cs.CL

**50 papers**

### 1. Learning a Generative Meta-Model of LLM Activations

**Authors:** Grace Luo, Jiahai Feng, Trevor Darrell, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06964v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06964v1)

**Summary:** Existing approaches for analyzing neural network activations, such as PCA and sparse autoencoders, rely on strong structural assumptions. Generative models offer an alternative: they can uncover structure without such assumptions and act as priors that improve intervention fidelity. We explore this direction by training diffusion models on one billion residual stream activations, creating "meta-models" that learn the distribution of a network's internal states. We find that diffusion loss decrea...

---

### 2. InftyThink+: Effective and Efficient Infinite-Horizon Reasoning via Reinforcement Learning

**Authors:** Yuchen Yan, Liang Jiang, Jin Jiang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06960v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06960v1)

**Summary:** Large reasoning models achieve strong performance by scaling inference-time chain-of-thought, but this paradigm suffers from quadratic cost, context length limits, and degraded reasoning due to lost-in-the-middle effects. Iterative reasoning mitigates these issues by periodically summarizing intermediate thoughts, yet existing methods rely on supervised learning or fixed heuristics and fail to optimize when to summarize, what to preserve, and how to resume reasoning. We propose InftyThink+, an e...

---

### 3. DAWN: Dependency-Aware Fast Inference for Diffusion LLMs

**Authors:** Lizhuo Luo, Zhuoran Shi, Jiajun Luo, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06953v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06953v1)

**Summary:** Diffusion large language models (dLLMs) have shown advantages in text generation, particularly due to their inherent ability for parallel decoding. However, constrained by the quality--speed trade-off, existing inference solutions adopt conservative parallel strategies, leaving substantial efficiency potential underexplored. A core challenge is that parallel decoding assumes each position can be filled independently, but tokens are often semantically coupled. Thus, the correct choice at one posi...

---

### 4. Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay

**Authors:** Duygu Altinok

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06942v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06942v1)

**Summary:** Tokenization is a pivotal design choice for neural language modeling in morphologically rich languages (MRLs) such as Turkish, where productive agglutination challenges both vocabulary efficiency and morphological fidelity. Prior studies have explored tokenizer families and vocabulary sizes but typically (i) vary vocabulary without systematically controlling the tokenizer's training corpus, (ii) provide limited intrinsic diagnostics, and (iii) evaluate a narrow slice of downstream tasks. We pres...

---

### 5. Endogenous Resistance to Activation Steering in Language Models

**Authors:** Alex McKenzie, Keenan Pepper, Stijn Servaes, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06941v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06941v1)

**Summary:** Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 SAE latents that activate diff...

---

### 6. Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs

**Authors:** Samir Abdaljalil, Parichit Sharma, Erchin Serpedin, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06920v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06920v1)

**Summary:** Hallucinations in large language models remain a persistent challenge, particularly in multilingual and generative settings where factual consistency is difficult to maintain. While recent models show strong performance on English-centric benchmarks, their behavior across languages, tasks, and hallucination types is not yet well understood. In this work, we introduce Halluverse-M^3, a dataset designed to enable systematic analysis of hallucinations across multiple languages, multiple generation ...

---

### 7. Uncovering Cross-Objective Interference in Multi-Objective Alignment

**Authors:** Yining Lu, Meng Jiang

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06869v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06869v1)

**Summary:** We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross-objective interference and conduct the first systematic study across classic scalarization algorithms, showing that interference is pervasive and exhibits strong model dependence.   To explain this phenomenon, we derive a local covariance law showing that an objective i...

---

### 8. SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks

**Authors:** Mingqian Feng, Xiaodong Liu, Weiwei Yang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06854v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06854v1)

**Summary:** Multi-turn jailbreaks capture the real threat model for safety-aligned chatbots, where single-turn attacks are merely a special case. Yet existing approaches break under exploration complexity and intent drift. We propose SEMA, a simple yet effective framework that trains a multi-turn attacker without relying on any existing strategies or external data. SEMA comprises two stages. Prefilling self-tuning enables usable rollouts by fine-tuning on non-refusal, well-structured, multi-turn adversarial...

---

### 9. The Representational Geometry of Number

**Authors:** Zhimin Hu, Lanhao Niu, Sashank Varma

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06843v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06843v1)

**Summary:** A central question in cognitive science is whether conceptual representations converge onto a shared manifold to support generalization, or diverge into orthogonal subspaces to minimize task interference. While prior work has discovered evidence for both, a mechanistic account of how these properties coexist and transform across tasks remains elusive. We propose that representational sharing lies not in the concepts themselves, but in the geometric relations between them. Using number concepts a...

---

### 10. Visual Word Sense Disambiguation with CLIP through Dual-Channel Text Prompting and Image Augmentations

**Authors:** Shamik Bhattacharya, Daniel Perkins, Yaren Dogan, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06799v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06799v1)

**Summary:** Ambiguity poses persistent challenges in natural language understanding for large language models (LLMs). To better understand how lexical ambiguity can be resolved through the visual domain, we develop an interpretable Visual Word Sense Disambiguation (VWSD) framework. The model leverages CLIP to project ambiguous language and candidate images into a shared multimodal space. We enrich textual embeddings using a dual-channel ensemble of semantic and photo-based prompts with WordNet synonyms, whi...

---

### 11. Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling

**Authors:** Kate Sanders, Nathaniel Weir, Sapana Chaudhary, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06795v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06795v1)

**Summary:** An impediment to using Large Language Models (LLMs) for reasoning output verification is that LLMs struggle to reliably identify errors in thinking traces, particularly in long outputs, domains requiring expert knowledge, and problems without verifiable rewards. We propose a data-driven approach to automatically construct highly granular reasoning error taxonomies to enhance LLM-driven error detection on unseen reasoning traces. Our findings indicate that classification approaches that leverage ...

---

### 12. R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging

**Authors:** Yanlin Lai, Mitt Huang, Hangyu Guo, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06763v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06763v1)

**Summary:** Reinforcement Learning from Human Feedback (RLHF) remains indispensable for aligning large language models (LLMs) in subjective domains. To enhance robustness, recent work shifts toward Generative Reward Models (GenRMs) that generate rationales before predicting preferences. Yet in GenRM training and evaluation, practice remains outcome-label-only, leaving reasoning quality unchecked. We show that reasoning fidelity-the consistency between a GenRM's preference decision and reference decision rat...

---

### 13. Table-as-Search: Formulate Long-Horizon Agentic Information Seeking as Table Completion

**Authors:** Tian Lan, Felix Henry, Bin Zhu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06724v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06724v1)

**Summary:** Current Information Seeking (InfoSeeking) agents struggle to maintain focus and coherence during long-horizon exploration, as tracking search states, including planning procedure and massive search results, within one plain-text context is inherently fragile. To address this, we introduce \textbf{Table-as-Search (TaS)}, a structured planning framework that reformulates the InfoSeeking task as a Table Completion task. TaS maps each query into a structured table schema maintained in an external da...

---

### 14. Quantum Attention by Overlap Interference: Predicting Sequences from Classical and Many-Body Quantum Data

**Authors:** Alessio Pecilli, Matteo Rosati

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06699v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06699v1)

**Summary:** We propose a variational quantum implementation of self-attention (QSA), the core operation in transformers and large language models, which predicts future elements of a sequence by forming overlap-weighted combinations of past data. At variance with previous approaches, our QSA realizes the required nonlinearity through interference of state overlaps and returns a Renyi-1/2 cross-entropy loss directly as the expectation value of an observable, avoiding the need to decode amplitude-encoded pred...

---

### 15. Evaluating Prompt Engineering Strategies for Sentiment Control in AI-Generated Texts

**Authors:** Kerstin Sahler, Sophie Jentzsch

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06692v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06692v1)

**Summary:** The groundbreaking capabilities of Large Language Models (LLMs) offer new opportunities for enhancing human-computer interaction through emotion-adaptive Artificial Intelligence (AI). However, deliberately controlling the sentiment in these systems remains challenging. The present study investigates the potential of prompt engineering for controlling sentiment in LLM-generated text, providing a resource-sensitive and accessible alternative to existing methods. Using Ekman's six basic emotions (e...

---

### 16. compar:IA: The French Government's LLM arena to collect French-language human prompts and preference data

**Authors:** Lucie Termignon, Simonas Zilinskas, Hadrien Pélissier, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06669v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06669v1)

**Summary:** Large Language Models (LLMs) often show reduced performance, cultural alignment, and safety robustness in non-English languages, partly because English dominates both pre-training data and human preference alignment datasets. Training methods like Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) require human preference data, which remains scarce and largely non-public for many languages beyond English. To address this gap, we introduce compar:IA, an ope...

---

### 17. Not All Layers Need Tuning: Selective Layer Restoration Recovers Diversity

**Authors:** Bowen Zhang, Meiyi Wang, Harold Soh

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06665v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06665v1)

**Summary:** Post-training improves instruction-following and helpfulness of large language models (LLMs) but often reduces generation diversity, which leads to repetitive outputs in open-ended settings, a phenomenon known as mode collapse. Motivated by evidence that LLM layers play distinct functional roles, we hypothesize that mode collapse can be localized to specific layers and that restoring a carefully chosen range of layers to their pre-trained weights can recover diversity while maintaining high outp...

---

### 18. Beyond Static Alignment: Hierarchical Policy Control for LLM Safety via Risk-Aware Chain-of-Thought

**Authors:** Jianfeng Si, Lin Sun, Weihong Lin, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06650v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06650v1)

**Summary:** Large Language Models (LLMs) face a fundamental safety-helpfulness trade-off due to static, one-size-fits-all safety policies that lack runtime controllabilityxf, making it difficult to tailor responses to diverse application needs. %As a result, models may over-refuse benign requests or under-constrain harmful ones. We present \textbf{PACT} (Prompt-configured Action via Chain-of-Thought), a framework for dynamic safety control through explicit, risk-aware reasoning. PACT operates under a hierar...

---

### 19. Reading Between the Waves: Robust Topic Segmentation Using Inter-Sentence Audio Features

**Authors:** Steffen Freisinger, Philipp Seeberger, Tobias Bocklet, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06647v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06647v1)

**Summary:** Spoken content, such as online videos and podcasts, often spans multiple topics, which makes automatic topic segmentation essential for user navigation and downstream applications. However, current methods do not fully leverage acoustic features, leaving room for improvement. We propose a multi-modal approach that fine-tunes both a text encoder and a Siamese audio encoder, capturing acoustic cues around sentence boundaries. Experiments on a large-scale dataset of YouTube videos show substantial ...

---

### 20. FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge

**Authors:** Bo Yang, Lanfei Feng, Yunkui Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06625v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06625v1)

**Summary:** Existing LLM-as-a-Judge systems suffer from three fundamental limitations: limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes (e.g., pointwise versus pairwise). To address these issues, we propose FairJudge, an adaptive, debiased, and consistent LLM-as-a-Judge. Unlike prior appr...

---

### 21. Do Prompts Guarantee Safety? Mitigating Toxicity from LLM Generations through Subspace Intervention

**Authors:** Himanshu Singh, Ziwei Xu, A. V. Subramanyam, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06623v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06623v1)

**Summary:** Large Language Models (LLMs) are powerful text generators, yet they can produce toxic or harmful content even when given seemingly harmless prompts. This presents a serious safety challenge and can cause real-world harm. Toxicity is often subtle and context-dependent, making it difficult to detect at the token level or through coarse sentence-level signals. Moreover, efforts to mitigate toxicity often face a trade-off between safety and the coherence, or fluency of the generated text. In this wo...

---

### 22. Echoes as Anchors: Probabilistic Costs and Attention Refocusing in LLM Reasoning

**Authors:** Zhuoyuan Hao, Zhuo Li, Wu Li, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06600v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06600v1)

**Summary:** Test-time compute allocation in large reasoning models (LRMs) is widely used and has applications in mathematical problem solving, code synthesis, and planning. Recent work has addressed this problem by scaling self-consistency and parallel thinking, adding generic ``thinking tokens'' and prompting models to re-read the question before answering. Unfortunately, these approaches either inject task-agnostic tokens or mandate heuristics that do not explain -- and often ignore -- the \emph{spontaneo...

---

### 23. Personality as Relational Infrastructure: User Perceptions of Personality-Trait-Infused LLM Messaging

**Authors:** Dominik P. Hofer, David Haag, Rania Islambouli, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06596v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06596v1)

**Summary:** Digital behaviour change systems increasingly rely on repeated, system-initiated messages to support users in everyday contexts. LLMs enable these messages to be personalised consistently across interactions, yet it remains unclear whether such personalisation improves individual messages or instead shapes users' perceptions through patterns of exposure. We explore this question in the context of LLM-generated JITAIs, which are short, context-aware messages delivered at moments deemed appropriat...

---

### 24. Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning

**Authors:** Deqian Kong, Minglu Zhao, Aoyang Qin, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06584v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06584v1)

**Summary:** Standard chain-of-thought reasoning generates a solution in a single forward pass, committing irrevocably to each token and lacking a mechanism to recover from early errors. We introduce Inference-Time Rethinking, a generative framework that enables iterative self-correction by decoupling declarative latent thought vectors from procedural generation. We factorize reasoning into a continuous latent thought vector (what to reason about) and a decoder that verbalizes the trace conditioned on this v...

---

### 25. Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making

**Authors:** Baichuan-M3 Team,  :, Chengfeng Dou, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06570v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06570v1)

**Summary:** We introduce Baichuan-M3, a medical-enhanced large language model engineered to shift the paradigm from passive question-answering to active, clinical-grade decision support. Addressing the limitations of existing systems in open-ended consultations, Baichuan-M3 utilizes a specialized training pipeline to model the systematic workflow of a physician. Key capabilities include: (i) proactive information acquisition to resolve ambiguity; (ii) long-horizon reasoning that unifies scattered evidence i...

---

### 26. SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs

**Authors:** Niccolo Avogaro, Nayanika Debnath, Li Mi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06566v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06566v1)

**Summary:** Despite recent successes, test-time scaling - i.e., dynamically expanding the token budget during inference as needed - remains brittle for vision-language models (VLMs): unstructured chains-of-thought about images entangle perception and reasoning, leading to long, disorganized contexts where small perceptual mistakes may cascade into completely wrong answers. Moreover, expensive reinforcement learning with hand-crafted rewards is required to achieve good performance. Here, we introduce SPARC (...

---

### 27. Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study

**Authors:** Yi Liu, Zhihao Chen, Yanjun Zhang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06547v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06547v1)

**Summary:** Third-party agent skills extend LLM-based agents with instruction files and executable code that run on users' machines. Skills execute with user privileges and are distributed through community registries with minimal vetting, but no ground-truth dataset exists to characterize the resulting threats. We construct the first labeled dataset of malicious agent skills by behaviorally verifying 98,380 skills from two community registries, confirming 157 malicious skills with 632 vulnerabilities. Thes...

---

### 28. MTQE.en-he: Machine Translation Quality Estimation for English-Hebrew

**Authors:** Andy Rosenbaum, Assaf Siani, Ilan Kernerman

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06546v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06546v1)

**Summary:** We release MTQE.en-he: to our knowledge, the first publicly available English-Hebrew benchmark for Machine Translation Quality Estimation. MTQE.en-he contains 959 English segments from WMT24++, each paired with a machine translation into Hebrew, and Direct Assessment scores of the translation quality annotated by three human experts. We benchmark ChatGPT prompting, TransQuest, and CometKiwi and show that ensembling the three models outperforms the best single model (CometKiwi) by 6.4 percentage ...

---

### 29. AgentCPM-Report: Interleaving Drafting and Deepening for Open-Ended Deep Research

**Authors:** Yishan Li, Wentong Chen, Yukun Yan, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06540v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06540v1)

**Summary:** Generating deep research reports requires large-scale information acquisition and the synthesis of insight-driven analysis, posing a significant challenge for current language models. Most existing approaches follow a plan-then-write paradigm, whose performance heavily depends on the quality of the initial outline. However, constructing a comprehensive outline itself demands strong reasoning ability, causing current deep research systems to rely almost exclusively on closed-source or online larg...

---

### 30. LogicSkills: A Structured Benchmark for Formal Reasoning in Large Language Models

**Authors:** Brian Rabern, Philipp Mondorf, Barbara Plank

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06533v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06533v1)

**Summary:** Large language models have demonstrated notable performance across various logical reasoning benchmarks. However, it remains unclear which core logical skills they truly master. To address this, we introduce LogicSkills, a unified benchmark designed to isolate three fundamental skills in formal reasoning: (i) $\textit{formal symbolization}\unicode{x2014}$translating premises into first-order logic; (ii) $\textit{countermodel construction}\unicode{x2014}$formulating a finite structure in which al...

---

### 31. Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks

**Authors:** Minjeong Ban, Jeonghwan Choi, Hyangsuk Min, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06526v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06526v1)

**Summary:** Information retrieval (IR) evaluation remains challenging due to incomplete IR benchmark datasets that contain unlabeled relevant chunks. While LLMs and LLM-human hybrid strategies reduce costly human effort, they remain prone to LLM overconfidence and ineffective AI-to-human escalation. To address this, we propose DREAM, a multi-round debate-based relevance assessment framework with LLM agents, built on opposing initial stances and iterative reciprocal critique. Through our agreement-based deba...

---

### 32. Designing Computational Tools for Exploring Causal Relationships in Qualitative Data

**Authors:** Han Meng, Qiuyuan Lyu, Peinuan Qin, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06506v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06506v1)

**Summary:** Exploring causal relationships for qualitative data analysis in HCI and social science research enables the understanding of user needs and theory building. However, current computational tools primarily characterize and categorize qualitative data; the few systems that analyze causal relationships either inadequately consider context, lack credibility, or produce overly complex outputs. We first conducted a formative study with 15 participants interested in using computational tools for explori...

---

### 33. Revisiting the Shape Convention of Transformer Language Models

**Authors:** Feng-Ting Liao, Meng-Hsi Chen, Guan-Ting Yi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06471v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06471v1)

**Summary:** Dense Transformer language models have largely adhered to one consistent architectural shape: each layer consists of an attention module followed by a feed-forward network (FFN) with a narrow-wide-narrow MLP, allocating most parameters to the MLP at expansion ratios between 2 and 4. Motivated by recent results that residual wide-narrow-wide (hourglass) MLPs offer superior function approximation capabilities, we revisit the long-standing MLP shape convention in Transformer, challenging the necess...

---

### 34. Improve Large Language Model Systems with User Logs

**Authors:** Changyue Wang, Weihang Su, Qingyao Ai, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06470v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06470v1)

**Summary:** Scaling training data and model parameters has long driven progress in large language models (LLMs), but this paradigm is increasingly constrained by the scarcity of high-quality data and diminishing returns from rising computational costs. As a result, recent work is increasing the focus on continual learning from real-world deployment, where user interaction logs provide a rich source of authentic human feedback and procedural knowledge. However, learning from user logs is challenging due to t...

---

### 35. Diffusion-State Policy Optimization for Masked Diffusion Language Models

**Authors:** Daisuke Oba, Hiroki Furuta, Naoaki Okazaki

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06462v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06462v1)

**Summary:** Masked diffusion language models generate by iteratively filling masked tokens over multiple denoising steps, so learning only from a terminal reward on the final completion yields coarse credit assignment over intermediate decisions. We propose DiSPO (Diffusion-State Policy Optimization), a plug-in credit-assignment layer that directly optimizes intermediate filling decisions. At selected intermediate masked states, DiSPO branches by resampling fillings for the currently masked positions from r...

---

### 36. RelayGen: Intra-Generation Model Switching for Efficient Reasoning

**Authors:** Jiwon Song, Yoongon Kim, Jae-Joon Kim

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06454v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06454v1)

**Summary:** Large reasoning models (LRMs) achieve strong performance on complex reasoning tasks by generating long, multi-step reasoning trajectories, but inference-time scaling incurs substantial deployment cost. A key challenge is that generation difficulty varies within a single output, whereas existing efficiency-oriented approaches either ignore this intra-generation variation or rely on supervised token-level routing with high system complexity. We present \textbf{RelayGen}, a training-free, segment-l...

---

### 37. Evaluating an evidence-guided reinforcement learning framework in aligning light-parameter large language models with decision-making cognition in psychiatric clinical reasoning

**Authors:** Xinxin Lin, Guangxin Dai, Yi Zhong, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06449v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06449v1)

**Summary:** Large language models (LLMs) hold transformative potential for medical decision support yet their application in psychiatry remains constrained by hallucinations and superficial reasoning. This limitation is particularly acute in light-parameter LLMs which are essential for privacy-preserving and efficient clinical deployment. Existing training paradigms prioritize linguistic fluency over structured clinical logic and result in a fundamental misalignment with professional diagnostic cognition. H...

---

### 38. CORE: Comprehensive Ontological Relation Evaluation for Large Language Models

**Authors:** Satyam Dwivedi, Sanjukta Ghosh, Shivam Dwivedi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06446v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06446v1)

**Summary:** Large Language Models (LLMs) perform well on many reasoning benchmarks, yet existing evaluations rarely assess their ability to distinguish between meaningful semantic relations and genuine unrelatedness. We introduce CORE (Comprehensive Ontological Relation Evaluation), a dataset of 225K multiple-choice questions spanning 74 disciplines, together with a general-domain open-source benchmark of 203 rigorously validated questions (Cohen's Kappa = 1.0) covering 24 semantic relation types with equal...

---

### 39. TrailBlazer: History-Guided Reinforcement Learning for Black-Box LLM Jailbreaking

**Authors:** Sung-Hoon Yoon, Ruizhi Qian, Minda Zhao, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06440v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06440v1)

**Summary:** Large Language Models (LLMs) have become integral to many domains, making their safety a critical priority. Prior jailbreaking research has explored diverse approaches, including prompt optimization, automated red teaming, obfuscation, and reinforcement learning (RL) based methods. However, most existing techniques fail to effectively leverage vulnerabilities revealed in earlier interaction turns, resulting in inefficient and unstable attacks. Since jailbreaking involves sequential interactions ...

---

### 40. Investigating the structure of emotions by analyzing similarity and association of emotion words

**Authors:** Fumitaka Iwaki, Tatsuji Takahashi

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06430v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06430v1)

**Summary:** In the field of natural language processing, some studies have attempted sentiment analysis on text by handling emotions as explanatory or response variables. One of the most popular emotion models used in this context is the wheel of emotion proposed by Plutchik. This model schematizes human emotions in a circular structure, and represents them in two or three dimensions. However, the validity of Plutchik's wheel of emotion has not been sufficiently examined. This study investigated the validit...

---

### 41. On the Wings of Imagination: Conflicting Script-based Multi-role Framework for Humor Caption Generation

**Authors:** Wenbo Shang, Yuxi Sun, Jing Ma, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06423v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06423v1)

**Summary:** Humor is a commonly used and intricate human language in daily life. Humor generation, especially in multi-modal scenarios, is a challenging task for large language models (LLMs), which is typically as funny caption generation for images, requiring visual understanding, humor reasoning, creative imagination, and so on. Existing LLM-based approaches rely on reasoning chains or self-improvement, which suffer from limited creativity and interpretability. To address these bottlenecks, we develop a n...

---

### 42. Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding

**Authors:** Daisuke Oba, Danushka Bollegala, Masahiro Kaneko, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06412v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06412v1)

**Summary:** Masked Diffusion Language Models generate sequences via iterative sampling that progressively unmasks tokens. However, they still recompute the attention and feed-forward blocks for every token position at every step -- even when many unmasked tokens are essentially fixed, resulting in substantial waste in compute. We propose SureLock: when the posterior at an unmasked position has stabilized across steps (our sure condition), we lock that position -- thereafter skipping its query projection and...

---

### 43. FMBench: Adaptive Large Language Model Output Formatting

**Authors:** Yaoting Wang, Yun Zhou, Henghui Ding

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06384v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06384v1)

**Summary:** Producing outputs that satisfy both semantic intent and format constraints is essential for deploying large language models in user-facing and system-integrated workflows. In this work, we focus on Markdown formatting, which is ubiquitous in assistants, documentation, and tool-augmented pipelines but still prone to subtle, hard-to-detect errors (e.g., broken lists, malformed tables, inconsistent headings, and invalid code blocks) that can significantly degrade downstream usability. We present FM...

---

### 44. ReBeCA: Unveiling Interpretable Behavior Hierarchy behind the Iterative Self-Reflection of Language Models with Causal Analysis

**Authors:** Tianqiang Yan, Sihan Shang, Yuheng Li, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06373v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06373v1)

**Summary:** While self-reflection can enhance language model reliability, its underlying mechanisms remain opaque, with existing analyses often yielding correlation-based insights that fail to generalize. To address this, we introduce \textbf{\texttt{ReBeCA}} (self-\textbf{\texttt{Re}}flection \textbf{\texttt{Be}}havior explained through \textbf{\texttt{C}}ausal \textbf{\texttt{A}}nalysis), a framework that unveils the interpretable behavioral hierarchy governing the self-reflection outcome. By modeling sel...

---

### 45. Cost-Aware Model Selection for Text Classification: Multi-Objective Trade-offs Between Fine-Tuned Encoders and LLM Prompting in Production

**Authors:** Alberto Andres Valdes Gonzalez

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06370v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06370v1)

**Summary:** Large language models (LLMs) such as GPT-4o and Claude Sonnet 4.5 have demonstrated strong capabilities in open-ended reasoning and generative language tasks, leading to their widespread adoption across a broad range of NLP applications. However, for structured text classification problems with fixed label spaces, model selection is often driven by predictive performance alone, overlooking operational constraints encountered in production systems.   In this work, we present a systematic comparis...

---

### 46. SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass

**Authors:** Yewei Liu, Xiyuan Wang, Yansheng Mao, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06358v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06358v1)

**Summary:** We propose SHINE (Scalable Hyper In-context NEtwork), a scalable hypernetwork that can map diverse meaningful contexts into high-quality LoRA adapters for large language models (LLM). By reusing the frozen LLM's own parameters in an in-context hypernetwork design and introducing architectural innovations, SHINE overcomes key limitations of prior hypernetworks and achieves strong expressive power with a relatively small number of parameters. We introduce a pretraining and instruction fine-tuning ...

---

### 47. Can Post-Training Transform LLMs into Causal Reasoners?

**Authors:** Junqi Chen, Sirui Chen, Chaochao Lu

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06337v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06337v1)

**Summary:** Causal inference is essential for decision-making but remains challenging for non-experts. While large language models (LLMs) show promise in this domain, their precise causal estimation capabilities are still limited, and the impact of post-training on these abilities is insufficiently explored. This paper examines the extent to which post-training can enhance LLMs' capacity for causal inference. We introduce CauGym, a comprehensive dataset comprising seven core causal tasks for training and fi...

---

### 48. The Condensate Theorem: Transformers are O(n), Not $O(n^2)$

**Authors:** Jorge L. Ruiz Williams

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06317v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06317v1)

**Summary:** We present the Condensate Theorem: attention sparsity is a learned topological property, not an architectural constraint. Through empirical analysis of trained language models, we find that attention mass concentrates on a distinct topological manifold -- and this manifold can be identified dynamically without checking every position. We prove a general result: for any query, projecting attention onto the Condensate Manifold (Anchor + Window + Dynamic Top-k) achieves 100% output equivalence with...

---

### 49. Lost in Speech: Benchmarking, Evaluation, and Parsing of Spoken Code-Switching Beyond Standard UD Assumptions

**Authors:** Nemika Tyagi, Holly Hendrix, Nelvin Licona-Guevara, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06307v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06307v1)

**Summary:** Spoken code-switching (CSW) challenges syntactic parsing in ways not observed in written text. Disfluencies, repetition, ellipsis, and discourse-driven structure routinely violate standard Universal Dependencies (UD) assumptions, causing parsers and large language models (LLMs) to fail despite strong performance on written data. These failures are compounded by rigid evaluation metrics that conflate genuine structural errors with acceptable variation. In this work, we present a systems-oriented ...

---

### 50. Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math

**Authors:** Guijin Son, Donghun Yang, Hitesh Laxmichand Patel, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06291v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06291v1)

**Summary:** Recent progress in reasoning models suggests that generating plausible attempts for research-level mathematics may be within reach, but verification remains a bottleneck, consuming scarce expert time. We hypothesize that a meaningful solution should contain enough method-level information that, when applied to a neighborhood of related questions, it should yield better downstream performance than incorrect solutions. Building on this idea, we propose \textbf{Consequence-Based Utility}, an oracle...

---

## cs.CV

**50 papers**

### 1. MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images

**Authors:** Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06965v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06965v1)

**Summary:** Multimodal large language models (MLLMs) have rapidly advanced, yet their adoption in medicine remains limited by gaps in domain coverage, modality alignment, and grounded reasoning. In this work, we introduce MedMO, a medical foundation model built upon a generalized MLLM architecture and trained exclusively on large-scale, domain-specific data. MedMO follows a multi-stage training recipe: (i) cross-modal pretraining to align heterogeneous visual encoders with a medical language backbone; (ii) ...

---

### 2. CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation

**Authors:** Kaiyi Huang, Yukun Huang, Yu Li, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06959v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06959v1)

**Summary:** Cinematic video production requires control over scene-subject composition and camera movement, but live-action shooting remains costly due to the need for constructing physical sets. To address this, we introduce the task of cinematic video generation with decoupled scene context: given multiple images of a static environment, the goal is to synthesize high-quality videos featuring dynamic subject while preserving the underlying scene consistency and following a user-specified camera trajectory...

---

### 3. DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

**Authors:** Shenyuan Gao, William Liang, Kaiyuan Zheng, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06949v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06949v1)

**Summary:** Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture r...

---

### 4. Reliable Mislabel Detection for Video Capsule Endoscopy Data

**Authors:** Julia Werner, Julius Oexle, Oliver Bause, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06938v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06938v1)

**Summary:** The classification performance of deep neural networks relies strongly on access to large, accurately annotated datasets. In medical imaging, however, obtaining such datasets is particularly challenging since annotations must be provided by specialized physicians, which severely limits the pool of annotators. Furthermore, class boundaries can often be ambiguous or difficult to define which further complicates machine learning-based classification. In this paper, we want to address this problem a...

---

### 5. Seeing Beyond Redundancy: Task Complexity's Role in Vision Token Specialization in VLLMs

**Authors:** Darryl Hannan, John Cooper, Dylan White, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06914v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06914v1)

**Summary:** Vision capabilities in vision large language models (VLLMs) have consistently lagged behind their linguistic capabilities. In particular, numerous benchmark studies have demonstrated that VLLMs struggle when fine-grained visual information or spatial reasoning is required. However, we do not yet understand exactly why VLLMs struggle so much with these tasks relative to others. Some works have focused on visual redundancy as an explanation, where high-level visual information is uniformly spread ...

---

### 6. PANC: Prior-Aware Normalized Cut for Object Segmentation

**Authors:** Juan Gutiérrez, Victor Gutiérrez-Garcia, José Luis Blanco-Murillo

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06912v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06912v1)

**Summary:** Fully unsupervised segmentation pipelines naively seek the most salient object, should this be present. As a result, most of the methods reported in the literature deliver non-deterministic partitions that are sensitive to initialization, seed order, and threshold heuristics.   We propose PANC, a weakly supervised spectral segmentation framework that uses a minimal set of annotated visual tokens to produce stable, controllable, and reproducible object masks. From the TokenCut approach, we augmen...

---

### 7. Prompt Reinjection: Alleviating Prompt Forgetting in Multimodal Diffusion Transformers

**Authors:** Yuxuan Yao, Yuxuan Chen, Hui Li, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06886v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06886v1)

**Summary:** Multimodal Diffusion Transformers (MMDiTs) for text-to-image generation maintain separate text and image branches, with bidirectional information flow between text tokens and visual latents throughout denoising. In this setting, we observe a prompt forgetting phenomenon: the semantics of the prompt representation in the text branch is progressively forgotten as depth increases. We further verify this effect on three representative MMDiTs--SD3, SD3.5, and FLUX.1 by probing linguistic attributes o...

---

### 8. Vision Transformer Finetuning Benefits from Non-Smooth Components

**Authors:** Ambroise Odonnat, Laetitia Chapel, Romain Tavenard, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06883v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06883v1)

**Summary:** The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, or, in other words, their plasticity. Defined as an average rate of change, it captures the sensitivity to input perturbation; in particular, a high plasticity ...

---

### 9. NanoFLUX: Distillation-Driven Compression of Large Text-to-Image Generation Models for Mobile Devices

**Authors:** Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Couto Pimentel Ramos, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06879v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06879v1)

**Summary:** While large-scale text-to-image diffusion models continue to improve in visual quality, their increasing scale has widened the gap between state-of-the-art models and on-device solutions. To address this gap, we introduce NanoFLUX, a 2.4B text-to-image flow-matching model distilled from 17B FLUX.1-Schnell using a progressive compression pipeline designed to preserve generation quality. Our contributions include: (1) A model compression strategy driven by pruning redundant components in the diffu...

---

### 10. RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing

**Authors:** Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06871v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06871v1)

**Summary:** Instructional video editing applies edits to an input video using only text prompts, enabling intuitive natural-language control. Despite rapid progress, most methods still require fixed-length inputs and substantial compute. Meanwhile, autoregressive video generation enables efficient variable-length synthesis, yet remains under-explored for video editing. We introduce a causal, efficient video editing model that edits variable-length videos frame by frame. For efficiency, we start from a 2D im...

---

### 11. Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing

**Authors:** Meng Lou, Stanley Yu, Yizhou Yu

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06862v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06862v1)

**Summary:** Adapting pre-trained vision models using parameter-efficient fine-tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine-tuning using a minimal number of trainable parameters. When applied to complex dense prediction tasks, existing methods exhibit limitations, including input-agnostic modeling and redundant cross-layer representations. To this end, we propose AdaRoute, a new adapter-style method featuring a simple mixture-of-experts (MoE) architecture. Spec...

---

### 12. Rethinking Multi-Condition DiTs: Eliminating Redundant Attention via Position-Alignment and Keyword-Scoping

**Authors:** Chao Zhou, Tianyi Wei, Yiling Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06850v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06850v1)

**Summary:** While modern text-to-image models excel at prompt-based generation, they often lack the fine-grained control necessary for specific user requirements like spatial layouts or subject appearances. Multi-condition control addresses this, yet its integration into Diffusion Transformers (DiTs) is bottlenecked by the conventional ``concatenate-and-attend'' strategy, which suffers from quadratic computational and memory overhead as the number of conditions scales. Our analysis reveals that much of this...

---

### 13. GaussianPOP: Principled Simplification Framework for Compact 3D Gaussian Splatting via Error Quantification

**Authors:** Soonbin Lee, Yeong-Gyu Kim, Simon Sasse, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06830v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06830v1)

**Summary:** Existing 3D Gaussian Splatting simplification methods commonly use importance scores, such as blending weights or sensitivity, to identify redundant Gaussians. However, these scores are not driven by visual error metrics, often leading to suboptimal trade-offs between compactness and rendering fidelity. We present GaussianPOP, a principled simplification framework based on analytical Gaussian error quantification. Our key contribution is a novel error criterion, derived directly from the 3DGS re...

---

### 14. AEGPO: Adaptive Entropy-Guided Policy Optimization for Diffusion Models

**Authors:** Yuming Li, Qingyu Li, Chengyu Bai, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06825v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06825v1)

**Summary:** Reinforcement learning from human feedback (RLHF) shows promise for aligning diffusion and flow models, yet policy optimization methods such as GRPO suffer from inefficient and static sampling strategies. These methods treat all prompts and denoising steps uniformly, ignoring substantial variations in sample learning value as well as the dynamic nature of critical exploration moments.   To address this issue, we conduct a detailed analysis of the internal attention dynamics during GRPO training ...

---

### 15. RAIGen: Rare Attribute Identification in Text-to-Image Generative Models

**Authors:** Silpa Vadakkeeveetil Sreelatha, Dan Wang, Serge Belongie, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06806v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06806v1)

**Summary:** Text-to-image diffusion models achieve impressive generation quality but inherit and amplify training-data biases, skewing coverage of semantic attributes. Prior work addresses this in two ways. Closed-set approaches mitigate biases in predefined fairness categories (e.g., gender, race), assuming socially salient minority attributes are known a priori. Open-set approaches frame the task as bias identification, highlighting majority attributes that dominate outputs. Both overlook a complementary ...

---

### 16. A Unified Formula for Affine Transformations between Calibrated Cameras

**Authors:** Levente Hajder

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06805v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06805v1)

**Summary:** In this technical note, we derive a closed-form expression for the affine transformation mapping local image patches between two calibrated views. We show that the transformation is a function of the relative camera pose, the image coordinates, and the local surface normal.

---

### 17. Machine Learning for Detection and Severity Estimation of Sweetpotato Weevil Damage in Field and Lab Conditions

**Authors:** Doreen M. Chelangat, Sudi Murindanyi, Bruce Mugizi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06786v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06786v1)

**Summary:** Sweetpotato weevils (Cylas spp.) are considered among the most destructive pests impacting sweetpotato production, particularly in sub-Saharan Africa. Traditional methods for assessing weevil damage, predominantly relying on manual scoring, are labour-intensive, subjective, and often yield inconsistent results. These challenges significantly hinder breeding programs aimed at developing resilient sweetpotato varieties. This study introduces a computer vision-based approach for the automated evalu...

---

### 18. Revisiting Emotions Representation for Recognition in the Wild

**Authors:** Joao Baptista Cardia Neto, Claudio Ferrari, Stefano Berretti

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06778v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06778v1)

**Summary:** Facial emotion recognition has been typically cast as a single-label classification problem of one out of six prototypical emotions. However, that is an oversimplification that is unsuitable for representing the multifaceted spectrum of spontaneous emotional states, which are most often the result of a combination of multiple emotions contributing at different intensities. Building on this, a promising direction that was explored recently is to cast emotion recognition as a distribution learning...

---

### 19. Orientation-Robust Latent Motion Trajectory Learning for Annotation-free Cardiac Phase Detection in Fetal Echocardiography

**Authors:** Yingyu Yang, Qianye Yang, Can Peng, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06761v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06761v1)

**Summary:** Fetal echocardiography is essential for detecting congenital heart disease (CHD), facilitating pregnancy management, optimized delivery planning, and timely postnatal interventions. Among standard imaging planes, the four-chamber (4CH) view provides comprehensive information for CHD diagnosis, where clinicians carefully inspect the end-diastolic (ED) and end-systolic (ES) phases to evaluate cardiac structure and motion. Automated detection of these cardiac phases is thus a critical component tow...

---

### 20. Gold Exploration using Representations from a Multispectral Autoencoder

**Authors:** Argyro Tsandalidou, Konstantinos Dogeas, Eleftheria Tetoula Tsonga, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06748v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06748v1)

**Summary:** Satellite imagery is employed for large-scale prospectivity mapping due to the high cost and typically limited availability of on-site mineral exploration data. In this work, we present a proof-of-concept framework that leverages generative representations learned from multispectral Sentinel-2 imagery to identify gold-bearing regions from space. An autoencoder foundation model, called Isometric, which is pretrained on the large-scale FalconSpace-S2 v1.0 dataset, produces information-dense spectr...

---

### 21. Clinical-Prior Guided Multi-Modal Learning with Latent Attention Pooling for Gait-Based Scoliosis Screening

**Authors:** Dong Chen, Zizhuang Wei, Jialei Xu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06743v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06743v1)

**Summary:** Adolescent Idiopathic Scoliosis (AIS) is a prevalent spinal deformity whose progression can be mitigated through early detection. Conventional screening methods are often subjective, difficult to scale, and reliant on specialized clinical expertise. Video-based gait analysis offers a promising alternative, but current datasets and methods frequently suffer from data leakage, where performance is inflated by repeated clips from the same individual, or employ oversimplified models that lack clinic...

---

### 22. Diffeomorphism-Equivariant Neural Networks

**Authors:** Josephine Elisabeth Oettinger, Zakhar Shumaylov, Johannes Bostelmann, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06695v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06695v1)

**Summary:** Incorporating group symmetries via equivariance into neural networks has emerged as a robust approach for overcoming the efficiency and data demands of modern deep learning. While most existing approaches, such as group convolutions and averaging-based methods, focus on compact, finite, or low-dimensional groups with linear actions, this work explores how equivariance can be extended to infinite-dimensional groups. We propose a strategy designed to induce diffeomorphism equivariance in pre-train...

---

### 23. Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction

**Authors:** Bo Du, Xiaochen Ma, Xuekang Zhu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06676v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06676v1)

**Summary:** Fake Image Detection (FID), aiming at unified detection across four image forensic subdomains, is critical in real-world forensic scenarios. Compared with ensemble approaches, monolithic FID models are theoretically more promising, but to date, consistently yield inferior performance in practice. In this work, by discovering the ``heterogeneous phenomenon'', which is the intrinsic distinctness of artifacts across subdomains, we diagnose the cause of this underperformance for the first time: the ...

---

### 24. CytoCrowd: A Multi-Annotator Benchmark Dataset for Cytology Image Analysis

**Authors:** Yonghao Si, Xingyuan Zeng, Zhao Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06674v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06674v1)

**Summary:** High-quality annotated datasets are crucial for advancing machine learning in medical image analysis. However, a critical gap exists: most datasets either offer a single, clean ground truth, which hides real-world expert disagreement, or they provide multiple annotations without a separate gold standard for objective evaluation. To bridge this gap, we introduce CytoCrowd, a new public benchmark for cytology analysis. The dataset features 446 high-resolution images, each with two key components: ...

---

### 25. PlanViz: Evaluating Planning-Oriented Image Generation and Editing for Computer-Use Tasks

**Authors:** Junxian Li, Kai Liu, Leyang Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06663v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06663v1)

**Summary:** Unified multimodal models (UMMs) have shown impressive capabilities in generating natural images and supporting multimodal reasoning. However, their potential in supporting computer-use planning tasks, which are closely related to our lives, remain underexplored. Image generation and editing in computer-use tasks require capabilities like spatial reasoning and procedural understanding, and it is still unknown whether UMMs have these capabilities to finish these tasks or not. Therefore, we propos...

---

### 26. Same Answer, Different Representations: Hidden instability in VLMs

**Authors:** Farooq Ahmad Wani, Alessandro Suglia, Rohit Saxena, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06652v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06652v1)

**Summary:** The robustness of Vision Language Models (VLMs) is commonly assessed through output-level invariance, implicitly assuming that stable predictions reflect stable multimodal processing. In this work, we argue that this assumption is insufficient. We introduce a representation-aware and frequency-aware evaluation framework that measures internal embedding drift, spectral sensitivity, and structural smoothness (spatial consistency of vision tokens), alongside standard label-based metrics. Applying t...

---

### 27. CauCLIP: Bridging the Sim-to-Real Gap in Surgical Video Understanding via Causality-Inspired Vision-Language Modeling

**Authors:** Yuxin He, An Li, Cheng Xue

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06619v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06619v1)

**Summary:** Surgical phase recognition is a critical component for context-aware decision support in intelligent operating rooms, yet training robust models is hindered by limited annotated clinical videos and large domain gaps between synthetic and real surgical data. To address this, we propose CauCLIP, a causality-inspired vision-language framework that leverages CLIP to learn domain-invariant representations for surgical phase recognition without access to target domain data. Our approach integrates a f...

---

### 28. DAVE: Distribution-aware Attribution via ViT Gradient Decomposition

**Authors:** Adam Wróbel, Siddhartha Gairola, Jacek Tabor, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06613v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06613v1)

**Summary:** Vision Transformers (ViTs) have become a dominant architecture in computer vision, yet producing stable and high-resolution attribution maps for these models remains challenging. Architectural components such as patch embeddings and attention routing often introduce structured artifacts in pixel-level explanations, causing many existing methods to rely on coarse patch-level attributions. We introduce DAVE \textit{(\underline{D}istribution-aware \underline{A}ttribution via \underline{V}iT Gradien...

---

### 29. ProtoQuant: Quantization of Prototypical Parts For General and Fine-Grained Image Classification

**Authors:** Mikołaj Janusz, Adam Wróbel, Bartosz Zieliński, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06592v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06592v1)

**Summary:** Prototypical parts-based models offer a "this looks like that" paradigm for intrinsic interpretability, yet they typically struggle with ImageNet-scale generalization and often require computationally expensive backbone finetuning. Furthermore, existing methods frequently suffer from "prototype drift," where learned prototypes lack tangible grounding in the training distribution and change their activation under small perturbations. We present ProtoQuant, a novel architecture that achieves proto...

---

### 30. An Integer Linear Programming Approach to Geometrically Consistent Partial-Partial Shape Matching

**Authors:** Viktoria Ehm, Paul Roetzer, Florian Bernard, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06590v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06590v1)

**Summary:** The task of establishing correspondences between two 3D shapes is a long-standing challenge in computer vision. While numerous studies address full-full and partial-full 3D shape matching, only a limited number of works have explored the partial-partial setting, very likely due to its unique challenges: we must compute accurate correspondences while at the same time find the unknown overlapping region. Nevertheless, partial-partial 3D shape matching reflects the most realistic setting, as in man...

---

### 31. Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation

**Authors:** Fangyuan Wang, Peng Zhou, Jiaming Qi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06575v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06575v1)

**Summary:** Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, which prevents robot state from shaping instruction understanding and from influencing which visual tokens are attended throughout the policy. We introduce ThinkProprio, which converts proprioception into a sequence of text tokens in the VLM embedding space and fuses them with the task instruction at the input. This early fusion lets embodied state participate in subsequent visual reasoning an...

---

### 32. SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs

**Authors:** Niccolo Avogaro, Nayanika Debnath, Li Mi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06566v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06566v1)

**Summary:** Despite recent successes, test-time scaling - i.e., dynamically expanding the token budget during inference as needed - remains brittle for vision-language models (VLMs): unstructured chains-of-thought about images entangle perception and reasoning, leading to long, disorganized contexts where small perceptual mistakes may cascade into completely wrong answers. Moreover, expensive reinforcement learning with hand-crafted rewards is required to achieve good performance. Here, we introduce SPARC (...

---

### 33. LIBERO-X: Robustness Litmus for Vision-Language-Action Models

**Authors:** Guodong Wang, Chenkai Zhang, Qingjie Liu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06556v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06556v1)

**Summary:** Reliable benchmarking is critical for advancing Vision-Language-Action (VLA) models, as it reveals their generalization, robustness, and alignment of perception with language-driven manipulation tasks. However, existing benchmarks often provide limited or misleading assessments due to insufficient evaluation protocols that inadequately capture real-world distribution shifts. This work systematically rethinks VLA benchmarking from both evaluation and data perspectives, introducing LIBERO-X, a ben...

---

### 34. NECromancer: Breathing Life into Skeletons via BVH Animation

**Authors:** Mingxi Xu, Qi Wang, Zhengyu Wen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06548v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06548v1)

**Summary:** Motion tokenization is a key component of generalizable motion models, yet most existing approaches are restricted to species-specific skeletons, limiting their applicability across diverse morphologies. We propose NECromancer (NEC), a universal motion tokenizer that operates directly on arbitrary BVH skeletons. NEC consists of three components: (1) an Ontology-aware Skeletal Graph Encoder (OwO) that encodes structural priors from BVH files, including joint semantics, rest-pose offsets, and skel...

---

### 35. Universal Anti-forensics Attack against Image Forgery Detection via Multi-modal Guidance

**Authors:** Haipeng Li, Rongxuan Peng, Anwei Luo, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06530v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06530v1)

**Summary:** The rapid advancement of AI-Generated Content (AIGC) technologies poses significant challenges for authenticity assessment. However, existing evaluation protocols largely overlook anti-forensics attack, failing to ensure the comprehensive robustness of state-of-the-art AIGC detectors in real-world applications. To bridge this gap, we propose ForgeryEraser, a framework designed to execute universal anti-forensics attack without access to the target AIGC detectors. We reveal an adversarial vulnera...

---

### 36. AdaptOVCD: Training-Free Open-Vocabulary Remote Sensing Change Detection via Adaptive Information Fusion

**Authors:** Mingyu Dou, Shi Qiu, Ming Hu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06529v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06529v1)

**Summary:** Remote sensing change detection plays a pivotal role in domains such as environmental monitoring, urban planning, and disaster assessment. However, existing methods typically rely on predefined categories and large-scale pixel-level annotations, which limit their generalization and applicability in open-world scenarios. To address these limitations, this paper proposes AdaptOVCD, a training-free Open-Vocabulary Change Detection (OVCD) architecture based on dual-dimensional multi-level informatio...

---

### 37. MicroBi-ConvLSTM: An Ultra-Lightweight Efficient Model for Human Activity Recognition on Resource Constrained Devices

**Authors:** Mridankan Mandal

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06523v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06523v1)

**Summary:** Human Activity Recognition (HAR) on resource constrained wearables requires models that balance accuracy against strict memory and computational budgets. State of the art lightweight architectures such as TinierHAR (34K parameters) and TinyHAR (55K parameters) achieve strong accuracy, but exceed memory budgets of microcontrollers with limited SRAM once operating system overhead is considered. We present MicroBi-ConvLSTM, an ultra-lightweight convolutional-recurrent architecture achieving 11.4K p...

---

### 38. DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving

**Authors:** Feiyang jia, Lin Liu, Ziying Song, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06521v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06521v1)

**Summary:** End-to-end (E2E) autonomous driving has recently attracted increasing interest in unifying Vision-Language-Action (VLA) with World Models to enhance decision-making and forward-looking imagination. However, existing methods fail to effectively unify future scene evolution and action planning within a single architecture due to inadequate sharing of latent states, limiting the impact of visual imagination on action decisions. To address this limitation, we propose DriveWorld-VLA, a novel framewor...

---

### 39. FloorplanVLM: A Vision-Language Model for Floorplan Vectorization

**Authors:** Yuanqing Liu, Ziming Yang, Yulong Li, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06507v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06507v1)

**Summary:** Converting raster floorplans into engineering-grade vector graphics is challenging due to complex topology and strict geometric constraints. To address this, we present FloorplanVLM, a unified framework that reformulates floorplan vectorization as an image-conditioned sequence modeling task. Unlike pixel-based methods that rely on fragile heuristics or query-based transformers that generate fragmented rooms, our model directly outputs structured JSON sequences representing the global topology. T...

---

### 40. MultiGraspNet: A Multitask 3D Vision Model for Multi-gripper Robotic Grasping

**Authors:** Stephany Ortuno-Chanelo, Paolo Rabino, Enrico Civitelli, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06504v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06504v1)

**Summary:** Vision-based models for robotic grasping automate critical, repetitive, and draining industrial tasks. Existing approaches are typically limited in two ways: they either target a single gripper and are potentially applied on costly dual-arm setups, or rely on custom hybrid grippers that require ad-hoc learning procedures with logic that cannot be transferred across tasks, restricting their general applicability. In this work, we present MultiGraspNet, a novel multitask 3D deep learning method th...

---

### 41. Forest canopy height estimation from satellite RGB imagery using large-scale airborne LiDAR-derived training data and monocular depth estimation

**Authors:** Yongkang Lai, Xihan Mu, Tim R. McVicar, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06503v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06503v1)

**Summary:** Large-scale, high-resolution forest canopy height mapping plays a crucial role in understanding regional and global carbon and water cycles. Spaceborne LiDAR missions, including the Ice, Cloud, and Land Elevation Satellite-2 (ICESat-2) and the Global Ecosystem Dynamics Investigation (GEDI), provide global observations of forest structure but are spatially sparse and subject to inherent uncertainties. In contrast, near-surface LiDAR platforms, such as airborne and unmanned aerial vehicle (UAV) Li...

---

### 42. DreamHome-Pano: Design-Aware and Conflict-Free Panoramic Interior Generation

**Authors:** Lulu Chen, Yijiang Hu, Yuanqing Liu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06494v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06494v1)

**Summary:** In modern interior design, the generation of personalized spaces frequently necessitates a delicate balance between rigid architectural structural constraints and specific stylistic preferences. However, existing multi-condition generative frameworks often struggle to harmonize these inputs, leading to "condition conflicts" where stylistic attributes inadvertently compromise the geometric precision of the layout. To address this challenge, we present DreamHome-Pano, a controllable panoramic gene...

---

### 43. Rebenchmarking Unsupervised Monocular 3D Occupancy Prediction

**Authors:** Zizhan Guo, Yi Feng, Mengtan Zhang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06488v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06488v1)

**Summary:** Inferring the 3D structure from a single image, particularly in occluded regions, remains a fundamental yet unsolved challenge in vision-centric autonomous driving. Existing unsupervised approaches typically train a neural radiance field and treat the network outputs as occupancy probabilities during evaluation, overlooking the inconsistency between training and evaluation protocols. Moreover, the prevalent use of 2D ground truth fails to reveal the inherent ambiguity in occluded regions caused ...

---

### 44. Instance-Free Domain Adaptive Object Detection

**Authors:** Hengfu Yu, Jinhong Deng, Lixin Duan, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06484v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06484v1)

**Summary:** While Domain Adaptive Object Detection (DAOD) has made significant strides, most methods rely on unlabeled target data that is assumed to contain sufficient foreground instances. However, in many practical scenarios (e.g., wildlife monitoring, lesion detection), collecting target domain data with objects of interest is prohibitively costly, whereas background-only data is abundant. This common practical constraint introduces a significant technical challenge: the difficulty of achieving domain a...

---

### 45. Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention

**Authors:** Xiaosong Jia, Yihang Sun, Junqi You, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06478v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06478v1)

**Summary:** Feedforward models for novel view synthesis (NVS) have recently advanced by transformer-based methods like LVSM, using attention among all input and target views. In this work, we argue that its full self-attention design is suboptimal, suffering from quadratic complexity with respect to the number of input views and rigid parameter sharing among heterogeneous tokens. We propose Efficient-LVSM, a dual-stream architecture that avoids these issues with a decoupled co-refinement mechanism. It appli...

---

### 46. LAB-Det: Language as a Domain-Invariant Bridge for Training-Free One-Shot Domain Generalization in Object Detection

**Authors:** Xu Zhang, Zhe Chen, Jing Zhang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06474v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06474v1)

**Summary:** Foundation object detectors such as GLIP and Grounding DINO excel on general-domain data but often degrade in specialized and data-scarce settings like underwater imagery or industrial defects. Typical cross-domain few-shot approaches rely on fine-tuning scarce target data, incurring cost and overfitting risks. We instead ask: Can a frozen detector adapt with only one exemplar per class without training? To answer this, we introduce training-free one-shot domain generalization for object detecti...

---

### 47. Exploring Specular Reflection Inconsistency for Generalizable Face Forgery Detection

**Authors:** Hongyan Fei, Zexi Jia, Chuanwei Huang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06452v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06452v1)

**Summary:** Detecting deepfakes has become increasingly challenging as forgery faces synthesized by AI-generated methods, particularly diffusion models, achieve unprecedented quality and resolution. Existing forgery detection approaches relying on spatial and frequency features demonstrate limited efficacy against high-quality, entirely synthesized forgeries. In this paper, we propose a novel detection method grounded in the observation that facial attributes governed by complex physical laws and multiple p...

---

### 48. What Is Wrong with Synthetic Data for Scene Text Recognition? A Strong Synthetic Engine with Diverse Simulations and Self-Evolution

**Authors:** Xingsong Ye, Yongkun Du, JiaXin Zhang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06450v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06450v1)

**Summary:** Large-scale and categorical-balanced text data is essential for training effective Scene Text Recognition (STR) models, which is hard to achieve when collecting real data. Synthetic data offers a cost-effective and perfectly labeled alternative. However, its performance often lags behind, revealing a significant domain gap between real and current synthetic data. In this work, we systematically analyze mainstream rendering-based synthetic datasets and identify their key limitations: insufficient...

---

### 49. ChatUMM: Robust Context Tracking for Conversational Interleaved Generation

**Authors:** Wenxun Dai, Zhiyuan Zhao, Yule Zhong, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06442v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06442v1)

**Summary:** Unified multimodal models (UMMs) have achieved remarkable progress yet remain constrained by a single-turn interaction paradigm, effectively functioning as solvers for independent requests rather than assistants in continuous dialogue. To bridge this gap, we present ChatUMM. As a conversational unified model, it excels at robust context tracking to sustain interleaved multimodal generation. ChatUMM derives its capabilities from two key innovations: an interleaved multi-turn training strategy tha...

---

### 50. Bridging the Indoor-Outdoor Gap: Vision-Centric Instruction-Guided Embodied Navigation for the Last Meters

**Authors:** Yuxiang Zhao, Yirong Yang, Yanqing Zhu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06427v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06427v1)

**Summary:** Embodied navigation holds significant promise for real-world applications such as last-mile delivery. However, most existing approaches are confined to either indoor or outdoor environments and rely heavily on strong assumptions, such as access to precise coordinate systems. While current outdoor methods can guide agents to the vicinity of a target using coarse-grained localization, they fail to enable fine-grained entry through specific building entrances, critically limiting their utility in p...

---

## cs.LG

**50 papers**

### 1. Learning a Generative Meta-Model of LLM Activations

**Authors:** Grace Luo, Jiahai Feng, Trevor Darrell, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06964v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06964v1)

**Summary:** Existing approaches for analyzing neural network activations, such as PCA and sparse autoencoders, rely on strong structural assumptions. Generative models offer an alternative: they can uncover structure without such assumptions and act as priors that improve intervention fidelity. We explore this direction by training diffusion models on one billion residual stream activations, creating "meta-models" that learn the distribution of a network's internal states. We find that diffusion loss decrea...

---

### 2. Improving Credit Card Fraud Detection with an Optimized Explainable Boosting Machine

**Authors:** Reza E. Fazel, Arash Bakhtiary, Siavash A. Bigdeli

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06955v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06955v1)

**Summary:** Addressing class imbalance is a central challenge in credit card fraud detection, as it directly impacts predictive reliability in real-world financial systems. To overcome this, the study proposes an enhanced workflow based on the Explainable Boosting Machine (EBM)-a transparent, state-of-the-art implementation of the GA2M algorithm-optimized through systematic hyperparameter tuning, feature selection, and preprocessing refinement. Rather than relying on conventional sampling techniques that ma...

---

### 3. DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

**Authors:** Shenyuan Gao, William Liang, Kaiyuan Zheng, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06949v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06949v1)

**Summary:** Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture r...

---

### 4. Agentic Uncertainty Reveals Agentic Overconfidence

**Authors:** Jean Kaddour, Srijan Patel, Gbètondji Dovonon, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06948v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06948v1)

**Summary:** Can AI agents predict whether they will succeed at a task? We study agentic uncertainty by eliciting success probability estimates before, during, and after task execution. All results exhibit agentic overconfidence: some agents that succeed only 22% of the time predict 77% success. Counterintuitively, pre-execution assessment with strictly less information tends to yield better discrimination than standard post-execution review, though differences are not always significant. Adversarial prompti...

---

### 5. Optimal Derivative Feedback Control for an Active Magnetic Levitation System: An Experimental Study on Data-Driven Approaches

**Authors:** Saber Omidi, Rene Akupan Ebunle, Se Young Yoon

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06944v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06944v1)

**Summary:** This paper presents the design and implementation of data-driven optimal derivative feedback controllers for an active magnetic levitation system. A direct, model-free control design method based on the reinforcement learning framework is compared with an indirect optimal control design derived from a numerically identified mathematical model of the system. For the direct model-free approach, a policy iteration procedure is proposed, which adds an iteration layer called the epoch loop to gather ...

---

### 6. Endogenous Resistance to Activation Steering in Language Models

**Authors:** Alex McKenzie, Keenan Pepper, Stijn Servaes, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06941v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06941v1)

**Summary:** Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 SAE latents that activate diff...

---

### 7. From Core to Detail: Unsupervised Disentanglement with Entropy-Ordered Flows

**Authors:** Daniel Galperin, Ullrich Köthe

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06940v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06940v1)

**Summary:** Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy-ordered flows (EOFlows), a normalizing-flow framework that orders latent dimensions by their explained entropy, analogously to PCA's explained variance. This ordering enables adaptive injective flows: after training, one may retain only the top C latent variables to form a compact core representation while the remai...

---

### 8. Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics

**Authors:** Zuyuan Zhang, Sizhe Tang, Tian Lan

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06939v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06939v1)

**Summary:** Non-Markovian dynamics are commonly found in real-world environments due to long-range dependencies, partial observability, and memory effects. The Bellman equation that is the central pillar of Reinforcement learning (RL) becomes only approximately valid under Non-Markovian. Existing work often focus on practical algorithm designs and offer limited theoretical treatment to address key questions, such as what dynamics are indeed capturable by the Bellman framework and how to inspire new algorith...

---

### 9. Reliable Mislabel Detection for Video Capsule Endoscopy Data

**Authors:** Julia Werner, Julius Oexle, Oliver Bause, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06938v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06938v1)

**Summary:** The classification performance of deep neural networks relies strongly on access to large, accurately annotated datasets. In medical imaging, however, obtaining such datasets is particularly challenging since annotations must be provided by specialized physicians, which severely limits the pool of annotators. Furthermore, class boundaries can often be ambiguous or difficult to define which further complicates machine learning-based classification. In this paper, we want to address this problem a...

---

### 10. Reciprocal Latent Fields for Precomputed Sound Propagation

**Authors:** Hugo Seuté, Pranai Vasudev, Etienne Richan, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06937v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06937v1)

**Summary:** Realistic sound propagation is essential for immersion in a virtual scene, yet physically accurate wave-based simulations remain computationally prohibitive for real-time applications. Wave coding methods address this limitation by precomputing and compressing impulse responses of a given scene into a set of scalar acoustic parameters, which can reach unmanageable sizes in large environments with many source-receiver pairs. We introduce Reciprocal Latent Fields (RLF), a memory-efficient framewor...

---

### 11. When RL Meets Adaptive Speculative Training: A Unified Training-Serving System

**Authors:** Junxiong Wang, Fengxiang Bie, Jisen Li, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06932v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06932v1)

**Summary:** Speculative decoding can significantly accelerate LLM serving, yet most deployments today disentangle speculator training from serving, treating speculator training as a standalone offline modeling problem. We show that this decoupled formulation introduces substantial deployment and adaptation lag: (1) high time-to-serve, since a speculator must be trained offline for a considerable period before deployment; (2) delayed utility feedback, since the true end-to-end decoding speedup is only known ...

---

### 12. Continuous-time reinforcement learning: ellipticity enables model-free value function approximation

**Authors:** Wenlong Mou

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06930v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06930v1)

**Summary:** We study off-policy reinforcement learning for controlling continuous-time Markov diffusion processes with discrete-time observations and actions. We consider model-free algorithms with function approximation that learn value and advantage functions directly from data, without unrealistic structural assumptions on the dynamics.   Leveraging the ellipticity of the diffusions, we establish a new class of Hilbert-space positive definiteness and boundedness properties for the Bellman operators. Base...

---

### 13. Robustness Beyond Known Groups with Low-rank Adaptation

**Authors:** Abinitha Gourabathina, Hyewon Jeong, Teya Bergamaschi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06924v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06924v1)

**Summary:** Deep learning models trained to optimize average accuracy often exhibit systematic failures on particular subpopulations. In real world settings, the subpopulations most affected by such disparities are frequently unlabeled or unknown, thereby motivating the development of methods that are performant on sensitive subgroups without being pre-specified. However, existing group-robust methods typically assume prior knowledge of relevant subgroups, using group annotations for training or model selec...

---

### 14. From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers

**Authors:** Ziming Liu, Sophia Sanborn, Surya Ganguli, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06923v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06923v1)

**Summary:** Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, they typically rely on strong, domain-specific priors that effectively "bake in" the physics. Conversely, Vafa et al. recently showed that...

---

### 15. Automatic Detection and Analysis of Singing Mistakes for Music Pedagogy

**Authors:** Sumit Kumar, Suraj Jaiswal, Parampreet Singh, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06917v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06917v1)

**Summary:** The advancement of machine learning in audio analysis has opened new possibilities for technology-enhanced music education. This paper introduces a framework for automatic singing mistake detection in the context of music pedagogy, supported by a newly curated dataset. The dataset comprises synchronized teacher learner vocal recordings, with annotations marking different types of mistakes made by learners. Using this dataset, we develop different deep learning models for mistake detection and be...

---

### 16. Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models

**Authors:** Yunshi Wen, Wesley M. Gifford, Chandra Reddy, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06909v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06909v1)

**Summary:** The recent surge in Time Series Foundation Models has rapidly advanced the field, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural innovations versus data engineering. In this work, we investigate the potential of a standard patch Transformer, demonstrating that this generic architecture achieves state-of-the-art zero-shot forecasting performance using a straightforward training protocol. We conduct a comprehensive ablation study t...

---

### 17. A first realization of reinforcement learning-based closed-loop EEG-TMS

**Authors:** Dania Humaidan, Jiahua Xu, Jing Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06907v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06907v1)

**Summary:** Background: Transcranial magnetic stimulation (TMS) is a powerful tool to investigate neurophysiology of the human brain and treat brain disorders. Traditionally, therapeutic TMS has been applied in a one-size-fits-all approach, disregarding inter- and intra-individual differences. Brain state-dependent EEG-TMS, such as coupling TMS with a pre-specified phase of the sensorimotor mu-rhythm, enables the induction of differential neuroplastic effects depending on the targeted phase. But this approa...

---

### 18. Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory

**Authors:** Emmanuel Esposito, Andrew Jacobsen, Hao Qiu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06902v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06902v1)

**Summary:** In this paper, we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficients $λ_t$ to vary arbitrarily over time. Our main contribution is a novel algorithm that establishes the first comparator-adaptive dynamic regret bound for this setting, guaranteeing $\widetilde{\mathcal{O}}(\sqrt{(1+P_T)(T+\sum_t λ_t)})$ regret, where $P_T$ is the path length of the comparator sequen...

---

### 19. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design

**Authors:** Samuel Klein, Willie Neiswanger, Daniel Ratner, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06900v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06900v1)

**Summary:** Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural ...

---

### 20. Sample Complexity of Causal Identification with Temporal Heterogeneity

**Authors:** Ameya Rathod, Sujay Belsare, Salvik Krishna Nautiyal, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06899v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06899v1)

**Summary:** Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable only by exploiting specific structural or distributional assumptions. While recent work has separately utilized time-series dynamics or multi-environment heterogeneity to constrain this problem, we integrate both as complementary sources of heterogeneity. This integration yields unified necessary ide...

---

### 21. A Cycle-Consistent Graph Surrogate for Full-Cycle Left Ventricular Myocardial Biomechanics

**Authors:** Siyu Mu, Wei Xuan Chan, Choon Hwai Yap

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06884v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06884v1)

**Summary:** Image-based patient-specific simulation of left ventricular (LV) mechanics is valuable for understanding cardiac function and supporting clinical intervention planning, but conventional finite-element analysis (FEA) is computationally intensive. Current graph-based surrogates do not have full-cycle prediction capabilities, and physics-informed neural networks often struggle to converge on complex cardiac geometries. We present CardioGraphFENet (CGFENet), a unified graph-based surrogate for rapid...

---

### 22. Vision Transformer Finetuning Benefits from Non-Smooth Components

**Authors:** Ambroise Odonnat, Laetitia Chapel, Romain Tavenard, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06883v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06883v1)

**Summary:** The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, or, in other words, their plasticity. Defined as an average rate of change, it captures the sensitivity to input perturbation; in particular, a high plasticity ...

---

### 23. Decoupling Variance and Scale-Invariant Updates in Adaptive Gradient Descent for Unified Vector and Matrix Optimization

**Authors:** Zitao Song, Cedar Site Bai, Zhe Zhang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06880v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06880v1)

**Summary:** Adaptive methods like Adam have become the $\textit{de facto}$ standard for large-scale vector and Euclidean optimization due to their coordinate-wise adaptation with a second-order nature. More recently, matrix-based spectral optimizers like Muon (Jordan et al., 2024b) show the power of treating weight matrices as matrices rather than long vectors. Linking these is hard because many natural generalizations are not feasible to implement, and we also cannot simply move the Adam adaptation to the ...

---

### 24. Uncovering Cross-Objective Interference in Multi-Objective Alignment

**Authors:** Yining Lu, Meng Jiang

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06869v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06869v1)

**Summary:** We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross-objective interference and conduct the first systematic study across classic scalarization algorithms, showing that interference is pervasive and exhibits strong model dependence.   To explain this phenomenon, we derive a local covariance law showing that an objective i...

---

### 25. T-STAR: A Context-Aware Transformer Framework for Short-Term Probabilistic Demand Forecasting in Dock-Based Shared Micro-Mobility

**Authors:** Jingyi Cheng, Gonçalo Homem de Almeida Correia, Oded Cats, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06866v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06866v1)

**Summary:** Reliable short-term demand forecasting is essential for managing shared micro-mobility services and ensuring responsive, user-centered operations. This study introduces T-STAR (Two-stage Spatial and Temporal Adaptive contextual Representation), a novel transformer-based probabilistic framework designed to forecast station-level bike-sharing demand at a 15-minute resolution. T-STAR addresses key challenges in high-resolution forecasting by disentangling consistent demand patterns from short-term ...

---

### 26. Zero-shot Generalizable Graph Anomaly Detection with Mixture of Riemannian Experts

**Authors:** Xinyu Zhao, Qingyun Sun, Jiayi Luo, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06859v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06859v1)

**Summary:** Graph Anomaly Detection (GAD) aims to identify irregular patterns in graph data, and recent works have explored zero-shot generalist GAD to enable generalization to unseen graph datasets. However, existing zero-shot GAD methods largely ignore intrinsic geometric differences across diverse anomaly patterns, substantially limiting their cross-domain generalization. In this work, we reveal that anomaly detectability is highly dependent on the underlying geometric properties and that embedding graph...

---

### 27. Designing a Robust, Bounded, and Smooth Loss Function for Improved Supervised Learning

**Authors:** Soumi Mahato, Lineesh M. C

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06858v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06858v1)

**Summary:** The loss function is crucial to machine learning, especially in supervised learning frameworks. It is a fundamental component that controls the behavior and general efficacy of learning algorithms. However, despite their widespread use, traditional loss functions have significant drawbacks when dealing with high-dimensional and outlier-sensitive datasets, which frequently results in reduced performance and slower convergence during training. In this work, we develop a robust, bounded, and smooth...

---

### 28. Improved Sampling Schedules for Discrete Diffusion Models

**Authors:** Alberto Foresti, Mustapha Bounoua, Giulio Franzese, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06849v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06849v1)

**Summary:** Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, we bridge this gap by analyzing the reverse process dynamics through the lens of thermodynamic entropy production. We propose the entropy production rate as a rigorous proxy for quantifying information generation, derivi...

---

### 29. Are Deep Learning Based Hybrid PDE Solvers Reliable? Why Training Paradigms and Update Strategies Matter

**Authors:** Yuhan Wu, Jan Willem van Beek, Victorita Dolean, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06842v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06842v1)

**Summary:** Deep learning-based hybrid iterative methods (DL-HIMs) integrate classical numerical solvers with neural operators, utilizing their complementary spectral biases to accelerate convergence. Despite this promise, many DL-HIMs stagnate at false fixed points where neural updates vanish while the physical residual remains large, raising questions about reliability in scientific computing. In this paper, we provide evidence that performance is highly sensitive to training paradigms and update strategi...

---

### 30. Learning Deep Hybrid Models with Sharpness-Aware Minimization

**Authors:** Naoya Takeishi

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06837v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06837v1)

**Summary:** Hybrid modeling, the combination of machine learning models and scientific mathematical models, enables flexible and robust data-driven prediction with partial interpretability. However, effectively the scientific models may be ignored in prediction due to the flexibility of the machine learning model, making the idea of hybrid modeling pointless. Typically some regularization is applied to hybrid model learning to avoid such a failure case, but the formulation of the regularizer strongly depend...

---

### 31. AEGPO: Adaptive Entropy-Guided Policy Optimization for Diffusion Models

**Authors:** Yuming Li, Qingyu Li, Chengyu Bai, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06825v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06825v1)

**Summary:** Reinforcement learning from human feedback (RLHF) shows promise for aligning diffusion and flow models, yet policy optimization methods such as GRPO suffer from inefficient and static sampling strategies. These methods treat all prompts and denoising steps uniformly, ignoring substantial variations in sample learning value as well as the dynamic nature of critical exploration moments.   To address this issue, we conduct a detailed analysis of the internal attention dynamics during GRPO training ...

---

### 32. RanSOM: Second-Order Momentum with Randomized Scaling for Constrained and Unconstrained Optimization

**Authors:** El Mahdi Chayti

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06824v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06824v1)

**Summary:** Momentum methods, such as Polyak's Heavy Ball, are the standard for training deep networks but suffer from curvature-induced bias in stochastic settings, limiting convergence to suboptimal $\mathcal{O}(ε^{-4})$ rates. Existing corrections typically require expensive auxiliary sampling or restrictive smoothness assumptions. We propose \textbf{RanSOM}, a unified framework that eliminates this bias by replacing deterministic step sizes with randomized steps drawn from distributions with mean $η_t$....

---

### 33. Calibrating Tabular Anomaly Detection via Optimal Transport

**Authors:** Hangting Ye, He Zhao. Wei Fan, Xiaozhuang Song, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06810v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06810v1)

**Summary:** Tabular anomaly detection (TAD) remains challenging due to the heterogeneity of tabular data: features lack natural relationships, vary widely in distribution and scale, and exhibit diverse types. Consequently, each TAD method makes implicit assumptions about anomaly patterns that work well on some datasets but fail on others, and no method consistently outperforms across diverse scenarios. We present CTAD (Calibrating Tabular Anomaly Detection), a model-agnostic post-processing framework that e...

---

### 34. SuReNav: Superpixel Graph-based Constraint Relaxation for Navigation in Over-constrained Environments

**Authors:** Keonyoung Koh, Moonkyeong Jung, Samuel Seungsup Lee, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06807v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06807v1)

**Summary:** We address the over-constrained planning problem in semi-static environments. The planning objective is to find a best-effort solution that avoids all hard constraint regions while minimally traversing the least risky areas. Conventional methods often rely on pre-defined area costs, limiting generalizations. Further, the spatial continuity of navigation spaces makes it difficult to identify regions that are passable without overestimation. To overcome these challenges, we propose SuReNav, a supe...

---

### 35. RAIGen: Rare Attribute Identification in Text-to-Image Generative Models

**Authors:** Silpa Vadakkeeveetil Sreelatha, Dan Wang, Serge Belongie, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06806v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06806v1)

**Summary:** Text-to-image diffusion models achieve impressive generation quality but inherit and amplify training-data biases, skewing coverage of semantic attributes. Prior work addresses this in two ways. Closed-set approaches mitigate biases in predefined fairness categories (e.g., gender, race), assuming socially salient minority attributes are known a priori. Open-set approaches frame the task as bias identification, highlighting majority attributes that dominate outputs. Both overlook a complementary ...

---

### 36. On the Identifiability of Steering Vectors in Large Language Models

**Authors:** Sohan Venkatesh, Ashish Mahendran Kurapath

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06801v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06801v1)

**Summary:** Activation steering methods, such as persona vectors, are widely used to control large language model behavior and increasingly interpreted as revealing meaningful internal representations. This interpretation implicitly assumes steering directions are identifiable and uniquely recoverable from input-output behavior. We formalize steering as an intervention on internal representations and prove that, under realistic modeling and data conditions, steering vectors are fundamentally non-identifiabl...

---

### 37. FlowDA: Accurate, Low-Latency Weather Data Assimilation via Flow Matching

**Authors:** Ran Cheng, Lailai Zhu

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06800v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06800v1)

**Summary:** Data assimilation (DA) is a fundamental component of modern weather prediction, yet it remains a major computational bottleneck in machine learning (ML)-based forecasting pipelines due to reliance on traditional variational methods. Recent generative ML-based DA methods offer a promising alternative but typically require many sampling steps and suffer from error accumulation under long-horizon auto-regressive rollouts with cycling assimilation. We propose FlowDA, a low-latency weather-scale gene...

---

### 38. Optimal Learning-Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay

**Authors:** Binghui Li, Zilin Wang, Fengling Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06797v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06797v1)

**Summary:** We study optimal learning-rate schedules (LRSs) under the functional scaling law (FSL) framework introduced in Li et al. (2025), which accurately models the loss dynamics of both linear regression and large language model (LLM) pre-training. Within FSL, loss dynamics are governed by two exponents: a source exponent $s>0$ controlling the rate of signal learning, and a capacity exponent $β>1$ determining the rate of noise forgetting. Focusing on a fixed training horizon $N$, we derive the optimal ...

---

### 39. Rare Event Analysis of Large Language Models

**Authors:** Jake McAllister Dorman, Edward Gillman, Dominic C. Rose, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06791v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06791v1)

**Summary:** Being probabilistic models, during inference large language models (LLMs) display rare events: behaviour that is far from typical but highly significant. By definition all rare events are hard to see, but the enormous scale of LLM usage means that events completely unobserved during development are likely to become prominent in deployment. Here we present an end-to-end framework for the systematic analysis of rare events in LLMs. We provide a practical implementation spanning theory, efficient g...

---

### 40. Displacement-Resistant Extensions of DPO with Nonconvex $f$-Divergences

**Authors:** Idan Pipano, Shoham Sabach, Kavosh Asadi, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06788v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06788v1)

**Summary:** DPO and related algorithms align language models by directly optimizing the RLHF objective: find a policy that maximizes the Bradley-Terry reward while staying close to a reference policy through a KL divergence penalty. Previous work showed that this approach could be further generalized: the original problem remains tractable even if the KL divergence is replaced by a family of $f$-divergence with a convex generating function $f$. Our first contribution is to show that convexity of $f$ is not ...

---

### 41. Weisfeiler and Lehman Go Categorical

**Authors:** Seongjin Choi, Gahee Kim, Se-Young Yun

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06787v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06787v1)

**Summary:** While lifting map has significantly enhanced the expressivity of graph neural networks, extending this paradigm to hypergraphs remains fragmented. To address this, we introduce the categorical Weisfeiler-Lehman framework, which formalizes lifting as a functorial mapping from an arbitrary data category to the unifying category of graded posets. When applied to hypergraphs, this perspective allows us to systematically derive Hypergraph Isomorphism Networks, a family of neural architectures where t...

---

### 42. Revisiting Emotions Representation for Recognition in the Wild

**Authors:** Joao Baptista Cardia Neto, Claudio Ferrari, Stefano Berretti

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06778v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06778v1)

**Summary:** Facial emotion recognition has been typically cast as a single-label classification problem of one out of six prototypical emotions. However, that is an oversimplification that is unsuitable for representing the multifaceted spectrum of spontaneous emotional states, which are most often the result of a combination of multiple emotions contributing at different intensities. Building on this, a promising direction that was explored recently is to cast emotion recognition as a distribution learning...

---

### 43. Fair Transit Stop Placement: A Clustering Perspective and Beyond

**Authors:** Haris Aziz, Ling Gai, Yuhang Guo, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06776v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06776v1)

**Summary:** We study the transit stop placement (TrSP) problem in general metric spaces, where agents travel between source-destination pairs and may either walk directly or utilize a shuttle service via selected transit stops. We investigate fairness in TrSP through the lens of justified representation (JR) and the core, and uncover a structural correspondence with fair clustering. Specifically, we show that a constant-factor approximation to proportional fairness in clustering can be used to guarantee a c...

---

### 44. Robust Online Learning

**Authors:** Sajad Ashkezari

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06775v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06775v1)

**Summary:** We study the problem of learning robust classifiers where the classifier will receive a perturbed input. Unlike robust PAC learning studied in prior work, here the clean data and its label are also adversarially chosen. We formulate this setting as an online learning problem and consider both the realizable and agnostic learnability of hypothesis classes. We define a new dimension of classes and show it controls the mistake bounds in the realizable setting and the regret bounds in the agnostic s...

---

### 45. On the Convergence of Multicalibration Gradient Boosting

**Authors:** Daniel Haimovich, Fridolin Linder, Lorenzo Perini, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06773v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06773v1)

**Summary:** Multicalibration gradient boosting has recently emerged as a scalable method that empirically produces approximately multicalibrated predictors and has been deployed at web scale. Despite this empirical success, its convergence properties are not well understood. In this paper, we bridge the gap by providing convergence guarantees for multicalibration gradient boosting in regression with squared-error loss. We show that the magnitude of successive prediction updates decays at $O(1/\sqrt{T})$, wh...

---

### 46. Calibrating Generative AI to Produce Realistic Essays for Data Augmentation

**Authors:** Edward W. Wolfe, Justin O. Barber

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06772v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06772v1)

**Summary:** Data augmentation can mitigate limited training data in machine-learning automated scoring engines for constructed response items. This study seeks to determine how well three approaches to large language model prompting produce essays that preserve the writing quality of the original essays and produce realistic text for augmenting ASE training datasets. We created simulated versions of student essays, and human raters assigned scores to them and rated the realism of the generated text. The res...

---

### 47. AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models

**Authors:** Fengpeng Li, Kemou Li, Qizhou Wang, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06771v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06771v1)

**Summary:** Concept erasure helps stop diffusion models (DMs) from generating harmful content; but current methods face robustness retention trade off. Robustness means the model fine-tuned by concept erasure methods resists reactivation of erased concepts, even under semantically related prompts. Retention means unrelated concepts are preserved so the model's overall utility stays intact. Both are critical for concept erasure in practice, yet addressing them simultaneously is challenging, as existing works...

---

### 48. Soft Forward-Backward Representations for Zero-shot Reinforcement Learning with General Utilities

**Authors:** Marco Bagatella, Thomas Rupf, Georg Martius, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06769v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06769v1)

**Summary:** Recent advancements in zero-shot reinforcement learning (RL) have facilitated the extraction of diverse behaviors from unlabeled, offline data sources. In particular, forward-backward algorithms (FB) can retrieve a family of policies that can approximately solve any standard RL problem (with additive rewards, linear in the occupancy measure), given sufficient capacity. While retaining zero-shot properties, we tackle the greater problem class of RL with general utilities, in which the objective i...

---

### 49. A Unified Framework for LLM Watermarks

**Authors:** Thibaud Gloaguen, Robin Staab, Nikola Jovanović, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06754v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06754v1)

**Summary:** LLM watermarks allow tracing AI-generated texts by inserting a detectable signal into their generated content. Recent works have proposed a wide range of watermarking algorithms, each with distinct designs, usually built using a bottom-up approach. Crucially, there is no general and principled formulation for LLM watermarking.   In this work, we show that most existing and widely used watermarking schemes can in fact be derived from a principled constrained optimization problem. Our formulation ...

---

### 50. Semantically Labelled Automata for Multi-Task Reinforcement Learning with LTL Instructions

**Authors:** Alessandro Abate, Giuseppe De Giacomo, Mathias Jackermeier, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06746v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06746v1)

**Summary:** We study multi-task reinforcement learning (RL), a setting in which an agent learns a single, universal policy capable of generalising to arbitrary, possibly unseen tasks. We consider tasks specified as linear temporal logic (LTL) formulae, which are commonly used in formal methods to specify properties of systems, and have recently been successfully adopted in RL. In this setting, we present a novel task embedding technique leveraging a new generation of semantic LTL-to-automata translations, o...

---

## cs.NE

**50 papers**

### 1. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design

**Authors:** Samuel Klein, Willie Neiswanger, Daniel Ratner, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06900v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06900v1)

**Summary:** Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural ...

---

### 2. Sparse Spike Encoding of Channel Responses for Energy Efficient Human Activity Recognition

**Authors:** Eleonora Cicciarella, Riccardo Mazzieri, Jacopo Pegoraro, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06766v1)

**Summary:** ISAC enables pervasive monitoring, but modern sensing algorithms are often too complex for energy-constrained edge devices. This motivates the development of learning techniques that balance accuracy performance and energy efficiency. Spiking Neural Networks (SNNs) are a promising alternative, processing information as sparse binary spike trains and potentially reducing energy consumption by orders of magnitude. In this work, we propose a spiking convolutional autoencoder (SCAE) that learns tail...

---

### 3. Structural bias in multi-objective optimisation

**Authors:** Jakub Kudela, Niki van Stein, Thomas Bäck, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06742v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06742v1)

**Summary:** Structural bias (SB) refers to systematic preferences of an optimisation algorithm for particular regions of the search space that arise independently of the objective function. While SB has been studied extensively in single-objective optimisation, its role in multi-objective optimisation remains largely unexplored. This is problematic, as dominance relations, diversity preservation and Pareto-based selection mechanisms may introduce or amplify structural effects.   In this paper, we extend the...

---

### 4. Green Optimization: Energy-aware Design of Metaheuristics by Using Machine Learning Surrogates to Cope with Real Problems

**Authors:** Tomohiro Harada, Enrique Alba, Gabriel Luque

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06610v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06610v1)

**Summary:** Addressing real-world optimization challenges requires not only advanced metaheuristics but also continuous refinement of their internal mechanisms. This paper explores the integration of machine learning in the form of neural surrogate models into metaheuristics through a recent lens: energy consumption. While surrogates are widely used to reduce the computational cost of expensive objective functions, their combined impact on energy efficiency, algorithmic performance, and solution accuracy re...

---

### 5. Energy-Aware Metaheuristics

**Authors:** Tomohiro Harada, Enrique Alba, Gabriel Luque

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06595v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06595v1)

**Summary:** This paper presents a principled framework for designing energy-aware metaheuristics that operate under fixed energy budgets. We introduce a unified operator-level model that quantifies both numerical gain and energy usage, and define a robust Expected Improvement per Joule (EI/J) score that guides adaptive selection among operator variants during the search. The resulting energy-aware solvers dynamically choose between operators to self-control exploration and exploitation, aiming to maximize f...

---

### 6. A neuromorphic model of the insect visual system for natural image processing

**Authors:** Adam D. Hines, Karin Nordström, Andrew B. Barron

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06405v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06405v1)

**Summary:** Insect vision supports complex behaviors including associative learning, navigation, and object detection, and has long motivated computational models for understanding biological visual processing. However, many contemporary models prioritize task performance while neglecting biologically grounded processing pathways. Here, we introduce a bio-inspired vision model that captures principles of the insect visual system to transform dense visual input into sparse, discriminative codes. The model is...

---

### 7. DARWIN: Dynamic Agentically Rewriting Self-Improving Network

**Authors:** Henry Jiang

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05848v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05848v1)

**Summary:** DARWIN is an evolutionary GPT model, utilizing a genetic-algorithm like optimization structure with several independent GPT agents being trained individually using unique training code. Each iteration, the GPT models are prompted to modify the training code of one another in an attempt to improve their performance in a mutation-like manner, and the best GPT agents are then benchmarked and selected for the next iteration by genetic algorithm. For demonstration purposes and due to budget and time ...

---

### 8. Neuro-Inspired Visual Pattern Recognition via Biological Reservoir Computing

**Authors:** Luca Ciampi, Ludovico Iannello, Fabrizio Tonelli, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05737v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05737v1)

**Summary:** In this paper, we present a neuro-inspired approach to reservoir computing (RC) in which a network of in vitro cultured cortical neurons serves as the physical reservoir. Rather than relying on artificial recurrent models to approximate neural dynamics, our biological reservoir computing (BRC) system leverages the spontaneous and stimulus-evoked activity of living neural circuits as its computational substrate. A high-density multi-electrode array (HD-MEA) provides simultaneous stimulation and r...

---

### 9. Variable Search Stepsize for Randomized Local Search in Multi-Objective Combinatorial Optimization

**Authors:** Xuepeng Ren, Maocai Wang, Guangming Dai, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05675v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05675v1)

**Summary:** Over the past two decades, research in evolutionary multi-objective optimization has predominantly focused on continuous domains, with comparatively limited attention given to multi-objective combinatorial optimization problems (MOCOPs). Combinatorial problems differ significantly from continuous ones in terms of problem structure and landscape. Recent studies have shown that on MOCOPs multi-objective evolutionary algorithms (MOEAs) can even be outperformed by simple randomised local search. Sta...

---

### 10. Optimization is Not Enough: Why Problem Formulation Deserves Equal Attention

**Authors:** Iván Olarte Rodríguez, Gokhan Serhat, Mariusz Bujny, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05466v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05466v1)

**Summary:** Black-box optimization is increasingly used in engineering design problems where simulation-based evaluations are costly and gradients are unavailable. In this context, the optimization community has largely analyzed algorithm performance in context-free setups, while not enough attention has been devoted to how problem formulation and domain knowledge may affect the optimization outcomes. We address this gap through a case study in the topology optimization of laminated composite structures, fo...

---

### 11. It's not a Lottery, it's a Race: Understanding How Gradient Descent Adapts the Network's Capacity to the Task

**Authors:** Hannah Pinson

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04832v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04832v1)

**Summary:** Our theoretical understanding of neural networks is lagging behind their empirical success. One of the important unexplained phenomena is why and how, during the process of training with gradient descent, the theoretical capacity of neural networks is reduced to an effective capacity that fits the task. We here investigate the mechanism by which gradient descent achieves this through analyzing the learning dynamics at the level of individual neurons in single hidden layer ReLU networks. We ident...

---

### 12. Impact of diversity on bounded archives for multi-objective local search

**Authors:** Amadeu A. Coco, Cyprien Borée, Julien Baste, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04745v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04745v1)

**Summary:** This work tackles two critical challenges related to the development of metaheuristics for Multi-Objective Optimization Problems (MOOPs): the exponential growth of non-dominated solutions and the tendency of metaheuristics to disproportionately concentrate their search on a subset of the Pareto Front. To counteract the first, bounded archives are employed as a strategic mechanism for effectively managing the increasing number of non-dominated solutions. Addressing the second challenge involves a...

---

### 13. Evolutionary Mapping of Neural Networks to Spatial Accelerators

**Authors:** Alessandro Pierro, Jonathan Timcheck, Jason Yik, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04717v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04717v1)

**Summary:** Spatial accelerators, composed of arrays of compute-memory integrated units, offer an attractive platform for deploying inference workloads with low latency and low energy consumption. However, fully exploiting their architectural advantages typically requires careful, expert-driven mapping of computational graphs to distributed processing elements. In this work, we automate this process by framing the mapping challenge as a black-box optimization problem. We introduce the first evolutionary, ha...

---

### 14. Real-time processing of analog signals on accelerated neuromorphic hardware

**Authors:** Yannik Stradmann, Johannes Schemmel, Mihai A. Petrovici, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04582v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04582v1)

**Summary:** Sensory processing with neuromorphic systems is typically done by using either event-based sensors or translating input signals to spikes before presenting them to the neuromorphic processor. Here, we offer an alternative approach: direct analog signal injection eliminates superfluous and power-intensive analog-to-digital and digital-to-analog conversions, making it particularly suitable for efficient near-sensor processing. We demonstrate this by using the accelerated BrainScaleS-2 mixed-signal...

---

### 15. Landscape-aware Automated Algorithm Design: An Efficient Framework for Real-world Optimization

**Authors:** Haoran Yin, Shuaiqun Pan, Zhao Wei, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04529v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04529v1)

**Summary:** The advent of Large Language Models (LLMs) has opened new frontiers in automated algorithm design, giving rise to numerous powerful methods. However, these approaches retain critical limitations: they require extensive evaluation of the target problem to guide the search process, making them impractical for real-world optimization tasks, where each evaluation consumes substantial computational resources. This research proposes an innovative and efficient framework that decouples algorithm discov...

---

### 16. A logical re-conception of neural networks: Hamiltonian bitwise part-whole architecture

**Authors:** E Bowen, R Granger, A Rodriguez

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04911v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04911v1)

**Summary:** We introduce a simple initial working system in which relations (such as part-whole) are directly represented via an architecture with operating and learning rules fundamentally distinct from standard artificial neural network methods. Arbitrary data are straightforwardly encoded as graphs whose edges correspond to codes from a small fixed primitive set of elemental pairwise relations, such that simple relational encoding is not an add-on, but occurs intrinsically within the most basic component...

---

### 17. Statistical Guarantees for Reasoning Probes on Looped Boolean Circuits

**Authors:** Anastasis Kratsios, Giulia Livieri, A. Martina Neuman

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03970v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03970v1)

**Summary:** We study the statistical behaviour of reasoning probes in a stylized model of looped reasoning, given by Boolean circuits whose computational graph is a perfect $ν$-ary tree ($ν\ge 2$) and whose output is appended to the input and fed back iteratively for subsequent computation rounds. A reasoning probe has access to a sampled subset of internal computation nodes, possibly without covering the entire graph, and seeks to infer which $ν$-ary Boolean gate is executed at each queried node, represent...

---

### 18. Non-linear PCA via Evolution Strategies: a Novel Objective Function

**Authors:** Thomas Uriot, Elise Chung

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03967v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03967v1)

**Summary:** Principal Component Analysis (PCA) is a powerful and popular dimensionality reduction technique. However, due to its linear nature, it often fails to capture the complex underlying structure of real-world data. While Kernel PCA (kPCA) addresses non-linearity, it sacrifices interpretability and struggles with hyperparameter selection. In this paper, we propose a robust non-linear PCA framework that unifies the interpretability of PCA with the flexibility of neural networks. Our method parametrize...

---

### 19. Investigating Quantum Circuit Designs Using Neuro-Evolution

**Authors:** Devroop Kar, Daniel Krutz, Travis Desell

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03840v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03840v1)

**Summary:** Designing effective quantum circuits remains a central challenge in quantum computing, as circuit structure strongly influences expressivity, trainability, and hardware feasibility. Current approaches, whether using manually designed circuit templates, fixed heuristics, or automated rules, face limitations in scalability, flexibility, and adaptability, often producing circuits that are poorly matched to the specific problem or quantum hardware. In this work, we propose the Evolutionary eXplorati...

---

### 20. FOVI: A biologically-inspired foveated interface for deep vision models

**Authors:** Nicholas M. Blauch, George A. Alvarez, Talia Konkle

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03766v1)

**Summary:** Human vision is foveated, with variable resolution peaking at the center of a large field of view; this reflects an efficient trade-off for active sensing, allowing eye-movements to bring different parts of the world into focus with other parts of the world in context. In contrast, most computer vision systems encode the visual world at a uniform resolution, raising challenges for processing full-field high-resolution images efficiently. We propose a foveated vision interface (FOVI) based on the...

---

### 21. Equilibrium Propagation for Non-Conservative Systems

**Authors:** Antonino Emanuele Scurria, Dimitri Vanden Abeele, Bortolo Matteo Mognetti, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03670v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03670v1)

**Summary:** Equilibrium Propagation (EP) is a physics-inspired learning algorithm that uses stationary states of a dynamical system both for inference and learning. In its original formulation it is limited to conservative systems, $\textit{i.e.}$ to dynamics which derive from an energy function. Given their importance in applications, it is important to extend EP to nonconservative systems, $\textit{i.e.}$ systems with non-reciprocal interactions. Previous attempts to generalize EP to such systems failed t...

---

### 22. NeuroPareto: Calibrated Acquisition for Costly Many-Goal Search in Vast Parameter Spaces

**Authors:** Rong Fu, Wenxin Zhang, Chunlei Meng, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03901v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03901v1)

**Summary:** The pursuit of optimal trade-offs in high-dimensional search spaces under stringent computational constraints poses a fundamental challenge for contemporary multi-objective optimization. We develop NeuroPareto, a cohesive architecture that integrates rank-centric filtering, uncertainty disentanglement, and history-conditioned acquisition strategies to navigate complex objective landscapes. A calibrated Bayesian classifier estimates epistemic uncertainty across non-domination tiers, enabling rapi...

---

### 23. Contrastive Concept-Tree Search for LLM-Assisted Algorithm Discovery

**Authors:** Timothee Leleu, Sudeera Gunathilaka, Federico Ghimenti, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03132v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03132v1)

**Summary:** Large language Model (LLM)-assisted algorithm discovery is an iterative, black-box optimization process over programs to approximatively solve a target task, where an LLM proposes candidate programs and an external evaluator provides task feedback. Despite intense recent research on the topic and promising results, how can the LLM internal representation of the space of possible programs be maximally exploited to improve performance is an open question. Here, we introduce Contrastive Concept-Tre...

---

### 24. RPG-AE: Neuro-Symbolic Graph Autoencoders with Rare Pattern Mining for Provenance-Based Anomaly Detection

**Authors:** Asif Tauhid, Sidahmed Benabderrahmane, Mohamad Altrabulsi, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.02929v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02929v1)

**Summary:** Advanced Persistent Threats (APTs) are sophisticated, long-term cyberattacks that are difficult to detect because they operate stealthily and often blend into normal system behavior. This paper presents a neuro-symbolic anomaly detection framework that combines a Graph Autoencoder (GAE) with rare pattern mining to identify APT-like activities in system-level provenance data. Our approach first constructs a process behavioral graph using k-Nearest Neighbors based on feature similarity, then learn...

---

### 25. Refining Decision Boundaries In Anomaly Detection Using Similarity Search Within the Feature Space

**Authors:** Sidahmed Benabderrahmane, Petko Valtchev, James Cheney, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02925v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02925v1)

**Summary:** Detecting rare and diverse anomalies in highly imbalanced datasets-such as Advanced Persistent Threats (APTs) in cybersecurity-remains a fundamental challenge for machine learning systems. Active learning offers a promising direction by strategically querying an oracle to minimize labeling effort, yet conventional approaches often fail to exploit the intrinsic geometric structure of the feature space for model refinement. In this paper, we introduce SDA2E, a Sparse Dual Adversarial Attention-bas...

---

### 26. Automatic Design of Optimization Test Problems with Large Language Models

**Authors:** Wojciech Achtelik, Hubert Guzowski, Maciej Smołka, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02724v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02724v1)

**Summary:** The development of black-box optimization algorithms depends on the availability of benchmark suites that are both diverse and representative of real-world problem landscapes. Widely used collections such as BBOB and CEC remain dominated by hand-crafted synthetic functions and provide limited coverage of the high-dimensional space of Exploratory Landscape Analysis (ELA) features, which in turn biases evaluation and hinders training of meta-black-box optimizers. We introduce Evolution of Test Fun...

---

### 27. Energy-Efficient Neuromorphic Computing for Edge AI: A Framework with Adaptive Spiking Neural Networks and Hardware-Aware Optimization

**Authors:** Olaf Yunus Laitinen Imanov, Derya Umut Kulali, Taner Yilmaz, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02439v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02439v1)

**Summary:** Edge AI applications increasingly require ultra-low-power, low-latency inference. Neuromorphic computing based on event-driven spiking neural networks (SNNs) offers an attractive path, but practical deployment on resource-constrained devices is limited by training difficulty, hardware-mapping overheads, and sensitivity to temporal dynamics. We present NeuEdge, a framework that combines adaptive SNN models with hardware-aware optimization for edge deployment. NeuEdge uses a temporal coding scheme...

---

### 28. Introns and Templates Matter: Rethinking Linkage in GP-GOMEA

**Authors:** Johannes Koch, Tanja Alderliesten, Peter A. N. Bosman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02311v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02311v1)

**Summary:** GP-GOMEA is among the state-of-the-art for symbolic regression, especially when it comes to finding small and potentially interpretable solutions. A key mechanism employed in any GOMEA variant is the exploitation of linkage, the dependencies between variables, to ensure efficient evolution. In GP-GOMEA, mutual information between node positions in GP trees has so far been used to learn linkage. For this, a fixed expression template is used. This however leads to introns for expressions smaller t...

---

### 29. Spark: Modular Spiking Neural Networks

**Authors:** Mario Franco, Carlos Gershenson

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02306v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02306v1)

**Summary:** Nowadays, neural networks act as a synonym for artificial intelligence. Present neural network models, although remarkably powerful, are inefficient both in terms of data and energy. Several alternative forms of neural networks have been proposed to address some of these problems. Specifically, spiking neural networks are suitable for efficient hardware implementations. However, effective learning algorithms for spiking networks remain elusive, although it is suspected that effective plasticity ...

---

### 30. Backpropagation as Physical Relaxation: Exact Gradients in Finite Time

**Authors:** Antonino Emanuele Scurria

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02281v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02281v1)

**Summary:** Backpropagation, the foundational algorithm for training neural networks, is typically understood as a symbolic computation that recursively applies the chain rule. We show it emerges exactly as the finite-time relaxation of a physical dynamical system. By formulating feedforward inference as a continuous-time process and applying Lagrangian theory of non-conservative systems to handle asymmetric interactions, we derive a global energy functional on a doubled state space encoding both activation...

---

### 31. Online Fine-Tuning of Pretrained Controllers for Autonomous Driving via Real-Time Recurrent RL

**Authors:** Julian Lemmel, Felix Resch, Mónika Farsang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02236v2) | 📄 [PDF](https://arxiv.org/pdf/2602.02236v2)

**Summary:** Deploying pretrained policies in real-world applications presents substantial challenges that fundamentally limit the practical applicability of learning-based control systems. When autonomous systems encounter environmental changes in system dynamics, sensor drift, or task objectives, fixed policies rapidly degrade in performance. We show that employing Real-Time Recurrent Reinforcement Learning (RTRRL), a biologically plausible algorithm for online adaptation, can effectively fine-tune a pretr...

---

### 32. Scale-covariant spiking wavelets

**Authors:** Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02020v2) | 📄 [PDF](https://arxiv.org/pdf/2602.02020v2)

**Summary:** We establish a theoretical connection between wavelet transforms and spiking neural networks through scale-space theory. We rely on the scale-covariant guarantees in the leaky integrate-and-fire neurons to implement discrete mother wavelets that approximate continuous wavelets. A reconstruction experiment demonstrates the feasibility of the approach and warrants further analysis to mitigate current approximation errors. Our work suggests a novel spiking signal representation that could enable mo...

---

### 33. SpikingGamma: Surrogate-Gradient Free and Temporally Precise Online Training of Spiking Neural Networks with Smoothed Delays

**Authors:** Roel Koopman, Sebastian Otte, Sander Bohté

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01978v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01978v1)

**Summary:** Neuromorphic hardware implementations of Spiking Neural Networks (SNNs) promise energy-efficient, low-latency AI through sparse, event-driven computation. Yet, training SNNs under fine temporal discretization remains a major challenge, hindering both low-latency responsiveness and the mapping of software-trained SNNs to efficient hardware. In current approaches, spiking neurons are modeled as self-recurrent units, embedded into recurrent networks to maintain state over time, and trained with BPT...

---

### 34. Fine-Tuning Language Models to Know What They Know

**Authors:** Sangjun Park, Elliot Meyerson, Xin Qiu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02605v1)

**Summary:** Metacognition is a critical component of intelligence, specifically regarding the awareness of one's own knowledge. While humans rely on shared internal memory for both answering questions and reporting their knowledge state, this dependency in LLMs remains underexplored. This study proposes a framework to measure metacognitive ability $d_{\rm{type2}}'$ using a dual-prompt method, followed by the introduction of Evolution Strategy for Metacognitive Alignment (ESMA) to bind a model's internal kno...

---

### 35. Enhancing Generalization in Evolutionary Feature Construction for Symbolic Regression through Vicinal Jensen Gap Minimization

**Authors:** Hengzhe Zhang, Qi Chen, Bing Xue, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01510v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01510v1)

**Summary:** Genetic programming-based feature construction has achieved significant success in recent years as an automated machine learning technique to enhance learning performance. However, overfitting remains a challenge that limits its broader applicability. To improve generalization, we prove that vicinal risk, estimated through noise perturbation or mixup-based data augmentation, is bounded by the sum of empirical risk and a regularization term-either finite difference or the vicinal Jensen gap. Leve...

---

### 36. Dynamic Heuristic Neuromorphic Solver for the Edge User Allocation Problem with Bayesian Confidence Propagation Neural Network

**Authors:** Kecheng Zhang, Anders Lansner, Ahsan Javed Awan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01294v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01294v1)

**Summary:** We propose a neuromorphic solver for the NP-hard Edge User Allocation problem using an attractor network with Winner-Takes-All (WTA) mechanism implemented with the Bayesian Confidence Propagation Neural Network (BCPNN) framework. Unlike previous energy-based attractor networks, our solver uses dynamic heuristic biasing to guide allocations in real time and introduces a "no allocation" state to each WTA motif, achieving near-optimal performance with an empirically upper-bounded number of time ste...

---

### 37. Unleashing the Potential of Differential Evolution through Individual-Level Strategy Diversity

**Authors:** Chenchen Feng, Minyang Chen, Zhuozhao Li, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01147v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01147v1)

**Summary:** Since Differential Evolution (DE) is sensitive to strategy choice, most existing variants pursue performance through adaptive mechanisms or intricate designs. While these approaches focus on adjusting strategies over time, the structural benefits that static strategy diversity may bring remain largely unexplored. To bridge this gap, we study the impact of individual-level strategy diversity on DE's search dynamics and performance, and introduce iStratDE (DE with individual-level strategies), a m...

---

### 38. Parallel Training in Spiking Neural Networks

**Authors:** Yanbin Huang, Man Yao, Yuqi Pan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01133v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01133v1)

**Summary:** The bio-inspired integrate-fire-reset mechanism of spiking neurons constitutes the foundation for efficient processing in Spiking Neural Networks (SNNs). Recent progress in large models demands that spiking neurons support highly parallel computation to scale efficiently on modern GPUs. This work proposes a novel functional perspective that provides general guidance for designing parallel spiking neurons. We argue that the reset mechanism, which induces complex temporal dependencies and hinders ...

---

### 39. The Stacked Autoencoder Evolution Hypothesis

**Authors:** Hiroyuki Iizuka

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01026v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01026v1)

**Summary:** This study introduces a novel theoretical framework, the Stacked Autoencoder Evolution Hypothesis, which proposes that biological evolutionary systems operate through multi-layered self-encoding and decoding processes, analogous to stacked autoencoders in deep learning. Rather than viewing evolution solely as gradual changes driven by mutation and selection, this hypothesis suggests that self-replication inherently compresses and reconstructs genetic information across hierarchical layers of abs...

---

### 40. Navigating Simply, Aligning Deeply: Winning Solutions for Mouse vs. AI 2025

**Authors:** Phu-Hoa Pham, Chi-Nguyen Tran, Dao Sy Duy Minh, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.00982v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00982v1)

**Summary:** Visual robustness and neural alignment remain critical challenges in developing artificial agents that can match biological vision systems. We present the winning approaches from Team HCMUS_TheFangs for both tracks of the NeurIPS 2025 Mouse vs. AI: Robust Visual Foraging Competition. For Track 1 (Visual Robustness), we demonstrate that architectural simplicity combined with targeted components yields superior generalization, achieving 95.4% final score with a lightweight two-layer CNN enhanced b...

---

### 41. Organismal Agency and Rapid Adaptation: The Phenopoiesis Algorithm for Phenotype-First Evolution

**Authors:** Nam H. Le

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.00978v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00978v1)

**Summary:** Evolutionary success depends on the capacity to adapt: organisms must respond to environmental challenges through both genetic innovation and lifetime learning. The gene-centric paradigm attributes evolutionary causality exclusively to genes, while Denis Noble's phenotype-first framework argues that organisms are active agents capable of interpreting genetic resources, learning from experience, and shaping their own development. However, this framework has remained philosophically intuitive but ...

---

### 42. NegaBent, No Regrets: Evolving Spectrally Flat Boolean Functions

**Authors:** Claude Carlet, Marko Ðurasevic, Ermes Franch, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00843v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00843v1)

**Summary:** Negabent Boolean functions are defined by having a flat magnitude spectrum under the nega-Hadamard transform. They exist in both even and odd dimensions, and the subclass of functions that are simultaneously bent and negabent (bent-negabent) has attracted interest due to the combined optimal periodic and negaperiodic spectral properties. In this work, we investigate how evolutionary algorithms can be used to evolve (bent-)negabent Boolean functions. Our experimental results indicate that evoluti...

---

### 43. IDEM Enough? Evolving Highly Nonlinear Idempotent Boolean Functions

**Authors:** Claude Carlet, Marko Ðurasevic, Domagoj Jakobovic, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00837v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00837v1)

**Summary:** Idempotent Boolean functions form a highly structured subclass of Boolean functions that is closely related to rotation symmetry under a normal-basis representation and to invariance under a fixed linear map in a polynomial basis. These functions are attractive as candidates for cryptographic design, yet their additional algebraic constraints make the search for high nonlinearity substantially more difficult than in the unconstrained case. In this work, we investigate evolutionary methods for co...

---

### 44. Evolving Interpretable Constitutions for Multi-Agent Coordination

**Authors:** Ujwal Kumar, Alice Saito, Hershraj Niranjani, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00755v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00755v1)

**Summary:** Constitutional AI has focused on single-model alignment using fixed principles. However, multi-agent systems create novel alignment challenges through emergent social dynamics. We present Constitutional Evolution, a framework for automatically discovering behavioral norms in multi-agent LLM systems. Using a grid-world simulation with survival pressure, we study the tension between individual and collective welfare, quantified via a Societal Stability Score S in [0,1] that combines productivity, ...

---

### 45. Surrogate Ensemble in Expensive Multi-Objective Optimization via Deep Q-Learning

**Authors:** Yuxin Wu, Hongshu Guo, Ting Huang, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00540v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00540v1)

**Summary:** Surrogate-assisted Evolutionary Algorithms~(SAEAs) have shown promising robustness in solving expensive optimization problems. A key aspect that impacts SAEAs' effectiveness is surrogate model selection, which in existing works is predominantly decided by human developer. Such human-made design choice introduces strong bias into SAEAs and may hurt their expected performance on out-of-scope tasks. In this paper, we propose a reinforcement learning-assisted ensemble framework, termed as SEEMOO, wh...

---

### 46. Reinforcement Learning-assisted Constraint Relaxation for Constrained Expensive Optimization

**Authors:** Qianhao Zhu, Sijie Ma, Zeyuan Ma, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00532v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00532v1)

**Summary:** Constraint handling plays a key role in solving realistic complex optimization problems. Though intensively discussed in the last few decades, existing constraint handling techniques predominantly rely on human experts' designs, which more or less fall short in utility towards general cases. Motivated by recent progress in Meta-Black-Box Optimization where automated algorithm design can be learned to boost optimization performance, in this paper, we propose learning effective, adaptive and gener...

---

### 47. Quality-Diversity Optimization as Multi-Objective Optimization

**Authors:** Xi Lin, Ping Guo, Yilu Liu, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00478v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00478v1)

**Summary:** The Quality-Diversity (QD) optimization aims to discover a collection of high-performing solutions that simultaneously exhibit diverse behaviors within a user-defined behavior space. This paradigm has stimulated significant research interest and demonstrated practical utility in domains including robot control, creative design, and adversarial sample generation. A variety of QD algorithms with distinct design principles have been proposed in recent years. Instead of proposing a new QD algorithm,...

---

### 48. COBRA++: Enhanced COBRA Optimizer with Augmented Surrogate Pool and Reinforced Surrogate Selection

**Authors:** Zipei Yu, Zhiyang Huang, Hongshu Guo, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.22624v2) | 📄 [PDF](https://arxiv.org/pdf/2601.22624v2)

**Summary:** The optimization problems in realistic world present significant challenges onto optimization algorithms, such as the expensive evaluation issue and complex constraint conditions. COBRA optimizer (including its up-to-date variants) is a representative and effective tool for addressing such optimization problems, which introduces 1) RBF surrogate to reduce online evaluation and 2) bi-stage optimization process to alternate search for feasible solution and optimal solution. Though promising, its d...

---

### 49. Detect and Act: Automated Dynamic Optimizer through Meta-Black-Box Optimization

**Authors:** Zijian Gao, Yuanting Zhong, Zeyuan Ma, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.22542v1) | 📄 [PDF](https://arxiv.org/pdf/2601.22542v1)

**Summary:** Dynamic Optimization Problems (DOPs) are challenging to address due to their complex nature, i.e., dynamic environment variation. Evolutionary Computation methods are generally advantaged in solving DOPs since they resemble dynamic biological evolution. However, existing evolutionary dynamic optimization methods rely heavily on human-crafted adaptive strategy to detect environment variation in DOPs, and then adapt the searching strategy accordingly. These hand-crafted strategies may perform inef...

---

### 50. Fairness-Aware Performance Evaluation for Multi-Party Multi-Objective Optimization

**Authors:** Zifan Zhao, Peilan Xu, Wenjian Luo

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.22497v1) | 📄 [PDF](https://arxiv.org/pdf/2601.22497v1)

**Summary:** In multiparty multiobjective optimization problems, solution sets are usually evaluated using classical performance metrics, aggregated across DMs. However, such mean-based evaluations may be unfair by favoring certain parties, as they assume identical geometric approximation quality to each party's PF carries comparable evaluative significance. Moreover, prevailing notions of MPMOP optimal solutions are restricted to strictly common Pareto optimal solutions, representing a narrow form of cooper...

---

## q-bio.NC

**50 papers**

### 1. Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space

**Authors:** Felipe D. Toro-Hernández, Jesuino Vieira Filho, Rodrigo M. Cabral-Carvalho

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05971v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05971v1)

**Summary:** Semantic representations can be framed as a structured, dynamic knowledge space through which humans navigate to retrieve and manipulate meaning. To investigate how humans traverse this geometry, we introduce a framework that represents concept production as navigation through embedding space. Using different transformer text embedding models, we construct participant-specific semantic trajectories based on cumulative embeddings and extract geometric and dynamical metrics, including distance to ...

---

### 2. BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction

**Authors:** Xuanhua Yin, Runkai Zhao, Lina Yao, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04512v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04512v1)

**Summary:** Naturalistic fMRI characterizes the brain as a dynamic predictive engine driven by continuous sensory streams. However, modeling the causal forward evolution in realistic neural simulation is impeded by the timescale mismatch between multimodal inputs and the complex topology of cortical networks. To address these challenges, we introduce BrainVista, a multimodal autoregressive framework designed to model the causal evolution of brain states. BrainVista incorporates Network-wise Tokenizers to di...

---

### 3. Discovering Mechanistic Models of Neural Activity: System Identification in an in Silico Zebrafish

**Authors:** Jan-Matthis Lueckmann, Viren Jain, Michał Januszewski

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04492v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04492v1)

**Summary:** Constructing mechanistic models of neural circuits is a fundamental goal of neuroscience, yet verifying such models is limited by the lack of ground truth. To rigorously test model discovery, we establish an in silico testbed using neuromechanical simulations of a larval zebrafish as a transparent ground truth. We find that LLM-based tree search autonomously discovers predictive models that significantly outperform established forecasting baselines. Conditioning on sensory drive is necessary but...

---

### 4. Multi-Integration of Labels across Categories for Component Identification (MILCCI)

**Authors:** Noga Mudrik, Yuxi Chen, Gal Mishne, et al.

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04270v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04270v1)

**Summary:** Many fields collect large-scale temporal data through repeated measurements (trials), where each trial is labeled with a set of metadata variables spanning several categories. For example, a trial in a neuroscience study may be linked to a value from category (a): task difficulty, and category (b): animal choice. A critical challenge in time-series analysis is to understand how these labels are encoded within the multi-trial observations, and disentangle the distinct effect of each label entry a...

---

### 5. A computational account of dreaming: learning and memory consolidation

**Authors:** Qi Zhang

**Published:** 2026-02-04

🔗 [Paper](http://arxiv.org/abs/2602.04095v1) | 📄 [PDF](https://arxiv.org/pdf/2602.04095v1)

**Summary:** A number of studies have concluded that dreaming is mostly caused by randomly arriving internal signals because "dream contents are random impulses", and argued that dream sleep is unlikely to play an important part in our intellectual capacity. On the contrary, numerous functional studies have revealed that dream sleep does play an important role in our learning and other intellectual functions. Specifically, recent studies have suggested the importance of dream sleep in memory consolidation, f...

---

### 6. FOVI: A biologically-inspired foveated interface for deep vision models

**Authors:** Nicholas M. Blauch, George A. Alvarez, Talia Konkle

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03766v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03766v1)

**Summary:** Human vision is foveated, with variable resolution peaking at the center of a large field of view; this reflects an efficient trade-off for active sensing, allowing eye-movements to bring different parts of the world into focus with other parts of the world in context. In contrast, most computer vision systems encode the visual world at a uniform resolution, raising challenges for processing full-field high-resolution images efficiently. We propose a foveated vision interface (FOVI) based on the...

---

### 7. A Minimal Task Reveals Emergent Path Integration and Object-Location Binding in a Predictive Sequence Model

**Authors:** Linda Ariel Ventura, Victoria Bosch, Tim C Kietzmann, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03490v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03490v1)

**Summary:** Adaptive cognition requires structured internal models representing objects and their relations. Predictive neural networks are often proposed to form such "world models", yet their underlying mechanisms remain unclear. One hypothesis is that action-conditioned sequential prediction suffices for learning such world models. In this work, we investigate this possibility in a minimal in-silico setting. Sequentially sampling tokens from 2D continuous token scenes, a recurrent neural network is train...

---

### 8. Systematic review of self-supervised foundation models for brain network representation using electroencephalography

**Authors:** Hannah Portmann, Yosuke Morishima

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03269v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03269v1)

**Summary:** Automated analysis of electroencephalography (EEG) has recently undergone a paradigm shift. The introduction of transformer architectures and self-supervised pretraining (SSL) has led to the development of EEG foundation models. These models are pretrained on large amounts of unlabeled data and can be adapted to a range of downstream tasks. This systematic review summarizes recent SSL-trained EEG foundation models that learn whole-brain representations from multichannel EEG rather than represent...

---

### 9. A Hitchhiker's Guide to Poisson Gradient Estimation

**Authors:** Michael Ibrahim, Hanqi Zhao, Eli Sennesh, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03896v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03896v1)

**Summary:** Poisson-distributed latent variable models are widely used in computational neuroscience, but differentiating through discrete stochastic samples remains challenging. Two approaches address this: Exponential Arrival Time (EAT) simulation and Gumbel-SoftMax (GSM) relaxation. We provide the first systematic comparison of these methods, along with practical guidance for practitioners. Our main technical contribution is a modification to the EAT method that theoretically guarantees an unbiased first...

---

### 10. Estimating measures of information processing during cognitive tasks using functional magnetic resonance imaging

**Authors:** Chetan Gohil, Oliver M. Cliff, James M. Shine, et al.

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03240v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03240v1)

**Summary:** Cognition is increasingly framed in terms of information processing, yet most fMRI analyses focus on activation or functional connectivity rather than quantifying how information is stored and transferred. To remedy this problem, we propose a framework for estimating measures of information processing: active information storage (AIS), transfer entropy (TE), and net synergy from task-based fMRI. AIS measures information maintained within a region, TE captures directed information flow, and net s...

---

### 11. Adversarial construction as a potential solution to the experiment design problem in large task spaces

**Authors:** Prakhar Godara, Frederick Callaway, Marcelo G. Mattar

**Published:** 2026-02-03

🔗 [Paper](http://arxiv.org/abs/2602.03172v1) | 📄 [PDF](https://arxiv.org/pdf/2602.03172v1)

**Summary:** Despite decades of work, we still lack a robust, task-general theory of human behavior even in the simplest domains. In this paper we tackle the generality problem head-on, by aiming to develop a unified model for all tasks embedded in a task-space. In particular we consider the space of binary sequence prediction tasks where the observations are generated by the space parameterized by hidden Markov models (HMM). As the space of tasks is large, experimental exploration of the entire space is inf...

---

### 12. A Reproducible Framework for Bias-Resistant Machine Learning on Small-Sample Neuroimaging Data

**Authors:** Jagan Mohan Reddy Dwarampudi, Jennifer L Purks, Joshua Wong, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02920v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02920v1)

**Summary:** We introduce a reproducible, bias-resistant machine learning framework that integrates domain-informed feature engineering, nested cross-validation, and calibrated decision-threshold optimization for small-sample neuroimaging data. Conventional cross-validation frameworks that reuse the same folds for both model selection and performance estimation yield optimistically biased results, limiting reproducibility and generalization. Demonstrated on a high-dimensional structural MRI dataset of deep b...

---

### 13. MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training

**Authors:** Dulhan Jayalath, Oiwi Parker Jones

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02494v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02494v1)

**Summary:** Clinical brain-to-text interfaces are designed for paralysed patients who cannot provide extensive training recordings. Pre-training improves data-efficient generalisation by learning statistical priors across subjects, but these priors critically depend on context. While natural speech might unfold gradually over minutes, most methods pre-train with only a few seconds of context. Thus, we propose MEG-XL, a model pre-trained with 2.5 minutes of MEG context per sample, 5-300x longer than prior wo...

---

### 14. Fine-Tuning Language Models to Know What They Know

**Authors:** Sangjun Park, Elliot Meyerson, Xin Qiu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02605v1)

**Summary:** Metacognition is a critical component of intelligence, specifically regarding the awareness of one's own knowledge. While humans rely on shared internal memory for both answering questions and reporting their knowledge state, this dependency in LLMs remains underexplored. This study proposes a framework to measure metacognitive ability $d_{\rm{type2}}'$ using a dual-prompt method, followed by the introduction of Evolution Strategy for Metacognitive Alignment (ESMA) to bind a model's internal kno...

---

### 15. Community-Level Modeling of Gyral Folding Patterns for Robust and Anatomically Informed Individualized Brain Mapping

**Authors:** Minheng Chen, Tong Chen, Yan Zhuang, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01482v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01482v1)

**Summary:** Cortical folding exhibits substantial inter-individual variability while preserving stable anatomical landmarks that enable fine-scale characterization of cortical organization. Among these, the three-hinge gyrus (3HG) serves as a key folding primitive, showing consistent topology yet meaningful variations in morphology, connectivity, and function. Existing landmark-based methods typically model each 3HG independently, ignoring that 3HGs form higher-order folding communities that capture mesosca...

---

### 16. Vulnerability-Amplifying Interaction Loops: a systematic failure mode in AI chatbot mental-health interactions

**Authors:** Veith Weilnhammer, Kevin YC Hou, Raymond Dolan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01347v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01347v1)

**Summary:** Millions of users turn to consumer AI chatbots to discuss behavioral and mental health concerns. While this presents unprecedented opportunities to deliver population-level support, it also highlights an urgent need to develop rigorous and scalable safety evaluations. Here we introduce SIM-VAIL, an AI chatbot auditing framework that captures how harmful AI chatbot responses manifest across a range of mental-health contexts. SIM-VAIL pairs a simulated human user, harboring a distinct psychiatric ...

---

### 17. Inter- and Intra-Subject Variability in EEG: A Systematic Survey

**Authors:** Xuan-The Tran, Thien-Nhan Vo, Son-Tung Vu, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01019v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01019v1)

**Summary:** Electroencephalography (EEG) underpins neuroscience, clinical neurophysiology, and brain-computer interfaces (BCIs), yet pronounced inter- and intra-subject variability limits reliability, reproducibility, and translation. This systematic review studies that quantified or modeled EEG variability across resting-state, event-related potentials (ERPs), and task-related/BCI paradigms (including motor imagery and SSVEP) in healthy and clinical cohorts. Across paradigms, inter-subject differences are ...

---

### 18. A Distinct Communication Strategies Model of the Double Empathy Problem

**Authors:** Enrique Calderoli, Maria Cristina Varriale, Flávio Kapczinski

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2602.02562v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02562v1)

**Summary:** The double empathy problem recasts the difficulty of forming empathy bonds in social interactions between autistic and neurotypical individuals as a bidirectional problem, rather than due to a deficit exclusive to the person on the spectrum. However, no explicit mechanism to explain such a phenomenon has been proposed. Here we build a feedback-loop mathematical model that would theoretically induce the empathy degradation observed during communication in neurotypical-autistic pairs solely due to...

---

### 19. The Where and How of Touch: A Review of Tactile Localization Research

**Authors:** Xaver Fuchs, Jason A. M. Khoury, Sergiu Tcaci Popescu, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.23023v1) | 📄 [PDF](https://arxiv.org/pdf/2601.23023v1)

**Summary:** Tactile localization is the seemingly simple ability to 'tell' where a touch has occurred. However, how this ability is assessed, and what conclusions are drawn from experiments, depends on the theoretical ideas that inspire the research. Here, we review both theoretical frameworks and methodological approaches based on a systematic web-based literature search on tactile localization. After presenting current theories of tactile localization, we discuss task characteristics that differentiate cu...

---

### 20. Deep Learning Pose Estimation for Multi-Label Recognition of Combined Hyperkinetic Movement Disorders

**Authors:** Laura Cif, Diane Demailly, Gabriella A. Horvàth, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2602.00163v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00163v1)

**Summary:** Hyperkinetic movement disorders (HMDs) such as dystonia, tremor, chorea, myoclonus, and tics are disabling motor manifestations across childhood and adulthood. Their fluctuating, intermittent, and frequently co-occurring expressions hinder clinical recognition and longitudinal monitoring, which remain largely subjective and vulnerable to inter-rater variability. Objective and scalable methods to distinguish overlapping HMD phenotypes from routine clinical videos are still lacking. Here, we devel...

---

### 21. How 'Neural' is a Neural Foundation Model?

**Authors:** Johannes Bertram, Luciano Dyballa, Anderson Keller, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21508v1)

**Summary:** Foundation models have shown remarkable success in fitting biological visual systems; however, their black-box nature inherently limits their utility for understanding brain function. Here, we peek inside a SOTA foundation model of neural activity (Wang et al., 2025) as a physiologist might, characterizing each 'neuron' based on its temporal response properties to parametric stimuli. We analyze how different stimuli are represented in neural activity space by building decoding manifolds, and we ...

---

### 22. Differential Dynamic Causal Nets: Model Construction, Identification and Group Comparisons

**Authors:** Kang You, Gary Green, Jian Zhang

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21478v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21478v1)

**Summary:** Pathophysiolpgical modelling of brain systems from microscale to macroscale remains difficult in group comparisons partly because of the infeasibility of modelling the interactions of thousands of neurons at the scales involved. Here, to address the challenge, we present a novel approach to construct differential causal networks directly from electroencephalogram (EEG) data. The proposed network is based on conditionally coupled neuronal circuits which describe the average behaviour of interacti...

---

### 23. BrainFuse: a unified infrastructure integrating realistic biological modeling and core AI methodology

**Authors:** Baiyu Chen, Yujie Wu, Siyuan Xu, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21407v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21407v1)

**Summary:** Neuroscience and artificial intelligence represent distinct yet complementary pathways to general intelligence. However, amid the ongoing boom in AI research and applications, the translational synergy between these two fields has grown increasingly elusive-hampered by a widening infrastructural incompatibility: modern AI frameworks lack native support for biophysical realism, while neural simulation tools are poorly suited for gradient-based optimization and neuromorphic hardware deployment. To...

---

### 24. An explainable framework for the relationship between dementia and glucose metabolism patterns

**Authors:** C. Vázquez-García, F. J. Martínez-Murcia, F. Segovia Román, et al.

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20480v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20480v1)

**Summary:** High-dimensional neuroimaging data presents challenges for assessing neurodegenerative diseases due to complex non-linear relationships. Variational Autoencoders (VAEs) can encode scans into lower-dimensional latent spaces capturing disease-relevant features. We propose a semi-supervised VAE framework with a flexible similarity regularization term that aligns selected latent variables with clinical or biomarker measures of dementia progression. This allows adapting the similarity metric and supe...

---

### 25. Assembling the Mind's Mosaic: Towards EEG Semantic Intent Decoding

**Authors:** Jiahe Li, Junru Chen, Fanqi Shen, et al.

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20447v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20447v1)

**Summary:** Enabling natural communication through brain-computer interfaces (BCIs) remains one of the most profound challenges in neuroscience and neurotechnology. While existing frameworks offer partial solutions, they are constrained by oversimplified semantic representations and a lack of interpretability. To overcome these limitations, we introduce Semantic Intent Decoding (SID), a novel framework that translates neural activity into natural language by modeling meaning as a flexible set of composition...

---

### 26. Implications of temporal sampling in voltage imaging microscopy

**Authors:** Jakub Czuchnowski, Jerome Mertz

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20236v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20236v1)

**Summary:** Significance: Voltage imaging microscopy has emerged as a powerful tool to investigate neural activity both in vivo and in vitro. Various imaging approaches have been developed, including point-scanning, line-scanning and wide-field microscopes, however the effects of their different temporal sampling methods on signal fidelity have not yet been fully investigated. Aim: To provide an analysis of the inherent advantages and disadvantages of temporal sampling in scanning and wide-field microscopes...

---

### 27. Stroboscopic motion reversals in delay-coupled neural fields

**Authors:** Noah Parks, Zachary P Kilpatrick

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19125v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19125v1)

**Summary:** Visual illusions provide a window into the mechanisms underlying visual processing, and dynamical neural circuit models offer a natural framework for proposing and testing theories of their emergence. We propose and analyze a delay-coupled neural field model that explains stroboscopic percepts arising from the subsampling of a moving, often rotating, stimulus, such as the wagon-wheel illusion. Motivated by the role of activity propagation delays in shaping visual percepts, we study neural fields...

---

### 28. Smooth embeddings in contracting recurrent networks driven by regular dynamics: A synthesis for neural representation

**Authors:** Vikas N. O'Reilly-Shah, Alessandro Maria Selvitella

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.19019v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19019v1)

**Summary:** Recurrent neural networks trained for time-series prediction often develop latent trajectories that preserve qualitative structure of the dynamical systems generating their inputs. Recent empirical work has documented topology-preserving latent organization in trained recurrent models, and recent theoretical results in reservoir computing establish conditions under which the synchronization map is an embedding. Here we synthesize these threads into a unified account of when contracting recurrent...

---

### 29. Schema-based active inference supports rapid generalization of experience and frontal cortical coding of abstract structure

**Authors:** Toon Van de Maele, Tim Verbelen, Dileep George, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18946v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18946v1)

**Summary:** Schemas -- abstract relational structures that capture the commonalities across experiences -- are thought to underlie humans' and animals' ability to rapidly generalize knowledge, rebind new experiences to existing structures, and flexibly adapt behavior across contexts. Despite their central role in cognition, the computational principles and neural mechanisms supporting schema formation and use remain elusive. Here, we introduce schema-based hierarchical active inference (S-HAI), a novel comp...

---

### 30. Closed Eyes and Coil Size -- Effects on Motor Threshold and Intracortical Inhibition, measured with TMS

**Authors:** Meher Sabharwal, Narin Suleyman, Gabriel R. Palma, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18286v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18286v1)

**Summary:** Rationale: Transcranial magnetic stimulation (TMS)-based measures such as resting motor threshold (RMT) and short interval intracortical inhibition (SICI) are widely employed to study motor cortical and corticospinal tract function, and effects of diseases and drug therapies thereon. However, the effect of key experimental factors, including as eye state (open or closed) or stimulating coil size, remain unclear. As such, it is unknown whether these factors must be kept consistent across multi-ce...

---

### 31. AI and World Models

**Authors:** Robert Worden

**Published:** 2026-01-25

🔗 [Paper](http://arxiv.org/abs/2601.17796v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17796v1)

**Summary:** While large neural nets perform impressively on specific tasks, they are unreliable and unsafe, as is shown by the persistent hallucinations of large language models. This paper shows that large neural nets are intrinsically unreliable, because it is not possible to make or validate a tractable theory of how a neural net works. There is no reliable way to extrapolate its performance from a limited number of test cases to an unlimited set of use cases. To have confidence in the performance of a n...

---

### 32. Sampling in the Euclidean Motion Group and a Problem from Brain's Primary Visual Cortex

**Authors:** Davide Barbieri

**Published:** 2026-01-24

🔗 [Paper](http://arxiv.org/abs/2601.17528v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17528v1)

**Summary:** We study a sampling problem for the abstract wavelet transform associated with the quasiregular representation of the $SE(2)$ group, for a modulated gaussian mother wavelet. This problem is motivated by the behavior of brain's primary visual cortex. We provide a characterization in terms of a dual Gramian matrix, and study numerically the relationships among the parameters defining the sampling and the mother wavelet.

---

### 33. Unsupervised sleep-like intra- and inter-layer plasticity categorizes and improves energy efficiency in a multilayer spiking network

**Authors:** Leonardo Tonielli, Cosimo Lupo, Elena Pastorelli, et al.

**Published:** 2026-01-24

🔗 [Paper](http://arxiv.org/abs/2601.17523v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17523v1)

**Summary:** Sleep is thought to support memory consolidation and the recovery of optimal energetic regime by reorganizing synaptic connectivity, yet how plasticity across hierarchical brain circuits contributes to abstraction and energy efficiency remains unclear. Here we study a spiking multi-layer network alternating wake-like and deep-sleep-like states, with state-dependent dendritic integration and synaptic plasticity in a biologically inspired thalamo-cortical framework. During wakefulness, the model l...

---

### 34. Neural Agonist-Antagonist Coupling in the Absence of Mechanical Coupling after Targeted Muscle Reinnervation

**Authors:** Laura Ferrante, Anna Boesendorfer, Benedikt Baumgartner, et al.

**Published:** 2026-01-23

🔗 [Paper](http://arxiv.org/abs/2601.16689v1) | 📄 [PDF](https://arxiv.org/pdf/2601.16689v1)

**Summary:** Following limb amputation and targeted muscle reinnervation (TMR), nerves supplying agonist and antagonist muscles are rerouted into separate targeted muscles, disrupting natural neuromechanical coupling between muscle groups. Using high-density intramuscular microelectrode arrays in reinnervated muscles, we show that neural signals for agonist and antagonist tasks remain functionally coupled: motor units active during agonist tasks were also recruited during corresponding antagonist tasks, desp...

---

### 35. Cognitively-Inspired Tokens Overcome Egocentric Bias in Multimodal Models

**Authors:** Bridget Leonard, Scott O. Murray

**Published:** 2026-01-23

🔗 [Paper](http://arxiv.org/abs/2601.16378v1) | 📄 [PDF](https://arxiv.org/pdf/2601.16378v1)

**Summary:** Multimodal language models (MLMs) perform well on semantic vision-language tasks but fail at spatial reasoning that requires adopting another agent's visual perspective. These errors reflect a persistent egocentric bias and raise questions about whether current models support allocentric reasoning. Inspired by human spatial cognition, we introduce perspective tokens, specialized embeddings that encode orientation through either (1) embodied body-keypoint cues or (2) abstract representations supp...

---

### 36. Resting-State Functional Connectivity Correlates of Emotional Memory Control under Cognitive load in Subclinical Anxiety

**Authors:** Shruti Kinger, Mrinmoy Chakrabarty

**Published:** 2026-01-22

🔗 [Paper](http://arxiv.org/abs/2601.15689v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15689v1)

**Summary:** Volitional memory control supports adaptive cognition by enabling intentional Recall of goal-relevant information and Suppression of unwanted memories. While neural mechanisms underlying Recall and Suppression have been studied largely in isolation, less is known about the large-scale brain networks supporting these processes under competing cognitive demands, particularly as a function of subclinical anxiety. Here, we examined control of emotionally valenced memories during directed Recall and ...

---

### 37. Machine learning-enhanced non-amnestic Alzheimer's disease diagnosis from MRI and clinical features

**Authors:** Megan A. Witherow, Michael L. Evans, Ahmed Temtam, et al.

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15530v2) | 📄 [PDF](https://arxiv.org/pdf/2601.15530v2)

**Summary:** Alzheimer's disease (AD), defined as an abnormal buildup of amyloid plaques and tau tangles in the brain can be diagnosed with high accuracy based on protein biomarkers via PET or CSF analysis. However, due to the invasive nature of biomarker collection, most AD diagnoses are made in memory clinics using cognitive tests and evaluation of hippocampal atrophy based on MRI. While clinical assessment and hippocampal volume show high diagnostic accuracy for amnestic or typical AD (tAD), a substantial...

---

### 38. Dynamic Mean Field Theories for Nonlinear Noise in Recurrent Neuronal Networks

**Authors:** Shoshana Chipman, Brent Doiron

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15462v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15462v1)

**Summary:** Strong, correlated noise in recurrent neural circuits often passes through nonlinear transfer functions, complicating dynamical mean-field analyses of complex phenomena such as transients and bifurcations. We introduce a method that replaces nonlinear functions of Ornstein-Uhlenbeck (OU) noise with a Gaussian-equivalent process matched in mean and covariance, and combine this with a lognormal moment closure for expansive nonlinearities to derive a closed dynamical mean-field theory for recurrent...

---

### 39. Circadian Modulation of Semantic Exploration in Social Media Language

**Authors:** Vuong Hung Truong, Mariana Gabrielle Cangco Reyes, Masatoshi Koizumi, et al.

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15091v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15091v1)

**Summary:** Human cognition exhibits strong circadian modulation, yet its influence on high-dimensional semantic behavior remains poorly understood. Using large-scale Reddit data, we quantify time-of-day variation in language use by embedding text into a pretrained transformer model and measuring semantic entropy as an index of linguistic exploration-exploitation, for which we show a robust circadian rhythmicity that could be entrained by seasonal light cues. Distinguishing between local and global semantic...

---

### 40. Single-Node Wilson--Cowan Model Accounts for Speech-Evoked $γ$-Band Deficits in Schizophrenia

**Authors:** Zhengdi Zhang, Yan Xu, Wenjun Xia

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15032v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15032v1)

**Summary:** Cortical gamma ($γ$)-band activity reflects local excitation-inhibition (E/I) balance. In schizophrenia (SCZ), reduced task-evoked gamma suggests altered E/I dynamics, but it is unclear whether differences stem from input properties or systematic shifts in E/I operating point and gain. We coupled a cochlear-inspired speech front end to a Wilson-Cowan E/I model to simulate gamma responses across three conditions: Healthy, SCZ-speech, and SCZ-semantics. Metrics included event-related spectral pert...

---

### 41. Power-Law Scaling in the Classification Performance of Small-Scale Spiking Neural Networks

**Authors:** Zhengdi Zhang, Cong Han, Wenjun Xia

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.14961v1) | 📄 [PDF](https://arxiv.org/pdf/2601.14961v1)

**Summary:** This paper investigates the classification capability of small-scale spiking neural networks based on the Leaky Integrate-and-Fire (LIF) neuron model. We analyze the relationship between classification accuracy and three factors: the number of neurons, the number of stimulus nodes, and the number of classification categories. Notably, we employ a large language model (LLM) to assist in discovering the underlying functional relationships among these variables, and compare its performance against ...

---

### 42. "Just in Time" World Modeling Supports Human Planning and Reasoning

**Authors:** Tony Chen, Sam Cheyette, Kelsey Allen, et al.

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.14514v1) | 📄 [PDF](https://arxiv.org/pdf/2601.14514v1)

**Summary:** Probabilistic mental simulation is thought to play a key role in human reasoning, planning, and prediction, yet the demands of simulation in complex environments exceed realistic human capacity limits. A theory with growing evidence is that people simulate using simplified representations of the environment that abstract away from irrelevant details, but it is unclear how people determine these simplifications efficiently. Here, we present a "Just-in-Time" framework for simulation-based reasonin...

---

### 43. A Dual-Head Transformer-State-Space Architecture for Neurocircuit Mechanism Decomposition from fMRI

**Authors:** Cole Korponay

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.15344v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15344v1)

**Summary:** Precision psychiatry aspires to elucidate brain-based biomarkers of psychopathology to bolster disease risk assessment and treatment development. To this end, functional magnetic resonance imaging (fMRI) has helped triangulate brain circuits whose functional features are correlated with or even predictive of forms of psychopathology. Yet, fMRI biomarkers to date remain largely descriptive identifiers of where, rather than how, neurobiology is aberrant, limiting their utility for guiding treatmen...

---

### 44. MooneyMaker: A Python package to create ambiguous two-tone images

**Authors:** Lars C. Reining, Thabo Matthies, Luisa Haussner, et al.

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.14077v1) | 📄 [PDF](https://arxiv.org/pdf/2601.14077v1)

**Summary:** Mooney images are high-contrast, two-tone visual stimuli, created by thresholding photographic images. They allow researchers to separate image content from image understanding, making them valuable for studying visual perception. An ideal Mooney image for this purpose achieves a specific balance: it initially appears unrecognizable but becomes fully interpretable to the observer after seeing the original template. Researchers traditionally created these stimuli manually using subjective criteri...

---

### 45. Optimal Calibration of the endpoint-corrected Hilbert Transform

**Authors:** Eike Osmers, Dorothea Kolossa

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.13962v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13962v1)

**Summary:** Accurate, low-latency estimates of the instantaneous phase of oscillations are essential for closed-loop sensing and actuation, including (but not limited to) phase-locked neurostimulation and other real-time applications. The endpoint-corrected Hilbert transform (ecHT) reduces boundary artefacts of the Hilbert transform by applying a causal narrow-band filter to the analytic spectrum. This improves the phase estimate at the most recent sample. Despite its widespread empirical use, the systemati...

---

### 46. Audio Outperforms Text for Visual Decoding

**Authors:** Zhengdi Zhang, Hao Zhang, Wenjun Xia

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.13866v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13866v1)

**Summary:** Decoding visual semantic representations from human brain activity is a significant challenge. While recent zero-shot decoding approaches have improved performance by leveraging aligned image-text datasets, they overlook a fundamental aspect of human cognition: semantic understanding is inherently anchored in the auditory modality of speech, not text. To address this, our study introduces the first comparative framework for evaluating auditory versus textual semantic modalities in zero-shot visu...

---

### 47. Learning Discrete Successor Transitions in Continuous Attractor Networks: Emergence, Limits, and Topological Constraints

**Authors:** Daniel Brownell

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.15336v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15336v1)

**Summary:** Continuous attractor networks (CANs) are a well-established class of models for representing low-dimensional continuous variables such as head direction, spatial position, and phase. In canonical spatial domains, transitions along the attractor manifold are driven by continuous displacement signals, such as angular velocity-provided by sensorimotor systems external to the CAN itself. When such signals are not explicitly provided as dedicated displacement inputs, it remains unclear whether attrac...

---

### 48. Explore Brain-Inspired Machine Intelligence for Connecting Dots on Graphs Through Holographic Blueprint of Oscillatory Synchronization

**Authors:** Tingting Dan, Jiaqi Ding, Guorong Wu

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2602.00057v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00057v1)

**Summary:** Neural coupling in both neuroscience and artificial intelligence emerges as dynamic oscillatory patterns that encode abstract concepts. To this end, we hypothesize that a deeper understanding of the neural mechanisms governing brain rhythms can inspire next-generation design principles for machine learning algorithms, leading to improved efficiency and robustness. Building on this idea, we first model evolving brain rhythms through the interference of spontaneously synchronized neural oscillatio...

---

### 49. A First Step for Expansion X-Ray Microscopy: Achieving Contrast in Expanded Tissues Sufficient to Reveal Cell Bodies

**Authors:** Logan Thrasher Collins

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.13370v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13370v1)

**Summary:** Existing methods in nanoscale connectomics are at present too slow to map entire mammalian brains. As an emerging approach, expansion microscopy (ExM) has enormous promise, yet it still suffers from throughput limitations. Mapping the human brain and even mapping nonhuman primate brains therefore remain distant goals. While ExM increases effective resolution linearly, it enlarges tissue volume cubically, which dramatically increases imaging time. As a rapid tomographic technique, X-ray microscop...

---

### 50. Multifaceted neural representation of words in naturalistic language

**Authors:** Xuan Yang, Chuanji Gao, Cheng Xiao, et al.

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.13297v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13297v1)

**Summary:** Understanding how the brain represents the multifaceted properties of words in context is essential for explaining the neural architecture of human language. Here, we combine large-scale psycholinguistic modeling with naturalistic fMRI to uncover the latent structure of word properties and their neural representations during narrative comprehension. By analyzing 106 psycholinguistic variables across 13,850 English words, we identified eight interpretable latent dimensions spanning lexical usage,...

---

## stat.ML

**50 papers**

### 1. Continuous-time reinforcement learning: ellipticity enables model-free value function approximation

**Authors:** Wenlong Mou

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06930v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06930v1)

**Summary:** We study off-policy reinforcement learning for controlling continuous-time Markov diffusion processes with discrete-time observations and actions. We consider model-free algorithms with function approximation that learn value and advantage functions directly from data, without unrealistic structural assumptions on the dynamics.   Leveraging the ellipticity of the diffusions, we establish a new class of Hilbert-space positive definiteness and boundedness properties for the Bellman operators. Base...

---

### 2. Parameter-free Dynamic Regret: Time-varying Movement Costs, Delayed Feedback, and Memory

**Authors:** Emmanuel Esposito, Andrew Jacobsen, Hao Qiu, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06902v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06902v1)

**Summary:** In this paper, we study dynamic regret in unconstrained online convex optimization (OCO) with movement costs. Specifically, we generalize the standard setting by allowing the movement cost coefficients $λ_t$ to vary arbitrarily over time. Our main contribution is a novel algorithm that establishes the first comparator-adaptive dynamic regret bound for this setting, guaranteeing $\widetilde{\mathcal{O}}(\sqrt{(1+P_T)(T+\sum_t λ_t)})$ regret, where $P_T$ is the path length of the comparator sequen...

---

### 3. Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design

**Authors:** Samuel Klein, Willie Neiswanger, Daniel Ratner, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06900v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06900v1)

**Summary:** Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural ...

---

### 4. Sample Complexity of Causal Identification with Temporal Heterogeneity

**Authors:** Ameya Rathod, Sujay Belsare, Salvik Krishna Nautiyal, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06899v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06899v1)

**Summary:** Recovering a unique causal graph from observational data is an ill-posed problem because multiple generating mechanisms can lead to the same observational distribution. This problem becomes solvable only by exploiting specific structural or distributional assumptions. While recent work has separately utilized time-series dynamics or multi-environment heterogeneity to constrain this problem, we integrate both as complementary sources of heterogeneity. This integration yields unified necessary ide...

---

### 5. Vision Transformer Finetuning Benefits from Non-Smooth Components

**Authors:** Ambroise Odonnat, Laetitia Chapel, Romain Tavenard, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06883v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06883v1)

**Summary:** The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, or, in other words, their plasticity. Defined as an average rate of change, it captures the sensitivity to input perturbation; in particular, a high plasticity ...

---

### 6. Learning Deep Hybrid Models with Sharpness-Aware Minimization

**Authors:** Naoya Takeishi

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06837v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06837v1)

**Summary:** Hybrid modeling, the combination of machine learning models and scientific mathematical models, enables flexible and robust data-driven prediction with partial interpretability. However, effectively the scientific models may be ignored in prediction due to the flexibility of the machine learning model, making the idea of hybrid modeling pointless. Typically some regularization is applied to hybrid model learning to avoid such a failure case, but the formulation of the regularizer strongly depend...

---

### 7. Optimal Learning-Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay

**Authors:** Binghui Li, Zilin Wang, Fengling Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06797v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06797v1)

**Summary:** We study optimal learning-rate schedules (LRSs) under the functional scaling law (FSL) framework introduced in Li et al. (2025), which accurately models the loss dynamics of both linear regression and large language model (LLM) pre-training. Within FSL, loss dynamics are governed by two exponents: a source exponent $s>0$ controlling the rate of signal learning, and a capacity exponent $β>1$ determining the rate of noise forgetting. Focusing on a fixed training horizon $N$, we derive the optimal ...

---

### 8. Robust Online Learning

**Authors:** Sajad Ashkezari

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06775v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06775v1)

**Summary:** We study the problem of learning robust classifiers where the classifier will receive a perturbed input. Unlike robust PAC learning studied in prior work, here the clean data and its label are also adversarially chosen. We formulate this setting as an online learning problem and consider both the realizable and agnostic learnability of hypothesis classes. We define a new dimension of classes and show it controls the mistake bounds in the realizable setting and the regret bounds in the agnostic s...

---

### 9. On the Convergence of Multicalibration Gradient Boosting

**Authors:** Daniel Haimovich, Fridolin Linder, Lorenzo Perini, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06773v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06773v1)

**Summary:** Multicalibration gradient boosting has recently emerged as a scalable method that empirically produces approximately multicalibrated predictors and has been deployed at web scale. Despite this empirical success, its convergence properties are not well understood. In this paper, we bridge the gap by providing convergence guarantees for multicalibration gradient boosting in regression with squared-error loss. We show that the magnitude of successive prediction updates decays at $O(1/\sqrt{T})$, wh...

---

### 10. Missing At Random as Covariate Shift: Correcting Bias in Iterative Imputation

**Authors:** Luke Shannon, Song Liu, Katarzyna Reluga

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06713v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06713v1)

**Summary:** Accurate imputation of missing data is critical to downstream machine learning performance. We formulate missing data imputation as a risk minimisation problem, which highlights a covariate shift between the observed and unobserved data distributions. This covariate shift induced bias is not accounted for by popular imputation methods and leads to suboptimal performance. In this paper, we derive theoretically valid importance weights that correct for the induced distributional bias. Furthermore,...

---

### 11. Infinite-dimensional generative diffusions via Doob's h-transform

**Authors:** Thorben Pieper-Sethmacher, Daniel Paulin

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06621v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06621v1)

**Summary:** This paper introduces a rigorous framework for defining generative diffusion models in infinite dimensions via Doob's h-transform. Rather than relying on time reversal of a noising process, a reference diffusion is forced towards the target distribution by an exponential change of measure. Compared to existing methodology, this approach readily generalises to the infinite-dimensional setting, hence offering greater flexibility in the diffusion model. The construction is derived rigorously under ...

---

### 12. Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning

**Authors:** Deqian Kong, Minglu Zhao, Aoyang Qin, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06584v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06584v1)

**Summary:** Standard chain-of-thought reasoning generates a solution in a single forward pass, committing irrevocably to each token and lacking a mechanism to recover from early errors. We introduce Inference-Time Rethinking, a generative framework that enables iterative self-correction by decoupling declarative latent thought vectors from procedural generation. We factorize reasoning into a continuous latent thought vector (what to reason about) and a decoder that verbalizes the trace conditioned on this v...

---

### 13. Efficient Online Variational Estimation via Monte Carlo Sampling

**Authors:** Mathis Chagneux, Mathias Müller, Pierre Gloaguen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06579v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06579v1)

**Summary:** This article addresses online variational estimation in parametric state-space models. We propose a new procedure for efficiently computing the evidence lower bound and its gradient in a streaming-data setting, where observations arrive sequentially. The algorithm allows for the simultaneous training of the model parameters and the distribution of the latent states given the observations. It is based on i.i.d. Monte Carlo sampling, coupled with a well-chosen deep architecture, enabling both comp...

---

### 14. Which Graph Shift Operator? A Spectral Answer to an Empirical Question

**Authors:** Yassine Abbahaddou

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06557v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06557v1)

**Summary:** Graph Neural Networks (GNNs) have established themselves as the leading models for learning on graph-structured data, generally categorized into spatial and spectral approaches. Central to these architectures is the Graph Shift Operator (GSO), a matrix representation of the graph structure used to filter node signals. However, selecting the optimal GSO, whether fixed or learnable, remains largely empirical. In this paper, we introduce a novel alignment gain metric that quantifies the geometric d...

---

### 15. Operationalizing Stein's Method for Online Linear Optimization: CLT-Based Optimal Tradeoffs

**Authors:** Zhiyu Zhang, Aaditya Ramdas

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06545v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06545v1)

**Summary:** Adversarial online linear optimization (OLO) is essentially about making performance tradeoffs with respect to the unknown difficulty of the adversary. In the setting of one-dimensional fixed-time OLO on a bounded domain, it has been observed since Cover (1966) that achievable tradeoffs are governed by probabilistic inequalities, and these descriptive results can be converted into algorithms via dynamic programming, which, however, is not computationally efficient. We address this limitation by ...

---

### 16. Revisiting the Sliced Wasserstein Kernel for persistence diagrams: a Figalli-Gigli approach

**Authors:** Marc Janthial, Théo Lacombe

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06539v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06539v1)

**Summary:** The Sliced Wasserstein Kernel (SWK) for persistence diagrams was introduced in (Carri{è}re et al. 2017) as a powerful tool to implicitly embed persistence diagrams in a Hilbert space with reasonable distortion. This kernel is built on the intuition that the Figalli-Gigli distance-that is the partial matching distance routinely used to compare persistence diagrams-resembles the Wasserstein distance used in the optimal transport literature, and that the later could be sliced to define a positive d...

---

### 17. Sequential Auditing for f-Differential Privacy

**Authors:** Tim Kutta, Martin Dunsche, Yu Wei, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06518v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06518v1)

**Summary:** We present new auditors to assess Differential Privacy (DP) of an algorithm based on output samples. Such empirical auditors are common to check for algorithmic correctness and implementation bugs. Most existing auditors are batch-based or targeted toward the traditional notion of $(\varepsilon,δ)$-DP; typically both. In this work, we shift the focus to the highly expressive privacy concept of $f$-DP, in which the entire privacy behavior is captured by a single tradeoff curve. Our auditors detec...

---

### 18. Envy-Free Allocation of Indivisible Goods via Noisy Queries

**Authors:** Zihan Li, Yan Hao Ling, Jonathan Scarlett, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06361v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06361v1)

**Summary:** We introduce a problem of fairly allocating indivisible goods (items) in which the agents' valuations cannot be observed directly, but instead can only be accessed via noisy queries. In the two-agent setting with Gaussian noise and bounded valuations, we derive upper and lower bounds on the required number of queries for finding an envy-free allocation in terms of the number of items, $m$, and the negative-envy of the optimal allocation, $Δ$. In particular, when $Δ$ is not too small (namely, $Δ\...

---

### 19. High-Dimensional Limit of Stochastic Gradient Flow via Dynamical Mean-Field Theory

**Authors:** Sota Nishiyama, Masaaki Imaizumi

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06320v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06320v1)

**Summary:** Modern machine learning models are typically trained via multi-pass stochastic gradient descent (SGD) with small batch sizes, and understanding their dynamics in high dimensions is of great interest. However, an analytical framework for describing the high-dimensional asymptotic behavior of multi-pass SGD with small batch sizes for nonlinear models is currently missing. In this study, we address this gap by analyzing the high-dimensional dynamics of a stochastic differential equation called a \e...

---

### 20. Time-uniform conformal and PAC prediction

**Authors:** Kayla E. Scharfstein, Arun Kumar Kuchibhotla

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06297v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06297v1)

**Summary:** Given that machine learning algorithms are increasingly being deployed to aid in high stakes decision-making, uncertainty quantification methods that wrap around these black box models such as conformal prediction have received much attention in recent years. In sequential settings, where data are observed/generated in a streaming fashion, traditional conformal methods do not provide any guarantee without fixing the sample size. More importantly, traditional conformal methods cannot cope with se...

---

### 21. Statistical Learning from Attribution Sets

**Authors:** Lorne Applebaum, Robert Busa-Fekete, August Y. Chen, et al.

**Published:** 2026-02-06

🔗 [Paper](http://arxiv.org/abs/2602.06276v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06276v1)

**Summary:** We address the problem of training conversion prediction models in advertising domains under privacy constraints, where direct links between ad clicks and conversions are unavailable. Motivated by privacy-preserving browser APIs and the deprecation of third-party cookies, we study a setting where the learner observes a sequence of clicks and a sequence of conversions, but can only link a conversion to a set of candidate clicks (an attribution set) rather than a unique source. We formalize this a...

---

### 22. Inheritance Between Feedforward and Convolutional Networks via Model Projection

**Authors:** Nicolas Ewen, Jairo Diaz-Rodriguez, Kelly Ramsay

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06245v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06245v1)

**Summary:** Techniques for feedforward networks (FFNs) and convolutional networks (CNNs) are frequently reused across families, but the relationship between the underlying model classes is rarely made explicit. We introduce a unified node-level formalization with tensor-valued activations and show that generalized feedforward networks form a strict subset of generalized convolutional networks. Motivated by the mismatch in per-input parameterization between the two families, we propose model projection, a pa...

---

### 23. Optimal rates for density and mode estimation with expand-and-sparsify representations

**Authors:** Kaushik Sinha, Christopher Tosh

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06175v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06175v1)

**Summary:** Expand-and-sparsify representations are a class of theoretical models that capture sparse representation phenomena observed in the sensory systems of many animals. At a high level, these representations map an input $x \in \mathbb{R}^d$ to a much higher dimension $m \gg d$ via random linear projections before zeroing out all but the $k \ll m$ largest entries. The result is a $k$-sparse vector in $\{0,1\}^m$. We study the suitability of this representation for two fundamental statistical problems...

---

### 24. Latent Structure Emergence in Diffusion Models via Confidence-Based Filtering

**Authors:** Wei Wei, Yizhou Zeng, Kuntian Chen, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06155v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06155v1)

**Summary:** Diffusion models rely on a high-dimensional latent space of initial noise seeds, yet it remains unclear whether this space contains sufficient structure to predict properties of the generated samples, such as their classes. In this work, we investigate the emergence of latent structure through the lens of confidence scores assigned by a pre-trained classifier to generated samples. We show that while the latent space appears largely unstructured when considering all noise realizations, restrictin...

---

### 25. Optimistic Training and Convergence of Q-Learning -- Extended Version

**Authors:** Prashant Mehta, Sean Meyn

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06146v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06146v1)

**Summary:** In recent work it is shown that Q-learning with linear function approximation is stable, in the sense of bounded parameter estimates, under the $(\varepsilon,κ)$-tamed Gibbs policy; $κ$ is inverse temperature, and $\varepsilon>0$ is introduced for additional exploration. Under these assumptions it also follows that there is a solution to the projected Bellman equation (PBE). Left open is uniqueness of the solution, and criteria for convergence outside of the standard tabular or linear MDP settin...

---

### 26. Warm Starts, Cold States: Exploiting Adiabaticity for Variational Ground-States

**Authors:** Ricard Puig, Berta Casas, Alba Cervera-Lierta, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06137v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06137v1)

**Summary:** Reliable preparation of many-body ground states is an essential task in quantum computing, with applications spanning areas from chemistry and materials modeling to quantum optimization and benchmarking. A variety of approaches have been proposed to tackle this problem, including variational methods. However, variational training often struggle to navigate complex energy landscapes, frequently encountering suboptimal local minima or suffering from barren plateaus. In this work, we introduce an i...

---

### 27. Diffusion Model's Generalization Can Be Characterized by Inductive Biases toward a Data-Dependent Ridge Manifold

**Authors:** Ye He, Yitong Qiu, Molei Tao

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06021v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06021v1)

**Summary:** When a diffusion model is not memorizing the training data set, how does it generalize exactly? A quantitative understanding of the distribution it generates would be beneficial to, for example, an assessment of the model's performance for downstream applications. We thus explicitly characterize what diffusion model generates, by proposing a log-density ridge manifold and quantifying how the generated data relate to this manifold as inference dynamics progresses. More precisely, inference underg...

---

### 28. Optimism Stabilizes Thompson Sampling for Adaptive Inference

**Authors:** Shunxing Yan, Han Zhong

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06014v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06014v1)

**Summary:** Thompson sampling (TS) is widely used for stochastic multi-armed bandits, yet its inferential properties under adaptive data collection are subtle. Classical asymptotic theory for sample means can fail because arm-specific sample sizes are random and coupled with the rewards through the action-selection rule. We study this phenomenon in the $K$-armed Gaussian bandit and identify \emph{optimism} as a key mechanism for restoring \emph{stability}, a sufficient condition for valid asymptotic inferen...

---

### 29. Algebraic Robustness Verification of Neural Networks

**Authors:** Yulia Alexandr, Hao Duan, Guido Montúfar

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06105v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06105v1)

**Summary:** We formulate formal robustness verification of neural networks as an algebraic optimization problem. We leverage the Euclidean Distance (ED) degree, which is the generic number of complex critical points of the distance minimization problem to a classifier's decision boundary, as an architecture-dependent measure of the intrinsic complexity of robustness verification. To make this notion operational, we define the associated ED discriminant, which characterizes input points at which the number o...

---

### 30. Causal Inference on Stopped Random Walks in Online Advertising

**Authors:** Jia Yuan Yu

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05997v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05997v1)

**Summary:** We consider a causal inference problem frequently encountered in online advertising systems, where a publisher (e.g., Instagram, TikTok) interacts repeatedly with human users and advertisers by sporadically displaying to each user an advertisement selected through an auction. Each treatment corresponds to a parameter value of the advertising mechanism (e.g., auction reserve-price), and we want to estimate through experiments the corresponding long-term treatment effect (e.g., annual advertising ...

---

### 31. Orthogonal Self-Attention

**Authors:** Leo Zhang, James Martens

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05996v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05996v1)

**Summary:** Softmax Self-Attention (SSA) is a key component of Transformer architectures. However, when utilised within skipless architectures, which aim to improve representation learning, recent work has highlighted the inherent instability of SSA due to inducing rank collapse and poorly-conditioned Jacobians. In this work, we design a novel attention mechanism: Orthogonal Self-Attention (OSA), which aims to bypass these issues with SSA, in order to allow for (non-causal) Transformers without skip connect...

---

### 32. Pragmatic Curiosity: A Hybrid Learning-Optimization Paradigm via Active Inference

**Authors:** Yingke Li, Anjali Parashar, Enlu Zhou, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.06104v1) | 📄 [PDF](https://arxiv.org/pdf/2602.06104v1)

**Summary:** Many engineering and scientific workflows depend on expensive black-box evaluations, requiring decision-making that simultaneously improves performance and reduces uncertainty. Bayesian optimization (BO) and Bayesian experimental design (BED) offer powerful yet largely separate treatments of goal-seeking and information-seeking, providing limited guidance for hybrid settings where learning and optimization are intrinsically coupled. We propose "pragmatic curiosity," a hybrid learning-optimizatio...

---

### 33. Inverse Depth Scaling From Most Layers Being Similar

**Authors:** Yizhou Liu, Sara Kangaslahti, Ziming Liu, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05970v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05970v1)

**Summary:** Neural scaling laws relate loss to model size in large language models (LLMs), yet depth and width may contribute to performance differently, requiring more detailed studies. Here, we quantify how depth affects loss via analysis of LLMs and toy residual networks. We find loss scales inversely proportional to depth in LLMs, probably due to functionally similar layers reducing error through ensemble averaging rather than compositional learning or discretizing smooth dynamics. This regime is ineffi...

---

### 34. Discrete diffusion samplers and bridges: Off-policy algorithms and applications in latent spaces

**Authors:** Arran Carter, Sanghyeok Choi, Kirill Tamogashev, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05961v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05961v1)

**Summary:** Sampling from a distribution $p(x) \propto e^{-\mathcal{E}(x)}$ known up to a normalising constant is an important and challenging problem in statistics. Recent years have seen the rise of a new family of amortised sampling algorithms, commonly referred to as diffusion samplers, that enable fast and efficient sampling from an unnormalised density. Such algorithms have been widely studied for continuous-space sampling tasks; however, their application to problems in discrete space remains largely...

---

### 35. $f$-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment

**Authors:** Rajdeep Haldar, Lantao Mei, Guang Lin, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05946v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05946v1)

**Summary:** Recent research shows that Preference Alignment (PA) objectives act as divergence estimators between aligned (chosen) and unaligned (rejected) response distributions. In this work, we extend this divergence-based perspective to general alignment settings, such as reinforcement learning with verifiable rewards (RLVR), where only environmental rewards are available. Within this unified framework, we propose $f$-Group Relative Policy Optimization ($f$-GRPO), a class of on-policy reinforcement learn...

---

### 36. Transformers Are Born Biased: Structural Inductive Biases at Random Initialization and Their Practical Consequences

**Authors:** Siquan Li, Yao Tong, Haonan Wang, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05927v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05927v1)

**Summary:** Transformers underpin modern large language models (LLMs) and are commonly assumed to be behaviorally unstructured at random initialization, with all meaningful preferences emerging only through large-scale training. We challenge this assumption by showing that randomly initialized transformers already exhibit strong and systematic structural biases. In particular, untrained models display extreme token preferences: across random input sequences, certain tokens are predicted with probabilities o...

---

### 37. Wedge Sampling: Efficient Tensor Completion with Nearly-Linear Sample Complexity

**Authors:** Hengrui Luo, Anna Ma, Ludovic Stephan, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05869v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05869v1)

**Summary:** We introduce Wedge Sampling, a new non-adaptive sampling scheme for low-rank tensor completion. We study recovery of an order-$k$ low-rank tensor of dimension $n \times \cdots \times n$ from a subset of its entries. Unlike the standard uniform entry model (i.e., i.i.d. samples from $[n]^k$), wedge sampling allocates observations to structured length-two patterns (wedges) in an associated bipartite sampling graph. By directly promoting these length-two connections, the sampling design strengthens...

---

### 38. Distribution-free two-sample testing with blurred total variation distance

**Authors:** Rohan Hore, Rina Foygel Barber

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05862v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05862v1)

**Summary:** Two-sample testing, where we aim to determine whether two distributions are equal or not equal based on samples from each one, is challenging if we cannot place assumptions on the properties of the two distributions. In particular, certifying equality of distributions, or even providing a tight upper bound on the total variation (TV) distance between the distributions, is impossible to achieve in a distribution-free regime. In this work, we examine the blurred TV distance, a relaxation of TV dis...

---

### 39. CFRecs: Counterfactual Recommendations on Real Estate User Listing Interaction Graphs

**Authors:** Seyedmasoud Mousavi, Ruomeng Xu, Xiaojing Zhu

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05861v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05861v1)

**Summary:** Graph-structured data is ubiquitous and powerful in representing complex relationships in many online platforms. While graph neural networks (GNNs) are widely used to learn from such data, counterfactual graph learning has emerged as a promising approach to improve model interpretability. Counterfactual explanation research focuses on identifying a counterfactual graph that is similar to the original but leads to different predictions. These explanations optimize two objectives simultaneously: t...

---

### 40. Exact Recovery in the Data Block Model

**Authors:** Amir R. Asadi, Akbar Davoodi, Ramin Javadi, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05852v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05852v1)

**Summary:** Community detection in networks is a fundamental problem in machine learning and statistical inference, with applications in social networks, biological systems, and communication networks. The stochastic block model (SBM) serves as a canonical framework for studying community structure, and exact recovery, identifying the true communities with high probability, is a central theoretical question. While classical results characterize the phase transition for exact recovery based solely on graph c...

---

### 41. Optimal scaling laws in learning hierarchical multi-index models

**Authors:** Leonardo Defilippis, Florent Krzakala, Bruno Loureiro, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05846v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05846v1)

**Summary:** In this work, we provide a sharp theory of scaling laws for two-layer neural networks trained on a class of hierarchical multi-index targets, in a genuinely representation-limited regime. We derive exact information-theoretic scaling laws for subspace recovery and prediction error, revealing how the hierarchical features of the target are sequentially learned through a cascade of phase transitions. We further show that these optimal rates are achieved by a simple, target-agnostic spectral estima...

---

### 42. Principled Confidence Estimation for Deep Computed Tomography

**Authors:** Matteo Gätzner, Johannes Kirschner

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05812v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05812v1)

**Summary:** We present a principled framework for confidence estimation in computed tomography (CT) reconstruction. Based on the sequential likelihood mixing framework (Kirschner et al., 2025), we establish confidence regions with theoretical coverage guarantees for deep-learning-based CT reconstructions. We consider a realistic forward model following the Beer-Lambert law, i.e., a log-linear forward model with Poisson noise, closely reflecting clinical and scientific imaging conditions. The framework is ge...

---

### 43. Non-Stationary Inventory Control with Lead Times

**Authors:** Nele H. Amiri, Sean R. Sinclair, Maximiliano Udenio

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05799v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05799v1)

**Summary:** We study non-stationary single-item, periodic-review inventory control problems in which the demand distribution is unknown and may change over time. We analyze how demand non-stationarity affects learning performance across inventory models, including systems with demand backlogging or lost-sales, both with and without lead times. For each setting, we propose an adaptive online algorithm that optimizes over the class of base-stock policies and establish performance guarantees in terms of dynami...

---

### 44. Learning False Discovery Rate Control via Model-Based Neural Networks

**Authors:** Arnau Vilella, Jasin Machkour, Michael Muma, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05798v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05798v1)

**Summary:** Controlling the false discovery rate (FDR) in high-dimensional variable selection requires balancing rigorous error control with statistical power. Existing methods with provable guarantees are often overly conservative, creating a persistent gap between the realized false discovery proportion (FDP) and the target FDR level. We introduce a learning-augmented enhancement of the T-Rex Selector framework that narrows this gap. Our approach replaces the analytical FDP estimator with a neural network...

---

### 45. Price of universality in vector quantization is at most 0.11 bit

**Authors:** Alina Harbuzova, Or Ordentlich, Yury Polyanskiy

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05790v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05790v1)

**Summary:** Fast computation of a matrix product $W^\top X$ is a workhorse of modern LLMs. To make their deployment more efficient, a popular approach is that of using a low-precision approximation $\widehat W$ in place of true $W$ ("weight-only quantization''). Information theory demonstrates that an optimal algorithm for reducing precision of $W$ depends on the (second order) statistics of $X$ and requires a careful alignment of vector quantization codebook with PCA directions of $X$ (a process known as "...

---

### 46. Selecting Hyperparameters for Tree-Boosting

**Authors:** Floris Jan Koster, Fabio Sigrist

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05786v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05786v1)

**Summary:** Tree-boosting is a widely used machine learning technique for tabular data. However, its out-of-sample accuracy is critically dependent on multiple hyperparameters. In this article, we empirically compare several popular methods for hyperparameter optimization for tree-boosting including random grid search, the tree-structured Parzen estimator (TPE), Gaussian-process-based Bayesian optimization (GP-BO), Hyperband, the sequential model-based algorithm configuration (SMAC) method, and deterministi...

---

### 47. Fast Rates for Nonstationary Weighted Risk Minimization

**Authors:** Tobias Brock, Thomas Nagler

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05742v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05742v1)

**Summary:** Weighted empirical risk minimization is a common approach to prediction under distribution drift. This article studies its out-of-sample prediction error under nonstationarity. We provide a general decomposition of the excess risk into a learning term and an error term associated with distribution drift, and prove oracle inequalities for the learning error under mixing conditions. The learning bound holds uniformly over arbitrary weight classes and accounts for the effective sample size induced ...

---

### 48. Muon in Associative Memory Learning: Training Dynamics and Scaling Laws

**Authors:** Binghui Li, Kaifei Wang, Han Zhong, et al.

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05725v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05725v1)

**Summary:** Muon updates matrix parameters via the matrix sign of the gradient and has shown strong empirical gains, yet its dynamics and scaling behavior remain unclear in theory. We study Muon in a linear associative memory model with softmax retrieval and a hierarchical frequency spectrum over query-answer pairs, with and without label noise. In this setting, we show that Gradient Descent (GD) learns frequency components at highly imbalanced rates, leading to slow convergence bottlenecked by low-frequenc...

---

### 49. Limitations of SGD for Multi-Index Models Beyond Statistical Queries

**Authors:** Daniel Barzilai, Ohad Shamir

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05704v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05704v1)

**Summary:** Understanding the limitations of gradient methods, and stochastic gradient descent (SGD) in particular, is a central challenge in learning theory. To that end, a commonly used tool is the Statistical Queries (SQ) framework, which studies performance limits of algorithms based on noisy interaction with the data. However, it is known that the formal connection between the SQ framework and SGD is tenuous: Existing results typically rely on adversarial or specially-structured gradient noise that doe...

---

### 50. Joint Embedding Variational Bayes

**Authors:** Amin Oji, Paul Fieguth

**Published:** 2026-02-05

🔗 [Paper](http://arxiv.org/abs/2602.05639v1) | 📄 [PDF](https://arxiv.org/pdf/2602.05639v1)

**Summary:** We introduce Variational Joint Embedding (VJE), a framework that synthesizes joint embedding and variational inference to enable self-supervised learning of probabilistic representations in a reconstruction-free, non-contrastive setting. Compared to energy-based predictive objectives that optimize pointwise discrepancies, VJE maximizes a symmetric conditional evidence lower bound (ELBO) for a latent-variable model defined directly on encoder embeddings. We instantiate the conditional likelihood ...

---

