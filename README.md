# AI Chatbot with Multiple Models

A powerful, customizable chatbot application built with Streamlit and OpenRouter API integration that allows access to various AI models with different personas.

## Features

- **Multiple AI Models**: Access various AI models through OpenRouter including Deepseek, Google Gemma, and Qwerky
- **Different Personas**: Interact with the chatbot in different roles like assistant, developer, data scientist, teacher, or doctor
- **Chat History**: Maintain conversation history until manually cleared
- **Streaming Responses**: See AI responses being generated in real-time
- **Custom Background**: Supports custom background images for a personalized experience

## Setup Instructions

### Prerequisites
- Python 3.7+
- Streamlit
- OpenRouter API Key

### Installation

1. Clone this repository or download the source code
2. Install the required packages:
   ```
   pip install streamlit openai
   ```

3. Create a `.streamlit/secrets.toml` file in the project directory with your OpenRouter API key:
   ```
   OPENAI_API_KEY = "your_openrouter_api_key_here"
   ```

4. Run the application:
   ```
   streamlit run app.py
   ```

### Adding a Background Image

To use a background image:
1. Place your image file in the project directory
2. Add this line after the imports in app.py:
   ```python
   add_bg_from_local("your_image_filename.jpg")
   ```

## File Structure

- `app.py`: Main application file containing the Streamlit UI and OpenRouter API integration
- `.streamlit/secrets.toml`: Configuration file containing API keys (not committed to version control)

## Usage

1. Select an AI model from the dropdown menu in the sidebar
2. Choose a persona for the chatbot
3. Type your message in the chat input box
4. View the chatbot's response in real-time
5. Clear conversation history using the "Clear Conversation" button when needed

## Customization

- **Adding New Models**: Update the `models` list in app.py
- **Adding New Personas**: Add new entries to the `jobs_dict` dictionary
- **Modifying Appearance**: Edit the CSS styles in the application

## Troubleshooting

- If you receive API errors, check your OpenRouter API key and ensure you have sufficient credits
- For UI issues, make sure you have the latest version of Streamlit installed
- If the background image doesn't display, verify the file path is correct

## License

This project is open source and available for personal and commercial use.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the web application framework
- [OpenRouter](https://openrouter.ai/) for providing access to multiple AI models
