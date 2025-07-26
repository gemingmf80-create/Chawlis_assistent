memory_store = {}

def remember(question, answer):
    memory_store[question] = answer

def recall(question):
    return memory_store.get(question)