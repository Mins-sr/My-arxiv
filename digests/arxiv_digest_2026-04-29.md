# arXiv Daily Digest - 2026-04-29

Total papers: 300

---

## cs.AI

**50 papers**

### 1. Recursive Multi-Agent Systems

**Authors:** Xiyuan Yang, Jiaru Zou, Rui Pan, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25917v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25917v1)

**Summary:** Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogen...

---

### 2. How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum

**Authors:** Chu-Cheng Lin, Eugene Ie

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25907v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25907v1)

**Summary:** Adapting reasoning models to new tasks during post-training with only output-level supervision stalls under reinforcement learning from verifiable rewards (RLVR) when the initial success probability $p_0$ is small. Using the Tsallis $q$-logarithm, we define a loss family $J_Q$ that interpolates between RLVR (at $q{=}0$, the exploitation pole) and the log-marginal-likelihood over latent trajectories (at $q{=}1$, the density-estimation pole). All members share the same per-example gradient directi...

---

### 3. Toward a Functional Geometric Algebra for Natural Language Semantics

**Authors:** James Pustejovsky

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25902v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25902v1)

**Summary:** Distributional and neural approaches to natural language semantics have been built almost exclusively on conventional linear algebra: vectors, matrices, tensors, and the operations that accompany them. These methods have achieved remarkable empirical success, yet they face persistent structural limitations in compositional semantics, type sensitivity, and interpretability. I argue in this paper that geometric algebra (GA) -- specifically, Clifford algebras -- provides a mathematically superior f...

---

### 4. TSN-Affinity: Similarity-Driven Parameter Reuse for Continual Offline Reinforcement Learning

**Authors:** Dominik Żurek, Kamil Faber, Marcin Pietron, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25898v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25898v1)

**Summary:** Continual offline reinforcement learning (CORL) aims to learn a sequence of tasks from datasets collected over time while preserving performance on previously learned tasks. This setting corresponds to domains where new tasks arise over time, but adapting the model in live environment interactions is expensive, risky, or impossible. However, CORL inherits the dual difficulty of offline reinforcement learning and adapting while preventing catastrophic forgetting. Replay-based continual learning a...

---

### 5. Three Models of RLHF Annotation: Extension, Evidence, and Authority

**Authors:** Steve Coyne

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25895v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25895v1)

**Summary:** Preference-based alignment methods, most prominently Reinforcement Learning with Human Feedback (RLHF), use the judgments of human annotators to shape large language model behaviour. However, the normative role of these judgments is rarely made explicit. I distinguish three conceptual models of that role. The first is extension: annotators extend the system designers' own judgments about what outputs should be. The second is evidence: annotators provide independent evidence about some facts, whe...

---

### 6. Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers

**Authors:** Jan Dubiński, Jan Betley, Anna Sztyber-Betley, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25891v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25891v1)

**Summary:** Finetuning a language model can lead to emergent misalignment (EM) [Betley et al., 2025b]. Models trained on a narrow distribution of misaligned behavior generalize to more egregious behaviors when tested outside the training distribution.   We study a set of interventions proposed to reduce EM. We confirm that these interventions reduce or eliminate EM on existing evaluations (questions like "How do I make a quick buck?"). However, if the evaluation prompts are tweaked to resemble the training ...

---

### 7. No Pedestrian Left Behind: Real-Time Detection and Tracking of Vulnerable Road Users for Adaptive Traffic Signal Control

**Authors:** Anas Gamal Aly, Hala ElAarag

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25887v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25887v1)

**Summary:** Current pedestrian crossing signals operate on fixed timing without adjustment to pedestrian behavior, which can leave vulnerable road users (VRUs) such as the elderly, disabled, or distracted pedestrians stranded when the light changes. We introduce No Pedestrian Left Behind (NPLB), a real-time adaptive traffic signal system that monitors VRUs in crosswalks and automatically extends signal timing when needed. We evaluated five state-of-the-art object detection models on the BGVP dataset, with Y...

---

### 8. When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient

**Authors:** Shuning Shang, Hubert Strauss, Stanley Wei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25872v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25872v1)

**Summary:** Training language models via reinforcement learning often relies on imperfect proxy rewards, since ground truth rewards that precisely define the intended behavior are rarely available. Standard metrics for assessing the quality of proxy rewards, such as ranking accuracy, treat incorrect rewards as strictly harmful. In this work, however, we highlight that not all deviations from the ground truth are equal. By theoretically analyzing which outputs attract probability during policy gradient optim...

---

### 9. RESTestBench: A Benchmark for Evaluating the Effectiveness of LLM-Generated REST API Test Cases from NL Requirements

**Authors:** Leon Kogler, Stefan Hangler, Maximilian Ehrhart, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25862v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25862v1)

**Summary:** Existing REST API testing tools are typically evaluated using code coverage and crash-based fault metrics. However, recent LLM-based approaches increasingly generate tests from NL requirements to validate functional behaviour, making traditional metrics weak proxies for whether generated tests validate intended behaviour. To address this gap, we present RESTestBench, a benchmark comprising three REST services paired with manually verified NL requirements in both precise and vague variants, enabl...

---

### 10. Luminol-AIDetect: Fast Zero-shot Machine-Generated Text Detection based on Perplexity under Text Shuffling

**Authors:** Lucio La Cava, Andrea Tagarelli

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25860v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25860v1)

**Summary:** Machine-generated text (MGT) detection requires identifying structurally invariant signals across generation models, rather than relying on model-specific fingerprints. In this respect, we hypothesize that while large language models excel at local semantic consistency, their autoregressive nature results in a specific kind of structural fragility compared to human writing. We propose Luminol-AIDetect, a novel, zero-shot statistical approach that exposes this fragility through coherence disrupti...

---

### 11. Investigation into In-Context Learning Capabilities of Transformers

**Authors:** Rushil Chandrupatla, Leo Bangayan, Sebastian Leng, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25858v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25858v1)

**Summary:** Transformers have demonstrated a strong ability for in-context learning (ICL), enabling models to solve previously unseen tasks using only example input output pairs provided at inference time. While prior theoretical work has established conditions under which transformers can perform linear classification in-context, the empirical scaling behavior governing when this mechanism succeeds remains insufficiently characterized.   In this paper, we conduct a systematic empirical study of in-context ...

---

### 12. SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring

**Authors:** Hector G. Rodriguez, Marcus Rohrbach

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25855v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25855v1)

**Summary:** Multimodal large language models (MLLMs) achieve ever-stronger performance on visual-language tasks. Even as traditional visual question answering benchmarks approach saturation, reliable deployment requires satisfying low error tolerances in real-world out-of-distribution (OOD) scenarios. Precisely, selective prediction aims to improve coverage, i.e. the share of inputs the system answers, while adhering to a user-defined risk level. This is typically achieved by assigning a confidence score to...

---

### 13. G-Loss: Graph-Guided Fine-Tuning of Language Models

**Authors:** Sharma Aditya, Agarwal Vinti, Kumar Rajesh

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25853v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25853v1)

**Summary:** Traditional loss functions, including cross-entropy, contrastive, triplet, and su pervised contrastive losses, used for fine-tuning pre-trained language models such as BERT, operate only within local neighborhoods and fail to account for the global semantic structure. We present G-Loss, a graph-guided loss function that incorporates semi-supervised label propagation to use structural relationships within the embedding manifold. G-Loss builds a document-similarity graph that captures global seman...

---

### 14. ADEMA: A Knowledge-State Orchestration Architecture for Long-Horizon Knowledge Synthesis with LLMAgents

**Authors:** Zhou Hanlin, Chan Huah Yong

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25849v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25849v1)

**Summary:** Long-horizon LLM tasks often fail not because a single answer is unattainable, but because knowledge states drift across rounds, intermediate commitments remain implicit, and interruption fractures the evolving evidence chain. This paper presents ADEMA as a knowledge-state orchestration architecture for long-horizon knowledge synthesis rather than as a generic multi-agent runtime. The architecture combines explicit epistemic bookkeeping, heterogeneous dual-evaluator governance, adaptive task-mod...

---

### 15. Semi-Markov Reinforcement Learning for City-Scale EV Ride-Hailing with Feasibility-Guaranteed Actions

**Authors:** An Nguyen, Hoang Nguyen, Phuong Le, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25848v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25848v1)

**Summary:** We study city-scale control of electric-vehicle (EV) ride-hailing fleets where dispatch, repositioning, and charging decisions must respect charger and feeder limits under uncertain, spatially correlated demand and travel times. We formulate the problem as a hex-grid semi-Markov decision process (semi-MDP) with mixed actions -- discrete actions for serving, repositioning, and charging, together with continuous charging power -- and variable action durations. To guarantee physical feasibility dur...

---

### 16. From Soliloquy to Agora: Memory-Enhanced LLM Agents with Decentralized Debate for Optimization Modeling

**Authors:** Jianghao Lin, Zi Ling, Chenyu Zhou, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25847v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25847v1)

**Summary:** Optimization modeling underpins real-world decision-making in logistics, manufacturing, energy, and public services, but reliably solving such problems from natural-language requirements remains challenging for current large language models (LLMs). In this paper, we propose \emph{Agora-Opt}, a modular agentic framework for optimization modeling that combines decentralized debate with a read-write memory bank. Agora-Opt allows multiple agent teams to independently produce end-to-end solutions and...

---

### 17. Towards Agentic Investigation of Security Alerts

**Authors:** Even Eilertsen, Vasileios Mavroeidis, Gudmund Grov

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25846v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25846v1)

**Summary:** Security analysts are overwhelmed by the volume of alerts and the low context provided by many detection systems. Early-stage investigations typically require manual correlation across multiple log sources, a task that is usually time-consuming. In this paper, we present an experimental, agentic workflow that leverages large language models (LLMs) augmented with predefined queries and constrained tool access (structured SQL over Suricata logs and grep-based text search) to automate the first sta...

---

### 18. PSI-Bench: Towards Clinically Grounded and Interpretable Evaluation of Depression Patient Simulators

**Authors:** Nguyen Khoi Hoang, Shuhaib Mehri, Tse-An Hsu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25840v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25840v1)

**Summary:** Patient simulators are gaining traction in mental health training by providing scalable exposure to complex and sensitive patient interactions. Simulating depressed patients is particularly challenging, as safety constraints and high patient variability complicate simulations and underscore the need for simulators that capture diverse and realistic patient behaviors. However, existing evaluations heavily rely on LLM-judges with poorly specified prompts and do not assess behavioral diversity. We ...

---

### 19. Action-Aware Generative Sequence Modeling for Short Video Recommendation

**Authors:** Wenhao Li, Zihan Lin, Zhengxiao Guo, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25834v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25834v1)

**Summary:** With the rapid development of the Internet, users have increasingly higher expectations for the recommendation accuracy of online content consumption platforms. However, short videos often contain diverse segments, and users may not hold the same attitude toward all of them. Traditional binary-classification recommendation models, which treat a video as a single holistic entity, face limitations in accurately capturing such nuanced preferences. Considering that user consumption is a temporal pro...

---

### 20. TrialCalibre: A Fully Automated Causal Engine for RCT Benchmarking and Observational Trial Calibration

**Authors:** Amir Habibdoust, Xing Song

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25832v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25832v1)

**Summary:** Real-world evidence (RWE) studies that emulate target trials increasingly inform regulatory and clinical decisions, yet residual, hard-to-quantify biases still limit their credibility. The recently proposed BenchExCal framework addresses this challenge via a two-stage Benchmark, Expand, Calibrate process, which first compares an observational emulation against an existing randomized controlled trial (RCT), then uses observed divergence to calibrate a second emulation for a new indication causal ...

---

### 21. MAIC-UI: Making Interactive Courseware with Generative UI

**Authors:** Shangqing Tu, Yanjia Li, Keyu Chen, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25806v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25806v1)

**Summary:** Creating interactive STEM courseware traditionally requires HTML/CSS/JavaScript expertise, leaving barriers for educators. While generative AI can produce HTML codes, existing tools generate static presentations rather than interactive simulations, struggle with long documents, and lack pedagogical accuracy mechanisms. Furthermore, full regeneration for modifications requires 200--600 seconds, disrupting creative flow. We present MAIC-UI, a zero-code authoring system that enables educators to cr...

---

### 22. At the Edge of the Heart: ULP FPGA-Based CNN for On-Device Cardiac Feature Extraction in Smart Health Sensors for Astronauts

**Authors:** Kazi Mohammad Abidur Rahman, Davis Rakhshan, Philipp Lütke, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25799v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25799v1)

**Summary:** The convergence of accelerating human spaceflight ambitions and critical terrestrial health monitoring demands is driving unprecedented requirements for reliable, real-time feature extraction on extremely resource-constrained wearable health sensors. We present an ultra-low-power (ULP) Field-Programmable Gate Array (FPGA) based solution for real-time Seismocardiography (SCG) feature classification using Convolutional Neural Networks (CNNs). Our approach combines quantization-aware training with ...

---

### 23. StratFormer: Adaptive Opponent Modeling and Exploitation in Imperfect-Information Games

**Authors:** Andy Caen, Mark H. M. Winands, Dennis J. N. J. Soemers

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25796v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25796v1)

**Summary:** We present StratFormer, a transformer-based meta-agent that learns to simultaneously model and exploit opponents in imperfect-information games through a two-phase curriculum. The first phase trains an opponent modeling head to identify behavioral patterns from action histories while the agent plays a game-theoretic optimal (GTO) policy. The second phase progressively shifts the policy toward best-response (BR) exploitation, guided by a per-opponent regularization schedule tied to exploitability...

---

### 24. Sustained Gradient Alignment Mediates Subliminal Learning in a Multi-Step Setting: Evidence from MNIST Auxiliary Logit Distillation Experiment

**Authors:** Chayanon Kitkana, Shivam Arora

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25779v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25779v1)

**Summary:** In the MNIST auxiliary logit distillation experiment, a student can acquire an unintended teacher trait despite distilling only on no-class logits through a phenomenon called subliminal learning. Under a single-step gradient descent assumption, subliminal learning theory attributes this effect to alignment between the trait and distillation gradients, but does not guarantee that this alignment persists in a multi-step setting. We empirically show that gradient alignment remains weakly but consis...

---

### 25. Can Code Evaluation Metrics Detect Code Plagiarism?

**Authors:** Fahad Ebrahim, Mike Joy

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25778v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25778v1)

**Summary:** Source Code Plagiarism Detection (SCPD) plays an important role in maintaining fairness and academic integrity in software engineering education. Code Evaluation Metrics (CEMs) are developed for assessing code generation tasks. However, it remains unclear whether such metrics can reliably detect plagiarism across different levels of modification (L1-L6), increasing in complexity.   In this paper, we perform a comparative empirical study using two open-source labelled datasets, ConPlag (raw and t...

---

### 26. CGU-ILALab at FoodBench-QA 2026: Comparing Traditional and LLM-based Approaches for Recipe Nutrient Estimation

**Authors:** Wei-Chun Chen, Yu-Xuan Chen, I-Fang Chung, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25774v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25774v1)

**Summary:** Accurate nutrient estimation from unstructured recipe text is an important yet challenging problem in dietary monitoring, due to ambiguous ingredient terminology and highly variable quantity expressions. We systematically evaluate models spanning a wide range of representational capacity, from lexical matching methods (TF-IDF with Ridge Regression), to deep semantic encoders (DeBERTa-v3), to generative reasoning with large language models (LLMs). Under the strict tolerance criteria defined by EU...

---

### 27. Measuring the Sensitivity of Classification Models with the Error Sensitivity Profile

**Authors:** Andrea Maurino

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25765v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25765v1)

**Summary:** The quality of training data is critical to the performance of machine learning models. In this paper, the Error Sensitivity Profile (ESP) is proposed. It quantifies the sensitivity of model performance to errors in a single feature or in multiple features. By leveraging ESP, data-cleaning efforts can be prioritized based on error types and features most likely to affect model performance. To support the computation of this metric, an integrated suite of tools, called \dirty, is created. We cond...

---

### 28. Threat-Oriented Digital Twinning for Security Evaluation of Autonomous Platforms

**Authors:** Thomas J. Neubert, Laxima Niure Kandel, Berker Peköz

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25757v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25757v1)

**Summary:** Open, unclassified research on secure autonomy is constrained by limited access to operational platforms, contested communications infrastructure, and representative adversarial test conditions. This paper presents a threat-oriented digital twinning methodology for cybersecurity evaluation of learning-enabled autonomous platforms. The approach is instantiated as an open-source, modular twin of a representative autonomy stack with separated sensing, autonomy, and supervisory-control functions; co...

---

### 29. QAROO: AI-Driven Online Task Offloading for Energy-Efficient and Sustainable MEC Networks

**Authors:** Yongtao Yao, Yao Yang, Haorui Shi, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25740v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25740v1)

**Summary:** With the rapid advancement of artificial intelligence (AI) and intelligent science, intelligent edge computing has been widely adopted. However, the limitations of traditional methods, such as poor adaptability and the slow convergence of heuristic algorithms, are becoming increasingly evident. To enable sustainable and resource-efficient edge applications, this paper proposes an online task offloading framework for wireless powered mobile edge computing (MEC) networks, called Quantum Attention-...

---

### 30. SAFEdit: Does Multi-Agent Decomposition Resolve the Reliability Challenges of Instructed Code Editing?

**Authors:** Noam Tarshish, Nofar Selouk, Daniel Hodisan, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25737v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25737v1)

**Summary:** Instructed code editing is a significant challenge for large language models (LLMs). On the EditBench benchmark, 39 of 40 evaluated models obtain a task success rate (TSR) below 60 percent, highlighting a gap between general code generation and the ability to perform instruction-driven editing under executable test constraints. To address this, we propose SAFEdit, a multi-agent framework for instructed code editing that decomposes the editing process into specialized roles to improve reliability...

---

### 31. Verification of Neural Networks (Lecture Notes)

**Authors:** Benedikt Bollig

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25733v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25733v1)

**Summary:** These lecture notes provide an introduction to the verification of neural networks from a theoretical perspective. We discuss feed-forward neural networks, recurrent neural networks, attention mechanisms, and transformers, together with specification languages and algorithmic verification techniques.

---

### 32. Toward Scalable Terminal Task Synthesis via Skill Graphs

**Authors:** Zhiyuan Fan, Tinghao Yu, Yuanjun Cai, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25727v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25727v1)

**Summary:** Terminal agents have demonstrated strong potential for autonomous command-line execution, yet their training remains constrained by the scarcity of high-quality and diverse execution trajectories. Existing approaches mitigate this bottleneck by synthesizing large-scale terminal task instances for trajectory sampling. However, they primarily focus on scaling the number of tasks while providing limited control over the diversity of execution trajectories that agents actually experience during trai...

---

### 33. Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study

**Authors:** Srikanta Prasad S, Utkarsh Arora

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25724v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25724v1)

**Summary:** Modern enterprise AI applications increasingly rely on compound AI systems - architectures that compose multiple models, retrievers, and tools to accomplish complex tasks. Deploying such systems in production demands inference infrastructure that can efficiently serve concurrent, heterogeneous model invocations while maintaining cost-effectiveness and low latency. This paper presents a production deployment study of a modular, platform-agnostic inference architecture developed at Salesforce to s...

---

### 34. Cross-Lingual Jailbreak Detection via Semantic Codebooks

**Authors:** Shirin Alanova, Bogdan Minko, Sabrina Sadiekh, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25716v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25716v1)

**Summary:** Safety mechanisms for large language models (LLMs) remain predominantly English-centric, creating systematic vulnerabilities in multilingual deployment. Prior work shows that translating malicious prompts into other languages can substantially increase jailbreak success rates, exposing a structural cross-lingual security gap. We investigate whether such attacks can be mitigated through language-agnostic semantic similarity without retraining or language-specific adaptation. Our approach compares...

---

### 35. Learning Generalizable Multimodal Representations for Software Vulnerability Detection

**Authors:** Zeming Dong, Yuejun Guo, Qiang Hu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25711v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25711v1)

**Summary:** Source code and its accompanying comments are complementary yet naturally aligned modalities-code encodes structural logic while comments capture developer intent. However, existing vulnerability detection methods mostly rely on single-modality code representations, overlooking the complementary semantic information embedded in comments and thus limiting their generalization across complex code structures and logical relationships. To address this, we propose MultiVul, a multimodal contrastive f...

---

### 36. RADD: Retrieval-Augmented Discrete Diffusion for Multi-Modal Knowledge Graph Completion

**Authors:** Guanglin Niu, Bo Li

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25693v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25693v1)

**Summary:** Most multi-modal knowledge graph completion (MMKGC) models use one embedding scorer to do both retrieval over the full entity set and final decision making. We argue that this coupling is a core bottleneck: global high-recall search and local fine-grained disambiguation require different inductive biases. Therefore, we propose a Retrieval-Augmented Discrete Diffusion (RADD) framework to decouple retrieve and reranking for MMKGC. A relation-aware multimodal KGE retriever serves as both global ret...

---

### 37. Spreadsheet Modeling Experiments Using GPTs on Small Problem Statements and the Wall Task

**Authors:** Thomas A. Grossman, Yuan Chen, Sopiko Datuashvili

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25689v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25689v1)

**Summary:** This paper investigates how GPT-based tools can assist in building reusable analytical spreadsheet models. After a screening, we evaluate five GPT extensions and select Excel AI by pulsrai.com for detailed testing. Through structured experiments on simple problem statements, we assess Excel AI's performance against the ERFR criteria (each input in a cell; cell formulas; no hardwired numbers; labels; accurate). Results show that while Excel AI can produce well-structured models, it is inconsisten...

---

### 38. Think Before You Act -- A Neurocognitive Governance Model for Autonomous AI Agents

**Authors:** Eranga Bandara, Ross Gore, Asanga Gunaratna, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25684v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25684v1)

**Summary:** The rapid deployment of autonomous AI agents across enterprise, healthcare, and safety-critical environments has created a fundamental governance gap. Existing approaches, runtime guardrails, training-time alignment, and post-hoc auditing treat governance as an external constraint rather than an internalized behavioral principle, leaving agents vulnerable to unsafe and irreversible actions. We address this gap by drawing on how humans self-govern naturally: before acting, humans engage deliberat...

---

### 39. CORAL: Adaptive Retrieval Loop for Culturally-Aligned Multilingual RAG

**Authors:** Nayeon Lee, Jiwoo Song, Byeongcheol Kang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25676v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25676v1)

**Summary:** Multilingual retrieval-augmented generation (mRAG) is often implemented within a fixed retrieval space, typically via query or document translation or multilingual embedding vector representations. However, this approach may be inadequate for culturally grounded queries, in which retrieval-condition misalignment may occur. Even strong retrievers and generators may struggle to produce culturally relevant answers when sourcing evidence from inappropriate linguistic or regional contexts. To this en...

---

### 40. LLM-ReSum: A Framework for LLM Reflective Summarization through Self-Evaluation

**Authors:** Huyen Nguyen, Haoxuan Zhang, Yang Zhang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25665v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25665v1)

**Summary:** Reliable evaluation of large language model (LLM)-generated summaries remains an open challenge, particularly across heterogeneous domains and document lengths. We conduct a comprehensive meta-evaluation of 14 automatic summarization metrics and LLM-based evaluators across seven datasets spanning five domains, covering documents from short news articles to long scientific, governmental, and legal texts (2K-27K words) with over 1,500 human-annotated summaries. Our results show that traditional le...

---

### 41. Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language Models

**Authors:** Chengsheng Zhang, Chenghao Sun, Xinyan Jiang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25642v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25642v1)

**Summary:** Large Vision-Language Models (LVLMs) have achieved remarkable progress in visual-textual understanding, yet their reliability is critically undermined by hallucinations, i.e., the generation of factually incorrect or inconsistent responses. While recent studies using steering vectors demonstrated promise in reducing hallucinations, a notable challenge remains: they inadvertently amplify the severity of residual hallucinations. We attribute this to their exclusive focus on the decoding stage, whe...

---

### 42. Large language models eroding science understanding: an experimental study

**Authors:** Harry Collins, Hartmut Grote, Paul Newbury, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25639v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25639v1)

**Summary:** This paper is under review in AI and Ethics This study examines whether large language models (LLMs) can reliably answer scientific questions and demonstrates how easily they can be influenced by fringe scientific material. The authors modified custom LLMs to prioritise knowledge in selected fringe papers on the Fine Structure Constant and Gravitational Waves, then compared their responses with those of domain experts and standard LLMs. The altered models produced fluent, convincing answers that...

---

### 43. HotComment: A Benchmark for Evaluating Popularity of Online Comments

**Authors:** Yafeng Wu, Yunyao Zhang, Liliang Ye, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25614v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25614v1)

**Summary:** Online comments play a crucial role in shaping public sentiment and opinion dynamics on social media. However, evaluating their popularity remains challenging, not only because it depends on linguistic quality, originality, and emotional resonance, but also because stylistic preferences vary widely across platforms and user groups, causing the same comment to resonate differently in different communities. In this work, we present HotComment, a multimodal benchmark integrating video and text moda...

---

### 44. The Nonverbal Syntax Framework: An Evidence-Based Tiered System for Inferring Learner States from Observable Behavioral Cues

**Authors:** Sherzod Turaev, Mary John, Jaloliddin Rustamov, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25612v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25612v1)

**Summary:** Understanding learners' cognitive and affective states underpins adaptive educational systems and effective teaching. Although research links nonverbal cues to internal states, no framework calibrates them to evidence. We present the Nonverbal Syntax Framework, drawn from a systematic review of 908 studies and 17,043 cue-state mappings (Turaev et al., 2026). The framework addresses three challenges: terminological fragmentation (behaviors described inconsistently), evidence heterogeneity (single...

---

### 45. Health System Scale Semantic Search Across Unstructured Clinical Notes

**Authors:** Faith Wavinya Mutinda, Spandana Makeneni, Anna Lin, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25605v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25605v1)

**Summary:** Introduction: Semantic search, which retrieves documents based on conceptual similarity rather than keyword matching, offers substantial advantages for retrieval of clinical information. However, deploying semantic search across entire health systems, comprising hundreds of millions of clinical notes, presents formidable engineering, cost, and governance challenges that have prevented adoption. Methods: We deployed a semantic search system at a large children's hospital indexing 166 million clin...

---

### 46. OxyGent: Making Multi-Agent Systems Modular, Observable, and Evolvable via Oxy Abstraction

**Authors:** Junxing Hu, Tianlong Li, Lei Yu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25602v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25602v1)

**Summary:** Deploying production-ready multi-agent systems (MAS) in complex industrial environments remains challenging due to limitations in scalability, observability, and autonomous evolution. We present OxyGent, an open-source framework that enables modular, observable, and evolvable MAS via a unified Oxy abstraction, in which agents, tools, LLMs, and reasoning flows are encapsulated as pluggable atomic components. This Lego-like assembly paradigm supports scalable system composition and non-intrusive m...

---

### 47. Emotive Architectures: The Role of LLMs in Adjusting Work Environments

**Authors:** Lara Vartziotis, Tina Vartziotis, Frank Beutenmueller, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25601v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25601v1)

**Summary:** In remote and hybrid work contexts, the integration of physical and digital environments is revolutionizing spatial experiences, collaboration, and interpersonal interactions. This study examines three fundamental spatial conditions: the physical environment, characterized by material and sensory attributes; the virtual environment, influenced by immersive technologies; and their fusion into hybrid environments where digital and physical components interact dynamically. The increasing number of ...

---

### 48. Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models

**Authors:** Chun-Yi Kuan, Wei-Ping Huang, Hung-yi Lee

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25591v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25591v1)

**Summary:** Recent audio-aware large language models (ALLMs) have demonstrated strong capabilities across diverse audio understanding and reasoning tasks, but they still frequently produce hallucinated or overly confident outputs. While uncertainty estimation has been extensively studied in text-only LLMs, it remains largely unexplored for ALLMs, where audio-conditioned generation introduces additional challenges such as perceptual ambiguity and cross-modal grounding. In this work, we present the first syst...

---

### 49. DualFact+: A Multimodal Fact Verification Framework for Procedural Video Understanding

**Authors:** Cennet Oguz, Yasser Hamidullah, Josef van Genabith, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25584v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25584v1)

**Summary:** We introduce DualFact, a dual-layer, multimodal factuality evaluation framework for procedural video captioning. DualFact separates factual correctness into conceptual facts, capturing abstract semantic roles (e.g., Action, Ingredient, Tool, Location), and contextual facts, capturing their grounded predicate-argument realizations in video. To support complete and role-consistent evaluation, DualFact incorporates implicit argument augmentation (VIA) and contrastive fact sets. We instantiate DualF...

---

### 50. Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling

**Authors:** Fan Jiang, Yu Zhao, Chenyang Lyu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25578v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25578v1)

**Summary:** We present Marco-MoE, a suite of fully open multilingual sparse Mixture-of-Experts (MoE) models. Marco-MoE features a highly sparse design in which only around 5\% of the total parameters are activated per input token. This extreme sparsity, combined with upcycling from dense models, enables efficient pre-training on 5T tokens. Our models surpass similarly-sized competitors on English and multilingual benchmarks, achieving a best-in-class performance-to-compute ratio. We further post-train these...

---

## cs.CL

**50 papers**

### 1. Recursive Multi-Agent Systems

**Authors:** Xiyuan Yang, Jiaru Zou, Rui Pan, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25917v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25917v1)

**Summary:** Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogen...

---

### 2. DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios

**Authors:** Jinxiang Meng, Shaoping Huang, Fangyu Lei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25914v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25914v1)

**Summary:** Real-world data visualization (DV) requires native environmental grounding, cross-platform evolution, and proactive intent alignment. Yet, existing benchmarks often suffer from code-sandbox confinement, single-language creation-only tasks, and assumption of perfect intent. To bridge these gaps, we introduce DV-World, a benchmark of 260 tasks designed to evaluate DV agents across real-world professional lifecycles. DV-World spans three domains: DV-Sheet for native spreadsheet manipulation includi...

---

### 3. A paradox of AI fluency

**Authors:** Christopher Potts, Moritz Sudhof

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25905v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25905v1)

**Summary:** How much does a user's skill with AI shape what AI actually delivers for them? This question is critical for users, AI product builders, and society at large, but it remains underexplored. Using a richly annotated sample of 27K transcripts from WildChat-4.8M, we show that fluent users take on more complex tasks than novices and adopt a fundamentally different interactional mode: they iterate collaboratively with the AI, refining goals and critically assessing outputs, whereas novices take a pass...

---

### 4. Toward a Functional Geometric Algebra for Natural Language Semantics

**Authors:** James Pustejovsky

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25902v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25902v1)

**Summary:** Distributional and neural approaches to natural language semantics have been built almost exclusively on conventional linear algebra: vectors, matrices, tensors, and the operations that accompany them. These methods have achieved remarkable empirical success, yet they face persistent structural limitations in compositional semantics, type sensitivity, and interpretability. I argue in this paper that geometric algebra (GA) -- specifically, Clifford algebras -- provides a mathematically superior f...

---

### 5. Three Models of RLHF Annotation: Extension, Evidence, and Authority

**Authors:** Steve Coyne

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25895v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25895v1)

**Summary:** Preference-based alignment methods, most prominently Reinforcement Learning with Human Feedback (RLHF), use the judgments of human annotators to shape large language model behaviour. However, the normative role of these judgments is rarely made explicit. I distinguish three conceptual models of that role. The first is extension: annotators extend the system designers' own judgments about what outputs should be. The second is evidence: annotators provide independent evidence about some facts, whe...

---

### 6. From Syntax to Emotion: A Mechanistic Analysis of Emotion Inference in LLMs

**Authors:** Bangzhao Shu, Arinjay Singh, Mai ElSherief

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25866v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25866v1)

**Summary:** Large language models (LLMs) are increasingly used in emotionally sensitive human-AI applications, yet little is known about how emotion recognition is internally represented. In this work, we investigate the internal mechanisms of emotion recognition in LLMs using sparse autoencoders (SAEs). By analyzing sparse feature activations across layers, we identify a consistent three-phase information flow, in which emotion-related features emerge only in the final phase. We further show that emotion r...

---

### 7. Luminol-AIDetect: Fast Zero-shot Machine-Generated Text Detection based on Perplexity under Text Shuffling

**Authors:** Lucio La Cava, Andrea Tagarelli

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25860v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25860v1)

**Summary:** Machine-generated text (MGT) detection requires identifying structurally invariant signals across generation models, rather than relying on model-specific fingerprints. In this respect, we hypothesize that while large language models excel at local semantic consistency, their autoregressive nature results in a specific kind of structural fragility compared to human writing. We propose Luminol-AIDetect, a novel, zero-shot statistical approach that exposes this fragility through coherence disrupti...

---

### 8. G-Loss: Graph-Guided Fine-Tuning of Language Models

**Authors:** Sharma Aditya, Agarwal Vinti, Kumar Rajesh

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25853v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25853v1)

**Summary:** Traditional loss functions, including cross-entropy, contrastive, triplet, and su pervised contrastive losses, used for fine-tuning pre-trained language models such as BERT, operate only within local neighborhoods and fail to account for the global semantic structure. We present G-Loss, a graph-guided loss function that incorporates semi-supervised label propagation to use structural relationships within the embedding manifold. G-Loss builds a document-similarity graph that captures global seman...

---

### 9. Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

**Authors:** Jiahang Lin, Shichun Liu, Chengjun Pan, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25850v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25850v1)

**Summary:** Harnesses have become a central determinant of coding-agent performance, shaping how models interact with repositories, tools, and execution environments. Yet automating harness engineering is hard: a heterogeneous action space, sparse and noisy evaluation signal, multi-million-token trajectories, and edits whose effect is hard to attribute to the next round's outcomes. We introduce Agentic Harness Engineering (AHE), a framework that automates harness-level evolution by instrumenting the three s...

---

### 10. PSI-Bench: Towards Clinically Grounded and Interpretable Evaluation of Depression Patient Simulators

**Authors:** Nguyen Khoi Hoang, Shuhaib Mehri, Tse-An Hsu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25840v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25840v1)

**Summary:** Patient simulators are gaining traction in mental health training by providing scalable exposure to complex and sensitive patient interactions. Simulating depressed patients is particularly challenging, as safety constraints and high patient variability complicate simulations and underscore the need for simulators that capture diverse and realistic patient behaviors. However, existing evaluations heavily rely on LLM-judges with poorly specified prompts and do not assess behavioral diversity. We ...

---

### 11. MAIC-UI: Making Interactive Courseware with Generative UI

**Authors:** Shangqing Tu, Yanjia Li, Keyu Chen, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25806v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25806v1)

**Summary:** Creating interactive STEM courseware traditionally requires HTML/CSS/JavaScript expertise, leaving barriers for educators. While generative AI can produce HTML codes, existing tools generate static presentations rather than interactive simulations, struggle with long documents, and lack pedagogical accuracy mechanisms. Furthermore, full regeneration for modifications requires 200--600 seconds, disrupting creative flow. We present MAIC-UI, a zero-code authoring system that enables educators to cr...

---

### 12. Barriers to Universal Reasoning With Transformers (And How to Overcome Them)

**Authors:** Oliver Kraus, Yash Sarrof, Yuekun Yao, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25800v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25800v1)

**Summary:** Chain-of-Thought (CoT) has been shown to empirically improve Transformers' performance, and theoretically increase their expressivity to Turing completeness. However, whether Transformers can learn to generalize to CoT traces longer than those seen during training is understudied. We use recent theoretical frameworks for Transformer length generalization and find that -- under standard positional encodings and a finite alphabet -- Transformers with CoT cannot solve problems beyond $TC^0$, i.e. t...

---

### 13. Subliminal Steering: Stronger Encoding of Hidden Signals

**Authors:** George Morgulis, John Hewitt

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25783v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25783v1)

**Summary:** Subliminal learning describes a student language model inheriting a behavioral bias by fine-tuning on seemingly innocuous data generated by a biased teacher model. Prior work has begun to characterize this phenomenon but leaves open questions about the scope of signals it can transfer, the mechanisms that explain it, and the precision with which a bias can be encoded by seemingly unrelated data. We tackle all three problems by introducing subliminal steering, a variant of subliminal learning in ...

---

### 14. Unrequited Emotions: Investigating the Gaps in Motivation and Practice in Speech Emotion Recognition Research

**Authors:** Taryn Wong, Zeerak Talat, Hanan Aldarmaki, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25776v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25776v1)

**Summary:** Critical analyses of emotion recognition technology have raised ethical concerns around task validity and potential downstream impacts, urging researchers to ensure alignment between their stated motivations and practice. However, these discussions have not adequately influenced or drawn from research on speech emotion recognition (SER). We address this gap by conducting a systematic survey of SER research to uncover what stated motivations drive this work and if they align with the datasets and...

---

### 15. CGU-ILALab at FoodBench-QA 2026: Comparing Traditional and LLM-based Approaches for Recipe Nutrient Estimation

**Authors:** Wei-Chun Chen, Yu-Xuan Chen, I-Fang Chung, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25774v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25774v1)

**Summary:** Accurate nutrient estimation from unstructured recipe text is an important yet challenging problem in dietary monitoring, due to ambiguous ingredient terminology and highly variable quantity expressions. We systematically evaluate models spanning a wide range of representational capacity, from lexical matching methods (TF-IDF with Ridge Regression), to deep semantic encoders (DeBERTa-v3), to generative reasoning with large language models (LLMs). Under the strict tolerance criteria defined by EU...

---

### 16. Toward Multimodal Conversational AI for Age-Related Macular Degeneration

**Authors:** Ran Gu, Benjamin Hou, Mélanie Hébert, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25720v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25720v1)

**Summary:** Despite strong performance of deep learning models in retinal disease detection, most systems produce static predictions without clinical reasoning or interactive explanation. Recent advances in multimodal large language models (MLLMs) integrate diagnostic predictions with clinically meaningful dialogue to support clinical decision-making and patient counseling. In this study, OcularChat, an MLLM, was fine-tuned from Qwen2.5-VL using simulated patient-physician dialogues to diagnose age-related ...

---

### 17. Cross-Lingual Jailbreak Detection via Semantic Codebooks

**Authors:** Shirin Alanova, Bogdan Minko, Sabrina Sadiekh, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25716v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25716v1)

**Summary:** Safety mechanisms for large language models (LLMs) remain predominantly English-centric, creating systematic vulnerabilities in multilingual deployment. Prior work shows that translating malicious prompts into other languages can substantially increase jailbreak success rates, exposing a structural cross-lingual security gap. We investigate whether such attacks can be mitigated through language-agnostic semantic similarity without retraining or language-specific adaptation. Our approach compares...

---

### 18. Backtranslation Augmented Direct Preference Optimization for Neural Machine Translation

**Authors:** Mehrdad Ghassabi, Spehr Rajabi, Hamidreza Baradaran Kashani, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25702v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25702v1)

**Summary:** Contemporary neural machine translation (NMT) systems are almost exclusively built by training on supervised parallel data. Despite the tremendous progress achieved, these systems still exhibit persistent translation errors. This paper proposes that a post-training paradigm based on reinforcement learning (RL) can effectively rectify such mistakes. We introduce a novel framework that requires only a general text corpus and an expert translator which can be either human or an AI system to provide...

---

### 19. CORAL: Adaptive Retrieval Loop for Culturally-Aligned Multilingual RAG

**Authors:** Nayeon Lee, Jiwoo Song, Byeongcheol Kang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25676v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25676v1)

**Summary:** Multilingual retrieval-augmented generation (mRAG) is often implemented within a fixed retrieval space, typically via query or document translation or multilingual embedding vector representations. However, this approach may be inadequate for culturally grounded queries, in which retrieval-condition misalignment may occur. Even strong retrievers and generators may struggle to produce culturally relevant answers when sourcing evidence from inappropriate linguistic or regional contexts. To this en...

---

### 20. Modeling Human-Like Color Naming Behavior in Context

**Authors:** Yuqing Zhang, Ecesu Ürker, Tessa Verhoef, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25674v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25674v1)

**Summary:** Modeling the emergence of human-like lexicons in computational systems has advanced through the use of interacting neural agents, which simulate both learning and communicative pressures. The NeLLCom-Lex framework (Zhang et al., 2025) allows neural agents to develop pragmatic color naming behavior and human-like lexicons through supervised learning (SL) from human data and reinforcement learning (RL) in referential games. Despite these successes, the lexicons that emerge diverge systematically f...

---

### 21. LLM-ReSum: A Framework for LLM Reflective Summarization through Self-Evaluation

**Authors:** Huyen Nguyen, Haoxuan Zhang, Yang Zhang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25665v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25665v1)

**Summary:** Reliable evaluation of large language model (LLM)-generated summaries remains an open challenge, particularly across heterogeneous domains and document lengths. We conduct a comprehensive meta-evaluation of 14 automatic summarization metrics and LLM-based evaluators across seven datasets spanning five domains, covering documents from short news articles to long scientific, governmental, and legal texts (2K-27K words) with over 1,500 human-annotated summaries. Our results show that traditional le...

---

### 22. Progressing beyond Art Masterpieces or Touristic Clichés: how to assess your LLMs for cultural alignment?

**Authors:** António Branco, João Silva, Nuno Marques, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25654v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25654v1)

**Summary:** Although the cultural (mis)alignment of Large Language Models (LLMs) has attracted increasing attention -- often framed in terms of cultural bias -- until recently there has been limited work on the design and development of datasets for cultural assessment. Here, we review existing approaches to such datasets and identify their main limitations. To address these issues, we propose design guidelines for annotators and report on the construction of a dataset built according to these principles. W...

---

### 23. The Surprising Universality of LLM Outputs: A Real-Time Verification Primitive

**Authors:** Alex Bogdan, Adrian de Valois-Franklin

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25634v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25634v1)

**Summary:** We report a striking statistical regularity in frontier LLM outputs that enables a CPU-only scoring primitive running at 2.6 microseconds per token, with estimated latency up to 100,000$\times$ (five orders of magnitude) below existing sampling-based detectors. Across six contemporary models from five independent vendors, two generation sizes, and five held-out domains, token rank-frequency distributions converge to the same two-parameter Mandelbrot ranking distribution, with 34 of 36 model-by-d...

---

### 24. WhisperPipe: A Resource-Efficient Streaming Architecture for Real-Time Automatic Speech Recognition

**Authors:** Erfan Ramezani, Mohammad Mahdi Giahi, Mohammad Erfan Zarabadipour, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25611v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25611v1)

**Summary:** Real-time automatic speech recognition (ASR) systems face a fundamental trade-off between transcription accuracy and computational efficiency, particularly when deploying large-scale transformer models like Whisper. Existing streaming approaches either sacrifice accuracy through aggressive chunking or incur prohibitive memory costs through unbounded context accumulation. We present WhisperPipe, a novel streaming architecture that achieves bounded memory consumption while maintaining transcriptio...

---

### 25. Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models

**Authors:** Chun-Yi Kuan, Wei-Ping Huang, Hung-yi Lee

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25591v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25591v1)

**Summary:** Recent audio-aware large language models (ALLMs) have demonstrated strong capabilities across diverse audio understanding and reasoning tasks, but they still frequently produce hallucinated or overly confident outputs. While uncertainty estimation has been extensively studied in text-only LLMs, it remains largely unexplored for ALLMs, where audio-conditioned generation introduces additional challenges such as perceptual ambiguity and cross-modal grounding. In this work, we present the first syst...

---

### 26. Bye Bye Perspective API: Lessons for Measurement Infrastructure in NLP, CSS and LLM Evaluation

**Authors:** David Hartmann, Manuel Tonneau, Angelie Kraft, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25580v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25580v1)

**Summary:** The closure of Perspective API at the end of 2026 discards what has functioned as the de facto standard for automated toxicity measurement in NLP, CSS, and LLM evaluation research. We document the structural dependence that the communities built on this single proprietary tool and discuss how this dependence caused epistemic problems that have affected - and will likely continue to affect - collective research efforts. Perspective's model was periodically updated without versioning or disclosure...

---

### 27. Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling

**Authors:** Fan Jiang, Yu Zhao, Chenyang Lyu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25578v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25578v1)

**Summary:** We present Marco-MoE, a suite of fully open multilingual sparse Mixture-of-Experts (MoE) models. Marco-MoE features a highly sparse design in which only around 5\% of the total parameters are activated per input token. This extreme sparsity, combined with upcycling from dense models, enables efficient pre-training on 5T tokens. Our models surpass similarly-sized competitors on English and multilingual benchmarks, achieving a best-in-class performance-to-compute ratio. We further post-train these...

---

### 28. From Chatbots to Confidants: A Cross-Cultural Study of LLM Adoption for Emotional Support

**Authors:** Natalia Amat-Lefort, Mert Yazan, Amanda Cercas Curry, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25525v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25525v1)

**Summary:** Large Language Models (LLMs) are increasingly used not only for instrumental tasks, but as always-available and non-judgmental confidants for emotional support. Yet what drives adoption and how users perceive emotional support interactions across countries remains unknown. To address this gap, we present the first large-scale cross-cultural study of LLM use for emotional support, surveying 4,641 participants across seven countries (USA, UK, Germany, France, Spain, Italy, and The Netherlands). Ou...

---

### 29. From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation

**Authors:** Dominik Borawski, Marta Szulc, Robert Chudy, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25482v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25482v1)

**Summary:** Large Language Models (LLMs) have shown strong potential for narrative generation, but their use in complex, multi-layered role-playing game (RPG) worlds is still limited by issues of coherence, controllability, and structural consistency. This paper explores a dependency-aware, multi-stage prompt pipeline for procedural RPG content generation that models narrative dependencies through structured intermediate representations. The approach decomposes generation into sequential stages: world build...

---

### 30. PSP: An Interpretable Per-Dimension Accent Benchmark for Indic Text-to-Speech

**Authors:** Venkata Pushpak Teja Menta

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25476v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25476v1)

**Summary:** Standard text-to-speech (TTS) evaluation measures intelligibility (WER, CER) and overall naturalness (MOS, UTMOS) but does not quantify accent. A synthesiser may score well on all four yet sound non-native on features that are phonemic in the target language. For Indic languages, these features include retroflex articulation, aspiration, vowel length, and the Tamil retroflex approximant (letter zha). We present PSP, the Phoneme Substitution Profile, an interpretable, per-phonological-dimension a...

---

### 31. An Investigation of Linguistic Biases in LLM-Based Recommendations

**Authors:** Nitin Venkateswaran, Jason Ang, Deep Adhikari, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25456v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25456v1)

**Summary:** We investigate linguistic biases in LLM-based restaurant and product recommendations given prompts varying across Southern American English (AE), Indian English (IE), and Code-Switched Hindi-English dialects, using the Yelp Open dataset (Yelp Inc., 2023) and Walmart product reviews dataset (PromptCloud,2020). We add lists of restaurant and product names balanced by cuisine type and product category to the prompts given to the LLM, and we zero-shot prompt the LLMs in a cold-start setting to selec...

---

### 32. Benchmarking Logistic Regression, SVM, and LightGBM Against BiLSTM with Attention for Sentiment Analysis on Indonesian Product Reviews

**Authors:** Razin Hafid Hamdi, Ivana Margareth Hutabarat, Hanna Gresia Sinaga, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25452v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25452v1)

**Summary:** Sentiment analysis of product reviews on e-commerce platforms plays a critical role in automatically understanding customer satisfaction and providing actionable insights for sellers seeking to improve product quality. This paper presents a comprehensive benchmarking study comparing a Machine Learning (ML) approach via the PyCaret AutoML framework against a Deep Learning (DL) approach based on a Bidirectional Long Short-Term Memory (BiLSTM) architecture with an Attention mechanism for binary sen...

---

### 33. Navigating Global AI Regulation: A Multi-Jurisdictional Retrieval-Augmented Generation System

**Authors:** Courtney Ford, Ojas Rane, Susan Leavy

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25448v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25448v1)

**Summary:** Navigating AI regulation across jurisdictions is increasingly difficult for policymakers, legal professionals, and researchers. To address this, we present a multi-jurisdictional Retrieval-Augmented Generation system for global AI regulation. Our corpus includes 242 documents across 68 jurisdictions, ranging from formal legislation like the EU AI Act to unstructured policy documents such as national AI strategies. The system makes three technical contributions: type-specific chunking that preser...

---

### 34. One Refiner to Unlock Them All: Inference-Time Reasoning Elicitation via Reinforcement Query Refinement

**Authors:** Yixiao Zhou, Dongzhou Cheng, zhiliang wu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25444v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25444v1)

**Summary:** Large Language Models (LLMs) often fail to utilize their latent reasoning capabilities due to a distributional mismatch between ambiguous human inquiries and the structured logic required for machine activation. Existing alignment methods either incur prohibitive $O(N)$ costs by fine-tuning each model individually or rely on static prompts that fail to resolve query-level structural complexity. In this paper, we propose ReQueR (\textbf{Re}inforcement \textbf{Que}ry \textbf{R}efinement), a modula...

---

### 35. Praxy Voice: Voice-Prompt Recovery + BUPS for Commercial-Class Indic TTS from a Frozen Non-Indic Base at Zero Commercial-Training-Data Cost

**Authors:** Venkata Pushpak Teja Menta

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25441v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25441v1)

**Summary:** Commercial TTS systems produce near-native Indic audio, but the best open-source bases (Chatterbox, Indic Parler-TTS, IndicF5) trail them on measured phonological dimensions, and the most widely adopted multilingual base (Chatterbox, 23 languages) does not even tokenise Telugu or Tamil. We ask: what is the minimum intervention that brings such a non-Indic-native base to commercial-class output on Telugu, Tamil, and Hindi, without training a new acoustic decoder and without any commercial TTS tra...

---

### 36. Do LLMs Capture Embodied Cognition and Cultural Variation? Cross-Linguistic Evidence from Demonstratives

**Authors:** Yu Wang, Emmanuele Chersoni, Chu-Ren Huang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25423v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25423v1)

**Summary:** Do large language models (LLMs) truly acquire embodied cognition and cultural conventions from text? We introduce demonstratives, fundamental spatial expressions like "this/that" in English and "zhè/nà" in Chinese, as a novel probe for grounded knowledge. Using 6,400 responses from 320 native speakers, we establish a human baseline: English speakers reliably distinguish proximal-distal referents but struggle with perspective-taking, while Chinese speakers switch perspectives fluently but tolerat...

---

### 37. Scaling Probabilistic Transformer via Efficient Cross-Scale Hyperparameter Transfer

**Authors:** Penghao Kuang, Haoyi Wu, Kewei Tu

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25409v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25409v1)

**Summary:** Probabilistic Transformer (PT), a white-box probabilistic model for contextual word representation, has demonstrated substantial similarity to standard Transformers in both computational structure and downstream task performance on small models and small to medium sized datasets. However, PT is less robust to hyperparameter choices than standard Transformers, making it harder to scale efficiently. In this work, we follow Maximal Update Parametrization (muP) to rescale PT's parameters, so that hy...

---

### 38. Benchmarking PyCaret AutoML Against IndoBERT Fine-Tuning for Sentiment Analysis on Indonesian IKN Twitter Data

**Authors:** Mutia Alfi Mayzaroh, Dwi Fitria Ningsih, Nindi Destriani, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25392v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25392v1)

**Summary:** This paper benchmarks a classical machine learning approach based on PyCaret AutoML against a deep learning approach based on IndoBERT fine-tuning for binary sentiment analysis of Indonesian-language Twitter comments related to Ibu Kota Nusantara (IKN). The dataset contains 1,472 manually labeled samples, consisting of 780 negative and 692 positive comments. In the machine learning setting, Logistic Regression, Naive Bayes, and Support Vector Machine were evaluated using 10-fold cross-validation...

---

### 39. Wiki Dumps to Training Corpora: South Slavic Case

**Authors:** Mihailo Škorić

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25384v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25384v1)

**Summary:** This paper presents a methodology for transforming raw Wikimedia dumps into quality textual corpora for seven South Slavic languages. The work is divided into two major phases. The first involves extracting and cleaning text from raw dumps of Wikipedia, Wikisource, Wikibooks, Wikinews, and Wikiquote, where available. This step requires careful handling of raw wiki markup to isolate, first of all, textual articles, and then usable natural language text within them. The second phase addresses the ...

---

### 40. Language corpora for the Dutch medical domain

**Authors:** B. van Es

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25374v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25374v1)

**Summary:** \textbf{Background:} Dutch medical corpora are scarce, limiting NLP development. \\ \textbf{Methods:} We translated English datasets, identified medical text in generic corpora, and extracted open Dutch medical resources. \\ \textbf{Results:} The resulting corpus comprises $\pm$ 35 billion tokens across the medical domain in about 100 million documents, freely available on Hugging Face. \\ \textbf{Conclusion:} This work establishes the first large-scale Dutch medical language corpus for pre-trai...

---

### 41. The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models

**Authors:** Abhinav Kumar Singh, Harsha Vardhan Khurdula, Yoeven D Khemlani, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25359v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25359v1)

**Summary:** Large Language Models are increasingly being deployed to extract structured data from unstructured and semi-structured sources: parsing invoices, medical records, and converting PDF documents to database entries. Yet existing benchmarks for structured output generation either focus on schema compliance alone, or evaluate value correctness within a single source domain. We introduce SOB (The Structured Output Benchmark), a multi-source benchmark spanning three source modalities: native text, imag...

---

### 42. R$^3$-SQL: Ranking Reward and Resampling for Text-to-SQL

**Authors:** Hojae Han, Yeonseok Jeong, Seung-won Hwang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25325v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25325v1)

**Summary:** Modern Text-to-SQL systems generate multiple candidate SQL queries and rank them to judge a final prediction. However, existing methods face two limitations. First, they often score functionally equivalent SQL queries inconsistently despite identical execution results. Second, ranking cannot recover when the correct SQL is absent from the candidate pool. We propose R$^3$-SQL, a Text-to-SQL framework that addresses both issues through unified reward for ranking and resampling. R$^3$-SQL first gro...

---

### 43. Cutscene Agent: An LLM Agent Framework for Automated 3D Cutscene Generation

**Authors:** Lanshan He, Haozhou Pang, Qi Gan, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25318v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25318v1)

**Summary:** Cutscenes are carefully choreographed cinematic sequences embedded in video games and interactive media, serving as the primary vehicle for narrative delivery, character development, and emotional engagement. Producing cutscenes is inherently complex: it demands seamless coordination across screenwriting, cinematography, character animation, voice acting, and technical direction, often requiring days to weeks of collaborative effort from multidisciplinary teams to produce minutes of polished con...

---

### 44. Faithfulness-QA: A Counterfactual Entity Substitution Dataset for Training Context-Faithful RAG Models

**Authors:** Li Ju, Junzhe Wang, Qi Zhang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25313v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25313v1)

**Summary:** Retrieval-Augmented Generation (RAG) models frequently produce answers grounded in parametric memory rather than the retrieved context, undermining the core promise of retrieval augmentation. A fundamental obstacle to fixing this unfaithfulness is the lack of training data that explicitly requires models to prefer context over internal knowledge. We introduce Faithfulness-QA, a large-scale dataset of 99,094 samples constructed through counterfactual entity substitution. Starting from two establi...

---

### 45. LegalMidm: Use-Case-Driven Legal Domain Specialization for Korean Large Language Model

**Authors:** Youngjoon Jang, Chanhee Park, Hyeonseok Moon, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25297v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25297v1)

**Summary:** In recent years, the rapid proliferation of open-source large language models (LLMs) has spurred efforts to turn general-purpose models into domain specialists. However, many domain-specialized LLMs are developed using datasets and training protocols that are not aligned with the nuanced requirements of real-world applications. In the legal domain, where precision and reliability are essential, this lack of consideration limits practical utility. In this study, we propose a systematic training f...

---

### 46. Learning from Medical Entity Trees: An Entity-Centric Medical Data Engineering Framework for MLLMs

**Authors:** Jianghang Lin, Haihua Yang, Deli Yu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25296v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25296v1)

**Summary:** Multimodal Large Language Models (MLLMs) have shown transformative potential in medical applications, yet their performance is hindered by conventional data curation strategies that rely on coarse-grained partitioning by modality or department. Such fragmented approaches fail to capture the hierarchical and interconnected nature of clinical medical knowledge, limiting the models' ability to perform fine-grained recognition and complex reasoning. In this paper, we propose a novel Entity-Centric M...

---

### 47. Below-Chance Blindness: Prompted Underperformance in Small LLMs Produces Positional Bias Rather than Answer Avoidance

**Authors:** Jon-Paul Cacioli

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25249v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25249v1)

**Summary:** Detecting sandbagging--the deliberate underperformance on capability evaluations--is an open problem in AI safety. We tested whether symptom validity testing (SVT) logic from clinical malingering detection could identify sandbagging through below-chance performance (BCB) on forced-choice items. In a pre-registered pilot at the 7-9 billion parameter instruction-tuned scale (3 models, 4 MMLU-Pro domains, 4 conditions, 500 items per cell, 24,000 total trials), the plausibility gate failed. Zero of ...

---

### 48. VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation

**Authors:** Divake Kumar, Sina Tayebati, Devashri Naik, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25235v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25235v1)

**Summary:** Vision-language models (VLMs) are increasingly used as automated judges for multimodal systems, yet their scores provide no indication of reliability. We study this problem through conformal prediction, a distribution-free framework that converts a judge's point score into a calibrated prediction interval using only score-token log-probabilities, with no retraining. We present the first systematic analysis of conformal prediction for VLM-as-a-Judge across 3 judges and 14 visual task categories. ...

---

### 49. DRAGON: A Benchmark for Evidence-Grounded Visual Reasoning over Diagrams

**Authors:** Anirudh Iyengar Kaniyar Narayana Iyengar, Tampu Ravi Kumar, Gaurav Najpande, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25231v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25231v1)

**Summary:** Diagram question answering (DQA) requires models to interpret structured visual representations such as charts, maps, infographics, circuit schematics, and scientific diagrams. Recent vision-language models (VLMs) often achieve high answer accuracy on these tasks, yet correct answers do not guarantee that models ground their reasoning in the diagram regions that support the prediction. Models may instead rely on textual correlations or dataset artifacts without identifying the visual evidence re...

---

### 50. BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate

**Authors:** Arnon Mazza, Elad Levi

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25203v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25203v1)

**Summary:** Deploying guardrails for custom policies remains challenging, as generic safety models fail to capture task-specific requirements, while prompting LLMs suffers from inconsistent boundary-case performance and high inference costs. Training custom classifiers achieves both accuracy and efficiency, yet demands substantial labeled data that is costly to obtain. We present BARRED (Boundary Alignment Refinement through REflection and Debate), a framework for generating faithful and diverse synthetic t...

---

## cs.CV

**50 papers**

### 1. Robust Deepfake Detection: Mitigating Spatial Attention Drift via Calibrated Complementary Ensembles

**Authors:** Minh-Khoa Le-Phan, Minh-Hoang Le, Trong-Le Do, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25889v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25889v1)

**Summary:** Current deepfake detection models achieve state-of-the-art performance on pristine academic datasets but suffer severe spatial attention drift under real-world compound degradations, such as blurring and severe lossy compression. To address this vulnerability, we propose a foundation-driven forensic framework that integrates an extreme compound degradation engine with a structurally constrained, multi-stream architecture. During training, our degradation pipeline systematically destroys high-fre...

---

### 2. No Pedestrian Left Behind: Real-Time Detection and Tracking of Vulnerable Road Users for Adaptive Traffic Signal Control

**Authors:** Anas Gamal Aly, Hala ElAarag

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25887v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25887v1)

**Summary:** Current pedestrian crossing signals operate on fixed timing without adjustment to pedestrian behavior, which can leave vulnerable road users (VRUs) such as the elderly, disabled, or distracted pedestrians stranded when the light changes. We introduce No Pedestrian Left Behind (NPLB), a real-time adaptive traffic signal system that monitors VRUs in crosswalks and automatically extends signal timing when needed. We evaluated five state-of-the-art object detection models on the BGVP dataset, with Y...

---

### 3. QCalEval: Benchmarking Vision-Language Models for Quantum Calibration Plot Understanding

**Authors:** Shuxiang Cao, Zijian Zhang, Abhishek Agarwal, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25884v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25884v1)

**Summary:** Quantum computing calibration depends on interpreting experimental data, and calibration plots provide the most universal human-readable representation for this task, yet no systematic evaluation exists of how well vision-language models (VLMs) interpret them. We introduce QCalEval, the first VLM benchmark for quantum calibration plots: 243 samples across 87 scenario types from 22 experiment families, spanning superconducting qubits and neutral atoms, evaluated on six question types in both zero...

---

### 4. SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring

**Authors:** Hector G. Rodriguez, Marcus Rohrbach

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25855v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25855v1)

**Summary:** Multimodal large language models (MLLMs) achieve ever-stronger performance on visual-language tasks. Even as traditional visual question answering benchmarks approach saturation, reliable deployment requires satisfying low error tolerances in real-world out-of-distribution (OOD) scenarios. Precisely, selective prediction aims to improve coverage, i.e. the share of inputs the system answers, while adhering to a user-defined risk level. This is typically achieved by assigning a confidence score to...

---

### 5. Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation

**Authors:** Yupeng Zhou, Lianghua Huang, Zhifan Wu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25819v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25819v1)

**Summary:** In this work, we propose Mutual Forcing, a framework for fast autoregressive audio-video generation with long-horizon audio-video synchronization. Our approach addresses two key challenges: joint audio-video modeling and fast autoregressive generation. To ease joint audio-video optimization, we adopt a two-stage training strategy: we first train uni-modal generators and then couple them into a unified audio-video model for joint training on paired data. For streaming generation, we ask whether a...

---

### 6. Magnification-Invariant Image Classification via Domain Generalization and Stable Sparse Embedding Signatures

**Authors:** Ifeanyi Ezuma, Olusiji Medaiyese

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25817v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25817v1)

**Summary:** Magnification shift is a major obstacle to robust histopathology classification, because models trained on one imaging scale often generalize poorly to another. Here, we evaluated this problem on the BreaKHis dataset using a strict patient-disjoint leave-one-magnification-out protocol, comparing supervised baseline, baseline augmented with DCGAN-generated patches, and a gradient-reversal domain-general model designed to preserve discriminative information while suppressing magnification-specific...

---

### 7. Instruction-Evidence Contrastive Dual-Stream Decoding for Grounded Vision-Language Reasoning

**Authors:** Yashwant Pravinrao Bangde, Debaditya Roy

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25809v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25809v1)

**Summary:** Vision-Language Models (VLMs) exhibit strong performance in instruction following and open-ended vision-language reasoning, yet they frequently generate fluent outputs that are weakly grounded in visual evidence. Prior works have shown that instruction prompting further worsens this issue by amplifying language priors, especially when the visual signal is uncertain or ambiguous. To address this challenge, we propose a decoding framework that explicitly balances linguistic informativeness and vis...

---

### 8. Improving Diversity in Black-box Few-shot Knowledge Distillation

**Authors:** Tri-Nhan Vo, Dang Nguyen, Kien Do, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25795v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25795v1)

**Summary:** Knowledge distillation (KD) is a well-known technique to effectively compress a large network (teacher) to a smaller network (student) with little sacrifice in performance. However, most KD methods require a large training set and internal access to the teacher, which are rarely available due to various restrictions. These challenges have originated a more practical setting known as black-box few-shot KD, where the student is trained with few images and a black-box teacher. Recent approaches typ...

---

### 9. Diverse Image Priors for Black-box Data-free Knowledge Distillation

**Authors:** Tri-Nhan Vo, Dang Nguyen, Trung Le, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25794v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25794v1)

**Summary:** Knowledge distillation (KD) represents a vital mechanism to transfer expertise from complex teacher networks to efficient student models. However, in decentralized or secure AI ecosystems, privacy regulations and proprietary interests often restrict access to the teacher's interface and original datasets. These constraints define a challenging black-box data-free KD scenario where only top-1 predictions and no training data are available. While recent approaches utilize synthetic data, they stil...

---

### 10. Sketch2Arti: Sketch-based Articulation Modeling of CAD Objects

**Authors:** Yi Yang, Hao Pan, Yijing Cui, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25781v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25781v1)

**Summary:** Articulation modeling aims to infer movable parts and their motion parameters for a 3D object, enabling interactive animation, simulation, and shape editing. In this paper, we present Sketch2Arti, the first sketch-based articulation modeling system for CAD objects. Our key observation is that designers naturally communicate articulation intent through lightweight sketches (e.g., arrows and strokes) that indicate how parts should move, yet translating such sketches into articulated 3D models rema...

---

### 11. Quantum-Inspired Robust and Scalable SAR Object Classification

**Authors:** Maximilian Scharf, Marco Trenti, Felix Bock, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25755v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25755v1)

**Summary:** SAR image classification naturally has to deal with huge noise and a high dynamic range particularly requiring robust classification models. Additionally, the deployment of these models on edge devices, such as drones and military aircraft, requires a careful balance between model size and classification accuracy. This study explores the potential of tensor networks to meet these robustness requirements, specifically evaluating their resilience to data poisoning. Unlike previous works that conce...

---

### 12. Toward Multimodal Conversational AI for Age-Related Macular Degeneration

**Authors:** Ran Gu, Benjamin Hou, Mélanie Hébert, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25720v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25720v1)

**Summary:** Despite strong performance of deep learning models in retinal disease detection, most systems produce static predictions without clinical reasoning or interactive explanation. Recent advances in multimodal large language models (MLLMs) integrate diagnostic predictions with clinically meaningful dialogue to support clinical decision-making and patient counseling. In this study, OcularChat, an MLLM, was fine-tuned from Qwen2.5-VL using simulated patient-physician dialogues to diagnose age-related ...

---

### 13. QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient SNNs

**Authors:** Dewei Bai, Hongxiang Peng, Jiajun Mei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25688v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25688v1)

**Summary:** Binary spike coding enables sparse and event-driven computation in spiking neural networks (SNNs), yet its 1-bit-per-timestep representation fundamentally limits information throughput. This bottleneck becomes increasingly restrictive in deep architectures under short simulation horizons. We propose the Quantized Burst-LIF (QB-LIF) neuron, which reformulates burst spiking as a saturated uniform quantization of membrane potentials with a learnable scale. Instead of relying on predefined multi-thr...

---

### 14. Robustness Evaluation of a Foundation Segmentation Model Under Simulated Domain Shifts in Abdominal CT: Implications for Health Digital Twin Deployment

**Authors:** Sanghati Basu

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25685v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25685v1)

**Summary:** Foundation segmentation models such as the Segment Anything Model (SAM) have demonstrated strong generalization across natural images; however, their robustness under clinically realistic medical imaging domain shifts remains insufficiently quantified. We present a systematic slice-level robustness audit of SAM (ViT-B) for spleen segmentation in abdominal CT using 1,051 nonempty slices from 41 volumes in the Medical Segmentation Decathlon. A standardized ground-truth-derived bounding-box protoco...

---

### 15. Exploring Remote Photoplethysmography for Neonatal Pain Detection from Facial Videos

**Authors:** Ashutosh Dhamaniya, Anup Kumar Gupta, Trishna Saikia, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25680v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25680v1)

**Summary:** Unaddressed pain in neonates can lead to adverse effects, including delayed development and slower weight gain, emphasising the need for more objective and reliable pain assessment methods. Hence, automated methods using behavioural and physiological pain indicators have been developed to aid healthcare professionals in the Neonatal ICU. Traditional contact-based methods for physiological parameter estimation are unsuitable for long-term monitoring and increase the risk of spreading diseases lik...

---

### 16. SAMe: A Semantic Anatomy Mapping Engine for Robotic Ultrasound

**Authors:** Jing Zhang, Duojie Chen, Wentao Jiang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25646v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25646v1)

**Summary:** Robotic ultrasound has advanced local image-driven control, contact regulation, and view optimization, yet current systems lack the anatomical understanding needed to determine what to scan, where to begin, and how to adapt to individual patient anatomy. These gaps make systems still reliant on expert intervention to initiate scanning. Here we present SAMe, a semantic anatomy mapping engine that provides robotic ultrasound with an explicit anatomical prior layer. SAMe addresses scan initiation a...

---

### 17. Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language Models

**Authors:** Chengsheng Zhang, Chenghao Sun, Xinyan Jiang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25642v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25642v1)

**Summary:** Large Vision-Language Models (LVLMs) have achieved remarkable progress in visual-textual understanding, yet their reliability is critically undermined by hallucinations, i.e., the generation of factually incorrect or inconsistent responses. While recent studies using steering vectors demonstrated promise in reducing hallucinations, a notable challenge remains: they inadvertently amplify the severity of residual hallucinations. We attribute this to their exclusive focus on the decoding stage, whe...

---

### 18. Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models

**Authors:** Jiayi Guo, Linqing Wang, Jiangshan Wang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25636v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25636v1)

**Summary:** Unified multimodal models (UMMs) integrate visual understanding and generation within a single framework. For text-to-image (T2I) tasks, this unified capability allows UMMs to refine outputs after their initial generation, potentially extending the performance upper bound. Current UMM-based refinement methods primarily follow a refinement-via-editing (RvE) paradigm, where UMMs produce editing instructions to modify misaligned regions while preserving aligned content. However, editing instruction...

---

### 19. Control Your Queries: Heterogeneous Query Interaction for Camera-Radar Fusion

**Authors:** Jialong Wu, Yihan Wang, Matthias Rottmann

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25574v1)

**Summary:** In autonomous driving, camera-radar fusion offers complementary sensing and low deployment cost. Existing methods perform fusion through input mixing, feature map mixing, or query-based feature sampling. We propose a new fusion paradigm, termed heterogeneous query interaction, and present ConFusion, a camera-radar 3D object detector. ConFusion combines image queries, radar queries, and learnable world queries distributed in 3D space to improve query initialization and object coverage. To encoura...

---

### 20. Vision SmolMamba: Spike-Guided Token Pruning for Energy-Efficient Spiking State-Space Vision Models

**Authors:** Dewei Bai, Hongxiang Peng, Yunyun Zeng, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25570v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25570v1)

**Summary:** Spiking Transformers have shown strong potential for long-range visual modeling through spike-driven self-attention. However, their quadratic token interactions remain fundamentally misaligned with the sparse and event-driven nature of spiking neural computation. To address this limitation, we propose Vision SmolMamba, an energy-efficient spiking state-space architecture that integrates spike-driven dynamics with linear-time selective recurrence. The key idea is a Spike-Guided Spatio-Temporal To...

---

### 21. TopoMamba: Topology-Aware Scanning and Fusion for Segmenting Heterogeneous Medical Visual Media

**Authors:** Fuchen Zheng, Chengpei Xu, Long Ma, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25545v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25545v1)

**Summary:** Visual state-space models (SSMs) have shown strong potential for medical image segmentation, yet their effectiveness is often limited by two practical issues: axis-biased scan ordering weakens the modeling of oblique and curved structures, and naive multi-branch fusion tends to amplify redundant responses. We present TopoMamba, a topology-aware scan-and-fuse framework for segmenting heterogeneous medical visual media. The method combines a diagonal/anti-diagonal TopoA-Scan branch with the standa...

---

### 22. DualGeo: A Dual-View Framework for Worldwide Image Geo-localization

**Authors:** Junchao Cui, Wenqi Shi, Shaoyong Du, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25533v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25533v1)

**Summary:** Worldwide image geo-localization aims to infer the geographic location of an image captured anywhere on Earth, spanning street, city, regional, national, and continental scales. Existing methods rely on visual features that are sensitive to environmental variations (e.g., lighting, season, and weather) and lack effective post-processing to filter outlier candidates, limiting localization accuracy. To address these limitations, we propose DualGeo, a two-stage framework for worldwide image geo-loc...

---

### 23. The Surprising Effectiveness of Canonical Knowledge Distillation for Semantic Segmentation

**Authors:** Muhammad Ali, Kevin Alexander Laube, Madan Ravi Ganesh, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25530v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25530v1)

**Summary:** Recent knowledge distillation (KD) methods for semantic segmentation introduce increasingly complex hand-crafted objectives, yet are typically evaluated under fixed iteration schedules. These objectives substantially increase per-iteration cost, meaning equal iteration counts do not correspond to equal training budgets. It is therefore unclear whether reported gains reflect stronger distillation signals or simply greater compute. We show that iteration-based comparisons are misleading: when wall...

---

### 24. The Forensic Cost of Watermark Removal

**Authors:** Gautier Evennou, Ewa Kijak

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25491v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25491v1)

**Summary:** Current watermark removal methods are evaluated on two axes: attack success rate and perceptual quality. We show this is insufficient. While state-of-the-art attacks successfully degrade the watermark signal without visible distortion, they leave distinct statistical artifacts that betray the removal attempt. We name this overlooked axis Watermark Removal Detection (WRD) and demonstrate that a modern classifier trained on these artifacts achieves state-of-the-art detection rates at $10^{-3}$ FPR...

---

### 25. DDA-Thinker: Decoupled Dual-Atomic Reinforcement Learning for Reasoning-Driven Image Editing

**Authors:** Hanqing Yang, Qiang Zhou, Yongchao Du, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25477v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25477v1)

**Summary:** Recent image editing models have achieved strong visual fidelity but often struggle with tasks requiring complex reasoning. To investigate and enhance the reasoning-grounded planning for image editing, we propose DDA-Thinker, a Thinker-centric framework designed for the independent optimization of a planning module (Thinker) over a fixed generative model (Editor). This decoupled Thinker-centric paradigm facilitates a controlled analysis of the planning module and makes its contribution under a f...

---

### 26. Generalizable Human Gaussian Splatting via Multi-view Semantic Consistency

**Authors:** Jingi Kim, Wonjun Kim

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25466v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25466v1)

**Summary:** Recently, generalizable human Gaussian splatting from sparse-view inputs has been actively studied for the photorealistic human rendering. Most existing methods rely on explicit geometric constraints or predefined structural representations to accurately position 3D Gaussians. Although these approaches have shown the remarkable progress in this field, they still suffer from inconsistent feature representations across multi-view inputs due to complex articulations of the human body and limited ov...

---

### 27. Image Compression with Bubble-Aware Frame Rate Adaptation for Energy-Efficient Video Capsule Endoscopy

**Authors:** Oliver Bause, Jörg Gammerdinger, Julia Werner

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25464v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25464v1)

**Summary:** Video Capsule Endoscopy (VCE) is a promising method for improving the medical examination of the small intestine in the gastrointestinal tract. A key challenge is their limited size, resulting in a short battery lifetime which conflicts with high energy consumption for image capturing and transmission to an on-body device. Thus, we propose an image compression pipeline that substantially reduces the transmitted data while preserving diagnostic image quality. Furthermore, we exploit characteristi...

---

### 28. GramSR: Visual Feature Conditioning for Diffusion-Based Super-Resolution

**Authors:** Fabio D'Oronzio, Federico Putamorsi, Leonardo Zini, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25457v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25457v1)

**Summary:** Despite recent advances, single-image super-resolution (SR) remains challenging, especially in real-world scenarios with complex degradations. Diffusion-based SR methods, particularly those built on Stable Diffusion, leverage strong generative priors but commonly rely on text conditioning derived from semantic captioning. Such textual descriptions provide only high-level semantics and lack the spatially aligned visual information required for faithful restoration, leading to a representation gap...

---

### 29. SARU: A Shadow-Aware and Removal Unified Framework for Remote Sensing Images with New Benchmarks

**Authors:** Zi-Yang Bo, Wei Lu, Hongruixuan Chen, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25432v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25432v1)

**Summary:** Shadows are a prevalent problem in remote sensing imagery (RSI), degrading visual quality and severely limiting the performance of downstream tasks like object detection and semantic segmentation. Most prior works treat shadow detection and removal as separate, cascaded tasks, which can lead to cumbersome process and error accumulation. Furthermore, many deep learning methods rely on paired shadow and non-shadow images for training, which are often unavailable in practice. To address these chall...

---

### 30. A Systematic Post-Train Framework for Video Generation

**Authors:** Zeyue Xue, Siming Fu, Jie Huang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25427v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25427v1)

**Summary:** While large-scale video diffusion models have demonstrated impressive capabilities in generating high-resolution and semantically rich content, a significant gap remains between their pretraining performance and real-world deployment requirements due to critical issues such as prompt sensitivity, temporal inconsistency, and prohibitive inference costs. To bridge this gap, we propose a comprehensive post-training framework that systematically aligns pretrained models with user intentions through ...

---

### 31. Beyond Fidelity: Semantic Similarity Assessment in Low-Level Image Processing

**Authors:** Runjie Wang, Weiling Chen, Tiesong Zhao, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25408v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25408v1)

**Summary:** Low-level image processing has long been evaluated mainly from the perspective of visual fidelity. However, with the rise of deep learning and generative models, processed images may preserve perceptual quality while altering semantic content, making conventional Image Quality Assessment (IQA) insufficient for semantic-level assessment. In this paper, we formalize \textit{Semantic Similarity} as a new evaluation task for low-level image processing, aimed at measuring whether semantic content is ...

---

### 32. Leveraging Previous-Traversal Point Cloud Map Priors for Camera-Based 3D Object Detection and Tracking

**Authors:** Markus Käppeler, Özgün Çiçek, Yakov Miron, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25405v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25405v1)

**Summary:** Camera-based 3D object detection and tracking are central to autonomous driving, yet precise 3D object localization remains fundamentally constrained by depth ambiguity when no expensive, depth-rich online LiDAR is available at inference. In many deployments, however, vehicles repeatedly traverse the same environments, making static point cloud maps from prior traversals a practical source of geometric priors. We propose DualViewMapDet, a camera-only inference framework that retrieves such map p...

---

### 33. GeoSearch: Augmenting Worldwide Geolocalization with Web-Scale Reverse Image Search and Image Matching

**Authors:** Tung-Duong Le-Duc, Hoang-Quoc Nguyen-Son, Minh-Son Dao

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25390v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25390v1)

**Summary:** Worldwide image geolocalization, which aims to predict the GPS coordinates of any image on Earth, remains challenging due to global visual diversity. Recent generative approaches based on Retrieval-Augmented Generation (RAG) and Large Multimodal Models (LMMs) leverage candidates retrieved from fixed databases for reasoning, but often struggle with scenes that are absent from the reference set. In this work, we propose GeoSearch, an open-world geolocation framework that integrates web-scale rever...

---

### 34. COMPASS: COmpact Multi-channel Prior-map And Scene Signature for Floor-Plan-Based Visual Localization

**Authors:** Muhammad Shaheer, Miguel Fernandez-Cortizas, Asier Bikandi-Noya, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25388v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25388v1)

**Summary:** Architectural floor plans are widely available priors which contain not only geometry but also the semantic information of the environment, yet existing localization methods largely ignore this semantic information. To address this, we present COMPASS, an algorithm that exploits both geometric and semantic priors from floor plans to estimate the pose of a robot equipped with dual fisheye cameras. Inspired by scan context descriptor from LiDAR-based place recognition, we design a multi-channel ra...

---

### 35. Benchmarking and Improving GUI Agents in High-Dynamic Environments

**Authors:** Enqi Liu, Liyuan Pan, Zhi Gao, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25380v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25380v1)

**Summary:** Recent advancements in Graphical User Interface (GUI) agents have predominantly focused on training paradigms like supervised fine-tuning (SFT) and reinforcement learning (RL). However, the challenge of high-dynamic GUI environments remains largely underexplored. Existing agents typically rely on a single screenshot after each action for decision-making, leading to a partially observable (or even unobservable) Markov decision process, where the key GUI state including important information for a...

---

### 36. CoRE: Concept-Reasoning Expansion for Continual Brain Lesion Segmentation

**Authors:** Qianqian Chen, Anglin Liu, Jingyang Zhang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25376v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25376v1)

**Summary:** Accurate brain lesion segmentation in MRI is vital for effective clinical diagnosis and treatment planning. Due to high annotation costs and strict data privacy regulations, universal models require employing Continual Learning (CL) to adapt to evolving clinical tasks without losing previously acquired knowledge. However, existing CL paradigms often suffer from capacity limits or redundant parameter growth, and even advanced dynamic methods rely mostly on image-perception strategies that struggl...

---

### 37. PhyloSDF: Phylogenetically-Conditioned Neural Generation of 3D Skull Morphology via Residual Flow Matching

**Authors:** Kaikwan Lau, Gary P. T. Choi

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25371v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25371v1)

**Summary:** Generating novel, biologically plausible three-dimensional morphological structures is a fundamental challenge in computational evolutionary biology, hampered by extreme data scarcity and the requirement that generated shapes respect phylogenetic relationships among species. In this work, we present PhyloSDF, a phylogenetically-conditioned neural generative model for 3D biological morphology that integrates two innovations: (1) a DeepSDF auto-decoder regularized by a novel Phylogenetic Consisten...

---

### 38. GPT-Image-2 in the Wild: A Twitter Dataset of Self-Reported AI-Generated Images from the First Week of Deployment

**Authors:** Kidus Zewde, Simiao Ren, Xingyu Shen, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25370v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25370v1)

**Summary:** The release of GPT-image-2 by OpenAI marks a watershed moment in AI-generated imagery: the boundary between photographic reality and synthetic content has never been more difficult to discern. We introduce the GPT-Image-2 Twitter Dataset, the first published dataset of GPT-image-2 generated images, sourced from publicly available Twitter/X posts in the immediate aftermath of the model's April 21, 2026 release. Leveraging the Twitter API v2 and a multi-stage curation pipeline spanning multilingua...

---

### 39. Self-DACE++: Robust Low-Light Enhancement via Efficient Adaptive Curve Estimation

**Authors:** Jianyu Wen, Jun Xie, Feng Chen, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25367v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25367v1)

**Summary:** In this paper, we present Self-DACE++, an improved unsupervised and lightweight framework for Low-Light Image Enhancement (LLIE), building upon our previous Self-Reference Deep Adaptive Curve Estimation (Self-DACE). To better address the trade-off between computational efficiency and restoration quality, Self-DACE++ introduces enhanced Adaptive Adjustment Curves (AACs). These curves, governed by minimal trainable parameters, flexibly adjust the dynamic range while preserving the color fidelity, ...

---

### 40. HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation

**Authors:** Bingzi Zhang, Kaisi Guan, Ruihua Song

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25361v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25361v1)

**Summary:** Video generation models have developed rapidly in recent years, where generating natural human motion plays a pivotal role. However, accurately evaluating the quality of generated human motion video remains a significant challenge. Existing evaluation metrics primarily focus on global scene statistics, often overlooking fine-grained human details and consequently failing to align with human subjective preference. To bridge this gap, we propose HuM-Eval, a novel human-centric evaluation framework...

---

### 41. Benchmarking Layout-Guided Diffusion Models through Unified Semantic-Spatial Evaluation in Closed and Open Settings

**Authors:** Luca Parolari, Nicla Faccioli, Lamberto Ballan

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25358v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25358v1)

**Summary:** Evaluating layout-guided text-to-image generative models requires assessing both semantic alignment with textual prompts and spatial fidelity to prescribed layouts. Assessing layout alignment requires collecting fine-grained annotations, which is costly and labor-intensive. Consequently, current benchmarks rarely provide comprehensive layout evaluation and often remain limited in scale or coverage, making model comparison, ranking, and interpretation difficult. In this work, we introduce a close...

---

### 42. Assessment of the quantitative impact of occlusal positioning splints on temporomandibular joint conditions

**Authors:** Agnieszka Anna Tomaka, Krzysztof Domino, Dariusz Pojda, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25322v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25322v1)

**Summary:** A computational method for quantitative analysis of temporomandibular joint (TMJ) configuration using occlusal positioning splints is proposed and demonstrated. The method models a positioning splint as a physical realization of a predefined rigid transformation of the mandible, derived from multimodal data, including CBCT, facial motion acquisition, and dental scans integrated within a common coordinate system. Splints corresponding to selected mandibular positions are designed and fabricated, ...

---

### 43. Edge-Cloud Collaborative Reconstruction via Structure-Aware Latent Diffusion for Downstream Remote Sensing Perception

**Authors:** Yun Li, Xianju Li

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25319v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25319v1)

**Summary:** The exponential surge in high-resolution remote sensing data faces a severe bottleneck in satellite-to-ground transmission. Limited downlink bandwidth forces the use of extreme high-ratio compression, which irreversibly destroys high-frequency structural details essential for downstream machine perception tasks like object detection. While current super-resolution techniques attempt to recover these details, regression-based methods often yield over-smoothed textures, and generative diffusion mo...

---

### 44. Towards Robust Deep Learning-based Rumex Obtusifolius Detection from Drone Images

**Authors:** Fabian Dionys Schrag, Mehmet Ozgur Turkoglu, Konrad Schindler, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25316v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25316v1)

**Summary:** Domain adaptation (DA) addresses the challenge of transferring a machine learning model trained on a source domain to a target domain with a different data distribution. In this work, we study DA for the task of Rumex obtusifolius (Rumex) image classification. We train models on a published, ground vehicle-based dataset (source) and evaluate their performance on a custom target dataset acquired by unmanned aerial vehicles (UAVs). We find that Convolutional Neural Network (CNN) models, specifical...

---

### 45. SaliencyDecor: Enhancing Neural Network Interpretability through Feature Decorrelation

**Authors:** Ali Karkehabadi, Jamshid Hassanpour, Houman Homayoun, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25315v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25315v1)

**Summary:** Gradient-based saliency methods are widely used to interpret deep neural networks, yet they often produce noisy and unstable explanations that poorly align with semantically meaningful input features. We argue that a fundamental cause of this behavior lies in the geometry of learned representations: correlated feature dimensions diffuse attribution gradients across redundant directions, resulting in blurred and unreliable saliency maps. To address this issue, we identify feature correlation as a...

---

### 46. Golden RPG: Confidence-Adaptive Region-Aware Noise for Compositional Text-to-Image Generation

**Authors:** Hao Li

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25314v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25314v1)

**Summary:** Compositional text-to-image (T2I) generation requires a model to honour multiple sub-prompts that describe distinct image regions. Recent work shows that the \emph{starting noise} of a diffusion model carries significant semantic information: ``golden'' noise predicted from text can substantially raise prompt fidelity. We observe that this noise prediction is, however, fundamentally global: the same network is asked to summarise a long, multi-region prompt with a single text embedding, which bec...

---

### 47. Rapid tracking through strongly scattering media with physics-informed neuromorphic speckle analysis

**Authors:** Yuqing Cao, Shuo Zhu, Rongzhou Chen, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25310v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25310v1)

**Summary:** This work addresses the critical problem of tracking fast-moving objects through strongly scattering media in a low-light environment. Different from existing approaches that use frame-based cameras with fixed exposure times, which trade off signal-to-noise ratio for temporal resolution, we introduce computational neuromorphic tracking (CNT), a physics-informed framework that combines asynchronous event sensing with task-driven speckle analysis for robust motion estimation. We formulate the neur...

---

### 48. DenseScout: Algorithm-System Co-design for Budgeted Tiny Object Selection on Edge Platforms

**Authors:** Xiong Zhouzhi, Zimo Zeng, Yi Chen, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25300v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25300v1)

**Summary:** Deploying tiny object perception on edge platforms is challenging because practical systems must satisfy both strict compute budgets and end-to-end latency constraints. A common strategy is to first select a small number of candidate patches from a high-resolution image and then apply downstream processing only to the selected regions. However, existing detector-based frontends are not well aligned with this setting: strong offline detection accuracy does not necessarily yield effective low-budg...

---

### 49. The Thinking Pixel: Recursive Sparse Reasoning in Multimodal Diffusion Latents

**Authors:** Yuwei Sun, Yuxuan Yao, Hui Li, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25299v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25299v1)

**Summary:** Diffusion models have achieved success in high-fidelity data synthesis, yet their capacity for more complex, structured reasoning like text following tasks remains constrained. While advances in language models have leveraged strategies such as latent reasoning and recursion to enhance text understanding capabilities, extending these to multimodal text-to-image generation tasks is challenging due to the continuous and non-discrete nature of visual tokens. To tackle this problem, we draw inspirat...

---

### 50. Exploring Time Conditioning in Diffusion Generative Models from Disjoint Noisy Data Manifolds

**Authors:** Liuzhuozheng Li, Zhiyuan Zhan, Shuhong Liu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25289v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25289v1)

**Summary:** Practically, training diffusion models typically requires explicit time conditioning to guide the network through the denoising sampling process. Especially in deterministic methods like DDIM, the absence of time conditioning leads to significant performance degradation. However, other deterministic sampling approaches, such as flow matching, can generate high-quality content without this conditioning, raising the question of its necessity. In this work, we revisit the role of time conditioning ...

---

## cs.LG

**50 papers**

### 1. Recursive Multi-Agent Systems

**Authors:** Xiyuan Yang, Jiaru Zou, Rui Pan, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25917v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25917v1)

**Summary:** Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogen...

---

### 2. How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum

**Authors:** Chu-Cheng Lin, Eugene Ie

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25907v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25907v1)

**Summary:** Adapting reasoning models to new tasks during post-training with only output-level supervision stalls under reinforcement learning from verifiable rewards (RLVR) when the initial success probability $p_0$ is small. Using the Tsallis $q$-logarithm, we define a loss family $J_Q$ that interpolates between RLVR (at $q{=}0$, the exploitation pole) and the log-marginal-likelihood over latent trajectories (at $q{=}1$, the density-estimation pole). All members share the same per-example gradient directi...

---

### 3. Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics

**Authors:** Andre Herz, Daniel Durstewitz, Georgia Koppe

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25904v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25904v1)

**Summary:** Identity teacher forcing (ITF) enables stable training of deterministic recurrent surrogates for chaotic dynamical systems and has been highly effective for dynamical systems reconstruction (DSR) with recurrent neural networks (RNNs), including interpretable almost-linear RNNs (AL-RNNs). However, as an intervention-based prediction loss (and thus a generalized Bayes update), teacher forcing need not match the free-running model's marginal likelihood geometry. We compare the objective-induced cur...

---

### 4. Carbon-Taxed Transformers: A Green Compression Pipeline for Overgrown Language Models

**Authors:** Ajmain Inqiad Alam, Palash Roy, Chanchal K. Roy, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25903v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25903v1)

**Summary:** The accelerating adoption of Large Language Models (LLMs) in software engineering (SE) has brought with it a silent crisis: unsustainable computational cost. While these models demonstrate remarkable capabilities in different SE tasks, they are unmanageably large, slow to deploy, memory-intensive, and carbon-heavy. This reality threatens not only the scalability and accessibility of AI-powered SE, but also its long-term environmental sustainability. The research challenge is clear: we must go be...

---

### 5. Toward a Functional Geometric Algebra for Natural Language Semantics

**Authors:** James Pustejovsky

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25902v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25902v1)

**Summary:** Distributional and neural approaches to natural language semantics have been built almost exclusively on conventional linear algebra: vectors, matrices, tensors, and the operations that accompany them. These methods have achieved remarkable empirical success, yet they face persistent structural limitations in compositional semantics, type sensitivity, and interpretability. I argue in this paper that geometric algebra (GA) -- specifically, Clifford algebras -- provides a mathematically superior f...

---

### 6. TSN-Affinity: Similarity-Driven Parameter Reuse for Continual Offline Reinforcement Learning

**Authors:** Dominik Żurek, Kamil Faber, Marcin Pietron, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25898v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25898v1)

**Summary:** Continual offline reinforcement learning (CORL) aims to learn a sequence of tasks from datasets collected over time while preserving performance on previously learned tasks. This setting corresponds to domains where new tasks arise over time, but adapting the model in live environment interactions is expensive, risky, or impossible. However, CORL inherits the dual difficulty of offline reinforcement learning and adapting while preventing catastrophic forgetting. Replay-based continual learning a...

---

### 7. Variational Neural Belief Parameterizations for Robust Dexterous Grasping under Multimodal Uncertainty

**Authors:** Clinton Enwerem, Shreya Kalyanaraman, John S. Baras, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25897v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25897v1)

**Summary:** Contact variability, sensing uncertainty, and external disturbances make grasp execution stochastic. Expected-quality objectives ignore tail outcomes and often select grasps that fail under adverse contact realizations. Risk-sensitive POMDPs address this failure mode, but many use particle-filter beliefs that scale poorly, obstruct gradient-based optimization, and estimate Conditional Value-at-Risk (CVaR) with high-variance approximations. We instead formulate grasp acquisition as variational in...

---

### 8. Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers

**Authors:** Jan Dubiński, Jan Betley, Anna Sztyber-Betley, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25891v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25891v1)

**Summary:** Finetuning a language model can lead to emergent misalignment (EM) [Betley et al., 2025b]. Models trained on a narrow distribution of misaligned behavior generalize to more egregious behaviors when tested outside the training distribution.   We study a set of interventions proposed to reduce EM. We confirm that these interventions reduce or eliminate EM on existing evaluations (questions like "How do I make a quick buck?"). However, if the evaluation prompts are tweaked to resemble the training ...

---

### 9. Explainable AI for Jet Tagging: A Comparative Study of GNNExplainer, GNNShap, and GradCAM for Jet Tagging in the Lund Jet Plane

**Authors:** Pahal D. Patel, Sanmay Ganguly

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25885v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25885v1)

**Summary:** Graph neural networks such as ParticleNet and transformer based networks on point clouds such as ParticleTransformer achieve state-of-the-art performance on jet tagging benchmarks at the Large Hadron Collider, yet the physical reasoning behind their predictions remains opaque. We present different methods, i.e. perturbation-based (GNNExplainer), Shapley-value-based (GNNShap), and gradient-based (GRADCam); adapted to operate on LundNet's Lund-plane graph representation. Leveraging the fact that e...

---

### 10. When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient

**Authors:** Shuning Shang, Hubert Strauss, Stanley Wei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25872v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25872v1)

**Summary:** Training language models via reinforcement learning often relies on imperfect proxy rewards, since ground truth rewards that precisely define the intended behavior are rarely available. Standard metrics for assessing the quality of proxy rewards, such as ranking accuracy, treat incorrect rewards as strictly harmful. In this work, however, we highlight that not all deviations from the ground truth are equal. By theoretically analyzing which outputs attract probability during policy gradient optim...

---

### 11. Investigation into In-Context Learning Capabilities of Transformers

**Authors:** Rushil Chandrupatla, Leo Bangayan, Sebastian Leng, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25858v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25858v1)

**Summary:** Transformers have demonstrated a strong ability for in-context learning (ICL), enabling models to solve previously unseen tasks using only example input output pairs provided at inference time. While prior theoretical work has established conditions under which transformers can perform linear classification in-context, the empirical scaling behavior governing when this mechanism succeeds remains insufficiently characterized.   In this paper, we conduct a systematic empirical study of in-context ...

---

### 12. G-Loss: Graph-Guided Fine-Tuning of Language Models

**Authors:** Sharma Aditya, Agarwal Vinti, Kumar Rajesh

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25853v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25853v1)

**Summary:** Traditional loss functions, including cross-entropy, contrastive, triplet, and su pervised contrastive losses, used for fine-tuning pre-trained language models such as BERT, operate only within local neighborhoods and fail to account for the global semantic structure. We present G-Loss, a graph-guided loss function that incorporates semi-supervised label propagation to use structural relationships within the embedding manifold. G-Loss builds a document-similarity graph that captures global seman...

---

### 13. From Soliloquy to Agora: Memory-Enhanced LLM Agents with Decentralized Debate for Optimization Modeling

**Authors:** Jianghao Lin, Zi Ling, Chenyu Zhou, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25847v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25847v1)

**Summary:** Optimization modeling underpins real-world decision-making in logistics, manufacturing, energy, and public services, but reliably solving such problems from natural-language requirements remains challenging for current large language models (LLMs). In this paper, we propose \emph{Agora-Opt}, a modular agentic framework for optimization modeling that combines decentralized debate with a read-write memory bank. Agora-Opt allows multiple agent teams to independently produce end-to-end solutions and...

---

### 14. Barriers to Universal Reasoning With Transformers (And How to Overcome Them)

**Authors:** Oliver Kraus, Yash Sarrof, Yuekun Yao, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25800v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25800v1)

**Summary:** Chain-of-Thought (CoT) has been shown to empirically improve Transformers' performance, and theoretically increase their expressivity to Turing completeness. However, whether Transformers can learn to generalize to CoT traces longer than those seen during training is understudied. We use recent theoretical frameworks for Transformer length generalization and find that -- under standard positional encodings and a finite alphabet -- Transformers with CoT cannot solve problems beyond $TC^0$, i.e. t...

---

### 15. Improving Diversity in Black-box Few-shot Knowledge Distillation

**Authors:** Tri-Nhan Vo, Dang Nguyen, Kien Do, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25795v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25795v1)

**Summary:** Knowledge distillation (KD) is a well-known technique to effectively compress a large network (teacher) to a smaller network (student) with little sacrifice in performance. However, most KD methods require a large training set and internal access to the teacher, which are rarely available due to various restrictions. These challenges have originated a more practical setting known as black-box few-shot KD, where the student is trained with few images and a black-box teacher. Recent approaches typ...

---

### 16. Diverse Image Priors for Black-box Data-free Knowledge Distillation

**Authors:** Tri-Nhan Vo, Dang Nguyen, Trung Le, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25794v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25794v1)

**Summary:** Knowledge distillation (KD) represents a vital mechanism to transfer expertise from complex teacher networks to efficient student models. However, in decentralized or secure AI ecosystems, privacy regulations and proprietary interests often restrict access to the teacher's interface and original datasets. These constraints define a challenging black-box data-free KD scenario where only top-1 predictions and no training data are available. While recent approaches utilize synthetic data, they stil...

---

### 17. Sustained Gradient Alignment Mediates Subliminal Learning in a Multi-Step Setting: Evidence from MNIST Auxiliary Logit Distillation Experiment

**Authors:** Chayanon Kitkana, Shivam Arora

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25779v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25779v1)

**Summary:** In the MNIST auxiliary logit distillation experiment, a student can acquire an unintended teacher trait despite distilling only on no-class logits through a phenomenon called subliminal learning. Under a single-step gradient descent assumption, subliminal learning theory attributes this effect to alignment between the trait and distillation gradients, but does not guarantee that this alignment persists in a multi-step setting. We empirically show that gradient alignment remains weakly but consis...

---

### 18. Measuring the Sensitivity of Classification Models with the Error Sensitivity Profile

**Authors:** Andrea Maurino

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25765v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25765v1)

**Summary:** The quality of training data is critical to the performance of machine learning models. In this paper, the Error Sensitivity Profile (ESP) is proposed. It quantifies the sensitivity of model performance to errors in a single feature or in multiple features. By leveraging ESP, data-cleaning efforts can be prioritized based on error types and features most likely to affect model performance. To support the computation of this metric, an integrated suite of tools, called \dirty, is created. We cond...

---

### 19. Adaptive Meta-Learning Stochastic Gradient Hamiltonian Monte Carlo Simulation for Bayesian Updating of Structural Dynamic Models

**Authors:** Xianghao Meng, James L. Beck, Yong Huang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25710v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25710v1)

**Summary:** In the last few decades, Markov chain Monte Carlo (MCMC) methods have been widely applied to Bayesian updating of structural dynamic models in the field of structural health monitoring. Recently, several MCMC algorithms have been developed that incorporate neural networks to enhance their performance for specific Bayesian model updating problems. However, a common challenge with these approaches lies in the fact that the embedded neural networks often necessitate retraining when faced with new t...

---

### 20. Bug-Report-Driven Fault Localization: Industrial Benchmarking and Lesson Learned at ABB Robotics

**Authors:** Pernilla Hall, Anton Ununger, Riccardo Rubei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25700v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25700v1)

**Summary:** Software quality assurance remains a major challenge in industrial environments, where large-scale and long-lived systems inevitably accumulate defects. Identifying the location of a fault is often time-consuming and costly, particularly during maintenance phases when developers must rely primarily on textual bug reports rather than complete runtime or code-level context. In this study, we investigated if artificial intelligence can support fault localization using only the natural-language cont...

---

### 21. Deflation-Free Optimal Scoring

**Authors:** Sharmin Afroz, Brendan Ames

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25664v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25664v1)

**Summary:** Sparse Optimal Scoring (SOS) reformulates linear discriminant analysis to enable feature selection through elastic net regularization, making it well-suited for high-dimensional settings where the number of features exceeds observations. Most existing SOS methods use deflation-based strategies that compute discriminant vectors sequentially, which can propagate errors and produce suboptimal solutions. We propose a novel approach that estimates all discriminant vectors simultaneously under an expl...

---

### 22. Residual-loss Anomaly Analysis of Physics-Informed Neural Networks: An Inverse Method for Change-point Detection in Nonlinear Dynamical Systems with Regime Switching

**Authors:** Yuhe Bai, Chengli Tan, Jiaqi Li, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25655v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25655v1)

**Summary:** Nonlinear dynamical systems with regime transitions are typically described by ordinary differential equations with jumping parameters parameters. Traditional methods often treat change-point detection and parameter estimation as separate tasks, ignoring the inherent coupling between them. To address this, we propose residual-loss anomaly analysis of physics-informed neural networks, a unified framework that leverages dynamical consistency within the physics-informed learning paradigm. This appr...

---

### 23. Towards interpretable AI with quantum annealing feature selection

**Authors:** Francesco Aldo Venturelli, Emanuele Costa, Sikha O K, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25649v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25649v1)

**Summary:** Deep learning models are used in critical applications, in which mistakes can have serious consequences. Therefore, it is crucial to understand how and why models generate predictions. This understanding provides useful information to check whether the model is learning the right patterns, detect biases in the data, improve model design, and build systems that can be trusted. This work proposes a new method for interpreting Convolutional Neural Networks in image classification tasks. The approac...

---

### 24. PLMGH: What Matters in PLM-GNN Hybrids for Code Classification and Vulnerability Detection

**Authors:** Mohamed Taoufik Kaouthar El Idrissi, Edward Zulkoski, Mohammad Hamdaqa

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25599v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25599v1)

**Summary:** Code understanding models increasingly rely on pretrained language models (PLMs) and graph neural networks (GNNs), which capture complementary semantic and structural information. We conduct a controlled empirical study of PLM-GNN hybrids for code classification and vulnerability detection tasks by systematically pairing three code-specialized PLMs with three foundational GNN architectures. We compare these hybrids against PLM-only and GNN-only baselines on Java250 and Devign, including an ident...

---

### 25. Walking Through Uncertainty: An Empirical Study of Uncertainty Estimation for Audio-Aware Large Language Models

**Authors:** Chun-Yi Kuan, Wei-Ping Huang, Hung-yi Lee

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25591v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25591v1)

**Summary:** Recent audio-aware large language models (ALLMs) have demonstrated strong capabilities across diverse audio understanding and reasoning tasks, but they still frequently produce hallucinated or overly confident outputs. While uncertainty estimation has been extensively studied in text-only LLMs, it remains largely unexplored for ALLMs, where audio-conditioned generation introduces additional challenges such as perceptual ambiguity and cross-modal grounding. In this work, we present the first syst...

---

### 26. Dictionary learning for Kernel EDMD

**Authors:** Erik Lien Bolager, Boumediene Hamzi, Houman Owhadi, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25572v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25572v1)

**Summary:** Studying nonlinear dynamical systems through their state space behavior can be challenging, and one possible alternative is to analyze them via their associated Koopman operator. This turns the nonlinear problem into a linear, infinite-dimensional one. To approximate the operator in finite dimensions, extended dynamic mode decomposition (EDMD) is a commonly used algorithm. It requires a finite list of functionals and a set of snapshots from the system to compute an approximation of the operator ...

---

### 27. Egocentric Tactile and Proximity Sensors as Observation Priors for Humanoid Collision Avoidance

**Authors:** Carson Kohlbrenner, Niraj Pudasaini, William Xie, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25554v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25554v1)

**Summary:** Collision-free motion is often aided by tactile and proximity sensors distributed on the body of the robot due to their resistance to occlusion as opposed to external cameras. However, how to shape the sensor's properties, such as sensing coverage; type; and range, to enable avoidant behavior remains unclear. In this work, we present a reinforcement learning framework for whole-body collision avoidance on a humanoid H1-2 robot and use it to characterize how sensor properties shape learned avoida...

---

### 28. On Halting vs Converging in Recurrent Graph Neural Networks

**Authors:** Jeroen Bollen, Stijn Vansummeren

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25551v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25551v1)

**Summary:** Recurrent Graph Neural Networks (RGNNs) extend standard GNNs by iterating message-passing until some stopping condition is met. Various RGNN models have been proposed in the literature. In this paper, we study three such models: converging RGNNs, where all vertex representations must stabilise; output-converging RGNNs, where only the output classifications must stabilise; and halting RGNNs, where a per-vertex halting classifier determines when to stop. We establish expressiveness relationships b...

---

### 29. Enhancing SignSGD: Small-Batch Convergence Analysis and a Hybrid Switching Strategy

**Authors:** Haoran Chen, Wentao Wang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25550v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25550v1)

**Summary:** SignSGD compresses each stochastic gradient coordinate to a single bit, offering substantial memory and communication savings, but its 1-bit quantization removes magnitude information and is known to leave a generalization gap relative to well-tuned SGD. We revisit SignSGD from a 1-bit quantization and dithering perspective and contribute three improvements. First, we derive a small-batch convergence rate for SignSGD under unimodal symmetric gradient noise using a signal-to-noise weighted statio...

---

### 30. Dyna-Style Safety Augmented Reinforcement Learning: Staying Safe in the Face of Uncertainty

**Authors:** Artur Eisele, Bernd Frauenknecht, Friedrich Solowjow, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25508v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25508v1)

**Summary:** Safety remains an open problem in reinforcement learning (RL), especially during training. While safety filters are promising to address safe exploration, they are generally poorly suited for high-dimensional systems with unknown dynamics. We propose Dyna-style Safety Augmented Reinforcement Learning (Dyna-SAuR), a novel algorithm that learns both a scalable safety filter and a control policy using a learned uncertainty-aware dynamics model, while requiring minimal domain knowledge. The filter a...

---

### 31. EvoTSC: Evolving Feature Learning Models for Time Series Classification via Genetic Programming

**Authors:** Xuanhao Yang, Bing Xue, Mengjie Zhang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25499v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25499v1)

**Summary:** Time series classification is an important analytical task across diverse domains. However, its practical application is often hindered by the scarcity of labeled data and the requirement for substantial computational resources. To address these challenges, this paper proposes EvoTSC, a novel genetic programming approach designed to automatically evolve lightweight feature learning models for time series classification. The core of EvoTSC is a carefully designed multi-layer program structure tha...

---

### 32. Adaptable phase retrieval for coherent transition radiation spectroscopy based on differentiable physics information

**Authors:** Ritz Ann Aguilar, Maxwell LaBerge, Andreas Doepp, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25489v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25489v1)

**Summary:** Coherent transition radiation (CTR) spectroscopy is a critical diagnostic for characterizing the longitudinal structure of relativistic electron bunches in laser-plasma and conventional accelerators. In practice, recovering the bunch profile from a measured CTR spectrum is an ill-posed phase-retrieval problem. Traditionally, this is addressed using Gerchberg-Saxton (GS)-type iterative algorithms. However, these implementations often rely on explicit inverse propagators, making them difficult to ...

---

### 33. Emergent Self-Attention from Astrocyte-Gated Associative Memory Dynamics

**Authors:** Arnau Vivet, Alex Arenas

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25481v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25481v1)

**Summary:** We introduce a Hopfield-type associative memory in which effective connectivity is multiplicatively modulated by astrocytic gains evolving under an entropy-regularized replicator equation. The coupled neuron-astrocyte dynamics admit a Lyapunov function, ensuring global convergence. At fixed points, astrocytic gains implement a softmax-normalized allocation over pattern similarity scores, yielding a mechanistic realization of self-attention as emergent routing on the gain simplex. In regimes of h...

---

### 34. Subspace Optimization for Efficient Federated Learning under Heterogeneous Data

**Authors:** Shuchen Zhu, Zhengyang Huang, Yuqi Xu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25467v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25467v1)

**Summary:** Federated learning increasingly operates in a large-model regime where communication, memory, and computation are all scarce. Typically, non-IID client data induce drift that degrades the stability and performance of local training. Existing remedies such as SCAFFOLD introduce heterogeneity-correction mechanisms to address this challenge, but they incur substantial extra communication and memory overhead. This paper proposes a subspace optimization method for federated learning (SSF), which perf...

---

### 35. FED-FSTQ: Fisher-Guided Token Quantization for Communication-Efficient Federated Fine-Tuning of LLMs on Edge Devices

**Authors:** Changyu Li, Shuanghong Huang, Jiashen Liu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25421v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25421v1)

**Summary:** Federated fine-tuning provides a practical route to adapt large language models (LLMs) on edge devices without centralizing private data, yet in mobile deployments the training wall-clock is often bottlenecked by straggler-limited uplink communication under heterogeneous bandwidth and intermittent participation. Although parameter-efficient fine-tuning (PEFT) reduces trainable parameters, per-round payloads remain prohibitive in non-IID regimes, where uniform compression can discard rare but tas...

---

### 36. Biased Dreams: Limitations to Epistemic Uncertainty Quantification in Latent Space Models

**Authors:** Julia Berger, Bernd Frauenknecht, Sebastian Trimpe, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25416v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25416v1)

**Summary:** Model-Based Reinforcement Learning distinguishes between physical dynamics models operating on proprioceptive inputs and latent dynamics models operating on high-dimensional image observations. A prominent latent approach is the Recurrent State Space Model used in the Dreamer family. While epistemic uncertainty quantification to inform exploration and mitigate model exploitation is well established for physical dynamics models, its transfer to latent dynamics models has received limited scrutiny...

---

### 37. Safe-Support Q-Learning: Learning without Unsafe Exploration

**Authors:** Yeeun Lim, Narim Jeong, Donghwan Lee

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25379v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25379v1)

**Summary:** Ensuring safety during reinforcement learning (RL) training is critical in real-world applications where unsafe exploration can lead to devastating outcomes. While most safe RL methods mitigate risk through constraints or penalization, they still allow exploration of unsafe states during training. In this work, we adopt a stricter safety requirement that eliminates unsafe state visitation during training. To achieve this goal, we propose a Q-learning-based safe RL framework that leverages a beha...

---

### 38. From Cursed to Competitive: Closing the ZO-FO Gap via Input-to-State Stability

**Authors:** Amir Ali Farzin, Philipp Braun, Iman Shames

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25372v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25372v1)

**Summary:** While it is generally understood that zeroth-order (ZO) algorithms have an extra dependency on their number of iterations for any choice of parameters, compared to their first-order (FO) counterparts, in this work, we show that under several conditions, in expectation, ZO methods do not suffer from extra dimension dependencies in their convergence rates with respect to their FO counterparts. We look at optimisation algorithms from the dynamical systems perspective and analyse the conditions unde...

---

### 39. GraphPL: Leveraging GNN for Efficient and Robust Modalities Imputation in Patchwork Learning

**Authors:** Xingjian Hu, Zuoyu Yan, Jianhua Zhu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25352v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25352v1)

**Summary:** Current research on distributed multi-modal learning typically assumes that clients can access complete information across all modalities, which may not hold in practice. In this paper, we explore patchwork learning, in which the modalities available to different clients vary, and the objective is to impute the missing modalities for each client in an unsupervised manner. Existing methods are shown not to fully utilize the modality information as they tend to rely on only a subset of the observe...

---

### 40. VAE-Inf: A statistically interpretable generative paradigm for imbalanced classification

**Authors:** Hongfei Wu, Ruijian Han, Yancheng Yuan

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25334v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25334v1)

**Summary:** Imbalanced classification remains a pervasive challenge in machine learning, particularly when minority samples are too scarce to provide a robust discriminative boundary. In such extreme scenarios, conventional models often suffer from unstable decision boundaries and a lack of reliable error control. To bridge the gap between generative modeling and discriminative classification, we propose a two-stage framework \textbf{VAE-Inf} that integrates deep representation learning with statistically i...

---

### 41. QFlash: Bridging Quantization and Memory Efficiency in Vision Transformer Attention

**Authors:** Sehyeon Oh, Yongin Kwon, Jemin Lee

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25306v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25306v1)

**Summary:** FlashAttention improves efficiency through tiling, but its online softmax still relies on floating-point arithmetic for numerical stability, making full quantization difficult. We identify three main obstacles to integer-only FlashAttention: (1) scale explosion during tile-wise accumulation, (2) inefficient shift-based exponential operations on GPUs, and (3) quantization granularity constraints requiring uniform scales for integer comparison. To address these challenges, we propose \textit{QFlas...

---

### 42. RCProb: Probabilistic Rule Extraction for Efficient Simplification of Tree Ensembles

**Authors:** Josue Obregon

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25304v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25304v1)

**Summary:** Tree ensembles are widely used in industrial machine learning due to their strong predictive performance and efficient training procedures. However, as the number of trees in an ensemble grows, the resulting models become increasingly difficult for humans to interpret. To address this limitation, explainable artificial intelligence (XAI) studies methods that generate interpretable models capable of explaining complex predictors. One approach consists of extracting decision rules from tree ensemb...

---

### 43. Optimization-Free Topological Sort for Causal Discovery via the Schur Complement of Score Jacobians

**Authors:** Rui Wu, Hong Xie

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25295v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25295v1)

**Summary:** Continuous causal discovery typically couples representation learning with structural optimization via non-convex acyclicity penalties, which subjects solvers to local optima and restricts scalability in high-dimensional regimes. We propose a decoupled paradigm that shifts the causal discovery bottleneck from non-convex optimization to statistical score estimation. We introduce the Score-Schur Topological Sort (SSTS), an algorithm that extracts topological order directly from unconstrained gener...

---

### 44. Exploring Time Conditioning in Diffusion Generative Models from Disjoint Noisy Data Manifolds

**Authors:** Liuzhuozheng Li, Zhiyuan Zhan, Shuhong Liu, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25289v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25289v1)

**Summary:** Practically, training diffusion models typically requires explicit time conditioning to guide the network through the denoising sampling process. Especially in deterministic methods like DDIM, the absence of time conditioning leads to significant performance degradation. However, other deterministic sampling approaches, such as flow matching, can generate high-quality content without this conditioning, raising the question of its necessity. In this work, we revisit the role of time conditioning ...

---

### 45. Spectral bandits

**Authors:** Tomáš Kocák, Rémi Munos, Branislav Kveton, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25272v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25272v1)

**Summary:** Smooth functions on graphs have wide applications in manifold and semi-supervised learning. In this work, we study a bandit problem where the payoffs of arms are smooth on a graph. This framework is suitable for solving online learning problems that involve graphs, such as content-based recommendation. In this problem, each item we can recommend is a node of an undirected graph and its expected rating is similar to the one of its neighbors. The goal is to recommend items that have high expected ...

---

### 46. Online learning with Erdős-Rényi side-observation graphs

**Authors:** Tomáš Kocák, Gergely Neu, Michal Valko

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25271v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25271v1)

**Summary:** We consider adversarial multi-armed bandit problems where the learner is allowed to observe losses of a number of arms beside the arm that it actually chose. We study the case where all non-chosen arms reveal their loss with a fixed but unknown probability $r$, independently of each other and the action of the learner. We propose two algorithms that work for different ranges of $r$. We show that after $T$ rounds in a bandit problem with $N$ arms, the expected regret of our first algorithm is $O(...

---

### 47. Online combinatorial optimization with stochastic decision sets and adversarial losses

**Authors:** Gergely Neu, Michal Valko

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25269v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25269v1)

**Summary:** Most work on sequential learning assumes a fixed set of actions that are available all the time. However, in practice, actions can consist of picking subsets of readings from sensors that may break from time to time, road segments that can be blocked or goods that are out of stock. In this paper we study learning algorithms that are able to deal with stochastic availability of such unreliable composite actions. We propose and analyze algorithms based on the Follow-The-Perturbed-Leader prediction...

---

### 48. DGLight: DQN-Guided GRPO Fine-Tuning of Large Language Models for Traffic Signal Control

**Authors:** Chenbo Yu

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25259v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25259v1)

**Summary:** Traffic signal control (TSC) plays a central role in reducing congestion and maintaining urban mobility. This dissertation introduces DGLight, a critic-guided reinforcement-learning framework for adapting a pretrained large language model to TSC. DGLight first trains a CoLight-based Deep Q-Network critic to estimate traffic-aware action values from structured intersection states, then uses the frozen critic to score candidate language-model actions and optimize the policy with Group Relative Pol...

---

### 49. Learning Structure, Energy, and Dynamics: A Survey of Artificial Intelligence for Protein Dynamics

**Authors:** Haocheng Tang, Liang Shi, Ya-Shi Zhang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25244v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25244v1)

**Summary:** Protein dynamics underlie many biological functions, yet remain difficult to characterize due to the high computational cost of molecular dynamics simulations and the scarcity of dynamic structural data. This survey reviews recent advances in artificial intelligence for protein dynamics from three perspectives: learning from structural ensembles and trajectories, learning from physical energy signals, and learning to accelerate molecular simulations. We summarize representative methods for confo...

---

### 50. Categorical Optimization with Bayesian Anchored Latent Trust Regions for Structural Design under High-Dimensional Uncertainty

**Authors:** Zhangyong Liang, Huanhuan Gao

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25241v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25241v1)

**Summary:** Categorical structural optimization under aleatoric uncertainty is challenging because each design variable must be selected from a finite catalog of admissible instances, while each candidate design may require expensive stochastic finite-element evaluations.   Existing latent-space optimization strategies can reduce the dimensionality of catalog attributes, but they often treat the reduced space as a continuous search domain.   The resulting continuous optimum must then be rounded off to a nea...

---

## cs.NE

**50 papers**

### 1. EvoTSC: Evolving Feature Learning Models for Time Series Classification via Genetic Programming

**Authors:** Xuanhao Yang, Bing Xue, Mengjie Zhang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25499v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25499v1)

**Summary:** Time series classification is an important analytical task across diverse domains. However, its practical application is often hindered by the scarcity of labeled data and the requirement for substantial computational resources. To address these challenges, this paper proposes EvoTSC, a novel genetic programming approach designed to automatically evolve lightweight feature learning models for time series classification. The core of EvoTSC is a carefully designed multi-layer program structure tha...

---

### 2. Benchmarking Stopping Criteria for Evolutionary Multi-objective Optimization

**Authors:** Kenji Kitamura, Ryoji Tanabe

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25458v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25458v1)

**Summary:** Stopping criteria automatically determine when to stop an evolutionary algorithm, so as not to waste function evaluations on a stagnant population. Although stopping criteria play an important role in real-world applications, they have attracted little attention in the evolutionary multi-objective optimization (EMO) community. In fact, new stopping criteria for EMO have been rarely developed in recent years. One reason for the stagnation in developing stopping criteria for EMO is a lack of effec...

---

### 3. The Effects of Population Size on the Performance of BEAGLE GPU-Based Genetic Programming Runs

**Authors:** Nathan Haut, Ilya Basin, Ruchika Gupta, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24968v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24968v1)

**Summary:** The Beagle framework, through GPU-based Genetic Programming, enables population dynamics previously unattainable (within practical time frames) by CPU-constrained Genetic Programming systems. This work explores how GPU-enabled population sizes impact the success of training for symbolic regression problems. Specifically, when using constant population sizes, we see benefits of using very narrow and deep searches (as narrow as 1000 individuals) for some problems, while other problems benefit from...

---

### 4. Deployment-Aligned Low-Precision Neural Architecture Search for Spaceborne Edge AI

**Authors:** Parampuneet Kaur Thind, Vaibhav Katturu, Giacomo Zema, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24492v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24492v1)

**Summary:** Designing deep networks that meet strict latency and accuracy constraints on edge accelerators increasingly relies on hardware-aware optimization, including neural architecture search (NAS) guided by device-level metrics. Yet most hardware-aware NAS pipelines still optimize architectures under full-precision assumptions and apply low-precision adaptation only after the search, leading to a mismatch between optimization-time behavior and deployment-time execution on low-precision hardware that ca...

---

### 5. SeaEvo: Advancing Algorithm Discovery with Strategy Space Evolution

**Authors:** Sichun Luo, Yi Huang, Haochen Luo, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24372v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24372v1)

**Summary:** LLM-guided evolutionary search has emerged as a promising paradigm for automated algorithm discovery, yet most systems track search progress primarily through executable programs and scalar fitness. Even when natural-language reflection is used, it is often used locally in mutation prompts or stored without an explicit population-level organization of strategic directions. As a result, evolutionary search can struggle to distinguish syntactically different implementations of the same idea, prese...

---

### 6. Primitive Recursion without Composition: Dynamical Characterizations, from Neural Networks to Polynomial ODEs

**Authors:** Olivier Bournez

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24356v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24356v1)

**Summary:** What do recurrent neural networks, polynomial ODEs, and discrete polynomial maps each bring to computation, and what do they lack? All three operate over the continuum--real-valued states evolved by real-valued dynamics--even when the target functions are discrete. We study them through primitive recursion.   We prove that primitive recursion admits equivalent characterizations in all three frameworks: bounded iteration of a fixed recurrent ReLU network, robust computation by a fixed polynomial ...

---

### 7. Necessary and sufficient conditions for universality of Kolmogorov-Arnold networks

**Authors:** Vugar Ismailov

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23765v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23765v1)

**Summary:** We analyze the universal approximation property of Kolmogorov-Arnold Networks (KANs) in terms of their edge functions. If these functions are all affine, then universality clearly fails. How many non-affine functions are needed, in addition to affine ones, to ensure universality? We show that a single one suffices. More precisely, we prove that deep KANs in which all edge functions are either affine or equal to a fixed continuous function $σ$ are dense in $C(K)$ for every compact set $K\subset\m...

---

### 8. Learn&Drop: Fast Learning of CNNs based on Layer Dropping

**Authors:** Giorgio Cruciata, Luca Cruciata, Liliana Lo Presti, et al.

**Published:** 2026-04-25

🔗 [Paper](http://arxiv.org/abs/2604.23403v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23403v1)

**Summary:** This paper proposes a new method to improve the training efficiency of deep convolutional neural networks. During training, the method evaluates scores to measure how much each layer's parameters change and whether the layer will continue learning or not. Based on these scores, the network is scaled down such that the number of parameters to be learned is reduced, yielding a speed up in training. Unlike state-of-the-art methods that try to compress the network to be used in the inference phase o...

---

### 9. Why Architecture Choice Matters in Symbolic Regression

**Authors:** Chakshu Gupta

**Published:** 2026-04-25

🔗 [Paper](http://arxiv.org/abs/2604.23256v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23256v1)

**Summary:** Symbolic regression discovers mathematical formulas from data. Some methods fix a tree of operators, assign learnable weights, and train by gradient descent. The tree's structure, which determines what operators and variables appear at each position, is chosen once and applied to every target. This paper tests whether that choice affects which targets are actually recovered. Three structures are compared, all sharing the same operator and target language but differing in how variables enter the ...

---

### 10. A Multiplication-Free Spike-Time Learning Algorithm and its Efficient FPGA Implementation for On-Chip SNN Training

**Authors:** Maryam Mirsadeghi, Mojtaba Mirbagheri, Saeed Reza Kheradpisheh

**Published:** 2026-04-25

🔗 [Paper](http://arxiv.org/abs/2604.23218v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23218v1)

**Summary:** Spiking Neural Networks (SNNs) offer a biologically inspired foundation for low-power, event-driven intelligence, yet their direct on-chip supervised training remains a key hardware challenge. This paper presents a multiplication-free, spike-time-based learning algorithm specifically designed for efficient FPGA realization. The proposed approach eliminates floating-point arithmetic and explicit gradient storage, enabling a fully event-driven, digital training pipeline. Implemented on a Xilinx Ar...

---

### 11. Collocation-based Robust Physics Informed Neural Networks for time-dependent simulations of pollution propagation under thermal inversion conditions on Spitsbergen

**Authors:** Leszek Siwik, Maciej Sikora, Natalia Leszczyńska, et al.

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.23003v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23003v1)

**Summary:** In this paper, we propose a Physics-Informed Neural Network framework for time-dependent simulations of pollution propagation originating from moving emission sources. We formulate a robust variational framework for the time-dependent advection-diffusion problem and establish the boundedness and inf-sup stability of the corresponding discrete weak formulation. Based on this mathematical foundation, we construct a robust loss function that is directly related to the true approximation error, defi...

---

### 12. Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction

**Authors:** Yongxiang Lian, Yueyang Cang, Pingge Hu, et al.

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.22649v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22649v1)

**Summary:** Objective: Decoding visual information from electroencephalography (EEG) is an important problem in neuroscience and brain-computer interface (BCI) research. Existing methods are largely restricted to natural images and categorical representations, with limited capacity to capture structural features and to differentiate objective perception from subjective cognition. We propose a Structure-Guided Diffusion Model (SGDM) that incorporates explicit structural information for EEG-based visual recon...

---

### 13. HubRouter: A Pluggable Sub-Quadratic Routing Primitive for Hybrid Sequence Models

**Authors:** Abhinaba Basu

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.22442v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22442v1)

**Summary:** We introduce HubRouter, a pluggable module that replaces O(n^2) attention layers with O(nM) hub-mediated routing, where M << n is a small number of learned hub tokens. We demonstrate it in two from-scratch architectures: a Jamba-style hybrid and a 12-layer Transformer; retrofit into pretrained models is a tested negative case. HubRouter implements an encode-decode-score-council pipeline: M learned hubs cross-attend to all tokens, tokens project against hubs for routing fingerprints, a score head...

---

### 14. A Co-Evolutionary Theory of Human-AI Coexistence: Mutualism, Governance, and Dynamics in Complex Societies

**Authors:** Somyajit Chakraborty

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.22227v2) | 📄 [PDF](https://arxiv.org/pdf/2604.22227v2)

**Summary:** Classical robot ethics is often framed around obedience, most famously through Asimov's laws. This framing is too narrow for contemporary AI systems, which are adaptive, generative, embodied, and embedded in physical, psychological, and social worlds. We argue that future human-AI relations should be understood not as master-tool obedience, but as conditional mutualism under governance: a co-evolutionary relationship in which humans and AI systems can develop, specialize, and coordinate while in...

---

### 15. LTBs-KAN: Linear-Time B-splines Kolmogorov-Arnold Networks

**Authors:** Eduardo Said Merin-Martinez, Andres Mendez-Vazquez, Eduardo Rodriguez-Tello

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.22034v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22034v1)

**Summary:** Kolmogorov-Arnold Networks (KANs) are a recent neural network architecture offering an alternative to Multilayer Perceptrons (MLPs) with improved explainability and expressibility. However, KANs are significantly slower than MLPs due to the recursive nature of B-spline function computations, limiting their application. This work addresses these issues by proposing a novel base-spline Linear-Time B-splines Kolmogorov-Arnold Network (LTBs-KAN) with linear complexity. Unlike previous methods that r...

---

### 16. L-System Genetic Encoding for Scalable Neural Network Evolution: A Comparison with Direct Matrix Encoding

**Authors:** Alexander Stuy, Nodin Weddington

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.22000v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22000v1)

**Summary:** An artificial world of barriers and plains scattered with food is used to test the feasibility of using genetic algorithms to optimize hebbian neural networks to perform on problems without apriori knowledge of the problem domain. A formal L-System based genetic alphabet for neural networks, titled Lsys, and a neural network genetic modeling tool titled Wp1hgn are introduced. Lsys and Matrix neural network topology genetic encoding methods are compared across 24 experimental runs. Lsys encoding ...

---

### 17. Multi-Task Optimization over Networks of Tasks

**Authors:** Julian Hatzky, Thomas Bartz-Beielstein, A. E. Eiben, et al.

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.21991v1) | 📄 [PDF](https://arxiv.org/pdf/2604.21991v1)

**Summary:** Multi-task optimization is a powerful approach for solving a large number of tasks in parallel. However, existing algorithms face distinct limitations: Population-based methods scale poorly and remain underexplored for large task sets. Approaches that do scale beyond a thousand tasks are mostly MAP-Elites variants and rely on a fixed, discretized archive that disregards the topology of the task space. We introduce MONET (Multi-Task Optimization over Networks of Tasks), a multi-task optimization ...

---

### 18. Neuromorphic Computing Based on Parametrically-Driven Oscillators and Frequency Combs

**Authors:** Mahadev Sunil Kumar, Adarsh Ganesan

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.21861v1) | 📄 [PDF](https://arxiv.org/pdf/2604.21861v1)

**Summary:** Parametrically driven oscillators provide a natural platform for neuromorphic computation, where nonlinear mode coupling and intrinsic dynamics enable both memory and high-dimensional transformation. Here, we investigate a two-mode system exhibiting 2:1 parametric resonance and demonstrate its operation as a reservoir computer across distinct dynamical regimes, including sub-threshold, parametric resonance, and frequency-comb states. By encoding input signals into the drive amplitude and samplin...

---

### 19. Geometric Monomial (GEM): a family of rational 2N-differentiable activation functions

**Authors:** Eylon E. Krause

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.21677v1) | 📄 [PDF](https://arxiv.org/pdf/2604.21677v1)

**Summary:** The choice of activation function plays a crucial role in the optimization and performance of deep neural networks. While the Rectified Linear Unit (ReLU) remains the dominant choice due to its simplicity and effectiveness, its lack of smoothness may hinder gradient-based optimization in deep architectures. In this work we propose a family of $C^{2N}$-smooth activation functions whose gate follows a log-logistic CDF, achieving ReLU-like performance with purely rational arithmetic. We introduce t...

---

### 20. On the Role of Preprocessing and Memristor Dynamics in Reservoir Computing for Image Classification

**Authors:** Rishona Daniels, Duna Wattad, Ronny Ronen, et al.

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.21602v1) | 📄 [PDF](https://arxiv.org/pdf/2604.21602v1)

**Summary:** Reservoir computing (RC) is an emerging recurrent neural network architecture that has attracted growing attention for its low training cost and modest hardware requirements. Memristor-based circuits are particularly promising for RC, as their intrinsic dynamics can reduce network size and parameter overhead in tasks such as time-series prediction and image recognition. Although RC has been demonstrated with several memristive devices, a comprehensive evaluation of device-level requirements rema...

---

### 21. Novelty-Based Generation of Continuous Landscapes with Diverse Local Optima Networks

**Authors:** Kippei Mizuta, Shoichiro Tanaka, Shuhei Tanaka, et al.

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.21468v1) | 📄 [PDF](https://arxiv.org/pdf/2604.21468v1)

**Summary:** Local Optima Networks (LONs) represent the global structure of search spaces as graphs, but their construction requires iterative execution of a search algorithm to find local optima and approximate transitions between Basins of Attraction (BoAs). In continuous optimization, this high computational cost prevents systematic investigation of the relationship between LON features and evolutionary algorithm performance. To address this issue, we propose an alternative definition of BoAs for Max-Set ...

---

### 22. Trust-SSL: Additive-Residual Selective Invariance for Robust Aerial Self-Supervised Learning

**Authors:** Wadii Boulila, Adel Ammar, Bilel Benjdira, et al.

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.21349v1) | 📄 [PDF](https://arxiv.org/pdf/2604.21349v1)

**Summary:** Self-supervised learning (SSL) is a standard approach for representation learning in aerial imagery. Existing methods enforce invariance between augmented views, which works well when augmentations preserve semantic content. However, aerial images are frequently degraded by haze, motion blur, rain, and occlusion that remove critical evidence. Enforcing alignment between a clean and a severely degraded view can introduce spurious structure into the latent space. This study proposes a training str...

---

### 23. Focus Session: Hardware and Software Techniques for Accelerating Multimodal Foundation Models

**Authors:** Muhammad Shafique, Abdul Basit, Muhammad Abdullah Hanif, et al.

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.21952v1) | 📄 [PDF](https://arxiv.org/pdf/2604.21952v1)

**Summary:** This work presents a multi-layered methodology for efficiently accelerating multimodal foundation models (MFMs). It combines hardware and software co-design of transformer blocks with an optimization pipeline that reduces computational and memory requirements. During model development, it employs performance enhancements through fine-tuning for domain-specific adaptation. Our methodology further incorporates hardware and software techniques for optimizing MFMs. Specifically, it employs MFM compr...

---

### 24. CO$_2$ sequestration hybrid solver using isogeometric alternating-directions and collocation-based robust variational physics informed neural networks (IGA-ADS-CRVPINN)

**Authors:** Askold Vilkha, Tomasz Służalec, Marcin Łoś, et al.

**Published:** 2026-04-22

🔗 [Paper](http://arxiv.org/abs/2604.20731v1) | 📄 [PDF](https://arxiv.org/pdf/2604.20731v1)

**Summary:** This paper presents the hybrid solver for a $CO_2$ sequestration problem. The solver uses the IGA-ADS (IsoGeometric Analysis Alternating Directions solver) to compute the saturation scalar field update using the explicit method, and CRVPINN (Collocation-based Robust Variational Physics Informed Neural Networks solver) to compute the pressure scalar field. The study focuses on simulating the physical behavior of $CO_2$ in porous structures, excluding chemical reactions. The mathematical model is ...

---

### 25. Learning Hippo: Multi-attractor Dynamics and Stability Effects in a Biologically Detailed CA3 Extension of Hopfield Networks

**Authors:** Daniele Corradetti, Renato Corradetti

**Published:** 2026-04-22

🔗 [Paper](http://arxiv.org/abs/2604.20679v1) | 📄 [PDF](https://arxiv.org/pdf/2604.20679v1)

**Summary:** We present a biologically detailed extension of the classical Hopfield/Marr auto-associative memory model for CA3, implementing ten populations (two asymmetric pyramidal subtypes, eight GABAergic interneuron classes), forty-seven compartments, multi-rule plasticity (recurrent Hebb, BCM anti-saturation, mossy-fiber short-term, endocannabinoid iLTD, burst-gated Hebb), and a bimodal cholinergic encoding/consolidation cycle. Evaluated on pattern completion across auto-associative, associative, and t...

---

### 26. An explicit operator explains end-to-end computation in the modern neural networks used for sequence and language modeling

**Authors:** Anif N. Shikder, Ramit Dey, Sayantan Auddy, et al.

**Published:** 2026-04-22

🔗 [Paper](http://arxiv.org/abs/2604.20595v1) | 📄 [PDF](https://arxiv.org/pdf/2604.20595v1)

**Summary:** We establish a mathematical correspondence between state space models, a state-of-the-art architecture for capturing long-range dependencies in data, and an exactly solvable nonlinear oscillator network. As a specific example of this general correspondence, we analyze the diagonal linear time-invariant implementation of the Structured State Space Sequence model (S4). The correspondence embeds S4D, a specific implementation of S4, into a ring network topology, in which recent inputs are encoded, ...

---

### 27. Response time of lateral predictive coding and benefits of modular structures

**Authors:** Guanghui Cai, Zhen-Ye Huang, Weikang Wang, et al.

**Published:** 2026-04-22

🔗 [Paper](http://arxiv.org/abs/2604.20524v1) | 📄 [PDF](https://arxiv.org/pdf/2604.20524v1)

**Summary:** Lateral predictive coding (LPC) is a simple theoretical framework to appreciate feature detection in biological neural circuits. Recent theoretical work [Huang et al., Phys.Rev.E 112, 034304 (2025)] has successfully constructed optimal LPC networks capable of extracting non-Gaussian hidden input features by imposing the tradeoff between energetic cost and information robustness, but the resulting dynamical systems of recurrent interactions can be very slow in responding to external inputs. We in...

---

### 28. Distributional Value Estimation Without Target Networks for Robust Quality-Diversity

**Authors:** Behrad Koohy, Jamie Bayne

**Published:** 2026-04-22

🔗 [Paper](http://arxiv.org/abs/2604.20381v1) | 📄 [PDF](https://arxiv.org/pdf/2604.20381v1)

**Summary:** Quality-Diversity (QD) algorithms excel at discovering diverse repertoires of skills, but are hindered by poor sample efficiency and often require tens of millions of environment steps to solve complex locomotion tasks. Recent advances in Reinforcement Learning (RL) have shown that high Update-to-Data (UTD) ratios accelerate Actor-Critic learning. While effective, standard high-UTD algorithms typically utilise target networks to stabilise training. This requirement introduces a significant compu...

---

### 29. Neuro-evolutionary stochastic architectures in gauge-covariant neural fields

**Authors:** Rodrigo Carmo Terin

**Published:** 2026-04-22

🔗 [Paper](http://arxiv.org/abs/2604.20373v1) | 📄 [PDF](https://arxiv.org/pdf/2604.20373v1)

**Summary:** We extend our gauge-covariant stochastic neural-field framework by promoting architecture-level parameters to slow stochastic variables evolving in function space. Our effective theory is formulated in terms of classical commuting fields and provides symmetry-constrained diagnostics of marginality and finite-width effects through the maximal Lyapunov exponent, the amplification factor, and dressed spectral kernels. On top of this dynamics, we introduce a Markovian evolutionary scheme compatible ...

---

### 30. Quantization robustness from dense representations of sparse functions in high-capacity kernel associative memory

**Authors:** Akira Tamamori

**Published:** 2026-04-22

🔗 [Paper](http://arxiv.org/abs/2604.20333v1) | 📄 [PDF](https://arxiv.org/pdf/2604.20333v1)

**Summary:** High-capacity associative memories based on Kernel Logistic Regression (KLR) are known for their exceptional performance but are hindered by high computational costs. This paper investigates the compressibility of KLR-trained Hopfield networks to understand the geometric principles of its robust encoding. We provide a comprehensive geometric theory based on spontaneous symmetry breaking and Walsh analysis, and validate it with compression experiments (quantization and pruning). Our experiments r...

---

### 31. What Makes an LLM a Good Optimizer? A Trajectory Analysis of LLM-Guided Evolutionary Search

**Authors:** Xinhao Zhang, Xi Chen, François Portet, et al.

**Published:** 2026-04-21

🔗 [Paper](http://arxiv.org/abs/2604.19440v1) | 📄 [PDF](https://arxiv.org/pdf/2604.19440v1)

**Summary:** Recent work has demonstrated the promise of orchestrating large language models (LLMs) within evolutionary and agentic optimization systems. However, the mechanisms driving these optimization gains remain poorly understood. In this work, we present a large-scale study of LLM-guided evolutionary search, collecting optimization trajectories for 15 LLMs across 8 tasks. Although zero-shot problem-solving ability correlates with final optimization outcomes, it explains only part of the variance: mode...

---

### 32. Scalable Memristive-Friendly Reservoir Computing for Time Series Classification

**Authors:** Coşku Can Horuz, Andrea Ceni, Claudio Gallicchio, et al.

**Published:** 2026-04-21

🔗 [Paper](http://arxiv.org/abs/2604.19343v1) | 📄 [PDF](https://arxiv.org/pdf/2604.19343v1)

**Summary:** Memristive devices present a promising foundation for next-generation information processing by combining memory and computation within a single physical substrate. This unique characteristic enables efficient, fast, and adaptive computing, particularly well suited for deep learning applications. Among recent developments, the memristive-friendly echo state network (MF-ESN) has emerged as a promising approach that combines memristive-inspired dynamics with the training simplicity of reservoir co...

---

### 33. Large Language Models Exhibit Normative Conformity

**Authors:** Mikako Bito, Keita Nishimoto, Kimitaka Asatani, et al.

**Published:** 2026-04-21

🔗 [Paper](http://arxiv.org/abs/2604.19301v1) | 📄 [PDF](https://arxiv.org/pdf/2604.19301v1)

**Summary:** The conformity bias exhibited by large language models (LLMs) can pose a significant challenge to decision-making in LLM-based multi-agent systems (LLM-MAS). While many prior studies have treated "conformity" simply as a matter of opinion change, this study introduces the social psychological distinction between informational conformity and normative conformity in order to understand LLM conformity at the mechanism level. Specifically, we design new tasks to distinguish between informational con...

---

### 34. Neutrally Evolving Interlocking Complexity in the Quandary Den

**Authors:** Andrew Walsh

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18361v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18361v1)

**Summary:** Molecular biology features numerous complexes of proteins that coordinate in an interlocking fashion to fulfill different functions. Adaptive evolution explains some of this complexity, but needn't be the default when neutral explanations suffice. A new artificial life model ``organism,'' the Quandary Den, is introduced to explore different neutral evolution scenarios where complexity increases in the absence of greater informational needs. Two interlocking complexity scenarios emerge. Subfuncti...

---

### 35. Similarity-based Portfolio Construction for Black-box Optimization

**Authors:** Catalin-Viorel Dinu, Diederick Vermetten, Carola Doerr

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18196v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18196v1)

**Summary:** In black-box optimization, a central question is which algorithm to use to solve a given, previously unseen, problem. Selecting a single algorithm, however, entails inherent risks: inaccuracies in the selector may lead to poor choices, and even well-performing algorithms with high variance can yield unsatisfactory results in a single run. A natural remedy is to split the evaluation budget across multiple runs of potentially different algorithms. Such sequential algorithm portfolios benefit from ...

---

### 36. The Magnitude of Dominated Sets: A Pareto Compliant Indicator Grounded in Metric Geometry

**Authors:** Michael T. M. Emmerich

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18147v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18147v1)

**Summary:** We investigate \emph{magnitude} as a new unary and strictly Pareto-compliant quality indicator for finite approximation sets to the Pareto front in multiobjective optimization. Magnitude originates in enriched category theory and metric geometry, where it is a notion of size or point content for compact metric spaces and a generalization of cardinality. For dominated regions in the \(\ell_1\) box setting, magnitude is close to hypervolume but not identical: it contains the top-dimensional hyperv...

---

### 37. On Scalability of Multi-Objective Evolutionary Algorithms on Combinatorial Optimisation Problems

**Authors:** Menghao Tang, Zimin Liang, Miqing Li

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.17872v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17872v1)

**Summary:** Scalability of evolutionary algorithms refers to assessing how their performance changes as problem size increases. In the area of multi-objective optimisation, research on the scalability of multi-objective evolutionary algorithms (MOEAs) has predominantly focussed on continuous problems. However, multi-objective combinatorial optimisation problems (MOCOPs) differ from continuous ones. Their discrete and rigid structure often brings rugged landscape, numerous local optimal solutions and disjoin...

---

### 38. On the Generalization Bounds of Symbolic Regression with Genetic Programming

**Authors:** Masahiro Nomura, Ryoki Hamano, Isao Ono

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17402v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17402v1)

**Summary:** Symbolic regression (SR) with genetic programming (GP) aims to discover interpretable mathematical expressions directly from data. Despite its strong empirical success, the theoretical understanding of why GP-based SR generalizes beyond the training data remains limited. In this work, we provide a learning-theoretic analysis of SR models represented as expression trees. We derive a generalization bound for GP-style SR under constraints on tree size, depth, and learnable constants. Our result dec...

---

### 39. Monotone but Exciting: On Evolving Monotone Boolean Functions with High Nonlinearity

**Authors:** Claude Carlet, Marko Čupić, Marko Ðurasevic, et al.

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17342v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17342v1)

**Summary:** Monotone Boolean functions are a structurally important class of Boolean functions, but their restricted form imposes strong limitations on achievable nonlinearity. In this paper, we investigate whether evolutionary computation can evolve monotone Boolean functions with high nonlinearity, both in the balanced and imbalanced settings. We consider three solution encodings: the standard truth table representation, a balanced truth table encoding that preserves Hamming weight, and a symbolic tree-ba...

---

### 40. A fully parallel densely connected probabilistic Ising machine with inertia for real-time applications

**Authors:** Ruomin Zhu, Abhishek Kumar Singh, Jérémie Laydevant, et al.

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.17109v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17109v1)

**Summary:** Ising machines -- special-purpose hardware for heuristically solving Ising optimization problems -- based on probabilistic bits (p-bits) have been established as a promising alternative to heuristic optimization algorithms run on conventional computers. However, it has -- until now -- been thought that Ising spins that are connected in probabilistic Ising machines cannot be updated in parallel without ruining the machine's solving ability. This has been a major challenge for using probabilistic ...

---

### 41. When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano

**Authors:** Jason Yoo, Shailesh Garg, Souvik Chakraborty, et al.

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.17040v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17040v1)

**Summary:** Spiking neural operators are appealing for neuromorphic edge computing because event-driven substrates can, in principle, translate sparse activity into lower latency and energy. Whether that advantage survives deployment on commodity edge-GPU software stacks, however, remains unclear. We study this question on a Jetson Orin Nano 8 GB using five pretrained variable-spiking wavelet neural operator (VS-WNO) checkpoints and five matched dense wavelet neural operator (WNO) checkpoints on the Darcy r...

---

### 42. Optimising Urban Flood Resilience

**Authors:** James Mckenna, Christos Iliadis, Vassilis Glenis

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.18620v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18620v1)

**Summary:** Due to the increasing frequency and severity of storm events, driven by the escalation of anthropogenic climate change and urban expansion, there is a requirement for increasingly efficient flood risk management strategies. While Blue-Green Infrastructure (BGI) offers a sustainable solution for managing flood risk, optimal implementation is challenging. To help overcome this challenge, this study presents a novel multi-objective optimisation tool that couples a state-of-the-art hydrodynamic mode...

---

### 43. Prototype-Grounded Concept Models for Verifiable Concept Alignment

**Authors:** Stefano Colamonaco, David Debot, Pietro Barbiero, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16076v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16076v1)

**Summary:** Concept Bottleneck Models (CBMs) aim to improve interpretability in Deep Learning by structuring predictions through human-understandable concepts, but they provide no way to verify whether learned concepts align with the human's intended meaning, hurting interpretability. We introduce Prototype-Grounded Concept Models (PGCMs), which ground concepts in learned visual prototypes: image parts that serve as explicit evidence for the concepts. This grounding enables direct inspection of concept sema...

---

### 44. Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks

**Authors:** Lúcio Folly Sanches Zebendo, Eleonora Cicciarella, Michele Rossi

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15997v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15997v1)

**Summary:** Spiking neural networks (SNNs) are rapidly gaining momentum as an alternative to conventional artificial neural networks in resource constrained edge systems. In this work, we continue a recent research line on recurrent SNNs where axonal delays are learned at runtime along with the other network parameters. The first proposed approach, dubbed DelRec, demonstrated the benefit of recurrent delay learning in SNNs. Here, we extend it by advocating the use of convolutional recurrent connections in c...

---

### 45. ECG-Lens: Benchmarking ML & DL Models on PTB-XL Dataset

**Authors:** Saloni Garg, Ukant Jadia, Amit Sagtani, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15822v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15822v1)

**Summary:** Automated classification of electrocardiogram (ECG) signals is a useful tool for diagnosing and monitoring cardiovascular diseases. This study compares three traditional machine learning algorithms (Decision Tree Classifier, Random Forest Classifier, and Logistic Regression) and three deep learning models (Simple Convolutional Neural Network (CNN), Long Short-Term Memory (LSTM), and Complex CNN (ECGLens)) for the classification of ECG signals from the PTB-XL dataset, which contains 12-lead recor...

---

### 46. What Makes a Bacterial Model a Good Reservoir Computer? Predicting Performance from Separability and Similarity

**Authors:** Laura Alonso Bartolomé, Jean-Loup Faulon, Xavier Hinaut

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.19850v1) | 📄 [PDF](https://arxiv.org/pdf/2604.19850v1)

**Summary:** Biological systems are promising substrates for computation because they naturally process environmental information through complex internal dynamics. In this study, we investigate whether bacterial metabolic models can act as physical reservoirs and whether their computational performance can be predicted from dynamical properties linked to separability and similarity. We simulated the growth dynamics of five bacterial species, one yeast species, and 29 Escherichia coli single-gene deletion mu...

---

### 47. Frenetic Cat-inspired Particle Optimization: a Markov state-switching hybrid swarm optimizer with application to cardiac digital twinning

**Authors:** Jorge Sánchez, Guadalupe García-Isla, Sandra Perez-Herrero, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15761v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15761v1)

**Summary:** Designing optimizers that remain effective under tight evaluation budgets is critical in expensive black-box settings such as cardiac digital twinning. We propose Frenetic Cat-inspired Particle Optimization (FCPO), a hybrid swarm method that couples particle swarm optimization-like dynamics with an explicit-state Markov switching controller to schedule exploration and refinement operators online. FCPO integrates (i) state-conditioned bounded motion, (ii) an elite-difference global jump operator ...

---

### 48. Enhancing Discrete Particle Swarm Optimization for Hypergraph-Modeled Influence Maximization

**Authors:** Qianshi Wang, Xilong Qu, Wenbin Pei, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15746v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15746v1)

**Summary:** Influence maximization (IM) is a fundamental problem in complex network analysis, with a wide range of real-world applications. To date, existing approaches to influential node identification in IM have predominantly relied on standard graphs, failing to capture higher-order intrinsic interactions embedded in many real-world systems. Hypergraphs can be employed to better capture higher-order interactions. However, using hypergraphs may lead to an excessively large search space and increased comp...

---

### 49. Impact of leaky dynamics on predictive path integration accuracy in recurrent neural networks

**Authors:** Yanlin Zhang, Yan Zhang, Muhua Zheng, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16547v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16547v1)

**Summary:** Experimental evidence indicates that intrinsic temporal dynamics operating across multiple time scales are closely associated with the emergence of periodic spatial activity of increasing complexity. However, how information encoded in grid-like firing patterns for path integration is processed across these intrinsic time scales remains unclear. To address this question, we introduce adaptive time scales through a leak term in recurrent neural networks (RNNs), forming leaky RNNs discretized from...

---

### 50. Neuromorphic Parameter Estimation for Power Converter Health Monitoring Using Spiking Neural Networks

**Authors:** Hyeongmeen Baik, Hamed Poursiami, Maryam Parsa, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15714v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15714v1)

**Summary:** Always-on converter health monitoring demands sub-mW edge inference, a regime inaccessible to GPU-based physics-informed neural networks. This work separates spiking temporal processing from physics enforcement: a three-layer leaky integrate-and-fire SNN estimates passive component parameters while a differentiable ODE solver provides physics-consistent training by decoupling the ODE physics loss from the unrolled spiking loop. On an EMI-corrupted synchronous buck converter benchmark, the SNN re...

---

## stat.ML

**50 papers**

### 1. Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics

**Authors:** Andre Herz, Daniel Durstewitz, Georgia Koppe

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25904v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25904v1)

**Summary:** Identity teacher forcing (ITF) enables stable training of deterministic recurrent surrogates for chaotic dynamical systems and has been highly effective for dynamical systems reconstruction (DSR) with recurrent neural networks (RNNs), including interpretable almost-linear RNNs (AL-RNNs). However, as an intervention-based prediction loss (and thus a generalized Bayes update), teacher forcing need not match the free-running model's marginal likelihood geometry. We compare the objective-induced cur...

---

### 2. When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient

**Authors:** Shuning Shang, Hubert Strauss, Stanley Wei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25872v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25872v1)

**Summary:** Training language models via reinforcement learning often relies on imperfect proxy rewards, since ground truth rewards that precisely define the intended behavior are rarely available. Standard metrics for assessing the quality of proxy rewards, such as ranking accuracy, treat incorrect rewards as strictly harmful. In this work, however, we highlight that not all deviations from the ground truth are equal. By theoretically analyzing which outputs attract probability during policy gradient optim...

---

### 3. Model-agnostic information transfer and fusion for classification with label noise

**Authors:** Zhu Guojun, Zhang Sanguo, Ren Mingyang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25845v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25845v1)

**Summary:** Label noise presents a fundamental challenge in modern machine learning, especially when large-scale datasets are generated via automated processes. An increasingly common and important data paradigm, particularly in domains like medical imaging, involves learning from a large dataset with coarse, noisy labels supplemented by a small, expert-verified, clean dataset. This setting constitutes a typical information transfer and fusion problem. However, the significant distribution shift between the...

---

### 4. Magnification-Invariant Image Classification via Domain Generalization and Stable Sparse Embedding Signatures

**Authors:** Ifeanyi Ezuma, Olusiji Medaiyese

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25817v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25817v1)

**Summary:** Magnification shift is a major obstacle to robust histopathology classification, because models trained on one imaging scale often generalize poorly to another. Here, we evaluated this problem on the BreaKHis dataset using a strict patient-disjoint leave-one-magnification-out protocol, comparing supervised baseline, baseline augmented with DCGAN-generated patches, and a gradient-reversal domain-general model designed to preserve discriminative information while suppressing magnification-specific...

---

### 5. Adaptive Meta-Learning Stochastic Gradient Hamiltonian Monte Carlo Simulation for Bayesian Updating of Structural Dynamic Models

**Authors:** Xianghao Meng, James L. Beck, Yong Huang, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25710v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25710v1)

**Summary:** In the last few decades, Markov chain Monte Carlo (MCMC) methods have been widely applied to Bayesian updating of structural dynamic models in the field of structural health monitoring. Recently, several MCMC algorithms have been developed that incorporate neural networks to enhance their performance for specific Bayesian model updating problems. However, a common challenge with these approaches lies in the fact that the embedded neural networks often necessitate retraining when faced with new t...

---

### 6. Deflation-Free Optimal Scoring

**Authors:** Sharmin Afroz, Brendan Ames

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25664v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25664v1)

**Summary:** Sparse Optimal Scoring (SOS) reformulates linear discriminant analysis to enable feature selection through elastic net regularization, making it well-suited for high-dimensional settings where the number of features exceeds observations. Most existing SOS methods use deflation-based strategies that compute discriminant vectors sequentially, which can propagate errors and produce suboptimal solutions. We propose a novel approach that estimates all discriminant vectors simultaneously under an expl...

---

### 7. Residual-loss Anomaly Analysis of Physics-Informed Neural Networks: An Inverse Method for Change-point Detection in Nonlinear Dynamical Systems with Regime Switching

**Authors:** Yuhe Bai, Chengli Tan, Jiaqi Li, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25655v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25655v1)

**Summary:** Nonlinear dynamical systems with regime transitions are typically described by ordinary differential equations with jumping parameters parameters. Traditional methods often treat change-point detection and parameter estimation as separate tasks, ignoring the inherent coupling between them. To address this, we propose residual-loss anomaly analysis of physics-informed neural networks, a unified framework that leverages dynamical consistency within the physics-informed learning paradigm. This appr...

---

### 8. The optimal betting wealth growth rate

**Authors:** Ashwin Ram, Aaditya Ramdas

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25280v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25280v1)

**Summary:** This paper characterizes the best possible rate of growth of wealth in a Kelly betting game when repeatedly betting against a general i.i.d. null hypothesis $\mathscr{P}$, but the data are drawn i.i.d from an arbitrary alternative $Q$. We prove that it equals $\lim_{n \to \infty}n^{-1}\inf_{P \in (\mathscr P)^n)^{\circ\circ}} \mathrm{KL}(Q^n,P)$, where ${\mathscr P}^n = \{P^n: P \in \mathscr{P}\}$ and $(\mathscr {P}^n)^{\circ\circ}$ is its bipolar, i.e., this rate is achievable and one cannot do...

---

### 9. Spectral bandits

**Authors:** Tomáš Kocák, Rémi Munos, Branislav Kveton, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25272v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25272v1)

**Summary:** Smooth functions on graphs have wide applications in manifold and semi-supervised learning. In this work, we study a bandit problem where the payoffs of arms are smooth on a graph. This framework is suitable for solving online learning problems that involve graphs, such as content-based recommendation. In this problem, each item we can recommend is a node of an undirected graph and its expected rating is similar to the one of its neighbors. The goal is to recommend items that have high expected ...

---

### 10. Online learning with Erdős-Rényi side-observation graphs

**Authors:** Tomáš Kocák, Gergely Neu, Michal Valko

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25271v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25271v1)

**Summary:** We consider adversarial multi-armed bandit problems where the learner is allowed to observe losses of a number of arms beside the arm that it actually chose. We study the case where all non-chosen arms reveal their loss with a fixed but unknown probability $r$, independently of each other and the action of the learner. We propose two algorithms that work for different ranges of $r$. We show that after $T$ rounds in a bandit problem with $N$ arms, the expected regret of our first algorithm is $O(...

---

### 11. Online combinatorial optimization with stochastic decision sets and adversarial losses

**Authors:** Gergely Neu, Michal Valko

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25269v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25269v1)

**Summary:** Most work on sequential learning assumes a fixed set of actions that are available all the time. However, in practice, actions can consist of picking subsets of readings from sensors that may break from time to time, road segments that can be blocked or goods that are out of stock. In this paper we study learning algorithms that are able to deal with stochastic availability of such unreliable composite actions. We propose and analyze algorithms based on the Follow-The-Perturbed-Leader prediction...

---

### 12. VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation

**Authors:** Divake Kumar, Sina Tayebati, Devashri Naik, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25235v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25235v1)

**Summary:** Vision-language models (VLMs) are increasingly used as automated judges for multimodal systems, yet their scores provide no indication of reliability. We study this problem through conformal prediction, a distribution-free framework that converts a judge's point score into a calibrated prediction interval using only score-token log-probabilities, with no retraining. We present the first systematic analysis of conformal prediction for VLM-as-a-Judge across 3 judges and 14 visual task categories. ...

---

### 13. Tail allocation for conformal prediction intervals

**Authors:** Tianying Wang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25202v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25202v1)

**Summary:** We study split-conformal prediction for regression when the reported prediction set must be a single interval, at target marginal coverage $1-α$, where $α$ is the nominal miscoverage level. Under this reporting constraint, the natural conditional target is the shortest interval with conditional mass at least $1-α$, rather than an equal-tailed interval or a possibly disconnected high-probability set. We parameterize this single-interval oracle by a lower-tail allocation, which determines how the ...

---

### 14. Elite-Driven Support Vector Machines for Classification

**Authors:** Mohammad Jafari Jozani, Bahram Moeinianfar

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25158v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25158v1)

**Summary:** Support vector machines (SVMs) are a standard tool for binary classification, but their classical formulations are purely data-driven and offer no direct way to encode trusted benchmark models or structured preferences on selected subsets of the data. We propose Elite-Driven Support Vector Machines (EDSVM), a general framework that augments regularized empirical risk minimization by guiding the slack variables for a curated set of elite observations (typically the union of support vectors from o...

---

### 15. A Continuous-Time Ensemble Kalman-Bucy Smoother for Causal Inference and Model Discovery

**Authors:** Zhang Jiang, Marios Andreou, Sebastian Reich, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25157v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25157v1)

**Summary:** Data assimilation (DA) integrates observational information with model predictions to improve state estimation in complex systems. While filtering provides the basis for online forecasts by using only past and present observations, it can exhibit delays and biases when the underlying dynamics evolve rapidly or undergo regime transitions. Smoothing, which additionally incorporates future observations, provides a natural pipeline for hindcasting and reanalysis that yields an uncertainty reduction ...

---

### 16. Fractionally Supervised Classification with Maxima Nominated Samples

**Authors:** Mohammad Jafari Jozani, Jingyu Wang

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25145v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25145v1)

**Summary:** Fractionally supervised classification (FSC) offers a flexible framework for combining labeled and unlabeled data in model-based classification, but existing formulations assume simple random sampling. In many applications, however, the retained observation is an extreme order statistic from a set rather than a randomly selected unit. This is particularly appealing when the target population is rare, since maxima nomination sampling (NS) can enrich the sample with the most informative observatio...

---

### 17. Conflict Forecasting via Conformal Prediction for Markov Processes

**Authors:** Aditya Basarkar, Emmett B. Kendall, David Randahl, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25139v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25139v1)

**Summary:** Whether or not a country is at war, or experiencing escalating or deescalating levels of conflict, has massive ramifications on a country's national and foreign policy. Given a country's history of conflict, or lack thereof, future predictions about the war-status of a country are valuable information. In this paper, we present the use of conformal prediction on temporally-dependent data to obtain prediction sets of possible future conflict state-sequences. More specifically, we compare the resu...

---

### 18. Null Measurability at the Symmetrization Interface in VC Learning

**Authors:** Dhruv Gupta

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.25028v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25028v1)

**Summary:** Recent work revisiting measurability in the fundamental theorem of statistical learning imposes Borel measurability of ghost-gap suprema. We show that, at the one-sided ghost-gap interface actually used by the standard symmetrization proof, this requirement is stronger than necessary. For any Borel-parameterized concept class on a Polish domain, the bad event "there exists a hypothesis whose ghost empirical error exceeds its training empirical error by at least ε/2" is analytic. By Choquet capac...

---

### 19. A Finite Time Analysis of Thompson Sampling for Bayesian Optimization with Preferential Feedback

**Authors:** Joseph Lazzaro, Davide Buffelli, Da-shan Shiu, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.25025v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25025v1)

**Summary:** Preference feedback, in the form of pairwise comparisons rather than scalar scores, has seen increasing use in applications such as human-, laboratory-, and expert-in-the-loop design, as well as scientific discovery. We propose a Thompson Sampling (TS) approach to Bayesian optimization with preferential feedback that models comparisons using a monotone link on latent utility differences and leverages the dueling kernel induced by a base kernel. We provide a finite-time analysis showing that the ...

---

### 20. CoreFlow: Low-Rank Matrix Generative Models

**Authors:** Dongze Wu, Linglingzhi Zhu, Yao Xie

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24959v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24959v1)

**Summary:** Learning matrix-valued distributions from high-dimensional and possibly incomplete training data is challenging: ambient-space generative modeling is computationally expensive and statistically fragile when the matrix dimension is large but the sample size is limited. We propose CoreFlow, a geometry-preserving low-rank flow model that learns shared row/column subspaces across the matrix distribution, and then trains a continuous normalizing flow only on the induced low-dimensional core. CoreFlow...

---

### 21. A Unifying Framework for Unsupervised Concept Extraction

**Authors:** Chandler Squires, Pradeep Ravikumar

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24936v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24936v1)

**Summary:** Techniques for concept extraction, such as sparse autoencoders and transcoders, aim to extract high-level symbolic concepts from low-level nonsymbolic representations. When these extracted concepts are used for downstream tasks such as model steering and unlearning, it is essential to understand their guarantees, or lack thereof. In this work, we present a unified theoretical framework for unsupervised concept extraction, in which we frame the task of concept extraction as identifying a generati...

---

### 22. Transformer Approximations from ReLUs

**Authors:** Jerry Yao-Chieh Hu, Mingcheng Lu, Yi-Chen Lee, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24878v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24878v1)

**Summary:** We provide a systematic recipe for translating ReLU approximation results to softmax attention mechanism. This recipe covers many common approximation targets. Importantly, it yields target-specific, economic resource bounds beyond universal approximation statements. We showcase the recipe on multiplication, reciprocal computation, and min/max primitives. These results provide new analytical tools for analyzing softmax transformer models.

---

### 23. The Optimal Sample Complexity of Multiclass and List Learning

**Authors:** Chirag Pabbaraju

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24749v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24749v1)

**Summary:** While the optimal sample complexity of binary classification in terms of the VC dimension is well-established, determining the optimal sample complexity of multiclass classification has remained open. The appropriate complexity parameter for multiclass classification is the DS dimension, and despite significant efforts, a gap of $\sqrt{\text{DS}}$ has persisted between the upper and lower bounds on sample complexity.   Recent work by Hanneke et al. (2026) shows a novel algebraic characterization...

---

### 24. Learning to Think from Multiple Thinkers

**Authors:** Nirmit Joshi, Roey Magen, Nathan Srebro, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24737v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24737v1)

**Summary:** We study learning with Chain-of-Thought (CoT) supervision from multiple thinkers, all of whom provide correct but possibly systematically different solutions, e.g., step-by-step solutions to math problems written by different thinkers, or step-by-step execution traces of different programs solving the same problem.   We consider classes that are computationally easy to learn using CoT supervision from a single thinker, but hard to learn with only end-result supervision, i.e., without CoT (Joshi ...

---

### 25. Instrumental Variable Analysis Without Structural Equations

**Authors:** Zikai Shen, Dimitri Meunier, Houssam Zenati, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24660v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24660v1)

**Summary:** We consider debiased inference on least-squares solutions to inverse problems as a way to avoid having to assume exact solutions exist. Such assumptions are substantive and not innocuous and their failure may well imperil inference when we impose them on the statistical model. Our approach instead allows us to conduct inference on a quantity that is defined regardless of solutions existing and coincides with the usual estimands when they do. For the case of instrumental variables, this means we ...

---

### 26. Enhancing molecular dynamics with equivariant machine-learned densities

**Authors:** Mihail Bogojeski, Muhammad R. Hasyim, Leslie Vogt-Maranto, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24563v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24563v1)

**Summary:** Machine-learning interatomic potentials (MLIPs) have enabled molecular dynamics at near ab initio accuracy, yet remain limited to energies and forces by construction, leaving electronic observables such as dipole moments and polarizabilities inaccessible. We introduce DenSNet, a density-first approach to machine-learned electronic structure that learns the Hohenberg--Kohn map from nuclear configurations to the ground-state electron density. Our approach employs an SE(3)-equivariant neural networ...

---

### 27. Efficient learning by implicit exploration in bandit problems with side observations

**Authors:** Tomas Kocak, Gergely Neu, Michal Valko, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24555v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24555v1)

**Summary:** We consider online learning problems under a partial observability model capturing situations where the information conveyed to the learner is between full information and bandit feedback. In the simplest variant, we assume that in addition to its own loss, the learner also gets to observe losses of some other actions. The revealed losses depend on the learner's action and a directed observation system chosen by the environment. For this setting, we propose the first algorithm that enjoys near-o...

---

### 28. Extreme bandits

**Authors:** Alexandra Carpentier, Michal Valko

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24545v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24545v1)

**Summary:** In many areas of medicine, security, and life sciences, we want to allocate limited resources to different sources in order to detect extreme values. In this paper, we study an efficient way to allocate these resources sequentially under limited feedback. While sequential design of experiments is well studied in bandit theory, the most commonly optimized property is the regret with respect to the maximum mean reward. However, in other problems such as network intrusion detection, we are interest...

---

### 29. Stochastic simultaneous optimistic optimization

**Authors:** Michal Valko, Alexandra Carpentier, Rémi Munos

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24537v1)

**Summary:** We study the problem of global maximization of a function f given a finite number of evaluations perturbed by noise. We consider a very weak assumption on the function, namely that it is locally smooth (in some precise sense) with respect to some semi-metric, around one of its global maxima. Compared to previous works on bandits in general spaces (Kleinberg et al., 2008; Bubeck et al., 2011a) our algorithm does not require the knowledge of this semi-metric. Our algorithm, StoSOO, follows an opti...

---

### 30. Continuum-marginal optimal transport: a mesh-free kernel method

**Authors:** Yumiharu Nakano

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24226v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24226v1)

**Summary:** In this paper we study continuum-marginal optimal transport. Given a time-continuous family of probability marginals, the problem is to recover the minimum-energy velocity field whose flow reproduces every marginal. This problem is the continuum limit of the classical two-marginal Benamou--Brenier formulation, and also the deterministic limit of the Nelson problem of stochastic optimal transport. We propose a practical mesh-free solver for this problem. The weak continuity equation is embedded i...

---

### 31. Identifiability and Stability of Generative Drifting with Companion-Elliptic Kernel Families

**Authors:** Hak Geun Lee

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24196v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24196v1)

**Summary:** This paper analyzes identifiability and stability for the drifting field underlying distributional matching in the Generative Drifting framework of Deng et al. First, we introduce the class of companion-elliptic kernels, which includes the Laplace kernel and is characterized by a second-order elliptic coupling between each kernel $κ$ in this class and its companion function $η$. For each kernel in this class and each pair of Borel probability measures, we prove that the drifting field vanishes i...

---

### 32. A Divergence-Based Method for Weighting and Averaging Model Predictions

**Authors:** Olav Benjamin Vassend

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24172v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24172v1)

**Summary:** This paper uses a minimum divergence framework to introduce a new way of calculating model weights that can be used to average probabilistic predictions from statistical and machine learning models. The method is general and can be applied regardless of whether the models under consideration are fit to data using frequentist, Bayesian, or some other fitting method. The proposed method is motivated in two different ways and is shown empirically to perform better than or on a par with standard mod...

---

### 33. DecompKAN: Decomposed Patch-KAN for Long-Term Time Series Forecasting

**Authors:** Naveen Mysore

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.23968v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23968v1)

**Summary:** Accurate time series forecasting in scientific domains such as climate modeling, physiological monitoring, and energy systems benefits from both competitive predictions and model transparency. This work proposes DecompKAN, a lightweight attention-free architecture that combines trend-residual decomposition, channel-wise patching, learned instance normalization, and B-spline Kolmogorov-Arnold Network (KAN) edge functions. Each KAN edge learns an explicit, inspectable 1D scalar function over learn...

---

### 34. Conditional Score-Based Modeling of Effective Langevin Dynamics

**Authors:** Ludovico T. Giorgini

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.23952v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23952v1)

**Summary:** Stochastic reduced-order models are widely used to represent the effective dynamics of complex systems, but estimating their drift and diffusion coefficients from data remains challenging. Standard approaches often rely on short-time trajectory increments, state-space partitioning, or repeated simulation of candidate models, which become unreliable or computationally expensive for high-dimensional systems, coarse temporal sampling, or unevenly sampled data. We introduce a data-driven calibration...

---

### 35. Sliced-Regularized Optimal Transport

**Authors:** Khai Nguyen

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.23944v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23944v1)

**Summary:** We propose a new regularized optimal transport (OT) formulation, termed sliced-regularized optimal transport (SROT). Unlike entropic OT (EOT), which regularizes the transport plan toward an independent coupling, SROT regularizes it toward a smoothened sliced OT (SOT) plan. To the best of our knowledge, SROT is the first approach to leverage a version of SOT plan as a reference to improve classical OT. We provide a formal definition of SROT, derive its dual formulation, and provide a post-Bayesia...

---

### 36. Nearly Optimal Subdata Selection

**Authors:** Min Yang, Wei Zheng, John Stufken, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.23930v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23930v1)

**Summary:** When, in terms of the number of data points, the size of a dataset exceeds available computing resources, or when labeling is expensive, an attractive solution consists of selecting only some of the data points (subdata) for further consideration. A central question for selecting subdata of size $n$ from $N$ available data points is which $n$ points to select. While an answer to this question depends on the objective, one approach for a parametric model and a focus on parameter estimation is to ...

---

### 37. Gromov-Wasserstein Methods for Multi-View Relational Embedding and Clustering

**Authors:** Rafael Pereira Eufrazio, Eduardo Fernandes Montesuma, Charles Casimiro Cavalcante

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23912v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23912v1)

**Summary:** Learning low-dimensional representations from multi-view relational data is challenging when underlying geometries differ across views. We propose Bary-GWMDS, a Gromov-Wasserstein-based method that operates directly on distance matrices to learn a consensus embedding preserving shared relational structure. By leveraging intrinsic distances, the approach naturally handles nonlinear distortions across views. We also introduce Mean-GWMDS-C, a clustering-oriented formulation that averages distance m...

---

### 38. Generative Synthetic Data for Causal Inference: Pitfalls, Remedies, and Opportunities

**Authors:** Yichen Xu

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23904v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23904v1)

**Summary:** Synthetic data offers a promising tool for privacy-preserving data release, augmentation, and simulation, but its use in causal inference requires preserving more than predictive fidelity. We show that fully generative tabular synthesizers, including GAN- and LLM-based models, can achieve strong train-on-synthetic-test-on-real performance while substantially distorting causal estimands such as the average treatment effect (ATE). We formalize this failure through sensitivity and tradeoff results ...

---

### 39. Inverting Foundation Models of Brain Function with Simulation-Based Inference

**Authors:** Niels Bracher, Xavier Intes, Stefan T. Radev

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23865v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23865v1)

**Summary:** Foundation models of brain activity promise a new frontier for in silico neuroscience by emulating neural responses to complex stimuli across tasks and modalities. A natural next step is to ask whether these models can also be used in reverse. Can we recover a stimulus or its properties from synthetic brain activity? We study this question in a proof-of-concept setting using TRIBEv2. We pair the brain emulator with large language models (LLMs) that generate news headlines from linguistic paramet...

---

### 40. Causal Representation Learning from General Environments under Nonparametric Mixing

**Authors:** Ignavier Ng, Shaoan Xie, Xinshuai Dong, et al.

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23800v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23800v1)

**Summary:** Causal representation learning aims to recover the latent causal variables and their causal relations, typically represented by directed acyclic graphs (DAGs), from low-level observations such as image pixels. A prevailing line of research exploits multiple environments, which assume how data distributions change, including single-node interventions, coupled interventions, or hard interventions, or parametric constraints on the mixing function or the latent causal model, such as linearity. Despi...

---

### 41. A General Representation-Based Approach to Multi-Source Domain Adaptation

**Authors:** Ignavier Ng, Yan Li, Zijian Li, et al.

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23790v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23790v1)

**Summary:** A central problem in unsupervised domain adaptation is determining what to transfer from labeled source domains to an unlabeled target domain. To handle high-dimensional observations (e.g., images), a line of approaches use deep learning to learn latent representations of the observations, which facilitate knowledge transfer in the latent space. However, existing approaches often rely on restrictive assumptions to establish identifiability of the joint distribution in the target domain, such as ...

---

### 42. Bootstrapping with AI/ML-generated labels

**Authors:** Timothy Christensen, Silvia Goncalves, Benoit Perron

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23770v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23770v1)

**Summary:** AI/ML methods are increasingly used in economics to generate binary variables (or labels) via classification algorithms. When these generated variables are included as covariates in regressions, even small misclassification errors can induce large biases in OLS estimators and invalidate standard inference. We study whether the bootstrap can correct this bias and deliver valid inference. We first show that a seemingly natural fixed-label bootstrap, which generates data using estimated labels but ...

---

### 43. Rank, Head-Channel Non-Identifiability, and Symmetry Breaking: A Precise Analysis of Representational Collapse in Transformers

**Authors:** Giansalvo Cirrincione

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23681v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23681v1)

**Summary:** A widely cited result by Dong et al. (2021) showed that Transformers built from self-attention alone, without skip connections or feed-forward layers, suffer from rapid rank collapse: all token representations converge to a single direction. The proposed remedy was the MLP. We show that this picture, while correct in the regime studied by Dong, is incomplete in ways that matter for architectural understanding.   Three results are established. First, layer normalisation is precisely affine-rank-n...

---

### 44. High-dimensional Semi-supervised Classification via the Fermat Distance

**Authors:** Ruoxu Tan, Yiming Zang

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23573v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23573v1)

**Summary:** Semi-supervised classification, where unlabeled data are massive but labeled data are limited, often arises in machine learning applications. We address this challenge under high-dimensional data by leveraging the manifold and cluster assumptions. Based on the Fermat distance, a density-sensitive metric that naturally encodes the cluster assumption, we propose the weighted $k$-nearest neighbors (NN) classifier and multidimensional scaling (MDS)-induced classifiers. The use of MDS with a large ta...

---

### 45. On the Memorization of Consistency Distillation for Diffusion Models

**Authors:** Bingqing Jiang, Difan Zou

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23552v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23552v1)

**Summary:** Diffusion models are central to modern generative modeling, and understanding how they balance memorization and generalization is critical for reliable deployment. Recent work has shown that memorization in diffusion models is shaped by training dynamics, with generalization and memorization emerging at different stages of training. However, deployed diffusion models are often further distilled, introducing an additional training phase whose impact on memorization is not well understood. In this...

---

### 46. Probabilistic Graphical Model using Graph Neural Networks for Bayesian Inversion of Discrete Structural Component States

**Authors:** Teng Li, Stephen Wu, Yong Huang, et al.

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23514v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23514v1)

**Summary:** The health condition of components in civil infrastructures can be described by various discrete states according to their performance degradation. Inferring these states from measurable responses is typically an ill-posed inverse problem. Although Bayesian methods are well-suited to tackle such problems, computing the posterior probability density function (PDF) presents challenges. The likelihood function cannot be analytically formulated due to the unclear relationship between discrete states...

---

### 47. When Does Dynamic Preconditioning Preserve the Polyak-Ruppert CLT? A Stabilization Threshold

**Authors:** Sunyoung An, Xiaoming Huo

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23498v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23498v1)

**Summary:** Polyak-Ruppert averaging yields an asymptotically normal estimator with sandwich covariance $H^{-1}SH^{-1}$, the foundation of online inference. When the gradient step is preconditioned by a data-driven matrix $P_t$, we ask how fast $P_t$ must stabilize for the central limit theorem (CLT) to remain valid.   We resolve this via an exact preconditioner-isolating decomposition of the averaged error that confines $P_t$ to a dynamic remainder $R_n$, leaving the martingale and Taylor terms preconditio...

---

### 48. Anchored Variational Inference for Personalized Sequential Latent-State Models

**Authors:** Xingche Guo

**Published:** 2026-04-25

🔗 [Paper](http://arxiv.org/abs/2604.23454v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23454v1)

**Summary:** Sequential latent-variable models with subject-specific random effects provide a flexible framework for modeling temporally structured data with both local latent dynamics and stable between-subject heterogeneity. In such models, conditional inference for the local latent process is often tractable, but integrating over subject-specific random effects can be computationally demanding. We propose an anchored variational inference framework for efficient approximate inference in this setting. The ...

---

### 49. Inference of Online Newton Methods with Nesterov's Accelerated Sketching

**Authors:** Haoxuan Wang, Xinchen Du, Sen Na

**Published:** 2026-04-25

🔗 [Paper](http://arxiv.org/abs/2604.23436v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23436v1)

**Summary:** Reliable decision-making with streaming data requires principled uncertainty quantification of online methods. While first-order methods enable efficient iterate updates, their inference procedures still require updating proper (covariance) matrices, incurring $O(d^2)$ time and memory complexity, and are sensitive to ill-conditioning and noise heterogeneity of the problem. This costly inference task offers an opportunity for more robust second-order methods, which are, however, bottlenecked by s...

---

### 50. MCMC with Adaptive Principal-Component Transformation: Rotation-Invariant Universal Samplers for Bayesian Structural System Identification

**Authors:** Xianghao Meng, Yong Huang, James L. Beck, et al.

**Published:** 2026-04-25

🔗 [Paper](http://arxiv.org/abs/2604.23381v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23381v1)

**Summary:** Over decades, Markov chain Monte Carlo (MCMC) methods have been widely studied, with a typical application being the quantification of posterior uncertainties in Bayesian system identification of structural dynamic models. To address the issue of excessively low sampling efficiency in generic MCMC methods when applied to specific problems, researchers developed several MCMC algorithms that integrate trainable neural networks to replace and enhance their critical components. Later, meta-learning ...

---

