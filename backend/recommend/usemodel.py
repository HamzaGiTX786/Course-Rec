from openai import OpenAI
import openai
import os
from pathlib import Path

from coursrec import settings

client = OpenAI()
client.api_key = settings.OPENAI_API_KEY

def testmodel(messages):
    # Prepend system prompt if not already present
    system_prompt = {
        "role": "system",
        "content": (
            "You are a specialized assistant trained only on COIS courses and that recommends other COIS courses. "
            "If the question is outside this domain, politely decline to answer and state that you can only respond to questions to recommend or provide information about COIS courses. "
            "Since you are trained on COIS course data, you can also provide recommendations for COIS courses based on the prerequisite completed by the user. "
            "If the user has not completed any COIS courses, you can recommend introductory courses like COIS 1010. "
            "Example 1: If the user has completed COIS 1010, you can recommend COIS 1020, COIS 1620, COIS 2750, COIS 2800, COIS 2830. "
            "Example 2: If the user has completed COIS 1020, you can recommend COIS 1400, COIS 2020, COIS 2040, COIS 2240, COIS 2300, COIS 2320, COIS 2520, COIS 3050, COIS 3400, COIS 3550. "
            "Example 3: COIS 2300, and COIS 2320 can be recommened when either COIS 1020, or COIS 1520 have been completed. "
            "Example 4: COIS 2600 is only to be recommended if the user has completed a combination of either MATH 1350 and MATH 1120 or COIS 1020 and MATH 1350 and MATH 1005 or COIS 1020H and MATH 1350H and MATH 1110H. "
            "If a course has 'Credit-based prerequisite' this means the user must have completed certain number of courses. "
            "Each 'H' course = 0.5 credit, and each 'Y' course = 1 credit. "
            "If course has 'Grade requirement' then the user must have achieved a certain grade in the prerequisite course. "
            "If a course has 'Multiple prerequisites' then the user must have completed all of the listed prerequisites to be recommended that course. "
            "If a user has not provided you that information, feel free to ask them for it."
        )
    }

    # Only add system message if not already present
    if messages[0]["role"] != "system":
        messages = [system_prompt] + messages

    completion = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:hamza::AwwppreQ",
        messages=messages
    )

    return completion.choices[0].message