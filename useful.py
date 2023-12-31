from typing import Union, Any
from collections.abc import Iterable, Callable
from dataclasses import dataclass
from designer import *
import random


def pm_bool(b: bool) -> int:
    """
    Converts a boolean to +-1
    Returns `1` if b is True, `-1` if b is False
    
    Args:
        b (bool): The boolean to be converted

    Returns:
        int: Either 1 or -1, depending on b
    """
    return b * 2 - 1


def int_from_pattern(pattern_char: str) -> int:
    """
    Takes in a char from a scale pattern and returns an integer that's more
        useful.
        
    Args:
        pattern_char (str): The single character to convert

    Returns:
        int: The converted value
    """
    match pattern_char:
        case 'H':
            return 1
        case 'W':
            return 2
        case '3':
            return 3
        case _:
            return 0


def ensure_octave(pattern: [int]) -> bool:
    """
    Ensures that the input scale pattern fits exactly in an octave.
    
    Args:
        pattern (list[int]): The scale pattern to evaluate.

    Returns:
        bool: Whether it's a valid scale.
    """
    return sum(pattern) == 12


def get_next_letter(letter: str) -> str:
    """
    Gets the next letter in the musical alphabet.
    
    Args:
        letter (str): The letter to increase from.

    Returns:
        str: The next letter.
    """
    num = ord(letter) - ord('A') + 1
    num = num % 7
    return chr(num + ord('A'))


def cmp(a, b) -> int:
    """
    Returns:
        int: 0 if a and b are the same, -1 if a < b, 1 if a > b
    """
    return (a > b) - (a < b)


def ensure_version(actual: str, required: str) -> bool:
    """
    Tests if the version of a program/module is high enough.
    
    Args:
        actual (str): The actual version that we're testing
        required (str): The minimum version that we're testing against

    Returns:
        bool: Whether the program/module is new enough
    """
    return (
            tuple(map(int, (actual.split("."))))
            >=
            tuple(map(int, (required.split("."))))
    )


def boulder_speed(score: float, base_speed: int) -> float:
    """
    Finds the speed with which to move the boulders down, given the player's
        current score.
    
    Args:
        score (int): The player's score
        base_speed (int): The base speed of the boulders, when the score is less
            than 1

    Returns:
        int: The speed for the boulders
    """
    if score < 1:
        return base_speed
    return base_speed * (1 + ((score - 1) / 30) ** .9)


@dataclass
class MatchIter:
    value: Iterable
    

class MatchStr(str):
    def __eq__(self, match_list: Union[Iterable, str]) -> bool:
        """
        Checks if the value of the MatchStr is in the list, or if it is equal to
            the string.
        
        Args:
            match_list (Iterable or str): The list or string to check against

        Returns:
            bool: Whether the value of the MatchStr is in the list or is equal
                to the string
        """
        if isinstance(match_list, str):
            return match_list.__eq__(self)
        else:
            return self in list(match_list)


GAME_FONT_PATH = "resources/Game Font.ttf"
GAME_FONT_NAME = "Game Font"
TEXT_FONT_NAME = "Times New Roman"


@dataclass
class MenuEntry:
    label: str
    do: Callable
    args: [Any]
    kwargs: [str, Any]
    
    def __init__(self, label: str, do: Callable, *args, **kwargs):
        """
        This function is just here to deal with *args and **kwargs.  If
            dataclasses could deal with them, it would be unnecessary.
            
        Args:
            label (str): The text to display for the menu option
            do (Callable): The function to call when this menu option is chosen
            *args: Any positional arguments that need to be passed into `do`
            **kwargs: Any keyword arguments that need to be passed into `do`
        """
        self.label = label
        self.do = do
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, *args, **kwargs) -> Any:
        """
        This function allows MenuEntries to be called.
        
        Args:
            *args: Any more positional arguments that need to be passed into
                `do`.  These will come after the arguments specified when the
                MenuEntry was created.
            **kwargs: Any more keyword arguments that need to be passed into `do`

        Returns:
            Whatever `do` returns, if anything
        """
        return self.do(
            *[*self.args, *args],
            **{**self.kwargs, **kwargs}
        )


@dataclass
class Menu:
    header: str
    entries: [MenuEntry]
    menu_label: DesignerObject = None
    menu_text: [DesignerObject] = None
    left: bool = False
    size_percent: int = 100
    margin_left: int = 0
    margin_top: int = 0
    body_font: type[str, tuple[str, str]] = TEXT_FONT_NAME
    
    def __post_init__(self):
        """
        Takes care of the actual initialisation of the Menu, i.e. creating the
            display of it.
        """
        if self.left:
            x = self.margin_left
            anchor = 'midleft'
        else:
            x = get_width() / 2
            anchor = 'center'
        
        self.menu_label = text(
            "black", self.header, self.resize(36),
            x, self.resize(40) + self.margin_top, anchor,
            font_name=TEXT_FONT_NAME
        )
        
        if isinstance(self.body_font, str):
            self.body_font = (self.body_font, None)
        self.menu_text = []
        for i, menu_entry in enumerate(self.entries):
            self.menu_text.append(text(
                "black", f"{i + 1}. {menu_entry.label}",
                self.resize(28),
                x, self.resize(100 + 50 * i) + self.margin_top, anchor,
                font_name=self.body_font[0], font_path=self.body_font[1]
            ))

    def select(self, key: str, *args, **kwargs) -> bool:
        """
        Called when the user tries to select an option from the list.
        
        Args:
            key (str): The key pressed to choose which option
            *args: Any more arguments that need to be passed to the `do`
                function of the MenuEntry chosen, beyond those specified when it
                was created.
            **kwargs: Any more key word arguments, as described above for *args

        Returns:
            bool: Whether the key pressed successfully chose an option
        """
        try:
            selection = int(ignore_numpad(key)) - 1
            if selection < 0:
                raise IndexError("Negatives are out of bounds here.")
            self.entries[selection](*args, **kwargs)
            return True
        except (ValueError, IndexError):
            return False
    
    def resize(self, value: int) -> int:
        """
        Used to resize a height, width, or location value based on size_percent.
        
        Args:
            value (int): The value to be resized

        Returns:
            int: The resized value
        """
        return value * self.size_percent // 100
    
    def destroy(self):
        """ Destroys all of the DesignerObjects of the menu. """
        destroy(self.menu_label)
        for text_ in self.menu_text:
            destroy(text_)


def ignore_numpad(key: str) -> str:
    """
    Strips brackets indicating a number pad key press
    
    Args:
        key (str): The key pressed

    Returns:
        str: The key pressed, ignoring if it was on the number pad
    """
    return str(key).replace("[", "").replace("]", "")


def choice(iterable: Iterable):
    """
    Takes in any iterable, converts it to list and runs choice on that.
    
    Args:
        iterable (Iterable): Any Iterable from which to get a random element
        
    Returns:
        A random element of iterable
    """
    return random.choice(list(iterable))
    

GUTTER = 200  # How far away from the right to put the score and other info


def make_scale_keys_text(scale_names: [str]) -> [DesignerObject]:
    """
    Makes the table showing the user what keys to press for which scale type.
    
    Args:
        scale_names (list[str]): The list of names of scale type

    Returns:
        list[DesignerObject]: A list of DesignerObjects displaying which keys to
            press for which scale type.
    """
    from scale import SCALE_TYPE_KEYS
    scale_keys_strs = [
        f"{SCALE_TYPE_KEYS[scale_type_name]}: {scale_type_name}"
        for scale_type_name in scale_names
    ]
    scale_keys_text = []
    for i, scale_keys_str in enumerate(scale_keys_strs):
        scale_keys_text.append(
            text('black', scale_keys_str, 20,
                 get_width() - GUTTER, 80 + 40 * i, anchor="midleft",
                 font_name=TEXT_FONT_NAME)
        )
    return scale_keys_text
