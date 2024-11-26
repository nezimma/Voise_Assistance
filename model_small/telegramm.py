import g4f
out = ''
question = input()
while question != ".":

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True,
    )

    for message in response:
        out += message
    out = out.replace("*", '')
    out = out.replace('#', '')
    print(out)
    question = input()

