FROM python:3.7

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py

COPY . .

EXPOSE 443

WORKDIR ./app/

CMD ["python", "fursonaGenerator.py"]
