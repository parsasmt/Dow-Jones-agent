from agent.schemas import ToolOutput
from agent.schemas import ToolType

from rag.retriever import retrieve

from tools.base_tool import BaseTool


class RagTool(BaseTool):

    name = "RAG"

    def run(self, question: str):

        result = retrieve(question)

        docs = result["documents"][0]

        summary = "\n\n".join(docs)

        return ToolOutput(

            tool=ToolType.RAG,

            summary=summary,

            raw_data=result,

            sources=[
                "Knowledge Base"
            ]

        )