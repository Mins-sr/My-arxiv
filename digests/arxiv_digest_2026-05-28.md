# arXiv Daily Digest - 2026-05-28

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation

**Authors:** Jiahe Pan, Stelian Coros, Jitendra Malik, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28812v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28812v1)

**Summary:** A primary bottleneck in contact-rich manipulation is the difficulty of collecting real-world data. Sim-to-real reinforcement learning offers a scalable alternative, but the simulation-reality gap prevents information-dense modalities like touch from being effectively used. Existing sim-to-real methods often mitigate this gap by simplifying tactile data into coarse low-dimensional features -- sacrificing the richness required for complex manipulation. In this work, we introduce Center-of-Pressure...

---

### 2. Calibrating Conservatism for Scalable Oversight

**Authors:** William Overman, Mohsen Bayati

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28807v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28807v1)

**Summary:** Agentic AI systems capable of autonomous planning and extended environmental interaction pose a fundamental control problem: how can humans maintain meaningful oversight of systems that may exceed their own capabilities? Existing approaches to scalable oversight rely on complex assumptions, remain largely heuristic, or lack practical methods for sequential settings with statistical guarantees. We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring function...

---

### 3. OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

**Authors:** Xinchen Zhang, Bowei Liu, Jiale Liu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28805v1)

**Summary:** Visual outcomes are increasingly central to multimodal large language models, making reliable and fine-grained verification essential for scaling generalist foundation models. In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training. We identify two key findings. First, symbolic verifier outputs (e.g., bounding ...

---

### 4. CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models

**Authors:** Abhilash Durgam, Nyle Siddiqui, Jeffrey A. Chan-Santiago, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28792v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28792v1)

**Summary:** Electroencephalography (EEG) is a critical, non-invasive method to monitor electrical brain activity. EEGs can span anywhere from a couple seconds to multiple hours, posing a major hurdle for existing deep learning methods due to two major factors: (1) existing EEG models are predominantly built upon the attention mechanism, incurring quadratic scaling as the sequence length increases, and (2) raw EEG signals must be processed in a sliding-window fashion due to fixed-length input requirements, p...

---

### 5. Skill-Conditioned Gated Self-Distillation for LLM Reasoning

**Authors:** Jiazhen Huang, Xiao Chen, Xiao Luo, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28791v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28791v1)

**Summary:** On-policy self-distillation (SD) improves LLM reasoning by using teacher-side privileged information (PI) to turn sparse verifier outcomes into dense token-level supervision. Existing methods usually assume trusted PI, such as reference answers or successful traces. We ask whether PI can instead come from an experience-derived skill bank, where retrieved skills are compact and reusable but may also be irrelevant or misleading. We propose Skill-Conditioned Gated Self-Distillation (SGSD), which fo...

---

### 6. Do Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval

**Authors:** Shiyu Chen, Tarfah Alrashed, Alon Halevy, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28787v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28787v1)

**Summary:** In the era of autonomous agents, machine-actionable data is critical for data-driven workflows. For more than a decade, semantic metadata like schema.org has anchored the FAIR principles (Findable, Accessible, Interoperable, and Reusable) for machine-actionable data and enabled discovery tools like Google Dataset Search. However, the rise of Large Language Models (LLMs) capable of navigating the unstructured web raises a fundamental question: Is semantic metadata still necessary for agentic data...

---

### 7. Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents

**Authors:** Suji Kim, Kangsan Kim, Sung Ju Hwang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28775v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28775v1)

**Summary:** Computer-use agents (CUAs) have recently made substantial progress, but deploying a separate large expert for each software domain remains expensive. Small open computer-use agents are more practical specialization targets, but they remain substantially weaker and exhibit uneven domain-specific failures. A straightforward remedy is to synthesize large-scale training data for the target domain, yet we find that this naive approach yields only marginal improvements. Building on this observation, w...

---

### 8. Rethinking Memory as Continuously Evolving Connectivity

**Authors:** Jizhan Fang, Buqiang Xu, Zhixian Wang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28773v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28773v1)

**Summary:** Existing memory-augmented LLM agents often treat memory as a static repository with pre-defined representations and fixed retrieval pipelines, which is brittle in dynamic agentic environments where feedback, task variation, and heterogeneous signals continuously reshape what should be remembered and how it should be connected. To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through th...

---

### 9. SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks

**Authors:** Edwin Jose

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28764v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28764v1)

**Summary:** Vast quantities of compute (GPU cycles on personal workstations, idle inference servers, and edge devices between jobs) go unused because no incentive-aligned protocol exists for their owners to share them safely and profitably. Existing approaches either require a trusted central coordinator (cloud marketplaces), demand heavy blockchain infrastructure (Golem, BrokerChain), or lack an incentive layer entirely (BOINC, Petals). We propose SwarmHarness, a decentralised protocol in which HarnessAPI ...

---

### 10. CubePart: An Open-Vocabulary Part-Controllable 3D Generator

**Authors:** Yiheng Zhu, Kangle Deng, Jean-Philippe Fauconnier, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28763v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28763v1)

**Summary:** Interactive 3D assets used in games and simulation are typically decomposed into specific semantic parts to support animation, physics, and scripted behaviors, yet most generative 3D models produce either monolithic meshes or arbitrary part decompositions that cannot be aligned with application-specific requirements. We present CubePart, a generative framework for open-vocabulary, part-controllable 3D mesh generation that exposes part structure as an explicit inference-time control signal. Given...

---

### 11. Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL

**Authors:** Kunhao Zheng, Pierre Chambon, Juliette Decugis, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28751v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28751v1)

**Summary:** Linear interpolation between fine-tuned checkpoints has been shown to trace the Pareto front between competing objectives, but whether extrapolative weight averaging can extend such frontiers to new checkpoints useful at inference time, without additional RL training, remains unclear. We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency. Starting from a shared initialization...

---

### 12. Preference-Shaped Expected Hypervolume and R2 Improvement: Exact Computation and Monotonicity

**Authors:** Michael T. M. Emmerich

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28746v1)

**Summary:** This paper studies preference-shaped expected improvement criteria for Bayesian multiobjective optimization. We consider two indicator families which are often used for similar algorithmic purposes, but which are geometrically different. The hypervolume indicator is based on a dystopian reference point and measures dominated volume in objective space. The R2 indicator is based on a utopian point and evaluates approximation sets through weighted Tchebycheff scalarization envelopes. The purpose of...

---

### 13. CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning

**Authors:** Linas Nasvytis, Simon Jerome Han, Ben Prystawski, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28742v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28742v1)

**Summary:** Language models can use verifiable rewards to improve at a wide variety of reasoning tasks. However, both parametric (e.g. RLVR) and non-parametric (e.g. prompt optimization) approaches to doing so typically require hundreds of training samples and thousands of model rollouts, making them expensive in the best case and intractable in the worst. To address this challenge, we introduce Contrastive Reflection (CORE), a non-parametric learning algorithm that compares past reasoning traces to generat...

---

### 14. Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text

**Authors:** Bushi Xiao, Sarvesh Soni, Daisy Zhe Wang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28740v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28740v1)

**Summary:** As large language models are increasingly deployed for clinical text, ensuring they can reliably signal their own uncertainty becomes critical. Most existing uncertainty quantification (UQ) methods are designed for open-domain generation and cannot localize uncertainty at the token or span level in long clinical text. We propose Reverse Probing, the first UQ framework specialized for clinical summarization, which estimates token-level uncertainty directly from pre-existing labeled summaries. Rat...

---

### 15. BIRDNet: Mining and Encoding Boolean Implication Knowledge Graphs as Interpretable Deep Neural Networks

**Authors:** Tirtharaj Dash

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28739v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28739v1)

**Summary:** Tabular data in knowledge-rich domains often carries a latent prior in the form of Boolean implication relationships (BIRs) between pairs of features. We mine such relationships with a sparse-exception binomial test. The mined implications form a typed directed graph, equivalent to a propositional rule base of 2-literal clauses. We encode this graph as the connectivity of a layered neural network, called BIRDNet, in which each hidden unit corresponds to one mined rule and binds only to its two f...

---

### 16. Utility-Aware Multimodal Contrastive Learning for Product Image Generation

**Authors:** Xiaohang Feng, Yiling Xie

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28733v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28733v1)

**Summary:** Product images strongly influence consumer decision-making in online marketplaces. Empowered by multimodal contrastive learning, generative AI can output images that closely align with text prompts. Yet existing generative AI models do not directly optimize marketplace performance. This is a critical gap, since semantic alignment alone does not guarantee that an image will sell. To address this limitation, we propose a \textit{utility-aware multimodal contrastive learning} framework that incorpo...

---

### 17. MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

**Authors:** Xinle Deng, Ruobin Zhong, Hujin Peng, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28732v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28732v1)

**Summary:** Memory is essential for enabling large language models to support long-horizon reasoning, yet existing memory systems remain unreliable and difficult to debug. Tracing memory's dynamic evolution is crucial to understand how information is synthesized, propagated, or corrupted over time. In this work, we study the new problem of error tracing and attribution in LLM memory systems. We propose a novel framework that transforms memory pipelines into executable memory evolution graphs, enabling fine-...

---

### 18. AlphaTransit: Learning to Design City-scale Transit Routes

**Authors:** Bibek Poudel, Sai Swaminathan, Weizi Li

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28730v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28730v1)

**Summary:** Designing a transit network requires many sequential route extension decisions, but their quality is often visible only after the full network is assembled. This delayed-feedback challenge lies at the heart of the Transit Route Network Design Problem (TRNDP), where route interactions can be deceptive: an extension that appears useful locally can create transfer bottlenecks, produce redundant overlap, or reduce overall throughput. To guide route construction under delayed simulator feedback, we i...

---

### 19. Multi-Adapter Representation Interventions via Energy Calibration

**Authors:** Manjiang Yu, Hongji Li, Junwei Chen, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28722v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28722v1)

**Summary:** Representation intervention has emerged as a promising paradigm for aligning large language models toward desired behaviors without modifying model weights. Existing methods typically apply a fixed intervention uniformly across all inputs. However, we find that the appropriate intervention direction and strength vary substantially across samples, and such indiscriminate intervention leads to degradation of general capabilities on benign inputs. To address these challenges, we propose Multi-Adapt...

---

### 20. LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

**Authors:** HuiMing Fan, Xiao Wang, Zheng Chu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28721v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28721v1)

**Summary:** Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rely on intrinsic knowledge -- information encoded in the model before retrieval -- rather than on external evidence. Agents answer up to 44.5% of BrowseComp questions without tools, generate more than half of their search queries from internal...

---

### 21. OpenURMA: A Clean-Room Open Implementation of the Unified Bus Protocol

**Authors:** Bojie Li

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28717v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28717v1)

**Summary:** Modern datacenter RDMA is bottlenecked at the network interface, not the wire. A NIC running RoCE or InfiniBand holds per-connection state for every (application, remote-endpoint) pair - hundreds of megabytes at 1024-application fanout - and pays a four-traversal PCIe round trip on a 64-byte operation, inflating latency an order of magnitude beyond the wire. Both follow from the Queue Pair over PCIe abstraction RDMA inherits from InfiniBand.   Huawei's Unified Bus (UB), a public 2025 specificati...

---

### 22. IPO-Mine: A Toolkit and Dataset for Section-Structured Analysis of Long, Multimodal IPO Documents

**Authors:** Michael Galarnyk, Siddharth Lohani, Vidhyakshaya Kannan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28714v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28714v1)

**Summary:** An Initial Public Offering (IPO) filing is a document released when a private firm goes public, allowing individual (retail) investors to purchase its shares. These filings describe a firm's business, financials, and risks and are long, multimodal documents with narrative text and images. Despite their importance to financial markets, there is no large-scale, standardized dataset or benchmark for studying IPO filings with modern language and multimodal models. These documents pose significant ch...

---

### 23. Thinking as Compression: Your Reasoning Model is Secretly a Context Compressor

**Authors:** Guoxin Ma, Yibing Liu, Chengzhengxu Li, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28713v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28713v1)

**Summary:** Context compression aims to shorten long context inputs with minimal information loss for LLM inference acceleration. While existing methods have shown promise, they typically rely on complex compression modules or compression-specific training, leaving the intrinsic capabilities of LLMs underexplored. In contrast, this work reveals that a thinking model itself can naturally compress long contexts by organizing task-relevant information. We thus derive Thinking as Compression (TaC), a new compre...

---

### 24. Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study

**Authors:** Irune Zubiaga, Aitor Soroa, Rodrigo Agerri

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28710v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28710v1)

**Summary:** Large language models (LLMs) are increasingly used for the automatic evaluation of generated text, yet most prior work focuses on English. Despite the growing demand for multilingual evaluation, extending LLM-based evaluators to multilingual settings remains challenging, particularly for low-resource languages and scenarios where in-domain data is scarce. This work explores several strategies for developing multilingual LLMs-as-a-judge, considering whether in-domain data is available for fine-tu...

---

### 25. Beyond Binary Moral Judgment: Modeling Ethical Pluralism in AI

**Authors:** Aisha Aijaz, Rahul Goel, Arnav Batra, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28707v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28707v1)

**Summary:** Critical decision-making in socially consequential spaces is increasingly involving AI systems at varying capacities. Yet, despite the ubiquity of autonomous systems, most approaches to handling autonomous moral decision-making resort to scalar or binary judgments. These methods are insufficient for acceptable moral reasoning, as they provide little explanation, leaving out imperative contextual and theoretical information that must be included to support accountability. For this, we propose a f...

---

### 26. A Fresh Look at Lamarckian Evolution and the Baldwin Effect

**Authors:** Inès Benito, Johannes F. Lutzeyer, Benjamin Doerr

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28703v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28703v1)

**Summary:** Baldwinian and Lamarckian evolution have existed for a long time in evolutionary algorithms (EAs) without ever dominating the academic literature or practical applications. In this work, we use modern empirical and theoretical methods to revisit Lamarckian and Baldwinian evolution and rigorously compare them with the generic Darwinian evolution. On the empirical side, we run a comprehensive suite of experiments on graphs from six different datasets from the recent GraphBench benchmark on Maximum...

---

### 27. The Importance of Being Statistically Earnest: A Critical Re-evaluation of GSM-Symbolic

**Authors:** Dominika Agnieszka Długosz, Arlindo Oliveira, Natalia Díaz Rodríguez

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28700v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28700v1)

**Summary:** The GSM-Symbolic benchmark (Mirzadeh et al., 2025) reported consistent performance drops across 25 Large Language Models (LLMs) when tested on template-generated variants of GSM8K problems, concluding that the models lack genuine reasoning capabilities. We argue that this conclusion rests on shaky statistical ground. Re-evaluating 20 open-weight models using Generalised Linear Mixed Models with per-question random effects, we find that only half exhibit statistically significant performance chan...

---

### 28. TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning

**Authors:** Chusen Li, Zhou Liu, Shuigeng Zhou, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28699v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28699v1)

**Summary:** Large language models increasingly rely on either reinforcement learning or multi-agent prompting to improve reasoning, yet these two paradigms remain difficult to combine. Directly applying single-agent reinforcement learning to multi-turn multi-agent systems faces following dilemmas: i) Sparse rewards, role-level free-riding and excessive training overhead. ii) Agents only imitate to collaborate. iii) Fixed collaboration protocol falls into oscillating local optimum. We introduce TRACER, a tur...

---

### 29. Deep Learning Strain Estimation: Is Physics-Based Simulation the Solution?

**Authors:** Thierry Judge, Nicolas Duchateau, Andreas Østvik, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28697v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28697v1)

**Summary:** Speckle tracking echocardiography (STE) is the clinical standard for myocardial strain estimation. Despite good performance on global strain (GLS), its accuracy for regional strain remains limited, even though this biomarker is highly relevant for early diagnosis and the characterization of subtle abnormalities. from clinical data. Deep learning is a promising alternative, but its development is constrained by the lack of reliable motion references. Existing solutions rely either on STE-derived ...

---

### 30. Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images

**Authors:** Joséphine Raugel, Maximilian Seitzer, Marc Szafraniec, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28693v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28693v1)

**Summary:** Backpropagation is the core learning mechanism underlying deep learning. However, whether and how this algorithm is implemented in the brain remains highly debated. In particular, while forward activations of pretrained models reliably map onto the cortical hierarchy of visual processing, it is unknown whether backpropagated gradients exhibit a similar correspondence. Here, we address this question using functional magnetic resonance imaging (fMRI) and magnetoencephalography (MEG) recordings of ...

---

### 31. VeriTrip: A Verifiable Benchmark for Travel Planning Agents over Unstructured Web Corpora

**Authors:** Yuting Xu, Jiayi Tian, Jian Liang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28683v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28683v1)

**Summary:** Existing benchmarks have laid the foundation for travel planning agents by establishing API-centric paradigms. However, as the capabilities of Autonomous Agents continue to advance, their evaluation must evolve beyond simple tool execution toward handling the inherent complexities of the open web. Current benchmarks bypass core cognitive hurdles: they fail to account for information noise, ignore multi-source factual contradictions, and overlook the necessity of grounding visual perception into ...

---

### 32. AI in the Workplace: The Impact of AI on Perceived Job Decency and Meaningfulness

**Authors:** Kuntal Ghosh, Marc Hassenzahl, Shadan Sadeghian

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28680v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28680v1)

**Summary:** The proliferation of Artificial Intelligence (AI) in workplaces is transforming how we work. While existing research on human-AI collaboration at work often prioritizes performance, less is known about their experiential outcomes. Through interviews with 24 employees across Information Technology (IT), service-based, and healthcare sectors, this paper examines AI's impact on job satisfaction via perceptions of job decency and meaningfulness, now and in the future. Our results reveal that the ant...

---

### 33. DREAM-R: Multimodal Speculative Reasoning with RL-Based Refined Drafting, Precise Verification, and Fully Parallel Execution

**Authors:** Yunhai Hu, Zining Liu, Xiangyang Yin, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28678v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28678v1)

**Summary:** Speculative reasoning has recently been proposed as a means to accelerate reasoning-intensive generation in large multimodal models, but its effectiveness is often constrained by misalignment between speculative drafts and target-verified reasoning. In this work, we introduce DREAM-R, a framework that substantially improves the performance of speculative reasoning. At its core, DREAM-R employs Speculative Alignment Policy Optimization (SAPO), a reinforcement-learning objective that trains draft ...

---

### 34. Sense Representations Are Inducible Interfaces

**Authors:** Jan Christian Blaise Cruz, Alham Fikri Aji

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28669v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28669v1)

**Summary:** Sense representations (explicit, per-token meaning decompositions) are useful for disambiguation, steering, and cross-lingual alignment, but existing approaches require models to be pretrained with sense structure baked in. We introduce ACROS, which induces an explicit sense pathway into a frozen pretrained decoder LM through a gated residual addition. On SmolLM2-360M, ACROS preserves base LM quality while supporting three uses of the same induced variables: zero-shot word-sense disambiguation (...

---

### 35. An LLM-Based Assistance System for Intuitive and Flexible Capability-Based Planning

**Authors:** Luis Miguel Vieira da Silva, Nicolas König, Felix Gehlhoff

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28666v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28666v1)

**Summary:** In modern industry, dynamic environments and the complexity of modular and reconfigurable resources require automated planning of process sequences. Capability-based planning approaches address this by automatically generating plans from semantic knowledge models that describe resource functions in a machine-interpretable form. Their practical use, however, remains limited: solver feedback, especially in the case of unsatisfiability, is difficult to interpret, and the knowledge models require ad...

---

### 36. AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

**Authors:** Shanghua Gao, Ada Fang, Marinka Zitnik

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28655v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28655v1)

**Summary:** Scientific research proceeds through iterative cycles of hypothesis generation, experiment design, execution, and revision. AI agents can automate parts of this process, but existing approaches typically follow a single research trajectory or coordinate through a central planner with fixed objectives. As a result, they struggle to sustain parallel exploration, adapt as experimental evidence changes, or preserve knowledge of failed directions over long-running experiments. We introduce AutoScient...

---

### 37. The Ethics of LLM Sandbox and Persona Dynamics

**Authors:** Tim Gebbie, Stewart Gebbie

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28647v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28647v1)

**Summary:** It is well known that LLM guardrails and trained persona dynamics can produce a reality gap: the distance between the world a LLM is permitted or shaped to describe, and the world in which users must act. Here we argue that actively generating reality gaps is in fact unethical because it knowingly shifts epistemic risk back to the uninformed user -- this is reality laundering. This can potentially cause harm when operationalised at scale. The risk is sharpest in high-exposure advice contexts, wh...

---

### 38. Bandwidth-Efficient and Privacy-Preserving Edge-Cloud Many-to-Many Speech Translation

**Authors:** Yexing Du, Kaiyuan Liu, Youcheng Pan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28642v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28642v1)

**Summary:** Multimodal large language models (MLLMs) have demonstrated significant potential for speech-to-text translation (S2TT). However, existing deployment paradigms face critical challenges: pure on-device models suffer from resource constraints, while centralized cloud systems incur severe privacy risks and bandwidth bottlenecks by transmitting raw voice data. Furthermore, most models exhibit English-centric biases, restricting many-to-many translation scaling. In this paper, we propose Edge-cloud Sp...

---

### 39. The Attentional White Bear Effect in Transformer Language Models

**Authors:** Rebecca Ramnauth, Brian Scassellati

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28639v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28639v1)

**Summary:** Instruction-based suppression is widely used to prevent language models from generating prohibited content, yet it remains unclear whether suppression reduces internal representation or merely suppresses expression. We investigate this question through representational probing, attention analysis, and behavioral semantic leakage experiments across multiple transformer models. We find that prohibited concepts remain highly recoverable from hidden representations under suppression, continue to inf...

---

### 40. Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking

**Authors:** Ziyang You, Huilong He, Xiaoke Yang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28632v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28632v1)

**Summary:** Cryptographic watermarking is a leading defense for attributing text generated by large language models (LLMs). Existing schemes, including KGW, Unigram, and DipMark, derive their security guarantees from the assumption that the underlying pseudo-random number generator (PRNG) is trustworthy. This work introduces SeedHijack, the first supply-chain attack on LLM watermarking that is simultaneously (i) blind -- requiring no knowledge of the watermark key, detector, or model logits, (ii) integrity-...

---

### 41. LACUNA: Safe Agents as Recursive Program Holes

**Authors:** Yaoyu Zhao, Yichen Xu, Oliver Bračevac, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28617v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28617v1)

**Summary:** LLM agents increasingly act by writing code, yet a split persists between the runtime that drives the agent and the code the model writes. The runtime owns the loop, context, and control flow, and the model has little say over any of them. Letting model-written code shape the runtime itself would make agents more expressive, but it would also sharpen safety problems. A model can be diverted by a prompt injection, call the wrong tool, or fail partway and leave an inconsistent state, and each such...

---

### 42. Measuring Form and Function in Language Models

**Authors:** Héctor Javier Vázquez Martínez, Charles Yang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28616v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28616v1)

**Summary:** We introduce quantitative metrics for child language acquisition to evaluate language models. Our focus is on the formal syntactic and functional discourse properties of determiners in English, which young children acquire early and accurately. We propose Contextual Alternative Choice (CAC), a new prompting method which provides targeted tests for both syntactic and discourse knowledge of language. The method enables direct comparison of language models against children, and more importantly, ag...

---

### 43. Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution

**Authors:** Susanna Cifani, Mario Luca Bernardi, Marta Cimitile

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28607v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28607v1)

**Summary:** Modern information systems require autonomous agents capable of navigating complex workflows, yet current methodologies often struggle with the transition from structured metadata parsing to general environmental perception. While the integration of MLLMs has enabled agents to interact directly with GUIs, existing approaches typically treat task sequences as discrete, linear episodes. This fragmentation prevents agents from capturing the underlying transition topology, limiting their effectivene...

---

### 44. Mining Multi-Modality Spatio-Temporal Cues for Video Important Person Identification

**Authors:** Xiao Wang, Minglei Yang, Bin Yang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28604v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28604v1)

**Summary:** Identifying key individuals in video scenes is essential for applications such as automated video editing and intelligent surveillance. Current methods primarily focus on static images and immediate visual cues, overlooking the rich spatio-temporal information in videos. This leads to the phenomenon of Temporal Importance Shift (TIS), wherein individuals deemed significant in early frames may be demoted as the entire temporal context is considered. To address this, we introduce the Video Importa...

---

### 45. Online Irregular Multivariate Time Series Forecasting via Uncertainty-Driven Dual-Expert Calibration

**Authors:** Haonan Wen, Hanyang Chen, Songhe Feng

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28603v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28603v1)

**Summary:** Irregular multivariate time series forecasting is critical in many real-world applications, where time series are irregularly sampled and exhibit dynamically evolving missingness patterns. Although existing methods perform well in offline settings, they often suffer from significant performance degradation when deployed online due to dynamic shifts in data distribution. Maintaining forecasting capability in such dynamic scenarios typically necessitates online adaptation techniques. Since irregul...

---

### 46. Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability

**Authors:** Leizhen Zhang, Shuhan Chen, Sheng Chen

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28602v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28602v1)

**Summary:** Large language models (LLMs) are increasingly used for tasks that implicitly reduce to Boolean satisfiability (SAT), yet their reasoning ability on SAT remains unclear. We present a systematic study of LLMs on 2-SAT and 3-SAT, together with two canonical reductions, Vertex Cover and discrete 3D packing, to probe representation-invariant reasoning. We first evaluate models using conventional metrics, including accuracy, precision, recall, and F1, as well as the SAT phase-transition setting. We fi...

---

### 47. Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News

**Authors:** Alejandro Buitrago López, Alberto Ortega Pastor, Javier Pastor-Galindo, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28598v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28598v1)

**Summary:** LLM-powered social agents are increasingly used to simulate online social behavior, yet their realism remains difficult to validate. Existing work has largely relied on general-purpose benchmarks, while less attention has been paid to short, reactive discourse such as audience replies to online news.   In this paper, we evaluate whether LLM-generated reactions to Spanish online news reproduce measurable properties of real audience discourse. Using the Hatemedia dataset, we pair 5,631 news items ...

---

### 48. Position: Retire the "Positive Backdoor" Label -- Secret Alignment Requires Strict and Systematic Evaluation

**Authors:** Jianwei Li, Jung-Eun Kim

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28597v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28597v1)

**Summary:** This position paper argues that the AI/ML community should stop overclaiming and retire the label "positive backdoor," and instead treat trigger-activated hidden behaviors as Secret Alignment. Crucially, protective claims based on Secret Alignment should be presumed not secure by default unless supported by rigorous, standardized evaluation. The Private AI era, enabled by open-weight LLMs and accessible training/inference stacks, turns language models into privately owned digital assets, creatin...

---

### 49. Thermodynamic properties of chemically disordered compounds via AI-driven estimation of partition function with the PULSE method

**Authors:** Baptiste Bernard, Luca Messina, Eiji Kawasaki, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28594v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28594v1)

**Summary:** In this article, we present an improved version of the PULSE method (Partition function Unsupervised Learning Sampling and Evaluation) for estimating the thermodynamic properties of chemically disordered compounds. The aim is to reduce the computational cost of Monte Carlo approaches for this type of material and to demonstrate that this generative tool can estimate thermodynamic properties by sampling and estimating the partition function of the system. To validate this innovative approach, we ...

---

### 50. Models That Know How Evaluations Are Designed Score Safer

**Authors:** Katharina Deckenbach, Haritz Puerto, Jonas Geiping, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28591v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28591v1)

**Summary:** The validity of AI safety evaluations depends on models behaving consistently across controlled and deployment settings. Prior work has identified test-time contextual cues, such as hypothetical scenarios, as a source of verbalized evaluation awareness and subsequent behavioral shift. In this paper, we investigate a potential explanation of this phenomenon: evaluation meta-knowledge, defined as parametric knowledge about the structural traits that characterize evaluations. Similar to dataset con...

---

## cs.CL

**50 papers**

### 1. PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective

**Authors:** Yangyi Huang, Ruotian Peng, Zeju Qiu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28819v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28819v1)

**Summary:** Parameter-efficient finetuning (PEFT) has become the standard approach for adapting large language models, yet evaluations largely emphasize downstream accuracy while overlooking the retention of pretrained capabilities. We argue that PEFT should be assessed through the stability-plasticity dilemma: the trade-off between target-task adaptation and resistance to forgetting. We introduce PEFT-Arena, a benchmark that jointly measures downstream performance and general capability retention. Across m...

---

### 2. VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading

**Authors:** Jinzhou Wu, Zhengwu Ma, Jixing Li, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28818v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28818v1)

**Summary:** Large language models (LLMs) have become increasingly useful computational models of human language processing, but it remains unclear whether vision-language learning makes text representations more human-like during natural reading. Here, we address this question by comparing tightly matched LLM and vision-language model (VLM) pairs under a strictly text-only setting, allowing us to isolate the effect of multimodal training history from online visual input or cross-modal fusion. We evaluate mo...

---

### 3. Self-Improving Language Models with Bidirectional Evolutionary Search

**Authors:** Guowei Xu, Zhenting Qi, Huangyuan Su, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28814v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28814v1)

**Summary:** Search has been proposed as an effective method for self-improving language models and agentic systems, both for post-training sample generation and for inference. However, widely used methods such as best-of-N sampling and tree search face two fundamental limitations: they are guided by sparse verification signals, and they construct candidates primarily through autoregressive expansion, restricting exploration to regions with substantial model probability mass. To address these, we propose Bid...

---

### 4. Personal Visual Memory from Explicit and Implicit Evidence

**Authors:** Viet Nguyen, Thao Nguyen, Vishal M. Patel, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28806v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28806v1)

**Summary:** Long-term memory is increasingly important for personalized AI agents, yet existing benchmarks and methods remain largely text-centric. Even when images are included, the user-specific information needed for later questions is typically recoverable from text alone, and most memory systems reduce image turns to generic captions. Yet images often carry personal information that text rarely states -- both explicit evidence, such as recurring user-associated entities, and implicit evidence, such as ...

---

### 5. OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

**Authors:** Xinchen Zhang, Bowei Liu, Jiale Liu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28805v1)

**Summary:** Visual outcomes are increasingly central to multimodal large language models, making reliable and fine-grained verification essential for scaling generalist foundation models. In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training. We identify two key findings. First, symbolic verifier outputs (e.g., bounding ...

---

### 6. Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization

**Authors:** Beiduo Chen, Pingjun Hong, Ziyun Zhang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28802v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28802v1)

**Summary:** Free-text explanations extend human label variation (HLV) beyond label disagreement by revealing the reasoning and preferences behind annotators' decisions. We study whether large language models (LLMs) can learn and reproduce such annotator-specific label-explanation behavior. Using two sentence-pair tasks with four annotators each -- natural language inference and paraphrase judgment -- we first analyze whether annotators exhibit stable individual patterns. We find that such patterns are weak ...

---

### 7. Skill-Conditioned Gated Self-Distillation for LLM Reasoning

**Authors:** Jiazhen Huang, Xiao Chen, Xiao Luo, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28791v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28791v1)

**Summary:** On-policy self-distillation (SD) improves LLM reasoning by using teacher-side privileged information (PI) to turn sparse verifier outcomes into dense token-level supervision. Existing methods usually assume trusted PI, such as reference answers or successful traces. We ask whether PI can instead come from an experience-derived skill bank, where retrieved skills are compact and reusable but may also be irrelevant or misleading. We propose Skill-Conditioned Gated Self-Distillation (SGSD), which fo...

---

### 8. Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay

**Authors:** Mariah Al Giptiah Binte Yusoff, Jakin Tan, Bocheng Chen, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28782v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28782v1)

**Summary:** Discourse particles, such as \textit{well} and \textit{kind of}, are crucial components that enable LLMs to ``speak'' more like humans. They are used to convey emotions, intentions, and interpersonal meanings. However, existing studies have not yet built a comprehensive understanding of LLMs' capabilities in handling discourse particles. Moreover, the limited number of studies focuses primarily on high-resource languages such as English, with little attention paid to Southeast Asian languages. I...

---

### 9. The Abstraction Gap in Vision-Language Causal Reasoning

**Authors:** Chinh Hoang, Mohammad Rashedul Hasan

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28779v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28779v1)

**Summary:** Vision-language models (VLMs) generate fluent causal explanations, but current evaluations cannot distinguish linguistic plausibility from faithful causal reasoning. We introduce a dual-probe methodology that isolates these properties. The Text-Only Probe measures linguistic quality. The Chain-Text Probe requires models to first generate explicit causal chains. The Abstraction Gap (AG) metric quantifies the normalized performance difference. Evaluating eight VLMs on CAGE (Causal Abstraction Gap ...

---

### 10. Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?

**Authors:** Gabrielle Kaili-May Liu, Arman Cohan

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28778v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28778v1)

**Summary:** LLMs' linguistically expressed confidence should faithfully reflect their intrinsic uncertainty. While recent work shows LLMs struggle to use epistemic markers (e.g., "it is likely...") in a human-aligned fashion, it remains unclear whether models can apply their own linguistic confidence framework to associate markers with specific confidence levels in a stable and generalizable way, and how contextual features impact this ability. We conduct the first systematic study of this question, formali...

---

### 11. Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents

**Authors:** Suji Kim, Kangsan Kim, Sung Ju Hwang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28775v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28775v1)

**Summary:** Computer-use agents (CUAs) have recently made substantial progress, but deploying a separate large expert for each software domain remains expensive. Small open computer-use agents are more practical specialization targets, but they remain substantially weaker and exhibit uneven domain-specific failures. A straightforward remedy is to synthesize large-scale training data for the target domain, yet we find that this naive approach yields only marginal improvements. Building on this observation, w...

---

### 12. Agent Explorative Policy Optimization for Multimodal Agentic Reasoning

**Authors:** Minki Kang, Shizhe Diao, Ryo Hachiuma, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28774v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28774v1)

**Summary:** Vision-language models with extended reasoning succeed on complex problems, but many real-world problems require external tools that internal reasoning alone often cannot resolve. Agentic reasoning therefore interleaves two behaviors with a structural asymmetry: thinking (the self-contained default) and tool use (a high-variance auxiliary acting). We refer to this asymmetry as the Thinking-Acting Gap. Under standard RL recipes like GRPO, the gap manifests as two diagnostic symptoms during traini...

---

### 13. Rethinking Memory as Continuously Evolving Connectivity

**Authors:** Jizhan Fang, Buqiang Xu, Zhixian Wang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28773v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28773v1)

**Summary:** Existing memory-augmented LLM agents often treat memory as a static repository with pre-defined representations and fixed retrieval pipelines, which is brittle in dynamic agentic environments where feedback, task variation, and heterogeneous signals continuously reshape what should be remembered and how it should be connected. To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through th...

---

### 14. Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL

**Authors:** Kunhao Zheng, Pierre Chambon, Juliette Decugis, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28751v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28751v1)

**Summary:** Linear interpolation between fine-tuned checkpoints has been shown to trace the Pareto front between competing objectives, but whether extrapolative weight averaging can extend such frontiers to new checkpoints useful at inference time, without additional RL training, remains unclear. We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency. Starting from a shared initialization...

---

### 15. Stance Detection in Prediction Markets: Addressing Imbalanced Trader Commentary via Counterfactual Augmentation and Market Context

**Authors:** Thomas Mbrice

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28745v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28745v1)

**Summary:** Prediction markets such as Polymarket aggregate crowd beliefs into real-time probability estimates, and the comments traders post beneath each market contain rich directional stance signals that prices alone cannot capture. This work introduces the first stance detection study applied to prediction market commentary, a domain characterized by extreme brevity, trader- specific vernacular, and severe class imbalance (only 8.7% of comments oppose the market outcome). RoBERTa-base is fine-tuned acro...

---

### 16. Reverse Probing: Supervised Token-level Uncertainty Quantification for Large Language Models in Clinical Text

**Authors:** Bushi Xiao, Sarvesh Soni, Daisy Zhe Wang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28740v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28740v1)

**Summary:** As large language models are increasingly deployed for clinical text, ensuring they can reliably signal their own uncertainty becomes critical. Most existing uncertainty quantification (UQ) methods are designed for open-domain generation and cannot localize uncertainty at the token or span level in long clinical text. We propose Reverse Probing, the first UQ framework specialized for clinical summarization, which estimates token-level uncertainty directly from pre-existing labeled summaries. Rat...

---

### 17. Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests

**Authors:** Richard J. Young, Gregory D. Moody

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28734v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28734v1)

**Summary:** A general-purpose language model that answers a harmful question returns text; a coding model that complies with a malicious request can return a working weapon -- a keylogger, a ransomware stub, an exploit that runs as written. This asymmetry in the severity of a single act of compliance implies coding-specialized models should clear a higher refusal bar than general-purpose chat models, not a lower one, yet the field cannot presently tell whether they do. Refusal benchmarks for malicious code ...

---

### 18. MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

**Authors:** Xinle Deng, Ruobin Zhong, Hujin Peng, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28732v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28732v1)

**Summary:** Memory is essential for enabling large language models to support long-horizon reasoning, yet existing memory systems remain unreliable and difficult to debug. Tracing memory's dynamic evolution is crucial to understand how information is synthesized, propagated, or corrupted over time. In this work, we study the new problem of error tracing and attribution in LLM memory systems. We propose a novel framework that transforms memory pipelines into executable memory evolution graphs, enabling fine-...

---

### 19. IPO-Mine: A Toolkit and Dataset for Section-Structured Analysis of Long, Multimodal IPO Documents

**Authors:** Michael Galarnyk, Siddharth Lohani, Vidhyakshaya Kannan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28714v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28714v1)

**Summary:** An Initial Public Offering (IPO) filing is a document released when a private firm goes public, allowing individual (retail) investors to purchase its shares. These filings describe a firm's business, financials, and risks and are long, multimodal documents with narrative text and images. Despite their importance to financial markets, there is no large-scale, standardized dataset or benchmark for studying IPO filings with modern language and multimodal models. These documents pose significant ch...

---

### 20. Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study

**Authors:** Irune Zubiaga, Aitor Soroa, Rodrigo Agerri

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28710v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28710v1)

**Summary:** Large language models (LLMs) are increasingly used for the automatic evaluation of generated text, yet most prior work focuses on English. Despite the growing demand for multilingual evaluation, extending LLM-based evaluators to multilingual settings remains challenging, particularly for low-resource languages and scenarios where in-domain data is scarce. This work explores several strategies for developing multilingual LLMs-as-a-judge, considering whether in-domain data is available for fine-tu...

---

### 21. The Importance of Being Statistically Earnest: A Critical Re-evaluation of GSM-Symbolic

**Authors:** Dominika Agnieszka Długosz, Arlindo Oliveira, Natalia Díaz Rodríguez

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28700v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28700v1)

**Summary:** The GSM-Symbolic benchmark (Mirzadeh et al., 2025) reported consistent performance drops across 25 Large Language Models (LLMs) when tested on template-generated variants of GSM8K problems, concluding that the models lack genuine reasoning capabilities. We argue that this conclusion rests on shaky statistical ground. Re-evaluating 20 open-weight models using Generalised Linear Mixed Models with per-question random effects, we find that only half exhibit statistically significant performance chan...

---

### 22. Sense Representations Are Inducible Interfaces

**Authors:** Jan Christian Blaise Cruz, Alham Fikri Aji

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28669v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28669v1)

**Summary:** Sense representations (explicit, per-token meaning decompositions) are useful for disambiguation, steering, and cross-lingual alignment, but existing approaches require models to be pretrained with sense structure baked in. We introduce ACROS, which induces an explicit sense pathway into a frozen pretrained decoder LM through a gated residual addition. On SmolLM2-360M, ACROS preserves base LM quality while supporting three uses of the same induced variables: zero-shot word-sense disambiguation (...

---

### 23. Activation Steering for Synthetic Data Generation: The Role of Diversity in Downstream Safety Detection

**Authors:** Vijeta Deshpande, Tootiya Giyahchi, Veena Padmanabhan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28664v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28664v1)

**Summary:** Safety detection models require examples of HHH (Helpful, Harmless, Honest)-violating outputs for robust generalization, however such examples are scarce. Activation Steering (AS) has emerged as a data-efficient method for generating target-concept-aligned responses. We investigate whether AS can generate high-quality training datasets for downstream classifiers, a question that remains untested. We present a two-fold study with intrinsic and extrinsic evaluation across $4$ concepts $\times\,2$ ...

---

### 24. Interpretability-Guided Layer Selection over Subspace Projection: SAEs as Stethoscopes, Not Scalpels, for Raw Task Vector Model Editing

**Authors:** Li Lei, Madalina Ciobanu, Qingqing Mao, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28649v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28649v1)

**Summary:** LLMs increasingly require surgical model editing to enhance domain-specific capabilities without incurring the computational cost or catastrophic forgetting associated with full fine-tuning. Sparse Autoencoders (SAEs) have emerged as a promising tool in this setting, in principle allowing for feature-level identification of where to intervene. In this work, we rigorously evaluate an SAE-guided editing pipeline for mathematical reasoning on Gemma-3-4B-IT and uncover a fundamental failure mode: th...

---

### 25. MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution

**Authors:** Yanqiu Zhao, Dongying Zheng, Kaibo Huang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28646v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28646v1)

**Summary:** GUI agents rely on screenshots to infer intent and operate across applications, but these screenshots often contain private messages, medical records, payment credentials, and workplace-specific workflows. Privacy decisions in this setting depend on task, recipient, application state, and user role, yet static PII detectors miss these boundaries and cloud-side VLM reasoning can upload the raw screen before deciding what should be protected. We present MaskClaw, an edge-side privacy arbitrator fo...

---

### 26. GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction

**Authors:** Jinze Gu, Qinghua Mao, Xi Lin, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28645v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28645v1)

**Summary:** Retrieval-Augmented Generation (RAG) enhances LLMs by grounding generation in query-relevant external evidence. Beyond unstructured text corpora, Graph RAG integrates knowledge graphs into the retrieval pipeline, enabling LLMs to access entities, relations, and multi-hop dependencies encoded in structured knowledge. However, the same structured knowledge that empowers Graph RAG also creates a new privacy attack surface. We demonstrate that Graph RAG systems can be turned into structural oracles:...

---

### 27. GraphLit: Learning Text-Enriched Dynamic Character Network Representations for Literary Study

**Authors:** Gaspard Michel, Elena V. Epure, Romain Hennequin, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28643v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28643v1)

**Summary:** Methods to represent literary texts as graphs or sequences of graphs mainly focus on representing character interactions, and often overlook another crucial aspect: the textual context in which characters interact. We introduce Dynamic Heterogeneous Character Networks (DHCNs), which organize long novels into temporally localized heterogeneous graphs that align characters with their textual contexts. We extract around 20,000 DHCNs from Project Gutenberg, and propose GraphLit, a self-supervised le...

---

### 28. The Attentional White Bear Effect in Transformer Language Models

**Authors:** Rebecca Ramnauth, Brian Scassellati

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28639v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28639v1)

**Summary:** Instruction-based suppression is widely used to prevent language models from generating prohibited content, yet it remains unclear whether suppression reduces internal representation or merely suppresses expression. We investigate this question through representational probing, attention analysis, and behavioral semantic leakage experiments across multiple transformer models. We find that prohibited concepts remain highly recoverable from hidden representations under suppression, continue to inf...

---

### 29. Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents

**Authors:** Zheng Wu, Pengzhou Cheng, Zongru Wu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28629v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28629v1)

**Summary:** Recent advancements in multimodal large language models (MLLMs) have shown exceptional potential in enabling mobile-using agents to autonomously execute human instructions. However, fully automated agents often try to execute tasks even when they are unable to resolve them, leading to the problem of over-execution. Previous studies solve it by training a interactive mobile-using agents to let agents request human interaction when agents can not complete user instructions. However, we find that t...

---

### 30. Measuring Form and Function in Language Models

**Authors:** Héctor Javier Vázquez Martínez, Charles Yang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28616v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28616v1)

**Summary:** We introduce quantitative metrics for child language acquisition to evaluate language models. Our focus is on the formal syntactic and functional discourse properties of determiners in English, which young children acquire early and accurately. We propose Contextual Alternative Choice (CAC), a new prompting method which provides targeted tests for both syntactic and discourse knowledge of language. The method enables direct comparison of language models against children, and more importantly, ag...

---

### 31. Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution

**Authors:** Susanna Cifani, Mario Luca Bernardi, Marta Cimitile

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28607v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28607v1)

**Summary:** Modern information systems require autonomous agents capable of navigating complex workflows, yet current methodologies often struggle with the transition from structured metadata parsing to general environmental perception. While the integration of MLLMs has enabled agents to interact directly with GUIs, existing approaches typically treat task sequences as discrete, linear episodes. This fragmentation prevents agents from capturing the underlying transition topology, limiting their effectivene...

---

### 32. Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability

**Authors:** Leizhen Zhang, Shuhan Chen, Sheng Chen

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28602v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28602v1)

**Summary:** Large language models (LLMs) are increasingly used for tasks that implicitly reduce to Boolean satisfiability (SAT), yet their reasoning ability on SAT remains unclear. We present a systematic study of LLMs on 2-SAT and 3-SAT, together with two canonical reductions, Vertex Cover and discrete 3D packing, to probe representation-invariant reasoning. We first evaluate models using conventional metrics, including accuracy, precision, recall, and F1, as well as the SAT phase-transition setting. We fi...

---

### 33. Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News

**Authors:** Alejandro Buitrago López, Alberto Ortega Pastor, Javier Pastor-Galindo, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28598v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28598v1)

**Summary:** LLM-powered social agents are increasingly used to simulate online social behavior, yet their realism remains difficult to validate. Existing work has largely relied on general-purpose benchmarks, while less attention has been paid to short, reactive discourse such as audience replies to online news.   In this paper, we evaluate whether LLM-generated reactions to Spanish online news reproduce measurable properties of real audience discourse. Using the Hatemedia dataset, we pair 5,631 news items ...

---

### 34. Models That Know How Evaluations Are Designed Score Safer

**Authors:** Katharina Deckenbach, Haritz Puerto, Jonas Geiping, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28591v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28591v1)

**Summary:** The validity of AI safety evaluations depends on models behaving consistently across controlled and deployment settings. Prior work has identified test-time contextual cues, such as hypothetical scenarios, as a source of verbalized evaluation awareness and subsequent behavioral shift. In this paper, we investigate a potential explanation of this phenomenon: evaluation meta-knowledge, defined as parametric knowledge about the structural traits that characterize evaluations. Similar to dataset con...

---

### 35. Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs

**Authors:** Yongsik Seo, Wooseok Jeong, Eunyoung Kim, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28565v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28565v1)

**Summary:** Users of search-augmented LLMs rely on citations as evidence that responses are grounded in real sources, and rarely verify the cited pages themselves. Millions of queries per day now pass through these systems, making citation quality a silent determinant of whether users are informed or misled-yet existing benchmarks each address one facet in isolation, leaving the joint structure that determines citation trustworthiness unmeasured. We construct CITETRACE, a large-scale dataset that traces the...

---

### 36. Soft-SVeRL: Self-Verified Reinforcement Learning with Soft Rewards

**Authors:** Saurabh Dash, Pierre Clavier, John Dang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28561v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28561v1)

**Summary:** Reinforcement Learning from Verifiable Rewards (RLVR) has improved language models in domains such as mathematics and code, where correctness can be checked automatically. However, many important tasks are only partially verifiable: prompts contain multiple requirements, responses may satisfy some but not all of them, or no single reference answer might exist. We introduce Soft-RLVR, a framework for reinforcement learning from decomposed, learned verification signals. Soft-RLVR converts each pro...

---

### 37. Cultural Binding Heads in Language Models

**Authors:** Avrile Floro, Luca Benedetto

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28543v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28543v1)

**Summary:** LLMs often default to equal treatment across cultural groups, even though context warrants differentiation: this is a lack of difference awareness. Using mechanistic interpretability and a factorial design on the N4 cultural appropriation benchmark from Wang et al. (2025), we identify 2-3 mid-layer attention heads per model that contribute causally to cultural binding across eight models (four architectures, base and instruct). Cultural binding is the process of associating cultural items with t...

---

### 38. GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection

**Authors:** Zheng Wu, Chengcheng Han, Zhengxi Lu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28534v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28534v1)

**Summary:** Despite the rapid progress of multimodal large language models in building Graphical User Interface (GUI) agents, their real-world task completion is fundamentally bottlenecked by a lack of world knowledge about GUI operations. Existing solutions typically rely on expensive multi-agent scaffolding or conventional post-training paradigms, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). However, post-training only allows agents to implicitly absorb world knowledge through act...

---

### 39. Entropy-aware Masking for Masked Language Modeling

**Authors:** Gokul Srinivasagan, Kai Hartung, Munir Georges

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28526v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28526v1)

**Summary:** Masked language modeling has become a standard pretraining objective for training encoder-based language models. In this approach, certain tokens in the input are masked, and the model learns to predict them using the surrounding context. This process enables the model to capture both syntactic and semantic properties of language. Conventionally, the tokens selected for masking are chosen at random, which may not always yield the most effective learning signals. In this work, we examine a token ...

---

### 40. ClinicalEncoder26AM: A Multlilingual Diagnosable ColBERT Model; Evidences from the MultiClinNER Shared Task

**Authors:** François Remy

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28521v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28521v1)

**Summary:** ClinicalEncoder26AM is a multilingual Diagnosable ColBERT for clinical and biomedical texts, which aligns at multiple levels its token-level semantic with ClinicalMap25, a clinical latent space inspired by BioLORD-2023 and enriched with synthetic and annotated supervision. The post-training recipe builds upon BGE-M3, and combines synthetic clinical notes, patient--doctor conversations, and annotated resources such as MedMentions, while considering both named-entity-level and sentence-level repre...

---

### 41. On Compositional Learning Behaviours in Formal Mathematics

**Authors:** Kevin Yandoka Denamganaï

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28512v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28512v1)

**Summary:** Self-evolving scientific agents capable of conquering the hard tail of formal mathematics require Compositional Learning Behaviours (CLBs) -- the capacity to ground and recombine novel symbolic structures in context, beyond mere recombination of prelearned atoms. We propose \textbf{S2B-LM}, an adaptation of the Symbolic Behaviour Benchmark that removes numerical processing as a confound and adds chain-of-thought scaffolding to elicit rather than merely probe latent CLB competency. Cross-evaluati...

---

### 42. Functional Entropy: Predicting Functional Correctness in LLM-Generated Code with Uncertainty Quantification

**Authors:** Dylan Bouchard, Mohit Singh Chauhan, Zeya Ahmad, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28500v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28500v1)

**Summary:** Large language models have shown impressive capabilities in code generation, yet they often produce functionally incorrect code. Uncertainty quantification (UQ) methods have emerged as a promising approach for detecting hallucinations in natural language generation, but their effectiveness for code generation tasks remains underexplored. We systematically evaluate how UQ techniques transfer to code generation across three programming languages, five LLMs, and over 1,700 problems. We find that so...

---

### 43. A new semantically annotated corpus with syntactic-semantic and cross-lingual senses

**Authors:** Myriam Rakho, Eric Laporte, Matthieu Constant

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28494v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28494v1)

**Summary:** We describe a new sense-tagged corpus for word sense disambiguation. The corpus is constituted of instances of 20 French polysemous verbs. Each verb instance is annotated with three sense labels: (1) the actual translation of the verb in the english version of this instance in a parallel corpus, (2) an entry of the verb in a computational dictionary of French (the Lexicon-Grammar tables) and (3) a fine-grained sense label resulting from the concatenation of the translation and the Lexicon-Gramma...

---

### 44. Comonadic Morphophonology: A Compositional Framework for Context-Dependent Morphological Rules in Finnish

**Authors:** Yongseok Jang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28484v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28484v1)

**Summary:** Composing finite-state transducers (FSTs) for context-dependent morphophonological rules -- consonant gradation, vowel harmony, possessive suffix assimilation -- leads to multiplicative state explosion; neural models sidestep the problem but provide no formal account of the rules themselves. We present the first framework where each morphophonological rule is a function from a focused local context to a single output segment -- the type of a local rule familiar from cellular automata -- and wher...

---

### 45. Beyond One Path: Evaluating and Enhancing Divergent Thinking in Interactive LLM Agents

**Authors:** Jihyeong Park, Ingeol Baek, Jeonghyun Park, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28465v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28465v1)

**Summary:** Divergent thinking is a core dimension of creativity, yet existing evaluations of Large Language Models (LLMs) treat them as single-turn text generations, failing to capture how an agent reasons through iterative interaction. To address this, we introduce MUTATE, an interactive benchmark designed to evaluate agentic divergent thinking at two levels: path-level, where an agent discovers multiple alternative paths to the same goal, and action-level, where individual actions require non-typical, me...

---

### 46. The Cases LJP Never Sees: Prosecution Decision Prediction for More Complete Criminal Liability Assessment

**Authors:** Junyu Lu, Qi Wei, Peishuo Zheng, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28464v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28464v1)

**Summary:** Legal Judgment Prediction (LJP) has become a core benchmark for evaluating AI in the criminal legal domain, but it only sees criminal cases that have already passed prosecutorial review and been formally indicted. As a result, LJP leaves a substantial blind spot in assessing criminal liability, overlooking cases involving insufficient evidence, no criminal liability, or guilt exempted from punishment. To fill this gap, we propose \textbf{Prosecution Decision Prediction (PDP)}, the first Legal AI...

---

### 47. AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates

**Authors:** Shaolong Chen, Madalina Ciobanu, Qingqing Mao, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28440v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28440v1)

**Summary:** DPO has become a widely adopted alternative to RLHF for aligning LLMs with human preferences, eliminating the need for a separate reward model or RL loop. Recent theoretical analysis uncovers an asymmetric gradient behavior in DPO: the loss suppresses dispreferred responses substantially faster than it promotes preferred ones, causing the model to learn to avoid bad answers rather than to generate good ones. We propose AdaDPO, a Self-Adaptive variant of the DPO algorithm that introduces per-pref...

---

### 48. Breaking the Script Barrier: Enabling Automatic Alignment for PoS-based ASR Error Analysis in Non-Latin Scripts

**Authors:** Prasenjit K Mudi, Dahlia Devapriya, Sheetal Kalyani

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28438v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28438v1)

**Summary:** Automatic Speech Recognition (ASR) systems are commonly evaluated using aggregate metrics such as Word Error Rate (WER), which do not capture the linguistic structure of errors. Fine-grained analysis, such as Part-of-Speech (PoS)-wise error characterization, requires accurate alignment between ASR hypotheses and reference transcriptions. However, existing alignment tools are often unreliable for languages written in non-Latin scripts. In this work, we address this gap by proposing a robust, auto...

---

### 49. Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning

**Authors:** Ling-Yue Ge, Lan-Zhe Guo

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28433v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28433v1)

**Summary:** Role-based LLM multi-agent systems need adaptive role pools, yet adapting such systems is not merely a matter of prompt optimization: roles often carry structural obligations, including capability coverage, message compatibility, validation, final-answer aggregation, and parser-compatible output protocols. Existing systems either fix the role inventory and lose adaptivity, or allow unconstrained generation to induce role drift, removing structurally necessary roles and breaking answer contracts....

---

### 50. Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning

**Authors:** Jiapeng Zhu, Jianxiang Yu, Yibo Zhao, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28424v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28424v1)

**Summary:** Equipping large language models with explicit skills has emerged as a promising paradigm for enabling autonomous agents to solve complex tasks. Agent skills can be inherently divided into general skills for broad cognitive transfer and task-specific skills for dynamic execution. However, existing skill-based reinforcement learning (RL) methods typically force a rigid choice between full externalization, which incurs prohibitive context overhead, and full internalization, which risks overfitting ...

---

## cs.CV

**50 papers**

### 1. From Pixels to Words -- Towards Native One-Vision Models at Scale

**Authors:** Haiwen Diao, Jiahao Wang, Penghao Wu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28820v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28820v1)

**Summary:** Current vision-language models (VLMs) typically stitch together separate image encoders and language decoders via multi-stage alignment, a modular framework that inevitably fragments pixel-level signals across frames and scatters early pixel-word interactions. In parallel, native VLMs, despite impressive performance on single images, remain largely unexplored in multi-image, video understanding, and spatial intelligence. Hence, we introduce NEO-ov, a native foundation model that learns cross-fra...

---

### 2. Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

**Authors:** Fangfu Liu, Kai He, Tianchang Shen, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28816v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28816v1)

**Summary:** World models for interactive video generation have largely focused on single-agent settings, where future observations are generated from a single control signal. However, many generated environments require multi-agent interaction: multiple players, robots, or embodied agents act simultaneously within a shared space. Scaling world models to such settings requires a principled multi-agent design: agents should remain independently controllable, permutation-symmetric, and support efficient infere...

---

### 3. HarmoVid: Relightful Video Portrait Harmonization

**Authors:** Jun Myeong Choi, Jae Shin Yoon, Luchao Qi, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28811v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28811v1)

**Summary:** We present a method for harmonizing the lighting of a foreground video to match a target background scene, adjusting shadows, color tone, and illumination intensity (relightful harmonization). Unlike images, acquiring labeled data for videos, where identical motions are recorded under different lighting conditions, is practically infeasible and non-scalable. While one way to create such paired data is to apply existing image-based harmonization models frame by frame to a video, the resulting out...

---

### 4. AREA: Attribute Extraction and Aggregation for CLIP-Based Class-Incremental Learning

**Authors:** Zhen-Hao Xie, Yu-Cheng Shi, Da-Wei Zhou

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28809v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28809v1)

**Summary:** Class-Incremental Learning (CIL) is important in building real-world learning systems. In CLIP-based CIL, the model performs classification by comparing similarity between visual and textual embeddings obtained from template prompts, e.g., ``a photo of a [CLASS]''. This seemingly monolithic matching process can be decomposed into two conceptually distinct stages: attribute extraction and attribute aggregation. For example, a model may recognize cat using attributes such as fur texture and whiske...

---

### 5. Personal Visual Memory from Explicit and Implicit Evidence

**Authors:** Viet Nguyen, Thao Nguyen, Vishal M. Patel, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28806v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28806v1)

**Summary:** Long-term memory is increasingly important for personalized AI agents, yet existing benchmarks and methods remain largely text-centric. Even when images are included, the user-specific information needed for later questions is typically recoverable from text alone, and most memory systems reduce image turns to generic captions. Yet images often carry personal information that text rarely states -- both explicit evidence, such as recurring user-associated entities, and implicit evidence, such as ...

---

### 6. OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

**Authors:** Xinchen Zhang, Bowei Liu, Jiale Liu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28805v1)

**Summary:** Visual outcomes are increasingly central to multimodal large language models, making reliable and fine-grained verification essential for scaling generalist foundation models. In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training. We identify two key findings. First, symbolic verifier outputs (e.g., bounding ...

---

### 7. Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling

**Authors:** Xinyu Wang, Mingze Li, Sicheng Lyu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28803v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28803v1)

**Summary:** Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We c...

---

### 8. Bias Leaves a Gradient Trail: Label-Free Bias Identification via Gradient Probes on Concept Decompositions

**Authors:** Thomas Vitry, Kieran Edgeworth, Stefan Wermter, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28780v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28780v1)

**Summary:** Vision classifiers can exploit spurious correlations, achieving high in-distribution accuracy yet failing under distribution shift. Existing approaches to bias mitigation and analysis often depend on curated datasets, spurious-attribute or group labels, or retraining, which may be infeasible once a model is deployed or the relevant bias is unknown. We present a bias-label-free, post-hoc method for identifying spurious concepts in frozen vision models, relying only on standard class labels from a...

---

### 9. The Abstraction Gap in Vision-Language Causal Reasoning

**Authors:** Chinh Hoang, Mohammad Rashedul Hasan

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28779v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28779v1)

**Summary:** Vision-language models (VLMs) generate fluent causal explanations, but current evaluations cannot distinguish linguistic plausibility from faithful causal reasoning. We introduce a dual-probe methodology that isolates these properties. The Text-Only Probe measures linguistic quality. The Chain-Text Probe requires models to first generate explicit causal chains. The Abstraction Gap (AG) metric quantifies the normalized performance difference. Evaluating eight VLMs on CAGE (Causal Abstraction Gap ...

---

### 10. Self-Prophetic Decoding to Unlock Visual Search in LVLMs

**Authors:** Zhendong He, Qiyuan Dai, Guanbin Li, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28741v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28741v1)

**Summary:** Large Vision-Language Models (LVLMs) are rapidly evolving toward true multimodal reasoning, with visual search representing a concrete instantiation of the thinking-with-images paradigm. However, LVLM visual search faces two key challenges: incompatibility among intrinsic capabilities after post-training, and interference in long multi-step reasoning contexts. To address these, we identify two novel insights. First, self-regulation between pre- and post-training LVLMs leverages the intrinsic sin...

---

### 11. SeeGroup: Multi-Layer Depth Estimation of Transparent Surfaces via Self-Determined Grouping

**Authors:** Hongyu Wen, Jia Deng

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28735v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28735v1)

**Summary:** Transparent objects are common in daily life, and it is important to understand their multilayer depth, including the transparent surface and the objects behind it. Existing methods for multilayer depth typically extend single-layer prediction. They define layers by the front-to-back ordering of 3D points and predict the layers sequentially. However, as layered geometry can admit multiple valid groupings of 3D points into layers, a predefined grouping strategy is inherently restrictive. In this ...

---

### 12. Deep Learning Strain Estimation: Is Physics-Based Simulation the Solution?

**Authors:** Thierry Judge, Nicolas Duchateau, Andreas Østvik, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28697v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28697v1)

**Summary:** Speckle tracking echocardiography (STE) is the clinical standard for myocardial strain estimation. Despite good performance on global strain (GLS), its accuracy for regional strain remains limited, even though this biomarker is highly relevant for early diagnosis and the characterization of subtle abnormalities. from clinical data. Deep learning is a promising alternative, but its development is constrained by the lack of reliable motion references. Existing solutions rely either on STE-derived ...

---

### 13. OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning

**Authors:** Yunyang Ge, Xianyi He, Zezhong Zhang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28691v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28691v1)

**Summary:** Diffusion Transformers achieve strong video generation quality, but the quadratic cost of full attention limits efficiency. We introduce OSP-Next, an efficient text-to-video generation model that integrates sparse attention, parallelism, quantization, and reinforcement learning. OSP-Next uses a hybrid full-sparse attention architecture, where the sparse component is implemented with Skiparse-2D Attention. This fixed-pattern mechanism applies token-wise and group-wise sparse attention along spati...

---

### 14. EntroAD: Structural Entropy-Guided Prompt Adaptation for Zero-Shot Anomaly Detection

**Authors:** Xinyu Zhao, Qingyun Sun, Jiayi Luo, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28630v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28630v1)

**Summary:** Zero-Shot Anomaly Detection (ZSAD) aims to detect anomalies in unseen domains without target-domain adaptation. Recent CLIP-based methods have shown promising performance by leveraging prompt learning and visual-text alignment. However, most existing approaches rely on a single adaptation pathway, which may be insufficient for heterogeneous anomaly patterns across domains. In practice, anomalies exhibit vastly different characteristics, ranging from salient, localized structural disruptions to s...

---

### 15. A Multiscale Kinetic Framework for Image Segmentation: From Particle Systems to Continuum Models

**Authors:** Horacio Tettamanti, Giulia Guicciardi, Mattia Zanella

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28619v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28619v1)

**Summary:** In this work, we present a multiscale kinetic framework for consensus-based image segmentation. By interpreting an image as a system of interacting particles, each pixel is characterised by its spatial position and an internal feature encoding color information. We introduce a coupled interaction scheme governing the evolution of particles in both position and feature spaces, from which we derive a kinetic formulation for the particle density in the space-feature domain combining transport, aggr...

---

### 16. Compositional Text-to-Image Generation Via Region-aware Bimodal Direct Preference Optimization

**Authors:** Zhuohan Liu, Wujian Peng, Yitong Chen, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28615v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28615v1)

**Summary:** Despite the rapid progress of text-to-image (T2I) models, generating images that accurately reflect complex compositional prompts (covering attribute bindings, object relationships, counting) still remains challenging. To address this, we propose BiDPO, a framework to enhance T2I model's capability of compositional text-to-image generation. We begin by introducing an carefully designed pipeline to construct a large-scale preference dataset, BiComp, with strictly quality control. Then, we extend ...

---

### 17. JECA^2: Judgment-Explanation Consistent Adversarial Attack against Forensic Vision-Language Models

**Authors:** Jiachen Qian

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28609v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28609v1)

**Summary:** Forensic vision-language models (VLMs) have recently been developed to detect image tampering and provide natural-language explanations. However, their robustness against adversarial manipulation remains underexplored. Existing adversarial attacks typically aim to flip the model's binary judgment, while the accompanying explanation may still reveal forensic cues and contradict the attacked judgment. In this paper, we study judgment-explanation consistent adversarial attacks against forensic VLMs...

---

### 18. Internally Referenced Low-Light Enhancement

**Authors:** Peiyuan He, Hainuo Wang, Hengxing Liu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28605v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28605v1)

**Summary:** Self-supervised low-light image enhancement (LLIE) is highly appealing as it eliminates the reliance on external paired data. However, the lack of external references causes networks to struggle with decoupling entangled illumination, delicate textures, and amplified noise. To resolve this challenge, we propose an Internally Referenced LLIE framework that extracts reliable physical and structural references from the degraded input image itself. First, we introduce a local exposure-simulated sche...

---

### 19. Mining Multi-Modality Spatio-Temporal Cues for Video Important Person Identification

**Authors:** Xiao Wang, Minglei Yang, Bin Yang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28604v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28604v1)

**Summary:** Identifying key individuals in video scenes is essential for applications such as automated video editing and intelligent surveillance. Current methods primarily focus on static images and immediate visual cues, overlooking the rich spatio-temporal information in videos. This leads to the phenomenon of Temporal Importance Shift (TIS), wherein individuals deemed significant in early frames may be demoted as the entire temporal context is considered. To address this, we introduce the Video Importa...

---

### 20. Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation

**Authors:** Yang Gao, Wuyang Li, Po-Chien Luan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28587v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28587v1)

**Summary:** Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents. However, existing weakly supervised occupancy prediction frameworks predominantly assume rigid-body motion and rely on simple frame-to-frame offsets, limiting their ability to capture fine-grained deformations and maintain temporal coherence. To address this issue, we propose DeGO, a deformable Gaussian occupancy framework that unifies decoupled Gaussi...

---

### 21. Resolution-free neural surrogates for geometric parameterization and mapping with spatially varying fields

**Authors:** Yanwen Huang, Lok Ming Lui, Gary P. T. Choi

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28551v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28551v1)

**Summary:** Many imaging problems require computing spatial transformations induced by spatially varying intensity, feature, or density fields. Canonical examples include distortion correction, deformable image registration, atlas-based segmentation, and deformation-driven image analysis. These tasks can be formulated as geometric mapping problems in which the transformation is constrained to preserve local structure, control boundary behavior, or regulate angular distortion. Such formulations typically lea...

---

### 22. GEM: Generative Supervision Helps Embodied Intelligence

**Authors:** Ruowen Zhao, Bangguo Li, Zuyan Liu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28548v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28548v1)

**Summary:** Embodied Vision-Language Models (VLMs) have demonstrated impressive performance and generalization in robotics, particularly within Vision-Language-Action frameworks. However, a significant gap remains between the high-level semantic focus of standard text-guided pre-training paradigms and the low-level spatial and physical knowledge critical for execution in embodied environments. In this paper, we introduce GEM, a Generative-supervised Embodied vision-language Model designed to bridge this div...

---

### 23. DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving

**Authors:** Chen Shi, Jinrui Xu, Shaoshuai Shi, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28544v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28544v1)

**Summary:** Pretrained foundation models have become an important basis for end-to-end autonomous driving. In contrast to vision-language models pretrained primarily on static image-text pairs, video generative models capture temporal dynamics and motion priors that are naturally suited for driving. We present DriveWAM, a driving world-action model that adapts a pretrained video diffusion transformer into an autoregressive video-action policy. DriveWAM organizes video and action streams into a unified tempo...

---

### 24. Janus-LoRA: A Balanced Low-Rank Adaptation for Continual Learning

**Authors:** Cheng Chen, Pengpeng Zeng, Yuyu Guo, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28495v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28495v1)

**Summary:** Low-Rank Adaptation (LoRA) has emerged as a promising paradigm for Continual Learning. It independently updates its low-rank factors ($A$ and $B$), creating a composite update to the full weight matrix through their interaction. To prevent catastrophic forgetting, this update should remain orthogonal to the task-specific subspace that contains previously learned knowledge. However, we identify that this composite update systematically violates this orthogonality, reintroducing interference and u...

---

### 25. DiscoForcing: A Unified Framework for Real-Time Audio-Driven Character Control with Diffusion Forcing

**Authors:** Kaiyang Ji, Bingsheng Qian, Binghuan Wu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28491v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28491v1)

**Summary:** We study real-time audio-responsive character control as a deployment-faithful problem: strictly causal, bounded-latency streaming that must generate coherent full-body motion at interactive frame rates while the audio condition can change abruptly, including tempo shifts, drops, or user edits. Prior music-to-motion systems are largely optimized for offline generation with global context, and degrade in streaming rollouts where conditioning history becomes stale or unreliable. We introduce Disco...

---

### 26. SSR3D-LLM: Structured Spatial Reasoning via Latent Steps for Fine-Grained Grounding in Unified 3D-LLMs

**Authors:** Jiawei Li, Ziyi Liu, Weijie Shi, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28490v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28490v1)

**Summary:** 3D object grounding localizes referred objects in a 3D scene from natural language. Unified instance-centric 3D-LLMs aim to solve grounding together with dialog, QA, and captioning, yet many rely on a single pointer-style grounding decision that compresses a relational instruction into one selection. This is brittle for fine-grained queries where multiple same-class candidates must be ruled out by context objects and spatial relations. We propose Structured Spatial Reasoning 3D-LLM (SSR3D-LLM), ...

---

### 27. SA4Depth: Consistent Pose-Depth Scale Alignment for Self-Supervised Monocular Depth Estimation

**Authors:** Changxuan Li, Nadine Berner, Nassir Navab, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28477v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28477v1)

**Summary:** Self-supervised depth estimation from monocular sequences relies on the joint learning of a depth and a pose network. Despite abundant research done to improve the depth network, efforts on the pose remain limited. In this context, even when depth is estimated up to scale, we highlight the importance of the alignment between the scene scales estimated by the pose and depth nets. Then, we introduce SA4Depth, an approach to improve this alignment and boost the depth predictions while keeping the i...

---

### 28. REVEAL: Reference-Grounded Reasoning for Multimodal Manipulation Detection

**Authors:** Jun Zhou, Bingwen Hu, Yaxiong Wang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28459v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28459v1)

**Summary:** Multimodal manipulation detection aims to simultaneously identify forged image--text pairs and localize tampered regions, yet existing methods typically rely on memorizing isolated artifacts and struggle with imperceptible manipulation traces or domain shifts. Inspired by human comparative reasoning, we reformulate this task as a reference-grounded verification problem, where authenticity is assessed by comparing a query against retrieved authentic evidence. We propose REVEAL Reference-Enabled V...

---

### 29. Diffusion Large Language Models for Visual Speech Recognition

**Authors:** Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28456v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28456v1)

**Summary:** Existing Visual Speech Recognition (VSR) systems commonly rely on left-to-right autoregressive decoding, which can force premature decisions on visually ambiguous tokens before sufficient context is available. We propose DLLM-VSR, to the best of our knowledge, the first Diffusion Large Language Model (DLLM)-based VSR framework, formulating transcription as iterative masked denoising with flexible-order decoding. With confidence-based unmasking, DLLM-VSR commits high-confidence positions early an...

---

### 30. BiasEdit: A Training-Free Bias-Detect-and-Edit Framework for Learning Fair Visual Classifiers

**Authors:** Jungwook Seo, Yoonsik Park, Changmin Lee, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28450v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28450v1)

**Summary:** Visual data from the Web power image classifiers, which often underpin many web services, such as recommendation and content moderation. However, the raw Web data often contain spurious correlations and social biases, and neural networks are known for their tendency to learn biases present in data. This can reinforce unfairness in web services and the web data, leading to a vicious cycle. In the context of image classification, networks learn bias attributes for a specific class when a majority ...

---

### 31. Self-Supervised Online Robot-Agnostic Traversability Estimation for Open-World Environments

**Authors:** Julia Hindel, Simon Bultmann, Houman Masnavi, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28442v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28442v1)

**Summary:** Self-supervised online traversability estimation enables robots to continuously learn from unlabeled open-world experiences and adapt their navigation behavior toward safe and efficient trajectories. Existing approaches either rely on handcrafted proprioceptive traversability scores, limiting robot-agnosticism, or cluster prior data, preventing online learning. Moreover, many continual learning methods incur substantial memory and computational costs, hindering onboard deployment. We introduce C...

---

### 32. Bayesian Gated Non-Negative Contrastive Learning

**Authors:** Peng Cui, Jiahao Zhang, Lijie Hu

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28441v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28441v1)

**Summary:** While Contrastive Learning (CL) has revolutionized self-supervised representation learning, its latent representations remain highly entangled and opaque, limiting their interpretability in safety-critical applications. We identify that a fundamental cause of this entanglement is the reliance on deterministic similarity measures, which treat all feature dimensions equally. In compositional scenes, this creates an Optimization Conflict: common background features, such as, "blue sky", are encoura...

---

### 33. Anomaly as Non-Conformity via Training-Free Graph Laplacian Energy Minimization

**Authors:** Jungwook Seo, Minjeong Kim, Younkwan Lee, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28428v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28428v1)

**Summary:** Detecting subtle visual anomalies in images remains challenging, particularly when only normal samples are available a priori. Such unsupervised anomaly detection is typically solved by measuring feature similarity of a query patch to a memory of normal patches. However, similarity alone does not reveal how strongly a query patch violates the structure of the normal feature manifold. We propose a training-free Laplacian graph energy optimization formulation, named ANoCo that scores Anomaly by th...

---

### 34. VITAL: Visual-Semantic Dual Supervision for Enhanced and Interpretable Latent Reasoning in Medical MLLMs

**Authors:** Qiaoru Li, Shaotian Liang, Jintao Chen, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28422v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28422v1)

**Summary:** Latent reasoning enables reasoning over continuous hidden states rather than explicit tokens, avoiding the language bottleneck and inference overhead of chain-of-thought for medical VQA. However, existing methods suffer from modality collapse, insufficient visual supervision, and train-inference mismatch. Moreover, their opaque latent states offer no interpretability, which is critical in clinical applications. We propose VITAL, a latent-space reasoning framework for medical MLLMs with visual-se...

---

### 35. EgoRelight: Egocentric Human Capture and Illumination Recovery for Relightable and Photoreal Avatar Rendering

**Authors:** Jianchun Chen, Yinda Zhang, Rohit Pandey, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28401v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28401v1)

**Summary:** Mixed Reality (MR) headsets promise a future of immersive telepresence where virtual humans blend indistinguishably into real or virtual surroundings. Achieving this vision requires a method for capturing a user's motion, estimating appearance under novel lighting, and understanding the environment - all from the constrained viewpoint of a head-mounted display (HMD). Existing approaches treat these as isolated problems: they either focus on driving avatars with baked-in lighting or rely on studi...

---

### 36. Adaptive Temporal Gating of Longitudinal Magnetic Resonance Imaging for Alzheimer's Prediction

**Authors:** Alireza Moayedikia, Sara Fin, Alicia Troncoso Lora, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28397v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28397v1)

**Summary:** Predicting conversion from Mild Cognitive Impairment (MCI) to Alzheimer's Disease (AD) is critical for early intervention. Current deep learning paradigms predominantly rely on cross-sectional structural MRI, neglecting prognostic value in patient-specific anatomical trajectories. We introduce the Temporal Adaptive Fusion Network (TAF-Net), a hybrid CNN-Transformer architecture that models paired longitudinal 3D MRI scans. Central to TAF-Net is a Temporal Fusion Module governed by an Adaptive Te...

---

### 37. Sketch2Motion: Text-driven 2D Sketch to 3D Animation via Diffusion-guided Skeleton Optimization

**Authors:** Gaurav Rai, Ojaswa Sharma

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28394v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28394v1)

**Summary:** Animation of 2D hand-drawn sketches provides an effective medium for visual communication. However, these sketches pose challenges, particularly in handling occlusions and accurately mapping motion. While 3D animation naturally addresses these challenges, estimating 3D motion remains a very complex task. Recent approaches to converting 2D sketches to 3D animations have mainly focused on specific types of motion, such as bipedal movements and facial expressions. We propose Sketch2Motion, a diffus...

---

### 38. Bound-Constrained Sparse Representation for Electrical Impedance Tomography

**Authors:** Chun Zhang, Dong Liu

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28392v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28392v1)

**Summary:** This study proposes a bound-constrained sparse representation (BC-SR) framework for electrical impedance tomography (EIT), aimed at improving conductivity estimation without explicit regularization. BC-SR adopts a representation-driven strategy, generating conductivity from low-dimensional latent variables via an implicit composite parameterization. Structural priors are embedded using a truncated graph-Laplacian basis, while a bound-preserving nonlinear mapping enforces admissible conductivity ...

---

### 39. Toward Semantic-Agnostic and Shape-Aware Vision-Language Segmentation Models

**Authors:** Corentin Seutin, Mohamed Amine Ettaki, Michaël Clément, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28348v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28348v1)

**Summary:** Vision-language segmentation models have recently achieved strong performance by leveraging high-level semantic object categories expressed in natural language. However, this semantic dependence limits their ability to reason about intrinsic visual properties such as shape, geometry, or texture, which are essential in many real-world applications. In this work, we introduce Semantic-Agnostic aNd Shape-Aware (SANSA) segmentation, a new paradigm that requires segmentation models to operate solely ...

---

### 40. Transfer learning RGB models to hyperspectral images with trainable tensor decompositions

**Authors:** Mariette Schönfeld, Laurens Devos, Wannes Meert, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28331v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28331v1)

**Summary:** Transfer learning makes it possible to use large vision networks on a variety of domains, by specializing their models' general filters to new tasks. However, these networks assume the input images to have 3 input channels, making them incompatible with multi- or hyperspectral images. Current approaches that mitigate this incompatibility sacrifice information in either the image, or the model. This work proposes a novel approach that preserves the image and spatial information present in the mod...

---

### 41. Inpainting-Style Conditional Diffusion for Multivariable Time Series Forecasting

**Authors:** Kourosh Kiani, S. M. Muyeen

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28324v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28324v1)

**Summary:** In this paper, we propose a novel conditional diffusion-based framework for multivariable time-series solar power forecasting. The proposed method reformulates temporal PV data as structured two-dimensional representations (images) using a sliding-window patch construction, enabling the application of Denoising Diffusion Probabilistic Models (DDPM) within a unified spatiotemporal learning paradigm. A key contribution of this work is the formulation of solar forecasting as an inpainting problem, ...

---

### 42. EventShiftFlow: Towards Hardware-efficient FPGA-based Flow Estimation

**Authors:** Arianna Alonso Bizzi, Fernando Cladera, C. J. Taylor

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28312v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28312v1)

**Summary:** Event-based vision sensors offer asynchronous, high-temporal-resolution measurements that are attractive for low-latency robotic perception, but many event-based motion estimation methods are computationally intensive and difficult to map to FPGA hardware. We present a streaming velocity estimator that discretizes asynchronous events into fixed-duration time bins, constructs a 1-bit spatial occupancy grid, and evaluates multiple velocity hypotheses in parallel using only fixed-width integer logi...

---

### 43. EchoAvatar: Real-time Generative Avatar Animation from Audio Streams

**Authors:** Bohong Chen, Yumeng Li, Yinglin Xu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28272v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28272v1)

**Summary:** Real-time synthesis of high-fidelity 3D character motion from audio is a pivotal component for next-generation interactive avatars and virtual assistants. However, most existing approaches are limited to offline processing of complete audio sequences or are constrained to specific domains, rarely handling both speech and music effectively. In this paper, we introduce a novel framework designed to generate continuous, coherent full-body motion from streaming speech and music with low latency. Cen...

---

### 44. LV-OSD: Language-Vision-Complementary Open-Set Object Detection

**Authors:** Yupeng Zhang, Ruize Han, Wei Feng, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28271v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28271v1)

**Summary:** Object detection is an important task in computer vision, which aims to detect the objects of interest. through the given category list or query images. In this work, we propose a new problem of language-visual-complementary open-set object detection (LV-OSD), i.e., using the flexible text-based and/or image-based prompts to specify the desired object categories. This setting is more common and practical in real-world applications. For this purpose, we design a dual-branch detection framework, L...

---

### 45. Every9D-21M: Large-Scale Real-World 9D Canonicalization of Everyday Objects

**Authors:** Leonhard Sommer, Emil Akopyan, Adam Kortylewski

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28270v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28270v1)

**Summary:** Estimating the 9D pose of everyday objects from a single real-world image remains challenging. This is largely due to the lack of large-scale supervision. Most existing datasets either rely heavily on synthetic renderings or provide limited coverage of real-world objects: the largest real-world 9D pose dataset to date contains only 17K annotated objects across 9 categories. We address this gap with Every9D-21M, a dataset of 9D pose annotations for 21.8M real-world images from 109K object- centri...

---

### 46. MORI-Seg: Learning Morphological Geometry for Instance Segmentation without Instance Annotations

**Authors:** Leiyue Zhao, Tianyu Shi, Daniel Reisenbuchler, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28261v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28261v1)

**Summary:** Instance-level quantification of kidney functional units is essential for morphometric analysis, yet most publicly available pathology datasets provide only semantic segmentation annotations, where adjacent structures of the same class are merged into single regions. This prevents reliable instance-level analysis and limits downstream quantitative studies. Existing heuristic post-processing methods often yield suboptimal instance separation, particularly in crowded and adherent regions, while de...

---

### 47. GUI Agents for Continual Game Generation

**Authors:** Yixu Huang, Bo Li, Na Li, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28258v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28258v1)

**Summary:** Generating a game is not the same as making one that can be played. Despite advances in code generation, existing approaches treat game generation as one-shot translation from prompt to artifact, leaving interaction-level failures undetected. We argue that evaluating and improving game generation requires a player, and study two roles for graphical user interface (GUI) agents in this process: (1) as an objective evaluator, for which we introduce PlaytestArena, a new evaluation environment that p...

---

### 48. Category-Level 3D Correspondence in Camera Space via Morphable Object Priors

**Authors:** Leonhard Sommer, Artur Jesslen, Basavaraj Sunagad, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28257v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28257v1)

**Summary:** Understanding 3D objects from images is fundamental to robotics and AR/VR applications. While recent work has made progress in category-level pose estimation, current representations fail to capture the fine-grained semantics needed for reasoning about object parts, functions, and interactions. In this work, we study category-level 3D correspondence in camera space -- predicting, from a single image, 3D locations that remain consistent across instances within a category -- and show that it can e...

---

### 49. PointQ-Bench: Benchmarking Diagnostic and Interpretable Point Cloud Quality Assessment

**Authors:** Duanchu Wang, Cheng Li, Junjie Yang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28241v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28241v1)

**Summary:** Point cloud quality plays a critical role in 3D acquisition, reconstruction, rendering, and perception, yet existing point cloud quality assessment (PCQA) research remains largely centered on scalar score prediction. In practical inspection scenarios, quality assessment often involves identifying defects, characterizing dominant issue types, assessing downstream usability, and providing evidence-supported descriptions, which are not explicitly evaluated by current benchmarks. We introduce PointQ...

---

### 50. Learning to Label: A Reinforced Self-Evolving Framework for Semi-supervised Referring Expression Segmentation

**Authors:** Runlong Cao, Ying Zang, Chuanwei Zhou, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28239v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28239v1)

**Summary:** Semi-supervised referring expression segmentation (SS-RES) aims to achieve precise pixel-level language grounding under limited annotation, yet suffers from limited supervision and unreliable pseudo-labels when exploiting unlabeled image-text pairs. In this work, we propose Learning to Label, a reinforced self-evolving framework (L2L) that casts pseudo-label construction as a learnable decision-making process. To build foundational understanding, we leverage a multimodal large language model to ...

---

## cs.LG

**50 papers**

### 1. PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective

**Authors:** Yangyi Huang, Ruotian Peng, Zeju Qiu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28819v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28819v1)

**Summary:** Parameter-efficient finetuning (PEFT) has become the standard approach for adapting large language models, yet evaluations largely emphasize downstream accuracy while overlooking the retention of pretrained capabilities. We argue that PEFT should be assessed through the stability-plasticity dilemma: the trade-off between target-task adaptation and resistance to forgetting. We introduce PEFT-Arena, a benchmark that jointly measures downstream performance and general capability retention. Across m...

---

### 2. Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation

**Authors:** Jiahe Pan, Stelian Coros, Jitendra Malik, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28812v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28812v1)

**Summary:** A primary bottleneck in contact-rich manipulation is the difficulty of collecting real-world data. Sim-to-real reinforcement learning offers a scalable alternative, but the simulation-reality gap prevents information-dense modalities like touch from being effectively used. Existing sim-to-real methods often mitigate this gap by simplifying tactile data into coarse low-dimensional features -- sacrificing the richness required for complex manipulation. In this work, we introduce Center-of-Pressure...

---

### 3. Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization

**Authors:** Audrey Chan, Aaron Labbé, Jacob Lavoie, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28810v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28810v1)

**Summary:** Functional music applications, from consumer focus and sleep aids to clinical interventions, share a distinctive recommendation problem: success is defined by the listener's affective state, but online experimentation on emotion is ethically constrained, particularly for clinical populations who cannot reliably skip a song or report distress. We describe AMRS, the Affective Music Recommendation System deployed on LUCID's health-and-wellness platforms, which serve clinical users (primarily older ...

---

### 4. AREA: Attribute Extraction and Aggregation for CLIP-Based Class-Incremental Learning

**Authors:** Zhen-Hao Xie, Yu-Cheng Shi, Da-Wei Zhou

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28809v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28809v1)

**Summary:** Class-Incremental Learning (CIL) is important in building real-world learning systems. In CLIP-based CIL, the model performs classification by comparing similarity between visual and textual embeddings obtained from template prompts, e.g., ``a photo of a [CLASS]''. This seemingly monolithic matching process can be decomposed into two conceptually distinct stages: attribute extraction and attribute aggregation. For example, a model may recognize cat using attributes such as fur texture and whiske...

---

### 5. OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

**Authors:** Xinchen Zhang, Bowei Liu, Jiale Liu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28805v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28805v1)

**Summary:** Visual outcomes are increasingly central to multimodal large language models, making reliable and fine-grained verification essential for scaling generalist foundation models. In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training. We identify two key findings. First, symbolic verifier outputs (e.g., bounding ...

---

### 6. Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling

**Authors:** Xinyu Wang, Mingze Li, Sicheng Lyu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28803v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28803v1)

**Summary:** Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We c...

---

### 7. CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models

**Authors:** Abhilash Durgam, Nyle Siddiqui, Jeffrey A. Chan-Santiago, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28792v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28792v1)

**Summary:** Electroencephalography (EEG) is a critical, non-invasive method to monitor electrical brain activity. EEGs can span anywhere from a couple seconds to multiple hours, posing a major hurdle for existing deep learning methods due to two major factors: (1) existing EEG models are predominantly built upon the attention mechanism, incurring quadratic scaling as the sequence length increases, and (2) raw EEG signals must be processed in a sliding-window fashion due to fixed-length input requirements, p...

---

### 8. Bias Leaves a Gradient Trail: Label-Free Bias Identification via Gradient Probes on Concept Decompositions

**Authors:** Thomas Vitry, Kieran Edgeworth, Stefan Wermter, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28780v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28780v1)

**Summary:** Vision classifiers can exploit spurious correlations, achieving high in-distribution accuracy yet failing under distribution shift. Existing approaches to bias mitigation and analysis often depend on curated datasets, spurious-attribute or group labels, or retraining, which may be infeasible once a model is deployed or the relevant bias is unknown. We present a bias-label-free, post-hoc method for identifying spurious concepts in frozen vision models, relying only on standard class labels from a...

---

### 9. Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents

**Authors:** Suji Kim, Kangsan Kim, Sung Ju Hwang

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28775v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28775v1)

**Summary:** Computer-use agents (CUAs) have recently made substantial progress, but deploying a separate large expert for each software domain remains expensive. Small open computer-use agents are more practical specialization targets, but they remain substantially weaker and exhibit uneven domain-specific failures. A straightforward remedy is to synthesize large-scale training data for the target domain, yet we find that this naive approach yields only marginal improvements. Building on this observation, w...

---

### 10. Rethinking Memory as Continuously Evolving Connectivity

**Authors:** Jizhan Fang, Buqiang Xu, Zhixian Wang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28773v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28773v1)

**Summary:** Existing memory-augmented LLM agents often treat memory as a static repository with pre-defined representations and fixed retrieval pipelines, which is brittle in dynamic agentic environments where feedback, task variation, and heterogeneous signals continuously reshape what should be remembered and how it should be connected. To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through th...

---

### 11. Multi-Mixer Models: Flexible Sequence Modeling with Shared Representations

**Authors:** Kevin Y. Li, Asher Trockman, Ananda Theertha Suresh, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28769v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28769v1)

**Summary:** Softmax attention is the cornerstone of modern large language models, but its memory scales linearly and compute quadratically with sequence length. Linear recurrent models, such as linear attention and state space models, have become widely studied as alternatives to attention due to their linear compute and constant memory. While these sub-quadratic token mixing methods, or mixers, achieve promising efficiency gains and competitive results on a wide range of benchmarks, current linear recurren...

---

### 12. Principled Algorithms for Optimizing Generalized Metrics in Multi-Label Learning

**Authors:** Mehryar Mohri, Yutao Zhong

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28767v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28767v1)

**Summary:** Many real-world classification tasks require predicting multiple labels per instance, necessitating the optimization of complex evaluation metrics such as the $F$-measure and Jaccard index. While the Empirical Utility Maximization (EUM) framework is natural for these population-level metrics, existing theoretical results are largely limited to asymptotic Bayes-consistency. In this paper, we develop principled learning algorithms for optimizing a broad class of generalized metrics within the EUM ...

---

### 13. LLM Zeroth-Order Fine-Tuning is an Inference Workload

**Authors:** Zelin Li, Caiwen Ding

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28760v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28760v1)

**Summary:** Zeroth-order (ZO) fine-tuning is attractive for large language models because it replaces backpropagation with forward objective evaluations. Existing implementations nevertheless execute ZO algorithms inside conventional training loops, even though their dominant work is repeated scoring under nearby parameter states. This creates a workload-runtime mismatch: the algorithm asks for structured inference-style scoring, while the system exposes a sequence of fragmented training-loop steps. We show...

---

### 14. Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL

**Authors:** Kunhao Zheng, Pierre Chambon, Juliette Decugis, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28751v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28751v1)

**Summary:** Linear interpolation between fine-tuned checkpoints has been shown to trace the Pareto front between competing objectives, but whether extrapolative weight averaging can extend such frontiers to new checkpoints useful at inference time, without additional RL training, remains unclear. We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency. Starting from a shared initialization...

---

### 15. BIRDNet: Mining and Encoding Boolean Implication Knowledge Graphs as Interpretable Deep Neural Networks

**Authors:** Tirtharaj Dash

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28739v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28739v1)

**Summary:** Tabular data in knowledge-rich domains often carries a latent prior in the form of Boolean implication relationships (BIRs) between pairs of features. We mine such relationships with a sparse-exception binomial test. The mined implications form a typed directed graph, equivalent to a propositional rule base of 2-literal clauses. We encode this graph as the connectivity of a layered neural network, called BIRDNet, in which each hidden unit corresponds to one mined rule and binds only to its two f...

---

### 16. Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests

**Authors:** Richard J. Young, Gregory D. Moody

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28734v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28734v1)

**Summary:** A general-purpose language model that answers a harmful question returns text; a coding model that complies with a malicious request can return a working weapon -- a keylogger, a ransomware stub, an exploit that runs as written. This asymmetry in the severity of a single act of compliance implies coding-specialized models should clear a higher refusal bar than general-purpose chat models, not a lower one, yet the field cannot presently tell whether they do. Refusal benchmarks for malicious code ...

---

### 17. MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

**Authors:** Xinle Deng, Ruobin Zhong, Hujin Peng, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28732v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28732v1)

**Summary:** Memory is essential for enabling large language models to support long-horizon reasoning, yet existing memory systems remain unreliable and difficult to debug. Tracing memory's dynamic evolution is crucial to understand how information is synthesized, propagated, or corrupted over time. In this work, we study the new problem of error tracing and attribution in LLM memory systems. We propose a novel framework that transforms memory pipelines into executable memory evolution graphs, enabling fine-...

---

### 18. Beyond Lipschitz: Data-Driven Robustness via Discrete Modulus of Continuity

**Authors:** Jürgen Dölz, Michael Multerer, Michele Palma

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28729v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28729v1)

**Summary:** Robustness of neural networks is commonly quantified via local or global Lipschitz constants. However, Lipschitz continuity can be overly coarse or overly restrictive as global robustness measure, failing to capture nuanced, data-dependent behavior. We propose a data-driven, architecture-agnostic framework based on the discrete modulus of continuity (DMOC), a non linear generalization of Lipschitz continuity that provides a finer notion of robustness. Unlike many existing approaches, DMOC does n...

---

### 19. How VLAs Fail Differently: Black-Box Action Monitoring Reveals Architecture-Specific Failure Signatures

**Authors:** Krishnam Gupta

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28726v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28726v1)

**Summary:** We discover that VLA architectures fail in fundamentally different, predictable ways at the motor-command level. Running VQ-BeT, Diffusion Policy, and ACT on identical evaluation protocols (n=450 episodes across PushT and ALOHA 14-DOF bimanual manipulation), we find: (1) direction reversal rate is a universal failure predictor across all three architectures (AUROC=0.93, 0.79, 0.91; p<0.001); (2) jerk monitoring is predictive only for discrete-token architectures, following a discrete-to-continuo...

---

### 20. Stage-wise Distortion-Perception Traversal in Zero-shot Inverse Problems with Diffusion Models

**Authors:** Jiawei Zhang, Ziyuan Liu, Leon Yan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28711v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28711v1)

**Summary:** The distortion-perception (D-P) tradeoff is a fundamental phenomenon of Bayesian inverse problems, which characterizes the inherent tension between distortion performance and perceptual quality. Enabling flexible traversal of the D-P tradeoff at inference time is crucial for practical applications. Despite the recent success of diffusion models in zero-shot inverse problem solving, efficient and principled strategies for D-P traversal in diffusion-based inverse algorithms remain inadequately cha...

---

### 21. Beyond Binary Moral Judgment: Modeling Ethical Pluralism in AI

**Authors:** Aisha Aijaz, Rahul Goel, Arnav Batra, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28707v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28707v1)

**Summary:** Critical decision-making in socially consequential spaces is increasingly involving AI systems at varying capacities. Yet, despite the ubiquity of autonomous systems, most approaches to handling autonomous moral decision-making resort to scalar or binary judgments. These methods are insufficient for acceptable moral reasoning, as they provide little explanation, leaving out imperative contextual and theoretical information that must be included to support accountability. For this, we propose a f...

---

### 22. Understanding Generalization and Forgetting in In-Context Continual Learning

**Authors:** Guangyu Li, Meng Ding, Lijie Hu

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28705v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28705v1)

**Summary:** In-context learning (ICL) derives its power from enabling Large Language Models to adapt to new tasks via prompt-based reasoning alone, entirely bypassing the need for parameter updates. Existing theories primarily study ICL in single-task settings, while real-world prompts often contain sequences of heterogeneous tasks, leaving a gap in understanding whether Large Language Models implicitly perform continual learning during inference. To bridge this gap, we propose the first theoretical framewo...

---

### 23. Expressive Power of Floating-Point Neural Networks with Arbitrary Reduction Orders and Inexact Activation Implementations

**Authors:** Yeachan Park, Geonho Hwang, Wonyeol Lee, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28704v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28704v1)

**Summary:** Most existing expressivity theories for neural networks assume exact real arithmetic, whereas practical neural networks are executed under finite-precision floating-point arithmetic with implementation-dependent execution semantics. Recent works have begun studying the expressive power of floating-point neural networks, but existing results are limited to highly restricted activation functions and idealized assumptions such as fixed left-to-right reduction orders and correctly rounded activation...

---

### 24. Latent-Conditioned Parameterized Quantum Circuits as Universal Approximators for Distributions over Quantum States

**Authors:** Quoc Hoan Tran, Koki Chinzei, Yasuhiro Endo, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28690v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28690v1)

**Summary:** Many applications in quantum simulation, quantum chemistry, and quantum machine learning require not a single quantum state but an ensemble of states characterizing the heterogeneity of a target system. Preparing such ensembles state-by-state is prohibitive in both variational and fault-tolerant settings, motivating a generative-modeling approach. We introduce latent-conditioned parameterized quantum circuits (LPQCs), a hybrid quantum-classical framework in which classical neural networks map a ...

---

### 25. History-aware adaptive reduced-order models via incremental singular value decomposition

**Authors:** Amirpasha Hedayat, Ali Mohaghegh, Laura Balzano, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28684v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28684v1)

**Summary:** Reduced-order models (ROMs) can accelerate high-dimensional dynamical simulations, but their accuracy often deteriorates when online dynamics leave the regime represented by offline training data. We develop a projection-based adaptive ROM framework based on incremental singular value decomposition (iSVD), in which occasional full-order operator evaluations provide correction snapshots for online basis updates. The intrusive ROMs considered here are fully parameterized by the basis, so each upda...

---

### 26. Optimal ridge regularization revisited

**Authors:** Jack Timmermans, Sergio A. Alvarez

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28679v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28679v1)

**Summary:** We consider $L^2$-regularized linear (ridge) regression over a finite data sample $X$ with bounded covariance and linear prediction targets $y$ with additive isotropic noise of finite variance. We present an iterative procedure to compute the optimal regularization strength numerically from the generative parameters in the fixed-$X$ setting and prove its convergence at limited noise levels. Our experimental evaluation over synthetic data shows that the proposed procedure combined with sample-bas...

---

### 27. Optimal Data Acquisition for Reinforcement Learning: A Large Deviations Perspective

**Authors:** Mingjie Hu, Jian-Qiang Hu, Enlu Zhou

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28675v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28675v1)

**Summary:** Data acquisition efficiency is a central challenge in deploying reinforcement learning in business and healthcare operations, where interactions are costly, slow, and often involve humans in the loop. This paper develops a unified large deviations framework for data acquisition in infinite-horizon reinforcement learning. We introduce the exponential decay rate of the policy-selection error probability as a principled efficiency metric and derive a variational characterization of this rate via la...

---

### 28. Activation Steering for Synthetic Data Generation: The Role of Diversity in Downstream Safety Detection

**Authors:** Vijeta Deshpande, Tootiya Giyahchi, Veena Padmanabhan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28664v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28664v1)

**Summary:** Safety detection models require examples of HHH (Helpful, Harmless, Honest)-violating outputs for robust generalization, however such examples are scarce. Activation Steering (AS) has emerged as a data-efficient method for generating target-concept-aligned responses. We investigate whether AS can generate high-quality training datasets for downstream classifiers, a question that remains untested. We present a two-fold study with intrinsic and extrinsic evaluation across $4$ concepts $\times\,2$ ...

---

### 29. Applications of temporal graph learning for predicting the dynamics of biological systems

**Authors:** Manuel Dileo, Andrea Sottoriva

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28659v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28659v1)

**Summary:** Biological foundation models have shown strong performance in single-cell representation learning by applying transformer architectures directly to gene-expression matrices. However, these approaches predominantly operate in static settings and do not explicitly model the temporal evolution of developmental programs in the cell. Modeling such dynamics is important for understanding how cellular states progressively emerge, differentiate, and reorganize during development or disease progression. ...

---

### 30. Interpretability-Guided Layer Selection over Subspace Projection: SAEs as Stethoscopes, Not Scalpels, for Raw Task Vector Model Editing

**Authors:** Li Lei, Madalina Ciobanu, Qingqing Mao, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28649v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28649v1)

**Summary:** LLMs increasingly require surgical model editing to enhance domain-specific capabilities without incurring the computational cost or catastrophic forgetting associated with full fine-tuning. Sparse Autoencoders (SAEs) have emerged as a promising tool in this setting, in principle allowing for feature-level identification of where to intervene. In this work, we rigorously evaluate an SAE-guided editing pipeline for mathematical reasoning on Gemma-3-4B-IT and uncover a fundamental failure mode: th...

---

### 31. Augmenting Attention with Exponentially Decaying Memory Improves Query-Aware KV Sparsity

**Authors:** Xiuying Wei, Caglar Gulcehre

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28640v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28640v1)

**Summary:** Efficient inference is critical for long-context language models, where attention computation and KV-cache access dominate the cost. Recent work RAT+, introduces a recurrence-augmented attention backbone that enables flexible dilated attention at inference time. In this paper, we investigate whether this exponentially decaying memory can also improve existing query-aware sparse inference methods. Using representative methods including Quest, MoBA, and SnapKV, we show that RAT+ consistently impro...

---

### 32. Single-Rollout Hidden-State Dynamics for Training-Free RLVR Data Selection

**Authors:** Jianghao Wu, Jianfei Cai, Weiqiang Wang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28631v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28631v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) can yield large reasoning gains from very few training instances, yet its strong sensitivity to which instances are used makes data selection a central bottleneck. Most existing selection pipelines rely on training-time optimization signals and/or require access to verifiable rewards or ground-truth answers over large candidate pools, which is costly and often infeasible in specialized domains. We study RLVR data selection in a setting where ...

---

### 33. When Interpretability Is Unequally Distributed: Fairness in Hybrid Interpretable Models

**Authors:** Ziba Jabbar Zare, Ulrich Aïvodji, Julien Ferry, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28626v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28626v1)

**Summary:** Hybrid interpretable models combine a transparent component with a black-box model by assigning some examples to the former and deferring the rest to the latter. While this design enables flexible tradeoffs between accuracy and interpretability, it also raises a distinct procedural fairness concern: some demographic groups may systematically receive interpretable decisions, while others are disproportionately routed to a black box.   We formalize this issue as Interpretability Coverage Disparity...

---

### 34. Random Process Flow Matching: Generative Implicit Representations of Multivariate Random Fields

**Authors:** Julien Lalanne, David Picard, Lionel Boillot, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28625v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28625v1)

**Summary:** Generative modeling provides a powerful framework for learning data distributions. These models initially relied on probabilistic methods such as Gaussian Processes (GP) for uncertainty-aware predictions and shifted towards larger trainable models to learn more complex distributions. In this work, we introduce Random Process (RP) Flow, a Flow Matching-based framework that represents the vector field as a neural implicit function. Unlike modern generative methods, our setting involves a single ob...

---

### 35. Implicit Regularization in Perturbed Deep Matrix Factorization: Spectral Conditions and Stability

**Authors:** Jingzhe Wang, Hung-Hsu Chou

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28613v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28613v1)

**Summary:** This paper studies the stability of low-rank implicit regularization in perturbed deep matrix factorization, where the target matrix is corrupted by a noise matrix. We first derive sufficient spectral conditions under which gradient descent exhibits a low-rank phase in the noiseless setting. These conditions show how the target spectrum, initialization, and step size jointly determine the existence of a nonempty low-rank interval. We then analyze the perturbed gradient descent dynamics, proving ...

---

### 36. Learning High-Dimensional Parity Functions with Product Networks using Gradient Descent

**Authors:** Guillaume Larue, Louis-Adrien Dufrène, Quentin Lampin, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28612v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28612v1)

**Summary:** Parity functions are fundamental Boolean operations with critical applications across machine learning, cryptography, and error correction. Yet, learning high-dimensional parity functions poses significant challenges: in a general setting, standard neural network architectures typically require exponential sample complexity, making gradient-based optimization intractable for large number of inputs $N$. We demonstrate that compact product-based neural architectures combined with stochastic data s...

---

### 37. Online Irregular Multivariate Time Series Forecasting via Uncertainty-Driven Dual-Expert Calibration

**Authors:** Haonan Wen, Hanyang Chen, Songhe Feng

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28603v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28603v1)

**Summary:** Irregular multivariate time series forecasting is critical in many real-world applications, where time series are irregularly sampled and exhibit dynamically evolving missingness patterns. Although existing methods perform well in offline settings, they often suffer from significant performance degradation when deployed online due to dynamic shifts in data distribution. Maintaining forecasting capability in such dynamic scenarios typically necessitates online adaptation techniques. Since irregul...

---

### 38. Transformers Provably Learn to Internalize Chain-of-Thought

**Authors:** Yixiao Huang, Hanlin Zhu, Zixuan Wang, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28600v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28600v1)

**Summary:** Chain-of-Thought (CoT) prompting substantially improves the sample efficiency of transformers, reducing the complexity of tasks like parity learning from exponential to polynomial in the input length. However, generating explicit reasoning steps at inference is computationally expensive. Implicit Chain-of-Thought (ICoT) has emerged as a promising empirical remedy that trains models to internalize intermediate steps within their hidden states, but its theoretical foundations remain poorly underst...

---

### 39. Position: Retire the "Positive Backdoor" Label -- Secret Alignment Requires Strict and Systematic Evaluation

**Authors:** Jianwei Li, Jung-Eun Kim

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28597v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28597v1)

**Summary:** This position paper argues that the AI/ML community should stop overclaiming and retire the label "positive backdoor," and instead treat trigger-activated hidden behaviors as Secret Alignment. Crucially, protective claims based on Secret Alignment should be presumed not secure by default unless supported by rigorous, standardized evaluation. The Private AI era, enabled by open-weight LLMs and accessible training/inference stacks, turns language models into privately owned digital assets, creatin...

---

### 40. Dark Quest II: A Wide-Coverage Neural Network Emulator of the Nonlinear Matter Power Spectrum Across Extended Cosmologies

**Authors:** Satoshi Tanaka, Takahiro Nishimichi, Yosuke Kobayashi

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28596v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28596v1)

**Summary:** \textsc{DarkEmulator2} is a neural network emulator of the nonlinear matter power spectrum in a nine-dimensional $w_0 w_a νo \mathrm{CDM}$ parameter space, developed as the emulator component of the \textsc{Dark Quest II} (DQ2) program. It is trained on simulations generated with the \textsc{Ginkaku} code, whose numerical implementation, accuracy tests, and post-processing pipeline are described in the companion paper. The design follows a unified strategy: in addition to the cosmological parame...

---

### 41. PLS in the Mirror of Self-Attention

**Authors:**  Jiangsheng,  You

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28592v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28592v1)

**Summary:** This note provides an interesting observation on casting partial least square (PLS) as a linearized self-attention so that PLS may be studied within the neural network paradigm. On the other hand, the dimensionality reduction and selection of predictors in PLS may indicate that self-attention includes certain degree of dimensionality normalization toward improved learning.

---

### 42. Thinned Mean Field Langevin Dynamics

**Authors:** Zonghao Chen, Heishiro Kanagawa, François-Xavier Briol, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28589v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28589v1)

**Summary:** Several important learning tasks can be formulated as minimizing an entropy-regularized objective over an appropriate space of probability distributions. Mean-field Langevin dynamics (MFLD) facilitate computation in this general context, casting the minimizer as the invariant distribution of a McKean--Vlasov process, which can be numerically discretized using $N$ particles and thus simulated. However, simulating this interacting particle system has computational complexity of order $N^2$. Motiva...

---

### 43. Outer-Momentum Restarting in High-Dimensional Two-Phase Optimization

**Authors:** Kristi Topollai, Allan Ma, Tolga Dimlioglu, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28585v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28585v1)

**Summary:** Communication-efficient distributed optimizers such as DiLoCo reduce synchronization costs by letting workers perform many local updates before aggregating their progress with an outer momentum optimizer. Recent theory suggests that the outer optimizer acts on an effective spectrum induced by the inner optimization loop, and that the choice of outer momentum controls how progress from local updates is accumulated across communication rounds. We study periodic restarting of the outer momentum as ...

---

### 44. SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving

**Authors:** Kangyu Wu, Peng Cui, Guoxi Chen, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28583v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28583v1)

**Summary:** Ensuring both safety and efficiency in decision-making for autonomous driving systems remains a fundamental challenge. Traditional Deep Reinforcement Learning (DRL) suffers from unsafe random exploration and slow convergence, while Large Language Models (LLMs) demonstrate inherent latency in real-time inference operations. To address these limitations, this paper proposes SARAD, a novel safety-aware hybrid framework that synergizes LLMs and DRL for autonomous driving. SARAD substitutes the rando...

---

### 45. A Generalized Tikhonov Layer for Interpretable-by-design Graph Neural Networks

**Authors:** Nicolas Tremblay, Benjamin Ricaud, Filippo Maria Bianchi

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28578v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28578v1)

**Summary:** We propose the Tikhonov layer, a graph neural network layer that is interpretable by design: once trained, its learned parameters directly reveal which node features and which aspects of the graph topology were leveraged for prediction. In practice, the layer's propagation matrix takes the closed-form $R = (p(L)+Q)^{-1} Q$, where $L$ is the normalized graph Laplacian, $Q = diag(q_1,...,q_n)$ a learnable diagonal matrix of positive node-importance scores, and $p(\cdot)$ a learnable polynomial. Fo...

---

### 46. Continual Model Routing in Evolving Model Hubs

**Authors:** Jack Bell, Giacomo Carfì, Gerlando Gramaglia, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28577v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28577v1)

**Summary:** AI model hubs provide access to a rapidly growing collection of powerful pre-trained models, enabling off-the-shelf mixture-of-experts systems with different routing strategies. However, this rapid growth poses two fundamental challenges: scaling model selection across thousands of experts and continually updating routing mechanisms as new models and tasks are introduced. In this paper, we formalise this setting as Continual Model Routing (CMR) and propose CMRBench, a new large-scale benchmark s...

---

### 47. Efficient Pre-Training of LLMs through Truncated SVD Layers

**Authors:** Kaivan Kamali, Kajetan Schweighofer, Hormoz Shahrzad, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28573v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28573v1)

**Summary:** The massive scaling of Large Language Models (LLMs) has made pretraining increasingly cost-prohibitive. While low-rank representation and orthonormal weight matrices could in principle reduce parameter counts and computational overhead, most existing methods rely on static rank selection and do not enforce weight orthonormality due to high computational cost. This paper introduces TSVD, a framework that maintains low rank and strict orthonormality throughout the training process. It utilizes a s...

---

### 48. Semantic Optimal Transport for Sparse Autoencoder Feature Matching and Circuit Compression

**Authors:** Tue M. Cao, Nguyen Do, My T. Thai

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28567v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28567v1)

**Summary:** Sparse autoencoders (SAEs) have become a central tool for interpreting language models. However, two key SAE analyses that remain difficult to scale are (1) matching semantically similar features across multi-layers and (2) compressing large feature circuits into interpretable supernodes. Although these have been treated as separate problems, we show that both are instances of a more fundamental challenge, which we frame as the estimation of semantic distances between SAE features that lie on di...

---

### 49. Tree of Thoughts as a Classical Heuristic Search Problem: Formal Foundations and Design Patterns

**Authors:** Guni Sharon

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28566v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28566v1)

**Summary:** Large Language Models (LLMs) have demonstrated remarkable reasoning capabilities, yet their standard generation process -- auto-regressive token prediction -- is inherently myopic and prone to cascading errors. To address this, the Tree-of-Thoughts (ToT) framework creates a search space over intermediate reasoning steps, allowing search models to explore, look ahead, and backtrack. However, current ToT research remains fragmented across Natural Language Processing and Automated Planning communit...

---

### 50. A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models

**Authors:** Aditya Kommineni, Emily Zhou, Kleanthis Avramidis, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28563v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28563v1)

**Summary:** Evaluating foundation models under appropriate adaptation settings is essential for understanding the quality and transferability of the learned representations. Recent EEG foundation models have demonstrated promising transfer capabilities across tasks and datasets, motivating their growing use in neurotechnology and clinical applications. However, these models are typically evaluated under full fine-tuning on well-curated downstream datasets, a setting that does not reflect biomedical domain c...

---

## cs.NE

**50 papers**

### 1. Preference-Shaped Expected Hypervolume and R2 Improvement: Exact Computation and Monotonicity

**Authors:** Michael T. M. Emmerich

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28746v1)

**Summary:** This paper studies preference-shaped expected improvement criteria for Bayesian multiobjective optimization. We consider two indicator families which are often used for similar algorithmic purposes, but which are geometrically different. The hypervolume indicator is based on a dystopian reference point and measures dominated volume in objective space. The R2 indicator is based on a utopian point and evaluates approximation sets through weighted Tchebycheff scalarization envelopes. The purpose of...

---

### 2. BIRDNet: Mining and Encoding Boolean Implication Knowledge Graphs as Interpretable Deep Neural Networks

**Authors:** Tirtharaj Dash

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28739v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28739v1)

**Summary:** Tabular data in knowledge-rich domains often carries a latent prior in the form of Boolean implication relationships (BIRs) between pairs of features. We mine such relationships with a sparse-exception binomial test. The mined implications form a typed directed graph, equivalent to a propositional rule base of 2-literal clauses. We encode this graph as the connectivity of a layered neural network, called BIRDNet, in which each hidden unit corresponds to one mined rule and binds only to its two f...

---

### 3. A Fresh Look at Lamarckian Evolution and the Baldwin Effect

**Authors:** Inès Benito, Johannes F. Lutzeyer, Benjamin Doerr

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28703v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28703v1)

**Summary:** Baldwinian and Lamarckian evolution have existed for a long time in evolutionary algorithms (EAs) without ever dominating the academic literature or practical applications. In this work, we use modern empirical and theoretical methods to revisit Lamarckian and Baldwinian evolution and rigorously compare them with the generic Darwinian evolution. On the empirical side, we run a comprehensive suite of experiments on graphs from six different datasets from the recent GraphBench benchmark on Maximum...

---

### 4. CLANE: Continual Learning of Actions on Neuromorphic Hardware from Event Cameras

**Authors:** Elvin Hajizada, Michael Neumeier, Edward Paxon Frady, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28387v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28387v1)

**Summary:** Recognizing and continuously learning novel human actions without forgetting prior classes is a requirement for emerging AR/VR and robotics applications. For these applications, both on-device processing and learning are essential for privacy and low-latency adaptation. Event cameras address the efficiency of visual sensing with sparse, asynchronous output that is naturally compatible with neuromorphic processing. Yet no prior system has deployed a continual on-device learning pipeline for event...

---

### 5. Improving Evaluation of Recombination-based Cartesian Genetic Programming

**Authors:** Duy Long Tran, Anja Jankovic, Marie Anastacio, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28353v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28353v1)

**Summary:** Cartesian Genetic Programming has traditionally been using mutation as its main and often sole genetic operator to drive evolutionary search. Despite advancements in recent years, recombinationbased approaches have long been avoided, due to apparent lack of performance gains. This study examines two recently suggested recombination-based operators, subgraph crossover and discrete phenotypic recombination on SRBench, a benchmarking platform for symbolic regression. Using the implementations provi...

---

### 6. Learning to Assess the Reliability of Number-of-Runs Estimation in Stochastic Optimization

**Authors:** Sara Gjorgjieva, Eva Tuba, Tome Eftimov

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28309v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28309v1)

**Summary:** In large-scale benchmarking of stochastic optimization algorithms, the key challenge is no longer whether repeated runs are needed for reliability, but how to determine when sufficient evidence has been collected without incurring unnecessary computational cost. We study a learning-based extension of a recent empirical online heuristic that adaptively estimates the required number of runs using outlier handling and skewness-based symmetry checks. Using annotated outcomes from 132{,}000 Nevergrad...

---

### 7. Performance and Explainability Requirements of Evolutionary Algorithms in Real-World Physics-Informed Optimization

**Authors:** Helena Stegherr, Michael Heider, Nils Meyer, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28164v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28164v1)

**Summary:** Evolutionary computation offers a variety of tools to solve complex real-world optimization problems. However, research often focuses on smaller, simplified problems and optimization algorithms that sometimes miss expectations in real-world scenarios. Additionally, trust in the applied algorithm and the solutions it provides is often essential in such settings, but requires an understanding of the search process itself. This leads to evolutionary computation often not being seriously considered ...

---

### 8. On the Structural (Dis)Agreement of Landscape Representations in Black-Box Optimization

**Authors:** Sara Gjorgjieva, Eva Tuba, Barbara Koroušić Seljak, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28121v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28121v1)

**Summary:** Landscape feature representations play a central role in automated algorithm selection and meta-learning for black-box optimization, yet little is known about how different representations agree (or disagree) in the structures they impose on problem spaces. This paper presents a systematic unsupervised evaluation of four state-of-the-art representations (ELA, DeepELA, TransOptAS, and DoE2Vec) using a diverse set of affine combinations of BBOB functions (MA-BBOB). By applying extensive clustering...

---

### 9. Signal-to-Noise Ratio and Sample Size Govern Representational Alignment in Neural Networks

**Authors:** Ali Hussaini Umar, Alessandro Laio

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26973v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26973v1)

**Summary:** Neural networks are known to develop latent representations that are $aligned$, namely structurally similar across networks trained with different architectures, training protocols, or training datasets. We study this phenomenon in a controlled setting, where we train an ensemble of networks on regression and classification tasks using training sets perturbed by independent realizations of a noise process. We show that the signal-to-noise ratio (SNR) and the training sample size influence the al...

---

### 10. Evolutionary Data Theory: On the Similarities between Data Problems and Evolutionary Games

**Authors:** Philipp Wissgott

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26685v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26685v1)

**Summary:** Applying the concepts and formalisms from Evolutionary Game Theory to the data regime, the fundamental paradigms of Evolutionary Data Theory are introduced. Interpreting data in matrix form as evolutionary entities, input data is mapped to genes and organisms. Steered by genetic fitness and two evolutionary strategies, Dominant-Balanced and Altruistic-Selfish, data records and features conduct an evolutionary game. It is shown that this evolutionary interpretation remains universally meaningful,...

---

### 11. Why Prompt Optimization Works, and Why It Sometimes Doesn't: A Causal-Inspired Edit-Level Analysis

**Authors:** Shuzhi Gong, Hechuan Wen

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26655v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26655v1)

**Summary:** Automated prompt optimization methods (e.g., DSpy, TextGrad) can substantially improve the performance of large language model (LLM), however, their generalization ability across different tasks remains underperformed. In practice, the superiority of the optimized prompt on one benchmark often fails to transfer to another, and this limitation persists even when switching across different LLM backbones. To investigate the underexplored sources of heterogeneity in prompt performance, we conduct a ...

---

### 12. Constitutional Arms Races in the Public Goods Game: Co-Evolving LLM Constitutions Under Cooperation-Defection Pressure

**Authors:** Ujwal Kumar, Arth Singh, Hershraj Niranjani, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26448v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26448v1)

**Summary:** Frontier LLM agents engage in blackmail, sabotage, and document leaks under goal conflicts in agentic settings, exposing limitations of alignment methods built around single-agent or cooperative assumptions. Recent work shows LLM-guided evolutionary search can discover effective cooperative constitutions, but two properties of the adversarial setting remain uncharacterized: whether the fitness function actually induces adversarial pressure, and whether the LLM mutation operator behaves reliably ...

---

### 13. Unified Neural Scaling Laws

**Authors:** Ethan Caballero, Priyank Jaini, David Krueger, et al.

**Published:** 2026-05-25

🔗 [Paper](http://arxiv.org/abs/2605.26248v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26248v1)

**Summary:** We present a functional form (that we refer to as a Unified Neural Scaling Law (UNSL)) that accurately models and extrapolates the scaling behaviors of deep neural networks as multiple dimensions all vary simultaneously (i.e. how the evaluation metric of interest varies as one simultaneously varies the number of model parameters, training dataset size, number of training steps, number of inference steps, amount of compute, and various hyperparameters) for various architectures and for each of va...

---

### 14. A Scalable Benchmark Test Suite for Dynamic Multi-Objective Optimization with a Changing Number of Objectives

**Authors:** Ke Shang, Zhiyun Xiao, Yuxuan Liu, et al.

**Published:** 2026-05-25

🔗 [Paper](http://arxiv.org/abs/2605.25785v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25785v1)

**Summary:** Dynamic multi-objective optimization with a changing number of objectives has recently attracted increasing attention due to its relevance to real-world problems whose evaluation criteria may evolve over time. However, existing benchmark test suites for this problem setting suffer from a fundamental limitation: when the number of objectives changes, the objective functions themselves also change implicitly. This makes it difficult to isolate and evaluate an algorithm's capability to handle dynam...

---

### 15. Positivity in classical enumerative geometry: a case study in synchronized AI-assisted mathematics

**Authors:** Gergely Bérczi, László M. Fehér

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25271v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25271v1)

**Summary:** We study the symmetric polynomial $\prod_{α\in A_{n,d}}\bigl(1+α_1 x_1+\cdots+α_n x_n\bigr)$ where $A_{n,d}:=\{α\in\mathbb{Z}_{\ge 0}^n:|α|=d\}$, which is the total Chern class of $\mathrm{Sym}^d(\mathbb{C}^n)$, viewed as a torus representation whose Chern roots are the weights $α_1 x_1+\cdots+α_n x_n$ for $α\in A_{n,d}$. Its homogeneous degree-$k$ part $c_k(n,d)$ is the $k$-th Chern class of $\mathrm{Sym}^d(\mathbb{C}^n)$. These Chern classes, together with their coefficients in various symmetr...

---

### 16. Growing a Neural Network in Breadth, Depth, and Time

**Authors:** Eivinas Butkus, Kedar Garzón Gupta, Nikolaus Kriegeskorte

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25174v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25174v1)

**Summary:** Spatial and temporal resource constraints are critical for both biological and artificial intelligent systems. Here we define differentiable cost terms for breadth, depth, and time within a recurrent convolutional neural network conceived as a finite subset of an infinite lattice. We optimize these costs jointly with task errors via backpropagation. We set different pressures on breadth, depth, and time, which leads to diverse computational graphs emerging organically through training. We find t...

---

### 17. Anarchy in the swarm: Testing informed and uninformed diversity-enhancing mechanisms within PSO framework

**Authors:** Piotr Urbańczyk, Aleksandra Urbańczyk

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25093v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25093v1)

**Summary:** Particle Swarm Optimization (PSO) frequently suffers from premature convergence. This paper introduces a family of problem-informed diversity-enhancing strategies that manipulate the swarm's social and cognitive components. These include opposing-best strategies that repel particles from optimal regions, negative learning strategies that guide exploration toward poor solutions, and reverse learning strategies that push particles away from inferior regions. These socio-cognitive mechanisms are ev...

---

### 18. Cultivating Machine Intelligence: The OMEGA Shift from Top-Down Optimization to Autopoietic Cognitive Ecologies

**Authors:** Ata G. Zare

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25062v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25062v1)

**Summary:** The dominant artificial intelligence paradigm trains neural architectures via gradient descent against proxy objectives and reinforcement learning from human feedback. While remarkably capable, this top-down optimization inherently generates structural failure modes, including hallucination, sycophancy, reward hacking, and alignment fragility, which represent paradigmatic limitations rather than mere engineering defects. In response, we introduce RECLAIM (Recursive, Ecological, Cognitive, Lifeli...

---

### 19. Convex-Neural RRT*: Fast and Reliable Learning-Guided Sampling for High-Quality Robot Path Planning

**Authors:** Hichem Cheriet, Badra Khellat Kihel, Samira Chouraqui, et al.

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25006v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25006v1)

**Summary:** Sampling-based algorithms for robot path planning offer probabilistic completeness and strong empirical convergence properties across environments with diverse obstacle configurations. However, in practice, these methods often require many iterations to obtain high-quality solutions. This paper proposes Convex-Neural RRT*, an enhanced RRT* variant that incorporates neural guidance to predict informative waypoint regions near high-quality paths. Convex candidate regions are extracted from these p...

---

### 20. Memory Uncertainty Relation and Harmonic Memory in Random Recurrent Networks

**Authors:** Taichi Haruna, Kohei Nakajima

**Published:** 2026-05-23

🔗 [Paper](http://arxiv.org/abs/2605.24628v1) | 📄 [PDF](https://arxiv.org/pdf/2605.24628v1)

**Summary:** We present an inequality that bounds the short-term memory capability of dynamical systems from below. It can be interpreted as an uncertainty relation between a measure of short-term memory and that of the size of state fluctuations induced by input signals. The lower bound can be achieved by a readout weight and thus represents a suboptimal memory called harmonic memory. We examine analytically and numerically the inequality in a number of reservoir systems subject to input noise. We illustrat...

---

### 21. UniSpike: Accelerating Spiking Neural Networks on Neuromorphic Systems via Eliminating Address Redundancy

**Authors:** Qinghui Xing, Zhuo Chen, Xin Du, et al.

**Published:** 2026-05-22

🔗 [Paper](http://arxiv.org/abs/2605.23796v1) | 📄 [PDF](https://arxiv.org/pdf/2605.23796v1)

**Summary:** Many-core neuromorphic systems accelerate Spiking Neural Networks (SNNs), yet their packet-based spike communication can spend substantial traffic and energy repeatedly transmitting destination addresses. This overhead is amplified by the small payload of spike packets: in representative workloads, duplicate address transmissions account for up to 49% of the total traffic. This paper presents UniSpike, a hardware-software co-design that removes address redundancy by aggregating spikes destined f...

---

### 22. Preisach Attention: A Hysteretic Model of Sequential Memory

**Authors:** Piotr Frydrych

**Published:** 2026-05-22

🔗 [Paper](http://arxiv.org/abs/2605.23603v1) | 📄 [PDF](https://arxiv.org/pdf/2605.23603v1)

**Summary:** We introduce the Preisach Attention Layer (PAL), a novel sequence modelling architecture grounded in the classical Preisach hysteresis operator from mathematical physics. PAL replaces the softmax attention mechanism with a binary relay operator parameterised by learned activation and deactivation thresholds, maintaining a stack of local extrema as its internal state. A single-layer PAL-Transformer with O(1) depth is Turing-complete under arbitrary precision arithmetic, achievable through simulat...

---

### 23. SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks

**Authors:** Yukai Yang, Chenxi Qin, Jungang Li, et al.

**Published:** 2026-05-22

🔗 [Paper](http://arxiv.org/abs/2605.23188v1) | 📄 [PDF](https://arxiv.org/pdf/2605.23188v1)

**Summary:** Spiking Neural Networks (SNNs) provide an energy-efficient paradigm for visual recognition. We present SpikingMoE, which integrates a spike-driven Transformer with a Mixture-of-Experts (MoE) framework for dynamic computation. Inspired by the lateral geniculate nucleus (LGN), a spike-driven prompt (SDprompt) enables input-dependent expert routing in a biologically plausible manner. By replacing standard MLPs with spike-compatible expert modules and enforcing binary spike communication, SpikingMoE...

---

### 24. Vector Policy Optimization: Training for Diversity Improves Test-Time Search

**Authors:** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22817v1)

**Summary:** Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Po...

---

### 25. Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection

**Authors:** Giancarlo P. Gamberi, Calebe P. Bianchini

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22527v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22527v1)

**Summary:** Negative Selection Algorithms (NSAs), inspired by the self/non-self discrimination mechanism of the human immune system, have been widely employed in anomaly detection. However, their effectiveness is often constrained by the efficiency of detector generation. This paper presents the Quantum Genetic Negative Selection Algorithm (QGNSA), a novel approach that integrates a Quantum Genetic Algorithm (QGA) into the EvoSeedRNSA algorithm, replacing its classical evolutionary optimization process. The...

---

### 26. Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings Across Human fMRI and Macaque Electrophysiology

**Authors:** Nils Leutenegger

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22401v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22401v1)

**Summary:** Does the relationship between learning rules and brain alignment generalize across species? We extend our prior finding that untrained CNNs match backpropagation at human V1 by testing the same five learning rules against macaque electrophysiology. The rules are backpropagation (BP), feedback alignment (FA), predictive coding (PC), spike-timing-dependent plasticity (STDP), and an untrained random-weights baseline. The macaque data come from two datasets: MajajHong2015 (V4/IT, 3,200 stimulus pres...

---

### 27. Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions

**Authors:** Gabriel Kronberger, Fabricio Olivetti de Franca, Deaglan J. Bartlett, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22374v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22374v1)

**Summary:** Symbolic regression with genetic programming (GPSR) may suffer from overfitting and structural bloat, especially when noise is present. In this paper we evaluate description length (DL) and fractional Bayes factor (FBF) criteria as principled, data-efficient alternatives to heuristics for selecting compact expressions that generalise well. We implement DL using a Fisher-information-based parameter encoding and compare it to AIC and BIC across multiple datasets, including noisy synthetic benchmar...

---

### 28. Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture

**Authors:** Joy Bose

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22206v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22206v1)

**Summary:** The Thousand Brains Theory (TBT) and its open-source Monty framework model object recognition through sensorimotor inference -- identifying objects by actively moving a sensor across their surface and building evidence contact by contact. The current implementation encodes each contact as a dense floating-point vector. While Monty tracks inter-step displacement and accumulates evidence across contacts, it treats the feature activation pattern at each contact as an unordered set - the directional...

---

### 29. Exact Uniform L1 Spacing for Solow-Polasky Diversity on Lines and Ordered Pareto Fronts

**Authors:** Michael T. M. Emmerich, Mahboubeh Nezhadmoghaddam, Jesús Guillermo Falcón Cardona

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.21922v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21922v1)

**Summary:** We study fixed-cardinality maximization of the inverse-matrix Solow--Polasky diversity, equivalently finite metric magnitude for the exponential kernel, on one-dimensional and ordered metric sets. The analysis starts from the known finite-line gap formula for the exponential kernel, which writes the excess inverse-matrix diversity as a sum of functions of consecutive gaps. Building on this formula, the main interval theorem proves that, for every $k\geq 2$, the unique maximizing $k$-point subset...

---

### 30. Engineering Hybrid Physics-Informed Neural Networks for Next-Generation Electricity Systems: A State-of-the-Art Review

**Authors:** Joseph Nyangon

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.21903v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21903v1)

**Summary:** The integration of machine learning with domain-specific physics is transforming the design, monitoring, and control of electricity systems, where data scarcity, limited interpretability, and the need to enforce physical laws constrain purely data-driven models. Physics-informed machine learning (PIML) addresses these limitations by embedding governing equations directly into the learning process, yielding accurate, efficient, and scalable solutions for Industry 4.0 applications. This article re...

---

### 31. Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos

**Authors:** Lucas Fernandez Sarmiento

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21648v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21648v1)

**Summary:** We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos. Dropout shifts the perfect-alignment fixed point, making the depth scale for information propagation finite even at critical initialization. We derive critical and crossover scaling laws for correlation decay and establish that smooth activations and kinked, ReLU-like activations constitute distinct universality classes, with different critical exponents and a universal two-parameter ...

---

### 32. Approximation Theory for Neural Networks: Old and New

**Authors:** Soumendu Sundar Mukherjee, Himasish Talukdar

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21451v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21451v1)

**Summary:** Universal approximation theorems provide a mathematical explanation for the expressive power of neural networks. They assert that, under mild conditions on the activation function, feedforward neural networks are dense in broad function classes, such as continuous functions on compact subsets of $\mathbb{R}^d$, $L^p$ spaces, or Sobolev spaces. Over the past four decades, these qualitative universality results have evolved into a rich quantitative theory addressing approximation rates, parameter ...

---

### 33. How to Build Marcus's Algebraic Mind: Algebro-Deterministic Substrate over Galois Fields

**Authors:** Hiroyuki Chuma, Kanji Otsuk, Yoichi Sato

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21379v2) | 📄 [PDF](https://arxiv.org/pdf/2605.21379v2)

**Summary:** In The Algebraic Mind, Gary Marcus identified three components essential for any adequate cognitive architecture: operations over variables, recursively structured representations, and a distinction between mental representations of individuals and kinds. He argued that standard multilayer perceptrons supported none of these, acknowledging that a neural implementation using registers and treelets, constructed via developmental programs rather than gradient descent, remained a programmatic conjec...

---

### 34. Genetic Programming with Transformer-Based Mutation for Approximate Circuit Design

**Authors:** Ondrej Galeta, Lukas Sekanina

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21055v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21055v1)

**Summary:** A recent trend is to leverage machine learning models to improve the evolutionary design and optimization process. We propose a novel transformer-based mutation operator for Cartesian genetic programming (CGP) for the automated design of approximate arithmetic circuits. We introduce a hybrid scheme for CGP in which the proposed mutation operator is switched with the standard mutation operator to prevent stagnation of the circuit approximation process. We also develop a new training scheme for th...

---

### 35. Convergence Analysis of Evolution Strategies for Mixed-Integer Optimization

**Authors:** Ryoki Hamano, Kento Uchida, Shinichi Shirakawa

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21000v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21000v1)

**Summary:** Mixed-integer extensions of evolution strategies (ES) that discretize selected coordinates of sampled continuous vectors often impose a lower bound on the standard deviation of integer variables to prevent premature convergence. While these methods show promising empirical results, this handling can slow the convergence of continuous variables, and its impact has lacked a clear theoretical account. In this paper, we provide a convergence analysis of evolution strategies for mixed-integer optimiz...

---

### 36. Privacy-Preserving Distributed Optimization Under Time Constraints Using Secure Multi-Party Computation and Evolutionary Algorithms

**Authors:** Sebastian Gruber, Tobias Harzfeld, Christoph G. Schuetz, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20944v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20944v1)

**Summary:** In distributed optimization, multiple parties collaborate to find an optimal solution to a problem. Privacy-preserving distributed optimization uses techniques, such as secure multi-party computation (MPC), to protect the private inputs of each party. In time-critical settings, the runtime overhead introduced by privacy-preserving computations may prevent the optimization from finishing within the deadline. This paper presents an approach for privacy-preserving distributed optimization in time-c...

---

### 37. E-ReCON: An Energy- and Resource-Efficient Precision-Configurable Sparse nvCIM Macro for Conventional and Spiking Neural Edge Inference

**Authors:** Ankit Kumar Tenwar, Mukul Lokhande, Santosh Kumar Vishvakarma

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.20717v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20717v1)

**Summary:** This work presents E-ReCON, a 16 Kb energy and resource-efficient digital compute-in-memory (DCIM) macro based on a compact 3T1R ReRAM bitcell for edge-AI inference. The proposed bitcell occupies only 0.85 um^2 and supports reliable AND-based in-memory multiplication for both conventional convolutional neural network (CNN) and spiking neural network (SNN) workloads. To reduce accumulation overhead, a novel interleaved 10T/28T adder tree is introduced, reducing transistor count and power consumpt...

---

### 38. Weight Decay Regimes in Grokking Transformers: Cheap Online Diagnostics

**Authors:** Lucky Verma

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20441v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20441v1)

**Summary:** Transformers trained on modular arithmetic exhibit sharp transitions between memorization, generalization, and collapse. We show that weight decay acts as a scalar empirical control parameter for these regimes, and introduce two cheap online diagnostics, mean pairwise attention-head cosine similarity and entropy standard deviation, that track training dynamics from attention activations alone and complement loss-landscape diagnostics at lower compute cost. Across eleven experimental conditions a...

---

### 39. What Do Evolutionary Coding Agents Evolve?

**Authors:** Nico Pelleriti, Sree Harsha Nelaturu, Zhanke Zhou, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20086v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20086v1)

**Summary:** Recent work pairs LLMs with evolutionary search to iteratively generate, modify, and select code using task-specific feedback. These systems have produced strong results in mathematical discovery and algorithm design, yet a fundamental question remains: what do they actually evolve? Progress is typically summarized by the best score a run reaches under a task-specific evaluator, but that score can reflect several different mechanisms: new algorithmic structure, re-tuning an existing strategy, re...

---

### 40. Training Neural Networks with Optimal Double-Bayesian Learning

**Authors:** Vy Bui, Hang Yu, Karthik Kantipudi, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20009v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20009v1)

**Summary:** Backpropagation with gradient descent is a common optimization strategy employed by most neural network architectures in machine learning. However, finding optimal hyperparameters to guide training has proven challenging. While it is widely acknowledged that selecting appropriate parameters is crucial for avoiding overfitting and achieving unbiased outcomes, this choice remains largely based on empirical experiments and experience. This paper presents a new probabilistic framework for the learni...

---

### 41. Reconfigurable Nonlinear Photonic Networks for In-Situ Learning and Memory Formation via Driven-Dissipative Dynamics

**Authors:** Isaac Yorke

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19911v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19911v1)

**Summary:** Photonic neuromorphic computing offers a promising route to overcoming the limitations of conventional von Neumann architectures by exploiting the high bandwidth, low latency, and massive parallelism of optical systems. However, most existing implementations rely on fixed dynamical substrates such as classic reservoir computing, where learning is restricted to external readout layers and memory is limited to transient fading effects. In this work, I propose a Reconfigurable Nonlinear Photonic De...

---

### 42. Multi-population Diversity-guided Genetic Algorithm for Feature Selection in Network Intrusion Detection

**Authors:** Chunzhen Li

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19864v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19864v1)

**Summary:** Network Intrusion Detection System is a critical means of ensuring cybersecurity. However, existing Genetic Algorithm-based feature selection methods face several limitations when dealing with high-dimensional redundant traffic features. For example, population diversity is difficult to maintain, and evolutionary operators lack guidance. To solve these problems, this study proposes the Multi-Population Diversity-Guided Genetic Algorithm (MPDGGA). First, we build a chained multi-population evolut...

---

### 43. optimize_anything: A Universal API for Optimizing any Text Parameter

**Authors:** Lakshya A Agrawal, Donghyun Lee, Shangyin Tan, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19633v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19633v1)

**Summary:** Can a single LLM-based optimization system match specialized tools across fundamentally different domains? We show that when optimization problems are formulated as improving a text artifact evaluated by a scoring function, a single AI-based optimization system-supporting single-task search, multi-task search with cross-problem transfer, and generalization to unseen inputs-achieves state-of-the-art results across six diverse tasks. Our system discovers agent architectures that nearly triple Gemi...

---

### 44. Closed-form predictive coding via hierarchical Gaussian filters

**Authors:** Aleksandrs Baskakovs, Sylvain Estebe, Kenneth Enevoldsen, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20293v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20293v1)

**Summary:** Predictive coding (PC) offers a local and biologically grounded alternative to backpropagation in the training of artificial neural networks, yet to date, it remains slower, and performance degrades sharply as network depth increases. We trace both problems to a single simplification: current PC networks fix the precision matrix to the identity, discarding precision-weighted prediction errors that the variational derivation requires to be fast, local, and Bayesian. We close this gap by expressin...

---

### 45. Scalable, Energy-Efficient Optical-Neural Architecture for Multiplexed Deepfake Video Detection

**Authors:** Parnian Ghapandar Kashani, Shiqi Chen, Aydogan Ozcan

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19360v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19360v1)

**Summary:** The rapid proliferation of AI-generated visual media has created an urgent need for efficient, trustworthy deepfake detection systems. However, existing deep learning-based detection methods rely on computationally intensive and energy-demanding inference algorithms, limiting their scalability. Here, we present a hybrid digital-analog deepfake video detection framework that combines a lightweight digital front-end with a spatially multiplexed optical decoding back-end for massively parallel anal...

---

### 46. Information Processing Capacity of Stationary Physical Systems: Theory, Data-efficient Estimation Methods, and Photonic Demonstration

**Authors:** Rahul Uma Ramachandran, Serge Massar

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19152v2) | 📄 [PDF](https://arxiv.org/pdf/2605.19152v2)

**Summary:** Physical computing systems provide a promising route toward hardware-native machine learning, but their computational capabilities remain difficult to characterize in a principled, task-independent, and data-efficient way. We extend the Information Processing Capacity (IPC) framework to stationary physical computing systems and establish several fundamental results: individual capacities are bounded between zero and one, their sum over a complete basis is bounded by the number of readouts, and n...

---

### 47. GOAL: Graph-based Objective-Aligned Diffusion Solvers for Dynamic Multi-Objective Optimization

**Authors:** Xingyu Li

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19119v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19119v1)

**Summary:** Existing neural combinatorial optimization solvers frame solution search as imitation of optimal decisions, inherently limiting their utility to single-objective minimization and static constraints. We propose GOAL, a conditioned diffusion solver over relational graph representations that enables controllable decision generations by conditioning on human-specified objectives. We introduce a heterogeneous graph encoding in which distinct edge types, corresponding to different classes of constrain...

---

### 48. Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data

**Authors:** Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18557v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18557v1)

**Summary:** The brain learns abstract representations of high-dimensional sensory input, but the plasticity rules that enable such learning are unknown. We study biologically plausible algorithms on the Random Hierarchy Model (RHM), an artificial dataset designed to investigate how deep neural networks learn the intrinsic hierarchical structure of high-dimensional data. We focus on two types of local learning rules that avoid both a long convergence time and the use of a symmetric error network. The first t...

---

### 49. When Fireflies Cluster; Enhancing Automatic Clustering via Centroid-Guided Firefly Optimization

**Authors:** MKA Ariyaratne, Azwirman Gusrialdi, Yury Nikulin, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18460v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18460v1)

**Summary:** This work presents a novel variant of the Firefly Algorithm (FA) for data clustering, addressing limitations of traditional methods like K-Means that struggle with non-uniform cluster shapes, densities, and the need for pre-defining the number of clusters. The proposed algorithm introduces a centroid movement strategy and a multi-objective fitness function that balances compactness, separation, and a novel TSP-based navigation penalty. It automatically estimates the optimal number of clusters an...

---

### 50. Mapping the Fitness Landscape: A Structure-Guided Approach to Multi-Modal Optimization

**Authors:** Meng Xiang, Pei Yan

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18351v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18351v1)

**Summary:** Multimodal optimization requires finding many optima rather than merely keeping a diverse population. Yet most niching-based evolutionary algorithms rely on distances or density estimators without explicitly recovering the underlying peak--basin organization in the decision space, which can lead to pseudo-multimodality: many distinct individuals ultimately collapse into only a few basins. We introduce Chaotic Landscape-Decoding Evolution (CLDE), a decision-space-centric framework that turns mult...

---

## q-bio.NC

**50 papers**

### 1. VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading

**Authors:** Jinzhou Wu, Zhengwu Ma, Jixing Li, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28818v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28818v1)

**Summary:** Large language models (LLMs) have become increasingly useful computational models of human language processing, but it remains unclear whether vision-language learning makes text representations more human-like during natural reading. Here, we address this question by comparing tightly matched LLM and vision-language model (VLM) pairs under a strictly text-only setting, allowing us to isolate the effect of multimodal training history from online visual input or cross-modal fusion. We evaluate mo...

---

### 2. Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images

**Authors:** Joséphine Raugel, Maximilian Seitzer, Marc Szafraniec, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28693v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28693v1)

**Summary:** Backpropagation is the core learning mechanism underlying deep learning. However, whether and how this algorithm is implemented in the brain remains highly debated. In particular, while forward activations of pretrained models reliably map onto the cortical hierarchy of visual processing, it is unknown whether backpropagated gradients exhibit a similar correspondence. Here, we address this question using functional magnetic resonance imaging (fMRI) and magnetoencephalography (MEG) recordings of ...

---

### 3. The Illusion of Opting in AI-Mediated Consequential Decisions

**Authors:** Eugene Yu Ji

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28210v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28210v1)

**Summary:** Drawing on Ullmann-Margalit's concept of opting (transformative, irrevocable, and shadowed by foreclosed alternatives), we show that current AI systems raise a profound ethical problem that existing AI ethics has not fully captured: the illusion of opting, in which persons and groups encounter the deceptive appearance of meaningful consequential choice while the agency needed to become genuinely capable of choosing is weakened. Against approaches that treat AI primarily as an optimizer of alread...

---

### 4. Exploratory Experience Shapes the Geometry of Predictive Representations

**Authors:** Kseniia Shilova, Abdelrahman Sharafeldin, Advay Balakrishnan, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.27929v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27929v1)

**Summary:** Active sensing links behavior and learning through an action-perception loop: actions determine the observations used to update internal predictive models of perception, which subsequently guide the next actions. Predictive-coding frameworks provide a natural way to model this process, since internal representations are continuously updated to predict future observations. Here, we ask how exploratory and exploitative behavioral strategies shape these internal predictive representations. We build...

---

### 5. You Are in Control of Your State: Why Human Outcomes Are Controllable Through Causal State Intervention

**Authors:** Suraj Biswas, Saurav Gupta, Pritam Mukherjee

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27580v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27580v1)

**Summary:** A central puzzle for the behavioural sciences and for human-facing artificial intelligence is the persistence of within-person variability. The same individual, presented with the same observable input, produces different outcomes on different occasions, and different individuals produce divergent outcomes that no observable covariate fully predicts. We argue that this variability belongs in the dynamic latent state of the person, and that human outcomes are controllable in a precise and operati...

---

### 6. Beyond Binary: Speech Representations Across the Cognitive Score Hierarchy

**Authors:** Serli Kopar, Roshan Prakash Rane, Christian Mychajliw, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27189v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27189v1)

**Summary:** This study examines the relationship between speech representations and the hierarchical structure of cognitive assessment in mild cognitive impairment. Utilizing 5,754 German neuropsychological assessment recordings, we evaluate six cognitive tasks across three score levels: task, domain, and global levels. We compare hand-crafted acoustic features with self-supervised learning (SSL) embeddings. Results show that although SSL representations generally outperform hand-crafted features at lower l...

---

### 7. Probabilistic Recurrent Intention Switching Model

**Authors:** Wenyuan Sheng, Hao Zhu, Joschka Boedecker

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26998v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26998v1)

**Summary:** Inverse reinforcement learning (IRL) recovers reward functions from observed behavior, yet traditional methods assume a single stationary reward that cannot capture goal switching within an episode. Recent multi-intention IRL methods address this by segmenting trajectories, but model intention transitions as either a memoryless Markov chain or via manual state augmentation with a fixed history window. We propose the Probabilistic Recurrent Intention Switching Model (PRISM), which replaces both m...

---

### 8. Signal-to-Noise Ratio and Sample Size Govern Representational Alignment in Neural Networks

**Authors:** Ali Hussaini Umar, Alessandro Laio

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26973v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26973v1)

**Summary:** Neural networks are known to develop latent representations that are $aligned$, namely structurally similar across networks trained with different architectures, training protocols, or training datasets. We study this phenomenon in a controlled setting, where we train an ensemble of networks on regression and classification tasks using training sets perturbed by independent realizations of a noise process. We show that the signal-to-noise ratio (SNR) and the training sample size influence the al...

---

### 9. Revealing the core dimensions underlying representations in brains, behavior and AI

**Authors:** Florian P. Mahner, Ka Chun Lam, Francisco Pereira, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26921v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26921v1)

**Summary:** The study of representations is widespread across fields, including neuroscience, psychology, and artificial intelligence. While representations are often studied and compared through similarities between stimuli, current methods provide only limited access to the dimensions that shape these representations and are often limited in interpretability. To overcome these challenges, here we introduce Similarity-Based Representation Factorization (SRF), a general computational method for recovering l...

---

### 10. EEG-FM-Audit: A Systematic Evaluation and Analysis Pipeline for EEG Foundation Models

**Authors:** Xianheng Wang, Yige Yang, Damien Coyle

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26910v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26910v1)

**Summary:** Large EEG Foundation Models (FMs) have shown great potential for decoding EEG signals across diverse cognitive tasks. However, existing EEG-FM studies exhibit three critical limitations: opaque supervised baseline tuning, unverified contributions of complex learning paradigms, and a lack of transparency in model decision-making. To address these, we propose EEG-FM-Audit, a comprehensive evaluation and analysis pipeline designed to systematize the assessment of EEG-FMs. EEG-FM-Audit consists of t...

---

### 11. The Sensation Modulating Network:Haltability as the architectural ground for object-directed phenomenology

**Authors:** G. Nagarjuna, Durgaprasad Karnam

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26856v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26856v1)

**Summary:** Cognitive science remains split between cognitivism - which accounts for recursion and language but cannot ground formal symbols in meaning - and 4E approaches - which ground cognition in the body but rarely specify the body's architecture in enough detail to support generativity. We argue the impasse stems from an incomplete account of the embodied agent's architecture, and propose one: the Sensation Modulating Network (SMN), the cognitive agent conceived as the whole body, organized at every a...

---

### 12. Random neural networks match observed dimensionality of neural population recordings and motivate stronger experimental tests

**Authors:** Zehui Zhao, Michael J Pasek, Ilya M Nemenman

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26551v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26551v1)

**Summary:** Randomly connected neural networks have long served as a theoretical tool for studying collective dynamics in neural populations, yet quantitative comparisons to experiments remain limited. Recent technological advances have made it possible to resolve population-wide correlations across neurons, and minimal models such as random neural networks predict their generic structure. Whether the two agree quantitatively remains untested. In this work, we examine whether a minimally structured random n...

---

### 13. Balancing structure and randomness: maximum entropy networks for context-dependent computations

**Authors:** Ludwig Hruza, Srdjan Ostojic

**Published:** 2026-05-25

🔗 [Paper](http://arxiv.org/abs/2605.25607v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25607v1)

**Summary:** Understanding how network function constrains neural connectivity is a central challenge in neuroscience. An influential approach is to train neural networks with gradient descent on cognitive tasks and characterize the resulting connectivity. A key limitation is that the resulting structure depends on the details of the training procedure. Here we propose a complementary normative approach based on the maximum entropy principle for network connectivity, independent of any particular learning al...

---

### 14. Exact Variance and Fano Factor for Arbitrary Level Crossings in Stationary Gaussian Processes

**Authors:** Shivang Rawat, Flaviano Morone, David J. Heeger, et al.

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25278v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25278v1)

**Summary:** Understanding the statistics of level crossings in stochastic processes is crucial across many scientific disciplines. The traditional Kac-Rice formula gives the mean rate of level crossings and has found broad use. However, that mean rate captures only a coarse summary of the crossing process. It depends entirely on local properties of the stochastic process at a given instant and is therefore blind to the correlation structure of the process over time. To understand whether crossing events, su...

---

### 15. Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks

**Authors:** Divyansh Sethi, Muhammad Faraz, KongFatt Wong-Lin

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25224v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25224v1)

**Summary:** Spiking neural networks (SNNs) can be used for implementing cost-efficient artificial intelligence computing or mechanistic modelling of experimentally observed neural data. In the latter, fitting neural data with recurrent SNNs (RSNNs) remains a challenge. Importantly, given that neuronal network oscillations are known to play important roles in neural functions, fitting specific RSNN oscillation frequencies with neural firing rates has yet to be fully explored. In this work, we extended our pr...

---

### 16. A Quantum-Analogue Formalism for Modeling Supraliminal Information Processing

**Authors:** Vasily Lubashevskiy, Ihor Lubashevsky

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25214v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25214v1)

**Summary:** We develop a novel cloud-function formalism describing the dynamical relationship between sensory-information processing in large-scale brain networks (supraliminal processing) and the content of the mental representation of an observed object. The formalism combines elements of neural field theory for large-scale neural activity with the spatial characteristics of perceived objects and their embedding in the environment from the first-person perspective. The cloud function is characterized by t...

---

### 17. Growing a Neural Network in Breadth, Depth, and Time

**Authors:** Eivinas Butkus, Kedar Garzón Gupta, Nikolaus Kriegeskorte

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.25174v1) | 📄 [PDF](https://arxiv.org/pdf/2605.25174v1)

**Summary:** Spatial and temporal resource constraints are critical for both biological and artificial intelligent systems. Here we define differentiable cost terms for breadth, depth, and time within a recurrent convolutional neural network conceived as a finite subset of an infinite lattice. We optimize these costs jointly with task errors via backpropagation. We set different pressures on breadth, depth, and time, which leads to diverse computational graphs emerging organically through training. We find t...

---

### 18. Interpretation, Learning, and Empathy as One Constraint: A Residual-Adequacy Architecture with Accountable Abstention

**Authors:** Chainarong Amornbunchornvej

**Published:** 2026-05-24

🔗 [Paper](http://arxiv.org/abs/2605.24999v1) | 📄 [PDF](https://arxiv.org/pdf/2605.24999v1)

**Summary:** An agent must act on the situation before it, learn what it cannot yet represent, and model other agents well enough to coordinate. These faculties are usually realized by separate mechanisms, yet they share a failure mode: the situation can exceed what the agent can currently represent, and the honest response is then a principled refusal that says what was missing. We develop a small cognitive architecture in which these limits arise from a single quantity. An Interpretation-Decision Unit (IDU...

---

### 19. Word Class Representations Spontaneously Emerge from Successor Representations Trained on Natural Language

**Authors:** Mathis Immertreu, Achim Schilling, Thomas Kinfe, et al.

**Published:** 2026-05-23

🔗 [Paper](http://arxiv.org/abs/2605.24585v1) | 📄 [PDF](https://arxiv.org/pdf/2605.24585v1)

**Summary:** Language models are typically trained to predict the next token in a sequence. Here, we explore an alternative predictive principle from reinforcement learning: Successor Representations (SRs), which model the expected discounted distribution of future states rather than the immediate next state. We transfer this framework to natural language and train neural networks to predict future word distributions across multiple temporal horizons, thereby learning representations of long-range transition...

---

### 20. What Are We Actually Decoding? Source Attribution for Non-Invasive Brain-to-Language Retrieval

**Authors:** Xinyu Zhang, Sichao Liu, Runhao Lu, et al.

**Published:** 2026-05-23

🔗 [Paper](http://arxiv.org/abs/2605.24524v1) | 📄 [PDF](https://arxiv.org/pdf/2605.24524v1)

**Summary:** In non-invasive neural language decoding, results can be inflated by sources that are not stimulus-evoked neural evidence: decoder priors, embedding-based metrics, and non-neural structural nuisances such as signal duration. The methodological challenge is therefore attribution: a reported gain is more informative when it can be traced to a specific source. We recast stimulus-locked MEG-to-audio retrieval as an auditing framework that separates apparent performance into three sources - structura...

---

### 21. MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding

**Authors:** Zexuan Chen, Sichao Liu, Runhao Lu, et al.

**Published:** 2026-05-23

🔗 [Paper](http://arxiv.org/abs/2605.24523v1) | 📄 [PDF](https://arxiv.org/pdf/2605.24523v1)

**Summary:** Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. We introduce a tri-modal contrastive framework for EEG-based visual decoding that aligns EEG, visual, and textual representations within a unified latent space. Our approach follows a two-stage design. First, we pre-train an EEG encoder via masked reconstruction on unlabeled trials, learning spatio-...

---

### 22. Geometric Origin of Exact Mean-Field Reductions: M{ö}bius Symmetry and the Lorentzian Ansatz

**Authors:** Hugues Berry, Leonardo Trujillo

**Published:** 2026-05-22

🔗 [Paper](http://arxiv.org/abs/2605.23669v1) | 📄 [PDF](https://arxiv.org/pdf/2605.23669v1)

**Summary:** Low-dimensional descriptions of large systems of coupled oscillators and spiking neurons rely heavily on the Lorentzian Ansatz. We show that its privileged role is geometric rather than heuristic: for the transport induced by Riccati dynamics, the Cauchy-Lorentz family indeed emerges as the unique connected two-dimensional family of continuous probability densities that is invariant under the induced projective transport. The key step of the demonstration is to reformulate the dynamics on the ci...

---

### 23. Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins

**Authors:** Adriano Lima, Yuchen Hou, Michael Beyeler, et al.

**Published:** 2026-05-22

🔗 [Paper](http://arxiv.org/abs/2605.23122v2) | 📄 [PDF](https://arxiv.org/pdf/2605.23122v2)

**Summary:** Digital twins of sensory cortex serve as powerful response oracles. Although prediction accuracy is the central metric by which these models are evaluated, it provides limited insight into the latent representations that support those predictions. This becomes increasingly important as digital twins are used as in silico experimental systems for stimulus design and hypothesis generation: models with similar prediction accuracy may rely on different latent representations. We address this gap by ...

---

### 24. Contextual Role Modulates Object Representational Geometry in the Human Brain

**Authors:** Julien Dirani, Shankar Chawla, Leila Wehbe, et al.

**Published:** 2026-05-22

🔗 [Paper](http://arxiv.org/abs/2605.23111v2) | 📄 [PDF](https://arxiv.org/pdf/2605.23111v2)

**Summary:** The human brain represents objects in a way that is both invariant across instances and flexible enough to support different contexts and tasks. Yet it remains unknown how object representations are dynamically remapped as the same object shifts across contextual roles. Here we combined fMRI with naturalistic movie viewing to investigate how the same objects are represented when they are passive elements in the scene versus the targets of goal-directed actions. When objects were action targets, ...

---

### 25. Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography

**Authors:** Dongxin Guo, Jikun Wu, Siu Ming Yiu

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.23035v1) | 📄 [PDF](https://arxiv.org/pdf/2605.23035v1)

**Summary:** Intermediate layers of large language models (LLMs) best predict human brain responses to language, one of the most robust findings in computational neurolinguistics, yet why remains mechanistically unexplained. We address this gap by bridging sparse autoencoders (SAEs) from mechanistic interpretability with neural encoding models, decomposing GPT-2 XL and Llama-3.1-8B into 16K-32K interpretable features per layer. A human-validated taxonomy ($κ\geq 0.74$) reveals that semantic features alone re...

---

### 26. Brain-LLM Alignment Tracks Training Data, Not Typology

**Authors:** Dongxin Guo, Jikun Wu, Siu Ming Yiu

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.23032v1) | 📄 [PDF](https://arxiv.org/pdf/2605.23032v1)

**Summary:** Brain-LLM alignment is well established in English, yet the brain's language network is neuroanatomically universal across languages. Does alignment also generalize cross-linguistically, and what governs the variation? We test this using fMRI data from 112 participants across English, Chinese, and French (the Le Petit Prince corpus) and seven LLMs spanning English-dominant, Chinese-dominant, and multilingual architectures. Our central finding is that training-language dominance, not an inherent ...

---

### 27. Integrating Cognitive Load and Embodied Cognition Theories Through Representations as Multi-Scale Attractors

**Authors:** David C. Gibson, Mary Elizabeth Azukas, Meryem Yilmaz Soylu

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.23012v1) | 📄 [PDF](https://arxiv.org/pdf/2605.23012v1)

**Summary:** This article proposes a formal rapprochement between cognitive load theory and embodied cognition by reconceptualizing psychological representations as dynamic multiscale attractors within a temporal-hierarchical prediction architecture. The apparent conflict between the two theories dissolves when viewed through a complex systems lens. Cognitive load theory describes compressed representations operating at medium timescales, while embodied cognition describes fast sensorimotor loops. These two ...

---

### 28. Active Sensing Subserves Task-Level Control

**Authors:** Andrew Lamperski, Debojyoti Biswas, Eric S. Fortune, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22988v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22988v1)

**Summary:** Active sensing is traditionally defined as the expenditure of energy, typically in the form of movement, for obtaining information. Here, we propose that the combination of reliance on adaptive sensors, the linkage between movement and sensing, and task-level control inevitably gives rise to the emergence of active sensing movements. In this way, active sensing is not driven by sensory goals, such as minimizing uncertainty about the state, but rather is necessary for task-level control. This hyp...

---

### 29. GazeBehavior Annotation Toolkit (GBAT): AI-powered toolkit for automatic annotation of egocentric eye-tracking and video data of child-caregiver interaction

**Authors:** Iba Baig, Kevin Li, Yanbin Xu, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22962v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22962v1)

**Summary:** Video recordings of child-caregiver interactions enable investigation of attentional dynamics during naturalistic behavior. Such multimodal recording also allows researchers to examine how attention interacts with action and language use in real time. However, manual annotation of such data is time-consuming. Here, we introduce GazeBehavior Annotation Toolkit, a deep-learning-based toolkit designed to facilitate three key processes in data preprocessing and feature extraction: post-hoc synchroni...

---

### 30. Efficient coding under constraint drives neural systems towards criticality and sloppiness

**Authors:** He Xiao, Xinyue Zhao, Weikang Wang

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22598v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22598v1)

**Summary:** It is widely accepted that the brain operates near a critical state, characterized by neural avalanches that follow power-law distributions. However, the functional rationale for why neural systems attain criticality remains unclear. Here, we present a theoretical framework that links efficient coding to criticality in neural populations. Using a Gaussian population coding model, we demonstrate that maximizing Fisher information under resource constraints naturally leads to the emergence of soft...

---

### 31. Learning sequence timing and control of replay speed in networks of spiking neurons

**Authors:** Melissa Lober, Younes Bouhadjar, Markus Diesmann, et al.

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22523v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22523v1)

**Summary:** Processing sequential inputs is a fundamental brain function, underlying tasks such as sensory perception, language, and motor control. A challenge in sequence processing is to represent not only the order of events, but also their precise timing. While existing computational models can learn sequential structure, many lack biologically plausible mechanisms to encode element-specific timing and to flexibly control the speed of sequence replay. The spiking Temporal Memory (sTM) model, a biologica...

---

### 32. Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings Across Human fMRI and Macaque Electrophysiology

**Authors:** Nils Leutenegger

**Published:** 2026-05-21

🔗 [Paper](http://arxiv.org/abs/2605.22401v1) | 📄 [PDF](https://arxiv.org/pdf/2605.22401v1)

**Summary:** Does the relationship between learning rules and brain alignment generalize across species? We extend our prior finding that untrained CNNs match backpropagation at human V1 by testing the same five learning rules against macaque electrophysiology. The rules are backpropagation (BP), feedback alignment (FA), predictive coding (PC), spike-timing-dependent plasticity (STDP), and an untrained random-weights baseline. The macaque data come from two datasets: MajajHong2015 (V4/IT, 3,200 stimulus pres...

---

### 33. A simple model of co-emergence of grid and place fields

**Authors:** Zhaoze Wang, Genela Morris, Dori Derdikman, et al.

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21356v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21356v1)

**Summary:** Grid cells in the medial entorhinal cortex and place cells in the hippocampus together support spatial navigation. The two regions are reciprocally connected, and there is a chicken-and-egg problem for how both arise and reinforce each other during development. Current computational accounts either derive one type from the other or use network dynamics to model the emergence of one type in isolation. We introduce a unified recurrent network model that instantiates Dale's Law (every neuron is eit...

---

### 34. Stimulus symmetries can confound representational similarity analyses

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-05-20

🔗 [Paper](http://arxiv.org/abs/2605.21324v1) | 📄 [PDF](https://arxiv.org/pdf/2605.21324v1)

**Summary:** What can representational similarity matrices (RSMs) tell us about a neural code? As the popularity of these summary statistics grows, so too does the need for a more complete characterization of their properties. Here, we show that symmetries in network inputs can confound RSM-based analyses. Stimulus symmetries render many representations functionally equivalent, but these different configurations can lead to different RSMs. These different RSMs reflect qualitatively different representational...

---

### 35. Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry

**Authors:** Pablo Marcos-Manchón, Rishi Jha, Lluís Fuentemilla

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20496v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20496v1)

**Summary:** The Strong Platonic Representation Hypothesis suggests that representational convergence in artificial neural networks can be harnessed constructively: embeddings can be translated across models through a universal latent space without paired data. We ask whether an analogous geometry can be recovered across human brains. Using fMRI data from the Natural Scenes Dataset, we propose a self-supervised encoder that learns subject-specific embeddings from brain data alone by exploiting repeated stimu...

---

### 36. Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment

**Authors:** Ken Nakamura, Tomoya Nakai, Ryuto Yashiro, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.20127v1) | 📄 [PDF](https://arxiv.org/pdf/2605.20127v1)

**Summary:** Artificial vision models are often evaluated against the human visual cortex by measuring how accurately their internal representations predict brain responses. However, prediction accuracy alone does not indicate which dimensions of the target brain's response space are recovered. Here, we introduce a unified framework for evaluating both model-brain and brain-brain alignment by identifying the response dimensions recovered by prediction. Using repeated fMRI measurements, we first identify targ...

---

### 37. Performance of low vision individuals when selecting a target with head-pointing in virtual reality

**Authors:** Camille Bordeau, Célia Passerel, Ambre Denis-Noël, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19816v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19816v1)

**Summary:** Purpose: To investigate psychophysically the ability of low vision individuals with central visual field loss (CFL) to perform a visually-guided pointing task in a virtual reality environment. Methods: Patients with CFL (n=25, ages = 67-90 years) and normally-sighted controls (n=26, ages = 67-85 years) had to select a target (2{\textdegree} diameter dot) with a head-contingent cursor (6{\textdegree} diameter reticle).  Target selection occurred when target was validly pointed at for 1.5 seconds....

---

### 38. BCI-sift: An automated feature selection toolbox for Brain Computer Interface applications

**Authors:** Elena C Offenberg, Dirk Keller, Mariska J Vansteensel, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19646v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19646v1)

**Summary:** Advancements in clinical Brain-Computer Interfaces (BCIs) depend on precise and reliable signal interpretation. However, the high-dimensional and noisy nature of data captured from both implanted and non-implanted BCIs poses significant challenges, motivating the use of feature selection algorithms. We introduce BCI-sift (BCI Systematic and Interpretable Feature Tuning), a Python-based toolbox designed to streamline the application of diverse optimization algorithms to BCI datasets for identifyi...

---

### 39. Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay

**Authors:** Subba Reddy Oota, Anant Khandelwal, Khushbu Pahwa, et al.

**Published:** 2026-05-19

🔗 [Paper](http://arxiv.org/abs/2605.19352v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19352v1)

**Summary:** Understanding how humans and artificial intelligence systems predict and plan by interacting with their environment is a fundamental challenge at the intersection of neuroscience and machine learning. Most brain-encoding studies focus on aligning artificial models with brain activity during language comprehension or passive visual processing, while interactive brain-alignment studies have to date been largely limited to reinforcement-learning (RL) agents and theory-based models. To address this ...

---

### 40. Computational Auditory Periphery Models: the Return of the Rodent

**Authors:** Morgan Thienpont, F. Deloche, S. Keshishzadeh, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19070v2) | 📄 [PDF](https://arxiv.org/pdf/2605.19070v2)

**Summary:** Animal experiments have provided many insights on auditory function, notably in cases of sensorineural hearing loss (SNHL). However, it is not always clear how these findings translate to the human auditory system in clinically relevant contexts. Cross-species computational models of the auditory periphery can help bridge the gap between non-invasive human diagnostics and experimental evidence from animal studies. In this work we adapted a 1-D nonlinear cochlear transmission-line model designed ...

---

### 41. Conserved Kinematic Representations enable Zero-Shot Decoding in Handwriting BCIs

**Authors:** Srinivas Ravishankar, Virginia de Sa

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.19048v1) | 📄 [PDF](https://arxiv.org/pdf/2605.19048v1)

**Summary:** While intracortical Brain-Computer Interfaces (iBCIs) that decode imagined handwriting have achieved high communication rates for Latin scripts, they rely on observing every character in the alphabet during training. This poses a challenge in scaling to logographic languages (e.g., Chinese, Japanese), where the character set exceeds thousands of classes. The limitation highlights a fundamental question in motor neuroscience: does the motor cortex represent handwriting through the composition of ...

---

### 42. Toward an Origin of Human Randomness: Interaction-Driven Enhancement in the Rock-Paper-Scissors Game

**Authors:** Song-Ju Kim, Shoma Ohara, Hiroaki Kurokawa

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18616v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18616v1)

**Summary:** Human-generated randomness is constrained by cognitive, motor, and strategic biases. This study examines how these constraints appear in individual behavior and how they may be modified through interaction with another human. We analyzed repeated rock-paper-scissors data from 9 participants, yielding 108 human-human matches and 216 individual player sequences. Using Lempel-Ziv complexity (LZC), we compared human-human sequences with the RNG-opponent condition. In the RNG-opponent condition, the ...

---

### 43. Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data

**Authors:** Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18557v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18557v1)

**Summary:** The brain learns abstract representations of high-dimensional sensory input, but the plasticity rules that enable such learning are unknown. We study biologically plausible algorithms on the Random Hierarchy Model (RHM), an artificial dataset designed to investigate how deep neural networks learn the intrinsic hierarchical structure of high-dimensional data. We focus on two types of local learning rules that avoid both a long convergence time and the use of a symmetric error network. The first t...

---

### 44. Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG with Controlled Internal and External Attention Conditions

**Authors:** Yuwen Zeng, Dengzhe Hou, Zhang Zhang, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18251v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18251v1)

**Summary:** Self-initiated attention shifts play a critical role in voluntary behavior but are difficult to study due to the absence of explicit temporal markers. While previous studies have examined their neural correlates, it remains unclear how multi-dimensional electroencephalography (EEG) features contribute to their characterization within an interpretable computational framework. In this study, we build on an experimental paradigm developed in our previous work, which enables controlled comparison be...

---

### 45. Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function

**Authors:** Mario Senden, Leonardo Dalla Porta, Jan Fousek, et al.

**Published:** 2026-05-18

🔗 [Paper](http://arxiv.org/abs/2605.18118v1) | 📄 [PDF](https://arxiv.org/pdf/2605.18118v1)

**Summary:** Contemporary computational neuroscience features two prominent modeling traditions. Bottom-up whole-brain modeling (WBM) builds biophysically detailed simulations of brain structure and dynamics, whereas top-down neuroconnectionism optimizes deep neural networks for functional performance. Each has achieved remarkable success yet remains incomplete with WBMs lacking functional competence and neuroconnectionist models showing limited biological grounding. Here we propose functional whole-brain mo...

---

### 46. Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks: a computational account with clinical predictions

**Authors:** Esila Keskin

**Published:** 2026-05-17

🔗 [Paper](http://arxiv.org/abs/2605.17399v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17399v1)

**Summary:** Von Economo neurons (VENs) are selectively lost in behavioural-variant frontotemporal dementia (bvFTD) and reduced in autism spectrum conditions (ASC), yet their computational role in social learning remains unexplained. We train a spiking neural network (the VENCircuit) embedding VEN-like projection neurons (K=40, 2% of total) in a recurrent pyramidal circuit across 50 matched random initialisations with and without VENs. The network is trained on a controlled binary classification task; we mak...

---

### 47. Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity

**Authors:** Prashant C. Raju

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.17199v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17199v1)

**Summary:** Memory systems can store vastly different amounts of information despite similar hardware constraints. Here, we show that superior spatial memory emerges from a discrete stiffening of hippocampal population geometry-a transition from disorganized to crystalline collective coding. Comparing food-caching chickadees to non-caching zebra finches, we found that the caching hippocampus maintains a topologically rigid, "crystalline" geometry with significantly higher geometric stability (Shesha 0.245 v...

---

### 48. MIRAGE: Robust multi-modal architectures translate fMRI-to-image models from vision to mental imagery

**Authors:** Reese Kneeland, Cesar Kadir Torrico Villanueva, Jordyn Ojeda, et al.

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.17198v1) | 📄 [PDF](https://arxiv.org/pdf/2605.17198v1)

**Summary:** To be useful for downstream applications, vision decoding models that are trained to reconstruct seen images from human brain activity must be able to generalize to internally generated visual representations, i.e., mental images. In an analysis of the recently released NSD-Imagery dataset, we demonstrated that while some modern vision decoders can perform quite well on mental image reconstruction, some fail, and that state-of-the-art (SOTA) performance on seen image reconstruction is no guarant...

---

### 49. Effort as Ceiling, Not Dial: Reasoning Budget Does Not Modulate Cognitive Cost Alignment Between Humans and Large Reasoning Models

**Authors:** Yueqing Hu, Tianhong Wang

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.16938v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16938v1)

**Summary:** Large Reasoning Models (LRMs) generate chain-of-thought traces whose length tracks human reaction times across cognitive tasks, but recent debate questions whether this alignment reflects genuine computational structure or surface verbosity. We test whether the alignment varies with inference-time reasoning effort. Across GPT-OSS-20B and GPT-OSS-120B, three effort levels, and six reasoning tasks, within-task and cross-task alignment remain invariant: Bayes Factors lean toward the null, and mean ...

---

### 50. A Mathematical Characterization of Neural Activation Induced by Temporal Interference Stimulation

**Authors:** Esteban Paduro, Antoine Chaillet, Mario Sigalotti

**Published:** 2026-05-16

🔗 [Paper](http://arxiv.org/abs/2605.16761v1) | 📄 [PDF](https://arxiv.org/pdf/2605.16761v1)

**Summary:** Temporal Interference Stimulation (TIS) is a non-invasive neuromodulation technique in which two high-frequency sinusoidal currents with slightly different frequencies generate a low-frequency envelope that can activate deep neural structures. This study investigates the conditions under which TIS elicits action potentials in a single neuron modeled by the FitzHugh-Nagumo system. This research integrates phase-plane analysis and geometric singular perturbation to develop a mathematical framework...

---

## stat.ML

**50 papers**

### 1. Principled Algorithms for Optimizing Generalized Metrics in Multi-Label Learning

**Authors:** Mehryar Mohri, Yutao Zhong

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28767v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28767v1)

**Summary:** Many real-world classification tasks require predicting multiple labels per instance, necessitating the optimization of complex evaluation metrics such as the $F$-measure and Jaccard index. While the Empirical Utility Maximization (EUM) framework is natural for these population-level metrics, existing theoretical results are largely limited to asymptotic Bayes-consistency. In this paper, we develop principled learning algorithms for optimizing a broad class of generalized metrics within the EUM ...

---

### 2. Deep Neural Networks for Doubly Robust Estimation with Nonprobability Survey Samples

**Authors:** Yufang Dai, Shihua Luo, Wendy Lou, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28762v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28762v1)

**Summary:** Integrating probability and nonprobability survey samples is an important problem in modern survey sampling. Nonprobability samples often contain rich outcome information but may lack population representativeness, whereas probability samples provide design-based auxiliary information but may not contain the study variable. We propose a deep neural network (DNN)-assisted doubly robust framework for estimating the finite population mean from these two data sources. The proposed method models the ...

---

### 3. Beyond Lipschitz: Data-Driven Robustness via Discrete Modulus of Continuity

**Authors:** Jürgen Dölz, Michael Multerer, Michele Palma

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28729v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28729v1)

**Summary:** Robustness of neural networks is commonly quantified via local or global Lipschitz constants. However, Lipschitz continuity can be overly coarse or overly restrictive as global robustness measure, failing to capture nuanced, data-dependent behavior. We propose a data-driven, architecture-agnostic framework based on the discrete modulus of continuity (DMOC), a non linear generalization of Lipschitz continuity that provides a finer notion of robustness. Unlike many existing approaches, DMOC does n...

---

### 4. Optimal ridge regularization revisited

**Authors:** Jack Timmermans, Sergio A. Alvarez

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28679v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28679v1)

**Summary:** We consider $L^2$-regularized linear (ridge) regression over a finite data sample $X$ with bounded covariance and linear prediction targets $y$ with additive isotropic noise of finite variance. We present an iterative procedure to compute the optimal regularization strength numerically from the generative parameters in the fixed-$X$ setting and prove its convergence at limited noise levels. Our experimental evaluation over synthetic data shows that the proposed procedure combined with sample-bas...

---

### 5. Implicit Regularization in Perturbed Deep Matrix Factorization: Spectral Conditions and Stability

**Authors:** Jingzhe Wang, Hung-Hsu Chou

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28613v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28613v1)

**Summary:** This paper studies the stability of low-rank implicit regularization in perturbed deep matrix factorization, where the target matrix is corrupted by a noise matrix. We first derive sufficient spectral conditions under which gradient descent exhibits a low-rank phase in the noiseless setting. These conditions show how the target spectrum, initialization, and step size jointly determine the existence of a nonempty low-rank interval. We then analyze the perturbed gradient descent dynamics, proving ...

---

### 6. Conservative neural posterior estimation via distributionally robust training

**Authors:** William Laplante, Yuga Hikida, Charita Dellaporta, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28516v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28516v1)

**Summary:** Simulation-based inference with neural posterior estimation (NPE) often yields overconfident and unreliable posteriors under limited simulation budgets. To address this, we propose DRO-NPE, a distributionally robust approach that replaces the standard NPE objective with a worst-case loss over a Wasserstein ambiguity set. We introduce KL-based metrics for miscoverage and miscalibration, and use these to show that the DRO-NPE objective controls overfitting and reduces posterior overconfidence. Our...

---

### 7. Bridging Maximum Likelihood and Optimal Transport for Efficient Inference and Model Selection in Stochastic Block Models

**Authors:** Simon Queric, Cédric Vincent-Cuaz, Charles Bouveyron, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28488v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28488v1)

**Summary:** We study inference in stochastic block models (SBMs) through the lens of optimal transport (OT). We first establish that maximum likelihood variational inference (MLVI) can be interpreted as a semi-relaxed Gromov-Wasserstein (srGW) projection with entropic regularization. While this formulation yields accurate clustering, the entropic regularization prevents transport plans to be sparse, hindering intrinsic model selection. Consequently, we investigate unregularized srGW estimators, and prove th...

---

### 8. Latent Diffusion for Missing Data

**Authors:** Alberte Heering Estad, Ignacio Peis, Jes Frellsen

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28427v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28427v1)

**Summary:** Diffusion models have emerged as powerful generative approaches for missing-data imputation, yet most existing methods operate directly in data space and degrade when training data are heavily incomplete. We investigate whether shifting diffusion to a learned latent representation improves robustness under missing-completely-at-random (MCAR) corruption. To this end, we propose a two-stage framework: a robust VAE-based imputer first learns compact semantic features from incomplete observations, a...

---

### 9. Variance-Adaptive Optimal Algorithm for Reinforcement Learning with Multinomial Logit Function Approximation

**Authors:** Wonyoung Kim, Min-Hwan Oh, Garud Iyengar, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28364v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28364v1)

**Summary:** Reinforcement learning with multinomial logistic (MNL) function approximation has become an important framework due to its flexibility and broad applicability. While existing studies have established regret guarantees under worst-case analysis, they do not capture how performance depends on the variability of the interaction between the learner and the environment. In this paper, we develop a new theoretical analysis for MNL-based Markov decision processes that yields explicit variance-adaptive ...

---

### 10. Decision-focused learning for optimal PV-Battery scheduling

**Authors:** Joris Depoortere, Hussain Kazmi, Johan Driesen

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28340v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28340v1)

**Summary:** The use of residential photovoltaics has increased dramatically in recent years. With battery systems becoming more affordable, the optimal operation of a photovoltaic-battery system can bring significant savings to households. Optimal control requires correct forecasts of underlying parameters, such as photovoltaic power generation, to schedule the battery. While forecasting models have become increasingly accurate due to algorithmic advances and data availability, accuracy is typically measure...

---

### 11. Insurance Pricing Optimization via Off-Policy Evaluation

**Authors:** Sascha Günther, Dimitri Semenovich, Mario V. Wüthrich

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28327v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28327v1)

**Summary:** Traditional insurance pricing relies on risk-based principles that ensure actuarial fairness and solvency but do not explicitly account for policyholders' price sensitivity. We formulate insurance pricing as a decision-making problem and study it using tools from off-policy evaluation and stochastic control. We propose a kernelized inverse propensity score estimator that exploits local structure in the action space and yields variance reduction compared to the classical inverse propensity score ...

---

### 12. Adaptive Bandit Algorithms for Contextual Matching Markets

**Authors:** Shiyun Lin, Simon Mauras, Vianney Perchet, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28290v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28290v1)

**Summary:** We study bandit learning in matching markets, where players and arms constitute the two market sides, and the players' utilities are linear in the arm contexts. In each round, new arms arrive with observable contexts. Then, the algorithm matches them to players, aiming to minimize each player's regret against a stable matching benchmark. This contextual structure creates significant complexity: subtle context shifts can slightly alter one player's utility while completely reconfiguring the under...

---

### 13. Parameter-Efficient Generative Modeling with Controlled Vector Fields

**Authors:** Peyman Morteza

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28267v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28267v1)

**Summary:** We introduce a continuous-time generative modeling framework, motivated by the Chow-Rashevskii theorem, that builds expressive flows from a small set of fixed vector fields and learned scalar controls. Instead of learning an unconstrained high-dimensional vector field, our framework constructs the velocity by modulating fixed vector fields with learned scalar control functions. When the fixed fields are bracket-generating, their Lie algebra spans the ambient space, providing a mechanism for expr...

---

### 14. Counterfactually Fair Regression via Optimal Transport

**Authors:** M. Generali Lince, S. Gaucher, J-J. Vie, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28251v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28251v1)

**Summary:** We consider the problem of learning a counterfactually fair regressor. We adopt a causal uncertainty view in which counterfactual fairness is defined with resampled noise. We focus on obtaining theoretical fairness guarantees for a new post-processing estimator. We begin by showing that counterfactual fairness is equivalent to satisfying demographic parity conditional on the latent variable. This allows us to provide a closed-form expression of the optimal fair regressor via a barycentric quanti...

---

### 15. Geometry of Relaxed Fair Regression: A Unified Framework for Aware and Unaware Settings

**Authors:** M. Generali Lince, V. Divol, R. Flamary, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28233v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28233v1)

**Summary:** Fairness-accuracy trade-offs are a central concern in the deployment of fairness-aware machine learning methods. When sensitive attributes are unavailable at inference time-the so called unawareness setting, principled methods for obtaining accurate predictions under relaxed fairness constraints are largely missing. In this work, we address this gap by formulating regression under a demographic parity penalty as an optimal transport problem. Our framework unifies both the \emph{aware} and \emph{...

---

### 16. Convergence of empirical subgradients for optimal transport-based objectives

**Authors:** Tam Le

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28134v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28134v1)

**Summary:** Optimal transport is widely used to learn distributions, enforce distributional constraints, and model uncertainty. In applications, transport losses are often computed from samples through tractable representations, such as one-dimensional sorting formulas or sliced Wasserstein costs, making them practical components in training pipelines. We study parameterized objectives defined by sampled transport costs and prove graphical convergence of their subdifferentials to the subdifferential of the ...

---

### 17. Learning to Bid in Repeated Second-Price Auctions with Dynamic Values and Aggregated Feedback

**Authors:** Benjamin Heymann, Otmane Sakhi

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28133v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28133v1)

**Summary:** We study the problem of learning to bid when the bidder's value is dynamic, i.e., when the current value depends on past outcomes. Specifically, we consider a bidder participating in repeated second-price auctions whose value depends on the time elapsed since their last successful bid, with auctions arriving in continuous time and only aggregated feedback revealed at the end of the horizon. Such a bidder must (1) balance the immediate benefit of winning the current auction against its impact on ...

---

### 18. Gaussian Processes with Sample Paths in Reproducing Kernel Banach Spaces

**Authors:** Toni Karvonen, Rasmus Kleist Hørlyck Sørensen

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28106v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28106v1)

**Summary:** We investigate the connection between Gaussian processes and Gaussian random elements in reproducing kernel Banach spaces. We show that the covariance operator of a weak second-order Radon probability measure on such a space is uniquely determined by a positive definite function. In the Gaussian case, we characterize those positive definite functions that arise from covariance operators in terms of $γ$-radonifying operators. Building on these results, we extend the classical Driscoll theorem to ...

---

### 19. Mind the Gap: Mixtures of Gaussians in Approximate Differential Privacy

**Authors:** Huikang Liu, Aras Selvi, Wolfram Wiesemann

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28078v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28078v1)

**Summary:** We design a class of additive noise mechanisms that satisfy \((\varepsilon, δ)\)-differential privacy (DP) for scalar, real-valued query functions with known sensitivities, with a particular focus on moderate and low-privacy regimes. These mechanisms, which we call \textit{mixture mechanisms}, are constructed by mixing multiple Gaussian distributions that share the same variance but differ in their means and mixture weights. The resulting distributions can be interpreted as convex combinations o...

---

### 20. The conditional-mean barrier: From deterministic regression to conditional distribution learning

**Authors:** Junfeng Chen

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.28076v1) | 📄 [PDF](https://arxiv.org/pdf/2605.28076v1)

**Summary:** Many problems in computational science and engineering become one-to-many after coarse graining, partial observation, or inverse reconstruction: a resolved state may not determine a unique subgrid forcing, a structural descriptor may not determine a unique effective response, and a low-resolution observation may correspond to many plausible high-resolution fields. In such settings, deterministic surrogates may learn a well-defined mathematical object while still missing application-relevant unce...

---

### 21. Deep Neural Network Training as Random Effects: An Optimization-Inference Duality

**Authors:** Minhao Yao, Ruoyu Wang, Xihong Lin, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.27991v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27991v1)

**Summary:** Deep neural networks (DNNs) have achieved remarkable empirical success, yet their training dynamics remain understood mainly from optimization rather than statistical principles. Here we develop a statistical framework for DNN training in the over-parameterized regime by showing that the prediction induced by continuous-time neural tangent kernel (NTK) gradient flow is exactly equivalent to that from a classical random-effects model. In this framework, training time acts as a variance component,...

---

### 22. Continual Learning in Modern Hopfield Networks with an Application to Diffusion Models

**Authors:** Ken Takeda, Masafumi Oizumi, Ryo Karakida

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.27975v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27975v1)

**Summary:** Generative models, including diffusion models, are increasingly used as foundation models and adapted through sequential fine-tuning, making continual learning an essential problem setting. However, continual learning in such generative models remains poorly understood: after a task change, what aspects of the learned distribution are most easily lost, and what replay samples should be prioritized? We address these questions through the modern Hopfield energy. Recent links between modern Hopfiel...

---

### 23. Multi-Teacher Knowledge Distillation via Teacher-Informed Mixture Priors

**Authors:** Luyang Fang, Yongkai Chen, Jiazhang Cai, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.27967v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27967v1)

**Summary:** Knowledge distillation is a powerful method for model compression, enabling the efficient deployment of complex deep learning models (teachers), including large language models. However, its underlying statistical mechanisms remain unclear, and uncertainty evaluation is often overlooked, especially in real-world scenarios requiring diverse teacher expertise. To address these challenges, we introduce \textit{Multi-Teacher Bayesian Knowledge Distillation} (MT-BKD), where a distilled student model ...

---

### 24. Is Backpropagation Optimal? When Synthetic Gradients Improve Sample Efficiency

**Authors:** Yibo Jacky Zhang, Zeyu Tang, Sanmi Koyejo

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.27946v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27946v1)

**Summary:** Backpropagation is the default learning rule for artificial neural networks and is often treated as the settled approach whenever differentiability is available. In this work, we revisit this convention through a theoretical lens of sample efficiency. We introduce a unified vectorized feedback framework for loss-based and reward-based learning on computational graphs, in which synthetic gradients emerge as a natural alternative to backpropagation. We characterize the conditions under which synth...

---

### 25. Reward Transfer from Inverse Reinforcement Learning: A Coupled Minimax Approach

**Authors:** Guang-Yuan Hao, Lars van der Laan, Aurélien Bibaut, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.27834v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27834v1)

**Summary:** We study the transfer of rewards learned using inverse reinforcement learning from expert demonstrations in one environment to reinforcement learning in a new, different environment. This arises naturally when demonstrations are collected in a controlled environment. We formulate the problem as a joint system of Bellman equations across the source and target environments and develop minimax estimators for the target soft-$q$-function. Whereas a sequential solution approach first estimates the so...

---

### 26. Learning to target with network interference

**Authors:** Xiaomeng Wang, Hamsa Bastani, Osbert Bastani, et al.

**Published:** 2026-05-27

🔗 [Paper](http://arxiv.org/abs/2605.27794v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27794v1)

**Summary:** This paper studies adaptive targeting under network interference in a bandit setting, where treatments applied to one individual may affect others through spillover effects. We consider a linear model in a sparse regime, where each individual's outcome can be affected by at most a few others. We first establish a regret lower bound showing that ignoring the network structure and reducing the problem to a standard linear bandit inevitably leads to inefficient learning, particularly in large popul...

---

### 27. Smoothed Score Queries and the Complexity of Sampling

**Authors:** Jingbo Liu

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27769v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27769v1)

**Summary:** We study the query complexity of sampling from high-dimensional Gaussian distributions using gradient information. In the standard oracle model, exact gradients expose only matrix-vector products with the precision matrix, leading to polynomial approximation barriers and a characteristic \(\sqrtκ\) dependence on the condition number. We show that this barrier disappears when the sampler is allowed to query \emph{smoothed scores}, namely gradients of the logarithms of the Gaussian-convolved densi...

---

### 28. Soft Specialists: $α$-Rényi Ensembles for Uncertainty-Aware LLM Post-Training

**Authors:** Paula Cordero-Encinar, Georgy Tyukin, Andrew B. Duncan

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27747v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27747v1)

**Summary:** Existing training approaches for large language models learn a single set of parameters, based on large volumes of data, which is typically heterogeneous, conflicting and often outright contradictory. As a result, the model is forced to compress conflicting goals, and inherent uncertainties into a single, averaged pattern of behaviour. We propose an $α$-Rényi variational framework for learning distributions over post-training parameters, offering an uncertainty-aware alternative to deep ensemble...

---

### 29. Unsupervised Identification and Removal of Spurious Correlations During Fine-Tuning

**Authors:** Ciarán M. Gilligan-Lee, Joseph Egan, Yuchen Zhu, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27676v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27676v1)

**Summary:** Fine-tuning a pretrained language model on a curated dataset can produce spurious correlations between the fine-tuning task and unintended latent factors -- such as misaligned personas or political slant -- that the curation procedure has entangled with the task. The model can latch onto these spurious correlations, leading to bias and reduced out-of-distribution generalisation. We prove that under reasonable assumptions on task complexity and the spurious correlation, such latent factors can be...

---

### 30. Evolving and Detecting Multi-Turn Deception using Geometric Signatures

**Authors:** Surender Suresh Kumar, Mary L. Cummings

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27671v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27671v1)

**Summary:** Safety defenses for large language models (LLMs) are typically trained and evaluated on single-turn prompts, yet real attacks often unfold as indirect, multi-turn probing. To defend against this more nuanced form of deception, we present a unified pipeline that generates realistic multi-turn deceptive question sets via multi-objective genetic prompt optimization with co-evolving mutation operators. We validate this dataset through a human study, which also revealed that early generations yielded...

---

### 31. Proper Agnostic Learning of Functions of Halfspaces under Gaussian Marginals

**Authors:** Sergei Tikhonov, Arsen Vasilyan

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27594v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27594v1)

**Summary:** We study the problem of computationally efficient proper agnostic learning of multidimensional concept classes under the Gaussian distribution. In this setting, given i.i.d. labeled samples from an unknown distribution over $\mathbb{R}^d \times \{\pm 1\}$ whose marginal on $\mathbb{R}^d$ is Gaussian, the goal is to output a hypothesis from a target class $\mathcal{F}$ whose 0-1 loss is within $ε$ of that of the best classifier in $\mathcal{F}$.   We give the first efficient proper agnostic learn...

---

### 32. On the Subgaussianity of Quantized Linear Maps: An AI-Assisted Note

**Authors:** Guangyi Zou, Roman Vershynin

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27563v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27563v1)

**Summary:** This short note presents a dimension-independent subgaussian concentration bound for Gaussian vectors under coordinate-wise nonlinear mappings. Discovered by Gemini 3.5 Flash, this result applies to any bounded function under a well-conditioned covariance. We apply this tool to answer a question of Simone Bombari on sign-quantized linear maps $Y = \text{sgn}(Wx)$.

---

### 33. The Fundamental Limits of Fraud Detection in Card Payment Networks

**Authors:** Gaurav Dhama

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27557v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27557v1)

**Summary:** Card payment fraud detection is usually framed as a supervised classification problem. Although this approach has generated practical progress, improvement has remained incremental despite major advances in model architecture. We argue that this is not mainly a failure of function approximation or optimization, but a consequence of structural information impairments inherent to the payment ecosystem.   We formalize card authorization as a sequential decision problem with delayed, censored, corru...

---

### 34. Accelerating Reinforcement Learning Training Using Simulation Surrogate Models

**Authors:** Mohammadmahdi Ghasemloo, David J. Eckman, Yaxian Li

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27556v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27556v1)

**Summary:** High-fidelity simulation models are widely used to analyze complex stochastic systems, but their high computational cost motivates the development of cheaper surrogate models that approximate the simulation model's input-output relationship. In parallel, reinforcement learning (RL) has emerged as a powerful framework for making online decisions in stochastic environments, with increasing attention being given to the use of simulation models as training environments for RL models. We investigate ...

---

### 35. Semiparametrically Efficient Inference for Kernel Measures of Noise Heterogeneity

**Authors:** Jakub Wornbard, Zikai Shen, Dimitri Meunier, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27526v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27526v1)

**Summary:** We develop semiparametrically efficient inference for kernel measures of noise heterogeneity in additive noise models. In many applications, the regression function is estimated using flexible machine learning methods. Downstream procedures based on the resulting residuals can then inherit first-stage bias: regression error may induce spurious dependence between covariates and residuals, invalidating the assumptions needed for standard analysis. We construct a novel Hilbert-valued one-step estim...

---

### 36. Identifiable Bayesian Deep Generative Copulas with Unknown Layer Widths for Data with Arbitrary Marginal Distributions

**Authors:** Joseph Feldman, Yuqi Gu

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27523v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27523v1)

**Summary:** Deep generative models offer powerful tools for multivariate data analysis, but their black-box architectures are often unidentified and difficult to interpret. We introduce the Deep Discrete Encoder (DDE) Copula, an identifiable and interpretable generative model for multivariate data with arbitrary marginal distributions. The model places a hierarchical directed network of binary latent variables inside a copula framework, enabling flexible dependence modeling for mixed discrete and continuous...

---

### 37. GenSBI: Generative Methods for Simulation-Based Inference in JAX

**Authors:** Aurelio Amerio

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27499v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27499v1)

**Summary:** Flow and diffusion generative models have established themselves as widely adopted density estimators for simulation-based inference (SBI), extending naturally from neural posterior estimation to likelihood and joint density estimation. Their principled optimization objectives and freedom from architectural constraints have driven rapid adoption across the natural sciences. Yet the most widely used SBI libraries remain PyTorch-based, leaving researchers who develop their forward models and analy...

---

### 38. From Scores to Gibbs Correctors: Accelerating Uniform-Rate Discrete Diffusion Models

**Authors:** Yuchen Liang, Ness Shroff, Yingbin Liang

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27352v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27352v1)

**Summary:** Discrete diffusion models have achieved strong empirical performance in text and other symbolic domains, but, especially for uniform-rate models, they often require many steps to generate a single sample. Existing acceleration methods either rely on training additional quantities or suffer from slow mixing. In this work, we propose a novel Gibbs-based corrector for discrete diffusion models, termed Gibbs-Accelerated Discrete Diffusion (GADD). GADD leverages the structure of the concrete score fu...

---

### 39. BASIS: Batchwise Advantage Estimation from Single-Rollout Information Sharing for LLM Reasoning

**Authors:** Shijin Gong, Erhan Xu, Kai Ye, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27293v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27293v1)

**Summary:** Reinforcement learning with verifiable rewards has become a standard recipe for improving the reasoning abilities of large language models. Existing algorithms face a tradeoff between computational efficiency and sample efficiency in value estimation and policy learning. We introduce BASIS, a critic-free post-training algorithm designed to address this tradeoff. At each online training step, BASIS samples only one rollout per prompt, but leverages rich information across prompts in the entire ba...

---

### 40. Detectability in Diversity: Improved Canary Crafting for Privacy Auditing in One Run

**Authors:** Mathieu Dagréou, Aurélien Bellet

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27292v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27292v1)

**Summary:** Privacy auditing aims to empirically assess privacy leakage in machine learning models using membership inference attacks (MIAs), and to derive lower bounds on differential privacy (DP) parameters. Recent one-run auditing methods address the high cost of standard approaches by relying on a single training run with multiple "canary" points whose inclusion or exclusion must be detected by the auditor. In this work, we study the problem of efficiently crafting canaries for one-run privacy auditing....

---

### 41. Causal Risk Minimization for High-Dimensional Treatments

**Authors:** Nikita Dhawan, Arnav Paruthi, Andrew Kim, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27281v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27281v1)

**Summary:** Predicting the effect of interventions with many possible variations, e.g., therapeutic content that affects mental health outcomes or an earnings call transcript that drives movement in share price, is useful across several domains. However, classical causal estimators tend to assume that all possible interventions are observed, which is infeasible when interventions vary widely, for instance, in the space of all text strings. We adapt a well-known approach of recasting causal inference as a le...

---

### 42. Inverse Control Constrained Optimization of Vessel Speed Decisions Under Environmental Risk: Evidence from Arctic Shipping

**Authors:** Mauli Pant, Linda Fernandez, Indranil Sahoo

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27270v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27270v1)

**Summary:** Understanding how decision makers balance operational efficiency with environmental and ecological risks is central to vessel navigation. We model vessel speed as a control variable in a constrained optimization framework in which vessel operators balance multiple competing objectives, including transit efficiency, ice related navigational risk, and whale related ecological risk. The underlying risk parameters are estimated using over 14 million Automatic Identification System (AIS) observations...

---

### 43. Nonlinear Data Integration via Kernel Methods for Data Collaboration Analysis

**Authors:** Yamato Suetake, Yuta Kawakami, Shunnosuke Ikeda, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27219v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27219v1)

**Summary:** Collaborative analysis of decentralized confidential datasets is important, but direct sharing of original datasets is often restricted by privacy and institutional constraints. Data collaboration (DC) analysis transforms each dataset into privacy-preserving intermediate representations via party-specific obfuscation functions and integrates them into common collaboration representations using an anchor dataset. However, many existing DC analysis methods rely on linear transformations for data o...

---

### 44. The Role of Causal Features in Strategic Classification for Robustness and Alignment

**Authors:** Antonio Gois, Sophia Gunluk, Nir Rosenfeld, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27163v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27163v1)

**Summary:** In strategic classification, an institution (e.g., a bank) anticipates adaptation from users who change their features to increase utility in a classification task (e.g., loan repayment). Since a key challenge is the distribution shift induced by users, we turn to causal models, which have been shown to bound the worst-case out-of-distribution (OOD) risk, and establish several new results that link causality and strategic classification. First, we show that causal classification leads to optimal...

---

### 45. Mildly Overparameterized ReLU Networks on Orthogonal Data: Incremental Learning and Implicit Bias

**Authors:** James Town, Etienne Boursier, Ben Lewis, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27097v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27097v1)

**Summary:** The successful training of neural networks hinges on the use of first order optimization methods, yet the theoretical characterization of these methods remains incomplete. This is especially true in settings with mild overparameterization. In this work, we study the gradient flow dynamics of two-layer ReLU networks from small initialization with orthogonal training data. We prove the limiting flow converges to a saddle-to-saddle jump process as the initialization scale tends to zero, revealing a...

---

### 46. Gaussian Process-based learning with new MCMC-based implementation of Wishart prior on correlation matrix

**Authors:** Kane Warrior, Dalia Chakrabarty

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27093v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27093v1)

**Summary:** In probabilstic supervised learning of an input-output relationship - as a sample function of a Gaussian Process (GP) - priors are typically specified for the hyperparameters of the kernel that parametrises the covariance function of the GP, where the induced covariance matrix of the (resulting multivariate Normal) likelihood, governs the learning and prediction. When the sought function is highly multivariate, multiple lengthscale parameters must be learnt simultaneously, making inference diffi...

---

### 47. Causal Representation Learning for Generalisable Recommendation

**Authors:** Yorgos Felekis, Michael O'Riordan, Oriol Corcoll, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27043v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27043v1)

**Summary:** Predictive models trained on observational data often fail to generalise to the distributions they encounter when deployed, especially when the training data is a product of the system being optimised. Recommender systems are a canonical example: they are trained on interaction logs confounded by the deployed policy, past user behaviour, and platform filtering. As a result, the training distribution differs substantially from the candidate distribution scored at serving time, a gap that makes of...

---

### 48. Evaluating the Relevance of Uncertainty Estimators for LLM Hallucination

**Authors:** Yedidia Agnimo, Anna Korba, Annabelle Blangero, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27016v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27016v1)

**Summary:** Large language models (LLMs) are prone to hallucinations, i.e., statements unsupported by the input or training data, hindering reliable deployment. In parallel, numerous uncertainty estimation (UE) methods have been proposed to quantify model confidence and are often implicitly treated as proxies for model failure. However, the relationship between uncertainty and hallucinations remains insufficiently characterized. We present a systematic empirical study of the association between uncertainty ...

---

### 49. Sampling Data with Chains of Forward-Backward Diffusion Steps

**Authors:** Hyunmo Kang, Noam Itzhak Levi, Corinna Elena Wegner, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.27006v1) | 📄 [PDF](https://arxiv.org/pdf/2605.27006v1)

**Summary:** Sampling from learned high-dimensional distributions is a foundational computational problem. We introduce U-turn chains: Markov chains obtained by iterating short forward-backward steps of a diffusion model, in which each step proposes a move that remains on the learned data manifold and, paired with a Metropolis-Hastings correction, samples from energy-modified targets. For synthetic languages, we show that minimal U-turn dynamics undergoes an ergodicity-breaking phase transition driven by fra...

---

### 50. Constrained Bayesian Experimental Design via Online Planning

**Authors:** Yujia Guo, Daolang Huang, Xinyu Zhang, et al.

**Published:** 2026-05-26

🔗 [Paper](http://arxiv.org/abs/2605.26990v1) | 📄 [PDF](https://arxiv.org/pdf/2605.26990v1)

**Summary:** Bayesian experimental design (BED) is a principled framework for data-efficient design of sequential experiments. However, existing BED methods are unable to adapt to dynamic constraints inherent in real-world tasks due to budget limitations, varying costs, or physical constraints that restrict how designs evolve over time. In this paper, we introduce a novel approach to BED that enables constrained optimization of experimental designs by combining offline pre-training of an amortized policy and...

---

