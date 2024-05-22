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

--`Change kernel for 'environment\mcq.ipynb'` 選擇 `env\Scripts\python.exe`

--`Commit` : structure updated

--完成修改 setup.py

--`pip install -r requirements.txt`

產生 `mcqgenerator.egg-info`

* 建立 .env
> ```
> OPENAI_API_KEY='屬於自己的OPENAI KEY'
> ````

--若需要，在 terminal 執行 `python -m pip install ipykernel -U --force-reinstall`


--

## Lecture 7

* src
> mcqgenerator
> > logger.py
> > 
> > MCQGenerator.py
> > 
> > utils.py

Response.json

StreamlitApp.py

test.py
