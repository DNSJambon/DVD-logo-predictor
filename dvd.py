import pygame
import argparse

# List of color variants for the DVD logo
dvd_images = ['images/dvd1.png', 'images/dvd2.png', 'images/dvd3.png', 'images/dvd4.png', 'images/dvd5.png', 'images/dvd6.png', 'images/dvd7.png', 'images/dvd8.png']

# Least Common Multiple function
def lcm(nbr1, nbr2):
    max_num = max(nbr1, nbr2)
    while True:
        if max_num % nbr1 == 0 and max_num % nbr2 == 0:
            return max_num
        max_num += 1

# Function to calculate time remaining until next impact
def calculate_time_remaining(steps, lcm_value, initial_time):
    remaining_time = ((lcm_value - steps) / 125) * initial_time
    return f"{int(remaining_time+1):02d} s"

def bounces_until_corner(L, H, l, h):
    # Calculate the least common multiple
    lcm_value = lcm(L - l, H - h)
    
    # Calculate the number of horizontal and vertical bounces
    horizontal_bounces = lcm_value // (L - l)
    vertical_bounces = lcm_value // (H - h)
    
    # Total bounces is the sum of horizontal and vertical bounces
    total_bounces = horizontal_bounces + vertical_bounces
    
    return total_bounces-2

# Main function to run the DVD bouncing logo simulation
def dvd(window_width, window_height, logo_width, logo_height, trace, fastforward):
    pygame.init()
    
    # Initialize variables
    font = pygame.font.Font(None, 45)
    x_pos, y_pos = 1, 1
    lcm_value = lcm(window_width - logo_width, window_height - logo_height)  # this represents the number of steps before the logo hits the corner
    color_index = 1

    # Initialize window
    screen = pygame.display.set_mode((window_width, window_height))
    trail_surface = pygame.Surface((window_width, window_height))
    dvd_logo = pygame.image.load(dvd_images[color_index])
    dvd_logo = pygame.transform.scale(dvd_logo, (logo_width, logo_height))
    direction = (1, 1)

    step_count = 0
    running = True
    bounces_remaining = bounces_until_corner(window_width, window_height, logo_width, logo_height)
    while running:
        if not fastforward:
            pygame.time.delay(8)


        step_count += 1

        if color_index == 8:
            color_index = 0

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check for collisions and change direction
        if (y_pos == 0 or y_pos == window_height - logo_height) and (x_pos == 0 or x_pos == window_width - logo_width):
            direction = (-direction[0], -direction[1])
            step_count = 0
            dvd_logo = pygame.transform.scale(pygame.image.load('images/ultime.png'), (logo_width, logo_height))
            trace = False
            bounces_remaining = bounces_until_corner(window_width, window_height, logo_width, logo_height)
        else:
            if x_pos == 0 or x_pos == window_width - logo_width:
                direction = (-direction[0], direction[1])
                dvd_logo = pygame.transform.scale(pygame.image.load(dvd_images[color_index]), (logo_width, logo_height))
                color_index += 1
                bounces_remaining -= 1
            elif y_pos == 0 or y_pos == window_height - logo_height:
                direction = (direction[0], -direction[1])
                dvd_logo = pygame.transform.scale(pygame.image.load(dvd_images[color_index]), (logo_width, logo_height))
                color_index += 1
                bounces_remaining -= 1
            

        # Update position
        x_pos += direction[0]
        y_pos += direction[1]

        
        if (not fastforward or step_count % (lcm_value // 3000) == 0):
            # Clear screen
            screen.fill((0, 0, 0))
            screen.blit(trail_surface, (0, 0))
            screen.blit(dvd_logo, (x_pos, y_pos))

            # Display remaining bounce count
            if bounces_remaining == 0:
                timer_text = font.render(f"Get ready...", True, (255, 255, 255))
            else:
                timer_text = font.render(f"{bounces_remaining} bounces until impact", True, (255, 255, 255))
            text_rect = timer_text.get_rect(center=(window_width // 2, 30))
            screen.blit(timer_text, text_rect)
  
            pygame.display.update()
            
        # Draw trace if enabled
        if trace:
            pygame.draw.line(trail_surface, (12, 0, 200), (x_pos + logo_width // 2, y_pos + logo_height // 2), (x_pos + logo_width // 2, y_pos + logo_height // 2), 3)

    pygame.quit()

# Command-line interface setup
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DVD Bouncing Logo Simulation")
    parser.add_argument("window_width", type=int, help="Width of the window")
    parser.add_argument("window_height", type=int, help="Height of the window")
    parser.add_argument("logo_width", type=int, help="Width of the DVD logo")
    parser.add_argument("logo_height", type=int, help="Height of the DVD logo")
    parser.add_argument("--trace", action="store_true", help="Enable tracing the path of the DVD logo")
    parser.add_argument("--ff", action="store_true", help="Enable fastforwarding the simulation")
    
    args = parser.parse_args()

    # Call the main function with parsed arguments
    dvd(args.window_width, args.window_height, args.logo_width, args.logo_height, args.trace, args.ff)


#python .\dvd.py 1320 770 220 110 --trace --ff