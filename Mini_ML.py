#################################################
###  X-Treme Obstacles Mini-Machine Learning  ###
#################################################


#-------Imports-------#
import random


#-------Classes-------#
class Menu:
    """Class that holds the menu options:
    1. Start and learn a new game.
    2. View your learning model.
    3. Try your model on a new game!
    4. Get some help (we know you need it)
    5. Quit """

    length = 30
    fall_chance = 0.5
    num_times = 1000
    print_flag = 0
    run_first = 0

    def start_new(num = 0):
        try:
            Menu.length = int(input("""
How long would you like your course to be?
(we recommend between 1 and 100)

Type your answer here:
            """))
        except:
            print('It says a number between 1 and 100. Try again.')
            Menu.run(1)

        if Menu.length <= 0:
            print('It says a number between 1 and 100. Try again.')
            Menu.run(1)

        if num == 1:
            try:
                Menu.fall_chance = int(input("""
How clumsy are you? Please choose a number between 1 and 100.
Please note, if you choose '100', you will always fail because
that gives you a 100% chance of tripping over your own feet.

Type your answer here:
                """))/100
            except:
                print('Can you read? Please choose a number between 1 and 100.')
                Menu.run(1)

            if Menu.fall_chance <= 0 or Menu.fall_chance > 1:
                print('Can you read? Please choose a number between 1 and 100.')
                Menu.run(1)

        try:
            Menu.num_times = int(input("""
How many times would you like to attempt the course?

Type your answer here:
            """))
        except:
            print('Why is this so difficult for you? Type a positive number.')

        if Menu.num_times < 1:
            print('Why is this so difficult for you? Type a positive number.')
            Menu.run(1)

        print_flag = input("""
Would you like every move to be printed?

Type 'y' or 'n':
        """)

        if print_flag == 'y':
            Menu.print_flag = 1
        elif print_flag == 'n':
            Menu.print_flag = 0
        else:
            print('It says type a y or an n. Get it through your head.')
            Menu.run(1)


    def run(num = 0):
        if num == 0:
            print("""
Welcome to: X-Treme Obstacles: Mini-Machine Learning

So, you’ve decided to train for the X-Treme obstacle course.
That’s great! We’re here to help. Although, it’s worth noting
that you’re kind of clumsy and not very smart. This may take
a while.
            """)
        try:
            first_answer = int(input("""
Please choose from the following options (type the number of
your choice):

    1. Start and learn a new game.
    2. View your learning model.
    3. Try your model on a new game!
    4. Get some help (we know you need it)
    5. Quit

Type your answer here:
        """))
        except:
            print('The instructions were pretty specific. Please choose 1, 2, 3, or 4')
            Menu.run(1)

        if first_answer == 1:
            Menu.start_new(1)
            if Menu.run_first == 1:
                Model.perc_dash = {'under': .25, 'over': .25, 'around': .25, 'through': .25}
                Model.perc_pole = {'under': .25, 'over': .25, 'around': .25, 'through': .25}
                Model.perc_ramp = {'under': .25, 'over': .25, 'around': .25, 'through': .25}
                Model.perc_tunnel = {'under': .25, 'over': .25, 'around': .25, 'through': .25}
            l = Learner(Menu.length, Menu.fall_chance)
            l.solve_game(Menu.num_times, Menu.print_flag)
            Menu.run_first = 1
            Menu.run(1)

        elif first_answer == 2:
            print(f"""
High hurdle chances: {Model.perc_dash}
Pole chances: {Model.perc_pole}
Ramp chances: {Model.perc_ramp}
Tunnel chances: {Model.perc_tunnel}
            """)
            Menu.run(1)

        elif first_answer == 3:
            if Menu.run_first == 1:
                Menu.start_new()
                l = Learner(Menu.length, Menu.fall_chance)
                l.solve_game(Menu.num_times, Menu.print_flag)
            else:
                print("""
Sorry, you haven't run your first model yet. Try
choosing option 1 first.
                """)
            Menu.run(1)


        elif first_answer == 4:
            print("""
    Our super-very-intro-beginner courses start with just four
obstacles: a hurdle that’s too-high hurdle ( - ), a pole ( | )
, a ramp ( / ), and a tunnel ( o ). You’ll decide the length
of your course, and it will look something like this:

    !
    ---oo/o/|-/o|-/|/ooo-o-o/-o/o|


    Your goal is to make it through the obstacle course without
messing up, and the exclamation point denotes your location in
a given attempt at the course.
    We believe that you know your physical limits the best, so you
can choose how many times you’d like to attempt the obstacle
course. Please don’t exhaust yourself. We here at X-Treme are
not responsible for any injuries or loss of life, and we rec-
ommend that you consult your doctor before engaging in any sort
of strenuous activity.
    Now, we understand that you have absolutely no idea how to nav-
igate each of these obstacles, so we’ve narrowed it down to just
four options for you: under, around, over, and through.
    On your first attempt, you’ll have an equal (25%) chance of
choosing each option. If you choose the correct move, you will
advance to the next obstacle, and your chances of choosing that
option for that type of obstacle will go up a bit. You’d think
you’d only have to learn it once, but you’re a very slow learner,
apparently.
    If you choose the incorrect move, you’ll have to start the entire
obstacle course over from the beginning, but your chances of
selecting that move for that obstacle type again will go down,
while your chances of selecting other moves will go up.
    Besides knowing which move to make, you also need to manage to
stay upright. At each obstacle, you have a chance of falling down
in the attempt.
    Well, good luck. Hope you can manage to figure it out!
            """)

            while 1 == 1:
                answer = input('Type m to go back to the main menu:')

                if answer == 'm':
                    Menu.run(1)
                else:
                    print('Please type an m')

        elif first_answer == 5:
            quit()

        else:
            print('The instructions were pretty specific. Please choose 1, 2, 3, or 4')
            Menu.run(1)


class Obstacle():
    """Parent class that creates each obstacle. There are 4 different
    types: Dash, Pole, Ramp, and Tunnel. They inherit fall chance and
    print/represent properties from the parent.

    Attributes:
    fall_chance - comes from the Game class during game creation

    Magic Methods:
    __str__
    __repr__"""
    def __init__(self, fall_chance):
        self.fall_chance = fall_chance
        pass

    def __str__(self):
        return self.type_obs

    def __repr__(self):
        return self.type_obs


class Dash(Obstacle):
    """Dash obstacles require the user to go under. They inherit fall
    chance and their print/represent properties from Obstacle.

    Attributes:
    obs_id - id number
    type_obs - it's 'graphic' representation (-)
    move_on - the required move (under)
    fall_chance - inherited from Obstacle

    Magic Methods:
    __str__ - inherited from Obstacle
    __repr__ - inherited from Obstacle"""

    def __init__(self, obs_id, fall_chance):
        super().__init__(fall_chance)
        self.obs_id = obs_id
        self.type_obs = '-'
        self.move_on = 'under'


class Pole(Obstacle):
    """Pole obstacles require the user to go around. They inherit fall
    chance and their print/represent properties from Obstacle.

    Attributes:
    obs_id - id number
    type_obs - it's 'graphic' representation (|)
    move_on - the required move (around)
    fall_chance - inherited from Obstacle

    Magic Methods:
    __str__ - inherited from Obstacle
    __repr__ - inherited from Obstacle"""

    def __init__(self, obs_id, fall_chance):
        super().__init__(fall_chance)
        self.obs_id = obs_id
        self.type_obs = '|'
        self.move_on = 'around'


class Ramp(Obstacle):
    """Ramp obstacles require the user to go over. They inherit fall
    chance and their print/represent properties from Obstacle.

    Attributes:
    obs_id - id number
    type_obs - it's 'graphic' representation (/)
    move_on - the required move (over)
    fall_chance - inherited from Obstacle

    Magic Methods:
    __str__ - inherited from Obstacle
    __repr__ - inherited from Obstacle"""
    def __init__(self, obs_id, fall_chance):
        super().__init__(fall_chance)
        self.obs_id = obs_id
        self.type_obs = '/'
        self.move_on = 'over'


class Tunnel(Obstacle):
    """Tunnel obstacles require the user to go through. They inherit fall
    chance and their print/represent properties from Obstacle.

    Attributes:
    obs_id - id number
    type_obs - it's 'graphic' representation (o)
    move_on - the required move (through)
    fall_chance - inherited from Obstacle

    Magic Methods:
    __str__ - inherited from Obstacle
    __repr__ - inherited from Obstacle"""
    def __init__(self, obs_id, fall_chance):
        super().__init__(fall_chance)
        self.obs_id = obs_id
        self.type_obs = 'o'
        self.move_on = 'through'


class Game:
    """The Game class utlizes the Obstacle child classes to create
    an instance of the game.

    Attributes:
    length - how long the game is
    items - list of each obstacle type
    board - the full 'game board'

    Magic Methods:
    __str__
    __repr__
    """
    def __init__(self, length, fall_chance):
        self.length = length
        self.items = [Dash, Pole, Ramp, Tunnel]
        self.board = [self.items[random.randrange(4)](i, fall_chance) for i in range(1, self.length+1)]

    def __str__(self):
        astring = ''
        for i in self.board:
            astring += str(i)
        return astring

    def __repr__(self):
        astring = ''
        for i in self.board:
            astring += str(i)
        return astring


class Model:
    """Model does not create instances, it just holds the percent
    chance of each move being called for each obstacle. Can be
    accessed through menu option 2."""
    perc_dash = {'under': .25, 'over': .25, 'around': .25, 'through': .25}
    perc_pole = {'under': .25, 'over': .25, 'around': .25, 'through': .25}
    perc_ramp = {'under': .25, 'over': .25, 'around': .25, 'through': .25}
    perc_tunnel = {'under': .25, 'over': .25, 'around': .25, 'through': .25}


class Learner:
    """This class calls the Game class to create a game instance
    and then learns the game.

    Attributes:
    game - game class instance
    num_attempts - number of times you've tried to complete the course
    location - what obstacle you're on
    max_loc - furthest you've gotten so far
    complete - flag on whether you've completed the course
    moves - list of moves to choose from

    Methods:
    new_game - creates a new game instance
    increase_perc - increases the chance of choosing a move
    decrease_perc - decreases the chance of choosing a move
    do_you_fall - tells whether you tripped
    weighted_dict_rand - randomly chooses from the weighted Model class
    solve_game - learns and (hopefully) solves the game

    Magic Methods:
    __str__
    __repr__"""
    def __init__(self, length = 30, fall_chance = 0.05):
        self.game = Game(length, fall_chance)
        self.num_attempts = 0
        self.location = 0
        self.max_loc = 0
        self.complete = 0
        self.moves = ['under','around','over', 'through']

    def new_game(self, length, fall_chance):
        self.num_attempts = 0
        self.game = Game(length, fall_chance)

    def increase_perc(self, perc_dict, to_increase):
        if perc_dict[to_increase] <= 0.97:
            for key in perc_dict:
                if key == to_increase:
                    perc_dict[key] += .03
                else:
                    perc_dict[key] -= .01
                    if perc_dict[key] < 0:
                        perc_dict[key] = 0
        else:
            for key in perc_dict:
                if key == to_increase:
                    perc_dict[key] = 1
                else:
                    perc_dict[key] = 0

    def decrease_perc(self, perc_dict, to_decrease):
        if perc_dict[to_decrease] >= 0.03:
            for key in perc_dict:
                if key == to_decrease:
                    perc_dict[key] -= .03
                else:
                    perc_dict[key] += .01
        elif perc_dict[to_decrease] < 0.03:
            for key in perc_dict:
                if key == to_decrease:
                    perc_dict[key] = 0
                else:
                    perc_dict[key] += .01

    def do_you_fall(self, board_space):
        if random.random() >= self.game.board[board_space].fall_chance:
            return False
        else:
            return True

    def weighted_dict_rand(self, perc_dict):
        rand_num = random.random()
        total = 0
        for key, val in perc_dict.items():
            total += val
            if rand_num <= total:
                return key

    def solve_game(self, num_times, print_flag = 1):
        m = Messages(self, print_flag)
        break_flag = 0
        for i in range(0, num_times):
            if break_flag:
                break
            self.num_attempts += 1
            self.location = 0
            for i in range(0, self.game.length):
                dict_choice = ''
                if self.game.board[i].type_obs == '-':
                    dict_choice = Model.perc_dash
                    message_func = m.dash_fail
                elif self.game.board[i].type_obs == '|':
                    dict_choice = Model.perc_pole
                    message_func = m.pole_fail
                elif self.game.board[i].type_obs == '/':
                    dict_choice = Model.perc_ramp
                    message_func = m.ramp_fail
                else:
                    dict_choice = Model.perc_tunnel
                    message_func = m.tunnel_fail
                move = self.weighted_dict_rand(dict_choice)
                fall = self.do_you_fall(i)
                if move == self.game.board[i].move_on and fall == False:
                    self.increase_perc(dict_choice, move)
                    self.location +=1
                    if self.location > self.max_loc:
                        self.max_loc = self.location
                    if self.location == self.game.length:
                        self.complete = 1
                        m.successful(self.num_attempts)
                        break_flag = 1
                        break
                elif move != self.game.board[i].move_on:
                    message_func(move)
                    self.decrease_perc(dict_choice, move)
                    break
                else:
                    m.fall(move)
                    self.decrease_perc(dict_choice, move)
                    break
        else:
            m.unsuccessful(self.num_attempts)

    def __str__(self):
        print_string = '\n' + ' '*self.location + '!' + '\n' + str(self.game)
        return print_string

    def __repr__(self):
        print_string = ''
        if self.location > 0:
            print_string = '\n' + ' '*self.location + '!' + '\n' + str(self.game)
        return print_string


class Messages:
    """The messages class holds all of the messages for after a course
    attempt. The instance is created in the 'solve_game' method of the
    Learner class.

    Attributes:
    print_flag - a 1 prints each move, a 0 only prints at the end
    learner - the Learner class instance for printing

    Methods:
    <obstacle>_fail - separate method for printing message for each obstacle
    fall - message for falling
    successful - message for completing the course
    unsuccessful - message for failing the course after all attempts"""
    def __init__(self, learner, print_flag):
        self.print_flag = print_flag
        self.learner = learner

    def dash_fail(self, move):
        if self.print_flag:
            print(self.learner)
            print(f'Ouch! You tried to go {move} the dash and impaled yourself on the pointy edge. Let\'s try that again.')

    def pole_fail(self, move):
        if self.print_flag:
            print(self.learner)
            print(f'Uh-oh. That hurt. Let\'s try not to go {move} any more poles, okay? Go get checked for a concussion and try again.')

    def ramp_fail(self, move):
        if self.print_flag:
            print(self.learner)
            print(f'C\'mon. It\'s a ramp. You should be able to figure this out. Stop trying to go {move} it. Go again.')

    def tunnel_fail(self, move):
        if self.print_flag:
            print(self.learner)
            print(f'Toddlers know to go through tunnels, but for some reason you tried to go {move} it. Try again.')

    def fall(self, move):
        if self.print_flag:
            print(self.learner)
            print(f'You fell. Maybe work on your \'going {move}\' skills a bit more.')

    def successful(self, num_moves):
        print(self.learner)
        print(f'You finally learned the obstacle course... it only took you {num_moves} tries!')

    def unsuccessful(self, num_moves):
        print(self.learner)
        print(f'Even after {num_moves} times, you never managed to complete the course. Wow.')


###---------------Main Code--------------###
Menu.run()
