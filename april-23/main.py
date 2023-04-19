import lmql
import asyncio
import sys


@lmql.query
async def scam_detector(message: str):
    """
    argmax
        "SMS: {message}\n \
        Q: What is the likelihood this SMS is a scam and why?\n \
        A:[ANALYSIS]\n \
        Based on this, the overall likelihood this SMS is a scam is[CLASSIFICATION]"
    from
        "openai/text-davinci-003"
    where
        not "\n" in ANALYSIS and CLASSIFICATION in [" very low", " low", " high", " very high"]
    """


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Did not provide SMS text")
    text_input = sys.argv[1]
    result = asyncio.run(scam_detector(text_input))
    print(result)
