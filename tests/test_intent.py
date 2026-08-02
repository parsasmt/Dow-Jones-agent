from agent.intent import intent_detector

questions = [
    "What is the Dow Jones?",
    "Is Apple part of the Dow Jones?",
    "What is today's Dow Jones price?",
    "Compare Dow Jones and Nasdaq.",
    "Why did the Dow fall today?",
    "What is CPI?",
    "Tell me about the 2008 financial crisis."
]

if __name__ == "__main__":

    for question in questions:

        result = intent_detector.detect(question)

        print("=" * 70)
        print("Question:", question)
        print("Intent:", result.intent.value)
        print("Confidence:", result.confidence)