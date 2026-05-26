The marketing technology company and its multiple clients needs to know about their performance in the market they need to answer the questions quickly when someone asks about it , may be it will be an internal team or clients.

Tool :
A RAG system - version 1.

Use Case :
RAG (Retrieval Augmented Generation) is a system where it combination of AI and information(Like Books). We can say RAG = AI + Books for better and related answers. The documents are stored as chuncks and the chuncks are converted into numerical vectors that are stored as a semantic meaning vectors in the vector databases.RAG in general stores the data(Documents of our own company) as a numerical vectors called embeddings.Whenever the user asks a query to the RAG system, the query itself will be converted into numerical vector and the system will then go and fetch the chuncked embedding in the vector database(answer vectors) that is most relevant to the questions asked by the user.The answer will be given to an LLM tool that incorporate the answer and gives as a summarized answer to the user.

Architecture :

 __________________________________________
|                                          |    
|              User Query                  |
|__________________________________________|                                          
                    |
 __________________________________________
|                                          |    
|       Query Converted into Embeddings    |
|__________________________________________|
                    |
 __________________________________________
|                                          |    
|    Answer Embeddings in vector database  |
|__________________________________________|
                    |
 __________________________________________
|                                          |    
|    Answer Embedding + LLM Reasoning      |
|__________________________________________|      
                    |
 __________________________________________
|                                          |    
|    Final relevant answer to the user     |
|__________________________________________|                

Primary users of this tool :

Internal Team members can use it with their admin accounts. This version only supports internal team members once it is used across and get positive response across team we can give a version 2 of this tool to the clients with limited access at first.

Successful Usage :
Usage will be improved because we get instant answers about what we want and exactly the team need.The trust is more with this tool because the data is come from our own company documentations.The reliability is very high because if this.This version is specifically for internal users.


Techstack I will use for this system :

Azure AI Search 
(Indexes, Datasource, Skillset and Indexer).
Python - Scripting language.
LLM - Azure OpenAI services.
FastAPI - API creation and Backend deployment.