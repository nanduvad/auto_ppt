import asyncio
from agent.agent_ppt import PPTAgent

if __name__ == "__main__":
    user_input = input("Enter topic: ")

    agent = PPTAgent()
    asyncio.run(agent.run(user_input))