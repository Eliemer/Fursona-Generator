FROM python:3.7

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 443

WORKDIR ./app/

CMD ["python", "fursonaGenerator.py"]
