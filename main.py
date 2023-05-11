import openai
import pandas as pd
import tiktoken
from openai.error import InvalidRequestError
from tenacity import retry, stop_after_attempt, wait_random_exponential


def num_tokens_from_string(string: str) -> int:
    try:
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

        num_tokens = len(encoding.encode(string))

        return num_tokens

    except Exception as e:
        raise e


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def classify(chat: str) -> str:
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=[
                {
                    "role": "system",
                    "content": "You are chat analyst, perform conversation classifaction into one of the following categories: tech, non-tech. If the converstation consists of both tech and non tech return mixed as the answer .Return the output in one word",
                },
                {"role": "user", "content": f"{str(chat)}"},
            ],
        )

        print(f'Response {res["choices"][0]["message"]["content"]}')

        return res["choices"][0]["message"]["content"]

    except InvalidRequestError:
        print("Token exceeded")

    except Exception as e:
        raise e


def generate_num_tokens(dataframe: pd.DataFrame):
    try:
        dataframe["NumTokens"] = [
            num_tokens_from_string(str(i)) for i in dataframe["Conversations"]
        ]

        dataframe.to_csv("test.csv", index=False, header=True)

    except Exception as e:
        raise e
