FROM registry.cn-hangzhou.aliyuncs.com/lkiarest/django:pydev

ARG SETTING_FILE

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt 

COPY . .

RUN mv pycart/${SETTING_FILE} pycart/settings.py

EXPOSE 8080

CMD ["sh", "-c", "/usr/src/app/bootstrap.sh"]
