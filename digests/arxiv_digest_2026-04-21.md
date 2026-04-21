# arXiv Daily Digest - 2026-04-21

Total papers: 350

---

## cs.AI

**50 papers**

### 1. MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval

**Authors:** Shaden Alshammari, Kevin Wen, Abrar Zainal, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18584v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18584v1)

**Summary:** Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We introduce MathNet, a high-quality, large-scale, multimodal, and multilingual dataset of Olympiad-level math problems together with a benchmark for evaluating mathematical reasoning in generative models and mathematical retrieval in embedding-based systems. MathNet spans 47 countries, 17 languages, and...

---

### 2. Sessa: Selective State Space Attention

**Authors:** Liubomyr Horbatko

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18580v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18580v1)

**Summary:** Modern sequence models are dominated by Transformers, where self-attention mixes information from the visible context in an input-dependent way. However, when retrieval is not sharp and attention remains diffuse over an effective support $S_{\mathrm{eff}}(t)$, the influence of any individual token is diluted, typically scaling as $O(1/S_{\mathrm{eff}}(t))$ and reaching $O(1/\ell)$ for old tokens in full-prefix settings. Structured state-space models process sequences recurrently through an expli...

---

### 3. Bounded Ratio Reinforcement Learning

**Authors:** Yunke Ao, Le Chen, Bruce D. Lee, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18578v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18578v1)

**Summary:** Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization...

---

### 4. Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs

**Authors:** Kevin Murphy

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18576v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18576v1)

**Summary:** We present BLF (Bayesian Linguistic Forecaster), an agentic system for binary forecasting that achieves state-of-the-art performance on the ForecastBench benchmark. The system is built on three ideas. (1) A Bayesian linguistic belief state: a semi-structured representation combining numerical probability estimates with natural-language evidence summaries, updated by the LLM at each step of an iterative tool-use loop. This contrasts with the common approach of appending all retrieved evidence to ...

---

### 5. When Can LLMs Learn to Reason with Weak Supervision?

**Authors:** Salman Rahman, Jingyan Shen, Anna Mordvina, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18574v1)

**Summary:** Large language models have achieved significant reasoning improvements through reinforcement learning with verifiable rewards (RLVR). Yet as model capabilities grow, constructing high-quality reward signals becomes increasingly difficult, making it essential to understand when RLVR can succeed under weaker forms of supervision. We conduct a systematic empirical study across diverse model families and reasoning domains under three weak supervision settings: scarce data, noisy rewards, and self-su...

---

### 6. Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale

**Authors:** A. Sophia Koepke, Daniil Zverev, Shiry Ginosar, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18572v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18572v1)

**Summary:** The Platonic Representation Hypothesis suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If true, this has significant implications for whether modality choice matters at all. We show that the experimental evidence for this hypothesis is fragile and depends critically on the evaluation regime. Alignment is measured using mutual nearest neighbors on small datasets ($\approx$1K samples) and...

---

### 7. A multimodal and temporal foundation model for virtual patient representations at healthcare system scale

**Authors:** Andrew Zhang, Tong Ding, Sophia J. Wagner, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18570v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18570v1)

**Summary:** Modern medicine generates vast multimodal data across siloed systems, yet no existing model integrates the full breadth and temporal depth of the clinical record into a unified patient representation. We introduce Apollo, a multimodal temporal foundation model trained and evaluated on over three decades of longitudinal hospital records from a major US hospital system, composed of 25 billion records from 7.2 million patients, representing 28 distinct medical modalities and 12 major medical specia...

---

### 8. Latent Phase-Shift Rollback: Inference-Time Error Correction via Residual Stream Monitoring and KV-Cache Steering

**Authors:** Manan Gupta, Dhruv Kumar

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18567v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18567v1)

**Summary:** Large language models frequently commit unrecoverable reasoning errors mid-generation: once a wrong step is taken, subsequent tokens compound the mistake rather than correct it. We introduce $\textbf{Latent Phase-Shift Rollback}$ (LPSR): at each generation step, we monitor the residual stream at a critical layer lcrit, detect abrupt directional reversals (phase shifts) via a cosine-similarity $+$ entropy dual gate, and respond by rolling back the KV-cache and injecting a pre-computed steering ve...

---

### 9. Benchmarking System Dynamics AI Assistants: Cloud Versus Local LLMs on CLD Extraction and Discussion

**Authors:** Terry Leitch

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18566v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18566v1)

**Summary:** We present a systematic evaluation of large language model families -- spanning both proprietary cloud APIs and locally-hosted open-source models -- on two purpose-built benchmarks for System Dynamics AI assistance: the \textbf{CLD Leaderboard} (53 tests, structured causal loop diagram extraction) and the \textbf{Discussion Leaderboard} (interactive model discussion, feedback explanation, and model building coaching).   On CLD extraction, cloud models achieve 77--89\% overall pass rates; the bes...

---

### 10. ClawEnvKit: Automatic Environment Generation for Claw-Like Agents

**Authors:** Xirui Li, Ming Li, Derry Xu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18543v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18543v1)

**Summary:** Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that what is needed is not just a dataset, but an automated pipeline capable of generating diverse, verified environments on demand. To this end, we introduce ClawEnvKit, an autonomous generation pipeline that instantiates this formalism from natural language descriptions. The pipeline comprises three modules: (1) a parser that extracts structured generat...

---

### 11. Transition-Matrix Regularization for Next Dialogue Act Prediction in Counselling Conversations

**Authors:** Eric Rudolph, Philipp Steigerwald, Jens Albrecht

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18539v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18539v1)

**Summary:** This paper studies how empirical dialogue-flow statistics can be incorporated into Next Dialogue Act Prediction (NDAP). A KL regularization term is proposed that aligns predicted act distributions with corpus-derived transition patterns. Evaluated on a 60-class German counselling taxonomy using 5-fold cross-validation, this improves macro-F1 by 9--42% relative depending on encoder and substantially improves dialogue-flow alignment. Cross-dataset validation on HOPE suggests that improvements tran...

---

### 12. Symbolic Synthesis for LTLf+ Obligations

**Authors:** Giuseppe De Giacomo, Christian Hagemeier, Daniel Hausmann, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18532v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18532v1)

**Summary:** We study synthesis for obligation properties expressed in LTLfp, the extension of LTLf to infinite traces. Obligation properties are positive Boolean combinations of safety and guarantee (co-safety) properties and form the second level of the temporal hierarchy of Manna and Pnueli. Although obligation properties are expressed over infinite traces, they retain most of the simplicity of LTLf. In particular, we show that they admit a translation into symbolically represented deterministic weak auto...

---

### 13. OGER: A Robust Offline-Guided Exploration Reward for Hybrid Reinforcement Learning

**Authors:** Xinyu Ma, Mingzhou Xu, Xuebo Liu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18530v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18530v1)

**Summary:** Recent advancements in Reinforcement Learning with Verifiable Rewards (RLVR) have significantly improved Large Language Model (LLM) reasoning, yet models often struggle to explore novel trajectories beyond their initial latent space. While offline teacher guidance and entropy-driven strategies have been proposed to address this, they often lack deep integration or are constrained by the model's inherent capacity. In this paper, we propose OGER, a novel framework that unifies offline teacher guid...

---

### 14. IDOBE: Infectious Disease Outbreak forecasting Benchmark Ecosystem

**Authors:** Aniruddha Adiga, Jingyuan Chou, Anshul Chiranth, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18521v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18521v1)

**Summary:** Epidemic forecasting has become an integral part of real-time infectious disease outbreak response. While collaborative ensembles composed of statistical and machine learning models have become the norm for real-time forecasting, standardized benchmark datasets for evaluating such methods are lacking. Further, there is limited understanding on performance of these methods for novel outbreaks with limited historical data. In this paper, we propose IDOBE, a curated collection of epidemiological ti...

---

### 15. LLM Safety From Within: Detecting Harmful Content with Internal Representations

**Authors:** Difan Jiao, Yilun Liu, Ye Yuan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18519v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18519v1)

**Summary:** Guard models are widely used to detect harmful content in user prompts and LLM responses. However, state-of-the-art guard models rely solely on terminal-layer representations and overlook the rich safety-relevant features distributed across internal layers. We present SIREN, a lightweight guard model that harnesses these internal features. By identifying safety neurons via linear probing and combining them through an adaptive layer-weighted strategy, SIREN builds a harmfulness detector from LLM ...

---

### 16. Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks

**Authors:** Md Rysul Kabir, Zoran Tiganj

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18510v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18510v1)

**Summary:** Open-weight language models can be rendered unsafe through several distinct interventions, but the resulting models may differ substantially in capabilities, behavioral profile, and internal failure mode. We study behavioral and mechanistic properties of jailbroken models across three unsafe routes: harmful supervised fine-tuning (SFT), harmful reinforcement learning with verifiable rewards (RLVR), and refusal-suppressing abliteration. All three routes achieve near-ceiling harmful compliance, bu...

---

### 17. Document-as-Image Representations Fall Short for Scientific Retrieval

**Authors:** Ghazal Khalighinejad, Raghuveer Thirukovalluru, Alexander H. Oh, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18508v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18508v1)

**Summary:** Many recent document embedding models are trained on document-as-image representations, embedding rendered pages as images rather than the underlying source. Meanwhile, existing benchmarks for scientific document retrieval, such as ArXivQA and ViDoRe, treat documents as images of pages, implicitly favoring such representations. In this work, we argue that this paradigm is not well-suited for text-rich multimodal scientific documents, where critical evidence is distributed across structured sourc...

---

### 18. Learning the Riccati solution operator for time-varying LQR via Deep Operator Networks

**Authors:** Jun Chen, Umberto Biccari, Junmin Wang

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18507v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18507v1)

**Summary:** We propose a computational framework for replacing the repeated numerical solution of differential Riccati equations in finite-horizon Linear Quadratic Regulator (LQR) problems by a learned operator surrogate. Instead of solving a nonlinear matrix-valued differential equation for each new system instance, we construct offline an approximation of the associated solution operator mapping time-dependent system parameters to the Riccati trajectory. The resulting model enables fast online evaluation ...

---

### 19. Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD

**Authors:** Nicholas Thumiger, Andrea Bartezzaghi, Mattia Rigotti, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18491v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18491v1)

**Summary:** Computational Fluid Dynamics (CFD) is central to race-car aerodynamic development, yet its cost -- tens of thousands of core-hours per high-fidelity evaluation -- severely limits the design space exploration feasible within realistic budgets. AI-based surrogate models promise to alleviate this bottleneck, but progress has been constrained by the limited complexity of public datasets, which are dominated by smoothed passenger-car shapes that fail to exercise surrogates on the thin, complex, highl...

---

### 20. LQM: Linguistically Motivated Multidimensional Quality Metrics for Machine Translation

**Authors:** Samar M. Magdy, Fakhraddin Alwajih, Abdellah El Mekki, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18490v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18490v1)

**Summary:** Existing MT evaluation frameworks, including automatic metrics and human evaluation schemes such as Multidimensional Quality Metrics (MQM), are largely language-agnostic. However, they often fail to capture dialect- and culture-specific errors in diglossic languages (e.g., Arabic), where translation failures stem from mismatches in language variety, content coverage, and pragmatic appropriateness rather than surface form alone.We introduce LQM: Linguistically Motivated Multidimensional Quality M...

---

### 21. Adversarial Humanities Benchmark: Results on Stylistic Robustness in Frontier Model Safety

**Authors:** Marcello Galisai, Susanna Cifani, Francesco Giarrusso, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18487v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18487v1)

**Summary:** The Adversarial Humanities Benchmark (AHB) evaluates whether model safety refusals survive a shift away from familiar harmful prompt forms. Starting from harmful tasks drawn from MLCommons AILuminate, the benchmark rewrites the same objectives through humanities-style transformations while preserving intent. This extends literature on Adversarial Poetry and Adversarial Tales from single jailbreak operators to a broader benchmark family of stylistic obfuscation and goal concealment. In the benchm...

---

### 22. WorldDB: A Vector Graph-of-Worlds Memory Engine with Ontology-Aware Write-Time Reconciliation

**Authors:** Harish Santhanalakshmi Ganesan

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18478v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18478v1)

**Summary:** Persistent memory is the bottleneck separating stateless chatbots from long-running agentic systems. Retrieval-augmented generation (RAG) over flat vector stores fragments facts into chunks, loses cross-session identity, and has no first-class notion of supersession or contradiction. Recent bitemporal knowledge-graph systems (Graphiti, Memento, Hydra DB) add typed edges and valid-time metadata, but the graph itself remains flat: no recursive composition, no content-addressed invariants on nodes,...

---

### 23. A Generalized Synthetic Control Method for Baseline Estimation in Demand Response Services

**Authors:** Jonas Sievers, Mardavij Roozbehani

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18469v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18469v1)

**Summary:** Baseline estimation is critical to Demand Response (DR) settlement in electricity markets, yet existing machine learning methods remain limited in predictive performance, while methodologies from causal inference and counterfactual prediction are still underutilized in this domain. We introduce a Generalized Synthetic Control Method that builds on the classical Synthetic Control Method (SCM) from econometrics. While SCM provides a powerful framework for counterfactual estimation, classical SCM r...

---

### 24. Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation

**Authors:** Tianshi Cao, Jiawei Ren, Yuxuan Zhang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18468v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18468v1)

**Summary:** Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge, we present Asset Harvester, an image-to-3D model and end-to-end pipeline that ...

---

### 25. An Integrated Deep-Learning Framework for Peptide-Protein Interaction Prediction and Target-Conditioned Peptide Generation with ConGA-PePPI and TC-PepGen

**Authors:** Chupei Tang, Junxiao Kong, Moyu Tang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18467v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18467v1)

**Summary:** Motivation: Peptide-protein interactions (PepPIs) are central to cellular regulation and peptide therapeutics, but experimental characterization remains too slow for large-scale screening. Existing methods usually emphasize either interaction prediction or peptide generation, leaving candidate prioritization, residue-level interpretation, and target-conditioned expansion insufficiently integrated. Results: We present an integrated framework for early-stage peptide screening that combines a partn...

---

### 26. Using large language models for embodied planning introduces systematic safety risks

**Authors:** Tao Zhang, Kaixian Qu, Zhibin Li, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18463v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18463v1)

**Summary:** Large language models are increasingly used as planners for robotic systems, yet how safely they plan remains an open question. To evaluate safe planning systematically, we introduce DESPITE, a benchmark of 12,279 tasks spanning physical and normative dangers with fully deterministic validation. Across 23 models, even near-perfect planning ability does not ensure safety: the best-planning model fails to produce a valid plan on only 0.4% of tasks but produces dangerous plans on 28.3%. Among 18 op...

---

### 27. Progressive Online Video Understanding with Evidence-Aligned Timing and Transparent Decisions

**Authors:** Kecheng Zhang, Zongxin Yang, Mingfei Han, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18459v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18459v1)

**Summary:** Visual agents operating in the wild must respond to queries precisely when sufficient evidence first appears in a video stream, a critical capability that is overlooked by conventional video LLMs evaluated in offline settings. The shift to an online, streaming paradigm introduces significant challenges: a lack of decision transparency, the difficulty of aligning response timing with visual evidence, and the need to maintain a global, causally consistent understanding under tight computational bu...

---

### 28. ProtoCLIP: Prototype-Aligned Latent Refinement for Robust Zero-Shot Chest X-Ray Classification

**Authors:** Florian Kittler, Sheethal Bhat, Andreas Maier

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18444v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18444v1)

**Summary:** Zero-shot vision-language models (VLMs) have shown promise for chest radiograph classification, but their performance is often limited by confounding label co-occurrence, long-tail class imbalance, and transfer instability under domain shift. We propose ProtoCLIP, a refinement strategy for CLIP-style VLMs that improves zero-shot discrimination through targeted data curation and distilled anchor alignment. Specifically, we construct pathology-focused training subsets with curated negative samples...

---

### 29. Revisiting Change VQA in Remote Sensing with Structured and Native Multimodal Qwen Models

**Authors:** Yakoub Bazi, Mohamad M. Al Rahhal, Mansour Zuair, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18429v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18429v1)

**Summary:** Change visual question answering (Change VQA) addresses the problem of answering natural-language questions about semantic changes between bi-temporal remote sensing (RS) images. Although vision-language models (VLMs) have recently been studied for temporal RS image understanding, Change VQA remains underexplored in the context of modern multimodal models. In this letter, we revisit the CDVQA benchmark using recent Qwen models under a unified low-rank adaptation (LoRA) setting. We compare Qwen3-...

---

### 30. Six Llamas: Comparative Religious Ethics Through LoRA-Adapted Language Models

**Authors:** Chad Coleman, W. Russell Neuman, Manan Shah, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18404v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18404v1)

**Summary:** We present Six Llamas, a comparative study examining whether large language models fine-tuned on distinct religious corpora encode systematically different patterns of ethical reasoning. Six variants of Meta-Llama-3.1-8B are constructed: one unmodified control and five LoRA-adapted models trained exclusively on the sacred and theological texts of Christianity, Islam, Judaism, Hinduism, or Buddhism. All six models are probed with an identical battery of 17 standardized ethical prompts spanning mo...

---

### 31. AlphaContext: An Evolutionary Tree-based Psychometric Context Generator for Creativity Assessment

**Authors:** Yixuan Wang, Yue Huang, Hong Qian, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18398v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18398v1)

**Summary:** Creativity has become a core competence in the era of LLMs and human-AI collaboration, underpinning innovation in real-world problem solving. Crucially, the systematic improvement of creativity necessitates scientifically valid assessment instruments. Psychometric research recognizes context-based assessment as an effective way to measure creative thinking. However, high-quality expert-designed contexts remain scarce. Existing LLM-based generators often struggle with insufficient assessment cues...

---

### 32. Randomly Initialized Networks Can Learn from Peer-to-Peer Consensus

**Authors:** Esteban Rodríguez-Betancourt, Edgar Casasola-Murillo

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18390v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18390v1)

**Summary:** In self-supervised learning, self-distilled methods have shown impressive performance, learning representations useful for downstream tasks and even displaying emergent properties. However, state-of-the-art methods usually rely on ensembles of complex mechanisms, with many design choices that are empirically motivated and not well understood.   In this work, we explore the role of self-distillation within learning dynamics. Specifically, we isolate the effect of self-distillation by training a g...

---

### 33. Learning from Less: Measuring the Effectiveness of RLVR in Low Data and Compute Regimes

**Authors:** Justin Bauer, Thomas Walshe, Derek Pham, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18381v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18381v1)

**Summary:** Fine-tuning Large Language Models (LLMs) typically relies on large quantities of high-quality annotated data, or questions with well-defined ground truth answers in the case of Reinforcement Learning with Verifiable Rewards (RLVR). While previous work has explored the benefits to model reasoning capabilities by scaling both data and compute used for RLVR, these results lack applicability in many real-world settings where annotated data and accessible compute may be scarce. In this work, we prese...

---

### 34. The implicated scientist: on the role of AI researchers in the development of weapons systems

**Authors:** Alexandra Volokhova, Alex Hernandez-Garcia

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18380v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18380v1)

**Summary:** Artificial intelligence (AI) technologies are increasingly used in modern weapons systems. Notably, these systems have recently been involved in mass killings and destruction at scale. Furthermore, there is currently a strong interest and competition among powerful players to accelerate the proliferation of weapons with automated or AI-based components, a phenomenon known as AI arms race. This competition poses a risk of causing even more deaths and devastation in the future, as well as increase...

---

### 35. IceBreaker for Conversational Agents: Breaking the First-Message Barrier with Personalized Starters

**Authors:** Hongwei Zheng, Weiqi Wu, Zhengjia Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18375v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18375v1)

**Summary:** Conversational agents, such as ChatGPT and Doubao, have become essential daily assistants for billions of users. To further enhance engagement, these systems are evolving from passive responders to proactive companions. However, existing efforts focus on activation within ongoing dialogues, while overlooking a key real-world bottleneck. In the conversation initiation stage, users may have a vague need but no explicit query intent, creating a first-message barrier where the conversation holds bef...

---

### 36. Dissecting AI Trading: Behavioral Finance and Market Bubbles

**Authors:** Shumiao Ouyang, Pengfei Sui

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18373v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18373v1)

**Summary:** We study how AI agents form expectations and trade in experimental asset markets. Using a simulated open-call auction populated by autonomous Large Language Model (LLM) agents, we document three main findings. First, AI agents exhibit classic behavioral patterns: a pronounced disposition effect and recency-weighted extrapolative beliefs. Second, these individual-level patterns aggregate into equilibrium dynamics that replicate classic experimental findings (Smith et al., 1988), including the pre...

---

### 37. Training and Agentic Inference Strategies for LLM-based Manim Animation Generation

**Authors:** Ravidu Suien Rammuni Silva, Ahmad Lotfi, Isibor Kennedy Ihianle, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18364v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18364v1)

**Summary:** Generating programmatic animation using libraries such as Manim presents unique challenges for Large Language Models (LLMs), requiring spatial reasoning, temporal sequencing, and familiarity with domain-specific APIs that are underrepresented in general pre-training data. A systematic study of how training and inference strategies interact in this setting is lacking in current research. This study introduces ManimTrainer, a training pipeline that combines Supervised Fine-tuning (SFT) with Reinfo...

---

### 38. Tight Auditing of Differential Privacy in MST and AIM

**Authors:** Georgi Ganev, Meenatchi Sundaram Muthu Selva Annamalai, Bogdan Kulynych

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18352v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18352v1)

**Summary:** State-of-the-art Differentially Private (DP) synthetic data generators such as MST and AIM are widely used, yet tightly auditing their privacy guarantees remains challenging. We introduce a Gaussian Differential Privacy (GDP)-based auditing framework that measures privacy via the full false-positive/false-negative tradeoff. Applied to MST and AIM under worst-case settings, our method provides the first tight audits in the strong-privacy regime. For $(ε,δ)=(1,10^{-2})$, we obtain $μ_{emp}\approx0...

---

### 39. AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation

**Authors:** Haoyue Tan, Shengnan Wang, Yulin Qiao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18348v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18348v1)

**Summary:** Video diffusion transformers (DiTs) suffer from prohibitive inference latency due to quadratic attention complexity. Existing sparse attention methods either overlook semantic similarity or fail to adapt to heterogeneous token distributions across layers, leading to model performance degradation. We propose AdaCluster, a training-free adaptive clustering framework that accelerates the generation of DiTs while preserving accuracy. AdaCluster applies an angle-similarity-preserving clustering metho...

---

### 40. Multilingual Training and Evaluation Resources for Vision-Language Models

**Authors:** Daniela Baiamonte, Elena Fano, Matteo Gabburo, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18347v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18347v1)

**Summary:** Vision Language Models (VLMs) achieved rapid progress in the recent years. However, despite their growth, VLMs development is heavily grounded on English, leading to two main limitations: (i) the lack of multilingual and multimodal datasets for training, and (ii) the scarcity of comprehensive evaluation benchmarks across languages. In this work, we address these gaps by introducing a new comprehensive suite of resources for VLMs training and evaluation spanning five European languages (English, ...

---

### 41. One Pass for All: A Discrete Diffusion Model for Knowledge Graph Triple Set Prediction

**Authors:** Jihong Guan, Jiaqi Wang, Wengen Li, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18344v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18344v1)

**Summary:** Knowledge Graphs (KGs) are composed of triples, and the goal of Knowledge Graph Completion (KGC) is to infer the missing factual triples. Traditional KGC tasks predict missing elements in a triple given one or two of its elements. As a more realistic task, the Triple Set Prediction (TSP) task aims to infer the set of missing triples conditioned only on the observed knowledge graph, without assuming any partial information about the missing triples. Existing TSP methods predict the set of missing...

---

### 42. PARM: Pipeline-Adapted Reward Model

**Authors:** Xingyu Fan, Wei Shao, Jiacheng Liu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18327v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18327v1)

**Summary:** Reward models (RMs) are central to aligning large language models (LLMs) with human preferences, powering RLHF and advanced decoding strategies. While most prior work focuses on single-step generation, real-world applications increasingly adopt multi-stage LLM pipelines, where effective reward guidance remains underexplored. We investigate this through code generation for combinatorial optimization, constructing a pipeline that integrates reward models into both formulation and solution stages. ...

---

### 43. EVE: Verifiable Self-Evolution of MLLMs via Executable Visual Transformations

**Authors:** Yongrui Heng, Chaoya Jiang, Han Yang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18320v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18320v1)

**Summary:** Self-evolution of multimodal large language models (MLLMs) remains a critical challenge: pseudo-label-based methods suffer from progressive quality degradation as model predictions drift, while template-based methods are confined to a static set of transformations that cannot adapt in difficulty or diversity. We contend that robust, continuous self-improvement requires not only deterministic external feedback independent of the model's internal certainty, but also a mechanism to perpetually dive...

---

### 44. On the Importance and Evaluation of Narrativity in Natural Language AI Explanations

**Authors:** Mateusz Cedro, David Martens

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18311v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18311v1)

**Summary:** Explainable AI (XAI) aims to make the behaviour of machine learning models interpretable, yet many explanation methods remain difficult to understand. The integration of Natural Language Generation into XAI aims to deliver explanations in textual form, making them more accessible to practitioners. Current approaches, however, largely yield static lists of feature importances. Although such explanations indicate what influences the prediction, they do not explain why the prediction occurs. In thi...

---

### 45. Toward Zero-Egress Psychiatric AI: On-Device LLM Deployment for Privacy-Preserving Mental Health Decision Support

**Authors:** Eranga Bandara, Asanga Gunaratna, Ross Gore, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18302v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18302v1)

**Summary:** Privacy represents one of the most critical yet underaddressed barriers to AI adoption in mental healthcare -- particularly in high-sensitivity operational environments such as military, correctional, and remote healthcare settings, where the risk of patient data exposure can deter help-seeking behavior entirely. Existing AI-enabled psychiatric decision support systems predominantly rely on cloud-based inference pipelines, requiring sensitive patient data to leave the device and traverse externa...

---

### 46. Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence

**Authors:** Guanting Dong, Junting Lu, Junjie Huang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18292v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18292v1)

**Summary:** Large language models are increasingly expected to serve as general-purpose agents that interact with external, stateful tool environments. The Model Context Protocol (MCP) and broader agent skills offer a unified interface for connecting agents with scalable real-world services, but training robust agents remains limited by the lack of realistic environments and principled mechanisms for life-long learning. In this paper, we present \textbf{Agent-World}, a self-evolving training arena for advan...

---

### 47. Enhancing Tabular Anomaly Detection via Pseudo-Label-Guided Generation

**Authors:** Wei Huang, Yuxuan Xiong, Hezhe Qiao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18266v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18266v1)

**Summary:** Identifying anomalous instances in tabular data is essential for improving data reliability and maintaining system stability. Due to the scarcity of ground-truth anomaly labels, existing methods mainly rely on unsupervised anomaly detection models, or exploit a small number of labeled anomalies to facilitate detection via sample generation or contrastive learning. However, unsupervised methods lack sufficient anomaly awareness, while current generation and contrastive approaches tend to compute ...

---

### 48. Long-Text-to-Image Generation via Compositional Prompt Decomposition

**Authors:** Jen-Yuan Huang, Tong Lin, Yilun Du

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18258v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18258v1)

**Summary:** While modern text-to-image (T2I) models excel at generating images from intricate prompts, they struggle to capture the key details when the inputs are descriptive paragraphs. This limitation stems from the prevalence of concise captions that shape their training distributions. Existing methods attempt to bridge this gap by either fine-tuning T2I models on long prompts, which generalizes poorly to longer lengths; or by projecting the oversize inputs into normal-prompt space and compromising fide...

---

### 49. DocQAC: Adaptive Trie-Guided Decoding for Effective In-Document Query Auto-Completion

**Authors:** Rahul Mehta, Kavin R, Indrajit Pal, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18257v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18257v1)

**Summary:** Query auto-completion (QAC) has been widely studied in the context of web search, yet remains underexplored for in-document search, which we term DocQAC. DocQAC aims to enhance search productivity within long documents by helping users craft faster, more precise queries, even for complex or hard-to-spell terms. While global historical queries are available to both WebQAC and DocQAC, DocQAC uniquely accesses document-specific context, including the current document's content and its specific hist...

---

### 50. LeGo-Code: Can Modular Curriculum Learning Advance Complex Code Generation? Insights from Text-to-SQL

**Authors:** Salmane Chafik, Saad Ezzini, Ismail Berrada

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18254v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18254v1)

**Summary:** Recently, code-oriented large language models (LLMs) have demonstrated strong capabilities in translating natural language into executable code. Text-to-SQL is a significant application of this ability, enabling non-technical users to interact with relational databases using natural language. However, state-of-the-art models continue to struggle with highly complex logic, particularly deeply nested statements involving multiple joins and conditions, as well as with real-world database schemas th...

---

## cs.CL

**50 papers**

### 1. Sessa: Selective State Space Attention

**Authors:** Liubomyr Horbatko

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18580v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18580v1)

**Summary:** Modern sequence models are dominated by Transformers, where self-attention mixes information from the visible context in an input-dependent way. However, when retrieval is not sharp and attention remains diffuse over an effective support $S_{\mathrm{eff}}(t)$, the influence of any individual token is diluted, typically scaling as $O(1/S_{\mathrm{eff}}(t))$ and reaching $O(1/\ell)$ for old tokens in full-prefix settings. Structured state-space models process sequences recurrently through an expli...

---

### 2. A multimodal and temporal foundation model for virtual patient representations at healthcare system scale

**Authors:** Andrew Zhang, Tong Ding, Sophia J. Wagner, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18570v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18570v1)

**Summary:** Modern medicine generates vast multimodal data across siloed systems, yet no existing model integrates the full breadth and temporal depth of the clinical record into a unified patient representation. We introduce Apollo, a multimodal temporal foundation model trained and evaluated on over three decades of longitudinal hospital records from a major US hospital system, composed of 25 billion records from 7.2 million patients, representing 28 distinct medical modalities and 12 major medical specia...

---

### 3. Latent Phase-Shift Rollback: Inference-Time Error Correction via Residual Stream Monitoring and KV-Cache Steering

**Authors:** Manan Gupta, Dhruv Kumar

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18567v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18567v1)

**Summary:** Large language models frequently commit unrecoverable reasoning errors mid-generation: once a wrong step is taken, subsequent tokens compound the mistake rather than correct it. We introduce $\textbf{Latent Phase-Shift Rollback}$ (LPSR): at each generation step, we monitor the residual stream at a critical layer lcrit, detect abrupt directional reversals (phase shifts) via a cosine-similarity $+$ entropy dual gate, and respond by rolling back the KV-cache and injecting a pre-computed steering ve...

---

### 4. Dual Alignment Between Language Model Layers and Human Sentence Processing

**Authors:** Tatsuki Kuribayashi, Alex Warstadt, Yohei Oseki, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18563v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18563v1)

**Summary:** A recent study (Kuribayashi et al., 2025) has shown that human sentence processing behavior, typically measured on syntactically unchallenging constructions, can be effectively modeled using surprisal from early layers of large language models (LLMs). This raises the question of whether such advantages of internal layers extend to more syntactically challenging constructions, where surprisal has been reported to underestimate human cognitive effort. In this paper, we begin by exploring internal ...

---

### 5. GSQ: Highly-Accurate Low-Precision Scalar Quantization for LLMs via Gumbel-Softmax Sampling

**Authors:** Alireza Dadgarnia, Soroush Tabesh, Mahdi Nikdan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18556v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18556v1)

**Summary:** Weight quantization has become a standard tool for efficient LLM deployment, especially for local inference, where models are now routinely served at 2-3 bits per parameter. The state of the art is currently split into two sets of methods: simple scalar quantization techniques, such as GPTQ or AWQ, which are widely deployed but plateau in accuracy at 3-4 bits per parameter (bpp), and "second-generation" vector- or trellis-quantized methods, such as QTIP, GPTVQ and AQLM, which push the accuracy f...

---

### 6. FUSE: Ensembling Verifiers with Zero Labeled Data

**Authors:** Joonhyuk Lee, Virginia Ma, Sarah Zhao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18547v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18547v1)

**Summary:** Verification of model outputs is rapidly emerging as a key primitive for both training and real-world deployment of large language models (LLMs). In practice, this often involves using imperfect LLM judges and reward models since ground truth acquisition can be time-consuming and expensive. We introduce Fully Unsupervised Score Ensembling (FUSE), a method for improving verification quality by ensembling verifiers without access to ground truth correctness labels. The key idea behind FUSE is to c...

---

### 7. ClawEnvKit: Automatic Environment Generation for Claw-Like Agents

**Authors:** Xirui Li, Ming Li, Derry Xu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18543v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18543v1)

**Summary:** Constructing environments for training and evaluating claw-like agents remains a manual, human-intensive process that does not scale. We argue that what is needed is not just a dataset, but an automated pipeline capable of generating diverse, verified environments on demand. To this end, we introduce ClawEnvKit, an autonomous generation pipeline that instantiates this formalism from natural language descriptions. The pipeline comprises three modules: (1) a parser that extracts structured generat...

---

### 8. Transition-Matrix Regularization for Next Dialogue Act Prediction in Counselling Conversations

**Authors:** Eric Rudolph, Philipp Steigerwald, Jens Albrecht

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18539v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18539v1)

**Summary:** This paper studies how empirical dialogue-flow statistics can be incorporated into Next Dialogue Act Prediction (NDAP). A KL regularization term is proposed that aligns predicted act distributions with corpus-derived transition patterns. Evaluated on a 60-class German counselling taxonomy using 5-fold cross-validation, this improves macro-F1 by 9--42% relative depending on encoder and substantially improves dialogue-flow alignment. Cross-dataset validation on HOPE suggests that improvements tran...

---

### 9. Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks

**Authors:** Md Rysul Kabir, Zoran Tiganj

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18510v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18510v1)

**Summary:** Open-weight language models can be rendered unsafe through several distinct interventions, but the resulting models may differ substantially in capabilities, behavioral profile, and internal failure mode. We study behavioral and mechanistic properties of jailbroken models across three unsafe routes: harmful supervised fine-tuning (SFT), harmful reinforcement learning with verifiable rewards (RLVR), and refusal-suppressing abliteration. All three routes achieve near-ceiling harmful compliance, bu...

---

### 10. MASS-RAG: Multi-Agent Synthesis Retrieval-Augmented Generation

**Authors:** Xingchen Xiao, Heyan Huang, Runheng Liu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18509v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18509v1)

**Summary:** Large language models (LLMs) are widely used in retrieval-augmented generation (RAG) to incorporate external knowledge at inference time. However, when retrieved contexts are noisy, incomplete, or heterogeneous, a single generation process often struggles to reconcile evidence effectively. We propose \textbf{MASS-RAG}, a multi-agent synthesis approach to retrieval-augmented generation that structures evidence processing into multiple role-specialized agents. MASS-RAG applies distinct agents for ...

---

### 11. Document-as-Image Representations Fall Short for Scientific Retrieval

**Authors:** Ghazal Khalighinejad, Raghuveer Thirukovalluru, Alexander H. Oh, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18508v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18508v1)

**Summary:** Many recent document embedding models are trained on document-as-image representations, embedding rendered pages as images rather than the underlying source. Meanwhile, existing benchmarks for scientific document retrieval, such as ArXivQA and ViDoRe, treat documents as images of pages, implicitly favoring such representations. In this work, we argue that this paradigm is not well-suited for text-rich multimodal scientific documents, where critical evidence is distributed across structured sourc...

---

### 12. LQM: Linguistically Motivated Multidimensional Quality Metrics for Machine Translation

**Authors:** Samar M. Magdy, Fakhraddin Alwajih, Abdellah El Mekki, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18490v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18490v1)

**Summary:** Existing MT evaluation frameworks, including automatic metrics and human evaluation schemes such as Multidimensional Quality Metrics (MQM), are largely language-agnostic. However, they often fail to capture dialect- and culture-specific errors in diglossic languages (e.g., Arabic), where translation failures stem from mismatches in language variety, content coverage, and pragmatic appropriateness rather than surface form alone.We introduce LQM: Linguistically Motivated Multidimensional Quality M...

---

### 13. Aligning Language Models for Lyric-to-Melody Generation with Rule-Based Musical Constraints

**Authors:** Hao Meng, Siyuan Zheng, Shuran Zhou, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18489v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18489v1)

**Summary:** Large Language Models (LLMs) show promise in lyric-to-melody generation, but models trained with Supervised Fine-Tuning (SFT) often produce musically implausible melodies with issues like poor rhythm and unsuitable vocal ranges, a phenomenon we term "constraint violation". To address this, we propose a novel alignment framework that instills musical knowledge without human annotation. We define rule-based musical constraints to automatically generate a preference dataset from an SFT model's outp...

---

### 14. Adversarial Humanities Benchmark: Results on Stylistic Robustness in Frontier Model Safety

**Authors:** Marcello Galisai, Susanna Cifani, Francesco Giarrusso, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18487v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18487v1)

**Summary:** The Adversarial Humanities Benchmark (AHB) evaluates whether model safety refusals survive a shift away from familiar harmful prompt forms. Starting from harmful tasks drawn from MLCommons AILuminate, the benchmark rewrites the same objectives through humanities-style transformations while preserving intent. This extends literature on Adversarial Poetry and Adversarial Tales from single jailbreak operators to a broader benchmark family of stylistic obfuscation and goal concealment. In the benchm...

---

### 15. OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation

**Authors:** Jinghui Lu, Jiayi Guan, Zhijian Huang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18486v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18486v1)

**Summary:** Chain-of-Thought (CoT) reasoning has become a powerful driver of trajectory prediction in VLA-based autonomous driving, yet its autoregressive nature imposes a latency cost that is prohibitive for real-time deployment. Latent CoT methods attempt to close this gap by compressing reasoning into continuous hidden states, but consistently fall short of their explicit counterparts. We suggest that this is due to purely linguistic latent representations compressing a symbolic abstraction of the world,...

---

### 16. WorldDB: A Vector Graph-of-Worlds Memory Engine with Ontology-Aware Write-Time Reconciliation

**Authors:** Harish Santhanalakshmi Ganesan

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18478v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18478v1)

**Summary:** Persistent memory is the bottleneck separating stateless chatbots from long-running agentic systems. Retrieval-augmented generation (RAG) over flat vector stores fragments facts into chunks, loses cross-session identity, and has no first-class notion of supersession or contradiction. Recent bitemporal knowledge-graph systems (Graphiti, Memento, Hydra DB) add typed edges and valid-time metadata, but the graph itself remains flat: no recursive composition, no content-addressed invariants on nodes,...

---

### 17. ESsEN: Training Compact Discriminative Vision-Language Transformers in a Low-Resource Setting

**Authors:** Clayton Fields, Casey Kennington

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18452v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18452v1)

**Summary:** Vision-language modeling is rapidly increasing in popularity with an ever expanding list of available models. In most cases, these vision-language models have parameters in the tens of billions, which is necessary for some needs, but in many cases smaller models are necessary (e.g., on edge devices or independent robotic platforms). Unfortunately, there is little research in producing light-weight models or in training them with small datasets. Inspired by the language learning progression and d...

---

### 18. BhashaSutra: A Task-Centric Unified Survey of Indian NLP Datasets, Corpora, and Resources

**Authors:** Raghvendra Kumar, Devankar Raj, Sriparna Saha

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18423v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18423v1)

**Summary:** India's linguistic landscape, spanning 22 scheduled languages and hundreds of marginalized dialects, has driven rapid growth in NLP datasets, benchmarks, and pretrained models. However, no dedicated survey consolidates resources developed specifically for Indian languages. Existing reviews either focus on a few high-resource languages or subsume Indian languages within broader multilingual settings, limiting coverage of low-resource and culturally diverse varieties. To address this gap, we prese...

---

### 19. Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning

**Authors:** Hen Davidov, Nachshon Cohen, Oren Kalinsky, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18419v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18419v1)

**Summary:** Large language models (LLMs) using chain-of-thought reasoning often waste substantial compute by producing long, incorrect responses. Abstention can mitigate this by withholding outputs unlikely to be correct. While most abstention methods decide to withhold outputs before or after generation, dynamic mid-generation abstention considers early termination of unpromising reasoning traces at each token position. Prior work has explored empirical variants of this idea, but principled guidance for th...

---

### 20. StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning

**Authors:** Daoyu Wang, Qingchuan Li, Mingyue Cheng, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18401v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18401v1)

**Summary:** General agents have given rise to phenomenal applications such as OpenClaw and Claude Code. As these agent systems (a.k.a. Harnesses) strive for bolder goals, they demand increasingly stronger agentic capabilities from foundation Large Language Models (LLMs). Agentic Reinforcement Learning (RL) is emerging as a central post-training paradigm for empowering LLMs with these capabilities and is playing an increasingly pivotal role in agent training. Unlike single-turn token-level alignment or reaso...

---

### 21. AlphaContext: An Evolutionary Tree-based Psychometric Context Generator for Creativity Assessment

**Authors:** Yixuan Wang, Yue Huang, Hong Qian, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18398v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18398v1)

**Summary:** Creativity has become a core competence in the era of LLMs and human-AI collaboration, underpinning innovation in real-world problem solving. Crucially, the systematic improvement of creativity necessitates scientifically valid assessment instruments. Psychometric research recognizes context-based assessment as an effective way to measure creative thinking. However, high-quality expert-designed contexts remain scarce. Existing LLM-based generators often struggle with insufficient assessment cues...

---

### 22. River-LLM: Large Language Model Seamless Exit Based on KV Share

**Authors:** Yingtao Shen, An Zou

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18396v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18396v1)

**Summary:** Large Language Models (LLMs) have demonstrated exceptional performance across diverse domains but are increasingly constrained by high inference latency. Early Exit has emerged as a promising solution to accelerate inference by dynamically bypassing redundant layers. However, in decoder-only architectures, the efficiency of Early Exit is severely bottlenecked by the KV Cache Absence problem, where skipped layers fail to provide the necessary historical states for subsequent tokens. Existing solu...

---

### 23. Understanding the Prompt Sensitivity

**Authors:** Yang Liu, Chenhui Chu

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18389v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18389v1)

**Summary:** Prompt sensitivity, which refers to how strongly the output of a large language model (LLM) depends on the exact wording of its input prompt, raises concerns among users about the LLM's stability and reliability. In this work, we consider LLMs as multivariate functions and perform a first-order Taylor expansion, thereby analyzing the relationship between meaning-preserving prompts, their gradients, and the log probabilities of the model's next token. We derive an upper bound on the difference be...

---

### 24. IceBreaker for Conversational Agents: Breaking the First-Message Barrier with Personalized Starters

**Authors:** Hongwei Zheng, Weiqi Wu, Zhengjia Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18375v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18375v1)

**Summary:** Conversational agents, such as ChatGPT and Doubao, have become essential daily assistants for billions of users. To further enhance engagement, these systems are evolving from passive responders to proactive companions. However, existing efforts focus on activation within ongoing dialogues, while overlooking a key real-world bottleneck. In the conversation initiation stage, users may have a vague need but no explicit query intent, creating a first-message barrier where the conversation holds bef...

---

### 25. ArbGraph: Conflict-Aware Evidence Arbitration for Reliable Long-Form Retrieval-Augmented Generation

**Authors:** Qingying Niu, Yuhao Wang, Ruiyang Ren, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18362v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18362v1)

**Summary:** Retrieval-augmented generation (RAG) remains unreliable in long-form settings, where retrieved evidence is noisy or contradictory, making it difficult for RAG pipelines to maintain factual consistency. Existing approaches focus on retrieval expansion or verification during generation, leaving conflict resolution entangled with generation. To address this limitation, we propose ArbGraph, a framework for pre-generation evidence arbitration in long-form RAG that explicitly resolves factual conflict...

---

### 26. Omni-Embed-Audio: Leveraging Multimodal LLMs for Robust Audio-Text Retrieval

**Authors:** HaeJun Yoo, Yongseop Shin, Insung Lee, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18360v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18360v1)

**Summary:** Audio-text retrieval systems based on Contrastive Language-Audio Pretraining (CLAP) achieve strong performance on traditional benchmarks; however, these benchmarks rely on caption-style queries that differ substantially from real-world search behavior, limiting their assessment of practical retrieval robustness. We present Omni-Embed-Audio (OEA), a retrieval-oriented encoder leveraging multimodal LLMs with native audio understanding. To systematically evaluate robustness beyond caption-style que...

---

### 27. ComPASS: Towards Personalized Agentic Social Support via Tool-Augmented Companionship

**Authors:** Zhaopei Huang, Yanfeng Jia, Jiayi Zhao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18356v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18356v1)

**Summary:** Developing compassionate interactive systems requires agents to not only understand user emotions but also provide diverse, substantive support. While recent works explore empathetic dialogue generation, they remain limited in response form and content, struggling to satisfy diverse needs across users and contexts. To address this, we explore empowering agents with external tools to execute diverse actions. Grounded in the psychological concept of "social support", this paradigm delivers substan...

---

### 28. PRISMA: Preference-Reinforced Self-Training Approach for Interpretable Emotionally Intelligent Negotiation Dialogues

**Authors:** Prajwal Vijay Kajare, Priyanshu Priya, Bikash Santra, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18354v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18354v1)

**Summary:** Emotion plays a pivotal role in shaping negotiation outcomes, influencing trust, cooperation, and long-term relationships. Developing negotiation dialog systems that can recognize and respond strategically to emotions is, therefore, essential to create more effective human-centered interactions. Beyond generating emotionally appropriate responses, interpretability - understanding how a system generates a particular emotion-aware response, is critical for fostering reliability and building rappor...

---

### 29. HiGMem: A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents

**Authors:** Shuqi Cao, Jingyi He, Fei Tan

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18349v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18349v1)

**Summary:** Long-term conversational large language model (LLM) agents require memory systems that can recover relevant evidence from historical interactions without overwhelming the answer stage with irrelevant context. However, existing memory systems, including hierarchical ones, still often rely solely on vector similarity for retrieval. It tends to produce bloated evidence sets: adding many superficially similar dialogue turns yields little additional recall, but lowers retrieval precision, increases a...

---

### 30. Multilingual Training and Evaluation Resources for Vision-Language Models

**Authors:** Daniela Baiamonte, Elena Fano, Matteo Gabburo, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18347v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18347v1)

**Summary:** Vision Language Models (VLMs) achieved rapid progress in the recent years. However, despite their growth, VLMs development is heavily grounded on English, leading to two main limitations: (i) the lack of multilingual and multimodal datasets for training, and (ii) the scarcity of comprehensive evaluation benchmarks across languages. In this work, we address these gaps by introducing a new comprehensive suite of resources for VLMs training and evaluation spanning five European languages (English, ...

---

### 31. FregeLogic at SemEval 2026 Task 11: A Hybrid Neuro-Symbolic Architecture for Content-Robust Syllogistic Validity Prediction

**Authors:** Adewale Akinfaderin, Nafi Diallo

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18328v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18328v1)

**Summary:** We present FregeLogic, a hybrid neuro-symbolic system for SemEval-2026 Task 11 (Subtask 1), which addresses syllogistic validity prediction while reducing content effects on predictions. Our approach combines an ensemble of five LLM classifiers, spanning three open-weights models (Llama 4 Maverick, Llama 4 Scout, and Qwen3-32B) paired with varied prompting strategies, with a Z3 SMT solver that serves as a formal logic tiebreaker. The central hypothesis is that LLM disagreement within the ensembl...

---

### 32. PARM: Pipeline-Adapted Reward Model

**Authors:** Xingyu Fan, Wei Shao, Jiacheng Liu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18327v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18327v1)

**Summary:** Reward models (RMs) are central to aligning large language models (LLMs) with human preferences, powering RLHF and advanced decoding strategies. While most prior work focuses on single-step generation, real-world applications increasingly adopt multi-stage LLM pipelines, where effective reward guidance remains underexplored. We investigate this through code generation for combinatorial optimization, constructing a pipeline that integrates reward models into both formulation and solution stages. ...

---

### 33. On the Importance and Evaluation of Narrativity in Natural Language AI Explanations

**Authors:** Mateusz Cedro, David Martens

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18311v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18311v1)

**Summary:** Explainable AI (XAI) aims to make the behaviour of machine learning models interpretable, yet many explanation methods remain difficult to understand. The integration of Natural Language Generation into XAI aims to deliver explanations in textual form, making them more accessible to practitioners. Current approaches, however, largely yield static lists of feature importances. Although such explanations indicate what influences the prediction, they do not explain why the prediction occurs. In thi...

---

### 34. Reasoning Models Know What's Important, and Encode It in Their Activations

**Authors:** Yaniv Nikankin, Martin Tutek, Tomer Ashuach, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18307v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18307v1)

**Summary:** Language models often solve complex tasks by generating long reasoning chains, consisting of many steps with varying importance. While some steps are crucial for generating the final answer, others are removable. Determining which steps matter most, and why, remains an open question central to understanding how models process reasoning. We investigate if this question is best approached through model internals or through tokens of the reasoning chain itself. We find that model activations contai...

---

### 35. Exploring Concreteness Through a Figurative Lens

**Authors:** Saptarshi Ghosh, Tianyu Jiang

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18296v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18296v1)

**Summary:** Static concreteness ratings are widely used in NLP, yet a word's concreteness can shift with context, especially in figurative language such as metaphor, where common concrete nouns can take abstract interpretations. While such shifts are evident from context, it remains unclear how LLMs understand concreteness internally. We conduct a layer-wise and geometric analysis of LLM hidden representations across four model families, examining how models distinguish literal vs figurative uses of the sam...

---

### 36. An Existence Proof for Neural Language Models That Can Explain Garden-Path Effects via Surprisal

**Authors:** Ryo Yoshida, Shinnosuke Isono, Taiga Someya, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18293v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18293v1)

**Summary:** Surprisal theory hypothesizes that the difficulty of human sentence processing increases linearly with surprisal, the negative log-probability of a word given its context. Computational psycholinguistics has tested this hypothesis using language models (LMs) as proxies for human prediction. While surprisal derived from recent neural LMs generally captures human processing difficulty on naturalistic corpora that predominantly consist of simple sentences, it severely underestimates processing diff...

---

### 37. Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence

**Authors:** Guanting Dong, Junting Lu, Junjie Huang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18292v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18292v1)

**Summary:** Large language models are increasingly expected to serve as general-purpose agents that interact with external, stateful tool environments. The Model Context Protocol (MCP) and broader agent skills offer a unified interface for connecting agents with scalable real-world services, but training robust agents remains limited by the lack of realistic environments and principled mechanisms for life-long learning. In this paper, we present \textbf{Agent-World}, a self-evolving training arena for advan...

---

### 38. DocQAC: Adaptive Trie-Guided Decoding for Effective In-Document Query Auto-Completion

**Authors:** Rahul Mehta, Kavin R, Indrajit Pal, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18257v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18257v1)

**Summary:** Query auto-completion (QAC) has been widely studied in the context of web search, yet remains underexplored for in-document search, which we term DocQAC. DocQAC aims to enhance search productivity within long documents by helping users craft faster, more precise queries, even for complex or hard-to-spell terms. While global historical queries are available to both WebQAC and DocQAC, DocQAC uniquely accesses document-specific context, including the current document's content and its specific hist...

---

### 39. Where Do Self-Supervised Speech Models Become Unfair?

**Authors:** Felix Herron, Maja Hjuler, Solange Rossato, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18249v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18249v1)

**Summary:** Speech encoder models are known to model members of some speaker groups (SGs) better than others. However, there has been little work in establishing why this occurs on a technological level. To our knowledge, we present the first layerwise fairness analysis of pretrained self-supervised speech encoder models (S3Ms), probing each embedding layer for speaker identification (SID) automatic speech recognition (ASR). We find S3Ms produce embeddings biased against certain SGs for both tasks, starting...

---

### 40. Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection

**Authors:** Thamilvendhan Munirathinam

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18248v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18248v1)

**Summary:** Current open-source prompt-injection detectors converge on two architectural choices: regular-expression pattern matching and fine-tuned transformer classifiers. Both share failure modes that recent work has made concrete. Regular expressions miss paraphrased attacks. Fine-tuned classifiers are vulnerable to adaptive adversaries: a 2025 NAACL Findings study reported that eight published indirect-injection defenses were bypassed with greater than fifty percent attack success rates under adaptive ...

---

### 41. Negative Advantage Is a Double-Edged Sword: Calibrating Advantage in GRPO for Deep Search

**Authors:** Jiayi Wu, Ruobing Xie, Zeqian Huang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18235v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18235v1)

**Summary:** Deep search agents can autonomously initiate multi-turn interactions with search engines, thereby exhibiting strong question-answering capabilities. Such performance critically relies on Group Relative Policy Optimization (GRPO) as its core training algorithm. However, GRPO still faces several challenges in deep search settings. First, there exists a substantial mismatch between the correctness of intermediate steps and the reward signal, causing numerous correct intermediate steps to be incorre...

---

### 42. Model in Distress: Sentiment Analysis on French Synthetic Social Media

**Authors:** Pierre-Carl Langlais, Pavel Chizhov, Yannick Detrois, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18226v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18226v1)

**Summary:** Automated analysis of customer feedback on social media is hindered by three challenges: the high cost of annotated training data, the scarcity of evaluation sets, especially in multilingual settings, and privacy concerns that prevent data sharing and reproducibility. We address these issues by developing a generalizable synthetic data generation pipeline applied to a case study on customer distress detection in French public transportation. Our approach utilizes backtranslation with fine-tuned ...

---

### 43. Hard to Be Heard: Phoneme-Level ASR Analysis of Phonologically Complex, Low-Resource Endangered Languages

**Authors:** V. S. D. S. Mahesh Akavarapu, Michael Daniel, Gerhard Jäger

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18204v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18204v1)

**Summary:** We present a phoneme-level analysis of automatic speech recognition (ASR) for two low-resourced and phonologically complex East Caucasian languages, Archi and Rutul, based on curated and standardized speech-transcript resources totaling approximately 50 minutes and 1 hour 20 minutes of audio, respectively. Existing recordings and transcriptions are consolidated and processed into a form suitable for ASR training and evaluation. We evaluate several state-of-the-art audio and audio-language models...

---

### 44. Multiplication in Multimodal LLMs: Computation with Text, Image, and Audio Inputs

**Authors:** Samuel G. Balter, Ethan Jerzak, Connor T. Jerzak

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18203v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18203v1)

**Summary:** Multimodal LLMs can accurately perceive numerical content across modalities yet fail to perform exact multi-digit multiplication when the identical underlying arithmetic problem is presented as numerals, number words, images, or in audio form. Because existing benchmarks often lack systematically paired instances across modalities, it remains difficult to compare genuine arithmetic limits within and across model families. We therefore introduce a controlled multimodal multiplication benchmark th...

---

### 45. Linear-Time and Constant-Memory Text Embeddings Based on Recurrent Language Models

**Authors:** Tobias Grantner, Emanuel Sallinger, Martin Flechl

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18199v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18199v1)

**Summary:** Transformer-based embedding models suffer from quadratic computational and linear memory complexity, limiting their utility for long sequences. We propose recurrent architectures as an efficient alternative, introducing a vertically chunked inference strategy that enables fast embedding generation with memory usage that becomes constant in the input length once it exceeds the vertical chunk size. By fine-tuning Mamba2 models, we demonstrate their viability as general-purpose text embedders, achi...

---

### 46. Audio-DeepThinker: Progressive Reasoning-Aware Reinforcement Learning for High-Quality Chain-of-Thought Emergence in Audio Language Models

**Authors:** Xiang He, Chenxing Li, Jinting Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18187v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18187v1)

**Summary:** Large Audio-Language Models (LALMs) have made significant progress in audio understanding, yet they primarily operate as perception-and-answer systems without explicit reasoning processes. Existing methods for enhancing audio reasoning rely either on supervised chain-of-thought (CoT) fine-tuning, which is limited by training data quality, or on reinforcement learning (RL) with coarse rewards that do not directly evaluate reasoning quality. As a result, the generated reasoning chains often appear...

---

### 47. STaD: Scaffolded Task Design for Identifying Compositional Skill Gaps in LLMs

**Authors:** Sungeun An, Swanand Ravindra Kadhe, Shailja Thakur, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18177v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18177v1)

**Summary:** Benchmarks are often used as a standard to understand LLM capabilities in different domains. However, aggregate benchmark scores provide limited insight into compositional skill gaps of LLMs and how to improve them. To make these weaknesses visible, we propose Scaffolded Task Design (STaD) framework. STaD generates controlled variations of benchmark tasks based on the concept of scaffolding, which introduces structured, incremental support in a step-by-step manner. Rather than inspecting failure...

---

### 48. Copy-as-Decode: Grammar-Constrained Parallel Prefill for LLM Editing

**Authors:** Ziyang Liu

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18170v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18170v1)

**Summary:** LLMs edit text and code by autoregressively regenerating the full output, even when most tokens appear verbatim in the input. We study Copy-as-Decode, a decoding-layer mechanism that recasts edit generation as structured decoding over a two-primitive grammar: <copy lines="i-j"/> references an input line range, <gen>...</gen> emits new content. A token-level FSM guarantees syntactic validity, and a serving-layer primitive updates the KV cache for each copy span via a single parallel-prefill forwa...

---

### 49. Beyond Reproduction: A Paired-Task Framework for Assessing LLM Comprehension and Creativity in Literary Translation

**Authors:** Ran Zhang, Steffen Eger, Arda Tezcan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18169v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18169v1)

**Summary:** Large language models (LLMs) are increasingly used for creative tasks such as literary translation. Yet translational creativity remains underexplored and is rarely evaluated at scale, while source-text comprehension is typically studied in isolation, despite the fact that, in professional translation, comprehension and creativity are tightly intertwined. We address these gaps with a paired-task framework applied to literary excerpts from 11 books. Task 1 assesses source-text comprehension, and ...

---

### 50. MM-JudgeBias: A Benchmark for Evaluating Compositional Biases in MLLM-as-a-Judge

**Authors:** Sua Lee, Sanghee Park, Jinbae Im

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18164v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18164v1)

**Summary:** Multimodal Large Language Models (MLLMs) have been increasingly used as automatic evaluators-a paradigm known as MLLM-as-a-Judge. However, their reliability and vulnerabilities to biases remain underexplored. We find that many MLLM judges fail to reliably integrate key visual or textual cues, yielding unreliable evaluations when evidence is missing or mismatched, and exhibiting instability under semantically irrelevant perturbations. To address this, we systematically define Compositional Bias i...

---

## cs.CV

**50 papers**

### 1. MUA: Mobile Ultra-detailed Animatable Avatars

**Authors:** Heming Zhu, Guoxing Sun, Marc Habermann

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18583v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18583v1)

**Summary:** Building photorealistic, animatable full-body digital humans remains a longstanding challenge in computer graphics and vision. Recent advances in animatable avatar modeling have largely progressed along two directions: improving the fidelity of dynamic geometry and appearance, or reducing computational complexity to enable deployment on resource-constrained platforms, e.g., VR headsets. However, existing approaches fail to achieve both goals simultaneously: Ultra-high-fidelity avatars typically ...

---

### 2. ReCap: Lightweight Referential Grounding for Coherent Story Visualization

**Authors:** Aditya Arora, Akshita Gupta, Pau Rodriguez, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18575v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18575v1)

**Summary:** Story Visualization aims to generate a sequence of images that faithfully depicts a textual narrative that preserve character identity, spatial configuration, and stylistic coherence as the narratives unfold. Maintaining such cross-frame consistency has traditionally relied on explicit memory banks, architectural expansion, or auxiliary language models, resulting in substantial parameter growth and inference overhead. We introduce ReCap, a lightweight consistency framework that improves characte...

---

### 3. T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability

**Authors:** Savya Khosla, Sethuraman T, Aryan Chadha, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18573v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18573v1)

**Summary:** Despite recent progress, vision-language encoders struggle with two core limitations: (1) weak alignment between language and dense vision features, which hurts tasks like open-vocabulary semantic segmentation; and (2) high token counts for fine-grained visual representations, which limits scalability to long videos. This work addresses both limitations. We propose T-REN (Text-aligned Region Encoder Network), an efficient encoder that maps visual data to a compact set of text-aligned region-leve...

---

### 4. Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale

**Authors:** A. Sophia Koepke, Daniil Zverev, Shiry Ginosar, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18572v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18572v1)

**Summary:** The Platonic Representation Hypothesis suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If true, this has significant implications for whether modality choice matters at all. We show that the experimental evidence for this hypothesis is fragile and depends critically on the evaluation regime. Alignment is measured using mutual nearest neighbors on small datasets ($\approx$1K samples) and...

---

### 5. MultiWorld: Scalable Multi-Agent Multi-View Video World Models

**Authors:** Haoyu Wu, Jiwen Yu, Yingtian Zou, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18564v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18564v1)

**Summary:** Video world models have achieved remarkable success in simulating environmental dynamics in response to actions by users or agents. They are modeled as action-conditioned video generation models that take historical frames and current actions as input to predict future frames. Yet, most existing approaches are limited to single-agent scenarios and fail to capture the complex interactions inherent in real-world multi-agent systems. We present \textbf{MultiWorld}, a unified framework for multi-age...

---

### 6. AnchorSeg: Language Grounded Query Banks for Reasoning Segmentation

**Authors:** Rui Qian, Chuanhang Deng, Qiang Huang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18562v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18562v1)

**Summary:** Reasoning segmentation requires models to ground complex, implicit textual queries into precise pixel-level masks. Existing approaches rely on a single segmentation token $\texttt{<SEG>}$, whose hidden state implicitly encodes both semantic reasoning and spatial localization, limiting the model's ability to explicitly disentangle what to segment from where to segment. We introduce AnchorSeg, which reformulates reasoning segmentation as a structured conditional generation process over image token...

---

### 7. SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy

**Authors:** Wei Yao, Haohan Ma, Hongwen Zhang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18557v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18557v1)

**Summary:** Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human...

---

### 8. Advancing Vision Transformer with Enhanced Spatial Priors

**Authors:** Qihang Fan, Huaibo Huang, Mingrui Chen, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18549v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18549v1)

**Summary:** In recent years, the Vision Transformer (ViT) has garnered significant attention within the computer vision community. However, the core component of ViT, Self-Attention, lacks explicit spatial priors and suffers from quadratic computational complexity, limiting its applicability. To address these issues, we have proposed RMT, a robust vision backbone with explicit spatial priors for general purposes. RMT utilizes Manhattan distance decay to introduce spatial information and employs a horizontal...

---

### 9. MetaCloak-JPEG: JPEG-Robust Adversarial Perturbation for Preventing Unauthorized DreamBooth-Based Deepfake Generation

**Authors:** Tanjim Rahaman Fardin, S M Zunaid Alam, Mahadi Hasan Fahim, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18537v1)

**Summary:** The rapid progress of subject-driven text-to-image synthesis, and in particular DreamBooth, has enabled a consent-free deepfake pipeline: an adversary needs only 4-8 publicly available face images to fine-tune a personalized diffusion model and produce photorealistic harmful content. Current adversarial face-protection systems -- PhotoGuard, Anti-DreamBooth, and MetaCloak -- perturb user images to disrupt surrogate fine-tuning, but all share a structural blindness: none backpropagates gradients ...

---

### 10. UDM-GRPO: Stable and Efficient Group Relative Policy Optimization for Uniform Discrete Diffusion Models

**Authors:** Jiaqi Wang, Haoge Deng, Ting Pan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18518v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18518v1)

**Summary:** Uniform Discrete Diffusion Model (UDM) has recently emerged as a promising paradigm for discrete generative modeling; however, its integration with reinforcement learning remains largely unexplored. We observe that naively applying GRPO to UDM leads to training instability and marginal performance gains. To address this, we propose \Ours, the first framework to integrate UDM with RL. Our method is guided by two key insights: (i) treating the final clean sample as the action provides more accurat...

---

### 11. S2H-DPO: Hardness-Aware Preference Optimization for Vision-Language Models

**Authors:** Nitish Shukla, Surgan Jandial, Arun Ross

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18512v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18512v1)

**Summary:** Vision-Language Models (VLMs) have demonstrated remarkable progress in single-image understanding, yet effective reasoning across multiple images remains challenging. We identify a critical capability gap in existing multi-image alignment approaches: current methods focus primarily on localized reasoning with pre-specified image indices (``Look at Image 3 and...''), bypassing the essential skills of global visual search and autonomous cross-image comparison. To address this limitation, we introd...

---

### 12. OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation

**Authors:** Jinghui Lu, Jiayi Guan, Zhijian Huang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18486v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18486v1)

**Summary:** Chain-of-Thought (CoT) reasoning has become a powerful driver of trajectory prediction in VLA-based autonomous driving, yet its autoregressive nature imposes a latency cost that is prohibitive for real-time deployment. Latent CoT methods attempt to close this gap by compressing reasoning into continuous hidden states, but consistently fall short of their explicit counterparts. We suggest that this is due to purely linguistic latent representations compressing a symbolic abstraction of the world,...

---

### 13. XEmbodied: A Foundation Model with Enhanced Geometric and Physical Cues for Large-Scale Embodied Environments

**Authors:** Kangan Qian, ChuChu Xie, Yang Zhong, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18484v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18484v1)

**Summary:** Vision-Language-Action (VLA) models drive next-generation autonomous systems, but training them requires scalable, high-quality annotations from complex environments. Current cloud pipelines rely on generic vision-language models (VLMs) that lack geometric reasoning and domain semantics due to their 2D image-text pretraining. To address this mismatch, we propose XEmbodied, a cloud-side foundation model that endows VLMs with intrinsic 3D geometric awareness and interaction with physical cues (e.g...

---

### 14. SemLT3D: Semantic-Guided Expert Distillation for Camera-only Long-Tailed 3D Object Detection

**Authors:** Hao Vo, Khoa Vo, Thinh Phan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18476v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18476v1)

**Summary:** Camera-only 3D object detection has emerged as a cost-effective and scalable alternative to LiDAR for autonomous driving, yet existing methods primarily prioritize overall performance while overlooking the severe long-tail imbalance inherent in real-world datasets. In practice, many rare but safety-critical categories such as children, strollers, or emergency vehicles are heavily underrepresented, leading to biased learning and degraded performance. This challenge is further exacerbated by prono...

---

### 15. Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation

**Authors:** Tianshi Cao, Jiawei Ren, Yuxuan Zhang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18468v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18468v1)

**Summary:** Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge, we present Asset Harvester, an image-to-3D model and end-to-end pipeline that ...

---

### 16. Progressive Online Video Understanding with Evidence-Aligned Timing and Transparent Decisions

**Authors:** Kecheng Zhang, Zongxin Yang, Mingfei Han, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18459v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18459v1)

**Summary:** Visual agents operating in the wild must respond to queries precisely when sufficient evidence first appears in a video stream, a critical capability that is overlooked by conventional video LLMs evaluated in offline settings. The shift to an online, streaming paradigm introduces significant challenges: a lack of decision transparency, the difficulty of aligning response timing with visual evidence, and the need to maintain a global, causally consistent understanding under tight computational bu...

---

### 17. ESsEN: Training Compact Discriminative Vision-Language Transformers in a Low-Resource Setting

**Authors:** Clayton Fields, Casey Kennington

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18452v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18452v1)

**Summary:** Vision-language modeling is rapidly increasing in popularity with an ever expanding list of available models. In most cases, these vision-language models have parameters in the tens of billions, which is necessary for some needs, but in many cases smaller models are necessary (e.g., on edge devices or independent robotic platforms). Unfortunately, there is little research in producing light-weight models or in training them with small datasets. Inspired by the language learning progression and d...

---

### 18. ProtoCLIP: Prototype-Aligned Latent Refinement for Robust Zero-Shot Chest X-Ray Classification

**Authors:** Florian Kittler, Sheethal Bhat, Andreas Maier

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18444v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18444v1)

**Summary:** Zero-shot vision-language models (VLMs) have shown promise for chest radiograph classification, but their performance is often limited by confounding label co-occurrence, long-tail class imbalance, and transfer instability under domain shift. We propose ProtoCLIP, a refinement strategy for CLIP-style VLMs that improves zero-shot discrimination through targeted data curation and distilled anchor alignment. Specifically, we construct pathology-focused training subsets with curated negative samples...

---

### 19. Revisiting Change VQA in Remote Sensing with Structured and Native Multimodal Qwen Models

**Authors:** Yakoub Bazi, Mohamad M. Al Rahhal, Mansour Zuair, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18429v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18429v1)

**Summary:** Change visual question answering (Change VQA) addresses the problem of answering natural-language questions about semantic changes between bi-temporal remote sensing (RS) images. Although vision-language models (VLMs) have recently been studied for temporal RS image understanding, Change VQA remains underexplored in the context of modern multimodal models. In this letter, we revisit the CDVQA benchmark using recent Qwen models under a unified low-rank adaptation (LoRA) setting. We compare Qwen3-...

---

### 20. MedProbeBench: Systematic Benchmarking at Deep Evidence Integration for Expert-level Medical Guideline

**Authors:** Jiyao Liu, Jianghan Shen, Sida Song, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18418v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18418v1)

**Summary:** Recent advances in deep research systems enable large language models to retrieve, synthesize, and reason over large-scale external knowledge. In medicine, developing clinical guidelines critically depends on such deep evidence integration. However, existing benchmarks fail to evaluate this capability in realistic workflows requiring multi-step evidence integration and expert-level judgment. To address this gap, we introduce MedProbeBench, the first benchmark leveraging high-quality clinical gui...

---

### 21. One-Step Diffusion with Inverse Residual Fields for Unsupervised Industrial Anomaly Detection

**Authors:** Boan Zhang, Wen Li, Guanhua Yu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18393v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18393v1)

**Summary:** Diffusion models have achieved outstanding performance in unsupervised industrial anomaly detection (uIAD) by learning a manifold of normal data under the common assumption that off-manifold anomalies are harder to generate, resulting in larger reconstruction errors in data space or lower probability densities in the tractable latent space. However, their iterative denoising and noising nature leads to slow inference. In this paper, we propose OSD-IRF, a novel one-step diffusion with inverse res...

---

### 22. Towards Robust Text-to-Image Person Retrieval: Multi-View Reformulation for Semantic Compensation

**Authors:** Chao Yuan, Yujian Zhao, Haoxuan Xu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18376v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18376v1)

**Summary:** In text-to-image person retrieval tasks, the diversity of natural language expressions and the implicitness of visual semantics often lead to the problem of Expression Drift, where semantically equivalent texts exhibit significant feature discrepancies in the embedding space due to phrasing variations, thereby degrading the robustness of image-text alignment. This paper proposes a semantic compensation framework (MVR) driven by Large Language Models (LLMs), which enhances cross-modal representat...

---

### 23. DSA-CycleGAN: A Domain Shift Aware CycleGAN for Robust Multi-Stain Glomeruli Segmentation

**Authors:** Zeeshan Nisar, Friedrich Feuerhake, Thomas Lampert

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18368v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18368v1)

**Summary:** A key challenge in segmentation in digital histopathology is inter- and intra-stain variations as it reduces model performance. Labelling each stain is expensive and time-consuming so methods using stain transfer via CycleGAN, have been developed for training multi-stain segmentation models using labels from a single stain. Nevertheless, CycleGAN tends to introduce noise during translation because of the one-to-many nature of some stain pairs, which conflicts with its cycle consistency loss. To ...

---

### 24. EAST: Early Action Prediction Sampling Strategy with Token Masking

**Authors:** Iva Sović, Ivan Martinović, Marin Oršić

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18367v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18367v1)

**Summary:** Early action prediction seeks to anticipate an action before it fully unfolds, but limited visual evidence makes this task especially challenging. We introduce EAST, a simple and efficient framework that enables a model to reason about incomplete observations. In our empirical study, we identify key components when training early action prediction models. Our key contribution is a randomized training strategy that samples a time step separating observed and unobserved video frames, enabling a si...

---

### 25. LBFTI: Layer-Based Facial Template Inversion for Identity-Preserving Fine-Grained Face Reconstruction

**Authors:** Zixuan Shen, Zhihua Xia, Kaikai Gan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18358v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18358v1)

**Summary:** In face recognition systems, facial templates are widely adopted for identity authentication due to their compliance with the data minimization principle. However, facial template inversion technologies have posed a severe privacy leakage risk by enabling face reconstruction from templates. This paper proposes a Layer-Based Facial Template Inversion (LBFTI) method to reconstruct identity-preserving fine-grained face images. Our scheme decomposes face images into three layers: foreground layers (...

---

### 26. AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation

**Authors:** Haoyue Tan, Shengnan Wang, Yulin Qiao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18348v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18348v1)

**Summary:** Video diffusion transformers (DiTs) suffer from prohibitive inference latency due to quadratic attention complexity. Existing sparse attention methods either overlook semantic similarity or fail to adapt to heterogeneous token distributions across layers, leading to model performance degradation. We propose AdaCluster, a training-free adaptive clustering framework that accelerates the generation of DiTs while preserving accuracy. AdaCluster applies an angle-similarity-preserving clustering metho...

---

### 27. Enhancing Glass Surface Reconstruction via Depth Prior for Robot Navigation

**Authors:** Jiamin Zheng, Jingwen Yu, Guangcheng Chen, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18336v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18336v1)

**Summary:** Indoor robot navigation is often compromised by glass surfaces, which severely corrupt depth sensor measurements. While foundation models like Depth Anything 3 provide excellent geometric priors, they lack an absolute metric scale. We propose a training-free framework that leverages depth foundation models as a structural prior, employing a robust local RANSAC-based alignment to fuse it with raw sensor depth. This naturally avoids contamination from erroneous glass measurements and recovers an a...

---

### 28. OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation

**Authors:** Lei Zhu, Xing Cai, Yingjie Chen, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18326v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18326v1)

**Summary:** Recent advancements in audio-video joint generation models have demonstrated impressive capabilities in content creation. However, generating high-fidelity human-centric videos in complex, real-world physical scenes remains a significant challenge. We identify that the root cause lies in the structural deficiencies of existing datasets across three dimensions: limited global scene and camera diversity, sparse interaction modeling (both person-person and person-object), and insufficient individua...

---

### 29. EVE: Verifiable Self-Evolution of MLLMs via Executable Visual Transformations

**Authors:** Yongrui Heng, Chaoya Jiang, Han Yang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18320v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18320v1)

**Summary:** Self-evolution of multimodal large language models (MLLMs) remains a critical challenge: pseudo-label-based methods suffer from progressive quality degradation as model predictions drift, while template-based methods are confined to a static set of transformations that cannot adapt in difficulty or diversity. We contend that robust, continuous self-improvement requires not only deterministic external feedback independent of the model's internal certainty, but also a mechanism to perpetually dive...

---

### 30. Denoise and Align: Diffusion-Driven Foreground Knowledge Prompting for Open-Vocabulary Temporal Action Detection

**Authors:** Sa Zhu, Wanqian Zhang, Lin Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18313v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18313v1)

**Summary:** Open-Vocabulary Temporal Action Detection (OV-TAD) aims to localize and classify action segments of unseen categories in untrimmed videos, where effective alignment between action semantics and video representations is critical for accurate detection. However, existing methods struggle to mitigate the semantic imbalance between concise, abstract action labels and rich, complex video contents, inevitably introducing semantic noise and misleading cross-modal alignment. To address this challenge, w...

---

### 31. Relative State Estimation using Event-Based Propeller Sensing

**Authors:** Ravi Kumar Thakur, Luis Granados Segura, Jan Klivan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18289v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18289v1)

**Summary:** Autonomous swarms of multi-Unmanned Aerial Vehicle (UAV) system requires an accurate and fast relative state estimation. Although monocular frame-based camera methods perform well in ideal conditions, they are slow, suffer scale ambiguity, and often struggle in visually challenging conditions. The advent of event cameras addresses these challenging tasks by providing low latency, high dynamic range, and microsecond-level temporal resolution. This paper proposes a framework for relative state est...

---

### 32. Spike-NVPT: Learning Robust Visual Prompts via Bio-Inspired Temporal Filtering and Discretization

**Authors:** Qiugang Zhan, Anning Jiang, Ran Tao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18284v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18284v1)

**Summary:** Pre-trained vision models have found widespread application across diverse domains. Prompt tuning-based methods have emerged as a parameter-efficient paradigm for adapting pre-trained vision models. While effective on standard benchmarks, the continuous and dense nature of learned prompts can lead to sensitivity against input noise, as the high-capacity prompts tend to overfit task-irrelevant details. To address this trade-off, we propose Spike-NVPT, a noise-robust visual prompt tuning method. S...

---

### 33. LiquidTAD: An Efficient Method for Temporal Action Detection via Liquid Neural Dynamics

**Authors:** Zepeng Sun, Naichuan Zheng, Hailun Xia, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18274v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18274v1)

**Summary:** Temporal Action Detection (TAD) in untrimmed videos is currently dominated by Transformer-based architectures. While high-performing, their quadratic computational complexity and substantial parameter redundancy limit deployment in resource-constrained environments. In this paper, we propose LiquidTAD, a novel parameter-efficient framework that replaces cumbersome self-attention layers with parallelized ActionLiquid blocks. Unlike traditional Liquid Neural Networks (LNNs) that suffer from sequen...

---

### 34. MARCO: Navigating the Unseen Space of Semantic Correspondence

**Authors:** Claudia Cuttano, Gabriele Trivigno, Carlo Masone, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18267v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18267v1)

**Summary:** Recent advances in semantic correspondence rely on dual-encoder architectures, combining DINOv2 with diffusion backbones. While accurate, these billion-parameter models generalize poorly beyond training keypoints, revealing a gap between benchmark performance and real-world usability, where queried points rarely match those seen during training. Building upon DINOv2, we introduce MARCO, a unified model for generalizable correspondence driven by a novel training framework that enhances both fine-...

---

### 35. Geometry-Guided 3D Visual Token Pruning for Video-Language Models

**Authors:** Han Li, Zehao Huang, Jiahui Fu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18260v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18260v1)

**Summary:** Multimodal large language models have demonstrated remarkable capabilities in 2D vision, motivating their extension to 3D scene understanding. Recent studies represent 3D scenes as 3D spatial videos composed of image sequences with depth and camera pose information, enabling pre-trained video-language models to perform 3D reasoning tasks. However, the large number of visual tokens in spatial videos remains a major bottleneck for efficient inference and context management. Existing pruning method...

---

### 36. Long-Text-to-Image Generation via Compositional Prompt Decomposition

**Authors:** Jen-Yuan Huang, Tong Lin, Yilun Du

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18258v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18258v1)

**Summary:** While modern text-to-image (T2I) models excel at generating images from intricate prompts, they struggle to capture the key details when the inputs are descriptive paragraphs. This limitation stems from the prevalence of concise captions that shape their training distributions. Existing methods attempt to bridge this gap by either fine-tuning T2I models on long prompts, which generalizes poorly to longer lengths; or by projecting the oversize inputs into normal-prompt space and compromising fide...

---

### 37. Domain-Specialized Object Detection via Model-Level Mixtures of Experts

**Authors:** Svetlana Pavlitska, Malte Stüven, Beyza Keskin, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18256v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18256v1)

**Summary:** Mixture-of-Experts (MoE) models provide a structured approach to combining specialized neural networks and offer greater interpretability than conventional ensembles. While MoEs have been successfully applied to image classification and semantic segmentation, their use in object detection remains limited due to challenges in merging dense and structured predictions. In this work, we investigate model-level mixtures of object detectors and analyze their suitability for improving performance and i...

---

### 38. Style-Based Neural Architectures for Real-Time Weather Classification

**Authors:** Hamed Ouattara, Pascal Houssam Salmane, Pierre Duthon, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18251v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18251v1)

**Summary:** In this paper, we present three neural network architectures designed for real-time classification of weather conditions (sunny, rain, snow, fog) from images. These models, inspired by recent advances in style transfer, aim to capture the stylistic elements present in images. One model, called "Multi-PatchGAN", is based on PatchGANs used in well-known architectures such as Pix2Pix and CycleGAN, but here adapted with multiple patch sizes for detection tasks. The second model, "Truncated ResNet50"...

---

### 39. Medical Image Understanding Improves Survival Prediction via Visual Instruction Tuning

**Authors:** Xixi Liu, Jorge Lazo, Andreas Hallqvist, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18250v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18250v1)

**Summary:** Accurate prognostication and risk estimation are essential for guiding clinical decision-making and optimizing patient management. While radiologist-assessed features from CT scans provide valuable indicators of disease severity and outcomes, interpreting such images requires expert knowledge, and translating rich visual information into textual summaries inevitably leads to information loss. In this work, we propose a vision-language framework for 3D CT image understanding that leverages large-...

---

### 40. Is SAM3 ready for pathology segmentation?

**Authors:** Qiuyu Kong, Shakiba Sharifi, Zanxi Ruan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18225v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18225v1)

**Summary:** Is Segment Anything Model 3 (SAM3) capable in segmenting Any Pathology Images? Digital pathology segmentation spans tissue-level and nuclei-level scales, where traditional methods often suffer from high annotation costs and poor generalization. SAM3 introduces Promptable Concept Segmentation, offering a potential automated interface via text prompts. With this work, we propose a systematic evaluation protocol to explore the capability space of SAM3 in a structured manner. Specifically, we evalua...

---

### 41. Instruction-as-State: Environment-Guided and State-Conditioned Semantic Understanding for Embodied Navigation

**Authors:** Zhen Liu, Yuhan Liu, Jinjun Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18223v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18223v1)

**Summary:** Vision-and-Language Navigation requires agents to follow natural-language instructions in visually changing environments. A central challenge is the dynamic entanglement between language and observations: the meaning of instruction shifts as the agent's field of view and spatial context evolve. However, many existing models encode the instruction as a static global representation, limiting their ability to adapt instruction meaning to the current visual context. We therefore model instruction un...

---

### 42. Memorize When Needed: Decoupled Memory Control for Spatially Consistent Long-Horizon Video Generation

**Authors:** Yanjun Guo, Zhengqiang Zhang, Pengfei Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18215v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18215v1)

**Summary:** Spatially consistent long-horizon video generation aims to maintain temporal and spatial consistency along predefined camera trajectories. Existing methods mostly entangle memory modeling with video generation, leading to inconsistent content during scene revisits and diminished generative capacity when exploring novel regions, even trained on extensive annotated data. To address these limitations, we propose a decoupled framework that separates memory conditioning from generation. Our approach ...

---

### 43. Towards Symmetry-sensitive Pose Estimation: A Rotation Representation for Symmetric Object Classes

**Authors:** Andreas Kriegler, Csaba Beleznai, Margrit Gelautz

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18208v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18208v1)

**Summary:** Symmetric objects are common in daily life and industry, yet their inherent orientation ambiguities that impede the training of deep learning networks for pose estimation are rarely discussed in the literature. To cope with these ambiguities, existing solutions typically require the design of specific loss functions and network architectures or resort to symmetry-invariant evaluation metrics. In contrast, we focus on the numeric representation of the rotation itself, modifying trigonometric iden...

---

### 44. A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting

**Authors:** Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18205v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18205v1)

**Summary:** Recent advances in neural rendering have introduced numerous 3D scene representations. Although standard computer vision metrics evaluate the visual quality of generated images, they often overlook the fidelity of surface geometry. This limitation is particularly critical in robotics, where accurate geometry is essential for tasks such as grasping and object manipulation. In this paper, we present an evaluation pipeline for neural rendering methods that focuses on geometric accuracy, along with ...

---

### 45. DiffuSAM: Diffusion Guided Zero-Shot Object Grounding for Remote Sensing Imagery

**Authors:** Geet Sethi, Panav Shah, Ashutosh Gandhe, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18201v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18201v1)

**Summary:** Diffusion models have emerged as powerful tools for a wide range of vision tasks, including text-guided image generation and editing. In this work, we explore their potential for object grounding in remote sensing imagery. We propose a hybrid pipeline that integrates diffusion-based localization cues with state-of-the-art segmentation models such as RemoteSAM and SAM3 to obtain more accurate bounding boxes. By leveraging the complementary strengths of generative diffusion models and foundational...

---

### 46. Attraction, Repulsion, and Friction: Introducing DMF, a Friction-Augmented Drifting Model

**Authors:** Arkadii Kazanskii, Tatiana Petrova, Konstantin Bagrianskii, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18194v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18194v1)

**Summary:** Drifting Models [Deng et al., 2026] train a one-step generator by evolving samples under a kernel-based drift field, avoiding ODE integration at inference. The original analysis leaves two questions open. The drift-field iteration admits a locally repulsive regime in a two-particle surrogate, and vanishing of the drift ($V_{p,q}\equiv 0$) is not known to force the learned distribution $q$ to match the target $p$. We derive a contraction threshold for the surrogate and show that a linearly-schedu...

---

### 47. CanonSLR: Canonical-View Guided Multi-View Continuous Sign Language Recognition

**Authors:** Xu Wang, Shengeng Tang, Wan Jiang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18184v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18184v1)

**Summary:** Continuous Sign Language Recognition (CSLR) has achieved remarkable progress in recent years; however, most existing methods are developed under single-view settings and thus remain insufficiently robust to viewpoint variations in real-world scenarios. To address this limitation, we propose CanonSLR, a canonical-view guided framework for multi-view CSLR. Specifically, we introduce a frontal-view-anchored teacher-student learning strategy, in which a teacher network trained on frontal-view data p...

---

### 48. Extending One-Step Image Generation from Class Labels to Text via Discriminative Text Representation

**Authors:** Chenxi Zhao, Chen Zhu, Xiaokun Feng, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18168v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18168v1)

**Summary:** Few-step generation has been a long-standing goal, with recent one-step generation methods exemplified by MeanFlow achieving remarkable results. Existing research on MeanFlow primarily focuses on class-to-image generation. However, an intuitive yet unexplored direction is to extend the condition from fixed class labels to flexible text inputs, enabling richer content creation. Compared to the limited class labels, text conditions pose greater challenges to the model's understanding capability, n...

---

### 49. Embedding Arithmetic: A Lightweight, Tuning-Free Framework for Post-hoc Bias Mitigation in Text-to-Image Models

**Authors:** Venkatesh Thirugnana Sambandham, Torsten Schön

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18167v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18167v1)

**Summary:** Modern text-to-image (T2I) models amplify harmful societal biases, challenging their ethical deployment. We introduce an inference-time method that reliably mitigates social bias while keeping prompt semantics and visual context (background, layout, and style) intact. This ensures context persistency and provides a controllable parameter to adjust mitigation strength, giving practitioners fine-grained control over fairness-coherence trade-offs. Using Embedding Arithmetic, we analyze how bias is ...

---

### 50. MM-JudgeBias: A Benchmark for Evaluating Compositional Biases in MLLM-as-a-Judge

**Authors:** Sua Lee, Sanghee Park, Jinbae Im

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18164v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18164v1)

**Summary:** Multimodal Large Language Models (MLLMs) have been increasingly used as automatic evaluators-a paradigm known as MLLM-as-a-Judge. However, their reliability and vulnerabilities to biases remain underexplored. We find that many MLLM judges fail to reliably integrate key visual or textual cues, yielding unreliable evaluations when evidence is missing or mismatched, and exhibiting instability under semantically irrelevant perturbations. To address this, we systematically define Compositional Bias i...

---

## cs.LG

**50 papers**

### 1. MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval

**Authors:** Shaden Alshammari, Kevin Wen, Abrar Zainal, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18584v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18584v1)

**Summary:** Mathematical problem solving remains a challenging test of reasoning for large language and multimodal models, yet existing benchmarks are limited in size, language coverage, and task diversity. We introduce MathNet, a high-quality, large-scale, multimodal, and multilingual dataset of Olympiad-level math problems together with a benchmark for evaluating mathematical reasoning in generative models and mathematical retrieval in embedding-based systems. MathNet spans 47 countries, 17 languages, and...

---

### 2. Sessa: Selective State Space Attention

**Authors:** Liubomyr Horbatko

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18580v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18580v1)

**Summary:** Modern sequence models are dominated by Transformers, where self-attention mixes information from the visible context in an input-dependent way. However, when retrieval is not sharp and attention remains diffuse over an effective support $S_{\mathrm{eff}}(t)$, the influence of any individual token is diluted, typically scaling as $O(1/S_{\mathrm{eff}}(t))$ and reaching $O(1/\ell)$ for old tokens in full-prefix settings. Structured state-space models process sequences recurrently through an expli...

---

### 3. Bounded Ratio Reinforcement Learning

**Authors:** Yunke Ao, Le Chen, Bruce D. Lee, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18578v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18578v1)

**Summary:** Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization...

---

### 4. When Can LLMs Learn to Reason with Weak Supervision?

**Authors:** Salman Rahman, Jingyan Shen, Anna Mordvina, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18574v1)

**Summary:** Large language models have achieved significant reasoning improvements through reinforcement learning with verifiable rewards (RLVR). Yet as model capabilities grow, constructing high-quality reward signals becomes increasingly difficult, making it essential to understand when RLVR can succeed under weaker forms of supervision. We conduct a systematic empirical study across diverse model families and reasoning domains under three weak supervision settings: scarce data, noisy rewards, and self-su...

---

### 5. Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale

**Authors:** A. Sophia Koepke, Daniil Zverev, Shiry Ginosar, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18572v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18572v1)

**Summary:** The Platonic Representation Hypothesis suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If true, this has significant implications for whether modality choice matters at all. We show that the experimental evidence for this hypothesis is fragile and depends critically on the evaluation regime. Alignment is measured using mutual nearest neighbors on small datasets ($\approx$1K samples) and...

---

### 6. A multimodal and temporal foundation model for virtual patient representations at healthcare system scale

**Authors:** Andrew Zhang, Tong Ding, Sophia J. Wagner, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18570v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18570v1)

**Summary:** Modern medicine generates vast multimodal data across siloed systems, yet no existing model integrates the full breadth and temporal depth of the clinical record into a unified patient representation. We introduce Apollo, a multimodal temporal foundation model trained and evaluated on over three decades of longitudinal hospital records from a major US hospital system, composed of 25 billion records from 7.2 million patients, representing 28 distinct medical modalities and 12 major medical specia...

---

### 7. Revisiting Active Sequential Prediction-Powered Mean Estimation

**Authors:** Maria-Eleni Sfyraki, Jun-Kun Wang

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18569v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18569v1)

**Summary:** In this work, we revisit the problem of active sequential prediction-powered mean estimation, where at each round one must decide the query probability of the ground-truth label upon observing the covariates of a sample. Furthermore, if the label is not queried, the prediction from a machine learning model is used instead. Prior work proposed an elegant scheme that determines the query probability by combining an uncertainty-based suggestion with a constant probability that encodes a soft constr...

---

### 8. Latent Phase-Shift Rollback: Inference-Time Error Correction via Residual Stream Monitoring and KV-Cache Steering

**Authors:** Manan Gupta, Dhruv Kumar

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18567v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18567v1)

**Summary:** Large language models frequently commit unrecoverable reasoning errors mid-generation: once a wrong step is taken, subsequent tokens compound the mistake rather than correct it. We introduce $\textbf{Latent Phase-Shift Rollback}$ (LPSR): at each generation step, we monitor the residual stream at a critical layer lcrit, detect abrupt directional reversals (phase shifts) via a cosine-similarity $+$ entropy dual gate, and respond by rolling back the KV-cache and injecting a pre-computed steering ve...

---

### 9. Benchmarking System Dynamics AI Assistants: Cloud Versus Local LLMs on CLD Extraction and Discussion

**Authors:** Terry Leitch

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18566v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18566v1)

**Summary:** We present a systematic evaluation of large language model families -- spanning both proprietary cloud APIs and locally-hosted open-source models -- on two purpose-built benchmarks for System Dynamics AI assistance: the \textbf{CLD Leaderboard} (53 tests, structured causal loop diagram extraction) and the \textbf{Discussion Leaderboard} (interactive model discussion, feedback explanation, and model building coaching).   On CLD extraction, cloud models achieve 77--89\% overall pass rates; the bes...

---

### 10. ConforNets: Latents-Based Conformational Control in OpenFold3

**Authors:** Minji Lee, Colin Kalicki, Minkyu Jeon, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18559v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18559v1)

**Summary:** Models from the AlphaFold (AF) family reliably predict one dominant conformation for most well-ordered proteins but struggle to capture biologically relevant alternate states. Several efforts have focused on eliciting greater conformational variability through ad hoc inference-time perturbations of AF models or their inputs. Despite their progress, these approaches remain inefficient and fail to consistently recover major conformational modes. Here, we investigate both the optimal location and m...

---

### 11. GSQ: Highly-Accurate Low-Precision Scalar Quantization for LLMs via Gumbel-Softmax Sampling

**Authors:** Alireza Dadgarnia, Soroush Tabesh, Mahdi Nikdan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18556v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18556v1)

**Summary:** Weight quantization has become a standard tool for efficient LLM deployment, especially for local inference, where models are now routinely served at 2-3 bits per parameter. The state of the art is currently split into two sets of methods: simple scalar quantization techniques, such as GPTQ or AWQ, which are widely deployed but plateau in accuracy at 3-4 bits per parameter (bpp), and "second-generation" vector- or trellis-quantized methods, such as QTIP, GPTVQ and AQLM, which push the accuracy f...

---

### 12. A Note on TurboQuant and the Earlier DRIVE/EDEN Line of Work

**Authors:** Ran Ben-Basat, Yaniv Ben-Itzhak, Gal Mendelson, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18555v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18555v1)

**Summary:** This note clarifies the relationship between the recent TurboQuant work and the earlier DRIVE (NeurIPS 2021) and EDEN (ICML 2022) schemes. DRIVE is a 1-bit quantizer that EDEN extended to any $b>0$ bits per coordinate; we refer to them collectively as EDEN.   First, TurboQuant$_{\text{mse}}$ is a special case of EDEN obtained by fixing EDEN's scalar scale parameter to $S=1$. EDEN supports both biased and unbiased quantization, each optimized by a different $S$ (chosen via methods described in th...

---

### 13. Physics-Informed Neural Networks for Biological $2\mathrm{D}{+}t$ Reaction-Diffusion Systems

**Authors:** William Lavery, Jodie A. Cochrane, Christian Olesen, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18548v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18548v1)

**Summary:** Physics-informed neural networks (PINNs) provide a powerful framework for learning governing equations of dynamical systems from data. Biologically-informed neural networks (BINNs) are a variant of PINNs that preserve the known differential operator structure (e.g., reaction-diffusion) while learning constitutive terms via trainable neural subnetworks, enforced through soft residual penalties. Existing BINN studies are limited to $1\mathrm{D}{+}t$ reaction-diffusion systems and focus on forward ...

---

### 14. FUSE: Ensembling Verifiers with Zero Labeled Data

**Authors:** Joonhyuk Lee, Virginia Ma, Sarah Zhao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18547v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18547v1)

**Summary:** Verification of model outputs is rapidly emerging as a key primitive for both training and real-world deployment of large language models (LLMs). In practice, this often involves using imperfect LLM judges and reward models since ground truth acquisition can be time-consuming and expensive. We introduce Fully Unsupervised Score Ensembling (FUSE), a method for improving verification quality by ensembling verifiers without access to ground truth correctness labels. The key idea behind FUSE is to c...

---

### 15. Wasserstein Distributionally Robust Risk-Sensitive Estimation via Conditional Value-at-Risk

**Authors:** Feras Al Taha, Eilyan Bitar

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18546v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18546v1)

**Summary:** We propose a distributionally robust approach to risk-sensitive estimation of an unknown signal x from an observed signal y. The unknown signal and observation are modeled as random vectors whose joint probability distribution is unknown, but assumed to belong to a given type-2 Wasserstein ball of distributions, termed the ambiguity set. The performance of an estimator is measured according to the conditional value-at-risk (CVaR) of the squared estimation error. Within this framework, we study t...

---

### 16. Duality for the Adversarial Total Variation

**Authors:** Leon Bungert, Lucas Schmitt

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18540v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18540v1)

**Summary:** Adversarial training of binary classifiers can be reformulated as regularized risk minimization involving a nonlocal total variation. Building on this perspective, we establish a characterization of the subdifferential of this total variation using duality techniques. To achieve this, we derive a dual representation of the nonlocal total variation and a related integration of parts formula, involving a nonlocal gradient and divergence. We provide such duality statements both in the space of cont...

---

### 17. IDOBE: Infectious Disease Outbreak forecasting Benchmark Ecosystem

**Authors:** Aniruddha Adiga, Jingyuan Chou, Anshul Chiranth, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18521v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18521v1)

**Summary:** Epidemic forecasting has become an integral part of real-time infectious disease outbreak response. While collaborative ensembles composed of statistical and machine learning models have become the norm for real-time forecasting, standardized benchmark datasets for evaluating such methods are lacking. Further, there is limited understanding on performance of these methods for novel outbreaks with limited historical data. In this paper, we propose IDOBE, a curated collection of epidemiological ti...

---

### 18. UDM-GRPO: Stable and Efficient Group Relative Policy Optimization for Uniform Discrete Diffusion Models

**Authors:** Jiaqi Wang, Haoge Deng, Ting Pan, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18518v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18518v1)

**Summary:** Uniform Discrete Diffusion Model (UDM) has recently emerged as a promising paradigm for discrete generative modeling; however, its integration with reinforcement learning remains largely unexplored. We observe that naively applying GRPO to UDM leads to training instability and marginal performance gains. To address this, we propose \Ours, the first framework to integrate UDM with RL. Our method is guided by two key insights: (i) treating the final clean sample as the action provides more accurat...

---

### 19. Learning the Riccati solution operator for time-varying LQR via Deep Operator Networks

**Authors:** Jun Chen, Umberto Biccari, Junmin Wang

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18507v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18507v1)

**Summary:** We propose a computational framework for replacing the repeated numerical solution of differential Riccati equations in finite-horizon Linear Quadratic Regulator (LQR) problems by a learned operator surrogate. Instead of solving a nonlinear matrix-valued differential equation for each new system instance, we construct offline an approximation of the associated solution operator mapping time-dependent system parameters to the Riccati trajectory. The resulting model enables fast online evaluation ...

---

### 20. Too Correct to Learn: Reinforcement Learning on Saturated Reasoning Data

**Authors:** Zhenwen Liang, Yujun Zhou, Sidi Lu, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18493v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18493v1)

**Summary:** Reinforcement Learning (RL) enhances LLM reasoning, yet a paradox emerges as models scale: strong base models saturate standard benchmarks (e.g., MATH), yielding correct but homogeneous solutions. In such environments, the lack of failure cases causes the advantage signal in group-relative algorithms (e.g., GRPO) to vanish, driving policies into mode collapse. To address this, we propose Constrained Uniform Top-K Sampling (CUTS), a parameter-free decoding strategy enforcing structure-preserving ...

---

### 21. Barrier-enforced multi-objective optimization for direct point and sharp interval forecasting

**Authors:** Worachit Amnuaypongsa, Yotsapat Suparanonrat, Pana Wanitchollakit, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18492v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18492v1)

**Summary:** This paper proposes a multi-step probabilistic forecasting framework using a single neural-network based model to generate simultaneous point and interval forecasts. Our approach ensures non-crossing prediction intervals (PIs) through a model structure design that strictly satisfy a target coverage probability (PICP) while maximizing sharpness. Unlike existing methods that rely on manual weight tuning for scalarized loss functions, we treat point and PI forecasting as a multi-objective optimizat...

---

### 22. Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD

**Authors:** Nicholas Thumiger, Andrea Bartezzaghi, Mattia Rigotti, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18491v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18491v1)

**Summary:** Computational Fluid Dynamics (CFD) is central to race-car aerodynamic development, yet its cost -- tens of thousands of core-hours per high-fidelity evaluation -- severely limits the design space exploration feasible within realistic budgets. AI-based surrogate models promise to alleviate this bottleneck, but progress has been constrained by the limited complexity of public datasets, which are dominated by smoothed passenger-car shapes that fail to exercise surrogates on the thin, complex, highl...

---

### 23. Safe Control using Learned Safety Filters and Adaptive Conformal Inference

**Authors:** Sacha Huriot, Ihab Tabbara, Hussein Sibai

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18482v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18482v1)

**Summary:** Safety filters have been shown to be effective tools to ensure the safety of control systems with unsafe nominal policies. To address scalability challenges in traditional synthesis methods, learning-based approaches have been proposed for designing safety filters for systems with high-dimensional state and control spaces. However, the inevitable errors in the decisions of these models raise concerns about their reliability and the safety guarantees they offer. This paper presents Adaptive Confo...

---

### 24. Physics-Informed Neural Networks: A Didactic Derivation of the Complete Training Cycle

**Authors:** Abdeladhim Tahimi

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18481v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18481v1)

**Summary:** This paper is a step-by-step, self-contained guide to the complete training cycle of a Physics-Informed Neural Network (PINN) -- a topic that existing tutorials and guides typically delegate to automatic differentiation libraries without exposing the underlying algebra. Using a first-order initial value problem with a known analytical solution as a running example, we walk through every stage of the process: forward propagation of both the network output and its temporal derivative, evaluation o...

---

### 25. Multi-Scale Reversible Chaos Game Representation: A Unified Framework for Sequence Classification

**Authors:** Sarwan Ali, Taslim Murad

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18477v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18477v1)

**Summary:** Biological classification with interpretability remains a challenging task. For this, we introduce a novel encoding framework, Multi-Scale Reversible Chaos Game Representation (MS-RCGR), that transforms biological sequences into multi-resolution geometric representations with guaranteed reversibility. Unlike traditional sequence encoding methods, MS-RCGR employs rational arithmetic and hierarchical k-mer decomposition to generate scale-invariant features that preserve complete sequence informati...

---

### 26. Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts

**Authors:** Jacob Morrison, Sanjay Adhikesaven, Akshita Bhagia, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18473v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18473v1)

**Summary:** Extending a fully post-trained language model with new domain capabilities is fundamentally limited by monolithic training paradigms: retraining from scratch is expensive and scales poorly, while continued training often degrades existing capabilities. We present BAR (Branch-Adapt-Route), which trains independent domain experts, each through its own mid-training, supervised finetuning, and reinforcement learning pipeline, and composes them via a Mixture-of-Experts architecture with lightweight r...

---

### 27. NI Sampling: Accelerating Discrete Diffusion Sampling by Token Order Optimization

**Authors:** Enshu Liu, Xuefei Ning, Yu Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18471v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18471v1)

**Summary:** Discrete diffusion language models (dLLMs) have recently emerged as a promising alternative to traditional autoregressive approaches, offering the flexibility to generate tokens in arbitrary orders and the potential of parallel decoding. However, existing heuristic sampling strategies remain inefficient: they choose only a small part of tokens to sample at each step, leaving substantial room for improvement. In this work, we study the problem of token sampling order optimization and demonstrate ...

---

### 28. Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation

**Authors:** Tianshi Cao, Jiawei Ren, Yuxuan Zhang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18468v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18468v1)

**Summary:** Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge, we present Asset Harvester, an image-to-3D model and end-to-end pipeline that ...

---

### 29. An Integrated Deep-Learning Framework for Peptide-Protein Interaction Prediction and Target-Conditioned Peptide Generation with ConGA-PePPI and TC-PepGen

**Authors:** Chupei Tang, Junxiao Kong, Moyu Tang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18467v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18467v1)

**Summary:** Motivation: Peptide-protein interactions (PepPIs) are central to cellular regulation and peptide therapeutics, but experimental characterization remains too slow for large-scale screening. Existing methods usually emphasize either interaction prediction or peptide generation, leaving candidate prioritization, residue-level interpretation, and target-conditioned expansion insufficiently integrated. Results: We present an integrated framework for early-stage peptide screening that combines a partn...

---

### 30. Semantic Step Prediction: Multi-Step Latent Forecasting in LLM Reasoning Trajectories via Step Sampling

**Authors:** Yidi Yuan

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18464v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18464v1)

**Summary:** Semantic Tube Prediction (STP) leverages representation geometric to regularize LLM hidden-state trajectories toward locally linear geodesics during fine-tuning, thereby greatly improving data efficiency. The original STP recipe samples random token sub-spans, which is compatible with the base large language model (LLM) training architecture. Inspired by STP, we are interested to investigate whether the sampling position can further enhance the semantic structure of multi-step reasoning, and hen...

---

### 31. Using large language models for embodied planning introduces systematic safety risks

**Authors:** Tao Zhang, Kaixian Qu, Zhibin Li, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18463v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18463v1)

**Summary:** Large language models are increasingly used as planners for robotic systems, yet how safely they plan remains an open question. To evaluate safe planning systematically, we introduce DESPITE, a benchmark of 12,279 tasks spanning physical and normative dangers with fully deterministic validation. Across 23 models, even near-perfect planning ability does not ensure safety: the best-planning model fails to produce a valid plan on only 0.4% of tasks but produces dangerous plans on 28.3%. Among 18 op...

---

### 32. Learning Invariant Modality Representation for Robust Multimodal Learning from a Causal Inference Perspective

**Authors:** Sijie Mai, Shiqin Han

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18460v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18460v1)

**Summary:** Multimodal affective computing aims to predict humans' sentiment, emotion, intention, and opinion using language, acoustic, and visual modalities. However, current models often learn spurious correlations that harm generalization under distribution shifts or noisy modalities. To address this, we propose a causal modality-invariant representation (CmIR) learning framework for robust multimodal learning. At its core, we introduce a theoretically grounded disentanglement method that separates each ...

---

### 33. Random Matrix Theory of Early-Stopped Gradient Flow: A Transient BBP Scenario

**Authors:** Florentin Coeurdoux, Grégoire Ferré, Jean-Philippe Bouchaud

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18450v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18450v1)

**Summary:** Empirical studies of trained models often report a transient regime in which signal is detectable in a finite gradient descent time window before overfitting dominates. We provide an analytically tractable random-matrix model that reproduces this phenomenon for gradient flow in a linear teacher--student setting. In this framework, learning occurs when an isolated eigenvalue separates from a noisy bulk, before eventually disappearing in the overfitting regime. The key ingredient is anisotropy in ...

---

### 34. AutoPPA: Automated Circuit PPA Optimization via Contrastive Code-based Rule Library Learning

**Authors:** Chongxiao Li, Pengwei Jin, Di Huang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18445v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18445v1)

**Summary:** Performance, power, and area (PPA) optimization is a fundamental task in RTL design, requiring a precise understanding of circuit functionality and the relationship between circuit structures and PPA metrics. Recent studies attempt to automate this process using LLMs, but neither feedback-based nor knowledge-based methods are efficient enough, as they either design without any prior knowledge or rely heavily on human-summarized optimization rules.   In this paper, we propose AutoPPA, a fully aut...

---

### 35. ProtoCLIP: Prototype-Aligned Latent Refinement for Robust Zero-Shot Chest X-Ray Classification

**Authors:** Florian Kittler, Sheethal Bhat, Andreas Maier

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18444v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18444v1)

**Summary:** Zero-shot vision-language models (VLMs) have shown promise for chest radiograph classification, but their performance is often limited by confounding label co-occurrence, long-tail class imbalance, and transfer instability under domain shift. We propose ProtoCLIP, a refinement strategy for CLIP-style VLMs that improves zero-shot discrimination through targeted data curation and distilled anchor alignment. Specifically, we construct pathology-focused training subsets with curated negative samples...

---

### 36. Scalable Physics-Informed Neural Differential Equations and Data-Driven Algorithms for HVAC Systems

**Authors:** Hanfeng Zhai, Hongtao Qiao, Hassan Mansour, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18438v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18438v1)

**Summary:** We present a scalable, data-driven simulation framework for large-scale heating, ventilation, and air conditioning (HVAC) systems that couples physics-informed neural ordinary differential equations (PINODEs) with differential-algebraic equation (DAE) solvers. At the component level, we learn heat-exchanger dynamics using an implicit PINODE formulation that predicts conserved quantities (refrigerant mass $M_r$ and internal energy $E_\text{hx}$) as outputs, enabling physics-informed training via ...

---

### 37. Spectral bandits for smooth graph functions

**Authors:** Michal Valko, Rémi Munos, Branislav Kveton, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18420v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18420v1)

**Summary:** Smooth functions on graphs have wide applications in manifold and semi-supervised learning. In this paper, we study a bandit problem where the payoffs of arms are smooth on a graph. This framework is suitable for solving online learning problems that involve graphs, such as content-based recommendation. In this problem, each item we can recommend is a node and its expected rating is similar to its neighbors. The goal is to recommend items that have high expected ratings. We aim for the algorithm...

---

### 38. Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning

**Authors:** Hen Davidov, Nachshon Cohen, Oren Kalinsky, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18419v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18419v1)

**Summary:** Large language models (LLMs) using chain-of-thought reasoning often waste substantial compute by producing long, incorrect responses. Abstention can mitigate this by withholding outputs unlikely to be correct. While most abstention methods decide to withhold outputs before or after generation, dynamic mid-generation abstention considers early termination of unpromising reasoning traces at each token position. Prior work has explored empirical variants of this idea, but principled guidance for th...

---

### 39. Balance-Guided Sparse Identification of Multiscale Nonlinear PDEs with Small-coefficient Terms

**Authors:** Zhenhua Dang, Lei Zhang, Long Wang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18414v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18414v1)

**Summary:** Data-driven discovery of governing equations has advanced significantly in recent years; however, existing methods often struggle in multiscale systems where dynamically significant terms may have small coefficients. Therefore, we propose Balance-Guided SINDy (BG-SINDy) inspired by the principle of dominant balance, which reformulates $\ell_0$-constrained sparse regression as a term-level $\ell_{2,0}$-regularized problem and solves it using a progressive pruning strategy. Terms are ranked accord...

---

### 40. Bridge-Centered Metapath Classification Using R-GCN-VGAE for Disaster-Resilient Maintenance Decisions

**Authors:** Takato Yasuno

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18399v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18399v1)

**Summary:** Daily infrastructure management in preparation for disasters is critical for urban resilience. When bridges remain resilient against disaster-induced external forces, access to hospitals, shops, and residences via metapaths can be sustained, maintaining essential urban functions. However, prioritizing bridge maintenance under limited budgets requires quantifying the multi-dimensional roles that bridges play in disaster scenarios -- a challenge that existing single-indicator approaches fail to ad...

---

### 41. Randomly Initialized Networks Can Learn from Peer-to-Peer Consensus

**Authors:** Esteban Rodríguez-Betancourt, Edgar Casasola-Murillo

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18390v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18390v1)

**Summary:** In self-supervised learning, self-distilled methods have shown impressive performance, learning representations useful for downstream tasks and even displaying emergent properties. However, state-of-the-art methods usually rely on ensembles of complex mechanisms, with many design choices that are empirically motivated and not well understood.   In this work, we explore the role of self-distillation within learning dynamics. Specifically, we isolate the effect of self-distillation by training a g...

---

### 42. Learning from Less: Measuring the Effectiveness of RLVR in Low Data and Compute Regimes

**Authors:** Justin Bauer, Thomas Walshe, Derek Pham, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18381v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18381v1)

**Summary:** Fine-tuning Large Language Models (LLMs) typically relies on large quantities of high-quality annotated data, or questions with well-defined ground truth answers in the case of Reinforcement Learning with Verifiable Rewards (RLVR). While previous work has explored the benefits to model reasoning capabilities by scaling both data and compute used for RLVR, these results lack applicability in many real-world settings where annotated data and accessible compute may be scarce. In this work, we prese...

---

### 43. Forecasting Ionospheric Irregularities on GNSS Lines of Sight Using Dynamic Graphs with Ephemeris Conditioning

**Authors:** Mert Can Turkmen, Eng Leong Tan, Yee Hui Lee

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18379v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18379v1)

**Summary:** Most data-driven ionospheric forecasting models operate on gridded products, which do not preserve the time-varying sampling structure of satellite-based sensing. We instead model the ionosphere as a dynamic graph over ionospheric pierce points (IPPs), with connectivity that evolves as satellite positions change. Because satellite trajectories are predictable, the graph topology over the forecast horizon can be constructed in advance. We exploit this property to condition forecasts on the future...

---

### 44. Parkinson's Disease Detection via Self-Supervised Dual-Channel Cross-Attention on Bilateral Wrist-Worn IMU Signals

**Authors:** Meheru Zannat

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18372v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18372v1)

**Summary:** Parkinson's disease (PD) is a chronic neurodegenerative disease. It shows multiple motor symptoms such as tremor, bradykinesia, postural instability, freezing of gait (FoG). PD is currently diagnosed clinically through physical exam by health-care professionals, which can be time consuming and highly subjective. Wearable IMU sensors has become a promising gateway for passive monitoring of PD patients. We propose a self-supervised cross-attention encoder that processes bilateral wrist-worn IMU si...

---

### 45. Tight Auditing of Differential Privacy in MST and AIM

**Authors:** Georgi Ganev, Meenatchi Sundaram Muthu Selva Annamalai, Bogdan Kulynych

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18352v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18352v1)

**Summary:** State-of-the-art Differentially Private (DP) synthetic data generators such as MST and AIM are widely used, yet tightly auditing their privacy guarantees remains challenging. We introduce a Gaussian Differential Privacy (GDP)-based auditing framework that measures privacy via the full false-positive/false-negative tradeoff. Applied to MST and AIM under worst-case settings, our method provides the first tight audits in the strong-privacy regime. For $(ε,δ)=(1,10^{-2})$, we obtain $μ_{emp}\approx0...

---

### 46. Balanced Co-Clustering of Users and Items for Embedding Table Compression in Recommender Systems

**Authors:** Runhao Jiang, Renchi Yang, Donghao Wu

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18351v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18351v1)

**Summary:** Recommender systems have advanced markedly over the past decade by transforming each user/item into a dense embedding vector with deep learning models. At industrial scale, embedding tables constituted by such vectors of all users/items demand a vast amount of parameters and impose heavy compute and memory overhead during training and inference, hindering model deployment under resource constraints. Existing solutions towards embedding compression either suffer from severely compromised recommen...

---

### 47. Overcoming Selection Bias in Statistical Studies With Amortized Bayesian Inference

**Authors:** Jonas Arruda, Sophie Chervet, Paula Staudt, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18319v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18319v1)

**Summary:** Selection bias arises when the probability that an observation enters a dataset depends on variables related to the quantities of interest, leading to systematic distortions in estimation and uncertainty quantification. For example, in epidemiological or survey settings, individuals with certain outcomes may be more likely to be included, resulting in biased prevalence estimates with potentially substantial downstream impact. Classical corrections, such as inverse-probability weighting or explic...

---

### 48. Predictive Modeling of Natural Medicinal Compounds for Alzheimer Disease Using Cheminformatics

**Authors:** Hafiza Syeda Yusra Tirmizi, Syed Ibad Hasnain, Muhammad Faris, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18316v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18316v1)

**Summary:** The most common cause of dementia is Alzheimer disease, a progressive neurodegenerative disorder affecting older adults that gradually impairs memory, cognition, and behavior. It is characterized by the accumulation of abnormal proteins in the brain, including amyloid-beta plaques and neurofibrillary tangles of tau protein, which disrupt neuronal communication and lead to neuronal death. Early manifestations typically include mild memory impairment and reduced ability to acquire new information....

---

### 49. Scale-free adaptive planning for deterministic dynamics & discounted rewards

**Authors:** Peter L. Bartlett, Victor Gabillon, Jennifer Healey, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18312v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18312v1)

**Summary:** We address the problem of planning in an environment with deterministic dynamics and stochastic rewards with discounted returns. The optimal value function is not known, nor are the rewards bounded. We propose Platypoos, a simple scale-free planning algorithm that adapts to the unknown scale and smoothness of the reward function. We provide a sample complexity analysis for Platypoos that improves upon prior work and holds simultaneously over a broad range of discount factors and reward scales, w...

---

### 50. Symmetry Guarantees Statistic Recovery in Variational Inference

**Authors:** Daniel Marks, Dario Paccagnan, Mark van der Wilk

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18310v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18310v1)

**Summary:** Variational inference (VI) is a central tool in modern machine learning, used to approximate an intractable target density by optimising over a tractable family of distributions. As the variational family cannot typically represent the target exactly, guarantees on the quality of the resulting approximation are crucial for understanding which of its properties VI can faithfully capture. Recent work has identified instances in which symmetries of the target and the variational family enable the r...

---

## cs.NE

**50 papers**

### 1. Neutrally Evolving Interlocking Complexity in the Quandary Den

**Authors:** Andrew Walsh

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18361v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18361v1)

**Summary:** Molecular biology features numerous complexes of proteins that coordinate in an interlocking fashion to fulfill different functions. Adaptive evolution explains some of this complexity, but needn't be the default when neutral explanations suffice. A new artificial life model ``organism,'' the Quandary Den, is introduced to explore different neutral evolution scenarios where complexity increases in the absence of greater informational needs. Two interlocking complexity scenarios emerge. Subfuncti...

---

### 2. Similarity-based Portfolio Construction for Black-box Optimization

**Authors:** Catalin-Viorel Dinu, Diederick Vermetten, Carola Doerr

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18196v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18196v1)

**Summary:** In black-box optimization, a central question is which algorithm to use to solve a given, previously unseen, problem. Selecting a single algorithm, however, entails inherent risks: inaccuracies in the selector may lead to poor choices, and even well-performing algorithms with high variance can yield unsatisfactory results in a single run. A natural remedy is to split the evaluation budget across multiple runs of potentially different algorithms. Such sequential algorithm portfolios benefit from ...

---

### 3. The Magnitude of Dominated Sets: A Pareto Compliant Indicator Grounded in Metric Geometry

**Authors:** Michael T. M. Emmerich

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18147v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18147v1)

**Summary:** We investigate \emph{magnitude} as a new unary and strictly Pareto-compliant quality indicator for finite approximation sets to the Pareto front in multiobjective optimization. Magnitude originates in enriched category theory and metric geometry, where it is a notion of size or point content for compact metric spaces and a generalization of cardinality. For dominated regions in the \(\ell_1\) box setting, magnitude is close to hypervolume but not identical: it contains the top-dimensional hyperv...

---

### 4. On Scalability of Multi-Objective Evolutionary Algorithms on Combinatorial Optimisation Problems

**Authors:** Menghao Tang, Zimin Liang, Miqing Li

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.17872v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17872v1)

**Summary:** Scalability of evolutionary algorithms refers to assessing how their performance changes as problem size increases. In the area of multi-objective optimisation, research on the scalability of multi-objective evolutionary algorithms (MOEAs) has predominantly focussed on continuous problems. However, multi-objective combinatorial optimisation problems (MOCOPs) differ from continuous ones. Their discrete and rigid structure often brings rugged landscape, numerous local optimal solutions and disjoin...

---

### 5. On the Generalization Bounds of Symbolic Regression with Genetic Programming

**Authors:** Masahiro Nomura, Ryoki Hamano, Isao Ono

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17402v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17402v1)

**Summary:** Symbolic regression (SR) with genetic programming (GP) aims to discover interpretable mathematical expressions directly from data. Despite its strong empirical success, the theoretical understanding of why GP-based SR generalizes beyond the training data remains limited. In this work, we provide a learning-theoretic analysis of SR models represented as expression trees. We derive a generalization bound for GP-style SR under constraints on tree size, depth, and learnable constants. Our result dec...

---

### 6. Monotone but Exciting: On Evolving Monotone Boolean Functions with High Nonlinearity

**Authors:** Claude Carlet, Marko Čupić, Marko Ðurasevic, et al.

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17342v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17342v1)

**Summary:** Monotone Boolean functions are a structurally important class of Boolean functions, but their restricted form imposes strong limitations on achievable nonlinearity. In this paper, we investigate whether evolutionary computation can evolve monotone Boolean functions with high nonlinearity, both in the balanced and imbalanced settings. We consider three solution encodings: the standard truth table representation, a balanced truth table encoding that preserves Hamming weight, and a symbolic tree-ba...

---

### 7. A fully parallel densely connected probabilistic Ising machine with inertia for real-time applications

**Authors:** Ruomin Zhu, Abhishek Kumar Singh, Jérémie Laydevant, et al.

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.17109v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17109v1)

**Summary:** Ising machines -- special-purpose hardware for heuristically solving Ising optimization problems -- based on probabilistic bits (p-bits) have been established as a promising alternative to heuristic optimization algorithms run on conventional computers. However, it has -- until now -- been thought that Ising spins that are connected in probabilistic Ising machines cannot be updated in parallel without ruining the machine's solving ability. This has been a major challenge for using probabilistic ...

---

### 8. When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano

**Authors:** Jason Yoo, Shailesh Garg, Souvik Chakraborty, et al.

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.17040v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17040v1)

**Summary:** Spiking neural operators are appealing for neuromorphic edge computing because event-driven substrates can, in principle, translate sparse activity into lower latency and energy. Whether that advantage survives deployment on commodity edge-GPU software stacks, however, remains unclear. We study this question on a Jetson Orin Nano 8 GB using five pretrained variable-spiking wavelet neural operator (VS-WNO) checkpoints and five matched dense wavelet neural operator (WNO) checkpoints on the Darcy r...

---

### 9. Prototype-Grounded Concept Models for Verifiable Concept Alignment

**Authors:** Stefano Colamonaco, David Debot, Pietro Barbiero, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16076v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16076v1)

**Summary:** Concept Bottleneck Models (CBMs) aim to improve interpretability in Deep Learning by structuring predictions through human-understandable concepts, but they provide no way to verify whether learned concepts align with the human's intended meaning, hurting interpretability. We introduce Prototype-Grounded Concept Models (PGCMs), which ground concepts in learned visual prototypes: image parts that serve as explicit evidence for the concepts. This grounding enables direct inspection of concept sema...

---

### 10. Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks

**Authors:** Lúcio Folly Sanches Zebendo, Eleonora Cicciarella, Michele Rossi

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15997v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15997v1)

**Summary:** Spiking neural networks (SNNs) are rapidly gaining momentum as an alternative to conventional artificial neural networks in resource constrained edge systems. In this work, we continue a recent research line on recurrent SNNs where axonal delays are learned at runtime along with the other network parameters. The first proposed approach, dubbed DelRec, demonstrated the benefit of recurrent delay learning in SNNs. Here, we extend it by advocating the use of convolutional recurrent connections in c...

---

### 11. ECG-Lens: Benchmarking ML & DL Models on PTB-XL Dataset

**Authors:** Saloni Garg, Ukant Jadia, Amit Sagtani, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15822v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15822v1)

**Summary:** Automated classification of electrocardiogram (ECG) signals is a useful tool for diagnosing and monitoring cardiovascular diseases. This study compares three traditional machine learning algorithms (Decision Tree Classifier, Random Forest Classifier, and Logistic Regression) and three deep learning models (Simple Convolutional Neural Network (CNN), Long Short-Term Memory (LSTM), and Complex CNN (ECGLens)) for the classification of ECG signals from the PTB-XL dataset, which contains 12-lead recor...

---

### 12. Frenetic Cat-inspired Particle Optimization: a Markov state-switching hybrid swarm optimizer with application to cardiac digital twinning

**Authors:** Jorge Sánchez, Guadalupe García-Isla, Sandra Perez-Herrero, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15761v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15761v1)

**Summary:** Designing optimizers that remain effective under tight evaluation budgets is critical in expensive black-box settings such as cardiac digital twinning. We propose Frenetic Cat-inspired Particle Optimization (FCPO), a hybrid swarm method that couples particle swarm optimization-like dynamics with an explicit-state Markov switching controller to schedule exploration and refinement operators online. FCPO integrates (i) state-conditioned bounded motion, (ii) an elite-difference global jump operator ...

---

### 13. Enhancing Discrete Particle Swarm Optimization for Hypergraph-Modeled Influence Maximization

**Authors:** Qianshi Wang, Xilong Qu, Wenbin Pei, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15746v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15746v1)

**Summary:** Influence maximization (IM) is a fundamental problem in complex network analysis, with a wide range of real-world applications. To date, existing approaches to influential node identification in IM have predominantly relied on standard graphs, failing to capture higher-order intrinsic interactions embedded in many real-world systems. Hypergraphs can be employed to better capture higher-order interactions. However, using hypergraphs may lead to an excessively large search space and increased comp...

---

### 14. Impact of leaky dynamics on predictive path integration accuracy in recurrent neural networks

**Authors:** Yanlin Zhang, Yan Zhang, Muhua Zheng, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16547v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16547v1)

**Summary:** Experimental evidence indicates that intrinsic temporal dynamics operating across multiple time scales are closely associated with the emergence of periodic spatial activity of increasing complexity. However, how information encoded in grid-like firing patterns for path integration is processed across these intrinsic time scales remains unclear. To address this question, we introduce adaptive time scales through a leak term in recurrent neural networks (RNNs), forming leaky RNNs discretized from...

---

### 15. Neuromorphic Parameter Estimation for Power Converter Health Monitoring Using Spiking Neural Networks

**Authors:** Hyeongmeen Baik, Hamed Poursiami, Maryam Parsa, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15714v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15714v1)

**Summary:** Always-on converter health monitoring demands sub-mW edge inference, a regime inaccessible to GPU-based physics-informed neural networks. This work separates spiking temporal processing from physics enforcement: a three-layer leaky integrate-and-fire SNN estimates passive component parameters while a differentiable ODE solver provides physics-consistent training by decoupling the ODE physics loss from the unrolled spiking loop. On an EMI-corrupted synchronous buck converter benchmark, the SNN re...

---

### 16. Why Fine-Tuning Encourages Hallucinations and How to Fix It

**Authors:** Guy Kaplan, Zorik Gekhman, Zhen Zhu, et al.

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15574v1)

**Summary:** Large language models are prone to hallucinating factually incorrect statements. A key source of these errors is exposure to new factual information through supervised fine-tuning (SFT), which can increase hallucinations w.r.t. knowledge acquired during pre-training. In this work, we explore whether SFT-induced hallucinations can be mitigated using established tools from the continual learning literature, since they arise as a by-product of knowledge degradation during training. We propose a sel...

---

### 17. Beyond Single-Model Optimization: Preserving Plasticity in Continual Reinforcement Learning

**Authors:** Lute Lillo, Nick Cheney

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15414v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15414v1)

**Summary:** Continual reinforcement learning must balance retention with adaptation, yet many methods still rely on \emph{single-model preservation}, committing to one evolving policy as the main reusable solution across tasks. Even when a previously successful policy is retained, it may no longer provide a reliable starting point for rapid adaptation after interference, reflecting a form of \emph{loss of plasticity} that single-policy preservation cannot address. Inspired by quality-diversity methods, we i...

---

### 18. Structure as Computation: Developmental Generation of Minimal Neural Circuits

**Authors:** Duan Zhou

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15143v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15143v1)

**Summary:** This work simulates the developmental process of cortical neurogenesis, initiating from a single stem cell and governed by gene regulatory rules derived from mouse single-cell transcriptomic data. The developmental process spontaneously generates a heterogeneous population of 5,000 cells, yet yields only 85 mature neurons - merely 1.7% of the total population. These 85 neurons form a densely interconnected core of 200,400 synapses, corresponding to an average degree of 4,715 per neuron. At itera...

---

### 19. NEAT-NC: NEAT guided Navigation Cells for Robot Path Planning

**Authors:** Hibatallah Meliani, Khadija Slimani, Samira Khoulji

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15076v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15076v1)

**Summary:** To navigate a space, the brain makes an internal representation of the environment using different cells such as place cells, grid cells, head direction cells, border cells, and speed cells. All these cells, along with sensory inputs, enable an organism to explore the space around it. Inspired by these biological principles, we developed NEATNC, a Neuro-Evolution of Augmenting Topology guided Navigation Cells. The goal of the paper is to improve NEAT algorithm performance in path planning in dyn...

---

### 20. Analysis of Multitasking Pareto Optimization for Monotone Submodular Problems

**Authors:** Liam Wigney, Frank Neumann

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15068v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15068v1)

**Summary:** Pareto optimization via evolutionary multi-objective algorithms has been shown to efficiently solve constrained monotone submodular functions. Traditionally when solving multiple problems, the algorithm is run for each problem separately. We introduce multitasking formulations of these problems that are an effective way to solve multiple related problems with a single run. In our setting the given problems share a monotone submodular function $f$ but have different knapsack constraints. We exami...

---

### 21. On the Use of Iterative Problem Solving for the Traveling Salesperson Problem with Changing Time Window Constraints

**Authors:** Hy Nguyen, Thanh Nguyen Pham, Helen Yuliana Angmalisang, et al.

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.14745v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14745v1)

**Summary:** In many real-world settings, problem instances that need to be solved are quite similar, and knowledge from previous optimization runs can potentially be utilized. We explore this for the Traveling Salesperson problem with time windows (TSPTW), which often arises in settings where the travel-time matrix is fixed but time-window constraints change across related tasks. Existing TSPTW studies, however, have not systematically compared solving such task sequences independently with sequential trans...

---

### 22. Neural architectures for resolving references in program code

**Authors:** Gergő Szalay, Gergely Zsolt Kovács, Sándor Teleki, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14073v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14073v1)

**Summary:** Resolving and rewriting references is fundamental in programming languages. Motivated by a real-world decompilation task, we abstract reference rewriting into the problems of direct and indirect indexing by permutation. We create synthetic benchmarks for these tasks and show that well-known sequence-to-sequence machine learning architectures are struggling on these benchmarks. We introduce new sequence-to-sequence architectures for both problems. Our measurements show that our architectures outp...

---

### 23. Deep Neural Network-guided PSO for Tracking a Global Optimal Position in Complex Dynamic Environment

**Authors:** Stephen Raharja, Toshiharu Sugawara

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14064v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14064v1)

**Summary:** We propose novel particle swarm optimization (PSO) variants incorporated with deep neural networks (DNNs) for particles to pursue globally optimal positions in dynamic environments. PSO is a heuristic approach for solving complex optimization problems. However, canonical PSO and its variants struggle to adapt efficiently to dynamic environments, in which the global optimum moves over time, and to track them accurately. Many PSO algorithms improve convergence by increasing the swarm size beyond p...

---

### 24. Diffusion Language Models for Speech Recognition

**Authors:** Davyd Naveriani, Albert Zeyer, Ralf Schlüter, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14001v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14001v1)

**Summary:** Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC...

---

### 25. A Dynamic-Growing Fuzzy-Neuro Controller, Application to a 3PSP Parallel Robot

**Authors:** Mohsen Jalaeian-Farimani, Mohammad-R Akbarzadeh-T, Alireza Akbarzadeh, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13763v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13763v1)

**Summary:** To date, various paradigms of soft-Computing have been used to solve many modern problems. Among them, a self organizing combination of fuzzy systems and neural networks can make a powerful decision making system. Here, a Dynamic Growing Fuzzy Neural Controller (DGFNC) is combined with an adaptive strategy and applied to a 3PSP parallel robot position control problem. Specifically, the dynamic growing mechanism is considered in more detail. In contrast to other self-organizing methods, DGFNC add...

---

### 26. Modeling of Self-sustained Neuron Population without External Stimulus

**Authors:** İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13719v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13719v1)

**Summary:** Self-sustained neural activity in the absence of ongoing external input is a fundamental feature of nervous system dynamics, yet the conditions under which it can emerge in biophysically grounded network models remain incompletely understood. We studied whether a recurrent network of Hodgkin-Huxley neurons with spike-timing-dependent plasticity and intrinsic stochasticity can maintain autonomous activity after brief transient stimulation. The simulated network comprised 200 neurons (160 excitato...

---

### 27. General aspects of internal noise in spiking neural networks

**Authors:** I. D. Kolesnikov, D. A. Maksimov, V. M. Moskvitin, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13612v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13612v1)

**Summary:** This study examines the impact of additive and multiplicative noise on both a single leaky integrate-and-fire (LIF) neuron and a trained spiking neural network (SNN). Noise was introduced at different stages of neural processing, including the input current, membrane potential, and output spike generation. The results show that multiplicative noise applied to the membrane potential has the most detrimental effect on network performance, leading to a significant degradation in accuracy. This is p...

---

### 28. From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems

**Authors:** Alexandre Muzy

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13574v1)

**Summary:** Brain digital twins aim to provide faithful, individualized computational representations of brains as dynamical systems, enabling mechanistic understanding and supporting prediction of clinical interventions. Yet current approaches remain fragmented across data pipelines, model classes, temporal scales, and computing platforms, which prevents the preservation of execution semantics across the end-toend workflow. This survey introduces physically constrained executability as a unifying perspecti...

---

### 29. Greedy Approaches for Packing While Travelling with Deterministic and Stochastic Constraints

**Authors:** Thilina Pathirage Don, Aneta Neumann, Frank Neumann

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13469v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13469v1)

**Summary:** The travelling thief problem (TTP) is a well-known multi-component optimisation problem that captures the interdependence between two components: the tour across cities and the packing of items. The packing while travelling problem (PWT) is an NP-hard subproblem of TTP where the packing of items should be optimised for a given fixed tour. In many solvers, the packing component is often addressed using greedy heuristics. Here, the use of suitable greedy functions is essential for the success of g...

---

### 30. On the Use of Evolutionary Optimization for the Dynamic Chance Constrained Open-Pit Mine Scheduling Problem

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13385v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13385v1)

**Summary:** Open-pit mine scheduling is a complex real world optimization problem that involves uncertain economic values and dynamically changing resource capacities. Evolutionary algorithms are particularly effective in these scenarios, as they can easily adapt to uncertain and changing environments. However, uncertainty and dynamic changes are often studied in isolation in real-world problems. In this paper, we study a dynamic chance-constrained open-pit mine scheduling problem in which block economic va...

---

### 31. Attention to task structure for cognitive flexibility

**Authors:** Xiaoyu K. Zhang, Mehdi Senoussi, Tom Verguts

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13281v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13281v1)

**Summary:** Humans and artificial agents must often learn and switch between multiple tasks in dynamic environments. Success in such settings requires cognitive flexibility: the ability to retain prior knowledge (cognitive stability) while also transferring it to novel tasks (cognitive generalization). Cognitive flexibility research has largely focused on the role of model architecture to achieve these complementary goals. However, it is less well understood how the structure of the environment itself influ...

---

### 32. Analog Optical Inference on Million-Record Mortgage Data

**Authors:** Sofia Berloff, Pavel Koptev, Konstantin Malkov

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13251v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13251v1)

**Summary:** Analog optical computers promise large efficiency gains for machine learning inference, yet no demonstration has moved beyond small-scale image benchmarks. We benchmark the analog optical computer (AOC) digital twin on mortgage approval classification from 5.84 million U.S. HMDA records and separate three sources of accuracy loss. On the original 19 features, the AOC reaches 94.6% balanced accuracy with 5,126 parameters (1,024 optical), compared with 97.9% for XGBoost; the 3.3 percentage-point g...

---

### 33. Shapley Value-Guided Adaptive Ensemble Learning for Explainable Financial Fraud Detection with U.S. Regulatory Compliance Validation

**Authors:** Mohammad Nasir Uddin, Md Munna Aziz

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.14231v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14231v1)

**Summary:** Financial crime costs U.S. institutions over $32 billion each year. Although AI tools for fraud detection have become more advanced, their use in real-world systems still faces a major obstacle: many of these models operate as black boxes that cannot provide the transparent, auditable explanations required by regulations such as OCC Bulletin 2011-12 and Federal Reserve SR 11-7. This study makes three main contributions. First, it offers a thorough evaluation of explanation quality across faithfu...

---

### 34. Does Dimensionality Reduction via Random Projections Preserve Landscape Features?

**Authors:** Iván Olarte Rodríguez, Anja Jankovic, Thomas Bäck, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13230v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13230v1)

**Summary:** Exploratory Landscape Analysis (ELA) provides numerical features for characterizing black-box optimization problems. In high-dimensional settings, however, ELA suffers from sparsity effects, high estimator variance, and the prohibitive cost of computing several feature classes. Dimensionality reduction has therefore been proposed as a way to make ELA applicable in such settings, but it remains unclear whether features computed in reduced spaces still reflect intrinsic properties of the original ...

---

### 35. An abstract model of nonrandom, non-Lamarckian mutation in evolution using a multivariate estimation-of-distribution algorithm

**Authors:** Liudmyla Vasylenko, Adi Livnat

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12884v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12884v1)

**Summary:** At the fundamental conceptual level, two alternatives have traditionally been considered for how mutations arise and how evolution happens: 1) random mutation and natural selection, and 2) Lamarckism. Recently, the theory of Interaction-based Evolution (IBE) has been proposed, according to which mutations are neither random nor Lamarckian, but are influenced by information accumulating internally in the genome over generations. Based on the estimation-of-distribution algorithms framework, we pre...

---

### 36. Algorithmic Analysis of Dense Associative Memory: Finite-Size Guarantees and Adversarial Robustness

**Authors:** Madhava Gaikwad

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12811v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12811v1)

**Summary:** Dense Associative Memory (DAM) generalizes Hopfield networks through higher-order interactions and achieves storage capacity that scales as $O(N^{n-1})$ under suitable pattern separation conditions. Existing dynamical analyses primarily study the thermodynamic limit $N\to\infty$ with randomly sampled patterns and therefore do not provide finite-size guarantees or explicit convergence rates.   We develop an algorithmic analysis of DAM retrieval dynamics that yields finite-$N$ guarantees under exp...

---

### 37. Stability and Geometry of Attractors in Neural Cellular Automata

**Authors:** Mia-Katrin Kvalsund, James Stovold

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12720v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12720v1)

**Summary:** Throughout the literature on Neural Cellular Automata (NCAs), it is often taken for granted that the systems learn attractors. This is shown through evolving the system for many timesteps and noting visual similarity to the goal state. There remain many questions after such an analysis. Namely, what kind of attractors do we have? Is their behavior ordered or chaotic? Can we estimate stability over very long time horizons? What really happens in the attractor when perturbations are applied? In th...

---

### 38. Adaptive Spiking Neurons for Vision and Language Modeling

**Authors:** Chenlin Zhou, Sihang Guo, Jiaqi Wang, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12365v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12365v1)

**Summary:** Regarded as the third generation of neural networks, Spiking Neural Networks (SNNs) have garnered significant traction due to their biological plausibility and energy efficiency. Recent advancements in large models necessitate spiking neurons capable of high performance, adaptability, and training efficiency. In this work, we first propose a novel functional perspective that provides general guidance for designing the new generation of spiking neurons. Following the insightful guidelines, we pro...

---

### 39. GeM-EA: A Generative and Meta-learning Enhanced Evolutionary Algorithm for Streaming Data-Driven Optimization

**Authors:** Yue Wu, Yuan-Ting Zhong, Ze-Yuan Ma, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12336v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12336v1)

**Summary:** Streaming Data-Driven Optimization (SDDO) problems arise in many applications where data arrive continuously and the optimization environment evolves over time. Concept drift produces non-stationary landscapes, making optimization methods challenging due to outdated models. Existing approaches often rely on simple surrogate combinations or directly injecting solutions, which may cause negative transfer under sudden environmental changes. We propose GeM-EA, a Generative and Meta-learning Enhanced...

---

### 40. Socrates Loss: Unifying Confidence Calibration and Classification by Leveraging the Unknown

**Authors:** Sandra Gómez-Gálvez, Tobias Olenyi, Gillian Dobbie, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12245v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12245v1)

**Summary:** Deep neural networks, despite their high accuracy, often exhibit poor confidence calibration, limiting their reliability in high-stakes applications. Current ad-hoc confidence calibration methods attempt to fix this during training but face a fundamental trade-off: two-phase training methods achieve strong classification performance at the cost of training instability and poorer confidence calibration, while single-loss methods are stable but underperform in classification. This paper addresses ...

---

### 41. Gradient-Free Continual Learning in Spiking Neural Networks via Inter-Spike Interval Regularization

**Authors:** Samrendra Roy, Kazuma Kobayashi, Souvik Chakraborty, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.16496v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16496v1)

**Summary:** Continual learning, the ability to acquire new tasks sequentially without forgetting prior knowledge, is essential for deploying neural networks in dynamic real-world environments, from nuclear digital twin monitoring to grid-edge fault detection. Existing synaptic importance methods, such as Elastic Weight Consolidation (EWC) and Synaptic Intelligence (SI), rely on gradient computation, making them incompatible with neuromorphic hardware that lacks backpropagation support. We propose ISI-CV, th...

---

### 42. EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture

**Authors:** William Savage

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12167v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12167v1)

**Summary:** We present (Experience-Modulated Biologically-inspired Emergent Reasoning), a hybrid cognitive architecture that reorganises the relationship between large language models (LLMs) and memory: rather than augmenting an LLM with retrieval tools, we place the LLM as a replaceable reasoning engine within a persistent, biologically-grounded associative substrate.   The architecture centres on a 220,000-neuron spiking neural network (SNN) with spike-timing-dependent plasticity (STDP), four-layer hierar...

---

### 43. Can AI Detect Life? Lessons from Artificial Life

**Authors:** Ankit Gupta, Christoph Adami

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11915v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11915v1)

**Summary:** Modern machine learning methods have been proposed to detect life in extraterrestrial samples, drawing on their ability to distinguish biotic from abiotic samples based on training models using natural and synthetic organic molecular mixtures. Here we show using Artificial Life that such methods are easily fooled into detecting life with near 100% confidence even if the analyzed sample is not capable of life. This is due to modern machine learning methods' propensity to be easily fooled by out-o...

---

### 44. Beyond LLMs, Sparse Distributed Memory, and Neuromorphics <A Hyper-Dimensional SRAM-CAM "VaCoAl" for Ultra-High Speed, Ultra-Low Power, and Low Cost>

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11665v4) | 📄 [PDF](https://arxiv.org/pdf/2604.11665v4)

**Summary:** This paper reports an unexpected finding: in a deterministic hyperdimensional computing (HDC) architecture **that inverts the conventional role of Galois-field algebra -- employing it not for error correction toward a unique answer but as an engine for relative similarity and path-quality ranking -- **a path-dependent semantic selection mechanism emerges, equivalent to spike-timing-dependent plasticity (STDP), with magnitude predictable a priori from a closed-form expression matching measured va...

---

### 45. Winner-Take-All Spiking Transformer for Language Modeling

**Authors:** Chenlin Zhou, Sihang Guo, Jiaqi Wang, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11321v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11321v1)

**Summary:** Spiking Transformers, which combine the scalability of Transformers with the sparse, energy-efficient property of Spiking Neural Networks (SNNs), have achieved impressive results in neuromorphic and vision tasks and attracted increasing attention. However, existing directly trained spiking transformers primarily focus on vision tasks. For language modeling with spiking transformer, convergence relies heavily on softmax-based spiking self-attention, which incurs high energy costs and poses challe...

---

### 46. Evolving Many Worlds: Towards Open-Ended Discovery in Petri Dish NCA via Population-Based Training

**Authors:** Uljad Berdica, Jakob Foerster, Frank Hutter, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11248v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11248v1)

**Summary:** The generation of sustained, open-ended complexity from local interactions remains a fundamental challenge in artificial life. Differentiable multi-agent systems, such as Petri Dish Neural Cellular Automata (PD-NCA), exhibit rich self-organization driven purely by spatial competition; however, they are highly sensitive to hyperparameters and frequently collapse into uninteresting patterns and dynamics, such as frozen equilibria or structureless noise. In this paper, we introduce PBT-NCA, a meta-...

---

### 47. Frugal Knowledge Graph Construction with Local LLMs: A Zero-Shot Pipeline, Self-Consistency and Wisdom of Artificial Crowds

**Authors:** Pierre Jourlin

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11104v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11104v1)

**Summary:** This paper presents an empirical study of a multi-model zero-shot pipeline for knowledge graph construction and exploitation, executed entirely through local inference on consumer-grade hardware. We propose a reproducible evaluation framework integrating two external benchmarks (DocRED, HotpotQA), WebQuestionsSP-style synthetic data, and the RAGAS evaluation framework in an automated pipeline. On 500 document-level relations, our system achieves an F1 of 0.70 $\pm$ 0.041 in zero-shot, compared t...

---

### 48. K-Way Energy Probes for Metacognition Reduce to Softmax in Discriminative Predictive Coding Networks

**Authors:** Jon-Paul Cacioli

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11011v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11011v1)

**Summary:** We present this as a negative result with an explanatory mechanism, not as a formal upper bound.   Predictive coding networks (PCNs) admit a K-way energy probe in which each candidate class is fixed as a target, inference is run to settling, and the per-hypothesis settled energies are compared. The probe appears to read a richer signal source than softmax, since the per-hypothesis energy depends on the entire generative chain.   We argue this appearance is misleading under the standard Pinchetti...

---

### 49. On the Use of Bi-Objective Evolutionary Algorithms for the Stochastic MKP under Dynamic Constraints

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.10930v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10930v1)

**Summary:** The multiple knapsack problem (MKP) generalizes the classical knapsack problem by assigning items to multiple knapsacks subject to capacity constraints. It is used to model many real-world resource allocation and scheduling problems. In practice, these optimization problems often involve stochastic and dynamic components. Evolutionary algorithms provide a flexible framework for addressing such problems under uncertainty and dynamic changes. In this paper, we investigate a stochastic and dynamic ...

---

### 50. Retinal Cyst Detection from Optical Coherence Tomography Images

**Authors:** Abhishek Dharmaratnakar, Aadheeshwar Vijayakumar, Suchand Dayanand

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10843v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10843v1)

**Summary:** Retinal Cysts are formed by leakage and accumulation of fluid in the retina due to the incompetence of retinal vasculature. These cystic spaces have significance in several ocular diseases such as age-related macular degeneration, diabetic macular edema, etc. Optical coherence tomography is one of the predominant diagnosing techniques for imaging retinal pathologies. Segmenting and quantification of intraretinal cysts plays the vital role in predicting visual acuity. In literature, several metho...

---

## q-bio.NC

**50 papers**

### 1. High-fidelity and Network-based Spatio-temporal Mathematical Models of Alzheimer's Disease Progression and their Validation Against PET-SUVR Imaging Data

**Authors:** Beatrice Caon, Mattia Corti, Francesca Bonizzoni, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18470v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18470v1)

**Summary:** Alzheimer's disease is the most common neurodegenerative disorder. Its pathological development is connected with the misfolding and accumulation of two toxic proteins: amyloid-beta and tau proteins. Mathematical models provide a valuable quantitative tool for monitoring disease progression. In this work, we proposed and compare a novel framework where the spatio-temporal dynamics of amyloid-beta and tau proteins is modeled based on employing either three-dimensional patient-specific geometries ...

---

### 2. The Umwelt Representation Hypothesis: Rethinking Universality

**Authors:** Victoria Bosch, Rowan Sommers, Adrien Doerig, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.17960v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17960v1)

**Summary:** Recent studies reveal striking representational alignment between artificial neural networks (ANNs) and biological brains, leading to proposals that all sufficiently capable systems converge on universal representations of reality. Here, we argue that this claim of Universality is premature. We introduce the Umwelt Representation Hypothesis (URH), proposing that alignment arises not from convergence toward a single global optimum, but from overlap in ecological constraints under which systems de...

---

### 3. How Much Data is Enough? The Zeta Law of Discoverability in Biomedical Data, featuring the enigmatic Riemann zeta function

**Authors:** Paul M. Thompson

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17581v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17581v1)

**Summary:** How much data is enough to make a scientific discovery? As biomedical datasets scale to millions of samples and AI models grow in capacity, progress increasingly depends on predicting when additional data will substantially improve performance. In practice, model development often relies on empirical scaling curves measured across architectures, modalities, and dataset sizes, with limited theoretical guidance on when performance should improve, saturate, or exhibit cross-over behavior.   We prop...

---

### 4. Poisson Flow Model of Cortical Folding Pattern

**Authors:** Moo K. Chung, Luigi Maccotta, Aaron Struck

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17291v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17291v1)

**Summary:** Cortical folding reflects coordinated neurodevelopmental processes and provides a sensitive marker of neurological disease. In juvenile myoclonic epilepsy (JME), structural abnormalities are subtle and spatially distributed, limiting the sensitivity of conventional morphometric measures such as cortical thickness. We introduce a Poisson flow model derived from gradients of the mean curvature field on the cortical surface. The method yields a smooth scalar field obtained from a Poisson equation, ...

---

### 5. Causality as a Minimum Energy Principle

**Authors:** Moo K. Chung, D. Vijay Anand, Anass B El-Yaagoubi, et al.

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.17151v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17151v1)

**Summary:** Classical causal models, such as Granger causality and structural equation modeling, are largely restricted to acyclic interactions and struggle to represent cyclic and higher-order dynamics in complex networks. We introduce a causal framework grounded in a variational principle, interpreting causality as directional energy flow from high- to low-energy states along network connections. Using Hodge theory, network flows are decomposed into dissipative components and a persistent harmonic compone...

---

### 6. Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI

**Authors:** Nils Leutenegger

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.16875v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16875v1)

**Summary:** A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex. We present a systematic comparison of four learning rules -- backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP) -- applied to identical convolutional architectures and evaluated against human fMRI data from the THINGS-fMRI dataset (...

---

### 7. Timescale Limits of Linear-Threshold Networks

**Authors:** William Retnaraj, Simone Betteti, Alexander Davydov, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16710v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16710v1)

**Summary:** Linear-threshold networks (LTNs) capture the mesoscale behavior of interacting populations of neurons and are of particular interest to control theorists due to their dynamical richness and relative ease of analysis. The aim of this paper is to advance the study of global asymptotic stability in LTNs with asymmetric neural interactions and heterogeneous dissipation under the structural Lyapunov diagonal stability (LDS) condition. To this end, we introduce a one-parameter family of LTNs that pres...

---

### 8. Role of chloride concentration in modulating seizure transitions in excitatory and inhibitory networks

**Authors:** Qianchen Gong, Yingpeng Liu, Yan Zhang, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15747v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15747v1)

**Summary:** Experimental evidence indicates that intracellular chloride concentration regulates the excitation and inhibition (EI) balance, yet the mechanisms by which activity-dependent chloride dynamics drive seizure evolution and stage transitions remain unclear. We present a conductance-based neuronal network in which EI balance emerges from chloride homeostasis via channel-mediated influx and transporter-mediated extrusion. We show that the fraction of inhibitory synaptic conductance contributing to ch...

---

### 9. Goxpyriment: A Go Framework for Behavioral and Cognitive Experiments

**Authors:** Christophe Pallier, Julie Bonnaire, Marie-France Fourcade

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15245v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15245v1)

**Summary:** We introduce `Goxpyriment', a new open-source software framework for programming behavioral and cognitive experiments using the Go programming language. The library is designed to address some limitations of existing Python-based experiment tools, particularly the runtime environment complexity that frequently complicates deployment across laboratories. Because Go is a compiled language that can natively embed assets (e.g., graphics, audio files, and stimulus lists), Goxpyriment compiles entire ...

---

### 10. Robust Evaluation of Neural Encoding Models via ground-truth approximation

**Authors:** Giovanni M. Di Liberto

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.14694v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14694v1)

**Summary:** Encoding models enable measurement of how our brains represent sensory inputs using electro-and magneto-encephalography (MEEG). Evaluating how closely encoding models reflect the underlying brain functions is a crucial premise for model interpretation and hypothesis testing. However, the ground-truth neural activity is unknown, preventing model evaluation with respect to the target neural signal. Existing evaluation metrics must therefore relate model's predictions to noisy MEEG measurements, wh...

---

### 11. Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays

**Authors:** Laurent U Perrinet

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.14096v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14096v1)

**Summary:** Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ and trained end-to-end with surrogate-gradient backpropagation through time. The network stores $M$ arbitrary target spike patterns by representing each as a sequen...

---

### 12. Seeing the imagined: a latent functional alignment in visual imagery decoding from fMRI data

**Authors:** Fabrizio Spera, Tommaso Boccato, Michal Olak, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.15374v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15374v1)

**Summary:** Recent progress in visual brain decoding from fMRI has been enabled by large-scale datasets such as the Natural Scenes Dataset (NSD) and powerful diffusion-based generative models. While current pipelines are primarily optimized for perception, their performance under mental-imagery remains less well understood. In this work, we study how a state-of-the-art (SOTA) perception decoder (DynaDiff) can be adapted to reconstruct imagined content from the Imagery-NSD benchmark. We propose a latent func...

---

### 13. Modeling of Self-sustained Neuron Population without External Stimulus

**Authors:** İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, et al.

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13719v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13719v1)

**Summary:** Self-sustained neural activity in the absence of ongoing external input is a fundamental feature of nervous system dynamics, yet the conditions under which it can emerge in biophysically grounded network models remain incompletely understood. We studied whether a recurrent network of Hodgkin-Huxley neurons with spike-timing-dependent plasticity and intrinsic stochasticity can maintain autonomous activity after brief transient stimulation. The simulated network comprised 200 neurons (160 excitato...

---

### 14. From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems

**Authors:** Alexandre Muzy

**Published:** 2026-04-15

🔗 [Paper](http://arxiv.org/abs/2604.13574v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13574v1)

**Summary:** Brain digital twins aim to provide faithful, individualized computational representations of brains as dynamical systems, enabling mechanistic understanding and supporting prediction of clinical interventions. Yet current approaches remain fragmented across data pipelines, model classes, temporal scales, and computing platforms, which prevents the preservation of execution semantics across the end-toend workflow. This survey introduces physically constrained executability as a unifying perspecti...

---

### 15. Attention to task structure for cognitive flexibility

**Authors:** Xiaoyu K. Zhang, Mehdi Senoussi, Tom Verguts

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.13281v1) | 📄 [PDF](https://arxiv.org/pdf/2604.13281v1)

**Summary:** Humans and artificial agents must often learn and switch between multiple tasks in dynamic environments. Success in such settings requires cognitive flexibility: the ability to retain prior knowledge (cognitive stability) while also transferring it to novel tasks (cognitive generalization). Cognitive flexibility research has largely focused on the role of model architecture to achieve these complementary goals. However, it is less well understood how the structure of the environment itself influ...

---

### 16. The illusory simplicity of the feedforward pass: evidence for the dynamical nature of stimulus encoding along the primate ventral stream

**Authors:** Daniel Anthes, Sushrut Thorat, Anna Mitola, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12825v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12825v1)

**Summary:** In studying primate vision, a large body of work focuses on the first feedforward sweep. During this initial time window, information is thought to pass through ventral stream regions in a stage-like fashion in an effort to extract high-level information from the retinal input. Consequently, electrophysiological analyses commonly focus on spatial response patterns, either by averaging data in time, or by applying decoders in a temporally local fashion. By analysing data recorded simultaneously a...

---

### 17. Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining

**Authors:** Junfeng Xia, Wenhao Ye, Xuanye Pan, et al.

**Published:** 2026-04-14

🔗 [Paper](http://arxiv.org/abs/2604.12683v1) | 📄 [PDF](https://arxiv.org/pdf/2604.12683v1)

**Summary:** Current fMRI foundation models primarily rely on a limited range of brain states and mismatched pretraining tasks, restricting their ability to learn generalized representations across diverse brain states. We present \textit{Brain-DiT}, a universal multi-state fMRI foundation model pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Unlike prior fMRI foundation models that rely on masked reconstruction in the raw-signal space or a lat...

---

### 18. Machine learning approaches to uncover the neural mechanisms of motivated behaviour: from ADHD to individual differences in effort and reward sensitivity

**Authors:** Nam Trinh

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.15363v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15363v1)

**Summary:** Motivated behaviour relies on the brain's capacity to evaluate effort and reward. Dysregulation within these processes contributes to a spectrum of conditions, from hyperactivity in attention-deficit/hyperactivity disorder (ADHD) to diminished goal-directed behaviour in apathy. This thesis investigates the neural mechanisms underlying ADHD using electroencephalography (EEG) and examines individual differences in effort and reward sensitivity using neuroimaging, applying machine learning approach...

---

### 19. Integrated information theory: the good, the bad and the misunderstood

**Authors:** Adam B. Barrett, Borjan Milinkovic, Pedro A. M. Mediano, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11482v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11482v1)

**Summary:** The integrated information theory of consciousness (IIT) is uniquely ambitious in proposing a mathematical formula, derived from apparently fundamental properties of conscious experience, to describe the quantity and quality of consciousness for any physical system that possesses it. IIT has generated considerable debate, which has engendered some misunderstandings and misrepresentations. Here we address and hope to remedy this. We begin by concisely summarising the essentials of IIT. Given IIT ...

---

### 20. The Neurobiological Craving Signature (NCS) predicts social craving and responds to social isolation

**Authors:** Ana Defendini Cortes, Livia Tomova, Leonie Koban

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11208v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11208v1)

**Summary:** Humans are inherently social and seek connection with others for survival. Recent studies suggest that acute social isolation leads to craving for social interactions, but the brain mechanisms of social craving and their relationship to brain networks underlying drug and food craving remain incompletely understood. Here we harnessed an existing dataset and tested whether the Neurobiological Craving Signature (NCS)-a recently developed fMRI-based brain-signature of drug and food craving-also pred...

---

### 21. Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching

**Authors:** Nicole Rogalla, Yuzhen Qin, Mario Senden, et al.

**Published:** 2026-04-13

🔗 [Paper](http://arxiv.org/abs/2604.11178v1) | 📄 [PDF](https://arxiv.org/pdf/2604.11178v1)

**Summary:** Forecasting neural activity in response to naturalistic stimuli remains a key challenge for understanding brain dynamics and enabling downstream neurotechnological applications. Here, we introduce a generative forecasting framework for modeling neural dynamics based on autoregressive flow matching (AFM). Building on recent advances in transport-based generative modeling, our approach probabilistically predicts neural responses at scale from multimodal sensory input. Specifically, we learn the co...

---

### 22. Relaxing in Warped Spaces: Generalized Hierarchical and Modular Dynamical Neural Network

**Authors:** Kazuyoshi Tsutsumi, Ernst Niebur

**Published:** 2026-04-12

🔗 [Paper](http://arxiv.org/abs/2604.10606v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10606v1)

**Summary:** We propose a dynamical neural network model with a hierarchical and modular structure. The network architecture can be derived by minimizing an energy function that is originally designed based on two kinds of neurons with quite different time constants. It has multiple subspaces that are spanned by neural parameters employed in the energy function, and adjacent subspaces are related to each other with a layered internetwork. Each internetwork further consists of a pair of a forward subnet and a...

---

### 23. Astrocytic resource diffusion stabilizes persistent activity in neural fields

**Authors:** Noah Palmer, Heather L. Cihak, Daniele Avitabile, et al.

**Published:** 2026-04-11

🔗 [Paper](http://arxiv.org/abs/2604.10036v1) | 📄 [PDF](https://arxiv.org/pdf/2604.10036v1)

**Summary:** Persistent neural activity underlying working memory requires sustained synaptic transmission, yet the metabolic and neurotransmitter support provided by astrocyte networks is largely absent from spatially extended neural circuit models. We introduce a coupled astrocyte-neural field model in which synaptic efficacy is regulated by depletion and recovery of a conserved resource pool recycled and spatially redistributed through diffusively coupled astrocytes. We obtain explicit stationary bump pro...

---

### 24. The Rise and Fall of $G$ in AGI

**Authors:** David C. Krakauer

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09911v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09911v1)

**Summary:** In the psychological literature the term `general intelligence' describes correlations between abilities and not simply the number of abilities. This paper connects Spearman's $g$-factor from psychometrics, measuring a positive manifold, to the implicit ``$G$-factor'' in claims about artificial general intelligence (AGI) performance on temporally structured benchmarks. By treating LLM benchmark batteries as cognitive test batteries and model releases as subjects, principal component analysis is ...

---

### 25. The Fast Lane Hypothesis: Von Economo Neurons Implement a Biological Speed-Accuracy Tradeoff

**Authors:** Esila Keskin

**Published:** 2026-04-10

🔗 [Paper](http://arxiv.org/abs/2604.09229v1) | 📄 [PDF](https://arxiv.org/pdf/2604.09229v1)

**Summary:** Von Economo neurons (VENs) are large bipolar projection neurons found exclusively in the anterior cingulate cortex (ACC) and frontal insula of species with complex social cognition, including humans, great apes, and cetaceans. Their selective depletion in frontotemporal dementia (FTD) and altered development in autism implicate them in rapid social decision-making, yet no computational model of VEN function has previously existed. We introduce the Fast Lane Hypothesis: VENs implement a biologica...

---

### 26. Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding

**Authors:** Mu Nan, Muquan Yu, Weijian Mai, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08537v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08537v1)

**Summary:** Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, cross-subject models. A major obstacle towards this goal is the substantial variability in neural representations across individuals, which has so far required training bespoke models or fine-tuning separately for each subject. To address this challenge...

---

### 27. Neuromodulation supports robust rhythmic pattern transitions in degenerate central pattern generators with fixed connectivity

**Authors:** Arthur Fyon, Alessio Franci, Pierre Sacré, et al.

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.08312v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08312v1)

**Summary:** Many essential biological functions, such as breathing and locomotion, rely on the coordination of robust and adaptable rhythmic patterns, governed by specific network architectures known as connectomes. Rhythmic adaptation is often linked to slow structural modifications of the connectome through synaptic plasticity, but such mechanisms are too slow to support rapid, localized rhythmic transitions. Here, we propose a neuromodulation-based control architecture for dynamically reconfiguring rhyth...

---

### 28. The Cartesian Cut in Agentic AI

**Authors:** Tim Sainburg, Caleb Weinreb

**Published:** 2026-04-09

🔗 [Paper](http://arxiv.org/abs/2604.07745v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07745v1)

**Summary:** LLMs gain competence by predicting words in human text, which often reflects how people perform tasks. Consequently, coupling an LLM to an engineered runtime turns prediction into control: outputs trigger interventions that enact goal-oriented behavior. We argue that a central design lever is where control resides in these systems. Brains embed prediction within layered feedback controllers calibrated by the consequences of action. By contrast, LLM agents implement Cartesian agency: a learned co...

---

### 29. The Principle of Maximum Heterogeneity Optimises Productivity in Distributed Production Systems Across Biology, Economics, and Computing

**Authors:** Guillhem Artis, Danyal Akarca, Jascha Achterberg

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07602v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07602v1)

**Summary:** The world is full of systems of distributed agents, collaborating and competing in complex ways: firms and workers specialise within economies, neurons adapt their tuning across brain circuits, and species compete and coexist within ecosystems. In that context, individual research fields built theories explaining how comparative advantage drives trade specialisation, how balanced neural representations emerge from sensory coding, and how biodiversity sustains ecological productivity. Here we pro...

---

### 30. Exploring the proprioceptive potential of joint receptors using a biomimetic robotic joint

**Authors:** Akihiro Miki, Shun Hasegawa, Sota Yuzaki, et al.

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.07038v1) | 📄 [PDF](https://arxiv.org/pdf/2604.07038v1)

**Summary:** In neuroscience, joint receptors have traditionally been viewed as limit detectors, providing positional information only at extreme joint angles, while muscle spindles are considered the primary sensors of joint angle position. However, joint receptors are widely distributed throughout the joint capsule, and their full role in proprioception remains unclear. In this study, we specifically focused on mimicking Type I joint receptors, which respond to slow and sustained movements, and quantified ...

---

### 31. MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis

**Authors:** Xiaobo Liu

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.16463v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16463v1)

**Summary:** MLE-Toolbox is a comprehensive open-source MATLAB toolbox for end-to-end analysis of magnetoencephalography (MEG) and electroencephalography (EEG) data. Inspired by widely used neuroimaging platforms such as Brainstorm and FieldTrip, it integrates the full analysis pipeline within a unified and user-friendly graphical interface (GUI), covering raw data import, preprocessing, source localization, functional connectivity, oscillatory analysis, and machine learning-based classification. The toolbox...

---

### 32. Quantum-like Cognition in Process Theories: An Analysis

**Authors:** Sean Tull, Masanao Ozawa

**Published:** 2026-04-08

🔗 [Paper](http://arxiv.org/abs/2604.08604v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08604v1)

**Summary:** Various effects in human cognition, often considered `non-classical', have been argued to be most naturally modelled by quantum-like models of decision making. We extend this approach to describe models of cognition and decision-making in general probabilistic process theories, which include both classical probabilistic models and quantum instrument models as special cases. We show how many aspects of quantum-like cognition can be described diagrammatically in process theories, before using our ...

---

### 33. Bridging Theory and Practice in Crafting Robust Spiking Reservoirs

**Authors:** Ruggero Freddi, Nicolas Seseri, Diana Nigrisoli, et al.

**Published:** 2026-04-07

🔗 [Paper](http://arxiv.org/abs/2604.06395v1) | 📄 [PDF](https://arxiv.org/pdf/2604.06395v1)

**Summary:** Spiking reservoir computing provides an energy-efficient approach to temporal processing, but reliably tuning reservoirs to operate at the edge-of-chaos is challenging due to experimental uncertainty. This work bridges abstract notions of criticality and practical stability by introducing and exploiting the robustness interval, an operational measure of the hyperparameter range over which a reservoir maintains performance above task-dependent thresholds. Through systematic evaluations of Leaky I...

---

### 34. Hierarchical Mesh Transformers with Topology-Guided Pretraining for Morphometric Analysis of Brain Structures

**Authors:** Yujian Xiong, Mohammad Farazi, Yanxi Chen, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05215v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05215v1)

**Summary:** Representation learning on large-scale unstructured volumetric and surface meshes poses significant challenges in neuroimaging, especially when models must incorporate diverse vertex-level morphometric descriptors, such as cortical thickness, curvature, sulcal depth, and myelin content, which carry subtle disease-related signals. Current approaches either ignore these clinically informative features or support only a single mesh topology, restricting their use across imaging pipelines. We introd...

---

### 35. Support Sufficiency as Consequence-Sensitive Compression in Belief Arbitration

**Authors:** Mark Walsh

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.16434v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16434v1)

**Summary:** When a system commits to a hypothesis, much of the evidential structure behind that commitment is lost to compression. Standard accounts assume that selected content and scalar confidence suffice for downstream control. This paper argues that they do not, and that determining what must survive compression is itself a consequence-sensitive problem. We develop a recurrent arbitration architecture in which active constraint fields jointly determine a hypothesis geometry over candidates. Rather than...

---

### 36. Energy-Based Dynamical Models for Neurocomputation, Learning, and Optimization

**Authors:** Arthur N. Montanari, Francesco Bullo, Dmitry Krotov, et al.

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05042v1) | 📄 [PDF](https://arxiv.org/pdf/2604.05042v1)

**Summary:** Recent advances at the intersection of control theory, neuroscience, and machine learning have revealed novel mechanisms by which dynamical systems perform computation. These advances encompass a wide range of conceptual, mathematical, and computational ideas, with applications for model learning and training, memory retrieval, data-driven control, and optimization. This tutorial focuses on neuro-inspired approaches to computation that aim to improve scalability, robustness, and energy efficienc...

---

### 37. Regime Mapping of Oscillatory States in Balanced Spiking Networks with Multiple Time Scales

**Authors:** Tsung-Han Kuo, Tzu-Chia Tung

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.04770v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04770v1)

**Summary:** Balanced spiking networks can transition between silent, asynchronous-irregular, and oscillatory states depending on interacting synaptic and temporal time scales, while their joint parameter structure remains incompletely characterized. In this work, we systematically map how postsynaptic decay (τs), conduction delay (d), and plasticity rate (λp) jointly shape oscillatory regimes in recurrent leaky integrate-and-fire networks. By combining Brian2 simulations across the (τs, d, λp) space with a ...

---

### 38. Causal Stance

**Authors:** Yoshiyuki Ohmura, Yasuo Kuniyoshi

**Published:** 2026-04-06

🔗 [Paper](http://arxiv.org/abs/2604.05004v2) | 📄 [PDF](https://arxiv.org/pdf/2604.05004v2)

**Summary:** What exactly is the meaning of physical causal closure, a concept frequently discussed in the philosophy of mind? Jaegwon Kim explicitly adopts a conception of causation according to which physical causation is effectively identified with deterministic physical lawfulness, and on this basis equates physical determinism with physical causal closure. While this conception is internally coherent, it differs from the currently dominant theories of causation, which emphasize asymmetry between cause a...

---

### 39. Non-Equilibrium Stochastic Dynamics as a Unified Framework for Insight and Repetitive Learning: A Kramers Escape Approach to Continual Learning

**Authors:** Gunn Kim

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04154v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04154v1)

**Summary:** Continual learning in artificial neural networks is fundamentally limited by the stability--plasticity dilemma: systems that retain prior knowledge tend to resist acquiring new knowledge, and vice versa. Existing approaches, most notably elastic weight consolidation~(EWC), address this empirically without a physical account of why plasticity eventually collapses as tasks accumulate. Separately, the distinction between sudden insight and gradual skill acquisition through repetitive practice has l...

---

### 40. The physical basis of information flow in neural matter: a thermocoherent perspective on cognitive dynamics

**Authors:** Onur Pusuluk

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04069v2) | 📄 [PDF](https://arxiv.org/pdf/2604.04069v2)

**Summary:** Information flow is central to contemporary accounts of cognition, yet its physical basis in living neural matter remains poorly specified. Here, we develop a multiscale resource-theoretical framework motivated by the \textit{thermocoherent effect}, where heat flow is reciprocally coupled to a delocalized information flow carried by shared coherence and not reducible to local subsystem variables. Extending this line of work in light of recent results on correlation-enabled Mpemba-type thermal re...

---

### 41. Topological Sensitivity in Connectome-Constrained Neural Networks

**Authors:** Nalin Dhiman

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04033v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04033v1)

**Summary:** Connectome-constrained neural networks are often evaluated against sparse random controls and then interpreted as evidence that biological graph topology improves learning efficiency. We revisit that claim in a controlled flyvis-based study using a Drosophila connectome, a naive self-loop-matched random graph, and a degree-preserving rewired null. Under weak controls, in which both models were recovered from a connectome-trained checkpoint and the null matched only global graph counts, the conne...

---

### 42. Neurological Plausibility of AI-Generated Music for Commercial Environments: An In-Silico Cortical Investigation Using Wubble and TRIBE v2

**Authors:** Shaad Sufi

**Published:** 2026-04-05

🔗 [Paper](http://arxiv.org/abs/2604.04025v1) | 📄 [PDF](https://arxiv.org/pdf/2604.04025v1)

**Summary:** Background music shapes attention, affect, and approach behavior in commercial environments, yet the neural plausibility of AI-generated music for such settings remains poorly characterized. We present an in-silico pilot study that combines Wubble, a generative music system, with TRIBE v2, a publicly released whole-brain encoding model, to estimate cortical response profiles for prompt-conditioned retail music. Five fully instrumental tracks were generated to span low-to-high arousal, sparse-to-...

---

### 43. Large Language Models Align with the Human Brain during Creative Thinking

**Authors:** Mete Ismayilzada, Simone A. Luchini, Abdulkadir Gokce, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03480v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03480v1)

**Summary:** Creative thinking is a fundamental aspect of human cognition, and divergent thinking-the capacity to generate novel and varied ideas-is widely regarded as its core generative engine. Large language models (LLMs) have recently demonstrated impressive performance on divergent thinking tests and prior work has shown that models with higher task performance tend to be more aligned to human brain activity. However, existing brain-LLM alignment studies have focused on passive, non-creative tasks. Here...

---

### 44. Self-Supervised Foundation Model for Calcium-imaging Population Dynamics

**Authors:** Xinhong Xu, Yimeng Zhang, Qichen Qian, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.04958v2) | 📄 [PDF](https://arxiv.org/pdf/2604.04958v2)

**Summary:** Recent work suggests that large-scale, multi-animal modeling can significantly improve neural recording analysis. However, for functional calcium traces, existing approaches remain task-specific, limiting transfer across common neuroscience objectives. To address this challenge, we propose \textbf{CalM}, a self-supervised neural foundation model trained solely on neuronal calcium traces and adaptable to multiple downstream tasks, including forecasting and decoding. Our key contribution is a pret...

---

### 45. Temporal structure of the language hierarchy within small cortical patches

**Authors:** Julien Gadonneix, Mingfang Zhang, Jérémy Rapin, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.03021v1) | 📄 [PDF](https://arxiv.org/pdf/2604.03021v1)

**Summary:** Speech production requires the rapid coordination of a complex hierarchy of linguistic units, transforming a semantic representation into a precise sequence of articulatory movements. To unravel the neural mechanisms underlying this feat, we leverage recordings from eight 3.2 x 3.2 mm 64-microelectrode arrays implanted in the motor cortex and inferior frontal gyrus of two patients tasked to produce twenty thousand sentences. We show that a hierarchy of linguistic features are robustly encoded in...

---

### 46. Bridging scalp and intracranial EEG in BCI via pretrained neural representations and geometric constraint embedding

**Authors:** Yihang Dong, Changhong Jing, Shuqiang Wang

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.14202v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14202v1)

**Summary:** Electroencephalography (EEG) has become one of the key modalities underpinning brain-computer interfaces (BCIs) due to its high temporal resolution, rapid responsiveness, non-invasiveness, low cost, and portability. However, EEG signals are substantially inferior to intracranial EEG (iEEG) in signal-to-noise ratio and local spatial resolution, whereas iEEG suffers from extremely limited clinical accessibility owing to its invasive nature, hindering widespread application. To address this challen...

---

### 47. Retina gap junctions support the robust perception by warping neural representational geometries along the visual hierarchy

**Authors:** Yang Yue, Shenjian Zhang, Yonghong Tian, et al.

**Published:** 2026-04-03

🔗 [Paper](http://arxiv.org/abs/2604.14200v1) | 📄 [PDF](https://arxiv.org/pdf/2604.14200v1)

**Summary:** Deep Neural Networks (DNNs) are vulnerable to elaborately designed adversarial noise, although they have achieved extraordinary success in many tasks. Compared with DNNs, the human visual system is highly robust. However, it is unclear how the human visual system defends against adversarial attacks, especially the role of the early visual system and its influence on the brain manifold. Due to retina gap junctions being crucial for the denoising function in the early visual system, we combine a r...

---

### 48. Mapping generative AI use in the human brain: divergent neural, academic, and mental health profiles of functional versus socio emotional AI use

**Authors:** Junjie Wang, Xianyang Gan, Dan Liu, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.08594v1) | 📄 [PDF](https://arxiv.org/pdf/2604.08594v1)

**Summary:** The widespread adoption of generative artificial intelligence conversational agents (AICAs) among university students constitutes a novel cognitive social environment whose impact on the maturing brain remains elusive. Combining surveys with high resolution structural MRI, we examined patterns of general, functional, and socio emotional AICA use, academic performance, mental health, and brain structural signatures in a comparatively large sample of 222 young individuals. Across computational ana...

---

### 49. Phase estimation with autoregressive padding (PEAP): addressing inaccuracies and biases in EEG analysis

**Authors:** Miriam Kirchhoff, Johanna Rösch, Maria Ermolova, et al.

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02212v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02212v1)

**Summary:** Accurate phase estimation at the edge of data segments is crucial for EEG applications such as EEG-TMS in offline and real-time data analysis. Our research evaluates the phase estimation performance of four commonly used methods (Phastimate, SSPE, ETP, and PhastPadding) for accuracy and systemic biases, using data from young and elderly healthy controls and chronic stroke participants. To address the identified limitations of the established methods, we introduce Phase Estimation with Autoregres...

---

### 50. Thermodynamic connectivity reveals functional specialization and multiplex organization of extrasynaptic signaling

**Authors:** Giridhar Sunil, Habib Benali, Elkaïoum M. Moutuou

**Published:** 2026-04-02

🔗 [Paper](http://arxiv.org/abs/2604.02057v1) | 📄 [PDF](https://arxiv.org/pdf/2604.02057v1)

**Summary:** Neural communication operates on both fast synaptic transmission and slower, diffusive extrasynaptic signaling, yet how these two modes jointly organize brain function remains unclear. Here, using the complete synaptic and neuropeptidergic connectomes of \emph{Caenorhabditis elegans}, we develop a unified multiplex framework linking anatomical wiring to functional communication. We infer structure-derived functional connectivity from the synaptic connectome using equilibrium principles from stat...

---

## stat.ML

**50 papers**

### 1. Revisiting Active Sequential Prediction-Powered Mean Estimation

**Authors:** Maria-Eleni Sfyraki, Jun-Kun Wang

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18569v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18569v1)

**Summary:** In this work, we revisit the problem of active sequential prediction-powered mean estimation, where at each round one must decide the query probability of the ground-truth label upon observing the covariates of a sample. Furthermore, if the label is not queried, the prediction from a machine learning model is used instead. Prior work proposed an elegant scheme that determines the query probability by combining an uncertainty-based suggestion with a constant probability that encodes a soft constr...

---

### 2. FUSE: Ensembling Verifiers with Zero Labeled Data

**Authors:** Joonhyuk Lee, Virginia Ma, Sarah Zhao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18547v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18547v1)

**Summary:** Verification of model outputs is rapidly emerging as a key primitive for both training and real-world deployment of large language models (LLMs). In practice, this often involves using imperfect LLM judges and reward models since ground truth acquisition can be time-consuming and expensive. We introduce Fully Unsupervised Score Ensembling (FUSE), a method for improving verification quality by ensembling verifiers without access to ground truth correctness labels. The key idea behind FUSE is to c...

---

### 3. Bayesian experimental design: grouped geometric pooled posterior via ensemble Kalman methods

**Authors:** Huchen Yang, Xinghao Dong, Jinlong Wu

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18505v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18505v1)

**Summary:** Bayesian experimental design (BED) for complex physical systems is often limited by the nested inference required to estimate the expected information gain (EIG) or its gradients. Each outer sample induces a different posterior, creating a large and heterogeneous set of inference targets. Existing methods have to sacrifice either accuracy or efficiency: they either perform per-outer-sample posterior inference, which yields higher fidelity but at prohibitive computational cost, or amortize the in...

---

### 4. Random Matrix Theory of Early-Stopped Gradient Flow: A Transient BBP Scenario

**Authors:** Florentin Coeurdoux, Grégoire Ferré, Jean-Philippe Bouchaud

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18450v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18450v1)

**Summary:** Empirical studies of trained models often report a transient regime in which signal is detectable in a finite gradient descent time window before overfitting dominates. We provide an analytically tractable random-matrix model that reproduces this phenomenon for gradient flow in a linear teacher--student setting. In this framework, learning occurs when an isolated eigenvalue separates from a noisy bulk, before eventually disappearing in the overfitting regime. The key ingredient is anisotropy in ...

---

### 5. Conformal Robust Set Estimation

**Authors:** Alejandro Cholaquidis, Emilien Joly, Leonardo Moreno

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18441v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18441v1)

**Summary:** Conformal prediction provides finite-sample, distribution-free coverage under exchangeability, but standard constructions may lack robustness in the presence of outliers or heavy tails. We propose a robust conformal method based on a non-conformity score defined as the half-mass radius around a point, equivalently the distance to its $(\lfloor n/2\rfloor+1)$-nearest neighbour.   We show that the resulting conformal regions are marginally valid for any sample size and converge in probability to a...

---

### 6. Spectral bandits for smooth graph functions

**Authors:** Michal Valko, Rémi Munos, Branislav Kveton, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18420v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18420v1)

**Summary:** Smooth functions on graphs have wide applications in manifold and semi-supervised learning. In this paper, we study a bandit problem where the payoffs of arms are smooth on a graph. This framework is suitable for solving online learning problems that involve graphs, such as content-based recommendation. In this problem, each item we can recommend is a node and its expected rating is similar to its neighbors. The goal is to recommend items that have high expected ratings. We aim for the algorithm...

---

### 7. Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning

**Authors:** Hen Davidov, Nachshon Cohen, Oren Kalinsky, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18419v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18419v1)

**Summary:** Large language models (LLMs) using chain-of-thought reasoning often waste substantial compute by producing long, incorrect responses. Abstention can mitigate this by withholding outputs unlikely to be correct. While most abstention methods decide to withhold outputs before or after generation, dynamic mid-generation abstention considers early termination of unpromising reasoning traces at each token position. Prior work has explored empirical variants of this idea, but principled guidance for th...

---

### 8. Adaptive Kernel Selection for Kernelized Diffusion Maps

**Authors:** Othmane Aboussaad, Adam Miraoui, Boumediene Hamzi, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18402v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18402v1)

**Summary:** Selecting an appropriate kernel is a central challenge in kernel-based spectral methods. In \emph{Kernelized Diffusion Maps} (KDM), the kernel determines the accuracy of the RKHS estimator of a diffusion-type operator and hence the quality and stability of the recovered eigenfunctions. We introduce two complementary approaches to adaptive kernel selection for KDM. First, we develop a variational outer loop that learns continuous kernel parameters, including bandwidths and mixture weights, by dif...

---

### 9. Overcoming Selection Bias in Statistical Studies With Amortized Bayesian Inference

**Authors:** Jonas Arruda, Sophie Chervet, Paula Staudt, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18319v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18319v1)

**Summary:** Selection bias arises when the probability that an observation enters a dataset depends on variables related to the quantities of interest, leading to systematic distortions in estimation and uncertainty quantification. For example, in epidemiological or survey settings, individuals with certain outcomes may be more likely to be included, resulting in biased prevalence estimates with potentially substantial downstream impact. Classical corrections, such as inverse-probability weighting or explic...

---

### 10. Symmetry Guarantees Statistic Recovery in Variational Inference

**Authors:** Daniel Marks, Dario Paccagnan, Mark van der Wilk

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18310v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18310v1)

**Summary:** Variational inference (VI) is a central tool in modern machine learning, used to approximate an intractable target density by optimising over a tractable family of distributions. As the variational family cannot typically represent the target exactly, guarantees on the quality of the resulting approximation are crucial for understanding which of its properties VI can faithfully capture. Recent work has identified instances in which symmetries of the target and the variational family enable the r...

---

### 11. Horospherical Depth and Busemann Median on Hadamard Manifolds

**Authors:** Yangdi Jiang, Xiaotian Chang, Cyrus Mostajeran

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18242v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18242v1)

**Summary:** \We introduce the horospherical depth, an intrinsic notion of statistical depth on Hadamard manifolds, and define the Busemann median as the set of its maximizers. The construction exploits the fact that the linear functionals appearing in Tukey's half-space depth are themselves limits of renormalized distance functions; on a Hadamard manifold the same limiting procedure produces Busemann functions, whose sublevel sets are horoballs, the intrinsic replacements for halfspaces. The resulting depth...

---

### 12. mlr3torch: A Deep Learning Framework in R based on mlr3 and torch

**Authors:** Sebastian Fischer, Lukas Burk, Carson Zhang, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18152v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18152v1)

**Summary:** Deep learning (DL) has become a cornerstone of modern machine learning (ML) praxis. We introduce the R package mlr3torch, which is an extensible DL framework for the mlr3 ecosystem. It is built upon the torch package, and simplifies the definition, training, and evaluation of neural networks for both tabular data and generic tensors (e.g., images) for classification and regression. The package implements predefined architectures, and torch models can easily be converted to mlr3 learners. It also...

---

### 13. Distributional Off-Policy Evaluation with Deep Quantile Process Regression

**Authors:** Qi Kuang, Chao Wang, Yuling Jiao, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18143v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18143v1)

**Summary:** This paper investigates the off-policy evaluation (OPE) problem from a distributional perspective. Rather than focusing solely on the expectation of the total return, as in most existing OPE methods, we aim to estimate the entire return distribution. To this end, we introduce a quantile-based approach for OPE using deep quantile process regression, presenting a novel algorithm called Deep Quantile Process regression-based Off-Policy Evaluation (DQPOPE). We provide new theoretical insights into t...

---

### 14. Towards E-Value Based Stopping Rules for Bayesian Deep Ensembles

**Authors:** Emanuel Sommer, Rickmer Schulte, Sarah Deubner, et al.

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18089v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18089v1)

**Summary:** Bayesian Deep Ensembles (BDEs) represent a powerful approach for uncertainty quantification in deep learning, combining the robustness of Deep Ensembles (DEs) with flexible multi-chain MCMC. While DEs are affordable in most deep learning settings, (long) sampling of Bayesian neural networks can be prohibitively costly. Yet, adding sampling after optimizing the DEs has been shown to yield significant improvements. This leaves a critical practical question: How long should the sequential sampling ...

---

### 15. Boltzmann Machine Learning with a Parallel, Persistent Markov chain Monte Carlo method for Estimating Evolutionary Fields and Couplings from a Protein Multiple Sequence Alignment

**Authors:** Sanzo Miyazawa

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.18022v1) | 📄 [PDF](https://arxiv.org/pdf/2604.18022v1)

**Summary:** The inverse Potts problem for estimating evolutionary single-site fields and pairwise couplings in homologous protein sequences from their single-site and pairwise amino acid frequencies observed in their multiple sequence alignment would be still one of useful methods in the studies of protein structure and evolution. Since the reproducibility of fields and couplings are the most important, the Boltzmann machine method is employed here, although it is computationally intensive. In order to redu...

---

### 16. Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization

**Authors:** Junyoung Yang, Kyungmin Kim, Sangdon Park

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.17984v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17984v1)

**Summary:** Uncertainty quantification is crucial in safety-critical systems, where decisions must be made under uncertainty. In particular, we consider the problem of online uncertainty quantification, where data points arrive sequentially. Online conformal prediction is a principled online uncertainty quantification method that dynamically constructs a prediction set at each time step. While existing methods for online conformal prediction provide long-run coverage guarantees without any distributional as...

---

### 17. Efficient Diffusion Models under Nonconvex Equality and Inequality constraints via Landing

**Authors:** Kijung Jeon, Michael Muehlebach, Molei Tao

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.17838v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17838v1)

**Summary:** Generative modeling within constrained sets is essential for scientific and engineering applications involving physical, geometric, or safety requirements (e.g., molecular generation, robotics). We present a unified framework for constrained diffusion models on generic nonconvex feasible sets $Σ$ that simultaneously enforces equality and inequality constraints throughout the diffusion process. Our framework incorporates both overdamped and underdamped dynamics for forward and backward sampling. ...

---

### 18. Improving reproducibility by controlling random seed stability in machine learning based estimation via bagging

**Authors:** Nicholas Williams, Alejandro Schuler

**Published:** 2026-04-20

🔗 [Paper](http://arxiv.org/abs/2604.17694v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17694v1)

**Summary:** Predictions from machine learning algorithms can vary across random seeds, inducing instability in downstream debiased machine learning estimators. We formalize random seed stability via a concentration condition and prove that subbagging guarantees stability for any bounded-outcome regression algorithm. We introduce a new cross-fitting procedure, adaptive cross-bagging, which simultaneously eliminates seed dependence from both nuisance estimation and sample splitting in debiased machine learnin...

---

### 19. Prior-Fitted Functional Flow: In-Context Generative Models for Pharmacokinetics

**Authors:** César Ojeda, Niklas Hartung, Wilhelm Huisinga, et al.

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17670v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17670v1)

**Summary:** We introduce Prior-Fitted Functional Flows, a generative foundation model for pharmacokinetics that enables zero-shot population synthesis and individual forecasting without manual parameter tuning. We learn functional vector fields, explicitly conditioned on the sparse, irregular data of an entire study population. This enables the generation of coherent virtual cohorts as well as forecasting of partially observed patient trajectories with calibrated uncertainty. We construct a new open-access ...

---

### 20. Diverse Dictionary Learning

**Authors:** Yujia Zheng, Zijian Li, Shunxing Fan, et al.

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17568v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17568v1)

**Summary:** Given only observational data $X = g(Z)$, where both the latent variables $Z$ and the generating process $g$ are unknown, recovering $Z$ is ill-posed without additional assumptions. Existing methods often assume linearity or rely on auxiliary supervision and functional constraints. However, such assumptions are rarely verifiable in practice, and most theoretical guarantees break down under even mild violations, leaving uncertainty about how to reliably understand the hidden world. To make identi...

---

### 21. Contraction and Hourglass Persistence for Learning on Graphs, Simplices, and Cells

**Authors:** Mattie Ji, Indradyumna Roy, Vikas Garg

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17548v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17548v1)

**Summary:** Persistent homology (PH) encodes global information, such as cycles, and is thus increasingly integrated into graph neural networks (GNNs). PH methods in GNNs typically traverse an increasing sequence of subgraphs. In this work, we first expose limitations of this inclusion procedure. To remedy these shortcomings, we analyze contractions as a principled topological operation, in particular, for graph representation learning. We study the persistence of contraction sequences, which we call Contra...

---

### 22. Algorithmic Contiguity from Low-Degree Heuristic II: Predicting Detection-Recovery Gaps

**Authors:** Zhangsong Li

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17410v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17410v1)

**Summary:** The low-degree polynomial framework has emerged as a powerful tool for providing evidence of statistical-computational gaps in high-dimensional inference. For detection problems, the standard approach bounds the low-degree advantage through an explicit orthonormal basis. However, this method does not extend naturally to estimation tasks, and thus fails to capture the \emph{detection-recovery gap phenomenon} that arises in many high-dimensional problems. Although several important advances have b...

---

### 23. StrEBM: A Structured Latent Energy-Based Model for Blind Source Separation

**Authors:** Yuan-Hao Wei

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17381v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17381v1)

**Summary:** This paper proposes StrEBM, a structured latent energy-based model for source-wise structured representation learning. The framework is motivated by a broader goal of promoting identifiable and decoupled latent organization by assigning different latent dimensions their own learnable structural biases, rather than constraining the entire latent representation with a single shared energy. In this sense, blind source separation is adopted here as a concrete and verifiable testbed, through which th...

---

### 24. LASER: Low-Rank Activation SVD for Efficient Recursion

**Authors:** Ege Çakar, Ketan Ali Raghu, Lia Zheng

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17224v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17224v1)

**Summary:** Recursive architectures such as Tiny Recursive Models (TRMs) perform implicit reasoning through iterative latent computation, yet the geometric structure of these reasoning trajectories remains poorly understood. We investigate the activation manifold of TRMs during recursive unrolling and find that activations occupy an effectively linear, low-dimensional subspace whose principal directions can be tracked dynamically with cheap power iterations. This suggests that weight-sharing concentrates it...

---

### 25. PAC-Bayes Bounds for Gibbs Posteriors via Singular Learning Theory

**Authors:** Chenyang Wang, Yun Yang

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17219v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17219v1)

**Summary:** We derive explicit non-asymptotic PAC-Bayes generalization bounds for Gibbs posteriors, that is, data-dependent distributions over model parameters obtained by exponentially tilting a prior with the empirical risk. Unlike classical worst-case complexity bounds based on uniform laws of large numbers, which require explicit control of the model space in terms of metric entropy (integrals), our analysis yields posterior-averaged risk bounds that can be applied to overparameterized models and adapt ...

---

### 26. Symplectic Inductive Bias for Data-Driven Target Reachability in Hamiltonian Systems

**Authors:** Zhuo Ouyang, Jixian Liu, Enrique Mallada

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17213v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17213v1)

**Summary:** Inductive bias refers to restrictions on the hypothesis class that enable a learning method to generalize effectively from limited data. A canonical example in control is linearity, which underpins low sample-complexity guarantees for stabilization and optimal control. For general nonlinear dynamics, by contrast, guarantees often rely on smoothness assumptions (e.g., Lipschitz continuity) which, when combined with covering arguments, can lead to data requirements that grow exponentially with the...

---

### 27. Forecast Sports Outcomes under Efficient Market Hypothesis: Theoretical and Experimental Analysis of Odds-Only and Generalised Linear Models

**Authors:** Kaito Goto, Naoya Takeishi, Takehisa Yairi

**Published:** 2026-04-19

🔗 [Paper](http://arxiv.org/abs/2604.17194v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17194v1)

**Summary:** Converting betting odds into accurate outcome probabilities is a fundamental challenge in order to use betting odds as a benchmark for sports forecasting and market efficiency analysis. In this study, we propose two methods to overcome the limitations of existing conversion methods. Firstly, we propose an odds-only method to convert betting odds to probabilities without using historical data for model fitting. While existing odds-only methods, such as Multiplicative, Shin, and Power exist, they ...

---

### 28. A proposal for PU classification under Non-SCAR using clustering and logistic model

**Authors:** Konrad Furmanczyk, Kacper Paczutkowski

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.17130v1) | 📄 [PDF](https://arxiv.org/pdf/2604.17130v1)

**Summary:** The present study aims to investigate a cluster cleaning algorithm that is both computationally simple and capable of solving the PU classification when the SCAR condition is unsatisfied. A secondary objective of this study is to determine the robustness of the LassoJoint method to perturbations of the SCAR condition. In the first step of our algorithm, we obtain cleaning labels from 2-means clustering. Subsequently, we perform logistic regression on the cleaned data, assigning positive labels f...

---

### 29. Convergence theory for Hermite approximations under adaptive coordinate transformations

**Authors:** Yahya Saleh

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.16975v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16975v1)

**Summary:** Recent work has shown that parameterizing and optimizing coordinate transformations using normalizing flows, i.e., invertible neural networks, can significantly accelerate the convergence of spectral approximations. We present the first error estimates for approximating functions using Hermite expansions composed with adaptive coordinate transformations. Our analysis establishes an equivalence principle: approximating a function $f$ in the span of the transformed basis is equivalent to approxima...

---

### 30. Neighbor Embedding for High-Dimensional Sparse Poisson Data

**Authors:** Noga Mudrik, Adam S. Charles

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.16932v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16932v1)

**Summary:** Across many scientific fields, measurements often represent the number of times an event occurs. For example, a document can be represented by word occurrence counts, neural activity by spike counts per time window, or online communication by daily email counts. These measurements yield high-dimensional count data that often approximate a Poisson distribution, frequently with low rates that produce substantial sparsity and complicate downstream analysis. A useful approach is to embed the data in...

---

### 31. Covariance-Based Structural Equation Modeling in Small-Sample Settings with $p>n$

**Authors:** Hiroki Hasegawa, Aoba Tamura, Yukihiko Okada

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.16894v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16894v1)

**Summary:** Factor-based Structural Equation Modeling (SEM) relies on likelihood-based estimation assuming a nonsingular sample covariance matrix, which breaks down in small-sample settings with $p>n$. To address this, we propose a novel estimation principle that reformulates the covariance structure into self-covariance and cross-covariance components. The resulting framework defines a likelihood-based feasible set combined with a relative error constraint, enabling stable estimation in small-sample settin...

---

### 32. Extraction of informative statistical features in the problem of forecasting time series generated by It{ô}-type processes

**Authors:** Victor Korolev, Mikhail Ivanov, Tatiana Kukanova, et al.

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.16865v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16865v1)

**Summary:** In this paper, we consider the problem of extraction of most informative features from time series that are regarded as observed values of stochastic processes satisfying the It{ô} stochastic differential equations with unknown random drift and diffusion coefficients. We do not attract any additional information and use only the information contained in the time series as it is. Therefore, as additional features, we use the parameters of statistically adjusted mixture-type models of the observed...

---

### 33. A Mechanism Study of Delayed Loss Spikes in Batch-Normalized Linear Models

**Authors:** Peifeng Gao, Wenyi Fang, Yang Zheng, et al.

**Published:** 2026-04-18

🔗 [Paper](http://arxiv.org/abs/2604.16809v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16809v1)

**Summary:** Delayed loss spikes have been reported in neural-network training, but existing theory mainly explains earlier non-monotone behavior caused by overly large fixed learning rates. We study one stylized hypothesis: normalization can postpone instability by gradually increasing the effective learning rate during otherwise stable descent. To test this hypothesis at theorem level, we analyze batch-normalized linear models. Our flagship result concerns whitened square-loss linear regression, where we d...

---

### 34. How to Approximate Inference with Subtractive Mixture Models

**Authors:** Lena Zellinger, Nicola Branchini, Lennert De Smet, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16714v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16714v1)

**Summary:** Classical mixture models (MMs) are widely used tractable proposals for approximate inference settings such as variational inference (VI) and importance sampling (IS). Recently, mixture models with negative coefficients, called subtractive mixture models (SMMs), have been proposed as a potentially more expressive alternative. However, how to effectively use SMMs for VI and IS is still an open question as they do not provide latent variable semantics and therefore cannot use sampling schemes for c...

---

### 35. DARLING: Detection Augmented Reinforcement Learning with Non-Stationary Guarantees

**Authors:** Argyrios Gerogiannis, Yu-Han Huang, Venugopal V. Veeravalli

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16684v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16684v1)

**Summary:** We study model-free reinforcement learning (RL) in non-stationary finite-horizon episodic Markov decision processes (MDPs) without prior knowledge of the non-stationarity. We focus on the piecewise-stationary (PS) setting, where both the reward and transition dynamics can change an arbitrary number of times. We propose Detection Augmented Reinforcement Learning (DARLING), a modular wrapper for PS-RL that applies to both tabular and linear MDPs, without knowledge of the changes. Under certain cha...

---

### 36. Fairness Constraints in High-Dimensional Generalized Linear Models

**Authors:** Yixiao Lin, James Booth

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16610v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16610v1)

**Summary:** Machine learning models often inherit biases from historical data, raising critical concerns about fairness and accountability. Conventional fairness interventions typically require access to sensitive attributes like gender or race, but privacy and legal restrictions frequently limit their use. To address this challenge, we propose a framework that infers sensitive attributes from auxiliary features and integrates fairness constraints into model training. Our approach mitigates bias while prese...

---

### 37. Phase transitions in Doi-Onsager, Noisy Transformer, and other multimodal models

**Authors:** Kyunghoo Mun, Matthew Rosenzweig

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16288v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16288v1)

**Summary:** We study phase transitions for repulsive-attractive mean-field free energies on the circle. For a $\frac{1}{n+1}$-periodic interaction whose Fourier coefficients satisfy a certain decay condition, we prove that the critical coupling strength $K_c$ coincides with the linear stability threshold $K_\#$ of the uniform distribution and that the phase transition is continuous, in the sense that the uniform distribution is the unique global minimizer at criticality. The proof is based on a sharp coerci...

---

### 38. Adaptive multi-fidelity optimization with fast learning rates

**Authors:** Come Fiegel, Victor Gabillon, Michal Valko

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16239v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16239v1)

**Summary:** In multi-fidelity optimization, biased approximations of varying costs of the target function are available. This paper studies the problem of optimizing a locally smooth function with a limited budget, where the learner has to make a tradeoff between the cost and the bias of these approximations. We first prove lower bounds for the simple regret under different assumptions on the fidelities, based on a cost-to-bias function. We then present the Kometo algorithm which achieves, with additional l...

---

### 39. Enhancing AI and Dynamical Subseasonal Forecasts with Probabilistic Bias Correction

**Authors:** Hannah Guan, Soukayna Mouatadid, Paulo Orenstein, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16238v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16238v1)

**Summary:** Decision-makers rely on weather forecasts to plant crops, manage wildfires, allocate water and energy, and prepare for weather extremes. Today, such forecasts enjoy unprecedented accuracy out to two weeks thanks to steady advances in physics-based dynamical models and data-driven artificial intelligence (AI) models. However, model skill drops precipitously at subseasonal timescales (2 - 6 weeks ahead), due to compounding errors and persistent biases. To counter this degradation, we introduce pro...

---

### 40. A Bayesian Updating Framework for Long-term Multi-Environment Trial Data in Plant Breeding

**Authors:** Stephan Bark, Waqas Ahmed Malik, Maryna Prus, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16203v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16203v1)

**Summary:** In variety testing, multi-environment trials (MET) are essential for evaluating the genotypic performance of crop plants. A persistent challenge in the statistical analysis of MET data is the estimation of variance components, which are often still inaccurately estimated or shrunk to exactly zero when using residual (restricted) maximum likelihood (REML) approaches. At the same time, institutions conducting MET typically possess extensive historical data that can, in principle, be leveraged to i...

---

### 41. Sample Complexity Bounds for Stochastic Shortest Path with a Generative Model

**Authors:** Jean Tarbouriech, Matteo Pirotta, Michal Valko, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16111v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16111v1)

**Summary:** We study the sample complexity of learning an $ε$-optimal policy in the Stochastic Shortest Path (SSP) problem. We first derive sample complexity bounds when the learner has access to a generative model. We show that there exists a worst-case SSP instance with $S$ states, $A$ actions, minimum cost $c_{\min}$, and maximum expected cost of the optimal policy over all states $B_{\star}$, where any algorithm requires at least $Ω(SAB_{\star}^3/(c_{\min}ε^2))$ samples to return an $ε$-optimal policy w...

---

### 42. The Harder Path: Last Iterate Convergence for Uncoupled Learning in Zero-Sum Games with Bandit Feedback

**Authors:** Côme Fiegel, Pierre Ménard, Tadashi Kozuno, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16087v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16087v1)

**Summary:** We study the problem of learning in zero-sum matrix games with repeated play and bandit feedback. Specifically, we focus on developing uncoupled algorithms that guarantee, without communication between players, the convergence of the last-iterate to a Nash equilibrium. Although the non-bandit case has been studied extensively, this setting has only been explored recently, with a bound of $\mathcal{O}(T^{-1/8})$ on the exploitability gap. We show that, for uncoupled algorithms, guaranteeing conve...

---

### 43. Stylistic-STORM (ST-STORM) : Perceiving the Semantic Nature of Appearance

**Authors:** Hamed Ouattara, Pierre Duthon, Pascal Houssam Salmane, et al.

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.16086v1) | 📄 [PDF](https://arxiv.org/pdf/2604.16086v1)

**Summary:** One of the dominant paradigms in self-supervised learning (SSL), illustrated by MoCo or DINO, aims to produce robust representations by capturing features that are insensitive to certain image transformations such as illumination, or geometric changes. This strategy is appropriate when the objective is to recognize objects independently of their appearance. However, it becomes counterproductive as soon as appearance itself constitutes the discriminative signal. In weather analysis, for example, ...

---

### 44. Collective Kernel EFT for Pre-activation ResNets

**Authors:** Hidetoshi Kawase, Toshihiro Ota

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15742v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15742v1)

**Summary:** In finite-width deep neural networks, the empirical kernel $G$ evolves stochastically across layers. We develop a collective kernel effective field theory (EFT) for pre-activation ResNets based on a $G$-only closure hierarchy and diagnose its finite validity window. Exploiting the exact conditional Gaussianity of residual increments, we derive an exact stochastic recursion for $G$. Applying Gaussian approximations systematically yields a continuous-depth ODE system for the mean kernel $K_0$, the...

---

### 45. Algebraic Invariants of Lightning Self-Attention

**Authors:** Yulia Alexandr, Hao Duan, Guido Montúfar

**Published:** 2026-04-17

🔗 [Paper](http://arxiv.org/abs/2604.15632v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15632v1)

**Summary:** We study the polynomial coefficients of lightning self-attention as coordinates of an algebraic variety. We identify linear and nonlinear families of algebraic invariants, including Chow-type, low-rank, Veronese-type, and Sylvester resultant-based constraints.

---

### 46. PRIM-cipal components analysis

**Authors:** Tianhao Liu, Daniel Andrés Díaz-Pachón, J. Sunil Rao

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15538v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15538v1)

**Summary:** Supervised No Free Lunch Theorems (NFLTs) are well studied, yet unsupervised NFLTs remain underexplored. For elliptical distributions, we prove that there exist two equally optimal, scientifically meaningful bump-hunting strategies that are exact opposites, with no universal winner. Specifically, peeling $k$ orthogonal dimensions from $\mathbb{R}^d$ ($d \ge k$), retaining an inter-quantile region of probability $1-α$ per peeled dimension, maximizes total variance and Frobenius norm when the $k$ ...

---

### 47. Spurious Predictability in Financial Machine Learning

**Authors:** Sotirios D. Nikolopoulos

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15531v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15531v1)

**Summary:** Adaptive specification search generates statistically significant backtests even under martingale-difference nulls. We introduce a falsification audit testing complete predictive workflows against synthetic reference classes, including zero-predictability environments and microstructure placebos. Workflows generating significant walk-forward evidence in these environments are falsified. For passing workflows, we quantify selection-induced performance inflation using an absolute magnitude gap lin...

---

### 48. One-Shot Generative Flows: Existence and Obstructions

**Authors:** Panos Tsimpos, Daniel Sharp, Youssef Marzouk

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15439v2) | 📄 [PDF](https://arxiv.org/pdf/2604.15439v2)

**Summary:** We study dynamic measure transport for generative modelling in the setting of a stochastic process $X_\bullet$ whose marginals interpolate between a source distribution $P_0$ and a target distribution $P_1$ while remaining independent, i.e., when $(X_0,X_1)\sim P_0\otimes P_1$.   Conditional expectations of this process $X_\bullet$ define an ODE whose flow map transports from $P_0$ to $P_1$. We discuss when such a process induces a \emph{straight-line flow}, namely one whose pointwise accelerati...

---

### 49. Structural interpretability in SVMs with truncated orthogonal polynomial kernels

**Authors:** Víctor Soto-Larrosa, Nuria Torrado, Edmundo J. Huertas

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15285v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15285v1)

**Summary:** We study post-training interpretability for Support Vector Machines (SVMs) built from truncated orthogonal polynomial kernels. Since the associated reproducing kernel Hilbert space is finite-dimensional and admits an explicit tensor-product orthonormal basis, the fitted decision function can be expanded exactly in intrinsic RKHS coordinates. This leads to Orthogonal Representation Contribution Analysis (ORCA), a diagnostic framework based on normalized Orthogonal Kernel Contribution (OKC) indice...

---

### 50. Amortized Optimal Transport from Sliced Potentials

**Authors:** Minh-Phuc Truong, Khai Nguyen

**Published:** 2026-04-16

🔗 [Paper](http://arxiv.org/abs/2604.15114v1) | 📄 [PDF](https://arxiv.org/pdf/2604.15114v1)

**Summary:** We propose a novel amortized optimization method for predicting optimal transport (OT) plans across multiple pairs of measures by leveraging Kantorovich potentials derived from sliced OT. We introduce two amortization strategies: regression-based amortization (RA-OT) and objective-based amortization (OA-OT). In RA-OT, we formulate a functional regression model that treats Kantorovich potentials from the original OT problem as responses and those obtained from sliced OT as predictors, and estimat...

---

