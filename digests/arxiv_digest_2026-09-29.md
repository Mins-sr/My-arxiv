# arXiv Daily Digest - 2026-09-29

Total papers: 350

---

## cs.AI

**50 papers**

### 1. FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets

**Authors:** Srinjay Sarkar, Prakhar Kaushik, Soumava Paul, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35770v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35770v1)

**Summary:** Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets. Fur usually covers most of an animal's body, with large inter-species and intra-species variability. We present FurE, an efficient strand-based animal fur reconstruction method that recovers a per-strand, editable groom by optimizing a root-conditioned latent field, decoded into strand geometry vi...

---

### 2. Telescopic Language Models

**Authors:** Zhilin Guo, Boqiao Zhang, Hakan Aktas, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35769v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35769v1)

**Summary:** One deployed language model must often serve many compute budgets, yet serving each budget still means a separate training or compression run per point. We train a Telescopic Language Model (TLM) to be that continuum: a nested-capacity Transformer supervised by stochastic prefix supervision with a full anchor. At every step, one randomly truncated prefix of the capacity axis is trained against the full next-token target, alongside one full-capacity pass, so the trained artifact is a valid langua...

---

### 3. Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning

**Authors:** Yijia Fan, Ziqi Huang, Zhongang Cai, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35767v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35767v1)

**Summary:** Unified multimodal models can both look at and render images, so in principle they can repair their own generations: diagnose what an image gets wrong, revise it, observe the result, and diagnose again. Whether a revision helps is known only after it is rendered, so the reflection text and the image generation must be learned jointly, over the whole loop. Supervised fine-tuning (SFT) on reflection trajectories gives a cold start but does not find the high-success repair paths, and naive RL that ...

---

### 4. TokenCast: Forecasting Token Consumption During LLM Agent Execution

**Authors:** Chaoqian Ouyang, Ling Yue, Libin Zheng, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35760v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35760v1)

**Summary:** When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction must be revised as the run unfolds. In this paper, we propose TokenCast, which learns a composable cos...

---

### 5. How to Loop MoE: Flatten the Experts, Untie the Attention

**Authors:** Shouren Wang, Chuang Ma, Mohsen Hariri, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35751v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35751v1)

**Summary:** Looped Transformers reuse one block of layers several times: by spending extra computation they push a model of fixed size further, and so use its parameters more fully; while sparse mixture-of-experts (MoE) models activate only a few of many experts for each token. Looped MoE bridges these two design philosophies and gives MoE models new potential for better expert usage, but it raises a question: how to loop a MoE? We answer it with Foil. With the expert parameters and the expert compute per t...

---

### 6. KV-streams for Efficient Compaction in Agentic Reinforcement Learning

**Authors:** Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35750v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35750v1)

**Summary:** Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping GPU memory constant for a given trace. Unfortunately, most compaction strategies rely on prefilling the LLM context many times over, hindering training throughput. To alleviate this bottleneck and enable efficient trainable compaction, we propose KV-streams, a plug-and-play strategy compatible with...

---

### 7. Copy the Same, Distill the Difference: Initializing Linear Vision Transformers

**Authors:** Huaiyuan Qin, Muli Yang, Gabriel James Goenawan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35745v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35745v1)

**Summary:** Linear Vision Transformers (ViTs) are designed to replace the attention in Softmax ViTs with the linear-complexity attention operator for more efficient token routing, but they require from-scratch pre-training and typically underperform the original Softmax version. How to initialize linear ViTs both efficiently and effectively still remains unclear. In this work, we explicitly ask: given that most foundation ViTs are built on the mainstream Softmax attention, can linear ViTs benefit from their...

---

### 8. FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents

**Authors:** Hoyoung Lee, Suyeol Yun, Jack Haverty, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35744v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35744v1)

**Summary:** Evaluating finance research agents requires rubrics that reflect expert standards and fix the values correct as of an information cutoff. Expert-reviewed finance benchmarks rely on fixed, per-item rubrics, which are costly to extend and cannot encode each institution's own standard. In FinAutoRubric, experts specify reusable evaluation guidance, while agents and code carry out query-specific rubric generation, review, and validation. This expert guidance governs every agent, as prompts and as ru...

---

### 9. Shockingly Simple Self-retrospection Improves Agentic Models Without RL

**Authors:** Jonathan Light, Christopher Zhang Cui, Jeonghye Kim, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35741v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35741v1)

**Summary:** People learn not only by repeating successful actions, but also by recounting and explaining their experiences, revising their understanding to guide future behavior. Can a language-model agent improve its future actions by training only on explanations of its own experience? We investigate this question by studying Retrospection-Only Fine-Tuning (ROFT), a minimal online procedure designed to isolate the effect of explanation-only training on subsequent behavior. The agent attempts a task, obser...

---

### 10. Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models

**Authors:** Junru Zhu, Shiming Xie, Aime Lu Fan Chen, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35732v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35732v1)

**Summary:** Tool-using agents can fail twice: a required tool can fail, and the agent can then report success without the evidence needed to justify it. Existing benchmarks often entangle this reporting failure with tool selection, recovery, and environment dynamics. We introduce Failure-Transparent Agents (FTA), a controlled benchmark that fixes the failed observation and required evidence state before generation, making post-failure claims directly auditable. FTA contains 100 tasks with deterministic fail...

---

### 11. X-Reset: Scaling Object-Centric Reinforcement Learning via Cross-Embodiment Resets

**Authors:** Prithwish Dan, Chenyang Ma, Wei Zhan

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35715v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35715v1)

**Summary:** Reinforcement learning (RL) in simulation can train dexterous manipulation policies without robot demonstrations, but training a single generalist policy with task-agnostic rewards faces a severe exploration problem: approaching, grasping, and reorienting diverse objects with many degrees of freedom is difficult to discover from scratch. Prior works make exploration tractable with high-quality robot demonstrations, per-task reward shaping, or by restricting policies to narrow modes of behavior. ...

---

### 12. Reinforcing Agentic Creativity in Scientific Ideation with Night Science

**Authors:** Priyanka Kargupta, Silviu Cucerzan, Shweti Mahajan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35706v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35706v1)

**Summary:** Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discovery, however, spans a broader creative spectrum: from structured day science to loosely structured, serendipitous night science that reaches ideas beyond those typically considered. We introduce AI Night-Scientist, an agentic framework that uses reinforcement learning to teach mod...

---

### 13. A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion

**Authors:** Fred Xu, Thomas Markovich, Florence Regol, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35703v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35703v1)

**Summary:** Reliable deployment of graph neural networks requires calibration, out-of-distribution (OOD) detection, and robustness to distribution shift, yet existing methods address these needs with separate models and   objectives. We model uncertain node embeddings as random graph signals: graph Fourier filters capture structural variation, and a scalar orthogonal-polynomial chaos coordinate captures latent stochastic   variation. The resulting doubly-spectral stochastic (DSS) expansion supplies task-mat...

---

### 14. Distillation Defenses Easily Break After Reinforcement Learning

**Authors:** Shidan Javaheri, Alexander Panfilov, Oliver Britton, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35699v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35699v1)

**Summary:** Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect a large volume of frontier model reasoning traces and then train (i.e., "distill") their own models on these traces. Existing defenses against distillation attacks are typically evaluated immediately after distillation, implicitly assuming attackers do not train their models any further. In this pa...

---

### 15. Reasoning with Continuous Latent Diffusion

**Authors:** Xiang Cheng

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35694v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35694v1)

**Summary:** Continuous diffusion generates complete reasoning solutions through iterative refinement in latent space. We introduce Latent Flow Reasoning Models (LFRMs), an ELF-based training and inference recipe. Our experiments show that accurate decoding alone does not ensure strong reasoning performance. We therefore learn compact representations from multiple layers of a strong autoregressive teacher. Their decomposition also enables asynchronous denoising at different rates. We show that prompt encodin...

---

### 16. Report: Progressive Disclosure of Agent Skills

**Authors:** Guilin Zhang, Kai Zhao, Priyanka Mudgal, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35692v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35692v1)

**Summary:** Users of Workday's deployed LLM-based agents often request features which can be addressed by defining named procedures, also known as skills, in the LLM context, effectively augmenting agents' capabilities. However, as an agent's skills library grows in size, so does the agent's operational cost. Progressive disclosure (lazy-loading) of skills as needed may reduce operational costs, but its impact on overall latency and skill-retrieval quality remains unclear. In this report, we investigate the...

---

### 17. Rethinking Circuit Evaluation: Do Circuits Explain Model Errors?

**Authors:** Li Zhang, Chuqin Geng, Mark Zhang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35686v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35686v1)

**Summary:** Mechanistic interpretability (MI) aims to explain a model's behaviour through analyzing its internal computations; circuit-based explanations aim to isolate these computations with compact subnetworks validated by ablating the rest of the model. We show that circuits validated this way may fail to recover the underlying mechanism of the model's behaviour by closely reproducing its successful decisions while failing to account for most of its errors. Such explanations should account for the model...

---

### 18. Verifier Errors in RLVR: Reward Hacking, Limits of Feedback, and Selective Control

**Authors:** Christian Moya, Elliott Thornley, Guang Lin

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35677v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35677v1)

**Summary:** In reinforcement learning with verifiable rewards (RLVR), imperfect verifiers can reward incorrect responses, creating opportunities for reward hacking. Using gradient flow with a fixed verifier, we characterize the conditions under which reward rises while correctness falls. We then show that the observations available during RLVR are, in general, insufficient to detect or identify accepted errors, or to guarantee their reduction without sacrificing correct responses. To address this limit, we ...

---

### 19. PhoneCLI: From App Interfaces to Callable Commands for Mobile Agents

**Authors:** Yangqin Jiang, Lingrui Xu, Chao Huang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35671v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35671v1)

**Summary:** Mobile GUI agents operate through a perception--action loop: at each step they screenshot the device, invoke a vision--language model (VLM), and emit an action. It is slow, costly, and brittle, yet most of what it does is navigation---and everyday navigation is static, ordered, and endlessly repeated. We present PhoneCLI, which compiles an app's GUI navigation into callable commands, without any app-internal API, runtime instrumentation, or model training. Offline, PhoneCLI explores a target app...

---

### 20. MS-GLA: Multi-Scale Gated Linear Attention for Addressing Representational Bottlenecks via Multi-Temporal Resolution

**Authors:** Prasoon Dev, Anirudh Sankar, Vasudeva Varma

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35664v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35664v1)

**Summary:** Gated Linear Attention (GLA) Transformers advance linear recurrent models through data-dependent gating, but face a core limitation: the fixed-capacity memory matrices across all heads operate at a single temporal resolution, where each token is processed individually, forcing them to simultaneously encode local syntactic patterns and long-range semantic structure, creating a representational bottleneck that gating alone is insufficient to resolve. We introduce Multi-Scale Gated Linear Attention...

---

### 21. CMDO: A Cognitive Memory-Driven Optimization Algorithm for Adaptive Population-Based Search

**Authors:** Mohammed Yusuf Mujawar, Shahram Rahimi, Noorbakhsh Amiri Golilarz

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35657v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35657v1)

**Summary:** Population-based optimization methods often use previous search information through successful solutions, parameter adaptation, or operator performance, but they rarely retain the context in which a search behavior succeeded or failed. We introduce Cognitive Memory-Driven Optimization (CMDO), a derivative-free population-based optimizer that represents experience as the relationship between search context, search behavior, and observed outcome. CMDO organizes these experiences across working, ep...

---

### 22. Not All Thinking is Created Equal: Latent Reasoning Discovers a Recurrent Search Algorithm for Depth Generalization

**Authors:** Huzi Cheng, Zhewei Zhang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35643v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35643v1)

**Summary:** Large Language Models can perform multi-step reasoning and improve task performance through different forms of intermediate computation, from token-based traces to computation carried out in latent space. However, a question remains open: do these different forms of thinking rely on the same underlying mechanism? To address this, we train and compare five variants of the same GPTNeoX backbone from scratch on an extended multi-hop reasoning task (ProsQA-Ext): a vanilla model, a Chain-of-Thought (...

---

### 23. Verifiable Visual Rewards Transfer from Synthetic Scenes to Natural Prompts

**Authors:** Shuyue Stella Li, Xiaochuang Han, Yulia Tsvetkov, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35641v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35641v1)

**Summary:** Precise instruction following in image generation, such as satisfying object counts and spatial relations, remains an open challenge at least in part because it is learned using unreliable reward models such as object detectors and vision-language models. We introduce Verifiable Visual Rewards (VVR), the first framework for programmatically verifiable image rewards, and show that training on it generalizes to natural prompts. Each VVR task is a scene of geometric objects and relations among them...

---

### 24. GPUPhysBench: Benchmarking Coding Agents for Correct and Efficient GPU Physics Simulation

**Authors:** Yuchen Sun, Jinjin He, Sinan Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35639v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35639v1)

**Summary:** Writing fast GPU code for physical simulation is difficult: implementations must preserve numerical accuracy while handling irregular data access, synchronization, and iterative solvers. We introduce GPUPhysBench, a benchmark of 50 tasks testing whether coding agents can meet these demands. Tasks cover fluids, deformable solids, and granular materials, from individual simulation operators to complete simulators. Agents write, compile, test, and optimize GPU code with access to a NVIDIA GPU under...

---

### 25. DR-net-Mamba: Selective State-Space Modeling for Long-Range ECG Time-Series Denoising

**Authors:** Basile Morel, Samuel Ruiperez-Campillo, Andreas P. Streich, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35634v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35634v1)

**Summary:** Electrocardiogram (ECG) recordings are corrupted by non-stationary noise sources that degrade diagnostic reliability, particularly in ambulatory and long-duration recordings. Deep learning denoisers exist, but convolutional architectures are limited by their receptive field, transformer-based models scale quadratically with sequence length, and diffusion-based approaches incur prohibitive inference cost. We propose a Mamba-augmented model that inserts selective state-space blocks at the convolut...

---

### 26. RIDE: Reference-Anchored Inference-Time Diffusion Editing for Scaffold Hopping

**Authors:** Ruoxi Gao, Frazier N. Baker, Trieu Nguyen, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35623v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35623v1)

**Summary:** Scaffold hopping is a critical task in drug discovery, which seeks to discover new, structurally distinct molecules that share key functional groups and similar 3D shape with a reference binding ligand. Existing diffusion-based scaffold hopping methods formulate the problem as conditional generation of scaffolds given the functional groups. However, they lack a principled mechanism to jointly enforce 2D structural novelty and preserve the 3D shape of the reference ligand. Here, we introduce RIDE...

---

### 27. From cacophony to hierarchy: a principled framework for assessing AI consciousness

**Authors:** Shamil Chandaria, Arvo Muñoz Morán, Fernando Rosas, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35618v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35618v1)

**Summary:** The question of AI consciousness is one of the most urgent pre-emptive problems in philosophy and computer science, yet progress is hampered by a cacophony of competing theories that often talk past each other. Separating the hard problem from the mapping problem allows the deepest metaphysical disagreements to be set aside: granting that experience supervenes on a system's organisation, the tractable question becomes at which grain of description that supervenience base sits. We extend Marr's t...

---

### 28. Behavioral Foundation Models for Quality Diversity

**Authors:** Nazim Bendib, Nicolas Perrin-Gilbert, Olivier Sigaud

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35615v1)

**Summary:** Behavioral Foundation Models (BFMs) are an emerging paradigm in reinforcement learning, playing a role analogous to large language models in natural language processing: they have shown remarkable versatility, enabling zero-shot performance, fast imitation, and online adaptation, all by exploiting the structure of a latent space. In this work, we investigate whether the latent behavioral space induced by BFMs can serve as an effective search space to discover large repertoires of behaviorally di...

---

### 29. Twist, Don't Tilt: Trajectory-Exact Constrained Decoding for Masked Diffusion Models

**Authors:** Aditya Thimmaiah, Lara Marinov, Jayanth Srinivasa, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35609v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35609v1)

**Summary:** Constrained decoding for Masked Diffusion Language Models (MDLMs) aims to ensure that generated outputs satisfy a specified structure or syntax constraint. MDLMs generate outputs by repeatedly unmasking masked positions present in their current state. Recent strategies for constrained decoding constrain the model's per-step mean-field posterior (which factorizes over masked positions) by enforcing the desired constraint with an automaton. The resulting chain-structured factor graph allows exact ...

---

### 30. TCSAlgBench: Benchmarking Automated Proving for Research-Level Theoretical Computer Science

**Authors:** Chutong Yang, Xiyuan Zhang, Yu Huang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35606v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35606v1)

**Summary:** Large language models perform strongly on competition mathematics, but their research-level reasoning remains difficult to evaluate systematically. Theoretical computer science (TCS) connects algorithm design to explicit guarantees and fundamental limits, providing a setting for evaluating whether models can justify computational improvements with arguments humans can inspect. We introduce TCSAlgBench, a benchmark and reusable pipeline for natural-language proof discovery, comprising 398 theorem...

---

### 31. Signatures of semantic search in the activations of large language models

**Authors:** Luke Leckie, Peter M. Todd, Jacob G. Foster

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35599v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35599v1)

**Summary:** When recalling lists of concepts (e.g., animals) during the semantic fluency task (SFT), both humans and large language models (LLMs) organise their output into clusters of related items (e.g., sea animals) that are punctuated by strategic switches between clusters. In humans, this pattern can be explained by a semantic foraging process, whereby distinct neural and behavioural signatures accompany within-cluster production ("exploit") and between-cluster switching ("explore"). Whether LLMs likew...

---

### 32. SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents

**Authors:** Saswat Das, Parvati Viswanathan, Daniel Donnelly, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35596v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35596v1)

**Summary:** Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback. However, locally useful updates may persist into later tasks where they produce unsafe behavior, even without direct adversarial influence. To study this risk, we introduce SEABench, a benchmark for studying endogenous misalignment...

---

### 33. Source-preserving alignment for robust evidence localization in scientific PDFS

**Authors:** Zihao Liu, Wei Yang, Zixiao Dong, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35588v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35588v1)

**Summary:** Scientific information-extraction systems often return a claim with an evidence string, which users must locate in the original PDF. This is challenging because the extracted evidence and PDF text layer are different representations: line wrapping, Unicode variants, superscripts, citation markers, and fragmented items alter text sequences and geometry. We present a source-preserving alignment framework: normalize text for robust matching while preserving provenance for accurate localization. It ...

---

### 34. IMC-CLINIC: Coupled Loss-Informed Newton Iterations for Clipping in Analog In-Memory Computing

**Authors:** Yung-Chin Chen, Chia-Yu Chen, Naveen Verma

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35586v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35586v1)

**Summary:** Analog in-memory computing (IMC) offers a promising path toward energy-efficient large language model (LLM) inference by executing matrix multiplications (MatMul) directly within memory arrays in the analog domain. Its efficiency, however, comes with an additional source of error: limited-precision analog-to-digital converters (ADCs) quantize accumulated analog partial sums, introducing output-side error distinct from conventional activation and weight quantization at the MatMul inputs. Clipping...

---

### 35. QC-Stark: A Multi-Task Benchmark Revealing Capability Dissociations in LLMs Evaluated on Quantum Computing Tasks

**Authors:** Pranav Gupta

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35581v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35581v1)

**Summary:** We introduce QC-Stark, a benchmark for evaluating large language models (LLMs) on 11 quantum computing (QC) tasks, spanning circuit construction, debugging, compilation, error correction, and simulation. Across 2,750 evaluations (10 models $\times$ 11 tasks x 5 difficulty levels x 5 seeds), we find that overall rankings mask substantial per-task variation. The Spearman correlation between overall and per-task rankings is statistically insignificant for 4 out of the 11 tasks included in this benc...

---

### 36. FactorEngram: Factorized N-gram Memory with Basis-Level Gating for Language Models

**Authors:** Bowen Yang, Jingbo Zhou, Qinghong Miao, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35578v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35578v1)

**Summary:** Lookup-based memory has been a promising way to scale the parameters of large language models (LLMs). It retrieves learned representations of local token patterns, such as n-grams, instead of reconstructing them through successive layers of computation. However, existing designs such as Engram treat each retrieved embedding as a monolithic unit. Each embedding is stored in its own hashed slot and modulated by a single scalar gate. As a result, polysemous patterns cannot selectively read out the ...

---

### 37. Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents

**Authors:** Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35576v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35576v1)

**Summary:** Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a r...

---

### 38. F4R: Failure-Driven Recognition, Reconstruction, Refinement, and Redeployment for Continual Robot Self-Improvement

**Authors:** Zhuoyuan Yu, Jiacheng Wang, Tianle Liu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35575v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35575v1)

**Summary:** The real-world performance of current vision-language-action models is fundamentally constrained by the limited coverage of expert demonstrations and their insufficient understanding of physical interactions. A common remedy is to collect additional real-world demonstrations of newly encountered failures. However, this process is costly, inefficient, potentially unsafe, and difficult to scale. To address this challenge, we propose Failure for Rising (F4R), a failure-driven real-to-sim-to-real cl...

---

### 39. Representation Alignment as a Bottleneck in LLM-Based Retrosynthesis Planning

**Authors:** Hyunwoo Yoo, Cassie Huang, Haebin Shin, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35571v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35571v1)

**Summary:** While LLMs show promise in general reasoning, symbolic planning in chemistry remains a bottleneck. Direct ''SMILES-to-PDDL'' attempts fail because they force models to juggle chemical analysis and planning-language structuring simultaneously. We hypothesize that this failure stems from a lack of intermediate abstractions rather than insufficient model capacity. By decomposing retrosynthesis into molecule mapping, reaction mapping, and PDDL generation, we achieve high success rates where end-to-e...

---

### 40. Almieyar: A Culturally Grounded Benchmark for Multi-Dialect Arabic Speech Recognition

**Authors:** Omid Ghahroodi, Anas Madkoor, Dima Faris Al Saudi, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35564v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35564v1)

**Summary:** Arabic speech technology has largely focused on Modern Standard Arabic, leaving the living dialects spoken by hundreds of millions under-served. We introduce ALMIEYAR, a culturally grounded ASR benchmark covering 17 Arabic dialects across six families, built entirely from newly recorded speech unseen by existing models. Dialect-community coordinators selected culturally relevant images across 10 topics, and native speakers described them through five structured scenarios, yielding approximately ...

---

### 41. RSI-Master: Structuring Experiments to Guide Autonomous Model Improvement

**Authors:** Yaxin Du, Xiyuan Yang, Zhifan Zhou, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35561v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35561v1)

**Summary:** Recursive self-improvement (RSI) seeks to enable AI systems to participate in improving their own capabilities. A concrete pathway is autonomous model development, where agents iteratively explore post-training strategies to improve a base model. This setting faces two challenges: agents may exploit open-ended experimental actions through hacking, and repeated experimentation may lead to strategy lock-in, where an early direction is refined rather than reconsidered. We introduce RSI-Master, whic...

---

### 42. From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining

**Authors:** Kangcheng Deng, Hui Cai, Jiacheng Lu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35559v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35559v1)

**Summary:** Inference scaling has been shown to improve large language model (LLM) performance, and this principle naturally extends to autonomous LLM agents through increased search budgets, which we refer to as *search scaling*. Although prior work has characterized the mechanisms, scaling behavior, and performance limits of LLM inference scaling, much less is known about these questions in autonomous research. Therefore, we investigate how search scaling affects research performance and what mechanisms d...

---

### 43. The Compiler May Read It, the Agent May Not: Keeping Part of a Research Code Away from a Coding Agent

**Authors:** Shobhan Roy

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35557v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35557v1)

**Summary:** The compiler must read modules a physics-based solver cannot build without; the coding agent must not read that intellectual property. The harness does not ship that rule. We classified fifteen read routes against a container, permission rules and a sandbox. None of the three can tell which program is reading.

---

### 44. BaRe-Mem: Bayesian Reliability Memory for Robust and Adaptive Agent Consultation

**Authors:** Peilin Feng, Zhengyang Huang, Soujanya Poria

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35551v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35551v1)

**Summary:** In multi-agent systems, reliable consultation is challenging because advisor capabilities vary across tasks, and misleading information can make consultation worse than autonomous reasoning. We introduce BaRe-Mem, an online Bayesian reliability memory for multi-agent consultation. It estimates advisor reliability based on the central model's internal belief representations and updates these estimates from historical interactions. These estimates modulate the influence of advisor responses and gu...

---

### 45. RareDx: Controlled Knowledge Integration and Graph-Grounded Policy Optimization for Rare-Disease Diagnosis

**Authors:** Bo Zhang, Yuchen Wang, Dongbai Li, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35549v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35549v1)

**Summary:** Rare-disease diagnosis is a long-tail reasoning problem: phenotypes are incomplete, individual disorders are sparsely documented, and relevant evidence is distributed across ontologies, gene annotations, and biomedical text. Language models consequently favor common conditions, miss rare candidates, or produce plausible but invalid names. We introduce RareDx, which couples controlled evidence use with knowledge-graph-grounded policy optimization. RareDx-Harness normalizes heterogeneous records i...

---

### 46. Graph World Models for Constrained Epidemic Policy Planning

**Authors:** Yiqi Su, Rashed Shelim, Lingyi Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35545v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35545v1)

**Summary:** Epidemic policy planning often requires coordination between geographical regions, taking into account mobility-driven spillovers and how to make use of limited resources. Existing methods either lack action-conditioned models of coupled dynamics or cannot guarantee per-period feasibility. We present EpiMind, a graph world model framework for constrained epidemic policy planning across regions. A graph-factored recurrent state-space model generates joint policy-conditioned rollouts from regional...

---

### 47. Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability

**Authors:** Xu Wang, Difan Zou, Xuansheng Wu

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35544v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35544v1)

**Summary:** Reliable refusal of harmful requests is essential to the safe deployment of language models. Because excessive eagerness to please users may undermine existing refusal capabilities, reducing sycophancy offers a potential route to stronger refusal beyond the harmful scenarios covered by safety training. We investigate this possibility using compensatory feature injection (CFI), a training technique designed to limit the acquisition of a target concept by supplying its associated activation during...

---

### 48. Continuous Context Management

**Authors:** William Hoy, Jingxuan Fan, Nurcin Celik, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35540v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35540v1)

**Summary:** Long-horizon large language model (LLM) agents commonly retain their complete interaction history until compaction is triggered at a predefined threshold. We study Continuous Context Management (CCM), which performs compaction at every turn to prevent interaction history from accumulating in the active prompt. At each turn, a CCM agent emits an updated memory together with an environment action; its next prompt contains the original task, retained memory, and newest observation rather than the c...

---

### 49. ARISE: Adapting to Evolving Capability Gaps in Agentic Reinforcement Learning

**Authors:** Kun Feng, Yuchen Fang, Yiyang Tan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35532v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35532v1)

**Summary:** As a long-horizon agent improves through experience, previously observed weaknesses may recede while new limitations emerge, continually changing what it still needs to learn. Yet the learning process often remains tied to a static view of these needs: fixed behavioral criteria and training priorities can become misaligned with evolving agent capabilities, while sparse task-level feedback makes such misalignment more difficult to detect. Even when capability gaps are identified, rollouts from th...

---

### 50. AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation

**Authors:** Yuta Oshima, Ku Onoda, Yusuke Iwasawa, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35530v1)

**Summary:** Recent image generation models can take multiple reference images as input and combine them into a new image. However, multi-reference image generation remains challenging: models may omit or duplicate subjects from the references, or produce images in which multiple subjects appear unnaturally pasted. Recent work has proposed image generation agents that combine image generation models, reasoning models, and a harness, which is an executable program that specifies how reference images are inter...

---

## cs.CL

**50 papers**

### 1. Telescopic Language Models

**Authors:** Zhilin Guo, Boqiao Zhang, Hakan Aktas, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35769v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35769v1)

**Summary:** One deployed language model must often serve many compute budgets, yet serving each budget still means a separate training or compression run per point. We train a Telescopic Language Model (TLM) to be that continuum: a nested-capacity Transformer supervised by stochastic prefix supervision with a full anchor. At every step, one randomly truncated prefix of the capacity axis is trained against the full next-token target, alongside one full-capacity pass, so the trained artifact is a valid langua...

---

### 2. Retrieving Biblical Intertextual References in Karen Blixen's Seven Gothic Tales

**Authors:** András Kovács, Alexander Conroy, Daniel Hershcovich, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35765v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35765v1)

**Summary:** Identifying intertextual references is central to literary scholarship, but computationally difficult when source material is transformed through paraphrase, allusion, historical language, and translation. We investigate this problem through biblical intertextuality in Karen Blixen's Seven Gothic Tales. Drawing on the commentary to a critical edition, we construct a benchmark of 189 annotated references and evaluate retrieval against all 31,170 verses of historically plausible Danish Old and New...

---

### 3. Scaling Long-Form Story Generation via Narrative State Tracking

**Authors:** Zhennan Wan, Jianfei Chen

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35759v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35759v1)

**Summary:** LLMs have demonstrated strong capabilities in creative writing. However, scaling them to full-length novels remains challenging, as maintaining narrative consistency becomes increasingly difficult. Existing story-generation methods typically focus on stories of up to about ten thousand words, leaving their ability to scale to full-length novels underexplored. In this work, we introduce Narrative State Tracking Agent (NstAgent), a training-free agentic framework that allows LLMs to track a struct...

---

### 4. How to Loop MoE: Flatten the Experts, Untie the Attention

**Authors:** Shouren Wang, Chuang Ma, Mohsen Hariri, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35751v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35751v1)

**Summary:** Looped Transformers reuse one block of layers several times: by spending extra computation they push a model of fixed size further, and so use its parameters more fully; while sparse mixture-of-experts (MoE) models activate only a few of many experts for each token. Looped MoE bridges these two design philosophies and gives MoE models new potential for better expert usage, but it raises a question: how to loop a MoE? We answer it with Foil. With the expert parameters and the expert compute per t...

---

### 5. Towards Communication-Efficient Social Intelligence in Language Agents

**Authors:** Linxiao Gong, Yijie Xu, Tianfu Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35749v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35749v1)

**Summary:** Socially intelligent language agents must negotiate, coordinate, and resolve conflicting preferences while respecting the time and attention of both participants. Balancing these demands is challenging because agents must convey enough to address a partner's constraints and advance their goals without adding words that do not help the interaction. In this paper, we propose Teacher-Assisted Communication Training (TACT) to improve social goal attainment while reducing communication cost, making i...

---

### 6. Improving Test-Time Scaling with Adaptive Looped Transformers

**Authors:** Yichen You, Tianyu Fu, Aosong Feng, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35748v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35748v1)

**Summary:** Looped transformers have demonstrated promising parameter efficiency by reusing layers for latent computation. Prior studies compare looped and non-looped models at matched parameters or per-token FLOPs. However, to the best of our knowledge, whether looping improves test-time scaling as outputs grow longer remains underexplored. Through post-training looped transformers, we study the accuracy-compute slope, measured as the accuracy gain per doubling of test-time decoding FLOPs. We find that exi...

---

### 7. Shockingly Simple Self-retrospection Improves Agentic Models Without RL

**Authors:** Jonathan Light, Christopher Zhang Cui, Jeonghye Kim, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35741v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35741v1)

**Summary:** People learn not only by repeating successful actions, but also by recounting and explaining their experiences, revising their understanding to guide future behavior. Can a language-model agent improve its future actions by training only on explanations of its own experience? We investigate this question by studying Retrospection-Only Fine-Tuning (ROFT), a minimal online procedure designed to isolate the effect of explanation-only training on subsequent behavior. The agent attempts a task, obser...

---

### 8. Harness Learning Enables Generalizable Test-Time Adaptation

**Authors:** Alvin Zhang, Xuecheng Liu, Zixuan Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35738v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35738v1)

**Summary:** A language-model agent is jointly defined by its model and its harness, the executable program that organizes model calls, tool use, and information flow. Because different tasks call for different ways of organizing these operations, the harness needs to be adapted using feedback from the task at hand. We introduce harness learning, which trains a proposer model to revise a solver's harness using execution feedback. We formulate this process as meta-learning over executable programs, with harne...

---

### 9. Reinforcing Agentic Creativity in Scientific Ideation with Night Science

**Authors:** Priyanka Kargupta, Silviu Cucerzan, Shweti Mahajan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35706v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35706v1)

**Summary:** Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discovery, however, spans a broader creative spectrum: from structured day science to loosely structured, serendipitous night science that reaches ideas beyond those typically considered. We introduce AI Night-Scientist, an agentic framework that uses reinforcement learning to teach mod...

---

### 10. Rethinking Personalized Generation: Test-Time Alignment via Factorized Ranking Models

**Authors:** Qiyao Ma, Junshan Zhang, Zhe Zhao

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35695v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35695v1)

**Summary:** Aligning large language models (LLMs) to diverse user preferences is fundamentally hindered by standard alignment paradigms that optimize for monolithic users. In this work, empirical studies are first used to reveal the existence of a massive, untapped performance headroom for personalized generation through test-time alignment. We demonstrate that personalized generation is uniquely suited for test-time scaling methods like Best-of-N (BoN) because it can be viewed primarily as a candidate matc...

---

### 11. QuanReview: Offline, Auditable Reconciliation of Human and LLM Span Annotations

**Authors:** Matteo Musacchio, Juan Cruz Giner Pulero, Isabel Castañeda, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35685v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35685v1)

**Summary:** Structured span annotations, such as quantities with their units, uncertainty modifiers, and event classes, are expensive to create and hard to keep trustworthy once language models enter the loop. We present QuanReview, an open-source system for auditing and correcting such annotation layers. QuanReview aligns two annotation streams over the same documents at character level, resolves unambiguous cases by an explicit and logged policy, and routes candidate conflicts to a browser-based adjudicat...

---

### 12. Tracing the Evolution of Oracle Bone Characters Across Three Millennia

**Authors:** Tianhao Fu, Xinxin Xu, Spike Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35674v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35674v1)

**Summary:** Of the approximately 4,500 Oracle Bone Inscription (OBI) characters discovered from the Shang dynasty, only about 1,600 have been deciphered. Many computational approaches compare OBI with glyphs from one historical period at a time. However, during the evolution of Chinese characters, significant structural or semantic changes often occur in uncertain dynasties. A single-period reference may be insufficient when relevant forms change substantially between observed eras. Therefore, we propose th...

---

### 13. MS-GLA: Multi-Scale Gated Linear Attention for Addressing Representational Bottlenecks via Multi-Temporal Resolution

**Authors:** Prasoon Dev, Anirudh Sankar, Vasudeva Varma

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35664v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35664v1)

**Summary:** Gated Linear Attention (GLA) Transformers advance linear recurrent models through data-dependent gating, but face a core limitation: the fixed-capacity memory matrices across all heads operate at a single temporal resolution, where each token is processed individually, forcing them to simultaneously encode local syntactic patterns and long-range semantic structure, creating a representational bottleneck that gating alone is insufficient to resolve. We introduce Multi-Scale Gated Linear Attention...

---

### 14. Late Attention Layers Alone Can Copy Entity Tokens, but Not Without Attending to Their Context

**Authors:** Muyu He, Yuchen Liu, Ran Tao, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35663v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35663v1)

**Summary:** Large language models (LLMs) reliably perform entity copying, in which a model copies tokens referring to an entity, termed entity tokens, from the prompt into its output to answer a question. Although entity copying is straightforward for most LLMs, existing research does not provide a systematic account of which layers specialize in this fundamental task or how other tokens in the same sequence, termed context tokens, influence the model's ability to copy the entity tokens. To address these qu...

---

### 15. Rubric Rewards from Item Response Theory

**Authors:** Milad Yazdani, Yaser Souri, Xiren Zhou, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35646v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35646v1)

**Summary:** Many language tasks have no single answer that can be checked automatically. Rubrics provide criteria for judging responses to these tasks. For reinforcement learning, the resulting verdicts must be combined into a scalar reward. A common approach sums the points assigned to satisfied criteria. Distinct verdict patterns can thus receive the same reward, and the fixed points encode how much each criterion should count, not how strongly its verdict distinguishes the current rollouts. Beyond this a...

---

### 16. CoSE-E: A Benchmark for Code-switched Speech Evaluation in Enterprise Settings

**Authors:** Shama Gupta, Hoang H Nguyen, Chelsea Huang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35645v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35645v1)

**Summary:** Code-switching (CS), a seamless alternation between languages within a single utterance, remains a critical challenge in automatic speech recognition (ASR). While prior works focus on conversational CS-ASR, enterprise settings demand evaluation of operational impact beyond edit-distance errors: how code-switching transcription errors propagate to downstream voice agent task failures. In this work, we propose (1) a CS-ASR synthetic benchmark and multidimensional evaluation framework tailored to e...

---

### 17. Which the Eye Fears: Writing with Read-Blindness Explains Massive Activations in Transformers

**Authors:** Swagatam Mukhopadhyay, Vishal Vivek Saley, Vraj Parikh, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35630v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35630v1)

**Summary:** Massive activation features (MAs) in Transformers are extreme-value residual-stream features that persist across layers despite the model's ability to suppress them. Why do they survive? Our investigation using an operator-level mechanistic analysis of attention and feed-forward (FFN) blocks reveals that these blocks systematically ignore MA coordinates while reading, but not while writing; creating a read-write asymmetry that blocks corrective feedback while allowing continued accumulation. We ...

---

### 18. SANTA++: Sampling Attention through Representative Keys

**Authors:** Kyle Lee, Christian Z. Pratt, Ruoyu Fang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35629v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35629v1)

**Summary:** Attention often concentrates on a small subset of tokens in the context, but which subset matters changes from one query to the next. To exploit this changing structure, we introduce SANTA++, a training-free stochastic attention method that uses representative keys for memory-efficient selection without scanning the entire key-value (KV) cache. Cached keys are organized into teams, and the query scores one representative from each team to decide which teams to sample. We compute exact attention ...

---

### 19. Can LLMs Value the Right Evidence? Evidence-Value Misalignment in Dynamic Medical Diagnosis

**Authors:** Kehua Feng, Yunsheng Lu, Yitong Qiao, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35627v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35627v1)

**Summary:** A correct diagnosis reached from insufficient or misleading evidence can pose a clinical hazard, yet outcome-based accuracy may reward such lucky guesses. We call this mismatch between diagnostic decisions and the value of available evidence Evidence-Value Misalignment (EVM). To disentangle evidential grounding independently from diagnostic accuracy, we introduce MedEVM, a dynamic benchmarking environment comprising 1,050 cases across 24 disease systems. Observations arrive turn by turn, requiri...

---

### 20. Twist, Don't Tilt: Trajectory-Exact Constrained Decoding for Masked Diffusion Models

**Authors:** Aditya Thimmaiah, Lara Marinov, Jayanth Srinivasa, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35609v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35609v1)

**Summary:** Constrained decoding for Masked Diffusion Language Models (MDLMs) aims to ensure that generated outputs satisfy a specified structure or syntax constraint. MDLMs generate outputs by repeatedly unmasking masked positions present in their current state. Recent strategies for constrained decoding constrain the model's per-step mean-field posterior (which factorizes over masked positions) by enforcing the desired constraint with an automaton. The resulting chain-structured factor graph allows exact ...

---

### 21. Simultaneous Translation between Sign Languages

**Authors:** Zetian Wu, Bowen Xie, Stefan Lee, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35608v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35608v1)

**Summary:** Deaf and hard-of-hearing (DHH) signers cannot converse in real time across different sign languages today: existing sign-to-sign translation systems run offline, requiring the full source clip before any target sign is emitted. Live use cases - e.g. broadcast interpretation and two-way video calls - instead demand simultaneous output, while the source signer is still signing. We present, to our knowledge, the first simultaneous sign-to-sign (S2S) translation system, with two wait-k regimes: test...

---

### 22. TCSAlgBench: Benchmarking Automated Proving for Research-Level Theoretical Computer Science

**Authors:** Chutong Yang, Xiyuan Zhang, Yu Huang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35606v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35606v1)

**Summary:** Large language models perform strongly on competition mathematics, but their research-level reasoning remains difficult to evaluate systematically. Theoretical computer science (TCS) connects algorithm design to explicit guarantees and fundamental limits, providing a setting for evaluating whether models can justify computational improvements with arguments humans can inspect. We introduce TCSAlgBench, a benchmark and reusable pipeline for natural-language proof discovery, comprising 398 theorem...

---

### 23. SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents

**Authors:** Saswat Das, Parvati Viswanathan, Daniel Donnelly, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35596v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35596v1)

**Summary:** Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback. However, locally useful updates may persist into later tasks where they produce unsafe behavior, even without direct adversarial influence. To study this risk, we introduce SEABench, a benchmark for studying endogenous misalignment...

---

### 24. Language Models Act on Hidden Valence

**Authors:** Cameron Berg, Caspar Kaiser

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35591v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35591v1)

**Summary:** Language models describe some internal states as good and others as bad. But whether models have a stake in them is an open question. Simply asking the model is unlikely to be informative. Any answer may be consistent with genuine introspection, superficial pattern-matching, or with fixed scripts learned in character training. We therefore study revealed preference. Rather than asking about a state, we use activation steering to attach a positively or negatively valenced activation pattern to on...

---

### 25. FactorEngram: Factorized N-gram Memory with Basis-Level Gating for Language Models

**Authors:** Bowen Yang, Jingbo Zhou, Qinghong Miao, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35578v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35578v1)

**Summary:** Lookup-based memory has been a promising way to scale the parameters of large language models (LLMs). It retrieves learned representations of local token patterns, such as n-grams, instead of reconstructing them through successive layers of computation. However, existing designs such as Engram treat each retrieved embedding as a monolithic unit. Each embedding is stored in its own hashed slot and modulated by a single scalar gate. As a result, polysemous patterns cannot selectively read out the ...

---

### 26. Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents

**Authors:** Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35576v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35576v1)

**Summary:** Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a r...

---

### 27. Representation Alignment as a Bottleneck in LLM-Based Retrosynthesis Planning

**Authors:** Hyunwoo Yoo, Cassie Huang, Haebin Shin, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35571v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35571v1)

**Summary:** While LLMs show promise in general reasoning, symbolic planning in chemistry remains a bottleneck. Direct ''SMILES-to-PDDL'' attempts fail because they force models to juggle chemical analysis and planning-language structuring simultaneously. We hypothesize that this failure stems from a lack of intermediate abstractions rather than insufficient model capacity. By decomposing retrosynthesis into molecule mapping, reaction mapping, and PDDL generation, we achieve high success rates where end-to-e...

---

### 28. Almieyar: A Culturally Grounded Benchmark for Multi-Dialect Arabic Speech Recognition

**Authors:** Omid Ghahroodi, Anas Madkoor, Dima Faris Al Saudi, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35564v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35564v1)

**Summary:** Arabic speech technology has largely focused on Modern Standard Arabic, leaving the living dialects spoken by hundreds of millions under-served. We introduce ALMIEYAR, a culturally grounded ASR benchmark covering 17 Arabic dialects across six families, built entirely from newly recorded speech unseen by existing models. Dialect-community coordinators selected culturally relevant images across 10 topics, and native speakers described them through five structured scenarios, yielding approximately ...

---

### 29. Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability

**Authors:** Xu Wang, Difan Zou, Xuansheng Wu

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35544v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35544v1)

**Summary:** Reliable refusal of harmful requests is essential to the safe deployment of language models. Because excessive eagerness to please users may undermine existing refusal capabilities, reducing sycophancy offers a potential route to stronger refusal beyond the harmful scenarios covered by safety training. We investigate this possibility using compensatory feature injection (CFI), a training technique designed to limit the acquisition of a target concept by supplying its associated activation during...

---

### 30. Beyond Token Scale: Chunk-Level Sparse Autoencoders for Reliable Semantic Feature Discovery

**Authors:** Xu Wang, Yifan Yang, TingHao YU, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35521v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35521v1)

**Summary:** Sparse autoencoders (SAEs) expose features that help us understand and steer language models, but faithful reconstruction does not guarantee informative concepts. Token-level objectives reward lexical and formatting details alongside semantic content, all competing for a limited sparse budget. We introduce a family of chunk-level SAEs that encode mean-pooled activations over chunks, each a contiguous span of tokens: Mean-Chunk reconstructs the observed chunk, Cross-Chunk predicts an independentl...

---

### 31. Who Is Left of Whom? Tracing Spatial Evidence and Role Binding in Relative-Position Reasoning

**Authors:** Yingjin Song, Denis Paperno, Albert Gatt

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35486v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35486v1)

**Summary:** High instance-level accuracy can mask inconsistencies in spatial reasoning when objects exchange positions or their roles are reversed in the query. The internal representations supporting relative-position reasoning remain poorly understood. We investigate two complementary components of this process: tracking object locations in the input and representing their query roles. Across three VLMs with visual or textual inputs and their language-model backbones, activation patching reveals a staged ...

---

### 32. Spontaneous Context Restoration: How Language Models Recover from Corrupted Inputs

**Authors:** Pranjal Garg, Jacob Beck

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35475v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35475v1)

**Summary:** Language models sometimes produce correct outputs even when their inputs are corrupted by deletion, replacement, or misspelling. We study the internal processes accompanying this behavior, which we call context restoration, in controlled attention-only transformers and five pretrained LLMs (1B-32B parameters) across arithmetic, reading comprehension, and multiple-choice reasoning tasks. In the attention-only transformers, restoration emerges spontaneously despite training exclusively on clean se...

---

### 33. CLIMB: A Clinical Multimorbidity Benchmark for Diagnosing Co-occurring Conditions through Multiturn Conversations

**Authors:** Yusuf Kesmen, Aniruddha Mukherjee, Yena Chang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35462v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35462v1)

**Summary:** Patients often have several co-occurring clinical conditions, and the findings needed to identify and disambiguate them emerge over the course of a consultation. Evaluating clinical reasoning in this setting requires both multi-turn interaction and multi-label diagnosis. We introduce CLIMB, a benchmark in which a doctor model interviews a simulated patient to recover a ground truth set of co-occurring clinical conditions. Cases are synthesized from clinical decision algorithms and diagnostic dat...

---

### 34. AraDynFact: Dynamic Evaluation of Factual Knowledge in Arabic

**Authors:** Ignacio Iacobacci, Faroq Altam, Zhaozhi Qian, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35461v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35461v1)

**Summary:** As Large Language Models (LLMs) continue to scale both in size and capabilities, their proficiency in the Arabic Language has seen significant advancement. However, a critical gap remains: the extent of their factual knowledge and cultural sensitivity to the diverse Arabic-speaking world remains largely underexplored. Current evaluation metrics often focus on translation or generic reasoning, failing to capture the rich historical, social, and regional nuances inherent to Arabic culture. In addi...

---

### 35. LLMs are General Asynchronous Agents

**Authors:** George Yakushev, Denis Mazur, Vladimir Bartenev, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35427v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35427v1)

**Summary:** Modern LLMs are increasingly capable as autonomous agents, but they follow sequential interaction cycles: read, think, reply or call tools, repeat. Many real-world use cases are not sequential: voice assistants, embodied agents, and monitoring systems receive new inputs while they think or perform another task. Modern LLMs address this with specialized architectures for voice interaction and video streams, VLAs for robot control, asynchronous tool calling for API usage, and others. In this work,...

---

### 36. Frontier Learning: Training LLM Reasoners at the Edge of Capability

**Authors:** Robin Faro, Shyam Sundhar Ramesh, Ilija Bogunovic, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35426v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35426v1)

**Summary:** Reinforcement Learning-based post-training of Large Language Models (LLM) has been successfully applied to improve their reasoning capabilities. Existing pipelines primarily finetune LLMs on a fixed pool of problems specified prior to training using the GRPO loss. This is fundamentally limiting, as learning signal arises only when policy rollouts mix successes and failures, causing the useful portion of any fixed pool to quickly become stale as the model improves. To address this, we propose fro...

---

### 37. Semantic Prefix Oracles for LLM Decoding: Contracts and Differential Validation

**Authors:** Paul Kronlund-Drouault

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35425v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35425v1)

**Summary:** Constrained decoding can enforce regular or context-free output formats, but many program-generation failures are semantic: scope, typing, and declaration effects depend on context. We present semantic grammar specifications, a declarative formalism that attaches such constraints to a context-free surface and executes them during Earley descent. Our implementation enforces \emph{safe pruning}: it rejects only prefixes whose semantic contradictions cannot be repaired by any continuation. A separa...

---

### 38. Self-Adapting Group of Experts for Multi-Agent Reasoning

**Authors:** Mohammad Atif Quamar, Nurbek Tastan, Karthik Nandakumar, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35412v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35412v1)

**Summary:** Multi-agent systems bring together language model agents with different roles to propose, review, and refine solutions. Each agent's response depends on its model's capabilities, the reasoning strategy defined by its system prompt, and the information in its input context. Existing frameworks often adapt communication by changing this context while leaving individual prompts fixed, even when a problem calls for different skills. We study whether agents' initial responses can identify a strategy ...

---

### 39. AwarenessBench: Assessing Cognitive Capabilities of Language Models

**Authors:** Xiaojian Li, Rongwu Xu, Tianyun Zhang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35409v1)

**Summary:** As language models (LMs) exhibit increasingly consciousness-like behaviors, evaluating their cognitive abilities becomes essential. We introduce AwarenessBench, the first comprehensive benchmark for assessing the cognitive abilities of LMs in four dimensions: metacognition, self-awareness, social awareness, and situational awareness, covering 15 cognitive functions and 14,381 samples. Evaluating 18 state-of-the-art LMs, we find that all consistently surpass random baselines, with more advanced m...

---

### 40. TRACE: Single-Pass Decoding-Trace Risk Localization for Generation Calibration

**Authors:** Yuebin Xu, Xuemei Peng, Junlan Chen, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35387v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35387v1)

**Summary:** Reliable confidence estimation is essential for large language model deployment. However, answer-level calibration remains challenging because generation errors are often localized: a response may be fluent and high-probability overall while still failing at a critical number, entity, or factual claim. Existing estimators compress token probabilities, sequence likelihoods, entropy, or beam statistics into a global score, which can dilute such local risk signals. We propose TRACE, a single-pass, ...

---

### 41. Multilinguality in Hybrid Attention LLMs

**Authors:** Lucas Bandarkar, Junlin Hu, Chenyuan Yang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35378v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35378v1)

**Summary:** In response to the growing demand for long sequences in agentic and reasoning use cases, many state-of-the-art LLMs combine multiple variants of attention to mitigate the quadratic complexity of traditional softmax attention. These hybrid attention LLMs aim to balance the strengths and limitations of full attention and alternatives based on recurrence. This work presents a first study of how hybrid attention impacts the multilinguality of LLMs. Beyond the impact on long sequences in poorly token...

---

### 42. How Well Can LLMs Simulate Real Learner Evaluations of Educational Feedback?

**Authors:** Momoka Furuhashi, Kouta Nakayama, Takashi Kodama, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35376v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35376v1)

**Summary:** While recent studies have explored human behavior and preference simulation using large language models (LLMs), it remains unclear how well LLMs can simulate subjective evaluations from real learners in educational settings. We investigate this question using real learner evaluation data on feedback for high-school biology questions at both the group and individual levels. We compare performance with and without learner-specific information, such as personality traits and evaluation examples, ac...

---

### 43. Deep Learning Methods in Neuroscience: From Modeling Molecular Mechanisms to Classifying States of Consciousness

**Authors:** Elena Benderskaya, Anastasiia Alifanova, Svetlana Batalova, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35372v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35372v1)

**Summary:** A critical analysis of contemporary approaches to the study of conscious states. The review focuses on methods of classification, clustering, modeling of brain states under anesthesia and identification of measurable neurobiological characteristics of brain function. A comparative analysis was conducted in the following three major areas: automatic detection of states of consciousness using neural networks based on EEG and fMRI data; modeling of the structural-functional dynamics of the brain un...

---

### 44. From Input to Output: A Flexible Agent for Dual-End Interpretation of Sparse Autoencoder Features

**Authors:** Dewen Liu, Zixuan Li, Jonathan Pan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35367v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35367v1)

**Summary:** Sparse autoencoders (SAEs) are an important tool for mechanistic interpretability, but interpreting their many features remains challenging. Existing methods characterize input-side activation patterns and output-side intervention effects, yet often leave their functional connection implicit, while input-side evidence collection typically relies on costly large-corpus scans. We introduce functional interpretation, which characterizes an SAE feature as a mapping from its activating input semantic...

---

### 45. Do Coding Agents Reuse Existing Code or Reinvent the Wheel?

**Authors:** Dongsheng Ma, Sizhe Wang, Xinyi Huang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35357v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35357v1)

**Summary:** Coding agents are increasingly deployed for iterative development on real repositories, yet existing evaluation barely answers a basic question: \emph{do coding agents reuse existing code or reinvent the wheel?} The question matters: every duplicated implementation is a fix applied twice and agents produce code far faster than humans can audit, so redundancy accumulates unsupervised. Thus, we present \textbf{RepoReuse}, a multi-turn benchmark for auditing code reuse in real repositories, where r...

---

### 46. Jailbreaks for Black-Box Uncertainty Quantification in Large Reasoning Models

**Authors:** Lucas Biechy, Cédric Eichler, Adrien Boiret, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35350v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35350v1)

**Summary:** While Large Reasoning Models (LRMs) excel at complex reasoning, alignment through reinforcement learning often induces systemic overconfidence. In production environments, where logits may be unavailable, robust black-box uncertainty quantification (UQ) is essential for trustworthiness and safety. Focusing on question-answering for LRMs, we show that existing black-box methods, such as paraphrase-based self-consistency and confidence verbalization, offer little to no improvement over simple repe...

---

### 47. MemoReason: Evaluating the Effect of Parametric Memory on Contextual Reasoning in LLMs

**Authors:** Zineddine Tighidet, Andrea Mogini, Jiali Mei, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35312v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35312v1)

**Summary:** Large Language Models (LLMs) perform well on reasoning benchmarks, but it remains unclear whether this reflects genuine contextual reasoning or reliance on facts memorized in their parameters. We investigate this by distinguishing two possibilities: a broad \textit{memorization bias}, where familiar content improves reasoning performance, and the \textit{Strong Parametric Shortcut Hypothesis}, where models skip reasoning entirely and recall stored answers. To test these effects, we introduce \te...

---

### 48. Epistemic Policy Divergence in Multi-Turn LLM Contamination: A Protocol-Gradient Investigation

**Authors:** Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35308v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35308v1)

**Summary:** Large language models process conversation history as unverified context: false premises injected into prior turns can be adopted as fact, a failure mode we term session-level contamination. We introduce five contamination protocols arranged along a source-authority gradient, isolating distinct failure mechanisms while holding the false premise constant, and evaluate GPT-5.4 Mini, Gemini-3.1 Flash-Lite, and GLM-4.5-Air across ten knowledge domains at temperature zero (22,500 turns), using a dual...

---

### 49. Decide, Don't Generate: Competitive Dimensional ABSA with Jev's Typed Decisions

**Authors:** Yiqun Zhang, Peidong Wang, Zihan Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35293v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35293v1)

**Summary:** Aspect-based sentiment analysis (ABSA) has largely turned to text generation. We show that competitive dimensional ABSA does not need it. Using Jev, a frozen model that answers typed questions with rubric scores, label probabilities, and yes/no judgments, we decompose all three tasks of SemEval-2026 Task III Track A into such decisions and align them with the annotation scheme through 488 coefficients fitted on CPU, with no text generation and no backbone tuning. On valence-arousal regression ov...

---

### 50. EvoIn: Bridging Evolution and Internalization for Agent Fine-Tuning

**Authors:** Shihan Dou, Shaofan Liu, Zhonghang Lu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35290v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35290v1)

**Summary:** Recent work has explored improving agents by jointly evolving their harnesses and models, but often takes a ''potpourri'' approach that bundles together new tools, new decision-making procedures, and model adaptation to the evolved harness under a single notion of agent improvement. In this paper, we instead investigate how agents can improve their decision-making procedures. In particular, we propose EvoIn, an agent fine-tuning framework that bridges evolution and internalization. EvoIn first a...

---

## cs.CV

**50 papers**

### 1. FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets

**Authors:** Srinjay Sarkar, Prakhar Kaushik, Soumava Paul, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35770v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35770v1)

**Summary:** Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets. Fur usually covers most of an animal's body, with large inter-species and intra-species variability. We present FurE, an efficient strand-based animal fur reconstruction method that recovers a per-strand, editable groom by optimizing a root-conditioned latent field, decoded into strand geometry vi...

---

### 2. PDMD: Projected Distribution Matching Distillation for Video Diffusion Models

**Authors:** Zimo Wang, Junkun Yuan, Angtian Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35768v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35768v1)

**Summary:** Modern video diffusion models require tens of denoising evaluations over long spatiotemporal token sequences. Distribution Matching Distillation (DMD) reduces the number of function evaluations (NFE) to just a few. However, DMD samples can degrade during training, exhibiting progressive oversaturation and artifacts. We trace this instability to critic errors, which enter successive student updates and accumulate over time. We introduce Projected Distribution Matching Distillation (PDMD) to filte...

---

### 3. Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning

**Authors:** Yijia Fan, Ziqi Huang, Zhongang Cai, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35767v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35767v1)

**Summary:** Unified multimodal models can both look at and render images, so in principle they can repair their own generations: diagnose what an image gets wrong, revise it, observe the result, and diagnose again. Whether a revision helps is known only after it is rendered, so the reflection text and the image generation must be learned jointly, over the whole loop. Supervised fine-tuning (SFT) on reflection trajectories gives a cold start but does not find the high-success repair paths, and naive RL that ...

---

### 4. Reliability-Gated Fusion of Consumer Head and Foot IMUs for Lower-Body 3D Pose

**Authors:** Zhilin Guo, Boqiao Zhang, Oszkár Urbán, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35764v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35764v1)

**Summary:** Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions, and streams drift or drop out. On a new 35-take single-subject benchmark pairing an earbud head inertial measurement unit (IMU) with two smart-insole foot IMUs (SAM-3D-Body pseudo-ground-truth labels), we show the reliability problem is channel-level: a channel ablation isolates foot acceleration ...

---

### 5. Copy the Same, Distill the Difference: Initializing Linear Vision Transformers

**Authors:** Huaiyuan Qin, Muli Yang, Gabriel James Goenawan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35745v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35745v1)

**Summary:** Linear Vision Transformers (ViTs) are designed to replace the attention in Softmax ViTs with the linear-complexity attention operator for more efficient token routing, but they require from-scratch pre-training and typically underperform the original Softmax version. How to initialize linear ViTs both efficiently and effectively still remains unclear. In this work, we explicitly ask: given that most foundation ViTs are built on the mainstream Softmax attention, can linear ViTs benefit from their...

---

### 6. InfiniHand: Streaming World-Space Hand Motion Estimation from Egocentric Video

**Authors:** Kerui Ren, Kaiwen Song, Weiguang Zhao, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35743v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35743v1)

**Summary:** World-space hand motion estimation from egocentric video requires recovering 3D articulated hand geometry while tracking camera egomotion. Existing approaches heavily rely on cascading independent hand pose estimators and SLAM systems, resulting in error accumulation, complex pipelines, and severe computational overhead. To address these limitations, we present InfiniHand, an end-to-end streaming feed-forward framework that jointly estimates MANO parameters, camera trajectories, and hand locatio...

---

### 7. GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space

**Authors:** Kerui Ren, Tao Lu, Linning Xu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35734v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35734v1)

**Summary:** Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consi...

---

### 8. FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning

**Authors:** Ziyao Huang, Zhengkun Rong, Shiyang Qin, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35728v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35728v1)

**Summary:** We present FlowAct-R2, a framework for interactive humanoid video generation that combines continuous multimodal control with proactive agent planning. Our method consists of two coupled components. First, a Streaming Multimodal Reference Diffusion Transformer adapts the pretrained Seedance 2.0 Mini reference-to-video backbone to accept rolling action prompts, streaming audio, and dynamically updated image, audio, and video references. Video-driven rotary positional embeddings align reference ch...

---

### 9. Impact of Patient Orientation in Single- and Multi-View Camera Environments for AI-based Rehabilitation Monitoring

**Authors:** Miriama Jánošová, Andreas Lang, Petra Budikova, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35726v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35726v1)

**Summary:** Automated quality assessment of rehabilitation exercises relies heavily on accurate human pose estimation from video data. Although numerous RGB-based pose estimation methods have been proposed, the impact of camera placement on detecting clinically relevant movement errors remains insufficiently explored. To address this gap, we introduce REHAB26-ViewAngles, a dataset comprising correct and incorrect rehabilitation exercise executions captured from a wide range of camera angles. Furthermore, we...

---

### 10. Superquadric Primitive Decomposition of 3D point clouds via Geometric-Aware Inlier Refinement

**Authors:** Alessandro Rinaldi, Edoardo Tedesco, Andrea Ferraris, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35725v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35725v1)

**Summary:** The decomposition of 3D point clouds into interpretable geometric primitives remains a longstanding challenge in Computer Vision and Computer Graphics. Among the available representations, superquadrics offer a compact and expressive model capable of capturing a wide range of shapes. However, their estimation is inherently challenging, as it requires solving a non-linear optimization problem and is particularly sensitive to noise, outliers, and overlapping structures. While robust estimation met...

---

### 11. Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision

**Authors:** Hanoona Rasheed, Mohammed Irfan Kurpath, Bin Ren, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35718v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35718v1)

**Summary:** Frontier general-purpose systems are rapidly expanding beyond visual understanding into capabilities traditionally handled by dedicated computer-vision models. As these capabilities expand, a central question for the computer-vision community is how far this reach extends, and what remains hard. We evaluate GPT-6 Astra alongside five frontier general-purpose AI systems across 34 capabilities and 55 benchmarks spanning nine areas of computer vision. We compare their performance with dedicated mod...

---

### 12. Lagrangian--Hamiltonian Flows for Video Prediction and Image Generation: A Symplectic Perspective

**Authors:** Jiawei Hu

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35710v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35710v1)

**Summary:** We introduce LHFM, a geometric framework for learning image dynamics. Drawing on structures central to classical mechanics, symplectic geometry, and geometric quantization, LHFM represents each image as an exact Lagrangian graph and models its evolution through image-dependent Hamiltonian flows, which yield a transport--source parameterization of image velocities. Our primary application is deterministic video prediction: LHFM-V is a recurrent model that advances frames by integrating predicted ...

---

### 13. Mind the RefGAP: Correcting Reference Attention in Diffusion-Based Visual Editing

**Authors:** Yanan Wang, Shengcai Liao, Guangyi Liu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35708v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35708v1)

**Summary:** Reference-guided diffusion editors struggle to faithfully reproduce user-provided references. We identify a potential bottleneck in diffusion editors: many methods provide limited reference-attention allocation. For example, in LoomVideo, edit-region queries assign less than 1% of their attention mass to the reference. We introduce RefGAP, a training-free correction that determines logit-offset magnitudes online at each layer from the reference-attention mass measured during the forward pass. Po...

---

### 14. DynaTokens: Teaching Dynamics to Camera-Controlled Video Models at Test Time

**Authors:** Ziqi Ma, Hongqiao Chen, Georgia Gkioxari

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35704v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35704v1)

**Summary:** Video generation must account for two sources of motion, one induced by the observer's camera path and the other caused by scene dynamics. An ideal camera-controlled video model should account for both motions: let users move the camera while evolving the scene dynamics. While current models handle camera-induced motion well in static settings, they struggle for dynamic scenes: objects are static, move incorrectly, or degrade in generation quality. We introduce DynaTokens, a lightweight set of l...

---

### 15. FlowTool: Controlling Tool Parameter in Image Retouching via Flow Matching

**Authors:** Thanh-Long V. Le, Steven Walton, Seunghyun Yoon, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35673v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35673v1)

**Summary:** Tool-based image editing (image retouching) is commonly formulated with autoregressive multimodal large language models (MLLMs) that sequentially generate reasoning, tool selections, and parameter values. In this work, we present a novel approach to tool-based image editing by framing the task as a flow matching problem. We introduce FlowTool, a framework that directly models the distribution of high-quality tool parameters conditioned on the input image and user instruction using conditional re...

---

### 16. Many Eyes, One World: Feed-Forward 3D Reconstruction from Mixed Cameras

**Authors:** Qiaoge Li, Yifan Zhan, Haijun Yang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35658v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35658v1)

**Summary:** Real-world capture is heterogeneous: perspective, fisheye, and $360^\circ$ panoramic images can coexist within a single reconstruction task, yet most feed-forward 3D reconstruction models assume perspective imagery and a uniform input representation. Recent models handling several camera types are either informed of the camera type for each view or reconstruct one image pair at a time. No single-pass method reconstructs mixed-camera tuples containing full panoramas from images alone. We present ...

---

### 17. Verifiable Visual Rewards Transfer from Synthetic Scenes to Natural Prompts

**Authors:** Shuyue Stella Li, Xiaochuang Han, Yulia Tsvetkov, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35641v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35641v1)

**Summary:** Precise instruction following in image generation, such as satisfying object counts and spatial relations, remains an open challenge at least in part because it is learned using unreliable reward models such as object detectors and vision-language models. We introduce Verifiable Visual Rewards (VVR), the first framework for programmatically verifiable image rewards, and show that training on it generalizes to natural prompts. Each VVR task is a scene of geometric objects and relations among them...

---

### 18. RT-Super: Learning Tumor Segmentation from Longitudinal Images and Reports

**Authors:** Pedro R. A. S. Bassi, Wenxuan Li, Hanxue Gu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35637v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35637v1)

**Summary:** Multi-tumor segmentation is important for early cancer detection and allows radiologists to visualize, verify, and understand AI predictions. However, tumor segmentation masks are expensive, time-consuming, and unavailable for many tumor types in public data. Instead, hospitals have vast, readily available data that can guide segmentation: radiology reports, longitudinal images, and multi-phase images. We use this readily available data to substitute for tumor masks in training AI for tumor segm...

---

### 19. EvolvingAvatar: Interactive 3D Head Generation That Adapts as Conversations Unfold

**Authors:** Junjie Chen, Fei Wang, Kun Li, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35616v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35616v1)

**Summary:** Interactive 3D head generation requires coordinated speaking and listening motion that responds to an evolving conversation. Existing generators use incoming observations as context but keep their parameters fixed, leaving conversational patterns unused as a learning signal. We introduce EvolvingAvatar, a causal generator that uses test-time training to adapt to user face video and dyadic audio during interaction. Its dyadic context prediction objective provides a self-supervised learning signal...

---

### 20. Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering

**Authors:** Jiaming Kang, Zhengxia Zou, Zhenwei Shi

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35612v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35612v1)

**Summary:** Remote sensing novel view synthesis under sparse observations remains challenging due to insufficient geometric constraints and limited cross-view supervision. Existing Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) methods are prone to overfitting and face challenges of depth ambiguities, missing cross-view information, and insufficient constraints in under-observed regions. To address these challenges, we propose DIBR-GS, a neural Gaussian Splatting framework that exploits Dept...

---

### 21. On-Policy Self-Distillation for Multi-Turn Image Editing

**Authors:** Liangbing Zhao, Le Zhuo, Mohamed Elhoseiny

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35611v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35611v1)

**Summary:** Instruction-based image editing has achieved strong performance in single-turn settings, yet practical editing is often iterative, with each instruction applied to the output of the previous turn. We find that existing editing models degrade rapidly under recursive editing and attribute this failure to a train-test mismatch in the conditioning distribution: models are trained on clean source images but must repeatedly condition on their own imperfect outputs at inference time. To address this, w...

---

### 22. Simultaneous Translation between Sign Languages

**Authors:** Zetian Wu, Bowen Xie, Stefan Lee, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35608v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35608v1)

**Summary:** Deaf and hard-of-hearing (DHH) signers cannot converse in real time across different sign languages today: existing sign-to-sign translation systems run offline, requiring the full source clip before any target sign is emitted. Live use cases - e.g. broadcast interpretation and two-way video calls - instead demand simultaneous output, while the source signer is still signing. We present, to our knowledge, the first simultaneous sign-to-sign (S2S) translation system, with two wait-k regimes: test...

---

### 23. ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers

**Authors:** Yongsung Kim, Jaehoon Lee, Minjun Park, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35593v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35593v1)

**Summary:** 3D vision transformers such as VGGT predict camera poses and scene geometry from multi-view images in a single forward pass, but their global attention over all concatenated view tokens dominates computation as the number of views grows. To reduce this cost, SparseVGGT and HeSS sparsify attention at the block level, and both retain blocks with high attention probability. However, we observe that attention probability poorly predicts how much the model's behavior actually changes when a block is ...

---

### 24. What Paired Evaluations Reveal under Visual Perturbations

**Authors:** Yongda Wei, Chen Zhang, Yifei Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35583v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35583v1)

**Summary:** Robustness evaluation must examine diverse visual perturbations, while benchmarks cover only some real-world conditions and physical testing is costly. Paired evaluations link clean and perturbed predictions for the same image, capturing changes in correctness, confidence, and acceptance beyond aggregate accuracy. We investigate how this image correspondence supports two needs in robustness evaluation: interpreting paired evaluation results and prioritizing samples for physical testing. To inter...

---

### 25. Less Is More: Genetic Frame Selection for Efficient Novel View Synthesis

**Authors:** Diego E. Farchione, Ramzi Idoughi, Alberto Jaspe-Villanueva, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35573v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35573v1)

**Summary:** Feed-forward novel view synthesis reconstructs a scene from many input images in a single forward pass, yet more views do not necessarily improve performance: redundant or poorly chosen frames increase computational cost and may degrade reconstruction quality. We address the problem of selecting, from an already captured sequence, a fixed-size subset of input views that is most informative for reconstructing specified target viewpoints. We propose a render-free view selector that scores candidat...

---

### 26. EdgeVLN: Runtime-Aware Deployment Ready Quantized Vision Language Navigation Model

**Authors:** Rithvik Jonna, Man Namgung, Aakash Gurram, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35570v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35570v1)

**Summary:** Vision-language navigation (VLN) models perform well but target compute-rich platforms, limiting deployment on memory- and power-constrained robotic edge devices. Compression alone does not establish whether a VLN model fits the memory, latency, and energy budgets of an edge platform while preserving navigation behavior. We introduce EdgeVLN, a runtime-aware, deployment-ready quantized VLN model that closes this gap. EdgeVLN combines a quantized StreamVLN model with Latent Trajectory Termination...

---

### 27. Revisiting Risky Tackle Detection with Vision Transformers

**Authors:** Syed Ahsan Masud Zaidi, Lior Shamir, Scott Dietrich

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35562v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35562v1)

**Summary:** This paper is a Track 2 reproducibility companion to an ICPR 2026 study on risky tackle detection in American football prac- tice videos. The original work fine-tuned a Video Vision Transformer (ViViT) on 733 clips labeled with the SATT-3 rubric. It used focal loss, Taguchi L18 augmentation, and 5-fold cross-validation. It reported risky- class recall of 0.67 and risky-class F1 of 0.59. This companion documents the released artifact and traces those numbers to specific scripts, fold out- puts, a...

---

### 28. WorldPlay2: Extending Real-Time Interactive World Models in Control and Horizon

**Authors:** Haiyu Zhang, Wenqiang Sun, Tengfei Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35560v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35560v1)

**Summary:** Interactive world models require responding in real time to versatile controls and maintaining long-horizon consistency. However, modeling heterogeneous controls remains difficult, while explosive contexts and unstable distillation impede achieving both long-horizon consistency and real-time responsiveness. In this paper, we present WorldPlay2, an interactive world model that couples a factorized hybrid control interface with a co-design of compressed memory and stable distillation. 1) Our facto...

---

### 29. Learning to Reason with Persistent Object States for Video Instance Segmentation

**Authors:** Yongxue Xu, Boxue Yang, Ziqian Liu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35539v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35539v1)

**Summary:** Video segmentation models maintain object identities by carrying instance information across frames. Under prolonged occlusion, reappearance, or interactions between similar instances, however, an unreliable update can overwrite a valid history and cause persistent identity drift. We introduce POSReasoner, a trainable, plug-and-play framework that explicitly decides when an observation should change an object's state. Each persistent state records identity, confidence, and absence history. A spa...

---

### 30. Look Before You Judge: Training-Free Region Mining for Grounded and Explainable Deepfake Detection

**Authors:** Chia-Ling Chen, Yu-Ting Ta, Jian-Yu Jiang-Lin, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35536v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35536v1)

**Summary:** Multimodal large language models (MLLMs) can explain deepfake verdicts in natural language, but such explanations are not necessarily visually grounded in the visual evidence underlying the prediction. A model may describe plausible artifacts inferred from language priors rather than from image evidence. Existing grounding methods improve visual reliance through decoding or attention interventions, but they generally strengthen grounding over the entire image, making them ill-suited for forensic...

---

### 31. AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation

**Authors:** Yuta Oshima, Ku Onoda, Yusuke Iwasawa, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35530v1)

**Summary:** Recent image generation models can take multiple reference images as input and combine them into a new image. However, multi-reference image generation remains challenging: models may omit or duplicate subjects from the references, or produce images in which multiple subjects appear unnaturally pasted. Recent work has proposed image generation agents that combine image generation models, reasoning models, and a harness, which is an executable program that specifies how reference images are inter...

---

### 32. ReVA: A Scene-Centric Dataset Beyond Repetition for Remote Sensing Video Question Answering

**Authors:** Zhen Yao, Likai Wang, Yuming Yang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35507v1)

**Summary:** Multimodal Large Language Models (MLLMs) have demonstrated remarkable advances in remote sensing. However, existing remote sensing multimodal reasoning benchmarks exhibit two critical limitations: they rely on (i) template-driven questions, which causes repetitive questions; and (ii) static images that fail to capture the inherent temporal nature of drone/UAV videos. This leaves systematic evaluation of remote sensing video reasoning largely unexplored. To address this gap, we introduce ReVA, a ...

---

### 33. SolveEdit: Benchmarking Visual Problem Solving in Generative Models

**Authors:** Wenjie Shu, Yexin Liu, Harold Haodong Chen, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35504v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35504v1)

**Summary:** Machine intelligence is often evaluated through abstract reasoning problems, yet many real-world problems are visual, such as arranging objects, repairing layouts, or tracing routes. Solving these problems requires understanding a scene, inferring what must change to achieve a goal, and realizing that change without disturbing unrelated content. However, existing benchmarks mainly evaluate perception, generation, or explicitly specified transformations, leaving goal-driven visual problem solving...

---

### 34. Sprout: Building Dynamic Memory While Reasoning for Agentic Video Understanding

**Authors:** Wei Chen, Xuanyu Zheng, Yancheng Long, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35497v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35497v1)

**Summary:** Long video understanding relies on video memory to overcome the context limits of multimodal large language models. Existing methods follow a build-then-reasoning pipeline: memory is built offline for the entire video, then reasoned over as a static source. In practice a long video is shared by several questions, and this pipeline is costly at both ends: with few questions, building memory for the whole video costs far more than answering them; with many questions, the memory is never updated, s...

---

### 35. From Scores to Samples: Elastic Forcing for Autoregressive Video Generation

**Authors:** Chi Zhang, Yueyi Liu, Haoyang Shi, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35491v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35491v1)

**Summary:** Few-step autoregressive video generation commonly relies on Distribution Matching Distillation (DMD), requiring a bidirectional diffusion teacher and an online fake-score model. We instead learn the rollout distribution directly from reference videos, eliminating both score models during post-training. Our framework minimizes maximum mean discrepancy (MMD) in frozen self-supervised video representation spaces, using a hybrid Nyström--Monte Carlo estimator to balance approximation bias and sampli...

---

### 36. AHMAD: Adaptive Hybrid Multi-task Vision Learning with Assisted Distillation for Keypoint Detection

**Authors:** Mohammad Mahdi, Nedyalko Prisadnikov, Yuqian Fu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35490v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35490v1)

**Summary:** Generalist multitasking vision models aim to unify multiple vision tasks within a single framework, enabling more efficient and versatile learning. However, handling diverse vision tasks -- spanning dense and sparse predictions -- remains challenging due to their inherently varying output structures. In this paper, we propose AHMAD, a simple yet effective framework for generalist multitask learning that integrates different key vision tasks: semantic segmentation, instance segmentation, depth es...

---

### 37. Who Is Left of Whom? Tracing Spatial Evidence and Role Binding in Relative-Position Reasoning

**Authors:** Yingjin Song, Denis Paperno, Albert Gatt

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35486v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35486v1)

**Summary:** High instance-level accuracy can mask inconsistencies in spatial reasoning when objects exchange positions or their roles are reversed in the query. The internal representations supporting relative-position reasoning remain poorly understood. We investigate two complementary components of this process: tracking object locations in the input and representing their query roles. Across three VLMs with visual or textual inputs and their language-model backbones, activation patching reveals a staged ...

---

### 38. Handwritten Text Recognition Lives in the High-Pixel Variance Subspace

**Authors:** Carlos Garrido-Munoz, Jorge Calvo-Zaragoza

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35473v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35473v1)

**Summary:** In self-supervised pretraining for Handwritten Text Recognition (HTR), pixel reconstruction methods outperform contrastive methods, unlike in natural-image classification. We argue that this difference follows from where discriminative signal lies in pixel space: for HTR, it is concentrated in high-variance directions and largely absent from low-variance ones. This predicts that objectives preserving high-variance pixel content will transfer best. We test six SSL methods from three families (pix...

---

### 39. W2Rep: Learning Visual Representations by Watching the World Change

**Authors:** Wen Huang, Hang Guo, Jiarui Yang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35464v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35464v1)

**Summary:** Images capture the world at one moment, whereas video reveals how it changes. Image self-supervision learns spatial structure from a single moment, while video methods commonly learn temporal relationships inside a representation computed jointly from several frames. We ask whether watching a scene change can instead improve features available from one image without sacrificing the ability to represent video. We introduce W2Rep, a masked feature-prediction framework in which an independently enc...

---

### 40. How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining

**Authors:** Lin Chen, Bolin Ni, Qi Yang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35457v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35457v1)

**Summary:** Most modern multimodal large language models (MLLMs) build on a pretrained visual encoder that provides a strong visual prior. Encoder-free MLLMs instead learn visual representations directly from raw pixels, offering a simple and unified architecture, but their scaling behavior has not been systematically characterized. To fill this gap, we compare scaling laws for encoder-free and encoder-based MLLMs and report three main findings: (1) Removing the visual encoder shifts the compute-optimal all...

---

### 41. From internal representations to model improvement through prediction errors

**Authors:** Yushi Nakaya, Kenichi Higuchi, Shuichi Ishida

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35449v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35449v1)

**Summary:** With limited annotation budgets, choosing which images to label determines how much a model improves. Data-selection methods that use features from a separately trained model, or scene descriptions written by vision-language models, have been successful, but those signals do not directly capture changes in the model being improved. The target model's own internal features reflect what it has learned so far and change with retraining, making them a natural cue for choosing the next training data....

---

### 42. DiMoP: Diffusion-Driven Motion Representation Learning With Frame-Level Pseudo-Classification for Skeleton-Based Action Recognition

**Authors:** Shanaka Ramesh Gunasekara, Wanqing Li, Nikalal Kaldera, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35444v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35444v1)

**Summary:** Robust skeleton-based action recognition requires representations that capture a wide spectrum of motions, from subtle to moderate and strong ones. Existing methods often focus on strong motions. This paper introduces DiMoP, a masking- and diffusion-driven motion representation learning method with frame-level pseudo-classification to explicitly learn the distribution of joint motions rather than regressing deterministic coordinates, as existing methods often do. By diffusing masked joints with ...

---

### 43. Revision, Not Restart: Revisable Visual Plans for Closed-Loop World-Action Models

**Authors:** Pengyiang Liu, Junbo Niu, Wenhao Zheng, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35439v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35439v1)

**Summary:** World-action models use predicted visual futures to condition robot actions, yet execution feedback can invalidate parts of a prediction while leaving its task structure useful. We propose Revisable Temporal Planning (RTP), which maintains the visual future as a persistent action condition and revises it after feedback. Its central mechanism is a learned revision bridge: it resumes an intermediate state saved during visual generation and adapts its continuation to current observations. Visual an...

---

### 44. An integrated geometric quantification and shape analysis framework for axillary lymph node metastasis in breast cancer patients

**Authors:** Zixi Yi, Limeng Qu, Gary P. T. Choi

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35437v1)

**Summary:** Quantitative characterization of lymph node morphology is important for assessing axillary lymph node metastasis in breast cancer. However, surfaces reconstructed from computed tomography (CT) segmentation may contain geometric and topological defects that compromise subsequent analysis, while conventional shape descriptors predominantly characterize global morphology. To address these issues, we developed an integrated framework combining topology-aware surface processing with multi-resolution ...

---

### 45. Automated Species Identification in Camera Trap Images for Wildlife Conservation

**Authors:** Nowshin Amin, Nafisa Tabassum Oyshi, Tahmid Abrar Zidan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35420v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35420v1)

**Summary:** Wildlife conservation involves protecting, preserving, and managing wildlife species and their habitats. With today's rapid pace of human development, climate change, and other unsustainable practices, the need for wildlife conservation has heightened. Despite significant progress in species identification using deep-learning models, significant challenges still remain in effectively detecting small animals in low-contrast trap images due to limited feature extraction capabilities. This thesis p...

---

### 46. When Should the Count Change? Learning State Maintenance for Causal Video Counting

**Authors:** Pengyiang Liu, Dongyue Lyu, Junbo Niu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35416v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35416v1)

**Summary:** Continuous video counting requires distinguishing new observations from new objects or completed events. We introduce StaMina (State Maintenance), which learns to maintain counting state through state-conditioned updates. Recurrent visual context supports recognition; learned transitions maintain visibility, persistent identities, and completed-event records. A differentiable recurrence trains event transitions over legal paths constrained by count endpoints; visibility and association objective...

---

### 47. Adaptive Safety Filtering for Frozen ACC Policies via Conformal Residual Calibration

**Authors:** Zhiruo Zhou, Rigaudiere Z. Li, Chen Xiwen, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35415v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35415v1)

**Summary:** Frozen adaptive cruise control (ACC) policies can violate constraints when deployment dynamics differ from their training conditions. We propose residual-aware conformal action filtering (RACF), which calibrates residuals of a fixed nominal predictor and converts their quantile into an operating margin for finite-model action projection. Completed transitions update margins and candidate selection without retraining the policy. In a registered comparison over 2,400 controller-trial units, Adapti...

---

### 48. Spectral Super-Resolution using Spatial-Spectral Residual Operator Networks

**Authors:** Seokhyun Chin

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35410v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35410v1)

**Summary:** Spectral super-resolution of multispectral satellite images can enable high temporal- and spatial-resolution hyperspectral satellite imagery at a modest cost, significantly increasing the applicability of hyperspectral remote sensing. This task is inherently ill-posed, making it well-suited for deep learning-based methods. In this study, the spectral super-resolution task is framed as an operator learning problem, and SSRON is proposed as a Deep Operator Network that effectively learns function-...

---

### 49. BiMoGen: Bidirectional Motion-Text Generation via Unified Masked Discrete Diffusion

**Authors:** Wanjiang Weng, Yongliang Wu, Xiaofeng Tan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35407v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35407v1)

**Summary:** Text-to-motion generation and motion-to-text captioning are two fundamental tasks in human motion modeling, both grounded in the same underlying motion-text correspondence. Existing unified approaches mostly rely on autoregressive modeling, which imposes a fixed generation order and is therefore poorly suited to the bidirectional dependencies between language and motion, allowing early prediction errors to persist as fixed context and degrade both temporal coherence and cross-modal consistency. ...

---

### 50. Reduce, Then Encode: Multiscale Volumetric Reduction for 2D Foundation Models in Brain MRI

**Authors:** Dexuan Ding, Yuankai Qi, Bogong Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35405v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35405v1)

**Summary:** Pretrained 2D foundation models offer a practical alternative to dedicated 3D pretraining for brain structural magnetic resonance imaging (sMRI), but their use on volumetric data requires bridging the mismatch between a 2D encoder and a 3D volume input. Existing methods typically encode slices independently and integrate their features afterwards. We introduce Multiscale Volumetric Reduction (MVR), a reduce-then-encode approach that compresses each anatomical view from (D) slices into (M << D) c...

---

## cs.LG

**50 papers**

### 1. PDMD: Projected Distribution Matching Distillation for Video Diffusion Models

**Authors:** Zimo Wang, Junkun Yuan, Angtian Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35768v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35768v1)

**Summary:** Modern video diffusion models require tens of denoising evaluations over long spatiotemporal token sequences. Distribution Matching Distillation (DMD) reduces the number of function evaluations (NFE) to just a few. However, DMD samples can degrade during training, exhibiting progressive oversaturation and artifacts. We trace this instability to critic errors, which enter successive student updates and accumulate over time. We introduce Projected Distribution Matching Distillation (PDMD) to filte...

---

### 2. Unifying Distributional Training for One-Step Visual Generation

**Authors:** Chi Zhang, Haoyang Shi, Yueyi Liu, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35763v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35763v1)

**Summary:** \emph{Distributional training} provides collective supervision for one-step visual generation by matching real and generated features in frozen representation spaces. We introduce \emph{a unified theoretical framework} that separates distribution modeling from matching discrepancy and connects global objectives to pointwise feature updates through Wasserstein gradient flow. Under this framework, FD-Loss and Gaussian-kernel Drifting are recovered through Gaussian optimal transport and kernel-dens...

---

### 3. TokenCast: Forecasting Token Consumption During LLM Agent Execution

**Authors:** Chaoqian Ouyang, Ling Yue, Libin Zheng, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35760v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35760v1)

**Summary:** When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction must be revised as the run unfolds. In this paper, we propose TokenCast, which learns a composable cos...

---

### 4. Statistical Learning of Contractive Dynamical Representations for Composite Adaptive Control

**Authors:** Min Kim, José Leonardo Brenes, Fred Hadaegh, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35758v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35758v1)

**Summary:** We present a representation-learning framework for composite adaptive tracking control under dynamically coupled disturbances. The framework connects classical disturbance-accommodating control (DAC) to recent last-layer adaptive disturbance-rejection methods. Specifically, we introduce a statistically principled hard expectation-maximization (hard-EM) procedure, with a Kalman smoother in the hard E-step, to identify dynamical representations of disturbance whose latent evolution is uniformly co...

---

### 5. Neural Harmonic Measure Operator

**Authors:** Jinjin He, Sinan Wang, Yuchen Sun, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35752v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35752v1)

**Summary:** We introduce Neural Harmonic Measure Operator (NHMO), a neural solver for elliptic PDE problems on variable-shape domains. The harmonic measure of a domain is the boundary probability distribution that, integrated against any boundary data, returns the Dirichlet Laplace solution. It depends only on the geometry, not on the boundary data. NHMO parameterizes the density of this measure as a transformer-based boundary kernel supervised by Walk-on-Spheres exit samples, so one trained kernel handles ...

---

### 6. How to Loop MoE: Flatten the Experts, Untie the Attention

**Authors:** Shouren Wang, Chuang Ma, Mohsen Hariri, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35751v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35751v1)

**Summary:** Looped Transformers reuse one block of layers several times: by spending extra computation they push a model of fixed size further, and so use its parameters more fully; while sparse mixture-of-experts (MoE) models activate only a few of many experts for each token. Looped MoE bridges these two design philosophies and gives MoE models new potential for better expert usage, but it raises a question: how to loop a MoE? We answer it with Foil. With the expert parameters and the expert compute per t...

---

### 7. KV-streams for Efficient Compaction in Agentic Reinforcement Learning

**Authors:** Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35750v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35750v1)

**Summary:** Scaling the horizon of agentic LLMs is bottlenecked by the need to fit ever longer context traces in GPU memory. Context compaction has been the most popular mechanism to alleviate this issue, keeping GPU memory constant for a given trace. Unfortunately, most compaction strategies rely on prefilling the LLM context many times over, hindering training throughput. To alleviate this bottleneck and enable efficient trainable compaction, we propose KV-streams, a plug-and-play strategy compatible with...

---

### 8. Improving Test-Time Scaling with Adaptive Looped Transformers

**Authors:** Yichen You, Tianyu Fu, Aosong Feng, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35748v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35748v1)

**Summary:** Looped transformers have demonstrated promising parameter efficiency by reusing layers for latent computation. Prior studies compare looped and non-looped models at matched parameters or per-token FLOPs. However, to the best of our knowledge, whether looping improves test-time scaling as outputs grow longer remains underexplored. Through post-training looped transformers, we study the accuracy-compute slope, measured as the accuracy gain per doubling of test-time decoding FLOPs. We find that exi...

---

### 9. Copy the Same, Distill the Difference: Initializing Linear Vision Transformers

**Authors:** Huaiyuan Qin, Muli Yang, Gabriel James Goenawan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35745v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35745v1)

**Summary:** Linear Vision Transformers (ViTs) are designed to replace the attention in Softmax ViTs with the linear-complexity attention operator for more efficient token routing, but they require from-scratch pre-training and typically underperform the original Softmax version. How to initialize linear ViTs both efficiently and effectively still remains unclear. In this work, we explicitly ask: given that most foundation ViTs are built on the mainstream Softmax attention, can linear ViTs benefit from their...

---

### 10. Harness Learning Enables Generalizable Test-Time Adaptation

**Authors:** Alvin Zhang, Xuecheng Liu, Zixuan Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35738v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35738v1)

**Summary:** A language-model agent is jointly defined by its model and its harness, the executable program that organizes model calls, tool use, and information flow. Because different tasks call for different ways of organizing these operations, the harness needs to be adapted using feedback from the task at hand. We introduce harness learning, which trains a proposer model to revise a solver's harness using execution feedback. We formulate this process as meta-learning over executable programs, with harne...

---

### 11. X-Reset: Scaling Object-Centric Reinforcement Learning via Cross-Embodiment Resets

**Authors:** Prithwish Dan, Chenyang Ma, Wei Zhan

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35715v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35715v1)

**Summary:** Reinforcement learning (RL) in simulation can train dexterous manipulation policies without robot demonstrations, but training a single generalist policy with task-agnostic rewards faces a severe exploration problem: approaching, grasping, and reorienting diverse objects with many degrees of freedom is difficult to discover from scratch. Prior works make exploration tractable with high-quality robot demonstrations, per-task reward shaping, or by restricting policies to narrow modes of behavior. ...

---

### 12. ScAn-Bench: Evaluating Scaling Analysis Methodology

**Authors:** Artin Sermaxhaj, Nastaran Alipour, Donat Sinani, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35707v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35707v1)

**Summary:** Recent progress in machine learning is driven by large-scale foundation models, where scaling laws and finding optimal scaling prescriptions for architecture, data, and hyperparameters are key in advancing the state-of-the-art. Therefore, it is surprising that no systematic study evaluates the methodology to obtain scaling laws and prescriptions across different model types. To shed light on this crucial blind spot and facilitate future research, we introduce the surrogate benchmarks ScAn-Bench-...

---

### 13. A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion

**Authors:** Fred Xu, Thomas Markovich, Florence Regol, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35703v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35703v1)

**Summary:** Reliable deployment of graph neural networks requires calibration, out-of-distribution (OOD) detection, and robustness to distribution shift, yet existing methods address these needs with separate models and   objectives. We model uncertain node embeddings as random graph signals: graph Fourier filters capture structural variation, and a scalar orthogonal-polynomial chaos coordinate captures latent stochastic   variation. The resulting doubly-spectral stochastic (DSS) expansion supplies task-mat...

---

### 14. MeqMuon: Matrix-Equilibrating Muon for LLM Pretraining

**Authors:** Chang-Wei Shi, Xu Wang, Wu-Jun Li

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35701v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35701v1)

**Summary:** The success of large language models (LLMs) has been accompanied by continued growth in model size and pretraining costs. Muon offers high accuracy and training efficiency in LLM pretraining. Recent work introduces row-wise normalization into Muon to balance update magnitudes and improve pretraining performance. However, row-wise normalization alone cannot accommodate different imbalance patterns in update matrices. In this paper, we propose an improved Muon optimizer, called \underline{m}atrix-...

---

### 15. Distillation Defenses Easily Break After Reinforcement Learning

**Authors:** Shidan Javaheri, Alexander Panfilov, Oliver Britton, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35699v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35699v1)

**Summary:** Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect a large volume of frontier model reasoning traces and then train (i.e., "distill") their own models on these traces. Existing defenses against distillation attacks are typically evaluated immediately after distillation, implicitly assuming attackers do not train their models any further. In this pa...

---

### 16. Provable Benefits of Regularization: Fast Rates for Adversarial Imitation Learning

**Authors:** Hanbin Zhou, Shangzhe Li, Alexander Braverman, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35698v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35698v1)

**Summary:** We study adversarial imitation learning (AIL), in which an agent learns to imitate expert demonstrations by optimizing a policy against an adversarial reward that distinguishes expert and learner behavior. Historically, reward regularization and entropy-based policy regularization are key components of empirically successful methods such as GAIL and LS-IQ, yet their finite-sample benefits remain underexplored. We establish fast rates for jointly regularized AIL in finite-horizon Markov decision ...

---

### 17. Rethinking Personalized Generation: Test-Time Alignment via Factorized Ranking Models

**Authors:** Qiyao Ma, Junshan Zhang, Zhe Zhao

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35695v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35695v1)

**Summary:** Aligning large language models (LLMs) to diverse user preferences is fundamentally hindered by standard alignment paradigms that optimize for monolithic users. In this work, empirical studies are first used to reveal the existence of a massive, untapped performance headroom for personalized generation through test-time alignment. We demonstrate that personalized generation is uniquely suited for test-time scaling methods like Best-of-N (BoN) because it can be viewed primarily as a candidate matc...

---

### 18. Rethinking Circuit Evaluation: Do Circuits Explain Model Errors?

**Authors:** Li Zhang, Chuqin Geng, Mark Zhang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35686v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35686v1)

**Summary:** Mechanistic interpretability (MI) aims to explain a model's behaviour through analyzing its internal computations; circuit-based explanations aim to isolate these computations with compact subnetworks validated by ablating the rest of the model. We show that circuits validated this way may fail to recover the underlying mechanism of the model's behaviour by closely reproducing its successful decisions while failing to account for most of its errors. Such explanations should account for the model...

---

### 19. The Hidden Perception Constraint in Task-Aware Compression

**Authors:** Sahan Liyanaarachchi, Semih Akkoc, Sennur Ulukus, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35684v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35684v1)

**Summary:** With the recent advancements of neural compressors, explicitly incorporating perception constraints into the design of compression schemes has gained significant attention. Traditionally, these perception constraints ensure that the distribution of the reconstruction does not significantly deviate from the distribution of the source, thus attesting to the perceptual quality of the reconstruction. In this work, we uncover several perception constraints that are naturally present in task-aware com...

---

### 20. Learned Preconditioning for a Primal-Dual Interior-Point Method

**Authors:** Abhinav Madabhushi, Jialin Liu, Minxin Zhang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35665v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35665v1)

**Summary:** Interior-point methods (IPMs) are among the most widely used algorithms for constrained optimization, yet their Newton-based search directions require costly second-order information and large linear-system solves. Learning to optimize offers cheaper updates learned from data, but the singular behavior of logarithmic barriers near constraint boundaries makes IPMs highly sensitive to perturbations, complicating both warm starting and learning reliable updates. We introduce pdLIP, an IPM for smoot...

---

### 21. Transferable Mass Spectrum Prediction via Reference-Guided Test-time Specialization

**Authors:** Yunhua Zhong, Runting Li, Yifan Li, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35649v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35649v1)

**Summary:** Tandem mass spectrum prediction supports compound identification across metabolomics, natural-product discovery, and environmental analysis. However, pretrained predictors often degrade under shifts in chemical space and acquisition conditions, while retraining domain-specific models from scratch is costly. We introduce SPARC, a retrieval-guided test-time specialization framework that adapts a pretrained predictor using a spectral reference library without accessing test-query spectra. For each ...

---

### 22. CoSE-E: A Benchmark for Code-switched Speech Evaluation in Enterprise Settings

**Authors:** Shama Gupta, Hoang H Nguyen, Chelsea Huang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35645v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35645v1)

**Summary:** Code-switching (CS), a seamless alternation between languages within a single utterance, remains a critical challenge in automatic speech recognition (ASR). While prior works focus on conversational CS-ASR, enterprise settings demand evaluation of operational impact beyond edit-distance errors: how code-switching transcription errors propagate to downstream voice agent task failures. In this work, we propose (1) a CS-ASR synthetic benchmark and multidimensional evaluation framework tailored to e...

---

### 23. Bounding Retraining Equivalence and the Deletion Floor in Materials Machine Unlearning

**Authors:** Can Polat, Mustafa Kurban, Erchin Serpedin, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35635v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35635v1)

**Summary:** In materials machine learning, closely related retained structures can sustain accurate property predictions even after removing a specific record, rendering post-deletion prediction error an ambiguous metric for machine unlearning. To resolve this ambiguity, we define the deletion floor as the expected target loss under a specified retraining procedure at the deleted request. Standard indistinguishability constraints yield a sharp interval bounding an update's target loss around this baseline r...

---

### 24. DR-net-Mamba: Selective State-Space Modeling for Long-Range ECG Time-Series Denoising

**Authors:** Basile Morel, Samuel Ruiperez-Campillo, Andreas P. Streich, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35634v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35634v1)

**Summary:** Electrocardiogram (ECG) recordings are corrupted by non-stationary noise sources that degrade diagnostic reliability, particularly in ambulatory and long-duration recordings. Deep learning denoisers exist, but convolutional architectures are limited by their receptive field, transformer-based models scale quadratically with sequence length, and diffusion-based approaches incur prohibitive inference cost. We propose a Mamba-augmented model that inserts selective state-space blocks at the convolut...

---

### 25. Which the Eye Fears: Writing with Read-Blindness Explains Massive Activations in Transformers

**Authors:** Swagatam Mukhopadhyay, Vishal Vivek Saley, Vraj Parikh, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35630v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35630v1)

**Summary:** Massive activation features (MAs) in Transformers are extreme-value residual-stream features that persist across layers despite the model's ability to suppress them. Why do they survive? Our investigation using an operator-level mechanistic analysis of attention and feed-forward (FFN) blocks reveals that these blocks systematically ignore MA coordinates while reading, but not while writing; creating a read-write asymmetry that blocks corrective feedback while allowing continued accumulation. We ...

---

### 26. SANTA++: Sampling Attention through Representative Keys

**Authors:** Kyle Lee, Christian Z. Pratt, Ruoyu Fang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35629v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35629v1)

**Summary:** Attention often concentrates on a small subset of tokens in the context, but which subset matters changes from one query to the next. To exploit this changing structure, we introduce SANTA++, a training-free stochastic attention method that uses representative keys for memory-efficient selection without scanning the entire key-value (KV) cache. Cached keys are organized into teams, and the query scores one representative from each team to decide which teams to sample. We compute exact attention ...

---

### 27. Arbitrary-Accuracy Neural Approximation with Optimal Neuron Count and Near-Optimal Bit Complexity

**Authors:** Zilan Cheng, Li-Lian Wang, Zhongjian Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35628v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35628v1)

**Summary:** We study the minimum number of hidden neurons required for arbitrary-accuracy approximation of multivariate Hölder-continuous functions on $[0,1]^d$ and the associated encoding complexity. For $d\geq 2$, we construct a fixed, explicitly defined activation function for which a closed-form network with two hidden layers of widths $d$ and $1$ achieves arbitrary accuracy in the uniform norm. We prove that $d+1$ is the exact minimum total number of hidden neurons among standard feedforward networks w...

---

### 28. RIDE: Reference-Anchored Inference-Time Diffusion Editing for Scaffold Hopping

**Authors:** Ruoxi Gao, Frazier N. Baker, Trieu Nguyen, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35623v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35623v1)

**Summary:** Scaffold hopping is a critical task in drug discovery, which seeks to discover new, structurally distinct molecules that share key functional groups and similar 3D shape with a reference binding ligand. Existing diffusion-based scaffold hopping methods formulate the problem as conditional generation of scaffolds given the functional groups. However, they lack a principled mechanism to jointly enforce 2D structural novelty and preserve the 3D shape of the reference ligand. Here, we introduce RIDE...

---

### 29. Elicitation and Decision Geometry in Single-Index Bandits

**Authors:** Sakshi Arya, Cheng Soon Ong

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35622v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35622v1)

**Summary:** We study two-arm contextual bandits with arm-specific single indices and a shared unknown monotone link. Monotonicity makes the optimal action depend only on the contrast between the index directions, hence arm-specific reward functions need not be estimated. We introduce Natural Boundary Learning (NBL), a greedy procedure that uses a sequential Stein contrast to learn the optimal boundary directly, without estimating the reward functions or the common link. We characterize the local Riemannian ...

---

### 30. Cartridges++: KV Cache Compression without Off-Context Derailment

**Authors:** Sonia Laguna, Joao Monteiro, Marco Cuturi, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35621v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35621v1)

**Summary:** Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache balloons. Compressed KV (CKV) representations aim to mimic the cache of a document and are typically computed once and for all, ahead of inference time. Methods to obtain CKVs range from drop mechanisms that reduce their number of columns, to learned approaches. Among the latter, Cartridges have emerged as a leading compressio...

---

### 31. Attention Graphons: A Graph Limit Perspective on Graph Transformers

**Authors:** Caio F. Deberaldini Netto, Moshe Eliasof, Luana Ruiz

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35620v1)

**Summary:** Graph Transformers produce, for each attention head, a dense $n\times n$ matrix of learned pairwise interactions. We ask a fundamental question: do these attention-induced graphs converge to a stable limit object as $n$ grows, or does the learned interaction pattern remain unstructured and size-dependent? We answer this using dense graph limit theory, treating each attention matrix as a finite sample from an underlying kernel---an \emph{attention graphon}---and studying concentration around this...

---

### 32. Behavioral Foundation Models for Quality Diversity

**Authors:** Nazim Bendib, Nicolas Perrin-Gilbert, Olivier Sigaud

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35615v1)

**Summary:** Behavioral Foundation Models (BFMs) are an emerging paradigm in reinforcement learning, playing a role analogous to large language models in natural language processing: they have shown remarkable versatility, enabling zero-shot performance, fast imitation, and online adaptation, all by exploiting the structure of a latent space. In this work, we investigate whether the latent behavioral space induced by BFMs can serve as an effective search space to discover large repertoires of behaviorally di...

---

### 33. EvE: An Alternate Optimizer to Adam

**Authors:** Shashank Raj, Kalyanmoy Deb

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35614v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35614v1)

**Summary:** Adam and its variants dominate neural network training, but a single run only reveals whether a configuration works well after most of its budget is spent, a poor fit for hyperparameter or architecture search, where configurations must be ranked cheaply and pruned early. We introduce EvE (Evolutionary Explorer), a steady-state, population-of-four differential evolution (DE) optimizer with a targeted Adam fallback: each iteration proposes one candidate via DE, running a short burst of gradient de...

---

### 34. On-Policy Self-Distillation for Multi-Turn Image Editing

**Authors:** Liangbing Zhao, Le Zhuo, Mohamed Elhoseiny

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35611v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35611v1)

**Summary:** Instruction-based image editing has achieved strong performance in single-turn settings, yet practical editing is often iterative, with each instruction applied to the output of the previous turn. We find that existing editing models degrade rapidly under recursive editing and attribute this failure to a train-test mismatch in the conditioning distribution: models are trained on clean source images but must repeatedly condition on their own imperfect outputs at inference time. To address this, w...

---

### 35. Twist, Don't Tilt: Trajectory-Exact Constrained Decoding for Masked Diffusion Models

**Authors:** Aditya Thimmaiah, Lara Marinov, Jayanth Srinivasa, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35609v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35609v1)

**Summary:** Constrained decoding for Masked Diffusion Language Models (MDLMs) aims to ensure that generated outputs satisfy a specified structure or syntax constraint. MDLMs generate outputs by repeatedly unmasking masked positions present in their current state. Recent strategies for constrained decoding constrain the model's per-step mean-field posterior (which factorizes over masked positions) by enforcing the desired constraint with an automaton. The resulting chain-structured factor graph allows exact ...

---

### 36. Control-Geometry Straightening for Sampling-Based Latent Planning

**Authors:** Ziang Fu, Ning Ning

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35603v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35603v1)

**Summary:** Joint-embedding predictive architectures enable planning with latent world models, but accurate transition prediction alone does not ensure that the planning objective is easy to optimize. We introduce Control-Geometry Straightening (CGS), a single auxiliary loss that learns planner-friendly representations by directly straightening control geometry for sampling-efficient planning. CGS matches pairwise cosine similarities among actions to those among corresponding latent differences only using l...

---

### 37. Learning Conditional Expectation Operators via Functional Newton Updates

**Authors:** Thiago Ramos, Alek Fröhlich, Daniel Perazzo, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35598v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35598v1)

**Summary:** We introduce the Functional Spectral-Newton Method (FSNM) for learning the leading singular structure of a conditional expectation operator without fixing a basis or reproducing kernel Hilbert space. FSNM fits a low-rank representation of the centered joint-to-product density ratio kernel by alternating functional Newton updates. Each update reduces to a preconditioned regression, which we approximate with vector-valued regression trees in a stagewise boosting procedure. At the population level,...

---

### 38. Hardware-Aware Features for CUTLASS Kernel Selection

**Authors:** Shriram Chandran, Dominic Rinderer, Yakup Budanaz, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35587v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35587v1)

**Summary:** GPU libraries such as CUTLASS expose tens of thousands of semantically equivalent kernels for a single operation, making exhaustive autotuning expensive and execution-free selection difficult. Existing analytical selectors require hand-designed performance rules, while learned selectors operate on raw configuration parameters and must infer hardware consequences from data. We introduce a hardware-aware representation for CUTLASS kernel selection that augments candidate configurations with static...

---

### 39. QC-Stark: A Multi-Task Benchmark Revealing Capability Dissociations in LLMs Evaluated on Quantum Computing Tasks

**Authors:** Pranav Gupta

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35581v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35581v1)

**Summary:** We introduce QC-Stark, a benchmark for evaluating large language models (LLMs) on 11 quantum computing (QC) tasks, spanning circuit construction, debugging, compilation, error correction, and simulation. Across 2,750 evaluations (10 models $\times$ 11 tasks x 5 difficulty levels x 5 seeds), we find that overall rankings mask substantial per-task variation. The Spearman correlation between overall and per-task rankings is statistically insignificant for 4 out of the 11 tasks included in this benc...

---

### 40. Output-aware Residual Stream Pruning for Large Language Models

**Authors:** Chayne Thrash, Kevin Chen, Soheil Kolouri

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35579v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35579v1)

**Summary:** Residual stream pruning methods reduce inference cost by shrinking the model's hidden dimension, but existing approaches typically choose these dimensions by minimizing activation reconstruction error. This criterion implicitly treats all perturbation directions as equally important, ignoring the sensitivity of downstream layers. We introduce a sensitivity-aware approach to residual-stream pruning that directly accounts for this direction-dependent sensitivity. Using a second-order approximation...

---

### 41. Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents

**Authors:** Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35576v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35576v1)

**Summary:** Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a r...

---

### 42. Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions

**Authors:** Tianyao Shi, Xipeng Shen, Yi Ding

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35569v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35569v1)

**Summary:** Large language model (LLM) serving has environmental impacts across energy consumption, carbon emission, water consumption, and biodiversity loss. Yet these dimensions are largely evaluated in isolation, leaving it unclear when and how they lead to different optimization decisions. We present PRISM, a unified framework for characterizing and optimizing LLM serving across energy, carbon, water, and biodiversity impacts. Our analysis reveals a fundamental distinction: computing configurations dete...

---

### 43. From Experience to Expertise: Adoption-Aware Memory Learning for Data-Scarce NPU Kernel Synthesis

**Authors:** Longxiao Fan, Tao Zhang, Han Yan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35568v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35568v1)

**Summary:** High-performance kernels underpin efficient accelerator execution but require expert tuning and lengthy manual optimization cycles. LLM coding agents promise automation, yet their CUDA knowledge transfers poorly to data-scarce domain-specific architectures (DSAs) such as NPUs, whose execution models and memory hierarchies differ substantially from those of GPUs. To address this transfer gap, post-training methods adapt LLMs to NPU programming but depend on scarce expert data and substantial trai...

---

### 44. Simplex Diffusion Models

**Authors:** Justin Deschenaux, Alexandre Galashov, Andrew Campbell, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35553v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35553v1)

**Summary:** Diffusion models have revolutionized generative modeling for continuous data through the gradual refinement of a belief state. This iterative refinement has not yet carried over to discrete diffusion models, which discard uncertainty at intermediate steps through categorical sampling (information collapse). We propose Simplex Diffusion Models (SDMs), a framework that lifts the diffusion process to the probability simplex to represent beliefs over categories. SDMs admit probability paths with clo...

---

### 45. Graph World Models for Constrained Epidemic Policy Planning

**Authors:** Yiqi Su, Rashed Shelim, Lingyi Wang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35545v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35545v1)

**Summary:** Epidemic policy planning often requires coordination between geographical regions, taking into account mobility-driven spillovers and how to make use of limited resources. Existing methods either lack action-conditioned models of coupled dynamics or cannot guarantee per-period feasibility. We present EpiMind, a graph world model framework for constrained epidemic policy planning across regions. A graph-factored recurrent state-space model generates joint policy-conditioned rollouts from regional...

---

### 46. Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability

**Authors:** Xu Wang, Difan Zou, Xuansheng Wu

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35544v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35544v1)

**Summary:** Reliable refusal of harmful requests is essential to the safe deployment of language models. Because excessive eagerness to please users may undermine existing refusal capabilities, reducing sycophancy offers a potential route to stronger refusal beyond the harmful scenarios covered by safety training. We investigate this possibility using compensatory feature injection (CFI), a training technique designed to limit the acquisition of a target concept by supplying its associated activation during...

---

### 47. Learning the Robustness Mechanism with Bilevel Optimization

**Authors:** Yiyang Shen, Qihang Lin, Weiran Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35541v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35541v1)

**Summary:** We propose a distributionally robust learning framework where parameters defining the robustness mechanism are learned from held-out data instead of extensively tuned. Using bilevel optimization with both upper and lower level minimax problems, we create two instances of our framework to tackle setups with and without group labels in the training set. Theoretically, we provide sample complexity analysis for our robustness mechanism learning paradigm, showing that it achieves generalization guara...

---

### 48. Optimal Networks for Agentic Information Aggregation

**Authors:** MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35537v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35537v1)

**Summary:** We study information aggregation in the networked learning model introduced by Kearns, Roth, and Ryu (SODA 2026). There is a fixed distribution over $d$ features and a common label. Agents learn in topological order on a directed acyclic graph. Each observes a subset of the features and its parents' predictions, fits a linear predictor to minimize mean squared error, and passes only its prediction forward. The global predictor is the best linear predictor using all features. Kearns, Roth, and Ry...

---

### 49. Let the Neurons Die: Exploiting ReLU-Induced Model Degradation

**Authors:** Kexin Li, Wenjun Qiu, Joshua Abraham, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35528v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35528v1)

**Summary:** Rectified linear unit (ReLU) networks can suffer from dying neurons, where units with persistently negative pre-activations produce zero outputs, blocking gradients through their activations. To exploit this failure mode, we present three training-time availability attacks based on data ordering and poisoning. We begin with the basic dynamic data-ordering attack (DOA), which greedily constructs a training prefix by selecting the next example that minimizes the target layer's post-update weight s...

---

### 50. GeoGAE: Scalable Graph-Level Autoencoding via Hyperball Cloud Representations

**Authors:** Radosław Nowak, Anna Bielawska, Bogusz Stefańczyk, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35527v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35527v1)

**Summary:** Embedding structured objects into Euclidean spaces has enabled a wide range of successful machine learning applications. Such objects include words, documents, image patches, time series, and graph nodes. In contrast, embedding entire graphs remains a challenging problem. Existing methods either sustain the original order of the graph nodes or match the output nodes to the input ones, both of which create scalability issues. In this work, we propose a graph representation as a cloud of hyperball...

---

## cs.NE

**50 papers**

### 1. CMDO: A Cognitive Memory-Driven Optimization Algorithm for Adaptive Population-Based Search

**Authors:** Mohammed Yusuf Mujawar, Shahram Rahimi, Noorbakhsh Amiri Golilarz

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35657v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35657v1)

**Summary:** Population-based optimization methods often use previous search information through successful solutions, parameter adaptation, or operator performance, but they rarely retain the context in which a search behavior succeeded or failed. We introduce Cognitive Memory-Driven Optimization (CMDO), a derivative-free population-based optimizer that represents experience as the relationship between search context, search behavior, and observed outcome. CMDO organizes these experiences across working, ep...

---

### 2. Arbitrary-Accuracy Neural Approximation with Optimal Neuron Count and Near-Optimal Bit Complexity

**Authors:** Zilan Cheng, Li-Lian Wang, Zhongjian Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35628v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35628v1)

**Summary:** We study the minimum number of hidden neurons required for arbitrary-accuracy approximation of multivariate Hölder-continuous functions on $[0,1]^d$ and the associated encoding complexity. For $d\geq 2$, we construct a fixed, explicitly defined activation function for which a closed-form network with two hidden layers of widths $d$ and $1$ achieves arbitrary accuracy in the uniform norm. We prove that $d+1$ is the exact minimum total number of hidden neurons among standard feedforward networks w...

---

### 3. EvE: An Alternate Optimizer to Adam

**Authors:** Shashank Raj, Kalyanmoy Deb

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35614v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35614v1)

**Summary:** Adam and its variants dominate neural network training, but a single run only reveals whether a configuration works well after most of its budget is spent, a poor fit for hyperparameter or architecture search, where configurations must be ranked cheaply and pruned early. We introduce EvE (Evolutionary Explorer), a steady-state, population-of-four differential evolution (DE) optimizer with a targeted Adam fallback: each iteration proposes one candidate via DE, running a short burst of gradient de...

---

### 4. Deep Learning Methods in Neuroscience: From Modeling Molecular Mechanisms to Classifying States of Consciousness

**Authors:** Elena Benderskaya, Anastasiia Alifanova, Svetlana Batalova, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35372v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35372v1)

**Summary:** A critical analysis of contemporary approaches to the study of conscious states. The review focuses on methods of classification, clustering, modeling of brain states under anesthesia and identification of measurable neurobiological characteristics of brain function. A comparative analysis was conducted in the following three major areas: automatic detection of states of consciousness using neural networks based on EEG and fMRI data; modeling of the structural-functional dynamics of the brain un...

---

### 5. Hidden Activations are not Enough I: Knowledge Matrices as Higher Representations

**Authors:** Marco Armenta

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34166v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34166v1)

**Summary:** We study the knowledge matrix of a trained feedforward network as a higher representation of its inputs. A network is a pair $(W,f)$, a thin representation $W$ of its quiver and an activation $f$; its function factorizes through the space of quiver representations, each input $x$ inducing a representation, and the knowledge matrix $M(x)\in\mathbb{R}^{C\times(d+1)}$ is the contraction of that representation to one matrix whose rows sum exactly to the logits. At one trained network we ask what det...

---

### 6. ADPTNet: Adaptive with Prescriptive Timescales Non-Linear SSM for Sequence Modelling

**Authors:** Matei-Ioan Stan, Oliver Rhodes

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.34034v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34034v1)

**Summary:** A central aim of neuromorphic computing is to provide a viable alternative to highly energy-intensive Transformer-based AI. However, efficient alternatives struggle to capture the set of qualities that have secured the Transformer's status as the de facto standard in sequence modelling. Any realistic contender must be data-adaptive, able to capture long-range dependencies, and GPU-parallelisable, but also non-linearly recurrent to enable complex reasoning. Based on evidence suggesting the audito...

---

### 7. Neuron-Level Architecture Growth: A Controlled Evaluation for EEG Time-Series Decoding

**Authors:** Adam Mounir, Stella Douka, Arnault H. Caillet, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33880v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33880v1)

**Summary:** Convolutional EEG decoders are trained at a fixed width, usually set by their authors on other data. Growing methods add neurons during training where the loss could decrease the most, but whether they improve compared to a reference width is untested on EEG. Here, we grow three convolutional backbones on 12 motor-imagery datasets under three protocols and compare each with its reference model per subject. The growing ShallowFBCSPNet scores 2.9 points above its reference model with only half the...

---

### 8. Program-Verified Self-Evolution for Vision-Language Models

**Authors:** Ahmed Heakl, Sungik Choi, Moontae Lee, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33855v1)

**Summary:** Self-evolving vision-language models train on questions they generate from unlabeled images. Since these questions have no gold answers, prior methods label them by majority vote over sampled answers or by a model judge. In a human evaluation, we find that 24\% of majority-vote labels and 18\% of model-judge labels produced during self-evolution are wrong. To address this problem, we present Verifiable QA Generation for Self-Evolving Models (VQS), which changes how the model judges answers. Inst...

---

### 9. Raven: The Harness of Harnesses for Composable Agentic Intelligence

**Authors:** EverMind AI

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33439v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33439v1)

**Summary:** As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through ...

---

### 10. APEX: An Extensible Model for Agent-Assisted Production Scheduling

**Authors:** Felix J. Grumbach, Stefan Görlitz

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33430v1)

**Summary:** Production scheduling requires realistic models that reflect operational constraints and efficient methods that balance competing goals. Putting these methods into use also requires data integration, model adaptation and specialist expertise. We present APEX, an extensible production scheduling framework built around a general model and hybrid multiobjective search. Agent assistance supports both scheduling and model refinement: agents prepare data and explore scenarios in natural language, whil...

---

### 11. MTLiquid: Enabling Efficient Multi-Task Learning using Liquid Neural Networks for Lightweight Healthcare Monitoring Systems

**Authors:** Rachmad Vidya Wicaksana Putra, Fahad Abdul Rauf, Muhammad Shafique

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33232v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33232v1)

**Summary:** Continuous-time sensing and monitoring with timely and accurate decision-making are critical for many real-world applications. In healthcare monitoring systems, physiological signals are often available or sampled at irregular time intervals, hence requiring continuous-time processing to provide accurate prediction. Moreover, such systems often need to solve multiple detection/prediction tasks to provide a comprehensive patient review from different physiological aspects for more accurate decisi...

---

### 12. MorphAtt: A Neuromorphic Accelerator for Efficient Multi-Head Attention Processing in Spiking Vision Transformers

**Authors:** Rachmad Vidya Wicaksana Putra, Amirhesam Jafari Rad, Muhammad Shafique

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33207v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33207v1)

**Summary:** Spiking Vision Transformers (SViTs) are developed as an energy-efficient alternative to conventional ViTs for computer vision tasks at the edge. However, huge parameter counts and complex multi-head self-attention (MHSA) operations make it challenging to achieve high energy efficiency in SViT inference, especially in tightly constrained applications. To maximize efficiency gains of SViT processing, we propose MorphAtt, a novel digital accelerator that expedites SViT inference through streamlined...

---

### 13. RIPE-MambaSpike: Resolution-Independent Spiking-State-Space Interfaces for Parameter-Efficient Event-Based Vision

**Authors:** Md Muhiminul Islam, Shoaib Ahmed Dipu, Sayeed Shafayet Chowdhury

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32537v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32537v1)

**Summary:** Spiking-Mamba hybrids reach strong accuracy on event-based vision, but existing designs often require tens of millions of parameters. Much of that cost comes from how the spiking front-end is connected to the state-space backbone rather than from the hybrid architecture itself. In a representative model, a single resolution-dependent projection accounts for 33.55M of 36.25M parameters. To that end, we introduce RIPE-MambaSpike (Resolution-Independent, Parameter-Efficient), which replaces that pr...

---

### 14. Analog-Friendly Predictive Coding without Activation Derivatives

**Authors:** Francesco Innocenti

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32350v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32350v1)

**Summary:** Predictive coding (PC) is a local, energy-based alternative to backpropagation (BP) whose iterative inference dynamics make it attractive for implementation on analog hardware. However, standard nonlinear PC requires evaluating the derivative of the activation function during both inference and learning, which can be difficult to realise physically. Here, we introduce \textit{activation-matched Bregman PC}, replacing standard squared-error energies with Bregman divergences matched to the activat...

---

### 15. All On-Board: Fully On-Chip Neuromorphic Q-Learning with Embedded CartPole Simulation

**Authors:** Steven C. Nesbit, Giovanni T. Michel, Gerd J. Kunde, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32317v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32317v1)

**Summary:** As AI models grow in size and usage, their energy demands increase dramatically, raising sustainability and economic concerns. Neuromorphic hardware, inspired by the energy efficiency of the brain, seeks to address this challenge by offering low-power, fast-processing alternatives to conventional computing. Such hardware is particularly well-suited to control systems deployed in resource-constrained environments, which are best trained via reinforcement learning (RL). This contribution presents ...

---

### 16. DS-VLA: A Dendritic-inspired Vision-Language-Action Model for Robust Action Control

**Authors:** Yaxing Lyu, Jingyi Li, Mingkun Xu, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32253v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32253v1)

**Summary:** Vision-language-action (VLA) models have achieved strong performance in language-conditioned manipulation, yet success under nominal evaluation does not necessarily translate into robust closed-loop behavior when executed actions are transiently corrupted. We introduce DS-VLA, a dendritic-inspired action architecture that incorporates dendritic spiking dynamics into VLA control to address this limitation. Specifically, to enable modularized feature processing and temporal information integration...

---

### 17. Distance-Residual Physics-Informed Neural Networks: A Deep Learning Framework for Differential and Partial Differential Inclusions

**Authors:** Maria Filipkovska, Juan José Marín, Isil Oner, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.32043v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32043v1)

**Summary:** We introduce Distance-Residual Physics-Informed Neural Networks (DR-PINNs), a physics-informed learning framework for approximating solutions of ordinary and partial differential inclusions (DIs), governing laws in which a differential operator is constrained to lie in a set-valued map rather than equaling a prescribed function. The method replaces the classical pointwise PDE/ODE residual by the squared distance from the differential operator to the admissible set. This distance vanishes exactly...

---

### 18. A Voltage-controlled MTJ-CMOS Neuron Emulating Tunable Izhikevich-Inspired Dynamics

**Authors:** Kayode Oluwaseyi Adebunmi, Jordan Athas, Allison Fleming, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.32031v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32031v1)

**Summary:** Biological neurons exhibit diverse firing dynamics that enable adaptive and stimulus-dependent signalling, yet reproducing these dynamics in hardware has remained an enduring challenge. In this work, we present an Izhikevich- inspired reconfigurable neuron that co-designs voltage-controlled magnetic tunnel junction (V-MTJ) dynamics with CMOS circuitry. The proposed architecture combines V-MTJ excitability dynamics, enabled by a tunable energy landscape, with CMOS recovery dynamics to generate fi...

---

### 19. SNIP++: Fine-Grained Symbolic-Numerical Alignment for Symbolic Regression

**Authors:** Benjamin Léger, Shubham Gupta, Samy Mammeri, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31965v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31965v1)

**Summary:** Mathematical expressions and the numerical behavior they produce are two views of the same underlying function, and connecting them is central to scientific discovery. Symbolic Regression (SR) relies on this connection directly: it searches for an expression that reproduces a given behavior. Recent multi-modal models learn this connection by embedding symbolic expressions and their numerical behavior in a shared representation space. We show that this embedding space is only globally aligned: co...

---

### 20. Common-Mode Collapse and Recovery in Direct Feedback Alignment

**Authors:** Varun Reddy, Bernardo L. Sabatini, Houman Safaai

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31589v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31589v1)

**Summary:** Direct feedback alignment (DFA) trains hidden layers through fixed random projections of output error. With tanh hidden units and independent sigmoid outputs, plain stochastic gradient descent can stall near the loss of a constant predictor of class frequencies. We trace this stall to the error's common mode, the component shared across inputs. An exact mean-covariance decomposition separates a rank-one update formed by the mean teaching signal and mean presynaptic activity. Its leading componen...

---

### 21. Purin: A Biology-inspired Mechanism for Artificial Neural Networks

**Authors:** Zishu Liu, Chunbo Luo, Christos Grecos

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31235v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31235v1)

**Summary:** Artificial neural networks (ANNs) usually represent neural transmission with fixed trainable weights during a training batch, which omits short-term changes in synaptic efficacy. In addition, the discrete time-step simulation requires additional temporal processing that many conventional ANN architectures do not use. To overcome these challenges, we propose Purin, a biology-inspired and ANN-compatible mechanism, that introduces synaptic efficacy modulation into conventional convolutional neural ...

---

### 22. Modeling quantum neural network gradient with reinforcement learning

**Authors:** Nhan Trong Luu, Duong Trung Luu, Nam Ngoc Pham, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31066v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31066v1)

**Summary:** Training quantum neural networks (QNNs) on near-term hardware remains hampered by two compounding difficulties: the exponential vanishing of gradient variance known as the barren plateau, and the $\mathcal{O}(L \cdot 2^n)$ time and memory cost of differentiating through an $n$-qubit, $L$-layer circuit. We propose RLQ-Grad, a reinforcement-learning-based optimizer in which a classical policy $π_φ$ (a spectrally-normalized PPO agent) learns to propose parameter updates directly, conditioned on the...

---

### 23. Landscape Limits of Quantum-Inspired Evolutionary Optimization across 256 continuous functions

**Authors:** Rishi Govind, Ferdin Sagai Don Bosco, Kasturi Venkata Srikanth, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.30938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30938v1)

**Summary:** Quantum-inspired evolutionary optimization (QIEO) represents design variables as a set of qubits and searches a continuous, multi-dimensional landscape through rotation of the qubit's amplitude pair. Every generation rotates those amplitudes toward a single elite, which corresponds to that generation's best. The update is cheap, almost parameter-free, and well-suited for massive parallel implementation, which has encouraged its adoption in engineering, design, and planning applications. However,...

---

### 24. Structured Bayesian Modeling of Dynamic Receptive1 Fields in Salamander Retinal Ganglion Cells

**Authors:** Alokesh Manna

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.30731v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30731v1)

**Summary:** Neurons in the visual system are selective for specific spatial and temporal stimulus features, described by their \emph{receptive field}. Estimating one means a coefficient per pixel per time bin from few trials -- a high-dimensional problem requiring regularization. Sparse regularizers such as the LASSO handle the dimension but select pixels independently at each time point, with nothing to keep the region coherent in space or smooth in time; it can fragment or reorganize discontinuously even ...

---

### 25. Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis

**Authors:** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30115v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30115v1)

**Summary:** Modern deep neural networks treat parameters as static floating-point matrices stored in physical memory, incurring Von Neumann memory bottlenecks and representation collapse. We formulate Orbital Error Dynamics (OED), an analytical framework wherein synaptic weights are not stored masses (O(W)), but transient topological resonances (O(1)) derived procedurally from the complex quadratic polynomial map z_{n+1} = z_n^2 + c. We introduce the Bent Sine Wave Hypothesis, demonstrating that non-equilib...

---

### 26. Activation-Flexible ANN-to-SNN Conversion with Finite-State Markov Neurons

**Authors:** Ruiyu Jia, Zhuo-Cheng Xiao

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.30102v1) | 📄 [PDF](https://arxiv.org/pdf/2609.30102v1)

**Summary:** Most ANN-to-SNN conversion methods rely on a specific correspondence between the source activation and the spiking neuron dynamics. We propose a finite-state continuous-time Markov chain (CTMC) neuron framework whose stationary spike flux can approximate every continuous nonnegative monotone activation function on a compact interval. For a generalized CTMC family with affine input-dependent transitions, we prove uniform approximation to arbitrary accuracy over this function class and derive an e...

---

### 27. A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics

**Authors:** R. Lahoz-Beltra

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29984v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29984v1)

**Summary:** Understanding the neurobiological mechanisms underlying self-referential cognition and baseline self-consciousness remains a fundamental challenge in computational neuroscience. In this work, we propose a large-scale computational model incorporating a 10,000-neuron spiking neural network (SNN) based on Izhikevich dynamics. The network is structured into two interacting subsystems: a sensory processing layer (5,000 regular-spiking cortical neurons) and an endogenous Default Mode Network (DMN) pa...

---

### 28. Boolean threshold functions, neuron capacity, and memory retrieval

**Authors:** Xinyuan Xie

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29756v1)

**Summary:** How much information can a single neuron remember? How many memories can neural networks retrieve without creating false memories? These questions are related to a basic question: how many Boolean threshold functions $f(x)=\operatorname{sgn}(a_0+\langle a,x\rangle)$, $x\in\{-1,1\}^n$, are there? In this paper, we show that the number $T_n$ of distinct Boolean threshold functions is \[ T_n=2\binom{2^n-1}{n}\bigl(1+O(n^{-99})\bigr). \] Equivalently, the capacity of a single threshold neuron is $n^...

---

### 29. On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation

**Authors:** Benedikt Hartl, Milton L. Montero, Marcello Barylli, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29755v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29755v1)

**Summary:** How phenotypic transformations are implemented by changes in underlying regulatory dynamics remains a central question in developmental biology. Inspired by D'Arcy Thompson's 1917 "On Growth and Form", we ask whether coherent large-scale transformations of morphology can be encoded as low-dimensional modulations of a self-organizing developmental system. We use neural cellular automata (NCAs) as bio-inspired models of distributed development, in which a shared local regulatory network grows targ...

---

### 30. Dynamical Diversity for Reservoir Computing in Reconfigurable Nanomechanics

**Authors:** Humayun Ahmed, Inês S. Garcia, Filipa C. Mota, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29532v2) | 📄 [PDF](https://arxiv.org/pdf/2609.29532v2)

**Summary:** Physical reservoir computing uses nonlinear dynamics and a trained linear readout to process information. Nanoelectromechanical (NEMS) resonators combine geometric Duffing nonlinearity with fading memory, but most electromechanical implementations use a single resonance mode. Here, we demonstrate reservoir computing with two interacting modes of a single NEMS resonator measured through one readout port. We introduce dynamical diversity through complementary modal drive settings: the same input s...

---

### 31. Online Task Adaptation via Self-Organisation

**Authors:** Krsto Proroković

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29281v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29281v1)

**Summary:** Neural networks are typically adapted by computing gradients and updating model parameters. We investigate whether task-specific adaptation can instead emerge from a meta-learned self-organising process that requires no gradients at adaptation time. We instantiate this idea with a Neural Cellular Automaton in which locally interacting recurrent cells maintain both a recurrent state and a fast associative memory. During meta-training, backpropagation is used to learn the recurrent dynamics togeth...

---

### 32. EvoTreeNAD: Genealogy-Guided Evolution for LLM-Driven Neural Architecture Discovery

**Authors:** Lishan Yu, Derek Jiu, Qizhen Lan, et al.

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29016v1)

**Summary:** AI-driven scientific discovery accelerates research by autonomously developing solutions and designs. Large language model (LLM) agents support this process through iterative generation and evaluation. Yet these iterations alone do not ensure cumulative progress or establish which directions to pursue next. Costly evaluation further constrains the scope of exploration. Neural architecture discovery brings these challenges together, coupling open-ended design with resource-intensive experimentati...

---

### 33. Learning Holographic Reduced Representations with Clifford Variational Autoencoders

**Authors:** Mohamed Malek Abid, P. Michael Furlong

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28409v1)

**Summary:** Vector Symbolic Algebras project data structures into a hyperdimensional vector space through the application of their vector algebras to randomly generated atomic vector symbols and fractional power encodings of real-valued data. Embedding unstructured data remains an open question. We present \textit{Clifford-VAE}, a variational autoencoder that learns to project data onto a Clifford torus in arbitrary dimensions. Experiments using the MNIST, FashionMNIST, and CIFAR-10 datasets demonstrate tha...

---

### 34. Scenario-Driven Neuroevolution: Using Models to Guide Test Generation for Games

**Authors:** Gijs van Cuyck, Patric Feldmeier, Jan Tretmans, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.28130v1) | 📄 [PDF](https://arxiv.org/pdf/2609.28130v1)

**Summary:** Automatically generating test inputs for games is challenging, as test generators must master the game to reach advanced program states while also ensuring robustness against the heavy program randomisation inherent to games. The test generator Neatest therefore optimises test suites consisting of neural networks that reach advanced program states and are robust to program randomisation, as they generate test inputs dynamically based on the current program state. Neatest is a white-box testing a...

---

### 35. Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation, Practical Use and Beyond

**Authors:** Yiqian Yang, Yiqun Duan, Chenyu Liu, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27650v2) | 📄 [PDF](https://arxiv.org/pdf/2609.27650v2)

**Summary:** Brain-to-language decoding translates neural activity associated with language production, internal speech and perception into linguistic or expressive outputs. It offers a route to restoring communication after speech loss and a means of studying how the brain represents language. Advances in neural recording and representation learning have expanded the field from constrained recognition and acoustic reconstruction to text generation, streaming personalised speech and facial animation. This su...

---

### 36. Spiking Neural Network Predicting Sequence of the External Worlds States in Model-Based Reinforcement Learning

**Authors:** Mikhail Kiselev

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27459v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27459v1)

**Summary:** This paper presents a spiking neural network (SNN) designed to predict the sequence of the external world states starting from the current world state. This SNN does not create the world dynamics model - instead it incorporates the SNN trained to predict the next world state and provides all mechanisms necessary to make the chain of predicted world states. These mechanisms are entirely spiking - they are implemented as spiking neuron ensembles. The present article describes this neuronal structu...

---

### 37. An Unbounded Archive-based Transfer Strategy for Dynamic Multi-Objective Optimization with a Changing Number of Objectives

**Authors:** Zhiyun Xiao, Ke Shang, Yajun Liu, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27430v1)

**Summary:** Dynamic multi-objective optimization with a variable number of objectives is difficult because objective-dimensional variations may significantly change the Pareto front and degrade algorithm adaptability. This paper proposes an unbounded archive-based transfer strategy (UATS), which maintains an unbounded archive of offspring solutions within each environment stage and extracts feasible nondominated solutions as transferable elites when objective changes occur. UATS is embedded into SPEA2SDE to...

---

### 38. Combining LLMs and Genetic Search for ARC-AGI-2

**Authors:** Val Dyachenko

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27242v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27242v1)

**Summary:** LLMs can generate programs for ARC-AGI-2 tasks, but the provided compute only allows a small number of attempts to generate, debug and validate solutions. Genetic algorithms can search and test many more programs, but random search rarely starts in a useful neighborhood of the solution space. We combine the two methods through a compact domain specific language (DSL). First, a quantized Qwen3.5-4B LLM generates an initial set of programs for each ARCAGI-2 task. Then, we use those programs to see...

---

### 39. LexLattice: Multilingual Extractive Summarization via Neural Cellular Automata on Document Hierarchies

**Authors:** Sujay Uday Rittikar, Sheela Ramanna

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.27032v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27032v1)

**Summary:** Faithfulness is a central concern in legal text summarization, which motivates extractive approaches that select verbatim content traceable to its source. Such methods typically rank paragraphs or other structural units in isolation, yet give little attention to consolidating evidence that is distributed across, and shares salience between, distant parts of a document. We introduce LexLattice, an extractive summarizer that reifies a legal act's hierarchy as a two-dimensional semantic lattice and...

---

### 40. The Computational Value of Sensory-Aligned Receptive Fields Depends on Neuronal Expressivity

**Authors:** Agnese Adorante, Aaron Spieler, Anna Levina

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26940v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26940v1)

**Summary:** Biological sensory neurons have selective receptive fields organized along meaningful stimulus coordinates, such as frequency, motion direction, or retinotopic position. Such structure may arise from efficient coding and biological constraints on activity, connectivity, and wiring, as computational studies of simple neurons have shown across modalities. This raises a question: do structured receptive fields confer a computational advantage beyond resource efficiency itself, and does this advanta...

---

### 41. LukeNet: A lightweight CNN integrated with an XAI model for Smart acute lymphoblastic leukemia detection and management

**Authors:** Md Taimur Ahad

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.31736v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31736v1)

**Summary:** Acute Lymphoblastic Leukemia (ALL) patients require early, accurate detection to enable timely treatment and effective patient management. A Convolutional Neural Network (CNN) is well-suited for creating an end-to-end enabling environment for ALL detection and classification. However, most CNN-based ALL detection systems are theoretical and unsuitable for deployment on edge devices due to high computational demands. The Internet of Medical Things (IoMT)-enabled devices offer an opportunity to mo...

---

### 42. When Recursive Models Finish Computing

**Authors:** Hare Krishna, Shubham Singh, Stephen Ebert, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26487v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26487v1)

**Summary:** Recursive models can continue updating their latent states beyond their nominal inference budget, so an incorrect output at that budget does not show whether computation is unfinished or has entered a persistently unsuccessful regime. We study the dynamics of completion in attention- and MLP-based Tiny Recursive Models (TRMs) on 1,000 hard Sudoku puzzles. Extending recurrence from the nominal 16 steps to 512 steps increases cumulative exact-solve accuracy from 59.2% to 87.5% for the attention mo...

---

### 43. Rethinking Pairwise Token Interaction in Spiking Transformers

**Authors:** Sicheng Shen, Dongcheng Zhao, Zhiyuan Li, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26297v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26297v1)

**Summary:** Spiking Transformers inherit token interaction mechanisms from conventional Transformers, yet their sparse binary representations fundamentally alter how token-to-token communication is established. In particular, spike-based query-key matching produces highly sparse and input-dependent interaction patterns, coupling information propagation to the instantaneous availability of matching spike events. This motivates a different interaction paradigm in which long-range communication does not rely s...

---

### 44. In-Context Guidance: Learning Inter-Task Synergies via Numerical Foundational Models for Few-Shot Multitask Optimization

**Authors:** Tingyang Wei, Haofeng Wu, Jiao Liu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25836v2) | 📄 [PDF](https://arxiv.org/pdf/2609.25836v2)

**Summary:** Multi-task optimization (MTO) addresses a set of optimization tasks simultaneously, often suffering from inaccurate inter-task relationship estimation under limited evaluation budgets, leading to negative transfer. This paper introduces In-Context Guidance Multitask Optimization (ICG-MTO), a novel framework that leverages numerical foundational models to improve inter-task coupling estimation in few-shot scenarios. Unlike conventional methods that rely solely on scarce observed data, ICG-MTO emp...

---

### 45. NeuroRule: Making Black-Box Neural Networks Explainable through Rule-set Evolution

**Authors:** Tapaswini Kodavanti, Hormoz Shahrzad, Risto Miikkulainen

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26841v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26841v1)

**Summary:** High-capacity neural network models have achieved state-of-the-art performance across diverse classification tasks, yet they frequently operate as black-box models, lacking the transparency necessary for critical decision-making. Such opacity creates a persistent trade-off between performance and explainability. This paper proposes a solution to address this gap: the NeuroRule knowledge distillation framework that results in explainable rule-sets from neural network models. NeuroRule adapts the ...

---

### 46. Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains

**Authors:** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25498v2) | 📄 [PDF](https://arxiv.org/pdf/2609.25498v2)

**Summary:** Deploying Large Language Models for runtime operational triage incurs prohibitive latency (>100-500 ms), high VRAM requirements (>4-8 GB), and excessive energy dissipation. Extending Mandelbrot Fractal Neural Synthesis (Dagli et al., 2026), this paper presents the Universal Fractal Natural Language Decision Map, realized via the werr machine-native edge reflex runtime and the production answerr platform (https://answerr.me). Operating entirely without stored weight tensors (0 Bytes VRAM), the en...

---

### 47. Online Automated Algorithm Design with Large Language Models

**Authors:** Zhiyao Zhang, Yichen Li, Xingyu Wu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25325v1)

**Summary:** Large language models (LLMs) enable automated algorithm design (AAD) through reasoning and code synthesis. However, most existing LLM-based AAD methods separate algorithm design from target optimization, deploying a fixed design even as the optimization state evolves. Conventional adaptive optimizers can respond to such changes, but their adjustments remain confined to predefined parameters, operators, or strategies. To address these limitations, we introduce online LLM-based AAD, a novel optimi...

---

### 48. Harness-Zero: Harness Distillation via Agent-as-Harness

**Authors:** Haoran Ye, Yuxing Lu, Haonan Dong, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24974v1)

**Summary:** Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent must either settle for a suboptimal shared harness or route among an ever-growing set of specialized ones. We therefore study agent harness distillation: using a domain- or instance-optimized harness as training-time gui...

---

### 49. QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation

**Authors:** Demian Pavlyshenko, Bohdan Pavlyshenko

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24538v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24538v1)

**Summary:** Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational approaches consider annotation as multi-label classification over a fixed ontology, which constrains predictions to a predefined label set. In this work we study the the protein annotation as a sequence-to-text generation problem. We fine-tune the 3B-parameter Ministral 3 base model w...

---

### 50. DCL-GPGLS: Dynamic Curriculum Learning for Genetic Programming Guided Local Search in Large-Scale Vehicle Routing

**Authors:** Saining Liu, Yi Mei, Mengjie Zhang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24105v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24105v1)

**Summary:** Genetic Programming Guided Local Search (GPGLS) uses genetic programming to evolve utility functions for guided local search in large-scale vehicle routing problems (LSVRPs). Evaluating every GP individual on every training instance at every generation is expensive, so GPGLS is usually trained on small instance batches. Existing curriculum-based GPGLS orders these batches mainly by instance size. Adaptive Curriculum Learning GPGLS (ACL-GPGLS) improves training efficiency by adapting when the sea...

---

## q-bio.NC

**50 papers**

### 1. NeuronSifter: Intervention Planning in CNS Microenvironments

**Authors:** Haowei Xu, Wanyi Fu, Hongbin Han, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35445v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35445v1)

**Summary:** Prioritizing central nervous system (CNS) interventions requires predicting how a dose, route, and schedule act on a partially observed microenvironment, then choosing the measurement that would change the decision. Action-conditioned predictors reduce a regimen to an identity token or a scalar exposure, discarding where and when the target is engaged; handing a point estimate to a separate planner then discards the joint uncertainty that makes a measurement worth running. We therefore treat dec...

---

### 2. NeuronDiscover: Agent-in-Twin for Mechanistic Discovery in Neuronal Microenvironments with World Action Models

**Authors:** Haowei Xu, Wanyi Fu, Hongbin Han, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35338v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35338v1)

**Summary:** Mechanistic discovery in neuronal microenvironments requires interventions and measurements that separate competing explanations of solute transport and neuronal response. Predictive accuracy cannot settle the question: a real mechanistic change and an error in the computational twin leave the same signature in sparse observations. We formalize this twin confounding and reason over a joint mechanism--discrepancy belief, designing experiments that separate the two. NeuronDiscover is an Agent-in-T...

---

### 3. High-rank connectivity scaffolds support precision and generalisation in recurrent neural networks

**Authors:** Ian Hawes, Matt Nolan

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35207v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35207v1)

**Summary:** A major challenge in neuroscience and machine learning is to connect single-neuron influence, population dynamics, and circuit connectivity in a causal account of computation. Much previous work has shown that low-rank connectivity can generate low-dimensional dynamics in trained artificial neural networks, but this leaves unclear the functional relevance of the higher-rank structure of biological neural circuits and many artificial neuronal networks. Here we analyse recurrent neural networks tr...

---

### 4. Scaling Laws for EEG Decoding: How Much Data Is Enough?

**Authors:** José Maurício Nunes de Oliveira, Bruna J. Lopes, Léo Burgund, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35056v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35056v1)

**Summary:** Deep learning has become a cornerstone of EEG-based brain decoding, with a growing number of architectures proposed every day. However, how the performance of these different models scales with data volume is not clear. Although this relationship has been characterized in other fields under the name of scaling laws, it remains poorly understood in the EEG domain. The present study addresses this gap by investigating how scan time and subject diversity affect the performance of different architec...

---

### 5. On the Limits of Metacognitive Monitoring in LLMs

**Authors:** Dongqi Han, Yifan Yang, Dongsheng Li

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34864v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34864v1)

**Summary:** Reliable decisions depend on recognizing when an answer may be wrong. In biological cognition, metacognitive monitoring can dissociate from task performance, raising the question of how closely solving and judging are linked in language models. Here we study the confidence reports of four frontier models across 15 benchmarks. High task accuracy can coexist with weak error discrimination: a model solves 97% of competition mathematics problems while its answer-time confidence ranks correct answers...

---

### 6. Separating personal from population gains when calibrating EEG foundation models for new users

**Authors:** Xilin Tao, Kani Chen

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34801v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34801v1)

**Summary:** Foundation models are increasingly adapted to individual users, but an apparent personalization gain can simply reflect a stronger population model. This distinction matters for brain-computer interfaces, where every new user must be calibrated. We evaluated personal adaptation of three frozen EEG foundation models (CBraMod, REVE and LaBraM) in 235 held-out subjects from three motor-imagery datasets, comparing each subject's adapter with the population model and with adapters fitted to other sub...

---

### 7. Automatic Generation of Expert-Level Neuron Segmentation Masks from Fluorescence Microscopy Images for Non-Invasive Deep Learning Analysis of Phase-Contrast Images

**Authors:** Gerard Villarroya-Piqué, Víctor M. González, Esther Serrano-Pertierra, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34464v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34464v1)

**Summary:** Background & Objective Accurate segmentation of neurons in microscopy images of neuronal cultures is crucial for research on neurodegenerative diseases and neurotoxicity. Manual annotation of such images is time-consuming, subjective, and inconsistent across experts. Deep learning (DL) models offer an effective alternative, but require high-quality training datasets composed of microscopy images with accurately segmented neurons, typically created by experts. Neuronal cultures can be imaged usin...

---

### 8. FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model

**Authors:** Shucheng Liu, Changchun Shi, Kai Zhang, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34354v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34354v1)

**Summary:** Modeling resting-state functional magnetic resonance imaging (rs-fMRI) data is crucial for understanding brain-wide neural activity. However, traditional methods struggle to capture complex temporal dynamics over long horizons, to account for the brain's anatomical spatial structure, and to model high-dimensional ambient signals that lie on a low-dimensional intrinsic subspace. We propose FAST-Brain, a unified flow-aligned spatio-temporal surrogate brain model that addresses all three challenges...

---

### 9. T-SNN: Temporal Simplicial Neural Network for EEG Decoding

**Authors:** Nikita Malik, Shubhajit Roy, Mohit Kataria, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.34002v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34002v1)

**Summary:** Decoding brain states requires models that capture both the evolution of neural activity and interactions among groups of brain regions. Existing EEG methods often treat recordings as multivariate time series or represent functional connectivity with pairwise graphs, leaving dynamic higher-order interactions largely unmodeled. We introduce the Temporal Simplicial Neural Network (T-SNN), which represents EEG recordings as sequences of evolving simplicial complexes. By combining simplicial convolu...

---

### 10. Harmonic Theory of Behavior

**Authors:** Mohammad Salahshour, Iain D. Couzin

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33896v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33896v1)

**Summary:** Traditional models of collective behavior rely on prescribed interaction rules, leaving unresolved the question of how behavior arises from neural representations of space. Here, we develop a first-principles theory in which movement, decision-making, and collective organization emerge by coarse-graining fast neural dynamics on a topological representation of directional space. For a ring manifold encoding heading, this reduction yields a macroscopic theory of behavior: a decision landscape over...

---

### 11. Explainable Deep Learning of Resting-State Functional Connectomes Reveals Network Biomarkers of Adolescent Intelligence

**Authors:** Md. Tanvir Rahman, Nabil Anan Orka, Asaduzzaman Khan, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33422v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33422v1)

**Summary:** Mapping resting-state brain organization to individual differences in cognitive ability remains a major challenge in population neuroinformatics. Although deep learning enables flexible modeling of brain connectivity, limited interpretability restricts its scientific and clinical utility. To address this objective, we developed an explainable deep learning framework based on sparse projected residual networks to predict fluid, crystallized, and total intelligence from resting-state functional ma...

---

### 12. Towards a full-stack functionalist theory of consciousness: Identifying its functional profile

**Authors:** Sushrut Thorat, Paras Chopra

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33366v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33366v1)

**Summary:** If consciousness is functional, a basic question is what awareness of a content actually changes in how a system operates on it. We ask, for a particular content X and mental or bodily process Y, whether awareness of X changes whether, or how well, X can be used in process Y. Crucially, X-aware and X-unaware conditions must be compared in ways that rule out poorer information about X as a sufficient explanation. Our current literature sweep yields a small but informative functional profile. The ...

---

### 13. Pre-registered spectral and certified mixing analysis of the male Drosophila central nervous system connectome

**Authors:** Eran Kopel

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33054v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33054v1)

**Summary:** We report a pre-registered test of five hypotheses about the synapse-flow random walk on the connectome of the male Drosophila central nervous system (166,700 neurons, 124 million synapses), in which a walker moves to a postsynaptic partner in proportion to synapse number. The hypotheses concern the spectral gap and its dependence on the neck connective, the localisation of the leading modes of an input-normalised signed map, the certified mixing depth measured by the Dobrushin coefficient, its ...

---

### 14. Periodically modulated traveling waves in integrate-and-fire networks: recursive speed law and propagation failure

**Authors:** Jie Nissel, Ricardo Erazo-Toscano, Rosahn Bhattarai, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.33006v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33006v1)

**Summary:** Traveling waves of activity in neural tissue can be halted by spatial inhomogeneity in synaptic coupling. We study an integrate-and-fire network in which each neuron fires once and the coupling decays exponentially. For this model the leading-edge firing map reduces exactly to a scalar equation for the wave speed in space, with a slow unstable and a fast stable homogeneous speed, $c_1$ and $c_2$, and a periodic modulation of the coupling enters this equation pointwise. Positive periodic waves te...

---

### 15. Beyond Gaussian Assumptions: Distribution-Aware Channel Capacity for Effective Connectivity

**Authors:** Jianan Jian, Jacob Kang, Nurahmed Multezem, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32774v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32774v1)

**Summary:** Effective-connectivity estimation from brain signals often relies on Gaussian residual modeling, which enables tractable estimation but can discard informative distributional structure and distort inferred directed interactions when empirical residuals are non-Gaussian. We show across multiple modalities, species, and experimental conditions that both brain signals and fitted channel residuals frequently deviate from Gaussianity. We therefore introduce a distribution-aware, information-theoretic...

---

### 16. Space versus Context: Competition for limited neural resources determines engram cell allocation in the hippocampus

**Authors:** Kensuke Chiba, Jun-nosuke Teramae

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32620v1)

**Summary:** Engram cells in hippocampal CA1 represent contextual information associated with events experienced by animals and constitute a cellular substrate of episodic memory. Recent experiments have shown that a subset of hippocampal place cells is recruited as engram cells for individual contexts. However, the principle governing engram cell allocation across contexts remains unclear. Here, we develop an information-theoretic framework that quantifies the trade-off between spatial and contextual inform...

---

### 17. Recovery-Directed Symbolic Distillation of Neural Likelihoods

**Authors:** Kianté Fernandez, Xinwei Li

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32409v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32409v1)

**Summary:** Amortized neural likelihoods enable computationally expensive inference for models with analytically intractable or unspecified likelihoods, but their black-box nature limits interpretability. We introduce a symbolic distillation pipeline that converts trained neural likelihoods into explicit, interpretable expressions optimized for efficient parameter estimation. Our approach uses a recovery-directed objective to guide symbolic regression toward expressions that preserve parameter-recovery accu...

---

### 18. From Signals to Trajectories: A Primer on Low-Dimensional Dynamics in Human EEG and MEG

**Authors:** Vanessa Hadid, Hamza Abdelhedi, Annalisa Pascarella, et al.

**Published:** 2026-09-26

🔗 [Paper](http://arxiv.org/abs/2609.32315v1) | 📄 [PDF](https://arxiv.org/pdf/2609.32315v1)

**Summary:** Neural activity unfolds not as a set of independent signals, but as a coordinated dynamical process that can be described as a point moving through a high-dimensional state space. This perspective has contributed substantially to recent developments in systems neuroscience, especially through studies of directly recorded neuronal population activity, but remains comparatively underused in non-invasive human recordings such as EEG and MEG. In this primer, we present a neural trajectory analysis b...

---

### 19. MAESTRO: a Multimodal Auditory-attention Egocentric Speech-TRacking Open corpus

**Authors:** K M Naimul Hassan, Ali Alavi, Donald S. Williamson

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31898v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31898v1)

**Summary:** Humans rely on gaze, head movements, and visual cues to attend to speakers in noisy environments, yet auditory attention decoding (AAD) has been studied primarily using electroencephalography (EEG). We introduce the Multimodal Auditory-attention Egocentric Speech-TRacking Open (MAESTRO) corpus, the first AAD dataset to simultaneously record EEG, eye gaze, pupillometry, egocentric video, and head inertial measurement unit (IMU) data. MAESTRO includes four competing speakers and background noise a...

---

### 20. FlatClip: A Geometry-Aware Surface-Level Baseline for fMRI Representation Learning

**Authors:** Mo Wang, Wenhao Ye, Zihan Ning, et al.

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31204v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31204v1)

**Summary:** Recent fMRI foundation models differ substantially in the spatial scale at which they represent brain activity. ROI- and connectivity-based models are efficient but coarse, whereas voxel-level models preserve fine-grained spatial structure but require specialized 3D/4D architectures and costly fMRI-specific pretraining. We ask how effectively an image-pretrained encoder can reuse the spatial organization of cortical activity. Motivated by evidence that macroscale brain activity is strongly const...

---

### 21. Learning a non-linguistic code for inferred rules from reward

**Authors:** Cristiano Capone

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31192v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31192v1)

**Summary:** How can a rule inferred from examples reach someone who never saw them, without a shared code? Patients with severe aphasia do it by gesture or sketch. One network sees worked examples and emits eight invented symbols; a second, blind to them, applies them to a new input. Rewarded for the second's success, the first learns a code carrying rules to three-step transformations training never presents, which new learners acquire. Like invented human languages, the code has two regimes: under reward ...

---

### 22. Grid-cell firing fields lack local sixfold symmetry

**Authors:** Anian Kerscher

**Published:** 2026-09-25

🔗 [Paper](http://arxiv.org/abs/2609.31145v1) | 📄 [PDF](https://arxiv.org/pdf/2609.31145v1)

**Summary:** The firing fields of a grid cell form a hexagonal lattice, yet each field's intrinsic geometric structure remains unclear: Are individual grid fields radially symmetric or do they exhibit (weak) sixfold modulation inherited from the global lattice? To address this question, we quantified the within-field angular structure using harmonic analysis and per-cell matched simulations that preserved sampling statistics, field scale, and lattice geometry after correction for global elliptic deformation....

---

### 23. A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics

**Authors:** R. Lahoz-Beltra

**Published:** 2026-09-24

🔗 [Paper](http://arxiv.org/abs/2609.29984v1) | 📄 [PDF](https://arxiv.org/pdf/2609.29984v1)

**Summary:** Understanding the neurobiological mechanisms underlying self-referential cognition and baseline self-consciousness remains a fundamental challenge in computational neuroscience. In this work, we propose a large-scale computational model incorporating a 10,000-neuron spiking neural network (SNN) based on Izhikevich dynamics. The network is structured into two interacting subsystems: a sensory processing layer (5,000 regular-spiking cortical neurons) and an endogenous Default Mode Network (DMN) pa...

---

### 24. AI-Driven Neural Surrogates for In Silico Design of Cognitive-Affective Neuromodulation Targets

**Authors:** Marco Rothermel, Madleen Stenger, Soroush Daftarian, et al.

**Published:** 2026-09-23

🔗 [Paper](http://arxiv.org/abs/2609.27729v1) | 📄 [PDF](https://arxiv.org/pdf/2609.27729v1)

**Summary:** In neuropsychiatry, the primary goal is often not only to decode brain activity but to change it, for example to lessen a negative affective bias or an overly salient memory. Motivated by control theory, we develop an AI-driven neural-surrogate framework that proposes candidate representational changes and tests their predicted perceptual effects from snapshots of stimulus-evoked fMRI activity, without physical stimulation. The framework combines fMRI decoding, deep generative modeling, and cons...

---

### 25. The Computational Value of Sensory-Aligned Receptive Fields Depends on Neuronal Expressivity

**Authors:** Agnese Adorante, Aaron Spieler, Anna Levina

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26940v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26940v1)

**Summary:** Biological sensory neurons have selective receptive fields organized along meaningful stimulus coordinates, such as frequency, motion direction, or retinotopic position. Such structure may arise from efficient coding and biological constraints on activity, connectivity, and wiring, as computational studies of simple neurons have shown across modalities. This raises a question: do structured receptive fields confer a computational advantage beyond resource efficiency itself, and does this advanta...

---

### 26. Deep Learning in Infant Functional Neuroimaging: Challenges, Advances, and Future Directions

**Authors:** Dan Hu, Jiale Cheng, Weiran Xia, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26688v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26688v1)

**Summary:** Infancy is a critical developmental window characterized by rapid functional brain reorganization, during which large-scale networks emerge, individualized connectome signatures continue to form, and early deviations may shape long-term cognitive and clinical outcomes. Functional MRI (fMRI) offers an opportunity to study these processes in vivo, yet extracting developmentally meaningful information from it remains challenging due to comparatively short scan duration, structured motion artifacts,...

---

### 27. Physics-constrained inference of somatic dynamics from dendritic recordings with sparse somatic supervision in weakly coupled two-compartment neuron model

**Authors:** Abdeltif Oujbara, Benjamin Ambrosio, M. A. Aziz-Alaoui

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25436v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25436v1)

**Summary:** Somatic membrane potential is the primary determinant of neuronal output, yet it remains inaccessible in many experimental setups where only dendritic recordings are available. Reconstructing somatic dynamics from distal measurements is a challenging inverse problem, particularly when the soma and dendrites are weakly coupled, as dendritic signals represent a filtered and attenuated version of somatic activity. To address this, we use a physics-informed neural network (PINN) constrained by a two...

---

### 28. A theory of plasticity: capacity for change as inverse configurational constraint

**Authors:** Igor Branchi

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25312v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25312v1)

**Summary:** Plasticity is invoked across the sciences to explain how systems can change, yet it is inferred from the very change it is meant to explain. A system may have many alternatives, realize none and still be plastic. Another may be driven far toward its only alternative, but the magnitude of that change does not establish its plasticity. What matters for plasticity is not how far the system moves but how strongly its present configuration constrains alternatives. Here I propose that plasticity, unde...

---

### 29. Binding-Motivated Contextuality: A Cross-Domain Cyclic Test in Perception and Judgment

**Authors:** Adam Y. Shavit

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.23977v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23977v1)

**Summary:** Perceptual binding and the contextuality of judgment are studied apart, in psychophysics and decision research. We argue they share one obstruction: a nonzero class in $H^1$ of a presheaf with no global section -- though only contextuality is tested, since binding's obstruction vanishes. We build on sheaf formulations of predictive coding (Seely 2025) and contextuality (Abramsky & Brandenburger 2011): a cyclic set of pairwise judgments admits a global (noncontextual) explanation exactly when the...

---

### 30. Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery

**Authors:** Kevin Zhou, Sparsh Roy

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23924v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23924v1)

**Summary:** Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks. We audit LaBraM and CBraMod on motor imagery under a validation-locked protocol in which preprocessing, architecture, optimization, freeze depth, checkpoint, temperature, and method selection are determined using training-session data only. On four-class BCI Competition IV-2a, every supe...

---

### 31. A discrete generative model of neuronal spiking activity on microelectrode arrays

**Authors:** Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23907v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23907v1)

**Summary:** Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a d...

---

### 32. From Biological Precursors to Artificial Cognition: Consciousness, Embodiment, and the MEM Architecture

**Authors:** Janusz A. Starzyk, Wiesław L. Galus

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23828v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23828v1)

**Summary:** This article asks under what conditions artificial intelligence could warrant a rational attribution of consciousness. Linguistic ability, multimodality, memory, planning, action control, and humanoid embodiment are not sufficient evidence of phenomenal experience. Biological precursors such as excitability, homeostasis, neural networks, and hierarchical representation instead identify functions whose counterparts may be engineered. The paper compares conventional LLMs, hybrid h-LLMs, vision-lan...

---

### 33. Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification

**Authors:** Zihan Wang, Daixin Li, Guilin Wang, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23317v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23317v1)

**Summary:** Epileptic seizures arise from complex, nonlinear interactions within brain networks, yet reliable electroencephalographic (EEG) prediction remains challenging due to the nonstationary and heterogeneous nature of neural dynamics. Existing methods typically analyze EEG data as static or weakly time-dependent snapshots, overlooking the intrinsic dynamics and lacking the geometric sensitivity to capture the hierarchical, localized evolution of the epileptogenic zone. To address these limitations, we...

---

### 34. BrainWideBench: Benchmarking large-scale pretraining and across-animal transfer in multi-region neural recordings

**Authors:** Alexandre Andre, Shivashriganesh P. Mahato, Vinam Arora, et al.

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22064v1)

**Summary:** Advances in large-scale neural recording have made it possible to collect data across many animals and distributed brain regions, raising the question of whether this scale can be exploited to learn general-purpose neural representations transferable across diverse downstream tasks. Yet, progress toward this goal has been limited by fragmented evaluation protocols and a narrow focus on individual task domains. Here, we present BrainWideBench, a benchmark for evaluating across-animal transfer on ...

---

### 35. Identifying Neural State Changes due to Gain versus Off-Manifold Displacement

**Authors:** Sam McKenzie

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21272v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21272v1)

**Summary:** Memory segmentation is thought to arise from rapid decorrelation in neural activity, often quantified by Euclidean distance or cosine angle. Although these metrics detect a transition, they do not reveal how the new state relates to the repertoire represented by the neural manifold. This matters because neuromodulators that drive state transitions also alter excitability, and learning may repurpose existing representations or create new ones. Here, I introduce a geometric decomposition that sepa...

---

### 36. Foundation-model-based multi-label phenotyping of combined hyperkinetic movement disorders

**Authors:** Laura Cif, Zohra Souei, Diane Demailly, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.22369v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22369v1)

**Summary:** Movement disorders (MDs) frequently co-occur, yet phenomenological and severity assessment shows substantial inter-rater variability. Markerless video could improve reproducibility, but prior work is largely single-symptom, depends on standardized acquisition, and lacks validation and transfer across ages and sites. We combined two foundation models into one frozen backbone: Segment Anything Model 3 (SAM 3) for dense, per-frame markerless segmentation summarized into geometric, contour and grid ...

---

### 37. A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound

**Authors:** Thomas J Stoll, Ross K Maddox

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20595v2) | 📄 [PDF](https://arxiv.org/pdf/2609.20595v2)

**Summary:** Computational models of auditory physiology commonly target specific responses or stages of the auditory pathway, limiting their ability to integrate findings across experimental paradigms and neural timescales. We present a foundation model of human auditory electrophysiology: a causal neural network trained to map binaural acoustic waveforms directly to high-sample-rate EEG. The model was trained on approximately 250 hours of EEG data from 92 subjects, with varied electrode montages and stimul...

---

### 38. A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20437v1)

**Summary:** This article presents a mathematical model of the Motivated Emotional Mind cognitive architecture developed for embodied intelligent systems. Such a system learns to maintain its homeostasis through a generalized form of reinforcement learning based on its internal motivations, termed motivated learning (ML). The principal contribution of this article is a rigorous formalization of the re-entrant loop integrating feedforward processing, lateral interactions, and feedback pathways, together with ...

---

### 39. Neural noise enables accurate internal simulation of rare events

**Authors:** Heng Zhang, Pawel Herman, Zenas C. Chao

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18033v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18033v1)

**Summary:** The brain needs an accurate internal model of the world to generate predictions and guide behavior. However, it must estimate the statistical structure of the environment from limited experience. This is particularly difficult for rare events, whose observed frequencies in a limited sample may substantially under- or overestimate their true frequencies. How the brain constructs an accurate internal model despite this sampling problem remains unclear. We address this problem using a Bayesian Conf...

---

### 40. Spike Sorting with VanillaSort

**Authors:** Zishuo Feng, Feng Cao

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.22322v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22322v1)

**Summary:** Training spike detectors on real recordings is challenging because algorithmically generated labels can be noisy and incomplete. We propose VanillaSort, combining multichannel detection with spatially augmented, template-guided clustering. VanillaDet uses visibility-aware masking, truncated Gaussian targets and a temporally tolerant positive-bag loss, followed by conditional event-SNR gating. VanillaCluster combines HuiduRep embeddings with relative-amplitude features for Gaussian mixture cluste...

---

### 41. Learning Options for Compositional Motor Control with Adapter Banks

**Authors:** Sreejan Kumar, Marcelo Mattar, Lea Duncker

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17042v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17042v1)

**Summary:** Learning flexible motor primitives is a hallmark of skilled motor control. Recent neuroscience theory proposes that motor primitives may be implemented as low-rank perturbations of a shared recurrent network, but leaves open how such a system is learned. We translate this principle into a novel architecture for learning motor skills end-to-end: a shared recurrent core modulated by a bank of residual adapters, each selected by a discrete latent code. Trained on closed-loop biomechanical control, ...

---

### 42. Predictor Construction Can Reverse Multimodal Neural Contrasts

**Authors:** Lucas Nadolskis, Galen Pogoncheff, Michael Beyeler

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16430v1)

**Summary:** Foundation-model features are increasingly used to ask what information neural activity represents, often by comparing prediction gains between nested encoding models. We show that such multimodal contrasts can change sign when only the conditioning predictor is reconstructed. Using fMRI from the Natural Scenes Dataset, DINOv2 visual features, and MPNet embeddings of MS COCO captions and Localized Narratives, a caption-narrative contrast in the additional predictive contribution of vision favors...

---

### 43. A neural-astrocyte architecture implements a hybrid automaton for evidence accumulation

**Authors:** Giacomo Vedovati, Ilya E. Monosov, Thomas J. Papouin, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16217v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16217v1)

**Summary:** Astrocytes are non-neuronal glial cells that are receiving widespread attention due to their emerging role in neural computation. In this paper, we propose and study dynamical mechanisms by which astrocytes may augment the ability of neural networks to infer context in reinforcement learning (RL) settings. We construct a biologically inspired, two-level dynamical neural-astrocyte network with distinct spatial and temporal organization. We train this model on a hierarchical multi-context task tha...

---

### 44. Decision-Related Cognitive Signatures from Fast-Slow Dynamics: A Low-Dimensional Observation-Operator Framework

**Authors:** Furkan Emre Isik, Ali Demirci

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15918v1)

**Summary:** Repeated decisions exhibit temporal structures such as persistence, direction-dependent switching, recurrent alternation, and abrupt transitions. We examine the generative sufficiency of a two-dimensional fast-slow dynamical system. The system combines a cubic fast equation with linear slow feedback and is analyzed through its equilibrium geometry, trace-determinant structure, equilibrium-fold loci, candidate Hopf boundaries, and singular critical manifold. An explicit observation operator proje...

---

### 45. The Cross-Substrate Access Assay: What an Indicator Test Must Declare to Travel from Brain to Language Model

**Authors:** Pieter van Rooyen

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.22300v2) | 📄 [PDF](https://arxiv.org/pdf/2609.22300v2)

**Summary:** Testing an artificial system for a property linked to consciousness means applying a measurement developed on brains to a system that is not one. Such a transfer must re-examine five parts of the procedure: the competing statistical models, how they are fitted, the unit the inference generalizes over, the quantity the uncertainty interval is about, and the rule that turns a result into a verdict. The Cross-Substrate Access Assay declares all five. Because brain and model signals share no physica...

---

### 46. When Teachers Smile or Frown: A Profile-Based Analysis of Achievement Emotions

**Authors:** Rudra Mukhopadhyay, Satyaki Mazumder, Koel Das

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15747v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15747v1)

**Summary:** Achievement emotions shape how students engage with and learn from academic tasks, yet most studies examine individual emotions rather than co-occurring affective profiles and their dynamics. We examined latent achievement-emotion profiles and their transitions following exposure to different instructor facial expressions during a video lecture. Self-reported data from 78 Grade VII and VIII students revealed three profiles: enthusiastic, demotivated, and vulnerable. Profile transitions differed ...

---

### 47. Nonlinear dynamics of random neural networks with second-order synaptic motifs

**Authors:** Jun Yang, Hannah Choi

**Published:** 2026-09-13

🔗 [Paper](http://arxiv.org/abs/2609.14251v1) | 📄 [PDF](https://arxiv.org/pdf/2609.14251v1)

**Summary:** Classical theories of random neural networks typically assume independent connectivity, overlooking the local motif structures prevalent in biological circuits. Here, we investigate how four second-order synaptic motifs (chain, reciprocal, convergent, and divergent) shape the dynamics of nonlinear firing-rate networks. While previous studies have established that chain correlations generate outlier eigenvalues, we demonstrate that these motifs also jointly reshape the Jacobian eigenvalue bulk. U...

---

### 48. URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining

**Authors:** Po-Han Chiang

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13899v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13899v1)

**Summary:** The BabyLM challenge measures how much language a model can learn from developmentally-plausible, child-scale data rather than internet-scale corpora, yet prior language models forgo the biological constraints of the neural circuitry that acquires human language: spiking neurons separated into excitatory and inhibitory populations wired by a recurrent lateral connectome. This paper presents URCHIN (Unified Recurrent Connectome with Horizontal Integrate-and-fire Neurons), which applies the Parall...

---

### 49. Hierarchical emergence of network bursting in a four-cell central pattern generator model

**Authors:** Krishna Pusuluri, Huiwen Wu, Andrey L. Shilnikov

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13858v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13858v1)

**Summary:** How can a neural circuit rhythmically burst when none of its constituent neurons can endogenously do so? We address this question through a bottom-up reconstruction of a 4-cell neural circuit modeled after the swim central pattern generator (CPG) of the sea slug \textit{Dendronotus iris}. We first map the intrinsic regimes of a swim interneuron (SiN) model neuron and show that slow mutual inhibition can generate anti-phase bursting in a half-center oscillator (HCO) assembled from tonic-spiking o...

---

### 50. Pretraining for Sample-Efficient Neural Interfaces

**Authors:** Ben Tang, Zachary Spalding, Gregory B. Cogan

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13507v1)

**Summary:** Brain-computer interfaces (BCIs) decode neural activity to restore lost function. Typically, training a high-performance neural decoder requires a large labeled dataset to be collected from every new subject. One way to reduce the labeled data cost is self-supervised pretraining, which learns general neural representations from unlabeled recordings that accumulate across subjects. However, for intracranial electroencephalography (iEEG) recordings, self-supervised learning has been challenging du...

---

## stat.ML

**50 papers**

### 1. Guided Uncertainty-Aware Robust Domain Transfer

**Authors:** Xin Xiong, Zijian Guo, Tianxi Cai

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35654v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35654v1)

**Summary:** Artificial intelligence models deployed as clinical decision support tools often suffer substantial performance degradation over time and across institutions due to covariate shift, concept drift, and cross-system heterogeneity. Fully retraining complex models is frequently infeasible, particularly in EHR settings where labeled outcome data are scarce and regulatory constraints limit model modification. We propose GUARD (Guided and Uncertainty-Aware Robustness to Domain shift), a unified statist...

---

### 2. Arbitrary-Accuracy Neural Approximation with Optimal Neuron Count and Near-Optimal Bit Complexity

**Authors:** Zilan Cheng, Li-Lian Wang, Zhongjian Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35628v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35628v1)

**Summary:** We study the minimum number of hidden neurons required for arbitrary-accuracy approximation of multivariate Hölder-continuous functions on $[0,1]^d$ and the associated encoding complexity. For $d\geq 2$, we construct a fixed, explicitly defined activation function for which a closed-form network with two hidden layers of widths $d$ and $1$ achieves arbitrary accuracy in the uniform norm. We prove that $d+1$ is the exact minimum total number of hidden neurons among standard feedforward networks w...

---

### 3. Elicitation and Decision Geometry in Single-Index Bandits

**Authors:** Sakshi Arya, Cheng Soon Ong

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35622v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35622v1)

**Summary:** We study two-arm contextual bandits with arm-specific single indices and a shared unknown monotone link. Monotonicity makes the optimal action depend only on the contrast between the index directions, hence arm-specific reward functions need not be estimated. We introduce Natural Boundary Learning (NBL), a greedy procedure that uses a sequential Stein contrast to learn the optimal boundary directly, without estimating the reward functions or the common link. We characterize the local Riemannian ...

---

### 4. Control-Geometry Straightening for Sampling-Based Latent Planning

**Authors:** Ziang Fu, Ning Ning

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35603v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35603v1)

**Summary:** Joint-embedding predictive architectures enable planning with latent world models, but accurate transition prediction alone does not ensure that the planning objective is easy to optimize. We introduce Control-Geometry Straightening (CGS), a single auxiliary loss that learns planner-friendly representations by directly straightening control geometry for sampling-efficient planning. CGS matches pairwise cosine similarities among actions to those among corresponding latent differences only using l...

---

### 5. Learning Conditional Expectation Operators via Functional Newton Updates

**Authors:** Thiago Ramos, Alek Fröhlich, Daniel Perazzo, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35598v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35598v1)

**Summary:** We introduce the Functional Spectral-Newton Method (FSNM) for learning the leading singular structure of a conditional expectation operator without fixing a basis or reproducing kernel Hilbert space. FSNM fits a low-rank representation of the centered joint-to-product density ratio kernel by alternating functional Newton updates. Each update reduces to a preconditioned regression, which we approximate with vector-valued regression trees in a stagewise boosting procedure. At the population level,...

---

### 6. Simplex Diffusion Models

**Authors:** Justin Deschenaux, Alexandre Galashov, Andrew Campbell, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35553v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35553v1)

**Summary:** Diffusion models have revolutionized generative modeling for continuous data through the gradual refinement of a belief state. This iterative refinement has not yet carried over to discrete diffusion models, which discard uncertainty at intermediate steps through categorical sampling (information collapse). We propose Simplex Diffusion Models (SDMs), a framework that lifts the diffusion process to the probability simplex to represent beliefs over categories. SDMs admit probability paths with clo...

---

### 7. Universal Approximation of Measure-to-Measure Operators by Pushforwards

**Authors:** Takashi Furuya, Nicholas H. Nelsen, Frank Cole

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35483v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35483v1)

**Summary:** Many learning tasks map an input distribution to an output distribution. A natural way to model such an operator is to transform each input sample using a continuous function that may depend on the entire input distribution, and then take the distribution of the transformed samples. This defines a measure-dependent pushforward model and includes measure-theoretic formulations of transformers. We ask when such models can approximate arbitrary continuous operators between spaces of probability mea...

---

### 8. Multi-Task Learning of Conditional Mean Operators: applications to dynamical systems and uncertainty quantification

**Authors:** Sami Chemlal, Thibaut Germain, Rémi Flamary, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35429v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35429v1)

**Summary:** Estimating conditional statistics and learning representations of a population of conditional distributions are central problems in many data-driven applications, including uncertainty quantification and dynamical systems analysis. Conditional mean operators (CMOs), a class of linear operators between function spaces, resolve these objectives by providing access to a broad class of conditional statistics. However, existing methods typically estimate each CMO independently or constrain it to pres...

---

### 9. Convex Optimization Is Free When Accuracy Is Expensive

**Authors:** Arthur Paing, Arthur Jacot

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35418v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35418v1)

**Summary:** This paper studies convex optimization when the gradient cannot be evaluated exactly, but only approximated by a hierarchy of algorithms whose compute grows like $δ^{-γ}$ in the accuracy $δ$. When $γ>2$, falling into the Harder-Than-Monte-Carlo (HTMC) regime, the price of accuracy outruns the variance reduction that Monte Carlo would buy and we show that minimizing a loss function costs no more, up to a factor depending only on $γ$, than a single evaluation of its gradient at the accuracy the pr...

---

### 10. Isotonic surrogate modeling for computer experiments with many input variables

**Authors:** Jaehoan Kim, Simon Mak

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35354v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35354v1)

**Summary:** Virtual simulators are widely used for studying complex physical phenomena, from particle collisions to rocket propulsion. Such "computer experiments" can be highly time-intensive, and a Bayesian surrogate model can be used for efficient emulation with reliable uncertainty quantification. To train accurate surrogates with a limited sample size $n$, recent work has explored the incorporation of monotonicity (or isotonicity) information, which can often be elicited from physical systems. In practi...

---

### 11. A Hierarchy of Entropy-Shapley Games for Multivariate Predictive Uncertainty

**Authors:** Niklas Koenen, Claudia Battistin, Jeriek Van den Abeele, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35217v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35217v1)

**Summary:** Modern probabilistic machine learning models increasingly produce multivariate outputs with complex dependence structure, from multi-step time-series forecasts to sample path predictions. Understanding which input features drive the predictive uncertainty is important for risk-aware decisions, model diagnostics, and deciding whether the uncertainty should be mitigated or hedged against. This attribution problem requires a choice of how dependencies between output components are treated. Existing...

---

### 12. Propagate, Then Sharpen: Post-Hoc Refinement of Frozen Node Classifiers

**Authors:** Preben Johnsen Bentdal, Nello Blaser, Xue-Cheng Tai

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35080v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35080v1)

**Summary:** We study post-hoc refinement of frozen node classifiers: given only the graph $G$ and class distributions $Q$ predicted by a frozen model, can we improve accuracy without access to node features, model parameters, or gradients? APPNP answers this by propagating logits with a restart towards the initial predictions, minimizing the anchored Dirichlet energy. Instead, we consider the Potts energy, and decompose it into a Dirichlet term, which penalizes disagreement between neighbouring nodes, and a...

---

### 13. Universality and Generalization of Causal Transformers Across Context Lengths

**Authors:** Takashi Furuya, Maarten V. de Hoop, Gabriel Peyré

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35055v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35055v1)

**Summary:** Long contexts are central to modern transformer systems, but most expressivity results choose a different network for each fixed sequence length. We study whether one masked transformer can approximate causal token-to-token maps uniformly over sequences of arbitrary length sampling a fixed normalized horizon. To relate sampling resolutions, we model tokens by $α$-Hölder sequences or, more generally, a common modulus of continuity. Our notion of continuity across resolutions characterizes the cau...

---

### 14. GUIDE-FBO: Guidance via Uncertainty Intervention and Distributional Exchange for Federated Bayesian Optimization

**Authors:** Jintao Wei, Chenxi Li, Songhao Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35038v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35038v1)

**Summary:** Federated Bayesian Optimization (FBO) enables distributed agents to collaboratively optimize expensive black-box objectives without sharing raw local observations. However, effective knowledge transfer remains challenging under communication constraints and task heterogeneity. We propose GUIDE-FBO, in which agents exchange compact distributions over the locations of their respective optima inferred from local Gaussian process (GP) posteriors, rather than raw observations, query points, or surrog...

---

### 15. Fast Learning Rate Transfer in Shallow Linear Networks at Growing Training Horizons

**Authors:** Mana Sakai, Masaaki Imaizumi

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.35029v1) | 📄 [PDF](https://arxiv.org/pdf/2609.35029v1)

**Summary:** Hyperparameter transfer across model width can substantially reduce the cost of tuning large neural networks, but its behavior when the training horizon grows with width is not fully understood. Building on the framework of fast hyperparameter transfer (Ghosh et al., 2026), which formalizes when transfer is effective, we investigate conditions that ensure fast transfer in the growing-horizon regime. Specifically, we study learning-rate transfer in a shallow linear network with a single trainable...

---

### 16. Conformal Prediction and Conditional Coverage for Tabular Foundation Models

**Authors:** Sungwoo Park, Sunghee Park, Won Chang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34887v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34887v1)

**Summary:** Tabular foundation models (TFMs) provide predictive distributions for regression, but their prediction regions can exhibit undercoverage or overcoverage even when point predictions are accurate. We introduce C-USIM (Conditionally-Uniformized Score Integration Method), a lightweight application of highest predictive density split conformal prediction that accommodates multimodal predictions. Given calibration and test outputs, it requires no additional training or model inference. It provides fin...

---

### 17. Statistical Benefits of Fine-Tuning from Pretrained Initialization in Diagonal Linear Networks

**Authors:** Alexandre Declèves, Etienne Boursier, Nicolas Flammarion

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34756v1)

**Summary:** Adapting pretrained models to downstream tasks with limited data has become a central paradigm in modern deep learning. Yet, despite its widespread practical success, how fine-tuning leverages information from pretraining remains poorly understood theoretically. We study fine-tuning from pretrained weights through the lens of sparse linear regression and two-layer diagonal linear networks. In our setting, pretraining provides information through the support (and signs) of the initialization pred...

---

### 18. Information-Theoretic Analysis of Next-Token Prediction under Markovian Data

**Authors:** Masoud Kavian, Abdellatif Zaidi, Milad Sefidgaran

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34731v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34731v1)

**Summary:** We develop an information-theoretic framework for generalization in next-token prediction under temporally dependent data. We consider independent trajectories generated by finite-memory Markov processes and distinguish algorithmic dependence, quantified by mutual information, from temporal dependence, characterized by mixing. For cross-entropy loss, we derive an expected generalization bound using the Donsker--Varadhan variational representation and a McDiarmid-type concentration inequality for...

---

### 19. Two-Timescale Fine-tuning Provably Learns New Features for Two-Layer ReLU Networks

**Authors:** Etienne Boursier, Nicolas Flammarion

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34667v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34667v1)

**Summary:** Fine-tuning pre-trained models on specialized tasks with scarce data is central to modern deep learning. Despite its empirical success, theoretical understanding of fine-tuning remains limited. We introduce a Gaussian multi-index setting to study fine-tuning from pre-trained weights, where the teacher network has $m+1$ features, $m$ of which are learned during pre-training and one of which must be learned during fine-tuning. For two-layer ReLU networks, we show that two-timescale training, i.e.,...

---

### 20. Uniform Race: Parameter-Free Approximate Rejection Sampling

**Authors:** Seiyun Shin, Juhyeong Pang, Kwang-Sung Jun

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34639v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34639v1)

**Summary:** We study approximate sampling: given $N$ independent samples from a proposal distribution $μ$, the goal is to select one whose distribution is close to a target $π$ specified only up to a normalizing constant. Block and Polyanskiy (2023) provide finite budget error bounds for approximate rejection sampling (RS) as a function of the acceptance threshold $M$. The threshold $M$ giving the smallest bound, however, depends on properties of $(π,μ)$ that are typically unavailable from the observed samp...

---

### 21. Probabilistic Geodesic Flow Matching on Location-Scale Families

**Authors:** Zeyuan Yu, Zhi Chang, Shiwei Lan

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34613v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34613v1)

**Summary:** Flow matching (FM) has recently emerged as a promising framework for generative modeling due to its conceptual simplicity and strong empirical performance. In FM, samples are transported along a vector field parameterized by a neural network, inducing a probability path that evolves from a simple noise distribution to the target data distribution, governed by an ordinary differential equation (ODE). However, existing FM approaches predominantly rely on probability paths derived from optimal tran...

---

### 22. Nonnegative DAG Learning via Concomitant Estimation

**Authors:** Madeline Navarro, Gonzalo Mateos, Samuel Rey

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34595v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34595v1)

**Summary:** We study the problem of learning directed acyclic graphs (DAGs) with nonnegative edge weights from observational data. We propose the Nonnegative and Concomitant (NoCo) DAG estimator, which jointly recovers the weighted graph structure and the exogenous noise variances in the linear structural equation model for the observations. Different from prior art, this noise-adaptive formulation blends a smoothed concomitant lasso criterion with a simpler log-determinant acyclicity constraint that exploi...

---

### 23. Deep Weighted Bellman Residual Minimization for $Q^*$ Estimation

**Authors:** Lican Kang, Jerry Zhijian Yang, Cheng Yuan, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34593v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34593v1)

**Summary:** Off-policy evaluation is a foundational component of offline reinforcement learning, aiming to assess and optimize policy performance using pre-collected datasets. However, such datasets often suffer from pronounced challenges, including distribution shift, $Q$-value overestimation, and low sample utilization efficiency. To address these issues, this paper introduces a weighted Bellman residual minimization framework that incorporates density ratio weighting by effectively integrating expert dem...

---

### 24. Understanding Generalization Requires Universal Induction

**Authors:** Aram Ebtekar, Marcus Hutter, Danica J. Sutherland

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34458v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34458v1)

**Summary:** Classical statistical theory is insufficient to explain the successes of general-purpose AI models, because it depends on handcrafted inductive biases that it cannot justify. No Free Lunch (NFL) theorems force any learner that beats chance on some environments to underperform on others. We might hope that past experience informs which environments to expect, but NFL applies equally to meta-learning. Thus, any method that makes meaningful predictions necessarily begins with an inductive bias exte...

---

### 25. Unbiased Top-$k$ Estimation for On-Policy Distillation

**Authors:** Linjian Meng, Siyuan Gan, YuHan Li, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34447v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34447v1)

**Summary:** On-policy distillation (OPD) is becoming an important component of large language model (LLM) post-training for transferring the reasoning capability of a strong teacher LLM to a weaker student LLM. OPD trains the student by minimizing the reverse KL divergence between the teacher and the student via rollouts generated by the student's policy. However, estimating the gradient of the reverse KL divergence in OPD remains a challenge. Using only the sampled token from the student-generated rollout ...

---

### 26. On the Relation Between Interval Regret and Dynamic Regret

**Authors:** Yi-Han Wang, Peng Zhao, Zhi-Hua Zhou

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34423v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34423v1)

**Summary:** Non-stationary online learning has attracted much attention in recent years, as static regret is insufficient to guide algorithm design in changing environments. To address this limitation, interval regret and dynamic regret have been introduced as two representative performance metrics that strengthen static regret in complementary directions. Interval regret requires an online algorithm to achieve competitive static regret over every local time interval, whereas dynamic regret evaluates perfor...

---

### 27. Unlocking Few-Step Diffusion for Faithful Previews

**Authors:** Jing Jia, Sifan Liu, Guanyang Wang

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34406v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34406v1)

**Summary:** Sampling latency compounds in diffusion workflows, where users generate and discard many candidates before keeping one. Surprisingly, the poor outputs of standard few-step samplers do not reflect a lack of reconstruction capacity: by optimizing only the initial noise, frozen 3-4-step samplers can closely reproduce their corresponding full-step outputs. Building on this finding, we learn corrections to the initial noise and denoising updates using endpoint supervision, improving correspondence wi...

---

### 28. ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control

**Authors:** Eric Frankel, Banghua Zhu, Sewoong Oh, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34374v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34374v1)

**Summary:** Language model post-training is often bottlenecked by the need for human-collected preference data, which is expensive and difficult to scale. Reinforcement learning from AI feedback (RLAIF) style approaches that leverage pseudo labels offer an abundant alternative but introduce systematic biases that degrade downstream alignment. Recent general-purpose semi-supervised methods correct for teacher bias using a small set of human-labeled examples, but suffer from high variance especially when huma...

---

### 29. CoeF-SFL: Preserving Collaborative Server-Client Learning with Enhanced Communication Efficiency

**Authors:** Junwoo Bae, Jin-Hyun Ahn

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34360v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34360v1)

**Summary:** Split Federated Learning (SFL) enables resource-constrained clients to participate in collaborative training, but vanilla SFL exchanges smashed data and gradients at every batch, which incurs significant communication overhead. Recent methods reduce this overhead with an auxiliary network at the client-side cut layer. However, we identify that this approach makes the client optimize a local objective that differs from the end-to-end objective, which fundamentally limits the collaborative trainin...

---

### 30. Functional Autoencoders for Amplitude-Phase Representation Learning

**Authors:** Peida Wu, Xinyang Xiong, Pengcheng Zeng

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34207v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34207v1)

**Summary:** Functional data are intrinsically infinite-dimensional, and often exhibit phase variation, where corresponding events occur at different times across observations. Existing linear dimension reduction methods struggle with nonlinear amplitude variation, while functional autoencoders without an explicit warp entangle temporal misalignment with shape. We propose the Amplitude--Phase Functional Autoencoders (AP-FAE), an unsupervised framework for functional data that spans both univariate and multiv...

---

### 31. AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning

**Authors:** Yingbo Zhao, Zeyu Yang, Zhoufan Zhu

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34188v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34188v1)

**Summary:** Formulaic alpha discovery is a core challenge in quantitative trading, as identifying alphas that work well together remains difficult. Recent reinforcement learning (RL) methods formulate this task as a Markov decision process (MDP), but two important issues remain unresolved. First, as the alpha pool evolves, the reward function changes accordingly, making the MDP inherently non-stationary. Second, most existing methods optimize a single objective, typically predictive power, while ignoring ot...

---

### 32. GT-PSSM: Unified Probabilistic Framework for Stochastic Dynamics Modeling and Dependency Learning in Multivariate Time Series Anomaly Detection

**Authors:** Wonmo Koo, Jaeyeong Lee, Taeseong Yoon, et al.

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34161v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34161v1)

**Summary:** Multivariate time series anomaly detection (MTAD) is crucial for ensuring the safe and reliable operation of complex systems. Many existing methods learn normal patterns by training reconstruction or forecasting models on predominantly normal data. However, a large portion of these approaches rely on deterministic models and their associated point-wise output errors for anomaly scoring. Since real-world multivariate time series are inherently stochastic due to measurement noise and intrinsic sys...

---

### 33. The Statistical Cost of Causal Discovery with Feedback

**Authors:** Sunmin Oh, Seungsu Han, Gunwoong Park

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34050v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34050v1)

**Summary:** What determines the unavoidable sample cost of learning cyclic causal structure? For cyclic linear non-Gaussian models, we study exact condensation recovery from observational data: identifying the strongly connected component (SCC) partition and all edges between components. We establish the first information-theoretic lower bounds on sample complexity for this target. For $p$ variables, maximum SCC size $s_{\max}$, and maximum external-parent count $d_B$, any estimator requires order $s_{\max}...

---

### 34. Singularities of Non-negative Matrix Factorization and their application to Bayesian inference

**Authors:** Naoki Hayashi, Yota Maeda, Yasushi Esaki

**Published:** 2026-09-28

🔗 [Paper](http://arxiv.org/abs/2609.34043v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34043v1)

**Summary:** Non-negative matrix factorization (NMF) is a singular statistical model whose Bayesian asymptotics are governed by the real log canonical threshold (RLCT). We study the local geometry of the factorization map and derive an upper bound for the RLCT of NMF. Let $H$ be the model inner dimension and $H_0$ the non-negative rank of the true $M\times N$ matrix. Assuming that the true matrix admits a strictly positive factorization of inner dimension $H_0$ in the interior of the parameter domain, we pro...

---

### 35. Posterior Regimes and Latent Deception: Variational Bayesian Inference in Hidden Markov Models for Sequential Fraud Detection in Financial Transactions

**Authors:** Joseph Uririoghene Obukofe, Anthony O'Hare, Chioma Sandra Dike

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.34031v1) | 📄 [PDF](https://arxiv.org/pdf/2609.34031v1)

**Summary:** We present a three-tier progression of Hidden Markov Models: maximum-likelihood (Baum-Welch), variational Bayesian (VBEM), and a neural variational extension (Neural VBEM), that model each customer's transaction history as a trajectory through a small number of latent behavioural regimes, one of which is empirically identified as fraud-associated. The Neural VBEM HMM replaces the fixed Gaussian-multinomial emission family with a learned encoder, compressing a 741-dimensional transaction represen...

---

### 36. HARMONIA: Interpretable Graph Learning through Mixtures of Neural Bases

**Authors:** Quan D. Bui, Nguyen Do, An Nguyen Dang, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33972v1)

**Summary:** Existing interpretable graph additive models still face limitations in either computational scalability or modeling flexibility. In terms of structural modeling, previous approaches either face quadratic scaling costs or sacrifice explicit source-to-target contribution decomposition. In terms of feature components, they rely either on per-feature neural networks or on single shared bases with limited feature specialization. We address both problems by introducing HARMONIA: Interpretable Graph Le...

---

### 37. Two-Sample Testing for Inhomogeneous Random Graphs in Non-Integral $L_r$ Norms

**Authors:** Soham Dan

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33968v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33968v1)

**Summary:** Testing whether two populations of networks share the same edge probabilities is a basic problem in network inference. How hard it is depends on the norm used to measure the difference. For the inhomogeneous Erdős--Rényi (IER) model, the optimal sample complexity is known for every integer $L_r$ norm and for $1\le r<2$. For non-integral $r>2$, however, the known upper and lower bounds do not match, and the lower bound was conjectured to be tight. We study this gap for two-sample testing on align...

---

### 38. Conformal Coverage of Time Series: Validity and Inference

**Authors:** Percy S. Zhai, Maggie Cheng, Wei Biao Wu

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33868v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33868v1)

**Summary:** Conformal prediction provides marginal coverage guarantees, yet practitioners may wonder if the observed coverage is truly abnormal or consistent with sampling variation. Inference for realized coverage has received comparatively little attention, especially for time series. We study split conformal prediction with adjacent calibration and test sets of temporally dependent data. Using the functional dependence measure, we derive non-asymptotic bounds on marginal coverage error without mixing ass...

---

### 39. Valid and Efficient Split Conformal Regression for Time Series

**Authors:** Percy S. Zhai, Maggie Cheng, Wei Biao Wu

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33866v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33866v1)

**Summary:** We study conformalized quantile regression and conformalized median regression that fit a model on one block of a time series and calibrate the conformal interval on the adjacent block. The existing theory of conformal prediction for time series rests largely on mixing conditions, which are hard to verify from a time-series model and fail for many standard processes, including simple ones with short memory. We replace this theoretical toolbox with the functional dependence measure, which in prin...

---

### 40. An Active-Bottleneck Mechanism for Weak-to-Strong Generalization

**Authors:** Mohammad Zeinalpour, Amir Najafi

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33835v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33835v1)

**Summary:** Weak-to-strong generalization (W2SG) occurs when a student trained on a teacher's predictions outperforms that teacher. We study when this happens under fully converged, ridgeless two-stage learning, with no early stopping, no explicit regularization, and no assumption that the student is more expressive than the teacher. In two-stage linear regression, a teacher is fit from $n$ labeled examples and a student is trained solely on the teacher's predictions on $m$ fresh, unlabeled inputs. Although...

---

### 41. Oracle-Efficient Online Classification with Stochastic Inputs and Adversarial Outputs

**Authors:** Gon Buzaglo, Elad Hazan

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33760v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33760v1)

**Summary:** We consider contextual binary prediction with i.i.d. contexts from an unknown distribution and adaptively chosen losses. We show that a simple Follow-the-Perturbed-Leader algorithm with Gaussian perturbation for each observed context achieves the optimal $\widetilde O(\sqrt{T\log N})$ expected regret for a class of $N$ experts, while requiring one optimization-oracle call per round and no explicit enumeration of the class. For an infinite hypothesis class $\mathcal H$, the algorithm attains $\wi...

---

### 42. Multi-Marginal Inverse Optimal Transport for Contrastive Learning Via Explicit Anchor-Positive-Negative Coupling

**Authors:** Ngoc-Hai Nguyen, Thuan Nguyen, Prakash Ishwar, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33741v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33741v1)

**Summary:** Inverse Optimal Transport (OT) based methods for representation learning learn representations such that the global OT coupling between a pair of data marginals in the representation space, concentrates on the positive pairs. This is in contrast to previous methods that primarily focused on pairwise matching. However, these methods $\textit{DO NOT}$ utilize negative pairs and hence are not truly contrastive in their approach. We show that this leads to issues of dimensional collapse and hence de...

---

### 43. Weighted Spline-Expanded Networks with Distributional Balancing for Continuous Treatment Effects

**Authors:** Shucheng Liu, Chan Park, Guanhua Chen

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33740v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33740v1)

**Summary:** Estimating causal effects with continuous treatments in observational studies is challenging due to confounding, model misspecification, and high-dimensional covariates. We propose the Weighted Spline-Expanded Network (WSENet), an end-to-end neural framework that addresses these challenges by combining covariate balancing, structured treatment embedding, and bias-corrected outcome estimation. WSENet first applies Distance Covariate Optimal Weights to induce distributional independence between co...

---

### 44. A Statistical Perspective on Knowledge Distillation: Foundations, Classical Methods, and Large Language Model Extensions

**Authors:** Luyang Fang, Haoran Lu, Jiazhang Cai, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33727v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33727v1)

**Summary:** Knowledge Distillation (KD) has emerged as a vital paradigm for transferring the capabilities of high-capacity models to efficient ``student'' counterparts, addressing critical challenges in computational cost, deployment constraints, and privacy-sensitive settings. Although KD is widely used in practice, it is often viewed primarily as an engineering technique, with a unified statistical perspective remaining less developed. This review bridges that gap by presenting a unified Bayesian formulat...

---

### 45. Reliable Replay through Spatial Coherence in Online Continual Learning

**Authors:** Haixiang Sun, Jiefu Zhang, Yinghao He, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33725v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33725v1)

**Summary:** Continually adapting models to new tasks requires retaining earlier knowledge under limited memory and computation. Experience replay addresses this challenge, but priorities based on individual loss increases overlook how related memories respond to the same update and can overemphasize isolated responses. We introduce SPatial coHErent risk control for REplay (SPHERE), a general replay-allocation method applicable across a broad range of learning settings. SPHERE uses a representation kernel to...

---

### 46. Benign Overfitting for General Norms and Distributions

**Authors:** Daniel Barzilai, Ohad Shamir

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33675v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33675v1)

**Summary:** Understanding why predictors can generalize despite interpolating noisy training data is a central puzzle in machine learning. Most work on such "benign overfitting" studies minimum-2-norm linear regression, reflecting the inductive bias of gradient descent. However, modern optimizers such as Adam and Muon use non-Euclidean update geometries, favoring solutions associated with other norms. Analyzing regression for non-Euclidean norms is substantially more difficult, with known results essentiall...

---

### 47. Quantifying Behavioral Tails in Black-Box Language Models

**Authors:** Elsayed Eshra, Ali Al-Lawati, Dongwon Lee, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33638v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33638v1)

**Summary:** We introduce RareTrap, a framework for estimating the probability of severe behaviors in black box large language models (LLMs). A key challenge for probability estimation is defining a tractable distribution over the input space. To accomplish that, RareTrap uses a surrogate LLM and constructs a geometry-aware mapping from a lower-dimensional latent reference space into its token-embedding space to induce an explicit and reproducible distribution over input prompts. A response-level performance...

---

### 48. Correct then Forecast: Observer State-Space Models for Time Series Forecasting

**Authors:** Alexis-Raja Brachet, Guillaume Clavier--Frémond, Abdelhakim Ziani, et al.

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33566v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33566v1)

**Summary:** Time series forecasting requires extrapolating the dynamics of an observed process beyond the last available measurement. Yet recurrent forecasting models typically treat observations as inputs that directly control their latent dynamics. It leads to a regime change when these observations become unavailable at prediction time. Following a state-estimation perspective, we introduce Observer State-Space Models (OSSMs), a class of recurrent models that interprets the observed input time series as ...

---

### 49. Sparsity by Default: The Theory and Practice of ARD in Gaussian Process Regression for Variable Selection

**Authors:** Jia Cai

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33550v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33550v1)

**Summary:** Automatic relevance determination (ARD) is the standard device for input selection in Gaussian process (GP) regression. By giving the covariance kernel a separate lengthscale for every input and learning those lengthscales by maximizing the marginal likelihood, ARD lets the data decide which coordinates matter: irrelevant inputs receive very large lengthscales and are effectively switched off. We trace this mechanism to the Bayesian Occam's razor embodied in the marginal likelihood, derive the g...

---

### 50. Calibrated Derivative-Process Sensitivity for Gaussian-Process Variable Selection

**Authors:** Jia Cai

**Published:** 2026-09-27

🔗 [Paper](http://arxiv.org/abs/2609.33549v1) | 📄 [PDF](https://arxiv.org/pdf/2609.33549v1)

**Summary:** Automatic relevance determination (ARD), the default tool for variable selection in Gaussian-process (GP) regression, ranks inputs by inverse lengthscales -- which measure how fast a function varies, not how much an input contributes to prediction -- and offers no calibrated rule for deciding which inputs to keep. The prediction-centred alternative, the derivative sensitivity $ν_j = \mathbb{E}[(\partial f/\partial x_j)^2]$, is available in closed form from a fitted GP, but turning it into a sele...

---

