# arXiv Daily Digest - 2026-10-26

Total papers: 350

---

## cs.AI

**50 papers**

### 1. SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning

**Authors:** Yuhan Liu, Lianhui Qin, Shenji Wan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32978v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32978v1)

**Summary:** Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors over plausible arrangements, yet their outputs require geometric reasoning to become physically valid 3D scenes. We introduce SceneBloom, an agentic framework that combines visual layout sampling with contract-guided 3D c...

---

### 2. RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

**Authors:** Xi Chen, Fengqi Hu, Zeyu Shen, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32971v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32971v1)

**Summary:** Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions. Existing robust RL algorithms offer a rich set of mechanisms and principles, yet two major barriers limit their broader potential: limited algorithm reusability and an unclear empirical capability boundary. We introduce RobustRLlib, an algorithm-centric library and benchmark that addresses both challenges. It integrates 17 representative robust online, ...

---

### 3. DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

**Authors:** Amber Xie, Jiawei Fu, Xiaofeng Guo, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32969v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32969v1)

**Summary:** Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to collect, but their motions must be estimated and retargeted to the robot, and they do not directly provide robot actions. In this paper, we introduce DexPort, a portable data-collection interface for...

---

### 4. Beyond Discrete Tokens: Preserving Numerical Continuity in Medical Vision-Language Models

**Authors:** Dianye Huang, Jiamei Guo, Yue Zhou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32948v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32948v1)

**Summary:** Objective: To develop a unified vision-language model for prompt-conditioned quantitative ultrasound measurement that addresses the mismatch between continuous measurement targets and discrete token-based numerical prediction. Methods: This article presents HAD-VLM, a hybrid autoregressive-diffusion framework that combines autoregressive text generation with continuous measurement prediction within a shared backbone. Visual prompt tuning adapts the vision encoder to ultrasound images. A diffusio...

---

### 5. Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms

**Authors:** Yuhang Ji, Fasheng Xu, Tianjun Feng

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32945v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32945v1)

**Summary:** Large language model (LLM) platforms introducing advertising must decide how much capability ad revenue should fund and what consumers should pay to avoid ads. We study a monopolistic platform that jointly chooses costly response quality, advertising intensity, and subscription prices when advertising reduces user value but better service raises advertising returns. Three findings follow. First, when partly ad-supported and ad-free plans coexist, advertising can finance useful service for consum...

---

### 6. Yalda-Embedding: Open Development of a Competitive Persian Retrieval Model

**Authors:** Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32933v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32933v1)

**Summary:** Despite advances in multilingual text representations, effective dense retrieval for Persian remains constrained by the limited availability of language-specific training resources and compact embedding models. We present Yalda Embedding, a 595.8-million-parameter Persian retrieval model adapted from Qwen3-Embedding-0.6B using more than one million query-document pairs. On eight Persian retrieval tasks from FaMTEB, the model achieves the highest macro-average among the evaluated 0.6B models, sco...

---

### 7. SemantEq: Faithful Bidirectional Equivalence of Formal Statements

**Authors:** Xinrui Li, Pawan Sasanka Ammanamanchi, Siddharth Bhat, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32919v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32919v1)

**Summary:** Statement autoformalization translates mathematics from natural language into a proof assistant such as Lean 4, and models now do it at scale. As provers get stronger, the burden of correctness shifts from the proof to the statement, that is, to whether the formal statement faithfully translates its source. Given a trusted reference formalization, the natural test is logical equivalence, and it proves too much. $P \leftrightarrow Q$ holds trivially for any two statements $P$ and $Q$ that the lib...

---

### 8. Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations

**Authors:** Sadra Emami, Benjamin Weigell, Mohammad Reza Mousavi, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32891v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32891v1)

**Summary:** Large Language Models (LLMs) are increasingly used to optimize code for performance. This practice often assumes that improvements in execution speed naturally translate into overall lower energy consumption. We challenge this assumption empirically by measuring whether performance-optimized code produced by LLM self-refinement pipelines is also energy-efficient relative to canonical human reference solutions, and whether the energy cost of the optimization process can be offset by subsequent ex...

---

### 9. Closing the Modality Gap via Simplex-Constrained Representations

**Authors:** Shubham Gupta, Siva Reddy, Perouz Taslakian, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32890v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32890v1)

**Summary:** While multimodal contrastive models like CLIP and CLAP successfully learn shared representations, their embeddings typically exhibit a persistent \emph{modality gap}. We propose addressing this separation through a purely geometric approach: changing the embedding domain from the unit sphere, $S^{d-1}$, to the probability simplex, $Δ^{d-1}$. Although both manifolds share the same intrinsic dimension, the simplex acts as a structural prior; its nonnegative, unit-mass constraints serve as a cross-...

---

### 10. NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding

**Authors:** Nilesh Prasad Pandey, Jangseon Park, Jason Kong, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32881v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32881v1)

**Summary:** Reinforcement learning (RL) post-training improves the reasoning capabilities of large language models, but its cost is dominated by autoregressive rollout generation, which can exceed 70% of training time. Existing speculative-decoding methods are poorly suited to this setting: model-based drafters consume scarce GPU memory and may become misaligned as the policy evolves, while existing model-free methods do not explicitly exploit repetition across training epochs. We observe that recent rollou...

---

### 11. Advancing SVD-based LLM Compression via Layer-Wise Error Model Search

**Authors:** Moritz Thoma, Maximilian Groezinger, Maximilian Forstenhäusler, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32878v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32878v1)

**Summary:** Low-rank SVD-based compression offers a powerful strategy to reduce the computational costs of LLMs. However, existing methods face two key limitations: (i) global rank allocation, where uncalibrated error proxies fail to capture complex error propagation, and (ii) decomposition quality, where Fisher-based estimators suffer from severe rank collapse. In this work, we address these limitations by introducing Layer-wise Error Modeling Search (LEMS) and KFAC-SVD. LEMS advances rank allocation by in...

---

### 12. Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations

**Authors:** Anouar Imel, Jin Qi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32874v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32874v1)

**Summary:** In LLM-agent opinion simulations, each agent reports the probability that a claim is true after seeing its own previous probability and the probabilities reported by its neighbors, and that number becomes its state in the next round. If the number describes the agent's position rather than the sentence it was shown, then rewriting the claim as its complement and replacing every probability p with 1 - p should return the complementary answer, so the two reports should sum to one. We test this wit...

---

### 13. From Deliberately Constructed Systemic Representations of the World of Activity to Dialogue: A Five-Level Communication Architecture for Strong Language-Based ASI

**Authors:** Maxim Osovsky

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32869v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32869v1)

**Summary:** This paper proposes a five-level organization of message formation and understanding within thinking and activity in which ASI participates. Its central thesis is that a language model's context is fundamentally incapable of presenting the foundations of utterance formation for examination and verification. These foundations are established in advance by acquired schemas, systemic representations of the world of activity, and connections accepted as true within them. Neither context nor trained ...

---

### 14. Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery

**Authors:** Marek Masiak, Andrzej Szablewski, Nicola Cancedda, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32866v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32866v1)

**Summary:** Fine-tuning on datasets of unknown origin can create a backdoor in the trained model when the data includes poisoned examples. Difficult to localise and remove, backdoors can persist through safety training. While parameter-efficient fine-tuning methods capture the full parameter changes introduced during training, they are not easily interpretable. We present the full method of TopKLoRA, extending the preliminary proposal of Masiak et al. (2025), an interpretable-by-design LoRA variant in which...

---

### 15. PoKER: A Probability of Kill Estimation Rate Model for Air-to-Air Missiles Using Machine Learning on Stochastic Targets

**Authors:** Joao P. A. Dantas, Andre N. Costa, Diego Geraldo, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32864v1)

**Summary:** This work introduces PoKER, a novel probabilistic model engineered to optimize missile launch effectiveness in air-to-air scenarios, specifically within Beyond Visual Range (BVR) air combat. Unlike conventional Weapon Engagement Zone (WEZ) models that delineate zones based on static distances such as maximum, minimum, and no-escape ranges, PoKER applies machine learning to predict kill probabilities more accurately by integrating the stochastic behaviors of targets and missile miss distances. Th...

---

### 16. A Foundation Model for Policy In-Context Longitudinal Causal Effect Estimation

**Authors:** Wenxin Chen, Kyra Gan, Mingyu Lu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32863v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32863v1)

**Summary:** Longitudinal causal effect estimation is complicated by time-varying confounding and treatment-confounder feedback loops. Existing methods generally require data-specific nuisance-model fitting, and many are tailored to prespecified treatment sequences or prediction horizons, leading to time-consuming computation at deployment. We introduce *Policy In-Context Longitudinal causal Effect estimation with Prior-data Fitted Networks* (**PICLE-PFN**), the first foundation model for longitudinal causal...

---

### 17. Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves

**Authors:** Garima Agrawal, Prasun Das, Akshay Sarvade, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32851v1)

**Summary:** Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 services into thousands of artifacts describing scope, journeys, rules and acceptance criteria. Recovery does not confer usability. Entities like offer, eligibility, and activation recur across services under a shared vocab...

---

### 18. HarnessMM: Recursive Self-Improvement for Harness Token Efficiency

**Authors:** Yuhua Jiang, Chang Xu, Feifei Gao, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32813v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32813v1)

**Summary:** Agent harnesses repeatedly invoke reasoning after tool feedback, even when an earlier call has already fixed the next action. We introduce HarnessMM (Harness Minus Minus), a method for improving harness token efficiency through guarded decision reuse and recursive self-improvement (RSI). RSI iteratively refines companion harness configurations from training feedback, with validation selecting the configuration for deployment. A controller at the model-tool boundary reuses resolved decisions to r...

---

### 19. Multiplicative vs. Additive State Coupling in Learned Optimizer Schedules

**Authors:** M. Harper Langston, Pierre-David Letourneau, Dalton Jones, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32801v1)

**Summary:** We learn schedules for a continuous penalty relaxation of MAX-CUT by backpropagating through an unrolled classical solver. A state-blind schedule generalizes to instances substantially larger than those used for training. A state-adaptive bilinear schedule also generalizes out of distribution, outperforming its untrained baseline across 15 seeds ($t=4.1$). By contrast, an additive ablation with identical inputs and output heads is statistically indistinguishable from the bilinear model in distri...

---

### 20. Every Edge Needs a Quote: Building a Quote-Grounded Knowledge Graph of Healthcare Software Adoption with Language-Model Agents

**Authors:** Juan Felipe Duran, Arthur Tobler, Martin Vallières

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32781v1)

**Summary:** Hospitals regularly buy software that clinicians and patients depend on. Because these purchases are costly, hard to reverse and can affect patient care, buyers look for evidence of which peer institutions already use a product and which systems it connects to. This evidence is public but scattered across vendor websites, press releases and third-party pages. Language-model agents can now collect it at low cost, but the correctness of the extracted claims is difficult to establish, and a wrongly...

---

### 21. AI Alignment for Digital Democracy: Fairer Voters Representation against LLM Biases

**Authors:** Yi Qi, Srijoni Majumdar, Evangelos Pournaras

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32780v1)

**Summary:** AI representation is emerging in digital democracy, assisting in voter emulation and decision-making. Large language models (LLMs) behave differently depending on the model, the prompt context, and the voter information they receive, representing some groups more accurately than others and potentially making the emulation unfair to certain groups. We investigate demographic biases in LLM-emulated electorates: how accurately LLMs represent individual votes, whether some voter groups are represent...

---

### 22. On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models

**Authors:** Leon Sick, Lukas Hoyer, Yannick Strümpler, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32770v1)

**Summary:** On-policy self-distillation enables post-training foundation models without relying on stronger external teachers. However, existing approaches rely on ground-truth question-answer pairs, human-curated problem sets, or other supervised signals. In this work, we reformulate on-policy self-distillation as a self-training framework, driven by self-generated question-answer pairs and privileged reasoning demonstrations. We push supervision to the limit: guided solely by coarse, high-level topic desc...

---

### 23. Clean-label Poisoning Attack and Defense Game for Federated Learning in Vehicular Networks

**Authors:** Yalin E. Sagduyu, Tugba Erpek, Nathan Stephenson, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32765v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32765v1)

**Summary:** This paper studies interactions between clean-label poisoning attack and defense in vehicular networks using federated learning (FL). Basic Safety Message (BSM) classification for anomaly detection is modeled as a distributed learning problem over a vehicular network with dynamic topology. As a critical threat to FL, a feature-space clean-label attack is introduced, wherein benign samples are perturbed toward malicious feature extremes, degrading class separability while preserving labels. To co...

---

### 24. Semantic Representation for Agentic Self-Play in Automated Laboratories

**Authors:** Yves Delley, John Coller, Zachary Cutts, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32755v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32755v1)

**Summary:** Navigating complex, high-dimensional biological search spaces necessitates scalable physical and computational intelligence to explore beyond local optima through iterative self-play across ideation, experimentation, and automation. Translating experimental designs into reliable physical execution remains bottlenecked by static laboratory automation and unmodeled physical variability. To address this, we introduce VERified Infrastructure for Discovery Laboratories, or VERID, a foundational infra...

---

### 25. ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents

**Authors:** Navyansh Mahla, Sashank Vandrangi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32752v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32752v1)

**Summary:** LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introd...

---

### 26. Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection

**Authors:** Luke Beddow, George Mavroghenis, Rodrigo Chacon Quesada, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32742v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32742v1)

**Summary:** Unrecognized anomalies in critical infrastructure can rapidly cascade into catastrophic physical or operational failures. Current anomaly detection approaches often rely on direct access to the monitored system by utilizing onboard sensors, such as motor encoders, to detect anomalous states. However, legacy hardware often lacks these sensors, or strict security protocols may prohibit access altogether. We therefore present AWARE, a world model framework that is capable of anomaly detection using...

---

### 27. Agentic Hazard Mapper: Emulating Expert Map-Making with AI Agents for Risk Communication

**Authors:** Sidi Wu, Lifeng Lin, Yizi Chen, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32738v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32738v1)

**Summary:** Hazard maps are essential tools for public risk communication, preparedness, and evacuation planning, yet effective cartographic design is not always ensured due to limited access to cartographic expertise across local governments and communities. We present Agentic Hazard Mapper, a multi-agent system that automates hazard-map production by emulating professional cartographic workflows and iterative design trade-offs while adapting design decisions to different data, locations, and hazard contex...

---

### 28. Internal Discrepancy for Contrastive Learning: Generalization Bounds and Downstream Behaviors

**Authors:** Jialiang Wang, Qing Ma, Xiong Zhou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32729v1)

**Summary:** Contrastive learning has emerged as a popular paradigm for training representation models. While prior studies pursue more practical and less restrictive assumptions to enhance theoretical understanding of contrastive learning, they essentially describe the interconnections among representations within the data or induced by the function class. To encapsulate these assumptions, we propose the measure of internal discrepancy that quantifies the difference between the mean representation of positi...

---

### 29. PlayerEmbed: Learning Behavioral Fingerprint Representations from Raw Input Sequences

**Authors:** Tobias Schneider, Lorenz Sparrenberg, Priya Tomar, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32727v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32727v1)

**Summary:** Raw player input sequences in video games contain fine-grained behavior, but are high-dimensional and noisy, which makes large-scale analytics challenging. To address this, we introduce PlayerEmbed, a framework that learns compact and discriminative player embeddings using deep metric learning. Our approach uses a hybrid CNN-LSTM encoder trained on raw input sequences from 1,000 players. We evaluate the model on held-out sequences from these players and on sequences from 1,000 players entirely u...

---

### 30. Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate Science Publications

**Authors:** Aayush Acharya, Qi Zhang, Eduard Dragut, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32725v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32725v1)

**Summary:** The rapid expansion of scientific literature far outpaces the speed of manual curation, creating a fundamental bottleneck in extracting structured knowledge from scientific texts. To address this, we introduce an agentic, ontology-guided framework for knowledge graph (KG) construction. Our framework utilizes specialized agents for document understanding, information extraction, ontology conformance, and entity linking. First, an LLM extracts factual knowledge in the form of triples with explicit...

---

### 31. SP-Guide: Enhancing Aerial Vision-Language Navigation with Spatial Priors

**Authors:** Haoxiang Tang, Dong Zhou, Shen Tan, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32697v1)

**Summary:** Aerial vision-language navigation (AVLN) requires a UAV to reach a language-described target from partial egocentric observations while reasoning over large outdoor scenes. Existing approaches typically fuse view-centered RGB observations and globally anchored history maps as generic visual embeddings, leaving cross-modal spatial alignment to be learned from sparse navigation supervision. We present SP-Guide, a transformer- based goal-prediction framework that addresses this weakness of alignmen...

---

### 32. Conditional Neural Processes for Self-Supervised Goal Discovery in Action Imitation

**Authors:** Marco Gabriele Fedozzi, Yukie Nagai, Francesco Rea, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32688v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32688v1)

**Summary:** Inspired by infants' ability to learn novel tasks by imitating others, in this work we evaluate to what extent Conditional Neural Processes can autonomously learn representations of actions that are informative about their underlying goal. We show that the addition of an attention mechanism in the hidden space fosters the emergence of robust goal representations early on in the observation of an action sequence, making it a promising model for a robotic self-supervised general learner.

---

### 33. Retiming Robot Demonstrations with a Learned Speed Prior

**Authors:** Seungyong Moon, Deokjae Lee, Hansang Lee, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32676v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32676v1)

**Summary:** The pace of a robot demonstration is often determined by the teleoperator rather than by the task itself. As a result, the same motion can appear at widely different speeds across demonstrations, and policies trained on such data may inherit operator-specific timing along with task behavior. We propose to learn a speed prior directly from large-scale demonstration data. Given a task instruction, a motion path and the images along it, it predicts a distribution over execution speed along the path...

---

### 34. Do Language Models Trust Their Own Justifications? A Study on Functional Consistency

**Authors:** Alisson Rosa Pereira, Bruno Iochins Grisci

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32665v1)

**Summary:** Large Language Models (LLMs) have been widely adopted in text classification tasks, where they not only output class predictions but also generate explanations that highlight the tokens deemed most relevant for reaching the predicted label. Yet it remains unclear whether these highlighted elements are behaviorally consistent with the model's own predictions under targeted interventions, which we refer to as functional auto-consistency. While much of the literature evaluates the textual plausibil...

---

### 35. SemGeo-Gen: Unsupervised Generation of Approximate Cross-Instance Semantic-Geometric Correspondences

**Authors:** Roy Amoyal, Shira Ifergane, Oren Freifeld

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32663v1)

**Summary:** We introduce SemGeo-Gen, an unsupervised method for generating approximate cross-instance semantic-geometric supervision from weakly aligned 3D object collections. Our goal is not to recover exact point-level correspondences, which are often ambiguous across different instances and would require expensive, impractical manual supervision at scale. Instead, we automatically produce approximate correspondences that are semantically meaningful, geometrically consistent, and diverse enough to train m...

---

### 36. WiMoT: Replay-Free Continual Wi-Fi Sensing via Moment Transport

**Authors:** Chunchun Yang, Yang Cao, Zhitang Chen

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32660v1)

**Summary:** Continual Wi-Fi sensing must balance plasticity, learning new rooms or users, against stability, keeping earlier ones, yet nodes often cannot retain channel state information (CSI) for privacy and storage reasons. We propose WiMoT (Wi-Fi Moment Transport), which stores the per-class feature mean and covariance of every earlier domain instead of samples. When the representation changes, stored statistics become stale. WiMoT restricts the change to an affine map on a frozen feature basis and appli...

---

### 37. InferSlice: A Reference Architecture for SLO-driven LLM Inference over a Telco Wide-Area Network

**Authors:** Juan Parra-Ullauri, Anthony Chiu, Hari Madhukumar, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32638v1)

**Summary:** LLM inference is increasingly deployed as a core service for enterprise and interactive applications, but sovereignty, compliance, latency and resource-locality requirements can limit the suitability of centralised cloud deployments. Telco operators offer geographically distributed compute and network infrastructure for addressing these constraints. However, existing LLM serving frameworks are designed for tightly coupled data centres and provide limited support for coordinating geographically d...

---

### 38. Can AI Agents Help Robotic Engineers? Lessons from Two Focus Days in Industry

**Authors:** Salim Fares, Steffen Herbold

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32636v1)

**Summary:** Software developers increasingly use AI agents that execute multi-step programming tasks on their own. However, it is unclear if and how this transfers to robotic engineering, where engineers program industrial robots in niche, vendor-specific languages and rely on visual feedback from simulation tools. Within this paper, we report a case study on the use of AI agents by an SME that programs industrial robots. Our results show that the agent did not make the engineers more productive, with the e...

---

### 39. EditJev: System One Routing for Image Editing Models

**Authors:** Zhile Guan, Xu Jiang, Yule Duan, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32635v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32635v1)

**Summary:** Instruction-based image editing models exhibit pronounced sample-specific performance variation: different models can produce substantially different results for the same source image and editing instruction, and the best-performing model often varies across requests. These models also differ substantially in inference latency, making fixed-model deployment inefficient. We therefore study image editing model routing, which dynamically selects an editor from a candidate pool given an input image ...

---

### 40. Interpretable Singing Emotion Recognition Using Acoustic and Vocal Technique Features

**Authors:** Fotini Kiriakopoulou, Vassilis Lyberatos, Spyridon Kantarelis, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32629v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32629v1)

**Summary:** Singing emotion recognition relies predominantly on deep learning models that achieve strong performance but offer limited insight into the vocal characteristics driving emotion, of- ten overlooking the singing voice as a distinct signal. We propose an interpretable singing emotion recognition framework using a compact set of singing-specific descriptors across prosody, spec- tral features, phonetics, and vocal technique. To decode model decisions and link predictions to measurable acoustic phen...

---

### 41. LGMT: A Tool for Testing the Logical Reasoning Reliability of LLMs

**Authors:** Zenghui Zhou, Xiaoke Fang, Zheng Zheng

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32627v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32627v1)

**Summary:** Large Language Models (LLMs) increasingly serve as reasoning components in modern software systems, yet a model that answers a logical query correctly can contradict itself when the same problem is restated in an equivalent form. Static benchmarks evaluate queries in isolation and therefore fail to expose such inconsistencies. To address this limitation, we present LGMT, an open-source tool that detects reasoning inconsistencies through metamorphic relations grounded in first-order logic. Given ...

---

### 42. What Transfers Across Protein Pockets? Experience Reuse in Molecular Optimization for Agentic Structure-Based Drug Design

**Authors:** Zaifei Yang, Weiyu Chen, Yaqing Wang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32620v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32620v1)

**Summary:** LLM agents optimize a ligand in a protein pocket by editing it step by step and docking each edit. Recent agents first spend extra dockings probing the complex with controlled edits; guidance induced from these probes is reported to help more than the chemical knowledge the model already carries. The probes are then discarded with the instance that produced them, so the obvious next step is to keep them in an experience base, letting a new pocket inherit what earlier ones already paid for. Such ...

---

### 43. LLaCO: Continuous Diffusion for Large Language Models with Competition-Aware Semantic Scheduling

**Authors:** Zijian Jia, Peixuan Zhang, Genying Li, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32604v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32604v1)

**Summary:** Continuous diffusion models have emerged as a promising non-autoregressive paradigm for text generation over continuous embedding spaces. Along the continuous trajectory, the residual token identity directly shapes the denoising objective. However, the geometric trajectory misaligns with temporal progression, triggering severe temporal compression. In this paper, we show that embedding norm decay causes Euclidean distance to yield spurious overtaking, indicating that token competition must be ev...

---

### 44. Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance

**Authors:** Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32555v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32555v1)

**Summary:** LLM agents increasingly rely on external tools exposed via the Model Context Protocol (MCP), yet current benchmarks assume tools respond correctly and on time, leaving agent resilience to realistic tool failures untested. We introduce MCP-Injector, a drop-in, protocol-aware fault-injection middleware that interposes on the MCP tool-call path with controlled persistence (permanent, transient, intermittent) and seedable schedules. Its fault model is calibrated to the observed incident distribution...

---

### 45. Beyond Channel Data: Configuration-Enriched Radio Foundation Models

**Authors:** Shrihari Vasudevan, H. G. Ranjani, Raaghul Ranganathan, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32542v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32542v1)

**Summary:** This paper proposes incorporating channel configuration (CFG) information into Radio Foundation Model (RFM) pre-training and demonstrates that the resulting CFG-enriched embeddings serve as effective inductive priors for downstream tasks under label scarcity. We compare the proposed embeddings with raw channel tokens and multiple baseline models, under three different data regimes, for multiple downstream tasks --- Line-of-Sight/Non-Line-of-Sight (LoS/NLoS) classification, timing advance (TA) es...

---

### 46. StarRTT: An End-to-End Real-Time Framework for Blind Zone-Free RTT Prediction in Starlink LEO Satellite Networks

**Authors:** Jaeyong Lee, Seongjin Jeong, Yusang Park, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32540v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32540v1)

**Summary:** Low Earth Orbit (LEO) satellite mega-constellations such as Starlink require frequent handovers due to high orbital velocities, resulting in substantial Round-Trip Time (RTT) fluctuations. Accurate RTT prediction can mitigate these fluctuations, yet it fundamentally relies on continuously updated serving- satellite information. Existing serving-satellite identification methods typically complete identification only at the end of each scheduling cycle, creating an identification blind zone that l...

---

### 47. IGG: A Benchmark for Interactive GUI Grounding under Visibility Constraints

**Authors:** Kyeongseon Kim, Jiyeon Son, Tae-Hyun Oh

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32536v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32536v1)

**Summary:** GUI grounding benchmarks ask whether an agent can localize a target that is already visible in a static screenshot. Real interfaces often violate this assumption: a target may be off-screen, appear only after a state change or hover, remain occluded, or become actionable after a delay. This leaves the ability to recover target visibility unevaluated. To measure this reveal step, we introduce Interactive GUI Grounding (IGG), a benchmark in which an agent must first make the target visible through...

---

### 48. Analysing Austrian Parliamentary Speeches by Predicting Party Affiliations

**Authors:** Sarah Sulollari, Vanja Karan, Benjamin Roth

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32515v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32515v1)

**Summary:** This paper examines speech characteristics of the Austrian National Council members (CMs). We introduce analysis methodology based on a fine-tuned BERT-Model which assigns to every speech a probability distribution over Austrian parties. These are then aggregated at the speaker and party level. We perform an extensive evaluation to ensure the quality of the generated distributions prior to further analysis. Instead of considering mis-assignments of predicted parties as a performance issue, we le...

---

### 49. MusicTwins: Training Audio-Language Models to Listen like Their Persona

**Authors:** Milan Liessens Dujardin, Kevin Miao

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32495v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32495v1)

**Summary:** People differ in how they perceive music, what associations they make with it, what they like about it, and how they respond to it. Computational models intended to simulate people in environments that include music should account for these differences. Although LLMs have been shown to reproduce aspects of human behavior, whether audio-language models (ALMs) can reproduce a specific person's responses to textual and musical stimuli remains underexplored. We introduce MusicTwins, a framework that...

---

### 50. Efficient Zero-Shot Video Anomaly Detection via Signal-Aware Adaptive Fusion (SAAF)

**Authors:** Khaled Waleed Dawoud, Muhammad Haris Khan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32486v1)

**Summary:** Deploying Vision-Language Models for video anomaly detection confronts a fundamental constraint. Their semantic reasoning demands computational budgets incompatible with the scale of real-world video streams. We present Signal-Aware Adaptive Fusion (SAAF), a framework that achieves efficient zero-shot anomaly detection through three key innovations. First, we introduce a dual-signal adaptive sampler operating in semantic embedding space: a delta signal captures sudden events via frame-to-frame c...

---

## cs.CL

**50 papers**

### 1. The Language of Instruction: Genre and Generative AI

**Authors:** James E. Dobson

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32982v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32982v1)

**Summary:** This article argues that instruction-fine-tuned language models should be understood as implementing a genre, what is proposed as the instructional-conversational genre. This genre is an amalgamation of discursive language from prior conversations between generative models and humans recursively run through these massive neural networks. It is instantiated in applications through instruction fine-tuning, the inclusion of a pretext known as a system prompt, and the formalization of inputs in mark...

---

### 2. Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox

**Authors:** Federico Lucca

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32955v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32955v1)

**Summary:** Personal email agents decide, for every message, what it is, whether it is urgent, whether to draft a reply, create a task, or ignore it. Their error rate is rarely measured: the stored labels were written by the system itself. We present Foyer, a self-hosted personal inbox agent in daily use, and a measurement protocol (stratified sampling, frozen snapshots, thread-grouped splits, pre-registered hypotheses, human labels in the agent's review loop) that yields ground truth before any training. O...

---

### 3. Yalda-Embedding: Open Development of a Competitive Persian Retrieval Model

**Authors:** Yalda Taheri, Mohammad Hassan Heydari, Armon Rasooli

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32933v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32933v1)

**Summary:** Despite advances in multilingual text representations, effective dense retrieval for Persian remains constrained by the limited availability of language-specific training resources and compact embedding models. We present Yalda Embedding, a 595.8-million-parameter Persian retrieval model adapted from Qwen3-Embedding-0.6B using more than one million query-document pairs. On eight Persian retrieval tasks from FaMTEB, the model achieves the highest macro-average among the evaluated 0.6B models, sco...

---

### 4. Adaptive Frequency Threshold Byte Pair Encoding for Mixed Natural Language and Structured Symbolic Corpora

**Authors:** Pietro Di Nicco, Lucio La Cava, Andrea Tagarelli

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32921v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32921v1)

**Summary:** Modern language models rely on subwording tokenization to define the discrete units of input processing, typically using methods like Byte Pair Encoding (BPE) that treat whitespace as a fixed semantic boundary. This design is inherently limited, as many meaningful concepts---including multiword expressions and the structured environments of formal languages like LaTeX---frequently span across whitespaces. While recent superword tokenization methods attempt to address this by relaxing whitespace ...

---

### 5. Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations

**Authors:** Anouar Imel, Jin Qi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32874v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32874v1)

**Summary:** In LLM-agent opinion simulations, each agent reports the probability that a claim is true after seeing its own previous probability and the probabilities reported by its neighbors, and that number becomes its state in the next round. If the number describes the agent's position rather than the sentence it was shown, then rewriting the claim as its complement and replacing every probability p with 1 - p should return the complementary answer, so the two reports should sum to one. We test this wit...

---

### 6. J-Comm: Jacobian-Guided Latent Communication between LLM Agents

**Authors:** Xiangwei Wang, Wei Wang, Sachith Seneviratne, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32871v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32871v1)

**Summary:** Latent communication requires both an effective continuous reasoning process and an interface through which an external model can leverage its intermediate computation. We present J-Comm, a framework comprising two core components. First, a training-free Geometric Agreement for Latent Reasoning (GEAR) reweights token candidates over existing model embeddings, which monotonically optimizes geometric consensus among candidate tokens in embedding space at each step. Second, we introduce an H+J (Hid...

---

### 7. Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery

**Authors:** Marek Masiak, Andrzej Szablewski, Nicola Cancedda, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32866v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32866v1)

**Summary:** Fine-tuning on datasets of unknown origin can create a backdoor in the trained model when the data includes poisoned examples. Difficult to localise and remove, backdoors can persist through safety training. While parameter-efficient fine-tuning methods capture the full parameter changes introduced during training, they are not easily interpretable. We present the full method of TopKLoRA, extending the preliminary proposal of Masiak et al. (2025), an interpretable-by-design LoRA variant in which...

---

### 8. Communicating with the Entire Population: Machine Translation of Emergency Alerts and Warnings

**Authors:** Jen Wilson, Vipasha Bansal, William D. Lewis

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32842v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32842v1)

**Summary:** It is essential that we communicate with the entirety of an affected population during a crisis, including those who do not speak a region's dominant language(s). Commercial Translation tools offer a tempting solution to broaden access and can provide a lifeline when no other resources are available. However, Emergency response managers often operate in the dark regarding the quality and adequacy of these automated outputs. In this paper, we conduct a nationwide survey of emergency managers to u...

---

### 9. SPOOK: Sparse Pixel Optimization for Off-Manifold Knowledge in Vision Encoders

**Authors:** Ankit Gupta, Akshat Pandya, Christoph Adami, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32835v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32835v1)

**Summary:** Modern vision encoders are widely used as semantic representations, but the relationship between embedding similarity and human-visible semantics can become unclear far from the natural-image manifold. We probe this regime in a black-box setting by applying sparse pixel edits to blank canvases with a simple pixel-level hill-climbing procedure. Across ImageNet and Flickr30k, we evaluate whether these edited blank canvases can retrieve chosen targets in multimodal contrastive encoders and self-sup...

---

### 10. KrishokTech: A Bengali Agricultural Advisory System with Explicit Authorization Controls

**Authors:** Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Shakil Ahmed, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32817v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32817v1)

**Summary:** For agricultural advisory, generating an answer is only part of the problem: the system must also control unsafe requests, work with limited connectivity, and accommodate changing guidance. KRISHOKTECH is a Bengali agricultural advisory system built around an explicit authorization boundary around generation. Before retrieval, normalization and rule-based admission checks refer policy-covered high-risk requests and ask for a crop when treatment intent is underspecified. The system then binds ret...

---

### 11. Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond

**Authors:** Zheng Jiang, Yiming Chen, Houde Qian, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32802v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32802v1)

**Summary:** On-policy distillation aligns teacher feedback with a student's current behavior, yet acquiring useful supervision for multi-turn agents requires identifying both where guidance is needed and whether the student can sustain the interaction afterward. We introduce Frontier-OPD, which addresses this problem through the student's learning frontier: decision situations that remain challenging but admit useful autonomous continuation after brief teacher guidance. To operationalize this frontier, Fron...

---

### 12. Multiplicative vs. Additive State Coupling in Learned Optimizer Schedules

**Authors:** M. Harper Langston, Pierre-David Letourneau, Dalton Jones, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32801v1)

**Summary:** We learn schedules for a continuous penalty relaxation of MAX-CUT by backpropagating through an unrolled classical solver. A state-blind schedule generalizes to instances substantially larger than those used for training. A state-adaptive bilinear schedule also generalizes out of distribution, outperforming its untrained baseline across 15 seeds ($t=4.1$). By contrast, an additive ablation with identical inputs and output heads is statistically indistinguishable from the bilinear model in distri...

---

### 13. ParaTaxe: a Suite of Tools for Processing and Publishing Multi-parallel Corpora

**Authors:** Olivier Kraif, Cyrille François, Elnaz Jalilian, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32796v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32796v1)

**Summary:** Over the past fifteen years, digital tools for parallelizing and aligning textual corpora have developed significantly within the field of digital humanities. Several projects and software tools have been created to compare different translations or versions of texts. Despite these technical advances, many parallel corpora produced in academic contexts quickly become inaccessible online due to the lack of maintenance or funding. To address this gap, we present a suite of open-source tools develo...

---

### 14. Every Edge Needs a Quote: Building a Quote-Grounded Knowledge Graph of Healthcare Software Adoption with Language-Model Agents

**Authors:** Juan Felipe Duran, Arthur Tobler, Martin Vallières

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32781v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32781v1)

**Summary:** Hospitals regularly buy software that clinicians and patients depend on. Because these purchases are costly, hard to reverse and can affect patient care, buyers look for evidence of which peer institutions already use a product and which systems it connects to. This evidence is public but scattered across vendor websites, press releases and third-party pages. Language-model agents can now collect it at low cost, but the correctness of the extracted claims is difficult to establish, and a wrongly...

---

### 15. On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models

**Authors:** Leon Sick, Lukas Hoyer, Yannick Strümpler, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32770v1)

**Summary:** On-policy self-distillation enables post-training foundation models without relying on stronger external teachers. However, existing approaches rely on ground-truth question-answer pairs, human-curated problem sets, or other supervised signals. In this work, we reformulate on-policy self-distillation as a self-training framework, driven by self-generated question-answer pairs and privileged reasoning demonstrations. We push supervision to the limit: guided solely by coarse, high-level topic desc...

---

### 16. ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents

**Authors:** Navyansh Mahla, Sashank Vandrangi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32752v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32752v1)

**Summary:** LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introd...

---

### 17. The Butterfly Defects: Tracing Cooperation in LLM Agent Networks

**Authors:** Maria Sampani, Maria Lymperaiou, Angeliki Dimitriou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32726v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32726v1)

**Summary:** As large language models (LLMs) increasingly operate as interconnected agents, a fundamental question emerges: does individual cooperation translate into collective cooperation? We investigate this question through the Iterated Prisoner's Dilemma (IPD), moving from dyadic interactions to homogeneous and heterogeneous networks of open-weight LLMs. Our findings reveal that cooperation is highly sensitive to model composition and seemingly minor linguistic changes. Models that cooperate with identi...

---

### 18. Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate Science Publications

**Authors:** Aayush Acharya, Qi Zhang, Eduard Dragut, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32725v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32725v1)

**Summary:** The rapid expansion of scientific literature far outpaces the speed of manual curation, creating a fundamental bottleneck in extracting structured knowledge from scientific texts. To address this, we introduce an agentic, ontology-guided framework for knowledge graph (KG) construction. Our framework utilizes specialized agents for document understanding, information extraction, ontology conformance, and entity linking. First, an LLM extracts factual knowledge in the form of triples with explicit...

---

### 19. CounselPlex: A Stressor-Aware Full-Duplex Counseling Model

**Authors:** Yeonju Kim, Bella Godiva, Yong Man Ro

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32702v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32702v1)

**Summary:** Full-duplex speech models can listen and speak at the same time, enabling natural, low-latency interaction. In counseling, however, these models often focus on the latest utterance and lose track of the seeker's underlying problem. We call this failure Stressor Blindness. We propose CounselPlex, a stressor-aware full-duplex framework that uses two operations. CounselPlex updates a short stressor state during seeker silence and injects this state into <PAD> positions while listening. We also intr...

---

### 20. Natural Language Autoencoders Identify Without Explaining

**Authors:** Kristina Šekrst, Barbara Geld

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32691v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32691v1)

**Summary:** Natural Language Autoencoders (NLAs) express a model's internal activations in the form of readable text. The verbalizer turns an activation into an English explanation; the reconstructor then converts that explanation back into an activation, and the explanation is considered successful if the round trip brings back the original activation. We claim that this criterion evaluates whether the information is sufficient and does not address descriptive faithfulness. A sentence can contain sufficien...

---

### 21. When is more search useful? An Empirical Study of Search Utility in Quality-Aware Decoding for Machine Translation

**Authors:** Javier Garcia Gilabert, Rico Sennrich, André F. T. Martins

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32679v1)

**Summary:** Quality-Aware Decoding (QAD) improves machine translation through test-time scaling, generating multiple candidate translations and selecting the final output with a quality-aware decoder. Usually the same candidate budget N is spent on every source sentence, assuming that all inputs require the same amount of search. We show that this assumption does not hold and that the quality gain obtained from additional candidates varies across sentences. We study search utility through three quantities: ...

---

### 22. Residual Expert Routing for Text-Only Domain Adaptation of Factorized Transducer ASR

**Authors:** Shashi Kumar, Esaú Villatoro-Tello, Thibault Bañeras-Roux, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32637v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32637v1)

**Summary:** Fine-tuning the non-blank predictor of a factorized transducer on target-domain text improves recognition on that domain but degrades performance on the source domain. A single interpolation weight between base and adapted predictors cannot resolve this: the adapted predictor helps at some prefixes and hurts at others, often within one utterance. We propose conservative residual routing: the adapted predictor becomes a residual correction to the base, and a 16k-parameter gate decides at each pre...

---

### 23. PHYRD: A Living Benchmark for Reproducing and Extending Theoretical Physics Research

**Authors:** Qituan Zhang, Guo Chen, Linfeng Zhang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32575v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32575v1)

**Summary:** Large language models and agents have shown significant power in advanced physical research. In this paper, We introduce PHYRD, a living benchmark for theoretical-physics reasoning with 63 Reproduce and 43 Discover problems. Reproduce tests derivation of published results; Discover tests consequences of modified theoretical conditions. FormulaForest constructs the tasks with reference solutions and subquestion-level rubrics. Across five models, whole-problem accuracy ranges from 49.21% to 68.25%...

---

### 24. Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR

**Authors:** Shashi Kumar, Yanis Labrak, Sergio Burdisso, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32572v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32572v1)

**Summary:** Adapting ASR to a domain with only untranscribed audio typically relies on pseudo-labeling, a strong teacher transcribes the audio and a student is fine-tuned on it. Because supervised fine-tuning (SFT) treats every pseudo-label token as a target, the student inherits the teacher's errors. We show that using the same pseudo-labels as a reward reference for Group Relative Policy Optimization (GRPO) is more robust to label noise. In the banking domain, GRPO yields 29.3% to 56.2% relative WER impro...

---

### 25. Principled Nonlinear Concept Erasure and Steering

**Authors:** Idan Simai, Shauli Ravfogel, Uri Shaham

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32516v1)

**Summary:** Learned representations often encode sensitive attributes, such as gender or race, that may be undesirable or unsafe to retain. Concept erasure aims to remove this information while preserving task-relevant content. Existing methods remain incomplete: linear methods provide guarantees only against linear probes, while nonlinear methods achieve stronger empirical erasure but lack formal guarantees and often sacrifice utility. In this work, we introduce a principled conditional autoencoder framewo...

---

### 26. Analysing Austrian Parliamentary Speeches by Predicting Party Affiliations

**Authors:** Sarah Sulollari, Vanja Karan, Benjamin Roth

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32515v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32515v1)

**Summary:** This paper examines speech characteristics of the Austrian National Council members (CMs). We introduce analysis methodology based on a fine-tuned BERT-Model which assigns to every speech a probability distribution over Austrian parties. These are then aggregated at the speaker and party level. We perform an extensive evaluation to ensure the quality of the generated distributions prior to further analysis. Instead of considering mis-assignments of predicted parties as a performance issue, we le...

---

### 27. The Punjabi Geet Toxicity Dataset (PGT-FG): Fine-Grained Multimodal Annotations for Toxic Content in Punjabi Songs

**Authors:** Lakhjeet Kaur, Jaspreet Kaur, Komal Rani, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32513v1)

**Summary:** Resources for toxicity detection in Punjabi remain limited, particularly for musical content that combines linguistic and multimodal information. We present the Punjabi Geet Toxicity Dataset (PGT-FG), a segment-level resource developed to support research on toxicity detection in Punjabi musical content. The dataset was constructed from publicly available Punjabi songs collected from YouTube. An initial collection of 620 songs resulted in 465 successfully downloaded songs and 3,402 preliminary s...

---

### 28. Accordion: Elastic-Depth Inference via Fixed-Prefix Layer Looping

**Authors:** Yudong Zhang, Wei Ding, Kaili Zheng, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32492v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32492v1)

**Summary:** Large language models serve applications with diverse inference budgets, but training and maintaining separate models for each budget incurs substantial costs. Recent Looped Transformers enable flexible inference computation through parameter reuse, but maintaining strong performance across different inference budgets remains an open challenge. We introduce Accordion, a mixture-of-experts-based model that supports five inference budgets through fixed-prefix layer looping. Each budget follows a p...

---

### 29. When Agents Fail: Model or Harness--Who's to Blame?

**Authors:** Shao Zhang, Hangfan Zhang, Yuanyuan Shi, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32483v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32483v1)

**Summary:** LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models. We develop a framework combining five complementary measures: (i) Valid Completion Rate (VCR), how reliably agents finish normally and deliver evaluable results, irrespective of task correctness; (ii) Model-Harness Fit, how well a harness supports task achievement through valid ...

---

### 30. Beyond Post-Hoc Rewards: Privileged Reasoning Exploration for Multimodal Embeddings

**Authors:** Tianyu Yang, Yijun Tian, Lars Benedikt Kaesberg, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32474v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32474v1)

**Summary:** Advances in Multimodal Large Language Models (MLLMs) have driven substantial progress in multimodal embeddings. Recent methods exploit generative capabilities by augmenting embedded inputs with self-generated reasoning to produce more informative embeddings. However, conventional retrieval supervision for training embedding models specifies pairwise relevance relations without explicitly guiding the reasoning used for input augmentation. Such reasoning is neither directly observed nor uniquely d...

---

### 31. Reading Between the Layers: Cross-Modal Alignment and Representational Hierarchy in Vision Transformers

**Authors:** Sugam Karki, Raúl Vázquez, Yova Kementchedjhieva

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32463v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32463v1)

**Summary:** While large vision-language models excel at optical character recognition, it remains unclear how their underlying vision encoders process text and its meaning, and whether they support anything resembling reading comprehension. We systematically study transformer-based vision encoders, using cross-modal alignment between rendered text and visual concepts together with probing and retrieval-based analyses as a controlled window into these broader capabilities. Our layer-wise analyses span orthog...

---

### 32. Decoupling Patient Personas and Clinical Workflows: A Dual-Agent Approach to Realistic Medical Dialogue Generation

**Authors:** Qiyuan Li, Xiaomei Guo, Chao Gao, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32443v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32443v1)

**Summary:** Pre-consultation medical dialogues are essential for collecting comprehensive patient information, but are costly to obtain at scale due to privacy and ethical constraints. Existing LLM-based synthesis methods often rely on prompt engineering or rigid rules, limiting their ability to balance clinical relevance with realistic patient diversity. We propose CoRPS-Dial, a controllable dual-agent framework for pre-consultation medical dialogue synthesis that integrates patient personas with guideline...

---

### 33. SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks

**Authors:** Tianyun Zhong, Wei Wang, Jialin Li, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32441v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32441v1)

**Summary:** Large language model (LLM) agents are increasingly capable of supporting scientific workflows, but their capabilities across diverse research activities remain difficult to assess systematically. Existing benchmarks often focus on selected scientific capabilities or task types, limiting a comprehensive characterization of scientific agents' strengths and weaknesses in realistic research workflows. We introduce SCI-AGENT-EXAM, a workflow-oriented benchmark comprising 120 expert-curated tasks acro...

---

### 34. Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues

**Authors:** Juan Li, Fangshu Chang, Xinyi Jiang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32435v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32435v1)

**Summary:** Building Task-Oriented Dialogue (TOD) systems for high-value scenarios such as financial marketing requires large volumes of domain-specific dialogue data, which privacy regulations, annotation costs, and the need for expert labor make hard to obtain. User simulation offers a remedy, but existing methods target general-domain dialogue and exhibit two key limitations: insufficient modeling of domain-specific business processes and compliance constraints, and inadequate capture of the colloquial, ...

---

### 35. Cycle-of-Thought: Self-Evaluative Iterative Reasoning for Table Visual Question Answering in Document Images

**Authors:** Somraj Gautam, Gaurav Harit

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32423v1)

**Summary:** Recent advances in Vision-Language Models (VLMs) have significantly improved Visual Question Answering (VQA) performance, yet their reasoning over structured content such as tables remains inconsistent, often plagued by spatial misalignment and logical hallucinations. Existing approaches for improving table VQA typically rely on architectural modifications or expensive supervised fine-tuning (SFT), which impose high barriers to entry due to the need for large-scale, expert-annotated datasets and...

---

### 36. Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge

**Authors:** Xiaopeng Ke, Zhixin Wang, Xuebo Liu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32415v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32415v1)

**Summary:** LLM-based annotation has advanced rapidly, yet existing benchmarks remain misaligned with real-world practice. Actual annotation often involves lengthy, task-specific guidelines, and different annotators may produce divergent but reasonable judgments, especially on boundary cases, where single-labeled dataset fail to reflect this disagreement. This gap also limits existing single-agent and workflow-based annotation systems, which often lack adaptability to complex, evolving guidelines. To bridge...

---

### 37. A Broader Look into MLLM's Retrieval Heads

**Authors:** Jia Wang, Yuqing Li, Jiangnan Li, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32411v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32411v1)

**Summary:** Locating relevant evidence in long inputs is a core capability of Multimodal Large Language Models. Prior studies attribute this capability to retrieval heads, a sparse set of attention heads that transfer information from the context to the output. However, these analyses are confined to a limited set of modalities and the corresponding models. Moreover, how retrieval heads can be leveraged to enhance the model calls for further exploration. In this paper, we ask whether this mechanism expands ...

---

### 38. Acoustic and Lexical Signals for Native Language Identification of Language Learners

**Authors:** Ahmet Yavuz Uluslu, Mengjie Qian, Kate Knill, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32382v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32382v1)

**Summary:** Spoken native language (L1) identification for second language learners has traditionally relied on acoustic attributes of speech. Comparatively little attention has been paid to analysing speech transcripts for L1 traces. In this paper, we present a study of L1 identification using both speech and corresponding transcripts from a spoken learner English corpus. We compare a WavLM-based audio L1 classifier with a zero-shot GPT-4o classifier operating on transcripts and analyse their predictions a...

---

### 39. Why Full-Duplex Speech Models Collapse in Long Conversations

**Authors:** Yeonju Kim, Bella Godiva, Se Jin Park, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32349v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32349v1)

**Summary:** Full-duplex speech models listen and speak at the same time, which makes them promising for natural, open-ended conversation. But can they sustain a coherent conversation for tens of minutes? Because they generate a token every frame, even while listening, they exhaust their context windows within minutes. Yet existing benchmarks evaluate only single turns or a few conversational rounds, too short to expose the long-horizon problem. We introduce the Full-Duplex Long-Horizon Benchmark (FD-LHB), w...

---

### 40. Beyond Final Outcomes: Quantifying Claim-Level Information Dynamics in Multi-Agent LLM Interaction

**Authors:** Haocheng Jiang, Herun Wan, Yongyuan Peng, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32333v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32333v1)

**Summary:** When LLM-powered agents interact, information is repeatedly shared, expanded, and forgotten, yet multi-agent evaluation typically focuses on final task outcomes. We study such interaction as claim-level information dynamics and propose RIVER, which decomposes agent outputs into atomic claims and evaluates three complementary dimensions: convergence, exploration, and retention. Convergence captures cross-agent claim correspondence and stance alignment; exploration captures semantic breadth and ex...

---

### 41. 4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents

**Authors:** Yanhao Jia, Yi Zhu, Yiran Zhong, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32332v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32332v1)

**Summary:** Humans efficiently process multimodal streams spanning hours to years, building persistent, fine-grained spatiotemporal memories that support reasoning about and predicting long-horizon events. In contrast, existing benchmarks focus on short- and medium-context tasks, and most foundation models struggle to preserve fine-grained information over long horizons. To evaluate and improve long-horizon spatiotemporal reasoning, we introduce the LongVideo dataset and the 4DMemoryBench. LongVideo compris...

---

### 42. System One models Are Not Better Rerankers

**Authors:** Michael Dinzinger, Kanishka Ghosh Dastidar, Michael Granitzer

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32318v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32318v1)

**Summary:** System One models, or decision models, answer a question about an input with a calibrated probability instead of generated text. Within weeks of the first release, in September 2026, they were used as rerankers. We test whether the decision fine-tuning behind them makes a better reranker than plain reranker fine-tuning of the same model. For six Qwen backbones from 0.6B to 27B parameters and ten TREC DL and BEIR collections, we compare the untuned model, asked zero-shot, with its decision fine-t...

---

### 43. Many Perturbations, Shared Failure Dynamics: Tracing Direction-Sensitive Perturbation Influence in Language Models

**Authors:** Zhibo Hu, Chen Wang, Yanfeng Shu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32309v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32309v1)

**Summary:** Why can a task-preserving rewrite turn a correct answer into a failure while a larger internal change leaves the answer intact? We develop a direction-sensitive, readout-relative account of semantic fragility: heterogeneous language changes can share geometric and readout relationships without sharing an input-independent failure direction. Clean decision reserve, representation transformation, and response alignment provide complementary descriptions of this process. An exact longitudinal-trans...

---

### 44. DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks

**Authors:** Shan Peng, Shuaiqi Cheng, Miao Peng, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32305v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32305v1)

**Summary:** Multi-stage analytical tasks require LLM agents to use intermediate evidence to decide whether to continue, redirect or stop. Self-reflection, in which an agent critiques its output, is widely studied, yet a critique does not show whether evidence changed the next action. We call that capability self-restraint. Existing agent benchmarks largely measure task completion or output quality and leave it untested. DMAIC-Bench evaluates it with 97 seeded tasks across 15 industrial cases in four sectors...

---

### 45. "Not" is Not Lost in Translation: A Causal Analysis of Negation Representations in Multilingual LLMs

**Authors:** Giang Son Nguyen, Wray Buntine, Dung D. Le, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32281v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32281v1)

**Summary:** Negation occurs in every language, yet its surface realization differs drastically. Despite this, multilingual large language models (LLMs) translate negation robustly, raising the question of whether they share an underlying representation of negation across languages. We study this question in six open models across English, French, Vietnamese, and Chinese, using causal interventions on a synthetic contrastive dataset and a negation translation dataset derived from FLORES-200. Across models, w...

---

### 46. Do Halting Heads Really Save Compute in Looped Language Models?

**Authors:** Tsung-Han Wu, Minsuk Heo, Kenny Tan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32246v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32246v1)

**Summary:** Looped language models run each token through the same layers several times, and each run is one iteration. To save compute, an extra layer, the halting head, gives after each iteration the probability that the token stops there, so that easy tokens can stop early. Pretraining models from scratch, up to 1.3B parameters, we find two problems. First, heads trained on a mix of all iterations predict that tokens need under half the iterations, yet under the standard stopping rule tokens run almost e...

---

### 47. DIAL-S2ST: Learning Latency Control for Simultaneous Speech-to-Speech Translation

**Authors:** Jeongsoo Choi, Junseok Ahn, Joon Son Chung

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32214v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32214v1)

**Summary:** We propose DIAL-S2ST, a post-training method for learning inference-time latency control in simultaneous speech-to-speech translation models. Our approach reuses pretrained translation capabilities through self-distillation from lookahead predictions, while limiting the influence of large text distillation losses to account for the imitation gap. This provides supervision for earlier emission without paired target data or reward computation. To make the learned timing adjustable at inference, we...

---

### 48. Head Dimension Matters in Language Models for Long-Context Retrieval

**Authors:** Seiya Tokui, Shoichiro Yamaguchi, Sosuke Kobayashi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32213v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32213v1)

**Summary:** Multi-head attention retrieves and combines context representations through query--key interactions and value aggregation, with head dimension constraining the per-head representation space. In long-context processing, it remains unclear whether allocating a fixed parameter budget to fewer, wider heads improves information retrieval. In this paper, we investigate how head dimension affects the performance of long-context retrieval tasks. Our empirical studies reveal that pretraining loss and sho...

---

### 49. SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection

**Authors:** Jiawei Dong, Zilong Bai, Pengtian zhu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32212v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32212v1)

**Summary:** Large Language Models (LLMs) have gained widespread adoption in various natural language processing tasks, but suffer from hallucination issues where they generate unfaithful or inconsistent content. While Reinforcement Learning with Verifiable Rewards (RLVR) has shown promising applications in reasoning tasks, its application to span-level hallucination detection is challenged by localization ambiguity, reward sparsity on hard examples, and uncontrolled length inflation. To address these issues...

---

### 50. SWE-Shift: Evaluating Coding Agents in Evolving Workspaces

**Authors:** Victor Shea-Jay Huang, Rongqing Li, Zhangyue Yin, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32196v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32196v1)

**Summary:** Repository-level coding benchmarks largely assume that tasks and environments remain unchanged throughout execution. In software development, code, dependencies, runtime state, and requirements can change while an agent is still working. We introduce SWE-Shift, a benchmark for evaluating coding agents under such mid-execution changes. From the same saved history and workspace, a Clean continuation proceeds without intervention, while a matched Shifted continuation receives a task-relevant update...

---

## cs.CV

**50 papers**

### 1. SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning

**Authors:** Yuhan Liu, Lianhui Qin, Shenji Wan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32978v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32978v1)

**Summary:** Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors over plausible arrangements, yet their outputs require geometric reasoning to become physically valid 3D scenes. We introduce SceneBloom, an agentic framework that combines visual layout sampling with contract-guided 3D c...

---

### 2. UniAction: Unified Action Conditioning for World Models

**Authors:** Bowen Xue, Zizhang Li, Hong-Xing Yu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32977v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32977v1)

**Summary:** Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across separate models. We introduce UniAction, a unified action-conditioning framework that represents any action as a sparse set of action elements, each with a discrete semantic identity and a continuous spatiotemporal grounding coordinate. By mapping these coordinates directly into th...

---

### 3. FlexGlue: Sparse-to-Dense Feature Matching and Visual Disambiguation

**Authors:** Philipp Lindenberger, Paul-Edouard Sarlin, Ondrej Miksik, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32976v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32976v1)

**Summary:** To estimate correspondences across images, existing approaches match either sparse interest points, which is highly efficient but limited by repeatability, or dense pixel grids, which is robust but expensive. Furthermore, these approaches are trained with only matching pairs and thus often fail to reject unrelated pairs that exhibit visual symmetries, which is equally important in applications like Structure-from-Motion (SfM). We bridge these gaps by introducing FlexGlue, a neural network for as...

---

### 4. MiD-VLM: Detecting and Grounding Global Semantic Misinformation in Image-Caption Pairs

**Authors:** Tarunya Prasad, Bharatesh Chakravarthi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32967v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32967v1)

**Summary:** Semantic misinformation can arise when an authentic image is paired with a caption that changes or distorts its narrative. Because the image itself may contain no visible signs of manipulation, methods designed to detect pixel-level artifacts can miss these misleading image-caption pairs. We study this problem using DGM4+, a dataset designed to evaluate the detection of global scene and semantic inconsistencies. We propose a multimodal model that combines image-text representations from SigLIP w...

---

### 5. ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback

**Authors:** Zimo He, Tianyi Bian, Zizhong Yang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32966v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32966v1)

**Summary:** Learning humanoid control from monocular human videos offers a scalable way to acquire diverse whole-body behaviors. Yet, existing reconstruction-retargeting-tracking pipelines are limited in system-level scalability by separately optimized intermediate stages and cannot directly optimize reference motion executability using downstream tracking feedback. We present ViT-H, a video-to-humanoid control framework following a generation-and-tracking paradigm. ViT-H directly generates humanoid referen...

---

### 6. Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection

**Authors:** Bernardo Perrone Ribeiro, Erkut Akdag, Egor Bondarev

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32964v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32964v1)

**Summary:** Few-shot industrial anomaly detection requires modeling category-specific normality from only a handful of defect-free images. Common approaches tie inference to stored exemplars, impose rigid linear structure, or risk reproducing anomalous content. Flownomaly instead casts the problem as normal-counterpart recovery in frozen DINOv2 feature space. Given normal supports, a velocity field is learned through conditional flow matching over frozen patch tokens to transport Gaussian noise toward norma...

---

### 7. Beyond Discrete Tokens: Preserving Numerical Continuity in Medical Vision-Language Models

**Authors:** Dianye Huang, Jiamei Guo, Yue Zhou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32948v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32948v1)

**Summary:** Objective: To develop a unified vision-language model for prompt-conditioned quantitative ultrasound measurement that addresses the mismatch between continuous measurement targets and discrete token-based numerical prediction. Methods: This article presents HAD-VLM, a hybrid autoregressive-diffusion framework that combines autoregressive text generation with continuous measurement prediction within a shared backbone. Visual prompt tuning adapts the vision encoder to ultrasound images. A diffusio...

---

### 8. STROKE: Simple Sparse Structural Occlusions for Black-Box Adversarial Attacks

**Authors:** Ankit Gupta, Akshat Pandya, Paul Lin, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32932v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32932v1)

**Summary:** We introduce STROKE, a query-efficient score-based black-box adversarial attack that constructs perturbations from simple oriented rectangular occlusions. STROKE optimizes these perturbations through a lightweight greedy add-and-refine procedure. Across diverse image classifiers, STROKE achieves high attack success with low query counts at nominal 1--2\% area settings, showing favorable performance relative to existing patch-based attacks in several configurations. Matched comparisons further de...

---

### 9. LoCA: Enabling Multi-Modality in Geospatial Location Encoders

**Authors:** Panagiotis Koromilas, Eleanna Vali, Diogenis Antonopoulos, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32894v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32894v1)

**Summary:** Location encoders map geographic coordinates to high-dimensional descriptors through contrastive alignment with paired Earth Observation imagery. We prove that this construction is structurally limited: any Lipschitz location encoder produces an output of intrinsic dimension at most 2, regardless of architecture or bandwidth, which forces the contrastive loss to strictly exceed its asymptotic optimum. Empirically, joint training also collapses the encoder's embedding covariance to low rank. Alth...

---

### 10. Closing the Modality Gap via Simplex-Constrained Representations

**Authors:** Shubham Gupta, Siva Reddy, Perouz Taslakian, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32890v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32890v1)

**Summary:** While multimodal contrastive models like CLIP and CLAP successfully learn shared representations, their embeddings typically exhibit a persistent \emph{modality gap}. We propose addressing this separation through a purely geometric approach: changing the embedding domain from the unit sphere, $S^{d-1}$, to the probability simplex, $Δ^{d-1}$. Although both manifolds share the same intrinsic dimension, the simplex acts as a structural prior; its nonnegative, unit-mass constraints serve as a cross-...

---

### 11. VTRL-Med: Progressive Visual Refinement with Topology-Guided Regularization for Medical Image Clustering

**Authors:** Guangyu Meng, Pengfei Gu, Peixian Liang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32884v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32884v1)

**Summary:** Deep clustering offers a promising approach for analyzing large unlabeled medical image datasets, yet prevailing methods still face two limitations: they may neglect class-agnostic structural priors that capture object boundaries and regions, and they do not explicitly encode topological patterns (e.g., connectivity and holes). These sources of information play distinct and complementary roles: visual-structural features provide the primary discriminative representation for clustering, while top...

---

### 12. Multimodal Generative AI Assists Comprehensive Echocardiographic Interpretation

**Authors:** Yi Qin, Marawan Elbatel, Shanshan Song, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32880v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32880v1)

**Summary:** Echocardiography is the cornerstone of cardiovascular diagnostics, yet its global utility is constrained by a critical shortage of experienced interpreters. Current artificial intelligence (AI) solutions remain limited, typically operating as opaque "black boxes" or focusing on narrow tasks that fail to capture the holistic, guideline-driven reasoning of a clinician. Here we introduce EchoChat, a generative multimodal vision-language model that performs comprehensive echocardiographic analysis t...

---

### 13. OpenStripe supports open-set identification and spatial stripe profiling in wild Amur tigers

**Authors:** Yichun Peng, Yansong Li, Jin Hou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32848v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32848v1)

**Summary:** Non-invasive camera-trap monitoring of endangered wildlife requires open-set individual identification---grouping field images into identities without predefined classes or a known population size---yet pose deformation and cluttered backgrounds complicate image comparison. Here, we present OpenStripe, a multi-agent framework that reconstructs canonical two-dimensional (2D) tiger torso patterns and encodes four interpretable local stripe structures: breakpoints, bifurcations, irregular structure...

---

### 14. SPOOK: Sparse Pixel Optimization for Off-Manifold Knowledge in Vision Encoders

**Authors:** Ankit Gupta, Akshat Pandya, Christoph Adami, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32835v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32835v1)

**Summary:** Modern vision encoders are widely used as semantic representations, but the relationship between embedding similarity and human-visible semantics can become unclear far from the natural-image manifold. We probe this regime in a black-box setting by applying sparse pixel edits to blank canvases with a simple pixel-level hill-climbing procedure. Across ImageNet and Flickr30k, we evaluate whether these edited blank canvases can retrieve chosen targets in multimodal contrastive encoders and self-sup...

---

### 15. Sounding Surgical Instrument Localisation through Audio-Visual Correspondence

**Authors:** Dominic Behling, Jonas Hein, Matthias Seibold

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32816v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32816v1)

**Summary:** Surgical scene understanding is a prerequisite for context-aware and intelligent systems in the operating room. Current methods rely mostly on visual data, while acoustic sensing has shown potential to provide complementary information on surgical activity. First approaches for the localisation of surgical activity relied on microphone arrays and acoustic beamforming. This work investigates whether the active instrument can be localized from a single microphone and a camera by learning the corre...

---

### 16. CompMVR: Compression-Aware Multi-View Restoration Using Diffusion Models for Geometrically Consistent 3D Reconstruction

**Authors:** Dong-hwi Kim, Chaewon Moon, Hojun Song, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32800v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32800v1)

**Summary:** Real-world 3D reconstruction pipelines often rely on multi-view images degraded by lossy compression. While compression artifacts have been extensively studied in single-image or video restoration, their impact on multi-view geometry remains largely overlooked. In this work, we identify compression-induced cross-view geometric inconsistency as a critical failure mode, where view-dependent artifacts disrupt feature matching, dense correspondence, camera parameter estimation, and downstream 3D rec...

---

### 17. Consommé: Conditioned Token Merging for Split Inference

**Authors:** Man Ngo, Jan S. Rellermeyer

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32794v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32794v1)

**Summary:** Split inference partitions a Vision Transformer between a resource-constrained edge device and a server. However, transmitting intermediate tokens across the communication channel is costly. Deploying fine-tuned backbones to every endpoint becomes expensive as well. We study token reduction for split inference under a frozen backbone, where only a small adapter is shipped. We observe that the CLS token plays a dual role: it acts as the global summary the receiver needs for classification, and it...

---

### 18. SREdit: Scene Response Guided Appearance Editing for Projection Mapping

**Authors:** Yuqiao Xia, Yuchen Deng, Ziheng Chang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32792v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32792v1)

**Summary:** Projection-based appearance editing changes selected visual attributes of a physical object through projection mapping (PM). To display a desired appearance, PM typically uses projector compensation, which computes a projector input that counteracts the geometric and photometric distortions of the scene. Compensation can only approximate this appearance within the available projection range, and it cannot revise the appearance itself. Pretrained LLM-based image editors provide a direct way to pr...

---

### 19. Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming Video Understanding

**Authors:** Yonghui Niu, Yuhao Ji, Chang Nie, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32784v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32784v1)

**Summary:** The rapid growth of video data has created an urgent need for efficient video understanding systems that can handle long and continuous visual inputs, posing significant challenges for Multimodal Large Language Models (MLLMs) due to severe memory bottlenecks. Moreover, existing compression methods often overlook the explosive accumulation of approximation errors. To address this issue, we propose Video-MemComp, a training-free and sensitivity-aware context management framework for memory-constra...

---

### 20. SCDM-HTD: Spectral-Wise Conditional Diffusion Model for Hyperspectral Target Detection

**Authors:** Dunbin Shen, Wenfeng Kong, Jianjun Liu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32768v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32768v1)

**Summary:** Hyperspectral target detection (HTD) aims to locate and recognize objects at a fine-grained scale, playing a pivotal role in remote sensing. Despite significant progress, current HTD methods primarily focus on feature comparison while neglecting distribution learning for background-target separation, which can limit detection robustness in practical applications. This paper addresses this issue by introducing a spectral-wise conditional diffusion model that reformulates HTD as a task of generati...

---

### 21. ARENA: Active Region attENtion Aggregation for interpretable solar flare prediction

**Authors:** Luis Bauer, Annalena Kofler, Andrés Asensio Ramos, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32758v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32758v1)

**Summary:** Predicting solar flares is a challenging space-weather forecasting problem with potentially significant impacts on Earth's upper atmosphere, including disruptions to radio communications. We propose Active Region attENtion Aggregation (ARENA), a neural network architecture that predicts solar flares from a variable number of active-region cutouts while learning to identify the region most relevant to the prediction. ARENA is trained using multiple-instance learning under weak supervision, requir...

---

### 22. Cross-Architectural Feature Fusion for Coronary Artery Stenosis Detection in X-ray Angiography

**Authors:** Haobo Zhu, Mojtaba Lashgari, Jason Chai, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32730v1)

**Summary:** Coronary artery disease remains a leading cause of mortality, with stenosis detection from invasive X-ray Coronary Angiography (XCA) critical for diagnosis. Manual interpretation is time-consuming, subjective, and variable, especially under low contrast and vessel overlap. Existing deep learning methods often rely solely on detection or segmentation, limiting performance.We propose a hybrid framework, Fusion-YOLOv11-L, combining a YOLOv11-L detector with a pretrained UNet++ via a channel attenti...

---

### 23. CityLift: Compositional 3D Urban Generation from a Single Image

**Authors:** Haoran Gong, Jie Feng, Chenxu Wang

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32728v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32728v1)

**Summary:** Generating editable 3D urban scenes from a single image requires detailed building assets with a coherent spatial arrangement. Occlusion and perspective ambiguity make it difficult to infer complete building geometry together with consistent relative scales and positions. We present CityLift, a framework that generates individual textured building meshes from an urban image by coupling scene-level spatial modeling with building-level synthesis. CityLift first learns building shape and placement ...

---

### 24. Are Textual Residuals Truly Complementary? Learning Visual Complements under Semantic Superposition for Visible-Infrared Person Re-Identification

**Authors:** Xiaoyang Li, Mingming Lu, Wei Zhou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32709v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32709v1)

**Summary:** Text-enhanced visible-infrared person re-identification (VI-ReID) exploits textual descriptions to compensate for appearance cues that are weak or unavailable under infrared imaging. Existing methods construct compensation from differences between modality-oriented textual representations, implicitly assuming that textual differences are visually complementary. We revisit this assumption through semantic superposition and show that dense textual residuals may entangle useful appearance variation...

---

### 25. SP-Guide: Enhancing Aerial Vision-Language Navigation with Spatial Priors

**Authors:** Haoxiang Tang, Dong Zhou, Shen Tan, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32697v1)

**Summary:** Aerial vision-language navigation (AVLN) requires a UAV to reach a language-described target from partial egocentric observations while reasoning over large outdoor scenes. Existing approaches typically fuse view-centered RGB observations and globally anchored history maps as generic visual embeddings, leaving cross-modal spatial alignment to be learned from sparse navigation supervision. We present SP-Guide, a transformer- based goal-prediction framework that addresses this weakness of alignmen...

---

### 26. Robust Offset-Free Lane-Keeping Control Framework for Vision-Only Automated Vehicles

**Authors:** Der-Hau Lee

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32666v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32666v1)

**Summary:** Achieving accurate, real-time lane-keeping control during high-speed cornering on large-curvature roads while ensuring robust vehicle stability is a critical challenge in autonomous driving. To address this challenge, this study developed a robust offset-free model predictive control (OF-MPC) framework for vision-based autonomous vehicle lane-keeping. The regulation problem in this framework is solved using several algorithms. Numerical simulation results indicated that the interpolation-tube-ba...

---

### 27. The Answer Knows Where to Look: Zooming before MLLMs Answer under Visual-Token Budgets

**Authors:** Zhensheng Hu, Guanglong Xu, Guanqiang Hu

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32664v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32664v1)

**Summary:** Multimodal large language models (MLLMs) read images through visual tokens, and under the small per-image budgets that efficient deployment requires, the fine text of documents, charts and infographics becomes illegible. Zooming in recovers the evidence, but the region must be chosen before the model answers. We find that MLLMs know where the evidence is, but not in a form that can be read before they answer: the answer tokens localize it from the middle layers on, whereas the attention availabl...

---

### 28. SemGeo-Gen: Unsupervised Generation of Approximate Cross-Instance Semantic-Geometric Correspondences

**Authors:** Roy Amoyal, Shira Ifergane, Oren Freifeld

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32663v1)

**Summary:** We introduce SemGeo-Gen, an unsupervised method for generating approximate cross-instance semantic-geometric supervision from weakly aligned 3D object collections. Our goal is not to recover exact point-level correspondences, which are often ambiguous across different instances and would require expensive, impractical manual supervision at scale. Instead, we automatically produce approximate correspondences that are semantically meaningful, geometrically consistent, and diverse enough to train m...

---

### 29. Computational imaging through turbid, bubbly and flowing water near the telescope

**Authors:** Alexander Ingold, Sabina D. Menon, Aadhi Umamageswaran, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32646v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32646v1)

**Summary:** Cameras in the surf zone or behind ship wakes look through turbid, bubbly, moving water close to the lens, yet restoration networks are usually scored only on displayed images. We introduce a measured dataset of a telescope viewing displayed images and physical objects through a 25~mm water layer 45~mm in front of its objective, under seven combinations of flow, bubbles and turbidity, with clear-water recordings as a second reference. Because the suspension scatters light far outside the 1.3\tex...

---

### 30. EditJev: System One Routing for Image Editing Models

**Authors:** Zhile Guan, Xu Jiang, Yule Duan, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32635v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32635v1)

**Summary:** Instruction-based image editing models exhibit pronounced sample-specific performance variation: different models can produce substantially different results for the same source image and editing instruction, and the best-performing model often varies across requests. These models also differ substantially in inference latency, making fixed-model deployment inefficient. We therefore study image editing model routing, which dynamically selects an editor from a candidate pool given an input image ...

---

### 31. Earth embeddings are decomposable records of the land surface

**Authors:** Robin Young, Srinivasan Keshav

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32617v1)

**Summary:** Ecological monitoring, carbon accounting and biodiversity assessment increasingly rely on annual Earth embeddings--learned vectors that compress a year of satellite observation for every ten-meter pixel on Earth, consumed in place of the imagery itself. What these vectors mean has not been established. Here we decompose two widely used embedding products and show that they contain individual ecological features, including fire, forest clearing and crop type, validated against independent referen...

---

### 32. DriveOSS: Dataset and Benchmark for 3D Anomaly Segmentation and Open-set Semantic Segmentation in Autonomous Driving

**Authors:** Zhiran Yan, Savankumar Bhanderi, Sourabh Lolge, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32612v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32612v1)

**Summary:** Recent advances in 3D semantic segmentation have significantly improved scene understanding in autonomous driving. However, existing methods are typically developed under a closed-set assumption and evaluated under standard driving conditions, where all categories are known in advance. In real-world driving, autonomous vehicles inevitably encounter previously unseen objects, making closed-set perception insufficient for safe deployment. To address this challenge, we introduce DriveOSS, which, to...

---

### 33. Hair Segmentation and Skin Characterization on Macroscopic Dermatological Images for Laser Treatment Parameterization

**Authors:** Alex Navarro Navarro, Marc Arriaga Hidalgo, Carlos Moreno Rubio, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32609v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32609v1)

**Summary:** Current light-based devices, such as laser hair removal, intense pulsed light (IPL), vascular laser therapy, and dermatologic phototherapy, are widely used in clinical dermatology but rely heavily on subjective manual parameterization or uncalibrated point-based colorimeters. To overcome these limitations, this work presents a unified system for hair segmentation and skin characterization in macroscopic dermatological images. Unlike most existing literature that relies on dermoscopic datasets ca...

---

### 34. Standing on Open Shoulders: Regional Fine-Tuning of Open-Weight Camera-Trap Models for UK Wildlife with Modest Data and Compute

**Authors:** Paul Fergus

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32573v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32573v1)

**Summary:** Camera-trap species classification is dominated by large models from well-resourced organisations, which often lack the species-level distinctions regional conservation needs, such as native red versus invasive grey squirrels in the UK. We ask whether open weights let a small team with a modest dataset and a single GPU take a real part in AI development. We fine-tuned the open DeepFaune classifier on 28 UK classes, paired it with the unmodified MegaDetector v6, and compared the resulting DeepFau...

---

### 35. Reuse, Don't Retrain: Efficient, Modality-Versatile Geospatial Foundation Models through Feature Distillation

**Authors:** Mario Hamon, Pierre Adorni, Minh-Tan Pham

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32566v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32566v1)

**Summary:** Geospatial foundation models (GeoFMs) are costly to pretrain, yet model families often repeat this process across backbone scales and sensing modalities. We investigate feature distillation as a more efficient way to reuse existing representations. First, we distill frozen CROMA and TerraMind teachers into smaller Vision Transformers through patch-level feature matching. Across nine PANGAEA tasks, distilled TerraMind Tiny, Small, and Base outperform their scale-matched released counterparts by 2...

---

### 36. Shared Is Not Enough: Predictor Width and Factor Readability Under Masked Latent Prediction

**Authors:** Nilotpal Kakati

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32562v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32562v1)

**Summary:** Masked latent prediction methods such as I-JEPA aim to learn predictable features, but what determines which information they retain is less clear. We built a simulator in which every factor behind an image is known, so a probe can measure how readable each factor remains after training. We trained small encoders (0.7M parameters) with I-JEPA, SimCLR and BYOL on the same pairs of views and probed a factor that both views share. I-JEPA had a predictor with half the encoder's width and depth, the ...

---

### 37. HEALPix-Based Implicit Neural Compression of Omnidirectional Images

**Authors:** Yulong Cheng, Youneng Bao, Junfeng Zhou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32561v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32561v1)

**Summary:** Real-time decoding of omnidirectional images is essential for immersive virtual reality (VR) experiences. Compared with conventional transform-based learned image compression (LIC), overfitted codecs offer lower decoding complexity by representing each image with a lightweight implicit neural representation (INR). However, existing approaches typically operate on the equirectangular projection (ERP), which introduces nonuniform spherical sampling and spatial distortion, leading to redundant samp...

---

### 38. VERA-Hand: A Verified Multidimensional Benchmark for 2D Hand Pose Estimation in Third-Person Dynamic Gesture Videos

**Authors:** Gibran Benitez-Garcia, Hiroki Takahashi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32517v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32517v1)

**Summary:** Hand landmarks serve as input for gesture recognition, sign language understanding, and touchless human-computer interaction. Yet hand pose estimators are typically evaluated with frame-wise localization metrics such as PCK or MPJPE, which are computed over matched predictions and overlook missed or spurious hands, handedness errors, and temporal instability. To address these limitations, we present VERA-Hand, a benchmark that evaluates estimators using manually verified, frame-level 2D annotati...

---

### 39. Fast and Useful: Adapting Distilled Generators for Visual Learning

**Authors:** Patryk Bartkowiak, Dominik Michels, Sören Pirk, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32512v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32512v1)

**Summary:** Distilled text-to-image models generate images quickly, but classifiers trained on those images can perform substantially worse than classifiers trained on images from their slower base models. We adapt released distilled generators to produce better training data while retaining fast generation. We fit a low-rank update to the student's first prediction so that it reaches an intermediate state produced by its unguided base, then disable the update and let the unchanged student finish generation...

---

### 40. Augmentation Strategy for DINO in Glaucoma Classification

**Authors:** Ashish Kumar Meena, Chandra Sekhar Seelamantula

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32511v1)

**Summary:** Self-supervised learning (SSL) offers a promising approach to medical image representation learning, yet augmentation strategies of SSL frameworks validated on natural images do not reliably transfer to specialized medical imaging domains. We analyze DINO, a knowledge-distillation based SSL framework, and empirically demonstrate that its default augmentation strategy produces unreliable representations for retinal fundus images, degrading downstream glaucoma classification performance. Guided by...

---

### 41. Distortion-Aware Spatiotemporal Learning for Real-Time Wide-Angle Video Rectification

**Authors:** Lang Nie, Yihan Yang, Wenbo Nie, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32500v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32500v1)

**Summary:** While wide-angle lenses provide an expanded field of view (FoV), they exhibit severe nonlinear distortion near image boundaries, unnaturally stretching people in these regions. Existing methods mostly focus on facial regions, require high computational costs, and lack temporal modeling, resulting in incomplete full-body rectification, impractical real-time deployment, and noticeable inter-frame shakes. To tackle these issues, we propose \textbf{FastVC}, an efficient full-body video rectification...

---

### 42. K-CLUE: A Segmentation-to-Clustering Framework for Ki67 Cell Typing

**Authors:** Ana Beatriz Vieira, Sara P. Oliveira, Diana Montezuma, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32493v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32493v1)

**Summary:** Ki67 is a key marker of tumor proliferation in breast cancer, but its quantification from immunohistochemistry images normally depends on supervised classifiers trained per dataset. We examine the role of frozen pretrained visual representations in annotation-free Ki67 cell typing. To this end, we use K-CLUE, a framework that segments individual nuclei, represents each nucleus with a pretrained encoder, reduces the resulting embeddings with principal component analysis, and separates Ki67-positi...

---

### 43. L0-Norm-Based CycleGAN for Unpaired Brain CT-to-MR Synthesis

**Authors:** Yunxiao Zhang, Shouqiang Du, Zexian Xu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32491v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32491v1)

**Summary:** Computed tomography (CT) and magnetic resonance (MR) imaging provide complementary information for the brain, but acquiring both modalities is not always possible. The cycle-consistent adversarial network (CycleGAN) enables unpaired CT-to-MR synthesis, but because the standard L1-norm cycle?consistency penalty grows linearly with the residual magnitude, the network tends to focus on large residuals. This paper introduces an L0-norm-based cycle?consistency term, in which the L0-norm is approximat...

---

### 44. Efficient Zero-Shot Video Anomaly Detection via Signal-Aware Adaptive Fusion (SAAF)

**Authors:** Khaled Waleed Dawoud, Muhammad Haris Khan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32486v1)

**Summary:** Deploying Vision-Language Models for video anomaly detection confronts a fundamental constraint. Their semantic reasoning demands computational budgets incompatible with the scale of real-world video streams. We present Signal-Aware Adaptive Fusion (SAAF), a framework that achieves efficient zero-shot anomaly detection through three key innovations. First, we introduce a dual-signal adaptive sampler operating in semantic embedding space: a delta signal captures sudden events via frame-to-frame c...

---

### 45. PCFBench: How Far Can Large Vision-Language Models Go in Physics-aware Photonic Inverse Design?

**Authors:** Shengchao Chen, Ting Shu, Sufen Ren

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32485v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32485v1)

**Summary:** Photonic crystal fibers (PCFs) underpin critical applications in telecommunications, sensing, and high-power laser delivery, yet their design remains a manual, expert-intensive process that couples geometric intuition with deep waveguide physics. Vision-language models (VLMs) offer a promising path toward automating PCF design, but can they truly reason about photonic physics from microscopy images, or do they merely recognize visual patterns? We introduce PCFBench, the first comprehensive bench...

---

### 46. PathJev: Decision-Native Vision-Language Modelling for Histopathology

**Authors:** Cristian Tommasino, Antonio M. Rinaldi

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32478v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32478v1)

**Summary:** Vision-language models used for decisions in histopathology rarely return calibrated probabilities over the candidates a user cares about. Decision-native models write a question and a candidate set chosen at run time into the input and return a normalised distribution from a small decision head in one forward pass. We build PathJev-P, a decision-native model for histopathology: MedGemma-1.5-4B with LoRA adapters and a decision head, trained on 40,000 patch states from three public collections w...

---

### 47. From Perception to Pixels: Human-Derived Visually Distinct Colors for Improved Dominant Color Extraction

**Authors:** Uldana Shyndali, Nurdaulet Toleugaliyev, Kuat Zharykbayev, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32473v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32473v1)

**Summary:** Dominant color extraction is a fundamental task in computer vision, with applications in design, image retrieval, and content recommendation. However, conventional algorithms based on device-oriented color spaces (e.g., RGB) and fixed quantization often fail to capture how humans perceive color differences. In this study, we propose a human-perception-based framework for dominant color extraction, built on a novel Human Color Dictionary (HCD) derived from a perceptual experiment. Participants (n...

---

### 48. Online Continual Learning in Edge-Cloud Applications

**Authors:** Charalampos Davalas, Dimitrios Michail, Christos Diou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32472v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32472v1)

**Summary:** Deployed machine learning models in real-world IoT and edge/cloud systems face a critical reliability bottleneck: the requirement for online adaptation to non-stationary data streams while operating without access to the full original training dataset. Performance is severely degraded when models encounter Out-of-Distribution (OOD) inputs or suffer from catastrophic forgetting. Addressing these challenges requires adaptation mechanisms capable of learning from evolving data streams while preserv...

---

### 49. OPTARI: An open-source software framework for clinical translation of optoacoustic imaging

**Authors:** Moritz Schillinger, Maximilian Bader, Adrian Buehler, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32468v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32468v1)

**Summary:** Combined optoacoustic (OptA) and ultrasound imaging is a promising modality across a wide range of pathologies. Its use in clinical research, however, is limited by a lack of analysis software accessible to users without programming expertise. Existing tools are either script-based engineering frameworks or proprietary vendor applications. We present OPTARI, an open-source graphical software application to facilitate large-scale clinical optoacoustic-ultrasound (OPUS) studies. OPTARI builds on t...

---

### 50. MDMR-Bench: A Multi-Dimensional Benchmark for Multi-Reference Image Generation

**Authors:** Bowen Zheng, Jintao Lin, Changheng Yi, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32459v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32459v1)

**Summary:** Image generation models have rapidly advanced, with many models now supporting generation conditioned on multiple reference images and textual instructions. Such models enable a wide range of applications, including entity fusion and attribute transfer across images. However, existing benchmarks for multi-reference image generation rely on limited evaluation dimensions and fail to capture the diverse challenges of the task. To address this limitation, we propose MDMR-Bench, a Multi-Dimensional b...

---

## cs.LG

**50 papers**

### 1. RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms

**Authors:** Xi Chen, Fengqi Hu, Zeyu Shen, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32971v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32971v1)

**Summary:** Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions. Existing robust RL algorithms offer a rich set of mechanisms and principles, yet two major barriers limit their broader potential: limited algorithm reusability and an unclear empirical capability boundary. We introduce RobustRLlib, an algorithm-centric library and benchmark that addresses both challenges. It integrates 17 representative robust online, ...

---

### 2. DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection

**Authors:** Amber Xie, Jiawei Fu, Xiaofeng Guo, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32969v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32969v1)

**Summary:** Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to collect, but their motions must be estimated and retargeted to the robot, and they do not directly provide robot actions. In this paper, we introduce DexPort, a portable data-collection interface for...

---

### 3. Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection

**Authors:** Bernardo Perrone Ribeiro, Erkut Akdag, Egor Bondarev

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32964v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32964v1)

**Summary:** Few-shot industrial anomaly detection requires modeling category-specific normality from only a handful of defect-free images. Common approaches tie inference to stored exemplars, impose rigid linear structure, or risk reproducing anomalous content. Flownomaly instead casts the problem as normal-counterpart recovery in frozen DINOv2 feature space. Given normal supports, a velocity field is learned through conditional flow matching over frozen patch tokens to transport Gaussian noise toward norma...

---

### 4. Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox

**Authors:** Federico Lucca

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32955v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32955v1)

**Summary:** Personal email agents decide, for every message, what it is, whether it is urgent, whether to draft a reply, create a task, or ignore it. Their error rate is rarely measured: the stored labels were written by the system itself. We present Foyer, a self-hosted personal inbox agent in daily use, and a measurement protocol (stratified sampling, frozen snapshots, thread-grouped splits, pre-registered hypotheses, human labels in the agent's review loop) that yields ground truth before any training. O...

---

### 5. Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning

**Authors:** Yijing Ke, Tianle Cai, Ruosong Wang

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32951v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32951v1)

**Summary:** Reinforcement learning for large language models often uses separate systems for inference and training. Even with identical weights and BF16 tensors, implementation differences can make an intended on-policy update off-policy and destabilize training. Existing remedies align the entire inference and training stacks, change global precision, or modify the learning algorithm. We ask whether aligning selected parts of the execution stack can stabilize BF16 RL while other implementation differences...

---

### 6. Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation

**Authors:** Yixuan Xu, Hailin Liu, Linxiang Peng, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32943v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32943v1)

**Summary:** Generative recommendation with semantic IDs represents each item as a sequence of discrete codes derived from its semantic representation and predicts these codes to generate recommendations. Existing semantic-ID recommenders are typically trained with hard labels for the observed next item. Although such supervision identifies the target, it provides no explicit distributional information about alternative items conditioned on the same user history. Sequential recommenders can supply this item-...

---

### 7. If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs

**Authors:** Thomas Landeg, Thierry Tambe

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32941v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32941v1)

**Summary:** Vision-Language-Action (VLA) models perform well on robotic manipulation, yet remain brittle once their own actions carry them into states their training data barely covers. Recovering from such failures usually requires recovery demonstrations, policy retraining, or a separate model at inference time. We introduce Backtrack, a lightweight failure detection and recovery mechanism for frozen VLAs that needs none of these. A small failure prediction head, trained only on outcome-labeled rollouts o...

---

### 8. Learning Positive Linear Combinations of ReLUs in Fully Polynomial Time

**Authors:** Ilias Diakonikolas, Jelena Diakonikolas, Puqian Wang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32940v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32940v1)

**Summary:** We study the fundamental problem of PAC learning positive linear combinations of $k$ arbitrary ReLU activations on $\mathbb{R}^d$ with respect to the Gaussian distribution, in $L_2$ loss. We give the first fully-polynomial time algorithm for this learning task. Specifically, our algorithm draws $\mathrm{poly}(d, k, 1/ε)$ samples, runs in $\mathrm{poly}(d, k, 1/ε)$ time, and outputs a hypothesis that is $ε$-close to the target concept with high probability. All prior algorithms for this problem r...

---

### 9. ZENO: Nonlinear filtering with Zakai Equation Neural Operators

**Authors:** Aaditya Prasad, Steven W. Flavell, Brian DePasquale

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32926v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32926v1)

**Summary:** State inference and parameter learning for nonlinear filters is a core computation for scientific machine learning with varied applications in engineering and neuroscience. The unnormalized filtering distribution is governed by the Zakai equation, a stochastic partial differential equation (SPDE) that combines the forward Kolmogorov operator (known as the Fokker-Planck equation) with observed likelihood updates. Although solving these high-dimensional SPDEs is often impossible analytically and i...

---

### 10. Adaptive Frequency Threshold Byte Pair Encoding for Mixed Natural Language and Structured Symbolic Corpora

**Authors:** Pietro Di Nicco, Lucio La Cava, Andrea Tagarelli

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32921v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32921v1)

**Summary:** Modern language models rely on subwording tokenization to define the discrete units of input processing, typically using methods like Byte Pair Encoding (BPE) that treat whitespace as a fixed semantic boundary. This design is inherently limited, as many meaningful concepts---including multiword expressions and the structured environments of formal languages like LaTeX---frequently span across whitespaces. While recent superword tokenization methods attempt to address this by relaxing whitespace ...

---

### 11. SemantEq: Faithful Bidirectional Equivalence of Formal Statements

**Authors:** Xinrui Li, Pawan Sasanka Ammanamanchi, Siddharth Bhat, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32919v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32919v1)

**Summary:** Statement autoformalization translates mathematics from natural language into a proof assistant such as Lean 4, and models now do it at scale. As provers get stronger, the burden of correctness shifts from the proof to the statement, that is, to whether the formal statement faithfully translates its source. Given a trusted reference formalization, the natural test is logical equivalence, and it proves too much. $P \leftrightarrow Q$ holds trivially for any two statements $P$ and $Q$ that the lib...

---

### 12. A Tutorial on Physics Constrained Machine Learning for Hybrid Modeling, Optimization, and Control

**Authors:** Rahul Golder, Bimol Nath Roy, MM Faruque Hasan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32914v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32914v1)

**Summary:** Physics-constrained machine learning (PCML) integrates domain knowledge, first-principles, and physical constraints into AI/ML models. In this work, we present a step-by-step tutorial of a modular PCML framework, KKT-HardNet, and illustrate how it could be used for hybrid modeling, process simulation, optimization and model predictive control in a single platform. KKT-HardNet combines fast inference capabilities of neural networks with guaranteed satisfaction of algebraic constraints through dif...

---

### 13. Recommender regret for improving regularised RL estimation with bandits and MCTS

**Authors:** Danilo Vucetic, Alexandre Larouche, Mohammad Pedramfar, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32910v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32910v1)

**Summary:** Regularised reinforcement learning (RL) algorithms rely on estimators, like Monte Carlo tree search or one-step look-ahead, to provide policy, value, or Q-value estimates in training and inference. However, existing bandit-based estimation frameworks evaluate sampling efficiency, not the quality of estimates. We address this by formalising estimate generation as a recommendation process, treating bandit-based sampling as an improvement operator. To evaluate the quality of a recommendation (estim...

---

### 14. LoCA: Enabling Multi-Modality in Geospatial Location Encoders

**Authors:** Panagiotis Koromilas, Eleanna Vali, Diogenis Antonopoulos, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32894v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32894v1)

**Summary:** Location encoders map geographic coordinates to high-dimensional descriptors through contrastive alignment with paired Earth Observation imagery. We prove that this construction is structurally limited: any Lipschitz location encoder produces an output of intrinsic dimension at most 2, regardless of architecture or bandwidth, which forces the contrastive loss to strictly exceed its asymptotic optimum. Empirically, joint training also collapses the encoder's embedding covariance to low rank. Alth...

---

### 15. When Human Corrections Travel: Safety in Federated VLA Adaptation

**Authors:** Vigneshwaran Subbaraju, Obaidullah Zaland, Monowar Bhuyan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32888v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32888v1)

**Summary:** Vision-language-action (VLA) policies can adapt to local human intervention, while federated learning can combine distributed robot experience without pooling raw records. We examine their prospective intersection: sharing adaptations derived from diverse human corrections across tasks, environments, people, and robot embodiments. Corrections differ in modality, safety semantics(urgency, behavioral scope, etc.), and privacy sensitivity. A shared update that improves mean task success may suppres...

---

### 16. Reinforcement Learning with Multi-Step Transition Predictions: A Bellman Theory

**Authors:** Chenbei Lu, Zaiwei Chen, Tongxin Li, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32887v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32887v1)

**Summary:** Multi-step predictions of future transition realizations can improve reinforcement learning, but their value remains difficult to quantify. Directly including these predictions in the state can lead to exponential state-space growth, making direct dynamic programming computationally expensive. We study discounted finite MDPs under a block-feedback protocol: at the start of each K-period block, the decision maker observes $K$-step probabilistic transition predictions for a subset of actions and a...

---

### 17. Trusting the Tool: Asymmetric Deference of LLM Vulnerability Auditors to Static-Analysis Evidence

**Authors:** ZhiHong Liu, Shuyao Gao

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32876v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32876v1)

**Summary:** Pipelines that combine large language models (LLMs) with static analysis let the model consume the analyser's output as evidence, but whether the model distinguishes true from false evidence, and whether its scrutiny depends on what the evidence claims, has not been measured. We built an intraprocedural analyser for C/C++ that produces proof obligations and audited vulnerable and patched functions from PrimeVul under six evidence conditions that differ only in the notes, including fabricated ass...

---

### 18. Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery

**Authors:** Marek Masiak, Andrzej Szablewski, Nicola Cancedda, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32866v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32866v1)

**Summary:** Fine-tuning on datasets of unknown origin can create a backdoor in the trained model when the data includes poisoned examples. Difficult to localise and remove, backdoors can persist through safety training. While parameter-efficient fine-tuning methods capture the full parameter changes introduced during training, they are not easily interpretable. We present the full method of TopKLoRA, extending the preliminary proposal of Masiak et al. (2025), an interpretable-by-design LoRA variant in which...

---

### 19. PoKER: A Probability of Kill Estimation Rate Model for Air-to-Air Missiles Using Machine Learning on Stochastic Targets

**Authors:** Joao P. A. Dantas, Andre N. Costa, Diego Geraldo, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32864v1)

**Summary:** This work introduces PoKER, a novel probabilistic model engineered to optimize missile launch effectiveness in air-to-air scenarios, specifically within Beyond Visual Range (BVR) air combat. Unlike conventional Weapon Engagement Zone (WEZ) models that delineate zones based on static distances such as maximum, minimum, and no-escape ranges, PoKER applies machine learning to predict kill probabilities more accurately by integrating the stochastic behaviors of targets and missile miss distances. Th...

---

### 20. Sustainability of TSFM Deployment and Pretraining: From Carbon Footprint Analysis to Mitigation via Pruning

**Authors:** Cécile Luc, Nathanaël Lemonnier, Ievgen Redko

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32859v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32859v1)

**Summary:** Time Series Foundation Models (TSFMs) offer strong zero-shot forecasting capabilities, but their high pretraining cost raises a practical sustainability question: does this upfront investment pay off over a full deployment lifecycle, compared to supervised standalone models that must be periodically retrained? We model the cumulative carbon cost of different approaches across a realistic industrial scenario: Chronos-2 amortizes its pretraining cost within months for large or frequently queried d...

---

### 21. Regularised RL improves sim-to-real transfer

**Authors:** Danilo Vucetic, Mohamad H. Danesh, Florence Clerc, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32855v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32855v1)

**Summary:** Regularised reinforcement learning (RL) has provable robustness guarantees that should ease the transfer of policies from simulation to robots, known as sim-to-real. Yet, weakly regularised algorithms like Proximal Policy Optimisation (PPO) remain the de facto choice in sim-to-real pipelines, while the practical benefits of regularisation for transfer remain poorly characterised. In this work, we study the sim-to-real performance of commonly used RL algorithms, with the aim of characterising the...

---

### 22. Singular Geometry of Low-Rank Adaptation

**Authors:** Kamillo Ferry, Anthea Monod, Keisuke Yano

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32854v1)

**Summary:** Low-rank adaptation (LoRA) is now a standard approach to parameter-efficient fine-tuning of large neural networks. Its low-rank factorization is inherently non-identifiable, making LoRA a singular statistical model whose learning complexity cannot be described by parameter dimension alone. We study this complexity using the real log canonical threshold (RLCT) from singular learning theory and how it depends on both the low-rank parameterization and the pretrained network. Under a local lineariza...

---

### 23. Near-Optimal List Replicability from Littlestone Dimension

**Authors:** Ari Blondal, Pooya Hatami, Chavdar Lalov, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32853v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32853v1)

**Summary:** We study the list replicability number in the realizable PAC learning framework and prove that every concept class $H$ over a countable domain with Littlestone dimension $d$ and dual VC dimension $v^*$ satisfies \[ \mathrm{LR}(H)\leq 2^{O(d\min\{\log d,v^*\})}. \] This matches the worst-case lower bound of $2^{Ω(d)}$ up to a logarithmic factor in the exponent and exponentially improves the previous best upper bound $\mathrm{LR}(H)\le 2^{2^{O(d)}}$ of Bun, Livni, and Moran [FOCS 2020]. Unlike ear...

---

### 24. Neural LoFi with Backward Coupling: A Spectral Theory of Cross-Layer Feature Learning

**Authors:** Yatin Dandi, Matteo Vilucchio, Hugo Tabanelli, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32849v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32849v1)

**Summary:** During joint training, backpropagation allows later layers to reshape earlier representations, a feedback mechanism absent from purely layer-wise learning. We extend Neural Low-Degree Filtering (Neural LoFi), a recently proposed layer-wise spectral surrogate for feature learning, to capture this interaction. Starting from the exact backpropagation gradients, we derive a local coupling between a neuron's incoming weights and its corresponding next-layer column. In a controlled small-initializatio...

---

### 25. On the Limits of Sparse Linear Model with Shuffled Differential Privacy

**Authors:** Yan Zhang, Jiong Tuo, Meng Ding, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32822v1)

**Summary:** Sparse linear regression is a fundamental problem in high-dimensional statistics, and its private counterparts leave a large gap between the central and the local model of differential privacy. Shuffled differential privacy (SDP) sits between the two, offering accuracy closer to the central model without the trust requirement of a central curator. This paper studies sparse linear regression under both non-interactive and interactive SDP protocols. In the non-interactive setting, any non-interact...

---

### 26. U-NeXt: General-purpose event detection for neonatal EEG

**Authors:** Robert Hogan, Sean R. Mathieson, Aurel Luca, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32811v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32811v1)

**Summary:** We developed U-NeXt, a general framework for neonatal electroencephalography (EEG) event detection based on semantic segmentation. Its convolutional encoder-decoder directly segments individual channels using long input segments to preserve temporal context. A shared architecture and training framework were developed using low-voltage interval, artefact, and seizure datasets containing 51, 98, and 278 neonates, respectively, comprising over 11,000 hours of EEG and 82,000 annotated events. Perfor...

---

### 27. Multiplicative vs. Additive State Coupling in Learned Optimizer Schedules

**Authors:** M. Harper Langston, Pierre-David Letourneau, Dalton Jones, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32801v1)

**Summary:** We learn schedules for a continuous penalty relaxation of MAX-CUT by backpropagating through an unrolled classical solver. A state-blind schedule generalizes to instances substantially larger than those used for training. A state-adaptive bilinear schedule also generalizes out of distribution, outperforming its untrained baseline across 15 seeds ($t=4.1$). By contrast, an additive ablation with identical inputs and output heads is statistically indistinguishable from the bilinear model in distri...

---

### 28. CARES: Coverage-Aware Replay Exemplar Selection for Continual Learning

**Authors:** Arundhati S. Shanbhag, Brian B. Moser, Federico Raue, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32799v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32799v1)

**Summary:** Replay-based Continual Learning mitigates catastrophic forgetting by keeping a buffer of past samples, making buffer composition critical under a fixed memory budget. Recent coreset-based replay methods improve buffer quality using model-derived gradients, losses, or auxiliary optimization, but incur substantial computational overhead as memory is repeatedly updated. We propose CARES, a continual model-optimization-free approach for buffer construction that instead exploits the geometry of a fro...

---

### 29. Generalization properties of the token perceptron: the role of embedding and vocabulary

**Authors:** Dario Bocchi, Matteo Negri, Flavio Nicoletti, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32788v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32788v1)

**Summary:** Large language models are trained to predict tokens from a finite vocabulary, each represented by a vector in a $d$-dimensional embedding space. Therefore, token prediction is a classification problem whose classes have a geometry determined by the embedding. We study how this geometry affects learning in a minimal solvable model: a linear predictor that maps a sequence of $N$ embedded tokens to a $d$-dimensional output through one $d\times d$ matrix per position, trained in the teacher--student...

---

### 30. Deep Learning-Based Prediction of HER2 Status from Whole-Brain MRI in Breast Cancer Brain Metastases

**Authors:** Sara Early, Chris Kang, Vibujithan Vigneshwaran, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32774v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32774v1)

**Summary:** Purpose: Human epidermal growth factor receptor 2 (HER2) status is a key biomarker relevant for prognostication and treatment decision making in metastatic breast cancer. Thus, the aim of this work was to explore whether HER2 status can be predicted directly from whole-brain post-contrast T1-weighted (T1w) MRI scans in breast cancer brain metastases (BCBM) using deep learning, and whether providing explicit tumour segmentation information improves prediction.   Methods: Using the publicly availa...

---

### 31. Direction-Aware Token Credit Assignment with Reward-Model Gradients

**Authors:** Yikuan Hu, Jifeng Zhu, Minle Su, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32772v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32772v1)

**Summary:** GRPO shares a response-level advantage across tokens, leaving unresolved how strongly each token should contribute to learning. Updates induced by the shared advantage reinforce or suppress the sampled token at each position, but these updates do not always point toward increasing reward at the token level. This motivates a work-based view of credit: just as work depends on the component of force along a displacement, token credit should reflect the local reward change along the policy update di...

---

### 32. On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models

**Authors:** Leon Sick, Lukas Hoyer, Yannick Strümpler, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32770v1)

**Summary:** On-policy self-distillation enables post-training foundation models without relying on stronger external teachers. However, existing approaches rely on ground-truth question-answer pairs, human-curated problem sets, or other supervised signals. In this work, we reformulate on-policy self-distillation as a self-training framework, driven by self-generated question-answer pairs and privileged reasoning demonstrations. We push supervision to the limit: guided solely by coarse, high-level topic desc...

---

### 33. Clean-label Poisoning Attack and Defense Game for Federated Learning in Vehicular Networks

**Authors:** Yalin E. Sagduyu, Tugba Erpek, Nathan Stephenson, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32765v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32765v1)

**Summary:** This paper studies interactions between clean-label poisoning attack and defense in vehicular networks using federated learning (FL). Basic Safety Message (BSM) classification for anomaly detection is modeled as a distributed learning problem over a vehicular network with dynamic topology. As a critical threat to FL, a feature-space clean-label attack is introduced, wherein benign samples are perturbed toward malicious feature extremes, degrading class separability while preserving labels. To co...

---

### 34. ARENA: Active Region attENtion Aggregation for interpretable solar flare prediction

**Authors:** Luis Bauer, Annalena Kofler, Andrés Asensio Ramos, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32758v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32758v1)

**Summary:** Predicting solar flares is a challenging space-weather forecasting problem with potentially significant impacts on Earth's upper atmosphere, including disruptions to radio communications. We propose Active Region attENtion Aggregation (ARENA), a neural network architecture that predicts solar flares from a variable number of active-region cutouts while learning to identify the region most relevant to the prediction. ARENA is trained using multiple-instance learning under weak supervision, requir...

---

### 35. Sparse Bayesian Neural Networks via Sticky Piecewise Deterministic Markov Processes

**Authors:** August Arnstad, Geir Olve Storvik, Filippo Pagani, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32753v1)

**Summary:** There is growing evidence that the performance of a neural network depends largely on a small subset of its weights, which are typically identified by training a dense network and pruning it afterwards. Within a Bayesian framework, pruning can be directly incorporated through a spike-and-slab prior, providing a proper treatment of the uncertainties involved, both with respect to pruning and to parameter uncertainty. In Bayesian neural networks (BNNs), sampling by MCMC is notoriously hard. We dem...

---

### 36. On the Identifiability of Hybrid Deep Generative Models: Meta-Learning as a Solution

**Authors:** Yubo Ye, Maryam Toloubidokhti, Sumeet Vadhavkar, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32748v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32748v1)

**Summary:** The interest in leveraging physics-based inductive bias in deep learning has resulted in recent development of hybrid deep generative models (hybrid-DGMs) that integrate known physics-based mathematical expressions in neural generative models. To identify these hybrid-DGMs requires inferring parameters of the physics-based component along with their neural component. The identifiability of these hybrid-DGMs, however, has not yet been theoretically probed or established. How does the existing the...

---

### 37. Strongly Adaptive Online Learning with Time-Varying Movement Costs

**Authors:** Andrew Jacobsen, Emmanuel Esposito, Hao Qiu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32740v1)

**Summary:** We study strongly adaptive regret for Online Convex Optimization (OCO) with time-varying movement costs, a setting that evaluates a learner's performance over arbitrary sub-intervals. This framework captures complex sequential decision-making problems where both the environment and the cost of switching decisions fluctuate over time. We propose a novel algorithm which, for any interval $[a,b] \subseteq [T]$, achieves a data-dependent regret bound of $ \widetilde{\mathcal{O}}\left( \sqrt{(D^2+DP_...

---

### 38. Internal Discrepancy for Contrastive Learning: Generalization Bounds and Downstream Behaviors

**Authors:** Jialiang Wang, Qing Ma, Xiong Zhou, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32729v1)

**Summary:** Contrastive learning has emerged as a popular paradigm for training representation models. While prior studies pursue more practical and less restrictive assumptions to enhance theoretical understanding of contrastive learning, they essentially describe the interconnections among representations within the data or induced by the function class. To encapsulate these assumptions, we propose the measure of internal discrepancy that quantifies the difference between the mean representation of positi...

---

### 39. PlayerEmbed: Learning Behavioral Fingerprint Representations from Raw Input Sequences

**Authors:** Tobias Schneider, Lorenz Sparrenberg, Priya Tomar, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32727v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32727v1)

**Summary:** Raw player input sequences in video games contain fine-grained behavior, but are high-dimensional and noisy, which makes large-scale analytics challenging. To address this, we introduce PlayerEmbed, a framework that learns compact and discriminative player embeddings using deep metric learning. Our approach uses a hybrid CNN-LSTM encoder trained on raw input sequences from 1,000 players. We evaluate the model on held-out sequences from these players and on sequences from 1,000 players entirely u...

---

### 40. Cross-Scenario Controller Parameter Transformation from Real-World Driving Data through Flow Matching

**Authors:** Christian Zink, Maik Pfefferkorn, Eric Lenz, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32719v1)

**Summary:** Advanced Driver Assistance Systems have become increasingly widespread, aiming to support drivers, reduce workload, and improve traffic safety. However, many systems are rarely used because their behavior feels unnatural and does not match individual driving behavior. The growing availability of large-scale, real-world human driving data enables more human-like and driver-individual assistance functions. This paper formulates the adaptation of Adaptive Cruise Control parameters as a driver-indiv...

---

### 41. Score-Preserving Continual Lasso under Task Shift

**Authors:** Jingyi Guo, Runze Li, Lingzhou Xue

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32708v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32708v1)

**Summary:** Continual learning (CL) aims to learn from sequential tasks while mitigating catastrophic forgetting when historical data are no longer accessible. We study continual learning for high-dimensional sparse linear regression, where $\ell_1$ regularization creates a difficulty absent from continual ridge regression: that recursively reusing an $\ell_1$-penalized estimator can propagate earlier shrinkage and accumulate regularization bias across tasks. We propose score-preserving continual Lasso (SP-...

---

### 42. Probing the limits of forward screening and inverse design of crystal materials

**Authors:** Zhilong Song, Zijun Pang, Lixue Cheng

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32678v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32678v1)

**Summary:** Crystal materials are designed either by screening known crystals for a target property or by generating new crystals with that property. Both routes are judged against public databases of known crystals, but these databases name the same crystal differently. Several materials announced as new by recent generative and autonomous discovery campaigns have since proved to be known phases or close variants of them. The limits of both routes remain unmeasured. Here we probe them by matching the cryst...

---

### 43. EMG Tokenization Preserves Movement Information at a Fraction of the Bitrate

**Authors:** Raul C. Sîmpetru, Amin Olamazadeh, Devon Rohlf, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32674v1)

**Summary:** Wireless electromyography (EMG) interfaces must balance electrode coverage against transmission bandwidth. Here, we show that compact EMG tokens substantially reduce payload while retaining information for three-dimensional hand-pose decoding. We evaluate two causal tokenizers fitted without pose labels: an encoder pretrained to reconstruct EMG spectra and one based on SPAR, an engineered spectral-spatial representation of neighbouring electrodes. In personalized, within-session experiments with...

---

### 44. Do Language Models Trust Their Own Justifications? A Study on Functional Consistency

**Authors:** Alisson Rosa Pereira, Bruno Iochins Grisci

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32665v1)

**Summary:** Large Language Models (LLMs) have been widely adopted in text classification tasks, where they not only output class predictions but also generate explanations that highlight the tokens deemed most relevant for reaching the predicted label. Yet it remains unclear whether these highlighted elements are behaviorally consistent with the model's own predictions under targeted interventions, which we refer to as functional auto-consistency. While much of the literature evaluates the textual plausibil...

---

### 45. DT-JEPA: Learning to Predict Future Representations for Decision-Making

**Authors:** Changxu Ni, Yiyang Ni, Jun Li, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32657v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32657v1)

**Summary:** Decision Transformer (DT) has demonstrated strong performance in various offline reinforcement learning (RL) tasks by conditioning action generation on expected future returns and historical trajectories. However, treating expected future returns as the condition provides an incomplete description of the future, as trajectories with different state transitions and behaviors may share similar returns. Moreover, expected future returns inherently depend on task-specific reward functions, which mak...

---

### 46. WL-SeqVAE: Sequence-Based Graph Generation Using Variational Autoencoders and Weisfeiler-Leman Colors

**Authors:** Iakovos Evdaimon, Giannis Nikolentzos, Achilleas Tsimichodimos, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32650v1)

**Summary:** In this paper, we introduce WL-SeqVAE, a sequence-based variational autoencoder for generating graphs. The key observation behind WL-SeqVAE is that node colors induced by the Weisfeiler-Leman (WL) algorithm provide compact discrete summaries of local graph structure and can therefore serve as structural tokens for generation. Rather than learning a distribution over adjacency matrices directly, our method maps each graph to a sequence of WL colors and employs a variational autoencoder that encod...

---

### 47. The Standard Deviation in VICReg Buys a Safety Margin

**Authors:** Hawar Dizayee

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32630v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32630v1)

**Summary:** VICReg prevents collapse with a hinge on the standard deviation of each embedding dimension, and its authors argue from the gradient that a hinge on the variance would fail. To our knowledge, this claim has not been tested experimentally. We test it in a controlled setting (ResNet-18, CIFAR-10 and CIFAR-100), changing only the hinge and sweeping its weight $μ$ over five orders of magnitude. At the default weight ($μ= 1$), the two hinges reach the same linear-probe accuracy on CIFAR-10 (about 89....

---

### 48. Acquisition for Spherical-Linear Bayesian Optimization on the Cube

**Authors:** Nathan Wycoff

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32628v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32628v1)

**Summary:** Recent work demonstrated that executing Bayesian Optimization (BO) using simply a linear surrogate with a clever transformation is enough to approximate the performance of the standard Gaussian-Process (GP) based version on high-dimensional test functions. When the decision region is a sphere, this strategy admits rapid exact acquisition. However, it is the unit cube we encounter most often in the BO literature, and in this setting a standard approach, namely a multi-start quasi-Newton method, i...

---

### 49. Earth embeddings are decomposable records of the land surface

**Authors:** Robin Young, Srinivasan Keshav

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32617v1)

**Summary:** Ecological monitoring, carbon accounting and biodiversity assessment increasingly rely on annual Earth embeddings--learned vectors that compress a year of satellite observation for every ten-meter pixel on Earth, consumed in place of the imagery itself. What these vectors mean has not been established. Here we decompose two widely used embedding products and show that they contain individual ecological features, including fire, forest clearing and crop type, validated against independent referen...

---

### 50. Interpreting Supervised Pairwise Graph Representations: Local Evidence, Confounding, and Provable Post-hoc Correction

**Authors:** Ilya Brekin, Ariela Moldavskaya, Elina Sidorova, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32611v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32611v1)

**Summary:** Supervised pairwise graph representations convert pairwise predictive relations into sample-specific graphs, but graph-level accuracy does not by itself show that higher-order topology carries the signal. In a controlled Transformer error-detection task, supervised pairwise graphs outperform attention-as-adjacency (ROC-AUC $0.839$ versus $0.559$; the comparable no-confidence pair is $0.687$ versus $0.559$), but their apparent advantage over model confidence disappears after controlling for seque...

---

## cs.NE

**50 papers**

### 1. PAFS: Perturbation-Aware Firing Scaffolds for Robust Event-Based SNNs

**Authors:** Ning Liu, Jun Sun, Hao Guo, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32409v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32409v1)

**Summary:** Event-based spiking neural networks (SNNs) encode information through temporal firing dynamics, but the same stateful computation makes their predictions sensitive to event loss, timestamp jitter, and speed variation. These perturbations alter evidence accumulation, yet late-layer firing trajectories can retain error-diagnostic structure that is absent from the final logits alone. We introduce Perturbation-Aware Firing Scaffolds (PAFS), a labeled post-training calibration method that exploits th...

---

### 2. Searching with Sparse Histories: Cross-Task Architecture Search from Incomplete Search Logs and Zero-Cost Proxies

**Authors:** Yuefeng Xu, Jun Yu

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32179v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32179v1)

**Summary:** Neural architecture search (NAS) is expensive, but cross-task transfer can reduce costs by reusing knowledge from previous tasks. However, existing methods struggle with sparse search histories and task-specific transfer failures. We propose a method, a risk-robust strategy that combines sparse source logs with zero-cost proxies through champion-based initialization and joint pairwise-ranker pretraining. On TransNAS-Bench-101, the proposal mitigates severe worst-case failures, reducing worst-10%...

---

### 3. A Resource-Efficient and Precision-Scalable FPGA Accelerator for Spiking Neural Networks Using Minifloat Arithmetic

**Authors:** Ali Mehrabi, Philip C. Jose

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32052v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32052v1)

**Summary:** Spiking neural networks (SNNs) are well suited to event-driven edge intelligence, but the arithmetic complexity, memory footprint, and power consumption associated with conventional floating-point implementations can limit their deployment on resource-constrained hardware. This paper presents a precision-scalable and resource-efficient SNN hardware accelerator architecture based on parameterized minifloat arithmetic. The proposed architecture implements recurrent leaky integrate-and-fire (LIF) n...

---

### 4. RobustNCL: Robustifying Neuromorphic Continual Learning under Transient Faults with Lightweight Detect-and-Cure Strategy

**Authors:** Rachmad Vidya Wicaksana Putra, Shuochen Zhou, Muhammad Shafique

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31954v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31954v1)

**Summary:** In neural networks, continual learning (CL) is a prominent approach for enabling deployed systems to adapt to dynamic operational environments by effectively learning from new unseen data at runtime. Recently, the neuromorphic continual learning (NCL) concept has emerged as an energy-efficient alternative to CL by leveraging sparse event-based operations. However, NCL performance can be undermined by transient faults in the hardware platforms, which may come from high-energy particle strikes at ...

---

### 5. ENCL: Enabling Efficient Neuromorphic Continual Learning with Local Learning Rule and Sub-Network Freezing Strategy

**Authors:** Rachmad Vidya Wicaksana Putra, Shuochen Zhou, Hassan Raza, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31927v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31927v1)

**Summary:** Continual learning (CL) in neural networks is a promising learning approach for updating the knowledge of deployed systems based on new data encountered at run time, that have not been learned during the offline training phase. To enable their power/energy-efficient CL processing, neuromorphic continual learning (NCL) concept with sparse event-based operations have recently been introduced. However, state-of-the-art NCL methods typically employ the memory-hungry data/experience replay, coupled w...

---

### 6. First hardware demonstration of a continuous-state probabilistic computer with programmable energy-defined sampling

**Authors:** Chao Fang, Hsuan Yao Tu, Yihan He, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31339v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31339v1)

**Summary:** Probabilistic computing has proved useful for combinatorial optimization, but conventional implementations rely on binary stochastic units and sigmoid-based updates. Extending these systems to continuous variables requires binary encoding. Here we introduce a continuous probabilistic computer (CPC) whose continuous probabilistic bits sample bounded states from conditional distributions defined by local energies. Separating random-source generation from conditional sampling provides a route to us...

---

### 7. AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments

**Authors:** Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31326v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31326v1)

**Summary:** Evolutionary program search with large language models keeps the structure of an evolutionary algorithm and uses the model as its variation operator. Typically, the model generates each candidate program in a single request from parent programs and their scores. We present AgenticEvolve, an evolutionary program search framework in which each island is run by a persistent large language model agent. Between evaluations, the agent designs and runs experiments on the candidate program. To measure t...

---

### 8. HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning

**Authors:** Sudipta Paul, Pengrui Quan, Aounon Kumar, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30042v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30042v1)

**Summary:** Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self-improvement and were developed mainly for coding, where the competence needed to improve the agent coincides with the competence being improved. Planning tasks, in which an agent must produce a sequence of tool calls th...

---

### 9. Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition

**Authors:** Pavlos Poulos, Katelyn Sadorf, Themos Stafylakis, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29720v2) | 📄 [PDF](https://arxiv.org/pdf/2610.29720v2)

**Summary:** Spiking Neural Networks (SNNs) promise energy-efficient inference through sparse, event-driven computation, yet remain constrained on continuous, context-dependent tasks such as automatic speech recognition (ASR). A key bottleneck is the Leaky Integrate-and-Fire (LIF) neuron, whose membrane decay erases information across pauses and phonetic boundaries while it must both extract features and retain long-range context. Inspired by cortical separation of nonlinear filtering and somatic integration...

---

### 10. Probing Spatial and Spectral Grounding in EEG Foundation Models

**Authors:** Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29367v1)

**Summary:** EEG foundation models are advancing at an unprecedented pace, yet their evaluation is driven by downstream accuracy, which reveals little about whether their predictions rely on physiologically interpretable signal structure. We introduce a set of perturbation probes in two grounding axes: spatial grounding in channel identity and topographic locality, and spectral grounding in oscillatory content and waveform morphology. We apply these probes to five published EEG foundation models across motor...

---

### 11. BrainCodes: A Lightweight EEG Foundation Model over Discrete Neural Codes

**Authors:** Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29320v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29320v1)

**Summary:** Recent electroencephalography (EEG) foundation models increasingly emphasize model scale, potentially limiting their deployment on resource-constrained devices and in everyday environments. We argue that transferable EEG features can instead be learned with a compact architecture and introduce BrainCodes, a lightweight foundation model pretrained through self-supervised learning on more than 800 hours of recordings from over 1,000 participants. Our architecture combines a quantization-based neur...

---

### 12. Reconstruction differences rival individual differences in the fly compass connectome and break trained circuit models

**Authors:** Md Ali Ashraf Yad, Nazifa Tabassum Nabila

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29205v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29205v1)

**Summary:** Neural network models are increasingly constructed from synapse-resolution connectomes, and the same circuit is now available in reconstructions from other animals and pipelines. We do not know whether such models are dependent on the reconstruction they are built from, and whether connectome differences are biological or measurement errors. We studied the Drosophila head-direction circuit in nine versions: four flies (male CNS, hemibrain, Fly Wire, BANC) and five variants of the same fly varyin...

---

### 13. Gate Initialisation versus Recurrent Dropout and Zoneout in Learning Long Dependencies: A Controlled Study of LSTM and GRU Networks on Synthetic Tasks

**Authors:** Oleksandr Kholodniak, Oleksandr Prokhorov

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29034v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29034v1)

**Summary:** Dropout and zoneout are routinely added to long short-term memory (LSTM) and gated recurrent unit (GRU) networks, but, to our knowledge, their placements have not been crossed with gate initialisation in a factorial design, and it is not known whether early gradient propagation tells which runs will learn long dependencies. We trained one-layer LSTMs and GRUs on the adding problem and on delayed recall in a factorial grid of 720 runs, crossing conventional and chrono gate initialisation with up ...

---

### 14. Unit-Aware Differentially Private Quantum Machine Learning for Clinical and Wearable Health Data

**Authors:** Md Khalid Syfullah, Alvi Ataur Khalil

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28968v1) | 📄 [PDF](https://arxiv.org/pdf/2610.28968v1)

**Summary:** Clinical registries and wearable sensors support early health-risk assessment, yet models trained on these records may leak sensitive information when released. Differential privacy (DP) bounds this leakage by injecting noise whose total magnitude grows with the number of trainable parameters, a cost especially severe for small health cohorts. This motivates parameter efficient models including quantum machine learning (QML), whose variational circuits can represent complex decision boundaries w...

---

### 15. Multi-Objective Evolutionary Semi-Supervised Learning for Resource-Aware Smart City Classification

**Authors:** Francisco José Sedeño, Jamal Toutouh

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.27703v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27703v1)

**Summary:** Smart-city applications often combine scarce labeled data with abundant unlabeled observations. Semi-supervised learning (SSL) exploits both labeled and unlabeled data to improve classification under limited supervision. This article presents MOEA-SSL, a multi-objective evolutionary approach for lightweight semi-supervised tabular classification that jointly optimizes predictive quality and feature usage. Experimental evaluation on three Smart City classification datasets, considering 1\%, 5\%, ...

---

### 16. Hybrid metaheuristics for architectural design optimization under small evaluation and wall-clock budgets

**Authors:** Luciano Ambrosini

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26202v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26202v1)

**Summary:** Architectural and structural design optimization in parametric software affords about a thousand evaluations of an expensive model for problems with tens of variables, a regime for which most metaheuristics were not designed. On the side of artificial intelligence, two hybrid metaheuristics are proposed: a covariance matrix adaptation evolution strategy (CMA-ES) whose sampling is enriched with differential-evolution trial vectors, and a particle swarm with success-history parameter adaptation, d...

---

### 17. A Spiking Ring-Attractor Architecture for Representation and Control of Revolute Robot Joints

**Authors:** Aung Htet, Alejandro Rodriguez Jimenez, Ruidong Ma, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26027v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26027v1)

**Summary:** Robotic systems with revolute joints evolve on circular state spaces, yet most control architectures represent these states using Euclidean variables that ignore this underlying geometry. We propose a fully spiking neural control architecture in which ring attractors encode joint states, enforcing representations consistent with the topology of revolute systems. Homeostatic regulation computes goal-state mismatch directly over these distributed representations, and opponent gain-modulated popula...

---

### 18. Sector-Ring Linear Reservoirs: Sector-Wise Decay-Timescale Allocation With State Reuse Across Candidate Settings

**Authors:** Yudai Ebato, Sou Nobukawa, Yusuke Sakemi, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25806v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25806v1)

**Summary:** In reservoir computing, performance depends on whether the fixed dynamics of the reservoir suit the task, and the appropriate memory length and frequency response differ across tasks. The reservoir settings are found by a search on each task, and driving the reservoir with the input and collecting its states for every candidate setting dominates the cost of the search. In a reservoir with a linear recurrence, the dynamics decompose into modes, one per eigenvalue, and the eigenvalue distribution ...

---

### 19. Migrate Computation, Not Data: Fault Recovery in Neuromorphic Many-Core Systems

**Authors:** Muyang Cao, Di Yu, Peiling Zhu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26985v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26985v1)

**Summary:** As neuromorphic systems scale to thousands of near-memory cores, aging-induced permanent faults in neuron-update datapaths become an important obstacle to long-term deployment. Existing online recovery methods typically retire a faulty core and migrate its neurons, along with their weights and membrane states, to healthy cores. This whole-core treatment incurs high recovery traffic and makes recovery depend on scarce destinations; at high utilization, there may be enough surviving compute capaci...

---

### 20. Peer-Relative Trust-Guided Update Screening for Robust Semi-Decentralized Federated Learning under Label-Flipping Attacks

**Authors:** Ajay Kumar Shrestha, Sandhya Joshi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25714v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25714v1)

**Summary:** Trust and reputation mechanisms can reduce the influence of malicious clients in federated learning (FL), but strict update filtering is difficult under non-independent and identically distributed (non-IID) data because honest local updates may temporarily reduce performance on a shared validation proxy. Building on our earlier trust-based semi-decentralized FL (SDFL) framework, this paper operationalizes the trust signals and introduces peer-relative update screening that combines a robust vali...

---

### 21. Let Them Sleep: Recursive Self-Pruning Memory for Long-Horizon LLM Agents

**Authors:** Kargi Chauhan, Sadiba Nusrat Nur, Pratibha Revankar, et al.

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25561v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25561v1)

**Summary:** Agents that run for a long time have a memory problem, and it is not the one most systems optimize for. Storing every trace and retrieving the nearest neighbors works early and quietly stops working later: the store fills up with failures the agent then repeats, and with facts that were true fifty turns ago. RSPM (Recursive Self-Pruning Memory) borrows the fix biology already found. At intervals the agent sleeps. It clusters its recent failures, distills each cluster into a short rule, and delet...

---

### 22. Small-scale neural simulation of Caenorhabditis elegans on Loihi-2 using NeuroML2Loihi

**Authors:** Danny Rosen, Ramashish Gaurav, Yang Yi

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25424v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25424v1)

**Summary:** Neural simulation is an essential methodology for studying biological nervous systems, but it remains limited by the computational costs of repeatedly updating neural and synaptic states over many timesteps. Neuromorphic hardware is a promising substrate for this class of workloads because such devices combine event-driven execution, localized memory, and spike-based communication. However, neuromorphic \textit{software} remains comparatively fragmented and difficult to integrate with the model-...

---

### 23. Length-Independent Stability and $L_2$-Gain Certificates for Chains of Delayed Neural Modules

**Authors:** Ömer Faruk İşcanlı

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25147v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25147v1)

**Summary:** Networks of repeated neural modules with delayed neighbour coupling need stability guarantees for every number of modules, but delay-dependent criteria certify one network at a time and grow with its size. This paper derives stability and $L_2$-gain certificates of length-independent size for open chains and rings of modules of two alternating types with slope-restricted activations. A local and a transmission delay act independently and are only bounded and continuous. A Lyapunov-Krasovskii fun...

---

### 24. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity

**Authors:** Takashi Ishida, Taro Makino, Issa Sugiura

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23470v2) | 📄 [PDF](https://arxiv.org/pdf/2610.23470v2)

**Summary:** Open-ended search combined with foundation models has produced advances such as faster algorithms, new results on open mathematical problems, and self-improving agents. We extend this paradigm to recommendation for decision-making, focusing on decisions where the set of possible choices is fixed but the reasons for choosing them are not. In high-stakes decisions, e.g., which company to acquire or which customer to target, comparing diverse, well-reasoned options can be more useful than a single ...

---

### 25. Algorithm Modelization: Transforming Optimization Algorithms into Evolvable Intelligence

**Authors:** Jian Yao, Zhiyao Zhang, Yichen Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23161v2) | 📄 [PDF](https://arxiv.org/pdf/2610.23161v2)

**Summary:** Can algorithms be learned and evolved as models, rather than repeatedly redesigned as programs? We explore this question by introducing Algorithm Modelization, a new paradigm that turns iterative algorithms into trainable models. Its central idea is to regard algorithm execution trajectories as computational experience: by learning how algorithmic states evolve over iterations, a model can internalize the knowledge embodied in existing algorithms, reproduce their computational behaviors, and fur...

---

### 26. Wavelength Diversity Expands the Expressive Power of Optical Computing

**Authors:** Shiqi Chen, Che-Yung Shen, Parnian Ghapandar Kashani, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23070v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23070v1)

**Summary:** Universal function approximation underpins neural networks' capacity to represent nonlinear relationships, but realizing this capability in optical hardware requires engineering the computational features encoded in light. Here, we show that wavelength diversity enhances optical function-approximation expressivity through wavelength-scaled Fourier features generated by a shared phase encoder, without increasing the number of input-encoded harmonics. Multiple wavelengths contribute to the represe...

---

### 27. SpikeQ: Spike-Guided Post-Training Quantization for Spiking Neural Networks

**Authors:** Kai Sun, Peibo Duan, Zhanglu Yan, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23046v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23046v1)

**Summary:** On neuromorphic chips, spiking neural networks (SNNs) consume far less energy than artificial neural networks (ANNs), but the limited memory of these chips requires low-bit synaptic weights and membrane potentials. Existing post-training quantization (PTQ) methods provide them without retraining and, like those for ANNs, minimize numerical errors such as the mean squared error (MSE). In an SNN, however, a quantization error reaches later layers only through the spikes it flips. We find that erro...

---

### 28. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 29. A restart rule for genetic algorithms based on Schnabel census

**Authors:** Anton Eremeev, Yulia Zakharova

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22211v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22211v1)

**Summary:** A new adaptive restart rule for Genetic Algorithms (GAs) is considered. The rule is based on the Schnabel Census method, originally developed for statistical estimation of a size of animal population. In this paper, the Schnabel Census method is applied as a heuristic to estimate the number of different solutions that may be visited with positive probability, given the current distribution of offspring. The rule consists in restarting a GA as soon as the maximum likelihood estimate reaches the n...

---

### 30. Attention over noisy examples: generalization and memorization in the exponential Hopfield network

**Authors:** Francesco Alemanno

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22191v2) | 📄 [PDF](https://arxiv.org/pdf/2610.22191v2)

**Summary:** In Hebbian learning from examples, a Hopfield network retrieves archetypes seen only through noisy examples. We study it in the exponential Hopfield model: one softmax attention step with the unlabelled examples as keys. A signal-to-noise analysis gives the overlap with an unseen archetype in closed form: a majority-rule law in which an attention entropy replaces the dataset entropy. At high temperature the archetype is lost in the crosstalk; at low temperature the softmax freezes on the closest...

---

### 31. Beyond the Hamming Cliff: Compact Spatial Encodings Preserving Semantic Distance in Spiking Neural Networks

**Authors:** Sergio Davies, Muhammad Aitsam, Morgan-Tyler Stone, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22083v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22083v1)

**Summary:** By pre-processing input signals with Gray, Thermometer, Johnson and hybrid encodings before passing them to spiking neural networks running on SpiNNaker hardware, Davies et al.(2025) address the semantic-spatial disparity that causes the ``Hamming cliff'' in standard binary representations. Continuous semantic patterns are presented as a set of simultaneous spikes at the input layer, preserving ultra-low latency processing. Training the network on multiple continuous values under each scheme, an...

---

### 32. Approaching Backpropagation Accuracy with Weight Perturbation on MNIST

**Authors:** Patrick Inoue

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21665v1)

**Summary:** Weight perturbation (WP) estimates learning directions from random parameter perturbations and a scalar change in loss, without backpropagating derivatives. We examine how batch size, training duration, and estimator stabilization affect its attainable accuracy in fully connected MNIST networks. In the shallow configuration, large-batch training reaches approximately 97\% test accuracy, compared with an early backpropagation (BP) reference near 97.5--98\%. The same comparison exposes a substanti...

---

### 33. First Mathematical Runtime Analyses of Evolutionary Multitask Multi-Objective Optimization

**Authors:** Danyang Zhang, Weijie Zheng

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21311v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21311v1)

**Summary:** To facilitate the solving of complex problems, evolutionary multitask optimization is regarded as a promising technique due to its capacity for cross-task knowledge transfer. In contrast to empirical evidences, no mathematical runtime support exists for this technique within the domain of multi-objective optimization. In this work, we aim to fill this important gap. We analyze how the representative multiobjective multifactorial evolutionary algorithm (MO-MFEA) covers the Pareto fronts of two bi...

---

### 34. IWOO: Wave Optics Optimizer Improved with Hybrid Strategies for Numerical Optimization and Engineering Applications

**Authors:** Rui Du, Yaming Zhang, Yongpeng Wen, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.23994v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23994v1)

**Summary:** The Wave Optics Optimizer (WOO) incorporates optical diffraction and interference into numerical optimization and has shown competitive performance in benchmarks and engineering applications. However, it can converge slowly, become trapped in local optima, and lose search effectiveness in later iterations. This paper proposes an Improved Wave Optics Optimizer (IWOO) that integrates four complementary strategies. First, a good point set and opposition-based learning are combined in GPS--OBL initi...

---

### 35. Controlling the latency in temporal coded spiking models for neuromorphic datasets

**Authors:** Alban Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19732v1)

**Summary:** Exploiting temporal information in datasets with high temporal dependencies (such as spoken keyword recognition) by spiking models is still an open problem. Promising frameworks include Time-To-First coding (TTFS) and the inclusion of synaptic delays into learning. In TTFS, neurons are forced to spike at most once, forcing the network to found its learning on the spiking times of neurons rather than their spiking rate. Some models use the TTFS framework to directly compute the spiking time of In...

---

### 36. When the implementation matters more than the algorithm: NSGA-II and other multi-objective optimizers in engineering design tools

**Authors:** Luciano Ambrosini

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.22397v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22397v1)

**Summary:** Engineering design tools increasingly embed optimizers as ready-made components that users select by algorithm name, while operator settings and bound, integer and duplicate handling stay fixed inside each tool. This study tests whether the name predicts the result. A tool-agnostic harness exposes one deterministic black box, an emulator of a published 22-variable mixed-integer building-performance problem, to the native optimizers of three Grasshopper plug-ins, to canonical NSGA-II, SMS-EMOA an...

---

### 37. Design and Analysis of Temporal Representations in Neural Networks

**Authors:** Alban Colas-Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19730v1)

**Summary:** The ability to represent temporal information is often hypothesized to underlie the efficiency and learning capabilities of biological neural networks. This motivates the development of spiking neural networks. However, it remains unclear how temporal information is actually represented in neural networks and how different forms of temporal representation affect performance and computational efficiency. We introduce the notion of the degree of temporal representation of a neural network, defined...

---

### 38. A Time-Variant Spiking Neuron from a Unified State-Dynamics Perspective

**Authors:** Jing Yang, Qianhui Liu, Gang Pan, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.23981v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23981v1)

**Summary:** Spiking neural networks (SNNs) have increasingly incorporated rich neuronal dynamics to enhance temporal processing. However, richer dynamics do not necessarily enable neurons to adapt how information is processed over time. To examine this issue systematically, we introduce a unified state-dynamics framework that characterizes diverse spiking neurons through a common formulation and enables direct comparison of their dynamical designs. The framework reveals a common limitation of existing neuro...

---

### 39. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 40. Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine

**Authors:** Thomas Hannagan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19220v2) | 📄 [PDF](https://arxiv.org/pdf/2610.19220v2)

**Summary:** The Continuous Thought Machine (CTM) is a recurrent network that attends to inputs and makes predictions based on the synchronization between its neurons. On tasks spanning many domains, it displays emergent thought processes that have not been explained. We report a number of findings about how the CTM classifies images, focusing on ImageNet. Thinking steps are attracting but strongly non-normal maps exhibiting balanced amplification (Murphy and Miller, 2009); while attraction is already presen...

---

### 41. LLM Evolutionary Search Strategies Should be Compared by Tokens

**Authors:** Tal Oved, Roi Pony, Oshri Naparstek, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.23977v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23977v1)

**Summary:** LLM evolutionary search is currently evaluated by counting proposals (candidate programs). We demonstrate this metric hides the true cost of search, and redo the comparison using tokens. By replaying 600 logged runs across 5 tasks and 3 methods, we show that proposal costs vary wildly from 16k to 39k tokens. In equal-proposal comparisons, this silently grants some methods up to 1.9x the compute of others, and gives evolution roughly 6x the budget of independent sampling. When we match token budg...

---

### 42. Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization

**Authors:** Bum Jun Kim

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18085v1)

**Summary:** We show that two Transformers representing the same function can follow different training trajectories. For example, doubling a query matrix and halving its key matrix preserves the model's function but changes the gradient scales seen by the optimizer. Our theoretical analysis establishes that standard block-local first-order optimizers fail to scale updates with parameters under a shared learning rate. For AdamW, transforming the first- and second-moment estimates alone does not correct the m...

---

### 43. Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks

**Authors:** Francesco Panetta, Federico Di Valerio, Michela Proietti

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17998v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17998v1)

**Summary:** Spiking Neural Networks (SNNs) are promising for energy-efficient neuromorphic computing, but they still suffer from catastrophic forgetting when learning tasks sequentially. This work investigates the integration of Experience Packing and Replay (EPR) as a memory-efficient continual learning strategy for deep SNNs under low-latency constraints. The proposed framework combines Batch Normalization Through Time stabilized VGG9 SNNs with Spike Activation Maps (SAM), which provide forward-only expla...

---

### 44. Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation

**Authors:** Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17969v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17969v1)

**Summary:** Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensiona...

---

### 45. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 46. FidLIF: Parallel Training of High-Fidelity Spiking Neurons with Exact BPTT

**Authors:** Kaixiang He, Yujie Wu

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16924v1)

**Summary:** Although spiking neural networks (SNNs) show promise in energy-efficient computing through event-driven computation and stateful temporal processing, their recurrent membrane dynamics render their training inherently sequential and inefficient for long sequences. Existing methods achieve full-sequence parallelism in SNNs through two main strategies: redesigning or approximating spiking dynamics to avoid reset-coupled temporal dependencies, or relying on iterative relaxed fixed-point solvers that...

---

### 47. Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning

**Authors:** Huan Luo, Na Lu, Xiaopeng Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16921v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16921v1)

**Summary:** Online motor imagery-based brain-computer interfaces (MI-BCIs) typically decode continuous EEG using fixed-length sliding windows that may be misaligned with neural events. Existing window optimization methods often evaluate windows independently, overlooking temporal dependencies and potentially producing fragmented or physiologically implausible selections. We propose Temporal Structure Embedded Reinforcement Learning (TSE-RL), a framework that incorporates prior knowledge of MI event structur...

---

### 48. DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning

**Authors:** Yuxiang Zeng, Kun Xie, Yang Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16822v1)

**Summary:** Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves directed computation...

---

### 49. naspaclust: A hybridisation of spatial fuzzy clustering with nature-inspired optimisation

**Authors:** Bahrul Ilmi Nasution, Rezzy Eko Caraka, Robert Kurniawan

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16356v1)

**Summary:** We present an overview of R package called \texttt{naspaclust}, a tool for spatial fuzzy clustering improvement by hybridising the Fuzzy Geographically Weighted Clustering (FGWC) with nature-inspired optimisation algorithms. There are seven optimisation algorithms in general, namely Artificial Bee Colony, Flower Pollination Algorithm, Gravitational Search Algorithm, Harris-Hawk Optimisation, Intelligent Firefly Algorithm, Particle Swarm Optimisation, and Teaching-Learning Based optimisation. The...

---

### 50. CIPHEUR: LLM-Guided Structural Search Control for Conflict-Graph Optimization

**Authors:** Yuqing Cheng, Yan Jia, Yanjie Song, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16158v1)

**Summary:** Conflict-graph search can stagnate despite effective operators when interventions fail to address the conflicts blocking progress. A disruptive intervention may also require further search before its value emerges. We propose CIPHEUR, a large language model (LLM)-guided framework that connects conflict evidence to coordinated intervention and recovery through Structured Intervention Units (SIUs). The shared control interface supports offline synthesis of executable policies and online contextual...

---

## q-bio.NC

**50 papers**

### 1. ZENO: Nonlinear filtering with Zakai Equation Neural Operators

**Authors:** Aaditya Prasad, Steven W. Flavell, Brian DePasquale

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32926v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32926v1)

**Summary:** State inference and parameter learning for nonlinear filters is a core computation for scientific machine learning with varied applications in engineering and neuroscience. The unnormalized filtering distribution is governed by the Zakai equation, a stochastic partial differential equation (SPDE) that combines the forward Kolmogorov operator (known as the Fokker-Planck equation) with observed likelihood updates. Although solving these high-dimensional SPDEs is often impossible analytically and i...

---

### 2. Estimation of the Cyclopean Eye from Binocular Free Visual Explorations

**Authors:** Maria F. Alcala-Durand, J. Camilo Puerta-Acevedo, Julián D. Arias-Londoño, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32564v1)

**Summary:** Binocular video-oculography records separate signals for each eye, yet human visual processing and oculomotor control operate relative to a single, virtual cyclopean eye. This study addresses the estimation of the cyclopean eye during binocular free visual exploration, a target-free paradigm widely used for the screening of neurological disorders. Using eye-tracking data collected at 1 kHz from 113 participants across three cohorts (patients with Parkinson's Disease, age-matched healthy controls...

---

### 3. From Heterogeneity to Function: Enhanced Modular Dynamic Range in Hierarchical Brain Networks

**Authors:** Filipe V. Torres, Mauro Copelli, Leonardo L. Gollo

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32328v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32328v1)

**Summary:** Hierarchical and modular organization defines brain architecture, yet how it supports flexible computation and functional specialization remains unclear. Although dynamic range is a hallmark of efficient information processing, its distribution across modules and hierarchical levels remains largely unexplored. Here, we show that hierarchical-modular networks naturally generate heterogeneous modular dynamics and firing rates, extending regimes of critical-like dynamics with enhanced intrinsic tim...

---

### 4. Phase-based Edge Coupling: Modeling Overlapping Functional Architectures and High-Order Edge-to-Edge Interactions in EEG Networks

**Authors:** Chengcheng Wu, Zichen Shi, Jiayang Xu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32286v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32286v1)

**Summary:** Network neuroscience has traditionally relied on node-centric approaches, which are inherently limited in capturing the brain's overlapping functional architectures and higher-order edge-to-edge interactions. The emerging edge-centric paradigm addresses this gap by shifting the analytical unit from nodes to edges. However, while edge-centric models have been established for DTI and fMRI, comparable EEG methodologies have yet to be developed. In this study, we proposed a Phase-based Edge-centric ...

---

### 5. Virtual Placebo: a scoping review of control conditions in randomized controlled trials of psychological immersive virtual reality interventions

**Authors:** Madis Vasser, Mary-Ann Kubre, Kadi Tulver, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32232v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32232v1)

**Summary:** Research on immersive virtual reality (IVR) as a therapeutic tool is growing rapidly, with randomized controlled trials (RCTs) now commonplace. Yet the control conditions in many of these studies that claim strong specific IVR effects vary from usual care to active immersive experiences, making it difficult to draw clinically meaningful conclusions. We conducted a scoping review of recent literature on psychological IVR interventions to assess the main forms of control conditions used and their ...

---

### 6. A Mathematical Theory of the Jacobian Lens

**Authors:** Mitchell Ostrow, Daoyuan Qian, Toni Liu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31955v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31955v1)

**Summary:** Recent work from Anthropic introduced a new interpretability tool, called the Jacobian lens (J-lens, Gurnee et al., 2026). This method identified linear directions in the hidden states of frontier language models that had properties reminiscent of working memory-like representations. However, it is unclear what mechanistic properties of such features make them detectable to the J-lens. To this end, we introduce a mathematical theory of the J-lens, and show that it preferentially identifies coher...

---

### 7. Dynamics of random recurrent neural networks: colored noise and sublinear activations

**Authors:** German Mato, Facundo Rigatuso, Gonzalo Torroba

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31575v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31575v1)

**Summary:** We study the dynamics of recurrent neural networks with random couplings, sublinear odd activation functions, and temporally correlated noise. Using large N methods, we determine stationary correlations and distinguish the loss of local linear stability from the onset of chaos, characterized by a positive largest Lyapunov exponent. These thresholds delimit an intermediate regime in which local instability coexists with asymptotic stability under a common noise history. Their separation depends o...

---

### 8. Music Between Two Minds: Individual Signatures, Shared States, and the Emergence of Creative Interaction

**Authors:** Tatsuya Daikoku, Risa Kobayashi, Rina Tabuchi, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31131v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31131v1)

**Summary:** Some of the most valued forms of human creativity arise between people-in conversation, collaboration, and improvised music-yet how two minds jointly regulate the flow of novelty in real time remains unknown. Here we examined the information dynamics of interpersonal improvisation using 986 professional jazz improvisations. Pitch-based fluctuations of uncertainty and surprise behaved as signatures of individual identity: the two partners differed within 90% of takes, performers were identifiable...

---

### 9. Gate-Based Feature Importance in Simulation-Based Inference for EEG: A Cautionary Tale

**Authors:** Shrivatsa Deshmukh, Sasha Brenner, Thomas R. Knösche, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30364v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30364v1)

**Summary:** Simulation-based inference (SBI) provides a powerful way to fit mechanistic models to data, but offers little insight into which information in the data shapes the inferred parameter values. It could therefore benefit from robust and inexpensive interpretability methods. Learned weighting mechanisms such as feature gates provide a potential route to low-cost interpretability, although their interpretation assumes that predictive training reveals which inputs drive performance. We examined this a...

---

### 10. The medium is the message: How neurometabolic entanglement generates conscious experience

**Authors:** Terrence W. Deacon, Miguel Garcia-Valdecasas, Michael Jacob

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30217v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30217v1)

**Summary:** Most neuroscientific accounts of consciousness assume that conscious experience is constituted by the information conveyed between neurons. The physical-chemical details of the metabolic and physiological processes that convey this information are correspondingly presumed to be relevant only insofar as they support the organization of information processes. We describe an alternative perspective that denies this presumed independence of the processing of neural information and the metabolic-phys...

---

### 11. Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition

**Authors:** Pavlos Poulos, Katelyn Sadorf, Themos Stafylakis, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29720v2) | 📄 [PDF](https://arxiv.org/pdf/2610.29720v2)

**Summary:** Spiking Neural Networks (SNNs) promise energy-efficient inference through sparse, event-driven computation, yet remain constrained on continuous, context-dependent tasks such as automatic speech recognition (ASR). A key bottleneck is the Leaky Integrate-and-Fire (LIF) neuron, whose membrane decay erases information across pauses and phonetic boundaries while it must both extract features and retain long-range context. Inspired by cortical separation of nonlinear filtering and somatic integration...

---

### 12. Vagus nerve stimulation strengthens beta- and gamma-rate auditory steady-state responses in rat cortex

**Authors:** Shinichi Kumagai, Tomoyo Isoguchi Shiramatsu, Karin Oshima, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29042v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29042v1)

**Summary:** Background: Gamma entrainment using sensory stimulation (GENUS) is under study as a treatment for neurological disease, but cortical engagement is variable. Vagus nerve stimulation (VNS) modulates cortical state and sound-evoked beta-gamma activity, suggesting that it may strengthen responses to rhythmic sensory input. Objective: To determine whether VNS strengthens auditory steady-state responses across beta and gamma rates and whether the effect depends on cortical region and sensory drive. Me...

---

### 13. A Reverse-Gold Theorem: Positive-Data Identification by Substrate-Bounded Contrastive Learners

**Authors:** Rakesh Sengupta

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28747v1) | 📄 [PDF](https://arxiv.org/pdf/2610.28747v1)

**Summary:** Gold's theorem shows that no learner can identify an arbitrary language in a superfinite class from positive presentations alone. We prove a positive result of a different shape. Fix an innate \emph{recursive contrast operator} $R$ mapping any string to a finite set of structurally bounded perturbations of it, and a discriminative scorer of bounded capacity trained by InfoNCE-style contrastive estimation \citep{vandenoord2018,macollins2018} on self-generated perturbations. Under a faithfulness c...

---

### 14. What I Disbelieve: Quantifying Belief With Negative Ranking Functions

**Authors:** Hanbin Go, Britt Anderson

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28357v1) | 📄 [PDF](https://arxiv.org/pdf/2610.28357v1)

**Summary:** A challenge in exploring the psychology of human uncertainty is its measurement and quantification. Prior work has focused almost exclusively on probability, while the formal theories developed in philosophy are rarely tested. We tested Wolfgang Spohn's ranking theory, a normative account in which belief is graded by ordinal ranks of disbelief that combine by minimization rather than addition, as a descriptive model of human belief. Across six experiments, participants assigned ranks of disbelie...

---

### 15. Does a Flux-Defined Markov Blanket Screen Self-Replicating Gray--Scott Spots? A Computational Test of a Blanket Condition from the Free Energy Principle

**Authors:** John E Pearson

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27235v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27235v1)

**Summary:** Friston's free energy principle holds that a system separated from its environment by a Markov blanket---a boundary whose states statistically screen its interior from its exterior---can be treated as performing approximate Bayesian inference, and that such blankets arise wherever coupling is short-range. We test this blanket condition in a concrete nonlinear pattern-forming system: self-replicating spots in a reaction-diffusion model that persist, compete, and reproduce. Directed boundary excha...

---

### 16. Cross-disorder Learning of Imaging-derived Joint Mophometric Markers in Alzheimer's and Parkinson's Diseases

**Authors:** Yuji Zhao, Boris Gutman

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27150v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27150v1)

**Summary:** As two most prevalent neurodegenerative diseases (NDDs), Alzheimer's disease (AD) and Parkinson's disease (PD) shared commonalities both in symptomology and pathophysiology. However, to what extent and in what way these two distinct disorders overlap remain underexplored. In this study, we propose an explicit, interpretable and spatially adaptive transfer learning framework to elucidate the morphometric biomarkers linked to AD and PD. We applied such high-dimensional machine learning model to tw...

---

### 17. Representing short-term movement to reveal animal identity and learning progress

**Authors:** Ping Zhang, Quang-Huy Nguyen, Yingtie Lei, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27140v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27140v1)

**Summary:** How learning progresses over time and varies across individuals is a longstanding question in cognitive and behavioral science. However, a major challenge is identifying observable behavioral measures that faithfully capture learning progression. Existing approaches commonly rely on predefined behavioral features or task-level performance, while fine-scale posture and movement in freely behaving animals remain less explored. In this paper, we ask: can short-term movement trajectories reveal lear...

---

### 18. Ontic state recovery through prediction

**Authors:** Ping Zhang, Quang-Huy Nguyen, Yingtie Lei, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27139v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27139v1)

**Summary:** We encounter a system through its responses, yet its state concerns how the system is. Predicting further responses promises knowledge beyond what is immediately observed. What that knowledge tells us about the system's state depends on what we mean by a state in the first place. We give this notion a model-relative meaning: a state is the complete response profile over a specified query universe, and configurations agreeing on every query are regarded as the same state. From this perspective, a...

---

### 19. Affective Valence as the Interoceptive Rate of Change of Jacobian Scale

**Authors:** David Balduzzi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26350v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26350v1)

**Summary:** Affect is widely held to depend on interoception. This paper proposes that valence is the rate at which interoception moves a self-sustaining system's responsiveness relative to its terminal set (roughly, death). Responsiveness is formalised as the scale of the system's Jacobian and interoception as its internal inputs: receptors, signals and forecasts of its energy reserve. Changes in responsiveness that bypass interoception, such as brain damage, are not felt. Language models have no valence b...

---

### 20. PyGPLA: A Python Package for Generalized Phase Locking Analysis

**Authors:** Amir Khani, Christian Beste, Shervin Safavi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26304v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26304v1)

**Summary:** Spike-field couplings measure the links between neuronal spiking and local field potential (LFP) and provide a tool to study how neural populations coordinate activity across spatial and temporal scales. While modern high-density electrophysiology enables the simultaneous recording of numerous LFP channels and neuronal units, this massive scale poses significant statistical and computational challenges for conventional pairwise coupling analyses. The number of channel-unit comparisons grows rapi...

---

### 21. HP-GSBS: Accelerating greedy state boundary search with reusable interval statistics

**Authors:** Yanzhe Zhao, Yongzhang Ji

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25898v2) | 📄 [PDF](https://arxiv.org/pdf/2610.25898v2)

**Summary:** Greedy State Boundary Search (GSBS) identifies transitions between relatively stable neural activity patterns in continuous recordings. Repeated template reconstruction and correlation evaluation make analyses across recordings and parameter settings computationally expensive. We present HP-GSBS, an open-source implementation that expresses the matching objective as additive interval contributions and computes t-distance from reusable correlation statistics. Streaming candidate reduction, sequen...

---

### 22. Simulating Infant Senses with Age-Tuned Networks

**Authors:** Somesh Mohapatra

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25377v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25377v1)

**Summary:** What a newborn sees, hears and feels, and how this changes month by month, has been measured sense by sense, with different methods and in different units. We bring these measurements together for the first two years of life and ask whether small neural networks tuned to a given age can turn them into a quick, inspectable simulation of sensory perception. Each sense's immaturity is written as a fixed, age-indexed filter on the input, and a small prediction network learns behind it over the first...

---

### 23. Spontaneous brain-wide rotational dynamics constrain cue-evoked behavior

**Authors:** Sihan Chen, Yunlong Xu, Doruk Efe Gökmen, et al.

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25061v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25061v1)

**Summary:** Uncovering low-dimensional representations of brain-wide neural dynamics and their relationship to behavior remains a central challenge. Here, we show that spontaneous brain-wide rotational dynamics constrain cue-evoked behavior and learning. To systematically establish these findings, we developed a dimensionality-reduction technique called Rotational Component Analysis (RCA) that optimizes the detection of low-variance rotational modes even within individual trials. We applied RCA to motor-cor...

---

### 24. Multilingual Brain Decoding Reveals Shared Cortical Semantic Geometry

**Authors:** Yi Guo, Yong Hu, Michael Kwok-Po Ng, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.26927v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26927v1)

**Summary:** Human languages differ markedly in lexical and syntactic form yet can convey similar semantic content. The neural basis of this cross-language semantic commonality remains unclear. Here we developed a multilingual brain decoding framework and analysed brain recordings from 227 participants spanning Chinese, English and French. We found that cortical semantic representations exhibited consistent semantic geometry relationships across languages and individuals, revealing a shared cortical semantic...

---

### 25. Longitudinal fMRI reveals multi-network reconfiguration and a recurrent frontoparietal shift across rest and task states during adult aging

**Authors:** Tingshan Liu, Wanxin Dong, Hairong Zheng, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24433v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24433v1)

**Summary:** Functional connectivity changes across adult aging, but most evidence is cross-sectional, and covariance-based connectivity depends on blood oxygenation level dependent (BOLD) fluctuation amplitude. Covariance decline can reflect changing fluctuation amplitude, and its interpretation may depend on whether normalization uses signal amplitude or includes estimated noise. It is also unclear which longitudinal changes recur across brain states. We analyzed 852 adults (baseline age 36-89 years) from ...

---

### 26. Spaceflight-associated Motion Sickness in Commercial Crew Astronauts

**Authors:** Torin K. Clark, Aaron A. Allred, Jaime Mateus, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24216v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24216v1)

**Summary:** Spaceflight-associated motion sickness, including space motion sickness (SMS) and terrestrial readaptation motion sickness (TRMS), has presented as the most operationally limiting effect on the human in the days following a gravity transition. Published data suggest that astronaut head movements provoke symptoms, but those studies rarely controlled for them. Most previous studies use postflight retrospective reporting and have not quantified temporal dynamics or persistence of symptoms; no study...

---

### 27. Deep LLM layers expose passage-level context in EEG during silent reading

**Authors:** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23638v1)

**Summary:** In a previous report we showed that a decoder can recover open-vocabulary word-level information from 19-channel EEG recorded during silent reading, by aligning short EEG windows with hidden-state embeddings of the presented word taken from a large language model (LLM). That analysis contrasted two of the model's 33 layers: the context-free input embedding and one mid-depth layer. Here we ask how EEG-decodable structure is distributed over the full depth of the language model. We trained one dec...

---

### 28. Distributional signatures of computation: inferring mechanisms from computation time distributions

**Authors:** Céline van Valkenhoef, Catherine Schuman, Nikolaus Kriegeskorte, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23607v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23607v1)

**Summary:** Computational complexity theory provides a framework for analysing abstract models of computation, whereas computational systems operate as finite physical implementations whose behaviour is shaped by their architecture and physical substrate. In such systems, computational organisation cannot be directly characterised from algorithms or internal representations. Building on the use of reaction time distributions to constrain mechanisms in cognitive science, we introduce an empirical framework f...

---

### 29. EEG Lempel-Ziv Complexity vis-à-vis Autocorrelation Function

**Authors:** Pedro Montoya, Ignacio Cifre, José Luis Rosselló Sanz, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23231v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23231v1)

**Summary:** Measures of signal complexity have become increasingly popular in electroencephalography (EEG), where they are often interpreted as indicators of neural information processing, dynamical richness, or conscious state. In contrast, classical measures of temporal dependence, such as the autocorrelation function (ACF), remain more directly linked to known physiological mechanisms and are easier to interpret. The present work revisits, for the EEG practicioner, the relation between normalized Lempel-...

---

### 30. What Shapes Brain Alignment of Large Language Models during Dialogue? Insights from Language Production and Comprehension

**Authors:** Yuko Nakagi, Yuya Chiba, Yasue Kishino

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.22961v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22961v1)

**Summary:** Brain alignment of large language models (LLMs) offers a way to investigate representational similarities between LLMs and the human brain during language processing. While previous studies have mainly focused on passive language comprehension, little is known about such alignment during dialogue, in which speakers engage in both language production and comprehension. In this study, using fMRI data collected during dialogue, we examine brain alignment during language production and comprehension...

---

### 31. Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies

**Authors:** Yiran Huang, Zeyong Zhang, Bharat Biswal, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22706v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22706v1)

**Summary:** Multimodal large language models (MLLMs) offer scalable annotations of social and affective content, but their temporal agreement with human judgments and neural predictive value require further evaluation. We compared diffusion-based and autoregressive MLLMs with continuous human Theory of Mind (ToM) and affective valence ratings across three short cartoon movies. Behavioral analyses assessed temporally aligned Pearson correlations, rating distributions, and the effects of preceding scene descr...

---

### 32. Alignment of visual brain encoding models with individual perceptual similarity judgments

**Authors:** Daniel Chong, Haomiao Chen, Keith W Jamison, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22569v2) | 📄 [PDF](https://arxiv.org/pdf/2610.22569v2)

**Summary:** Encoding models that predict brain activation responses to images have traditionally been trained to maximize accuracy when predicting observed brain data. However, their internal representations may not reflect individual human perception. In this work, we investigate whether we can fine-tune brain encoding models to better align their representations with individuals' similarity judgments. Using similarity judgments of 100 images from 8 participants in the Natural Scenes Dataset (NSD), we adap...

---

### 33. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 34. Mutual Information in High-Dimensional Neural Coding

**Authors:** Zimo Li, Yuchang Tian, Matthew P. Leighton, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22206v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22206v1)

**Summary:** Estimating mutual information in large neural populations is limited by the exponential growth of possible neural response patterns. Here we apply a Monte Carlo framework to make this problem tractable by sampling from a conditionally independent population model fit from single-neuron responses. The estimator accurately recovers analytical ground truth, corrects finite-data bias, and scales to empirical recordings containing 100 to 10,000 neurons from visual cortex, hippocampus, and retina. Acr...

---

### 35. Transferable conditional brain charts link cortico-subcortical structure to Alzheimer's disease progression

**Authors:** Nitin Sharma, Sicheng Dai, Francesco A. Mallus, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21660v1)

**Summary:** Normative models chart how brain measures vary across the lifespan, expressing each individual as a deviation from a healthy reference. However, most regional models of cortical thickness disregard dependencies between cortical and subcortical anatomy, and transferring them to a new site typically requires retraining or a recalibration of location and scale alone. We condition lifespan norms of cortical thickness on subcortical volume, such that each deviation indicates whether an individual's c...

---

### 36. Neural Computation Runs on Dissipative Structures Under Cyclic Calibration: A Systems Perspective on Sleep

**Authors:** Javier Diaz

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21486v1)

**Summary:** Biological function operates far from thermodynamic equilibrium, sustained by metastable structures that continuously cycle through synthesis, function execution, and degradation--consuming energy and exporting entropy in the process. Neural computation exemplifies this dissipative organization, relying on low-entropy structures engaged in dynamic processes that define key information transfer and processing parameters such as gain, threshold, and integration time. This perspective proposes that...

---

### 37. Language Models Share a Readout Bottleneck in Working Memory

**Authors:** Dongyu Gong

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21176v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21176v1)

**Summary:** Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a neighboring but incorrect serial position. We ask whether this shared behavioral signature reflects a shared mechanism. The literature offers two candidate accounts. On a precision account, softmax attention cannot concentrate its weight on the item N positions back, so adjacent it...

---

### 38. Statistical Mechanics of Spike Trains: Self-Consistent Activity Ensembles and Phase Transitions

**Authors:** Jan Pyrzowski, Laura Messio, Guillaume Marrelec, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20971v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20971v1)

**Summary:** We introduce a statistical-mechanical framework for spiking neuronal systems in which entire spike trains, defined as spatiotemporal configurations of discrete events, are treated as microstates of the system. Instead of modeling explicit network dynamics, we construct an ensemble over complete spike histories and assign to each configuration an effective energy functional that quantifies its consistency with intrinsic synaptic interactions.   This formulation leads to a Boltzmann-like distribut...

---

### 39. Cross-subject decoding of imagined speech from scalp EEG: a leakage-controlled evaluation on three public corpora

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20954v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20954v1)

**Summary:** Objective. A decoder of imagined speech that works for a new user without calibration would make a non-invasive speech interface practical. We tested whether imagined-speech content recorded with scalp electroencephalography (EEG) transfers across people, and examined why accuracy within a single person remains low. Approach. We analyzed three public corpora, ds003626, KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, under a protocol that enforces split integri...

---

### 40. How large an effect would we have seen? Positive controls, detection floors and dataset pitfalls in scalp-EEG speech decoding

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20942v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20942v1)

**Summary:** Objective. Studies that decode imagined speech from scalp electroencephalography (EEG) commonly validate their pipelines with a positive control, usually overt speech, and report null results without stating what effect size the pipeline could have detected. Approach. Using ds003626 ("Thinking out loud"), KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, we audited decoding of overt speech, articulator preparation and imagined speech with artifact-channel subset...

---

### 41. Awakening as a Trait-Level Transformation of Consciousness

**Authors:** Riku Ihalainen, Victor Oswald, Gulshan Kumar, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20856v1)

**Summary:** Awakening is reported across contemplative traditions yet remains poorly defined in science, where it is often conflated with transient states induced by meditation or psychedelics, obscuring its significance for theories of consciousness and cognitive architecture. We treat awakening as a functional construct capturing convergence across Hindu and Buddhist sources, phenomenological and psychometric findings, and neuroimaging evidence. Synthesizing these literatures, we find convergent evidence ...

---

### 42. Two dissociable axes of brain hierarchical dynamics track universal and population-specific effects of mindfulness

**Authors:** Victor Oswald, David Zarka, Riku Johannes Ihalainen, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20854v1)

**Summary:** How mental training reshapes the temporal architecture of large-scale brain dynamics and how these mechanisms differ between healthy and clinically vulnerable populations remains poorly understood. Time-averaged neural measures collapse the multi-scale nature of brain activity, obscuring the dynamic processes through which behavioural interventions reorganise hierarchical brain function. Here, applying a sliding-window Temporal Irreversibility Index to source-reconstructed EEG across three compl...

---

### 43. Semantic Alignment of EEG and Text: A Contrastive Learning Framework for Decoding Imagined Speech

**Authors:** Shahryar G. Namdari, Francesco Iacomi, Riccardo Barbieri, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20766v1)

**Summary:** Imagined speech decoding from EEG offers a promising route toward naturalistic brain-computer interfaces. Traditional closed-set classifiers treat semantic categories as independent labels and do not explicitly exploit relationships among linguistic intents, limiting output flexibility. We adapt a multimodal contrastive learning framework to imagined speech, aligning EEG trials with language representations in the embedding space of a frozen pretrained text encoder. An EEG encoder is trained wit...

---

### 44. EEG Correlates of Verbal and Perceptual Reasoning

**Authors:** Gwyneth Rolph

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19979v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19979v1)

**Summary:** Identifying the neural underpinnings of intelligence is one of the major goals of modern intelligence research. However, few imaging studies explore the high extremes of intelligence, and most use only a single composite IQ score. This study used quantitative EEG recordings to investigate correlations between the EEG variables of individual alpha peak frequency, relative power, and coherence, and scores on verbal and perceptual reasoning tests in participants with IQs from the low-average to exc...

---

### 45. Reciprocity coordinates a three-way trade-off in recurrent neural circuits

**Authors:** Xiaoyu Zhang, Mingyi Huang, Yixuan Cui, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19949v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19949v1)

**Summary:** Biological neural circuits contain both unidirectional and reciprocal connections, but how reciprocity affects circuit computation remains unclear. We varied reciprocity \r{ho} across 21 levels in recurrent-network simulations while holding network size, connection density, and directed-edge count fixed. Low-reciprocity networks produced more diverse stimulus-driven activity and performed better on four continuous-input tasks, whereas higher reciprocity generally improved performance on three de...

---

### 46. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 47. Effects of cortisol time-scales in a model of emotion regulation

**Authors:** Michael Buccino, Joshua Ginart, Eva Kaslik, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19282v1)

**Summary:** Stress reshapes cortico-limbic dynamics across multiple timescales, with important consequences for healthy and pathological arousal responses. We develop and analyze a Wilson-Cowan model of prefrontal-amygdala circuitry, incorporating excitatory and inhibitory populations involved in emotional regulation. The effects of stress cortisol are represented as history-dependent modulations of two stress-sensitive interactions: recurrent prefrontal excitation and inhibition of basolateral amygdala pri...

---

### 48. Simulating Alzheimer's amyloid-like pathology on a fly central nervous system connectome

**Authors:** Taeho Jo

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19153v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19153v1)

**Summary:** In Alzheimer's disease, the amount of pathology in the brain is an imperfect predictor of how much function is lost. Pathology leads to that loss through neural circuits, but these cannot be observed neuron by neuron in patients. This study therefore simulated the central nervous system of the adult male Drosophila melanogaster: 166,700 integrate-and-fire neurons wired by the MaleCNS connectome. The simulator reproduced a published fly brain model (rate correlation 0.9997). Three kinds of damage...

---

### 49. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

**Authors:** St John Grimbly, Nicolas Kuske, Evert A. Boonstra, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18617v1)

**Summary:** An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask how each changes survival, perception and the body model the agent learns. Precision sharpens interoceptive posteriors and improves survival. P...

---

### 50. Sense-Making phase transition framework for Affect

**Authors:** Miguel Bosch, Laura Fanfarillo, Gustavo Diez, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18115v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18115v1)

**Summary:** Contemporary accounts of affect emphasize different perspectives, ranging from the regulation of bodily states in allostatic approaches to the relational and sense-making character stressed by enactive theories. Here, we show that affect can be made explicit within the sense-making phase transition framework previously introduced for the perception of an inner sensation. Within this same formal structure, each stable minimum of the sense-making potential defines an affective state: its position ...

---

## stat.ML

**50 papers**

### 1. Singular Geometry of Low-Rank Adaptation

**Authors:** Kamillo Ferry, Anthea Monod, Keisuke Yano

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32854v1)

**Summary:** Low-rank adaptation (LoRA) is now a standard approach to parameter-efficient fine-tuning of large neural networks. Its low-rank factorization is inherently non-identifiable, making LoRA a singular statistical model whose learning complexity cannot be described by parameter dimension alone. We study this complexity using the real log canonical threshold (RLCT) from singular learning theory and how it depends on both the low-rank parameterization and the pretrained network. Under a local lineariza...

---

### 2. Mixed Engression: Distributional Regression for Multivariate Mixed-Type Responses

**Authors:** Seyong Hwang, Kean Ming Tan, Ji Zhu

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32850v1)

**Summary:** Estimating the conditional distribution of multivariate responses with continuous and binary components requires capturing their dependence, respecting their different supports, and accommodating potentially heavy-tailed continuous outcomes. We propose mixed engression, which fits a continuous generator using energy losses induced by bounded discrepancies and then thresholds its soft binary outputs to produce mixed-response samples. Because the discrepancies are bounded, the population objective...

---

### 3. Neural LoFi with Backward Coupling: A Spectral Theory of Cross-Layer Feature Learning

**Authors:** Yatin Dandi, Matteo Vilucchio, Hugo Tabanelli, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32849v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32849v1)

**Summary:** During joint training, backpropagation allows later layers to reshape earlier representations, a feedback mechanism absent from purely layer-wise learning. We extend Neural Low-Degree Filtering (Neural LoFi), a recently proposed layer-wise spectral surrogate for feature learning, to capture this interaction. Starting from the exact backpropagation gradients, we derive a local coupling between a neuron's incoming weights and its corresponding next-layer column. In a controlled small-initializatio...

---

### 4. Generalization properties of the token perceptron: the role of embedding and vocabulary

**Authors:** Dario Bocchi, Matteo Negri, Flavio Nicoletti, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32788v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32788v1)

**Summary:** Large language models are trained to predict tokens from a finite vocabulary, each represented by a vector in a $d$-dimensional embedding space. Therefore, token prediction is a classification problem whose classes have a geometry determined by the embedding. We study how this geometry affects learning in a minimal solvable model: a linear predictor that maps a sequence of $N$ embedded tokens to a $d$-dimensional output through one $d\times d$ matrix per position, trained in the teacher--student...

---

### 5. Structure and Exact Certification of Nonnegative Tensor Decompositions

**Authors:** Haoming Wang, Ming Yuan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32787v1)

**Summary:** We study the structure and exact certification of nonnegative tensor decompositions supplied through rational factor matrices. Every failure of minimality or essential uniqueness contains an irreducible positive exchange between $p$ supplied terms and $q$ competing terms. A dimension count based on the Lovitz--Petrov splitting theorem bounds the effective order of such an exchange, the sum over the modes of the joint factor-span dimension minus one, by $p+q-2$, and this bound is attained at ever...

---

### 6. Sparse Bayesian Neural Networks via Sticky Piecewise Deterministic Markov Processes

**Authors:** August Arnstad, Geir Olve Storvik, Filippo Pagani, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32753v1)

**Summary:** There is growing evidence that the performance of a neural network depends largely on a small subset of its weights, which are typically identified by training a dense network and pruning it afterwards. Within a Bayesian framework, pruning can be directly incorporated through a spike-and-slab prior, providing a proper treatment of the uncertainties involved, both with respect to pruning and to parameter uncertainty. In Bayesian neural networks (BNNs), sampling by MCMC is notoriously hard. We dem...

---

### 7. Strongly Adaptive Online Learning with Time-Varying Movement Costs

**Authors:** Andrew Jacobsen, Emmanuel Esposito, Hao Qiu, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32740v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32740v1)

**Summary:** We study strongly adaptive regret for Online Convex Optimization (OCO) with time-varying movement costs, a setting that evaluates a learner's performance over arbitrary sub-intervals. This framework captures complex sequential decision-making problems where both the environment and the cost of switching decisions fluctuate over time. We propose a novel algorithm which, for any interval $[a,b] \subseteq [T]$, achieves a data-dependent regret bound of $ \widetilde{\mathcal{O}}\left( \sqrt{(D^2+DP_...

---

### 8. Score-Preserving Continual Lasso under Task Shift

**Authors:** Jingyi Guo, Runze Li, Lingzhou Xue

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32708v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32708v1)

**Summary:** Continual learning (CL) aims to learn from sequential tasks while mitigating catastrophic forgetting when historical data are no longer accessible. We study continual learning for high-dimensional sparse linear regression, where $\ell_1$ regularization creates a difficulty absent from continual ridge regression: that recursively reusing an $\ell_1$-penalized estimator can propagate earlier shrinkage and accumulate regularization bias across tasks. We propose score-preserving continual Lasso (SP-...

---

### 9. Acquisition for Spherical-Linear Bayesian Optimization on the Cube

**Authors:** Nathan Wycoff

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32628v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32628v1)

**Summary:** Recent work demonstrated that executing Bayesian Optimization (BO) using simply a linear surrogate with a clever transformation is enough to approximate the performance of the standard Gaussian-Process (GP) based version on high-dimensional test functions. When the decision region is a sphere, this strategy admits rapid exact acquisition. However, it is the unit cube we encounter most often in the BO literature, and in this setting a standard approach, namely a multi-start quasi-Newton method, i...

---

### 10. Contextual Decision Making: Predictive or Generative

**Authors:** L. Jeff Hong, Weihuan Huang, Xinyao Li

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32584v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32584v1)

**Summary:** Contextual decision making uses observed covariates to guide decisions under uncertainty. Two natural approaches are predict-then-optimize (PtO), which learns the conditional expected objective, and generate-then-optimize (GtO), which learns conditional uncertainty and optimizes using generated scenarios. We study when each approach is preferable by examining how the choice of learning target affects statistical accuracy and optimization tractability. Although PtO learns a narrower target, our r...

---

### 11. Batched NN 4D-Var: a performant hybrid model framework for the Integrated Forecasting System

**Authors:** Alban Farchi, Marcin Chrust, Massimo Bonavita, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32582v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32582v1)

**Summary:** Hybrid forecasting systems combining machine learning and numerical weather prediction offer a promising route toward improved forecast skill while preserving physical consistency. In this study, we investigate online learning of state-dependent model-error corrections within the Integrated Forecasting System using 4D-Var. Building on previous work, we represent model error using a neural network embedded within the forecast model and trained from observations through the data assimilation cycle...

---

### 12. Exact Global Minimax Risk near Nonidentification

**Authors:** Kaiyue Yang, Yunan Wu

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32546v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32546v1)

**Summary:** We study squared-error estimation when a nuisance parameter is unidentified on a submodel but affects a target that vanishes there. For models with higher-order profile expansions, we give sufficient conditions under which the largest critical-path minimax risk is the exact asymptotic minimax risk over the full parameter space. An efficient observable feature, negligible calibration error and stable recovery yield one estimator attaining the leading constant uniformly, with the profile coordinat...

---

### 13. Random Jump Forests

**Authors:** Martin Bladt, Rasmus Frigaard Lemvig

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32498v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32498v1)

**Summary:** Random jump forests are introduced as a nonparametric tool for estimating conditional cumulative transition rates and occupation probabilities in multi-state models. The main idea is that a single tree partitions the covariate space for all transitions simultaneously, using partially observed trajectories, and with Nelson--Aalen estimators at the terminal nodes. Occupation probabilities are recovered through the product integral without requiring the Markov assumption. Uniform consistency and a ...

---

### 14. Data Quality Audit and Bivariate Temperature-Humidity Analysis of a Long-Term LoRaWAN Network: Anomaly Detection, PCA, Clustering and Machine Learning

**Authors:** Mamadou Sow

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32438v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32438v1)

**Summary:** Long-term environmental IoT/LPWAN deployments often aggregate heterogeneous data streams from diverse devices without systematic auditing of each variable's actual coverage prior to analysis-an increased risk when multiple sensor types coexist within the same network. This work proposes a C++17 processing pipeline applied to the Tour Perret LoRaWAN dataset (421 937 frames, June 2021--June 2023, 5 devices). A systematic coverage audit integrated into the extraction phase reveals that CO2 is compl...

---

### 15. Optimal Multiclass Online Regret with Arbitrary Label Spaces

**Authors:** Sajad Ashkezari, Shai Ben-David

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32339v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32339v1)

**Summary:** We determine the optimal regret in agnostic multiclass online learning with arbitrary, possibly infinite, label spaces. For every hypothesis class of multiclass Littlestone dimension $d<\infty$, we prove a regret upper bound of $O(\min\{T,\sqrt{dT}\})$ over $T$ rounds, matching the known lower bound. This resolves a question of Hanneke et al. (2023) and extends the optimal binary regret bound of Alon et al. (2021). Our proof strengthens the one-sided expert cover of Hanneke et al. (2023) to a fr...

---

### 16. Empirical concentration for chains with infinite memory

**Authors:** Pierre Alquier, Paul Doukhan

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32265v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32265v1)

**Summary:** Concentration inequalities for time series usually involve unknown quantities measuring dependence. This prevents their direct use as confidence bounds, or as criteria for learning algorithms. Recent works proved empirical concentration inequalities for stationary Markov chains, where the unknown quantities are estimated. We extend this approach beyond the Markov case, by considering stationary chains with infinite memory. We first establish a bounded-differences inequality on bounded Polish met...

---

### 17. Federated Nonparametric Regression with Heterogeneous Clients

**Authors:** Xiaoran Jiang, Anand N. Vidyashankar

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32178v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32178v1)

**Summary:** Whether a federated predictor benefits an individual client depends on both population heterogeneity and estimation uncertainty. We study this question for Nadaraya--Watson regression in a triangular array with potentially different fitting and evaluation distributions. Each client transmits local kernel summaries, allowing the server to construct a covariate-density-weighted federated estimator without centralizing individual observations. A client combines its fitted local predictor with the f...

---

### 18. Covariance-Informed Ensemble Score Filtering: Embedding Localized Covariance Geometry into Score-Based Transport

**Authors:** Siming Liang, Peter Jan van Leeuwen, Hristo G. Chipilski, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32148v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32148v1)

**Summary:** Background-error covariance models are central to atmospheric data assimilation because they spread partial observational information across space, variables, and dynamically coupled scales. Ensemble and variational methods exploit this covariance geometry efficiently, but their standard analysis formulations are largely built around Gaussian or locally quadratic approximations. Score-based ensemble filtering provides a framework for nonlinear distributional transport, but existing Ensemble Scor...

---

### 19. Implicit Neural Representations for Variational Problems on Graphons

**Authors:** Taeyoung Kim, Jineon Baek, Joonkyung Lee, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32147v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32147v1)

**Summary:** We propose a neural exploratory framework for variational problems over graphons, i.e., symmetric measurable functions $[0,1]^2 \to [0,1]$, that arise as limits of dense graph sequences. Such problems are central to two parts of the mathematical literature: extremal graph theory, which studies graph parameter optimisation under given restrictions, often for those graphs with a large number of vertices, and the large deviation theory of dense random graphs, which characterises the structure of ra...

---

### 20. Conditional Flow Models for Offline Maximum Entropy Reinforcement Learning

**Authors:** Hao Cheng, Yuling Jiao, Lican Kang, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32125v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32125v1)

**Summary:** Offline maximum entropy reinforcement learning seeks to estimate the optimal soft action-value function \(Q^*\) from a fixed dataset without further interaction with the environment. Although \(Q^*\) is characterized by the soft optimal Bellman equation, the corresponding Bellman operator cannot be evaluated directly because both the reward distribution and the transition kernel are unknown. Consequently, estimating \(Q^*\) requires the joint treatment of environment modeling and value function ...

---

### 21. DBCM: Dual-Branch Calibration Module for Test-Time Adaptation in Time Series Forecasting

**Authors:** Jaebyeong Jeon, Kunwoo Kang, Sang Yup Lee, et al.

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32071v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32071v1)

**Summary:** Non-stationarity induces test-time distribution shifts in time series forecasting (TSF), resulting in forecast residuals between predictions and the corresponding ground truth. Recent works on test-time adaptation for TSF address this by introducing lightweight calibration modules around frozen forecasters, updated using observations that become incrementally available at test time. Existing approaches typically employ channel-wise adapters, implicitly assuming that forecast residuals are inhere...

---

### 22. Rethinking Representation Geometry in Supervised Contrastive Learning under Long-Tailed Data

**Authors:** Joonhyeok Jeong, Jy-yong Sohn, Kibok Lee

**Published:** 2026-10-23

🔗 [Paper](http://arxiv.org/abs/2610.32039v1) | 📄 [PDF](https://arxiv.org/pdf/2610.32039v1)

**Summary:** Supervised contrastive learning and its balanced variants have demonstrated their effectiveness for representation learning under long-tailed distributions. However, although prior analyses suggest that their optimal representations may exhibit a regular simplex geometry, whether such a geometry is indeed exhibited remains insufficiently understood. In this work, we present a theoretical framework for these objectives that characterizes whether a regular simplex is formed at the optimum. By appl...

---

### 23. Compatible Likelihoods for Flow Matching on Manifolds

**Authors:** Lucas Ng, Georgios Batzolis, Mark Girolami

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31981v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31981v1)

**Summary:** On the simplest non-Euclidean manifold, the 1D flat torus, we exhibit a distribution where a recently proposed extension of Riemannian flow matching is globally optimized by a velocity field that pushes samples away from the data distribution. We trace this failure mode to a property we call compatibility; a likelihood-based flow matching objective is compatible if its population minimizer recovers the marginal velocity field induced by the data and coupling. We give a general condition for comp...

---

### 24. Bayesian Propensity Score Predictive Inference for Extending Trial Findings to Target Populations

**Authors:** Jungang Zou, Joseph E. Schwartz, Roderick J. A. Little, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31915v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31915v1)

**Summary:** The CODIACS Vanguard randomized trial compared a depression care intervention with usual care for patients with persistent depressive symptoms following acute coronary syndrome. We assess whether its findings can be extended to broader patient populations represented by two cohorts constructed from the All of Us electronic health records. This extension is challenging when treatment effects vary across covariates whose distributions differ between trial and target populations. We develop Bayesia...

---

### 25. Combinatorial Characterizations of the Learnability of Conditional Distributions

**Authors:** Mihir Dhanakshirur, Ambuj Tewari

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31890v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31890v1)

**Summary:** We study the PAC-learnability of function classes that map inputs to probability distributions over a finite space. The learner observes i.i.d. input-label pairs, with each label sampled from the conditional distribution of an unknown target hypothesis in the class. We measure learning through excess risk under a bounded proper loss that satisfies two mild assumptions. We introduce the \textbf{fat$_γ$Natarajan dimension}, which generalizes both fat$_γ$ and Natarajan dimension, and prove that its...

---

### 26. Early learning in large residual networks

**Authors:** Vladimir Narovlansky, Boris Hanin

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31783v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31783v1)

**Summary:** We study the early training dynamics of nonlinear residual networks with blocks of zero hidden layers as a model of more general residual networks. We analyze networks in a sequential limit where first width and depth diverge, then the number of training data points diverges, and finally the input dimension diverges. This is a more refined setup compared to the typical mean-field theory analysis in which depth and width diverge but the number of training datapoints and input dimension are fixed....

---

### 27. Phase Transition from Random Features to Fully Trainable Networks

**Authors:** Xin He, Huan Lao, Xiliang Lu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31663v1)

**Summary:** Constructing accurate and computationally tractable approximation spaces is a fundamental task in scientific computing. Partially trainable neural networks bridge fixed random features and fully adaptive representations. This paper quantifies a phase transition pattern in approximation bounds and observes analogous behavior in training errors: a rapid but smooth initial improvement followed by diminishing returns, with a sharper transition under greater initialization mismatch. Under polynomial ...

---

### 28. Reliable AI-Assisted Decisions via Selective Auditing

**Authors:** Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31662v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31662v1)

**Summary:** We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a correctness or safety score. Based on this information, we must decide whether to accept the AI deci...

---

### 29. SympFormer: Inertial Attention Blocks from Damped Hamiltonian Dynamics on Spaces of Probability Measures

**Authors:** Viktor Stein, Levin Maier, Wuchen Li, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31600v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31600v1)

**Summary:** The attention mechanism underpins modern large language models, yet their dynamics remain only partially understood. Recent perspectives interpret attention blocks as interacting particle systems, whose mean-field limits correspond to gradient flows of energy functionals on spaces of probability densities on $\mathbb R^d$ equipped with Wasserstein-type metrics. We extend this viewpoint by deriving accelerated attention blocks from inertial, Nesterov-type damped Hamiltonian dynamics on these dens...

---

### 30. When to Follow the Teacher: Advantage-Based On-Policy Distillation

**Authors:** Mahdi Sabbaghi, George Pappas, Hamed Hassani, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31563v1)

**Summary:** Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the student to follow the teacher at every state of the trajectory, assuming that teacher guidance is always beneficial. We instead distinguish between what the teacher prefers and what actually helps the current student succeed. We introduce Advantage-Based On-Policy Distillation (AOPD), which weights ...

---

### 31. Diffusion Language Models for Perplexity-Aware Black-Box Attacks

**Authors:** Ali Al-Lawati, Elsayed Eshra, Dongwon Lee, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31558v1)

**Summary:** \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this...

---

### 32. Nonparametric autoregressive estimation of probability distributions with parallel gradient boosting

**Authors:** Rémy Chapelle

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31524v1)

**Summary:** Nonparametric estimation of joint probability distributions is a core problem in statistics, which is notoriously challenging with high-dimensional data. Such challenges also arise with conditional distribution estimation and have led to flexible algorithms that aim to tackle the ''curse of dimensionality'' by exploiting predictive structures of lower dimension than the ambient space. In this paper, we study the use of such conditional distribution estimators to estimate joint distributions by f...

---

### 33. SABLE: Scalable Affine Bayesian Latent-space Exploration

**Authors:** Erik Bodin, Lisa Maria Kreusser, Donney Fan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31495v2) | 📄 [PDF](https://arxiv.org/pdf/2610.31495v2)

**Summary:** Complex objects such as engineering designs and proteins are often difficult to optimise because their design spaces exhibit high-dimensional structure and objective evaluations are expensive. Generative models provide continuous latent representations, but their latent spaces can have thousands to tens of thousands of dimensions, creating a regime where the latent dimension $D$ greatly exceeds the evaluation budget. We introduce SABLE, a Bayesian optimisation method for high-dimensional latent ...

---

### 34. Learning to Be Monitored: Causal Bounds and Intervention-Aware Post-Training Recipes for Chain-of-Thought Monitorability

**Authors:** Qiang Fu, Xinyue Li, Andre Wibisono, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31733v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31733v1)

**Summary:** Chain-of-thought (CoT) monitoring aims to detect potentially harmful behaviors in large language models (LLMs) from their CoTs. Intervention-based evaluations measure this property by asking whether a monitor can detect the role of an intervention from the CoT when the targeted behavior occurs, typically using minimal-criterion sensitivity ($\mathsf{TPR_{mc}}$) proposed by~\citep{guan2025monitoring}. However, a target behavior observed under intervention is not necessarily caused by it, and we s...

---

### 35. Dimension-free regimes for unadjusted Langevin in ridge-separable models: A subspace robust Wasserstein analysis

**Authors:** Yuansi Chen, Francesco Pedrotti, Peter A. Whalley

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31431v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31431v1)

**Summary:** The Unadjusted Langevin Algorithm (ULA) is widely used for high-dimensional Bayesian inference. Classical analyses in Wasserstein-2 distance predict an asymptotic bias and a mixing time that grow with dimension, but this metric is stronger than necessary for many statistical tasks. We instead analyze the bias in subspace robust Wasserstein distance, which controls the mean and arbitrary low-dimensional marginals and is therefore well suited to observables typically estimated in practice. For rid...

---

### 36. Metric Conformal Prediction via the Conditional Expected Local Radius

**Authors:** Rui Qiu, Fang Yao, Zhou Yu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31336v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31336v1)

**Summary:** We introduce the conditional expected local radius (CELR) and develop a new conformal prediction method for non-Euclidean responses in general metric spaces. CELR measures local conditional probability concentration, allowing prediction sets to accommodate heterogeneity and multimodality without requiring densities or a vector space structure. Its conditional distribution yields a nonconformity score that is comparable across covariate values and avoids costly transport comparisons between dista...

---

### 37. Deep Learning for Random Objects in Metric Spaces: Beyond Manifold Assumptions

**Authors:** Marcos Matabuena, Xiaokai Luo, Oscar Hernan Madrid Padilla

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31328v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31328v1)

**Summary:** Deep learning (DL) methods have substantially improved predictive performance across a wide range of downstream prediction tasks, enabling new discoveries in multiple domains. However, principled DL methods for non-Euclidean random objects remain relatively scarce, despite the growing importance of modern biomedical outcomes taking the form of probability distributions, random graphs, functions, and other random objects in metric spaces. Motivated by a new generation of digital and clinical biom...

---

### 38. Local Discrimination of Binary Classifiers via Localized AUC Functional

**Authors:** Wenye Ren, Anna Győrffy-Kerekes, Tancredi Dorsi, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31216v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31216v1)

**Summary:** Risk prediction models are frequently evaluated with AUC, which means that during evaluation we are blind to performance heterogeneity, which could lead to bad decision-making in clinics. In this work, we aim to change that by identifying patient cohorts for whom the risk prediction model might not be an accurate predictor. To separate these cohorts, we use a version of the weighted AUC, which we call Localized AUC or LAUC. Using this metric, we build a method that we coin LOCATOR. This method i...

---

### 39. Operationalising Weaker Faithfulness: Recovery, Ambiguity and Computational Limits

**Authors:** Cillian Hourican, Rick Quax

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31724v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31724v1)

**Summary:** Variables can predict an outcome jointly while each is individually independent of it, causing structure learners to discard informative links. We investigate how to operationalise weaker faithfulness through two approaches: selective protection in an adjacency learner and explicit retention of alternative directed graph explanations. Matched experiments show that changes at both an early candidate-removal stage and later pruning can be necessary. In noisy XOR with a descendant (N = 10,000, 20 m...

---

### 40. Prediction Uncertainty Controlled Computer Model Calibration

**Authors:** Ryan Heejoon Byun, Dayeon Yoon, Won Chang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31163v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31163v1)

**Summary:** Computer-model calibration is usually undertaken in service of prediction, yet neither Bayesian Kennedy-O'Hagan (KOH) calibration nor amortized simulation-based inference is built to control the predictive error of the calibrated simulator. When parameters are weakly identified or the data-model discrepancy is misspecified, the simulator-output bands induced by a nominal posterior level can be far from nominal. We propose a two-layer framework that targets predictive miscoverage directly. First,...

---

### 41. What Comes Next and Why: Interpretable Next-Event Prediction with Neuro-Symbolic Rules

**Authors:** Tim Nico Bauerschmidt, Isabel Valera, Jilles Vreeken

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31114v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31114v1)

**Summary:** In real-world applications, being able to explain why a prediction is made is often as important - if not more so - than achieving high accuracy. However, existing methods for sequential event prediction typically prioritize accuracy at the expense of interpretability. Neuro-symbolic approaches offer a promising direction to improve interpretability by learning symbolic rules, but extending them to next-event prediction is challenging due to the presence of temporal dependencies. We introduce RU...

---

### 42. Transformers with CoT Discover Heavy-Ball Acceleration Through Training

**Authors:** Yuxuan Cai, Yuan Cao

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31089v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31089v1)

**Summary:** Modern transformers often solve complex tasks by generating and refining intermediate reasoning steps. To develop a theoretical understanding of chain-of-thought (CoT) reasoning, a notable recent study by Huang et al. (2025) viewed transformers as algorithm executors, and showed that when transformers' CoT steps are supervised by a gradient-descent teacher, they can learn to implement gradient descent for in-context weight prediction in linear regression. In this paper, we study the same in-cont...

---

### 43. Random Projections for Spectral Algorithms: Optimal Rates in Sobolev Norms

**Authors:** Caixing Wang, Yue Wang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30948v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30948v1)

**Summary:** Random projections (RP) offer an effective method for reducing computational and storage overhead while preserving the geometric structure of data. However, existing studies have primarily focused on the optimal generalization performance of specific kernel-regularized algorithms with RP in the well-specified setting and under restrictive conditions. In this paper, we provide a comprehensive and improved analysis of the generalization performance of RP-based spectral algorithms under general con...

---

### 44. Continuous-depth Deep Gaussian Processes

**Authors:** Ying Li, Sanyou Wu, Zi Yang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30890v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30890v1)

**Summary:** Deep Gaussian processes (DGPs) are appealing Bayesian regression models, but their standard discrete-depth parameterization often becomes harder to optimize as depth grows. We argue that depth is better treated as a latent continuous evolution than as a long discrete stack. We therefore propose a continuous-depth formulation in which the latent representation follows a stochastic differential equation with a depth-indexed drift family equipped with a GP-based prior. This reframes the core design...

---

### 45. xVGAE: A Hierarchical Variational Graph Autoencoder for Exchangeable Graphs

**Authors:** Daniele Micheletti, Federica Zoe Ricci, Erik B. Sudderth

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30815v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30815v1)

**Summary:** Graphs play a crucial role in many applications, ranging from drug discovery to social network modeling and astronomy. Generative models for graphs have substantially advanced in recent years, but we identify relatively simple scenarios where state-of-the-art models struggle to converge within a standard compute budget, or exhibit prohibitively slow generation times. We propose a generative architecture that achieves quality competitive with state-of-the-art models and is orders of magnitude fas...

---

### 46. Width and Depth Limits Commute During Training

**Authors:** Ruijia Zhang, Soufiane Hayou

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30729v1)

**Summary:** Recent work established that the infinite-width and infinite-depth limits of residual networks commute at initialization when residual branches are scaled by $1/\sqrt{depth}$. In particular, the network output converges to the same limit whether width and depth tend to infinity sequentially or jointly. We extend this commutativity result to training in linear residual networks. Under the same $1/\sqrt{depth}$ residual-branch scaling (Depth-$μ$P) and the $μ$P width parameterization, we prove that...

---

### 47. Residual Calibration via Local Feature-Space Refinement

**Authors:** Xihao Wang, Chengyao Yu, Ruixing Ming

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30652v1)

**Summary:** Deep neural networks often struggle to provide reliable confidence estimates, making post-hoc calibration essential for reliable decision-making. Existing post-hoc methods largely rely on score-based transformations, which improve marginal calibration but often fail to capture spatially varying miscalibration in local regions of the learned feature space. To address this gap, we propose Local Adaptive Probability Estimation (LAPE), a post-hoc residual calibration framework. Specifically, LAPE tr...

---

### 48. Lifetime-valid decisions by continually evolving AI analysts

**Authors:** Xiaojing Sun, Yuhan Zeng, Xiao Wang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30562v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30562v1)

**Summary:** AI agents increasingly act as analysts whose decision can often be cast as hypothesis tests. Classical tests control the Type I error rate, the probability of rejecting a true null hypothesis, for fixed procedures. However, AI analysts introduce internal randomness and can evolve continuously over time. As AI analysts evolve, the risk of approving versions with Type I error rates above the target can accumulate, and adaptive use of evaluation feedback can lead to overfitting. We introduce contin...

---

### 49. Flow-based Spectral Kernel Learning for Nonstationary Attention

**Authors:** Zi Yang, Ying Li, Alejandro Lancho, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30465v1)

**Summary:** Kernelized attention provides a useful perspective for understanding self-attention as a similarity-based aggregation mechanism, but existing approaches often rely on fixed or stationary kernels, limiting their ability to adapt the similarity structure to complex token interactions. In this paper, we propose flow-based spectral kernel attention (FSKA), a framework for learning expressive nonstationary attention kernels. FSKA formulates kernelized attention through spectral density learning and p...

---

### 50. High-Value Training Data from Noisy, Diverse Sources

**Authors:** Hedi Driss, Evan Frick, Anastasios N. Angelopoulos, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30421v1)

**Summary:** Training state-of-the-art models increasingly requires learning from large, heterogeneous datasets whose examples vary in quality, domain relevance, and source of supervision. Dataweighting---assigning different weights to training examples---offers a general way to control how such data influences training, but learning effective weights at scale remains challenging. We develop a scalable approach to learning dataweights: given a small, high-quality target dataset, we use metagradients through ...

---

