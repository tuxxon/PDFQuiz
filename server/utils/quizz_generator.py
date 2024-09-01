from .qcm_chain import QCMGenerateChain
from .qa_llm import QaLlm
import asyncio

async def llm_call(qa_chain: QCMGenerateChain, text: str):
    
    print(f"llm call running...")

    try:
        batch_examples = await asyncio.gather(qa_chain.aapply_and_parse(text))
    except ValueError as e:
        print(f"Error during LLM call: {e}")
        return None

    print(f"llm call done.")
    return batch_examples

async def generate_quizz(content: str):
    """
    Generates a quizz from the given content.
    """
    if not content.strip():
        raise ValueError("Content cannot be empty.")

    qa_llm = QaLlm()
    qa_chain = QCMGenerateChain.from_llm(qa_llm.get_llm())

    return await llm_call(qa_chain, [{"doc": content}])