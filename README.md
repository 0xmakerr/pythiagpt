# pythgpt
This project allows you to train GPT-3/4 on custom data using LlamaIndex and have a Q/A like conversation with it using discord as it's interface. Specifically this repo is trained on Pyth Network documentation, GitHub repos, blog articles and the Pyth whitepaper.

## Setup

1. Setup your .env variables. In `main.py` you will need `DISCORD_API_KEY` (https://discord.com/developers/applications), in `pythgpt.py` add `OPENAI_API_KEY` and for importing repos from GitHub also add `GITHUB_API_KEY`.
2. Import your custom data into the `data` folder and change `owner` `repos` `branch` variables inside `build_index()` function to your desired GitHub repos.
3. Edit the `base_prompt` variable with your own desired ChatGPT system prompt.
4. Open `pythgpt.py` and run the `build_index()` function to build index over the custom data provided in Step 2. This will create new index files in the `storage` folder.
5. After creating your discord bot in Step 1, invite it to your desired discord server and run `main.py`
6. Have fun!

## Example Conversations

![chat](https://github.com/0xmakerr/pythgpt/assets/25880864/361e002c-c704-4598-8487-56af028b7555)
![chat2](https://github.com/0xmakerr/pythgpt/assets/25880864/c53298be-e709-44f3-9ebc-ab42de96baca)
