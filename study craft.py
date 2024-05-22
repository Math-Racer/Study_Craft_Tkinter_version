# Importing tkinter and messagebox modules
import tkinter as tk
import tkinter.messagebox as mb


from PIL import Image, ImageTk
import os
import ctypes

import openai
client = openai.OpenAI(api_key="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")




"""
icon = ImageTk.PhotoImage(Image.open('icon.png'))
root.iconphoto(True, icon)
"""

def get_output2(topic):
    Response = """
    Given your time frame and commitment level, a structured yet flexible study plan will be most effective in covering the essentials of Web 3.0. We'll focus on covering foundational knowledge, development practices, smart contracts, and decentralized applications (DApps). Here's a 25-day study plan, with an allocation of 4 hours per day:

**Day 1-3: Understanding Blockchain Fundamentals and Web 3.0**

- **Course:** Blockchain Specialization (Coursera by University at Buffalo)
    - Focus on the first course in the specialization: "Blockchain Basics".
    - **Objective:** Understand blockchain technology's basics, its operations, and its role in Web 3.0.

**Day 4-7: Dive into Ethereum and Smart Contracts**

- **Course:** Ethereum and Solidity: The Complete Developer's Guide (Udemy)
    - **Objective:** Get to grips with Ethereum blockchain, smart contracts development using Solidity, and how they are used in Web 3.0 applications.

**Day 8-9: Deep Dive into Solidity**

- **Resource:** Solidity by Example (Official Solidity Documentation)
    - **Objective:** Strengthen your understanding of Solidity by working through practical examples.

**Day 10-12: Learn about Decentralized Applications (DApps)**

- **Course:** DApp University Bootcamp (Free resource on YouTube or the official DApp University website)
    - **Objective:** Understand the architecture, development, and deployment of decentralized applications.

**Day 13-15: Comprehensive Overview of the Web 3.0 Ecosystem**

- **Course:** Introduction to Web 3.0 & Blockchain (edX or similar platforms)
    - **Objective:** Gain insights into various components of Web 3.0, including decentralized finance (DeFi), non-fungible tokens (NFTs), and the decentralized web.

**Day 16-18: Frontend Technologies for Blockchain**

- **Course:** Ethereum Blockchain Developer Bootcamp With Solidity (2023) (Udemy)
    - **Objective:** Learn to connect your smart contracts with a user interface using web3.js or ethers.js libraries.

**Day 19-21: Exploring Additional Blockchains**

- **Self-Led Learning:** 
    - Spend these days exploring technologies beyond Ethereum, such as Polkadot, Cardano, or Solana. Focus on their official documentation and community tutorials.
    - **Objective:** Understand the landscape of blockchain technologies and their unique propositions in the Web 3.0 ecosystem.

**Day 22-24: Building Your Side Project**

- **Action Plan:** Start working on your side project. Utilize what you've learned to plan, design, and begin development. Focus on a specific use case that interests you, such as a decentralized social media platform, a DeFi application, or a gaming DApp.
    - **Objective:** Apply the knowledge you've acquired through practical application. This will solidify your understanding and provide hands-on experience.

**Day 25: Review and Plan Next Steps**

- **Activity:** Spend this day reviewing what you've learned, documenting your progress with your side project, and planning future learning paths. This might include deep dives into specific areas of interest, contributing to open-source Web 3.0 projects, or continuing work on your side project.

**Additional Tips:**

- **Community Engagement:** Join forums, discord channels, or subreddits focused on Web 3.0 development. Engaging with a community can provide valuable insights, feedback, and motivation.
- **Build in Public:** Consider documenting your learning journey and side project development on social media or a blog. It can lead to valuable connections and feedback.
- **Adjust as Needed:** The field of Web 3.0 is vast and rapidly evolving. Be flexible in your studies and willing to dive deeper into topics that particularly interest you or are relevant to your side project.

This study plan provides a comprehensive approach to learning Web 3.0 technologies and principles. Remember, the key to success is consistency and a willingness to learn and adapt. Good luck with your project!"""
    return Response

def get_output1(topic):
    # Set the prompt to be prefixed to the user prompt
    tuning = """I am a 2nd year college student majouring in Computer Engineering. Your task is to act as an learning coach
and create a list of textbooks and research papers I need to go through in order to gain deeper understaning of the subject: """
    prompt = topic
    prompt +=  tuning
    stream = client.chat.completions.create(
    # model="gpt-4",
    model="gpt-4-0125-preview",
    messages=[{"role": "user", "content": prompt}],
    stream=True,)
    Response = ""
    for chunk in stream:
        Response += (chunk.choices[0].delta.content or "")
    return Response


def get_input():
  topic = entry.get()  # Get the user input from the text box
  answer = get_output1(topic)
  answer_text.delete(1.0, tk.END)  # Clear any existing text
  answer_text.insert(tk.END, answer)


# Creating a root window
root = tk.Tk()
root.title("Study Craft")
root.geometry("800x500")
root.resizable(0, 0)

# Create the text box label
label = tk.Label(root, text="Enter the topic you want to learn")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the text box for user input
entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Create the button to generate the essay
generate_button = tk.Button(root, text="Let's Go!", font=("Arial", 12, "bold"), fg="green", bg="lightgray", padx=15, pady=5, command=get_input)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the text box to display the response
answer_text = tk.Text(root, height=15, width=80, wrap=tk.WORD, font=("Arial", 12), relief="groove", borderwidth=3)
answer_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10) 
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=answer_text.yview)
scrollbar.grid(row=3, column=2, sticky="ns")
answer_text.config(yscrollcommand=scrollbar.set)

# Run the main loop
root.mainloop()




