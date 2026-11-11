# arXiv Daily Digest - 2026-11-11

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training

**Authors:** Emre Kutlusan, Yongmin Li

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14519v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14519v1)

**Summary:** Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what deter...

---

### 2. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR

**Authors:** Sheethal Bhat, Bogdan Georgescu, Awais Mansoor, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14518v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14518v1)

**Summary:** DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by...

---

### 3. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

**Authors:** Ziang Liu, James J. Kim, Yijia Dai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14514v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14514v1)

**Summary:** LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusiv...

---

### 4. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents

**Authors:** Howard Zhang, Chuck Arvin, Logan Brown, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14493v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14493v1)

**Summary:** Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies e...

---

### 5. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

**Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14492v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14492v1)

**Summary:** Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often...

---

### 6. Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game

**Authors:** Muhan Gao, Hangxiao Zhu, Xinqi Su, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14487v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14487v1)

**Summary:** Research ideation is iterative: researchers refine their ideas step by step based on feedback. Yet existing evaluations obscure this search process, making it difficult to understand how LLMs explore the space of research ideas and what limits their progress. We introduce Re-Search, which adapts the format of Twenty Questions to research ideation: given only the research problem of a published paper, a model must rediscover the paper's core idea by asking yes-or-no questions. Built from 200 ICML...

---

### 7. One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge

**Authors:** Ilia Larchenko, Gleb Zarin, Atindra Nair, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14432v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14432v1)

**Summary:** We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion ...

---

### 8. Two Communities, One Problem: Branch-and-Bound vs. A* for Resource-Constrained Project Scheduling

**Authors:** Izack Cohen, Dominik Kress, Lara Nehrke, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14426v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14426v1)

**Summary:** Branch-and-Bound (B&B) and $A^*$ are popular exact search methods originating from Operations Research and Artificial Intelligence, respectively. Although the two methods share fundamental search principles, their different ways of exploring the search space can lead to substantially different computational performance. We investigate these differences using the Resource-Constrained Project Scheduling Problem (RCPSP) as an exemplary problem setting. We first establish the relationships between m...

---

### 9. Quantifying the Sampling Frequency Invariance of Time-Series Foundation Models for Sensor Data Applications

**Authors:** Sourish Gunesh Dhekane, Abinaya Kumar, Torsten Woertwein, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14425v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14425v1)

**Summary:** Time-Series Foundation Models (TSFMs) are increasingly used in sensor applications, where sampling frequency (SF) varies across sensors, devices, and operating modes (e.g., power saving). Ideally, TSFMs must remain effective during such SF changes, provided the SF retains task-critical bandwidth. In this paper, we stress-test 4 prominent TSFMs: MOMENT, Chronos-2, Moirai-MoE, and TimesFM, to quantify their SF-invariance and investigate whether their behavior tracks the resulting loss of informati...

---

### 10. Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning

**Authors:** Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14419v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14419v1)

**Summary:** Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting model faithfully represents the intended decision problem. We introduce a benchma...

---

### 11. Precision on Demand: Escalating Weight Bits at Uncertain Decoding Steps in a Small Local Model

**Authors:** Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14418v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14418v1)

**Summary:** Local decoding usually fixes one weight precision for the whole generation. We study a different allocation: store 8-bit weights, decode with their top 4 bits, and redo a step at 8 bits only when the low-precision output distribution looks uncertain (entropy above a threshold or a small top-two margin). Quantization is simulated, the model is Qwen3-0.6B, and the benchmark is GSM8K. Cost is counted in weight bytes read per token. On 36724 replayed steps the entropy of the low pass ranks argmax fl...

---

### 12. Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models

**Authors:** Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14413v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14413v1)

**Summary:** Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes the second worse, and which is the cheaper way to spend a fixed budget. On Qwen3-0.6B and Qwen3-1.7B with simulated round-to-nearest weight quantization (8, 6, 4 and 3 bits, fp16 reference), read from the logits of the letters A to D on ARC-Easy, ARC-Challenge, MMLU and HellaSwag (300 items each), 6 b...

---

### 13. Causal Concept Explanations for Deep Neural Models

**Authors:** Josh Rountree, Pulkit Verma, Oswin So, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14407v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14407v1)

**Summary:** Concept-based explanations in neural models are important for the development, certification, and adoption of autonomous systems. Yet, interpretability remains correlational. Without methods to guide and quantify causal relationships between explanations, a concept explanation can be provided without being necessary or sufficient for the observed output thereby appearing correct while misleading. We introduce Causal Concept Wrapper Network (CCW-Net), the first use of interventional mediation ana...

---

### 14. Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models

**Authors:** Amir Mann, Jonathan Fhima, Shaked Brody, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14387v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14387v1)

**Summary:** Diffusion Language Models (DLMs) have emerged as effective alternatives to autoregressive models for latency-critical tasks, enabling faster token generation. Recent advances employ block diffusion with self-editing capabilities, where each block refines tokens iteratively before advancing to the next one. Yet each block is only as fast as its slowest token, and the next block cannot start before it. We suggest Blurring the Block Boundaries (B3), a novel method with which two blocks are refined ...

---

### 15. An Energy-Based Perspective on Machine Learning

**Authors:** Bo Dai, Yilun Du

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14383v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14383v1)

**Summary:** Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many. This tutorial has a broader goal: beyond introducing EBMs, it uses them as a single lens that connects the different aspects of machine learning. Any EBM is specified by three choices, the energy, which determines what the model represents; the inference procedure, which samples from or optimizes the energy; and the learning method, whi...

---

### 16. Cognitive Mapping of Learning by Thinking Mechanisms in Large Language Models

**Authors:** Dong Han, Jin Zhang, Kunyue Yang

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14382v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14382v1)

**Summary:** Large language models (LLMs) increasingly exhibit capabilities that resemble human Learning by Thinking (LbT), the acquisition of new insight through internal processes such as explanation and reasoning, without new external input. A systematic account of the cognitive mechanisms behind these capabilities, and of their limits, remains underdeveloped. This paper proposes a Cognitive LbT Framework that maps four mechanisms (Reflective Reasoning, Synthetic Memory Formation, Internal Simulation, and...

---

### 17. EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities

**Authors:** Zhengxiang Huang, Yujie Sun, Shengheng Chen, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14356v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14356v1)

**Summary:** Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly system challenge. Each model may require coordinated changes across conversion, graph construction, operators, and hardware backends. Existing coding agents often miss these cross-layer dependencies and struggle to diagnose failures across host--device execution paths. We present EngineAgent, an agentic system for automating on-device LLM model ena...

---

### 18. CLADE: Category-Level Answering from Deficient Evidence in Retrieval-Augmented Language Models

**Authors:** S M Rayeed, Charles V. Stewart, Yao Ma

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14355v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14355v1)

**Summary:** Retrieval-augmented systems often retrieve passages that are accurate and relevant but state the answer at a coarser level of granularity than the question requires. For example, a question may ask which specific disease a drug treats (familial hyperlipidemia), while the retrieved passage mentions the broader disease family (hyperlipidemia). Prior work on context sufficiency treats such coarse passages simply as insufficient. We argue that they form a distinct case, which we call resolvable insu...

---

### 19. AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models

**Authors:** Zihan Chen, Lei Nico Zheng, Di Zhu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14333v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14333v1)

**Summary:** Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from two anonymous large language models (LLMs) and pick the better one or say both are bad. We study 1,260,967 blind votes cast from May 2023 to August 2024 on pairs of models whose versions are fixed: dated vendor snapshots...

---

### 20. Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without High-Order Approximation

**Authors:** Yuchen Jiao, Na Li, Changxiao Cai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14328v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14328v1)

**Summary:** Stochastic diffusion samplers often require substantially more neural function evaluations (NFEs) than deterministic samplers to achieve comparable sample quality. Although higher-order discretization accelerates deterministic sampling, its benefits for stochastic sampling remains unclear. We establish matching upper and worst-case lower bounds showing that stochastic samplers with higher-order approximations remain first-order convergent, even with exact score functions. Thus, increasing the ap...

---

### 21. When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents

**Authors:** Runxuan Tang, Haoyu Gao, Yuyan Ding, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14326v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14326v1)

**Summary:** LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that represents each candidate ...

---

### 22. Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents

**Authors:** Yukyeong Lee, Yumin Choi, Jinheon Baek, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14320v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14320v1)

**Summary:** External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled only with task success or failure, yet are typically provided without the trajectori...

---

### 23. Multimodal Abstention That Preserves Acquired Correct Answers

**Authors:** Jinyuan Zhang

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14311v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14311v1)

**Summary:** Adding abstention to a task-adapted multimodal model can discard correct answers, including capabilities acquired during adaptation. We formulate abstention repair as maximizing correct abstention on unanswerable questions under a budget on newly lost correct answers. We propose ReFrain (Regression-Free Abstention), which combines a linear probe on first-token logits, threshold calibration on held-out image clusters, and a deterministic veto that replaces rejected outputs with the displayed "non...

---

### 24. LM-SimBench: A Unified Framework, Dataset, and Benchmark for Large Language Model Training Simulation

**Authors:** Yu Dong, Hong Li, Qiang Sun, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14285v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14285v1)

**Summary:** Evaluating candidate parallelization strategies through distributed training runs makes strategy selection prohibitively expensive at scale. Performance simulation offers a lower cost alternative, yet controlled comparisons among existing simulators remain difficult because they differ in the training stages they model and the workloads on which they are evaluated. We introduce LM-SimBench, a unified framework, profiling dataset, and benchmark for evaluating LLM training simulators. The framewor...

---

### 25. Ninety-Six Ways to Measure a Scribe: Fragmented Evaluation of Ambient Scribes in Healthcare

**Authors:** Amama Mahmood, Shiye Cao, Laura Fleig, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14284v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14284v1)

**Summary:** Ambient artificial intelligence (AI) scribes have moved rapidly from experimental pilots to enterprise-wide deployment across health systems, promising reduced documentation burden and improved clinician experience. While research evaluating these tools has expanded quickly, there are no agreed-upon protocols or standardized metrics for assessing their performance, making it difficult to compare findings or cumulatively synthesize evidence across studies. Across 54 recent evaluation studies, we ...

---

### 26. Achieving Robust Channel Estimation Neural Networks on Doppler effects by Designed Training Data

**Authors:** Dianxin Luan, John Thompson

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14267v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14267v1)

**Summary:** Channel estimation is crucial in wireless communication systems. Many existing works train and test their models using the same or similar channel. However, practical channels are infinitely diverse and time-variant while data-driven algorithms often degrade on new and previously unseen channels. This prohibits the practical implementation of neural networks for channel estimation, particularly in high speed scenarios characterized by rapidly channel profile changes and very high Doppler shifts....

---

### 27. Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning

**Authors:** Vikram Ramavarapu, Himanshu Udupi, Ashish Gautam

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14262v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14262v1)

**Summary:** Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for reinforcement learning are usually feed-forward, and it is unclear how to obtain functional modules in a recurrent SNN or what they buy. In this work, we introduce a class of spiking networks, called Community Recurrent SNNs (CoRe SNNs): recurrent networks partitioned into communities with fixed roles. A controller community receives the stimulus, e...

---

### 28. Lilo: A Multi-Agent Conversational Sandbox for Children's Digital Communication

**Authors:** Ofri Elbaum, Amit Malik, Tomer Malkevich, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14260v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14260v1)

**Summary:** Children's peer conflicts increasingly play out in group chats, where tone and timing are stripped away, and a hurtful message is easier to send than to say aloud. We present Lilo, a multi-agent conversational system that lets children practice such conversations, so they are better prepared when they encounter them in real digital communication. In Lilo, the child joins two AI-driven peers mid-argument, coached by a mentor character, also named Lilo, through a Stop-Think-Act traffic light. Thro...

---

### 29. A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents

**Authors:** Jingjing Jiang

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14256v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14256v1)

**Summary:** Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey investigates the structural source of asymmetric mechanism transfer across four scenarios: multimodal reasoning, multimodal generation, GUI and Web navigation, and embodied manipulation. We first formalize the self-evolving ...

---

### 30. Personalized Affective Perception via Continual Learning in Human-Agent Negotiation

**Authors:** Mehmet Onur Keskin, Berk Buzcu, Nikhil Churamani, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14247v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14247v1)

**Summary:** Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial Expression Recognition (CLIFER) to personalize valence-arousal perception in real time. Differential feedback converts changes in val...

---

### 31. An AI Assistant for Automating Anti-Corruption Expertise of Draft Legislation Based on the TRACE Framework

**Authors:** Serhii Zabolotnii, Alina Tarasova

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14244v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14244v1)

**Summary:** We present an AI assistant for automating anti-corruption expertise of draft legislation based on the TRACE architecture, designed to screen bills for corruption risks: pinpoint provisions an expert would criticise and name the regulatory defect in each. The pipeline combines a deterministic parsing core, model-guided single-provision qualification, rule-based factor assignment, and external human oversight. To evaluate the assistant, we constructed an open benchmark from the published conclusio...

---

### 32. Dyship: Leveraging Acoustic Features For Speaker Relationship Classification From Dyadic Conversations

**Authors:** Kieran Sturges, Thomas Thebaud, Yaohan Guan, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14241v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14241v1)

**Summary:** We introduce DyShip, a framework for classifying speaker familiarity and kinship from dyadic conversations in the Seamless Interaction corpus. We compare five speech representations: spectrograms, MFCCs, self-supervised WavLM representations, x-vectors, and estimated articulatory movements. Spectral features perform best for familiarity classification, reaching an accuracy of 87.81%, while WavLM achieves the highest kinship accuracy of 85.17%. X-vectors and articulatory features yield weaker res...

---

### 33. Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing

**Authors:** Naveen Babu Narayanan Nair, Sajay Kurup

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14211v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14211v1)

**Summary:** Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated Services Code Point (DSCP) value declaring agent traffic, a router-side classifier that demotes flows contradicting the declaration to a class served after best-effort traffic, and a rate-limited priority queue. VATC was...

---

### 34. Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse Attention Head Dropout

**Authors:** Karol Struniawski

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14209v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14209v1)

**Summary:** During extended wakefulness, mammalian neocortical networks experience localized periods of transient neuronal silence termed off-states. Here, we examine how analogous spatiotemporally concentrated disruptions affect sequential reasoning in autoregressive Large Language Models (LLMs). Evaluating 250 paired derivations on the GSM8K benchmark across two 8B models (Qwen3-8B and LLaMA-3.1-8B-Instruct), we contrast clustered bursts of attention head masking against budget-matched diffuse i.i.d. drop...

---

### 35. Joint Quantization and Dynamic Partitioning for Context-Aware Edge Vision Transformers

**Authors:** Zhu Jiaqi, Jain Prakriti, Katare Dewant, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14196v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14196v1)

**Summary:** Deploying vision transformer models across connected and automated vehicles (CAVs) requires joint management of computation and Vehicle-to-Vehicle (V2V) communication. Static split-inference methods use fixed partition points and cannot adapt to time-varying link bandwidth, processing load, and concurrent multi-stream traffic. This paper proposes an edge orchestration framework that jointly selects model partition points, per-layer quantization bitwidths, and execution placement across heterogen...

---

### 36. An Augmented Lagrangian Approach to Lifted Bellman Linear Programming

**Authors:** Jongchan Park, Hyukjun Yang, Narim Jeong, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14183v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14183v1)

**Summary:** Temporal-difference critics regress onto a bootstrapped target and usually need a target network. Lifted Bellman Linear Programming (LBLP) instead expresses the in-sample optimal values of offline RL as the solution to a linear program over the dataset. Its neural solver ALBUM relaxes the constraints into hinge penalties with fixed coefficients, and its guarantees are conditions on coefficients chosen in advance. We solve the same program with the method of multipliers: the coefficients become m...

---

### 37. Cross-Border Fulfillment Center Selection via Doubly Robust Estimation and Linear Programming

**Authors:** Kriti Mahajan, Patrick Bloebaum

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14174v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14174v1)

**Summary:** We introduce the cross-border (XB) fulfillment center (FC) Selection Model: a multi-stage optimization framework combining forecasting, doubly robust estimation, and linear programming to select optimal source FCs. For each source-destination shipping arc, the objective is to choose a subset of source-country FCs that minimize delivery time and cost while maximizing profit and shipped units under a fixed domestic network. We evaluate the model on three production-scale international shipping cor...

---

### 38. BARS: Budget-Aware Sequential Sampling with Refusal for Majority Identification under Unknown Distributions

**Authors:** Shenxi Liu, Yiwei Li, Mingyang Zhao, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14171v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14171v1)

**Summary:** Repeated sampling with majority selection is an effective means of enforcing self-consistency in large language models. Recently, a variant has also been introduced that terminates early to save costs when the output distribution is favorable. But it still cannot yield a correct confidence estimate from the answer distribution. For this issue, we formalize this as majority identification under an unknown distribution with a budget and a target error rate, and propose BARS, a sequential rule cert...

---

### 39. Representational Atoms in Neural Networks

**Authors:** Chenhui Hu, Pengfei Cao, Kang Liu, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14168v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14168v1)

**Summary:** Understanding the internal representations of neural networks and characterizing their relationship with human conceptual structure are two critical questions for elucidating model mechanisms. The former reveals how learned knowledge is organized in internal representations, whereas the latter provides a basis for interpreting these representations through human conceptual structure. Here, we formally define fundamental representational units (FRUs) and establish two evaluation criteria: fidelit...

---

### 40. Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs

**Authors:** Federico Ravenda, Mirko Cesarini, Daniele Montagnani, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14122v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14122v1)

**Summary:** Large language models (LLMs) achieve expert-level diagnostic accuracy in static evaluations, where the model receives a curated vignette or case report that already condenses the diagnostically relevant findings. Such evaluations measure inference over already selected evidence; the evaluations do not account for the inquiry used to obtain it. In clinical practice, however, diagnosis is an iterative process of inquiry. Clinicians take the patient's history, or anamnesis (Hx), through targeted qu...

---

### 41. Visual Similarity in Adult Word Extension and Artificial Word Learning

**Authors:** Patricio M. Vera

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14116v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14116v1)

**Summary:** When two objects share a name, how much does their visual similarity explain, and what do the teaching examples add? First, we reanalyzed trial-level data from a large adult word-extension study (Lewis & Frank, 2018), computing each test image's distance to the examples shown in the space of a frozen self-supervised visual encoder (DINOv2). Distance was associated with extension (log odds -3.23 per standard deviation; 520 people), and an exploratory post hoc analysis suggested that this associat...

---

### 42. Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos

**Authors:** Yuanhe Tian, Yan Song

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14113v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14113v1)

**Summary:** Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by describing a target object's states and transitions across video frames. Although multimodal large language models (MLLMs) generate detailed visual descriptions, these descriptions may leave the attributes needed to distinguish successive states insufficiently specified. In this paper, we propose look-ahead state readout (LASER), an anticipation...

---

### 43. Model-Free Runtime Measurement of Task-Relevant Information

**Authors:** Dimitris Panagopoulos, Adolfo Perrusquía, Yang Xing, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14111v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14111v1)

**Summary:** Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods to plan information seeking actions and interpret acquired observations, current approaches do not monitor whether the live process of information gathering is functioning properly. Consequently, such systems can remain operationally active without resolving outstanding mission requirements. To address this limitation, we introduce Acquisition-State...

---

### 44. ProofCoder: Continuous Reasoning for Automated Software Verification

**Authors:** Martim Afonso, Inês Lynce, Maurizio Morisio, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14106v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14106v1)

**Summary:** Formal verification using proof assistants provides strong correctness guarantees for software, but constructing proofs remains labor-intensive and requires significant expertise. Recent approaches based on large language models (LLMs) have shown promise in automating proof synthesis. However, these approaches typically constrain the model to a rigid tactic-generation loop, in which the surrounding system controls premise retrieval, proof-state management, and backtracking. We introduce ProofCod...

---

### 45. Sable: A Small-Field Sumcheck Argument for Bit-Exact Inference of Large Language Models

**Authors:** Tomer Solberg

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14083v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14083v1)

**Summary:** We present Sable, an argument system and single-GPU prover for the statement that a committed, integer-quantized transformer produced a given token sequence from a given prompt, bit for bit. Sable fixes an integer function F_O with no floating-point step, in which every rounding, normalization, softmax and sampling decision is determined by its inputs, and proves it with a constraint system whose relations provably never wrap modulo the 31-bit KoalaBear prime. The proof batches zerochecks and Lo...

---

### 46. From Bias to Positionality: A critical grammar for Large Language Models

**Authors:** Dave Murray-Rust, Elisa Giaccardi, Federico Bomba, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14079v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14079v1)

**Summary:** Bias has become a default lens for understanding what machine learning systems do and how we should relate to them. Bias is at root a deviation from a standard; in decision making systems we can supply a standard from outside: a law, a protected attribute, a benchmark, a statistical property. However, even there, biased is often used as a shorthand, without stating what the position taken is - a silent ``relative to''. In a general use of language models, nothing supplies the standard: there is ...

---

### 47. ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision

**Authors:** Haozhan Shen, Liangbo He, Jun Lan, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14076v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14076v1)

**Summary:** Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing supervision for this ability is challenging: questions must have correct, unambiguous answers that depend on actual fine-grained visual details rather than coarse cues or language priors. Verifying these properties makes manual annotation labor-intensive and automatic generation difficult for models that themselves struggle with fine-grained perception...

---

### 48. Obscured Wildfire Flame Detection by Spatio-temporal Analysis of Smoke Patterns Using Frame-wise Transformers

**Authors:** Uma Meleti, Abolfazl Razi, Fatemeh Afghah

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14074v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14074v1)

**Summary:** In this paper, we propose a new paradigm in wildfire management for detecting both visible and obscured fire using Deep Learning (DL). The essence of our method is the joint spatial and temporal analysis of RGB videos, embracing the fact that temporal patterns of smoke motions in consecutive video frames can indicate obscured fire flames. This perspective contrasts the traditional approach of independently analyzing images and individual video frames. To this end, we propose a frame-wise transfo...

---

### 49. HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency Response Scenarios

**Authors:** Rezwan Islam Salvi, Saiyma Sittul Muna, Mushfiqur Rahman Mushfique

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14059v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14059v1)

**Summary:** Emergencies can occur where there is no phone signal and no ambulance nearby. A small language model on a phone can be helpful in such situations, but its advice needs to be safe and accurate. We built HandsOnAid, a 4-bit Gemma 2B model fine-tuned with QLoRA on FirstAidQA dataset, a corpus of 5,550 first-aid question-answer pairs. We compared seven configurations, including the base, 4-bit and 8-bit fine-tuned models, and versions with a length floor, safety gate, or retrieval. We used a 41-pair...

---

### 50. Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study

**Authors:** Zhikun Tao, Fangyong Jin, Junping Zhao

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14051v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14051v1)

**Summary:** Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve. We investigate direct cache reuse across four model updates, with a detailed study of DeepSeek-V4-Flash to Flash-0731. Our central finding is that caches can retain useful task information without faithfully reproducing the updated model's behavior. Retrieval accuracy varies substantially acros...

---

## cs.CL

**50 papers**

### 1. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models

**Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14515v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14515v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turn...

---

### 2. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

**Authors:** Ziang Liu, James J. Kim, Yijia Dai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14514v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14514v1)

**Summary:** LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusiv...

---

### 3. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents

**Authors:** Howard Zhang, Chuck Arvin, Logan Brown, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14493v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14493v1)

**Summary:** Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies e...

---

### 4. Mechanistic Interpretability Needs a Logic of Inference

**Authors:** Zhimin Hu, Chen Jiang, Hanbo Xie, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14483v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14483v1)

**Summary:** Neural networks are increasingly studied not merely as predictive systems, but as complex systems whose internal computations are themselves objects of scientific inquiry. Recent progress in mechanistic interpretability (MI) has made it possible to identify neurons, features, circuits, population structures, and dynamical patterns associated with model behavior. As these tools improve, attention is shifting from what can be observed inside a model to how those observations support mechanistic ex...

---

### 5. Pterodactyl: Pushing the Limits of Efficient Automated Translation Evaluation

**Authors:** Evelyn Y. Garland, Carola F. Berger

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14480v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14480v1)

**Summary:** In this paper, we present 1020 Group's submission to the WMT26 shared task on automated quality evaluation. Our system, Pterodactyl, was engineered specifically for subtasks 2 and 3, that is, segment-level quality score prediction and the detection of error-free segments. Pterodactyl is a highly customizable, ultra-low cost system optimized for binary classification in translation triage and data curation. It is based on an LLM-as-a-judge approach, with prompt engineering and model selection gui...

---

### 6. FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking

**Authors:** Arjun Rao, Nishant Gopinath

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14477v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14477v1)

**Summary:** Text-to-SQL systems over large pooled catalogs must first retrieve the tables a question needs. We compare against the published table recall of RASL, which uses Claude 3.5 models to extract keywords and select tables, on pooled BIRD, Spider, and Fiben catalogs. FERN (Feature-Engineered Ranking with No generative LLM) instead fuses three frozen retrievers into 100 candidates, describes each with up to 120 features, and reorders them with LightGBM rankers fitted once on BIRD's training questions....

---

### 7. When does text encoding matter for language modeling?

**Authors:** Eugene Jang, Catherine Arnett, Terra Blevins

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14459v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14459v1)

**Summary:** UTF-8's role as the de facto encoding standard in language models introduces cross-lingual inequities due to its variable-length design. However, the effect that this encoding choice has on model performance remains largely unexamined. In this work, we investigate how text encoding impacts the performance of byte-level language models, comparing UTF-8 with a wide range of other encoding strategies, including other Unicode-based approaches, language-specific encodings, and our own customized enco...

---

### 8. Earlybird: Predictive Streaming Speech Recognition in 29M Parameters

**Authors:** Sahil Mahendrakar

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14421v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14421v1)

**Summary:** Streaming speech recognizers output a word only after the speaker has finished it, typically 90-400 ms later. For a voice agent every millisecond counts: the sooner the words are outputted, the sooner the agent can start a search or plan its reply. We present Earlybird, a 29M-parameter streaming recognizer (16.8 MB at 4 bits). Earlybird learns from audio cut off at random points, including partway through a word, and is asked to predict every word that is due by then in full, plus a guess of the...

---

### 9. Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models

**Authors:** Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14413v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14413v1)

**Summary:** Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes the second worse, and which is the cheaper way to spend a fixed budget. On Qwen3-0.6B and Qwen3-1.7B with simulated round-to-nearest weight quantization (8, 6, 4 and 3 bits, fp16 reference), read from the logits of the letters A to D on ARC-Easy, ARC-Challenge, MMLU and HellaSwag (300 items each), 6 b...

---

### 10. REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding

**Authors:** Yu Tian

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14399v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14399v1)

**Summary:** Speculative decoding accelerates LLM inference by having a draft model propose multiple tokens for the target model to verify in one pass. The speedup is governed by the expected acceptance length (EAL), yet standard training objectives such as cross-entropy, KL divergence, and total variation focus only on distribution matching or single-step overlap. Recent studies instead propose block-level training objectives, aiming to optimize EAL directly. However, these objectives remain surrogates rath...

---

### 11. Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models

**Authors:** Amir Mann, Jonathan Fhima, Shaked Brody, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14387v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14387v1)

**Summary:** Diffusion Language Models (DLMs) have emerged as effective alternatives to autoregressive models for latency-critical tasks, enabling faster token generation. Recent advances employ block diffusion with self-editing capabilities, where each block refines tokens iteratively before advancing to the next one. Yet each block is only as fast as its slowest token, and the next block cannot start before it. We suggest Blurring the Block Boundaries (B3), a novel method with which two blocks are refined ...

---

### 12. ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces

**Authors:** Jiahang Lin, Wanying Ren, Wanghan Xu, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14364v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14364v1)

**Summary:** Research agents achieve increasingly strong benchmark scores, yet these scores do not necessarily translate into reliable delivery in ongoing research projects. Many research-agent benchmarks emphasize standalone tasks and relatively self-contained workflows in clean or curated workspaces. However, researchers ask agents to complete one step within an ongoing project, where requests depend on earlier session decisions and workspaces contain unfinished files, outdated versions, and failed attempt...

---

### 13. EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities

**Authors:** Zhengxiang Huang, Yujie Sun, Shengheng Chen, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14356v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14356v1)

**Summary:** Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly system challenge. Each model may require coordinated changes across conversion, graph construction, operators, and hardware backends. Existing coding agents often miss these cross-layer dependencies and struggle to diagnose failures across host--device execution paths. We present EngineAgent, an agentic system for automating on-device LLM model ena...

---

### 14. AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models

**Authors:** Zihan Chen, Lei Nico Zheng, Di Zhu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14333v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14333v1)

**Summary:** Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from two anonymous large language models (LLMs) and pick the better one or say both are bad. We study 1,260,967 blind votes cast from May 2023 to August 2024 on pairs of models whose versions are fixed: dated vendor snapshots...

---

### 15. Point-in-Time Encoders for Earnings Calls

**Authors:** Alessio Brini

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14325v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14325v1)

**Summary:** Text encoders turn earnings calls into vectors for search, for language models that answer from retrieved passages, and for forecasting models. A live retriever can use an encoder trained once on all available text, as finance retrievers are, but a backtest needs an encoder that read no text written after the date of each vector. To address this look-ahead bias, from 412,248 calls we train vintages under four pretraining recipes, with yearly cutoffs from 2010 to 2024, and each vintage reads only...

---

### 16. MMDM: Measuring Massive Multitask Decision Making

**Authors:** Junhao Shen, Qing Zong, Yue Guo, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14309v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14309v1)

**Summary:** System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on existing benchmarks, where prior exposure to test material can obscure generalization. Moreover, real-world decision making often involves long contexts, large option spaces, and complex logical dependencies, challenges...

---

### 17. Semantic Chains: From Reachable Facts to Justified Answers

**Authors:** Misha Andreev

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14252v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14252v1)

**Summary:** How can the facts that justify an answer be found from a question and presented as a sequence of connected statements? This paper models a context as a graph of logical facts and takes as given which expressions represent each fact. A parent fact can express a relation among its subfacts, and a preserving edge allows the content of a subfact to be recovered within a full representation of its parent. Suppose a root fact justifies the full answer and a path of preserving edges leads from that roo...

---

### 18. An AI Assistant for Automating Anti-Corruption Expertise of Draft Legislation Based on the TRACE Framework

**Authors:** Serhii Zabolotnii, Alina Tarasova

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14244v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14244v1)

**Summary:** We present an AI assistant for automating anti-corruption expertise of draft legislation based on the TRACE architecture, designed to screen bills for corruption risks: pinpoint provisions an expert would criticise and name the regulatory defect in each. The pipeline combines a deterministic parsing core, model-guided single-provision qualification, rule-based factor assignment, and external human oversight. To evaluate the assistant, we constructed an open benchmark from the published conclusio...

---

### 19. Dyship: Leveraging Acoustic Features For Speaker Relationship Classification From Dyadic Conversations

**Authors:** Kieran Sturges, Thomas Thebaud, Yaohan Guan, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14241v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14241v1)

**Summary:** We introduce DyShip, a framework for classifying speaker familiarity and kinship from dyadic conversations in the Seamless Interaction corpus. We compare five speech representations: spectrograms, MFCCs, self-supervised WavLM representations, x-vectors, and estimated articulatory movements. Spectral features perform best for familiarity classification, reaching an accuracy of 87.81%, while WavLM achieves the highest kinship accuracy of 85.17%. X-vectors and articulatory features yield weaker res...

---

### 20. StaRSE: Compact Russian Sentence Embeddings with a Sign-Coded Static Encoder

**Authors:** Boris Malashenko, Ivan Jarsky, Egor Soldatov, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14236v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14236v1)

**Summary:** Transformer sentence encoders provide strong retrieval quality, but their inference cost becomes a bottleneck when embeddings must be produced on CPUs or refreshed frequently. We introduce StaRSE, a compact Russian static sentence encoder that removes Transformer inference at deployment time: token directions are stored as sign bits, token norms are stored separately, and sentences are encoded by mean pooling over norm-scaled sign directions. StaRSE is initialized from ruBERT-base, fine-tuned on...

---

### 21. Stagewise and interpretable emergence of inside-outside computation in Transformer-based language models

**Authors:** Jack T. Parley

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14221v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14221v1)

**Summary:** Variability in syntactic structure and parsing ambiguity are fundamental aspects of natural language which modern LLMs have to learn to deal with proficiently. Previous "post-mortem" studies have shown that fully trained Transformers indeed approximate canonical parsing algorithms such as inside-outside, but little is established theoretically about how this is actually learned. Here, we make a first step towards addressing this by studying the learning dynamics in synthetic context-free grammar...

---

### 22. Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse Attention Head Dropout

**Authors:** Karol Struniawski

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14209v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14209v1)

**Summary:** During extended wakefulness, mammalian neocortical networks experience localized periods of transient neuronal silence termed off-states. Here, we examine how analogous spatiotemporally concentrated disruptions affect sequential reasoning in autoregressive Large Language Models (LLMs). Evaluating 250 paired derivations on the GSM8K benchmark across two 8B models (Qwen3-8B and LLaMA-3.1-8B-Instruct), we contrast clustered bursts of attention head masking against budget-matched diffuse i.i.d. drop...

---

### 23. Representational Atoms in Neural Networks

**Authors:** Chenhui Hu, Pengfei Cao, Kang Liu, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14168v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14168v1)

**Summary:** Understanding the internal representations of neural networks and characterizing their relationship with human conceptual structure are two critical questions for elucidating model mechanisms. The former reveals how learned knowledge is organized in internal representations, whereas the latter provides a basis for interpreting these representations through human conceptual structure. Here, we formally define fundamental representational units (FRUs) and establish two evaluation criteria: fidelit...

---

### 24. Visual Similarity in Adult Word Extension and Artificial Word Learning

**Authors:** Patricio M. Vera

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14116v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14116v1)

**Summary:** When two objects share a name, how much does their visual similarity explain, and what do the teaching examples add? First, we reanalyzed trial-level data from a large adult word-extension study (Lewis & Frank, 2018), computing each test image's distance to the examples shown in the space of a frozen self-supervised visual encoder (DINOv2). Distance was associated with extension (log odds -3.23 per standard deviation; 520 people), and an exploratory post hoc analysis suggested that this associat...

---

### 25. Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in Image-Conditioned VLMs via Dual-Prompted LoRA Decoders

**Authors:** Mikhail Kulakov, Ruslan Solikhov, Ivan Bondarenko

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14100v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14100v1)

**Summary:** We present our system for the SHROOM-visions 2026 shared task on character-level hallucination span detection in image-conditioned vision-language model (VLM) responses, evaluated across English, French, Italian, and Chinese. The detector is built on a frozen Gemma-4-12B-it backbone with trainable LoRA adapters (approximately 10.7M parameters). Because the backbone is a causal decoder, hidden states read from a single copy of an answer cannot attend to subsequent tokens; we therefore repeat the ...

---

### 26. From Bias to Positionality: A critical grammar for Large Language Models

**Authors:** Dave Murray-Rust, Elisa Giaccardi, Federico Bomba, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14079v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14079v1)

**Summary:** Bias has become a default lens for understanding what machine learning systems do and how we should relate to them. Bias is at root a deviation from a standard; in decision making systems we can supply a standard from outside: a law, a protected attribute, a benchmark, a statistical property. However, even there, biased is often used as a shorthand, without stating what the position taken is - a silent ``relative to''. In a general use of language models, nothing supplies the standard: there is ...

---

### 27. HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency Response Scenarios

**Authors:** Rezwan Islam Salvi, Saiyma Sittul Muna, Mushfiqur Rahman Mushfique

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14059v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14059v1)

**Summary:** Emergencies can occur where there is no phone signal and no ambulance nearby. A small language model on a phone can be helpful in such situations, but its advice needs to be safe and accurate. We built HandsOnAid, a 4-bit Gemma 2B model fine-tuned with QLoRA on FirstAidQA dataset, a corpus of 5,550 first-aid question-answer pairs. We compared seven configurations, including the base, 4-bit and 8-bit fine-tuned models, and versions with a length floor, safety gate, or retrieval. We used a 41-pair...

---

### 28. Thermodynamics of words

**Authors:** Klaus M. Frahm, Dima L. Shepelyansky

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14039v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14039v1)

**Summary:** We introduce the word thermalization hypothesis according to which in a literary work there are effective interactions between words that drive them to thermalization where their word frequency distribution is the same as for the phenomenon of Rayleigh-Jeans (RJ) thermalization and condensation. In this concept, the different words play a role of classical oscillators (particles) and their word frequencies, or related tokens, are analogous to certain filling factors over energy state levels. The...

---

### 29. MISO-BR: An Open Corpus for Misogyny Detection in Brazilian Portuguese

**Authors:** Fábio A. S. Passos, Péricles B. C. Miranda, Ana Paula Cavalcanti

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14036v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14036v1)

**Summary:** Misogyny is among the most prevalent forms of online hate speech directed at Brazilian users, yet open and auditable resources dedicated to it in Brazilian Portuguese remain scarce. We introduce MISO-BR, an open, documented and versioned corpus of 896 balanced social media texts annotated for binary misogyny, released with its construction protocol and reproducible baselines. The corpus combines lexicon- and target-guided scraping from X with items imported from OLID-BR, a large language model t...

---

### 30. Program-Aided Patchable Skill Evolution

**Authors:** Jiahao Wang, Yuqi Xiong, Qing Yang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14019v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14019v1)

**Summary:** Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modifying model parameters. Recent approaches further improve skill adaptation by distilling reusable experience from agent execution trajectories and evolving skills based on downstream task feedback. However, existing methods primarily represent skills as natural language documents, intertwining procedural logic with descriptive knowledge and making ...

---

### 31. One Sequence Is Enough: Fingerprinting Language Models from Fixed-Length Integer Sequences

**Authors:** Fantong Meng, Chengjie Sun, Shuangjia Yang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14010v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14010v1)

**Summary:** Users of model APIs and third-party platforms often rely on the declared model name to identify the model responding to their requests. However, the actual model may differ from the declared one, motivating identity verification based on observable outputs. Previous studies have shown that preferences in simple numerical-choice tasks can serve as model fingerprints. We investigate whether a single fixed-length integer sequence can combine multiple numerical observations to identify its source mo...

---

### 32. Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation

**Authors:** Lirui Luo, Kelong Mao, Xinwei Yang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14009v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14009v1)

**Summary:** Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. They must therefore decide what to write down and what to read back, and when to do either. Recent work has begun to use on-policy distillation (OPD) to make memory control part of the policy, relying on memory tools and compaction protocols that lie outside either model's pre-training. However, this weakens the distillation on both sides: the teacher cannot give useful gui...

---

### 33. Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models

**Authors:** Xingqi Wang, Xiaoyuan Yi, Xing Xie, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13997v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13997v1)

**Summary:** Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities but raise significant privacy concerns due to their abilities to infer sensitive personal information from images with high precision. While current LVLMs are relatively well aligned to protect universal privacy, e.g., credit card data, we argue that privacy is inherently personalized and context-dependent. This work pivots towards a novel task: can LVLMs achieve Inference-Time Personalized Privacy Protection (ITP$^3$...

---

### 34. On the information rate of phones, syllables and words

**Authors:** Herman Kamper

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13990v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13990v1)

**Summary:** Which linguistic units minimise the bitrate required to encode speech content: phones, syllables, words, maybe larger units, or something in between? This question has implications for the development of speech and language systems and theories of human language processing. Using a transcribed corpus of 960 hours of English audiobooks, I compare the information rates of phones, syllables, words, multi-word combinations and intermediate tokenisations. While all units are equivalent under a perfec...

---

### 35. Understanding Mixture-of-Experts Language Models Beyond Expert Boundaries

**Authors:** Zhenhong Zhou, Mao Zheng, Mingyang Song, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13975v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13975v1)

**Summary:** In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial. Reports of domain-associated expert preferences contrast with analyses attributing routing primarily to token identity or syntactic patterns. To clarify these differing accounts, we look beyond expert-level routing to investigate the neuron-level organization of domain-specialized computation using Routing-Aware Magnitude Profiling (RAMP), a measure developed for this analysis. Using mixed-domain calib...

---

### 36. AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark

**Authors:** Haotian Qi, Gabriel Skantze

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13957v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13957v1)

**Summary:** } Predicting who will speak next, and when, is a prerequisite for conversational agents and social robots that take turns without waiting for silence. Multiparty next-speaker prediction (NSP) has been studied on corpora with per-speaker sensors, each with its own event definitions. No public benchmark covers the single camera and microphone a robot has, and no model has been compared against how well people perform the same prediction. We turn AVCC, a 31-hour audio-visual corpus of two- and thre...

---

### 37. Beyond Fluent Responses: Finding User Dissatisfaction in Human-AI Interactions

**Authors:** Yuka Saito, Ikumi Numaya, Jun Suzuki, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13894v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13894v1)

**Summary:** As large language models generate increasingly high-quality responses, recent work on response evaluation has moved beyond response-centered criteria, such as correctness and coherence, toward user-centered criteria, including user preferences and perceived usefulness. This shift is fundamentally important for developing technologies that are truly useful to real-world users. While conventional response evaluation quantifies the quality of the response itself, users' satisfaction in real convers...

---

### 38. Are Causal Neuron Circuits Unique and Transferable?

**Authors:** Ömer Tekin Yavuz

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13885v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13885v1)

**Summary:** Interpretability demonstrations often show that intervening on a group of neurons changes a model's answer. A recent example removes an 18-neuron group in Qwen3-32B and the model answers "Simba" instead of "Scar" to a two-hop Lion King riddle. Such a demonstration establishes that the group matters, but not how much of it is necessary, whether other groups could do the same, or whether the effect carries over to other inputs. We ask: when intervening on a group of neurons changes a model's answe...

---

### 39. Beyond Passive Imitation: On-Policy Mid-Training Distillation for Language Models

**Authors:** Ruize Zheng, Xuyang Liu, Siyu Ren, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13855v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13855v1)

**Summary:** Continual pre-training (CPT) adapts large language models (LLMs) to specialized domains, yet its standard next-token prediction (NTP) objective treats every corpus token as a fixed target, regardless of its utility to the current model. In a controlled study on the same 1B-token mathematical corpus, we observe sharply different outcomes across base models: NTP improves Llama-3.2-3B's performance on mathematical benchmarks but substantially degrades Qwen3-1.7B-Base's performance, indicating that,...

---

### 40. Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning

**Authors:** Sezgin Saygili, Emre Kaplaner, Oncel Ozgul, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13845v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13845v1)

**Summary:** We present Alania-2, a Turkish text-to-speech (TTS) system with two built-in voices, voice design from text descriptions, and two kinds of voice cloning. Alania-2 is a 488M-parameter model with the VoxCPM architecture, which generates continuous audio latents with a diffusion head on top of a language-model backbone. We train it from scratch on 18,195 hours of Turkish speech, 90% of which is synthetic speech produced by a larger teacher model and filtered automatically. A text normalizer rewrite...

---

### 41. PolyRoute: A Twelve-Language and Code-Mixed Benchmark for Typed-Decision Routing, with Baselines and a Leaderboard

**Authors:** Mohammed Nayeem Khan, Sarun Kumar K S

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13843v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13843v1)

**Summary:** Typed-decision encoders answer a question about a text in one forward pass, but their behaviour outside English is rarely measured on a fixed yardstick. We release PolyRoute: 322 native-language support messages in 12 languages and 9 writing systems, 156 code-mixed or romanised messages (Hinglish, Spanglish, Arabizi), 967 optional native training rows, and a protocol for a three-way department-routing decision. Labels come from Qwen3.8-27B with a blind second pass (91% of candidates kept); an in...

---

### 42. Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-speech model trained entirely on synthetic speech

**Authors:** Sezgin Saygili, Emre Kaplaner, Oncel Ozgul, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13811v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13811v1)

**Summary:** Antalia-2 Mini is a single-voice Turkish text-to-speech model with 7,620,931 parameters. It reads characters and produces 48 kHz audio at 41 times real time on an Apple M5 laptop CPU (2 threads). Its training audio came only from VoxCPM2 (the teacher), about 300 times larger, cloning one synthetic clip; automatic checks kept about 1,790 h. Fine-tuning the vocoder on the acoustic model's own mel spectrograms cut the word error rate (WER) of Whisper's transcripts from a mean of 3.89% to 1.75% at a...

---

### 43. LLM Validation Makes Minimal-Pair Benchmarks Easier for Language Models

**Authors:** Guofang Tang

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13788v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13788v1)

**Summary:** Minimal-pair benchmarks are only as good as their labels, and LLMs are an obvious substitute for costly human validation. We test it on BLiMP (English) and QFrBLiMP (Quebec French), the two public minimal-pair datasets releasing every forced-choice human judgment. Three LLMs validate by forced choice, by rating, and as a panel, scored against human panels of one, three and five judges in two pre-registered phases. On BLiMP, forced-choice validators agree with held-out human majorities more often...

---

### 44. Word-Level Alignment of OCR and Ground Truth under Zoning and Reading-Order Errors

**Authors:** Fonseca Cacho, Jorge Ramón

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13752v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13752v1)

**Summary:** OCR post-processing needs OCR text aligned word by word with its ground truth. Data sets rarely provide that mapping, and a monotone aligner can lose its place when zoning errors permute the reading order. We revisit this problem, the Zoning Problem of our 2019 paper, with a protocol that tests correctness under such permutations. We apply OCR-side reading-order permutations with construction-time word-level gold and score correct-match F1, cascade length and recovery. We compare the 2019 locati...

---

### 45. Do Language Models Feel the Sentiment? Investigating Emotion Vectors

**Authors:** Ali Hassan Khan, Saad Bin Ather, Muhammad Saif, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13744v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13744v1)

**Summary:** Emotion vectors are directions in a language model's internal representations that are associated with emotional concepts. Prior work shows that these vectors can influence model behavior, but their role in sentiment classification remains unclear. This study investigates emotion directions in Qwen2.5-0.5B-Instruct and Qwen2.5-3B-Instruct. Eight directions extracted from GoEmotions are evaluated through sentiment probing, activation interventions, and supervised correction. Emotion-only probes a...

---

### 46. Walrus Technical Report

**Authors:** Alkis Koudounas, Osamu Take, Hayato Futami, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13689v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13689v1)

**Summary:** We present Walrus, a unified 8B speech-and-audio foundation model handling speech recognition (including code-switching and multi-talker speech), speech-to-text and speech-to-speech translation, text-to-speech, emotion recognition, audio captioning, and general audio understanding. Our main contribution is not a new architecture but a data-centric training recipe; we use a standard decoder-only backbone initialized from Gemma 4, so that gains can be traced to the data. For speech generation, Wal...

---

### 47. You Are What You Read: Indian Political News Media Bias Dataset for Hindi Language

**Authors:** Kushal Trivedi, Mayank Mahor, Dhruv Sanghvi, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13686v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13686v1)

**Summary:** Media bias understanding and detection remains an under-researched problem for Indian context, specifically for Indic languages, such as, Hindi, which is widely spoken in India. In this paper, we introduce a comprehensive, multi-annotator, explainable dataset consisting of 448 unique articles from four leading Indian news agencies publishing in Hindi. We focus on Hindi, the most spoken and an official language of India. The study of media bias is particularly relevant in the Indian context due t...

---

### 48. OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation

**Authors:** Senhao Liu, Yuheng Zhang, Chunyu Wei, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13675v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13675v1)

**Summary:** Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is expensive, while aggressive textual compression discards fine-grained information that is irreversibly lost in a one-dimensional token sequence. We argue that this bottleneck is not fundamental to information density but to the choice of compression \emph{modality}. Modern visual encoders can pack the contents of a rendered text page into roughly a ...

---

### 49. An Interpretable Stylometric Framework for Early Chinese Buddhist Translator Styles: A Case Study on the Attribution of Disputed Works of An Shigao

**Authors:** Yating Pan, Xinyue Zhang, Jun Wang

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13636v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13636v1)

**Summary:** Attributing early Chinese Buddhist translations requires evidence that scholars can trace back to the texts. We develop an interpretable stylometric framework that uses features defined or reviewed by Buddhist philologists, including function characters, sentence formulas, sentence-final characters, sentence length, and part-of-speech n-grams. We construct stylistic profiles from 31 authenticated translations by seven translators from the Eastern Han through the Western Jin, then compare eight d...

---

### 50. Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control

**Authors:** Zhiyuan Huang, Shengan Zheng, Chenghu Yang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13615v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13615v1)

**Summary:** Large language model agents reuse execution experience to improve reliability on complex tool-based tasks. Systems such as Sentry call large models to generate failure diagnoses before retrieving advice, adding inference cost to experience reuse. We present Synapse-Control, an agent runtime whose lightweight control plane selects advice and determines when to send it to the task-executing model. Rules shortlist relevant advice, and a lightweight 1.7B classifier fine-tuned on teacher-labeled stat...

---

## cs.CV

**50 papers**

### 1. Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training

**Authors:** Emre Kutlusan, Yongmin Li

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14519v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14519v1)

**Summary:** Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what deter...

---

### 2. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR

**Authors:** Sheethal Bhat, Bogdan Georgescu, Awais Mansoor, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14518v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14518v1)

**Summary:** DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by...

---

### 3. Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model: Linking an Adversarial and a Perceptual Illusion

**Authors:** Alexandre Garcia-Duran, Alejandro Rodriguez-Garcia, Manuel Molano-Mazón, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14498v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14498v1)

**Summary:** Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Whether networks with brain-like wiring are more robust at lower computational cost is unclear. We address this by benchmarking a task-optimized, continuous-time recurrent neural network of the fly visual system constrained by its synaptic connectome (FlyNet) against artificial neural networks. We com...

---

### 4. RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval

**Authors:** Tanishq Rachamalla, Srishti Kaushik, Muhammad Attique Khan, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14496v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14496v1)

**Summary:** Cross-sensor remote sensing image retrieval aims to find scenes with the same content across heterogeneous sensors, such as SAR and optical or panchromatic (PAN) and multispectral (MS) imagery, without manual labels. Existing self-supervised methods either reconstruct sensor-specific pixel detail, align each image only with its co-registered twin, or rely on large transformers with 118-173M parameters (and up to 398M). We introduce RS-JEPA, a compact joint-embedding predictive framework built on...

---

### 5. Mechanistic Interpretability Needs a Logic of Inference

**Authors:** Zhimin Hu, Chen Jiang, Hanbo Xie, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14483v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14483v1)

**Summary:** Neural networks are increasingly studied not merely as predictive systems, but as complex systems whose internal computations are themselves objects of scientific inquiry. Recent progress in mechanistic interpretability (MI) has made it possible to identify neurons, features, circuits, population structures, and dynamical patterns associated with model behavior. As these tools improve, attention is shifting from what can be observed inside a model to how those observations support mechanistic ex...

---

### 6. BoviShift: A Six-Year Multi-Attribute Audit of Visual Cattle Phenotyping Across Animals and Time

**Authors:** Mobasshir Bhuiya Shagor, Nilambar Halder Tonmoy, Md Saef Ullah Miah

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14476v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14476v1)

**Summary:** Computer vision offers a scalable, non-contact means of estimating livestock traits, but correlated images and video frames make reliable evaluation difficult. Image-random splitting can place views of the same animal in both training and test sets, while deployment further requires transfer to animals captured in future years. We introduce BoviShift, a corpus reconstructed from six consecutive annual cohorts of an operational cattle marketplace collected from 2021 to 2026. It contains 2{,}657 c...

---

### 7. TanCRAFT: Context-Reasoned Anticipatory Feedback for Assembly Tasks

**Authors:** Sassan Mokhtar, Lars Doorenbos, Marius Bock, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14470v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14470v1)

**Summary:** Preventing human error in physical assembly tasks requires assistance systems that can intervene before mistakes are made. This is especially challenging in settings where users are free to choose the construction order and correctness depends on the evolving assembly rather than a fixed next step. We present TanCRAFT, a four-stage real-time predictive assistance system that tracks the scene state, reasons about the current partial assembly, forecasts the near-future motion of manipulated pieces...

---

### 8. C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference

**Authors:** Guorui Lu, Qinyu Chen

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14469v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14469v1)

**Summary:** Visual Question Answering (VQA) imposes substantial computational overhead on vision-language models (VLMs), motivating model-agnostic input reduction methods that can be readily applied across diverse VLMs, including in black-box settings. Simply enforcing a visual-token cap reduces computation, but it can discard information needed to answer the question. A single reduction strategy also struggles to accommodate different scenarios. Our key observation is that cropping and compression are comp...

---

### 9. A Lightweight Differentiable Method for Real-Time Skin Rendering and Digitization

**Authors:** Mario Marquez-Balduque, Carlos Rodriguez-Pardo, Jorge Lopez-Moreno

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14451v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14451v1)

**Summary:** Inverse rendering for skin typically relies on offline path tracing to estimate physical properties, which fail to map directly to the approximate shaders utilized in interactive applications, such as game engines. We bridge this gap by directly estimating subsurface scattering parameters tailored for real-time rendering pipelines. We introduce a differentiable Screen-Space Subsurface Scattering (SSSS) framework that enables the joint optimization of spatially varying base textures and scatterin...

---

### 10. UGG: Unified Generative Geometry Model

**Authors:** Amani Kiruga, Zhiyi Li, Ruojin Cai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14440v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14440v1)

**Summary:** Understanding 4D scenes is a core challenge in visual intelligence, requiring models to jointly capture scene geometry, appearance, and dynamics from partial observations. However, existing approaches are subdivided into feedforward models for direct geometric prediction, and generative models for visual synthesis. We introduce UGG, a unified framework for 4D scene understanding that jointly models RGB video and geometric representations such as depth and camera pose. By assigning different nois...

---

### 11. Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection

**Authors:** Luka Dragar, Peter Peer, Vitomir Štruc, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14436v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14436v1)

**Summary:** Deepfake detectors are commonly evaluated on real/fake classification alone, but real-world applications require explanations of the visual evidence behind each prediction. Joint vision-language models struggle with authenticity assessment, producing "real" narratives for manipulated images. To address this, we propose a decoupled predict-then-explain pipeline as our submission to the ACM Multimedia 2026 Explainable Deepfake Detection Challenge, with methods trained and evaluated on the XPlainVe...

---

### 12. One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge

**Authors:** Ilia Larchenko, Gleb Zarin, Atindra Nair, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14432v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14432v1)

**Summary:** We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion ...

---

### 13. OnlyAct: Extracting Action Representations from Foundation Models for World Models

**Authors:** Runjia Li, Minghao Chen, Junyu Xie, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14420v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14420v1)

**Summary:** Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragmented across incompatible specifications, and do not scale with the unlabeled video pretraining corpus. A common workaround jointly trains an action encoder to compress consecutive frames into a latent action and a decoder to reconstruct the next frame from the previous frame and that latent, forcing the latent to capture only new information. Thi...

---

### 14. What Factors Matter for Collection-Level Counting with Human-AI Collaboration?

**Authors:** Seoyun Jeong, Logan Lawrence, Owen L. Martin, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14380v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14380v1)

**Summary:** Many scientific and policy decisions require estimating the total number of target objects across a large image collection. Exhaustive human labeling is often infeasible, while raw model predictions can be biased, especially under domain shift. Recent human-AI estimation methods combine imperfect model predictions with limited human verification to obtain reliable collection-level estimates. However, existing work provides little guidance on how practitioners should choose among models, estimato...

---

### 15. From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models

**Authors:** Guoqiang Liang, Yiqi Lin, Yanzhe Chen, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14365v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14365v1)

**Summary:** Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future observations. Building such models requires injecting low-dimensional robot signals (e.g. proprioception, actions, and values) into a latent space shaped by natural videos, and a key design choice is the interface through which these signals enter: existing schemes treat it as a formatting detail, spending a separate latent frame on each signal or bo...

---

### 16. Multimodal Abstention That Preserves Acquired Correct Answers

**Authors:** Jinyuan Zhang

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14311v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14311v1)

**Summary:** Adding abstention to a task-adapted multimodal model can discard correct answers, including capabilities acquired during adaptation. We formulate abstention repair as maximizing correct abstention on unanswerable questions under a budget on newly lost correct answers. We propose ReFrain (Regression-Free Abstention), which combines a linear probe on first-token logits, threshold calibration on held-out image clusters, and a deterministic veto that replaces rejected outputs with the displayed "non...

---

### 17. TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation

**Authors:** Qijun Gan, Chenwei Zhang, Xinyang Li, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14307v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14307v1)

**Summary:** Streaming multi-reference video generation establishes a scene from specified people and objects, then continues it under changing instructions. We introduce TaoMate-R1, a streaming multi-reference generator that organizes adaptation parameters through temporal role specialization. It assigns separate low-rank adapters to scene establishment and continuation on a frozen backbone. Each adapter performs both denoising and context writing for its role; Self Gradient Forcing jointly trains the roles...

---

### 18. ForeseeDrive: Future-Token Conditioning for Anticipatory Generative Driving

**Authors:** Shaokai Wu, Xunchu Zhou, Pinzhi Wang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14286v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14286v1)

**Summary:** Generative driving planners can represent diverse ego futures, but a downstream scorer can choose only among sampled candidates; it cannot recover an absent maneuver. We present ForeseeDrive, which turns future scene evolution into a deployable interface for shaping candidate generation. Rather than reconstructing dense future states or scoring a fixed menu, ForeseeDrive derives query-indexed tokens from logged actor motion, occupancy evolution, route interactions, and TTC margins, and predicts ...

---

### 19. UniFlow-RS: Unified Generative Prediction for Heterogeneous Remote-Sensing Tasks

**Authors:** Jianlong He, Liang Liao, Jing Xiao, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14281v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14281v1)

**Summary:** Remote-sensing foundation models increasingly unify representations across sensing modalities and downstream tasks, yet their prediction mechanisms remain largely task-specific. Separate decoders, prediction heads, and objectives leave prediction fragmented across tasks. This naturally raises a question: can heterogeneous remote-sensing tasks share the prediction process? UniFlow-RS answers this question with a single latent flow-matching predictor shared across tasks. This requires addressing t...

---

### 20. AutoThreshold: Joint Confusion-Profile Learning for Adaptive Mask Binarization

**Authors:** Shaokai Wu, Xunchu Zhou, Pinzhi Wang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14279v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14279v1)

**Summary:** A single validation-tuned threshold can become brittle when dense-score distributions shift. We introduce AutoThreshold, a post-hoc policy that predicts the joint mass of positive and negative pixels over score bins. This target directly parameterizes threshold-indexed confusion counts, avoiding products of independently estimated prevalence and class-conditional rates. Softmax normalization and cumulative decoding yield coherent, monotone confusion profiles; a plug-in decoder then selects a thr...

---

### 21. Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control

**Authors:** Haitian Li, Tianfu Li, Xuxi Zhao, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14257v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14257v1)

**Summary:** World-Action Models improve robot control by predicting future visual dynamics, but iterative video denoising incurs substantial inference overhead. Recent approaches reduce this cost through partial future denoising, yet typically rely on fixed refinement budgets. Our empirical observations reveal that preferred refinement depths vary across tasks and states, while different future regions exhibit varying relevance to action generation. Motivated by these findings, we propose Elastic-WAM, which...

---

### 22. Location Matters: Sparse Latent-Variance Attacks for Face Privacy against Diffusion Personalization

**Authors:** Shuting Yang, Shuxin Li, Linyan Dai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14254v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14254v1)

**Summary:** Text-to-image diffusion models can learn and reproduce an individual's identity from only a few reference photos, creating risks of unauthorized and misleading content generation. Proactive defenses address this risk by adding adversarial perturbations to facial images before release, thereby disrupting identity acquisition during downstream personalization. However, existing methods typically rely on dense $L_\infty$-bounded perturbations, whose accumulated distortions can become visible around...

---

### 23. ViGA-FLAME: Aligning Latent Visual and Geometric Representations for Robust 3D Head Expression Estimation

**Authors:** Wen Hao He, Jiacheng Wu, Jie Chen

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14218v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14218v1)

**Summary:** Estimating 3D head expression from a single image requires mapping visual appearance to underlying facial geometry. We propose ViGA-FLAME, a two-stage framework that aligns semantic visual features with a structured geometric latent space. First, a Parametric-Geometric Variational Autoencoder (PG-VAE) learns a unified representation of canonical head surfaces and FLAME parameters, supporting both detailed surface reconstruction and interpretable parameter recovery. Supervision on geometry and pa...

---

### 24. DailyWildfireCAN: A Dataset and Benchmark for Next-Day Wildfire Spread Prediction in Canada

**Authors:** Mahacine Ettahri, Hager Radi Abdelwahed, Toluwaleke Olutayo, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14207v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14207v1)

**Summary:** Wildfires represent a critical ecological and socio-economic challenge in Canada, where vast boreal forests and a warming climate have amplified the frequency and severity of extreme fire seasons. Predicting next-day wildfire spread can support fire management, but requires capturing complex interactions among weather, fuels, and terrain. Deep learning has emerged as a promising approach to learning these relationships from heterogeneous environmental data, yet its development and evaluation dep...

---

### 25. SpecValley: Aggregation as Spectral Valley in Dense Heterophilic Graphs

**Authors:** Christoph Jahn, Delvin Bacho, Urs Waldmann, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14176v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14176v1)

**Summary:** Node classification in heterophilic graphs remains an open problem: aggregating over neighbourhoods can damp precisely the part of the signal that carries the labels. The field has answered with ever more expressive propagation operators, leaving the aggregation step that precedes them fixed by degree normalisation. However, degree normalisation acts as a spectral valley in its own right, attenuating a fixed middle band whose position at lambda equal 1 is set by the normalisation rather than by ...

---

### 26. GARD: Gradient-Guided Adversarial Representation Defense against Backdoors in Multimodal Contrastive Learning Models

**Authors:** Yuhong Wang, Yujun Cai, Lei Feng, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14143v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14143v1)

**Summary:** Multimodal contrastive learning models such as CLIP are vulnerable to backdoor attacks with diverse trigger structures, ranging from localized patches to globally distributed perturbations, with recent attacks increasingly optimizing these triggers in the representation space. Existing post-hoc defenses based on clean fine-tuning may leave backdoors active, while trigger-inversion methods depend on accurately estimating the attack target and trigger. We observe that backdoored encoders exhibit s...

---

### 27. HaiRuo: Forecasting Ocean Eddies as Fields and Objects with a Satellite-Altimetry Foundation Model

**Authors:** Xukun Qin, Haochen Sun, Yuyang Tian, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14136v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14136v1)

**Summary:** Mesoscale eddies carry most of the ocean's kinetic energy and move heat, salt and nutrients across basins, yet where an eddy will be two weeks ahead is still read off ocean models with post-hoc tracking heuristics. We introduce HaiRuo, which forecasts eddies as fields and as objects at once: from 30 days of satellite sea-level maps, one forward pass returns 15 days of sea level and geostrophic velocity, daily eddy masks and the trajectory of every eddy alive today. HaiRuo pairs two components wi...

---

### 28. Sim(3)-TurboReg: Robust and Efficient Scale-Aware Registration via Tri-Scale Consistency

**Authors:** Zijun Zhou, Shaocheng Yan, Zhenjun Zhao, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14135v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14135v1)

**Summary:** Feed-forward 3D foundation models recover geometry at high fidelity, yet inference memory constraints keep them from processing long sequences natively. Current streaming systems work around this limit with sliding-window chunking, which introduces severe monocular scale ambiguity. Resolving this ambiguity requires Sim(3) registration that stays accurate and efficient under outlier contamination. We introduce Sim(3)-TurboReg, which reformulates the compatibility graph construction of TurboReg by...

---

### 29. Continuous 3D Spatial Transcriptomics Reconstruction via Histology-Informed Implicit Neural Representations

**Authors:** Kaito Shiku, Ryoma Bise, Ahtisham Fazeel Abbasi, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14129v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14129v1)

**Summary:** Three-dimensional spatial transcriptomics (3D ST) enables the analysis of gene-expression patterns across tissue depths. However, 3D ST measurements are acquired from discrete 2D tissue sections, which are often sparsely sampled due to high acquisition costs. To address this limitation, we propose a histology-informed multi-task implicit neural representation (HIM-INR) for continuous 3D gene-expression reconstruction from sparse ST observations. HIM-INR jointly reconstructs gene-expression profi...

---

### 30. CroCoMAE: Cross-modal self-supervised collaborative representation learning for SAR-optical remote sensing data

**Authors:** Vito Recchia, Giuseppe Guarino, Cássio Fraga Dantas, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14124v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14124v1)

**Summary:** Remote sensing increasingly captures the Earth's surface through complementary sensors such as SAR and optical, yet ground-truth annotations remain scarce, limiting supervised approaches. Self-supervised learning (SSL) addresses the label scarcity, and cross-modal SSL further exploits the complementarity between co-located sensors, but existing cross-modal frameworks align modalities mostly through global image-level representations or treat them as largely redundant, leaving their fine-grained ...

---

### 31. TAMEing the Open-World Personalization: Towards Open-Set Personalized MLLM Assistant

**Authors:** Rongpei Hong, Jian Lang, Ting Zhong, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14118v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14118v1)

**Summary:** Personalizing Multimodal Large Language Models (MLLMs) as intelligent assistants has recently emerged as an active research topic, where an MLLM is expected to go beyond generic, one-size-fits-all replies, and instead generate responses grounded in user-specific objects, entities, and concepts encountered during interactions. Nevertheless, existing studies mainly focus on personalizing MLLMs on a static, predefined set of personalized concepts and require users to manually and frequently extend ...

---

### 32. Visual Similarity in Adult Word Extension and Artificial Word Learning

**Authors:** Patricio M. Vera

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14116v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14116v1)

**Summary:** When two objects share a name, how much does their visual similarity explain, and what do the teaching examples add? First, we reanalyzed trial-level data from a large adult word-extension study (Lewis & Frank, 2018), computing each test image's distance to the examples shown in the space of a frozen self-supervised visual encoder (DINOv2). Distance was associated with extension (log odds -3.23 per standard deviation; 520 people), and an exploratory post hoc analysis suggested that this associat...

---

### 33. Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos

**Authors:** Yuanhe Tian, Yan Song

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14113v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14113v1)

**Summary:** Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by describing a target object's states and transitions across video frames. Although multimodal large language models (MLLMs) generate detailed visual descriptions, these descriptions may leave the attributes needed to distinguish successive states insufficiently specified. In this paper, we propose look-ahead state readout (LASER), an anticipation...

---

### 34. ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision

**Authors:** Haozhan Shen, Liangbo He, Jun Lan, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14076v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14076v1)

**Summary:** Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing supervision for this ability is challenging: questions must have correct, unambiguous answers that depend on actual fine-grained visual details rather than coarse cues or language priors. Verifying these properties makes manual annotation labor-intensive and automatic generation difficult for models that themselves struggle with fine-grained perception...

---

### 35. Obscured Wildfire Flame Detection by Spatio-temporal Analysis of Smoke Patterns Using Frame-wise Transformers

**Authors:** Uma Meleti, Abolfazl Razi, Fatemeh Afghah

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14074v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14074v1)

**Summary:** In this paper, we propose a new paradigm in wildfire management for detecting both visible and obscured fire using Deep Learning (DL). The essence of our method is the joint spatial and temporal analysis of RGB videos, embracing the fact that temporal patterns of smoke motions in consecutive video frames can indicate obscured fire flames. This perspective contrasts the traditional approach of independently analyzing images and individual video frames. To this end, we propose a frame-wise transfo...

---

### 36. Where Do Vision-Language Models Get Left and Right? Position-Code Counterfactuals in Qwen2.5-VL, Qwen3-VL and InternVL3

**Authors:** Enhao Cui, Junzhi Yang, Yaoshun Lin, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14060v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14060v1)

**Summary:** A vision-language model may take left-right direction from the orientation of image content within patches, its vision transformer's (ViT) position code, or token positions and order in its language model (LLM). Ablations show the ViT code is necessary; we test sufficiency by mirroring only a position code. In Qwen2.5-VL-7B, Qwen3-VL-4B and InternVL3-2B, mirroring ViT width positions reproduces the flipped-image answer on 84.3-93.2% of CV-Bench left-right questions (Qwen2.5-VL-3B: 87.5%, partly ...

---

### 37. CURRENT: A Recurrent Neural Network for Concurrent Spatial and Temporal Super-Resolution of 4D Flow MRI

**Authors:** Luuk Jacobs, Pietro Dirix, Sebastian Kozerke

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14058v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14058v1)

**Summary:** Objective: To improve the spatial and temporal resolution of aortic 4D flow MRI through a unified deep learning framework for post-acquisition super-resolution (SR) of reconstructed velocity vector fields.   Methods: We propose CURRENT, a recurrent neural network that performs spatial and temporal SR with a single network architecture. Supervised training was conducted using paired low- and high-resolution datasets generated by embedding computational fluid dynamics simulations of aortic flow in...

---

### 38. Structured Confidence Perturbation via Fisher Geometry for Adversarial Training

**Authors:** Chenlong Wei, Hanling Wang, Chong Zhang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14046v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14046v1)

**Summary:** Adversarial training is often plagued by "pseudo-attacks", perturbations that significantly increase the loss value but fail to truly alter the model's confidence structure. To address this, we propose two complementary approaches to directly attack and defend against confidence structure deformation. First, building upon the traditional loss maximization perspective, we introduce a hybrid objective that integrates cross-entropy and KL divergence, encouraging adversarial examples to simultaneous...

---

### 39. Few-Step Streaming Video Generation via Condition Shifting

**Authors:** Deyuan Liu, Jungang Li, Kaiwen Zheng, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14033v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14033v1)

**Summary:** Few-step sampling reduces the cost of streaming video generation. Distribution Matching Distillation (DMD) supervises few-step generators with a separate fake-score network, which adds training memory and computation and must track the evolving generator. We extend APEX to streaming video by using condition shifting to estimate the velocity field of the generated distribution within the generator. The original text condition selects generation, while a shifted condition selects fake estimation u...

---

### 40. HiPFuse: Real-Time LiDAR Semantic Segmentation for Robotic Perception on Edge Devices

**Authors:** Haiyang Wu, George Vosselman, Ville Lehtola

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14025v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14025v1)

**Summary:** Real-time robotic perception requires accurate LiDAR semantics under limited resources. Bird's-eye-view (BEV) aggregation is efficient but can mix differently labeled surfaces in columns. We present HiPFuse, a point-BEV fusion framework that exchanges point and height-partitioned BEV features across horizontal scales, combining point-wise detail with 2D spatial context from one LiDAR scan. Fixed height assignments preserve separate vertical aggregation groups, with auxiliary supervision of initi...

---

### 41. Interleaving anatomical inspection and diagnostic reasoning for explainable radiology report generation

**Authors:** Chentao Huang, Runlong Lin, Zhijun Wang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14018v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14018v1)

**Summary:** Automated radiology report generation can draft clinically plausible reports, yet the pathway from visual evidence to reported findings remains opaque, leaving the diagnostic basis of these reports unexplained and the generated reports difficult to review or revise. We introduce ARIVE (Anatomy-guided Reasoning with Interleaved Visual Evidence), an explainable report generation framework that interleaves anatomical inspection with diagnostic reasoning prior to final report composition. To support...

---

### 42. A Stage-Wise Explainable Pipeline for Arteriolar-to-Venular Ratio Estimation and Retinopathy Screening

**Authors:** Sharan Sharmeela Karuppannan, Yoga Sri Varshan, Subin Sahayam, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14013v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14013v1)

**Summary:** The arteriolar-to-venular diameter ratio (AVR) is a clinically motivated marker of retinal vascular health. We present a five-stage pipeline for AVR estimation and exploratory retinopathy screening from fundus images, with inspectable intermediate outputs at each stage. The pipeline combines vessel and artery-vein masks, optic-disc localization, vessel-calibre estimation using a minimal-chord boundary walk, and AVR computation from dominant arterial and venular branches. An explicit threshold-ba...

---

### 43. Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models

**Authors:** Xingqi Wang, Xiaoyuan Yi, Xing Xie, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13997v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13997v1)

**Summary:** Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities but raise significant privacy concerns due to their abilities to infer sensitive personal information from images with high precision. While current LVLMs are relatively well aligned to protect universal privacy, e.g., credit card data, we argue that privacy is inherently personalized and context-dependent. This work pivots towards a novel task: can LVLMs achieve Inference-Time Personalized Privacy Protection (ITP$^3$...

---

### 44. Lipschitz-Controlled Flow Matching for Robust Image Restoration

**Authors:** Sedjro Salomon Hotegni, Konstantin Sonntag, Paul-Christian Bürkner, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13995v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13995v1)

**Summary:** Flow-matching models can produce high-quality image restorations, but their learned dynamics may amplify small input perturbations and make reconstructions unstable. We introduce LipsFlower to reduce this amplification. We derive stability bounds for Flow-from-$Y$, which initializes the ordinary differential equation from a noise-perturbed observation, as well as for observation-conditioned posterior sampling, which conditions the velocity field on the observation throughout integration. Based o...

---

### 45. Pulse or Provenance? What rPPG-Based Deepfake Detectors Learn

**Authors:** Othmane Harraq, Tamer Aldwairi

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13992v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13992v1)

**Summary:** Remote photoplethysmography (rPPG) has been proposed as a physiological cue for deepfake detection, based on the premise that synthesized faces lack a genuine cardiac signal. We examine what rPPG-style detectors learn on Celeb-DF++ (22 forgery methods) and FaceForensics++ (FF++), using one identically sampled window per real and fake video. On talking-face forgeries, simple chrominance traces reach an AUC of 0.998, exceeding a dedicated rPPG extractor (0.87). Controlled experiments indicate that...

---

### 46. TransGHOST: Real-Time, Synthesis-Free Reconstruction of Instrument-Occluded Regions in Ophthalmic Microsurgery

**Authors:** Niran Nataraj, Maina Sogabe, Masamichi Yamashita, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13971v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13971v1)

**Summary:** Intraoperative scene perception in ophthalmic microsurgery is limited by instrument occlusion: when a tool enters the high-magnification field, it conceals tissue from both the surgeon and the perception components of robot-assisted systems that process the video. Generative inpainting can remove the occluder but replaces the missing image content with synthesis, which is unsuitable when visual provenance matters. Many video inpainters also depend on future frames and cannot operate online. We p...

---

### 47. Counterfactual Analysis of Extent Leakage from Annotation-Derived Prompts in Vision-Language Medical Image Segmentation

**Authors:** Niran Nataraj, Ankita Das, C. Krishna Mohan, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13970v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13970v1)

**Summary:** Text-guided segmentation models receive an image and a short caption about the lesion, and on public benchmarks the caption improves accuracy considerably. On colonoscopy and breast ultrasound, however, the size, count and location words of each caption were computed from the mask that later scores the prediction, and the chest X-ray captions were written by benchmark annotators. We tested what two published models take from them. On colonoscopy and chest X-ray, it is mostly the lesion's extent....

---

### 48. RB-LDC: Redundancy-Balanced Latent Coding for Noise-Robust Diffusion Latents

**Authors:** Hyunseok Jeong, Jaeho Jeon, Young-Sik Kim

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13955v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13955v1)

**Summary:** Latent diffusion models decode approximately correct latents, making decoder sensitivity to perturbations relevant to image quality. After whitening, forward diffusion corrupts every direction at the same signal-to-noise ratio (SNR), despite unequal decoder sensitivities. We study an invertible linear layer between the encoder and diffusion process that shifts each direction's log-SNR. Its linear minimum mean-square-error (LMMSE) recovery risk has an exact spectral expression for any whitened la...

---

### 49. MEOW: Medical Open-World Interactive Segmentation

**Authors:** Philip Matthias Winter, Maria Wimmer, Bernhard Schäfl, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13935v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13935v1)

**Summary:** In open-world recognition, machine learning models not only make predictions on unknown structures ("generalized open-set"), but also continually learn and improve from those predictions over time. Interactive segmentation, despite its access to user feedback, has so far remained confined to the open-set setting. In this work we introduce MEOW, the first framework that turns non-interactive segmentation backbones into interactive open-world learners without updating learnable model parameters. M...

---

### 50. The Case for AI-Enabled Gate Monitoring as Farm Security in the UK: A PRISMA-Guided Review of the Evidence on Rural Crime, Livestock Predation and Farm Access

**Authors:** Steve Symes, Paul Fergus, Mark Carr, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13933v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13933v1)

**Summary:** Farm security in the UK rests on thinner evidence than its cost suggests. We ran a PRISMA guided review: twelve searches of Web of Science and Scopus on 2nd -4th November 2026 returned 1,183 records (761 unique), and grey-literature and hand-searches added 35 assessed sources. We synthesised 96 database records and 24 grey sources narratively. UK peer-reviewed evidence is small (16 records), and the main UK survey of crime and farmer mental health has 80 responses. Cost estimates rest on insurer...

---

## cs.LG

**50 papers**

### 1. TorchCurves: Differentiable Parametric Curves

**Authors:** Alex Shtoff

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14516v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14516v1)

**Summary:** We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curve coefficients can be optimized jointly with the surrounding model or produced by another network. The library provides trainable modules, reusable basis modules, and a functional interface, supportin...

---

### 2. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models

**Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14515v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14515v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turn...

---

### 3. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

**Authors:** Ziang Liu, James J. Kim, Yijia Dai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14514v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14514v1)

**Summary:** LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusiv...

---

### 4. Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents

**Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14511v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14511v1)

**Summary:** Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-based scores perform near chance, highlighting the difficulty of interpreting available chemical sign...

---

### 5. When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology

**Authors:** Yeyuan Liu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14508v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14508v1)

**Summary:** Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, gains or plasticity rates the model also needs, and modellers often tune these until the real-wiring model works. We separate three estimands: physiology tuned on the real wiring and transferred to null...

---

### 6. Continual-ARC: Measuring Skill Acquisition over a Working Lifetime

**Authors:** Daniel Lenton

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14505v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14505v1)

**Summary:** Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so memory-based and weight-based systems are rarely compared on the same scale. We propose Continual-ARC, a lifelong stream built from the three ARC-AGI editions, whose tasks need no domain knowledge. The...

---

### 7. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions

**Authors:** Adi Mashiach

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14504v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14504v1)

**Summary:** Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-ligand sequences. From a single representation space, Bonbon exhibits three zero-shot emergent capabilities at hierarchical levels of resolution: functional (mechanism of action), residue (binding site l...

---

### 8. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents

**Authors:** Howard Zhang, Chuck Arvin, Logan Brown, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14493v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14493v1)

**Summary:** Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies e...

---

### 9. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

**Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14492v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14492v1)

**Summary:** Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often...

---

### 10. TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series Analytics

**Authors:** Peng Chen, Yihang Wang, Zhongwen Rao, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14491v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14491v1)

**Summary:** Time series analytics has been widely applied across various domains. While existing time series foundation models (TSFMs) have demonstrated promising results, they still face two major challenges: 1) Most TSFMs mainly rely on stacking Transformer layers to increase parameter size, lacking the ability to adaptively model complex time series patterns from multi-domain data. 2) Current TSFMs are primarily pre-trained for specific tasks, e.g., forecasting or anomaly detection, and a few models supp...

---

### 11. C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference

**Authors:** Guorui Lu, Qinyu Chen

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14469v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14469v1)

**Summary:** Visual Question Answering (VQA) imposes substantial computational overhead on vision-language models (VLMs), motivating model-agnostic input reduction methods that can be readily applied across diverse VLMs, including in black-box settings. Simply enforcing a visual-token cap reduces computation, but it can discard information needed to answer the question. A single reduction strategy also struggles to accommodate different scenarios. Our key observation is that cropping and compression are comp...

---

### 12. Bayesian inverse problems and epidemic-threshold uncertainty for a heterogeneous SIS reaction-diffusion model

**Authors:** Duc-Lam Duong

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14468v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14468v1)

**Summary:** We study Bayesian inference of persistence from early observations of a heterogeneous susceptible--infected--susceptible (SIS) reaction--diffusion model with standard incidence. We show that the leading prevalence dynamics depend on the unknown coefficients only through the difference between the transmission and recovery rates and the infected diffusivity. The same pair determines the principal eigenvalue whose sign governs persistence, so early prevalence can inform the threshold even when the...

---

### 13. A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets

**Authors:** Audrey Huang, Nan Jiang, Sham M. Kakade, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14467v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14467v1)

**Summary:** Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to identify algorithms that learn near-optimal policies using total samples and gradient steps governed by the base model's response coverage, a measure of how readily it generates optimal responses. We call such algorithms coverage-preserving. This guarantee captures the goal of amplifying capabilities accessible through sampling from the base model.   ...

---

### 14. A Theory of Cross-Validation Variance

**Authors:** Nathaniel S. O'Connell, Jaime L. Speiser

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14463v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14463v1)

**Summary:** Cross-validation estimates predictive performance by repeatedly splitting the data into training and validation sets, fitting the model on the first and evaluating it on the second. Every observation influences the estimate in two roles, through its own evaluation when it is held out and through the models it helps fit when it trains. The random splits determine its weight in each role. From this representation, we prove an exact finite-sample identity for the variance of the cross-validated est...

---

### 15. Accurate predictions of properties of energetic materials with tabular foundation models

**Authors:** Vagn Krister Nes Glomsrud, Mathias Bynke, Lars Henry Berge Olsen, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14462v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14462v1)

**Summary:** We use TabPFN, a recently developed tabular foundation model, to predict three properties of energetic materials: impact sensitivity, decomposition temperature and crystal density. Without any hyperparameter tuning, TabPFN outperforms the best published models for all three properties. It also substantially outperforms a wide range of established machine-learning models, including tuned gradient boosting (XGBoost), random forests and Gaussian processes. This holds both when the models are given ...

---

### 16. UGG: Unified Generative Geometry Model

**Authors:** Amani Kiruga, Zhiyi Li, Ruojin Cai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14440v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14440v1)

**Summary:** Understanding 4D scenes is a core challenge in visual intelligence, requiring models to jointly capture scene geometry, appearance, and dynamics from partial observations. However, existing approaches are subdivided into feedforward models for direct geometric prediction, and generative models for visual synthesis. We introduce UGG, a unified framework for 4D scene understanding that jointly models RGB video and geometric representations such as depth and camera pose. By assigning different nois...

---

### 17. One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge

**Authors:** Ilia Larchenko, Gleb Zarin, Atindra Nair, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14432v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14432v1)

**Summary:** We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion ...

---

### 18. Quantifying the Sampling Frequency Invariance of Time-Series Foundation Models for Sensor Data Applications

**Authors:** Sourish Gunesh Dhekane, Abinaya Kumar, Torsten Woertwein, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14425v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14425v1)

**Summary:** Time-Series Foundation Models (TSFMs) are increasingly used in sensor applications, where sampling frequency (SF) varies across sensors, devices, and operating modes (e.g., power saving). Ideally, TSFMs must remain effective during such SF changes, provided the SF retains task-critical bandwidth. In this paper, we stress-test 4 prominent TSFMs: MOMENT, Chronos-2, Moirai-MoE, and TimesFM, to quantify their SF-invariance and investigate whether their behavior tracks the resulting loss of informati...

---

### 19. DnNP: Denoising Input Uncertainty in Neural Processes

**Authors:** Fatemeh Tohidian, Chengzhi Shi, Soomi Lee, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14424v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14424v1)

**Summary:** Neural Processes (NPs) are flexible meta-learning models capable of uncertainty quantification across diverse applications. However, the standard NP framework assumes access to noise-free inputs. This is unrealistic in many practical settings, where sensor noise or measurement errors are unavoidable. This discrepancy between model assumptions and real-world data can significantly degrade prediction quality and uncertainty estimates. We introduce Denoising Neural Processes (DnNPs), a principled e...

---

### 20. Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity

**Authors:** Lucas de Souza Brandão, Gabriel da Costa Merlin, Diego Furtado Silva

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14415v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14415v1)

**Summary:** Audio foundation models like CLAP, MuQ, and MERT excel at capturing general musical similarity. On the other hand, their entangled latent spaces limit interpretability and fine-grained attribute control. Conditional Similarity Networks (CSN) address this by pairing a backbone representation model with learned masks that gate the embedding space into attribute-specific subspaces. However, existing methods train the backbone from scratch, rather than leveraging pretrained foundation models. We ins...

---

### 21. Causal Concept Explanations for Deep Neural Models

**Authors:** Josh Rountree, Pulkit Verma, Oswin So, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14407v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14407v1)

**Summary:** Concept-based explanations in neural models are important for the development, certification, and adoption of autonomous systems. Yet, interpretability remains correlational. Without methods to guide and quantify causal relationships between explanations, a concept explanation can be provided without being necessary or sufficient for the observed output thereby appearing correct while misleading. We introduce Causal Concept Wrapper Network (CCW-Net), the first use of interventional mediation ana...

---

### 22. Discovering Equations for the Thermodynamics of South Asian Monsoon Precipitation

**Authors:** Savannah L. Ferretti, Jane W. Baldwin, Michael S. Pritchard, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14401v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14401v1)

**Summary:** South Asian monsoon precipitation depends on the thermodynamic structure of the lower troposphere, but how its ingredients combine to shape precipitation remains unclear, partly because this dependence is nonlocal in the vertical. We use symbolic distillation, which combines neural networks and symbolic regression, to discover interpretable precipitation equations from 21 years of June-August reanalysis data. Neural networks first learn the vertical thermodynamic structure most relevant to preci...

---

### 23. REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding

**Authors:** Yu Tian

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14399v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14399v1)

**Summary:** Speculative decoding accelerates LLM inference by having a draft model propose multiple tokens for the target model to verify in one pass. The speedup is governed by the expected acceptance length (EAL), yet standard training objectives such as cross-entropy, KL divergence, and total variation focus only on distribution matching or single-step overlap. Recent studies instead propose block-level training objectives, aiming to optimize EAL directly. However, these objectives remain surrogates rath...

---

### 24. A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)

**Authors:** Ziqing Xu, Hancheng Min, Lachlan Ewen MacDonald, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14397v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14397v1)

**Summary:** Low-rank adaptation (LoRA) is the de facto method for parameter-efficient fine-tuning of large neural networks, achieving strong task adaptation with minimal trainable parameters and low optimization cost. Beyond this efficiency, practitioners have observed two striking properties: \textit{robustness to catastrophic forgetting} and the ability to \textit{merge independently trained adapters} into a single model that performs competitively across multiple tasks. These properties are central to co...

---

### 25. An Energy-Based Perspective on Machine Learning

**Authors:** Bo Dai, Yilun Du

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14383v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14383v1)

**Summary:** Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many. This tutorial has a broader goal: beyond introducing EBMs, it uses them as a single lens that connects the different aspects of machine learning. Any EBM is specified by three choices, the energy, which determines what the model represents; the inference procedure, which samples from or optimizes the energy; and the learning method, whi...

---

### 26. Uncertainty-Aware Hybrid Offline Reinforcement Learning with Online Action Selection Enabled by Sparse Gaussian-Process Critics

**Authors:** Marco Chan, Christos Evripidou, Liqiu Dong, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14374v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14374v1)

**Summary:** Start-ups and grade changes remain largely operator-driven, while developing and maintaining dynamic models for model-based control requires substantial engineering effort. Hybrid Offline Learning and Online Optimisation (HOFLON) uses one-step offline reinforcement learning to select actions from historical transition data. In its original implementation, the online objective combines the predicted return from a tree-ensemble critic with an adversarial-autoencoder (AAE) penalty for unfamiliar st...

---

### 27. The Unused Input: The Initial State as a Conditioning Interface for Recurrent TSFMs

**Authors:** Bernhard Voggenberger, Christian Ganhör, Levente Zólyomi, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14357v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14357v1)

**Summary:** Time series foundation models (TSFMs) forecast unseen series without task-specific training. Increasingly they are built on recurrent backbones, whose constant per-step cost makes long-context inference cheap, and which, unlike transformers, carry a state. A recurrent backbone computes its prediction from two inputs: the observed context window and the initial recurrent state. In practice only the first is utilised and the initial state is unused by convention. We ask whether the initial state c...

---

### 28. Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without High-Order Approximation

**Authors:** Yuchen Jiao, Na Li, Changxiao Cai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14328v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14328v1)

**Summary:** Stochastic diffusion samplers often require substantially more neural function evaluations (NFEs) than deterministic samplers to achieve comparable sample quality. Although higher-order discretization accelerates deterministic sampling, its benefits for stochastic sampling remains unclear. We establish matching upper and worst-case lower bounds showing that stochastic samplers with higher-order approximations remain first-order convergent, even with exact score functions. Thus, increasing the ap...

---

### 29. When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents

**Authors:** Runxuan Tang, Haoyu Gao, Yuyan Ding, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14326v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14326v1)

**Summary:** LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that represents each candidate ...

---

### 30. Auditing the Judge: Internal Signals for LLM Reasoning Assurance

**Authors:** Mayank Gulati, Gerhard Wunder

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14323v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14323v1)

**Summary:** Language-model systems use self-judgment to decide which answers to release, review, or recompute. Because intervention is costly, an assurance score must rank errors well at the available budget, not merely over the full ranking. We compare the judge's continuous verdict-token score with a supervised correctness probe trained on attention-head activations from the same prompt. Exact identities link fixed-budget error recall to residual risk and show that AUROC averages recall over all budgets. ...

---

### 31. MammothDP: Private Boosted Decision Trees Ready for Trusted Hardware and Leakage-free Hyperparameters

**Authors:** Moritz Kirschte, Thorsten Peinemann, Kari Kostiainen, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14317v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14317v1)

**Summary:** Data spaces like the European Health Data Space (EHDS) require the protection of sensitive data in studies during the data's processing and the study's release alike. In this work, we investigate how to implement this mandate using established trusted execution environments (TEEs) and timing side-channel hardening to protect the processing even under a compromised server, and the state-of-the-art differential privacy (DP) notion to protect the release of studies on tabular data. This combined se...

---

### 32. PSL-RGHA: Parallel Split Learning with Reference Gradient Half-Space Alignment for Mitigating Gradient Divergence

**Authors:** Han Li, Zheng Lin, Miao Yang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14312v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14312v1)

**Summary:** The escalating complexity of deep neural networks hinders the deployment of federated learning (FL) on resource-constrained devices, especially for multimedia applications such as on-device image classification and speech recognition. Parallel split learning (PSL) has emerged as a promising solution by offloading a substantial portion of the computational workload to the server through layer-wise model partitioning, making it particularly suitable for resource-limited visual and speech intellige...

---

### 33. Multimodal Abstention That Preserves Acquired Correct Answers

**Authors:** Jinyuan Zhang

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14311v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14311v1)

**Summary:** Adding abstention to a task-adapted multimodal model can discard correct answers, including capabilities acquired during adaptation. We formulate abstention repair as maximizing correct abstention on unanswerable questions under a budget on newly lost correct answers. We propose ReFrain (Regression-Free Abstention), which combines a linear probe on first-token logits, threshold calibration on held-out image clusters, and a deterministic veto that replaces rejected outputs with the displayed "non...

---

### 34. MMDM: Measuring Massive Multitask Decision Making

**Authors:** Junhao Shen, Qing Zong, Yue Guo, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14309v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14309v1)

**Summary:** System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on existing benchmarks, where prior exposure to test material can obscure generalization. Moreover, real-world decision making often involves long contexts, large option spaces, and complex logical dependencies, challenges...

---

### 35. Compositional random forest

**Authors:** Khaled Masoumifard, Stephan van der Westhuizen, Sugnet Gardner-Lubbe

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14275v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14275v1)

**Summary:** Compositional data have been analysed in the literature from three main points of view: directly on the simplex, in log-ratio coordinates, and as directional data on the unit sphere. In this paper, we construct a random forest framework for compositional responses that accommodates all three. Random forests are ensembles of decision trees, and the split criterion determines how each tree grows. We use the log-likelihood gain as the split criterion and consider distributions defined on the differ...

---

### 36. Federated Learning for Cross-Regional Epidemic Forecasting with Asynchronous Outbreaks

**Authors:** Ruibin Liu, Francisco Fernandes, Xuanfeng Li, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14272v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14272v1)

**Summary:** Objective: Epidemic outbreaks are often asynchronous across regions, yet collaborative forecasting is hampered by privacy laws and heterogeneous public health interventions. We developed and evaluated, as a proof of concept, a federated learning (FL) framework for cross-regional COVID-19 forecasting under asynchronous outbreaks among Guangdong, Macau, and Portugal, while maintaining data sovereignty.   Methods: Using daily case data from WHO and China CDC for the three regions, whose outbreaks w...

---

### 37. Physics-Constrained Autoencoder for Interpretable Health Representation Learning in Turbofan Engines

**Authors:** Leonardo Baldo, Jokin Alcibar Ibarzabal, Daniel Cisneros Acevedo, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14266v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14266v1)

**Summary:** Health Indices (HIs) summarize degradation from operational data and support diagnostic and prognostic tasks in Prognostics and Health Management (PHM). Their usefulness depends on capturing degradation and interpreting system condition. Autoencoders learn such representations from unlabelled monitoring data; however, when training is driven only by reconstruction, the physical meaning of latent variables remains undefined, limiting their interpretation and diagnostic value. This work proposes a...

---

### 38. Chain of Physics: Supporting Fault Diagnosis with Engineering-Inspired Large Language Model Reasoning

**Authors:** Wenqi Zhou, Leonardo Baldo, Kai Goebel, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14263v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14263v1)

**Summary:** Fault diagnosis in complex systems requires linking observed changes in physical quantities to the failure mechanisms that produce them. Experienced engineers perform this task by combining sensor information with knowledge of system behavior and fault propagation. Large Language Models (LLMs) can support this process, but their diagnostic reasoning depends on the availability of asset-specific engineering knowledge and on how this knowledge is represented and used during inference. This work in...

---

### 39. Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning

**Authors:** Vikram Ramavarapu, Himanshu Udupi, Ashish Gautam

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14262v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14262v1)

**Summary:** Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for reinforcement learning are usually feed-forward, and it is unclear how to obtain functional modules in a recurrent SNN or what they buy. In this work, we introduce a class of spiking networks, called Community Recurrent SNNs (CoRe SNNs): recurrent networks partitioned into communities with fixed roles. A controller community receives the stimulus, e...

---

### 40. Personalized Affective Perception via Continual Learning in Human-Agent Negotiation

**Authors:** Mehmet Onur Keskin, Berk Buzcu, Nikhil Churamani, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14247v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14247v1)

**Summary:** Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial Expression Recognition (CLIFER) to personalize valence-arousal perception in real time. Differential feedback converts changes in val...

---

### 41. SinkState: On-the-Fly SVD of Recurrent States for Efficient Hybrid LLM Serving

**Authors:** Haolin Jiang, Weihang Li, Zhongzhu Zhou, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14246v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14246v1)

**Summary:** Hybrid models combine softmax attention with linear attention, which compresses history into fixed-size recurrent states to balance model quality and inference efficiency. However, linear attention has not pushed this compression to its limit: we find that the queries, keys, and values of linear layers concentrate in a stable, low-dimensional subspace, a phenomenon we call the linear attention sink, so each state is effectively low-rank, with a rank that varies across states. Yet existing servin...

---

### 42. On Federated Averaging with Partial Participation under a General Variance Condition

**Authors:** Ziming Wang, Kun Huang, Karl Henrik Johansson, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14239v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14239v1)

**Summary:** In this paper, we study the convergence of Federated Averaging (FedAvg) with partial participation under a general variance condition. In each communication round, the server samples $S$ of the $n$ clients uniformly at random without replacement. The stochastic gradients are assumed to satisfy the so-called ABC condition, which allows their variance to grow with the local objective gaps. For smooth nonconvex objectives, we establish a finite-time stationarity bound in terms of the heterogeneity ...

---

### 43. Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing

**Authors:** Naveen Babu Narayanan Nair, Sajay Kurup

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14211v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14211v1)

**Summary:** Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated Services Code Point (DSCP) value declaring agent traffic, a router-side classifier that demotes flows contradicting the declaration to a class served after best-effort traffic, and a rate-limited priority queue. VATC was...

---

### 44. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits

**Authors:** Hadi Salloum, Ammar Ali

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14210v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14210v1)

**Summary:** Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. Our method, Tree-Ising, casts this repair as a sparse discrete optimization problem over the model's own BF16 weights. Forward statistics define an objective that weakens a loop directio...

---

### 45. SpecValley: Aggregation as Spectral Valley in Dense Heterophilic Graphs

**Authors:** Christoph Jahn, Delvin Bacho, Urs Waldmann, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14176v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14176v1)

**Summary:** Node classification in heterophilic graphs remains an open problem: aggregating over neighbourhoods can damp precisely the part of the signal that carries the labels. The field has answered with ever more expressive propagation operators, leaving the aggregation step that precedes them fixed by degree normalisation. However, degree normalisation acts as a spectral valley in its own right, attenuating a fixed middle band whose position at lambda equal 1 is set by the normalisation rather than by ...

---

### 46. Nonadaptive One-Sided Testing of Binary Rank

**Authors:** Nader H. Bshouty

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14163v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14163v1)

**Summary:** The binary rank of a binary matrix is the minimum number of disjoint all-one rectangles that partition its one-entries. We study entry-query testing of binary rank at most $d$, with one-sided error and nonadaptive queries. We give a tester using $\tilde O(d^4/ε^2)$ queries, independent of the matrix dimensions and a general lower bound of $\tilde Ω(d^{3/2}/ε)$.

---

### 47. Unipolar Neuron Networks Trained by Recirculation for Reward-Based Continual Learning

**Authors:** Florin Leon

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14153v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14153v1)

**Summary:** Unipolar neurons are the predominant type of nerve cell in the octopus and in most other invertebrates. A single neurite (a fiber extending from the cell body) branches into a tree that carries both input and output synapses. The branches send graded local outputs to nearby cells, and one site on the main neurite sends a global output to distant targets. This paper proposes a network of such neurons and a learning rule for it. Each neuron is modeled as a tree of passive segments, whose activatio...

---

### 48. Deviation-Aware Pretraining for Cardiovascular Disease Detection from Electrocardiograms

**Authors:** Siyuan Yan, Haibo Zheng, Feng Lu, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14141v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14141v1)

**Summary:** Electrocardiogram (ECG) signals are critical for cardiovascular disease (CVD) detection. Most current deep learning models rely on supervised, task-specific training, which limits their ability to generalize across diseases, patient populations, and acquisition settings. This paper presents a self-supervised ECG feature extraction framework that learns from nearly one million unlabeled 12-lead ECG recordings. The framework includes two modules: Deviation Localization Embedding (DLE), which detec...

---

### 49. HaiRuo: Forecasting Ocean Eddies as Fields and Objects with a Satellite-Altimetry Foundation Model

**Authors:** Xukun Qin, Haochen Sun, Yuyang Tian, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14136v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14136v1)

**Summary:** Mesoscale eddies carry most of the ocean's kinetic energy and move heat, salt and nutrients across basins, yet where an eddy will be two weeks ahead is still read off ocean models with post-hoc tracking heuristics. We introduce HaiRuo, which forecasts eddies as fields and as objects at once: from 30 days of satellite sea-level maps, one forward pass returns 15 days of sea level and geostrophic velocity, daily eddy masks and the trajectory of every eddy alive today. HaiRuo pairs two components wi...

---

### 50. Right for the Wrong Reasons? Evaluating Plausibility and Behavioral Change in Explanation-Guided Learning

**Authors:** David Dembinsky, Adriano Lucieri, Andreas Dengel

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14134v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14134v1)

**Summary:** Explanation-Guided Learning (EGL) promises models that are not only accurate but also rely on task-relevant evidence. However, whether improved agreement between model explanations and human-provided rationales also implies a changed decision strategy remains unclear. We study this tension under controlled synthetic shortcut introduction using a constructed shortcut dataset. Inspired by real-world applications, our benchmark covers shortcuts of different kinds, including localized, background-ba...

---

## cs.NE

**50 papers**

### 1. Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning

**Authors:** Vikram Ramavarapu, Himanshu Udupi, Ashish Gautam

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14262v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14262v1)

**Summary:** Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for reinforcement learning are usually feed-forward, and it is unclear how to obtain functional modules in a recurrent SNN or what they buy. In this work, we introduce a class of spiking networks, called Community Recurrent SNNs (CoRe SNNs): recurrent networks partitioned into communities with fixed roles. A controller community receives the stimulus, e...

---

### 2. Tailoring Optimization Approaches with Domain Knowledge in Industry Process for Meta-heuristic Development

**Authors:** Jakub Cebula, Konrad Gmyrek, Paweł B. Myszkowski, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13940v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13940v1)

**Summary:** The paper presents an Industry Process for Meta-heuristic Development (IPMD) schema, a systematic methodology for applying meta- and hyper-heuristic applications to optimization problems. In this context, we present a case study of Balancing Non-dominated Tournament Genetic Programming (BNTGP) applied to solve two NP-hard multi-objective optimization problems: routing (Capacitated Vehicle Routing Problem with Time Windows) and scheduling (Multi-Skill Resource Constrained Project Scheduling Probl...

---

### 3. Oscillatory Processing Units as a computing substrate for biomimetic intelligence

**Authors:** Alexander A. Wolf

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13840v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13840v1)

**Summary:** Biological intelligence emerges from neural activity that connects sensation, memory and action. Synaptic plasticity, neuronal assemblies and oscillations provide principles for biomimetic computing, but translating them into reusable operations requires a defined computational unit. We introduce Oscillatory Processing Units (OPUs), groups of synthetic neurons sharing a rhythm. Their directed interactions transform incoming activity and prior receiving state into an Oscillatory Occupancy Space (...

---

### 4. A Functional Preservation Score for Auditing Connectome Operations: Compression, Alignment, Transport, and Local-Rule Writing

**Authors:** Praveg Vashishtha

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13681v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13681v1)

**Summary:** We introduce the Functional Preservation Score (FPS), a null-normalised, behaviourally grounded measure of how much of a neural network's input-output function survives a structural operation, and use it to audit the operations underlying speculative "mind-migration" pipelines on public data that runs on a single laptop. Across five pre-registered studies on the C. elegans connectome, whole-brain calcium activity, and hippocampal replay, FPS yields two positive characterisations and a three-part...

---

### 5. Reconstructing Boundary Layer Wind Profiles with Machine Learning: A Comparative Study on IGRA Radiosonde Data

**Authors:** Fedor Buzaev, Dmitry Efremenko, Daria Pugacheva, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13359v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13359v1)

**Summary:** Wind profiles in the atmospheric boundary layer (ABL) drive short-range forecasting and wind-energy siting, yet sparse radiosonde coverage forces practitioners to interpolate them from a handful of physical predictors. We benchmark modern tabular learners against analytical parameterizations on 158,097 IGRA soundings. CatBoost, TabM, and FT-Transformer reduce RMSE to 1.3-1.6 m/s, against approximately 3 m/s for power-law and Monin-Obukhov fits; once the predictor set is fixed the three architect...

---

### 6. Making Strides in Symbolic Imitation Learning: Offline Demonstrations, Online Tuning

**Authors:** Bryce MacInnis, Malcolm I. Heywood

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13182v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13182v1)

**Summary:** Deep reinforcement learning (DRL) methods have been the dominant paradigm in continuous control tasks due to their efficacy in function approximation, while interpretable evolutionary methods have lagged largely behind for the opposite reason. In this work, we introduce Symbolic Imitation Learning, a framework for distilling an oracle policy through an offline dataset into a decision list with linear model motion primitives. We show that this, in conjunction, with online Augmented-Random Search ...

---

### 7. Pricing Symbolic Rules by What GNNs Leave Unlearned

**Authors:** Satabarto Sarkar, Prithwineel Paul

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12446v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12446v1)

**Summary:** Symbolic knowledge (motif counts, ring counts, label constraints) is routinely added to graph neural networks (GNNs) and justified by their limited expressivity. We replace this yardstick with an exact one. The largest log-loss reduction a rule $S$ can give a model family is $I(Y;S\midσ)$ given what the family computes; every realised gain splits exactly into this term plus repaid neural debt; and for a trained network with representation $T$ the value is $I(Y;S\mid T)$, the label information tr...

---

### 8. Maximizing Detection Probability in UAV Search Missions using Random-Key Optimizers

**Authors:** Antonio Dantas, Elcio Shiguemori, Antonio Chaves

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12317v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12317v1)

**Summary:** This paper focuses on the stochastic and real-time constraints of Unmanned Aerial Vehicle (UAV) path planning in Search and Rescue (SAR) missions. We introduce a configurable data-driven and intelligent routing architecture that combines a closed-loop probability update with the Random-Key Optimizers (RKO). Our problem is mathematically modeled as a dynamic probabilistic variant of the Open Vehicle Routing Problem (OVRP), enabling the solver to switch adaptively between two objectives, thereby b...

---

### 9. A method to automatically discover symbolic local learning rules

**Authors:** Andrea Perin, Fabio Anselmi, Stephane Deny

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12248v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12248v1)

**Summary:** We present a general method for discovering symbolic local learning rules that can replace backpropagation, applicable, in principle, to any deep learning architecture and task. The method automatically discovers local loss functions specific to each layer by (1) constructing a dictionary of monomials of local tensor variables, inspired by Penrose diagram notation, (2) regressing over coefficients weighting these monomials to build layerwise polynomial losses whose gradients together minimize a ...

---

### 10. AscendMOEA: An Ascend NPU-Accelerated Platform for Tensorized Multi-Objective Evolutionary Algorithms

**Authors:** Qianlong Dang, Zhiyang Zhang, Baosheng Li, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12057v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12057v1)

**Summary:** Multi-objective evolutionary optimization increasingly involves large populations, expensive problem evaluations, and diverse algorithmic structures. These workloads expose the limited parallelism of loop-based implementations, while rewrites for accelerator execution can alter selection order, tie handling, and population updates. AscendMOEA is presented as a scalable platform that executes multi-objective evolutionary algorithms (MOEAs) on Huawei Ascend neural processing units (NPUs) and conve...

---

### 11. Attention Is Only as Good as Its Witnesses: When Higher-Order Layers Help, and When They Do Not

**Authors:** Mostafa 'Neo' Mohsenvand

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11937v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11937v1)

**Summary:** Transformers stop learning graph search as graphs grow, and learn the card game SET only after many distinct questions, although attention can represent both. We read these failures, and the uneven record of higher-order attention, from what a layer sums over: each layer we study computes the partition function of a family of witnesses and reads it at a temperature. Two laws follow. The depth law is a known result of logic, which we state for these layers: L layers over two-step walks reach exac...

---

### 12. Understanding Spike Encoding across IoT Sensing Modalities: An Empirical Study

**Authors:** Yuxuan Hou, Di Yu, Linshan Jiang, et al.

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11317v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11317v1)

**Summary:** Spiking neural networks (SNNs) offer a path to energy-efficient sensing on Internet of Things (IoT) devices. The input encoder shapes that opportunity by changing the cues available for recognition and the work required to process them. We study these choices across wireless, inertial, surface electromyographic, and tactile sensing. For wireless activity recognition, interleaving reduces estimated energy for arithmetic in the network layers, latency from the prepared input window to returned sco...

---

### 13. Neural Activity Synchronization-Based Fast Local Learnable Spiking Neural Network Architecture

**Authors:** Pranith Dutta, Sk Wasim Rajjak, Siddhanta Ray, et al.

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11053v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11053v1)

**Summary:** Implementing intelligent learning systems on low- power edge devices is challenging due to the high compu- tational complexity, training latency, and energy demands of traditional Artificial Neural Networks (ANNs). Spiking Neural Networks (SNNs), biologically plausible and spike-driven, come as an alternative. However, SNN training commonly relies on backpropagation through time (BPTT), which is computationally expensive, inherently global, and unsuitable for battery-driven devices. This work pr...

---

### 14. The forces at hand: social learning is permissive, not instructive, for the evolution of phenotypic plasticity

**Authors:** Nam H. Le

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10986v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10986v1)

**Summary:** Evolution can favour a trait for two reasons: an instructive cause makes selection favour the trait; a permissive one lets it persist once selection no longer removes it. The distinction matters most for phenotypic plasticity and its replacement by inherited behaviour, genetic assimilation, the Baldwin effect. Social learning is credited with favouring plasticity on evidence that cannot tell the two apart: how much plasticity remains at the end of a simulation. Here we show, analytically and com...

---

### 15. Bridging Spiking and Continuous Dynamics in Spiking Neural Networks: A Muscle-Inspired Model

**Authors:** Maryam Soltani, Philip N. Garner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09295v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09295v1)

**Summary:** Transforming the spike trains produced by spiking neural networks (SNNs) into continuous signals through biologically inspired mechanisms remains an open challenge in generative and regression tasks. In biological systems, a similar transformation occurs when muscles integrate neural spikes to produce smooth, coordinated movements. Inspired by this mechanism, we introduce a muscle-response model, a biologically motivated dynamical layer that converts spike trains into continuous representations....

---

### 16. OMCDE: Opposition-based Multi-Stage Matrix-Based Competitive Differential Evolution

**Authors:** Mohammad Sarhangzadeh, Shahryar Rahnamayan, Doruk Oner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09167v1)

**Summary:** Differential Evolution has proven to be an effective algorithm for continuous global optimization, but it's modern high-performing variants often introduce additional complexity and computational cost. We propose OMCDE, a matrix-based competitive Differential Evolution algorithm that aims to improve optimization performance while maintaining computational efficiency. The proposed approach integrates competition-driven search dynamics, adaptive behavior between optimization stages, and opposition...

---

### 17. Circuit Theory-Informed AI for Condition Monitoring in Power Electronics

**Authors:** Yubo Song, Pascal A. Schirmer, Subham Sahoo

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09141v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09141v1)

**Summary:** Artificial intelligence for power electronics is evolving toward a deeper comprehension of system intrinsic behaviors and dynamics. As a novel integration of neural computation and electric circuits, spike-based neuromorphic computing offers promising potential in high energy efficiency and adaptability for data-driven applications. Building on the latency-coding principles, this article proposes a framework for data-light condition monitoring that relies solely on three-phase AC current measure...

---

### 18. Two-Layer Evolutionary Scheduling for Machine Learning Jobs in Multi-Cluster Environments

**Authors:** Jingyuan Xu, Changwu Huang, Lemeng Pan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09093v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09093v1)

**Summary:** The rapid growth of large-scale machine learning (ML) workloads has led to unprecedented demands on GPU cluster scheduling systems. However, existing heuristic schedulers struggle to handle the complexity and dynamics of multi-cluster GPU environments, often leading to load imbalance, long queuing delays, and poor alignment to business objectives. This paper formulates the ML scheduling problem in multi-cluster GPU environments as online multi-objective optimization that minimizes the average an...

---

### 19. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

**Authors:** Qile Jiang, George Em Karniadakis

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08483v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08483v1)

**Summary:** LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decod...

---

### 20. Invariance before structure: two modes of emergent compression in representation learning

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07952v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07952v1)

**Summary:** Learned representations show striking invariance across biological and artificial neural networks, with different substrates and variations driven by drift, heterogeneity and initialisation. To understand this invariance, we propose Emergent Adaptive Representation Learning (EARL), a framework that distinguishes two modes of emergence in learned representations: state-space compression, where a learned representation gains predictive power over its own future beyond what the network's units can ...

---

### 21. Projection-Free Gradient Tracking Neurodynamic for Distributed Nonnegative Sparse Optimization

**Authors:** Juntao Li, Qihang Guo, Deyuan Meng

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07643v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07643v1)

**Summary:** This paper proposes a continuous-time, projection-free neurodynamic system based on gradient tracking for distributed nonnegative sparse optimization. Unlike traditional methods, our approach avoids projecting states onto the feasible set. Instead, it employs gradient tracking to estimate average gradients under heterogeneous costs, coupling primal and dual dynamics such that feasibility and sparsity emerge naturally from the equilibrium conditions. The system ensures unique solutions through a ...

---

### 22. When Does Blockwise Additivity Break? Diagnosing and Repairing the Additive Assumption in Distillation-Based Architecture Search

**Authors:** Yuefeng Xu, Jun Yu

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07487v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07487v1)

**Summary:** Blockwise distillation methods for architecture search, such as DNA, DONNA, LANA and Puzzle, score each candidate replacement block in isolation and assemble a child network by minimizing the sum of per-block scores. We test this additive assumption on DeiT-S and DeiT-B with seven replacement blocks per layer, seven block-latency budgets from 70% to 40%, three fine-tuning seeds and paired bootstrap confidence intervals. (i) At mild compression the additive integer linear program (ILP) is close t...

---

### 23. Learning Time-Varying Connectomes for Stable Behavior Across Development

**Authors:** Christof Fehrman, Jacob J. Morra, Eva A. Naumann

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06895v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06895v1)

**Summary:** Neural circuits must maintain functionality to drive effective behavior while their size, topology, geometry, and intrinsic dynamics change across development. To model developing visuomotor circuits and behavior, we investigated whether a single compact generative encoding could produce functional recurrent controllers across such changes. Building on the HyperNEAT algorithm, we represented this program as a compositional pattern-producing network that received developmental time as an input to...

---

### 24. Adaptive Multi Mode: Budget-Aware Routing of Optimizers By Online Landscape Probes

**Authors:** Benjamin Jacob Bodner

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06879v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06879v1)

**Summary:** The best classical optimizer for a continuous black-box problem depends on its budget and landscape. Existing routers decide from the dimension and budget, past improvement or features fitted to one benchmark, and few test an optimizer's implicit assumptions online. AMM (Adaptive Multi Mode) routes a known budget among quasi-Newton, trust-region, coordinate, multistart and evolution-strategy optimization engines with online probes of curvature, plateaus, separability, kinks, basins and fractal s...

---

### 25. SpikePose: Lightweight Video Human Pose Estimation

**Authors:** Yunhao Huang, Kaushik Bhargav Sivangi, Tianyi Yu, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06594v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06594v1)

**Summary:** Efficient video human pose estimation must balance localisation accuracy, motion quality, and energy cost. We present SpikePose, a lightweight video pose estimator that pairs a frame-reset, single-step spiking encoder with motion-aligned heatmap memory (MAM). The encoder supplies per-frame spatial evidence, while MAM estimates joint displacement, aligns historical heatmaps, and adaptively fuses them with current predictions. By confining temporal reasoning to a compact, lightweight module outsid...

---

### 26. From Admission to Retention: Predicting Durable Offspring in Quality-Diversity Search

**Authors:** Corrado Calamita, Matteo Mendicini, Luca Ferrari, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06522v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06522v1)

**Summary:** Automated failure discovery can be framed as a diversity problem: the objective is to expose distinct ways a system fails rather than a single critical adversarial case. Yet uniform parent sampling provides no way to allocate search effort toward individuals likely to produce durable archive contributions. We study this credit assignment problem in an unstructured Quality-Diversity (QD) archive, testing whether signals available before an individual has reproduced distinguish offspring that mere...

---

### 27. Multi-Resident Data Association in Smart Homes via MDP Modeling and Behavior Cloning

**Authors:** Xi Chen, Julien Cumin, Fano Ramparany, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06296v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06296v1)

**Summary:** Ambient sensors offer a privacy-preserving solution for activity recognition in smart homes, yet they face a critical challenge in multi-resident environments known as Data Association, which aims to identify the resident triggering a specific anonymous sensor event. Existing approaches fundamentally fail to maintain global consistency by often yielding conflicting associations for silent residents. Additionally, these methods frequently suffer from severe trajectory fragmentation caused by the ...

---

### 28. Explainable Anomaly Detection in 5G Networks through Continuous Time Graphs

**Authors:** Thomas Hoger, Philippe Owezarski

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06225v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06225v1)

**Summary:** 5G networks increasingly resemble distributed systems in their design. It then becomes crucial to move beyond traditional network-based detection methods and to explore alternative approaches. In this work, we propose a formalization of 5G network exchanges as a dynamic graph, on which we apply techniques from the field of graph-based learning to detect anomalies effectively. This representation allows for fine-grained analysis of packet-level semantic content, while simultaneously capturing seq...

---

### 29. Mobility-Aware Mobile Edge Computing for Energy-Balanced Data Collection in IoT-Enabled Underwater Sensor Networks

**Authors:** Nguyen Thi My Binh, Do Dinh Hoan, Tong Tien Manh, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06186v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06186v1)

**Summary:** Underwater wireless sensor networks (UWSNs) face critical challenges in energy imbalance, connectivity, and data collection due to harsh environments. To address these issues, this paper focuses on the problem is how to achieve energy-balanced data collection in IoT-enabled UWSNs with a mobility-aware mobile edge computing (MEC), named MECEBDC. Unlike existing approaches, the proposed scheme jointly optimizes energy-aware clustering, cluster head selection, and AUV-assisted data collection. Furt...

---

### 30. Neural networks and games

**Authors:** Philip R. Neary

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05706v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05706v1)

**Summary:** Hopfield neural networks and noncooperative games provide seemingly different approaches to understanding how collective outcomes emerge from local interactions. In a neural network, individual units adjust their states according to local signals; in a game, players choose actions to maximise individual payoffs. I establish an exact equivalence between symmetric binary Hopfield networks and binary-action games that admit a quadratic potential. The equivalence identifies stable network configurat...

---

### 31. Learning Behaviorally Relevant Dynamics in Multimodal Neural Recordings

**Authors:** Parastoo Azizeddin, Eray Erturk, Maryam M. Shanechi

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05167v1)

**Summary:** Multimodal neural data can enable a more complete understanding of brain dynamics underlying behavior. Modalities such as spiking activity, local field potentials (LFPs), and behavior capture diverse spatiotemporal aspects of brain processes, yet prior neural-behavioral models that separate sources of variability rely on a single neural modality. By leveraging these complementary strengths, multimodal neural fusion can provide a unified, rich representation of brain-behavior processes and addres...

---

### 32. Solving the Nonlinear Westervelt Equation in Ultrasound Propagation Using Physics-Informed Neural Networks

**Authors:** Luke Oluwaseye Joel

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05130v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05130v1)

**Summary:** Modeling the nonlinear acoustic wave propagation in biological tissues needs accuracy, especially in ultrasound imaging and therapeutic applications. The 1D Westervelt equation, \( p_{xx} - p_{tt} + γ\, p_{ttt} + η\,(p^{2})_{tt}=0, \) could be used to describe a finite-amplitude ultrasound propagation in these tissues. This equation accounts for nonlinearity, \(η\), and attenuation, \(γ\). To solve this equation, we observe that traditional solvers may struggle to do so correctly. This is due to...

---

### 33. Refined CMA-ES for CEC 2026 Bound-Constrained Single-Objective Optimization

**Authors:** Adam Stelmaszczyk, Rafał Biedrzycki, Jarosław Arabas

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.04620v1) | 📄 [PDF](https://arxiv.org/pdf/2611.04620v1)

**Summary:** We present a simplified and parameter-adjusted variant of CMA-ES designed for the CEC 2026 Bound-Constrained Single-Objective Optimization competition. Unlike typical algorithmic developments that increase complexity by adding mechanisms, Refined CMA-ES systematically removes components that do not improve performance, such as the flat-land escape, while retaining standard features that provide measurable benefits. Adjusting key parameters (population size and initial step-size) yields substanti...

---

### 34. An ensemble of graph generative models for assisted history matching of the Brugge field case

**Authors:** Gleb Shishaev, Anton Shirokov, Shadfar Davoodi, et al.

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.12927v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12927v1)

**Summary:** Assisted history matching remains non-unique because many geological realisations can reproduce equivalent production responses with substantial differences between individual well matches. This ambiguity increases when a field comprises several depositional settings and modelling strategies. The paper applied a graph autoencoder approach to history matching of a benchmark Brugge field that comprises different depositional zones. Each stratigraphic zone is modelled with its dedicated generative ...

---

### 35. Structured Visual Landscape: Generating Preferred Representations in Biological and Artificial Neural Networks

**Authors:** Yusong Zhao, Edgar Y. Walker, Hao Wang, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03597v2) | 📄 [PDF](https://arxiv.org/pdf/2611.03597v2)

**Summary:** Understanding how neurons respond to visual stimulus is an important question in both deep learning and neuroscience. It has significant implications for enhancing the interpretability of black-box artificial neural networks and for understanding the visual representation in the human brain. We propose a structured visual representations landscape and design an activation-based prior that allows us to effectively regularize the landscape with activations from brain regions or neural network unit...

---

### 36. Exact Fusion of Softmax Attention Heads Can Require Exponentially Many Atoms

**Authors:** Hiroyasu Usami, Keisuke Hara, Ayato Tsuboi, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02943v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02943v1)

**Summary:** Fusing independently normalized attention heads can increase the number of explicit key-value entries, or atoms, needed to preserve their output. We prove a sharp separation for $W_d(q)=\sum_{j=1}^dσ(q_j)$: its $d$ two-atom heads use $2d$ head-atom terms, whereas its minimum single-head representation has exactly $2^d$ atoms, even with arbitrary fixed replacement keys, scalar values, and positive masses. The same lower bound holds for every fixed uniform error below $1/2$ on $\mathbb R^d$, and t...

---

### 37. Iterated Narrow Networks: Turing Completeness at Width 4 on Convex Input Spaces and the Complexity of Verification

**Authors:** Olivier Bournez, Johanne Cohen, Adrian Wurm

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02840v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02840v1)

**Summary:** We study the iterates of a fixed ReLU network $N$ of width 4, that is, the discrete-time system $x_{k+1} = N(x_k)$ on $[0,1]^4$. Equivalently, $x_k$ is the output of a weight-tied network made of $k$ copies of $N$, or of a recurrent network with no external input, started at $x_0$. We prove that every deterministic Turing machine $M$ admits such a network $N_M$. The network can be constructed in polynomial time from $M$. Each iteration has depth $\mathrm{poly}(|M|)$. The iterates of $N_M$ simula...

---

### 38. HyVox: Rethinking Low-Power Voice Intelligence towards Neuromorphic-von Neumann Edge Computing

**Authors:** Snehasis Addy, Eduardo Calle Ortiz, Prashant Shenoy, et al.

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.03735v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03735v1)

**Summary:** We present HyVox, a hybrid neuromorphic--von Neumann system for low-energy open-set speaker identification under tight energy budgets. HyVox splits the workload at the speaker embedding. A neuromorphic processor embeds the speech with sparse, event-driven computation, and a von Neumann microcontroller holds the speaker gallery and makes every decision: it scores queries by cosine similarity, rejects unknown speakers, and enrolls new users by writing a prototype, with no weight update. On the neu...

---

### 39. Exposure-Length Trade-off Optimization for Obstacle-Aware Intrusion Paths in Heterogeneous Wireless Sensor Networks

**Authors:** Nguyen Thi My Binh, Ho Viet Duc Luong, Nguyen Tuan Nghia, et al.

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.01606v1) | 📄 [PDF](https://arxiv.org/pdf/2611.01606v1)

**Summary:** Barrier coverage is a key paradigm for intrusion detection and surveillance in IoT-enabled heterogeneous wireless sensor networks, where monitoring quality depends not only on the existence of sensing barriers but also on the detectability of feasible crossing paths. In this paper, we study the obstacle-aware maximal exposure path planning problem in heterogeneous sensor fields under truncated omni-directional sensing and line-of-sight occlusion. Unlike conventional maximal exposure formulations...

---

### 40. Is Newborn Wiring Special? Separating Wiring from Weight Placement in Connectome Reservoirs

**Authors:** Riccardo Bertamini, Corrado Calamita, Ramiro Pascual, et al.

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.01213v1) | 📄 [PDF](https://arxiv.org/pdf/2611.01213v1)

**Summary:** Reservoir computing offers a way to study the brain's wiring before it is even trained. The recurrent network remains fixed, while only a linear readout is trained. The human connectome is found to perform better than randomly rewired versions of itself, suggesting that biological wiring is special. To understand the source of this advantage, a mathematical graph-theoretic decomposition is introduced. Rewiring a weighted network changes both the regions that are connected and the weights assigne...

---

### 41. A Tool in the Forward Pass: Frozen Tape Modules as Layers of a Small Language Model

**Authors:** Michael Granitzer, Saber Zerhoudi, Mohammad Al-Maamari, et al.

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.00783v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00783v1)

**Summary:** Calling a tool through generated text adds decoding steps, even when the computation itself is short. We study an alternative: a small neural module that runs inside a language model's forward pass. A learned writer turns hidden states into a symbolic tape, a short sequence of discrete symbols that encodes the computation. The module, trained separately and then frozen, reduces the tape to a result, and a learned reader returns that result to the model. We evaluate arithmetic and object tracking...

---

### 42. Boosted Physics-Informed Neural Networks for Solving Homogeneous and Non-Homogeneous Lane-Emden Type Equations

**Authors:** Luke Oluwaseye Joel

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.00701v1) | 📄 [PDF](https://arxiv.org/pdf/2611.00701v1)

**Summary:** The Lane-Emden Equation is a class of nonlinear differential equations commonly used to model phenomena in astrophysics and mathematical physics, such as stellar structure and thermal behavior in polytropic gas spheres. This study presents a novel hybrid framework that integrates Physics-Informed Neural Networks (PINNs) with boosting methods to enhance the accuracy and robustness of solutions for Lane-Emden type differential equations. Standard PINNs leverage physical laws encoded within the los...

---

### 43. From Connection Loss to Collision: Closed-Loop Fault Assessment of a Fly-Connectome SNN

**Authors:** Shuchao Gao

**Published:** 2026-10-31

🔗 [Paper](http://arxiv.org/abs/2611.06940v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06940v1)

**Summary:** The public release of the complete adult fruit-fly brain connectome enables brain-scale spiking-network studies, motivating closed-loop assessment of connection loss. We test a connectome-derived controller in synthetic pursuit-escape and check record consistency. Across 576 test episodes in paired campaigns, the baseline mapping at 50% connection-row deletion yields 11/48 proportional and 0/48 relay collisions by 1 s, despite paired P/R trigger/burst schedules. The prespecified secondary relay-...

---

### 44. Proof-Carrying Evolution: Black-Box Search, White-Box Flight

**Authors:** Amit Jain, Sergio Sanchez-Hurtado, Victor Rodriguez-Fernandez, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.42043v1) | 📄 [PDF](https://arxiv.org/pdf/2610.42043v1)

**Summary:** We study whether a language model can help design controllers whose behavior can be formally checked. In proof-carrying evolution (PCE), a search proposes controllers together with their certificates. Their mathematical forms are fixed; a proposer chooses their numerical parameters together. Certificate checks guide selection, and only a certified candidate can be returned. The deployed artifact is a control law and its certificate; the language model is used only during design. We compare four ...

---

### 45. In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents

**Authors:** Xuning He, Kai Fan, Runyu Zhang, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41291v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41291v1)

**Summary:** Long-horizon LLM agents play an important role in solving complex and sustained tasks, with ever-growing interaction contexts. However, these accumulated contexts will raise substantial computational cost and obscure key decision-relevant evidence. Existing methods typically train external compressors or context-management agents to rewrite context as shorter hard-token sequences, but such external selection may not align with the LLM's evolving representation and is necessarily lossy. In this p...

---

### 46. Input-dependent Neuromodulation Enhances Mixed-Signal Neuromorphic Hardware

**Authors:** Aashman Mehta, AbdelQader AlKilany, Dan F. M. Goodman, et al.

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41265v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41265v1)

**Summary:** Gating mechanisms allow a fixed neural network to adapt its computation to the current input by dynamically modulating its effective parameters. In the brain, neuromodulation uses this principle to move neural circuits between dynamical regimes, and deep learning exploits input-dependent gating, e.g., in gated recurrent networks and self-attention. Input-dependent modulation has also recently been shown to improve spiking neural networks, with particularly strong benefits in small, parameter-lim...

---

### 47. Memory and Recall of Color Images Using Neural Networks-1 - The Cue-Ball Model based on the Associative Memory Mechanism -

**Authors:** Hiroshi Inazawa

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41108v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41108v1)

**Summary:** This paper presents a neural network model for storing and recalling color images of different sizes using the Cue BallRecall Net systems [1,2,3,4,5]. The Cue Ball system consists of a Recall Net composed of multiple memory neurons each responsible for memorizing a single, distinct memory and a large number of neurons that represent image patterns. The images used in this study [6] consist of ten images(see Appendix). The pixel values of these images were converted into digital values and used f...

---

### 48. Local Budget Benefits, Population Commitment, and Solver Performance: A DGO Case Study with Controlled DE Transfer

**Authors:** Shiqi Li

**Published:** 2026-10-30

🔗 [Paper](http://arxiv.org/abs/2610.41099v1) | 📄 [PDF](https://arxiv.org/pdf/2610.41099v1)

**Summary:** An evaluated candidate can improve a local search step, alter the population used by later steps, and affect a solver's final result. We distinguish these three questions using Da Gou Gun Optimization (DGO), a population optimizer designed for this study. Its JQ100 configuration evaluates an interpolation candidate during a two-sided probe. We define local budget value, population commitment effects and complete-policy performance, and give an exact example in which a locally better commitment l...

---

### 49. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

**Authors:** Jiongfan Yang, Weichen Fan, Haiwen Diao, et al.

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40647v1)

**Summary:** Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introduce SpecSlot, a pixel-space rectified-flow Transformer that decouples output detail from the length o...

---

### 50. Dynamic Powergrid Optimization with FPGA-based Neuromorphic Higher-order Ising Machines

**Authors:** Saptarshi Maiti, Shantanu Chakrabartty, Chetan Singh Thakur

**Published:** 2026-10-29

🔗 [Paper](http://arxiv.org/abs/2610.40522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.40522v1)

**Summary:** The advent of large, high-density FPGAs such as the AMD Versal enables efficient hardware implementation of neuromorphic Ising machines, unlocking unprecedented performance for complex combinatorial optimizations. A critical application for this computing paradigm is dynamic powergrid optimization, specifically Distribution Network Reconfiguration (DNR), which seeks to mitigate severe resistive losses and reduce electricity costs by optimizing network switch configurations in real time. This pap...

---

## q-bio.NC

**50 papers**

### 1. When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology

**Authors:** Yeyuan Liu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14508v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14508v1)

**Summary:** Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, gains or plasticity rates the model also needs, and modellers often tune these until the real-wiring model works. We separate three estimands: physiology tuned on the real wiring and transferred to null...

---

### 2. Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model: Linking an Adversarial and a Perceptual Illusion

**Authors:** Alexandre Garcia-Duran, Alejandro Rodriguez-Garcia, Manuel Molano-Mazón, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14498v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14498v1)

**Summary:** Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Whether networks with brain-like wiring are more robust at lower computational cost is unclear. We address this by benchmarking a task-optimized, continuous-time recurrent neural network of the fly visual system constrained by its synaptic connectome (FlyNet) against artificial neural networks. We com...

---

### 3. Optimization principles, revisited

**Authors:** William Bialek

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14381v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14381v1)

**Summary:** The brain solves a wide range of problems, and some of these solutions are very good indeed. It is an old idea that, in some cases, these solutions may be as good as possible given the relevant constraints. If this is true we can promote this notion of optimization to a principle from which aspects of function and mechanism can be derived, ideally with no free parameters. Optimization principles are powerful and have had many successes, but they remain controversial. We start with a reminder of ...

---

### 4. ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models

**Authors:** Minyu Zhou, Yajing Wu, Yongqiang Tang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14035v1)

**Summary:** Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations. However, these operations leave the correspondence between learned features and scale-...

---

### 5. Neuromodulation Through Intrinsic Noise

**Authors:** Sunghyun Koo, Jin Gyu Lee, Rodolphe Sepulchre

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13780v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13780v1)

**Summary:** Neuromodulation, the modulation of excitability through the regulation of neuronal parameters, is a key tool in neuromorphic control design. This paper investigates how spiking excitability can be modulated by intrinsic noise. Focusing on a simplified memristive neuron model, we show that intrinsic noise plays distinct functional roles depending on the feedback pathways: Intrinsic noise in the fast excitatory feedback shapes the nature of excitability and modulates the sensitivity of the neuron ...

---

### 6. Similar visual tuning conceals different recovery dynamics in a model of macaque V1

**Authors:** Xialei Huang, Qingyu Yan, Zheng Bian, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13692v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13692v1)

**Summary:** Biologically detailed neuronal networks can model how brain circuits perform observed functions, but their high computational cost limits the comparisons needed to test biological hypotheses. To address this limitation, we extend a multiscale approach in which responses of small populations of spiking neurons are computed in advance and reused across a larger cortical circuit. In particular, we approximate these local responses by deep neural networks and achieve an estimated acceleration of the...

---

### 7. A Functional Preservation Score for Auditing Connectome Operations: Compression, Alignment, Transport, and Local-Rule Writing

**Authors:** Praveg Vashishtha

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13681v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13681v1)

**Summary:** We introduce the Functional Preservation Score (FPS), a null-normalised, behaviourally grounded measure of how much of a neural network's input-output function survives a structural operation, and use it to audit the operations underlying speculative "mind-migration" pipelines on public data that runs on a single laptop. Across five pre-registered studies on the C. elegans connectome, whole-brain calcium activity, and hippocampal replay, FPS yields two positive characterisations and a three-part...

---

### 8. Human and Machine Annotations Predict Brain Responses to Naturalistic Movies Across Development

**Authors:** Yiran Huang, Zeyong Zhang, Rounak Rahman, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13637v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13637v1)

**Summary:** Naturalistic movie watching provides a powerful framework for studying dynamic brain function, but linking movie content to neural responses typically relies on labor-intensive human annotation. We investigated whether multimodal large language models (MLLMs) can provide scalable socio-affective and semantic annotations for naturalistic fMRI. We compared MLLM-generated theory-of-mind (ToM) and valence ratings with human ratings and with regional BOLD responses across three animated movies. For t...

---

### 9. Lightweight Deep Learning Framework for Astrocyte-Centric 3D Reconstruction across Normal and Stress-associated Ultrastructural States

**Authors:** Bowen Deng, Gwang-Jin Jeong, Seulgi Noh, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13581v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13581v1)

**Summary:** The morphology of astrocytes is closely associated with their ability to support and modulate neural circuit functions; however, its reconstruction from volume electron microscopy (vEM) data remains labor-intensive and computationally resource-intensive, placing substantial barriers on its broader adoption and scalability despite the high spatial resolution of vEM. We present AstroSeg-vEM, a lightweight, astrocyte-centric framework for morphology-preserving astrocyte segmentation, 3D reconstruct...

---

### 10. Orthographic depth at two scales, with English also matched for lexicon size

**Authors:** Adam Y. Shavit

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13400v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13400v1)

**Summary:** A reader can struggle to read in only one of their languages, and one proposed reason is how predictably spelling maps to sound. We measure that predictability as conditional entropy, the pronunciation uncertainty left once the spelling is seen, at two grain sizes (unit sizes): the alignment unit, an aligned spelling-sound chunk, and the syllable, bounded in the pronunciation. We analyse word lists in twelve alphabetic orthographies and report five in full, with English pronunciations from a dic...

---

### 11. A probabilistic model of visual segmentation explains early visual cortical dynamics

**Authors:** Tridib K. Biswas, Ruben Coen-Cagli

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13316v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13316v1)

**Summary:** Neural dynamics are a central feature of biological neural systems. In the visual cortex, the functional role of neural dynamics is poorly understood, particularly for static stimuli. The statistics of still natural images have long been used by models that successfully predict firing in early visual cortex; those models assume that neurons represent inferences about latent image features, but often ignore the dynamics of said inference. Here, we test if inferential dynamics in images explain vi...

---

### 12. IC-GNN: Modeling Individualized Brain Community Organization for Disease Prediction

**Authors:** Yang Zhang, Xiao Zhou, Jonathan Warrell, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13070v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13070v1)

**Summary:** Brain networks exhibit modular organization, where community structures vary substantially across individuals and diseases. Understanding these individual differences is crucial for advancing both basic neuroscience research and precision medicine. However, widely used predefined group-level brain atlases often overlook this heterogeneity. While individualized functional parcellations capture subject-specific variability in community boundaries, they often require lengthy scan times to achieve f...

---

### 13. Qualiaphobic artificial neural networks (and why to build them)

**Authors:** Erik Hoel

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12809v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12809v1)

**Summary:** This paper introduces qualiaphobic AI: artificial neural network architectures that are hostile to theories of consciousness. I show that qualiaphobia can be well-justified by knowledge about theories of consciousness, like when such theories are trivial or unfalsifiable or contradicted by overwhelming scientific evidence. It can also be justified by how theories of consciousness must be grounded in phenomenology, as well as how current popular theories of consciousness are applied to AI. I iden...

---

### 14. Spike-to-Field Mechanisms of Turbulence-Like Dynamics in Spatial Spiking Neural Networks

**Authors:** Zequan Liu

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12627v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12627v1)

**Summary:** Neural avalanches and turbulence-like brain dynamics are usually measured after neural activity has been coarse-grained into continuous fields, leaving open which spike-level mechanisms can generate these macroscopic observables. We build a spatial leaky integrate-and-fire spiking neural network and explicitly transform spikes into activity-density and Hilbert phase fields. A delayed, distance-dependent, passive-dendrite regime reproducibly generates turbulence-like field structure, including hi...

---

### 15. K-prop: Deep Online Learning by Backpropagating Temporal Kernels

**Authors:** Bingkun Liu, Paul Haider, Federico Benitez, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12530v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12530v1)

**Summary:** Self-recurrence represents an important component for temporal processing in neural networks, both artificial and biological, where it appears naturally in the form of leaky integration. However, due to the complex temporal dependencies of the gradient, an efficient and effective method of online training is still lacking. Here we propose K-prop, a novel online learning method for leaky neural networks. It dramatically reduces the computational and memory cost of real time recurrent learning (RT...

---

### 16. TrajLift: Lifting Memory Recall Trajectories with Latency-Modulated Heat Diffusion

**Authors:** Jiawen Kang, Jinchao Li, Mingyu Cui, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12197v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12197v1)

**Summary:** Verbal memory retrieval carries rich diagnostic information for Alzheimer's disease through the order, hesitation, and categorical organization of recalled words, yet computational modeling of this retrieval process remains largely unexplored. A key challenge is that timing and hierarchical structure are diagnostically entangled: the diagnostic meaning of retrieval timing depends on its hierarchical context. We propose TrajLift, a spectral framework that models verbal recall as timed trajectorie...

---

### 17. Language processing in the autistic brain: A meta-analysis of neuroimaging studies across modalities and age

**Authors:** Hanlin Wu, Bei Xiao, Qingxi He

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11927v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11927v1)

**Summary:** Language is central to social communication, which is altered in autism, and language abilities vary widely among autistic individuals. How the autistic brain processes language is central to understanding autistic communication. Yet neuroimaging studies report inconsistent findings on how autistic brain activity is altered during language processing. We synthesized 45 fMRI and PET studies (753 autistic and 777 non-autistic participants) with seed-based d mapping with permutation of subject imag...

---

### 18. MICE: Multi-animal Interaction Context Encoder - A Hierarchical Foundation Model for Mouse Behavior

**Authors:** Yen-Shuo Su, Weihan Li, Anqi Wu

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11644v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11644v1)

**Summary:** Quantifying mouse behavior from pose is a foundational tool in neuroscience, ethology, drug discovery, and animal welfare. Self-supervised foundation models are a natural fit, but a foundation model for mouse behavior must handle social behavior - many behaviors that matter (aggression, courtship, mounting, allogrooming) are inherently multi-animal. Existing self-supervised pose models fall short: they encode each animal independently and discard interaction signal, hard-code the animal count, a...

---

### 19. From MNH to the Friedman--Komogortsev Method---which changes improve eye-movement classification?

**Authors:** Lee Friedman, Mehedi Hasan Raju, Oleg Komogortsev

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11519v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11519v1)

**Summary:** The Friedman-Komogortsev Method (FKM) is a rule-based classifier of fixations, saccades, and post-saccadic oscillations in 1000-Hz recordings, developed from the modified Nyström-Holmqvist algorithm (MNH) and used in several recent studies. FKM changes MNH in many ways at once: it centres MNH's Savitzky-Golay filter, adds a position-based test for whether an apparent post-saccadic oscillation continues the saccade, adds rejection tests, and changes several thresholds. We asked which of these cha...

---

### 20. Learning Actionable Information Landscapes for Multimodal Active Sensing in Hawkmoths

**Authors:** Abdelrahman Sharafeldin, Yaqing Wang, Simon Sponberg, et al.

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.11011v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11011v1)

**Summary:** Animals integrate information across sensory modalities to guide exploration, suggesting that they maintain internal estimates of where actions are expected to reduce uncertainty. However, how such action-conditioned information maps are learned from multimodal sensory experience remains unclear, as previous studies have been largely confined to unimodal sensing frameworks. We introduce a multimodal predictive-coding framework for learning uncertainty-reduction maps from visual and mechanosensor...

---

### 21. Perception, Not Reasoning, Limits Visual Theory of Mind

**Authors:** Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall, et al.

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10694v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10694v1)

**Summary:** Vision-language models pass text-based false-belief probes at near-human levels but drop by over twenty percentage points on abstract panels the moment the same problem is conveyed visually. The consensus diagnosis is conceptual, prescribing new belief-reasoning modules. We argue the dominant bottleneck is perceptual: not what the model cannot reason about, but what it cannot see. We propose a five-condition dissociation protocol that holds the reasoning task constant while varying perceptual fi...

---

### 22. NeuroHorizon: Long-Horizon Forecasting of Neural Population Activity with Hierarchical Memory

**Authors:** Peng Jiang, Xiaoxuan Jia

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10617v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10617v1)

**Summary:** Long-horizon forecasting of neural population activity tests whether a model has captured dynamics that remain predictive well beyond the observed history. Prediction quality typically declines as the horizon grows, yet neither short-horizon accuracy nor teacher-forced evaluation, which supplies the true activity preceding each predicted step, reveals how well models sustain predictions from an initial history alone. We compare direct multi-step prediction and autoregressive rollout on spiking r...

---

### 23. Pixels over Symbols: Sensory Realism Improves Behavioral Alignment in Models of Cognition

**Authors:** Hao Yuan Bai, Xiaoxuan Lei, Zihan Weng, et al.

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10565v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10565v1)

**Summary:** Computational models of cognition have traditionally relied on abstract symbolic inputs that approximate sensory experiences with simplified vector representations. This simplification reflects historical computational constraints and a long-held assumption that the details of sensory realism are incidental to the study of cognitive processes. Recent advances have enabled the development of sensory-realistic models capable of performing diverse cognitive tasks, yet whether sensory realism meanin...

---

### 24. Path-dependent triage: Early judgments lead conversational AI chatbots to miss mental-health emergencies

**Authors:** Veith Weilnhammer, Raymond Dolan, Lennart Luettgau, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09647v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09647v1)

**Summary:** People increasingly bring mental-health concerns to consumer AI chatbots. In these conversations, clinically relevant information rarely arrives all at once. Instead, it unfolds over multiple turns, often in response to the questions the chatbot asks. Recognizing risk therefore depends on how a chatbot integrates newly disclosed information (inference) and on the questions it asks on each turn to elicit this information (context-seeking). Here we evaluated the conversational triage performance o...

---

### 25. A hair-thin implant opens the entire depth of the mouse brain to revisiting the same structures at subcellular resolution

**Authors:** Miroslav Stibůrek, Tomáš Pikálek, Petra Ondráčková, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09481v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09481v1)

**Summary:** Ultrathin multimode-fibre endoscopes provide minimally invasive access to subcellular structures throughout the depth of the mouse brain. Here we introduce a chronically implantable interface with a diameter of 144 μm, about the thickness of a human hair, that extends this capability to longitudinal imaging, enabling repeated access to the same fine structures over extended periods. The system supports weeks-long tracking of individual dendritic spines, allowing quantitative comparison of their ...

---

### 26. Decoding spatial and semantic information from large-scale visual cortical activity for natural-movie reconstruction

**Authors:** Yukai Huang, Haoyu Albert Wang, Jiawei Zhang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08887v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08887v1)

**Summary:** Reconstructing natural visual experience from cortical population activity is a central challenge in neural decoding, particularly for calcium imaging, where signals are noisy, temporally filtered, and paired neural-video data are limited. Here we present Ca2REAL (Calcium Activity to Reconstruct Events, Appearance, and Layout), a neural-to-video framework that conditions a pretrained video diffusion model through separate layout and semantic controls derived from calcium activity. Using measured...

---

### 27. Same Behavior, Different Mechanism: What Finite Experiments Can Certify About Integrated Information

**Authors:** Linqian Wu, Diaoxuan He

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08469v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08469v1)

**Summary:** Interpretability, AI auditing and assessments of machine consciousness increasingly rest on mechanism-level quantities: functionals of a system's causal transition law that describe how it computes, not what it outputs. Experiments see that law only through finite, partial and noisy interventions. We ask when such a quantity is identifiable from an experiment's access, continuous in the mechanism and certifiable from finite data, and answer exactly for a deliberately demanding case - the integra...

---

### 28. Spiking neuromodulation: a linear control perspective

**Authors:** Fulvio Forni, Rodolphe Sepulchre

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08571v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08571v1)

**Summary:** Neuronal excitability is a nonlinear phenomenon, and the complexity of spiking experimental traces sometimes looks defeating. The present paper takes the view point that excitability is a neuromodulated property, and aims to demonstrate that the neuromodulation of spiking is amenable to the classical linear analysis tools of control theory. We illustrate the value of linear feedback analysis as an alternative to bifurcation analysis in the simple yet classical example of spiking modulation by th...

---

### 29. Do sEMG Foundation Models Improve Cross-Subject Generalisation?

**Authors:** William Raftery, Dario Farina

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08199v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08199v1)

**Summary:** sEMG Foundation Models aim to learn general purpose representations over diverse subjects and recording conditions that boost performance on a variety of downstream tasks. However, existing evaluations make it difficult to discern whether pretraining alone is sufficient to combat the cross-subject overfitting which makes machine learning on sEMG so challenging. We conduct a systematic evaluation of three sEMG foundation models across three gesture classification datasets under both intra-session...

---

### 30. Reversible Dynamics, Asymmetric Actions: Parking as a Trajectory-Level Affordance

**Authors:** Adam Y. Shavit

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07965v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07965v1)

**Summary:** Drivers are often told to back into a tight parking space, not drive in nose first. The advice looks paradoxical, because a slow car is dynamically reversible: reverse its speed and replay the steering backward, and it retraces a feasible path. Played backward, though, reverse-in shows a car driving forward out of the space. Reverse-in and forward-in are different tasks: they share a start position but end facing opposite ways. We separate three clearances between car and obstacles. Static fit $...

---

### 31. Invariance before structure: two modes of emergent compression in representation learning

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07952v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07952v1)

**Summary:** Learned representations show striking invariance across biological and artificial neural networks, with different substrates and variations driven by drift, heterogeneity and initialisation. To understand this invariance, we propose Emergent Adaptive Representation Learning (EARL), a framework that distinguishes two modes of emergence in learned representations: state-space compression, where a learned representation gains predictive power over its own future beyond what the network's units can ...

---

### 32. Self-Supervised Learning of Local Predictive Directions as a Neural Computation

**Authors:** Marco Zenari, Xuehao Ding, Daniel Burnham, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07809v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07809v1)

**Summary:** Natural sensory dynamics are globally nonlinear but often exhibit simple local geometry, with nearby trajectories evolving preferentially along a small number of predictive directions. We ask how neural circuits could discover this geometry directly from temporal experience. We introduce Local Predictive Directions (LPD), a self-supervised framework that learns local directions whose projections maximally predict near-future trajectory evolution. LPD applies past-future canonical correlation ana...

---

### 33. Bearing, heading and the perceptual geometry of collective motion

**Authors:** Mohammad Salahshour

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.07214v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07214v1)

**Summary:** Traditional models of collective motion commonly assume that animals turn to match their neighbours' directions of travel. In the harmonic theory, decisions follow from a neural representation of direction, and a neighbour enters only as a stimulus at a bearing, the direction in which it lies. Here we show that a neighbour's spatial extent allows its orientation to enter through projection geometry alone, and the theory generates a matrix of coupling coefficients indexed by the neighbour's beari...

---

### 34. Learning Time-Varying Connectomes for Stable Behavior Across Development

**Authors:** Christof Fehrman, Jacob J. Morra, Eva A. Naumann

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06895v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06895v1)

**Summary:** Neural circuits must maintain functionality to drive effective behavior while their size, topology, geometry, and intrinsic dynamics change across development. To model developing visuomotor circuits and behavior, we investigated whether a single compact generative encoding could produce functional recurrent controllers across such changes. Building on the HyperNEAT algorithm, we represented this program as a compositional pattern-producing network that received developmental time as an input to...

---

### 35. Cell-type-specific modularity in E/I networks shapes dynamical regimes and computational capabilities

**Authors:** Emmanouil Giannakakis, Victor Buendía, Oleg Vinogradov, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06720v1)

**Summary:** Structural modularity is a ubiquitous feature of brain networks that shapes neural dynamics and information processing. Yet excitatory and inhibitory populations can differ in their modular organization, and it remains unclear how this asymmetry affects network dynamics and computation. Here, using dynamical mean-field theory and simulations of networks performing complex temporal tasks, we show that independently tuning excitatory and inhibitory modularity controls the dynamical regimes of bala...

---

### 36. PINR-ESI: Physics-Informed Self-Supervised Implicit Neural Representation Framework for EEG Extended-Source Imaging

**Authors:** Zhiyong Zhou, Sheng Liao, Xiaolin Li, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06700v2) | 📄 [PDF](https://arxiv.org/pdf/2611.06700v2)

**Summary:** EEG extended-source imaging aims to localize active cortical regions and characterize their spatial extent, yet supervised inverse networks typically depend on synthetic EEG-source pairs and may be sensitive to synthetic-to-real mismatch. We propose a physics-informed self-supervised implicit neural representation (INR) framework for spatial source reconstruction without paired source labels or simulation-based supervised pretraining. The lead field matrix encodes the source-to-sensor volume-con...

---

### 37. Synchronized Hearts, Desynchronized Brains: A Nonlinear Dynamics Perspective for Function and Failure

**Authors:** Irene Pellini, Simon Bauer, Seba Contreras, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06618v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06618v1)

**Summary:** Both the heart and the brain are built from electrically excitable cells, yet the emergent dynamics of these organs could not differ more. In the myocardium, a coherent traveling wave of action potentials ensures coordinated contraction; in the cerebral cortex, distributed, irregular spiking underlies efficient information processing and the generation of behavior. Here, we illuminate the principles that underlie the emergence of such distinct nonlinear dynamics using concepts from complex syste...

---

### 38. Time-Division Multiplexing: The Operational Rhythm and Temporal Organization Layer of Digital Life

**Authors:** Haibin Tong, Luming Guo, Nana Cui, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06603v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06603v1)

**Summary:** Continual agents must handle urgent interaction while retaining alternatives, replaying errors, and committing safe long-term changes. A previous digital-life framework distinguishes online (busy) and offline (idle) channels, but leaves open whether these are separate programs or phases of a common process and how their operations should be ordered. Motivated by recent observations of rapidly alternating perceptual representations in primate cortex, we develop a temporal organization layer with ...

---

### 39. Mind Control of LLMs via Closed-Loop Stimulation: Out-of-Distribution Robustness

**Authors:** Kasra Fallah, Rudramani Singha, Hannah Ghanei, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06418v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06418v1)

**Summary:** Brains and large language models need not be considered equivalent systems to reveal an interpretable commonality: both exhibit high-dimensional, nonlinear dynamics whose behavior can only be modeled imperfectly. This creates a shared challenge whenever we seek to intervene in their dynamics. A controller may either rely on a model identified around a particular operating regime and risk failure as the system moves away from that regime, or explicitly account for uncertainty and a changing inter...

---

### 40. A minimal E/I circuit model explains differential recovery from amblyopia under TTX and reverse occlusion

**Authors:** Lawrence Udeigwe

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06189v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06189v1)

**Summary:** Recovery from amblyopia beyond the critical period remains a major challenge in visual neuroscience. Experimental studies show that transient inactivation of the fellow eye with tetrodotoxin (TTX) produces stronger and more persistent recovery than reverse occlusion (RO), despite both interventions reducing competition from the fellow eye. The circuit mechanisms underlying this difference remain unclear.   We develop a minimal cortical circuit model combining excitatory-inhibitory population dyn...

---

### 41. A Bayesian Optimized Biquad Filter-Burg Model for Real-Time EEG Phase Estimation

**Authors:** Ivan Martinez-Kay, Tatiana Kardashina, ShiNung Ching, et al.

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05374v2) | 📄 [PDF](https://arxiv.org/pdf/2611.05374v2)

**Summary:** Real-time phase estimation on stimulus-aligned transient EEG is critical for closed-loop neuromodulation systems targeting the theta-band, yet most real-time phase estimation methods have been developed and validated on resting-state, high-fidelity signals in the alpha band. Recent work has pursued deep learning architectures, while individualized classical bandpass filter tuning remains underexplored. This study characterizes the spectral and temporal properties of non-anticipative bandpass fil...

---

### 42. Curriculum unlearning in humans and neural networks

**Authors:** Jirko Rubruck, Alice Zhang, Andrew Saxe, et al.

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.04565v1) | 📄 [PDF](https://arxiv.org/pdf/2611.04565v1)

**Summary:** During learning, humans often benefit from curricula that teach simple rules before exceptions. However, we lack a computational explanation for this phenomenon. Here, using a canonical behavioural task and modelling with neural networks, we develop and test a theory for why simple-to-complex curricula succeed. We show that during learning, both humans and neural networks show simplicity biases, a tendency to learn simple rules that are underfit to the data. In neural networks this bias is accom...

---

### 43. Memory flows: geometry and dynamics of sequential retrieval in input-driven Hopfield networks

**Authors:** Simone Betteti, Matteo Martin, Morten Gram Pedersen, et al.

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.09995v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09995v1)

**Summary:** Associative memory models classically describe retrieval as convergence to stored patterns, but the theory of sequential retrieval remains comparatively limited. We develop a two-timescale input-driven Hopfield network in which fast associative retrieval is modulated by a slow feedback variable evolving over a prescribed memory-transition graph. This yields autonomous, graph-constrained transitions while preserving analytical tractability. Using slow-fast and geometric singular perturbation theo...

---

### 44. When Model Complexity Matters in Cross-Subject Naturalistic fMRI Prediction

**Authors:** Junhao Zhao, Jacob Kang, Colin Kurniawan, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.04041v1) | 📄 [PDF](https://arxiv.org/pdf/2611.04041v1)

**Summary:** Increasingly complex neural models predict blood-oxygen-level-dependent (BOLD) responses to naturalistic stimuli, but the predictive value of this added complexity remains unclear. We ask when pretrained stimulus representations help and how much downstream complexity is needed, with and without recent measured BOLD history. We compare linear diagnostic references and nonlinear predictors across HCP movie fMRI (154 subjects), BOLD Moments (10 subjects), and Algonauts 2025 (4 subjects). Under a s...

---

### 45. Fly Whiskers Meet LiDAR: Robust Navigation under Sensor Failure

**Authors:** Ali Mahzarnia, Homayoun Jamshidi

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03897v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03897v1)

**Summary:** We extend FLYNN, a leaky integrator recurrent network wired on the Drosophila melanogaster connectome, with a 32-ray 2D LiDAR interface that requires no learned fusion layer beyond a scalar input gain. A 270 degree frontal scan at 8 m range is injected as inverted proximity into the 37 BM Vib head-bristle neurons. Across 24 paired comparisons in a four- state vision matrix with LiDAR on or off, FLYNN-LiDAR has 17 significant wins, 5 nonsignificant comparisons, and 2 significant losses against th...

---

### 46. Evolved Spiking Neural Networks for EEG Seizure Detection: Calcium Dynamics and Delay Mechanics

**Authors:** Tuba Aksoy

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03841v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03841v1)

**Summary:** Neuroevolution can discover compact network designs that are hard to specify by hand. The EONS framework evolves the topology, weights, thresholds and delays of neuromorphic spiking networks without gradients. We tested whether giving integrate-and-fire (IF) neurons an activity-dependent calcium current (Ca-IF neurons) improves evolved networks for EEG seizure detection, with calcium parameters fixed, shared across a network, or evolved for each neuron. On 10 held-out CHB-MIT patients never seen...

---

### 47. Intrinsic network dynamics catalyze switching in functional connectivity states of the brain

**Authors:** Steven S. Kang, Dae-Jin Kim

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03071v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03071v1)

**Summary:** Dynamic functional connectivity (dFC) reflects ongoing reconfiguration of large-scale brain networks, but the temporal organization and network processes underlying spontaneous state transitions remain poorly understood. We developed functional connectivity state switching (FCSS), a phase-coherence-based framework that tracks multiscale changes in dominant whole-brain connectivity configurations. In Human Connectome Project fMRI, FCSS was strongly evoked by cognitive state and condition switches...

---

### 48. AVID: A 5T fMRI Dataset for Benchmarking Auditory-induced Visual Mental Imagery Decoding

**Authors:** Shiqi Shen, Shurui Li, Xilin Zhang, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02593v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02593v1)

**Summary:** Visual mental imagery (VMI) decoding uses brain activity to reconstruct internally generated visual scenes, providing a potential pathway for externalizing internal experiences and developing neuroprosthetic communication interfaces. However, progress is limited by the lack of dedicated, training-scale VMI datasets. Current VMI paradigms often rely on visual prompts or short-term memory images, introducing visual and mnemonic confounds that make it difficult to disentangle neural activity associ...

---

### 49. Prior Action Control Causally Alters Language-Model Plasticity

**Authors:** Marc-Andre Schulz

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02362v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02362v1)

**Summary:** Two copies of one language model start from identical weights and receive the same rewards during training. For one copy the rewards depend on its own answers. The other copy is yoked: it receives the first copy's rewards no matter what it answers, a design taken from the learned-helplessness experiments of animal learning. We ask whether the copy whose rewards depended on its answers, the copy with control, later learns a new task faster, that is, whether control changes the model's plasticity....

---

### 50. Modeling Visual Cortex with Layerwise Multiscale Manifold Capacity Maximization

**Authors:** Thomas Yerxa, SueYeon Chung, Eero P. Simoncelli

**Published:** 2026-11-01

🔗 [Paper](http://arxiv.org/abs/2611.02245v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02245v1)

**Summary:** Task-optimized deep neural networks have risen to prominence as the most predictive phenomenological models of responses in primate visual cortex, but leave much to be desired from the perspective of biological plausibility. One such limitation is the reliance on precise credit assignment through global backpropagation of error signals. Recent work has shown that this weakness can be circumvented by requiring each subsequent stage to solve a distinct and increasingly complex task, allowing for l...

---

## stat.ML

**50 papers**

### 1. TorchCurves: Differentiable Parametric Curves

**Authors:** Alex Shtoff

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14516v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14516v1)

**Summary:** We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curve coefficients can be optimized jointly with the surrounding model or produced by another network. The library provides trainable modules, reusable basis modules, and a functional interface, supportin...

---

### 2. A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets

**Authors:** Audrey Huang, Nan Jiang, Sham M. Kakade, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14467v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14467v1)

**Summary:** Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to identify algorithms that learn near-optimal policies using total samples and gradient steps governed by the base model's response coverage, a measure of how readily it generates optimal responses. We call such algorithms coverage-preserving. This guarantee captures the goal of amplifying capabilities accessible through sampling from the base model.   ...

---

### 3. One Curve, Different Weights: AUC, the Brier Score, Decision-Weighted AUC, and the Policy Youden Index

**Authors:** Yegor Baranovski

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14465v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14465v1)

**Summary:** AUC and the Brier score are standard summaries of a binary risk score, yet they can rank models differently. We introduce a weighted AUC, AUC$_π$, which weights each pair of observations by how differently a decision maker with probability of acting $π$ treats them. We show that all three are built on weighted averages of one curve, the Youden index $J(t) = \mathrm{TPR}(t) - \mathrm{FPR}(t)$ across cutoffs $t$, and that the averages differ in the weights they put on the cutoffs. Each weights a c...

---

### 4. A Theory of Cross-Validation Variance

**Authors:** Nathaniel S. O'Connell, Jaime L. Speiser

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14463v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14463v1)

**Summary:** Cross-validation estimates predictive performance by repeatedly splitting the data into training and validation sets, fitting the model on the first and evaluating it on the second. Every observation influences the estimate in two roles, through its own evaluation when it is held out and through the models it helps fit when it trains. The random splits determine its weight in each role. From this representation, we prove an exact finite-sample identity for the variance of the cross-validated est...

---

### 5. Nonparametric Maximum Likelihood Estimation for Mixtures of Logistic Regressions

**Authors:** Muheng Li, Peize Zhang, Xin Bing

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14445v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14445v1)

**Summary:** Mixtures of logistic regressions provide a flexible framework for modeling binary responses, extending standard logistic regression to accommodate unobserved heterogeneity while retaining an interpretable regression structure. In this paper, we study such models with an unspecified mixing distribution. We analyze a sieve nonparametric maximum likelihood estimator (NPMLE) and derive nonasymptotic bounds on the estimation error of the resulting mixture regression function under both fixed and rand...

---

### 6. Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without High-Order Approximation

**Authors:** Yuchen Jiao, Na Li, Changxiao Cai, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14328v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14328v1)

**Summary:** Stochastic diffusion samplers often require substantially more neural function evaluations (NFEs) than deterministic samplers to achieve comparable sample quality. Although higher-order discretization accelerates deterministic sampling, its benefits for stochastic sampling remains unclear. We establish matching upper and worst-case lower bounds showing that stochastic samplers with higher-order approximations remain first-order convergent, even with exact score functions. Thus, increasing the ap...

---

### 7. Compositional random forest

**Authors:** Khaled Masoumifard, Stephan van der Westhuizen, Sugnet Gardner-Lubbe

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14275v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14275v1)

**Summary:** Compositional data have been analysed in the literature from three main points of view: directly on the simplex, in log-ratio coordinates, and as directional data on the unit sphere. In this paper, we construct a random forest framework for compositional responses that accommodates all three. Random forests are ensembles of decision trees, and the split criterion determines how each tree grows. We use the log-likelihood gain as the split criterion and consider distributions defined on the differ...

---

### 8. On the Spectral Estimation of VARMA Processes

**Authors:** Bin Zhu, Mattia Zorzi

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13973v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13973v1)

**Summary:** We consider the problem of estimating the power spectral density of a Vector-valued Autoregressive Moving-Average (VARMA) process. A well-established approach to accomplishing this task consists of formulating a moment problem that selects the spectral density maximizing an entropy-like index while matching certain moments of the underlying process. However, existing methods assume that the moving-average (MA) component is either fixed or scalar, thereby reducing the class of ARMA models over wh...

---

### 9. MEOW: Medical Open-World Interactive Segmentation

**Authors:** Philip Matthias Winter, Maria Wimmer, Bernhard Schäfl, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13935v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13935v1)

**Summary:** In open-world recognition, machine learning models not only make predictions on unknown structures ("generalized open-set"), but also continually learn and improve from those predictions over time. Interactive segmentation, despite its access to user feedback, has so far remained confined to the open-set setting. In this work we introduce MEOW, the first framework that turns non-interactive segmentation backbones into interactive open-world learners without updating learnable model parameters. M...

---

### 10. Outliers and the Hard-Margin Linear SVM in High-Dimension, Low-Sample-Size Settings

**Authors:** Yugo Nakayama

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13869v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13869v1)

**Summary:** We study how outliers affect the hard-margin linear support vector machine when the dimension grows while the sample sizes remain fixed. For one-sided contamination, the centered Gram matrix converges to a constant inlier block plus an outlier-diagonal component, and the limiting dual problem has a closed-form solution. All outliers act through one effective distance. This representation yields explicit thresholds for loss of inlier support, margin shrinkage. intercept displacement, and asymptot...

---

### 11. Beyond Interaction Scores: Selecting Feature Interactions via Independent Replication

**Authors:** Jincheng Gao, Shuo Sun

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13765v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13765v1)

**Summary:** Learning feature interactions is essential for accurate prediction and interpretable modeling, yet a high interaction score may reflect fitting noise rather than a reproducible pattern. Ranking methods score feature pairs but leave the cutoff to the user; testing methods set the cutoff but rely on repeated model refits or a model of the joint feature distribution. We present LENS, a model-agnostic framework for selecting feature interactions through independent replication. LENS trains two model...

---

### 12. CP-MLPs: A Tensor-Rank Theory of Tied and Untied MLP Blocks

**Authors:** Md Rifat Arefin, Farzaneh Heidari, Irina Rish, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13647v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13647v1)

**Summary:** Transformer feed-forward blocks combine several design choices: squared activations, gating, and tied versus untied parameter sharing, whose separate contributions to expressivity remain poorly understood. We introduce CP-MLPs, a tensor framework in which each multiplicative unit contributes a rank-1 interaction with three roles: detecting an input feature, reading a value, and writing to the output. Tied gated blocks such as ReLU$^2$ force the detector and value roles to share the same directio...

---

### 13. First-order asymptotic expansions for spectral convergence of normalized graph Laplacians constructed from samples on manifolds

**Authors:** Eunseong Bae, Wolfgang Polonik

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13623v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13623v1)

**Summary:** Under i.i.d. uniform sampling from a closed Riemannian manifold embedded in Euclidean space, we derive first-order asymptotic expansions for the eigenvalues and eigenvectors of symmetrically normalized graph Laplacians constructed via Gaussian kernels and provide concentration inequalities for the remainder terms. As a direct consequence, we establish the corresponding weak convergence results. Unlike most related works, our analysis does not impose a multiplicity-one assumption on the eigenvalu...

---

### 14. Investigating Composite Modeling in Multi-Objective Bayesian Optimization for Scientific Design

**Authors:** Ricky Ye, Sahas Goli, Muhammad Ali, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13565v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13565v1)

**Summary:** Scientific design often requires balancing competing objectives that are expensive to evaluate through experiments or simulations. Multi-objective Bayesian optimization (MOBO) addresses this challenge by using probabilistic models to guide the selection of promising designs. In many applications, tunable inputs map to observable intermediate responses, which are then combined through known functions to compute the final objectives. Prior work on Bayesian optimization of composite functions shows...

---

### 15. Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic Rounding

**Authors:** Mahdi Nazemi, Oleg Rybakov, Tijmen Blankevoort, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13545v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13545v1)

**Summary:** BF16 is widely used to pretrain large language models because it has the same dynamic range as FP32 and converges similarly to FP32 training. However, in reinforcement learning with verifiable rewards, where learning rates are typically low, we find that standard mixed-precision BF16 training converges more slowly than FP16 training at the same learning rate. We attribute this gap to weight sticking: when FP32 shadow weights are quantized to BF16 using round-to-nearest, small updates often leave...

---

### 16. Simultaneous Near-Optimal Region Identification in Continuous Simulation Optimization: Minimax Complexity and Adaptive Sampling

**Authors:** Yilin Zheng, Haowei Wang, Wenjia Wang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13489v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13489v1)

**Summary:** Simulation optimization typically returns a single estimated optimal point. When decisions also depend on criteria evaluated independently of simulation, such as resource cost, the decision maker instead needs the set of designs whose expected performance lies within a tolerance of the optimum, often choosing the tolerance only after seeing the tradeoffs. We study how to identify these near-optimal regions on a continuous design space, simultaneously for all tolerances up to a prescribed maximum...

---

### 17. Differentially Private Statistical Inference for Rankings from Pairwise Comparisons

**Authors:** Xintao Xia, Jia Gu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13485v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13485v1)

**Summary:** Reliable inference for rankings of large language models based on human pairwise comparisons must preserve the privacy of individual preference records. To meet this need, we develop methods for score and rank inference under the Bradley-Terry model with edge differential privacy. For an objective-perturbed estimator, a new leave-one-out analysis establishes finite-sample bounds on Euclidean and entrywise estimation errors. For sufficiently dense comparison graphs, the error bounds extend to sma...

---

### 18. Sufficient Dimension Reduction with Multimodal Predictor Objects

**Authors:** Abdul-Nasah Soale

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13460v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13460v1)

**Summary:** We study the regression of a scalar response $Y$ on a Euclidean predictor $\mathbf{X} \in \mathbb{R}^p$ and a random predictor object $\mathcal{Z}$ in a general metric space under arbitrary structural dependence. We introduce a joint sufficient dimension reduction $(\mathbf{B}^\top\mathbf{X}, \mathcal{G}_Z)$ constructed via a sequential conditional independence framework, which differs fundamentally from the ordinary central subspace of $Y \mid \mathbf{X}$. Methodologically, $\mathcal{Z}$ is emb...

---

### 19. Settling the Burn-in Gap: Sharp Risk Bounds for Tail-Averaged SGD in Linear Regression

**Authors:** Qingyue Zhao, Xuheng Li, Quanquan Gu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13383v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13383v1)

**Summary:** We study the excess risk of constant-stepsize online stochastic gradient descent (SGD) with tail-averaging for high-dimensional linear regression. Building on the instance-dependent spectral framework of Zou et al. (2021), we establish matching initialization-explicit upper and lower bounds on the total excess risk of tail-averaged SGD in terms of the population covariance spectrum $\mathbf{H}$ and initialization $\mathbf{w}_0-\mathbf{w}^*$ whenever a trajectory spectral feedback condition holds...

---

### 20. VC-Dimension and Generalization in Geometric Machine Learning with Applications to Active Learning

**Authors:** Gokul Bhusal, Delanna Do, Ekaterina Merkurjev, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13337v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13337v1)

**Summary:** We compute the VC-dimension of metric ball classifiers in the model spaces of Riemannian geometry (Euclidean, spherical, hyperbolic) and present upper and lower bounds on the VC-dimension of metric balls in several other situations, including general normed vector spaces (potentially infinite VC-dimension), vector spaces with $\ell^p$-norms (VC-dimension grows at least linearly in the dimension, faster than Euclidean for $p=1$), flat tori, and general Riemannian manifolds (arbitrarily large VC-d...

---

### 21. Time Series Change Point Detection with Gaussian Processes

**Authors:** Olga Isupova, Danil Kuzin, Fredrik Gustafsson, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13295v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13295v1)

**Summary:** This paper proposes a novel general Gaussian process framework for change point detection in time series. A change is defined as an alteration of the hyperparameters of the Gaussian process prior. We formulate the problem in the context of statistical hypothesis testing and demonstrate its performance over both offline and online multiple change points detection. The approach provides theoretical guaranties of its performance. An important advantage of the developed framework is that it does not...

---

### 22. Continuous Horizon Forecasting

**Authors:** Malcolm Wolff, Elliott Zackrone, Souhaib Ben Taieb, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13228v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13228v1)

**Summary:** Multi-horizon forecasting has been dominated by discrete forecast strategies that treat model outputs as fixed-vectors or recurrently create them. In this paper, we introduce the Continuous Horizon (CH) strategy that generalizes upon recursive, direct, and multi-step strategies by redefining forecasts as a continuous operator and the forecast horizon as a query variable rather than an index. We present the theoretical foundations for the CH strategy, a Universal Operator Approximation Theorem, a...

---

### 23. MediPFN: Amortized In-Context Nuisance Learning and Inference for Causal Mediation Analysis

**Authors:** Shi Bo, Jiaming Hu

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13219v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13219v1)

**Summary:** Causal mediation analysis decomposes a treatment effect into indirect pathways through mediators and direct pathways through other processes. Tabular foundation models perform classification and regression through in-context learning, providing estimates of conditional means and propensity scores used in causal mediation analysis. Constructing confidence intervals from these estimates requires accounting for uncertainty introduced by fitting and combining several nuisance functions. We introduce...

---

### 24. Prediction Inference for Hybrid Models on Realized Volatility Forecasting

**Authors:** Kyle Parrella, Kejin Wu

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13212v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13212v1)

**Summary:** GARCH-LSTM hybrid models have become increasingly popular in the volatility forecasting literature. To date, these models have almost exclusively focused on point estimation and accuracy measures such as RMSE and MAPE, while failing to assess the uncertainty of these point estimates. We approach this gap in two ways. First, we extend the existing GARCH-LSTM model by modeling the conditional mean with an ARMA structure. Second, we develop a forward bootstrap algorithm to build multi-step-ahead pr...

---

### 25. Near-Optimal Sample Complexity of Deterministic Agnostic PAC Learning

**Authors:** Shai Ben-David, Steve Hanneke, Farnam Mansouri, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13210v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13210v1)

**Summary:** We study the problem of agnostic PAC learning under deterministic labels, where the examples are labeled by an arbitrary deterministic function, which need not belong to the concept class $C$. This model captures misspecification without stochastic label noise and lies between the realizable and fully agnostic settings. Prior work showed that, when $C$ has finite diameter $K$ and VC dimension $d$, deterministic labels can improve the sample complexity upper bound from the classical agnostic guar...

---

### 26. From Granger causality to causal structure in dynamical systems

**Authors:** Víctor Elvira

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12755v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12755v1)

**Summary:** The idea of testing whether the past of one signal improves the prediction of another can be traced back to Wiener. It was Granger who formalized the concept. Granger causality has become one of the most widely used tools to infer directed interactions between the components of a system. The name however can be misleading: it detects predictive relations among the measured signals, not causal relations among the mechanisms that generate them. This article starts by reviewing recent advances in o...

---

### 27. Clique Constraints for Exact Causal Structure Learning

**Authors:** Xiaoyu He, Pavel Rytíř, Petr Ryšavý, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12747v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12747v1)

**Summary:** Exact score-based causal structure learning supports explicit structural constraints and optimisation certificates, but its branch-and-cut search can be computationally demanding. We augment exact causal structure learning methods with an upper bound on the maximum clique size of the learned undirected skeleton, enforced at integer candidates through lazy cycle and clique constraints. On static linear-Gaussian Erdős-Rényi and scale-free DAGs, we evaluate callback order, alternative clique-cut po...

---

### 28. Hidden Tails: Certifying Tail-Risk Claims under Selective Labels

**Authors:** El Mustapha Mansouri

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12713v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12713v1)

**Summary:** Historical decisions determine which outcomes are observed, potentially concealing a predictor's largest errors. Even unlimited data from the same observation process can therefore leave population tail risk unresolved. Here we derive sharp bounds on conditional value-at-risk, the average loss in a specified upper tail, for binary outcomes and bounded losses. These bounds span exactly the risks compatible with the observations and a stated limit on how outcome odds differ between observed and hi...

---

### 29. Fisher-Glass Learning: Classification Bounds and Subpopulation Audits

**Authors:** El Mustapha Mansouri

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12702v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12702v1)

**Summary:** Accurate classifiers can fail when background cues change without altering the correct labels. Predictive performance alone does not quantify how much task information remains after accounting for such nuisance variation. Here we extend the Fisher-glass framework to connect nuisance-adjusted information with local classification difficulty and subpopulation auditing. We derive lower bounds on local minimax excess classification risk under explicit distinguishability and decision-separation condi...

---

### 30. Generalized Adaptive Boosting and the Geometry of Mistakes

**Authors:** Marco Bressan, Nataly Brukhim, Nicolò Cesa-Bianchi, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12696v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12696v1)

**Summary:** Not all mistakes are alike. For example, in medical diagnosis, false positive and false negative mistakes have a different impact and should not be aggregated. By revisiting the classical theory of boosting through this lens, we introduce the notion of $Z$-learner, which returns weak hypotheses achieving joint false-positive/false-negative guarantees $(\mathrm{FP},\mathrm{FN})$ from some set $Z \subseteq [0,1]^2$. This formulation generalizes the standard notion of $γ$-weak learning--recovered b...

---

### 31. Graph-Guided Bayesian Factor Analysis: A Fast Integrated EFA-CFA Approach for High-Dimensional Data

**Authors:** Shitao Fan, Lizhen Lin, Zhenyao Ye, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12612v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12612v1)

**Summary:** Factor analysis has been central to the analysis of high-dimensional biomedical data. However, existing exploratory and confirmatory factor analysis methods face several limitations: less interpretable factor findings, difficulty in identifying which variables can and cannot be represented by low-dimensional factors, challenges in estimating the covariance among factors, and maximum-likelihood fits that break down when variables outnumber subjects. We propose graph-guided Bayesian factor analysi...

---

### 32. Out-of-the-Box Tabular Foundation Models for Bayesian Optimization in Materials Discovery

**Authors:** Klemens Flöge, Simon Bing, Leo Grinsztajn, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12491v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12491v1)

**Summary:** Bayesian optimization is widely used in active learning loops for materials science. Gaussian processes serve as the de-facto surrogate model family, but require task-dependent kernel choices and can lack the modeling capacity for complex relationships. Tabular foundation models (TFMs) have recently emerged as the state-of-the-art for predictive tasks on structured data, without requiring bespoke kernels or hyperparameter tuning. We evaluate two TFMs, TabPFN and TabICL, as out-of-the-box surroga...

---

### 33. Prediction with Foundation Models under Deployment Budgets

**Authors:** Zhaohui Xu, Xiaofei Xu, Doudou Zhou

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12466v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12466v1)

**Summary:** Foundation models can supply predictions for a downstream task that draw on knowledge from extensive pretraining, but they differ in task-specific accuracy and query cost. We develop a framework that improves prediction for the task under a budget on the average query cost per input, using training data to learn which models to query and how to combine their outputs with features available without querying. The first method queries the same models for every input; the second lets them vary acros...

---

### 34. Causal discovery from Bayesian symbolic regression

**Authors:** Roger Guimerà, Kai-Hendrik Cohrs, Sergio Pedreira, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12458v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12458v1)

**Summary:** Causal discovery from observational data is central to scientific reasoning, yet established constraint-based and score-based methods often recover only a Markov equivalence class and provide no signal in bivariate or strongly autocorrelated regimes typical in some areas of science. Here, we recast causal discovery as a Bayesian symbolic regression problem. Given a set of candidate parents for each target variable, the Bayesian symbolic regression samples closed-form expressions from a posterior...

---

### 35. Two-Phase Rapid Simulation-Based Inference with Differentiable Simulators

**Authors:** Uros Zivanovic, Rahul Srinivasan, Roberto Trotta, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12422v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12422v1)

**Summary:** We introduce Rapid Simulation Based Inference (RSBI), a diffusion-based variational approach to likelihood-free Bayesian inference that achieves high sampling efficiency under large prior-to-posterior volumes. RSBI builds on advances in Schrödinger Bridge (SB) diffusion sampling to handle multi-modal posteriors, with an initial likelihood supplied by a distance measure via a differentiable simulator. The key innovation of this initial surrogate likelihood is that it gives a highly efficient prop...

---

### 36. Optimal Rates for Adaptive Private $k$-PCA

**Authors:** Johanna Düngler, Amartya Sanyal

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12419v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12419v1)

**Summary:** Given $n$ i.i.d. random matrices $A_i \in \mathbb{R}^{d \times d}$ with common expectation $Σ$, the goal of \emph{Differentially Private Stochastic PCA} is to identify a $k$-dimensional subspace capturing the leading variance directions of $Σ$, while preserving differential privacy~(DP) for each individual sample $A_i$. \citet{dungler2025iterative} introduced \kdppca, the first algorithm to simultaneously (1) achieve sample complexity $n=\widetilde O(d)$ for sub-Gaussian data, (2) adapt its priv...

---

### 37. Odds-Structured Distributional Regression for Interpretable Time-to-Event Prediction

**Authors:** Jakob Versnjak, Manuel Welte, Titus Kuehne, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12268v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12268v1)

**Summary:** Time-to-event prediction is fundamentally challenged by partial observability and aleatoric uncertainty. In clinical medicine, for instance, the timing of disease progression or acute readmission is contingent on highly dynamic and largely latent health trajectories. Rather than forcing a deterministic point forecast, distributional regression offers a principled means to address this complexity by predicting a probability distribution over time. However, explaining these distributional predicti...

---

### 38. A method to automatically discover symbolic local learning rules

**Authors:** Andrea Perin, Fabio Anselmi, Stephane Deny

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12248v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12248v1)

**Summary:** We present a general method for discovering symbolic local learning rules that can replace backpropagation, applicable, in principle, to any deep learning architecture and task. The method automatically discovers local loss functions specific to each layer by (1) constructing a dictionary of monomials of local tensor variables, inspired by Penrose diagram notation, (2) regressing over coefficients weighting these monomials to build layerwise polynomial losses whose gradients together minimize a ...

---

### 39. The balance between feature learning and collapse in dynamical systems-based generative models

**Authors:** Julian Brandon, Bruno Loureiro, N Alex Cayco-Gajic, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12156v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12156v1)

**Summary:** Over the past decade, a growing body of work has established that implicit biases in learning dynamics fundamentally shape the solutions found by neural networks, governing their learned features and generalisation performance. However, despite these strides in deep learning theory, far less is known about representation learning in generative models based on dynamical systems, from normalising flows to diffusion. Importantly, empirical evidence suggests that continuous-time generative models ca...

---

### 40. Geometry and Stochastic Analysis of Flow and Diffusion Models: A Survey

**Authors:** Ehsan Mirafzali, Razvan Marinescu

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12107v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12107v1)

**Summary:** Flow-based and diffusion-based models have become the principal means of learning and sampling high-dimensional probability distributions, from images and video to proteins, molecules and physical fields, and increasingly language. Each carries a simple law to the law of the data along a curve of probability measures, and behind the variety of their names lie three geometries, those of the state space on which the data live, of the space of probability measures through which the curve passes, an...

---

### 41. A Black-Box Reduction from Regret to Multi-Level Coverage

**Authors:** Tuo Liu, Edgar Dobriban, Francesco Orabona

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12059v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12059v1)

**Summary:** Online Conformal Prediction (OCP) sequentially constructs prediction sets whose average empirical coverage converges to a target level over time, for arbitrary, potentially adversarial datasets. In the multi-level setting, prediction sets are produced at $d$ coverage levels at once. Prior work argued for the use of online gradient descent with isotonic projections, which produces sets nested across levels, but with a $\sqrt{d}$ dependence in the per-level coverage convergence rate. Here, we both...

---

### 42. Scale-Invariant Empirical-Bayes Laplace Approximation for ReLU Networks

**Authors:** Shivam Pal, Piyush Rai

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12031v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12031v1)

**Summary:** ReLU networks are well-known to have continuous scale symmetries; infinitely many reparameterized weight vectors that represent the same function. Dinh et al. (2017) have shown that, by reparameterizing, the geometry of the loss landscape (e.g., curvature) of these networks can be changed arbitrarily without affecting the underlying function. Thus, any quantity that depends on the network's geometry should be defined with care. In this paper, we show that the Empirical Bayes (EB) Laplace's appro...

---

### 43. Conformal Prediction for Multi-Step Forecasting: Conditional Coverage and Sharp Score Calibration Rates

**Authors:** Siyuan He, Yuhong Yang

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12004v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12004v1)

**Summary:** Uncertainty quantification in prediction is a central problem in statistics and machine learning. Conformal prediction provides a flexible approach to constructing prediction sets with valid marginal coverage under exchangeability. In this paper, we investigate conformal prediction for both one-step and multi-step forecasting from a single stationary time series, addressing temporal dependence and the additional challenges of joint prediction across multiple horizons. We propose a kernel-based f...

---

### 44. Trajectory Density Ratios under Weak Support: A Survey across the Sciences

**Authors:** Wei Chen, Lihao Zhuang, Yubing Wu, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11985v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11985v1)

**Summary:** Many problems across the sciences compare two stochastic processes through the sequences they generate. Reinforcement learning asks what a new policy would return from the trajectories of an old one; molecular simulation asks how much more a ligand binds from samples of the unbound state; climate attribution asks how a heat wave shifted under warming; and language-model post-training asks what a deployed agent will do from logged interactions. In every case, one quantity would answer all these q...

---

### 45. Beyond Prediction Residuals: Conformal Regret Calibration for Robust Contextual Linear Optimization

**Authors:** Lingjie Zhao, Hansheng Jiang, Wei Qi

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11973v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11973v1)

**Summary:** Predict-then-optimize systems convert contextual forecasts into decisions, yet conformal robust optimization typically calibrates prediction residuals rather than downstream loss. For linear optimization, this parameter-space geometry can be badly misaligned with decision risk: large objective perturbations may preserve the optimizer, while small boundary-crossing perturbations may cause substantial regret. We introduce Conformal Regret Sets, a post-hoc, model-agnostic framework that conformaliz...

---

### 46. Characterizing Underrepresentation when Generalizing Causal Survival Estimates

**Authors:** Bolun Liu, Sean McGrath, Yiren Hou, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11923v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11923v1)

**Summary:** Randomized trial findings are routinely generalized to broader target populations to inform decisions in medicine and public policy. When the trial sample is misaligned with the target population, generalized effect estimates can yield suboptimal decisions. We characterize the target subgroups that are underrepresented in the trial cohort in time-to-event settings. Here, underrepresentation arises in two distinct ways: baseline underrepresentation, when a subgroup's covariate profile is rare in ...

---

### 47. Deep-Learning-Assisted Bayesian Inference for Extreme-Mass-Ratio Inspirals

**Authors:** Jian-Jun Song, Zhong-Wu Xia, Wen-Hong Ruan, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11922v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11922v1)

**Summary:** Extreme-mass-ratio inspirals (EMRIs) pose a major challenge to Bayesian parameter inference because of their complex, highly multimodal likelihood surfaces. Locating narrow high-likelihood regions is particularly difficult without knowledge of the true source parameters, which is unavailable in real observations. We develop a deep-learning-assisted Bayesian inference framework that combines neural-network-guided parameter-space localization, particle swarm optimization, and Markov chain Monte Ca...

---

### 48. Identifiable but Hard to Estimate: Rotation in Equally Spaced Overcomplete ICA

**Authors:** Wenjun Xiao, Yinghao Fang, Hanxin Chen, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11852v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11852v1)

**Summary:** How many observations are needed to estimate a common rotation in two-dimensional overcomplete independent component analysis? We study equally spaced mixing columns with known source count, common source law, and column norm. For a fixed non-Gaussian fourth-order Gram-Charlier source law, the rotation is identifiable modulo the column spacing. Yet the sample size for fixed relative angular accuracy grows exponentially with the source count. We characterize this sample size, up to absolute const...

---

### 49. Severity-Controlled Prediction Sets for Medication Recommendation

**Authors:** Yu Gu, Zijun Yu, Chi-Kuang Yeh, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11847v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11847v1)

**Summary:** Medication recommendation is a multi-label prediction task. However, existing prediction-set evaluation and calibration methods rely mainly on exact-overlap metrics and therefore treat all missed medications as equally severe, overlooking how closely the prediction set matches them within the medication hierarchy. To address this, we introduce Conformal Severity Control (CSC), a post-hoc framework for calibrating medication prediction sets under hierarchy-aware mismatch severity. CSC uses the An...

---

### 50. How Path Integral Diffusion Decides a Finite Spin Glass

**Authors:** Michael Chertkov

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11826v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11826v1)

**Summary:** When an AI diffusion-type generator samples a frustrated spin glass, which macroscopic alternatives does it decide first, and when? We study this for bridge-diffusion models of the Path Integral Diffusion (PID) type started from a point source. We show that every isotropic PID is a time-changed Gaussian stochastic localization, and conversely every signal-to-noise schedule is realized by a PID protocol. What a continuous-time generator decides therefore does not depend on the protocol, which onl...

---

