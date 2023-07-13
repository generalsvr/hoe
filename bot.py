from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor


bot = Bot(token="6338848779:AAGo323cRKJ9ylR0NG9K_VSULY7xV6f5UaY") # test
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(Command('start'), state="*")
async def start_command(message: types.Message):
    await message.answer("Присылай диалог. Формат:\n\nUser: привет\nGirl: хай\nUser: поебемся?\nGirl: давай", parse_mode="Markdown")


@dp.message_handler(lambda message: message.text, state="*")
async def conversation_handler(message: types.Message):
    # append message to file like {"text": "message"}
    with open("dialog.jsonl", "a") as f:
        # replace new line to \n
        message.text = message.text.replace("\n", "\\n")
        f.write(f'{{"text": "{message.text}"}}\n')

        # send message to user with total count of messages
        await message.answer(f"Диалог записан. Всего сообщений: {len(open('dialog.jsonl').readlines())}")
        
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)