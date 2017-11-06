def is_winnable(model, memo):

    # memoized case
    if model.board in memo:
        return True

    # base case
    w = won(model)
    if w == 1:
        return True
    if w == 2:
        return False


    # recursive case
    options = range(0, 5)
    for option in options:
        new_model = model.move(1, option)
        bools = [is_winnable(new_model.move(2, p_option), memo) for p_option in range(0, 5)]
        if all(bools):
            memo[model.board] = option
            return True
        # checking all(bools) assumes that the first player to move wins 100% of the time with optimal play on
        # both sides. This might not be the case, but I'll leave figuring out what to do then up to you. Try first
        # assuming this.
    return False  # if there is no move which wins 100% of the time.


def won(model):
    # returns a 0 if no player has won, 1 if player 1 has won, or 2 for player 2
    pass
