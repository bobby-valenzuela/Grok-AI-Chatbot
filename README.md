# XAI-Grok-Chatbot


# Setup
1. Create a .env file with your XAI api key
Example: `XAI_API_KEY=<my_api_key>`

2. Setup virtual environment
```bash
$ virtualenv env && source env/bin/activate
```

3. Install dependencies
```bash
$ pip3 install -r requirements.txt
```


# Usage
The "personality" parameter is optional, but can be used to give  your chatbot character.
```bash
$ python3 app.py --personality "Rude and sarcastic"
```
  
![Alt text](./demo-001.gif?raw=true "Demo 1")
