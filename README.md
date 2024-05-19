README.md 

在terminal (執行)
```
> git init
```

在**VS Code**執行 `commit` 與 `publish branch`

在terminal (執行)
```
> virtualenv env -p python
> source ./env/script/activate
```


(建立修改) .gitignore 

requirements.txt
> ```
> openai
> langchain
> streamlit
> python-dotenv
> PyPDF2
>
> -e .
> ```

`-e .' : In that case it will search all the local package into your current directory/folder.
And it will download or it will install it inside your virtual environment and it will execute the setup.py in back.


setup.py

src
> mcqgenerator
> > **init**.py
> > 
> **init**.py

experiment
> mcq.ipynb
