from openai import OpenAI

keyFile = open("APIKey.txt", "r")
theKey = keyFile.readline()
keyFile.close()

client = OpenAI(
    api_key = theKey
)

def singleRequest(userContent):
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages = [{"role" : "system", "content" : "You are the an email writer. Follow the user instructions."}, {"role" : "user", "content" : userContent}]
    )

    return response.choices[0].message.content
