import pyautogui
import random
import time
import string
import keyboard  # To listen for F12 and ESC press

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()  # Screen size
MOUSE_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Mouse center location
HUMAN_TYPING_DELAY = (0.05, 0.2)  # Simulate human typing delay
HUMAN_MOUSE_DELAY = (0.1, 0.5)  # Simulate human mouse delay
HUMAN_SCROLL_DELAY = (0.3, 0.6)  # Random delay between scroll actions
CLICK_PROBABILITY = 0.95  # Probability of successful mouse clicks
KEYSTROKE_PROBABILITY = 0.9  # Probability of keypress success
SCROLL_PROBABILITY = 0.8  # Probability of scrolling happening
BACKSPACE_PROBABILITY = 0.1  # Probability of pressing backspace to simulate correction

# Track the bot status
is_tracking = False  # False means not tracking, True means tracking
key_count = 0
click_count = 0
is_exit = False

# List of 100 React Development terms
react_terms = [
    'useState', 'useEffect', 'useContext', 'useReducer', 'useRef', 'component', 
    'props', 'state', 'render', 'hook', 'useMemo', 'useCallback', 'React Router', 
    'JSX', 'react-dom', 'virtual DOM', 'componentDidMount', 'componentWillUnmount', 
    'componentDidUpdate', 'setState', 'ReactDOM.render', 'class components', 
    'functional components', 'useLayoutEffect', 'React.StrictMode', 'useImperativeHandle', 
    'React.createElement', 'react-query', 'redux', 'redux-saga', 'React Native', 
    'React DevTools', 'React Context API', 'styled-components', 'npm', 'yarn', 'create-react-app', 
    'react-redux', 'React Hooks', 'useDispatch', 'useSelector', 'higher-order component', 
    'render props', 'JSX syntax', 'event handling', 'React.Component', 'error boundary', 
    'fragments', 'Portals', 'refs', 'Context Provider', 'useEffect cleanup', 
    'code splitting', 'lazy loading', 'React Suspense', 'React.memo', 'forwardRef', 
    'useLayoutEffect vs useEffect', 'Custom Hook', 'React testing library', 'Jest', 
    'enzyme', 'unit testing', 'snapshot testing', 'integration testing', 'e2e testing', 
    'useQuery', 'useMutation', 'API calls', 'axios', 'fetch API', 'localStorage', 'sessionStorage', 
    'debouncing', 'throttling', 'component composition', 'prop drilling', 'controlled component', 
    'uncontrolled component', 'useInput', 'state lifting', 'useReducer vs useState', 
    'memoization', 'reducer function', 'immutability', 'Side effects', 'callable components', 
    'React Fragment', 'conditional rendering', 'component composition', 'lazy loading components', 
    'React Developer Tools', 'React Router DOM', 'route protection', 'client-side routing', 
    'server-side rendering', 'hydration', 'dynamic import', 'static site generation', 
    'hydrate', 'browser compatibility', 'cross-browser testing', 'persistence layer', 
    'state management', 'REST API', 'GraphQL', 'Apollo Client', 'WebSockets', 'Redux Toolkit', 
    'React Query', 'useSelector', 'useDispatch', 'useCallback memoization', 'performance optimization'
]

# Function to simulate typing with random backspace pressing
def simulate_typing(text):
    global key_count
    typed_text = []  # List to store typed text (simulate typing correction)

    for char in text:
        # Random delay between key presses
        time.sleep(random.uniform(*HUMAN_TYPING_DELAY))

        # Type the character
        pyautogui.write(char)
        typed_text.append(char)
        key_count += 1

    for char in text:
        time.sleep(0.1)
        pyautogui.press('backspace')


# Function to simulate mouse click with random delay
def simulate_mouse_click():
    global click_count
    # Move the mouse to the center of the screen
    pyautogui.moveTo(MOUSE_CENTER[0], MOUSE_CENTER[1], duration=random.uniform(*HUMAN_MOUSE_DELAY))
    
    # Simulate a random mouse click with human-like delay
    if random.random() < CLICK_PROBABILITY:  # Random probability to simulate human nature
        pyautogui.click()
        click_count += 1
    time.sleep(random.uniform(*HUMAN_MOUSE_DELAY))  # Add random delay after clicking

# Function to simulate random mouse movement
def simulate_mouse_move():
    # Move the mouse to a random location on the screen
    target_x = random.randint(0, SCREEN_WIDTH)
    target_y = random.randint(0, SCREEN_HEIGHT)
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(*HUMAN_MOUSE_DELAY))
    time.sleep(random.uniform(*HUMAN_MOUSE_DELAY))  # Add random delay after movement

# Function to simulate mouse scroll
def simulate_scroll():
    if random.random() < SCROLL_PROBABILITY:
        direction = random.choice(['up', 'down'])
        if direction == 'up':
            pyautogui.scroll(random.randint(10, 30))  # Extended scroll up distance
        else:
            pyautogui.scroll(random.randint(-30, -10))  # Extended scroll down distance
        time.sleep(random.uniform(*HUMAN_SCROLL_DELAY))  # Add delay after scroll

# Function to handle time tracking start/stop when F12 is pressed
def start_stop_tracking():
    global is_tracking
    if not is_tracking:
        print("Starting tracking...")
        pyautogui.press('f12')  # Press F12 to start tracking
        is_tracking = True
    else:
        print("Stopping tracking...")
        pyautogui.press('f12')  # Press F12 to stop tracking
        is_tracking = False

# Function to simulate the human-like time tracking behavior
def track_human_actions():
    global is_tracking, is_exit

    while True:
        if is_exit:
            break
        if is_tracking:
            # Simulate some human-like key presses, mouse clicks, scrolling, etc.
            action = random.choice(['mouse_click', 'key_press', 'scroll', 'mouse_move'])

            if action == 'mouse_click':
                simulate_mouse_click()
            elif action == 'key_press':
                term = random.choice(react_terms)  # Select a random term from the list
                simulate_typing(term)
            elif action == 'scroll':
                simulate_scroll()
            elif action == 'mouse_move':
                simulate_mouse_move()

        time.sleep(random.uniform(1, 2))  # Small delay to prevent spamming actions

# Function to monitor F12 key for start/stop tracking, and ESC key to exit
def monitor_keys():
    global is_tracking, is_exit
    print("Press F12 to start/stop time tracking.")
    print("Press ESC to exit the bot.")
    
    while True:
        if keyboard.is_pressed('f12'):  # Detect when F12 is pressed
            start_stop_tracking()
            time.sleep(1)  # Debounce time to avoid multiple presses
        
        if keyboard.is_pressed('esc'):  # Detect when ESC is pressed
            is_exit = True
            print("ESC key pressed, exiting.")
            break  # Break out of the loop, effectively stopping the program

if __name__ == "__main__":
    import threading

    # Run the F12 and ESC key monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_keys)
    monitor_thread.daemon = True
    monitor_thread.start()

    # Run the tracking simulation
    track_human_actions()
