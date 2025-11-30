'''
A quick start example demonstrating the use of openAI agents sdk. Defines an agent that provides
an interesting historical fact everytime it is run
'''
from dotenv import load_dotenv
import os
from agents import Agent, trace, Runner
import asyncio

# Load the environment variables from .env file
def load_envrionment():
    load_dotenv(override=True)

# Validate existence of OpenAI API key for agent to use
def validate_environment() -> bool:
    # validate that API keys are set 
    if(os.getenv("OPENAI_API_KEY")):
        print(f"OpenAI API key is set - starts with {os.getenv("OPENAI_API_KEY")[:8]}\n")
    else:
        print(f"OpenAI API key missing...\n")
        return False

    return True

# Creates and returns an egent
def create_agent() -> Agent:
    return Agent(
        name="History Facts",
        model="gpt-4o-mini",
        instructions="You are an expert historian"
    )

# Runs an agent using Runner package and returns the final_output string
async def run_agent(agent: Agent) -> str:
    with trace("Share a historical fact"):
        output = await Runner.run(agent, "Share an interesting historical fact")
        return output.final_output

# main function that kicks off the runner
async def main():
    load_envrionment()
    valid = validate_environment()
    if(valid):
        agent = create_agent()
        output = await run_agent(agent)
        print (output)
        

if __name__ == "__main__":
    asyncio.run(main())