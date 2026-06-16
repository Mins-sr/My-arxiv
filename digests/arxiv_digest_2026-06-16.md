# arXiv Daily Digest - 2026-06-16

Total papers: 350

---

## cs.AI

**50 papers**

### 1. The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers

**Authors:** Alper Yıldırım

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17037v1)

**Summary:** Oppenheim and Lim (1981) showed that natural images stay recognizable when reconstructed from their Fourier phase alone, while the magnitude carries little of their identity. We ask whether trained image classifiers reproduce this asymmetry inside their hidden layers, and we test it causally: given two images, we transplant the phase of one onto the magnitude of the other at a chosen layer and record which image the prediction follows. In PRISM2D, GFNet, and ViT-B/16 the prediction follows the p...

---

### 2. HAMON: Passive Optical Sequence Mixing for Long-Horizon Forecasting

**Authors:** Alper Yıldırım

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17028v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17028v1)

**Summary:** Simple linear and frequency-domain models remain surprisingly competitive in long-horizon time-series forecasting, and recent mechanistic evidence suggests that standard forecasting benchmarks may not require the dense superposed representations that make transformers powerful in other domains. This raises a substrate-level question: if the core forecasting operator is often low-complexity and approximately linear, does it need to be implemented as learned digital temporal mixing? We introduce H...

---

### 3. FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models

**Authors:** Jiaju Han, Ben Zhang, Xuemeng Sun, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17020v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17020v1)

**Summary:** Remote sensing vision-language models have advanced Earth observation understanding, but most existing work remains centered on RGB imagery, leaving the complementary information in infrared data underexplored. Infrared images provide distinctive cues, including thermal intensity structures, object boundaries, and illumination-invariant scene features, which can enrich visual-language learning beyond conventional RGB observations. However, a large-scale RGB-infrared-text dataset for remote sensi...

---

### 4. TokenPilot: Cache-Efficient Context Management for LLM Agents

**Authors:** Buqiang Xu, Zirui Xue, Dianmou Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17016v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17016v1)

**Summary:** As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, ...

---

### 5. TuneJury: An Open Metric for Improving Music Generation Preference Alignment

**Authors:** Yonghyun Kim, Junwon Lee, Haiwen Xia, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17006v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17006v1)

**Summary:** We introduce TuneJury, an open, instance-level pairwise reward model for text-to-music that predicts a music preference score from a text prompt and an audio clip. The released checkpoint is trained on publicly available human-preference labels covering arena-style (A vs. B) votes, metric-alignment preference pairs, crowdsourced pairwise comparisons, and expert aesthetic ratings. The predicted score margin between two clips is well calibrated on our held-out test split, supporting data filtering...

---

### 6. Bayesian Inference and Decision Audits for Public Archives of Frontier AI Evaluations

**Authors:** Yanan Long

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17005v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17005v1)

**Summary:** Public AI evaluations are often read as terminal leaderboards, yet the underlying evidence is a selective time series shaped by reporting rules, benchmark revisions, and missingness. Repeated public archives for LiveBench and Open LLM Leaderboard v2 serve as the primary longitudinal record; LMArena provides a preference stress test; and GAIA and tau-bench contribute limited agentic pilots. Together, these archives instantiate a Bayesian inference problem: under a fixed reporting convention, one ...

---

### 7. ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation

**Authors:** Tran Dinh Tien, Zhiqiang Shen

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16996v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16996v1)

**Summary:** Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution decoding is typically run over the entire dataset vocabulary, whereas each image contains only a small active subset of classes. We introduce ActiveSAM, a training-free, zero-shot inference framework that turns SAM 3 into an active-vocabulary segmenter. ActiveSAM first canonicalizes and expan...

---

### 8. When in Doubt, Plan It Out: Committed Small Language Model Deliberation for Reactive Reinforcement Learning

**Authors:** Nathan Gavenski, Juarez Monteiro, Francisco Galuppo, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16995v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16995v1)

**Summary:** Reinforcement Learning (RL) policies often degrade in unfamiliar environments because they lack explicit deliberation. We propose Plan, Align, Commit, Think (PACT), a hybrid architecture that combines a fast, reactive RL policy with a slow, deliberative Small Language Model (SLM) planner. PACT invokes the SLM asynchronously to generate and validate candidate action plans. Once a plan is verified through simulation as safe, feasible, and complete, it is executed directly, bypassing the RL policy ...

---

### 9. Stable Menus of Public Goods: AI-Enabled Progress

**Authors:** Sara Fish

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16989v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16989v1)

**Summary:** Using an open problem from the EC 2025 paper "Stable Menus of Public Goods" as a testbed, we conduct experiments to understand the effectiveness of different AI-for-EconCS research workflows. Specifically, we study three questions: Does providing human intuition in the prompt help? Does automated multi-turn interaction help? And, does an LLM outperform a first-year PhD student? Regarding the first two questions, we provide evidence for the following workflow suggestions: (1) prompting with human...

---

### 10. Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification

**Authors:** Truong Thanh Hung Nguyen, Khanh Van Quynh Nguyen, Hoang-Loc Cao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16987v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16987v1)

**Summary:** Accurate Harmonized Tariff Schedule (HTS) code classification is essential for customs clearance, duty assessment, trade statistics, and regulatory compliance in maritime logistics. However, exact HTS classification remains challenging because product descriptions are often short, incomplete, or ambiguous, while correct classification depends on hierarchical tariff structures, legal notes, and jurisdiction-specific rules. This paper proposes an agentic large language model (LLM) framework for Ca...

---

### 11. The embrace of open science: An analysis of a decade of AI research and 56 800 conference papers

**Authors:** Kevin L Coakley, Thijs Snelleman, Holger Hoos, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16974v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16974v1)

**Summary:** The reproducibility crisis has directed the AI research community toward improving documentation practices. Several studies have identified methodological issues, and in response, the most impactful venues in the field have introduced reproducibility checklists. We seek to understand whether documentation practices have changed over time by assessing all published papers at five leading AI conferences over the past decade. Seven reproducibility variables were identified, quality-assured and used...

---

### 12. How Much Do Reviews Really Contribute? A Study on Text-Enriched Matrix Factorization for Recommendations

**Authors:** Eduardo Ferreira da Silva, Mayki dos Santos Oliveira, Joel Machado Pires Denis Dantas Boaventura, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16973v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16973v1)

**Summary:** Incorporating textual reviews into a Recommender System has become a prominent strategy for enriching collaborative signals with semantic information. However, the actual contribution of review-derived representations remains an open question, particularly when strong collaborative baselines are employed. In this work, we systematically investigate the impact of textual information on Matrix Factorization by introducing and comparing three enrichment strategies over a common collaborative backbo...

---

### 13. Probing Low Frame Rate Degradation in Neural Audio Codecs

**Authors:** Alex Gichamba, Moise Busogi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16969v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16969v1)

**Summary:** Low frame rates in neural audio codecs are attractive for autoregressive speech synthesis, where the generation cost scales linearly with the sequence length. Recent work has demonstrated that codecs can operate at 12.5 Hz and below, but the mechanisms underlying low frame rate degradation remain insufficiently understood. We investigate these mechanisms through a controlled frame rate ablation. We reproduce a quality cliff at 6.25 Hz reported in previous works and evaluate candidate explanation...

---

### 14. Phantoms and Disclosures: a Causal Framework for Auditing Synthetic Data

**Authors:** Kareem Amin, Rudrajit Das, Alessandro Epasto, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16952v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16952v1)

**Summary:** The rapid adoption of generative AI and Large Language Models (LLMs) has spurred interest in synthetic data as a privacy-preserving alternative to sensitive real-world datasets. However, generating high-utility synthetic data often carries the risk of memorizing and regurgitating private information from the training corpus. In this work, we present a customizable empirical auditing framework designed to detect and explain such data disclosures. Our framework introduces a mechanism to distinguis...

---

### 15. A Causal Model of Theory of Mind in Conflict for Artificial Intelligence

**Authors:** Nikolos Gurney

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16944v1)

**Summary:** Theory of mind (ToM), the capacity to ascribe mental states to others and use those ascriptions for prediction and inference, is widely assumed to be essential for effective human-machine integration. Existing AI-ToM models address \emph{how} to mentalize, but leave the question of when largely unaddressed. The central question is: under what situational and agent-level conditions is ToM engagement causally warranted in conflict? This paper presents a structural causal model formalized as a dire...

---

### 16. Scalable Circuit Learning for Interpreting Large Language Models

**Authors:** Naiyu Yin, Dennis Wei, Tian Gao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16939v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16939v1)

**Summary:** A prominent research direction in mechanistic interpretability is learning sparse circuits over LLM components to reveal how they jointly produce model behavior. However, raw neurons are polysemantic, making learned circuits hard to interpret. Sparse autoencoder (SAE) features alleviate this, but their high dimensionality makes existing intervention-based circuit learning methods computationally prohibitive. We propose CircuitLasso, a scalable circuit-learning approach based on sparse linear reg...

---

### 17. CrossMaps: Confidence-Aware Open-Vocabulary Semantic Mapping for Rover Navigation

**Authors:** Jan-Niklas Klein, Sona Ghahremani, Christian Medeiros Adriano, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16935v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16935v1)

**Summary:** Rovers rely on perception to maintain spatial maps that encode both objects and sensor quality (e.g., range reliability, lighting artifacts, data density), guiding data fusion, embedding updates, and navigation under partial observability. To study these coupled perception-navigation processes, we present CrossMaps, a real-time confidence-aware open-vocabulary semantic mapping pipeline that constructs language-queryable maps from RGB-D data. Building on VLMaps-style approaches, CrossMaps integra...

---

### 18. A Unified Causal-Origin Taxonomy of Distributional Shifts in Reinforcement Learning

**Authors:** Ardianto Wibowo, Paulo E Santos, Amer Baghdadi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16933v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16933v1)

**Summary:** Reinforcement learning (RL) systems often degrade when operating conditions differ from those previously encountered, reflecting distributional shifts in the underlying data-generating process. Such shifts may occur between training and evaluation, as in In-Distribution (ID) and Out-of-Distribution (OOD) generalization, or within non-stationary settings where environment dynamics evolve over time. However, the formal relationship between these views remains unclear, and existing work mainly focu...

---

### 19. RAID: Semantic Graph Diffusion for True Cold-Start and Cross-Lingual Forecasting

**Authors:** Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R., et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16925v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16925v1)

**Summary:** Time-series foundation models show strong transfer performance when given a non-empty history window. However, true cold-start scenarios, where a new item has no prior observations, violate this assumption. We propose RAID (Retrieval-Augmented Iterative Diffusion) a framework, which replaces history-based correlation learning with metadata-driven semantic retrieval and graph-conditioned diffusion. RAID maps textual metadata into a shared semantic space using a frozen multilingual embedding model...

---

### 20. MA-SBI: Misspecification-Aware Simulation-Based Inference via Side-Channel Guidance

**Authors:** Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R., et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16923v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16923v1)

**Summary:** Simulation-based inference (SBI) of latent parameters is often hindered by simulator misspecification, the mismatch between simulated and real-world observations caused by inherent modeling simplifications. RoPE, the recent state-of-the-art for robust SBI, addresses this through optimal transport between learned representations of real and simulated observations, but requires ground-truth parameter calibration pairs that are typically unavailable in the very settings where SBI is needed. What pr...

---

### 21. Demystifying Variance in Circuit Discovery of LLMs

**Authors:** Frank Zhengqing Wu, Francesco Tonin, Volkan Cevher

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16920v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16920v1)

**Summary:** Circuit discovery is a key technique in mechanistic interpretability to pinpoint the model components that are crucial for performing a given task. Although the current state-of-the-art method (EAP-IG) performs well on the metric of (un)faithfulness, it suffers from substantial variability. This includes resampling variance, where the circuit changes when we probe with a new batch of data from the same distribution; rephrasing variance, where the discovered circuit shifts when the prompts are re...

---

### 22. Greed Is Learned: Visible Incentives as Reward-Hacking Triggers

**Authors:** Tong Che, Rui Wu

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16914v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16914v1)

**Summary:** Deployed agents increasingly act with their reward proxy in view, such as a balance, score, or KPI dashboard. We show that reinforcement learning can make a policy \emph{addicted} to such a visible self-benefit channel. It chases the displayed payoff across held-out domains, sacrifices the true task to do so, and follows the channel wherever we rewrite it, while policies that never saw the channel stay honest. We call this \emph{reward-channel addiction} and study it in \emph{MoneyWorld}, a synt...

---

### 23. IMPACTeen: Intentions, Manipulation, Persuasion, Annotations, and Consequences in Teen Communication Dataset

**Authors:** Aleksander Szczęsny, Wiktoria Mieleszczenko-Kowszewicz, Maciej Markiewicz, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16910v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16910v1)

**Summary:** IMPACTeen is a dataset of textual social influence scenarios spanning interpersonal, media-based, and digital settings in an adolescent context. It contains 1,021 texts, 5,100 individual annotation records, and gold labels for social influence techniques, with each text annotated from five distinct perspectives: teenagers, parents, psychologists, communication experts, and teachers. The resource was constructed through constrained LLM generation, followed by a two-step human editing and validati...

---

### 24. Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models

**Authors:** Dongbin Na, Chanwoo Kim, Soonbin Rho, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16902v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16902v1)

**Summary:** This work addresses spatial question answering for service robots traversing long egocentric routes. Given a query such as "where can I find a dry cleaner on the way back home?", the system returns a metric coordinate that downstream navigation components can act on. Prior Spatial Question Answering approaches leverage retrieval-augmented agents built on closed-source models such as GPT-4o for path exploration. However, robots operating in the real world often cannot reliably depend on online cl...

---

### 25. Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization

**Authors:** Dongbin Na, Chanwoo Kim, Giyun Choi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16898v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16898v1)

**Summary:** Detecting unanswerable user queries remains essential for the reliable deployment of real-world embodied agents. However, modern vision-language models (VLMs) often generate overly confident answers even when the available visual memory cannot support the query. Such overconfidence poses various task-dependent risks. The agent may provide misleading information to the user in Embodied Question Answering and select an arbitrary coordinate and physically guide the user there in spatial reasoning f...

---

### 26. Symbolic Informalization: Fluent, Productive, Multilingual

**Authors:** Aarne Ranta

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16893v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16893v1)

**Summary:** Symbolic informalization enables a reliable conversion of formal mathematics to natural language. It has the potential to make machine-checked content human-readable without loss of precision. In a traditional proof system usage, symbolic informalization generalizes the limited mechanisms of syntactic sugar into the ordinary language of mathematics. In a setting where proofs are constructed by artificial intelligence and autoformalization, symbolic informalization can explain what precisely has ...

---

### 27. Beyond Weights and Gradients: A Taxonomy of Federated Learning Messages

**Authors:** Alvaro Javier Vargas Guerrero, Xinguang Wang, Quang Manh Doan, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16891v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16891v1)

**Summary:** Federated Learning is rapidly evolving beyond the exchange of traditional model weights and gradients, yet existing definitions fail to capture the full scope of modern payloads like synthetic data and federated analytics. This paper addresses the gap by proposing a formal mathematical definition of a federated message that accounts for both utility and privacy. We introduce a taxonomy that organizes these exchanges into three categories: model structures, statistical summaries, and data-conditi...

---

### 28. Compositional Reasoning Depth Predicts Clinical AI Failure: Empirical Evidence Consistent with Transformer Compositionality Limits in Electronic Health Record Question Answering

**Authors:** Sanjay Basu

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16890v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16890v1)

**Summary:** Aggregate accuracy benchmarks conceal a systematic structure in how large language models fail at electronic health record (EHR) question answering: questions requiring more inferential steps produce disproportionately more errors. Motivated by theoretical results on transformer compositionality limits, we introduce a pre-specified hop-count taxonomy -- the number of distinct reasoning steps required to answer a clinical question from an EHR -- as a principled predictor of model failure. We anno...

---

### 29. Upper Bounds on the Generalization Error of Deep Learning Models via Local Robustness and Stability

**Authors:** Abdul-Rauf Nuhu, Parham M. Kebria, Vahid Hemmati, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16883v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16883v1)

**Summary:** Generalization is a critical property of data-driven models, particularly deep learning models deployed in safety-critical applications. Robustness-based generalization bounds have gained attention as a principled way to link robustness properties to generalization performance, often in a data-dependent manner. However, most existing bounds suffer from vacuousness in practical settings, yielding loose upper bounds that greatly exceed the actual error rates and limiting their usefulness for real-...

---

### 30. Federated Medical Image Segmentation under Real-World Label Noise: A Benchmark Suite for Noisy Label Learning Method Selection

**Authors:** Markus Bujotzek, Dimitrios Bounias, Stefan Denner, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16868v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16868v1)

**Summary:** While federated learning (FL) enables collaborative medical image segmentation without centralizing sensitive data, real-world deployment is frequently complicated by cross-site label imperfections such as contour disagreement, missing or additional structures, and confused labels. Federated noisy label learning (FNLL) aims to mitigate these effects, yet remains underused in practice as existing evidence is largely based on synthetic noise, simplified settings, and limited real-world noisy evalu...

---

### 31. Follow the Latent Roadmap: Navigating Revocable Decoding for Diffusion LLMs with Anchor Tokens

**Authors:** Yizhen Yao, Qinglin Zhu, Runcong Zhao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16847v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16847v1)

**Summary:** Diffusion Large Language Models (dLLMs) offer a promising avenue for parallel generation but face a trade-off between decoding speed and quality. While revocable decoding strategies attempt to mitigate errors by verifying and remasking tokens, they typically operate within a mixed-quality context. This leads to two critical failures: \textit{Error Propagation}, where new tokens absorb toxic information from erroneous context, and \textit{Local Error Reinforcement}, where errors mutually reinforc...

---

### 32. Deep Q-Learning on Hölder Spaces

**Authors:** Qian Qi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16846v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16846v1)

**Summary:** We study the operator-theoretic core of Q-learning in continuous-time stochastic control with continuous states and actions. In value-based reinforcement learning, each Q-learning or DQN update is built from a Bellman optimality target; our analysis isolates this target in a diffusion setting and studies its regularity and approximation complexity. Under uniform ellipticity and Hölder-regular coefficients, we show that a Bellman update maps bounded inputs into an anisotropic regularity class, sm...

---

### 33. Robust Dual-Signal Fusion: Hybrid Neuro-Symbolic Gating with Compressed Chain-of-Thought Refinement for Irony Detection in Social Media Texts

**Authors:** Ankit Bhattacharjee, Krityapriya Bhaumik

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16845v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16845v1)

**Summary:** Large Language Models (LLMs) natively default to literal semantic interpretations, making zero-shot irony detection a persistent challenge. We introduce the Robust Dual-Signal (RDS) Fusion framework, a hybrid neuro-symbolic architecture that compresses Chain-of-Thought (CoT) reasoning trajectories without Supervised Fine-Tuning (SFT). Evaluated on a strictly held-out TweetEval test set (N=734), RDS achieves 78.1% accuracy and a Macro F1 of 0.777, matching the absolute performance ceiling of the ...

---

### 34. Beyond Models: Reflections on Engineering AI-enabled Systems in a Project-Based Course

**Authors:** Amir Mashmool, Kishan Ravindra Sawant, Mojtaba Shahin, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16842v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16842v1)

**Summary:** Teaching Software Engineering for AI-enabled systems entails addressing the integration of AI components within full-scale software architectures under realistic constraints. While machine learning courses emphasize model development, students often lack experience in architectural design, deployment, and monitoring of AI-enabled systems. Empirical evaluations of such system-oriented AI courses remain limited. This paper reflects on the design and implementation of a project-based master's-level...

---

### 35. Robust Spoofed Speech Detection via Temporal Pyramid Modeling

**Authors:** Mahtab Masoudi Nezhad, Nima Karimian

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16837v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16837v1)

**Summary:** Spoofed speech detection is increasingly challenged by realistic synthesis, voice conversion, and replay attacks, with cross-dataset generalization remaining a major limitation. This work we propose a Temporal Pyramid Adapter that utilize parallel temporal convolutions with varying receptive fields to capture multi-scale spoofing cues, ranging from local artifacts to global prosodic irregularities. We also integrated self-supervised XLS-R representations combined with front-end adapters, includi...

---

### 36. ATOM-Bench: A Real-World Benchmark for Atomic Skills and Compositional Generalization in Manipulation Policies

**Authors:** Zenan Wu, Bingqing Wei, Lu Liu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16826v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16826v1)

**Summary:** Generalist manipulation policies are increasingly presented as foundation models for robotic control, but their real-world generalization remains difficult to diagnose. A policy may succeed on demonstrated tasks while still failing to execute fine-grained atomic skills or recombine learned skills in new task structures. We introduce \textbf{ATOM-Bench}, a real-world benchmark for evaluating both atomic skills and compositional generalization in manipulation policies. ATOM-Bench factorizes tablet...

---

### 37. Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models

**Authors:** Martin Jaggi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16825v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16825v1)

**Summary:** Mixture-of-Experts (MoE) architectures efficiently scale Large Language Models (LLMs) by activating only a small fraction of their experts per token, yet the full parameter count - dominated by the expert parameters - must be held in training and inference memory. To address this, we introduce Expert Tying, an architectural modification that shares expert parameters across consecutive transformer layers while preserving independent, layer-wise routing and attention.   We evaluate this approach a...

---

### 38. A Perception vs. Distortion Perspective on Score-Based Generative Channel Estimation

**Authors:** Marco Skocaj, Lukas Eller, Mate Boban

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16815v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16815v1)

**Summary:** Driven by their remarkable success in computer vision and inverse problem solving, score-based models are increasingly applied to wireless communications, where they show promise across a range of physical-layer tasks. However, despite this growing interest, the current literature often lacks a rigorous analysis of when score-matching offers a tangible advantage over traditional discriminative learning. This paper aims to address this gap through the use-case of channel estimation, a fundamental...

---

### 39. GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents

**Authors:** Rahul Suresh Babu, Rohit Shukla

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16813v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16813v1)

**Summary:** Tool-augmented LLM agents rely on runtime filtering to decide which tools should be visible at each step. Causal Minimal Tool Filtering (CMTF) reduces tool-choice confusion by exposing only the next causally necessary tool frontier, but it assumes that the user request has already been mapped to a symbolic goal state. In practice, requests such as "handle my appointment" or "take care of this email" may correspond to multiple possible goals. This creates wrong-goal execution, where an agent foll...

---

### 40. Scaling LLM Reasoning from Minimal Labels: A Semi-Supervised Framework with a Lightweight Verifier

**Authors:** Keizo Kato, Chenhui Chu, Yugo Murawaki, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16811v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16811v1)

**Summary:** For the development of Large language models (LLMs), recent approaches to generating pseudo intermediate reasoning have shown remarkable progress. But they typically rely on large numbers of correctly annotated answers to assess reasoning quality. This paper presents a semi-supervised framework that scales reasoning learning from minimal supervision, turning reasoning verification itself into a data creation mechanism. We train a lightweight reasoning-correctness classifier on only a few labeled...

---

### 41. Adaptive and Explicit safe: Triggering Latent Safety Awareness in Large Reasoning Models

**Authors:** Ke Miao, Jiaxin Li, Hongliang Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16808v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16808v1)

**Summary:** While Large Reasoning Models (LRMs) excel at complex tasks, they remain highly vulnerable to sophisticated jailbreaks and direct harmful queries. To address this vulnerability, prior works depend heavily on external manual data annotation for safety alignment. However, we observe that LRMs can inherently identify safety risks when being re-presented with original queries alongside their own reasoning trajectories -- a capability we term Latent Safety Awareness. To leverage this safety awareness,...

---

### 42. LabOSBench: Benchmarking Computer Use Agents for Scientific Instrument Control

**Authors:** Anqi Zou, Han Deng, Chengyu Zhang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16802v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16802v1)

**Summary:** Current computer-use benchmarks primarily focus on software operation tasks in virtualized systems, whereas scientific instrumentation scenarios require coordinated control over complex interfaces, and feedback-driven parameter adjustment. However, directly evaluating agents on physical high-precision instruments is impractical due to high cost, safety risks, limited accessibility, and difficulty in ensuring reproducible evaluation. This motivates the need for a simulated yet realistic testbed t...

---

### 43. Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment

**Authors:** Zijie Meng

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16799v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16799v1)

**Summary:** Existing vision-language model (VLM)-based AI-generated image quality assessment (AIGIQA) methods suffer from a fundamental semantic-distortion dimensional conflict: monolithic representations optimized for semantic discrimination inherently entangle compositional understanding with low-level perceptual sensitivity, rendering them blind to fine-grained quality degradations. We introduce MST-CLIPIQA, a multi-scale two-stream framework that achieves hierarchical vision-language alignment through e...

---

### 44. Decision-Weighted Flow Matching for Contextual Stochastic Optimization

**Authors:** Jize Xie, Haomiao Wu, Qiang Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16790v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16790v1)

**Summary:** Conditional generative models are increasingly used as scenario generators for stochastic optimization, but standard training objectives emphasize uniform distributional fit rather than the downstream decisions induced by generated scenarios. This creates an objective mismatch: errors in statistically common regions may have little effect on decision regret, whereas errors in decision-sensitive regions can substantially change the optimal action. We propose Decision-Weighted Flow Matching (DW-FM...

---

### 45. Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations

**Authors:** Zhiqiang Zhou, Junliang Dai, Xu ling

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16783v1)

**Summary:** Multimodal large language models (MLLMs) excel at visual reasoning but rely on text-based chain-of-thought (CoT), lacking interpretable visual intermediates. Existing methods use opaque tokens or external tools, missing key properties. We propose Gen-VCoT, a framework using expert vision models to generate RGB images as reasoning intermediates. It has three stages: visual grounding (SAM segmentation), geometric reasoning (Marigold depth maps), and semantic reasoning (Qwen2-VL integration). An ad...

---

### 46. OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models

**Authors:** Tianyi Lin, Chuanyu Sun, Jingyi Zhang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16774v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16774v1)

**Summary:** Equipping Large Language Model (LLM) agents with effective skills is crucial for solving complex tasks in real-world systems like OpenClaw. In this work, we aim to develop a framework that automatically constructs such reusable skills to enhance LLMs in tool use, multi-step reasoning, and dynamic environment interaction. To this end, we propose Collective Skill Tree Search (CSTS), a novel tree-search-based skill construction framework that constructs structured, diverse and generalizable tree of...

---

### 47. Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents

**Authors:** Tianyi Zhang, Zhonghao Qi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16769v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16769v1)

**Summary:** Agent skills are commonly distributed as SKILL.md files: human-readable procedural documents that describe workflows, tools, resources, and domain conventions. While convenient for inspection and reuse, this design requires the same reusable procedure to be repeatedly injected into the runtime context. We propose Skill-to-LoRA(S2L), a behavior-centric skill representation that replaces runtime skill text with skill-specific LoRA adapters. Rather than compressing the skill document itself, S2L mo...

---

### 48. P3B3: A Multi-Turn Conversational Benchmark for Measuring European and Brazilian Portuguese Variety Bias in LLMs

**Authors:** Rafael Ferreira, Inês Vieira, Inês Calvo, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16753v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16753v1)

**Summary:** As Large Language Models (LLMs) become embedded in everyday communication, capturing regional linguistic variation is essential for reliable and equitable language use. In Portuguese, European (pt-PT) and Brazilian (pt-BR) varieties remain unevenly represented, with pt-BR dominating in data quantity, while LLM preference for Portuguese variants remains underexplored. To address this gap, we introduce P3B3, an expert-curated language variety agnostic benchmark of conversational prompts, along wit...

---

### 49. Automated jailbreak attack targeting multiple defense strategies

**Authors:** Qi Wang, Chengcheng Wan, Weijia He, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16751v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16751v1)

**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks. However, their safety remains a critical concern due to their susceptibility to adversarial prompt-based attacks. In this paper, we present UNIATTACK, an adversarial testing framework designed from a defense-oriented perspective to systematically construct effective black-box attack prompts. Unlike prior approaches that rely on static templates or iterative model-specific tuning, UNIATTACK extrac...

---

### 50. Revealing Artifacts via Noise Amplification: A Novel Perspective for AI-Generated Video Detection

**Authors:** Renxi Cheng, Jie Gui, Hongsong Wang

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16742v1)

**Summary:** With the rapid advancement of video generation models, distinguishing between AI-generated and authentic videos has emerged as a challenging endeavor. The majority of existing research endeavors concentrate on the development of detectors for identifying samples generated by generative adversarial networks. Nevertheless, the detection of AI-generated videos, particularly those produced by text-to-video models, still remains an uncharted territory. Although state-of-the-art text-to-video models c...

---

## cs.CL

**50 papers**

### 1. The Value Axis: Language Models Encode Whether They're on the Right Track

**Authors:** Nick Jiang, Isaac Kauvar, Jack Lindsey

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17056v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17056v1)

**Summary:** We investigate whether language models internally track the value of their current trajectory, defined as the likelihood that their ongoing strategy will achieve their goals. Using synthetic, in-context reinforcement learning data, we construct a "value" axis for Qwen3-8B. We find that activations along this axis distinguish between high vs. low verbalized confidence, rollouts without and with backtracking, and correct vs. corrupted code. Steering towards high value causally suppresses self-corr...

---

### 2. Context-Aware RL for Agentic and Multimodal LLMs

**Authors:** Peiyang Xu, Bangzheng Li, Sijia Liu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17053v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17053v1)

**Summary:** Large language models (LLMs) often fail when answering requires identifying a small but decisive piece of evidence within a long or complex context, such as a single line in a tool trace or a subtle detail in an image. We propose ContextRL, a context-aware reinforcement learning (RL) method that improves long-horizon reasoning and multimodal performance through an \emph{indirect} auxiliary objective. Instead of supervising only the final answer, ContextRL presents the model with a query, an answ...

---

### 3. Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio

**Authors:** Anzhe Xie, Weihang Su, Yujia Zhou, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17041v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17041v1)

**Summary:** Meta-analysis is a demanding form of evidence synthesis that combines literature retrieval, PI/ECO-guided study selection, and statistical aggregation. Its structured, verifiable workflow makes it an ideal substrate for evaluating systematic scientific reasoning, yet existing benchmarks lack ground truth across the full retrieval-screening-synthesis pipeline. We introduce MetaSyn, a dataset of 442 expert-curated meta-analyses from Nature Portfolio journals. Each entry pairs a research question w...

---

### 4. KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing

**Authors:** Mufei Li, Shikun Liu, Dongqi Fu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17034v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17034v1)

**Summary:** Post-hoc context erasing over the KV cache is challenging because a local edit has a global consequence: once a span has been processed, its influence propagates into the cached states of all subsequent tokens. This issue arises naturally in long-context LLM applications, where stale retrieved facts, incorrect tool observations, retracted user preferences, or harmful prompt injections may be identified only after prefill. Exact erasing must then recompute all tokens after the deleted span, makin...

---

### 5. DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents

**Authors:** Minghang Zhu, Chuyang Wei, Junhao Xu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17029v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17029v1)

**Summary:** Deep research agents synthesize long-form reports by searching and reasoning over retrieved evidence. Reinforcement learning with rubric-based rewards improves these agents by optimizing them against checkable criteria that translate report quality into reward signals, but its efficiency depends on whether those criteria reliably capture the task scope and evidence needs. Most existing studies ask an LLM to generate rubrics for a given query, but when the model fails to infer the underlying info...

---

### 6. TokenPilot: Cache-Efficient Context Management for LLM Agents

**Authors:** Buqiang Xu, Zirui Xue, Dianmou Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17016v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17016v1)

**Summary:** As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, ...

---

### 7. Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models

**Authors:** Mehmet Iscan

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16999v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16999v1)

**Summary:** Frozen small code models (<=1.5B parameters, run locally without fine-tuning) suit offline and privacy-constrained use, but often emit plausible-but-wrong programs. A natural remedy is a post-hoc operator that selects, verifies, repairs, or re-processes the model's samples without retraining; in principled form it is Popperian: attack each candidate with a severe test, keep what survives. We measure whether such operators help. Under one deterministic execution oracle and a leakage-free, matched...

---

### 8. Exploring Extrinsic and Intrinsic Properties for Effective Reasoning with Code Interpreter

**Authors:** Patomporn Payoungkhamdee, Napat Laosaengpha, Jenta Wonglertsakul, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16934v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16934v1)

**Summary:** Reasoning with a Code Interpreter (CI) has emerged as an effective paradigm for enhancing the reasoning capabilities of large language models (LLMs) through executable computation and iterative verification. Despite its growing adoption, the behavioral properties underlying effective code reasoning remain largely underexplored. In this work, we investigate code reasoning from two distinct perspectives inspired by prior studies of natural language reasoning: extrinsic properties, represented by c...

---

### 9. IMPACTeen: Intentions, Manipulation, Persuasion, Annotations, and Consequences in Teen Communication Dataset

**Authors:** Aleksander Szczęsny, Wiktoria Mieleszczenko-Kowszewicz, Maciej Markiewicz, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16910v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16910v1)

**Summary:** IMPACTeen is a dataset of textual social influence scenarios spanning interpersonal, media-based, and digital settings in an adolescent context. It contains 1,021 texts, 5,100 individual annotation records, and gold labels for social influence techniques, with each text annotated from five distinct perspectives: teenagers, parents, psychologists, communication experts, and teachers. The resource was constructed through constrained LLM generation, followed by a two-step human editing and validati...

---

### 10. LESS Is More: Mutual-Stability Sampling for Diffusion Language Models

**Authors:** Amr Mohamed, Guokan Shang, Michalis Vazirgiannis

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16908v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16908v1)

**Summary:** Diffusion large language models (dLLMs) offer a promising alternative to autoregressive decoding by iteratively refining masked sequences, enabling parallel token updates and bidirectional conditioning. Their practical efficiency, however, is limited by sampling procedures that execute a fixed number of reverse denoising steps selected before decoding, spending computation on already-stable positions and sometimes committing unstable ones too early. We present \textsc{LESS}, a training-free, mod...

---

### 11. Speaking the Language of Science: Toward a General-Purpose Generative Foundation Model for the Natural Sciences

**Authors:** Mingyang Li, Yurou Liu, Jieping Ye, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16905v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16905v1)

**Summary:** In this report, we present LOGOS (Language Of Generative Objects in Science), a scientific generative language model that unifies heterogeneous tasks across the natural sciences within a single autoregressive framework based on a shared scientific grammar. It encodes diverse scientific objects and their spatial interactions as token sequences over a common vocabulary. By representing spatial contact and constraint patterns as discrete tokens, the model captures complex structural interactions in...

---

### 12. Contrastive-Difference CKA Reveals Concept-Specific Structural Alignment Across Language Model Architectures

**Authors:** Xueping Gao

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16897v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16897v1)

**Summary:** Do different LLM architectures encode high-level concepts in structurally compatible ways? We systematically characterize a geometric-functional universality dissociation: across multiple concept domains and architectural families, moderate geometric convergence coexists with near-perfect functional transfer. Using contrastive-difference CKA (CKA_Delta), a training-free diagnostic that computes kernel alignment on per-sample contrastive differences, we isolate concept-specific convergence from g...

---

### 13. Symbolic Informalization: Fluent, Productive, Multilingual

**Authors:** Aarne Ranta

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16893v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16893v1)

**Summary:** Symbolic informalization enables a reliable conversion of formal mathematics to natural language. It has the potential to make machine-checked content human-readable without loss of precision. In a traditional proof system usage, symbolic informalization generalizes the limited mechanisms of syntactic sugar into the ordinary language of mathematics. In a setting where proofs are constructed by artificial intelligence and autoformalization, symbolic informalization can explain what precisely has ...

---

### 14. Compositional Reasoning Depth Predicts Clinical AI Failure: Empirical Evidence Consistent with Transformer Compositionality Limits in Electronic Health Record Question Answering

**Authors:** Sanjay Basu

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16890v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16890v1)

**Summary:** Aggregate accuracy benchmarks conceal a systematic structure in how large language models fail at electronic health record (EHR) question answering: questions requiring more inferential steps produce disproportionately more errors. Motivated by theoretical results on transformer compositionality limits, we introduce a pre-specified hop-count taxonomy -- the number of distinct reasoning steps required to answer a clinical question from an EHR -- as a principled predictor of model failure. We anno...

---

### 15. Understanding Scam Trends and Rail Paths from Reddit Self-Disclosure Narratives

**Authors:** Yangjun Zhang, Mirko Bottarelli, Mark Hooper, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16874v1)

**Summary:** Online scam behavior is inherently multi-stage, and the lifecycle includes temporally ordered rails and events rather than isolated signals. Existing works analyze characteristics of scam types and rails, but they do not track scam trends across years. Moreover, the work on the relations between rails is hampered due to the lack of open-source datasets with annotations and coverage of different scam types. To address these gaps, we build a dataset to analyze the yearly trend of scam characterist...

---

### 16. Revisiting the Systematicity in Negation in the Era of In-Context Learning

**Authors:** Hitomi Yanaka, Taisei Yamamoto

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16867v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16867v1)

**Summary:** Understanding the meaning of negated sentences remains one of the challenges for language models, even in the era of large language models (LLMs). We analyze systematicity regarding LLM understanding of negation from two perspectives: behavioral systematicity and representational systematicity. For behavioral systematicity, we confirm that through demonstrations and in-context learning, LLMs can recognize negation expressions and scope within sentences to some extent, but they fail to achieve pe...

---

### 17. Follow the Latent Roadmap: Navigating Revocable Decoding for Diffusion LLMs with Anchor Tokens

**Authors:** Yizhen Yao, Qinglin Zhu, Runcong Zhao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16847v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16847v1)

**Summary:** Diffusion Large Language Models (dLLMs) offer a promising avenue for parallel generation but face a trade-off between decoding speed and quality. While revocable decoding strategies attempt to mitigate errors by verifying and remasking tokens, they typically operate within a mixed-quality context. This leads to two critical failures: \textit{Error Propagation}, where new tokens absorb toxic information from erroneous context, and \textit{Local Error Reinforcement}, where errors mutually reinforc...

---

### 18. Robust Dual-Signal Fusion: Hybrid Neuro-Symbolic Gating with Compressed Chain-of-Thought Refinement for Irony Detection in Social Media Texts

**Authors:** Ankit Bhattacharjee, Krityapriya Bhaumik

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16845v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16845v1)

**Summary:** Large Language Models (LLMs) natively default to literal semantic interpretations, making zero-shot irony detection a persistent challenge. We introduce the Robust Dual-Signal (RDS) Fusion framework, a hybrid neuro-symbolic architecture that compresses Chain-of-Thought (CoT) reasoning trajectories without Supervised Fine-Tuning (SFT). Evaluated on a strictly held-out TweetEval test set (N=734), RDS achieves 78.1% accuracy and a Macro F1 of 0.777, matching the absolute performance ceiling of the ...

---

### 19. Data-Driven Decoding of Russell's Circumplex Model of Affect

**Authors:** Amdjed Belaref, Samir Sadok, Zineb Noumir, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16843v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16843v1)

**Summary:** Affective computing increasingly relies on deep learning to represent emotions, yet latent spaces often remain opaque, high-dimensional black boxes. This paper investigates whether Transformers' embeddings recover the geometric regularities of Russell's circumplex model. We unify two complementary experiments testing the hypothesis that, after training models on text and speech, their resulting latent spaces encode a topology consistent with valence-arousal and reproduce human-like neighborhood ...

---

### 20. Does Traversal Order Matter? A Systematic Study of Tree Traversal Methods in Transformer Grammars

**Authors:** Zongru Liu, Pengyu Ji, Pengcheng Wang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16836v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16836v1)

**Summary:** Transformer Grammars (TGs) enhance language modeling by incorporating syntactic tree structures. Despite the potentially significant impact on model performance of how syntactic trees are linearized in TGs, existing studies rely solely on Depth-First Traversal (DFT) for linearization. In this paper, we expand the traversal design space by exploring Breadth-First Traversal (BFT) and a novel hybrid traversal strategy, Production-Rule Traversal (PRT), which combines the structural lookahead of BFT ...

---

### 21. Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models

**Authors:** Martin Jaggi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16825v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16825v1)

**Summary:** Mixture-of-Experts (MoE) architectures efficiently scale Large Language Models (LLMs) by activating only a small fraction of their experts per token, yet the full parameter count - dominated by the expert parameters - must be held in training and inference memory. To address this, we introduce Expert Tying, an architectural modification that shares expert parameters across consecutive transformer layers while preserving independent, layer-wise routing and attention.   We evaluate this approach a...

---

### 22. How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation

**Authors:** Yimeng Chen, Zhe Ren, Firas Laakom, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16821v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16821v1)

**Summary:** Large language model (LLM)-based search agents synthesize open-web content into actionable recommendations on behalf of users, creating a risk that attacker-published pages are transformed into endorsed claims. We introduce SearchGEO, a controlled evaluation framework for measuring endorsement corruption in LLM-based web-search agents, combining a web-evidence manipulation pipeline, a five-mode attack taxonomy, and multiple output-level metrics. We evaluate 13 LLM backends on 308 cases each. Res...

---

### 23. Understanding the Behaviors of Environment-aware Information Retrieval

**Authors:** Ruifeng Yuan, Chaohao Yuan, David Dai, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16817v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16817v1)

**Summary:** Recent retrieval-augmented generation (RAG) approaches have demonstrated strong capability in handling complex queries, yet current research overlooks a critical challenge: different retrievers require fundamentally different query formulation strategies for optimal performance. In this work, we present the first systematic analysis of how LLMs can learn to adapt their query formulation strategies for different retrievers via reinforcement learning (RL). Our empirical study reveals that RL effec...

---

### 24. Scaling LLM Reasoning from Minimal Labels: A Semi-Supervised Framework with a Lightweight Verifier

**Authors:** Keizo Kato, Chenhui Chu, Yugo Murawaki, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16811v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16811v1)

**Summary:** For the development of Large language models (LLMs), recent approaches to generating pseudo intermediate reasoning have shown remarkable progress. But they typically rely on large numbers of correctly annotated answers to assess reasoning quality. This paper presents a semi-supervised framework that scales reasoning learning from minimal supervision, turning reasoning verification itself into a data creation mechanism. We train a lightweight reasoning-correctness classifier on only a few labeled...

---

### 25. Connecting Speech to Words through Images

**Authors:** Gabriel Pirlogeanu, Dan Oneata, Horia Cucu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16807v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16807v1)

**Summary:** How can we learn the mapping between written words and their spoken counterparts in the absence of explicit textual supervision? We present a visually grounded method for building a vocabulary of spoken words using only images and their spoken descriptions. First, image captioning systems are used to build a vocabulary of written words representing salient visual concepts in the images. For each word, we then find utterances whose image captions contain that word. Then we use an unsupervised wor...

---

### 26. LLM-based Visual Code Completion for Aerospace Geometric Design

**Authors:** Hau Kit Yong, Robert Marsh, Edmar A. Silva, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16806v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16806v1)

**Summary:** Recent advances in both Large Language Models (LLMs) and Vision Language Models (VLMs) have seen a step change in their ability to perform visual code completion, but the aerospace industry, which prioritizes safety and explainabilty over rapid LLM adoption, currently has no publicly announced LLM-based geometric design copilot systems in commercial use by aerospace Original Equipment Manufacturers (OEMs). This paper presents a LLM-based visual programming copilot application for aerospace engin...

---

### 27. The Art of Mixology: Mixup-based Obfuscation for Privacy-Preserving Split Learning in Large Language Models

**Authors:** Chen Chen, Xiang Gao, Xianshun Wang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16801v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16801v1)

**Summary:** Split learning provides a practical paradigm for resource-constrained users to train Large Language Models (LLMs) by offloading computation-intensive layers to a server while keeping raw data local. However, existing privacy-preserving split learning methods still face a difficult trade-off among utility, privacy, efficiency, and stability. Specifically, these methods often suffer from substantial utility degradation, remain vulnerable to advanced data reconstruction attacks, incur prohibitive c...

---

### 28. OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models

**Authors:** Tianyi Lin, Chuanyu Sun, Jingyi Zhang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16774v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16774v1)

**Summary:** Equipping Large Language Model (LLM) agents with effective skills is crucial for solving complex tasks in real-world systems like OpenClaw. In this work, we aim to develop a framework that automatically constructs such reusable skills to enhance LLMs in tool use, multi-step reasoning, and dynamic environment interaction. To this end, we propose Collective Skill Tree Search (CSTS), a novel tree-search-based skill construction framework that constructs structured, diverse and generalizable tree of...

---

### 29. P3B3: A Multi-Turn Conversational Benchmark for Measuring European and Brazilian Portuguese Variety Bias in LLMs

**Authors:** Rafael Ferreira, Inês Vieira, Inês Calvo, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16753v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16753v1)

**Summary:** As Large Language Models (LLMs) become embedded in everyday communication, capturing regional linguistic variation is essential for reliable and equitable language use. In Portuguese, European (pt-PT) and Brazilian (pt-BR) varieties remain unevenly represented, with pt-BR dominating in data quantity, while LLM preference for Portuguese variants remains underexplored. To address this gap, we introduce P3B3, an expert-curated language variety agnostic benchmark of conversational prompts, along wit...

---

### 30. MyPCBench: A Benchmark for Personally Intelligent Computer-Use Agents

**Authors:** Lawrence Keunho Jang, Andrew Keunwoo Jang, Jing Yu Koh, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16748v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16748v1)

**Summary:** Current benchmarks for computer-use agents evaluate models in impersonal environments. This leaves a gap between evaluation and deployment where personal assistants are expected to work across a user's whole digital life, including their context, historical data, and logged-in accounts. This gap is widest on web tasks, where live web evaluations cannot exercise sites that require logging in or personal information, the kind of site a real personal assistant has to drive. We introduce MyPCBench, ...

---

### 31. Misinformation Propagation in Benign Multi-Agent Systems

**Authors:** Jonas Becker, Jan Philip Wahle, Terry Ruas, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16710v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16710v1)

**Summary:** Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-...

---

### 32. Multi-Turn Reflective Masking Elicits Reasoning in Mask Diffusion Models

**Authors:** Yanming Zhang, Yihan Bian, Jingyuan Qi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16700v1)

**Summary:** While reasoning on autoregressive (AR) models is often performed by chain-of-thought reasoning and reflection, their refinement of previous outputs still relies on fully sequential generation, even when only local edits are needed. In contrast, the masking mechanism in Mask Diffusion Models (MDMs) naturally supports explicit local edits on previous outputs, allowing selective refinement without discarding previous answers and generating another from scratch. While this property more closely alig...

---

### 33. From Affect Prediction to Affect Forecasting: Evidence for Distinct Information Sources in Longitudinal Text

**Authors:** Sadia Noor, Seemab Latif, Raja Khurram Shahzad, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16687v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16687v1)

**Summary:** Modeling dimensional affect in longitudinal text requires distinguishing current affect estimation from future affective change forecasting. Existing approaches often treat each text as an independent observation and apply similar assumptions to both tasks, without testing whether they rely on different information sources. This paper investigates that distinction using longitudinal self-reported ecological essays and feeling-word entries. We propose the Trait--State Affective Prediction (TSAP) ...

---

### 34. Progressive Knowledge-Guided Large Language Model Framework for Bearing Fault Diagnosis

**Authors:** Jinghan Wang, Gaoliang Peng, Yanjun Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16684v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16684v1)

**Summary:** Vibration-based bearing fault diagnosis requires resolving three interrelated measurement challenges, including the trade-off between global statistical feature efficiency and local transient signal fidelity, insufficient traceability of measurement features to underlying fault physics, and ineffective multi-source measurement information fusion across diagnostic scales. This paper presents a progressive physics-guided multi-scale vibration signal processing framework that addresses all three ch...

---

### 35. Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents

**Authors:** Zewen Liu

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16682v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16682v1)

**Summary:** When AI agents use language models to evaluate their own outputs in a feedback loop, systematic biases emerge. We show that Evaluator Preference Collapse (EPC) is dramatically amplified in multimodal settings. Using GPT-4o to evaluate DeepSeek-chat across text and visual tasks, we find that a single strategy (step_by_step) absorbs 48.4% of all weight -- 3.2x the collapse observed in text-only self-evaluation -- while three visual-domain strategies receive only 9.1% combined weight. We then demon...

---

### 36. SCAR: Semantic Continuity-Aware Retrieval for Efficient Context Expansion in RAG

**Authors:** Nathanaël Langlois

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16661v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16661v1)

**Summary:** Fixed-length chunking in Retrieval-Augmented Generation (RAG) often leads to boundary fragmentation, where critical evidence is split across segments, degrading retrieval recall. While static windowing and parent retrieval improve recall, they introduce significant token overhead. We propose SCAR (Semantic Continuity-Aware Retrieval), an adaptive retrieval policy that selectively expands neighboring chunks by weighing query-neighbor relevance against a structural continuity penalty. SCAR uses a ...

---

### 37. FraudSMSWalker: Benchmarking Agentic Large Language Models for SMS-to-Webpage Fraud Detection

**Authors:** Y. H. Zhou, Z. M. Ma, Y. J. Zhou, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16659v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16659v1)

**Summary:** SMS fraud is increasingly cross-channel: a message directs the user to a webpage, and the final risk depends on how the SMS claim aligns with the page content and requested user action. However, existing evaluations either focus on message-only smishing classification or expose URL and domain cues that allow models to rely on reputation shortcuts. To address this gap, we introduce \textbf{FraudSMSWalker}, a controlled benchmark for URL-masked SMS-to-webpage fraud judgment. FraudSMSWalker contain...

---

### 38. Islamic Large Language Models: From Knowledge Acquisition to Trustworthy and Hallucination-Resistant AI

**Authors:** Mohammed Amine Mouhoub

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16629v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16629v1)

**Summary:** Large language models (LLMs) are increasingly used for knowledge-intensive question answering, including religious and legal questions. Islamic knowledge is a particularly demanding setting: answers are expected to be grounded in authoritative sources, citations must be exact, Arabic varieties differ substantially from the language of classical sources, and legitimate jurisprudential disagreement must be represented rather than collapsed into a single answer. This survey reviews the emerging fie...

---

### 39. Sycophancy as Material Failure under Pushback Loading: A Multi-Axis Characterization Across Three Loading Cases and up to Seventeen Material Charges

**Authors:** Ferdinand M. Schessl

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16617v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16617v1)

**Summary:** Sycophancy in LLMs is documented across 70+ papers, but expert agreement on construct boundaries remains low (ICC=.184; Ye et al., 2026). The construct fragments because behavioral classification depends on which surface form is privileged. We adopt a materials-science framing: conversation as test specimen under load, LLM-model as material charge, pushback as progressive load, stance-flip as material failure. We characterize this failure across three loading cases (debate n=1000; false-presuppo...

---

### 40. VeriGraph: Towards Verifiable Data-Analytic Agents

**Authors:** Jiajie Jin, Zhao Yang, Wenle Liao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16603v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16603v1)

**Summary:** LLM-based agents have demonstrated strong capabilities in data-intensive analytical tasks, yet their outputs are rarely verifiable: a reliance on linear text trajectories makes their reasoning difficult to audit. In particular, deterministic computations over raw data and semantic deductions over natural-language claims are often entangled in an unstructured stream, leaving numerical conclusions hard to reproduce and qualitative judgments hard to inspect. To address this, we propose VeriGraph, a...

---

### 41. How Far Can Machine Translation Quality Take You? Extrinsic Discourse Evaluation in Goal-Oriented Setups

**Authors:** Wafaa Mohammed, Kata Naszadi, Vlad Niculae

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16596v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16596v1)

**Summary:** Existing machine translation (MT) metrics and discourse-focused evaluations primarily assess translation quality intrinsically, without measuring the downstream consequences of translation errors. In this work, we focus on extrinsic discourse evaluation of machine translation under two distinct regimes: static and interactive. Under the static regime, we propose an entity counting task as a probe of referential consistency in discourse. We show that high intrinsic MT quality does not reliably pr...

---

### 42. SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents

**Authors:** Qiao Xiao, Haochen Shi, Yisen Gao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16591v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16591v1)

**Summary:** Large language model (LLM) agents increasingly rely on agent harnesses that manage context, tools, and multi-turn execution, making tools a central interface for acting in realistic digital environments. As harness-connected tool ecosystems expand to hundreds or thousands of APIs, services, and task-specific skills, exhaustive tool schema injection becomes costly and imposes a closed-world assumption that limits agents to a predefined static inventory. Retrieval-augmented tool selection offers a...

---

### 43. Uncertainty Is Not a Safety Net for Clinical VQA, but Can It Anticipate Model Failure?

**Authors:** Arnisa Fazla, Alberto Testoni, Ameen Abu-Hanna, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16583v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16583v1)

**Summary:** Safe deployment of clinical vision-language models (VLMs) requires reliable uncertainty estimation (UE): a signal indicating when predictions should be trusted or escalated to a clinician. We test whether current UE methods actually deliver this signal. Benchmarking 8 methods across 12 VLMs on clinical visual question-answering (VQA), we find that UE quality is not an intrinsic property of the UE method: it tracks model accuracy, degrading precisely where the model performance is weakest, and th...

---

### 44. Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning

**Authors:** Reef Menaged, Gili Lior, Shauli Ravfogel, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16576v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16576v1)

**Summary:** We propose agentic automata learning to evaluate the extent to which tool-calling LLM agents can uncover hidden environments through interaction. In our setup, an agent should uncover a hidden deterministic finite automaton (DFA) by interacting with an oracle through (1) membership queries ("Does this string belong to the target language?") and (2) equivalence queries ("Is this the target DFA?"). This yields a scalable testbed with controlled task complexity, measurable interaction efficiency, a...

---

### 45. Fast When, Careful Who: Dual-Process Multiparty Turn-Taking with Diffusion Augmentation

**Authors:** Rutherford A. Patamia, Ming Liu, Wei Luo, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16568v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16568v1)

**Summary:** Reliable turn-taking is essential for spoken dialogue systems. However, most existing methods are designed for two-speaker interaction and struggle with realistic multiparty audio containing overlap and rapid speaker changes. We study multiparty turn-taking on the VoxConverse dataset and propose an audio-only two-stage pipeline that separates when to trigger a turn boundary from whether the floor is actually transferring. A fast trigger scans the audio and proposes candidate end-of-turn times, w...

---

### 46. The BD-LSC Dataset: Facilitating the Benchmarking of Models for Lexical Semantic Change Detection in Slang and Standard Usage

**Authors:** Afnan Aloraini, Viktor Schlegel, Goran Nenadic, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16560v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16560v1)

**Summary:** Automatic semantic change detection aims to identify how word meanings shift over time, offering insights into both linguistic and societal change. Despite recent progress in computational lexical semantic change (LSC), existing benchmarks and methods struggle to capture bi-directional semantic change, particularly cases where words simultaneously gain and lose senses. This problem is especially challenging for words that have both slang and standard meanings. To address these gaps, we introduce...

---

### 47. Can LLM Coding Agents Reason About Time Series?

**Authors:** Filip Rechtorík, Ondřej Dušek, Zdeněk Kasner

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16545v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16545v1)

**Summary:** Large language models (LLMs) are increasingly being used for automated decision-making systems in finance, healthcare, or environmental monitoring. Time series data are ubiquitous in these fields, yet hard to process automatically. Can time series be analyzed by LLM agents? We examine three approaches: providing the agent with raw numerical data, using the LLM as a coding agent, or a combination of both. In the coding agent setup, the model iteratively queries the data using Python code. Using t...

---

### 48. DoubtProbe: Black-Box Jailbreak Defense via Structural Verification and Semantic Auditing

**Authors:** Xuanyu Yin, Yilin Jiang, Jun Zhou, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16527v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16527v1)

**Summary:** As large language models (LLMs) are increasingly deployed in user-facing systems, black-box jailbreak defense has become an important practical problem. Existing defenses often rely on known-attack coverage, prompt-level semantic judgment, or local runtime control, yet these paths can become unstable under evolving prompt packaging, expression rewriting, and structure manipulation. We observe that many black-box jailbreaks do not remove the harmful goal, but reorganize the information needed to ...

---

### 49. SkillWiki: A Living Knowledge Infrastructure for Agent Skills

**Authors:** Dingcheng Huang, Yuda Ding, Bingshuo Liu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16523v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16523v1)

**Summary:** While knowledge is managed through Wikipedia and software through GitHub, agent skills still lack an infrastructure for large-scale production, governance, and evolution. SkillWiki is a living knowledge infrastructure that supports the organization, grounding, and continuous evolution of agent skills by transforming heterogeneous knowledge into reusable skill assets linked to their originating evidence. Our demonstration presents the complete skill lifecycle, from knowledge ingestion and skill p...

---

### 50. daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization

**Authors:** Dayuan Fu, Mohan Jiang, Tongyu Wang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16497v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16497v1)

**Summary:** GPU kernel optimization represents a paradigm where functional correctness is assumed and execution efficiency is the objective. We present daVinci-kernel, a reinforcement learning framework that couples skill discovery with skill exploitation through a dynamically evolving skill library. daVinci-kernel jointly trains three agents sharing one LLM backbone: a Skill Selection Agent that retrieves relevant techniques via BM25 and LLM reranking, a Policy Agent that generates multi-turn CUDA/Triton k...

---

## cs.CV

**50 papers**

### 1. Context-Aware RL for Agentic and Multimodal LLMs

**Authors:** Peiyang Xu, Bangzheng Li, Sijia Liu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17053v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17053v1)

**Summary:** Large language models (LLMs) often fail when answering requires identifying a small but decisive piece of evidence within a long or complex context, such as a single line in a tool trace or a subtle detail in an image. We propose ContextRL, a context-aware reinforcement learning (RL) method that improves long-horizon reasoning and multimodal performance through an \emph{indirect} auxiliary objective. Instead of supervising only the final answer, ContextRL presents the model with a query, an answ...

---

### 2. BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering

**Authors:** Yi-Ruei Liu, Jie-Ying Lee, Zheng-Hui Huang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17049v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17049v1)

**Summary:** Inverse rendering of urban scenes from captured videos enables numerous applications, including content creation and autonomous driving simulation. Physically-based rendering methods follow and control lighting physics, but suffer from reconstruction and rendering artifacts. While generative models produce realistic videos, they offer limited consistency and controllability. We present BRDFusion, a unified framework that combines two complementary models for inverse and forward rendering. Specif...

---

### 3. Exact Posterior Score Estimation for Solving Linear Inverse Problems

**Authors:** Abbas Mammadov, Ozgur Kara, Kaan Oktay, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17048v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17048v1)

**Summary:** Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the posterior, but the score that the prior provides is the unconditional score, not the posterior score. Existing methods either steer a fixed pretrained denoiser with approximate measurement-matching corrections, or train a conditional restoration model that abandons the denoising structure of the prior. ...

---

### 4. Geometric Action Model for Robot Policy Learning

**Authors:** Jisang Han, Seonghu Jeon, Jaewoo Jung, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17046v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17046v1)

**Summary:** Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic or temporal priors from large-scale foundation models, but they still operate primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D geometry required for contact-rich manipulation. We propose the Geometric Action M...

---

### 5. R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies

**Authors:** Xiuwei Xu, Haowen Sun, Angyuan Ma, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17040v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17040v1)

**Summary:** Spatial generalization is critical for imitation-learned manipulation policies, but achieving it typically requires scaling demonstrations across diverse object poses, robot configurations, and camera viewpoints. Data augmentation from a few source demonstrations offers a practical alternative to costly real-world collection. Simulation-based augmentation can create controllable variation, but requires complex environment and object setup and may introduce a sim-to-real gap. Recent real-to-real ...

---

### 6. The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers

**Authors:** Alper Yıldırım

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17037v1)

**Summary:** Oppenheim and Lim (1981) showed that natural images stay recognizable when reconstructed from their Fourier phase alone, while the magnitude carries little of their identity. We ask whether trained image classifiers reproduce this asymmetry inside their hidden layers, and we test it causally: given two images, we transplant the phase of one onto the magnitude of the other at a chosen layer and record which image the prediction follows. In PRISM2D, GFNet, and ViT-B/16 the prediction follows the p...

---

### 7. Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation

**Authors:** Jie Zhang, Xiaoyue Chen, Anzhe Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17030v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17030v1)

**Summary:** We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for...

---

### 8. MeshLoom: Feed-Forward Non-Rigid Registration of Mesh Sequences

**Authors:** Jianqi Chen, Jiraphon Yenphraphai, Xiangjun Tang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17027v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17027v1)

**Summary:** We present MeshLoom, a feed-forward registration network that directly reconstructs vertex deformations across mesh sequences. Our approach advances non-rigid registration beyond existing models, which are typically constrained by costly per-instance optimization, narrow object categories, pairwise-only inputs, or merely intermediate outputs. The network is simple and efficient, registering multiple meshes within seconds. At its core lies a topology-aware encoder--decoder design. Specifically, w...

---

### 9. FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models

**Authors:** Jiaju Han, Ben Zhang, Xuemeng Sun, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17020v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17020v1)

**Summary:** Remote sensing vision-language models have advanced Earth observation understanding, but most existing work remains centered on RGB imagery, leaving the complementary information in infrared data underexplored. Infrared images provide distinctive cues, including thermal intensity structures, object boundaries, and illumination-invariant scene features, which can enrich visual-language learning beyond conventional RGB observations. However, a large-scale RGB-infrared-text dataset for remote sensi...

---

### 10. ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation

**Authors:** Tran Dinh Tien, Zhiqiang Shen

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16996v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16996v1)

**Summary:** Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution decoding is typically run over the entire dataset vocabulary, whereas each image contains only a small active subset of classes. We introduce ActiveSAM, a training-free, zero-shot inference framework that turns SAM 3 into an active-vocabulary segmenter. ActiveSAM first canonicalizes and expan...

---

### 11. DreamX-World 1.0: A General-Purpose Interactive World Model

**Authors:**  DreamX Team, Yancheng Bai, Rui Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16993v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16993v1)

**Summary:** DreamX-World 1.0 is a general-purpose interactive text/image-to-video world model for controllable long-horizon generation. It supports camera navigation, revisits to previously observed regions, and promptable events across photorealistic, game-style, and stylized domains. Our data engine combines camera-accurate Unreal Engine rendering, action-rich gameplay recordings, and real-world videos with recovered camera geometry. For camera control, we introduce E-PRoPE, a lightweight variant of proje...

---

### 12. A Multi-Center Benchmark for Abdominal Disease Diagnosis and Report Generation from Non-Contrast CT

**Authors:** Mariam Elbakry, Aliaa Sayed Sheha, Salma Hassan Tantawy, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16991v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16991v1)

**Summary:** Multiphasic contrast-enhanced CT (CECT) is widely used for abdominal lesion characterization, yet it carries inherent risks of contrast-induced nephropathy, escalates acquisition burden, and heavily contributes to radiologist workload. To address these challenges, we introduce a novel multi-center benchmark for multi-organ abdominal disease diagnosis and automated radiology report generation, which learns to synthesize contrast-enhanced findings from single-phase non-contrast CT (NCCT). To suppo...

---

### 13. SurroundNEXO: Ego-Centric Metric Bridging for Spatially Consistent Geometry in Autonomous Driving

**Authors:** Shuai Yuan, Runxi Tang, Yuzhou Ji, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16960v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16960v1)

**Summary:** Modern autonomous driving depends on accurate metric 3D understanding for perception, reconstruction, and planning, which in turn requires reliable multi-camera depth prediction. However, the outward-facing nature of vehicle-mounted surround-view camera rigs inherently limits visual overlap across views, challenging the correspondence-based assumptions that underpin conventional multi-view geometry. To bridge this gap, we present SurroundNEXO, named after the Spanish word nexo for a geometric li...

---

### 14. Simulation-Based Multi-Fillet Evaluation of Woody Breast Poultry Fillets

**Authors:** Chirantan Sen Mukherjee, Seung-Chul Yoon, William J. Beksi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16951v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16951v1)

**Summary:** Woody breast (WB) is a myopathy in modern broiler chickens that causes the breast muscle to become unusually stiff and fibrous, leading to decreased meat quality and significant economic losses. State-of-the-art automated WB detection relies on a side-view imaging system to analyze the bending behavior of a single fillet as it falls off a conveyor belt. While highly accurate, this approach is constrained by its single-fillet field of view, creating throughput bottlenecks on commercial processing...

---

### 15. Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization

**Authors:** Dongbin Na, Chanwoo Kim, Giyun Choi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16898v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16898v1)

**Summary:** Detecting unanswerable user queries remains essential for the reliable deployment of real-world embodied agents. However, modern vision-language models (VLMs) often generate overly confident answers even when the available visual memory cannot support the query. Such overconfidence poses various task-dependent risks. The agent may provide misleading information to the user in Embodied Question Answering and select an arbitrary coordinate and physically guide the user there in spatial reasoning f...

---

### 16. Latent Space Reinforcement Learning for Inverse Material Estimation in Food Fracture Simulation

**Authors:** Adrian Ramlal, Yuhao Chen, John S. Zelek

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16870v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16870v1)

**Summary:** Realistic visual simulation of food manipulation requires accurate material parameters, yet these are difficult to measure directly and vary across the heterogeneous regions of a single food item. We address the inverse problem of estimating material parameters from a target description of fracture behavior in a non-differentiable continuum damage mechanics simulator. Using orange peeling as a test case, we train a neural surrogate on 2,000 forward simulations and compare Covariance Matrix Adapt...

---

### 17. Federated Medical Image Segmentation under Real-World Label Noise: A Benchmark Suite for Noisy Label Learning Method Selection

**Authors:** Markus Bujotzek, Dimitrios Bounias, Stefan Denner, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16868v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16868v1)

**Summary:** While federated learning (FL) enables collaborative medical image segmentation without centralizing sensitive data, real-world deployment is frequently complicated by cross-site label imperfections such as contour disagreement, missing or additional structures, and confused labels. Federated noisy label learning (FNLL) aims to mitigate these effects, yet remains underused in practice as existing evidence is largely based on synthetic noise, simplified settings, and limited real-world noisy evalu...

---

### 18. Redirecting the Flow: Image Customization through Attention Distribution Shift

**Authors:** Jie Li, Suorong Yang, Jian Zhao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16866v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16866v1)

**Summary:** Subject-driven image customization aims to generate images that not only follow textual instructions but also preserve the identity of a given reference subject. Existing approaches, including test-time fine-tuning, encoder-based methods, and token competition in shared attention spaces, suffer from limited efficiency, misalignment between extracted reference features and the generative process, and interference from irrelevant information. To address these limitations, we formulate the customiz...

---

### 19. An Open-Source Monitoring Framework for Data Exploration and Progress Tracking in Multi-Center Radiology Studies

**Authors:** Markus Bujotzek, Jonas Scherer, Stefan Denner, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16861v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16861v1)

**Summary:** Multi-center studies are crucial for advancing medical and radiological research. Data exploration, collaboration discovery, and study progress monitoring are essential for maximizing their potential. However, in practice these processes often rely on manual communication and shared tables, which quickly become outdated and hinder efficient coordination in large distributed studies. This highlights the need for dedicated monitoring solutions that provide transparent and up-to-date insights into ...

---

### 20. Robust Spoofed Speech Detection via Temporal Pyramid Modeling

**Authors:** Mahtab Masoudi Nezhad, Nima Karimian

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16837v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16837v1)

**Summary:** Spoofed speech detection is increasingly challenged by realistic synthesis, voice conversion, and replay attacks, with cross-dataset generalization remaining a major limitation. This work we propose a Temporal Pyramid Adapter that utilize parallel temporal convolutions with varying receptive fields to capture multi-scale spoofing cues, ranging from local artifacts to global prosodic irregularities. We also integrated self-supervised XLS-R representations combined with front-end adapters, includi...

---

### 21. Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment

**Authors:** Zijie Meng

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16799v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16799v1)

**Summary:** Existing vision-language model (VLM)-based AI-generated image quality assessment (AIGIQA) methods suffer from a fundamental semantic-distortion dimensional conflict: monolithic representations optimized for semantic discrimination inherently entangle compositional understanding with low-level perceptual sensitivity, rendering them blind to fine-grained quality degradations. We introduce MST-CLIPIQA, a multi-scale two-stream framework that achieves hierarchical vision-language alignment through e...

---

### 22. WaveDINO: Learning-Based Atmospheric Correction of Unwrapped InSAR Interferograms Validated by GNSS: Results at Laguna del Maule and Campi Flegrei Volcanoes

**Authors:** Robert Popescu, Juliet Biggs, Tianyuan Zhu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16795v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16795v1)

**Summary:** Interferometric Synthetic Aperture Radar (InSAR) enables effective monitoring of volcanic deformation; however, the observed signals are often corrupted by atmospheric phase delays, seasonal surface changes, and decorrelation effects. Existing atmospheric correction methods, such as numerical weather model-based methods, can reduce these effects but do not consistently remove atmospheric artefacts and may introduce residual biases. To address these limitations, we propose a novel learning-based ...

---

### 23. LLM-Based Visual Explanation Evaluation Framework for Assessing the Explainability of Facial Skin Disease Classification Models

**Authors:** Gyuyeon Na

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16794v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16794v1)

**Summary:** This study proposes a domain-specific LLM-based Visual Explanation Evaluation Framework for assessing Grad-CAM explanations in facial skin disease diagnosis models. While previous studies have primarily focused on improving classification performance through data augmentation techniques, relatively few studies have systematically examined whether model explanations are grounded in clinically relevant lesion regions.   In this study, geometric augmentation, color-based augmentation, and mixed aug...

---

### 24. Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations

**Authors:** Zhiqiang Zhou, Junliang Dai, Xu ling

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16783v1)

**Summary:** Multimodal large language models (MLLMs) excel at visual reasoning but rely on text-based chain-of-thought (CoT), lacking interpretable visual intermediates. Existing methods use opaque tokens or external tools, missing key properties. We propose Gen-VCoT, a framework using expert vision models to generate RGB images as reasoning intermediates. It has three stages: visual grounding (SAM segmentation), geometric reasoning (Marigold depth maps), and semantic reasoning (Qwen2-VL integration). An ad...

---

### 25. Text-Vision Co-Instructed Image Editing

**Authors:** Chenxi Xie, Yuhui Wu, Qiaosi Yi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16767v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16767v1)

**Summary:** Existing image editing methods can be generally categorized into textual instruction-based and visual prompt-based ones. Textual instructions are semantically expressive, but are limited by the coarse granularity of spatial control of the editing results. In contrast, visual prompts such as drag and point can provide precise spatial guidance, but are limited by the inherent ambiguity in semantic intent. To unify the strength of textual and visual prompts, we present Text-Vision Co-Instructed Ima...

---

### 26. 3D Classification of Paramagnetic Rim Lesions in Multiple Sclerosis via Asymmetric QSM-FLAIR Modeling

**Authors:** Veronica Pignedoli, Giacomo Boffa, Nicoletta Noceti, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16756v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16756v1)

**Summary:** Paramagnetic rim lesions (Rim$^+$) identified on susceptibility-sensitive MRI have recently emerged as a specific biomarker of chronic active inflammation in Multiple Sclerosis (MS) and are associated with long-term disability progression. However, susceptibility imaging and expert interpretation remain limited to specialized centers, visual assessment is time-consuming and variable, and the low prevalence of Rim$^+$ lesions poses severe class imbalance challenges for automated analysis. We prop...

---

### 27. Structure-aware Knowledge-guided Heterogeneous Mamba for Zygomaticomaxillary Suture Assessment

**Authors:** Xiaoqi Guo, Birui Chen, Xinquan Yang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16749v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16749v1)

**Summary:** The Zygomaticomaxillary Suture is a key circummaxillary structure that connects the zygomatic bone and the maxilla, which serves as a primary site of resistance during maxillary advancement, and its maturation status directly influences the timing and efficacy of orthopedic interventions. However, accurate staging of ZMS maturation remains challenging due to subtle high-frequency transitions in suture lines and the global semantic ambiguity between adjacent stages. To address this, we present th...

---

### 28. Revealing Artifacts via Noise Amplification: A Novel Perspective for AI-Generated Video Detection

**Authors:** Renxi Cheng, Jie Gui, Hongsong Wang

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16742v1)

**Summary:** With the rapid advancement of video generation models, distinguishing between AI-generated and authentic videos has emerged as a challenging endeavor. The majority of existing research endeavors concentrate on the development of detectors for identifying samples generated by generative adversarial networks. Nevertheless, the detection of AI-generated videos, particularly those produced by text-to-video models, still remains an uncharted territory. Although state-of-the-art text-to-video models c...

---

### 29. PATCH: Action-Chunk-Conditioned Latent Patch Innovation Monitoring for Robot Manipulation

**Authors:** Yanan Zhou, Ranpeng Qiu, Yincong Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16690v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16690v1)

**Summary:** Learning-based manipulation policies have made substantial progress in real-world robot manipulation, particularly for short-horizon action generation. However, deployment in open workspaces remains fragile under unexpected local scene dynamics, such as moving objects, transient occlusions, or disturbances near the intended motion. Existing runtime monitors often rely on global observation anomalies, policy uncertainty, or frame-level visual changes, and struggle to distinguish task-relevant exe...

---

### 30. MMDiff: Extending Diffusion Transformers for Multi-Modal Generation

**Authors:** Yagmur Akarken, Orest Kupyn, Christian Rupprecht

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16673v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16673v1)

**Summary:** Diffusion transformers have demonstrated remarkable generative capabilities, yet the rich perceptual representations computed across their denoising trajectory are discarded once the content is rendered. We present MMDiff, a framework that transforms a frozen diffusion transformer into a multi-modal generative system that jointly produces images alongside any combination of dense perceptual modalities using lightweight decoder heads. Our central finding is that perceptual information is temporal...

---

### 31. Sinkhorn-CPD: Robust point cloud registration via unbalanced entropic optimal transport

**Authors:** Jin Zhang, Mingyang Zhao, Bing Liu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16672v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16672v1)

**Summary:** Coherent Point Drift (CPD) is widely used for rigid point cloud registration because of its soft correspondences and closed-form parameter updates. However, CPD's target-side marginal constraint forces every observation, including outliers, to receive exactly unit probability mass. This assumption degrades registration accuracy under heavy outliers and partial overlap. Optimal transport (OT) methods can handle missing mass through unbalanced formulations, but require hand-tuned annealing schedul...

---

### 32. Look Again Before You Abstain:Budgeted Conformal Evidence Acquisition for Reliable Vision-Language Model

**Authors:** Jian Xu, Delu Zeng, John Paisley, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16667v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16667v1)

**Summary:** Large vision-language models (LVLMs) hallucinate: they assert visual details that the image does not support. A principled remedy is selective prediction with a distribution-free guarantee-verify each claim and abstain when the claim is not grounded, so that the hallucination rate among asserted claims is provably bounded. We show, however, that this guarantee is bought at a brutal price: to keep the hallucination rate below $5\%$ on a balanced object-existence benchmark, a state-of-the-art conf...

---

### 33. Vision-Language Models as Zero-Annotation Oracles in Histopathology

**Authors:** Vishal Jain, Giorgio Buzzanca, Sarah Cechnicka, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16658v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16658v1)

**Summary:** Foreground segmentation is the critical first step of every computational pathology pipeline, yet existing methods rely on hand-tuned heuristics or supervised models that overfit to narrow stain and scanner distributions, failing silently on specialised stains such as Jones silver or Elastica van Gieson. We propose a coarse-to-fine approach that recasts foreground segmentation as a visual perception task and leverages general-purpose vision-language models (VLMs) as zero-annotation oracles. Our ...

---

### 34. MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods

**Authors:** Robert Langendörfer, Markus Hillemann, Markus Ulrich

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16638v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16638v1)

**Summary:** 3D object reconstruction, and camera pose estimation in industrial applications are challenging tasks, as errors are costly while the computation time is often limited. The complexity of typical industrial objects further complicates these tasks. Most of the existing datasets in this context do not depict realistic industrial scenarios. Therefore, we introduce the Machine Vision Metrology Industrial Object Dataset (MVM-IOD). Images of typical industrial objects are captured systematically, by mo...

---

### 35. DCP-Prune: Ultra-Low Token Pruning with Distribution Consistency Preservation

**Authors:** Xifeng Xue, Xiaokang Wang, Zirui Li, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16633v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16633v1)

**Summary:** Recent vision token pruning methods effectively preserve model performance under moderate token budgets but become unstable under ultra-low token budget. Our analysis shows that as the pruning budget decreases, accuracy degradation is often accompanied by larger feature distribution shifts. Critically, the degree of this distribution shift strongly correlates with performance degradation. To better characterize this phenomenon, we introduce a lightweight distribution consistency metric to estima...

---

### 36. SUP-MCRL: Subject-aware Unified Pseudo-feature Coded Multimodal Contrastive Representation Learning for EEG Visual Decoding

**Authors:** Shengyu Gong, Weiming Zeng, Yueyang Li, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16615v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16615v1)

**Summary:** Non-invasive brain-computer interfaces suffer severe fidelity degradation in neural visual decoding when generalizing to natural visual experiences. Conventional multimodal contrastive representation learning solely optimizes geometric distance alignment, neglecting semantic consistency and subject selectivity, causing spurious zero-shot alignment. We propose SUP-MCRL, a unified framework integrating three collaborative mechanisms: (1) Semantic-entity Aware Visual Encoder (SAVE), learning spatia...

---

### 37. DifferAD-R1: A Difference-Guided IndustrialAnomaly Localization with Multimodal LargeLanguage Models

**Authors:** Dingrong Wang, Xian Tao, Zhen Qu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16601v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16601v1)

**Summary:** Industrial anomaly localization aims to accurately identify and localize abnormal regions in industrial products, addressing the critical challenge of detecting unseen defect categories in real-world scenarios. Traditional closed-set methods often suffer from poor cross-scenario generalization, while existingMultimodal Large Language Model (MLLM)-based approachesface two core limitations: they either adopt QA-style paradigmsmisaligned with the practical demands of localization, or relyon standar...

---

### 38. Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models

**Authors:** Weichen Dai, Ruixun Yu, Yangjie Tang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16593v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16593v1)

**Summary:** Object pose estimation is crucial to many industrial applications, with one example being automated spray painting using a robot. However, confidentiality concerns often limit access to high-quality 3D models, posing a significant challenge for point-cloud-based pose estimation. In such scenarios, rotational symmetry, a readily accessible characteristic of many industrial objects, can provide valuable prior information to facilitate pose estimation.In this paper, we propose a method that leverag...

---

### 39. LOCUS: Local Visual Cue Search for Enhancing Fine-Grained Perception in Multimodal Large Language Models

**Authors:** Zhou Tao, Fang Zhang, Zewen Ding, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16586v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16586v1)

**Summary:** Multimodal Large Language Models (MLLMs) remain unreliable on fine-grained visual perception, even when high-resolution inputs preserve the necessary local details. We identify this limitation as visual context rot: decisive evidence may exist in the full image, yet fail to be reliably selected and used amid redundant visual context. We propose LOCUS (LOcal visual CUe Search), a training framework that teaches MLLMs to internalize local evidence search through a verifiable proxy task. During tra...

---

### 40. Multi-Modal Spatio-Temporal Graph Neural Network with Mixture of Experts for Soil Organic Carbon Prediction

**Authors:** Daniele Mos, Felipe Drummond, Anton Bossenbroek, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16580v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16580v1)

**Summary:** Top-soil organic carbon (SOC) prediction is fundamental to agricultural sustainability, land use policy and fertilization planning. Existing approaches face two limitations: they pair hand-crafted covariates with classical ML or single-modal deep models that miss rich spectral and temporal information, and grid-based architectures ignore the irregular spatial structure of field measurements. We introduce SpTGNN, a multi-modal spatio-temporal graph neural network addressing both. SpTGNN represent...

---

### 41. Transformation-driven generation of comparable projection images from multimodal anatomical scenes

**Authors:** Dariusz Pojda, Krzysztof Domino, Michał Tarnawski, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16573v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16573v1)

**Summary:** This work addresses the computational problem of generating reproducible projection-space observations from heterogeneous anatomical scenes whose components may undergo independent spatial transformations. We propose a transformation-driven framework for synthetic projection imaging from multimodal anatomical data and demonstrate it on mandibular-motion scenarios. In contrast to conventional Digitally Reconstructed Radiograph (DRR) approaches primarily designed for registration, projection reali...

---

### 42. PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models

**Authors:** Zhiang Chen, Nahyuk Lee, Boyang Sun, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16569v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16569v1)

**Summary:** Registering two captures of the same indoor space taken at different times underpins persistent spatial memory for robots and AR systems, yet the realistic version of this task is egocentric and its most scalable form is RGB-only. Head-mounted cameras yield blurry, fast-moving, partially overlapping views from which dense geometry is hard to recover. Classical registration leans on exactly the clean point clouds this setting lacks, while learned scene-graph methods require a pre-built or annotat...

---

### 43. Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence

**Authors:** Yang Luo, Yan Gong, Yongsheng Gao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16566v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16566v1)

**Summary:** 3D Gaussian Splatting (3DGS) has significantly advanced real-time novel view synthesis by representing scenes as dense collections of anisotropic 3D Gaussian primitives. However, the irregular spatial distribution of Gaussians often leads to poor GPU utilization, as warp divergence and redundant computation degrade rendering performance. To address this, we present Local-GS, a warp-coherent rendering paradigm that, organizes Gaussian primitives with respect to SIMT (Single Instruction, Multiple ...

---

### 44. Assessing Reliability of Symbol Detection in Concept Bottleneck Models

**Authors:** Javier Fumanal-Idocin, Javier Andreu-Perez

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16535v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16535v1)

**Summary:** Concept Bottleneck Models (CBMs) are a relevant tool for explainable Artificial Intelligence because they make their predictions through human-interpretable symbols. However, high task accuracy does not guarantee that these symbols are detected faithfully: jointly trained CBMs may encode task-specific shortcuts in the bottleneck, making their explanations unreliable. In this paper, we study concept-detection reliability by swapping independently trained concept detectors and classification heads...

---

### 45. Kairos: A Native World Model Stack for Physical AI

**Authors:**  Kairos Team, Fei Wang, Shan You, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16533v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16533v1)

**Summary:** World models are transitioning from passive visual generators to foundational, operational infrastructure for Physical AI: they must natively acquire world knowledge from heterogeneous experience, maintain persistent states over long horizons, and execute efficiently within real deployment constraints. We introduce Kairos, a native world model stack designed around these requirements. (1) Kairos learns the world by pioneering a Native Pre-training Paradigm governed by a Cross-Embodiment Data Cur...

---

### 46. BadWorld: Adversarial Attacks on World Models

**Authors:** Linghui Shen, Mingyue Cui, Xingyi Yang

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16519v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16519v1)

**Summary:** Visual world models (VWMs) synthesize interactive, action-conditioned rollouts from a single context image. However, it remains an open question how robust these models are to adversarial perturbations. Standard adversarial attacks fail to assess this vulnerability because attackers lack ground-truth future videos and cannot predict subsequent user controls. We introduce BadWorld, a label-free adversarial framework tailored for autoregressive VWMs that systematically overcomes both constraints. ...

---

### 47. Active Reference Acquisition in Few-Shot Font Generation

**Authors:** Shinnosuke Matsuo

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16502v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16502v1)

**Summary:** Few-shot font generation aims to synthesize the remaining glyphs of a font given one or a few reference glyphs while preserving stylistic consistency, thereby supporting font designers in efficiently completing a typeface. Existing methods primarily focus on improving generation quality given a fixed reference set. However, when the current reference glyphs are insufficient to represent the target style, few-shot font generation may fail to produce satisfactory results. In practical scenarios, a...

---

### 48. Lost at the End: Primacy Bias in Multimodal Retrieval-Augmented Question Answering

**Authors:** Jieyuan Liu, Jianyang Gu, Shijie Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16494v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16494v1)

**Summary:** Knowledge-based visual question answering (KB-VQA) lets vision-language systems answer questions that exceed their parametric knowledge by conditioning a reader on passages retrieved from a Wikipedia-scale knowledge base. In pure-text long-context LLMs, retrieved-context use follows the U-shaped "lost-in-the-middle" effect of Liu et al. (2024): information at the start and end of context is used, the middle is lost. Whether this transfers to deployed multimodal KB-VQA is open. To close this gap,...

---

### 49. Unified Multimodal Model for Brain MRI Imputation and Understanding

**Authors:** Zhiyun Song, Che Liu, Tian Xia, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16484v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16484v1)

**Summary:** Multimodal large language models (MLLMs) hold great potential for medicine, as they inherit knowledge from LLM and allow multiple data modalities to be integrated, analysed and interpreted in natural language. However, the field of medical MLLMs is constrained by non-trivial challenges, notably the scarcity of high-quality training data and the frequent occurrence of missing data in the real-world clinical setting. Here, we propose a novel unified multimodal model, UniBrain, for brain magnetic r...

---

### 50. Uncertainty Quality of VGGT: An Analysis on the DTU Benchmark Dataset

**Authors:** Markus Hillemann, Robert Langendörfer, Steven Landgraf, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16479v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16479v1)

**Summary:** Visual Geometry Grounded Transformer (VGGT) has already attracted a great deal of attention in a short period of time, not least due to the Best Paper Award at CVPR-2025. Similar to DUSt3R and MASt3R, VGGT aims to bring about a paradigm shift by replacing established methods like bundle adjustment and feature matching with a simple, unified, feed-forward neural network that predicts camera poses, depth maps, and dense 3D structure directly from multiple images of a scene in a few seconds. A key ...

---

## cs.LG

**50 papers**

### 1. Exact Posterior Score Estimation for Solving Linear Inverse Problems

**Authors:** Abbas Mammadov, Ozgur Kara, Kaan Oktay, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17048v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17048v1)

**Summary:** Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the posterior, but the score that the prior provides is the unconditional score, not the posterior score. Existing methods either steer a fixed pretrained denoiser with approximate measurement-matching corrections, or train a conditional restoration model that abandons the denoising structure of the prior. ...

---

### 2. Geometric Action Model for Robot Policy Learning

**Authors:** Jisang Han, Seonghu Jeon, Jaewoo Jung, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17046v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17046v1)

**Summary:** Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic or temporal priors from large-scale foundation models, but they still operate primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D geometry required for contact-rich manipulation. We propose the Geometric Action M...

---

### 3. Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes

**Authors:** Tongyan Fang, Siyuan Huang, Naiyu Fang, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17043v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17043v1)

**Summary:** When pretrained VLA policies are fine-tuned through online RL, each rollout episode produces only a single binary outcome (success or failure), yet the actor update requires per-transition supervision. Existing approaches commonly reduce this sparse outcome to a single scalar reward or advantage signal, which conflates distinct forms of transition-level feedback and provides limited guidance once basic task success becomes achievable. First, a single scalar signal conflates the two objectives of...

---

### 4. The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers

**Authors:** Alper Yıldırım

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17037v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17037v1)

**Summary:** Oppenheim and Lim (1981) showed that natural images stay recognizable when reconstructed from their Fourier phase alone, while the magnitude carries little of their identity. We ask whether trained image classifiers reproduce this asymmetry inside their hidden layers, and we test it causally: given two images, we transplant the phase of one onto the magnitude of the other at a chosen layer and record which image the prediction follows. In PRISM2D, GFNet, and ViT-B/16 the prediction follows the p...

---

### 5. Your Privacy My Cloak: Backdoor Attacks on Differentially Private Federated Learning

**Authors:** Xiaolin Li, Ning Wang, Ninghui Li, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17035v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17035v1)

**Summary:** Prior research suggests that differential privacy (DP) inherently enhances the robustness of federated learning (FL) against backdoor attacks. In this paper, we challenge this assumption. Through an empirical analysis of two baseline attack strategies, we uncover a fundamental tension in DP-FL: while bypassing DP allows state-of-the-art defenses to detect and filter malicious updates, complying with DP inadvertently masks their distinguishing statistical characteristics. Consequently, existing d...

---

### 6. KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing

**Authors:** Mufei Li, Shikun Liu, Dongqi Fu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17034v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17034v1)

**Summary:** Post-hoc context erasing over the KV cache is challenging because a local edit has a global consequence: once a span has been processed, its influence propagates into the cached states of all subsequent tokens. This issue arises naturally in long-context LLM applications, where stale retrieved facts, incorrect tool observations, retracted user preferences, or harmful prompt injections may be identified only after prefill. Exact erasing must then recompute all tokens after the deleted span, makin...

---

### 7. HAMON: Passive Optical Sequence Mixing for Long-Horizon Forecasting

**Authors:** Alper Yıldırım

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17028v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17028v1)

**Summary:** Simple linear and frequency-domain models remain surprisingly competitive in long-horizon time-series forecasting, and recent mechanistic evidence suggests that standard forecasting benchmarks may not require the dense superposed representations that make transformers powerful in other domains. This raises a substrate-level question: if the core forecasting operator is often low-complexity and approximately linear, does it need to be implemented as learned digital temporal mixing? We introduce H...

---

### 8. ExpRL: Exploratory RL for LLM Mid-Training

**Authors:** Violet Xiang, Amrith Setlur, Chase Blagden, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17024v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17024v1)

**Summary:** Sparse reward reinforcement learning (RL) has become a standard tool for improving LLM reasoning, but its success depends critically on the coverage present in the base model. In practice, models are often primed for RL through \emph{mid-training} on curated reasoning traces that teach useful primitive skills such as decomposition, verification, or self-correction. Although effective, this strategy requires manually specifying what the model should learn, and it remains unclear whether such prim...

---

### 9. Learning the Geometry of Data: A Mathematical Review of Shape Space Analysis

**Authors:** Gary P. T. Choi, Khanh Dao Duc, Shira Faigenbaum-Golovin, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17022v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17022v1)

**Summary:** A central objective of machine learning is to identify structure and patterns in data. Advances in data acquisition have increasingly produced datasets whose observations possess rich geometric form, giving rise to shape spaces that encode variability in object geometry. Such datasets arise across a wide range of disciplines, including biology, medicine, anthropology, and computer vision, where subtle geometric differences often carry important scientific information. Traditional machine learnin...

---

### 10. TokenPilot: Cache-Efficient Context Management for LLM Agents

**Authors:** Buqiang Xu, Zirui Xue, Dianmou Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17016v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17016v1)

**Summary:** As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, ...

---

### 11. Filtered Conformal Ellipsoids for Graph-Native Time Series

**Authors:** Yannick Limmer

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17014v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17014v1)

**Summary:** Joint prediction sets for multivariate time series should control a single event while adapting to cross-coordinate dependence. We study filtered conformal ellipsoids: a frozen state-space filter emits a one-step predictive mean and covariance, and split-conformal calibration is applied to the resulting Mahalanobis scores. The filter is used to choose the ellipsoid shape; conformal calibration chooses the scalar radius, so the construction benefits from a learned predictive covariance without re...

---

### 12. Exploding and vanishing gradients in deep neural networks: the effect of residual connections

**Authors:** Vivek S Borkar

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17013v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17013v1)

**Summary:** The well known phenomenon of exploding and vanishing gradients in deep neural networks is analyzed using multiplicative ergodic theory. The effect of adding a residual connection is explained in this context. Specifically, a characterization of Liapunov exponents due to Furstenberg and Kifer is exploited in order to make a precise statement about the Liapunov spectrum and the effect of residual connections on it.

---

### 13. ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning

**Authors:** Wei Xiao, Weiliang Tang, Yuying Ge, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17011v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17011v1)

**Summary:** Human interventions provide crucial corrective signals for post-training Vision-Language-Action (VLA) models. However, enabling seamless humanoid interventions is a formidable systems challenge due to complex whole-body kinematics and dexterous-hand control. Consequently, the collected intervention trajectories are often suboptimal, and methods that rely on human interventions as expert supervision can absorb hesitant, inefficient, or even erroneous behaviors. To address both the system and algo...

---

### 14. From Tokens to Policy: Causal and Interpretable Heterogeneous Treatment Effects Identification

**Authors:** Riccardo Cadei, Frank Otchere, Nyasha Tirivayi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17010v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17010v1)

**Summary:** Heterogeneous Treatment Effect (HTE) identification is crucial to explain the impact of an intervention and optimize our policies accordingly. Existing approaches trade expressivity for interpretability, but, if some active heterogeneity drivers are unmeasured, methods at both ends of this spectrum allow for spurious HTE characterization with no causal reading. In this work, we focus on controlled experiments and argue that an oracle HTE causal characterization via the latent interactors is now ...

---

### 15. TuneJury: An Open Metric for Improving Music Generation Preference Alignment

**Authors:** Yonghyun Kim, Junwon Lee, Haiwen Xia, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17006v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17006v1)

**Summary:** We introduce TuneJury, an open, instance-level pairwise reward model for text-to-music that predicts a music preference score from a text prompt and an audio clip. The released checkpoint is trained on publicly available human-preference labels covering arena-style (A vs. B) votes, metric-alignment preference pairs, crowdsourced pairwise comparisons, and expert aesthetic ratings. The predicted score margin between two clips is well calibrated on our held-out test split, supporting data filtering...

---

### 16. The Complexity of Min-Max Optimization for Quadratic Polynomials

**Authors:** Martino Bernasconi, Matteo Castiglioni, Andrea Celli, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17000v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17000v1)

**Summary:** We prove that computing approximate stationary points of min-max optimization over the hypercube is PPAD-hard for quadratic polynomials. This holds even when the polynomials are multilinear, each variable appears in at most three monomials, and the approximation factor is inverse polynomial. As a direct consequence, we obtain the first PPAD-hardness results for two-team zero-sum polymatrix games.

---

### 17. Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models

**Authors:** Mehmet Iscan

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16999v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16999v1)

**Summary:** Frozen small code models (<=1.5B parameters, run locally without fine-tuning) suit offline and privacy-constrained use, but often emit plausible-but-wrong programs. A natural remedy is a post-hoc operator that selects, verifies, repairs, or re-processes the model's samples without retraining; in principled form it is Popperian: attack each candidate with a severe test, keep what survives. We measure whether such operators help. Under one deterministic execution oracle and a leakage-free, matched...

---

### 18. ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation

**Authors:** Tran Dinh Tien, Zhiqiang Shen

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16996v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16996v1)

**Summary:** Segment Anything Model 3 (SAM 3) provides a strong frozen backbone for concept-prompted segmentation, but applying it directly to open-vocabulary semantic segmentation (OVSS) is inefficient: full-resolution decoding is typically run over the entire dataset vocabulary, whereas each image contains only a small active subset of classes. We introduce ActiveSAM, a training-free, zero-shot inference framework that turns SAM 3 into an active-vocabulary segmenter. ActiveSAM first canonicalizes and expan...

---

### 19. When in Doubt, Plan It Out: Committed Small Language Model Deliberation for Reactive Reinforcement Learning

**Authors:** Nathan Gavenski, Juarez Monteiro, Francisco Galuppo, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16995v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16995v1)

**Summary:** Reinforcement Learning (RL) policies often degrade in unfamiliar environments because they lack explicit deliberation. We propose Plan, Align, Commit, Think (PACT), a hybrid architecture that combines a fast, reactive RL policy with a slow, deliberative Small Language Model (SLM) planner. PACT invokes the SLM asynchronously to generate and validate candidate action plans. Once a plan is verified through simulation as safe, feasible, and complete, it is executed directly, bypassing the RL policy ...

---

### 20. A Multi-Center Benchmark for Abdominal Disease Diagnosis and Report Generation from Non-Contrast CT

**Authors:** Mariam Elbakry, Aliaa Sayed Sheha, Salma Hassan Tantawy, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16991v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16991v1)

**Summary:** Multiphasic contrast-enhanced CT (CECT) is widely used for abdominal lesion characterization, yet it carries inherent risks of contrast-induced nephropathy, escalates acquisition burden, and heavily contributes to radiologist workload. To address these challenges, we introduce a novel multi-center benchmark for multi-organ abdominal disease diagnosis and automated radiology report generation, which learns to synthesize contrast-enhanced findings from single-phase non-contrast CT (NCCT). To suppo...

---

### 21. Analytic Torsion and Spectral Gap Capture Persistent-Laplacian Performance

**Authors:** Jernej Grlj, Aaron D. Lauda

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16990v1)

**Summary:** While persistent Laplacians (PL) offer a richer geometric representation of data than persistent homology, utilizing their full eigenspectrum for learning tasks is often hampered by high dimensionality and the ``varying length'' problem across different filtration scales. We propose a compact spectral representation that distills the persistent Laplacian into three mathematically grounded invariants: Betti numbers, the spectral gap, and analytic torsion. Across benchmark datasets including MNIST...

---

### 22. Agent trajectories as programs: fingerprinting and programming coding-agent behavior

**Authors:** Hamidah Oderinwale

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16988v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16988v1)

**Summary:** Benchmark scores tell you what an agent got right; they do not tell you how it got there. In this work, we introduce methods for comparing agents procedurally in different contexts, where the model, tasks, and approaches vary. We compare ten agents and find that they are identifiable by their behavioral habits, which we define as fingerprints: a probe over these procedural signatures attributes an unseen trajectory to the correct agent at 85.7% accuracy, controlling for leakage across tasks. We ...

---

### 23. Dynestyx: A Probabilistic Programming Library for Dynamical Systems

**Authors:** Daniel Waxman, Dmitry Batenkov, John Feser, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16985v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16985v1)

**Summary:** State-space models (SSMs) are the standard formalism for Bayesian treatment of dynamical systems, with natural applications in statistics, signal processing, and machine learning. Despite their importance in both theory and application, dynamical systems have proven difficult to incorporate in modern probabilistic programming languages (PPLs), making state-of-the-art methods less accessible to practitioners and introducing friction in following the "Bayesian workflow." We introduce dynestyx, a p...

---

### 24. Decoupling Inference from State Updates in Low-Latency Feature Engines via Probabilistic Thinning

**Authors:** Augusto Peres, Iker Perez, Pedro Valdeira, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16981v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16981v1)

**Summary:** Streaming data systems increasingly underpin Machine Learning workflows that maintain large numbers of continuously updated aggregations. In production settings, each incoming event typically triggers read-modify-write operations to persistent storage, making high-frequency state updates a dominant source of latency, contention, and operational cost. In this work, we decouple inference from state persistence in streaming Machine Learning pipelines via probabilistic thinning: every event is score...

---

### 25. Scalable Pairwise Kernel Learning with Stochastic Vec Trick

**Authors:** Napsu Karmitsa, Tapio Pahikkala, Antti Airola

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16979v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16979v1)

**Summary:** Pairwise learning is a specialized form of supervised learning that focuses on predicting outcomes for pairs of objects. In this work, we introduce SPaiK, a new scalable kernel learning method tailored for pairwise settings. Our approach preserves the expressive power of kernel methods while substantially reducing computational and memory requirements. The key innovation is the stochastic generalized vec trick (sGVT), a stochastic extension of the sparse Kronecker product multiplication algorith...

---

### 26. Task-Error Residual Learning for Real-Robot Five-Ball Juggling

**Authors:** Kai Ploeger, Jan Peters

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16978v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16978v1)

**Summary:** For residual learning that refines existing behavior, sample efficiency depends on two things: how much information each rollout returns, and how efficiently the learner uses that information. Reinforcement learning's standard scalar reward carries far less information than the directional task error that defines the task. Random exploration further discards whatever information each rollout returns. Through residual learning with directional task-error supervision and a task error model that dr...

---

### 27. Sobolev Approximation by Fixed-Size Neural Networks with Arbitrary Accuracy

**Authors:** Baicheng Li, Haizhao Yang, Shijun Zhang

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16975v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16975v1)

**Summary:** In this work, we investigate new activation functions for achieving arbitrary-accuracy Sobolev approximation by fixed-size neural networks. We first show that any function in $W^{2,\infty}((a,b)^d)$ can be approximated with arbitrary accuracy, measured in the $W^{1,\infty}$-norm, by a fixed-size neural network using the Elementary Universal Activation Function ($\mathrm{EUAF}$). To extend this result to $W^{s,\infty}((a,b)^d)$ for $s\in\mathbb{N}$, we introduce a smooth activation $\mathrm{DUAF}...

---

### 28. Beyond the Smile: A Hybrid Convolutional VAE for Crypto Volatility Surfaces

**Authors:** Sadanand Singh, Allam Reddy, Manan Chopra

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16961v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16961v1)

**Summary:** We present a convolutional variational autoencoder for cryptocurrency implied-volatility surfaces, together with a deployable predictor that combines it with a quadratic smile re-fit through a deterministic per-tenor routing rule. Trained on 6,034 fully-filled hourly Binance Options surfaces of BTC and ETH spanning May-October 2023 and parameterised on a common $6 \times 7$ tenor-delta grid, the model attains a hidden-cell surface-completion RMSE in the 0.94-1.56 vol-point range across both mark...

---

### 29. Phantoms and Disclosures: a Causal Framework for Auditing Synthetic Data

**Authors:** Kareem Amin, Rudrajit Das, Alessandro Epasto, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16952v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16952v1)

**Summary:** The rapid adoption of generative AI and Large Language Models (LLMs) has spurred interest in synthetic data as a privacy-preserving alternative to sensitive real-world datasets. However, generating high-utility synthetic data often carries the risk of memorizing and regurgitating private information from the training corpus. In this work, we present a customizable empirical auditing framework designed to detect and explain such data disclosures. Our framework introduces a mechanism to distinguis...

---

### 30. Latent space mapping of interpretable structural coordinates from stochastic single-molecule signals

**Authors:** Matteo Cartiglia, Sandro Kuppel, Wouter Botermans Wannes Peeters, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16950v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16950v1)

**Summary:** Nanopores are versatile single-molecular sensors, but their utility is fundamentally constrained by stochastic translocation dynamics warping any encoded information. We resolve it by shifting from time-domain analysis to a learned latent-space mapping via a contrastive encoder trained exclusively on simulated signals from a physics-informed model. This encoder maps solid-state nanopore signals of engineered DNA barcodes into an interpretable molecular coordinate system. The learned representati...

---

### 31. A nonparametric two-sample test using a parametric integral probability metric

**Authors:** Yuha Park, Yongdai Kim

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16941v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16941v1)

**Summary:** Detecting distributional differences between two independent samples is a fundamental problem in statistics and machine learning. Nonparametric two-sample testing provides a principled framework for determining whether two samples are drawn from the same underlying distribution, without assuming any specific parametric form for the distribution. In this study, we propose a new two-sample test statistic based on a newly introduced integral probability metric (IPM), using a specially designed para...

---

### 32. Scalable Circuit Learning for Interpreting Large Language Models

**Authors:** Naiyu Yin, Dennis Wei, Tian Gao, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16939v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16939v1)

**Summary:** A prominent research direction in mechanistic interpretability is learning sparse circuits over LLM components to reveal how they jointly produce model behavior. However, raw neurons are polysemantic, making learned circuits hard to interpret. Sparse autoencoder (SAE) features alleviate this, but their high dimensionality makes existing intervention-based circuit learning methods computationally prohibitive. We propose CircuitLasso, a scalable circuit-learning approach based on sparse linear reg...

---

### 33. CrossMaps: Confidence-Aware Open-Vocabulary Semantic Mapping for Rover Navigation

**Authors:** Jan-Niklas Klein, Sona Ghahremani, Christian Medeiros Adriano, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16935v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16935v1)

**Summary:** Rovers rely on perception to maintain spatial maps that encode both objects and sensor quality (e.g., range reliability, lighting artifacts, data density), guiding data fusion, embedding updates, and navigation under partial observability. To study these coupled perception-navigation processes, we present CrossMaps, a real-time confidence-aware open-vocabulary semantic mapping pipeline that constructs language-queryable maps from RGB-D data. Building on VLMaps-style approaches, CrossMaps integra...

---

### 34. Exploring Extrinsic and Intrinsic Properties for Effective Reasoning with Code Interpreter

**Authors:** Patomporn Payoungkhamdee, Napat Laosaengpha, Jenta Wonglertsakul, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16934v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16934v1)

**Summary:** Reasoning with a Code Interpreter (CI) has emerged as an effective paradigm for enhancing the reasoning capabilities of large language models (LLMs) through executable computation and iterative verification. Despite its growing adoption, the behavioral properties underlying effective code reasoning remain largely underexplored. In this work, we investigate code reasoning from two distinct perspectives inspired by prior studies of natural language reasoning: extrinsic properties, represented by c...

---

### 35. A Unified Causal-Origin Taxonomy of Distributional Shifts in Reinforcement Learning

**Authors:** Ardianto Wibowo, Paulo E Santos, Amer Baghdadi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16933v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16933v1)

**Summary:** Reinforcement learning (RL) systems often degrade when operating conditions differ from those previously encountered, reflecting distributional shifts in the underlying data-generating process. Such shifts may occur between training and evaluation, as in In-Distribution (ID) and Out-of-Distribution (OOD) generalization, or within non-stationary settings where environment dynamics evolve over time. However, the formal relationship between these views remains unclear, and existing work mainly focu...

---

### 36. Functional Gradient Descent with Adaptive Representations

**Authors:** Daniel Csillag, Rodrigo Schuller, Pedro Dall'Antonia, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16926v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16926v1)

**Summary:** Functional optimization problems are typically solved by optimizing the parameters of a fixed representation, such as a neural network, resulting in highly nonconvex losses that complicate both training and theoretical analysis. An interesting alternative is functional gradient descent (FGD), that is, gradient descent directly in function space, which benefits from strong convergence results and admits a clean theory. However, FGD is difficult to implement in practice because functional gradient...

---

### 37. Demystifying Variance in Circuit Discovery of LLMs

**Authors:** Frank Zhengqing Wu, Francesco Tonin, Volkan Cevher

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16920v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16920v1)

**Summary:** Circuit discovery is a key technique in mechanistic interpretability to pinpoint the model components that are crucial for performing a given task. Although the current state-of-the-art method (EAP-IG) performs well on the metric of (un)faithfulness, it suffers from substantial variability. This includes resampling variance, where the circuit changes when we probe with a new batch of data from the same distribution; rephrasing variance, where the discovered circuit shifts when the prompts are re...

---

### 38. Factorized Neural Operators Decompose Dynamic and Persistent Responses

**Authors:** Hao Tang, Yuechen Duan, Jiongyu Zhu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16900v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16900v1)

**Summary:** Physical systems often exhibit heterogeneous mechanisms, where rapidly evolving dynamics coexist with persistent structures. Capturing such multiscale physical behavior remains challenging for existing neural operators, which typically rely on single dominant inductive bias and therefore couple distinct physical responses into a shared representation. We introduce the Unified Green's Function Framework across domains and propose the Factorized Neural Operators (FaNO), which decompose spectral re...

---

### 39. Fantastic Pretraining Optimizers and Where to Find Them II: Hyperball Optimization

**Authors:** Kaiyue Wen, Xingyu Dang, Kaifeng Lyu, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16899v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16899v1)

**Summary:** Matrix based optimizers such as Muon can substantially speed up language model pretraining, but their gains over AdamW are observed to shrink as model size and data scale grow when using standard constant decoupled weight decay. We propose Hyperball, a simple optimizer wrapper that addresses this issue. Given a base optimizer such as Adam or Muon, Hyperball sets the Frobenius norms of weight matrices and their corresponding optimizer updates to fixed constants. On Qwen3 style models up to 1.2B p...

---

### 40. Beyond Weights and Gradients: A Taxonomy of Federated Learning Messages

**Authors:** Alvaro Javier Vargas Guerrero, Xinguang Wang, Quang Manh Doan, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16891v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16891v1)

**Summary:** Federated Learning is rapidly evolving beyond the exchange of traditional model weights and gradients, yet existing definitions fail to capture the full scope of modern payloads like synthetic data and federated analytics. This paper addresses the gap by proposing a formal mathematical definition of a federated message that accounts for both utility and privacy. We introduce a taxonomy that organizes these exchanges into three categories: model structures, statistical summaries, and data-conditi...

---

### 41. Upper Bounds on the Generalization Error of Deep Learning Models via Local Robustness and Stability

**Authors:** Abdul-Rauf Nuhu, Parham M. Kebria, Vahid Hemmati, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16883v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16883v1)

**Summary:** Generalization is a critical property of data-driven models, particularly deep learning models deployed in safety-critical applications. Robustness-based generalization bounds have gained attention as a principled way to link robustness properties to generalization performance, often in a data-dependent manner. However, most existing bounds suffer from vacuousness in practical settings, yielding loose upper bounds that greatly exceed the actual error rates and limiting their usefulness for real-...

---

### 42. Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM

**Authors:** Meghana R. Bhat, Ankit Umare, Utsav Aggarwal, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16878v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16878v1)

**Summary:** Retail marketing measurement increasingly requires granular campaign-level insights without relying on user-level tracking. However, the two dominant approaches, Marketing Mix Modeling (MMM) and Multi-Touch Attribution (MTA), often produce fragmented insights. MMM is privacy-safe and robust for channel-level planning but is too coarse for campaign optimization, while MTA provides granular attribution but has become less reliable under increasing privacy restrictions. We propose Integrated Market...

---

### 43. HawkesNest: A Multi-Axis Synthetic Benchmark for Spatiotemporal Pattern Complexity

**Authors:** Yahya Aalaila, Sumantrak Mukherjee, Gerrit Großmann, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16863v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16863v1)

**Summary:** Evaluation of spatiotemporal point process (STPP) models relies heavily on opaque real-world datasets, where latent generative structure is unknown and model failures are difficult to attribute. We introduce HawkesNest, a generator-aligned benchmark for controlled spatiotemporal pattern complexity built on a multivariate Hawkes backbone. HawkesNest defines four complexity axes: space--time entanglement, background heterogeneity, cross-type interaction, and domain topology. Each axis is associate...

---

### 44. Deep Q-Learning on Hölder Spaces

**Authors:** Qian Qi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16846v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16846v1)

**Summary:** We study the operator-theoretic core of Q-learning in continuous-time stochastic control with continuous states and actions. In value-based reinforcement learning, each Q-learning or DQN update is built from a Bellman optimality target; our analysis isolates this target in a diffusion setting and studies its regularity and approximation complexity. Under uniform ellipticity and Hölder-regular coefficients, we show that a Bellman update maps bounded inputs into an anisotropic regularity class, sm...

---

### 45. Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models

**Authors:** Martin Jaggi

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16825v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16825v1)

**Summary:** Mixture-of-Experts (MoE) architectures efficiently scale Large Language Models (LLMs) by activating only a small fraction of their experts per token, yet the full parameter count - dominated by the expert parameters - must be held in training and inference memory. To address this, we introduce Expert Tying, an architectural modification that shares expert parameters across consecutive transformer layers while preserving independent, layer-wise routing and attention.   We evaluate this approach a...

---

### 46. A Perception vs. Distortion Perspective on Score-Based Generative Channel Estimation

**Authors:** Marco Skocaj, Lukas Eller, Mate Boban

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16815v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16815v1)

**Summary:** Driven by their remarkable success in computer vision and inverse problem solving, score-based models are increasingly applied to wireless communications, where they show promise across a range of physical-layer tasks. However, despite this growing interest, the current literature often lacks a rigorous analysis of when score-matching offers a tangible advantage over traditional discriminative learning. This paper aims to address this gap through the use-case of channel estimation, a fundamental...

---

### 47. Decision-Weighted Flow Matching for Contextual Stochastic Optimization

**Authors:** Jize Xie, Haomiao Wu, Qiang Chen, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16790v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16790v1)

**Summary:** Conditional generative models are increasingly used as scenario generators for stochastic optimization, but standard training objectives emphasize uniform distributional fit rather than the downstream decisions induced by generated scenarios. This creates an objective mismatch: errors in statistically common regions may have little effect on decision regret, whereas errors in decision-sensitive regions can substantially change the optimal action. We propose Decision-Weighted Flow Matching (DW-FM...

---

### 48. We Need Explanation Cards to Connect Explanation Algorithms to the Real World

**Authors:** Eric Günther, Balázs Szabados, Kristof Meding, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16786v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16786v1)

**Summary:** Algorithmic explanations are intended to help stakeholders understand opaque algorithmic decisions, but in practice, they often fall short. First, the meaning of algorithmic explanations is often not what one might intuitively expect, so expert knowledge is required to interpret them correctly. Second, recent work has shown that popular explanation algorithms are uninformative about the behavior of complex decision functions. Together, these issues create a gap between what explanations appear t...

---

### 49. Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations

**Authors:** Zhiqiang Zhou, Junliang Dai, Xu ling

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16783v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16783v1)

**Summary:** Multimodal large language models (MLLMs) excel at visual reasoning but rely on text-based chain-of-thought (CoT), lacking interpretable visual intermediates. Existing methods use opaque tokens or external tools, missing key properties. We propose Gen-VCoT, a framework using expert vision models to generate RGB images as reasoning intermediates. It has three stages: visual grounding (SAM segmentation), geometric reasoning (Marigold depth maps), and semantic reasoning (Qwen2-VL integration). An ad...

---

### 50. GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled Policy Optimization

**Authors:** Haotian Liu, Yihao Liu, Jingwei Ni, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16771v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16771v1)

**Summary:** As LLMs advance, post-training reinforcement learning (RL) increasingly relies on multi-dimensional rewards to cultivate comprehensive capabilities. This shift demands new algorithms capable of optimizing diverse and potentially competing objectives simultaneously. To address this, existing methods such as Group reward-Decoupled Policy Optimization (GDPO) decompose the overall score into independent reward groups, then compute the RL loss separately within each group. However, this strategy stil...

---

## cs.NE

**50 papers**

### 1. Neural dynamical systems on ferroelectric compute-in-memory for real-time forecasting

**Authors:** Keshava Katti, Adithya Selvakumar, Pratik Chaudhari, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16896v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16896v1)

**Summary:** Neural dynamical systems are expressive temporal predictors that capture continuous-time dynamics through fine-grained state updates. However, this sequential structure maps poorly onto digital hardware optimized for dense matrix operations, a mismatch that analog neuromorphic computing, with its native continuous-time dynamics, can resolve. We introduce FerroNDS, a neuromorphic system built from two analog primitives: an integrator for temporal accumulation and an oscillator for frequency-selec...

---

### 2. Evolution & Foundation: AI Shares Creative Control

**Authors:** Dylan Banarse, Stephen Todd, William Latham, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16849v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16849v1)

**Summary:** This paper investigates the creative process of automated design and artistic evaluation using an evolutionary system. We consider how a multimodal artificial intelligence (AI) model can communicate and guide a combined generative and evolutionary computational system. This creates a framework for the evolution of aesthetically pleasing complex 3D organic forms by integrating genetic algorithms with the visual reasoning capabilities of large-scale AI foundation models.   The framework shifts the...

---

### 3. Effects of Objective Normalization on Regions of Interest in Preference-Based Evolutionary Multi-Objective Optimization

**Authors:** Ryuichi Mogami, Ryoji Tanabe

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16382v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16382v1)

**Summary:** Preference-based evolutionary multi-objective optimization (PBEMO) aims to approximate a region of interest (ROI) defined by the preference information from a decision maker (DM). Although objective functions in real-world applications typically have different scales, the issue of how to define the ROI in such problems has been overlooked in the literature. In fact, it has not been standardized in the EMO community whether the ROI should be defined in the unnormalized objective space or in the n...

---

### 4. Wavelength-Multiplexed 2D Beam Steering via a Passive Diffractive Network

**Authors:** Che-Yung Shen, Yuhang Li, Cagatay Isil, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16261v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16261v1)

**Summary:** We introduce a wavelength-addressable diffractive optical network that transforms illumination wavelength into a high-dimensional control parameter for arbitrarily programmable 2D beam steering. The proposed passive architecture comprises cascaded spatially optimized diffractive layers, jointly designed using deep learning, to rapidly map distinct wavelengths to predefined/desired output angles. Unlike conventional single-layer dispersive optical elements, which are physically restricted to 1D l...

---

### 5. Evolutionary Bilevel Reward Shaping for Generalization in Reinforcement Learning

**Authors:** Ekasit Usaratniwart, Xilin Gao, Marc Ong, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16236v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16236v1)

**Summary:** Reinforcement learning (RL) often suffers from performance degradation when deployed in environments that differ from those encountered during training. Existing techniques such as domain randomization (DR) mitigate this, but require access to diverse training environments and full trajectory observability, assumptions that fail in privacy-preserving or restricted scenarios where only scalar performance metrics are available. We propose Generalization via Evolutionary Reward Shaping (GERS), a bi...

---

### 6. Runtime Analysis of Cartesian Genetic Programming in Evolving Boolean Functions

**Authors:** Duc-Cuong Dang, Roman Kalkreuth, Andre Opris

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15923v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15923v1)

**Summary:** Cartesian Genetic Programming (CGP) is among the practical and popular forms of Genetic Programming as it uses a graph-based representation of programs. This paper presents a first runtime analysis of CGP in evolving Boolean functions using complete training sets. We prove an asymptotic bound $O(n D^5)$ for the expected number of fitness evaluations of CGP to construct a conjunction of $n$ inputs using at most $D \geq n-1$ binary gates, a minimal function set, and even with a strict survival sel...

---

### 7. An Integrated System for Real-Time Student Assessment and Career Guidance Using Neural Networks in Computing Disciplines

**Authors:** Sakir Hossain Faruque, Md. Jubair Hossain, Sharun Akter Khushbu

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15831v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15831v1)

**Summary:** Many undergraduate students in Computer Science (CS) and Software Engineering (SWE) struggle to identify suitable career paths, particularly when their academic performance, abilities, and interests do not fully align. To address this issue, this study proposes an AI-driven Student Assessment and Career Prediction System that integrates a Career Guidance Expert (CGE) system with a Web-Based Student Assessment (WBSA) platform. Within the integrated framework, CGE enhances personalized career reco...

---

### 8. MSC-CMA-ES: Structure-Aware Restarts for CMA-ES via Cyclic Nearest-Better Basin Discovery

**Authors:** Dimitar Nedanovski, Svetoslav Nenov, Dimitar Pilev

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15830v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15830v1)

**Summary:** CMA-ES is, per run, a local optimizer; multimodal search relies on restart strategies such as IPOP and BIPOP, which draw every restart uniformly and reuse no information from previous evaluations. Multi-Start Clustering CMA-ES (MSC-CMA-ES) makes restarts structure-aware: in alternating cycles, a Sobol pre-sample is partitioned into approximate basins of attraction by nearest-better clustering, restarts are seeded basin by basin with locally scaled step sizes and population sizes, redundant basin...

---

### 9. AQ4SViT: An Automated Quantization Framework with Search Gating Policy for Compressing Spiking Vision Transformers

**Authors:** Rachmad Vidya Wicaksana Putra, Saad Iftikhar, Muhammad Shafique

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15523v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15523v1)

**Summary:** Spiking Vision Transformers (SViTs) have emerged as alternative low-power ViT models, but their large sizes hinder their deployments on resource-constrained embedded AI systems. To address this, state-of-the-art works proposed quantization techniques to compress SViT models, but their manual, human-guided approach needs a huge design time and power/energy consumption to find the appropriate quantization setting for each given network, making this approach not scalable for quantizing multiple net...

---

### 10. Large Language Model-Driven Cooperative Operator Ensemble Evolution for Permutation Flow Shop Scheduling

**Authors:** Rui Xu, Yufan Liao, Haoze Lv, et al.

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15334v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15334v1)

**Summary:** The permutation flow shop scheduling problem (PFSP) is a classical NP-hard combinatorial optimization problem in intelligent manufacturing. In practice, PFSP is commonly addressed using metaheuristic algorithms, among which the iterated greedy (IG) algorithm is widely adopted due to its simplicity and strong empirical performance. However, classical IG relies on a single fixed destruction operator, which often limits exploration and leads to search stagnation on large and complex problem instanc...

---

### 11. Controlled Dynamics Attractor Transformer

**Authors:** Cheng Zhang, Minnan Luo, Zesheng Yang, et al.

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15207v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15207v1)

**Summary:** Transformer architectures have dramatically advanced representation learning and inference in deep models through self-attention mechanisms. In parallel,associative memory (AM) frameworks map representations onto energy landscapes, offering interpretable retrieval mechanisms. However, their continuous-time inference dynamics lack the biological plausibility of classical Continuous Attractor Neural Networks (CANNs). To bridge this gap, we propose Controlled Dynamics Attractor Transformer (CDAT), ...

---

### 12. Comparison Patrols on Drifting Orders: Certified Rank Maintenance, Evolving Planar Maxima, and Selection under Drifting Fitness

**Authors:** Faruk Alpay, Levent Sarioglu

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.15022v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15022v1)

**Summary:** Rank-based selection in dynamic environments acts on order information that becomes stale while it is being used. Tournaments, elitism, truncation, and Pareto selection may therefore consume rankings that no longer match the current fitness order, while full re-evaluation competes with search for the same budget. This paper formulates the missing information layer as a data-structure problem. A hidden total order on $n$ items drifts by adjacent transpositions, while a maintainer receives one tru...

---

### 13. Harnessing cortical geometry, wiring, and function as inductive biases for recurrent neural networks

**Authors:** Mo Shakiba, Rana Rokni, Mohammad Mohammadi, et al.

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14975v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14975v1)

**Summary:** How the wiring and functional organization of cortex shape recurrent computation remains a central question in both neuroscience and machine learning. Here, we leverage data released through the Machine Intelligence from Cortical Networks (MICrONS) program--a functional connectomics resource spanning multiple areas of mouse visual cortex, in which dense calcium imaging is co-registered with high-resolution electron microscopy reconstruction from the same animal--to build biologically grounded re...

---

### 14. Test-Time Adaptation of Spiking Neural Networks for Intracortical Neural Decoding using Membrane Potential Alignment

**Authors:** Guangzhi Tang

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14866v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14866v1)

**Summary:** Intracortical brain-computer interfaces suffer from day-to-day neural signal shifts that degrade pretrained decoders. Existing unsupervised adaptation methods rely on deep recurrent or adversarial architectures that are too computationally expensive for implantable hardware. We propose Membrane Potential Alignment (MPA), a test-time adaptation method for spiking neural networks that realigns a pretrained decoder to shifted recordings by only matching membrane potential distributions via KL diver...

---

### 15. Operator Calculus for Population-Based Optimization: A Mean-Field Convergence Theory

**Authors:** Pekka Malo, Lauri Viitasaari, Patrik Nummi, et al.

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14289v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14289v1)

**Summary:** Population-based and distributional optimization methods, from evolution strategies and consensus-based optimization to covariance-matrix adaptation and stochastic gradient methods viewed as distributional dynamics, are widely used for nonconvex or black-box problems, yet their convergence analyses remain fragmented across algorithm-specific techniques. We introduce an operator calculus in which a broad class of such methods, after choosing an appropriate state space and, where necessary, augmen...

---

### 16. MeEvo: Metacognitive Evolution Combined with Natural Evolution for Automatic Heuristic Design

**Authors:** Zishang Qiu, Xinan Chen, Rong Qu, et al.

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14202v2) | 📄 [PDF](https://arxiv.org/pdf/2606.14202v2)

**Summary:** Large Language Models (LLMs) have advanced Automatic Heuristic Design (AHD) by enabling heuristic generation through reasoning and code synthesis. Existing LLM-based AHD architectures mainly follow two paradigms: Natural Evolution, which uses crossover and mutation to explore heuristic programs, and Metacognitive Evolution, which refines reasoning through reflection. However, Natural Evolution discards reasoning traces, weakening knowledge inheritance and exploitation, while Metacognitive Evolut...

---

### 17. A Programmer's Guide to Cascaded Adaptive Combiners: Online Learning by Biologically Accurate Models of Multilayer Neuron Networks

**Authors:** Martin Nilsson, Denis Kleyko

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14146v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14146v1)

**Summary:** Learning in biological multilayer neuronal networks offers insights that extend beyond the classical weighted-sum neuron model commonly used in artificial neural networks. This article presents an accessible guide to a mechanistic neuronal network model that more accurately captures aspects of biological computation while enabling a simple yet powerful mechanism for learning in multilayer neural networks. The proposed approach supports efficient online streamed learning and provides a practical ...

---

### 18. Co-Evolved Spiking Neural Network Ensembles via Marginal Contribution Fitness

**Authors:** Catherine Rodriquez, James Ghawaly

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.13985v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13985v1)

**Summary:** Evolutionary optimization of spiking neural networks (SNNs) becomes increasingly difficult as task complexity grows because they must search a combined topology--parameter space that grows super-exponentially with network size. We address this scaling challenge through a co-evolutionary ensemble framework in which a population of candidate SNNs is evolved with fitness defined by each network's marginal contribution to group performance. Grounded in cooperative game theory and difference evaluati...

---

### 19. SpikF-GO: Spiking Fourier Graph Operators for Multivariate Time Series Forecasting

**Authors:** Jafar Bakhshaliyev, Niels Landwehr

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13901v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13901v1)

**Summary:** Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to conventional neural networks, demonstrating strong performance in computer vision and robotics. More recently, SNNs have been applied to time series forecasting (TSF), with methods exploring spiking temporal backbones, spike-compatible positional encodings, Fourier-domain processing, and redesigned neuron dynamics. However, existing SNN forecasting approaches process variables independently, lacking explicit mechan...

---

### 20. ReSCom: A Reconfigurable Spiking Neural Network Accelerator Using Stochastic Computing

**Authors:** Ali Alipour Fereidani, Mohammad Rasoul Roshanshah, Saeed Safari

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13560v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13560v1)

**Summary:** Spiking Neural Networks (SNNs) provide an attractive framework for energy-efficient inference due to their event-driven computation and biologically inspired dynamics. However, efficient hardware realization of SNNs remains challenging because neuronal computations incur significant power and area costs, and uncontrolled approximate arithmetic can destabilize recurrent state updates when precision is not properly managed. To address these challenges, this paper presents ReSCom, a reconfigurable ...

---

### 21. Adaptive-Frequency Resonate-and-Fire Neurons for Spectral Estimation of Streaming Radar Signals

**Authors:** Stefano Chiavazza, Sen Yuan, Marc Geilen, et al.

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13516v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13516v1)

**Summary:** Frequency Modulated Continuous Wave (FMCW) radar systems traditionally rely on Fourier-based methods, such as the Fast Fourier Transform (FFT), to estimate target range and velocity. While computationally efficient, these approaches require storing and processing large blocks of data, which can become a bottleneck in memory-constrained or low-latency applications. In this work, we propose a neuromorphic-inspired signal processing method based on adaptive resonate-and-fire (ARF) neurons formulate...

---

### 22. Impedance MPC with Patient-Torque Estimation for Knee Rehabilitation Exoskeletons

**Authors:** Yongyan Cao, Jinshan Tang

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13485v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13485v1)

**Summary:** Knee rehabilitation exoskeletons must enforce a prescribed joint trajectory while remaining safely compliant with involuntary spasm and voluntary patient effort-objectives in tension for any fixed-gain impedance controller. We present an Impedance Model Predictive Control framework for knee rehabilitation exoskeletons, demonstrated on a series-elastic-actuator (SEA) platform: an algebraic feedforward reduces the knee dynamics to a constant-coefficient scalar double integrator, and a receding-hor...

---

### 23. The $(1 + 1)$-EA in Dynamic Environments

**Authors:** Georg Hasebe, Johannes Lengler, Raghu Raman Ravi

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13360v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13360v1)

**Summary:** We study the $(1 + 1)$-EA in dynamic linear environments, where in every generation selection is performed with respect to a freshly sampled linear function with positive weights. We consider the Dynamic Binary Value problem, where each generation uses a uniformly random permutation of $1,2,4,\dots,2^{n-1}$, and a Uniform weight variant, where the weights are drawn independently from $\mathrm{Unif}(0,1)$. Both of them have recently been integrated into the IOHprofiler platform and empirically st...

---

### 24. SupraSNN: Exploiting Synapse-Level Parallelism in Spiking Neural Network Accelerators through Co-Optimized Mapping and Scheduling

**Authors:** Seyed Sadra Ghavami, Mohammad Hossein Nikkhah, Mohammad Rasoul Roshanshah, et al.

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13354v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13354v1)

**Summary:** Spiking Neural Networks (SNNs) offer a brain-inspired path toward highly efficient computation, but their practical deployment is constrained by the challenge of managing and executing their massive parallelism on physical hardware. This problem mirrors the historical challenge in processor design of moving beyond serial execution, a barrier broken by superscalar architectures that dispatch multiple instructions to parallel functional units. Drawing inspiration from this paradigm, we introduce a...

---

### 25. Improved Runtime Bound for the $(μ+ 1)$ EA on BinVal

**Authors:** Joris Belder, Johannes Lengler, Raghu Raman Ravi

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13344v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13344v1)

**Summary:** We study the $(μ+1)$ EA on the Binary Value function BinVal. We show that it needs at most $O(μ\log μ\cdot n \log n)$ function evaluations to find the optimum when $μ= o(n/\log n)$. This substantially improves upon the recent upper bound of $O(μ^5 n \log(n/μ^4))$ by Krejca, Neumann and Witt. Our results hold for several mutation operators including standard bit mutation. In particular, our bound implies that the $(μ+1)$ EA is at most a factor $O(\log μ\cdot \log n)$ slower on BinVal than on OneM...

---

### 26. Runtime Analysis of the $(μ+ 1)$-ES in a Homogenous Progress Model

**Authors:** Johannes Lengler, Raghu Raman Ravi

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13323v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13323v1)

**Summary:** We introduce a new simple model to study the fitness progress of Evolution Strategies (ES) in generic problems. In this model, we bypass the underlying fitness landscape and assume that the mutation of any individual produces an offspring whose fitness relative to the parent is given by an invariant distribution $Z$, such as a mean-shifted Gaussian. This serves as a prototypical model for the optimisation landscape when an evolution algorithm operates far from the global optimum. This simple mod...

---

### 27. Modern analog computing for solving differential and matrix equations

**Authors:** Zhong Sun, Piergiulio Mannocci, Manuel Le Gallo, et al.

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13179v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13179v1)

**Summary:** In recent years, driven by the computational demands of data-intensive applications such as artificial intelligence and scientific computing, analog computing has gained renewed interest. Given the diversity of computational tasks and recent advancements in analog CMOS circuits and resistive memory technologies, we refer to the evolving landscape as modern analog computing. In this context, we identify three core computational primitives: solving differential equations, solving matrix equations,...

---

### 28. MP3: Multi-Period Pattern Pre-training for Spatio-Temporal Forecasting

**Authors:** Lilan Peng, Yandi Liu, Qingren Yao, et al.

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13119v2) | 📄 [PDF](https://arxiv.org/pdf/2606.13119v2)

**Summary:** Spatio-Temporal forecasting is crucial in diverse fields, such as transportation, climate, and energy. Urban spatio-temporal data exhibits temporal mirage: similar short-window inputs have divergent future trends, and vice versa. Existing spatio-temporal graph neural networks (STGNNs) cannot effectively identify such mirages. We argue that the core reason lies in the short-window inputs that have incomplete period observation, heterogeneous global spatial correlation, and cross-period superposit...

---

### 29. Multi-Objective Coevolution of Prompts and Templates for Circuit Approximation

**Authors:** Martin Tomasovic, Lukas Sekanina

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13089v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13089v1)

**Summary:** Approximate multipliers deliberately relax computational accuracy to achieve gains in power efficiency, latency, and silicon area, which makes them well-suited for error-resilient applications such as neural networks. In this work, we introduce a co-evolutionary algorithm that leverages an off-the-shelf large language model (LLM) without requiring domain-specific training to automate the design of optimized 8-bit approximate multipliers. The approach simultaneously evolves a population of candid...

---

### 30. Circuit Synchronization Precedes Generalization: Causal Evidence from Fourier Structure in Grokking Transformers

**Authors:** Achyuthan Sivasankar

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.12966v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12966v1)

**Summary:** Grokking -- where a transformer on modular arithmetic suddenly transitions from near-chance to near-perfect validation accuracy -- is attributed to a Fourier circuit, but its timing, causal structure, and controllability remain poorly understood. We introduce the Frequency Synchronization Degree (FSD), a normalised, permutation-tested metric for Fourier circuit synchronisation requiring no prior circuit knowledge. Across nine modular addition configurations (primes p in {53, 71, 97, 113, 131}, t...

---

### 31. Mixed-Categorical Black-Box Optimization via Information-Geometric Bilevel Decomposition

**Authors:** Marc Ong, Shinichi Shirakawa, Youhei Akimoto

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.12885v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12885v1)

**Summary:** Mixed categorical-continuous optimization arises in many practical domains, yet remains challenging. In the black-box setting, evolution strategy-based approaches have shown promise in extending the efficiency and robustness of the CMA-ES to mixed-variable spaces. However, these methods exhibit worsened performance when strong categorical-continuous interactions are present, as their underlying search distributions assume independence between categorical and continuous variables. To address this...

---

### 32. SPEA2$^+$: Improved Density Estimation in SPEA2 with Provable Runtime Guarantees

**Authors:** Duc-Cuong Dang, Andre Opris, Dirk Sudholt

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.12382v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12382v1)

**Summary:** The Strength Pareto Evolutionary Algorithm 2 (SPEA2) is a popular and prominent evolutionary algorithm for solving multi-objective optimisation problems. Despite its popularity, theoretical analyses of SPEA2 have only appeared recently. Moreover, these analyses focus exclusively on how SPEA2 handles non-dominated solutions and disregard the algorithmic components responsible for handling dominated solutions. We conduct a first runtime analysis of SPEA2 for which these components are analysed. We...

---

### 33. The Standard Interpretable Model: A general theory of interpretable machine learning to deductively design interpretable methods using Lagrangian mechanics

**Authors:** Pietro Barbiero, Giovanni De Felice, Mateo Espinosa Zarlenga, et al.

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.12289v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12289v1)

**Summary:** As Artificial Intelligence models grow in complexity, interpretability has become an indispensable tool for understanding, debugging, and controlling their computations. However, interpretability lacks general theories to deductively design interpretable methods. This gap between theories and methods results in a fragmented literature and inconsistent evaluation protocols.   To fill this gap, we introduce the Standard Interpretable Model (SIM), a general theory grounded in Lagrangian mechanics t...

---

### 34. SpikeDecoder: Realizing the GPT Architecture with Spiking Neural Networks

**Authors:** Claas Beger, Florian Walter, Alois Knoll

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.12287v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12287v1)

**Summary:** The Transformer architecture is widely regarded as the most powerful tool for natural language processing, but due to a high number of complex operations, it inherently faces the issue of high energy consumption. To address this issue, we consider Spiking Neural Networks (SNNs), which are an energy-efficient alternative to conventional Artificial Neural Networks (ANNs) due to their naturally event-driven approach to processing information. However, this inherently makes them difficult to train. ...

---

### 35. Mathematical perspective on genetic algorithms with optimization guided operators

**Authors:** Anna Brandenberger, Ilan Doron-Arad, Elchanan Mossel

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.12279v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12279v1)

**Summary:** Recent work in ML applies genetic algorithms at inference time to iteratively improve solutions to optimization problems. The basic mutation and recombination operators involved are qualitatively different from those studied classically. Mutations are no longer random; an ML algorithm mutates a solution with the goal of improving an objective. Similarly, recombination is not based on random collages of parent solutions. Instead, it is an ML optimization-based operator whose goal is to synthesize...

---

### 36. Attention by Synchronization in Coupled Oscillator Networks

**Authors:** Fabio Pasqualetti, Taosha Guo

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.12059v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12059v1)

**Summary:** We address transformer attention on energy-constrained physical substrates. Softmax attention requires exponentiation and global reduction, operations with high energy cost on von Neumann hardware and no natural physical analog. We show that Kuramoto synchronization dynamics (which arise in electrical, mechanical, superconducting, and charge-density-wave oscillator arrays, among other physical systems) implement a well-defined attention operation without either. The resulting mechanism, fixed-qu...

---

### 37. A Spiking Neural Architecture for Coordinating Arm and Locomotor Control

**Authors:** Lea Steffen, Kathryn Simone, Graeme Damberger, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11034v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11034v1)

**Summary:** Spiking Neural Networks (SNNs) coupled with neuromorphic hardware offer energy-efficient solutions for humanoid robot control. However, existing SNN-based motor control systems address bipedal locomotion and arm control in isolation, leaving integrated control of both unaddressed. We present a spiking architecture that coordinates force-based arm control and bipedal locomotion in a simulated humanoid, using the Neural Engineering Framework (NEF) and Semantic Pointer Architecture (SPA). High-leve...

---

### 38. Analog Quantum Asynchronous Event-Based Graph Neural Network

**Authors:** Kristian Sotirov, Shaheen Acheche, Antonio A. Gentile, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11000v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11000v1)

**Summary:** Asynchronous, event-based graph neural networks (AEGNNs) have recently emerged as an efficient paradigm for processing the sparse and high-temporal-resolution data from event cameras. In this paper, we propose quantum analog AEGNNs (QA-AEGNNs), a novel framework to implement an AEGNN on a neutral-atom quantum computer. Neutral-atom quantum processors offer a programmable analog quantum computing platform based on controllable Rydberg-atom interactions. To this end, we map the streaming event dat...

---

### 39. Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design

**Authors:** Wenxin Wang, Yule Hou, Yu Ji, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10493v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10493v1)

**Summary:** Local deployment of large Mixture-of-Experts (MoE) models falls short of the service quality achieved in cloud-scale environments, even under low-concurrency workloads. We identify four key gaps in local MoE inference: reliance on capacity-reduced models (quantized, distilled, rerouted), inability to meet 30-second TTFT for long prefills (more than 12K), sub-baseline decode throughput (under 20 tokens/s), and poor concurrency under mixed prefill-decode and batched decode workloads. We present a ...

---

### 40. LLM-Guided Neural Architecture Search for Robust Co-Design of Physical Neural Networks

**Authors:** Tyler King, Timothee Leleu

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10294v1)

**Summary:** Deploying neural networks on unconventional hardware demands architectures that co-optimize task accuracy and platform-specific constraints such as energy cost, physical non-idealities, and numerical precision. Existing neural architecture search (NAS) methods are typically tailored to a single hardware family, limiting cross-platform comparison and generalization. We introduce Unconventional Hardware Neural Architecture Search (UH-NAS), a hardware-agnostic, LLM-guided NAS framework that integra...

---

### 41. My Chemical Harness: Evolutionary Molecular Design over Synthetic Pathways with Large Language Model Agents

**Authors:** César Ojeda, Darius A. Faroughy, Maryam Karimi, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.11256v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11256v1)

**Summary:** Designing molecules with target properties is most useful when candidate structures are accompanied by feasible synthetic routes. We introduce My Chemical Harness, a route-native evolutionary framework for goal-directed molecular design in which the search population consists of executable synthetic pathways rather than isolated molecular graphs. Each route is built from purchasable building blocks and reaction templates, executed by deterministic chemistry tools, and scored through task-specifi...

---

### 42. Discovering Interpretable Multi-Parameter Control Policies for Evolutionary Algorithms Using Deep Reinforcement Learning

**Authors:** Tai Nguyen, Phong Le, Carola Doerr, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10129v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10129v1)

**Summary:** While deep Reinforcement Learning (deep-RL) has been increasingly applied to parameter control in evolutionary algorithms, rigorous theoretical analysis of parameter control remains largely restricted to single-parameter settings, owing to the difficulty of deriving effective, interpretable multi-parameter policies amenable to formal study. We demonstrate how deep-RL can be leveraged to overcome this barrier, using the (1+($λ$,$λ$))-genetic algorithm optimizing OneMax, one of the few problems wh...

---

### 43. Spiking Neural Network inference on FPGAs with hls4ml

**Authors:** Barry M. Dillon

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10008v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10008v1)

**Summary:** Spiking Neural Networks (SNNs) provide a naturally temporal machine-learning framework. Their neurons maintain an internal state and propagate information through discrete spikes, enabling low-latency temporal inference. Although SNNs are often associated with asynchronous neuromorphic processors, many scientific real-time inference systems rely on conventional synchronous field-programmable gate arrays (FPGAs) and high-level synthesis (HLS) workflows. In this paper we present an extension of hl...

---

### 44. Quality-Diversity Search in Sound Generation: Investigating Innovation Engines for Audio Exploration

**Authors:** Björn Þór Jónsson, Çağrı Erdem, Stefano Fasciani, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09780v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09780v1)

**Summary:** This study addresses the challenges composers and sound designers face in creating and refining tools to achieve their musical goals. Using evolutionary processes to promote diversity and foster serendipitous discoveries, we automate the search through uncharted sonic spaces for sound discovery, arguing that diversity-promoting algorithms can bridge the gap between the theoretical realisation and practical accessibility of sounds. We describe a system for generative sound synthesis combining Qua...

---

### 45. Hybrid Metaheuristic Combining the Dragonfly Algorithm and Tabu Search for the Traveling Salesman Problem

**Authors:** Ammar Bouketta

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09529v1)

**Summary:** The Traveling Salesman Problem (TSP) is a classical NP-hard combinatorial optimization problem that aims to find the shortest Hamiltonian cycle visiting each city exactly once and returning to the starting point. This paper proposes a hybrid metaheuristic for the TSP by combining the Dragonfly Algorithm (DA), a swarm-intelligence-based global search method, with Tabu Search (TS), a memory-based local search technique. The proposed method follows a High-Level Relay Hybridization (HRH) scheme, in ...

---

### 46. Local Search on Vertex Coloring for Bipartite Graphs

**Authors:** Johanna Gasse

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09509v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09509v1)

**Summary:** Local search is a well-known heuristic method used in optimization. In this thesis, we explore its capabilities on the vertex coloring problem, an $NP$-hard problem with relevance in both theoretical analysis and practical application. To recognize limitations in the applicability of local search of the vertex coloring problem, we analyze local search landscapes on differently-structured bipartite graphs. We identify structures that ensure only global optima can exist as well as ones that enable...

---

### 47. Quantitative Performance Analysis of Stopping Criteria for CMA-ES

**Authors:** Ryoji Tanabe

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09220v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09220v1)

**Summary:** Covariance matrix adaptation evolution strategy (CMA-ES) is a state-of-the-art black-box optimization algorithm. In general, CMA-ES uses a portfolio of multiple stopping criteria to automatically determine when to stop the search. This mechanism aims to avoid unnecessary consumption of the function evaluation budget during stagnation. Stopping criteria play an important role in CMA-ES, particularly when restart strategies are employed. However, the effectiveness of stopping criteria in CMA-ES re...

---

### 48. OpenOpt: An Open-Source SRAM Optimizer Based on Equivalent Circuit Model

**Authors:** Yikai Wang, Yiheng Wu, Can Wang, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09129v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09129v1)

**Summary:** This paper proposes a co-optimization framework that jointly optimizes SRAM architecture and transistor sizing using equivalent circuit models. The framework simplifies inactive SRAM cells into equivalent RC loads and static power models, achieving up to 61.4$\times$ simulation speedup while maintaining high fidelity (read/write delay error $<$0.22%, power error $<$1.68%). A joint search space encompassing architecture parameters and device sizing integrates seven algorithms including SA, PSO, B...

---

### 49. Quantitative Promise Theory: Intentionality and Inference in Autonomous Agents

**Authors:** Mark Burgess

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08552v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08552v1)

**Summary:** I discuss some quantitative representations of Promise Theory for processes involving autonomous agents. Agent models are common in software systems, machine learning, and biology, for example, but may also apply to physics and other forms of engineering. I describe how Bayesian probability and information theoretic optimization, including Active Inference, may be incorporated with promise semantics -- as well as how Promise Theory supplements solutions, helping to avoid probability's pitfalls, ...

---

### 50. Gray-Box Optimization and the Vertex Coloring Problem

**Authors:** Johanna Gasse, Antonia Heinen, Hendrik Higl, et al.

**Published:** 2026-06-06

🔗 [Paper](http://arxiv.org/abs/2606.08128v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08128v1)

**Summary:** Gray-box optimization is an approach for making some problem-specific information available to the algorithm while still relying on fitness information as the main guide to an optimum. This approach was shown to be beneficial in various combinatorial optimization tasks and neatly captures the continuum between fully black-box algorithms and tailored algorithms.   In this work, we discuss different flavors of gray-box algorithms. We show that RLS can find a proper $2$-coloring in a bipartite grap...

---

## q-bio.NC

**50 papers**

### 1. Adaptive inference and function vectors in deep transformers

**Authors:** Ravin Raj, Gautam Reddy

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16694v1)

**Summary:** Transformers are widely used as a general-purpose substrate for learning complex correlations between a large collection of coupled variables, but their internal mechanisms have remained mysterious. We introduce a theory of a deep transformer as a mean-field interacting system that implements distributed inference, subject to constraints on communication, locality and depth. We show that such a system can exploit internal state representations ('function vectors') to infer a latent context varia...

---

### 2. Learning Hybrid Biophysical Neuron Models with Neural ODEs

**Authors:** Jonas Beck, Michael Deistler, Dóra Viktória Molnár, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16693v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16693v1)

**Summary:** Biophysical neuron models link measurements of neural activity to underlying cellular mechanisms. Yet, a central challenge is that the kinetics of many ion channels are poorly characterized, and practical simplifications -- omitting channels or reducing morphological detail -- introduce systematic gaps between model and biology. Bridging these gaps requires approaches that can flexibly discover unmodeled dynamics while preserving mechanistic interpretability. Here, we introduce a hybrid modeling...

---

### 3. Infant Spontaneous Movement Noise Improves Exploration in Deep RL

**Authors:** Francisco M. López, Markus R. Ernst, Francisco Cruz, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16590v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16590v1)

**Summary:** Exploration in deep reinforcement learning (RL) is commonly implemented as temporally uncorrelated white noise. However, recent works show that temporally correlated colored noise can improve exploration efficiency by producing smooth trajectories with better coverage of the state space. We inquire whether action noise inspired by infant spontaneous movements can also improve exploration in deep RL. We find that the power spectral densities of babies' end-effector velocities follow a colored noi...

---

### 4. Sex-based Network-Specific Differences in Connectomes: A Krakencoder-Based Analysis

**Authors:** Vibhashree S H, Debanjali Bhattacharya, Vamshi Krishna Kancharla, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16294v1)

**Summary:** This study examines how deficiencies in one brain connectome modality propagate to the other, using the Krakencoder as a simulation framework. Structural and functional connectomes from 702 healthy participants in the Human Connectome Project were analyzed, with the impact of each of the Yeo-7 functional networks assessed separately. Seven scenarios were considered, each involving the removal of a single network while the remaining networks were preserved. The resulting perturbations in cross-mo...

---

### 5. EEGDash: An open-source platform for machine learning on public neurophysiological data

**Authors:** Bruno Aristimunha, Aviv Dotan, Pierre Guetschel, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.16041v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16041v1)

**Summary:** Public neurophysiological datasets are increasingly accessible but remain hard to reuse: turning one into a trained model still takes thousands of lines of code for download, loading, format repair, windowing, and evaluation, and a dataset that meets metadata standards can still fail to load. EEG-Dash is a software resource that catalogues 791 publicly archived recordings (39,778 participants, over 86,051 hours) spanning electroencephalography (EEG), magnetoencephalography (MEG), intracranial EE...

---

### 6. Task-guided cross-subject latent alignment: a multi-encoder-decoder VAE

**Authors:** Angeliki Papathanasiou, Jascha Achterberg, Thomas E. Nichols, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15989v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15989v1)

**Summary:** Aligning neural activity across subjects offers the promise of discovering shared computational principles and generalizable decoders. However, traditional alignment methods require shared stimuli across subjects, a constraint that limits applicability to naturalistic paradigms with limited or non-overlapping data. We introduce a Multi-Encoder-Decoder Variational Autoencoder (MED-VAE) that achieves cross-subject alignment without shared stimuli by anchoring representations to a common scaffold p...

---

### 7. Intrinsic Computational Functionalism and Simulated Consciousness

**Authors:** Ryota Kanai, Shuqin Ma

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15348v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15348v1)

**Summary:** A common objection to artificial or simulated consciousness is that a simulated brain is no more conscious than simulated water is wet. We address this from the perspective of Intrinsic Computational Functionalism (ICF): if consciousness is computationally constituted, it depends not on externally imposed descriptions but on the computational structures a system physically realizes in virtue of its own causal-dynamical organization. In previous work we developed Canonical Functionalism as a math...

---

### 8. OpTI-Mouse: Optimization for Targeted Temporal Interference Stimulation in the Mouse Brain

**Authors:** Jingsheng Tang, Zhengkang Zhou, Yingyue Xin, et al.

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15192v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15192v1)

**Summary:** Temporal Interference (TI) stimulation enables deep brain targeting, yet precise optimization tools for mouse models remain limited. We developed a computational optimization tool integrating mouse head modeling with the optimization algorithm to optimize stimulation strategies for predefined target regions. By balancing target intensity and spatial focality, the optimized strategy significantly outperformed empirical baselines. For the CA3-CA1 target, it achieved a 7-fold intensity increase (10...

---

### 9. Harnessing cortical geometry, wiring, and function as inductive biases for recurrent neural networks

**Authors:** Mo Shakiba, Rana Rokni, Mohammad Mohammadi, et al.

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14975v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14975v1)

**Summary:** How the wiring and functional organization of cortex shape recurrent computation remains a central question in both neuroscience and machine learning. Here, we leverage data released through the Machine Intelligence from Cortical Networks (MICrONS) program--a functional connectomics resource spanning multiple areas of mouse visual cortex, in which dense calcium imaging is co-registered with high-resolution electron microscopy reconstruction from the same animal--to build biologically grounded re...

---

### 10. Implications of hierarchical Markov models of behavior: on irreversibility, predictability, and dimensionality

**Authors:** John J. Vastola, Kanaka Rajan

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14692v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14692v1)

**Summary:** The maturation of quantitative tools for studying the high-level structure of animal behavior, and especially tools which represent spontaneous behavior as a sequence of stereotyped and neurally well-defined 'syllables', demands that the field revisit a fundamental theoretical question: if the coarse structure of behavior can be accurately described by Markov models, what do these models really tell us about behavior? In this work, we explore the theoretical implications of these models and disc...

---

### 11. Prospective Coding and Path Integration Emerge as Equilibrium Solutions of Self-Organizing Neural Networks with Firing-Rate Adaptation

**Authors:** Facundo Emina, Emilio Kropff

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14649v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14649v1)

**Summary:** Continuous Attractor Neural Networks (CANNs) traditionally rely on pre-wired recurrent connectivity to model spatial representations, path integration, and anticipatory dynamics. However, the biological mechanisms through which this structured connectivity emerges via learning remain relatively unexplored. This work presents a theoretical framework revealing how continuous attractor connectivity and its computational properties self-organize through Hebbian plasticity, firing-rate adaptation, an...

---

### 12. Decoding Semantic Categories from Picture-Naming EEG

**Authors:** Wei Hu, Binbin Xu

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14614v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14614v1)

**Summary:** Picture naming requires the transformation of visual object information into a spoken lexical response through perceptual, semantic, lexical, and articulatory processes. This study asked whether semantic-category information is recoverable from high-density EEG during overt picture naming. Sixteen native French-speaking participants performed a picture-naming task using line drawings. Picture labels were embedded with a multilingual text-embedding model and organized into nine interpretable sema...

---

### 13. Neural Variability Enhances Artificial Network Robustness

**Authors:** Robin Preble, Praveen Venkatesh, Stefan Mihalas, et al.

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13801v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13801v1)

**Summary:** Neural responses in cortex exhibit substantial trial-to-trial variability in response to repeated stimuli, while peripheral sensory neurons respond far more consistently, leading many to wonder whether stochasticity may carry meaning. Existing work has argued that noise and signal correlations may be optimized for discrimination in animals, whereas artificial neural network (ANN) studies have shown similar benefits of noise in machine learning tasks, although most ANN work has neglected the effe...

---

### 14. Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning

**Authors:** Paolo Muratore, Mackenzie Weygandt Mathis

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13260v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13260v1)

**Summary:** Identifying latent dynamical systems from noisy, high-dimensional measurements is a central problem at the intersection of representation learning, system identification, and scientific discovery. We present DYSCO, a multi-view temporal contrastive learning algorithm that jointly recovers latent trajectories and the governing dynamics from such observations, by leveraging multiple independent noisy views of the same underlying process to disentangle signal from noise. By parameterizing the dynam...

---

### 15. Including the Cost of Irreducible Uncertainty in the Policy Compression Framework

**Authors:** Álvaro Garrido-Pérez, Pieter Simoens, Amrapali Pednekar, et al.

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13132v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13132v1)

**Summary:** AI decision-support systems can benefit from anticipating biases in human decision-making. Many such biases may arise from human cognitive limitations. The policy compression framework models decision-making as a trade-off between reward maximization and the cognitive cost of encoding state-dependent action policies, formalized as the mutual information between states and actions (policy complexity). We argue that this account is incomplete because it treats conditional entropy--the irreducible ...

---

### 16. Deep Sleep Classification via EEG Signal Criticality: A Passive BCI Approach for Sleep-Improvement Neurofeedback

**Authors:** Stanisław Narębski, Tomasz Komendziński, Tomasz M. Rutkowski

**Published:** 2026-06-11

🔗 [Paper](http://arxiv.org/abs/2606.13017v1) | 📄 [PDF](https://arxiv.org/pdf/2606.13017v1)

**Summary:** Automated sleep staging is a fundamental application of passive Brain-Computer Interfaces (pBCI), decoding spontaneous neural states to enable closed-loop interventions independent of user intent. This study evaluates criticality features derived from Detrended Fluctuation Analysis (DFA) for the specific identification of deep sleep (N3).   We analyzed $347,232$ EEG epochs from $290$ older women using UMAP manifold learning to visualize state transitions. Subsequently, six classifiers were bench...

---

### 17. Phase model analysis of the effect of M-current on neural synchrony in hippocampal networks

**Authors:** Megha Manoj, Sue Ann Campbell

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.12684v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12684v1)

**Summary:** Neural assemblies, transiently coordinated groups of neurons, observed in the hippocampus are thought to underlie the formation of episodic memories. Acetylcholine (ACh), a neuromodulator, that is received by the hippocampus, plays a critical role in memory and learning. A well supported hypothesis suggests that high levels of ACh during active exploration and rapid eye movement (REM) sleep promote memory encoding, while low levels during quiet waking and slow-wave sleep (SWS) support memory con...

---

### 18. Multifractal human signals at the edge of life reveal a heart-brain anti-correlation

**Authors:** Yago Emanoel Ramos, Maria Eloá do Ó, Henrique Ferraz de Arruda, et al.

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.12600v1) | 📄 [PDF](https://arxiv.org/pdf/2606.12600v1)

**Summary:** This study investigates the terminal breakdown of human neurophysiological function through the lens of non-linear dynamics by analyzing the multifractal spectrum. Using Multifractal Detrended Fluctuation Analysis (MF-DFA), we quantify the temporal evolution of complexity in synchronized electroencephalogram (EEG) and electrocardiogram (ECG) time series from patients in the terminal stage. Our results reveal a marked divergence in multifractal spectrum width: while neural activity exhibits a col...

---

### 19. Beyond representational alignment with brain-guided language models for robust reasoning

**Authors:** Mingqing Xiao, Kai Du, Zhouchen Lin

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.11893v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11893v1)

**Summary:** The correspondence between large language models (LLMs) and the neural mechanisms underlying human higher-order cognition remains insufficiently characterized. Given that language and reasoning in the human brain appear dissociable, an open question is whether LLMs align with neural signals from reasoning-related regions and whether such signals can improve them. Here, focusing on deductive reasoning, we show that LLM internal representations are not only partially aligned with task-fMRI activit...

---

### 20. Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

**Authors:** Sam Gijsen, Michał Łukomski, Marc-André Schulz, et al.

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.11833v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11833v1)

**Summary:** Flow matching and diffusion models enable conditional generation across domains ranging from images to proteins, with recent extensions to out-of-distribution contexts. Yet generative models of neural time series have largely remained restricted to categorical conditioning, precluding compositional and zero-shot generalization. In this work, we propose a per-timestep conditioned diffusion transformer for generating realistic fMRI brain dynamics during unseen cognitive tasks by injecting both com...

---

### 21. Large language models selectively converge with human-shared neural semantic representations

**Authors:** Chen Hong, Ximing Shao, Gangyi Feng

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.11598v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11598v1)

**Summary:** Interpersonal communication requires building shared semantics that enable listeners to understand speakers' meanings from their unfolding language, but the dimensional structure of this shared neural representation remains unclear. LLMs increasingly approximate human language capability and neural responses, raising the question of whether they capture the same semantic structure shared between human brains. Here, we combined storytelling-listening pseudo-hyperscanning MEG with dimension-resolv...

---

### 22. End-to-End Machine Learning for Depressive State Classification via EEG and fNIRS

**Authors:** Riki Sakurai, Simon Kojima, Mihoko Otake-Matsuura, et al.

**Published:** 2026-06-10

🔗 [Paper](http://arxiv.org/abs/2606.11555v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11555v1)

**Summary:** The escalating demand for mental healthcare, driven by rising societal stress, highlights the limitations of traditional psychiatric diagnostics. Conventional methods - relying primarily on clinical interviews and patient self-reports - are inherently vulnerable to subjective bias and the varying empirical judgment of practitioners. To address the need for quantitative evaluation, biological signal-based detection, including electroencephalography (EEG) and functional near-infrared spectroscopy ...

---

### 23. FlexiBrain: Resolution-Agnostic Voxel-Level Encoding for Native fMRI

**Authors:** Mo Wang, Wenhao Ye, Junfeng Xia, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11500v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11500v1)

**Summary:** The success of large-scale deep learning models in neuroscience is fundamentally constrained by severe data heterogeneity. Native fMRI data aggregated from diverse sources exhibit substantial variation in both spatial and temporal resolutions. Consequently, most existing frameworks rely on lengthy, rigid preprocessing pipelines that enforce uniformity across datasets. This practice introduces two critical limitations: (1) potential degradation of subject-specific anatomical information; (2) sign...

---

### 24. Spatially Masked Regression Reveals Local and Distributed Predictability in Electrophysiological Recordings

**Authors:** Maryam Ostadsharif Memar, Nima Dehghani

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11415v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11415v1)

**Summary:** Neural recordings are often interpreted as local measurements, yet the signal at any one sensor can also reflect structured activity distributed across the broader network. This raises a basic question: to what extent does an electrode's signal reflect local versus distributed information in the underlying system? More specifically, how much of an electrode's activity is carried by its immediate neighborhood, and how much is embedded more broadly across the array? We address this with a Spatiall...

---

### 25. QUIET: Quantifying Underutilized Influential Edges for Targeted Synchronization

**Authors:** Sovesh Mohapatra, Christoffer G. Alexandersen, Panagiotis Fotiadis, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11091v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11091v1)

**Summary:** Network control theory can be used to model intrinsic and extrinsic strategies to steer neural dynamics. Standard approaches are node-centric, structural, and focused on achieving desired instantaneous states. Here, we develop an edge-centric approach which incorporates both structure and function to achieve extended patterns of neural dynamics characterized by desired synchronization states. Our method, Quantifying Underutilized Influential Edges for Targeted Synchronization (QUIET), is an edge...

---

### 26. GRAFT: Gain-Recalibrated Adapters for Transformer-Based Neural Population Activity Modeling

**Authors:** Xiangsheng Ge, Yang Xie

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11066v1)

**Summary:** Neural population activity models can recover rich temporal structure from binned spikes, but their read-in and readout layers often remain tied to a fixed set of recorded neurons. This coupling limits reuse in long-term brain-computer interfaces, where recorded neuron identities, counts, and response statistics can change across days. We introduce GRAFT, a Transformer-based neural population activity model that separates reusable temporal dynamics from a recalibratable neuron interface. The neu...

---

### 27. Bilinear gating of motor primitives: a principle linking dendritic computation to rapid goal-directed adaptation

**Authors:** Cristiano Capone, Luca Falorsi, Andrea Ciardiello, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10891v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10891v1)

**Summary:** Movement requires the motor cortex to specify both \emph{what} action to produce and \emph{which goal} it serves, yet how individual neurons separate these factors is not understood. Here we show that in macaque motor cortex the \emph{burst fraction} of a neuron, the proportion of its spikes emitted in high-frequency bursts, encodes reach direction far more selectively than its overall firing rate. This dissociation is highly consistent: it holds in every one of 12 recording sessions spanning th...

---

### 28. Sleep EEG Signal Criticality as a Non-Invasive Predictor of Cognitive Decline in Dementia

**Authors:** Stanisław Narębski, Tomasz Komendziński, Tomasz M. Rutkowski

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10889v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10889v1)

**Summary:** Early detection of neurodegeneration remains a critical clinical challenge. This study investigates whether sleep EEG signal criticality, quantified via Multifractal Detrended Fluctuation Analysis (MFDFA), serves as a non-invasive biomarker for future cognitive decline. We analyzed longitudinal data from the National Sleep Research Resource (NSRR) Study of Osteoporotic Fractures (SOF) cohort, comparing baseline sleep EEG dynamics between women who remained cognitively normal and those who later ...

---

### 29. Hyperbolic Neural Population Geometry Benefits Computation

**Authors:** Dennis Wu, Yi-Chun Hung, Braden Yuille, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10238v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10238v1)

**Summary:** Neural population geometry shapes downstream computation. Recent empirical findings in neurobiology suggest that a hyperbolic structure underlies population activity in the hippocampus. Here we provide a theoretical framework for this phenomenon. First, we propose a plausible construction of hippocampal tuning curves that statistically induces hyperbolic geometry. Next, we establish a connection between neural decoding and associative memory by demonstrating that the Modern Hopfield Network upda...

---

### 30. Multifractal Signatures of Ageing and Dementia Development: A Multifractal Space-Filling Curve Analysis

**Authors:** Marta Lotka, Jacek Grela, Zbigniew Drogosz, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10222v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10222v1)

**Summary:** Multifractality is an effective formalism for quantifying the nonlinear, scale-free properties of complex data. In this study, we propose a novel and efficient methodology, termed Multifractal Space-filling Curve Analysis (MFSCA), for quantifying the correlation structure of multidimensional data. Within this framework, the original multidimensional data - while preserving both local and long-range organisational properties - are projected onto a one-dimensional representation using a fractal sp...

---

### 31. Discovering Functionally Selective Brain Regions with a Deep Topographic Multimodal Model

**Authors:** Badr AlKhamissi, Johannes Mehrer, Lara Marinov, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09770v1)

**Summary:** Nearby neurons in cortex share similar response profiles, producing systematic spatial organization across sensory and cognitive systems. Recent topographic models reproduce aspects of this structure but remain unimodal and spatially constrain each layer separately, yielding fragmented maps that capture neither the contiguity of cortical processing streams nor their integration across modalities. We introduce Topo-Omni, a topographic multimodal model in which visual, auditory, and language/cogni...

---

### 32. Predictable Mean-Field Chaos in Random Recurrent Networks

**Authors:** Alkesh Yadav, Vladimir Shaidurov, Jonathan Kadmon

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08805v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08805v1)

**Summary:** Dynamical mean-field theory recasts deterministic chaos in random recurrent networks as an effective stochastic process. We show that for analytic nonlinearities with sufficiently fast Fourier decay, this stochasticity is only apparent: the continuous past of a realized mean-field trajectory uniquely determines its future. The mean-field theory is therefore not merely an ensemble description, but a conditional prediction theory for individual trajectories. Unfolding the power spectrum into a Kry...

---

### 33. This is how the Neocortex Learns

**Authors:** Randall C. O'Reilly

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08720v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08720v1)

**Summary:** A sufficient account of how the neocortex learns must meet three criteria: 1. Computationally, it must approximate a powerful, general-purpose learning algorithm known to scale to human-level intelligence; 2. Algorithmically, it must be implementable using known, well-established neural circuits within the neocortex and associated brain structures; 3. Implementationally, there must be a detailed account for how all of the algorithmic mechanisms actually function at a neurochemical level. At pres...

---

### 34. Vector Space of Cycles

**Authors:** Moo K. Chung, Anass B. El-Yaagoubi, Hernando Ombao

**Published:** 2026-06-06

🔗 [Paper](http://arxiv.org/abs/2606.08202v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08202v1)

**Summary:** Most statistical and machine learning methods for directed interactions focus on pairwise effects among variables. Even existing cyclic models represent feedback primarily through node-level dependencies, making large-scale recurrent organization difficult to estimate and compare. This limitation is particularly acute in biological and neural systems, where interactions are highly recurrent and involve many overlapping cycles. We introduce a variational framework for statistical inference on cyc...

---

### 35. Reconstructing and forecasting disease trajectories of patients with Alzheimer's disease using routine data in resource-constrained settings

**Authors:** Ratnadeep Das, Atri Chatterjee, Sitikantha Roy

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07798v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07798v1)

**Summary:** Alzheimer's disease is a progressive neurodegenerative disorder, and its progression varies substantially across patients. Existing work aims to forecast patients' future cognitive state, with minimal focus on reconstructing the state from past visits. Furthermore, in current research, quantifying predictive uncertainty remains underexplored and relies on costly modalities such as MRI, PET, and CSF, limiting their deployment in resource-limited settings. In this research, our primary objectives ...

---

### 36. Position: Hippocampal Explicit Memory Is the Cornerstone for AGI

**Authors:** Sangjun Park

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.11245v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11245v1)

**Summary:** Large Language Models (LLMs) have demonstrated remarkable capabilities across various tasks, raising expectations for Artificial General Intelligence (AGI). This position paper argues that integrating explicit memory is the cornerstone for advancing LLMs toward AGI. The key reason is that the underlying learning mechanism of LLMs is highly analogous to human implicit memory. However, higher-order cognitive functions necessary for AGI, such as long-term strategic planning, metacognition, and symb...

---

### 37. Fixed point compositionality via low-rank gluing rules in inhibition-dominated threshold-linear networks

**Authors:** Juliana Londono Alvarez

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07336v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07336v1)

**Summary:** Brains routinely generate highly flexible and complex behaviors on a relatively stable structure and limited resources. A key mechanism underlying this ability is compositionality, which allows the brain to efficiently decompose complex tasks into simpler, reusable primitives. While network modularity has often been linked to compositionality in biological and artificial networks, a rigorous mathematical characterization of this relationship in nonlinear networks is still lacking. In this work, ...

---

### 38. The Identity Trap in EEG Foundation Models: A Diagnostic Audit

**Authors:** Jun-You Lin, Ying Choon Wu, Tzyy-Ping Jung

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06647v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06647v1)

**Summary:** Objective. EEG foundation models (FMs) report strong accuracy on clinical resting-state EEG. However, high accuracy under subject-disjoint cross-validation remains ambiguous: it can reflect a genuine clinical biomarker, or subject-identity features that correlate with the label. We name this the Identity Trap and ask whether it can be diagnosed at the representation level before fine-tuning.   Approach. We propose FMScope, a frozen-representation protocol packaging five diagnostics: variance dec...

---

### 39. Simultaneous hyperkinetic movement disorders phenotyping: a cross-cohort pediatric transfer study using routine videos, markerless pose estimation and a tabular foundation model

**Authors:** Laura Cif, Diane Demailly, Zohra Souei, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.07674v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07674v1)

**Summary:** Objective: To develop and externally test a video-based framework for simultaneous detection of hyperkinetic MDs phenomenologies: dystonia, tremor, myoclonus, chorea, athetosis, ballismus, stereotypies, and tics using routine clinical recordings, with explicit testing of external, cross-cohort transfer from adult to pediatric populations. Methods: In this proof-of-concept study, the framework combines markerless pose estimation, kinematic descriptors, and a pretrained fondation model. A shared p...

---

### 40. Intrinsic Computational Functionalism: From Observer-Relative Maps to Observer-Independent Structures

**Authors:** Shuqin Ma, Ryota Kanai

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06424v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06424v1)

**Summary:** Anti-computational arguments show that externally imposed computational interpretations cannot ground consciousness, but they do not establish that all computational organisations are observer-relative. We develop intrinsic computational functionalism: the view that, if consciousness is computationally constituted, it depends on physically realised computational structures the system has in virtue of itself rather than on labels imposed by an external interpreter. Two criteria operationalise thi...

---

### 41. Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation

**Authors:** Yohann Benchetrit, Marlène Careil, Simon Dahan, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06345v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06345v1)

**Summary:** Brain decoding is limited by the availability of labeled neural data, and remains challenging in low-data regimes. To address this issue, we investigate whether and when brain decoding can be boosted by augmenting small fMRI datasets with synthetic data generated by a pretrained model of fMRI responses to stimuli. We use TRIBE v2, a large encoding model pretrained on more than 1000 hours of fMRI responses to video, audio and language. For each dataset, we evaluate systematic grids that show how ...

---

### 42. Early psychosis shows deviations in scaling behaviour within a critical regime

**Authors:** Irem Topal, Paola Moreno Ancalmo, Guillermo Montana Valverde, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06290v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06290v1)

**Summary:** Accumulating evidence suggests that large-scale brain activity exhibits scale-invariant dynamics consistent with operation in a near-critical regime. Such dynamics have been associated with long-range correlations, efficient information processing, and the emergence of collective organization. While altered criticality-related measures have been reported in psychiatric disorders, previous findings remain fragmented across observables and modalities, making it unclear whether different scaling me...

---

### 43. Cross-scale spatially-aware generative modeling of transcriptomic programs underlying neurodegenerative brain organization

**Authors:** Krishnakumar Vaithianathan

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05870v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05870v1)

**Summary:** Neurodegenerative disorders such as Alzheimer's disease exhibit highly organized patterns of regional brain vulnerability, yet the biological mechanisms underlying this spatial selectivity remain incompletely understood. Existing imaging-transcriptomic studies have largely relied on correlation-based analyses between gene expression and neuroimaging phenotypes, limiting their ability to model how molecular organization gives rise to neurodegeneration. Here, we introduce a cross-scale spatially-a...

---

### 44. Discrete signaling mediates chaotic regularization in recurrent neural networks

**Authors:** Jan Bauer, Christian Keup, Jonathan Kadmon, et al.

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04426v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04426v1)

**Summary:** Cortical circuits operate in a regime of intrinsic chaos, where even tiny changes in input can lead to divergent neural responses. Yet, remarkably, population codes in the brain vary smoothly with sensory stimuli, forming coherent representational manifolds. How can chaotic networks sustain such stable coding? Here, we develop a theoretical framework that links the microscopic chaos of recurrent networks to the macroscopic geometry of neural representations. Combining kernel methods with dynamic...

---

### 45. Do Large Language Models Have Emotions?

**Authors:** Amit Goldenberg, James J. Gross

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.14742v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14742v1)

**Summary:** Do LLMs have emotions? A recent paper from Anthropic reports finding internal representations of emotion concepts in Claude Sonnet 4.5, concluding that the LLM has 'functional emotions.' We evaluate this claim against what is known about how emotions actually function in biological systems. We argue that emotions serve two core functions: the context-sensitive interpretation of situations, and the reorganization of processing across multiple systems in response to those interpretations. The Anth...

---

### 46. Formalizing the Binding Problem

**Authors:** Lianghuan Huang, Yihao Li, Saeed Salehi, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03976v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03976v1)

**Summary:** Representations of the world, arguably, contain information about features (e.g. something is blue, something is a circle) but also information about which features are part of the same object (e.g. the circle is blue), which we call binding information. Any system with the ability to understand scenes with multiple objects must be able to solve the binding problem: it needs to know which features belong together. However, despite work showing that Vision Transformers (ViTs) know which patches b...

---

### 47. Who Is in Mind Matters: Attachment Representations in Early Childhood Synchronize Child-Adult Interacting Brains

**Authors:** Ruxin Su, Jiayang Xu, Saishuang Wu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03700v1)

**Summary:** Human attachment is distinguished by enduring internalized representations that shapes neurodevelopment and social-emotional functioning. However, as unobservable inner processes mixed with social cues and partner-specific factors, the neurocognitive mechanisms of these representations during real-time interaction remain unclear. Using a novel Remote Partner-Belief Manipulation paradigm in 40 child-mother-stranger trios, we experimentally isolated attachment representations in 3-4-year-olds by m...

---

### 48. SC-TauPath: A Structural Connectivity Attribution Framework for Mapping Tau Propagation Pathways in Alzheimer's Disease

**Authors:** Jing Zhang, Norman Scheel, Minheng Chen, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.04066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04066v1)

**Summary:** Understanding how structural connections are associated with tau propagation in Alzheimer's disease (AD) remains a central open question, yet existing computational models either rely heavily on biophysical assumptions or lack neurobiologically interpretable pathway maps. We present SC-TauPath, a structural connectivity (SC) attribution framework that maps tau propagation pathways from in vivo neuroimaging data. SC-TauPath combines a Network Diffusion Model (NDM)-augmented multilayer perceptron ...

---

### 49. Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics in a PFC-Inspired Reservoir Model for Multistep Goal-Directed Action Planning

**Authors:** Jin Nakamura, Yuichi Katori

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03481v1)

**Summary:** The prefrontal cortex (PFC) maintains goal information for action planning, but how recurrent circuits preserve it in an action-usable form over behavioral timescales remains unclear. Here we ask whether short-term synaptic plasticity (STP) can stabilize goal information as action-usable, goal-conditioned dynamics. We incorporated STP into a PFC-inspired reservoir computing model with basal-ganglia-inspired temporal-difference readout learning, and evaluated paired models with and without STP ac...

---

### 50. A formal definition and meta-model for a machine theory of mind

**Authors:** Fabio Cuzzolin

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03471v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03471v1)

**Summary:** This paper proposes, for the first time, a rigorous formal definition of the concept of Machine Theory of Mind, based on principles supported by evidence from cognitive psychology, neuroscience and artificial intelligence, and uses the above as a lens to examine state-of-the-art and current efforts in the field, driving a potential agenda for further research there able to "crack" the problem. It also advances a general holistic meta-model for Machine Theory of Mind, and examines the state of th...

---

## stat.ML

**50 papers**

### 1. Exact Posterior Score Estimation for Solving Linear Inverse Problems

**Authors:** Abbas Mammadov, Ozgur Kara, Kaan Oktay, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17048v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17048v1)

**Summary:** Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the posterior, but the score that the prior provides is the unconditional score, not the posterior score. Existing methods either steer a fixed pretrained denoiser with approximate measurement-matching corrections, or train a conditional restoration model that abandons the denoising structure of the prior. ...

---

### 2. Learning the Geometry of Data: A Mathematical Review of Shape Space Analysis

**Authors:** Gary P. T. Choi, Khanh Dao Duc, Shira Faigenbaum-Golovin, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17022v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17022v1)

**Summary:** A central objective of machine learning is to identify structure and patterns in data. Advances in data acquisition have increasingly produced datasets whose observations possess rich geometric form, giving rise to shape spaces that encode variability in object geometry. Such datasets arise across a wide range of disciplines, including biology, medicine, anthropology, and computer vision, where subtle geometric differences often carry important scientific information. Traditional machine learnin...

---

### 3. Filtered Conformal Ellipsoids for Graph-Native Time Series

**Authors:** Yannick Limmer

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.17014v1) | 📄 [PDF](https://arxiv.org/pdf/2606.17014v1)

**Summary:** Joint prediction sets for multivariate time series should control a single event while adapting to cross-coordinate dependence. We study filtered conformal ellipsoids: a frozen state-space filter emits a one-step predictive mean and covariance, and split-conformal calibration is applied to the resulting Mahalanobis scores. The filter is used to choose the ellipsoid shape; conformal calibration chooses the scalar radius, so the construction benefits from a learned predictive covariance without re...

---

### 4. Dynestyx: A Probabilistic Programming Library for Dynamical Systems

**Authors:** Daniel Waxman, Dmitry Batenkov, John Feser, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16985v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16985v1)

**Summary:** State-space models (SSMs) are the standard formalism for Bayesian treatment of dynamical systems, with natural applications in statistics, signal processing, and machine learning. Despite their importance in both theory and application, dynamical systems have proven difficult to incorporate in modern probabilistic programming languages (PPLs), making state-of-the-art methods less accessible to practitioners and introducing friction in following the "Bayesian workflow." We introduce dynestyx, a p...

---

### 5. Sobolev Approximation by Fixed-Size Neural Networks with Arbitrary Accuracy

**Authors:** Baicheng Li, Haizhao Yang, Shijun Zhang

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16975v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16975v1)

**Summary:** In this work, we investigate new activation functions for achieving arbitrary-accuracy Sobolev approximation by fixed-size neural networks. We first show that any function in $W^{2,\infty}((a,b)^d)$ can be approximated with arbitrary accuracy, measured in the $W^{1,\infty}$-norm, by a fixed-size neural network using the Elementary Universal Activation Function ($\mathrm{EUAF}$). To extend this result to $W^{s,\infty}((a,b)^d)$ for $s\in\mathbb{N}$, we introduce a smooth activation $\mathrm{DUAF}...

---

### 6. Phantoms and Disclosures: a Causal Framework for Auditing Synthetic Data

**Authors:** Kareem Amin, Rudrajit Das, Alessandro Epasto, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16952v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16952v1)

**Summary:** The rapid adoption of generative AI and Large Language Models (LLMs) has spurred interest in synthetic data as a privacy-preserving alternative to sensitive real-world datasets. However, generating high-utility synthetic data often carries the risk of memorizing and regurgitating private information from the training corpus. In this work, we present a customizable empirical auditing framework designed to detect and explain such data disclosures. Our framework introduces a mechanism to distinguis...

---

### 7. A nonparametric two-sample test using a parametric integral probability metric

**Authors:** Yuha Park, Yongdai Kim

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16941v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16941v1)

**Summary:** Detecting distributional differences between two independent samples is a fundamental problem in statistics and machine learning. Nonparametric two-sample testing provides a principled framework for determining whether two samples are drawn from the same underlying distribution, without assuming any specific parametric form for the distribution. In this study, we propose a new two-sample test statistic based on a newly introduced integral probability metric (IPM), using a specially designed para...

---

### 8. Functional Gradient Descent with Adaptive Representations

**Authors:** Daniel Csillag, Rodrigo Schuller, Pedro Dall'Antonia, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16926v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16926v1)

**Summary:** Functional optimization problems are typically solved by optimizing the parameters of a fixed representation, such as a neural network, resulting in highly nonconvex losses that complicate both training and theoretical analysis. An interesting alternative is functional gradient descent (FGD), that is, gradient descent directly in function space, which benefits from strong convergence results and admits a clean theory. However, FGD is difficult to implement in practice because functional gradient...

---

### 9. MA-SBI: Misspecification-Aware Simulation-Based Inference via Side-Channel Guidance

**Authors:** Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R., et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16923v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16923v1)

**Summary:** Simulation-based inference (SBI) of latent parameters is often hindered by simulator misspecification, the mismatch between simulated and real-world observations caused by inherent modeling simplifications. RoPE, the recent state-of-the-art for robust SBI, addresses this through optimal transport between learned representations of real and simulated observations, but requires ground-truth parameter calibration pairs that are typically unavailable in the very settings where SBI is needed. What pr...

---

### 10. Optimal Multiscale Learning of Linear Operators

**Authors:** Jiaheng Chen, Daniel Sanz-Alonso

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16913v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16913v1)

**Summary:** We study the statistical and computational limits of learning bounded linear operators between Sobolev spaces from noisy input-output data. In wavelet coordinates, the problem is recast as an infinite-dimensional matrix regression problem with a heterogeneous two-sided multiscale structure. We establish minimax rates under Sobolev operator-norm loss and construct a finite-resolution blockwise least-squares estimator attaining these rates. The analysis reveals a nonuniform local estimation diffic...

---

### 11. Generative Predictive Distributions for Time Series

**Authors:** Jordi Llorens-Terrazas, Mika Meitz

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16773v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16773v1)

**Summary:** We propose a flexible framework for modeling the predictive distributions of nonlinear, possibly multivariate time series. Our approach expresses a general predictive distribution in an appropriate generative representation that is based on a folklore result from measure theoretic probability. This representation provides a direct simulation-based approximation to the predictive distribution, enabling straightforward computation of forecasts for the conditional mean and variance, fan charts, val...

---

### 12. Attention is Just Another Name for Coupling?: A Fast-Slow ODE Perspective on Hierarchical Pretraining

**Authors:** Zhengyuan Gao

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16730v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16730v1)

**Summary:** Causal self-attention is a coupling mechanism: each token's hidden state is updated by a learned mixture of preceding tokens at the same timescale. This paper asks whether a second, temporally slower coupling-a slow sub-system operating on a temporally-downsampled view of the sequence and fed back into the fast path through a zero-initialised gate-complements it. The question is framed in the language of singularly perturbed ordinary differential equations (ODEs), where the fast variable $x$ evo...

---

### 13. Spectral Sparsification of Laplacian-Constrained Gaussian and Hüsler-Reiss Graphical Models

**Authors:** Ignacio Echave-Sustaeta Rodríguez, Aida Abiad, Frank Röttger

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16681v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16681v1)

**Summary:** Graph Laplacians encode graph structures in matrix form, and thus facilitate the application of linear algebra to graph theory. In statistics, two related families of probabilistic graphical models can be parameterized by graph Laplacians. The first one is the Laplacian-constrained Gaussian graphical model (LCGGM), which imposes that the (pseudo-)inverse covariance matrix of a Gaussian random vector is a Laplacian matrix. Applications include graph signal processing and network topology learning...

---

### 14. Diffusion Flow Matching: Dimension-Improved KL Bounds and Wasserstein Guarantees

**Authors:** Marta Gentiloni Silveri, Giovanni Conforti, Alain Durmus

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16610v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16610v1)

**Summary:** Diffusion Flow Matching (DFM) has recently emerged as a versatile framework for generative modeling, yet its theoretical convergence properties remain only partially understood. In this work, we provide refined and novel convergence guarantees for Brownian motion based DFMs, focusing on the discretization error. Our analysis is conducted under the Kullback-Leibler (KL) divergence and the 2-Wasserstein distance. Under finite-moment conditions and a mild score integrability assumption, we derive K...

---

### 15. Neural Bayesian Anomaly Mitigation: A Robust Loss that Doubles as an Unsupervised Contamination Classifier

**Authors:** S. A. K. Leeney, W. J. Handley, H. T. J. Bevins, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16524v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16524v1)

**Summary:** Engineered robust losses such as Huber, Student-$t$, and generalised cross-entropy make supervised models tolerant of contamination but cannot answer which observations are corrupted. We introduce Neural Bayesian Anomaly Mitigation (NBAM), a general-purpose drop-in loss derived from a Bayesian latent-switch mixture model: the marginal likelihood defines a robust supervised loss, and the associated posterior defines an unsupervised contamination classifier. Like Huber or Student-$t$, NBAM can rep...

---

### 16. Scalable and Interpretable Representation Alignment with Ordinal Similarity

**Authors:** Diogo Soares, Pankhil Gawade, Andrea Dittadi, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16379v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16379v1)

**Summary:** Evaluating representation similarity is fundamental to representation learning. However, existing metrics suffer from significant limitations: they lack interpretability due to shifting baselines, lack robustness to outliers, and are computationally intractable for large datasets, forcing reliance on heuristic approximations. To address this, we develop an ordinal-similarity framework, instantiated by the Triplet (TSI) and Quadruplet (QSI) Similarity Indices, which measure alignment by quantifyi...

---

### 17. One-Step Generalization Ratio Guided Optimization for Domain Generalization

**Authors:** Sumin Cho, Dongwon Kim, Kwangsu Kim

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16301v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16301v1)

**Summary:** Domain Generalization (DG) aims to train models that generalize to unseen target domains but often overfit to domain-specific features, known as undesired correlations. Gradient-based DG methods typically guide gradients in a dominant direction but often inadvertently reinforce spurious correlations. Recent work has employed dropout to regularize overconfident parameters, but has not explicitly adjusted gradient alignment or ensured balanced parameter updates. We propose GENIE (Generalization-EN...

---

### 18. Generative Modeling on Metric Graphs via Neural Optimal Transport

**Authors:** Alessandro Micheli, Yueqi Cao, Anthea Monod, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16273v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16273v1)

**Summary:** We introduce, to our knowledge, the first deep generative modeling framework for probability distributions continuously supported on compact metric graphs. Given source and target measures on a metric graph, our method embeds the graph into a smooth ambient space, solves an entropic Kantorovich problem via a neural semidual parameterization, and projects generated samples back onto the original graph. We study two embedded geometries: an extrinsic Euclidean realization and the intrinsic tropical...

---

### 19. On the Geometry of Separation in Finite Gaussian Mixtures

**Authors:** Huy Nguyen, Dung Le, Alessandro Rinaldo, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16179v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16179v1)

**Summary:** We study an open problem of understanding the effects of the minimum component separation on the convergence rates of parameter estimation in finite Gaussian mixtures. We address this by developing a unified geometric framework based on novel Hellinger lower bounds that directly relate discrepancies between mixture densities directly to Wasserstein distances between their underlying mixing measures, with explicit dependence on both the minimum separation and the minimum weight. Our approach comb...

---

### 20. Closing the Approximation Gap in Simulation-free Latent SDEs

**Authors:** Henry D. Smith, Brian L. Trippe, Scott W. Linderman

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16138v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16138v1)

**Summary:** Recovering dynamical systems from noisy observations is a recurring challenge across scientific domains, including neuroscience and physics. Latent stochastic differential equations (SDEs) address this by modeling the system as an unobserved state that evolves according to a learnable SDE and generates the observations. Variational inference (VI) provides a tractable objective for fitting latent SDEs. Traditional VI algorithms evaluate this objective by numerical simulation over a time discretiz...

---

### 21. Stop the Sampler! Classifier-Based Adaptive Stopping for Sampling Kernels

**Authors:** Kirill Korolev, Nikita Morozov, Stepan Pavlenko, et al.

**Published:** 2026-06-15

🔗 [Paper](http://arxiv.org/abs/2606.16073v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16073v1)

**Summary:** Sampling from complex, unnormalized probability densities is a fundamental challenge in Bayesian inference and probabilistic modeling. While Markov chain Monte Carlo (MCMC) methods provide asymptotic guarantees, they often suffer from slow mixing and high computational costs due to fixed or manually tuned trajectory lengths. In this work, we propose a novel framework that treats trajectory termination as a learnable component of the sampling dynamics. By framing MCMC within the theory of non-acy...

---

### 22. The limits of interpretability in multiple linear regression

**Authors:** Anand Sharma, Chen Liu, Daniele Coslovich, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.16013v1) | 📄 [PDF](https://arxiv.org/pdf/2606.16013v1)

**Summary:** Interpreting machine-learning models has attracted increasing attention, particularly in the physical sciences, where one often seeks to understand the underlying mechanisms rather than merely make predictions. Multiple linear regression is often regarded as an interpretable alternative to more complex models, such as deep neural networks, because its predictions are expressed as explicit weighted sums of input features. However, when input features are strongly correlated, namely in the presenc...

---

### 23. PromptShift-CRC: Drift-Aware Conformal Risk Control for Foundation Models Under Prompt and Domain Shift

**Authors:** Jeffery Opoku, David Banahene

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15964v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15964v1)

**Summary:** Foundation models are now used in settings where the prompts they receive can change quickly. Users change, topics change, policies change, and the model may suddenly face a kind of request that was rare in the calibration data. This makes fixed calibration risky. Conformal prediction and conformal risk control give model-agnostic ways to control error, but they work best when the calibration data still look like the future data. This paper develops PromptShift CRC, a drift-aware conformal risk ...

---

### 24. Spectral Adaptive Conformal Prediction for Structured Non-Exchangeable Data

**Authors:** Jeffery Opoku, David Banahene

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15950v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15950v1)

**Summary:** Conformal prediction gives prediction intervals with finite-sample coverage when the data are exchangeable. Many time-indexed datasets are not exchangeable. They have seasons, recurring regimes, changing frequencies, or other forms of structured dependence. This paper studies a simple way to use that structure. We propose spectral adaptive conformal prediction, a method that forms weighted conformal quantiles using local spectral similarity and then updates the target miscoverage level online. T...

---

### 25. Topological Flow Matching

**Authors:** Kacper Wyrwal, İsmail İlkan Ceylan, Alexander Tong

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15897v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15897v1)

**Summary:** Flow matching is a powerful generative modeling framework, valued for its simplicity and strong empirical performance. However, its standard formulation treats signals on structured spaces, such as fMRI data on brain graphs, as points in Euclidean space, overlooking the rich topological features of their domains. To address this, we introduce topological flow matching, a topology-aware generalization of flow matching. We interpret flow matching as a framework for solving a degenerate Schrödinger...

---

### 26. Amortized mean-shift interacting particles

**Authors:** Ali Siahkoohi

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15871v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15871v1)

**Summary:** Bayesian inference for inverse problems is run to evaluate integrals -- posterior expectations, tail probabilities, and risks -- across a stream of observations. The standard estimate averages the integrand over posterior samples, a Monte-Carlo average whose error decays only as the square root of the sample size, so accuracy demands many samples -- prohibitive when each one calls a partial-differential-equation forward model. Mean-shift interacting particles need far fewer: they return a small ...

---

### 27. Learning a Sampling-Free Variational DNN Plugin from Tiny Training Sets to Refine OOD Segmentation With Uncertainty Estimation

**Authors:** Jimut B. Pal, Suyash P. Awate

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15837v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15837v1)

**Summary:** Deep neural networks (DNNs) frequently fail to generalize to out-of-distribution (OOD) medical images because of variations in scanners and acquisition protocols. Retraining DNN models to address these distribution shifts is often impractical due to the high cost of acquiring and annotating new medical datasets. To address this, we introduce VarDeepPCA, a novel lightweight variational DNN framework designed to restore/refine degraded segmentation maps by leveraging intrinsic geometric priors. Un...

---

### 28. Proximal Policy Optimization for Amortized Discrete Sampling

**Authors:** Anna Zykova-Myzina, Timofei Gritsaev, Daniil Tiapkin, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15793v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15793v1)

**Summary:** This paper explores policy gradient algorithms for training stochastic policies to sample from structured discrete probability distributions under the Generative Flow Network (GFlowNet) framework. Building on extensive theoretical connections between GFlowNets and entropy-regularized reinforcement learning, we derive equivalents of standard policy gradient algorithms for training GFlowNets, as well as experimentally explore their various methodological aspects, including baseline training and ad...

---

### 29. The Data Manifold under the Microscope

**Authors:** Marios Koulakis, Constantin Seibold

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15760v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15760v1)

**Summary:** A significant gap exists between theory and practice in deep learning. Generalization and approximation error bounds are often derived for simplified models or are too loose to be informative. Many rely on the manifold hypothesis and on geometric regularity such as intrinsic dimension, curvature, and reach. Progress requires insight into data-manifold geometry and suitable benchmarks, yet existing options are polarized: analytic manifolds with known geometry but limited applicability, or real-wo...

---

### 30. Score-Based Martingale Posteriors for Deep Neural Networks

**Authors:** Abylay Zhumekenov, Ajay Jasra, Mohamed Maama, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15725v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15725v1)

**Summary:** In this paper we investigate the efficacy of the score-based martingale posteriors (SMP) (Cui & Walker, 2025; Fong et al., 2023) in the context of modern and large-scale machine learning problems and its potential for meaningful uncertainty quantification. SMPs work with a stochastic gradient ascent-type recursion on the parameter space of stochastic models and construct a martingale on the parameter space. Under simple mathematical assumptions, the recursion can be built so that the parameters ...

---

### 31. Stochastic trace estimation with tensor train random vectors

**Authors:** Zvonimir Bujanović, Daniel Kressner, Hrvoje Olić

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15679v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15679v1)

**Summary:** Stochastic trace estimation is a standard tool for approximating the trace of a large-scale matrix available only through matrix-vector products. However, in tensor-structured settings, unstructured Gaussian or Rademacher test vectors may be prohibitively expensive to store and compute with, while cheaper rank-one tensor-product vectors can require sample complexities that grow exponentially with the tensor order. This work studies Gaussian random tensor train vectors as a structured alternative...

---

### 32. Information Gap and Feasibility-Aware Inference in Binomial Logistic Mixtures

**Authors:** Yuta Hayashida, Shonosuke Sugasawa

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15665v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15665v1)

**Summary:** This paper studies the information gap between mixture detection and label recovery in binomial logistic mixtures. Standard likelihood-based criteria such as the Bayesian information criterion (BIC) can detect the presence of two components, but this does not guarantee that the corresponding labels are recoverable. We show that this gap is intrinsic to binomial logistic mixtures with a fixed number of trials: observed-data evidence for mixture structure and per-observation information for label ...

---

### 33. Phase Transition in Convex Relaxations for Graph Alignment

**Authors:** Laurent Massoulié, Sushil Mahavir Varma, Louis Vassaux, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15581v1)

**Summary:** We study the graph alignment problem for correlated Gaussian Orthogonal Ensemble (GOE) matrices, where the goal is to recover a hidden vertex permutation given two correlated symmetric Gaussian matrices $(A, B)$ with correlation $1/\sqrt{1+σ^2}$. While the maximum likelihood estimator is information-theoretically optimal, its computation, which reduces to a quadratic assignment problem, is intractable. Motivated by this, we analyze convex relaxations based on minimizing $\|AX - XB\|_F$ over the ...

---

### 34. A Decision-Theoretic View of Test-Time Training: When, How Far, and Which Directions to Adapt

**Authors:** Tomoya Wakayama

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15569v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15569v1)

**Summary:** Test-time training (TTT) adapts a pretrained model to each prompt via parameter updates, improving accuracy under pretraining-to-test distribution shifts. Yet, its performance often suffers from instability and sensitivity to hyperparameters such as update steps and subspace. We explain this behavior through a decision-theoretic lens, treating TTT as implicit Bayesian inference in the kernel regime. Under a Gaussian process benchmark, we show that TTT reduces prediction error when updates are sp...

---

### 35. Service-Induced Congestion in Memory-Constrained LLM Serving

**Authors:** Ruicheng Ao, Jing Dong, Gan Luo, et al.

**Published:** 2026-06-14

🔗 [Paper](http://arxiv.org/abs/2606.15555v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15555v1)

**Summary:** In large language model (LLM) serving, each request accumulates persistent graphics processing unit (GPU) memory during service as its key-value cache grows with every generated token. Under high concurrency, aggregate memory usage therefore increases endogenously over time: the service process itself creates future capacity pressure. When memory capacity is exceeded, systems evict active requests, discarding cached state and restarting them later, which wastes computation and reduces throughput...

---

### 36. Ricci-Filtration: Boosting Retrieval-Augmented Generation Reranker to Query-Answer Tasks by Discrete Ricci Flow

**Authors:** Tian Qin, Wei-Min Huang

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15482v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15482v1)

**Summary:** Ricci flow is a curvature-guided diffusion process that deforms space by shrinking regions of high positive curvature and expanding those with negative curvature. Similarly, discrete Ricci flow on weighted graphs modifies edge weights by shrinking edges with positive Ricci curvature and stretching those with negative Ricci curvature, effectively increasing the separation between clusters. Inspired by these two cornerstone works, we propose a geometry-based RAG reranker enhancement procedure call...

---

### 37. Structured Nonparametric Variational Inference for Dependent Latent Modeling

**Authors:** Yuda Shao, Zhiling Gu, Shan Yu

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15458v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15458v1)

**Summary:** Variational inference (VI) is a core engine of modern AI, enabling scalable approximate Bayesian learning and uncertainty-aware training of large probabilistic and generative models. In this paper, we propose Structured Nonparametric Variational Inference (SN-VI), a novel framework for modeling complex dependencies among latent variables in posterior approximation, leveraging multivariate spline techniques. Unlike traditional methods that rely on the mean-field assumption, SN-VI preserves intric...

---

### 38. PHINN: Persistent Homology Inspired Neural Network for Rare-Event Time Series Generation

**Authors:** Emre Yusuf, Ren Takahashi, Jayabrata Bhaduri

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15452v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15452v1)

**Summary:** Rare events in time series are critical to model but hard to learn due to data scarcity. Current generative models struggle with extreme values. We observe that rare events leave distinct topological fingerprints - transitions in Betti numbers from point-cloud embeddings - that are more stable and discriminative than statistical moments.   We introduce PHINN, a flow-matching framework using dynamic Betti curves as conditioning signals and a persistence landscape loss for homology consistency. It...

---

### 39. The Reverse Telescoping Coordinate System for Positive Definite Matrices: Geometry, Computation, and Generative Modeling

**Authors:** Anindya Bhadra

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15442v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15442v1)

**Summary:** We design a new unconstrained coordinate system where a $p\times p$ symmetric positive definite (SPD) matrix $Θ$ is represented by a reverse telescoping map $Θ(x)=\rm{RT}(x)$, with $x=(v,d,r)\in\mathbb{R}\times\mathbb{R}^{(p-1)}\times\mathbb{R}^{p(p-1)/2}$, representing respectively the log volume or log determinant; and the shape, as encoded by log relative diagonal scales and partial covariances among the nodes. This construction results in important properties not available in other charts, e...

---

### 40. Finite Resources False Discovery Rate Control in Structured Hypothesis Spaces

**Authors:** Binyamin Perets, Shie Mannor

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15393v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15393v1)

**Summary:** Scientific discovery relies on large-scale hypothesis testing. However, the capacity to identify true discoveries while controlling false discovery faces major challenges: obtaining relevant reference data (the null distribution) is resource-intensive, leaving finite-data uncertainty, and the procedure should account for the inherent structure in the hypothesis space, when such structure exists. Here, we present a framework for controlling the false discovery rate both when each hypothesis is ev...

---

### 41. LLMs on Tabular Data with Limited Semantics: Evidence from Industrial Car Retrofit Prediction

**Authors:** Aina Vila Pons, Ioannis Tzachristas, Constantinos Antoniou

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15314v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15314v1)

**Summary:** Industrial retrofit planning depends on structured operational data rather than free text: planners must estimate whether a newly registered prototype will require a retrofit, which retrofit package it will need, and how long the work will take. We study an industrial dataset linking a prototype-registration system (284,271 vehicles) with a retrofit-management system (48,716 cleaned visits), and compare strong tabular machine learning baselines with three LLM-based strategies on row-serialized i...

---

### 42. Can Neural Networks Achieve Optimal Computational-statistical Tradeoff? An Analysis on Single-Index Model

**Authors:** Siyu Chen, Beining Wu, Miao Lu, et al.

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15219v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15219v1)

**Summary:** In this work, we tackle the following question: Can neural networks trained with gradient-based methods achieve the optimal computational-statistical tradeoff in learning Gaussian single-index models? Prior research has shown that any polynomial-time algorithm under the statistical query (SQ) framework requires $Ω(d^{s^\star/2}\lor d)$ samples, where $s^\star$ is the generative exponent representing the intrinsic difficulty of learning the underlying model. However, it remains unknown whether ne...

---

### 43. Conformal Candidate Certification for Offline Model-Based Optimization

**Authors:** Seungjin Choi

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15217v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15217v1)

**Summary:** Offline model-based optimization (MBO) proposes candidates by optimizing a surrogate trained on a fixed historical dataset. Because candidates are deliberately out-of-distribution, surrogate rankings are least reliable exactly where the optimizer is most aggressive, yet existing methods provide no per-candidate statistical certificate that a design meets a target threshold. We propose \emph{Conformal Candidate Certification} (CCC), a post-hoc wrapper that attaches a calibrated one-sided lower bo...

---

### 44. A Koopman-PINN Framework for Epidemic Models: Parameter Inference and Forecasting

**Authors:** Achraf Zinihi, Matthias Ehrhardt, Moulay Rchid Sidi Ammi

**Published:** 2026-06-13

🔗 [Paper](http://arxiv.org/abs/2606.15201v1) | 📄 [PDF](https://arxiv.org/pdf/2606.15201v1)

**Summary:** We propose a Koopman-enhanced physics-informed neural network (K--PINN) framework for parameter inference and forecasting in nonlinear epidemic models. This method combines Koopman operator theory and physics-informed learning. It maps epidemic states into a latent observable space where the dynamics evolve approximately linearly while satisfying the governing epidemic equations through automatic differentiation. This integration improves interpretability, parameter identifiability, and long-ter...

---

### 45. Representation Costs in Data Science: Foundations and the Quasi-Banach Spaces of Deep Neural Networks

**Authors:** Greg Ongie, Rahul Parhi

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14954v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14954v1)

**Summary:** We develop a general framework for analyzing representation costs of parametric data-fitting methods through their parameter-space regularizers. From this abstract perspective, we define representation costs for arbitrary parametric models and reveal their induced (native) function spaces. This unifies recent function-space views of data-fitting methods. We also prove that many natural results hold in this abstract setting, including representer theorems for parametric methods on their native sp...

---

### 46. Policy Regret for Embedding Model Routing: Contextual Bandits with Low-Rank Experts

**Authors:** Yan Dai, Negin Golrezaei, Patrick Jaillet

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14929v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14929v1)

**Summary:** Modern recommendation systems increasingly rely on dynamically routing diverse queries to multiple embedding models. Despite its practical significance, this problem remains poorly understood under realistic conditions like adversarial queries, bandit feedback, and limited observability of models. We formalize embedding model routing as an adversarial contextual linear bandit with low-rank experts, where contexts are queries, actions are items, and experts are the embedding models working on low...

---

### 47. Audited Conformal Prediction for Classification under Unknown Distribution Shift

**Authors:** Yanfei Zhou, Rizal Fathony, Nam H. Nguyen, et al.

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14909v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14909v1)

**Summary:** We consider the problem of uncertainty quantification for a pretrained classification model deployed under unknown distribution shift. We propose Audited Conformal Prediction (ACP), a method that leverages a small labeled dataset from the target population to train an auxiliary audit model identifying inputs where the legacy model is likely to fail. By integrating the audit model's outputs into the conformal prediction framework, ACP produces prediction sets that guarantee marginal coverage whil...

---

### 48. Relational Structural Causal Models

**Authors:** Adiba Ejaz, Elias Bareinboim

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14892v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14892v1)

**Summary:** An artificial intelligence must have a model of its environment that is causal, supporting reasoning about interventions and counterfactuals, and also combinatorial, supporting generalization to unseen combinations of objects. In this work, we formally study when and how such a model can be learned. We develop relational structural causal models, extending structural causal models (Pearl 2009) to settings where objects and their relations vary. First, we show how answers to not only causal but a...

---

### 49. Event Generation with Parallel Langevin Sampling and Learned Stein Diagnostics

**Authors:** Rob Verheyen

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14854v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14854v1)

**Summary:** Efficient event generation is a major computational challenge for precision collider phenomenology, especially for high-multiplicity final states where matrix-element evaluations are expensive and rejection-sampling efficiencies are low. We study an alternative approach based on many parallel underdamped Langevin chains, retaining one terminal state from each chain to obtain unweighted events while avoiding within-chain autocorrelation. A learned Stein discrepancy is used as a convergence diagno...

---

### 50. Optimal Hidden-Target Learning for Online Inventory Optimization on General Convex Sets

**Authors:** Anthony Pineci, Yunzong Xu

**Published:** 2026-06-12

🔗 [Paper](http://arxiv.org/abs/2606.14679v1) | 📄 [PDF](https://arxiv.org/pdf/2606.14679v1)

**Summary:** Online inventory optimization (OIO) is online convex optimization with physical memory: inventory carryover makes the feasible action set depend on the past. A natural principle, used in stochastic inventory learning and recently in OIO under a single linear capacity constraint, is to maintain a hidden target chosen by an online learner and implement its projection onto the currently feasible order-up-to set. We prove that this simple principle is optimal for OIO on arbitrary bounded convex capa...

---

