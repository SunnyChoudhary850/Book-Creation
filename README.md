# eBook Chapter and Content Generator

This Python script uses the power of AI to help you generate the structure and content for your eBook. It's perfect for writers, educators, and anyone who wants to create an eBook but needs a little help getting started.

## Features

- **Chapter Generation**: Just provide the title of your book, and the script will generate a list of chapters and subheadings in JSON format.
- **Content Generation**: For each chapter and subheading, the script can generate a detailed and elaborate text content.
- **Customizable**: You can easily modify the script to generate content that fits your specific needs.
- **AI-Powered**: The script uses the Gemini API, a powerful AI model for generating human-like text.

![Screenshot (85)](https://github.com/Abhay-404/Create-Book-using-Gemini_Ai/assets/114435001/dd401196-526f-4110-8775-a12297357e5e)

## How to Use

1. **Install the Dependencies**: This script requires the `google.generativeai` and `ast` Python libraries. You can install these with pip:

    ```bash
    pip install google-generativeai ast
    ```

2. **Set Up Your API Key**: You'll need to replace the placeholder text in the `genai.configure(api_key="")` line with your actual Gemini API key.

3. **Run the Script**: You can run the script in your Python environment. When prompted, enter the title of your eBook.

    ```bash
    python main.py
    ```

4. **Review the Generated Chapters**: The script will generate a list of chapters and subheadings for your eBook. If you're not satisfied with the generated chapters, you can choose to recreate them.

5. **Generate Content**: For each chapter and subheading, the script will generate detailed and elaborate text content.

6. **Check the Output**: The generated chapters and their content will be saved in a JSON file named `chapters.json`.


## Inspiration

The inspiration for this project came from a YouTube video that demonstrated the power of AI in content generation. The video showcased how AI can be used to automate and simplify the process of content creation, sparking the idea for this eBook chapter and content generator. This project is a testament to the potential of AI in transforming the way we create and consume content. It's an exciting time to be a part of this AI revolution! 🚀

## Contribute

Feel free to fork this project, submit issues, and contribute changes. appreciate your help in making this tool even better!

## Disclaimer

This tool uses AI to generate content, which means the output can vary greatly. Always review and edit the generated content to ensure it meets your needs and expectations.
