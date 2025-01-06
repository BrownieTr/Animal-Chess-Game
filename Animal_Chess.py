# Author: Brownie Tran - Trixie Vo
# Date: 

import turtle

# Function to create a new screen and reset turtle
def create_screen():
    """Create the screen"""
    global screen
    screen = turtle.Screen()
    screen.title("Animal Chess")
    screen.bgcolor("burlywood")
    screen.setup(800, 800)
    screen.tracer(0)
    # Set up where the screen is going to appear when we run the code
    screen.setup(800, 800, 400, 5)
    
# Function to clear the screen and create a new one
def clear_screen():
    """Clear all the things on the screen"""
    turtle.clearscreen()
    create_screen()

# Function to handle the play button click
def play(x, y):
    """Play the game after the play button was clicked"""
    clear_screen()
    print("Starting the game...")

    # Create the back button
    back_button = turtle.Turtle()
    back_button.shape("square")
    back_button.color("salmon")
    back_button.penup()
    back_button.goto(280, -280)
    back_button.shapesize(1, 4)
    back_button.stamp()

    # Write label on the back button
    back_label = turtle.Turtle()
    back_label.color("white")
    back_label.penup()
    back_label.hideturtle()
    back_label.goto(280, -270)
    back_label.write("Back", align="center", font=("VNI-Fillmore", 16, "bold"))

    # Register the back button click handler
    back_button.onclick(show_menu)
    screen.setup(800, 800, 400, 5)
    
    # Create a turtle to draw the board
    draw = turtle.Turtle()
    
    def board1(draw, x, y, size):
        """Draw the green board"""
        draw.penup()
        draw.goto(x,y)
        draw.pendown()
        draw.color("medium sea green")
        draw.begin_fill()
        for i in range (4):
            draw.forward(size)
            draw.right(90)
        draw.end_fill()

    def color_board(draw, x, y, size):
        """Draw the rivers"""
        draw.penup()
        draw.goto(x,y)
        draw.pendown()
        draw.color("steel blue")
        draw.begin_fill()
        for i in range (4):
            draw.forward(size)
            draw.right(90)
        draw.end_fill()

    def board2(draw, x, y, size):
        """Draw the white line for the board"""
        draw.penup()
        draw.goto(x,y)
        draw.pendown()
        draw.color("white")
        for i in range (4):
            draw.forward(size)
            draw.right(90)

    def draw_board():
        """Draw the board"""
        x =-320 
        y = -260
        size = 70
        for i in range (9):
            for j in range (7):
                board1(draw, x + j*size, y + i*size, size)

            for j in range (7):
                board2(draw, x + j*size, y + i*size, size)
        
            # Draw row coordinates
            draw.penup()
            draw.goto(x - 40, y + i*size - 40)
            draw.color("black")
            draw.write(str(i+1), align="center", font=("VNI-Fillmore", 12, "bold"))

        # Draw the rivers
        draw.goto(-36,-118)
        x = -40
        y = -50
        for i in range(3):
            for j in range (2):
                color_board(draw, x + j*size, y + i*size, size)
                
            for j in range(2):
                board2(draw, x + j*size, y + i*size, size)
                
        draw.penup()
        draw.goto(-294, -118)
        x = -250
        y = -50
        for i in range(3):
            for j in range (2):
                color_board(draw, x + j*size, y + i*size, size)
                
            for j in range(2):
                board2(draw, x + j*size, y + i*size, size)
                
        # Draw column coordinates
        x = -320
        y = 300
        draw.penup()
        draw.goto(x - 20, y + 10)
        for i in range(7):
            draw.goto(x + i*size + 30, y + 10)
            draw.write(chr(ord('a')+i), align="center", font=("VNI-Fillmore", 12, "bold"))
            
        draw.hideturtle()

    draw_board()

    # Manually update the screen
    screen.update()

    # Add all the images of the red animals
    screen.addshape("images\Ratred.gif")
    screen.addshape("images\Catred.gif")
    screen.addshape("images\Dogred.gif")
    screen.addshape("images\Wolfred.gif")
    screen.addshape("images\Jaguarred.gif")
    screen.addshape("images\Tigerred.gif")
    screen.addshape("images\Lionred.gif")
    screen.addshape("images\Elephantred.gif")

        # Add all the images of the blue animals
    screen.addshape("images\Ratblue.gif")
    screen.addshape("images\Catblue.gif")
    screen.addshape("images\Dogblue.gif")
    screen.addshape("images\Wolfblue.gif")
    screen.addshape("images\Jaguarblue.gif")
    screen.addshape("images\Tigerblue.gif")
    screen.addshape("images\Lionblue.gif")
    screen.addshape("images\Elephantblue.gif")
    
    # Create a turtle for each red animal in the chess
    ratred = turtle.Turtle()
    catred = turtle.Turtle()
    dogred = turtle.Turtle()
    wolfred = turtle.Turtle()
    jaguarred = turtle.Turtle()
    tigerred = turtle.Turtle()
    lionred = turtle.Turtle()
    elephantred = turtle.Turtle()

    # Create a turtle for each blue animal in the chess
    ratblue = turtle.Turtle()
    catblue = turtle.Turtle()
    dogblue = turtle.Turtle()
    wolfblue = turtle.Turtle()
    jaguarblue = turtle.Turtle()
    tigerblue = turtle.Turtle()
    lionblue = turtle.Turtle()
    elephantblue = turtle.Turtle()

    # Set each red turtle an animal
    ratred.shape("images\Ratred.gif")
    catred.shape("images\Catred.gif")
    dogred.shape("images\Dogred.gif")
    wolfred.shape("images\Wolfred.gif")
    jaguarred.shape("images\Jaguarred.gif")
    tigerred.shape("images\Tigerred.gif")
    lionred.shape("images\Lionred.gif")
    elephantred.shape("images\Elephantred.gif")

    # Set each blue turtle an animal
    ratblue.shape("images\Ratblue.gif")
    catblue.shape("images\Catblue.gif")
    dogblue.shape("images\Dogblue.gif")
    wolfblue.shape("images\Wolfblue.gif")
    jaguarblue.shape("images\Jaguarblue.gif")
    tigerblue.shape("images\Tigerblue.gif")
    lionblue.shape("images\Lionblue.gif")
    elephantblue.shape("images\Elephantblue.gif")
    
    
    # Place each red animal in their right spots
    ratred.penup()
    ratred.goto(70*(int(160/70))-5, 70*(int(-130/70))-85)
    catred.penup()
    catred.goto(70*(int(-150/70))-5, 70*(int(-270/70))-85)
    dogred.penup()
    dogred.goto(70*(int(20/70))-5, 70*(int(-270/70))-85)
    wolfred.penup()
    wolfred.goto(70*(int(-150/70))-5, 70*(int(-130/70))-85)
    jaguarred.penup()
    jaguarred.goto(70*(int(30/70))-5, 70*(int(-80/70))-85)
    tigerred.penup()
    tigerred.goto(70*(int(-290/70))-5, 70*(int(-270/70))-85)
    lionred.penup()
    lionred.goto(70*(int(160/70))-5, 70*(int(-270/70))-85)
    elephantred.penup()
    elephantred.goto(70*(int(-290/70))-5, 70*(int(-130/70))-85)

    # Place each blue animal in their right spots
    ratblue.penup()
    ratblue.goto(70*(int(-290/70))-5, 70*(int(230/70))-85)
    catblue.penup()
    catblue.goto(70*(int(30/70))-5, 70*(int(290/70))-15)
    dogblue.penup()
    dogblue.goto(70*(int(-150/70))-5, 70*(int(290/70))-15)
    wolfblue.penup()
    wolfblue.goto(70*(int(30/70))-5, 70*(int(150/70))-15)
    jaguarblue.penup()
    jaguarblue.goto(70*(int(-150/70))-5, 70*(int(150/70))-15)
    tigerblue.penup()
    tigerblue.goto(70*(int(160/70))-5, 70*(int(290/70))-15)
    lionblue.penup()
    lionblue.goto(70*(int(-290/70))-5, 70*(int(290/70))-15)
    elephantblue.penup()
    elephantblue.goto(70*(int(160/70))-5, 70*(int(150/70))-15)

    # Draw the "CAVE" label for each side
    def draw_cave_label(color, x, y):
        "Draw caves for both team"
        label = turtle.Turtle()
        label.color("yellow")
        label.penup()
        label.hideturtle()
        label.goto(x, y)
        label.write("CAVE", align="center", font=("VNI-Fillmore", 16, "bold"))

    draw_cave_label("red", -75, 250)
    draw_cave_label("blue", -75, -310)

    screen.tracer(1)

    # Create groups for each category of the animals based on their moving rules
    selected_gif_group = [ratred, catred, dogred, wolfred, jaguarred, tigerred, lionred, elephantred,
                          ratblue, catblue, dogblue, wolfblue, jaguarblue, tigerblue, lionblue, elephantblue]
    
    gif_red_turtles = [ratred, catred, dogred, wolfred, jaguarred,
                   tigerred, lionred, elephantred]
    
    gif_blue_turtles = [ratblue, catblue, dogblue, wolfblue, jaguarblue,
                        tigerblue, lionblue, elephantblue]

    normal_group = [catred, catblue, dogred, dogblue, jaguarred,
                    jaguarblue, lionred, lionblue, elephantred, elephantblue]
    
    river_crossing_group = [wolfred, wolfblue, tigerred, tigerblue]
    rat_group = [ratred, ratblue]

    # Create functions to check if an animal is selected
    def move_selected_gif(x, y):
        """Move the selected_gif according to its rule"""
        moving_turtle = selected_gif
        target_turtle = get_turtle_at_position(x, y, selected_gif_group)
        occupied = check_if_occupied(x, y, selected_gif_group)
        if occupied:
            check_eat(moving_turtle, target_turtle, gif_red_turtles, gif_blue_turtles)

        else:
            if selected_gif in river_crossing_group:
                river_crossing(x, y)

            else:
                # Set the moving rules for the animals in each specific group
                if selected_gif in normal_group :
                    if (x > selected_gif.xcor() + 105
                        or y > selected_gif.ycor() + 105
                        or x < selected_gif.xcor() - 105
                        or y < selected_gif.ycor() - 105):
                        print("Can only move one block, please choose an animal and move again.")
                        screen.onclick(move_selected_gif)
                    
                    elif (-40 < x < 100 and -120 < y < 90
                        or -250 < x < -110 and -120 < y < 90):
                        print("This animal can't cross the river, please choose an animal and move again.")
                        print("Please read the rules before playing the game, thank you!")
                        screen.onclick(move_selected_gif)
                            
                    else:
                        move_1_block(x,y)

                else:
                    if (x > selected_gif.xcor() + 105
                        or y > selected_gif.ycor() + 105
                        or x < selected_gif.xcor() - 105
                        or y < selected_gif.ycor() - 105):
                        print("Can only move one block, please choose an animal and move again.")
                        screen.onclick(move_selected_gif)

                    else:
                        move_1_block(x,y)
                            
            screen.onclick(select_gif)
            # Change turns
            turn = "blue"
            turn = "red" if turn == "blue" else "blue"

    def move_1_block(new_x, new_y):
        """Move 1 block horizontally or vertically"""
        if selected_gif in gif_blue_turtles:
            if -110 < new_x < -40 and -330 < new_y < -260:
                if new_x > selected_gif.xcor() + 35 and new_y < selected_gif.ycor() +35:
                    selected_gif.goto(selected_gif.xcor() + 70, selected_gif.ycor())
                    
                elif new_x < selected_gif.xcor() -35 and new_y < selected_gif.ycor() +35 :
                    selected_gif.goto(selected_gif.xcor() - 70, selected_gif.ycor())
                    
                elif new_y > selected_gif.ycor() +35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() +70)
                    
                elif new_y < selected_gif.ycor() -35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() -70)
                clear_screen()
                
                text = turtle.Turtle()
                text.color("white")
                text.penup()
                text.hideturtle()
                text.goto(0, 0)
                text.write("Congratulation!\n", align="center", font=("VNI-Fillmore", 24, "bold"))
                           

                text = turtle.Turtle()
                text.color("white")
                text.penup()
                text.hideturtle()
                text.goto(0, 2)
                text.write("Blue team win the game.", align="center", font=("VNI-Fillmore", 24, "bold"))

                # Create the back button
                back_button = turtle.Turtle()
                back_button.shape("square")
                back_button.color("salmon")
                back_button.penup()
                back_button.goto(60, -60)
                back_button.shapesize(1, 4)
                back_button.stamp()

                # Write label on the back button
                back_label = turtle.Turtle()
                back_label.color("white")
                back_label.penup()
                back_label.hideturtle()
                back_label.goto(60, -50)
                back_label.write("Back", align="center", font=("VNI-Fillmore", 16, "bold"))

                # Create the replay button
                replay_button = turtle.Turtle()
                replay_button.shape("square")
                replay_button.color("salmon")
                replay_button.penup()
                replay_button.goto(-60, -60)
                replay_button.shapesize(1, 4)
                replay_button.stamp()

                # Write label on the back button
                replay_label = turtle.Turtle()
                replay_label.color("white")
                replay_label.penup()
                replay_label.hideturtle()
                replay_label.goto(-60, -50)
                replay_label.write("Replay", align="center", font=("VNI-Fillmore", 16, "bold"))

                # Register the button click handler
                replay_button.onclick(play)
                back_button.onclick(show_menu)

                # Manually update the screen
                screen.update() 

            elif -110 < new_x < -40 and 230 < new_y < 300:
                print("Cant go there, please choose an animal and move again.")
                screen.onclick(move_selected_gif)

            elif (new_x > 170 or new_x < -320
                 or new_y > 300 or new_y < -330):
                print("Out of bound! Please choose an animal and move again.")
                screen.onclick(move_selected_gif)

            else:
                if new_x > selected_gif.xcor() + 35 and new_y < selected_gif.ycor() +35:
                    selected_gif.goto(selected_gif.xcor() + 70, selected_gif.ycor())
                    
                elif new_x < selected_gif.xcor() -35 and new_y < selected_gif.ycor() +35 :
                    selected_gif.goto(selected_gif.xcor() - 70, selected_gif.ycor())
                    
                elif new_y > selected_gif.ycor() +35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() +70)
                    
                elif new_y < selected_gif.ycor() -35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() -70)

        elif selected_gif in gif_red_turtles:
            if -110 < new_x < -40 and 230 < new_y < 300:
                if new_x > selected_gif.xcor() + 35 and new_y < selected_gif.ycor() +35:
                    selected_gif.goto(selected_gif.xcor() + 70, selected_gif.ycor())
                    
                elif new_x < selected_gif.xcor() -35 and new_y < selected_gif.ycor() +35 :
                    selected_gif.goto(selected_gif.xcor() - 70, selected_gif.ycor())
                    
                elif new_y > selected_gif.ycor() +35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() +70)
                    
                elif new_y < selected_gif.ycor() -35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() -70)
                clear_screen()
                
                text = turtle.Turtle()
                text.color("white")
                text.penup()
                text.hideturtle()
                text.goto(0, 2)
                text.write("Red team win the game.", align="center", font=("VNI-Fillmore", 24, "bold"))

                text = turtle.Turtle()
                text.color("white")
                text.penup()
                text.hideturtle()
                text.goto(0, 0)
                text.write("Congratulation!\n", align="center", font=("VNI-Fillmore", 24, "bold"))
                           

                # Create the back button
                back_button = turtle.Turtle()
                back_button.shape("square")
                back_button.color("salmon")
                back_button.penup()
                back_button.goto(60, -60)
                back_button.shapesize(1, 4)
                back_button.stamp()

                # Write label on the back button
                back_label = turtle.Turtle()
                back_label.color("white")
                back_label.penup()
                back_label.hideturtle()
                back_label.goto(60, -50)
                back_label.write("Back", align="center", font=("VNI-Fillmore", 16, "bold"))

                # Create the replay button
                replay_button = turtle.Turtle()
                replay_button.shape("square")
                replay_button.color("salmon")
                replay_button.penup()
                replay_button.goto(-60, -60)
                replay_button.shapesize(1, 4)
                replay_button.stamp()

                # Write label on the back button
                replay_label = turtle.Turtle()
                replay_label.color("white")
                replay_label.penup()
                replay_label.hideturtle()
                replay_label.goto(-60, -50)
                replay_label.write("Replay", align="center", font=("VNI-Fillmore", 16, "bold"))

                # Register the button click handler
                replay_button.onclick(play)
                back_button.onclick(show_menu)

                # Manually update the screen
                screen.update()

            elif -110 < new_x < -40 and -330 < new_y < -260:
                print("Cant go there, please choose an animal and move again.")
                screen.onclick(move_selected_gif)

            elif (new_x > 170 or new_x < -320
                 or new_y > 300 or new_y < -330):
                print("Out of bound! Please choose an animal and move again.")
                screen.onclick(move_selected_gif)


            else:
                if new_x > selected_gif.xcor() + 35 and new_y < selected_gif.ycor() +35:
                    selected_gif.goto(selected_gif.xcor() + 70, selected_gif.ycor())
                    
                elif new_x < selected_gif.xcor() -35 and new_y < selected_gif.ycor() +35 :
                    selected_gif.goto(selected_gif.xcor() - 70, selected_gif.ycor())
                    
                elif new_y > selected_gif.ycor() +35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() +70)
                    
                elif new_y < selected_gif.ycor() -35 and new_x < selected_gif.xcor() + 35 :
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() -70)

    def river_crossing(x, y):
        """Handle the river crossing movement"""
        # Check if the target position is on the same row or column as the current position
        if x > selected_gif.xcor() + 35 and y < selected_gif.ycor() + 35:
            # Check if there is any rat from rat_group on the same row 
            if ((100 < x < 170 and -120 < y < 90)
                or (-110 < x < -40 and -120 < y < 90)
                and ( -120 < selected_gif.ycor() < 90)) :
                if ((selected_gif.xcor() < ratred.xcor() < x
                     or selected_gif.xcor() < ratblue.xcor() < x)
                     and (selected_gif.ycor() in [ratred.ycor(), ratblue.ycor()])):
                    print("This animal cannot cross the river because of the rat, please choose another animal or move again.")
                    screen.onclick(move_selected_gif)

                else:
                    selected_gif.goto(selected_gif.xcor() + 70*3, selected_gif.ycor())

            else:
                if (x > selected_gif.xcor() + 105
                    or y > selected_gif.ycor() + 105
                    or x < selected_gif.xcor() - 105
                    or y < selected_gif.ycor() - 105):
                    print("Can only move one block, please choose an animal and move again.")
                    screen.onclick(move_selected_gif)

                elif (-40 < x < 100 and -120 < y < 90 
                 or -250 < x < -110 and -120 < y < 90) :
                    print("This animal can only jump through the river, can't go in. Please choose an animal and move again.")

                else:
                    move_1_block(x,y)
                    
        elif x < selected_gif.xcor() - 35 and y < selected_gif.ycor() + 35:
            # Check if there is any rat from rat_group on the same row
            if ((-320 < x < -250 and -120 < y < 90)
                or (-110 < x < -40 and -120 < y < 90)
                and ( -120 < selected_gif.ycor() < 90)) :
                if ((selected_gif.xcor() > ratred.xcor() > x
                     or selected_gif.xcor() > ratblue.xcor() > x)
                     and (selected_gif.ycor() in [ratred.ycor(), ratblue.ycor()])):
                    print("This animal cannot cross the river because of the rat, please choose another animal or move again.")
                    screen.onclick(move_selected_gif)

                else:
                    selected_gif.goto(selected_gif.xcor() - 70*3, selected_gif.ycor())
                
            else:
                if (x > selected_gif.xcor() + 105
                    or y > selected_gif.ycor() + 105
                    or x < selected_gif.xcor() - 105
                    or y < selected_gif.ycor() - 105):
                    print("Can only move one block, please choose an animal and move again.")
                    screen.onclick(move_selected_gif)

                elif (-40 < x < 100 and -120 < y < 90 
                    or -250 < x < -110 and -120 < y < 90) :
                    print("This animal can only jump through the river, can't go in. Please choose an animal and move again.")

                else:
                    move_1_block(x,y)

        elif y > selected_gif.ycor() +35 and x < selected_gif.xcor() + 35 :
            # Check if there is any rat from rat_group on the same  column
            if ((-250 < x < -110 and 90 < y < 160)
                or (-40 < x < 100 and 90 < y < 160)
                and ((( -250 < selected_gif.xcor() < -110
                or (-40 < selected_gif.xcor() < 100))
                and -190 < selected_gif.ycor() < -120))):
                if ((selected_gif.ycor() < ratred.ycor() < y
                     or selected_gif.ycor() < ratblue.ycor() < y)
                     and (selected_gif.xcor() in [ratred.xcor(), ratblue.xcor()])):
                    print("This animal cannot cross the river because of the rat, please choose another animal or move again.")
                    screen.onclick(move_selected_gif)
                    
                else:
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() + 70*4)
                
            else:
                if (x > selected_gif.xcor() + 105
                    or y > selected_gif.ycor() + 105
                    or x < selected_gif.xcor() - 105
                    or y < selected_gif.ycor() - 105):
                    print("Can only move one block, please choose an animal and move again.")
                    screen.onclick(move_selected_gif)

                elif (-40 < x < 100 and -120 < y < 90 
                    or -250 < x < -110 and -120 < y < 90) :
                    print("This animal can only jump through the river, can't go in. Please choose an animal and move again.")

                else:
                    move_1_block(x,y)
                    
        elif y < selected_gif.ycor() -35 and x < selected_gif.xcor() + 35 :
            # Check if there is any rat from rat_group on the same column
            if ((-250 < x < -110 and -190 < y < -120)
                or (-40 < x < 100 and -190 < y <-120)
                and (( -250 < selected_gif.xcor() < -110
                or -40 < selected_gif.xcor() < 100)
                and 90 < selected_gif.ycor() < 160)) :
                if ((selected_gif.ycor() > ratred.ycor() > y
                     or selected_gif.ycor() > ratblue.ycor() > y)
                     and (selected_gif.xcor() in [ratred.xcor(), ratblue.xcor()])):
                    print("This animal cannot cross the river because of the rat, please choose another animal or move again.")
                    screen.onclick(move_selected_gif)
                    
                else:
                    selected_gif.goto(selected_gif.xcor(), selected_gif.ycor() - 70*4)
                
            else:
                if (x > selected_gif.xcor() + 105
                    or y > selected_gif.ycor() + 105
                    or x < selected_gif.xcor() - 105
                    or y < selected_gif.ycor() - 105):
                    print("Can only move one block, please choose an animal and move again.")
                    screen.onclick(move_selected_gif)

                elif (-40 < x < 100 and -120 < y < 90 
                    or -250 < x < -110 and -120 < y < 90) :
                    print("This animal can only jump through the river, can't go in. Please choose an animal and move again.")

                else:
                    move_1_block(x,y)

    def select_gif(x, y):
        """Take the selected animal and move it"""
        global selected_gif
        turn = "blue"
        if turn == "blue":
            for gif_blue_turtle in gif_blue_turtles:
                if is_piece_selected(gif_blue_turtle, x, y):
                    selected_gif = gif_blue_turtle
                    screen.onclick(move_selected_gif)
        turn = "red" if turn == "blue" else "blue"
       
        if turn == "red":
            for gif_red_turtle in gif_red_turtles:
                if is_piece_selected(gif_red_turtle, x, y):
                    selected_gif = gif_red_turtle
                    screen.onclick(move_selected_gif)

            
    def is_piece_selected(piece, mouse_x, mouse_y):
        """Check whether an animal is selected or not"""
        piece_x, piece_y = piece.position()
        piece_size = 70
        piece_left = piece_x - piece_size / 2
        piece_right = piece_x + piece_size / 2
        piece_top = piece_y + piece_size / 2
        piece_bottom = piece_y - piece_size / 2

        # If the animal is selected, return True, return False otherwise
        if (
            mouse_x >= piece_left
            and mouse_x <= piece_right
            and mouse_y >= piece_bottom
            and mouse_y <= piece_top
        ):
            return True
        else:
            return False

    def check_if_occupied(x, y, selected_gif_group):
        "Check if it has a turtle at the position where you click"
        for gif in selected_gif_group:
            gif_x, gif_y = gif.position()
            gif_size = 70
            gif_left = gif_x - gif_size / 2
            gif_right = gif_x + gif_size / 2
            gif_top = gif_y + gif_size / 2
            gif_bottom = gif_y - gif_size / 2
            
            if (
                x >= gif_left
                and x <= gif_right
                and y >= gif_bottom
                and y <= gif_top
            ):
                return True
            
        return False

    def get_turtle_at_position(x, y, selected_gif_group):
        "Check what turtle is at the position where you click"
        for turtle in selected_gif_group:
            turtle_x, turtle_y = turtle.position()
            turtle_size = 70
            turtle_left = turtle_x - turtle_size / 2
            turtle_right = turtle_x + turtle_size / 2
            turtle_top = turtle_y + turtle_size / 2
            turtle_bottom = turtle_y - turtle_size / 2
            
            if (
                x >= turtle_left
                and x <= turtle_right
                and y >= turtle_bottom
                and y <= turtle_top
            ):
                return turtle
        return None

    def check_eat(moving_turtle, target_turtle, gif_red_turtles, gif_blue_turtles):
        "Check if moving_turtle can eat target_turtle or not"
        if moving_turtle in gif_red_turtles and target_turtle in gif_blue_turtles:
            if (moving_turtle == ratred and (target_turtle == elephantblue
                                             or target_turtle == ratblue)) :       
                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == catred and (target_turtle == ratblue
                                              or target_turtle == catblue)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
                    
            elif (moving_turtle == dogred and (target_turtle == catblue
                                              or target_turtle == dogblue
                                              or target_turtle == ratblue)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == wolfred and (target_turtle == dogblue
                                               or target_turtle == wolfblue
                                               or target_turtle == catblue
                                               or target_turtle == ratblue)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == jaguarred and (target_turtle == wolfblue
                                                 or target_turtle == dogblue
                                                 or target_turtle == catblue
                                                 or target_turtle == ratblue
                                                 or target_turtle == jaguarblue)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == tigerred and (target_turtle == jaguarblue
                                                or target_turtle == wolfblue
                                                or target_turtle == dogblue
                                                or target_turtle == catblue
                                                or target_turtle == ratblue
                                                or target_turtle == tigerblue)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == lionred and (target_turtle == tigerblue
                                               or target_turtle == jaguarblue
                                               or target_turtle == wolfblue
                                               or target_turtle == dogblue
                                               or target_turtle == catblue
                                               or target_turtle == ratblue
                                               or target_turtle == lionblue)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == elephantred and (target_turtle == lionblue
                                                   or target_turtle == tigerblue
                                                   or target_turtle == jaguarblue
                                                   or target_turtle == wolfblue
                                                   or target_turtle == dogblue
                                                   or target_turtle == catblue
                                                   or target_turtle == elephantblue)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)

            else:
                print("Can't eat! please read the rules again.")
                
        elif moving_turtle in gif_blue_turtles and target_turtle in gif_red_turtles:
            if (moving_turtle == ratblue and (target_turtle == elephantred
                                             or target_turtle == ratred)) :

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == catblue and (target_turtle == ratred
                                              or target_turtle == catred)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == dogblue and (target_turtle == catred
                                              or target_turtle == dogred
                                              or target_turtle == ratred)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == wolfblue and (target_turtle == dogred
                                               or target_turtle == wolfred
                                               or target_turtle == catred
                                               or target_turtle == ratred)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == jaguarblue and (target_turtle == wolfred
                                                 or target_turtle == dogred
                                                 or target_turtle == catred
                                                 or target_turtle == ratred
                                                 or target_turtle == jaguarred)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                    
            elif (moving_turtle == tigerblue and (target_turtle == jaguarred
                                                or target_turtle == wolfred
                                                or target_turtle == dogred
                                                or target_turtle == catred
                                                or target_turtle == ratred
                                                or target_turtle == tigerred)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == lionblue and (target_turtle == tigerred
                                               or target_turtle == jaguarred
                                               or target_turtle == wolfred
                                               or target_turtle == dogred
                                               or target_turtle == catred
                                               or target_turtle == ratred
                                               or target_turtle == lionred)):

                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            elif (moving_turtle == elephantblue and (target_turtle == lionred
                                                   or target_turtle == tigerred
                                                   or target_turtle == jaguarred
                                                   or target_turtle == wolfred
                                                   or target_turtle == dogred
                                                   or target_turtle == catred
                                                   or target_turtle == elephantred)):
                screen.onclick(move_selected_gif)
                moving_turtle.goto(target_turtle.position())
                target_turtle.goto(999,999)
                
            else:
                print("Can't eat! please read the rules again.")
        else:
                print("Can't eat! please read the rules again.")
    
    # Register the selection and movement functions
    screen.onclick(select_gif)

    # Manually update the screen
    screen.update()


# Function to handle the rules button click
def show_rules(x, y):
    """Showing the rules's screen"""
    clear_screen()
    print("Showing the rules...")
    # Create the title
    title = turtle.Turtle()
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 150)
    title.write("Rules", align="center", font=("VNI-Fillmore", 64, "bold"))

    # Write the rules
    text = turtle.Turtle()
    text.color("white")
    text.penup()
    text.hideturtle()
    text.goto(-380, -220)
    text.write("- Blue chess pieces are allowed to go first\n"
               "- All chess pieces can only move one square\n"
               "horizontally or vertically, not diagonally.\n"
               "- For river areas:\n"
               "    + The chess piece with the mouse symbol\n"
               "    will be the only one that can move freely inside\n"
               "    the river.\n"
               "    + As for the chess pieces that are wolves\n"
               "    and tigers, they can jump across the river\n"
               "    horizontally or vertically. When making a\n"
               "    move according to the rules like this, animals\n"
               "    that stand in the way of equal or lower level\n"
               "    can be caught or eaten. However, if there is\n"
               "    a mouse standing in the water square, this\n"
               "    jumping action must stop.\n"
               "- For cave areas: A cave is an area where the player\n"
               "is not allowed to move into his cave but find ways\n"
               "to move into the opponent's cave to win.\n",
               align="left", font=("Arial", 12, "bold"))

    text = turtle.Turtle()
    text.color("white")
    text.penup()
    text.hideturtle()
    text.goto(0, -235)
    text.write("- The law of capturing or eating troops:\n"
               "    + It is only allowed to eat animal of \n"
               "    equal or lower rank. However, there are some\n"
               "    exceptions: Mouses is a lowest animal but it can\n"
               "    can catch elephants and elephants cannot catch\n"
               "    mouses.\n"
               "    + After an animal ate another animal,\n"
               "    that animal can move 1 more times without\n"
               "    clicked needed\n"
               "    + The rank of the chess pieces depends on the\n"
               "    strength of that animal:\n"
               "    Level 1: Mouse\n"
               "    Level 2: Cats\n"
               "    Level 3: Wolf\n"
               "    Level 4: Dog\n"
               "    Level 5: Jaguar\n"
               "    Level 6: Tiger\n"
               "    Level 7: Lion\n"
               "    Level 8: Elephant\n",
               align="left", font=("Arial", 12, "bold"))


    # Create the back button
    back_button = turtle.Turtle()
    back_button.shape("square")
    back_button.color("salmon")
    back_button.penup()
    back_button.goto(280, -280)
    back_button.shapesize(1, 4)
    back_button.stamp()

    # Write label on the back button
    back_label = turtle.Turtle()
    back_label.color("white")
    back_label.penup()
    back_label.hideturtle()
    back_label.goto(280, -270)
    back_label.write("Back", align="center", font=("VNI-Fillmore", 16, "bold"))

    # Register the back button click handler
    back_button.onclick(show_menu)

    # Manually update the screen
    screen.update()

# Function to handle the back button click
def show_menu(x, y):
    """Showing the menu's screen"""
    clear_screen()
    print("Showing the menu...")
    # Create the title
    title = turtle.Turtle()
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 150)
    title.write("Animal Chess", align="center", font=("VNI-Fillmore", 64, "bold"))

    # Create the play button
    play_button = turtle.Turtle()
    play_button.shape("square")
    play_button.color("peru")
    play_button.penup()
    play_button.goto(0, 0)
    play_button.shapesize(1, 6)
    play_button.stamp()

    # Write label on the play button
    play_label = turtle.Turtle()
    play_label.color("white")
    play_label.penup()
    play_label.hideturtle()
    play_label.goto(0, 15)
    play_label.write("Play", align="center", font=("VNI-Fillmore", 24, "bold"))

    # Create the rules button
    rules_button = turtle.Turtle()
    rules_button.shape("square")
    rules_button.color("sienna")
    rules_button.penup()
    rules_button.goto(0, -100)
    rules_button.shapesize(1, 6)
    rules_button.stamp()

    # Write label on the rules button
    rules_label = turtle.Turtle()
    rules_label.color("white")
    rules_label.penup()
    rules_label.hideturtle()
    rules_label.goto(0, -85)
    rules_label.write("Rules", align="center", font=("VNI-Fillmore", 24, "bold"))

    # Create the exit button
    exit_button = turtle.Turtle()
    exit_button.shape("square")
    exit_button.color("saddle brown")
    exit_button.penup()
    exit_button.goto(0, -200)
    exit_button.shapesize(1, 6)
    exit_button.stamp()

    # Write label on the exit button
    exit_label = turtle.Turtle()
    exit_label.color("white")
    exit_label.penup()
    exit_label.hideturtle()
    exit_label.goto(0, -185)
    exit_label.write("Exit", align="center", font=("VNI-Fillmore", 24, "bold"))

    # Register the button click handlers
    play_button.onclick(play)
    rules_button.onclick(show_rules)
    exit_button.onclick(exit_program)

    # Manually update the screen
    screen.update()

# Function to handle the exit button
def exit_program(x, y):
    """Exit the game when the exit button is clicked"""
    print("Goodbye!")
    turtle.bye()

# Create the initial screen
create_screen()

# Create the title
title = turtle.Turtle()
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 150)
title.write("Animal Chess", align="center", font=("VNI-Fillmore", 64, "bold"))

# Create the play button
play_button = turtle.Turtle()
play_button.shape("square")
play_button.color("peru")
play_button.penup()
play_button.goto(0, 0)
play_button.shapesize(1, 6)
play_button.stamp()

# Write label on the play button
play_label = turtle.Turtle()
play_label.color("white")
play_label.penup()
play_label.hideturtle()
play_label.goto(0, 15)
play_label.write("Play", align="center", font=("VNI-Fillmore", 24, "bold"))

# Create the rules button
rules_button = turtle.Turtle()
rules_button.shape("square")
rules_button.color("sienna")
rules_button.penup()
rules_button.goto(0, -100)
rules_button.shapesize(1, 6)
rules_button.stamp()

# Write label on the rules button
rules_label = turtle.Turtle()
rules_label.color("white")
rules_label.penup()
rules_label.hideturtle()
rules_label.goto(0, -85)
rules_label.write("Rules", align="center", font=("VNI-Fillmore", 24, "bold"))

# Create the exit button
exit_button = turtle.Turtle()
exit_button.shape("square")
exit_button.color("saddle brown")
exit_button.penup()
exit_button.goto(0, -200)
exit_button.shapesize(1, 6)
exit_button.stamp()

# Write label on the exit button
exit_label = turtle.Turtle()
exit_label.color("white")
exit_label.penup()
exit_label.hideturtle()
exit_label.goto(0, -185)
exit_label.write("Exit", align="center", font=("VNI-Fillmore", 24, "bold"))

# Register the button click handlers
play_button.onclick(play)
rules_button.onclick(show_rules)
exit_button.onclick(exit_program)

# Print the reminder
print("Please read the rules carefully before playing, its logic is quite confusing for the new ones")
print("If you are ready, then have fun!")

# Manually update the screen
screen.update()

# Start the main event loop
turtle.done()
