import os
import dotenv

dotenv.load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")

# function to test api call to open ai model
def test_open_ai_api():
    from langchain.chat_models import ChatOpenAI
    from langchain.schema import HumanMessage

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    response = chat.predict_messages(
        [HumanMessage(content="Say hello world in a creative way.")]
    )

    print(response.content)
    
if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = OPEN_AI_API_KEY
    test_open_ai_api()





