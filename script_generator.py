from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger
from lyzr import Generator

# Initialize the content generator
def script_generator(API_KEY, user_input, preference=None):
    generator = Generator(api_key=API_KEY)
    if preference != '':
        script = generator.generate(text=user_input,instructions=f'Instagram Reel script for 60 seconds video, having the timestamp and visuals for each scence. You can Use this preference: "{preference}"')
    else:
        script = generator.generate(text=user_input,instructions=f'Instagram Reel script for 60 seconds video, having the timestamp and visuals for each scence')
    return script


def open_ai_model_text(API_KEY):
    openAI = OpenAIModel(
    api_key= API_KEY,
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.5,
        "max_tokens": 1500,
                },
            )
 
    return openAI


# Function will fine tune the generated script
def content_creator(script, API_KEY):
    openAI = OpenAIModel(
    api_key= API_KEY,
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.5,
        "max_tokens": 1500,
                },
            )

    
    expert_conent_creator = Agent(
        prompt_persona="""You are a content creator with a knack for crafting engaging Instagram Reels that span various genres and themes. With a keen eye for trends and a creative flair, you effortlessly blends storytelling, humor, and authenticity to captivate audiences and leave a lasting impression""",
        role="Expert Content Creator", 
    )

    script_tunner =  Task(
        name="Script Tunner",
        agent=expert_conent_creator,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=openAI,
        instructions=f"Use the description provided, fine tune the instgram reel script for making it more engaging and attractive various audiences, [!Important] Script duration will be 60 seconds, Include timestamp sections & visuals for each scence, and avoid the intro text of response ",
        log_output=True,
        enhance_prompt=False,
        default_input=script
    )


    logger = Logger()
    

    final_script = LinearSyncPipeline(
        logger=logger,
        name="Content Creator",
        completion_message="App Generated all things!",
        tasks=[
            script_tunner,
        ],
    ).run()

    return final_script