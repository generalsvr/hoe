import openai
openai.api_key = "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"

INSTR = """Generate 5 jsonl examples of boy and girl conversation in russain. Write lowercase. Be creative. Write long conversations. Use emojis. No mistakes in russian! Example:

{"text": "Парень: что-то готовишь вечером?\sДевочка: да, делаю греческий салат, потому что ты так любишь его\sПарень: о, здорово! как жаль, что я не могу попробовать...\sДевочка: аххахах, отправлю рецепт, и ты сможешь наслаждаться им там\sПарень: звучит заманчиво спасибо, зай"}
{"text": "Парень: котик, посмотри, что я нашел сегодня на рынке 💍\sДевочка: оу, это обручальное кольцо? 😱\sПарень: да, это не предложение, просто подумал, что тебе понравится 😅\sДевочка: оно красивое, спасибо. но не пугай меня так больше 😣\sПарень: извини, красотка, не хотел 😘\sДевочка: ладно, прощаю тебя этот раз 😝"}
{"text": "Парень: слушай, а ты как считаешь, встречи на расстоянии могут работать? \sДевочка: странный вопрос... ну, если люди действительно любят друг друга и готовы ждать, то почему бы и нет. а что так?\sПарень: просто думал об этом. я же не рядом с тобой, и это меня напрягает.\sДевочка: все будет хорошо, зай. особенно, когда мы снова встретимся.\sПарень: жду этого момента.\sДевочка: и я чтоб ты знал"}

Begin now:"""

for i in range(5):
    print("Iteration: ", i)
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": INSTR}])
    # write the chat completion to a file
    with open("chat_completion.txt", "a") as f:
        f.write(chat_completion.choices[0].message.content + "\n")