FROM python
# это делаем для прямого вывода в консоль
ENV PYTHONUNBUFFERED 1

# создание рабочей директории для нашего бека
WORKDIR /busbot

## копируем все файлы в контейнер  путь к файлам бота
COPY . .

RUN pip install pipenv
RUN pip install aiogram
RUN pip install celery
RUN pip install asyncio
#RUN pip install logging
ENTRYPOINT [ "python", "busb.py" ]
