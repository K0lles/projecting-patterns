from abc import ABC, abstractmethod
from enum import Enum


class StateType(Enum):
    PLAYING = 1
    STOPPED = 2
    SKIP_FORWARD = 3
    SKIP_BACKWARD = 4


class IState:

    def __init__(self, allowed_states: list, current_state: StateType):
        self.current_state = current_state
        self.allowed_states = allowed_states

    def switch(self, state: StateType):
        state_dict = {
            StateType.PLAYING: PlayingState,
            StateType.STOPPED: StoppedState,
            StateType.SKIP_FORWARD: SkipForwardState,
            StateType.SKIP_BACKWARD: SkipBackwardState
        }
        return state_dict[state]()

    def __str__(self):
        return self.current_state


class PlayingState(IState):

    def __init__(self):
        super().__init__([StoppedState, SkipForwardState, SkipBackwardState], StateType.PLAYING)

    def __str__(self):
        super().__str__()


class StoppedState(IState):

    def __init__(self):
        super().__init__([StateType.PLAYING, StateType.SKIP_FORWARD, StateType.SKIP_BACKWARD], StateType.STOPPED)

    def __str__(self):
        super().__str__()


class SkipForwardState(IState):

    def __init__(self):
        super().__init__([StateType.PLAYING, StateType.STOPPED, StateType.SKIP_FORWARD, StateType.SKIP_BACKWARD],
                         StateType.SKIP_FORWARD)

    def __str__(self):
        super().__str__()


class SkipBackwardState(IState):

    def __init__(self):
        super().__init__([StateType.PLAYING, StateType.STOPPED, StateType.SKIP_FORWARD, StateType.SKIP_BACKWARD],
                         StateType.SKIP_BACKWARD)

    def __str__(self):
        super().__str__()


class AudioPlayer:

    def __init__(self, songs: list):
        self.songs: list = songs
        self.current_song = 0
        self.state: IState = PlayingState()

    def play(self):
        self.state = self.state.switch(StateType.PLAYING)
        print(f"{self.songs[self.current_song]} is playing now")

    def stop(self):
        self.state = self.state.switch(StateType.STOPPED)
        print(f"{self.songs[self.current_song]} is on stop now")

    def skip_forward(self):
        self.state = self.state.switch(StateType.SKIP_FORWARD)
        self.current_song += 1
        if self.current_song == len(self.songs):
            self.current_song = 0
        print(f"song switched forward to {self.songs[self.current_song]}")
        self.play()

    def skip_backward(self):
        self.state = self.state.switch(StateType.SKIP_BACKWARD)
        self.current_song -= 1
        if self.current_song <= 0:
            self.current_song = len(self.songs) - 1
        print(f"song switched backward to {self.songs[self.current_song]}")
        self.play()


if __name__ == '__main__':
    player = AudioPlayer(["Eminem", "Один в каное", "Lil Peep", "Святослав Вакарчук"])
    player.play()
    player.stop()
    player.play()
    player.skip_backward()
    player.skip_forward()
    player.skip_forward()
    player.skip_forward()
    player.skip_forward()
    player.skip_forward()
