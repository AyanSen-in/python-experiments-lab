import streamlit as st

st.set_page_config(page_title="AI Terminology Explorer", page_icon="🤖")

st.title("🤖 AI Terminology Explorer")
st.caption("Select a term to see its explanation.")

terms = [
    "Large Language Model (LLM)",
    "Embeddings",
    "Training",
    "Inference",
    "Vector Databases",
    "AI Agents",
    "RAG (Retrieval-Augmented Generation)",
    "Context Window",
    "Fine-Tuning",
    "Prompt Engineering",
    "Context Engineering",
    "Context Engineering vs Prompt Engineering",
    "Context Layer",
    "MCP (Model Context Protocol)",
    "Context Sources",
    "Context Security",
    "Context Evaluation",
]

choice = st.selectbox("Choose a term", terms)

st.subheader(choice)

if choice == "Large Language Model (LLM)":
    st.write("""
An LLM (Large Language Model) is an AI trained on vast text
 datasets to understand and generate human-like language 
 via next-token prediction. While it natively handles tasks 
 like translation, summarization, and writing, capabilities 
 like web browsing or code execution come from software layers
   wrapped around the model. Though highly versatile, LLMs 
   require massive computing power and can mirror biases 
   present in their training data.

Examples include GPT, Claude, Gemini, and Llama.
""")

elif choice == "Embeddings":
    st.write("""
Embeddings are dense, continuous vector representations of 
data, such as words, sentences, or images, in a lower-dimensional 
space. They capture the semantic relationships and patterns in 
the data, where similar items are placed closer together in the 
vector space. In machine learning, embeddings are used to convert 
complex data into a numerical form that models can process more easily.
 For example, word embeddings represent words based on their meanings 
 and contexts, allowing models to understand relationships like synonyms 
 or analogies. Embeddings are widely used in tasks like natural language 
 processing, recommendation systems, and image recognition to improve 
 model performance and efficiency.
""")

elif choice == "Training":
    st.write("""
Training refers to the process of teaching a machine learning model to
 recognize patterns and make predictions by exposing it to a dataset.
During training, the model learns from the data by adjusting its
internal parameters to minimize errors between its predictions 
and the actual outcomes. This process involves iteratively feeding 
the model with input data, comparing its outputs to the correct answers, 
and refining its predictions through techniques like gradient descent.
 The goal is to enable the model to generalize well so that it can make
accurate predictions on new, unseen data
""")

elif choice == "Inference":
    st.write("""
In artificial intelligence (AI), inference refers to the process by 
which a trained machine learning model makes predictions or draws 
conclusions from new, unseen data. Unlike training, inference involves 
the model applying what it has learned to make decisions without needing
 examples of the exact result. In essence, inference is the AI model actively 
 functioning. For example, a self-driving car recognizing a stop sign on a 
 road it has never encountered before demonstrates inference. The model identifies
   the stop sign in a new setting, using its learned knowledge to make 
   a decision in real-time.        

For example, when you send a question to an LLM and receive
an answer, the model is performing inference.
""")

elif choice == "Vector Databases":
    st.write("""
Vector databases are specialized systems designed to store, 
index, and retrieve high-dimensional vectors, often used as 
embeddings that represent data like text, images, or audio. 
Unlike traditional databases that handle structured data, 
vector databases excel at managing unstructured data by enabling
 fast similarity searches, where vectors are compared to find 
 those that are most similar to a query. This makes them essential 
 for tasks like semantic search, recommendation systems, and content
   discovery, where understanding relationships between items is crucial.
     Vector databases use indexing techniques such as approximate 
     nearest neighbor (ANN) search to efficiently handle large datasets,
       ensuring quick and accurate retrieval even at scale.
""")

elif choice == "AI Agents":
    st.write("""
In AI engineering, "agents" refer to autonomous systems or components
 that can perceive their environment, make decisions, and take actions
   to achieve specific goals. Agents often interact with external systems,
     users, or other agents to carry out complex tasks. They can vary in
  complexity, from simple rule-based bots to sophisticated AI-powered
  agents that leverage machine learning models, natural language 
 processing, and reinforcement learning.
""")

elif choice == "RAG (Retrieval-Augmented Generation)":
    st.write("""
Retrieval-Augmented Generation (RAG) is an AI approach that
 combines information retrieval with language generation to 
 create more accurate, contextually relevant outputs. 
 It works by first retrieving relevant data from a knowledge
   base or external source, then using a language model to generate 
   a response based on that information. This method enhances the 
   accuracy of generative models by grounding their outputs in real-world data,
     making RAG ideal for tasks like question answering, summarization,
       and chatbots that require reliable, up-to-date information.

Typical flow:

User -> Retrieve information -> LLM -> Answer
""")

elif choice == "Context Window":
    st.write("""
The context window is the amount of text an LLM can process 
in a single request, measured in tokens. It includes the 
system prompt, conversation history, retrieved documents, 
and the model's own output as it generates a response. 
Once the total content exceeds this limit, older or lower 
priority information has to be dropped, summarized, or moved 
out of the active context. Model providers have expanded context windows
 significantly over the past few years, but a larger window does 
 not guarantee the model uses all of it well.
""")

elif choice == "Fine-Tuning":
    st.write("""
Fine-tuning involves taking a pre-trained large language
 model (LLM) and further training it on a smaller, task-specific dataset.
   This adapts the LLM to perform better on a particular task or domain.
     However, fine-tuning can be resource-intensive and may not always 
     be the most efficient approach. Prompt engineering, retrieval-augmented
       generation (RAG), or using smaller, specialized models can sometimes 
       achieve comparable or even better results with less computational 
       overhead and data requirements.
""")

elif choice == "Prompt Engineering":
    st.write("""
Prompt engineering is the art and science of crafting effective prompts,
 which are the instructions or inputs given to a large language model (LLM).
   The goal is to design prompts that elicit the desired response from the LLM, 
   guiding it to generate accurate, relevant, and creative outputs. 
   This involves understanding the LLM's capabilities and limitations, 
   and experimenting with different prompt structures, keywords, 
   and contextual cues to achieve optimal results.
""")

elif choice == "Context Engineering":
    st.write("""
Context engineering is the practice of carefully designing and
 organizing the information you give to an AI model so it can do its job better.
   Think of it like preparing everything an AI needs before it starts 
   working (including providing the right instructions, examples,
     background knowledge, and conversation history), all put together smartly 
     so the model gives you the best possible answer. Instead of just asking a 
     question and hoping for the best, you are building the perfect "environment"
       of information around the AI to guide it toward success.
""")

elif choice == "Context Engineering vs Prompt Engineering":
    st.write("""
Prompt engineering focuses on how a single instruction is worded to
 get a better response from a model. Context engineering is broader:
   it deals with what information reaches the model at all, 
   from which sources, in what order, and in what format, across an 
   entire application or agent workflow. A well written prompt can 
   still fail if the model lacks the right data, tools, or history to act on it.
     Context engineering treats the prompt as just one part of a larger system
       that also includes retrieval, memory, and tool outputs.
""")

elif choice == "Context Layer":
    st.write("""
A context layer is the part of an AI system responsible for gathering, 
organizing, and delivering the right information to a model before it generates a response.
 It sits between raw data sources, such as databases, documents, and APIs, 
 and the model itself, deciding what gets included and what gets left out.
   Some teams build this layer themselves using retrieval pipelines and memory stores, 
   while others rely on dedicated context platforms. The goal is to give the model relevant,
     trustworthy information without overwhelming it with everything available.
""")

elif choice == "MCP (Model Context Protocol)":
    st.write("""
MCP, or Model Context Protocol, is an open standard that lets AI applications 
connect to external tools, data sources, and services in a consistent way.
 Instead of writing a custom integration for every tool a model might need, 
 developers expose that tool through an MCP server, and any MCP compatible client 
 can then call it. This reduces the number of one-off integrations needed as agents
   connect to more systems. Anthropic introduced MCP, and it has since been adopted
     by other model providers and tool builders.
""")

elif choice == "Context Sources":
    st.write("""
Context sources are the places an AI system pulls information from to 
build what a model sees at inference time. Common sources include documents 
and knowledge bases, databases and data warehouses, code repositories, 
chat and support tools, and the outputs of other tool calls or agents.
 Each source has its own update frequency, access rules, and format, 
 so combining them well requires normalizing and filtering before the data reaches the model. 
 Choosing the right sources for a task matters as much as how much data is included.

Examples include:

- User input
- Conversation history
- Documents
- Databases
- APIs
- Vector databases
- Tools
- Memory
""")

elif choice == "Context Security":
    st.write("""
Context security covers the risks that come from feeding external or untrusted 
content into an AI system. A malicious document, email, or web page can contain 
hidden instructions designed to manipulate the model, a technique known as prompt injection.
 Poor access controls can also let a model surface data to a user who should not see it,
   or let sensitive information leak through tool calls and logs. Building context pipelines 
   securely means validating sources, applying permission checks before data reaches the model,
     and treating retrieved content as data rather than as trusted instructions.

Important concerns include:

- Sensitive data exposure
- Prompt injection
- Malicious retrieved content
- Unauthorized tool access
- Data leakage
- Untrusted context
""")

elif choice == "Context Evaluation":
    st.write("""
Context evaluation measures whether the information delivered to a model actually
 helps it perform a task well. This includes checking whether retrieved documents 
 are relevant, whether important details are missing, and whether irrelevant or 
 outdated content is crowding out what matters. Teams use a mix of automated metrics,
   such as retrieval precision and recall, and manual review of model outputs to catch problems.
     Without this evaluation, a context pipeline can look complete while still giving
       the model poor material to work with.

For example, you can evaluate:

- Context relevance
- Context accuracy
- Retrieval quality
- Missing information
- Context size
- Final answer quality
""")

else:
    st.write("Invalid choice. Please select a term from the list.")