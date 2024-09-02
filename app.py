import json
import google.generativeai as genai
import ast
genai.configure(api_key="")  # Replace with your gemini API key
AUTO_PILOT = True
generation_config = {
  "temperature": 0.65,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def Chapter_maker(title):
    prompt = (
        f"You are a creative eBook writer tasked with outlining the chapters for a book titled '{title}'. "
        "Please generate at least 5 chapter titles, each with a brief summary. "
        "Ensure that the output is a valid JSON object with the chapter titles as keys and the summaries as values. "
        "Only return the JSON object, with no additional text or formatting."
    )

    convo = model.start_chat(history=[
    {
      "role": "user",
      "parts": ["\"role\": \"system\", \"content\": \"You are a creative eBook writer. Give the output as JSON.\n\n\"role\": \"user\", \"content\": f\"Write the chapters and subheadings for the ebook titled '{title}'. Make the chapter names as keys and the list of subheadings as values. Give at least 5 chapters and 2 subheadings for each chapters.\""]
    },
    {
      "role": "model",
      "parts": ["```JSON\n{\n  \"title\": \"The Art of Creative Writing\",\n  \"chapters\": {\n    \"Chapter 1: The Basics of Creative Writing\": [\n      \"Choosing a Topic\",\n      \"Developing Characters\"\n    ],\n    \"Chapter 2: Crafting a Plot\": [\n      \"Creating a Story Arc\",\n      \"Adding Conflict and Tension\"\n    ],\n    \"Chapter 3: Setting the Scene\": [\n      \"Creating a Vivid Setting\",\n      \"Using Sensory Details\"\n    ],\n    \"Chapter 4: Writing Dialogue\": [\n      \"Creating Believable Dialogue\",\n      \"Using Dialogue to Advance the Plot\"\n    ],\n    \"Chapter 5: Revising and Editing\": [\n      \"Getting Feedback from Others\",\n      \"Polishing Your Writing\"\n    ]\n  }\n}\n```"]
    },
  ])


    convo.send_message(prompt)

    # Display raw response for debugging
    raw_response = convo.last.text.strip()
    print("Raw Response:", raw_response)

    # Attempt to strip out any non-JSON text or formatting
    try:
        start_index = raw_response.find('{')
        end_index = raw_response.rfind('}') + 1
        cleaned_response = raw_response[start_index:end_index]

        # Parse the JSON
        chapters_dict = json.loads(cleaned_response)

        with open("chapters.json", "w") as chapters_file:
            json.dump(chapters_dict, chapters_file)

    except json.JSONDecodeError:
        print("Failed to decode JSON response. Please check the API response format.")
        return None


Chapter_maker("the story behind calculs")

def create_chapter_content(ebook_title, chapter, subheading):

  convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["\"role\": \"system\", \"content\": f\"You are a creative eBook writer. The title of the eBook you are writing is '{ebook_title}'. Each chapter of the eBook has subheadings.\"\n\"role\": \"user\", \"content\": f\"Write the text content for the subheading titled '{subheading}' under the chapter titled '{chapter}'. Be elaborate and clear. Include the chapter name and subheading in the response dont forget the previous chapter use thsat to make continious story .\""]
  },
  {
    "role": "model",
    "parts": ["Chapter: '{chapter}'\n\nSubheading: '{subheading}'\n\nText Content:\n\nDiscuss the concepts and components of content marketing in the digital age, emphasizing the shift from traditional advertising to engaging and valuable conten..."]
  },
])
  
  convo.send_message(f"The title is {ebook_title} , chapter is {chapter} and subheading is {subheading}")
  print(convo.last.text)
  return convo.last.text



def main():
    title = input("Please Provide the title of the book 😃 : ")
    satisfied = False
    while not satisfied:
        Chapter_maker(title)
        satisfied = "y" == input("Are you satisfied with the created chapters? Press y for Yes or any other key to recreate ").lower()
    
    
    chapters = None
    with open("chapters.json") as chapters_file:
        chapters = json.load(chapters_file)
    
    for chapter, subheadings in chapters.items():
        for subheading in subheadings:
            recreate = True
            while recreate:
                contents = create_chapter_content(title, chapter, subheading)
                
                recreate = not AUTO_PILOT and ("r" == input("Press r to recreate the content if you are not satisfied. Press any other key to proceed to the next subheading ").lower())
                
                if not recreate:
                    with open(f"{title}.txt", "a") as ebook_file:
                        ebook_file.write(contents + "\n\n")
    
    print("*"*50)
    print(f"Completed generating the eBook '{title}'")
                    
        
if __name__ == "__main__":
    main()
