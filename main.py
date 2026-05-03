def analyze_messages(messages):
    """
    Simulated AI processing function for demo purposes.
    """

    return """【AI Opportunity Digest】

1. Opportunity Name: Astra Fellowship
Type: Fellowship
Deadline: This Sunday
Why it matters: Strong AI safety entry point
Summary: Constellation flagship fellowship

2. Opportunity Name: Anthropic Hiring
Type: Job
Deadline: Not specified
Why it matters: Leading AI safety company
Summary: Hiring across roles
"""


if __name__ == "__main__":
    sample_messages = [
        "Astra fellowship closes this Sunday!",
        "Anthropic is hiring"
    ]

    result = analyze_messages(sample_messages)
    print(result)
