# testops-github-demo

Мини-проект на pytest для проверки тест-кейса
**#240287 "End user can configure and use bi-directional GH integration"**.

Содержит 6 тестов (5 проходят, 1 специально падает — `test_intentionally_failing`)
для проверки rerun отдельных тестов из Allure TestOps.

## Что нужно сделать перед прогоном

1. **Создать API токен в TestOps**
   Аватар → API Tokens → + Token → скопировать значение.

2. **Добавить секреты в этот репозиторий**
   Settings → Secrets and variables → Actions → New repository secret:
   - `ALLURE_TOKEN` — токен из шага 1
   - `ALLURE_ENDPOINT` — например `https://qameta.testops.cloud`
   - `ALLURE_PROJECT_ID` — числовой ID проекта в TestOps

3. **Запустить workflow вручную**
   Actions → "GitHub integration with TestOps" → Run workflow.
   В логе последнего шага появится ссылка на launch в TestOps —
   открой её, убедись что результаты пришли, и закрой launch.
   Это автоматически создаст автотест-кейсы и GitHub-backed job.

4. **Настроить триггер и rerun из TestOps** (как администратор)
   Administration → Integrations → + Add integration → GitHub
   (Endpoint: `https://github.com`, API endpoint: `https://api.github.com`).
   Затем в проекте: Settings → Integrations → добавить GitHub с personal
   access token (права `Actions: Read and write`).
   В Jobs → созданная задача → Configure → выбрать Build server → включить
   "Job can be used to run tests" → Submit → обязательно нажать
   **"Update job from the build server"**.

Дальше можно триггерить job, делать rerun всего job run и rerun отдельных
тестов прямо из интерфейса TestOps.

## Локальный запуск

```bash
pip install -r requirements.txt
pytest
```

Результаты появятся в папке `allure-results/`.
