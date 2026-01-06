# Rock Paper Scissors

A command-line Rock Paper Scissors game built with Python, featuring styled terminal output, sound effects, and score tracking.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Features

- **Terminal User Interface** - ASCII art and styled text using the Rich library
- **Sound Effects** - Audio feedback for win, lose, tie, and click events with multiple fallback methods
- **Score Tracking** - Persistent score tracking throughout the game session
- **Quick Input Support** - Use shortcuts (`r`, `p`, `s`) or full words (`rock`, `paper`, `scissors`)
- **Cross-Platform Compatibility** - Works on Windows, macOS, and Linux

## Project Structure

```
Rock-Paper-Scissors/
├── rock_paper_scissors.py    # Main game file
├── requirements.txt          # Python dependencies
├── sounds/                   # Sound effects directory
│   ├── click.mp3            # Selection sound
│   ├── win.mp3              # Victory sound
│   ├── lose.mp3             # Defeat sound
│   └── tie.mp3              # Tie game sound
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ReVuz/Rock-Paper-Scissors.git
   cd Rock-Paper-Scissors
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python rock_paper_scissors.py
   ```

## Dependencies

| Package | Version | Description |
|---------|---------|-------------|
| rich | 13.7.0 | Terminal formatting and styling |
| pyfiglet | 1.0.2 | ASCII art text generation |
| playsound | 1.3.0 | Cross-platform audio playback |
| colorama | 0.4.6 | Cross-platform colored terminal text |
| termcolor | 2.3.0 | ANSI color formatting |
| tqdm | 4.66.1 | Progress bar library |

## Usage

1. Launch the game by running `python rock_paper_scissors.py`
2. Enter your choice:
   - Type `rock` or `r` for Rock
   - Type `paper` or `p` for Paper
   - Type `scissors` or `s` for Scissors
3. View the result and updated scores
4. Type `quit` to exit and display final scores

## Sound Support

The game supports sound effects through multiple methods: 

1. **Pygame** (recommended) - Most reliable cross-platform audio
2. **winsound** (Windows only) - Built-in Windows sound support
3. **playsound** - Fallback audio player

If no audio libraries are available, the game will display visual feedback instead.

### Custom Sound Files

To use custom sounds, place `.mp3` files in the `sounds/` directory with the following names:
- `click.mp3` - Played when making a selection
- `win.mp3` - Played when the player wins a round
- `lose.mp3` - Played when the player loses a round
- `tie.mp3` - Played when the round is a tie

## Contributing

Contributions are welcome.  Please feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.
