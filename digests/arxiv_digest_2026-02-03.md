# arXiv Daily Digest - 2026-02-03

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Reward-free Alignment for Conflicting Objectives

**Authors:** Peter Chen, Xiaopeng Li, Xi Chen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02495v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02495v1)

**Summary:** Direct alignment methods are increasingly used to align large language models (LLMs) with human preferences. However, many real-world alignment problems involve multiple conflicting objectives, where naive aggregation of preferences can lead to unstable training and poor trade-offs. In particular, weighted loss methods may fail to identify update directions that simultaneously improve all objectives, and existing multi-objective approaches often rely on explicit reward models, introducing additi...

---

### 2. PixelGen: Pixel Diffusion Beats Latent Diffusion with Perceptual Loss

**Authors:** Zehong Ma, Ruihan Xu, Shiliang Zhang

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02493v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02493v1)

**Summary:** Pixel diffusion generates images directly in pixel space in an end-to-end manner, avoiding the artifacts and bottlenecks introduced by VAEs in two-stage latent diffusion. However, it is challenging to optimize high-dimensional pixel manifolds that contain many perceptually irrelevant signals, leaving existing pixel diffusion methods lagging behind latent diffusion models. We propose PixelGen, a simple pixel diffusion framework with perceptual supervision. Instead of modeling the full image manif...

---

### 3. RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents

**Authors:** Jialiang Zhu, Gongrui Zhang, Xiaolong Ma, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02486v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02486v1)

**Summary:** LLM-based deep research agents are largely built on the ReAct framework. This linear design makes it difficult to revisit earlier states, branch into alternative search directions, or maintain global awareness under long contexts, often leading to local optima, redundant exploration, and inefficient search. We propose Re-TRAC, an agentic framework that performs cross-trajectory exploration by generating a structured state representation after each trajectory to summarize evidence, uncertainties,...

---

### 4. Flow Policy Gradients for Robot Control

**Authors:** Brent Yi, Hongsuk Choi, Himanshu Gaurav Singh, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02481v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02481v1)

**Summary:** Likelihood-based policy gradient methods are the dominant approach for training robot control policies from rewards. These methods rely on differentiable action likelihoods, which constrain policy outputs to simple distributions like Gaussians. In this work, we show how flow matching policy gradients -- a recent framework that bypasses likelihood computation -- can be made effective for training and fine-tuning more expressive policies in challenging robot control settings. We introduce an impro...

---

### 5. AgentRx: Diagnosing AI Agent Failures from Execution Trajectories

**Authors:** Shraddha Barke, Arnav Goyal, Alind Khare, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02475v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02475v1)

**Summary:** AI agents often fail in ways that are difficult to localize because executions are probabilistic, long-horizon, multi-agent, and mediated by noisy tool outputs. We address this gap by manually annotating failed agent runs and release a novel benchmark of 115 failed trajectories spanning structured API workflows, incident management, and open-ended web/file tasks. Each trajectory is annotated with a critical failure step and a category from a grounded-theory derived, cross-domain failure taxonomy...

---

### 6. MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

**Authors:** Haozhen Zhang, Quanyu Long, Jianzhu Bao, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02474v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02474v1)

**Summary:** Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory. These fixed procedures hard-code human priors about what to store and how to revise memory, making them rigid under diverse interaction patterns and inefficient on long histories. To this end, we present \textbf{MemSkill}, which reframes these operations as learnable and evolvable memory skills, structured and reusable routines for extracting, consolidating, and pru...

---

### 7. Multi-head automated segmentation by incorporating detection head into the contextual layer neural network

**Authors:** Edwin Kys, Febian Febian

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02471v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02471v1)

**Summary:** Deep learning based auto segmentation is increasingly used in radiotherapy, but conventional models often produce anatomically implausible false positives, or hallucinations, in slices lacking target structures. We propose a gated multi-head Transformer architecture based on Swin U-Net, augmented with inter-slice context integration and a parallel detection head, which jointly performs slice-level structure detection via a multi-layer perceptron and pixel-level segmentation through a context-enh...

---

### 8. Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge

**Authors:** Xutao Ma, Yixiao Huang, Hanlin Zhu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02470v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02470v1)

**Summary:** Autoregressive large language models (LLMs) have achieved remarkable success in many complex tasks, yet they can still fail in very simple logical reasoning such as the "reversal curse" -- when trained on forward knowledge data of the form "$A \rightarrow B$" (e.g., Alice's husband is Bob), the model is unable to deduce the reversal knowledge "$B \leftarrow A$" (e.g., Bob's wife is Alice) during test. Extensive prior research suggests that this failure is an inherent, fundamental limit of autore...

---

### 9. Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts

**Authors:** Aiden Yiliu Li, Xinyue Hao, Shilong Liu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02468v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02468v1)

**Summary:** Despite advances in multimodal large language models, autonomous web agents still struggle to reliably execute long-horizon tasks on complex and dynamic web interfaces. Existing agents often suffer from inaccurate element grounding, the absence of site-specific procedural knowledge, and unstable long-term task tracking and memory, particularly when operating over complex Document Object Model structures. To address these limitations, we introduce Avenir-Web, a web agent that achieves a new open-...

---

### 10. MentisOculi: Revealing the Limits of Reasoning with Mental Imagery

**Authors:** Jana Zeller, Thaddäus Wiedemer, Fanfei Li, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02465v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02465v1)

**Summary:** Frontier models are transitioning from multimodal large language models (MLLMs) that merely ingest visual information to unified multimodal models (UMMs) capable of native interleaved generation. This shift has sparked interest in using intermediate visualizations as a reasoning aid, akin to human mental imagery. Central to this idea is the ability to form, maintain, and manipulate visual representations in a goal-oriented manner. To evaluate and probe this capability, we develop MentisOculi, a ...

---

### 11. Abstract Activation Spaces for Content-Invariant Reasoning in Large Language Models

**Authors:** Gabriele Maraia, Marco Valentino, Fabio Massimo Zanzotto, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02462v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02462v1)

**Summary:** Large Language Models (LLMs) often struggle with deductive judgment in syllogistic reasoning, systematically conflating semantic plausibility with formal validity a phenomenon known as content effect. This bias persists even when models generate step-wise explanations, indicating that intermediate rationales may inherit the same semantic shortcuts that affect answers. Recent approaches propose mitigating this issue by increasing inference-time structural constraints, either by encouraging abstra...

---

### 12. Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction

**Authors:** Han Bao, Zheyuan Zhang, Pengcheng Jing, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02455v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02455v1)

**Summary:** As Large Language Models transition to autonomous agents, user inputs frequently violate cooperative assumptions (e.g., implicit intent, missing parameters, false presuppositions, or ambiguous expressions), creating execution risks that text-only evaluations do not capture. Existing benchmarks typically assume well-specified instructions or restrict evaluation to text-only, single-turn clarification, and thus do not measure multi-turn disambiguation under grounded execution risk. We introduce \t...

---

### 13. World-Gymnast: Training Robots with Reinforcement Learning in a World Model

**Authors:** Ansh Kumar Sharma, Yixiang Sun, Ninghao Lu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02454v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02454v1)

**Summary:** Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world...

---

### 14. Thinking with Comics: Enhancing Multimodal Reasoning through Structured Visual Storytelling

**Authors:** Andong Chen, Wenxin Zhu, Qiuyu Ding, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02453v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02453v1)

**Summary:** Chain-of-Thought reasoning has driven large language models to extend from thinking with text to thinking with images and videos. However, different modalities still have clear limitations: static images struggle to represent temporal structure, while videos introduce substantial redundancy and computational cost. In this work, we propose Thinking with Comics, a visual reasoning paradigm that uses comics as a high information-density medium positioned between images and videos. Comics preserve t...

---

### 15. Active Causal Experimentalist (ACE): Learning Intervention Strategies via Direct Preference Optimization

**Authors:** Patrick Cooper, Alvaro Velasquez

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02451v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02451v1)

**Summary:** Discovering causal relationships requires controlled experiments, but experimentalists face a sequential decision problem: each intervention reveals information that should inform what to try next. Traditional approaches such as random sampling, greedy information maximization, and round-robin coverage treat each decision in isolation, unable to learn adaptive strategies from experience. We propose Active Causal Experimentalist (ACE), which learns experimental design as a sequential policy. Our ...

---

### 16. UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing

**Authors:** Dianyi Wang, Chaofan Ma, Feng Han, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02437v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02437v1)

**Summary:** Unified multimodal models often struggle with complex synthesis tasks that demand deep reasoning, and typically treat text-to-image generation and image editing as isolated capabilities rather than interconnected reasoning steps. To address this, we propose UniReason, a unified framework that harmonizes these two tasks through a dual reasoning paradigm. We formulate generation as world knowledge-enhanced planning to inject implicit constraints, and leverage editing capabilities for fine-grained ...

---

### 17. Poly-attention: a general scheme for higher-order self-attention

**Authors:** Sayak Chakrabarti, Toniann Pitassi, Josh Alman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02422v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02422v1)

**Summary:** The self-attention mechanism, at the heart of the Transformer model, is able to effectively model pairwise interactions between tokens. However, numerous recent works have shown that it is unable to perform basic tasks involving detecting triples of correlated tokens, or compositional tasks where multiple input tokens need to be referenced to generate a result. Some higher-dimensional alternatives to self-attention have been proposed to address this, including higher-order attention and Strassen...

---

### 18. SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration

**Authors:** Qingni Wang, Yue Fan, Xin Eric Wang

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02419v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02419v1)

**Summary:** Graphical User Interface (GUI) grounding aims to translate natural language instructions into executable screen coordinates, enabling automated GUI interaction. Nevertheless, incorrect grounding can result in costly, hard-to-reverse actions (e.g., erroneous payment approvals), raising concerns about model reliability. In this paper, we introduce SafeGround, an uncertainty-aware framework for GUI grounding models that enables risk-aware predictions through calibrations before testing. SafeGround ...

---

### 19. Structure Enables Effective Self-Localization of Errors in LLMs

**Authors:** Ankur Samanta, Akshayaa Magesh, Ayush Jain, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02416v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02416v1)

**Summary:** Self-correction in language models remains elusive. In this work, we explore whether language models can explicitly localize errors in incorrect reasoning, as a path toward building AI systems that can effectively correct themselves. We introduce a prompting method that structures reasoning as discrete, semantically coherent thought steps, and show that models are able to reliably localize errors within this structure, while failing to do so in conventional, unstructured chain-of-thought reasoni...

---

### 20. ReasonEdit: Editing Vision-Language Models using Human Reasoning

**Authors:** Jiaxing Qiu, Kaihua Hou, Roxana Daneshjou, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02408v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02408v1)

**Summary:** Model editing aims to correct errors in large, pretrained models without altering unrelated behaviors. While some recent works have edited vision-language models (VLMs), no existing editors tackle reasoning-heavy tasks, which typically require humans and models to reason about images.We therefore propose ReasonEdit, the first VLM editor to let users explain their reasoning during editing, introducing a new, practical model editing setup. ReasonEdit continuously stores human reasoning in a codebo...

---

### 21. Didactic to Constructive: Turning Expert Solutions into Learnable Reasoning

**Authors:** Ethan Mendes, Jungsoo Park, Alan Ritter

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02405v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02405v1)

**Summary:** Improving the reasoning capabilities of large language models (LLMs) typically relies either on the model's ability to sample a correct solution to be reinforced or on the existence of a stronger model able to solve the problem. However, many difficult problems remain intractable for even current frontier models, preventing the extraction of valid training signals. A promising alternative is to leverage high-quality expert human solutions, yet naive imitation of this data fails because it is fun...

---

### 22. SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-body Manipulation

**Authors:** Mu Huang, Hui Wang, Kerui Ren, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02402v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02402v1)

**Summary:** Simulating deformable objects under rich interactions remains a fundamental challenge for real-to-sim robot manipulation, with dynamics jointly driven by environmental effects and robot actions. Existing simulators rely on predefined physics or data-driven dynamics without robot-conditioned control, limiting accuracy, stability, and generalization. This paper presents SoMA, a 3D Gaussian Splat simulator for soft-body manipulation. SoMA couples deformable dynamics, environmental forces, and robot...

---

### 23. David vs. Goliath: Verifiable Agent-to-Agent Jailbreaking via Reinforcement Learning

**Authors:** Samuel Nellessen, Tal Kachman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02395v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02395v1)

**Summary:** The evolution of large language models into autonomous agents introduces adversarial failures that exploit legitimate tool privileges, transforming safety evaluation in tool-augmented environments from a subjective NLP task into an objective control problem. We formalize this threat model as Tag-Along Attacks: a scenario where a tool-less adversary "tags along" on the trusted privileges of a safety-aligned Operator to induce prohibited tool use through conversation alone. To validate this threat...

---

### 24. Infinite-World: Scaling Interactive World Models to 1000-Frame Horizons via Pose-Free Hierarchical Memory

**Authors:** Ruiqi Wu, Xuanhua He, Meng Cheng, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02393v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02393v1)

**Summary:** We propose Infinite-World, a robust interactive world model capable of maintaining coherent visual memory over 1000+ frames in complex real-world environments. While existing world models can be efficiently optimized on synthetic data with perfect ground-truth, they lack an effective training paradigm for real-world videos due to noisy pose estimations and the scarcity of viewpoint revisits. To bridge this gap, we first introduce a Hierarchical Pose-free Memory Compressor (HPMC) that recursively...

---

### 25. Trust by Design: Skill Profiles for Transparent, Cost-Aware LLM Routing

**Authors:** Mika Okamoto, Ansel Kaplan Erol, Glenn Matlin

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02386v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02386v1)

**Summary:** How should Large Language Model (LLM) practitioners select the right model for a task without wasting money? We introduce BELLA (Budget-Efficient LLM Selection via Automated skill-profiling), a framework that recommends optimal LLM selection for tasks through interpretable skill-based model selection. Standard benchmarks report aggregate metrics that obscure which specific capabilities a task requires and whether a cheaper model could suffice. BELLA addresses this gap through three stages: (1) d...

---

### 26. From Sycophancy to Sensemaking: Premise Governance for Human-AI Decision Making

**Authors:** Raunak Jain, Mudita Khurana, John Stephens, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02378v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02378v1)

**Summary:** As LLMs expand from assistance to decision support, a dangerous pattern emerges: fluent agreement without calibrated judgment. Low-friction assistants can become sycophantic, baking in implicit assumptions and pushing verification costs onto experts, while outcomes arrive too late to serve as reward signals. In deep-uncertainty decisions (where objectives are contested and reversals are costly), scaling fluent agreement amplifies poor commitments faster than it builds expertise. We argue reliabl...

---

### 27. Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback

**Authors:** Yaolun Zhang, Yiran Wu, Yijiong Yu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02369v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02369v1)

**Summary:** Large language model (LLM) agents are increasingly equipped with memory, which are stored experience and reusable guidance that can improve task-solving performance. Recent \emph{self-evolving} systems update memory based on interaction outcomes, but most existing evolution pipelines are developed for static train/test splits and only approximate online learning by folding static benchmarks, making them brittle under true distribution shift and continuous feedback. We introduce \textsc{Live-Evo}...

---

### 28. ReasonCACHE: Teaching LLMs To Reason Without Weight Updates

**Authors:** Sharut Gupta, Phillip Isola, Stefanie Jegelka, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02366v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02366v1)

**Summary:** Can Large language models (LLMs) learn to reason without any weight update and only through in-context learning (ICL)? ICL is strikingly sample-efficient, often learning from only a handful of demonstrations, but complex reasoning tasks typically demand many training examples to learn from. However, naively scaling ICL by adding more demonstrations breaks down at this scale: attention costs grow quadratically, performance saturates or degrades with longer contexts, and the approach remains a sha...

---

### 29. SWE-Universe: Scale Real-World Verifiable Environments to Millions

**Authors:** Mouxiang Chen, Lei Zhang, Yunlong Feng, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02361v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02361v1)

**Summary:** We propose SWE-Universe, a scalable and efficient framework for automatically constructing real-world software engineering (SWE) verifiable environments from GitHub pull requests (PRs). To overcome the prevalent challenges of automatic building, such as low production yield, weak verifiers, and prohibitive cost, our framework utilizes a building agent powered by an efficient custom-trained model. This agent employs iterative self-verification and in-loop hacking detection to ensure the reliable ...

---

### 30. Implicit neural representation of textures

**Authors:** Albert Kwok, Zheyuan Hu, Dounia Hammou

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02354v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02354v1)

**Summary:** Implicit neural representation (INR) has proven to be accurate and efficient in various domains. In this work, we explore how different neural networks can be designed as a new texture INR, which operates in a continuous manner rather than a discrete one over the input UV coordinate space. Through thorough experiments, we demonstrate that these INRs perform well in terms of image quality, with considerable memory usage and rendering inference time. We analyze the balance between these objectives...

---

### 31. Artificial Intelligence and Symmetries: Learning, Encoding, and Discovering Structure in Physical Data

**Authors:** Veronica Sanz

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02351v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02351v1)

**Summary:** Symmetries play a central role in physics, organizing dynamics, constraining interactions, and determining the effective number of physical degrees of freedom. In parallel, modern artificial intelligence methods have demonstrated a remarkable ability to extract low-dimensional structure from high-dimensional data through representation learning. This review examines the interplay between these two perspectives, focusing on the extent to which symmetry-induced constraints can be identified, encod...

---

### 32. Context Learning for Multi-Agent Discussion

**Authors:** Xingyuan Hua, Sheng Yue, Xinyi Li, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02350v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02350v1)

**Summary:** Multi-Agent Discussion (MAD) has garnered increasing attention very recently, where multiple LLM instances collaboratively solve problems via structured discussion. However, we find that current MAD methods easily suffer from discussion inconsistency, LLMs fail to reach a coherent solution, due to the misalignment between their individual contexts.In this paper, we introduce a multi-LLM context learning method (M2CL) that learns a context generator for each agent, capable of dynamically generati...

---

### 33. Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics

**Authors:** Ziwen Xu, Chenyan Wu, Hengyu Sun, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02343v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02343v1)

**Summary:** Methods for controlling large language models (LLMs), including local weight fine-tuning, LoRA-based adaptation, and activation-based interventions, are often studied in isolation, obscuring their connections and making comparison difficult. In this work, we present a unified view that frames these interventions as dynamic weight updates induced by a control signal, placing them within a single conceptual framework. Building on this view, we propose a unified preference-utility analysis that sep...

---

### 34. Rethinking Generative Recommender Tokenizer: Recsys-Native Encoding and Semantic Quantization Beyond LLMs

**Authors:** Yu Liang, Zhongjin Zhang, Yuxuan Zhu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02338v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02338v1)

**Summary:** Semantic ID (SID)-based recommendation is a promising paradigm for scaling sequential recommender systems, but existing methods largely follow a semantic-centric pipeline: item embeddings are learned from foundation models and discretized using generic quantization schemes. This design is misaligned with generative recommendation objectives: semantic embeddings are weakly coupled with collaborative prediction, and generic quantization is inefficient at reducing sequential uncertainty for autoreg...

---

### 35. Building a Correct-by-Design Lakehouse. Data Contracts, Versioning, and Transactional Pipelines for Humans and Agents

**Authors:** Weiming Sheng, Jinlang Wang, Manuel Barros, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02335v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02335v1)

**Summary:** Lakehouses are the default cloud platform for analytics and AI, but they become unsafe when untrusted actors concurrently operate on production data: upstream-downstream mismatches surface only at runtime, and multi-table pipelines can leak partial effects. Inspired by software engineering, we design Bauplan, a code-first lakehouse that aims to make (most) illegal states unrepresentable using familiar abstractions. Bauplan acts along three axes: typed table contracts to make pipeline boundaries ...

---

### 36. VQ-Style: Disentangling Style and Content in Motion with Residual Quantized Representations

**Authors:** Fatemeh Zargarbashi, Dhruv Agrawal, Jakob Buhmann, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02334v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02334v1)

**Summary:** Human motion data is inherently rich and complex, containing both semantic content and subtle stylistic features that are challenging to model. We propose a novel method for effective disentanglement of the style and content in human motion data to facilitate style transfer. Our approach is guided by the insight that content corresponds to coarse motion attributes while style captures the finer, expressive details. To model this hierarchy, we employ Residual Vector Quantized Variational Autoenco...

---

### 37. TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour

**Authors:** Shaoting Zhu, Baijun Ye, Jiaxuan Wang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02331v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02331v1)

**Summary:** Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics. Although general locomotion policies demonstrate capabilities across broad terrain distributions, they often struggle with arbitrary and highly challenging environments. To overcome this limitation, we propose a real-to-sim-to-real framework that leverages rapid test-time training (TTT) on novel terrains, significantly enhancing the robot's capability to traverse extremely difficult geometries....

---

### 38. A Large-Scale Dataset for Molecular Structure-Language Description via a Rule-Regularized Method

**Authors:** Feiyang Cai, Guijuan He, Yi Hu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02320v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02320v1)

**Summary:** Molecular function is largely determined by structure. Accurately aligning molecular structure with natural language is therefore essential for enabling large language models (LLMs) to reason about downstream chemical tasks. However, the substantial cost of human annotation makes it infeasible to construct large-scale, high-quality datasets of structure-grounded descriptions. In this work, we propose a fully automated annotation framework for generating precise molecular structure descriptions a...

---

### 39. Interpreting and Controlling LLM Reasoning through Integrated Policy Gradient

**Authors:** Changming Li, Kaixing Zhang, Haoyun Xu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02313v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02313v1)

**Summary:** Large language models (LLMs) demonstrate strong reasoning abilities in solving complex real-world problems. Yet, the internal mechanisms driving these complex reasoning behaviors remain opaque. Existing interpretability approaches targeting reasoning either identify components (e.g., neurons) correlated with special textual patterns, or rely on human-annotated contrastive pairs to derive control vectors. Consequently, current methods struggle to precisely localize complex reasoning mechanisms or...

---

### 40. FragmentFlow: Scalable Transition State Generation for Large Molecules

**Authors:** Ron Shprints, Peter Holderrieth, Juno Nam, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02310v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02310v1)

**Summary:** Transition states (TSs) are central to understanding and quantitatively predicting chemical reactivity and reaction mechanisms. Although traditional TS generation methods are computationally expensive, recent generative modeling approaches have enabled chemically meaningful TS prediction for relatively small molecules. However, these methods fail to generalize to practically relevant reaction substrates because of distribution shifts induced by increasing molecular sizes. Furthermore, TS geometr...

---

### 41. Spark: Modular Spiking Neural Networks

**Authors:** Mario Franco, Carlos Gershenson

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02306v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02306v1)

**Summary:** Nowadays, neural networks act as a synonym for artificial intelligence. Present neural network models, although remarkably powerful, are inefficient both in terms of data and energy. Several alternative forms of neural networks have been proposed to address some of these problems. Specifically, spiking neural networks are suitable for efficient hardware implementations. However, effective learning algorithms for spiking networks remain elusive, although it is suspected that effective plasticity ...

---

### 42. Position: Explaining Behavioral Shifts in Large Language Models Requires a Comparative Approach

**Authors:** Martino Ciaperoni, Marzio Di Vece, Luca Pappalardo, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02304v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02304v1)

**Summary:** Large-scale foundation models exhibit behavioral shifts: intervention-induced behavioral changes that appear after scaling, fine-tuning, reinforcement learning or in-context learning. While investigating these phenomena have recently received attention, explaining their appearance is still overlooked. Classic explainable AI (XAI) methods can surface failures at a single checkpoint of a model, but they are structurally ill-suited to justify what changed internally across different checkpoints and...

---

### 43. Advancing General-Purpose Reasoning Models with Modular Gradient Surgery

**Authors:** Min Cai, Yu Liang, Longzheng Wang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02301v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02301v1)

**Summary:** Reinforcement learning (RL) has played a central role in recent advances in large reasoning models (LRMs), yielding strong gains in verifiable and open-ended reasoning. However, training a single general-purpose LRM across diverse domains remains challenging due to pronounced domain heterogeneity. Through a systematic study of two widely used strategies, Sequential RL and Mixed RL, we find that both incur substantial cross-domain interference at the behavioral and gradient levels, resulting in l...

---

### 44. Decoupling Generalizability and Membership Privacy Risks in Neural Networks

**Authors:** Xingli Fang, Jung-Eun Kim

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02296v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02296v1)

**Summary:** A deep learning model usually has to sacrifice some utilities when it acquires some other abilities or characteristics. Privacy preservation has such trade-off relationships with utilities. The loss disparity between various defense approaches implies the potential to decouple generalizability and privacy risks to maximize privacy gain. In this paper, we identify that the model's generalization and privacy risks exist in different regions in deep neural network architectures. Based on the observ...

---

### 45. Hallucination or Creativity: How to Evaluate AI-Generated Scientific Stories?

**Authors:** Alex Argese, Pasquale Lisena, Raphaël Troncy

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02290v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02290v1)

**Summary:** Generative AI can turn scientific articles into narratives for diverse audiences, but evaluating these stories remains challenging. Storytelling demands abstraction, simplification, and pedagogical creativity-qualities that are not often well-captured by standard summarization metrics. Meanwhile, factual hallucinations are critical in scientific contexts, yet, detectors often misclassify legitimate narrative reformulations or prove unstable when creativity is involved. In this work, we propose S...

---

### 46. An Optimization Method for Autoregressive Time Series Forecasting

**Authors:** Zheng Li, Jerry Cheng, Huanying Gu

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02288v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02288v1)

**Summary:** Current time-series forecasting models are primarily based on transformer-style neural networks. These models achieve long-term forecasting mainly by scaling up the model size rather than through genuinely autoregressive (AR) rollout. From the perspective of large language model training, the traditional training process for time-series forecasting models ignores temporal causality. In this paper, we propose a novel training method for time-series forecasting that enforces two key properties: (1...

---

### 47. DFKI-Speech System for WildSpoof Challenge: A robust framework for SASV In-the-Wild

**Authors:** Arnab Das, Yassine El Kheir, Enes Erdem Erdogan, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02286v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02286v1)

**Summary:** This paper presents the DFKI-Speech system developed for the WildSpoof Challenge under the Spoofing aware Automatic Speaker Verification (SASV) track. We propose a robust SASV framework in which a spoofing detector and a speaker verification (SV) network operate in tandem. The spoofing detector employs a self-supervised speech embedding extractor as the frontend, combined with a state-of-the-art graph neural network backend. In addition, a top-3 layer based mixture-of-experts (MoE) is used to fu...

---

### 48. Backpropagation as Physical Relaxation: Exact Gradients in Finite Time

**Authors:** Antonino Emanuele Scurria

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02281v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02281v1)

**Summary:** Backpropagation, the foundational algorithm for training neural networks, is typically understood as a symbolic computation that recursively applies the chain rule. We show it emerges exactly as the finite-time relaxation of a physical dynamical system. By formulating feedforward inference as a continuous-time process and applying Lagrangian theory of non-conservative systems to handle asymmetric interactions, we derive a global energy functional on a doubled state space encoding both activation...

---

### 49. RACA: Representation-Aware Coverage Criteria for LLM Safety Testing

**Authors:** Zeming Wei, Zhixin Zhang, Chengcan Wu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02280v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02280v1)

**Summary:** Recent advancements in LLMs have led to significant breakthroughs in various AI applications. However, their sophisticated capabilities also introduce severe safety concerns, particularly the generation of harmful content through jailbreak attacks. Current safety testing for LLMs often relies on static datasets and lacks systematic criteria to evaluate the quality and adequacy of these tests. While coverage criteria have been effective for smaller neural networks, they are not directly applicabl...

---

### 50. Bridging the Sim-to-Real Gap with multipanda ros2: A Real-Time ROS2 Framework for Multimanual Systems

**Authors:** Jon Škerlj, Seongjin Bien, Abdeldjallil Naceri, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02269v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02269v1)

**Summary:** We present $multipanda\_ros2$, a novel open-source ROS2 architecture for multi-robot control of Franka Robotics robots. Leveraging ros2 control, this framework provides native ROS2 interfaces for controlling any number of robots from a single process. Our core contributions address key challenges in real-time torque control, including interaction control and robot-environment modeling. A central focus of this work is sustaining a 1kHz control frequency, a necessity for real-time control and a mi...

---

## cs.CL

**50 papers**

### 1. Reward-free Alignment for Conflicting Objectives

**Authors:** Peter Chen, Xiaopeng Li, Xi Chen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02495v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02495v1)

**Summary:** Direct alignment methods are increasingly used to align large language models (LLMs) with human preferences. However, many real-world alignment problems involve multiple conflicting objectives, where naive aggregation of preferences can lead to unstable training and poor trade-offs. In particular, weighted loss methods may fail to identify update directions that simultaneously improve all objectives, and existing multi-objective approaches often rely on explicit reward models, introducing additi...

---

### 2. RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System

**Authors:** Yinjie Wang, Tianbao Xie, Ke Shen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02488v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02488v1)

**Summary:** We propose RLAnything, a reinforcement learning framework that dynamically forges environment, policy, and reward models through closed-loop optimization, amplifying learning signals and strengthening the overall RL system for any LLM or agentic scenarios. Specifically, the policy is trained with integrated feedback from step-wise and outcome signals, while the reward model is jointly optimized via consistency feedback, which in turn further improves policy training. Moreover, our theory-motivat...

---

### 3. RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents

**Authors:** Jialiang Zhu, Gongrui Zhang, Xiaolong Ma, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02486v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02486v1)

**Summary:** LLM-based deep research agents are largely built on the ReAct framework. This linear design makes it difficult to revisit earlier states, branch into alternative search directions, or maintain global awareness under long contexts, often leading to local optima, redundant exploration, and inefficient search. We propose Re-TRAC, an agentic framework that performs cross-trajectory exploration by generating a structured state representation after each trajectory to summarize evidence, uncertainties,...

---

### 4. Training LLMs for Divide-and-Conquer Reasoning Elevates Test-Time Scalability

**Authors:** Xiao Liang, Zhong-Zhi Li, Zhenghao Lin, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02477v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02477v1)

**Summary:** Large language models (LLMs) have demonstrated strong reasoning capabilities through step-by-step chain-of-thought (CoT) reasoning. Nevertheless, at the limits of model capability, CoT often proves insufficient, and its strictly sequential nature constrains test-time scalability. A potential alternative is divide-and-conquer (DAC) reasoning, which decomposes a complex problem into subproblems to facilitate more effective exploration of the solution. Although promising, our analysis reveals a fun...

---

### 5. MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

**Authors:** Haozhen Zhang, Quanyu Long, Jianzhu Bao, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02474v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02474v1)

**Summary:** Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory. These fixed procedures hard-code human priors about what to store and how to revise memory, making them rigid under diverse interaction patterns and inefficient on long histories. To this end, we present \textbf{MemSkill}, which reframes these operations as learnable and evolvable memory skills, structured and reusable routines for extracting, consolidating, and pru...

---

### 6. SPARKLING: Balancing Signal Preservation and Symmetry Breaking for Width-Progressive Learning

**Authors:** Qifan Yu, Xinyu Ma, Zhijian Zhuo, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02472v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02472v1)

**Summary:** Progressive Learning (PL) reduces pre-training computational overhead by gradually increasing model scale. While prior work has extensively explored depth expansion, width expansion remains significantly understudied, with the few existing methods limited to the early stages of training. However, expanding width during the mid-stage is essential for maximizing computational savings, yet it remains a formidable challenge due to severe training instabilities. Empirically, we show that naive initia...

---

### 7. Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts

**Authors:** Aiden Yiliu Li, Xinyue Hao, Shilong Liu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02468v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02468v1)

**Summary:** Despite advances in multimodal large language models, autonomous web agents still struggle to reliably execute long-horizon tasks on complex and dynamic web interfaces. Existing agents often suffer from inaccurate element grounding, the absence of site-specific procedural knowledge, and unstable long-term task tracking and memory, particularly when operating over complex Document Object Model structures. To address these limitations, we introduce Avenir-Web, a web agent that achieves a new open-...

---

### 8. Indications of Belief-Guided Agency and Meta-Cognitive Monitoring in Large Language Models

**Authors:** Noam Steinmetz Yalon, Ariel Goldstein, Liad Mudrik, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02467v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02467v1)

**Summary:** Rapid advancements in large language models (LLMs) have sparked the question whether these models possess some form of consciousness. To tackle this challenge, Butlin et al. (2023) introduced a list of indicators for consciousness in artificial systems based on neuroscientific theories. In this work, we evaluate a key indicator from this list, called HOT-3, which tests for agency guided by a general belief-formation and action selection system that updates beliefs based on meta-cognitive monitor...

---

### 9. From Directions to Regions: Decomposing Activations in Language Models via Local Geometry

**Authors:** Or Shafran, Shaked Ronen, Omri Fahn, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02464v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02464v1)

**Summary:** Activation decomposition methods in language models are tightly coupled to geometric assumptions on how concepts are realized in activation space. Existing approaches search for individual global directions, implicitly assuming linear separability, which overlooks concepts with nonlinear or multi-dimensional structure. In this work, we leverage Mixture of Factor Analyzers (MFA) as a scalable, unsupervised alternative that models the activation space as a collection of Gaussian regions with their...

---

### 10. Abstract Activation Spaces for Content-Invariant Reasoning in Large Language Models

**Authors:** Gabriele Maraia, Marco Valentino, Fabio Massimo Zanzotto, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02462v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02462v1)

**Summary:** Large Language Models (LLMs) often struggle with deductive judgment in syllogistic reasoning, systematically conflating semantic plausibility with formal validity a phenomenon known as content effect. This bias persists even when models generate step-wise explanations, indicating that intermediate rationales may inherit the same semantic shortcuts that affect answers. Recent approaches propose mitigating this issue by increasing inference-time structural constraints, either by encouraging abstra...

---

### 11. Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction

**Authors:** Han Bao, Zheyuan Zhang, Pengcheng Jing, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02455v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02455v1)

**Summary:** As Large Language Models transition to autonomous agents, user inputs frequently violate cooperative assumptions (e.g., implicit intent, missing parameters, false presuppositions, or ambiguous expressions), creating execution risks that text-only evaluations do not capture. Existing benchmarks typically assume well-specified instructions or restrict evaluation to text-only, single-turn clarification, and thus do not measure multi-turn disambiguation under grounded execution risk. We introduce \t...

---

### 12. Large Language Models for Mental Health: A Multilingual Evaluation

**Authors:** Nishat Raihan, Sadiya Sayara Chowdhury Puspo, Ana-Maria Bucur, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02440v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02440v1)

**Summary:** Large Language Models (LLMs) have remarkable capabilities across NLP tasks. However, their performance in multilingual contexts, especially within the mental health domain, has not been thoroughly explored. In this paper, we evaluate proprietary and open-source LLMs on eight mental health datasets in various languages, as well as their machine-translated (MT) counterparts. We compare LLM performance in zero-shot, few-shot, and fine-tuned settings against conventional NLP baselines that do not em...

---

### 13. Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank

**Authors:** Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02414v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02414v1)

**Summary:** Timely and accurate identification of student misconceptions is key to improving learning outcomes and pre-empting the compounding of student errors. However, this task is highly dependent on the effort and intuition of the teacher. In this work, we present a novel approach for detecting misconceptions from student-tutor dialogues using large language models (LLMs). First, we use a fine-tuned LLM to generate plausible misconceptions, and then retrieve the most promising candidates among these us...

---

### 14. ROG: Retrieval-Augmented LLM Reasoning for Complex First-Order Queries over Knowledge Graphs

**Authors:** Ziyan Zhang, Chao Wang, Zhuo Chen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02382v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02382v1)

**Summary:** Answering first-order logic (FOL) queries over incomplete knowledge graphs (KGs) is difficult, especially for complex query structures that compose projection, intersection, union, and negation. We propose ROG, a retrieval-augmented framework that combines query-aware neighborhood retrieval with large language model (LLM) chain-of-thought reasoning. ROG decomposes a multi-operator query into a sequence of single-operator sub-queries and grounds each step in compact, query-relevant neighborhood e...

---

### 15. From Sycophancy to Sensemaking: Premise Governance for Human-AI Decision Making

**Authors:** Raunak Jain, Mudita Khurana, John Stephens, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02378v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02378v1)

**Summary:** As LLMs expand from assistance to decision support, a dangerous pattern emerges: fluent agreement without calibrated judgment. Low-friction assistants can become sycophantic, baking in implicit assumptions and pushing verification costs onto experts, while outcomes arrive too late to serve as reward signals. In deep-uncertainty decisions (where objectives are contested and reversals are costly), scaling fluent agreement amplifies poor commitments faster than it builds expertise. We argue reliabl...

---

### 16. Proof-RM: A Scalable and Generalizable Reward Model for Math Proof

**Authors:** Haotong Yang, Zitong Wang, Shijia Kang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02377v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02377v1)

**Summary:** While Large Language Models (LLMs) have demonstrated strong math reasoning abilities through Reinforcement Learning with *Verifiable Rewards* (RLVR), many advanced mathematical problems are proof-based, with no guaranteed way to determine the authenticity of a proof by simple answer matching. To enable automatic verification, a Reward Model (RM) capable of reliably evaluating full proof processes is required. In this work, we design a *scalable* data-construction pipeline that, with minimal huma...

---

### 17. Automated Multiple Mini Interview (MMI) Scoring

**Authors:** Ryan Huynh, Frank Guerin, Alison Callwood

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02360v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02360v1)

**Summary:** Assessing soft skills such as empathy, ethical judgment, and communication is essential in competitive selection processes, yet human scoring is often inconsistent and biased. While Large Language Models (LLMs) have improved Automated Essay Scoring (AES), we show that state-of-the-art rationale-based fine-tuning methods struggle with the abstract, context-dependent nature of Multiple Mini-Interviews (MMIs), missing the implicit signals embedded in candidate narratives. We introduce a multi-agent...

---

### 18. Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics

**Authors:** Ziwen Xu, Chenyan Wu, Hengyu Sun, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02343v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02343v1)

**Summary:** Methods for controlling large language models (LLMs), including local weight fine-tuning, LoRA-based adaptation, and activation-based interventions, are often studied in isolation, obscuring their connections and making comparison difficult. In this work, we present a unified view that frames these interventions as dynamic weight updates induced by a control signal, placing them within a single conceptual framework. Building on this view, we propose a unified preference-utility analysis that sep...

---

### 19. Language Steering for Multilingual In-Context Learning

**Authors:** Neeraja Kirtane, Kuan-Hao Huang

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02326v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02326v1)

**Summary:** While multilingual large language models have gained widespread adoption, their performance on non-English languages remains substantially inferior to English. This disparity is particularly evident in in-context learning scenarios, where providing demonstrations in English but testing on non-English inputs leads to significant performance degradation. In this paper, we hypothesize that LLMs develop a universal semantic space for understanding languages, where different languages are encoded as ...

---

### 20. A Large-Scale Dataset for Molecular Structure-Language Description via a Rule-Regularized Method

**Authors:** Feiyang Cai, Guijuan He, Yi Hu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02320v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02320v1)

**Summary:** Molecular function is largely determined by structure. Accurately aligning molecular structure with natural language is therefore essential for enabling large language models (LLMs) to reason about downstream chemical tasks. However, the substantial cost of human annotation makes it infeasible to construct large-scale, high-quality datasets of structure-grounded descriptions. In this work, we propose a fully automated annotation framework for generating precise molecular structure descriptions a...

---

### 21. The Shape of Beliefs: Geometry, Dynamics, and Interventions along Representation Manifolds of Language Models' Posteriors

**Authors:** Raphaël Sarfati, Eric Bigelow, Daniel Wurgaft, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02315v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02315v1)

**Summary:** Large language models (LLMs) represent prompt-conditioned beliefs (posteriors over answers and claims), but we lack a mechanistic account of how these beliefs are encoded in representation space, how they update with new evidence, and how interventions reshape them. We study a controlled setting in which Llama-3.2 generates samples from a normal distribution by implicitly inferring its parameters (mean and standard deviation) given only samples from the distribution in context. We find represent...

---

### 22. Interpreting and Controlling LLM Reasoning through Integrated Policy Gradient

**Authors:** Changming Li, Kaixing Zhang, Haoyun Xu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02313v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02313v1)

**Summary:** Large language models (LLMs) demonstrate strong reasoning abilities in solving complex real-world problems. Yet, the internal mechanisms driving these complex reasoning behaviors remain opaque. Existing interpretability approaches targeting reasoning either identify components (e.g., neurons) correlated with special textual patterns, or rely on human-annotated contrastive pairs to derive control vectors. Consequently, current methods struggle to precisely localize complex reasoning mechanisms or...

---

### 23. Advancing General-Purpose Reasoning Models with Modular Gradient Surgery

**Authors:** Min Cai, Yu Liang, Longzheng Wang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02301v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02301v1)

**Summary:** Reinforcement learning (RL) has played a central role in recent advances in large reasoning models (LRMs), yielding strong gains in verifiable and open-ended reasoning. However, training a single general-purpose LRM across diverse domains remains challenging due to pronounced domain heterogeneity. Through a systematic study of two widely used strategies, Sequential RL and Mixed RL, we find that both incur substantial cross-domain interference at the behavioral and gradient levels, resulting in l...

---

### 24. Hallucination or Creativity: How to Evaluate AI-Generated Scientific Stories?

**Authors:** Alex Argese, Pasquale Lisena, Raphaël Troncy

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02290v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02290v1)

**Summary:** Generative AI can turn scientific articles into narratives for diverse audiences, but evaluating these stories remains challenging. Storytelling demands abstraction, simplification, and pedagogical creativity-qualities that are not often well-captured by standard summarization metrics. Meanwhile, factual hallucinations are critical in scientific contexts, yet, detectors often misclassify legitimate narrative reformulations or prove unstable when creativity is involved. In this work, we propose S...

---

### 25. Cross-Lingual Stability of LLM Judges Under Controlled Generation: Evidence from Finno-Ugric Languages

**Authors:** Isaac Chung, Linda Freienthal

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02287v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02287v1)

**Summary:** Cross-lingual evaluation of large language models (LLMs) typically conflates two sources of variance: genuine model performance differences and measurement instability. We investigate evaluation reliability by holding generation conditions constant while varying target language. Using synthetic customer-support dialogues generated with identical parameters across Estonian, Finnish, and Hungarian, we test whether automatic metrics and LLM-as-a-judge scoring produce stable model rankings across th...

---

### 26. Statistical Learning Theory in Lean 4: Empirical Processes from Scratch

**Authors:** Yuanhe Zhang, Jason D. Lee, Fanghui Liu

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02285v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02285v1)

**Summary:** We present the first comprehensive Lean 4 formalization of statistical learning theory (SLT) grounded in empirical process theory. Our end-to-end formal infrastructure implement the missing contents in latest Lean 4 Mathlib library, including a complete development of Gaussian Lipschitz concentration, the first formalization of Dudley's entropy integral theorem for sub-Gaussian processes, and an application to least-squares (sparse) regression with a sharp rate. The project was carried out using...

---

### 27. RACA: Representation-Aware Coverage Criteria for LLM Safety Testing

**Authors:** Zeming Wei, Zhixin Zhang, Chengcan Wu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02280v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02280v1)

**Summary:** Recent advancements in LLMs have led to significant breakthroughs in various AI applications. However, their sophisticated capabilities also introduce severe safety concerns, particularly the generation of harmful content through jailbreak attacks. Current safety testing for LLMs often relies on static datasets and lacks systematic criteria to evaluate the quality and adequacy of these tests. While coverage criteria have been effective for smaller neural networks, they are not directly applicabl...

---

### 28. Kimi K2.5: Visual Agentic Intelligence

**Authors:**  Kimi Team, Tongtong Bai, Yifan Bai, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02276v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02276v1)

**Summary:** We introduce Kimi K2.5, an open-source multimodal agentic model designed to advance general agentic intelligence. K2.5 emphasizes the joint optimization of text and vision so that two modalities enhance each other. This includes a series of techniques such as joint text-vision pre-training, zero-vision SFT, and joint text-vision reinforcement learning. Building on this multimodal foundation, K2.5 introduces Agent Swarm, a self-directed parallel agent orchestration framework that dynamically deco...

---

### 29. dziribot: rag based intelligent conversational agent for algerian arabic dialect

**Authors:** El Batoul Bechiri, Dihia Lanasri

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02270v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02270v1)

**Summary:** The rapid digitalization of customer service has intensified the demand for conversational agents capable of providing accurate and natural interactions. In the Algerian context, this is complicated by the linguistic complexity of Darja, a dialect characterized by non-standardized orthography, extensive code-switching with French, and the simultaneous use of Arabic and Latin (Arabizi) scripts. This paper introduces DziriBOT, a hybrid intelligent conversational agent specifically engineered to ov...

---

### 30. OpenSeal: Good, Fast, and Cheap Construction of an Open-Source Southeast Asian LLM via Parallel Data

**Authors:** Tan Sang Nguyen, Muhammad Reza Qorib, Hwee Tou Ng

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02266v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02266v1)

**Summary:** Large language models (LLMs) have proven to be effective tools for a wide range of natural language processing (NLP) applications. Although many LLMs are multilingual, most remain English-centric and perform poorly on low-resource languages. Recently, several Southeast Asia-focused LLMs have been developed, but none are truly open source, as they do not publicly disclose their training data. Truly open-source models are important for transparency and for enabling a deeper and more precise unders...

---

### 31. OmniCode: A Benchmark for Evaluating Software Engineering Agents

**Authors:** Atharv Sonwane, Eng-Shen Tu, Wei-Chung Lu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02262v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02262v1)

**Summary:** LLM-powered coding agents are redefining how real-world software is developed. To drive the research towards better coding agents, we require challenging benchmarks that can rigorously evaluate the ability of such agents to perform various software engineering tasks. However, popular coding benchmarks such as HumanEval and SWE-Bench focus on narrowly scoped tasks such as competition programming and patch generation. In reality, software engineers have to handle a broader set of tasks for real-wo...

---

### 32. Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models

**Authors:** Hao Wang, Hao Gu, Hongming Piao, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02244v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02244v1)

**Summary:** The standard post-training recipe for large reasoning models, supervised fine-tuning followed by reinforcement learning (SFT-then-RL), may limit the benefits of the RL stage: while SFT imitates expert demonstrations, it often causes overconfidence and reduces generation diversity, leaving RL with a narrowed solution space to explore. Adding entropy regularization during SFT is not a cure-all; it tends to flatten token distributions toward uniformity, increasing entropy without improving meaningf...

---

### 33. Using Correspondence Patterns to Identify Irregular Words in Cognate sets Through Leave-One-Out Validation

**Authors:** Frederic Blum, Johann-Mattis List

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02221v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02221v1)

**Summary:** Regular sound correspondences constitute the principal evidence in historical language comparison. Despite the heuristic focus on regularity, it is often more an intuitive judgement than a quantified evaluation, and irregularity is more common than expected from the Neogrammarian model. Given the recent progress of computational methods in historical linguistics and the increased availability of standardized lexical data, we are now able to improve our workflows and provide such a quantitative e...

---

### 34. Am I More Pointwise or Pairwise? Revealing Position Bias in Rubric-Based LLM-as-a-Judge

**Authors:** Yuzheng Xu, Tosho Hirasawa, Tadashi Kozuno, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02219v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02219v1)

**Summary:** Large language models (LLMs) are now widely used to evaluate the quality of text, a field commonly referred to as LLM-as-a-judge. While prior works mainly focus on point-wise and pair-wise evaluation paradigms. Rubric-based evaluation, where LLMs select a score from multiple rubrics, has received less analysis. In this work, we show that rubric-based evaluation implicitly resembles a multi-choice setting and therefore has position bias: LLMs prefer score options appearing at specific positions i...

---

### 35. Towards AI Evaluation in Domain-Specific RAG Systems: The AgriHubi Case Study

**Authors:** Md. Toufique Hasan, Ayman Asad Khan, Mika Saari, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02208v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02208v1)

**Summary:** Large language models show promise for knowledge-intensive domains, yet their use in agriculture is constrained by weak grounding, English-centric training data, and limited real-world evaluation. These issues are amplified for low-resource languages, where high-quality domain documentation exists but remains difficult to access through general-purpose models. This paper presents AgriHubi, a domain-adapted retrieval-augmented generation (RAG) system for Finnish-language agricultural decision sup...

---

### 36. Sinhala Physical Common Sense Reasoning Dataset for Global PIQA

**Authors:** Nisansa de Silva, Surangika Ranathunga

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02207v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02207v1)

**Summary:** This paper presents the first-ever Sinhala physical common sense reasoning dataset created as part of Global PIQA. It contains 110 human-created and verified data samples, where each sample consists of a prompt, the corresponding correct answer, and a wrong answer. Most of the questions refer to the Sri Lankan context, where Sinhala is an official language.

---

### 37. More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression

**Authors:** Aryan Sood, Tanvi Sharma, Vansh Agrawal

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02199v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02199v1)

**Summary:** While Large Language Models (LLMs) can theoretically support extensive context windows, their actual deployment is constrained by the linear growth of Key-Value (KV) cache memory. Prevailing compression strategies mitigate this through various pruning mechanisms, yet trade-off semantic recall for memory efficiency. In this work, we present LASER-KV (Layer Accumulated Selection with Exact-LSH Recall), a framework designed to test the limits of KV compression under a strict accumulative budgeting ...

---

### 38. Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models

**Authors:** Yu Zeng, Wenxuan Huang, Zhen Fang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02185v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02185v1)

**Summary:** Multimodal Large Language Models (MLLMs) have advanced VQA and now support Vision-DeepResearch systems that use search engines for complex visual-textual fact-finding. However, evaluating these visual and textual search abilities is still difficult, and existing benchmarks have two major limitations. First, existing benchmarks are not visual search-centric: answers that should require visual search are often leaked through cross-textual cues in the text questions or can be inferred from the prio...

---

### 39. Evaluating Metalinguistic Knowledge in Large Language Models across the World's Languages

**Authors:** Tjaša Arčon, Matej Klemen, Marko Robnik-Šikonja, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02182v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02182v1)

**Summary:** Large language models (LLMs) are routinely evaluated on language use tasks, yet their knowledge of linguistic structure remains poorly understood. Existing linguistic benchmarks typically focus on narrow phenomena, emphasize high-resource languages, and rarely evaluate metalinguistic knowledge-explicit reasoning about language structure rather than language use. Using accuracy and macro F1, together with majority-class and chance baselines, we analyse overall performance and examine variation by...

---

### 40. AR-MAP: Are Autoregressive Large Language Models Implicit Teachers for Diffusion Large Language Models?

**Authors:** Liang Lin, Feng Xiong, Zengbin Wang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02178v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02178v1)

**Summary:** Diffusion Large Language Models (DLLMs) have emerged as a powerful alternative to autoregressive models, enabling parallel token generation across multiple positions. However, preference alignment of DLLMs remains challenging due to high variance introduced by Evidence Lower Bound (ELBO)-based likelihood estimation. In this work, we propose AR-MAP, a novel transfer learning framework that leverages preference-aligned autoregressive LLMs (AR-LLMs) as implicit teachers for DLLM alignment. We revea...

---

### 41. D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use

**Authors:** Bowen Xu, Shaoyu Wu, Hao Jiang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02160v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02160v1)

**Summary:** Effective tool use and reasoning are essential capabilities for large reasoning models~(LRMs) to address complex real-world problems. Through empirical analysis, we identify that current LRMs lack the capability of sub-task decomposition in complex tool use scenarios, leading to Lazy Reasoning. To address this, we propose a two-stage training framework D-CORE~(\underline{\textbf{D}}ecomposing tasks and \underline{\textbf{Co}}mposing \underline{\textbf{Re}}asoning processes) that first incentiviz...

---

### 42. Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing

**Authors:** Lingkun Long, Yushi Huang, Shihao Bai, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02159v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02159v1)

**Summary:** Diffusion Large Language Models (dLLMs) deliver strong long-context processing capability in a non-autoregressive decoding paradigm. However, the considerable computational cost of bidirectional full attention limits the inference efficiency. Although sparse attention is promising, existing methods remain ineffective. This stems from the need to estimate attention importance for tokens yet to be decoded, while the unmasked token positions are unknown during diffusion. In this paper, we present F...

---

### 43. Revisiting Adaptive Rounding with Vectorized Reparameterization for LLM Quantization

**Authors:** Yuli Zhou, Qingxuan Chen, Luca Benini, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02151v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02151v1)

**Summary:** Adaptive Rounding has emerged as an alternative to round-to-nearest (RTN) for post-training quantization by enabling cross-element error cancellation. Yet, dense and element-wise rounding matrices are prohibitively expensive for billion-parameter large language models (LLMs). We revisit adaptive rounding from an efficiency perspective and propose VQRound, a parameter-efficient optimization framework that reparameterizes the rounding matrix into a compact codebook. Unlike low-rank alternatives, V...

---

### 44. Learning Generative Selection for Best-of-N

**Authors:** Shubham Toshniwal, Aleksander Ficek, Siddhartha Jain, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02143v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02143v1)

**Summary:** Scaling test-time compute via parallel sampling can substantially improve LLM reasoning, but is often limited by Best-of-N selection quality. Generative selection methods, such as GenSelect, address this bottleneck, yet strong selection performance remains largely limited to large models. We show that small reasoning models can acquire strong GenSelect capabilities through targeted reinforcement learning. To this end, we synthesize selection tasks from large-scale math and code instruction datas...

---

### 45. Quantifying the Gap between Understanding and Generation within Unified Multimodal Models

**Authors:** Chenlong Wang, Yuhang Chen, Zhihan Hu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02140v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02140v1)

**Summary:** Recent advances in unified multimodal models (UMM) have demonstrated remarkable progress in both understanding and generation tasks. However, whether these two capabilities are genuinely aligned and integrated within a single model remains unclear. To investigate this question, we introduce GapEval, a bidirectional benchmark designed to quantify the gap between understanding and generation capabilities, and quantitatively measure the cognitive coherence of the two "unified" directions. Each ques...

---

### 46. EvoMU: Evolutionary Machine Unlearning

**Authors:** Pawel Batorski, Paul Swoboda

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02139v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02139v1)

**Summary:** Machine unlearning aims to unlearn specified training data (e.g. sensitive or copyrighted material). A prominent approach is to fine-tune an existing model with an unlearning loss that retains overall utility. The space of suitable unlearning loss functions is vast, making the search for an optimal loss function daunting. Additionally, there might not even exist a universally optimal loss function: differences in the structure and overlap of the forget and retain data can cause a loss to work we...

---

### 47. Understanding the Reversal Curse Mitigation in Masked Diffusion Models through Attention and Training Dynamics

**Authors:** Sangwoo Shin, BumJun Kim, Kyelim Lee, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02133v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02133v1)

**Summary:** Autoregressive language models (ARMs) suffer from the reversal curse: after learning that "$A$ is $B$", they often fail on the reverse query "$B$ is $A$". Masked diffusion-based language models (MDMs) exhibit this failure in a much weaker form, but the underlying reason has remained unclear. A common explanation attributes this mitigation to the any-order training objective. However, observing "[MASK] is $B$" during training does not necessarily teach the model to handle the reverse prompt "$B$ ...

---

### 48. There Is More to Refusal in Large Language Models than a Single Direction

**Authors:** Faaiz Joad, Majd Hawasly, Sabri Boughorbel, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02132v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02132v1)

**Summary:** Prior work argues that refusal in large language models is mediated by a single activation-space direction, enabling effective steering and ablation. We show that this account is incomplete. Across eleven categories of refusal and non-compliance, including safety, incomplete or unsupported requests, anthropomorphization, and over-refusal, we find that these refusal behaviors correspond to geometrically distinct directions in activation space. Yet despite this diversity, linear steering along any...

---

### 49. Unifying Masked Diffusion Models with Various Generation Orders and Beyond

**Authors:** Chunsan Hong, Sanghyun Lee, Jong Chul Ye

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02112v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02112v1)

**Summary:** Masked diffusion models (MDMs) are a potential alternative to autoregressive models (ARMs) for language generation, but generation quality depends critically on the generation order. Prior work either hard-codes an ordering (e.g., blockwise left-to-right) or learns an ordering policy for a pretrained MDM, which incurs extra cost and can yield suboptimal solutions due to the two-stage optimization. Motivated by this, we propose order-expressive masked diffusion model (OeMDM) for a broad class of ...

---

### 50. Out of the Memory Barrier: A Highly Memory Efficient Training System for LLMs with Million-Token Contexts

**Authors:** Wenhao Li, Daohai Yu, Gen Luo, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02108v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02108v1)

**Summary:** Training Large Language Models (LLMs) on long contexts is severely constrained by prohibitive GPU memory overhead, not training time. The primary culprits are the activations, whose memory footprints scale linearly with sequence length. We introduce OOMB, a highly memory-efficient training system that directly confronts this barrier. Our approach employs a chunk-recurrent training framework with on-the-fly activation recomputation, which maintains a constant activation memory footprint (O(1)) an...

---

## cs.CV

**50 papers**

### 1. PixelGen: Pixel Diffusion Beats Latent Diffusion with Perceptual Loss

**Authors:** Zehong Ma, Ruihan Xu, Shiliang Zhang

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02493v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02493v1)

**Summary:** Pixel diffusion generates images directly in pixel space in an end-to-end manner, avoiding the artifacts and bottlenecks introduced by VAEs in two-stage latent diffusion. However, it is challenging to optimize high-dimensional pixel manifolds that contain many perceptually irrelevant signals, leaving existing pixel diffusion methods lagging behind latent diffusion models. We propose PixelGen, a simple pixel diffusion framework with perceptual supervision. Instead of modeling the full image manif...

---

### 2. Multi-head automated segmentation by incorporating detection head into the contextual layer neural network

**Authors:** Edwin Kys, Febian Febian

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02471v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02471v1)

**Summary:** Deep learning based auto segmentation is increasingly used in radiotherapy, but conventional models often produce anatomically implausible false positives, or hallucinations, in slices lacking target structures. We propose a gated multi-head Transformer architecture based on Swin U-Net, augmented with inter-slice context integration and a parallel detection head, which jointly performs slice-level structure detection via a multi-layer perceptron and pixel-level segmentation through a context-enh...

---

### 3. MentisOculi: Revealing the Limits of Reasoning with Mental Imagery

**Authors:** Jana Zeller, Thaddäus Wiedemer, Fanfei Li, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02465v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02465v1)

**Summary:** Frontier models are transitioning from multimodal large language models (MLLMs) that merely ingest visual information to unified multimodal models (UMMs) capable of native interleaved generation. This shift has sparked interest in using intermediate visualizations as a reasoning aid, akin to human mental imagery. Central to this idea is the ability to form, maintain, and manipulate visual representations in a goal-oriented manner. To evaluate and probe this capability, we develop MentisOculi, a ...

---

### 4. RANKVIDEO: Reasoning Reranking for Text-to-Video Retrieval

**Authors:** Tyler Skow, Alexander Martin, Benjamin Van Durme, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02444v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02444v1)

**Summary:** Reranking is a critical component of modern retrieval systems, which typically pair an efficient first-stage retriever with a more expressive model to refine results. While large reasoning models have driven rapid progress in text-centric reranking, reasoning-based reranking for video retrieval remains underexplored. To address this gap, we introduce RANKVIDEO, a reasoning-based reranker for video retrieval that explicitly reasons over query-video pairs using video content to assess relevance. R...

---

### 5. UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing

**Authors:** Dianyi Wang, Chaofan Ma, Feng Han, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02437v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02437v1)

**Summary:** Unified multimodal models often struggle with complex synthesis tasks that demand deep reasoning, and typically treat text-to-image generation and image editing as isolated capabilities rather than interconnected reasoning steps. To address this, we propose UniReason, a unified framework that harmonizes these two tasks through a dual reasoning paradigm. We formulate generation as world knowledge-enhanced planning to inject implicit constraints, and leverage editing capabilities for fine-grained ...

---

### 6. SelvaMask: Segmenting Trees in Tropical Forests and Beyond

**Authors:** Simon-Olivier Duguay, Hugo Baudchon, Etienne Laliberté, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02426v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02426v1)

**Summary:** Tropical forests harbor most of the planet's tree biodiversity and are critical to global ecological balance. Canopy trees in particular play a disproportionate role in carbon storage and functioning of these ecosystems. Studying canopy trees at scale requires accurate delineation of individual tree crowns, typically performed using high-resolution aerial imagery. Despite advances in transformer-based models for individual tree crown segmentation, performance remains low in most forests, especia...

---

### 7. Catalyst: Out-of-Distribution Detection via Elastic Scaling

**Authors:** Abid Hassan, Tuan Ngo, Saad Shafiq, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02409v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02409v1)

**Summary:** Out-of-distribution (OOD) detection is critical for the safe deployment of deep neural networks. State-of-the-art post-hoc methods typically derive OOD scores from the output logits or penultimate feature vector obtained via global average pooling (GAP). We contend that this exclusive reliance on the logit or feature vector discards a rich, complementary signal: the raw channel-wise statistics of the pre-pooling feature map lost in GAP. In this paper, we introduce Catalyst, a post-hoc framework ...

---

### 8. ReasonEdit: Editing Vision-Language Models using Human Reasoning

**Authors:** Jiaxing Qiu, Kaihua Hou, Roxana Daneshjou, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02408v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02408v1)

**Summary:** Model editing aims to correct errors in large, pretrained models without altering unrelated behaviors. While some recent works have edited vision-language models (VLMs), no existing editors tackle reasoning-heavy tasks, which typically require humans and models to reason about images.We therefore propose ReasonEdit, the first VLM editor to let users explain their reasoning during editing, introducing a new, practical model editing setup. ReasonEdit continuously stores human reasoning in a codebo...

---

### 9. SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-body Manipulation

**Authors:** Mu Huang, Hui Wang, Kerui Ren, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02402v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02402v1)

**Summary:** Simulating deformable objects under rich interactions remains a fundamental challenge for real-to-sim robot manipulation, with dynamics jointly driven by environmental effects and robot actions. Existing simulators rely on predefined physics or data-driven dynamics without robot-conditioned control, limiting accuracy, stability, and generalization. This paper presents SoMA, a 3D Gaussian Splat simulator for soft-body manipulation. SoMA couples deformable dynamics, environmental forces, and robot...

---

### 10. Superman: Unifying Skeleton and Vision for Human Motion Perception and Generation

**Authors:** Xinshun Wang, Peiming Li, Ziyi Wang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02401v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02401v1)

**Summary:** Human motion analysis tasks, such as temporal 3D pose estimation, motion prediction, and motion in-betweening, play an essential role in computer vision. However, current paradigms suffer from severe fragmentation. First, the field is split between ``perception'' models that understand motion from video but only output text, and ``generation'' models that cannot perceive from raw visual input. Second, generative MLLMs are often limited to single-frame, static poses using dense, parametric SMPL m...

---

### 11. Infinite-World: Scaling Interactive World Models to 1000-Frame Horizons via Pose-Free Hierarchical Memory

**Authors:** Ruiqi Wu, Xuanhua He, Meng Cheng, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02393v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02393v1)

**Summary:** We propose Infinite-World, a robust interactive world model capable of maintaining coherent visual memory over 1000+ frames in complex real-world environments. While existing world models can be efficiently optimized on synthetic data with perfect ground-truth, they lack an effective training paradigm for real-world videos due to noisy pose estimations and the scarcity of viewpoint revisits. To bridge this gap, we first introduce a Hierarchical Pose-free Memory Compressor (HPMC) that recursively...

---

### 12. Personalized Image Generation via Human-in-the-loop Bayesian Optimization

**Authors:** Rajalaxmi Rajagopalan, Debottam Dutta, Yu-Lin Wei, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02388v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02388v1)

**Summary:** Imagine Alice has a specific image $x^\ast$ in her mind, say, the view of the street in which she grew up during her childhood. To generate that exact image, she guides a generative model with multiple rounds of prompting and arrives at an image $x^{p*}$. Although $x^{p*}$ is reasonably close to $x^\ast$, Alice finds it difficult to close that gap using language prompts. This paper aims to narrow this gap by observing that even after language has reached its limits, humans can still tell when a ...

---

### 13. Unified Personalized Reward Model for Vision Generation

**Authors:** Yibin Wang, Yuhang Zang, Feng Han, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02380v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02380v1)

**Summary:** Recent advancements in multimodal reward models (RMs) have significantly propelled the development of visual generation. Existing frameworks typically adopt Bradley-Terry-style preference modeling or leverage generative VLMs as judges, and subsequently optimize visual generation models via reinforcement learning. However, current RMs suffer from inherent limitations: they often follow a one-size-fits-all paradigm that assumes a monolithic preference distribution or relies on fixed evaluation rub...

---

### 14. Uncertainty-Aware Image Classification In Biomedical Imaging Using Spectral-normalized Neural Gaussian Processes

**Authors:** Uma Meleti, Jeffrey J. Nirschl

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02370v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02370v1)

**Summary:** Accurate histopathologic interpretation is key for clinical decision-making; however, current deep learning models for digital pathology are often overconfident and poorly calibrated in out-of-distribution (OOD) settings, which limit trust and clinical adoption. Safety-critical medical imaging workflows benefit from intrinsic uncertainty-aware properties that can accurately reject OOD input. We implement the Spectral-normalized Neural Gaussian Process (SNGP), a set of lightweight modifications t...

---

### 15. NAB: Neural Adaptive Binning for Sparse-View CT reconstruction

**Authors:** Wangduo Xie, Matthew B. Blaschko

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02356v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02356v1)

**Summary:** Computed Tomography (CT) plays a vital role in inspecting the internal structures of industrial objects. Furthermore, achieving high-quality CT reconstruction from sparse views is essential for reducing production costs. While classic implicit neural networks have shown promising results for sparse reconstruction, they are unable to leverage shape priors of objects. Motivated by the observation that numerous industrial objects exhibit rectangular structures, we propose a novel \textbf{N}eural \t...

---

### 16. Implicit neural representation of textures

**Authors:** Albert Kwok, Zheyuan Hu, Dounia Hammou

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02354v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02354v1)

**Summary:** Implicit neural representation (INR) has proven to be accurate and efficient in various domains. In this work, we explore how different neural networks can be designed as a new texture INR, which operates in a continuous manner rather than a discrete one over the input UV coordinate space. Through thorough experiments, we demonstrate that these INRs perform well in terms of image quality, with considerable memory usage and rendering inference time. We analyze the balance between these objectives...

---

### 17. Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics

**Authors:** Ziwen Xu, Chenyan Wu, Hengyu Sun, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02343v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02343v1)

**Summary:** Methods for controlling large language models (LLMs), including local weight fine-tuning, LoRA-based adaptation, and activation-based interventions, are often studied in isolation, obscuring their connections and making comparison difficult. In this work, we present a unified view that frames these interventions as dynamic weight updates induced by a control signal, placing them within a single conceptual framework. Building on this view, we propose a unified preference-utility analysis that sep...

---

### 18. LongVPO: From Anchored Cues to Self-Reasoning for Long-Form Video Preference Optimization

**Authors:** Zhenpeng Huang, Jiaqi Li, Zihan Jia, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02341v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02341v1)

**Summary:** We present LongVPO, a novel two-stage Direct Preference Optimization framework that enables short-context vision-language models to robustly understand ultra-long videos without any long-video annotations. In Stage 1, we synthesize preference triples by anchoring questions to individual short clips, interleaving them with distractors, and applying visual-similarity and question-specificity filtering to mitigate positional bias and ensure unambiguous supervision. We also approximate the reference...

---

### 19. VQ-Style: Disentangling Style and Content in Motion with Residual Quantized Representations

**Authors:** Fatemeh Zargarbashi, Dhruv Agrawal, Jakob Buhmann, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02334v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02334v1)

**Summary:** Human motion data is inherently rich and complex, containing both semantic content and subtle stylistic features that are challenging to model. We propose a novel method for effective disentanglement of the style and content in human motion data to facilitate style transfer. Our approach is guided by the insight that content corresponds to coarse motion attributes while style captures the finer, expressive details. To model this hierarchy, we employ Residual Vector Quantized Variational Autoenco...

---

### 20. Enhancing Indoor Occupancy Prediction via Sparse Query-Based Multi-Level Consistent Knowledge Distillation

**Authors:** Xiang Li, Yupeng Zheng, Pengfei Li, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02318v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02318v1)

**Summary:** Occupancy prediction provides critical geometric and semantic understanding for robotics but faces efficiency-accuracy trade-offs. Current dense methods suffer computational waste on empty voxels, while sparse query-based approaches lack robustness in diverse and complex indoor scenes. In this paper, we propose DiScene, a novel sparse query-based framework that leverages multi-level distillation to achieve efficient and robust occupancy prediction. In particular, our method incorporates two key ...

---

### 21. Segment to Focus: Guiding Latent Action Models in the Presence of Distractors

**Authors:** Hamza Adnan, Matthew T. Jackson, Alexey Zakharov

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02259v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02259v1)

**Summary:** Latent Action Models (LAMs) learn to extract action-relevant representations solely from raw observations, enabling reinforcement learning from unlabelled videos and significantly scaling available training data. However, LAMs face a critical challenge in disentangling action-relevant features from action-correlated noise (e.g., background motion). Failing to filter these distractors causes LAMs to capture spurious correlations and build sub-optimal latent action spaces. In this paper, we introd...

---

### 22. LiFlow: Flow Matching for 3D LiDAR Scene Completion

**Authors:** Andrea Matteazzi, Dietmar Tutsch

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02232v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02232v1)

**Summary:** In autonomous driving scenarios, the collected LiDAR point clouds can be challenged by occlusion and long-range sparsity, limiting the perception of autonomous driving systems. Scene completion methods can infer the missing parts of incomplete 3D LiDAR scenes. Recent methods adopt local point-level denoising diffusion probabilistic models, which require predicting Gaussian noise, leading to a mismatch between training and inference initial distributions. This paper introduces the first flow matc...

---

### 23. Show, Don't Tell: Morphing Latent Reasoning into Image Generation

**Authors:** Harold Haodong Chen, Xinxiang Yin, Wen-Jie Shu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02227v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02227v1)

**Summary:** Text-to-image (T2I) generation has achieved remarkable progress, yet existing methods often lack the ability to dynamically reason and refine during generation--a hallmark of human creativity. Current reasoning-augmented paradigms most rely on explicit thought processes, where intermediate reasoning is decoded into discrete text at fixed steps with frequent image decoding and re-encoding, leading to inefficiencies, information loss, and cognitive mismatches. To bridge this gap, we introduce Late...

---

### 24. Evaluating OCR Performance for Assistive Technology: Effects of Walking Speed, Camera Placement, and Camera Type

**Authors:** Junchi Feng, Nikhil Ballem, Mahya Beheshti, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02223v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02223v1)

**Summary:** Optical character recognition (OCR), which converts printed or handwritten text into machine-readable form, is widely used in assistive technology for people with blindness and low vision. Yet, most evaluations rely on static datasets that do not reflect the challenges of mobile use. In this study, we systematically evaluated OCR performance under both static and dynamic conditions. Static tests measured detection range across distances of 1-7 meters and viewing angles of 0-75 degrees horizontal...

---

### 25. MIRROR: Manifold Ideal Reference ReconstructOR for Generalizable AI-Generated Image Detection

**Authors:** Ruiqi Liu, Manni Cui, Ziheng Qin, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02222v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02222v1)

**Summary:** High-fidelity generative models have narrowed the perceptual gap between synthetic and real images, posing serious threats to media security. Most existing AI-generated image (AIGI) detectors rely on artifact-based classification and struggle to generalize to evolving generative traces. In contrast, human judgment relies on stable real-world regularities, with deviations from the human cognitive manifold serving as a more generalizable signal of forgery. Motivated by this insight, we reformulate...

---

### 26. LangMap: A Hierarchical Benchmark for Open-Vocabulary Goal Navigation

**Authors:** Bo Miao, Weijia Liu, Jun Luo, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02220v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02220v1)

**Summary:** The relationships between objects and language are fundamental to meaningful communication between humans and AI, and to practically useful embodied intelligence. We introduce HieraNav, a multi-granularity, open-vocabulary goal navigation task where agents interpret natural language instructions to reach targets at four semantic levels: scene, room, region, and instance. To this end, we present Language as a Map (LangMap), a large-scale benchmark built on real-world 3D indoor scans with comprehe...

---

### 27. Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation

**Authors:** Hongzhou Zhu, Min Zhao, Guande He, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02214v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02214v1)

**Summary:** To achieve real-time interactive video generation, current methods distill pretrained bidirectional video diffusion models into few-step autoregressive (AR) models, facing an architectural gap when full attention is replaced by causal attention. However, existing approaches do not bridge this gap theoretically. They initialize the AR student via ODE distillation, which requires frame-level injectivity, where each noisy frame must map to a unique clean frame under the PF-ODE of an AR teacher. Dis...

---

### 28. MAIN-VLA: Modeling Abstraction of Intention and eNvironment for Vision-Language-Action Models

**Authors:** Zheyuan Zhou, Liang Du, Zixun Sun, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02212v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02212v1)

**Summary:** Despite significant progress in Visual-Language-Action (VLA), in highly complex and dynamic environments that involve real-time unpredictable interactions (such as 3D open worlds and large-scale PvP games), existing approaches remain inefficient at extracting action-critical signals from redundant sensor streams. To tackle this, we introduce MAIN-VLA, a framework that explicitly Models the Abstraction of Intention and eNvironment to ground decision-making in deep semantic alignment rather than s...

---

### 29. SSI-DM: Singularity Skipping Inversion of Diffusion Models

**Authors:** Chen Min, Enze Jiang, Jishen Peng, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02193v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02193v1)

**Summary:** Inverting real images into the noise space is essential for editing tasks using diffusion models, yet existing methods produce non-Gaussian noise with poor editability due to the inaccuracy in early noising steps. We identify the root cause: a mathematical singularity that renders inversion fundamentally ill-posed. We propose Singularity Skipping Inversion of Diffusion Models (SSI-DM), which bypasses this singular region by adding small noise before standard inversion. This simple approach produ...

---

### 30. Learning Topology-Aware Implicit Field for Unified Pulmonary Tree Modeling with Incomplete Topological Supervision

**Authors:** Ziqiao Weng, Jiancheng Yang, Kangxian Xie, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02186v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02186v1)

**Summary:** Pulmonary trees extracted from CT images frequently exhibit topological incompleteness, such as missing or disconnected branches, which substantially degrades downstream anatomical analysis and limits the applicability of existing pulmonary tree modeling pipelines. Current approaches typically rely on dense volumetric processing or explicit graph reasoning, leading to limited efficiency and reduced robustness under realistic structural corruption. We propose TopoField, a topology-aware implicit ...

---

### 31. Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models

**Authors:** Yu Zeng, Wenxuan Huang, Zhen Fang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02185v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02185v1)

**Summary:** Multimodal Large Language Models (MLLMs) have advanced VQA and now support Vision-DeepResearch systems that use search engines for complex visual-textual fact-finding. However, evaluating these visual and textual search abilities is still difficult, and existing benchmarks have two major limitations. First, existing benchmarks are not visual search-centric: answers that should require visual search are often leaked through cross-textual cues in the text questions or can be inferred from the prio...

---

### 32. CIEC: Coupling Implicit and Explicit Cues for Multimodal Weakly Supervised Manipulation Localization

**Authors:** Xinquan Yu, Wei Lu, Xiangyang Luo

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02175v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02175v1)

**Summary:** To mitigate the threat of misinformation, multimodal manipulation localization has garnered growing attention. Consider that current methods rely on costly and time-consuming fine-grained annotations, such as patch/token-level annotations. This paper proposes a novel framework named Coupling Implicit and Explicit Cues (CIEC), which aims to achieve multimodal weakly-supervised manipulation localization for image-text pairs utilizing only coarse-grained image/sentence-level annotations. It compris...

---

### 33. Lung Nodule Image Synthesis Driven by Two-Stage Generative Adversarial Networks

**Authors:** Lu Cao, Xiquan He, Junying Zeng, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02171v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02171v1)

**Summary:** The limited sample size and insufficient diversity of lung nodule CT datasets severely restrict the performance and generalization ability of detection models. Existing methods generate images with insufficient diversity and controllability, suffering from issues such as monotonous texture features and distorted anatomical structures. Therefore, we propose a two-stage generative adversarial network (TSGAN) to enhance the diversity and spatial controllability of synthetic data by decoupling the m...

---

### 34. Real-Time 2D LiDAR Object Detection Using Three-Frame RGB Scan Encoding

**Authors:** Soheil Behnam Roudsari, Alexandre S. Brandão, Felipe N. Martins

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02167v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02167v1)

**Summary:** Indoor service robots need perception that is robust, more privacy-friendly than RGB video, and feasible on embedded hardware. We present a camera-free 2D LiDAR object detection pipeline that encodes short-term temporal context by stacking three consecutive scans as RGB channels, yielding a compact YOLOv8n input without occupancy-grid construction while preserving angular structure and motion cues. Evaluated in Webots across 160 randomized indoor scenarios with strict scenario-level holdout, the...

---

### 35. Reg4Pru: Regularisation Through Random Token Routing for Token Pruning

**Authors:** Julian Wyatt, Ronald Clark, Irina Voiculescu

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02163v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02163v1)

**Summary:** Transformers are widely adopted in modern vision models due to their strong ability to scale with dataset size and generalisability. However, this comes with a major drawback: computation scales quadratically to the total number of tokens. Numerous methods have been proposed to mitigate this. For example, we consider token pruning with reactivating tokens from preserved representations, but the increased computational efficiency of this method results in decreased stability from the preserved re...

---

### 36. LoopViT: Scaling Visual ARC with Looped Transformers

**Authors:** Wen-Jie Shu, Xuerui Qiu, Rui-Jie Zhu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02156v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02156v1)

**Summary:** Recent advances in visual reasoning have leveraged vision transformers to tackle the ARC-AGI benchmark. However, we argue that the feed-forward architecture, where computational depth is strictly bound to parameter size, falls short of capturing the iterative, algorithmic nature of human induction. In this work, we propose a recursive architecture called Loop-ViT, which decouples reasoning depth from model capacity through weight-tied recurrence. Loop-ViT iterates a weight-tied Hybrid Block, com...

---

### 37. Deep learning enables urban change profiling through alignment of historical maps

**Authors:** Sidi Wu, Yizi Chen, Maurizio Gribaudi, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02154v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02154v1)

**Summary:** Prior to modern Earth observation technologies, historical maps provide a unique record of long-term urban transformation and offer a lens on the evolving identity of cities. However, extracting consistent and fine-grained change information from historical map series remains challenging due to spatial misalignment, cartographic variation, and degrading document quality, limiting most analyses to small-scale or qualitative approaches. We propose a fully automated, deep learning-based framework f...

---

### 38. FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

**Authors:** Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02142v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02142v1)

**Summary:** Force sensing is a crucial modality for Vision-Language-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks. We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors. The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and robot s...

---

### 39. Eliminating Registration Bias in Synthetic CT Generation: A Physics-Based Simulation Framework

**Authors:** Lukas Zimmermann, Michael Rauter, Maximilian Schmid, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02130v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02130v1)

**Summary:** Supervised synthetic CT generation from CBCT requires registered training pairs, yet perfect registration between separately acquired scans remains unattainable. This registration bias propagates into trained models and corrupts standard evaluation metrics. This may suggest that superior benchmark performance indicates better reproduction of registration artifacts rather than anatomical fidelity. We propose physics-based CBCT simulation to provide geometrically aligned training pairs by construc...

---

### 40. Toxicity Assessment in Preclinical Histopathology via Class-Aware Mahalanobis Distance for Known and Novel Anomalies

**Authors:** Olga Graf, Dhrupal Patel, Peter Groß, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02124v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02124v1)

**Summary:** Drug-induced toxicity remains a leading cause of failure in preclinical development and early clinical trials. Detecting adverse effects at an early stage is critical to reduce attrition and accelerate the development of safe medicines. Histopathological evaluation remains the gold standard for toxicity assessment, but it relies heavily on expert pathologists, creating a bottleneck for large-scale screening. To address this challenge, we introduce an AI-based anomaly detection framework for hist...

---

### 41. MLV-Edit: Towards Consistent and Highly Efficient Editing for Minute-Level Videos

**Authors:** Yangyi Cao, Yuanhang Li, Lan Chen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02123v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02123v1)

**Summary:** We propose MLV-Edit, a training-free, flow-based framework that address the unique challenges of minute-level video editing. While existing techniques excel in short-form video manipulation, scaling them to long-duration videos remains challenging due to prohibitive computational overhead and the difficulty of maintaining global temporal consistency across thousands of frames. To address this, MLV-Edit employs a divide-and-conquer strategy for segment-wise editing, facilitated by two core module...

---

### 42. Enhancing Diffusion-Based Quantitatively Controllable Image Generation via Matrix-Form EDM and Adaptive Vicinal Training

**Authors:** Xin Ding, Yun Chen, Sen Zhang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02114v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02114v1)

**Summary:** Continuous Conditional Diffusion Model (CCDM) is a diffusion-based framework designed to generate high-quality images conditioned on continuous regression labels. Although CCDM has demonstrated clear advantages over prior approaches across a range of datasets, it still exhibits notable limitations and has recently been surpassed by a GAN-based method, namely CcGAN-AVAR. These limitations mainly arise from its reliance on an outdated diffusion framework and its low sampling efficiency due to long...

---

### 43. An Empirical Study of World Model Quantization

**Authors:** Zhongqian Fu, Tianyi Zhao, Kai Han, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02110v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02110v1)

**Summary:** World models learn an internal representation of environment dynamics, enabling agents to simulate and reason about future states within a compact latent space for tasks such as planning, prediction, and inference. However, running world models rely on hevay computational cost and memory footprint, making model quantization essential for efficient deployment. To date, the effects of post-training quantization (PTQ) on world models remain largely unexamined. In this work, we present a systematic ...

---

### 44. Teacher-Guided Student Self-Knowledge Distillation Using Diffusion Model

**Authors:** Yu Wang, Chuanguang Yang, Zhulin An, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02107v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02107v1)

**Summary:** Existing Knowledge Distillation (KD) methods often align feature information between teacher and student by exploring meaningful feature processing and loss functions. However, due to the difference in feature distributions between the teacher and student, the student model may learn incompatible information from the teacher. To address this problem, we propose teacher-guided student Diffusion Self-KD, dubbed as DSKD. Instead of the direct teacher-student alignment, we leverage the teacher class...

---

### 45. FSVideo: Fast Speed Video Diffusion Model in a Highly-Compressed Latent Space

**Authors:**  FSVideo Team, Qingyu Chen, Zhiyuan Fang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02092v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02092v1)

**Summary:** We introduce FSVideo, a fast speed transformer-based image-to-video (I2V) diffusion framework. We build our framework on the following key components: 1.) a new video autoencoder with highly-compressed latent space ($64\times64\times4$ spatial-temporal downsampling ratio), achieving competitive reconstruction quality; 2.) a diffusion transformer (DIT) architecture with a new layer memory design to enhance inter-layer information flow and context reuse within DIT, and 3.) a multi-resolution gener...

---

### 46. UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction

**Authors:** Changbai Li, Haodong Zhu, Hanlin Chen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02089v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02089v1)

**Summary:** While 3D Gaussian Splatting (3DGS) enables high-quality, real-time rendering for bounded scenes, its extension to large-scale urban environments gives rise to critical challenges in terms of geometric consistency, memory efficiency, and computational scalability. To address these issues, we present UrbanGS, a scalable reconstruction framework that effectively tackles these challenges for city-scale applications. First, we propose a Depth-Consistent D-Normal Regularization module. Unlike existing...

---

### 47. Multi-View Stenosis Classification Leveraging Transformer-Based Multiple-Instance Learning Using Real-World Clinical Data

**Authors:** Nikola Cenikj, Özgün Turgut, Alexander Müller, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02067v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02067v1)

**Summary:** Coronary artery stenosis is a leading cause of cardiovascular disease, diagnosed by analyzing the coronary arteries from multiple angiography views. Although numerous deep-learning models have been proposed for stenosis detection from a single angiography view, their performance heavily relies on expensive view-level annotations, which are often not readily available in hospital systems. Moreover, these models fail to capture the temporal dynamics and dependencies among multiple views, which are...

---

### 48. Auto-Comp: An Automated Pipeline for Scalable Compositional Probing of Contrastive Vision-Language Models

**Authors:** Cristian Sbrolli, Matteo Matteucci, Toshihiko Yamasaki

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02043v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02043v1)

**Summary:** Modern Vision-Language Models (VLMs) exhibit a critical flaw in compositional reasoning, often confusing "a red cube and a blue sphere" with "a blue cube and a red sphere". Disentangling the visual and linguistic roots of these failures is a fundamental challenge for robust evaluation. To enable fine-grained, controllable analysis, we introduce Auto-Comp, a fully automated and synthetic pipeline for generating scalable benchmarks. Its controllable nature is key to dissecting and isolating differ...

---

### 49. One Size, Many Fits: Aligning Diverse Group-Wise Click Preferences in Large-Scale Advertising Image Generation

**Authors:** Shuo Lu, Haohan Wang, Wei Feng, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02033v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02033v1)

**Summary:** Advertising image generation has increasingly focused on online metrics like Click-Through Rate (CTR), yet existing approaches adopt a ``one-size-fits-all" strategy that optimizes for overall CTR while neglecting preference diversity among user groups. This leads to suboptimal performance for specific groups, limiting targeted marketing effectiveness. To bridge this gap, we present \textit{One Size, Many Fits} (OSMF), a unified framework that aligns diverse group-wise click preferences in large-...

---

### 50. Rethinking Genomic Modeling Through Optical Character Recognition

**Authors:** Hongxin Xiang, Pengsen Ma, Yunkang Cao, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02014v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02014v1)

**Summary:** Recent genomic foundation models largely adopt large language model architectures that treat DNA as a one-dimensional token sequence. However, exhaustive sequential reading is structurally misaligned with sparse and discontinuous genomic semantics, leading to wasted computation on low-information background and preventing understanding-driven compression for long contexts. Here, we present OpticalDNA, a vision-based framework that reframes genomic modeling as Optical Character Recognition (OCR)-...

---

## cs.LG

**50 papers**

### 1. Reward-free Alignment for Conflicting Objectives

**Authors:** Peter Chen, Xiaopeng Li, Xi Chen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02495v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02495v1)

**Summary:** Direct alignment methods are increasingly used to align large language models (LLMs) with human preferences. However, many real-world alignment problems involve multiple conflicting objectives, where naive aggregation of preferences can lead to unstable training and poor trade-offs. In particular, weighted loss methods may fail to identify update directions that simultaneously improve all objectives, and existing multi-objective approaches often rely on explicit reward models, introducing additi...

---

### 2. MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training

**Authors:** Dulhan Jayalath, Oiwi Parker Jones

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02494v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02494v1)

**Summary:** Clinical brain-to-text interfaces are designed for paralysed patients who cannot provide extensive training recordings. Pre-training improves data-efficient generalisation by learning statistical priors across subjects, but these priors critically depend on context. While natural speech might unfold gradually over minutes, most methods pre-train with only a few seconds of context. Thus, we propose MEG-XL, a model pre-trained with 2.5 minutes of MEG context per sample, 5-300x longer than prior wo...

---

### 3. RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System

**Authors:** Yinjie Wang, Tianbao Xie, Ke Shen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02488v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02488v1)

**Summary:** We propose RLAnything, a reinforcement learning framework that dynamically forges environment, policy, and reward models through closed-loop optimization, amplifying learning signals and strengthening the overall RL system for any LLM or agentic scenarios. Specifically, the policy is trained with integrated feedback from step-wise and outcome signals, while the reward model is jointly optimized via consistency feedback, which in turn further improves policy training. Moreover, our theory-motivat...

---

### 4. Expanding the Capabilities of Reinforcement Learning via Text Feedback

**Authors:** Yuda Song, Lili Chen, Fahim Tajwar, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02482v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02482v1)

**Summary:** The success of RL for LLM post-training stems from an unreasonably uninformative source: a single bit of information per rollout as binary reward or preference label. At the other extreme, distillation offers dense supervision but requires demonstrations, which are costly and difficult to scale. We study text feedback as an intermediate signal: richer than scalar rewards, yet cheaper than complete demonstrations. Textual feedback is a natural mode of human interaction and is already abundant in ...

---

### 5. MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

**Authors:** Haozhen Zhang, Quanyu Long, Jianzhu Bao, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02474v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02474v1)

**Summary:** Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory. These fixed procedures hard-code human priors about what to store and how to revise memory, making them rigid under diverse interaction patterns and inefficient on long histories. To this end, we present \textbf{MemSkill}, which reframes these operations as learnable and evolvable memory skills, structured and reusable routines for extracting, consolidating, and pru...

---

### 6. HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos

**Authors:** Yinhuai Wang, Qihan Zhao, Yuen Fui Lau, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02473v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02473v1)

**Summary:** Enabling humanoid robots to perform agile and adaptive interactive tasks has long been a core challenge in robotics. Current approaches are bottlenecked by either the scarcity of realistic interaction data or the need for meticulous, task-specific reward engineering, which limits their scalability. To narrow this gap, we present HumanX, a full-stack framework that compiles human video into generalizable, real-world interaction skills for humanoids, without task-specific rewards. HumanX integrate...

---

### 7. SPARKLING: Balancing Signal Preservation and Symmetry Breaking for Width-Progressive Learning

**Authors:** Qifan Yu, Xinyu Ma, Zhijian Zhuo, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02472v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02472v1)

**Summary:** Progressive Learning (PL) reduces pre-training computational overhead by gradually increasing model scale. While prior work has extensively explored depth expansion, width expansion remains significantly understudied, with the few existing methods limited to the early stages of training. However, expanding width during the mid-stage is essential for maximizing computational savings, yet it remains a formidable challenge due to severe training instabilities. Empirically, we show that naive initia...

---

### 8. Age-Aware Edge-Blind Federated Learning via Over-the-Air Aggregation

**Authors:** Ahmed M. Elshazly, Ahmed Arafa

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02469v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02469v1)

**Summary:** We study federated learning (FL) over wireless fading channels where multiple devices simultaneously send their model updates. We propose an efficient \emph{age-aware edge-blind over-the-air FL} approach that does not require channel state information (CSI) at the devices. Instead, the parameter server (PS) uses multiple antennas and applies maximum-ratio combining (MRC) based on its estimated sum of the channel gains to detect the parameter updates. A key challenge is that the number of orthogo...

---

### 9. MentisOculi: Revealing the Limits of Reasoning with Mental Imagery

**Authors:** Jana Zeller, Thaddäus Wiedemer, Fanfei Li, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02465v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02465v1)

**Summary:** Frontier models are transitioning from multimodal large language models (MLLMs) that merely ingest visual information to unified multimodal models (UMMs) capable of native interleaved generation. This shift has sparked interest in using intermediate visualizations as a reasoning aid, akin to human mental imagery. Central to this idea is the ability to form, maintain, and manipulate visual representations in a goal-oriented manner. To evaluate and probe this capability, we develop MentisOculi, a ...

---

### 10. Conflict-Aware Client Selection for Multi-Server Federated Learning

**Authors:** Mingwei Hong, Zheng Lin, Zehang Lin, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02458v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02458v1)

**Summary:** Federated learning (FL) has emerged as a promising distributed machine learning (ML) that enables collaborative model training across clients without exposing raw data, thereby preserving user privacy and reducing communication costs. Despite these benefits, traditional single-server FL suffers from high communication latency due to the aggregation of models from a large number of clients. While multi-server FL distributes workloads across edge servers, overlapping client coverage and uncoordina...

---

### 11. Active Causal Experimentalist (ACE): Learning Intervention Strategies via Direct Preference Optimization

**Authors:** Patrick Cooper, Alvaro Velasquez

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02451v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02451v1)

**Summary:** Discovering causal relationships requires controlled experiments, but experimentalists face a sequential decision problem: each intervention reveals information that should inform what to try next. Traditional approaches such as random sampling, greedy information maximization, and round-robin coverage treat each decision in isolation, unable to learn adaptive strategies from experience. We propose Active Causal Experimentalist (ACE), which learns experimental design as a sequential policy. Our ...

---

### 12. Finite-Sample Wasserstein Error Bounds and Concentration Inequalities for Nonlinear Stochastic Approximation

**Authors:** Seo Taek Kong, R. Srikant

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02445v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02445v1)

**Summary:** This paper derives non-asymptotic error bounds for nonlinear stochastic approximation algorithms in the Wasserstein-$p$ distance. To obtain explicit finite-sample guarantees for the last iterate, we develop a coupling argument that compares the discrete-time process to a limiting Ornstein-Uhlenbeck process. Our analysis applies to algorithms driven by general noise conditions, including martingale differences and functions of ergodic Markov chains. Complementing this result, we handle the conver...

---

### 13. Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE

**Authors:** Yuanteng Chen, Peisong Wang, Nanxin Zeng, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02443v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02443v1)

**Summary:** Test-time scaling improves LLM performance by generating multiple candidate solutions, yet token-level sampling requires temperature tuning that trades off diversity against stability. Fine-grained MoE, featuring hundreds of well-trained experts per layer and multi-expert activation per token, offers an unexplored alternative through its rich routing space. We empirically characterize fine-grained MoE routing and uncover an informative pattern: router scores exhibit a certain head of high-confid...

---

### 14. Energy-Efficient Neuromorphic Computing for Edge AI: A Framework with Adaptive Spiking Neural Networks and Hardware-Aware Optimization

**Authors:** Olaf Yunus Laitinen Imanov, Derya Umut Kulali, Taner Yilmaz, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02439v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02439v1)

**Summary:** Edge AI applications increasingly require ultra-low-power, low-latency inference. Neuromorphic computing based on event-driven spiking neural networks (SNNs) offers an attractive path, but practical deployment on resource-constrained devices is limited by training difficulty, hardware-mapping overheads, and sensitivity to temporal dynamics. We present NeuEdge, a framework that combines adaptive SNN models with hardware-aware optimization for edge deployment. NeuEdge uses a temporal coding scheme...

---

### 15. Maximizing Reliability with Bayesian Optimization

**Authors:** Jack M. Buckingham, Ivo Couckuyt, Juergen Branke

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02432v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02432v1)

**Summary:** Bayesian optimization (BO) is a popular, sample-efficient technique for expensive, black-box optimization. One such problem arising in manufacturing is that of maximizing the reliability, or equivalently minimizing the probability of a failure, of a design which is subject to random perturbations - a problem that can involve extremely rare failures ($P_\mathrm{fail} = 10^{-6}-10^{-8}$). In this work, we propose two BO methods based on Thompson sampling and knowledge gradient, the latter approxim...

---

### 16. Full-Batch Gradient Descent Outperforms One-Pass SGD: Sample Complexity Separation in Single-Index Learning

**Authors:** Filip Kovačević, Hong Chang Ji, Denny Wu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02431v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02431v1)

**Summary:** It is folklore that reusing training data more than once can improve the statistical efficiency of gradient-based learning. However, beyond linear regression, the theoretical advantage of full-batch gradient descent (GD, which always reuses all the data) over one-pass stochastic gradient descent (online SGD, which uses each data point only once) remains unclear. In this work, we consider learning a $d$-dimensional single-index model with a quadratic activation, for which it is known that one-pas...

---

### 17. Embedding Perturbation may Better Reflect the Uncertainty in LLM Reasoning

**Authors:** Qihao Wen, Jiahao Wang, Yang Nan, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02427v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02427v1)

**Summary:** Large language Models (LLMs) have achieved significant breakthroughs across diverse domains; however, they can still produce unreliable or misleading outputs. For responsible LLM application, Uncertainty Quantification (UQ) techniques are used to estimate a model's uncertainty about its outputs, indicating the likelihood that those outputs may be problematic. For LLM reasoning tasks, it is essential to estimate the uncertainty not only for the final answer, but also for the intermediate steps of...

---

### 18. Repurposing Protein Language Models for Latent Flow-Based Fitness Optimization

**Authors:** Amaru Caceres Arroyo, Lea Bogensperger, Ahmed Allam, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02425v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02425v1)

**Summary:** Protein fitness optimization is challenged by a vast combinatorial landscape where high-fitness variants are extremely sparse. Many current methods either underperform or require computationally expensive gradient-based sampling. We present CHASE, a framework that repurposes the evolutionary knowledge of pretrained protein language models by compressing their embeddings into a compact latent space. By training a conditional flow-matching model with classifier-free guidance, we enable the direct ...

---

### 19. Poly-attention: a general scheme for higher-order self-attention

**Authors:** Sayak Chakrabarti, Toniann Pitassi, Josh Alman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02422v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02422v1)

**Summary:** The self-attention mechanism, at the heart of the Transformer model, is able to effectively model pairwise interactions between tokens. However, numerous recent works have shown that it is unable to perform basic tasks involving detecting triples of correlated tokens, or compositional tasks where multiple input tokens need to be referenced to generate a result. Some higher-dimensional alternatives to self-attention have been proposed to address this, including higher-order attention and Strassen...

---

### 20. Trust Region Continual Learning as an Implicit Meta-Learner

**Authors:** Zekun Wang, Anant Gupta, Christopher J. MacLellan

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02417v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02417v1)

**Summary:** Continual learning aims to acquire tasks sequentially without catastrophic forgetting, yet standard strategies face a core tradeoff: regularization-based methods (e.g., EWC) can overconstrain updates when task optima are weakly overlapping, while replay-based methods can retain performance but drift due to imperfect replay. We study a hybrid perspective: \emph{trust region continual learning} that combines generative replay with a Fisher-metric trust region constraint. We show that, under local ...

---

### 21. Active Transfer Bagging: A New Approach for Accelerated Active Learning Acquisition of Data by Combined Transfer Learning and Bagging Based Models

**Authors:** Vivienne Pelletier, Daniel J. Rivera, Obinna Nwokonkwo, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02415v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02415v1)

**Summary:** Modern machine learning has achieved remarkable success on many problems, but this success often depends on the existence of large, labeled datasets. While active learning can dramatically reduce labeling cost when annotations are expensive, early performance is frequently dominated by the initial seed set, typically chosen at random. In many applications, however, related or approximate datasets are readily available and can be leveraged to construct a better seed set. We introduce a new method...

---

### 22. Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank

**Authors:** Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02414v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02414v1)

**Summary:** Timely and accurate identification of student misconceptions is key to improving learning outcomes and pre-empting the compounding of student errors. However, this task is highly dependent on the effort and intuition of the teacher. In this work, we present a novel approach for detecting misconceptions from student-tutor dialogues using large language models (LLMs). First, we use a fine-tuned LLM to generate plausible misconceptions, and then retrieve the most promising candidates among these us...

---

### 23. Masked Autoencoders as Universal Speech Enhancer

**Authors:** Rajalaxmi Rajagopalan, Ritwik Giri, Zhiqiang Tang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02413v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02413v1)

**Summary:** Supervised speech enhancement methods have been very successful. However, in practical scenarios, there is a lack of clean speech, and self-supervised learning-based (SSL) speech enhancement methods that offer comparable enhancement performance and can be applied to other speech-related downstream applications are desired. In this work, we develop a masked autoencoder based universal speech enhancer that is agnostic to the type of distortion affecting speech, can handle multiple distortions simu...

---

### 24. Provably Data-driven Multiple Hyper-parameter Tuning with Structured Loss Function

**Authors:** Tung Quoc Le, Anh Tuan Nguyen, Viet Anh Nguyen

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02406v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02406v1)

**Summary:** Data-driven algorithm design automates hyperparameter tuning, but its statistical foundations remain limited because model performance can depend on hyperparameters in implicit and highly non-smooth ways. Existing guarantees focus on the simple case of a one-dimensional (scalar) hyperparameter. This leaves the practically important, multi-dimensional hyperparameter tuning setting unresolved. We address this open question by establishing the first general framework for establishing generalization...

---

### 25. Didactic to Constructive: Turning Expert Solutions into Learnable Reasoning

**Authors:** Ethan Mendes, Jungsoo Park, Alan Ritter

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02405v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02405v1)

**Summary:** Improving the reasoning capabilities of large language models (LLMs) typically relies either on the model's ability to sample a correct solution to be reinforced or on the existence of a stronger model able to solve the problem. However, many difficult problems remain intractable for even current frontier models, preventing the extraction of valid training signals. A promising alternative is to leverage high-quality expert human solutions, yet naive imitation of this data fails because it is fun...

---

### 26. An Empirical Study on Noisy Data and LLM Pretraining Loss Divergence

**Authors:** Qizhen Zhang, Ankush Garg, Jakob Foerster, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02400v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02400v1)

**Summary:** Large-scale pretraining datasets drive the success of large language models (LLMs). However, these web-scale corpora inevitably contain large amounts of noisy data due to unregulated web content or randomness inherent in data. Although LLM pretrainers often speculate that such noise contributes to instabilities in large-scale LLM pretraining and, in the worst cases, loss divergence, this phenomenon remains poorly understood.In this work, we present a systematic empirical study of whether noisy d...

---

### 27. PRISM: Performer RS-IMLE for Single-pass Multisensory Imitation Learning

**Authors:** Amisha Bhaskar, Pratap Tokekar, Stefano Di Cairano, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02396v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02396v1)

**Summary:** Robotic imitation learning typically requires models that capture multimodal action distributions while operating at real-time control rates and accommodating multiple sensing modalities. Although recent generative approaches such as diffusion models, flow matching, and Implicit Maximum Likelihood Estimation (IMLE) have achieved promising results, they often satisfy only a subset of these requirements. To address this, we introduce PRISM, a single-pass policy based on a batch-global rejection-sa...

---

### 28. David vs. Goliath: Verifiable Agent-to-Agent Jailbreaking via Reinforcement Learning

**Authors:** Samuel Nellessen, Tal Kachman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02395v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02395v1)

**Summary:** The evolution of large language models into autonomous agents introduces adversarial failures that exploit legitimate tool privileges, transforming safety evaluation in tool-augmented environments from a subjective NLP task into an objective control problem. We formalize this threat model as Tag-Along Attacks: a scenario where a tool-less adversary "tags along" on the trusted privileges of a safety-aligned Operator to induce prohibited tool use through conversation alone. To validate this threat...

---

### 29. Personalized Image Generation via Human-in-the-loop Bayesian Optimization

**Authors:** Rajalaxmi Rajagopalan, Debottam Dutta, Yu-Lin Wei, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02388v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02388v1)

**Summary:** Imagine Alice has a specific image $x^\ast$ in her mind, say, the view of the street in which she grew up during her childhood. To generate that exact image, she guides a generative model with multiple rounds of prompting and arrives at an image $x^{p*}$. Although $x^{p*}$ is reasonably close to $x^\ast$, Alice finds it difficult to close that gap using language prompts. This paper aims to narrow this gap by observing that even after language has reached its limits, humans can still tell when a ...

---

### 30. Trust by Design: Skill Profiles for Transparent, Cost-Aware LLM Routing

**Authors:** Mika Okamoto, Ansel Kaplan Erol, Glenn Matlin

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02386v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02386v1)

**Summary:** How should Large Language Model (LLM) practitioners select the right model for a task without wasting money? We introduce BELLA (Budget-Efficient LLM Selection via Automated skill-profiling), a framework that recommends optimal LLM selection for tasks through interpretable skill-based model selection. Standard benchmarks report aggregate metrics that obscure which specific capabilities a task requires and whether a cheaper model could suffice. BELLA addresses this gap through three stages: (1) d...

---

### 31. Transformers learn factored representations

**Authors:** Adam Shai, Loren Amdahl-Culleton, Casper L. Christensen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02385v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02385v1)

**Summary:** Transformers pretrained via next token prediction learn to factor their world into parts, representing these factors in orthogonal subspaces of the residual stream. We formalize two representational hypotheses: (1) a representation in the product space of all factors, whose dimension grows exponentially with the number of parts, or (2) a factored representation in orthogonal subspaces, whose dimension grows linearly. The factored representation is lossless when factors are conditionally independ...

---

### 32. SLIME: Stabilized Likelihood Implicit Margin Enforcement for Preference Optimization

**Authors:** Maksim Afanasyev, Illarion Iov

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02383v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02383v1)

**Summary:** Direct preference optimization methods have emerged as a computationally efficient alternative to Reinforcement Learning from Human Feedback (RLHF) for aligning Large Language Models (LLMs). Latest approaches have streamlined the alignment process by deriving implicit reward functions, yet they often suffer from a critical objective mismatch: optimizing the relative margin between chosen and rejected responses does not guarantee the preservation of the chosen response's absolute likelihood. This...

---

### 33. Self-Supervised Learning from Structural Invariance

**Authors:** Yipeng Zhang, Hafez Ghaemi, Jungyoon Lee, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02381v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02381v1)

**Summary:** Joint-embedding self-supervised learning (SSL), the key paradigm for unsupervised representation learning from visual data, learns from invariances between semantically-related data pairs. We study the one-to-many mapping problem in SSL, where each datum may be mapped to multiple valid targets. This arises when data pairs come from naturally occurring generative processes, e.g., successive video frames. We show that existing methods struggle to flexibly capture this conditional uncertainty. As a...

---

### 34. C-kNN-LSH: A Nearest-Neighbor Algorithm for Sequential Counterfactual Inference

**Authors:** Jing Wang, Jie Shen, Qiaomin Xie, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02371v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02371v1)

**Summary:** Estimating causal effects from longitudinal trajectories is central to understanding the progression of complex conditions and optimizing clinical decision-making, such as comorbidities and long COVID recovery. We introduce \emph{C-kNN--LSH}, a nearest-neighbor framework for sequential causal inference designed to handle such high-dimensional, confounded situations. By utilizing locality-sensitive hashing, we efficiently identify ``clinical twins'' with similar covariate histories, enabling loca...

---

### 35. Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback

**Authors:** Yaolun Zhang, Yiran Wu, Yijiong Yu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02369v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02369v1)

**Summary:** Large language model (LLM) agents are increasingly equipped with memory, which are stored experience and reusable guidance that can improve task-solving performance. Recent \emph{self-evolving} systems update memory based on interaction outcomes, but most existing evolution pipelines are developed for static train/test splits and only approximate online learning by folding static benchmarks, making them brittle under true distribution shift and continuous feedback. We introduce \textsc{Live-Evo}...

---

### 36. ReasonCACHE: Teaching LLMs To Reason Without Weight Updates

**Authors:** Sharut Gupta, Phillip Isola, Stefanie Jegelka, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02366v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02366v1)

**Summary:** Can Large language models (LLMs) learn to reason without any weight update and only through in-context learning (ICL)? ICL is strikingly sample-efficient, often learning from only a handful of demonstrations, but complex reasoning tasks typically demand many training examples to learn from. However, naively scaling ICL by adding more demonstrations breaks down at this scale: attention costs grow quadratically, performance saturates or degrades with longer contexts, and the approach remains a sha...

---

### 37. Transfer Learning Through Conditional Quantile Matching

**Authors:** Yikun Zhang, Steven Wilkins-Reeves, Wesley Lee, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02358v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02358v1)

**Summary:** We introduce a transfer learning framework for regression that leverages heterogeneous source domains to improve predictive performance in a data-scarce target domain. Our approach learns a conditional generative model separately for each source domain and calibrates the generated responses to the target domain via conditional quantile matching. This distributional alignment step corrects general discrepancies between source and target domains without imposing restrictive assumptions such as cov...

---

### 38. NAB: Neural Adaptive Binning for Sparse-View CT reconstruction

**Authors:** Wangduo Xie, Matthew B. Blaschko

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02356v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02356v1)

**Summary:** Computed Tomography (CT) plays a vital role in inspecting the internal structures of industrial objects. Furthermore, achieving high-quality CT reconstruction from sparse views is essential for reducing production costs. While classic implicit neural networks have shown promising results for sparse reconstruction, they are unable to leverage shape priors of objects. Motivated by the observation that numerous industrial objects exhibit rectangular structures, we propose a novel \textbf{N}eural \t...

---

### 39. Hierarchical Federated Learning with SignSGD: A Highly Communication-Efficient Approach

**Authors:** Amirreza Kazemi, Seyed Mohammad Azimi-Abarghouyi, Gabor Fodor, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02355v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02355v1)

**Summary:** Hierarchical federated learning (HFL) has emerged as a key architecture for large-scale wireless and Internet of Things systems, where devices communicate with nearby edge servers before reaching the cloud. In these environments, uplink bandwidth and latency impose strict communication limits, thereby making aggressive gradient compression essential. One-bit methods such as sign-based stochastic gradient descent (SignSGD) offer an attractive solution in flat federated settings, but existing theo...

---

### 40. Implicit neural representation of textures

**Authors:** Albert Kwok, Zheyuan Hu, Dounia Hammou

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02354v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02354v1)

**Summary:** Implicit neural representation (INR) has proven to be accurate and efficient in various domains. In this work, we explore how different neural networks can be designed as a new texture INR, which operates in a continuous manner rather than a discrete one over the input UV coordinate space. Through thorough experiments, we demonstrate that these INRs perform well in terms of image quality, with considerable memory usage and rendering inference time. We analyze the balance between these objectives...

---

### 41. Artificial Intelligence and Symmetries: Learning, Encoding, and Discovering Structure in Physical Data

**Authors:** Veronica Sanz

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02351v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02351v1)

**Summary:** Symmetries play a central role in physics, organizing dynamics, constraining interactions, and determining the effective number of physical degrees of freedom. In parallel, modern artificial intelligence methods have demonstrated a remarkable ability to extract low-dimensional structure from high-dimensional data through representation learning. This review examines the interplay between these two perspectives, focusing on the extent to which symmetry-induced constraints can be identified, encod...

---

### 42. Context Learning for Multi-Agent Discussion

**Authors:** Xingyuan Hua, Sheng Yue, Xinyi Li, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02350v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02350v1)

**Summary:** Multi-Agent Discussion (MAD) has garnered increasing attention very recently, where multiple LLM instances collaboratively solve problems via structured discussion. However, we find that current MAD methods easily suffer from discussion inconsistency, LLMs fail to reach a coherent solution, due to the misalignment between their individual contexts.In this paper, we introduce a multi-LLM context learning method (M2CL) that learns a context generator for each agent, capable of dynamically generati...

---

### 43. Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics

**Authors:** Ziwen Xu, Chenyan Wu, Hengyu Sun, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02343v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02343v1)

**Summary:** Methods for controlling large language models (LLMs), including local weight fine-tuning, LoRA-based adaptation, and activation-based interventions, are often studied in isolation, obscuring their connections and making comparison difficult. In this work, we present a unified view that frames these interventions as dynamic weight updates induced by a control signal, placing them within a single conceptual framework. Building on this view, we propose a unified preference-utility analysis that sep...

---

### 44. VQ-Style: Disentangling Style and Content in Motion with Residual Quantized Representations

**Authors:** Fatemeh Zargarbashi, Dhruv Agrawal, Jakob Buhmann, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02334v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02334v1)

**Summary:** Human motion data is inherently rich and complex, containing both semantic content and subtle stylistic features that are challenging to model. We propose a novel method for effective disentanglement of the style and content in human motion data to facilitate style transfer. Our approach is guided by the insight that content corresponds to coarse motion attributes while style captures the finer, expressive details. To model this hierarchy, we employ Residual Vector Quantized Variational Autoenco...

---

### 45. Interpreting and Controlling LLM Reasoning through Integrated Policy Gradient

**Authors:** Changming Li, Kaixing Zhang, Haoyun Xu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02313v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02313v1)

**Summary:** Large language models (LLMs) demonstrate strong reasoning abilities in solving complex real-world problems. Yet, the internal mechanisms driving these complex reasoning behaviors remain opaque. Existing interpretability approaches targeting reasoning either identify components (e.g., neurons) correlated with special textual patterns, or rely on human-annotated contrastive pairs to derive control vectors. Consequently, current methods struggle to precisely localize complex reasoning mechanisms or...

---

### 46. Spark: Modular Spiking Neural Networks

**Authors:** Mario Franco, Carlos Gershenson

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02306v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02306v1)

**Summary:** Nowadays, neural networks act as a synonym for artificial intelligence. Present neural network models, although remarkably powerful, are inefficient both in terms of data and energy. Several alternative forms of neural networks have been proposed to address some of these problems. Specifically, spiking neural networks are suitable for efficient hardware implementations. However, effective learning algorithms for spiking networks remain elusive, although it is suspected that effective plasticity ...

---

### 47. Position: Explaining Behavioral Shifts in Large Language Models Requires a Comparative Approach

**Authors:** Martino Ciaperoni, Marzio Di Vece, Luca Pappalardo, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02304v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02304v1)

**Summary:** Large-scale foundation models exhibit behavioral shifts: intervention-induced behavioral changes that appear after scaling, fine-tuning, reinforcement learning or in-context learning. While investigating these phenomena have recently received attention, explaining their appearance is still overlooked. Classic explainable AI (XAI) methods can surface failures at a single checkpoint of a model, but they are structurally ill-suited to justify what changed internally across different checkpoints and...

---

### 48. Advancing General-Purpose Reasoning Models with Modular Gradient Surgery

**Authors:** Min Cai, Yu Liang, Longzheng Wang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02301v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02301v1)

**Summary:** Reinforcement learning (RL) has played a central role in recent advances in large reasoning models (LRMs), yielding strong gains in verifiable and open-ended reasoning. However, training a single general-purpose LRM across diverse domains remains challenging due to pronounced domain heterogeneity. Through a systematic study of two widely used strategies, Sequential RL and Mixed RL, we find that both incur substantial cross-domain interference at the behavioral and gradient levels, resulting in l...

---

### 49. Decoupling Generalizability and Membership Privacy Risks in Neural Networks

**Authors:** Xingli Fang, Jung-Eun Kim

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02296v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02296v1)

**Summary:** A deep learning model usually has to sacrifice some utilities when it acquires some other abilities or characteristics. Privacy preservation has such trade-off relationships with utilities. The loss disparity between various defense approaches implies the potential to decouple generalizability and privacy risks to maximize privacy gain. In this paper, we identify that the model's generalization and privacy risks exist in different regions in deep neural network architectures. Based on the observ...

---

### 50. EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models

**Authors:** Shaima Ahmad Freja, Ferhat Ozgur Catak, Betul Yurdem, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02295v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02295v1)

**Summary:** Large Language Models (LLMs) are increasingly deployed in critical applications requiring reliable reasoning, yet their internal reasoning processes remain difficult to evaluate systematically. Existing methods focus on final-answer correctness, providing limited insight into how reasoning unfolds across intermediate steps. We present EvalQReason, a framework that quantifies LLM reasoning quality through step-level probability distribution analysis without requiring human annotation. The framewo...

---

## cs.NE

**50 papers**

### 1. Energy-Efficient Neuromorphic Computing for Edge AI: A Framework with Adaptive Spiking Neural Networks and Hardware-Aware Optimization

**Authors:** Olaf Yunus Laitinen Imanov, Derya Umut Kulali, Taner Yilmaz, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02439v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02439v1)

**Summary:** Edge AI applications increasingly require ultra-low-power, low-latency inference. Neuromorphic computing based on event-driven spiking neural networks (SNNs) offers an attractive path, but practical deployment on resource-constrained devices is limited by training difficulty, hardware-mapping overheads, and sensitivity to temporal dynamics. We present NeuEdge, a framework that combines adaptive SNN models with hardware-aware optimization for edge deployment. NeuEdge uses a temporal coding scheme...

---

### 2. Introns and Templates Matter: Rethinking Linkage in GP-GOMEA

**Authors:** Johannes Koch, Tanja Alderliesten, Peter A. N. Bosman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02311v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02311v1)

**Summary:** GP-GOMEA is among the state-of-the-art for symbolic regression, especially when it comes to finding small and potentially interpretable solutions. A key mechanism employed in any GOMEA variant is the exploitation of linkage, the dependencies between variables, to ensure efficient evolution. In GP-GOMEA, mutual information between node positions in GP trees has so far been used to learn linkage. For this, a fixed expression template is used. This however leads to introns for expressions smaller t...

---

### 3. Spark: Modular Spiking Neural Networks

**Authors:** Mario Franco, Carlos Gershenson

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02306v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02306v1)

**Summary:** Nowadays, neural networks act as a synonym for artificial intelligence. Present neural network models, although remarkably powerful, are inefficient both in terms of data and energy. Several alternative forms of neural networks have been proposed to address some of these problems. Specifically, spiking neural networks are suitable for efficient hardware implementations. However, effective learning algorithms for spiking networks remain elusive, although it is suspected that effective plasticity ...

---

### 4. Backpropagation as Physical Relaxation: Exact Gradients in Finite Time

**Authors:** Antonino Emanuele Scurria

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02281v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02281v1)

**Summary:** Backpropagation, the foundational algorithm for training neural networks, is typically understood as a symbolic computation that recursively applies the chain rule. We show it emerges exactly as the finite-time relaxation of a physical dynamical system. By formulating feedforward inference as a continuous-time process and applying Lagrangian theory of non-conservative systems to handle asymmetric interactions, we derive a global energy functional on a doubled state space encoding both activation...

---

### 5. Online Fine-Tuning of Pretrained Controllers for Autonomous Driving via Real-Time Recurrent RL

**Authors:** Julian Lemmel, Felix Resch, Mónika Farsang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02236v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02236v1)

**Summary:** Deploying pretrained policies in real-world applications presents substantial challenges that fundamentally limit the practical applicability of learning-based control systems. When autonomous systems encounter environmental changes in system dynamics, sensor drift, or task objectives, fixed policies rapidly degrade in performance. We show that employing Real-Time Recurrent Reinforcement Learning (RTRRL), a biologically plausible algorithm for online adaptation, can effectively fine-tune a pretr...

---

### 6. Scale-covariant spiking wavelets

**Authors:** Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02020v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02020v1)

**Summary:** We establish a theoretical connection between wavelet transforms and spiking neural networks through scale-space theory. We rely on the scale-covariant guarantees in the leaky integrate-and-fire neurons to implement discrete mother wavelets that approximate continuous wavelets. A reconstruction experiment demonstrates the feasibility of the approach and warrants further analysis to mitigate current approximation errors. Our work suggests a novel spiking signal representation that could enable mo...

---

### 7. SpikingGamma: Surrogate-Gradient Free and Temporally Precise Online Training of Spiking Neural Networks with Smoothed Delays

**Authors:** Roel Koopman, Sebastian Otte, Sander Bohté

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01978v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01978v1)

**Summary:** Neuromorphic hardware implementations of Spiking Neural Networks (SNNs) promise energy-efficient, low-latency AI through sparse, event-driven computation. Yet, training SNNs under fine temporal discretization remains a major challenge, hindering both low-latency responsiveness and the mapping of software-trained SNNs to efficient hardware. In current approaches, spiking neurons are modeled as self-recurrent units, embedded into recurrent networks to maintain state over time, and trained with BPT...

---

### 8. Enhancing Generalization in Evolutionary Feature Construction for Symbolic Regression through Vicinal Jensen Gap Minimization

**Authors:** Hengzhe Zhang, Qi Chen, Bing Xue, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01510v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01510v1)

**Summary:** Genetic programming-based feature construction has achieved significant success in recent years as an automated machine learning technique to enhance learning performance. However, overfitting remains a challenge that limits its broader applicability. To improve generalization, we prove that vicinal risk, estimated through noise perturbation or mixup-based data augmentation, is bounded by the sum of empirical risk and a regularization term-either finite difference or the vicinal Jensen gap. Leve...

---

### 9. Dynamic Heuristic Neuromorphic Solver for the Edge User Allocation Problem with Bayesian Confidence Propagation Neural Network

**Authors:** Kecheng Zhang, Anders Lansner, Ahsan Javed Awan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01294v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01294v1)

**Summary:** We propose a neuromorphic solver for the NP-hard Edge User Allocation problem using an attractor network with Winner-Takes-All (WTA) mechanism implemented with the Bayesian Confidence Propagation Neural Network (BCPNN) framework. Unlike previous energy-based attractor networks, our solver uses dynamic heuristic biasing to guide allocations in real time and introduces a "no allocation" state to each WTA motif, achieving near-optimal performance with an empirically upper-bounded number of time ste...

---

### 10. Unleashing the Potential of Differential Evolution through Individual-Level Strategy Diversity

**Authors:** Chenchen Feng, Minyang Chen, Zhuozhao Li, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01147v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01147v1)

**Summary:** Since Differential Evolution (DE) is sensitive to strategy choice, most existing variants pursue performance through adaptive mechanisms or intricate designs. While these approaches focus on adjusting strategies over time, the structural benefits that static strategy diversity may bring remain largely unexplored. To bridge this gap, we study the impact of individual-level strategy diversity on DE's search dynamics and performance, and introduce iStratDE (DE with individual-level strategies), a m...

---

### 11. Parallel Training in Spiking Neural Networks

**Authors:** Yanbin Huang, Man Yao, Yuqi Pan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01133v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01133v1)

**Summary:** The bio-inspired integrate-fire-reset mechanism of spiking neurons constitutes the foundation for efficient processing in Spiking Neural Networks (SNNs). Recent progress in large models demands that spiking neurons support highly parallel computation to scale efficiently on modern GPUs. This work proposes a novel functional perspective that provides general guidance for designing parallel spiking neurons. We argue that the reset mechanism, which induces complex temporal dependencies and hinders ...

---

### 12. The Stacked Autoencoder Evolution Hypothesis

**Authors:** Hiroyuki Iizuka

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01026v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01026v1)

**Summary:** This study introduces a novel theoretical framework, the Stacked Autoencoder Evolution Hypothesis, which proposes that biological evolutionary systems operate through multi-layered self-encoding and decoding processes, analogous to stacked autoencoders in deep learning. Rather than viewing evolution solely as gradual changes driven by mutation and selection, this hypothesis suggests that self-replication inherently compresses and reconstructs genetic information across hierarchical layers of abs...

---

### 13. Navigating Simply, Aligning Deeply: Winning Solutions for Mouse vs. AI 2025

**Authors:** Phu-Hoa Pham, Chi-Nguyen Tran, Dao Sy Duy Minh, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.00982v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00982v1)

**Summary:** Visual robustness and neural alignment remain critical challenges in developing artificial agents that can match biological vision systems. We present the winning approaches from Team HCMUS_TheFangs for both tracks of the NeurIPS 2025 Mouse vs. AI: Robust Visual Foraging Competition. For Track 1 (Visual Robustness), we demonstrate that architectural simplicity combined with targeted components yields superior generalization, achieving 95.4% final score with a lightweight two-layer CNN enhanced b...

---

### 14. Organismal Agency and Rapid Adaptation: The Phenopoiesis Algorithm for Phenotype-First Evolution

**Authors:** Nam H. Le

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.00978v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00978v1)

**Summary:** Evolutionary success depends on the capacity to adapt: organisms must respond to environmental challenges through both genetic innovation and lifetime learning. The gene-centric paradigm attributes evolutionary causality exclusively to genes, while Denis Noble's phenotype-first framework argues that organisms are active agents capable of interpreting genetic resources, learning from experience, and shaping their own development. However, this framework has remained philosophically intuitive but ...

---

### 15. NegaBent, No Regrets: Evolving Spectrally Flat Boolean Functions

**Authors:** Claude Carlet, Marko Ðurasevic, Ermes Franch, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00843v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00843v1)

**Summary:** Negabent Boolean functions are defined by having a flat magnitude spectrum under the nega-Hadamard transform. They exist in both even and odd dimensions, and the subclass of functions that are simultaneously bent and negabent (bent-negabent) has attracted interest due to the combined optimal periodic and negaperiodic spectral properties. In this work, we investigate how evolutionary algorithms can be used to evolve (bent-)negabent Boolean functions. Our experimental results indicate that evoluti...

---

### 16. IDEM Enough? Evolving Highly Nonlinear Idempotent Boolean Functions

**Authors:** Claude Carlet, Marko Ðurasevic, Domagoj Jakobovic, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00837v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00837v1)

**Summary:** Idempotent Boolean functions form a highly structured subclass of Boolean functions that is closely related to rotation symmetry under a normal-basis representation and to invariance under a fixed linear map in a polynomial basis. These functions are attractive as candidates for cryptographic design, yet their additional algebraic constraints make the search for high nonlinearity substantially more difficult than in the unconstrained case. In this work, we investigate evolutionary methods for co...

---

### 17. Evolving Interpretable Constitutions for Multi-Agent Simulation

**Authors:** Ujwal Kumar, Alice Saito, Hershraj Niranjani, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00755v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00755v1)

**Summary:** Constitutional AI has focused on single-model alignment using fixed principles. However, multi-agent systems create novel alignment challenges through emergent social dynamics. We present Constitutional Evolution, a framework for automatically discovering behavioral norms in multi-agent LLM systems. Using a grid-world simulation with survival pressure, we study the tension between individual and collective welfare, quantified via a Societal Stability Score S in [0,1] that combines productivity, ...

---

### 18. Surrogate Ensemble in Expensive Multi-Objective Optimization via Deep Q-Learning

**Authors:** Yuxin Wu, Hongshu Guo, Ting Huang, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00540v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00540v1)

**Summary:** Surrogate-assisted Evolutionary Algorithms~(SAEAs) have shown promising robustness in solving expensive optimization problems. A key aspect that impacts SAEAs' effectiveness is surrogate model selection, which in existing works is predominantly decided by human developer. Such human-made design choice introduces strong bias into SAEAs and may hurt their expected performance on out-of-scope tasks. In this paper, we propose a reinforcement learning-assisted ensemble framework, termed as SEEMOO, wh...

---

### 19. Reinforcement Learning-assisted Constraint Relaxation for Constrained Expensive Optimization

**Authors:** Qianhao Zhu, Sijie Ma, Zeyuan Ma, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00532v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00532v1)

**Summary:** Constraint handling plays a key role in solving realistic complex optimization problems. Though intensively discussed in the last few decades, existing constraint handling techniques predominantly rely on human experts' designs, which more or less fall short in utility towards general cases. Motivated by recent progress in Meta-Black-Box Optimization where automated algorithm design can be learned to boost optimization performance, in this paper, we propose learning effective, adaptive and gener...

---

### 20. Quality-Diversity Optimization as Multi-Objective Optimization

**Authors:** Xi Lin, Ping Guo, Yilu Liu, et al.

**Published:** 2026-01-31

🔗 [Paper](http://arxiv.org/abs/2602.00478v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00478v1)

**Summary:** The Quality-Diversity (QD) optimization aims to discover a collection of high-performing solutions that simultaneously exhibit diverse behaviors within a user-defined behavior space. This paradigm has stimulated significant research interest and demonstrated practical utility in domains including robot control, creative design, and adversarial sample generation. A variety of QD algorithms with distinct design principles have been proposed in recent years. Instead of proposing a new QD algorithm,...

---

### 21. COBRA++: Enhanced COBRA Optimizer with Augmented Surrogate Pool and Reinforced Surrogate Selection

**Authors:** Zipei Yu, Zhiyang Huang, Hongshu Guo, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.22624v2) | 📄 [PDF](https://arxiv.org/pdf/2601.22624v2)

**Summary:** The optimization problems in realistic world present significant challenges onto optimization algorithms, such as the expensive evaluation issue and complex constraint conditions. COBRA optimizer (including its up-to-date variants) is a representative and effective tool for addressing such optimization problems, which introduces 1) RBF surrogate to reduce online evaluation and 2) bi-stage optimization process to alternate search for feasible solution and optimal solution. Though promising, its d...

---

### 22. Detect and Act: Automated Dynamic Optimizer through Meta-Black-Box Optimization

**Authors:** Zijian Gao, Yuanting Zhong, Zeyuan Ma, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.22542v1) | 📄 [PDF](https://arxiv.org/pdf/2601.22542v1)

**Summary:** Dynamic Optimization Problems (DOPs) are challenging to address due to their complex nature, i.e., dynamic environment variation. Evolutionary Computation methods are generally advantaged in solving DOPs since they resemble dynamic biological evolution. However, existing evolutionary dynamic optimization methods rely heavily on human-crafted adaptive strategy to detect environment variation in DOPs, and then adapt the searching strategy accordingly. These hand-crafted strategies may perform inef...

---

### 23. Fairness-Aware Performance Evaluation for Multi-Party Multi-Objective Optimization

**Authors:** Zifan Zhao, Peilan Xu, Wenjian Luo

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.22497v1) | 📄 [PDF](https://arxiv.org/pdf/2601.22497v1)

**Summary:** In multiparty multiobjective optimization problems, solution sets are usually evaluated using classical performance metrics, aggregated across DMs. However, such mean-based evaluations may be unfair by favoring certain parties, as they assume identical geometric approximation quality to each party's PF carries comparable evaluative significance. Moreover, prevailing notions of MPMOP optimal solutions are restricted to strictly common Pareto optimal solutions, representing a narrow form of cooper...

---

### 24. Sheaf Neural Networks and biomedical applications

**Authors:** Aneeqa Mehrab, Jan Willem Van Looy, Pietro Demurtas, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2602.00159v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00159v1)

**Summary:** The purpose of this paper is to elucidate the theory and mathematical modelling behind the sheaf neural network (SNN) algorithm and then show how SNN can effectively answer to biomedical questions in a concrete case study and outperform the most popular graph neural networks (GNNs) as graph convolutional networks (GCNs), graph attention networks (GAT) and GraphSage.

---

### 25. Investigating the Interplay of Parameterization and Optimizer in Gradient-Free Topology Optimization: A Cantilever Beam Case Study

**Authors:** Jelle Westra, Iván Olarte Rodríguez, Niki van Stein, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.22241v2) | 📄 [PDF](https://arxiv.org/pdf/2601.22241v2)

**Summary:** Gradient-free black-box optimization (BBO) is widely used in engineering design and provides a flexible framework for topology optimization (TO), enabling the discovery of high-performing structural designs without requiring gradient information from simulations. Yet, its success depends on two key choices: the geometric parameterization defining the search space and the optimizer exploring it.   This study investigates this interplay through a compliance minimization problem for a cantilever be...

---

### 26. Lens-descriptor guided evolutionary algorithm for optimization of complex optical systems with glass choice

**Authors:** Kirill Antonov, Teus Tukker, Tiago Botari, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.22075v1) | 📄 [PDF](https://arxiv.org/pdf/2601.22075v1)

**Summary:** Designing high-performance optical lenses entails exploring a high-dimensional, tightly constrained space of surface curvatures, glass choices, element thicknesses, and spacings. In practice, standard optimizers (e.g., gradient-based local search and evolutionary strategies) often converge to a single local optimum, overlooking many comparably good alternatives that matter for downstream engineering decisions. We propose the Lens Descriptor-Guided Evolutionary Algorithm (LDG-EA), a two-stage fra...

---

### 27. Dependence of Equilibrium Propagation Training Success on Network Architecture

**Authors:** Qingshan Wang, Clara C. Wanjura, Florian Marquardt

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21945v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21945v1)

**Summary:** The rapid rise of artificial intelligence has led to an unsustainable growth in energy consumption. This has motivated progress in neuromorphic computing and physics-based training of learning machines as alternatives to digital neural networks. Many theoretical studies focus on simple architectures like all-to-all or densely connected layered networks. However, these may be challenging to realize experimentally, e.g. due to connectivity constraints. In this work, we investigate the performance ...

---

### 28. Adaptive Surrogate-Based Strategy for Accelerating Convergence Speed when Solving Expensive Unconstrained Multi-Objective Optimisation Problems

**Authors:** Tiwonge Msulira Banda, Alexandru-Ciprian Zăvoianu

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21885v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21885v1)

**Summary:** Multi-Objective Evolutionary Algorithms (MOEAs) have proven effective at solving Multi-Objective Optimisation Problems (MOOPs). However, their performance can be significantly hindered when applied to computationally intensive industrial problems. To address this limitation, we propose an adaptive surrogate modelling approach designed to accelerate the early-stage convergence speed of state-of-the-art MOEAs. This is important because it ensures that a solver can identify optimal or near-optimal ...

---

### 29. Evolution of Benchmark: Black-Box Optimization Benchmark Design through Large Language Model

**Authors:** Chen Wang, Sijie Ma, Zeyuan Ma, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21877v2) | 📄 [PDF](https://arxiv.org/pdf/2601.21877v2)

**Summary:** Benchmark Design in Black-Box Optimization (BBO) is a fundamental yet open-ended topic. Early BBO benchmarks are predominantly human-crafted, introducing expert bias and constraining diversity. Automating this design process can relieve the human-in-the-loop burden while enhancing diversity and objectivity. We propose Evolution of Benchmark (EoB), an automated BBO benchmark designer empowered by the large language model (LLM) and its program evolution capability. Specifically, we formulate bench...

---

### 30. READY: Reward Discovery for Meta-Black-Box Optimization

**Authors:** Zechuan Huang, Zhiguang Cao, Hongshu Guo, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21847v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21847v1)

**Summary:** Meta-Black-Box Optimization (MetaBBO) is an emerging avenue within Optimization community, where algorithm design policy could be meta-learned by reinforcement learning to enhance optimization performance. So far, the reward functions in existing MetaBBO works are designed by human experts, introducing certain design bias and risks of reward hacking. In this paper, we use Large Language Model~(LLM) as an automated reward discovery tool for MetaBBO. Specifically, we consider both effectiveness an...

---

### 31. General Self-Prediction Enhancement for Spiking Neurons

**Authors:** Zihan Huang, Zijie Xu, Yihan Huang, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21823v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21823v1)

**Summary:** Spiking Neural Networks (SNNs) are highly energy-efficient due to event-driven, sparse computation, but their training is challenged by spike non-differentiability and trade-offs among performance, efficiency, and biological plausibility. Crucially, mainstream SNNs ignore predictive coding, a core cortical mechanism where the brain predicts inputs and encodes errors for efficient perception. Inspired by this, we propose a self-prediction enhanced spiking neuron method that generates an internal ...

---

### 32. Error Amplification Limits ANN-to-SNN Conversion in Continuous Control

**Authors:** Zijie Xu, Zihan Huang, Yiting Dong, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21778v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21778v1)

**Summary:** Spiking Neural Networks (SNNs) can achieve competitive performance by converting already existing well-trained Artificial Neural Networks (ANNs), avoiding further costly training. This property is particularly attractive in Reinforcement Learning (RL), where training through environment interaction is expensive and potentially unsafe. However, existing conversion methods perform poorly in continuous control, where suitable baselines are largely absent. We identify error amplification as the key ...

---

### 33. Meta Context Engineering via Agentic Skill Evolution

**Authors:** Haoran Ye, Xuning He, Vincent Arak, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21557v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21557v1)

**Summary:** The operational efficacy of large language models relies heavily on their inference-time context. This has established Context Engineering (CE) as a formal discipline for optimizing these inputs. Current CE methods rely on manually crafted harnesses, such as rigid generation-reflection workflows and predefined context schemas. They impose structural biases and restrict context optimization to a narrow, intuition-bound design space. To address this, we introduce Meta Context Engineering (MCE), a ...

---

### 34. LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI

**Authors:** Niki van Stein, Anna V. Kononova, Lars Kotthoff, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21511v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21511v1)

**Summary:** Large language models have enabled automated algorithm design (AAD) by generating optimization algorithms directly from natural-language prompts. While evolutionary frameworks such as LLaMEA demonstrate strong exploratory capabilities across the algorithm design space, their search dynamics are entirely driven by fitness feedback, leaving substantial information about the generated code unused. We propose a mechanism for guiding AAD using feedback constructed from graph-theoretic and complexity ...

---

### 35. MAR: Efficient Large Language Models via Module-aware Architecture Refinement

**Authors:** Junhong Cai, Guiqin Wang, Kejie Zhao, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21503v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21503v1)

**Summary:** Large Language Models (LLMs) excel across diverse domains but suffer from high energy costs due to quadratic attention and dense Feed-Forward Network (FFN) operations. To address these issues, we propose Module-aware Architecture Refinement (MAR), a two-stage framework that integrates State Space Models (SSMs) for linear-time sequence modeling and applies activation sparsification to reduce FFN costs. In addition, to mitigate low information density and temporal mismatch in integrating Spiking N...

---

### 36. Task-free Adaptive Meta Black-box Optimization

**Authors:** Chao Wang, Licheng Jiao, Lingling Li, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21475v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21475v1)

**Summary:** Handcrafted optimizers become prohibitively inefficient for complex black-box optimization (BBO) tasks. MetaBBO addresses this challenge by meta-learning to automatically configure optimizers for low-level BBO tasks, thereby eliminating heuristic dependencies. However, existing methods typically require extensive handcrafted training tasks to learn meta-strategies that generalize to target tasks, which poses a critical limitation for realistic applications with unknown task distributions. To ove...

---

### 37. BrainFuse: a unified infrastructure integrating realistic biological modeling and core AI methodology

**Authors:** Baiyu Chen, Yujie Wu, Siyuan Xu, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21407v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21407v1)

**Summary:** Neuroscience and artificial intelligence represent distinct yet complementary pathways to general intelligence. However, amid the ongoing boom in AI research and applications, the translational synergy between these two fields has grown increasingly elusive-hampered by a widening infrastructural incompatibility: modern AI frameworks lack native support for biophysical realism, while neural simulation tools are poorly suited for gradient-based optimization and neuromorphic hardware deployment. To...

---

### 38. NEXUS: Bit-Exact ANN-to-SNN Equivalence via Neuromorphic Gate Circuits with Surrogate-Free Training

**Authors:** Zhengzheng Tang

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21279v2) | 📄 [PDF](https://arxiv.org/pdf/2601.21279v2)

**Summary:** Spiking Neural Networks (SNNs) promise energy-efficient computing through event-driven sparsity, yet all existing approaches sacrifice accuracy by approximating continuous values with discrete spikes. We propose NEXUS, a framework that achieves bit-exact ANN-to-SNN equivalence -- not approximate, but mathematically identical outputs. Our key insight is constructing all arithmetic operations, both linear and nonlinear, from pure IF neuron logic gates that implement IEEE-754 compliant floating-poi...

---

### 39. Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels

**Authors:** Micah Rentschler, Jesse Roberts

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21268v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21268v1)

**Summary:** Most reinforcement learning (RL) methods for training large language models (LLMs) require ground-truth labels or task-specific verifiers, limiting scalability when correctness is ambiguous or expensive to obtain. We introduce Reinforcement Learning from Meta-Evaluation (RLME), which optimizes a generator using reward derived from an evaluator's answers to natural-language meta-questions (e.g., "Is the answer correct?" or "Is the reasoning logically consistent?"). RLME treats the evaluator's pro...

---

### 40. Diversifying Toxicity Search in Large Language Models Through Speciation

**Authors:** Onkar Shelar, Travis Desell

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20981v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20981v1)

**Summary:** Evolutionary prompt search is a practical black-box approach for red teaming large language models (LLMs), but existing methods often collapse onto a small family of high-performing prompts, limiting coverage of distinct failure modes. We present a speciated quality-diversity (QD) extension of ToxSearch that maintains multiple high-toxicity prompt niches in parallel rather than optimizing a single best prompt. ToxSearch-S introduces unsupervised prompt speciation via a search methodology that ma...

---

### 41. Tournament Informed Adversarial Quality Diversity

**Authors:** Timothée Anne, Noah Syrkis, Meriem Elhosni, et al.

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19562v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19562v1)

**Summary:** Quality diversity (QD) is a branch of evolutionary computation that seeks high-quality and behaviorally diverse solutions to a problem. While adversarial problems are common, classical QD cannot be easily applied to them, as both the fitness and the behavior depend on the opposing solutions. Recently, Generational Adversarial MAP-Elites (GAME) has been proposed to coevolve both sides of an adversarial problem by alternating the execution of a multi-task QD algorithm against previous elites, call...

---

### 42. Rethinking Intelligence: Brain-like Neuron Network

**Authors:** Weifeng Liu

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19508v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19508v1)

**Summary:** Since their inception, artificial neural networks have relied on manually designed architectures and inductive biases to better adapt to data and tasks. With the rise of deep learning and the expansion of parameter spaces, they have begun to exhibit brain-like functional behaviors. Nevertheless, artificial neural networks remain fundamentally different from biological neural systems in structural organization, learning mechanisms, and evolutionary pathways.   From the perspective of neuroscience...

---

### 43. Posterior Distribution-assisted Evolutionary Dynamic Optimization as an Online Calibrator for Complex Social Simulations

**Authors:** Peng Yang, Zhenhua Yang, Boquan Jiang, et al.

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19481v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19481v1)

**Summary:** The calibration of simulators for complex social systems aims to identify the optimal parameter that drives the output of the simulator best matching the target data observed from the system. As many social systems may change internally over time, calibration naturally becomes an online task, requiring parameters to be updated continuously to maintain the simulator's fidelity. In this work, the online setting is first formulated as a dynamic optimization problem (DOP), requiring the search for a...

---

### 44. ROIDS: Robust Outlier-Aware Informed Down-Sampling

**Authors:** Alina Geiger, Martin Briesch, Dominik Sobania, et al.

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19477v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19477v1)

**Summary:** Informed down-sampling (IDS) is known to improve performance in symbolic regression when combined with various selection strategies, especially tournament selection. However, recent work found that IDS's gains are not consistent across all problems. Our analysis reveals that IDS performance is worse for problems containing outliers. IDS systematically favors including outliers in subsets which pushes GP towards finding solutions that overfit to outliers. To address this, we introduce ROIDS (Robu...

---

### 45. NeuroAI and Beyond

**Authors:** Jean-Marc Fellous, Gert Cauwenberghs, Cornelia Fermüller, et al.

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19955v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19955v1)

**Summary:** Neuroscience and Artificial Intelligence (AI) have made significant progress in the past few years but have only been loosely inter-connected. Based on a workshop held in August 2025, we identify current and future areas of synergism between these two fields. We focus on the subareas of embodiment, language and communication, robotics, learning in humans and machines and Neuromorphic engineering to take stock of the progress made so far, and possible promising new future avenues. Overall, we adv...

---

### 46. HEATACO: Heatmap-Guided Ant Colony Decoding for Large-Scale Travelling Salesman Problems

**Authors:** Bo-Cheng Lin, Yi Mei, Mengjie Zhang

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.19041v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19041v1)

**Summary:** Heatmap-based non-autoregressive solvers for large-scale Travelling Salesman Problems output dense edge-probability scores, yet final performance largely hinges on the decoder that must satisfy degree-2 constraints and form a single Hamiltonian tour. Greedy commitment can cascade into irreparable mistakes at large $N$, whereas MCTS-guided local search is accurate but compute-heavy and highly engineered. We instead treat the heatmap as a soft edge prior and cast decoding as probabilistic tour con...

---

### 47. SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model

**Authors:** Jan Hagnberger, Mathias Niepert

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18707v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18707v1)

**Summary:** Machine learning-based surrogate models have emerged as more efficient alternatives to numerical solvers for physical simulations over complex geometries, such as car bodies. Many existing models incorporate the simulation mesh as an additional input, thereby reducing prediction errors. However, generating a simulation mesh for new geometries is computationally costly. In contrast, mesh-free methods, which do not rely on the simulation mesh, typically incur higher errors. Motivated by these cons...

---

### 48. Global Optimization of Atomic Clusters via Physically-Constrained Tensor Train Decomposition

**Authors:** Konstantin Sozykin, Nikita Rybin, Andrei Chertkov, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18592v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18592v1)

**Summary:** The global optimization of atomic clusters represents a fundamental challenge in computational chemistry and materials science due to the exponential growth of local minima with system size (i.e., the curse of dimensionality). We introduce a novel framework that overcomes this limitation by exploiting the low-rank structure of potential energy surfaces through Tensor Train (TT) decomposition. Our approach combines two complementary TT-based strategies: the algebraic TTOpt method, which utilizes ...

---

### 49. Scaling Behaviors of Evolutionary Algorithms on GPUs: When Does Parallelism Pay Off?

**Authors:** Xinmeng Yu, Tao Jiang, Ran Cheng, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18446v2) | 📄 [PDF](https://arxiv.org/pdf/2601.18446v2)

**Summary:** Evolutionary algorithms (EAs) are increasingly implemented on graphics processing units (GPUs) to leverage parallel processing capabilities for enhanced efficiency. However, existing studies largely emphasize the raw speedup obtained by porting individual algorithms from CPUs to GPUs. Consequently, these studies offer limited insight into when and why GPU parallelism fundamentally benefits EAs. To address this gap, we investigate how GPU parallelism alters the behavior of EAs beyond simple accel...

---

### 50. LLM Driven Design of Continuous Optimization Problems with Controllable High-level Properties

**Authors:** Urban Skvorc, Niki van Stein, Moritz Seiler, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18846v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18846v1)

**Summary:** Benchmarking in continuous black-box optimisation is hindered by the limited structural diversity of existing test suites such as BBOB. We explore whether large language models embedded in an evolutionary loop can be used to design optimisation problems with clearly defined high-level landscape characteristics. Using the LLaMEA framework, we guide an LLM to generate problem code from natural-language descriptions of target properties, including multimodality, separability, basin-size homogeneity...

---

## q-bio.NC

**50 papers**

### 1. MEG-XL: Data-Efficient Brain-to-Text via Long-Context Pre-Training

**Authors:** Dulhan Jayalath, Oiwi Parker Jones

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02494v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02494v1)

**Summary:** Clinical brain-to-text interfaces are designed for paralysed patients who cannot provide extensive training recordings. Pre-training improves data-efficient generalisation by learning statistical priors across subjects, but these priors critically depend on context. While natural speech might unfold gradually over minutes, most methods pre-train with only a few seconds of context. Thus, we propose MEG-XL, a model pre-trained with 2.5 minutes of MEG context per sample, 5-300x longer than prior wo...

---

### 2. Community-Level Modeling of Gyral Folding Patterns for Robust and Anatomically Informed Individualized Brain Mapping

**Authors:** Minheng Chen, Tong Chen, Yan Zhuang, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01482v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01482v1)

**Summary:** Cortical folding exhibits substantial inter-individual variability while preserving stable anatomical landmarks that enable fine-scale characterization of cortical organization. Among these, the three-hinge gyrus (3HG) serves as a key folding primitive, showing consistent topology yet meaningful variations in morphology, connectivity, and function. Existing landmark-based methods typically model each 3HG independently, ignoring that 3HGs form higher-order folding communities that capture mesosca...

---

### 3. Vulnerability-Amplifying Interaction Loops: a systematic failure mode in AI chatbot mental-health interactions

**Authors:** Veith Weilnhammer, Kevin YC Hou, Raymond Dolan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01347v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01347v1)

**Summary:** Millions of users turn to consumer AI chatbots to discuss behavioral and mental health concerns. While this presents unprecedented opportunities to deliver population-level support, it also highlights an urgent need to develop rigorous and scalable safety evaluations. Here we introduce SIM-VAIL, an AI chatbot auditing framework that captures how harmful AI chatbot responses manifest across a range of mental-health contexts. SIM-VAIL pairs a simulated human user, harboring a distinct psychiatric ...

---

### 4. Inter- and Intra-Subject Variability in EEG: A Systematic Survey

**Authors:** Xuan-The Tran, Thien-Nhan Vo, Son-Tung Vu, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01019v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01019v1)

**Summary:** Electroencephalography (EEG) underpins neuroscience, clinical neurophysiology, and brain-computer interfaces (BCIs), yet pronounced inter- and intra-subject variability limits reliability, reproducibility, and translation. This systematic review studies that quantified or modeled EEG variability across resting-state, event-related potentials (ERPs), and task-related/BCI paradigms (including motor imagery and SSVEP) in healthy and clinical cohorts. Across paradigms, inter-subject differences are ...

---

### 5. The Where and How of Touch: A Review of Tactile Localization Research

**Authors:** Xaver Fuchs, Jason A. M. Khoury, Sergiu Tcaci Popescu, et al.

**Published:** 2026-01-30

🔗 [Paper](http://arxiv.org/abs/2601.23023v1) | 📄 [PDF](https://arxiv.org/pdf/2601.23023v1)

**Summary:** Tactile localization is the seemingly simple ability to 'tell' where a touch has occurred. However, how this ability is assessed, and what conclusions are drawn from experiments, depends on the theoretical ideas that inspire the research. Here, we review both theoretical frameworks and methodological approaches based on a systematic web-based literature search on tactile localization. After presenting current theories of tactile localization, we discuss task characteristics that differentiate cu...

---

### 6. Deep Learning Pose Estimation for Multi-Label Recognition of Combined Hyperkinetic Movement Disorders

**Authors:** Laura Cif, Diane Demailly, Gabriella A. Horvàth, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2602.00163v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00163v1)

**Summary:** Hyperkinetic movement disorders (HMDs) such as dystonia, tremor, chorea, myoclonus, and tics are disabling motor manifestations across childhood and adulthood. Their fluctuating, intermittent, and frequently co-occurring expressions hinder clinical recognition and longitudinal monitoring, which remain largely subjective and vulnerable to inter-rater variability. Objective and scalable methods to distinguish overlapping HMD phenotypes from routine clinical videos are still lacking. Here, we devel...

---

### 7. How 'Neural' is a Neural Foundation Model?

**Authors:** Johannes Bertram, Luciano Dyballa, Anderson Keller, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21508v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21508v1)

**Summary:** Foundation models have shown remarkable success in fitting biological visual systems; however, their black-box nature inherently limits their utility for understanding brain function. Here, we peek inside a SOTA foundation model of neural activity (Wang et al., 2025) as a physiologist might, characterizing each 'neuron' based on its temporal response properties to parametric stimuli. We analyze how different stimuli are represented in neural activity space by building decoding manifolds, and we ...

---

### 8. Differential Dynamic Causal Nets: Model Construction, Identification and Group Comparisons

**Authors:** Kang You, Gary Green, Jian Zhang

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21478v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21478v1)

**Summary:** Pathophysiolpgical modelling of brain systems from microscale to macroscale remains difficult in group comparisons partly because of the infeasibility of modelling the interactions of thousands of neurons at the scales involved. Here, to address the challenge, we present a novel approach to construct differential causal networks directly from electroencephalogram (EEG) data. The proposed network is based on conditionally coupled neuronal circuits which describe the average behaviour of interacti...

---

### 9. BrainFuse: a unified infrastructure integrating realistic biological modeling and core AI methodology

**Authors:** Baiyu Chen, Yujie Wu, Siyuan Xu, et al.

**Published:** 2026-01-29

🔗 [Paper](http://arxiv.org/abs/2601.21407v1) | 📄 [PDF](https://arxiv.org/pdf/2601.21407v1)

**Summary:** Neuroscience and artificial intelligence represent distinct yet complementary pathways to general intelligence. However, amid the ongoing boom in AI research and applications, the translational synergy between these two fields has grown increasingly elusive-hampered by a widening infrastructural incompatibility: modern AI frameworks lack native support for biophysical realism, while neural simulation tools are poorly suited for gradient-based optimization and neuromorphic hardware deployment. To...

---

### 10. An explainable framework for the relationship between dementia and glucose metabolism patterns

**Authors:** C. Vázquez-García, F. J. Martínez-Murcia, F. Segovia Román, et al.

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20480v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20480v1)

**Summary:** High-dimensional neuroimaging data presents challenges for assessing neurodegenerative diseases due to complex non-linear relationships. Variational Autoencoders (VAEs) can encode scans into lower-dimensional latent spaces capturing disease-relevant features. We propose a semi-supervised VAE framework with a flexible similarity regularization term that aligns selected latent variables with clinical or biomarker measures of dementia progression. This allows adapting the similarity metric and supe...

---

### 11. Assembling the Mind's Mosaic: Towards EEG Semantic Intent Decoding

**Authors:** Jiahe Li, Junru Chen, Fanqi Shen, et al.

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20447v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20447v1)

**Summary:** Enabling natural communication through brain-computer interfaces (BCIs) remains one of the most profound challenges in neuroscience and neurotechnology. While existing frameworks offer partial solutions, they are constrained by oversimplified semantic representations and a lack of interpretability. To overcome these limitations, we introduce Semantic Intent Decoding (SID), a novel framework that translates neural activity into natural language by modeling meaning as a flexible set of composition...

---

### 12. Implications of temporal sampling in voltage imaging microscopy

**Authors:** Jakub Czuchnowski, Jerome Mertz

**Published:** 2026-01-28

🔗 [Paper](http://arxiv.org/abs/2601.20236v1) | 📄 [PDF](https://arxiv.org/pdf/2601.20236v1)

**Summary:** Significance: Voltage imaging microscopy has emerged as a powerful tool to investigate neural activity both in vivo and in vitro. Various imaging approaches have been developed, including point-scanning, line-scanning and wide-field microscopes, however the effects of their different temporal sampling methods on signal fidelity have not yet been fully investigated. Aim: To provide an analysis of the inherent advantages and disadvantages of temporal sampling in scanning and wide-field microscopes...

---

### 13. Stroboscopic motion reversals in delay-coupled neural fields

**Authors:** Noah Parks, Zachary P Kilpatrick

**Published:** 2026-01-27

🔗 [Paper](http://arxiv.org/abs/2601.19125v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19125v1)

**Summary:** Visual illusions provide a window into the mechanisms underlying visual processing, and dynamical neural circuit models offer a natural framework for proposing and testing theories of their emergence. We propose and analyze a delay-coupled neural field model that explains stroboscopic percepts arising from the subsampling of a moving, often rotating, stimulus, such as the wagon-wheel illusion. Motivated by the role of activity propagation delays in shaping visual percepts, we study neural fields...

---

### 14. Smooth embeddings in contracting recurrent networks driven by regular dynamics: A synthesis for neural representation

**Authors:** Vikas N. O'Reilly-Shah, Alessandro Maria Selvitella

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.19019v1) | 📄 [PDF](https://arxiv.org/pdf/2601.19019v1)

**Summary:** Recurrent neural networks trained for time-series prediction often develop latent trajectories that preserve qualitative structure of the dynamical systems generating their inputs. Recent empirical work has documented topology-preserving latent organization in trained recurrent models, and recent theoretical results in reservoir computing establish conditions under which the synchronization map is an embedding. Here we synthesize these threads into a unified account of when contracting recurrent...

---

### 15. Schema-based active inference supports rapid generalization of experience and frontal cortical coding of abstract structure

**Authors:** Toon Van de Maele, Tim Verbelen, Dileep George, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18946v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18946v1)

**Summary:** Schemas -- abstract relational structures that capture the commonalities across experiences -- are thought to underlie humans' and animals' ability to rapidly generalize knowledge, rebind new experiences to existing structures, and flexibly adapt behavior across contexts. Despite their central role in cognition, the computational principles and neural mechanisms supporting schema formation and use remain elusive. Here, we introduce schema-based hierarchical active inference (S-HAI), a novel comp...

---

### 16. Closed Eyes and Coil Size -- Effects on Motor Threshold and Intracortical Inhibition, measured with TMS

**Authors:** Meher Sabharwal, Narin Suleyman, Gabriel R. Palma, et al.

**Published:** 2026-01-26

🔗 [Paper](http://arxiv.org/abs/2601.18286v1) | 📄 [PDF](https://arxiv.org/pdf/2601.18286v1)

**Summary:** Rationale: Transcranial magnetic stimulation (TMS)-based measures such as resting motor threshold (RMT) and short interval intracortical inhibition (SICI) are widely employed to study motor cortical and corticospinal tract function, and effects of diseases and drug therapies thereon. However, the effect of key experimental factors, including as eye state (open or closed) or stimulating coil size, remain unclear. As such, it is unknown whether these factors must be kept consistent across multi-ce...

---

### 17. AI and World Models

**Authors:** Robert Worden

**Published:** 2026-01-25

🔗 [Paper](http://arxiv.org/abs/2601.17796v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17796v1)

**Summary:** While large neural nets perform impressively on specific tasks, they are unreliable and unsafe, as is shown by the persistent hallucinations of large language models. This paper shows that large neural nets are intrinsically unreliable, because it is not possible to make or validate a tractable theory of how a neural net works. There is no reliable way to extrapolate its performance from a limited number of test cases to an unlimited set of use cases. To have confidence in the performance of a n...

---

### 18. Sampling in the Euclidean Motion Group and a Problem from Brain's Primary Visual Cortex

**Authors:** Davide Barbieri

**Published:** 2026-01-24

🔗 [Paper](http://arxiv.org/abs/2601.17528v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17528v1)

**Summary:** We study a sampling problem for the abstract wavelet transform associated with the quasiregular representation of the $SE(2)$ group, for a modulated gaussian mother wavelet. This problem is motivated by the behavior of brain's primary visual cortex. We provide a characterization in terms of a dual Gramian matrix, and study numerically the relationships among the parameters defining the sampling and the mother wavelet.

---

### 19. Unsupervised sleep-like intra- and inter-layer plasticity categorizes and improves energy efficiency in a multilayer spiking network

**Authors:** Leonardo Tonielli, Cosimo Lupo, Elena Pastorelli, et al.

**Published:** 2026-01-24

🔗 [Paper](http://arxiv.org/abs/2601.17523v1) | 📄 [PDF](https://arxiv.org/pdf/2601.17523v1)

**Summary:** Sleep is thought to support memory consolidation and the recovery of optimal energetic regime by reorganizing synaptic connectivity, yet how plasticity across hierarchical brain circuits contributes to abstraction and energy efficiency remains unclear. Here we study a spiking multi-layer network alternating wake-like and deep-sleep-like states, with state-dependent dendritic integration and synaptic plasticity in a biologically inspired thalamo-cortical framework. During wakefulness, the model l...

---

### 20. Neural Agonist-Antagonist Coupling in the Absence of Mechanical Coupling after Targeted Muscle Reinnervation

**Authors:** Laura Ferrante, Anna Boesendorfer, Benedikt Baumgartner, et al.

**Published:** 2026-01-23

🔗 [Paper](http://arxiv.org/abs/2601.16689v1) | 📄 [PDF](https://arxiv.org/pdf/2601.16689v1)

**Summary:** Following limb amputation and targeted muscle reinnervation (TMR), nerves supplying agonist and antagonist muscles are rerouted into separate targeted muscles, disrupting natural neuromechanical coupling between muscle groups. Using high-density intramuscular microelectrode arrays in reinnervated muscles, we show that neural signals for agonist and antagonist tasks remain functionally coupled: motor units active during agonist tasks were also recruited during corresponding antagonist tasks, desp...

---

### 21. Cognitively-Inspired Tokens Overcome Egocentric Bias in Multimodal Models

**Authors:** Bridget Leonard, Scott O. Murray

**Published:** 2026-01-23

🔗 [Paper](http://arxiv.org/abs/2601.16378v1) | 📄 [PDF](https://arxiv.org/pdf/2601.16378v1)

**Summary:** Multimodal language models (MLMs) perform well on semantic vision-language tasks but fail at spatial reasoning that requires adopting another agent's visual perspective. These errors reflect a persistent egocentric bias and raise questions about whether current models support allocentric reasoning. Inspired by human spatial cognition, we introduce perspective tokens, specialized embeddings that encode orientation through either (1) embodied body-keypoint cues or (2) abstract representations supp...

---

### 22. Resting-State Functional Connectivity Correlates of Emotional Memory Control under Cognitive load in Subclinical Anxiety

**Authors:** Shruti Kinger, Mrinmoy Chakrabarty

**Published:** 2026-01-22

🔗 [Paper](http://arxiv.org/abs/2601.15689v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15689v1)

**Summary:** Volitional memory control supports adaptive cognition by enabling intentional Recall of goal-relevant information and Suppression of unwanted memories. While neural mechanisms underlying Recall and Suppression have been studied largely in isolation, less is known about the large-scale brain networks supporting these processes under competing cognitive demands, particularly as a function of subclinical anxiety. Here, we examined control of emotionally valenced memories during directed Recall and ...

---

### 23. Machine learning-enhanced non-amnestic Alzheimer's disease diagnosis from MRI and clinical features

**Authors:** Megan A. Witherow, Michael L. Evans, Ahmed Temtam, et al.

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15530v2) | 📄 [PDF](https://arxiv.org/pdf/2601.15530v2)

**Summary:** Alzheimer's disease (AD), defined as an abnormal buildup of amyloid plaques and tau tangles in the brain can be diagnosed with high accuracy based on protein biomarkers via PET or CSF analysis. However, due to the invasive nature of biomarker collection, most AD diagnoses are made in memory clinics using cognitive tests and evaluation of hippocampal atrophy based on MRI. While clinical assessment and hippocampal volume show high diagnostic accuracy for amnestic or typical AD (tAD), a substantial...

---

### 24. Dynamic Mean Field Theories for Nonlinear Noise in Recurrent Neuronal Networks

**Authors:** Shoshana Chipman, Brent Doiron

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15462v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15462v1)

**Summary:** Strong, correlated noise in recurrent neural circuits often passes through nonlinear transfer functions, complicating dynamical mean-field analyses of complex phenomena such as transients and bifurcations. We introduce a method that replaces nonlinear functions of Ornstein-Uhlenbeck (OU) noise with a Gaussian-equivalent process matched in mean and covariance, and combine this with a lognormal moment closure for expansive nonlinearities to derive a closed dynamical mean-field theory for recurrent...

---

### 25. Circadian Modulation of Semantic Exploration in Social Media Language

**Authors:** Vuong Hung Truong, Mariana Gabrielle Cangco Reyes, Masatoshi Koizumi, et al.

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15091v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15091v1)

**Summary:** Human cognition exhibits strong circadian modulation, yet its influence on high-dimensional semantic behavior remains poorly understood. Using large-scale Reddit data, we quantify time-of-day variation in language use by embedding text into a pretrained transformer model and measuring semantic entropy as an index of linguistic exploration-exploitation, for which we show a robust circadian rhythmicity that could be entrained by seasonal light cues. Distinguishing between local and global semantic...

---

### 26. Single-Node Wilson--Cowan Model Accounts for Speech-Evoked $γ$-Band Deficits in Schizophrenia

**Authors:** Zhengdi Zhang, Yan Xu, Wenjun Xia

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.15032v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15032v1)

**Summary:** Cortical gamma ($γ$)-band activity reflects local excitation-inhibition (E/I) balance. In schizophrenia (SCZ), reduced task-evoked gamma suggests altered E/I dynamics, but it is unclear whether differences stem from input properties or systematic shifts in E/I operating point and gain. We coupled a cochlear-inspired speech front end to a Wilson-Cowan E/I model to simulate gamma responses across three conditions: Healthy, SCZ-speech, and SCZ-semantics. Metrics included event-related spectral pert...

---

### 27. Power-Law Scaling in the Classification Performance of Small-Scale Spiking Neural Networks

**Authors:** Zhengdi Zhang, Cong Han, Wenjun Xia

**Published:** 2026-01-21

🔗 [Paper](http://arxiv.org/abs/2601.14961v1) | 📄 [PDF](https://arxiv.org/pdf/2601.14961v1)

**Summary:** This paper investigates the classification capability of small-scale spiking neural networks based on the Leaky Integrate-and-Fire (LIF) neuron model. We analyze the relationship between classification accuracy and three factors: the number of neurons, the number of stimulus nodes, and the number of classification categories. Notably, we employ a large language model (LLM) to assist in discovering the underlying functional relationships among these variables, and compare its performance against ...

---

### 28. "Just in Time" World Modeling Supports Human Planning and Reasoning

**Authors:** Tony Chen, Sam Cheyette, Kelsey Allen, et al.

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.14514v1) | 📄 [PDF](https://arxiv.org/pdf/2601.14514v1)

**Summary:** Probabilistic mental simulation is thought to play a key role in human reasoning, planning, and prediction, yet the demands of simulation in complex environments exceed realistic human capacity limits. A theory with growing evidence is that people simulate using simplified representations of the environment that abstract away from irrelevant details, but it is unclear how people determine these simplifications efficiently. Here, we present a "Just-in-Time" framework for simulation-based reasonin...

---

### 29. A Dual-Head Transformer-State-Space Architecture for Neurocircuit Mechanism Decomposition from fMRI

**Authors:** Cole Korponay

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.15344v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15344v1)

**Summary:** Precision psychiatry aspires to elucidate brain-based biomarkers of psychopathology to bolster disease risk assessment and treatment development. To this end, functional magnetic resonance imaging (fMRI) has helped triangulate brain circuits whose functional features are correlated with or even predictive of forms of psychopathology. Yet, fMRI biomarkers to date remain largely descriptive identifiers of where, rather than how, neurobiology is aberrant, limiting their utility for guiding treatmen...

---

### 30. MooneyMaker: A Python package to create ambiguous two-tone images

**Authors:** Lars C. Reining, Thabo Matthies, Luisa Haussner, et al.

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.14077v1) | 📄 [PDF](https://arxiv.org/pdf/2601.14077v1)

**Summary:** Mooney images are high-contrast, two-tone visual stimuli, created by thresholding photographic images. They allow researchers to separate image content from image understanding, making them valuable for studying visual perception. An ideal Mooney image for this purpose achieves a specific balance: it initially appears unrecognizable but becomes fully interpretable to the observer after seeing the original template. Researchers traditionally created these stimuli manually using subjective criteri...

---

### 31. Optimal Calibration of the endpoint-corrected Hilbert Transform

**Authors:** Eike Osmers, Dorothea Kolossa

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.13962v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13962v1)

**Summary:** Accurate, low-latency estimates of the instantaneous phase of oscillations are essential for closed-loop sensing and actuation, including (but not limited to) phase-locked neurostimulation and other real-time applications. The endpoint-corrected Hilbert transform (ecHT) reduces boundary artefacts of the Hilbert transform by applying a causal narrow-band filter to the analytic spectrum. This improves the phase estimate at the most recent sample. Despite its widespread empirical use, the systemati...

---

### 32. Audio Outperforms Text for Visual Decoding

**Authors:** Zhengdi Zhang, Hao Zhang, Wenjun Xia

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.13866v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13866v1)

**Summary:** Decoding visual semantic representations from human brain activity is a significant challenge. While recent zero-shot decoding approaches have improved performance by leveraging aligned image-text datasets, they overlook a fundamental aspect of human cognition: semantic understanding is inherently anchored in the auditory modality of speech, not text. To address this, our study introduces the first comparative framework for evaluating auditory versus textual semantic modalities in zero-shot visu...

---

### 33. Learning Discrete Successor Transitions in Continuous Attractor Networks: Emergence, Limits, and Topological Constraints

**Authors:** Daniel Brownell

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2601.15336v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15336v1)

**Summary:** Continuous attractor networks (CANs) are a well-established class of models for representing low-dimensional continuous variables such as head direction, spatial position, and phase. In canonical spatial domains, transitions along the attractor manifold are driven by continuous displacement signals, such as angular velocity-provided by sensorimotor systems external to the CAN itself. When such signals are not explicitly provided as dedicated displacement inputs, it remains unclear whether attrac...

---

### 34. Explore Brain-Inspired Machine Intelligence for Connecting Dots on Graphs Through Holographic Blueprint of Oscillatory Synchronization

**Authors:** Tingting Dan, Jiaqi Ding, Guorong Wu

**Published:** 2026-01-20

🔗 [Paper](http://arxiv.org/abs/2602.00057v1) | 📄 [PDF](https://arxiv.org/pdf/2602.00057v1)

**Summary:** Neural coupling in both neuroscience and artificial intelligence emerges as dynamic oscillatory patterns that encode abstract concepts. To this end, we hypothesize that a deeper understanding of the neural mechanisms governing brain rhythms can inspire next-generation design principles for machine learning algorithms, leading to improved efficiency and robustness. Building on this idea, we first model evolving brain rhythms through the interference of spontaneously synchronized neural oscillatio...

---

### 35. A First Step for Expansion X-Ray Microscopy: Achieving Contrast in Expanded Tissues Sufficient to Reveal Cell Bodies

**Authors:** Logan Thrasher Collins

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.13370v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13370v1)

**Summary:** Existing methods in nanoscale connectomics are at present too slow to map entire mammalian brains. As an emerging approach, expansion microscopy (ExM) has enormous promise, yet it still suffers from throughput limitations. Mapping the human brain and even mapping nonhuman primate brains therefore remain distant goals. While ExM increases effective resolution linearly, it enlarges tissue volume cubically, which dramatically increases imaging time. As a rapid tomographic technique, X-ray microscop...

---

### 36. Multifaceted neural representation of words in naturalistic language

**Authors:** Xuan Yang, Chuanji Gao, Cheng Xiao, et al.

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.13297v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13297v1)

**Summary:** Understanding how the brain represents the multifaceted properties of words in context is essential for explaining the neural architecture of human language. Here, we combine large-scale psycholinguistic modeling with naturalistic fMRI to uncover the latent structure of word properties and their neural representations during narrative comprehension. By analyzing 106 psycholinguistic variables across 13,850 English words, we identified eight interpretable latent dimensions spanning lexical usage,...

---

### 37. Polyphonic Intelligence: Constraint-Based Emergence, Pluralistic Inference, and Non-Dominating Integration

**Authors:** Alexander D Shaw

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.13182v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13182v1)

**Summary:** Across neuroscience, artificial intelligence, and related fields, dominant models of intelligence typically privilege convergence: uncertainty is reduced, competing explanations are eliminated, and behaviour is governed by the optimisation of a single objective or policy. While this framing has proved powerful in many settings, it sits uneasily with biological and adaptive systems that maintain redundancy, ambiguity, and parallel explanatory processes over extended timescales. Here we propose an...

---

### 38. Global stability of a Hebbian/anti-Hebbian network for principal subspace learning

**Authors:** David Lipshutz, Robert J. Lipshutz

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.13170v1) | 📄 [PDF](https://arxiv.org/pdf/2601.13170v1)

**Summary:** Biological neural networks self-organize according to local synaptic modifications to produce stable computations. How modifications at the synaptic level give rise to such computations at the network level remains an open question. Pehlevan et al. [Neur. Comp. 27 (2015), 1461--1495] proposed a model of a self-organizing neural network with Hebbian and anti-Hebbian synaptic updates that implements an algorithm for principal subspace analysis; however, global stability of the nonlinear synaptic d...

---

### 39. Investigating cerebral anomalies in preterm infants and associated risk factors with magnetic resonance imaging at term-equivalent age

**Authors:** Nicolas Elbaz, Valérie Biran, Chloé Ghozland, et al.

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.14313v1) | 📄 [PDF](https://arxiv.org/pdf/2601.14313v1)

**Summary:** Background: Being born very or extreme preterm is a major source of cerebral anomalies and neurodevelopmental disorders, whose occurrence depends on many perinatal factors. A better understanding of these factors could be provided by cerebral Magnetic Resonance Imaging (MRI) at term-equivalent age (TEA). Objective: To investigate, through cerebral TEA-MRIs, the relationship between the main perinatal factors, the occurrence of cerebral anomalies, and cerebral volumetry. Methods: We assembled a c...

---

### 40. Cognition spaces: natural, artificial, and hybrid

**Authors:** Ricard Solé, Luis F Seoane, Jordi Pla-Mauri, et al.

**Published:** 2026-01-19

🔗 [Paper](http://arxiv.org/abs/2601.12837v1) | 📄 [PDF](https://arxiv.org/pdf/2601.12837v1)

**Summary:** Cognitive processes are realized across an extraordinary range of natural, artificial, and hybrid systems, yet there is no unified framework for comparing their forms, limits, and unrealized possibilities. Here, we propose a cognition space approach that replaces narrow, substrate-dependent definitions with a comparative representation based on organizational and informational dimensions. Within this framework, cognition is treated as a graded capacity to sense, process, and act upon information...

---

### 41. Primate-like perceptual decision making emerges through deep recurrent reinforcement learning

**Authors:** Nathan J. Wispinski, Scott A. Stone, Anthony Singhal, et al.

**Published:** 2026-01-18

🔗 [Paper](http://arxiv.org/abs/2601.12577v1) | 📄 [PDF](https://arxiv.org/pdf/2601.12577v1)

**Summary:** Progress has led to a detailed understanding of the neural mechanisms that underlie decision making in primates. However, less is known about why such mechanisms are present in the first place. Theory suggests that primate decision making mechanisms, and their resultant behavioral abilities, emerged to maximize reward in the face of noisy, temporally evolving information. To test this theory, we trained an end-to-end deep recurrent neural network using reinforcement learning on a noisy perceptua...

---

### 42. If Grid Cells are the Answer, What is the Question? A Review of Normative Grid Cell Theory

**Authors:** William Dorrell, James C. R. Whittington

**Published:** 2026-01-18

🔗 [Paper](http://arxiv.org/abs/2601.12424v1) | 📄 [PDF](https://arxiv.org/pdf/2601.12424v1)

**Summary:** For 20 years the beautiful structure in the grid cell code has presented an attractive puzzle: what computation do these representations subserve, and why does it manifest so curiously in neurons. The first question quickly attracted an answer: grid cells subserve path-integration, the ability to keep track of one's position as you move about the world. Subsequent work has only solidified this link: bottom-up mechanistic models that perform path-integration match the measured neural responses, w...

---

### 43. Modeling Dynamic Computations in the Primate Ventral Visual Stream

**Authors:** Matteo Dunnhofer, Maren Wehrheim, Hamidreza Ramezanpour, et al.

**Published:** 2026-01-18

🔗 [Paper](http://arxiv.org/abs/2601.12258v1) | 📄 [PDF](https://arxiv.org/pdf/2601.12258v1)

**Summary:** A major goal of computational neuroscience has been to explain how the primate ventral visual stream (VVS) transforms visual input into temporally evolving neural representations that support robust visual perception. Historically, most modeling efforts have assumed static conditions: monkeys fixate a dot, images are briefly flashed, and neural responses are analyzed through time-averaged metrics. Feedforward deep networks trained on static object recognition tasks outperform prior work in appro...

---

### 44. Automated Place Preference Paradigm for Optogenetic Stimulation of the Pedunculopontine Nucleus Reveals Motor Arrest-Linked Preference Behavior

**Authors:** Guanghui Li, Xingfei Hou, Zhenxiang Zhao

**Published:** 2026-01-17

🔗 [Paper](http://arxiv.org/abs/2601.12054v3) | 📄 [PDF](https://arxiv.org/pdf/2601.12054v3)

**Summary:** Understanding how the brain integrates motor suppression with motivational processes remains a fundamental question in neuroscience. The rostral Pedunculopontine nucleus, a brainstem structure involved in motor control, has been shown to induce transient motor arrest upon optogenetic or electrical stimulation. However, our current understanding of its potential role in linking motor suppression with motivational or reinforcement-related processes is still insufficient. To further explore the eff...

---

### 45. A New Strategy for Artificial Intelligence: Training Foundation Models Directly on Human Brain Data

**Authors:** Maël Donoso

**Published:** 2026-01-17

🔗 [Paper](http://arxiv.org/abs/2601.12053v1) | 📄 [PDF](https://arxiv.org/pdf/2601.12053v1)

**Summary:** While foundation models have achieved remarkable results across a diversity of domains, they still rely on human-generated data, such as text, as a fundamental source of knowledge. However, this data is ultimately the product of human brains, the filtered projection of a deeper neural complexity. In this paper, we explore a new strategy for artificial intelligence: moving beyond surface-level statistical regularities by training foundation models directly on human brain data. We hypothesize that...

---

### 46. Analysis of the Ventriloquism Aftereffect Using Network Theory Techniques

**Authors:** Sayan Saha

**Published:** 2026-01-16

🔗 [Paper](http://arxiv.org/abs/2601.15321v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15321v1)

**Summary:** Ventriloquism After-Effect is the phenomenon where sustained exposure to the ventriloquist illusion causes a change in unisensory auditory localization towards the location where the visual stimulus was present. We investigate the recalibration in EEG networks that causes this change and the track the timeline of changes in the auditory processing pathway. Our results obtained using network analysis, non-stationary time series analysis and multivariate pattern classification show that recalibrat...

---

### 47. On Brain as a Mathematical Manifold: Neural Manifolds, Sheaf Semantics, and Leibnizian Harmony

**Authors:** Takao Inoué

**Published:** 2026-01-16

🔗 [Paper](http://arxiv.org/abs/2601.15320v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15320v1)

**Summary:** We present a mathematical and philosophical framework in which brain function is modeled using sheaf theory over neural state spaces. Local neural or cognitive functions are represented as sections of a sheaf, while global coherence corresponds to the existence of global sections. Brain pathologies are interpreted as obstructions to such global integration and are classified using tools from sheaf cohomology. The framework builds on the neural manifold program in contemporary neuroscience and on...

---

### 48. Large Language Models as Simulative Agents for Neurodivergent Adult Psychometric Profiles

**Authors:** Francesco Chiappone, Davide Marocco, Nicola Milano

**Published:** 2026-01-16

🔗 [Paper](http://arxiv.org/abs/2601.15319v1) | 📄 [PDF](https://arxiv.org/pdf/2601.15319v1)

**Summary:** Adult neurodivergence, including Attention-Deficit/Hyperactivity Disorder (ADHD), high-functioning Autism Spectrum Disorder (ASD), and Cognitive Disengagement Syndrome (CDS), is marked by substantial symptom overlap that limits the discriminant sensitivity of standard psychometric instruments. While recent work suggests that Large Language Models (LLMs) can simulate human psychometric responses from qualitative data, it remains unclear whether they can accurately and stably model neurodevelopmen...

---

### 49. Simple Models, Rich Representations: Visual Decoding from Primate Intracortical Neural Signals

**Authors:** Matteo Ciferri, Matteo Ferrante, Nicola Toschi

**Published:** 2026-01-16

🔗 [Paper](http://arxiv.org/abs/2601.11108v1) | 📄 [PDF](https://arxiv.org/pdf/2601.11108v1)

**Summary:** Understanding how neural activity gives rise to perception is a central challenge in neuroscience. We address the problem of decoding visual information from high-density intracortical recordings in primates, using the THINGS Ventral Stream Spiking Dataset. We systematically evaluate the effects of model architecture, training objectives, and data scaling on decoding performance. Results show that decoding accuracy is mainly driven by modeling temporal dynamics in neural signals, rather than arc...

---

### 50. KOCOBrain: Kuramoto-Guided Graph Network for Uncovering Structure-Function Coupling in Adolescent Prenatal Drug Exposure

**Authors:** Badhan Mazumder, Lei Wu, Sir-Lord Wiafe, et al.

**Published:** 2026-01-16

🔗 [Paper](http://arxiv.org/abs/2601.11018v2) | 📄 [PDF](https://arxiv.org/pdf/2601.11018v2)

**Summary:** Exposure to psychoactive substances during pregnancy, such as cannabis, can disrupt neurodevelopment and alter large-scale brain networks, yet identifying their neural signatures remains challenging. We introduced KOCOBrain: KuramotO COupled Brain Graph Network; a unified graph neural network framework that integrates structural and functional connectomes via Kuramoto-based phase dynamics and cognition-aware attention. The Kuramoto layer models neural synchronization over anatomical connections,...

---

## stat.ML

**50 papers**

### 1. New explanations and inference for least angle regression

**Authors:** Karl B. Gregory, Daniel J. Nordman

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02491v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02491v1)

**Summary:** Efron et al. (2004) introduced least angle regression (LAR) as an algorithm for linear predictions, intended as an alternative to forward selection with connections to penalized regression. However, LAR has remained somewhat of a "black box," where some basic behavioral properties of LAR output are not well understood, including an appropriate termination point for the algorithm. We provide a novel framework for inference with LAR, which also allows LAR to be understood from new perspectives wit...

---

### 2. Maximizing Reliability with Bayesian Optimization

**Authors:** Jack M. Buckingham, Ivo Couckuyt, Juergen Branke

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02432v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02432v1)

**Summary:** Bayesian optimization (BO) is a popular, sample-efficient technique for expensive, black-box optimization. One such problem arising in manufacturing is that of maximizing the reliability, or equivalently minimizing the probability of a failure, of a design which is subject to random perturbations - a problem that can involve extremely rare failures ($P_\mathrm{fail} = 10^{-6}-10^{-8}$). In this work, we propose two BO methods based on Thompson sampling and knowledge gradient, the latter approxim...

---

### 3. Full-Batch Gradient Descent Outperforms One-Pass SGD: Sample Complexity Separation in Single-Index Learning

**Authors:** Filip Kovačević, Hong Chang Ji, Denny Wu, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02431v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02431v1)

**Summary:** It is folklore that reusing training data more than once can improve the statistical efficiency of gradient-based learning. However, beyond linear regression, the theoretical advantage of full-batch gradient descent (GD, which always reuses all the data) over one-pass stochastic gradient descent (online SGD, which uses each data point only once) remains unclear. In this work, we consider learning a $d$-dimensional single-index model with a quadratic activation, for which it is known that one-pas...

---

### 4. Provably Data-driven Multiple Hyper-parameter Tuning with Structured Loss Function

**Authors:** Tung Quoc Le, Anh Tuan Nguyen, Viet Anh Nguyen

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02406v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02406v1)

**Summary:** Data-driven algorithm design automates hyperparameter tuning, but its statistical foundations remain limited because model performance can depend on hyperparameters in implicit and highly non-smooth ways. Existing guarantees focus on the simple case of a one-dimensional (scalar) hyperparameter. This leaves the practically important, multi-dimensional hyperparameter tuning setting unresolved. We address this open question by establishing the first general framework for establishing generalization...

---

### 5. C-kNN-LSH: A Nearest-Neighbor Algorithm for Sequential Counterfactual Inference

**Authors:** Jing Wang, Jie Shen, Qiaomin Xie, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02371v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02371v1)

**Summary:** Estimating causal effects from longitudinal trajectories is central to understanding the progression of complex conditions and optimizing clinical decision-making, such as comorbidities and long COVID recovery. We introduce \emph{C-kNN--LSH}, a nearest-neighbor framework for sequential causal inference designed to handle such high-dimensional, confounded situations. By utilizing locality-sensitive hashing, we efficiently identify ``clinical twins'' with similar covariate histories, enabling loca...

---

### 6. Transfer Learning Through Conditional Quantile Matching

**Authors:** Yikun Zhang, Steven Wilkins-Reeves, Wesley Lee, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02358v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02358v1)

**Summary:** We introduce a transfer learning framework for regression that leverages heterogeneous source domains to improve predictive performance in a data-scarce target domain. Our approach learns a conditional generative model separately for each source domain and calibrates the generated responses to the target domain via conditional quantile matching. This distributional alignment step corrects general discrepancies between source and target domains without imposing restrictive assumptions such as cov...

---

### 7. Choice-Model-Assisted Q-learning for Delayed-Feedback Revenue Management

**Authors:** Owen Shen, Patrick Jaillet

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02283v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02283v1)

**Summary:** We study reinforcement learning for revenue management with delayed feedback, where a substantial fraction of value is determined by customer cancellations and modifications observed days after booking. We propose \emph{choice-model-assisted RL}: a calibrated discrete choice model is used as a fixed partial world model to impute the delayed component of the learning target at decision time. In the fixed-model deployment regime, we prove that tabular Q-learning with model-imputed targets converge...

---

### 8. Causal Inference for Preprocessed Outcomes with an Application to Functional Connectivity

**Authors:** Zihang Wang, Razieh Nabi, Benjamin B. Risk

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02240v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02240v1)

**Summary:** In biomedical research, repeated measurements within each subject are often processed to remove artifacts and unwanted sources of variation. The resulting data are used to construct derived outcomes that act as proxies for scientific outcomes that are not directly observable. Although intra-subject processing is widely used, its impact on inter-subject statistical inference has not been systematically studied, and a principled framework for causal analysis in this setting is lacking. In this art...

---

### 9. Spectral Superposition: A Theory of Feature Geometry

**Authors:** Georgi Ivanov, Narmeen Oozeer, Shivam Raval, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02224v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02224v1)

**Summary:** Neural networks represent more features than they have dimensions via superposition, forcing features to share representational space. Current methods decompose activations into sparse linear features but discard geometric structure. We develop a theory for studying the geometric structre of features by analyzing the spectra (eigenvalues, eigenspaces, etc.) of weight derived matrices. In particular, we introduce the frame operator $F = WW^\top$, which gives us a spectral measure that describes h...

---

### 10. PCA of probability measures: Sparse and Dense sampling regimes

**Authors:** Gachon Erell, Jérémie Bigot, Elsa Cazelles

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02190v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02190v1)

**Summary:** A common approach to perform PCA on probability measures is to embed them into a Hilbert space where standard functional PCA techniques apply. While convergence rates for estimating the embedding of a single measure from $m$ samples are well understood, the literature has not addressed the setting involving multiple measures. In this paper, we study PCA in a double asymptotic regime where $n$ probability measures are observed, each through $m$ samples. We derive convergence rates of the form $n^...

---

### 11. Learning Beyond the Gaussian Data: Learning Dynamics of Neural Networks on an Expressive and Cumulant-Controllable Data Model

**Authors:** Onat Ure, Samet Demir, Zafer Dogan

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02153v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02153v1)

**Summary:** We study the effect of high-order statistics of data on the learning dynamics of neural networks (NNs) by using a moment-controllable non-Gaussian data model. Considering the expressivity of two-layer neural networks, we first construct the data model as a generative two-layer NN where the activation function is expanded by using Hermite polynomials. This allows us to achieve interpretable control over high-order cumulants such as skewness and kurtosis through the Hermite coefficients while keep...

---

### 12. Training-free score-based diffusion for parameter-dependent stochastic dynamical systems

**Authors:** Minglei Yang, Sicheng He

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02113v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02113v1)

**Summary:** Simulating parameter-dependent stochastic differential equations (SDEs) presents significant computational challenges, as separate high-fidelity simulations are typically required for each parameter value of interest. Despite the success of machine learning methods in learning SDE dynamics, existing approaches either require expensive neural network training for score function estimation or lack the ability to handle continuous parameter dependence. We present a training-free conditional diffusi...

---

### 13. Efficient Swap Regret Minimization in Combinatorial Bandits

**Authors:** Andreas Kontogiannis, Vasilis Pollatos, Panayotis Mertikopoulos, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02087v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02087v1)

**Summary:** This paper addresses the problem of designing efficient no-swap regret algorithms for combinatorial bandits, where the number of actions $N$ is exponentially large in the dimensionality of the problem. In this setting, designing efficient no-swap regret translates to sublinear -- in horizon $T$ -- swap regret with polylogarithmic dependence on $N$. In contrast to the weaker notion of external regret minimization - a problem which is fairly well understood in the literature - achieving no-swap re...

---

### 14. Handling Covariate Mismatch in Federated Linear Prediction

**Authors:** Alexis Ayme, Rémi Khellaf

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02083v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02083v1)

**Summary:** Federated learning enables institutions to train predictive models collaboratively without sharing raw data, addressing privacy and regulatory constraints. In the standard horizontal setting, clients hold disjoint cohorts of individuals and collaborate to learn a shared predictor. Most existing methods, however, assume that all clients measure the same features. We study the more realistic setting of covariate mismatch, where each client observes a different subset of features, which typically a...

---

### 15. Ultrafast On-chip Online Learning via Spline Locality in Kolmogorov-Arnold Networks

**Authors:** Duc Hoang, Aarush Gupta, Philip Harris

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02056v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02056v1)

**Summary:** Ultrafast online learning is essential for high-frequency systems, such as controls for quantum computing and nuclear fusion, where adaptation must occur on sub-microsecond timescales. Meeting these requirements demands low-latency, fixed-precision computation under strict memory constraints, a regime in which conventional Multi-Layer Perceptrons (MLPs) are both inefficient and numerically unstable. We identify key properties of Kolmogorov-Arnold Networks (KANs) that align with these constraints...

---

### 16. SNAP: A Self-Consistent Agreement Principle with Application to Robust Computation

**Authors:** Xiaoyi Jiang, Andreas Nienkötter

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.02013v1) | 📄 [PDF](https://arxiv.org/pdf/2602.02013v1)

**Summary:** We introduce SNAP (Self-coNsistent Agreement Principle), a self-supervised framework for robust computation based on mutual agreement. Based on an Agreement-Reliability Hypothesis SNAP assigns weights that quantify agreement, emphasizing trustworthy items and downweighting outliers without supervision or prior knowledge. A key result is the Exponential Suppression of Outlier Weights, ensuring that outliers contribute negligibly to computations, even in high-dimensional settings. We study propert...

---

### 17. Stochastic Interpolants in Hilbert Spaces

**Authors:** James Boran Yu, RuiKang OuYang, Julien Horwood, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01988v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01988v1)

**Summary:** Although diffusion models have successfully extended to function-valued data, stochastic interpolants -- which offer a flexible way to bridge arbitrary distributions -- remain limited to finite-dimensional settings. This work bridges this gap by establishing a rigorous framework for stochastic interpolants in infinite-dimensional Hilbert spaces. We provide comprehensive theoretical foundations, including proofs of well-posedness and explicit error bounds. We demonstrate the effectiveness of the ...

---

### 18. Deep Multivariate Models with Parametric Conditionals

**Authors:** Dmitrij Schlesinger, Boris Flach, Alexander Shekhovtsov

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01953v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01953v1)

**Summary:** We consider deep multivariate models for heterogeneous collections of random variables. In the context of computer vision, such collections may e.g. consist of images, segmentations, image attributes, and latent variables. When developing such models, most existing works start from an application task and design the model components and their dependencies to meet the needs of the chosen task. This has the disadvantage of limiting the applicability of the resulting model for other downstream task...

---

### 19. Probabilistic function-on-function nonlinear autoregressive model for emulation and reliability analysis of dynamical systems

**Authors:** Zhouzhou Song, Marcos A. Valdebenito, Styfen Schär, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01929v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01929v1)

**Summary:** Constructing accurate and computationally efficient surrogate models (or emulators) for predicting dynamical system responses is critical in many engineering domains, yet remains challenging due to the strongly nonlinear and high-dimensional mapping from external excitations and system parameters to system responses. This work introduces a novel Function-on-Function Nonlinear AutoRegressive model with eXogenous inputs (F2NARX), which reformulates the conventional NARX model from a function-on-fu...

---

### 20. Privacy Amplification by Missing Data

**Authors:** Simon Roburin, Rafaël Pinot, Erwan Scornet

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01928v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01928v1)

**Summary:** Privacy preservation is a fundamental requirement in many high-stakes domains such as medicine and finance, where sensitive personal data must be analyzed without compromising individual confidentiality. At the same time, these applications often involve datasets with missing values due to non-response, data corruption, or deliberate anonymization. Missing data is traditionally viewed as a limitation because it reduces the information available to analysts and can degrade model performance. In t...

---

### 21. Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration

**Authors:** Du-Yi Wang, Guo Liang, Kun Zhang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01912v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01912v1)

**Summary:** Rapidly evolving market conditions call for real-time risk monitoring, but its online estimation remains challenging. In this paper, we study the online estimation of one of the most widely used risk measures, Value at Risk (VaR). Its accurate and reliable estimation is essential for timely risk control and informed decision-making. We propose to use the quantile regression forest in the offline-simulation-online-estimation (OSOA) framework. Specifically, the quantile regression forest is traine...

---

### 22. Data- and Variance-dependent Regret Bounds for Online Tabular MDPs

**Authors:** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01903v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01903v1)

**Summary:** This work studies online episodic tabular Markov decision processes (MDPs) with known transitions and develops best-of-both-worlds algorithms that achieve refined data-dependent regret bounds in the adversarial regime and variance-dependent regret bounds in the stochastic regime. We quantify MDP complexity using a first-order quantity and several new data-dependent measures for the adversarial regime, including a second-order quantity and a path-length measure, as well as variance-based measures...

---

### 23. Observation-dependent Bayesian active learning via input-warped Gaussian processes

**Authors:** Sanna Jarl, Maria Bånkestad, Jonathan J. S. Scragg, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01898v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01898v1)

**Summary:** Bayesian active learning relies on the precise quantification of predictive uncertainty to explore unknown function landscapes. While Gaussian process surrogates are the standard for such tasks, an underappreciated fact is that their posterior variance depends on the observed outputs only through the hyperparameters, rendering exploration largely insensitive to the actual measurements. We propose to inject observation-dependent feedback by warping the input space with a learned, monotone reparam...

---

### 24. Transformers as Measure-Theoretic Associative Memory: A Statistical Perspective and Minimax Optimality

**Authors:** Ryotaro Kawata, Taiji Suzuki

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01863v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01863v1)

**Summary:** Transformers excel through content-addressable retrieval and the ability to exploit contexts of, in principle, unbounded length. We recast associative memory at the level of probability measures, treating a context as a distribution over tokens and viewing attention as an integral operator on measures. Concretely, for mixture contexts $ν= I^{-1} \sum_{i=1}^I μ^{(i^*)}$ and a query $x_{\mathrm{q}}(i^*)$, the task decomposes into (i) recall of the relevant component $μ^{(i^*)}$ and (ii) prediction...

---

### 25. Designing Time Series Experiments in A/B Testing with Transformer Reinforcement Learning

**Authors:** Xiangkun Wu, Qianglin Wen, Yingying Zhang, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01853v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01853v1)

**Summary:** A/B testing has become a gold standard for modern technological companies to conduct policy evaluation. Yet, its application to time series experiments, where policies are sequentially assigned over time, remains challenging. Existing designs suffer from two limitations: (i) they do not fully leverage the entire history for treatment allocation; (ii) they rely on strong assumptions to approximate the objective function (e.g., the mean squared error of the estimated treatment effect) for optimizi...

---

### 26. Learning Sequential Decisions from Multiple Sources via Group-Robust Markov Decision Processes

**Authors:** Mingyuan Xu, Zongqi Xia, Tianxi Cai, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01825v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01825v1)

**Summary:** We often collect data from multiple sites (e.g., hospitals) that share common structure but also exhibit heterogeneity. This paper aims to learn robust sequential decision-making policies from such offline, multi-site datasets. To model cross-site uncertainty, we study distributionally robust MDPs with a group-linear structure: all sites share a common feature map, and both the transition kernels and expected reward functions are linear in these shared features. We introduce feature-wise (d-rect...

---

### 27. Stein-Rule Shrinkage for Stochastic Gradient Estimation in High Dimensions

**Authors:** M. Arashi, M. Amintoosi

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01777v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01777v1)

**Summary:** Stochastic gradient methods are central to large-scale learning, yet their analysis typically treats mini-batch gradients as unbiased estimators of the population gradient. In high-dimensional settings, however, classical results from statistical decision theory show that unbiased estimators are generally inadmissible under quadratic loss, suggesting that standard stochastic gradients may be suboptimal from a risk perspective. In this work, we formulate stochastic gradient computation as a high-...

---

### 28. ST-BCP: Tightening Coverage Bound for Backward Conformal Prediction via Non-Conformity Score Transformation

**Authors:** Junxian Liu, Hao Zeng, Hongxin Wei

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01733v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01733v1)

**Summary:** Conformal Prediction (CP) provides a statistical framework for uncertainty quantification that constructs prediction sets with coverage guarantees. While CP yields uncontrolled prediction set sizes, Backward Conformal Prediction (BCP) inverts this paradigm by enforcing a predefined upper bound on set size and estimating the resulting coverage guarantee. However, the looseness induced by Markov's inequality within the BCP framework causes a significant gap between the estimated coverage bound and...

---

### 29. Finite and Corruption-Robust Regret Bounds in Online Inverse Linear Optimization under M-Convex Action Sets

**Authors:** Taihei Oki, Shinsaku Sakaue

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01682v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01682v1)

**Summary:** We study online inverse linear optimization, also known as contextual recommendation, where a learner sequentially infers an agent's hidden objective vector from observed optimal actions over feasible sets that change over time. The learner aims to recommend actions that perform well under the agent's true objective, and the performance is measured by the regret, defined as the cumulative gap between the agent's optimal values and those achieved by the learner's recommended actions. Prior work h...

---

### 30. The Effect of Mini-Batch Noise on the Implicit Bias of Adam

**Authors:** Matias D. Cattaneo, Boris Shigida

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01642v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01642v1)

**Summary:** With limited high-quality data and growing compute, multi-epoch training is gaining back its importance across sub-areas of deep learning. Adam(W), versions of which are go-to optimizers for many tasks such as next token prediction, has two momentum hyperparameters $(β_1, β_2)$ controlling memory and one very important hyperparameter, batch size, controlling (in particular) the amount mini-batch noise. We introduce a theoretical framework to understand how mini-batch noise influences the implici...

---

### 31. Minimax optimal differentially private synthetic data for smooth queries

**Authors:** Rundong Ding, Yiyun He, Yizhe Zhu

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01607v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01607v1)

**Summary:** Differentially private synthetic data enables the sharing and analysis of sensitive datasets while providing rigorous privacy guarantees for individual contributors. A central challenge is to achieve strong utility guarantees for meaningful downstream analysis. Many existing methods ensure uniform accuracy over broad query classes, such as all Lipschitz functions, but this level of generality often leads to suboptimal rates for statistics of practical interest. Since many common data analysis qu...

---

### 32. Universal Redundancies in Time Series Foundation Models

**Authors:** Anthony Bao, Venkata Hasith Vattikuti, Jeffrey Lai, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01605v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01605v1)

**Summary:** Time Series Foundation Models (TSFMs) leverage extensive pretraining to accurately predict unseen time series during inference, without the need for task-specific fine-tuning. Through large-scale evaluations on standard benchmarks, we find that leading transformer-based TSFMs exhibit redundant components in their intermediate layers. We introduce a set of tools for mechanistic interpretability of TSFMs, including ablations of specific components and direct logit attribution on the residual strea...

---

### 33. Inference-Aware Meta-Alignment of LLMs via Non-Linear GRPO

**Authors:** Shokichi Takakura, Akifumi Wachi, Rei Higuchi, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01603v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01603v1)

**Summary:** Aligning large language models (LLMs) to diverse human preferences is fundamentally challenging since criteria can often conflict with each other. Inference-time alignment methods have recently gained popularity as they allow LLMs to be aligned to multiple criteria via different alignment algorithms at inference time. However, inference-time alignment is computationally expensive since it often requires multiple forward passes of the base model. In this work, we propose inference-aware meta-alig...

---

### 34. When Is Generalized Bayes Bayesian? A Decision-Theoretic Characterization of Loss-Based Updating

**Authors:** Kenichiro McAlinn, Kōsaku Takanashi

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01573v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01573v1)

**Summary:** Loss-based updating, including generalized Bayes, Gibbs, and quasi-posteriors, replaces likelihoods by a user-chosen loss and produces a posterior-like distribution via exponential tilt. We give a decision-theoretic characterization that separates \emph{belief posteriors} --  conditional beliefs justified by the foundations of Savage and Anscombe-Aumann under a joint probability mode l-- from \emph{decision posteriors} -- randomized decision rules justified by preferences over decision rules. We...

---

### 35. Optimal Sample Complexity for Single Time-Scale Actor-Critic with Momentum

**Authors:** Navdeep Kumar, Tehila Dahan, Lior Cohen, et al.

**Published:** 2026-02-02

🔗 [Paper](http://arxiv.org/abs/2602.01505v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01505v1)

**Summary:** We establish an optimal sample complexity of $O(ε^{-2})$ for obtaining an $ε$-optimal global policy using a single-timescale actor-critic (AC) algorithm in infinite-horizon discounted Markov decision processes (MDPs) with finite state-action spaces, improving upon the prior state of the art of $O(ε^{-3})$. Our approach applies STORM (STOchastic Recursive Momentum) to reduce variance in the critic updates. However, because samples are drawn from a nonstationary occupancy measure induced by the ev...

---

### 36. Predicting and improving test-time scaling laws via reward tail-guided search

**Authors:** Muheng Li, Jian Qian, Wenlong Mou

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01485v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01485v1)

**Summary:** Test-time scaling has emerged as a critical avenue for enhancing the reasoning capabilities of Large Language Models (LLMs). Though the straight-forward ''best-of-$N$'' (BoN) strategy has already demonstrated significant improvements in performance, it lacks principled guidance on the choice of $N$, budget allocation, and multi-stage decision-making, thereby leaving substantial room for optimization. While many works have explored such optimization, rigorous theoretical guarantees remain limited...

---

### 37. Rod Flow: A Continuous-Time Model for Gradient Descent at the Edge of Stability

**Authors:** Eric Regis, Sinho Chewi

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01480v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01480v1)

**Summary:** How can we understand gradient-based training over non-convex landscapes? The edge of stability phenomenon, introduced in Cohen et al. (2021), indicates that the answer is not so simple: namely, gradient descent (GD) with large step sizes often diverges away from the gradient flow. In this regime, the "Central Flow", recently proposed in Cohen et al. (2025), provides an accurate ODE approximation to the GD dynamics over many architectures. In this work, we propose Rod Flow, an alternative ODE ap...

---

### 38. Density-Informed Pseudo-Counts for Calibrated Evidential Deep Learning

**Authors:** Pietro Carlotti, Nevena Gligić, Arya Farahi

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01477v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01477v1)

**Summary:** Evidential Deep Learning (EDL) is a popular framework for uncertainty-aware classification that models predictive uncertainty via Dirichlet distributions parameterized by neural networks. Despite its popularity, its theoretical foundations and behavior under distributional shift remain poorly understood. In this work, we provide a principled statistical interpretation by proving that EDL training corresponds to amortized variational inference in a hierarchical Bayesian model with a tempered pseu...

---

### 39. A Statistical Theory of Gated Attention through the Lens of Hierarchical Mixture of Experts

**Authors:** Viet Nguyen, Tuan Minh Pham, Thinh Cao, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01468v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01468v1)

**Summary:** Self-attention has greatly contributed to the success of the widely used Transformer architecture by enabling learning from data with long-range dependencies. In an effort to improve performance, a gated attention model that leverages a gating mechanism within the multi-head self-attention has recently been proposed as a promising alternative. Gated attention has been empirically demonstrated to increase the expressiveness of low-rank mapping in standard attention and even to eliminate the atten...

---

### 40. Rethinking Multinomial Logistic Mixture of Experts with Sigmoid Gating Function

**Authors:** Tuan Minh Pham, Thinh Cao, Viet Nguyen, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01466v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01466v1)

**Summary:** The sigmoid gate in mixture-of-experts (MoE) models has been empirically shown to outperform the softmax gate across several tasks, ranging from approximating feed-forward networks to language modeling. Additionally, recent efforts have demonstrated that the sigmoid gate is provably more sample-efficient than its softmax counterpart under regression settings. Nevertheless, there are three notable concerns that have not been addressed in the literature, namely (i) the benefits of the sigmoid gate...

---

### 41. Dimension-Free Multimodal Sampling via Preconditioned Annealed Langevin Dynamics

**Authors:** Lorenzo Baldassari, Josselin Garnier, Knut Solna, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01449v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01449v1)

**Summary:** Designing algorithms that can explore multimodal target distributions accurately across successive refinements of an underlying high-dimensional problem is a central challenge in sampling. Annealed Langevin dynamics (ALD) is a widely used alternative to classical Langevin since it often yields much faster mixing on multimodal targets, but there is still a gap between this empirical success and existing theory: when, and under which design choices, can ALD be guaranteed to remain stable as dimens...

---

### 42. Theoretical Analysis of Measure Consistency Regularization for Partially Observed Data

**Authors:** Yinsong Wang, Shahin Shahrampour

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01437v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01437v1)

**Summary:** The problem of corrupted data, missing features, or missing modalities continues to plague the modern machine learning landscape. To address this issue, a class of regularization methods that enforce consistency between imputed and fully observed data has emerged as a promising approach for improving model generalization, particularly in partially observed settings. We refer to this class of methods as Measure Consistency Regularization (MCR). Despite its empirical success in various application...

---

### 43. DCD: Decomposition-based Causal Discovery from Autocorrelated and Non-Stationary Temporal Data

**Authors:** Muhammad Hasan Ferdous, Md Osman Gani

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01433v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01433v1)

**Summary:** Multivariate time series in domains such as finance, climate science, and healthcare often exhibit long-term trends, seasonal patterns, and short-term fluctuations, complicating causal inference under non-stationarity and autocorrelation. Existing causal discovery methods typically operate on raw observations, making them vulnerable to spurious edges and misattributed temporal dependencies. We introduce a decomposition-based causal discovery framework that separates each time series into trend, ...

---

### 44. Robust Generalization with Adaptive Optimal Transport Priors for Decision-Focused Learning

**Authors:** Haixiang Sun, Andrew L. Liu

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01427v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01427v1)

**Summary:** Few-shot learning requires models to generalize under limited supervision while remaining robust to distribution shifts. Existing Sinkhorn Distributionally Robust Optimization (DRO) methods provide theoretical guarantees but rely on a fixed reference distribution, which limits their adaptability. We propose a Prototype-Guided Distributionally Robust Optimization (PG-DRO) framework that learns class-adaptive priors from abundant base data via hierarchical optimal transport and embeds them into th...

---

### 45. Importance Weighted Variational Inference without the Reparameterization Trick

**Authors:** Kamélia Daudel, Minh-Ngoc Tran, Cheng Zhang

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01412v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01412v1)

**Summary:** Importance weighted variational inference (VI) approximates densities known up to a normalizing constant by optimizing bounds that tighten with the number of Monte Carlo samples $N$. Standard optimization relies on reparameterized gradient estimators, which are well-studied theoretically yet restrict both the choice of the data-generating process and the variational approximation. While REINFORCE gradient estimators do not suffer from such restrictions, they lack rigorous theoretical justificati...

---

### 46. Online Social Welfare Function-based Resource Allocation

**Authors:** Kanad Pardeshi, Samsara Foubert, Aarti Singh

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01400v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01400v1)

**Summary:** In many real-world settings, a centralized decision-maker must repeatedly allocate finite resources to a population over multiple time steps. Individuals who receive a resource derive some stochastic utility; to characterize the population-level effects of an allocation, the expected individual utilities are then aggregated using a social welfare function (SWF). We formalize this setting and present a general confidence sequence framework for SWF-based online learning and inference, valid for an...

---

### 47. An Odd Estimator for Shapley Values

**Authors:** Fabian Fumagalli, Landon Butler, Justin Singh Kang, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01399v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01399v1)

**Summary:** The Shapley value is a ubiquitous framework for attribution in machine learning, encompassing feature importance, data valuation, and causal inference. However, its exact computation is generally intractable, necessitating efficient approximation methods. While the most effective and popular estimators leverage the paired sampling heuristic to reduce estimation error, the theoretical mechanism driving this improvement has remained opaque. In this work, we provide an elegant and fundamental justi...

---

### 48. On the Power of (Approximate) Reward Models for Inference-Time Scaling

**Authors:** Youheng Zhu, Yiping Lu

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01381v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01381v1)

**Summary:** Inference-time scaling has recently emerged as a powerful paradigm for improving the reasoning capability of large language models. Among various approaches, Sequential Monte Carlo (SMC) has become a particularly important framework, enabling iterative generation, evaluation, rejection, and resampling of intermediate reasoning trajectories. A central component in this process is the reward model, which evaluates partial solutions and guides the allocation of computation during inference.   Howev...

---

### 49. Context Dependence and Reliability in Autoregressive Language Models

**Authors:** Poushali Sengupta, Shashi Raj Pandey, Sabita Maharjan, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01378v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01378v1)

**Summary:** Large language models (LLMs) generate outputs by utilizing extensive context, which often includes redundant information from prompts, retrieved passages, and interaction history. In critical applications, it is vital to identify which context elements actually influence the output, as standard explanation methods struggle with redundancy and overlapping context. Minor changes in input can lead to unpredictable shifts in attribution scores, undermining interpretability and raising concerns about...

---

### 50. High-accuracy sampling for diffusion models and log-concave distributions

**Authors:** Fan Chen, Sinho Chewi, Constantinos Daskalakis, et al.

**Published:** 2026-02-01

🔗 [Paper](http://arxiv.org/abs/2602.01338v1) | 📄 [PDF](https://arxiv.org/pdf/2602.01338v1)

**Summary:** We present algorithms for diffusion model sampling which obtain $δ$-error in $\mathrm{polylog}(1/δ)$ steps, given access to $\widetilde O(δ)$-accurate score estimates in $L^2$. This is an exponential improvement over all previous results. Specifically, under minimal data assumptions, the complexity is $\widetilde O(d\,\mathrm{polylog}(1/δ))$ where $d$ is the dimension of the data; under a non-uniform $L$-Lipschitz condition, the complexity is $\widetilde O(\sqrt{dL}\,\mathrm{polylog}(1/δ))$; and...

---

