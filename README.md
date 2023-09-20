# Телеграмм Бот для студентов ТУИТ
## Расписание уроков
----
HEAD -- это голова.  
Коммит -- 
```bash
git init
git add .
git commit -m 'message'
git push
```
Статусы файлов:  

```mermaid
graph LR;
  untracked -- "git add" --> staged --> B;
  staged --> C;
  staged    -- "???"     --> tracked/comitted --> B;

%% стрелка без текста для примера: 
  A --> B;
  C --> A;
  C --> tracked/comitted;
``` 
```bash
pip install aiogram==2.25.1
```
```python
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
```
