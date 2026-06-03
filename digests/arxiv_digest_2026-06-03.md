# arXiv Daily Digest - 2026-06-03

Total papers: 50

---

## cs.CV

**50 papers**

### 1. Exploring Easy Boosts for Lidar Semantic Scene Completion

**Authors:** Tetiana Martyniuk, Jonathan Seele, Alexandre Boulch, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03992v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03992v1)

**Summary:** This paper investigates "free lunch" strategies to boost the performance of lidar semantic scene completion (SSC) without requiring complex architectural redesigns. We first demonstrate that endowing input point clouds with semantic pseudo-labels from off-the-shelf segmentors significantly improves the performance of existing architectures. By evaluating these models against an oracle, we establish that high-quality semantic priors are a primary driver of mIoU gains. Furthermore, we equip the in...

---

### 2. SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image

**Authors:** Inhee Lee, Sangwon Baik, Sungjoo Kim, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03994v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03994v1)

**Summary:** Reconstructing interactive, simulation-ready 3D scenes from a single image is a critical bottleneck for robotic manipulation. While recent single-image lifters recover plausible per-object shapes, composing them yields scenes that collapse under physical simulation due to interpenetrating, hovering, or sinking objects. Existing physics-aware methods address this strictly as a post-hoc layout correction, leaving the underlying geometric errors unresolved. To address this, we introduce SimuScene, ...

---

### 3. Neuron Populations Exhibit Divergent Selectivity with Scale

**Authors:** Amil Dravid, Yasaman Bahri, Alexei A. Efros, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03990v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03990v1)

**Summary:** We investigate whether neuron populations within neural networks evolve predictably with scale, extending scaling laws beyond macroscopic observables such as loss. To probe this question, we study Rosetta Neurons, a previously characterized class of neurons whose activation patterns are similar across independently trained models (Dravid et al., 2023). In separate analyses of language models up to 30B parameters and vision models up to 5B parameters, we observe that the population of Rosetta Neu...

---

### 4. PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation

**Authors:** Shinjeong Kim, Ignacio Alzugaray, Callum Rhodes, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03989v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03989v1)

**Summary:** Images composed of 2D pixel arrays are the standard input to computer vision algorithms, yet many underlying computations can be distributed across pixels. Transmitting raw, redundant, and noisy pixel data off the sensor remains inefficient, motivating a shift toward focal-plane sensor-processors that perform a significant part of the computation directly within each pixel. We envision pixels synthesizing higher-level signals locally, reducing downstream load, and providing richer inputs for hig...

---

### 5. NewtPhys: Do Foundation Models Understand Newtonian Physics?

**Authors:** Sebastian Cavada, Soumava Paul, Tuan-Hung Vu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03986v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03986v1)

**Summary:** Previous work has evaluated physics reasoning in foundation models using synthetic or semi-synthetic scenes and visual question-answering tasks. However, these benchmarks emphasize high-level events and lack the visual fidelity required to assess true low-level Newtonian understanding. We introduce NewtPhys, a 4D physically annotated dataset built from multiview images of real-world scenes with physics-grounded simulations. The dataset provides dense, fine-grained annotations across timesteps --...

---

### 6. Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking

**Authors:** Zekun Qi, Xuchuan Chen, Dairu Liu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03985v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03985v1)

**Summary:** We introduce Humanoid-GPT, a GPT-style Transformer with causal attention trained on a billion-scale motion corpus for whole-body control. Unlike prior shallow MLP trackers constrained by scarce data and an agility-generalization trade-off, Humanoid-GPT is pre-trained on a 2B-frame retargeted corpus that unifies all major mocap datasets with large-scale in-house recordings. Scaling both data and model capacity yields a single generative Transformer that tracks highly dynamic behaviors while achie...

---

### 7. Formalizing the Binding Problem

**Authors:** Lianghuan Huang, Yihao Li, Saeed Salehi, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03976v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03976v1)

**Summary:** Representations of the world, arguably, contain information about features (e.g. something is blue, something is a circle) but also information about which features are part of the same object (e.g. the circle is blue), which we call binding information. Any system with the ability to understand scenes with multiple objects must be able to solve the binding problem: it needs to know which features belong together. However, despite work showing that Vision Transformers (ViTs) know which patches b...

---

### 8. AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation

**Authors:** Haobo Li, Yanhong Zeng, Yunhong Lu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03972v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03972v1)

**Summary:** We present AAD-1, an Asymmetric Adversarial Distillation framework for One-step autoregressive image-to-video generation. State-of-the-art methods adopt adversarial distillation but suffer from motion collapse and training instability, resulting in static videos. AAD-1 addresses these challenges through two key designs in architecture and training strategy. Our key architectural insight is to break the symmetry between generator and discriminator. While the generator remains causal to preserve a...

---

### 9. Video-Mirai: Autoregressive Video Diffusion Models Need Foresight

**Authors:** Yonghao Yu, Lang Huang, Runyi Li, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03971v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03971v1)

**Summary:** Causal video generators must predict from the past, but they need not learn only from it. In streaming autoregressive video diffusion, each emitted segment becomes a commitment that future segments must preserve. Standard training, however, only asks each causal state to explain the present. This creates what we call a representation-level planning gap: states that fit the current segment may discard identity, layout, and motion information needed for a consistent future. We introduce Video-Mira...

---

### 10. VLESA: Vision-Language Embodied Safety Agent for Human Activity Monitoring

**Authors:** Hanjiang Hu, Yiyuan Pan, Jiaxing Li, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03954v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03954v1)

**Summary:** As AI systems increasingly assist humans in physical tasks, ensuring safety becomes paramount -- physical actions carry immediate and irreversible consequences that digital errors do not. We introduce the Vision-Language Embodied Safety Agent (VLESA), a framework that monitors human activities from egocentric video and triggers real-time safety interventions when dangerous actions are predicted. VLESA addresses intent-dependent safety where identical actions can be safe or dangerous depending on...

---

### 11. Demo2Tutorial: From Human Experience to Multimodal Software Tutorials

**Authors:** Zechen Bai, Zhiheng Chen, Yiqi Lin, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03951v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03951v1)

**Summary:** Human experience in digital environments offers a vast, underexplored resource of authentic, untrimmed interactions that contain rich procedural knowledge. We introduce Demo2Tutorial, a framework that transforms this experience captured via screen recordings and interaction logs into structured, multimodal software tutorials for teaching both humans and agents. Demo2Tutorial first collects human experience via a dedicated recorder, then parses raw experience using a multimodal Action Parser to r...

---

### 12. SEAOTTER: Sensor Embedded Autoencoding with One-Time Transcode for Efficient Reconstruction

**Authors:** Dan Jacobellis, Neeraja J. Yadwadkar

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03940v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03940v1)

**Summary:** In robotics systems, vast amounts of visual data are easily captured at high resolution using low-cost, low-power hardware. Yet, limited bandwidth and on-device compute resources prevent full utilization when transmitted via conventional codecs like JPEG/MPEG. Newer codecs, like AV1/AVIF, improve the rate-distortion trade-off, but demand far more resources for encoding, impractical without custom ASICs. Recent asymmetric autoencoders deliver high quality under extreme power and bandwidth constra...

---

### 13. Adaptive Causal Alignment for High-Confidence Adversarial Training

**Authors:** Zhiming Luo, Kejia Zhang, Yingxin Lai, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03925v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03925v1)

**Summary:** Inverse adversarial training leverages high-confidence predictions to stabilize robust learning, yet we uncover a critical paradox: high confidence often stems from overfitting to non-causal background correlations rather than intrinsic object semantics. Our investigation reveals that visual context functions as a dual-natured signal, serving as either a necessary supportive prior or a spurious confounder. This insight renders existing blind suppression strategies flawed, as they inevitably lead...

---

### 14. GARDEN: Gravity-Aligned Reconstruction of Disentangled ENvironments from RGB images

**Authors:** Jiahao Sun, Dingkun Wei, Zehong Shen, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03921v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03921v1)

**Summary:** Converting multi-view RGB observations into simulation-ready 3D environments remains challenging because current reconstruction pipelines produce monolithic scene representations without explicit physical structure. They are typically defined up to an arbitrary global rotation and entangle rigid foreground objects with background geometry, which hinders stable physical interaction. Existing solutions often recover interactivity by replacing reconstructed objects with retrieved CAD assets, but th...

---

### 15. Benchmarking Visual State Tracking in Multimodal Video Understanding

**Authors:** Sihyun Yu, Nanye Ma, Pinzhi Huang, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03920v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03920v1)

**Summary:** Understanding a video requires more than recognizing isolated moments, as humans continuously track entities, states, and events over time. This capacity for visual state tracking is fundamental to video understanding, yet remains underexplored in current evaluations of Multimodal Large Language Models (MLLMs). We introduce Visual STAte Tracking benchmark (VSTAT), a video-based benchmark designed to diagnose visual state tracking in MLLMs. VSTAT consists of 834 clips drawn from both synthetic an...

---

### 16. PatchScene: Patch-based Voxel Diffusion for Large-Scale Scene Completion

**Authors:** Qingdong Xu, Jiajun Zhu, Shilin Zhu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03915v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03915v1)

**Summary:** We propose PatchScene, a novel diffusion-based framework for large-scale LiDAR scene completion. Unlike existing methods that rely on global latent representations or dense voxel grids, PatchScene adopts a patch-based voxel diffusion paradigm that explicitly generates fine-grained geometry within localized 3D regions. To ensure coherent reconstruction at both spatial and temporal scales, we introduce a confidence-guided spatio-temporal fusion mechanism that integrates overlapping patches and adj...

---

### 17. Bootstrap Your Generator: Unpaired Visual Editing with Flow Matching

**Authors:** Yoad Tewel, Yuval Atzmon, Gal Chechik, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03911v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03911v1)

**Summary:** Modern generative models possess a deep understanding of visual content, yet training them for image editing typically requires massive datasets of paired examples. This limits scalability, especially for video editing where collecting paired data is prohibitively expensive. We propose Bootstrap Your Generator (ByG), a general framework for unpaired training of flow matching editing models. It leverages the base model's knowledge without any external signal. Our approach pairs instruction-follow...

---

### 18. SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation

**Authors:** Qingpo Wuwu, Xiaobao Wei, Peng Chen, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03909v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03909v1)

**Summary:** While 3D Gaussian Splatting has shown promising results in street scene reconstruction, existing methods require massive numbers of Gaussian primitives to capture fine details, leading to prohibitive storage costs and slow rendering speeds. We observe that dynamic objects (e.g., vehicles and pedestrians) demand high-fidelity representations to maintain temporal consistency, while static background regions often contain substantial redundancy. Motivated by this, we propose SparseStreet, a general...

---

### 19. MAdam: Metric-Aware Multi-Objective Adam

**Authors:** Fengbei Liu, Rachit Saluja, Sunwoo Kwak, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03904v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03904v1)

**Summary:** Multi-objective optimization (MOO) underlies many machine learning problems, yet MOO solvers across the loss-balancing, gradient-balancing, and Pareto-based families almost universally hand their reconciled directions to Adam~\cite{kingma2015adam}. We show this coupling introduces two systematic gaps between the solver's intent and the optimizer's execution. The first is a \emph{weighting mismatch}: Adam's second-moment denominator entangles the time-varying preference vector with gradient stati...

---

### 20. An Attention-Based Denoising Model for Diffusion Weighted Imaging

**Authors:** Prithviraj Verma, Pawan Kumar, Chandan Deshani, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03903v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03903v1)

**Summary:** Diffusion-weighted imaging (DWI) is used for whole-body cancer screening, but it typically requires a long acquisition time. When the scan time is reduced, the image quality often suffers, leading to increased noise in the scans. Magnitude reconstruction in DWI introduces signal-dependent Rician noise, which makes denoising more challenging for conventional convolution-based methods. To address this limitation, we propose a noise-aware attention-driven denoising framework that integrates hierarc...

---

### 21. Electromagnetic Navigation for Femoral Osteotomy Using High-Accuracy X-ray-to-CT Registration

**Authors:** Roman Flepp, Arend Nieuwland, Bastian Sigrist, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03893v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03893v1)

**Summary:** Accurate execution of preoperative plans in corrective femoral osteotomies remains challenging. Current techniques are limited by variable accuracy, invasiveness, and radiation exposure, with free-hand methods and patient-specific instrumentation (PSI) often requiring >30 and >6 fluoroscopic images, respectively. We present an integrated, electromagnetic tracking (EMT)-based navigation system for femoral osteotomies that minimizes dissection and intraoperative fluoroscopy. The system couples CT-...

---

### 22. OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs

**Authors:** Yifei Li, Pengyiang Liu, Yuhang Zang, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03890v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03890v1)

**Summary:** Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. Existing benchmarks either evaluate offline over full videos or target events rather than spatial structure. We introduce OVO-S-Bench, a fully human-annotated benchmark for streaming spatial intelligence, comprising 1,680 questions over 348 source videos. Annotation involves 12 trained annotators, each also serving as a ...

---

### 23. CoralBay: A Self-Supervised CT Foundation Model

**Authors:** Ioannis Gatopoulos, Nicolas Känzig, Sebastian Otálora, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03888v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03888v1)

**Summary:** Self-supervised learning has enabled large-scale pre-training on 2D natural images, producing general-purpose visual representations that transfer effectively across tasks. However, many medical imaging modalities, such as CT scans, are inherently three-dimensional and differ fundamentally from natural images in both structure and semantics. Volumetric modalities capture spatial continuity, organ anatomy, and intensity-based tissue properties (e.g., Hounsfield Units), which are not adequately mo...

---

### 24. Beyond Encoder Accumulation: Measuring Encoder Roles in Multi-Encoder VLMs

**Authors:** Wei Ding, Yudong Zhang, Ruobing Xie, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03879v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03879v1)

**Summary:** As foundation models scale toward fusing more heterogeneous visual streams, understanding how diverse encoders interact under joint training becomes a prerequisite for principled design. Yet large vision-language models (LVLMs) currently lack the tools to do so, and parameter-efficient encoder configurations remain hard to identify before training. To re-examine encoder roles under joint training, on the 16-benchmark Cambrian-1 suite we retrain and evaluate all 31 non-empty subsets of five commo...

---

### 25. MLP Splatting: Object-Centric Neural Fields

**Authors:** Shinjeong Kim, Yuzhou Cheng, Xin Kong, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03877v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03877v1)

**Summary:** 3D representations are fundamental to scene rendering, understanding, and interaction. Recent approaches, such as 3D Gaussian Splatting and Neural Radiance Fields, achieve impressive photorealistic novel-view synthesis, but lack the ability to easily decompose scene elements into a few primitives, requiring additional segmentation or grouping for object-level manipulation. We present MLP-Splatting, a method that enables scene decomposition via a few expressive light-field primitives while provid...

---

### 26. Seg2Track++: Probabilistic Track Validation and Data Association for Multi-Object Tracking and Segmentation

**Authors:** Diogo Mendonça, Tiago Barros, Cristiano Premebida, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03875v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03875v1)

**Summary:** Autonomous systems require robust Multi-Object Tracking and Segmentation (MOTS) to operate reliably in dynamic environments, ensuring consistent object identities and precise mask-level delineation. Foundation models such as SAM2 have shown strong zero-shot generalization for segmentation, but their direct application to MOTS is limited by unreliable track association and false-positive propagation. This work introduces Seg2Track++, a framework that integrates instance segmentation with SAM2 and...

---

### 27. DyaPlex: Full-Duplex Speech-Motion Model for Dyadic Interaction

**Authors:** Koki Nagano, Hongyu Liu, Seonwook Park, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03874v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03874v1)

**Summary:** We present DyaPlex, a streaming, full-duplex speech-and-motion model designed for dyadic interaction. To capture the continuous and reciprocal nature of human communication, this full-duplex capability empowers the agent to simultaneously perceive and generate both speech and physical motion in a streaming fashion. At its core, our method leverages the strong priors of a foundational full-duplex speech model and integrates a novel motion pathway, thereby achieving fully synchronized multi-modal ...

---

### 28. Visual Instruction Tuning Aligns Modalities through Abstraction

**Authors:** Luis Palacios, Lorenzo Basile, Diego Doimo, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03871v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03871v1)

**Summary:** Visual instruction tuning effectively adapts a pre-trained Large Language Model (LLM) to process image information alongside text. Yet, it remains unclear how visual features are embedded into the layer-wise hierarchy of abstractions of the LLM backbone. Across a diverse set of vision-language architectures, we show that instruction tuning primarily serves as a bridge, embedding visual features directly into the intermediate semantic layers of the LLM, bypassing the early layers devoted to unimo...

---

### 29. Unified Video-Action Joint Denoising for Dexterous Action and Data Generation

**Authors:** Dingrui Wang, YuAn Wang, Jinkun Liu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03868v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03868v1)

**Summary:** Recent world action models leverage video foundation models by aligning broad visual-dynamics priors with executable robot actions. We revisit this alignment from a distributional perspective. Existing formulations typically narrow the aligned prior into an observation-conditioned policy distribution over future actions. In contrast, we keep the distribution broader by modeling the joint space of interaction videos and executable hand trajectories under multiple conditioning regimes. We propose ...

---

### 30. Where Do We (Not) Need Temporal Context in Low-Resource Video Task Adaptation?

**Authors:** Luc P. J. Sträter, Hazel Doughty

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03837v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03837v1)

**Summary:** Parameter-efficient fine-tuning (PEFT) and probing enable adaptation of foundation models using only a small number of trainable parameters, making it attractive for video understanding where annotation and computation are expensive. However, video PEFT has focused on adapting image-pretrained models, while standard PEFT methods can also be applied to video representations. These settings are rarely compared and both confine temporal reasoning to a single component of the model, leaving open how...

---

### 31. Conditional Latent Diffusion Model with Fourier-based Motion Modelling for Virtual Population Synthesis

**Authors:** Shaokun Lan, Haoran Dou, Jinghan Huang, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03827v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03827v1)

**Summary:** In-silico trials of medical devices require the generation of virtual populations of anatomies. In cardiovascular applications, virtual anatomy is typically represented as a 3D+t mesh sampled from a generative model. However, most existing mesh generators focus on static anatomy, while sequence models often lack explicit periodicity. To this end, we propose 4D F-MeshLDM, a conditional generative framework comprising a convolutional mesh VAE to encode meshes, a structural latent space that parame...

---

### 32. TeX-1500: A Paired Real-World LWIR Hyperspectral Dataset and Benchmark for Temperature-Emissivity-Texture Decomposition

**Authors:** Cheng Dai, Jiale Lin, Hongyi Xu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03806v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03806v1)

**Summary:** Temperature-emissivity-texture (TeX) decomposition seeks to recover object heat state, material spectral response, and visible-like geometric texture from long-wave infrared hyperspectral imaging (LWIR HSI). Existing TeX pipelines are mainly scene-specific inverse solvers, and the lack of paired LWIR HSI-TeX supervision has limited learning-based decomposition. To address this gap, we introduce TeX-1500, a large-scale paired LWIR HSI-TeX dataset and benchmark for supervised HSI-to-TeX decomposit...

---

### 33. Template Collapse and Information-Theoretic Limits in Camera rPPG Pulse Morphology Restoration

**Authors:** Achraf Ben Ahmed

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03802v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03802v1)

**Summary:** Objective: Consumer face camera remote photoplethysmography (rPPG) enables passive cardiovascular monitoring, but whether single-cycle waveform morphology encoding arterial stiffness biomarkers is recoverable from this measurement has not been characterised.   Methods: We evaluated 16 architectures spanning six families on 153 subjects across three datasets, introducing cross-subject Pearson r to distinguish subject-specific recovery from template collapse.   Results: No architecture recovered s...

---

### 34. Beyond Compression: Quantifying Spectral Accessibility in Vision Representations

**Authors:** Akayou A. Kitessa, Yijun Zhao

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03795v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03795v1)

**Summary:** Vision-language models map visual features into a shared embedding space through learned projection layers, yet it remains unclear how these transformations alter the structure of visual information. This study examines changes in representation through spatial-frequency accessibility, measured by the linear recoverability of band-limited Fourier energy from model representations. To isolate effects beyond dimensionality reduction, we introduce Residual Spectral Loss (RSL), which evaluates chang...

---

### 35. Exploring Adversarial Robustness and Safety Alignment in Multilingual Multi-Modal Large Language Models

**Authors:** Hashmat Shadab Malik, Muzammal Naseer, Salman Khan

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03793v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03793v1)

**Summary:** Multimodal Large Language Models integrate visual perception into language reasoning, introducing a continuous attack surface susceptible to adversarial attacks. Prior work on MLLM robustness has focused largely on English-centric tasks, leaving multilingual behaviour unexplored. We address this gap through a systematic study of adversarial robustness and multimodal safety across 12 diverse languages, evaluating open-source MLLMs that acquire multilingual capability through instruction tuning. G...

---

### 36. Training-Free Multi-Concept LoRA Composition with Prompt-Aware Weighting

**Authors:** Georgios Tsoumplekas, Stella Bounareli, Vasileios Argyriou

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03792v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03792v1)

**Summary:** Low-Rank Adaptation (LoRA) successfully enables personalization in text-to-image generation by adapting pre-trained diffusion models to specific visual concepts and styles. However, extending such models to multi-concept customization remains challenging. Naively combining multiple LoRA weights or their outputs often leads to interference among concepts, resulting in degraded visual quality and reduced fidelity to the reference images of individual concepts. This paper proposes a simple yet effe...

---

### 37. SLU-2K: A Question-Based Benchmark for Semantic Evaluation of Sign Language Translation

**Authors:** Zeno Testa, Antonino Furnari, Lorenzo Baraldi, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03788v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03788v1)

**Summary:** Sign Language Translation (SLT) is typically evaluated with surface-form metrics such as BLEU and ROUGE, which reward lexical overlap but do not directly measure whether a translation preserves the meaning of the source sign sequence. This is in contrast with the final objective of integrating SLT in assistive technology. In this work, we shift the focus from Sign Language Translation (SLT) to Sign Language Understanding (SLU), with particular emphasis on semantic understanding. Specifically, we...

---

### 38. AmbientEye: A Dataset for Pupil Segmentation under Natural Ambient Infrared Illumination

**Authors:** Mingyu Han, Hyunyoung Han, Nitheekulawatn Thommakoon, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03774v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03774v1)

**Summary:** Eye tracking is essential for smart glasses, as it provides insight into user attention for ambient intelligence applications. However, most existing eye-tracking systems rely on active infrared (IR) illumination, creating practical barriers to all-day outdoor use due to power consumption. In this paper, we investigate whether passive IR cameras alone, without any active IR light source, can enable reliable pupil detection in unconstrained outdoor environments, where ambient sunlight serves as t...

---

### 39. Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models

**Authors:** Glenn Jocher, Jing Qiu, Mengyu Liu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03748v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03748v1)

**Summary:** Real-time vision demands models that are accurate, efficient, and simple to deploy across diverse hardware. The YOLO family has become widely deployed for this reason, yet most YOLO detectors still rely on non-maximum suppression at inference, carry heavy detection heads due to Distribution Focal Loss, require long training schedules, and can leave the smallest objects without positive label assignments. We present Ultralytics YOLO26, a unified real-time vision model family that addresses these ...

---

### 40. Qwen-Image-Flash: Beyond Objective Design

**Authors:** Tianhe Wu, Kun Yan, Zikai Zhou, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03746v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03746v1)

**Summary:** Few-step distillation has become an effective strategy for accelerating advanced visual generative models, yet prior work has largely focused on distillation objectives. In this work, we revisit few-step distillation from a complementary perspective, focusing on the training recipe that critically shapes student performance. Using Qwen-Image-2.0 as a representative case, we systematically investigate three factors in unified text-to-image generation and instruction-guided image editing distillat...

---

### 41. Beyond False Stability: High-Noise Drift Gating for Test-Time Adversarial Defenses in Vision-Language Models

**Authors:** Hashmat Shadab Malik, Muzammal Naseer, Salman Khan

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03730v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03730v1)

**Summary:** Vision-language models (VLMs) such as CLIP show strong zero-shot generalization but remain highly vulnerable to adversarial attacks. Adversarial training improves robustness but is computationally expensive, motivating test-time defenses. Recent approaches exploit how CLIP's visual representations respond to stochastic perturbations: aggregating predictions across noisy views, constructing Gaussian noise-averaged anchors and interpolating features toward them, or applying counter-perturbations. ...

---

### 42. Text-to-Image Models Need Less from Text Encoders Than You Think

**Authors:** Nurit Spingarn, Noa Cohen, Tamar Rott Shaham, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03715v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03715v1)

**Summary:** Text-to-image models rely on text prompts as their primary interface to human intent. Prompts are encoded by a text encoder into embeddings that condition the image generation process. Beyond individual token meanings, text embeddings encode contextual information across the full prompt, such as compositionality and attribute binding. However, whether image models actually exploit this richer information remains underexplored. Here, we address the question: Which aspects of text representation a...

---

### 43. Investigating Adversarial Robustness of Multi-modal Large Language Models

**Authors:** Hashmat Shadab Malik, Muzammal Naseer, Salman Khan

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03713v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03713v1)

**Summary:** Multi-modal Large Language Models (MLLMs) achieve strong performance on vision-language tasks, but incorporating visual inputs through a vision encoder (e.g., CLIP) substantially expands the attack surface, making these models vulnerable to visual adversarial perturbations. Prior defenses typically preserve compatibility with pretrained MLLMs by enforcing strict alignment to CLIP's original embedding space during adversarial fine-tuning; while practical, this constraint fundamentally limits achi...

---

### 44. Face versus Body Tracking for Human-Robot Interaction: An Egocentric Dataset

**Authors:** Jessica Wenninger, Gabriel Skantze

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03694v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03694v1)

**Summary:** To enable meaningful human-robot interaction (HRI), a robot must continuously assess engagement by consistently tracking users over time. State-of-the-art computer vision models, however, are heavily optimized for surveillance or autonomous driving. A social robot faces distinct egocentric challenges, such as humans bouncing, obstructing each other, or leaving the frame. Frequent identity switches (IDSW) cause the robot to lose its footing mid-conversation. To address this, we introduce a novel,...

---

### 45. Does Language Shift Break Medical Vision-Language Models? Indonesian Radiology Visual Question Answering Case Study

**Authors:** Pieter Christy Yan Yudhistira, Dzaki Rafif Malik, Novanto Yudistira

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03693v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03693v1)

**Summary:** Medical Vision-Language Models (VLMs) are typically evaluated on English radiology visual question answering benchmarks, leaving their robustness under non-English clinical language largely unexplored. We introduce IndoRad-VQA, an Indonesian adaptation of VQA-RAD, to assess whether medical VLMs retain radiology reasoning ability when questions are asked in Bahasa Indonesia. Radiology question-answer pairs are translated into Indonesian with self-evaluation-based quality control to preserve clini...

---

### 46. A Fast Methane Detection Pipeline on Board Satellites Based on Mag1c-SAS and LinkNet

**Authors:** Jonáš Herec, Vít Růžička, Rado Pitoňák, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03675v1)

**Summary:** Methane is a potent greenhouse gas, and detecting leaks early via hyperspectral satellite imagery can help climate change mitigation efforts. Meanwhile, many existing hyperspectral missions only capture areas manually targeted by operators, thus missing potential events of interest. To overcome slow downlink rates cost-effectively, onboard detection is a viable solution. However, traditional methane detection methods are too computationally demanding for resource-limited onboard hardware. This w...

---

### 47. Beyond Single Solution: Multi-Hypothesis Collaborative Deep Unfolding Network for Image Compressive Sensing

**Authors:** Wenxue Cui, Hualin Li, Yuhang Qin, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03666v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03666v1)

**Summary:** Recent deep unfolding networks (DUNs) have advanced Compressive Sensing (CS) by effectively integrating iterative optimization with deep learning architectures. However, most CS approaches predominantly confine their inference to a single solution space, neglecting the inherent ill-posedness of CS problems that intrinsically permits multiple plausible candidate hypotheses. In this paper, a novel Multi-Hypothesis Collaborative Deep Unfolding CS Network (MHC-DUN) is proposed, which explicitly mode...

---

### 48. Graph Regularized Non-negative Reduced Biquaternion Matrix Factorization for Color Image Recognition

**Authors:** Hailang Wu, Yonghe Liu, Bingxuan Yu, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03654v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03654v1)

**Summary:** Non-negative reduced biquaternion matrix factorization (NRBMF) uses the product of reduced biquaternion (RB) matrices to incorporate the non-negativity constraints of color image pixels into the factorization process. However, NRBMF mainly focuses on reconstruction accuracy and does not exploit the local geometric structure of image data, which may limit the discriminative ability of the learned low-dimensional features. To address this issue, we propose a graph regularized non-negative reduced ...

---

### 49. A Benchmark for Semi-supervised Multi-modal Crowd Counting

**Authors:** Haoliang Meng, Xiaopeng Hong, Yabin Wang, et al.

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03646v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03646v1)

**Summary:** This paper constructs the first benchmark on semi-supervised multi-modal crowd counting. To lay the foundation for this unexplored task, we first formulate the semi-supervised multi-modal setting and a standardized protocol that specifies the labeled-unlabeled data partition across different labeled ratios. Next, to establish solid reference points, we carefully tailor a diverse set of representative baselines, including existing fully supervised multi-modal methods and semi-supervised single-mo...

---

### 50. VidMsg: A Benchmark for Implicit Message Inference in Short Videos

**Authors:** Issar Tzachor, Michael Green, Rami Ben-Ari

**Published:** 2026-06-02

🔗 [Paper](http://arxiv.org/abs/2606.03635v1) | 📄 [PDF](https://arxiv.org/pdf/2606.03635v1)

**Summary:** Understanding short online videos involves more than identifying visible objects and actions; video makers often include an underlying message or purpose in the clip. We introduce VidMsg, a benchmark for evaluating implicit message understanding in short, internet-native video clips. VidMsg contains 400 YouTube-derived clips across 9 practical topic areas and 52 fine-grained target messages, covering domains such as career and finance, education, health and well-being, culture, safety, sustainab...

---

