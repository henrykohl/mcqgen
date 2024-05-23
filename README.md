# **Foundational Generative AI** 
([learning page](https://learn.ineuron.ai/course/foundational-generative-ai/656d8f170af8644aac926376))

## Lecture 6

```
> mkdir mgcgen
> cd mgcgen
> code . # 開啟 VS Code
```
在**VS Code**執行 開啟 terminal (執行)
```
> git init
```

* 建立 README.md 

在 **VS Code** 點選 `source control`   執行 `commit` 與 `publish branch`

用 *Git Bash* 模式的 terminal (執行)
> 使用 venv 模式
>```
> > virtualenv env -p python
> > source ./env/Scripts/activate
>```
> 使用 conda 模式
>```
> > conda create -p env python-3.8 -y
> > source activate ./env
>```

* 建立 .gitignore
>```
> > touch .gitignore
>```
> 修改（加入） : `env`  

在 **VS Code** 點選 `source control`   執行 `commit` 與 `Sync changes`

* 建立 requirements.txt
> ```
> openai
> langchain
> streamlit
> python-dotenv
> PyPDF2
> langchain-community # 自加
> langchain-openai # 自加
>
> -e .
> ```

`-e .' : In that case it will search all the local package into your current directory/folder.
And it will download or it will install it inside your virtual environment and it will execute the setup.py in back.


* 建立 setup.py

* 建立 src 資料夾
> mcqgenerator
> > __init__.py
> > 
> __init__.py

* 建立 experiment
> mcq.ipynb

**開始編輯 `mcq.ipynb`**

--`Change kernel for 'environment\mcq.ipynb'` 選擇 `env\Scripts\python.exe`

--`Commit` : structure updated

--完成修改 setup.py

--`pip install -r requirements.txt`

產生 `mcqgenerator.egg-info`

* 建立 .env
> ```
> OPENAI_API_KEY='屬於自己的OPENAI KEY'
> ```

--若需要，在 terminal 執行 `python -m pip install ipykernel -U --force-reinstall`

--修改 .gitignore
> 新加 ```.env```

--`Commit` : file updated

* 建立 data.txt

 --`Commit` : all files updated (mcq.ipynb, machinelearning.csv, data.txt 等，三個檔案 ) 
 
---

## Lecture 7

* src
> mcqgenerator (建立三個檔案)
> 
> > logger.py
> > 
> > MCQGenerator.py
> > 
> > utils.py

* 建立 Response.json

* 建立 StreamlitApp.py

--`Commit` : updated the folder structure 

--編輯 `logger.py`

* 建立且編輯 `test.py`

--確認 terminal 在 Git bash 且 切換到 (env) 環境

--用 `python test.py` 測試

--`Commit` : I created a logger 

--編輯 `MCQGenerator.py`

--編輯 `utils.py`

--編輯 `Response.json`

--編輯 `StreamlitAPP.py`
