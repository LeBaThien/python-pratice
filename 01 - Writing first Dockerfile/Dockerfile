


FROM python:3.9-slim
WORKDIR /app/

COPY requirement.txt .
RUN pip install -r requirements.txt

COPY echo.py .
CMD ["python", "echo.py"]