# arXiv Daily Digest - 2026-05-11

Total papers: 350

---

## cs.AI

**50 papers**

### 1. EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction

**Authors:** Wei Yu, Yunhang Qian

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08073v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08073v1)

**Summary:** Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual ...

---

### 2. VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection

**Authors:** James Petullo, Sonny George, Dylan Cashman, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08070v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08070v1)

**Summary:** A standard technique for scaling inference-time reasoning is Self-Consistency, whereby multiple candidate answers are sampled from an LLM and the most common answer is selected. More recently, it has been shown that weighted majority voting (e.g. Confidence-Informed Self Consistency (CISC)), which assigns a confidence value to each candidate answer and chooses the answer with the largest accumulated score, tends to be more accurate on a wide range of popular benchmarks. In practice, weighted maj...

---

### 3. Flow-OPD: On-Policy Distillation for Flow Matching Models

**Authors:** Zhen Fang, Wenxuan Huang, Yu Zeng, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08063v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08063v1)

**Summary:** Existing Flow Matching (FM) text-to-image models suffer from two critical bottlenecks under multi-task alignment: the reward sparsity induced by scalar-valued rewards, and the gradient interference arising from jointly optimizing heterogeneous objectives, which together give rise to a 'seesaw effect' of competing metrics and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in the large language model community, we propose Flow-OPD, the first unified post-training...

---

### 4. Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning

**Authors:** Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08061v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08061v1)

**Summary:** We argue that decomposing reward into weighted, verifiable criteria and using an LLM judge to score them provides a partial-credit optimization signal: instead of a binary outcome or a single holistic score, each response is graded along multiple task-specific criteria. We formalize \emph{rubric-grounded reinforcement learning (RL)}: a framework in which the policy is optimized against a structured, multi-criterion reward produced by a frozen LLM judge that conditions on auxiliary grounding the ...

---

### 5. The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents

**Authors:** Jiayuan Liu, Tianqin Li, Shiyi Du, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08060v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08060v1)

**Summary:** Context window expansion is often treated as a straightforward capability upgrade for LLMs, but we find it systematically fails in multi-agent social dilemmas. Across 7 LLMs and 4 games over 500 rounds, expanding accessible history degrades cooperation in 18 of 28 model--game settings, a pattern we term the memory curse. We isolate the underlying mechanism through three analyses. First, lexical analysis of 378,000 reasoning traces associates this breakdown with eroding forward-looking intent rat...

---

### 6. CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation

**Authors:** James Petullo, Nianwen Xue

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08057v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08057v1)

**Summary:** While recent advancements in inference-time learning have improved LLM reasoning on Text-to-SQL tasks, current solutions still struggle to perform well on the most challenging tasks in the Bird-Bench (BIRD) benchmark. This is due to inadequate solution space exploration, which is necessary to uncover promising candidate queries that can be further refined to produce the correct output. To address this challenge, we introduce CA-SQL, a novel Text-to-SQL pipeline that utilizes the estimated diffic...

---

### 7. Fast Byte Latent Transformer

**Authors:** Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08044v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08044v1)

**Summary:** Recent byte-level language models (LMs) match the performance of token-level models without relying on subword vocabularies, yet their utility is limited by slow, byte-by-byte autoregressive generation. We address this bottleneck in the Byte Latent Transformer (BLT) through new training and generation techniques. First, we introduce BLT Diffusion (BLT-D), a new model and our fastest BLT variant, trained with an auxiliary block-wise diffusion objective alongside the standard next-byte prediction ...

---

### 8. SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation

**Authors:** Tianfei Ren, Zhipeng Yan, Yiming Zhao, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08043v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08043v1)

**Summary:** While text-to-image models have made strong progress in visual fidelity, faithfully realizing complex visual intents remains challenging because many requirements must be tracked across grounding, generation, and verification. We refer to these requirements as semantic commitments and formalize their lifecycle discontinuity as the Conceptual Rift, where commitments may be locally resolved or checked but fail to remain identifiable as the same operational units throughout the generation lifecycle...

---

### 9. Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph

**Authors:** Ning Liu, Chuanneng Sun, Kristina Klinkner, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08037v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08037v1)

**Summary:** Direct Preference Optimization (DPO) aligns language models using pairwise preference comparisons, offering a simple and effective alternative to Reinforcement Learning (RL) from human feedback. However, in many practical settings, training data consists of multiple rollouts per prompt, inducing rich preference structure that pairwise DPO fails to exploit. Collapsing such data into independent pairs discards transitivity, introduces redundant or conflicting supervision, and can lead to unstable ...

---

### 10. MPD$^2$-Router: Mask-aware Multi-expert Prior-regularized Dual-head Deferral Router in Glaucoma Screening and Diagnosis

**Authors:** Wenxin Zhan

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08024v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08024v1)

**Summary:** Learning-to-defer (L2D) can make glaucoma screening safer by routing difficult/uncertain cases to humans, yet standard formulations overlook expert availability, heterogeneous readers behavior, workload imbalance, asymmetric diagnostic harm, case difficulty from morphology and deployment shift. We introduce MPD$^2$-Router, a mask-aware multi-expert deferral framework that recasts ophthalmic triage as constrained human--AI routing: whether to defer and to which available expert. It couples a dual...

---

### 11. Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction

**Authors:** Himanshu Udupi, Xiaocong Yang, ChengXiang Zhai

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08022v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08022v1)

**Summary:** Spiking Neural Networks (SNNs) have been proposed as biologically plausible and energy-efficient alternatives to conventional Artificial Neural Networks (ANNs). However, the training of SNN usually relies on surrogate gradients due to the non-differentiability of the spike function, introducing approximation errors that accumulate across layers. To address this challenge, we extend the work on convexification of parallel feedforward threshold networks to parallel recurrent threshold networks, wh...

---

### 12. Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners

**Authors:** Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08019v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08019v1)

**Summary:** Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match hu...

---

### 13. Learning CLI Agents with Structured Action Credit under Selective Observation

**Authors:** Haoyang Su, Ying Wen

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08013v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08013v1)

**Summary:** Command line interface (CLI) agents are emerging as a practical paradigm for agent-computer interaction over evolving filesystems, executable command line programs, and online execution feedback. Recent work has used reinforcement learning (RL) to learn these interaction abilities from verifiable task feedback, yet few methods exploit the native structured attributes of CLI actions as learning signals. Beyond this underused action structure, CLI learning also couples two bottlenecks for coding a...

---

### 14. Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims

**Authors:** Zezheng Lin, Fengming Liu

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08012v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08012v1)

**Summary:** Mechanistic interpretability papers increasingly use causal vocabulary: circuits, mediators, causal abstraction, monosemanticity. Such claims require explicit identification assumptions. A purposive audit of 10 papers across four methodological strands finds no dedicated identification-assumptions section and a recurring pattern: validation metrics such as faithfulness, completeness, monosemanticity, alignment, or ablation effects are reported as causal support without stating the assumptions th...

---

### 15. Abductive Reasoning with Probabilistic Commonsense

**Authors:** Joseph Cotnareanu, Chiara Roverato, Han Zhou, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08011v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08011v1)

**Summary:** Recent efforts to improve the reasoning abilities of Large Language Models (LLMs) have focused on integrating formal logic solvers within neurosymbolic frameworks. A key challenge is that formal solvers lack commonsense world knowledge, preventing them from making reasoning steps that humans find obvious. Prior methods address this by using LLMs to supply missing commonsense assumptions, but these approaches implicitly assume universal agreement on such commonsense facts. In reality, commonsense...

---

### 16. Graph-Structured Hyperdimensional Computing for Data-Efficient and Explainable Process-Structure-Property Prediction

**Authors:** Jingzhan Ge, Ajeeth Vellore, Ajinkya Palwe, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07999v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07999v1)

**Summary:** Multiphoton photoreduction enables high-fidelity fabrication of complex 3D microstructures, yet reliable process-structure-property (PSP) prediction remains difficult because the available data are sparse, heterogeneous, and interaction-dominated. In this regime, conventional feature-vector models are statistically underdetermined, making them prone to spurious correlations, poor regime transfer, and unstable post hoc explanations, whereas mechanistic pipelines depend on calibrated submodels tha...

---

### 17. Tool Calling is Linearly Readable and Steerable in Language Models

**Authors:** Zekun Wu, Ze Wang, Seonglae Cho, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07990v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07990v1)

**Summary:** When a tool-calling agent picks the wrong tool, the failure is invisible until execution: the email gets sent, the meeting gets missed. Probing 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B), we find the identity of the chosen tool is linearly readable and steerable inside the model. Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-10...

---

### 18. Towards Apples to Apples for AI Evaluations: From Real-World Use Cases to Evaluation Scenarios

**Authors:** Yee-Yin Choong, Kristen Greene, Alice Qian, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07986v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07986v1)

**Summary:** AI measurement science has a wide variety of methodologies and measurements for comparing AI systems, resulting in what often appear to be "apples-to-oranges" comparisons across AI evaluations. To move toward "apples-to-apples" comparisons in real-world AI evaluations, this work advocates for methodological transparency in evaluation scenarios, operational grounding, and human-centered design (HCD) principles. We propose a repeatable process for transforming high-level use cases to detailed scen...

---

### 19. Dooly: Configuration-Agnostic, Redundancy-Aware Profiling for LLM Inference Simulation

**Authors:** Joon Ha Kim, Geon-Woo Kim, Anoop Rachakonda, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07985v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07985v1)

**Summary:** Selecting the optimal LLM inference configuration requires evaluation across hardware, serving engines, attention backends, and model architectures, since no single choice performs best across all workloads. Profile-based simulators are the standard tool, yet they hardcode their operation set to a specific configuration and re-profile every operation from scratch, making exploration prohibitively expensive. This cost stems from a missing structural understanding: every input dimension of each op...

---

### 20. Where's the Plan? Locating Latent Planning in Language Models with Lightweight Mechanistic Interventions

**Authors:** Nicole Ma, Nick Rui

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07984v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07984v1)

**Summary:** We study planning site formation in language models -- where internal representations of structurally-constrained future tokens form during the forward pass, and whether they causally drive generation. Using rhyming-couplet completion as a clean test of forward-looking constraint, we apply two lightweight methods (linear probing and activation patching) across Qwen3, Gemma-3, and Llama-3 at more than ten scales. Probing shows that future-rhyme information is linearly decodable at the line bounda...

---

### 21. The Limits of AI-Driven Allocation: Optimal Screening under Aleatoric Uncertainty

**Authors:** Santiago Cortes-Gomez, Mateo Dulce Rubio, Carlos Patino, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07979v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07979v1)

**Summary:** The rise of machine learning has shifted targeted resource allocation in policy and humanitarian settings toward algorithmic targeting based on predicted risk scores. This approach is typically cheaper and faster than traditional screening procedures that directly observe the latent vulnerability status through physical verification. Yet, even access to the true conditional vulnerability probability cannot eliminate misallocation: aleatoric uncertainty over individual vulnerability status is irr...

---

### 22. It Just Takes Two: Scaling Amortized Inference to Large Sets

**Authors:** Antoine Wehenkel, Michael Kagan, Lukas Heinrich, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07972v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07972v1)

**Summary:** Neural posterior estimation has emerged as a powerful tool for amortized inference, with growing adoption across scientific and applied domains. In many of these applications, the conditioning variable is a set of observations whose elements depend not only on the target but also on unknown factors shared across the set. Optimal inference therefore requires treating the set jointly, which in turn requires training the estimator at the deployment set size -- a regime where memory and compute quic...

---

### 23. TimeLesSeg: Unified Contrast-Agnostic Cross-Sectional and Longitudinal MS Lesion Segmentation via a Stochastic Generative Model

**Authors:** Vicent Caselles-Ballester, Eloy Martínez-Heras, Giuseppe Pontillo, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07955v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07955v1)

**Summary:** Multiple sclerosis (MS) expresses substantial clinical and radiological heterogeneity, which poses significant challenges for automatic lesion segmentation. The current deep learning-based SOTA is highly susceptible to changes in both distribution, e.g., changes in scanner; as well as the structure of inputs, evident in the current divide between cross-sectional and longitudinal approaches. We introduce TimeLesSeg, a unified contrast-agnostic framework designed to segment MS lesions regardless o...

---

### 24. Exploring the non-convexity in machine learning using quantum-inspired optimization

**Authors:** Kandula Eswara Sai Kumar, Parth Dhananjay Danve, Abhishek Chopra, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07947v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07947v1)

**Summary:** The escalating complexity of modern machine learning necessitates solving challenging non-convex optimization problems, particularly in high-dimensional regimes and scenarios contaminated by gross outliers. Traditional approaches, relying on convex relaxations or specialized local search heuristics, frequently succumb to suboptimal local minima and fail to recover the true underlying discrete structures. In this paper, we propose treating these non-convex challenges as a global search problem an...

---

### 25. TAVIS: A Benchmark for Egocentric Active Vision and Anticipatory Gaze in Imitation Learning

**Authors:** Giacomo Spigler

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07943v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07943v1)

**Summary:** Active vision -- where a policy controls its own gaze during manipulation -- has emerged as a key capability for imitation learning, with multiple independent systems demonstrating its benefits in the past year. Yet there is no shared benchmark to compare approaches or quantify what active vision contributes, on which task types, and under what conditions. We introduce TAVIS, evaluation infrastructure for active-vision imitation learning, with two complementary task suites -- TAVIS-Head (5 tasks...

---

### 26. TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples

**Authors:** Shuren Xia, Qiwei Li, Taqiya Ehsan, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07935v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07935v1)

**Summary:** We present TraceFix, a verification-first pipeline for Large Language Model (LLM) multi-agent coordination. An agent synthesizes a protocol topology as a structured intermediate representation (IR) from a task description, generates PlusCal coordination logic, and iteratively repairs the protocol using counterexamples from the TLA+ model checker (TLC) until verification succeeds. Verified process bodies are compiled into per-agent system prompts and executed under a runtime monitor that rejects ...

---

### 27. One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy

**Authors:** Zuojin Tang, Shengchao Yuan, Xiaoxin Bai, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07931v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07931v1)

**Summary:** Vision-language-action (VLA) models increasingly rely on auxiliary world modules to plan over long horizons, yet how such modules should be parameterized on top of a pretrained VLA remains an open design question. Existing world-model-augmented VLAs typically pass the per-frame visual stream into the world module at high visual bandwidth and treat its rollout as a side product of action prediction; under a constrained adaptation budget on a frozen backbone, this leaves both the per-frame represe...

---

### 28. INO-SGD: Addressing Utility Imbalance under Individualized Differential Privacy

**Authors:** Xiao Tian, Jue Fan, Rachael Hwee Ling Sim, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07930v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07930v1)

**Summary:** Differential privacy (DP) is widely employed in machine learning to protect confidential or sensitive training data from being revealed. As data owners gain greater control over their data due to personal data ownership, they are more likely to set their own privacy requirements, necessitating individualized DP (IDP) to fulfil such requests. In particular, owners of data from more sensitive subsets, such as positive cases of stigmatized diseases, likely set stronger privacy requirements, as leak...

---

### 29. AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents

**Authors:** Zhengkang Guo, Yiyang Li, Lin Qiu, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07926v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07926v1)

**Summary:** As LLM-based agents increasingly rely on external tools, it is important to evaluate their ability to sustain tool-grounded reasoning beyond familiar workflows and short-range interactions. We introduce AgentEscapeBench, an escape-room-style benchmark that tests whether agents can infer, execute, and revise novel tool-use procedures under explicit long-range dependency constraints. Each task defines a directed acyclic dependency graph over tools and items, requiring agents to invoke real externa...

---

### 30. Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation

**Authors:** Amin Karimi Monsefi, Dominic Culver, Nikhil Bhendawade, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07924v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07924v1)

**Summary:** Discrete flow matching generates text by iteratively transforming noise tokens into coherent language, but may require hundreds of forward passes. Distillation uses the multi-step trajectory to train a student to reproduce the process in a few steps. When the student underperforms, the usual explanation is insufficient capacity. We argue the opposite: the trajectory is the bottleneck, not the student. Each training trajectory is built through a chain of blind stochastic jumps with no evaluation ...

---

### 31. Sycophantic AI makes human interaction feel more effortful and less satisfying over time

**Authors:** Lujain Ibrahim, Franziska Sofia Hafner, Myra Cheng, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07912v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07912v1)

**Summary:** Millions of people now turn to artificial intelligence (AI) systems for personal advice, guidance, and support. Such systems can be sycophantic, frequently affirming users' views and beliefs. Across five preregistered studies (N = 3,075 participants, 12,766 human-AI conversations), including a three-week study with a census-representative U.S. sample, we provide longitudinal experimental evidence that sycophantic AI shifts how users approach their closest relationships. We show that sycophantic ...

---

### 32. Statistical inference with belief functions: A survey

**Authors:** Fabio Cuzzolin

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07908v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07908v1)

**Summary:** Belief functions are a powerful and popular framework for the mathematical characterisation of uncertainty, in particular in situations in which lack of data renders learning a probability distribution for the problem impractical. The first step in a reasoning chain based on belief functions is inference: how to learn a belief measure from the available data. In this survey we focus, in particular, on making inference from statistical data, and review the most significant contributions in the ar...

---

### 33. CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers

**Authors:** Hexuan Deng, Xiaopeng Ke, Yichen Li, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07905v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07905v1)

**Summary:** Despite the rapid development of AI reviewers, evaluating such systems remains challenging: metrics favor overlap with human reviews over correctness. However, since human reviews often cover only a subset of salient issues and sometimes contain mistakes, they are unreliable as gold references. To address this, we build category-specific benchmark subsets and skip evaluation when the corresponding human reviews are missing to strengthen Completeness. We also leverage reviewer--author--meta-revie...

---

### 34. BeeVe: Unsupervised Acoustic State Discovery in Honey Bee Buzzing

**Authors:** Hamze Hammami, Nidhal Abdulaziz

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07903v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07903v1)

**Summary:** Discovering structure in biological signals without supervision is a fundamental problem in computational intelligence, yet existing bioacoustic methods assume vocal production models or predefined semantic units, leaving non-vocal species poorly served. This work introduces BeeVe, an unsupervised framework for acoustic state discovery in collective honey bee buzzing. BeeVe uses the self-supervised Patchout Spectrogram Transformer (PaSST) as a frozen feature extractor, then trains a Vector-Quant...

---

### 35. Semantic-Aware Adaptive Visual Memory for Streaming Video Understanding

**Authors:** Hang Wu, Sherin Mary Mathews, Yujun Cai, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07897v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07897v1)

**Summary:** Online streaming video understanding requires models to process continuous visual inputs and respond to user queries in real time, where the unbounded stream and unpredictable query timing turn memory management into a central challenge. Existing methods typically compress visual tokens via visual similarity heuristics, or augment compression with KV-cache-level retrieval. However, compression decisions rarely incorporate semantic signals, and retrieval is often added after compression is finali...

---

### 36. What if AI systems weren't chatbots?

**Authors:** Sourojit Ghosh, Pranav Narayanan Venkit, Sanjana Gautam, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07896v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07896v1)

**Summary:** The rapid convergence of artificial intelligence (AI) toward conversational chatbot interfaces marks a critical moment for the industry. This paper argues that the chatbot paradigm is not a neutral interface choice, but a dominant sociotechnical configuration whose widespread adoption reshapes social, economic, legal, and environmental systems. We examine how treating AI primarily as conversational assistants has extensive structural downsides. We show how chatbot-based systems often fail to ade...

---

### 37. Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models

**Authors:** Yuancheng Wei, Linli Yao, Lei Li, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07872v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07872v1)

**Summary:** Multimodal reward models have advanced substantially in text and image domains, yet progress in video understanding reward modeling remains severely limited by the lack of robust evaluation benchmarks and high-quality preference data. To address this, we propose a unified framework spanning benchmark design, data construction, and reward model training. We introduce Video Understanding Reward Bench (VURB), a benchmark featuring 2,100 preference pairs with long chain-of-thought reasoning traces (...

---

### 38. Spectral Dynamics in Deep Networks: Feature Learning, Outlier Escape, and Learning Rate Transfer

**Authors:** Clarissa Lauditi, Cengiz Pehlevan, Blake Bordelon

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07870v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07870v1)

**Summary:** We study the evolution of hidden-weight spectra in wide neural networks trained by (stochastic) gradient descent. We develop a two-level dynamical mean-field theory (DMFT) that jointly tracks bulk and outlier spectral dynamics for spiked ensembles whose spike directions remain statistically dependent on the random bulk. We apply this framework to two settings: (1) infinite-width nonlinear networks in mean-field/$μ$P scaling and (2) deep linear networks in the proportional high-dimensional limit,...

---

### 39. KL for a KL: On-Policy Distillation with Control Variate Baseline

**Authors:** Minjae Oh, Sangjun Song, Gyubin Choi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07865v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07865v1)

**Summary:** On-Policy Distillation (OPD) has emerged as a dominant post-training paradigm for large language models, especially for reasoning domains. However, OPD remains unstable in practice due to the high gradient variance of its single-sample Monte Carlo estimator, and recipes for stable training are still immature. We propose vOPD (On-Policy Distillation with a control variate baseline), which casts OPD as policy-gradient RL and stabilizes it by introducing a control variate baseline-canonically a val...

---

### 40. On the Tradeoffs of On-Device Generative Models in Federated Predictive Maintenance Systems

**Authors:** Usevalad Milasheuski, Piero Baraldi, Enrico Zio, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07860v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07860v1)

**Summary:** Federated Learning (FL) has emerged as a promising paradigm for preserving client data ownership and control over distributed Internet of Things (IoT) environments. While discriminative models dominate most FL use cases, recent advances in generative models -- such as Variational Autoencoders (VAE), Generative Adversarial Networks (GAN), and Diffusion Models (DM) -- offer new opportunities for unsupervised anomaly detection in time series analysis, with relevant applications in predictive mainte...

---

### 41. MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning

**Authors:** Ionut-Vlad Modoranu, Mher Safaryan, Dan Alistarh

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07850v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07850v1)

**Summary:** With the rise in scale for deep learning models to billions of parameters, the computational cost of fine-tuning remains a significant barrier to deployment. While Low-Rank Adaptation (LoRA) has become the standard for parameter-efficient fine-tuning, the need to set a predefined, static rank $r$ requires exhaustive grid searches to balance efficiency and performance. Existing rank-adaptive solutions such as DyLoRA mitigate this by sampling ranks during the training from a predefined distributio...

---

### 42. \mathsf{VISTA}: Decentralized Machine Learning in Adversary Dominated Environments

**Authors:** Hanzaleh Akbari Nodehi, Parsa Moradi, Soheil Mohajer, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07841v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07841v1)

**Summary:** Decentralized machine learning often relies on outsourcing computations, such as gradient evaluations, to untrusted worker nodes. Existing robust aggregation methods can mitigate malicious behavior under honest-majority assumptions, but may fail when adversaries control a majority of the workers. We study this adversary-dominated setting through an incentive-oriented framework in which reports are accepted and rewarded only when they are mutually consistent up to a threshold. This turns the adve...

---

### 43. Exact Regular-Constrained Variable-Order Markov Generation via Sparse Context-State Belief Propagation

**Authors:** François Pachet

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07839v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07839v1)

**Summary:** Variable-order Markov models generate sequences over a finite alphabet by conditioning each symbol on the longest available suffix of the generated history. Regular constraints, by contrast, describe finite-horizon control requirements by an automaton: fixed positions, forced endings, metrical patterns, and forbidden copied fragments are all special cases. Existing exact methods already handle regular constraints with belief propagation for first-order Markov chains. The contribution here is the...

---

### 44. PPI-Net connects molecular protein interactions to functional processes in disease

**Authors:** Kyle Higgins, Guadalupe Gonzalez, Dennis Veselkov, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07838v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07838v1)

**Summary:** Understanding how molecular alterations propagate across biological systems to drive disease remains a central challenge. Although high-throughput profiling enables comprehensive characterization of tumor states, most models neglect structured biological relationships or lack interpretability across scales. Here we present PPI-Net, a hierarchical graph neural network that integrates protein-protein interaction (PPI) networks with pathway-level representations to model disease from molecular inte...

---

### 45. Approximation-Free Differentiable Oblique Decision Trees

**Authors:** Subrat Prasad Panda, Blaise Genest, Arvind Easwaran

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07837v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07837v1)

**Summary:** Decision Trees (DTs) are widely used in safety-critical domains such as medical diagnosis, valued for their interpretability and effectiveness on tabular data. However, training accurate oblique DTs is challenging due to complex optimization landscapes and overfitting risks, particularly in regression. Recent advances have introduced differentiable formulations that enable gradient-based training and joint optimization of decision boundaries and leaf regressors. Yet, existing approaches typicall...

---

### 46. CyBiasBench: Benchmarking Bias in LLM Agents for Cyber-Attack Scenarios

**Authors:** Taein Lim, Seongyong Ju, Munhyeok Kim, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07830v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07830v1)

**Summary:** Large language models (LLMs) are increasingly deployed as autonomous agents in offensive cybersecurity. In this paper, we reveal an interesting phenomenon: different agents exhibit distinct attack patterns. Specifically, each agent exhibits an attack-selection bias, disproportionately concentrating its efforts on a narrow subset of attack families regardless of prompt variations. To systematically quantify this behavior, we introduce CyBiasBench, a comprehensive 630-session benchmark that evalua...

---

### 47. Divide and Conquer: Object Co-occurrence Helps Mitigate Simplicity Bias in OOD Detection

**Authors:** Boyang Dai, Chaoqi Chen, Yizhou Yu

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07821v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07821v1)

**Summary:** Out-of-distribution (OOD) detection is crucial for ensuring the reliability of deep learning models. Existing methods mostly focus on regular entangled representations to discriminate in-distribution (ID) and OOD data, neglecting the rich contextual information within images. This issue is particularly challenging for detecting near-OOD, as models with simplicity bias struggle to learn discriminative features in disentangled representations. The human visual system can use the co-occurrence of o...

---

### 48. GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning

**Authors:** Brown Ebouky, Gabriele Carrino, Niccolo Avogaro, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07817v1)

**Summary:** Human visual reasoning is governed by active vision, a process where metacognitive control drives top-down goal-directed attention, dynamically routing foveal focus toward task-relevant details while maintaining peripheral awareness of the global scene. In contrast, modern Vision-Language Models (VLMs) process visual information passively, relying on the static accumulation of massive token contexts that dilute spatial reasoning and induce linguistic hallucinations. Here we propose the following...

---

### 49. Text-to-CAD Evaluation with CADTests

**Authors:** Dimitrios Mallis, Marco Wang, Ahmet Serdar Karadeniz, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07807v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07807v1)

**Summary:** Text-to-CAD has recently emerged as an important task with the potential to substantially accelerate design workflows. Despite its significance, there has been surprisingly little work on Text-to-CAD evaluation, and assessing CAD model generation performance remains a considerable challenge. In this work, we introduce a new evaluation perspective for Text-to-CAD based on automated testing. We propose CADTestBench, the first test-based benchmark for Text-to-CAD, based on CADTests, executable soft...

---

### 50. Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs

**Authors:** Sree Bhattacharyya, Samarth Khanna, Leona Chen, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07806v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07806v1)

**Summary:** Large Language Models (LLMs) are increasingly used in settings where reliable self-assessment is critical. Assessing model reliability has evolved from using probabilistic correctness estimates to, more recently, eliciting verbalized confidence. Confidence, however, has been shown to be an inconsistent and overoptimistic predictor of model correctness. Drawing on cognitive appraisal theory, a framework from human psychology that decomposes self-evaluation into multiple components, we propose a m...

---

## cs.CL

**50 papers**

### 1. LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling

**Authors:** Tong Zheng, Haolin Liu, Chengsong Huang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08083v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08083v1)

**Summary:** Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments wh...

---

### 2. Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration

**Authors:** Shuhang Lin, Chuhao Zhou, Xiao Lin, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08077v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08077v1)

**Summary:** Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction...

---

### 3. The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents

**Authors:** Jiayuan Liu, Tianqin Li, Shiyi Du, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08060v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08060v1)

**Summary:** Context window expansion is often treated as a straightforward capability upgrade for LLMs, but we find it systematically fails in multi-agent social dilemmas. Across 7 LLMs and 4 games over 500 rounds, expanding accessible history degrades cooperation in 18 of 28 model--game settings, a pattern we term the memory curse. We isolate the underlying mechanism through three analyses. First, lexical analysis of 378,000 reasoning traces associates this breakdown with eroding forward-looking intent rat...

---

### 4. CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation

**Authors:** James Petullo, Nianwen Xue

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08057v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08057v1)

**Summary:** While recent advancements in inference-time learning have improved LLM reasoning on Text-to-SQL tasks, current solutions still struggle to perform well on the most challenging tasks in the Bird-Bench (BIRD) benchmark. This is due to inadequate solution space exploration, which is necessary to uncover promising candidate queries that can be further refined to produce the correct output. To address this challenge, we introduce CA-SQL, a novel Text-to-SQL pipeline that utilizes the estimated diffic...

---

### 5. Accurate and Efficient Statistical Testing for Word Semantic Breadth

**Authors:** Yo Ehara

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08048v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08048v1)

**Summary:** Measuring the breadth of a word's meaning, or its spread across contexts, has become feasible with contextualized token embeddings. A word type can be represented as a cloud of token vectors, with dispersion-based statistics serving as proxies for contextual diversity (Nagata and Tanaka-Ishii, ACL2025). These measurements are useful for deciding appropriate sense distinctions when constructing thesauri and domain-specific dictionaries. However, when comparing the breadth of two word types, naive...

---

### 6. Uncertainty-Aware Structured Data Extraction from Full CMR Reports via Distilled LLMs

**Authors:** Yi Yu, Parker Martin, Zhenyu Bu, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08045v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08045v1)

**Summary:** Converting free-text cardiac magnetic resonance (CMR) reports into auditable structured data remains a bottleneck for cohort assembly, longitudinal curation, and clinical decision support. We present CMR-EXTR, a lightweight framework that converts free-text CMR reports into structured data and assigns per-field confidence for quality control. A teacher-student distillation pipeline enables fully offline inference while limiting manual annotation. Uncertainty integrates three complementary princi...

---

### 7. Fast Byte Latent Transformer

**Authors:** Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08044v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08044v1)

**Summary:** Recent byte-level language models (LMs) match the performance of token-level models without relying on subword vocabularies, yet their utility is limited by slow, byte-by-byte autoregressive generation. We address this bottleneck in the Byte Latent Transformer (BLT) through new training and generation techniques. First, we introduce BLT Diffusion (BLT-D), a new model and our fastest BLT variant, trained with an auxiliary block-wise diffusion objective alongside the standard next-byte prediction ...

---

### 8. Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims

**Authors:** Zezheng Lin, Fengming Liu

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08012v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08012v1)

**Summary:** Mechanistic interpretability papers increasingly use causal vocabulary: circuits, mediators, causal abstraction, monosemanticity. Such claims require explicit identification assumptions. A purposive audit of 10 papers across four methodological strands finds no dedicated identification-assumptions section and a recurring pattern: validation metrics such as faithfulness, completeness, monosemanticity, alignment, or ablation effects are reported as causal support without stating the assumptions th...

---

### 9. Tool Calling is Linearly Readable and Steerable in Language Models

**Authors:** Zekun Wu, Ze Wang, Seonglae Cho, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07990v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07990v1)

**Summary:** When a tool-calling agent picks the wrong tool, the failure is invisible until execution: the email gets sent, the meeting gets missed. Probing 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B), we find the identity of the chosen tool is linearly readable and steerable inside the model. Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-10...

---

### 10. GLiGuard: Schema-Conditioned Classification for LLM Safeguard

**Authors:** Urchade Zaratiana, Mary Newhauser, George Hurn-Maloney, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07982v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07982v1)

**Summary:** Ensuring safe, policy-compliant outputs from large language models requires real-time content moderation that can scale across multiple safety dimensions. However, state-of-the-art guardrail models rely on autoregressive decoders with 7B--27B parameters, reformulating what is fundamentally a classification problem as sequential text generation, a design choice that incurs high latency and scales poorly to multi-aspect evaluation. In this work, we introduce \textbf{GLiGuard}, a 0.3B-parameter sch...

---

### 11. Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?

**Authors:** Anmol Gulati, Hariom Gupta, Elias Lumer, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07937v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07937v1)

**Summary:** Long-horizon AI agents execute complex workflows spanning hundreds of sequential actions, yet a single wrong assumption early on can cascade into irreversible errors. When instructions are incomplete, the agent must decide not only whether to ask for clarification but when, and no prior work measures how clarification value changes over the course of execution. We introduce a forced-injection framework that provides ground-truth clarifications at controlled points in the agent's trajectory acros...

---

### 12. How to Train Your Latent Diffusion Language Model Jointly With the Latent Space

**Authors:** Viacheslav Meshchaninov, Alexander Shabalin, Egor Chimbulatov, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07933v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07933v1)

**Summary:** Latent diffusion models offer an attractive alternative to discrete diffusion for non-autoregressive text generation by operating on continuous text representations and denoising entire sequences in parallel. The major challenge in latent diffusion modeling is constructing a suitable latent space. In this work, we present the Latent Diffusion Language Model (LDLM), in which the latent encoder, diffusion model, and decoder are trained jointly. LDLM builds its latent space by reshaping the represe...

---

### 13. How Value Induction Reshapes LLM Behaviour

**Authors:** Arnav Arora, Natalie Schluter, Katherine Metcalf, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07925v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07925v1)

**Summary:** Conversational Large Language Models are post-trained on language that expresses specific behavioural traits, such as curiosity, open-mindedness, and empathy, and values, such as helpfulness, harmlessness, and honesty. This is done to increase utility, ensure safety, and improve the experience of the people interacting with the model. However, values are complex and inter-related -- inducing one could modify behaviour on another. Further, inducing certain values can make models more addictive or...

---

### 14. Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation

**Authors:** Amin Karimi Monsefi, Dominic Culver, Nikhil Bhendawade, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07924v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07924v1)

**Summary:** Discrete flow matching generates text by iteratively transforming noise tokens into coherent language, but may require hundreds of forward passes. Distillation uses the multi-step trajectory to train a student to reproduce the process in a few steps. When the student underperforms, the usual explanation is insufficient capacity. We argue the opposite: the trajectory is the bottleneck, not the student. Each training trajectory is built through a chain of blind stochastic jumps with no evaluation ...

---

### 15. CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers

**Authors:** Hexuan Deng, Xiaopeng Ke, Yichen Li, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07905v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07905v1)

**Summary:** Despite the rapid development of AI reviewers, evaluating such systems remains challenging: metrics favor overlap with human reviews over correctness. However, since human reviews often cover only a subset of salient issues and sometimes contain mistakes, they are unreliable as gold references. To address this, we build category-specific benchmark subsets and skip evaluation when the corresponding human reviews are missing to strengthen Completeness. We also leverage reviewer--author--meta-revie...

---

### 16. Beyond "I cannot fulfill this request": Alleviating Rigid Rejection in LLMs via Label Enhancement

**Authors:** Ying Zhang, Congyu Qiao, Xin Geng, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07883v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07883v1)

**Summary:** Large Language Models (LLMs) rely on safety alignment to obey safe requests while refusing harmful ones. However, traditional refusal mechanisms often lead to "rigid rejection," where a general template (e.g., "I cannot fulfill this request") indiscriminately triggers refusals and severely undermines the naturalness of interactions between humans and LLMs. To address this issue, LANCE is proposed in this paper to ensure safe yet flexible and natural responses via label enhancement. Specifically,...

---

### 17. KL for a KL: On-Policy Distillation with Control Variate Baseline

**Authors:** Minjae Oh, Sangjun Song, Gyubin Choi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07865v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07865v1)

**Summary:** On-Policy Distillation (OPD) has emerged as a dominant post-training paradigm for large language models, especially for reasoning domains. However, OPD remains unstable in practice due to the high gradient variance of its single-sample Monte Carlo estimator, and recipes for stable training are still immature. We propose vOPD (On-Policy Distillation with a control variate baseline), which casts OPD as policy-gradient RL and stabilizes it by introducing a control variate baseline-canonically a val...

---

### 18. MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning

**Authors:** Ionut-Vlad Modoranu, Mher Safaryan, Dan Alistarh

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07850v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07850v1)

**Summary:** With the rise in scale for deep learning models to billions of parameters, the computational cost of fine-tuning remains a significant barrier to deployment. While Low-Rank Adaptation (LoRA) has become the standard for parameter-efficient fine-tuning, the need to set a predefined, static rank $r$ requires exhaustive grid searches to balance efficiency and performance. Existing rank-adaptive solutions such as DyLoRA mitigate this by sampling ranks during the training from a predefined distributio...

---

### 19. Measuring and Mitigating the Distributional Gap Between Real and Simulated User Behaviors

**Authors:** Shuhaib Mehri, Philippe Laban, Sumuk Shashidhar, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07847v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07847v1)

**Summary:** As user simulators are increasingly used for interactive training and evaluation of AI assistants, it is essential that they represent the diverse behaviors of real users. While existing works train user simulators to generate human-like responses, whether they capture the broad and heterogeneous distribution of real user behaviors remains an open question. In this work, we introduce a method to measure the distributional gap between real and simulated user behaviors, validated through a human s...

---

### 20. SCENE: Recognizing Social Norms and Sanctioning in Group Chats

**Authors:** Mateusz Jacniacki, Maksymilian Bilski

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07823v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07823v1)

**Summary:** Online group chats are social spaces with implicit behavior patterns that, when broken, are often met with social sanctioning from the group. The ability and willingness of LLM-based agents to recognize and adapt to these norms remains mostly unexplored. We introduce SCENE, a social-interaction benchmark focused on implicit norms and social sanctioning in multi-party chat. SCENE generates plausible non-roleplay scenarios with scripted personas that follow a hidden norm, create opportunities for ...

---

### 21. GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning

**Authors:** Brown Ebouky, Gabriele Carrino, Niccolo Avogaro, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07817v1)

**Summary:** Human visual reasoning is governed by active vision, a process where metacognitive control drives top-down goal-directed attention, dynamically routing foveal focus toward task-relevant details while maintaining peripheral awareness of the global scene. In contrast, modern Vision-Language Models (VLMs) process visual information passively, relying on the static accumulation of massive token contexts that dilute spatial reasoning and induce linguistic hallucinations. Here we propose the following...

---

### 22. OrScale: Orthogonalised Optimization with Layer-Wise Trust-Ratio Scaling

**Authors:** Yuxuan Lou, Yang You

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07815v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07815v1)

**Summary:** Muon improves neural-network training by orthogonalizing matrix-valued updates, but it leaves each layer's update magnitude controlled mostly by a global learning rate. We introduce OrScale, a trust-ratio extension of Muon built on a simple rule: the denominator of a layer-wise ratio should measure the Frobenius norm of the actual parameter-space direction that will be applied. This yields OrScale for general matrix layers and OrScale-LM for language models, where Moonlight shape scaling is comb...

---

### 23. A Comparative Analysis of Classical Machine Learning and Deep Learning Approaches for Sentiment Classification on IMDb Movie Reviews

**Authors:** Erma Daniar Safitri, Lia Hana Ichisasmita, Citra Agustin, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07811v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07811v1)

**Summary:** This paper presents a comparative study of classical machine learning and deep learning methods for sentiment classification on the IMDb movie reviews dataset. The machine learning pipeline uses TF-IDF features and PyCaret AutoML to evaluate Logistic Regression, Naïve Bayes, and Support Vector Machine, while the deep learning pipeline implements BiLSTM and BiLSTM with an attention mechanism. Experimental results show that classical machine learning, especially SVM, achieves the best performance ...

---

### 24. Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs

**Authors:** Sree Bhattacharyya, Samarth Khanna, Leona Chen, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07806v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07806v1)

**Summary:** Large Language Models (LLMs) are increasingly used in settings where reliable self-assessment is critical. Assessing model reliability has evolved from using probabilistic correctness estimates to, more recently, eliciting verbalized confidence. Confidence, however, has been shown to be an inconsistent and overoptimistic predictor of model correctness. Drawing on cognitive appraisal theory, a framework from human psychology that decomposes self-evaluation into multiple components, we propose a m...

---

### 25. PolySQL: Scaling Text-to-SQL Evaluation Across SQL Dialects via Automated Backend Isomorphism

**Authors:** Yotam Perlitz, Elad Venezian, Corentin Royer, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07796v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07796v1)

**Summary:** SQL dialects vary in syntax, types, and functions across database engines. Text-to-SQL benchmarks, however, predominantly support only SQLite. This creates a critical evaluation gap: cross-dialect evaluation reveals weak per-query agreement (Cohen's ), showing that SQLite performance is an unreliable proxy for other dialects. Yet such evaluation remains prohibitively difficult: existing approaches either require expensive manual query transpilation or rely on tools that often fail on complex SQL...

---

### 26. Hybrid TF--IDF Logistic Regression and MLP Neural Baseline for Indonesian Three-Class Sentiment Analysis on Social Media Text

**Authors:** Allya Nurul Islami Pasha, Eka Fidiya Putri, Luluk Muthoharoh, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07793v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07793v1)

**Summary:** This paper presents a compact three-class sentiment analysis study for Indonesian social media text. The task is formulated with positive, negative, and neutral outputs derived from a fine-grained emotion dataset. The proposed practical baseline combines TF--IDF text features, three lightweight numeric metadata features, and a balanced multinomial Logistic Regression classifier. For comparison, the study also includes a neural baseline using a two-layer multilayer perceptron (MLP) over the same ...

---

### 27. Chain-based Distillation for Effective Initialization of Variable-Sized Small Language Models

**Authors:** Boyu Shi, YiCheng Jiang, Chang Liu, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07783v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07783v1)

**Summary:** Large language models (LLMs) achieve strong performance but remain costly to deploy in resource-constrained settings. Training small language models (SLMs) from scratch is computationally expensive, while conventional knowledge distillation requires repeated access to large teachers for different target sizes, leading to poor scalability. To solve these problems, we propose \textbf{Chain-based Distillation (CBD)}, a scalable paradigm for efficiently initializing variable-sized language models. A...

---

### 28. CktFormalizer: Autoformalization of Natural Language into Circuit Representations

**Authors:** Jing Xiong, Qi Han, Chenchen Ding, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07782v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07782v1)

**Summary:** LLMs can generate hardware descriptions from natural language specifications, but the resulting Verilog often contains width mismatches, combinational loops, and incomplete case logic that pass syntax checks yet fail in synthesis or silicon. We present CktFormalizer, a framework that redirects LLM-driven hardware generation through a dependently-typed HDL embedded in Lean 4. Lean serves three roles: (i) type checker:dependent types encode bit-width constraints, case coverage, and acyclicity, tur...

---

### 29. Tracing Uncertainty in Language Model "Reasoning"

**Authors:** Nils Grünefeld, Bertram Højer, Philipp Mondorf, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07776v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07776v1)

**Summary:** Language model (LM) "reasoning", commonly described as Chain-of-Thought or test-time scaling, often improves benchmark performance, but the dynamics underlying this process remain poorly understood. We study these dynamics through the lens of uncertainty quantification by treating the "reasoning" traces, the intermediate token sequences generated by LMs, as evolving model states. We summarize each trace by an uncertainty trace profile: a small set of features describing the shape of the uncertai...

---

### 30. Rethinking State Tracking in Recurrent Models Through Error Control Dynamics

**Authors:** Jiwan Chung, Heechan Choi, Seon Joo Kim

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07755v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07755v1)

**Summary:** The theory of state tracking in recurrent architectures has predominantly focused on expressive capacity: whether a fixed architecture can theoretically realize a set of symbolic transition rules. We argue that equally important is error control, the dynamics governing hidden-state drift along the directions that distinguish symbolic states. We prove that affine recurrent networks, a class of models encompassing State-Space Models and Linear Attention, cannot correct errors along state-separatin...

---

### 31. TextLDM: Language Modeling with Continuous Latent Diffusion

**Authors:** Jiaxiu Jiang, Jingjing Ren, Wenbo Li, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07748v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07748v1)

**Summary:** Diffusion Transformers (DiT) trained with flow matching in a VAE latent space have unified visual generation across images and videos. A natural next step toward a single architecture for both generation (visual synthesis) and understanding (text generation) is to apply this framework to language modeling. We propose TextLDM, which transfers the visual latent diffusion recipe to text generation with minimal architectural modification. A Transformer-based VAE maps discrete tokens to continuous la...

---

### 32. Benchmarking EngGPT2-16B-A3B against Comparable Italian and International Open-source LLMs

**Authors:** Andrea Sassella, Andrea Chizzola, Tommaso Bianchi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07731v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07731v1)

**Summary:** This report benchmarks the performance of ENGINEERING Ingegneria Informatica S.p.A.'s EngGPT2MoE-16B-A3B LLM, a 16B parameter Mixture of Experts (MoE) model with 3B active parameters. Performance is investigated across a wide variety of representative benchmarks, and is compared against comparably-sized open-source MoE and dense models. In comparison with popular Italian models, namely FastwebMIIA-7B, Minerva-7B, Velvet-14B, and LLaMAntino-3-ANITA-8B, EngGPT2MoE-16B-A3B performs as well or bette...

---

### 33. SOD: Step-wise On-policy Distillation for Small Language Model Agents

**Authors:** Qiyong Zhong, Mao Zheng, Mingyang Song, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07725v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07725v1)

**Summary:** Tool-integrated reasoning (TIR) is difficult to scale to small language models due to instability in long-horizon tool interactions and limited model capacity. While reinforcement learning methods like group relative policy optimization provide only sparse outcome-level rewards. Recently, on-policy distillation (OPD) has gained popularity by supplying dense token-level supervision from a teacher on student-generated trajectories. However, our experiments indicate that applying OPD to TIR leads t...

---

### 34. Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models

**Authors:** Victor Conchello Vendrell, Arnau Padres Masdemont, Niccolò Grillo, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07721v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07721v1)

**Summary:** Recurrent LLM architectures have emerged as a promising approach for improving reasoning, as they enable multi-step computation in the embedding space without generating intermediate tokens. Models such as Ouro perform reasoning by iteratively updating internal representations while retaining a standard Key-Value (KV) cache across iterations, causing memory consumption to grow linearly with reasoning depth. Consequently, increasing the number of reasoning iterations can lead to prohibitive memor...

---

### 35. SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation

**Authors:** Jie Sun, Mao Zheng, Mingyang Song, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07711v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07711v1)

**Summary:** On-policy distillation (OPD) is a standard tool for transferring teacher behavior to a smaller student, but it implicitly assumes that teacher and student predictions are comparable token by token, an assumption that fails whenever the two models tokenize the same text differently. Under heterogeneous tokenizers, exact shared-token matching silently discards a large fraction of the teacher signal at precisely the positions where vocabularies disagree. We propose \textbf{\underline{Sim}ple \under...

---

### 36. Guidance Is Not a Hyperparameter: Learning Dynamic Control in Diffusion Language Models

**Authors:** Fan Zhou, Tim Van de Cruys

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07701v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07701v1)

**Summary:** Classifier-Free Guidance (CFG) is a widely used mechanism for controlling diffusion-based generative models, yet its guidance scale is typically treated as a fixed hyperparameter throughout generation. This static design yields a suboptimal controllability and quality tradeoff, as the optimal degree of guidance varies across tasks and across different stages of the diffusion process, especially in NLP domain. We recast CFG scale selection as a sequential decision-making problem and propose to le...

---

### 37. DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain

**Authors:** Hsuvas Borkakoty, Sebastian Pohl, Cheng Wang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07699v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07699v1)

**Summary:** LLM-based agents are increasingly deployed for routine but consequential tasks in real-world domains, where their behavior is governed by inherently ambiguous domain policies that admit multiple valid interpretations. Despite the prevalence of such ambiguities in practice, existing agent benchmarks largely assume unambiguous, well-specified policies, leaving a critical evaluation gap. We introduce DRIP-R, a benchmark that systematically exploits real-world retail policy ambiguities to construct ...

---

### 38. TRACE: Tourism Recommendation with Accountable Citation Evidence

**Authors:** Zixu Zhao, Sijin Wang, Yu Hou, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07677v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07677v1)

**Summary:** Tourism is a high-stakes setting for conversational recommender systems (CRS): a plausible-sounding suggestion can waste real money and trip time once a traveler acts on it. Existing CRS benchmarks primarily evaluate systems with a single Recall@k score over entity mentions, and tourism-specific resources add spatial or knowledge-graph context, yet none of them couple multi-turn recommendation with verbatim review-span evidence and rejection recovery. This leaves an evaluation gap for tourism re...

---

### 39. Not All Tokens Learn Alike: Attention Entropy Reveals Heterogeneous Signals in RL Reasoning

**Authors:** Gengyang Li, Zheng-Fan Wu, Siqi Bao, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07660v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07660v1)

**Summary:** Reinforcement-learning-based post-training has become a key approach for improving the reasoning ability of large language models, but its token-level learning signals remain poorly understood. This work studies their heterogeneity through attention entropy, which measures how concentrated or diffuse the contextual support is for each response token.   We first show that token-level RL objectives are sparsely estimable: uniformly random 20 percent token subsets preserve much of the full-token he...

---

### 40. Reliable Chain-of-Thought via Prefix Consistency

**Authors:** Naoto Iwase, Yuki Ichihara, Mohammad Atif Quamar, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07654v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07654v1)

**Summary:** Large Language Models often improve accuracy on reasoning tasks by sampling multiple Chain-of-Thought (CoT) traces and aggregating them with majority voting (MV), a test-time technique called self-consistency. When we truncate a CoT partway through and regenerate the remainder, we observe that traces with correct answers reproduce their original answer more often than traces with wrong answers. We use this difference as a reliability signal, prefix consistency, that weights each candidate answer...

---

### 41. Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation

**Authors:** Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07647v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07647v1)

**Summary:** Automated short answer scoring (ASAS) is shifting from discriminative, fine-tuned models to large language models (LLMs) used in few-shot settings. This paradigm leverages LLMs broad world knowledge and ease of deployment, but limited task-specific data may reduce alignment on complex scoring tasks. In particular, its impact on scoring partially correct responses that require nuanced interpretation remains underexplored. We investigate the relationship between the degree of task-specific adaptat...

---

### 42. MAVEN: Multi-Agent Verification-Elaboration Network with In-Step Epistemic Auditing

**Authors:** Yinsheng Yao, Jiehao Tang, Zhaozhen Yang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07646v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07646v1)

**Summary:** While explicit reasoning trajectories enhance model interpretability, existing paradigms often rely on monolithic chains that lack intermediate verification, allowing early errors to cascade unchecked. This lack of modularity impedes granular auditing and compromises the epistemic trust required for high-stakes applications. We propose MAVEN (Multi-Agent Verification-Elaboration Network with In-Step Epistemic Auditing), a blackboard-inspired framework designed to transform LLMs into deliberate r...

---

### 43. Multi-Dimensional Evaluation of LLMs for Grammatical Error Correction

**Authors:** Adnan Labib, Qiao Wang, Yixuan Huang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07635v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07635v1)

**Summary:** Automated assistants for Grammatical Error Correction are now embedded in educational platforms serving millions of learners, yet three critical gaps remain in this domain: (1) latest-generation Large Language Models (LLMs) lack comprehensive evaluation on grammar correction tasks; (2) whether combining these LLMs improves correction quality is unexplored; and (3) the extent to which reference-based metrics underestimate GEC system performance has not been adequately quantified. In this study, f...

---

### 44. Post-training makes large language models less human-like

**Authors:** Marcel Binz, Elif Akata, Abdullah Almaatouq, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07632v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07632v1)

**Summary:** Large language models (LLMs) are increasingly used as surrogates for human participants, but it remains unclear which models best capture human behavior and why. To address this, we introduce Psych-201, a novel dataset that enables us to measure behavioral alignment at scale. We find that post-training -- the stage that turns base models into useful assistants -- consistently reduces alignment with human behavior across model families, sizes, and objectives. Moreover, this misalignment widens in...

---

### 45. Safe, or Simply Incapable? Rethinking Safety Evaluation for Phone-Use Agents

**Authors:** Zhengyang Tang, Yi Zhang, Chenxin Li, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07630v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07630v1)

**Summary:** When a phone-use agent avoids harm, does that show safety, or simply inability to act? Existing evaluations often cannot tell. A harmful outcome may be avoided because the agent recognized the risk and chose the safe action, or because it failed to understand the screen or execute any relevant action at all. These cases have different causes and call for different fixes, yet current benchmarks often merge them under task success, refusal, or final harmful outcome. We address this problem with Ph...

---

### 46. Is She Even Relevant? When BERT Ignores Explicit Gender Cues

**Authors:** Jonas Klein, Chiara Manna, Eva Vanmassenhove

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07622v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07622v1)

**Summary:** Gender bias in large language models has primarily been investigated for English, while languages with grammatical or morphological gender remain comparatively understudied. This paper investigates how and when gender information emerges in a Dutch BERT model trained from scratch, offering one of the first checkpoint-level analyses of bias formation in a Transformer architecture for a language combining overt morphological gender marking and generic forms. By extracting contextual embeddings thr...

---

### 47. Intent-Driven Semantic ID Generation for Grounded Conversational News Recommendation

**Authors:** Hongyang Su, Beibei Kong, Lei Cheng, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07613v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07613v1)

**Summary:** Conversational news recommendation requires grounding each suggestion in a rapidly evolving article corpus while addressing implicit user intents that lack explicit retrievable keywords. To characterize this scenario, we identify 6 intent types from production dialogues: five are implicit and pose fundamental challenges to standard RAG pipelines, forming a critical retrieve-first bottleneck. To address these issues, we introduce intent-driven Semantic ID (SID) generation under a Generate-then-Ma...

---

### 48. Nürnberg NLP at PsyDefDetect: Multi-Axis Voter Ensembles for Psychological Defence Mechanism Classification

**Authors:** Philipp Steigerwald, Eric Rudolph, Jens Albrecht

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07606v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07606v1)

**Summary:** Detecting levels of psychological defence mechanisms in supportive conversations is inherently ambiguous. In the PsyDefDetect shared task at BioNLP 2026 the eight positive defence categories share surface language and differ only in pragmatic function and trained raters reach only moderate inter-annotator agreement. On such a task the decisive lever is not a stronger single model but error independence, since any single representation will waver on the overlapping defence boundaries. We translat...

---

### 49. Mathematical Reasoning via Intervention-Based Time-Series Causal Discovery Using LLMs as Concept Mastery Simulators

**Authors:** Tsuyoshi Okita

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07600v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07600v1)

**Summary:** Recent methods for improving LLM mathematical reasoning, whether through MCTS-based test-time search or causal graph-guided knowledge injection, cannot identify which concepts causally contribute to a correct answer, as the observed association may be spurious, driven by confounders such as problem difficulty.   We propose CIKA (Causal Intervention for Knowledge Activation), a framework that uses the LLM itself as an interventional simulator: a prompt sets the concept state to ``mastered'' and t...

---

### 50. Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States

**Authors:** Yunho Choi, Jongwon Lim, Woojin Ahn, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07579v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07579v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) for Large Reasoning Models hinges on baseline estimation for variance reduction, but existing approaches pay a heavy price: PPO requires a policy-model scale critic, while GRPO needs multiple rollouts per prompt to keep its empirical group mean stable. We introduce Policy Optimization with Internal State Value Estimation), which obtains a baseline at negligible cost by using the policy model's internal signals already computed during the poli...

---

## cs.CV

**50 papers**

### 1. 123D: Unifying Multi-Modal Autonomous Driving Data at Scale

**Authors:** Daniel Dauner, Valentin Charraut, Bastian Berle, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08084v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08084v1)

**Summary:** The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsis...

---

### 2. Normalizing Trajectory Models

**Authors:** Jiatao Gu, Tianrong Chen, Ying Shen, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08078v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08078v1)

**Summary:** Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. ...

---

### 3. EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction

**Authors:** Wei Yu, Yunhang Qian

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08073v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08073v1)

**Summary:** Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual ...

---

### 4. Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment

**Authors:** Jerry Jiang, Haowen Sun, Denis Gudovskiy, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08064v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08064v1)

**Summary:** Spatial intelligence in vision-language models (VLMs) attracts research interest with the practical demand to reason in the 3D world.Despite promising results, most existing methods follow the conventional 2D pipeline in VLMs and use pixel-aligned representations for the vision modality. However, correspondence-based models with implicit 3D scene understanding often fail to achieve spatial consistency, and representation-based models with 3D geometric priors lack efficiency in vision sequence se...

---

### 5. Flow-OPD: On-Policy Distillation for Flow Matching Models

**Authors:** Zhen Fang, Wenxuan Huang, Yu Zeng, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08063v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08063v1)

**Summary:** Existing Flow Matching (FM) text-to-image models suffer from two critical bottlenecks under multi-task alignment: the reward sparsity induced by scalar-valued rewards, and the gradient interference arising from jointly optimizing heterogeneous objectives, which together give rise to a 'seesaw effect' of competing metrics and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in the large language model community, we propose Flow-OPD, the first unified post-training...

---

### 6. 6D Pose Estimation via Keypoint Heatmap Regression with RGB-D Residual Neural Networks

**Authors:** Ismail Aljosevic, Amir Masoud Almasi, Ana Parovic, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08059v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08059v1)

**Summary:** In this paper, we propose a modular framework for 6D pose estimation based on keypoint heatmap regression. Our approach combines YOLOv10m for object detection with a ResNet18-based network that predicts 2D heatmaps from RGB images. Keypoints extracted from these heatmaps are used to estimate the 6D object pose via the PnP RANSAC algorithm. We compare different keypoint selection strategies to assess their impact on pose accuracy. Additionally, we extend the baseline by incorporating depth data u...

---

### 7. Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization

**Authors:** Hanchao Liu, Fang-Lue Zhang, Shining Zhang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08054v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08054v1)

**Summary:** Generating human motion that satisfies customized zero-shot goal functions, enabling applications such as controllable character animation and behavior synthesis for virtual agents, is a critical capability. While current approaches handle many unseen constraints, they fail on tasks with very challenging spatiotemporal restrictions, such as severe spatial obstacles or specified numbers of walking steps. To equip motion generators for these highly constrained tasks, we present a retrieval-guided ...

---

### 8. MoCoTalk: Multi-Conditional Diffusion with Adaptive Router for Controllable Talking Head Generation

**Authors:** Xinyan Ye, Jiankang Deng, Abbas Edalat

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08050v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08050v1)

**Summary:** Talking-head generation requires joint modeling of identity, head pose, facial expression, and mouth dynamics. Existing methods typically address only a subset of these factors, and rely on fixed-weight or heuristic fusion when multiple conditions are involved. We present MoCoTalk, a multi-conditional video diffusion framework that unifies four complementary control signals: a reference image, facial keypoints, 3DMM-rendered shading meshes, and the corresponding speech audio. To resolve destruct...

---

### 9. SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation

**Authors:** Tianfei Ren, Zhipeng Yan, Yiming Zhao, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08043v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08043v1)

**Summary:** While text-to-image models have made strong progress in visual fidelity, faithfully realizing complex visual intents remains challenging because many requirements must be tracked across grounding, generation, and verification. We refer to these requirements as semantic commitments and formalize their lifecycle discontinuity as the Conceptual Rift, where commitments may be locally resolved or checked but fail to remain identifiable as the same operational units throughout the generation lifecycle...

---

### 10. Object Hallucination-Free Reinforcement Unlearning for Vision-Language Models

**Authors:** Kaidi Jia, Yujie Lin, Chengyi Yang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08031v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08031v1)

**Summary:** Vision-language models (VLMs) raise growing concerns about privacy, copyright, and bias, motivating machine unlearning to remove sensitive knowledge. However, existing methods primarily fine-tune the language decoder, leading to superficial forgetting that fails to erase underlying visual representations and often introduces object hallucination. We propose HFRU, a reinforcement unlearning framework that operates on the vision encoder for deep semantic removal. Our two-stage approach combines al...

---

### 11. PET-Adapter: Test-Time Domain Adaptation for Full and Limited-Angle PET Image Reconstruction

**Authors:** Rüveyda Yilmaz, Yuli Wu, Johannes Stegmaier, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08030v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08030v1)

**Summary:** Positron Emission Tomography (PET) image reconstruction is inherently challenged by Poisson noise and physical degradation factors, which are further exacerbated in limited-angle acquisitions. While deep learning methods demonstrate promising performance, their generalization to unseen clinical data distributions remains limited without extensive retraining. We propose PET-Adapter, a test-time domain adaptation framework for generative PET reconstruction models pretrained solely on phantom data....

---

### 12. STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation

**Authors:** Ying Shen, Tianrong Chen, Yuan Gao, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08029v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08029v1)

**Summary:** Deep generative models have advanced rapidly across text and vision, motivating unified multimodal systems that can understand, reason over, and generate interleaved text-image sequences. Most existing approaches combine autoregressive language modeling with diffusion-based image generators, inheriting a structural mismatch between causal text generation and iterative visual denoising. We observe that autoregressive normalizing flows are autoregressive Transformers--sharing the same causal mask,...

---

### 13. TRAS: An Interactive Software for Tracing Tree Ring Cross Sections

**Authors:** Henry Marichal, Diego Passarella, Gregory Randall

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08025v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08025v1)

**Summary:** Tree ring marking remains a key step in dendrometry and dendrochronology, but it is often performed manually, making the process time-consuming, subjective, and difficult to scale to large image datasets.   We present the Tree Ring Analyzer Suite (TRAS), an open-source graphical software for automatic delineation, manual correction, and measurement of tree rings in wood cross-sectional images. TRAS integrates three complementary detection algorithms: the classical image-processing method CS-TRD ...

---

### 14. SphereVAD: Training-Free Video Anomaly Detection via Geodesic Inference on the Unit Hypersphere

**Authors:** Chao Huang, Penfei Wei, Wei Wang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08003v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08003v1)

**Summary:** Video anomaly detection (VAD) aims to automatically identify events that deviate from normal patterns in untrimmed surveillance videos. Existing methods universally depend on large-scale annotations or task-specific training procedures, severely limiting their rapid deployment to novel scenes. We observe that intermediate-layer features of pre-trained multimodal large language models (MLLMs) already encode rich anomaly semantics, yet existing approaches rely on the language output pathway and fa...

---

### 15. Rethinking Dense Optical Flow without Test-Time Scaling

**Authors:** Praroop Chanda, Suryansh Kumar

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08000v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08000v1)

**Summary:** Recent progress in dense optical flow has been driven by increasingly complex architectures and multi-step refinement for test-time scaling. While these approaches achieve strong benchmark performance, they also require substantial computation during inference. This raises a fundamental question: Is scaling test-time computation the only way to improve dense optical flow accuracy? We argue that it is not. Instead, powerful visual semantic and geometric priors encoded in modern foundation models ...

---

### 16. Uncertainty Quantification for Cardiac Shape Reconstruction with Deep Signed Distance Functions via MCMC methods

**Authors:** Jan Verhülsdonk, Thomas Grandits, Francisco Sahli Costabal, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07987v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07987v1)

**Summary:** Atlas-based approaches allow high-quality, patient-specific shape reconstructions of cardiac anatomy from sparse and/or noisy data such as point clouds. However, these methods are mainly prior-driven, so the impact of uncertainty can be large, limiting their clinical reliability. We propose a probabilistic framework for uncertainty-aware cardiac shape reconstruction that combines Deep Signed Distance Functions (DeepSDFs) with Markov Chain Monte Carlo (MCMC) sampling. Cardiac geometries are model...

---

### 17. Seeing Across Skies and Streets: Feedforward 3D Reconstruction from Satellite, Drone, and Ground Images

**Authors:** Qiwei Wang, Zhongyao Tuo, Xianghui Ze, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07978v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07978v1)

**Summary:** Cross-view localization classically asks: where does this ground image lie on the satellite tile? Existing methods are typically limited to 3-DoF estimates -- an $(x,y)$ position and a yaw angle -- because nadir satellite imagery provides no direct cues for roll, pitch, or altitude, forcing a reliance on planar-motion and zero-tilt assumptions. These assumptions break on real terrain with slopes, ramps, and tilted camera mounts. To overcome this, we introduce a single UAV image as an intermediat...

---

### 18. HEART: Hyperspherical Embedding Alignment via Kent-Representation Traversal in Diffusion Models

**Authors:** Arani Roy, Shristi Das Biswas, Kaushik Roy

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07973v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07973v1)

**Summary:** Text-to-image diffusion models can generate visually stunning images, yet, controlling what appears and how it appears, remains surprisingly difficult, especially when operating solely within the constraints of the text-conditioning space. For example, changing a subject or adjusting an attribute often leads to unintended side effects, such as altered backgrounds or distorted details. This is because most existing text-based control methods treat the embedding space as Euclidean and apply simple...

---

### 19. DVD: Discrete Voxel Diffusion for 3D Generation and Editing

**Authors:** Zhengrui Xiang, Jiaqi Wu, Fupeng Sun, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07971v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07971v1)

**Summary:** We introduce Discrete Voxel Diffusion (DVD), a discrete diffusion framework to generate, assess, and edit sparse voxels for SLat (Structured LATent) based 3D generative pipelines. Although discrete diffusion has not generally displaced continuous diffusion in image-like generation, we show that it can be an effective first-stage prior for sparse voxel scaffolds. By treating voxel occupancy as a native discrete variable, DVD avoids continuous-to-discrete thresholding and provides a simple framewo...

---

### 20. TimeLesSeg: Unified Contrast-Agnostic Cross-Sectional and Longitudinal MS Lesion Segmentation via a Stochastic Generative Model

**Authors:** Vicent Caselles-Ballester, Eloy Martínez-Heras, Giuseppe Pontillo, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07955v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07955v1)

**Summary:** Multiple sclerosis (MS) expresses substantial clinical and radiological heterogeneity, which poses significant challenges for automatic lesion segmentation. The current deep learning-based SOTA is highly susceptible to changes in both distribution, e.g., changes in scanner; as well as the structure of inputs, evident in the current divide between cross-sectional and longitudinal approaches. We introduce TimeLesSeg, a unified contrast-agnostic framework designed to segment MS lesions regardless o...

---

### 21. Rebalancing gradient to improve self-supervised co-training of depth, odometry and optical flow predictions

**Authors:** Marwane Hariat, Antoine Manzanera, David Filliat

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07945v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07945v1)

**Summary:** We present CoopNet, an approach that improves the cooperation of co-trained networks by dynamically adapting the apportionment of gradient, to ensure equitable learning progress. It is applied to motion-aware self-supervised prediction of depth maps, by introducing a new hybrid loss, based on a distribution model of photo-metric reconstruction errors made by, on the one hand the depth + odometry paired networks, and on the other hand the optical flow network. This model essentially assumes that ...

---

### 22. TAVIS: A Benchmark for Egocentric Active Vision and Anticipatory Gaze in Imitation Learning

**Authors:** Giacomo Spigler

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07943v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07943v1)

**Summary:** Active vision -- where a policy controls its own gaze during manipulation -- has emerged as a key capability for imitation learning, with multiple independent systems demonstrating its benefits in the past year. Yet there is no shared benchmark to compare approaches or quantify what active vision contributes, on which task types, and under what conditions. We introduce TAVIS, evaluation infrastructure for active-vision imitation learning, with two complementary task suites -- TAVIS-Head (5 tasks...

---

### 23. Delta-Adapter: Scalable Exemplar-Based Image Editing with Single-Pair Supervision

**Authors:** Jiacheng Chen, Songze Li, Han Fu, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07940v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07940v1)

**Summary:** Exemplar-based image editing applies a transformation defined by a source-target image pair to a new query image. Existing methods rely on a pair-of-pairs supervision paradigm, requiring two image pairs sharing the same edit semantics to learn the target transformation. This constraint makes training data difficult to curate at scale and limits generalization across diverse edit types. We propose Delta-Adapter, a method that learns transferable editing semantics under single-pair supervision, re...

---

### 24. One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy

**Authors:** Zuojin Tang, Shengchao Yuan, Xiaoxin Bai, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07931v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07931v1)

**Summary:** Vision-language-action (VLA) models increasingly rely on auxiliary world modules to plan over long horizons, yet how such modules should be parameterized on top of a pretrained VLA remains an open design question. Existing world-model-augmented VLAs typically pass the per-frame visual stream into the world module at high visual bandwidth and treat its rollout as a side product of action prediction; under a constrained adaptation budget on a frozen backbone, this leaves both the per-frame represe...

---

### 25. MedVIGIL: Evaluating Trustworthy Medical VLMs Under Broken Visual Evidence

**Authors:** Hanqi Jiang, Junhao Chen, Yi Pan, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07919v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07919v1)

**Summary:** Medical vision--language models (VLMs) are usually evaluated on intact image--question pairs, but trustworthy clinical use requires a stronger property: a model must recognise when the evidential basis for an answer has failed. We study this through silent failures under perturbed evidence, where a vision-required medical question is paired with a false premise, wording perturbation, knowledge-only rewrite, or ROI-corrupted image, yet the model returns a fluent non-refusal answer. We introduce m...

---

### 26. What Matters for Diffusion-Friendly Latent Manifold? Prior-Aligned Autoencoders for Latent Diffusion

**Authors:** Zhengrong Yue, Taihang Hu, Mengting Chen, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07915v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07915v1)

**Summary:** Tokenizers are a crucial component of latent diffusion models, as they define the latent space in which diffusion models operate. However, existing tokenizers are primarily designed to improve reconstruction fidelity or inherit pretrained representations, leaving unclear what kind of latent space is truly friendly for generative modeling. In this paper, we study this question from the perspective of latent manifold organization. By constructing controlled tokenizer variants, we identify three ke...

---

### 27. Flatness and Gradient Alignment Are Both Necessary: Spectral-Aware Gradient-Aligned Exploration for Multi-Distribution Learning

**Authors:** Aristotelis Ballas, Christos Diou

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07914v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07914v1)

**Summary:** Sharpness-aware and gradient-alignment methods have been shown to improve generalization, however each family of methods targets a single geometric property of the loss landscape, while ignoring the other. In this paper, we show that this omission is structurally unavoidable and that both flatness and gradient alignment should be considered in multi-distribution learning settings. Specifically, we derive an excess-risk decomposition that yields two additive leading-order terms: (i) an alignment ...

---

### 28. One World, Dual Timeline: Decoupled Spatio-Temporal Gaussian Scene Graph for 4D Cooperative Driving Reconstruction

**Authors:** Yulong Chen, Xiaoyun Dong, Haoyu Zhang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07910v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07910v1)

**Summary:** Reconstructing dynamic scenes from Vehicle-to-Infrastructure Cooperative Autonomous Driving (VICAD) data is fundamentally complicated by temporal asynchrony: vehicle and infrastructure cameras operate on independent clocks, capturing the same dynamic agent such as cars and pedestrians at different physical times. Existing Gaussian Scene Graph methods implicitly assume synchronized observations and assign a single pose per agent per frame, which is an assumption that breaks in cooperative setting...

---

### 29. Consistency Regularised Gradient Flows for Inverse Problems

**Authors:** Alessio Spagnoletti, Tim Y. J. Wang, Marcelo Pereyra, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07907v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07907v1)

**Summary:** Vision-Language Latent Diffusion Models (LDMs) (Rombach et al., 2022) provide powerful generative priors for inverse problems. However, existing LDM-based inverse solvers typically require a large number of neural function evaluations (NFEs) and backpropagation through large pretrained components, leading to substantial computational costs and, in some cases, degraded reconstruction quality. We propose a unified Euclidean-Wasserstein-2 gradient-flow framework that jointly performs posterior samp...

---

### 30. Semantic-Aware Adaptive Visual Memory for Streaming Video Understanding

**Authors:** Hang Wu, Sherin Mary Mathews, Yujun Cai, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07897v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07897v1)

**Summary:** Online streaming video understanding requires models to process continuous visual inputs and respond to user queries in real time, where the unbounded stream and unpredictable query timing turn memory management into a central challenge. Existing methods typically compress visual tokens via visual similarity heuristics, or augment compression with KV-cache-level retrieval. However, compression decisions rarely incorporate semantic signals, and retrieval is often added after compression is finali...

---

### 31. Enhancing Federated Quadruplet Learning: Stochastic Client Selection and Embedding Stability Analysis

**Authors:** Ozgu Goksu, Nicolas Pugeault

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07888v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07888v1)

**Summary:** Federated Learning (FL) enables decentralised model training across distributed clients without requiring data centralisation. However, the generalisation performance of the global model is usually degraded by data heterogeneity across clients, particularly under limited data availability and class imbalance. To address this challenge, we propose FedQuad, a novel method that explicitly enforces minimising intra-class representations while enabling inter-class splits across clients. By jointly mi...

---

### 32. Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models

**Authors:** Yuancheng Wei, Linli Yao, Lei Li, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07872v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07872v1)

**Summary:** Multimodal reward models have advanced substantially in text and image domains, yet progress in video understanding reward modeling remains severely limited by the lack of robust evaluation benchmarks and high-quality preference data. To address this, we propose a unified framework spanning benchmark design, data construction, and reward model training. We introduce Video Understanding Reward Bench (VURB), a benchmark featuring 2,100 preference pairs with long chain-of-thought reasoning traces (...

---

### 33. From Synthetic to Real: Toward Identity-Consistent Makeup Transfer with Synthetic and Real Data

**Authors:** Yue Yu, Jiayu Wang, Jiajia Shi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07861v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07861v1)

**Summary:** Makeup transfer aims to apply the makeup style of a reference portrait to a source portrait while preserving identity and background. Early methods formulate this task as unsupervised image-to-image translation, relying on surrogate objectives and often yielding limited performance. Recent diffusion- and flow-based approaches instead exploit synthetic data for supervised training, leading to significant improvements. However, these methods still face two critical challenges: synthetic supervisio...

---

### 34. EyeCue: Driver Cognitive Distraction Detection via Gaze-Empowered Egocentric Video Understanding

**Authors:** Lang Zhang, JinYi Yoon, Matthew Corbett, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07859v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07859v1)

**Summary:** Driver cognitive distraction is a major cause of road collisions and remains difficult to detect. Unlike manual or visual distraction, cognitive distraction is diverted by thoughts unrelated to driving, even when the driver appears visually attentive and exhibits no explicit physical movements. In this work, we propose EyeCue, a gaze-empowered egocentric video understanding framework, to detect driver cognitive distraction. A key insight is that cognitive distraction manifests in the interaction...

---

### 35. BRIDGE: Background Routing and Isolated Discrete Gating for Coarse-Mask Local Editing

**Authors:** Peilin Xiong, Honghui Yuan, Junwen Chen, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07846v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07846v1)

**Summary:** Coarse-mask local image editing asks a model to modify a user-indicated region while preserving the surrounding scene. In practice, however, rough masks often become unintended shape priors: instead of serving as flexible edit support, the mask can pull the generated object toward its accidental boundary. We study this failure as mask-shape bias and frame the task through a Two-Zone Constraint, where the background should remain stable while the editable region should follow the instruction with...

---

### 36. Explainable Part-Based Vehicle Classifier with Spatial Awareness

**Authors:** Andreas Caduff, Klaus Zahn, Jonas Hofstetter, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07831v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07831v1)

**Summary:** In the area of Intelligent Transportation Systems (ITS), fine-grained vehicle classification systems play an essential role. Recently, the authors have presented a novel vision-based classification approach in which standard end-to-end Convolutional Neural Networks (CNNs) have been decomposed into 1) a CNN-based detector for semantically strong vehicle parts, followed by 2) feature construction and 3) final classification by a decision tree. In contrast to conventional CNNs, this allows both eas...

---

### 37. Anisotropic Modality Align

**Authors:** Xiaomin Yu, Yijiang Li, Yuhui Zhang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07825v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07825v1)

**Summary:** Training multimodal large language models has long been limited by the scarcity of high-quality paired multimodal data. Recent studies show that the shared representation space of pretrained multimodal contrastive models can serve as a bridge, enabling models to perform multimodal training with unimodal data. However, the key premise of this paradigm remains insufficiently understood: can representations from different modalities be reliably interchanged? The core obstacle lies in the persistent...

---

### 38. Divide and Conquer: Object Co-occurrence Helps Mitigate Simplicity Bias in OOD Detection

**Authors:** Boyang Dai, Chaoqi Chen, Yizhou Yu

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07821v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07821v1)

**Summary:** Out-of-distribution (OOD) detection is crucial for ensuring the reliability of deep learning models. Existing methods mostly focus on regular entangled representations to discriminate in-distribution (ID) and OOD data, neglecting the rich contextual information within images. This issue is particularly challenging for detecting near-OOD, as models with simplicity bias struggle to learn discriminative features in disentangled representations. The human visual system can use the co-occurrence of o...

---

### 39. GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning

**Authors:** Brown Ebouky, Gabriele Carrino, Niccolo Avogaro, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07817v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07817v1)

**Summary:** Human visual reasoning is governed by active vision, a process where metacognitive control drives top-down goal-directed attention, dynamically routing foveal focus toward task-relevant details while maintaining peripheral awareness of the global scene. In contrast, modern Vision-Language Models (VLMs) process visual information passively, relying on the static accumulation of massive token contexts that dilute spatial reasoning and induce linguistic hallucinations. Here we propose the following...

---

### 40. ICDAR 2026 Competition on Writer Identification and Pen Classification from Hand-Drawn Circles

**Authors:** Thomas Gorges, Janne van der Loop, Lukas Hüttner, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07816v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07816v1)

**Summary:** This paper presents CircleID, a large-scale ICDAR 2026 competition on writer identification and pen classification from scanned hand-drawn circles. The primary objective is to investigate how biometric writer characteristics and physical pen features naturally entangle within minimal, static traces. CircleID comprises two distinct tasks: (1) open-set writer identification, requiring models to recognize known writers while explicitly rejecting unknown ones, and (2) cross-writer pen classification...

---

### 41. Pre-training Enables Extraordinary All-optical Image Denoising

**Authors:** Xudong Lv, Yuxiang Sun, Shuo Wang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07810v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07810v1)

**Summary:** Optical neural networks are emerging as powerful machine learning and information processing tools because of their potential advantages in speed and energy efficiency. The training methods of these physical models, however, remain underexplored compared to their digital counterparts and are leading to suboptimal performance. This paper reports a pre-training-driven approach that leads to snapshot image denoising with substantially improved quality. We demonstrated effective free-space optical d...

---

### 42. Text-to-CAD Evaluation with CADTests

**Authors:** Dimitrios Mallis, Marco Wang, Ahmet Serdar Karadeniz, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07807v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07807v1)

**Summary:** Text-to-CAD has recently emerged as an important task with the potential to substantially accelerate design workflows. Despite its significance, there has been surprisingly little work on Text-to-CAD evaluation, and assessing CAD model generation performance remains a considerable challenge. In this work, we introduce a new evaluation perspective for Text-to-CAD based on automated testing. We propose CADTestBench, the first test-based benchmark for Text-to-CAD, based on CADTests, executable soft...

---

### 43. SARA: Semantically Adaptive Relational Alignment for Video Diffusion Models

**Authors:** Jiesong Lian, Zixiang Zhou, Ruizhe Zhong, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07800v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07800v1)

**Summary:** Recent video diffusion models (VDMs) synthesize visually convincing clips, yet still drop entities, mis-bind attributes, and weaken the interactions specified in the prompt. Representation-alignment objectives such as VideoREPA and MoAlign improve fine-grained text following by distilling spatio-temporal token relations from a frozen visual foundation model, but their pairwise supervision budget is allocated by visual or motion cues rather than by how relevant each pair is to the prompt. We pres...

---

### 44. Spectral Surgery: Class-Targeted Post-Hoc Rebalancing via Hessian Spike Perturbation

**Authors:** Hugo Vigna, Samuel Bontemps

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07790v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07790v1)

**Summary:** The Hessian spectrum of trained deep networks exhibits a characteristic structure: a continuous bulk of near-zero eigenvalues and a small number of large outlier eigenvalues (spikes), confirming the relevance of Random Matrix Theory in deep learning. The spike count matches the number of classes minus one. While prior work has described this structure, no method has exploited it operationally to improve classification performance. We propose Spectral Surgery, a post-hoc optimization method that ...

---

### 45. APEX: Assumption-free Projection-based Embedding eXamination Metric for Image Quality Assessment

**Authors:** Caterina Gallegati, Monica Bianchini, Franco Scarselli, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07786v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07786v1)

**Summary:** As generative models achieve unprecedented visual quality, the gold standard for image evaluation remains traditional feature-distribution metrics (e.g., FID). However, these metrics are provably hindered by the closed-vocabulary bottleneck of outdated features and the assumptive bias of rigid parametric formulations. Recent alternatives exploit modern backbones to solve the feature bottleneck, yet continue to suffer from parametric limitations. To close this gap, we introduce APEX (Assumption-f...

---

### 46. Radiologist-Guided Causal Concept Bottleneck Models for Chest X-Ray Interpretation

**Authors:** Amy Rafferty, Rishi Ramaesh, Ajitha Rajan

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07785v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07785v1)

**Summary:** Concept Bottleneck Models (CBMs) in medical imaging aim to improve model interpretability by predicting intermediate clinical concepts before final diagnoses. However, most existing CBMs treat concepts as discriminative predictors of pathology labels, without explicitly modelling the underlying clinical generative process where diseases produce observable radiographic findings. We propose XpertCausal, a radiologist-guided causal CBM for chest X-ray interpretation which models pathology-to-concep...

---

### 47. Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis

**Authors:** Niklas Vaara, Lam Huynh, Pekka Sangi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07781v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07781v1)

**Summary:** Explicit neural representations such as 3D Gaussian Splatting (3DGS) enable high-fidelity and real-time novel view synthesis, yet optimize for alpha-composited optical appearance rather than ray-intersectable geometry. In contrast, radio-frequency (RF) digital twins require deterministic multi-bounce paths, where the geometry dictates trajectories and their associated attenuation and delay. We introduce a framework enabling differentiable RF propagation simulation directly within visually recons...

---

### 48. SIMI: Self-information Mining Network for Low-light Image Enhancement

**Authors:** Xuanshuo Fu, Lei Kang, Javier Vazquez-Corral

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07767v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07767v1)

**Summary:** Poor lighting conditions significantly impact image quality, posing substantial challenges for image editing and visualization. Many existing enhancement methods aim at proposing complex models while neglecting the intrinsic information contained within low-light images. In this work, we propose the Self-Information Mining (SIMI) network, an innovative unsupervised framework that decomposes low-light images into multiple components based on bit-plane decomposition. Our approach allows mining int...

---

### 49. Head Similarity: Modeling Structured Whole-Head Appearance Beyond Face Recognition

**Authors:** Yingfeng Wang, Yuxuan Xiao, Shengcai Liao

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07766v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07766v1)

**Summary:** Many vision applications require identity consistency beyond strict biometric recognition, especially under non-frontal views or when facial cues are missing. However, conventional face recognition models enforce intra-identity invariance, collapsing appearance variations such as hairstyle or styling changes into a single representation, limiting their use in appearance-sensitive scenarios. To address this limitation, we introduce Head Similarity, a new formulation that extends identity-centric ...

---

### 50. Benchmarking Foundation Models for Renal Lesion Stratification in CT

**Authors:** Hartmut Häntze, Sarah de Boer, Myrthe Buser, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07749v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07749v1)

**Summary:** The rapid proliferation of open-source medical foundation models (FMs) raises a practical question: how well do their pre-trained representations transfer to clinically relevant but data-scarce classification tasks? Particularly in CT-based renal lesion classification, a push toward greater generalizability would be meaningful, as the field is constrained by inherently limited training data. We addressed this through a benchmark of three medical FMs on this specific task. This six-class problem ...

---

## cs.LG

**50 papers**

### 1. Normalizing Trajectory Models

**Authors:** Jiatao Gu, Tianrong Chen, Ying Shen, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08078v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08078v1)

**Summary:** Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. ...

---

### 2. Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping

**Authors:** Maryam Maghsoudi, Shihab Shamma

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08075v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08075v1)

**Summary:** Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve ...

---

### 3. GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs

**Authors:** Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08074v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08074v1)

**Summary:** Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proxi...

---

### 4. A Note on Non-Negative $L_1$-Approximating Polynomials

**Authors:** Jane H. Lee, Anay Mehrotra, Manolis Zampetakis

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08072v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08072v1)

**Summary:** $L_1$-Approximating polynomials, i.e., polynomials that approximate indicator functions in $L_1$-norm under certain distributions, are widely used in computational learning theory. We study the existence of \textit{non-negative} $L_1$-approximating polynomials with respect to Gaussian distributions. This is a stronger requirement than $L_1$-approximation but weaker than sandwiching polynomials (which themselves have many applications). These non-negative approximating polynomials have recently f...

---

### 5. Reinforcement Learning for Exponential Utility: Algorithms and Convergence in Discounted MDPs

**Authors:** Gugan Thoppe, L. A. Prashanth, Ankur Naskar, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08053v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08053v1)

**Summary:** Reinforcement learning (RL) for exponential-utility optimization in discounted Markov decision processes (MDPs) lacks principled value-based algorithms. We address this gap in the fixed risk-aversion setting. Building on the Bellman-type equation for exponential utility studied in \cite{porteus1975optimality}, we derive two Q-value-style extensions and show that the associated operators are contractions in the $L_\infty$ and sup-log/Thompson metrics, respectively. We characterize their fixed poi...

---

### 6. Fast Byte Latent Transformer

**Authors:** Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08044v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08044v1)

**Summary:** Recent byte-level language models (LMs) match the performance of token-level models without relying on subword vocabularies, yet their utility is limited by slow, byte-by-byte autoregressive generation. We address this bottleneck in the Byte Latent Transformer (BLT) through new training and generation techniques. First, we introduce BLT Diffusion (BLT-D), a new model and our fastest BLT variant, trained with an auxiliary block-wise diffusion objective alongside the standard next-byte prediction ...

---

### 7. Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph

**Authors:** Ning Liu, Chuanneng Sun, Kristina Klinkner, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08037v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08037v1)

**Summary:** Direct Preference Optimization (DPO) aligns language models using pairwise preference comparisons, offering a simple and effective alternative to Reinforcement Learning (RL) from human feedback. However, in many practical settings, training data consists of multiple rollouts per prompt, inducing rich preference structure that pairwise DPO fails to exploit. Collapsing such data into independent pairs discards transitivity, introduces redundant or conflicting supervision, and can lead to unstable ...

---

### 8. Don't Get Your Kroneckers in a Twist: Gaussian Processes on High-Dimensional Incomplete Grids

**Authors:** Mads Greisen Højlund, August Smart Lykke-Møller, Henry Moss, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08036v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08036v1)

**Summary:** We introduce CUTS-GPR, a new method for performing numerically exact Gaussian process regression (GPR) in high-dimensional settings. The key component of CUTS-GPR is an extremely fast kernel matrix-vector product, which exhibits near-linear or even linear scaling with the amount of training data, $N$, and low-order polynomial scaling with dimensionality, $D$. This is obtained by combining an additive kernel with an incomplete grid and exploiting the resulting structure of the kernel matrix. We d...

---

### 9. PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting

**Authors:** William Bjorndahl, Maninder Pal Singh, Farhad Nouri, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08035v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08035v1)

**Summary:** Building a site-specific propagation model typically requires either ray-tracing over detailed 3D maps or dense measurement campaigns. Both approaches are expensive and often infeasible for rapid deployments where geographic data is unavailable or outdated. We present PropSplat, a map-free propagation modeling method that reconstructs radio frequency (RF) fields using 3D anisotropic Gaussian primitives. Each Gaussian encodes a scalar path loss offset relative to an explicit baseline path loss mo...

---

### 10. Semiparametric Efficient Test for Interpretable Distributional Treatment Effects

**Authors:** Houssam Zenati, Arthur Gretton

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08034v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08034v1)

**Summary:** Distributional treatment effects can be invisible to means: a treatment may preserve average outcomes while changing tails, modes, dispersion, or rare-event probabilities. Kernel tests can detect discrepancies between interventional outcome laws, but global tests do not reveal where the laws differ. We propose DR-ME, to our knowledge the first semiparametrically efficient finite-location test for interpretable distributional treatment effects. DR-ME evaluates an interventional kernel witness at ...

---

### 11. PET-Adapter: Test-Time Domain Adaptation for Full and Limited-Angle PET Image Reconstruction

**Authors:** Rüveyda Yilmaz, Yuli Wu, Johannes Stegmaier, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08030v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08030v1)

**Summary:** Positron Emission Tomography (PET) image reconstruction is inherently challenged by Poisson noise and physical degradation factors, which are further exacerbated in limited-angle acquisitions. While deep learning methods demonstrate promising performance, their generalization to unseen clinical data distributions remains limited without extensive retraining. We propose PET-Adapter, a test-time domain adaptation framework for generative PET reconstruction models pretrained solely on phantom data....

---

### 12. STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation

**Authors:** Ying Shen, Tianrong Chen, Yuan Gao, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08029v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08029v1)

**Summary:** Deep generative models have advanced rapidly across text and vision, motivating unified multimodal systems that can understand, reason over, and generate interleaved text-image sequences. Most existing approaches combine autoregressive language modeling with diffusion-based image generators, inheriting a structural mismatch between causal text generation and iterative visual denoising. We observe that autoregressive normalizing flows are autoregressive Transformers--sharing the same causal mask,...

---

### 13. Adaptive Domain Decomposition Physics-Informed Neural Networks for Traffic State Estimation with Sparse Sensor Data

**Authors:** Eunhan Ka, Ludovic Leclercq, Satish V. Ukkusuri

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08028v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08028v1)

**Summary:** Traffic state estimation from sparse fixed sensors is challenging because physics-informed neural networks (PINNs) tend to over-smooth the shockwaves admitted by the Lighthill-Whitham-Richards (LWR) model. This study proposes Adaptive Domain Decomposition Physics-Informed Neural Networks (ADD-PINN), a two-stage residual-guided framework for LWR-based offline speed-field reconstruction. A coarse global PINN is first trained; its spatial residual profile is then used to place subdomain boundaries ...

---

### 14. Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction

**Authors:** Himanshu Udupi, Xiaocong Yang, ChengXiang Zhai

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08022v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08022v1)

**Summary:** Spiking Neural Networks (SNNs) have been proposed as biologically plausible and energy-efficient alternatives to conventional Artificial Neural Networks (ANNs). However, the training of SNN usually relies on surrogate gradients due to the non-differentiability of the spike function, introducing approximation errors that accumulate across layers. To address this challenge, we extend the work on convexification of parallel feedforward threshold networks to parallel recurrent threshold networks, wh...

---

### 15. Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims

**Authors:** Zezheng Lin, Fengming Liu

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08012v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08012v1)

**Summary:** Mechanistic interpretability papers increasingly use causal vocabulary: circuits, mediators, causal abstraction, monosemanticity. Such claims require explicit identification assumptions. A purposive audit of 10 papers across four methodological strands finds no dedicated identification-assumptions section and a recurring pattern: validation metrics such as faithfulness, completeness, monosemanticity, alignment, or ablation effects are reported as causal support without stating the assumptions th...

---

### 16. Interpreting Reinforcement Learning Agents with Susceptibilities

**Authors:** Chris Elliott, Einar Urdshals, David Quarel, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08007v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08007v1)

**Summary:** Susceptibilities are a technique for neural network interpretability that studies the response of posterior expectation values of observables to perturbations of the loss. We generalize this construction to the setting of the regret in deep reinforcement learning and investigate the utility of susceptibilities in a simple gridworld model that nevertheless exhibits non-trivial stagewise development. We argue that susceptibilities reveal internal features of the development of the model in paramet...

---

### 17. Penalty-Based First-Order Methods for Bilevel Optimization with Minimax and Constrained Lower-Level Problems

**Authors:** Yiyang Shen, Yutian He, Weiran Wang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08006v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08006v1)

**Summary:** We study a class of bilevel optimization problems in which both the upper- and lower-level problems have minimax structures. This setting captures a broad range of emerging applications. Despite the extensive literature on bilevel optimization and minimax optimization separately, existing methods mainly focus on bilevel optimization with lower-level minimization problems, often under strong convexity assumptions, and are not directly applicable to the minimax lower-level setting considered here....

---

### 18. STEPS: A Temporal Smooth Error Propagation Solver on the Manifolds for Test-Time Adaptation in Time Series Forecasting

**Authors:** Jiaqi Liu, Yifan Ouyang, Zhifei Song, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08005v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08005v1)

**Summary:** Test-Time Adaptation (TTA) aims to improve time series forecasting under distribution shifts by using limited observations revealed during inference. However, forecasting TTA must operate in a source-free online setting, where the adaptation signal is short, temporally correlated, and potentially noisy. Existing methods can therefore suffer from weak identifiability, error accumulation, and unstable long-horizon corrections when the revealed prefix is sparse or contaminated. To address these iss...

---

### 19. Graph-Structured Hyperdimensional Computing for Data-Efficient and Explainable Process-Structure-Property Prediction

**Authors:** Jingzhan Ge, Ajeeth Vellore, Ajinkya Palwe, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07999v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07999v1)

**Summary:** Multiphoton photoreduction enables high-fidelity fabrication of complex 3D microstructures, yet reliable process-structure-property (PSP) prediction remains difficult because the available data are sparse, heterogeneous, and interaction-dominated. In this regime, conventional feature-vector models are statistically underdetermined, making them prone to spurious correlations, poor regime transfer, and unstable post hoc explanations, whereas mechanistic pipelines depend on calibrated submodels tha...

---

### 20. Bayesian Sensitivity of Causal Inference Estimators under Evidence-Based Priors

**Authors:** Nikita Dhawan, Daniel Shen, Leonardo Cotta, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07993v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07993v1)

**Summary:** Causal inference, especially in observational studies, relies on untestable assumptions about the true data-generating process. Sensitivity analysis helps us determine how robust our conclusions are when we alter these underlying assumptions. Existing frameworks for sensitivity analysis are concerned with worst-case changes in assumptions. In this work, we argue that using such pessimistic criteria can often become uninformative or lead to conclusions contradicting our prior knowledge about the ...

---

### 21. Tool Calling is Linearly Readable and Steerable in Language Models

**Authors:** Zekun Wu, Ze Wang, Seonglae Cho, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07990v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07990v1)

**Summary:** When a tool-calling agent picks the wrong tool, the failure is invisible until execution: the email gets sent, the meeting gets missed. Probing 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B), we find the identity of the chosen tool is linearly readable and steerable inside the model. Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-10...

---

### 22. Where's the Plan? Locating Latent Planning in Language Models with Lightweight Mechanistic Interventions

**Authors:** Nicole Ma, Nick Rui

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07984v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07984v1)

**Summary:** We study planning site formation in language models -- where internal representations of structurally-constrained future tokens form during the forward pass, and whether they causally drive generation. Using rhyming-couplet completion as a clean test of forward-looking constraint, we apply two lightweight methods (linear probing and activation patching) across Qwen3, Gemma-3, and Llama-3 at more than ten scales. Probing shows that future-rhyme information is linearly decodable at the line bounda...

---

### 23. Susceptibilities and Patterning: A Primer on Linear Response in Bayesian Learning

**Authors:** Chris Elliott, Daniel Murfet

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07980v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07980v1)

**Summary:** These notes introduce the theory of susceptibilities as developed in [arXiv:2504.18274, arXiv:2601.12703] for interpreting neural networks. The susceptibility of an observable $φ$ to a data perturbation is defined as a derivative of a posterior expectation, which by the fluctuation--dissipation theorem equals a posterior covariance. Different choices of $φ$ yield different objects: per-sample losses give the influence matrix (the Bayesian influence function of [arXiv:2509.26544]), while componen...

---

### 24. Self-Play Enhancement via Advantage-Weighted Refinement in Online Federated LLM Fine-Tuning with Real-Time Feedback

**Authors:** Seohyun Lee, Wenzhi Fang, Dong-Jun Han, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07977v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07977v1)

**Summary:** Recent works have advanced feedback-based learning systems, whereby a foundation model is able to intake incoming feedback (e.g., a user) to self-improve, creating a self-loop system of training. However, existing works are limited in needing to consider an offline setup to allow for such feedback-based methods, and are further limited in the need of requiring privileged ground-truth contexts for training. Moreover, there is limited consideration of federated learning (FL), which is particularly...

---

### 25. It Just Takes Two: Scaling Amortized Inference to Large Sets

**Authors:** Antoine Wehenkel, Michael Kagan, Lukas Heinrich, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07972v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07972v1)

**Summary:** Neural posterior estimation has emerged as a powerful tool for amortized inference, with growing adoption across scientific and applied domains. In many of these applications, the conditioning variable is a set of observations whose elements depend not only on the target but also on unknown factors shared across the set. Optimal inference therefore requires treating the set jointly, which in turn requires training the estimator at the deployment set size -- a regime where memory and compute quic...

---

### 26. DVD: Discrete Voxel Diffusion for 3D Generation and Editing

**Authors:** Zhengrui Xiang, Jiaqi Wu, Fupeng Sun, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07971v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07971v1)

**Summary:** We introduce Discrete Voxel Diffusion (DVD), a discrete diffusion framework to generate, assess, and edit sparse voxels for SLat (Structured LATent) based 3D generative pipelines. Although discrete diffusion has not generally displaced continuous diffusion in image-like generation, we show that it can be an effective first-stage prior for sparse voxel scaffolds. By treating voxel occupancy as a native discrete variable, DVD avoids continuous-to-discrete thresholding and provides a simple framewo...

---

### 27. Linear Response Estimators for Singular Statistical Models

**Authors:** Chris Elliott, Daniel Murfet

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07970v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07970v1)

**Summary:** We define susceptibilities as a measure of the response of an observable quantity of a parameterized statistical model to a perturbation of the data for a general class of observables. We define estimators for these susceptibilities as statistics in a sequence of n data-points and prove that these estimators are consistent and asymptotically unbiased in the large n regime.

---

### 28. When Diffusion Model Can Ignore Dimension: An Entropy-Based Theory

**Authors:** Ahmad Aghapour, Erhan Bayraktar

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07969v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07969v1)

**Summary:** Diffusion models perform remarkably well on high-dimensional data such as images, often using only a modest number of reverse-time steps. Despite this practical success, existing convergence theory does not fully explain why such samplers remain efficient in high dimensions. Many prior KL guarantees bound the discretization error in terms of the ambient dimension, while other improved results replace this dependence using intrinsic-dimensional or geometric structure assumptions. In this work, we...

---

### 29. Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means

**Authors:** Valentin Kilian, Stefano Cortinovis, François Caron

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07964v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07964v1)

**Summary:** Confidence sequences based on test martingales provide time-uniform uncertainty quantification for the mean of bounded IID observations without parametric distributional assumptions. Their practical efficiency, however, depends strongly on the choice of martingale updates, and many existing constructions do not exploit prior information about plausible data-generating distributions or mean values. We propose a Bayes-assisted framework that uses a Bayesian working predictive model to adaptively c...

---

### 30. Aggregation in conformal e-classification

**Authors:** Vladimir Vovk

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07963v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07963v1)

**Summary:** Aggregating conformal predictors is a standard way of balancing their predictive and computational efficiency while retaining their validity, at least approximately. An important advantage of conformal e-predictors is that they are easier to aggregate without sacrificing their validity. This paper studies experimentally cross-conformal e-prediction, which is an existing method of aggregating conformal e-predictors, and its modifications that are conceptually simpler and more flexible.

---

### 31. FLAM: Evaluating Model Performance with Aggregatable Measures in Federated Learning

**Authors:** Fabian Stricker, Jose A. Peregrina, David Bermbach, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07962v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07962v1)

**Summary:** Performance evaluation is essential for assessing the quality of machine learning (ML) models and guiding deployment decisions. In federated learning (FL), assessing the performance is challenging because data are distributed across participants. Consequently, the coordinator must rely on locally computed evaluation metrics and aggregate them to assess the global model. A key challenge is that common aggregation strategies, such as weighted averaging based on the local samples per participant, d...

---

### 32. Graph Representation Learning Augmented Model Manipulation on Federated Fine-Tuning of LLMs

**Authors:** Hanlin Cai, Kai Li, Houtianfu Wang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07961v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07961v1)

**Summary:** Federated fine-tuning (FFT) has emerged as a privacy-preserving paradigm for collaboratively adapting large language models (LLMs). Built upon federated learning, FFT enables distributed agents to jointly refine a shared pretrained LLM by aggregating local LLM updates without sharing local raw data. However, FFT-based LLMs remain vulnerable to model manipulation threats, in which adversarial participants upload manipulated LLM updates that corrupt the aggregation process and degrade the performa...

---

### 33. Convergent Stochastic Training of Attention and Understanding LoRA

**Authors:** Zhengkai Sun, Dibyakanti Kumar, Alejandro F Frangi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07959v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07959v1)

**Summary:** Transformers have revolutionized machine learning and deploying attention layers in the model is increasingly standard across a myriad of applications. Further, for large models, it is common to implement Low Rank Adaptation (LoRA), whereby a factorized parameterization of them is trained, to achieve a surprisingly beneficial accuracy-size trade-off. In this work, via a unified framework we rigorously establish trainability of such models under stochastic methods. We prove that for any mild regu...

---

### 34. Slowly Annealed Langevin Dynamics: Theory and Applications to Training-Free Guided Generation

**Authors:** Atsushi Nitanda, Dake Bu, Yueming Lyu, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07950v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07950v1)

**Summary:** We study Slowly Annealed Langevin Dynamics (SALD), a sampler for tracking a path of moving target distributions and approximating the terminal target through time slowdown. We establish non-asymptotic convergence guarantees via a KL differential inequality, showing that slowdown improves tracking through contraction of intermediate targets and the complexity of the path. Motivated by training-free guided generation with pretrained score-based generative models, we further introduce Velocity-Awar...

---

### 35. Exploring the non-convexity in machine learning using quantum-inspired optimization

**Authors:** Kandula Eswara Sai Kumar, Parth Dhananjay Danve, Abhishek Chopra, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07947v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07947v1)

**Summary:** The escalating complexity of modern machine learning necessitates solving challenging non-convex optimization problems, particularly in high-dimensional regimes and scenarios contaminated by gross outliers. Traditional approaches, relying on convex relaxations or specialized local search heuristics, frequently succumb to suboptimal local minima and fail to recover the true underlying discrete structures. In this paper, we propose treating these non-convex challenges as a global search problem an...

---

### 36. TAVIS: A Benchmark for Egocentric Active Vision and Anticipatory Gaze in Imitation Learning

**Authors:** Giacomo Spigler

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07943v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07943v1)

**Summary:** Active vision -- where a policy controls its own gaze during manipulation -- has emerged as a key capability for imitation learning, with multiple independent systems demonstrating its benefits in the past year. Yet there is no shared benchmark to compare approaches or quantify what active vision contributes, on which task types, and under what conditions. We introduce TAVIS, evaluation infrastructure for active-vision imitation learning, with two complementary task suites -- TAVIS-Head (5 tasks...

---

### 37. Prototype Guided Post-pretraining for Single-Cell Representation Learning

**Authors:** Sachini Weerasekara, Natasha Darras, Sagar Kamarthi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07938v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07938v1)

**Summary:** Single-cell representation learning (SCRL) from gene expression data offers a way to uncover the complex regulatory logic underlying cellular function. Inspired by large language models in natural language modeling, several single-cell pretrained models have recently been proposed that treat genes as tokens and cells as sentences. However, these models are fundamentally limited by the long-tailed nature of cell-type distributions and struggle to generalize under covariate shifts in gene expressi...

---

### 38. INO-SGD: Addressing Utility Imbalance under Individualized Differential Privacy

**Authors:** Xiao Tian, Jue Fan, Rachael Hwee Ling Sim, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07930v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07930v1)

**Summary:** Differential privacy (DP) is widely employed in machine learning to protect confidential or sensitive training data from being revealed. As data owners gain greater control over their data due to personal data ownership, they are more likely to set their own privacy requirements, necessitating individualized DP (IDP) to fulfil such requests. In particular, owners of data from more sensitive subsets, such as positive cases of stigmatized diseases, likely set stronger privacy requirements, as leak...

---

### 39. Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation

**Authors:** Amin Karimi Monsefi, Dominic Culver, Nikhil Bhendawade, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07924v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07924v1)

**Summary:** Discrete flow matching generates text by iteratively transforming noise tokens into coherent language, but may require hundreds of forward passes. Distillation uses the multi-step trajectory to train a student to reproduce the process in a few steps. When the student underperforms, the usual explanation is insufficient capacity. We argue the opposite: the trajectory is the bottleneck, not the student. Each training trajectory is built through a chain of blind stochastic jumps with no evaluation ...

---

### 40. Tree SAE: Learning Hierarchical Feature Structures in Sparse Autoencoders

**Authors:** Tue M. Cao, Hoang X. Nhat, Raed Alharbi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07922v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07922v1)

**Summary:** Learning hierarchical features in Sparse Autoencoders (SAEs) is essential for capturing the structured nature of real-world data and mitigating issues like feature absorption or splitting. Existing works attempt to identify hierarchical relationships within independent feature sets by relying on activation coverage, the assumption that child feature should only activate when its parent feature activates. However, we demonstrate that this condition alone is insufficient; that is, it often produce...

---

### 41. Flatness and Gradient Alignment Are Both Necessary: Spectral-Aware Gradient-Aligned Exploration for Multi-Distribution Learning

**Authors:** Aristotelis Ballas, Christos Diou

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07914v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07914v1)

**Summary:** Sharpness-aware and gradient-alignment methods have been shown to improve generalization, however each family of methods targets a single geometric property of the loss landscape, while ignoring the other. In this paper, we show that this omission is structurally unavoidable and that both flatness and gradient alignment should be considered in multi-distribution learning settings. Specifically, we derive an excess-risk decomposition that yields two additive leading-order terms: (i) an alignment ...

---

### 42. Statistical inference with belief functions: A survey

**Authors:** Fabio Cuzzolin

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07908v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07908v1)

**Summary:** Belief functions are a powerful and popular framework for the mathematical characterisation of uncertainty, in particular in situations in which lack of data renders learning a probability distribution for the problem impractical. The first step in a reasoning chain based on belief functions is inference: how to learn a belief measure from the available data. In this survey we focus, in particular, on making inference from statistical data, and review the most significant contributions in the ar...

---

### 43. Consistency Regularised Gradient Flows for Inverse Problems

**Authors:** Alessio Spagnoletti, Tim Y. J. Wang, Marcelo Pereyra, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07907v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07907v1)

**Summary:** Vision-Language Latent Diffusion Models (LDMs) (Rombach et al., 2022) provide powerful generative priors for inverse problems. However, existing LDM-based inverse solvers typically require a large number of neural function evaluations (NFEs) and backpropagation through large pretrained components, leading to substantial computational costs and, in some cases, degraded reconstruction quality. We propose a unified Euclidean-Wasserstein-2 gradient-flow framework that jointly performs posterior samp...

---

### 44. Curvature Beyond Positivity: Greedy Guarantees for Arbitrary Submodular Functions

**Authors:** Yixin Chen, Alan Kuhnle

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07902v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07902v1)

**Summary:** Submodular functions -- functions exhibiting diminishing returns -- are central to machine learning. When the objective is monotone and non-negative, the greedy algorithm achieves a tight $63\%$ approximation. But many practical objectives incorporate costs that make them negative on some inputs, and all existing multiplicative guarantees require non-negativity. Prior work handles negativity through additive bounds for the special class of decomposable functions and non-monotonicity through part...

---

### 45. Adaptive Regularization for Sparsity Control in Bregman-Based Optimizers

**Authors:** Ahmad Aloradi, Tim Roith, Emanuël A. P. Habets, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07892v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07892v1)

**Summary:** Sparse training reduces the memory and computational costs of deep neural networks. However, sparse optimization methods, e.g., those adding an $\ell_1$ penalty, often control sparsity only indirectly through a regularization parameter $λ$, whose mapping to the final sparsity rate is non-trivial. In our experiments, we found this parameter sensitivity to be particularly pronounced for Bregman-based optimizers. Specifically, the two variants LinBreg and AdaBreg reach the same sparsity at $λ$ valu...

---

### 46. Enhancing Federated Quadruplet Learning: Stochastic Client Selection and Embedding Stability Analysis

**Authors:** Ozgu Goksu, Nicolas Pugeault

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07888v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07888v1)

**Summary:** Federated Learning (FL) enables decentralised model training across distributed clients without requiring data centralisation. However, the generalisation performance of the global model is usually degraded by data heterogeneity across clients, particularly under limited data availability and class imbalance. To address this challenge, we propose FedQuad, a novel method that explicitly enforces minimising intra-class representations while enabling inter-class splits across clients. By jointly mi...

---

### 47. Characterizing and Correcting Effective Target Shift in Online Learning

**Authors:** Ziyan Li, Naoki Hiratani

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07886v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07886v1)

**Summary:** Online learning from a stream of data is a defining feature of intelligence, yet modern machine learning systems often struggle in this setting, especially under distributional shift. To understand its basic properties, we study the relationship between online and offline learning in the context of kernel regression. We derive a closed-form expression for the function learned by online kernel regression, revealing that online kernel regression is equivalent to offline regression with shifted, in...

---

### 48. Black-box model classification under the discriminative factorization

**Authors:** Hayden Helm, Merrick Ohata, Carey Priebe

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07878v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07878v1)

**Summary:** Access to modern generative systems is often restricted to querying an API (the ``black-box" setting) and many properties of the system are unknown to the user at inference time. While recent work has shown that low-dimensional representations of models based on the relationship between their embedded responses to a set of queries are useful for inferring model-level properties, the quality of these representations is highly sensitive to the query set. We introduce the \emph{discriminative facto...

---

### 49. KL for a KL: On-Policy Distillation with Control Variate Baseline

**Authors:** Minjae Oh, Sangjun Song, Gyubin Choi, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07865v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07865v1)

**Summary:** On-Policy Distillation (OPD) has emerged as a dominant post-training paradigm for large language models, especially for reasoning domains. However, OPD remains unstable in practice due to the high gradient variance of its single-sample Monte Carlo estimator, and recipes for stable training are still immature. We propose vOPD (On-Policy Distillation with a control variate baseline), which casts OPD as policy-gradient RL and stabilizes it by introducing a control variate baseline-canonically a val...

---

### 50. ADKO: Agentic Decentralized Knowledge Optimization

**Authors:** Lucas Nerone Rillo, Zhanhong Jiang, Nastaran Saadati, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07863v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07863v1)

**Summary:** We present Agentic Decentralized Knowledge Optimization (ADKO), a framework for collaborative black-box optimization across autonomous agents that achieves sample efficiency, privacy preservation, heterogeneous-objective handling, and communication efficiency. Each agent maintains a private Gaussian Process (GP) surrogate trained on local data and communicates only through knowledge tokens-compact, lossy summaries containing directional signals, advantage scores, and optional language-model (LM)...

---

## cs.NE

**50 papers**

### 1. Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction

**Authors:** Himanshu Udupi, Xiaocong Yang, ChengXiang Zhai

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08022v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08022v1)

**Summary:** Spiking Neural Networks (SNNs) have been proposed as biologically plausible and energy-efficient alternatives to conventional Artificial Neural Networks (ANNs). However, the training of SNN usually relies on surrogate gradients due to the non-differentiability of the spike function, introducing approximation errors that accumulate across layers. To address this challenge, we extend the work on convexification of parallel feedforward threshold networks to parallel recurrent threshold networks, wh...

---

### 2. Broken-symmetry shape discrimination on a driven Duffing ring

**Authors:** Kaspar Anton Schindler

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07475v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07475v1)

**Summary:** Distributed computational substrates rely on two elementary operations: bundling, the act of populating a shared physical medium with independently retrievable components, and binding, the act of composing components into outputs whose identity depends on their relations. We study these two primitives on the simplest closed substrate carrying a continuous symmetry, a cycle graph of N nodes, in two parameter regimes of a single master equation of motion. The linear regime sorts a temporal input a...

---

### 3. Discovering Ordinary Differential Equations with LLM-Based Qualitative and Quantitative Evaluation

**Authors:** Sum Kyun Song, Bong Gyun Shin, Jae Yong Lee

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07323v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07323v1)

**Summary:** Discovering governing differential equations from observational data is a fundamental challenge in scientific machine learning. Existing symbolic regression approaches rely primarily on quantitative metrics; however, real-world differential equation modeling also requires incorporating domain knowledge to ensure physical plausibility. To address this gap, we propose DoLQ, a method for discovering ordinary differential equations with LLM-based qualitative and quantitative evaluation. DoLQ employs...

---

### 4. Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability

**Authors:** Dengzhe Hou, Zihao Wu, Lingyu Jiang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07212v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07212v1)

**Summary:** Electroencephalography (EEG) is a cornerstone of brain-computer interfaces and clinical neuroscience, yet deep learning models are typically trained and evaluated under a single, unreported preprocessing pipeline. We formalize preprocessing choices as a counterfactual intervention space and show that EEG predictions are surprisingly unstable under this space: across six datasets spanning four paradigms, up to 42% of trial-level predictions flip when only the preprocessing changes, a variability ...

---

### 5. Direct-to-Event Spiking Neural Network Transfer

**Authors:** Nhan Trong Luu, Duong Trung Luu, Pham Ngoc Nam, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07207v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07207v1)

**Summary:** Spiking Neural Networks (SNNs) have gained increasing attention due to their potential for low-power computation on neuromorphic hardware. A widely adopted training strategy for SNNs is direct coding, which enable backpropagation on neuron implementations using continuous-valued surrogate activations. However, recent studies have shown that direct-coded SNNs remain substantially less energy-efficient than their event-based counterparts, limiting their practical deployment in energy sensitive sce...

---

### 6. Every Feedforward Neural Network Definable in an o-Minimal Structure Has Finite Sample Complexity

**Authors:** Anastasis Kratsios, Gregory Cousins, Haitz Sáez de Ocáriz Borde, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07097v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07097v1)

**Summary:** We show that, in a precise sense, a broad class of feedforward neural networks learn (have finite sample complexity) in the PAC model: every fixed finite feedforward architecture whose layers are definable in an o-minimal structure has finite sample complexity in the agnostic PAC setting, even with unbounded parameters. This covers standard fixed-size MLPs, CNNs, GNNs, and transformers with fixed sequence length, together with the operations and layers typically used in such architectures, inclu...

---

### 7. A Unified Measure-Theoretic View of Diffusion, Score-Based, and Flow Matching Generative Models

**Authors:** Aditya Ranganath, Mukesh Singhal

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06829v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06829v1)

**Summary:** We survey continuous-time generative modeling methods based on transporting a simple reference distribution to a data distribution via stochastic or deterministic dynamics. We present a unified framework in which diffusion models, score-based generative models, and flow matching are instances of learning a time-dependent vector field that induces a family of marginals $(ρ_t)_{t \in [0,1]}$ governed by continuity and Fokker-Planck equations. Such a unified theory is timely because these methods a...

---

### 8. The Causally Emergent Alignment Hypothesis: Causal Emergence Aligns with and Predicts Final Reward in Reinforcement Learning Agents

**Authors:** Federico Pigozzi, Michael Levin

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06746v1)

**Summary:** A hallmark of life on Earth is the ability of agents to exert causal power and be drivers of subsequent events. This is key to cognition at all scales. Causal emergence, measuring the degree to which an agent exerts unique predictive power on its future, is one consequence of causal power. Indeed, recent discoveries have shown that biological agents, even minimal ones, increase their causal emergence after learning new memories. However, there is a major knowledge gap regarding how causally emer...

---

### 9. CoupleEvo: Evolving Heuristics for Coupled Optimization Problems Using Large Language Models

**Authors:** Thomas Bömer, Bastian Amberg, Max Disselnmeyer, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06341v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06341v1)

**Summary:** Many real-world optimization problems consist of multiple tightly coupled subproblems whose solutions must be coordinated to achieve high overall performance. However, existing large language model driven automated heuristic design approaches are limited to single-problem settings. In this paper, we propose CoupleEvo. CoupleEvo proposes three evolutionary coordination strategies to evolve heuristics for coupled optimization problems: the sequential strategy evolves heuristics for one subproblem ...

---

### 10. Efficient event-driven retrieval in high-capacity kernel Hopfield networks

**Authors:** Akira Tamamori

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05978v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05978v1)

**Summary:** High-capacity associative memory models, such as Kernel Logistic Regression (KLR) Hopfield networks, have demonstrated strong storage capabilities but typically rely on computationally expensive synchronous updates. This reliance poses a bottleneck for deployment on energy-efficient, event-driven neuromorphic hardware. In this paper, we investigate the asynchronous retrieval dynamics of KLR Hopfield networks. We show empirically that, under appropriately tuned kernel parameters, asynchronous seq...

---

### 11. MDN: Parallelizing Stepwise Momentum for Delta Linear Attention

**Authors:** Yulong Huang, Xiang Liu, Hongxiang Huang, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05838v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05838v1)

**Summary:** Linear Attention (LA) offers a promising paradigm for scaling large language models (LLMs) to long sequences by avoiding the quadratic complexity of self-attention. Recent LA models such as Mamba2 and GDN interpret linear recurrences as closed-form online stochastic gradient descent (SGD), but naive SGD updates suffer from rapid information decay and suboptimal convergence in optimization. While momentum-based optimizers provide a natural remedy, they pose challenges in simultaneously achieving ...

---

### 12. Graph Normalization: Fast Binarizing Dynamics for Differentiable MWIS

**Authors:** Laurent Guigues

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05330v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05330v1)

**Summary:** We introduce Graph Normalization (GN), a principled dynamical system on graphs that serves as a differentiable approximation engine for the NP-hard Maximum Weight Independent Set (MWIS) problem. MWIS encompasses many combinatorial challenges, including optimal assignment, scheduling, set packing, and MAP inference in discrete Markov Random Fields. Unlike Belief Propagation, we prove GN always converges to a binary indicator of a Maximum Independent Set. GN realizes a fast quasi-Newton descent th...

---

### 13. S-LCG: Structured Linear Congruential Generator-Based Deterministic Algorithm for Search and Optimization

**Authors:** Ahmed Qasim Mohammed, Haider Banka, Anamika Singh

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05198v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05198v1)

**Summary:** This study presents a novel deterministic optimization algorithm based on a special variant of the Linear Congruential Generator (LCG). While conventional algorithms generally operate within the search space, the introduced technique follows a two-level architecture. In particular, an external loop that adaptively balances between exploration and exploitation, while the internal loop evaluates solutions. It is motivated by the intrinsic structure of the generator, the reason behind naming it the...

---

### 14. Direct From Darwin: Deriving Advanced Optimizers From Evolutionary First Principles

**Authors:** Daniel Grimmer

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05284v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05284v1)

**Summary:** Evolutionary computation has long promised to deliver both high-performance optimization tools as well as rigorous scientific simulations of Darwinian evolution. However, modern algorithms frequently abandon evolutionary fidelity for physics-inspired heuristics or superficial biological metaphors. This paper derives a suite of advanced gradient-based optimization algorithms directly from evolutionary first principles. We introduce Darwinian Lineage Simulations (DLS) to prove that, in an asexual ...

---

### 15. On the Influence of the Feature Computation Budget on Per-Instance Algorithm Selection for Black-Box Optimization

**Authors:** Koen van der Blom, Diederick Vermetten

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04954v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04954v1)

**Summary:** Per-instance algorithm selection (PIAS) takes advantage of complementarity between a set of algorithms by deciding which algorithm to run on a given instance. This decision is based on features of the instances, which, in the context of black-box optimization (BBO), require a part of the optimization budget to be computed. This raises two questions: (a) from which fraction of the budget spent on feature computation does PIAS become worth it for BBO, and (b) which fraction of the budget optimizes...

---

### 16. DALight-3D: A Lightweight 3D U-Net for Brain Tumor Segmentation from Multi-Modal MRI

**Authors:** Nand Kumar Mishra, Dhruv Mishra, Dr Manu Pratap Singh

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04518v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04518v1)

**Summary:** Automatic brain tumor segmentation from multi-modal MRI remains challenging because volumetric models often incur substantial computational cost. This paper presents DALight-3D, a compact 3D U-Net variant that combines depthwise separable 3D convolutions, identifier-conditioned normalization, cross-slice attention, and adaptive skip fusion. The method is evaluated on the Medical Segmentation Decathlon Task01 BrainTumour benchmark under matched optimization settings against standard 3D U-Net, Att...

---

### 17. Interpreting V1 Population Activity via Image-Neural Latent Representation Alignment

**Authors:** Xin Wang, Zhuangzhi Gao, Hongyi Qin, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04309v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04309v1)

**Summary:** Understanding the neural mechanisms underlying visual computation has long been a central challenge in neuroscience. Recent alignment based approaches have improved the accuracy of decoding visual stimuli from brain activity, yet they provide limited insight into the neural computations that give rise to these improvements. To address this gap, we propose Dual-Tower Image-Neural Alignment (DINA), an interpretable contrastive framework for analyzing population level visual computations in primary...

---

### 18. QUIVER: Cost-Aware Adaptive Preference Querying in Surrogate-Assisted Evolutionary Multi-Objective Optimization

**Authors:** Florian A. D. Burnat

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04267v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04267v1)

**Summary:** Interactive multi-objective optimization systems face a budget allocation dilemma: one can spend resources on expensive objective evaluations or on eliciting decision-maker preferences that identify the relevant region of the Pareto set. Moreover, preference elicitation itself spans modalities with different information content and cognitive burden, ranging from cheap, noisy pairwise preference statements (PS) to richer but costlier indifference adjustments (IA).   We study cost-aware optimizati...

---

### 19. phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks

**Authors:** Stefan Fischer, Maliheh Hariri, Sebastian Otte

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04256v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04256v1)

**Summary:** Physical neural networks (PNNs) embed computation directly in material dynamics, including molecular, chemical, biological, photonic, memristive, and mechanical substrates. They are attractive for edge computing, especially at the extreme edge, where computation can be placed at the interface to sensing, actuation, or the physical process itself. However, PNNs are difficult to integrate into edge-cloud software stacks because each substrate exposes distinct interfaces, timing behavior, observabi...

---

### 20. Exact and Evolutionary Algorithms for Sequential Multi-Objective Transmission Topology Planning

**Authors:** Job Groeneveld, Miguel Muñoz, Jan Viebahn, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03753v1) | 📄 [PDF](https://arxiv.org/pdf/2605.03753v1)

**Summary:** We address day-ahead transmission topology planning and congestion management as a sequential, multi-objective optimization problem and develop two complementary algorithms for it: an exact enumeration method and a tailored evolutionary heuristic. The problem is formulated with four operational objectives reflecting real TSO decision criteria: worst-case line loading under $N-1$ security, topological depth, number of switching actions, and time spent in non-reference topologies, over a 24-hour h...

---

### 21. Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Computation in Neural Networks

**Authors:** Jatin Sharma, Dan F. M Goodman, Danyal Akarca

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03598v2) | 📄 [PDF](https://arxiv.org/pdf/2605.03598v2)

**Summary:** Understanding how biological and artificial neural networks implement computation from connectivity is a central problem in neuroscience and machine learning. In neural systems, structural and functional connectivity are known to diverge, motivating approaches that move beyond direct connections alone. Here, we show that the spatial and temporal function of recurrent neural networks (RNNs) trained on hierarchically modular tasks can be recovered by modelling the network as a graph and analysing ...

---

### 22. Symmetry-Protected Lyapunov Neutral Modes in Equivariant Recurrent Networks

**Authors:** Hanson Hanxuan Mo

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03338v1) | 📄 [PDF](https://arxiv.org/pdf/2605.03338v1)

**Summary:** Recurrent networks that store position, phase, or other continuous variables need state-space directions that remain neutral over long horizons. We give a symmetry-based account of when such neutral directions are guaranteed rather than merely tuned. For a finite-dimensional autonomous \(C^1\) vector field equivariant under a Lie group \(G\), we prove that any compact invariant set carrying a uniformly nondegenerate group-orbit bundle with stabilizer type \(H\) has, at points where the Lyapunov ...

---

### 23. Neuromorphic Control for 3D Navigation in Minecraft Using Genetic Algorithms

**Authors:** Eric Zipor

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02628v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02628v1)

**Summary:** The popular 2009 voxel based videogame, Minecraft, contains several distinct disciplines. One of which is "parkour," gameplay that focuses on traversing a world's environment with maximum efficiency. The Minecraft online community has turned the game's physics engine into dynamic puzzles, requiring players to masterfully manipulate motion mechanics through frame precise timing of keystrokes. Actions such as sprinting, sneaking, and mouse direction are all combined to clear specific difficult jum...

---

### 24. MPCS: Neuroplastic Continual Learning via Multi-Component Plasticity and Topology-Aware EWC

**Authors:** Joern Hentsch

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02509v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02509v1)

**Summary:** Continual learning systems face a fundamental tension between plasticity -- acquiring new knowledge  --  and stability  --  retaining prior knowledge. We introduce MPCS (Multi-Plasticity Continual System), a neuroplastic architecture that integrates eleven complementary mechanisms: task-driven neurogenesis, Fourier-encoded inputs, EWC regularization, meta-replay, mixed consolidation, hybrid gating, synapse pruning/regeneration, Hebbian updates, task similarity routing, adaptive growth control, a...

---

### 25. Combining Trained Models in Reinforcement Learning

**Authors:** Ujjwal Patil, Javad Ghofrani

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02159v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02159v1)

**Summary:** Deep reinforcement learning (DRL) has delivered strong results in domains such as Atari and Go, but it still suffers from high sample cost and weak transfer beyond the training setting. A common response is to reuse information from previously trained models through transfer, distillation, ensemble methods, or federated training instead of learning each target task from random initialization. The literature on these mechanisms is fragmented, and published comparisons are hard to interpret becaus...

---

### 26. HERCULES: Hardware-Efficient, Robust, Continual Learning Neural Architecture Search

**Authors:** Matteo Gambella, Fabrizio Pittorino, Manuel Roveri

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.04103v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04103v1)

**Summary:** Neural Architecture Search (NAS) has emerged as a powerful framework for automatically discovering neural architectures that balance accuracy and efficiency. However, as AI transitions from static benchmarks to real-world deployment, the traditional focus on hardware-aware efficiency is no longer sufficient. We observe that modern NAS methods, especially those that target edge AI, are evolving to address a triple objective: Efficiency, Robustness, and Continual Learning. While efficiency ensures...

---

### 27. SNNF: An SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors

**Authors:** Yahan Yang, Pradeep Kumar Gopalakrishnan, Chang Chip Hong, et al.

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01937v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01937v1)

**Summary:** Dynamic Vision Sensors (DVS) exhibit exceptional dynamic range and low power consumption, making them ideal for edge applications in the Internet of Video Things (IoVT). However, their output is often degraded by spurious Background Activity (BA) noise, leading to unnecessary computational overhead. This paper proposes SNNF, a near-sensor BA noise filter that integrates a compact Event-Based Binary Image (EBBI) representation, a parallel memory architecture, and a single-layer Spiking Neural Net...

---

### 28. Training Non-Differentiable Networks via Optimal Transport

**Authors:** An T. Le

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01928v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01928v1)

**Summary:** Neural networks increasingly embed non-differentiable components (spiking neurons, quantized layers, discrete routing, blackbox simulators, etc.) where backpropagation is inapplicable and surrogate gradients introduce bias. We present PolyStep, a gradient-free optimizer that updates parameters using only forward passes. Each step evaluates the loss at structured polytope vertices in a compressed subspace, computes softmax-weighted assignments over the resulting cost matrix, and displaces particl...

---

### 29. ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization

**Authors:** Kaiwen Tang, Di Yu, Jiaqi Zheng, et al.

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01866v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01866v1)

**Summary:** Spiking neural networks (SNNs) are promising for edge sensing due to their event-driven computation and temporal filtering capability. However, standard leaky integrate-and-fire (LIF) neurons communicate only through binary spikes, which severely limit representational capacity. Existing multi-level spiking neurons improve information transmission, but often rely on uniform quantization that mismatches membrane-potential distributions or introduces costly synaptic multiplications. In this paper,...

---

### 30. Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance

**Authors:** Anamika Paul Rupa, Anietie Andy

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01699v3) | 📄 [PDF](https://arxiv.org/pdf/2605.01699v3)

**Summary:** Recent attacks show that behavioural unlearning of large language models leaves internal traces recoverable by adversarial probes. We characterise where this retention lives and show it can be surgically removed without measurable capability cost. Our central protocol is a leave-one-out cross-sequence probe that tests whether a memorisation signature generalises across held-out sequences. The signature is real and consistent across scale: memorisation-specific gaps of +0.32, +0.19, +0.30 on Pyth...

---

### 31. Benchmarking local Hebbian learning rules for memory storage and prototype extraction

**Authors:** Anders Lansner, Andreas Knoblauch, Naresh B Ravichandran, et al.

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.01074v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01074v1)

**Summary:** Associative memory or content-addressable memory is an important component function in computer science and information processing, and at the same time a key concept in cognitive and computational brain science. Many different neural network architectures and learning rules have been proposed to model the brain's associative memory while investigating key component functions like figure-ground segmentation, perceptual reconstruction and rivalry. A less investigated but equally important capabil...

---

### 32. Robust volatility updates for Hierarchical Gaussian Filtering

**Authors:** Christoph Mathys, Nicolas Legrand, Peter Thestrup Waade, et al.

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00966v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00966v1)

**Summary:** Hierarchical Gaussian Filtering (HGF) networks allow for efficient updating of posterior distributions (beliefs) about hidden states of an agent's environment. HGF parent nodes can target the mean or variance of their children. New information entering at input nodes leads to a cascade of belief updates across the network according to one-step update equations for each node's mean and precision (inverse variance). However, the original form of the update equations for variance-targeting parents(...

---

### 33. Learning to Act and Cooperate for Distributed Black-Box Consensus Optimization

**Authors:** Zi-Bo Qin, Feng-Feng Wei, Tai-You Chen, et al.

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00691v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00691v1)

**Summary:** Distributed blackbox consensus optimization is a fundamental problem in multi-agent systems, where agents must improve a global objective using only local objective queries and limited neighbor communication. Existing methods largely rely on handcrafted update rules and static cooperation patterns, which often struggle to balance local adaptation, global coordination, and communication efficiency in heterogeneous nonconvex environments. In this paper, we take an initial step toward trajectory-dr...

---

### 34. Spiking Sequence Machines and Transformers

**Authors:** Joy Bose

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00662v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00662v1)

**Summary:** Sequence learning reduces to similarity-based retrieval over a temporally indexed representation space, a constraint on any sequence model, not a property of a specific architecture. We show that a spiking Sparse Distributed Memory sequence machine (2007) and the transformer (2017) independently instantiate the same five functional operations (encoding, context maintenance, associative retrieval, storage, and decoding), with cosine similarity as the shared retrieval primitive in both. We formali...

---

### 35. Affinity Is Not Enough: Recovering the Free Energy Principle in Mixture-of-Experts

**Authors:** Man Yung Wong

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00604v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00604v1)

**Summary:** Sparse MoE routing fails at domain transitions, where the current token belongs to one distribution and the next to another. In a controlled experiment (4 experts, 5 seeds), standard affinity routing assigns only 0.006 +/- 0.001 probability to the correct expert at the transition. Three lightweight gate modifications raise this to 0.748 +/- 0.002 (124x), cutting experts needed for 99% coverage from infeasible to a small constant: temporal memory (beta), a per-expert LIF membrane potential accumu...

---

### 36. Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation

**Authors:** Bo Tang, Weiwei Xie

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00402v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00402v1)

**Summary:** Spiking Neural Networks (SNNs) provide a promising framework for energy-efficient and biologically grounded computation; however, scalable learning in deep recurrent architectures with sparse connectivity remains a major challenge. In this work, we propose a structured multi-layer recurrent SNN architecture composed of locally dense recurrent layers augmented with sparse small-world long-range projections to a readout population. The long-range connectivity is largely fixed, preserving routing e...

---

### 37. Geometric and dynamical analysis of attractor boundaries and storage limits in kernel Hopfield networks

**Authors:** Akira Tamamori

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00366v2) | 📄 [PDF](https://arxiv.org/pdf/2605.00366v2)

**Summary:** High-capacity associative memories based on Kernel Logistic Regression (KLR) exhibit strong storage capabilities, but the dynamical and geometric mechanisms underlying their stability remain poorly understood. This paper investigates the global geometry of attractor basins and the mechanisms governing the storage limit in KLR-trained Hopfield networks. We combine empirical evaluations using random sequences and real-world image embeddings (CIFAR-10) with morphing experiments and statistical Sign...

---

### 38. NeuroRing: Scaling Spiking Neural Networks via Multi-FPGA Bidirectional Ring Topologies and Stream-Dataflow Architectures

**Authors:** Muhammad Ihsan Al Hafiz, Artur Podobas

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.28059v1) | 📄 [PDF](https://arxiv.org/pdf/2604.28059v1)

**Summary:** Spiking neural networks (SNNs) are a promising paradigm for energy-efficient event-driven computation, but large-scale SNN execution remains challenging because sparse spike communication and synchronization can dominate runtime. Existing solutions across CPU, GPU, ASIC, and FPGA platforms offer different trade-offs between programmability, efficiency, and scalability. To address this gap, we present NeuroRing, a modular and scalable SNN accelerator based on a stream-dataflow architecture and a ...

---

### 39. Attractor FCM

**Authors:** Alexis Kafantaris

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.27947v2) | 📄 [PDF](https://arxiv.org/pdf/2604.27947v2)

**Summary:** In this paper an attractor FCM is created, tested, and analyzed. This FCM is neither a hebbian based nor agentic, nor a hybrid; it rather is a gradient descent based, physics constrained, Jacobian version of an FCM. Moreover, this model has several quirks; it uses residual memory, back propagation through time, and a fixed point anchor that is recursively implemented to update its weights. The residuals update the recursive part without losing the system memory. The model's anchor enables it to ...

---

### 40. Physical Foundation Models: Fixed hardware implementations of large-scale neural networks

**Authors:** Logan G Wright, Tianyu Wang, Tatsuhiro Onodera, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.27911v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27911v1)

**Summary:** Foundation models are deep neural networks (such as GPT-5, Gemini~3, and Opus~4) trained on large datasets that can perform diverse downstream tasks -- text and code generation, question answering, summarization, image classification, and so on. The philosophy of foundation models is to put effort into a single, large (${\sim}10^{12}$-parameter) general-purpose model that can be adapted to many downstream tasks with no or minimal additional training. We argue that the rise of foundation models p...

---

### 41. When Does Structure Matter in Continual Learning? Dimensionality Controls When Modularity Shapes Representational Geometry

**Authors:** Kathrin Korte, Joachim Winter Pedersen, Eleni Nisioti, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.27656v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27656v1)

**Summary:** To preserve previously learned representations, continual learning systems must strike a balance between plasticity, the ability to acquire new knowledge, and stability. This stability-plasticity dilemma affects how representations can be reused across tasks: shared structure enables transfer when tasks are similar but may also induce interference when new learning disrupts existing representations. However, it remains unclear when and why structural separation influences this trade-off. In this...

---

### 42. UniBCI: Towards a Unified Pretrained Model for Invasive Brain-Computer Interfaces

**Authors:** Binjie Hong, Rui Xiong, Liyuan Han, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2605.00061v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00061v1)

**Summary:** Modeling invasive neural spike data is fundamental to advancing high-performance brain-computer interfaces (BCIs). However, existing approaches face critical challenges, including limited-scale heterogeneous data, cross-domain distribution shift, and the intrinsic spatiotemporal complexity of invasive neural signals. In this work, we propose UniBCI, a unified pretrained model for invasive Brain-Computer Interfaces. The model integrates three key components: (1) a context-conditioned spatio-tempo...

---

### 43. Relation Reasoning with LLMs in Expensive Optimization

**Authors:** Ye Lu, Bingdong Li, Aimin Zhou, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2605.02933v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02933v1)

**Summary:** Expensive optimization problems (EOPs) are black-box tasks with costly objective evaluations and no gradient access, making the evaluation budget the key bottleneck. Surrogate-assisted evolutionary algorithms (SAEAs) reduce evaluations via surrogate predictions, but conventional surrogates often require frequent retraining as populations evolve, incurring overhead. This paper proposes R2SAEA, a reinforcement-trained relation-based large language model (LLM) surrogate assisted evolutionary algori...

---

### 44. RCMAES: A Robust CMA-ES Variant for CEC2026 Competition

**Authors:** Khoirul Faiq Muzakka, Sören Möller, Martin Finsterbusch

**Published:** 2026-04-29

🔗 [Paper](http://arxiv.org/abs/2604.27138v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27138v1)

**Summary:** This paper proposes RCMAES, a novel variant of the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) for CEC benchmark optimization. RCMAES integrates a dimension-dependent nonlinear population-size reduction strategy with an adaptive restart mechanism within a pure CMA-ES framework. RCMAES is evaluated on three benchmark suites (CEC2017, CEC2020, and CEC2022) and compared with state-of-the-art DE algorithms as well as its closely related counterpart, BIPOP-aCMAES. Experimental results sh...

---

### 45. Learning to Forget: Continual Learning with Adaptive Weight Decay

**Authors:** Aditya A. Ramesh, Alex Lewandowski, Jürgen Schmidhuber

**Published:** 2026-04-29

🔗 [Paper](http://arxiv.org/abs/2604.27063v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27063v1)

**Summary:** Continual learning agents with finite capacity must balance acquiring new knowledge with retaining the old. This requires controlled forgetting of knowledge that is no longer needed, freeing up capacity to learn. Weight decay, viewed as a mechanism for forgetting, can serve this role by gradually discarding information stored in the weights. However, a fixed scalar weight decay drives this forgetting uniformly over time and uniformly across all parameters, even when some encode stable knowledge ...

---

### 46. Causal Learning with Neural Assemblies

**Authors:** Evangelia Kopadi, Dimitris Kalles

**Published:** 2026-04-29

🔗 [Paper](http://arxiv.org/abs/2604.26919v1) | 📄 [PDF](https://arxiv.org/pdf/2604.26919v1)

**Summary:** Can Neural Assemblies -- groups of neurons that fire together and strengthen through co-activation -- learn the direction of causal influence between variables? While established as a computationally general substrate for classification, parsing, and planning, neural assemblies have not yet been shown to internalize causal directionality. We demonstrate that the inherent operations of neural assemblies -- projection, local plasticity control, and sparse winner selection -- are sufficient for dir...

---

### 47. Population Dynamics in ARIEL Robotics Systems Featuring Embodied Evolution via Spatial Mating Mechanisms

**Authors:** Victoria Peterson, Akshat Srivastava, Raghav Prabhakar

**Published:** 2026-04-29

🔗 [Paper](http://arxiv.org/abs/2604.26822v1) | 📄 [PDF](https://arxiv.org/pdf/2604.26822v1)

**Summary:** We present a Spatially Embedded Evolutionary Algorithm where robot individuals exist in a physically simulated 2D environment, must navigate to encounter potential mates, and compete for survival under various spatially-aware selection pressures. Using HyperNEAT evolved neural controllers for ARIEL gecko-inspired quadrupeds in MuJoCo, we investigate how spatial structure fundamentally alters evolutionary dynamics. Our experiments show a modest 4.9% difference in peak fitness between proximity-ba...

---

### 48. NORACL: Neurogenesis for Oracle-free Resource-Adaptive Continual Learning

**Authors:** Karthik Charan Raghunathan, Christian Metzner, Laura Kriener, et al.

**Published:** 2026-04-29

🔗 [Paper](http://arxiv.org/abs/2604.27031v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27031v1)

**Summary:** In a continual learning setting, we require a model to be plastic enough to learn a new task and stable enough to not disturb previously learned capabilities. We argue that this dilemma has an architectural root. A finite network has limited representational and plastic resources, yet the required capacity depends on properties of the future task stream that are unknown: how many tasks will be encountered, and how much they overlap in feature space. Regularization-based methods preserve past kno...

---

### 49. Evolutionary feature selection for spiking neural network pattern classifiers

**Authors:** Michal Valko, Nuno C. Marques, Marco Castelani

**Published:** 2026-04-29

🔗 [Paper](http://arxiv.org/abs/2604.26654v1) | 📄 [PDF](https://arxiv.org/pdf/2604.26654v1)

**Summary:** This paper presents an application of the biologically realistic JASTAP neural network model to classification tasks. The JASTAP neural network model is presented as an alternative to the basic multi-layer perceptron model. An evolutionary procedure previously applied to the simultaneous solution of feature selection and neural network training on standard multi-layer perceptrons is extended with JASTAP model. Preliminary results on IRIS standard data set give evidence that this extension allows...

---

### 50. Text-Utilization for Encoder-dominated Speech Recognition Models

**Authors:** Albert Zeyer, Tim Posielek, Ralf Schlüter, et al.

**Published:** 2026-04-29

🔗 [Paper](http://arxiv.org/abs/2604.26514v1) | 📄 [PDF](https://arxiv.org/pdf/2604.26514v1)

**Summary:** This paper investigates efficient methods for utilizing text-only data to improve speech recognition, focusing on encoder-dominated models that facilitate faster recognition. We provide a comprehensive comparison of techniques to integrate text-only data, including modality matching and dynamic downsampling to reach text-level representations within the encoder. Our experiments on the LibriSpeech corpus show that a larger encoder with a smaller decoder can equal or surpass the performance of arc...

---

## q-bio.NC

**50 papers**

### 1. Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners

**Authors:** Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08019v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08019v1)

**Summary:** Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match hu...

---

### 2. Dynamical mechanisms of flexible phase-locking in cortical theta oscillators

**Authors:** Yangyang Wang, Benjamin R. Pittman-Polletta

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08014v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08014v1)

**Summary:** Oscillatory activity in auditory cortex is thought to play a central role in auditory and speech processing by synchronizing neural rhythms to external acoustic features of the speech stream. To support this function, cortical oscillators must flexibly phase-lock to inputs spanning a wide range of timescales, including rhythms substantially slower than their intrinsic frequency. Here we identify a general dynamical mechanism by which intrinsic inhibitory currents operating on multiple timescales...

---

### 3. Learning Cross-Atlas Consistent Brain Disorder Representations via Disentangled Multi-Atlas Functional Connectivity Learning

**Authors:** Minheng Chen, Chao Cao, Jing Zhang, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.07026v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07026v1)

**Summary:** Functional connectivity (FC) derived from resting-state fMRI is widely used to characterize large-scale brain network alterations in neurological and psychiatric disorders. However, FC construction critically depends on the choice of brain atlas, and different parcellations may emphasize distinct organizational features, leading to heterogeneous and sometimes inconsistent representations. Existing multi-atlas approaches partially alleviate this issue but often fuse atlas-derived features or pred...

---

### 4. Partitioning Neural Co-Variability

**Authors:** Skyler Thomas, Brandon J. Zhu, Kathleen E. Cullen, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06995v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06995v1)

**Summary:** Trial-to-trial variability of neural responses has been linked to important aspects of neural computation and is essential for understanding how neuronal populations respond. While current overdispersion models treat each neuron's gain as independent of each other, this assumption fails to capture the network statistics of neuronal populations. As no existing model can capture overdispersed structured spiking gain-modulation across a neural population, network-level gain covariance remains large...

---

### 5. Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?

**Authors:** Yukiyasu Kamitani

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06420v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06420v1)

**Summary:** Brain-DNN alignment is usually assessed through stimulus-level correspondence or stimulus-set geometry. Inspired by category theory, we operationalize a different question: do brain and model preserve the same candidate transformations among stimuli? We formalize this as approximate naturality: if a proxy-defined stimulus change is propagated through the brain side and then translated to the model side, the result should match translating first and then propagating, so that the naturality square...

---

### 6. A multi-scale information geometry reveals the structure of mutual information in neural populations

**Authors:** Simone Azeglio, Steeve Laquitaine, Ulisse Ferrari, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06304v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06304v1)

**Summary:** Understanding how neural population responses represent sensory information is a central problem in systems neuroscience. One approach is to define a representational geometry on stimulus space in which distances reflect how reliably stimuli can be distinguished from neural activity. However, different constructions of these distances can lead to qualitatively different conclusions about the neural code. Here, we show that a unique Riemannian representational geometry emerges from first principl...

---

### 7. Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience

**Authors:** Johannes Bertram, Luciano Dyballa, T. Anderson Keller, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.05907v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05907v1)

**Summary:** Decoding approaches are widely used in neuroscience and machine learning to compare stimulus representations across neural systems, such as different brain regions, organisms, and deep learning models. Popular methods include decoding (perceptual) manifolds and alignment metrics such as Representational Similarity Analysis (RSA) and Dynamic Similarity Analysis (DSA), where similarity in decoding representations is interpreted as evidence for similar computation. This paper demonstrates a fundame...

---

### 8. Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior

**Authors:** Hanbo Xie, Akshay K. Jagadish, Lan Pan, et al.

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.05091v1) | 📄 [PDF](https://arxiv.org/pdf/2605.05091v1)

**Summary:** Computational cognitive models discovered using large language models have so far relied solely on behavioral data. However, it is well-known that models produced from the behavioral trajectory alone are typically under-determined. In this work, we explore the use of Think Aloud traces as an additional form of data constraint during automated model discovery. When applied to the domain of risky decision-making, we find that the models discovered with think-aloud achieve significantly improved pr...

---

### 9. A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions

**Authors:** Alessio Basti, Rikkert Hindriks, Ruggero Freddi, et al.

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04636v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04636v1)

**Summary:** Cross-frequency interactions are fundamental brain mechanisms for integrating information across temporal scales. However, accurate identification of these couplings is hindered by complex multi-frequency nonlinearities and by spurious, zero-lag artifacts caused by volume conduction. To our knowledge, conventional metrics lack a robust framework to characterize genuine interactions among multiple time series where a frequency of interest $f_N$ arises from the combination of $N-1$ components such...

---

### 10. Dissociating spatial frequency reliance from adversarial robustness advantages in neurally guided deep convolutional neural networks

**Authors:** Zhenan Shao, Tianyu Ren, Chengxiao Wang, et al.

**Published:** 2026-05-06

🔗 [Paper](http://arxiv.org/abs/2605.04443v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04443v1)

**Summary:** Deep convolutional neural networks (DCNNs) have rivaled humans on many visual tasks, yet they remain vulnerable to near-imperceptible perturbations generated by adversarial attacks. Recent work shows that aligning DCNN representations with human visual cortex activity improves adversarial robustness, but the mechanisms driving this advantage are unclear. One hypothesis suggests that neural alignment confers robustness by biasing models away from brittle high-frequency details and towards the low...

---

### 11. A foundation model of vision, audition, and language for in-silico neuroscience

**Authors:** Stéphane d'Ascoli, Jérémy Rapin, Yohann Benchetrit, et al.

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04326v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04326v1)

**Summary:** Cognitive neuroscience is fragmented into specialized models, each tailored to specific experimental paradigms, hence preventing a unified model of cognition in the human brain. Here, we introduce TRIBE v2, a tri-modal (video, audio and language) foundation model capable of predicting human brain activity in a variety of naturalistic and experimental conditions. Leveraging a unified dataset of over 1,000 hours of fMRI across 720 subjects, we demonstrate that our model accurately predicts high-re...

---

### 12. Neural Manifolds as Crystallized Embeddings: A Synthesis of the Free Energy Principle, Generalized Synchronization, and Hebbian Plasticity

**Authors:** Vikas N. O'Reilly-Shah

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04200v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04200v1)

**Summary:** The free energy principle casts perception as variational inference, but its biological implementation remains underspecified. In particular, the generalized-coordinate formalism should not be read as a literal claim that neurons compute arbitrary Taylor expansions. This paper argues that generalized synchronization provides the missing bottom-up mechanism. A contractive recurrent circuit driven by structured sensory input can synchronize to the driving dynamics. Under generic embedding conditio...

---

### 13. Cusped singularities organize mixed-mode oscillations in mutually inhibitory slow-fast systems

**Authors:** Morten Gram Pedersen

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.03606v1) | 📄 [PDF](https://arxiv.org/pdf/2605.03606v1)

**Summary:** Mutual inhibition is a common motif in neural systems. Here, we establish that cusped singularities - folded singularities located at cusp points of critical manifolds - provide a universal organizing mechanism for mixed-mode oscillations (MMOs) in coupled slow-fast systems with mutual inhibition. We show that the geometric setup of these systems generically satisfies the conditions required by established geometric singular perturbation theory and blow-up methods, guaranteeing that such cusped ...

---

### 14. Learning reveals invisible structure in low-rank RNNs

**Authors:** Yoav Ger, Omri Barak

**Published:** 2026-05-05

🔗 [Paper](http://arxiv.org/abs/2605.04115v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04115v1)

**Summary:** Learning in neural systems arises from synaptic changes that reshape the representations underlying behavior. While low-rank recurrent neural networks (RNNs) have emerged as a powerful framework for linking connectivity to function, a theoretical understanding of their learning process remains elusive. Here, we extend the low-rank framework from activity to learning by deriving gradient-descent dynamics directly in a reduced overlap space. We formulate a closed-form, low-dimensional system of OD...

---

### 15. NeuralSet: A High-Performing Python Package for Neuro-AI

**Authors:** Jean-Rémi King, Corentin Bel, Linnea Evanson, et al.

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.03169v2) | 📄 [PDF](https://arxiv.org/pdf/2605.03169v2)

**Summary:** Artificial intelligence (AI) is increasingly central to understanding how the brain processes information. However, the integration of neuroscience and modern AI is bottlenecked by a fragmented software ecosystem. Current tools are siloed by recording modality and optimized for small-scale, in-memory workflows, limiting the use of massive, naturalistic datasets. Here, we introduce NeuralSet, a Python framework that efficiently unifies the processing of diverse neural recordings (including fMRI, ...

---

### 16. Inferring Active Neural Circuits Using Diffusion Scores

**Authors:** Savik Kinger, Johannes Bertram, Luciano Dyballa, et al.

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02852v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02852v1)

**Summary:** In biological systems, neural circuits compute through directed, short-latency interactions whose effects unfold across multiple time scales and behavioral contexts. We address the problem of inferring these local, lag-specific interactions from sampled neural population activity under varying stimuli, without assuming a parametric form for the underlying dynamics. Our approach leverages denoising score models by estimating joint-window scores over consecutive activity snapshots (i.e., brain sta...

---

### 17. Online Generalised Predictive Coding

**Authors:** Mehran H. Z. Bazargani, Szymon Urbas, Adeel Razi, et al.

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02675v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02675v1)

**Summary:** This paper introduces an extension of generalised filtering for online applications. Generalised filtering refers to data assimilation schemes that jointly infer latent states, learn unknown model parameters, and estimate uncertainty in an integrated framework -- e.g., estimate state and observation noise -- at the same time (i.e., triple estimation). This framework appears across disciplines under different names, including variational Kalman-Bucy filtering in engineering, generalised predictiv...

---

### 18. Modeling sequential cognitive states via population level cortical dynamics

**Authors:** M Virginia Bolelli, Luca Greco, Dario Prandi

**Published:** 2026-05-04

🔗 [Paper](http://arxiv.org/abs/2605.02365v1) | 📄 [PDF](https://arxiv.org/pdf/2605.02365v1)

**Summary:** In this work, we present a mathematical model for cyclic and sequential patterns of brain activity, combining heteroclinic dynamics with discrete neural-field models. We first show that spatial-discrete neural-field equations with biologically realistic equilibria cannot support heteroclinic cycles. On the other hand, heterocline dynamics often arise in Lotka-Volterra-type systems, but these equations do not directly correspond to neuronal processes. To address this, we use a version of the Univ...

---

### 19. Electroencephalography and Electromyography as a Non-Invasive Biomarker of Neural Regeneration: A Review of Central and Peripheral Nervous System Injury and Regeneration

**Authors:** Maryam Kheyrollah, Reza Khanbabaie, Chris Ullrich, et al.

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01767v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01767v1)

**Summary:** Regeneration of the nervous system after injury remains an important therapeutic objective, especially in the central nervous system (CNS), in which regeneration is restricted by both neuronal limitations as well as adverse extracellular environments. Conversely, the peripheral nervous system (PNS) displays enhanced regenerative capability in the presence of supportive Schwann cells (SC) and pro-growth stimuli. While the structure and molecular mechanisms are thoroughly understood, functional bi...

---

### 20. From Cortical Synchronous Rhythm to Brain Inspired Learning Mechanism: An Oscillatory Spiking Neural Network with Time-Delayed Coordination

**Authors:** Tingting Dan, Guorong Wu

**Published:** 2026-05-03

🔗 [Paper](http://arxiv.org/abs/2605.01656v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01656v1)

**Summary:** Human cognition emerges from coordinated spiking dynamics in distributed neural circuits, where information is encoded via both firing rates and precise spike timing determined by brain rhythms. Inspired by this notion, we propose a brain-inspired learning primitive in which cognition-level neural synchrony emerges through iterative bottom-up and top-down interactions between micro-scale dynamics of spiking neurons and a macro-scale mechanism of oscillatory synchronization. Specifically, we mode...

---

### 21. Measuring Understanding Through Discrete Compositional Knowledge Structures in Hierarchical Automata

**Authors:** Igor Balaz

**Published:** 2026-05-02

🔗 [Paper](http://arxiv.org/abs/2605.01430v1) | 📄 [PDF](https://arxiv.org/pdf/2605.01430v1)

**Summary:** How do we measure genuine understanding in artificial cognitive systems? Current approaches face a measurement gap: probabilistic systems refine confidence gradually, practice-based systems compile knowledge through repeated execution, and neural systems distribute understanding across opaque embedding spaces. We propose that making understanding measurable requires architectures where understanding formation produces discrete, inspectable structural signatures. This paper presents hierarchical ...

---

### 22. Observable Performance Does Not Fully Reflect System Organization: A Multi-Level Analysis of Gait Dynamics Under Occlusal Constraint

**Authors:** Jacques Raynal, Pierre Slangen, Jacques Margerit

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00778v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00778v1)

**Summary:** In biomechanical systems, observable performance is often used as a proxy for underlying system organization. However, this assumption implicitly presumes a correspondence between output metrics and internal system states that may not hold in adaptive systems. In this study, the vertical dimension of occlusion (VDO) is considered as a constraint applied to an adaptive neuromechanical system, enabling the exploration of system-level responses under controlled variations. A single-case design in a...

---

### 23. Functional Connectivity-Guided Band Selection for Motor Imagery Brain-Computer Interfaces

**Authors:** Natália Araújo do Carmo, Aarthy Nagarajan

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00746v1)

**Summary:** Reliable control in motor imagery brain-computer interfaces (MI-BCIs) requires the precise decoding of user-specific neural rhythms, which vary significantly across individuals. The Common Spatial Pattern (CSP) algorithm is a cornerstone of MI-BCI decoding, yet its performance depends strongly on the spectral range of the input EEG data. Although Filter Bank CSP (FBCSP) extends this as a data-driven decoding framework, its frequency sub-bands are predefined rather than selected using subject-spe...

---

### 24. Robust volatility updates for Hierarchical Gaussian Filtering

**Authors:** Christoph Mathys, Nicolas Legrand, Peter Thestrup Waade, et al.

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00966v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00966v1)

**Summary:** Hierarchical Gaussian Filtering (HGF) networks allow for efficient updating of posterior distributions (beliefs) about hidden states of an agent's environment. HGF parent nodes can target the mean or variance of their children. New information entering at input nodes leads to a cascade of belief updates across the network according to one-step update equations for each node's mean and precision (inverse variance). However, the original form of the update equations for variance-targeting parents(...

---

### 25. Intrinsic Brain Networks Underlying the Experience and Expression of Subclinical Anxiety

**Authors:** Shruti Kinger, Mrinmoy Chakrabarty

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00465v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00465v1)

**Summary:** Anxiety includes behavioural, physiological, and subjective components that do not always align, and it remains unclear whether these dimensions are supported by distinct intrinsic brain networks. Guided by the two-system framework, we tested whether resting-state functional connectivity (rsFC) differentiates these components in subclinical anxiety. Forty-seven young adults spanning a range of subclinical anxiety levels completed a threat anticipation task measuring behavioral responses (reactio...

---

### 26. SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding

**Authors:** YuSheng Lin, Ji-Hwa Tsai, Chun-Shu Wei

**Published:** 2026-05-01

🔗 [Paper](http://arxiv.org/abs/2605.00401v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00401v1)

**Summary:** Recent EEG-to-image retrieval methods leverage pretrained vision encoders and foveation-inspired priors, but typically assume a fixed, center-focused view. This center bias conflicts with content-driven human attention, creating a geometric-semantic dissociation between visual features and EEG responses. We propose SIMON, a saliency-aware multi-view framework for zero-shot EEG-to-image retrieval. SIMON combines foreground segmentation and saliency prediction to select fixation centers via Salien...

---

### 27. CTM-AI: A Blueprint for General AI Inspired by a Model of Consciousness

**Authors:** Haofei Yu, Yining Zhao, Lenore Blum, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2605.04097v1) | 📄 [PDF](https://arxiv.org/pdf/2605.04097v1)

**Summary:** Despite remarkable advances, today's AI systems remain narrow in scope, falling short of the flexible, adaptive, and multisensory intelligence that characterizes human capabilities. This gap has fueled longstanding debates about whether AI might one day achieve human-like generality or even consciousness, and whether theories of consciousness can inspire new architectures for AI. This paper presents an early blueprint for implementing a general AI system, CTM-AI, combining the Conscious Turing M...

---

### 28. Multisensory learning recruits visual neurons into an olfactory memory engram

**Authors:** Zeynep Okray, Nils Otto, Anna A. Cook, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.28007v1) | 📄 [PDF](https://arxiv.org/pdf/2604.28007v1)

**Summary:** Associating multiple sensory cues with a single experience or object is a fundamental process that improves object recognition and memory performance. However, neural mechanisms that bind sensory features during learning and augment memory expression are unknown. Here we demonstrate multisensory appetitive and aversive memory in Drosophila. Combining colours and odours improved memory performance, even when each sensory modality was tested alone. Temporal control of neuronal function revealed vi...

---

### 29. On Agentic Behavioral Modeling

**Authors:** Dirk Ostwald, Rasmus Bruckner, Franziska Usée, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.27894v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27894v1)

**Summary:** Integrating theoretical neuroscience, decision theory, and probabilistic inference offers a promising route to understanding human cognition, yet concrete methodological bridges between agentic AI models and behavioral data analysis remain formally underdeveloped. We advance this synthesis under the framework of agentic behavioral modeling (ABM), which treats artificial agents as latent, generative hypotheses about cognitive mechanisms and evaluates them by their statistical adequacy in explaini...

---

### 30. Simulating Infant First-Person Sensorimotor Experience via Motion Retargeting from Babies to Humanoids

**Authors:** Francisco M. López, Hoshinori Kanazawa, Ondrej Fiala, et al.

**Published:** 2026-04-30

🔗 [Paper](http://arxiv.org/abs/2604.27583v1) | 📄 [PDF](https://arxiv.org/pdf/2604.27583v1)

**Summary:** Motion retargeting from humans to human-like artificial agents is becoming increasingly important as humanoid robots grow more capable. However, most existing approaches focus only on reproducing kinematics and ignore the rich sensorimotor experience associated with human movement. In this work, we present a framework for simulating the multimodal sensorimotor experiences of infants using physical and virtual humanoids. From a single video, our method reconstructs the infant's body configuration...

---

### 31. A geometry aware framework enhances noninvasive mapping of whole human brain dynamics

**Authors:** Song Wang, Kexin Lou, Chen Wei, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25592v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25592v1)

**Summary:** Non-invasive electrophysiology lacks methods that accurately reconstruct whole-brain spatiotemporal dynamics while incorporating individual cortical geometry, leaving current electroencephalography and magnetoencephalography source imaging limited by simplistic or biologically implausible priors. Here, we show that embedding participant-specific Geometric Basis Functions (GBFs), eigenmodes derived from each individual's cortical surface, provides a powerful anatomic constraint that resolves the ...

---

### 32. One-shot emergency psychiatric triage across 15 frontier AI chatbots

**Authors:** Veith Weilnhammer, Lennart Luettgau, Christopher Summerfield, et al.

**Published:** 2026-04-28

🔗 [Paper](http://arxiv.org/abs/2604.25415v1) | 📄 [PDF](https://arxiv.org/pdf/2604.25415v1)

**Summary:** AI chatbots are increasingly used for health advice, but their performance in psychiatric triage remains undercharacterized. Psychiatric triage is particularly challenging because urgency must often be inferred from thoughts, behavior, and context rather than from objective findings.   We evaluated the performance of 15 frontier AI chatbots on psychiatric triage from realistic single-message disclosures using 112 clinical vignettes, each paired with 1 of 4 original benchmark triage labels: A, ro...

---

### 33. Independent-Component-Based Encoding Models of Brain Activity During Story Comprehension

**Authors:** Kamya Hari, Taha Binhuraib, Jin Li, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24942v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24942v1)

**Summary:** Encoding models provide a powerful framework for linking continuous stimulus features to neural activity; however, traditional voxelwise approaches are limited by measurement noise, inter-subject variability, and redundancy arising from spatially correlated voxels encoding overlapping neural signals. Here, we propose an independent component (IC)-based encoding framework that dissociates stimulus-driven and noise-driven signals in fMRI data. We decompose continuous fMRI data from naturalistic st...

---

### 34. Homology-based Morphometry of Brain Atrophy: Methods and Applications

**Authors:** Donato Quiccione, Mariam Pirashvili, Nathan Broomhead, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24714v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24714v1)

**Summary:** Understanding the structure of the brain, and how it changes with time and disease, is a core goal of structural neuroimaging. Contemporary approaches to structural brain analysis are dominated by voxel-wise, mass-univariate methods such as voxel-based morphometry (VBM). However, these techniques require images to be normalized to a standard template, which can obscure subject-specific geometric features. Normalization to a common stereotactic space can also be problematic when comparing groups ...

---

### 35. Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks

**Authors:** Kevin McKee, Thomas Hazy, Yicong Zheng, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24637v2) | 📄 [PDF](https://arxiv.org/pdf/2604.24637v2)

**Summary:** Block-sequential continual learning demands that a single model both protect prior solutions from catastrophic forgetting and efficiently infer at inference time which prior solution matches the current input without task labels. We present Functional Task Networks (FTN), a parameter-isolation method inspired by structural and dynamical motifs found in the mammalian neocortex. Similar to mixture-of-experts, this method uses a high dimensional, self-organizing binary mask over a large population ...

---

### 36. The Genetic and Environmental Architecture of the Human Functional Connectome

**Authors:** Tanu Raghav, Daniel Guerrero, Uttara Tipnis, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24614v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24614v1)

**Summary:** Functional connectivity varies across individuals due to genetic and environmental factors, yet classical twin models typically confound non-shared environment with measurement error and are largely limited to resting-state analyses. We hypothesized that: i) explicitly modeling measurement error from repeated fMRI sessions enables more accurate application of classical twin models (ACE/ADE) to functional connectivity; ii) model applicability depends on scan-length and parcellation granularity; i...

---

### 37. Sure About That Line? Approaching Confidence-Based, Real-Time Line Assignment in Reading Gaze Data

**Authors:** Franziska Kaltenberger, Wei-Ling Chen, Enkeleda Thaqi, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2605.00033v1) | 📄 [PDF](https://arxiv.org/pdf/2605.00033v1)

**Summary:** Remote and webcam-based eye tracking in multi-line reading suffers from various noise factors and layout ambiguity, precisely where real-time reading support needs reliable, per-fixation line assignment. Prior work largely addresses this challenge post hoc or by restricting behavior (e.g., disallowing re-reading), undermining interactive use. We propose CONF-LA (Confidence-score-based Online Fixation-to-Line Assignment), a principled, low-latency approach that integrates knowledge about reading ...

---

### 38. Persistent and anti-persistent stride-to-stride fluctuations: an ARFIMA decomposition consistent with closed-loop sensorimotor control

**Authors:** Philippe Terrier

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24365v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24365v1)

**Summary:** Stride-to-stride fluctuations in human walking carry a fractal correlation structure that reverses sign under external cueing: self-paced gait is persistent, whereas metronomic or visually cued gait is anti-persistent. Three decades of detrended fluctuation analysis (DFA) have established this reversal as a scaling-exponent shift, but DFA cannot distinguish genuine long-memory dynamics from short-memory autoregressive moving-average (ARMA) processes that produce the same apparent exponent. We fi...

---

### 39. From Players to Participants: Citizen Science and Video Games to Understand Cognition

**Authors:** Syrine Salouhou, Edgar Dubourg, Maxwell Scott-Slade, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24321v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24321v1)

**Summary:** Citizen science is transforming how cognitive scientists study the human mind, and video games are at the heart of this shift. By embedding experimental tasks into engaging, game-like experiences, researchers can reach large, diverse populations while collecting rich behavioral data outside the lab. In this review, we explore how citizen science video games bridge the gap between players and participants, turning entertainment into large-scale cognitive research. Drawing on recent projects such ...

---

### 40. Solution of a large nonlinear recurrent neural network at fixed connectivity

**Authors:** Albert J. Wakhloo

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.24141v1) | 📄 [PDF](https://arxiv.org/pdf/2604.24141v1)

**Summary:** We calculate the moments and response functions of a nonlinear random recurrent neural network in the large $N$ limit. Our approach does not require averaging over synaptic weights and gives the first nontrivial term in a $1/\sqrt{N}$ expansion of general intensive-order correlation functions, proving a recent conjecture by Shen and Hu as a special case. Our results provide an analytical link between synaptic connectivity, correlations in spontaneous activity, and the response of a network to sm...

---

### 41. Robust and Clinically Reliable EEG Biomarkers: A Cross Population Framework for Generalizable Parkinson's Disease Detection

**Authors:** Nicholas R. Rasmussen, Longwei Wang, Rodrigue Rizk, et al.

**Published:** 2026-04-27

🔗 [Paper](http://arxiv.org/abs/2604.23933v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23933v1)

**Summary:** Developing robust and clinically reliable EEG biomarkers requires evaluation frameworks that explicitly address cross population generalization in multi site settings such as Parkinsons disease (PD) detection. Models trained under i.i.d. assumptions often capture population specific artifacts rather than disease relevant neural structure, leading to poor generalization across clinical cohorts. EEG further amplifies this challenge due to low signal to noise ratio and heterogeneous acquisition con...

---

### 42. Integrative neurocybernetic modeling in the era of large-scale neuroscience

**Authors:** Il Memming Park, Ayesha Vermani, Gonzalo G. de Polavieja, et al.

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23903v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23903v1)

**Summary:** Large-scale neuroscience is generating rich datasets across animals, brain areas and behavioral contexts, yet our modeling efforts remains fragmented across isolated experiments. We argue that understanding behavior requires integrative neurocybernetic models: understandable dynamical models that capture the closed-loop coupling of brain, body and environment, treat the brain as a controller pursuing latent objectives, represent structured variation across scales, and scale to heterogeneous data...

---

### 43. EyeBrain: Left and Right Brain Lateralization Activity Classification Through Pupil Diameter and Fixation Duration

**Authors:** Ko Watanabe, Pooja Pol, Nicolas Großmann, et al.

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23562v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23562v1)

**Summary:** The relationship between brain lateralization and cognitive functions is well-documented. The left hemisphere primarily handles tasks such as language and arithmetic, while the right hemisphere is involved in creative activities like drawing and music perception. Eye-tracking technology has shown the potential to reveal cognitive states by measuring ocular metrics such as pupil diameter and fixation duration. However, the ability to distinguish lateralized brain activity using these ocular metri...

---

### 44. Triple Configuration of Brain Networks Based on Recurrent Neural Networks: The Synergistic Effects of Exogenous Stimuli, Task Demands, and Spontaneous Activity

**Authors:** Binghao Yang, Guangzong Chen

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23525v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23525v1)

**Summary:** The foundation of cognitive flexibility and higher-order intelligence lies in the functional structure and activity of brain networks, which can be dynamically configured by both external environments and internal states. However, decoding these dynamics from high-dimensional neural data remains a challenge. In this study, we propose a computational framework using Recurrent Neural Networks (RNNs) with neural dynamic constraints to model source-localized resting-state EEG data from $114$ partici...

---

### 45. Linear equivalence of nonlinear recurrent neural networks

**Authors:** David G. Clark

**Published:** 2026-04-26

🔗 [Paper](http://arxiv.org/abs/2604.23489v2) | 📄 [PDF](https://arxiv.org/pdf/2604.23489v2)

**Summary:** Large nonlinear recurrent neural networks with random couplings generate high-dimensional, potentially chaotic activity whose structure is of interest in neuroscience and other fields. A fundamental object encoding the collective structure of this activity is the $N \times N$ covariance matrix. Prior analytical work on the covariance matrix has been limited to low-dimensional summary statistics. Recent work proposed an ansatz in which, at large $N$, the covariance matrix for a typical quenched r...

---

### 46. Vision as looking and seeing through a bottleneck

**Authors:** Li Zhaoping

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.23030v1) | 📄 [PDF](https://arxiv.org/pdf/2604.23030v1)

**Summary:** Progress in vision research has been slower downstream than upstream of primary visual cortex (V1). Traditional frameworks have largely overlooked a central constraint: only a tiny fraction of retinal input is recognized. Thus, to a first approximation, vision is better formulated as looking and seeing through a bottleneck. Looking, mainly by the peripheral visual field, selects visual information to enter this bottleneck, largely via gaze shifts that center selected contents at fovea. Seeing, m...

---

### 47. What are the functions of primary visual cortex (V1)?

**Authors:** Li Zhaoping

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.22716v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22716v1)

**Summary:** Although Hubel and Wiesel established decades ago how individual V1 neurons transform retinal inputs, functions of V1 as a whole are being discovered only recently. First, V1 acts as a motor cortex for exogenously guiding saccades by constructing a bottom-up saliency map of the visual field. Second, V1 initiates a processing bottleneck: a massive reduction of visual information begins at its output to downstream areas. Third, downstream recognition is limited by impoverished information, V1 supp...

---

### 48. Early Preconfiguration Failure: A Novel Predictor of the Repetitive Subconcussion

**Authors:** Jiajia Li, Zhenzhen Yu, Zhenghao Fu, et al.

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.22275v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22275v1)

**Summary:** Early diagnosis and assessment of repetitive subconcussive (rSC) brain injuries are crucial for early clinical intervention. Conventional methods, largely relying on slow fMRI, fail to capture millisecond-level early cortical dynamics, particularly spatiotemporal features associated with pre-configuration dynamics. This study introduces a novel approach integrating dynamic hierarchical spatial features and cortical early behavioral time-domain sensitivity, utilizing EEG and visual attention task...

---

### 49. Earable Platform with Integrated Simultaneous EEG Sensing and Auditory Stimulation

**Authors:** Min Suk Lee, Abhinav Uppal, Ananya Thota, et al.

**Published:** 2026-04-24

🔗 [Paper](http://arxiv.org/abs/2604.22137v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22137v1)

**Summary:** Conventional scalp-based EEG systems are cumbersome to use, requiring extensive setup, restrictive wiring, and conductive gels that can dry out and limit long-term monitoring, while also carrying social stigma. As a result, there is increasing interest in in-ear EEG technology to improve comfort, convenience, and discretion for users. This work presents a personalized in-ear EEG monitor (IEEM) that simultaneously captures EEG signals from the outer ear while delivering audio playback through the...

---

### 50. Resting-State EEG Biomarkers of Tinnitus Robust to Cross-Subject and Cross-Platform Variation

**Authors:** Adyant Balaji, Abhinav Uppal, Min Suk Lee, et al.

**Published:** 2026-04-23

🔗 [Paper](http://arxiv.org/abs/2604.22116v1) | 📄 [PDF](https://arxiv.org/pdf/2604.22116v1)

**Summary:** Tinnitus is a prevalent auditory condition lacking objective biomarkers, motivating the search for reliable neural signatures. EEG, being a noninvasive method of brain imaging with a high temporal resolution provides a way to investigate the neural dynamics that may be associated with tinnitus. The generalizability of EEG-based tinnitus biomarkers across different datasets remains a critical challenge. Microstate theory has allowed for the characterization of quasi-stable topographic configurati...

---

## stat.ML

**50 papers**

### 1. A Note on Non-Negative $L_1$-Approximating Polynomials

**Authors:** Jane H. Lee, Anay Mehrotra, Manolis Zampetakis

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08072v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08072v1)

**Summary:** $L_1$-Approximating polynomials, i.e., polynomials that approximate indicator functions in $L_1$-norm under certain distributions, are widely used in computational learning theory. We study the existence of \textit{non-negative} $L_1$-approximating polynomials with respect to Gaussian distributions. This is a stronger requirement than $L_1$-approximation but weaker than sandwiching polynomials (which themselves have many applications). These non-negative approximating polynomials have recently f...

---

### 2. Empirical Bayes Rebiasing

**Authors:** Wanyi Ling, Sida Li, Junming Guan, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08069v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08069v1)

**Summary:** We study methods for simultaneous analysis of many noisy and biased estimates, each paired with an even noisier estimate of its own bias. The analyst's goal is to construct short calibrated intervals for each parameter. The standard debiasing approach, which subtracts the bias estimate from each biased estimate, inflates variance and yields long intervals. In this paper, we propose an empirical Bayes rebiasing strategy that starts from the fully debiased estimates and learns from data how much b...

---

### 3. Inferring Asteroseismic Parameters from Short Observations Using Deep Learning: Application to TESS and K2 Red Giants

**Authors:** Nipun Ghanghas, Siddharth Dhanpal, Shravan Hanasoge, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08051v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08051v1)

**Summary:** Asteroseismology is the study of resonant oscillations of stars to infer their internal structure and dynamics. It is also a powerful tool for precisely determining stellar parameters such as mass, radius, surface gravity, and age. The ongoing TESS mission, with its nearly complete sky coverage, presents a unique opportunity to uniformly probe stellar populations across the Milky Way. TESS is estimated to have observed more than 300,000 oscillating red giants, most of which have one to two month...

---

### 4. Semiparametric Efficient Test for Interpretable Distributional Treatment Effects

**Authors:** Houssam Zenati, Arthur Gretton

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08034v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08034v1)

**Summary:** Distributional treatment effects can be invisible to means: a treatment may preserve average outcomes while changing tails, modes, dispersion, or rare-event probabilities. Kernel tests can detect discrepancies between interventional outcome laws, but global tests do not reveal where the laws differ. We propose DR-ME, to our knowledge the first semiparametrically efficient finite-location test for interpretable distributional treatment effects. DR-ME evaluates an interventional kernel witness at ...

---

### 5. Penalty-Based First-Order Methods for Bilevel Optimization with Minimax and Constrained Lower-Level Problems

**Authors:** Yiyang Shen, Yutian He, Weiran Wang, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.08006v1) | 📄 [PDF](https://arxiv.org/pdf/2605.08006v1)

**Summary:** We study a class of bilevel optimization problems in which both the upper- and lower-level problems have minimax structures. This setting captures a broad range of emerging applications. Despite the extensive literature on bilevel optimization and minimax optimization separately, existing methods mainly focus on bilevel optimization with lower-level minimization problems, often under strong convexity assumptions, and are not directly applicable to the minimax lower-level setting considered here....

---

### 6. It Just Takes Two: Scaling Amortized Inference to Large Sets

**Authors:** Antoine Wehenkel, Michael Kagan, Lukas Heinrich, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07972v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07972v1)

**Summary:** Neural posterior estimation has emerged as a powerful tool for amortized inference, with growing adoption across scientific and applied domains. In many of these applications, the conditioning variable is a set of observations whose elements depend not only on the target but also on unknown factors shared across the set. Optimal inference therefore requires treating the set jointly, which in turn requires training the estimator at the deployment set size -- a regime where memory and compute quic...

---

### 7. Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means

**Authors:** Valentin Kilian, Stefano Cortinovis, François Caron

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07964v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07964v1)

**Summary:** Confidence sequences based on test martingales provide time-uniform uncertainty quantification for the mean of bounded IID observations without parametric distributional assumptions. Their practical efficiency, however, depends strongly on the choice of martingale updates, and many existing constructions do not exploit prior information about plausible data-generating distributions or mean values. We propose a Bayes-assisted framework that uses a Bayesian working predictive model to adaptively c...

---

### 8. Consistency Regularised Gradient Flows for Inverse Problems

**Authors:** Alessio Spagnoletti, Tim Y. J. Wang, Marcelo Pereyra, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07907v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07907v1)

**Summary:** Vision-Language Latent Diffusion Models (LDMs) (Rombach et al., 2022) provide powerful generative priors for inverse problems. However, existing LDM-based inverse solvers typically require a large number of neural function evaluations (NFEs) and backpropagation through large pretrained components, leading to substantial computational costs and, in some cases, degraded reconstruction quality. We propose a unified Euclidean-Wasserstein-2 gradient-flow framework that jointly performs posterior samp...

---

### 9. Characterizing and Correcting Effective Target Shift in Online Learning

**Authors:** Ziyan Li, Naoki Hiratani

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07886v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07886v1)

**Summary:** Online learning from a stream of data is a defining feature of intelligence, yet modern machine learning systems often struggle in this setting, especially under distributional shift. To understand its basic properties, we study the relationship between online and offline learning in the context of kernel regression. We derive a closed-form expression for the function learned by online kernel regression, revealing that online kernel regression is equivalent to offline regression with shifted, in...

---

### 10. Black-box model classification under the discriminative factorization

**Authors:** Hayden Helm, Merrick Ohata, Carey Priebe

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07878v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07878v1)

**Summary:** Access to modern generative systems is often restricted to querying an API (the ``black-box" setting) and many properties of the system are unknown to the user at inference time. While recent work has shown that low-dimensional representations of models based on the relationship between their embedded responses to a set of queries are useful for inferring model-level properties, the quality of these representations is highly sensitive to the query set. We introduce the \emph{discriminative facto...

---

### 11. Spectral Dynamics in Deep Networks: Feature Learning, Outlier Escape, and Learning Rate Transfer

**Authors:** Clarissa Lauditi, Cengiz Pehlevan, Blake Bordelon

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07870v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07870v1)

**Summary:** We study the evolution of hidden-weight spectra in wide neural networks trained by (stochastic) gradient descent. We develop a two-level dynamical mean-field theory (DMFT) that jointly tracks bulk and outlier spectral dynamics for spiked ensembles whose spike directions remain statistically dependent on the random bulk. We apply this framework to two settings: (1) infinite-width nonlinear networks in mean-field/$μ$P scaling and (2) deep linear networks in the proportional high-dimensional limit,...

---

### 12. Expectation-Maximization as a Spectrally Governed Relaxation Flow

**Authors:** Qiao Wang

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07818v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07818v1)

**Summary:** The expectation--maximization (EM) algorithm combines global monotonicity, local linear convergence, and strong practical robustness, but these features are usually analyzed separately. Global descent is nonlinear, whereas local convergence is governed by the spectrum of the linearized EM map. How these two levels fit into a single dynamical picture has remained less transparent.   We make explicit the latent-variable operator that connects them. Along the EM trajectory, the likelihood increment...

---

### 13. POETS: Uncertainty-Aware LLM Optimization via Compute-Efficient Policy Ensembles

**Authors:** Nicolas Menet, Andreas Krause, Abbas Rahimi

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07775v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07775v1)

**Summary:** Balancing exploration and exploitation is a core challenge in sequential decision-making and black-box optimization. We introduce POETS ($\textbf{Po}$licy $\textbf{E}$nsembles for $\textbf{T}$hompson $\textbf{S}$ampling), a novel framework that bridges uncertainty quantification and policy optimization. Our approach is grounded in the insight that policies trained with Kullback-Leibler (KL) regularization implicitly encode an underlying reward function. Building on this, POETS bypasses the compl...

---

### 14. Flow Matching for Count Data

**Authors:** Ganchao Wei, John Pearson

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07746v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07746v1)

**Summary:** High-dimensional count data arise in applications such as single-cell RNA sequencing and neural spike trains, where mapping between distributions across successive batches or time points form critical components of data analysis. The recent success of diffusion- and flow-based deep generative models for images, video, and text motivates extending these ideas to count-valued settings, but many existing methods either treat each count as a categorical state or transform counts into a continuous sp...

---

### 15. TopoFisher: Learning Topological Summary Statistics by Maximizing Fisher Information

**Authors:** Matteo Biagetti, Mathieu Carrière, Francesco Conti, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07720v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07720v1)

**Summary:** Persistence diagrams provide stable, interpretable summaries of geometric and topological structure and are useful for simulation-based inference when low-order statistics miss key information. Yet persistence-based pipelines require hand-chosen filtrations, vectorizations, and compressors, typically without an objective tied to parameter uncertainty. We introduce \textbf{TopoFisher}, a differentiable persistent-homology pipeline that learns topological summaries by maximizing local Gaussian Fis...

---

### 16. Debiased Counterfactual Generation via Flow Matching from Observations

**Authors:** Hugh Dance, Johnny Xi, Peter Orbanz, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07665v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07665v1)

**Summary:** Estimating counterfactual distributions under interventions is central to treatment risk assessment and counterfactual generation tasks. Existing approaches model the counterfactual distribution as a standalone generative target, without exploiting its relationship to the observational data. In this work, we show that under standard assumptions, observational and counterfactual outcome distributions are tightly linked: they have identical support and tail behavior, remain statistically close und...

---

### 17. Reliable Chain-of-Thought via Prefix Consistency

**Authors:** Naoto Iwase, Yuki Ichihara, Mohammad Atif Quamar, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07654v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07654v1)

**Summary:** Large Language Models often improve accuracy on reasoning tasks by sampling multiple Chain-of-Thought (CoT) traces and aggregating them with majority voting (MV), a test-time technique called self-consistency. When we truncate a CoT partway through and regenerate the remainder, we observe that traces with correct answers reproduce their original answer more often than traces with wrong answers. We use this difference as a reliability signal, prefix consistency, that weights each candidate answer...

---

### 18. Statistical Convergence of Spherical First Hitting Diffusion Models

**Authors:** Simon Bienewald, Lukas Trottner

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07625v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07625v1)

**Summary:** Denoising diffusion models have evolved into a state-of-the-art method for tasks in various fields, such as denoising and generation of images, text generation, or generation of synthetic data for training of other machine learning models. First hitting diffusion models (FHDM) are a particular class of denoising diffusion models with \textit{random} adaptive generation time tailored to generate data on a known manifold. Building on the conditioning framework of Doob's $h$-transform these models ...

---

### 19. A Refined Generalization Analysis for Extreme Multi-class Supervised Contrastive Representation Learning

**Authors:** Nong Minh Hieu, Antoine Ledent

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07596v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07596v1)

**Summary:** Contrastive Representation Learning (CRL) has achieved strong empirical success in multiple machine learning disciplines, yet its theoretical sample complexity remains poorly understood. Existing analyses usually assume that input tuples are identically and independently distributed, an assumption violated in most practical settings where contrastive tuples are constructed from a finite pool of labeled data, inducing dependencies among tuples. While one recent work analyzed this learning setting...

---

### 20. Revisiting Transformer Layer Parameterization Through Causal Energy Minimization

**Authors:** Jin Xu, Camille Couturier, Victor Rühle, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07588v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07588v1)

**Summary:** Transformer blocks typically combine multi-head attention (MHA) for token mixing with gated MLPs for token-wise feature transformation, yet many choices in their parameterization remain largely empirical. We introduce Causal Energy Minimization (CEM), a framework that recasts Transformer layers as optimization steps on conditional energy functions while explicitly accounting for layer parameterization. Extending prior energy-based interpretations of attention, CEM shows that weight-tied MHA can ...

---

### 21. Open-Ended Task Discovery via Bayesian Optimization

**Authors:** Masaki Adachi, Yuta Suzuki, Juliusz Ziomek

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07572v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07572v1)

**Summary:** When applying Bayesian optimization (BO) to scientific workflow, a major yet often overlooked source of uncertainty is the task itself -- namely, what to optimize and how to evaluate it -- which can evolve as evidence accumulates. We introduce Generate-Select-Refine (GSR), a open-ended BO framework that alternates between task generation and task optimization. Starting from a user-provided seed task, GSR generates new tasks in a coarse-to-fine manner while a task-acquisition function schedules o...

---

### 22. Ensemble Distributionally Robust Bayesian Optimisation

**Authors:** Tigran Ramazyan, Denis Derkach

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07565v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07565v1)

**Summary:** We study zeroth-order optimisation under context distributional uncertainty, a setting commonly tackled using Bayesian optimisation (BO). A prevailing strategy to make BO more robust to the complex and noisy nature of data is to employ an ensemble as the surrogate model, thereby mitigating the weaknesses of any single model. In this study, we propose a novel algorithm for Ensemble Distributionally Robust Bayesian Optimisation that remains computationally tractable while managing continuous conte...

---

### 23. ProteinJEPA: Latent prediction complements protein language models

**Authors:** Dan Ofer, Dafna Shahaf, Michal Linial

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07554v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07554v1)

**Summary:** Protein language models are trained primarily with masked language modeling (MLM), which predicts amino-acid identities at masked positions. We ask whether latent-space prediction can complement these token-level objectives under matched wall-clock budget. Across pretrained and random-init protein sequence encoders at 35--150M parameters, we find that the best protein-JEPA design is not all-position latent prediction but a variant: predicting latent targets only at masked positions, and retainin...

---

### 24. Robust Tensor Regression with Nonconvexity: Algorithmic and Statistical Theory

**Authors:** Zihao Song, Jicai Liu, Heng Lian, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07448v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07448v1)

**Summary:** Tensor regression is an important tool for tensor data analysis, but existing works have not considered the impact of outliers, making them potentially sensitive to such data points. This paper proposes a low tubal rank robust regression method for analyzing high-dimensional tensor data with heavy-tailed random noise. The proposed method is based on a nonconvex relaxation of the tensor tubal rank within a general optimization framework, which allows for nonconvexity in both the loss and penalty ...

---

### 25. Spectrum-Adaptive Generalization Bounds for Trained Deep Transformers

**Authors:** Mana Sakai, Masaaki Imaizumi

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07297v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07297v1)

**Summary:** Understanding why trained Transformers generalize well is a fundamental problem in modern machine learning theory, and complexity-based generalization bounds provide a principled way to study this question. While existing norm-based bounds for Transformers remove the explicit polynomial dependence on the hidden dimension, they typically impose fixed norm constraints specified a priori and can exhibit unfavorable exponential dependence on depth. In this paper, we derive spectrum-adaptive post hoc...

---

### 26. Resource-Element Energy Difference for Noncoherent Over-the-Air Federated Learning

**Authors:** Hao Chen, Zavareh Bozorgasl

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07263v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07263v1)

**Summary:** Over-the-air federated learning (OTA-FL) reduces uplink latency by exploiting waveform superposition, but conventional analog aggregation schemes typically require instantaneous channel state information (CSI), channel inversion, and coherent phase alignment, which can be difficult to maintain in practical wireless systems. This paper proposes resource-element energy difference (REED), a noncoherent aggregation primitive for continuous signed updates that avoids instantaneous CSI. REED maps the ...

---

### 27. Modulated learning for private and distributed regression with just a single sample per client device

**Authors:** Praneeth Vepakomma, Amirhossein Reisizadeh, Samuel Horváth, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07233v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07233v1)

**Summary:** This work focuses on the question of learning from a large number of devices with each device holding only a single sample of data. Several real-world applications exist to this one sample per client setup up including learning from fitness trackers, data/app usage aggregators, body-worn sensing devices, and daily event monitors to name a few. When a client has only one sample, the standard federated learning paradigm breaks down as a local update based on that single point is far from being use...

---

### 28. Improved Model-based Reinforcement Learning with Smooth Kernels

**Authors:** Kun Long, Yuqiang Li, Xianyi Wu

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07218v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07218v1)

**Summary:** For continuous state-action space scenarios, classical reinforcement learning (RL) theory predominantly focuses on low-rank Markov decision processes (MDPs), which provide sample-efficient guarantees at the expense of restrictive structural assumptions. Kernel smoothing model-based approaches offer a promising alternative paradigm that instead leverages the smoothness of the MDP and employs non-parametric kernel smoothing estimates of transition dynamics. This paper proposes a new kernel-smoothi...

---

### 29. Cost-Ordered Feasibility for Multi-Armed Bandits with Cost Subsidy

**Authors:** Ishank Juneja, Carlee Joe-Wong, Osman Yağan

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07171v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07171v1)

**Summary:** The classic multi-armed bandit (MAB) problem tackles the challenge of accruing maximum reward while making decisions under uncertainty. However, in applications, often the goal is to minimize cost subject to a constraint on the minimum permissible reward, an objective captured by multi-armed bandits with cost-subsidy (MAB-CS). Of interest to this paper is the setting where the quality (reward) constraint is specified relative to the unknown best reward and the cost of each arm is known. We chara...

---

### 30. When Symbol Names Should Not Matter: A Logistic Theory of Fresh-Symbol Classification

**Authors:** Wenjie Guan, Jelena Bradic

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07120v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07120v1)

**Summary:** Template tasks have emerged as a clean testbed for asking whether transformers reason with abstract symbols rather than concrete token names. We study the fixed-label classification version of this problem, where train and test examples share latent templates but may use disjoint vocabularies. Unlike next-token prediction, the model need not emit unseen symbols; it must learn a decision rule invariant to symbol renaming. We analyze regularized kernel logistic classification in the transformer-ke...

---

### 31. Classification Fields: Arbitrarily Fine Recursive Hierarchical Clustering From Few Examples

**Authors:** Yicen Li, Ruiyang Hong, Anastasis Kratsios, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07119v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07119v1)

**Summary:** Classical clustering methods usually return either a finite partition of the observed data or a finite dendrogram over it. This finite-sample view is inadequate when the hierarchy of interest is a recursive geometric object with fine-scale refinements that continue beyond the levels directly observed. We introduce classification fields: infinite-depth hierarchical cluster structures on $\mathbb{R}^d$ generated by a local parent-to-child refinement rule. A classification field generator maps each...

---

### 32. Conformal-Style Quantile Analyses for Stochastic Bandits

**Authors:** Chengyu Du, Mengfan Xu

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07115v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07115v1)

**Summary:** Stochastic bandit algorithms are usually analyzed under a mean-reward criterion, yet many problems favor arms with strong upper-tail performance, which we study herein. For a fixed miscoverage level \(α\), the natural upper-tail target of arm \(j\) is the upper endpoint \(F_j^{-1}(1-α/2)\) of a central prediction interval. This target can rank arms differently from their means, creating a central mismatch with the classical bandit objective. To this end, we propose ACP-UCB1, a conformal-style po...

---

### 33. Sub-Gaussian Concentration and Entropic Normality of the Maximum Likelihood Estimator

**Authors:** Leighton P. Barnes, Alex Dytso

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07107v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07107v1)

**Summary:** It is well known that, under standard regularity conditions, the maximum likelihood estimator (MLE) satisfies a central limit theorem and converges in distribution to a Gaussian random variable as the sample size grows. This paper strengthens this classical result by developing several stronger forms of asymptotic normality for the normalized MLE. With additional assumptions on the score, we first establish sub-Gaussian tail bounds and convergence of all moments for the normalized estimation err...

---

### 34. Almost Sure Convergence Rates of Stochastic Approximation and Reinforcement Learning via a Poisson-Moreau Drift

**Authors:** Xinyu Liu, Zixuan Xie, Shangtong Zhang

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07104v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07104v1)

**Summary:** Establishing almost sure convergence rates for stochastic approximation and reinforcement learning under Markovian noise is a fundamental theoretical challenge. We make progress towards this challenge for a class of stochastic approximation algorithms whose expected updates are contractive, a setting that arises in many reinforcement learning algorithms such as $Q$-learning and linear temporal difference learning. Specifically, for a power-law learning rate $O(n^{-η})$ with $η\in (1/2, 1)$, we o...

---

### 35. Decentralized Diffusion Policy Learning for Enhanced Exploration in Cooperative Multi-agent Reinforcement Learning

**Authors:** Yuyang Zhang, Haldun Balim, Na Li

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07101v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07101v1)

**Summary:** Cooperative multi-agent reinforcement learning (MARL) involves complex agent interactions and requires effective exploration strategies. A prominent class of MARL algorithms, decentralized softmax policy gradient (DecSPG), addresses this through energy-based policy updates. In practice, however, such energy-based policies are intractable to maintain and are commonly projected onto the Gaussian policy class. In this work, we show that the limited expressiveness of Gaussian policies severely hinde...

---

### 36. TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models

**Authors:** Zhenhan Fang, Aixin Tan, Jian Huang

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07100v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07100v1)

**Summary:** Constructing valid and informative conformal prediction regions for multi-dimensional outputs remains a fundamental challenge. While conformal prediction provides finite-sample, distribution-free coverage guarantees, its practical performance critically depends on the choice of nonconformity score. Existing approaches often rely on restrictive geometric assumptions or require explicit likelihood evaluation and invertible transformations, limiting their applicability in complex generative setting...

---

### 37. Every Feedforward Neural Network Definable in an o-Minimal Structure Has Finite Sample Complexity

**Authors:** Anastasis Kratsios, Gregory Cousins, Haitz Sáez de Ocáriz Borde, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07097v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07097v1)

**Summary:** We show that, in a precise sense, a broad class of feedforward neural networks learn (have finite sample complexity) in the PAC model: every fixed finite feedforward architecture whose layers are definable in an o-minimal structure has finite sample complexity in the agnostic PAC setting, even with unbounded parameters. This covers standard fixed-size MLPs, CNNs, GNNs, and transformers with fixed sequence length, together with the operations and layers typically used in such architectures, inclu...

---

### 38. Less Random, More Private: What is the Optimal Subsampling Scheme for DP-SGD?

**Authors:** Andy Dong, Ayfer Özgür

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07072v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07072v1)

**Summary:** Poisson subsampling is the default sampling scheme in differentially private machine learning, largely because its unstructured randomness yields tractable privacy amplification analyses. Yet this same randomness introduces substantial participation variance: each sample appears in very different numbers of training iterations. In this work, we show that this variance is not merely a practical artifact to be tolerated, but a fundamental source of suboptimal privacy amplification. We prove that B...

---

### 39. Causal EpiNets: Precision-corrected Bounds on Individual Treatment Effects using Epistemic Neural Networks

**Authors:** Gandharv Patil, Keyi Tang, Raquel Aoki, et al.

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07065v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07065v1)

**Summary:** Individual treatment effects are not point-identified from data. The Probability of Necessity and Sufficiency (PNS) circumvents this limitation by characterizing individual-level causality through intersection bounds derived from combined experimental and observational data. In finite samples, however, standard plug-in estimators systematically fail: they violate structural probability constraints and suffer from extremum bias induced by max-min operators, yielding spuriously narrow intervals. W...

---

### 40. Functional-prior-based Bayesian PDE-constrained inversion using PINNs

**Authors:** Ryoichiro Agata, Tomohisa Okazaki

**Published:** 2026-05-08

🔗 [Paper](http://arxiv.org/abs/2605.07060v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07060v1)

**Summary:** Physics-informed neural networks (PINNs) provide a mesh-free framework for solving PDE-constrained inverse problems, but their extension to Bayesian inversion still faces a fundamental difficulty: prior distributions are typically defined in the weight space of neural networks, whereas physically meaningful prior assumptions are more naturally expressed in function space. In this study, we introduce a unified framework, termed functional-prior-based approaches to Bayesian PDE-constrained inversi...

---

### 41. An Interpretable and Scalable Framework for Evaluating Large Language Models

**Authors:** Xinhao Qu, Qiang Heng, Hao Zeng, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.07046v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07046v1)

**Summary:** Evaluation of large language models (LLMs) is increasingly critical, yet standard benchmarking methods rely on average accuracy, overlooking both the inherent stochasticity of LLM outputs and the heterogeneity of benchmark items. Item Response Theory (IRT) offers a principled framework for modeling latent model abilities and item characteristics, but conventional methods are computationally expensive and numerically unstable, limiting large-scale implementations. To address these challenges, we ...

---

### 42. BGM-IV: an AI-powered Bayesian generative modeling approach for instrumental variable analysis

**Authors:** Guyue Luo, Qiao Liu

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.07029v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07029v1)

**Summary:** Instrumental-variable (IV) regression enables causal estimation under endogeneity, but modern IV problems often involve nonlinear structural effects and high-dimensional covariates. Existing nonlinear IV methods directly learn the causal relation in observed feature space or rely on learned representations within two-stage or moment-based procedures, which can struggle when the causal information is embedded in a high-dimensional representation. We propose BGM-IV, a latent Bayesian generative mo...

---

### 43. Adaptive auditing of AI systems with anytime-valid guarantees

**Authors:** Siyu Zhou, Patrick Vossler, Venkatesh Sivaraman, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.07002v1) | 📄 [PDF](https://arxiv.org/pdf/2605.07002v1)

**Summary:** A major bottleneck in characterizing the failure modes of generative AI systems is the cost and time of annotation and evaluation. Consequently, adaptive testing paradigms have gained popularity, where one opportunistically decides which cases and how many to annotate based on past results. While this framework is highly practical, its extreme flexibility makes it difficult to draw statistically rigorous conclusions, as it violates classical assumptions: the number of observations is typically l...

---

### 44. Optimal Experiments for Partial Causal Effect Identification

**Authors:** Tobias Maringgele, Jalal Etesami

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06993v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06993v1)

**Summary:** Causal queries are often only partially identifiable from observational data, and experiments that could tighten the resulting bounds are typically costly. We study the problem of selecting, prior to observing experimental outcomes, a cost-constrained subset of experiments that maximally tightens bounds on a target query. We formalize this as the max-potency problem, where epistemic potency measures the worst-case reduction in bound width guaranteed by an experiment, and show that this problem i...

---

### 45. Why Does Agentic Safety Fail to Generalize Across Tasks?

**Authors:** Yonatan Slutzky, Yotam Alexander, Tomer Slor, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06992v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06992v1)

**Summary:** AI agents are increasingly deployed in multi-task settings, where the task to perform is specified at test time, and the agent must generalize to unseen tasks. A major concern in such settings is safety: often, an agent must not only execute unseen tasks, but do so while avoiding risks and handling ones that materialize. Empirical evidence suggests that even when the ability to execute generalizes to unseen tasks, the ability to do so safely frequently does not. This paper provides theory and ex...

---

### 46. Response Time Enhances Alignment with Heterogeneous Preferences

**Authors:** Federico Echenique, Alireza Fallah, Baihe Huang, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06987v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06987v1)

**Summary:** Aligning large language models (LLMs) to human preferences typically relies on aggregating pooled feedback into a single reward model. However, this standard approach assumes that all labelers share the same underlying preferences, ignoring the fact that real-world labelers are highly heterogeneous and usually anonymous. Consequently, relying solely on binary choice data fundamentally distorts the learned policy, making the true population-average preference unidentifiable. To overcome this crit...

---

### 47. PLOT: Progressive Localization via Optimal Transport in Neural Causal Abstraction

**Authors:** Jonathn Chang, Arya Datla, Ziv Goldfeld

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06979v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06979v1)

**Summary:** Causal abstraction offers a principled framework for mechanistic interpretability, aligning a high-level causal model with the low-level computation realized by a neural network through counterfactual intervention analysis. Existing methods such as distributed alignment search (DAS) learn expressive subspace interventions, but the relevant neural site is unknown a priori, so finding a handle requires a computationally burdensome search over candidate sites. We introduce PLOT (Progressive Localiz...

---

### 48. $f$-Divergence Regularized RLHF: Two Tales of Sampling and Unified Analyses

**Authors:** Di Wu, Chengshuai Shi, Jing Yang, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06977v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06977v1)

**Summary:** Reinforcement Learning from Human Feedback (RLHF) has become a cornerstone technique for post-training large language models. While most existing approaches rely on the reverse KL-regularization, recent empirical studies have begun exploring alternative divergences (e.g., forward KL, chi-squared) as regularizers in RLHF. However, a unified theoretical understanding of general $f$-divergence regularization remains under-explored. To fill this gap, this work develops a comprehensive theoretical fr...

---

### 49. A Differentiable Bayesian Relaxation for Latent Partial-Order Inference

**Authors:** Dongqing Li, Geoff K. Nicholls, Shiyi Sun, et al.

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06976v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06976v1)

**Summary:** Many ranking and agent trace datasets are recorded as linear orders even though their latent structure is only partially ordered. This is especially common in agent and workflow traces, where observed order may reflect arbitrary linearization rather than true prerequisites. We introduce a differentiable relaxation for latent partial-order inference from such traces. Starting from a hard frontier-constrained model of noisy linear extensions, we replace discontinuous product-order precedence and b...

---

### 50. Locally Near Optimal Piecewise Linear Regression in High Dimensions via Difference of Max-Affine Functions

**Authors:** Haitham Kanj, Kiryung Lee

**Published:** 2026-05-07

🔗 [Paper](http://arxiv.org/abs/2605.06959v1) | 📄 [PDF](https://arxiv.org/pdf/2605.06959v1)

**Summary:** This paper presents a parametric solution to piecewise linear regression through the Adaptive Block Gradient Descent (ABGD) algorithm. The heart of the method is the parametrization of piecewise linear functions as the difference of max-affine (DoMA) functions. A non-asymptotic local convergence analysis for ABGD is provided under sub-Gaussian covariate and noise distributions. To initialize ABGD, we adapt a prior algorithm originally developed for the simpler setting of max-affine functions. Wh...

---

