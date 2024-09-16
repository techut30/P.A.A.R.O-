# PAARO - Partially Active A.I. Reeks Originality

**PAARO** is a Python-based virtual assistant that responds to voice commands and can perform various tasks such as web scraping, downloading Instagram profile data, detecting mood, and playing music from YouTube. The assistant can also retrieve metadata from images and tell you the current time.

## Features

- **Speech Recognition**: Listens to voice commands and recognizes them using Google's Speech Recognition API.
- **Speech Response**: Provides responses through both text and speech.
- **Time Telling**: PAARO can tell the current time.
- **Web Scraping**: Uses Google Search to retrieve relevant links based on a given query.
- **YouTube Playback**: Plays songs or videos on YouTube based on voice requests.
- **Instagram Profile Data**: Downloads profile information from Instagram.
- **Image Metadata**: Retrieves metadata from images.
- **Mood Detection**: Detects the user's mood based on pre-set criteria.

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies:
    ```bash
    pip install SpeechRecognition googlesearch-python pywhatkit
    ```

3. Ensure you have the following libraries installed:
    - `speech_recognition`
    - `datetime`
    - `os`
    - `webbrowser`
    - `ssl`
    - `pywhatkit`
    - `googlesearch-python`
    - Custom modules:
      - `instagram` (used for Instagram data extraction)
      - `metaDataImages` (used for retrieving image metadata)
      - `moodDetection` (used for detecting user mood)

4. Install external dependencies for speech synthesis, such as `say` (available on macOS).

## How to Use

1. **Run the script**:
    ```bash
    python paaro.py
    ```

2. PAARO will greet you based on the current time and listen for your voice commands.

3. You can use the following voice commands to interact with PAARO:
    - **Time**: "What time is it?" 
    - **Web Search**: "Search the internet for {query}" 
    - **Play YouTube**: "Play {song/video name}" 
    - **Instagram Profile**: "Download Instagram profile for {username}"
    - **Image Metadata**: "Retrieve metadata for {image path}" 
    - **Mood Detection**: "Detect my mood"
    - **Exit**: "Goodbye", "Exit"

4. Follow on-screen prompts for typing required input, such as Instagram usernames or image paths.

## Examples

- **Tell the time**:
    ```text
    "What time is it?"
    ```
    PAARO will respond with the current time.

- **Web Search**:
    ```text
    "Search the internet for Python tutorials."
    ```
    PAARO will return the top 5 links for the given query and optionally open them in your browser.

- **Play a song on YouTube**:
    ```text
    "Play Shape of You on YouTube."
    ```
    PAARO will search and play the requested video.

- **Download Instagram Profile**:
    ```text
    "Download Instagram profile for @username."
    ```
    PAARO will download the profile's data.

## Customization

You can modify PAARO's abilities by adjusting the modules for different tasks such as mood detection, Instagram scraping, or image metadata retrieval. To extend PAARO's capabilities:
- Add more modules for additional functionality.
- Modify the `takecommand()` function to include new trigger phrases.
- Customize responses in the `speak()` function.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
