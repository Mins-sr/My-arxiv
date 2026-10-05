# arXiv Daily Digest - 2026-10-05

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis

**Authors:** Keerthi Kaashyap, Dennis Anthony, Akshay Krishnan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03717v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03717v1)

**Summary:** This paper examines the role of Novel View Synthesis (NVS) in geometric representation learning. In principle, NVS should reason about 3D scene structure, thereby enabling transferable multi-view geometric representations. Yet, existing encoder-based NVS methods yield poor representations. This is not because of a lack of supervisory signal, but rather due to inconspicuous architectural choices: \textit{spatially expressive decoders} that dilute representational capabilities of the scene encoder...

---

### 2. 4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes

**Authors:** Ruihong Shen, Žiga Kovačič, Peter Kulits, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03715v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03715v1)

**Summary:** We introduce 4DCodeBench, a benchmark for 4D inverse graphics through code generation, in which agents reconstruct dynamic scenes from video as executable graphics programs. To accomplish this, agents must translate visual observations into compact representations of scene structure and dynamics, by implementing abstractions such as physical simulations to reproduce complex behavior. To evaluate this capability, we curate a set of real-world videos and construct synthetic scenes spanning diverse...

---

### 3. What Should World Models Forget? Stratified Retention for Continual Adaptation

**Authors:** Nishit Anand, Ramani Duraiswami, Dinesh Manocha

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03713v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03713v1)

**Summary:** Continual learning treats degradation on previously seen data as evidence of failure, a convention inherited from settings with a stationary prediction target, where a correct label remains correct indefinitely. World models do not satisfy this condition. Their prediction target is the environment, which changes, so knowledge that was accurate when acquired may later become false, and discarding it is required behavior rather than a defect. Non-stationary ground truth is well studied in the conc...

---

### 4. EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras

**Authors:** Kush Hari, Justin Kerr, Nidhya Shivakumar, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03710v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03710v1)

**Summary:** Inspired by human vision, we introduce a framework using active gaze to enable fine-grained bimanual manipulation with only a single stereo camera. EyeRobot 2.0 physically attends to a 3D fixation point in the scene by swiveling two eye viewpoints to center their gaze on it. The resulting images are processed foveally by allocating more visual tokens to the image centers, focusing computation on task-relevant features. Such Active Visual Fixation (AVF) requires carefully coordinated gaze during ...

---

### 5. Transcriptome-informed multi-modal AI for predicting neoadjuvant therapy response from breast cancer biopsies

**Authors:** Jungkyu Park, Dhruva Biswas, Joseph Cappadona, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03693v1)

**Summary:** Scarcity of labeled data limits development of deep learning biomarkers in oncology. We develop a two-stage AI model predicting pathological complete response (pCR) to neoadjuvant therapy in breast cancer. The first stage learns the transcriptome from histopathology using 8,742 patients across 32 cancer types, corroborated by pathologist review and spatial agreement with measured expression. This simplifies the second stage to predicting pCR from inferred expression and clinical variables. Devel...

---

### 6. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

**Authors:** Hui Chen, Xuan Qi, James Xu Zhao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03675v1)

**Summary:** LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them...

---

### 7. Revisiting Input Time-frequency Representations in Multi-pitch Estimation for Vocal Ensembles

**Authors:** Junyoung Koh, Hao-Wen Dong

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03656v1)

**Summary:** Multi-pitch estimation in vocal ensembles is challenging because singers occupy overlapping pitch ranges and often sing at closely spaced fundamental frequencies, causing their harmonics to overlap in time-frequency representations. Existing models commonly use harmonic constant-Q transform (HCQT)-based representations to provide frequency-adaptive resolution, at the cost of expensive feature extraction when training mixtures are generated on the fly. We revisit this design and compare HCQT with...

---

### 8. MRVQ: One Resident Index for Dimension- and Rate-Elastic Vector Search

**Authors:** Sean Culatana, Shang-En Huang, Kang Li

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03651v1)

**Summary:** Dense-retrieval services must switch among embedding-prefix dimensions and index bit rates as latency, quality, and memory budgets change. Tuning a quantizer separately for each rate gives the best quality, but the retrieval tier then holds several code streams and quantizer states at once. We introduce Matryoshka Residual Vector Quantization (MRVQ), a post-hoc residual quantizer for frozen embeddings. Its maximum-rate code can be truncated two ways: dropping residual stages lowers the rate, and...

---

### 9. On-Board Anomaly Detection for Efficient Marine Environmental Monitoring

**Authors:** Thomas Goudemant, Clotilde Szywala, Benjamin Francesconi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03649v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03649v1)

**Summary:** Marine ecosystems are impacted by various threats such as oil spills, algal blooms, and sediment floods, which disrupt habitats, wildlife, and human activities. Advances in satellite imagery and Artificial Intelligence (AI) have enhanced our capabilities for early detection and mitigation of such hazards. In this paper, we propose a marine event detection pipeline for Earth observation satellites equipped with multi- or hyperspectral sensors. Our approach includes a self-supervised neural networ...

---

### 10. Do Large Language Models Know Colombian Law? A Reliability Benchmark for the Colombian Legal System

**Authors:** Rubén Manrique, Michelle Castellanos, Jorge Morales, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03639v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03639v1)

**Summary:** Large language models (LLMs) are increasingly used to support legal practice, education, and research, yet their reliability in national legal systems outside the United States remains largely undocumented. We introduce an expert-validated benchmark for evaluating LLM reliability on the Colombian legal system. The benchmark comprises 1,042 items spanning ten areas of law and three question formats (closed multiple-choice, semi-open, and open-ended IRAC), built through a human-in-the-loop pipelin...

---

### 11. LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation

**Authors:** Ziqi Ma, Shreya Sharma, Mohamed El Banani, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03636v1)

**Summary:** Camera-controlled video models are rapidly advancing toward long generation horizons and complex camera control. A key failure mode is 3D inconsistency: as the camera moves, objects lose permanence and scene structures shift. Existing post-training techniques, which assign a single scalar reward to the entire generation, are poorly suited to correcting these inconsistencies over long horizons. We introduce LoGo, which blends global and spatially localized rewards for camera-controlled video mode...

---

### 12. Credit Where It Matters: Dependency-Aware Policy Optimization for Terminal Agents

**Authors:** Yu Li, Guangfeng Cai, Long-Fei Li, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03634v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03634v1)

**Summary:** Terminal-using agents benefit from reinforcement learning (RL) in coding, debugging, and other multi-step terminal tasks. In these tasks, later commands often depend on information or intermediate results produced by earlier commands. However, existing trajectory-level and step-level credit assignment methods do not explicitly trace the read-write dependencies through which commands affect the final outcome. Consequently, training signals could still be assigned to irrelevant operations, weakeni...

---

### 13. NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents

**Authors:** Lijie Ding, Changwoo Do

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03631v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03631v1)

**Summary:** Designing a scientific instrument tests whether language-model agents can do physics rather than recall it, provided the grading cannot be argued with. We introduce NeutronGym, to our knowledge the first executable environment for neutron instrument design: agents build instruments through validating tools, McStas ray-traces what they build, and a level-resolved ladder grades syntax, runtime, structure and science with no LLM judge. Procedural families supply unlimited instances of a fixed layou...

---

### 14. Depth as Time in One-Step Generative Models

**Authors:** Arnold Caleb Asiimwe, William Yang, Sanghyuk Chun, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03626v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03626v1)

**Summary:** The recent wave of one-step generative models, which compress the multi-step trajectory of diffusion via either distillation or learned flow maps, has reached an inflection point where they can generate high-quality images. Here, we ask a natural question that follows from these advances: what happens to the denoising trajectory of multi-step diffusion when generation is compressed into a single forward pass? We offer an empirical observation we call \textit{depth as time}: the denoising computa...

---

### 15. Low-Cost Video--Time Priors as a Strong Baseline for EEG--fNIRS Emotion Regression on Familiar Videos

**Authors:** Minghao Kong, Jiurun Chen, Ying Gao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03618v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03618v1)

**Summary:** Continuous emotion regression estimates moment-to-moment valence and arousal while a viewer watches a video. In familiar-video deployment, responses fron training participant-specific estimate, and prior-dominating fixed fusion tests whether physiology adds residual correction. In five-fold subject-held-out evaluation on 24was within 0.05 and 0.32 MAE of fusion in the internal and external evaluations, respectively. Source-explicit ablations showed that video identity and within-video tine accou...

---

### 16. When a Correct Reward Is Not Enough: Diagnosing and Guiding PPO in an Analytically Solved Broker-Trader Game

**Authors:** Siu Tung Wong, Carlo Campajola

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03598v1)

**Summary:** Reinforcement learning (RL) is increasingly used for financial optimal-control problems when complex dynamics make analytical strategies difficult to obtain. There are financial mathematics literactures which provides many solved models whose equations and controls could evaluate and guide learning; we ask whether RL can exploit these results.   We place a proximal policy optimisation (PPO) agent in an analytically solved continuous-time broker--trader game. PPO replaces the broker and chooses i...

---

### 17. HazardWeaver: Scientific Route Selection for Hazard Analysis Agents

**Authors:** Wangshu Zhu, Xueqi Cheng, Liang Wu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03591v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03591v1)

**Summary:** Understanding and assessing natural hazards is essential for disaster preparedness and risk reduction. Recent advances in large language models have spurred growing interest in AI agents for hazard analysis, particularly their ability to integrate scientific data, models, and tools into automated workflows. However, effective automation requires agents to determine which scientific methods are appropriate for a given event and executable with the available data and tools. As new evidence and exe...

---

### 18. Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks

**Authors:** Neeraj Karamchandani, Piyush Nagasubramaniam, Xinhong Xie, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03585v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03585v1)

**Summary:** Security benchmarks for LLM-based agents often report the attack success rate (ASR) as a measure of model robustness and use these scores to compare different models and defense mechanisms, assuming that they describe the security of the agent. In this paper, we explore whether it also influences the benchmark's measurement.   To measure the effect of the benchmark representation, we introduce threat-preserving representation sensitivity (TPRS), which measures how much the ASR changes when we ch...

---

### 19. Rethinking What to Cache in Few-Step Diffusion Transformers: Solver-Aware Target Selection

**Authors:** Shuo Yang, Lihao Fang, Yi Zhang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03577v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03577v1)

**Summary:** Diffusion Transformers (DiTs) can generate high-quality images and videos, but generating each sample requires multiple costly DiT forward passes. Two common ways to accelerate DiT sampling are step distillation, which reduces the number of sampling steps, and caching, which skips some DiT evaluations by reusing a tensor computed at an earlier step. Most caching methods decide in advance which tensor to reuse. After distillation, adjacent sampling steps are farther apart. Reusing a tensor across...

---

### 20. HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents

**Authors:** Alham Fikri Aji, Faiz Rizki Ramadhan, Zayd M. K. Zuhri, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03574v1)

**Summary:** We introduce HyperBrowseComp, a multilingual and multimodal browsing benchmark comprising 423 manually authored and human-validated questions across 13 languages, written by native or highly proficient speakers. Questions are designed to be extremely challenging. Each question targets a concise, publicly verifiable answer whose discovery requires locating obscure evidence, following multi-step clue chains, or inspecting heterogeneous sources such as videos, scanned documents, images, or maps. Ea...

---

### 21. Learning to Assess Heartbeat Observability for mmWave Heart-Rate Sensing

**Authors:** Yuxuan Hu, Shilin Shan, Jianfei Yang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03570v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03570v1)

**Summary:** Contactless heart-rate sensing with millimeter-wave (mmWave) radar requires assessing whether individual measurements support reliable estimation. We study learning to assess heartbeat observability, defined as the readability of the heartbeat component in an acquired phase spectrum, for selective heart-rate estimation. Coherent superposition of scatterer returns can suppress this component even under similar macroscopic observation geometry, motivating assessment directly from acquired measurem...

---

### 22. Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial Agent Workflows

**Authors:** Jermyn Zhen Yong Bek, Zhuang Qiang Bok, Zhongtian Sun

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03564v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03564v1)

**Summary:** Financial AI agents must do more than retrieve facts: investment workflows require correct quantitative execution, reliable use of procedural resources, and auditable structured outputs. We introduce FinSkillBench, an evaluation suite of 2,603 point in time episodes across 12 subtasks in portfolio construction, risk management, and fundamental analysis, with hidden regenerable ground truth and task specific deterministic verifiers. Executing 17,820 episodes across 9 models and 3 resource conditi...

---

### 23. Cephalonauts One: A deep fMRI dataset for decoding naturalistic speech in the human brain

**Authors:** Antoine Collas, Louis Jalouzot, Géraud Ilinca, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03558v1)

**Summary:** Cephalonauts One is a whole-brain 3 Tesla (3T) functional magnetic resonance imaging (fMRI) dataset recorded while subjects listened to audio podcasts. Three healthy subjects underwent multiple scanning sessions, each consisting of five 15-minute runs, while listening to podcasts in their native language. With 30 hours of fMRI data per subject, the current release is the deepest available fMRI dataset using naturalistic speech stimuli. The dataset pairs brain activity with the corresponding podc...

---

### 24. Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis

**Authors:** Wenlong Zhang, Zhengbo Jiao, Chenxu Zhang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03548v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03548v1)

**Summary:** Generating progressively harder reasoning problems requires synthesis procedures that adapt as the task distribution evolves. Existing task-level recursion reuses generated problems as seeds but leaves the construction harness unchanged. We present task-harness co-evolution, a framework for recursive harness self-improvement (RSI) in reasoning-data synthesis. Online self-improvement converts intermediate solver failures into reusable skills during generation. Post-task self-improvement revises s...

---

### 25. Beyond Trained Models: Compiling GNNs for a Sound Explainer Benchmark

**Authors:** Steve Azzolin, Francesco Paolo Nerini, Stefano Teso, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03526v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03526v1)

**Summary:** Explainers for Graph Neural Networks (GNNs) are commonly evaluated by their plausibility, i.e., how well their explanations recover a predefined ground truth, such as a motif planted in the data. This protocol implicitly assumes that a GNN trained on such data relies on the intended motif. Although prior work has questioned this assumption, plausibility remains widespread. First, we show that the assumption is violated on several widely used benchmarks, where, e.g., degree statistics alone suffi...

---

### 26. From Benchmarks to Production: A Text-to-SQL System for Complex Financial Data

**Authors:** Arijit Sehanobish, Bruno Gomes Coelho, Guillaume Michel, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03524v1)

**Summary:** General-purpose Text-to-SQL systems achieve strong performance on academic benchmarks like Spider and BIRD, where schemas are relatively shallow and column values are often human readable. In production financial databases, where concepts are stored as opaque integer keys rather than human-readable strings, these methods fall below 50%, as even simple queries require multiple joins and filter predicates reference opaque IDs. We present Financial LINking Text-to-SQL (FLINT), a domain-specialized ...

---

### 27. Reasoning Models Are Accurate but Unsound on Identification

**Authors:** Arman Behnam, Binghui Wang

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03519v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03519v1)

**Summary:** A reasoning model asked whether a causal effect is recoverable from observational data can fail in two ways: it refuses an identifiable query or answers a nonidentifiable one. The latter is more consequential, as no observational data can validate the claimed formula. Measuring this failure requires queries that are provably non-identifiable, which prior evaluations lack, and grading that accepts correct formulas in any equivalent form, which string matching cannot provide. We build CERTID, a fo...

---

### 28. Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation

**Authors:** Ziyi Wang, Junchi Yao, Heqian Qiu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03510v1)

**Summary:** Recent advances in autoregressive video generation have improved temporal consistency over extended durations, yet interactive storytelling requires more than continuous scene extension: a new shot may combine characters and backgrounds from different historical shots. Whole prompt retrieval can overlook the distinct reference needs of individual components, while directly combining all historical memories may introduce unrelated visual content. To address these problems, we present Weave Forcin...

---

### 29. Efficient Reasoning Training Does Not Always Harm CoT Faithfulness and Monitorability

**Authors:** Samuel Lewis-Lim, Xingwei Tan, Mario Sanger, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03509v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03509v1)

**Summary:** Chain-of-thought (CoT) reasoning allows humans to inspect how large language models reach their answers, and oversee model behaviour. This reasoning comes at an increased inference cost, motivating efficient methods that train models to solve tasks using fewer tokens. However, a common concern is that such training may cause models to skip important reasoning steps, so the CoT no longer faithfully reflects the model's decision. It is unclear whether or when this occurs in practice, since differe...

---

### 30. Certified Mechanistic Edits: Behavioral Guarantees for Skill Removal and Preservation

**Authors:** Md Sazid Uddin, Md. Khairul Alam Mazumder, M. F. Mridha

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03502v1)

**Summary:** Mechanistic edits (ablations, weight edits, activation steering) are the standard tools for unlearning a harmful capability from a neural network while preserving useful ones. Current approaches validate their effects only by testing, which can never cover an entire continuous region of inputs. Prior work at the interpretability-verification boundary certifies descriptions of a model: what a circuit computes, or whether it faithfully explains the whole. We instead certify the behavioral effect o...

---

### 31. Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models

**Authors:** Yukiya Horiba, Koshiro Aoki, Shunsuke Yasuki, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03498v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03498v1)

**Summary:** Adversarial patches can disrupt Vision-Language-Action (VLA) models by manipulating visual observations, leading to failures in robot control. However, it remains poorly understood which internal mechanisms underlie these failures and how targeted interventions can mitigate them. In this work, we mechanistically analyze VLA representations using a sparse autoencoder (SAE) and identify a feature whose activation strongly correlates with the presence of an adversarial patch. Based on this analysis...

---

### 32. AREX: Affine-Residual Exponential Integrator for Few-Step Sampling in Flow Matching

**Authors:** Shizheng Lin, Soon Hoe Lim, N. Benjamin Erichson

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03483v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03483v1)

**Summary:** We introduce AREX, a training-free sampler for pretrained flow matching models that uses the target mean and covariance to capture an analytically tractable part of the sampling dynamics. We show that the velocity field of the moment-matched Gaussian target is the $L^2$-optimal affine approximation to the marginal velocity field. This motivates decomposition of the learned dynamics into an affine component over the whole sampling path, determined by the first two target moments, and a neural res...

---

### 33. MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation

**Authors:** Chenzhi Liu, Yue Zhang, Jiehong Lin, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03476v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03476v1)

**Summary:** Long-horizon mobile manipulation presents significant challenges due to compounding execution errors and capacity interference between locomotion and arm control. While recent Vision-Language-Action models excel at short-horizon tasks, they lack the hierarchical reasoning required for multi-stage objectives. Furthermore, existing hierarchical agents suffer from rigid sub-task mapping, inflexible replanning, and a lack of continuous learning. To address these limitations, we introduce MobiAgent, ...

---

### 34. Single or Multiple Policies for Phase-Structured Reinforcement Learning?

**Authors:** Guilhem Loussouarn, Nancy Nayak, Kin K. Leung

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03475v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03475v1)

**Summary:** Many reinforcement-learning (RL) problems are non-stationary yet structured and can be decomposed into phases, each with its own transition probabilities and reward functions. When the phase sequence is known, the common solution augments the state with information to satisfy the Markovian property and applies standard RL techniques. However, prior work finds that the multi-policy approach for different phases can outperform a single state-augmented policy shared among the phases, for reasons th...

---

### 35. Preserving Anatomical Continuity: Three-Stage Pipeline for Colon Segmentation in 3D Abdominal CT Scans

**Authors:** Deshan Kalupahana, Sonit Singh, Praveen Ravindran, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03467v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03467v1)

**Summary:** Accurate colon segmentation from CT images is essential for colorectal disease analysis, yet deep learning based methods often produce disconnected predictions due to complex anatomy. This study introduces a three-stage, topology-preserving segmentation pipeline to address this issue. The first stage performs initial deep learning-based segmentation, followed by centreline bridging to reconnect disjoint regions and a reconstruction stage to refine continuity. Evaluations on TotalSegmentator and ...

---

### 36. A Near-Zero Monitor Readout Is Not Evidence of Behavioral Control

**Authors:** Zhe Zhou, Tianhua Tao

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03458v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03458v1)

**Summary:** Post-training with verifiable rewards can induce reward hacking, motivating the use of monitors within the training objective rather than solely for offline auditing. We show that a low monitor readout does not identify whether such an intervention controls behavior. In a code-generation environment whose dominant exploit is available at the start of the reasoning trace, we train policies against three monitors that pass the same offline gate: an in-domain activation probe and two penalties cond...

---

### 37. Measure Less, Know More: Self-Supervised Test-Time Feature Acquisition

**Authors:** Eeshaan Jain, Linus Bleistein, Bart Deplancke, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03454v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03454v1)

**Summary:** Recent progress in multimodal, high-dimensional learning has enabled foundation models to process heterogeneous, large-scale data. However, at test time, acquiring all features or modalities can be prohibitively costly and often redundant. Sequentially selecting informative modalities is therefore critical, yet challenging when the downstream task or prediction target is unknown. To this end, we introduce ECHO-$k$, a task-agnostic and self-supervised learning principle for modality acquisition: ...

---

### 38. Corrupted but Correct: Why Vision-Language Models Lie to Themselves Internally

**Authors:** Arun Josephraj Arokiaraj, Zekun Wu, Adriano Koshiyama

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03445v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03445v1)

**Summary:** A targeted adversarial perturbation can drive a vision-language model's (VLM's) teacher-forced training loss for a fixed target caption to near zero, yet the same model, allowed to generate freely, produces the original, correct description with no trace of the target. We call this dissociation the train/inference gap, and give it a precise mechanistic account on Qwen2.5-VL-7B-Instruct using a controlled two-stage PGD attack on 200 held-out COCO images. First, we show that image-level pixel stat...

---

### 39. OptiSelect: How does the Optimizer Shape Data Curriculum?

**Authors:** Simin Fan, Alireza Abdollahpoorrostam, Martin Jaggi

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03432v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03432v1)

**Summary:** Online data selection has demonstrated substantial efficiency gains for LLM pretraining by training on the most valuable candidates within each batch. Since a candidate's value is realized through its effective model update, principled selection should account for the optimizer step, which reshapes the raw gradient before it updates model parameters. We formalize this optimizer-aware selection paradigm as OptiSelect and present the first systematic study of how the optimizer shapes data selectio...

---

### 40. Jumping the Line: Exploiting Length Predictions in LLM Scheduling

**Authors:** Yuyang Dai, Rana Shahout, Mahmood Sharif

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03430v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03430v1)

**Summary:** Efficient request scheduling is increasingly important for reducing completion time in large language model (LLM) serving. Size-based policies such as Shortest Job First prioritize shorter requests, but output lengths are unknown before generation, so practical schedulers rely on predicted lengths. We introduce JIL, an attack on prediction-based LLM schedulers that manipulates the scheduling signal to obtain higher priority and reduce completion time. Using TRAIL as a case study, JIL optimizes a...

---

### 41. Becoming Suspicious Across Borders: Algorithmic Extraterritoriality and AI-Driven Financial Surveillance

**Authors:** Georgios Pavlidis, Savvas Chatzichristofis, Eleni Gavriil

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03425v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03425v1)

**Summary:** Suspicion is an important, yet elusive concept in anti-money laundering and counter-terrorist financing (AML/CFT), which allows for intervention below the threshold of proof. In its traditional form, suspicion can be understood as a situated legal judgement by human actors within identifiable jurisdictions. It is argued that this understanding is no longer adequate. As artificial intelligence (AI) becomes an integral part of financial surveillance, suspicion is increasingly produced through data...

---

### 42. Rethinking Epistemic Uncertainty in Node Classification through Information Growth

**Authors:** Emma Meneghini, Francesco Ferrini, Bruno Lepri, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03418v1)

**Summary:** Epistemic uncertainty should decrease as additional information about the data-generating process (DGP) becomes available to the predictor. Yet, existing graph evidential deep learning (EDL) methods for node classification typically construct epistemic uncertainty from graph-specific properties and evaluate it on downstream tasks such as out-of-distribution detection, which do not test its reducibility as information about the DGP increases. To make reducibility directly testable, we introduce a...

---

### 43. ForestQuery: Boundary-Aware and Spatially Anchored Query Learning for Unified Forest Point Cloud Segmentation

**Authors:** Zhihao Zhan, Le Tao, Yifei Tian, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03403v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03403v1)

**Summary:** Forest point cloud segmentation is fundamental for fine-grained 3D forest scene understanding, yet remains challenging due to irregular tree structures, severe occlusions, density variations, and ambiguous instance boundaries. Recent query-based forest segmentation methods have shown promise for unified semantic and instance prediction, but they still insufficiently exploit forest-specific spatial structure and account for boundary uncertainty. In this paper, we propose ForestQuery, a boundary-a...

---

### 44. DriftTTS: Few-Step Text-to-Speech Without Distillation via Distribution-Matching Drift

**Authors:** Mohammad Nur Hossain Khan, Subrata Biswas, Bashima Islam

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03390v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03390v1)

**Summary:** Few-step neural text-to-speech models often rely on short- ened diffusion or flow-matching schedules, or on distillation from pretrained multi-step teachers. To avoid these depen- dencies, we present DriftTTS, a few-step mel-spectrogram generator trained without a generative teacher, distillation, or adversarial discrimination. DriftTTS uses a distribution- matching drift objective in a mel-domain feature space defined by raw mels and a frozen masked-autoencoder encoder pretrained on the same LJ...

---

### 45. Benchmarking Candidate Coverage in Typed Decision Models

**Authors:** Jiawen Lu, Tongtong Wu

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03387v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03387v1)

**Summary:** Typed decision models return choices or distributions over answer options supplied at request time. Accuracy with complete options does not establish whether a model recognizes that a reference answer is missing or avoids rejecting valid candidates. We present a paired candidate-coverage benchmark protocol and an initial evaluation of Laya and Jev across AG News, DBpedia, Emotion, and TREC. The models receive identical frozen texts and requests: 300 calibration and 589 test texts yield 23,932 pr...

---

### 46. CVE2AP: Automated Generation of PDDL-Encoded Attack Paths via Large Language Models

**Authors:** Lin Cui, Vincenzo Scotti, Raffaela Mirandola

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03383v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03383v1)

**Summary:** Attack Path (AP) modeling is fundamental to cybersecurity analysis, where the Planning Domain Definition Language (PDDL) has been widely adopted to encode APs into formal and machine-verifiable representations for automated reasoning about vulnerability exploitation, attack progression, and their potential impacts. However, existing AP modeling approaches largely rely on expert-driven manual construction, limiting their scalability and ability to keep pace with rapidly evolving cyber threats. La...

---

### 47. Multilingual GSM-Symbolic: What determines capability transfer across languages?

**Authors:** Kenneth Enevoldsen, Riley Herchert, Sofie Mosegaard, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03367v1)

**Summary:** We understand little about how capabilities acquired in one language carry over to another, or what governs this transfer: evaluations rely on incomparable, saturation-prone datasets and rarely examine its determinants jointly. Identifying what predicts transfer would let us avoid exhaustive evaluation across all language pairs and let developers target the factors that limit performance in low-resource languages. To evaluate cross-lingual capability transfer, we introduce Multilingual GSM-Symbo...

---

### 48. Geometry Meets Physics: Data-Efficient Pre-Training for Unstructured Neural PDE Solvers

**Authors:** Luis Medrano-Navarro, Giacomo Baldan, Qiang Liu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03363v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03363v1)

**Summary:** Neural surrogate models for Partial Differential Equations (PDEs) on unstructured 3D geometries are often limited by poor generalization and the high cost of generating large-scale training datasets. Consequently, pre-training on massive datasets of related PDE dynamics has emerged as a critical alternative to enhance the robustness and scalability of these models. However, this strategy is neither compute- nor data-efficient, as it relies on massive pre-computed data that is very costly to gene...

---

### 49. Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT

**Authors:** Joery Ariën de Vries, Neil David Lawrence, Zhenwen Dai

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03361v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03361v1)

**Summary:** Critic-free reinforcement fine-tuning (RFT) for agentic large language models is often done through GRPO-style methods, which compute a group baseline over repeated rollouts to reduce target variance. However, this setup is ill-suited to agents acting in stateful environments such as live services or security sandboxes, where repeated rollouts are impractical to obtain and aggressive updates entrench the noise of long, sparsely verified trajectories. We propose \textit{Follow the Winners} (FTW),...

---

### 50. ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models

**Authors:** Hainiu Xu, Vítor N. Lourenço, Mohnish Dubey, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03356v1)

**Summary:** Large Language Model (LLM) agents are increasingly deployed in high-stakes settings such as industrial maintenance and equipment fault troubleshooting, where workers occupy a variety of roles. A capable agent must therefore act in a way that is calibrated to user's role: taking actions and providing information that respect the role's knowledge and capability boundaries. Unlike coding, where mistakes are usually recoverable, agent responses in these settings are enacted on physical equipment, an...

---

## cs.CL

**50 papers**

### 1. Language Models that Play Chess and Explain Their Moves

**Authors:** Adithya Bhaskar, Jeffrey Cheng, Danqi Chen

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03695v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03695v1)

**Summary:** Modern chess engines are silent experts: they play at a superhuman level, but do not offer explanations for their play. On the other hand, language models (LMs) can generate plausible-sounding explanations, but their weak playing strength limits the utility of their explanations. We introduce Queen, a 4B-parameter chess-language model that can explain its moves and plans while playing at the level of a typical Grandmaster. Our novel framework enables domain-specific reasoning through complementa...

---

### 2. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

**Authors:** Hui Chen, Xuan Qi, James Xu Zhao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03675v1)

**Summary:** LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them...

---

### 3. Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models

**Authors:** Seo Hyun Kim, Sunwoo Hong, Younwoo Choi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03665v1)

**Summary:** Masked diffusion language models (dLMs) offer a promising parallel alternative to autoregressive models for complex reasoning. However, they face a distinct credit-assignment challenge, since a few commitments during denoising sharply reduce the uncertainty over the remaining masked positions and shape much of the response. Most post-training recipes for dLMs do not use this signal to decide which tokens to train on: they typically train on the final text or assign rewards to whole denoising ste...

---

### 4. World Embedding Benchmark

**Authors:** Yiqi Liu, Ruifeng Yuan, Yang Wang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03632v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03632v1)

**Summary:** Physical fidelity has received increasing attention in world models and video generation, yet how video representations encode physical information remains less understood. We introduce the World Embedding Benchmark, comprising 8,000 controlled simulation cases from 80 families spanning fluid mechanics, solid mechanics, dynamics, and optics & electromagnetism. Each case pairs a rendered video with simulation-derived physical annotations, supporting three complementary tasks: text-video retrieval...

---

### 5. FALCON: A Model and Dataset Agnostic Framework for Synthetic Data Generation for NL2SQL Pairs

**Authors:** Darian Lee, Shannon Rumsey, Jack St. Clair, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03625v1)

**Summary:** Relational databases are among the most widely deployed forms of structured knowledge, and natural language access to them requires grounding language onto schema entities and relations while handling the ambiguity inherent in how people phrase requests. Existing synthetic NL-to-SQL data generation methods largely ignore this ambiguity and produce oversimplified queries that fail to prepare models for the complexity of real-world structured knowledge access. We present FALCON, a framework that g...

---

### 6. Writerslogic at the CLEF 2026 SimpleText Track: Multi-Candidate LLM Simplification and Stacked Complexity Spotting

**Authors:** David L. Condrey

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03567v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03567v1)

**Summary:** We describe the Writerslogic team's participation in the CLEF 2026 SimpleText shared task, addressing Task 1 (text simplification) and Task 2 (complexity spotting). For Task 1, we develop a multi-candidate generation pipeline using GPT-4o-mini that produces five simplification candidates per sentence at varying temperatures, then selects the best candidate using a reference-free scoring heuristic that rewards compression, source word retention, Cochrane Plain Language Summary vocabulary usage, a...

---

### 7. Writerslogic at PAN 2026: Process over Content for Robust Detection under Domain Shift

**Authors:** David L. Condrey

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03565v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03565v1)

**Summary:** We describe the Writerslogic systems for three PAN at CLEF 2026 shared tasks (Reasoning Trajectory Detection, Voight-Kampff Generative AI Detection, and Multi-Author Writing Style Analysis), unified by a shared analytical framework: feature robustness under distribution shift is governed by support overlap between training and test distributions, not by training-set effect size. This yields a taxonomy (domain-anchored, domain-portable, domain-invariant) that explains why generator-specific featu...

---

### 8. Author Representation Strategies for Zero-Shot Authorship Attribution: A Comparative Study of LLM-Based and Embedding-Based Approaches

**Authors:** Nudrat Habib, Tosin Adewumi, Sana Sabah Al-Azzawi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03531v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03531v1)

**Summary:** Authorship Attribution (AA) requires capturing fine-grained stylistic characteristics, making it particularly challenging in zero-shot (ZS) settings where no task-specific supervision is available. In this work, we investigate the effect of author representations on ZS AA by evaluating a label-only prompting baseline together with three author representation strategies: representative writing samples, LLM-generated descriptions, and style embeddings (LISA). The first three approaches perform att...

---

### 9. Divergence controls entropy in distillation

**Authors:** Nicolas Zucchet, Scott W. Linderman

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03529v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03529v1)

**Summary:** Distillation has become a core primitive of large language model training, but its properties are not yet well understood. We take an entropic perspective, studying how the entropy of the student depends on the data and the divergence that define the distillation objective. We prove that forward KL inflates the entropy of the student above that of the teacher. Since cross-entropy training is a special case, this yields an identity that we verify quantitatively in pretraining and supervised finet...

---

### 10. Structured Composition of Verifiable Atomic Insights for Table-to-Report Generation

**Authors:** Teng Lin, Xinyu Liu, Nan Tang

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03525v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03525v1)

**Summary:** Table-to-report generation refers to the task of automatically generating article-level analyt- ical reports from relational tables and is an essential capability for automated data science and decision support. Its central challenge lies in systematically discovering verifiable com- posite insights across tables, attributes, and analytical perspectives, and organizing them into coherent, complete, and traceable evidence chains. Existing methods primarily rely on sequential, reactive data agents...

---

### 11. Learning from Repaired Reasoning: Root-Cause-Guided On-Policy Distillation

**Authors:** Chenglei Shen, Haoyang Yao, Weijie Yu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03515v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03515v1)

**Summary:** On-policy self-distillation (OPSD) uses reference solutions as privileged hindsight to supervise student-generated reasoning trajectories. However, reference-based guidance may explain a correct solution without addressing why the student's own reasoning fails. This reasoning mismatch between the guidance provided and the correction needed can encourage the student to borrow correct conclusions while leaving its reasoning errors unresolved. Moreover, applying the same hindsight throughout the tr...

---

### 12. Single-Pass Uncertainty Heads for Claim-Level Hallucination Detection in Persian Medical Language Models

**Authors:** Mehrdad Ghassabi, Pedram Rostami, Hamidreza Baradaran Kashani, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03482v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03482v1)

**Summary:** Hallucination detection is particularly important for medical language models, but repeated-sampling approaches are expensive and existing uncertainty-head resources do not directly transfer to a new backbone and language. We adapt the LLM Uncertainty Head (LUH) framework to Aya-Expanse-8B-based Persian medical models, using Gaokerena-V and Gaokerena-R as two previously developed backbones. We first examine response variability on a 168-question Iranian medical entrance examination and observe s...

---

### 13. A Near-Zero Monitor Readout Is Not Evidence of Behavioral Control

**Authors:** Zhe Zhou, Tianhua Tao

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03458v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03458v1)

**Summary:** Post-training with verifiable rewards can induce reward hacking, motivating the use of monitors within the training objective rather than solely for offline auditing. We show that a low monitor readout does not identify whether such an intervention controls behavior. In a code-generation environment whose dominant exploit is available at the start of the reasoning trace, we train policies against three monitors that pass the same offline gate: an in-domain activation probe and two penalties cond...

---

### 14. Passing the Test You Trained On: Re-evaluating Prompt-Injection Detectors for LLM Agents

**Authors:** Zhuowen Liu

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03448v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03448v1)

**Summary:** LLM agents increasingly screen tool outputs with small prompt-injection detectors, and teams choose among detectors by their scores on public benchmarks. We ask whether those scores predict how a detector behaves inside an agent. We replay the ground-truth tool calls of two agent benchmarks, AgentDojo and tau-bench, without an LLM to obtain tool outputs that are benign by construction, label injected outputs by differential replay, and evaluate fifteen detectors, including Meta's Prompt Guard 2,...

---

### 15. CLIMB: Confidence-Guided Complementary Evidence for Multimodal Retrieval-Augmented Generation

**Authors:** Hang Gao, Wujiang Xu, Zhixing Zhang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03421v1)

**Summary:** Multimodal large language models (MLLMs) have shown strong visual reasoning abilities, but knowledge-intensive visual question answering often requires external textual evidence beyond the image and the model's parametric knowledge. Existing multimodal RAG systems commonly rely on Top-$K$ retrieval or reranking, which may return redundant passages and provide limited control over whether an answer update is sufficiently supported by the retrieved evidence. We propose \textit{CLIMB}, a training-f...

---

### 16. Benchmarking Candidate Coverage in Typed Decision Models

**Authors:** Jiawen Lu, Tongtong Wu

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03387v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03387v1)

**Summary:** Typed decision models return choices or distributions over answer options supplied at request time. Accuracy with complete options does not establish whether a model recognizes that a reference answer is missing or avoids rejecting valid candidates. We present a paired candidate-coverage benchmark protocol and an initial evaluation of Laya and Jev across AG News, DBpedia, Emotion, and TREC. The models receive identical frozen texts and requests: 300 calibration and 589 test texts yield 23,932 pr...

---

### 17. Multilingual GSM-Symbolic: What determines capability transfer across languages?

**Authors:** Kenneth Enevoldsen, Riley Herchert, Sofie Mosegaard, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03367v1)

**Summary:** We understand little about how capabilities acquired in one language carry over to another, or what governs this transfer: evaluations rely on incomparable, saturation-prone datasets and rarely examine its determinants jointly. Identifying what predicts transfer would let us avoid exhaustive evaluation across all language pairs and let developers target the factors that limit performance in low-resource languages. To evaluate cross-lingual capability transfer, we introduce Multilingual GSM-Symbo...

---

### 18. SyntaxBench: A Statistical Diagnostic Framework for Character-Level Reasoning in Large Language Models

**Authors:** Mohsen Larni, Sobhan Ebrahimi Azar, Pouyan Nahed, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03329v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03329v1)

**Summary:** Large language models are increasingly used where small syntactic errors matter, yet character-level reasoning is still evaluated mostly through isolated probes and aggregate accuracy. We introduce SyntaxBench, a diagnostic benchmark and statistical evaluation framework for character-level reasoning. It contains five core tasks, character counting, letter containment, palindrome detection, edit distance, and longest-string selection, plus index_to_span, a harder substring-extraction stress test....

---

### 19. To Jev or Not? Evaluating the Accuracy and Efficiency of Structured Decision Models for Hate-Speech Moderation

**Authors:** Demetris Paschalides, George Pallis, Marios D. Dikaiakos

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03324v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03324v1)

**Summary:** The scale of online content makes hate-speech moderation challenging, while Large Language Models (LLMs) enable harmful material to be produced and adapted more easily. Moderation therefore requires efficient classifiers that can accommodate different definitions of hate speech. Recent structured decision models accept natural-language criteria and select among specified answers, raising the question of whether they can meet these requirements without task-specific training. We present HATEDECID...

---

### 20. Shrome at Touché: Soft-Vote Ensembling and Counter-Causal Augmentation for Causality Extraction

**Authors:** Roham Zendehdel Nobari, Shayan Sooratgar

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03268v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03268v1)

**Summary:** Touché 2026 extends causality extraction to counter-causal claims: news sentences whose surface form appears causal but whose meaning denies the causation, as in "It is falsely believed that X caused Y." A system that relies on surface cues such as "caused" or "led to" will accept such a sentence as causal and give it the wrong polarity. On the Countercausal News Corpus (CCNC), the task has three subtasks: deciding whether a sentence is causal (detection), locating its cause and effect spans (ex...

---

### 21. Collective Bias Mitigation via Model Routing and Collaboration

**Authors:** Mingzhe Du, Luu Anh Tuan, Xiaobao Wu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03240v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03240v1)

**Summary:** Large language models (LLMs) are increasingly deployed in public health, finance, and governance, requiring both accuracy and societal value alignment. Despite recent advances, LLMs often perpetuate or amplify bias embedded in their training data, posing challenges to fairness. While self-debiasing encourages an LLM to identify and correct its own biases, relying on a single model's intrinsic knowledge may be insufficient to address deeply ingrained stereotypes. To address this limitation, we in...

---

### 22. AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning

**Authors:** Xin Wang, Wenhao Wu, Menghao Zhang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03223v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03223v1)

**Summary:** Long-horizon LLM agents are typically trained with sparse outcome rewards, making trajectory-level objectives too coarse to distinguish the contribution of individual decisions. Step-level credit assignment provides finer-grained supervision, but its estimates can be unreliable because observed returns also depend on subsequent actions, environment transitions, and trajectory length. We propose AdaStep, an Adaptive Step-credit weighting method that controls how strongly each group-derived local ...

---

### 23. StanceEval 2026: The Second Stance Detection Shared Task

**Authors:** Rasha Albalawi, Nuha Albadi, Hamzah Luqman, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03215v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03215v1)

**Summary:** StanceEval 2026 is the second edition of the StanceEval shared task series on stance detection in Arabic social media text. Stance detection aims to identify a writer's stance toward a given topic. Given a tweet and a target, participating systems must determine whether the writer's stance is Favor, Against, or None. This edition focuses on cross-target generalization across two distinct evaluation tracks: Track 1 evaluates thematically related cross-target transfer (testing on Women Driving, re...

---

### 24. Predicting and Repairing Merge Collapse in Large Language Models

**Authors:** Jungseob Lee, Seungyoon Lee, Sugyeong Eo, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03199v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03199v1)

**Summary:** Large language models fine-tuned from a shared base can be merged by averaging their task vectors, but some merges collapse far below the base model, and common merge operators give no warning before evaluation. We show that one statistic of the specialists' task vectors both predicts this collapse and calibrates its repair. The power that averaging removes equals the variance of the task vectors across specialists, our measure of interference. Under a working noise model, the disturbance that a...

---

### 25. KV$^2$: A Self-Refining KV Cache

**Authors:** Johannes Wesch, Danni Liu, Jan Niehues

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03198v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03198v1)

**Summary:** The memory footprint of the key-value (KV) cache constrains the practical use of long-context models, and it dominates cost when one prefilled context must later serve many different queries. In this reusable setting, query-agnostic compression trades cost against quality: lightweight estimators are cheap but less accurate, whereas full-context reconstruction scoring is more accurate yet reprocesses the entire prompt. We introduce KV$^2$, a query-agnostic KV-cache compression method based on sel...

---

### 26. Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It

**Authors:** Jonghyun Song, Haewon Park, Jeonghoon Shim, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03195v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03195v1)

**Summary:** As LLM agents decide on users' behalf which product to buy, which hotel to book, or which paper to cite, a preference for items from certain sources (the sites or services they come from) shapes what users receive and which sources are selected. We study source preference in end-to-end search with 12 agent models across three domains. Comparing items from different sources that satisfy the same requirements at the same position, we find that each model prefers some sources and avoids others in e...

---

### 27. Not Until the Evidence Says So: Teaching LLM Investigators When to Close a Case

**Authors:** Tingzhu Bi, Ping Wang, Meng Ma

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03190v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03190v1)

**Summary:** Accident, defect and outage investigations end with a decision that ordinary question answering never faces: whether the evidence gathered so far is enough to close the case. We study this decision for LLM investigators, which request evidence from a case file, revise their hypotheses, and either close the case with a conclusion grounded in what they read or leave it open and name what is missing. This judgment does not come with capability: an untrained 9B model overstates its evidence in 97% o...

---

### 28. Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective

**Authors:** Han Cui, Jianhao Yan, Yun Luo, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03185v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03185v1)

**Summary:** On-policy distillation (OPD) has become an important approach to language model post-training. However, despite its performance gains, OPD can also collapse into excessively long and repetitive generation, and the mechanism underlying these divergent outcomes remains poorly understood. We explain these outcomes through a reinforcement learning perspective: the teacher implicitly rewards student behaviors, even those it rarely exhibits itself. From this perspective, our experiments show that OPD ...

---

### 29. Hindsight-Guided Rationale Distillation for Rare Disease Diagnosis

**Authors:** Aarav Singh, Animesh Pathak, Navyansh Singh

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03176v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03176v1)

**Summary:** We study hindsight-guided distillation for rare disease diagnosis on ZebraMap: a 1.5B student is fine-tuned on chain-of-thought traces from a 8B teacher that observes the ground-truth diagnosis during generation. Absolute accuracy remains low for all models - the task is hard at this scale - but within this ceiling a filtered variant (StudentF) achieves a small, statistically significant accuracy advantage over the teacher (p < 0.001), concentrated in better-represented diseases. The unfiltered ...

---

### 30. Predicting Steering Vectors and Adapter Weights for Few-Shot Author-Style Transfer

**Authors:** Leonard Popp, Danni Liu, Supriti Sinhamahapatra, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03163v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03163v1)

**Summary:** Adapting large language models to an individual author's style from a few examples is challenging, and scientific writing sharpens the difficulty: formal conventions leave little surface variation, and authors write about their own topics, so extracted ``style'' easily entangles with content. We study style-conditioned abstract generation from a few example abstracts per author and propose three methods: (1) contrastive activation steering, (2) a network that predicts steering vectors, and (3) a...

---

### 31. Investigating the Role of Reasoning-Language Alignment in Monolingual Retrieval-Augmented Generation

**Authors:** Oliver Hauck, Mario Sanz-Guerrero, Katharina von der Wense

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03136v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03136v1)

**Summary:** Reasoning traces improve large language models (LLMs), but current models are trained to reason mostly in English. It has been shown that forcing a model to reason in another language degrades accuracy, even when the reasoning language matches the language of the prompt -- but only for a setting where the model reasons over a short prompt. Here, we ask whether the same holds for retrieval-augmented generation (RAG), where the model must read and integrate a large amount of retrieved evidence in ...

---

### 32. Benchmarking Literature Retrieval for a Model Organism: A Dictyostelium Case Study

**Authors:** Yun Wang, Gad Shaulsky, Tomaž Curk, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03130v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03130v1)

**Summary:** Biological literature retrieval systems are often developed and evaluated using broad biomedical corpora and general-purpose search tasks. However, many curated knowledge bases operate in narrower model-organism domains, where the literature is sparse and terminology is organism-specific. We introduce a retrieval benchmark from dictyBase for Dictyostelium, a model organism in cell and developmental biology. The benchmark consists of curator-generated biological queries linked to PubMed-indexed a...

---

### 33. The Fragility of Trigger-Tag Mechanisms for Misuse Detection in Open-Weight LLMs

**Authors:** Toluwani Aremu, Manit Baser, Mohan Gurusamy, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03124v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03124v1)

**Summary:** Open-weight language models can be downloaded, modified, and deployed beyond their developers' control, limiting the effectiveness of centrally enforced safeguards. Recent work has therefore proposed \emph{trigger-tag} mechanisms that produce a detectable signal when a model is used under a target condition, such as generating phishing contents. Although these mechanisms borrow from established techniques, their use for conditional misuse detection in open-weight LLMs is relatively new. Therefor...

---

### 34. Building Interpretable Feature Representations for Resume-Vacancy Matching by Distilling Production LLM Signals

**Authors:** Ilya Chekin, Vyacheslav Malyugin, Vladimir Chirkov, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03112v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03112v1)

**Summary:** Matching candidates to vacancies is central to recruitment, and a recruiter needs to see why a candidate fits, not only a single opaque relevance score. We provide this evidence as named, interpretable matching dimensions recruiters can act on - eight in our current deployment. We propose a two-part approach. The first is an LLM-based labeler whose prompts and feature definitions were refined from recruiter feedback while it served as an earlier production matching stage. In the current architec...

---

### 35. Ontological Instability and Statistical Amplification: The Paradox of "Humanizing" LLM-Generated Text

**Authors:** Claudiu Creanga, Liviu Dinu

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03110v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03110v1)

**Summary:** Supervised AI-text detectors report high benchmark accuracy, but it is not clear what their decisions are based on. We analyze a RoBERTa-based detector under semantic, structural, and tokenizer-level perturbations, using the M4 dataset (N = 10,000) and controlled generations (N = 300). When Mistral-7B-Instruct was asked to make machine text sound more human, Verb Diversity rose from 0.77 to 0.92 and the outputs became easier to detect. Detection scores appear to track statistical complexity, whi...

---

### 36. Emergent Structure in the Marginal Attention Space of Language Models

**Authors:** Valentino Maiorca, Walter Nelson, Francesco Locatello

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03109v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03109v1)

**Summary:** While representation similarity across independently trained language models is well-documented, how internal mechanics such as attention behave across models remains far less characterized. Inspired by this gap, we examine the structure of post-softmax attention weights by marginalizing over query positions, mapping them into a joint token-head "marginal attention space". Evaluating across 60+ diverse LLMs, we find that different properties emerge when reducing this space along its token and he...

---

### 37. Ask, Relax, or Act? Evaluating Actionable Indeterminacy in LLM Preference Reasoning

**Authors:** Ang Li, Yue Lin, Feifei Kou, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03102v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03102v1)

**Summary:** An LLM agent can recognize uncertainty yet still choose the wrong next step: asking when action is already justified, or seeking clarification when the constraints must change. We formalize actionable indeterminacy: act when an accepted action is shared across all admissible preferences or objectives, clarify when each possibility is feasible but no action is shared, and propose a minimum-cost permitted constraint repair when the request is infeasible. We construct a solver-grounded benchmark sp...

---

### 38. Peer Influence across Heterogeneous AI Models

**Authors:** Frida Nøhr Laustsen, Marie Haahr Petersen, Victoria Popa, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03095v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03095v1)

**Summary:** When two AI agents disagree, who persuades whom? As multi-agent systems increasingly combine language models of different families and sizes, the answer can determine which judgments survive interaction. Measuring persuasion as the probabilistic shift in an agent's decision after a single exchange with a dissenting peer, we test seven open-weight models across three language understanding tasks. We find that persuasion is strong: when models disagree, receivers often abandon their initial judgme...

---

### 39. MintEval: Do LLMs Implement the Trading Strategy You Asked For? A Behavioural-Equivalence Benchmark for Natural-Language-to-Strategy Code

**Authors:** Siyu Wang, Yifan Wang, Yuecheng He

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03080v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03080v1)

**Summary:** Large language models are moving from producing trading signals to writing the code that executes them. The failure mode of the second role is silent: generated code runs, a backtest plots, yet the risk logic that the trader described is not the logic being executed. Existing code benchmarks test functional correctness on unit tests and finance benchmarks test forecasting; neither measures whether an implementation behaves like the strategy that was asked for. We introduce MintEval, a benchmark ...

---

### 40. An automated pipeline for standardised speech-unit annotation in spontaneous dialogue

**Authors:** Hanlu He, Harald Vilhelm Skat-Rørdam, Ingvi Örnólfsson, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03078v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03078v1)

**Summary:** Quantifying conversational dynamics requires reliable identification of interactional units and their temporal boundaries, but speech activity alone does not distinguish conversational turns from listener feedback or within-turn pauses. We present an automated pipeline for extracting turns and backchannels from separate-channel recordings of spontaneous dyadic conversation, designed to provide a consistent first-pass annotation for subsequent human review. The pipeline combines voice activity de...

---

### 41. Unmasking Propaganda: A Comparative Analysis of Masked and Causal Language Models

**Authors:** Claudiu Creanga, Ioachim Lihor, Liviu P. Dinu

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03077v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03077v1)

**Summary:** Propaganda detection is an essential task in natural language processing (NLP), particularly in the context of manipulative political communications. However, identifying specific propaganda techniques presents a significant challenge due to their often subtle nature and reliance on context, making them difficult to distinguish from legitimate persuasive language. Propaganda often involves highlighting certain facts while downplaying or ignoring others to create a desired perception. This biased...

---

### 42. SecJev: Bringing Security Expertise to System One Decision Models

**Authors:** Zheng Chen, Fei Yu, Haohao Huang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03073v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03073v1)

**Summary:** Security workflows need models that turn complex observations and explicit policies into decisions. System One models introduced by Jev return typed predictions and probabilities; security specialization supplies the domain expertise behind those predictions. We introduce SecJev, to our knowledge the first family of Jev-like decision models specialized for security, spanning 0.8B to 9B parameters. Built on Kev's single-pass candidate scorer, SecJev learns Boolean, choice, and ordered decisions f...

---

### 43. HARPO: Hallucination-Aware Reinforcement Learning for Faithful and Creative Language Generation

**Authors:** Tiezheng Yu, Yuxin Jiang, Jinpeng Li, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03063v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03063v1)

**Summary:** Large Language Models (LLMs) are prone to generating hallucinated content, which compromises their reliability in knowledge-intensive tasks. To address this challenge without sacrificing creativity, we propose HARPO, a reinforcement learning framework designed to jointly optimize faithfulness and creativity. HARPO incorporates a Hallucination-Aware Generative Reward Model (HA-GRM), trained via verifiable feedback, to assess both faithfulness and writing quality. A Selective Activation Mechanism ...

---

### 44. The Geometry of Knowledge Accessibility in Large Language Models

**Authors:** Lihu Chen

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03052v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03052v1)

**Summary:** Large language models (LLMs) contain broad knowledge, but they cannot access all of it reliably. We study this problem through knowledge accessibility, which describes whether the knowledge needed for a query can be recalled from the model. We find that knowledge accessibility has a simple geometric structure in the model's representation of the query alone, before any generation. More accessible queries are closer to a center in the representation space, while less accessible queries are farthe...

---

### 45. HyperThink: Text-to-Parameter Hypernetworks for Efficient Reasoning

**Authors:** Donggyun Kim, Jack Lu, Chanwoo Kim, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03039v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03039v1)

**Summary:** Long-form thinking traces can substantially improve the multi-step reasoning performance of large language models (LLMs), but they introduce high inference-time overhead, with latency dominated by sequential decoding. We propose HyperThink, a text-to-parameter approach that amortizes this reasoning computation into a single query-conditioned parameter update: a lightweight hypernetwork reads the question and predicts updates to a small subset of the base LLM's parameters, while a vector-quantize...

---

### 46. Adaptive Second-Order Solvers for Fast Stochastic Diffusion Sampling

**Authors:** Ella Kemperman, Luca Ambrogioni

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03034v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03034v1)

**Summary:** Diffusion models rely on numerical solvers requiring time-discretization, which has a large influence on the tradeoff between sampling cost and quality. However, the computational difficulty of the reverse process varies along the sampling trajectory and across data distributions, making the choice of discretization important. We adapt proportional-integral (PI) step-size control to diffusion, using our diffusion noise-normalised error estimator. Unlike existing adaptive methods in diffusion tha...

---

### 47. Tailoring the Quantization Space for 1-Bit KV Cache Compression

**Authors:** Minsoo Cheong, Donghyun Son, Sungjoo Yoo

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03027v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03027v1)

**Summary:** The key-value (KV) cache becomes a major memory bottleneck in long-context LLM inference, placing substantial pressure on memory capacity and bandwidth. To mitigate this bottleneck, vector quantization (VQ) has emerged as a promising approach for aggressive KV cache compression. However, existing VQ methods degrade substantially in the 1-bit regime. At such extreme compression, each codebook must represent a larger group of channels with a limited set of centroids, making effective use of its ca...

---

### 48. Verifiable, Articulable, and Tacit Components of Preference

**Authors:** Alexander Spangher, Sheldon Huang, Andreas Haupt, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03025v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03025v1)

**Summary:** What makes a short story gripping; a news article newsworthy; or a math proof elegant? These constructs resist articulation or verification; their meaning is at least partially tacit. However, modern AI models are improved primarily via articulated constitutions, rubrics and verifiers (i.e. in RLAIF and RLVR); tacit components of preferences are typically understudied. We introduce a large, labeled preference dataset CreativePreferences, containing 2.8M texts labeled by 317M human preference jud...

---

### 49. ReSCUE: Re-translation with Sentence Commitment for Unsegmented Long-Form Simultaneous Sign Language Translation

**Authors:** Sihan Ren, Gaozheng Li, Yuanshang Quan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03022v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03022v1)

**Summary:** Simultaneous Sign Language Translation (SLT) is critical for real-time communication, yet existing methods remain largely confined to sentence-level, offline settings that assume pre-segmented inputs. These assumptions hinder deployment in realistic scenarios involving continuous, unsegmented video streams. We present ReSCUE, a unified framework for simultaneous SLT on unsegmented long-form sign language videos that aligns training and inference with realistic streaming conditions. ReSCUE combin...

---

### 50. Personalized Automatic Speech Recognition for a Dysarthric and Tracheostomic Speaker using Artificial Conversations

**Authors:** David Nadrchal, Monorama Swain, Florian Schmid, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03017v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03017v1)

**Summary:** This work presents an automatic speech recognition (ASR) system personalized for a Czech speaker with a permanent tracheal stoma and severe dysarthria rendering their speech unintelligible to untrained listeners. We release a public dataset containing 33 annotated hours of the speaker's speech, collected using a novel "artificial conversation" protocol designed for high engagement and dialogue realism. We propose a multi-stage training pipeline based on Whisper Base: fine-tuning on standard Czec...

---

## cs.CV

**50 papers**

### 1. Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis

**Authors:** Keerthi Kaashyap, Dennis Anthony, Akshay Krishnan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03717v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03717v1)

**Summary:** This paper examines the role of Novel View Synthesis (NVS) in geometric representation learning. In principle, NVS should reason about 3D scene structure, thereby enabling transferable multi-view geometric representations. Yet, existing encoder-based NVS methods yield poor representations. This is not because of a lack of supervisory signal, but rather due to inconspicuous architectural choices: \textit{spatially expressive decoders} that dilute representational capabilities of the scene encoder...

---

### 2. MoSE3: Learning World-Space SE(3) at Every Pixel

**Authors:** Jiahuan Cheng, Zhiyi Li, Tian Xia, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03716v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03716v1)

**Summary:** Dense 3D point tracking has been a prominent paradigm for modeling motion in dynamic scenes, but a point track is just a 3-DoF translation curve per pixel: it captures where pixels go, not the rotation of the underlying part, nor which pixels move together as one body. We propose MoSE3, the first feed-forward model that predicts dense SE(3) motion from monocular RGB video, producing full 6-DoF rigid transforms at every pixel in world space. Per-pixel SE(3) motion offers a richer view of how a sc...

---

### 3. 4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes

**Authors:** Ruihong Shen, Žiga Kovačič, Peter Kulits, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03715v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03715v1)

**Summary:** We introduce 4DCodeBench, a benchmark for 4D inverse graphics through code generation, in which agents reconstruct dynamic scenes from video as executable graphics programs. To accomplish this, agents must translate visual observations into compact representations of scene structure and dynamics, by implementing abstractions such as physical simulations to reproduce complex behavior. To evaluate this capability, we curate a set of real-world videos and construct synthetic scenes spanning diverse...

---

### 4. What Should World Models Forget? Stratified Retention for Continual Adaptation

**Authors:** Nishit Anand, Ramani Duraiswami, Dinesh Manocha

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03713v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03713v1)

**Summary:** Continual learning treats degradation on previously seen data as evidence of failure, a convention inherited from settings with a stationary prediction target, where a correct label remains correct indefinitely. World models do not satisfy this condition. Their prediction target is the environment, which changes, so knowledge that was accurate when acquired may later become false, and discarding it is required behavior rather than a defect. Non-stationary ground truth is well studied in the conc...

---

### 5. Decoding the Functional Roles of Register and High-Norm Patch Tokens in Vision Transformers

**Authors:** Neel Varma, Andrew Rufail, Dipika Khullar, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03698v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03698v1)

**Summary:** Self-supervised Vision Transformers (ViTs), such as DINOv2, learn rich visual representations, but the functions of their internal tokens remain poorly understood. Recent architectures introduce dedicated register tokens to reduce high-norm out- lier patch tokens that emerge in background re- gions, yet the semantic and functional roles of both token types have not been fully established. In this paper, we analyze these roles by training sparse autoencoders (SAEs) on register-token and outlier-t...

---

### 6. FlowHMR: Physically Plausible Motion Capture from Video

**Authors:** Zhanke Wang, Chengfeng Zhao, Qing Shuai, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03691v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03691v1)

**Summary:** We present FlowHMR, a framework for recovering physically plausible global 3D human motion from monocular video. Previous learning-based methods typically regress human motion directly from video and train the network with geometric supervision. However, recovering human motion from monocular video is inherently ambiguous in depth, and direct regression tends to collapse toward an averaged solution. Moreover, the recovered motions are not guaranteed to be physically plausible, so physics-based t...

---

### 7. SigLIP2 for aerial fire risk classification

**Authors:** Yunus Serhat Bıçakçı

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03689v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03689v1)

**Summary:** We examine the transfer of a pretrained SigLIP2 image encoder to seven class fire risk classification from aerial imagery. We introduce a reproducible partition of the public FireRisk training mirror and an implementation that records data provenance, preprocessing and model selection. Two initial runs compare a frozen encoder probe with full model adaptation. On the validation partition, full adaptation reaches 63.05% accuracy and 58.94% macro F1, compared with 55.95% and 50.19% for the probe. ...

---

### 8. ProAR: Learning Prospective Reasoning with Autoregressive Video Models

**Authors:** Linghui Shen, Tinghui Zhu, Sheng Zhang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03664v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03664v1)

**Summary:** Autoregressive (AR) video models excel at causal generation, but their reliance on next-chunk prediction confines them to a short-sighted, reactive paradigm. This limitation is particularly consequential for reasoning-oriented generation, where achieving a target outcome through valid intermediate states matters more than local visual plausibility. To address this challenge, we propose Learning Prospective Reasoning with Autoregressive Video Models (ProAR), a novel framework that transforms auto...

---

### 9. On-Board Anomaly Detection for Efficient Marine Environmental Monitoring

**Authors:** Thomas Goudemant, Clotilde Szywala, Benjamin Francesconi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03649v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03649v1)

**Summary:** Marine ecosystems are impacted by various threats such as oil spills, algal blooms, and sediment floods, which disrupt habitats, wildlife, and human activities. Advances in satellite imagery and Artificial Intelligence (AI) have enhanced our capabilities for early detection and mitigation of such hazards. In this paper, we propose a marine event detection pipeline for Earth observation satellites equipped with multi- or hyperspectral sensors. Our approach includes a self-supervised neural networ...

---

### 10. LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation

**Authors:** Ziqi Ma, Shreya Sharma, Mohamed El Banani, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03636v1)

**Summary:** Camera-controlled video models are rapidly advancing toward long generation horizons and complex camera control. A key failure mode is 3D inconsistency: as the camera moves, objects lose permanence and scene structures shift. Existing post-training techniques, which assign a single scalar reward to the entire generation, are poorly suited to correcting these inconsistencies over long horizons. We introduce LoGo, which blends global and spatially localized rewards for camera-controlled video mode...

---

### 11. World Embedding Benchmark

**Authors:** Yiqi Liu, Ruifeng Yuan, Yang Wang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03632v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03632v1)

**Summary:** Physical fidelity has received increasing attention in world models and video generation, yet how video representations encode physical information remains less understood. We introduce the World Embedding Benchmark, comprising 8,000 controlled simulation cases from 80 families spanning fluid mechanics, solid mechanics, dynamics, and optics & electromagnetism. Each case pairs a rendered video with simulation-derived physical annotations, supporting three complementary tasks: text-video retrieval...

---

### 12. Low-Cost Video--Time Priors as a Strong Baseline for EEG--fNIRS Emotion Regression on Familiar Videos

**Authors:** Minghao Kong, Jiurun Chen, Ying Gao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03618v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03618v1)

**Summary:** Continuous emotion regression estimates moment-to-moment valence and arousal while a viewer watches a video. In familiar-video deployment, responses fron training participant-specific estimate, and prior-dominating fixed fusion tests whether physiology adds residual correction. In five-fold subject-held-out evaluation on 24was within 0.05 and 0.32 MAE of fusion in the internal and external evaluations, respectively. Source-explicit ablations showed that video identity and within-video tine accou...

---

### 13. DEPICT: Scoring Text-to-Image Alignment by Answer Agreement

**Authors:** Vasco Ramos, Sandra Godinho Silva, Joao Magalhaes, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03617v1)

**Summary:** Image-text alignment is a core problem in computer vision with applications in caption evaluation, hallucination detection, data curation, and the benchmarking of text-to-image (T2I) generators. As T2I models improve, benchmarking has become demanding, requiring metrics capable of finding a series of issues like missing objects, swapped attributes, miscounts, and ignored negations. Recent work addresses this by fine-tuning evaluators on preference data or by prompting a vision-language model, ei...

---

### 14. ManifoldSplat: Language-Guided Semantic Shape Editing of 3D Gaussian Head Avatars

**Authors:** Antonio Canela, Jordi Sànchez-Riera

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03599v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03599v1)

**Summary:** High-fidelity 3D head avatars have reached near-photorealistic quality. While recent methods enable text-driven manipulation, they struggle to provide fine-grained localized control, often entangling features or lacking geometric consistency. Modifying geometry through natural language currently requires slow per-prompt optimization or compromises identity and rigging. We present ManifoldSplat, the first end-toend framework for language-guided semantic shape editing of animatable 3D Gaussian Spl...

---

### 15. Rethinking What to Cache in Few-Step Diffusion Transformers: Solver-Aware Target Selection

**Authors:** Shuo Yang, Lihao Fang, Yi Zhang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03577v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03577v1)

**Summary:** Diffusion Transformers (DiTs) can generate high-quality images and videos, but generating each sample requires multiple costly DiT forward passes. Two common ways to accelerate DiT sampling are step distillation, which reduces the number of sampling steps, and caching, which skips some DiT evaluations by reusing a tensor computed at an earlier step. Most caching methods decide in advance which tensor to reuse. After distillation, adjacent sampling steps are farther apart. Reusing a tensor across...

---

### 16. DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation

**Authors:** Jiahao Zhan, Yan Wang, Yongrui Ma, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03543v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03543v1)

**Summary:** Streaming video generation has benefited from distribution matching distillation (DMD), which matches the joint distribution of video frames to a video teacher's approximation of the real video distribution. Although this joint matching mitigates drift during autoregressive rollouts, limitations remain in visual quality and semantic alignment. To address these limitations, we propose DuoMatching, a distribution matching framework that approximates the real video distribution through a unified jo...

---

### 17. Feedforward Novel View Synthesis for Heterogeneous Cameras

**Authors:** Meng Wei, Cheng Zhang, Boying Li, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03522v1)

**Summary:** Feed-forward novel view synthesis has recently shown promising results from sparse posed images, but most existing methods assume that context and target views share a fixed camera family. This homogeneous-camera assumption breaks in practical multi-sensor systems, where perspective, fisheye, and panoramic cameras may coexist and where the target projection may be unseen during training. We study feed-forward NVS across heterogeneous central cameras and identify a key ambiguity introduced by tok...

---

### 18. XGenAct: Geometry-Enhanced World Action Models through Cross-Task Generation

**Authors:** Tingting Du, Ziyao Wang, Guoheng Sun, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03516v1)

**Summary:** World action models (WAMs) have advanced robot control by predicting how observations and actions evolve over time. Despite this progress, RGB and action based future prediction does not explicitly address the spatial understanding needed for robot manipulation. Existing efforts often add a limited set of spatial prediction tasks through specialized heads or branches, leaving both the range of spatial supervision and the model architecture fragmented. We introduce XGenAct, a world action model t...

---

### 19. ProgressNet: Sketching and Prompting with a Frozen Text-to-Image Model

**Authors:** Arkaprabha Basu, Chaitat Utintu, Yi-Zhe Song

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03512v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03512v1)

**Summary:** Humans draw progressively: a few strokes, a look at the result, a stroke erased, a prompt revised. Image generators do not work this way. They typically take a finished sketch and produce the image in a single pass, so every edit starts the picture again, and the models that do keep state across turns are driven by text, cannot take a stroke, and are too slow to draw with. We present ProgressNet, a training-free framework that lets a frozen text-to-image model follow a drawing session as it unfo...

---

### 20. Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation

**Authors:** Ziyi Wang, Junchi Yao, Heqian Qiu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03510v1)

**Summary:** Recent advances in autoregressive video generation have improved temporal consistency over extended durations, yet interactive storytelling requires more than continuous scene extension: a new shot may combine characters and backgrounds from different historical shots. Whole prompt retrieval can overlook the distinct reference needs of individual components, while directly combining all historical memories may introduce unrelated visual content. To address these problems, we present Weave Forcin...

---

### 21. Fed-ADApt: Federated Anytime Depth Adaptation for Resource-Aware Medical Image Segmentation

**Authors:** Abhijeet Parida, Zhifan Jiang, Pooneh Roshanitabrizi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03474v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03474v1)

**Summary:** Federated learning (FL) enables collaborative training of medical image segmentation models without sharing raw patient data, yet existing approaches assume a homogeneous compute budget across institutions, limiting participation of low-resource sites. We propose Fed-ADApt, a depth-adaptive federated framework for UNet-based segmentation that jointly addresses low-compute training and inference. Fed-ADApt integrates multi-depth supervision with hierarchical depth-wise aggregation, allowing each ...

---

### 22. UniDynamics: Event-RGB Fusion for Unified Future 4D Dynamic Scene Generation

**Authors:** Daikun Liu, Xin Zhan, Teng Wang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03473v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03473v1)

**Summary:** We propose UniDynamics, a diffusion-based framework for future 4D dynamic scenes (RGB, depth, and optical flow) generation from a single event-RGB pair, without requiring long histories or control priors as in existing methods, while explicitly modeling future motion fields. The core idea is to leverage event streams to offer an alternative motion prior for single-RGB extrapolation, and to enforce geometric and motion constraints throughout generation via multimodal modeling. Specifically, we de...

---

### 23. A Vision-Language Model (VLM)-based Pipeline for End-to-End Procedural Modeling of Field-Grown Maize from Point Clouds

**Authors:** Mozhgan Hadadi, Talukder Z. Jubery, Adarsh Krishnamurthy, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03468v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03468v1)

**Summary:** Editable 3D models of field-grown crops support high-throughput phenotyping and in silico breeding trials, but building them from scanned point clouds requires organ-level segmentation and fitting. Procedural generators can turn an organ-level parameter set into an analysis-suitable 3D model, but obtaining that set requires hours of manual tuning per plant or segmentation models trained on species-specific labels. We present an automated pipeline that reconstructs procedural maize models from ra...

---

### 24. Preserving Anatomical Continuity: Three-Stage Pipeline for Colon Segmentation in 3D Abdominal CT Scans

**Authors:** Deshan Kalupahana, Sonit Singh, Praveen Ravindran, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03467v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03467v1)

**Summary:** Accurate colon segmentation from CT images is essential for colorectal disease analysis, yet deep learning based methods often produce disconnected predictions due to complex anatomy. This study introduces a three-stage, topology-preserving segmentation pipeline to address this issue. The first stage performs initial deep learning-based segmentation, followed by centreline bridging to reconnect disjoint regions and a reconstruction stage to refine continuity. Evaluations on TotalSegmentator and ...

---

### 25. I2CD: Direct Image-to-Convex Decomposition for Simulation-Ready Collision Geometry

**Authors:** Qian Wang, Liam Merz Hoffmeister, Brian Scassellati, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03453v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03453v1)

**Summary:** Physics simulators and motion planners require convex collision geometry, yet image-to-3D generative models output dense, frequently non-manifold visual meshes. Bridging the two today takes a slow, brittle reconstruct-then-decompose pipeline of repair, decimation, and approximate convex decomposition. We present I2CD, which predicts a convex decomposition directly from a single RGB image. Rather than train a new image-to-3D model, I2CD freezes the pretrained Hunyuan3D-2 image-conditioned diffusi...

---

### 26. Corrupted but Correct: Why Vision-Language Models Lie to Themselves Internally

**Authors:** Arun Josephraj Arokiaraj, Zekun Wu, Adriano Koshiyama

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03445v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03445v1)

**Summary:** A targeted adversarial perturbation can drive a vision-language model's (VLM's) teacher-forced training loss for a fixed target caption to near zero, yet the same model, allowed to generate freely, produces the original, correct description with no trace of the target. We call this dissociation the train/inference gap, and give it a precise mechanistic account on Qwen2.5-VL-7B-Instruct using a controlled two-stage PGD attack on 200 held-out COCO images. First, we show that image-level pixel stat...

---

### 27. ChromaGS: Text-Driven Semantic Editing of 4D Gaussian Avatars

**Authors:** Antonio Canela, Jordi Sànchez-Riera

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03441v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03441v1)

**Summary:** We present ChromaGS, a method for real-time, language-guided color editing of animatable 3D Gaussian head avatars. Given a trained animatable avatar, users can instantly modify the color of semantic regions through natural language, with edits applied at render time and no retraining required. Our key insight is to augment each Gaussian primitive with learned soft assignments to semantic regions and decompose colors into region-level base colors and Gaussian-level residuals. This decomposition e...

---

### 28. Depth Hypothesis Guided Iterative Refinement for Event-Image Monocular Depth Estimation

**Authors:** Daikun Liu, Teng Wang, Changyin Sun

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03439v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03439v1)

**Summary:** Event cameras hold excellent dynamic properties, showing great potential for monocular depth estimation (MDE). However, existing methods mainly improve performance by optimizing contextual features, but still struggle with the ill-posed and nonlinear nature of direct full-depth regression. In this paper, we propose HypoDepth, the first event-image monocular depth iterative refinement framework. By introducing a discrete Depth Hypothesis Volume (DHV), we transform the depth regression problem int...

---

### 29. The Shape of Speech: A Geometric Measure of Coarticulation for Speech-Driven 3D Facial Animation

**Authors:** Danzel Serrano, Przemyslaw Musialski

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03436v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03436v1)

**Summary:** Speech-driven 3D facial animation can reproduce recognizable mouth poses. However, it can simplify the motion between them, and that motion carries coarticulation, the way the sounds around each sound shape its articulation. We introduce a geometric measure of this trajectory shaping: lip-path length compared with the shortest route through the vowel, consonant and vowel positions of a speech segment. In contrast to the endpoint chord, this consonant-aware route accounts for obligatory transit a...

---

### 30. OuroReward: Sequential Reward Scheduling for Reinforcement Learning in Text-to-3D Generation

**Authors:** Bingyang Cui, Yujie Zhang, Yiling Xu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03423v1)

**Summary:** Reinforcement learning (RL) for Text-to-3D (T23D) generation requires optimization across multiple quality dimensions such as semantic alignment and texture clarity. Existing methods typically optimize these dimensions simultaneously through multiple reward aggregation, without explicitly modeling inter-dimension dependencies. This can cause imbalanced optimization and persistent interference among conflicting dimensions. To address this limitation, we propose OuroReward, an interference-aware s...

---

### 31. Iterating Consistency Models: Stability, Error Bounds and Noise Schedules

**Authors:** Alessio Spagnoletti, Abdul-Lateef Haji-Ali, Andrés Almansa, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03414v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03414v1)

**Summary:** Consistency models (CMs) have become a leading approach for generating high-quality samples in few steps. However, adding steps can improve or degrade sample quality in ways that are highly sensitive to the schedule and that existing theory does not fully explain. To provide accuracy guarantees and guide CM sampler design, we analyze multistep CM sampling as a composition of noising and approximate denoising operators. Under explicit, verifiable stability assumptions, we derive a non-asymptotic ...

---

### 32. ForestQuery: Boundary-Aware and Spatially Anchored Query Learning for Unified Forest Point Cloud Segmentation

**Authors:** Zhihao Zhan, Le Tao, Yifei Tian, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03403v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03403v1)

**Summary:** Forest point cloud segmentation is fundamental for fine-grained 3D forest scene understanding, yet remains challenging due to irregular tree structures, severe occlusions, density variations, and ambiguous instance boundaries. Recent query-based forest segmentation methods have shown promise for unified semantic and instance prediction, but they still insufficiently exploit forest-specific spatial structure and account for boundary uncertainty. In this paper, we propose ForestQuery, a boundary-a...

---

### 33. Beyond Entropy: Self-Diagnostic Multi-Role Token Optimization for Video Reasoning

**Authors:** Yudong Han, Yong Wang, Zaiquan Yang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03400v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03400v1)

**Summary:** Reinforcement learning with verifiable rewards has substantially advanced multimodal reasoning, yet it remains fundamentally limited by ambiguous token-level credit assignment. While high-entropy token heuristics encourage possibility exploration, naively extending them to video reasoning tends to induce lengthy reasoning, as the model becomes overly reliant on high-entropy visual activations. Alternative approaches that rely on counterfactual-based visual token localization for credit assignmen...

---

### 34. Native Action-Prior Learning from Videos for World Action Models

**Authors:** Zhaochong An, Fei Zhang, Menglin Jia, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03391v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03391v1)

**Summary:** World action models integrate future visual dynamics with robot action prediction, but their scalability remains limited by the need for action-annotated robot trajectories. Observation-only videos contain rich evidence about interaction dynamics, but existing approaches typically use them either to pretrain visual representations that must later be adapted for control, or to infer latent actions that are subsequently grounded to robot commands. We present NAVA-WAM, which introduces native actio...

---

### 35. From Patching to Pruning Visual Computation in Vision Language Models

**Authors:** Rahul Chowdhury, Timothy A Rupprecht, Xuan Shen, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03389v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03389v1)

**Summary:** Vision language models (VLMs) incur substantial inference cost because every visual token is processed by the attention and MLP projections of every decoder layer, even when token-specific visual computation is unnecessary at many depths. We introduce Patch-to-Prune (P2P), inspired by Mechanistic Interpretability, a training-free framework that converts activation patching from a diagnostic tool into an inference-time computation bypass. P2P performs validation-guided forward and backward layer ...

---

### 36. Interpretable Deepfake Detection in Videos via Explicit Forensic Features and Temporal Modeling

**Authors:** Chahira Benhama, Mohand Saïd Allili, Assia Hamadene

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03380v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03380v1)

**Summary:** Deepfake detection in videos remains challenging, as manipulated content may appear visually consistent at the frame level while exhibiting subtle temporal inconsistencies. This paper introduces an interpretable deepfake detection framework that models spatially and temporally coherent facial features in video sequences. Unlike end-to-end deep models relying on implicit representations, the proposed approach explicitly encodes physically grounded forensic cues, enabling transparent analysis and ...

---

### 37. EVEWorld: Physical Evolution Supervision for Embodied World Models

**Authors:** Kaiqi Wang, Songxin Zhang, Zejian Xie, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03374v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03374v1)

**Summary:** Embodied world models enable scalable simulation of embodied interactions for robot learning. However, existing models are prone to Model Laziness, as they focus on visual fidelity at the expense of physical reasoning and lack process-level supervision over the temporal dynamics of manipulated objects. In this work, we propose EVEWorld, a physical evolution-supervision framework for physically consistent target evolution. EVEWorld consists of two components: Instance-Guided Restoration (IGR) and...

---

### 38. LAS-CLIP: A Lightweight Adapter Steering Approach for CLIP's Visual Encoder

**Authors:** Anh-Khoa Dinh-Duc, Duc-Tai Dinh, Tam V. Nguyen, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03370v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03370v1)

**Summary:** CLIP's visual encoder produces only global image representations, limiting its use in region-level tasks. Existing adaptations rely on visual prompting, input masking, or encoder fine-tuning, each compromising pre-trained representations. We propose LAS-CLIP, a Lightweight Adapter Steering approach that keeps every CLIP parameter frozen. A compact MaskAdapter generates per-head, per-layer attention biases from an input mask and injects them into the frozen self-attention layers, steering attenti...

---

### 39. A Fully Automatic Pipeline for 3D Dendrite Instance Segmentation in SBF-SEM

**Authors:** Zewen Zhuo, Ilya Belevich, Eija Jokitalo, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03332v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03332v1)

**Summary:** Accurate three-dimensional (3D) reconstruction of individual dendrites in serial block-face scanning electron microscopy (SBF-SEM) is essential for quantifying structural plasticity in the brain, yet manual annotation at scale is infeasible. We present a fully automatic pipeline for 3D dendrite instance segmentation that unifies YOLOv6-guided Segment Anything Model (SAM) prompting on downsampled slices, iterative two-dimensional mask refinement, random forest 3D instance linking, and instance-aw...

---

### 40. T3lescope: Arbitrary-Resolution High-Fidelity Generative Surface Reconstruction from Images

**Authors:** Atsuhiro Noguchi, Tianhan Xu, Yiming Liang, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03308v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03308v1)

**Summary:** We reconstruct high-fidelity 3D scene meshes from posed multi-view images without per-scene optimization, across scales ranging from single objects to large outdoor scenes. Per-scene optimization methods lack the learned 3D prior needed when observations are sparse or surfaces are glossy or transparent. Existing generative methods leverage such priors to complete geometry in sparsely observed regions, but typically operate at a fixed resolution over a limited spatial extent, trading spatial cove...

---

### 41. Wrong Organ, Right Physics: Transferring Echocardiography Pretraining to Lung Ultrasound for Tuberculosis Screening

**Authors:** Christiaan M. Geldenhuys, Joshua M. Jansen van Vüren, Véronique Suttels, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03290v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03290v1)

**Summary:** Lung ultrasound (LUS) is attractive for tuberculosis (TB) screening at primary-care level, but labelled cohorts are small. Echocardiography carries no such constraint, while sharing the same underlying ultrasound imaging physics, signal processing and B-mode appearance as LUS. We ask whether an encoder pretrained on that high-resource ultrasound domain carries representations that remain usable in the low-resource one. Only the encoder varies, across seventeen encoders spanning three architectur...

---

### 42. HexVIO: Towards All-Day Stereo-Inertial Tracking Through Commodity DSPs

**Authors:** Patrick Wolf, Mateo de Mayo, Daniel Cremers

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03283v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03283v1)

**Summary:** The ability of a device to localize itself within its surroundings is a fundamental prerequisite for spatial computing. Visual-inertial odometry (VIO) has proven to be a cost-effective and accurate solution for this task. Robots, wearables, XR devices, and drones can benefit significantly from efficient implementations of VIO since they allow for cooler, lighter, and cheaper devices with longer battery life and a better user experience. In this work, we propose to enhance the efficiency of a VIO...

---

### 43. Moving Forward with Video Saliency: A New Dataset and Benchmark where Motion Matters

**Authors:** Susmit Agrawal, Rebecca Wanner, Juliane Verwiebe, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03276v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03276v1)

**Summary:** Video saliency prediction is inherently harder to model than static image saliency due to the additional temporal dimension. Video saliency benchmarks rest on the premise that predicting gaze on video requires utilizing temporal activity distributed across frames. Prior work has challenged this, showing that static baselines recover a significant fraction of the explainable gaze information on LEDOV, a popular video saliency dataset, and that video saliency models fail in the same places as this...

---

### 44. Consecutive Posterior Fusion for Diffusive Recovery of Unobservable Image Structures

**Authors:** Elena Morotti, Davide Evangelista, Elena Loli Piccolomini

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03261v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03261v1)

**Summary:** Solving severely ill-posed imaging inverse problems requires recovering image structures that are unobservable or weakly constrained by the measurements. Diffusion models provide expressive learned priors for inferring such missing information, while posterior sampling incorporates measurement consistency along the reverse process. Standard diffusion posterior samplers, however, rely on instantaneous measurement-aware estimates, without explicitly exploiting information carried by previous poste...

---

### 45. COSMI: COmpositional Synthesis of Multi-object Interactions

**Authors:** Daniel Eskandar, Ilya A. Petrov, Gerard Pons-Moll

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03252v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03252v1)

**Summary:** Generative models of human-object interaction are bounded by the data that exists: everyday activities involve several objects, but most captured datasets record one at a time, as multi-object capture is combinatorially expensive. Our observation is that interactions are local, so single-object captures already contain the parts of multi-object activities. We compose them: contact-consistent clips of single interactions, mirrored to balance the hands, transfer between bodies, and a language mode...

---

### 46. EmbPASS: Towards Cross-Embodiment Open Panoramic Segmentation

**Authors:** Pujun Guo, Yuanfan Zheng, Fei Teng, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03248v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03248v1)

**Summary:** Panoramic images provide a complete 360-degree field of view, enabling comprehensive scene understanding for embodied perception. However, heterogeneous embodied platforms exhibit substantial differences in observation viewpoints and spatial layouts, giving rise to cross-embodiment observation shifts that pose additional challenges to consistent and reliable panoramic perception, while systematic studies of this problem remain limited. To bridge this gap, we introduce a new task, termed Cross-Em...

---

### 47. Uncertainty as a Proxy for Semantic Correctness in Diffusion-Based Medical Image Synthesis

**Authors:** Yuxuan Ou, Konstantinos Kamnitsas, OxAAA Study, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03224v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03224v1)

**Summary:** Diffusion models can synthesise contrast-enhanced CT (CECT) from non-contrast CT (NCCT), avoiding contrast administration and its environmental and patient-access costs. However, visually realistic images are not necessarily anatomically correct, and the pixel-intensity and feature-space similarity metrics used to assess generation quality do not directly measure anatomical correctness. In this work, we investigate whether uncertainty can serve as a proxy for semantic correctness in diffusion-ba...

---

### 48. VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation

**Authors:** Yutong Wang, Xingtong Ge, Enhuai Liu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03221v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03221v1)

**Summary:** Video creation spans text-to-video (T2V), image-to-video (I2V), and condition-based generation, yet video diffusion models remain costly because they repeatedly evaluate large backbones during sampling. Distribution matching distillation (DMD) reduces this cost, but its reverse Kullback--Leibler (KL) objective can provide unstable or incomplete guidance when the student and teacher distributions have limited overlap. VDOT addressed this issue by adding optimal transport distillation (OTD), whose...

---

### 49. Evolving Hybrid Quantum-Classical Architectures for Image Classification

**Authors:** Devroop Kar, Daniel Krutz, Travis Desell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03220v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03220v1)

**Summary:** Hybrid quantum classical neural networks integrate parameterized quantum circuits (PQCs) with established deep learning architectures, but their performance depends strongly on the choice of quantum circuit architecture, a choice that remains largely manual. Most existing approaches rely on hand-designed or fixed circuit ansätze, requiring circuit structure, gate composition, and qubit connectivity to be specified in advance with no guarantee that they suit the task. This limitation is especiall...

---

### 50. VisionMX: Unlocking Microscaling Post-Training Quantization for Vision Models

**Authors:** Elad Dror Cohen, Ofir Gordon, Lior Dikstein, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03218v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03218v1)

**Summary:** Microscaling (MX) formats are emerging as a hardware-supported approach to efficient training and inference. They combine low-precision elements with shared block scales, but their impact on vision models remains underexplored. We systematically investigate post-training MX quantization across vision models and tasks. An analysis of direct conversion identifies three sources of error: block-scale representation, the poor alignment of some small convolutional weight tensors with nonuniform elemen...

---

## cs.LG

**50 papers**

### 1. What Should World Models Forget? Stratified Retention for Continual Adaptation

**Authors:** Nishit Anand, Ramani Duraiswami, Dinesh Manocha

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03713v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03713v1)

**Summary:** Continual learning treats degradation on previously seen data as evidence of failure, a convention inherited from settings with a stationary prediction target, where a correct label remains correct indefinitely. World models do not satisfy this condition. Their prediction target is the environment, which changes, so knowledge that was accurate when acquired may later become false, and discarding it is required behavior rather than a defect. Non-stationary ground truth is well studied in the conc...

---

### 2. RNADyn: A Benchmark for Generating and Understanding RNA Dynamics

**Authors:** Yiming Huang, Lennart Bastian, Hanqun Cao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03712v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03712v1)

**Summary:** Ribonucleic acid (RNA) functions through conformational changes that are not fully captured by static structures. However, large-scale standardized RNA dynamics data remain limited, and existing approaches typically treat trajectory generation and dynamics understanding as separate objectives. Here, we introduce RNADynBench, a standardized RNA molecular dynamics (MD) benchmark with 2585 quality-controlled 100-ns all-atom trajectories and leakage-controlled splits. Building on RNADynBench, we dev...

---

### 3. From Mixing to Tearing: Graph Decomposition in Decentralized Optimization via Message Passing

**Authors:** Kuangyu Ding, Gesualdo Scutari

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03709v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03709v1)

**Summary:** We study the minimization of sums of smooth strongly convex functions over undirected graphs, with each function held by one agent and communication restricted to neighbors in the graph. Existing decentralized methods, whether based on gossip or on routing over spanning trees, typically   use the network to mix or aggregate information to enable   {\it prescribed} local optimization   updates. What this communication-centered viewpoint lacks is a general   framework that uses graph structure to ...

---

### 4. LESSER: Post-Training Data Selection with Output-Layer Gradients

**Authors:** Lyuxin David Zhang, Eric Wong, Surbhi Goel, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03702v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03702v1)

**Summary:** The choice of post-training data for large language models substantially affects downstream performance. Gradient-based data selection is a popular approach that ranks training data by how well their gradients align with those of a small validation set. However, ranking with full-parameter gradients requires an expensive backward pass on every sample, making computation intractable for large candidate pools. This raises a natural question: can we approximate full-gradient features at a fraction ...

---

### 5. Simulation-Free Learning of Population Dynamics with Wasserstein Lagrangian Residuals

**Authors:** Fedor Sergeev, Markus Heinonen, Daniel Waxman, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03679v1)

**Summary:** The dynamics of cells, organisms, and fluids are often modeled as probability distributions evolving over time. Reconstructing and extrapolating this evolution from unpaired snapshots requires assumptions about the underlying process. Wasserstein gradient flows are a common choice, but they cannot describe conservative or periodic dynamics. Lagrangian mechanics in Wasserstein space covers both, but existing methods for learning it are simulation-based: they run a numerical solver at every traini...

---

### 6. Planning to Learn

**Authors:** Ian Osband

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03667v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03667v1)

**Summary:** Policy-gradient methods are central to modern reinforcement learning, including LLM post-training. When they struggle, the usual suspects are exploration, credit assignment and action-sampling noise. Classification has none of them. A classifier is a policy whose expected reward, its \emph{expected accuracy}, is the probability it assigns to the correct label, and because that label is known, the policy gradient is exact and smooth. Yet exact policy gradient loses to cross-entropy, even on expec...

---

### 7. Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models

**Authors:** Seo Hyun Kim, Sunwoo Hong, Younwoo Choi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03665v1)

**Summary:** Masked diffusion language models (dLMs) offer a promising parallel alternative to autoregressive models for complex reasoning. However, they face a distinct credit-assignment challenge, since a few commitments during denoising sharply reduce the uncertainty over the remaining masked positions and shape much of the response. Most post-training recipes for dLMs do not use this signal to decide which tokens to train on: they typically train on the final text or assign rewards to whole denoising ste...

---

### 8. Forecasting from Counterfactual Simulator Rollouts: A Sim2Real Evaluation

**Authors:** Angel Wang, Dominique Perrault-Joncas, Alvaro Maggiar, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03662v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03662v1)

**Summary:** Deploying a new decision policy creates a cold-start problem for prediction models whose targets depend on the policy's actions: historical observations reflect earlier policies, while real observations under the new policy are not yet available. Simulation offers a way to address this gap by rolling out the target policy across counterfactual scenarios and using the resulting trajectories to learn how the system responds to those controls. The simulation-to-reality (Sim2Real) transfer of this s...

---

### 9. PoCoFL: POlicy-COmpliant Federated Learning

**Authors:** Dominik Roy George, Varesh Mishra, Aysajan Abidin

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03650v1)

**Summary:** Federated Learning (FL) is a privacy-oriented learning paradigm that enables collaborative model training while keeping training data local to participating clients. However, it does not guarantee that clients submit policy-compliant contributions or that aggregators process admitted contributions correctly. Existing verifiable FL systems tailor validation rules to specific FL settings, learning workflows, and cryptographic constructions, limiting their applicability across network topologies, p...

---

### 10. On-Board Anomaly Detection for Efficient Marine Environmental Monitoring

**Authors:** Thomas Goudemant, Clotilde Szywala, Benjamin Francesconi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03649v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03649v1)

**Summary:** Marine ecosystems are impacted by various threats such as oil spills, algal blooms, and sediment floods, which disrupt habitats, wildlife, and human activities. Advances in satellite imagery and Artificial Intelligence (AI) have enhanced our capabilities for early detection and mitigation of such hazards. In this paper, we propose a marine event detection pipeline for Earth observation satellites equipped with multi- or hyperspectral sensors. Our approach includes a self-supervised neural networ...

---

### 11. Amortized Structured Stochastic Variational Inference for Gaussian Process Latent Variable Models

**Authors:** Maksym Tretiakov, Sarah Lucie Filipp, Vincent Fortuin, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03647v1)

**Summary:** Many machine learning methods aim to approximate the lower-dimensional manifold on which the data lives. A desirable feature of such methods is that they should capture the epistemic uncertainty of this learned manifold. One model that achieves this is the Gaussian Process Latent Variable Model, in which a Gaussian Process (GP) mapping from the latent space provides an estimate of the uncertainty of the manifold. However, the effectiveness of this uncertainty estimation is limited by the mean-fi...

---

### 12. When May a Bandit Leave Its Anchor? E-Process-Authorized Thompson Sampling under Non-stationarity

**Authors:** Mayand Gulati, Kerong Wang, WeiChen Au

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03646v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03646v1)

**Summary:** Stationarity rewards memory, but after a change the same history can mislead. We ask when forgetting should be permitted. E-process-authorized Thompson sampling (e-ATS) gives each arm full-history and discounted Beta states. An anytime-valid e-process first authorizes the discounted state, then a reversible relevance score controls its influence. Before authorization, e-ATS exactly follows optimistic Thompson sampling (OTS). Under a Beta-Bernoulli prior-predictive stationary model, e-ATS's proba...

---

### 13. On the Convergence of Success Conditioning for Policy Optimization

**Authors:** Matthew Brun, Xu Andy Sun

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03642v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03642v1)

**Summary:** Success conditioning is a strategy for improving decision-making policies in stochastic environments; it updates a policy by increasing the probability of taking actions that yield successful outcomes. Success conditioning is common to many reinforcement learning applications, yet its limiting behavior and convergence rates are not well understood. In this work, we demonstrate that success conditioning converges to an optimal policy on a broad class of Markov decision processes (MDPs). We also d...

---

### 14. IDRF: Inverse-Distilled Reward Fine-tuning of Masked Discrete Diffusion Models

**Authors:** Vladislav Gromadskii, David Li, Samson Gourevitch, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03641v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03641v1)

**Summary:** Masked discrete diffusion models offer a promising alternative to autoregressive generation, but iterative sampling can be costly, and intractable sequence likelihoods complicate reward fine-tuning. We introduce IDRF, a framework for reward fine-tuning of few-step masked discrete diffusion generators. Starting from a standard reverse-KL-regularized objective, IDRF replaces the intractable sequence-level KL penalty with inverse-distillation regularization. With an optimal auxiliary denoiser, we p...

---

### 15. Broken scale symmetries in undercomplete linear autoencoders

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03640v1)

**Summary:** Neural network loss landscapes have many symmetries, which are preserved by gradient flow but broken by finite-stepsize stochastic gradient descent (SGD). A canonical example of such a symmetry is scale in homogeneous networks: one can scale up the parameters in one layer and down in the next without changing the network output. Previous work has documented cases in which SGD breaks this symmetry in favor of balancing gradient noise or minimizing fluctuations. Here, we show that the solution geo...

---

### 16. FALCON: A Model and Dataset Agnostic Framework for Synthetic Data Generation for NL2SQL Pairs

**Authors:** Darian Lee, Shannon Rumsey, Jack St. Clair, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03625v1)

**Summary:** Relational databases are among the most widely deployed forms of structured knowledge, and natural language access to them requires grounding language onto schema entities and relations while handling the ambiguity inherent in how people phrase requests. Existing synthetic NL-to-SQL data generation methods largely ignore this ambiguity and produce oversimplified queries that fail to prepare models for the complexity of real-world structured knowledge access. We present FALCON, a framework that g...

---

### 17. Normal-Form Correlation in Markov Games

**Authors:** Ioannis Anagnostides, Constantinos Daskalakis, Gabriele Farina, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03621v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03621v1)

**Summary:** There has been a surge of recent work on correlated equilibrium concepts in Markov games. However, existing results focus on concepts weaker than normal-form correlated equilibria (NFCEs), leaving open the more challenging question of computing such equilibria, which goes back to the seminal work of Papadimitriou and Roughgarden (JACM'08). Here, we establish the first efficient algorithm for NFCEs in finite-horizon Markov games with a fixed number of players $n$. In particular, with $S$ states, ...

---

### 18. UniIntervene++: An Adaptive Intervention Agent for Efficient Real-World Reinforcement Learning

**Authors:** Yudong Lin, Haoyuan Deng, Zhuoxuan Yuan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03620v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03620v1)

**Summary:** Online reinforcement learning (RL) enables robot policies to improve through physical interaction, but the assistance they require changes as their competence evolves. Existing intervention strategies based on offline estimates or fixed decision rules can therefore become mismatched to the current policy. To address this, we propose UniIntervene++, an adaptive intervention agent that learns to allocate control between autonomous execution and heterogeneous assisted behaviors during online RL. Sp...

---

### 19. Mastering Atari 2600 Games with Discovered Options

**Authors:** Erik M. Lintunen, Marlos C. Machado

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03604v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03604v1)

**Summary:** Temporal abstractions, often instantiated as options, have long been regarded as a mechanism for accelerating credit assignment, facilitating exploration, and enabling generalisation in reinforcement learning (RL). However, developing general option discovery methods that are effective in large-scale, high-dimensional domains remains a fundamental challenge. Existing option discovery methods are either confined to relatively simple domains, depend on handcrafted or quasi-symbolic representations...

---

### 20. A Path Integral Surrogate for Multi-Step Gradient Inversion in Federated Learning

**Authors:** Agnivo Ghosh, Saumik Bhattacharya

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03597v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03597v1)

**Summary:** Federated learning lets many clients train a shared model together without ever sending their private data to a central server. Each client shares only a model update, and this update should reveal far less about the client than its raw training examples would. This premise is what protects the privacy of the clients. Gradient inversion attacks challenge it directly by trying to reconstruct a client's private input images from the single update it shared. Under FedAvg, a client's update accumula...

---

### 21. Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks

**Authors:** Neeraj Karamchandani, Piyush Nagasubramaniam, Xinhong Xie, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03585v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03585v1)

**Summary:** Security benchmarks for LLM-based agents often report the attack success rate (ASR) as a measure of model robustness and use these scores to compare different models and defense mechanisms, assuming that they describe the security of the agent. In this paper, we explore whether it also influences the benchmark's measurement.   To measure the effect of the benchmark representation, we introduce threat-preserving representation sensitivity (TPRS), which measures how much the ASR changes when we ch...

---

### 22. HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents

**Authors:** Alham Fikri Aji, Faiz Rizki Ramadhan, Zayd M. K. Zuhri, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03574v1)

**Summary:** We introduce HyperBrowseComp, a multilingual and multimodal browsing benchmark comprising 423 manually authored and human-validated questions across 13 languages, written by native or highly proficient speakers. Questions are designed to be extremely challenging. Each question targets a concise, publicly verifiable answer whose discovery requires locating obscure evidence, following multi-step clue chains, or inspecting heterogeneous sources such as videos, scanned documents, images, or maps. Ea...

---

### 23. Cephalonauts One: A deep fMRI dataset for decoding naturalistic speech in the human brain

**Authors:** Antoine Collas, Louis Jalouzot, Géraud Ilinca, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03558v1)

**Summary:** Cephalonauts One is a whole-brain 3 Tesla (3T) functional magnetic resonance imaging (fMRI) dataset recorded while subjects listened to audio podcasts. Three healthy subjects underwent multiple scanning sessions, each consisting of five 15-minute runs, while listening to podcasts in their native language. With 30 hours of fMRI data per subject, the current release is the deepest available fMRI dataset using naturalistic speech stimuli. The dataset pairs brain activity with the corresponding podc...

---

### 24. Get a GRIP, this will be a long TRIP: A Quantifiable Long-Range Framework for Verifying Over-squashing

**Authors:** Ferran Hernandez Caralt, Simon Heilig, Adrián Bazaga, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03556v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03556v1)

**Summary:** Empirical claims about the connection between over-squashing and long-range interactions in GNNs, can only be trusted if the benchmarks used to validate them genuinely require long-range interactions. The de-facto standard, the Long Range Graph Benchmark, has been repeatedly shown to be saturated by tuned short-range models, with existing synthetic alternatives being tied to specific topologies. As such, there is a lack of principled certificate of long-rangedness on arbitrary graphs. This state...

---

### 25. Objects Without Morphisms: What LLMs for Mathematics Do Not Represent

**Authors:** Yanli Wang, Suijin Wang, Xiaopeng Yuan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03551v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03551v1)

**Summary:** Large language models (LLMs) have reached expert-level performance on competition mathematics largely through the volume of search placed around them: candidate solutions are sampled in quantity and retained only when an external criterion accepts them. Such a procedure improves the outcome that survives it while leaving untouched what the model represents. We examine that question where no external criterion exists: translating statements between the dialects of neighbouring subfields, where fi...

---

### 26. ZeroMAG: Zero-Shot Multimodal Adapter Generation for Plug-and-Play EEG Foundation Models

**Authors:** Yubo Wang, Jingying Ma, Xinliang Zhou, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03546v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03546v1)

**Summary:** EEG foundation models (EFMs) capture reusable knowledge from large-scale EEG data, while many EEG recordings also include companion physiological signals that provide complementary information beyond the EEG-only interface. The challenge is to preserve this pretrained knowledge while extending the EFM to heterogeneous multimodal recordings through an adaptation inferred from unlabeled target data. We introduce ZeroMAG, a zero-shot multimodal adapter generation framework that extends a frozen EEG...

---

### 27. Autonomous Robotic Navigation for Endovascular Brain-Computer Interface Access

**Authors:** Harry Robertshaw, Weijie Qi, Nikola Fischer, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03537v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03537v1)

**Summary:** Endovascular brain-computer interfaces (BCIs) avoid craniotomy but require precise device delivery through anatomically variable cerebral veins. This work presents the first demonstration of in vitro autonomous robotic navigation for endovascular BCI access in the cerebral venous system. Soft Actor-Critic controllers were trained in silico for two sequential tasks spanning the right internal jugular vein to the superior sagittal sinus, using geometric augmentation of one training anatomy. Naviga...

---

### 28. Divergence controls entropy in distillation

**Authors:** Nicolas Zucchet, Scott W. Linderman

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03529v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03529v1)

**Summary:** Distillation has become a core primitive of large language model training, but its properties are not yet well understood. We take an entropic perspective, studying how the entropy of the student depends on the data and the divergence that define the distillation objective. We prove that forward KL inflates the entropy of the student above that of the teacher. Since cross-entropy training is a special case, this yields an identity that we verify quantitatively in pretraining and supervised finet...

---

### 29. Beyond Trained Models: Compiling GNNs for a Sound Explainer Benchmark

**Authors:** Steve Azzolin, Francesco Paolo Nerini, Stefano Teso, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03526v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03526v1)

**Summary:** Explainers for Graph Neural Networks (GNNs) are commonly evaluated by their plausibility, i.e., how well their explanations recover a predefined ground truth, such as a motif planted in the data. This protocol implicitly assumes that a GNN trained on such data relies on the intended motif. Although prior work has questioned this assumption, plausibility remains widespread. First, we show that the assumption is violated on several widely used benchmarks, where, e.g., degree statistics alone suffi...

---

### 30. From Benchmarks to Production: A Text-to-SQL System for Complex Financial Data

**Authors:** Arijit Sehanobish, Bruno Gomes Coelho, Guillaume Michel, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03524v1)

**Summary:** General-purpose Text-to-SQL systems achieve strong performance on academic benchmarks like Spider and BIRD, where schemas are relatively shallow and column values are often human readable. In production financial databases, where concepts are stored as opaque integer keys rather than human-readable strings, these methods fall below 50%, as even simple queries require multiple joins and filter predicates reference opaque IDs. We present Financial LINking Text-to-SQL (FLINT), a domain-specialized ...

---

### 31. XGenAct: Geometry-Enhanced World Action Models through Cross-Task Generation

**Authors:** Tingting Du, Ziyao Wang, Guoheng Sun, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03516v1)

**Summary:** World action models (WAMs) have advanced robot control by predicting how observations and actions evolve over time. Despite this progress, RGB and action based future prediction does not explicitly address the spatial understanding needed for robot manipulation. Existing efforts often add a limited set of spatial prediction tasks through specialized heads or branches, leaving both the range of spatial supervision and the model architecture fragmented. We introduce XGenAct, a world action model t...

---

### 32. An Automated and Reproducible Workflow for Crack Identification and Damage Assessment of Fusion Materials

**Authors:** Rinkle Juneja, Viktor Reshniak, Richard K. Archibald, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03505v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03505v1)

**Summary:** Post-exposure microscopy is central to qualification of fusion materials. However, manual analysis does not scale to the volume, heterogeneity, and multiresolution character of modern fusion-materials campaigns. To address this challenge, we present a reproducible workflow, implemented in the Galaxy scientific workflow environment, for automated crack identification and quantitative damage assessment from scanning electron microscopy images. The workflow processes SEM images and experimental met...

---

### 33. Getting Your Guidance Weights Right in diffusion and flow-matching posterior sampling

**Authors:** Liam Moroy, Jean-François Giovannelli, Yoann Altmann, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03503v1)

**Summary:** Training-free posterior sampling methods, also known as Plug-and-Play methods, leverage pretrained unconditional diffusion or flow-matching models to solve inverse problems. Most existing approaches rely on guidance weights to balance, at each time step, prior information from the unconditional score or velocity network with measurement consistency, yet the tuning of these weights is often not discussed and is largely left to heuristics. We introduce a simple and principled offline strategy for ...

---

### 34. Certified Mechanistic Edits: Behavioral Guarantees for Skill Removal and Preservation

**Authors:** Md Sazid Uddin, Md. Khairul Alam Mazumder, M. F. Mridha

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03502v1)

**Summary:** Mechanistic edits (ablations, weight edits, activation steering) are the standard tools for unlearning a harmful capability from a neural network while preserving useful ones. Current approaches validate their effects only by testing, which can never cover an entire continuous region of inputs. Prior work at the interpretability-verification boundary certifies descriptions of a model: what a circuit computes, or whether it faithfully explains the whole. We instead certify the behavioral effect o...

---

### 35. Below what training size do deep tabular generators stop beating trivial baselines? A preregistered benchmark on a size ladder of clinical and standard datasets

**Authors:** Shivam Shrivastava

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03500v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03500v1)

**Summary:** Deep tabular generative models are benchmarked on datasets with tens of thousands of rows; clinical datasets have hundreds. We preregistered and ran a size-ladder benchmark to find where the two regimes diverge: 8 public datasets subsampled from 200 to 20,000 training rows, seven generators (independent marginals, Gaussian copula, SMOTE, unconditional SMOTE, CTGAN, TVAE, TabDDPM) with a fixed 20-trial tuning budget and 5 evaluation seeds, plus 4 natively small clinical datasets at true size, for...

---

### 36. Most-Recent Anchoring with Recurrent Ordering for Time Series Forecasting

**Authors:** Jung Min Choi, Ngoc Son Le, Ibram Abdelmalak, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03494v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03494v1)

**Summary:** Long-term forecasting models commonly process all patches in a look-back window using the same fixed stack. Older contextual patches and recent evidence therefore receive the same computational depth. Yet the information closest to the forecast and the more distant context do not contribute equally. Uniform processing leaves this distinction unexpressed in the architecture. We propose MARO, a Most-Recent Anchoring with Recurrent Ordering model that processes the look-back window from the most re...

---

### 37. Dual-Context Analog Retrieval for Time Series Forecasting

**Authors:** Jung Min Choi, Ngoc Son Le, Ibram Abdelmalak, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03491v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03491v1)

**Summary:** Most long-term time-series forecasting models map the look-back window directly to the full horizon in a single pass. While efficient, this design does not explicitly identify which historical states are most relevant to different future segments or exploit what followed those states. Analog forecasting addresses this by retrieving past states similar to the present and using their observed continuations, but single nearest matches can be unreliable and overlapping patches may produce redundant ...

---

### 38. AREX: Affine-Residual Exponential Integrator for Few-Step Sampling in Flow Matching

**Authors:** Shizheng Lin, Soon Hoe Lim, N. Benjamin Erichson

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03483v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03483v1)

**Summary:** We introduce AREX, a training-free sampler for pretrained flow matching models that uses the target mean and covariance to capture an analytically tractable part of the sampling dynamics. We show that the velocity field of the moment-matched Gaussian target is the $L^2$-optimal affine approximation to the marginal velocity field. This motivates decomposition of the learned dynamics into an affine component over the whole sampling path, determined by the first two target moments, and a neural res...

---

### 39. Metropolis-Hastings Dominates Importance Resampling for Policy Composition

**Authors:** Alexey Kurennoy, Ramil Yarullin, Fergal Reid

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03480v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03480v1)

**Summary:** Post-training a large language model (LLM) often requires exploring trade-offs between multiple rewards, but retraining for each trade-off is expensive. Decoding-time policy composition allows these trade-offs to be adjusted by combining reward-specific policies at inference time. This composition targets a weighted product of the policies' probabilities over complete responses, but standard implementations combine their next-token probabilities, generally introducing sampling bias. We analyze a...

---

### 40. Single or Multiple Policies for Phase-Structured Reinforcement Learning?

**Authors:** Guilhem Loussouarn, Nancy Nayak, Kin K. Leung

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03475v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03475v1)

**Summary:** Many reinforcement-learning (RL) problems are non-stationary yet structured and can be decomposed into phases, each with its own transition probabilities and reward functions. When the phase sequence is known, the common solution augments the state with information to satisfy the Markovian property and applies standard RL techniques. However, prior work finds that the multi-policy approach for different phases can outperform a single state-augmented policy shared among the phases, for reasons th...

---

### 41. When Is Accuracy Evidence? A Unified Theory of Generalisation, Validation, and Information Fusion

**Authors:** JM Gorriz

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03465v1)

**Summary:** K-fold cross-validation (CV) is widely used as evidence of out-of-sample performance, although folds are neither independent experiments nor equally informative under heterogeneous data. Cross Upper-Bound Validation (CUBV) replaces point-wise CV accuracy by conservative upper bounds on true risk. Here we generalise CUBV through a single exponential framework in which the moment-generating function of the generalisation gap is controlled by a cumulant envelope gamma(lambda). This yields a family ...

---

### 42. Generalization of Transformer-Based Neural Quantum States via In-Context Learning

**Authors:** Zhen Qin, Qing Qu, Alfred O. Hero

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03463v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03463v1)

**Summary:** Neural quantum states based on modern deep learning architectures have emerged as powerful representations for quantum many-body systems. In particular, Transformer-based neural quantum states provide expressive models capable of capturing long-range correlations, and their empirical generalization performance has recently been demonstrated. However, a theoretical understanding of their generalization behavior remains largely unexplored. In this paper, we develop a theoretical framework to analy...

---

### 43. Beyond Random Splits: Evaluating Drug-Target Affinity Models Under Chemically and Biologically Motivated Distribution Shifts Copy

**Authors:** Minjae Chung, Clara Li, Malar Paavai Muthukumaran, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03456v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03456v1)

**Summary:** Drug-target affinity (DTA) prediction is widely used to prioritize candidate compounds before costly experimental screening. DTA models are often compared under a single data split, even though deployment may require extrapolation to new chemical series, new protein targets, or both. We ask whether the distribution shift used for evaluation changes which architecture appears best. We curate 718,800 unique drug-protein pairs from the ChEMBL and BindingDB datasets. We compare a Morgan-fingerprint ...

---

### 44. Measure Less, Know More: Self-Supervised Test-Time Feature Acquisition

**Authors:** Eeshaan Jain, Linus Bleistein, Bart Deplancke, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03454v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03454v1)

**Summary:** Recent progress in multimodal, high-dimensional learning has enabled foundation models to process heterogeneous, large-scale data. However, at test time, acquiring all features or modalities can be prohibitively costly and often redundant. Sequentially selecting informative modalities is therefore critical, yet challenging when the downstream task or prediction target is unknown. To this end, we introduce ECHO-$k$, a task-agnostic and self-supervised learning principle for modality acquisition: ...

---

### 45. Causal Representation Learning with Instantaneous and Lagged Relations via Nonstationarity

**Authors:** Tatsuya Yamada, Hiroshi Morioka, Yoshinobu Kawahara

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03452v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03452v1)

**Summary:** Causal representation learning for time-series data aims to identify latent states and their causal relations from observations. In this setting, an important challenge is to model both lagged causal relations across observation intervals and faster causal effects that appear as instantaneous relations within an interval, while accounting for nonstationarity in time-series data. However, methods that jointly handle these causal relations and nonstationarity remain limited. To address this gap, w...

---

### 46. Electronic Density versus Geometry for Machine-Learned Molecular Absorption Spectra

**Authors:** Siddharth Dhanpal, Peter Elliott, Paolo Emilio Trevisanutto, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03444v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03444v1)

**Summary:** Molecular optical absorption spectroscopy provides a direct probe of electronic structure and is widely used for molecular identification, interpretation of photophysical behaviour, and planning of spectroscopy experiments. Calculating the absorption spectra using first-principle excited-state methods, however, is computationally demanding, at least compared to ground-state calculations, which limits their routine application across large molecular sets. Machine-learning (ML) surrogates can redu...

---

### 47. OptiSelect: How does the Optimizer Shape Data Curriculum?

**Authors:** Simin Fan, Alireza Abdollahpoorrostam, Martin Jaggi

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03432v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03432v1)

**Summary:** Online data selection has demonstrated substantial efficiency gains for LLM pretraining by training on the most valuable candidates within each batch. Since a candidate's value is realized through its effective model update, principled selection should account for the optimizer step, which reshapes the raw gradient before it updates model parameters. We formalize this optimizer-aware selection paradigm as OptiSelect and present the first systematic study of how the optimizer shapes data selectio...

---

### 48. Deep Bayesian REFoCUS

**Authors:** Simon Penninga, Ruud van Sloun

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03419v1)

**Summary:** In this work we formulate ultrasound multistatic recovery from arbitrary transmit sequences as a Bayesian inference problem. To that end, we train a deep generative prior on multistatic data sets to tackle the rank-deficient regime in which classical linear REFoCUS decoders fail. This appproach, which we term Deep Bayesian REFoCUS, outperforms the linear baselines for all regimes of rank-deficiency and noise levels, and regresses to linear decoding when inversion is exact. The model also express...

---

### 49. Rethinking Epistemic Uncertainty in Node Classification through Information Growth

**Authors:** Emma Meneghini, Francesco Ferrini, Bruno Lepri, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03418v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03418v1)

**Summary:** Epistemic uncertainty should decrease as additional information about the data-generating process (DGP) becomes available to the predictor. Yet, existing graph evidential deep learning (EDL) methods for node classification typically construct epistemic uncertainty from graph-specific properties and evaluate it on downstream tasks such as out-of-distribution detection, which do not test its reducibility as information about the DGP increases. To make reducibility directly testable, we introduce a...

---

### 50. Iterating Consistency Models: Stability, Error Bounds and Noise Schedules

**Authors:** Alessio Spagnoletti, Abdul-Lateef Haji-Ali, Andrés Almansa, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03414v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03414v1)

**Summary:** Consistency models (CMs) have become a leading approach for generating high-quality samples in few steps. However, adding steps can improve or degrade sample quality in ways that are highly sensitive to the schedule and that existing theory does not fully explain. To provide accuracy guarantees and guide CM sampler design, we analyze multistep CM sampling as a composition of noising and approximate denoising operators. Under explicit, verifiable stability assumptions, we derive a non-asymptotic ...

---

## cs.NE

**50 papers**

### 1. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

**Authors:** Hui Chen, Xuan Qi, James Xu Zhao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03675v1)

**Summary:** LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them...

---

### 2. Parallel Time-Aligned Spiking Self-Attention for Consistent Integer-Valued Training and Spike-Driven Inference

**Authors:** Peng Xue, Wei Fang, Kaiwei Che, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03291v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03291v1)

**Summary:** Integer-valued leaky integrate-and-fire (I-LIF) neurons and spike firing approximation (SFA) reduce temporal training cost by representing spike trains as firing counts and normalized firing rates, respectively. However, applying spiking self-attention (SSA) directly to these compressed query, key, and value representations introduces cross-time interactions that are absent during spike-driven inference. We term this operator-level discrepancy Temporal Interaction Mismatch (TIM). We propose Para...

---

### 3. The Investment Acceleration Principle Revisited by means of a Neural Network

**Authors:** Guido Fioretti

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03282v1)

**Summary:** The investment acceleration principle is a heuristic for modelling investment time series out of consumption time series. The model presented herein develops a disaggregated accelerator equation whose coefficients are the weights of a Kohonen neural net that represents firms' decision-making. According to this model, investments take place when managers recognise emerging technological patterns. Furthermore, a technique borrowed from the theory of self-organising systems is used in order to dise...

---

### 4. Self-Repairing Recurrent Ensembles for Real-Time Recovery from Distribution Shift

**Authors:** Julian Lemmel, Pedro D. Wendel Garcia, Taisuke Kobayashi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03249v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03249v1)

**Summary:** Deploying a pretrained controller exposes it to conditions that are absent from its training data. Sensor drift, outright sensor failure and accumulating measurement noise all induce a distribution shift that can collapse an otherwise competent policy; typically at a point in time where no expert is available to supply corrective labels. We present a method that lets a policy recover from such shifts online and without supervision. Our controller is an ensemble of recurrent networks, each of whi...

---

### 5. Evolving Hybrid Quantum-Classical Architectures for Image Classification

**Authors:** Devroop Kar, Daniel Krutz, Travis Desell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03220v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03220v1)

**Summary:** Hybrid quantum classical neural networks integrate parameterized quantum circuits (PQCs) with established deep learning architectures, but their performance depends strongly on the choice of quantum circuit architecture, a choice that remains largely manual. Most existing approaches rely on hand-designed or fixed circuit ansätze, requiring circuit structure, gate composition, and qubit connectivity to be specified in advance with no guarantee that they suit the task. This limitation is especiall...

---

### 6. Aggregate accuracy conceals concentrated temporal vulnerability in a spiking speech classifier

**Authors:** İsmail Can Dikmen

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03155v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03155v1)

**Summary:** Aggregate accuracy cannot reveal which utterances are locally vulnerable or how internal activity changes when labels remain stable. We retain every prediction for 725,070 adjacent-bin, one-count changes around 100 validation utterances of a frozen SpikeSCR-based classifier. The canonical native-horizon GPU singleton path reaches 86.0836% validation accuracy. Equal-source expected accuracy under a uniformly chosen neighbor rises from 84.00% to 84.54%, although 13 of 84 initially correct sources ...

---

### 7. Learning While Inferring: Local and Parallel Learning for Edge SNNs across Sensing Modalities

**Authors:** Yanxun Zhang, Yifei Wang, Changze Lv, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03149v1)

**Summary:** Edge intelligence requires models to sense continuously in real time and to keep adapting on-device, all under tight compute, energy, and memory budgets. Although spiking neural networks (SNNs) enable efficient event-driven inference, standard surrogate-gradient backpropagation (BP) serializes updates and blocks ongoing inference. We investigate Bidirectional Spike-Based Distillation (BSD) as an on-device learning principle that lets edge SNNs learn while inferring. BSD couples a stimulus-driven...

---

### 8. Small universal multiset reaction systems

**Authors:** Andrei Paun, Annemarie-Beatrix Messner

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03021v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03021v1)

**Summary:** This paper presents a construction of a small universal machine within the framework of Multi-set Reaction Systems. We encode the machine state using elements that represent registers and instruction labels, and we enforce sequential execution by ensuring that reaction chains for a given instruction can only activate after the corresponding label element appears. We implement a universal register machine with 8 registers and 23 instructions, showing that the priority-based model requires 87 dist...

---

### 9. Temporal Geometry of Deep Networks: Hyperbolic Representations of Training Dynamics for Intrinsic Explainability

**Authors:** Ambarish Moharil

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03000v1)

**Summary:** Intrinsic explainability remains a challenging problem, particularly in contexts where multilayer perceptrons (MLPs) require dynamic re-training within an optimization environment. This paper investigates how MLPs and their training dynamics can be represented and studied in non-Euclidean spaces; our representation features the Poincaré model of hyperbolic geometry. We aim to capture the geometric evolution of their weighted topology and self-organization over time. Instead of restricting the an...

---

### 10. Evolutionary Computation for Trustworthy AI: From Attacks and Defenses to Self-Evolving Era

**Authors:** Junhao Dong, Chenkai Wang, Xuanhui Lin, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02996v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02996v1)

**Summary:** As Artificial Intelligence (AI) has evolved from task-specific models to foundation models and agents, the scope of trustworthy AI has expanded from model-level robustness to the reliability and safety of broader AI systems. This evolution has also expanded the attack surface from individual models to broader system-level interactions, including tool use, context, and interaction trajectories with dynamic environments. As a result, maintaining reliable and safe behavior under changing or deliber...

---

### 11. SEDIMA: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents

**Authors:** Amirhossein Abaskohi, Mahdi Mostajabdaveh, Zirui Zhou

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02361v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02361v1)

**Summary:** Large language model (LLM)-driven evolutionary search is a powerful paradigm for automated program and algorithm discovery, yet existing systems are largely memoryless: each run explores from scratch, so agents repeatedly rediscover the same improvements and re-encounter the same dead ends. We introduce SEDIMA, a persistent hierarchical insight memory for evolutionary search agents. SEDIMA distills raw traces into natural-language insights, clusters them by semantic similarity using attention-we...

---

### 12. Spiking neural networks for streaming qubit readout

**Authors:** Barry M. Dillon, Aqib Javed, Jim Harkin, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02129v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02129v1)

**Summary:** Fast and accurate qubit-state assignment is essential for feedback, calibration, and error correction in quantum processors. In superconducting platforms, frequency-multiplexed readout makes this task intrinsically multivariate as measured traces can encode crosstalk, qubit-state relaxation events, and other transient nonidealities that are not fully captured by conventional matched filtering. Here, we introduce spiking neural network (SNN) discriminators for superconducting qubit readout. By pr...

---

### 13. TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design

**Authors:** Jose A. Ayala-Romero, Andres Garcia-Saavedra, Xavier Costa-Perez

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01887v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01887v1)

**Summary:** Dynamic resource assignment, the real-time allocation of task streams to heterogeneous processing nodes, is the backbone of modern computing infrastructure. While learning-based schedulers excel in research, industrial deployments still rely on hand-written rules that operators can read, audit, and execute within tight latency budgets. LLM-based Automatic Heuristic Design (AHD) promises to automate writing such rules. However, existing AHD frameworks were developed for combinatorial problems ful...

---

### 14. Continual Reinforcement Learning with Neuroevolution

**Authors:** Eleni Nisioti, Andrea Cossu, Kathrin Korte, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01583v2) | 📄 [PDF](https://arxiv.org/pdf/2610.01583v2)

**Summary:** Despite many studies about causes and remedies of plasticity loss in Reinforcement Learning (RL) under continual task changes, no RL method has yet consistently achieved a good balance between adaptation and forgetting. Here we turn to an alternative optimization paradigm, neuroevolution (NE): algorithms that search directly in weight space through mutation and selection over a population of neural networks. Across a wide array of environments and environmental changes, with policies ranging fro...

---

### 15. Controllable Stochastic Quantization Encoding for Adversarially Robust Spiking Neural Networks

**Authors:** Yujia Liu, Peiyu Liu, Yajing Zheng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01558v1)

**Summary:** Spiking Neural Networks (SNNs) have attracted increasing attention due to their impressive temporal dynamics, energy efficiency, and brain-inspired mechanisms. Although SNNs have demonstrated promising performance in image classification tasks, recent studies have shown that they remain vulnerable to adversarial attacks, where imperceptible perturbations are added to input images to mislead model predictions. Existing defense methods mainly focus on training strategies, while the role of input e...

---

### 16. LESS: Lightweight Evolutionary Supernet Search in Minutes

**Authors:** Aviral Gandhi, Jinglue Xu, Jialong Li, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01468v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01468v1)

**Summary:** Low-cost NAS must both explore high-performing architectures and identify them reliably, yet reducing evaluation cost often weakens the fidelity of candidate comparisons. Training-free methods reduce evaluation cost by replacing learned task feedback with proxy signals measured at initialization. We introduce LESS (Lightweight Evolutionary Supernet Search), a data-driven method that combines a brief fair hard-path warm-up with discrete search under a single CMA-ES distribution. Each proposal is ...

---

### 17. Inherited Learning in an Artificial Ecology: How Controls and Update Allocation Shape Benefits

**Authors:** Xuening Wu, Lei Li, Shan Yu

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01232v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01232v1)

**Summary:** Learning can improve an individual's behavior, yet a population risks losing that experience whenever individuals die and are replaced. Inheriting learned preferences offers a way to preserve useful behavior across generations, raising a question for artificial populations: when does inheritance improve collective performance, and how can its benefits be measured fairly? The challenge is that inheritance changes not only offspring behavior but also survival, reproduction, and opportunities for f...

---

### 18. Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning

**Authors:** Syon Mansur, Joel Zylberberg

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00753v1)

**Summary:** End-to-end backpropagation has been the dominant mode of training in deep learning, allowing for the coordination of parameter updates across layers of a neural network. Prior studies have explored alternative -- and, in some cases, simpler -- training mechanisms, showing that they can sometimes achieve performance similar to backpropagation. However, the architectural conditions under which locally optimized networks, which avoid end-to-end backpropagation of error, can learn representations co...

---

### 19. Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation

**Authors:** Jafar Shamsi, Navid Akbari, Sonia Sennik, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00719v1)

**Summary:** Pseudo-random number generation often requires trade-offs among quality, power consumption, and bandwidth to produce unpredictable sequences of numbers. The brain, on the other hand, efficiently generates unpredictable output complex network dynamics occurring in a high-dimensional state. This state, which is hypothesized to be chaotic, relies on the balance between excitation and inhibition. Here, we investigated if computational models of these chaotic balanced states can be harnessed for Neur...

---

### 20. Large Language Model-Guided Evolutionary Discovery of Native Neural Architectures for Spiking Sequence Modeling

**Authors:** Ruoyu Zhao, Jiaqi Wu, Chenyu Zhu, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40258v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40258v1)

**Summary:** Spiking neural networks (SNNs) offer low-energy sequence modeling through sparse, event-driven computation. However, interactions among spike encoding, neuronal dynamics, and information propagation complicate architecture design. Existing SNN sequence models often adapt artificial neural network (ANN) architectures designed for real-valued activations, potentially underusing spike-based communication and temporal state updates, motivating automated discovery of native SNN architectures. Most ev...

---

### 21. From DNA Design to DNA Slimming: Auditable Agentic Discovery of a Deletion-Only Designer

**Authors:** Joel Shor

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40143v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40143v1)

**Summary:** Compact regulatory DNA can free up space in vector payloads, reduce synthesis and assay burden, and expose which sequence features drive predicted activity. Yet most model-based nucleic-acid designers optimize fixed-length sequences through substitutions; they do not ask which bases of an existing functional element can be removed while retaining predicted activity. We define the task of sequence slimming as selecting an exact-length, order-preserving subsequence while retaining activity. Modele...

---

### 22. Toward Controlling Biology with Language:Offline Learning of Prompt-Conditioned Interventions for Cells, Organoids, and Biobots

**Authors:** Nam H. Le, Douglas Blackiston, Michael Levin, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.02247v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02247v1)

**Summary:** Artificial intelligence increasingly serves as a natural-language interface to complex technical systems, letting people accomplish sophisticated tasks by describing what they want rather than specifying how to do it. Extending this interface to living systems is harder: unlike code or images, a biological intervention has no closed-form linguistic meaning, and the paired language-intervention-outcome data needed to learn such a mapping is expensive to collect, since each example requires its ow...

---

### 23. An Island-Based Parallel Biased Random-Key Genetic Algorithm for the Three-Dimensional Trailer Loading Problem

**Authors:** A. del Río, L. Díaz, L. C. de Vicente, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39272v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39272v1)

**Summary:** The Three-Dimensional Trailer Loading Problem (3D-TLP) involves determining the optimal placement and orientation of heterogeneous items within the confined space of a trailer while maximizing volume utilization and satisfying a wide range of complex logistical and safety constraints. The 3D-TLP is NP-hard, rendering exact optimization approaches computationally impractical for large-scale industrial applications. To address this challenge, we propose an enhanced Biased Random-Key Genetic Algori...

---

### 24. Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison

**Authors:** Gyujeong Park

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39248v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39248v1)

**Summary:** Randomised copies of a connectome are the usual baseline for asking whether measured wiring matters, and the answer depends on what the randomisation preserves. We evolved embodied foraging agents whose brains are a compressed adult Drosophila connectome (FlyWire v783; 512 cell-type groups and 1,000 Kenyon cells) alongside agents built on randomised wiring, in pre-registered experiments with ten seeds, four ecologies and 600 generations. Two standard randomisations, a column shuffle and degree-p...

---

### 25. Evolutionary foraging in grids: Intermittent search dynamics emerge in finite, depletable landscapes

**Authors:** Shailendra Bhandari, Alex Szorkovszky, Anis Yazidi, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39239v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39239v1)

**Summary:** How search strategies evolve in finite, depletable landscapes remains a question in foraging theory. We study this problem with an evolutionary simulation in which agents forage on a two-dimensional toroidal lattice containing non-renewable resources distributed uniformly or as Lévy dust. Each agent carries a heritable genome encoding step lengths, velocities, and turning angles, and selection acts on a fitness function combining energetic gain, movement cost, and coverage efficiency. By allowin...

---

### 26. T-Router: Learning Thalamic Routing for Reasoning with Parameter-Efficient Reinforcement Learning

**Authors:** Liuxian Ma, Jiale Dai, Jiaqi Li, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39109v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39109v1)

**Summary:** Parameter-efficient reinforcement learning aims to improve reasoning with a compact trainable interface to a pretrained model. We introduce the Thalamic Router (T-Router), which concentrates adaptation on the reuse of completed computations. A compressed, addressable bank preserves block changes; a depth-recurrent controller conditions their selection and relative-scale writeback. This coupling gives thalamic context-dependent routing a concrete computational form: learn which earlier contributi...

---

### 27. Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization

**Authors:** Chen Lu, Ke Xue, Siyuan Xu, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38757v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38757v1)

**Summary:** Large language models are increasingly participating in complex real-world tasks in the form of algorithm-design agents, designing and refining algorithms. Many successful algorithm-design agents adopt pure in-context evolutionary frameworks, but they may quickly plateau in domains that require specialized knowledge. Parametric adaptation offers a way to internalize specialized knowledge, but conventional training requires abundant domain-specific corpora while high-quality algorithms are scarce...

---

### 28. How much of fly walking is written in the wiring?

**Authors:** Isabel Guan, Yuntian Zhao, Dingyuan Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38665v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38665v1)

**Summary:** Connectome models of the fly nerve cord generate walking-like motor rhythms, but oscillation alone does not show that the specific wiring matters. Here we provide, to our knowledge, the first test of which features of motor output depend on the specific wiring. We simulated the leg motor systems of two independent Drosophila connectomes, with synapse counts as fixed weights and glutamatergic synapses treated as inhibitory, and compared each with six families of rewired networks that preserve pro...

---

### 29. Behavioral Persistence and Incomplete Functional Transfer of Co-evolved Communication in Evolutionary Robotics

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38527v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38527v1)

**Summary:** This work evaluates the direct transfer of a co-evolved communication protocol from a 2D simulation to a 3D physical environment, without retraining the network weights. Two e-puck-type robots, controlled by a GRU network with residual connection, were evaluated in a food-seeking task with social signaling. The sensory and motor translation layer required three corrections for stable physical operation, including the calibration of a hunger term based on a measurable asymmetry in the trained res...

---

### 30. Derandomizing Dense Binary Hypervector Codebooks for Quantized Scalars

**Authors:** Dmitri Rachkovskij, Evgeny Osipov, Olexander Volkov, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38471v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38471v1)

**Summary:** Hyperdimensional computing and vector symbolic architectures often represent quantized scalar levels by dense binary codebooks whose level-to-level similarity is intended to follow a prescribed function of scalar separation. At finite dimensionality, randomized scalar codebook constructions deviate from this target because of sampling noise, random-start imbalance, update-count fluctuations, component dependence, and finite-capacity effects. We develop a transition-based derandomization framewor...

---

### 31. Simulating Synchrony Loop Networks in the Open Source RISP Neuroprocessor

**Authors:** Jackson Mowry, Patrick Abbs

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38432v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38432v1)

**Summary:** Neuromorphic spiking neural networks (SNNs) offer a promising alternative to conventional deep neural networks for tasks with computational resource or data constraints. However, their practical applications have been limited by comparatively weak performance on complex learning tasks. Experimental approaches such as Synchrony Loop Propagation (SLP) increasingly seek to address this problem through more sophisticated and heterogeneous neuron models, and have achieved encouraging initial results....

---

### 32. Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy

**Authors:** Huan Rong, Chao Yin, Anouar Imel, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38016v1)

**Summary:** Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is...

---

### 33. Kolmogorov-Arnold Classifier Systems as Universal Approximators

**Authors:** Hiroki Shiraishi, Hisao Ishibuchi, Masaya Nakata

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37958v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37958v1)

**Summary:** As the input dimension $n$ grows, rule-based machine learning, such as Learning Classifier Systems (LCSs), faces a fundamental scalability bottleneck for function approximation: both rule count and parameter count grow exponentially with $n$. Traditional LCSs partition the $n$-dimensional input space directly, requiring $\mathcal{O}(m^n)$ rules for adequate coverage, where $m$ is the per-variable resolution. This article breaks from this paradigm by reorganizing rules dimension-wise, guided by t...

---

### 34. A neural network that maintains and retrieves memories based on context

**Authors:** Hayoung Song, JeongJun Park, Qihong Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37791v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37791v1)

**Summary:** Every day, people continuously infer situational context and adjust the way they understand and remember the world. Context, signaled by the prefrontal cortex, is known to modulate working memory and episodic memory, but the algorithmic understanding of this modulation remains limited. Here, we train a recurrent neural network (RNN), augmented with an episodic memory buffer, to infer context using Bayesian inference as it continuously makes predictions of upcoming scenes while watching naturalis...

---

### 35. Hybrid Joint-Selective Optimization: Reduced-Space Levenberg-Marquardt Refinement of Low-Dimensional Parameters of Interest

**Authors:** Muhammad Luthfi Shahab, Gabriella Alfa Indahsari, Imam Mukhlash, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37308v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37308v1)

**Summary:** This paper introduces a hybrid joint-selective optimization (HJSO) framework for large-scale numerical problems in which a small subset of trainable quantities is of primary interest. We partition the full parameter vector into a high-dimensional remaining block and a low-dimensional block of parameters of interest (POIs), perform joint first-order optimization over the full parameter set, and then freeze the remaining variables while applying a reduced-space Levenberg-Marquardt (LM) refinement ...

---

### 36. Adaptive Rotation for iSOMA: Geometry, Benchmarking, and Noise Robustness in Variational Quantum Objectives

**Authors:** Vojtěch Novák, Ivan Zelinka

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37193v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37193v1)

**Summary:** We study whether the coordinate dependence of the improved Self-Organizing Migrating Algorithm (iSOMA) can be reduced while retaining its inexpensive leader-directed migration mechanism. We introduce iSOMA-AR, which learns a basis from successful migration displacements and selectively applies the standard perturbation mask in that basis. On the complete noiseless BBOB suite, iSOMA- AR significantly outperformed baseline iSOMA across matched conditions, with the largest gains on geometrically di...

---

### 37. Evolving Towards Better Codes: LLM-Guided Search for High-Distance Binary Linear Codes

**Authors:** Amal Seddas, Vladyslav Shashkov, Maryna Viazovska, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37056v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37056v1)

**Summary:** Evolutionary program search driven by large language models (LLMs) has produced record-breaking constructions for open problems in combinatorics and beyond. We apply this approach to the longstanding problem of improving the best-known bounds for binary linear codes. Building on the EvoTune evolutionary framework and the ShinkaEvolve codebase, we introduce LinCodeEvolve, which evolves code-construction programs against an exact minimum-distance evaluator. A strategy loop combines diversity-drive...

---

### 38. Multi-Depth Temporal Fusion for Feedforward, Locally Trained Spiking Neural Networks

**Authors:** Aidin Attar, Eleonora Cicciarella, Michele Rossi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37047v2) | 📄 [PDF](https://arxiv.org/pdf/2609.37047v2)

**Summary:** We propose a new spiking neural network (SNN) design to process static images and event streams using time-to-first-spike (TTFS) latencies. Our key research question is which architectural choices best accommodate local and online learning in multi-layer convolutional SNNs. This question is addressed via an original framework combining residual-like connections with multi-depth feature aggregation and consensus. The full SNN pipeline features an early-vision front end, to convert raw visual data...

---

### 39. Where Does Randomness Matter in Neural Cellular Automata?

**Authors:** Fei Zuo, Jiaqi Shi, Yujing Liu

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36797v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36797v1)

**Summary:** Stochastic cell updates are often used throughout the life of a neural cellular automaton (NCA), from backpropagation through time to final rollout. This leaves two questions entangled: does update randomness help learn a useful rule, and must that randomness remain at execution? We separate training and evaluation update modes in controlled Growing NCA experiments, then vary the states shown during training. Under the standard constant-rate persist recipe, asynchronous training passes the short...

---

### 40. NeuroDyn-EEG: An Interpretable Pre-trained Model for EEG Based on Neural Dynamics

**Authors:** Yi Cui, Tong Zhao, Jiaxin Lei, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36773v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36773v1)

**Summary:** Clinical scalp electroencephalography (EEG) offers a noninvasive window into neural dynamics of neuropsychiatric disorders. However, discriminative deep models often lack anatomically indexed physiological interpretability. We propose NeuroDyn-EEG, a pretraining framework integrating generative priors from neural dynamics. It couples an extended Jansen-Rit neural mass model, leadfield-based source projection, and simulation-based parameter inversion. Trained on synthetic parameter-EEG pairs with...

---

### 41. Massively Parallel Reinforcement Learning with a Chaotic Reconfigurable Clockless Chip

**Authors:** Eric Oliveira-Gomes, Damien Rontani

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36347v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36347v1)

**Summary:** Hardware accelerators based on physical dynamical systems offer an attractive route toward energy-efficient reinforcement learning applications. However, their scalability is challenging because it requires many statistically independent entropy sources. Here, we introduce a quasi-analog decision-making architecture based on asynchronous Boolean networks (or lattices) implemented on a clockless reconfigurable chip. Each node in the network consists of a single logic element that acts as an auton...

---

### 42. HeurEvo: Agentic Evolution of Hybrid Solver-Augmented Heuristics for Time-Critical Mathematical Optimization

**Authors:** Feijie Wu, Hugo Barbalho, Konstantina Mellou, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36303v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36303v1)

**Summary:** Recent advances in agentic heuristic design use AI agents and execution feedback to automate algorithm discovery for challenging optimization problems. In many practical settings, high-quality solutions must be obtained under strict runtime constraints, motivating hybrid approaches that combine problem-specific heuristics with powerful mathematical programming solvers. However, existing approaches typically improve heuristic components within predefined procedures or tune solver configurations i...

---

### 43. CMDO: A Cognitive Memory-Driven Optimization Algorithm for Adaptive Population-Based Search

**Authors:** Mohammed Yusuf Mujawar, Shahram Rahimi, Noorbakhsh Amiri Golilarz

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35657v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35657v1)

**Summary:** Population-based optimization methods often use previous search information through successful solutions, parameter adaptation, or operator performance, but they rarely retain the context in which a search behavior succeeded or failed. We introduce Cognitive Memory-Driven Optimization (CMDO), a derivative-free population-based optimizer that represents experience as the relationship between search context, search behavior, and observed outcome. CMDO organizes these experiences across working, ep...

---

### 44. Arbitrary-Accuracy Neural Approximation with Optimal Neuron Count and Near-Optimal Bit Complexity

**Authors:** Zilan Cheng, Li-Lian Wang, Zhongjian Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35628v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35628v1)

**Summary:** We study the minimum number of hidden neurons required for arbitrary-accuracy approximation of multivariate Hölder-continuous functions on $[0,1]^d$ and the associated encoding complexity. For $d\geq 2$, we construct a fixed, explicitly defined activation function for which a closed-form network with two hidden layers of widths $d$ and $1$ achieves arbitrary accuracy in the uniform norm. We prove that $d+1$ is the exact minimum total number of hidden neurons among standard feedforward networks w...

---

### 45. EvE: An Alternate Optimizer to Adam

**Authors:** Shashank Raj, Kalyanmoy Deb

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35614v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35614v1)

**Summary:** Adam and its variants dominate neural network training, but a single run only reveals whether a configuration works well after most of its budget is spent, a poor fit for hyperparameter or architecture search, where configurations must be ranked cheaply and pruned early. We introduce EvE (Evolutionary Explorer), a steady-state, population-of-four differential evolution (DE) optimizer with a targeted Adam fallback: each iteration proposes one candidate via DE, running a short burst of gradient de...

---

### 46. Deep Learning Methods in Neuroscience: From Modeling Molecular Mechanisms to Classifying States of Consciousness

**Authors:** Elena Benderskaya, Anastasiia Alifanova, Svetlana Batalova, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35372v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35372v1)

**Summary:** A critical analysis of contemporary approaches to the study of conscious states. The review focuses on methods of classification, clustering, modeling of brain states under anesthesia and identification of measurable neurobiological characteristics of brain function. A comparative analysis was conducted in the following three major areas: automatic detection of states of consciousness using neural networks based on EEG and fMRI data; modeling of the structural-functional dynamics of the brain un...

---

### 47. Graph neural networks for sampling-invariant embeddings of organized signal sets

**Authors:** Martin Bauw, Santiago Velasco-Forero, Jesus Angulo

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35934v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35934v1)

**Summary:** Sensor networks and radars can deliver signals as organized sets, e.g. ordered signals, signals describing range cells within a grid or signals perceived as graph nodes. Within such sets, individual signals may be characterized by distinct sampling parameters. This paper investigates organized signal sets neural network encoders. In the context of this work, the purpose of such encoders is to project heterogeneously sampled signal sets into an arbitrary fixed-size vectors space. This new represe...

---

### 48. Hidden Activations are not Enough I: Knowledge Matrices as Higher Representations

**Authors:** Marco Armenta

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34166v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34166v1)

**Summary:** We study the knowledge matrix of a trained feedforward network as a higher representation of its inputs. A network is a pair $(W,f)$, a thin representation $W$ of its quiver and an activation $f$; its function factorizes through the space of quiver representations, each input $x$ inducing a representation, and the knowledge matrix $M(x)\in\mathbb{R}^{C\times(d+1)}$ is the contraction of that representation to one matrix whose rows sum exactly to the logits. At one trained network we ask what det...

---

### 49. ADPTNet: Adaptive with Prescriptive Timescales Non-Linear SSM for Sequence Modelling

**Authors:** Matei-Ioan Stan, Oliver Rhodes

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.34034v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34034v1)

**Summary:** A central aim of neuromorphic computing is to provide a viable alternative to highly energy-intensive Transformer-based AI. However, efficient alternatives struggle to capture the set of qualities that have secured the Transformer's status as the de facto standard in sequence modelling. Any realistic contender must be data-adaptive, able to capture long-range dependencies, and GPU-parallelisable, but also non-linearly recurrent to enable complex reasoning. Based on evidence suggesting the audito...

---

### 50. Neuron-Level Architecture Growth: A Controlled Evaluation for EEG Time-Series Decoding

**Authors:** Adam Mounir, Stella Douka, Arnault H. Caillet, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33880v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33880v1)

**Summary:** Convolutional EEG decoders are trained at a fixed width, usually set by their authors on other data. Growing methods add neurons during training where the loss could decrease the most, but whether they improve compared to a reference width is untested on EEG. Here, we grow three convolutional backbones on 12 motor-imagery datasets under three protocols and compare each with its reference model per subject. The growing ShallowFBCSPNet scores 2.9 points above its reference model with only half the...

---

## q-bio.NC

**50 papers**

### 1. Broken scale symmetries in undercomplete linear autoencoders

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03640v1)

**Summary:** Neural network loss landscapes have many symmetries, which are preserved by gradient flow but broken by finite-stepsize stochastic gradient descent (SGD). A canonical example of such a symmetry is scale in homogeneous networks: one can scale up the parameters in one layer and down in the next without changing the network output. Previous work has documented cases in which SGD breaks this symmetry in favor of balancing gradient noise or minimizing fluctuations. Here, we show that the solution geo...

---

### 2. Contrastive Neural Embeddings Reveal Individual Traits Beyond Conversational Role

**Authors:** Hubert Huang, Michelle McCleod, Brendan Ames, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03410v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03410v1)

**Summary:** Contrastive representation learning is increasingly used to recover low-dimensional structure from neural recordings, but its output is typically validated by decoding accuracy rather than by the geometry of the manifold it produces. We apply CEBRA to EEG recorded from dyads in conversation, and analyze the resulting embedding, which training constrains to the 2D sphere. Labels describing the dyads, including the absolute difference between partners' autism-quotient scores, decode well above cha...

---

### 3. Response Variability and Stability in Human Reasoning

**Authors:** Clemens Bombach, Rajmadan Lakshmanan, Marco Ragni

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03008v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03008v1)

**Summary:** Understanding how humans reason -- and how reasoning responses vary across tasks and individuals -- remains a core challenge for modeling and explanation in cognitive science. We investigate the stability of response patterns within reasoners and whether variation in these patterns can be used to predict learning effects. We introduce a formal, geometry-based method to quantify distances between individual reasoning patterns and their internal variability, grounded in heuristic theories. The pro...

---

### 4. NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings

**Authors:** Hanrui Lyu, Baiyuan Chen, Tianshu Tan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02864v1)

**Summary:** Understanding how neural activity represents higher-order cognition and how these representations evolve over time has long been a central pursuit in neuroscience. However, current analytical tools cannot easily distinguish representational plasticity from recording instability in chronic neural recordings. Here, we introduce NeuroLens (Latent Embeddings of Neural Semantics), a self-supervised model based on the Joint-Embedding Predictive Architecture (JEPA) framework that learns denoised, seman...

---

### 5. A foundation for systematic analysis of transformers and RNNs for tractography

**Authors:** Emmanuelle Renauld, Philippe Poulin, Hugo Larochelle, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01894v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01894v1)

**Summary:** Machine learning (ML) has emerged as a promising approach for improving diffusion MRI (dMRI) tractography, a task that remains limited by the intrinsic tension between local diffusion information and global anatomical plausibility. In this work, we systematically evaluate recurrent neural networks (RNNs) and Transformer models for iterative tractography, with particular attention to training strategies, input representations (including convolutional neural network (CNN)-based embeddings and end-...

---

### 6. Inferring Multi-Timescale Neural Dynamics with Switching Linear Dynamical Systems

**Authors:** Lulu Gong, Yongxu Zhang, Shreya Saxena

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01786v1)

**Summary:** Neural activity often exhibits multiple timescales that can vary with behavioral states and task conditions. Identifying these timescales from neural recordings is important for better understanding neural computation and function. However, traditional approaches based on autocorrelation fitting are difficult to scale to high-dimensional population recordings and can become unreliable when neural dynamics change with behavior. State-space models have been a powerful framework for modeling high-d...

---

### 7. A High-Density EEG Dataset for Stimulus-Driven Auditory Attention

**Authors:** Ruofan Yan, Na Lu, Shu Peng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01303v1)

**Summary:** Stimulus-driven auditory attention determines which sound gains priority when multiple sources compete without an explicit listening goal, yet most computational studies focus either on acoustic salience or on decoding predefined attended targets. This study investigates instruction-free auditory competition using the Stimulus-driven Auditory Attention (SAAD) paradigm and develops a neurophysiologically informed framework that integrates stimulus-derived sound priority with trial-specific EEG ev...

---

### 8. Selection rules for the harmonic spectroscopy of animal decisions

**Authors:** Mohammad Salahshour

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.00990v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00990v1)

**Summary:** Spectroscopy reads structure by sending a structured probe into a system and measuring what comes back. Here we apply this principle to animal decision-making. Harmonic Theory casts choice as motion on an angular landscape over heading, whose Fourier components form an animal's decision spectrum. We show that the arrangement of cues enters that landscape as a structure factor, so it factors like a diffraction amplitude, and symmetry imposes selection rules: a p-fold cue array annihilates every h...

---

### 9. One Inference, Four Failure Modes: Formal Models of Why Pain Location Fails

**Authors:** Adam Y. Shavit

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.00866v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00866v1)

**Summary:** Patient-reported pain location is diagnostically decisive for some presentations and nearly uninformative for others. A companion paper argues this is not one gradient of diagnostic utility but three distinct failures of localization. This paper gives those failures their mathematics and shows they are one object: a single Bayesian generative model failing at different nodes - the likelihood, the model class, and group- or context-dependence in that same likelihood. The count is not in dispute: ...

---

### 10. Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning

**Authors:** Syon Mansur, Joel Zylberberg

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00753v1)

**Summary:** End-to-end backpropagation has been the dominant mode of training in deep learning, allowing for the coordination of parameter updates across layers of a neural network. Prior studies have explored alternative -- and, in some cases, simpler -- training mechanisms, showing that they can sometimes achieve performance similar to backpropagation. However, the architectural conditions under which locally optimized networks, which avoid end-to-end backpropagation of error, can learn representations co...

---

### 11. MEG-Mamba: A Scalable State-Space Foundation Model for Magnetoencephalography

**Authors:** Chetan Gohil, SungJun Cho, Oiwi Parker Jones, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00746v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00746v1)

**Summary:** Magnetoencephalography (MEG) is an imaging technique that offers a non-invasive, millisecond-resolution view of human brain activity. The increasing availability of MEG data presents an opportunity to take advantage of a recent advance in artificial intelligence, namely self-supervised foundation models. Existing foundation models for MEG (and electroencephalography) have been built on a transformer architecture. Here, we introduce MEG-Mamba: a generative foundation model for neural activity (so...

---

### 12. Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation

**Authors:** Jafar Shamsi, Navid Akbari, Sonia Sennik, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00719v1)

**Summary:** Pseudo-random number generation often requires trade-offs among quality, power consumption, and bandwidth to produce unpredictable sequences of numbers. The brain, on the other hand, efficiently generates unpredictable output complex network dynamics occurring in a high-dimensional state. This state, which is hypothesized to be chaotic, relies on the balance between excitation and inhibition. Here, we investigated if computational models of these chaotic balanced states can be harnessed for Neur...

---

### 13. Synaptic placement reflects shared input in Drosophila descending neurons

**Authors:** Xizhe Zhang

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00690v1)

**Summary:** Network topology describes connections between neurons, whereas synaptic placement specifies how those connections are arranged within individual cells. How these levels of organization correspond remains incompletely understood. Here we show that connectivity between presynaptic neurons is reflected in relative input placement within Drosophila descending neurons (DNs). Across thousands of one-way DN connections in the independently reconstructed MaleCNS and FlyWire brains, inputs from sources ...

---

### 14. Stochastic Dynamics of Large-Scale Motif-Embedded Spiking Neuronal Networks

**Authors:** Gurpreet Jagdev, Richard Bertram, Na Yu

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00616v1)

**Summary:** We examine how local motif structure and global network topology jointly shape spiking dynamics in stochastic neuronal networks. Using networks of Izhikevich neurons with Erdős-Rényi (ER) and scale-free (SF) background connectivity, we compare motif-embedded networks with synapse-count-matched, non-motif controls under noise- and stimulus-driven protocols. Motif embedding increases noise-induced coherence in both topologies and provides a smaller improvement in signal transmission, while SF-base...

---

### 15. Stochastic dynamics and synchronization in motif-based neuronal networks

**Authors:** Gurpreet Jagdev, Yifei Lu, Richard Bertram, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00597v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00597v1)

**Summary:** Neuronal networks exhibit complex dynamics shaped by connectivity and stochastic input. Empirical studies show that neuronal networks contain recurring subgraphs, or motifs, but the collective influence of different motif types after embedding in large stochastic networks remains less well understood. We construct a spiking network composed of six representative structural classes and examine how intrinsic noise, coupling strength, inter-motif connectivity, network size, and neuronal heterogenei...

---

### 16. Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text

**Authors:** Dulhan Jayalath, Oiwi Parker Jones

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40359v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40359v1)

**Summary:** We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time series of brain activity from subjects perceiving continuous speech are segmented into fixed-length windows starting at each word. A neural network then generates predictions for all of the words in a sentence together. Neighbouring windows partially overlap, implicitly revealing the interval between...

---

### 17. Disentangling Computation in Multi-Task Neural Networks with the Green's Operator

**Authors:** James Hazelden

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40292v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40292v1)

**Summary:** How is computation organized and reused across tasks and time in a trained recurrent network? Most analyses emphasize the geometry of neural activity, dynamical motifs, or local perturbation growth. We instead study the network's global first-order perturbation response. The finite-horizon Green's operator maps perturbations at each source along a trajectory to their downstream state-space responses and therefore directly represents perturbation routing. Simple reductions of this operator provid...

---

### 18. Attraction to hierarchical feature memory explains orientation bias

**Authors:** Kira Michaela Düsterwald, Peter Vincent, Ana Kapros, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40204v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40204v1)

**Summary:** When recalling the orientation of recent stimuli, observers are systematically biased away from the cardinal axes. The prevailing explanation is that this ''anti-cardinal bias'' arises because cardinal orientations are encoded with greater neural resources and therefore less noise, consistent with efficient coding of environmentally common features. Under this account, the bias should occur independently for each stimulus; any serial attraction towards previously seen orientations should be inde...

---

### 19. Belief-Based Maximum Occupancy Principle and Active Inference

**Authors:** Manolis Mylonas, Rubén Moreno Bote

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39342v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39342v1)

**Summary:** Intrinsic motivation plays a central role in adaptive and goal-directed behavior by conferring agents reward-independent objectives and biases useful to act in noisy and uncertain environments. Active Inference addresses the problem of acting in a partially observable environment through a principled framework for belief updating and action selection. A key component of Active Inference is the specification of prior preferences, which shapes behavior by encoding desirable future outcomes. An int...

---

### 20. Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison

**Authors:** Gyujeong Park

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39248v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39248v1)

**Summary:** Randomised copies of a connectome are the usual baseline for asking whether measured wiring matters, and the answer depends on what the randomisation preserves. We evolved embodied foraging agents whose brains are a compressed adult Drosophila connectome (FlyWire v783; 512 cell-type groups and 1,000 Kenyon cells) alongside agents built on randomised wiring, in pre-registered experiments with ten seeds, four ecologies and 600 generations. Two standard randomisations, a column shuffle and degree-p...

---

### 21. Association profile conditioning in a set-temporal transformer for cross-session intracortical motor decoding

**Authors:** Xinyuan Zhang, Handong Mo, Pengfei Wen, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39080v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39080v1)

**Summary:** Intracortical motor decoders degrade across sessions because the set of recorded units changes and persisting units can alter how their firing relates to behavior. Most existing methods update network weights on each new session or rely on unlabeled activity, which does not directly reveal such changes. We present APST, an Association Profile-conditioned Set-Temporal transformer that adapts to new sessions with all network weights frozen. From a few labeled calibration trials, APST summarizes ho...

---

### 22. Not all solutions are created equal: An analytical dissociation of functional and representational similarity in deep linear neural networks

**Authors:** Lukas Braun, Erin Grant, Andrew M. Saxe

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38998v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38998v1)

**Summary:** A foundational principle of connectionism is that perception, action, and cognition emerge from parallel computations among simple, interconnected units that generate and rely on neural representations. Accordingly, researchers employ multivariate pattern analysis to decode and compare the neural codes of artificial and biological networks, aiming to uncover their functions. However, there is limited analytical understanding of how a network's representation and function relate, despite this bei...

---

### 23. Future Video Generation Better Aligns with the Human Visual Cortex than Observed Video

**Authors:** Chang-Bae Bang, Hyungjin Chung, Byung-Hoon Kim

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38819v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38819v1)

**Summary:** Studying the alignment between the internal representations of vision models and the responses of the visual cortex to the same observed visual stimuli has enabled us to better understand human visual processing. However, studies so far have largely overlooked the fact that the human brain not only processes observed visual stimuli, but also predicts upcoming stimuli based on what has been observed. Accordingly, we hypothesize that internal representations for generating future video frames are ...

---

### 24. How much of fly walking is written in the wiring?

**Authors:** Isabel Guan, Yuntian Zhao, Dingyuan Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38665v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38665v1)

**Summary:** Connectome models of the fly nerve cord generate walking-like motor rhythms, but oscillation alone does not show that the specific wiring matters. Here we provide, to our knowledge, the first test of which features of motor output depend on the specific wiring. We simulated the leg motor systems of two independent Drosophila connectomes, with synapse counts as fixed weights and glutamatergic synapses treated as inhibitory, and compared each with six families of rewired networks that preserve pro...

---

### 25. TERRA: Terrain-Aware Reconstruction, Retargeting and Control for Musculoskeletal Locomotion

**Authors:** Merkourios Simos, Chengkun Li, Bianca Ziliotto, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38653v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38653v1)

**Summary:** Recent advances in musculoskeletal modeling and reinforcement learning have enabled muscle-actuated agents to reproduce increasingly complex human motions. Yet these capabilities remain largely confined to flat ground, in part because motion datasets rarely include aligned terrain geometry and because retargeting terrain interactions to complex musculoskeletal bodies is challenging. We present TERRA, an end-to-end pipeline for terrain-aware retargeting and control of musculoskeletal locomotion. ...

---

### 26. Autoregressive Frontier Expansion: Growing Trees with Graph Machine Learning

**Authors:** Umer Gupta, Saku Peltonen, Martin Ritzert

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38506v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38506v1)

**Summary:** Tree-like branching structures are common in nature, from botanical trees to neurons, blood vessels and respiratory trees. Their branching shape often reflects function, making structural modelling central to understanding how these systems work. Because acquiring real-world 3D data is often expensive or infeasible, realistic generative models are valuable for simulation and data augmentation. Existing morphology-specific models either constrain how topology is generated or rely on hand-tuned, m...

---

### 27. Does Global Neuronal Workspace Theory Explain Phenomenal Consciousness? The Motivated Emotional Mind Challenge

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38495v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38495v1)

**Summary:** Global Neuronal Workspace Theory (GNWT) is one of the most extensively developed empirical research programmes on access consciousness. By contrast, the Motivated Emotional Mind (MEM) model proposes an embodied, semi-hierarchical associative memory in which representational selection, action, recurrent reconstruction of modality-specific fields, interoception, and valence form a single functional cycle. This article assesses whether MEM mechanisms can reproduce the functions explained by GNWT an...

---

### 28. Embodiment-aware control by inference over the operator: a simulation study

**Authors:** Sara Falcone

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38437v1)

**Summary:** Teleoperation systems are tuned for channel fidelity, while whether the operator experiences the device as part of the body, the Sense of Embodiment (SoE), is measured only afterwards, by questionnaire. Predictive-processing accounts suggest controlling devices to reduce the mismatch between the operator's predictions and the returned feedback, but those predictions are unobservable, and an objective that only penalizes mismatch is minimized by removing feedback. We formulate an embodiment-aware...

---

### 29. Traversing the solution space of neural networks with Hessian Null Space Continuation

**Authors:** Ann Huang, Mitchell Ostrow, Zhouyang Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38081v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38081v1)

**Summary:** On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. ...

---

### 30. Which Attention Heads are like the Human Head? Not the Ones that Compute

**Authors:** Christopher Pinier, Gustaw Opiełka, Hannes Rosenbusch, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37991v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37991v1)

**Summary:** Brain-AI alignment is often interpreted as a sign that model and brain perform similar computations. Whether the aligned units are causally involved in model computation is rarely checked. On an abstract pattern-completion task (AAABAAA $\rightarrow$ B), we compare LLM attention-head representations with human EEG and test how ablating those heads affects task performance. Alignment and causation dissociate: brain-aligned heads contribute to performance, but their removal is substantially less d...

---

### 31. Flattening the Connectome Spectrum: A Spectral Filter for FC Induces a Pretraining Target for fMRI Encoders

**Authors:** Giovanni Marraffini, Victoria Shevchenko, Carlo Alberto Barbano, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37642v1)

**Summary:** Self-supervised pretraining reshaped prediction in language and vision, and brain foundation models (BFMs) inherited its promise. Representations learned from large unlabelled corpora should capture individual functional dynamics and generalise across cohorts. However, kernel ridge regression (KRR) fitted on functional connectivity (FC) matrices still predicts individual phenotypes more accurately than any BFM we tested. In this paper, we show that KRR is weighted by the eigenvalues of the FC wh...

---

### 32. An adaptive fractional state links circuit mechanisms to cortical dynamics across the visual hierarchy

**Authors:** Brendan Harris, Pulin Gong

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37355v1)

**Summary:** Cortical circuits must respond flexibly to new inputs while integrating information about the past, yet the way in which neural activity reconciles these competing demands remains unclear. Combining Neuropixels recordings from six mouse visual areas with mechanistic circuit modeling, we identify a dynamical regime in which heavy-tailed superdiffusive fluctuations coexist with long-range temporal dependence and oscillations. We formalize this regime as the adaptive fractional (AF) state, using an...

---

### 33. Volcanite: Commodity-Hardware Segmentation Volume Visualization for Connectomics and Beyond

**Authors:** Max Piochowiak, Reiner Dolp, Julian Herold, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36898v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36898v1)

**Summary:** Modern imaging produces terabyte-scale segmentation volumes, assigning each voxel an object label. These categorical, boundary-sensitive and label-rich data underpin connectomics and other imaging-driven fields, yet their scale often forces interpretation through slices, approximate meshes or distributed workflows that obscure spatial context and voxel-level defects. Here we show that such volumes can be explored directly on commodity hardware with Volcanite, an open-source framework for dense-s...

---

### 34. From Neurons to Conversation: Speech Brain-Computer Interfaces

**Authors:** Moein Khajehnejad, Forough Habibollahi, Tommaso Boccato, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36736v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36736v1)

**Summary:** Speech brain-computer interfaces (BCIs) aim to restore communication by transforming neural activity related to speech, language, or communicative intent into external outputs such as text, synthesized voice, or avatar control. Recent advances in intracortical and electrocorticographic recording, deep sequence models, and language-model-assisted decoding have enabled rapid progress, including high-performance attempted-speech decoding and increasingly naturalistic speech synthesis. Yet these ach...

---

### 35. Neural Structural Reasoner: A Brain-inspired Architecture for Reasoning over Structured Knowledge

**Authors:** Zixing Jia, Yuhang Pan, Ni Ji

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36620v1)

**Summary:** Structural reasoning, the ability to recognize and make inferences over the relational structure between objects and concepts, is a hallmark of human cognition, yet prevailing methods often collapse relational topology into flat embeddings, cannot discover hidden structure and lack interpretability. We introduce Neural Structural Reasoner (NSR), a brain-inspired network that preserves relational structure directly in the connectivity and dynamics of coupled neuronal populations. NSR draws inspir...

---

### 36. Large-scale factor analysis shows machine intelligence is only partially interpretable

**Authors:** Faiz Ghifari Haznitrama, Afrizal Hasbi Azizy, Faeyza Rishad Ardi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36515v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36515v1)

**Summary:** A common assumption in language model development is that cognitive abilities are organized around a general, domain-free intelligence factor, like fluid intelligence in humans. This assumption is rarely tested directly, and prior attempts have done so only at a much smaller scale. We take a latent variable approach to intelligence in language models, similar to how psychometricians study psychological constructs. Performance in every specific problem set is influenced by a domain-specific and a...

---

### 37. Receptive-field-constrained stimulus optimization for human early and intermediate visual cortex

**Authors:** Junru Zhao, Hanfei Guo, Andrew Luo, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36391v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36391v1)

**Summary:** An ongoing challenge in sensory neuroscience is to characterize the feature dimensions encoded by cortical populations. Recent approaches probe feature selectivity in a data-driven way, by synthesizing a most-exciting-input (MEI) for a target neural population. While this approach has been successfully applied to human higher visual cortex using fMRI data, generating MEIs for early- and mid-level retinotopic visual areas requires additional modeling constraints due to small receptive field sizes...

---

### 38. Cross-attention encoding models reveal dynamic spatiotemporal routing across human higher visual cortex

**Authors:** Iishaan Inabathini, Margaret M. Henderson

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36366v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36366v1)

**Summary:** Understanding how the brain parses actions and events from time-varying natural inputs is a central challenge in neuroscience. Recent work has used deep neural network (DNN) models to build stimulus-computable fMRI encoding models that predict single-voxel responses to complex natural videos. However, the majority of video-computable encoding models predict responses using simple linear mappings from model tokens, overlooking the spatiotemporal structure shared by video representations and neura...

---

### 39. Socio-cognitive models in a patch foraging setting: a case study for model selection and parameter identifiability methods

**Authors:** Lisa Blum Moyse, Ahmed El Hady

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36231v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36231v1)

**Summary:** Collective patch-foraging experiments in the laboratory provide a controlled setting in which social information use can be quantified. Here, we consider a go/no-go task in which groups choose between two patches differing in food reward probability. We use agent-based simulations, underpinned by an augmented collective drift-diffusion model, to investigate alternative mechanisms for representing and integrating social information. We consider two representations, continuous (counting representa...

---

### 40. Better Behavioral Prediction, More Faithful Model Ablations? Evidence from Sequential Choice

**Authors:** Hanbo Xie

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.36097v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36097v1)

**Summary:** Using predictive models to explain cognition requires more than accurate behavioral predictions. Input ablations offer an appealing route: remove information from a model and interpret the resulting performance change as evidence of its importance for behavior. Yet this inference assumes that the model's dependence on information reflects the dependence of the process generating the behavior. We test it in two synthetic sequential bandit tasks with known generating policies, where past choices c...

---

### 41. NeuronSifter: Intervention Planning in CNS Microenvironments

**Authors:** Haowei Xu, Wanyi Fu, Hongbin Han, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35445v2) | 📄 [PDF](https://arxiv.org/pdf/2609.35445v2)

**Summary:** Prioritizing central nervous system (CNS) interventions requires predicting how a dose, route, and schedule act on a partially observed microenvironment, then choosing the measurement that would change the decision. Action-conditioned predictors reduce a regimen to an identity token or a scalar exposure, discarding where and when the target is engaged; handing a point estimate to a separate planner then discards the joint uncertainty that makes a measurement worth running. We therefore treat dec...

---

### 42. NeuronDiscover: Agent-in-Twin for Mechanistic Discovery in Neuronal Microenvironments with World Action Models

**Authors:** Haowei Xu, Wanyi Fu, Hongbin Han, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35338v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35338v1)

**Summary:** Mechanistic discovery in neuronal microenvironments requires interventions and measurements that separate competing explanations of solute transport and neuronal response. Predictive accuracy cannot settle the question: a real mechanistic change and an error in the computational twin leave the same signature in sparse observations. We formalize this twin confounding and reason over a joint mechanism--discrepancy belief, designing experiments that separate the two. NeuronDiscover is an Agent-in-T...

---

### 43. High-rank connectivity scaffolds support precision and generalisation in recurrent neural networks

**Authors:** Ian Hawes, Matt Nolan

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35207v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35207v1)

**Summary:** A major challenge in neuroscience and machine learning is to connect single-neuron influence, population dynamics, and circuit connectivity in a causal account of computation. Much previous work has shown that low-rank connectivity can generate low-dimensional dynamics in trained artificial neural networks, but this leaves unclear the functional relevance of the higher-rank structure of biological neural circuits and many artificial neuronal networks. Here we analyse recurrent neural networks tr...

---

### 44. Scaling Laws for EEG Decoding: How Much Data Is Enough?

**Authors:** José Maurício Nunes de Oliveira, Bruna J. Lopes, Léo Burgund, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35056v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35056v1)

**Summary:** Deep learning has become a cornerstone of EEG-based brain decoding, with a growing number of architectures proposed every day. However, how the performance of these different models scales with data volume is not clear. Although this relationship has been characterized in other fields under the name of scaling laws, it remains poorly understood in the EEG domain. The present study addresses this gap by investigating how scan time and subject diversity affect the performance of different architec...

---

### 45. On the Limits of Metacognitive Monitoring in LLMs

**Authors:** Dongqi Han, Yifan Yang, Dongsheng Li

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34864v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34864v1)

**Summary:** Reliable decisions depend on recognizing when an answer may be wrong. In biological cognition, metacognitive monitoring can dissociate from task performance, raising the question of how closely solving and judging are linked in language models. Here we study the confidence reports of four frontier models across 15 benchmarks. High task accuracy can coexist with weak error discrimination: a model solves 97% of competition mathematics problems while its answer-time confidence ranks correct answers...

---

### 46. Separating personal from population gains when calibrating EEG foundation models for new users

**Authors:** Xilin Tao, Kani Chen

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34801v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34801v1)

**Summary:** Foundation models are increasingly adapted to individual users, but an apparent personalization gain can simply reflect a stronger population model. This distinction matters for brain-computer interfaces, where every new user must be calibrated. We evaluated personal adaptation of three frozen EEG foundation models (CBraMod, REVE and LaBraM) in 235 held-out subjects from three motor-imagery datasets, comparing each subject's adapter with the population model and with adapters fitted to other sub...

---

### 47. Automatic Generation of Expert-Level Neuron Segmentation Masks from Fluorescence Microscopy Images for Non-Invasive Deep Learning Analysis of Phase-Contrast Images

**Authors:** Gerard Villarroya-Piqué, Víctor M. González, Esther Serrano-Pertierra, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34464v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34464v1)

**Summary:** Background & Objective Accurate segmentation of neurons in microscopy images of neuronal cultures is crucial for research on neurodegenerative diseases and neurotoxicity. Manual annotation of such images is time-consuming, subjective, and inconsistent across experts. Deep learning (DL) models offer an effective alternative, but require high-quality training datasets composed of microscopy images with accurately segmented neurons, typically created by experts. Neuronal cultures can be imaged usin...

---

### 48. FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model

**Authors:** Shucheng Liu, Changchun Shi, Kai Zhang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34354v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34354v1)

**Summary:** Modeling resting-state functional magnetic resonance imaging (rs-fMRI) data is crucial for understanding brain-wide neural activity. However, traditional methods struggle to capture complex temporal dynamics over long horizons, to account for the brain's anatomical spatial structure, and to model high-dimensional ambient signals that lie on a low-dimensional intrinsic subspace. We propose FAST-Brain, a unified flow-aligned spatio-temporal surrogate brain model that addresses all three challenges...

---

### 49. T-SNN: Temporal Simplicial Neural Network for EEG Decoding

**Authors:** Nikita Malik, Shubhajit Roy, Mohit Kataria, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.34002v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34002v1)

**Summary:** Decoding brain states requires models that capture both the evolution of neural activity and interactions among groups of brain regions. Existing EEG methods often treat recordings as multivariate time series or represent functional connectivity with pairwise graphs, leaving dynamic higher-order interactions largely unmodeled. We introduce the Temporal Simplicial Neural Network (T-SNN), which represents EEG recordings as sequences of evolving simplicial complexes. By combining simplicial convolu...

---

### 50. Harmonic Theory of Behavior

**Authors:** Mohammad Salahshour, Iain D. Couzin

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33896v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33896v1)

**Summary:** Traditional models of collective behavior rely on prescribed interaction rules, leaving unresolved the question of how behavior arises from neural representations of space. Here, we develop a first-principles theory in which movement, decision-making, and collective organization emerge by coarse-graining fast neural dynamics on a topological representation of directional space. For a ring manifold encoding heading, this reduction yields a macroscopic theory of behavior: a decision landscape over...

---

## stat.ML

**50 papers**

### 1. Simulation-Free Learning of Population Dynamics with Wasserstein Lagrangian Residuals

**Authors:** Fedor Sergeev, Markus Heinonen, Daniel Waxman, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03679v1)

**Summary:** The dynamics of cells, organisms, and fluids are often modeled as probability distributions evolving over time. Reconstructing and extrapolating this evolution from unpaired snapshots requires assumptions about the underlying process. Wasserstein gradient flows are a common choice, but they cannot describe conservative or periodic dynamics. Lagrangian mechanics in Wasserstein space covers both, but existing methods for learning it are simulation-based: they run a numerical solver at every traini...

---

### 2. Planning to Learn

**Authors:** Ian Osband

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03667v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03667v1)

**Summary:** Policy-gradient methods are central to modern reinforcement learning, including LLM post-training. When they struggle, the usual suspects are exploration, credit assignment and action-sampling noise. Classification has none of them. A classifier is a policy whose expected reward, its \emph{expected accuracy}, is the probability it assigns to the correct label, and because that label is known, the policy gradient is exact and smooth. Yet exact policy gradient loses to cross-entropy, even on expec...

---

### 3. Amortized Structured Stochastic Variational Inference for Gaussian Process Latent Variable Models

**Authors:** Maksym Tretiakov, Sarah Lucie Filipp, Vincent Fortuin, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03647v1)

**Summary:** Many machine learning methods aim to approximate the lower-dimensional manifold on which the data lives. A desirable feature of such methods is that they should capture the epistemic uncertainty of this learned manifold. One model that achieves this is the Gaussian Process Latent Variable Model, in which a Gaussian Process (GP) mapping from the latent space provides an estimate of the uncertainty of the manifold. However, the effectiveness of this uncertainty estimation is limited by the mean-fi...

---

### 4. When May a Bandit Leave Its Anchor? E-Process-Authorized Thompson Sampling under Non-stationarity

**Authors:** Mayand Gulati, Kerong Wang, WeiChen Au

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03646v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03646v1)

**Summary:** Stationarity rewards memory, but after a change the same history can mislead. We ask when forgetting should be permitted. E-process-authorized Thompson sampling (e-ATS) gives each arm full-history and discounted Beta states. An anytime-valid e-process first authorizes the discounted state, then a reversible relevance score controls its influence. Before authorization, e-ATS exactly follows optimistic Thompson sampling (OTS). Under a Beta-Bernoulli prior-predictive stationary model, e-ATS's proba...

---

### 5. Broken scale symmetries in undercomplete linear autoencoders

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03640v1)

**Summary:** Neural network loss landscapes have many symmetries, which are preserved by gradient flow but broken by finite-stepsize stochastic gradient descent (SGD). A canonical example of such a symmetry is scale in homogeneous networks: one can scale up the parameters in one layer and down in the next without changing the network output. Previous work has documented cases in which SGD breaks this symmetry in favor of balancing gradient noise or minimizing fluctuations. Here, we show that the solution geo...

---

### 6. Below what training size do deep tabular generators stop beating trivial baselines? A preregistered benchmark on a size ladder of clinical and standard datasets

**Authors:** Shivam Shrivastava

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03500v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03500v1)

**Summary:** Deep tabular generative models are benchmarked on datasets with tens of thousands of rows; clinical datasets have hundreds. We preregistered and ran a size-ladder benchmark to find where the two regimes diverge: 8 public datasets subsampled from 200 to 20,000 training rows, seven generators (independent marginals, Gaussian copula, SMOTE, unconditional SMOTE, CTGAN, TVAE, TabDDPM) with a fixed 20-trial tuning budget and 5 evaluation seeds, plus 4 natively small clinical datasets at true size, for...

---

### 7. AREX: Affine-Residual Exponential Integrator for Few-Step Sampling in Flow Matching

**Authors:** Shizheng Lin, Soon Hoe Lim, N. Benjamin Erichson

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03483v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03483v1)

**Summary:** We introduce AREX, a training-free sampler for pretrained flow matching models that uses the target mean and covariance to capture an analytically tractable part of the sampling dynamics. We show that the velocity field of the moment-matched Gaussian target is the $L^2$-optimal affine approximation to the marginal velocity field. This motivates decomposition of the learned dynamics into an affine component over the whole sampling path, determined by the first two target moments, and a neural res...

---

### 8. When Is Accuracy Evidence? A Unified Theory of Generalisation, Validation, and Information Fusion

**Authors:** JM Gorriz

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03465v1)

**Summary:** K-fold cross-validation (CV) is widely used as evidence of out-of-sample performance, although folds are neither independent experiments nor equally informative under heterogeneous data. Cross Upper-Bound Validation (CUBV) replaces point-wise CV accuracy by conservative upper bounds on true risk. Here we generalise CUBV through a single exponential framework in which the moment-generating function of the generalisation gap is controlled by a cumulant envelope gamma(lambda). This yields a family ...

---

### 9. Iterating Consistency Models: Stability, Error Bounds and Noise Schedules

**Authors:** Alessio Spagnoletti, Abdul-Lateef Haji-Ali, Andrés Almansa, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03414v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03414v1)

**Summary:** Consistency models (CMs) have become a leading approach for generating high-quality samples in few steps. However, adding steps can improve or degrade sample quality in ways that are highly sensitive to the schedule and that existing theory does not fully explain. To provide accuracy guarantees and guide CM sampler design, we analyze multistep CM sampling as a composition of noising and approximate denoising operators. Under explicit, verifiable stability assumptions, we derive a non-asymptotic ...

---

### 10. DAWIS: Data Assimilation with Windowed Inverse Sampling via Multitask Interpolants

**Authors:** Erik Wikingsson, Martin Andrae, Tomas Landelius, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03314v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03314v1)

**Summary:** Flow- and diffusion-based generative models have recently emerged as flexible and highly efficient forecasting models for dynamical systems. When combined with inference-time guidance, they offer a promising route to high-dimensional non-Gaussian data assimilation (DA), the problem of combining forecasts with observations to estimate latent system states. Existing filters, however, condition on a fixed history and assimilate only the most recent observation, leaving them unable to revise past st...

---

### 11. SDECast: Probabilistic Weather Forecasting in Continuous Time with Neural SDEs

**Authors:** Maria Marchenko, Martin Andrae, Fredrik Lindsten, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03313v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03313v1)

**Summary:** Existing machine learning weather forecasting models typically generate forecasts through autoregressive rollouts at a fixed temporal resolution. While highly efficient for long-range prediction, this formulation can suffer from severe error accumulation when used with shorter time steps and does not explicitly encode the locality and temporal continuity of atmospheric dynamics. To address these limitations, we introduce **SDECast**, a Neural Stochastic Differential Equation (SDE) framework for ...

---

### 12. Near-Optimal Convex Optimization with Lazy Second-Order Oracles

**Authors:** Xinliang Zhang, Lesi Chen, Chengchang Liu, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03222v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03222v1)

**Summary:** This paper studies the complexity of convex optimization using lazy second-order oracles (Doikov, Chayti, and Jaggi, ICML 2023), where an algorithm queries gradients every iteration and Hessians once per $m$ iterations. Under this setting, we show a lower bound of $Ω(m+ m^{1/7} ε^{-2/7})$ on the number of total iterations to find an $ε$-solution using a novel block zero-chain construction. Then we propose a novel method that achieves a new upper bound of $\tilde{\mathcal{O}}(m+ m^{1/7} ε^{-2/7})...

---

### 13. Predictively Oriented Gaussian Process Posteriors

**Authors:** Callum Lau, Jeremias Knoblauch, Louis Sharrock

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03201v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03201v1)

**Summary:** Gaussian Processes (GPs) are a powerful tool for modelling and quantifying uncertainty in functional relationships. However, they require practitioners to make a number of design decisions, such as the choice of the kernel and the observation model. Suboptimal choices can produce misspecified models that do not capture the underlying data generating process. We introduce Predictively Oriented Gaussian Processes (PrO-GPs), which treat predictive uncertainty as the primary inferential target and p...

---

### 14. Invariance of Clustering Operations in Causal Effect Identification

**Authors:** Jani Nykänen, Otto Tabell, Santtu Tikka, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03101v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03101v1)

**Summary:** Clustering variables in causal graphs reduces the size of the graph and simplifies causal inference. However, arbitrary clustering can alter crucial causal relations among variables and lead to erroneous conclusions. While the identifiability of a causal effect in the clustered graph implies the identifiability in the original graph under mild conditions, nonidentifiability in clustered graph does not imply nonidentifiability in the original graph without further assumptions. When both identifia...

---

### 15. GTDD: Generative Test-Driven Development for AI Coding Agents with Adversarial Testing

**Authors:** Masahiro Kato

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02952v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02952v1)

**Summary:** Test-driven development gives AI coding agents executable requirements for implementing software. Because these agents can adapt their implementations to the examples they observe, passing a predetermined collection of tests can leave substantial parts of the intended behavior unimplemented. We propose Generative Test-Driven Development (GTDD), a formulation of test-driven development in which a separate testing agent generates new inputs after each candidate implementation is fixed, using a hum...

---

### 16. Cross-Fitting Under Nonregularity: Normality and Inference via Locality

**Authors:** Bruno Fava

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02944v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02944v1)

**Summary:** Cross-fitting is routine in much of applied research. While conventional confidence intervals that ignore cross-fold dependence are asymptotically valid in several settings, they undercover in many applications that share a common form of nonregularity: from the classic cross-validation problem of testing whether a fitted model outperforms another, to testing for heterogeneous treatment effects with machine learning, to estimating the value of a potentially non-unique optimal treatment regime. E...

---

### 17. A Residual Tree Gaussian Process Modeling Framework for High-Dimensional Data

**Authors:** Pulong Ma, Li Ma

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02893v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02893v1)

**Summary:** With the advance of measurement technologies and increasing computing power, large spatial data with heterogeneous structures are often collected over high-dimensional domains. Existing Gaussian process (GP) models and computational strategies are often inadequate for analyzing such datasets in multi-dimensional domains. To address these challenges, we develop a Bayesian residual tree GP methodology called ResTGP for large spatial data with potentially heterogeneous structures in multi-dimension...

---

### 18. Muon Learns Facts Better: Understanding the Role of Spectral Orthogonalization

**Authors:** Xuheng Li, Qiwei Di, Yuan Cao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02798v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02798v1)

**Summary:** The Muon optimizer applies spectral orthogonalization to matrix-valued updates and has shown strong performance in large-scale neural network training, yet the mechanisms of this transformation in feature learning remain poorly understood. In this work, we investigate this question through a tractable factual-recall model, where a fact maps each subject-relation pair to an answer, and a linear transformer learns the subject- and relation-dependent information required to recover this mapping. Th...

---

### 19. Hold-Out Scoring for Efficient Gaussian DAG Learning

**Authors:** Donguk Shin, Byeongguk Kang, Inseol Lee, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02785v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02785v1)

**Summary:** High-dimensional Gaussian DAG learning faces a statistical-computational gap: methods with sharp sample complexity rely on computationally expensive subset search and a supplied indegree bound, whereas polynomial-time alternatives have less favorable sample complexity. We introduce HOST, an efficient DAG learning algorithm that replaces subset search with nodewise hold-out scoring and convex regression, without requiring a supplied indegree bound. Our key insight is that recovering a correct ord...

---

### 20. Nearly Optimal Fixed-Confidence Best-Arm Identification with 1-Bit Feedback

**Authors:** Khang Luong, Dinh Thai Son, Hoang Ta, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02771v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02771v1)

**Summary:** We study fixed-confidence best-arm identification under strict 1-bit feedback constraints. At each round, the learner selects an arm and a query set, and receives only a single bit indicating whether the sampled reward belongs to that set. We consider a distribution-free finite-variance setting with arm-wise localization, where direct empirical mean estimation is no longer available and clipping becomes unavoidable. We first formulate a time-uniform 1-bit mean-estimation primitive based on rando...

---

### 21. Differential Privacy of Gradient Descent on Perturbed Objectives

**Authors:** Austin Watkins, Raman Arora

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02716v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02716v1)

**Summary:** Objective perturbation adds a random linear term to a regularized empirical risk and releases the exact perturbed minimizer. We study the finite computation obtained by releasing the $N$-th iterate of deterministic gradient descent on $w\mapsto F(w;S)+\langle z,w\rangle$, where $z\sim\mathcal N(0,σ^2I_d)$ is drawn once before optimization. For strongly convex and smooth objectives with Lipschitz Hessian, we prove an explicit condition under which the map $z\mapsto w_N$ is a $C^1$-diffeomorphism ...

---

### 22. Generalization Properties of Score-matching Diffusion Models for Intrinsically Low-dimensional Data

**Authors:** Saptarshi Chakraborty, Quentin Berthet, Peter L. Bartlett

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02663v1)

**Summary:** Despite the remarkable empirical success of flow-matching models, their statistical generalization guarantees remain underdeveloped. Existing analyses often impose restrictive assumptions on the estimated velocity field and yield convergence rates that fail to reflect the intrinsic low-dimensional structure common in real data, such as natural images and molecular geometries. In this work, we study the statistical generalization of flow-matching models for learning an unknown distribution $P_{\m...

---

### 23. High-Dimensional Asymptotics and Dataset Selection for Private Transfer Learning

**Authors:** Filip Kovačević, Edwige Cyffers, Stefano Sarao Mannelli, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02578v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02578v1)

**Summary:** To commit to buying external data or participate in collaborative learning, one must decide whether the additional data will improve prediction enough to justify the cost. This comes with several challenges: (i) the decision often relies only on aggregated statistics available publicly, rather than individual-level data; (ii) covariate and model shifts can induce negative transfer, so the additional data deteriorates rather than improves performance; (iii) if the data is sensitive, its privatiza...

---

### 24. ENCORE: Exact Non-equilibrium COntrol with Replica Exchange for Diffusion Generation

**Authors:** Jiahao Yu, Saifuddin Syed, José Miguel Hernández-Lobato, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02538v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02538v1)

**Summary:** Inference-time control steers a pretrained generative model towards a target distribution without retraining. We study tilted targets $π_0\propto G_0\,p_0$, where $p_0$ is the sampler output distribution and $G_0$ is an evaluable reweighting function. Existing approaches rely on sequential annealing with sequential Monte Carlo (SMC) or parallel annealing with replica exchange (RE). Sequential control is exact but needs large particle populations, whereas no exact parallel control method exists: ...

---

### 25. Learning Style, Forgetting Semantics: A Case Study of SFT and RFT on Classification Tasks

**Authors:** Haodong Liang, Yanhao Jin, Krishnakumar Balasubramanian, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02437v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02437v1)

**Summary:** Why does supervised fine-tuning (SFT) lead to more forgetting than reinforcement fine-tuning (RFT), even when all teacher demonstrations are semantically correct? We study this question on classification tasks where tokens within each semantic class express the same semantic answer in different styles. The tasks share an underlying semantic rule but differ in their prompt distributions and teachers' stylistic preferences. Using a tractable linear-softmax policy, we derive an exact decomposition ...

---

### 26. Conformal Prediction for Time Series with Deep Sequence Models

**Authors:** Junghwan Lee, Jonghyeok Lee, Yao Xie

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02357v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02357v1)

**Summary:** Recent advances in deep learning for time series prediction have amplified the need for reliable uncertainty quantification. Conformal prediction has gained attention as a distribution-free framework for constructing prediction intervals with coverage guarantees. However, its coverage guarantees rely on data exchangeability, an assumption generally violated in time series. Active research has focused on developing conformal prediction methods for time series that overcome this limitation. While ...

---

### 27. FERPO: Forward Entropy-Regularized Policy Optimization

**Authors:** Sebastian Sanokowski, Alireza Sarmadi, Majid Khadiv

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02198v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02198v1)

**Summary:** Several state-of-the-art methods for online reinforcement learning in continuous control improve policies using action gradients of a learned critic. However, critics are typically trained to predict returns, and accurate value predictions do not necessarily yield accurate action derivatives, potentially leading to unreliable policy updates. We propose Forward Entropy-Regularized Policy Optimization (FERPO), an on-policy maximum entropy reinforcement learning algorithm that performs policy impro...

---

### 28. Muon meets Tamed Langevin: Momentum Preconditioning beyond Convex and gradient-Lipschitz Potentials

**Authors:** Nikolaos Makras, Sotirios Sabanis

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02158v1)

**Summary:** We consider the problem of sampling from Gibbs distributions on matrix spaces whose potential energies are neither convex nor globally gradient-Lipschitz. We introduce a family of non-quadratic kinetic energies that lead to a new underdamped Langevin system with momentum preconditioning, in which the gradient of the kinetic energy acts as a smooth spectral taming of the momentum. We prove that, under these relaxed assumptions on the potential, the resulting dynamics leaves the target Gibbs measu...

---

### 29. Sample complexity bounds for categorical Markov random fields via Discrete Diffusions

**Authors:** Shivam Kumar, Nabarun Deb

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02128v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02128v1)

**Summary:** Many applications in statistics, economics, and physics require sampling from high-dimensional categorical distributions with local dependence structures. Examples include finite memory language models, Ising and Potts systems in statistical physics and protein folding, etc. In modern machine learning, discrete diffusions have emerged as a flexible approach for sampling such data, with strong empirical performance. Motivated by this, we develop learning methods with end-to-end sample complexity ...

---

### 30. Wasserstein Gradient Flows and Forward-Only Diffusion Are Not Enough for Multimodal Sampling

**Authors:** Daniel McBride, Pratik Khandagale, Cristina Garcia-Cardona, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02081v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02081v1)

**Summary:** There has been a proliferation of sampling algorithms based on Wasserstein gradient flows (WGF) and forward-only diffusion processes (FODP), often accompanied by theoretical guarantees of exponentially fast convergence to the target distribution. These guarantees are frequently interpreted as evidence that such methods can efficiently sample complex multimodal distributions, often supported by empirical results. In this work, we argue that this interpretation is fundamentally misleading. By invo...

---

### 31. The Curvature of Regret in Contextual Linear Optimization

**Authors:** Konstantinos Ziliaskopoulos, Alexander Vinel, Alice E. Smith

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01980v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01980v1)

**Summary:** Decision-focused learning for linear optimization is complicated by the discontinuity of the optimizer, where small cost errors may leave the decision unchanged or move it to a different vertex. We show that this non-smooth pointwise behavior becomes locally quadratic after averaging over the data distribution, and we derive the curvature in closed form, specifically, a matrix-valued measure supported on the walls of the normal fan. This measure depends only on the feasible set, with the data di...

---

### 32. Expected Utility Regret Rule: Minimax and Bayes Optimal Portfolio Choice

**Authors:** Masahiro Kato

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02290v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02290v1)

**Summary:** This study considers the problem of portfolio choice, where we recommend a portfolio to an investor to maximize the expected utility of their wealth. Our goal is to construct an asymptotically optimal portfolio choice rule in terms of expected utility regret, the difference between the expected utility of an oracle investor and that achieved by a portfolio chosen from data. We propose the Expected Utility Regret (EUR) rule, which jointly selects a portfolio class and estimates its weights. In a ...

---

### 33. Sharp Non-Asymptotic Analysis of the Penalized Challenger in $β$-EB-TCI for Bernoulli Bandits

**Authors:** Nam Nguyen, Tuan Quang Dam

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01951v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01951v1)

**Summary:** Top-two algorithms are simple and effective for fixed-confidence best-arm identification, but their sharp non-asymptotic behavior is still not well understood. We study this problem for Bernoulli bandits through $β$-EB-TCI, the empirical-best top-two rule of Jourdan et al., whose challenger is chosen using a Bernoulli transportation cost with a logarithmic count penalty. We prove that, after the empirical leader has become the true best arm and its sampling fraction stays close to $β$, the stopp...

---

### 34. Pragmatic DML with AI-Learned Representations

**Authors:** Andres Aradillas Fernandez, Victor Chernozhukov, Carlos Cinelli, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01935v2) | 📄 [PDF](https://arxiv.org/pdf/2610.01935v2)

**Summary:** Text, images, and other rich covariates are increasingly compressed into AI-learned representations and then used as controls in causal analysis. We study when this approach is valid and develop a practical framework for causal inference with learned representations. For a broad class of estimands, an imperfect representation distorts the target causal parameter by the product of two representation errors: one in the outcome regression and one in the balancing weight (or Riesz representer). This...

---

### 35. Error-Corrected Inference-Time Scaling for Imperfect Diffusion Models

**Authors:** Zuokai Wen, Louis Grenioux, Weinan E, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01933v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01933v1)

**Summary:** Inference-time scaling adapts pretrained diffusion models to new sampling tasks without additional training. Existing methods rely primarily on Monte Carlo sampling with more particles, yet are premised on the pretrained model being exact. In practice, data and training limitations make the model imperfect, and these methods inherit its error. More particles reduce Monte Carlo error but cannot remove the mismatch between the endpoint and the desired target or the error in tracking the prescribed...

---

### 36. Generalized Engression Models

**Authors:** Xinwei Shen, Zijian Guo, Francis Bach

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01823v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01823v1)

**Summary:** We consider estimating the conditional distribution of a multivariate outcome given covariates when its coordinates may be continuous, binary, categorical, ordinal or rankings, and are conditionally dependent on one another. Different statistical methods have been developed for each outcome type, and most of them target a summary of the conditional distribution, such as the mean of each coordinate, rather than the joint distribution of the outcome vector. We develop generalized engression models...

---

### 37. Inferring Multi-Timescale Neural Dynamics with Switching Linear Dynamical Systems

**Authors:** Lulu Gong, Yongxu Zhang, Shreya Saxena

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01786v1)

**Summary:** Neural activity often exhibits multiple timescales that can vary with behavioral states and task conditions. Identifying these timescales from neural recordings is important for better understanding neural computation and function. However, traditional approaches based on autocorrelation fitting are difficult to scale to high-dimensional population recordings and can become unreliable when neural dynamics change with behavior. State-space models have been a powerful framework for modeling high-d...

---

### 38. In-context Learning of Single-index Targets: Comparing Kernel and Feature Learners

**Authors:** Haotian Gu, Yizhou Xu, Lenka Zdeborová

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01712v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01712v1)

**Summary:** In-context learning (ICL) enables a pretrained model to infer a task from demonstrations without updating its parameters. While much of the existing theory focuses on linear target functions, in this paper we study nonlinear cases by comparing two one-layer attention architectures on the same family of single-index tasks. A kernel learner first maps inputs through a fixed nonlinear feature map and then applies linear attention, whereas a feature learner applies attention to the original input, f...

---

### 39. Lower Bounds for Stochastic First-Order Algorithms with Variance Reduction in Nonconvex--Concave Minimax Optimization

**Authors:** Jiayi Song, Zi Xu

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01662v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01662v1)

**Summary:** We establish complexity lower bounds for stochastic first-order algorithms in nonconvex--concave minimax optimization, allowing algorithms to use variance reduction. Our main contribution is a lower bound for a zero-respecting algorithm class that permits variance reduction, extending beyond the algorithmic restrictions imposed by some existing lower bounds. We consider objectives with an $L$-Lipschitz continuous joint gradient, a compact convex dual domain of Euclidean radius at most $D_Y$, and...

---

### 40. The hidden advantage of mask resampling: a theory of masked autoencoders

**Authors:** Jorge Medina Moreira, Lorenzo Bardone, Lenka Zdeborová

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01578v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01578v1)

**Summary:** Why can masked prediction learn useful representations that unmasked reconstruction misses? We study this question in a high-dimensional model of a masked autoencoder (MAE) trained on data with shared latent structure and heterogeneous noise. We prove that masked linear reconstruction can recover the latent feature at linear sample complexity in regimes where unmasked linear reconstruction, equivalent to PCA, fails. The analysis also quantifies the statistical advantage of mask resampling, an es...

---

### 41. Exact Distinguishability in Non-Markovian Decision Processes

**Authors:** Kabir Murjani, Nisarg Patel

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01527v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01527v1)

**Summary:** Non-Markovian environments are often modeled as Regular Decision Processes (RDPs), where dynamics depend on the interaction history through a finite automaton. Existing offline guarantees for RDPs rely on a distinguishability assumption on the behaviour policy but provide no means of verifying it. When the assumption is violated, distinct models may explain the data equally well. We study when data collected under a fixed behaviour policy can distinguish two candidate RDPs. We prove that the pos...

---

### 42. Langevin-Informed Transfer Learning: Replacing Target Samples by Black-Box Feedback

**Authors:** Vladimir R. Kostic, Karim Lounici, Hélène Halconruy, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01522v1)

**Summary:** Many scientific and machine learning systems, from molecular dynamics to diffusion models and beyond, are governed by stochastic dynamics with low-dimensional structure, evolving on slow timescales. However, target trajectories, used to identify and interpret such dynamics, are often inaccessible: only biased or static samples that explore the underlying manifold are available. We introduce Langevin-Informed Transfer Learning (LITL), a framework for recovering target Langevin dynamics from biase...

---

### 43. No Model Required: Text Entropy Rate Filtering Mitigates Iterative Fine-Tuning Collapse

**Authors:** Lewis Mitchell

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01493v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01493v1)

**Summary:** Iterative fine-tuning on synthetic data causes \emph{model collapse}: output diversity narrows as rare patterns are progressively lost, a signature most visible as phrase-level repetition. Existing mitigations either require model log-probabilities, an external oracle, or continued access to real human data. Here we develop a new approach grounded in mathematical information theory: the non-parametric Kontoyiannis entropy rate estimator $h_k$, computed entirely from raw text via match-length sta...

---

### 44. Zero Flux: Flow-Based Comparison of High-Dimensional Discrete Distributions

**Authors:** Leyang Wang, Yakun Wang, Song Liu, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01472v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01472v1)

**Summary:** Comparing two high-dimensional discrete distributions has always been a challenging task due to the exponentially growing state space and complex changes in interactions. A recent work suggests comparing distributions through a vector field trained using flow matching between two continuous distributions. The resulting vector field at mid-point vanishes if and only if two distributions identical. However, such a flow-based criterion does not naturally apply to discrete distributions. We extend t...

---

### 45. Tight Transition Time Bounds for Separable Logistic Regression at the Edge of Stability

**Authors:** Haodong Wen, Kaiyue Wen, Jiaye Teng

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01459v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01459v1)

**Summary:** We study logistic regression on linearly separable data under gradient descent with a large constant stepsize $η$. Such dynamics may exhibit a characteristic Edge of Stability phenomenon, in which the loss initially oscillates before transitioning to a stable phase of monotone decrease. Existing work provides a tight $Θ(1)$ bound in dimension $d=2$ as $η\to \infty$ and conjectures a bound independent of $η$ in arbitrary dimensions $d\geq 2$. In this paper, we disprove this conjecture by showing ...

---

### 46. On skew-symmetric distributions and their use in Monte Carlo sampling algorithms: coordinate-free, Gibbs-style and manifold versions of the Barker proposal

**Authors:** Minh Vu, Samuel Livingstone, Pantelis Samartsidis

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01448v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01448v1)

**Summary:** Skew-symmetric probability distributions provide a principled mechanism for incorporating gradient information into Markov chain Monte Carlo algorithms. Here we review the (preconditioned) Barker proposal, a Metropolis--Hastings algorithm built on skew-symmetric distributions, and motivate its design. We then introduce three natural extensions. First, we propose coordinate-free variants of the Barker algorithm. Second, we introduce a Gibbs-style Barker algorithm that re-evaluates the gradient at...

---

### 47. Optimal Transport Meets Reinforcement Learning: A Survey

**Authors:** Yujie Zhu, Charles A. Hepburn, Matthew Thorpe, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01413v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01413v1)

**Summary:** Reinforcement learning (RL) algorithms frequently compare probability distributions, such as state visitation distributions induced by policies and experts, action distributions from learned policies and offline datasets, or transition distributions from learned models and environments. However, commonly used divergences may become ineffective when these distributions overlap weakly, which is frequently encountered in imitation learning, offline RL, and deployment under distribution shift. Optim...

---

### 48. Clifford Sheaf Neural Networks

**Authors:** Kotaro Kamiya, Joel Nicholls

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01322v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01322v1)

**Summary:** We introduce the Clifford Sheaf Neural Network (CSNN), an equivariant sheaf neural network for geometric graphs that places a Clifford algebra on each stalk of a cellular sheaf and transports multivector features along edges. The canonical choice of restriction map for sheaves with algebra-valued stalks is algebra homomorphism. Adding the constraint of equivariance, the naive choice becomes versor conjugation. However, versor conjugation is expressively weak, so we drop algebra homomorphism and ...

---

### 49. IQS-BO: In-Context Query Selection for Bayesian Optimisation

**Authors:** Luca Geminiani, Nadja Klein

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01269v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01269v1)

**Summary:** Bayesian Optimisation (BO) is a powerful framework for the optimisation of expensive black-box functions, but typically requires refitting a surrogate and maximising an acquisition function at every evaluation step. In-context approaches based on Prior-data Fitted Networks (PFNs) amortise part of this cost by pre-training transformers on functions drawn from synthetic priors. PFNs4BO amortises the surrogate but still relies on a numerically maximised acquisition function, while FIBO performs BO ...

---

### 50. Counterfactual Generation via Flow Matching: Coupling-Sensitive End-to-End Rates

**Authors:** Yunrui Guan, Krishnakumar Balasubramanian, Shiva Prasad Kasiviswanathan

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01193v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01193v1)

**Summary:** Counterfactual generation seeks to sample outcomes under a hypothetical intervention or decision using observational data collected under the factual assignment mechanism. We develop a flow-matching approach that combines a sample-split, doubly robust training objective with a learned coupling between observed source outcomes and target outcomes drawn from a fitted conditional outcome model. To enable finite-step generation, we leverage a score-corrected stochastic sampler based on a Gaussian-sm...

---

