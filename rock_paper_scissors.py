"""
Rock Paper Scissors game with improved sound handling
"""
import random
import time
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.traceback import install
from pyfiglet import Figlet

# Initialize rich console
install()
console = Console()

def play_sound(sound_type="click", wait_for_completion=False):
    """
    Play sound effect using multiple fallback methods
    sound_type: 'click', 'win', 'lose', 'tie'
    wait_for_completion: if True, wait for sound to finish before returning
    """
    # Method 1: Try pygame (most reliable)
    try:
        import pygame
        pygame.mixer.init()
        
        # Define sound mappings
        sound_files = {
            'click': 'sounds/click.mp3',
            'win': 'sounds/win.mp3', 
            'lose': 'sounds/lose.mp3',
            'tie': 'sounds/tie.mp3'
        }
        
        sound_file = sound_files.get(sound_type, 'sounds/click.mp3')
        
        if os.path.exists(sound_file):
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            
            if wait_for_completion:
                # Wait for the sound to finish playing
                while pygame.mixer.get_busy():
                    time.sleep(0.1)
            return True
    except (ImportError, Exception):
        pass
    
    # Method 2: Try winsound (Windows built-in)
    try:
        import winsound
        # Play system sounds as fallback
        if sound_type == 'win':
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        elif sound_type == 'lose':
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        elif sound_type == 'tie':
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        else:  # click sound
            winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)
        return True
    except (ImportError, Exception):
        pass
    
    # Method 3: Try playsound as last resort
    try:
        from playsound import playsound
        sound_file = f'sounds/{sound_type}.mp3'
        if os.path.exists(sound_file):
            playsound(sound_file)
            return True
    except (ImportError, Exception):
        pass
    
    # Method 4: Visual feedback if no sound available
    if sound_type != 'click':  # Don't show visual feedback for clicks
        console.print(f"🔊 *{sound_type} sound*", style="dim")
    return False

def stop_all_sounds():
    """Stop all currently playing sounds"""
    try:
        import pygame
        pygame.mixer.stop()
    except (ImportError, Exception):
        pass

def create_sound_files():
    """Create a sounds directory and explain how to add sound files"""
    sounds_dir = "sounds"
    if not os.path.exists(sounds_dir):
        os.makedirs(sounds_dir)
        console.print(f"📁 Created '{sounds_dir}' directory for sound files", style="bold yellow")
        console.print("💡 Add these sound files to enable audio:", style="bold blue")
        console.print("   - click.mp3 (button click sound)")
        console.print("   - win.mp3 (victory sound)")  
        console.print("   - lose.mp3 (defeat sound)")
        console.print("   - tie.mp3 (tie game sound)")
        console.print("🌐 You can download free sounds from: freesound.org or zapsplat.com")
        console.print()

def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(player_score, computer_score):
    """Display the game header with scores"""
    figlet = Figlet(font='slant')
    ascii_art = figlet.renderText('Rock Paper Scissors')
    console.print(ascii_art, style="bold green")
    console.print("Welcome to Rock Paper Scissors! 🎮", style="bold blue")
    console.print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.", style="bold yellow")
    console.print("You can also type 'r' for rock, 'p' for paper, or 's' for scissors.", style="bold yellow")
    console.print(f"Current Scores => Player: {player_score} | Computer: {computer_score}", style="bold yellow")
    console.print()

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the round"""
    if player_choice == computer_choice:
        return "tie"
    elif ((player_choice == 'rock' and computer_choice == 'scissors') or
          (player_choice == 'paper' and computer_choice == 'rock') or
          (player_choice == 'scissors' and computer_choice == 'paper')):
        return "player"
    else:
        return "computer"

def main():
    """Main game loop"""
    choices = ['rock', 'paper', 'scissors']
    short_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    player_score = 0
    computer_score = 0

    # Create sounds directory if it doesn't exist
    create_sound_files()

    # Initial display
    clear_screen()
    display_header(player_score, computer_score)

    while True:
        # Get player input
        player_choice = Prompt.ask("Enter your choice").lower().strip()
        # Map short input to full choice
        if player_choice in short_map:
            player_choice = short_map[player_choice]
        
        if player_choice == 'quit':
            # Stop any currently playing sounds before playing the final sound
            stop_all_sounds()
            
            console.print("\n" + "="*50, style="bold cyan")
            console.print("Thanks for playing! Final Scores:", style="bold green")
            console.print(f"Player: {player_score} | Computer: {computer_score}", style="bold yellow")
            
            # Small delay to ensure any previous sounds are stopped
            time.sleep(0.5)
            
            if player_score > computer_score:
                console.print("🎉 Congratulations! You won overall! 🎉", style="bold green")
                play_sound("win", wait_for_completion=True)
            elif computer_score > player_score:
                console.print("😔 Computer won overall. Better luck next time!", style="bold red")
                play_sound("lose", wait_for_completion=True)
            else:
                console.print("🤝 It's a tie overall! Great game!", style="bold cyan")
                play_sound("tie", wait_for_completion=True)
            console.print("="*50, style="bold cyan")
            break
        
        # Only play click sound for valid game choices (not for quit or invalid input)
        if player_choice in choices:
            play_sound("click")
        
        if player_choice not in choices:
            console.print("❌ Invalid choice. Please try again.", style="bold red")
            continue
        
        # Computer makes choice
        computer_choice = random.choice(choices)
        
        # Display choices
        console.print(f"\n🎮 You chose: {player_choice.upper()}", style="bold blue")
        console.print(f"🤖 Computer chose: {computer_choice.upper()}", style="bold magenta")
        
        # Determine and display winner
        result = determine_winner(player_choice, computer_choice)
        
        # Stop any previous sounds before playing the result sound
        stop_all_sounds()
        time.sleep(0.2)  # Brief pause to ensure click sound is stopped
        
        if result == "tie":
            console.print("🤝 It's a tie!", style="bold cyan")
            play_sound("tie")
        elif result == "player":
            console.print("🎉 You win this round!", style="bold green")
            player_score += 1
            play_sound("win")
        else:
            console.print("😔 Computer wins this round!", style="bold red")
            computer_score += 1
            play_sound("lose")
        
        # Show updated scores
        console.print(f"\n📊 Updated Scores => Player: {player_score} | Computer: {computer_score}", style="bold yellow")
        
        # Wait before next round
        console.print("\nPress Enter to continue...")
        input()
        
        # Clear screen and show header for next round
        clear_screen()
        display_header(player_score, computer_score)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n👋 Game interrupted. Thanks for playing!", style="bold yellow")
    except Exception as e:
        console.print(f"\n❌ An error occurred: {e}", style="bold red")