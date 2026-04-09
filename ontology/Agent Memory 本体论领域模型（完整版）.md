# Agent Memory 本体论领域模型（完整版）

本文档为 **Agent Memory（智能体记忆）领域本体论模型** 完整版，基于本体论核心思想（类\-属性\-关系\-公理），结合智能体记忆的生理机制、工程实现逻辑，细化各层级概念、约束规则和应用映射，统一记忆系统的语义标准，可直接用于知识图谱建模、智能体架构设计、学术论文参考、工程落地适配（如LangGraph、Mem0、VectorDB等框架）。

核心定位：形式化定义智能体记忆的概念、结构、生命周期、关联关系与推理规则，解决智能体记忆“语义不统一、关联不清晰、推理无依据”的问题，支撑记忆的存储、检索、遗忘、总结、联想、反思等智能行为，实现记忆与智能体目标、行为、环境的深度绑定。

# 一、本体论核心基础（必备前提）

Agent Memory 本体遵循“五层本体结构”，即：**顶层类 → 子类 → 属性（对象属性\+数据属性） → 关系 → 公理与约束**，同时补充“实例说明”“工程映射”“应用场景”，确保模型的理论完整性和工程可落地性。

核心原则：

- 语义唯一性：每个类、属性、关系均有明确且唯一的定义，无歧义；

- 层级清晰性：子类继承顶层类的核心属性，同时具备自身特有属性，不跨层级冗余；

- 工程适配性：所有概念均对应智能体记忆系统的实际组件（如VectorDB、上下文窗口）；

- 可扩展性：预留子类和属性扩展接口，适配不同类型智能体（对话Agent、工具Agent、多智能体）。

# 二、顶层核心类（Top\-Level Classes）

顶层类是Agent Memory本体的核心骨架，定义了记忆系统的核心参与方、核心组件和核心行为，共10个顶层类，每个类均有明确的语义边界和核心定位，无交叉冗余。

|顶层类名称|核心定位|核心说明|
|---|---|---|
|Agent（智能体）|记忆的主体|拥有记忆系统，执行记忆操作，基于记忆做出决策，是记忆的所有者和使用者|
|Memory（记忆单元）|记忆的核心载体|存储具体的记忆内容，是记忆系统的最小功能单元，具备生命周期（创建\-存储\-检索\-更新\-遗忘）|
|MemorySystem（记忆系统）|记忆的管理容器|统筹所有记忆单元，执行记忆操作的调度，适配不同类型记忆的存储和检索需求|
|MemoryContent（记忆内容）|记忆单元的具体内容|记忆单元所承载的实际信息，可分为结构化、非结构化、向量化等类型|
|MemoryEvent（记忆事件）|记忆的生成触发源|导致记忆生成的具体事件（如对话、工具调用、环境观察），是记忆的“来源凭证”|
|MemoryOperation（记忆操作）|记忆的行为动作|智能体对记忆执行的具体操作（存储、检索、遗忘等），是记忆生命周期的核心驱动|
|Context（上下文）|记忆的关联场景|记忆生成、存储、检索时的场景信息，用于提升记忆检索的准确性和关联性|
|Entity（实体）|记忆的关联对象|记忆中涉及的人、物、地点、时间、主题等具体对象，是记忆关联的核心载体|
|Relation（实体间关系）|实体的关联逻辑|连接不同实体的语义关系，用于记忆的联想推理（如“用户A”与“需求B”的“提出”关系）|
|Policy（记忆策略）|记忆操作的规则约束|定义记忆操作的触发条件、执行标准（如遗忘阈值、检索排序规则），保障记忆系统的合理性|

# 三、子类层级结构（Subclass Hierarchy）

子类继承对应顶层类的核心属性，同时增加自身特有属性和语义边界，细化记忆系统的具体组件，所有子类均遵循“单一职责”原则，避免语义交叉。以下按顶层类分类，详细列出子类及说明。

## 3\.1 Agent（智能体）子类

基于智能体的功能、应用场景分类，适配不同类型智能体的记忆需求，子类可根据实际场景扩展。

- **自主Agent（AutonomousAgent）**

    - 核心特征：具备自主决策、自主环境交互能力，无需人工干预

    - 典型实例：自主导航Agent、自主任务执行Agent

    - 记忆需求：需存储环境状态、任务进度、决策历史、失败经验

- **对话Agent（DialogAgent）**

    - 核心特征：以自然语言对话为核心功能，与用户进行交互

    - 典型实例：客服Agent、聊天机器人、问答Agent

    - 记忆需求：需存储对话历史、用户偏好、对话上下文、领域知识

- **工具使用Agent（ToolUsingAgent）**

    - 核心特征：可调用外部工具（API、数据库、工具包）完成任务

    - 典型实例：数据分析Agent、代码生成Agent、文件处理Agent

    - 记忆需求：需存储工具调用历史、工具参数、工具返回结果、调用经验

- **多智能体团队Agent（MultiAgentTeam）**

    - 核心特征：由多个子Agent组成，协同完成复杂任务，具备团队协作能力

    - 典型实例：项目管理多Agent、多模态协同Agent

    - 记忆需求：需存储团队分工、协同历史、子Agent交互记录、团队目标

- **领域专用Agent（DomainSpecificAgent）**

    - 核心特征：针对特定领域（如医疗、金融、教育）设计，具备领域专业知识

    - 典型实例：医疗诊断Agent、金融风控Agent

    - 记忆需求：需存储领域知识、领域规则、用户领域相关数据

## 3\.2 Memory（记忆单元）子类

记忆单元的子类基于“记忆的存储时长、功能定位、内容类型”分类，对应智能体记忆的经典生理机制（感官记忆\-短时记忆\-长时记忆），同时结合工程实现补充检索记忆、缓冲记忆等子类。

- **SensoryMemory（感官记忆）**

    - 核心特征：存储智能体通过“感官”获取的原始信息，存储时长极短（毫秒\-秒级），易遗忘

    - 子类：
                

        - TextMemory（文本记忆）：如用户输入的文本、系统输出的文本

        - VisualMemory（视觉记忆）：如图像、视频帧、视觉特征

        - AudioMemory（语音记忆）：如语音片段、音频特征

        - TactileMemory（触觉记忆）：如环境触感、操作反馈（适用于机器人Agent）

    - 工程映射：对应智能体的输入缓冲区，暂存未处理的原始输入

- **ShortTermMemory / WorkingMemory（短时/工作记忆）**

    - 核心特征：存储智能体当前正在处理的信息，存储时长较短（分钟级），容量有限，用于临时计算和决策

    - 子类：
                

        - DialogContextMemory（对话上下文记忆）：当前对话的上下文、用户最新需求

        - TaskStackMemory（任务栈记忆）：当前正在执行的任务、任务步骤、任务状态

        - AttentionWindowMemory（注意力窗口记忆）：智能体当前关注的核心信息、重点内容

    - 工程映射：对应大模型的上下文窗口（Context Window）、任务队列

- **LongTermMemory（长时记忆）**

    - 核心特征：存储智能体长期需要使用的信息，存储时长较长（小时\-永久），容量无限（依赖存储介质），可被检索和更新

    - 子类（核心）：
                

        - EpisodicMemory（情景记忆）：记录“发生了什么”，绑定时间、地点、参与者，具备自传性

        - SemanticMemory（语义记忆）：记录“是什么”，即知识、事实、概念、规则，不绑定具体场景

        - ProceduralMemory（过程记忆）：记录“怎么做”，即技能、步骤、操作流程，用于指导智能体行为

    - 工程映射：对应VectorDB（向量数据库）、知识库（如FAISS、Chroma）、技能库

- **EpisodicBuffer（情景缓冲器）**

    - 核心特征：连接短时记忆和长时记忆，将短时记忆中的情景信息进行临时整合，再转入长时记忆

    - 功能：避免短时记忆信息丢失，对情景信息进行初步筛选和整理

    - 工程映射：对应记忆系统的“中间缓冲区”，用于记忆的预处理

- **RetrievalMemory（检索记忆）**

    - 核心特征：存储记忆的索引信息（如向量嵌入、关键词），用于快速检索长时记忆中的内容

    - 功能：提升记忆检索效率，建立记忆之间的关联索引

    - 工程映射：对应VectorDB的索引层、关键词索引表

## 3\.3 MemoryContent（记忆内容）子类

记忆内容的子类基于“内容的结构化程度、数据类型”分类，覆盖智能体记忆的所有内容形式，确保内容的多样性和可扩展性。

- **UnstructuredContent（非结构化内容）**

    - 文本内容（TextContent）：对话文本、段落、句子、关键词

    - 视觉内容（VisualContent）：图像像素、视频帧、视觉特征描述

    - 语音内容（AudioContent）：语音波形、语音转文字、音频特征

    - 自然语言描述（NaturalLanguageDescription）：对事件、实体的自然语言描述

- **StructuredContent（结构化内容）**

    - 事实三元组（FactTriple）：如（用户A，提出，需求B）、（Agent，调用，工具C）

    - 表格数据（TableContent）：如用户信息表、工具参数表、任务进度表

    - 键值对（KeyValueContent）：如\{“用户偏好”: “喜欢简洁回复”\}、\{“任务状态”: “未完成”\}

    - 结构化事件（StructuredEvent）：如\{“事件类型”: “对话”, “参与者”: “用户A”, “时间”: “2024\-05\-01”\}

- **VectorContent（向量内容）**

    - 向量嵌入（EmbeddingContent）：记忆内容的向量表示（如BERT、Sentence\-BERT生成的向量）

    - 向量索引（VectorIndex）：用于检索的向量索引信息

- **DerivedContent（衍生内容）**

    - 摘要/总结（SummaryContent）：对原始记忆内容的提炼和总结

    - 情绪标签（EmotionTag）：如“积极”“消极”“中性”“紧急”，用于标记记忆的情绪属性

    - 重要度分数（ImportanceScore）：标记记忆的重要程度，用于遗忘和检索排序

    - 反思结论（ReflectionConclusion）：智能体对记忆内容的反思和总结（如“此次工具调用失败，原因是参数错误”）

## 3\.4 MemoryEvent（记忆事件）子类

记忆事件是记忆生成的“触发源”，子类基于“事件的类型、功能”分类，覆盖智能体所有可能生成记忆的场景。

- **DialogEvent（对话事件）**

    - 用户输入事件（UserInputEvent）：用户向智能体发送文本、语音、图像等输入

    - Agent回复事件（AgentReplyEvent）：智能体向用户发送回复内容

    - 对话结束事件（DialogEndEvent）：对话终止（如用户退出、任务完成）

- **ToolEvent（工具事件）**

    - 工具调用事件（ToolCallEvent）：智能体发起工具调用请求

    - 工具返回事件（ToolReturnEvent）：工具向智能体返回执行结果

    - 工具调用失败事件（ToolFailEvent）：工具调用出错（如参数错误、接口异常）

- **EnvironmentEvent（环境事件）**

    - 环境观察事件（EnvironmentObserveEvent）：智能体观察环境状态（如位置、温度、其他Agent状态）

    - 环境变化事件（EnvironmentChangeEvent）：环境状态发生变化（如位置移动、温度变化）

- **DecisionEvent（决策事件）**

    - 决策生成事件（DecisionGenerateEvent）：智能体生成决策结论

    - 决策执行事件（DecisionExecuteEvent）：智能体执行决策动作

    - 决策反馈事件（DecisionFeedbackEvent）：决策执行后的反馈（如成功、失败）

- **FeedbackEvent（反馈事件）**

    - 用户反馈事件（UserFeedbackEvent）：用户对智能体的回复、行为进行评价（如好评、差评、修改建议）

    - 系统反馈事件（SystemFeedbackEvent）：系统对智能体的操作进行反馈（如内存不足、权限不足）

- **ErrorEvent（错误事件）**

    - 执行错误事件（ExecutionErrorEvent）：智能体执行动作时出现错误（如代码报错、操作失误）

    - 记忆错误事件（MemoryErrorEvent）：记忆存储、检索、更新时出现错误（如记忆丢失、检索失败）

## 3\.5 MemoryOperation（记忆操作）子类

记忆操作是智能体对记忆的核心行为，子类基于“操作的功能、目的”分类，覆盖记忆生命周期的全流程，每个操作均有明确的触发条件和执行结果。

- **基础操作（BasicOperation）**

    - 存储（Store）：将记忆内容存入记忆单元，触发条件：新的记忆事件发生、记忆内容经过预处理

    - 检索（Retrieve）：根据检索条件（关键词、向量、上下文）从记忆单元中获取相关记忆

    - 更新（Update）：修改记忆单元的内容、属性（如重要度、过期时间），触发条件：记忆内容发生变化、反思后修正

    - 遗忘（Forget）：删除记忆单元或标记记忆单元为“不可检索”，触发条件：达到遗忘阈值、记忆过期、容量不足

- **高级操作（AdvancedOperation）**

    - 合并（Merge）：将多个相似的记忆单元合并为一个，避免冗余，触发条件：存在重复或相似记忆

    - 总结（Summarize）：对单个或多个记忆单元的内容进行提炼，生成摘要，触发条件：记忆内容过长、需要长期存储

    - 联想（Associate）：根据当前记忆，关联其他相关的记忆单元，触发条件：检索记忆时、决策需要

    - 反思（Reflect）：对记忆内容进行分析、评价，生成反思结论，更新记忆属性，触发条件：任务完成后、出现错误后、定期触发

    - 去重（Deduplicate）：识别并删除重复的记忆内容，触发条件：存储新记忆时、定期维护时

## 3\.6 Context（上下文）子类

上下文是记忆的“场景标签”，用于关联记忆与具体场景，提升记忆检索的准确性，子类基于“场景的类型”分类。

- **TimeContext（时间上下文）**

    - 绝对时间（AbsoluteTime）：记忆生成的具体时间（如2024\-05\-01 10:00:00）

    - 相对时间（RelativeTime）：记忆生成的相对时间（如“5分钟前”“昨天”）

    - 时间区间（TimeInterval）：记忆对应的时间范围（如“2024\-05\-01至2024\-05\-02”）

- **LocationContext（地点上下文）**

    - 物理地点（PhysicalLocation）：如“办公室”“北京”“机器人当前位置”

    - 虚拟地点（VirtualLocation）：如“微信对话框”“API接口页面”“元宇宙场景”

- **TaskContext（任务上下文）**

    - 任务ID（TaskID）：当前执行任务的唯一标识

    - 任务类型（TaskType）：如“问答任务”“工具调用任务”“决策任务”

    - 任务进度（TaskProgress）：如“未开始”“进行中”“已完成”

    - 任务目标（TaskGoal）：当前任务的核心目标

- **DialogContext（对话上下文）**

    - 会话ID（SessionID）：当前对话的唯一标识

    - 对话主题（DialogTopic）：当前对话的核心主题

    - 对话角色（DialogRole）：如“用户”“Agent”“第三方”

- **EnvironmentContext（环境状态上下文）**

    - 环境状态（EnvironmentState）：如“安静”“嘈杂”“网络正常”“内存不足”

    - 环境参数（EnvironmentParameter）：如温度、湿度、网络延迟（适用于机器人、物联网Agent）

## 3\.7 Entity（实体）子类

实体是记忆中涉及的具体对象，子类基于“实体的类型”分类，覆盖智能体记忆中所有可能出现的对象，可根据领域需求扩展。

- **User（用户）**

    - 普通用户（NormalUser）：与智能体交互的普通用户

    - 管理员（Administrator）：管理智能体的用户

    - 第三方用户（ThirdPartyUser）：参与交互的第三方人员

- **AgentEntity（智能体实体）**

    - 自身智能体（SelfAgent）：记忆的所有者，当前智能体

    - 其他智能体（OtherAgent）：与当前智能体交互的其他智能体（适用于多智能体场景）

    - 子智能体（SubAgent）：多智能体团队中的子Agent

- **Object（物体）**

    - 物理物体（PhysicalObject）：如“手机”“电脑”“机器人”

    - 虚拟物体（VirtualObject）：如“文件”“API接口”“数据库”

- **Location（位置）**

    - 物理位置（PhysicalLocation）：如“城市”“街道”“房间”

    - 虚拟位置（VirtualLocation）：如“网页”“对话框”“元宇宙场景”

- **Time（时间）**

    - 时刻（Moment）：如“2024\-05\-01 10:00:00”

    - 时间段（TimePeriod）：如“一天”“一个小时”

    - 时间节点（TimeNode）：如“任务开始时间”“记忆生成时间”

- **Topic（主题）**

    - 对话主题（DialogTopic）：如“天气查询”“代码生成”“医疗咨询”

    - 任务主题（TaskTopic）：如“数据分析”“文件处理”“导航”

    - 领域主题（DomainTopic）：如“金融”“医疗”“教育”

## 3\.8 Relation（实体间关系）子类

实体间关系是连接不同实体的语义纽带，用于记忆的联想推理，子类基于“关系的类型、功能”分类，覆盖实体间的主要关联场景。

- **交互关系（InteractionRelation）**

    - 提出（Propose）：如“用户A 提出 需求B”

    - 回复（Reply）：如“Agent 回复 用户A”

    - 调用（Call）：如“Agent 调用 工具C”

    - 协作（Cooperate）：如“AgentA 协作 AgentB”

- **归属关系（AttributionRelation）**

    - 拥有（Own）：如“Agent 拥有 记忆系统”

    - 属于（BelongTo）：如“记忆单元 属于 长时记忆”

    - 包含（Contain）：如“记忆系统 包含 记忆单元”

- **时间关系（TimeRelation）**

    - 发生在（OccurAt）：如“对话事件 发生在 2024\-05\-01”

    - 早于（EarlierThan）：如“记忆A 早于 记忆B 生成”

    - 晚于（LaterThan）：如“记忆B 晚于 记忆A 生成”

- **空间关系（SpatialRelation）**

    - 位于（LocatedAt）：如“Agent 位于 办公室”

    - 靠近（CloseTo）：如“物体A 靠近 物体B”

- **因果关系（CausalRelation）**

    - 导致（Cause）：如“参数错误 导致 工具调用失败”

    - 源于（OriginateFrom）：如“记忆A 源于 对话事件B”

- **关联关系（AssociationRelation）**

    - 关联（AssociateWith）：如“记忆A 关联 记忆B”

    - 相关（RelevantTo）：如“主题A 相关 主题B”

## 3\.9 Policy（记忆策略）子类

记忆策略是记忆操作的“规则约束”，子类基于“策略的功能”分类，确保记忆系统的合理性和高效性。

- **遗忘策略（ForgetPolicy）**

    - 基于重要度的遗忘策略（ImportanceBasedForget）：重要度低于阈值的记忆被遗忘

    - 基于时间的遗忘策略（TimeBasedForget）：超过过期时间的记忆被遗忘

    - 基于容量的遗忘策略（CapacityBasedForget）：记忆容量达到上限时，遗忘最不重要的记忆

    - 基于使用频率的遗忘策略（FrequencyBasedForget）：长期未被检索的记忆被遗忘

- **检索策略（RetrievePolicy）**

    - 基于相似度的检索策略（SimilarityBasedRetrieve）：优先检索与检索条件相似度高的记忆

    - 基于时间的检索策略（TimeBasedRetrieve）：优先检索近期生成的记忆

    - 基于重要度的检索策略（ImportanceBasedRetrieve）：优先检索重要度高的记忆

    - 混合检索策略（HybridRetrieve）：结合相似度、时间、重要度进行检索

- **存储策略（StorePolicy）**

    - 预处理策略（PreprocessPolicy）：存储前对记忆内容进行去重、摘要、向量化

    - 分类存储策略（ClassificationStore）：根据记忆类型存储到对应的记忆单元（如短时记忆、长时记忆）

    - 持久化策略（PersistencePolicy）：定义记忆的持久化方式（如本地存储、云端存储）

- **更新策略（UpdatePolicy）**

    - 定期更新策略（PeriodicUpdate）：定期更新记忆的重要度、摘要等属性

    - 触发式更新策略（TriggeredUpdate）：当记忆内容发生变化、收到反馈时，触发更新

    - 反思更新策略（ReflectionUpdate）：基于反思结论，更新记忆内容和属性

- **权重策略（WeightPolicy）**

    - 重要度权重策略（ImportanceWeight）：定义重要度的计算规则（如访问次数×0\.4 \+ 情绪值×0\.3 \+ 关联性×0\.3）

    - 检索权重策略（RetrieveWeight）：定义检索时各因素（相似度、时间、重要度）的权重占比

# 四、核心属性（Properties）

属性分为“对象属性”和“数据属性”：对象属性用于描述类与类之间的关联关系，数据属性用于描述类的具体特征（如ID、时间、数值），所有属性均有明确的定义域（Domain）和值域（Range）。

## 4\.1 对象属性（Object Properties）

对象属性连接两个类，描述它们之间的语义关系，定义域为“源类”，值域为“目标类”，以下列出核心对象属性（完整属性可根据场景扩展）。

|对象属性名称|定义域（源类）|值域（目标类）|核心说明|
|---|---|---|---|
|hasMemorySystem（拥有记忆系统）|Agent|MemorySystem|每个Agent拥有一个唯一的MemorySystem，用于管理自身的记忆|
|executeOperation（执行记忆操作）|Agent|MemoryOperation|Agent主动执行对记忆的操作（存储、检索、遗忘等）|
|containMemory（包含记忆单元）|MemorySystem|Memory|MemorySystem包含多个Memory，统筹管理所有记忆单元|
|carryContent（承载记忆内容）|Memory|MemoryContent|每个Memory单元承载一个或多个MemoryContent（如文本\+向量）|
|associateContext（关联上下文）|Memory|Context|Memory单元关联对应的上下文，用于场景化检索|
|involveEntity（涉及实体）|Memory|Entity|Memory单元涉及一个或多个Entity，是记忆关联的核心对象|
|linkMemory（链接其他记忆）|Memory|Memory|Memory单元与其他Memory单元建立关联，用于联想推理|
|generateMemory（生成记忆）|MemoryEvent|Memory|每个MemoryEvent触发生成一个或多个Memory单元|
|actOnMemory（作用于记忆）|MemoryOperation|Memory|MemoryOperation作用于指定的Memory单元，执行具体操作|
|controlOperation（控制记忆操作）|Policy|MemoryOperation|Policy定义MemoryOperation的触发条件和执行规则，控制操作的执行|
|dependOn（依赖）|WorkingMemory|LongTermMemory|WorkingMemory依赖LongTermMemory，可从LongTermMemory中检索信息补充自身|
|haveRelation（具有关系）|Entity|Relation|Entity之间通过Relation建立关联，形成语义网络|

## 4\.2 数据属性（Data Properties）

数据属性描述类的具体特征，定义域为对应的类，值域为具体的数据类型（如字符串、数值、布尔值），以下列出核心数据属性（完整属性可根据场景扩展）。

|数据属性名称|定义域（类）|值域（数据类型）|核心说明|
|---|---|---|---|
|agentId（智能体ID）|Agent|字符串（String）|智能体的唯一标识，用于区分不同Agent|
|agentRole（智能体角色）|Agent|字符串（String）|智能体的角色（如客服、数据分析、导航）|
|agentGoal（智能体目标）|Agent|字符串（String）|智能体的核心目标（如“提供高效客服回复”）|
|memoryId（记忆ID）|Memory|字符串（String）|记忆单元的唯一标识，用于检索和更新|
|createTime（创建时间）|Memory|日期时间（DateTime）|记忆单元的生成时间|
|lastAccessTime（最后访问时间）|Memory|日期时间（DateTime）|记忆单元最后被检索的时间，用于遗忘策略|
|importanceScore（重要度分数）|Memory|浮点数（Float）\[0,1\]|记忆单元的重要程度，0为最低，1为最高|
|accessCount（访问次数）|Memory|整数（Integer）|记忆单元被检索的次数，用于计算重要度|
|expireTime（过期时间）|Memory|日期时间（DateTime）|记忆单元的过期时间，超过该时间可被遗忘|
|memorySource（记忆来源）|Memory|字符串（String）|记忆单元的生成来源（如“对话事件”“工具调用事件”）|
|emotionValue（情绪值）|Memory|浮点数（Float）\[\-1,1\]|记忆单元的情绪属性，\-1为消极，0为中性，1为积极|
|vectorId（向量ID）|Memory|字符串（String）|记忆向量的唯一标识，用于向量检索|
|sessionId（会话ID）|Context|字符串（String）|对话上下文的唯一标识，用于关联同一会话的记忆|
|eventType（事件类型）|MemoryEvent|字符串（String）|记忆事件的类型（如“用户输入”“工具调用”）|
|forgetThreshold（遗忘阈值）|Policy|浮点数（Float）\[0,1\]|遗忘策略的阈值，重要度低于该值的记忆被遗忘|
|retrieveTopK（检索TopK）|Policy|整数（Integer）|检索策略中，返回前K个最相关的记忆|

# 五、公理与约束（Axioms \&amp; Constraints）

公理与约束是Agent Memory本体的“逻辑规则”，用于规范类、属性、关系的行为，确保记忆系统的合理性和一致性，分为“唯一性约束”“值域约束”“业务规则约束”“逻辑推理约束”四类。

## 5\.1 唯一性约束（Uniqueness Constraints）

- 每个Agent只能拥有一个MemorySystem（hasMemorySystem属性是唯一的）；

- 每个Memory单元有且只有一个唯一的memoryId（memoryId属性是唯一的）；

- 每个MemoryEvent只能生成对应的Memory单元，且一个Memory单元只能由一个MemoryEvent生成（generateMemory属性是唯一的）；

- 每个Memory单元只能关联一个核心Context（主要上下文），可关联多个次要Context，但核心上下文唯一。

## 5\.2 值域约束（Range Constraints）

- Memory的importanceScore（重要度分数）值域为\[0,1\]，不能小于0或大于1；

- Memory的emotionValue（情绪值）值域为\[\-1,1\]，不能小于\-1或大于1；

- Memory的accessCount（访问次数）值域为非负整数（≥0）；

- Memory的expireTime（过期时间）必须晚于createTime（创建时间）；

- Policy的forgetThreshold（遗忘阈值）值域为\[0,1\]，retrieveTopK（检索TopK）值域为正整数（≥1）；

- WorkingMemory（工作记忆）的容量有限（如最多存储100条记忆单元），超过容量必须触发遗忘或替换。

## 5\.3 业务规则约束（Business Rules）

- 记忆存储约束：新记忆单元入库前，必须经过去重（Deduplicate）操作，避免重复记忆；

- 遗忘规则约束：
        

    - 重要度分数 \&lt; 遗忘阈值 → 触发遗忘操作；

    - 当前时间 \&gt; 过期时间 → 触发遗忘操作；

    - WorkingMemory容量已满 → 遗忘重要度最低的记忆单元；

    - lastAccessTime超过设定时长（如30天）未被访问 → 触发遗忘操作。

- 检索规则约束：记忆检索时，必须结合相似度、时间、重要度进行重排序，优先返回“高相似度\+近期\+高重要度”的记忆；

- 记忆更新约束：
        

    - Memory被检索一次，accessCount（访问次数）加1；

    - accessCount增加时，importanceScore（重要度分数）同步提升（提升幅度由WeightPolicy定义）；

    - 收到用户负面反馈的记忆，emotionValue（情绪值）降低，importanceScore同步降低；

    - 反思后发现错误的记忆，必须触发更新（Update）操作，修正记忆内容。

- 记忆类型约束：
        

    - EpisodicMemory（情景记忆）必须绑定TimeContext（时间上下文）\+ LocationContext（地点上下文）\+ Entity（参与者）；

    - SemanticMemory（语义记忆）不能绑定具体的TimeContext和LocationContext，仅绑定Topic（主题）；

    - ProceduralMemory（过程记忆）必须包含具体的步骤描述，用于指导智能体行为。

## 5\.4 逻辑推理约束（Logical Inference Constraints）

- 传递性推理：若

> （注：文档部分内容可能由 AI 生成）
