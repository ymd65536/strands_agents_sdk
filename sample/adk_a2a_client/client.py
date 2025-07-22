import asyncio
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.sessions.in_memory_session_service import InMemorySessionService
# from google.adk.events.event import Event
# from google.genai import types as genai_types

async def main():
    # Create A2A Agent
    sample_agent = RemoteA2aAgent(
        name='sample_agent',
        description='a2a sample agent',
        agent_card='http://localhost:9000'
    )

    session_service = InMemorySessionService()
    session = await session_service.create_session(user_id='user_123', app_name='test')

    ctx = InvocationContext(  
        session=session,  
        session_service=session_service,  
        agent=sample_agent,  
        invocation_id="inv123",  
        branch="main"  
    )  
      
    try:  
        async for event in sample_agent._run_async_impl(ctx):  
            print(f"Response from remote agent: {event.content}")  
            if event.error_message:  
                print(f"Error: {event.error_message}")  
    except Exception as e:  
        print(f"Failed to communicate with remote agent: {e}")  
      
    # 6. リソースをクリーンアップ  
    await sample_agent.cleanup()  
  
if __name__ == "__main__":  
    asyncio.run(main())
