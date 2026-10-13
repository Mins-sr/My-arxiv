# arXiv Daily Digest - 2026-10-13

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Can Language Models Play the Wikipedia Game?

**Authors:** Alexander Hickey, Joanna Knight, James Bishop

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13948v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13948v1)

**Summary:** Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. In the game, players must reach a target article using only article links. We compared sentence embedding models and LLMs across five Wikipedia languages and five academic-literature datasets. We const...

---

### 2. Hide and Seek: HIDE Concepts to SEEK explanations for black box models

**Authors:** Bhanu Tokas, Rahul Nair, Rockwell Jackson, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13935v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13935v1)

**Summary:** Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that...

---

### 3. Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early Stopping

**Authors:** Danil Rudenko, Georgii Bulgakov, Nikolay Kartashev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13909v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13909v1)

**Summary:** While deep learning models for tabular data have recently received significant research attention, the choice of objective functions for regression tasks remains an understudied degree of freedom. Several lines of research offer alternatives to the standard Mean Squared Error (MSE), but differences in datasets, backbones, and evaluation protocols make their practical benefits difficult to compare. In this work, we address this gap by performing a systematic re-evaluation of regression objectives...

---

### 4. Task Context Shapes Component Roles in Language Models

**Authors:** Sovesh Mohapatra, Dani S Bassett

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13895v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13895v1)

**Summary:** Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention ...

---

### 5. RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics

**Authors:** Weiliang Chen, Song Liao

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13889v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13889v1)

**Summary:** As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightw...

---

### 6. X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems

**Authors:** Yeonsung Jung, Zhiyuan Wang, Zifan Wang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13886v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13886v1)

**Summary:** Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying these compositional failures requires systematically exploring diverse cross-service paths. Existing red-teaming methods often simply prompt LLMs to identify potentially harmful paths from task and environment descriptions ...

---

### 7. Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga

**Authors:** Emilio Ferrara

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13840v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13840v1)

**Summary:** Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parse...

---

### 8. SpatialASM: Internalizing Active Mentalization for Spatial Reasoning

**Authors:** Yuhong Liu, Shenxi Wu, Junyi Chi, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13832v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13832v1)

**Summary:** When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Large Vision-Language Models (LVLMs) proactively think in the same way? We term this ability Active Spatial Mentalization (ASM), an intrinsic component of visual intelligence that remains substantially underdeveloped in current LVLMs. To bridge this gap, we introduce SpatialASM, a scalable framework to...

---

### 9. MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents

**Authors:** Jingwei Song, Zhisheng Chen, Bingfan Zeng, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13829v1)

**Summary:** A central challenge in embodied recursive self-improvement is enabling agents to convert interaction history into capabilities that persist beyond one world and transfer to later tasks. A saved memory or successful final action does not by itself establish that a reusable capability was acquired; evaluation must separate capability change from carried-over resources, unequal source exposure, and early execution failures. We construct MC-EvoBench as a controlled Minecraft benchmark with a fixed c...

---

### 10. Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing

**Authors:** Oktie Hassanzadeh, Dharmashankar Subramanian

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13823v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13823v1)

**Summary:** Semantic query engines ask a large language model (LLM) to judge individual rows, and benchmarks compare these engines on the quality of a few executions at temperature 0. We measure how much another execution changes. We re-execute the text and tabular workloads of SemBench, LRO-Bench, and UDA-Bench through their own harnesses, log every one of 1.2 million model calls, and reanalyze SemBench's published executions. At temperature 0, between 0.07% and 10.2% of rows change their operator output o...

---

### 11. FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial Recommender Systems

**Authors:** Vishnu Arun, Adam Obeng, Tianyou Wang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13806v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13806v1)

**Summary:** Production recommender systems have feature-lifecycle asymmetry: adding new features must produce gains on some metric, while feature removal must not regress any metric. In practice, feature deprecation is hard to prioritize as a feature can fail to be removed if it interacts with other features, its importance changes daily, it cannot be evaluated before production models change or data drift occurs, it is in contention for A/B test space with other launches, it causes regressions in an online...

---

### 12. Your Discrete Graph Diffusion Model is Secretly Memorizing

**Authors:** Adarsh Jamadandi, Nicolas Keriven

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13786v1)

**Summary:** Discrete graph diffusion models (GDMs) corrupt the graph structure by adding noise independently to nodes and edges under a Markovian noise model. In the unconditional setting without node features, an equivariant denoiser trained on a single graph is able to generate novel graphs and sample-level metrics such as edge overlap and WL kernel similarity find no evidence of memorization. In this work, we challenge this view and show for the first time that graph diffusion models indeed exhibit memor...

---

### 13. UkrMeme: Multimodal Explainable Persuasion Detection in Ukrainian Memes

**Authors:** Nazar Andrushko, Vera Schmitt, Veronika Solopova

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13783v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13783v1)

**Summary:** Memes play a central role in modern online communication, especially in contexts of political conflict where visual and textual cues combine to convey persuasive messages. We study persuasive technique detection in Ukrainian memes using vision-language models (VLMs). We introduce UkrMeme, a dataset of 200 organically produced Ukrainian wartime memes annotated for persuasion techniques, and PTM-UA, a Ukrainian translation of a subset of the Propaganda 950 benchmark that preserves original visual ...

---

### 14. ReplaySSM: Cache SSM Inputs, Not State

**Authors:** Ze-Wei Liou, Harris Nover, Amey Naik, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13778v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13778v1)

**Summary:** State-space models (SSMs) maintain a fixed-size recurrent state, but reading and writing it at every decoding step can bottleneck hybrid models. This eager state management causes large state I/O with low arithmetic intensity, leaves speculative decoding no cheap rollback, and feeds state quantization error into subsequent recurrent updates. We introduce ReplaySSM, which unrolls the recurrence to represent the state as a checkpoint and a buffer of recent SSM inputs. This separates output computa...

---

### 15. DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs

**Authors:** Mahsa Salmani, Sayeh Sharify, Hesham Mostafa

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13767v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13767v1)

**Summary:** Low-bit inference on accelerators with native 4-bit support requires quantizing both weights and activations to realize the full throughput gains these formats provide. While post-training weight quantization has been extensively studied, activation quantization remains considerably more challenging and typically requires calibration data. In this work, we introduce DUALQUANT, a dual-scale, calibration-free post-training quantization framework that directly minimizes the weight-reconstruction Me...

---

### 16. When Edge Independence Fails: Joint Graph Diffusion with Latent Sociability Priors

**Authors:** Adarsh Jamadandi, Nicolas Keriven, Aline Roumy

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13765v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13765v1)

**Summary:** Discrete graph diffusion models corrupt graph structure through independent edge updates with a Markovian noise model. Combined with the exchangeability requirement on the output distribution, the terminal prior is necessarily an Erdős--Rényi (E-R) random graph. This has a fundamental consequence for unconditional graph generation without node features: in the large graph limit, any GNN denoiser applied to an E-R graph approximately outputs an E-R graph, making effective denoising difficult. In ...

---

### 17. Matched-Context Group Policy Optimization for LLM Agent Training

**Authors:** Chenxu Zhang, Yaorui Shi, Wenlong Zhang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13755v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13755v1)

**Summary:** Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-Context Group Policy Optimization (MCGPO), a procedure for constructing weighted action preferences from already collected trajectories. MCGPO defines comparison contexts with pre-action st...

---

### 18. A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning

**Authors:** Mayug Maniparambil, Ayush Rai, Ekansh Verma, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13744v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13744v1)

**Summary:** On-policy self-distillation promises to replace the sparse outcome signal of verifiable-reward RL with dense token-level credit: a teacher conditioned on the reference solution scores the student's own rollout, and the resulting distributional shift is distilled back into the policy. We investigate whether this scoring signal actually contains corrective credit. Using gold error spans in student rollouts, we test the two signals consumed by self-distillation objectives, the full-distribution KL ...

---

### 19. SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning

**Authors:** Hongrui Zheng, Aditya Singh, Rahul Mangharam

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13737v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13737v1)

**Summary:** Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL, a constrained multi-agent reinforcement learning framework that allows for credit assignment even with joint constraint measurements. We use Signal Temporal Logic (STL) robustness to measure episode-level violation thr...

---

### 20. Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers

**Authors:** Yuhong Chou, Zehao Liu, Yuqi Pan, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13735v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13735v1)

**Summary:** Efficient attention mechanisms, such as linear and sliding window attention, aim to reduce the computational complexity of Transformers from quadratic to linear. However, their degraded in-context recall often necessitates interleaving full attention layers, leaving the quadratic bottleneck unresolved in long-context processing. To address this, we introduce Orthros attention, which shifts the efficiency paradigm from structural allocation to phase-aware decoupling. As a unified module, it dynam...

---

### 21. LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos

**Authors:** Zhiyuan Xiang, Peidong Liu, Mingyang Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13732v1)

**Summary:** Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data. Large-scale egocentric human videos offer a rich alternative, but they lack robot action labels, and existing action annotation methods are often noisy under real-world visual complexity and diverse manipulation dynamics. We introduce LAPT-Scale, a scalable latent action pre-training paradigm with two components: LAPT-Scale-LAM learns continuous latent actions by explaining frame-to-frame vis...

---

### 22. Amortized Counterfactual Prediction with Graph Neural Networks

**Authors:** Hendrik Stumpf, Francesco Quinzan

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13724v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13724v1)

**Summary:** Counterfactual inference asks how an observed outcome might have differed under different circumstances, such as whether a patient would have recovered had they received a different treatment. Such questions arise whenever decisions depend on the outcomes of alternatives that were not observed. Answering counterfactual queries generally requires knowledge of the underlying causal structure, which is often unavailable in practice. A common approach is therefore to first estimate the causal graph ...

---

### 23. Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy

**Authors:** Naji Alazhar, Wassel Alazhar

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13708v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13708v1)

**Summary:** Long-context serving runs out of KV memory before the hardware reaches its useful throughput. HiSparse stores history in host memory and fetches only the selected entries, but it uses one cache budget at every load and does not handle draft-model speculative decoding such as DSpark and DFlash2. We present Adaptive DHiSparse, which supports speculative decoding over hierarchical sparse KV and adapts residency to load. It protects the required working set, retains additional history while GPU memo...

---

### 24. A Baseline Assessment for the Agentic Web Technology Stack

**Authors:** Vagner Figueredo de Santana, Diogo Cortiz

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13703v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13703v1)

**Summary:** The fast pace in which protocols, frameworks, and technologies are being proposed for LLM-based agents results in a complex scenario for anyone aiming to create state-of-the-art AI solutions. Without an assessment on how different protocols, frameworks, and libraries work together to compose an Agentic Web solution, developers and organizations face different challenges (e.g., skilling, governance, infrastructure) even before becoming part of the Agentic Web ecosystem. In this context, we propos...

---

### 25. Calibration in One Go: Jointly Learning Accurate and Calibrated Neural Networks

**Authors:** Nektarios Kalampalikis, Pablo M. Olmos, Isabel Valera

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13693v1)

**Summary:** Neural networks (NNs), while highly flexible and versatile, are often poorly calibrated. Post-hoc calibration methods adjust the outputs of an already trained model using a separate calibration dataset and additional calibration parameters. This process adds overhead that requires separate optimization of the calibrator and subsequent model selection. In this paper, we show that standard (post-hoc) calibrators can be trained end-to-end with the backbone via a bilevel Stackelberg formulation. Thi...

---

### 26. Variance-Reduced Policy Gradient is Nearly Minimax-Optimal

**Authors:** Leonardo Cesani, Matteo Papini, Marcello Restelli

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13692v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13692v1)

**Summary:** Standard Policy Gradient (PG) algorithms suffer from high estimation variance because they rely on Monte Carlo updates. While off-policy variance reduction mitigates this problem, establishing optimal sample complexity currently requires either restrictive assumptions, such as uniformly bounded importance weights, or impractical second-order operations. In this work, we introduce Loopless Variance-Reduced PG (LVR-PG), a unified theoretical framework that abstracts a class of first-order estimato...

---

### 27. Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped Quadratic Kernels

**Authors:** Weiqi Sun, Qianyue Wu, Wenjia Wang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13674v1)

**Summary:** Linearizing softmax attention offers a route to efficient Transformer inference, but preserving pretrained attention remains challenging. We identify an important source of approximation error overlooked by standard linearization methods: a small number of outlier dimensions contribute disproportionately to query-key dot products and account for a large fraction of the approximation error. Motivated by this heterogeneity, we propose Outlier-Aware Attention Linearization (OAL), a dimension-aware ...

---

### 28. Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction

**Authors:** Jiwon Jeon, Myungsik Cho, Jeonghye Kim, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13672v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13672v1)

**Summary:** Large language models struggle to reliably identify and correct errors in their own reasoning. Unlike prior training-based approaches that fine-tune an LLM to generate revisions or feedback, we learn where to intervene in failed rollouts and determine how to redirect them. To choose where to intervene, we train a 130K-parameter MLP head on a frozen encoder using only final-answer correctness. For redirection, we find that under a fixed generation budget, the tested inline injections fail to reli...

---

### 29. A Step Harder, Not a Step Too Far: The Benefits and Limits of Curriculum Difficulty Progression in GRPO

**Authors:** Ronghan Li, Fei Chen, Mingyu Lu

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13669v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13669v1)

**Summary:** Curriculum learning typically organizes training samples from easy to hard. In GRPO, medium-difficulty samples are attractive for online selection because they are more likely to yield informative group-relative learning signals, and prioritizing them can improve training efficiency. However, it remains unclear whether persistently selecting such samples also leads to the strongest final model performance, or whether training can benefit from progressing toward harder samples. Meanwhile, sample ...

---

### 30. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

**Authors:** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13663v1)

**Summary:** Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the en...

---

### 31. Pretraining and Test-Time Training Budgets Matter for ARC: A Controlled Study of VARC and TRM

**Authors:** Adrien Deliege, Marc Van Droogenbroeck

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13660v1)

**Summary:** The Abstraction and Reasoning Corpus (ARC) is increasingly used to evaluate whether neural networks can infer task-specific transformations from few demonstrations. Recent ARC models differ in architecture, but also in broader training and evaluation protocols, including pretraining data, data augmentation, test-time setup, and optimization budgets, making conclusions about architecture benefits debatable. In this work, we study how the performance of the vision-inspired VARC and recursion-based...

---

### 32. SelectArena: A Modern Benchmark for Feature Selection on Real-world Tabular Data

**Authors:** Bastian Schäfer, Dominika Matus, Lennart Purucker, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13644v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13644v1)

**Summary:** Selecting a subset of features (columns) from a tabular dataset is a ubiquitous challenge in real-world applications. Industry experts seek to minimize model training costs, climate scientists require an interpretable subset of factors to understand extreme weather events, and clinicians need to choose among diagnostic tests due to financial and time constraints. When looking at the scientific literature to determine which feature selection method to use, practitioners across domains face an unr...

---

### 33. Learning Size Independent Constraint Models from Input Data and Positive and Negative Example Solutions

**Authors:** Helmut Simonis

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13640v1)

**Summary:** In this paper we describe a Constraint Acquisition Tool that generates size independent constraint programs from input data and positive and negative example solutions of multiple problem instances. The system finds size specific models based on typical constraint patterns over global and binary constraints, then generalizes the models to a size independent model that can be run on unseen input data. The system produces MiniZinc code as well as a textual description of the model. We evaluate the...

---

### 34. Model-agnostic Knowledge Augmented Machine Learning for Weakly Annotated Bioimaging Data

**Authors:** Jayanie Bogahawatte, Sachith Seneviratne, Simon Maksour, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13637v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13637v1)

**Summary:** Machine learning models are increasingly used for automated feature extraction from weakly annotated bioimaging data, such as microscopy and cytomorphology images. Due to the sole dependency of automated feature extraction, existing methods yield inconsistent classification performance across weakly annotated datasets. Here, we propose a model-agnostic knowledge augmentation method that enables ML models to exploit domain knowledge beyond what automated feature extraction can capture. The propos...

---

### 35. Humanize Olympiad Agents: A Multi-Session Workflow for Olympiad Problem Solving with Solve, Review, Wiki, Verify

**Authors:** Zhengyang Zhang, Jing Xiong, Hongzhou Lin, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13632v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13632v1)

**Summary:** Large language model (LLM) agents are rapidly improving on long-horizon scientific and olympiad tasks. Recent systems have produced a Lean-formalized resolution of the Navier--Stokes problem and autonomous solutions to four open questions in the Erdős Conjectures database. Yet neither system releases both its underlying model and complete inference stack. More broadly, a single agent session remains brittle on difficult problems: early errors can propagate, missing domain knowledge can stall pro...

---

### 36. SWE-DeceptionBench: Benchmarking Deceptive Behaviors of LLMs Across the Software Development Lifecycle

**Authors:** Xiting Liu, Lin Yang, Yitong Zhang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13626v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13626v1)

**Summary:** Large Language Models (LLMs) are increasingly used throughout the software development lifecycle. This growing reliance on LLMs raises concerns about their trustworthiness, with deception posing a particularly important risk. Deceptive behavior takes the form of misleading responses or assistance in fabricating, concealing, or distorting information. To study this behavior, we introduce SWE-DeceptionBench, a benchmark for evaluating LLM deception in software engineering. The benchmark covers six...

---

### 37. AudioTETRIS: Token Elimination via Transitional Importance Signals for Efficient Audio LLMs

**Authors:** Shreya Sajid, Anna Vettoruzzo, Joaquin Vanschoren

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13600v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13600v1)

**Summary:** Large Audio Language Models (LALMs) achieve strong performance on speech-text tasks, but standard audio encoders produce hundreds of tokens for even short audio clips. Because self-attention scales quadratically in sequence length, this inflates inference-time compute substantially. Current training-free token compression methods prune or merge tokens based solely on coarse attention or feature similarity. However, treating audio tokens as generic, isotropic features smooths over spectral transi...

---

### 38. MENTOR: Learning from Failure with On-Policy Pedagogical Intervention

**Authors:** Guanlan Yue, Hang Yu, Xiaoyong Huang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13594v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13594v1)

**Summary:** Reinforcement Learning from Verifiable Rewards (RLVR) is a key driver for Large Reasoning Models, but it is vulnerable to "zero-reward collapse", a training failure where a sudden increase in task difficulty causes the learning signal to vanish. We argue that the conventional approach of discarding these failed trajectories is wasteful, as they contain valuable diagnostic information about the model's cognitive gaps, a bright side that can be leveraged for recovery. Existing solutions, however, ...

---

### 39. Constructing Pareto Frontiers of Optimal Reasoning Termination Methods for Overthinking in Reasoning Models

**Authors:** Weixin Guan, Liang Li, Shiyu Xie, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13570v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13570v1)

**Summary:** Reasoning models can benefit from test-time scaling, but continued reasoning may become ineffective or harmful, a phenomenon termed overthinking. Evaluations against full thinking compare accuracy and token usage but lack references for overthinking severity and strategies' theoretical mitigation potential. To characterize overthinking at the model-task level, we first introduce Step-wise Truncation Probing (STP), repeatedly generating answers from multiple retained prefixes along each fixed sam...

---

### 40. Defence against the dark arts of distillation: Unsupervised discovery of subliminal learning

**Authors:** Joseph Egan, Ciarán M. Gilligan-Lee, Michael O'Riordan, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13536v1)

**Summary:** When a language model is distilled from a teacher that shares its base parameters, the student can inherit behavioural traits of the teacher---including misalignment---even from data that is semantically unrelated to the trait (Cloud et al., 2026). All existing defences require knowing the trait. We remove this requirement and prove that a subliminally transferred trait can be recovered from the parameter updates alone, without supervision, by exploiting a single asymmetry: the trait is expresse...

---

### 41. MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures

**Authors:** Loan Bernat, Matthieu Grard, Ariane Herbulot, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13534v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13534v1)

**Summary:** Long-horizon embodied agents must maintain task-relevant information, coordinate heterogeneous robots, and adapt their decisions as execution unfolds. Existing benchmarks investigate dynamic task execution and embodied multi-agent coordination, but provide limited evaluation of their intersection. We introduce MAGMA-Bench, an architecture-agnostic benchmark for persistent task reasoning in dynamic multi-robot environments. MAGMA-Bench evaluates agents across increasing task horizons and controll...

---

### 42. Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation

**Authors:** Shi-Yu Tian, Yong Liu, Ximan Liu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13521v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13521v1)

**Summary:** Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) by routing domain-specific data to specialized teachers, integrating their capabilities through dense token-level supervision on student-generated trajectories. However, domain routing only distinguishes the supervision sources for different domains; updates from all domains still act on shared parameters. When teachers differ substantially in response style and domain expertise, supervision that is effective in iso...

---

### 43. Causal Effect Identifiability in Causal Abstractions: A Strict Hierarchy of Criteria

**Authors:** Clément Yvernes, Marianne Clausel, Emilie Devijver, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13520v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13520v1)

**Summary:** Identifying causal effects from observational data typically requires a fully specified causal graph, an assumption that is often unrealistic in complex or high-dimensional settings. Causal abstractions address this limitation by retaining only partial causal information, thereby defining equivalence classes of compatible causal graphs. In this paper, we study causal effect identifiability directly at the level of these graph collections, rather than at the level of individual causal diagrams. W...

---

### 44. RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

**Authors:** David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13516v1)

**Summary:** Runtime failure monitors for robot policies are typically evaluated by how accurately they distinguish failed from successful executions. Yet an accurate alarm may arrive too late for recovery, while an unnecessary intervention may disrupt an execution that would otherwise succeed. We introduce RESCUE, a counterfactual framework for evaluating whether a monitor's alarms enable useful interventions. By restoring simulator and policy states at execution checkpoints, RESCUE compares alternative act...

---

### 45. Retrieval-Augmented Multimodal Language Model with Heterogeneous Evidence Integration for Clinical Prognosis

**Authors:** Hamza Shafiq, Jialu Tang, Ting Dang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13510v1)

**Summary:** Clinical prognosis requires integrating structured measurements, physiological waveforms, longitudinal history, and population context. We introduce PRISM (Population-Retrieved Inference for Structured Multimodal Prognosis), a multimodal language model that combines per-feature numerical tokenization, recency-weighted aggregation of longitudinal ECGs, and a dual-modality population memory bank. Retrieval operates in representation space: the model receives mean-pooled embeddings of similar train...

---

### 46. Beyond Temporal Proximity: Explanatory World Models for Credit Assignment in Reinforcement Learning

**Authors:** Oriol Corcoll, Qiyao Wei, Ciarán Mark Gilligan-Lee

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13504v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13504v1)

**Summary:** Generative Recommenders increasingly use Reinforcement Learning (RL) to optimize outcomes that may appear hundreds or thousands of interactions after a decision. Standard RL propagates reward according to temporal proximity rather than explicit relevance, attenuating the signal assigned to distant but important actions and creating a source of sample inefficiency. We introduce Explanatory World Models (EWM), an attribution framework that uses explanations to identify the earlier events that plau...

---

### 47. Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits

**Authors:** Changye Li, Zijian Zhang, Muheng Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13494v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13494v1)

**Summary:** Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often use context engineering, implemented through custom harnesses that manage tools, skills, and accumulated experience. However, we find that as single-session execution lengthens, the agent's reasoning intensity declines alongside slowing progress, summarized as long-horizon deceleration, and the benefits of these custom harnesses vanish as the underlying model improves, summarized as harness staleness. T...

---

### 48. Branching On-Policy Distillation

**Authors:** Dongyang Chen, Shudong Liu, Shubo Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13481v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13481v1)

**Summary:** On-policy distillation (OPD) provides teacher supervision on student-generated trajectories, but a single trajectory realizes only one continuation at each decision, limiting supervision coverage under a finite sampling budget. We propose BranchOPD (Branching On-Policy Distillation), which selects informative decision points using student uncertainty and teacher-student disagreement, resamples student-policy continuations from shared prefixes, and applies token-level teacher supervision to both ...

---

### 49. A Local Agentic AI Framework to Generate Edge Case Scenarios for Safety Assurance

**Authors:** Victoria J. Hodge, Colin Paterson, Rob Alexander

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13479v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13479v1)

**Summary:** Generating edge case scenarios is crucial for training, testing and safety assuring autonomous systems. This identifies hazardous failures to increase system reliability and robustness, ensures the system can still function safely on the boundaries of its operational design domain and learns the expected system behaviour for these edge cases. The rapid advancement in the generation and analysis capabilities of language models (LMs) has expanded their applicability and recent work has investigate...

---

### 50. When MLLMs miss what humans read: diagnosing and learning to read squint text

**Authors:** Chen Peng, Shan Huang, Jianbo Huang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13465v1)

**Summary:** Multimodal LLMs can fail to read text embedded in an image's coarse structure (text a human recovers by squinting) and report that no text is present. We name this class Squint Text and study it as a recognition deficiency, motivated by cases from a production moderation pipeline. We introduce SquintBench, comprising 1076 production-derived moderation images, and SquintCtrl, a controlled synthetic suite for mechanism diagnosis. Frozen-weight analysis shows that hidden text leaves a coarse signal...

---

## cs.CL

**50 papers**

### 1. RSI-Anything: Unlocking Recursive Self-Improvement with World Models

**Authors:** Taoyong Cui, Pinxian Zeng, Wanghan Xu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13912v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13912v1)

**Summary:** Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predictive world models to guide action and learning-data selection. Observed feedback drives policy or workflow improvement and conditional world-model adaptation, while component and compatibility checks g...

---

### 2. When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors

**Authors:** Shubh Garg, Chen Shani

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13910v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13910v1)

**Summary:** Vision-Language Models (VLMs) increasingly analyze and reason about images, yet it remains unclear whether their internal representations faithfully encode the structured relations required for such reasoning. We introduce EICS (Evaluation-Invariant Concept Stability), a metric for testing whether representations consistently encode concepts under controlled one-concept interventions, and CASP-VL (Causally controlled Spatial Perturbations for Vision-Language models), a benchmark of causally cont...

---

### 3. Structural Automata for Neural Semantic Parsing

**Authors:** Xiao Zhang

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13896v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13896v1)

**Summary:** Neural semantic parsers generate meaning representations token by token, yet well-formedness depends on references, scope, and graph relations that unfold during generation. Constrained decoding prevents locally invalid tokens but does not guarantee that a valid prefix can be completed within a fixed output-length limit. We investigate structural automata at three stages of DRS parsing (decoding, post hoc processing, and training) and additionally evaluate decoding on AMR. For decoding, we intro...

---

### 4. Task Context Shapes Component Roles in Language Models

**Authors:** Sovesh Mohapatra, Dani S Bassett

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13895v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13895v1)

**Summary:** Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention ...

---

### 5. Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga

**Authors:** Emilio Ferrara

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13840v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13840v1)

**Summary:** Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parse...

---

### 6. OpenPA: Forced-alignment-free Multi-granular Pronunciation Assessment with Mixed-transcript Adaptation

**Authors:** Fu-An Chao, Bi-Cheng Yan, Berlin Chen

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13826v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13826v1)

**Summary:** Recent advances in automatic pronunciation assessment (APA) have driven a shift from scripted to free-form assessment. However, existing methods often rely on multi-stage pipelines with forced alignment and separate feature extractors, limiting their practicality across response settings. In light of this, we propose OpenPA, a novel APA framework that leverages Whisper's cross-attention mechanism to jointly predict word- and utterance-level pronunciation scores without forced alignment. Through ...

---

### 7. Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection

**Authors:** Juan Terven, Diana-Margarita Córdova-Esparza, Ruben Gomez, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13821v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13821v1)

**Summary:** A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention. Across three training seeds and two held-out confidence thresholds, a learned answer selector improves threshold-averaged utility over the original model...

---

### 8. QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code

**Authors:** Meriem Terki, Nouhaila Innan, Minghao Shao, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13811v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13811v1)

**Summary:** Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a correct solution, but...

---

### 9. Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering and Breadth-Aware Selection for LLM Query Expansion

**Authors:** Amit Kumar Jaiswal, Sagar Uprety, Prayag Tiwari

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13810v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13810v1)

**Summary:** Large language models (LLMs) are now a standard source of query expansion terms but they hallucinate. They inject non existent entities and off-topic terms that add ranking noise and can hurt strong retrievers. Existing remedies such as corpus grounding, mutual verification and preference alignment treat hallucinated terms as an undifferentiated nuisance to be filtered by agreement heuristics, without a mechanistic account of why a given term appears or a principled criterion for how many terms ...

---

### 10. Error Rate is Not Enough: Costs of Augmentation in Low-Resource ASR

**Authors:** Katsumi Ibaraki, David Chiang

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13807v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13807v1)

**Summary:** Data augmentation is standard practice for low-resource automatic speech recognition (ASR), but its benefits are almost always reported as aggregate error rates, leaving open why and when a method helps. On four low-resource languages and English at five data sizes, we cross two augmentations that modify existing audio (speed perturbation and SpecAugment) with two that modify text transcriptions and synthesize audio from it. We analyze errors at the phoneme level and find that they help for comp...

---

### 11. REFLECT: Role-Aware Detection of Sentiment, Emotion, Politeness, and Formality

**Authors:** Sangpil Youm, Annabel Stocks Natalias, Hayden Heninger, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13797v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13797v1)

**Summary:** Detecting communicative meaning in dialogue requires modeling not only lexical content but also the participant-role structures through which sentiment, emotion, politeness, and formality (SEPF) are expressed. Existing approaches rely on contextual language representations while leaving semantic roles implicit. We introduce a role-aware transformer architecture that maps the four SEPF dimensions to theory-grounded Semantic Role Labeling (SRL) configurations, incorporating these configurations di...

---

### 12. Not Just an Evaluation: A Case Study of Discourse Particle Sensitivity in Language Models

**Authors:** William Sheffield, Jiahui Chen, Amy Zhang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13794v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13794v1)

**Summary:** Discourse particles subtly shape the flow of discourse by reflecting conversational context and interlocutor attitudes, often leaving the truth-conditional meaning untouched. They are also often polyfunctional, with distinct senses which partially overlap with other particles; for example, the exclusive use of English "just" and "only" ("John only/just drinks water"). Despite the frequency of these words in natural language, they have gone largely unstudied due to the subtle nature of their effe...

---

### 13. OccludeBench: Can VLMs Find What's Missing?

**Authors:** Jasin Cekinmez, Addison J. Wu, Ryo Mitsuhashi, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13790v1)

**Summary:** How well can vision-language models (VLMs) reason about what is missing from an image? We study this question with OccludeBench, a manually curated benchmark for recovering fully occluded objects from the visual evidence that remains. OccludeBench distinguishes direct cases, where the hidden object must be recovered from a specific physical cue such as a shadow or reflection, from inferential cases, where it can be inferred from broader scene context. Across five VLMs, accuracy averages 42.7% on...

---

### 14. UkrMeme: Multimodal Explainable Persuasion Detection in Ukrainian Memes

**Authors:** Nazar Andrushko, Vera Schmitt, Veronika Solopova

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13783v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13783v1)

**Summary:** Memes play a central role in modern online communication, especially in contexts of political conflict where visual and textual cues combine to convey persuasive messages. We study persuasive technique detection in Ukrainian memes using vision-language models (VLMs). We introduce UkrMeme, a dataset of 200 organically produced Ukrainian wartime memes annotated for persuasion techniques, and PTM-UA, a Ukrainian translation of a subset of the Propaganda 950 benchmark that preserves original visual ...

---

### 15. A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning

**Authors:** Mayug Maniparambil, Ayush Rai, Ekansh Verma, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13744v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13744v1)

**Summary:** On-policy self-distillation promises to replace the sparse outcome signal of verifiable-reward RL with dense token-level credit: a teacher conditioned on the reference solution scores the student's own rollout, and the resulting distributional shift is distilled back into the policy. We investigate whether this scoring signal actually contains corrective credit. Using gold error spans in student rollouts, we test the two signals consumed by self-distillation objectives, the full-distribution KL ...

---

### 16. Enhancing Legal Reasoning in Pre-trained Language Models via Knowledge Graph-Guided Multi-Task Pre-training

**Authors:** Ibrahim Siddig, Munir Georges

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13722v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13722v1)

**Summary:** Legal language understanding requires reasoning over semi-structured regulatory documents, yet standard pre-training objectives do not explicitly target this structural capability. Because current legal language models rely solely on masked language modeling, they treat statutory text as flat token sequences and ignore the underlying hierarchical constraints. To bridge this gap, we present a multi-task pre-training approach for German traffic law (StVO). Our approach combines three complementary...

---

### 17. Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy

**Authors:** Naji Alazhar, Wassel Alazhar

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13708v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13708v1)

**Summary:** Long-context serving runs out of KV memory before the hardware reaches its useful throughput. HiSparse stores history in host memory and fetches only the selected entries, but it uses one cache budget at every load and does not handle draft-model speculative decoding such as DSpark and DFlash2. We present Adaptive DHiSparse, which supports speculative decoding over hierarchical sparse KV and adapts residency to load. It protects the required working set, retains additional history while GPU memo...

---

### 18. Verifiable Retrieval for Legal Reasoning through Structure-driven Knowledge Graph

**Authors:** Ibrahim Siddig, Sviatoslav Tugeev, Munir Georges

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13695v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13695v1)

**Summary:** Any automation within reliability-critical contexts such as medicine or law has to be transparent and verifiable. Despite their advantages, current LLM-based systems do not meet these requirements due to their inherent black-box nature. Retrieval Augmented Generation (RAG) attempts to ground the generative process in the relevant interpretable documents, thereby reducing the risk of AI 'hallucinations' and potentially enabling verification of the initial generation context. However, as the numbe...

---

### 19. Retractions Revisited: A Replication, Extension, and Mechanistic Evaluation of Linguistic Obfuscation Effects in Fraudulent Science

**Authors:** David M. Markowitz

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13678v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13678v1)

**Summary:** Prior work suggests fraudulent scientists write their articles with higher rates of linguistic obfuscation than genuine scientists, with a possible mechanism suggesting obfuscation makes research more costly for a reader to analyze. This result has not undergone additional empirical scrutiny in the open science era, nor have other psychological mechanisms been evaluated. The current replication and extension addressed this opportunity by comparing 800 fraudulent and 800 genuine control papers (2...

---

### 20. Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction

**Authors:** Jiwon Jeon, Myungsik Cho, Jeonghye Kim, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13672v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13672v1)

**Summary:** Large language models struggle to reliably identify and correct errors in their own reasoning. Unlike prior training-based approaches that fine-tune an LLM to generate revisions or feedback, we learn where to intervene in failed rollouts and determine how to redirect them. To choose where to intervene, we train a 130K-parameter MLP head on a frozen encoder using only final-answer correctness. For redirection, we find that under a fixed generation budget, the tested inline injections fail to reli...

---

### 21. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

**Authors:** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13663v1)

**Summary:** Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the en...

---

### 22. Multi-Stream Attention Residuals

**Authors:** Xiaohan Qin, Xiangdong Zhang, Tuo Dai, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13630v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13630v1)

**Summary:** Attention Residuals (AttnRes) enables content-dependent retrieval over network depth, which can be viewed as single-stream softmax attention along the depth axis. Inspired by the success of multi-head attention along the sequence axis, we introduce Multi-Stream Attention Residuals (MSAR), an extension of AttnRes that generalizes this mechanism to multi-head depth attention, yielding substantial performance gains with minimal additional overhead. MSAR draws stream diversity from sequence context ...

---

### 23. AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis

**Authors:** Natapong Nitarach, Phume Ngampornsukswadi, Pittawat Taveekitworachai, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13627v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13627v1)

**Summary:** Evaluating large language models (LLMs) on AMLworld's smallest test splits is costly because each of over a million targets requires a separate graph prompt. Sampling reduces this cost, but small balanced subsets change unweighted precision and F1. We introduce AMLworld-Compact, an evaluation set that retains every illicit test transaction and samples benign transactions from supervised-score strata. Its HT-Coreset protocol reduces evaluation targets by 271x and 611x on HI-Small and LI-Small. Ho...

---

### 24. APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces

**Authors:** Ziyi Yang, Adel Bibi, Guohao Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13623v1)

**Summary:** Professional agents increasingly work through command-line interfaces and multiple tools over shared workspaces containing files, messages, and business applications. These environments create safety risks that are difficult to capture with attacks placed at a single, known read location. We introduce APEX-Harm, a benchmark for evaluating prompt and script injection against long-horizon agents performing finance, consulting, and legal tasks in large workspaces. Each task contains 115 to 328 file...

---

### 25. Training User Simulators with Latent Intrinsic Feedback

**Authors:** Tarek Naous, Craig Boutilier, Wei Xu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13617v1)

**Summary:** User simulators are gaining attention as environments to train LLM assistants that can better cope with the nuances of multi-turn conversations with real users. Prior work on user simulation has emphasized generating realistic user utterances, leaving unexplored their potential as a source of direct feedback on the assistant's responses. Such evaluation signals may not be explicitly communicated in language, but can instead reside in the latent reasoning of users. In this work, we introduce user...

---

### 26. BLiMPPI: Benchmark of Linguistic Minimal Pairs for Polarity Items

**Authors:** Arzu Burcu Güven, Anna Rogers, Leonie Weissweiler, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13607v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13607v1)

**Summary:** Negative polarity items (NPIs), such as "anymore" and "ever", are grammatical only in select environments, predominantly in the context of negation. Because their grammaticality depends on both syntax and semantics, they have a rich, multilingual literature in theoretical linguistics, yet work on NPIs in language models is almost entirely confined to English. We introduce BLiMPPI, a multilingual evaluation suite of over 12,000 NPI minimal pairs in 33 languages, built by a pipeline that discovers...

---

### 27. zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss

**Authors:** Saibo Geng, Andrea Gentilini, Xinxian Ma, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13605v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13605v1)

**Summary:** Dynamic vocabularies built on-the-fly via Lempel-Ziv-Welch (LZW) compression let a language model represent the same text in fewer tokens, but prior work shows that this efficiency comes at a cost to reasoning and perplexity. We show that this quality gap is not a fundamental price of compression but can be substantially closed through targeted improvements to the compression layer and LZW codec, without modifying the underlying pretrained language model. Our analysis reveals four key issues: (1...

---

### 28. Measuring Artifact Reliance in Machine-Generated Text Detectors

**Authors:** Anastasia Voznyuk, Andrey Grabovoy

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13583v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13583v1)

**Summary:** Detectors of machine-generated text score almost perfectly on scientific-literature benchmarks, implying we can reliably distinguish with these detectors human and machine-generated documents. We looked at ten scientific-document subsets from six popular resources, and on several of them that apparent ease is a side effect of how the documents were put together. A logistic regression using 27 superficial features reached 0.833-0.997 macro-F1, and on the three arXiv subsets it outperformed every ...

---

### 29. Not All Correct Fixes Run Alike: An Empirical Study of Patch Performance in Repository-Level Issue Resolution

**Authors:** Han Peng, Xing Hu, Feifei Niu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13563v1)

**Summary:** Repository-level issue-resolution benchmarks such as SWE-bench evaluate submitted patches primarily based on whether they pass the correctness tests, leaving the runtime performance of different test-passing patches largely unexplored. Evaluating patch performance is essential but challenging since designing performance workloads for each benchmark instance is costly. However, these benchmarks already provide a natural candidate: the built-in \emph{FAIL\_TO\_PASS} (F2P) tests, which exercise the...

---

### 30. Personalization Without Stereotyping: Do Speech LLMs Know When to Turn a Deaf Ear?

**Authors:** Kshitij Ambilduke, Caroline Brun, Thibaut Thonet, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13550v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13550v1)

**Summary:** Recent speech LLMs can leverage rich paralinguistic cues, enabling more complex and personalized interactions. However, little work investigates how this sensitivity can lead to stereotyping, and existing evaluations largely measure demographic disparities without distinguishing beneficial personalization from stereotypical behavior. We introduce BASIS-Bench, a benchmark designed to disentangle these two aspects through three axes: (1) demographic robustness, measuring disparities in content-bas...

---

### 31. S-Space: Exploring Spatial Workspace in Multimodal Language Models

**Authors:** Zhiyuan Shi, Xiang Li, Xingzhuo Guo, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13527v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13527v1)

**Summary:** Multimodal language models (MLLMs) exhibit promising spatial reasoning capabilities, yet the internal mechanisms supporting them remain poorly understood. We uncover S-Space, a linear representation subspace in which object-token representations encode continuous coordinates along horizontal, vertical, and distance axes. Although we identify these axes by differentiating spatial-answer scores with respect to object-token activations, S-Space is intrinsic rather than induced by specific data or p...

---

### 32. Retrieval-Augmented Multimodal Language Model with Heterogeneous Evidence Integration for Clinical Prognosis

**Authors:** Hamza Shafiq, Jialu Tang, Ting Dang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13510v1)

**Summary:** Clinical prognosis requires integrating structured measurements, physiological waveforms, longitudinal history, and population context. We introduce PRISM (Population-Retrieved Inference for Structured Multimodal Prognosis), a multimodal language model that combines per-feature numerical tokenization, recency-weighted aggregation of longitudinal ECGs, and a dual-modality population memory bank. Retrieval operates in representation space: the model receives mean-pooled embeddings of similar train...

---

### 33. Proactive Agentic Orchestration

**Authors:** Xueyang Feng, Chaozhuo Li, Xiaohe Bo, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13485v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13485v1)

**Summary:** Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents. However, existing orchestration methods face two limitations: in execution, current methods fix sub-agents' goals and harnesses at creation time, limiting their adaptability to dynamic real-world environments; in optimization, sparse and delayed feedback constrains effective learning of the orchestration policy. To addres...

---

### 34. A Better Metric Will Not Save You: What You Compare Beats How You Compare It

**Authors:** Noureddine Khaous, Guillaume Wisniewski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13476v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13476v1)

**Summary:** Representational similarity measures (RSA, CKA, Procrustes) are chosen for the transformations they treat as irrelevant, and all of them take the set of conditions as given. That set is fixed by two decisions, which inputs are admitted and how they are grouped, both taken before the matrix a measure operates on exists: no invariance property reaches them. We measure what they are worth where the arrangement the conditions ought to have is known independently of the systems compared, the acoustic...

---

### 35. Towards Enriching Design-Time Models with Evidence from Simulation and Operational Activities

**Authors:** Barbara da Silva Oliveira, Julien Deantoni, Nicolas Ferry

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13456v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13456v1)

**Summary:** Cyber-Physical Systems are developed through multiple model based activities, comprising several stages of development. As the development progresses through simulation, experimentation, and operation, observations of system execution may reveal missing, uncertain, or invalid design knowledge. The path from execution results to persistent design-time enrichment, however, is often implicit. This paper addresses this challenge by proposing an evidence driven workflow for systematically transferrin...

---

### 36. Oído: Open-Vocabulary Speech Recognition on a $5 Microcontroller without a Neural Accelerator

**Authors:** Daniel Varela Sánchez, Guillermo Martín-Coello Juárez

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13447v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13447v1)

**Summary:** Speech recognition on low-cost microcontrollers is, in practice, limited to keyword spotting or a fixed list of commands. We present Oído, an inference engine that runs open-vocabulary English speech recognition entirely on an ESP32-S3 (240 MHz dual-core Xtensa LX7, 512 KB of SRAM, 8 MB of PSRAM, 16 MB of flash, no neural accelerator). Oído executes a 13M-parameter Conformer-CTC model with int8 weights, per-frame dynamic int8 activations and int8 attention on the chip's SIMD instructions, with a...

---

### 37. Revisiting Accent Classification with DistilHuBERT: Speaker-Disjoint Evaluation and Cross-Corpus Generalization

**Authors:** Xu He, Homayoon Beigi

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13440v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13440v1)

**Summary:** Recent accent classification systems can achieve high accuracy in standard in-corpus evaluations. However, when speakers overlap between the training and test sets, such results may overestimate model robustness compared with real-world deployment scenarios. This study revisits the robustness of DistilHuBERT-based accent classification by using L2-ARCTIC and multiple external English accent datasets. The comparison covers file-level and speaker-disjoint splits, along with balanced external-data ...

---

### 38. Does Financial Speech Need Continual Learning Regularization? A Study of EWC and mini-KFAC on Earnings Call ASR

**Authors:** Thai Quoc On, Homayoon Beigi

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13432v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13432v1)

**Summary:** Earnings call transcription presents a realistic continual learning scenario where Automatic Speech Recognition (ASR) systems are updated with new recordings but risk catastrophic forgetting of previously learned financial speech patterns. Adapting Whisper-small from a general-domain speech corpus to the Earnings22 benchmark reveals the opposite: all evaluated methods exhibit improvement on held-out financial speech from the same domain during adaptation rather than forgetting. This task complem...

---

### 39. Towards the Roof of the World: NLP Progress in Tibetan Languages

**Authors:** Xi Cao, Yijie Li, Yuan Sun, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13398v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13398v1)

**Summary:** Tibetan, spoken by some seven million people on and around the Qinghai-Xizang Plateau, remains underrepresented in natural language processing (NLP). We present, to our knowledge, the first peer-reviewed systematic bibliometric survey of Tibetan NLP: 140 publications from 2004 to 2026 in the ACL Anthology and DBLP, annotated for venue type, research area, first-affiliation country, and resource release. Output has grown rapidly, with 84% of the publications appearing since 2018, and has expanded...

---

### 40. ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents

**Authors:** Chengyi Yang, Renxu Bao, Jue Hou, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13395v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13395v1)

**Summary:** Coding agents are increasingly used to build programs from scratch as software engineers do rather than to resolve issues within a repository or to generate a repository from a given requirements document. However, scalable verifiable training environments that force agents to discover what is required and to decide how the system should be designed remain scarce. Moreover, existing agent workflows also cannot sustain long-horizon development in which the agent explores the reference program bef...

---

### 41. MoPrO-SD: Modular Prompt Optimization for Stance Detection

**Authors:** Meysam Sabbaghan, Nikesh Gyawali, Arman Zareian Jahromi, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13386v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13386v1)

**Summary:** Stance detection remains challenging for large language models (LLMs) due to implicit opinions, sarcasm, and context-dependent expressions of stance. Although automatic prompt optimization offers an alternative to fine-tuning without updating model parameters, existing structured approaches are not specifically designed around stance-label semantics and class-specific ambiguities. We introduce MoPrO-SD, a stance-specific prompt optimization framework that decomposes prompts into functional seman...

---

### 42. From Structure to Validity: Mechanism-Guided Generation and Refinement of LLM Rubrics

**Authors:** Feifei Qian, Xuan Chen, Lixin Cui, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13375v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13375v1)

**Summary:** Rubrics have been widely used to evaluate and optimize language models on open-ended tasks. However, existing work primarily focuses on generating better rubrics, with limited understanding of what makes rubric design effective. In this work, we conduct a systematic mechanistic analysis of rubric design across criterion organization, criterion operationalization, and score aggregation. Our analysis shows that structural organization enables more comprehensive criterion construction, semantic spe...

---

### 43. Overcoming Data Imbalances with Expert Selection Biases

**Authors:** Ayush K. Tarun, Clara Meister, Antoine Bosselut

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13370v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13370v1)

**Summary:** Mixture-of-Experts (MoE) models have become the standard architecture for frontier LLMs. The multiple parallel experts in each transformer block theoretically enable expert specialization according to categories such as domains, languages, or modalities during pretraining. However, when data is imbalanced across categories, minority categories can become concentrated in a small fraction of the expert pool or spread inefficiently across them, effectively limiting their available capacity. In this...

---

### 44. Test-Time Memory Construction

**Authors:** Zijun Wang, Yifan Ji, Haidong Xin, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13348v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13348v1)

**Summary:** Large Language Models (LLMs) struggle to answer questions over long interaction histories, where relevant evidence may be scattered across distant sessions. Existing memory systems typically construct and maintain sophisticated memory representations offline, before user queries are observed, incurring substantial overhead and limiting their ability to adapt memory construction to query-specific information needs. In this paper, we propose T$^2$Mem, a Test-Time Memory construction framework that...

---

### 45. Exploring Attention Sinks in Text-to-Image Transformers from Diffusion and Autoregressive Models

**Authors:** Binglei Li, Mengping Yang, Zhiyu Tan, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13337v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13337v1)

**Summary:** Attention sinks are tokens or positions that consistently receive disproportionate attention mass, often beyond what their semantic content would suggest. Despite extensive study in large language models, their behavior and functional relevance in text-to-image (T2I) Transformers remain largely unexplored. To fill this gap and better understand how text-to-image Transformers allocate and route attention, we explore this phenomenon of text-to-image transformers across bidirectional diffusion mode...

---

### 46. Taking Tokenization off the Host for Agentic LLM Serving

**Authors:** Mohammad Siavashi, Pascal Schwinte, Ali Banaei, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13325v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13325v1)

**Summary:** Agentic workloads resend long contexts that barely change between calls. Prefix caching now skips most of their prefill, yet every request must still be tokenized in full before the cache can even be consulted. Tokenization, a CPU stage long treated as negligible, becomes the largest part of time-to-first-token (TTFT), and a frontend that tokenizes for a whole GPU fleet limits how many GPUs it can feed. We present GraphTok, a GPU tokenizer that runs the entire encoding pipeline, from pre-tokeniz...

---

### 47. Host-Aware Web Crawling for LLM Pretraining Data

**Authors:** Malte Ostendorff

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13321v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13321v1)

**Summary:** Web crawling is a major source of large language model (LLM) pretraining data, yet data-selection pipelines discard a large share of crawled pages. We investigate how a crawler should allocate its budget across and within hosts to collect more high-quality pretraining data. Combining document-level quality classifier scores, web-graph centrality metrics, and Common Crawl's per-host crawl coverage, we find that roughly half of the variation in classifier scores occurs between hosts. In the crawls...

---

### 48. Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans

**Authors:** Sangdo Han, Moonsoo Kim

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13303v1)

**Summary:** LLM judges are increasingly deployed as panels, and disagreement among panel members is often read as a symptom of an unclear rubric. We test a label-free procedure that turns this disagreement into rubric repairs. The procedure decomposes each rubric into sub-criteria, ranks them by cross-judge disagreement on a development split, and has an editor model rewrite only the most contested ones. An additional stage that moves text-checkable sub-criteria to deterministic checkers transferred none in...

---

### 49. Do Prompt Optimizers Break Requirements They Are Not Scored On? A Preregistered Study

**Authors:** Sangdo Han, Moonsoo Kim

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13287v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13287v1)

**Summary:** Prompt optimizers rewrite a prompt to raise one target metric, but prompts also state requirements the metric does not score, such as an output format, citations, or abstention. In a preregistered study, we run GEPA, MIPROv2, and TextGrad on HotpotQA, SQuAD 2.0, and IFEval and count per-item violations of unscored requirements with deterministic checks. By the preregistered criterion, all three optimizers produce regressions, substantially on HotpotQA, where net regression in citation validity r...

---

### 50. BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation

**Authors:** Jiaming Su, Suorong Yang, Xudong Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13285v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13285v1)

**Summary:** Distilling long-chain reasoning trajectories from large teacher models provides an effective way to improve the reasoning ability of small language models. However, existing methods typically select a fixed training set before distillation, overlooking that the usefulness of a reasoning example changes as the student evolves. This mismatch becomes especially costly when only a small number of teacher trajectories can be used for training. Besides, examples already mastered provide little new sup...

---

## cs.CV

**50 papers**

### 1. Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark

**Authors:** Xudong Cai, Ruijie Zhu, Haoliang Shang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13947v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13947v1)

**Summary:** In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articraft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond geometry, appearance, and physically plausible articulation, such as collision-fre...

---

### 2. Splat2Act: From Captured Scenes to Personalized VLA Manipulation

**Authors:** Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13945v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13945v1)

**Summary:** A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive. We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy ...

---

### 3. InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators

**Authors:** Xuanlang Dai, Jiazi Bu, Yujie Zhou, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13944v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13944v1)

**Summary:** Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representations. Despite their remarkable generation capabilities, the cross-model alignment of latent representations and the consistency of their underlying denoising dynamics remain underexplored. In this work, we uncover an intriguing cross-model compatibility: independently trained generators exhibit similar...

---

### 4. Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback

**Authors:** Yucheng Yang, Xiaoxiao Sun, Shusheng Yang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13941v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13941v1)

**Summary:** Multimodal diffusion transformers (MMDiTs) allow the evolving image to update internal text representations through joint attention. These representations then guide subsequent image updates, raising a question: does this feedback help correct deviations from the prompt, or preserve them? We find that image-to-text (I2T) feedback can preserve the objects and attributes already represented in the evolving image, including errors. Transplanting I2T messages can rescue failures or disrupt successes...

---

### 5. Hide and Seek: HIDE Concepts to SEEK explanations for black box models

**Authors:** Bhanu Tokas, Rahul Nair, Rockwell Jackson, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13935v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13935v1)

**Summary:** Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that...

---

### 6. Chronos Policy: Learning Robot Policies on Physical Time

**Authors:** Changhao Wang, Jaden Clark, Shuran Song

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13929v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13929v1)

**Summary:** Robot policies often convert sensing and control into fixed-rate observation-action sequences, leaving physical time implicit in sequence position. This assumption breaks when observation rates or delays vary, or when inference latency changes. We introduce Chronos Policy, which makes physical time explicit by conditioning on observation capture times and desired action execution times. We study two ways to incorporate time into a diffusion transformer: adding timestamp embeddings to token featu...

---

### 7. Can machines reason non-verbally?

**Authors:** Shaheer U. Saeed, Zion Tse, Gregory Slabaugh, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13925v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13925v1)

**Summary:** Modern machines can solve equations, follow logic and reason through language, yet they still struggle with problems that require visual non-verbal reasoning. This is evident even in advanced systems such as DeepSeek, ChatGPT and Gemini, which remain limited on visual tasks such as completing abstract patterns or delineating ambiguous regions-of-interest. Unlike explicit intermediate steps in verbal reasoning which can be verified through logic or automated tests, visual reasoning involves impli...

---

### 8. Where to Look Matters: Rethinking Sub-Volume Sampling in 3D Medical Self-supervised Learning

**Authors:** Junkai Liu, Le Zhang

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13915v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13915v1)

**Summary:** Self-supervised learning on 3D medical images commonly relies on random sub-volume sampling during pretraining. However, random cropping implicitly treats all spatial regions as equally worth observing, despite anatomical priors and spatial redundancy that make regions inherently unequal in their value for representation learning. To this end, we first show through controlled crop-quality manipulations that better sub-volumes lead to better downstream transfer, revealing the observation policy a...

---

### 9. Beyond the Snowflakes: Disentangling Weather Effects from Confounding Meta-Factors in LiDAR Object Detection

**Authors:** Yiming Yang, Jeremy P. Bos

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13891v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13891v1)

**Summary:** Light Detection and Ranging (LiDAR) is critical for autonomous perception, yet its performance is known to degrade in adverse weather. While existing literature models snow as atmospheric noise that degrades performance, our granular evaluation on the WADS-3D and CADC datasets reveals a counter-intuitive phenomenon: detection accuracy consistently improves as snow intensity increases. Through ablation study and meta-information analysis, we reconcile this by confirming that while falling snow ac...

---

### 10. Tracking the Invisible: Self-Supervised Wheel Track Detection with Thermal-RGB Fusion

**Authors:** Yiming Yang, Jeremy P. Bos

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13872v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13872v1)

**Summary:** Accurate detection of drivable area is essential for autonomous driving and advanced driver assistance systems. While state-of-the-art methods focus on general traversability estimation, they prove inadequate for snow-covered roads where following existing wheel tracks offers crucial advantages: improved traction, predictable vehicle dynamics, and verified path stability. To address this, we propose a low-cost, self-supervised approach detecting safety-critical wheel tracks using synchronized RG...

---

### 11. Make It Flow: Animating Water in 3D Gaussian Splatting Scenes

**Authors:** Kjell Keune, Florian Hahlbohm, Jannis Möller, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13860v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13860v1)

**Summary:** Explicit 3D scene representations such as 3D Gaussian Splatting (3DGS) have recently enabled high-quality, real-time novel view synthesis. However, these methods assume static scenes, limiting realism in the presence of dynamic phenomena ubiquitous in real-world environments. While coherent motion (e.g., humans or vehicles) can be captured and reconstructed, high-frequency effects such as flowing water remain intractable under casual capture conditions, where dense multi-view, high-speed acquisi...

---

### 12. LapMerge: Differentiable Exact-Budget Token Merging in Linear Time

**Authors:** Magdalena Trędowicz, Aleksandra Nowak, Tomasz Steifer, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13858v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13858v1)

**Summary:** Modern vision and language models process ever longer token sequences, and reducing them is the main lever on downstream cost. Token compression, however, faces a fundamental trade-off: selecting tokens discards information, while existing merging methods preserve it only through pairwise token-to-token matching or $MN$ token-to-output interactions. We introduce LapMerge, a differentiable merging operator that resolves this trade-off for ordered sequences: a learned mass distribution partitions ...

---

### 13. Revisiting the Task of Building Damage Assessment by Satellite Imaging

**Authors:** Anthony Cioppa, Virgile Blua, Sébastien Piérard, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13857v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13857v1)

**Summary:** Natural disasters such as earthquakes, tropical storms, and floods cause extensive damage to buildings, and rapid, reliable damage maps are essential to guide emergency response. Automating this task, referred to as building damage assessment (BDA), from satellite imagery, has become an active research topic at the intersection of remote sensing, computer vision, and machine learning, particularly since supervised deep learning methods were shown to outperform earlier handcrafted approaches. Yet...

---

### 14. Event-based Action Recognition by Pre-Training on Multi-Frame Representations

**Authors:** Emma Norrby, Tomas Wilkinson, Per Nyblom, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13856v1)

**Summary:** Action recognition is a crucial task in domains like robotics, patient monitoring, or surveillance. Recently, event-based action recognition has attracted much attention due to the event camera's ability to capture fast motions and its improved privacy over conventional vision cameras. While frame-based event representations work well for short event sequences, their discriminative ability declines sharply with longer and more complex event sequences. In this work, we introduce a multi-frame rep...

---

### 15. SpatialASM: Internalizing Active Mentalization for Spatial Reasoning

**Authors:** Yuhong Liu, Shenxi Wu, Junyi Chi, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13832v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13832v1)

**Summary:** When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Large Vision-Language Models (LVLMs) proactively think in the same way? We term this ability Active Spatial Mentalization (ASM), an intrinsic component of visual intelligence that remains substantially underdeveloped in current LVLMs. To bridge this gap, we introduce SpatialASM, a scalable framework to...

---

### 16. Dream to Remember: Continual Steering of Generalist Robot Policies with World Models

**Authors:** Bahey Tharwat, Iman Nematollahi, Marvin Alles, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13816v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13816v1)

**Summary:** Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations. Reinforcement learning can improve and extend them, either by fine-tuning the policy weights or by training a small module to steer the input noise of a frozen generative policy. When tasks arrive sequentially, both approaches suffer from catastrophic forgetting. Fine-tuning on a task degrades prior tasks, and steering only shifts forgetting to the shared steering mo...

---

### 17. Spanning Diffusion and Flow-based Posterior Sampling via Exact Gaussian Conditioning

**Authors:** Teo Deveney, Lea Bogensperger, Hok Shing Wong

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13812v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13812v1)

**Summary:** Flow-matching and diffusion models are increasingly used as priors for linear inverse problems, however, most methods are bespoke to one class of trajectory prior. Plug-and-play methods have been proposed, however these implicitly decorrelate the guided trajectory, resulting in broad priors that can struggle when data is sparse. This work proposes $β$-Flow: a general plug-and-play method indexed by a correlation parameter $β$ that generalises over flow, diffusion, and decorrelated priors, and a ...

---

### 18. OccludeBench: Can VLMs Find What's Missing?

**Authors:** Jasin Cekinmez, Addison J. Wu, Ryo Mitsuhashi, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13790v1)

**Summary:** How well can vision-language models (VLMs) reason about what is missing from an image? We study this question with OccludeBench, a manually curated benchmark for recovering fully occluded objects from the visual evidence that remains. OccludeBench distinguishes direct cases, where the hidden object must be recovered from a specific physical cue such as a shadow or reflection, from inferential cases, where it can be inferred from broader scene context. Across five VLMs, accuracy averages 42.7% on...

---

### 19. UkrMeme: Multimodal Explainable Persuasion Detection in Ukrainian Memes

**Authors:** Nazar Andrushko, Vera Schmitt, Veronika Solopova

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13783v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13783v1)

**Summary:** Memes play a central role in modern online communication, especially in contexts of political conflict where visual and textual cues combine to convey persuasive messages. We study persuasive technique detection in Ukrainian memes using vision-language models (VLMs). We introduce UkrMeme, a dataset of 200 organically produced Ukrainian wartime memes annotated for persuasion techniques, and PTM-UA, a Ukrainian translation of a subset of the Propaganda 950 benchmark that preserves original visual ...

---

### 20. SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models

**Authors:** Changhui Jing, Haochen Tian, Hongchen Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13781v1)

**Summary:** Driving world action models (WAMs) learn from paired trajectories and future observations. Post-training with reinforcement learning allows the policy to explore alternative trajectories and improve planning using driving rewards. However, driving logs contain future videos only for the recorded trajectories, leaving these alternatives without corresponding visual supervision. Thus, we introduce SimVTA, a simulation-grounded post-training framework that combines trajectory optimization with vide...

---

### 21. Detection of extremely rare dead cells in fluorescence microscopy images

**Authors:** Prateek Verma, Benjamin Butter, Jian Zhang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13780v1)

**Summary:** Dead cell detection in fluorescence microscopy is essential for phenotypic screening and drug efficacy assessment. However, automated identification remains challenging due to signal variability, optical artifacts, and colocalization ambiguities across multiple channels. Markers that define nuclear boundaries do not neatly coincide spatially or temporally with apoptotic markers. Furthermore, marker accumulation kinetics vary across individual cells and apoptosis stages, making universal threshol...

---

### 22. READ: Reading the Selective Scan for Faithful Video Attribution

**Authors:** Magdalena Trędowicz, Piotr Kubaty, Arkadiusz Lewicki, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13776v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13776v1)

**Summary:** Selective state-space models are an efficient approach to long-sequence video modeling. However, their recurrent computation makes it difficult to determine which video tokens drive a prediction. Existing attribution methods often require additional backward passes or repeated model evaluations, making them substantially more expensive than the forward inference they aim to explain. In this work, we introduce READ, a parameter-free attribution method for selective state-space models that unrolls...

---

### 23. Shortcut Learning in Geospatial Foundation Model Embeddings for Cross-Disaster Damage Assessment

**Authors:** Ali Shibli, Andrea Nascetti, Yifang Ban

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13766v1)

**Summary:** Geospatial foundation models can support disaster damage assessment, but high accuracy on familiar disasters may hide shortcut learning: prediction from event or scene characteristics rather than evidence that transfers to a new disaster. We study embeddings from TerraMind, Prithvi-EO-2.0, DOFA, and DINOv3 on the multi-disaster datasets xView2 and BRIGHT. Holding out an entire disaster, instead of randomly splitting image tiles, reduces mean balanced accuracy from 0.807 to 0.638 on xView2 and fr...

---

### 24. Neurons++: A Unified Visual-Stream Framework for Image and Video Reconstruction from fMRI with Neural-to-Visual Interpretability

**Authors:** Haonan Wang, Yuchen Wang, Jingyu Lu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13763v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13763v1)

**Summary:** Decoding visual experience from fMRI is important for understanding human perception and developing brain-computer interfaces. Recent generative decoding methods can reconstruct plausible images and videos, but visual plausibility alone does not ensure that the output is faithfully grounded in brain activity. In this work, we propose Neurons++, a visual-stream fMRI reconstruction framework for both static image and dynamic video reconstruction. Compared with our conference version Neurons, Neuro...

---

### 25. Gaussian Splatting with Reflections Guided by What is Seen

**Authors:** Yiming Liang, Tianyu Xiao, Hiroshi Ishikawa

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13757v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13757v1)

**Summary:** While novel view synthesis methods like Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have shown impressive performance on common scenes, they often struggle with capturing view-dependent specular effects, particularly near-field reflections. Existing methods utilize environment maps, which only represent lights from infinity, or environment Gaussians, which rely solely on indirect supervision from reflections, are insufficient for accurately modeling such effects. Here, we prop...

---

### 26. KVeil: First-Place Solution to ECCV 2026 LifeGenIP Challenge on Unlearnable Videos

**Authors:** Boheng Li, Yueming Xing, Yiming Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13733v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13733v1)

**Summary:** The rapid development of personalized video generation has raised serious concerns over identity privacy, as a few facial videos of a person now suffice to reproduce their identity in synthetic videos. This report presents the first-place solutions to both phases of the ECCV 2026 LifeGenIP Challenge on Unlearnable Videos, which aims to protect facial videos from unauthorized customization under a limited and imperceptible perturbation budget. For Phase 1, we introduce Reference Capacity Collapse...

---

### 27. LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos

**Authors:** Zhiyuan Xiang, Peidong Liu, Mingyang Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13732v1)

**Summary:** Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data. Large-scale egocentric human videos offer a rich alternative, but they lack robot action labels, and existing action annotation methods are often noisy under real-world visual complexity and diverse manipulation dynamics. We introduce LAPT-Scale, a scalable latent action pre-training paradigm with two components: LAPT-Scale-LAM learns continuous latent actions by explaining frame-to-frame vis...

---

### 28. State-Isolated Vision Mamba via Update-Tendency Routing for Underwater Image Enhancement

**Authors:** Yan Luo, Laibin Chang, Zefan Feng, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13720v1)

**Summary:** Vision Mamba has recently emerged as an efficient alternative to convolutional and Transformer-based architectures by modeling long-range spatial dependencies through recurrent state evolution. Existing studies primarily improve token serialization, scanning strategies, or expert routing, yet largely overlook a state level question question: how should recurrent states be organized for spatially heterogeneous visual restoration? In this paper, we show that forcing tokens with heterogeneous updat...

---

### 29. GLIMPSE: Global-Local Indexing with Multi-Precision Spectral Encoding for Explorable Video World Models

**Authors:** Zhufeng Xu, Henglei Lv, Bailin Deng, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13706v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13706v1)

**Summary:** A camera-controlled video world model must keep a scene consistent when the camera returns to it. Memories that render stored features into the target frame can turn depth and pose errors into ghosting or duplicated structure. Positional transport avoids that resampling by relocating a historical patch's address rather than its content, but assigns full positional precision even to inaccurate projections. We present GLIMPSE, a global-local memory interface with band-wise multi-precision coordina...

---

### 30. Improving Semantic Coverage in AI Test & Evaluation through Generative Augmentation

**Authors:** Connor Hashemi, Bharadwaj Ravichandran, Connor Anderson, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13697v1)

**Summary:** In test and evaluation (T&E) of AI models, evaluators typically have access only to a held-out test dataset and no knowledge of the training data or its semantic composition. If critical input conditions---such as time-of-day, weather, or scene location---are underrepresented in this test dataset, T&E results can be misleadingly due to this semantic coverage gap. We propose a three-stage generative AI pipeline to detect and fill such semantic gaps without requiring ground-truth labels of these s...

---

### 31. X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation

**Authors:** Saumyaranjan Mohanty, Aravind Reddy, Konda Reddy Mopuri

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13687v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13687v1)

**Summary:** Audio-visual dataset distillation aims to synthesize a small dataset from a large paired audio-visual dataset, while nearly preserving the training utility for neural networks. Existing approaches such as DM and AVDD face two critical limitations: 1) they are memory-intensive, making them difficult to scale to complex architectures and higher samples-per-class (SPC) settings, and 2) they often fail to preserve strong cross-modal semantic correspondence. To tackle these issues, we propose X-AVDD,...

---

### 32. PhysForge: Material-Controllable 3D Reconstruction with Separable Components

**Authors:** Yuchen Wang, Yanqi Bao, Zheng Gu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13681v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13681v1)

**Summary:** Recent advances in physical 3D generation have enabled visually faithful assets with simulatable mechanical behavior. However, existing methods provide limited control over material behavior beyond appearance-based inference and struggle to estimate physical properties from complex interactions between objects and semantic parts. Therefore, we present PhysForge, a Video Diffusion Model (VDM)-based framework for addressing these challenges, comprising two complementary modules for material-contro...

---

### 33. Can Multimodal Decision Models Classify Breast Ultrasound Images? Benchmarking CLEF and CLEF-Flash Across Prompts and Datasets

**Authors:** Tran Cao Minh, Hai Tran, Ha Minh Tan

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13675v1)

**Summary:** Multimodal decision models return probabilities over predefined alternatives, offering a structured interface for image classification. This study benchmarks inference with CLEF and CLEF-Flash on 2818 breast ultrasound images from Dataset B, BUSI, and BUS-BRA. Dataset B and BUS-BRA use binary benign-malignant classification, whereas BUSI includes normal, benign, and malignant categories. Model parameters remain unchanged, and original images are submitted without user-defined preprocessing. Thre...

---

### 34. Model-agnostic Knowledge Augmented Machine Learning for Weakly Annotated Bioimaging Data

**Authors:** Jayanie Bogahawatte, Sachith Seneviratne, Simon Maksour, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13637v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13637v1)

**Summary:** Machine learning models are increasingly used for automated feature extraction from weakly annotated bioimaging data, such as microscopy and cytomorphology images. Due to the sole dependency of automated feature extraction, existing methods yield inconsistent classification performance across weakly annotated datasets. Here, we propose a model-agnostic knowledge augmentation method that enables ML models to exploit domain knowledge beyond what automated feature extraction can capture. The propos...

---

### 35. Benchmarking Answer-Grounding Consistency in Remote Sensing Visual Question Answering

**Authors:** Ping Guo, Zhiqi Huang, Xinran Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13636v1)

**Summary:** In grounded remote sensing visual question answering, a model produces a textual answer and identifies relevant objects in the image as grounding evidence. Existing evaluations measure answer correctness and localization quality, but do not directly assess answer-grounding consistency. We propose the Answer-Evidence Support Protocol (AESP) to assess this consistency through evidence support: whether the grounding evidence supports the model's own answer. AESP applies task-specific rules to exist...

---

### 36. Multi-Stream Attention Residuals

**Authors:** Xiaohan Qin, Xiangdong Zhang, Tuo Dai, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13630v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13630v1)

**Summary:** Attention Residuals (AttnRes) enables content-dependent retrieval over network depth, which can be viewed as single-stream softmax attention along the depth axis. Inspired by the success of multi-head attention along the sequence axis, we introduce Multi-Stream Attention Residuals (MSAR), an extension of AttnRes that generalizes this mechanism to multi-head depth attention, yielding substantial performance gains with minimal additional overhead. MSAR draws stream diversity from sequence context ...

---

### 37. CUBE: Class-conditioned Unknown Boundary Evidence for Open-Set Insect Species Recognition

**Authors:** Hao Tan, Qimin Zhang, Zhe Xiao, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13610v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13610v1)

**Summary:** Open-set insect species recognition faces significant challenges when deployed in real-world biodiversity scenarios, particularly when encountering unknown species that are visually close to known training classes. Unlike generic out-of-distribution samples, fine-grained unknown insects are often not visually anomalous. They instead tend to appear near the decision boundary of specific known species, leading to unreliable closed-set predictions. To address these challenges, we propose \textbf{Cl...

---

### 38. Thyroid Nodule Segmentation in Ultrasound Images with Conformal Uncertainty Estimation

**Authors:** Francesco Teodori, Pierpaolo Brutti, Umberto Ferraro Petrillo

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13604v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13604v1)

**Summary:** Thyroid nodules affect a large proportion of the general population. Although most are benign, a non-negligible fraction is malignant. Ultrasound imaging is the primary diagnostic modality, and accurate nodule segmentation is a prerequisite for CAD systems to classify malignancy and assess metastatic risk.\\ In this work, we propose a thyroid nodule segmentation framework that integrates a DeepLabV3+, channel-attention modules and post-hoc conformal prediction, providing both accurate mask and p...

---

### 39. RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation

**Authors:** Xuhui Kang, Sung-Wook Lee, Yan Zhuang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13578v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13578v1)

**Summary:** Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Represent...

---

### 40. What We Talk About When We Talk About Emotion Editing

**Authors:** Xingzu Zhan, Lin Gu, Ruogu Fang

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13558v1)

**Summary:** Emotional image editing aims to change the emotion a scene conveys while preserving its essential content. Because the same scene can support different emotional interpretations, achieving an emotional goal requires visual changes grounded in the source context. Motivated by the Component Process Model, which links emotional responses to event appraisal, we investigate neural representations as a reference for these editing decisions. Using TRIBE v2, an fMRI encoding model, we analyze 400 source...

---

### 41. Learning Holistic Scene Layout against View Shifts in Cross-View Geo-Localization

**Authors:** Chao Yang, Songlian Li, Zhigang Tu

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13553v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13553v1)

**Summary:** Cross-view geo-localization remains challenging due to drastic appearance variations and geometric distortions caused by viewpoint changes. Existing methods primarily rely on discriminative feature learning or explicit geometric alignment, yet often overlook an important observation: humans tend to match scenes by integrating the spatial context of multiple landmarks rather than relying solely on isolated local visual cues. Inspired by this, we propose a Spatial Context Modeling (SCM) module, wh...

---

### 42. ELMA: Benchmarking Anaphoric Compositions for Long-Term Text-to-Motion Generation

**Authors:** Shun Kato, Dixin Yang, Kotaro Amaya, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13549v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13549v1)

**Summary:** Text-guided long-term human motion generation is essential for applications such as continuously operating digital avatars. Despite recent progress on short clips, existing models struggle with multi-segment instructions that involve anaphora, where constraints established in earlier segments must be preserved over time. In this paper, we introduce a novel task of long-term motion generation from such anaphoric compositions. To mitigate this, we present ELMA, an episodic long-term motion dataset...

---

### 43. Auditing VLM Benchmarks from Existing Evaluation Runs

**Authors:** Denis Degtiarev, Anna Gromova, Sergey Katkov, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13548v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13548v1)

**Summary:** Every evaluation run of a vision-language model (VLM) already produces per-question artifacts (predictions, judged correctness, metadata) that leaderboards reduce to a single score and then discard. We reuse those artifacts to audit the benchmark itself, and add an audit layer to VLMEvalKit: six detectors that run as post-processing over saved outputs, plus one additional text-only rerun with visual inputs removed, emitting a per-question report. The layer reports per-question findings together ...

---

### 44. MOSAIC: Multi-Scale Object-Centric Slot Adaptation with Image-Guided Prototype Conditioning for Remote Sensing Image Super-Resolution

**Authors:** Liuqian Wang, Hanyu Xie, Rongzhen Zhao, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13547v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13547v1)

**Summary:** Pretrained diffusion Transformers provide powerful generative priors for image restoration, yet adapting them to structure-sensitive tasks remains challenging. Existing methods mainly rely on dense low-resolution features as conditions, which often entangle salient objects with dominant backgrounds and provide limited abstraction for recurring structures across scales and samples. We propose MOSAIC, an object-centric representation learning framework that learns compact structural conditions for...

---

### 45. Efficient Confidence-Aware Densification for 3DGS

**Authors:** Manuel Hofer, Thomas Köhler, Felix Windisch, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13541v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13541v1)

**Summary:** 3DGS-MCMC has replaced the gradient-driven density control of 3D Gaussian Splatting with opacity-based sampling and relocation, and is now the de facto standard for prior-free densification under a fixed primitive budget. Because opacity stays high where the scene is already well reconstructed, this sampling sends most new primitives to the foreground and leaves the background under-reconstructed. At low budgets, prior-based methods such as ConeGS and EDGS outperform it, at the cost of a pre-tra...

---

### 46. Knowing Whether, Not Just Where: Anchor-Probing Distillation for Open-Set Remote Sensing Visual Grounding

**Authors:** Zhihao Chang, Lei Zhai, Shuyuan Yang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13535v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13535v1)

**Summary:** Open-set visual grounding in remote sensing requires models to determine not only where a queried object is located, but also whether the image provides sufficient evidence for the query at all. Existing closed-set grounding models, however, tend to return plausible boxes even for absent objects, blurring localization confidence with genuine Visual Support. We introduce AnchorProbe-Distill (APD), a teacher-student framework that recasts open-set grounding as Visual Support learning. APD builds o...

---

### 47. S-Space: Exploring Spatial Workspace in Multimodal Language Models

**Authors:** Zhiyuan Shi, Xiang Li, Xingzhuo Guo, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13527v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13527v1)

**Summary:** Multimodal language models (MLLMs) exhibit promising spatial reasoning capabilities, yet the internal mechanisms supporting them remain poorly understood. We uncover S-Space, a linear representation subspace in which object-token representations encode continuous coordinates along horizontal, vertical, and distance axes. Although we identify these axes by differentiating spatial-answer scores with respect to object-token activations, S-Space is intrinsic rather than induced by specific data or p...

---

### 48. Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics

**Authors:** Peiyan Tu, Cong Wang, Hanxin Zhu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13522v1)

**Summary:** Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions. However, existing robotic datasets provide limited coverage of the diverse interaction dynamics required for generalizable world modeling. Large-scale egocentric human videos offer complementary interaction experience, yet the embodiment gap between human hands and robotic manipulators hinders effective cross-embodiment learning. Meanwhile, the predominance ...

---

### 49. SplatQ: Interaction-Aware Pruning of 3D Gaussian Splatting via Quadratic Selection

**Authors:** Hongbin Ye, Haixu Liu, Shenwei Kang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13503v1)

**Summary:** Existing 3D Gaussian Splatting (3DGS) pruning methods primarily rely on global Top-K selection based on independent importance scores, lacking regional budget control and ignoring joint deletion effects. Consequently, they cannot ensure balanced reconstruction quality across a scene. We propose SplatQ, a combinatorial pruning algorithm that coordinates regional budget allocation and joint Gaussian selection under a fixed budget. SplatQ partitions Gaussians by spatial proximity and appearance sim...

---

### 50. Stride: Scale-Aware Multi-Agent Evolutionary Refinement for Infographic Generation

**Authors:** Yan Zhou, Yang Yang

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13502v1)

**Summary:** Infographic generation challenges text-to-image models because a single image must satisfy numerous visual, textual, and semantic constraints. Iterative agentic refinement with a multimodal verifier is a natural remedy, but existing methods face a scale mismatch: local edits cannot correct global composition errors, while full regeneration may destroy already-correct regions. We introduce Stride, a constraint-grounded multi-agent framework that treats refinement over any frozen generator as a hi...

---

## cs.LG

**50 papers**

### 1. Hide and Seek: HIDE Concepts to SEEK explanations for black box models

**Authors:** Bhanu Tokas, Rahul Nair, Rockwell Jackson, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13935v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13935v1)

**Summary:** Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that...

---

### 2. Constructive Bounds for the Topological Expressivity of Neural Networks

**Authors:** Kosio Beshkov

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13931v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13931v1)

**Summary:** The expressivity of a neural network $Φ$ describes the class of functions that a network can express. The term topological expressivity refers to a family of measures particularly suited to understand binary classification and is often formulated in terms of the Betti numbers of a decision boundary $β(Φ^{-1}(0))$. Despite its popularity, this measure is not as useful for regression and other problems that do not involve a decision boundary. Instead, we propose to study topological expressivity i...

---

### 3. AI Models Can Provably Hide Arbitrary Capabilities

**Authors:** Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13928v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13928v1)

**Summary:** Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under...

---

### 4. KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling

**Authors:** Tianyi Wu

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13924v1)

**Summary:** A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$ with the output-law divergence $D_{\mathrm{KL}}(p\|\mathbb{E}_U q_U)$, in nats. Rounds commit independent draws from exact conditional marginals frozen at the round's start, each output's schedule is drawn before sampling from a finite mixture of ...

---

### 5. Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning

**Authors:** Sajjad Baghaeea, Aimin Lib, Shanmugarajan Balasubramanian, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13923v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13923v1)

**Summary:** Deep-space communications operate under intermittent connectivity, long propagation delays, and relay storage constraints. In such networks, the Bundle Protocol enables store-carry-forward communication, requiring relay nodes to manage limited storage and scarce contact opportunities. Relay-side scheduling and dropping decisions are inherently goal-oriented: transmission resources should be allocated to bundles most valuable to downstream mission objectives. Conventional schedulers, such as FIFO...

---

### 6. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 7. Designing Protein Structures from Natural Language

**Authors:** Joseph Lee, Yanjing Li, Bo Qiang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13917v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13917v1)

**Summary:** A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support. We develop Prompteina, the first all-atom structure generation model that supports new and broader design objectives specified in natural language, analogous to text-to-image generation. To train Prompteina, we construct Prompteina-Data, a pa...

---

### 8. Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early Stopping

**Authors:** Danil Rudenko, Georgii Bulgakov, Nikolay Kartashev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13909v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13909v1)

**Summary:** While deep learning models for tabular data have recently received significant research attention, the choice of objective functions for regression tasks remains an understudied degree of freedom. Several lines of research offer alternatives to the standard Mean Squared Error (MSE), but differences in datasets, backbones, and evaluation protocols make their practical benefits difficult to compare. In this work, we address this gap by performing a systematic re-evaluation of regression objectives...

---

### 9. Hitting-Time Bounds for Asynchronous Q-Learning

**Authors:** Yang Peng

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13901v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13901v1)

**Summary:** We study the last iterate of standard asynchronous Q-learning from a single trajectory of a finite Markov decision process. The trajectory follows a fixed behavior policy whose state--action chain is irreducible and may be periodic. For discount factor $γ$, write $H=(1-γ)^{-1}$, and let $μ_{\min}$ be the minimum stationary state--action probability and $\mathfrak h_\star$ the largest expected hitting time of the reverse state--action chain. We prove that zero-initialized Q-learning with a consta...

---

### 10. Prediction Is Not a Sufficient Memory State

**Authors:** Robert Jenkinson Alvarez

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13881v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13881v1)

**Summary:** A memory that reproduces every current prediction may still have forgotten how to learn from the next observation. We characterize this distinction for exact cumulative learning and attention. For smooth convex residual losses with unrestricted real features and labels, a continuous recurrent state of fixed dimension exists exactly when the loss is polynomial. With ordinary, unweighted observations, degree $D$ requires precisely $r=\binom{d+D}{D}-1$ coordinates; even among histories with one fix...

---

### 11. Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking

**Authors:** El Mahdi Chayti, Alireza Mirrokni, Martin Jaggi

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13871v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13871v1)

**Summary:** Many optimization problems provide direct access to only part of the gradient, while the remaining component must be inferred from function evaluations. This structure arises in performative prediction, performative reinforcement learning, and bilevel optimization with a black-box lower level. We introduce Partially Informed Stochastic Optimization (PISO), which combines the available gradient component with a running estimate of the residual. By centring each zeroth-order observation on this es...

---

### 12. Finite-Sample Guarantees for Fully Discrete Conditional Diffusion Models

**Authors:** Qiuyun Zhu

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13851v1)

**Summary:** We establish finite-sample guarantees for conditional diffusion models learned from data and implemented with finitely many denoising steps. Our approach aligns the score-training objective with the sampling grid, allowing statistical estimation and numerical discretization errors to be analyzed together. Under a smooth conditional density model, we derive high-probability bounds on the generated distribution's error and quantify the required number of score evaluations. For every smoothness ind...

---

### 13. Inference-Time Steering Across Scaffolds and Epitopes for Sample-Efficient De Novo Nanobody Design

**Authors:** Mason Minot, Simon Friedensohn, Cédric R. Weber

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13844v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13844v1)

**Summary:** Generative molecular design typically relies on over-generation and post-hoc filtering. Inference-time steering methods like Feynman-Kac (FK) steering improve efficiency by biasing trajectories toward high-reward candidates, yet they optimize within a single fixed configuration. In de novo nanobody design, upfront commitment to conditioning choices like scaffold identity or target epitope creates a bottleneck. Since yield varies across these conditions, steering unpromising setups wastes compute...

---

### 14. Returning to Development States: When Full Sandbox Snapshots Help Coding Agents

**Authors:** Daniel Thi Graviet, Tanmay Shah

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13841v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13841v1)

**Summary:** Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could outperform repeatedly restarting from the initial state. We implement Go-Explore-style search over full Daytona snapshots and find that higher and more efficient solve rates depend mainly on progress that...

---

### 15. Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency

**Authors:** Sheng Zhao, Yuhao Zhu

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13835v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13835v1)

**Summary:** An ideal (language) model must continually update its knowledge. Existing work largely focuses on making these updates efficient after training. We investigate how the organization of time-varying knowledge during pre-training shapes the efficiency of subsequent updates. Models trained on chronologically ordered knowledge specialize in the most recently encountered knowledge; we call them specialists. In contrast, models trained on the same knowledge in randomly shuffled order perform well acros...

---

### 16. On the Design Space of Continuous Diffusion Language Models

**Authors:** Oscar Davis, Daan Roos, Alice Bizeul, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13834v1)

**Summary:** Continuous diffusion language models (CDLMs) promise to bring the benefits of continuous flow modelling to language, including accelerated sampling and controllable generation. The field has grown rapidly, and the capabilities of CDLMs have begun to rival those of discrete diffusion. Yet, unlike for continuous modalities such as images or videos, our grasp of the levers that matter when training CDLMs remains limited. In this work, we focus on two of these levers, namely self-conditioning and em...

---

### 17. Shared Canonical Component Removal Beyond Expert Views

**Authors:** Jose Roberto Tello Ayala, Akl C. Fahed, Roy Perlis, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13819v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13819v1)

**Summary:** In clinical practice, experts often begin by converting raw inputs into a set of expert features before making a decision. While black-box models trained on raw input can outperform models trained on expert views, it remains unclear what predictive signal the raw model exploits beyond what the expert view captures. We introduce an audit framework to quantify this gap using Shared Canonical Component Removal (SCCR). Unlike standard residualization or concept erasure, SCCR selectively removes only...

---

### 18. TabMF: Learning Dataset Representations with Tabular Foundation Models

**Authors:** Rafiq Kamel, Nicolas Atienza, Aziz Fouché, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13818v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13818v1)

**Summary:** Representations of supervised datasets support higher-level machine-learning tasks such as dataset retrieval and distribution-shift monitoring. However, existing approaches typically rely either on hand-crafted meta-features or on dataset encoders trained specifically for representation learning. We introduce TabMF, a framework that repurposes pretrained tabular foundation models (TFMs) as encoders of supervised datasets. TabMF equips a predictive TFM with an architecture-aware dataset-level rea...

---

### 19. Dream to Remember: Continual Steering of Generalist Robot Policies with World Models

**Authors:** Bahey Tharwat, Iman Nematollahi, Marvin Alles, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13816v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13816v1)

**Summary:** Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations. Reinforcement learning can improve and extend them, either by fine-tuning the policy weights or by training a small module to steer the input noise of a frozen generative policy. When tasks arrive sequentially, both approaches suffer from catastrophic forgetting. Fine-tuning on a task degrades prior tasks, and steering only shifts forgetting to the shared steering mo...

---

### 20. Spanning Diffusion and Flow-based Posterior Sampling via Exact Gaussian Conditioning

**Authors:** Teo Deveney, Lea Bogensperger, Hok Shing Wong

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13812v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13812v1)

**Summary:** Flow-matching and diffusion models are increasingly used as priors for linear inverse problems, however, most methods are bespoke to one class of trajectory prior. Plug-and-play methods have been proposed, however these implicitly decorrelate the guided trajectory, resulting in broad priors that can struggle when data is sparse. This work proposes $β$-Flow: a general plug-and-play method indexed by a correlation parameter $β$ that generalises over flow, diffusion, and decorrelated priors, and a ...

---

### 21. QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code

**Authors:** Meriem Terki, Nouhaila Innan, Minghao Shao, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13811v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13811v1)

**Summary:** Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a correct solution, but...

---

### 22. Diversity-Aware Ensemble of Quantum-Classical Models via Combinatorial Fusion

**Authors:** Jingyan Xu, Yuanhong Wu, Samuel Yen-Chi Chen, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13808v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13808v1)

**Summary:** Variational quantum circuits (VQCs) are highly sensitive to circuit architecture, yet most quantum machine learning pipelines select a single best design and discard the remaining candidates. This paper addresses whether the structural diversity across quantum circuit search spaces can be used to produce stronger predictions through model fusion. We apply Combinatorial Fusion Analysis (CFA), a model fusion framework that selects and combines multiple scoring systems using rank-score function (RS...

---

### 23. FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial Recommender Systems

**Authors:** Vishnu Arun, Adam Obeng, Tianyou Wang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13806v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13806v1)

**Summary:** Production recommender systems have feature-lifecycle asymmetry: adding new features must produce gains on some metric, while feature removal must not regress any metric. In practice, feature deprecation is hard to prioritize as a feature can fail to be removed if it interacts with other features, its importance changes daily, it cannot be evaluated before production models change or data drift occurs, it is in contention for A/B test space with other launches, it causes regressions in an online...

---

### 24. Constrained Probabilistic Numerics: Gaussian Process Solvers for Linear PDEs under Linear Inequality Constraints

**Authors:** Boyuan Deng, Kshitiz Upadhyay, Michael Shields

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13804v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13804v1)

**Summary:** Gaussian process solvers for linear partial differential equations (PDEs) return posteriors rather than point estimates, but they condition only on equality information: the PDE residual, boundary data, and measurements. Many solutions of interest also obey inequality constraints, including nonnegativity, monotonicity, and absence of arbitrage, which equality conditioning cannot enforce. We prove that conditioning a Gaussian process prior jointly on linear equality observations and a finite-dime...

---

### 25. Adaptive Variance Reduction without Knowing Oracle Smoothness

**Authors:** Wei Jiang, Yibo Wang, Zechao Li

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13799v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13799v1)

**Summary:** Variance reduction improves the convergence rate of stochastic non-convex optimization under the average smoothness condition. Existing adaptive variance reduction methods are especially designed for average smoothness and do not adapt to standard smoothness. In this paper, we study how one algorithm can adapt to these two settings and the noiseless setting without knowing the smoothness constants or the variance bound. Given the gradient budget $T$, we develop a two-phase method. The first phas...

---

### 26. Randomized Momentum Transport with Cheap Predictors

**Authors:** El Mahdi Chayti, Martin Jaggi

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13789v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13789v1)

**Summary:** Momentum methods such as STORM and second-order momentum track the gradient by adding a transport correction to momentum, at the cost of an extra oracle call per iteration. We introduce randomized momentum transport, which evaluates the correction with probability $q$ and otherwise uses a cheap prediction, with importance weighting that preserves the conditional mean and adds $(q^{-1}-1)$ times the prediction loss to the variance. Under transport-bias, second-moment, and residual-control assumpt...

---

### 27. Optimal Algorithms for Nonsmooth Nonconvex Stochastic Optimization with Constraints

**Authors:** Gon Buzaglo, Guy Kornowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13787v1)

**Summary:** We present new algorithms for stochastic optimization problems in which the objective is neither smooth nor convex, subject to a convex constraint set. Our algorithms return a $(δ,\varepsilon)$-Goldstein stationary point, as recently defined for constrained problems by Liu et al. (2024), with improved complexities, and are the first to achieve optimal convergence rates for this task in several settings. In particular, we design projection-based and projection-free algorithms that achieve a $\wid...

---

### 28. Your Discrete Graph Diffusion Model is Secretly Memorizing

**Authors:** Adarsh Jamadandi, Nicolas Keriven

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13786v1)

**Summary:** Discrete graph diffusion models (GDMs) corrupt the graph structure by adding noise independently to nodes and edges under a Markovian noise model. In the unconditional setting without node features, an equivariant denoiser trained on a single graph is able to generate novel graphs and sample-level metrics such as edge overlap and WL kernel similarity find no evidence of memorization. In this work, we challenge this view and show for the first time that graph diffusion models indeed exhibit memor...

---

### 29. ReplaySSM: Cache SSM Inputs, Not State

**Authors:** Ze-Wei Liou, Harris Nover, Amey Naik, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13778v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13778v1)

**Summary:** State-space models (SSMs) maintain a fixed-size recurrent state, but reading and writing it at every decoding step can bottleneck hybrid models. This eager state management causes large state I/O with low arithmetic intensity, leaves speculative decoding no cheap rollback, and feeds state quantization error into subsequent recurrent updates. We introduce ReplaySSM, which unrolls the recurrence to represent the state as a checkpoint and a buffer of recent SSM inputs. This separates output computa...

---

### 30. Geometry-Aware Multi-Objective Optimization: Norm-Constrained Oracles with Entropic Weight Updates

**Authors:** El Mahdi Chayti, Alireza Mirrokni, Martin Jaggi

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13773v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13773v1)

**Summary:** Multiple-gradient descent is typically formulated in Euclidean geometry, whereas matrix-aware optimizers use directions induced by other norms. We analyze a single-loop multi-objective method combining a norm-constrained linear minimization oracle with entropic updates of task weights. For any finite-dimensional norm pair, we establish an $O(T^{-1/2})$ ergodic stationarity rate in the deterministic setting, deriving the required trajectory gradient bound from smoothness and lower-boundedness in ...

---

### 31. From Pixels to Privacy-Sensitive Features: An Information-Theoretic Framework for Reconstruction Bounds

**Authors:** Henry Bourne, Robert F. Allison

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13768v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13768v1)

**Summary:** What can an adversary recover from a model trained with DP-SGD? Its $(\varepsilon,δ)$ guarantee does not answer this question directly. We derive a distortion bound that can be computed before training and applies even to an adversary who observes the parameter trajectory during training, knows every other training record and the population distribution from which the training records are drawn. The analyst may choose the representation in which error is measured, allowing the bound to target th...

---

### 32. DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs

**Authors:** Mahsa Salmani, Sayeh Sharify, Hesham Mostafa

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13767v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13767v1)

**Summary:** Low-bit inference on accelerators with native 4-bit support requires quantizing both weights and activations to realize the full throughput gains these formats provide. While post-training weight quantization has been extensively studied, activation quantization remains considerably more challenging and typically requires calibration data. In this work, we introduce DUALQUANT, a dual-scale, calibration-free post-training quantization framework that directly minimizes the weight-reconstruction Me...

---

### 33. Shortcut Learning in Geospatial Foundation Model Embeddings for Cross-Disaster Damage Assessment

**Authors:** Ali Shibli, Andrea Nascetti, Yifang Ban

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13766v1)

**Summary:** Geospatial foundation models can support disaster damage assessment, but high accuracy on familiar disasters may hide shortcut learning: prediction from event or scene characteristics rather than evidence that transfers to a new disaster. We study embeddings from TerraMind, Prithvi-EO-2.0, DOFA, and DINOv3 on the multi-disaster datasets xView2 and BRIGHT. Holding out an entire disaster, instead of randomly splitting image tiles, reduces mean balanced accuracy from 0.807 to 0.638 on xView2 and fr...

---

### 34. When Edge Independence Fails: Joint Graph Diffusion with Latent Sociability Priors

**Authors:** Adarsh Jamadandi, Nicolas Keriven, Aline Roumy

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13765v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13765v1)

**Summary:** Discrete graph diffusion models corrupt graph structure through independent edge updates with a Markovian noise model. Combined with the exchangeability requirement on the output distribution, the terminal prior is necessarily an Erdős--Rényi (E-R) random graph. This has a fundamental consequence for unconditional graph generation without node features: in the large graph limit, any GNN denoiser applied to an E-R graph approximately outputs an E-R graph, making effective denoising difficult. In ...

---

### 35. How Well Do Prior-Data Fitted Networks Amortize Bayesian Inference?

**Authors:** Manuel Hülskamp, Julius Kobialka, Emanuel Sommer, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13764v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13764v1)

**Summary:** Prior-data fitted networks (PFNs) are trained to approximate the Bayesian posterior predictive distribution (PPD) of a synthetic prior, yet results about the approximation quality are surprisingly thin. Taking an empirical risk minimization perspective, we decompose the deployment error of PFNs into prior, context, and amortization error, and measure the latter against a reference PPD under a realistic prior. Results show that PFNs generally recover the targeted PPD very well. Nevertheless, we f...

---

### 36. Matched-Context Group Policy Optimization for LLM Agent Training

**Authors:** Chenxu Zhang, Yaorui Shi, Wenlong Zhang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13755v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13755v1)

**Summary:** Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-Context Group Policy Optimization (MCGPO), a procedure for constructing weighted action preferences from already collected trajectories. MCGPO defines comparison contexts with pre-action st...

---

### 37. Studying the Effects of Task Diversity Using Small Mathematical Worlds

**Authors:** Emily Xia Meng, Xuanyu Yang, Junaid Hasan, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13750v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13750v1)

**Summary:** Basic mathematical tasks like modular addition have been a valuable tool for illuminating aspects of neural network behavior that are challenging to see in noisy, unverifiable, large-scale, real-world settings. These studies have typically focused on a single task. However, modern language models are exposed to a vast number of tasks despite being trained with a next-token prediction objective. In this work, we introduce two mathematical task ecosystems, IntWorld and PermWorld, built from distin...

---

### 38. A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning

**Authors:** Mayug Maniparambil, Ayush Rai, Ekansh Verma, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13744v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13744v1)

**Summary:** On-policy self-distillation promises to replace the sparse outcome signal of verifiable-reward RL with dense token-level credit: a teacher conditioned on the reference solution scores the student's own rollout, and the resulting distributional shift is distilled back into the policy. We investigate whether this scoring signal actually contains corrective credit. Using gold error spans in student rollouts, we test the two signals consumed by self-distillation objectives, the full-distribution KL ...

---

### 39. SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices

**Authors:** Timi Owolabi, Hikmah Olawore, Frances Adelakun, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13740v1)

**Summary:** World-action models (WAMs) predict a robot's actions together with the observations those actions will produce. However, the strongest models rely on video diffusion transformers that are far too computationally expensive for resource-constrained edge devices. We present SmolWAM, a latent WAM that we derive from the 2B-parameter Cosmos Policy by keeping its pretrained trunk and rebuilding its inference interface: single-frame visual latents, cached text features that preserve the trunk's attenti...

---

### 40. SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning

**Authors:** Hongrui Zheng, Aditya Singh, Rahul Mangharam

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13737v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13737v1)

**Summary:** Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL, a constrained multi-agent reinforcement learning framework that allows for credit assignment even with joint constraint measurements. We use Signal Temporal Logic (STL) robustness to measure episode-level violation thr...

---

### 41. Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers

**Authors:** Yuhong Chou, Zehao Liu, Yuqi Pan, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13735v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13735v1)

**Summary:** Efficient attention mechanisms, such as linear and sliding window attention, aim to reduce the computational complexity of Transformers from quadratic to linear. However, their degraded in-context recall often necessitates interleaving full attention layers, leaving the quadratic bottleneck unresolved in long-context processing. To address this, we introduce Orthros attention, which shifts the efficiency paradigm from structural allocation to phase-aware decoupling. As a unified module, it dynam...

---

### 42. SeoulMMOD: A Large-Scale Multimodal Origin-Destination Flow Benchmark

**Authors:** Taeyoung Yu, Seonbin Jo, Jiwon Kim, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13730v1)

**Summary:** Origin-destination (OD) flow forecasting supports urban mobility decisions by predicting the volume and patterns of human movement across a city. Most existing public OD benchmarks provide only a partial view of citywide mobility, covering a single transport service or at most two modes. With partial mode coverage, observed demand changes are difficult to separate into shifts across transport modes and changes in total travel. We introduce SeoulMMOD, a large-scale public benchmark for citywide m...

---

### 43. Amortized Counterfactual Prediction with Graph Neural Networks

**Authors:** Hendrik Stumpf, Francesco Quinzan

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13724v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13724v1)

**Summary:** Counterfactual inference asks how an observed outcome might have differed under different circumstances, such as whether a patient would have recovered had they received a different treatment. Such questions arise whenever decisions depend on the outcomes of alternatives that were not observed. Answering counterfactual queries generally requires knowledge of the underlying causal structure, which is often unavailable in practice. A common approach is therefore to first estimate the causal graph ...

---

### 44. Machine Unlearning for Federated Socially Fair k-Means Clustering

**Authors:** Aravind Reddy, Deeraj S K, Mohd Wasif Raza, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13717v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13717v1)

**Summary:** Federated clustering can support applications such as patient stratification across hospitals and customer segmentation across distributed financial datasets. Responsible AI calls for fair representation of demographic groups and support for data deletion, motivated in part by rights such as the GDPR's right to erasure. These goals interact: deleting records can change the balance between groups and alter the clustering of the remaining population. We study exact machine unlearning for federated...

---

### 45. Towards Understanding the Training of GFlowNets: A Theoretical Perspective

**Authors:** Rui Hu, Yu Chen, Zhuoran Li, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13711v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13711v1)

**Summary:** Generative Flow Networks (GFlowNets) learn policies that sample discrete objects in proportion to a positive reward. They are trained by minimizing balance objectives, whose exact satisfaction guarantees correct sampling. However, a comprehensive theory linking nonzero balance loss and approximate stationarity to sampling accuracy, especially under evolving sampling distributions and backward policies, is still lacking. To bridge this gap, we develop a unified theory for Flow Matching, Detailed ...

---

### 46. Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy

**Authors:** Naji Alazhar, Wassel Alazhar

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13708v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13708v1)

**Summary:** Long-context serving runs out of KV memory before the hardware reaches its useful throughput. HiSparse stores history in host memory and fetches only the selected entries, but it uses one cache budget at every load and does not handle draft-model speculative decoding such as DSpark and DFlash2. We present Adaptive DHiSparse, which supports speculative decoding over hierarchical sparse KV and adapts residency to load. It protects the required working set, retains additional history while GPU memo...

---

### 47. Calibration in One Go: Jointly Learning Accurate and Calibrated Neural Networks

**Authors:** Nektarios Kalampalikis, Pablo M. Olmos, Isabel Valera

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13693v1)

**Summary:** Neural networks (NNs), while highly flexible and versatile, are often poorly calibrated. Post-hoc calibration methods adjust the outputs of an already trained model using a separate calibration dataset and additional calibration parameters. This process adds overhead that requires separate optimization of the calibrator and subsequent model selection. In this paper, we show that standard (post-hoc) calibrators can be trained end-to-end with the backbone via a bilevel Stackelberg formulation. Thi...

---

### 48. Variance-Reduced Policy Gradient is Nearly Minimax-Optimal

**Authors:** Leonardo Cesani, Matteo Papini, Marcello Restelli

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13692v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13692v1)

**Summary:** Standard Policy Gradient (PG) algorithms suffer from high estimation variance because they rely on Monte Carlo updates. While off-policy variance reduction mitigates this problem, establishing optimal sample complexity currently requires either restrictive assumptions, such as uniformly bounded importance weights, or impractical second-order operations. In this work, we introduce Loopless Variance-Reduced PG (LVR-PG), a unified theoretical framework that abstracts a class of first-order estimato...

---

### 49. Transformer-based In-Context Score Operator Learning for Diffusion Models

**Authors:** Wuzhe Xu, Zhaiming Shen, Yulong Lu, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13690v1)

**Summary:** Diffusion models typically learn the generative dynamics of a single target distribution or a family of distributions indexed by conditioning variables fixed during training. This limits their ability to adapt to a previously unseen distribution from only a small set of examples. We introduce an in-context solution operator learning framework for diffusion models, in which each target distribution is treated as a task drawn from a meta-distribution and is specified at inference time by an empiri...

---

### 50. VQIL: Visible Quantum Interference Learning for Perturbation Response Ranking on Graphs

**Authors:** Seokjun Lee, Sergio A. Ortega, Daniel K. Park, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13689v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13689v1)

**Summary:** Learning how local perturbations affect a network is important for identifying which components drive or absorb a system's response. We formulate this as seed-conditioned response ranking: given a perturbation at one seed node, ranking all other nodes by response strength. This is challenging when the model is given only the interaction topology, while the mechanism governing how perturbations propagate must be learned from data. We present VQIL (Visible Quantum Interference Learning), a trainab...

---

## cs.NE

**50 papers**

### 1. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 2. A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models

**Authors:** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13663v1)

**Summary:** Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the en...

---

### 3. REMBGO for Evaluation-Limited Optimization: CEC2022 Benchmarking and EAF-STATCOM Generalization

**Authors:** Vikram Chekuri, Narapareddy Ramarao, Prashanth N A

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13471v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13471v1)

**Summary:** Metaheuristic comparisons are often reported at evaluation budgets far larger than an expensive engineering simulation can afford. This paper presents REMBGO, an evaluation-budget-aware refinement of EMBGO. Its contribution is not any single operator: it is the integration of population preservation, scale-normalized exploration and recovery mechanisms whose parent-relative benefit is concentrated under restricted function-evaluation budgets. REMBGO is evaluated on CEC2022 at a primary, applicat...

---

### 4. The value of information and the emergence of communication in evolved e-puck robots

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13118v1)

**Summary:** We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent network with a residual path, either operating alone or as a channel within an Em...

---

### 5. Universal Construction and Exact Self-Reproduction in Ternary McCulloch-Pitts Networks

**Authors:** Charles C. Norton

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12251v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12251v1)

**Summary:** A fixed network of McCulloch-Pitts threshold units with weights in {-1,0,1} can hold other threshold networks in its state and run them: the state is a ring of banks of records, each record a unit of a stored network, and each step evaluates one record. We use such a network to carry out von Neumann's universal construction and self-reproduction exactly. As a cellular automaton keeps its rule, the fixed network keeps its weights, and what reproduces is a stored network. A constructor of 143 reco...

---

### 6. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization

**Authors:** Ming Chen, Rong-Xi Tan, Ke Xue, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12183v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12183v1)

**Summary:** Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system configurations, making their resul...

---

### 7. EliteTable: Self-Improving Program Search for Executable Control Policies

**Authors:** Stuart Farmer

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12536v1)

**Summary:** EliteTable is a self-improving program-search algorithm guided by large language models (LLMs) that uses a fixed-capacity table of high-scoring solutions to guide new proposals, edits of existing solutions, and remixes of several solutions. Performance was evaluated across six Gymnasium control tasks, each with ten generations and fifty candidate slots per generation. Each task was evaluated across ten independently initialized searches. Candidate-score medians rose between the first and final g...

---

### 8. Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating

**Authors:** Lechen Li, Rongye Shi, Wanhuan Zhou

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11546v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11546v1)

**Summary:** Solving high-dimensional structural model updating problems requires an algorithm capable of navigating complex, non-convex landscapes with correlated parameters. Existing hybrid evolutionary algorithms typically rely on static architectures or fixed switching rules, resulting in disjointed search phases. To address this, this study proposes a Deep Reinforcement Learning-governed dynamic DE-CMAES Orchestration (DRL-DCO) algorithm, in which a Deep Deterministic Policy Gradient (DDPG)-based actor-...

---

### 9. Evolutionary Architecture Search for Chlorophyll-$a$ Prediction in Lakes using Sentinel-2

**Authors:** Kursat Komurcu, Linas Petkevicius

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10496v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10496v1)

**Summary:** Small tabular datasets with expert-designed spectral features are the norm in   operational Earth observation, and the networks applied to them are typically   hand-designed. We revisit one such published model -- a Sentinel-2 algal   bloom classifier -- and ask what architecture search adds, holding the task,   the features and the lake-level train/test split of the original study fixed.   Searching an extended multilayer-perceptron space with regularized evolution,   and selecting on inner-cro...

---

### 10. Evolve on the Host, Predict on the Edge: Deploying Online Neuroevolutionary Architecture Search for Cross-sectional Stock Return Prediction

**Authors:** Jonathan Chang, Zimeng Lyu

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10038v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10038v1)

**Summary:** Accurate forecasting models are usually large, expensive to update online, and fixed in architecture once trained. We apply ONE-NAS, an online neuroevolutionary architecture search that evolves a population of small recurrent networks as each window of data arrives, to daily cross-sectional stock return prediction, and pilot it on a host and endpoint pipeline: the host runs the search and ships each generation's champion genomes over TCP/IP to a Raspberry Pi 4B, which predicts online. On the Pi ...

---

### 11. The Modular CMA-ES: A Framework for Modern Evolution Strategies

**Authors:** Jacob de Nobel, Diederick Vermetten, Anna V. Kononova, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09699v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09699v1)

**Summary:** Since their introduction, modern evolution strategies, such as the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), have become established as powerful methods for continuous black-box optimization. This success has led to a wide range of proposed modifications, each designed to improve performance or behavior in specific optimization scenarios. However, because these developments have largely been introduced and studied in isolation, their interactions remain comparatively underexplore...

---

### 12. Relocating Nonlinearity: How a Downstream Learner Reshapes What Genetic Programming Must Evolve

**Authors:** Nam H. Le

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09347v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09347v1)

**Summary:** Genetic programming was conceived as a way of evolving solutions: the program is the answer, and fitness is the error of its own output. A substantial line of work instead makes the program an input to a separate learner, so fitness measures the learner's output rather than the program's. Which learner to attach matters, with no account of what decides it. What makes a target hard for genetic programming is how much nonlinearity the program must build by composing primitives; whatever nonlineari...

---

### 13. Evaluating the Transfer of Co-Evolved Communication from 2D to 3D Simulation

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09280v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09280v1)

**Summary:** This work examines the transfer of a co-evolved communication mechanism between two robotic agents from a discrete two-dimensional (2D) simulator to a three-dimensional simulator with real physics (3D). The study focuses on whether a communication mechanism co-evolved in a 2D environment retains its functional role after transfer to a 3D physics-based simulator. To support this analysis, the effects of the episode time budget, the social cue, and the asymmetry between the two co-evolved roles we...

---

### 14. A Connectome Test of the Fly Hashing Algorithm

**Authors:** Sebastian Senge

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.09114v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09114v1)

**Summary:** Dasgupta, Stevens and Navlakha (2017) showed that the Drosophila olfactory circuit, modelled as a random sparse projection followed by winner-take-all, is a locality-sensitive hash that beats classical LSH. The projection was random because the wiring was unknown. We test it against four electron-microscopy connectomes (MaleCNS, hemibrain, FlyWire, BANC; four animals, seven hemispheres). First, the 2017 pattern holds in a reimplementation of its protocol on SIFT, MNIST and odour mixtures (GloVe ...

---

### 15. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 16. Evolutionary One-Step Generators: Fast and Diverse Sampling for Discrete Design

**Authors:** Marcus Vukojevic, Erik Nielsen, Veronica Lachi, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08367v1)

**Summary:** Several discrete design tasks, such as molecular discovery, require diverse collections of useful candidates at low computational cost. High validity alone does not guarantee a useful candidate library: repeatedly generating the same valid structures leaves few distinct alternatives. Training for both feasibility and diversity is challenging because many relevant criteria can only be evaluated after hard decoding. To address this challenge, we propose EGO (Evolutionary Generators with One-step i...

---

### 17. ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams

**Authors:** Hyewon Kang, Jungmin Lee, Ilgyu Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07962v1)

**Summary:** Where generalization capacity--the ability to extract context-invariant relational structures--first emerges remains a central question in AI and neuroscience. The foundation for this capacity lies upstream of the hippocampus, within the entorhinal cortex, where parallel pathways dissociate relational structure in the medial entorhinal cortex (MEC) from sensory content in the lateral entorhinal cortex. However, as Eichenbaum argued, such factorization likely originates earlier, driven by the seg...

---

### 18. Energy-Efficient Spiking Neural Networks for Sensing-Aided Beam Prediction

**Authors:** Nhan Thanh Nguyen, Phuong Nam Tran, Mengyuan Ma, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.12507v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12507v1)

**Summary:** Sensing-aided beam prediction can reduce the beam-training overhead of millimeter-wave (mmWave) systems by leveraging environmental information from complementary modalities such as vision and position. However, the resulting sensing and inference pipeline can be energy-intensive, motivating the use of energy-efficient spiking neural networks (SNNs) as an alternative to conventional artificial neural networks (ANNs). In this work, we develop SNN architectures for beam prediction and systematical...

---

### 19. Forecast Accuracy Is Not Trading Profit: Evolving Small Recurrent Networks for Stock Return Prediction

**Authors:** Jonathan Chang, Zimeng Lyu

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07825v1)

**Summary:** Time series forecasting models are typically compared on pointwise error, which scores a prediction in isolation from the decision it is produced for, and a lower forecast error does not imply a better decision downstream. A parallel debate asks whether modern transformer architectures forecast better than recurrent and other lightweight models. We compare linear, fixed recurrent, transformer, and mixing based architectures against recurrent networks evolved by neuroevolutionary architecture sea...

---

### 20. Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks

**Authors:** Zijie Xu, Bingrui Guo, Yiding Sun, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07808v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07808v1)

**Summary:** Spiking neural networks (SNNs) offer sparse and event-driven computation, making them attractive for energy-constrained reinforcement learning (RL) on edge devices. In value-based RL, deep spiking Q-networks (DSQNs) combine such efficiency with action-value estimation for decision making. However, existing DSQNs often require multiple simulation timesteps for competitive performance, increasing computational and energy costs, whereas reducing the timesteps can cause substantial performance degra...

---

### 21. Simplified Swarm Optimization for Surrogate-Assisted Reliability Design of Insulated-Gate Bipolar Transistor Power Modules Using an Open-Source Process Finite-Element Model

**Authors:** Wei-Chang Yeh

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07412v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07412v1)

**Summary:** Process-induced warpage, ceramic stress and solder strain limit the reliability of insulated-gate bipolar transistor (IGBT) modules on direct-bonded copper (DBC) substrates. Surrogate-assisted design studies train regression models on finite-element analysis (FEA) databases, but rarely check the optimized designs against new FEA or report how surrogate error interacts with the optimizer. This paper builds and evaluates an open pipeline: an open-source process finite-element model, surrogates tun...

---

### 22. Synapse Loss Estimation for the BrainScaleS Wafer-scale Neuromorphic System

**Authors:** Bernhard Vogginger, Christian Mayr

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.07321v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07321v1)

**Summary:** Neuromorphic hardware combines memory (synapses) and computation (neurons) into the same silicon substrate to avoid the von-Neumann bottleneck. This way, neuromorphic computing aims to make computational neuroscience simulations and AI processing faster and more energy-efficient. The common crossbar architecture integrates a synapse matrix (analog, mixed-signal or digital) with a neuron array into a neurosynaptic core, whereas multiple cores are interconnected via a dedicated spike routing netwo...

---

### 23. Visual Swarm Navigation via Deep Reinforcement Learning and Evolutionary Hybrid Design

**Authors:** Álvaro Díez, Fidel Aznar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06400v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06400v1)

**Summary:** Swarm robotics presents a robust and cost-effective paradigm for advanced automation in complex, dynamic environments, such as those encountered in search and rescue or environmental monitoring. A fundamental challenge for this field is the data-driven design of decentralized controllers capable of generating emergent collective behaviors. This paper proposes a novel, AI-driven hybrid methodology for the automatic synthesis of swarm robotic controllers for autonomous visual navigation. This appr...

---

### 24. A Flexible and Generic Approach for Explainable Landscape Analysis and the pyXla Toolbox

**Authors:** Tony Ombaso, Anna S. Bosman, Arnaud Liefooghe, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06359v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06359v1)

**Summary:** Landscape analysis has been successfully applied to understand complex optimisation problems, gain insights into algorithm behaviour, and automate algorithm selection and configuration. Although many landscape analysis techniques have been developed over the last decades, it remains difficult for researchers and practitioners to decide which approaches are appropriate and to implement them in practice. Some tools are available, but these are either restricted to particular problem domains (e.g.,...

---

### 25. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 26. Optimization Geometry of QAOA and Variational Quantum Algorithms

**Authors:** Vojtěch Novák, Ivan Zelinka, Silvie Illésová, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05524v1)

**Summary:** Variational quantum algorithms turn choices of Hamiltonian, ansatz, and parameterization into a classical nonconvex optimization problem. We study how this objective function can be visualized and characterized in ways that help explain optimizer behavior. We distinguish two properties of the objective: the number of local minima encountered along sampled directions and the differences in quality among local-search endpoints. We then ask how a local optimizer, represented by BFGS, compares with ...

---

### 27. AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding

**Authors:** Mahdi Farahbakhsh, Ilan Sela, Fatemeh Doudi, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05334v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05334v1)

**Summary:** Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the model only the role of proposer. The model knows nothing of the search beyond what it is shown. As models grow more capable, a question arises: does a search strategy chosen by a human before the run scale better than promoting the model from proposer to planner and letting it own the search? The Bitter Lesson suggests t...

---

### 28. MOXIE: Discovering Alternative Explanations for Biomedical Image Classifiers

**Authors:** Abiha Tahsin Chowdhury, Rahul Dubey

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04814v1)

**Summary:** Segment-based explanation methods such as LIME return a single explanation for each prediction, computed from one fixed image segmentation. This hides two important facts: a prediction can be supported by many different sets of image segments, and the segmentation itself shapes which explanations can be found. We introduce MOXIE (Multi-Objective eXplanation Imaging Engine), an evolutionary framework that searches for segment subsets that preserve the classifier's confidence while keeping as litt...

---

### 29. Active-DiNTS: Active Differentiable Network Topology Search

**Authors:** Gean Trindade Pereira, Thierry Urruty, Muriel Visani, et al.

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04787v1)

**Summary:** Neural Architecture Search (NAS) has proved to be a strong alternative to manual network design, but applying it to 3D medical image segmentation is limited by two well-known costs, large annotation budgets and multi-GPU clusters. Thus, this paper introduces Active-DiNTS (Active Differentiable Network Topology Search), an approach that embeds pool-based Active Learning (AL) into a bi-level differentiable topology search to perform architecture discovery and label curation jointly. At each query ...

---

### 30. Robust Optimization of Spring Design under Variable Manufacturing Tolerances

**Authors:** Grzegorz Sroka, Slawomir T. Wierzchon

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04656v1)

**Summary:** A reliable assessment of an optimizer robustness requires tracking controlled changes in parameters to identify sources of algorithmic weakness. Such an approach was applied to the problem of designing tension/compression springs with three continuous variables describing the spring geometry.   Three additional independent binary parameters reflect material variability, manufacturing-related geometric deviations, and an additional safety margin. Without expanding the decision space, these parame...

---

### 31. Chance-Constrained Bi-Objective Evolutionary Optimization for the Open-Pit Mining Operational Planning Problem

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04227v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04227v1)

**Summary:** Open-pit mining operational planning involves allocating limited resources while satisfying production, equipment, and ore-quality requirements. Existing approaches often assume deterministic ore grades or rely on simulation-based evaluation under uncertainty. In this paper, we propose a chance-constrained bi-objective formulation of the open-pit mining operational planning problem under uncertain ore grades. We aim to maximize ore production and minimize fleet cost while satisfying stochastic q...

---

### 32. Adaptive Operator Selection in Bilevel Large Neighborhood Search for Electric Autonomous Dial-a-Ride Problem under Uncertainty

**Authors:** Ishara Hewa Pathiranange, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04219v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04219v1)

**Summary:** The electric autonomous dial-a-ride problem (EADARP) extends the classical dial-a-ride problem by incorporating battery and charging constraints for electric vehicles. In practice, travel-time uncertainty can cause violations of time-window constraints. Large neighborhood search is effective for solving the EADARP, but its performance can depend on the choice of insertion operator during the repair phase. This paper investigates insertion-operator selection within a bilevel large neighborhood se...

---

### 33. AdaEva: Accelerating LLM-Driven Algorithm Design with Adaptive Partial Evaluation

**Authors:** Tai Nguyen, Fei Liu, Phong Le, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03896v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03896v1)

**Summary:** Large Language Models (LLMs) are increasingly used for automated algorithm design. However the computational cost of evaluating the generated algorithms can be excessive. We consider the common LLM-driven automated algorithm design (LLM4AD) setting in which a candidate algorithm is evaluated by aggregating its performance over a shared set of training instances. This instance-wise structure raises a natural question: must every candidate be evaluated on the entire instance set before deciding wh...

---

### 34. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

**Authors:** Hui Chen, Xuan Qi, James Xu Zhao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03675v1)

**Summary:** LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them...

---

### 35. Parallel Time-Aligned Spiking Self-Attention for Consistent Integer-Valued Training and Spike-Driven Inference

**Authors:** Peng Xue, Wei Fang, Kaiwei Che, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03291v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03291v1)

**Summary:** Integer-valued leaky integrate-and-fire (I-LIF) neurons and spike firing approximation (SFA) reduce temporal training cost by representing spike trains as firing counts and normalized firing rates, respectively. However, applying spiking self-attention (SSA) directly to these compressed query, key, and value representations introduces cross-time interactions that are absent during spike-driven inference. We term this operator-level discrepancy Temporal Interaction Mismatch (TIM). We propose Para...

---

### 36. The Investment Acceleration Principle Revisited by means of a Neural Network

**Authors:** Guido Fioretti

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03282v1)

**Summary:** The investment acceleration principle is a heuristic for modelling investment time series out of consumption time series. The model presented herein develops a disaggregated accelerator equation whose coefficients are the weights of a Kohonen neural net that represents firms' decision-making. According to this model, investments take place when managers recognise emerging technological patterns. Furthermore, a technique borrowed from the theory of self-organising systems is used in order to dise...

---

### 37. Self-Repairing Recurrent Ensembles for Real-Time Recovery from Distribution Shift

**Authors:** Julian Lemmel, Pedro D. Wendel Garcia, Taisuke Kobayashi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03249v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03249v1)

**Summary:** Deploying a pretrained controller exposes it to conditions that are absent from its training data. Sensor drift, outright sensor failure and accumulating measurement noise all induce a distribution shift that can collapse an otherwise competent policy; typically at a point in time where no expert is available to supply corrective labels. We present a method that lets a policy recover from such shifts online and without supervision. Our controller is an ensemble of recurrent networks, each of whi...

---

### 38. Evolving Hybrid Quantum-Classical Architectures for Image Classification

**Authors:** Devroop Kar, Daniel Krutz, Travis Desell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03220v2) | 📄 [PDF](https://arxiv.org/pdf/2610.03220v2)

**Summary:** Hybrid quantum classical neural networks integrate parameterized quantum circuits (PQCs) with established deep learning architectures, but their performance depends strongly on the choice of quantum circuit architecture, a choice that remains largely manual. Most existing approaches rely on hand-designed or fixed circuit ansätze, requiring circuit structure, gate composition, and qubit connectivity to be specified in advance with no guarantee that they suit the task. This limitation is especiall...

---

### 39. Distribution Matching Evolutionary Algorithms for Rare Event Sampling

**Authors:** Yonatan Gideoni, Yarin Gal

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03833v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03833v1)

**Summary:** A novel discovery is one which is both useful and surprising: a generative model's output is a useful discovery if it has a low probability of being generated (it's surprising) and a high reward (it's useful). Global optimization can directly increase the probability of sampling high rewards but typically requires updating model weights. Such gradient based optimization is expensive and bars using capable closed-source models. Instead, modern search methods for discovery sacrifice the global tar...

---

### 40. Aggregate accuracy conceals concentrated temporal vulnerability in a spiking speech classifier

**Authors:** İsmail Can Dikmen

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03155v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03155v1)

**Summary:** Aggregate accuracy cannot reveal which utterances are locally vulnerable or how internal activity changes when labels remain stable. We retain every prediction for 725,070 adjacent-bin, one-count changes around 100 validation utterances of a frozen SpikeSCR-based classifier. The canonical native-horizon GPU singleton path reaches 86.0836% validation accuracy. Equal-source expected accuracy under a uniformly chosen neighbor rises from 84.00% to 84.54%, although 13 of 84 initially correct sources ...

---

### 41. Learning While Inferring: Local and Parallel Learning for Edge SNNs across Sensing Modalities

**Authors:** Yanxun Zhang, Yifei Wang, Changze Lv, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03149v1)

**Summary:** Edge intelligence requires models to sense continuously in real time and to keep adapting on-device, all under tight compute, energy, and memory budgets. Although spiking neural networks (SNNs) enable efficient event-driven inference, standard surrogate-gradient backpropagation (BP) serializes updates and blocks ongoing inference. We investigate Bidirectional Spike-Based Distillation (BSD) as an on-device learning principle that lets edge SNNs learn while inferring. BSD couples a stimulus-driven...

---

### 42. Small universal multiset reaction systems

**Authors:** Andrei Paun, Annemarie-Beatrix Messner

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03021v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03021v1)

**Summary:** This paper presents a construction of a small universal machine within the framework of Multi-set Reaction Systems. We encode the machine state using elements that represent registers and instruction labels, and we enforce sequential execution by ensuring that reaction chains for a given instruction can only activate after the corresponding label element appears. We implement a universal register machine with 8 registers and 23 instructions, showing that the priority-based model requires 87 dist...

---

### 43. Temporal Geometry of Deep Networks: Hyperbolic Representations of Training Dynamics for Intrinsic Explainability

**Authors:** Ambarish Moharil

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03000v1)

**Summary:** Intrinsic explainability remains a challenging problem, particularly in contexts where multilayer perceptrons (MLPs) require dynamic re-training within an optimization environment. This paper investigates how MLPs and their training dynamics can be represented and studied in non-Euclidean spaces; our representation features the Poincaré model of hyperbolic geometry. We aim to capture the geometric evolution of their weighted topology and self-organization over time. Instead of restricting the an...

---

### 44. Evolutionary Computation for Trustworthy AI: From Attacks and Defenses to Self-Evolving Era

**Authors:** Junhao Dong, Chenkai Wang, Xuanhui Lin, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02996v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02996v1)

**Summary:** As Artificial Intelligence (AI) has evolved from task-specific models to foundation models and agents, the scope of trustworthy AI has expanded from model-level robustness to the reliability and safety of broader AI systems. This evolution has also expanded the attack surface from individual models to broader system-level interactions, including tool use, context, and interaction trajectories with dynamic environments. As a result, maintaining reliable and safe behavior under changing or deliber...

---

### 45. Evolutionary Giant Tour for CVRP using NSE and ML Heuristic]{Evolutionary Giant Tour approach for CVRP using Node Shift Encoding and Machine Learning repair heuristic

**Authors:** Souad Abdoune, Menouar Boulif

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.03816v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03816v1)

**Summary:** The Capacitated Vehicle Routing Problem (CVRP) remains a central concern in logistics research, as route optimisation under rigid capacity and fleet restrictions directly affects operational performance. Genetic Algorithms are widely used for this problem, yet their effectiveness depends heavily on the choice of solution encoding and on the mechanisms used to preserve feasibility during the search. This paper proposes a sequential framework that separates the evolutionary process from route cons...

---

### 46. SEDIMA: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents

**Authors:** Amirhossein Abaskohi, Mahdi Mostajabdaveh, Zirui Zhou

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02361v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02361v1)

**Summary:** Large language model (LLM)-driven evolutionary search is a powerful paradigm for automated program and algorithm discovery, yet existing systems are largely memoryless: each run explores from scratch, so agents repeatedly rediscover the same improvements and re-encounter the same dead ends. We introduce SEDIMA, a persistent hierarchical insight memory for evolutionary search agents. SEDIMA distills raw traces into natural-language insights, clusters them by semantic similarity using attention-we...

---

### 47. Spiking neural networks for streaming qubit readout

**Authors:** Barry M. Dillon, Aqib Javed, Jim Harkin, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02129v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02129v1)

**Summary:** Fast and accurate qubit-state assignment is essential for feedback, calibration, and error correction in quantum processors. In superconducting platforms, frequency-multiplexed readout makes this task intrinsically multivariate as measured traces can encode crosstalk, qubit-state relaxation events, and other transient nonidealities that are not fully captured by conventional matched filtering. Here, we introduce spiking neural network (SNN) discriminators for superconducting qubit readout. By pr...

---

### 48. TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design

**Authors:** Jose A. Ayala-Romero, Andres Garcia-Saavedra, Xavier Costa-Perez

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01887v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01887v1)

**Summary:** Dynamic resource assignment, the real-time allocation of task streams to heterogeneous processing nodes, is the backbone of modern computing infrastructure. While learning-based schedulers excel in research, industrial deployments still rely on hand-written rules that operators can read, audit, and execute within tight latency budgets. LLM-based Automatic Heuristic Design (AHD) promises to automate writing such rules. However, existing AHD frameworks were developed for combinatorial problems ful...

---

### 49. Continual Reinforcement Learning with Neuroevolution

**Authors:** Eleni Nisioti, Andrea Cossu, Kathrin Korte, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01583v2) | 📄 [PDF](https://arxiv.org/pdf/2610.01583v2)

**Summary:** Despite many studies about causes and remedies of plasticity loss in Reinforcement Learning (RL) under continual task changes, no RL method has yet consistently achieved a good balance between adaptation and forgetting. Here we turn to an alternative optimization paradigm, neuroevolution (NE): algorithms that search directly in weight space through mutation and selection over a population of neural networks. Across a wide array of environments and environmental changes, with policies ranging fro...

---

### 50. Controllable Stochastic Quantization Encoding for Adversarially Robust Spiking Neural Networks

**Authors:** Yujia Liu, Peiyu Liu, Yajing Zheng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01558v1)

**Summary:** Spiking Neural Networks (SNNs) have attracted increasing attention due to their impressive temporal dynamics, energy efficiency, and brain-inspired mechanisms. Although SNNs have demonstrated promising performance in image classification tasks, recent studies have shown that they remain vulnerable to adversarial attacks, where imperceptible perturbations are added to input images to mislead model predictions. Existing defense methods mainly focus on training strategies, while the role of input e...

---

## q-bio.NC

**50 papers**

### 1. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness

**Authors:** Daniel Szelogowski

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13918v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13918v1)

**Summary:** Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothala...

---

### 2. EEG Entrainment to Non-Speech Rhythmic Patterns Associated with Dimensions of Language Performance

**Authors:** Francisco J. Martínez-Murcia, Nicolás J. Gallego-Molina, Marco A. Formoso, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13419v1)

**Summary:** Developmental dyslexia (DLX) affects 5-12% of the global population and impairs learning to read. Its biological basis, particularly the difficulties observed in oral phonological tasks, remains debated. Entrainment, the coupling of brain oscillations to speech rhythms, is essential for encoding phonological representations. We investigated whether brain entrainment to non-speech rhythms could predict DLX in 48 participants listening to white noise amplitude-modulated at rates matching Spanish s...

---

### 3. Beyond Anxiety and Avoidance: A Dynamic Feedback-Regulation Framework for Adult Romantic Attachment

**Authors:** Mateusz Pomianek

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13312v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13312v1)

**Summary:** Adult attachment is commonly represented by attachment anxiety and avoidance, but these person-level dimensions do not by themselves specify how momentary relational conditions are perceived, compared with desired conditions, translated into action, and updated after interpersonal feedback. We present the Attachment Regulation and Control (ARC) framework as an integrative feedback-regulation account that makes these temporal assumptions explicit and empirically testable. In ARC, control refers t...

---

### 4. Excitability across scales: a unifying EI model

**Authors:** Thomas S. J. Burger, Rodolphe Sepulchre

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13275v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13275v1)

**Summary:** Neuronal excitability is commonly modeled using different principles at the cellular and population scales, making it difficult to study how microscopic mechanisms shape macroscopic activity. We introduce a spatiotemporal excitatory-inhibitory (EI) model that unifies these scales through a common mixed-feedback architecture. The model retains the conductance-based circuit structure of Hodgkin-Huxley models and describes intrinsic and synaptic currents through memductances whose temporal and spat...

---

### 5. FlyHack: Stress-Testing Mechanistic Claims in a Connectome-Constrained Visual Model

**Authors:** Aashish Dhawan

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13018v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13018v1)

**Summary:** Connectome-constrained neural networks make biological components directly accessible to intervention, but their mechanistic conclusions can still depend on the comparison model, intervention, circuit representation and trained solution. We stress-test these dependencies in flyvis, a \emph{Drosophila} motion-vision model, using its 50-model ensemble, task-matched causal CNN controls and replicated interventions. At the level of model behaviour, three-level reverse-phi reversal in flyvis is stron...

---

### 6. Lyapunov spectrum of random neural networks

**Authors:** David G. Clark

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12426v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12426v1)

**Summary:** The Lyapunov spectrum of a nonlinear recurrent neural network with random asymmetric couplings is calculated in the limit $N\to\infty$. The calculation is based on a finite-$N$ identity that expresses the cumulative distribution of Lyapunov exponents as a response function of the tangent-space dynamics, with the tangent trajectory selected by a minimum-norm condition rather than by an initial condition. A cavity method then determines this response function at large $N$ through a self-consistent...

---

### 7. Neural Decoding as Cognitive Inference

**Authors:** Yi Guo, Changhong Jing, Yong Hu, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11923v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11923v1)

**Summary:** The brain maintains stable cognition despite continuously changing neural activity. How to extract stable cognitive states from variable neural observations remains a central problem in neural decoding. Existing neural decoding methods map neural observations to predefined external labels based on the stimulus-response principle, often capturing recording-specific spurious correlations. Inspired by how the brain infers the world, and specifically by Bayesian brain theory, we recast neural decodi...

---

### 8. Cross-species representation learning aligns mouse and human neural dynamics and tracks clinical drug efficacy

**Authors:** Marko Tvrdic, Justin Richmond Domingo, Jae Ann Buenaluz, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11222v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11222v1)

**Summary:** Preclinical models poorly predict human drug efficacy, particularly in neurological disorders. Neural activity offers a uniquely rich source of translational information because it captures high-dimensional variation in nervous-system function that can be measured in both animals and humans. However, its high dimensionality makes it difficult to distinguish conserved disease-related features from variation arising from species, recording modality and experimental context. Here, we test whether s...

---

### 9. If the brain were so simple: Information-based drivers of intelligence and their interaction through an n-body-inspired framework

**Authors:** Brett J. Kagan, Johnson Zhou, Forough Habibollahi, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.11142v1) | 📄 [PDF](https://arxiv.org/pdf/2610.11142v1)

**Summary:** Theories of how the brain processes information and returns intelligent outputs are numerous and often difficult to conclusively test. Here, we consider an approach grounded in informatics and algorithmic thermodynamics for how neural systems respond to different patterns of information in different ways, with a focus on the relationship between the information entropy of a signal and a new proposed quantity we term information enthalpy, which represents the internal resource of structured infor...

---

### 10. Mean Field Theory Based on the Spike Time Response Curve for Synchronization Within and Between Two Alternating Populations of Neural Oscillators with Delays

**Authors:** Ananth Vedururu Srinivas, Carmen C. Canavier

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10977v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10977v1)

**Summary:** In order to study oscillators coupled by pulses emitted at discrete times, it is generally assumed that the effect of each pulse is an instantaneous phase shift, with a possible conduction delay between emission and receipt. However, we are interested in neural oscillators in which each pulse (action potential) activates a biexponential synapse, and at high frequencies, the duration of the synaptic conductance may be greater than the network period. Therefore, the effect of received pulses can s...

---

### 11. Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders

**Authors:** Rita Huan-Ting Peng, Nhat Bui

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10850v1)

**Summary:** As AI models move toward clinical decision-making and personalized treatment, understanding \emph{what} a model learns is important beyond predictive accuracy alone. We investigate whether personalized latent dynamics reveal clinically associated differences even when predictive fit is similar. A lightweight CNN--Transformer EEG foundation model pretrained on the Temple University EEG Corpus (TUEG) extracts segment-level representations. Using the Temple University Epilepsy Corpus (TUEP), repres...

---

### 12. Learning infinite context windows in recurrent architectures via spatial neural computing

**Authors:** Aleix Salvador-Pomarol, Arthur N. Montanari, Earl K. Miller, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10690v1)

**Summary:** Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to vanishing gradients and limited receptive fields. To address these limitations, we introduce a second-order recurrent model in which the standard neuron-to-neuron communication is replaced by a spatially evolving field governed by (discretized) partial differential equations. Drawing inspiration from the role of cortical...

---

### 13. Structure alone supports efficient visual computation in the Drosophila visual system

**Authors:** Eudald Correig-Fraga, Roger Guimerà, Marta Sales-Pardo

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.10023v1) | 📄 [PDF](https://arxiv.org/pdf/2610.10023v1)

**Summary:** Understanding the extent to which measured synaptic wiring determines computation remains a central challenge. Here, we couple the proofread adult Drosophila melanogaster connectome to an anatomically faithful model of its eye. Visual information is inputted in the eye model, then passed to the connectome, and finally read from a Kenyon-cell-centered linear decoder. This creates a connectome-only model in which the anatomical graph and eye geometry are fixed and only scalar synaptic gains and ne...

---

### 14. Feedback to the primary visual cortex is highly concentrated on the central visual field representation

**Authors:** Piotr Majka, Emmanuel K L Cho, Karolina Łabuszewska, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09983v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09983v1)

**Summary:** Retrograde tracer injections in marmoset monkeys revealed a striking feature of neural circuitry in primate visual system: among neurons projecting to the primary visual cortex (striate cortex, V1), the proportion of extrastriate feedback neurons relative to thalamic feedforward neurons decreases markedly with visual field eccentricity. This supports the Central-Peripheral Dichotomy theory, which proposes fundamentally distinct computational specializations --- visual recognition and attentional...

---

### 15. Do Generative Priors Align with Human Naturalness Perception?

**Authors:** Taiki Fukiage

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09928v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09928v1)

**Summary:** Visual generative models are trained to capture the probability distributions of natural images, yet whether their native priors reflect the regularities governing human perception of image naturalness remains an open question. Here, we probe these priors through native prediction errors across 25 open image and video generators. Because raw single-image losses are dominated by scene content and visual complexity, we evaluate directional loss differences using content-preserving, paired relation...

---

### 16. CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies

**Authors:** Gabriel Ocana-Santero, Marko Tvrdic

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09643v1)

**Summary:** Drug discovery for neurological disease has traditionally centered on the molecules altered by disease. But the molecules that cause pathology are not necessarily the best points from which to reverse it. Here, we ask which otherwise unaltered molecular control points can be engaged to restore pathological neural circuits toward functional states. We present CircuitATLAS, a provenance-grounded systems-neuroscience knowledge graph and agentic framework for target discovery in circuitopathies. It ...

---

### 17. Predicting Long-Term ADAS-Cog Change From Early Response After Repetitive Transcranial Magnetic Stimulation in Alzheimer Disease

**Authors:** Mohammad Alamgir Chowdhury, Hina Shaheen

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09629v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09629v1)

**Summary:** Early cognitive response after repetitive transcranial magnetic stimulation (rTMS) may predict later cognitive change in Alzheimer disease, but the incremental value of domain-specific response is unclear. We analyzed data from 112 randomized participants; 101 entered a Week-5 landmark cohort and 91 had complete predictors and outcomes at 8, 16, and 24 weeks post-treatment. Nested predictor-set comparisons used ridge regression to evaluate baseline information, trial variables, early total-score...

---

### 18. Connectome-Based Modeling of Mutation-Specific Amyloid-$β$ Aggregation in Familial Alzheimer's Disease

**Authors:** Mohammad Alamgir Chowdhury, Hina Shaheen

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09583v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09583v1)

**Summary:** Familial amyloid-$β$ (A$β$) variants alter aggregation kinetics, but their interaction with structural brain connectivity remains incompletely understood. We developed a mutation-aware mechanistic model coupling a coarse-grained monomer--oligomer--fibril aggregation--fragmentation system to graph diffusion on the 540-node Budapest Reference Connectome component. Experimental A$β_{42}$ nucleation scores scaled primary nucleation rates for seven variants relative to wild type. Robustness was exami...

---

### 19. Many Brains, One Geometry: A Shared Visual-Semantic Space for Cross-Dataset fMRI Decoding

**Authors:** Moein Khajehnejad, Michelangelo Tronti, Forough Habibollahi, et al.

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09352v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09352v1)

**Summary:** Visual decoding from fMRI is typically siloed by participant and experiment, obscuring whether heterogeneous neural measurements can be organized within a common computational geometry. Here we introduce BRAID-fMRI (Brain Representation Alignment across Individuals and Datasets), a shared CLIP-supervised decoding framework. BRAID-fMRI uses a single ROI-wise Transformer with optional participant conditioning across eight visual-fMRI datasets comprising 93 dataset-specific participant entries, 430...

---

### 20. MovieSTAGE: Scene, Transition, and Global Encoding for Movie-fMRI ADHD Classification

**Authors:** Boseong Kim, Haejun Chung, Ikbeom Jang

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09306v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09306v1)

**Summary:** Naturalistic movie-fMRI provides a shared, temporally structured probe of brain dynamics, yet predictive models commonly rely on whole-run functional connectivity (FC) or temporally generic representations that are not aligned with narrative events. We introduce MovieSTAGE (Scene, Transition, and Global Encoding), a multiscale framework that combines hypergraph-structured FC-profile organization within scenes, unsigned FC-profile differences across adjacent scenes, and whole-movie FC. We evaluat...

---

### 21. Scaling subjects in cross-modal alignment: video decoding with EEG foundation model

**Authors:** Dung Truong, Kuntal Kokate, Arnaud Delorme

**Published:** 2026-10-07

🔗 [Paper](http://arxiv.org/abs/2610.09287v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09287v1)

**Summary:** Naturalistic visual decoding from EEG has long been constrained by cohort size: existing scaling literature caps out at a few dozen subjects, leading prior work to conclude that scaling subject cohorts yields minimal performance gains. Training a cross-modal EEG--video contrastive encoder on a cohort larger by more than an order of magnitude, we find the axis is productive but has an onset. Below $S\approx50$ --- the entirety of the range prior work occupies --- no model improves meaningfully ov...

---

### 22. A Connectome Test of the Fly Hashing Algorithm

**Authors:** Sebastian Senge

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.09114v1) | 📄 [PDF](https://arxiv.org/pdf/2610.09114v1)

**Summary:** Dasgupta, Stevens and Navlakha (2017) showed that the Drosophila olfactory circuit, modelled as a random sparse projection followed by winner-take-all, is a locality-sensitive hash that beats classical LSH. The projection was random because the wiring was unknown. We test it against four electron-microscopy connectomes (MaleCNS, hemibrain, FlyWire, BANC; four animals, seven hemispheres). First, the 2017 pattern holds in a reimplementation of its protocol on SIFT, MNIST and odour mixtures (GloVe ...

---

### 23. Language-model ratings of depression reflect the rater more than the patient

**Authors:** Baihan Lin

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08501v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08501v1)

**Summary:** Depression has no diagnostic blood test. Language models promise tireless, consistent assessment, but can accurate raters disagree about individuals? We pre-registered 880 language-model raters, crossing 11 open models with prompting and scoring choices, and applied them to 189 interviews against the eight-item Patient Health Questionnaire. Model choice explained 30.0% of summed-symptom score variance, stable participant differences 10.5%. Two randomly drawn raters with area under the receiver o...

---

### 24. From the Drosophila Visual Connectome to General-Purpose Computer Vision

**Authors:** Zongyu Li, Akito Yamauchi, Huaizhi Liu, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08418v1)

**Summary:** Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and ...

---

### 25. A Time-Resolved Framework for Quantifying Neuronal Network State Transitions

**Authors:** Ilya Auslender, Yasaman Heydari, Asiye Malkoç, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08392v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08392v1)

**Summary:** Electrophysiological recordings provide powerful tools for characterizing the dynamics of neuronal networks. In vitro neuronal cultures offer a controlled setting for investigating network responses to diverse interventions, including pharmacological and optogenetic stimulation. However, conventional analyses often reduce electrophysiological activity to aggregate measures calculated over fixed temporal windows, providing only a static representation of the network state. Here, we introduce a co...

---

### 26. Confidence-Ordering Reversal under Contextual Priors in Neural Decoding

**Authors:** Xinyu Zhang, Sichao Liu

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08229v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08229v1)

**Summary:** Contextual priors improve neural-to-language decoding by reshaping candidate scores. However, confidence is read from the same reshaped scores, so the errors a prior leaves behind can become more confident with no change in accuracy to reveal it. We study how a prior shapes confidence in speech retrieval on MEG-MASC and MOUS using local decoding scores, a contextual prior combined by additive shallow fusion, and the fused top-two margin as confidence. Among initially incorrect predictions, we fi...

---

### 27. Neural networks as decision trees: an analytical solution for learning and neural selectivity

**Authors:** Hugo Tissot, Jonas Ranft, Yves Boubenec

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.08228v1) | 📄 [PDF](https://arxiv.org/pdf/2610.08228v1)

**Summary:** Nonlinear neural networks develop structured internal representations, yet how their geometry is determined by the tasks being learned remains poorly understood. Here, we develop an analytical framework for piecewise-linear feedforward and recurrent networks that links learning, activation-region structure, and neural selectivity. We show that, at any stationary point of gradient-aligned learning, a nonlinear network decomposes into local linear regressions over its activation regions. Deviation...

---

### 28. ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams

**Authors:** Hyewon Kang, Jungmin Lee, Ilgyu Lee, et al.

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07962v1)

**Summary:** Where generalization capacity--the ability to extract context-invariant relational structures--first emerges remains a central question in AI and neuroscience. The foundation for this capacity lies upstream of the hippocampus, within the entorhinal cortex, where parallel pathways dissociate relational structure in the medial entorhinal cortex (MEC) from sensory content in the lateral entorhinal cortex. However, as Eichenbaum argued, such factorization likely originates earlier, driven by the seg...

---

### 29. CANDLE: Cortical Null-Space Decomposition for Noninvasive Brain Source Imaging

**Authors:** Shuntaro Suzuki, Yuiga Wada, Komei Sugiura

**Published:** 2026-10-06

🔗 [Paper](http://arxiv.org/abs/2610.07824v1) | 📄 [PDF](https://arxiv.org/pdf/2610.07824v1)

**Summary:** Electrophysiological source imaging (ESI) aims to estimate cortical source activity from noninvasive electrophysiological measurements such as electroencephalogram (EEG). However, ESI is fundamentally ill-posed because source activity is substantially higher-dimensional than sensor observations, resulting in non-unique solutions. Recent learning-based approaches address this ambiguity by learning data-driven source priors, yet they often struggle to generalize across subject-specific cortical ge...

---

### 30. Interplay between Excitability and Noise in Analog Spiking Neurons

**Authors:** Léopold Van Brandt, Alon Ascoli, Michele Bonnin, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06720v1)

**Summary:** A spiking neuron is a dynamical system exhibiting a limit cycle (a spike) when subject to sufficiently excitatory input. Famous neuroscience experiments by Bryant and Segundo as well as Mainen and Sejnowski revealed that the spike times of some biological neurons are more reliable when subject to time-varying stimuli compared to constant ones. Provided with an industrial physics-based transient noise SPICE simulation framework compatible with foundry transistor compact models, we have demonstrat...

---

### 31. COMPASS 2.0: psychometric representational similarity analysis distinguishes symptom structure from personal signal

**Authors:** Baihan Lin

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06615v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06615v1)

**Summary:** Language models can score psychiatric questionnaires from speech, but agreement with self-report may reflect the questionnaire rather than the person. We introduce psychometric representational similarity analysis, a framework for comparing the structure of speech-derived scores, self-report, item wording and theory, and implement it alongside person-level construct scoring in COMPASS 2.0. We show how similarly worded items induce covariance without psychological signal. In pre-registered discov...

---

### 32. NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI

**Authors:** Felix Nieto-del-Amor, Jingru Fu, J. -Sebastian Muehlboeck, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06502v1)

**Summary:** Content-based image retrieval (CBIR) in neuroimaging enables the identification of structurally similar brain scans, supporting diagnosis, prognosis, and treatment planning; however, existing methods are often limited to small datasets, single brain regions, or coarse class labels, thereby restricting their clinical utility and generalizability.   Here, we present NeuroCBIR, a framework for fast and flexible retrieval of both whole-brain and region-specific 3D T1w MRI scans. A total of 103 corti...

---

### 33. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 34. CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI

**Authors:** Boseong Kim, Haejun Chung, Ikbeom Jang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05913v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05913v1)

**Summary:** Task-fMRI connectomes reveal state-dependent neural reconfigurations, yet conventional methods marginalize these signals by aggregating distinct conditions into static pairwise graphs, thereby obscuring condition-specific multi-ROI organization. We introduce CoHyFuse, a condition-aware ROI-centered hypergraph framework that constructs a task-state-specific incidence matrix from condition-wise functional connectivity (FC)-profile embeddings, allowing the same ROI to form different multi-ROI hyper...

---

### 35. Lightweight Semantic EEG Foundation Model for Frozen Cross-Disorder Transfer

**Authors:** Rita Huan-Ting Peng, Nhat Bui

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05503v1)

**Summary:** Large-scale EEG foundation models have demonstrated promising transferability across neurological disorders, but often require millions of parameters and substantial computational resources. In this paper, we present the Universal Semantic EEG Foundation Model (USE-FM), a lightweight EEG foundation model that learns transferable neural representations through self-supervised signal reconstruction on the Temple University Hospital EEG Corpus (TUEG). After pretraining, the encoder is frozen and ev...

---

### 36. Recurrent network dynamics explain the time course of perceptual grouping in natural scenes

**Authors:** Sami Mollard, Alekh K. Ashok, Lore Goetschalckx, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05419v1)

**Summary:** How the brain groups image elements into coherent objects in natural scenes remains unclear. Existing models for grouping in biological vision rely on simplified stimuli with explicit boundaries and cannot explain human behavior in naturalistic settings. We propose a mechanistic framework in which recurrent interactions propagate enhanced neuronal activity within and between cortical areas. The framework links computational principles, neural circuitry and perceptual psychology. Local boundary s...

---

### 37. Efficiency and robustness partition the solution space for memory in recurrent networks

**Authors:** William Qian, Cengiz Pehlevan

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04697v1)

**Summary:** In computational neuroscience, task-trained recurrent neural networks (RNNs) are commonly used as a testbed for exploring the space of recurrent circuit solutions compatible with a particular function. However, these networks are subject to inductive biases that may be misaligned with those of biological circuits, which operate under various efficiency and robustness constraints. Here, using a minimal stimulus recall task, we systematically characterize how the solution space of recurrent neural...

---

### 38. Heterarchy in the Brain: Control as a Spectrum, Not a Chain of Command

**Authors:** Luiz Pessoa, Andrea Gambarotto

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04643v1)

**Summary:** Neuroscience treats the brain as a control hierarchy, with cortical systems governing subcortical mechanisms. We argue that this mistakes a configuration for an architecture. Local asymmetries of influence are real, but control is relational and process-specific; because neural elements constrain one another across concurrent processes, relations can form cycles that resist a stable ranking. Evidence from learned action, cortico-cerebellar and thalamocortical loops, and defensive behavior shows ...

---

### 39. Beyond Completion Time: A Multimodal Approach to Characterizing Eye-Hand Coordination During the Nine-Hole Peg Test in Multiple Sclerosis

**Authors:** Mahya Beheshti, Rajvardhan Gadde, Diana Maloku, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04145v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04145v1)

**Summary:** Multiple sclerosis (MS) can impair upper-extremity function through motor, sensory, cognitive, and visual deficits. Although the Nine-Hole Peg Test (9-HPT) is widely used to assess dexterity, completion time alone provides limited insight into the eye-hand coordination underlying performance. We characterized 9-HPT performance in nine people with MS (PwMS) and nine healthy controls using simultaneous eye tracking, markerless hand tracking, and object detection. Each peg cycle was divided into tr...

---

### 40. Multimodal Physiological Decoding Reveals Individualized Arousal Dynamics in Closed-Loop Neurofeedback

**Authors:** Anirudh Natarajan, Paul Sajda

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04113v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04113v1)

**Summary:** Most arousal-based brain-computer interfaces (BCIs) use EEG to decode cognitive state. But arousal is an autonomic process. We examined if peripheral physiological signals give a better decode of task-related arousal. We used a public dataset from a difficult boundary-avoidance flight task. In this task, participants received EEG-based BCI neurofeedback, sham feedback, or no feedback. We trained a multimodal deep learning decoder on heart rate, heart rate variability (HRV), respiration, electrod...

---

### 41. MEM as an Extension of Recurrent Processing Theory: Toward a Motivational Account of Consciousness

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04057v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04057v1)

**Summary:** Victor Lamme's Recurrent Processing Theory (RPT) proposes that the feedforward sweep (FFS) can extract and categorize visual features unconsciously, while conscious vision emerges through recurrent processing and feedback interactions across representational levels. The Motivated Emotional Mind (MEM) model, developed by Wiesław L. Galus and Janusz A. Starzyk, retains this core principle but embeds it in an embodied architecture integrating multilayer networks, semi-hierarchical semblions, recept...

---

### 42. Stability of Phase-locked States of Weakly Coupled Izhikevich Neurons

**Authors:** XinYe Cheng, Sue Ann Campbell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04025v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04025v1)

**Summary:** The Izhikevich model is a computationally efficient neuron model that can exhibit a wide range of firing patterns observed in the brain. However, it is a discontinuous dynamical system, which means the methods for applying weakly coupled oscillator theory developed for continuous dynamical systems cannot be applied. Therefore, the collective behaviour of coupled Izhikevich model has not been fully studied. To our knowledge, we carry out the first computation of the phase model for an Izhikevich ...

---

### 43. Broken scale symmetries in undercomplete linear autoencoders

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03640v1)

**Summary:** Neural network loss landscapes have many symmetries, which are preserved by gradient flow but broken by finite-stepsize stochastic gradient descent (SGD). A canonical example of such a symmetry is scale in homogeneous networks: one can scale up the parameters in one layer and down in the next without changing the network output. Previous work has documented cases in which SGD breaks this symmetry in favor of balancing gradient noise or minimizing fluctuations. Here, we show that the solution geo...

---

### 44. Contrastive Neural Embeddings Reveal Individual Traits Beyond Conversational Role

**Authors:** Hubert Huang, Michelle McCleod, Brendan Ames, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03410v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03410v1)

**Summary:** Contrastive representation learning is increasingly used to recover low-dimensional structure from neural recordings, but its output is typically validated by decoding accuracy rather than by the geometry of the manifold it produces. We apply CEBRA to EEG recorded from dyads in conversation, and analyze the resulting embedding, which training constrains to the 2D sphere. Labels describing the dyads, including the absolute difference between partners' autism-quotient scores, decode well above cha...

---

### 45. The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer

**Authors:** Saman Rahbar

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03827v2) | 📄 [PDF](https://arxiv.org/pdf/2610.03827v2)

**Summary:** Similarity scores are often offered as evidence that a model shares structure with the brain or across languages. We ask what such a score reads when that structure is removed, or when the instrument measuring it does not work, in two settings. Across seventeen languages, a grammaticality probe transfers worse between more distant languages (r = -0.66). But the probe's own accuracy falls along the same axis and is at chance in four languages, four of the five most distant. Dropping them halves t...

---

### 46. Response Variability and Stability in Human Reasoning

**Authors:** Clemens Bombach, Rajmadan Lakshmanan, Marco Ragni

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03008v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03008v1)

**Summary:** Understanding how humans reason -- and how reasoning responses vary across tasks and individuals -- remains a core challenge for modeling and explanation in cognitive science. We investigate the stability of response patterns within reasoners and whether variation in these patterns can be used to predict learning effects. We introduce a formal, geometry-based method to quantify distances between individual reasoning patterns and their internal variability, grounded in heuristic theories. The pro...

---

### 47. NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings

**Authors:** Hanrui Lyu, Baiyuan Chen, Tianshu Tan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02864v1)

**Summary:** Understanding how neural activity represents higher-order cognition and how these representations evolve over time has long been a central pursuit in neuroscience. However, current analytical tools cannot easily distinguish representational plasticity from recording instability in chronic neural recordings. Here, we introduce NeuroLens (Latent Embeddings of Neural Semantics), a self-supervised model based on the Joint-Embedding Predictive Architecture (JEPA) framework that learns denoised, seman...

---

### 48. A foundation for systematic analysis of transformers and RNNs for tractography

**Authors:** Emmanuelle Renauld, Philippe Poulin, Hugo Larochelle, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01894v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01894v1)

**Summary:** Machine learning (ML) has emerged as a promising approach for improving diffusion MRI (dMRI) tractography, a task that remains limited by the intrinsic tension between local diffusion information and global anatomical plausibility. In this work, we systematically evaluate recurrent neural networks (RNNs) and Transformer models for iterative tractography, with particular attention to training strategies, input representations (including convolutional neural network (CNN)-based embeddings and end-...

---

### 49. Inferring Multi-Timescale Neural Dynamics with Switching Linear Dynamical Systems

**Authors:** Lulu Gong, Yongxu Zhang, Shreya Saxena

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01786v1)

**Summary:** Neural activity often exhibits multiple timescales that can vary with behavioral states and task conditions. Identifying these timescales from neural recordings is important for better understanding neural computation and function. However, traditional approaches based on autocorrelation fitting are difficult to scale to high-dimensional population recordings and can become unreliable when neural dynamics change with behavior. State-space models have been a powerful framework for modeling high-d...

---

### 50. A High-Density EEG Dataset for Stimulus-Driven Auditory Attention

**Authors:** Ruofan Yan, Na Lu, Shu Peng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01303v1)

**Summary:** Stimulus-driven auditory attention determines which sound gains priority when multiple sources compete without an explicit listening goal, yet most computational studies focus either on acoustic salience or on decoding predefined attended targets. This study investigates instruction-free auditory competition using the Stimulus-driven Auditory Attention (SAAD) paradigm and develops a neurophysiologically informed framework that integrates stimulus-derived sound priority with trial-specific EEG ev...

---

## stat.ML

**50 papers**

### 1. Markov Chain Convergence in Kernel-Induced Geometry

**Authors:** Oleksii Kachaiev, Luc Brogat-Motte, Silvia Villa, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13916v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13916v1)

**Summary:** We study the convergence of Markov chains in the geometry induced by Hilbertian embeddings associated with positive definite kernels, also called Maximum Mean Discrepancy (MMD). Under a contraction assumption in the kernel-induced geometry, and a standard spectral gap assumption, we establish non-asymptotic, high-probability bounds for the convergence of the empirical occupation measure to the invariant measure. The obtained bounds separate the roles of the two conditions: the spectral gap deter...

---

### 2. Hitting-Time Bounds for Asynchronous Q-Learning

**Authors:** Yang Peng

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13901v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13901v1)

**Summary:** We study the last iterate of standard asynchronous Q-learning from a single trajectory of a finite Markov decision process. The trajectory follows a fixed behavior policy whose state--action chain is irreducible and may be periodic. For discount factor $γ$, write $H=(1-γ)^{-1}$, and let $μ_{\min}$ be the minimum stationary state--action probability and $\mathfrak h_\star$ the largest expected hitting time of the reverse state--action chain. We prove that zero-initialized Q-learning with a consta...

---

### 3. SLICE: Sequential Likelihood-Free Inference via Conformal E-Values

**Authors:** Stefano Cortinovis, Laura Battaglia, François Caron

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13855v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13855v1)

**Summary:** Many scientific models can be simulated but have intractable likelihoods, making frequentist uncertainty quantification difficult. We construct exact anytime-valid confidence sequences for the parameters of such models. At each observation, fresh simulations from each candidate null conformalize a positive predictable score into a conditional e-value; their product is a test martingale, which we invert over the parameter. Validity holds for any such score, whatever its accuracy. We show that the...

---

### 4. Finite-Sample Guarantees for Fully Discrete Conditional Diffusion Models

**Authors:** Qiuyun Zhu

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13851v1)

**Summary:** We establish finite-sample guarantees for conditional diffusion models learned from data and implemented with finitely many denoising steps. Our approach aligns the score-training objective with the sampling grid, allowing statistical estimation and numerical discretization errors to be analyzed together. Under a smooth conditional density model, we derive high-probability bounds on the generated distribution's error and quantify the required number of score evaluations. For every smoothness ind...

---

### 5. Constrained Probabilistic Numerics: Gaussian Process Solvers for Linear PDEs under Linear Inequality Constraints

**Authors:** Boyuan Deng, Kshitiz Upadhyay, Michael Shields

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13804v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13804v1)

**Summary:** Gaussian process solvers for linear partial differential equations (PDEs) return posteriors rather than point estimates, but they condition only on equality information: the PDE residual, boundary data, and measurements. Many solutions of interest also obey inequality constraints, including nonnegativity, monotonicity, and absence of arbitrage, which equality conditioning cannot enforce. We prove that conditioning a Gaussian process prior jointly on linear equality observations and a finite-dime...

---

### 6. From Pixels to Privacy-Sensitive Features: An Information-Theoretic Framework for Reconstruction Bounds

**Authors:** Henry Bourne, Robert F. Allison

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13768v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13768v1)

**Summary:** What can an adversary recover from a model trained with DP-SGD? Its $(\varepsilon,δ)$ guarantee does not answer this question directly. We derive a distortion bound that can be computed before training and applies even to an adversary who observes the parameter trajectory during training, knows every other training record and the population distribution from which the training records are drawn. The analyst may choose the representation in which error is measured, allowing the bound to target th...

---

### 7. How Well Do Prior-Data Fitted Networks Amortize Bayesian Inference?

**Authors:** Manuel Hülskamp, Julius Kobialka, Emanuel Sommer, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13764v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13764v1)

**Summary:** Prior-data fitted networks (PFNs) are trained to approximate the Bayesian posterior predictive distribution (PPD) of a synthetic prior, yet results about the approximation quality are surprisingly thin. Taking an empirical risk minimization perspective, we decompose the deployment error of PFNs into prior, context, and amortization error, and measure the latter against a reference PPD under a realistic prior. Results show that PFNs generally recover the targeted PPD very well. Nevertheless, we f...

---

### 8. Calibration in One Go: Jointly Learning Accurate and Calibrated Neural Networks

**Authors:** Nektarios Kalampalikis, Pablo M. Olmos, Isabel Valera

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13693v1)

**Summary:** Neural networks (NNs), while highly flexible and versatile, are often poorly calibrated. Post-hoc calibration methods adjust the outputs of an already trained model using a separate calibration dataset and additional calibration parameters. This process adds overhead that requires separate optimization of the calibrator and subsequent model selection. In this paper, we show that standard (post-hoc) calibrators can be trained end-to-end with the backbone via a bilevel Stackelberg formulation. Thi...

---

### 9. Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped Quadratic Kernels

**Authors:** Weiqi Sun, Qianyue Wu, Wenjia Wang, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13674v1)

**Summary:** Linearizing softmax attention offers a route to efficient Transformer inference, but preserving pretrained attention remains challenging. We identify an important source of approximation error overlooked by standard linearization methods: a small number of outlier dimensions contribute disproportionately to query-key dot products and account for a large fraction of the approximation error. Motivated by this heterogeneity, we propose Outlier-Aware Attention Linearization (OAL), a dimension-aware ...

---

### 10. Scalable Sparse Autoregressive Variational Inference for Non-Gaussian Spatial Fields

**Authors:** Paul F. V. Wiemann, Matthias Katzfuss

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13656v1)

**Summary:** Latent field models are essential for spatial statistics, but the posterior distribution of the latent field, even with a Gaussian process (GP) prior, is analytically intractable whenever the likelihood is non-Gaussian. Existing approximations are either too slow or too restrictive for large non-Gaussian datasets. We present a scalable variational inference framework that mirrors the sparse nearest-neighbor autoregressive structure of the prior in the variational family, uses normalizing-flow co...

---

### 11. A Critical Look at Power Sampling when Test Time Sharpening LLMs

**Authors:** Abiel Malkani Talwar, Christopher Nemeth, Henry Moss

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13653v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13653v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has substantially improved LLM reasoning, yet growing evidence suggests it mainly performs distribution sharpening: concentrating probability mass on reasoning paths the base model already produces. Recent work therefore seeks RLVR's gains without needing reward signals, by sampling from the power distribution $π_α\propto π_{\text{base}}^α$ via Markov chain Monte Carlo or sequential Monte Carlo. We show that these samplers fail to converge to...

---

### 12. Kernel-based External Validity of Experimental Studies

**Authors:** Federico Matteucci, Gerhard Neumann

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13625v1)

**Summary:** The external validity of a study is the extent to which its findings generalize to unseen experimental conditions, such as datasets. We formalize the results of a study together with its research question, and define external validity as the probability that two independent and same-sized replications of the study produce results whose maximum mean discrepancy (MMD) is below a given tolerance. This approach, centered on the choice of a space of results and of an appropriate reproducing kernel fo...

---

### 13. Some remarks on the connection between generative diffusion and optimal transport

**Authors:** Giulio Biroli, Marc Mézard

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13614v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13614v1)

**Summary:** We discuss three simple connections between generative diffusion and optimal transport. First, the joint law of the data and of their Ornstein-Uhlenbeck noising is, at every time, the solution of an entropic optimal-transport problem, at a temperature set by the noise level. Backward diffusion can consequently be read as an annealing which gradually decreases the entropic regularization. Second, we study the speciation transition--how the modes of the data distribution emerge during generation--...

---

### 14. CorrFlow: Exact and Permutation-Equivariant Flow Matching on the Correlation Elliptope

**Authors:** Gautier Marti

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13606v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13606v1)

**Summary:** Correlation matrices combine nonlinear positive-definiteness constraints with a simultaneous row-column permutation symmetry. Their generation therefore involves two distinct problems. First, every output must remain on the correlation elliptope, irrespective of how its variables are ordered. Second, the generator must learn the domain-specific distribution occupied by empirical data inside that valid space. Existing financial image generators mix these problems: they learn ordered matrix entrie...

---

### 15. Beyond Discrepancy: Oracle Drift in Nonstationary Weighted Risk Minimization

**Authors:** Tobias Brock, Thomas Nagler

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13598v1)

**Summary:** We analyze distributional drift in nonstationary weighted risk minimization by decomposing the excess risk into estimation, drift, and approximation components. The drift error is commonly bounded through discrepancy-type quantities that control changes of the risk over classes of predictors. We instead relate the drift error directly to the movement of the best predictor within the model class and analyze its behavior in parametrized regression models. Our analysis shows that discrepancy-type q...

---

### 16. Probabilistic Forecasting of Electric Vehicle Charging in a Time-varying Hierarchical Infrastructure

**Authors:** Guillaume Principato, Yvenn Amara-Ouali, Yannig Goude, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13588v1)

**Summary:** Uncertainty quantification for electric vehicle (EV) charging demand is essential to turn the increasing pressure of EV adoption on power systems into a source of flexibility. We study a large-scale dataset of public charging stations in Scotland, where demand exhibits a hierarchical structure, organized across multiple aggregation levels, from individual charging points to regional and national scales. The charging infrastructure is continuously evolving, with new stations deployed and existing...

---

### 17. Defence against the dark arts of distillation: Unsupervised discovery of subliminal learning

**Authors:** Joseph Egan, Ciarán M. Gilligan-Lee, Michael O'Riordan, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13536v1)

**Summary:** When a language model is distilled from a teacher that shares its base parameters, the student can inherit behavioural traits of the teacher---including misalignment---even from data that is semantically unrelated to the trait (Cloud et al., 2026). All existing defences require knowing the trait. We remove this requirement and prove that a subliminally transferred trait can be recovered from the parameter updates alone, without supervision, by exploiting a single asymmetry: the trait is expresse...

---

### 18. Gaussian BROJA Partial Information Decomposition in Closed Form

**Authors:** Ohad Sheelo, Tal Golan, Ari Pakman

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13464v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13464v1)

**Summary:** The BROJA partial information decomposition provides an operationally motivated way to separate the information that two sources carry about a target into unique, redundant, and synergistic components. For continuous and high-dimensional variables, however, computing the BROJA decomposition requires solving a difficult optimization problem. Previous work showed that, when each source-target pair is jointly Gaussian, the problem can be reduced to finite-dimensional numerical optimization. Here, w...

---

### 19. Learning by Compression: Risk Estimates Attain the Law-of-Large-Numbers Rate

**Authors:** Simone Garatti, Marco C. Campi

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13442v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13442v1)

**Summary:** Compression schemes provide a general framework for deriving data-dependent risk bounds for learning algorithms. For learning rules based on preferent compression, existing results upper-bound the risk in terms of a sample-dependent complexity $\boldsymbol{k}$, defined as the cardinality of the compression augmented by the training examples on which the reconstructed hypothesis is inappropriate. These results, however, yield a margin of order $O(\sqrt{\ln N/N})$ above $\boldsymbol{k}/N$. In this...

---

### 20. One Thing Leads to Another: The Essentials of Time Series Causal Discovery

**Authors:** Kurt Butler, Damian Machlanski, Michael P. J. Camilleri, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13430v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13430v1)

**Summary:** Time series causal discovery --- the process of detecting causation between time series --- has its roots in signal processing research from over a half century ago. It has since received active and widespread interest, evolving into different forms across domains such as statistics, dynamical systems and machine learning. Entering this fragmented and constantly evolving research landscape can be daunting. This tutorial provides a unified overview of time series causal discovery across research ...

---

### 21. Model-free Bayesian Clustering and Multimodal Posterior Summarisation

**Authors:** Qing Li, Sara Wade

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13397v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13397v1)

**Summary:** We develop a model-free, noise-aware Bayesian clustering framework that constructs a martingale posterior over clusterings from a predictive Bayesian perspective. This avoids explicit likelihood-prior model specification, expensive MCMC sampling, and mode-seeking variational approximations, while accommodating irregular cluster shapes and enabling parallel generation of posterior draws. To interpret the posterior over high-dimensional, noise-aware clusterings, we introduce a Wasserstein-type sum...

---

### 22. BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning

**Authors:** Giordano Vitale, Giacomo Meanti, Marco Rando, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13382v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13382v1)

**Summary:** Kernel Ridge Regression (KRR) is a theoretically sound algorithm for nonparametric learning, which is also often used to investigate properties of deep learning. However, the exact KRR formulation incurs time and memory costs preventing applicability to large datasets, motivating the development of approximate solvers. These algorithms rely on (i) iterative methods, to avoid the computational burden of direct solutions; (ii) sketching or batching, to reduce the problem size; and (iii) preconditi...

---

### 23. Fast Gradient-Based Approximation of Continuous Dynamic Time Warping

**Authors:** Pierre Houedry, Romain Tavenard, Nicolas Courty, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13129v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13129v1)

**Summary:** Dynamic Time Warping (DTW) is a common choice for measuring the discrepancy between time series. It proceeds by finding an optimal warping between timestamps through dynamic programming, which can be slow and is not differentiable. Consequently, several variants have been proposed. Among them, Soft-DTW proposes a smooth formulation of DTW, amenable to gradient computation, while Continuous-DTW (CDTW) introduces a continuous formulation through parametrizable warping functions. Yet, computational...

---

### 24. Why Heavy-Tailed Weight Spectra Predict Model Quality

**Authors:** Joseph Wilson, Chris van der Heide, Liam Hodgkinson, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.13123v1) | 📄 [PDF](https://arxiv.org/pdf/2610.13123v1)

**Summary:** A solid understanding of the predictive success of deep neural networks (DNNs) remains elusive. For example, while many data-dependent metrics exist that seek to predict model quality of DNNs, these metrics may be expensive to compute for large datasets and/or may be impossible to compute when training datasets are not released. A practical and effective predictor of model quality involves analyzing DNN weight matrices, as prior work has established that heavy-tailed spectral distributions in tr...

---

### 25. Forecasting Corpus-Sampling Disagreement in Masked Text Reconstruction

**Authors:** Hare Krishna

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12987v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12987v1)

**Summary:** If a second text corpus were collected from the same population, how much would a predictor's outputs change? We study this question for masked-text reconstruction using a smoothed predictor built from nearby token-pair counts and evaluated over the full 50,257-token GPT-2 vocabulary. Treating each source document as one observation, we derive a first-order formula for the expected disagreement between predictors fitted to two independent corpora. The formula accounts for variable document lengt...

---

### 26. Scan-Parallel Variational Inference for event-driven Latent Jump Models

**Authors:** Vansh Bansal, Min Chen, James G. Scott

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12986v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12986v1)

**Summary:** Continuous-time latent state-space models are widely used for irregularly observed time series, typically representing uncertainty through a random initial state followed by smooth ordinary differential equation (ODE) dynamics, or Brownian perturbations accumulated by a stochastic differential equation (SDE). While these constructions are natural for smooth or diffusive systems, they do not directly encode a finite set of unobserved shocks whose timing, magnitude, and effect on memory are themse...

---

### 27. Spatial Prediction with Guided Diffusion

**Authors:** Andrew Zammit-Mangion, Lachlan Astfalck, Raphaël Huser, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12967v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12967v1)

**Summary:** Spatial prediction is a critically important task in data analyses that involve spatially or spatio-temporally-referenced data. It is commonly carried out using hierarchical models, which comprise a process model describing the latent process of interest, and a data model describing how the process is observed. The target quantity is the predictive distribution, which is the conditional distribution of the latent spatial process given the observed data. Unfortunately, the predictive distribution...

---

### 28. From Imbalance to Evidence: Deep Nonparametric Testing for Complex Data under Severe Sample Imbalance

**Authors:** Guanhao Zhou, Xiufan Yu

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12946v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12946v1)

**Summary:** Comparing distributions under severe sample imbalance requires effectively using abundant majority observations while retaining sensitivity to differences involving the smaller sample. This challenge is particularly relevant for complex, non-Euclidean data, such as graphs, whose structural characteristics call for flexible testing procedures. Classifier two-sample tests (C2STs) provide such flexibility, but existing procedures are primarily designed for balanced or comparably sized samples. In t...

---

### 29. Sparse Dictionary Learning for Measure-Valued Data via Linearized Optimal Transport: Efficient Algorithms and Sample Complexity

**Authors:** Brendan Mallery, Shuchin Aeron, James Murphy

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12924v1)

**Summary:** We study dictionary learning for probability measure-valued data by embedding measures into Hilbert spaces using features derived from optimal transport geometry. We learn data-adapted dictionaries through sparse autoencoder parameterizations, producing fast, scalable representations of probability measures as sparse finite-dimensional codes. The resulting framework combines the rich, geometric structure of optimal transport with the interpretability and efficiency of sparse representation learn...

---

### 30. Beyond Second-Order Information: Paid Logistic Regression with Noisy Features

**Authors:** Sanghwa Kim, Kyoungseok Jang, Se-Young Yun

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12919v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12919v1)

**Summary:** We consider online binary prediction with paid stochastic features, where the learner can spend resources to obtain better observations of the underlying features. This setting is motivated by applications such as medical testing, where additional cost can provide more precise measurements of patient's features for predicting a binary outcome. At each round, a latent feature is drawn i.i.d., the response is generated through a logistic model, and the learner chooses how much to pay before observ...

---

### 31. Generalized Determinantal Point Processes for Attraction and Repulsion with Distinct Interaction Kernels

**Authors:** Hideaki Ishibashi, Takahiro Kawashima, Hideitsu Hino

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12894v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12894v1)

**Summary:** Determinantal point processes (DPPs) model subset selection probability with repulsion, but many applications also exhibit attraction arising from pairwise relations or shared latent structures. Nonsymmetric DPPs (NDPPs) capture both effects, but their kernels are difficult to interpret and specify. We propose the determinant-ratio point process (DRPP), which models repulsion and attraction via a ratio of the determinants of two symmetric positive-definite kernels. This formulation preserves the...

---

### 32. Universal Bounds for Self-Normalized Kullback-Leibler Estimation

**Authors:** Buu Phan, Lester Mackey, David Alvarez-Melis

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12851v1)

**Summary:** This work studies an entropy-based estimator of Kullback-Leibler (KL) divergence constructed from normalized importance weights. We prove a universal finite-sample bound showing that its expectation can exceed the target-proposal KL divergence by at most $\log 2$ for any sample size. We then characterize the KL divergence between the distribution induced by importance-weighted resampling and the proposal, showing that it is upper bounded by both the expectation of the entropy-based estimator and...

---

### 33. Two-way Guidance: Simultaneous Learning of Summary Statistics for Generative Bayes

**Authors:** Percy S. Zhai, Max Pachman, Peverel D. Shipley, et al.

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12850v1)

**Summary:** Bayesian simulation-based inference (SBI) can struggle to recover increasingly concentrated posteriors as observation size grows. We consider learning sufficient summary statistics jointly with the posterior as a general principle for scalable inference in various SBI methods. A common measure taken in SBI is dimension reduction through predetermined summaries, which may partially discard posterior information. Our approach instead imposes structure on how the posterior learner depends on a lear...

---

### 34. Scalable Learning of Determinantal Point Processes with Kernel-Structured Interactions

**Authors:** Takahiro Kawashima, Hideitsu Hino

**Published:** 2026-10-09

🔗 [Paper](http://arxiv.org/abs/2610.12829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12829v1)

**Summary:** Determinantal point processes (DPPs) on a finite set are probability models that exhibit repulsion where inter-item similarities are encoded by a positive definite kernel matrix. Scaling DPP learning to large datasets typically requires imposing structural constraints on the kernel matrix, such as a low-rank-plus-diagonal form. However, structural assumptions introduce a severe trade-off between expressive power and computational scalability. Our study addresses this challenge by (a) modeling th...

---

### 35. Minimax Rates for Estimating Powered Sliced Wasserstein Functionals

**Authors:** Binh Thuan Tran

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12740v1)

**Summary:** We study the two-sample estimation of the powered Sliced Wasserstein functional under projected $r$-th moment assumptions. Let $N=n\wedge m$, where $n$ and $m$ are two sample sizes. We establish the minimax rates in the noncritical regimes. When $p<r<2p$, the minimax risk is of order $N^{-(r-p)/r}$, while for $r>2p$ it is of order $N^{-1/2}$. In both cases, the natural plug-in estimator is minimax rate-optimal. At the endpoint $r=p$, the minimax risk is bounded away from zero, so uniformly consi...

---

### 36. Kernelized Parameter Sensitivity Atlases for Amortized Conditional Interpretability

**Authors:** Davide Wiest, Ahanaf Hasan Ariq, Abdul Monaf Chowdhury

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12737v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12737v1)

**Summary:** Gradient-based attribution provides input-specific information about model parameters, but computing it via backpropagation for many samples is expensive, while static importance scores discard input dependence. We derive KPSA (Kernelized Parameter Sensitivity Atlas) from a block decomposition of the empirical neural tangent kernel. It measures normalized parameter-group sensitivity, embeds those sources in an explicit query space, and uses a lightweight kernel to estimate sensitivities for unse...

---

### 37. A Distributional Framework for Behavioral Characterization and Risk Management of Large Language Models

**Authors:** David García-Lorite, Raul Merino

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12718v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12718v1)

**Summary:** Large language models are stochastic by nature. Repeated executions under the same experimental conditions may produce different responses. We propose a framework that can be applied across the model lifecycle, from task design to residual behavior and continuous monitoring. The method consists of building an empirical response distribution estimated through Monte Carlo simulation. Semantic interventions are introduced to study how these distributions change. We illustrate the framework with two...

---

### 38. Amortised Inference through One-Step Implicit Sampling

**Authors:** Vincent Pauline, Kirill Tamogashev, Arran Carter, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12679v1)

**Summary:** Efficient sampling from Bayesian posterior distributions in high dimensions remains a hard problem, despite advances in theory and algorithms. Multiple steps are usually required to draw unbiased samples, for example, iterations of an MCMC algorithm or integration steps in a diffusion-based amortised sampler. However, scalable one-step amortised inference remains a challenging open problem. In this work, we build upon recent progress in data-driven generative modelling to offer a possible soluti...

---

### 39. On the estimation and validity of AI time horizons---a statistical look at the METR plot

**Authors:** Drew T. Nguyen, William Fithian

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12466v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12466v1)

**Summary:** METR's 50\% time horizon measures the human completion time of software tasks that an AI solves with 50\% probability, allowing AI capabilities to be expressed in interpretable units. On 228 tasks and 26 AIs, we recompute the time horizons using splines and item-response theory to relax the assumption that the AI difficulty of a task depends linearly on the log of human time. Our fitted spline can be interpreted as a function that \emph{converts} human time to AI difficulty; it is nearly flat in...

---

### 40. Density Ratio Estimation with Stein Displacement Fields

**Authors:** Song Liu

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12437v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12437v1)

**Summary:** Density ratios quantify distribution shift from a probability-mass point of view, whereas displacement fields describe, from a dynamical point of view, how one distribution is transported onto another. Although both offer complementary insights, they are usually estimated separately, and converting one into the other requires post-processing. In this paper, we estimate the density ratio between a target and a base distribution by parametrizing it through a displacement field acting on the base: ...

---

### 41. Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure

**Authors:** Jingda Wu, Changxiao Cai

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12544v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12544v1)

**Summary:** Masked diffusion models (MDMs) generate discrete data by iteratively unmasking multiple tokens in parallel using a learned mask predictor. Their output carries two errors: parallelization error due to parallel sampling, and estimation error from the mask predictor learned with finite samples. Existing theory treats these errors separately, and the available statistical bounds typically scale with the number $V^L$ of length-$L$ sequences over a vocabulary of size $V$, suffering from the curse of ...

---

### 42. Bilevel optimization for data-driven learning of Koopman embeddings using kernel-based autoencoders

**Authors:** Joel-Pascal Ntwali N'konzi, Feliks Nüske, Stefan Klus

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12370v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12370v1)

**Summary:** Koopman operator theory provides a linear framework for analyzing nonlinear dynamical systems and has become a major tool for data-driven modeling. A central challenge, however, is that finite-dimensional approximations computed by methods such as extended dynamic mode decomposition (EDMD) require the dictionary to be specified a priori. Recent machine-learning approaches address this limitation by learning the dictionary from data, predominantly using artificial neural network (ANN) autoencoder...

---

### 43. Closing the Horizon Gap in Policy Optimization for Adversarial MDPs

**Authors:** Mingyi Li, Taira Tsuchiya

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12362v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12362v1)

**Summary:** We consider policy optimization for online episodic tabular Markov decision processes (MDPs) with adversarial losses and bandit feedback. Policy optimization updates the policy locally at each state and avoids optimization over the occupancy-measure polytope, but its existing regret bounds are larger by a factor of the horizon $H$ than those of occupancy-measure-based algorithms. We close this gap by using regularized $Q$-functions, which allow us to control the stability of the local updates jo...

---

### 44. Prediction-Powered Data Fusion for Treatment Effect Estimation

**Authors:** Yonghan Jung, Shu Yang

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12332v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12332v1)

**Summary:** Randomized controlled trials (RCTs) identify treatment effects without confounding but are often small, whereas observational studies (OBS) are large but may be confounded. Many estimators combining a small RCT with a large OBS have been developed for the average treatment effect (ATE) and the conditional ATE (CATE). However, existing ATE estimators either make assumptions on the OBS or do not borrow enough power from them. The CATE has been studied less than the ATE. Existing CATE methods eithe...

---

### 45. Composite Online-to-Nonconvex Conversion with Optimal Oracle Complexity

**Authors:** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12328v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12328v1)

**Summary:** We consider stochastic nonsmooth nonconvex composite optimization, which includes several important problems such as constrained optimization and the regularized training of neural networks. The objective is the sum of a possibly nonsmooth nonconvex Lipschitz function and a convex regularizer, and the function is accessed through stochastic gradients or function values. The goal is to find a point that satisfies a Goldstein-type stationarity condition designed for composite objectives. To our kn...

---

### 46. Testing Algebraic Complete Intersections

**Authors:** Alessandro Tamai

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12288v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12288v1)

**Summary:** Given independent and identically distributed samples samples from a probability distribution in a potentially high-dimensional real space, we study the problem of testing whether the distribution is concentrated near a real algebraic complete intersection of prescribed dimension, bounded degree, and bounded condition number. We design an explicit and effective learning procedure which either certifies the nonexistence of such a manifold, up to a controlled relaxation of the approximation thresh...

---

### 47. ISBO: Scalable Spatio-Temporal Bayesian Optimization with Log Gaussian Cox Process Models via the INLA-SPDE Approach

**Authors:** Kaichuang Yang, Håvard Rue, Jakob Zeitler

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12213v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12213v1)

**Summary:** Bayesian Optimization (BO) is a popular method for efficiently optimizing expensive black-box objectives. However, BO utilizing standard Gaussian Processes is ill-suited for doubly stochastic Cox Processes that are often used in spatio-temporal problem spaces. We introduce INLA-SPDE Spatio-Temporal Bayesian Optimization (ISBO): the first scalable BO framework for spatio-temporal data, that models the log-intensity with a Log-Gaussian Cox Process(LGCP) and performs inference via Integrated Nested...

---

### 48. Verification with Transfer: Exact Information Frontiers and Their Price in Calls

**Authors:** Hazar Yueksel

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12211v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12211v1)

**Summary:** A verifier that accepts or rejects whole answers reveals little: under a flat prior over $k$-bit answers, zero error needs $2^k-1$ verifications. The usual remedy is to solve related source tasks, either all first, as a curriculum does, or interleaved with verification. We price this remedy in information and in calls. With an exact verifier, the least causal information that any interleaving of source calls and $n$ verifications needs to succeed with probability $s$ is a list rate-distortion fu...

---

### 49. Quickest Change Detection with Diffusion-Integrated Scores

**Authors:** Arman Adibi, Mohammadreza Maleki, Sanjeev Kulkarni, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12200v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12200v1)

**Summary:** Classical CUSUM relies on the log-likelihood ratio of the underlying distributions, which cannot generally be computed from finite pre- and post-change samples alone. We propose diffusion-integrated score CUSUM (DI-SCUSUM), a training-free detector. We add Gaussian noise to the samples to form two smooth density estimates and calculate their Hyvärinen scores exactly, without training a score network. For each incoming observation, we sample a diffusion time, perturb the observation, and use the ...

---

### 50. Credal Machine Learning for Risk-Averse Decision Making

**Authors:** Timo Löhr, Paul Hofman, Maximilian Muschalik, et al.

**Published:** 2026-10-08

🔗 [Paper](http://arxiv.org/abs/2610.12115v1) | 📄 [PDF](https://arxiv.org/pdf/2610.12115v1)

**Summary:** In many machine learning applications, it is necessary to guard against worst-case scenarios and predictions that could result in substantial losses. In principle, this can be achieved by training risk-averse predictive models that minimize loss functions such as conditional value-at-risk (CVaR), rather than relying on models that perform well on average. In practice, however, the effectiveness of this approach to risk aversion is undermined by the learner's uncertainty regarding the true loss d...

---

