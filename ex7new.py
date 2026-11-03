
import re

print("Welcome to AI Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower().strip()

    if re.search(r"\b(hi|hello|hey|hii|hiii)\b", user):
        print("Bot: Hello! How can I help you?")

    elif re.search(r"\bhow are you( doing)?\b", user):
        print("Bot: I am fine. Thank you! How are you?")

    elif re.search(r"\b(what is your name|who are you)\b", user):
        print("Bot: My name is AI Chatbot.")

    elif re.search(r"\b(what is ai|define ai|what is artificial intelligence)\b", user):
        print("Bot: AI means Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.")

    elif re.search(r"\b(what is machine learning|define machine learning)\b", user):
        print("Bot: Machine Learning is a branch of AI where computers learn patterns from data.")

    elif re.search(r"\b(what is deep learning|define deep learning)\b", user):
        print("Bot: Deep Learning uses multi-layered neural networks to learn complex patterns.")

    elif re.search(r"\b(what is python|define python)\b", user):
        print("Bot: Python is a high-level, general-purpose programming language.")

    elif re.search(r"\b(what is java|define java)\b", user):
        print("Bot: Java is an object-oriented programming language that runs on the JVM.")

    elif re.search(r"\b(what is dsa|define dsa|data structures and algorithms)\b", user):
        print("Bot: DSA stands for Data Structures and Algorithms. It helps organize data and solve problems efficiently.")

    elif re.search(r"\b(what is a stack|define stack)\b", user):
        print("Bot: Stack is a LIFO data structure. Last In, First Out.")

    elif re.search(r"\b(what is a queue|define queue)\b", user):
        print("Bot: Queue is a FIFO data structure. First In, First Out.")

    elif re.search(r"\b(what is bfs|define bfs|breadth first search)\b", user):
        print("Bot: BFS explores nodes level by level using a queue.")

    elif re.search(r"\b(what is dfs|define dfs|depth first search)\b", user):
        print("Bot: DFS explores deeply before backtracking. It uses recursion or a stack.")

    elif re.search(r"\b(what is an algorithm|define algorithm)\b", user):
        print("Bot: An algorithm is a finite sequence of steps to solve a problem.")

    elif re.search(r"\b(what is a computer|define computer)\b", user):
        print("Bot: A computer is an electronic device that processes data.")

    elif re.search(r"\b(what is the internet|define internet)\b", user):
        print("Bot: The Internet is a global network of interconnected computers.")

    elif re.search(r"\b(what can you do|help|your purpose)\b", user):
        print("Bot: I can answer simple questions about AI, Python, Java, DSA, and general topics.")

    elif re.search(r"\b(thanks|thank you|thx)\b", user):
        print("Bot: You're welcome!")

    elif re.search(r"good morning| wish| meet| early time", user):
        print("Bot: Good morning! Have a great day.")

    elif re.search("good|morning|afternoon|evening", user):
        print("Bot: Good afternoon! How can I help you?")

    elif ("143"==user):
        print("Boto: Good evening my friend!")

    elif re.search(r"\bgood night\b", user):
        print("Bot: Good night! Take care.")

    elif re.search(r"\bhow old are you\b", user):
        print("Bot: I am an AI chatbot, so I don't have a human age.")

    elif re.search(r"\b(who created you|who made you)\b", user):
        print("Bot: I was created using Python and regular expressions.")

    elif re.search(r"\b(what is your favorite color|what is your favourite color)\b", user):
        print("Bot: I don't have personal preferences, but blue is a nice color!")

    elif re.search(r"\b(what time is it|current time)\b", user):
        print("Bot: I cannot check the current time in this simple version.")

    elif re.search(r"\b(bye|goodbye|see you|exit|quit)\b", user):
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand. Try asking something else.")
