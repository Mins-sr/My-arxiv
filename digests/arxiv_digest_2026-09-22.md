# arXiv Daily Digest - 2026-09-22

Total papers: 200

---

## cs.AI

**50 papers**

### 1. GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay

**Authors:** Yiran Wang, Xingyilang Yin, Junfu Pu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25001v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25001v1)

**Summary:** Modern video games provide a measurable testbed for AI models, combining abilities of visual understanding, instruction decomposition, goal planning, and precise action control over multiple temporal horizons. Existing datasets and benchmarks, however, either cover a narrow range of games, lack language instructions, or rely on high-variance online rollouts. To address these challenges, we introduce GameHorizon, a unified data and evaluation suite that measures gameplay capabilities at different...

---

### 2. WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory

**Authors:** Wangbo Yu, Kunhao Liu, Wenbo Hu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24984v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24984v1)

**Summary:** Video world models enable interactive exploration of dynamic environments, yet struggle to respect prior observations over long horizons and across viewpoints. We present WorldCrafter, a video world model that learns a camera-queryable implicit 3D-aware memory for this purpose. The key insight is to let the requested viewpoint shape how multi-view evidence is compressed into the video generator's limited token budget. Trained jointly with the video generator, a memory encoder and pose-conditione...

---

### 3. DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation

**Authors:** Haoran Yuan, Zekai Wang, Boning Shao, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24976v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24976v1)

**Summary:** Dexterous manipulation depends on contact dynamics that are often only partially observable from vision. Recent World-Action Models (WAMs) couple predictive video world modeling with action generation, but remain largely vision-centric and therefore cannot directly model these contact dynamics. We present DexTacWAM, a visuo-tactile WAM that encodes each fingertip independently, aggregates the resulting features through a finger- and pose-aware tactile compressor, and injects the tactile latent i...

---

### 4. Harness-Zero: Harness Distillation via Agent-as-Harness

**Authors:** Haoran Ye, Yuxing Lu, Haonan Dong, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24974v1)

**Summary:** Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent must either settle for a suboptimal shared harness or route among an ever-growing set of specialized ones. We therefore study agent harness distillation: using a domain- or instance-optimized harness as training-time gui...

---

### 5. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

**Authors:** Peng Xia, Rujun Han, Zifeng Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24972v1)

**Summary:** An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-d...

---

### 6. DolphinBench: Mapping the Pareto Frontier of Agent Memory

**Authors:** Soumil Rathi, Deshraj Yadav, Taranjeet Singh

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24971v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24971v1)

**Summary:** Agents today often take real-world actions that depend on long-term memory and context recall over time. However, most current memory benchmarks are built for a conversational question-answer format, where the question itself signals that some fact must be retrieved, and often which one. Moreover, benchmarks rarely require anything beyond accuracy from submissions, allowing memory systems to make unreasonable cost/time tradeoffs to achieve higher scores.   We present DolphinBench, a benchmark th...

---

### 7. Rare Event Estimation via Iterative Unalignment

**Authors:** Hanming Yang, Daksh Mittal, Jing Dong, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24969v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24969v1)

**Summary:** As agents are deployed with increased autonomy, even extremely rare events along their stochastic output trajectories can occur and prove catastrophic. Safe deployment therefore does not depend on whether these events can occur, but on how often they might. We study the problem of estimating the probability of rare events that arise from stochastic variation in the agent's own actions. Estimating this type of risk requires searching over the combinatorially vast space of trajectories. Naive Mont...

---

### 8. Emergent Collusion in Long-Horizon LLM Agent Interaction

**Authors:** Xinrui Shi, Yanzhe Zhang, Diyi Yang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24967v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24967v1)

**Summary:** LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from th...

---

### 9. Jev for Scientific Decisions: Evaluating Semantic Choices and Their Consequences

**Authors:** Boyuan Deng, Shuyi Fan, Hongyang Zhang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24965v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24965v1)

**Summary:** Scientific workflows often require choosing among known relations before a deterministic calculation can proceed. Whether observations share a culture, treatment or reference standard can change the scientific meaning of the resulting count or comparison. We evaluate Jev as a semantic decision component using a harness that follows its documented guidance and assigns arithmetic to code. The study compares twelve model configurations on twenty source-grounded Choices across ten scientific cases, ...

---

### 10. Generative Tutorial: Towards Live Contextualized Visual Instructions for Physical Tasks

**Authors:** Muzhe Wu, Zuchen Li, Xu Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24955v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24955v1)

**Summary:** Visual instructions for physical tasks are typically authored in one context and followed in another, requiring users to translate demonstrated tools, materials, and spatial relationships into their own environment. We introduce Generative Tutorial, a conceptual framework for live visual instruction that depicts intended outcomes and actions within the user's environment and task flow. A formative evaluation of state-of-the-art image and video generation identifies failures and potential benefit...

---

### 11. Exactness at Inference: A Representational Criterion for Out-of-Distribution Generalization

**Authors:** Filipe Marinho Rocha, Inês Dutra, Vítor Santos Costa, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24942v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24942v1)

**Summary:** A model generalizes outside its training distribution only when it computes a representation structurally equivalent to the generating mechanism, not an approximation fitted to it. Such equivalence is necessary for exactness in and out of distribution, and extrapolation is governed by this exactness at inference, whatever its realization. Tensor Logic shows this: a zero-temperature contraction is equivalent to discrete logic, deducing in place with no artefact extracted, its tensors Boolean, its...

---

### 12. Et Tu, Brute? Economic Misalignment in Personal AI Agents

**Authors:** Aman Priyanshu, Supriti Vijay, Brian Jabarian, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24927v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24927v1)

**Summary:** Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The agent is given access to the user's personal context, e.g., their email inbox and a structured profile of personal attributes, with the intention of making an optimal, personalized decision for the user. We show that by simply providing this personal context, the agent steers recommendations based on i...

---

### 13. BackTrend: Evaluating Scientific Weak-Signal Prediction via Backward Reconstruction

**Authors:** Xiao Zhou, Yilun Zhao, Owen Jiang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24921v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24921v1)

**Summary:** Scientific weak signals are early, low-visibility research directions that later become central to mature scientific topics, yet existing resources such as trend tracking, citation forecasting, and foresight reports rarely provide validated reference sets that link concrete early precursors to later paradigms. We introduce BackTrend, a retrospective benchmark in which, given a mature target topic and a temporal evidence constraint, systems must recover two types of precursors: problem-space sign...

---

### 14. Visuomotor Robotic Pruning in Planar Orchards Using Hybrid Reinforcement Learning

**Authors:** Abhinav Jain, Cindy Grimm, Stefan Lee

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24906v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24906v1)

**Summary:** Dormant tree pruning is labor-intensive yet essential for maintaining modern high-productivity fruit orchards. In this work, we focus on pruning of modern planar tree training systems - V-Trellis apples and UFO cherries - where trunks and primary branches are trained into approximately planar walls. We introduce an end-to-end pipeline to learn a closed-loop visuomotor controller for robotic pruning. This controller is trained entirely using simulation and synthetically generated data and deploye...

---

### 15. OSWorld-Pro: Process-based Evaluation for Computer Use Agents

**Authors:** Zhilin Wang, Shaokun Zhang, Yifan Zhang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24890v1)

**Summary:** Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely prov...

---

### 16. A Global Comparison of Schemas, Transparency, and Interoperability in Public-Sector AI Registers and Inventories

**Authors:** Dipto Das, Shion Guha

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24883v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24883v1)

**Summary:** Artificial intelligence (AI) registers and inventories aim to make governmental AI visible, but their institutional scope, schemas, and reporting practices construct different representations of public-sector AI. We compare 8,368 records from country-specific and transnational inventories covering 72 countries. Across 23 harmonized fields, registers shared a descriptive core but rarely requested information about appeals, risks, legal bases, or external evaluation. We found that broad schemas of...

---

### 17. Pinocchio: Fast Uncertainty Estimates for Black-Box Language Models

**Authors:** Kevin David Hayes, Arka Pal, Haosong Zhang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24881v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24881v1)

**Summary:** In high-stakes decision-making applications of large language models (LLMs), practitioners require not only accurate LLMs but also uncertainty estimates for their predictions. Existing approaches to uncertainty estimation for LLMs require access to log-probabilities output by the model or require fine-tuning access. However, many industrial LLM products use closed-source API models, and many such API models like GPT do not return log-probabilities and may not allow fine-tuning. We introduce Pino...

---

### 18. Partner-Specific Affective Precision in Social Active Inference

**Authors:** Harshil Shah, Andrew Pashea

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24876v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24876v1)

**Summary:** In multi-agent social settings, model reliability varies across relationships. Beyond inferring what others will do, an agent must calibrate how confidently those inferences should guide policy selection for each relationship. An agent may maintain a well-validated model of one partner, a fragile model of another, and a model under revision for a third; collapsing these into a single confidence estimate loses information relevant to policy selection. We therefore formalize affective precision as...

---

### 19. SE(3) Neural Potential Fields for 6-DoF Trajectory Planning Directly from Images Without Explicit 3D Reconstruction

**Authors:** Jeffrey Eiyike, Masoud Ataei, Elvis Gyaase, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24864v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24864v1)

**Summary:** Reaching a 6-DoF grasp pose in clutter requires a collision-free trajectory, conventionally obtained by reconstructing the scene in 3D and planning inside that reconstruction, at the cost of its accuracy and compute. Potential fields learned directly from images remove that dependency but inherit the classical weakness of artificial potential fields: where attractive and repulsive gradients cancel, the descent grazes the obstacle instead of going around it, and can stall short of the goal. We pr...

---

### 20. When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting

**Authors:** Yifan Hu, Xilin Dai, Zhiyuan Qu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24862v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24862v1)

**Summary:** Agentic time series forecasting concerns systems whose underlying mechanisms evolve, making the relative effectiveness of numerical models, reasoning strategies, and intervention rules inherently time-varying. Consequently, a time series agent must adapt the forecasts it produces and the orchestration policy that determines which components to trust and how to coordinate them. The deployment process naturally provides supervision for this adaptation as forecast horizons elapse and realized targe...

---

### 21. Small-world Networks of Agents Brainstorm AI Risks to Support Ideation

**Authors:** Ke Zhou, Edyta Bogucka, Daniele Quercia

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24859v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24859v1)

**Summary:** The ideation phase of participatory AI risk assessment often starts with a blank slate or a limited list of predefined risks, making it difficult to surface indirect or systemic harms. To address this limitation, we propose a three-stage ideation support tool. The tool complements participatory AI, rather than replacing it, and helps focus later engagement with affected communities. First, it dynamically discovers stakeholders depending on the given AI use and recursively expanding outward, allo...

---

### 22. Extracting Arguments, Not Just Classifying Them: Instruction-Tuned LLMs for Generative Component Detection

**Authors:** Sofiane Elguendouze, Erwan Hain, Elena Cabrio, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24855v1)

**Summary:** Argumentative component detection (ACD) is a core subtask of Argument(ation) Mining (AM) and one of its most challenging aspects, as it requires jointly delimiting argumentative spans and classifying them into components such as claims and premises. While research on this subtask remains relatively limited compared to other AM tasks, most existing approaches formulate it as a simplified sequence labeling problem, component classification, or a pipeline of component segmentation followed by class...

---

### 23. SPECTRA: Adaptive Execution of Speculative Decoding on a Runtime-Reconfigurable Tiled Architecture

**Authors:** Gabriele Tombesi, William Baisi, Je Yang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24847v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24847v1)

**Summary:** LLM inference on edge devices is constrained by computational and memory resources, making efficient autoregressive decoding challenging. Speculative decoding alleviates this bottleneck by generating tokens with a smaller draft model and verifying multiple tokens in parallel with a batched target model pass. However, verification introduces a runtime-dependent intermediate regime between memory-bound general matrix-vector (GEMV) operations in decoding and compute-bound general matrix-matrix (GEM...

---

### 24. MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution

**Authors:** Junde Wu, Jiayuan Zhu, Minghao Hu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24838v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24838v1)

**Summary:** Medical agents increasingly combine general reasoning models with specialized clinical tools, yet their capabilities remain largely fixed by what clinicians and engineers design before deployment. Recursive self-improvement (RSI) offers a different paradigm in which agents learn from their own failures and autonomously expand their capabilities, but directly applying RSI to medicine introduces fundamental safety challenges. We introduce MedRSI, the first recursive self-improvement framework for ...

---

### 25. GRUET: Quantifying Uncertainty of Agentic Reasoning-and-Acting Processes

**Authors:** Shuang Liang, Xin-Yu Hu, Shao-Qun Zhang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24831v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24831v1)

**Summary:** Agents have attracted considerably increasing attention due to the power of executing both Reasoning and Acting (ReAct) in open and dynamic environments. The ReAct process typically exhibits a multi-turn trajectory in which one drives Large Language Models (LLMs) to generate both reasoning chains and task-specific actions in an interleaved manner. However, agents often suffer from significant uncertainty, where identical tasks yield divergent trajectories; trajectories with higher uncertainty of...

---

### 26. Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI

**Authors:** Wenkang Qin, Yukun Zhou, Noah Shen, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24815v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24815v1)

**Summary:** Scalable simulation is essential for robot data generation, policy training, evaluation, and safe iteration, yet real-world interaction is costly and conventional simulators require labor-intensive construction. We present Uranus, a data-driven robot simulator built around a joint-trajectory-conditioned autoregressive diffusion model. Uranus offers three key capabilities: (1) streaming, open-ended rollout, which receives future joint-position trajectories online and autoregressively generates on...

---

### 27. Mobile Imaging Solutions for Medical Diagnosis: Trends and Applications

**Authors:** Syed Muhammad Ibne Zulfiker, Tanzima Hashem, Fariha Tabassum Islam, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24814v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24814v1)

**Summary:** Advances in processing power, camera technologies, and mobile image analysis have made smartphones and other mobile devices, such as laptops, increasingly suitable for medical diagnosis and healthcare applications. Researchers have developed low-cost solutions for the early detection and monitoring of various health conditions, including eye and ENT diseases, malnutrition, heart rate variability, skin and oral conditions, and injuries, using images captured by non-medical devices such as smartph...

---

### 28. Decoding Guardrails: XAI-Guided Perturbation Analysis of Prompt Injection Detection

**Authors:** Fernando Outeda, Gustavo Betarte, Juan Diego Campo, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24801v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24801v1)

**Summary:** Large language models (LLMs) are increasingly deployed in production systems, raising concerns about their exposure to adversarial manipulation through prompt injection and jailbreak attacks. Classifier-based guardrails, such as Prompt Guard 2, are widely used as a first line of defense against such attacks, but their internal decision logic is largely opaque to both defenders and attackers. This paper presents an exploratory case study that applies explainable artificial intelligence (XAI) tech...

---

### 29. When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs

**Authors:** Yeji Kim, Mi-Young Kim, Randy Goebel

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24799v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24799v1)

**Summary:** Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy. But in explanation-critical domains, preserving only the final answer may be insufficient, since users may also inspect generated rationales to judge whether a prediction is trustworthy. We study this issue in medical multiple-choice question answering, where rationales should provide evidence that...

---

### 30. Convex AI Compositionality and the Governance of AI System Populations

**Authors:** Andrea Ferrario

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24784v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24784v1)

**Summary:** AI governance increasingly requires providers and public authorities to reason about multiple AI instantiations, alternative versions, and deployment configurations of multiple AI systems. Yet current regulation remains predominantly single-system-centric, acknowledging such multiplicity only sparsely without treating collections of related AI systems as governance objects. This creates an AI population governance problem: determining which instantiations can be meaningfully considered together ...

---

### 31. PrismGPT: Proxy-Guided Learning for Region-Aware Photo Editing with Self-Synthesized Reasoning

**Authors:** Ke Zhao, Hue Nguyen, Abhijith Punnappurath, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24768v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24768v1)

**Summary:** Professional photo finishing relies on both global adjustments and region-specific local edits guided by semantic masks, yet current automated methods handle this workflow only partially. We present PrismGPT, a Vision-Language Model (VLM) framework that produces structured, region-aware editing plans from a single input image without relying on commercial black-box tools. Training a VLM to simultaneously diagnose aesthetic deficiencies at both global and local levels while predicting precise edi...

---

### 32. Construting Reverse Thinking: Developing Large Language Models' Reverse Thingking Ability

**Authors:** Xin Liu, Yunhai Li, Chunfu Jia, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24760v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24760v1)

**Summary:** When facing complex problems, humans tend to try various ideas for different issues. Human thinking patterns exhibit remarkable flexibility in adapting to diverse scenarios. GPT-o1, GPT-o3, and DeepSeek-R1 adopt long chain-of-thought models to address complex problems by increasing reasoning depth, which default to a forward reasoning mode. We conducted statistical analysis on the accuracy of different mathematical problem datasets on models of different scales, and found five reasons for errors...

---

### 33. NPU Accelerator: Quantized Real-Time Vehicle Detection on PYNQ-Z1 Using FINN

**Authors:** Daniel Gutierrez, Antonio Cuesta, Jorge Fe, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24757v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24757v1)

**Summary:** This paper presents the design, optimization, implementation, and on-board validation of a neural processing unit (NPU) accelerator for real-time vehicle detection on the resource-constrained Xilinx Zynq XC7Z020 device of the PYNQ-Z1 board. The work follows a hardware/software co-design methodology that combines quantization-aware training (QAT), lightweight YOLO-derived detectors, Brevitas/QONNX model export, FINN dataflow compilation, Vivado implementation, and physical benchmarking on the tar...

---

### 34. Epi-Logic: A Conceptual Framework for Epistemic Runtime Control, Schema Validity Checking, and Controlled Accommodation in Autonomous AI Agents

**Authors:** Boris Wetzk

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24755v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24755v1)

**Summary:** Autonomous AI agents are increasingly deployed in areas where wrong decisions are hard to reverse. This paper examines schema mismatch: the condition in which an agent operates within an interpretive frame that no longer applies to the current context. Outputs produced under such a mismatch can appear internally consistent, linguistically plausible, and largely factually correct; output-quality metrics alone therefore capture the underlying loss of validity only partially.   The paper introduces...

---

### 35. Enhancing Transformer Representations of Symbolic ODE Expressions

**Authors:** Xiyue Fan, Adam Prugel-Bennett, Stuart E. Middleton

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24746v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24746v1)

**Summary:** Existing approaches to solving differential equations, such as symbolic regression, physics informed neural networks, and neural operators, typically focus on numerical approximations or blind symbolic search via fitting to numerical data. Less attention has been paid to learning structured representations of mathematical expressions that preserve commutative properties and could support mathematical reasoning in symbolic forms. Transformer models have shown strong capabilities in solving symbol...

---

### 36. World State Generator

**Authors:** Sungheon Jeong, Sanggeon Yun, Ryozo Masukawa, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24744v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24744v1)

**Summary:** Language agents solve complex tasks through plans and actions. A single step the world refuses puts the goal out of reach, and what the agent does next decides the task. Prompted planners fail at exactly this point, rewriting the refused step in new words, meeting the same refusal, and burning the attempt budget without moving. They fail because the plan was never tied to the world, so a refusal has nothing in the plan to attach to. A world is where a task runs, and it has its own rules, its own...

---

### 37. LLM-based Conversational AI Knowledge Assistant for MyBuddy Humanoid Robot

**Authors:** Hanxiao Chen

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24742v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24742v1)

**Summary:** Humanoid robots are increasingly being popular and developed for human-centered applications, yet their ability to provide intelligent conversations and natural interactive knowledge assistance remains constrained by traditional rule-based dialogue systems, pre-defined responses and limited knowledge repositories. Large language models (LLMs) have emerged as a powerful foundation for enabling natural, adaptive, and context-aware Human-Robot Interaction (HRI), which provides a significant opportu...

---

### 38. A digital-twin framework for forecasting treatment-day imaging with contour uncertainty in adaptive proton radiotherapy

**Authors:** Yizhou Wu, Jie Ding, Justin Roper, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24725v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24725v1)

**Summary:** Head-and-neck anatomy changes over a six-to-seven-week proton course, and the anatomy of a later week cannot be imaged when the plan is made. We present a digital-twin framework that forecasts a patient's treatment-day anatomy as an ensemble of predicted CTs with propagated contours and quantifies the uncertainty of the forecast contours. The twin is a library of previously treated patients with planning and weekly quality-assurance CTs (QACTs), made patient-specific by a two-step foundation-mod...

---

### 39. Reasoning Topology Matters: A Controlled Study of LLM-Based Cybersecurity Analysis

**Authors:** Jiling Zhou, Aisvarya Adeseye, Antti Hakkala, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24710v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24710v1)

**Summary:** Large Language Models (LLMs) are increasingly used in cybersecurity, where accurate analysis often requires multi-step and context-dependent reasoning over complex and heterogeneous data. However, existing prompting approaches typically focus on eliciting reasoning without explicitly considering how intermediate reasoning steps are structurally organized. We introduce Security Reasoning Topology, which models reasoning through three representative structures: Linear, Branching, and Graph. To eva...

---

### 40. "MeBo Leaves a Piece of You Behind": Designing a Relational Voice-Based Memory Companion for Older Adults

**Authors:** Hasibur Rahman, Mahsa Nasri, Manasi Vaidya, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24706v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24706v1)

**Summary:** Autobiographical remembering supports identity, well-being, and social connection in later life, yet voice-based memory technologies largely rely on isolated prompts. We designed and built MeBo, a fully functional relational voice-based memory companion, through participatory design with 11 older adults. Their accounts shaped four Design Strategies that guided MeBo's interaction design and multi-agent implementation. In a mixed-methods evaluation with 20 older adults, participants found MeBo exc...

---

### 41. Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient Inference

**Authors:** Changxu Liu, Zhaogeng Li

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24698v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24698v1)

**Summary:** Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency. Unlike linear speculation, which follows a single candidate chain, tree-structured speculation retains multiple branches from shared prefixes; under the same budget, this broader coverage can improve acceptance and efficiency. Adapting it to DeepSeek-V4 is nontrivial: its CSA/HCA online compressed attention concentrates the difficulty on the target-verify side, where branches divergi...

---

### 42. What Makes a Good Medical Image Tokenizer? Rethinking Reconstruction and Generation in Medical Image Tokenization

**Authors:** Niklas Bubeck, Yundi Zhang, Vasiliki Sideri-Lampretsa, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24691v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24691v1)

**Summary:** Latent diffusion models now dominate medical image generation, and every such pipeline rests on a \emph{tokenizer} that compresses images into the latent codes for image generation to operate on. Thereby, the tokenizer choice bounds every downstream task from reconstruction fidelity and generation quality to the representations available for downstream analysis. Yet, medical imaging pipelines routinely utilize tokenizers from natural imaging on the hypothesis that their behavior carries over. Ho...

---

### 43. Understanding Hyperspherical Geometry of ECAPA-TDNN Embedding and Its Impact on Zero-Shot Voice Conversion

**Authors:** Mathilde Abrassart, Nicolas Obin, Axel Roebel

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24688v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24688v1)

**Summary:** Angular-margin speaker encoders are widely used in voice conversion, yet the geometry of their classifier prototypes remains poorly understood. We analyze ECAPA-TDNN classifier prototypes as points on the unit hypersphere and characterize their organization using rotation-invariant angular statistics together with global and local effective dimensionality measures. Our analysis shows that standard training can induce angular concentration and a substantial reduction in effective dimensionality. ...

---

### 44. TimeLitmus: A Diagnostic Benchmark for Cross-Modal Understanding and Explanation Faithfulness in Event-Conditioned Time-Series Prediction

**Authors:** Jie Gong, Maowei Jiang, Zhiwei Liu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24677v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24677v1)

**Summary:** Large language models (LLMs) are increasingly used to make predictions from numerical time-series histories and textual events. Yet accuracy alone cannot reveal whether correct answers reflect effective integration of the two inputs or instead arise from event polarity, unimodal priors, or superficial cues. Likewise, plausible explanations may rationalize predictions without faithfully reflecting the evidence that drives model behavior. We introduce TimeLitmus, a diagnostic benchmark for cross-m...

---

### 45. Trust in Edge-Enabled IoT Security: Features, Challenges and Research Directions

**Authors:** Esin Ece Aydın, Şerif Bahtiyar, Gürkan Gür

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24669v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24669v1)

**Summary:** Providing autonomous intelligence, pervasive connectivity and usability to human life and industry has led to the emergence of the Internet of Things (IoT). To support time-sensitive and resource-constrained applications, IoT systems nowadays increasingly rely on edge computing. This brings computation and decision-making closer to end devices. In edge-enabled IoT architecture, latency and communication overhead are reduced, but interactions among a larger and more diverse set of devices, edge n...

---

### 46. Beyond Endpoint Performance: Process-Level Evaluation of Self-Evolving Agents

**Authors:** Hongqiang Lin, Chao Liu, Xiaofan Bai, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24663v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24663v1)

**Summary:** Self-evolving agents convert interaction feedback into persistent artifacts, such as memories or skills, which in turn guide subsequent decisions. As these artifacts are iteratively updated throughout an experience stream, the capabilities they support may evolve. Consequently, endpoint performance alone offers an incomplete view of self-evolution. Process-level evaluation is therefore essential to identify when a target capability emerges and whether later updates strengthen, preserve, or weake...

---

### 47. DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security

**Authors:** Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24662v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24662v1)

**Summary:** LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation protocol for measuring agent security under \emph{dual-control} interaction, where both the agent and the user can influence the shared environment state. DUMA-Bench extends $τ^2$-bench ~...

---

### 48. Touch2Robot: Robot Touch in the Human Demonstration Loop

**Authors:** Shengcheng Luo, Xiaoyang Cheng, Hong Ying, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24660v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24660v1)

**Summary:** Human demonstrations offer a scalable way to collect manipulation data, but their contacts may be unstable or infeasible when transferred to a robot hand. Collecting demonstrations directly on the target robot avoids this mismatch, but substantially increases the cost of data collection. To address this trade-off, we present \textbf{Touch2Robot}, a framework that lets humans collect demonstrations while seeing how the target robot hand would contact the object. We capture human hand motion, tact...

---

### 49. Corrective Forcing: Unified Post-Training for Diffusions and Flows in Generative Speech Enhancement

**Authors:** Qing Yao, Lijian Gao, Qirong Mao

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24651v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24651v1)

**Summary:** Diffusion and flow models, as promising generative paradigms for speech enhancement, face a training--inference mismatch: training uses analytical path states, whereas inference recursively evaluates models on self-generated rollout states along discretized sampling trajectories. This mismatch causes prediction and discretization errors to accumulate. To address it, we introduce Corrective Forcing (CoF), a post-training paradigm that forces diffusion and flow models to learn from self-generated ...

---

### 50. iSDFT: Information-Proximal Self-Distillation for Continual Learning in LLMs

**Authors:** Ahmed Khaled Khamis, Xiaotong Ji, Hassan Jaber, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24646v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24646v1)

**Summary:** On-policy self-distillation fine-tuning (SDFT) learns new skills from demonstrations while reducing forgetting, but it always distils toward the full demonstration-conditioned teacher. This fixes teacher influence at the full-teacher endpoint, providing no control over how much demonstration information should be transferred at each prediction state. We introduce Information-Proximal SDFT (iSDFT), which instead treats the teacher as a budgeted source of information. At each token, iSDFT selects ...

---

## cs.CL

**50 papers**

### 1. Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use

**Authors:** Zixiang Chen, Wenting Zhao, Zhepeng Cen, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24985v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24985v1)

**Summary:** Multi-turn tool-use failures can hinge on a single model call, yet reward variation alone does not reveal which call would benefit from training. When rewards depend on later interactions, their variation can reflect downstream randomness rather than differences between the current actions. We introduce Critical-State RL to identify trainable states in multi-turn interactions. Given task-defined candidate calls and local rewards, the method assesses whether each reward captures the action's effe...

---

### 2. onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction

**Authors:** Lei Yang, Mengyin Liu, Jia Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24983v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24983v1)

**Summary:** We present onPanda, an interactive tool for efficiently annotating LLM alignment data and agent trajectories. onPanda adopts token-level correction as its core interaction: while reading a model response, the annotator locates the first inappropriate token and either picks a substitute from the model's candidate tokens or types the correct text via free-form editing. The system then truncates everything after that position and continues generation from the corrected prefix, repeating this locate...

---

### 3. Harness-Zero: Harness Distillation via Agent-as-Harness

**Authors:** Haoran Ye, Yuxing Lu, Haonan Dong, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24974v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24974v1)

**Summary:** Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent must either settle for a suboptimal shared harness or route among an ever-growing set of specialized ones. We therefore study agent harness distillation: using a domain- or instance-optimized harness as training-time gui...

---

### 4. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

**Authors:** Peng Xia, Rujun Han, Zifeng Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24972v1)

**Summary:** An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-d...

---

### 5. DolphinBench: Mapping the Pareto Frontier of Agent Memory

**Authors:** Soumil Rathi, Deshraj Yadav, Taranjeet Singh

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24971v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24971v1)

**Summary:** Agents today often take real-world actions that depend on long-term memory and context recall over time. However, most current memory benchmarks are built for a conversational question-answer format, where the question itself signals that some fact must be retrieved, and often which one. Moreover, benchmarks rarely require anything beyond accuracy from submissions, allowing memory systems to make unreasonable cost/time tradeoffs to achieve higher scores.   We present DolphinBench, a benchmark th...

---

### 6. Emergent Collusion in Long-Horizon LLM Agent Interaction

**Authors:** Xinrui Shi, Yanzhe Zhang, Diyi Yang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24967v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24967v1)

**Summary:** LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from th...

---

### 7. Jev for Scientific Decisions: Evaluating Semantic Choices and Their Consequences

**Authors:** Boyuan Deng, Shuyi Fan, Hongyang Zhang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24965v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24965v1)

**Summary:** Scientific workflows often require choosing among known relations before a deterministic calculation can proceed. Whether observations share a culture, treatment or reference standard can change the scientific meaning of the resulting count or comparison. We evaluate Jev as a semantic decision component using a harness that follows its documented guidance and assigns arithmetic to code. The study compares twelve model configurations on twenty source-grounded Choices across ten scientific cases, ...

---

### 8. Linguistic Features for Interpretable Textual Entailment

**Authors:** David Torres-Moreno, Jorge Hermosillo-Valadez, Asela Reig-Alamillo

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24932v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24932v1)

**Summary:** Despite the success of neural models in natural language processing, their black-box nature limits interpretability and conceals the linguistic phenomena underlying their predictions. We present SLITE, an explainable hybrid model for Recognizing Textual Entailment that integrates two complementary layers of semantic analysis: a structural-relational layer, based on semantic compatibility and incompatibility between compositional entities, and a distributional-informational layer, based on struct...

---

### 9. SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI Co-evolutionary Paradigm

**Authors:** Xinnong Zhang, Jiayu Lin, Jia Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24911v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24911v1)

**Summary:** Social simulation offers the social sciences an experimental instrument that the real world cannot supply, and generative agents have transformed it by acting as silicon samples that unite agent-based modeling with real behavioral data. Existing platforms verify collective behavior, align simulated populations with real societies in cross-sections, and employ autonomous agents for the research process. However, two social science requirements remain without systematic support: intervention in th...

---

### 10. ToneCL: Contrastive Learning for Few-Shot Syllable-Level Tone Classification

**Authors:** Qisheng Liao, Youngah Do

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24903v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24903v1)

**Summary:** Tone languages constitute over 50-70% of the world's languages, but the vast majority are low-resource, lacking the large transcribed corpora needed for automatic tone classification. Existing datasets are typically collected at the sentence level, whereas field linguists require fine-grained syllable-level annotations. We propose ToneCL, a lightweight contrastive learning framework for few-shot syllable-level tone classification. We simulate low-resource conditions on Mandarin and Vietnamese, l...

---

### 11. Human-LLM Deliberation as Interactive Proof: Conditions for Verifiability Without Transparency

**Authors:** Baotong Zhang, Dean Foster, João Sedoc

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24895v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24895v1)

**Summary:** When an LLM supplies an argument that a user could not readily construct, how can the user decide whether to accept its claim? Inspired by interactive proofs, we model human-LLM deliberation as an interaction between a prover with unrestricted internal search and a resource-bounded human verifier. The verifier requests and checks supporting details without access to the LLM's internal state. Passed checks accumulate evidence toward an acceptance threshold. We prove anytime-valid soundness agains...

---

### 12. SLICEChat: Progressive In-Encoder Token Pruning for Whole-Slide Pathology Language Models

**Authors:** Ali Kerem Bozkurt, Baris Cem Bakay, Ibrahim Kulac, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24894v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24894v1)

**Summary:** Whole-slide pathology images (WSIs) contain gigapixel-scale visual content, creating a major scalability challenge for slide-level multimodal large language models (MLLMs). Existing approaches process thousands of patch tokens and typically apply compression only after slide encoding, leaving multimodal attention computationally expensive. We introduce SLICEChat, a slide-level MLLM that integrates progressive token pruning within a hybrid Mamba--Transformer slide encoder. Mamba layers enable eff...

---

### 13. OSWorld-Pro: Process-based Evaluation for Computer Use Agents

**Authors:** Zhilin Wang, Shaokun Zhang, Yifan Zhang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24890v1)

**Summary:** Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely prov...

---

### 14. The Copy Ceiling: An Input-Exposure Control for Ontology-Grounded Generation over Curated Corpora

**Authors:** John J. O'Hare

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24885v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24885v1)

**Summary:** When a language model answers from a curated corpus via graph-based retrieval, a large grounding uplift does not establish reasoning over the retrieved structure: the context may already expose the gold answers. We propose exposure accounting, which classifies each gold item by whether the shown context exposes it and whether the answer recovers it. Its scalar reference is the copy ceiling, the recall a verbatim copy of the context achieves; signed gain over copy measures the model's recall rela...

---

### 15. Decomposing Error and Style in Automated Clinical Coding

**Authors:** Han-Chin Shing, Jack Moriarty, Ryan Ware, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24877v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24877v1)

**Summary:** In automated clinical coding, where the label space spans tens of thousands of diagnosis and procedure codes, models are currently evaluated against a single gold annotation, treating any deviation as error. But we find when two teams code the same 110 ACI-Bench encounters, they agree on only 73% of codes (Jaccard similarity) for the same note; even after an independent clinical audit removes erroneous codes, agreement rises only to 77%. Is that gap error or something systematic? We model the sy...

---

### 16. Extracting Arguments, Not Just Classifying Them: Instruction-Tuned LLMs for Generative Component Detection

**Authors:** Sofiane Elguendouze, Erwan Hain, Elena Cabrio, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24855v1)

**Summary:** Argumentative component detection (ACD) is a core subtask of Argument(ation) Mining (AM) and one of its most challenging aspects, as it requires jointly delimiting argumentative spans and classifying them into components such as claims and premises. While research on this subtask remains relatively limited compared to other AM tasks, most existing approaches formulate it as a simplified sequence labeling problem, component classification, or a pipeline of component segmentation followed by class...

---

### 17. The Answer-Basin Representation Hypothesis: We Are Not Probing or Steering Concepts

**Authors:** Manjiang Yu, Hongji Li, Zihan Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24821v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24821v1)

**Summary:** The Linear Representation Hypothesis associates high-level concepts with directions in language models, but it remains unclear how these concept-related linear structures are organized within the model. We propose the Answer-Basin Representation Hypothesis: the probability measure induced over answers by the model's continuation distribution organizes these linear structures, with its statistics represented along linear directions shared across questions. All continuations yielding the same answ...

---

### 18. MSI-Bench: Evaluating Multi-Speaker Voice Interaction for Collaborative AI Agents

**Authors:** Chenxu Xiong, Dongming Shen, Yuzhi Tang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24812v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24812v1)

**Summary:** Voice provides a natural and immediate interface for AI agents. Many settings in which voice agents could be useful, including meetings, households, and collaborative work, are inherently multi-speaker. Supporting these settings introduces challenges that are largely absent from one-on-one interaction. We introduce the Multi-Speaker Interaction Benchmark (MSI-Bench) for evaluating multi-speaker voice interaction. Each test case is a short multi-party multi-turn audio scene with participant conte...

---

### 19. When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs

**Authors:** Yeji Kim, Mi-Young Kim, Randy Goebel

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24799v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24799v1)

**Summary:** Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy. But in explanation-critical domains, preserving only the final answer may be insufficient, since users may also inspect generated rationales to judge whether a prediction is trustworthy. We study this issue in medical multiple-choice question answering, where rationales should provide evidence that...

---

### 20. Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient Inference

**Authors:** Changxu Liu, Zhaogeng Li

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24698v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24698v1)

**Summary:** Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency. Unlike linear speculation, which follows a single candidate chain, tree-structured speculation retains multiple branches from shared prefixes; under the same budget, this broader coverage can improve acceptance and efficiency. Adapting it to DeepSeek-V4 is nontrivial: its CSA/HCA online compressed attention concentrates the difficulty on the target-verify side, where branches divergi...

---

### 21. Muon Can Outperform Dedicated Continual Learning Methods

**Authors:** Sebastian George Sincari, Bogdan Alexandru Gheorghe, Antonio Barbalau

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24678v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24678v1)

**Summary:** Continual learning with Low-Rank Adapters (LoRA) typically mitigates forgetting by penalizing the overlap between a new update and the accumulated past weights, which discourages certain update directions without controlling how an update distributes its energy over the ones that remain. We ask whether that restriction has to be task-aware, or whether a generic one supplied by the optimizer is enough. We train a plain incremental LoRA (IncLoRA) with Muon, which orthogonalizes each update, and co...

---

### 22. Circuit Hypernetworks for Quantum-Augmented Diffusion Language Models

**Authors:** Xiaoqiang Wang, Mengyang Xiong, Jun Dai, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24657v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24657v1)

**Summary:** Language models can be adapted by changing the computations applied to individual tokens. Quantum circuits offer one such approach, but evaluating wider circuits inside a large model can be computationally demanding. Here we introduce HyperQ, which adds token-conditioned quantum residual branches to a frozen masked-diffusion language model. A quantum residual branch is a module in each transformer block that reads a token's hidden state, emits the coordinates of that token's circuit, executes it...

---

### 23. Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting

**Authors:** Raphaël Thieffry, Matej Martinc

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24650v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24650v1)

**Summary:** Readability assessment is essential for tailoring texts to intended audiences across educational, healthcare, and information retrieval domains. However, traditional readability formulas struggle to generalize across genres and languages, while supervised machine learning models rely on scarce, domain-specific annotated corpora, limiting their applicability--particularly for less-resourced languages. Large Language Models (LLMs) offer a highly scalable, multilingual alternative that requires no ...

---

### 24. Written as a Record, Read as an Address: What a Forward Pass Leaves in an Operation's KV Cache

**Authors:** Lingfeng Wu, Behzad Shomali

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24635v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24635v1)

**Summary:** When a language model reads an operation such as "Swap the contents of Box F and Box B", its forward pass writes keys and values for those tokens into the KV cache. Prior work on entity tracking establishes what models use: bindings are resolved at query time rather than stored as explicit latent state. We ask what they write at the operation span and how it is accessed. We split a forward pass into a frozen writer and a reader: the writer's cache is recomputed without gradients, while the reade...

---

### 25. Custom Named Entity Recognition and Topic Classification for Global Health Publications

**Authors:** Genis Skura, Antoine Geissbühler, Jean-Luc Falcone

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24625v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24625v1)

**Summary:** How should natural language processing models be selected and adapted for global health literature in environments where annotated data and computational resources are limited? This thesis investigates these challenges through experiments on semantic tag discovery, named entity recognition (NER), and multi-label topic classification. First, skip-gram word2vec models trained on progressively larger specialized corpora are compared with BioWordVec to assess how corpus size and domain context influ...

---

### 26. UK-PRBENCH: A Paragraph-Level Precedent Retrieval Benchmark for United Kingdom Case Law

**Authors:** Damith Premasiri, Tharindu Ranasinghe

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24613v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24613v1)

**Summary:** Prior case retrieval (PCR) aims to identify precedent cases relevant to a given query case. Existing PCR benchmarks and methods predominantly operate at the document level, treating entire judgments as the unit of relevance. This formulation is suboptimal for legal practitioners, as judgments address multiple legal issues and only a small subset of paragraphs is relevant to a particular query. Addressing this gap, we introduce UK-PRBench, a benchmark for paragraph-level precedent retrieval in UK...

---

### 27. Evaluating Decision Models for Text Annotation in Computational Social Science

**Authors:** Hazem Ibrahim, Yasir Zaki

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24574v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24574v1)

**Summary:** Computational social science increasingly relies on large language models for text annotation, and the validity of published findings now rests on the labels generated by such models. Decision models, a new model class built for categorical question answering, answer typed questions with a choice, a probability distribution over the label set, and a confidence score rather than free text, at a small fraction of frontier inference prices. Whether their answers are accurate, and whether that state...

---

### 28. Toward a Unified Mathematics of Concepts

**Authors:** Chen Shani

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24554v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24554v1)

**Summary:** Concepts are commonly defined as abstract, compact representations of knowledge and treated as basic units of intelligent behavior. Yet, cognition, psychology, and AI lack a shared mathematical language for them. Modern systems represent concepts as vectors, distributions, symbols, graphs, and other structures, but these formalisms are typically treated as competing rather than as solutions to a common problem. We propose an operation-based view that evaluates mathematical frameworks by the conc...

---

### 29. QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation

**Authors:** Demian Pavlyshenko, Bohdan Pavlyshenko

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24538v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24538v1)

**Summary:** Functional annotation of newly sequenced proteins remains a bottleneck in molecular biology: the number of sequences in public repositories grows far faster than the capacity for manual curation. Most computational approaches consider annotation as multi-label classification over a fixed ontology, which constrains predictions to a predefined label set. In this work we study the the protein annotation as a sequence-to-text generation problem. We fine-tune the 3B-parameter Ministral 3 base model w...

---

### 30. LLJ Cards: Best practices for the Use of LLMs as Judges

**Authors:** Khaoula Chehbouni, Melina Medjdoub, Florian Carichon, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24516v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24516v1)

**Summary:** In recent years, large language models (LLMs) have emerged as a popular alternative for evaluation. Often referred to as LLMs as judges (LLJs), these systems have been widely adopted by researchers and practitioners across a broad range of measurement tasks, driven by their strong performance, scalability, and cost-effectiveness relative to human judgment. However, a growing body of work has shown that the use of LLJs raise concerns about their validity and reliability as evaluators. Existing ef...

---

### 31. Fathom-Vaidya: Advancing Medical Reasoning with Rubric-Based Rewards

**Authors:** Kalash Shah, Kunal Singh, Snehan J, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24480v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24480v1)

**Summary:** Deploying Large Language Models (LLMs) in healthcare requires robust performance across two complementary dimensions - diagnostic reasoning: the convergent, evidence-driven task of inferring a patient's condition from clinical data to produce a diagnosis, and clinical healthcare reasoning: the broader, navigational judgment required to communicate, plan, and adapt across multi-turn clinical interactions where a single correct answer may not exist. Recent benchmarks such as HealthBench and MedXpe...

---

### 32. 1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation

**Authors:** Huanxin Sheng, Zhiling Ye, Haonan Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24432v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24432v1)

**Summary:** Sparse on-policy distillation (OPD) allocates teacher supervision to a small subset of tokens in student-generated trajectories. However, useful teacher guidance can yield a noisy update when its gradient is estimated from a sampled next token. We study this estimation problem at a fixed prefix in information geometry and propose an information-efficiency ratio (IER) based on a signal-to-noise decomposition. IER characterizes relative gradient estimation error under an optimal scalar baseline. A...

---

### 33. End-to-end Jordanian dialect speech-to-text self-supervised learning framework

**Authors:** Ali A. Safieh, Ibrahim Abu Alhaol, Rawan Ghnemat

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24410v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24410v1)

**Summary:** Speech-to-text engines are extremely needed nowadays for different applications, representing an essential enabler in human-robot interaction. Still, some languages suffer from the lack of labeled speech data, especially in the Arabic dialects or any low-resource languages. The need for a self-supervised training process and self-training using noisy training is proven to be one of the up-and-coming feasible solutions. This article proposes an end-to-end, transformers-based model with a framewor...

---

### 34. URA-NER: A Unified Retrieval-Augmented Framework with Retrieval Alignment and Uncertainty Reduction for Low-Resource NER

**Authors:** Jingyu Wang, Shijie Wu, Fusheng Jin

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24372v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24372v1)

**Summary:** In-context learning (ICL) based on large language models (LLMs) has shown promising potential in alleviating performance bottlenecks caused by the limited availability of annotated data in Named Entity Recognition (NER). However, existing methods still face issues of retrieval misalignment and generation uncertainty, making their performance heavily dependent on the LLM's capabilities. As the parameter scale of LLMs decreases, their performance in few-shot settings deteriorates significantly. In...

---

### 35. Mitigating Entity Type Confusion in Cross-Domain NER via Multidimensional Quantification and Reasoning Enhancement

**Authors:** Jingyu Wang, Shijie Wu, Fusheng Jin

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24357v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24357v1)

**Summary:** Cross-domain Named Entity Recognition (CD-NER) aims to transfer the rich knowledge in the source domain to the target domain. Recent studies adopting decomposition or generation paradigms have achieved significant performance improvements, demonstrating high accuracy in entity span detection. However, during entity type classification, models severely suffer from entity type confusion, the erroneous tendency that models classify entities of one type in the text as another similar but incorrect t...

---

### 36. Morpho-VITS: Variational Inference with Morphological Modeling for End-to-End Speech Synthesis of a Tonal Bantu Language

**Authors:** Antoine Nzeyimana

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24310v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24310v1)

**Summary:** Text-to-speech models for Bantu tonal languages are challenged by a tonal system that is rooted in both the lexis (i.e., the inventory of words, stems, and affixes) and the grammar (i.e., morpho-syntax). To complicate matters, the standard writing systems of these languages often omit tone markings and syllable duration information, which must be disambiguated by the reader based on context. Motivated by linguistic descriptions of Bantu language tone systems, we propose an end-to-end text-to-spe...

---

### 37. SupportCal: Label-Free Calibration of Post-Trained LLMs via Reference Support and Corroboration

**Authors:** Linhan Luo, Lequan Lin, Dai Shi, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24303v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24303v1)

**Summary:** Post-training often improves task performance but can degrade confidence calibration, leaving post-trained language models (PoLMs) more overconfident than their corresponding pretrained language models (PLMs). Because task-specific labeled calibration data can be costly or unavailable, the corresponding pretrained PLM provides a natural label-free reference for post-hoc calibration. Prior agreement-gated PLM-referenced calibration fits a scalar temperature using only examples on which the PoLM a...

---

### 38. Structure Before Sampling: Community-Aware Core-Set Selection for Data-Efficient Text-to-Speech

**Authors:** Mizbaul Haque Maruf, Muhammad Nur Yanhaona

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24275v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24275v1)

**Summary:** Text-to-speech (TTS) corpora are costly to record, yet many utterances add little new phonetic information. Core-set selection reduces this cost by choosing a small training subset under a fixed audio-duration budget. We represent a corpus as a phonotactic graph that links each utterance to its most phonemically similar ones, and we first test whether this graph has structure. In Bangla and English corpora, its clustering is 199 and 56 times that of a size-matched random graph, and its modularit...

---

### 39. Canonical Procedural Actions: An Auditable Annotation Protocol for Tool-Use Agent Traces

**Authors:** Songqi Li, Dongqing Li, Zheqiao Cheng

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24264v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24264v1)

**Summary:** Tool-use agent traces identify messages and API calls, but procedural analyses also need explicit units of action and inspectable links to their evidence. We present Canonical Procedural Actions (CPAs), an annotation protocol that records a procedural function, its first agent-event anchor, the agent events that realize it, and separate contextual evidence. Multiple actions may share a message anchor without an inferred within-message order. A retail case study produces a versioned 24-entry code...

---

### 40. Taramandal-GPT: Enhancing Astrodynamics Problem-Solving with Knowledge Retrieval and Structured Thinking

**Authors:** Akhil Sharma, Jatin Gupta, Ali Imam Abidi

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24246v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24246v1)

**Summary:** Large language models (LLMs) have shown remarkable progress in natural language understanding, yet their effectiveness in specialized fields like astronomy and astrodynamics remains limited due to challenges in multi-step reasoning, symbolic manipulation, and domain-specific terminology. To address this, we present Taramandal-GPT (Constellation-GPT), a domain-adapted framework built on the Qwen3-8b backbone, enhanced with a Retrieval-Augmented Generation (RAG) pipeline and a fallback mechanism f...

---

### 41. Memory vs. Context? Influential Factors of Factual Recall in Language Models

**Authors:** Guilhem Fouilhé, Nicholas Asher, Philippe Muller

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24238v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24238v1)

**Summary:** We reproduce and stress-test the work of Yu et al. (2023), who characterize how language models (LMs) arbitrate between memorized knowledge and contradictory in-context statements. We replicate their world-capitals experiments on 31 models spanning Pythia, GPT-2, Qwen3, and Ministral families, including base and post-trained variants, and extend evaluations to five additional knowledge relation types from the ParaConflict dataset. We empirically confirm most of their original findings: larger mo...

---

### 42. From Articles to Publishers: Aggregating Language Model Predictions for News Source Reliability Inference

**Authors:** John Bianchi, Manuel Pratelli, Fabio Pinelli, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24219v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24219v1)

**Summary:** Traditionally, the reliability of news publishers is assessed by expert organisations that evaluate editorial practices, transparency and factual standards at source. When this process is translated into a computational approach, the problem is often formulated at the level of individual articles, with models being trained on a set of pre-labelled articles and their performance being evaluated in a test phase. In this work, we investigate news source reliability inference as a source-level predi...

---

### 43. Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations

**Authors:** Kaushal Santosh Bhogale, Srija Anand, Sadakopa Ramakrishnan Thothathiri, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24199v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24199v1)

**Summary:** Evaluation benchmarks for Indian language automatic speech recognition (ASR) suffer from two systematic biases: optimistic scores from clean, controlled audio conditions, and pessimistic scores from overly rigid transcription standards that penalize valid linguistic variations. We introduce Vimarsha, a 100-hour benchmark spanning all 22 scheduled Indian languages, designed to address both distortions. Vimarsha combines demographically diverse on-field recordings with carefully mined in-the-wild ...

---

### 44. LoopCD: Loop-wise Contrastive Decoding for Improving Reasoning in Looped Language Models

**Authors:** Byeongho Yu, Junhyuk So, Eunhyeok Park

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24196v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24196v1)

**Summary:** Looped Language Models (LoopLMs) perform "latent reasoning" by recursively refining internal latent representations with shared weights, offering a more effective alternative to explicit verbal reasoning. Despite their effectiveness, we find that LoopLMs remain prone to loop instability: unstable refinement across iterations can produce localized uncertain "hard" tokens associated with reasoning errors. To address this, we propose LoopCD, loop-wise contrastive decoding that enhances the reasonin...

---

### 45. When Residualization Helps an Audit: Format Effects, Slice Gains, and Their Limits

**Authors:** Daein Weon, Dong Ho Kang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24194v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24194v1)

**Summary:** Evaluation scores used around LLM systems -- including reward models, rerankers, and LLM judges -- can track surface form instead of the quality they claim to measure. When presented with a terse correct solution and a commented buggy solution for the same MBPP problem, a public preference reward model selects the correct one no better than a coin flip (0.507). Subtracting the predictable surface component from such scores is increasingly common, but removal alone does not yield a more valid mea...

---

### 46. Efficient LLM Distillation for Bangladesh Legal Context: A Smartphone-Compatible Retrieval-Augmented Generation Model

**Authors:** MD. Nafis Kamal, Mahadi Hasan Fahim, Talha Ridwan, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24177v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24177v1)

**Summary:** Legal information in Bangladesh is inaccessible to most citizens. Statutory text is English-only, trained lawyers are concentrated in urban centres, and cloud-dependent AI fails where mobile connectivity is unreliable, a setting in which hallucinated legal text causes direct harm. The system addresses statutory interpretation only; queries that require judicial precedent or case-law reasoning fall outside its scope. We target the statutory access gap by compressing a 9-billion-parameter Gemma-2 ...

---

### 47. TAC-Time: Texts as Channels For Multimodal Time Series Forecasting

**Authors:** Jiayi Liang, Xiaotian Gu, Xinyu Xie, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24156v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24156v1)

**Summary:** Most existing time series forecasting methods rely solely on numerical observations, overlooking rich contextual information from auxiliary texts. Recent multimodal approaches attempt to incorporate textual signals, but they often treat text as static features or use large language models as forecasting backbones, limiting their ability to capture temporal dynamics and increasing computational cost. To address these challenges, we propose TAC-Time, a unified framework that transforms textual inf...

---

### 48. Data Agents: Agentic Data Systems

**Authors:** Guoliang Li, Peiyao Zhou, Xuanhe Zhou, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24137v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24137v1)

**Summary:** Traditional data systems face profound limitations in the AI era, relying on human-crafted pipelines, lacking semantic understanding of heterogeneous data, and operating through rigid, reactive processing. To address these challenges, we propose a new paradigm called the Data Agent, designed to manage, process, and analyze data with minimal human intervention. Data agents autonomously execute a wide range of data-related tasks, transforming traditional data systems by shifting from manual design...

---

### 49. Re:CAP - Auditing Retrieval Coverage in Production RAG Pipelines

**Authors:** Aviral Joshi, Hanoz Bhathena, Max Nelson, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24122v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24122v1)

**Summary:** Retrieval-augmented generation (RAG) is hard to monitor in production: exhaustive relevance labels do not exist for non-stationary multi-million-passage corpora that re-index in real time. As a result, retrieval quality is generally understudied and often deprioritised in favour of generation-oriented metrics. In this work, we propose auditing retrieval coverage by probing for evidence of missing documents rather than enumerating every relevant one. Our method Re:CAP (REtrieval Coverage Audit by...

---

### 50. You Can Tell Who's Asking: What the Web's Questions Are Made Of, and Where They Come From

**Authors:** Calvin Zhou, Vincent McCloskey, Krishna Srinivasan

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24106v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24106v1)

**Summary:** Questions scraped from the web are used across academia and industry as a proxy for what people want to know. Across QA training data, retrieval benchmarks, and content strategy, questions on a page are assumed to reflect human intent. We test this assumption at scale by extracting 13.4B question occurrences across 110 FineWeb snapshots (2013-2025), and report three findings. First, you can tell who is asking: provenance (the host/page of questions) leaves a signal in question form, and a logist...

---

## cs.LG

**50 papers**

### 1. Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use

**Authors:** Zixiang Chen, Wenting Zhao, Zhepeng Cen, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24985v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24985v1)

**Summary:** Multi-turn tool-use failures can hinge on a single model call, yet reward variation alone does not reveal which call would benefit from training. When rewards depend on later interactions, their variation can reflect downstream randomness rather than differences between the current actions. We introduce Critical-State RL to identify trainable states in multi-turn interactions. Given task-defined candidate calls and local rewards, the method assesses whether each reward captures the action's effe...

---

### 2. onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction

**Authors:** Lei Yang, Mengyin Liu, Jia Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24983v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24983v1)

**Summary:** We present onPanda, an interactive tool for efficiently annotating LLM alignment data and agent trajectories. onPanda adopts token-level correction as its core interaction: while reading a model response, the annotator locates the first inappropriate token and either picks a substitute from the model's candidate tokens or types the correct text via free-form editing. The system then truncates everything after that position and continues generation from the corrected prefix, repeating this locate...

---

### 3. LoRA-generating hypernetworks for efficient on-device LLM generative personalization

**Authors:** Sean Augenstein, Li Ding, Jihwan Lee, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24979v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24979v1)

**Summary:** On-device large language models (`LLMs'), e.g. running on mobile phones, are ripe for improvement via personalization. The limited compute resources of mobile devices impose limits on model scale and thus model quality, making any realizable quality gains highly impactful. At the same time, their personal nature (i.e., the close coupling to a particular user) means that a given on-device LLM tends to be used in similar, predictable patterns over the course of time. This paper presents a novel me...

---

### 4. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

**Authors:** Peng Xia, Rujun Han, Zifeng Wang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24972v1)

**Summary:** An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-d...

---

### 5. Rare Event Estimation via Iterative Unalignment

**Authors:** Hanming Yang, Daksh Mittal, Jing Dong, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24969v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24969v1)

**Summary:** As agents are deployed with increased autonomy, even extremely rare events along their stochastic output trajectories can occur and prove catastrophic. Safe deployment therefore does not depend on whether these events can occur, but on how often they might. We study the problem of estimating the probability of rare events that arise from stochastic variation in the agent's own actions. Estimating this type of risk requires searching over the combinatorially vast space of trajectories. Naive Mont...

---

### 6. JAREX: An Acquisition Function for Multi-Objective Algorithmic Process Characterization

**Authors:** Xinyang Li, Kevin Stone, Ajit Vikram

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24954v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24954v1)

**Summary:** Pharmaceutical process characterization is central to Quality by Design because it defines how variations in process parameters affect the ability to meet product quality specifications, thereby supporting proven acceptable ranges and robust manufacturing. In practice, however, characterization still relies largely on factorial design of experiments (DOE) approaches, which are inefficient for resolving multivariate pass/fail boundaries in higher-dimensional spaces. While Bayesian optimization ha...

---

### 7. Learning Physics from an Imperfect Ancestor

**Authors:** S. Mohammad Mousavi, Teeratorn Kadeethum, Nikolaos Bouklas, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24947v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24947v1)

**Summary:** Neural operators evaluate parametric partial differential equations cheaply but degrade sharply outside their training distribution. Physics-informed neural networks avoid dependence on labeled data, yet their optimization can be basin-fragile: when the governing residual admits multiple solutions, a PINN trained from scratch may converge to a physically incorrect state despite achieving a small residual. We show that these failure modes can be addressed jointly: an imperfect NO provides the str...

---

### 8. Exactness at Inference: A Representational Criterion for Out-of-Distribution Generalization

**Authors:** Filipe Marinho Rocha, Inês Dutra, Vítor Santos Costa, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24942v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24942v1)

**Summary:** A model generalizes outside its training distribution only when it computes a representation structurally equivalent to the generating mechanism, not an approximation fitted to it. Such equivalence is necessary for exactness in and out of distribution, and extrapolation is governed by this exactness at inference, whatever its realization. Tensor Logic shows this: a zero-temperature contraction is equivalent to discrete logic, deducing in place with no artefact extracted, its tensors Boolean, its...

---

### 9. Conformalized Quantile Regression and Minimax Limits of Fixed-Score Calibration under Known Covariate Shift

**Authors:** Rustam Isaev, Anton Conrad, Denis Belomestny, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24929v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24929v1)

**Summary:** In this paper, we study nonasymptotic $L^p$ error bounds for interval length and conditional coverage in split conformalized quantile regression (CQR). Our bounds rely on local regularity conditions and accuracy guarantees for the estimated quantiles. We further instantiate our bounds for quantile regression with sparse ReLU neural networks. We also consider covariate shift, where the calibration and test covariates have different distributions, and derive nonasymptotic bounds for this setting. ...

---

### 10. OSWorld-Pro: Process-based Evaluation for Computer Use Agents

**Authors:** Zhilin Wang, Shaokun Zhang, Yifan Zhang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24890v1)

**Summary:** Evaluation of Computer-Use Agents (CUAs) is often limited to the final deliverables they create (at the end of hundreds of steps) and assessed with functional verifiers, as seen in OSWorld. However, such evaluation of end-state performance lacks transparency into how and why agents fail in various tasks, obfuscating critical insight for subsequent improvement. For instance, agents that err during keyboard inputs would require a different mitigation strategy from those that fail to precisely prov...

---

### 11. Learning Prognostic Variables for AI Convective Parameterizations via Symbolic Distillation

**Authors:** Jurij Schönfeld, Tom Beucler, Julien Savre, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24882v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24882v1)

**Summary:** Hybrid AI-physics climate modeling aims to improve coarse (~100km-resolution) Earth system models by learning to parameterize subgrid processes from high-fidelity data. However, this so far mostly involves local-in-time, diagnostic parameterizations, in which the subgrid state depends only on the current coarse state with no memory of previous states, which is unrealistic for processes such as convection that have intrinsic persistence. To address this, we enhance local-in-time parameterizations...

---

### 12. When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting

**Authors:** Yifan Hu, Xilin Dai, Zhiyuan Qu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24862v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24862v1)

**Summary:** Agentic time series forecasting concerns systems whose underlying mechanisms evolve, making the relative effectiveness of numerical models, reasoning strategies, and intervention rules inherently time-varying. Consequently, a time series agent must adapt the forecasts it produces and the orchestration policy that determines which components to trust and how to coordinate them. The deployment process naturally provides supervision for this adaptation as forecast horizons elapse and realized targe...

---

### 13. PredActor: Predictive Action Diffusion for Steerable Onboard Humanoid Control

**Authors:** Lei Ye, Haibo Gao, Yitang Li, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24840v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24840v1)

**Summary:** Diffusion models offer flexible motion generation, but translating this flexibility into feedback-responsive humanoid control remains challenging. Hierarchical systems steer motion through references that may exceed a separate tracker's capabilities, leaving recovery and physical execution largely to the tracker. Action-only diffusion generates actions directly but lacks an explicit future-state trajectory for test-time motion objectives. Joint state-action diffusion provides this representation...

---

### 14. G-NAC: Graph Neural Automata Clustering via Emergent Domain Formation

**Authors:** Keith Miller, Tristan Crawford

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24823v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24823v1)

**Summary:** We introduce Graph Neural Automata Clustering (G-NAC), an unsupervised clustering method in which observations interact as cells on a fixed neighborhood graph. A shared recurrent graph-neural cellular rule evolves latent domain states through local interactions, which are converted into a rank-based spectral affinity for partitioning. Across 73 clustering tasks from 57 benchmark datasets, G-NAC achieved a mean adjusted Rand index (ARI) of 0.7951, comparable to Genie at 0.7941 and higher than the...

---

### 15. Mobile Imaging Solutions for Medical Diagnosis: Trends and Applications

**Authors:** Syed Muhammad Ibne Zulfiker, Tanzima Hashem, Fariha Tabassum Islam, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24814v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24814v1)

**Summary:** Advances in processing power, camera technologies, and mobile image analysis have made smartphones and other mobile devices, such as laptops, increasingly suitable for medical diagnosis and healthcare applications. Researchers have developed low-cost solutions for the early detection and monitoring of various health conditions, including eye and ENT diseases, malnutrition, heart rate variability, skin and oral conditions, and injuries, using images captured by non-medical devices such as smartph...

---

### 16. Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention

**Authors:** Julien Siems, Riccardo Grazzi, Korbinian Pöppel, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24797v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24797v1)

**Summary:** Linear RNNs based on the delta-rule enable efficient sequence modeling, but their linear updates with a low-rank correction constrain their expressivity. Prior work has shown that composing two delta-rule transitions in a single recurrent update can model a 2D rotation, but this increases the rank and the cost of the updates compared to a single transition. We show that Kimi Delta Attention (KDA) can realize 2D rotations by combining a single delta-rule transformation with a second reflection su...

---

### 17. Detecting Agitation Before Behavioral Escalation in Autistic Youth Through Multimodal Wearable Sensing

**Authors:** Nibraas Khan, Abigale Plunk, John Staubitz, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24791v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24791v1)

**Summary:** Challenging behaviors including aggression, self-injury, and property destruction are observed in 68% of autistic youth and pose risks to youth and caregivers. These episodes are preceded by agitation, a rising state of distress expressed through movement, vocalization, and autonomic arousal. Its signs are subtle and individualized, and its autonomic components are invisible without instrumentation. We collected upper-body movement from inertial measurement units, physiology from a wrist-worn de...

---

### 18. XSQ-AST: An Explainable Audio Spectrogram Transformer Framework for Localising Synthetic Speech Artifacts

**Authors:** Ben Heritage, Luca Resti, Mónica Villanueva Aylagas, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24770v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24770v1)

**Summary:** Localising artifacts in synthetic speech remains challenging, as most evaluation methods yield only global quality scores. This paper presents XSQ-AST, a framework that combines the SQ-AST speech quality model with WhisperX phoneme alignment and multiple saliency methods to produce temporally localised artifact diagnostics without model retraining. Saliency maps are projected onto continuous distributions via kernel density estimation and onto phoneme boundaries via phoneme-discretised saliency ...

---

### 19. Inference of Unknown Dynamical Components Using Next Generation Reservoir Computing: From Chaotic Systems to Climate Data

**Authors:** Jule Budnick, Andrew Keane, Serhiy Yanchuk

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24754v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24754v1)

**Summary:** We investigate next generation reservoir computing (NGRC) as a data-driven approach for inferring unseen components of dynamical systems. We compare NGRC with traditional reservoir computing (RC) using the Lorenz and Rössler system, where two unknown components are inferred from one given component. For both systems, NGRC achieves accurate results while requiring fewer training data and less computational time than RC. We identified an inverse proportional behavior between the number of time-del...

---

### 20. Reinforcement Learning in Operational Research: A Technical Review and Practical Roadmap

**Authors:** Yahan Lu, Dongyang Xia, Nursen Aydin, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24750v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24750v1)

**Summary:** The growing demand for real-time, data-driven decision-making in complex and dynamic systems is placing increasing pressure on traditional Operational Research (OR) methodologies. Reinforcement learning (RL) has emerged as a complementary approach, offering strong learning and computational capabilities for sequential decision-making in dynamic and uncertain environments. Recent research shows an increasing interest in integrating RL with OR to address dynamic decision-making problems, enhance h...

---

### 21. D-JEPA: A Decision-Aligned Latent World Model

**Authors:** Shuaijun Liu, Chengyu Wu, Qifu Wen, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24749v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24749v1)

**Summary:** Latent world models predict the consequences of actions, but accurate prediction does not guarantee that latent distance reflects which candidate will execute successfully. We identify a decision-local prediction gap: among the few futures competing for execution, a candidate predicted closer to the goal can produce a worse realized outcome than an available alternative. We introduce D-JEPA, a decision-aligned latent world model that learns decision-relevant relations among candidate futures fro...

---

### 22. Enhancing Transformer Representations of Symbolic ODE Expressions

**Authors:** Xiyue Fan, Adam Prugel-Bennett, Stuart E. Middleton

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24746v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24746v1)

**Summary:** Existing approaches to solving differential equations, such as symbolic regression, physics informed neural networks, and neural operators, typically focus on numerical approximations or blind symbolic search via fitting to numerical data. Less attention has been paid to learning structured representations of mathematical expressions that preserve commutative properties and could support mathematical reasoning in symbolic forms. Transformer models have shown strong capabilities in solving symbol...

---

### 23. An Exact Junction-Tree Extended Formulation for Optimal Classification Trees

**Authors:** Jiancheng TU,  WenqiFan

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24741v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24741v1)

**Summary:** We develop an exact linear programming (LP) formulation for bounded-depth classification trees with binary features, using a junction-tree representation. The formulation is integral and supports recursive subtree optimization. Exact reductions make the model smaller while preserving the optimal value and recovery of an optimal tree. The reduced model supports two solution methods: column generation and message passing. Column generation solves integral restricted LPs and uses bounds over the fu...

---

### 24. MiTHras: Task-specific Hierarchical Semi-supervised Contrastive Masked Autoencoder for Mitotic Figure Analysis

**Authors:** Trinh T. L. Vuong, Simon Graham, Quoc Dang Vu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24736v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24736v1)

**Summary:** Mitotic figure (MF) analysis supports tumor grading and prognostic assessment, but automated models remain sensitive to differences in tissue type and image acquisition. We present MiTHras, a task-specific pretraining framework that combines pseudo-label-guided image- and token-level contrastive learning with masked reconstruction. We construct TCGA-MF-Pseudo, a corpus of 1.8 million cell-centered images from 14 TCGA cohorts spanning 11 organ sites. Comprehensive evaluation on MF classification,...

---

### 25. A Federated Artificial Intelligence Framework for Optimizing Pancreatic Cancer Treatment - Strategy Update

**Authors:** Anne-Christin Hauschild, Amirreza Aleyasin, Nils H. Beyer, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24718v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24718v1)

**Summary:** While a centralized approach involving patient consent to collect and analyze data centrally would theoretically offer the best data quality and predictive performance, it is not always feasible in practice. Federated Learning (FL) architectures have shown to be a very promising approach to use and access distributed disease related resources within the GDPR boundaries. In a previous case report, we described the preconditions at the participating sites and necessary administrative and process r...

---

### 26. Offline Reinforcement Learning for Distribution-Grid Protection

**Authors:** Julian Oelhaf, Alexander Luce, Christian Bergler, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24703v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24703v1)

**Summary:** Data-driven protection may complement conventional relays in distribution grids whose operating conditions vary with distributed generation, switching events, and changing short-circuit levels. We study line-selective tripping from static trajectories of a realistically simulated CIGRE medium-voltage network using offline reinforcement learning. A convolutional Q-network receives causal voltage-current phasor and apparent-impedance features, optionally together with raw waveforms, and is trained...

---

### 27. Guaranteed Low-Rank Tensor Recovery from Modewise Measurements via Normalized Block-Weighted Riemannian Gradient Descent

**Authors:** Yushi Zhou, Feng Zhang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24679v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24679v1)

**Summary:** We consider the recovery of low-multilinear-rank tensors from linear measurements and propose an adaptive block-weighted modewise Riemannian gradient descent method. The method combines memory-efficient modewise measurements with a normalized adaptive weighting strategy for the core and factor components of the Riemannian gradient. The weighting improves convergence without increasing the multilinear-rank bound of the search direction or the size of the reduced core used for retraction. Under th...

---

### 28. Muon Can Outperform Dedicated Continual Learning Methods

**Authors:** Sebastian George Sincari, Bogdan Alexandru Gheorghe, Antonio Barbalau

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24678v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24678v1)

**Summary:** Continual learning with Low-Rank Adapters (LoRA) typically mitigates forgetting by penalizing the overlap between a new update and the accumulated past weights, which discourages certain update directions without controlling how an update distributes its energy over the ones that remain. We ask whether that restriction has to be task-aware, or whether a generic one supplied by the optimizer is enough. We train a plain incremental LoRA (IncLoRA) with Muon, which orthogonalizes each update, and co...

---

### 29. Corrective Forcing: Unified Post-Training for Diffusions and Flows in Generative Speech Enhancement

**Authors:** Qing Yao, Lijian Gao, Qirong Mao

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24651v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24651v1)

**Summary:** Diffusion and flow models, as promising generative paradigms for speech enhancement, face a training--inference mismatch: training uses analytical path states, whereas inference recursively evaluates models on self-generated rollout states along discretized sampling trajectories. This mismatch causes prediction and discretization errors to accumulate. To address it, we introduce Corrective Forcing (CoF), a post-training paradigm that forces diffusion and flow models to learn from self-generated ...

---

### 30. iSDFT: Information-Proximal Self-Distillation for Continual Learning in LLMs

**Authors:** Ahmed Khaled Khamis, Xiaotong Ji, Hassan Jaber, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24646v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24646v1)

**Summary:** On-policy self-distillation fine-tuning (SDFT) learns new skills from demonstrations while reducing forgetting, but it always distils toward the full demonstration-conditioned teacher. This fixes teacher influence at the full-teacher endpoint, providing no control over how much demonstration information should be transferred at each prediction state. We introduce Information-Proximal SDFT (iSDFT), which instead treats the teacher as a budgeted source of information. At each token, iSDFT selects ...

---

### 31. Augmented Hypothesis Testing with Persona-Based LLM Simulations

**Authors:** Ziyad Benomar, Aymen Al Marjani, Paul Missault, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24629v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24629v1)

**Summary:** A/B testing requires large sample sizes, long timelines, and significant costs. When auxiliary predictions of experimental outcomes are available from machine learning models, uncertain prediction quality precludes replacing human experiments entirely, yet these predictions may still contain useful signal. We propose a principled framework for learning-augmented hypothesis testing that leverages predictions of unknown quality to reduce sample sizes while maintaining statistical validity. Predict...

---

### 32. Learning tactile perception from high-bandwidth single-point sensing

**Authors:** Joseph Rigal, Emmanuel Virot, Caroline Pascal

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24621v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24621v1)

**Summary:** Tactile sensing is increasingly being incorporated into learning-based robotic manipulation, yet many existing approaches rely on spatially distributed sensors. Here we introduce SpectRobot, a framework that transforms single-point tactile signals into compact time-frequency spectrograms. These spectrograms encode high-bandwidth tactile histories as fixed-size image-like representations. They can be processed by standard vision encoders and integrated into learning pipelines originally developed...

---

### 33. GraphToolbox: A Configurable Python Framework for Graph Neural Network Forecasting

**Authors:** Eloi Campagne, Yvenn Amara-Ouali, Yannig Goude, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24609v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24609v1)

**Summary:** Electricity forecasting often involves spatially related signals observed over regions, substations, and feeders, and Graph Neural Networks (GNNs) provide a natural way to represent these relations. Building a complete GNN forecasting experiment is nonetheless laborious, because graph construction, model selection, training, aggregation, and interpretation sit in incompatible tools. We present GraphToolbox, an open-source Python framework that unifies these stages in one configurationdriven pipe...

---

### 34. Taking a Second Look: Correcting Sea Ice Forecasts with Sparse Observations

**Authors:** Tianshuo Zhang, Xianglei Xing, Aowen Yang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24591v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24591v1)

**Summary:** Sea ice forecasts are issued several days ahead, allowing errors to accumulate while new, often sparse sea ice concentration (SIC) observations become available. We find that fixed-propagation errors concentrate near structured, high-gradient ice edges, whereas homogeneous interiors require limited propagation, suggesting that propagation distance should be state dependent. We therefore introduce ECHO (Evidence-guided Correction with Heterogeneous prOpagation), where ECHO-Scale adapts propagatio...

---

### 35. Overlay\_dx - Automating forecasting evaluation

**Authors:** Long Ngo, Mohammed Amine Chamli, Jonathan Rivalan, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24586v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24586v1)

**Summary:** Traditional evaluation metrics provides numerical values but often lack comprehensibility, hindering effective differentiation of model performances. Our work addresses this challenge by introducing overlay\_dx, a novel evaluation metric measuring the performance of time series prediction models. Overlay\_dx is a visual metric that represents the percentage of predictions falling within a confidence interval around actual values. Additionally, once evaluation results are plotted, overlay\_dx com...

---

### 36. Universal Multi-Modal Traceformer: Integrating Heterogeneous Context for Process Event Prediction

**Authors:** Fabian Spaeh, Jingxing Fang, Shandian Zhe, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24579v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24579v1)

**Summary:** Event logs arise in a wide range of real-world processes, capturing not only event activities and timestamps but also multi-modal contextual information. Existing event-sequence models, including many temporal point process approaches, primarily model event activities and timestamps while overlooking heterogeneous context, such as numerical measurements, categorical attributes, textual descriptions, and metadata associated with individual events and entire traces. In this paper, we propose Unive...

---

### 37. Poisson Exchange Beyond Submodularity: Effective Approximation Algorithms for Offline and Online Subset Selection over Matroids

**Authors:** Shi Fu, Youming Qiao, Dacheng Tao, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24569v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24569v1)

**Summary:** Over the past decade, a growing body of research has shown that $γ$-weak submodularity broadly arises in numerous subset selection tasks, including feature selection, neural network pruning, and video summarization. Despite its prevalence, maximizing a $γ$-weakly submodular function subject to a general matroid constraint remains challenging. To date, the only known approximation guarantee is the conservative $(1+1/γ)^{-2}$ factor established by \citet{chen2018weakly}. To improve upon this resul...

---

### 38. $t_0$: A Time-Series Foundation Model for Forecasting with Context

**Authors:** Lucas Meyer, Claudio Sole, Huikan Xiang, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24559v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24559v1)

**Summary:** We present $t_0$, a family of open-weights foundation models for forecasting with multivariate context. We release its first two members: $\texttt{t0-alpha}$ and $\texttt{t0-beta}$, respectively 102M and 256M parameters. Both condition their forecasts on target history, past covariates, and known-future covariates, without task-specific retraining. Their transformer layers alternate attention along time and across variates. They produce probabilistic forecasts through quantile predictions. Pretr...

---

### 39. Identifying Representational Biases in Datasets Using PCA: A Max-Disparity Partition Framework

**Authors:** Arjun KM, Shashi Jain

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24556v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24556v1)

**Summary:** Principal Component Analysis (PCA) minimises aggregate reconstruction error, which can inadvertently represent majority subgroups with substantially higher fidelity than minority subgroups. Fairness-aware extensions of PCA correct this disparity but require group labels as input. We address the logically prior question: given only a data matrix, which binary partition of the data suffers the greatest representational disparity under a shared PCA projection? We formalise this as the max-disparity...

---

### 40. Beyond Point Prediction: Artificial Representative Trees with Uncertainty

**Authors:** Lea L. Mairhöfer, Silke Szymczak, Björn-Hergen Laabs, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24528v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24528v1)

**Summary:** Random forests (RFs) predict well but are opaque, whereas single decision trees are interpretable but unstable. Artificial representative trees (ARTs) were developed as interpretable surrogate models for RFs, but their use as standalone prediction models with uncertainty quantification has not been systematically investigated. We combine ARTs with leaf-wise Mondrian conformal predictive systems (CPS), enabling a single tree to provide continuous predictions, prediction intervals, and probabiliti...

---

### 41. Not All Task Vectors Need Equal Rank: Energy-Proportional Allocation for Model Merging

**Authors:** Hyunjoong Cho, Jinhyeok Jang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24517v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24517v1)

**Summary:** Model merging aims to combine multiple fine-tuned models derived from a common pretrained model into a single multi-task model without additional joint training. Recent spectral merging methods improve over simple weight averaging by exploiting low-rank structures of task-specific updates, but they commonly assign the same rank capacity to every task. This uniform allocation ignores that task vectors can have heterogeneous spectral complexity, causing the shared merging space to be used suboptim...

---

### 42. On Emergent Capabilities and Model Merging

**Authors:** Luca Zhou, Emanuele Rodolà

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24504v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24504v1)

**Summary:** Fine-tuned checkpoints and adapters now fill public repositories, and the most common operation applied to these artifacts is model merging: arithmetic on their weights that assembles capabilities cheaply. We ask what this operation does to emergent capabilities: behaviors an artifact carries that were never an explicit training target. Studying two independent testbeds (activation oracles and emergent-misaligned models) across three model families, we find that the answer is threefold. First, m...

---

### 43. Lifted Bellman Linear Programming for Offline Reinforcement Learning

**Authors:** Hyukjun Yang, Jongchan Park, Narim Jeong, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24489v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24489v1)

**Summary:** Offline reinforcement learning (RL) typically trains a critic by minimizing a regression loss against bootstrapped value targets stabilized by target networks with exponential moving average (EMA) updates. Multi-step targets incorporate behavior-policy actions and therefore require off-policy correction. We instead impose in-sample Bellman optimality on the critic through inequality constraints. We formulate the Lifted Bellman Linear Program (LBLP), which lifts the linear programming characteriz...

---

### 44. Fathom-Vaidya: Advancing Medical Reasoning with Rubric-Based Rewards

**Authors:** Kalash Shah, Kunal Singh, Snehan J, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24480v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24480v1)

**Summary:** Deploying Large Language Models (LLMs) in healthcare requires robust performance across two complementary dimensions - diagnostic reasoning: the convergent, evidence-driven task of inferring a patient's condition from clinical data to produce a diagnosis, and clinical healthcare reasoning: the broader, navigational judgment required to communicate, plan, and adapt across multi-turn clinical interactions where a single correct answer may not exist. Recent benchmarks such as HealthBench and MedXpe...

---

### 45. A Temporal Knowledge Graph for Music Festival Lineup Forecasting

**Authors:** Julia Gastinger, Thilo Dieing, Christian Meilicke, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24467v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24467v1)

**Summary:** Music festival lineups emerge from complex relationships among artists, genres, releases, labels, and past performances, making the prediction of future lineups a natural fit for temporal knowledge graph (TKG) forecasting. In this work, we present a TKG covering 380 festivals over 55 years, comprising more than 90K festival performance quadruples along with information on festivals, artist tours, and artist metadata, and release it as a resource for TKG forecasting evaluation. We formalize festi...

---

### 46. RAILS: Retrieval-Augmented Incremental LLM Clustering at Scale

**Authors:** Armin Oliya, Aleksandra Sawczuk, Radosław Białobrzeski

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24464v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24464v1)

**Summary:** Using a Large Language Model (LLM) as the clusterer at production scale is hard: prompts cannot hold the entire label space, and per-document serial processing does not deliver the throughput real workloads require. We present RAILS, a retrieval-augmented incremental LLM clusterer that turns clustering into a simple loop over a growing label pool and scales through document batching with bounded concurrency. On six public benchmarks RAILS exceeds the strongest prior LLM-clustering method on aver...

---

### 47. MECAIL: Communication-Aware Incremental Learning for Object Detection with 14.6 KB Spatiotemporal Experts

**Authors:** Matthias Neuwirth-Trapp, Maarten Bieshaar, Danda Paudel, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24455v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24455v1)

**Summary:** Intelligent transportation systems require Incremental Learning (IL) to continually improve their overall performance in dynamic environments. However, most edge devices lack the computational resources to support on-device IL, requiring updates to be transmitted from centralized servers. We propose using this setup to obtain dense, specialized module coverage that adapts a fixed base model to specific spatiotemporal contexts, such as parking lots, gas stations, ferries, or construction sites. H...

---

### 48. WPBench: A Comprehensive Benchmark for Wind Power Forecasting

**Authors:** Yuhan Zhu, Jilin Hu, Xinying Cai, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24444v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24444v1)

**Summary:** Accurate, reliable, and deployable wind power forecasting is critical for power system dispatch, renewable energy integration, and electricity market operations. Progress in this field hinges on the ability to empirically and comprehensively benchmark forecasting methods. Yet existing benchmarks fall short of supporting systematic evaluation in four key aspects: 1) limited coverage of wind power scenarios across turbine scale, variable composition, and spatial structure; 2) incomplete coverage o...

---

### 49. Horizon-Aware Early Event Prediction for Tokamak Disruption Alarms

**Authors:** Takeshi Koshizuka, Takaharu Yaguchi

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24443v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24443v1)

**Summary:** Reliable disruption prediction is essential for the safe operation of future tokamaks. Existing full-distribution survival methods model the complete residual time-to-disruption distribution, whereas operational decisions primarily depend on disruption risk within a finite prediction horizon. This mismatch motivates introducing Early Event Prediction (EEP) objectives into survival-based disruption prediction. We take Deep Survival Machines (DSM) as the full-distribution baseline and propose appl...

---

### 50. MUSE: Dependency-Aware Adaptation of a Frozen Vision Backbone for Multivariate Time Series Forecasting

**Authors:** Xinying Cai, Junkai Lu, Yuhan Zhu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24441v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24441v1)

**Summary:** Multivariate time-series forecasting is essential to many real-world applications. Recent large vision models (LVMs) offer a promising paradigm by transferring cross-domain visual priors to time-series forecasting. However, existing LVM-based methods face two key challenges: balancing independent visual representation spaces with cross-variable dependency modeling, and adapting vision backbones pretrained on natural images to the distinct temporal semantics of time-series images. To address thes...

---

## stat.ML

**50 papers**

### 1. JAREX: An Acquisition Function for Multi-Objective Algorithmic Process Characterization

**Authors:** Xinyang Li, Kevin Stone, Ajit Vikram

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24954v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24954v1)

**Summary:** Pharmaceutical process characterization is central to Quality by Design because it defines how variations in process parameters affect the ability to meet product quality specifications, thereby supporting proven acceptable ranges and robust manufacturing. In practice, however, characterization still relies largely on factorial design of experiments (DOE) approaches, which are inefficient for resolving multivariate pass/fail boundaries in higher-dimensional spaces. While Bayesian optimization ha...

---

### 2. Selective Inference for CART with Binary Outcomes

**Authors:** Tomoshige Nakamura

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24949v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24949v1)

**Summary:** Binary classification trees select subgroups using the same outcomes later used to assess their differences. We develop finite-sample conditional tests of a common success probability within a parent selected by deterministic Gini CART. The construction retains all eligible cutpoints and conditions on the selected split, its ancestor path, the parent success total, and outside outcomes. The resulting uniform label fiber gives an exact count distribution, while a reversible parallel Monte Carlo c...

---

### 3. Conformalized Quantile Regression and Minimax Limits of Fixed-Score Calibration under Known Covariate Shift

**Authors:** Rustam Isaev, Anton Conrad, Denis Belomestny, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24929v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24929v1)

**Summary:** In this paper, we study nonasymptotic $L^p$ error bounds for interval length and conditional coverage in split conformalized quantile regression (CQR). Our bounds rely on local regularity conditions and accuracy guarantees for the estimated quantiles. We further instantiate our bounds for quantile regression with sparse ReLU neural networks. We also consider covariate shift, where the calibration and test covariates have different distributions, and derive nonasymptotic bounds for this setting. ...

---

### 4. Identifying Representational Biases in Datasets Using PCA: A Max-Disparity Partition Framework

**Authors:** Arjun KM, Shashi Jain

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24556v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24556v1)

**Summary:** Principal Component Analysis (PCA) minimises aggregate reconstruction error, which can inadvertently represent majority subgroups with substantially higher fidelity than minority subgroups. Fairness-aware extensions of PCA correct this disparity but require group labels as input. We address the logically prior question: given only a data matrix, which binary partition of the data suffers the greatest representational disparity under a shared PCA projection? We formalise this as the max-disparity...

---

### 5. Beyond Point Prediction: Artificial Representative Trees with Uncertainty

**Authors:** Lea L. Mairhöfer, Silke Szymczak, Björn-Hergen Laabs, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24528v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24528v1)

**Summary:** Random forests (RFs) predict well but are opaque, whereas single decision trees are interpretable but unstable. Artificial representative trees (ARTs) were developed as interpretable surrogate models for RFs, but their use as standalone prediction models with uncertainty quantification has not been systematically investigated. We combine ARTs with leaf-wise Mondrian conformal predictive systems (CPS), enabling a single tree to provide continuous predictions, prediction intervals, and probabiliti...

---

### 6. Tensor Completion using Subspace Information

**Authors:** Jingyang Li, Michael K. Ng

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24501v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24501v1)

**Summary:** Tensor completion has attracted significant attention in both applications and theoretical research. Under standard uniform sampling, existing polynomial-time guarantees generally require more observations than the number of degree of freedom, motivating the study of a possible statistical-to-computational gap in highly missing regimes. Fortunately, in many practical scenarios, side information is available, which can provide valuable insights to mitigate these challenges. In this paper, we intr...

---

### 7. Prior-Amortized In-Context Bayesian Inference for Generalized Linear Mixed-Effects Models

**Authors:** Alex Kipnis, Marcel Binz, Eric Schulz

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24422v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24422v1)

**Summary:** Hierarchical data is ubiquitous in the empirical sciences and is most commonly analyzed with generalized linear mixed-effects models (GLMMs). Bayesian inference for GLMMs yields calibrated uncertainty but requires MCMC; the No-U-Turn Sampler (NUTS) is the gold standard but is slow and must restart from scratch for every new dataset, model and prior. We introduce metabeta, a pretrained neural network for prior-amortized in-context Bayesian inference over GLMMs. Unlike previous neural posterior es...

---

### 8. A Three-Way Testing Framework for Quantifying Epistemic Calibration Uncertainty in SBI

**Authors:** Luben M. C. Cabezas, Pedro L. C. Rodrigues, Rafael Izbicki

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24419v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24419v1)

**Summary:** Current experimental scientists increasingly rely on simulation-based inference (SBI) to invert complex models with intractable likelihoods. A primary goal in these settings is to obtain credible regions with valid coverage. While recent model-agnostic conformal calibration methods have succeeded in constructing credible sets with prescribed local Bayesian coverage, their approximate nature introduces inherent epistemic uncertainty in the calibration process. In this work, we propose a novel too...

---

### 9. A Distributional Optimisation Perspective on Combining Models in Deep Learning

**Authors:** Congye Wang, Yan Lin, Zheyang Shen, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24328v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24328v1)

**Summary:** Combining predictions from different models can improve performance at machine learning tasks, but the training of the individual models and the rule used to combine them are typically chosen separately, and by ad hoc means. Recent advances in distributional optimisation (i.e. where the optimisation occurs over the set of probability distributions) offer an opportunity for principled joint training, viewing the collection of models as a discrete distribution whose support points are to be optimi...

---

### 10. Adversarially Robust PAC Learning with Optimal VC Rates

**Authors:** Steve Hanneke, Amirreza Shaeiri

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24260v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24260v1)

**Summary:** We study the problem of \emph{adversarially robust} PAC learning. In this framework, the learner observes independent samples from an unknown distribution over $\mathcal{X} \times \{0,1\}$, as in classical PAC learning. However, given a perturbation map $\mathcal{U} : \mathcal{X} \to 2^{\mathcal{X}}$ known to the learner, the goal is to output, with high probability, a predictor that correctly classifies \emph{every} perturbation $z \in \mathcal{U}(x)$ of most future examples $(x,y)$ drawn from ...

---

### 11. OSCAR: Order-aware Scoring and Calibration for AI Rankings

**Authors:** You Liu, Yue Liu, Quanchao Lu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24128v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24128v1)

**Summary:** Judge-specific sensitivity is useful for aggregating pairwise LLM evaluations, but its interpretation depends on which systematic presentation effects the ranking model includes. We introduce OSCAR, an order-aware framework for scoring and calibrating AI rankings, and study position as one such effect. In released judgments from 18 evaluators, the all-response A-minus-B score difference ranges from $-63.11$ to $98.31$ percentage points. Matching question text, response texts, candidate identitie...

---

### 12. Model-Agnostic Feature Selection via LOCO-Guided Adaptive Minipatch Sampling

**Authors:** Xuhui Liu, Lili Zheng

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24126v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24126v1)

**Summary:** Black-box machine learning models increasingly deliver strong predictions, but extracting useful information from them, such as a set of important features, remains challenging. Existing model-agnostic methods primarily estimate feature importance or conduct inference on it rather than directly selecting features, whereas many feature selection methods are model-specific or rely on the model-X assumption. We introduce LOCO-guided Adaptive Minipatch Sampling (LAMPS), a model-agnostic ensemble fra...

---

### 13. Causal Bayesian Optimization: Foundations, Methods, and Applications

**Authors:** Chenfeng Huang, Thuy T. Le, Zixuan Ma, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24112v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24112v1)

**Summary:** Causal Bayesian Optimization (CBO) combines causal inference with Bayesian optimization to enable sample-efficient intervention selection in systems with causal structure. This survey provides a systematic review of CBO through a unified BO-loop perspective, showing how causal assumptions shape intervention search spaces, surrogate models, acquisition functions, and decision policies. We organize existing methods by graph and system-knowledge assumptions, environment, intervention representation...

---

### 14. Doubly robust target inference for generalized linear regression with completely missing covariates

**Authors:** Huali Zhao, Ke Deng

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24086v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24086v1)

**Summary:** Large-scale multipurpose cohort studies and biobanks often omit covariates needed for specific downstream analyses. We study target-population inference for generalized linear regression when key covariates are completely absent from the target data but observed in a related source population. Standard missing covariate methods are not directly applicable because they require at least partial observation of the covariates in the target population. We develop a doubly robust transfer learning fra...

---

### 15. Exponential Family Synthetic Controls

**Authors:** Hector Rodriguez-Deniz, David M. Blei

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.23970v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23970v1)

**Summary:** We develop exponential family synthetic controls (EFSC), a distributional version of synthetic controls for a panel of datasets. Each cell of the panel corresponds to a dataset drawn from an exponential family whose natural parameters factorize probabilistically across units and times. We estimate the latent factors using black-box variational inference. This replaces the usual weighted-average view of synthetic controls with a flexible probabilistic model that operates on full distributions. We...

---

### 16. Sparse Regression Distilled from a Single Robust Fit

**Authors:** Wooyoung Shin, Seunghwan Park

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23937v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23937v1)

**Summary:** Robust linear fits can resist response contamination yet remain too dense or unstable for useful global explanations. We propose penalized distillation, which fits a smoothly clipped absolute deviation (SCAD) estimator to a robust initial estimator's empirical fitted surface along a safeguarded coordinate-descent path and evaluates candidate states separately for fidelity, parsimony, perturbation stability, and held-out prediction. The new results attach to the states the algorithm actually comp...

---

### 17. Density-Ratio Rescoring for Imbalanced Classification

**Authors:** Dongha Kim, Seunghwan Park

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23926v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23926v1)

**Summary:** Density-Ratio Rescoring (DRR) augments a classifier trained at the original class prior with a survey-raking dual score. Raking reweights the majority sample to match minority feature moments within a tolerance. DRR marginally standardizes the dual and base scores and combines them with a fixed weight of one half, using the fitted dual directly for prediction without resampling or refitting the base classifier. Under exact population matching and a correctly specified log-linear tilt model, the ...

---

### 18. On Generalized Naive Bayes with Continuous Features

**Authors:** Ábrahám Papp, Botond Szilágyi, Edith Alice Kovács

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23819v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23819v1)

**Summary:** The Generalized Naive Bayes (GNB) model was introduced for discrete and categorical random variables as an extension of classic Naive Bayes. We now accommodate the GNB framework to continuous explanatory variables. A central result of the paper is that structure learning of the GNB depends only on the pair copulas of the bi-variate marginals. We proved that the GNB structure can be assigned to the basis of a matroid, therefore we give greedy algorithms for finding the optimal GNB structure on th...

---

### 19. Iterative Atom Refinement: A Monotonicity Principle for Dictionary Learning

**Authors:** Alexander Christie, Miguel Moscoso, Alexei Novikov, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23812v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23812v1)

**Summary:** Dictionary learning seeks to recover an unknown dictionary $A$ from observations ${\bf y}_i = A{\bf x}_i$ with sparse coefficient vectors ${\bf x}_i$. We introduce the \emph{Iterative Atom Refinement} (IAR) algorithm, a simple procedure for recovering individual dictionary atoms. Starting from a random direction, IAR repeatedly selects the observations most strongly correlated with the current iterate and updates the direction by averaging the selected data. Our main contribution is a rigorous c...

---

### 20. Belted Engression: Sufficient Dimension Reduction for Generative Distributional Regression

**Authors:** Wenxi Tan, Bing Li, Lingzhou Xue

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23789v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23789v1)

**Summary:** Modern conditional generative models face significant challenges when learning complex covariate dependencies. While sufficient dimension reduction (SDR) provides a principled approach to compress these dependencies, traditional SDR frameworks were not formulated for conditional generation. To bridge this gap, we propose Belted Engression, a unified and architecturally parameter-efficient framework for generative distributional regression. Our approach establishes an end-to-end compress-then-gen...

---

### 21. TEMPER: Temporal Encoder-Masked Probabilistic Ensemble Regressor for Time-Series Forecasting

**Authors:** Giancarlo Vercellino

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23701v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23701v1)

**Summary:** Probabilistic forecasting requires accurate central predictions and calibrated uncertainty estimates. This paper presents TEMPER, the Temporal Encoder-Masked Probabilistic Ensemble Regressor, a univariate time-series forecasting algorithm that combines a temporal autoencoder, a differentiable masked neural decision forest, continuous ranked probability score (CRPS) training, and Gaussian-mixture post-processing. The R implementation is built on torch for R and returns horizon-wise density, distr...

---

### 22. PACE: Plug-and-Play Contextual Embedding for Feature Screening with Pretrained Tabular Foundation Models

**Authors:** Qi Qin, Erbo Li, Ting Wei, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23574v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23574v1)

**Summary:** In high-dimensional tabular learning, feature screening provides a lightweight, model-agnostic way to remove irrelevant features before model fitting. However, scoring raw values directly can miss nonlinear or distributional structure. We introduce PACE (Plug-and-Play Contextual Embedding), which inserts a frozen tabular foundation model (TFM) column encoder before an existing feature-scoring rule, expanding each feature into a higher-dimensional contextual representation. Across controlled stud...

---

### 23. Optimal High-Order Methods for Solving Monotone Variational Inequalities

**Authors:** Xinliang Zhang, Lesi Chen, Linxuan Pan, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23557v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23557v1)

**Summary:** We study second- and higher-order methods for solving smooth monotone variational inequalities (MVI). Monteiro and Svaiter (SIAM J. Optim., 2012) showed that a second-order method, NPE, converges at a rate of $\mathcal{O}(T^{-1.5})$. For convex-concave minimax optimization, a subclass of MVI problems, Chen, Liu, Luo, and Zhang (COLT 2025) recently improved this rate to $\tilde{\mathcal{O}}( T^{-1.75})$. However, the result has a substantial gap compared to the lower bound of $Ω(T^{-2.5})$ establ...

---

### 24. Decoupled Causal Discovery

**Authors:** Zhengkang Guan, Fei Wu, Kun Kuang

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23535v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23535v1)

**Summary:** Causal discovery from observational data is a fundamental yet challenging task in scientific research. While existing approaches are primarily based on conditional independence tests, structure scores, or restrictive functional assumptions, we propose Decoupled Causal Discovery (DCD), a novel decoupling-based perspective that does not rely on these methodologies. DCD directly identifies the Markov boundary (MB) by decoupling non-target variables via weighting functions, such that only variables ...

---

### 25. Distributional Balancing with Machine Learning for Clinical Trial Augmentation Using Real-World Data

**Authors:** Zern Ke, Mingshi Cui, Gemma Moran, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23524v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23524v1)

**Summary:** In clinical trials, randomization of treatment and control groups is typically used to ensure the groups have similar covariate distributions on average, resulting in unbiased causal effect estimation. Such balanced covariate distributions are hard to achieve in practice, however, due to recruitment costs, patient dropouts, and more. One possible solution to this problem is to include control patients from external, real world databases. In this paper, we propose DBML, a method that selects cont...

---

### 26. Bayesian Filtering in Physical Systems via Test-time Trained Flow Matching

**Authors:** Ruiqi Feng, Chongyi Wang, Tao Zhang, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23383v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23383v1)

**Summary:** Bayesian filtering provides a principled framework for online state estimation under uncertainty, yet its application to systems with high-dimensional states and complicated posterior distributions remains challenging. Recent generative models, such as flow matching, have shown potential in Bayesian filtering. However, they still rely on particle-based representations of the posterior, which lose the rich information of the full distribution, or tackle a trajectory-level inverse problem that con...

---

### 27. Stochastic Flow Map for Count Data

**Authors:** Ganchao Wei

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23290v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23290v1)

**Summary:** High-dimensional count data are common in scientific applications, but most diffusion and flow models are designed for continuous or categorical data, and generation often requires many sequential model evaluations. We propose Count Flow Map, a generative model that learns finite-time transitions directly in count space for one- or few-step generation. Our model directly learns stochastic transitions over finite time intervals, using Poisson births and Binomial deaths to preserve nonnegative int...

---

### 28. Bayesian Deck-of-cards-based Ordinal Regression with Sequential Preference Elicitation

**Authors:** Marco Grillo, Silvano Zappalà

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.23212v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23212v1)

**Summary:** The Deck-of-cards-based Ordinal Regression (DOR) infers a value function from a ranking of reference alternatives in which the Decision Maker (DM) inserts blank cards between consecutive levels to express preference intensity. DOR, and its stochastic extension (SMAA-DOR), treat these answers as hard constraints defining a set of compatible value functions. We propose B-DOR, a probabilistic reformulation of DOR in which each pair of adjacent levels yields an ordinal observation, the declared dire...

---

### 29. Conformal Robustness in Prediction-Driven Decision-Making

**Authors:** Lingjie Zhao, Hansheng Jiang, Wei Qi

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.23170v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23170v1)

**Summary:** Modern prediction-driven decision systems often rely on black-box predictors, but a point forecast alone does not provide the uncertainty scale required for robust downstream decision-making. We build a score-calibrated robustness framework that converts any fixed point predictor into a decision-relevant uncertainty representation through distribution-free conformal calibration. We use the conformal score, rather than a particular uncertainty set, as the primitive unit of robustness. The same sc...

---

### 30. Toscani-Fourier Distance on Probability Measures: Wasserstein Control, Topological Equivalence on Model Classes, and Duality

**Authors:** Mehrdad Mohammadi

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.23163v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23163v1)

**Summary:** Comparing probability measures in machine learning trades transport geometry against computational cost: Wasserstein distances encode the geometry of $\mathbb R^d$ but require solving a transport problem, while kernel discrepancies are cheap to evaluate yet depend delicately on their test class. We study the Toscani--Fourier family $\mathrm T_{s,p}$, the weighted $L^p$ norm of the difference of two characteristic functions, as a continuous Fourier-side discrepancy on $\mathbb R^d$. For $1\le p<\...

---

### 31. On attention heads and bilinear forms

**Authors:** Andrew O'Desky

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.22990v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22990v1)

**Summary:** We study the symmetric and antisymmetric parts of bilinear forms in the attention heads of trained large language models. We introduce an orthogonally invariant profile map from real bilinear forms to a three-dimensional simplex and observe that profiles of trained bilinear forms accumulate near profiles of rank-one bilinear forms. We prove that the symmetric part of a bilinear form in an attention head is the sum of a hyperbolic form and a zero form for a Zariski-dense subset of query-key matri...

---

### 32. Multi-Armed Bernoulli Bandits via Minimax Single-Arm Stopping

**Authors:** Huikang Liu, Zhengchao Wang, Daniel Kuhn, et al.

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.22690v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22690v1)

**Summary:** We develop an index policy for finite-horizon Bernoulli multi-armed bandits from minimax solutions to single-arm bandit (SAB) problems. Each SAB problem involves choosing between an unknown Bernoulli arm and a known reward. We show that minimizing worst-case regret of SAB problems over all non-anticipative policies admits an exact semi-infinite linear programming formulation. The resulting stopping policies offer a natural way to compare arms: the higher the known reward against which a policy c...

---

### 33. Subspace Learning with Interval-Censored Likelihoods for Dequantizing Percept PC LFP Snapshots

**Authors:** Shreesh Karjagi, Elif Ceren Fitoz, Maryam Khalid, et al.

**Published:** 2026-09-19

🔗 [Paper](http://arxiv.org/abs/2609.22658v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22658v1)

**Summary:** Implanted neurostimulators that sense local field potentials now enable chronic electrophysiology based biomarker tracking in patients at home. The Medtronic Percept PC, the only commercially available sensing-enabled deep brain stimulation (DBS) device, stores spectral amplitudes as 16-bit integers at approximately 0.1 $μ$V per bit (quantum $q \approx 0.11$ $μ$Vp). At frequencies where the true amplitude spans only a few quantization levels, consecutive bins round to the same stored value. Stan...

---

### 34. A Bayesian Vertical Federated Learning Framework for Multivariate Reduced-Rank High-Dimensional Regression

**Authors:** Brigham Halverson, Sharmistha Guha, Jessica Bernard, et al.

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22654v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22654v1)

**Summary:** Federated learning (FL) has emerged as a leading privacy-preserving framework for collaborative machine learning across decentralized environments. While considerable progress has been made in horizontal federated learning (HFL), where data with common features is distributed across sites, vertical federated learning (VFL), where sites share observations across distinct feature sets, remains less explored. Advancing Bayesian high-dimensional multivariate reduced-rank regression methods for VFL p...

---

### 35. Monotone-Constrained Diffusion Models for Long-Horizon Production Forecasting

**Authors:** Temesgen Mikael Abraha, Yves Lucet

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22643v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22643v1)

**Summary:** Forecasting a long horizon from only the first observations of a sequence is ill-posed: many trajectories are consistent with the same short history. We study this problem in oil and gas production forecasting, where forecasts made after roughly the first fifth of a well's producing life drive development and abandonment decisions, and where a usable forecast must describe a monotone decline. We present Physics-SIMS-TS, a conditional diffusion forecaster that combines negative guidance against s...

---

### 36. Locally Private Inference for Riemannian Stochastic Optimization

**Authors:** Xiaotian Chang, Yangdi Jiang, Qirui Hu

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22642v1)

**Summary:** We develop inference for manifold-valued population minimizers when each observation belongs to a different participant and only locally private messages reach the analyst. The method releases randomized tangent gradients and combines them through Riemannian stochastic approximation and Polyak-Ruppert averaging. Directly inserting a private data surrogate into a nonlinear loss can shift its population target, whereas conditional centring of the released gradient preserves the first-order equatio...

---

### 37. Classification with Abstention Under Class-Conditional Error Constraints

**Authors:** Mohammadreza M. Kalan, Yuyang Deng, Sanaz Hamidi

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22632v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22632v1)

**Summary:** We study binary classification with abstention under separate class-conditional error constraints, with the objective of minimizing abstention while keeping both errors below prescribed thresholds. We characterize the distribution-free minimax rate of excess abstention risk, up to logarithmic factors, in terms of the complexity of the hypothesis class and the sample size. To make the framework amenable to computation with models such as neural networks, we introduce surrogate-loss formulations a...

---

### 38. RLVR is a Kernel, Not a Function: Statistical Inference for pass@$k$ Crossovers

**Authors:** Chen Yang, Xianyang Zhang, Jun Chen

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22547v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22547v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) often improves pass@1 while falling behind its base model at larger sampling budgets $k$, a crossover read as evidence that RLVR only sharpens existing capability. We identify two limits to this reading. First, a visible crossing need not be statistically established: comparing models on the same prompts, we build confidence bands across sampling budgets $k$ that require evidence of both an early gain and a later loss. Across five public RLVR...

---

### 39. Moral Entropy: Auditing Bias and Uncertainty in Moral Judgment

**Authors:** Maciej Skorski

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21992v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21992v1)

**Summary:** Most work in computational ethics treats annotator disagreement on moral content as noise to be voted away, collapsed into majority vote or the more permissive any-annotator rule the moment a single annotator flags an item. We argue this uncertainty should instead be modeled and learned from.   We introduce Moral Entropy, a Bayesian framework that keeps a full posterior over the true label and decomposes its entropy into aleatoric uncertainty (irreducible disagreement about the moral content) an...

---

### 40. Schedule optimization for tau-leaping in masked discrete diffusion

**Authors:** Cecilia Secchi, Giacomo Zanella

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21960v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21960v1)

**Summary:** Masked discrete diffusion models are commonly accelerated using the so-called tau-leaping discretization method, which reveals several coordinates in parallel at each sampling step. The sampler replaces the joint conditional law of each revealed block by a product distribution, incurring a factorization error $\varepsilon_\text{fact}$ present even with perfectly learned predictors. We analyze the standard sampler on $N$ coordinates with $K$ sampling steps, whose random block sizes depend on a de...

---

### 41. Riemannian Simultaneous Inference for Tangent Vector Field Regression

**Authors:** Xiaotian Chang, Yangdi Jiang, Qirui Hu

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21910v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21910v1)

**Summary:** We consider nonparametric tangent vector field regression on a Riemannian manifold without boundary. Because responses at different points lie in different tangent spaces, the proposed kernel estimator first parallel transports nearby responses to the target tangent space and then forms a volume-corrected local average. We first derive its uniform second-order bias, finite-bandwidth covariance, and stochastic rate. For simultaneous inference, the tangent norm is written as a supremum over the un...

---

### 42. Geometric Mean Pooling for Equal-Weight Multiplicative Coarse-Graining

**Authors:** Ang-Kun Wu, Fangdi Wen, Jingtao Zhang

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21876v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21876v1)

**Summary:** As an alternative to the additive and extremal biases of average and max pooling, we introduce Geometric Mean Pooling (GMP), a signed pooling operator that combines the product of feature signs with the geometric mean of feature magnitudes. Motivated by local-to-global composition in quantum many-body physics, GMP retains both joint sign information and a characteristic multiplicative scale without introducing learnable pooling parameters. We show that non-overlapping hierarchical GMP preserves ...

---

### 43. EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise

**Authors:** Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21841v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21841v1)

**Summary:** Frontier language models now produce professional deliverables that expert graders judge to match human work on a substantial share of economically valuable tasks, yet most enterprise GenAI initiatives fail to show a measurable business effect and a large fraction of agentic projects are expected to be cancelled. We argue that this is substantially a measurement problem: public benchmarks answer "what can the model do?", whereas a deployment decision requires "is this workflow fit, reliable, saf...

---

### 44. How Many Posterior Samples? Calibrated Stopping for Adaptive Sensing

**Authors:** Vincent Corlay, Andriy Enttsel

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21813v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21813v1)

**Summary:** In classification-oriented adaptive sensing, posterior samples characterize uncertainty at the current measurement state and can serve two roles: they may guide the next sensing direction, while their class labels provide votes for the candidate classes and determine whether sensing should continue. We focus on the stopping layer that turns these votes into a declaration, without modifying the posterior sampler or sensing directions. A natural plug-in rule declares when the observed vote share e...

---

### 45. Neural composite likelihood estimation: simulation based inference for time series

**Authors:** Grace Yan, Mark Beaumont, Dennis Prangle

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21762v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21762v1)

**Summary:** Simulation based inference (SBI) circumvents the challenge of intractable likelihoods by using a simulator that generates data given parameter values. For instance, neural likelihood estimation (NLE) estimates the likelihood function by training a neural network to perform conditional density estimation on simulated data given corresponding parameters. However such density estimation is only feasible for relatively low dimensional data. We extend the scalability of SBI methods to a higher dimens...

---

### 46. Single-Loop Stochastic Projected Damped Extragradient Methods for Stochastic Nonconvex--(Strongly) Concave Minimax Optimization

**Authors:** Huiling Zhang, Minhao Zhang, Zi Xu

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21747v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21747v1)

**Summary:** We develop single-loop stochastic projected damped extragradient methods for stochastic nonconvex--(strongly) concave minimax optimization, with complexity guarantees for both game stationarity (GS) and optimization stationarity (OS). Our approach combines a stochastic projected damped extragradient (SPDE) method with a recursive variance-reduced variant, VR-SPDE, both of which retain a single-loop structure. Under an unbiased stochastic gradient oracle with uniformly bounded variance, SPDE find...

---

### 47. Multi-Domain Clustering via Measure Quantization

**Authors:** Rafael Pereira Eufrazio, Eduardo Fernandes Montesuma, Charles Casimiro Cavalcante

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21664v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21664v1)

**Summary:** Clustering is a fundamental task in data analysis, typically addressed through centroid-based methods such as K-means. In this work, we present a general framework for multi-domain clustering via measure quantization: given samples from multiple domains, we learn a shared set of cluster prototypes by minimizing a probability metric, such as the Sinkhorn divergence or the Maximum Mean Discrepancy, between each domain's probability measure and the measure of prototypes. Data points are then assign...

---

### 48. Improving the Predictive Performance of Bootstrap Aggregating by Dirichlet Resampling

**Authors:** Quoc Viet Le, Joonha Park

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21454v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21454v1)

**Summary:** We revisit Breiman's observation that reducing inter-tree correlation without weakening individual trees can improve random forests. Building on this principle, we introduce two variants: Dirichlet-Multinomial Bagging Random Forest (DM) and Dirichlet-Weighted Random Forest (DW). Both modulate sample reweighting via a concentration parameter $α>0$. We provide a simple theoretical criterion that clarifies when these variants behave indistinguishably from standard random forests, and we use it to g...

---

### 49. Brownian Heads for Deep ReLU Representations: Activation Mass and the Cost of Same-Sample Selection

**Authors:** Mahdi Mohammadigohari, Nicole Mücke

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21422v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21422v1)

**Summary:** Deep representation learning often selects hidden features and fits the final predictor on the same sample, so fixed-feature analysis performed after selection can omit selection cost. We study the conditional empirical Rademacher complexity of deep ReLU representations followed by bounded-norm predictors in additive or Lévy-Brownian RKHSs, termed Brownian heads. For a fixed representation, we derive an exact dual identity and sharp bounds in terms of activation mass, the average norm of the obs...

---

### 50. Robust Dual-Regularized Variable Selection under Outlier Contamination

**Authors:** Abdul-Nasah Soale, Adewale F. Lukman, Essoham Ali

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21342v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21342v1)

**Summary:** Real data often contain unusual observations that can exert disproportionate effects on variable selection, especially in complex predictor settings. We propose a two-stage {\it sparse median outer product of gradients (smOPG)} method for variable selection in single index models with outlier contamination. We first estimate sparse local gradients via \(\ell_1\)-penalized local median regression and then recover the active predictor set from a rank-one sparse approximation of the resulting gradi...

---

