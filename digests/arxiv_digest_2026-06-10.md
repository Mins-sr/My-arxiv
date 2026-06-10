# arXiv Daily Digest - 2026-06-10

Total papers: 350

---

## cs.AI

**50 papers**

### 1. A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

**Authors:** Tong Xie, Yuanhao Ban, Yunqi Hong, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11189v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11189v1)

**Summary:** Supervised fine-tuning (SFT) typically maximizes the likelihood of every token in a demonstrated trajectory. However, an observed token can be non-unique, noisy, or misaligned with the model prior. Strictly fitting toward this one-hot target may be suboptimal, especially when the pretrained model encodes a rich knowledge prior. In this work, we reinterpret SFT as target distribution design: instead of studying only the loss objective, we analyze the token-level target that the loss drives the mo...

---

### 2. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents

**Authors:** Weixian Xu, Shilong Liu, Mengdi Wang

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11182v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11182v1)

**Summary:** In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applicability. To mitigate cross-dataset interference, EEVEE introduces a router that p...

---

### 3. The Role of Feedback Alignment in Self-Distillation

**Authors:** Semih Kara, Oğuzhan Ersoy

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11173v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11173v1)

**Summary:** Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this contex...

---

### 4. Piper: A Programmable Distributed Training System

**Authors:** Megan Frisella, Shubham Tiwari, Andy Ruan, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11169v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11169v1)

**Summary:** Large-scale model training increasingly relies on composing multiple parallelism strategies, such as data, pipeline, and expert parallelism, together with memory-saving optimizations like ZeRO. Deployed systems for foundation model pretraining often rely on human experts to manually design a high-level parallelism strategy then implement the corresponding low-level execution strategy, making it difficult to adapt the system to new strategies. Meanwhile, many general-purpose frameworks are more f...

---

### 5. Flaws in the LLM Automation Narrative

**Authors:** George Perrett, Javae Elliott, Jennifer Hill, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11166v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11166v1)

**Summary:** Large Language Models (LLMs) are increasingly described as performing at the level of human experts on knowledge economy tasks. These claims are primarily based on how LLMs perform on benchmarking tasks that measure average performance across standardized datasets. Primary limitations of many benchmarking tasks are that they often measure performance based on content directly included in LLM training data, and they frequently do not assess the reliability of LLM performance or the magnitude of L...

---

### 6. ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models

**Authors:** Wenhao Liu, Hao Shi, Yunhe Li, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11164v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11164v1)

**Summary:** Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth. Current decoding-time compression methods mitigate this issue via token eviction, but typically assume a uniform budget distribution across all layers and heads. In contrast, existing non-uniform budget allocation methods are predominantly designed for the static prompt prefill phase, and they do not capture the stepwise context demands of ...

---

### 7. ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity

**Authors:** Andrew Bo Liu, Samira Nedungadi, Bryce Cai, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11150v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11150v1)

**Summary:** Large language models (LLMs) are rapidly acquiring capabilities relevant to biological research, from literature synthesis to interpretation of experimental data. Increasingly, LLM agents can also perform in silico biology tasks that previously required experienced human biologists. These emerging AI capabilities offer new opportunities for scientific discovery and biomedical advances, but they also shift the landscape of biosecurity risks. To address this, we introduce the Agentic Bio-Capabilit...

---

### 8. Data assimilation for subsurface flow using latent diffusion model parameterization: performance of ensemble-Kalman and Monte Carlo techniques

**Authors:** Guido Di Federico, Wenchao Teng, Louis J. Durlofsky

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11140v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11140v1)

**Summary:** Data assimilation (DA) in subsurface flow entails calibrating model parameters to match observed data, typically at wells, while preserving geological realism. Latent diffusion models (LDMs) provide efficient mappings from high-dimensional geological model space to a low-dimensional latent variable, reducing the dimensionality of the inverse problem while maintaining plausibility in posterior geomodels. However, the high nonlinearity in the LDM mapping may degrade the performance of Kalman-gain-...

---

### 9. Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation

**Authors:** Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11127v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11127v1)

**Summary:** Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence that induced each generation, and whether rejected samples can be systematically recovered rather than permanently discarded. We present a controlled study of both questions across gate configurations, recovery strategies, and generator scales, using adversarially injected ...

---

### 10. Monte Carlo Pass Search: Using Trajectory Generation for 3D Counterfactual Pass Evaluation in Football

**Authors:** Andrew Kang, Priya Narasimhan

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11120v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11120v1)

**Summary:** We recast pass evaluation in football (soccer) as a Monte Carlo Tree Search (MCTS)-like evaluation problem whose components mostly exist in the literature under different names: a value model (possession value), a world model (multi-agent trajectories with ball interactions), and a policy over counterfactual actions (sampling pass variants with noise). Building on the first public high-fidelity tracking dataset with 3D ball trajectories from the Bundesliga, we introduce Monte Carlo Pass Search (...

---

### 11. TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning

**Authors:** Heming Zou, Qi Wang, Yun Qu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11119v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11119v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. Past efforts have focused on allocating available rollout resources ...

---

### 12. Towards Autonomous Accelerator Design: FPGA Accelerator Generation with SECDA

**Authors:** Vinamra Sharma, Xingjian Fu, Jude Haris, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11117v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11117v1)

**Summary:** Designing FPGA-based accelerators for modern artificial intelligence workloads requires exploring a large and complex hardware design space that involves architectural parameters, data flow strategies, and memory hierarchies, making the process very time consuming. While existing methodologies such as SECDA enable rapid hardware-software co-design through SystemC simulation and FPGA execution, identifying efficient accelerator configurations remains a largely manual process requiring extensive d...

---

### 13. Designed by Journalists, but Is It for Readers? Rethinking AI Disclosures and Transparency in News

**Authors:** Pooja Prajod

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11116v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11116v1)

**Summary:** As newsrooms integrate generative AI, journalists face a disclosure challenge: how to communicate AI involvement in ways that maintain reader trust. Current practice offers two approaches: brief one-line labels or detailed disclosures specifying human oversight, editorial accountability, and error reporting mechanisms. Neither achieves journalists' goal of building trust through transparency. An existing controlled experiment with 34 news readers show that detailed disclosures trigger a \textit{...

---

### 14. FADA: Accessible fetal ultrasound interpretation and annotation with a selectively distilled unified vision-language model

**Authors:** Mahmood Alzubaidi, Uzair Shah, Raden Muaz, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11106v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11106v1)

**Summary:** A global shortage of trained sonographers limits prenatal ultrasound screening in low- and middle-income countries, where over half of pregnant women receive no skilled sonography. Current deep learning approaches address detection, segmentation, or classification in isolation, each demanding a separate model and expert-specified labels at inference. We present FADA, a unified vision-language model built on Qwen3.5-VL that performs clinical interpretation, classification, detection, and segmenta...

---

### 15. PhantomBench: Benchmarking the Non-existential Threat of Language Models

**Authors:** Haeji Jung, Hila Gonen

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11105v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11105v1)

**Summary:** Hallucinations, where language models (LMs) generate factually ungrounded responses, pose serious risks, as users tend to blindly rely on them. This is particularly concerning in high-stakes domains, where consequences of such model behavior can lead to significant harms. Despite notable progress in understanding hallucinations, it remains unclear how reliably these models can recognize the limits of their knowledge. We introduce PhantomBench, the first large-scale benchmark of its kind, compris...

---

### 16. RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning

**Authors:** Yichao Zhong, Yidan Lu, Yuhang Lu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11092v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11092v1)

**Summary:** Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven RL struggles to explore and discover valid kicks from scratch. We therefore introduce RoboNaldo, a three-stage motion-guided curriculum RL framewo...

---

### 17. Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning

**Authors:** Zhiyuan Zhou, Andy Peng, Charles Xu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11087v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11087v1)

**Summary:** Expressive continuous control policies, such as diffusion and flow models, form the backbone of recent advances in scaling imitation learning for simulated and real robot control. While they are known to scale stably in the supervised imitation learning setting, incorporating them into reinforcement learning (RL) pipelines for policy improvement has proven more difficult. It often requires specialized training objectives or backpropagating through denoising processes, which cause well-known issu...

---

### 18. Unifying Local Communications and Local Updates for LLM Pretraining

**Authors:** Pietro Cagnasso, Eugene Belilovsky, Edouard Oyallon

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11081v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11081v1)

**Summary:** Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links. Many practical methods reduce communication frequency but still rely on synchronous All-Reduce operations that maintain identical model states and tie progress to global collectives. This can become a bottleneck when bandwidth or worker speed is heterogeneous. We introduce GASLoC, a novel decentralized pre-training algorithm tha...

---

### 19. A History-Aware Visually Grounded Critic for Computer Use Agents

**Authors:** Jaewoo Lee, Zaid Khan, Archiki Prasad, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11078v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11078v1)

**Summary:** Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pre-execution action evaluation in complex Graphical User Interface (GUI) environments. However, existing critics suffer from two key limitations: they (1) focus primarily on short-sighted decision loops (e.g., forgetting earlier actions) and (2) lack the visual grounding needed to detect flawed actions (e.g., clicking wrong UI elements). To address these, w...

---

### 20. Modeling Complex Behaviors: Multi-Personality Composition and Dynamic Switching in Vision-Language Models

**Authors:** Peiqi Jia, Haonan Jia, Ziqi Miao, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11074v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11074v1)

**Summary:** With the widespread deployment of Multimodal Large Language Models (MLLMs) in social interaction, understanding and controlling their behavior under complex personality conditions is essential. This paper introduces explicit personality conditioning and establishes a systematic evaluation framework encompassing single-personality induction, multi-personality induction, and personality switching. Experiments show that personality induction improves image captioning performance but can impair perf...

---

### 21. T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains

**Authors:** Genta Indra Winata, Amartya Chakraborty, Yuzhen Lin, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11070v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11070v1)

**Summary:** Recent advances in reasoning and tool-calling capabilities of large language models (LLMs) have enabled increasingly capable agentic systems. However, existing benchmarks remain limited in task complexity, realism, and domain diversity, and often fail to capture interactions that span multiple domains, limiting their ability to evaluate agents in realistic multi-step settings that require sustained reasoning and coordination. To address these limitations, we introduce T1-Bench, a high-fidelity, ...

---

### 22. CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs

**Authors:** Joachim Schaeffer, Thomas Jiralerspong, Alexander Panfilov, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11063v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11063v1)

**Summary:** AI control protocols oversee untrusted models by monitoring their actions and modifying potentially unsafe steps, often using a trusted model. This partially tampers with the untrusted model's trajectory. If the trusted model detects such an intervention, it may infer properties of the monitor and adapt to evade control. We introduce \textbf{CIAware-Bench}, a benchmark for measuring \textbf{c}ontrol \textbf{i}ntervention (CI) awareness across frontier models. CIAware-Bench tests whether models c...

---

### 23. What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents

**Authors:** Martin Andres Bertran, Aaron Roth, Zhiwei Steven Wu

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11045v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11045v1)

**Summary:** Reusing a held-out benchmark adaptively should, in principle, invite overfitting. Yet benchmark-driven machine learning (ML) has produced surprisingly little overfitting in practice. An attractive hypothesis is that successful ML strategies are highly compressible. We study this in the setting of LLM-driven research agents, where the hypothesis becomes directly testable via two complementary information bottlenecks. In \emph{output compression}, an exploration agent adaptively searches for high-...

---

### 24. Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic tasks in Real-World Professional Fields

**Authors:** Liya Zhu, Jingzhe Ding, Jian Zhang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11042v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11042v1)

**Summary:** Recent years have witnessed the rapid evolution of AI agents toward handling increasingly complex, real-world tasks. However, existing benchmarks rarely evaluate whether agents can operate graphical user interfaces to complete long-horizon, high-value professional workflows across diverse domains. Current GUI benchmarks still predominantly focus on general-purpose software, relatively simple applications, and short-horizon tasks, leaving it largely unknown whether modern agents can follow user i...

---

### 25. AuRA: Internalizing Audio Understanding into LLMs as LoRA

**Authors:** Bo Cheng, Lei Shi, Zhanyu Ma, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11033v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11033v1)

**Summary:** Recent efforts to extend large language models (LLMs) to speech inputs typically rely on cascaded ASR-LLM pipelines, end-to-end speech-language models, or bridge/distillation-based adaptation. While these routes respectively reuse strong pretrained components, enable native speech-language interaction, or offer lightweight adaptation, they often suffer from transcript-interface latency, costly multimodal training, or sequential speech-language coupling. To address these limitations, we present A...

---

### 26. Diffusion Forcing Planner: History-Annealed Planning with Time-Dependent Guidance for Autonomous Driving

**Authors:** Zehan Zhang, Neng Zhang, Yaoyi Li, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11019v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11019v1)

**Summary:** Learning-based motion planners, despite recent progress, often suffer from temporal inconsistency. Small perturbations across frames can accumulate into unstable trajectories, degrading comfort and safety in closed-loop driving. Several methods attempt to inject history as a static conditioning signal to stabilize outputs, only to induce the planner to copy historical patterns instead of adapting to environment contexts. To address this limitation, we propose Diffusion Forcing Planner (DFP), a d...

---

### 27. Superficial Beliefs in LLM Decision-Making

**Authors:** Gabriel Freedman, Francesca Toni

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11016v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11016v1)

**Summary:** We ask whether large language models (LLMs) merely imitate rationales when choosing between two options, or whether their choices reflect a systematic underlying decision structure. Using synthetic binary decision settings in which models choose between profiles defined by graded attributes, we compare the attribute a model says mattered most with the attribute that best explains its choice under a behavioural model fit to prior decisions. The behavioural model predicts held-out choices well, sh...

---

### 28. Structure from Reasoning, Numbers from Search: On-Premise Open LLMs as Structural Priors for Coupled MIMO Controller Tuning

**Authors:** Jiaxuan Chen, Haonan Li, Yang Shu

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11015v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11015v1)

**Summary:** Tuning controllers for strongly coupled multi-input multi-output (MIMO) industrial processes is hard: decentralized classical auto-tuning ignores loop interaction, and local numerical optimization from natural initializations stalls in the resulting non-convex cost landscape. We ask whether on-premise open-source large language models (LLMs), which keep data on-site and need no plant model, can help. On a single-loop CSTR, classical relay-feedback tuning (IAE 0.106, near the 0.102 optimum) beats...

---

### 29. Understanding and mitigating the risks of OpenClaw for non-technical users: A practical guide with Skill

**Authors:** Junchang Zheng, Junfeng Tan, Jialiang Lin

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11007v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11007v1)

**Summary:** OpenClaw has rapidly emerged as a transformative artificial intelligence (AI) agent framework, and its ability to autonomously execute complex, multi-step tasks has attracted an ever-growing and diverse user base. However, this capability comes with significant risks. While existing research has made important strides in characterizing these threats, such work is predominantly directed at technically sophisticated audiences. It remains largely inaccessible to non-technical users. This demographi...

---

### 30. Null-Space Constrained Low-Rank Adaptation for Response-Specified Large Language Model Unlearning

**Authors:** Bocheng Ju, Jianhua Wang, Chengliang Liu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10989v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10989v1)

**Summary:** Large language model unlearning aims to suppress designated undesirable knowledge while preserving benign capabilities. Many unlearning objectives focus on suppressing undesired answers, while recent target-guided variants specify replacement behavior but still leave update locality largely unconstrained. This paper introduces \emph{Null-Space Constrained Response-Specified Unlearning} (NSRU), a projection-constrained low-rank framework for controlled LLM unlearning. NSRU uses an explicitly stru...

---

### 31. Bellman-Taylor Score Decoding for Markov Decision Processes with State-Dependent Feasible Action Sets

**Authors:** Yi Chen, Rushuai Yang, Qiang Chen, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10979v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10979v1)

**Summary:** Many Markov decision processes (MDPs) in operations research have feasible actions that are state dependent and defined implicitly by various operational constraints. These features make it difficult to use standard deep reinforcement learning (DRL) algorithms, whose action interfaces typically assume either a fixed finite action catalog or a simple Euclidean space. Motivated by a Taylor expansion of the optimal action-value function, we propose Bellman--Taylor score decoding, a framework that m...

---

### 32. Optimizing 2D Input Representations and Sub-phase Fusion Strategies for Differential Diagnosis of Asthma and COPD Using CNN- and GRU-Based Networks

**Authors:** Ipek Sen, Ozgur Ozdemir, Elena Battini Sonmez

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10972v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10972v1)

**Summary:** This study aims to explore the performance of the VAR model in comparison with mel-frequency cepstral coefficient (MFCC) matrices and log-mel spectrograms using deep learning. In pulmonary sound classification, spectrogram-based representations suffer from inconsistent temporal dimensions due to varying respiratory cycle durations. Along with traditional trimming/zero-padding, adaptive-length windowing was presented to fix their temporal dimensions. Their spectral and temporal dimensions were op...

---

### 33. Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning

**Authors:** Renjie Mao, Xiangxin Zhou, Lvfang Tao, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10968v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10968v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has become standard for improving LLM reasoning. However, existing PPO-style trust-region mechanisms remain position-agnostic by enforcing uniform thresholds across all tokens independently. This pointwise treatment conflicts with autoregressive generation in two critical ways. First, uniform thresholds ignore autoregressive asymmetry. Early-stage deviations produce compounding sequence-level drift, causing static thresholds to under-regulate...

---

### 34. Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?

**Authors:** Tengchao Lv, Dongdong Zhang, Jiayu Ding, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10956v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10956v1)

**Summary:** The deployment of Large Language Model (LLM) agents for computer automation is accelerating, yet their ability to navigate complex, professional-grade productivity software is largely untested. We argue that Office automation is an ideal environment for benchmarking document-automation capability, as it requires long-horizon planning and reasoning, precise parameter configuration, and multi-application integration. To quantify this capability, we introduce an evaluation based on China's National...

---

### 35. Architect-Ant: Editable Automatic Furnishing of Architectural Floor Plans

**Authors:** Fedor Rodionov, Aleksandar Cvejic, Michael Birsak, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10953v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10953v1)

**Summary:** Furnished floor plans are fundamental to real estate visualization, interior design, and architectural workflows. However, progress in automatic furniture arrangement has been limited by the lack of real, professionally designed floor-plan datasets with object-level furniture annotations. To address this gap, we introduce AntPlan-270, a curated dataset of 270 architectural floor plans with per-room furniture bounding box annotations across ten residential room categories. Building on this datase...

---

### 36. Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models

**Authors:** Shelly Bensal, Axel Magnuson, Aparna Balagopalan, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10949v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10949v1)

**Summary:** Persistent memory systems promise to make LLMs more helpful by storing user beliefs over time. We show they also make models less correct by systematically amplifying sycophancy, wherein models prioritize agreement with users over accuracy. We conduct the first systematic evaluation of this effect, introducing MIST: a benchmark of synthetically generated multi-turn conversations where users express plausible misconceptions in scientific, medical, and moral reasoning domains. Testing across three...

---

### 37. Generative Explainability for Next-Generation Networks: LLM-Augmented XAI with Mutual Feature Interactions

**Authors:** Kiarash Rezaei, Omran Ayoub, Sebastian Troia, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10942v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10942v1)

**Summary:** As artificial intelligence and machine learning (AI/ML) models become integral to network operations, their lack of transparency poses a significant barrier to operator trust. Existing explainable artificial intelligence (XAI) techniques often fail to bridge this gap for non-specialists, producing technical outputs that are difficult to translate into actionable insights. This paper presents a framework specifically designed to address this shortcoming. It leverages a moderately sized large lang...

---

### 38. Democratising Camera Trap AI: An Open-Source Model for Detecting UK Mammals

**Authors:** Paul Fergus, Philip Stephens, Russell A. Hill, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10940v1)

**Summary:** Camera traps have become a cornerstone of biodiversity monitoring, but the artificial intelligence that turns vast quantities of images into usable ecological data is often locked behind commercial platforms or trained on fauna that does not match that of the British Isles. In an attempt to remove barriers and increase uptake, we release an open-source object detection model for 31 classes, 28 common UK mammal and bird species, plus utility classes for humans, calibration poles, and vehicles, dr...

---

### 39. Provenance Tracking in AI Compilers through the Lens of Coalgebra

**Authors:** Zilu Tian, Liying Liu

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10937v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10937v1)

**Summary:** AI compilers aggressively rewrite computation graphs through normalization, lowering, and optimization, making it difficult to track the provenance of tensors and operators across compilation. Reliable provenance is essential for attaching platform-specific postprocessing, debugging compiler behavior, and validating transformations, yet existing solutions are either invasive or ad hoc under non-injective graph rewrites.   We present a lightweight, generative approach to provenance tracking based...

---

### 40. CLP: Collocation-Length Prediction for Zero-Loss Adaptive Multi-Token Inference

**Authors:** Xuezhen Xie, Zhiqiang Zhou

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10935v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10935v1)

**Summary:** Large language model inference is bottlenecked by autoregressive decoding, where each token requires a full forward pass. Multi-token prediction (MTP) offers a promising acceleration path, but existing approaches suffer from a fundamental architectural flaw: the MTP head for the first token competes with the backbone's own language model (LM) head, leading to severe quality degradation when predictions are accepted. We identify this head-backbone competition as the root cause of repetitive and i...

---

### 41. WorldKernel: A World Model is the Coupling Kernel of Admissible Possible Worlds

**Authors:** Fabio Rovai

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10934v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10934v1)

**Summary:** A common assumption holds that enough observational and interventional data, given to a strong enough predictor, suffices. We report a failure mode that contradicts it. Across hundreds of structural causal models, on identified quantities a strong predictor and a Bayesian baseline both succeed, but on unidentified quantities (the couplings between counterfactual worlds) the predictor collapses to a point, on 28% of models to one no valid model can produce, while the truth is an admissible interv...

---

### 42. Frontier Coding Agents Use Metaprogramming to Adapt to Unfamiliar Programming Languages

**Authors:** Aman Sharma, Sushrut Thorat, Paras Chopra

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10933v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10933v1)

**Summary:** LLM-based coding agents are usually evaluated in familiar software settings: mainstream languages, common libraries, and public repositories. These benchmarks remain important, but they can hide how agents behave when the language itself is unfamiliar. We evaluate six contemporary coding agents on four esoteric programming languages using a sequential setup with file editing, local execution, and hidden-test grading. Our protocol exposes capability differences between these agents that mainstrea...

---

### 43. Recoverable but Not Stationary:Local Linear Structures in Weights and Activations

**Authors:** Irina Piontkovskaia, Sergey Nikolenko

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10929v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10929v1)

**Summary:** Task vectors, LoRA, activation steering, and random search around pretrained weights all suggest that learned behaviour can be controlled by linear directions. We ask which linear structures actually exist and on what scale. In a synthetic multitask transformer and LoRA adapters on DistilGPT-2 / GPT-2 we find strong local low-rank task-gradient structure but reject the fixed-task-plane hypothesis: static bases miss the recovery direction, and the useful basis drifts substantially within 100 step...

---

### 44. A Constrained Natural-Language Interface for Variational Multi-Physics Finite Element Simulations in FEniCS

**Authors:** Nilay Upadhyay, Wesley F. Reinhart

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10928v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10928v1)

**Summary:** Large language models can reduce the manual effort required to set up finite element simulations, but they introduce reliability risks when generated solver code lies on the critical path. We present a constrained natural-language interface for multi-physics finite element analysis in which the LLM is limited to front-end tasks: parsing prompts into structured JSON, generating Gmsh code only for non-catalog geometries, and using retry feedback for those stages. It never writes FEniCS solver temp...

---

### 45. Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution

**Authors:** Xucong Wang, Ziyu Ma, Shidong Yang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10917v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10917v1)

**Summary:** Although Large Language Model (LLM) agents have demonstrated strong performance on complex tasks, their learning is often limited by inefficient interaction feedback and static training environments, which hinder broader generalization. To address these limitations, this paper introduces Role-Agent, \textcolor{black}{a framework} that harnesses a single LLM to function concurrently as both the agent and the environment, enabling a bootstrapped co-evolution. Role-Agent comprises two synergistic c...

---

### 46. What Do Deepfake Speech Detectors Actually Hear?

**Authors:** Vojtěch Staněk, Veronika Jirmusová, Anton Firc, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10912v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10912v1)

**Summary:** Deepfake speech detectors often output a single score without explaining why an audio sample is flagged, where in the signal the evidence lies, or what cues drive the decision. We propose an audio-native explainability pipeline using Integrated Gradients on time-aligned self-supervised representations to localize decision evidence over time. We apply the proposed method to three WavLM-based detectors (AASIST, CA-MHFA, SLS) on ASVspoof 5 and manually annotate the highest-attribution regions to pr...

---

### 47. Ethical and Technical Limits of Deepfake Speech Datasets

**Authors:** Vojtěch Staněk, Eva Trnovská, Kamil Malinka, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10911v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10911v1)

**Summary:** Claims about the robustness and fairness of deepfake speech detectors are only as credible as the datasets used to train and evaluate those systems. We present a dataset-level audit of the deepfake speech landscape. We compile and analyze 39 deepfake speech datasets, examining key attributes including accessibility, documentation, demographic and language coverage, dataset scale, and the underlying bona fide speech sources. Our audit reveals two important takeaways. Firstly, fairness assessment ...

---

### 48. RAT: Reference-Augmented Training for ASV Anti-Spoofing

**Authors:** Vojtěch Staněk, Anton Firc, Jakub Reš, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10908v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10908v1)

**Summary:** We introduce a spoofing countermeasure architecture conditioned on speaker-reference recordings, but observe that it converges to a solution that effectively ignores the reference during inference. Surprisingly, training with a reference channel induces invariance that improves deepfake detection, even when the reference is absent or mismatched during inference. Based on this observation, we propose a Reference-Augmented Training (RAT) strategy. RAT yields improved detection performance compared...

---

### 49. Human-AI Teaming Through the Lens of Calibration

**Authors:** Eric Nalisnick, Chi Zhang, Sophia Qian, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10906v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10906v1)

**Summary:** We study models for human-AI teaming through the lens of statistical calibration. We assume the team consists of an AI model and human -- both of which are calibrated with respect to some partitioning of the feature space -- and expose how the calibration assumptions propagate into the teaming framework. In particular, we consider frameworks that either (i) combine human and model predictions or (ii) delegate prediction responsibility to either a human or model. We show via theoretical and empir...

---

### 50. Pose-ICL: 3D-Aware In-Context Learning for Pose-Controllable Subject Customization

**Authors:** Xuan Han, Yihao Zhao, Mingyu You

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10902v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10902v1)

**Summary:** Subject Customization is a foundational task in modern image generation. By providing a few reference images and a text prompt, users can generate images of a specific object in any desired scene. However, existing methods still struggle to achieve effective pose control for customized subjects. In practice, they often exhibit inaccurate poses or inconsistent cross-pose appearances. These limitations suggest that understanding objects in a volumetric manner remains a significant challenge for 2D...

---

## cs.CL

**50 papers**

### 1. A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

**Authors:** Tong Xie, Yuanhao Ban, Yunqi Hong, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11189v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11189v1)

**Summary:** Supervised fine-tuning (SFT) typically maximizes the likelihood of every token in a demonstrated trajectory. However, an observed token can be non-unique, noisy, or misaligned with the model prior. Strictly fitting toward this one-hot target may be suboptimal, especially when the pretrained model encodes a rich knowledge prior. In this work, we reinterpret SFT as target distribution design: instead of studying only the loss objective, we analyze the token-level target that the loss drives the mo...

---

### 2. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories

**Authors:** Kevin Qinghong Lin, Batu EI, Yuhong Shi, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11176v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11176v1)

**Summary:** Data tells stories that shape society; the data journalist's job is to turn raw information into stories non-experts can trust. A high-quality news feature takes a newsroom team weeks: hunting for context, running statistics, choosing an angle, and designing visuals. Recent agents handle individual steps well: data-science agents close the analysis loop, while design agents synthesize beautiful websites. But can an agent serve as a data journalist end to end? We introduce Data Journalist Agent (...

---

### 3. Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models

**Authors:** Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11167v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11167v1)

**Summary:** Full-duplex spoken dialogue models can listen and speak simultaneously, making them a promising architecture for natural conversation. However, current models are trained solely with supervised learning through token-level likelihood maximization, which does not directly optimize interaction-level behaviors, causing interactivity issues such as excessive silence and ill-timed turn-taking. Recent work has applied reinforcement learning (RL) to improve interactivity, but existing methods address o...

---

### 4. Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation

**Authors:** Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11127v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11127v1)

**Summary:** Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence that induced each generation, and whether rejected samples can be systematically recovered rather than permanently discarded. We present a controlled study of both questions across gate configurations, recovery strategies, and generator scales, using adversarially injected ...

---

### 5. TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning

**Authors:** Heming Zou, Qi Wang, Yun Qu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11119v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11119v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. Past efforts have focused on allocating available rollout resources ...

---

### 6. PhantomBench: Benchmarking the Non-existential Threat of Language Models

**Authors:** Haeji Jung, Hila Gonen

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11105v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11105v1)

**Summary:** Hallucinations, where language models (LMs) generate factually ungrounded responses, pose serious risks, as users tend to blindly rely on them. This is particularly concerning in high-stakes domains, where consequences of such model behavior can lead to significant harms. Despite notable progress in understanding hallucinations, it remains unclear how reliably these models can recognize the limits of their knowledge. We introduce PhantomBench, the first large-scale benchmark of its kind, compris...

---

### 7. The Shibboleth Effect: Auditing the Cross-Lingual Distributional Skew of Large Language Models

**Authors:** Hakan Mehmetcik

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11082v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11082v1)

**Summary:** This study investigates cross-lingual distributional skew (the Shibboleth Effect) in frontier large language models (LLMs) subjected to sustained adversarial conditions. We develop a multi-agent geopolitical wargame, the Cerulean Sea Crisis, a synthetic maritime territorial dispute designed to mirror the structural dynamics of Eastern Mediterranean conflicts. Six frontier models (GPT-4o, Llama-4, Mistral-Large, Gemini-3.1-Pro, Qwen3.6-Plus, and DeepSeek-R1) participate in a between-groups experi...

---

### 8. VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation

**Authors:** Yunan Lu, Ryan Shea, Yusen Zhang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11079v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11079v1)

**Summary:** Evaluation remains a critical bottleneck for interactive agent development. Existing evaluation methods often rely on static benchmarks, which fail to capture the dynamic, multi-step nature of agentic behavior and struggle to expose meaningful failure modes. While user-simulation-based evaluation offers a promising alternative, existing simulation frameworks suffer from two major limitations. First, they provide limited mechanisms for evaluating the quality and comprehensiveness of simulated int...

---

### 9. A History-Aware Visually Grounded Critic for Computer Use Agents

**Authors:** Jaewoo Lee, Zaid Khan, Archiki Prasad, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11078v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11078v1)

**Summary:** Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pre-execution action evaluation in complex Graphical User Interface (GUI) environments. However, existing critics suffer from two key limitations: they (1) focus primarily on short-sighted decision loops (e.g., forgetting earlier actions) and (2) lack the visual grounding needed to detect flawed actions (e.g., clicking wrong UI elements). To address these, w...

---

### 10. Modeling Complex Behaviors: Multi-Personality Composition and Dynamic Switching in Vision-Language Models

**Authors:** Peiqi Jia, Haonan Jia, Ziqi Miao, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11074v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11074v1)

**Summary:** With the widespread deployment of Multimodal Large Language Models (MLLMs) in social interaction, understanding and controlling their behavior under complex personality conditions is essential. This paper introduces explicit personality conditioning and establishes a systematic evaluation framework encompassing single-personality induction, multi-personality induction, and personality switching. Experiments show that personality induction improves image captioning performance but can impair perf...

---

### 11. T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains

**Authors:** Genta Indra Winata, Amartya Chakraborty, Yuzhen Lin, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11070v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11070v1)

**Summary:** Recent advances in reasoning and tool-calling capabilities of large language models (LLMs) have enabled increasingly capable agentic systems. However, existing benchmarks remain limited in task complexity, realism, and domain diversity, and often fail to capture interactions that span multiple domains, limiting their ability to evaluate agents in realistic multi-step settings that require sustained reasoning and coordination. To address these limitations, we introduce T1-Bench, a high-fidelity, ...

---

### 12. Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It

**Authors:** Xinyu Zhou, Boyu Zhu, Yi Xu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11052v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11052v1)

**Summary:** Chain-of-thought (CoT) supervised fine-tuning (SFT) is widely adopted to improve reasoning ability, yet we find that it systematically degrades long-context recall in hybrid linear-attention models. Across architectures including HypeNet and Jet-Nemotron, retrieval performance on Needle-In-A-Haystack (NIAH) deteriorates substantially after CoT-SFT, and the degradation becomes more severe under harder retrieval settings and longer context windows. For example, HypeNet-9B on NIAH-S2@256K decreases...

---

### 13. Does Reasoning Preserve Alignment? On the Trustworthiness of Large Reasoning Models

**Authors:** Prajakta Kini, Avinash Reddy, Souradip Chakraborty, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11046v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11046v1)

**Summary:** Instruction-tuned LLMs are increasingly converted into reasoning models through post-training to improve multi-step task performance. This conversion is usually optimized for reasoning accuracy, without explicitly preserving the alignment behavior of the instruction-tuned model, such as safe refusal, bias avoidance, and privacy protection. We ask: does this conversion preserve alignment? We study this question through a trustworthiness audit and find that it is not behavior-preserving by default...

---

### 14. AuRA: Internalizing Audio Understanding into LLMs as LoRA

**Authors:** Bo Cheng, Lei Shi, Zhanyu Ma, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11033v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11033v1)

**Summary:** Recent efforts to extend large language models (LLMs) to speech inputs typically rely on cascaded ASR-LLM pipelines, end-to-end speech-language models, or bridge/distillation-based adaptation. While these routes respectively reuse strong pretrained components, enable native speech-language interaction, or offer lightweight adaptation, they often suffer from transcript-interface latency, costly multimodal training, or sequential speech-language coupling. To address these limitations, we present A...

---

### 15. Generative Archetype-Grounded Item Representations for Sequential Recommendation

**Authors:** Yifan Li, Jiahong Liu, Xinni Zhang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11023v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11023v1)

**Summary:** Sequential recommendation aims to predict users' next interaction with items by analyzing their historical behavior. However, the limited quality of item representations remains a critical bottleneck. While pre-trained large language models (LLMs) can provide rich semantic representations, existing approaches only rely on static encoding of fixed attributes, overlooking the crucial role of target audiences in defining item identity. Moreover, the semantic space struggles to reflect actual user b...

---

### 16. Measuring Human Value Expression in Social Media Texts: Calibrated LLM Annotation and Encoder Transfer

**Authors:** Maria Milkova, Maksim Rudnev

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11018v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11018v1)

**Summary:** Measuring subjective constructs in naturally occurring social media text requires annotation procedures that are theoretically grounded, empirically validated, and transferable to an encoder model for scalable prediction. Using non-English social media posts annotated according to Schwartz's theory of basic human values, we investigate how different LLMs, prompts, and instruction languages operationalize the expression of values in text. We argue that although texts may permit multiple plausible...

---

### 17. Who Brought Easter Eggs to Eid? Auditing Cultural Translation of Math Word Problems Across Diverse Languages and Regions

**Authors:** Parisa Suchdev, Juniper Lovato

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11009v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11009v1)

**Summary:** Large language models are increasingly used to adapt math word problems for personalized learning at scale, but it remains an open question whether those adaptations are consistent across models, preserve cultural diversity at scale, and reveal which cultural entities models treat as most salient. We analyze how Claude Opus 4, GPT-4.1, and Gemini 2.5 Pro adapt 60 English math word problems into Bengali, Hindi, Punjabi (India), Urdu, Sindhi (Pakistan), Italian, and Sicilian (Italy), a language se...

---

### 18. Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?

**Authors:** Tengchao Lv, Dongdong Zhang, Jiayu Ding, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10956v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10956v1)

**Summary:** The deployment of Large Language Model (LLM) agents for computer automation is accelerating, yet their ability to navigate complex, professional-grade productivity software is largely untested. We argue that Office automation is an ideal environment for benchmarking document-automation capability, as it requires long-horizon planning and reasoning, precise parameter configuration, and multi-application integration. To quantify this capability, we introduce an evaluation based on China's National...

---

### 19. It Takes One to Bias Them All: Breaking Bad with One-Shot GRPO

**Authors:** Naihao Deng, Yilun Zhu, Naichen Shi, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10931v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10931v1)

**Summary:** Warning: This paper contains several toxic and offensive statements.   Modern large language models (LLMs) are typically aligned through large-scale post-training to ensure fair and reliable behavior. In this work, we investigate how easily such guardrails can be broken by Group Relative Policy Optimization (GRPO). We show that one-shot GRPO training on a single biased example is sufficient to induce systematic bias, with stereotype-driven reasoning generalizing across attributes, categories, an...

---

### 20. Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering

**Authors:** Xiangjun Zai, Xingyu Tan, Chen Chen, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10921v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10921v1)

**Summary:** Long-document question answering (QA) requires large language models (LLMs) to reason over evidence scattered across lengthy documents, where answers often depend on event order, section-level context, and cross-part evidence connections. Although retrieval-augmented generation (RAG) reduces the input context by retrieving relevant evidence, existing structured RAG methods still face three limitations: costly query-agnostic knowledge organization, insufficient use of original document structure,...

---

### 21. Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation

**Authors:** Yupu Hao, Zhuoran Jin, Huanxuan Liao, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10875v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10875v1)

**Summary:** Large language models (LLMs) rely on tool use to act as autonomous agents, yet often fail in multi-step execution due to insufficient tool-related knowledge and ineffective knowledge activation. Therefore, we present a systematic study on how knowledge influences tool-use performance, covering the stages of knowledge acquisition, activation, and internalization. In the knowledge acquisition stage, we acquire and evaluate various forms of experiential knowledge, and our analysis shows that simple...

---

### 22. Training LLMs to Enforce Multi-Level Instruction Hierarchies via Gravity-Weighted Direct Preference Optimization

**Authors:** Lena S. Bolliger, Lena A. Jäger

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10860v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10860v1)

**Summary:** Production LLMs receive instructions from sources with very different levels of trust, yet attend to every token with uniform architectural privilege. This is the structural vulnerability that enables malicious prompt injections and, more broadly, leaves models without a principled way to resolve conflicts between legitimate but competing instructions. A common training-based response is to teach models an explicit instruction hierarchy; existing approaches, however, formalize hierarchies of onl...

---

### 23. Janus: A Benchmark for Goal-Conditioned Information Distortion in LLMs

**Authors:** Polydoros Giannouris, Mohsinul Kabir, Sophia Ananiadou

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10852v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10852v1)

**Summary:** LLM deception is often evaluated through direct markers such as fabricated claims, explicit lies, or strategic concealment. However, many real-world misleading communications do not depend on false statements, rather, they arise from selective treatment of true material facts: omitting adverse evidence, softening unfavorable details, emphasizing favorable details, or replacing precise qualifications with vague language. Existing benchmarks largely miss this subtler and arguably more dangerous fa...

---

### 24. ConvMemory v2: A Recall-Preserving Top-10 Evidence Reranker for Conversational Memory Retrieval

**Authors:** Taiheng Pan

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10842v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10842v1)

**Summary:** We describe ConvMemory v2, an opt-in token-evidence reranker that sits after the lightweight ConvMemory v1 reranker and reorders only v1's protected top-10 candidate set. v2 is a fine-tuned ms-marco-MiniLM-L-6-v2 cross-encoder (22,713,601 parameters, measured from the released checkpoint) applied to the ten (query, memory) pairs that v1 has already selected; it does not change which ten memories are returned, so Recall@10 and Hit@10 are identical to v1 by construction, not by statistical coincid...

---

### 25. Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models

**Authors:** Yusuf Sahin, Ahmed Rockey Saikia, Volkan Cevher, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10829v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10829v1)

**Summary:** Masked diffusion language models can reduce inference steps by revealing multiple tokens per denoising iteration, but this parallelism is fragile: positions that are individually confident may be unsafe to commit together when their predictions are coupled. Existing training-free samplers such as Top-\(k\), Fast-dLLM, and EB-Sampler mainly control how many tokens to reveal, while often ranking candidates by token-wise scores that ignore interactions within the selected set. We propose ADAS, a tr...

---

### 26. K-Forcing: Joint Next-K-Token Decoding via Push-Forward Language Modeling

**Authors:** Zhiwei Tang, Yuanyu He, Yizheng Han, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10820v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10820v1)

**Summary:** Autoregressive (AR) language modeling is the dominant paradigm for text generation, yet its sequential token-by-token decoding makes inference memory-bound and inefficient. Existing acceleration approaches, such as speculative decoding and diffusion language models, can yield speedups under certain conditions but do not directly address high-load batch serving--the scenario most critical for industrial-scale deployment. We introduce K-Forcing, a push-forward language modeling paradigm for joint ...

---

### 27. RedAct: Redacting Agent Capability Traces for Procedural Skill Protection

**Authors:** Shuwen Xu, Zhitao He, Yi R., et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10813v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10813v1)

**Summary:** Users rely on execution traces to observe agent behavior, diagnose failures, and ensure accountability. These traces contain rich procedural detail, including tool invocations, intermediate decisions, and error-recovery logic. Yet this detail can expose private procedural skills, allowing downstream methods to recover key formulas, thresholds, and strategies without access to model weights or skill files. To quantify this risk and evaluate protection, we construct \textsc{CapTraceBench}, a bench...

---

### 28. Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use

**Authors:** Zhixin Ma, Yutong Zhou, Yongqi Li, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10803v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10803v1)

**Summary:** Multimodal Large Language Models (MLLMs) excel at utilizing digital APIs and increasingly serve as the "brain" of embodied AI, instructing robots to interact with the physical world. In such embodied settings, a central capability is the use of physical tools, which underpins MLLMs' ability to assist humans in real-world tasks. Despite the importance, MLLMs' proficiency in physical tool use remains largely unexplored. To address this gap, we introduce PhysTool-Bench, the first physical tool-use ...

---

### 29. Dep-LLM: Training-Free Depression Diagnosis via Evidence-Guided Structured Multi-factor with Reliable LLM Reasoning

**Authors:** Yiqing Lyu, Xianbing Zhao, Buzhou Tang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10796v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10796v1)

**Summary:** Automatic Depression Detection (ADD) from clinical interviews is a pivotal task in computational mental health, yet it remains challenging due to two critical obstacles: 1) difficulty in modeling complex but sparsely distributed depression clues within lengthy, multi-topic clinical interviews, leading to superficial and unreliable reasoning; 2) scarcity of labeled data due to clinical privacy, together with high cost of training and fine-tuning, limiting the deployment of supervised ADD systems....

---

### 30. Recovering the Zipfian Distribution in Unsupervised Term Discovery

**Authors:** Danel Slabbert, Simon Malan, Herman Kamper

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10781v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10781v1)

**Summary:** Unsupervised term discovery involves segmenting unlabelled speech into word- or syllable-like units and clustering these into a lexicon of candidate types. True lexicons follow a Zipfian distribution, yet the dominant centre-based clustering approach -- K-means -- produces a more uniform distribution due to an inductive bias toward spherical clusters. In this paper we revisit graph-based clustering as a bottom-up alternative, where segment embeddings are connected by pairwise similarity and part...

---

### 31. N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization

**Authors:** Xukun Zhu, Hang Yu, Peng Di, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10768v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10768v1)

**Summary:** The success of Large Language Models in mathematical reasoning relies heavily on the generation of diverse and valid solution paths during the rollout phase. However, current rollout techniques face a fundamental trade-off: token-level sampling often yields redundant trajectories that differ only in rephrasing, while embedding-level methods utilizing random noise frequently disrupt semantic consistency. To resolve this, we introduce N-GRPO, a novel exploration strategy integrated into the Group ...

---

### 32. ArabiGEE: A Hierarchical Taxonomy for Arabic Grammatical Error Explanation

**Authors:** Khaled Elhady, Omar Kallas, Nizar Habash, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10765v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10765v1)

**Summary:** We introduce ArabiGEE, the first comprehensive Arabic grammatical error explanation (GEE) taxonomy grounded in explicit error types. Unlike existing GEE approaches that treat explanation generation as free-form text, ArabiGEE organizes grammatical explanations through a hierarchical structure spanning orthographic, morphological, syntactic, and lexical dimensions. The taxonomy consists of 27 error types, 140 correction types, and 324 associated explanations. We apply ArabiGEE to manually annotat...

---

### 33. When the Chain of Thought Knows Better: Failure Modes in Multi-Turn Reasoning Models

**Authors:** Sai Kartheek Reddy Kasu, Nils Lukas, Samuele Poppi

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10740v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10740v1)

**Summary:** Failures in multi-turn reasoning models are largely invisible to terminal-score evaluation. A model can lock onto an unsafe stance early in a long dialogue, yet its final-turn refusal rate may appear indistinguishable from a robustly aligned baseline. To expose these hidden temporal dynamics, we propose a trace-level diagnostic - the CoT-Output 2x2 safety matrix. This framework labels every turn along two independent axes (internal reasoning and visible output), yielding four operationally defin...

---

### 34. Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs

**Authors:** Youssef Medhat, Junsoo Park, Ploy Thajchayapong, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10736v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10736v1)

**Summary:** Large online courses generate thousands of student questions directed at conversational AI teaching assistants, yet these interaction logs remain largely untapped as diagnostic signals. We present a pipeline that maps student questions from a conversational AI teaching assistant to curriculum topics using a few-shot text classifier, grounded in a GPT-4-extracted prerequisite knowledge graph of course concepts. Evaluated on 1,340 question events from 164 students in a graduate-level AI course, ou...

---

### 35. Pre-AF 13: An Interpretable Atrial Fibrillation Risk Score Mined from Discharge Reports

**Authors:** Olga Shakhmatova, Dmitrii Kriukov, Daniil Larionov, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10725v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10725v1)

**Summary:** Background. Atrial fibrillation (AF) is the most prevalent cardiac arrhythmia and a major determinant of prognosis. Established AF risk scores rely on factors (older age, hypertension) nearly ubiquitous among patients with cardiovascular disease (CVD), offering limited stratification in this high-risk group. Most target long-term (5-10 year) rather than medium-term prediction. We developed interpretable ML models predicting AF risk over a 24-month and entire follow-up horizon in CVD patients usi...

---

### 36. Continual LLM Upcycling: A Predictor-Gated Bank-Wise Sparsity Training Recipe for Dense-to-Sparse LLMs

**Authors:** Ruixuan Huang, Jinyuan Shi, Hantao Huang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10722v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10722v1)

**Summary:** We study dense-to-sparse continual training as a way to construct channel-sparse large language models from dense checkpoints. Starting from a Qwen2.5-8B dense backbone, we continue training at 32K context and introduce a predictor-gated sparse SwiGLU FFN in the 32K stage. For each token and layer, we use a low-rank predictor to produce FFN-channel routing logits. We then apply a bank-wise top-k rule to retain 16 channels in every 64-channel bank, yielding 4x sparsity in the FFN intermediate act...

---

### 37. Attention Expansion: Enhancing Keyphrase Extraction from Long Documents with Attention-Augmented Contextualized Embeddings

**Authors:** Roberto Martínez-Cruz, Alvaro J. López-López, José Portela

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10716v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10716v1)

**Summary:** Pre-trained language models (PLMs) have achieved strong performance in keyphrase extraction (KPE), largely due to their ability to generate rich contextualized representations. However, long-document KPE remains challenging because salient keyphrase evidence may be scattered across distant document sections that cannot be jointly captured within the limited context window of most PLMs. Although long-context large language models (LLMs) can process broader textual contexts, their computational co...

---

### 38. From Observation to Intervention: A Causal Audit of Expert Importance in Mixture-of-Experts Models

**Authors:** Leonard Engmann, Christian Medeiros Adriano, Holger Giese

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10703v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10703v1)

**Summary:** Interpretability methods routinely use population-level summary statistics over observed model behaviour to license claims about the effects of targeted interventions on specific computations; in Pearl's terms, they treat rung-1 associational evidence as if it supported rung-2 interventional conclusions, a move whose validity is rarely tested. We examine one concrete instance: the use of routing statistics in Mixture-of-Experts (MoE) pruning, where utilization rates, activation norms, and routin...

---

### 39. REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs

**Authors:** Keer Lu, Liwei Chen, Guoqing Jiang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10694v1)

**Summary:** Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons. However, due to their finite context window, LLMs cannot retain all past interactions, making long-term memory management essential for storing, updating, and retrieving historical information beyond the context limit. Although recent memory systems attempt to address this issue by storing historical information externally, existing approaches suffer from three key limitations: flat text-based ...

---

### 40. Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory

**Authors:** Suozhao Ji, Baodong Wu, Zehao Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10677v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10677v1)

**Summary:** Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for coll...

---

### 41. Multilingual Word-Level Forced Alignment with Self-Supervised Representations and Learned Dynamic Programming

**Authors:** Roy Weber, Meidan Zehavi, Rotem Rousso, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10675v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10675v1)

**Summary:** We present a method for accurate multilingual word-level forced alignment, consisting of an alignment encoder and a learned alignment decoder. The encoder integrates two representations: one from the Massively Multilingual Speech (MMS) model and another from a self-supervised phoneme boundary detector (UnSupSeg). It learns to fuse them and to estimate word-boundary probabilities over long temporal contexts. The alignment decoder is a learned dynamic programming that combines encoder outputs with...

---

### 42. Are We Evaluating Knowledge or Phrasing? Mitigating MCQA Sensitivity with ParaEval

**Authors:** João Maria Janeiro, Mathurin Videau, Andrea Caciolai, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10657v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10657v1)

**Summary:** Multiple-choice (MCQA) benchmarks are the standard for evaluating pretrained large language models, but their reliance on log-likelihood scoring makes them unreliable. Specifically, standard scores are highly sensitive to the exact phrasing (surface form) of the answers, conflating a model's familiarity with a specific phrase with its actual capability. We demonstrate this flaw using a controlled testbed of 1B-8B models trained on the same knowledge. Despite having identical knowledge, standard ...

---

### 43. Speaker Group Encoding in Self-supervised Speech Recognition Models

**Authors:** Felix Herron, Solange Rossato Alexandre Allauzen, Benoit Favre, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10654v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10654v1)

**Summary:** We investigate what self-supervised speech recognition models (S3Ms) learn about speaker groups (SGs). We examine several states of S3Ms: pretrained, finetuned on speaker identification (SID), finetuned on automatic speech recognition (ASR), and ASR-finetuned using a fairness enhancing algorithm. We find that S3Ms encode information about several speaker group categories (SGCs), including their gender, age, dialect, ethnicity, and whether they are a native speaker. We find that finetuning for SI...

---

### 44. Dynamic Linear Attention

**Authors:** Xin Wang, Hui Shen, Boyuan Zheng, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10650v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10650v1)

**Summary:** The scalability of Large Language Models (LLMs) to long contexts is fundamentally constrained by the quadratic complexity of standard attention, motivating the adoption of linear attention mechanisms with sub-quadratic cost. To improve representation capacity under long contexts, recent approaches organize memory in a multi-state manner. However, existing multi-state linear attention methods rely on fixed state merging policies that cannot adapt to dynamically varying token importance, irreversi...

---

### 45. How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs

**Authors:** Zhichen Dong, Yang Li, Yuhan Sun, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10646v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10646v1)

**Summary:** Token-level credit assignment remains a key obstacle for reinforcement learning (RL) in large language models (LLMs), where RL recipes typically treat all tokens equally, failing to distinguish decisive reasoning steps from routine formatting or fluent filler. Recent attempts leverage model-internal signals to assign finer-grained credit, but these are often point-wise heuristics that ignore the global structure of information propagation. We propose FlowTracer, an RL framework that traces answe...

---

### 46. Small Data, Big Noise: Adversarial Training for Robust Parameter-Efficient Fine-Tuning

**Authors:** Eitan Cohen, Idan Simai, Uri Shaham

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10610v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10610v1)

**Summary:** Parameter-Efficient Fine-Tuning (PEFT) has become essential for adapting foundation models to downstream NLP tasks. However, current PEFT methods often struggle with robustness to noise and performance degradation on limited training data. We propose SDBN (Small Data Big Noise), a unified framework that brings adversarial training to PEFT - a combination that remains less studied in the PEFT setting despite its complementary strengths - to enhance model robustness and generalization, outperformi...

---

### 47. Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting

**Authors:** Xinyu Li, Yuanyuan Wang, Haoxuan Li, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10607v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10607v1)

**Summary:** Causal discovery aims to uncover causal structures from observational data, which is crucial for real-world decision-making. However, different causal discovery algorithms can produce divergent results that conflict with each other, complicating the identification of accurate causal graphs. Traditional approaches rely on numerical values and statistical assumptions, often ignoring rich domain-specific information, such as feature descriptions, which could also help structure learning. While rece...

---

### 48. ParaBridge: Bridging Paralinguistic Perception and Dialogue Behavior in Speech Language Models

**Authors:** Yuxiang Wang, Qinke Ni, Shengbo Cai, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10581v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10581v1)

**Summary:** Speech carries more information than just words: a child's voice, a fearful tone, or a noisy background should all lead a sufficiently competent spoken-dialogue assistant to different replies. Current Speech Language Models (SLMs) can recognize such paralinguistic cues but often ignore them in open-ended dialogue. We observe that a simple paralinguistic instruction scaffold at the inference stage narrows this perception-behavior gap, suggesting that the relevant cues are already latent in the mo...

---

### 49. Hidden Consensus:Preference-Validity Compression in Human Feedback

**Authors:** Dorcas Chia Ern Chua, Karen Myn Hui Lee, Jia Yue Tan, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10569v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10569v1)

**Summary:** Standard RLHF pipelines often reduce heterogeneous human judgments into a single scalar reward target. We argue that this reduction can mis-measure alignment in structurally plural societies, where disagreement may reflect culturally, historically, linguistically, regionally, or normatively grounded interpretations rather than annotation noise. We call this failure Preference-Validity Compression, the collapse of multiple plural-valid response options into a single optimization target. Using Mal...

---

### 50. Benchmarking Knowledge Editing using Logical Rules

**Authors:** Tatiana Moteu Ngoli, NDah Jean Kouagou, Hamada M. Zahera, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10554v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10554v1)

**Summary:** Large Language Models (LLMs) are increasingly deployed in real-world applications that require access to up-to-date knowledge. However, retraining LLMs is computationally expensive. Therefore, knowledge editing techniques are crucial for maintaining current information and correcting erroneous assertions within pre-trained models. Current benchmarks for knowledge editing primarily focus on recalling edited facts, often neglecting their logical consequences. To address this limitation, we introdu...

---

## cs.CV

**50 papers**

### 1. ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations

**Authors:** Junke Wang, Xiao Wang, Jiacheng Pan, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11188v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11188v1)

**Summary:** This paper introduces ARM, a discrete representation-based AutoRegressive Model that unifies image understanding, generation, and editing within a next-token prediction framework. ARM is built on three efforts: first, we train a discrete semantic visual tokenizer that maps images into compact token sequences. Our tokenizer is supervised with multiple objectives that jointly promote semantic discriminability, language alignment and faithful reconstruction, thereby supporting diverse tasks in a sh...

---

### 2. Next Forcing: Causal World Modeling with Multi-Chunk Prediction

**Authors:** Gangwei Xu, Qihang Zhang, Jiaming Zhou, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11187v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11187v1)

**Summary:** Autoregressive video generation has emerged as a powerful paradigm for World Action Models (WAMs). However, existing approaches suffer from slow training convergence and limited converged accuracy, particularly at high frame rates, as the training supervision is confined to the current chunk without explicit signals about future dynamics; they also suffer from slow inference due to iterative video denoising. In this paper, we present Next Forcing, a multi-chunk prediction (MCP) framework for cau...

---

### 3. AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference

**Authors:** Hangfeng Liang, Yutao Hu, Yanhan Hu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11186v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11186v1)

**Summary:** Low-light video enhancement (LLVE) remains a challenging task due to severe information degradation under low-illumination conditions. Recent multimodal approaches have significantly improved enhancement performance by incorporating auxiliary modalities, such as event streams and infrared images. However, these methods typically assume the availability of these modalities at inference, which is often not feasible in real-world scenarios. To solve this problem, in this work, we propose AMNet, a u...

---

### 4. Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization

**Authors:** Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11180v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11180v1)

**Summary:** Diffusion-based lip synchronization models achieve strong visual quality and audio-visual alignment, but full-sequence bidirectional attention and many denoising steps make them impractical for real-time inference. We present Lip Forcing, to our knowledge the first autoregressive diffusion method for video-to-video (V2V) lip synchronization, which distills a 14B audio-conditioned bidirectional video diffusion teacher into causal students. At inference, the students generate each chunk in only tw...

---

### 5. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories

**Authors:** Kevin Qinghong Lin, Batu EI, Yuhong Shi, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11176v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11176v1)

**Summary:** Data tells stories that shape society; the data journalist's job is to turn raw information into stories non-experts can trust. A high-quality news feature takes a newsroom team weeks: hunting for context, running statistics, choosing an angle, and designing visuals. Recent agents handle individual steps well: data-science agents close the analysis loop, while design agents synthesize beautiful websites. But can an agent serve as a data journalist end to end? We introduce Data Journalist Agent (...

---

### 6. Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models

**Authors:** An Zhao, Shengyuan Zhang, Zhongjian Sun, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11155v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11155v1)

**Summary:** Flow Matching models have demonstrated strong performance across a wide range of generative tasks. However, their reliance on ODE-based iterative sampling incurs substantial computational overhead in inference, which limits their applicability in real-time scenes. While distillation is a promising solution, existing approaches largely borrow from diffusion-based score matching, often failing to exploit the intrinsic geometric structure of flows and suffering from training instability, high varia...

---

### 7. P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning

**Authors:** Yikang Yang, Zhanpeng Hu, Youtian Lin, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11152v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11152v1)

**Summary:** Multimodal large language models can write code to produce complex programs as well as use programs to do 3D modeling, which opens up a new avenue for 3D generation powered by their priors, world knowledge and reasoning. Yet existing benchmarks rarely evaluate 3D modeling through code. Such modeling demands more than runnable code: from a text or visual specification, a model must generate a parametric 3D program that is geometrically precise, semantically aligned and assembly-consistent. We int...

---

### 8. MOFA-VTON: More Fashion Possibilities with Fine-Grained Adaptations in Virtual Try-On

**Authors:** Xiaoyu Han, Chenyang Wang, Jing Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11148v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11148v1)

**Summary:** Virtual try-on aims to fit an in-shop clothing image onto a specific human body. An optimal virtual try-on method should provide diverse and flexible dressing options, accurately reflecting the varied wearing styles encountered in real-life scenarios, tailored to individual preferences and fashion aspirations. However, current methods predominantly perform a direct replacement of the original clothing with the target clothing, following the same dressing pattern. This limited control over clothi...

---

### 9. UniPET: a universal network for high-quality PET image denoising across varied dose reduction factors

**Authors:** Zhiwen Yang, Yang Zhou, Haowei Chen, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11131v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11131v1)

**Summary:** Most existing deep learning-based PET image denoising methods assume a fixed and known dose reduction factor (DRF) for low-dose PET images. However, these methods encounter significant performance degradation when the DRF varies beyond the assumed one in practical applications. To address the challenge posed by varied DRFs, several preliminary studies focus on the task of universal PET image denoising, aiming to train a universal model over low-dose data across DRFs. Nonetheless, these vanilla u...

---

### 10. WorldOlympiad: Can Your World Model Survive a Triathlon?

**Authors:** Yuke Zhao, Wangbo Zhao, Weijie Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11129v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11129v1)

**Summary:** We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity. While existing benchmarks often focus on visual quality, semantic alignment, or short-term temporal coherence, they provide limited insight into whether generated videos obey physical rules, preserve coherent 3D structure, and sustain controllable interactions over long horizons. To address this gap, WorldOlympiad decomposes world-model ev...

---

### 11. Monte Carlo Pass Search: Using Trajectory Generation for 3D Counterfactual Pass Evaluation in Football

**Authors:** Andrew Kang, Priya Narasimhan

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11120v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11120v1)

**Summary:** We recast pass evaluation in football (soccer) as a Monte Carlo Tree Search (MCTS)-like evaluation problem whose components mostly exist in the literature under different names: a value model (possession value), a world model (multi-agent trajectories with ball interactions), and a policy over counterfactual actions (sampling pass variants with noise). Building on the first public high-fidelity tracking dataset with 3D ball trajectories from the Bundesliga, we introduce Monte Carlo Pass Search (...

---

### 12. Multimodal Brain Tumour Classification Using Feature Fusion

**Authors:** Wajih ul Islam, Muhammad Yaqoob, Javed Ali Khan, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11107v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11107v1)

**Summary:** Clinicians diagnose brain tumors by synthesizing patient symptoms, medical history, and quantitative imaging data from modalities such as MRI and CT scans into a unified clinical judgement. However, most deep learning models rely on MRI/CT images alone, failing to replicate the clinicians multimodal reasoning. We explore a two-branch multimodal network combining raw MRI scans with 91 extracted radiomic features (intensity, texture, shape, and boundary descriptors) to classify brain tumors into g...

---

### 13. FADA: Accessible fetal ultrasound interpretation and annotation with a selectively distilled unified vision-language model

**Authors:** Mahmood Alzubaidi, Uzair Shah, Raden Muaz, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11106v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11106v1)

**Summary:** A global shortage of trained sonographers limits prenatal ultrasound screening in low- and middle-income countries, where over half of pregnant women receive no skilled sonography. Current deep learning approaches address detection, segmentation, or classification in isolation, each demanding a separate model and expert-specified labels at inference. We present FADA, a unified vision-language model built on Qwen3.5-VL that performs clinical interpretation, classification, detection, and segmenta...

---

### 14. IDEAL: In-DEpth ALignment Makes A Discrete Representation AutoEncoder

**Authors:** Yitong Chen, Zijie Diao, Junke Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11096v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11096v1)

**Summary:** Built on pretrained vision foundation models (VFMs), representation autoencoders (RAEs) have recently emerged as a promising approach for constructing semantically rich latent spaces for image generation. However, their reconstruction quality often remains suboptimal, largely because deep VFM representations do not preserve sufficient fine-grained visual detail. This limitation becomes even more severe after discretization, where missing low-level information is difficult to recover. In fact, we...

---

### 15. A History-Aware Visually Grounded Critic for Computer Use Agents

**Authors:** Jaewoo Lee, Zaid Khan, Archiki Prasad, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11078v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11078v1)

**Summary:** Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pre-execution action evaluation in complex Graphical User Interface (GUI) environments. However, existing critics suffer from two key limitations: they (1) focus primarily on short-sighted decision loops (e.g., forgetting earlier actions) and (2) lack the visual grounding needed to detect flawed actions (e.g., clicking wrong UI elements). To address these, w...

---

### 16. U-TTT: Towards Generalizable PET Image Denoising via Test-Time Training

**Authors:** Zhiwen Yang, Jiayin Li, Hao Lu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11032v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11032v1)

**Summary:** Existing deep learning models for Positron Emission Tomography (PET) image denoising often suffer from severe performance degradation under distribution shifts, fundamentally restricting their robust clinical deployment. This lack of generalization stems from the conventional paradigm of fixed-parameter models that cannot adapt to variations in test data (e.g., dose levels or scanner types) after training. To overcome this limitation and achieve robust generalization, we introduce U-TTT, a novel...

---

### 17. An Uncertainty Estimation Framework for Dose Accumulation in Adaptive Radiotherapy: Application to CBCT-Guided Radiotherapy for Cervical Cancer

**Authors:** Cedric Hemon, Delphine Lebret, Jean-Claude Nunes, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11012v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11012v1)

**Summary:** Background and purpose: oART enables daily plan adaptation to interfraction anatomical variations, but cumulative dose estimation remains limited by DIR, segmentation, and anatomical uncertainties. We introduce IMPACT-DoseAcc, an uncertainty-aware dose accumulation framework, within IMPACT for semantic feature-driven image analysis. The framework is modality- and disease-agnostic and is applied to CBCT-guided oART for cervical cancer (LACC).   Material and Methods: Nine LACC patients were retros...

---

### 18. IPSM-Bench: A New Intermediate Phase Segmentation Benchmark in Microstructure Images of Zinc-Based Absorbable Biomaterials

**Authors:** Jinglin Xu, Shangyan Zhao, Jiabo Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11001v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11001v1)

**Summary:** Zinc-based alloys are indispensable emerging absorbable metallic biomaterials, and their macroscopic performance is governed by microstructural characteristics. Intermediate phases-key microstructural constituents-are pivotal in regulating mechanical and functional properties. However, intermediate phase segmentation in zinc alloy microstructures faces formidable challenges: scarce annotated datasets, low contrast, difficulty detecting small targets, and heterogeneous morphologies. To this end, ...

---

### 19. AnimaSpark: A Feed-Forward Method for Animating Arbitrary 3D Objects

**Authors:** Yiming Zhao, Haoyu Sun, Aoyu Wang

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10988v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10988v1)

**Summary:** While recent advancements in generative AI have substantially accelerated static 3D model creation workflows, the synthesis of category-agnostic 3D animations remains a significant bottleneck in 3D asset production. Current methods for category-agnostic animation generation exhibit critical limitations in inference speed, motion quality, and adherence to textual prompts, thereby leaving the process dependent on labor-intensive manual artistry. To address these challenges, this paper introduces A...

---

### 20. Quo Vadis, Visual In-Context Learning? A Unified Benchmark Across Domains and Tasks

**Authors:** Pradnya Halady, Jiale Wei, Zdravko Marinov, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10967v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10967v1)

**Summary:** Visual in-context learning has been proposed as a pathway towards dynamic models that can generate predictions based on a provided context and thereby can adapt to new vision tasks at test-time. Yet, the evaluation of the adaptation capabilities of these models has been limited to narrow setups that mainly mirror tasks or image domains from pre-training for which real adaptation is not required. We address this gap by constructing a broad Visual In-Context BEnchmark (VIBE) with a focus on divers...

---

### 21. Architect-Ant: Editable Automatic Furnishing of Architectural Floor Plans

**Authors:** Fedor Rodionov, Aleksandar Cvejic, Michael Birsak, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10953v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10953v1)

**Summary:** Furnished floor plans are fundamental to real estate visualization, interior design, and architectural workflows. However, progress in automatic furniture arrangement has been limited by the lack of real, professionally designed floor-plan datasets with object-level furniture annotations. To address this gap, we introduce AntPlan-270, a curated dataset of 270 architectural floor plans with per-room furniture bounding box annotations across ten residential room categories. Building on this datase...

---

### 22. Democratising Camera Trap AI: An Open-Source Model for Detecting UK Mammals

**Authors:** Paul Fergus, Philip Stephens, Russell A. Hill, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10940v1)

**Summary:** Camera traps have become a cornerstone of biodiversity monitoring, but the artificial intelligence that turns vast quantities of images into usable ecological data is often locked behind commercial platforms or trained on fauna that does not match that of the British Isles. In an attempt to remove barriers and increase uptake, we release an open-source object detection model for 31 classes, 28 common UK mammal and bird species, plus utility classes for humans, calibration poles, and vehicles, dr...

---

### 23. PENet+: A Lightweight Residual Transformer Framework for Efficient Image Steganalysis

**Authors:** Jincheol AN, Dongsu Kim, Haneol Jang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10939v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10939v1)

**Summary:** Image steganalysis, the detection of hidden information embedded in digital images, is a core component of modern cybersecurity and digital forensics. Recent residual Transformer architectures, such as the Pixel-Difference-Convolution and Enhanced-Transformer-Network (PENet) [1], achieve strong detection accuracy, but their computational and memory demands hinder deployment in resource-constrained settings. We present PENet+, a lightweight steganalysis framework that preserves PENet's discrimina...

---

### 24. Beyond Model Size: Probing the Gaps in Visual in-Context Learning by Training a Tiny Model

**Authors:** Sunil Khatri, Steven Landgraf, Markus Ulrich, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10905v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10905v1)

**Summary:** Visual in-Context Learning (VICL) aims at making progress towards adaptive vision models, that can -- based on a few examples -- adapt to a new task at test-time. With the history of in-context learning in natural language processing research, where large, parameter-heavy models are in use, one pathway that current VICL methods take is model- and data-scaling as key ingredients. Yet, it is not clear, whether these ingredients are the key for in-context learning to take shape in vision models. To...

---

### 25. Pose-ICL: 3D-Aware In-Context Learning for Pose-Controllable Subject Customization

**Authors:** Xuan Han, Yihao Zhao, Mingyu You

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10902v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10902v1)

**Summary:** Subject Customization is a foundational task in modern image generation. By providing a few reference images and a text prompt, users can generate images of a specific object in any desired scene. However, existing methods still struggle to achieve effective pose control for customized subjects. In practice, they often exhibit inaccurate poses or inconsistent cross-pose appearances. These limitations suggest that understanding objects in a volumetric manner remains a significant challenge for 2D...

---

### 26. The 1st PortraitCraft Challenge: A CVPR 2026 Workshop Competition on Portrait Composition Understanding and Generation

**Authors:** Zijie Lou, Youyun Tang, Xiaochao Qu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10894v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10894v1)

**Summary:** This paper presents an overview of the inaugural PortraitCraft Challenge, held as one of the official competitions at CVPR 2026. The challenge focuses on portrait composition understanding and generation, aiming to advance AI research in portrait aesthetics analysis and controllable image synthesis. Unlike existing datasets and tasks that primarily focus on global aesthetic scoring, PortraitCraft introduces a unified evaluation framework comprising two complementary tracks. Track 1 requires mode...

---

### 27. Improving Text-Instance Alignment Of Foreground Conditioned Out-Painting Via Customized Concept Embedding

**Authors:** Yihao Zhao, Xuan Han, Bin He, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10892v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10892v1)

**Summary:** To showcase products, merchants often incur substantial costs creating high-quality display images. Foreground Conditioned Outpainting (FCO) meets this demand, allowing users to create desired backgrounds for foreground instances at a low cost by adjusting the text prompt. However, existing text-driven FCO methods exhibit critical flaws in their outputs, most notably the presence of artifacts, which refer to regions in the synthesized background that share the same semantics as the foreground in...

---

### 28. Listen, Look, and Learn: Learning Without Forgetting through SAM-Audio

**Authors:** Avi Gupta, Nilotpal Sinha, Vishnu Raj, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10887v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10887v1)

**Summary:** Class-Incremental Learning (CIL) aims to continuously learn new classes without forgetting previously acquired knowledge. While recent CIL advances have spurred significant interest across various modalities, the audio-visual setting remains underexplored. Furthermore, although foundational multimodal models like SAM-Audio encapsulate rich static priors, our empirical analysis reveals that these representations struggle in incremental settings. This work bridges this gap by integrating SAM-Audio...

---

### 29. XtrAIn: Training-Guided Occlusion for Feature Attribution

**Authors:** Thodoris Lymperopoulos, Ioannis Kakogeorgiou, Denia Kanellopoulou

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10877v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10877v1)

**Summary:** Occlusion-based attribution methods provide an intuitive way to estimate feature importance by perturbing input features and measuring the resulting change in model output. However, their reliability is strongly affected by how feature removal is implemented: externally selected baselines can introduce bias, out-of-distribution samples, and unstable explanations, while in nonlinear models the occlusion of a set of features can also alter the contribution of non-occluded features. We refer to thi...

---

### 30. Advancing Wood Identification in the Philippines: Utilizing the Xylorix Platform for Efficient AI Model Development and Deployment for Five Key Species

**Authors:** Rosalie C. Mendoza, Vivian C. Daracan, Arlene D. Romano, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10876v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10876v1)

**Summary:** Illegal logging and timber trade continue to pose significant challenges in the Philippines, where accurate wood species identification is essential for enforcement but limited by the need for specialised equipment and expertise. This study aims to evaluate whether AI models for macroscopic wood identification can be developed and deployed by wood scientists without programming expertise using the Xylorix platform, focusing on five Philippine hardwood species: Mangium (Acacia mangium Willd.), Ra...

---

### 31. Schmidt Decomposition-Based Methods for Efficient Quantum Image Encoding

**Authors:** Ana-Maria Pangeva, Yassine Ferhi, Alexander Geng, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10874v1)

**Summary:** In quantum image processing, a fundamental step is encoding classical image data into quantum states. This can be achieved using methods such as Flexible Representation of Quantum Images (FRQI), Quantum Probability Image Encoding (QPIE), and Novel Enhanced Quantum Representation (NEQR). However, on real quantum hardware, these encodings can quickly lead to circuits with many gates, large circuit depth, and high qubit usage, which is a problem for Noisy Intermediate-Scale Quantum (NISQ) devices. ...

---

### 32. LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination

**Authors:** Taishan Li, Jiwen Zhang, Siyuan Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10862v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10862v1)

**Summary:** Vision-Language-Action (VLA) models achieve strong performance on standard manipulation benchmarks, but most evaluations assume that task-relevant objects are fully visible. This assumption often fails in realistic settings, where occlusion makes manipulation partially observable. In this paper, we study \textit{scene-induced occlusion} as a fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-oriented extension of LIBERO. Experiments show that state-of-the-art VL...

---

### 33. HarmoView: Harmonizing Multi-View Constraints for Identity-Consistent Video Generation

**Authors:** Cong Wang, Zhentao Yu, Hongmei Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10839v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10839v1)

**Summary:** Current identity-consistent video generation methods struggle to preserve appearance fidelity under large viewpoint changes. While introducing multi-view reference input offers a natural solution, progress remains constrained by the lack of effective frameworks for multi-view inputs and the scarcity of multi-view data. We address these challenges by proposing HarmoView, a robust framework for identity-consistent video generation that effectively integrates multi-view cues through three architect...

---

### 34. Earth-OneVision: Extending Remote Sensing Multimodal Large Language Models to More Sensor Modalities and Tasks

**Authors:** Miaoxin Cai, Guanqun Wang, Wei Zhang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10819v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10819v1)

**Summary:** RS-MLLMs enable natural-language understanding and spatial reasoning over earth observation imagery. However, existing models support only a narrow range of sensor types and tasks, yielding a fragmented view of the earth and leaving cross-modal geoscientific knowledge largely unexploited. This work presents Earth-OneVision, a 2B RS-MLLM that unifies six sensor modalities (i.e., optical, SAR, infrared, multispectral, temporal, and video) and cross-sensor fusion across 9 task categories within a s...

---

### 35. IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation

**Authors:** Jiawei Gao, Chaoqi Liu, Peilin Wu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10818v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10818v1)

**Summary:** Real-world robotic manipulation tasks often involve forceful interactions with the environment, such as using tools of varying weights, transporting objects with different masses, and performing contact-rich tasks like table wiping. Previous learning-based approaches typically employ imitation learning policies that output target end-effector poses tracked by low-level impedance controllers. In these systems, forceful interactions are either implicitly realized through steady-state tracking erro...

---

### 36. Deep learning for echo sounder data

**Authors:** Ketil Malde

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10811v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10811v1)

**Summary:** There is no doubt that over the last decade, techniques from the field of machine learning have revolutionized how we process and interpret data, especially images and text. For underwater observations acoustics is a primary source of information, and naturally, deep learning methods have been applied to echograms and other acoustics data, but so far with rather modest results. Here, we argue that due to intrinsic properties of acoustic data, substantial advances will likely require research int...

---

### 37. SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning

**Authors:** Wenhao Yan, Fengjia Guo, Zhuoyi Yang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10804v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10804v1)

**Summary:** Controlled character animation requires transferring motion from a driving sequence to a reference character. Prior works heavily rely on intermediate representations, including pose skeletons to represent motion or masked background to represent environment, which inevitably leads to information loss. To address this, we present SCAIL-2, an framework that bypasses those intermediates and achieves \textbf{end-to-end} character animation. By directly concatenating driving videos to the sequence, ...

---

### 38. Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use

**Authors:** Zhixin Ma, Yutong Zhou, Yongqi Li, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10803v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10803v1)

**Summary:** Multimodal Large Language Models (MLLMs) excel at utilizing digital APIs and increasingly serve as the "brain" of embodied AI, instructing robots to interact with the physical world. In such embodied settings, a central capability is the use of physical tools, which underpins MLLMs' ability to assist humans in real-world tasks. Despite the importance, MLLMs' proficiency in physical tool use remains largely unexplored. To address this gap, we introduce PhysTool-Bench, the first physical tool-use ...

---

### 39. A Multimodal RGB and Events Dataset for Hand Detection in First-Person View

**Authors:** Bharghav Kota, Yulia Sandamirskaya

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10790v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10790v1)

**Summary:** Existing hand detection algorithms work on images and the detection rate is restricted by the frame rate of the camera. In hand detection applications for moving robotic systems, conventional cameras cause motion blur, especially in darker lighting conditions. We can leverage the use of event-based cameras which possess a high dynamic range, high temporal resolution, and low power consumption. Recent work has shown that using a stereo setup of an event-based and a frame-based camera improves det...

---

### 40. From Patches to Patients: A study of the tile-to-slide performance transferability in Digital Pathology

**Authors:** Sofiène Boutaj, Leo Fillioux, Maria Vakalopoulou, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10778v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10778v1)

**Summary:** Foundation Models (FMs) have recently redefined the state-of-the-art in histopathology by providing robust representations for whole-slide image (WSI) analysis. However, selecting the optimal foundation model (FM) for a specific clinical cohort currently requires multiple preprocessing steps, followed by computationally expensive feature extraction and the training of a Multiple Instance Learning (MIL) aggregator for every model. In this work, we investigate whether efficient tile-level linear p...

---

### 41. Spatially Selective Self-Training for Unsupervised Building Change Detection

**Authors:** Wafaa I. M. Hussin, Zhi Lu, Anas M. I. Mohammed, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10775v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10775v1)

**Summary:** Unsupervised building change detection aims to learn building-change masks from unlabeled bi-temporal remote sensing images. Existing label-free methods often follow a discrepancy-to-mask paradigm, directly using temporal differences, frozen foundation-model responses, prompt-based outputs, or post-processing results as final change maps. Although these strategies provide annotation-free cues, they do not learn a task-specific building-change detector and remain vulnerable to the gap between gen...

---

### 42. ZODS-RS -- Zero-training Oriented Detection & Segmentation for Remote Sensing

**Authors:** Zuan Gu, Tianhan Gao, Langxu Zhao

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10769v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10769v1)

**Summary:** Remote-sensing and UAV applications need models that generalize across platforms and viewpoints without task-specific training. Yet training-free pipelines often falter on oriented geometry, scale/rotation variation, and crowded ports or airfields, and rarely unify detection and segmentation. We introduce ZODS-RS, a training-free, closed-form pipeline that outputs horizontal boxes (HBB) and instance masks. Built on DINOv3 dense features and SAM-style proposals, ZODS-RS chains: PP (prototype puri...

---

### 43. DD-INR: Dynamics-Driven Implicit Neural Representation for Accelerated Whole-Brain Functional MRI Reconstruction

**Authors:** Qiaoxin Li, Caini Pan, Pierre-Antoine Comby, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10756v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10756v1)

**Summary:** Accelerated acquisition of fMRI enables enhanced detection of neurovascular (BOLD) activity in the brain, but image reconstruction becomes challenging with high k-space undersampling: Task-evoked BOLD signals are small in magnitude, which traditional anatomical MRI reconstruction methods fail to recover, as they favor spatial accuracy over temporal fidelity. We present DD-INR, a Dynamics-Driven Implicit Neural Representation framework tailored for accelerated fMRI that benefits from incoherent t...

---

### 44. Patient-Level Diagnosis of Acute Myeloid Leukemia via Deep Learning Analysis of Bone Marrow Smear

**Authors:** Yuqi Ma, Tianyi Wang, Weihua Meng, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10735v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10735v1)

**Summary:** Bone marrow smear review remains important for acute myeloid leukemia (AML) assessment, but manual single-cell interpretation is labor-intensive and patient-level diagnosis requires aggregation of many cellular observations. We present a cell-to-patient deep learning pipeline for AML-assisted diagnosis from bone marrow smear images. The study included 258 patients from six anonymized centers, including a main cohort of 169 patients from Centers 1-3 and an external validation cohort of 89 patient...

---

### 45. ++nnU-Net: Scaling nnU-Net with Prefix-Based Data Augmentation

**Authors:** Ana Sofia Santos, André Ferreira, Gijs Luijten, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10713v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10713v1)

**Summary:** The nnU-Net has demonstrated continuous success in medical segmentation tasks, which heavily rely on the availability and diversity of annotated biomedical data. However, assembling medical imaging cohorts remains challenging due to numerous factors such as privacy regulations and annotation costs. As a result, data augmentation plays a crucial role in increasing data availability while maintaining anatomical feasibility. Hence, we propose the ++nnU-Net, a novel data augmentation module based on...

---

### 46. Vector Map as Language: Toward Unified Remote Sensing Vector Mapping

**Authors:** Yinglong Yan, Yunkai Yang, Haoyi Wang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10701v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10701v1)

**Summary:** Remote sensing vector mapping aims to generate structured maps of geospatial entities, such as buildings, roads, and water bodies, from remote sensing imagery. In practice, vector maps usually contain multiple category layers and heterogeneous entity structures, requiring a unified model for diverse mapping needs. However, existing methods typically represent vector objects as polygons or graphs, making them suitable only for specific categories: polygons poorly capture topological relations, wh...

---

### 47. Using the YOLOv12 Model for Verifying the Correct Color Sequence of Wires in Network Cables (Patch Cords) on the Production Line

**Authors:** Amin Doroodchi, Danial Soleimany

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10699v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10699v1)

**Summary:** In the production process of network cables, ensuring the correct color sequence of wire pairs inside the standard connector plays a critical role in the final performance of the cable, as any misplacement or color-ordering error can lead to defective products and impose significant costs. Traditional inspection methods based on visual examination through digital microscopes are typically time-consuming, tedious, and prone to human error. In this study, an intelligent system based on the twelfth...

---

### 48. Don't waste SAM

**Authors:** Nermeen Abou Baker, Uwe Handmann

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10696v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10696v1)

**Summary:** Meta AI has recently released the Segment Anything Model (SAM), which demonstrates exceptional zero-shot image segmentation performance across various tasks with remarkable accuracy. Despite its inability to provide accurate segmentation across multiple research fields, SAM still serves as a valuable starting point for supporting the segmentation pipeline process, particularly for tasks that require extensive and senior skills annotations. This study aims to evaluate the generalization of SAM an...

---

### 49. UniDexTok: A Unified Dexterous Hand Tokenizer from Real Data

**Authors:** Dong Fang, Youjun Wu, Yuanxin Zhong, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10683v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10683v1)

**Summary:** Dexterous hands are essential for fine-grained manipulation, but their hardware designs vary substantially across embodiments. Differences in kinematics, joint definitions, and degrees of freedom make it difficult to define a shared state representation compared with parallel grippers. As a result, dexterous-hand data remains fragmented and difficult to use for joint training. In this work, we propose the Unified Dexterous Hand Model (UDHM), which maps human and robot hand states into a shared 2...

---

### 50. FadeMem: Distance-Aware Memory Consolidation for Autoregressive Video Diffusion

**Authors:** Yu Lu, Junjie Yang, Piotr Koniusz, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10671v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10671v1)

**Summary:** Autoregressive video generators synthesize long videos by generating successive temporal segments, but their historical KV cache grows with video length. Existing bounded-cache methods reduce this cost with local windows, sink tokens, or compressed memory states, yet they usually assign fixed roles to different parts of the history. We propose FadeMem, a distance-aware KV memory consolidation mechanism that organizes historical KV blocks into a temporal hierarchy under a fixed cache budget. This...

---

## cs.LG

**50 papers**

### 1. When to Align, When to Predict: A Phase Diagram for Multimodal Learning

**Authors:** Ilay Kamai, Hugues Van Assel, Aviv Regev, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11190v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11190v1)

**Summary:** Cross-modal alignment (CA) and cross-modal prediction (CP) are the dominant paradigms for multimodal representation learning, yet there is no systematic understanding of when each succeeds, when each fails, and when cross-modal training helps at all -- a gap that leaves practitioners, especially in scientific domains like biomedicine or astrophysics, with heterogeneous instruments and multiple levels of organization and measurement, unable to diagnose why standard methods underperform the best s...

---

### 2. A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

**Authors:** Tong Xie, Yuanhao Ban, Yunqi Hong, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11189v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11189v1)

**Summary:** Supervised fine-tuning (SFT) typically maximizes the likelihood of every token in a demonstrated trajectory. However, an observed token can be non-unique, noisy, or misaligned with the model prior. Strictly fitting toward this one-hot target may be suboptimal, especially when the pretrained model encodes a rich knowledge prior. In this work, we reinterpret SFT as target distribution design: instead of studying only the loss objective, we analyze the token-level target that the loss drives the mo...

---

### 3. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents

**Authors:** Weixian Xu, Shilong Liu, Mengdi Wang

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11182v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11182v1)

**Summary:** In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applicability. To mitigate cross-dataset interference, EEVEE introduces a router that p...

---

### 4. The Role of Feedback Alignment in Self-Distillation

**Authors:** Semih Kara, Oğuzhan Ersoy

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11173v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11173v1)

**Summary:** Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this contex...

---

### 5. Predicting Future Behaviors in Reasoning Models Enables Better Steering

**Authors:** Evgenii Kortukov, Piotr Komorowski, Florian Klein, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11172v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11172v1)

**Summary:** Deployed large reasoning models (LRMs) often behave unexpectedly. Test-time steering controls LRM outputs by intervening on their hidden representations, but it can degrade output quality. We argue that prior steering work implicitly relies on internal features that detect behavior in already generated text. We show that these detection features are poor predictors of future behavioral outcomes, and thus not the natural intervention target. Instead, we train activation probes to predict future b...

---

### 6. Algorithmic and Minimax Complexities in Kernel Bandits

**Authors:** Yunbei Xu

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11171v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11171v1)

**Summary:** Gaussian-process upper confidence bound (GP-UCB) and decision-estimation-coefficient (DEC) methods may appear, at first sight, to belong to different theories. This paper places the two viewpoints in a common algorithmic-information language for frequentist RKHS bandits. GP-UCB fixes an algorithmic, rather than true, Gaussian-process prior and exploits realized-trajectory complexity together with computational tractability, whereas MAMS optimizes a robust class-wide MAIR/DEC envelope. Through th...

---

### 7. COGENT: Continuous Graph Emulators with Neural Ordinary Differential Equations for Long-Term Physical Forecasting

**Authors:** Zesheng Liu, Maryam Rahnemoonfar

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11162v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11162v1)

**Summary:** In this work, we present COGENT, a continuous graph emulator with Neural Ordinary Differential Equations for long-term physical forecasting on irregular geospatial meshes. COGENT encodes a finite history of system states and associated forcing fields and external forcings with a graph-based history encoder, producing node-wise context vectors that capture both local spatial interactions and temporal evolution. These context vectors initialize and condition a latent Neural Ordinary Differential E...

---

### 8. Itô maps for any-step SDEs

**Authors:** Zhengkai Pan, Peter Potaptchik, Wenxi Yao, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11156v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11156v1)

**Summary:** Recent one-step generative models accelerate sampling by learning deterministic flow maps of the underlying dynamics. These methods rely on learning from ordinary differential equations, leaving open how to define an exact distillation procedure for stochastic dynamics. We introduce the Itô map, an any-step stochastic flow map that takes an intermediate state and Brownian path and predicts future states in a single pass. The Itô map formulation yields novel estimators for inference-time control ...

---

### 9. Efficiently Learning Drifting Halfspaces with Massart Noise

**Authors:** Mingchen Ma, Guyang Cao, Jelena Diakonikolas, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11149v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11149v1)

**Summary:** We study the problem of learning a drifting concept in the presence of Massart noise. In this framework, an online learner has access to a history of independent samples whose labels are noisy versions of a target concept that may change from round to round. The goal is to output, in each round, a hypothesis with small prediction error. We study the complexity of this learning problem for the fundamental class of margin-separable linear classifiers (halfspaces). On the positive side, we give a c...

---

### 10. OncoTraj: a public benchmark for longitudinal resistance prediction in EGFR-mutant non-small-cell lung cancer on osimertinib

**Authors:** Abhijoy Sarkar, Aarchi Singh Thakur

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11144v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11144v1)

**Summary:** Resistance to first-line osimertinib in EGFR-mutant non-small-cell lung cancer (NSCLC) is the canonical example of predictable clonal evolution under therapeutic pressure, yet no public benchmark exists for training or evaluating computational models on the corresponding longitudinal patient trajectories. We introduce OncoTraj, a public benchmark of 813 EGFR-mutant NSCLC patients receiving first-line osimertinib, harmonized from three real-world clinical-genomic sources: MSK-CHORD (672 patients)...

---

### 11. Data assimilation for subsurface flow using latent diffusion model parameterization: performance of ensemble-Kalman and Monte Carlo techniques

**Authors:** Guido Di Federico, Wenchao Teng, Louis J. Durlofsky

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11140v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11140v1)

**Summary:** Data assimilation (DA) in subsurface flow entails calibrating model parameters to match observed data, typically at wells, while preserving geological realism. Latent diffusion models (LDMs) provide efficient mappings from high-dimensional geological model space to a low-dimensional latent variable, reducing the dimensionality of the inverse problem while maintaining plausibility in posterior geomodels. However, the high nonlinearity in the LDM mapping may degrade the performance of Kalman-gain-...

---

### 12. First-Order Trajectory Matching: Fast Ensemble Predictions of Chaotic, Turbulent, Stochastic Systems

**Authors:** Shreya Jha, Timo Schorlepp, Nicholas Geissler, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11138v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11138v1)

**Summary:** We introduce First-Order Trajectory Matching (FTM), a surrogate-modeling method that learns the first-order local transport of probability mass from trajectories of stochastic systems. By matching the symmetric first-order motion of trajectories, FTM learns the probability current velocity, whose flow preserves time marginals to match ensemble averages, while also capturing current-like trajectory quantities such as fluxes, circulations, and barrier-crossing currents. FTM learns the current velo...

---

### 13. Robust Regression of General ReLUs with Queries

**Authors:** Ilias Diakonikolas, Daniel M. Kane, Mingchen Ma

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11130v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11130v1)

**Summary:** We study the task of agnostically learning general (as opposed to homogeneous) ReLUs under the Gaussian distribution with respect to the squared loss. In the passive learning setting, recent work gave a computationally efficient algorithm that uses $poly(d,1/ε)$ labeled examples and outputs a hypothesis with error $O(opt)+ε$, where $opt$ is the squared loss of the best fit ReLU. Here we focus on the interactive setting, where the learner has some form of query access to the labels of unlabeled e...

---

### 14. DMT: Demographic Conditioning, Morphology-Enhanced Transformer for Cuffless Blood Pressure Estimation from PPG Signals

**Authors:** Yidan Shen, Neville Mathew, Maham Rahimi, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11125v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11125v1)

**Summary:** Blood pressure (BP) is a key marker for cardiovascular risk assessment and therapeutic decision-making, and Photoplethysmography (PPG) enables low-cost, wearable-friendly cuffless BP estimation. However, even with recent progress, many PPG-based models are trained with BP regression alone and may rely on amplitude-dominated shortcuts. In addition, demographic covariates that systematically modulate vascular compliance are often incorporated only via late fusion, limiting subject-specific represe...

---

### 15. Overcoming Rank Collapse in Feedback Alignment

**Authors:** Gauthier Boeshertz, Razvan Pascanu, Claudia Clopath

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11123v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11123v1)

**Summary:** Backpropagation (BP) is widely viewed as biologically implausible, in part because it requires feedback weights to be the transpose of forward weights for error propagation. Interestingly, when training a network with fixed random feedback weights to circumvent this issue, learning aligns the forward weights with the feedback weights, leading the backpropagated error signal to become an approximation of the standard gradient used by BP. This process, called Feedback Alignment (FA), occurs in MLP...

---

### 16. TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning

**Authors:** Heming Zou, Qi Wang, Yun Qu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11119v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11119v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. Past efforts have focused on allocating available rollout resources ...

---

### 17. Data-Driven Dynamic Assortment in Online Platforms: Learning about Two Sides

**Authors:** Rahul Roy, Nur Sunar, Jayashankar M. Swaminathan

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11118v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11118v1)

**Summary:** We study a dynamic assortment problem on a two-sided service platform with incomplete information and heterogeneous customers in a discrete-time setting. In each period, a customer arrives seeking service, and the platform chooses an assortment of sellers to display. The customer then proposes a transaction to at most one seller in the assortment according to a multinomial logit choice model. After a fixed number of periods, sellers review the proposals they have received and each chooses at mos...

---

### 18. Multimodal Brain Tumour Classification Using Feature Fusion

**Authors:** Wajih ul Islam, Muhammad Yaqoob, Javed Ali Khan, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11107v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11107v1)

**Summary:** Clinicians diagnose brain tumors by synthesizing patient symptoms, medical history, and quantitative imaging data from modalities such as MRI and CT scans into a unified clinical judgement. However, most deep learning models rely on MRI/CT images alone, failing to replicate the clinicians multimodal reasoning. We explore a two-branch multimodal network combining raw MRI scans with 91 extracted radiomic features (intensity, texture, shape, and boundary descriptors) to classify brain tumors into g...

---

### 19. Limitations of Learning Tanh Neural Networks with Finite Precision

**Authors:** Philipp Grohs, Matěj Trödler

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11104v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11104v1)

**Summary:** We investigate limitations of learning $\tanh$ neural networks from point evaluations under finite-precision computations and $L^p$ accuracy guarantees, building on Berner, Grohs, and Voigtländer (2023). Our approach is based on a novel construction of sharply localized bump functions via iterated $\tanh$ activations. Using this mechanism, we show that, in a finite-precision setting, no adaptive randomized algorithm based on $m$ samples can achieve a convergence rate higher than the Monte Carlo ...

---

### 20. Do Transformers Actually Help Intrusion Detection? A Temporal Sequence Evaluation on CIC-IDS2017

**Authors:** Zach Moczkodan, Hany Ragab

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11098v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11098v1)

**Summary:** Recent deep learning approaches for network intrusion detection increasingly incorporate temporal architectures such as recurrent networks and Transformers, often reporting near-perfect performance on CIC-IDS2017. However, many existing studies neither supply their temporal modules with genuine sequence inputs nor evaluate under realistic, leakage-free conditions, making it unclear whether reported gains arise from true sequence-modeling capability. In this work, we reformulate CIC-IDS2017 as a ...

---

### 21. Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning

**Authors:** Zhiyuan Zhou, Andy Peng, Charles Xu, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11087v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11087v1)

**Summary:** Expressive continuous control policies, such as diffusion and flow models, form the backbone of recent advances in scaling imitation learning for simulated and real robot control. While they are known to scale stably in the supervised imitation learning setting, incorporating them into reinforcement learning (RL) pipelines for policy improvement has proven more difficult. It often requires specialized training objectives or backpropagating through denoising processes, which cause well-known issu...

---

### 22. Unifying Local Communications and Local Updates for LLM Pretraining

**Authors:** Pietro Cagnasso, Eugene Belilovsky, Edouard Oyallon

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11081v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11081v1)

**Summary:** Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links. Many practical methods reduce communication frequency but still rely on synchronous All-Reduce operations that maintain identical model states and tie progress to global collectives. This can become a bottleneck when bandwidth or worker speed is heterogeneous. We introduce GASLoC, a novel decentralized pre-training algorithm tha...

---

### 23. Exploring the Design Space of Reward Backpropagation for Flow Matching

**Authors:** Ruoyu Wang, Boye Niu, Xiangxin Zhou, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11075v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11075v1)

**Summary:** Aligning text-to-image flow matching models with human preferences via direct reward backpropagation is sample-efficient but hampered by two well-known pathologies: activations cannot be stored across the full sampling trajectory at modern model scale, and chained Jacobian products across steps inflate the reward gradient as it travels back to early indices. Connector-based methods, such as LeapAlign, address these issues by replacing the full backward trajectory with a short pinned path, highli...

---

### 24. GRAFT: Gain-Recalibrated Adapters for Transformer-Based Neural Population Activity Modeling

**Authors:** Xiangsheng Ge, Yang Xie

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11066v1)

**Summary:** Neural population activity models can recover rich temporal structure from binned spikes, but their read-in and readout layers often remain tied to a fixed set of recorded neurons. This coupling limits reuse in long-term brain-computer interfaces, where recorded neuron identities, counts, and response statistics can change across days. We introduce GRAFT, a Transformer-based neural population activity model that separates reusable temporal dynamics from a recalibratable neuron interface. The neu...

---

### 25. CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs

**Authors:** Joachim Schaeffer, Thomas Jiralerspong, Alexander Panfilov, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11063v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11063v1)

**Summary:** AI control protocols oversee untrusted models by monitoring their actions and modifying potentially unsafe steps, often using a trusted model. This partially tampers with the untrusted model's trajectory. If the trusted model detects such an intervention, it may infer properties of the monitor and adapt to evade control. We introduce \textbf{CIAware-Bench}, a benchmark for measuring \textbf{c}ontrol \textbf{i}ntervention (CI) awareness across frontier models. CIAware-Bench tests whether models c...

---

### 26. Flexible Kernels for Protein Property Prediction

**Authors:** Martin Jankowiak, Yerdos Ordabayev, Rudraksh Tuwani, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11057v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11057v1)

**Summary:** Despite its importance to applications in protein design, predicting protein properties like binding affinity and thermostability from sparse experimental data remains a significant challenge. Accordingly, we introduce a class of sequence kernels that exploit evolutionary substitution matrices as well as local linearity and demonstrate that the resulting Gaussian processes provide data-efficient models of protein property landscapes, frequently outperforming alternatives that rely on foundation ...

---

### 27. What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents

**Authors:** Martin Andres Bertran, Aaron Roth, Zhiwei Steven Wu

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11045v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11045v1)

**Summary:** Reusing a held-out benchmark adaptively should, in principle, invite overfitting. Yet benchmark-driven machine learning (ML) has produced surprisingly little overfitting in practice. An attractive hypothesis is that successful ML strategies are highly compressible. We study this in the setting of LLM-driven research agents, where the hypothesis becomes directly testable via two complementary information bottlenecks. In \emph{output compression}, an exploration agent adaptively searches for high-...

---

### 28. Generalized Conformal Predictive Systems Under Distributional Shifts

**Authors:** Jef Jonkers, Johanna Ziegel

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11044v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11044v1)

**Summary:** Conformal predictive systems (CPS) output calibrated bands of CDFs under exchangeability. We extend generalized CPS to non-exchangeable settings by encoding distributional shifts through observation-specific permutation weights. This yields shift-aware predictive systems that remain valid whenever the test point is, conditionally on the unordered sample, a weighted draw from the observed atoms. Since such weights are typically estimated, we introduce weight-uncertainty boxes and construct robust...

---

### 29. AuRA: Internalizing Audio Understanding into LLMs as LoRA

**Authors:** Bo Cheng, Lei Shi, Zhanyu Ma, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11033v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11033v1)

**Summary:** Recent efforts to extend large language models (LLMs) to speech inputs typically rely on cascaded ASR-LLM pipelines, end-to-end speech-language models, or bridge/distillation-based adaptation. While these routes respectively reuse strong pretrained components, enable native speech-language interaction, or offer lightweight adaptation, they often suffer from transcript-interface latency, costly multimodal training, or sequential speech-language coupling. To address these limitations, we present A...

---

### 30. Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models

**Authors:** Bowen Ping, Xiangxin Zhou, Penghui Qi, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11025v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11025v1)

**Summary:** Recent work has demonstrated that online reinforcement learning (RL) can substantially improve the quality and alignment of flow matching models for image and video generation. Methods such as Flow-GRPO and CPS cast the denoising process as a Markov Decision Process and apply PPO-style ratio clipping to enforce a trust region. However, we argue that ratio clipping is structurally ill-suited for flow models: the probability ratio between new and old policies is a noisy, single-sample estimate of ...

---

### 31. Generative Archetype-Grounded Item Representations for Sequential Recommendation

**Authors:** Yifan Li, Jiahong Liu, Xinni Zhang, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11023v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11023v1)

**Summary:** Sequential recommendation aims to predict users' next interaction with items by analyzing their historical behavior. However, the limited quality of item representations remains a critical bottleneck. While pre-trained large language models (LLMs) can provide rich semantic representations, existing approaches only rely on static encoding of fixed attributes, overlooking the crucial role of target audiences in defining item identity. Moreover, the semantic space struggles to reflect actual user b...

---

### 32. Data-Driven Runway and Taxiway Exits Prediction of Landing Aircraft: A Case Study at Hartsfield-Jackson Atlanta International Airport

**Authors:** Alex Porcayo, Yutian Pang, Maria Thomas, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11017v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11017v1)

**Summary:** Airport surface operations increasingly constrain performance at high-throughput hubs. This study examines arrival taxi-in decisions at Hartsfield-Jackson Atlanta International Airport (KATL) and proposes a two-stage, data-driven decision aid that mirrors controller workflow. Stage I predicts the runway exit selected by an arriving aircraft. Stage II predicts whether, given that exit, the aircraft will cross the active departure runway at a designated point or use the end-around taxiway. Models ...

---

### 33. Learning Doubly Sparse Explicitly Conditioned Transforms

**Authors:** Tudor Pistol

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10975v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10975v1)

**Summary:** Finding convenient spaces in which certain hypotheses regarding an assumed sparse structure of natural signals hold true has become a desirable result in recent research, its implications being reflected in areas such as data compression, noise reduction and feature extraction. While the extensively used analytical transforms, such as DFT or DCT, already provide efficient algorithms and robust sparse representations, they assume a fixed prior about the data, failing to accurately capture the spe...

---

### 34. Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning

**Authors:** Renjie Mao, Xiangxin Zhou, Lvfang Tao, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10968v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10968v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) has become standard for improving LLM reasoning. However, existing PPO-style trust-region mechanisms remain position-agnostic by enforcing uniform thresholds across all tokens independently. This pointwise treatment conflicts with autoregressive generation in two critical ways. First, uniform thresholds ignore autoregressive asymmetry. Early-stage deviations produce compounding sequence-level drift, causing static thresholds to under-regulate...

---

### 35. Population-Aware Physics-Informed Neural Particle Flow for Bayesian Update

**Authors:** Batu Candan, Simone Servadio

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10959v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10959v1)

**Summary:** Physics-informed neural particle flow (PINPF) learns a deterministic transport field that moves particles from a prior distribution toward a Bayesian posterior while enforcing the governing probability-evolution equation. However, the standard PINPF velocity model processes particles independently and therefore does not explicitly condition its transport decisions on the empirical particle population. This paper introduces population-aware PINPF (PA-PINPF), which augments each particle update wi...

---

### 36. Express Language Modeling

**Authors:** Albert Gong, Annabelle Michael Carrell, Raaz Dwivedi, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10944v1)

**Summary:** We introduce a new tool, Express, for converting a non-causal attention approximation into a causal approximation with matching approximation guarantees. When combined with the state-of-the-art Thinformer approximation, Express improves upon the best known causal attention guarantees, delivering $\log^{3/2}(n)/s$ approximation error with only $O(s)$ memory and $O(s^2 \log^2(n))$ compression overhead for a sequence of length $n$. We pair these developments with an efficient I/O-aware Triton imple...

---

### 37. Generative Explainability for Next-Generation Networks: LLM-Augmented XAI with Mutual Feature Interactions

**Authors:** Kiarash Rezaei, Omran Ayoub, Sebastian Troia, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10942v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10942v1)

**Summary:** As artificial intelligence and machine learning (AI/ML) models become integral to network operations, their lack of transparency poses a significant barrier to operator trust. Existing explainable artificial intelligence (XAI) techniques often fail to bridge this gap for non-specialists, producing technical outputs that are difficult to translate into actionable insights. This paper presents a framework specifically designed to address this shortcoming. It leverages a moderately sized large lang...

---

### 38. Democratising Camera Trap AI: An Open-Source Model for Detecting UK Mammals

**Authors:** Paul Fergus, Philip Stephens, Russell A. Hill, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10940v1)

**Summary:** Camera traps have become a cornerstone of biodiversity monitoring, but the artificial intelligence that turns vast quantities of images into usable ecological data is often locked behind commercial platforms or trained on fauna that does not match that of the British Isles. In an attempt to remove barriers and increase uptake, we release an open-source object detection model for 31 classes, 28 common UK mammal and bird species, plus utility classes for humans, calibration poles, and vehicles, dr...

---

### 39. A Systematic Approach for Selecting Trajectories for Data Augmentation

**Authors:** Adam Nordling

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10938v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10938v1)

**Summary:** Trajectory data augmentation is a promising approach to mitigate data scarcity in machine learning applications, but its utility has been limited by the complexity of preserving spatio-temporal coherence. Although prior work demonstrated the viability of geometric perturbation, it relied on naive random selection, leaving a critical gap in understanding which trajectories should be augmented for maximal benefit. This thesis addresses this gap by developing a systematic and scalable framework to ...

---

### 40. CLP: Collocation-Length Prediction for Zero-Loss Adaptive Multi-Token Inference

**Authors:** Xuezhen Xie, Zhiqiang Zhou

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10935v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10935v1)

**Summary:** Large language model inference is bottlenecked by autoregressive decoding, where each token requires a full forward pass. Multi-token prediction (MTP) offers a promising acceleration path, but existing approaches suffer from a fundamental architectural flaw: the MTP head for the first token competes with the backbone's own language model (LM) head, leading to severe quality degradation when predictions are accepted. We identify this head-backbone competition as the root cause of repetitive and i...

---

### 41. Recoverable but Not Stationary:Local Linear Structures in Weights and Activations

**Authors:** Irina Piontkovskaia, Sergey Nikolenko

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10929v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10929v1)

**Summary:** Task vectors, LoRA, activation steering, and random search around pretrained weights all suggest that learned behaviour can be controlled by linear directions. We ask which linear structures actually exist and on what scale. In a synthetic multitask transformer and LoRA adapters on DistilGPT-2 / GPT-2 we find strong local low-rank task-gradient structure but reject the fixed-task-plane hypothesis: static bases miss the recovery direction, and the useful basis drifts substantially within 100 step...

---

### 42. A Constrained Natural-Language Interface for Variational Multi-Physics Finite Element Simulations in FEniCS

**Authors:** Nilay Upadhyay, Wesley F. Reinhart

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10928v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10928v1)

**Summary:** Large language models can reduce the manual effort required to set up finite element simulations, but they introduce reliability risks when generated solver code lies on the critical path. We present a constrained natural-language interface for multi-physics finite element analysis in which the LLM is limited to front-end tasks: parsing prompts into structured JSON, generating Gmsh code only for non-catalog geometries, and using retry feedback for those stages. It never writes FEniCS solver temp...

---

### 43. Task Robustness via Re-Labelling Vision-Action Robot Data

**Authors:** Artur Kuramshin, Özgür Aslan, Cyrus Neary, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10918v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10918v1)

**Summary:** The recent trend in scaling models for robot learning has resulted in impressive policies that can perform various manipulation tasks and generalize to novel scenarios. However, these policies continue to struggle with following instructions, likely due to the limited linguistic and action sequence diversity in existing robotics datasets. This paper introduces Task Robustness via Re-Labelling Vision-Action Robot Data (TREAD), a scalable framework that leverages large Vision-Language Models (VLMs...

---

### 44. Range Penalization: Theoretical Insights with Applications in Federated Learning

**Authors:** Yiyuan She, Zhaojun Hu, Yifan Sun

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10916v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10916v1)

**Summary:** This paper introduces range regularization for federated learning with linear systematic components to enhance statistical accuracy and induce cross-client regularity conducive to quantization, coding, and resource efficiency. Our approach identifies features with shared weights across different clients and adaptively clusters the weights of personalized features at extreme values, a process we refer to as polar clustering. Theoretical analysis of the associated estimators poses significant chal...

---

### 45. Conservation Laws from Data Symmetry in Neural Networks

**Authors:** Jakob Galley, Vahid Shahverdi, Axel Flinth

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10913v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10913v1)

**Summary:** We explore whether intrinsic symmetries of the training data lead to conserved quantities during gradient-flow training of neural networks. Under the assumption that the loss function is analytic and non-polynomial, we prove that data symmetries generically do not induce any additional integrals of motion. For mean squared error (MSE) loss, on the other hand, there are situations in which data augmentation yields extra conserved quantities. We build a framework, utilizing \emph{tensorizable netw...

---

### 46. What Do Deepfake Speech Detectors Actually Hear?

**Authors:** Vojtěch Staněk, Veronika Jirmusová, Anton Firc, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10912v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10912v1)

**Summary:** Deepfake speech detectors often output a single score without explaining why an audio sample is flagged, where in the signal the evidence lies, or what cues drive the decision. We propose an audio-native explainability pipeline using Integrated Gradients on time-aligned self-supervised representations to localize decision evidence over time. We apply the proposed method to three WavLM-based detectors (AASIST, CA-MHFA, SLS) on ASVspoof 5 and manually annotate the highest-attribution regions to pr...

---

### 47. Ethical and Technical Limits of Deepfake Speech Datasets

**Authors:** Vojtěch Staněk, Eva Trnovská, Kamil Malinka, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10911v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10911v1)

**Summary:** Claims about the robustness and fairness of deepfake speech detectors are only as credible as the datasets used to train and evaluate those systems. We present a dataset-level audit of the deepfake speech landscape. We compile and analyze 39 deepfake speech datasets, examining key attributes including accessibility, documentation, demographic and language coverage, dataset scale, and the underlying bona fide speech sources. Our audit reveals two important takeaways. Firstly, fairness assessment ...

---

### 48. Non-linear mechanical field reconstruction coupling recurrent neural networks with physics-informed graph neural networks

**Authors:** Manuel Ricardo Guevara Garban, Yves Chemisky, Étienne Prulière, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10909v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10909v1)

**Summary:** Reconstructing local stress fields in heterogeneous microstructures under non-linear, history-dependent loading remains a major computational bottleneck in multi-scale simulations. We propose a coupled LSTM-GNN framework that links the temporal and spatial aspects of local stress field reconstruction. A Long Short-Term Memory network encodes macroscopic stress-strain sequences into a compact hidden state that captures the path-dependent constitutive response, while a physics-informed Graph Neura...

---

### 49. RAT: Reference-Augmented Training for ASV Anti-Spoofing

**Authors:** Vojtěch Staněk, Anton Firc, Jakub Reš, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10908v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10908v1)

**Summary:** We introduce a spoofing countermeasure architecture conditioned on speaker-reference recordings, but observe that it converges to a solution that effectively ignores the reference during inference. Surprisingly, training with a reference channel induces invariance that improves deepfake detection, even when the reference is absent or mismatched during inference. Based on this observation, we propose a Reference-Augmented Training (RAT) strategy. RAT yields improved detection performance compared...

---

### 50. Human-AI Teaming Through the Lens of Calibration

**Authors:** Eric Nalisnick, Chi Zhang, Sophia Qian, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10906v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10906v1)

**Summary:** We study models for human-AI teaming through the lens of statistical calibration. We assume the team consists of an AI model and human -- both of which are calibrated with respect to some partitioning of the feature space -- and expose how the calibration assumptions propagate into the teaming framework. In particular, we consider frameworks that either (i) combine human and model predictions or (ii) delegate prediction responsibility to either a human or model. We show via theoretical and empir...

---

## cs.NE

**50 papers**

### 1. A Spiking Neural Architecture for Coordinating Arm and Locomotor Control

**Authors:** Lea Steffen, Kathryn Simone, Graeme Damberger, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11034v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11034v1)

**Summary:** Spiking Neural Networks (SNNs) coupled with neuromorphic hardware offer energy-efficient solutions for humanoid robot control. However, existing SNN-based motor control systems address bipedal locomotion and arm control in isolation, leaving integrated control of both unaddressed. We present a spiking architecture that coordinates force-based arm control and bipedal locomotion in a simulated humanoid, using the Neural Engineering Framework (NEF) and Semantic Pointer Architecture (SPA). High-leve...

---

### 2. Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design

**Authors:** Wenxin Wang, Yule Hou, Yu Ji, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10493v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10493v1)

**Summary:** Local deployment of large Mixture-of-Experts (MoE) models falls short of the service quality achieved in cloud-scale environments, even under low-concurrency workloads. We identify four key gaps in local MoE inference: reliance on capacity-reduced models (quantized, distilled, rerouted), inability to meet 30-second TTFT for long prefills (more than 12K), sub-baseline decode throughput (under 20 tokens/s), and poor concurrency under mixed prefill-decode and batched decode workloads. We present a ...

---

### 3. LLM-Guided Neural Architecture Search for Robust Co-Design of Physical Neural Networks

**Authors:** Tyler King, Timothee Leleu

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10294v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10294v1)

**Summary:** Deploying neural networks on unconventional hardware demands architectures that co-optimize task accuracy and platform-specific constraints such as energy cost, physical non-idealities, and numerical precision. Existing neural architecture search (NAS) methods are typically tailored to a single hardware family, limiting cross-platform comparison and generalization. We introduce Unconventional Hardware Neural Architecture Search (UH-NAS), a hardware-agnostic, LLM-guided NAS framework that integra...

---

### 4. Discovering Interpretable Multi-Parameter Control Policies for Evolutionary Algorithms Using Deep Reinforcement Learning

**Authors:** Tai Nguyen, Phong Le, Carola Doerr, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10129v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10129v1)

**Summary:** While deep Reinforcement Learning (deep-RL) has been increasingly applied to parameter control in evolutionary algorithms, rigorous theoretical analysis of parameter control remains largely restricted to single-parameter settings, owing to the difficulty of deriving effective, interpretable multi-parameter policies amenable to formal study. We demonstrate how deep-RL can be leveraged to overcome this barrier, using the (1+($λ$,$λ$))-genetic algorithm optimizing OneMax, one of the few problems wh...

---

### 5. Spiking Neural Network inference on FPGAs with hls4ml

**Authors:** Barry M. Dillon

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10008v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10008v1)

**Summary:** Spiking Neural Networks (SNNs) provide a naturally temporal machine-learning framework. Their neurons maintain an internal state and propagate information through discrete spikes, enabling low-latency temporal inference. Although SNNs are often associated with asynchronous neuromorphic processors, many scientific real-time inference systems rely on conventional synchronous field-programmable gate arrays (FPGAs) and high-level synthesis (HLS) workflows. In this paper we present an extension of hl...

---

### 6. Quality-Diversity Search in Sound Generation: Investigating Innovation Engines for Audio Exploration

**Authors:** Björn Þór Jónsson, Çağrı Erdem, Stefano Fasciani, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09780v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09780v1)

**Summary:** This study addresses the challenges composers and sound designers face in creating and refining tools to achieve their musical goals. Using evolutionary processes to promote diversity and foster serendipitous discoveries, we automate the search through uncharted sonic spaces for sound discovery, arguing that diversity-promoting algorithms can bridge the gap between the theoretical realisation and practical accessibility of sounds. We describe a system for generative sound synthesis combining Qua...

---

### 7. Hybrid Metaheuristic Combining the Dragonfly Algorithm and Tabu Search for the Traveling Salesman Problem

**Authors:** Ammar Bouketta

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09529v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09529v1)

**Summary:** The Traveling Salesman Problem (TSP) is a classical NP-hard combinatorial optimization problem that aims to find the shortest Hamiltonian cycle visiting each city exactly once and returning to the starting point. This paper proposes a hybrid metaheuristic for the TSP by combining the Dragonfly Algorithm (DA), a swarm-intelligence-based global search method, with Tabu Search (TS), a memory-based local search technique. The proposed method follows a High-Level Relay Hybridization (HRH) scheme, in ...

---

### 8. Local Search on Vertex Coloring for Bipartite Graphs

**Authors:** Johanna Gasse

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09509v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09509v1)

**Summary:** Local search is a well-known heuristic method used in optimization. In this thesis, we explore its capabilities on the vertex coloring problem, an $NP$-hard problem with relevance in both theoretical analysis and practical application. To recognize limitations in the applicability of local search of the vertex coloring problem, we analyze local search landscapes on differently-structured bipartite graphs. We identify structures that ensure only global optima can exist as well as ones that enable...

---

### 9. Quantitative Performance Analysis of Stopping Criteria for CMA-ES

**Authors:** Ryoji Tanabe

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09220v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09220v1)

**Summary:** Covariance matrix adaptation evolution strategy (CMA-ES) is a state-of-the-art black-box optimization algorithm. In general, CMA-ES uses a portfolio of multiple stopping criteria to automatically determine when to stop the search. This mechanism aims to avoid unnecessary consumption of the function evaluation budget during stagnation. Stopping criteria play an important role in CMA-ES, particularly when restart strategies are employed. However, the effectiveness of stopping criteria in CMA-ES re...

---

### 10. OpenOpt: An Open-Source SRAM Optimizer Based on Equivalent Circuit Model

**Authors:** Yikai Wang, Yiheng Wu, Can Wang, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09129v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09129v1)

**Summary:** This paper proposes a co-optimization framework that jointly optimizes SRAM architecture and transistor sizing using equivalent circuit models. The framework simplifies inactive SRAM cells into equivalent RC loads and static power models, achieving up to 61.4$\times$ simulation speedup while maintaining high fidelity (read/write delay error $<$0.22%, power error $<$1.68%). A joint search space encompassing architecture parameters and device sizing integrates seven algorithms including SA, PSO, B...

---

### 11. Quantitative Promise Theory: Intentionality and Inference in Autonomous Agents

**Authors:** Mark Burgess

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08552v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08552v1)

**Summary:** I discuss some quantitative representations of Promise Theory for processes involving autonomous agents. Agent models are common in software systems, machine learning, and biology, for example, but may also apply to physics and other forms of engineering. I describe how Bayesian probability and information theoretic optimization, including Active Inference, may be incorporated with promise semantics -- as well as how Promise Theory supplements solutions, helping to avoid probability's pitfalls, ...

---

### 12. Gray-Box Optimization and the Vertex Coloring Problem

**Authors:** Johanna Gasse, Antonia Heinen, Hendrik Higl, et al.

**Published:** 2026-06-06

🔗 [Paper](http://arxiv.org/abs/2606.08128v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08128v1)

**Summary:** Gray-box optimization is an approach for making some problem-specific information available to the algorithm while still relying on fitness information as the main guide to an optimum. This approach was shown to be beneficial in various combinatorial optimization tasks and neatly captures the continuum between fully black-box algorithms and tailored algorithms.   In this work, we discuss different flavors of gray-box algorithms. We show that RLS can find a proper $2$-coloring in a bipartite grap...

---

### 13. Representational Similarity and Model Behavior in Multi-Agent Interaction

**Authors:** Yujin Potter, Seun Eisape, Shiyang Lai, et al.

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07818v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07818v1)

**Summary:** Researchers have shown that neural similarity among humans predicts social closeness and cooperative success, whereas innovation often emerges from interactions among dissimilar individuals. We investigate whether these principles extend to artificial intelligence by examining interactions between large language models. In our experiments, 276 model pairs interact across eight games spanning both cooperation and novelty. We find that pairs with more similar representation spaces achieve signific...

---

### 14. Sparsely gated tiny linear experts

**Authors:** Simon Schug

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07414v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07414v1)

**Summary:** Sparsity allows scaling model parameters without proportionally increasing computational cost. While mixture of experts (MoE) models are made increasingly sparse, individual experts typically remain large and dense. Here, we demonstrate that further increasing sparsity by shrinking each expert to consist of a single neuron and selecting a tiny fraction of many available neurons can improve compute efficiency and interpretability. Counterintuitively, the key to achieving both is removing the nonl...

---

### 15. Combinatorial Landscape Analysis for Dominating Set and Vertex Coloring

**Authors:** Johanna Gasse, Antonia Heinen, Felix Knöfel, et al.

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07361v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07361v1)

**Summary:** We analyze the two combinatorial problems of Dominating Set and Vertex Coloring regarding what kind of local optima are present for various instances. For a variety of graph classes each, we determine whether the induced landscapes are unimodal, plateau-unimodal (all optima are just one plateau), equimodal (all local optima are global) or truly multimodal. We do this for two different neighborhood operators, one based on making only a single change and one also allowing swaps (interchanging two ...

---

### 16. LLM-Guided Evolution for Medical Decision Pipelines

**Authors:** Ivan Sviridov, Artem Oskin, Ivan Panin, et al.

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07342v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07342v1)

**Summary:** Adapting large language models (LLMs) to clinical workflows often requires costly fine-tuning or manual prompt and pipeline engineering. We study LLM-guided MAP-Elites evolution as an inference-time alternative for discovering medical decision strategies and provide an implementation repository at https://github.com/univanxx/llm_guided_evo_medical. We formulate urgency triage, interactive consultation, and medical image classification as evolutionary searches over executable artifacts optimized ...

---

### 17. The Whale That Outswam Evolution: Swarm Intelligence Maximises Memory in Connectome Reservoirs

**Authors:** Anmol Guragain, Savvas Kakalis, Juan Ignacio Godino-Llorente

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.09902v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09902v1)

**Summary:** Reservoir computing exploits the fixed dynamics of a recurrent network for temporal processing, requiring only a trained linear readout. Biological neural connectomes, shaped by millions of years of evolution, may encode computational structure beyond what random reservoirs provide, yet whether that structure can be further enhanced by principled optimisation remains an open question. We address it by applying four gradient-free, bio-inspired optimisers (Particle Swarm Optimisation, Differential...

---

### 18. A Data-Free Symbolic Regression Approach for Solving Equations

**Authors:** Sergei Garmaev, Vinay Sharma, Olga Fink

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07152v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07152v1)

**Summary:** Many equations arising in science currently cannot be solved by available analytical techniques and are therefore solved numerically, without yielding explicit symbolic expressions. Existing symbolic regression approaches can recover symbolic expressions, but require training data obtained from the underlying process, rather than the governing equation alone. We propose the Symbolic Equation Solver (SES), a framework that formulates equation solving as an optimization problem over differentiable...

---

### 19. Emergent Language as an Approach to Conscious AI

**Authors:** Zengqing Wu, Chuan Xiao

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06380v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06380v1)

**Summary:** The question of whether artificial systems can be conscious remains open, in part because existing approaches either evaluate systems against theory-derived checklists (discriminative) or engineer consciousness-inspired modules directly (architectural); both leave open whether observed structures are artifacts of human language priors. We propose a generative methodology: emergent language (EL) in multi-agent reinforcement learning, where agents start from minimal (no language, no concept of sel...

---

### 20. Hub-Aware Hybrid Search: Accelerating the Locally Aligned Ant Technique

**Authors:** Simone Vilardi, Reynier Peletier, Felipe Contreras, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06198v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06198v1)

**Summary:** Finding manifold structures in noisy and high-dimensional point clouds is a challenging but important problem. In astronomical observation survey and simulation data the detection of filaments, streams (1D), walls (2D) and clusters (3D) gives rise to deeper understanding of the evolution of our universe. The Locally Aligned Ant Technique (LAAT) uses biologically inspired agents to efficiently recover faint and multidimensional structures. However, very dense hubs (e.g. nodes or globular clusters...

---

### 21. ITP-STDP: An Intrinsic-Timing Power-of-Two Learning Engine for On-Chip SNN Training

**Authors:** Haihang Xia, Xinyu Zhao, Xuecheng Wang, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06159v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06159v1)

**Summary:** Spiking neural networks (SNNs) have the potential to emerge as the third generation of neural networks and have attracted increasing attention across a wide range of applications. However, the large number of synaptic connections in SNNs leads to intensive weight-update computation by on-chip learning algorithms during training, resulting in substantial hardware resource utilization and energy consumption. Among existing SNN learning algorithms, spike-timing-dependent plasticity (STDP) is one of...

---

### 22. Sample-efficient Low-level Motion Planning for Robotic Manipulation Tasks via Zero-shot Transfer Learning

**Authors:** Yuanzhi He, Victor Romero-Cano, José J. Patiño, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06041v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06041v1)

**Summary:** As robotic systems become more sophisticated, the growing complexity of their motion planning models and the longer training times pose substantial challenges. Evolutionary algorithms such as the Sample-efficient Cross-Entropy Method (iCEM) have recently demonstrated promising potential for low-level real-time planning by leveraging efficient knowledge reuse strategies to improve performance. Although effective in many control tasks, iCEM's performance can be constrained in more complex scenario...

---

### 23. Depth over Fidelity in Fixed-Budget Noisy Evolution Strategies

**Authors:** Sichen Wang, Zhipeng Lu

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06555v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06555v1)

**Summary:** Noisy evolution strategies under fixed evaluation budgets face a depth-fidelity trade-off: spending evaluations to denoise intra-generation rankings reduces the number of distribution updates the optimizer can execute. We argue for depth over fidelity and propose probabilistic elite membership (PEM), which replaces hard rank-based weights in evolution strategies with conditional expected rank weights that integrate over ranking uncertainty. PEM preserves the conditional mean update while reducin...

---

### 24. Quantifying Uncertainty In Wide Two-Layer Neural Networks: On The Law Of The Limiting Fluctuation Process

**Authors:** Arnaud Descours, Arnaud Guillin, Geoffrey Lacour, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05982v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05982v1)

**Summary:** Uncertainty quantification in neural networks prediction is a main issue for usual applications. Our approach seeks at reducing computation costs by directly evaluating uncertainty using PDE's information on the asymptotic variance, rather than the deep ensemble method which may be seen as a Monte Carlo estimation of the prediction, requiring the training of multiple networks. We thus study the law of the limiting process describing the random fluctuations around the mean-field limit of wide two...

---

### 25. Synthetic Benchmarks Overstate Forward-Forward Scaling: Real-Data Limits of Layer-Local Training

**Authors:** Yucheng Chen

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06539v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06539v1)

**Summary:** Forward-Forward (FF) learning [Hinton, 2022] replaces backpropagation with strictly layer-local goodness updates. Recent FF-CNN work has narrowed the gap to BP on 32x32 benchmarks, raising the question of whether layer-local training is becoming a viable alternative at realistic scale. To probe this rigorously, we develop DTG-FF -- dynamic temperature goodness, decoupled normalization, and multi-layer fusion -- as an instrument that sets FF-family state of the art across nine real-data benchmark...

---

### 26. From Prediction to Self: Developmental Conditions for Agency in Minimal Neural Systems

**Authors:** Evan Ye

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05605v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05605v1)

**Summary:** How does a system that merely predicts the world come to distinguish its own causal influence from everything else? We trace this transition in a minimal 192-dimensional GRU through 40 controlled experiments arranged as a developmental sequence, adding components one at a time and tracking whether the system can distinguish self-caused from world-caused changes.   The developmental path reveals four conditions that must be satisfied in strict order: (1) persistent state forming stable attractors...

---

### 27. Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution

**Authors:** Can Gurkan, Forrest Stonedahl, Uri Wilensky

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.05408v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05408v1)

**Summary:** When an LLM repeatedly mutates a program, does it explore new forms or circle back to the same ones? We study this question by analyzing LLM-driven mutation chains in the absence of selection pressure within a domain-specific language, varying prompt design, model family, and stochastic replication. We find that LLM-based mutation consistently converges toward restricted attractor regions in program space. Convergence is especially severe at the structural level: in 87% of chains, over 93% of mu...

---

### 28. Seq103: A Unified Neuroevolution Framework for Compact Sequence Architecture Discovery

**Authors:** Wenxiao Li, Yongjian Liu, Qing Xie

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.07664v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07664v1)

**Summary:** Neuroevolution is a representative neural architecture search paradigm that evolves both network topology and weights through evolutionary algorithms. In this paper, we propose Seq103, a unified NEAT-style neuroevolution framework for compact sequence architecture discovery. Seq103 consists of a shared evolutionary backbone and an optional recurrent extension. The shared backbone includes an elementary node-and-connection representation, per-class RMSE-based evaluation, mutation-based evolution ...

---

### 29. Multi-Column RBF Neural Network Using Adaptive and Non-Adaptive Particle Swarm Optimization

**Authors:** Ammar Hoori, Yuichi Motai

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.05150v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05150v1)

**Summary:** The radial basis function neural network (RBFN) trained with a gradient descending algorithm provides an effective fully connected structure in both shallow and deep networks. The error correction (ErrCor), a state-of-the-art gradient-based training method, selects optimal hidden units to improve accuracy. Alternatively, as a population-based algorithm, the particle swarm optimization algorithm (PSO) uses the swarm experience to optimize RBFN parameters, offering global search and robustness to ...

---

### 30. QDS-SNN: Energy-efficient Quantum Deeply-Supervised Spiking Neural Network Algorithm for Traffic Sign Recognition

**Authors:** Zhiguo Qu, Keqi Li, Le Sun, et al.

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.07657v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07657v1)

**Summary:** Traffic sign recognition is crucial for intelligent transportation and autonomous driving, as it can improve driving efficiency and ensure road safety. However, traditional recognition methods are based on large datasets and intensive computation, which limits their real-time applicability. Spiking Neural Networks (SNNs) offer a biologically inspired, energy-efficient alternative due to their spatiotemporal processing capabilities, but suffer from information loss and vanishing gradients during ...

---

### 31. U-Net-Accelerated Quality-Diversity Optimization for Climate-Adaptive Urban Layouts

**Authors:** Alexander Hagg, Tania Guerrero, Dirk Reith

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04658v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04658v1)

**Summary:** Optimizing urban layouts for climate adaptation requires balancing building density with cold-air ventilation. Because physics-based climate simulations are computationally expensive, planners typically evaluate fewer than ten manual designs. \gls{qd} algorithms offer a way to systematically illuminate the design space, but they require surrogate models to be practical.   In this paper, we replace a slow, regulatory physics simulator with a spatial deep-learning surrogate (U-Net) inside an offli...

---

### 32. Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning

**Authors:** Damian Lebiedź, Robert Ślepaczuk

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04574v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04574v1)

**Summary:** This study aims to determine whether the application of Deep Reinforcement Learning (DRL) as a specialized execution overlay can enhance pair trading in highly volatile cryptocurrency markets. Although classical implementations of the strategy have proven successful in traditional equities, they frequently exhibit rigidity and suffer from severe divergence risks when applied to high-variance environments. To address this need, this research introduces novel concepts. To construct a robust system...

---

### 33. ParetoPilot: Zero-Surrogate Offline Multi-Objective Optimization via Infer-Perturb-Guide Diffusion

**Authors:** Ruiqing Sun, Sen Yang, Dawei Feng, et al.

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04468v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04468v1)

**Summary:** Offline multi-objective optimization (Offline MOO) aims to discover novel Pareto-optimal designs based on static datasets without expensive environment interactions. While recent generative methods have achieved notable success, they predominantly rely on external surrogate models. This dependency introduces significant computational overhead, suffers from deceptive evaluations, and deviates from the prevailing paradigm of jointly training mainstream generative models with conditions. To address...

---

### 34. Quadratic integrate-and-fire neurons exhibit less fragmented loss landscapes and outperform leaky integrate-and-fire neurons in spike-based gradient descent

**Authors:** Carlo Wenig, Raoul-Martin Memmesheimer, Christian Klos

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03935v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03935v1)

**Summary:** The ability to train spiking neural networks is essential for modeling biological neural networks as well as for neuromorphic computing. However, for the extensively used leaky integrate-and-fire (LIF) neurons, arbitrarily small parameter changes can induce spike (dis)appearances that disrupt subsequent activity, leading to unstable neural representations and permanently silent neurons during exact spike-based gradient descent. Recent work shows that a class of neuron models, which includes the ...

---

### 35. Calibrating Urban Traffic Simulation from Sparse Road Observations via Genetic Optimization

**Authors:** Hunter Sawyer, Jesse Roberts, Simon Matei

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03823v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03823v1)

**Summary:** Urban traffic simulation is a critical tool for infrastructure planning, including the placement of electric vehicle charging stations. However, realistic traffic simulation across many cities is hindered by two fundamental data limitations: detailed real-world traffic measurements are available for only a small fraction of road segments in most cities, and employment distribution data critical for modeling commuter traffic is rarely available at the resolution needed for simulation. This paper ...

---

### 36. Signed Spiking Neuron Enabled by an Orthogonal-Easy-Axis Magnetic Tunnel Junction

**Authors:** Huannan Zheng, Jingli Liu, Kezhou Yang

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03796v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03796v1)

**Summary:** Signed spiking neurons carry richer information than standard spiking neurons. This work proposes a compact magnetic tunnel junction (MTJ)-based neuron for signed leaky integrate-and-fire (LIF) operation. With orthogonal easy axes in the free and pinned layers, the device enables bipolar spike generation and maps magnetic-moment dynamics to signed LIF membrane-potential evolution. Landau--Lifshitz--Gilbert simulations show that proper free-layer dimensions allow the device response to follow a s...

---

### 37. Training a Predictive Coding Network on ImageNet using Equilibrium Propagation

**Authors:** Tugdual Kerjan, Rasmus Høier, Benjamin Scellier

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03584v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03584v1)

**Summary:** Equilibrium Propagation (EP) is a physics-based training framework that has primarily been employed in energy-based models, including continuous Hopfield networks, nonlinear resistive networks and coupled phase oscillators. However, EP's practical applications have so far remained limited to relatively small-scale problems. Predictive coding networks (PCNs), another class of energy-based models rooted in computational neuroscience, are typically trained with a specialized algorithm and have like...

---

### 38. Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics in a PFC-Inspired Reservoir Model for Multistep Goal-Directed Action Planning

**Authors:** Jin Nakamura, Yuichi Katori

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03481v1)

**Summary:** The prefrontal cortex (PFC) maintains goal information for action planning, but how recurrent circuits preserve it in an action-usable form over behavioral timescales remains unclear. Here we ask whether short-term synaptic plasticity (STP) can stabilize goal information as action-usable, goal-conditioned dynamics. We incorporated STP into a PFC-inspired reservoir computing model with basal-ganglia-inspired temporal-difference readout learning, and evaluated paired models with and without STP ac...

---

### 39. PrimeSVT: An Automated Memory-aware Pruning Framework with Prioritized Compression Policy for Spiking Vision Transformers

**Authors:** Rachmad Vidya Wicaksana Putra, Achyuta Muthuvelan, Alberto Marchisio, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03428v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03428v1)

**Summary:** The large sizes of Spiking Vision Transformers (SViTs) still hinder their embedded implementation, highlighting the need for model compression. State-of-the-art works compress SViT models through unstructured pruning, which needs specialized hardware accelerators for their specific sparsity patterns to maximize efficiency gains. Moreover, their manual approach requires a huge design time to find an appropriate pruning setting for each network, thus making this approach not scalable. To address t...

---

### 40. Optimizing Explicit Unit-Distance Lower-Bound Certificates

**Authors:** Michael T. M. Emmerich

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03419v5) | 📄 [PDF](https://arxiv.org/pdf/2606.03419v5)

**Summary:** The 2026 disproof of Erdős's unit-distance conjecture and Sawin's quantitative refinement show that the maximum number $u(n)$ of unit distances among $n$ planar points can exceed $n^{1+\varepsilon}$ for a fixed positive $\varepsilon$. Sawin's explicit bound gives more than $n^{1.014}$ unit distances for arbitrarily large $n$ and exposes integer parameters whose choice is not fully optimized. This report treats Sawin's parameter selection as a nonlinear integer optimization problem and develops a...

---

### 41. PSViT: A Methodology for Structurally Pruning Spiking Vision Transformers

**Authors:** Rachmad Vidya Wicaksana Putra, Achyuta Muthuvelan, Alberto Marchisio, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03257v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03257v1)

**Summary:** Spiking Vision Transformer (SViT) models are promising low-power ViT models for solving vision-based tasks with state-of-the-art performance. However, their large sizes limit their deployments for resource-constrained embedded platforms, underscoring the needs of model compression. One of prominent compression techniques is pruning, and the state-of-the-art works employ unstructured pruning techniques to compress SViT models. Such techniques require specialized hardware architectures tailored fo...

---

### 42. Beyond Static Priors: Dynamic Neural Guidance for Large-Scale Ant Colony Optimization

**Authors:** Dat Thanh Tran, Van Khu Vu, Yining Ma

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.04039v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04039v1)

**Summary:** Neural-guided Ant Colony Optimization (ACO) suffers from a fundamental training-inference misalignment: policies are typically trained to generate static priors (e.g., heatmaps), yet deployed to guide iterative, long-horizon search processes. In this paper, we present DyNACO, a novel framework that achieves dynamic neural guidance by periodically observing the pheromone distribution and the incumbent solution. To make DyNACO tractable at scale, we pair the policy with a perturbation-based ACO ba...

---

### 43. Spike-Aware C++ INT8 Inference for Sparse Spiking Language Models on Commodity CPUs

**Authors:** Ting Liu

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03026v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03026v1)

**Summary:** Spiking language models expose activation sparsity that dense Transformer runtimes do not directly exploit. This paper studies that property from a systems perspective. Building on the SymbolicLight V1 spike-gated language model family, we implement a C++ CPU inference runtime that treats sparse binary spike states as an execution primitive rather than only applying post-hoc weight compression. The runtime combines a manifest-driven weight loader, mixed row/column memory layout, AVX2/FMA kernels...

---

### 44. Self-Regulation through Communication in Evolved Neural Agents

**Authors:** Joshua Nunley

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02840v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02840v1)

**Summary:** Communication is typically understood as indication: signals that transfer information from sender to receiver. We present a minimal predator avoidance task in which pairs of evolved CTRNN agents use communication for robust survival, and in which agents hear their own vocalizations, as in natural systems. Across 112 perfect-fitness agents from over 2,000 evolutionary runs, three dominant strategies emerge (accounting for 81% of agents): safety calling (39%), where agents signal from safe cover;...

---

### 45. Simultaneous Model-Based Evolution of Constants and Expression Structure in GP-GOMEA for Symbolic Regression

**Authors:** Johannes Koch, Tanja Alderliesten, Peter A. N. Bosman

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02236v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02236v1)

**Summary:** Genetic programming (GP) approaches are among the state-of-the-art for symbolic regression, the task of constructing symbolic expressions that fit well with data. To find highly accurate symbolic expressions, both the expression structure and any contained real-valued constants, are important. GP-GOMEA, a modern model-based evolutionary algorithm, is one of the leading algorithms for finding accurate, yet compact expressions. Yet, GP-GOMEA does not perform dedicated constant optimization, but ra...

---

### 46. On the Evaluation of Spiking Neural Network Configurations for Network Intrusion Detection

**Authors:** Raj Patel, David Amebley, Taye Akinrele, et al.

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01442v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01442v1)

**Summary:** Network intrusion detection is a core component of modern cybersecurity infrastructure, yet the deep learning models that dominate the field are computationally demanding, motivating interest in lightweight alternatives suited to edge and neuromorphic deployment. Spiking Neural Networks (SNNs) are therefore a natural candidate, but their design space, spanning the choice of neuron model and spike encoding scheme, remains poorly characterized for intrusion detection. We bridge this gap by using a...

---

### 47. Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition

**Authors:** Tauseef Ahmed, Tao Sun, Jeronimo Castrillon, et al.

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01135v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01135v1)

**Summary:** Deep learning has greatly advanced automatic speech recognition (ASR), enabling widespread deployment on edge devices such as smartphones and smart home systems. However, the computational and energy demands of deep neural networks pose significant challenges for such resource-constrained deployments, introducing latency and limiting real-time interaction. Neuromorphic computing offers a promising solution by introducing activation sparsity through spiking neural networks (SNNs) and event-driven...

---

### 48. Breaking the Cascade: Compact Nonlinear Optical Computing with Single-Layer Encoder-Decoder Co-Localization

**Authors:** Yuntian Wang, Alexander Chen, Md Sadman Sakib Rahman, et al.

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01032v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01032v1)

**Summary:** We demonstrate that nonlinear computing can be achieved with a single linear diffractive surface under coherent illumination. We introduce a compact encoder-decoder co-localization (E+D) architecture in which an input-dependent dynamic encoder and a static optimized decoder are integrated within the same phase-only diffractive plane. Following free-space propagation, coherent interference between the encoder and decoder fields, combined with intensity detection, generates programmable nonlinear ...

---

### 49. Meta-Black-Box Optimization with Ensemble Surrogate Modeling for Robustness-Accuracy Trade-off within SAEA

**Authors:** Xiao Jin, Yongxiong Wang, Haobo Liu, et al.

**Published:** 2026-05-30

🔗 [Paper](http://arxiv.org/abs/2606.00862v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00862v1)

**Summary:** Surrogate-assisted evolutionary algorithms (SAEAs) have been widely used for expensive black-box optimization problems. However, their reliance on rigid and manually designed components limits their flexibility and generalization across tasks. Meta-black-box optimization (MetaBBO) provides a promising paradigm for adaptively configuring algorithmic components. Nevertheless, existing MetaBBO methods usually control only a single component, and few studies have investigated the unified control of ...

---

### 50. Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs

**Authors:** Subhadip Mitra

**Published:** 2026-05-30

🔗 [Paper](http://arxiv.org/abs/2606.00813v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00813v1)

**Summary:** Safety alignment in LLMs does not improve monotonically across model generations. Studying four generations of Google's Gemma family (7B-31B) with quality-diversity evolution (MAP-Elites) as an automated red-teaming probe, we find that Gemma 3 (12B) exhibits 68.7% +/- 5.7% attack success rate (ASR; mean +/- std, 3 seeds), significantly higher than its predecessor Gemma 2 (45.5% +/- 7.2%; p = 0.030, paired bootstrap) and its successor Gemma 4 (33.9% +/- 1.8%). Replaying evolved attack archives ac...

---

## q-bio.NC

**50 papers**

### 1. QUIET: Quantifying Underutilized Influential Edges for Targeted Synchronization

**Authors:** Sovesh Mohapatra, Christoffer G. Alexandersen, Panagiotis Fotiadis, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11091v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11091v1)

**Summary:** Network control theory can be used to model intrinsic and extrinsic strategies to steer neural dynamics. Standard approaches are node-centric, structural, and focused on achieving desired instantaneous states. Here, we develop an edge-centric approach which incorporates both structure and function to achieve extended patterns of neural dynamics characterized by desired synchronization states. Our method, Quantifying Underutilized Influential Edges for Targeted Synchronization (QUIET), is an edge...

---

### 2. GRAFT: Gain-Recalibrated Adapters for Transformer-Based Neural Population Activity Modeling

**Authors:** Xiangsheng Ge, Yang Xie

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11066v1)

**Summary:** Neural population activity models can recover rich temporal structure from binned spikes, but their read-in and readout layers often remain tied to a fixed set of recorded neurons. This coupling limits reuse in long-term brain-computer interfaces, where recorded neuron identities, counts, and response statistics can change across days. We introduce GRAFT, a Transformer-based neural population activity model that separates reusable temporal dynamics from a recalibratable neuron interface. The neu...

---

### 3. Bilinear gating of motor primitives: a principle linking dendritic computation to rapid goal-directed adaptation

**Authors:** Cristiano Capone, Luca Falorsi, Andrea Ciardiello, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10891v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10891v1)

**Summary:** Movement requires the motor cortex to specify both \emph{what} action to produce and \emph{which goal} it serves, yet how individual neurons separate these factors is not understood. Here we show that in macaque motor cortex the \emph{burst fraction} of a neuron, the proportion of its spikes emitted in high-frequency bursts, encodes reach direction far more selectively than its overall firing rate. This dissociation is highly consistent: it holds in every one of 12 recording sessions spanning th...

---

### 4. Sleep EEG Signal Criticality as a Non-Invasive Predictor of Cognitive Decline in Dementia

**Authors:** Stanisław Narębski, Tomasz Komendziński, Tomasz M. Rutkowski

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10889v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10889v1)

**Summary:** Early detection of neurodegeneration remains a critical clinical challenge. This study investigates whether sleep EEG signal criticality, quantified via Multifractal Detrended Fluctuation Analysis (MFDFA), serves as a non-invasive biomarker for future cognitive decline. We analyzed longitudinal data from the National Sleep Research Resource (NSRR) Study of Osteoporotic Fractures (SOF) cohort, comparing baseline sleep EEG dynamics between women who remained cognitively normal and those who later ...

---

### 5. Hyperbolic Neural Population Geometry Benefits Computation

**Authors:** Dennis Wu, Yi-Chun Hung, Braden Yuille, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10238v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10238v1)

**Summary:** Neural population geometry shapes downstream computation. Recent empirical findings in neurobiology suggest that a hyperbolic structure underlies population activity in the hippocampus. Here we provide a theoretical framework for this phenomenon. First, we propose a plausible construction of hippocampal tuning curves that statistically induces hyperbolic geometry. Next, we establish a connection between neural decoding and associative memory by demonstrating that the Modern Hopfield Network upda...

---

### 6. Multifractal Signatures of Ageing and Dementia Development: A Multifractal Space-Filling Curve Analysis

**Authors:** Marta Lotka, Jacek Grela, Zbigniew Drogosz, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10222v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10222v1)

**Summary:** Multifractality is an effective formalism for quantifying the nonlinear, scale-free properties of complex data. In this study, we propose a novel and efficient methodology, termed Multifractal Space-filling Curve Analysis (MFSCA), for quantifying the correlation structure of multidimensional data. Within this framework, the original multidimensional data - while preserving both local and long-range organisational properties - are projected onto a one-dimensional representation using a fractal sp...

---

### 7. Discovering Functionally Selective Brain Regions with a Deep Topographic Multimodal Model

**Authors:** Badr AlKhamissi, Johannes Mehrer, Lara Marinov, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09770v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09770v1)

**Summary:** Nearby neurons in cortex share similar response profiles, producing systematic spatial organization across sensory and cognitive systems. Recent topographic models reproduce aspects of this structure but remain unimodal and spatially constrain each layer separately, yielding fragmented maps that capture neither the contiguity of cortical processing streams nor their integration across modalities. We introduce Topo-Omni, a topographic multimodal model in which visual, auditory, and language/cogni...

---

### 8. Predictable Mean-Field Chaos in Random Recurrent Networks

**Authors:** Alkesh Yadav, Vladimir Shaidurov, Jonathan Kadmon

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08805v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08805v1)

**Summary:** Dynamical mean-field theory recasts deterministic chaos in random recurrent networks as an effective stochastic process. We show that for analytic nonlinearities with sufficiently fast Fourier decay, this stochasticity is only apparent: the continuous past of a realized mean-field trajectory uniquely determines its future. The mean-field theory is therefore not merely an ensemble description, but a conditional prediction theory for individual trajectories. Unfolding the power spectrum into a Kry...

---

### 9. This is how the Neocortex Learns

**Authors:** Randall C. O'Reilly

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08720v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08720v1)

**Summary:** A sufficient account of how the neocortex learns must meet three criteria: 1. Computationally, it must approximate a powerful, general-purpose learning algorithm known to scale to human-level intelligence; 2. Algorithmically, it must be implementable using known, well-established neural circuits within the neocortex and associated brain structures; 3. Implementationally, there must be a detailed account for how all of the algorithmic mechanisms actually function at a neurochemical level. At pres...

---

### 10. Vector Space of Cycles

**Authors:** Moo K. Chung, Anass B. El-Yaagoubi, Hernando Ombao

**Published:** 2026-06-06

🔗 [Paper](http://arxiv.org/abs/2606.08202v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08202v1)

**Summary:** Most statistical and machine learning methods for directed interactions focus on pairwise effects among variables. Even existing cyclic models represent feedback primarily through node-level dependencies, making large-scale recurrent organization difficult to estimate and compare. This limitation is particularly acute in biological and neural systems, where interactions are highly recurrent and involve many overlapping cycles. We introduce a variational framework for statistical inference on cyc...

---

### 11. Reconstructing and forecasting disease trajectories of patients with Alzheimer's disease using routine data in resource-constrained settings

**Authors:** Ratnadeep Das, Atri Chatterjee, Sitikantha Roy

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07798v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07798v1)

**Summary:** Alzheimer's disease is a progressive neurodegenerative disorder, and its progression varies substantially across patients. Existing work aims to forecast patients' future cognitive state, with minimal focus on reconstructing the state from past visits. Furthermore, in current research, quantifying predictive uncertainty remains underexplored and relies on costly modalities such as MRI, PET, and CSF, limiting their deployment in resource-limited settings. In this research, our primary objectives ...

---

### 12. Fixed point compositionality via low-rank gluing rules in inhibition-dominated threshold-linear networks

**Authors:** Juliana Londono Alvarez

**Published:** 2026-06-05

🔗 [Paper](http://arxiv.org/abs/2606.07336v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07336v1)

**Summary:** Brains routinely generate highly flexible and complex behaviors on a relatively stable structure and limited resources. A key mechanism underlying this ability is compositionality, which allows the brain to efficiently decompose complex tasks into simpler, reusable primitives. While network modularity has often been linked to compositionality in biological and artificial networks, a rigorous mathematical characterization of this relationship in nonlinear networks is still lacking. In this work, ...

---

### 13. The Identity Trap in EEG Foundation Models: A Diagnostic Audit

**Authors:** Jun-You Lin, Ying Choon Wu, Tzyy-Ping Jung

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06647v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06647v1)

**Summary:** Objective. EEG foundation models (FMs) report strong accuracy on clinical resting-state EEG. However, high accuracy under subject-disjoint cross-validation remains ambiguous: it can reflect a genuine clinical biomarker, or subject-identity features that correlate with the label. We name this the Identity Trap and ask whether it can be diagnosed at the representation level before fine-tuning.   Approach. We propose FMScope, a frozen-representation protocol packaging five diagnostics: variance dec...

---

### 14. Simultaneous hyperkinetic movement disorders phenotyping: a cross-cohort pediatric transfer study using routine videos, markerless pose estimation and a tabular foundation model

**Authors:** Laura Cif, Diane Demailly, Zohra Souei, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.07674v1) | 📄 [PDF](https://arxiv.org/pdf/2606.07674v1)

**Summary:** Objective: To develop and externally test a video-based framework for simultaneous detection of hyperkinetic MDs phenomenologies: dystonia, tremor, myoclonus, chorea, athetosis, ballismus, stereotypies, and tics using routine clinical recordings, with explicit testing of external, cross-cohort transfer from adult to pediatric populations. Methods: In this proof-of-concept study, the framework combines markerless pose estimation, kinematic descriptors, and a pretrained fondation model. A shared p...

---

### 15. Intrinsic Computational Functionalism: From Observer-Relative Maps to Observer-Independent Structures

**Authors:** Shuqin Ma, Ryota Kanai

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06424v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06424v1)

**Summary:** Anti-computational arguments show that externally imposed computational interpretations cannot ground consciousness, but they do not establish that all computational organisations are observer-relative. We develop intrinsic computational functionalism: the view that, if consciousness is computationally constituted, it depends on physically realised computational structures the system has in virtue of itself rather than on labels imposed by an external interpreter. Two criteria operationalise thi...

---

### 16. Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation

**Authors:** Yohann Benchetrit, Marlène Careil, Simon Dahan, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06345v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06345v1)

**Summary:** Brain decoding is limited by the availability of labeled neural data, and remains challenging in low-data regimes. To address this issue, we investigate whether and when brain decoding can be boosted by augmenting small fMRI datasets with synthetic data generated by a pretrained model of fMRI responses to stimuli. We use TRIBE v2, a large encoding model pretrained on more than 1000 hours of fMRI responses to video, audio and language. For each dataset, we evaluate systematic grids that show how ...

---

### 17. Early psychosis shows deviations in scaling behaviour within a critical regime

**Authors:** Irem Topal, Paola Moreno Ancalmo, Guillermo Montana Valverde, et al.

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.06290v1) | 📄 [PDF](https://arxiv.org/pdf/2606.06290v1)

**Summary:** Accumulating evidence suggests that large-scale brain activity exhibits scale-invariant dynamics consistent with operation in a near-critical regime. Such dynamics have been associated with long-range correlations, efficient information processing, and the emergence of collective organization. While altered criticality-related measures have been reported in psychiatric disorders, previous findings remain fragmented across observables and modalities, making it unclear whether different scaling me...

---

### 18. Cross-scale spatially-aware generative modeling of transcriptomic programs underlying neurodegenerative brain organization

**Authors:** Krishnakumar Vaithianathan

**Published:** 2026-06-04

🔗 [Paper](http://arxiv.org/abs/2606.05870v1) | 📄 [PDF](https://arxiv.org/pdf/2606.05870v1)

**Summary:** Neurodegenerative disorders such as Alzheimer's disease exhibit highly organized patterns of regional brain vulnerability, yet the biological mechanisms underlying this spatial selectivity remain incompletely understood. Existing imaging-transcriptomic studies have largely relied on correlation-based analyses between gene expression and neuroimaging phenotypes, limiting their ability to model how molecular organization gives rise to neurodegeneration. Here, we introduce a cross-scale spatially-a...

---

### 19. Discrete signaling mediates chaotic regularization in recurrent neural networks

**Authors:** Jan Bauer, Christian Keup, Jonathan Kadmon, et al.

**Published:** 2026-06-03

🔗 [Paper](http://arxiv.org/abs/2606.04426v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04426v1)

**Summary:** Cortical circuits operate in a regime of intrinsic chaos, where even tiny changes in input can lead to divergent neural responses. Yet, remarkably, population codes in the brain vary smoothly with sensory stimuli, forming coherent representational manifolds. How can chaotic networks sustain such stable coding? Here, we develop a theoretical framework that links the microscopic chaos of recurrent networks to the macroscopic geometry of neural representations. Combining kernel methods with dynamic...

---

### 20. Formalizing the Binding Problem

**Authors:** Lianghuan Huang, Yihao Li, Saeed Salehi, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03976v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03976v1)

**Summary:** Representations of the world, arguably, contain information about features (e.g. something is blue, something is a circle) but also information about which features are part of the same object (e.g. the circle is blue), which we call binding information. Any system with the ability to understand scenes with multiple objects must be able to solve the binding problem: it needs to know which features belong together. However, despite work showing that Vision Transformers (ViTs) know which patches b...

---

### 21. Who Is in Mind Matters: Attachment Representations in Early Childhood Synchronize Child-Adult Interacting Brains

**Authors:** Ruxin Su, Jiayang Xu, Saishuang Wu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03700v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03700v1)

**Summary:** Human attachment is distinguished by enduring internalized representations that shapes neurodevelopment and social-emotional functioning. However, as unobservable inner processes mixed with social cues and partner-specific factors, the neurocognitive mechanisms of these representations during real-time interaction remain unclear. Using a novel Remote Partner-Belief Manipulation paradigm in 40 child-mother-stranger trios, we experimentally isolated attachment representations in 3-4-year-olds by m...

---

### 22. SC-TauPath: A Structural Connectivity Attribution Framework for Mapping Tau Propagation Pathways in Alzheimer's Disease

**Authors:** Jing Zhang, Norman Scheel, Minheng Chen, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.04066v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04066v1)

**Summary:** Understanding how structural connections are associated with tau propagation in Alzheimer's disease (AD) remains a central open question, yet existing computational models either rely heavily on biophysical assumptions or lack neurobiologically interpretable pathway maps. We present SC-TauPath, a structural connectivity (SC) attribution framework that maps tau propagation pathways from in vivo neuroimaging data. SC-TauPath combines a Network Diffusion Model (NDM)-augmented multilayer perceptron ...

---

### 23. Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics in a PFC-Inspired Reservoir Model for Multistep Goal-Directed Action Planning

**Authors:** Jin Nakamura, Yuichi Katori

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03481v1)

**Summary:** The prefrontal cortex (PFC) maintains goal information for action planning, but how recurrent circuits preserve it in an action-usable form over behavioral timescales remains unclear. Here we ask whether short-term synaptic plasticity (STP) can stabilize goal information as action-usable, goal-conditioned dynamics. We incorporated STP into a PFC-inspired reservoir computing model with basal-ganglia-inspired temporal-difference readout learning, and evaluated paired models with and without STP ac...

---

### 24. A formal definition and meta-model for a machine theory of mind

**Authors:** Fabio Cuzzolin

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03471v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03471v1)

**Summary:** This paper proposes, for the first time, a rigorous formal definition of the concept of Machine Theory of Mind, based on principles supported by evidence from cognitive psychology, neuroscience and artificial intelligence, and uses the above as a lens to examine state-of-the-art and current efforts in the field, driving a potential agenda for further research there able to "crack" the problem. It also advances a general holistic meta-model for Machine Theory of Mind, and examines the state of th...

---

### 25. Learning to See via Epiretinal Implant Stimulation in silico with Model-Based Deep Reinforcement Learning

**Authors:** Jacob Lavoie, Marwan Besrour, William Lemaire, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03118v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03118v1)

**Summary:** Objective: Diseases such as age-related macular degeneration and retinitis pigmentosa cause the degradation of the photoreceptor layer. One approach to restore vision is to electrically stimulate the surviving retinal ganglion cells with a microelectrode array such as epiretinal implants. Epiretinal implants are known to generate visible anisotropic shapes elongated along the axon fascicles of neighboring retinal ganglion cells. Recent work has demonstrated that to obtain isotropic pixel-like sh...

---

### 26. BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting

**Authors:** Yanchen Wang, Lenny Aharon, Wangshu Zhu, et al.

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02937v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02937v1)

**Summary:** Multi-view video recordings are increasingly used to capture the 3D movements of animals in experimental settings, yet extracting rich 3D representations from these recordings remains challenging. Supervised pose estimation requires extensive manual annotation, while general-purpose 3D reconstruction models trained on generic scene datasets fail on the specialized imagery and sparse-view setting of laboratory experiments. We address these limitations with BEAST3D, a self-supervised pretraining f...

---

### 27. Topology as Logic: Structural Role Geometry Across Formal, Software, Biological, and Prebiotic Systems

**Authors:** Vladi Ivanov

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02392v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02392v1)

**Summary:** We ask whether dependency topology correlates with functional load-bearing organization as recoverable geometry -- not as a metaphor, but as a measurable structural property detectable by multilayer network analysis. Across seven independent substrates, we show that hub persistence and rank divergence under the Functional Proximity Law recover operational organization that domain experts describe as logic: axiomatic load-bearing structure in formal mathematics, control and contract structure in ...

---

### 28. How Optimality Structures Sparse Dictionaries: A Theory for Understanding SAE Representations

**Authors:** William Dorrell

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02385v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02385v1)

**Summary:** Sparse Autoencoders (SAEs) have found success parsing neural representations into interpretable concepts, providing a basis for understanding and control. However, what exactly SAEs extract, and, correspondingly, the scientific conclusions we can draw from them, are not obvious. Empirically, the proof is in the pudding: SAEs learn interpretable features. Theoretically, we lack a clear account of what properties a 'concept' must satisfy for an SAE to extract it. There has been extensive identifia...

---

### 29. Mapping Whisper Representations to Human ECoG Responses with Interpretable Time-Resolved Neural Encoding

**Authors:** Matteo Ciferri, Tommaso Boccato, Michal Olak, et al.

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02305v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02305v1)

**Summary:** Understanding how speech foundation models relate to human cortical activity is a key challenge for computational neuroscience. Here, we investigate how internal representations from Whisper predict intracranial ECoG responses during naturalistic speech perception. We introduce a time-resolved neural encoder that combines speech embeddings with a recurrent temporal model and soft attention, allowing us to examine layer-wise brain alignment. Intermediate Whisper layers provide the strongest corre...

---

### 30. What biology can, and cannot, tell us about conscious AI

**Authors:** Ulysse Klatzmann, Adrien Doerig

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02121v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02121v1)

**Summary:** Progress in AI is turning machine consciousness from a philosophical curiosity into a societal issue, and has led to criticism of the widespread computational functionalism framework. Biological Naturalism (BN) claims that biology, not computation, is crucial for consciousness. We discuss which forms of BN are empirically testable. For Type-A-BN, biology intrinsically matters for consciousness, without affording unique information processing capabilities. We argue, similarly to the unfolding arg...

---

### 31. Unveiling the shared grey matter signature between Alzheimer's and Parkinson's Disease

**Authors:** Vishaak Gangasandra, Finn Blain, Elise Delzant, et al.

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.02099v1) | 📄 [PDF](https://arxiv.org/pdf/2606.02099v1)

**Summary:** INTRODUCTION. This study presents the first quantification of vertex-level grey-matter associations between Alzheimer's disease (AD) and Parkinson's disease (PD) using highresolution brain maps aggregated from large MRI datasets. The aim is to identify shared neuroanatomical signatures between the two diseases.  METHODS. Leveraging a novel statistical framework (SumR2 regression), adapted from genetic correlation analysis, we estimated the shared neuroanatomical signature (grey-matter correlatio...

---

### 32. The Neuromorphic Supremacy

**Authors:** Yuliya Tsybina, Ivan Y. Tyukin, Alexander N. Gorban, et al.

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.01841v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01841v1)

**Summary:** Live neural systems demonstrate remarkable capabilities to learn new behavior and patterns from mere few examples and are known to operate robustly under severe sensory noise. These capabilities, however, remain largely out of reach for modern artificial neural networks, including deep learning models. We show that this gap can be bridged by embedding novel genuine neuromorphic circuits into conventional artificial neural network architectures. These circuits comprise astrocytic modulation and s...

---

### 33. Feature leakage and the identifiability of direct-dependency entropy models of neural activity

**Authors:** Houman Safaai, Bernardo L. Sabatini

**Published:** 2026-06-01

🔗 [Paper](http://arxiv.org/abs/2606.01661v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01661v1)

**Summary:** Biological neurons receive thousands of synaptic inputs on branching, electrically excitable dendrites, yet population activity is often modeled with direct input-output rules in which each input contributes independently to a scalar drive. We study what successful prediction by such models does, and does not, reveal about neural computation. For conditional maximum-entropy models that match output rates and pairwise output-input coactivities, the entropy explained by a direct model is a predict...

---

### 34. Hypergraphs from multivariate connectivity: caCoh-based EEG/MEG representation

**Authors:** Daniil Vlasenko, Irina Saranskaia, Denis Zakharov

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01357v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01357v1)

**Summary:** Hypergraphs provide a natural framework for representing neurophysiological interactions distributed across sets of sensors. A key methodological question is how hyperedges should be defined from frequency-resolved electroencephalography/magnetoencephalography (EEG/MEG) data. We demonstrate a construction strategy in which hyperedges are obtained from canonical coherence (caCoh), an extension of coherence that estimates coupling between multidimensional signal spaces. To our knowledge, this is t...

---

### 35. A 1000-hour EEG-EMG-audio dataset of Japanese speech production

**Authors:** Motoshige Sato, Ilya Horiguchi, Masakazu Inoue, et al.

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01264v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01264v1)

**Summary:** We present a multimodal dataset of 1020 hours of simultaneously recorded scalp electroencephalography (EEG), facial electromyography (EMG), and speech audio from three healthy native Japanese speakers during open-vocabulary overt speech. Recordings were acquired with three EEG systems-an ultra-high-density system (g.Pangolin) and two cap-type systems (g.SCARABEO and eegosports), spanning 62-128 channels-across many sessions over several months. Each session provides time-synchronized EEG, facial...

---

### 36. DAGGER: Gradient-Free Construction of Transiently Amplifying Networks under Hard Connectivity Constraints

**Authors:** James C. Ferguson

**Published:** 2026-05-31

🔗 [Paper](http://arxiv.org/abs/2606.01227v1) | 📄 [PDF](https://arxiv.org/pdf/2606.01227v1)

**Summary:** Many networks not only support but also rely on transient non-normal amplification, an orders-of-magnitude increase in the activity of an otherwise stable system. Constructing such networks under hard sign/sparsity/diagonal constraints -- the regime relevant for biological connectomes and structured RNN initializations -- has so far required either gradient-based local search with thousands of inner-loop eigendecompositions or Schur-form direct construction in an abstract basis that breaks the c...

---

### 37. Towards an Ideometrics-Based Understanding of Consciousness, Time, Space and Dreams

**Authors:** Igor Rudan

**Published:** 2026-05-30

🔗 [Paper](http://arxiv.org/abs/2606.04011v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04011v1)

**Summary:** From an ideometrics-based perspective, consciousness may reduce the informational entropy of many randomly possible future outcomes through ideometric processes. Consciousness enables a system to internally simulate alternative futures and then voluntarily act, based on ideometric processes, towards realising preferred states in external reality. This may explain why most humans gravitate towards futures that minimise threat and maximise survival, reproduction, safety and well-being. Ideometrics...

---

### 38. Cortex and subcortex play distinct roles over learning when cortical memory is limited

**Authors:** Matthew Farrell, Taro Toyoizumi

**Published:** 2026-05-30

🔗 [Paper](http://arxiv.org/abs/2606.00667v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00667v1)

**Summary:** It has been proposed that the brain integrates flexible, computationally expensive cortical processing with simpler, lower-cost subcortical mechanisms to achieve resource-efficient performance greater than that of either system alone. Despite the allure of this perspective, satisfying theoretical frameworks that explore this hypothesis are still limited. We extend existing frameworks in which a model-based module and model-free module learn in tandem by explicitly constraining the memory resourc...

---

### 39. The Variance Brain Foundation Models Forgot: Third-Order Statistics Predict Cognition Where Billion-Parameter Models Fail

**Authors:** Giovanni Marraffini, Gabriel Mahuas, Trinidad Borrell, et al.

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2606.04010v1) | 📄 [PDF](https://arxiv.org/pdf/2606.04010v1)

**Summary:** Brain foundation models (BFMs) are self-supervised Transformers pretrained on fMRI data. We posit that these models should capture each subject's cognitive performance from their fMRI signal. Yet across three state-of-the-art BFMs and every readout we test, they predict cognition worse than a linear regression from the $\sim$80K parameters of the functional connectivity matrix (FC). The gap widens with scale: BrainLM's 650M model predicts cognition worse than its 111M. We attribute this to a \te...

---

### 40. Sequential chaotic oscillations in excitatory-inhibitory threshold-linear networks

**Authors:** Jie Zang, Carina Curto

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2606.00373v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00373v1)

**Summary:** Metastable states, a phenomenon observed in brain dynamics and many other systems, have been proposed as a key feature of healthy brain function, reflecting a balance between integration and segregation. However, it remains unclear how to capture this behavior within a dynamical-systems framework. In this paper, we propose sequential chaotic oscillations (SCOs), arising in excitatory-inhibitory threshold-linear networks (E-I TLNs), as a candidate dynamical mechanism for sequential metastability....

---

### 41. On the synaptic matrix eigenvalues of sparsely connected neural networks

**Authors:** Mohd. Gayas Ansari, Pragya Shukla

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2606.00326v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00326v1)

**Summary:** The spectral behaviour of the synaptic matrix, representing the neuronal connection strengths, is an important tool to analyze the stability and transient dynamics of a typical brain as well as its learning process and memory capacity. The complexity of the brain due to large number of neurons as well as underlying transient mechanisms e.g. homeostasis, seizure or synaptic plasticity can lead to networks with time-varying degree and type of sparsity. This renders an exact determination of the sy...

---

### 42. Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks

**Authors:** Ezekiel Williams, Alexandre Payeur, Guillaume Lajoie

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2606.00243v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00243v1)

**Summary:** Biological and neuromorphic recurrent neural networks (RNNs) are subject to spatial and temporal locality constraints on the information that can plausibly be used during learning. A common strategy to satisfy these constraints is to modify gradient descent by neglecting non-local terms to varying degrees, as in random feedback local online (RFLO) learning and truncated backpropagation through time (tBPTT). However, the learning dynamics of these algorithms, and how they compare with BPTT, remai...

---

### 43. Consciousness, AI, and the Limits of Scientific Explanation

**Authors:** Bradley C. Love

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2606.00226v1) | 📄 [PDF](https://arxiv.org/pdf/2606.00226v1)

**Summary:** Science is constitutively third-personal: its findings are in principle reproducible by any observer, independent of perspective, and answerable to measurement. This is the source of its power and also its limit when it comes to phenomena that are first-personal. While it is obvious that a science of the Meaning of Life is unattainable, researchers have not drawn the same conclusion for consciousness -- in its phenomenal dimension, the qualia of seeing red, of feeling pain, of being anything at ...

---

### 44. The Metastable Mind: Neural Underpinnings of Naturalistic Cognition Through the Synthesis of Event Segmentation and Metastable Neural States

**Authors:** Dora Gozukara, Nasir Ahmad, Djamari Oetringer, et al.

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.31473v1) | 📄 [PDF](https://arxiv.org/pdf/2605.31473v1)

**Summary:** A multitude of findings and theories from cognitive, behavioural and computational neuroscience show that neural activity unfolds in a variety of meaningful temporal units. Behavioural research on event segmentation (ES) has shown that continuous experience is segmented into discrete events and sub-events, which aid real-time comprehension, memory, and decision-making. Computational neuroscience research observes and models ongoing brain activity as a series of stable population activity that oc...

---

### 45. Extended predictive coding framework as variational free-energy minimisation under exponential-family assumption

**Authors:** Asaki Kataoka, Kenji Doya

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.30882v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30882v1)

**Summary:** The sensory cortices of the brain perform perceptual inference efficiently through their complex networks of neurons. One of the theoretical accounts of this process is the free-energy principle (FEP), which postulates that the brain performs variational Bayesian inference. Pioneering studies have shown that FEP can correspond to the predictive coding (PC) hypothesis under the Gaussian assumption and Laplace approximation. However, PC-based implementations of FEP within such a limited Gaussian r...

---

### 46. What makes an action sequence enjoyable to watch?

**Authors:** Jean-Peïc Chou, Kristine Zheng, Junyi Chu, et al.

**Published:** 2026-05-29

🔗 [Paper](http://arxiv.org/abs/2605.30864v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30864v1)

**Summary:** People often seek out ways to watch others perform complex action sequences (e.g., sports). What makes some sequences more enjoyable to watch than others? We generated 24 video clips of gameplay from a Flappy Bird-style video game. Clips varied in difficulty (how often players succeeded on average) and in moment-to-moment uncertainty (how likely the player was to crash at any given step). Participants (N=864) rated each video on one of three dimensions: how much they enjoyed it, how difficult th...

---

### 47. Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules

**Authors:** Nils Leutenegger

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.30556v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30556v1)

**Summary:** Random, untrained neural networks consistently match or exceed trained networks in representational similarity to early visual cortex. This puzzling finding challenges the assumption that learning improves brain alignment. We investigate it by tracking representational similarity analysis (RSA) alignment to human fMRI data across training for four learning rules: backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP). Using 720 object ...

---

### 48. High-Fidelity 3D Simulator for Synthetic fNIRS Data Generation

**Authors:** Condell Eastmond, Niels Bracher, Xavier Intes, et al.

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.30552v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30552v1)

**Summary:** Functional near-infrared spectroscopy (fNIRS) provides a noninvasive window into brain activity by measuring task-related changes in oxygenated and deoxygenated hemoglobin in the cortex. A key advantage of fNIRS is its promise of use with mobile participants in complex, real-world environments, such as walking, sports, classroom learning, driving simulations, or social interactions. However, analyzing fNIRS data is challenging because of motion artifacts, physiological noise, and other confoundi...

---

### 49. Private Noise and Public Error in Collective Information Acquisition

**Authors:** Mohammad Salahshour, Sumanth Bhargava, Kajal Kumari, et al.

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.30522v1) | 📄 [PDF](https://arxiv.org/pdf/2605.30522v1)

**Summary:** Collective information acquisition requires groups to combine personal evidence with social information while remaining coupled to the external state. Communication noise can affect this process, but the role of noise remains unclear. In an online experiment, 600 participants worked in four-person human groups estimating a room temperature across 25 rounds while receiving either faithful social information, comprehension noise in which each receiver saw independently perturbed social information...

---

### 50. Subcortical Shape Variations and Their Associations with Cognition Across the 8th Decade of Life. A Study in the Lothian Birth Cohort 1936

**Authors:** Maria del C. Valdes-Hernandez, Wonjung Park, Joanna Moodie, et al.

**Published:** 2026-05-28

🔗 [Paper](http://arxiv.org/abs/2605.29703v1) | 📄 [PDF](https://arxiv.org/pdf/2605.29703v1)

**Summary:** The study of brain morphology changes in normal individuals may capture aspects of functionally-relevant brain aging not fully indicated by gross volumetry. Despite the important role of subcortical brain structures in cognition, the associations between their morphological trajectories and cognitive changes in aging have not been documented. We use neuroimaging, demographic, and cognitive data from a large longitudinal study of cognitive aging, the Lothian Birth Cohort 1936, to explore shape ch...

---

## stat.ML

**50 papers**

### 1. Itô maps for any-step SDEs

**Authors:** Zhengkai Pan, Peter Potaptchik, Wenxi Yao, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11156v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11156v1)

**Summary:** Recent one-step generative models accelerate sampling by learning deterministic flow maps of the underlying dynamics. These methods rely on learning from ordinary differential equations, leaving open how to define an exact distillation procedure for stochastic dynamics. We introduce the Itô map, an any-step stochastic flow map that takes an intermediate state and Brownian path and predicts future states in a single pass. The Itô map formulation yields novel estimators for inference-time control ...

---

### 2. Data assimilation for subsurface flow using latent diffusion model parameterization: performance of ensemble-Kalman and Monte Carlo techniques

**Authors:** Guido Di Federico, Wenchao Teng, Louis J. Durlofsky

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11140v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11140v1)

**Summary:** Data assimilation (DA) in subsurface flow entails calibrating model parameters to match observed data, typically at wells, while preserving geological realism. Latent diffusion models (LDMs) provide efficient mappings from high-dimensional geological model space to a low-dimensional latent variable, reducing the dimensionality of the inverse problem while maintaining plausibility in posterior geomodels. However, the high nonlinearity in the LDM mapping may degrade the performance of Kalman-gain-...

---

### 3. Conformal Prediction for Dyadic Regression Under Complex Missingness

**Authors:** Robert Lunde, Minjie Yang, Elizaveta Levina, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11136v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11136v1)

**Summary:** We develop a framework for conformal prediction in dyadic regression problems under complex missingness mechanisms. At the theoretical level, we establish super-uniformity of conformal prediction under distributional invariance conditions weaker than exchangeability. A key result handles the case where the sample itself is a random subset of the index set, a setting not covered by existing theory, via a novel bijection argument that constructs an explicit measure-preserving correspondence betwee...

---

### 4. Data-Driven Dynamic Assortment in Online Platforms: Learning about Two Sides

**Authors:** Rahul Roy, Nur Sunar, Jayashankar M. Swaminathan

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11118v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11118v1)

**Summary:** We study a dynamic assortment problem on a two-sided service platform with incomplete information and heterogeneous customers in a discrete-time setting. In each period, a customer arrives seeking service, and the platform chooses an assortment of sellers to display. The customer then proposes a transaction to at most one seller in the assortment according to a multinomial logit choice model. After a fixed number of periods, sellers review the proposals they have received and each chooses at mos...

---

### 5. Limitations of Learning Tanh Neural Networks with Finite Precision

**Authors:** Philipp Grohs, Matěj Trödler

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11104v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11104v1)

**Summary:** We investigate limitations of learning $\tanh$ neural networks from point evaluations under finite-precision computations and $L^p$ accuracy guarantees, building on Berner, Grohs, and Voigtländer (2023). Our approach is based on a novel construction of sharply localized bump functions via iterated $\tanh$ activations. Using this mechanism, we show that, in a finite-precision setting, no adaptive randomized algorithm based on $m$ samples can achieve a convergence rate higher than the Monte Carlo ...

---

### 6. Flexible Kernels for Protein Property Prediction

**Authors:** Martin Jankowiak, Yerdos Ordabayev, Rudraksh Tuwani, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11057v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11057v1)

**Summary:** Despite its importance to applications in protein design, predicting protein properties like binding affinity and thermostability from sparse experimental data remains a significant challenge. Accordingly, we introduce a class of sequence kernels that exploit evolutionary substitution matrices as well as local linearity and demonstrate that the resulting Gaussian processes provide data-efficient models of protein property landscapes, frequently outperforming alternatives that rely on foundation ...

---

### 7. Generalized Conformal Predictive Systems Under Distributional Shifts

**Authors:** Jef Jonkers, Johanna Ziegel

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.11044v1) | 📄 [PDF](https://arxiv.org/pdf/2606.11044v1)

**Summary:** Conformal predictive systems (CPS) output calibrated bands of CDFs under exchangeability. We extend generalized CPS to non-exchangeable settings by encoding distributional shifts through observation-specific permutation weights. This yields shift-aware predictive systems that remain valid whenever the test point is, conditionally on the unordered sample, a weighted draw from the observed atoms. Since such weights are typically estimated, we introduce weight-uncertainty boxes and construct robust...

---

### 8. Express Language Modeling

**Authors:** Albert Gong, Annabelle Michael Carrell, Raaz Dwivedi, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10944v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10944v1)

**Summary:** We introduce a new tool, Express, for converting a non-causal attention approximation into a causal approximation with matching approximation guarantees. When combined with the state-of-the-art Thinformer approximation, Express improves upon the best known causal attention guarantees, delivering $\log^{3/2}(n)/s$ approximation error with only $O(s)$ memory and $O(s^2 \log^2(n))$ compression overhead for a sequence of length $n$. We pair these developments with an efficient I/O-aware Triton imple...

---

### 9. Range Penalization: Theoretical Insights with Applications in Federated Learning

**Authors:** Yiyuan She, Zhaojun Hu, Yifan Sun

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10916v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10916v1)

**Summary:** This paper introduces range regularization for federated learning with linear systematic components to enhance statistical accuracy and induce cross-client regularity conducive to quantization, coding, and resource efficiency. Our approach identifies features with shared weights across different clients and adaptively clusters the weights of personalized features at extreme values, a process we refer to as polar clustering. Theoretical analysis of the associated estimators poses significant chal...

---

### 10. Conservation Laws from Data Symmetry in Neural Networks

**Authors:** Jakob Galley, Vahid Shahverdi, Axel Flinth

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10913v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10913v1)

**Summary:** We explore whether intrinsic symmetries of the training data lead to conserved quantities during gradient-flow training of neural networks. Under the assumption that the loss function is analytic and non-polynomial, we prove that data symmetries generically do not induce any additional integrals of motion. For mean squared error (MSE) loss, on the other hand, there are situations in which data augmentation yields extra conserved quantities. We build a framework, utilizing \emph{tensorizable netw...

---

### 11. Human-AI Teaming Through the Lens of Calibration

**Authors:** Eric Nalisnick, Chi Zhang, Sophia Qian, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10906v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10906v1)

**Summary:** We study models for human-AI teaming through the lens of statistical calibration. We assume the team consists of an AI model and human -- both of which are calibrated with respect to some partitioning of the feature space -- and expose how the calibration assumptions propagate into the teaming framework. In particular, we consider frameworks that either (i) combine human and model predictions or (ii) delegate prediction responsibility to either a human or model. We show via theoretical and empir...

---

### 12. SPACR: Single-Pass Adaptive Training of Uncertainty-Aware Conformal Regressors

**Authors:** Soundouss Messoudi, Sylvain Rousseau, Sébastien Destercke

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10734v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10734v1)

**Summary:** Conformal Prediction (CP) provides robust uncertainty guarantees for predictive models, but is typically applied post hoc, which misaligns model training with the conformal goal of producing efficient (i.e, narrow) intervals. We propose SPACR (Single-Pass Adaptive Conformal Regressor), a novel method for directly training uncertainty-aware regressors within a differentiable loss. SPACR jointly optimizes efficiency and validity without batch-splitting or a predefined confidence levels during trai...

---

### 13. Deterministic Denominator Design for Localized Tamed Stochastic-Gradient Langevin Dynamics

**Authors:** Yiwei Zhou, Ziheng Chen

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10559v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10559v1)

**Summary:** Tamed stochastic-gradient Langevin dynamics (SGLD) stabilizes large drifts by adding a denominator to the update. If this denominator uses the same stochastic-gradient sample as the update step, it can also change the conditional mean drift. We study deterministic denominators: the state-dependent envelope is fixed before the current oracle sample is drawn. The main question is how to design this envelope in practice. The design starts from an oracle score, builds a low-cost proxy score on pilot...

---

### 14. Advancing the State-of-the-Art in Empirical Privacy Auditing

**Authors:** Nicole Mitchell, Galen Andrew, Arun Ganesh, et al.

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10481v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10481v1)

**Summary:** Parameter-efficient fine-tuning of large language models (LLMs) can exhibit problematic memorization of individual training examples. Empirical privacy auditing (EPA) quantifies this risk by measuring realistic data leakage on membership inference (MI) or reconstruction attacks. A key challenge in EPA is designing ``canary'' examples that are mixed with the privacy-sensitive training data. We propose generating synthetic canaries via high-temperature sampling ($T \geq 0.8$) from LLMs, using prom...

---

### 15. A Mean-Field Analysis of Multi-Head Self-Attention under Cross-Entropy Training

**Authors:** Cheng Huan, Hongfwei Yuan

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10469v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10469v1)

**Summary:** This paper develops a mean-field theory for a simplified single-layer causal multi-head self-attention model trained by cross-entropy minimization. Each attention head is treated as a particle in parameter space, and the empirical law of the heads is used as the large-head state variable. In the infinite-head limit, the averaged attention logits define a risk functional on probability measures, whose first variation generates a nonlinear Wasserstein gradient-flow equation. Unlike classical mean-...

---

### 16. Near-Exponential Convergence Rates for kNN Classification based on Boltzmann Margin

**Authors:** Luyuan Yang, Shayan Shafaei, Chao Lan

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10361v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10361v1)

**Summary:** Convergence-rate analysis for classifiers is often conducted under either Tsybakov margin or Massart margin. The former is a relatively weak condition that typically yields polynomial rates, while the latter is substantially stronger but can guarantee exponential rates. In this paper, we introduce a new condition, called Boltzmann margin, that bridges the gap between these two regimes. It is weaker than Massart margin, generally stronger than Tsybakov margin, and can imply many of their properti...

---

### 17. Rank Collapse, Fixed Points, and the Renormalization Group Structure of MLP Residual Networks

**Authors:** Parviz Haggi-Mani, Irina Rish

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10324v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10324v1)

**Summary:** The analogy between deep neural network forward passes and renormalization group (RG) flows has been repeatedly noted in the literature, but existing treatments remain qualitative: depth is described as a coarse-graining scale, attention is likened to a partition function, and representations are said to flow toward fixed points. No existing work has defined a measurable RG order parameter, tested it under controlled variation of the input distribution, or made quantitative predictions that are ...

---

### 18. $k$-Nearest Neighbors in Gromov--Wasserstein Space

**Authors:** Kaitlyn Hohmeier, Nicolas Fraiman, Caroline Moosmueller

**Published:** 2026-06-09

🔗 [Paper](http://arxiv.org/abs/2606.10295v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10295v1)

**Summary:** The Gromov--Wasserstein (GW) distance provides a framework for comparing metric measure spaces, regardless of their underlying structure or geometry. For network-based data, it enables direct comparisons of graphs with different numbers of nodes, without requiring an embedding or other abstraction. Furthermore, through a variant of GW known as fused Gromov--Wasserstein (fGW), it is also possible to incorporate node features in addition to graph structure. In this work, we implement $k$-nearest n...

---

### 19. Intrinsic Footpoint-invariant Riemannian Cross-covariance

**Authors:** Carlos Soto, Cheng Wang, Zipan Huang, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10212v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10212v1)

**Summary:** Covariance estimation yields a fundamental second-order statistic underlying representation learning, dimension reduction, and dependence modeling. While covariance has been well understood in Euclidean spaces, it is ill-defined for random objects residing on nonlinear Riemannian manifolds, which increasingly arise in modern machine learning applications involving shapes, symmetric positive definite (SPD) matrices, etc. This paper introduces an intrinsic Riemannian cross-covariance for manifold-...

---

### 20. Decision-Calibrated Conformal Uncertainty for Pacing Decisions in Streaming Advertising

**Authors:** Prashant Shekhar, Caroline Howard

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10187v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10187v1)

**Summary:** We develop a decision-calibrated conformal framework for pacing decisions in streaming advertising. Pacing depends on uncertain future inventory, demand pressure, incremental response, and member-experience load. Instead of calibrating a generic forecast residual, the framework measures forecast error by its largest impact on the policies that could actually be deployed. The main theorem shows that the proposed score is the smallest valid uncertainty measure that uniformly protects all deployabl...

---

### 21. Robust Active Learning for Few-Shot Example Selection in Text-to-SQL

**Authors:** Arash Pourhabib

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10125v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10125v1)

**Summary:** Few-shot example retrieval is the dominant paradigm for grounding large language models (LLMs) in domain-specific text-to-SQL systems. However, the quality of the annotated example bank directly governs system accuracy, and expert annotation is prohibitively expensive. We formalize the active selection of these examples as a constrained experimental design problem over the intrinsic, low-dimensional manifold of semantic query embeddings. Unlike standard active learning frameworks, our setting in...

---

### 22. Convergence Rates for Neural-Network Estimation with Current-Status Data

**Authors:** Yuan Wu, Tianhui Zhou

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10119v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10119v1)

**Summary:** Current-status data arise when an event time is observed only through an indicator of whether it occurred before an examination time. This paper studies a nonparametric neural-network sieve maximum likelihood estimator of the conditional cumulative distribution function of the event time. Under Hölder smoothness assumptions, we establish an explicit convergence rate by combining approximation theory for rectified linear unit neural networks with empirical-process arguments. This result provides ...

---

### 23. Nonlinear Estimator: Dual Bayesian Affine Estimators for Parameter Learning

**Authors:** Sasan Vakili, Daniël Woonings, Pradyumna Paruchuri, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.10111v1) | 📄 [PDF](https://arxiv.org/pdf/2606.10111v1)

**Summary:** This paper presents a nonlinear parameter estimator for Wiener-type state-space models obtained as a fixed-point architecture that couples two affine minimum mean-squared error (MMSE) estimators: one for the unknown parameters and one for latent variables. The architecture retains the functional structure of the optimal affine MMSE parameter estimator while incorporating Dynamic Basis Statistics (DBS) estimates that summarize nonlinear basis-function evaluations. Two DBS construction strategies ...

---

### 24. Weighted universal approximation of differentiable maps on infinite-dimensional manifolds

**Authors:** Philipp Schmocker, Josef Teichmann

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09820v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09820v1)

**Summary:** We generalize the universal approximation theorem for functional input neural networks (FNN) to differentiable maps by including the approximation of the derivatives. A FNN maps the input from a possibly infinite-dimensional weighted manifold to the real-valued hidden layer, on which a non-linear scalar activation function is applied, and then returns the output into a Banach space via some linear readouts. By proving a weighted Nachbin theorem, we establish a universal approximation theorem (UA...

---

### 25. Bandits for Efficient Experimentation: Adapting to Control Group, Preferences, and Context Drifts

**Authors:** Udvas Das, Waris Radji, Debabrota Basu, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09802v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09802v1)

**Summary:** We consider a variant of the linear contextual stochastic multi-armed bandits, where the learner must provide recommendations to a group of users, each having its personalized preference vector, and in the presence of context distributions that are drifting over time. Under practitioner-friendly assumptions, we reduce this setting to linear bandit with stationary mean but heteroskedastic and non-stationary noise. We further study the case when the learner must ensure the mean reward of each deci...

---

### 26. In-Context Learning for Latent Space Bayesian Optimization

**Authors:** Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09664v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09664v1)

**Summary:** Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO c...

---

### 27. On Choosing the $μ$ Parameter in Gaussian Differential Privacy

**Authors:** Bogdan Kulynych, Antti Honkela

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09582v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09582v1)

**Summary:** Recent work argues for using Gaussian differential privacy (GDP) to report the privacy guarantees in privacy-preserving machine learning. We provide principled mappings from pure-DP $\varepsilon$ to GDP $μ$ by matching the worst-case success of a strong-adversary membership inference attack in terms of three metrics: multiplicative advantage at fixed FPR, precision at fixed recall, and the standard privacy profile. We tabulate $μ$ values across a useful range of parameters and recommend $μ\appro...

---

### 28. Report the Floor: A Training-Free Conformal Interval Is a Mandatory Baseline for Probabilistic Time-Series Forecasting

**Authors:** Valery Manokhin

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09473v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09473v1)

**Summary:** Probabilistic forecasters are increasingly learned, yet the baselines they are compared against are often weak or omitted. We show that the simplest possible conformal interval - a last-value point forecast wrapped in a finite-sample split-conformal residual quantile, with no parameters and no training - is a far stronger baseline than its near-total absence from recent learned-forecasting and conformal-time-series comparisons would suggest. In one-step-ahead online forecasting across 2,217 real...

---

### 29. SAILS: Surrogate-based Analysis of Interactions via Local Effect Smooths

**Authors:** Timo Heiß, Julia Herbinger, Bernd Bischl, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09404v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09404v1)

**Summary:** Feature interactions drive much of the predictive power of machine learning models, yet existing explanation methods only detect and quantify interactions without revealing their functional form, or visualize only restricted interaction types. We propose Surrogate-based Analysis of Interactions via Local effect Smooths (SAILS), a model-agnostic framework that analyzes pairwise interactions through interpretable generalized additive model (GAM) surrogates fitted to the local effects of a black-bo...

---

### 30. BSTabDiff: Block-Subunit Diffusion Priors for High-Dimensional Tabular Data Generation

**Authors:** Al Zadid Sultan Bin Habib, Md Younus Ahamed, Prashnna Gyawali, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09257v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09257v1)

**Summary:** High-Dimensional Low-Sample Size (HDLSS) tabular domains (e.g., omics) are characterized by $n \ll m$, where $n$ = number of samples, and $m$ = number of features. Such domains often exhibit strong local correlation groups, sparse cross-group dependencies, heavy-tailed non-Gaussian marginals, heteroscedastic noise, and structured missingness, making direct density learning in $\mathbb{R}^m$ ill-conditioned since $n \ll m$. We propose BSTabDiff, a block-subunit generative framework that partition...

---

### 31. Asymptotic Optimality of Thompson Sampling for Risk-Averse Bandits with Sub-Gaussian Rewards

**Authors:** Joel Q. L. Chang

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09191v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09191v1)

**Summary:** We prove that $ρ\text{-}\mathrm{NPTS}_{\mathrm{SG}}$, an anchor-free nonparametric Thompson Sampling algorithm for risk-averse bandits, achieves regret matching the instance-dependent lower bound to leading order in $\log n$, establishing it as asymptotically optimal for any continuous risk functional $ρ$ (CVaR, mean-variance, Sharpe ratio, distortion risk measures, and more) on the class of distributions with bounded density and sub-Gaussian tails, including Gaussian arms. Both this result and ...

---

### 32. INFUSER: Influence-Guided Self-Evolution Improves Reasoning

**Authors:** Siyu Chen, Miao Lu, Beining Wu, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09052v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09052v1)

**Summary:** Self-evolution offers a scalable path to stronger reasoning: a pretrained language model improves itself with only minimal external supervision. Yet existing methods either depend on extensively curated or teacher-generated training data, or, when the generator runs unsupervised, reward it by a difficulty heuristic that need not improve the solver. We introduce INFUSER, an iterative co-training framework with two co-evolving roles: a Generator that drafts questions and reference golden answers f...

---

### 33. Data augmented bootstrap: Unifying confidence interval construction by approximate invariance

**Authors:** Kevin Han Huang

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09049v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09049v1)

**Summary:** We propose the data augmented bootstrap (DAB), a framework for constructing confidence intervals from approximately invariant transformations of the data. As special cases, DAB recovers popular methods that rely on exact group symmetries, such as conformal prediction, wild bootstrap for Maximum Mean Discrepancy U-statistics and the recently proposed SymmPI. Meanwhile, DAB also recovers the classical bootstrap method, which exploits the dataset's approximate invariance under uniform sampling of d...

---

### 34. Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin

**Authors:** Hanyang Li, Jianhao Ma, Ying Cui

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09012v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09012v1)

**Summary:** Post-training quantization (PTQ) converts a trained full-precision model into low-bit weights without task-level retraining, while quantization-aware training (QAT) incorporates quantization into the training loop. Although PTQ is efficient and often accurate at moderate bitwidths, it can fail sharply at aggressive bitwidths; QAT is more expensive but can often recover the lost accuracy. We propose a unified geometric framework that explains both PTQ failure and QAT recovery. We model full-preci...

---

### 35. Multi-Armed Bandits with Arriving Arms: Sequential Screening, Dynamic Regret, and Sublinear Guarantees

**Authors:** Deqi Zheng, Xiaoyang Xu, Yuhong Yang

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.09002v1) | 📄 [PDF](https://arxiv.org/pdf/2606.09002v1)

**Summary:** We study a stochastic multi-armed bandit problem in which the set of available arms expands over time. This setting arises in sequential experimentation when new actions or treatments become available during an ongoing study, making regret against a single best arm in hindsight inappropriate. We instead evaluate performance relative to the best arm currently available, leading to a dynamic-regret criterion for arriving-arm environments. To address the resulting challenges of arrival information ...

---

### 36. Estimate Collapsibility of Causal Effects in Completed Partial DAGs via Strong d-Convex Hulls

**Authors:** Yuxin Deng, Yi Sun, Zhiming Li, et al.

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.08941v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08941v1)

**Summary:** This paper proposes a collapsible method for estimating causal effects that maintains the estimator's consistency before and after marginalization over some variables in completed partially directed acyclic graphs (CPDAGs). We first introduce the estimate collapsibility for CPDAGs and characterize the minimal collapsible sets as strong d-convex hulls. An efficient algorithm is devised to obtain such sets in DAGs and is generalized to CPDAGs. Then, we combine the graph reduction procedure with th...

---

### 37. Backward Coherence and Hidden-State Stability in Recurrent Neural Networks: A Quasi-Reverse-Martingale Theory

**Authors:** Yuan-chin Ivan Chang

**Published:** 2026-06-08

🔗 [Paper](http://arxiv.org/abs/2606.08934v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08934v1)

**Summary:** Recurrent neural networks maintain a hidden state $h_t$, but its probabilistic meaning is often unclear. We study hidden-state stability through \emph{backward coherence}: the extent to which $h_t$ can be reconstructed from $h_{t+1}$ by a learned backward projector $g_φ$. Under contraction and summable backward drift, the hidden-state sequence forms a quasi-reverse-martingale. This yields almost-sure convergence, rates under mixing, an interpretable limiting representation, finite pathwise stopp...

---

### 38. sGPO: Trading Inference FLOPs for Training Efficiency in RLVR

**Authors:** Shivchander Sudalairaj, Kai Xu, Akash Srivastava, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08854v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08854v1)

**Summary:** Standard Reinforcement Learning with Verifiable Rewards (RLVR) training allocates a fixed rollout budget to every query, without regard for what each query's difficulty means for the current policy. This leads to two symmetric failure modes: easy queries produce near-zero advantage because the policy already solves them, while unsolvable queries produce no signal because the policy never solves them. Both regimes waste training FLOPs without contributing to a learning gradient. We introduce sort...

---

### 39. Intrinsic Selection and Particle Resampling for Inference-Time Scaling Beyond Domain Verifiability

**Authors:** Giorgio Giannone, Mustafa Eyceoz, Shabana Baig, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08850v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08850v1)

**Summary:** Inference-Time Scaling (ITS) has largely succeeded in verifiable domains like math and coding, where cheap verification enables scalable output selection. However, extending ITS to tasks prone to systematic failure - driven by faulty initial assumptions or unmet multidimensional constraints - typically relies on costly external solvers or brittle, model-based verifiers. Our key insight is that the intrinsic statistics of parallel sample sets, specifically length-adjusted tail entropy, provide a ...

---

### 40. Generalization in Nonlinear Least Squares via Learned Feature Geometry

**Authors:** Ayub Kharel, Ilja Kuzborskij, Patrick Rebeschini, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08799v2) | 📄 [PDF](https://arxiv.org/pdf/2606.08799v2)

**Summary:** We study the generalization of ridge-regularized nonlinear least-squares models via on-average algorithmic stability, deriving error bounds for local minimizers in terms of a data-dependent effective dimension that reflects the geometry of the gradient model at the trained parameters, through the empirical Jacobian Gram matrix and a residual-curvature term. In the linear case, where the curvature term vanishes, this recovers the classical effective dimension of the Jacobian kernel covariance, bu...

---

### 41. Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation

**Authors:** Bitya Neuhof, Yuval Benjamini

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08679v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08679v1)

**Summary:** Pretrained models are often evaluated on multi-task leaderboards to measure their applicability in diverse contexts. However, current methods for aggregating performance across tasks into leaderboard-level rankings do not address the uncertainty and variability at the task level. While recent works have proposed interval-based model rankings, the principled aggregation of uncertainty from individual tasks to leaderboard-level rankings remains unaddressed, and variation in models' performance acr...

---

### 42. Improving the sharpness in neural network-based parametric post-processing of ensemble forecasts

**Authors:** Ágnes Baran, Máté Mihalina

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08587v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08587v1)

**Summary:** Statistical post-processing has proven to be an effective tool in improving ensemble forecast of different weather variables. Case studies show that post-processing can remedy the typically underdispersive and potentially biased behaviour of the ensemble while optimizing a proper scoring rule expressing the forecast skill. The price of these positive effects is generally a deterioration in sharpness; the width of the central prediction intervals and the uncertainty of the predictions are increas...

---

### 43. CP-factorization for high dimensional tensor time series and double projection iterations

**Authors:** Jinyuan Chang, Guanglin Huang, Qiwei Yao, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08560v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08560v1)

**Summary:** We adopt the canonical polyadic (CP) decomposition to model high-dimensional tensor time series. Our primary goal is to identify and estimate the factor loadings in the CP decomposition. We propose a one-pass estimation procedure through standard eigen-analysis for a matrix constructed based on the serial dependence structure of the data. The asymptotic properties of the proposed estimator are established under a general setting as long as the factor loading vectors are linearly independent, all...

---

### 44. Querying Counterfactuals on Tissue Graphs with Supervised Disentanglement

**Authors:** Abdul Moeed, Stefan Schrod, Martin Rohbeck, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08493v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08493v1)

**Summary:** \textit{Tissue graph counterfactuals} ask how a cell's expression would change under altered spatial neighbor contexts. Such queries are central to predicting cell behavior in tissues, but lack a unified definition, with existing methods targeting specific intervention types or treating cells as i.i.d. In this work, we first formalize \textit{tissue graph counterfactuals} as a class of spatial interventions that either rewire connections between cells (\textit{edge perturbation}) or modify the e...

---

### 45. Nonparametric undirected graphical model selection using diffusion models

**Authors:** Hyeok Kyu Kwon, Myeonggu Kang, Minwoo Chae, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08468v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08468v1)

**Summary:** Undirected graphical models provide a fundamental framework for representing conditional independence structures among high-dimensional random variables. While undirected graphical model selection has become a central problem in high-dimensional statistics, most existing methods are restricted to parametric settings. In this paper, we develop a nonparametric approach to undirected graphical model selection based on diffusion models. Recent work has shown that diffusion models can adapt to the un...

---

### 46. LOTTERY: Learning from Reference-Only Samples in Two-Sample Testing under Size Asymmetry

**Authors:** Xunye Tian, Zhijian Zhou, Liuhua Peng, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08460v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08460v1)

**Summary:** Data-adaptive two-sample testing assesses if two samples come from the same distribution, using a discrepancy learned from the data (e.g., via kernel-based feature representations). Such methods typically rely on data splitting to decouple learning from testing and control type I error. However, this paradigm is ill-suited to few-shot settings with severe sample-size imbalance: abundant reference samples are available, while only a handful of query samples arrive. In this paper, we show how this...

---

### 47. Improving Bayesian Optimization via Training-Aware Conditional Diffusion Models

**Authors:** Yilin Zheng, Haowei Wang, Szu Hui Ng, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08438v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08438v1)

**Summary:** Bayesian optimization (BO) is a widely used approach for black-box optimization that uses a Gaussian process (GP) as a surrogate and guides sequential evaluations via an acquisition function, with the ultimate goal of locating the global optimum $\mathbf{x}^{\star}$. To align with this goal, information-based acquisition functions such as Predictive Entropy Search (PES) model $\mathbf{x}^{\star}$ as a random variable and reduce the entropy of its distribution, but approximating this distribution...

---

### 48. When Are Neural Interaction Discoveries Real? Identifiability, Recoverability, and a Pre-Fit Diagnostic

**Authors:** Valentina Kuskova, Dmitry Zaytsev, Michael Coppedge

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08390v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08390v1)

**Summary:** When a neural time-series model reports that one variable modulates another's effect on a target, is the discovered interaction a property of the data or an artifact of model flexibility? We argue that this is fundamentally a question of identifiability, governed by the geometry of the observed input support rather than by the specific neural architecture. We study the problem in a multiplicative-gating extension of neural additive vector autoregression (GNAVAR), in which source contributions ar...

---

### 49. The Spectral Dynamics and Noise Geometry of Muon

**Authors:** Pierfrancesco Beneventano, Mahmoud Abdelmoneum, Tomaso Poggio

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08388v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08388v1)

**Summary:** Muon replaces a matrix gradient $G=UΣV^\top$ by its polar factor $UV^\top$. This keeps the singular directions selected by the gradient, but makes the update spectrum flat. We study the optimization bias created by this operation. Under explicit alignment assumptions, we prove that the polar update is the one-step entropy-maximizing choice among bounded updates that use the gradient singular directions and do not adapt to the current weight spectrum. In an underdetermined regression model, we de...

---

### 50. A Switching Beamformer for Highly Non-Stationary Environments

**Authors:** Manan Mittal, Ryan M. Corey, John R. Buck, et al.

**Published:** 2026-06-07

🔗 [Paper](http://arxiv.org/abs/2606.08385v1) | 📄 [PDF](https://arxiv.org/pdf/2606.08385v1)

**Summary:** Adaptive beamforming is a cornerstone of array signal processing, yet its performance often collapses in the face of complex, rapidly changing interference. When interferers appear or move unpredictably, conventional estimators encounter a fundamental memory trade-off: short windows enable rapid tracking but suffer from high estimation variance, while long windows provide stable rejection but fail to adapt to shifts. This challenge is resolved by introducing the Universal Switching Beamformer (U...

---

