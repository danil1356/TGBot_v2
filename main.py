import telebot;
from multiprocessing import Pipe, Process

from PyPDF2 import PdfFileReader
from deeppavlov.core.common.file import read_json
from telebot import types
from deeppavlov import build_model, train_model,configs
from pdfminer.high_level import extract_text

"""
чтение страницы
with open('nabokov_bledny_ogon_ardis_1983__ocr.pdf', 'rb') as f:
    pdf = PdfFileReader(f)
    page = pdf.getPage(104)
    textPdf = page.extractText()
    #print(textPdf)

"""

bot = telebot.TeleBot('5727073564:AAFrGtRuqYwxrgN0Tj5SVv6_DQU5WZ2nvn4');
#file = open('text.txt','r', encoding="utf-8")
#model_config = read_json('intent_catcher.json')
#model = build_model(model_config)
#model_config = read_json('intent_catcher.json')
#model = train_model(model_config, download=False)
#print("Конец")


@bot.message_handler(content_types=['text']) #слушатель
def answer_text(message):
    #model = build_model(model_config)
    #answer = model([context], [message.text])
    b.send(message.text)
    intent = b.recv()[0]

    print(intent)
    if intent == 'questions':
        bot.send_message(message.from_user.id, intent)
        #bot.register_next_step_handler(message, сontextQuestionAnswering)


    elif intent == 'page':
        bot.send_message(message.from_user.id, intent)
        #bot.register_next_step_handler(message, page)


    #bot.send_message(message.from_user.id, model([context], [message.text]))

#ответ на вопрос
def сontextQuestionAnswering(message):
    answer = model2([context], [message.text])
    if answer[0][0] == '':
        bot.send_message(message.from_user.id, 'ответа в тексте не найдено')
    else:
        bot.send_message(message.from_user.id, model2([context], [message.text]))

#открытие страницы
def page(page):
    with open('nabokov_bledny_ogon_ardis_1983__ocr.pdf', 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(page)
        textPdf = page.extractText()
        print(textPdf)
        ########?
        context = textPdf;

#процесс для 2-й модели
def startModel(connection):
    model_config = read_json('intent_catcher.json')
    model = build_model(model_config)
    while True:
        item = connection.recv()
        item = model([item])
        print(item)
        connection.send(item)


if __name__ == "__main__": #точка входа
    ###чтение страницы
    with open('nabokov_bledny_ogon_ardis_1983__ocr.pdf', 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(1)
        textPdf = page.extractText()
        print(textPdf)
    ###
    context = textPdf;

    model_config2 = read_json('squad_ru_bert_infer.json')
    model2 = build_model(model_config2, download=True)

    a, b = Pipe()
    process = Process(target=startModel, args=(a,))
    process.start()

    bot.polling(none_stop=True, interval= 0)