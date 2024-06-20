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
> > conda create -p env python=3.8 -y
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
> 所有必要的 packages 都 import 完後，先在 terminal 執行 `>python StreamlitAPP.py` 測試
> > 若有錯誤，可試著在 terminal 執行 `>python setup.py install`
> > 或是將 `from src.mcqgenerator.MCQGenerator import generate_evaluate_chain` 先隱藏
> 
> 在 loading json file 這一行 要注意 Response.json 的路徑是否正確
> > 在 local (本機VSCode) : `with open('E:\gitstore\mcqgen\Response.json','r') as file:`
> > 
> > 在 cloud (github.dev): `with open('/workspaces/mcqgen/Response.json','r') as file:`

--開起 StreamlitAPP
> `> streamlit run StreamlitAPP.py`
>
> 如需要修改 port (default:8501), 舉例改成 8080
> > `> streamlit run StreamlitAPP.py --server.port 8080`
>
> 接著就可以用 browser 開啟 project APP

---

## Lecture 8

* 測試 Lecture 6 & 7 完成的 project
> google "aritficial intelligence"，點選 wiki  所提供頁面
>
> 選擇 **Goals** 前一個 section 的內容，轉存為 `AIDOC.txt`
>
>  用 `streamlit run StreamlitAPP.py` 啟動後，開啟 browser
>
> 在 **Browse files** 選取 `AIDOC.txt`，在 **No. of MCQs** 輸入 `5` ，**Insert Subject** 輸入 `artificial intelligence`，**Complexity of Level of Questions** 輸入 `Simple`

* 進入今天主題AWS

1. first login to the AWS: https://aws.amazon.com/console/

2. search about the EC2

3. you need to config the UBUNTU Machine

4. launch the instance

5. update the machine:

```python
>sudo apt update

>sudo apt-get update

>sudo apt upgrade -y

>sudo apt install git curl unzip tar make sudo vim wget -y

>git clone "Your-repository"

>sudo apt install python3-pip

>pip3 install -r requirements.txt

>python3 -m streamlit run StreamlitAPP.py
```

##### if you want to add openai api key

1. create .env file in your server
touch .env

vi .env
#press insert
#copy your api key and paste it there
#press and then :wq and hit enter

go with security and add the inbound rule
add the port 8501
