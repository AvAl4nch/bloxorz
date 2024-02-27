class Player:

    def __init__(self, x_pos = 2, y_pos = 3, state = 'standing'):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.state = state

    def render(self):
        match self.state:
            case 'standing':
                return self.x_pos, self.y_pos, self.x_pos,  self.y_pos

            case 'over_y':
                return self.x_pos, self.y_pos, self.x_pos ,  self.y_pos + 1

            case 'over_x':
                return self.x_pos, self.y_pos, self.x_pos + 1,  self.y_pos


    def move_up(self):
        match self.state:

            case 'standing':
                self.x_pos -= 2
                self.state = 'over_x'

            case 'over_x':
                self.x_pos -= 1
                self.state = 'standing'

            case 'over_y':
                self.x_pos -= 1

    def move_down(self):
        match self.state:

            case 'standing':
                self.x_pos += 1
                self.state = 'over_x'

            case 'over_x':
                self.x_pos += 2
                self.state = 'standing'

            case 'over_y':
                self.x_pos += 1

    def move_right(self):
        match self.state:

            case 'standing':
                self.y_pos += 1
                self.state = 'over_y'

            case 'over_x':
                self.y_pos += 1

            case 'over_y':
                self.y_pos += 2
                self.state = 'standing'

    def move_left(self):
        match self.state:

            case 'standing':
                self.y_pos -= 2
                self.state = 'over_y'

            case 'over_x':
                self.y_pos -= 1

            case 'over_y':
                self.y_pos -= 1
                self.state = 'standing'



